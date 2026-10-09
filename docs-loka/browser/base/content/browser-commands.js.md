# browser/base/content/browser-commands.js

source: browser/base/content/browser-commands.js
source-hash: 757c5b16612c96f327798f9e47c83144668074f0
lines: 599

## <module>
- 役割: ブラウザの基本コマンド(戻る・進む・再読込・タブ操作・ホーム・ファイルを開く等)を BrowserCommands にまとめて定義する。

## back()
- 位置: L12-22
- 役割: 現在のタブで戻る。修飾クリックなら戻り先を新しいタブや窓で開く。
- 触るとき: 戻る操作の遷移先(同じタブか別タブか)を変えるとき。
- 呼び出し先: `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (where == "current")` → `gBrowser.goBack()`
- 条件付き依存: `if (!(where == "current"))` → `duplicateTabIn()`
- 参照: `gBrowser.selectedTab`

## forward()
- 位置: L24-34
- 役割: 現在のタブで進む。修飾クリックなら進み先を新しいタブや窓で開く。
- 触るとき: 進む操作の遷移先を変えるとき。
- 呼び出し先: `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (where == "current")` → `gBrowser.goForward()`
- 条件付き依存: `if (!(where == "current"))` → `duplicateTabIn()`
- 参照: `gBrowser.selectedTab`

## handleBackspace()
- 位置: L36-45
- 役割: Backspace を browser.backspace_action に従い戻る操作かページスクロールに振り分ける。
- 触るとき: Backspace キーの動作を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `goDoCommand()`, `this.back()`
- XPCOM: `Services.prefs`

## handleShiftBackspace()
- 位置: L47-56
- 役割: Shift+Backspace を browser.backspace_action に従い進む操作かページ下スクロールに振り分ける。
- 触るとき: Shift+Backspace の動作を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `goDoCommand()`, `this.forward()`
- XPCOM: `Services.prefs`

## gotoHistoryIndex()
- 位置: L58-83
- 役割: 履歴メニューの項目で、通常クリックなら現タブの履歴を移動し、修飾クリックなら新しいタブや窓で開く。
- 触るとき: 履歴メニューからの移動や新規タブでの開き方を変えるとき。
- 呼び出し先: `BrowserUtils.getRootEvent()`, `BrowserUtils.whereToOpenLink()`, `Number()`, `aEvent.target.getAttribute()`, `duplicateTabIn()`
- 条件付き依存: `if (where == "current")` → `gBrowser.gotoIndex()`
- 参照: `gBrowser.selectedTab`

## addTabSplitView()
- 位置: L85-101
- 役割: 選択中のタブと新規の about:opentabs タブを分割表示に組み、新しいタブを選択する。
- 触るとき: タブの分割表示の作成条件や配置を変えるとき。
- 呼び出し先: `gBrowser.addTabSplitView()`, `gBrowser.addTrustedTab()`
- 参照: `gBrowser.selectedTab`, `gBrowser.selectedTab.hidden`, `gBrowser.selectedTab.pinned`, `gBrowser.selectedTab.splitview`

## separateTabSplitView()
- 位置: L103-105
- 役割: 選択中タブの分割表示を解除する。
- 触るとき: 分割表示の解除操作を変えるとき。
- 呼び出し先: `gBrowser.selectedTab?.splitview?.unsplitTabs()`

## duplicateTab()
- 位置: L107-109
- 役割: 選択中のタブを複製して新しいタブで開く。
- 触るとき: タブ複製の挙動を変えるとき。
- 呼び出し先: `duplicateTabIn()`
- 参照: `gBrowser.selectedTab`

## reloadOrDuplicate()
- 位置: L111-128
- 役割: Shift 付きならキャッシュを無視して再読込し、修飾クリックなら複製タブを開き、それ以外は再読込する。
- 触るとき: 再読込ボタンやショートカットの分岐を変えるとき。
- 呼び出し先: `BrowserUtils.getRootEvent()`, `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (aEvent.shiftKey && !backgroundTabModifier)` → `this.reloadSkipCache()`
- 条件付き依存: `if (where == "current")` → `this.reload()`
- 条件付き依存: `if (!(where == "current"))` → `duplicateTabIn()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `gBrowser.selectedTab`

## reload()
- 位置: L130-137
- 役割: 通常の再読込を行う。view-source ページはキャッシュを使わず再読込する。
- 触るとき: 再読込時のキャッシュ扱いを変えるとき。
- 呼び出し先: `gBrowser.currentURI.schemeIs()`, `gBrowser.reloadWithFlags()`
- 条件付き依存: `if (gBrowser.currentURI.schemeIs("view-source"))` → `this.reloadSkipCache()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## reloadSkipCache()
- 位置: L139-142
- 役割: プロキシとキャッシュを迂回して再読込する。
- 触るとき: 強制再読込のフラグを変えるとき。
- 呼び出し先: `gBrowser.reloadWithFlags()`

