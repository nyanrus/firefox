# browser/modules/Sanitizer.sys.mjs

source: browser/modules/Sanitizer.sys.mjs
source-hash: f0d146337bab529afd7f6b108c7388ceb286caae
lines: 1383

## <module>
- 役割: 閲覧履歴、Cookie、キャッシュなどの個人データを、ユーザーの指定や終了時の設定に応じて消去する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## log()
- 位置: L22-31
- 役割: Sanitizer 用のログ出力を遅延生成し、browser.sanitizer.loglevel に従って出す。
- 触るとき: 消去処理の進行を追うためにログを増やすとき、ログが出ない原因を調べるとき。
- 呼び出し先: `logConsole.log()`
- 条件付き依存: `if (!logConsole)` → `console.createInstance()`

## TIMESPAN_TODAY()
- 位置: L93-95
- 役割: 今日の0時からの経過ミリ秒を返す。
- 触るとき: 「今日」の消去期間の計算を変えるとき。
- 呼び出し先: `Date.now()`, `new Date().setHours()`

## showUI()
- 位置: async L124-159
- 役割: 消去ダイアログ(sanitize_v2)を開き、ユーザーが承認したか取り消したかを返す。親ウィンドウに gDialogBox があればその中に、無ければ独立したモーダルとして開く。
- 触るとき: 消去ダイアログの開き方や戻り値の扱いを変えるとき。
- 呼び出し先: `Promise.withResolvers()`
- 条件付き依存: `if (parentWindow?.gDialogBox)` → `parentWindow.gDialogBox.open()`
- 条件付き依存: `if (!(parentWindow?.gDialogBox))` → `Services.ww.openWindow()`
- 参照: `deferred.promise`, `parentWindow?.document.documentURI`, `parentWindow?.gDialogBox`
- XPCOM: `Services.ww`

## onAccept()
- 位置: L140-140
- 役割: ダイアログ内で承認されたとき accept で解決する。
- 触るとき: 承認時の戻り値を変えるとき。
- 呼び出し先: `deferred.resolve()`

## onCancel()
- 位置: L141-141
- 役割: ダイアログ内で取り消されたとき cancel で解決する。
- 触るとき: 取り消し時の戻り値を変えるとき。
- 呼び出し先: `deferred.resolve()`

## onAccept()
- 位置: L152-152
- 役割: 独立ウィンドウで承認されたとき accept で解決する。
- 触るとき: 独立ウィンドウ版の承認処理を変えるとき。
- 呼び出し先: `deferred.resolve()`

## onCancel()
- 位置: L153-153
- 役割: 独立ウィンドウで取り消されたとき cancel で解決する。
- 触るとき: 独立ウィンドウ版の取り消し処理を変えるとき。
- 呼び出し先: `deferred.resolve()`

## onStartup()
- 位置: async L166-234
- 役割: 前回のセッションで終わらなかった消去を実行し、終了時消去の保留を登録し、終了時に実行するブロッカーを追加する。
- 触るとき: 起動時に消去が再実行されない問題や、終了時消去の登録順を変えるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `cleanupAfterSanitization()`, `console.error()`, `getAndClearPendingSanitizations()`, `log()`, `pendingSanitizations.findIndex()`, `sanitizeOnShutdown()`, `shutdownClient.addBlocker()`, `this.sanitize()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `addPendingSanitization()`
- 条件付き依存: `if (this.shouldSanitizeNewTabContainer)` → `addPendingSanitization()`
- 条件付き依存: `if (i != -1)` → `pendingSanitizations.splice()`
- 条件付き依存: `if (i != -1)` → `sanitizeNewTabSegregation()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL`, `Sanitizer.PREF_SANITIZE_ON_SHUTDOWN`, `Sanitizer.PREF_SHUTDOWN_BRANCH`, `lazy.PlacesUtils.history.shutdownClient.jsclient`, `options.progress`, `s.id`, `this.PREF_NEWTAB_SEGREGATION`, `this.shouldSanitizeNewTabContainer`, `this.shouldSanitizeOnShutdown`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.prefs`

