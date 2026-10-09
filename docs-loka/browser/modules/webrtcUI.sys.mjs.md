# browser/modules/webrtcUI.sys.mjs

source: browser/modules/webrtcUI.sys.mjs
source-hash: cc85adce900d89042cf01bf277904c59d77cf7e9
lines: 1107

## <module>
- 役割: WebRTCでカメラ・マイク・画面を共有しているタブを追跡し、タブ別・全体の共有インジケーターと共有メニュー、停止・権限の処理をまとめるモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## init()
- 位置: L87-104
- 役割: ウィンドウ起動完了の通知を一度だけ登録し、macOS 14以上でインジケーターを出すかのprefなどを遅延取得の設定にする。
- 触るとき: インジケーター関連のprefの読み込み方や、起動時の初期化順序を変えるとき。
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.initialized)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## uninit()
- 位置: L106-111
- 役割: 初期化済みなら起動完了通知の登録を外す。
- 触るとき: webrtcUIの後始末や再初期化の挙動を調べるとき。
- 条件付き依存: `if (this.initialized)` → `Services.obs.removeObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L113-119
- 役割: 起動完了通知を受けたとき、共有中ならそのウィンドウに共有メニューを作る。
- 触るとき: 起動直後のウィンドウで共有メニューが出ない問題を調べるとき。
- 条件付き依存: `if (webrtcUI.showGlobalIndicator)` → `showOrCreateMenuForWindow()`
- 参照: `webrtcUI.showGlobalIndicator`

## showGlobalIndicator()
- 位置: L139-150
- 役割: いずれかのタブにカメラ・マイク・画面共有のインジケーターが必要なら真を返す。
- 触るとき: 全体インジケーター(ツールバーのメニューやインジケーターウィンドウ)を出す条件を変えるとき。
- 参照: `indicators.showCameraIndicator`, `indicators.showMicrophoneIndicator`, `indicators.showScreenSharingIndicator`, `this.perTabIndicators`

## showCameraIndicator()
- 位置: L152-168
- 役割: macOS 14以上でpref無効なら偽。それ以外は、いずれかのタブでカメラ表示が必要なら真を返す。
- 触るとき: カメラ使用中のインジケーター表示条件や、macOS 14の抑止条件を変えるとき。
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`
- 参照: `indicators.showCameraIndicator`, `this.perTabIndicators`, `this.showIndicatorsOnMacos14AndAbove`

## showMicrophoneIndicator()
- 位置: L170-186
- 役割: macOS 14以上でpref無効なら偽。それ以外は、いずれかのタブでマイク表示が必要なら真を返す。
- 触るとき: マイク使用中のインジケーター表示条件や、macOS 14の抑止条件を変えるとき。
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`
- 参照: `indicators.showMicrophoneIndicator`, `this.perTabIndicators`, `this.showIndicatorsOnMacos14AndAbove`

## showScreenSharingIndicator()
- 位置: L188-212
- 役割: macOS 14以上でpref無効なら空文字。それ以外は、タブごとの共有種別のうち優先度の高いもの(Screen, Window, Application, Browser)を返す。
- 触るとき: 画面共有の種別によってインジケーターの文言を切り替える処理を変えるとき。
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`, `list.sort()`, `precedence.indexOf()`
- 条件付き依存: `if (indicators.showScreenSharingIndicator)` → `list.push()`
- 参照: `indicators.showScreenSharingIndicator`, `this.perTabIndicators`, `this.showIndicatorsOnMacos14AndAbove`

## getActiveStreams()
- 位置: L216-249
- 役割: 引数で指定された種別(カメラ・マイク・画面・タブ・ウィンドウ)を含む共有ストリームを抜き出し、URI・タブ・ブラウザ・種別・デバイスの組にして返す。
- 触るとき: 共有メニューや停止処理に渡す対象ストリームの絞り込みを変えるとき。
- 呼び出し先: `browser?.documentGlobal.gBrowser?.getTabForBrowser()`, `webrtcUI._streams .filter()`
- 参照: `aStream.state`, `aStream.topBrowsingContext.embedderElement`, `state.browser`, `state.camera`, `state.devices`, `state.documentURI`, `state.microphone`, `state.screen`, `state.window`

## browserHasStreams()
- 位置: L254-262
- 役割: 指定ブラウザの最上位ブラウジングコンテキストに、共有中のストリームがあるかを返す。
- 触るとき: タブが共有中かどうかで表示や警告を分ける箇所を追うとき。
- 参照: `stream.topBrowsingContext.embedderElement`, `this._streams`

