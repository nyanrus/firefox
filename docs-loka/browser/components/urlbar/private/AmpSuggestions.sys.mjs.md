# browser/components/urlbar/private/AmpSuggestions.sys.mjs

source: browser/components/urlbar/private/AmpSuggestions.sys.mjs
source-hash: 3f7ed5fa6dc7e86a297fb49bc25314e591eacf64
lines: 517

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Promise.resolve()`

## AmpSuggestions.enablingPreferences()
- 位置: L45-52
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.primaryUserControlledPreferences()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.merinoProvider()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.rustSuggestionType()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.rustProviderConstraints()
- 位置: L66-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(lazy.AmpMatchingStrategy).includes()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!Object.values(lazy.AmpMatchingStrategy).includes(intValue))` → `this.logger.error()`
- 参照: `lazy.AmpMatchingStrategy`

## AmpSuggestions.isSuggestionSponsored()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.getSuggestionTelemetryType()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.enable()
- 位置: L93-111
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (enabled)` → `GleanPings.quickSuggest.setEnabled()`

## AmpSuggestions.makeResult()
- 位置: L113-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 条件付き依存: `if (suggestion.source == "merino")` → `this.#replaceSuggestionTemplates()`
- 条件付き依存: `if (!( suggestion.source == "merino" && typeof suggestion.is_top_pick == "boolean" ))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!isTopPick))` → `lazy.UrlbarPrefs.get()`
- 参照: `amp.header_text`, `amp.suggestion_id`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `normalized.advertiser`, `normalized.blockId`, `normalized.clickUrl`, `normalized.fullKeyword`, `normalized.iabCategory`, `normalized.impressionUrl`, `normalized.rawUrl`, `normalized.requestId`, `normalized.suggestionId`, `normalized.title`, `normalized.url`, `normalized.urlTimestampIndex`, `queryContext.trimmedLowerCaseSearchString.length`, `searchString.length`, `suggestion.block_id`, `suggestion.click_url`, `suggestion.custom_details`, `suggestion.custom_details?.amp`, `suggestion.full_keyword`, `suggestion.iab_category`, `suggestion.impression_url`, `suggestion.is_top_pick`, `suggestion.request_id`, `suggestion.source`, `suggestion.url`, `this.#minKeywordLength`, `this.showLessFrequentlyCount`

## AmpSuggestions.getResultCommands()
- 位置: L200-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `this.canShowLessFrequently`

## AmpSuggestions.onImpression()
- 位置: L245-259
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (state == "engagement")` → `this.#submitQuickSuggestImpressionPing()`

## AmpSuggestions.onEngagement()
- 位置: L267-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 条件付き依存: `if (details.isSessionOngoing)` → `this.#submitQuickSuggestImpressionPing()`
- 条件付き依存: `if (pingData)` → `this.#submitQuickSuggestPing()`
- 参照: `QUICK_SUGGEST_PING_TYPE.BLOCK`, `QUICK_SUGGEST_PING_TYPE.CLICK`, `details.isSessionOngoing`, `details.selType`, `result.payload.sponsoredClickUrl`, `result.payload.sponsoredIabCategory`, `searchString.length`

## AmpSuggestions.incrementShowLessFrequentlyCount()
- 位置: L318-325
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## AmpSuggestions.showLessFrequentlyCount()
- 位置: L327-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## AmpSuggestions.canShowLessFrequently()
- 位置: L332-335
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## AmpSuggestions.#minKeywordLength()
- 位置: L337-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## AmpSuggestions.isUrlEquivalentToResultUrl()
- 位置: L342-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TIMESTAMP_REGEXP.test()`, `resultURL.substring()`, `url.substring()`
- 条件付き依存: `if (result.payload.source == "rust")` → `lazy.rawSuggestionUrlMatches()`
- 参照: `result.payload`, `result.payload.originalUrl`, `result.payload.source`, `result.payload.url`, `resultURL.length`, `url.length`

## AmpSuggestions.#submitQuickSuggestPing()
- 位置: L383-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings.quickSuggest.submit()`, `Object.entries()`, `lazy.ContextId.request()`, `lazy.NimbusFeatures.urlbar.getEnrollmentMetadata()`, `lazy.UrlbarPrefs.get()`, `result.payload.sponsoredAdvertiser.toLocaleLowerCase()`, `result.suggestedIndex.toString()`, `submission.catch()`, `this.#lastPingSubmission.then()`
- 条件付き依存: `if (queryContext.isPrivate)` → `Promise.resolve()`
- 条件付き依存: `if (value !== undefined && value !== "")` → `glean.set()`
- 参照: `Glean.quickSuggest`, `console.error`, `lazy.Region.home`, `nimbusEnrollment?.branch`, `nimbusEnrollment?.slug`, `queryContext.isPrivate`, `result.isBestMatch`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.requestId`, `result.payload.source`, `result.payload.sponsoredBlockId`, `result.payload.suggestionId`, `result.rowIndex`, `this.#lastPingSubmission`

## AmpSuggestions.#submitQuickSuggestImpressionPing()
- 位置: L433-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#submitQuickSuggestPing()`
- 参照: `QUICK_SUGGEST_PING_TYPE.IMPRESSION`, `details.result?.id`, `details.selType`, `result.id`, `result.payload.sponsoredImpressionUrl`

## AmpSuggestions.#submitQuickSuggestDeletionRequestPing()
- 位置: async L449-458
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.ContextId.rotationEnabled)` → `lazy.ContextId.forceRotation()`
- 条件付き依存: `if (!(lazy.ContextId.rotationEnabled))` → `Glean.quickSuggest.contextId.set()`
- 条件付き依存: `if (!(lazy.ContextId.rotationEnabled))` → `lazy.ContextId.request()`
- 条件付き依存: `if (!(lazy.ContextId.rotationEnabled))` → `GleanPings.quickSuggestDeletionRequest.submit()`
- 参照: `lazy.ContextId.rotationEnabled`

## AmpSuggestions.#replaceSuggestionTemplates()
- 位置: L475-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.toString()`, `n.toString().padStart()`, `now.getDate()`, `now.getFullYear()`, `now.getHours()`, `now.getMonth()`, `timestampParts .map()`, `timestampParts .map(n => n.toString().padStart(2, "0")) .join()`, `value.indexOf()`
- 条件付き依存: `if (timestampIndex >= 0)` → `value.substring()`
- 参照: `TIMESTAMP_TEMPLATE.length`, `suggestion.urlTimestampIndex`

## AmpSuggestions.TIMESTAMP_TEMPLATE()
- 位置: L509-511
- 役割: (未記入)
- 触るとき: (未記入)

## AmpSuggestions.TIMESTAMP_LENGTH()
- 位置: L513-515
- 役割: (未記入)
- 触るとき: (未記入)