## fetchState()
- 位置: L201-201
- 役割: 終了時消去のブロッカーに、進行状況を渡す。
- 触るとき: 終了時消去がタイムアウトしたときに報告される進行状況の内容を変えるとき。

## getClearRange()
- 位置: L250-288
- 役割: 消去期間を [開始, 終了] のマイクロ秒で返す。全期間なら null を返し、ts が省略されたら privacy.sanitize.timeSpan を使う。不正な値なら例外を投げる。
- 触るとき: 消去期間の計算を変えるとき、期間指定で消す範囲がずれる問題を調べるとき。
- 呼び出し先: `Date.now()`, `d.setHours()`, `d.setMilliseconds()`, `d.setMinutes()`, `d.setSeconds()`, `d.valueOf()`
- 条件付き依存: `if (ts === undefined)` → `Services.prefs.getIntPref()`
- 参照: `Sanitizer.PREF_TIMESPAN`, `Sanitizer.TIMESPAN_24HOURS`, `Sanitizer.TIMESPAN_2HOURS`, `Sanitizer.TIMESPAN_4HOURS`, `Sanitizer.TIMESPAN_5MIN`, `Sanitizer.TIMESPAN_EVERYTHING`, `Sanitizer.TIMESPAN_HOUR`, `Sanitizer.TIMESPAN_TODAY`
- XPCOM: `Services.prefs`

## sanitize()
- 位置: async L314-345
- 役割: 消去の進行状況を作り、項目を消去する。項目が指定されなければ privacy.cpd の項目を使う。終了時以外は消去の完了まで終了ブロッカーに登録し、完了通知を出す。
- 触るとき: 消去 API の受け付け方や終了ブロッカーの登録を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `sanitizeInternal()`
- 条件付き依存: `if (!itemsToClear)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (!progress.isShutdown)` → `shutdownClient.addBlocker()`
- 参照: `lazy.PlacesUtils.history.shutdownClient.jsclient`, `lazy.PrincipalsCollector`, `options.progress`, `progress.isShutdown`, `this.PREF_CPD_BRANCH`, `this.items`
- XPCOM: `Services.obs`

## fetchState()
- 位置: L335-335
- 役割: 消去処理のブロッカーに、進行状況を渡す。
- 触るとき: 消去処理がシャットダウンで止まったときの報告内容を変えるとき。

## observe()
- 位置: L347-382
- 役割: 終了時消去、その項目、新しいタブのコンテナー分離の pref が変わったとき、保留中の消去を作り直すか外す。
- 触るとき: 設定変更が終了時の保留に反映されない問題を調べるとき。
- 条件付き依存: `if (topic == "nsPref:changed")` → `data.startsWith()`
- 条件付き依存: `if ( data.startsWith(this.PREF_SHUTDOWN_BRANCH) && this.shouldSanitizeOnShutdown )` → `removePendingSanitization()`
- 条件付き依存: `if ( data.startsWith(this.PREF_SHUTDOWN_BRANCH) && this.shouldSanitizeOnShutdown )` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if ( data.startsWith(this.PREF_SHUTDOWN_BRANCH) && this.shouldSanitizeOnShutdown )` → `addPendingSanitization()`
- 条件付き依存: `if (data == this.PREF_SANITIZE_ON_SHUTDOWN)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (data == this.PREF_SANITIZE_ON_SHUTDOWN)` → `removePendingSanitization()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `addPendingSanitization()`
- 条件付き依存: `if (data == this.PREF_NEWTAB_SEGREGATION)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (data == this.PREF_NEWTAB_SEGREGATION)` → `removePendingSanitization()`
- 条件付き依存: `if (this.shouldSanitizeNewTabContainer)` → `addPendingSanitization()`
- 参照: `Sanitizer.PREF_SANITIZE_ON_SHUTDOWN`, `Sanitizer.PREF_SHUTDOWN_BRANCH`, `this.PREF_NEWTAB_SEGREGATION`, `this.PREF_SANITIZE_ON_SHUTDOWN`, `this.PREF_SHUTDOWN_BRANCH`, `this.shouldSanitizeNewTabContainer`, `this.shouldSanitizeOnShutdown`
- XPCOM: `Services.prefs`

