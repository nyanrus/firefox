# browser/modules/ContextId.sys.mjs

source: browser/modules/ContextId.sys.mjs
source-hash: 6165af7407f293b552e9ee680f0ccc36e438bdf6
lines: 264

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## JsContextIdCallback.constructor()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.dispatchEvent`

## JsContextIdCallback.persist()
- 位置: L60-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setCharPref()`, `Services.prefs.setIntPref()`, `this.dispatchEvent()`
- XPCOM: `Services.prefs`

## JsContextIdCallback.rotated()
- 位置: L66-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContextId.sendMARSDeletionRequest()`, `Glean.contextualServices.contextId.set()`, `GleanPings.contextIdDeletionRequest.setEnabled()`, `GleanPings.contextIdDeletionRequest.submit()`

## _ContextId.constructor()
- 位置: L85-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `super()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `ContextIdComponent.init()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `this.dispatchEvent.bind()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `Services.obs.addObserver()`
- 参照: `lazy.CURRENT_CONTEXT_ID`, `this.#comp`, `this.#observer`, `this.#rotationDays`, `this.#rustComponentEnabled`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#observer()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observe()`

## _ContextId.observe()
- 位置: L130-136
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == SHUTDOWN_TOPIC)` → `this.#comp.unsetCallback()`
- 条件付き依存: `if (topic == SHUTDOWN_TOPIC)` → `Services.obs.removeObserver()`
- 参照: `this.#observer`
- XPCOM: `Services.obs`

## _ContextId.request()
- 位置: async L148-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `this.#comp.request()`
- 条件付き依存: `if (!lazy.CURRENT_CONTEXT_ID)` → `Services.uuid.generateUUID().toString()`
- 条件付き依存: `if (!lazy.CURRENT_CONTEXT_ID)` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (!lazy.CURRENT_CONTEXT_ID)` → `Services.prefs.setStringPref()`
- 参照: `lazy.CURRENT_CONTEXT_ID`, `this.#rotationDays`, `this.#rustComponentEnabled`
- XPCOM: `Services.prefs` / `Services.uuid`

## _ContextId.forceRotation()
- 位置: async L170-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `this.#comp.forceRotation()`
- 参照: `this.#rustComponentEnabled`

## _ContextId.rotationEnabled()
- 位置: L182-184
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#rotationDays`, `this.#rustComponentEnabled`

## _ContextId.requestSynchronously()
- 位置: L192-200
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.CURRENT_CONTEXT_ID`, `this.rotationEnabled`

## _ContextId.sendMARSDeletionRequest()
- 位置: async L212-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `headers.append()`, `lazy.ObliviousHTTP.getOHTTPConfig()`, `lazy.ObliviousHTTP.ohttpRequest()`
- 条件付き依存: `if (!config)` → `console.error()`
- 条件付き依存: `if (!response.ok)` → `console.error()`
- 参照: `lazy.OHTTP_CONFIG_URL`, `lazy.OHTTP_RELAY_URL`, `lazy.UNIFIED_ADS_ENDPOINT`, `response.ok`, `response.status`