## stop()
- 位置: L144-146
- 役割: 現在の読み込みを停止する。
- 触るとき: 読み込み停止の挙動を変えるとき。
- 呼び出し先: `gBrowser.webNavigation.stop()`
- 参照: `Ci.nsIWebNavigation.STOP_ALL`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## home()
- 位置: L148-226
- 役割: ホームページを読み込む。現在のタブ、新規タブ、新規窓のどれで開くかをクリック修飾により決める。
- 触るとき: ホームボタンの遷移先や、ホームページ変更の通知(browser-open-homepage-start)を変えるとき。
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `HomePage.get()`, `OpenBrowserWindow()`, `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `aEvent?.preventDefault()`, `gBrowser.loadTabs()`, `homePage.split()`, `isBlankPageURL()`, `isInitialPage()`, `loadOneOrMoreURIs()`
- 条件付き依存: `if (isBlankPageURL(homePage))` → `gURLBar.select()`
- 条件付き依存: `if (!(isBlankPageURL(homePage)))` → `gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (!loadInBackground)` → `isBlankPageURL()`
- 条件付き依存: `if (notifyObservers)` → `Services.obs.notifyObservers()`
- 参照: `aEvent?.button`, `gBrowser.selectedBrowser.initialPageLoadedFromUserAction`, `gBrowser?.selectedTab.hidden`, `gBrowser?.selectedTab.pinned`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.scriptSecurityManager`

## openTab()
- 位置: L228-286
- 役割: 新規タブを開く。中クリック時は貼り付け機能を使い、クリップボードの URL を開くこともある。
- 触るとき: 新規タブのコマンド経路や browser-open-newtab-start 通知を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `openTrustedLinkIn()`
- 条件付き依存: `if (event)` → `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (!werePassedURL && searchClipboard)` → `readFromClipboard()`
- 条件付き依存: `if (!werePassedURL && searchClipboard)` → `UrlbarShared.stripUnsafeProtocolOnPaste(clipboard).trim()`
- 条件付き依存: `if (!werePassedURL && searchClipboard)` → `UrlbarShared.stripUnsafeProtocolOnPaste()`
- 参照: `event?.button`, `options.allowThirdPartyFixup`
- XPCOM: `Services.obs` / `Services.prefs`

