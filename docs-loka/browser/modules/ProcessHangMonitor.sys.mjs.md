# browser/modules/ProcessHangMonitor.sys.mjs

source: browser/modules/ProcessHangMonitor.sys.mjs
source-hash: 2c9b2a18e7aa5a0819a3319acf934eef63f3b848
lines: 698

## <module>
- 役割: 親プロセスでコンテンツプロセスのスクリプトハング報告を受け、ユーザーに止めるか待つかを尋ねる通知を管理する

## elideMiddleOfString()
- 位置: L12-39
- 役割: 文字列が threshold を超えるとき中央を省略記号で置き換える。書記素クラスタを割らないよう境界を調整する
- 触るとき: タブ名などの長い文字列を通知文に入れる幅を変えるとき。threshold の半分から 5 を引いた長さが 5 未満なら元の文字列を返す
- 呼び出し先: `searchElisionPoint()`
- 条件付き依存: `if (elisionStart < elisionEnd)` → `str.slice()`
- 参照: `str.length`

## searchElisionPoint()
- 位置: L19-31
- 役割: 省略の切れ目の位置を、前後 5 文字の範囲で結合文字やサロゲートでない所に寄せる
- 触るとき: 省略で絵文字や結合文字が壊れる問題を調べるとき
- 呼び出し先: `unsplittableCharacter()`

## unsplittableCharacter()
- 位置: L20-20
- 役割: 結合文字(\p{M})とサロゲートの下位半分に当たる文字かどうかを判定する
- 触るとき: 割ってはいけない文字の判定条件を変えるとき
- 呼び出し先: `/[\p{M}\uDC00-\uDFFF]/u.test()`