## getCombinedStateForBrowser()
- 位置: L268-371
- 役割: 最上位ブラウジングコンテキストの全ストリームの状態をまとめ、画面共有の種別・一時停止・どのインジケーターを出すかを決める。
- 触るとき: タブ単位の共有状態(一時停止を含む)やインジケーターの判定を変えるとき。
- 呼び出し先: `tabState.screen.includes()`
- 条件付き依存: `if (stream.topBrowsingContext == aTopBrowsingContext)` → `combine()`
- 条件付き依存: `if (tabState.screen)` → `tabState.screen.startsWith()`
- 条件付き依存: `if (!(tabState.screen.startsWith("Screen")))` → `tabState.screen.startsWith()`
- 条件付き依存: `if (!(tabState.screen.startsWith("Window")))` → `tabState.screen.startsWith()`
- 参照: `Ci.nsIMediaManagerService.STATE_CAPTURE_DISABLED`, `Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED`, `stream.state.browser`, `stream.state.camera`, `stream.state.microphone`, `stream.state.screen`, `stream.state.window`, `stream.topBrowsingContext`, `tabState.camera`, `tabState.microphone`, `tabState.paused`, `tabState.screen`, `tabState.sharing`, `tabState.showCameraIndicator`, `tabState.showMicrophoneIndicator`, `tabState.showScreenSharingIndicator`, `this._streams`
- XPCOM: [`nsIMediaManagerService`](../../dom/media/nsIMediaManager.idl.md)

## combine()
- 位置: L269-283
- 役割: 2つの捕捉状態を合成する。有効が最優先、次いで無効、どちらでもなければ非捕捉。
- 触るとき: 複数ストリームの捕捉状態をまとめる優先順位を変えるとき。
- 参照: `Ci.nsIMediaManagerService.STATE_CAPTURE_DISABLED`, `Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED`, `Ci.nsIMediaManagerService.STATE_NOCAPTURE`
- XPCOM: [`nsIMediaManagerService`](../../dom/media/nsIMediaManager.idl.md)

## streamAddedOrRemoved()
- 位置: L379-495
- 役割: ストリームを追加または削除し、画面・ウィンドウ共有の有無を再計算して、タブ切り替え警告の許可リストやシステム通知の抑止を更新する。
- 触るとき: 共有の開始・停止時に警告状態がリセットされない、または通知が抑止されない問題を調べるとき。(scaryなデバイスのみ判定対象)
- 呼び出し先: `Services.prefs.getBoolPref()`, `sharedWindowRawDeviceIds.has()`, `this._setSharedData()`, `this.init()`
- 条件付き依存: `if (index < this._streams.length)` → `this._streams.splice()`
- 条件付き依存: `if (mediaSource == "window")` → `sharedWindowRawDeviceIds.add()`
- 条件付き依存: `if (browser.permanentKey)` → `this.allowedSharedBrowsers.add()`
- 条件付き依存: `if (sharedWindowRawDeviceIds.has(rawDeviceId))` → `this.sharedBrowserWindows.add()`
- 条件付き依存: `if (sharedWindowRawDeviceIds.has(rawDeviceId))` → `this.allowedSharedBrowsers.add()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "privacy.webrtc.allowSilencingNotifications", false ) )` → `Cc["@mozilla.org/alerts-service;1"] .getService(Ci.nsIAlertsService) .QueryInterface()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "privacy.webrtc.allowSilencingNotifications", false ) )` → `Cc["@mozilla.org/alerts-service;1"] .getService()`
- 参照: `Ci.nsIAlertsDoNotDisturb`, `Ci.nsIAlertsService`, `aBrowsingContext.top`, `aData.remove`, `alertsService.suppressForScreenSharing`, `browser.permanentKey`, `device.mediaSource`, `device.rawId`, `device.scary`, `lazy.BrowserWindowTracker.orderedWindows`, `selectedBrowser.permanentKey`, `state.devices`, `state.suppressNotifications`, `stream.browsingContext`, `stream.topBrowsingContext.embedderElement`, `this._streams`, `this._streams.length`, `this.allowTabSwitchesForSession`, `this.allowedSharedBrowsers`, `this.sharedBrowserWindows`, `this.sharingScreen`, `this.tabSwitchCountForSession`, `webrtcUI._streams.length`, `win.gBrowser.selectedBrowser`, `win.windowUtils.webrtcRawDeviceId`
- XPCOM: [`nsIAlertsDoNotDisturb`](../../toolkit/components/alerts/nsIAlertsService.idl.md) / [`nsIAlertsService`](../../toolkit/components/alerts/nsIAlertsService.idl.md) / `@mozilla.org/alerts-service;1` / `Services.prefs`