## runSanitizeOnShutdown()
- 位置: async L390-402
- 役割: テスト用に、主体の収集結果を消してから終了時の消去を実行する。
- 触るとき: 終了時消去のテストの前提を変えるとき。
- 呼び出し先: `sanitizeOnShutdown()`

## maybeMigratePrefs()
- 位置: L413-493
- 役割: 旧版の消去設定を新しい設定(clearOnShutdown_v2 か clearHistory)へ移し、移行済みのフラグを立てる。移行済みなら何もしない。
- 触るとき: 消去ダイアログの設定の移行ルールを変えるとき、旧設定から値が正しく移らない問題を調べるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( `privacy.sanitize.${context}.hasMigratedToNewPrefs2` ) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!( Services.prefs.getBoolPref( `privacy.sanitize.${context}.hasMigratedToNewPrefs2` ) ))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!( Services.prefs.getBoolPref( `privacy.sanitize.${context}.hasMigratedToNewPrefs2` ) ))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## clear()
- 位置: async L501-505
- 役割: キャッシュを消去し、その所要時間を計測する。
- 触るとき: キャッシュの消去範囲を変えるとき。
- 呼び出し先: `Glean.browserSanitizer.cache.start()`, `Glean.browserSanitizer.cache.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL_CACHES`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L509-535
- 役割: Cookie とサイトデータなどを消去する。終了時は主体ごとに例外を考慮して消し、それ以外は期間内を消す。さらにメディアデバイスの許可も消す。
- 触るとき: Cookie の消去範囲や終了時の例外の扱いを変えるとき。
- 呼び出し先: `Glean.browserSanitizer.cookies.start()`, `Glean.browserSanitizer.cookies.stopAndAccumulate()`, `clearData()`
- 条件付き依存: `if (clearHonoringExceptions)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (clearHonoringExceptions)` → `maybeSanitizeSessionPrincipals()`
- 条件付き依存: `if (!(clearHonoringExceptions))` → `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_BOUNCE_TRACKING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_COOKIES`, `Ci.nsIClearDataService.CLEAR_FINGERPRINTING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_MEDIA_DEVICES`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L539-560
- 役割: オフラインアプリのデータ(DOM ストレージ)を消去する。終了時は主体ごとに例外を考慮する。
- 触るとき: オフラインデータの消去範囲や終了時の例外の扱いを変えるとき。
- 条件付き依存: `if (clearHonoringExceptions)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (clearHonoringExceptions)` → `maybeSanitizeSessionPrincipals()`
- 条件付き依存: `if (!(clearHonoringExceptions))` → `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_DOM_STORAGES`, `Ci.nsIClearDataService.CLEAR_FINGERPRINTING_PROTECTION_STATE`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L564-595
- 役割: 全主体を集めた上で、閲覧履歴とコンテンツブロックの記録を消し、ストレージアクセス権限のうちデータを持たないものを消す。
- 触るとき: 履歴の消去範囲や、ストレージアクセス権限の扱いを変えるとき。
- 呼び出し先: `Glean.browserSanitizer.history.start()`, `Glean.browserSanitizer.history.stopAndAccumulate()`, `Services.clearData.deleteUserInteractionForClearingHistory()`, `clearData()`, `gPrincipalsCollector.getAllPrincipals()`
- 参照: `Ci.nsIClearDataService.CLEAR_CONTENT_BLOCKING_RECORDS`, `Ci.nsIClearDataService.CLEAR_HISTORY`, `lazy.PrincipalsCollector`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## clear()
- 位置: async L599-652
- 役割: 検索バーの取り消し履歴と検索バーの値、検索窓の値を消去し、フォーム履歴の期間内を削除する。途中で起きた例外は最後にまとめて投げる。
- 触るとき: フォーム履歴や検索の入力の消去方法を変えるとき。
- 呼び出し先: `Glean.browserSanitizer.formdata.start()`, `Glean.browserSanitizer.formdata.stopAndAccumulate()`, `Services.wm.getEnumerator()`, `currentDocument.getElementById()`, `lazy.FormHistory.update()`, `lazy.FormHistory.update(change).catch()`, `tabBrowser.clearLastFindValue()`, `tabBrowser.isFindBarInitialized()`
- 条件付き依存: `if (searchBar)` → `input.editor?.clearUndoRedo()`
- 条件付き依存: `if (tabBrowser.isFindBarInitialized(tab))` → `tabBrowser.getCachedFindBar(tab).clear()`
- 条件付き依存: `if (tabBrowser.isFindBarInitialized(tab))` → `tabBrowser.getCachedFindBar()`
- 参照: `change.firstUsedEnd`, `change.firstUsedStart`, `currentWindow.document`, `currentWindow.gBrowser`, `e.message`, `e.result`, `input.value`, `searchBar.textbox`, `tabBrowser.tabs`
- XPCOM: `Services.wm`

