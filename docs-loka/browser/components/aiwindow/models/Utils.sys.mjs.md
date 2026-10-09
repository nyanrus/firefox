# browser/components/aiwindow/models/Utils.sys.mjs

source: browser/components/aiwindow/models/Utils.sys.mjs
source-hash: 1a697c87e67806a0f03dfcd61150805be4479082
lines: 841

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `Services.prefs.addObserver()`, `XPCOMUtils.declareLazy()`

## dropRecordsCache()
- 位置: L38-44
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (_recordsIdleTimer)` → `clearTimeout()`

## touchRecordsCache()
- 位置: L48-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`
- 条件付き依存: `if (_recordsIdleTimer)` → `clearTimeout()`

## getRemoteClient()
- 位置: L62-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.on()`, `console.error()`, `dropRecordsCache()`, `lazy.RemoteSettings()`, `refreshModelsDataCache()`

## getRemoteRecords()
- 位置: L91-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getRemoteClient()`, `getRemoteClient() .get()`, `getRemoteClient() .get() .catch()`, `touchRecordsCache()`
- 条件付き依存: `if (_recordsPromise)` → `touchRecordsCache()`
- 条件付き依存: `if (_recordsPromise === promise)` → `dropRecordsCache()`

## _setRemoteClientForTesting()
- 位置: L118-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dropRecordsCache()`

## _clearRemoteClientForTesting()
- 位置: L126-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dropRecordsCache()`

## _clearRecordsCacheForTesting()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dropRecordsCache()`

## _setRecordsIdleMsForTesting()
- 位置: L145-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dropRecordsCache()`

## observe()
- 位置: L151-159
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "nsPref:changed" && data === MODEL_PREF)` → `console.warn()`
- 条件付き依存: `if (topic === "nsPref:changed" && data === MODEL_PREF)` → `dropRecordsCache()`

## [MODEL_FEATURES.CHAT]()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `MODEL_FEATURES.CHAT`
- XPCOM: `Services.prefs`

## parseVersion()
- 位置: L335-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^v?(\d+)\.(\d+)$/.exec()`, `Number()`

## checkMajorVersion()
- 位置: L354-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseVersion()`
- 参照: `parsed.major`

## isCustomModelChoice()
- 位置: L416-418
- 役割: (未記入)
- 触るとき: (未記入)

## selectMainConfig()
- 位置: L438-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkMajorVersion()`, `console.warn()`, `featureConfigs.filter()`, `sameMajor.find()`
- 条件付き依存: `if (sameMajor.length === 0)` → `console.warn()`
- 条件付き依存: `if (feature === MODEL_FEATURES.CHAT)` → `isCustomModelChoice()`
- 条件付き依存: `if (!isCustomModelChoice(modelChoiceId))` → `sameMajor.find()`
- 条件付き依存: `if (!isCustomModelChoice(modelChoiceId))` → `console.warn()`
- 条件付き依存: `if (!(!isCustomModelChoice(modelChoiceId)))` → `sameMajor.find()`
- 条件付き依存: `if (!(!isCustomModelChoice(modelChoiceId)))` → `console.warn()`
- 条件付き依存: `if (feature === MODEL_FEATURES.CHAT)` → `sameMajor.find()`
- 条件付き依存: `if (defaultConfig)` → `isCustomModelChoice()`
- 参照: `MODEL_FEATURES.CHAT`, `config.is_default`, `config.model`, `config.model_choice_id`, `config.version`, `sameMajor.length`

## parseModelDetails()
- 位置: L525-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `console.warn()`
- 参照: `details.brandName`, `details.labelId`, `details.ownerName`, `details.shortName`, `record?.model_details`

## resolveChatModelChoice()
- 位置: async L558-601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allRecords.filter()`, `console.warn()`, `getRemoteRecords()`, `parseModelDetails()`, `selectMainConfig()`
- 条件付き依存: `if (choiceId === "0")` → `getActiveFallbackModels()`
- 参照: `MODEL_FEATURES.CHAT`, `details?.brandName`, `details?.labelId`, `details?.ownerName`, `details?.shortName`, `r.feature`, `r.kind`, `record.model`, `record.owner_name`

## getActiveFallbackModels()
- 位置: L608-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## getModelDisplayOrder()
- 位置: L623-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## getModelForChoice()
- 位置: async L636-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActiveFallbackModels()`, `getCurrentModelChoiceId()`, `resolveChatModelChoice()`

## refreshModelsDataCache()
- 位置: async L678-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getAllModelsData()`

## getAllModelsData()
- 位置: async L688-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `getActiveFallbackModels()`, `getModelDisplayOrder()`, `getModelDisplayOrder().map()`, `getModelForChoice()`

## getCachedModelsData()
- 位置: L716-718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActiveFallbackModels()`

## getCurrentModelName()
- 位置: L720-722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCachedModelsData()`, `getCurrentModelChoiceId()`
- 参照: `getCachedModelsData()[getCurrentModelChoiceId()]?.model`

## getCurrentModelChoiceId()
- 位置: L724-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## _clearModelsDataCacheForTesting()
- 位置: L731-733
- 役割: (未記入)
- 触るとき: (未記入)

## renderPrompt()
- 位置: L742-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `finalPromptContent.replace()`

## parseAndExtractJSON()
- 位置: L761-779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `rawContent.match()`
- 条件付き依存: `if (e instanceof SyntaxError)` → `console.warn()`
- 参照: `e.message`, `response?.finalOutput`

## toIntegerId()
- 位置: L788-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.trim()`
- 条件付き依存: `if (typeof value === "number")` → `Number.isInteger()`
- 条件付き依存: `if (typeof value === "string" && value.trim() !== "")` → `Number()`
- 条件付き依存: `if (typeof value === "string" && value.trim() !== "")` → `Number.isInteger()`

## indexInferenceResultsById()
- 位置: L807-816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resultsById.has()`, `toIntegerId()`
- 条件付き依存: `if (id !== null && !resultsById.has(id))` → `resultsById.set()`
- 参照: `result?.id`

## makeJSONSchemaBlob()
- 位置: L831-840
- 役割: (未記入)
- 触るとき: (未記入)
