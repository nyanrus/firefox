# browser/components/urlbar/UrlbarProviderSearchSuggestions.sys.mjs

source: browser/components/urlbar/UrlbarProviderSearchSuggestions.sys.mjs
source-hash: c8e07ac2164de89420b3a00e2d6c92e55e1ddf7e
lines: 719

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Services.urlFormatter.formatURLPref()`

## looksLikeUrl()
- 位置: L59-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^([\[\]A-Z0-9-]+\.){3,}[^.]+$/i.test()`, `["/", "@", ":", "["].some()`, `lazy.UrlUtils.REGEXP_SPACES.test()`, `str.includes()`

## UrlbarProviderSearchSuggestions.constructor()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderSearchSuggestions.type()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.NETWORK`

## UrlbarProviderSearchSuggestions.isActive()
- 位置: async L95-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.sources.includes()`, `this.#shouldFetchTrending()`, `this._allowRemoteSuggestions()`, `this._allowSuggestions()`, `this._isTokenOrRestrictionPresent()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.restrictSource`, `queryContext.trimmedSearchString`

## UrlbarProviderSearchSuggestions._isTokenOrRestrictionPresent()
- 位置: L138-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.searchString.startsWith()`, `queryContext.sources.includes()`, `queryContext.tokens.some()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `queryContext.restrictSource`, `queryContext.searchMode`, `t.type`

## UrlbarProviderSearchSuggestions._allowSuggestions()
- 位置: L161-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._isTokenOrRestrictionPresent()`
- 参照: `queryContext.isPrivate`, `queryContext.isSearchbarSAP`, `queryContext.sapName`

## UrlbarProviderSearchSuggestions._allowRemoteSuggestions()
- 位置: L189-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.allowRemoteResults()`, `searchString.startsWith()`, `searchString.trim()`, `this.#shouldFetchTrending()`, `this._isTokenOrRestrictionPresent()`
- 参照: `queryContext.prohibitRemoteResults`, `queryContext.searchString`, `searchString.length`, `this._lastLowResultsSearchSuggestion`, `this._lastLowResultsSearchSuggestion.length`

## UrlbarProviderSearchSuggestions.startQuery()
- 位置: async L241-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.substringAt()`, `UrlbarUtils.substringAt( queryContext.searchString, queryContext.tokens[0]?.value || "" ).trim()`, `addCallback()`, `lazy.UrlbarTokenizer.isRestrictionToken()`, `this.#fetchSearchSuggestions()`, `this._maybeGetAlias()`
- 条件付き依存: `if (!aliasEngine)` → `queryContext.searchString.startsWith()`
- 条件付き依存: `if (leadingRestrictionToken === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH)` → `UrlbarUtils.substringAfter(query, leadingRestrictionToken).trim()`
- 条件付き依存: `if (leadingRestrictionToken === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH)` → `UrlbarUtils.substringAfter()`
- 条件付き依存: `if (queryContext.searchMode?.engineName)` → `lazy.UrlbarSearchUtils.getEngineByName()`
- 条件付き依存: `if (!(queryContext.searchMode?.engineName))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 参照: `aliasEngine.alias`, `aliasEngine.engine`, `aliasEngine.query`, `lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `queryContext.isPrivate`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens.length`, `queryContext.tokens[0].type`, `queryContext.tokens[0].value`, `queryContext.tokens[0]?.value`, `this.queryInstance`

## UrlbarProviderSearchSuggestions.getPriority()
- 位置: L322-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#shouldFetchTrending()`
- 参照: `lazy.UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderSearchSuggestions.cancelQuery()
- 位置: L332-336
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#suggestionsController)` → `this.#suggestionsController.stop()`
- 参照: `this.#suggestionsController`

## UrlbarProviderSearchSuggestions.getResultCommands()
- 位置: L344-361
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `RESULT_MENU_COMMANDS.TRENDING_BLOCK`, `RESULT_MENU_COMMANDS.TRENDING_HELP`, `result.payload.trending`

## UrlbarProviderSearchSuggestions.onEngagement()
- 位置: L368-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.set()`, `this.#recordTrendingBlockedTelemetry()`, `this.#replaceTrendingResultWithAcknowledgement()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.FormHistory.update()`
- 条件付き依存: `if (details.selType == "dismiss")` → `console.error()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `RESULT_MENU_COMMANDS.TRENDING_BLOCK`, `RESULT_MENU_COMMANDS.TRENDING_HELP`, `details.selType`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `result.payload.suggestion`

## UrlbarProviderSearchSuggestions.#fetchSearchSuggestions()
- 位置: async L403-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `UrlbarUtils.getRemoteImageUrl()`, `entry.value.toLocaleLowerCase()`, `lazy.UrlbarPrefs.get()`, `looksLikeUrl()`, `results.push()`, `searchString.trim()`, `this.#shouldFetchTrending()`, `this.#suggestionsController.fetch()`, `this._allowRemoteSuggestions()`, `this._isTokenOrRestrictionPresent()`, `this.logger.error()`
- 条件付き依存: `if (allowRemote && this.#shouldFetchTrending(queryContext))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( queryContext.searchMode && lazy.UrlbarPrefs.get("trending.maxResultsSearchMode") != -1 )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!( queryContext.searchMode && lazy.UrlbarPrefs.get("trending.maxResultsSearchMode") != -1 ))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( !queryContext.searchMode && lazy.UrlbarPrefs.get("trending.maxResultsNoSearchMode") != -1 )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("maxHistoricalSearchSuggestions"))` → `results.push()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("maxHistoricalSearchSuggestions"))` → `makeFormHistoryResult()`
- 条件付き依存: `if (!tail)` → `tailTimer.fire().catch()`
- 条件付き依存: `if (!tail)` → `tailTimer.fire()`
- 条件付き依存: `if (!tail)` → `this.logger.error()`
- 参照: `UrlbarProviderSearchSuggestions.RICH_ICON_SIZE`, `engine.name`, `entry.description`, `entry.icon`, `entry.matchPrefix`, `entry.tail`, `entry.tailOffsetIndex`, `entry.trending`, `entry.value`, `fetchData.local`, `fetchData.remote`, `fetchData.remote.length`, `lazy.SearchSuggestionController`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.isPrivate`, `queryContext.maxResults`, `queryContext.sapName`, `queryContext.searchMode`, `queryContext.userContextId`, `searchString.length`, `tailTimer.promise`, `this.#suggestionsController`, `this._lastLowResultsSearchSuggestion`, `this.logger`

## UrlbarProviderSearchSuggestions._maybeGetAlias()
- 位置: async L603-639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.substringAfter()`, `lazy.UrlUtils.REGEXP_SPACES_START.test()`, `lazy.UrlbarSearchUtils.engineForAlias()`
- 条件付き依存: `if (engineMatch)` → `query.trim()`
- 参照: `queryContext.searchMode`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0]?.value`

## UrlbarProviderSearchSuggestions.#shouldFetchTrending()
- 位置: L652-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `queryContext.searchMode`, `queryContext.searchString`

## UrlbarProviderSearchSuggestions.#recordTrendingBlockedTelemetry()
- 位置: L665-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarTrending.block.add()`

## UrlbarProviderSearchSuggestions.#replaceTrendingResultWithAcknowledgement()
- 位置: L676-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `queryContext.results.filter()`, `resultsToRemove.forEach()`, `resultsToRemove.reverse()`
- 参照: `result.payload.trending`

## makeFormHistoryResult()
- 位置: L699-718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `entry.value.toLocaleLowerCase()`
- 参照: `engine.name`, `entry.value`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`
- XPCOM: `Services.urlFormatter`