## clear()
- 位置: async L656-660
- 役割: ダウンロード履歴を消去する。
- 触るとき: ダウンロード履歴の消去範囲を変えるとき。
- 呼び出し先: `Glean.browserSanitizer.downloads.start()`, `Glean.browserSanitizer.downloads.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_DOWNLOADS`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L664-672
- 役割: 認証トークンと認証キャッシュを消去する。
- 触るとき: セッション関連の認証情報の消去範囲を変えるとき。
- 呼び出し先: `Glean.browserSanitizer.sessions.start()`, `Glean.browserSanitizer.sessions.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_AUTH_CACHE`, `Ci.nsIClearDataService.CLEAR_AUTH_TOKENS`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L676-696
- 役割: サイトの権限、コンテンツ設定、プッシュ通知、クライアント証明書の記憶、証明書の例外などを消去する。終了時は終了時例外を残す権限の種類を使い、手動の消去は全権限を消す。
- 触るとき: サイト設定の消去範囲や、終了時の例外の扱いを変えるとき。
- 呼び出し先: `Glean.browserSanitizer.sitesettings.start()`, `Glean.browserSanitizer.sitesettings.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_CERT_EXCEPTIONS`, `Ci.nsIClearDataService.CLEAR_CLIENT_AUTH_REMEMBER_SERVICE`, `Ci.nsIClearDataService.CLEAR_CONTENT_PREFERENCES`, `Ci.nsIClearDataService.CLEAR_CREDENTIAL_MANAGER_STATE`, `Ci.nsIClearDataService.CLEAR_DOM_PUSH_NOTIFICATIONS`, `Ci.nsIClearDataService.CLEAR_FINGERPRINTING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_PERMISSIONS`, `Ci.nsIClearDataService.CLEAR_SITE_PERMISSIONS`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## _canCloseWindow()
- 位置: L700-709
- 役割: ウィンドウを閉じてよいか確認し、よいなら次の閉じる確認を省くフラグを立てる。
- 触るとき: 未保存の確認で消去が中断される問題を調べるとき。
- 呼び出し先: `win.CanCloseWindow()`
- 参照: `win.skipNextCanClose`

## _resetAllWindowClosures()
- 位置: L710-714
- 役割: 確認済みのフラグを全ウィンドウで外す。
- 触るとき: 消去を中断したときにフラグが残る問題を調べるとき。
- 参照: `win.skipNextCanClose`

