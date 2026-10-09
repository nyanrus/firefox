# browser/components/newtab/AboutNewTabRedirector.sys.mjs

source: browser/components/newtab/AboutNewTabRedirector.sys.mjs
source-hash: 33ebe5111a15dcfba5c446efd1292cce4b29af34
lines: 644

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## init()
- 位置: L106-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.addMessageListener()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `this.setState()`
- 参照: `this.CACHE_REQUEST_MESSAGE`, `this.STATES.UNCONSUMED`, `this._initted`, `this._pageInputStream`, `this._scriptInputStream`
- XPCOM: `Services.cpmm` / `Services.obs` / `Services.prefs`

## uninit()
- 位置: L143-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.removeMessageListener()`, `Services.obs.removeObserver()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this._cacheWorker)` → `this._cacheWorker.terminate()`
- 参照: `this.CACHE_REQUEST_MESSAGE`, `this.STATES.UNAVAILABLE`, `this._cacheWorker`, `this._consumerBCID`, `this._initted`, `this._pageInputStream`, `this._scriptInputStream`, `this._state`
- XPCOM: `Services.cpmm` / `Services.obs` / `Services.prefs`

## maybeGetCachedPageChannel()
- 位置: L189-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/network/input-stream-channel;1" ].createInstance()`, `channel.QueryInterface()`, `channel.setURI()`
- 条件付き依存: `if (requestType === this.REQUEST_TYPE.PAGE)` → `this._scriptInputStream.available()`
- 条件付き依存: `if (requestType === this.REQUEST_TYPE.PAGE)` → `this._pageInputStream.available()`
- 条件付き依存: `if ( !this._scriptInputStream.available() || !this._pageInputStream.available() )` → `this.setState()`
- 条件付き依存: `if ( !this._scriptInputStream.available() || !this._pageInputStream.available() )` → `this.reportUsageResult()`
- 条件付き依存: `if (requestType === this.REQUEST_TYPE.PAGE)` → `this.setState()`
- 条件付き依存: `if (e.result === Cr.NS_BASE_STREAM_CLOSED)` → `this.reportUsageResult()`
- 条件付き依存: `if ( requestType === this.REQUEST_TYPE.SCRIPT && this._consumerBCID !== loadInfo.browsingContextID )` → `this.setState()`
- 条件付き依存: `if (requestType === this.REQUEST_TYPE.SCRIPT)` → `this.setState()`
- 条件付き依存: `if (requestType === this.REQUEST_TYPE.SCRIPT)` → `this.reportUsageResult()`
- 条件付き依存: `if (!(requestType === this.REQUEST_TYPE.SCRIPT))` → `this.setState()`
- 参照: `Ci.nsIChannel`, `Ci.nsIInputStreamChannel`, `Cr.NS_BASE_STREAM_CLOSED`, `channel.contentStream`, `channel.loadInfo`, `e.result`, `loadInfo.browsingContextID`, `this.REQUEST_TYPE.PAGE`, `this.REQUEST_TYPE.SCRIPT`, `this.REQUEST_TYPE_SCRIPT`, `this.STATES.FAILED`, `this.STATES.PAGE_AND_SCRIPT_CONSUMED`, `this.STATES.PAGE_CONSUMED`, `this.STATES.UNCONSUMED`, `this._consumerBCID`, `this._initted`, `this._pageInputStream`, `this._scriptInputStream`, `this._state`, `uri.query`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIInputStreamChannel`](../../../netwerk/base/nsIInputStreamChannel.idl.md) / `@mozilla.org/network/input-stream-channel;1`

## constructAndSendCache()
- 位置: async L292-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/io/string-input-stream;1" ].createInstance()`, `Glean.newtab.abouthomeCacheConstruction.start()`, `Glean.newtab.abouthomeCacheConstruction.stopAndAccumulate()`, `Services.cpmm.sendAsyncMessage()`, `pageInputStream.setUTF8Data()`, `scriptInputStream.setUTF8Data()`, `this.getOrCreateWorker()`, `worker .post()`, `worker .post("construct", [state, direction]) .finally()`
- 参照: `Ci.nsIStringInputStream`, `Services.locale.isAppLocaleRTL`, `this.CACHE_RESPONSE_MESSAGE`
- XPCOM: [`nsIStringInputStream`](../../../xpcom/io/nsIStringStream.idl.md) / `@mozilla.org/io/string-input-stream;1` / `Services.cpmm` / `Services.locale`

## getOrCreateWorker()
- 位置: L327-334
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BasePromiseWorker`, `this._cacheWorker`

## receiveMessage()
- 位置: L336-341
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name === this.CACHE_REQUEST_MESSAGE)` → `this.constructAndSendCache()`
- 参照: `message.data`, `message.name`, `this.CACHE_REQUEST_MESSAGE`

