# browser/components/urlbar/private/DynamicSuggestions.sys.mjs

source: browser/components/urlbar/private/DynamicSuggestions.sys.mjs
source-hash: 2487dd1027dcaf5755220dc22200b1759a15e5e7
lines: 163

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## DynamicSuggestions.enablingPreferences()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)

## DynamicSuggestions.shouldEnable()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dynamicRustSuggestionTypes.length`

## DynamicSuggestions.rustSuggestionType()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)

## DynamicSuggestions.dynamicRustSuggestionTypes()
- 位置: L43-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`

## DynamicSuggestions.isSuggestionSponsored()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `suggestion.data?.result?.payload?.isSponsored`

## DynamicSuggestions.getSuggestionTelemetryType()
- 位置: L52-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.telemetryType`, `suggestion.data?.result?.isHiddenExposure`, `suggestion.suggestionType`

## DynamicSuggestions.makeResult()
- 位置: L62-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `result.hasOwnProperty()`
- 条件付き依存: `if (!data || typeof data != "object")` → `this.logger.warn()`
- 条件付き依存: `if (!result || typeof result != "object")` → `this.logger.warn()`
- 条件付き依存: `if (typeof result.payload != "object")` → `this.logger.warn()`
- 条件付き依存: `if (result.isHiddenExposure)` → `this.#makeExposureResult()`
- 参照: `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `payload.helpUrl`, `payload.isManageable`, `payload.isSponsored`, `result.bypassSuggestAll`, `result.isHiddenExposure`, `result.payload`, `resultProperties.payload`

## DynamicSuggestions.onEngagement()
- 位置: L125-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`
- 参照: `details.selType`

## DynamicSuggestions.#makeExposureResult()
- 位置: L143-161
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.EXPOSURE_TELEMETRY.HIDDEN`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`
