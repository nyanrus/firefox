# browser/components/urlbar/private/ImportantDatesSuggestions.sys.mjs

source: browser/components/urlbar/private/ImportantDatesSuggestions.sys.mjs
source-hash: ccdb697be1875535513b9937f276c4e3b1ee76d3
lines: 262

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ImportantDatesSuggestions.enablingPreferences()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)

## ImportantDatesSuggestions.primaryUserControlledPreferences()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)

## ImportantDatesSuggestions.rustSuggestionType()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)

## ImportantDatesSuggestions.dynamicRustSuggestionTypes()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)

## ImportantDatesSuggestions.isSuggestionSponsored()
- 位置: L40-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.isSponsored`

## ImportantDatesSuggestions.getSuggestionTelemetryType()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.telemetryType`, `this.dynamicRustSuggestionTypes`

## ImportantDatesSuggestions.makeResult()
- 位置: async L54-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#makeDateResult()`
- 条件付き依存: `if ( !suggestion.data?.result?.payload || typeof suggestion.data.result.payload != "object" )` → `this.logger.warn()`
- 参照: `suggestion.data.result.payload`, `suggestion.data?.result?.payload`

## ImportantDatesSuggestions.#formatDateOrRange()
- 位置: L86-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `format.format()`
- 条件付き依存: `if (Array.isArray(dateStr))` → `format.formatRange()`
- 参照: `Intl.DateTimeFormat`, `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## ImportantDatesSuggestions.#formatDateCountdown()
- 位置: L120-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `this.#getDaysUntil()`
- 条件付き依存: `if (Array.isArray(dateStr))` → `this.#getDaysUntil()`

## ImportantDatesSuggestions.#getDaysUntil()
- 位置: L169-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `date.getTime()`, `now.getTime()`, `now.setHours()`

## ImportantDatesSuggestions.#makeDateResult()
- 位置: L189-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.UrlbarSearchUtils.getDefaultEngine()`, `payload.dates.find()`, `payload.name.toLowerCase()`, `this.#formatDateOrRange()`, `this.#getDaysUntil()`
- 条件付き依存: `if (!(daysUntilStart > SHOW_COUNTDOWN_THRESHOLD_DAYS))` → `this.#formatDateCountdown()`
- 参照: `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarSearchUtils.getDefaultEngine(queryContext.isPrivate) .name`, `lazy.UrlbarShared.HIGHLIGHT.ALL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `payload.name`, `queryContext.isPrivate`

## ImportantDatesSuggestions.onEngagement()
- 位置: L244-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`
- 参照: `details.selType`