## WAIT_EXPIRATION_TIME()
- 位置: L52-58
- 役割: 「待つ」を選んだ後に再通知を止める時間を、browser.hangNotification.waitPeriod から読む
- 触るとき: 待機時間の既定値や pref 名を確認・変更するとき。pref が読めない場合は 10000 ミリ秒を返す
- 呼び出し先: `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## init()
- 位置: L88-94
- 役割: ハング報告・ハング解除・終了開始・xpcom 終了の各オブザーバーと、ウィンドウ通知を登録する
- 触るとき: ハング監視の起動経路を調べるとき。親プロセスの初期化時に 1 回だけ呼ばれる
- 呼び出し先: `Services.obs.addObserver()`, `Services.ww.registerNotification()`
- XPCOM: `Services.obs` / `Services.ww`

## terminateScript()
- 位置: L100-102
- 役割: 選択中タブのハング報告を取り出し、そのスクリプトを停止する
- 触るとき: 通知の「停止」ボタンや終了時の強制停止の経路を変えるとき
- 呼び出し先: `report.terminateScript()`, `this.handleUserInput()`

## debugScript()
- 位置: L108-123
- 役割: 選択中タブのハング報告についてスローススクリプトのデバッガを起動し、終了時のコールバックを渡す
- 触るとき: 通知の「デバッグ」ボタンの動作や、デバッガ起動時のテレメトリを変えるとき
- 呼び出し先: `Cc["@mozilla.org/dom/slow-script-debug;1"].getService()`, `handler.handleSlowScriptDebug()`, `report.beginStartingDebugger()`, `this._recordTelemetryForReport()`, `this.handleUserInput()`
- 参照: `Ci.nsISlowScriptDebug`, `report.scriptBrowser`, `svc.remoteActivationHandler`
- XPCOM: [`nsISlowScriptDebug`](../../dom/base/nsISlowScriptDebug.idl.md) / `@mozilla.org/dom/slow-script-debug;1` → `SlowScriptDebug` (dom/base/components.conf)

## callback()
- 位置: L110-112
- 役割: デバッガ起動の完了を報告に伝える
- 触るとき: デバッガ起動が完了しないまま残る問題を調べるとき
- 呼び出し先: `report.endStartingDebugger()`

## stopIt()
- 位置: L129-137
- 役割: 選択中タブのアクティブなハング報告に「利用者が中止」を記録し、スクリプトを停止する
- 触るとき: ユーザーが「停止」を押した後の処理順序や記録される終了理由を変えるとき
- 呼び出し先: `this._recordTelemetryForReport()`, `this.findActiveReport()`, `this.terminateScript()`
- 参照: `win.gBrowser.selectedBrowser`

## stopHang()
- 位置: L143-146
- 役割: 終了理由をテレメトリに記録してから、報告のスクリプトを停止する。UI は更新しない
- 触るとき: ハングを UI に出さずに止める経路(ウィンドウ終了、終了処理など)を調べるとき
- 呼び出し先: `report.terminateScript()`, `this._recordTelemetryForReport()`

## waitLonger()
- 位置: L152-194
- 役割: アクティブな報告を待機リストへ移し、待機時間の one-shot タイマーを張って通知を消す
- 触るとき: 通知の「待つ」(閉じる)操作や、再通知までの間隔を変えるとき。タイマー満了時に、まだハングしていれば再びアクティブに戻す
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `this._activeReports.get()`, `this._pausedReports.set()`, `this.findActiveReport()`, `this.removeActiveReport()`, `this.updateWindows()`, `timer.initWithCallback()`
- 条件付き依存: `if (pausedInfo.timer === timer)` → `this.removePausedReport()`
- 条件付き依存: `if (pausedInfo.timer === timer)` → `this._activeReports.set()`
- 条件付き依存: `if (pausedInfo.timer === timer)` → `this.updateWindows()`
- 参照: `Ci.nsITimer`, `pausedInfo.timer`, `reportInfo.timer`, `reportInfo.waitCount`, `this.WAIT_EXPIRATION_TIME`, `this._pausedReports`, `timer.TYPE_ONE_SHOT`, `win.gBrowser.selectedBrowser`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## handleUserInput()
- 位置: L201-209
- 役割: 選択中タブのアクティブな報告を外し、渡された関数をその報告に対して実行する
- 触るとき: 通知のボタン操作がどの報告に作用するかを確認するとき。報告が無ければ null を返す
- 呼び出し先: `func()`, `this.findActiveReport()`, `this.removeActiveReport()`
- 参照: `win.gBrowser.selectedBrowser`

## observe()
- 位置: L211-255
- 役割: オブザーバーの通知種別ごとに、終了処理・ハング報告・ハング解除・ウィンドウ開閉の処理へ振り分ける
- 触るとき: 新しい通知種別を監視に加えるとき、または特定のイベントで処理が走らない問題を見るとき
- 呼び出し先: `Services.obs.removeObserver()`, `Services.ww.unregisterNotification()`, `subject.QueryInterface()`, `this.clearHang()`, `this.onQuitApplicationGranted()`, `this.onWindowClosed()`, `this.reportHang()`, `win.addEventListener()`
- 参照: `Ci.nsIHangReport`
- XPCOM: [`nsIHangReport`](../../dom/ipc/nsIHangReport.idl.md) / `Services.obs` / `Services.ww`

## listener()
- 位置: L241-244
- 役割: 新しく開いたウィンドウの読み込み完了時に、ハング通知を更新する
- 触るとき: 起動直後に開いたウィンドウに既存のハングが表示されない問題を調べるとき
- 呼び出し先: `this.updateWindows()`, `win.removeEventListener()`

## onQuitApplicationGranted()
- 位置: L263-267
- 役割: 終了が許可されたら終了中フラグを立て、すべてのハングを停止して通知を更新する
- 触るとき: 終了時にハングが残ったり、終了が遅れたりする問題を調べるとき
- 呼び出し先: `this.stopAllHangs()`, `this.updateWindows()`
- 参照: `this._shuttingDown`

## onWindowClosed()
- 位置: L269-302
- 役割: 閉じたウィンドウに属するアクティブ・待機中のハングを停止し、リストから外す
- 触るとき: ウィンドウを閉じた後にハング通知や待機タイマーが残る問題を調べるとき
- 呼び出し先: `maybeStopHang()`, `this.updateWindows()`
- 条件付き依存: `if (maybeStopHang(report))` → `this._activeReports.delete()`
- 条件付き依存: `if (maybeStopHang(pausedReport))` → `this.removePausedReport()`
- 参照: `this._activeReports`, `this._pausedReports`

## maybeStopHang()
- 位置: L270-285
- 役割: 報告のスクリプトブラウザのウィンドウが閉じたウィンドウか、取得できない場合にハングを停止する
- 触るとき: どの報告を閉じたウィンドウの分とみなすかの判定条件を変えるとき。取得に失敗したら安全側で止める
- 条件付き依存: `if (!hungBrowserWindow || hungBrowserWindow == win)` → `this.stopHang()`
- 参照: `report.scriptBrowser.documentGlobal`

## stopAllHangs()
- 位置: L304-315
- 役割: すべてのアクティブ・待機中のハングを、指定の終了理由で停止して両方のリストを空にする
- 触るとき: 終了時やウィンドウが無くなったときのハング一括停止の動作を変えるとき
- 呼び出し先: `this.removePausedReport()`, `this.stopHang()`
- 参照: `this._activeReports`, `this._pausedReports`

## findActiveReport()
- 位置: L320-328
- 役割: 指定の browser に属する(子を含む)アクティブなハング報告を探す
- 触るとき: 選択中のタブにハングがあるかを判定する経路を調べるとき
- 呼び出し先: `report.isReportForBrowserOrChildren()`, `this._activeReports.keys()`
- 参照: `browser.frameLoader`

## findPausedReport()
- 位置: L333-341
- 役割: 指定の browser に属する待機中のハング報告を探す
- 触るとき: タブ切り替え時に待機中の報告を引き継ぐ処理を変えるとき
- 呼び出し先: `report.isReportForBrowserOrChildren()`
- 参照: `browser.frameLoader`, `this._pausedReports`

## _recordTelemetryForReport()
- 位置: L346-405
- 役割: ハングの発生元(拡張機能、devtools、pdf.js、ブラウザ、コンテンツ)を判定し、継続時間などを Glean の slowScriptWarning に記録する
- 触るとき: ハング関連のテレメトリ項目や区分を追加・変更するとき。記録できない場合は例外を握りつぶして console.error に出す
- 呼び出し先: `ChromeUtils.now()`, `Glean.slowScriptWarning.shownContent.record()`, `console.error()`, `this._activeReports.get()`, `this._pausedReports.get()`
- 条件付き依存: `if (!(report.addonId))` → `report.scriptFileName?.startsWith()`
- 条件付き依存: `if (!(report.scriptFileName?.startsWith("debugger")))` → `report.scriptFileName?.startsWith()`
- 条件付き依存: `if (!( report.scriptFileName?.startsWith( "resource://pdf.js/build/pdf.scripting.mjs" ) ))` → `console.error()`
- 条件付き依存: `if (info.notificationTime)` → `ChromeUtils.now()`
- 参照: `info.deselectCount`, `info.lastReportFromChild`, `info.notificationTime`, `info.waitCount`, `report.addonId`, `report.hangDuration`, `report.scriptFileName`, `url.protocol`

## removeActiveReport()
- 位置: L411-414
- 役割: アクティブな報告をリストから外し、ウィンドウの通知を更新する
- 触るとき: 報告の解除後に通知表示がずれる問題を調べるとき
- 呼び出し先: `this._activeReports.delete()`, `this.updateWindows()`

## removePausedReport()
- 位置: L420-424
- 役割: 待機中の報告のタイマーを止め、リストから外す
- 触るとき: 待機タイマーが残ったまま再通知される問題を調べるとき
- 呼び出し先: `info?.timer?.cancel()`, `this._pausedReports.delete()`, `this._pausedReports.get()`

## updateWindows()
- 位置: L432-453
- 役割: 開いているすべてのブラウザウィンドウの通知を更新し、アクティブな報告があれば監視を付ける。ウィンドウが無ければ全停止する
- 触るとき: 通知の再描画の起点を変えるとき。macOS でウィンドウが 0 個のときは利用者に尋ねられないので停止する
- 呼び出し先: `Services.wm.getEnumerator()`, `e.hasMoreElements()`, `this.updateWindow()`
- 条件付き依存: `if (!e.hasMoreElements())` → `this.stopAllHangs()`
- 条件付き依存: `if (this._activeReports.size)` → `this.trackWindow()`
- 条件付き依存: `if (!(this._activeReports.size))` → `this.untrackWindow()`
- 参照: `this._activeReports.size`
- XPCOM: `Services.wm`

## updateWindow()
- 位置: L458-470
- 役割: 選択中タブの報告があれば通知を出し、無ければ通知を消す。初回表示時刻を記録する
- 触るとき: タブ選択後に通知が正しいタブに対応するかを確認するとき
- 呼び出し先: `this.findActiveReport()`
- 条件付き依存: `if (report)` → `this._activeReports.get()`
- 条件付き依存: `if (info && !info.notificationTime)` → `ChromeUtils.now()`
- 条件付き依存: `if (report)` → `this.showNotification()`
- 条件付き依存: `if (!(report))` → `this.hideNotification()`
- 参照: `info.notificationTime`, `win.gBrowser.selectedBrowser`

## showNotification()
- 位置: async L475-592
- 役割: 報告の種類(拡張機能、選択中タブ、別タブ、特定できないタブ)に応じた文言とボタンを作り、process-hang 通知を出す
- 触るとき: 通知の文言、ボタン、デバッグボタンの出す条件を変えるとき。開発版と Nightly、または devtools が監視中のときだけデバッグボタンを付け、ポリシーで無効なら付けない
- 呼び出し先: `Services.prefs.getBoolPref()`, `bundle.getString()`, `console.warn()`, `doc .getElementById()`, `doc .getElementById("bundle_brand") .getString()`, `hangNotification.setAttribute()`, `notification?.getAttribute()`, `win.gNotificationBox.appendNotification()`, `win.gNotificationBox.getNotificationWithValue()`
- 条件付き依存: `if (report.addonId)` → `Cc["@mozilla.org/addons/policy-service;1"].getService()`
- 条件付き依存: `if (report.addonId)` → `aps.getExtensionName()`
- 条件付き依存: `if (report.addonId)` → `bundle.getFormattedString()`
- 条件付き依存: `if (report.addonId)` → `buttons.unshift()`
- 条件付き依存: `if (report.addonId)` → `bundle.getString()`
- 条件付き依存: `if (scriptBrowser == win.gBrowser?.selectedBrowser)` → `bundle.getFormattedString()`
- 条件付き依存: `if (!(scriptBrowser == win.gBrowser?.selectedBrowser))` → `scriptBrowser?.documentGlobal.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (!tab)` → `bundle.getFormattedString()`
- 条件付き依存: `if (!(!tab))` → `scriptBrowser.browserId.toString()`
- 条件付き依存: `if (!(!tab))` → `tab.getAttribute()`
- 条件付き依存: `if (!(!tab))` → `elideMiddleOfString()`
- 条件付き依存: `if (!(!tab))` → `bundle.getFormattedString()`
- 条件付き依存: `if (notification)` → `notification.setAttribute()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("devtools.policy.disabled", false) && (AppConstants.MOZ_DEV_EDITION || AppConstants.NIGHTLY_BUILD || report.scriptBrowser.browsi...)` → `buttons.push()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("devtools.policy.disabled", false) && (AppConstants.MOZ_DEV_EDITION || AppConstants.NIGHTLY_BUILD || report.scriptBrowser.browsi...)` → `bundle.getString()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `AppConstants.NIGHTLY_BUILD`, `Ci.nsIAddonPolicyService`, `notification.label`, `report.addonId`, `report.scriptBrowser`, `report.scriptBrowser.browsingContext.watchedByDevTools`, `win.document`, `win.gBrowser?.selectedBrowser`, `win.gNavigatorBundle`, `win.gNotificationBox.PRIORITY_INFO_HIGH`
- XPCOM: `nsIAddonPolicyService` / `@mozilla.org/addons/policy-service;1` / `Services.prefs`

