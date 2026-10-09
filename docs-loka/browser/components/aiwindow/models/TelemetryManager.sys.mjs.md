# browser/components/aiwindow/models/TelemetryManager.sys.mjs

source: browser/components/aiwindow/models/TelemetryManager.sys.mjs
source-hash: 07e3544b9a80946fbbbf053ca9bf90f32455e02b
lines: 230

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## TelemetryScheduler.maybeInit()
- 位置: L49-55
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#instance`

## TelemetryScheduler.constructor()
- 位置: L63-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.debug()`, `this.#init()`

## TelemetryScheduler.#init()
- 位置: async L77-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (isFirstRun)` → `lazy.console.debug()`
- 条件付き依存: `if (isFirstRun)` → `this.#onInterval()`
- 条件付き依存: `if (!(isFirstRun))` → `this.#startInterval()`
- XPCOM: `Services.prefs`

## TelemetryScheduler.#startInterval()
- 位置: L96-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setInterval()`
- 参照: `this.#intervalHandle`, `this.#onInterval`

## TelemetryScheduler.#stopInterval()
- 位置: L111-116
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#intervalHandle)` → `lazy.clearInterval()`
- 参照: `this.#intervalHandle`

## TelemetryScheduler.#onInterval()
- 位置: async L123-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await telemetryEngine.runTelemetryByName( telemetryNames, conversation ) ).map()`, `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Date.now()`, `Math.floor()`, `Math.max()`, `Math.random()`, `Object.keys()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `conversation.currentTurnIndex()`, `lazy.ChatStore.findConversationById()`, `lazy.ChatStore.getConversationsForTelemetry()`, `lazy.ChatStore.markLLMTelemetryProcessed()`, `lazy.console.debug()`, `lazy.console.error()`, `lazy.setTimeout()`, `lazy.submitTelemetryResult()`, `telemetryEngine.runTelemetryByName()`, `this.#stopInterval()`
- 条件付き依存: `if (this.#destroyed)` → `lazy.console.warn()`
- 条件付き依存: `if (this.#running)` → `lazy.console.debug()`
- 条件付き依存: `if (!this.#destroyed)` → `this.#startInterval()`
- 参照: `conversationObj.convId`, `conversationObj.modelId`, `conversationObj.telemetryJobs`, `conversationObj.telemetryProbs`, `conversationObj.uniformSamplingProbability`, `conversationsToRun.length`, `lazy.TelemetryEngine`, `r.telemetry_name`, `this.#destroyed`, `this.#running`
- XPCOM: `Services.prefs`

## TelemetryScheduler.destroy()
- 位置: L223-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.debug()`, `this.#stopInterval()`
- 参照: `TelemetryScheduler.#instance`, `this.#destroyed`