## clear()
- 位置: async L715-840
- 役割: 全ブラウザーウィンドウを閉じる前に、全部が閉じられるか確認する。閉じられなければ例外を投げて中断する。1分を超えたら中断する。新しいウィンドウを開いてから古いものを閉じ、両方の完了を待つ。
- 触るとき: 開いているウィンドウの消去方法や、確認の中断条件を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/browser/clh;1"].getService()`, `Date.now()`, `Glean.browserSanitizer.openwindows.start()`, `Services.obs.addObserver()`, `Services.wm.getEnumerator()`, `newWindow.focus()`, `this._canCloseWindow()`, `windowList.pop()`, `windowList.pop().close()`, `windowList.push()`, `windowList[0].openDialog()`
- 条件付き依存: `if (!this._canCloseWindow(someWin))` → `this._resetAllWindowClosures()`
- 条件付き依存: `if (Date.now() > startDate + 60 * 1000)` → `this._resetAllWindowClosures()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `newWindow.addEventListener()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `AppConstants.platform`, `Ci.nsIBrowserHandler`, `handler.defaultArgs`, `windowList.length`
- XPCOM: [`nsIBrowserHandler`](../components/nsIBrowserHandler.idl.md) / `@mozilla.org/browser/clh;1` / `Services.obs` / `Services.wm`

## onFullScreen()
- 位置: L769-780
- 役割: macOS で、新しいウィンドウが全画面のまま戻らないように sizemode を normal に戻す。
- 触るとき: macOS で消去後の新しいウィンドウが全画面になる問題を調べるとき。
- 呼び出し先: `docEl.getAttribute()`, `newWindow.removeEventListener()`
- 条件付き依存: `if (!newWindow.fullScreen && sizemode == "fullscreen")` → `docEl.setAttribute()`
- 条件付き依存: `if (!newWindow.fullScreen && sizemode == "fullscreen")` → `e.preventDefault()`
- 条件付き依存: `if (!newWindow.fullScreen && sizemode == "fullscreen")` → `e.stopPropagation()`
- 参照: `newWindow.document.documentElement`, `newWindow.fullScreen`

## onWindowOpened()
- 位置: L792-810
- 役割: 新しいウィンドウの起動完了を受け、古いウィンドウが全部閉じられていれば完了として解決する。
- 触るとき: 新しいウィンドウの起動完了の判定を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `newWindow.removeEventListener()`
- 条件付き依存: `if (numWindowsClosing == 0)` → `Glean.browserSanitizer.openwindows.stopAndAccumulate()`
- 条件付き依存: `if (numWindowsClosing == 0)` → `resolve()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.obs`

## onWindowClosed()
- 位置: L813-826
- 役割: 古いウィンドウが閉じられたことを数え、全部閉じて新しいウィンドウも開いていれば完了として解決する。
- 触るとき: ウィンドウの閉じる完了の待ち方を変えるとき、消去後に待ち続ける問題を調べるとき。
- 条件付き依存: `if (numWindowsClosing == 0)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (newWindowOpened)` → `Glean.browserSanitizer.openwindows.stopAndAccumulate()`
- 条件付き依存: `if (newWindowOpened)` → `resolve()`
- XPCOM: `Services.obs`

## clear()
- 位置: async L844-844
- 役割: プラグインのデータの消去は何もしない。
- 触るとき: プラグインのデータを消す処理を追加するとき。