## callback()
- 位置: L482-484
- 役割: 通知の「停止」ボタンから、そのウィンドウのハングを中止させる
- 触るとき: 停止ボタンの押下後の処理を変えるとき
- 呼び出し先: `ProcessHangMonitor.stopIt()`

## callback()
- 位置: L565-567
- 役割: 通知の「デバッグ」ボタンから、そのウィンドウのスクリプトデバッガを起動する
- 触るとき: デバッグボタンの押下後の処理を変えるとき
- 呼び出し先: `ProcessHangMonitor.debugScript()`

## eventCallback()
- 位置: L580-584
- 役割: 通知が閉じられた(dismissed)ときに、そのハングを待機リストへ移す
- 触るとき: 通知を閉じた後に再び通知が出る条件を変えるとき
- 条件付き依存: `if (event == "dismissed")` → `ProcessHangMonitor.waitLonger()`

## hideNotification()
- 位置: L597-603
- 役割: ウィンドウから process-hang 通知を取り除く
- 触るとき: ハングの無いタブに切り替えた後も通知が残る問題を調べるとき
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `win.gNotificationBox.removeNotification()`

## trackWindow()
- 位置: L609-616
- 役割: タブ選択とタブのリモート性変更のイベントを、タブコンテナーに登録する
- 触るとき: 通知をタブ切り替えに追従させる仕組みを変えるとき
- 呼び出し先: `win.gBrowser.tabContainer.addEventListener()`

