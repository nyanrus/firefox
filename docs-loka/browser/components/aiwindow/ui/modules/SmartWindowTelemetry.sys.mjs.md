# browser/components/aiwindow/ui/modules/SmartWindowTelemetry.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartWindowTelemetry.sys.mjs
source-hash: 768d54783b683ca4b41e0561b15b843039660add
lines: 224

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `SmartWindowTelemetry.updateEnabledMetric()`, `SmartWindowTelemetry.updateMemoriesFromConversationMetric()`, `SmartWindowTelemetry.updateMemoriesFromHistoryMetric()`, `SmartWindowTelemetry.updateModelMetric()`, `SmartWindowTelemetry.updateSetDefaultOptinMetric()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## init()
- 位置: L81-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateEnabledMetric()`, `this.updateMemoriesFromConversationMetric()`, `this.updateMemoriesFromHistoryMetric()`, `this.updateModelMetric()`, `this.updateModelMetric().catch()`, `this.updateSetDefaultOptinMetric()`
- 参照: `console.error`, `this._initialized`

## updateMemoriesFromConversationMetric()
- 位置: L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoriesOptin.generate_from_conversation.set()`
- 参照: `lazy.memoriesFromConversation`

## updateMemoriesFromHistoryMetric()
- 位置: L101-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoriesOptin.generate_from_history.set()`
- 参照: `lazy.memoriesFromHistory`

## updateSetDefaultOptinMetric()
- 位置: L108-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.setDefaultOptin.set()`
- 参照: `lazy.isDefaultWindow`

## updateEnabledMetric()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.enabled.set()`
- 参照: `lazy.smartWindowEnabled`

## updateModelMetric()
- 位置: async L116-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.model.set()`, `lazy.getModelForChoice()`
- 参照: `lazy.modelChoice`, `modelInfo?.model`

## recordClientError()
- 位置: L142-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extractClientErrorFields()`, `this.recordClientErrorDetail()`

## recordClientErrorDetail()
- 位置: L160-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CLIENT_ERROR_SOURCES.has()`, `Glean.smartWindow.clientError.record()`, `Number.isFinite()`, `asString()`, `clientErrorEmitCounts.get()`, `clientErrorEmitCounts.set()`, `normalizeClientErrorMessage()`
- 条件付き依存: `if (!CLIENT_ERROR_SOURCES.has(source))` → `console.warn()`
- 条件付き依存: `if (!CLIENT_ERROR_SOURCES.has(source))` → `JSON.stringify()`
- 参照: `context.chat_id`, `context.location`, `context.message_seq`, `context.model`, `detail.lineno`, `detail?.filename`, `detail?.lineno`, `detail?.message`, `detail?.messageKey`, `detail?.name`, `detail?.source`

## _resetClientErrorDedupForTests()
- 位置: L201-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clientErrorEmitCounts.clear()`

## recordUriLoad()
- 位置: async L205-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.smartWindow.uriLoad.record()`, `lazy.getModelForChoice()`
- 参照: `lazy.modelChoice`, `modelInfo?.model`, `this.lastUriLoadTimestamp`