## reportUsageResult()
- 位置: L343-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.sendAsyncMessage()`
- 参照: `this.CACHE_USAGE_RESULT_MESSAGE`
- XPCOM: `Services.cpmm`

## observe()
- 位置: L349-354
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "memory-pressure" && this._cacheWorker)` → `this._cacheWorker.terminate()`
- 参照: `this._cacheWorker`

## setState()
- 位置: L363-373
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(state > this._state))` → `console.error()`
- 参照: `new Error().stack`, `this._state`

## disqualifyCache()
- 位置: L381-386
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._state === this.STATES.UNCONSUMED)` → `this.setState()`
- 条件付き依存: `if (this._state === this.STATES.UNCONSUMED)` → `this.reportUsageResult()`
- 参照: `this.STATES.DISQUALIFIED`, `this.STATES.UNCONSUMED`, `this._state`

## BaseAboutNewTabRedirector.constructor()
- 位置: L394-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (!AppConstants.RELEASE_OR_BETA)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `AppConstants.RELEASE_OR_BETA`, `this.activityStreamDebug`

## BaseAboutNewTabRedirector.defaultURL()
- 位置: L427-443
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.activityStreamDebug`, `this.remoteRendererEnabled`, `this.selfLoadingEnabled`

## BaseAboutNewTabRedirector.newChannel()
- 位置: L445-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## BaseAboutNewTabRedirector.getURIFlags()
- 位置: L452-460
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIAboutModule.ALLOW_SCRIPT`, `Ci.nsIAboutModule.ENABLE_INDEXED_DB`, `Ci.nsIAboutModule.URI_CAN_LOAD_IN_PRIVILEGEDABOUT_PROCESS`, `Ci.nsIAboutModule.URI_MUST_LOAD_IN_CHILD`, `Ci.nsIAboutModule.URI_SAFE_FOR_UNTRUSTED_CONTENT`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md)

## BaseAboutNewTabRedirector.getChromeURI()
- 位置: L462-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- XPCOM: `Services.io`

## AboutNewTabRedirectorParent.constructor()
- 位置: L480-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.registerWindowActor()`, `Promise.withResolvers()`, `super()`
- 参照: `this.#addonInitializedPromise`, `this.#addonInitializedResolver`, `this.wrappedJSObject`

## AboutNewTabRedirectorParent.notifyBuiltInAddonInitialized()
- 位置: L520-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suspendedChannel.resume()`, `this.#addonInitializedResolver()`
- 参照: `this.#addonInitialized`, `this.#suspendedChannels`

## AboutNewTabRedirectorParent.promiseBuiltInAddonInitialized()
- 位置: L536-538
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#addonInitializedPromise`

## AboutNewTabRedirectorParent.newChannel()
- 位置: L540-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newChannelFromURIWithLoadInfo()`, `this.getChromeURI()`, `uri.spec.startsWith()`
- 条件付き依存: `if ( uri.spec.startsWith("about:home") || (uri.spec.startsWith("about:newtab") && lazy.BUILTIN_NEWTAB_ENABLED) )` → `Services.io.newURI()`
- 条件付き依存: `if (!this.#addonInitialized)` → `this.#getSuspendedChannel()`
- 参照: `lazy.BUILTIN_NEWTAB_ENABLED`, `resultChannel.originalURI`, `this.#addonInitialized`, `this.defaultURL`
- XPCOM: `Services.io`

## AboutNewTabRedirectorParent.#getSuspendedChannel()
- 位置: L572-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newSuspendableChannelWrapper()`, `suspendedChannel.suspend()`, `this.#suspendedChannels.push()`
- XPCOM: `Services.io`

## AboutNewTabRedirectorChild.newChannel()
- 位置: L588-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newChannelFromURIWithLoadInfo()`, `uri.spec.startsWith()`
- 条件付き依存: `if (!IS_PRIVILEGED_PROCESS)` → `Components.Exception()`
- 条件付き依存: `if (uri.spec.startsWith("about:home"))` → `AboutHomeStartupCacheChild.maybeGetCachedPageChannel()`
- 条件付き依存: `if (uri.spec.startsWith("about:home"))` → `Services.io.newURI()`
- 条件付き依存: `if (!(uri.spec.startsWith("about:home")))` → `AboutHomeStartupCacheChild.disqualifyCache()`
- 条件付き依存: `if (lazy.BUILTIN_NEWTAB_ENABLED)` → `Services.io.newURI()`
- 条件付き依存: `if (!(lazy.BUILTIN_NEWTAB_ENABLED))` → `this.getChromeURI()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `lazy.BUILTIN_NEWTAB_ENABLED`, `resultChannel.originalURI`, `this.defaultURL`
- XPCOM: `Services.io`

## AboutNewTabRedirectorStub()
- 位置: L638-643
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`
- XPCOM: `Services.appinfo`
