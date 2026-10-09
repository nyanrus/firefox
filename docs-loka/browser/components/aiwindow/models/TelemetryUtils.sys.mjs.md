# browser/components/aiwindow/models/TelemetryUtils.sys.mjs

source: browser/components/aiwindow/models/TelemetryUtils.sys.mjs
source-hash: 3382b87e7872f439f566ebdd5dea49251816f032
lines: 529

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `XPCOMUtils.declareLazy()`, `console.createInstance()`

## uniform_sample()
- 位置: L42-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.currentTurnIndex()`

## uniform_sample_at_turn()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.currentTurnIndex()`
- 参照: `conversation._telemetryUniformSample`

## min_turns()
- 位置: L47-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.currentTurnIndex()`

## Trigger.constructor()
- 位置: L76-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.check`, `this.description`, `this.name`, `this.samplingProbability`

## TelemetryPromptEngine.build()
- 位置: async L108-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `lazy.console.error()`, `lazy.openAIEngine._createEngine()`
- 参照: `engine.#engineInstance`, `engine.#promptRecord`, `lazy.openAIEngine.endpoint`, `promptRecord.model`, `promptRecord.purpose`, `promptRecord.service_type`
- XPCOM: `Services.prefs`

## TelemetryPromptEngine.verifyResult()
- 位置: L144-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.fromEntries()`, `Object.keys()`, `Object.keys(schema).map()`, `schema[key]?.includes()`
- 参照: `result.finalOutput`, `this.#promptRecord.output_schema`

## TelemetryPromptEngine.run()
- 位置: async L172-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.keys()`, `conversation.getMessagesInChatCompletionsFormat()`, `lazy.console.debug()`, `lazy.openAIEngine.getFxAccountToken()`, `renderPrompt()`, `this.#engineInstance.run()`, `this.verifyResult()`
- 参照: `this.#promptRecord.output_schema`, `this.#promptRecord.prompt`

## TelemetryEngine._fetchRecords()
- 位置: async L212-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.get()`, `lazy.RemoteSettings()`, `lazy.console.error()`

## TelemetryEngine.getTriggerDefinitions()
- 位置: async L223-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TRIGGER_CHECK_STRATEGIES[def.check]()`, `checkMajorVersion()`, `this._fetchRecords()`, `triggerRecords .filter()`, `triggerRecords .filter(def => TRIGGER_CHECK_STRATEGIES[def.check]) .filter()`
- 参照: `def.check`, `def.description`, `def.name`, `def.params`, `def.sampling_probability`, `def.version`, `this._triggers`

## TelemetryEngine._getRandom()
- 位置: L252-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`

## TelemetryEngine.getTriggers()
- 位置: async L256-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation._checkedTelemetryTriggers.has()`, `conversation.currentTurnIndex()`, `lazy.console.debug()`, `this.getTriggerDefinitions()`, `trigger.check()`
- 条件付き依存: `if (conversation._checkedTelemetryTriggers.has(trigger.name))` → `lazy.console.debug()`
- 条件付き依存: `if (trigger.check(conversation))` → `conversation._checkedTelemetryTriggers.add()`
- 条件付き依存: `if (trigger.check(conversation))` → `this._getRandom()`
- 条件付き依存: `if (this._getRandom() < trigger.samplingProbability)` → `lazy.console.debug()`
- 条件付き依存: `if (this._getRandom() < trigger.samplingProbability)` → `fired.push()`
- 参照: `conversation._checkedTelemetryTriggers`, `conversation._telemetryUniformProbability`, `conversation._telemetryUniformSample`, `this._triggers`, `trigger.name`, `trigger.samplingProbability`

## TelemetryEngine.runTelemetry()
- 位置: async L305-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkMajorVersion()`, `results.map()`, `samplingProbabilities.get()`, `seen.has()`, `this._fetchRecords()`, `this._runPrompts()`, `triggers.map()`
- 条件付き依存: `if ( !seen.has(record.telemetry_name) && // sometimes multiple triggers will use the same telemetry checkMajorVersion( record.version, TELEMETRY_MAJOR_VERSIONS[r...)` → `recordTriggers.find()`
- 条件付き依存: `if ( !seen.has(record.telemetry_name) && // sometimes multiple triggers will use the same telemetry checkMajorVersion( record.version, TELEMETRY_MAJOR_VERSIONS[r...)` → `triggerByName.has()`
- 条件付き依存: `if (matchingTriggerName)` → `seen.add()`
- 条件付き依存: `if (matchingTriggerName)` → `promptsToRun.push()`
- 条件付き依存: `if (matchingTriggerName)` → `samplingProbabilities.set()`
- 条件付き依存: `if (matchingTriggerName)` → `triggerByName.get()`
- 参照: `r.telemetry_name`, `record.telemetry_name`, `record.triggers`, `record.version`, `t.name`, `triggerByName.get(matchingTriggerName).samplingProbability`, `triggers.length`

## TelemetryEngine.runTelemetryByName()
- 位置: async L355-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allRecords .filter()`, `allRecords .filter(record => nameSet.has(record.telemetry_name)) .filter()`, `checkMajorVersion()`, `nameSet.has()`, `this._fetchRecords()`, `this._runPrompts()`
- 参照: `promptNames.length`, `record.run_terminal`, `record.telemetry_name`, `record.version`

## TelemetryEngine._runPrompts()
- 位置: async L378-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TelemetryPromptEngine.build()`, `engine.run()`, `lazy.console.debug()`, `lazy.openAIEngine.is429Error()`, `results.push()`
- 条件付き依存: `if (attempt > 0)` → `lazy.setTimeout()`
- 条件付き依存: `if (attempt > 0)` → `Math.random()`
- 条件付き依存: `if (!(lazy.openAIEngine.is429Error(error)))` → `lazy.console.error()`
- 条件付き依存: `if (lastError)` → `lazy.console.error()`
- 参照: `record.telemetry_name`, `record.version`

## normalizeMetadata()
- 位置: L422-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.stringify()`, `Math.round()`

## submitTelemetryResult()
- 位置: L446-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(metadata.triggers ?? []).includes()`, `(metadata.triggers ?? []).some()`, `Glean.smartWindow.llmajBasedTelemetry.record()`, `Object.entries()`, `String()`, `conversation.currentTurnIndex()`, `normalizeMetadata()`
- 参照: `conversation.id`, `metadata.triggers`, `resultObject?.result`, `resultObject?.samplingProbability`, `resultObject?.telemetry_name`, `resultObject?.telemetry_version`

## runLLMaJTelemetry()
- 位置: async L486-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Object.fromEntries()`, `console.error()`, `conversation.currentTurnIndex()`, `lazy.ChatStore.markLLMTelemetryUnprocessed()`, `lazy.ChatStore.markLLMTelemetryUnprocessed(conversation.id).catch()`, `lazy.ChatStore.updateLLMTelemetryRecord()`, `results.map()`, `submitTelemetryResult()`, `telemetryEngine .runTelemetry()`, `telemetryEngine .runTelemetry(triggers, conversation) .then()`, `telemetryEngine.getTriggers()`, `triggers.map()`
- 参照: `conversation._telemetryUniformProbability`, `conversation.engine?.model`, `conversation.id`, `conversation.systemPromptVersion`, `r.samplingProbability`, `r.telemetry_name`, `results.length`, `t.name`