## forgetStreamsFromBrowserContext()
- 位置: L501-526
- 役割: 指定のブラウジングコンテキストのストリームを外し、不要になったタブのインジケーターを消して全体表示を更新する。
- 触るとき: ページが閉じたり遷移したときに共有表示が残る問題を調べるとき。
- 呼び出し先: `this._setSharedData()`, `this.perTabIndicators.has()`, `this.updateGlobalIndicator()`
- 条件付き依存: `if (stream.browsingContext == aBrowsingContext)` → `this._streams.splice()`
- 条件付き依存: `if (this.perTabIndicators.has(topBC))` → `this.getCombinedStateForBrowser()`
- 条件付き依存: `if ( !tabState.showCameraIndicator && !tabState.showMicrophoneIndicator && !tabState.showScreenSharingIndicator )` → `this.perTabIndicators.delete()`
- 参照: `aBrowsingContext.top`, `stream.browsingContext`, `tabState.showCameraIndicator`, `tabState.showMicrophoneIndicator`, `tabState.showScreenSharingIndicator`, `this._streams`, `webrtcUI._streams.length`

## stopSharingStreams()
- 位置: L546-583
- 役割: 渡されたストリームの共有を、指定された種別で停止する。最後のストリームのタブを選択して前面に出す。種別の既定は全てtrue。
- 触るとき: 共有の停止ボタンや停止後のフォーカス先の挙動を変えるとき。
- 呼び出し先: `browserToSelect.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `this.clearPermissionsAndStopSharing()`, `window.focus()`
- 条件付き依存: `if (stopCameras)` → `ids.push()`
- 条件付き依存: `if (stopMics)` → `ids.push()`
- 条件付き依存: `if (stopScreens || stopWindows)` → `ids.push()`
- 参照: `activeStreams.length`, `browserToSelect.documentGlobal`, `gBrowser.selectedTab`

## clearPermissionsAndStopSharing()
- 位置: L593-658
- 役割: 種別が不正なら例外。該当するサイト権限を削除し、有効な共有があればWebRTCに停止を送る。カメラとマイクは片方だけ止めない。
- 触るとき: 権限の取り消しと共有停止の対象の決め方を変えるとき。
- 呼び出し先: `["camera", "screen", "microphone", "speaker"].includes()`, `actor.sendAsyncMessage()`, `lazy.SitePermissions.getAllForBrowser()`, `lazy.SitePermissions.removeFromPrincipal()`, `perm.id.split()`, `perms .filter()`, `sharingState.browsingContext.currentWindowGlobal.getActor()`, `types.filter()`, `types.includes()`, `webrtcUI.forgetActivePermissionsFromBrowser()`, `windowIds.forEach()`
- 条件付き依存: `if (invalidTypes.length)` → `invalidTypes.join()`
- 条件付き依存: `if (types.includes("screen") && sharingState.screen)` → `windowIds.push()`
- 条件付き依存: `if (sharingCameraOrMic)` → `windowIds.push()`
- 参照: `browser._sharingState?.webRTC`, `browser.contentPrincipal`, `invalidTypes.length`, `lazy.SitePermissions.PERM_KEY_DELIMITER`, `perm.id`, `sharingState.screen`, `sharingState?.camera`, `sharingState?.microphone`, `sharingState?.windowId`, `windowIds.length`

## updateIndicators()
- 位置: L660-677
- 役割: タブごとのインジケーター状態を保存し、全体表示を更新する。
- 触るとき: タブ単位のインジケーター情報が古い問題を調べるとき。
- 呼び出し先: `this.getCombinedStateForBrowser()`, `this.perTabIndicators.has()`, `this.updateGlobalIndicator()`
- 条件付き依存: `if (this.perTabIndicators.has(aTopBrowsingContext))` → `this.perTabIndicators.get()`
- 条件付き依存: `if (!(this.perTabIndicators.has(aTopBrowsingContext)))` → `this.perTabIndicators.set()`
- 参照: `indicators.showCameraIndicator`, `indicators.showMicrophoneIndicator`, `indicators.showScreenSharingIndicator`, `tabState.showCameraIndicator`, `tabState.showMicrophoneIndicator`, `tabState.showScreenSharingIndicator`

## swapBrowserForNotification()
- 位置: L679-685
- 役割: タブのブラウザが入れ替わったとき、ストリームの記録を新しいブラウザに付け替える。
- 触るとき: タブの移動や差し替えの後に共有の停止や選択が効かない問題を調べるとき。
- 参照: `stream.browser`, `this._streams`

## forgetActivePermissionsFromBrowser()
- 位置: L695-702
- 役割: ブラウザとその子フレームのウィンドウIDに対応するactivePermsの記録を削除する。
- 触るとき: 共有停止時に、権限パネルが古い状態を持ち続ける問題を調べるとき。
- 呼び出し先: `aBrowser.browsingContext .getAllBrowsingContextsInSubtree()`, `aBrowser.browsingContext .getAllBrowsingContextsInSubtree() .map()`, `aBrowser.browsingContext .getAllBrowsingContextsInSubtree() .map(bc => bc.currentWindowGlobal?.outerWindowId) .filter()`, `browserWindowIds.forEach()`, `browserWindowIds.push()`, `this.activePerms.delete()`
- 参照: `aBrowser.outerWindowId`, `bc.currentWindowGlobal?.outerWindowId`

## showSharingDoorhanger()
- 位置: L712-737
- 役割: 対象タブを選択してウィンドウを前面に出し、権限パネルを開く。macOSで非アクティブなら前面化を待ってから開く。
- 触るとき: 共有の権限パネルを開くまでの前面化や選択の手順を変えるとき。
- 呼び出し先: `browserWindow.focus()`, `browserWindow.gPermissionPanel.openPopup()`
- 条件付き依存: `if (!(aActiveStream.tab))` → `aActiveStream.browser.focus()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `browserWindow.addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `browserWindow.gPermissionPanel.openPopup()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService(Ci.nsIMacDockSupport) .activateApplication()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService()`
- 参照: `AppConstants.platform`, `Ci.nsIMacDockSupport`, `Services.focus.activeWindow`, `aActiveStream.browser.documentGlobal`, `aActiveStream.tab`, `browserWindow.gBrowser.selectedTab`
- XPCOM: `nsIMacDockSupport` / `@mozilla.org/widget/macdocksupport;1` / `Services.focus` / `Services.tm`

## updateWarningLabel()
- 位置: L739-744
- 役割: 選択中のデバイス種別が画面なら、全ウィンドウ共有の注意表示を出す。
- 触るとき: 共有対象の選択メニューの注意文言の出し方を変えるとき。
- 呼び出し先: `aMenuList.selectedItem.getAttribute()`, `document.getElementById()`
- 参照: `aMenuList.ownerDocument`, `document.getElementById("webRTC-all-windows-shared").hidden`

## addPeerConnectionBlocker()
- 位置: L770-772
- 役割: 接続を拒否するかを判定するコールバックを登録する。
- 触るとき: アドオンが接続許可の判定を追加するための口を変えるとき。
- 呼び出し先: `this.peerConnectionBlockers.add()`

## removePeerConnectionBlocker()
- 位置: L774-776
- 役割: 登録済みの接続判定コールバックを外す。
- 触るとき: アドオンが判定を外したときに残らないかを調べるとき。
- 呼び出し先: `this.peerConnectionBlockers.delete()`

## on()
- 位置: L778-780
- 役割: 内部のイベント発行器に、接続イベントの購読を登録する。
- 触るとき: peer-request系のイベント通知を追加・変更するとき。
- 呼び出し先: `this.emitter.on()`

## off()
- 位置: L782-784
- 役割: 内部のイベント発行器から購読を外す。
- 触るとき: イベント購読の解除の挙動を調べるとき。
- 呼び出し先: `this.emitter.off()`

## getHostOrExtensionName()
- 位置: L786-809
- 役割: アドオン名があればそれを、なければホスト名を返す。about:はハッシュを除いたURI全体、取れなければ不明ホストの文言を使う。
- 触るとき: 共有メニューや権限パネルに出す共有元の名前の決め方を変えるとき。
- 呼び出し先: `WebExtensionPolicy.getByURI()`
- 条件付き依存: `if (!uri)` → `Services.io.newURI()`
- 条件付き依存: `if (!host)` → `uri.scheme.toLowerCase()`
- 条件付き依存: `if (!(uri && uri.scheme.toLowerCase() == "about"))` → `lazy.syncL10n.formatValueSync()`
- 参照: `addonPolicy?.name`, `uri.hostPort`, `uri.specIgnoringRef`
- XPCOM: `Services.io`

## updateGlobalIndicator()
- 位置: L811-854
- 役割: 全ウィンドウの共有メニューを表示・非表示にし、インジケーターウィンドウを作成・更新・閉じる。
- 触るとき: 全体インジケーターの出し方や閉じ方を変えるとき。
- 呼び出し先: `Services.wm.getEnumerator()`
- 条件付き依存: `if (this.showGlobalIndicator)` → `showOrCreateMenuForWindow()`
- 条件付き依存: `if (!(this.showGlobalIndicator))` → `doc.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `doc.getElementById()`
- 条件付き依存: `if (!gIndicatorWindow)` → `getGlobalIndicator()`
- 条件付き依存: `if (!(!gIndicatorWindow))` → `gIndicatorWindow.updateIndicatorState()`
- 条件付き依存: `if (!(!gIndicatorWindow))` → `console.error()`
- 条件付き依存: `if (gIndicatorWindow.closingInternally)` → `gIndicatorWindow.closingInternally()`
- 条件付き依存: `if (gIndicatorWindow)` → `gIndicatorWindow.close()`
- 参照: `AppConstants.platform`, `chromeWin.document`, `err.message`, `existingMenu.hidden`, `gIndicatorWindow.closingInternally`, `separator.hidden`, `this.showGlobalIndicator`
- XPCOM: `Services.wm`