## openFileWindow()
- 位置: L288-354
- 役割: ファイル選択ダイアログを開き、選んだファイルを現在のタブで開く。非ブラウザ窓では実ブラウザ窓に転送する。
- 触るとき: ファイルを開く操作や、macOS の隠しメニューバー窓からの呼び出しを扱うとき。
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `gNavigatorBundle.getString()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `URILoadingHelper.getTargetWindow()`
- 条件付き依存: `if (targetWin)` → `targetWin.focus()`
- 条件付き依存: `if (targetWin)` → `targetWin.BrowserCommands.openFileWindow()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `window.openDialog()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `newWin.addEventListener()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `newWin.focus()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `newWin.BrowserCommands.openFileWindow()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIFilePicker`, `fp.displayDirectory`, `gLastOpenDirectory.path`, `nsIFilePicker.filterAll`, `nsIFilePicker.filterHTML`, `nsIFilePicker.filterImages`, `nsIFilePicker.filterPDF`, `nsIFilePicker.filterText`, `nsIFilePicker.filterXML`, `nsIFilePicker.modeOpen`, `window.browsingContext`, `window.location.href`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback_done()
- 位置: L325-336
- 役割: ファイル選択が確定したとき、最後に開いたフォルダを記録し、そのファイルを現在のタブで開く。
- 触るとき: ファイルを開いた後の最終フォルダ記憶やロード先を変えるとき。
- 条件付き依存: `if (fp.file)` → `fp.file.parent.QueryInterface()`
- 条件付き依存: `if (aResult == nsIFilePicker.returnOK)` → `openTrustedLinkIn()`
- 参照: `Ci.nsIFile`, `fp.file`, `fp.fileURL.spec`, `gLastOpenDirectory.path`, `nsIFilePicker.returnOK`
- XPCOM: [`nsIFile`](../../components/shell/nsIShellService.idl.md)

## closeTabOrWindow()
- 位置: L356-400
- 役割: タブを閉じる。複数選択中なら選択タブをまとめて閉じ、固定タブへのショートカットは最初の非固定タブを選ぶ。
- 触るとき: Ctrl+W などの閉じるショートカットの対象決定を変えるとき。
- 呼び出し先: `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.removeCurrentTab()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `closeWindow()`
- 条件付き依存: `if (gBrowser.multiSelectedTabsCount)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (gBrowser.multiSelectedTabsCount)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if ( event && (event.ctrlKey || event.metaKey || event.altKey) && gBrowser.selectedTab.pinned )` → `gBrowser.visibleTabs.find()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `event.altKey`, `event.ctrlKey`, `event.metaKey`, `gBrowser.TabMetrics.METRIC_SOURCE.KEYBOARD`, `gBrowser.multiSelectedTabsCount`, `gBrowser.selectedTab`, `gBrowser.selectedTab.pinned`, `tab.pinned`, `window.location.href`

## tryToCloseWindow()
- 位置: L402-406
- 役割: WindowIsClosing の確認を経て窓を閉じる。
- 触るとき: 窓を閉じる前の確認処理を変えるとき。
- 呼び出し先: `WindowIsClosing()`
- 条件付き依存: `if (WindowIsClosing(event))` → `window.close()`

## returnToOpenerFromPiP()
- 位置: L415-425
- 役割: Document Picture-in-Picture 窓から開き元のタブを前面にし、その後 PiP 窓を閉じる。
- 触るとき: PiP 窓を閉じて元のタブに戻る動作を変えるとき。
- 呼び出し先: `openerWindow.focus()`, `openerWindow.gBrowser.getTabForBrowser()`, `this.tryToCloseWindow()`
- 参照: `gBrowser.selectedBrowser.browsingContext.opener`, `openerBC.embedderElement`, `openerBrowser.documentGlobal`, `openerWindow.gBrowser.selectedTab`

## viewSourceOfDocument()
- 位置: async L446-512
- 役割: ソース表示用のタブを作り、外部エディタ設定があればそれを使い、無ければ内部の view-source で表示する。
- 触るとき: ソース表示のタブ生成、リモートタイプ、新規窓での開き方を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `tabBrowser.addTab()`, `tabBrowser.getBrowserForTab()`, `top.gViewSourceUtils.viewSourceInBrowser()`
- 条件付き依存: `if (Services.prefs.getBoolPref("view_source.editor.external"))` → `top.gViewSourceUtils.openInExternalEditor()`
- 条件付き依存: `if (!(args.browser))` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (!tabBrowser || !window.toolbar.visible)` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!tabBrowser || !window.toolbar.visible)` → `BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (inNewWindow)` → `tabBrowser.hideTab()`
- 条件付き依存: `if (inNewWindow)` → `tabBrowser.replaceTabWithWindow()`
- 参照: `args.URL`, `args.browser`, `args.browser.browsingContext.group.id`, `args.browser.remoteType`, `args.viewSourceBrowser`, `browserWindow.gBrowser`, `window.toolbar.visible`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## viewSource()
- 位置: L522-528
- 役割: 指定ブラウザのルート文書のソースを viewSourceOfDocument に渡して表示する。
- 触るとき: ブラウザ単位のソース表示の入口を変えるとき。
- 呼び出し先: `this.viewSourceOfDocument()`
- 参照: `browser.currentURI.spec`, `browser.outerWindowID`

## pageInfo()
- 位置: L537-576
- 役割: 同じ URL とプライバシー状態のページ情報窓があれば前面に出して再初期化し、無ければ新しく開く。
- 触るとき: ページ情報窓の再利用条件や引数を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.wm.getEnumerator()`, `currentWindow.document.documentElement.getAttribute()`, `openDialog()`
- 条件付き依存: `if ( currentWindow.document.documentElement.getAttribute("relatedUrl") == documentURL && PrivateBrowsingUtils.isWindowPrivate(currentWindow) == isPrivate )` → `currentWindow.focus()`
- 条件付き依存: `if ( currentWindow.document.documentElement.getAttribute("relatedUrl") == documentURL && PrivateBrowsingUtils.isWindowPrivate(currentWindow) == isPrivate )` → `currentWindow.resetPageInfo()`
- 参照: `currentWindow.closed`, `window.gBrowser.selectedBrowser.currentURI.spec`
- XPCOM: `Services.wm`

## fullScreen()
- 位置: L578-580
- 役割: 全画面表示を切り替える。キオスクモードでは常に全画面にする。
- 触るとき: 全画面切り替えの条件を変えるとき。
- 参照: `BrowserHandler.kiosk`, `window.fullScreen`

## downloadsUI()
- 位置: L582-588
- 役割: ダウンロード一覧を開く。プライベート窓では about:downloads をタブで開き、通常窓では Places の Downloads を表示する。
- 触るとき: ダウンロード画面の開き方を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `openTrustedLinkIn()`
- 条件付き依存: `if (!(PrivateBrowsingUtils.isWindowPrivate(window)))` → `PlacesCommandHook.showPlacesOrganizer()`

## forceEncodingDetection()
- 位置: L590-593
- 役割: 選択中のブラウザで文字コードの自動判定を行い、文字コード変更付きで再読込する。
- 触るとき: 文字コード判定の再実行の仕組みを変えるとき。
- 呼び出し先: `gBrowser.reloadWithFlags()`, `gBrowser.selectedBrowser.forceEncodingDetection()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_CHARSET_CHANGE`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## processCloseRequest()
- 位置: L595-597
- 役割: 選択中ブラウザのプロセスに閉じる要求を渡す。
- 触るとき: コンテンツプロセスへの閉じる要求の経路を調べるとき。
- 呼び出し先: `gBrowser.selectedBrowser.processCloseRequest()`
