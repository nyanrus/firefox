# browser/components/urlbar/UrlbarProviderSearchTips.sys.mjs

source: browser/components/urlbar/UrlbarProviderSearchTips.sys.mjs
source-hash: 162beebeda8195e3d80d1369323065c967997548
lines: 535

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.SearchStaticData.getAlternateDomains()`, `lazy.SearchStaticData.getAlternateDomains("www.google.com") .map()`, `str.slice()`, `str.slice("www.google.".length).replaceAll()`

## UrlbarProviderSearchTips.constructor()
- 位置: L100-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `lazy.UrlbarPrefs.get()`, `super()`
- 参照: `UrlbarProviderSearchTips.#instance`, `UrlbarShared.SEARCH_TIP_TYPE`, `this._seenWindows`, `this.disableTipsForCurrentSession`

## UrlbarProviderSearchTips.PRIORITY()
- 位置: L124-127
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderSearchTips.type()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderSearchTips.isActive()
- 位置: async L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.cfrFeaturesUserPref`, `this.currentTip`

## UrlbarProviderSearchTips.getPriority()
- 位置: L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarProviderSearchTips.PRIORITY`

## UrlbarProviderSearchTips.startQuery()
- 位置: async L162-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `addCallback()`, `lazy.SearchService.getDefault()`, `this.#makeResult()`
- 参照: `UrlbarShared.SEARCH_TIP_TYPE.NONE`, `UrlbarShared.SEARCH_TIP_TYPE.ONBOARD`, `UrlbarShared.SEARCH_TIP_TYPE.REDIRECT`, `defaultEngine.name`, `this.currentTip`, `this.queryInstance`, `this.showedTipTypeInCurrentEngagement`

## UrlbarProviderSearchTips.#pickResult()
- 位置: L214-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.set()`, `window.gURLBar.focus()`, `window.gURLBar.removeAttribute()`, `window.gURLBar.setPageProxyState()`
- 参照: `result.payload.type`, `window.gURLBar.value`

## UrlbarProviderSearchTips.onEngagement()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pickResult()`
- 参照: `controller.browserWindow`, `details.result`

## UrlbarProviderSearchTips.onSearchSessionEnd()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.SEARCH_TIP_TYPE.NONE`, `this.showedTipTypeInCurrentEngagement`

## UrlbarProviderSearchTips.onLocationChange()
- 位置: async L255-264
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (UrlbarProviderSearchTips.#instance)` → `UrlbarProviderSearchTips.#instance.onLocationChange()`
- 参照: `UrlbarProviderSearchTips.#instance`

## UrlbarProviderSearchTips.onLocationChange()
- 位置: async L278-335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._maybeShowTipForUrl()`, `this._maybeShowTipForUrl(uri.spec, window).catch()`, `this._seenWindows.has()`, `this.logger.error()`
- 条件付き依存: `if (!this._seenWindows.has(window))` → `this._seenWindows.add()`
- 条件付き依存: `if (!this._seenWindows.has(window))` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 条件付き依存: `if (!this._seenWindows.has(window))` → `timer.initWithCallback()`
- 条件付き依存: `if ( this.showedTipTypeInCurrentEngagement != UrlbarShared.SEARCH_TIP_TYPE.NONE )` → `window.gURLBar.view.close()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `UrlbarShared.SEARCH_TIP_TYPE.NONE`, `lazy.cfrFeaturesUserPref`, `this._onLocationChangeInstance`, `this.disableTipsForCurrentSession`, `this.showedTipTypeInCurrentEngagement`, `uri.spec`, `webProgress.isTopLevel`, `window.gBrowserInit.firstContentWindowPaintPromise`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `@mozilla.org/timer;1`

## UrlbarProviderSearchTips._maybeShowTipForUrl()
- 位置: async L346-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `["about:newtab", "about:home"].includes()`, `isBrowserShowingNotification()`, `isDefaultEngineHomepage()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`, `lazy.setTimeout()`, `window.gURLBar.getAttribute()`, `window.gURLBar.search()`
- 参照: `UrlbarShared.SEARCH_TIP_TYPE.ONBOARD`, `UrlbarShared.SEARCH_TIP_TYPE.REDIRECT`, `lazy.LaterRun.hoursSinceInstall`, `lazy.LaterRun.hoursSinceUpdate`, `this._maybeShowTipForUrlInstance`, `this.currentTip`, `this.disableTipsForCurrentSession`, `window.gURLBar.value`

## UrlbarProviderSearchTips.#makeResult()
- 位置: L425-437
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.TIP`, `lazy.UrlbarResult`

## isBrowserShowingNotification()
- 位置: async L440-499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DefaultBrowserCheck.willCheckDefaultBrowser()`, `navbar.querySelectorAll()`, `node.getAttribute()`, `window.document.getElementById()`, `window.gBrowser.getNotificationBox()`
- 条件付き依存: `if (pageActions)` → `child.getAttribute()`
- 参照: `lazy.AppMenuNotifications.activeNotification`, `lazy.AppMenuNotifications.activeNotification.dismissed`, `lazy.AppMenuNotifications.activeNotification.options.badgeOnly`, `pageActions.childNodes`, `window.PopupNotifications.isPanelOpen`, `window.gBrowser.getNotificationBox().currentNotification`, `window.gDialogBox.isOpen`, `window.gNotificationBox.currentNotification`, `window.gURLBar.view.isOpen`

## isDefaultEngineHomepage()
- 位置: async L510-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `homepageMatches.domainPath.test()`, `lazy.SUPPORTED_ENGINES.get()`, `lazy.SearchService.getDefault()`, `url.hostname.concat()`, `url.searchParams.has()`
- 参照: `defaultEngine.name`, `homepageMatches.prohibitedSearchParams`, `url.pathname`
