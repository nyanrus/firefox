# browser/components/search/SearchUIUtils.sys.mjs

source: browser/components/search/SearchUIUtils.sys.mjs
source-hash: d2a1a93992f6a9565299c68a92ccdfa64e6480fa
lines: 623

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## SearchUIUtilsL10n()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L45-54
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.initialized)` → `this.updatePlaceholderNamePreference()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L61-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePlaceholderNamePreference()`

## showSearchServiceNotification()
- 位置: L84-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removalOfSearchEngineNotificationBox()`, `this.searchSettingsResetNotificationBox()`

## removalOfSearchEngineNotificationBox()
- 位置: async L108-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `openWin.gURLBar?.updatePlaceholder()`
- 条件付き依存: `if (win)` → `win.gNotificationBox.appendNotification()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `win.gNotificationBox.PRIORITY_SYSTEM`

## callback()
- 位置: L118-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`, `win.gNotificationBox.removeNotification()`

## searchSettingsResetNotificationBox()
- 位置: async L156-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.gNotificationBox.appendNotification()`
- 参照: `win.gNotificationBox.PRIORITY_SYSTEM`

## callback()
- 位置: L165-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`, `win.gNotificationBox.removeNotification()`

## addOpenSearchEngine()
- 位置: async L204-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.alertBC()`, `lazy.SearchService.addOpenSearchEngine()`, `lazy.SearchUIUtilsL10n.formatValues()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_CONTENT`, `browsingContext?.embedderElement?.contentPrincipal?.originAttributes`, `ex.type`, `lazy.SearchEngineInstallError`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt`

## searchEnginesURL()
- 位置: L260-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## updatePlaceholderNamePreference()
- 位置: async L271-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `lazy.SearchService.init()`
- 条件付き依存: `if (engine instanceof lazy.ConfigSearchEngine)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(engine instanceof lazy.ConfigSearchEngine))` → `Services.prefs.clearUserPref()`
- 参照: `engine.name`, `lazy.ConfigSearchEngine`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`
- XPCOM: `Services.prefs`

## webSearch()
- 位置: L300-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `focusUrlBarIfSearchFieldIsNotActive()`, `lazy.CustomizableUI.getPlacementOfWidget()`, `searchBar.parentElement.getAttribute()`, `window.document.getElementById()`
- 条件付き依存: `if ( window.location.href != AppConstants.BROWSER_CHROME_URL || window.gURLBar.readOnly )` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (topWindow && !topWindow.gURLBar.readOnly)` → `topWindow.focus()`
- 条件付き依存: `if (topWindow && !topWindow.gURLBar.readOnly)` → `SearchUIUtils.webSearch()`
- 条件付き依存: `if (!(topWindow && !topWindow.gURLBar.readOnly))` → `window.openDialog()`
- 条件付き依存: `if (!(topWindow && !topWindow.gURLBar.readOnly))` → `Services.obs.addObserver()`
- 条件付き依存: `if ( placement && searchBar && ((searchBar.parentElement.getAttribute("overflowedItem") == "true" && placement.area == lazy.CustomizableUI.AREA_NAVBAR) || placem...)` → `window.document.getElementById()`
- 条件付き依存: `if ( placement && searchBar && ((searchBar.parentElement.getAttribute("overflowedItem") == "true" && placement.area == lazy.CustomizableUI.AREA_NAVBAR) || placem...)` → `navBar.overflowable.show().then()`
- 条件付き依存: `if ( placement && searchBar && ((searchBar.parentElement.getAttribute("overflowedItem") == "true" && placement.area == lazy.CustomizableUI.AREA_NAVBAR) || placem...)` → `navBar.overflowable.show()`
- 条件付き依存: `if (window.fullScreen)` → `window.FullScreen.showNavToolbox()`
- 条件付き依存: `if (searchBar)` → `searchBar.select()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `lazy.CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `lazy.CustomizableUI.AREA_NAVBAR`, `placement.area`, `topWindow.gURLBar.readOnly`, `window.fullScreen`, `window.gURLBar.readOnly`, `window.location.href`
- XPCOM: `Services.obs` / `Services.prefs`

## observer()
- 位置: L319-327
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (subject == newWindow)` → `SearchUIUtils.webSearch()`
- 条件付き依存: `if (subject == newWindow)` → `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## focusUrlBarIfSearchFieldIsNotActive()
- 位置: L334-339
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!searchBar || window.document.activeElement != searchBar.inputField)` → `window.gURLBar.searchModeShortcut()`
- 参照: `searchBar.inputField`, `window.document.activeElement`

## focusSearchBar()
- 位置: L350-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `focusUrlBarIfSearchFieldIsNotActive()`, `searchBar.select()`, `window.document.getElementById()`
- XPCOM: `Services.prefs`

## loadSearch()
- 位置: async L423-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.getSubmission()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `window.openLinkIn()`
- 条件付き依存: `if (!engine)` → `lazy.SearchService.getDefaultPrivate()`
- 条件付き依存: `if (!engine)` → `lazy.SearchService.getDefault()`
- 参照: `engine.name`, `submission.postData`, `submission.uri.spec`, `tab?.linkedBrowser`, `window.gBrowser.selectedBrowser`

## loadSearchFromContext()
- 位置: async L507-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.createNullPrincipal()`, `lazy.BrowserUtils.getRootEvent()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.loadSearch()`
- 参照: `event.button`, `event.ctrlKey`, `lazy.SearchUtils.URL_TYPE.VISUAL_SEARCH`, `triggeringPrincipal.originAttributes`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## SearchNewTabComponentsRegistrant.constructor()
- 位置: L565-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`, `lazy.UrlbarPrefs.addObserver()`, `super()`
- 参照: `this.lazy`

## onUpdate()
- 位置: L573-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updated()`

## SearchNewTabComponentsRegistrant.destroy()
- 位置: L581-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.removeObserver()`

## SearchNewTabComponentsRegistrant.onNimbusChanged()
- 位置: L585-589
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (variable == "newtabFeatureGate")` → `this.updated()`

## SearchNewTabComponentsRegistrant.onPrefChanged()
- 位置: L591-595
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pref == "browser.nova.enabled")` → `this.updated()`

## SearchNewTabComponentsRegistrant.getComponents()
- 位置: L597-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `AboutNewTabComponentRegistry.TYPES.SEARCH`, `Services.appinfo`, `this.lazy.prefHandoffToAwesomebar`
- XPCOM: `Services.appinfo`