## untrackWindow()
- 位置: L618-625
- 役割: trackWindow で登録したタブ選択とリモート性変更のイベントを外す
- 触るとき: アクティブな報告が無くなったウィンドウでイベントが残る問題を調べるとき
- 呼び出し先: `win.gBrowser.tabContainer.removeEventListener()`

## handleEvent()
- 位置: L627-646
- 役割: タブ選択時は前のタブの報告に切り替え回数を加え、選択とリモート性変更の両方で通知を更新する
- 触るとき: タブ切り替えの回数(n_tab_deselect)の数え方や、切り替えに伴う通知更新を変えるとき
- 条件付き依存: `if (event.type == "TabSelect" && event.detail.previousTab)` → `this.findActiveReport()`
- 条件付き依存: `if (event.type == "TabSelect" && event.detail.previousTab)` → `this.findPausedReport()`
- 条件付き依存: `if (r)` → `this._activeReports.get()`
- 条件付き依存: `if (r)` → `this._pausedReports.get()`
- 条件付き依存: `if (event.type == "TabSelect" || event.type == "TabRemotenessChange")` → `this.updateWindow()`
- 参照: `event.detail.previousTab`, `event.detail.previousTab.linkedBrowser`, `event.target.documentGlobal`, `event.type`, `info.deselectCount`