## getWindowShareState()
- 位置: L856-863
- 役割: 画面を共有中なら画面、そのウィンドウが共有中ならウィンドウ、どちらでもなければ非共有を返す。
- 触るとき: ウィンドウごとの共有状態を表示に反映する箇所を追うとき。
- 条件付き依存: `if (!(this.sharingScreen))` → `this.sharedBrowserWindows.has()`
- 参照: `this.SHARING_NONE`, `this.SHARING_SCREEN`, `this.SHARING_WINDOW`, `this.sharingScreen`

## tabAddedWhileSharing()
- 位置: L865-867
- 役割: 共有中に追加されたタブを、タブ切り替え警告の許可リストに入れる。
- 触るとき: 共有中に開いた新しいタブで切り替え警告が出る問題を調べるとき。
- 呼び出し先: `this.allowedSharedBrowsers.add()`
- 参照: `tab.linkedBrowser.permanentKey`

## shouldShowSharedTabWarning()
- 位置: L869-894
- 役割: 共有中のタブ切り替えで警告を出すかを返す。最初の切り替えでは選択中のタブを許可リストに入れ、切り替え回数を数える。
- 触るとき: 共有中のタブ切り替え警告の条件を変えるとき。
- 呼び出し先: `this.allowedSharedBrowsers.has()`
- 条件付き依存: `if (!this.tabSwitchCountForSession)` → `this.allowedSharedBrowsers.add()`
- 参照: `browser.permanentKey`, `tab.linkedBrowser`, `this.allowTabSwitchesForSession`, `this.tabSwitchCountForSession`

