# browser/components/urlbar/UrlbarMuxerStandard.sys.mjs

source: browser/components/urlbar/UrlbarMuxerStandard.sys.mjs
source-hash: d5fa820ef45e21cf3a2b8d3c8e430f63ebe55e63
lines: 1619

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## makeMapKeyForTabResult()
- 位置: L39-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.tupleString()`, `lazy.UrlbarShared.isNonPrivateUserContextId()`
- 参照: `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.payload.url`, `result.payload.userContext?.id`, `result.type`

## stripUrlForDedupe()
- 位置: L59-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`

## MuxerUnifiedComplete.constructor()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## MuxerUnifiedComplete.name()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)

## MuxerUnifiedComplete.sort()
- 位置: L89-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `indicesToSort.values()`, `lazy.UrlbarPrefs.getResultGroups()`, `lazy.UrlbarShared.getResultGroup()`, `lazy.logger.debug()`, `results.push()`, `resultsByGroup.get()`, `state.resultsByGroup.get()`, `this.#getGroupAsObject()`, `this._fillGroup()`, `this._updateStatePreAdd()`, `toSort.sort()`, `unsortedResults.slice()`, `unsortedResults.splice()`
- 条件付き依存: `if (sortingField)` → `indicesToSort.get()`
- 条件付き依存: `if (!indices)` → `indicesToSort.set()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.URL)` → `state.nonSemanticDupeKeys.add()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.URL)` → `stripUrlForDedupe()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH)` → `state.nonSemanticDupeKeys.add()`
- 条件付き依存: `if (!results)` → `resultsByGroup.set()`
- 条件付き依存: `if (state.maxHeuristicResultSpan)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (context.maxResults > 0)` → `Math.max()`
- 条件付き依存: `if (globalSuggestedIndexResults)` → `this._addSuggestedIndexResults()`
- 参照: `a.payload`, `b.payload`, `context.maxResults`, `context.results`, `groupObj?.orderBy`, `indices.length`, `lazy.UrlbarShared.RESULT_GROUP.SUGGESTED_INDEX`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `result.hasSuggestedIndex`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.url`, `result.providerName`, `result.type`, `state.availableResultSpan`, `state.globalSuggestedIndexResultSpan`, `state.maxHeuristicResultSpan`, `state.maxTabToSearchResultSpan`, `state.resultsByGroup`, `state.suggestedIndexResultsByGroup`, `unsortedResults.length`

## MuxerUnifiedComplete.#getGroupAsObject()
- 位置: L273-287
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("children" in child)` → `this.#getGroupAsObject()`
- 参照: `child.group`, `rootGroup.children`

## MuxerUnifiedComplete._copyState()
- 位置: L300-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `copy[key].set()`
- 参照: `state.addedRemoteTabUrls`, `state.addedResultUrls`, `state.addedSwitchTabUrls`, `state.baseAndTitleToTopRef`, `state.nonSemanticDupeKeys`, `state.strippedUrlToTopPrefixAndTitle`, `state.suggestions`, `state.urlToTabResultType`

