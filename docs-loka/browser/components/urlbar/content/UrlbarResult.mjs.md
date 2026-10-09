# browser/components/urlbar/content/UrlbarResult.mjs

source: browser/components/urlbar/content/UrlbarResult.mjs
source-hash: febdaae5818d21b142ba1d5968875133b6f3adb9
lines: 709

## <module>
- 役割: (未記入)

## UrlbarResult.constructor()
- 位置: L82-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(payload).filter()`, `Object.fromEntries()`, `Object.values()`, `Object.values(UrlbarShared.RESULT_SOURCE).includes()`, `Object.values(UrlbarShared.RESULT_TYPE).includes()`, `this.#validatePayload()`
- 条件付き依存: `if (highlights)` → `Object.freeze()`
- 参照: `UrlbarShared.EXPOSURE_TELEMETRY.NONE`, `UrlbarShared.RESULT_SOURCE`, `UrlbarShared.RESULT_TYPE`, `UrlbarShared.RESULT_TYPE.TIP`, `this.#autofill`, `this.#exposureTelemetry`, `this.#group`, `this.#heuristic`, `this.#hideRowLabel`, `this.#highlights`, `this.#isBestMatch`, `this.#isBottomUrlSuggestion`, `this.#isRichSuggestion`, `this.#isSuggestedIndexRelativeToGroup`, `this.#payload`, `this.#providerName`, `this.#resultSpan`, `this.#richSuggestionIconSize`, `this.#richSuggestionIconVariation`, `this.#rowLabel`, `this.#showFeedbackMenu`, `this.#source`, `this.#suggestedIndex`, `this.#testForceNewContent`, `this.#type`

## UrlbarResult.type()
- 位置: L203-205
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#type`

## UrlbarResult.source()
- 位置: L212-214
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#source`

## UrlbarResult.autofill()
- 位置: L221-223
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#autofill`

## UrlbarResult.exposureTelemetry()
- 位置: L231-233
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#exposureTelemetry`

## UrlbarResult.exposureTelemetry()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#exposureTelemetry`

## UrlbarResult.group()
- 位置: L242-244
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#group`

## UrlbarResult.heuristic()
- 位置: L252-254
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#heuristic`

## UrlbarResult.hideRowLabel()
- 位置: L261-263
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#hideRowLabel`

## UrlbarResult.isBestMatch()
- 位置: L270-272
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isBestMatch`

## UrlbarResult.isBottomUrlSuggestion()
- 位置: L280-282
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isBottomUrlSuggestion`

## UrlbarResult.isRichSuggestion()
- 位置: L290-292
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isRichSuggestion`

## UrlbarResult.isRichSuggestion()
- 位置: L293-295
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isRichSuggestion`

## UrlbarResult.isSuggestedIndexRelativeToGroup()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isSuggestedIndexRelativeToGroup`

## UrlbarResult.isSuggestedIndexRelativeToGroup()
- 位置: L306-308
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isSuggestedIndexRelativeToGroup`

## UrlbarResult.providerName()
- 位置: L315-317
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#providerName`

## UrlbarResult.providerName()
- 位置: L318-320
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#providerName`

## UrlbarResult.providerType()
- 位置: L327-329
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#providerType`

## UrlbarResult.providerType()
- 位置: L330-332
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#providerType`

## UrlbarResult.resultSpan()
- 位置: L341-343
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#resultSpan`

## UrlbarResult.richSuggestionIconSize()
- 位置: L350-352
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#richSuggestionIconSize`

## UrlbarResult.richSuggestionIconVariation()
- 位置: L360-362
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#richSuggestionIconVariation`

## UrlbarResult.richSuggestionIconSize()
- 位置: L363-365
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#richSuggestionIconSize`

## UrlbarResult.rowLabel()
- 位置: L373-375
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#rowLabel`

## UrlbarResult.showFeedbackMenu()
- 位置: L382-384
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#showFeedbackMenu`