## clear()
- 位置: async L850-883
- 役割: 閲覧履歴とダウンロードをまとめて消去し、チャットの会話も消す。
- 触るとき: 閲覧履歴の消去の組み合わせを変えるとき。
- 呼び出し先: `Glean.browserSanitizer.downloads.start()`, `Glean.browserSanitizer.downloads.stopAndAccumulate()`, `Glean.browserSanitizer.history.start()`, `Glean.browserSanitizer.history.stopAndAccumulate()`, `Services.clearData.deleteUserInteractionForClearingHistory()`, `clearChatConversations()`, `clearData()`, `gPrincipalsCollector.getAllPrincipals()`
- 参照: `Ci.nsIClearDataService.CLEAR_CONTENT_BLOCKING_RECORDS`, `Ci.nsIClearDataService.CLEAR_DOWNLOADS`, `Ci.nsIClearDataService.CLEAR_HISTORY`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## clear()
- 位置: async L887-911
- 役割: Cookie とサイトデータを消去し、メディアデバイスの許可を消し、チャットの会話も消す。終了時は主体ごとに例外を考慮する。
- 触るとき: Cookie やサイトデータの消去の組み合わせを変えるとき。
- 呼び出し先: `Glean.browserSanitizer.cookies.start()`, `Glean.browserSanitizer.cookies.stopAndAccumulate()`, `clearChatConversations()`, `clearData()`
- 条件付き依存: `if (clearHonoringExceptions)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (clearHonoringExceptions)` → `maybeSanitizeSessionPrincipals()`
- 条件付き依存: `if (!(clearHonoringExceptions))` → `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_COOKIES_AND_SITE_DATA`, `Ci.nsIClearDataService.CLEAR_MEDIA_DEVICES`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clearChatConversations()
- 位置: async L918-934
- 役割: AI ウィンドウが有効なら、期間内または全件のチャット会話を削除する。失敗はログに残して続行する。
- 触るとき: チャット会話の消去の条件や範囲を変えるとき。
- 呼び出し先: `log()`
- 条件付き依存: `if (range)` → `lazy.ChatStore.deleteConversationsByDateRange()`
- 条件付き依存: `if (!(range))` → `lazy.ChatStore.deleteAllConversations()`
- 参照: `lazy.AIWindow.isEnabled`, `progress.step`

## sanitizeInternal()
- 位置: async L936-1040
- 役割: 項目を1つずつ並行して消去する。openWindows は先に実行し、保留の記録を作り、終わったら保留を外す。どれか失敗していれば最後に例外を投げる。
- 触るとき: 消去の並行実行や順序、失敗の扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `Glean.browserSanitizer.total.start()`, `Glean.browserSanitizer.total.stopAndAccumulate()`, `Object.assign()`, `Promise.all()`, `annotateError()`, `handles.map()`, `handles.push()`, `item .clear()`, `itemsToClear.indexOf()`, `log()`
- 条件付き依存: `if (!progress.isShutdown)` → `addPendingSanitization()`
- 条件付き依存: `if (openWindowsIndex != -1)` → `itemsToClear.splice()`
- 条件付き依存: `if (openWindowsIndex != -1)` → `items.openWindows.clear()`
- 条件付き依存: `if (openWindowsIndex != -1)` → `Object.assign()`
- 条件付き依存: `if (!ignoreTimespan && !range)` → `Sanitizer.getClearRange()`
- 条件付き依存: `if (!progress.isShutdown)` → `removePendingSanitization()`
- 参照: `h.promise`, `progress.clearHonoringExceptions`, `progress.isShutdown`, `progress.openWindows`, `progress.openWindowsProgress`

## annotateError()
- 位置: L993-997
- 役割: 項目の進行状況を failed にし、エラーのフラグを立ててコンソールに出す。
- 触るとき: 消去の失敗がどう記録されるかを変えるとき。
- 呼び出し先: `console.error()`