## MuxerUnifiedComplete._fillGroup()
- 位置: L362-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addResults()`, `this._fillGroupChildren()`
- 条件付き依存: `if ("group" in group)` → `state.suggestedIndexResultsByGroup.get()`
- 条件付き依存: `if (results)` → `this._canAddResult()`
- 条件付き依存: `if (this._canAddResult(result, state))` → `suggestedIndexResults.push()`
- 条件付き依存: `if (this._canAddResult(result, state))` → `lazy.UrlbarShared.getSpanForResult()`
- 条件付き依存: `if (results)` → `Math.min()`
- 条件付き依存: `if (suggestedIndexResults)` → `this._addSuggestedIndexResults()`
- 条件付き依存: `if (suggestedIndexResults)` → `Object.entries()`
- 参照: `group.children`, `group.group`, `limits.availableSpan`, `limits.maxResultCount`

## MuxerUnifiedComplete._fillGroupChildren()
- 位置: L440-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `Object.keys()`, `results.concat()`, `this._fillGroup()`
- 条件付き依存: `if (group.flexChildren)` → `this._copyState()`
- 条件付き依存: `if (group.flexChildren)` → `this._updateFlexData()`
- 条件付き依存: `if (flexData?.hasMoreResults)` → `[...Object.entries(childLimits)].every()`
- 条件付き依存: `if (flexData?.hasMoreResults)` → `Object.entries()`
- 条件付き依存: `if (anyChildUnderfilled && anyChildHasMoreResults)` → `this._fillGroupChildren()`
- 条件付き依存: `if (anyChildUnderfilled && anyChildHasMoreResults)` → `Object.entries()`
- 参照: `flexData.hasMoreResults`, `flexData.limits`, `flexData.usedLimits`, `flexData?.hasMoreResults`, `group.children`, `group.children.length`, `group.flexChildren`

## MuxerUnifiedComplete._updateFlexData()
- 位置: L551-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.round()`, `Object.entries()`, `Object.keys()`, `group.children.map()`
- 条件付き依存: `if (data.hasMoreResults)` → `fillableDataArray.push()`
- 条件付き依存: `if (summedFillableLimit != fillableLimit)` → `fillableDataArray.filter()`
- 条件付き依存: `if (summedFillableLimit < fillableLimit)` → `fractionalDataArray.sort()`
- 条件付き依存: `if (fillableLimit < summedFillableLimit)` → `fractionalDataArray.sort()`
- 条件付き依存: `if (!fractionalDataArray.length)` → `lazy.logger.error()`
- 条件付き依存: `if (summedFillableLimit != fillableLimit)` → `fractionalDataArray.shift()`
- 参照: `a.index`, `a.limitFractions`, `b.index`, `b.limitFractions`, `child.flex`, `data.flex`, `data.hasMoreResults`, `data.limitFractions`, `data.limits`, `data.usedLimits`, `fractionalDataArray.length`, `fractionalDataArray.shift().index`

## MuxerUnifiedComplete._addResults()
- 位置: L711-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.keys()`, `[...Object.entries(limits)].every()`, `groupResults.shift()`, `lazy.UrlbarPrefs.get()`, `state.resultsByGroup.get()`, `this._canAddResult()`
- 条件付き依存: `if (this._canAddResult(result, state))` → `this.#updateUsedLimits()`
- 条件付き依存: `if (this._canAddResult(result, state))` → `addedResults.push()`
- 参照: `groupResults?.length`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `limits.maxResultCount`, `state.availableResultSpan`, `state.usedResultSpan`

## MuxerUnifiedComplete.#isSuppressedSemanticDupe()
- 位置: L772-788
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.URL)` → `state.nonSemanticDupeKeys.has()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.URL)` → `stripUrlForDedupe()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH)` → `state.nonSemanticDupeKeys.has()`
- 参照: `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `result.payload.url`, `result.providerName`, `result.type`

