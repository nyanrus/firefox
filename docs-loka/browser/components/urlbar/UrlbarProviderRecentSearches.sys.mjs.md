# browser/components/urlbar/UrlbarProviderRecentSearches.sys.mjs

source: browser/components/urlbar/UrlbarProviderRecentSearches.sys.mjs
source-hash: 43fb936974e91b999db21263753a6b2bcc634849
lines: 178

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderRecentSearches.constructor()
- 位置: L34-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `super()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`
- XPCOM: `Services.obs`

## UrlbarProviderRecentSearches.type()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderRecentSearches.isActive()
- 位置: async L46-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.isSearchbarSAP`, `queryContext.restrictSource`, `queryContext.searchString`

## UrlbarProviderRecentSearches.getPriority()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderRecentSearches.onEngagement()
- 位置: L77-92
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.FormHistory.update()`
- 条件付き依存: `if (details.selType == "dismiss")` → `console.error()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `details.selType`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `result.payload.suggestion`

## UrlbarProviderRecentSearches.startQuery()
- 位置: async L101-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.urlFormatter.formatURLPref()`, `addCallback()`, `lazy.FormHistory.search()`, `lazy.UrlbarPrefs.get()`, `results.filter()`, `results.sort()`
- 条件付き依存: `if (queryContext.searchMode?.engineName)` → `lazy.UrlbarSearchUtils.getEngineByName()`
- 条件付き依存: `if (!(queryContext.searchMode?.engineName))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if (!queryContext.isSearchbarSAP)` → `parseInt()`
- 条件付き依存: `if (!queryContext.isSearchbarSAP)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lastDefaultChanged != -1)` → `Math.min()`
- 条件付き依存: `if ( !queryContext.isSearchbarSAP && results.length > lazy.UrlbarPrefs.get("recentsearches.maxResults") )` → `lazy.UrlbarPrefs.get()`
- 参照: `a.lastUsed`, `b.lastUsed`, `engine.name`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.isPrivate`, `queryContext.isSearchbarSAP`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `result.lastUsed`, `result.value`, `results.length`
- XPCOM: `Services.urlFormatter`

## UrlbarProviderRecentSearches.observe()
- 位置: L170-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Date.now().toString()`, `lazy.UrlbarPrefs.set()`
- 参照: `lazy.SearchUtils.MODIFIED_TYPE.DEFAULT`
