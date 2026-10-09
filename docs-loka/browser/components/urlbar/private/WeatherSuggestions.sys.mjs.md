# browser/components/urlbar/private/WeatherSuggestions.sys.mjs

source: browser/components/urlbar/private/WeatherSuggestions.sys.mjs
source-hash: f78d312e18e520455aa645ff7858919d46398916
lines: 594

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WeatherSuggestions.constructor()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## WeatherSuggestions.enablingPreferences()
- 位置: L145-152
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherSuggestions.primaryUserControlledPreferences()
- 位置: L154-156
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherSuggestions.rustSuggestionType()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherSuggestions.showLessFrequentlyCount()
- 位置: L162-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## WeatherSuggestions.canShowLessFrequently()
- 位置: L167-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## WeatherSuggestions.isSuggestionSponsored()
- 位置: L175-177
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherSuggestions.getSuggestionTelemetryType()
- 位置: L179-181
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherSuggestions.enable()
- 位置: L183-187
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#merino`

## WeatherSuggestions.filterSuggestions()
- 位置: async L189-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.GeolocationUtils.best()`, `s.city?.adminDivisionCodes.get()`
- 参照: `s.city?.countryCode`, `s.city?.latitude`, `s.city?.longitude`, `s.city?.population`, `suggestions.length`

## WeatherSuggestions.makeResult()
- 位置: async L209-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `lazy.UrlbarPrefs.get()`, `this.#fetchMerinoSuggestion()`, `this.#getTitleL10n()`, `unit.toUpperCase()`
- 条件付き依存: `if (treatment == 1 || treatment == 2)` → `this.#makeDynamicResult()`
- 参照: `Services.locale.regionalPrefsLocales`, `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `merinoSuggestion.current_conditions.icon_id`, `merinoSuggestion.current_conditions.temperature`, `merinoSuggestion.url`, `searchString.length`, `suggestion.city`, `this.#minKeywordLength`, `titleL10n.args`, `titleL10n.id`
- XPCOM: `Services.locale`

## WeatherSuggestions.#makeDynamicResult()
- 位置: L259-281
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `suggestion.city_name`, `suggestion.current_conditions.icon_id`, `suggestion.current_conditions.summary`, `suggestion.current_conditions.temperature`, `suggestion.forecast.high`, `suggestion.forecast.low`, `suggestion.forecast.summary`, `suggestion.region_code`, `suggestion.url`

## WeatherSuggestions.getViewTemplate()
- 位置: L283-285
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherSuggestions.getViewUpdate()
- 位置: L287-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `result.payload.temperatureUnit.toUpperCase()`
- 参照: `result.payload.city`, `result.payload.currentConditions`, `result.payload.forecast`, `result.payload.high`, `result.payload.iconId`, `result.payload.low`, `result.payload.region`, `result.payload.temperature`, `result.payload.url`

## WeatherSuggestions.getResultCommands()
- 位置: L363-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## WeatherSuggestions.onEngagement()
- 位置: L414-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `controller.view.acknowledgeFeedback()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`, `this.logger.info()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `result.id`, `searchString.length`

## WeatherSuggestions.incrementShowLessFrequentlyCount()
- 位置: L450-457
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## WeatherSuggestions.#config()
- 位置: L459-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rustBackend.getConfigForSuggestionType()`
- 参照: `lazy.QuickSuggest`, `rustBackend.isEnabled`, `this.rustSuggestionType`

## WeatherSuggestions.#minKeywordLength()
- 位置: L467-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Services.prefs.prefHasUserValue()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( !Services.prefs.prefHasUserValue( "browser.urlbar.weather.minKeywordLength" ) )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(nimbusValue !== null))` → `isNaN()`
- 参照: `this.#config.minKeywordLength`
- XPCOM: `Services.prefs`

## WeatherSuggestions.#fetchMerinoSuggestion()
- 位置: async L488-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...cityGeoname.adminDivisionCodes.entries()] .sort()`, `[...cityGeoname.adminDivisionCodes.entries()] .sort(([level1, _admin1], [level2, _admin2]) => level1 - level2) .map()`, `cityGeoname.adminDivisionCodes.entries()`, `merino.fetchWeatherReport()`
- 参照: `cityGeoname?.adminDivisionCodes`, `cityGeoname?.countryCode`, `cityGeoname?.name`, `lazy.MerinoClient`, `this.#fetchInstance`, `this.#merino`, `this.#timeoutMs`, `this.constructor.name`

## WeatherSuggestions.#getTitleL10n()
- 位置: async L518-580
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(!cityGeoname))` → `lazy.QuickSuggest.rustBackend.fetchGeonameAlternates()`
- 条件付き依存: `if (!(!cityGeoname))` → `NORTH_AMERICA_COUNTRY_CODES.has()`
- 条件付き依存: `if (NORTH_AMERICA_COUNTRY_CODES.has(cityGeoname.countryCode))` → `alts.adminDivisions.get()`
- 参照: `alts.adminDivisions.get(1)?.abbreviation`, `alts.adminDivisions.get(1)?.localized`, `alts.adminDivisions.get(1)?.primary`, `alts.country?.localized`, `alts.country?.primary`, `alts.geoname.localized`, `alts.geoname.primary`, `cityGeoname.countryCode`, `lazy.Region.home`, `merinoSuggestion.city_name`, `merinoSuggestion.region_code`

## WeatherSuggestions._test_merino()
- 位置: L582-584
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#merino`

## WeatherSuggestions._test_setTimeoutMs()
- 位置: L586-588
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#timeoutMs`