## MuxerUnifiedComplete._canAddResult()
- 位置: L804-1192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.isUrlEquivalentToResultUrl()`, `lazy.UrlbarPrefs.get()`, `makeMapKeyForTabResult()`, `result.payload.suggestion?.startsWith()`, `state.addedSwitchTabUrls.has()`, `state.context.restrictInSearchMode()`, `state.urlToTabResultType.has()`, `this.#isSuppressedSemanticDupe()`
- 条件付き依存: `if (result.providerName == lazy.UrlbarProviderQuickSuggest.name)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( heuristicUrl && result.payload.telemetryType == "top_picks" && !lazy.UrlbarPrefs.get("experimental.hideHeuristic") )` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if ( !result.heuristic && result.type == lazy.UrlbarShared.RESULT_TYPE.URL && result.payload.url )` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if ( !result.heuristic && result.type == lazy.UrlbarShared.RESULT_TYPE.URL && result.payload.url )` → `state.strippedUrlToTopPrefixAndTitle.get()`
- 条件付き依存: `if ( topPrefixData && (prefix != topPrefixData.prefix || result.providerName != topPrefixData.providerName) )` → `UrlbarUtils.getPrefixRank()`
- 条件付き依存: `if ( topPrefixData && (prefix != topPrefixData.prefix || result.providerName != topPrefixData.providerName) )` → `prefix.endsWith()`
- 条件付き依存: `if ( topPrefixData && (prefix != topPrefixData.prefix || result.providerName != topPrefixData.providerName) )` → `topPrefixData.prefix.endsWith()`
- 条件付き依存: `if ( state.context.heuristicResult?.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if ( state.context.heuristicResult?.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `UrlbarUtils.stripPublicSuffixFromHost()`
- 条件付き依存: `if ( state.context.heuristicResult?.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `engineDomain.endsWith()`
- 条件付き依存: `if ( result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH && result.payload.lowerCaseSuggestion && !result.isRichSuggestion )` → `result.payload.lowerCaseSuggestion.trim()`
- 条件付き依存: `if ( result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH && result.payload.lowerCaseSuggestion && !result.isRichSuggestion )` → `state.suggestions.has()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB)` → `state.addedRemoteTabUrls.has()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB)` → `state.urlToTabResultType.get()`
- 条件付き依存: `if ( result.source == lazy.UrlbarShared.RESULT_SOURCE.HISTORY && result.type == lazy.UrlbarShared.RESULT_TYPE.URL && // If there's no suggestions, we're not goin...)` → `lazy.SearchService.parseSubmissionURL()`
- 条件付き依存: `if (submission)` → `submission.terms.trim().toLocaleLowerCase()`
- 条件付き依存: `if (submission)` → `submission.terms.trim()`
- 条件付き依存: `if (submission)` → `state.suggestions.has()`
- 条件付き依存: `if (state.suggestions.has(resultQuery))` → `UrlbarUtils.getSearchQueryUrl()`
- 条件付き依存: `if (state.suggestions.has(resultQuery))` → `lazy.UrlbarSearchUtils.serpsAreEquivalent()`
- 条件付き依存: `if ( state.context.searchMode?.engineName && result.payload.url && state.context.restrictInSearchMode() && !(result.heuristic && state.context.navigationInSearch...)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (engine)` → `lazy.UrlbarSearchUtils.getRootDomainFromEngine()`
- 条件付き依存: `if (engine)` → `resultUrl.hostname.includes()`
- 条件付き依存: `if ( result.source == lazy.UrlbarShared.RESULT_SOURCE.HISTORY && result.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (param)` → `param.split()`
- 条件付き依存: `if (param)` → `URL.parse()`
- 条件付き依存: `if (param)` → `searchParams?.has()`
- 条件付き依存: `if (param)` → `searchParams?.getAll(key).includes()`
- 条件付き依存: `if (param)` → `searchParams?.getAll()`
- 条件付き依存: `if (result.payload.url)` → `result.payload.url.split("?").pop()`
- 条件付き依存: `if (result.payload.url)` → `result.payload.url.split()`
- 条件付き依存: `if (result.payload.url)` → `new URLSearchParams(urlParams).get()`
- 条件付き依存: `if (result.payload.url)` → `state.addedResultUrls.has()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("deduplication.enabled") && result.source == lazy.UrlbarShared.RESULT_SOURCE.HISTORY && result.type == lazy.UrlbarShared.RESULT_TYPE.UR...)` → `UrlbarUtils.extractRefFromUrl()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("deduplication.enabled") && result.source == lazy.UrlbarShared.RESULT_SOURCE.HISTORY && result.type == lazy.UrlbarShared.RESULT_TYPE.UR...)` → `state.baseAndTitleToTopRef.get()`
- 参照: `URL.parse(result.payload.url)?.searchParams`, `lazy.UrlbarProviderQuickSuggest.name`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `new URL( state.context.heuristicResult.payload.url ).hostname`, `result.autofill`, `result.heuristic`, `result.isHiddenExposure`, `result.isRichSuggestion`, `result.payload.dupedHeuristic`, `result.payload.engine`, `result.payload.inPrivateWindow`, `result.payload.isSponsored`, `result.payload.lowerCaseSuggestion`, `result.payload.satisfiesAutofillThreshold`, `result.payload.searchUrlDomainWithoutSuffix`, `result.payload.suggestionObject?.suggestionType`, `result.payload.tail`, `result.payload.telemetryType`, `result.payload.title`, `result.payload.url`, `result.payload?.title`, `result.providerName`, `result.source`, `result.type`, `state.canAddTabToSearch`, `state.canShowPrivateSearch`, `state.canShowTailSuggestions`, `state.context.excludeSponsoredResults`, `state.context.heuristicResult`, `state.context.heuristicResult.autofill`, `state.context.heuristicResult.payload.url`, `state.context.heuristicResult.payload?.url`, `state.context.heuristicResult.type`, `state.context.heuristicResult?.payload.url`, `state.context.heuristicResult?.providerName`, `state.context.heuristicResult?.type`, `state.context.navigationInSearchModeEnabled`, `state.context.searchMode.engineName`, `state.context.searchMode?.engineName`, `state.hasUnitConversionResult`, `state.quickSuggestResult`, `state.suggestions.size`, `state.usedResultSpan`, `submission.engine`, `submission.terms`, `topPrefixData.prefix`, `topPrefixData.providerName`, `topPrefixData.rank`, `topPrefixData.title`
- XPCOM: `Services.prefs`

## MuxerUnifiedComplete._updateStatePreAdd()
- 位置: L1204-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `makeMapKeyForTabResult()`, `state.urlToTabResultType.has()`, `this.#isSuppressedSemanticDupe()`, `this.#setExposureTelemetryProperty()`, `this._canAddResult()`
- 条件付き依存: `if (result.heuristic && this._canAddResult(result, state))` → `Math.max()`
- 条件付き依存: `if (result.heuristic && this._canAddResult(result, state))` → `lazy.UrlbarShared.getSpanForResult()`
- 条件付き依存: `if ( result.hasSuggestedIndex && !result.isSuggestedIndexRelativeToGroup && this._canAddResult(result, state) )` → `lazy.UrlbarShared.getSpanForResult()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderTabToSearch")` → `Math.max()`
- 条件付き依存: `if ( !isSemanticDupe && (result.type == lazy.UrlbarShared.RESULT_TYPE.URL || result.type == lazy.UrlbarShared.RESULT_TYPE.KEYWORD) && result.payload.url && (!res...)` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if ( !isSemanticDupe && (result.type == lazy.UrlbarShared.RESULT_TYPE.URL || result.type == lazy.UrlbarShared.RESULT_TYPE.KEYWORD) && result.payload.url && (!res...)` → `UrlbarUtils.getPrefixRank()`
- 条件付き依存: `if ( !isSemanticDupe && (result.type == lazy.UrlbarShared.RESULT_TYPE.URL || result.type == lazy.UrlbarShared.RESULT_TYPE.KEYWORD) && result.payload.url && (!res...)` → `state.strippedUrlToTopPrefixAndTitle.get()`
- 条件付き依存: `if ( topPrefixRank < prefixRank || // If a quick suggest result has the same stripped URL and prefix rank // as another result, store the quick suggest as the to...)` → `state.strippedUrlToTopPrefixAndTitle.set()`
- 条件付き依存: `if ( !isSemanticDupe && (result.type == lazy.UrlbarShared.RESULT_TYPE.URL || result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH) )` → `UrlbarUtils.extractRefFromUrl()`
- 条件付き依存: `if ( !isSemanticDupe && (result.type == lazy.UrlbarShared.RESULT_TYPE.URL || result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH) )` → `state.baseAndTitleToTopRef.has()`
- 条件付き依存: `if (!state.baseAndTitleToTopRef.has(baseAndTitle) || result.heuristic)` → `state.baseAndTitleToTopRef.set()`
- 条件付き依存: `if ( result.payload.url && (result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH || (result.type == lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB && !state.urlToTa...)` → `state.urlToTabResultType.set()`
- 条件付き依存: `if ( result.payload.url && (result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH || (result.type == lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB && !state.urlToTa...)` → `makeMapKeyForTabResult()`
- 条件付き依存: `if (result.payload.url)` → `state.addedResultUrls.add()`
- 参照: `lazy.UrlbarProviderQuickSuggest.name`, `lazy.UrlbarShared.RESULT_TYPE.AI_CHAT`, `lazy.UrlbarShared.RESULT_TYPE.KEYWORD`, `lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `result.hasSuggestedIndex`, `result.heuristic`, `result.isHiddenExposure`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.inPrivateWindow`, `result.payload.suggestionObject?.suggestionType`, `result.payload.tail`, `result.payload.title`, `result.payload.url`, `result.providerName`, `result.type`, `state.canShowTailSuggestions`, `state.globalSuggestedIndexResultSpan`, `state.hasUnitConversionResult`, `state.maxHeuristicResultSpan`, `state.maxTabToSearchResultSpan`, `state.quickSuggestResult`, `topPrefixData.rank`

## MuxerUnifiedComplete._updateStatePostAdd()
- 位置: L1361-1423
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.heuristic)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH && result.payload.query && !lazy.UrlbarPrefs.get("experimental.hideHeuristic") )` → `result.payload.query.trim().toLocaleLowerCase()`
- 条件付き依存: `if ( result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH && result.payload.query && !lazy.UrlbarPrefs.get("experimental.hideHeuristic") )` → `result.payload.query.trim()`
- 条件付き依存: `if (query)` → `state.suggestions.add()`
- 条件付き依存: `if ( result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH && result.payload.lowerCaseSuggestion )` → `result.payload.lowerCaseSuggestion.trim()`
- 条件付き依存: `if (suggestion)` → `state.suggestions.add()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB)` → `state.addedRemoteTabUrls.add()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH)` → `state.addedSwitchTabUrls.add()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH)` → `makeMapKeyForTabResult()`
- 参照: `lazy.SearchService.separatePrivateDefaultUrlbarResultEnabled`, `lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.heuristic`, `result.isHiddenExposure`, `result.payload.keyword`, `result.payload.lowerCaseSuggestion`, `result.payload.providesSearchMode`, `result.payload.query`, `result.payload.url`, `result.providerName`, `result.type`, `state.canAddTabToSearch`, `state.canShowPrivateSearch`, `state.context.heuristicResult`

## MuxerUnifiedComplete._addSuggestedIndexResults()
- 位置: L1446-1555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `negative.sort()`, `positive.sort()`, `results.push()`, `this._canAddResult()`
- 条件付き依存: `if (a.providerName === lazy.UrlbarProviderQuickSuggest.name)` → `Number()`
- 条件付き依存: `if (this._canAddResult(result, state))` → `this.#updateUsedLimits()`
- 条件付き依存: `if (!( prevResult && prevResult.suggestedIndex == result.suggestedIndex ))` → `Math.min()`
- 条件付き依存: `if (!( prevResult && prevResult.suggestedIndex == result.suggestedIndex ))` → `Math.max()`
- 条件付き依存: `if (this._canAddResult(result, state))` → `sortedResults.splice()`
- 参照: `a.payload.suggestionObject?.suggestionType`, `a.providerName`, `a.suggestedIndex`, `b.payload.suggestionObject?.suggestionType`, `b.providerName`, `b.suggestedIndex`, `lazy.UrlbarProviderQuickSuggest.name`, `prevResult.suggestedIndex`, `result.suggestedIndex`, `sortedResults.length`, `suggestedIndexResults?.length`

## MuxerUnifiedComplete.#updateUsedLimits()
- 位置: L1577-1594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.getSpanForResult()`, `this._updateStatePostAdd()`
- 参照: `limits.availableSpan`, `state.usedResultSpan`, `usedLimits.availableSpan`, `usedLimits.maxResultCount`

## MuxerUnifiedComplete.#setExposureTelemetryProperty()
- 位置: L1604-1615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (exposureResults.size)` → `lazy.UrlbarShared.searchEngagementTelemetryType()`
- 条件付き依存: `if (exposureResults.size)` → `exposureResults.has()`
- 条件付き依存: `if (exposureResults.has(telemetryType))` → `lazy.UrlbarPrefs.get()`
- 参照: `exposureResults.size`, `lazy.UrlbarShared.EXPOSURE_TELEMETRY.HIDDEN`, `lazy.UrlbarShared.EXPOSURE_TELEMETRY.SHOWN`, `result.exposureTelemetry`
