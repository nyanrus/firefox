# browser/extensions/newtab/lib/AdsClient.sys.mjs

source: browser/extensions/newtab/lib/AdsClient.sys.mjs
source-hash: fad75b152e4fb9ca1b533a3164b9e2da5fda0e4b
lines: 298

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## _AdsClient.hasShutdown()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#hasShutdown`

## _AdsClient.isEnabled()
- 位置: L76-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `prefValues?.trainhopConfig?.adsClient?.enabled`

## _AdsClient.getBlocks()
- 位置: L88-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(prefValues[PREF_BLOCKED_LIST] ?? "") .split()`, `(prefValues[PREF_BLOCKED_LIST] ?? "") .split(",") .concat()`, `(prefValues[PREF_BLOCKED_LIST] ?? "") .split(",") .concat(additionalBlocks) .map()`, `(prefValues[PREF_BLOCKED_LIST] ?? "") .split(",") .concat(additionalBlocks) .map(block => block.trim()) .filter()`, `Array.from()`, `Boolean()`, `block.trim()`

## _AdsClient.getClient()
- 位置: L105-110
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#client === undefined)` → `this.#build()`
- 参照: `this.#client`

## _AdsClient.cacheConfig()
- 位置: L119-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `PathUtils.localProfileDir`, `lazy.MozAdsCacheConfig`

## _AdsClient.requestOptions()
- 位置: L133-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `this.#configureOhttp()`, `this.getBlocks()`
- 参照: `lazy.MozAdsRequestOptions`, `prefValues?.adsBackendConfig`

## _AdsClient.callbackOptions()
- 位置: L147-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#configureOhttp()`
- 参照: `lazy.MozAdsCallbackOptions`

## _AdsClient.#configureOhttp()
- 位置: L158-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `console.error()`, `lazy.configureOhttpChannel()`
- 参照: `lazy.OhttpConfig`, `new URL(configUrl).host`
- XPCOM: `Services.prefs`

## _AdsClient.buildTelemetry()
- 位置: L197-236
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Glean.adsClient`, `lazy.MozAdsTelemetry`

## GleanTelemetry.recordBuildCacheError()
- 位置: L199-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.set()`, `this.#record()`

## GleanTelemetry.recordClientError()
- 位置: L202-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.set()`, `this.#record()`

## GleanTelemetry.recordClientOperationTotal()
- 位置: L205-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.add()`, `this.#record()`

## GleanTelemetry.recordDeserializationError()
- 位置: L208-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.set()`, `this.#record()`

## GleanTelemetry.recordHttpCacheOutcome()
- 位置: L211-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.set()`, `this.#record()`

## GleanTelemetry.#record()
- 位置: L221-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getMetrics()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `record()`

## _AdsClient.#build()
- 位置: L238-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.AsyncShutdown.profileChangeTeardown.addBlocker()`, `lazy.MozAdsClientBuilder.init()`, `this.buildTelemetry()`, `this.uninit()`
- 参照: `lazy.AsyncShutdown.profileChangeTeardown.isClosed`, `lazy.MozAdsEnvironment.PROD`, `lazy.MozAdsEnvironment.Prod`, `this.cacheConfig`

## _AdsClient.uninit()
- 位置: async L286-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.info()`
- 条件付き依存: `if (client)` → `client.shutdown()`
- 条件付き依存: `if (this.#client)` → `this.#client.shutdown()`
- 参照: `this.#client`, `this.#hasShutdown`