## allowSharedTabSwitch()
- 位置: L896-902
- 役割: 指定タブを許可リストに入れて選択し、セッション中の切り替え許可を設定する。
- 触るとき: 警告で切り替えを許可したときの動作を変えるとき。
- 呼び出し先: `browser.getTabBrowser()`, `this.allowedSharedBrowsers.add()`
- 参照: `browser.permanentKey`, `gBrowser.selectedTab`, `tab.linkedBrowser`, `this.allowTabSwitchesForSession`

## _setSharedData()
- 位置: L912-929
- 役割: 画面共有の有無と、共有中のトップウィンドウのinnerWindowId集合を共有データに書き出す。
- 触るとき: コンテンツ側が共有状態を読む値を追加・変更するとき。
- 呼び出し先: `Services.ppmm.sharedData.set()`, `this.sharedBrowserWindows.has()`
- 条件付き依存: `if (this.sharedBrowserWindows.has(win))` → `sharedTopInnerWindowIds.add()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `this.sharingScreen`, `win.browsingContext.currentWindowGlobal.innerWindowId`
- XPCOM: `Services.ppmm`

## getGlobalIndicator()
- 位置: L932-943
- 役割: webrtcIndicator.xhtmlを、常に前面・最小化可能なダイアログとして開く。
- 触るとき: 共有インジケーターのウィンドウの種類や見た目の設定を変えるとき。
- 呼び出し先: `Services.ww.openWindow()`
- XPCOM: `Services.ww`

## showStreamSharingMenu()
- 位置: L952-1022
- 役割: 共有インジケーターのメニューに、カメラ・マイク・画面の共有先を項目として追加する。1件なら表示名と操作項目、複数なら件数と各タブの項目。
- 触るとき: インジケーターのメニューの項目構成や、共有の操作項目の動作を変えるとき。(注意: 操作項目のcommandリスナーに this を渡しているが、呼び出し元webrtcIndicator.jsは単純な関数呼び出しのため this がundefinedになる。)
- 呼び出し先: `SHARING_L10NID_BY_TYPE.get()`, `menu.getAttribute()`, `win.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (type == "Camera")` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (type == "Microphone")` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (type == "Screen")` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (!activeStreams.length)` → `event.preventDefault()`
- 条件付き依存: `if (activeStreams.length == 1)` → `doc.createXULElement()`
- 条件付き依存: `if (activeStreams.length == 1)` → `getDisplayHostForStream()`
- 条件付き依存: `if (activeStreams.length == 1)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (activeStreams.length == 1)` → `sharingItem.setAttribute()`
- 条件付き依存: `if (activeStreams.length == 1)` → `menu.appendChild()`
- 条件付き依存: `if (activeStreams.length == 1)` → `controlItem.addEventListener()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `doc.createXULElement()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `sharingItem.setAttribute()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `menu.appendChild()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `getDisplayHostForStream()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `controlItem.addEventListener()`
- 参照: `activeStreams.length`, `controlItem.stream`, `event.target`, `webrtcUI.showScreenSharingIndicator`, `win.document`

## getDisplayHostForStream()
- 位置: L1024-1041
- 役割: ストリームのURIからホストを表示用に取り、空や例外なら表示用のspecを返す。
- 触るとき: 共有メニューに出すサイト名の表示を変えるとき。
- 呼び出し先: `Services.io.newURI()`
- 参照: `stream.uri`, `uri.displayHost`, `uri.displaySpec`
- XPCOM: `Services.io`

## onTabSharingMenuPopupShowing()
- 位置: L1043-1061
- 役割: 共有中の各タブについて、デバイス名の一覧と共有元名を持つメニュー項目を追加する。
- 触るとき: タブの共有メニューの項目の文言や並びを変えるとき。
- 呼び出し先: `MEDIA_SOURCE_L10NID_BY_TYPE.get()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `e.target.appendChild()`, `lazy.listFormat.format()`, `lazy.syncL10n.formatValueSync()`, `menuitem.addEventListener()`, `streamInfo.devices.map()`, `webrtcUI.getActiveStreams()`, `webrtcUI.getHostOrExtensionName()`
- 参照: `e.target.ownerDocument`, `menuitem.stream`, `streamInfo.uri`

