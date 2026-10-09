# browser/base/content/browser-commands.js

source: browser/base/content/browser-commands.js
source-hash: 757c5b16612c96f327798f9e47c83144668074f0
lines: 599

## <module>
- 役割: (未記入)

## back()
- 位置: L12-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (where == "current")` → `gBrowser.goBack()`
- 条件付き依存: `if (!(where == "current"))` → `duplicateTabIn()`
- 参照: `gBrowser.selectedTab`

## forward()
- 位置: L24-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (where == "current")` → `gBrowser.goForward()`
- 条件付き依存: `if (!(where == "current"))` → `duplicateTabIn()`
- 参照: `gBrowser.selectedTab`

## handleBackspace()
- 位置: L36-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `goDoCommand()`, `this.back()`
- XPCOM: `Services.prefs`

## handleShiftBackspace()
- 位置: L47-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `goDoCommand()`, `this.forward()`
- XPCOM: `Services.prefs`

## gotoHistoryIndex()
- 位置: L58-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getRootEvent()`, `BrowserUtils.whereToOpenLink()`, `Number()`, `aEvent.target.getAttribute()`, `duplicateTabIn()`
- 条件付き依存: `if (where == "current")` → `gBrowser.gotoIndex()`
- 参照: `gBrowser.selectedTab`

## addTabSplitView()
- 位置: L85-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.addTabSplitView()`, `gBrowser.addTrustedTab()`
- 参照: `gBrowser.selectedTab`, `gBrowser.selectedTab.hidden`, `gBrowser.selectedTab.pinned`, `gBrowser.selectedTab.splitview`

## separateTabSplitView()
- 位置: L103-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.selectedTab?.splitview?.unsplitTabs()`

## duplicateTab()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `duplicateTabIn()`
- 参照: `gBrowser.selectedTab`

## reloadOrDuplicate()
- 位置: L111-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getRootEvent()`, `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (aEvent.shiftKey && !backgroundTabModifier)` → `this.reloadSkipCache()`
- 条件付き依存: `if (where == "current")` → `this.reload()`
- 条件付き依存: `if (!(where == "current"))` → `duplicateTabIn()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `gBrowser.selectedTab`

## reload()
- 位置: L130-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.currentURI.schemeIs()`, `gBrowser.reloadWithFlags()`
- 条件付き依存: `if (gBrowser.currentURI.schemeIs("view-source"))` → `this.reloadSkipCache()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## reloadSkipCache()
- 位置: L139-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.reloadWithFlags()`

## stop()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.webNavigation.stop()`
- 参照: `Ci.nsIWebNavigation.STOP_ALL`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## home()
- 位置: L148-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `HomePage.get()`, `OpenBrowserWindow()`, `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `aEvent?.preventDefault()`, `gBrowser.loadTabs()`, `homePage.split()`, `isBlankPageURL()`, `isInitialPage()`, `loadOneOrMoreURIs()`
- 条件付き依存: `if (isBlankPageURL(homePage))` → `gURLBar.select()`
- 条件付き依存: `if (!(isBlankPageURL(homePage)))` → `gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (!loadInBackground)` → `isBlankPageURL()`
- 条件付き依存: `if (notifyObservers)` → `Services.obs.notifyObservers()`
- 参照: `aEvent?.button`, `gBrowser.selectedBrowser.initialPageLoadedFromUserAction`, `gBrowser?.selectedTab.hidden`, `gBrowser?.selectedTab.pinned`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.scriptSecurityManager`

## openTab()
- 位置: L228-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `openTrustedLinkIn()`
- 条件付き依存: `if (event)` → `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (!werePassedURL && searchClipboard)` → `readFromClipboard()`
- 条件付き依存: `if (!werePassedURL && searchClipboard)` → `UrlbarShared.stripUnsafeProtocolOnPaste(clipboard).trim()`
- 条件付き依存: `if (!werePassedURL && searchClipboard)` → `UrlbarShared.stripUnsafeProtocolOnPaste()`
- 参照: `event?.button`, `options.allowThirdPartyFixup`
- XPCOM: `Services.obs` / `Services.prefs`

## openFileWindow()
- 位置: L288-354
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (fp.file)` → `fp.file.parent.QueryInterface()`
- 条件付き依存: `if (aResult == nsIFilePicker.returnOK)` → `openTrustedLinkIn()`
- 参照: `Ci.nsIFile`, `fp.file`, `fp.fileURL.spec`, `gLastOpenDirectory.path`, `nsIFilePicker.returnOK`
- XPCOM: [`nsIFile`](../../components/shell/nsIShellService.idl.md)

## closeTabOrWindow()
- 位置: L356-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.removeCurrentTab()`
- 条件付き依存: `if (window.location.href != AppConstants.BROWSER_CHROME_URL)` → `closeWindow()`
- 条件付き依存: `if (gBrowser.multiSelectedTabsCount)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (gBrowser.multiSelectedTabsCount)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if ( event && (event.ctrlKey || event.metaKey || event.altKey) && gBrowser.selectedTab.pinned )` → `gBrowser.visibleTabs.find()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `event.altKey`, `event.ctrlKey`, `event.metaKey`, `gBrowser.TabMetrics.METRIC_SOURCE.KEYBOARD`, `gBrowser.multiSelectedTabsCount`, `gBrowser.selectedTab`, `gBrowser.selectedTab.pinned`, `tab.pinned`, `window.location.href`

## tryToCloseWindow()
- 位置: L402-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WindowIsClosing()`
- 条件付き依存: `if (WindowIsClosing(event))` → `window.close()`

## returnToOpenerFromPiP()
- 位置: L415-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openerWindow.focus()`, `openerWindow.gBrowser.getTabForBrowser()`, `this.tryToCloseWindow()`
- 参照: `gBrowser.selectedBrowser.browsingContext.opener`, `openerBC.embedderElement`, `openerBrowser.documentGlobal`, `openerWindow.gBrowser.selectedTab`

## viewSourceOfDocument()
- 位置: async L446-512
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.viewSourceOfDocument()`
- 参照: `browser.currentURI.spec`, `browser.outerWindowID`

## pageInfo()
- 位置: L537-576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.wm.getEnumerator()`, `currentWindow.document.documentElement.getAttribute()`, `openDialog()`
- 条件付き依存: `if ( currentWindow.document.documentElement.getAttribute("relatedUrl") == documentURL && PrivateBrowsingUtils.isWindowPrivate(currentWindow) == isPrivate )` → `currentWindow.focus()`
- 条件付き依存: `if ( currentWindow.document.documentElement.getAttribute("relatedUrl") == documentURL && PrivateBrowsingUtils.isWindowPrivate(currentWindow) == isPrivate )` → `currentWindow.resetPageInfo()`
- 参照: `currentWindow.closed`, `window.gBrowser.selectedBrowser.currentURI.spec`
- XPCOM: `Services.wm`

## fullScreen()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BrowserHandler.kiosk`, `window.fullScreen`

## downloadsUI()
- 位置: L582-588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `openTrustedLinkIn()`
- 条件付き依存: `if (!(PrivateBrowsingUtils.isWindowPrivate(window)))` → `PlacesCommandHook.showPlacesOrganizer()`

## forceEncodingDetection()
- 位置: L590-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.reloadWithFlags()`, `gBrowser.selectedBrowser.forceEncodingDetection()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_CHARSET_CHANGE`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## processCloseRequest()
- 位置: L595-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.selectedBrowser.processCloseRequest()`
