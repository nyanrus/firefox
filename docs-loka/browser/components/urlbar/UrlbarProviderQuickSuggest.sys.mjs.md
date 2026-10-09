# browser/components/urlbar/UrlbarProviderQuickSuggest.sys.mjs

source: browser/components/urlbar/UrlbarProviderQuickSuggest.sys.mjs
source-hash: 410ed98058deb64ac1f2006fbf9f5be8bb542b52
lines: 641

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderQuickSuggest.type()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.NETWORK`

## UrlbarProviderQuickSuggest.DEFAULT_SUGGESTION_SCORE()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderQuickSuggest.isActive()
- 位置: async L56-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`, `queryContext.searchString.trimStart()`, `queryContext.sources.includes()`, `trimmedSearchString.trimEnd()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.isPrivate`, `queryContext.restrictSource`, `this._trimmedSearchString`, `trimmedSearchString.trimEnd().length`

## UrlbarProviderQuickSuggest.startQuery()
- 位置: async L97-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `backend.query()`, `lazy.QuickSuggest.enabledBackends.map()`, `this.#filterAndSortSuggestions()`, `this.#makeResult()`, `values.flat()`
- 条件付き依存: `if (result)` → `this.#canAddResult()`
- 条件付き依存: `if (canAdd)` → `addCallback()`
- 参照: `queryContext.maxResults`, `result.isHiddenExposure`, `this._trimmedSearchString`, `this.queryInstance`

## UrlbarProviderQuickSuggest.#filterAndSortSuggestions()
- 位置: async L143-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.resolve()`, `[...suggestionsByFeature].map()`, `feature.filterSuggestions()`, `featureSuggestions.push()`, `filteredSuggestions.sort()`, `indexesBySuggestion.get()`, `indexesBySuggestion.set()`, `isNaN()`, `lazy.QuickSuggest.getFeatureBySource()`, `lazy.UrlbarPrefs.get()`, `requiredKeys.every()`, `suggestionsByFeature.get()`, `this.#applyRanking()`
- 条件付き依存: `if (!requiredKeys.every(key => suggestion[key]))` → `this.logger.error()`
- 条件付き依存: `if (scoreMap)` → `this.#getSuggestionTelemetryType()`
- 条件付き依存: `if (scoreMap)` → `scoreMap.hasOwnProperty()`
- 条件付き依存: `if (scoreMap.hasOwnProperty(telemetryType))` → `parseFloat()`
- 条件付き依存: `if (scoreMap.hasOwnProperty(telemetryType))` → `isNaN()`
- 条件付き依存: `if (!featureSuggestions)` → `suggestionsByFeature.set()`
- 参照: `a.score`, `b.score`, `suggestion.score`, `suggestions.length`

## UrlbarProviderQuickSuggest.onImpression()
- 位置: L227-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feature.onImpression()`, `lazy.QuickSuggest.getFeatureByResult()`, `resultsAndIndexes.reduce()`
- 条件付き依存: `if (feature)` → `memo.get()`
- 条件付き依存: `if (!featureResults)` → `memo.set()`
- 条件付き依存: `if (feature)` → `featureResults.push()`

## UrlbarProviderQuickSuggest.onEngagement()
- 位置: L259-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`
- 条件付き依存: `if (feature)` → `feature.onEngagement()`
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `lazy.QuickSuggest.dismissResult()`
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `controller.removeResult()`
- 参照: `details.selType`, `result.payload.isBlockable`, `this._trimmedSearchString`

## UrlbarProviderQuickSuggest.onSearchSessionEnd()
- 位置: L289-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `backend.onSearchSessionEnd()`
- 参照: `lazy.QuickSuggest.enabledBackends`

## UrlbarProviderQuickSuggest.getViewTemplate()
- 位置: L301-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.getFeatureByResult(result)?.getViewTemplate()`

## UrlbarProviderQuickSuggest.getViewUpdate()
- 位置: L314-319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.getFeatureByResult(result)?.getViewUpdate()`

