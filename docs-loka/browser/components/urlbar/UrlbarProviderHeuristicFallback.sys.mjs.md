# browser/components/urlbar/UrlbarProviderHeuristicFallback.sys.mjs

source: browser/components/urlbar/UrlbarProviderHeuristicFallback.sys.mjs
source-hash: be9c68d0683c33214e4297cbb5cf189dedfac7a5
lines: 348

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderHeuristicFallback.constructor()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderHeuristicFallback.type()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderHeuristicFallback.isActive()
- 位置: async L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `queryContext.searchString.length`

## UrlbarProviderHeuristicFallback.getPriority()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderHeuristicFallback.startQuery()
- 位置: async L68-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._searchModeKeywordResult()`
- 条件付き依存: `if (queryContext.navigationEnabled)` → `UrlbarProviderHeuristicFallback.matchUnknownUrl()`
- 条件付き依存: `if (result)` → `addCallback()`
- 条件付き依存: `if (result)` → `URL.canParse()`
- 条件付き依存: `if (!URL.canParse(str))` → `lazy.UrlUtils.looksLikeOrigin()`
- 条件付き依存: `if (!URL.canParse(str))` → `lazy.UrlUtils.REGEXP_COMMON_EMAIL.test()`
- 条件付き依存: `if ( queryContext.keywordEnabled && (lazy.UrlUtils.looksLikeOrigin(str, { noIp: true, noPort: true, }) || lazy.UrlUtils.REGEXP_COMMON_EMAIL.test(str)) )` → `this._engineSearchResult()`
- 条件付き依存: `if ( queryContext.keywordEnabled && (lazy.UrlUtils.looksLikeOrigin(str, { noIp: true, noPort: true, }) || lazy.UrlUtils.REGEXP_COMMON_EMAIL.test(str)) )` → `addCallback()`
- 条件付き依存: `if ( queryContext.keywordEnabled || queryContext.restrictSource == lazy.UrlbarShared.RESULT_SOURCE.SEARCH || queryContext.searchMode )` → `this._engineSearchResult()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.keywordEnabled`, `queryContext.navigationEnabled`, `queryContext.restrictSource`, `queryContext.searchMode`, `queryContext.searchString`, `this.queryInstance`

## UrlbarProviderHeuristicFallback.matchUnknownUrl()
- 位置: L127-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.stripURLPrefix()`, `["http:", "https:", "ftp:", "chrome:"].includes()`, `lazy.UrlbarShared.SEARCH_MODE_RESTRICT.has()`, `lazy.UrlbarShared.prepareUrlForDisplay()`, `lazy.UrlbarShared.unEscapeURIForUI()`, `searchUrl.endsWith()`, `uri.toString()`
- 条件付き依存: `if (hostExpected && (searchUrl.endsWith("/") || uri.pathname.length > 1))` → `uri.toString().lastIndexOf()`
- 条件付き依存: `if (hostExpected && (searchUrl.endsWith("/") || uri.pathname.length > 1))` → `uri.toString()`
- 条件付き依存: `if (hostExpected && (searchUrl.endsWith("/") || uri.pathname.length > 1))` → `uri.toString().slice()`
- 参照: `Cr.NS_ERROR_MALFORMED_URI`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.fixupError`, `queryContext.fixupInfo.href`, `queryContext.fixupInfo?.href`, `queryContext.fixupInfo?.isSearch`, `queryContext.keywordEnabled`, `queryContext.navigationInSearchModeEnabled`, `queryContext.restrictSource`, `queryContext.restrictToken?.value`, `queryContext.searchMode`, `queryContext.searchMode.engineName`, `queryContext.searchString`, `queryContext.trimmedSearchString`, `uri.host`, `uri.pathname`, `uri.pathname.length`, `uri.protocol`

## UrlbarProviderHeuristicFallback._searchModeKeywordResult()
- 位置: async L244-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.substringAfter()`, `lazy.UrlUtils.REGEXP_SPACES_START.test()`, `lazy.UrlbarShared.SEARCH_MODE_RESTRICT.has()`, `query.trimStart()`
- 条件付き依存: `if (queryContext.restrictSource == lazy.UrlbarShared.RESULT_SOURCE.SEARCH)` → `this._engineSearchResult()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.restrictSource`, `queryContext.sapName`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens.length`, `queryContext.tokens[0].value`

## UrlbarProviderHeuristicFallback._engineSearchResult()
- 位置: async L301-346
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (queryContext.searchMode?.engineName)` → `lazy.UrlbarSearchUtils.getEngineByName()`
- 条件付き依存: `if (!(queryContext.searchMode?.engineName))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if ( queryContext.tokens[0] && queryContext.tokens[0].value === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH )` → `UrlbarUtils.substringAfter( query, queryContext.tokens[0].value ).trim()`
- 条件付き依存: `if ( queryContext.tokens[0] && queryContext.tokens[0].value === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH )` → `UrlbarUtils.substringAfter()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.ICON.SEARCH_GLASS`, `lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.isPrivate`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0].value`