## sanitizeOnShutdown()
- 位置: async L1042-1150
- 役割: 終了時の消去を行う。終了時消去が有効なら設定された項目を消し、新しいタブのコンテナーを消す。無効でも、Cookie をセッション限りにした主体は終了時に消す。最後に後始末を行う。
- 触るとき: 終了時に何が消えるかを変えるとき、終了時の消去が実行されない問題を調べるとき。
- 呼び出し先: `Sanitizer.maybeMigratePrefs()`, `Services.prefs.getBoolPref()`, `cleanupAfterSanitization()`, `log()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeOnShutdown)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeOnShutdown)` → `Sanitizer.sanitize()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeOnShutdown)` → `removePendingSanitization()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeNewTabContainer)` → `sanitizeNewTabSegregation()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeNewTabContainer)` → `removePendingSanitization()`
- 条件付き依存: `if (needsSyncSavePrefs)` → `Services.prefs.savePrefFile()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `isSupportedPrincipal()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `log()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `selectedPrincipals.push()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `extractMatchingPrincipals()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `maybeSanitizeSessionPrincipals()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL`, `Ci.nsIClearDataService.CLEAR_ALL_CACHES`, `Ci.nsIClearDataService.CLEAR_BOUNCE_TRACKING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_COOKIES`, `Ci.nsIClearDataService.CLEAR_DOM_STORAGES`, `Ci.nsIClearDataService.CLEAR_EME`, `Ci.nsICookiePermission.ACCESS_SESSION`, `Sanitizer.PREF_SHUTDOWN_BRANCH`, `Sanitizer.shouldSanitizeNewTabContainer`, `Sanitizer.shouldSanitizeOnShutdown`, `Services.perms.all`, `lazy.PrincipalsCollector`, `permission.capability`, `permission.principal`, `permission.principal.asciiSpec`, `permission.principal.host`, `permission.type`, `progress.advancement`, `progress.sanitizationPrefs`, `progress.sanitizationPrefs.session_permission_exceptions`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / [`nsICookiePermission`](../../netwerk/cookie/nsICookiePermission.idl.md) / `Services.perms` / `Services.prefs`

## cleanupAfterSanitization()
- 位置: async L1152-1156
- 役割: 消去後のクリーンアップを、データ消去サービスの終了時後処理として呼ぶ。
- 触るとき: 消去後の後始末の種類を変えるとき。
- 呼び出し先: `Services.clearData.cleanupAfterDeletionAtShutdown()`
- XPCOM: `Services.clearData`

## extractMatchingPrincipals()
- 位置: L1159-1163
- 役割: ホストがルートドメインとして一致する主体だけを抜き出す。
- 触るとき: 例外のドメインに属する主体を選ぶ条件を変えるとき。
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `principals.filter()`
- 参照: `principal.host`
- XPCOM: `Services.eTLD`

## maybeSanitizeSessionPrincipals()
- 位置: async L1174-1230
- 役割: 終了時例外の許可を集め、各主体について Cookie のセッション指定があれば消去し、例外があれば残し、それ以外は消去する。
- 触るとき: 終了時の例外の判定順序や残す条件を変えるとき。
- 呼び出し先: `Services.perms.getAllByTypes()`, `isCookieSession()`, `isSupportedPrincipal()`, `log()`, `principals.forEach()`
- 条件付き依存: `if ( perm.capability == Ci.nsIPermissionManager.ALLOW_ACTION && isSupportedPrincipal(perm.principal) )` → `exceptionPartitionSites.add()`
- 条件付き依存: `if ( perm.capability == Ci.nsIPermissionManager.ALLOW_ACTION && isSupportedPrincipal(perm.principal) )` → `shutdownExceptionHosts.push()`
- 条件付き依存: `if (!(isCookieSession(principal)))` → `isShutdownExceptionApplicable()`
- 条件付き依存: `if (!preserve)` → `promises.push()`
- 条件付き依存: `if (!preserve)` → `sanitizeSessionPrincipal()`
- 条件付き依存: `if (promises.length)` → `Promise.all()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `perm.capability`, `perm.principal`, `perm.principal.baseDomain`, `perm.principal.host`, `principals.length`, `progress.step`, `promises.length`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## isShutdownExceptionApplicable()
- 位置: L1237-1263
- 役割: 終了時例外が主体に当てはまるかを返す。パーティションなしは権限の上位ドメインまで見て判定し、パーティションありは分割キーのベースドメインで判定する。
- 触るとき: サードパーティ分割のデータに終了時例外が効く範囲を変えるとき。
- 呼び出し先: `ChromeUtils.getBaseDomainFromPartitionKey()`, `exceptionPartitionSites.has()`
- 条件付き依存: `if (!partitionKey)` → `Services.perms.testPermissionFromPrincipal()`
- 条件付き依存: `if (!partitionKey)` → `shutdownExceptionHosts.some()`
- 条件付き依存: `if (!partitionKey)` → `Services.eTLD.hasRootDomain()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `principal.host`, `principal.originAttributes`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / `Services.eTLD` / `Services.perms`

## isCookieSession()
- 位置: L1265-1270
- 役割: 主体の Cookie の権限がセッション限り(ACCESS_SESSION)かを返す。
- 触るとき: セッション限りの Cookie の判定を変えるとき。
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`
- XPCOM: [`nsICookiePermission`](../../netwerk/cookie/nsICookiePermission.idl.md) / `Services.perms`