## UrlbarProviderQuickSuggest.getResultCommands()
- 位置: L330-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.getFeatureByResult(result)?.getResultCommands()`

## UrlbarProviderQuickSuggest.#getSuggestionTelemetryType()
- 位置: L349-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureBySource()`
- 条件付き依存: `if (feature)` → `feature.getSuggestionTelemetryType()`
- 参照: `suggestion.provider`

## UrlbarProviderQuickSuggest.#makeResult()
- 位置: async L357-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureBySource()`, `result.payload.hasOwnProperty()`, `this.#getSuggestionTelemetryType()`
- 条件付き依存: `if (!feature)` → `this.#makeUnmanagedResult()`
- 条件付き依存: `if (feature.isEnabled)` → `feature.makeResult()`
- 条件付き依存: `if (!result.payload.hasOwnProperty("isSponsored"))` → `feature?.isSuggestionSponsored()`
- 条件付き依存: `if (result.payload.icon)` → `UrlbarUtils.getRemoteImageUrl()`
- 条件付き依存: `if (!result.payload.isSponsored)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `this.queryInstance .getProvider("UrlbarProviderSearchSuggestions") ?.isActive()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `this.queryInstance .getProvider()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `lazy.UrlbarSearchUtils.getDefaultEngine( queryContext.isPrivate ).supportsResponseType()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("showSearchSuggestionsFirst") && (await this.queryInstance .getProvider("UrlbarProviderSearchSuggestions") ?.isActive(queryContext, thi...)` → `lazy.UrlbarPrefs.get()`
- 参照: `feature.isEnabled`, `lazy.SearchUtils.URL_TYPE.SUGGEST_JSON`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`, `queryContext.isPrivate`, `result.hasSuggestedIndex`, `result.isBestMatch`, `result.isRichSuggestion`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.dismissalKey`, `result.payload.icon`, `result.payload.iconBlob`, `result.payload.isSponsored`, `result.payload.provider`, `result.payload.source`, `result.payload.suggestionObject`, `result.payload.suggestionType`, `result.payload.telemetryType`, `result.richSuggestionIconSize`, `result.suggestedIndex`, `suggestion.dismissal_key`, `suggestion.icon`, `suggestion.icon_blob`, `suggestion.provider`, `suggestion.source`, `suggestion.suggestionType`, `this._trimmedSearchString`, `this.queryInstance.controller`

## UrlbarProviderQuickSuggest.#makeUnmanagedResult()
- 位置: L484-524
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (suggestion.full_keyword)` → `lazy.QuickSuggest.getFullKeywordTitleAndHighlights()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `payload.shouldShowUrl`, `payload.title`, `queryContext.tokens`, `suggestion.full_keyword`, `suggestion.is_sponsored`, `suggestion.is_top_pick`, `suggestion.original_url`, `suggestion.provider`, `suggestion.source`, `suggestion.title`, `suggestion.url`

## UrlbarProviderQuickSuggest.cancelQuery()
- 位置: L529-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `backend.cancelQuery()`
- 参照: `lazy.QuickSuggest.enabledBackends`

## UrlbarProviderQuickSuggest.#applyRanking()
- 位置: async L541-563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`, `lazy.UrlbarPrefs.get()`, `suggestion.score.toFixed()`, `this.#updateScoreByRelevance()`, `this.logger.debug()`
- 参照: `suggestion.score`

## UrlbarProviderQuickSuggest.#updateScoreByRelevance()
- 位置: async L574-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.suggestRelevance.outcome[ suggestion.score >= oldScore ? "boosted" : "decreased" ].add()`, `Glean.suggestRelevance.status.failure.add()`, `Glean.suggestRelevance.status.success.add()`, `lazy.ContentRelevancyManager.score()`, `this.logger.error()`
- 参照: `Glean.suggestRelevance.outcome`, `suggestion.categories`, `suggestion.categories?.length`, `suggestion.score`

## UrlbarProviderQuickSuggest.#canAddResult()
- 位置: async L605-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.isResultDismissed()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (await lazy.QuickSuggest.isResultDismissed(result))` → `this.logger.debug()`
- 参照: `result.payload.isSponsored`

## UrlbarProviderQuickSuggest._test_applyRanking()
- 位置: async L637-639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#applyRanking()`