## UrlbarResult.suggestedIndex()
- 位置: L393-395
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#suggestedIndex`

## UrlbarResult.suggestedIndex()
- 位置: L396-398
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#suggestedIndex`

## UrlbarResult.payload()
- 位置: L404-406
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#payload`

## UrlbarResult.testForceNewContent()
- 位置: L408-410
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#testForceNewContent`

## UrlbarResult.testHighlights()
- 位置: L413-415
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#highlights`

## UrlbarResult.icon()
- 位置: L422-424
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.payload.icon`

## UrlbarResult.hasSuggestedIndex()
- 位置: L433-435
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.suggestedIndex`

## UrlbarResult.isHiddenExposure()
- 位置: L444-446
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.EXPOSURE_TELEMETRY.HIDDEN`, `this.exposureTelemetry`

## UrlbarResult.getDisplayableValueAndHighlights()
- 位置: L460-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `UrlbarShared.getTokenMatches()`, `structuredClone()`, `this.#displayValuesCache.has()`, `this.#displayValuesCache.set()`, `value.map()`
- 条件付き依存: `if (this.#displayValuesCache.has(payloadName))` → `this.#displayValuesCache.get()`
- 条件付き依存: `if (this.#displayValuesCache.has(payloadName))` → `UrlbarShared.deepEqual()`
- 条件付き依存: `if ( options.isURL == cached.options.isURL && (options.tokens == undefined || UrlbarShared.deepEqual(options.tokens, cached.options.tokens)) )` → `this.#displayValuesCache.get()`
- 条件付き依存: `if (isURL)` → `UrlbarShared.prepareUrlForDisplay()`
- 条件付き依存: `if (typeof value == "string")` → `value.substring()`
- 条件付き依存: `if (!options.tokens?.length || !highlightType)` → `this.#displayValuesCache.set()`
- 参照: `UrlbarShared.HIGHLIGHT.TYPED`, `UrlbarShared.MAX_TEXT_LENGTH`, `cached.options.isURL`, `cached.options.tokens`, `new URL(this.payload.url).URI.displayHostPort`, `options.isURL`, `options.tokens`, `options.tokens?.length`, `this.#displayValuesCache`, `this.#highlights`, `this.payload`, `this.payload.url`

## UrlbarResult.#validatePayload()
- 位置: L553-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.JsonSchemaValidator.validate()`, `lazy.UrlbarUtils.getPayloadSchema()`
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `result.error`, `result.valid`, `this.type`

## UrlbarResult.toString()
- 位置: L583-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`
- 条件付き依存: `if (this.payload.url)` → `this.payload.url.substr()`
- 参照: `this.payload.engine`, `this.payload.keyword`, `this.payload.query`, `this.payload.suggestion`, `this.payload.title`, `this.payload.url`

## UrlbarResult.toWire()
- 位置: L607-636
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#autofill`, `this.#exposureTelemetry`, `this.#group`, `this.#heuristic`, `this.#hideRowLabel`, `this.#highlights`, `this.#isBestMatch`, `this.#isBottomUrlSuggestion`, `this.#isRichSuggestion`, `this.#isSuggestedIndexRelativeToGroup`, `this.#payload`, `this.#providerName`, `this.#providerType`, `this.#resultSpan`, `this.#richSuggestionIconSize`, `this.#richSuggestionIconVariation`, `this.#rowLabel`, `this.#showFeedbackMenu`, `this.#source`, `this.#suggestedIndex`, `this.#testForceNewContent`, `this.#type`, `this.commands`, `this.id`, `this.isSERP`, `this.rowIndex`

## UrlbarResult.fromWire()
- 位置: L655-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `liveResults?.find()`
- 参照: `liveResult.rowIndex`, `r.id`, `result.commands`, `result.id`, `result.isSERP`, `result.providerType`, `result.rowIndex`, `wire.commands`, `wire.id`, `wire.isSERP`, `wire.providerType`, `wire.rowIndex`