## onTabSharingMenuPopupHiding()
- 位置: L1063-1067
- 役割: メニューを閉じたとき、子の項目を全て削除する。
- 触るとき: メニューを開き直すたびに項目が重複する問題を調べるとき。
- 呼び出し先: `this.lastChild.remove()`
- 参照: `this.lastChild`

## onTabSharingMenuPopupCommand()
- 位置: L1069-1071
- 役割: メニュー項目が選ばれたら、そのストリームの権限パネルを開く。
- 触るとき: 共有メニューの項目を選んだときの動作を変えるとき。
- 呼び出し先: `webrtcUI.showSharingDoorhanger()`
- 参照: `e.target.stream`

## showOrCreateMenuForWindow()
- 位置: L1073-1104
- 役割: 共有メニューがなければ作成して、ツールメニュー(macOS)かヘルプの前(その他)に挿入する。あれば表示する。
- 触るとき: ウィンドウのメニューバーへの共有メニューの配置や表示条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!menu)` → `document.createXULElement()`
- 条件付き依存: `if (!menu)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.createXULElement()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `container.insertBefore()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document.getElementById()`
- 条件付き依存: `if (!menu)` → `popup.addEventListener()`
- 条件付き依存: `if (!menu)` → `menu.appendChild()`
- 条件付き依存: `if (!menu)` → `container.insertBefore()`
- 参照: `AppConstants.platform`, `aWindow.document`, `document.getElementById("tabSharingSeparator").hidden`, `menu.hidden`, `menu.id`, `popup.id`, `separator.id`