## sanitizeSessionPrincipal()
- 位置: async L1272-1285
- 役割: 主体の指定の種類のデータを、データ消去サービスで削除する。
- 触るとき: 主体単位の削除の内容を変えるとき。
- 呼び出し先: `Services.clearData.deleteDataFromPrincipal()`, `log()`
- 参照: `principal.asciiSpec`, `progress.sanitizePrincipal`
- XPCOM: `Services.clearData`

## sanitizeNewTabSegregation()
- 位置: L1287-1296
- 役割: 新しいタブのサムネイル用の分離コンテナーのデータを消す。
- 触るとき: about:newtab の分離コンテナーの後始末を変えるとき。
- 呼び出し先: `lazy.ContextualIdentityService.getPrivateIdentity()`
- 条件付き依存: `if (identity)` → `Services.clearData.deleteDataFromOriginAttributesPattern()`
- 参照: `identity.userContextId`
- XPCOM: `Services.clearData`

## getItemsToClearFromPrefBranch()
- 位置: L1304-1313
- 役割: 指定の pref ブランチで true になっている消去項目の名前を返す。
- 触るとき: 消去項目の pref の読み方や、項目を増やすときに確認するとき。
- 呼び出し先: `Object.keys()`, `Object.keys(Sanitizer.items).filter()`, `Services.prefs.getBranch()`, `branch.getBoolPref()`
- 参照: `Sanitizer.items`
- XPCOM: `Services.prefs`

## addPendingSanitization()
- 位置: L1323-1330
- 役割: 保留中の消去を、privacy.sanitize.pending の JSON に追加する。
- 触るとき: クラッシュ時に消去を再実行する記録の内容を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `pendingSanitizations.push()`, `safeGetPendingSanitizations()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`
- XPCOM: `Services.prefs`

## removePendingSanitization()
- 位置: L1332-1341
- 役割: 保留中の消去を ID で探して JSON から取り除き、保存する。見つからない場合も splice(-1, 1) により末尾の要素が消える。
- 触るとき: 保留中の記録が意図せず消える問題、特に ID が無いときの挙動を調べるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `pendingSanitizations.findIndex()`, `pendingSanitizations.splice()`, `safeGetPendingSanitizations()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`, `s.id`
- XPCOM: `Services.prefs`

## getAndClearPendingSanitizations()
- 位置: L1343-1349
- 役割: 前回の保留中の消去を読み出し、pref を消す。
- 触るとき: 起動時に前回の保留を回収する処理を変えるとき。
- 呼び出し先: `safeGetPendingSanitizations()`
- 条件付き依存: `if (pendingSanitizations.length)` → `Services.prefs.clearUserPref()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`, `pendingSanitizations.length`
- XPCOM: `Services.prefs`

## safeGetPendingSanitizations()
- 位置: L1351-1360
- 役割: 保留中の消去の JSON を読む。壊れていれば空の配列を返す。
- 触るとき: 保留中の記録の形式を変えるとき、壊れた記録の扱いを調べるとき。
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `console.error()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`
- XPCOM: `Services.prefs`

## clearData()
- 位置: async L1362-1378
- 役割: 期間が指定されていれば期間内を、無ければ全体を、データ消去サービスで削除する。
- 触るとき: データ消去の基本の呼び出し方を変えるとき。
- 条件付き依存: `if (range)` → `Services.clearData.deleteDataInTimeRange()`
- 条件付き依存: `if (!(range))` → `Services.clearData.deleteData()`
- XPCOM: `Services.clearData`

## isSupportedPrincipal()
- 位置: L1380-1382
- 役割: 主体のスキームが http、https、file のいずれかかを返す。
- 触るとき: 終了時の例外の対象となるスキームを変えるとき。
- 呼び出し先: `["http", "https", "file"].some()`, `principal.schemeIs()`
