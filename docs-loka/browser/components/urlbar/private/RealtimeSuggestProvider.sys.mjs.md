# browser/components/urlbar/private/RealtimeSuggestProvider.sys.mjs

source: browser/components/urlbar/private/RealtimeSuggestProvider.sys.mjs
source-hash: d8afa268f0f4b9b7ae053e4427e02cde0cc81160
lines: 708

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## RealtimeSuggestProvider.realtimeType()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.getViewTemplateForDescriptionTop()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.getViewTemplateForDescriptionBottom()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.getViewUpdateForPayloadItem()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.dynamicRustSuggestionTypes()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.merinoProvider()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.baseTelemetryType()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.realtimeTypeForFtl()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.realtimeType.replace()`, `this.realtimeType.replace(/([A-Z])/g, "-$1").toLowerCase()`

## RealtimeSuggestProvider.featureGatePref()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.suggestPref()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.minKeywordLengthPref()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.showLessFrequentlyCountPref()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.optInIcon()
- 位置: L97-99
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.optInTitleL10n()
- 位置: L101-105
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.optInDescriptionL10n()
- 位置: L107-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.notInterestedCommandL10n()
- 位置: L114-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.acknowledgeDismissalL10n()
- 位置: L120-124
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.ariaGroupL10n()
- 位置: L126-131
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeTypeForFtl`

## RealtimeSuggestProvider.isSponsored()
- 位置: L133-135
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.dynamicResultType()
- 位置: L147-149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.realtimeType`

## RealtimeSuggestProvider.rustSuggestionType()
- 位置: L153-155
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.enablingPreferences()
- 位置: L157-176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.featureGatePref`, `this.suggestPref`

## RealtimeSuggestProvider.primaryUserControlledPreferences()
- 位置: L178-186
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.suggestPref`

## RealtimeSuggestProvider.shouldEnable()
- 位置: L188-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `dismissTypes.has()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("quicksuggest.online.enabled"))` → `lazy.UrlbarPrefs.get()`
- 参照: `this.featureGatePref`, `this.realtimeType`, `this.suggestPref`

## RealtimeSuggestProvider.isSuggestionSponsored()
- 位置: L234-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`, `suggestion.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.isSponsored`, `suggestion.is_sponsored`, `suggestion.source`, `this.isSponsored`

## RealtimeSuggestProvider.getSuggestionTelemetryType()
- 位置: L269-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`, `suggestion.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.telemetryType`, `suggestion.source`, `suggestion.telemetry_type`, `this.baseTelemetryType`

## RealtimeSuggestProvider.filterSuggestions()
- 位置: L285-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("quicksuggest.online.enabled"))` → `suggestions.filter()`
- 参照: `s.source`

## RealtimeSuggestProvider.makeResult()
- 位置: L294-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.isSuggestionSponsored()`, `this.makeMerinoResult()`, `this.makeOptInResult()`
- 参照: `suggestion.source`

## RealtimeSuggestProvider.makeMerinoResult()
- 位置: L314-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.makePayloadItem()`, `values.map()`, `values.some()`
- 条件付き依存: `if (values.some(v => v.query))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 参照: `engine?.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.isPrivate`, `searchString.length`, `suggestion.custom_details`, `suggestion.custom_details?.[this.merinoProvider]?.values`, `this.#minKeywordLength`, `this.dynamicResultType`, `this.isEnabled`, `this.merinoProvider`, `this.showLessFrequentlyCount`, `v.query`, `values?.length`

## RealtimeSuggestProvider.makePayloadItem()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.makeOptInResult()
- 位置: L380-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `notNowTypes.has()`
- 参照: `lazy.QuickSuggest.HELP_TOPIC`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.TIP`, `queryContext.searchString`, `this.optInDescriptionL10n`, `this.optInIcon`, `this.optInTitleL10n`, `this.realtimeType`

## RealtimeSuggestProvider.getViewTemplate()
- 位置: L436-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.map()`, `this.getViewTemplateForDescriptionBottom()`, `this.getViewTemplateForDescriptionTop()`, `this.getViewTemplateForImageContainer()`
- 参照: `item.query`, `item.url`, `items.length`, `items[0].query`, `items[0].url`, `result.payload`

## RealtimeSuggestProvider.getViewTemplateForImageContainer()
- 位置: L500-520
- 役割: (未記入)
- 触るとき: (未記入)

## RealtimeSuggestProvider.getViewUpdate()
- 位置: L522-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.getViewUpdateForPayloadItem()`
- 参照: `items.length`, `result.payload`, `this.ariaGroupL10n`

## RealtimeSuggestProvider.getResultCommands()
- 位置: L543-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `result.payload.source`, `this.canShowLessFrequently`, `this.notInterestedCommandL10n`

## RealtimeSuggestProvider.onEngagement()
- 位置: L590-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onMerinoEngagement()`, `this.onOptInEngagement()`
- 参照: `details.result.payload.source`

## RealtimeSuggestProvider.onMerinoEngagement()
- 位置: L606-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `details.selType`, `searchString.length`, `this.acknowledgeDismissalL10n`, `this.minKeywordLengthPref`, `this.suggestPref`

## RealtimeSuggestProvider.onOptInEngagement()
- 位置: L633-671
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `controller.input.startQuery()`, `controller.removeResult()`, `lazy.UrlbarPrefs.add()`, `lazy.UrlbarPrefs.set()`
- 参照: `details.result`, `details.selType`, `this.acknowledgeDismissalL10n`, `this.realtimeType`

## RealtimeSuggestProvider.incrementShowLessFrequentlyCount()
- 位置: L673-680
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`, `this.showLessFrequentlyCountPref`

## RealtimeSuggestProvider.showLessFrequentlyCount()
- 位置: L682-686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`
- 参照: `this.showLessFrequentlyCountPref`

## RealtimeSuggestProvider.canShowLessFrequently()
- 位置: L688-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## RealtimeSuggestProvider.#minKeywordLength()
- 位置: L696-706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Services.prefs.prefHasUserValue()`, `lazy.UrlbarPrefs.get()`
- 参照: `this.minKeywordLengthPref`
- XPCOM: `Services.prefs`
