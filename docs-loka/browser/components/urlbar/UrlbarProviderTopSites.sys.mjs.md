# browser/components/urlbar/UrlbarProviderTopSites.sys.mjs

source: browser/components/urlbar/UrlbarProviderTopSites.sys.mjs
source-hash: 412fa55be76f1292684d9eb5c4bc1a115ce42b19
lines: 510

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## sameUrlIgnoringRef()
- 位置: L43-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url1.replace()`, `url2.replace()`

## UrlbarProviderTopSites.constructor()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderTopSites.PRIORITY()
- 位置: L62-65
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderTopSites.type()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderTopSites.isActive()
- 位置: async L81-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.restrictInSearchMode()`
- 参照: `queryContext.restrictSource`, `queryContext.searchString`

## UrlbarProviderTopSites.getPriority()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderTopSites.startQuery()
- 位置: async L105-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `Services.prefs.getBoolPref()`, `TOP_SITES_ENABLED_PREFS.every()`, `addCallback()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarSearchUtils.engineForAlias()`, `sites.filter()`, `sites.map()`, `sites.slice()`, `this.logger.error()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.topsites.component.enabled"))` → `lazy.TopSites.getSites()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.topsites.component.enabled")))` → `lazy.AboutNewTab.getTopSites()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("sponsoredTopSites"))` → `sites.filter()`
- 条件付き依存: `if (UrlbarProviderTopSites.topSitesRows === undefined)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `lazy.UrlbarProviderOpenTabs.getOpenTabUrls( queryContext.isPrivate ).forEach()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `lazy.UrlbarProviderOpenTabs.getOpenTabUrls()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `userContextIds.add()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `tabUrlsToContextIds.set()`
- 条件付き依存: `if (tabUrlsToContextIds)` → `tabUrlsToContextIds.get()`
- 条件付き依存: `if (tabUrlsToContextIds)` → `site.url.replace()`
- 条件付き依存: `if (tabUserContextIds.size)` → `sameUrlIgnoringRef()`
- 条件付き依存: `if (tabUserContextIds.size)` → `UrlbarUtils.getUserContextData()`
- 条件付き依存: `if (tabUserContextIds.size)` → `addCallback()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("resultExplanationsFeatureGate") && lazy.UrlbarPrefs.get("suggest.history") )` → `this.#fetchLastVisit()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.bookmark"))` → `lazy.PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if (bookmark)` → `bookmark.dateAdded.getTime()`
- 条件付き依存: `if (!engine && site.url)` → `URL.parse()`
- 条件付き依存: `if (host)` → `lazy.UrlbarSearchUtils.enginesForDomainPrefix()`
- 参照: `URL.parse(site.url)?.hostname`, `UrlbarProviderTopSites.topSitesRows`, `engine.name`, `lazy.TOP_SITES_DEFAULT_ROWS`, `lazy.TOP_SITES_MAX_SITES_PER_ROW`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `link.favicon`, `link.hostname`, `link.isPinned`, `link.label`, `link.lastVisitDate`, `link.searchTopSite`, `link.smallFavicon`, `link.sponsored_position`, `link.title`, `link.type`, `link.url`, `link.url_urlbar`, `payload.bookmarkDateMs`, `payload.isBlockable`, `payload.lastVisit`, `payload.sponsoredClickUrl`, `payload.sponsoredTileId`, `payload.url`, `payload.userContext`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.userContextId`, `site.favicon`, `site.isPinned`, `site.isSponsored`, `site.lastVisitDate`, `site.sponsoredClickUrl`, `site.sponsoredTileId`, `site.sponsored_position`, `site.subtype`, `site.title`, `site.type`, `site.url`, `tabUserContextIds.size`, `this.queryInstance`
- XPCOM: `Services.prefs`

## UrlbarProviderTopSites.onImpression()
- 位置: L360-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `providerVisibleResults.forEach()`
- 条件付き依存: `if (result?.payload.isSponsored)` → `Glean.contextualServicesTopsites.impression[`urlbar_${index}`].add()`
- 参照: `Glean.contextualServicesTopsites.impression`, `queryContext.isPrivate`, `result?.payload.isSponsored`

## UrlbarProviderTopSites.onEngagement()
- 位置: async L379-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.NewTabUtils.activityStreamLinks.blockURL()`, `lazy.PlacesUtils.history.remove()`
- 参照: `result.payload.isBlockable`, `result.payload.url`

## UrlbarProviderTopSites.getResultCommands()
- 位置: L404-419
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.isBlockable`

## UrlbarProviderTopSites.#fetchLastVisit()
- 位置: async L421-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.execute()`, `lazy.PlacesUtils.promiseDBConnection()`, `rows[0]?.getResultByName()`
- 参照: `lazy.PlacesUtils.history.TRANSITIONS.REDIRECT_PERMANENT`, `lazy.PlacesUtils.history.TRANSITIONS.REDIRECT_TEMPORARY`, `new URL(url).href`

## UrlbarProviderTopSites.addTopSitesListener()
- 位置: L471-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `UrlbarProviderTopSites.#topSitesListeners.push()`
- 条件付き依存: `if (!UrlbarProviderTopSites.#topSitesListeners)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.topsites.component.enabled"))` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.topsites.component.enabled")))` → `Services.obs.addObserver()`
- 条件付き依存: `if (!UrlbarProviderTopSites.#topSitesListeners)` → `Services.prefs.addObserver()`
- 参照: `UrlbarProviderTopSites.#callTopSitesListeners`, `UrlbarProviderTopSites.#topSitesListeners`
- XPCOM: `Services.obs` / `Services.prefs`

## UrlbarProviderTopSites.#callTopSitesListeners()
- 位置: L490-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarProviderTopSites.#topSitesListeners[i].get()`
- 条件付き依存: `if (!listener)` → `UrlbarProviderTopSites.#topSitesListeners.splice()`
- 条件付き依存: `if (!(!listener))` → `listener()`
- 参照: `UrlbarProviderTopSites.#topSitesListeners`, `UrlbarProviderTopSites.#topSitesListeners.length`
