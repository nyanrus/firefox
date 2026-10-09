# browser/components/urlbar/private/YelpSuggestions.sys.mjs

source: browser/components/urlbar/private/YelpSuggestions.sys.mjs
source-hash: 5474ec145da4fac55d6179f17a03d575fbe971f6
lines: 586

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## YelpSuggestions.enablingPreferences()
- 位置: L39-46
- 役割: (未記入)
- 触るとき: (未記入)

## YelpSuggestions.primaryUserControlledPreferences()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)

## YelpSuggestions.rustSuggestionType()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)

## YelpSuggestions.mlIntent()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)

## YelpSuggestions.isMlIntentEnabled()
- 位置: L60-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`

## YelpSuggestions.showLessFrequentlyCount()
- 位置: L67-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## YelpSuggestions.canShowLessFrequently()
- 位置: L72-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## YelpSuggestions.isSuggestionSponsored()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)

## YelpSuggestions.getSuggestionTelemetryType()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)

## YelpSuggestions.enable()
- 位置: L88-92
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#metadataCache`

## YelpSuggestions.filterSuggestions()
- 位置: async L94-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("yelpMlEnabled"))` → `suggestions.find()`
- 条件付き依存: `if (suggestion)` → `this.#normalizeRustSuggestion()`
- 条件付き依存: `if (!(!lazy.UrlbarPrefs.get("yelpMlEnabled")))` → `suggestions.find()`
- 条件付き依存: `if (!this.#metadataCache)` → `this.#makeMetadataCache()`
- 条件付き依存: `if (suggestion)` → `this.#normalizeMlSuggestion()`
- 参照: `s.source`, `this.#metadataCache`

## YelpSuggestions.makeResult()
- 位置: async L137-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[city, region].filter()`, `[city, region].filter(s => !!s).join()`, `lazy.UrlbarPrefs.get()`, `url.searchParams.set()`, `url.toString()`
- 条件付き依存: `if (!city && !region)` → `lazy.GeolocationUtils.geolocation()`
- 条件付き依存: `if (!(!city && !region))` → `this.#bestCityRegion()`
- 条件付き依存: `if (locationStr)` → `url.searchParams.set()`
- 条件付き依存: `if (!resultProperties.isBestMatch)` → `lazy.UrlbarPrefs.get()`
- 参照: `geo.city`, `geo.region_code`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `lazy.YelpSubjectType.SERVICE`, `match.city`, `match.region`, `payload.title`, `payload.titleL10n`, `resultProperties.isBestMatch`, `resultProperties.isSuggestedIndexRelativeToGroup`, `resultProperties.suggestedIndex`, `searchString.length`, `suggestion.hasLocationSign`, `suggestion.icon_blob`, `suggestion.locationParam`, `suggestion.subjectExactMatch`, `suggestion.subjectType`, `suggestion.title`, `suggestion.url`, `this.#minKeywordLength`, `this.showLessFrequentlyCount`

## YelpSuggestions.getResultCommands()
- 位置: L244-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## YelpSuggestions.onEngagement()
- 位置: L295-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `controller.view.acknowledgeFeedback()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `result.id`, `searchString.length`

## YelpSuggestions.incrementShowLessFrequentlyCount()
- 位置: L334-341
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## YelpSuggestions.#minKeywordLength()
- 位置: L343-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Services.prefs.prefHasUserValue()`, `lazy.UrlbarPrefs.get()`
- XPCOM: `Services.prefs`

## YelpSuggestions.#normalizeRustSuggestion()
- 位置: L359-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.searchParams.get()`
- 条件付き依存: `if (loc)` → `url.searchParams.delete()`
- 条件付き依存: `if (loc)` → `url.toString()`
- 条件付き依存: `if (loc)` → `suggestion.title.endsWith()`
- 条件付き依存: `if (suggestion.title.endsWith(loc))` → `suggestion.title .substring(0, suggestion.title.length - loc.length) .trimEnd()`
- 条件付き依存: `if (suggestion.title.endsWith(loc))` → `suggestion.title .substring()`
- 参照: `loc.length`, `suggestion.city`, `suggestion.locationParam`, `suggestion.title`, `suggestion.title.length`, `suggestion.url`

## YelpSuggestions.#normalizeMlSuggestion()
- 位置: L390-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.searchParams.set()`, `url.toString()`
- 参照: `ml.location?.city`, `ml.location?.state`, `ml.subject`, `this.#metadataCache.findDesc`, `this.#metadataCache.findLoc`, `this.#metadataCache.iconBlob`, `this.#metadataCache.score`, `this.#metadataCache.urlOrigin`, `this.#metadataCache.urlPathname`, `url.pathname`

## YelpSuggestions.#makeMetadataCache()
- 位置: async L423-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `lazy.QuickSuggest.rustBackend.query()`, `this.logger.debug()`
- 条件付き依存: `if (!rs.length)` → `this.logger.debug()`
- 条件付き依存: `if (!(!rs.length))` → `findParamWithValue()`
- 参照: `rs.length`, `suggestion.icon_blob`, `suggestion.score`, `suggestion.url`, `url.origin`, `url.pathname`

## findParamWithValue()
- 位置: L436-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...url.searchParams.entries()].find()`, `url.searchParams.entries()`

## YelpSuggestions.#bestCityRegion()
- 位置: async L493-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `regionMatches?.filter()`
- 条件付き依存: `if (region)` → `lazy.QuickSuggest.rustBackend.fetchGeonames()`
- 条件付き依存: `if (city)` → `lazy.QuickSuggest.rustBackend.fetchGeonames()`
- 条件付き依存: `if (city)` → `regionMatches?.map()`
- 条件付き依存: `if (city)` → `cityMatches.filter()`
- 条件付き依存: `if (city)` → `lazy.GeolocationUtils.best()`
- 条件付き依存: `if (city)` → `best.geoname.adminDivisionCodes.get()`
- 条件付き依存: `if (regionMatches?.length)` → `lazy.GeolocationUtils.best()`
- 参照: `best.geoname.name`, `cityMatches.length`, `lazy.GeonameMatchType.NAME`, `m.geoname`, `match.matchType`, `match.prefix`, `regionMatches.length`, `regionMatches?.length`

## YelpSuggestions._test_invalidateMetadataCache()
- 位置: L560-562
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#metadataCache`

## locationFromGeonameMatch()
- 位置: L577-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `match.geoname.adminDivisionCodes.get()`
- 参照: `match.geoname.countryCode`, `match.geoname.latitude`, `match.geoname.longitude`, `match.geoname.population`
