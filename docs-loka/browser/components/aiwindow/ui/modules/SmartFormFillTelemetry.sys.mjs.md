# browser/components/aiwindow/ui/modules/SmartFormFillTelemetry.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillTelemetry.sys.mjs
source-hash: 08f4e7a36dce6de920106786b199ada8e08a009f
lines: 633

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## SmartFormFillTelemetry.#getLatency()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Math.round()`
- 参照: `flow.startTime`

## SmartFormFillTelemetry.#getErrorName()
- 位置: L167-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `REQUEST_ERROR_REASONS.has()`
- 参照: `error?.clientReason`

## SmartFormFillTelemetry.#getDecisionSource()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DECISION_SOURCE_BY_ACTION.get()`

## SmartFormFillTelemetry.#getPercent()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`

## SmartFormFillTelemetry.#getSimilarityStats()
- 位置: L205-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `scores.reduce()`, `this.#getPercent()`
- 参照: `scores.length`

## SmartFormFillTelemetry.#getTypedFieldCount()
- 位置: L226-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UNTYPED_FIELD_KINDS.has()`, `fields.filter()`
- 参照: `field.type`, `fields.filter( field => field.type && !UNTYPED_FIELD_KINDS.has(field.type) ).length`

## SmartFormFillTelemetry.#getUnknownFieldCount()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UNTYPED_FIELD_KINDS.has()`, `fields.filter()`
- 参照: `field.type`, `fields.filter(field => UNTYPED_FIELD_KINDS.has(field.type)).length`

## SmartFormFillTelemetry.startClassifyRequest()
- 位置: L252-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.smartWindow.formFillClassifyRequest.record()`
- 参照: `modelInfo.model`, `modelInfo.promptVersion`, `request.fields.length`

## SmartFormFillTelemetry.sendClassifyResponseTelemetry()
- 位置: L270-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formFillClassifyResponse.record()`, `this.#getLatency()`, `this.#getTypedFieldCount()`, `this.#getUnknownFieldCount()`
- 参照: `flow.flowId`, `response.fields`, `response.pageType`

## SmartFormFillTelemetry.sendClassifyErrorTelemetry()
- 位置: L289-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formFillClassifyResponse.record()`, `this.#getErrorName()`, `this.#getLatency()`
- 参照: `flow.flowId`

## SmartFormFillTelemetry.startRelevantTabsRequest()
- 位置: L308-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.smartWindow.formRelevantTabsRequest.record()`
- 参照: `modelInfo.model`, `modelInfo.promptVersion`, `request.tabs.length`

## SmartFormFillTelemetry.sendRelevantTabsResponseTelemetry()
- 位置: L328-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formRelevantTabsResponse.record()`, `rated()`, `this.#getLatency()`
- 参照: `flow.flowId`, `response?.selectedTabs`, `response?.selectedTabs?.length`

## rated()
- 位置: L330-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectedTabs.filter()`
- 参照: `selectedTabs.filter(tab => tab?.relevance === level).length`, `tab?.relevance`

## SmartFormFillTelemetry.sendRelevantTabsErrorTelemetry()
- 位置: L351-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formRelevantTabsResponse.record()`, `this.#getErrorName()`, `this.#getLatency()`
- 参照: `flow.flowId`

## SmartFormFillTelemetry.sendRelevantTabsOutcomeTelemetry()
- 位置: L368-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formRelevantTabsOutcome.record()`, `[...final].filter()`, `[...suggested].filter()`, `final.has()`, `finalTabs.map()`, `suggested.has()`, `suggestedTabs.map()`
- 参照: `[...final].filter(id => !suggested.has(id)).length`, `[...suggested].filter(id => !final.has(id)).length`, `[...suggested].filter(id => final.has(id)).length`, `editor?.opens`, `editor?.result`, `final.size`

## SmartFormFillTelemetry.startGenerateRequest()
- 位置: L395-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.smartWindow.formFillGenerateRequest.record()`, `similarityByMemory.values()`, `this.#getSimilarityStats()`
- 参照: `modelInfo.model`, `modelInfo.promptVersion`, `request.context.memories.length`, `request.context.relevantTabs.length`, `similarity?.avg`, `similarity?.max`, `similarity?.min`, `valuesByToken.size`

## SmartFormFillTelemetry.sendGenerateResponseTelemetry()
- 位置: L428-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(response.memories_used ?? []) .map()`, `(response.memories_used ?? []) .map(memoryId => similarityByMemory.get(memoryId)) .filter()`, `Glean.smartWindow.formFillGenerateResponse.record()`, `similarityByMemory.get()`, `this.#getLatency()`, `this.#getSimilarityStats()`
- 参照: `flow.flowId`, `response.batches?.failed`, `response.batches?.total`, `response.memories_used`, `response.memories_used?.length`, `response.tabs_used?.length`, `similarity?.avg`, `similarity?.max`, `similarity?.min`

## SmartFormFillTelemetry.sendGenerateErrorTelemetry()
- 位置: L460-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formFillGenerateResponse.record()`, `this.#getErrorName()`, `this.#getLatency()`
- 参照: `flow.flowId`

## SmartFormFillTelemetry.resolveFieldDecisions()
- 位置: L480-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classifications.get()`, `fields.map()`, `formFields.findIndex()`, `this.#getDecisionSource()`, `this.#getPercent()`, `tokensByFieldId.get()`, `tokensByFieldId.has()`, `values.fields?.find()`
- 参照: `classifications.get(field.id)?.type`, `field.id`, `field.inputType`, `field.localConfidence`, `field.localGuess`, `field.localSource`, `result?.action`, `result?.confidence`

## SmartFormFillTelemetry.sendFillFieldTelemetry()
- 位置: L515-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formFillField.record()`, `filledFieldIds.includes()`
- 参照: `decision.confidence`, `decision.fieldId`, `decision.fieldKind`, `decision.fieldSeq`, `decision.inputType`, `decision.preLLMConfidence`, `decision.preLLMFieldKind`, `decision.preLLMSource`, `decision.source`, `decision.tokenAvailable`, `decision.tokenKind`

## SmartFormFillTelemetry.#getFieldOutcome()
- 位置: L542-548
- 役割: (未記入)
- 触るとき: (未記入)

## SmartFormFillTelemetry.sendFillFieldOutcomeTelemetry()
- 位置: L565-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formFillFieldOutcome.record()`, `decisions.find()`, `this.#getFieldOutcome()`
- 参照: `decision.confidence`, `decision.fieldKind`, `decision.fieldSeq`, `decision.source`, `field.filledLength`, `field.finalLength`, `field.id`

## SmartFormFillTelemetry.sendFillFieldReviewOutcomeTelemetry()
- 位置: L601-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.formFillFieldReviewOutcome.record()`, `decisions.find()`, `generated.get()`, `this.#getFieldOutcome()`, `value.trim()`
- 参照: `decision.fieldSeq`, `generatedValue.length`, `value.length`