## reportHang()
- 位置: L652-688
- 役割: 新しいハング報告をアクティブに登録して通知を更新する。既知の報告は最終報告時刻だけ更新し、終了中なら即停止する
- 触るとき: コンテンツプロセスからのハング報告の扱いを変えるとき。slowScriptNoticeCount は新規の報告時だけ加算する
- 呼び出し先: `ChromeUtils.now()`, `Glean.dom.slowScriptNoticeCount.add()`, `this._activeReports.has()`, `this._activeReports.set()`, `this._pausedReports.has()`, `this.updateWindows()`
- 条件付き依存: `if (this._shuttingDown)` → `this.stopHang()`
- 条件付き依存: `if (this._activeReports.has(report))` → `this._activeReports.get()`
- 条件付き依存: `if (this._activeReports.has(report))` → `this.updateWindows()`
- 条件付き依存: `if (this._pausedReports.has(report))` → `this._pausedReports.get()`
- 参照: `this._activeReports.get(report).lastReportFromChild`, `this._pausedReports.get(report).lastReportFromChild`, `this._shuttingDown`

## clearHang()
- 位置: L690-696
- 役割: 報告を「解除」として記録し、アクティブと待機の両方から外してから、報告側へキャンセルを通知する
- 触るとき: コンテンツ側でハングが解消されたときの後始末を変えるとき
- 呼び出し先: `report.userCanceled()`, `this._recordTelemetryForReport()`, `this.removeActiveReport()`, `this.removePausedReport()`
