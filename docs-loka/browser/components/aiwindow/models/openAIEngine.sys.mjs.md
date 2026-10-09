# browser/components/aiwindow/models/openAIEngine.sys.mjs

source: browser/components/aiwindow/models/openAIEngine.sys.mjs
source-hash: ae91b41e84d3292d5516a6880a99c30527f61aad
lines: 510

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## openAIEngine.hasCustomEndpoint()
- 位置: L104-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## openAIEngine.isCustomEndpoint()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `openAIEngine.endpoint`, `this.#baseURL`

## openAIEngine.usesCustomEndpoint()
- 位置: L128-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 参照: `openAIEngine.endpoint`
- XPCOM: `Services.prefs`

## openAIEngine.resolveEndpointConfig()
- 位置: L142-154
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (modelChoiceId === CUSTOM_MODEL_CHOICE_ID)` → `Services.prefs.getStringPref()`
- 参照: `openAIEngine.endpoint`
- XPCOM: `Services.prefs`

## openAIEngine.build()
- 位置: async L169-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openAIEngine.#createOpenAIEngine()`
- 参照: `engine.#apiKey`, `engine.#baseURL`, `engine.#engineId`, `engine.#flowId`, `engine.#purpose`, `engine.#serviceType`, `engine.engineInstance`, `engine.feature`, `engine.model`, `openAIEngine.endpoint`

## openAIEngine.getFxAccountToken()
- 位置: async L206-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `fxAccounts.getOAuthToken()`, `lazy.getFxAccountsSingleton()`

## openAIEngine.is429Error()
- 位置: L226-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `error.message?.includes()`
- 参照: `error.status`

## openAIEngine.isRetryableError()
- 位置: L241-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/NS_ERROR_(NET_|CONNECTION|PROXY)|NetworkError|connection (refused|reset)|timed? ?out/i.test()`, `Number()`, `error.message?.match()`, `isRetryableStatus()`, `this.is429Error()`
- 参照: `error.message`, `error.name`, `error.status`

## isRetryableStatus()
- 位置: L248-249
- 役割: (未記入)
- 触るとき: (未記入)

## openAIEngine.#createOpenAIEngine()
- 位置: async L280-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.clearUserPref()`, `Services.prefs.getStringPref()`, `console.error()`, `openAIEngine._createEngine()`
- XPCOM: `Services.prefs`

## openAIEngine.run()
- 位置: async L331-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._runWithAuth()`

## openAIEngine._runWithAuth()
- 位置: async L341-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `lazy.getFxAccountsSingleton()`, `openAIEngine.getFxAccountToken()`, `this._is401Error()`, `this._recreateEngine()`, `this.engineInstance.run()`
- 条件付き依存: `if (oldToken)` → `fxAccounts.removeCachedOAuthToken()`
- 条件付き依存: `if (newToken)` → `fxAccounts.removeCachedOAuthToken()`
- 参照: `content.fxAccountToken`, `this.isCustomEndpoint`

## openAIEngine._recreateEngine()
- 位置: async L392-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openAIEngine.#createOpenAIEngine()`
- 条件付き依存: `if (!this.#engineId || !this.#serviceType)` → `console.warn()`
- 参照: `this.#apiKey`, `this.#baseURL`, `this.#engineId`, `this.#flowId`, `this.#purpose`, `this.#serviceType`, `this.engineInstance`, `this.feature`, `this.model`

## openAIEngine._is401Error()
- 位置: L417-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `error.message?.includes()`
- 参照: `error.status`

## openAIEngine._runWithGeneratorAuth()
- 位置: async L431-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `lazy.getFxAccountsSingleton()`, `openAIEngine.getFxAccountToken()`, `this._is401Error()`, `this._recreateEngine()`, `this.engineInstance.runWithGenerator()`
- 条件付き依存: `if (oldToken)` → `fxAccounts.removeCachedOAuthToken()`
- 条件付き依存: `if (newToken)` → `fxAccounts.removeCachedOAuthToken()`
- 参照: `options.fxAccountToken`, `signal?.aborted`, `this.isCustomEndpoint`

## openAIEngine.runWithGenerator()
- 位置: L497-499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._runWithGeneratorAuth()`
