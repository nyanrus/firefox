# browser/components/urlbar/UrlbarProviderAutofill.sys.mjs

source: browser/components/urlbar/UrlbarProviderAutofill.sys.mjs
source-hash: 92d7a4b1da39753d3db65c9066abd885bd053aa1
lines: 1313

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.PlacesUtils.history.pageFrecencyThreshold()`, `originQuery()`, `parseFloat()`, `urlQuery()`

## inputHistoryPicksToUseCount()
- 位置: L84-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.frecencyDecayRate`

## urlUseCountThreshold()
- 位置: L98-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `inputHistoryPicksToUseCount()`
- 参照: `lazy.urlMinPicks`, `lazy.urlPicksAgeDays`

## effectiveSources()
- 位置: L110-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.sources.includes()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.historyEnabled`

## originQuery()
- 位置: L173-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `where.includes()`

## urlQuery()
- 位置: L268-318
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderAutofill.constructor()
- 位置: L441-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderAutofill.type()
- 位置: L448-450
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderAutofill.isActive()
- 位置: async L459-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.stripURLPrefix()`, `lazy.UrlUtils.REGEXP_SPACES.test()`, `lazy.UrlbarPrefs.get()`, `queryContext.sources.includes()`, `queryContext.tokens.some()`, `this._getAutofillResult()`, `this._strippedPrefix.toLowerCase()`
- 参照: `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `queryContext.allowAutofill`, `queryContext.searchString`, `queryContext.searchString.length`, `queryContext.tokens.length`, `t.type`, `this._autofillData`, `this._searchString`, `this._strippedPrefix`, `this.queryInstance`

## UrlbarProviderAutofill.getPriority()
- 位置: L534-536
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderAutofill.startQuery()
- 位置: async L545-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`
- 条件付き依存: `if ( !this._autofillData || this._autofillData.instance != this.queryInstance )` → `this.logger.error()`
- 条件付き依存: `if (this._autofillData.fallbackResult)` → `addCallback()`
- 参照: `this._autofillData`, `this._autofillData.fallbackResult`, `this._autofillData.instance`, `this._autofillData.result`, `this.queryInstance`

