# browser/components/urlbar/ActionsProviderContextualSearch.sys.mjs

source: browser/components/urlbar/ActionsProviderContextualSearch.sys.mjs
source-hash: f966cb15a14b45aea81cc85c30b3846419a66723
lines: 452

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `XPCOMUtils.declareLazy()`

## ProviderContextualSearch.constructor()
- 位置: L63-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesObservers.addListener()`, `super()`, `this.handlePlacesEvents.bind()`
- 参照: `this.#placesObserver`

## ProviderContextualSearch.name()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)

## ProviderContextualSearch.isActive()
- 位置: L77-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.trimmedSearchString`

## ProviderContextualSearch.queryActions()
- 位置: async L86-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.matchEngine()`
- 条件付き依存: `if (this.#resultEngine)` → `this.#createActionResult()`
- 参照: `this.#resultEngine`

## ProviderContextualSearch.onSearchSessionEnd()
- 位置: L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hostEngines.clear()`

## ProviderContextualSearch.#createActionResult()
- 位置: async L101-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine?.getIconURL()`
- 参照: `engine.name`, `engine.title`, `engine?.icon`, `this.name`

## ProviderContextualSearch.matchEngine()
- 位置: async L123-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `this.#hostEngines.has()`, `this.#matchTabToSearchEngine()`
- 条件付き依存: `if (host && !this.#hostEngines.has(host))` → `this.#matchInstalledEngine()`
- 条件付き依存: `if (!hostEngine)` → `lazy.SearchService.findContextualSearchEngineByHost()`
- 条件付き依存: `if (host && !this.#hostEngines.has(host))` → `this.#hostEngines.set()`
- 条件付き依存: `if (host)` → `this.#hostEngines.get()`
- 条件付き依存: `if (browser)` → `lazy.OpenSearchManager.getEngines()`
- 参照: `browser.currentURI.host`, `cachedEngine.engine.name`, `defaultEngine.name`, `hostEngine.engine.name`, `lazy.BrowserWindowTracker.getTopWindow()?.gBrowser.selectedBrowser`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `openSearchEngines.length`, `queryContext.isPrivate`

## ProviderContextualSearch.onLocationChange()
- 位置: async L210-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#visitedEngineDomains.has()`, `uri.scheme.startsWith()`
- 条件付き依存: `if (this.#visitedEngineDomains.has(uri.host))` → `this.#visitedEngineDomains.set()`
- 参照: `uri.host`

## ProviderContextualSearch.#matchInstalledEngine()
- 位置: async L221-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarSearchUtils.enginesForDomainPrefix()`
- 参照: `engines.length`

## ProviderContextualSearch.#matchTabToSearchEngine()
- 位置: async L234-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.toLocaleLowerCase()`, `engine.aliases.map()`, `engine.name.toLocaleLowerCase()`, `engineAliases.some()`, `lazy.SearchService.getVisibleEngines()`, `matches()`, `queryContext.trimmedSearchString.toLocaleLowerCase()`, `this.#engineDomainHasRecentVisits()`, `this.#shouldskipRecentVisitCheck()`
- 参照: `defaultEngine.name`, `engine.name`, `engine.searchUrlDomain`, `lazy.SearchService.defaultEngine`

## matches()
- 位置: L243-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `name.includes()`, `name.startsWith()`
- 参照: `search.length`

## ProviderContextualSearch.#engineDomainHasRecentVisits()
- 位置: async L281-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `this.#visitedEngineDomains.has()`, `this.#visitedEngineDomains.set()`
- 条件付き依存: `if (this.#visitedEngineDomains.has(host))` → `this.#visitedEngineDomains.get()`
- 参照: `rows.length`

## ProviderContextualSearch.#shouldskipRecentVisitCheck()
- 位置: async L302-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `query.length`
- XPCOM: `Services.prefs`

## ProviderContextualSearch.onPick()
- 位置: L326-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pickAction()`, `this.pickAction(queryContext, controller, details.searchSource).catch()`
- 参照: `console.error`, `details.searchSource`

## ProviderContextualSearch.pickAction()
- 位置: async L339-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `lazy.SearchService.shouldShowInstallPrompt()`, `this.#performSearch()`
- 条件付き依存: `if (type == OPEN_SEARCH_ENGINE)` → `Services.io.newURI()`
- 条件付き依存: `if (type == OPEN_SEARCH_ENGINE)` → `Services.eTLD.getSchemelessSite()`
- 条件付き依存: `if (type == OPEN_SEARCH_ENGINE)` → `lazy.loadAndParseOpenSearchEngine()`
- 条件付き依存: `if ( !queryContext.isPrivate && type != INSTALLED_ENGINE && Services.policies.isAllowed("installSearchEngine") && (await lazy.SearchService.shouldShowInstallProm...)` → `this.#showInstallPrompt()`
- 参照: `engine.uri`, `lazy.OpenSearchEngine`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.searchString`, `this.#resultEngine`, `this.#resultEngine.key`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.policies`

## ProviderContextualSearch.handlePlacesEvents()
- 位置: L379-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#visitedEngineDomains.clear()`

## ProviderContextualSearch.#performSearch()
- 位置: async L392-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.SearchUIUtils.loadSearch()`
- 条件付き依存: `if (enterSearchMode)` → `controller.input.search()`
- 参照: `controller.browserWindow`, `engine.aliases`, `engine.name`
- XPCOM: `Services.scriptSecurityManager`

## ProviderContextualSearch.#showInstallPrompt()
- 位置: L420-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.gNotificationBox.appendNotification()`
- 参照: `controller.browserWindow.gNotificationBox.PRIORITY_INFO_LOW`, `engineData.name`

## ProviderContextualSearch.callback()
- 位置: L424-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.addSearchEngine()`

## ProviderContextualSearch.callback()
- 位置: L430-430
- 役割: (未記入)
- 触るとき: (未記入)