## UrlbarProviderAutofill.cancelQuery()
- 位置: L567-571
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._autofillData`, `this._autofillData?.instance`, `this.queryInstance`

## UrlbarProviderAutofill.onEngagement()
- 位置: async L578-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.dismissAutofill()`
- 条件付き依存: `if (didRemove)` → `controller.input.setValue()`
- 条件付き依存: `if (didRemove)` → `controller.input.startQuery()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `RESULT_MENU_COMMANDS.DISMISS_AUTOFILL`, `details.selType`, `queryContext.searchString`, `result.payload.url`

## UrlbarProviderAutofill.getResultCommands()
- 位置: L608-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( result.autofill.type === "adaptive_url" || result.autofill.type === "adaptive_origin" || result.autofill.type === "origin" )` → `lazy.UrlbarShared.isOriginUrl()`
- 条件付き依存: `if (!isPrivate)` → `resultArray.push()`
- 条件付き依存: `if (!isOrigin)` → `resultArray.push()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `RESULT_MENU_COMMANDS.DISMISS_AUTOFILL`, `result.autofill`, `result.autofill.type`, `result.payload.url`, `resultArray.length`

## UrlbarProviderAutofill.getTopHostOverThreshold()
- 位置: async L657-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conditions.join()`, `db.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `new Array(hosts.length).fill()`, `new Array(hosts.length).fill("?").join()`, `rows[0].getResultByName()`, `sources.includes()`
- 条件付き依存: `if ( sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY) && sources.includes(lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS) )` → `conditions.push()`
- 条件付き依存: `if (!( sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY) && sources.includes(lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS) ))` → `sources.includes()`
- 条件付き依存: `if (sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY))` → `conditions.push()`
- 条件付き依存: `if (!(sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY)))` → `sources.includes()`
- 条件付き依存: `if (sources.includes(lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS))` → `conditions.push()`
- 参照: `conditions.length`, `hosts.length`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `queryContext.sources`, `rows.length`

## UrlbarProviderAutofill._getOriginQuery()
- 位置: L727-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `effectiveSources()`, `lazy.UrlbarPrefs.get()`, `searchStr.toLowerCase()`, `this._searchString.endsWith()`, `this._searchString.slice()`
- 参照: `QUERYTYPE.AUTOFILL_ORIGIN`, `opts.prefix`, `this._searchString`, `this._strippedPrefix`

## UrlbarProviderAutofill._getUrlQuery()
- 位置: L787-851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `effectiveSources()`, `host.split()`, `host.split("").reverse()`, `host.split("").reverse().join()`, `hostMatch[0].toLowerCase()`, `strippedURL.substr()`, `urlQueryHostRegexp.exec()`
- 条件付き依存: `if (this._strippedPrefix)` → `strippedURL.substr()`
- 条件付き依存: `if (historyAllowed && bookmarksAllowed)` → `lazy.UrlbarPrefs.get()`
- 参照: `QUERYTYPE.AUTOFILL_URL`, `host.length`, `lazy.pageFrecencyThreshold`, `opts.adaptiveAutofillEnabled`, `opts.pageFrecencyThreshold`, `opts.prefix`, `queryContext.trimmedSearchString`, `this._searchString`, `this._strippedPrefix`, `this._strippedPrefix.length`

## UrlbarProviderAutofill._getAdaptiveHistoryQuery()
- 位置: L853-947
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Object.assign()`, `effectiveSources()`, `lazy.UrlbarPrefs.get()`, `urlUseCountThreshold()`
- 参照: `QUERYTYPE.AUTOFILL_ADAPTIVE`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.pageFrecencyThreshold`, `params.pageFrecencyThreshold`, `queryContext.lowerCaseSearchString`, `this._searchString`, `this._strippedPrefix`

## UrlbarProviderAutofill._processRow()
- 位置: L958-1132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fixedURL.substring()`, `lazy.UrlbarShared.canAutofillURL()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.isOriginUrl()`, `row.getResultByName()`, `strippedURL.toLowerCase()`, `url .toLowerCase()`, `url .toLowerCase() .indexOf()`, `url.indexOf()`, `url.substr()`, `url.substring()`
- 条件付き依存: `if ( queryType != QUERYTYPE.AUTOFILL_ORIGIN && queryContext.searchString.length == autofilledValue.length )` → `autofilledValue.substring()`
- 条件付き依存: `if ( queryType != QUERYTYPE.AUTOFILL_ORIGIN && queryContext.searchString.length == autofilledValue.length )` → `finalCompleteValue.substring()`
- 条件付き依存: `if (!(title))` → `lazy.UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (!(title))` → `lazy.UrlbarShared.prepareUrlForDisplay()`
- 条件付き依存: `if (!(title))` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if (!(title))` → `this._searchString.includes()`
- 参照: `QUERYTYPE.AUTOFILL_ADAPTIVE`, `QUERYTYPE.AUTOFILL_ORIGIN`, `QUERYTYPE.AUTOFILL_URL`, `autofilledValue.length`, `finalCompleteValue.length`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `new URL(finalCompleteValue).href`, `payload.title`, `queryContext.searchString`, `queryContext.searchString.length`, `searchString.length`, `strippedAutofilledValue.length`, `strippedURL.length`, `this._strippedPrefix.length`

## UrlbarProviderAutofill._getAutofillResult()
- 位置: async L1134-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._matchAboutPageForAutofill()`, `this._matchKnownUrl()`

## UrlbarProviderAutofill._matchAboutPageForAutofill()
- 位置: L1145-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aboutUrl.startsWith()`, `this._searchString.toLowerCase()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `this._searchString.includes()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `aboutUrl.substring()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `lazy.UrlbarShared.getIconForUrl()`
- 参照: `autofilledValue.length`, `lazy.AboutPagesUtils.visibleAboutUrls`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.searchString`, `queryContext.searchString.length`, `this._searchString`, `this._strippedPrefix`

## UrlbarProviderAutofill._matchKnownUrl()
- 位置: async L1187-1250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.UrlUtils.looksLikeOrigin()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("autoFill.adaptiveHistory.enabled") && lazy.UrlbarPrefs.get("autoFill.adaptiveHistory.minCharsThreshold") <= queryContext.searchString....)` → `this._getAdaptiveHistoryQuery()`
- 条件付き依存: `if (query)` → `conn.executeCached()`
- 条件付き依存: `if (resultSet.length)` → `this._processRow()`
- 条件付き依存: `if (result)` → `this._getFallbackOriginResult()`
- 条件付き依存: `if ( lazy.UrlUtils.looksLikeOrigin(this._searchString, { ignoreKnownDomains: true, allowPartialNumericalTLDs: true, }) )` → `this._getOriginQuery()`
- 条件付き依存: `if (!( lazy.UrlUtils.looksLikeOrigin(this._searchString, { ignoreKnownDomains: true, allowPartialNumericalTLDs: true, }) ))` → `this._getUrlQuery()`
- 条件付き依存: `if (rows.length)` → `this._processRow()`
- 参照: `queryContext.searchString.length`, `result.payload.url`, `resultSet.length`, `rows.length`, `this._searchString`, `this._searchString.length`

## UrlbarProviderAutofill._getFallbackOriginResult()
- 位置: async L1270-1311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.urlFormatter.formatURLPref()`, `URL.parse()`, `conn.executeCached()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.isOriginUrl()`, `rows[0].getResultByName()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `parsedUrl.origin`, `rows.length`
- XPCOM: `Services.urlFormatter`
