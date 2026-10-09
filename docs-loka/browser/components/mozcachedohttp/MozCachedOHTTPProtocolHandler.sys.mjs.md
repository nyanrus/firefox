# browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs

source: browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs
source-hash: 5f52a97f2481584469037cae4058a9a032be4b08
lines: 1138

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyServiceGetter()`

## MozCachedOHTTPProtocolHandler.allowPort()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)

## MozCachedOHTTPProtocolHandler.newChannel()
- 位置: L85-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 条件付き依存: `if ( Services.appinfo.remoteType == lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `this.#getOHTTPService()`
- 条件付き依存: `if (loadingPrincipal.isSystemPrincipal)` → `this.#getOHTTPService()`
- 条件付き依存: `if (loadingPrincipal)` → `lazy.E10SUtils.getRemoteTypeForPrincipal()`
- 条件付き依存: `if (remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE)` → `this.#getOHTTPService()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`, `Services.appinfo.remoteType`, `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `loadInfo?.loadingPrincipal`, `loadingPrincipal.isSystemPrincipal`, `this.#injectedOHTTPService`
- XPCOM: `Services.appinfo`

## MozCachedOHTTPProtocolHandler.getOHTTPGatewayConfigAndRelayURI()
- 位置: async L156-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HOST_MAP.get()`, `Services.io.newURI()`, `lazy.ObliviousHTTP.getOHTTPConfig()`
- 条件付き依存: `if ( hostMapping.gatewayConfigURL === undefined || hostMapping.relayURL === undefined )` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `hostMapping.gatewayConfigURL`, `hostMapping.gatewayConfigURLPrefName`, `hostMapping.relayURL`, `hostMapping.relayURLPrefName`
- XPCOM: `Services.io`

## MozCachedOHTTPProtocolHandler.injectOHTTPService()
- 位置: L203-205
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#injectedOHTTPService`

## MozCachedOHTTPProtocolHandler.#getOHTTPService()
- 位置: L213-215
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.obliviousHttpService`, `this.#injectedOHTTPService`

## MozCachedOHTTPChannel.constructor()
- 位置: L261-274
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#inTestingMode`, `this.#loadInfo`, `this.#ohttpService`, `this.#originalURI`, `this.#protocolHandler`, `this.#uri`

## MozCachedOHTTPChannel.URI()
- 位置: L282-284
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#uri`

## MozCachedOHTTPChannel.originalURI()
- 位置: L291-293
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#originalURI`

## MozCachedOHTTPChannel.originalURI()
- 位置: L295-297
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#originalURI`

## MozCachedOHTTPChannel.status()
- 位置: L305-307
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#status`

## MozCachedOHTTPChannel.contentType()
- 位置: L314-316
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentType`

## MozCachedOHTTPChannel.contentType()
- 位置: L318-320
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentType`

## MozCachedOHTTPChannel.contentCharset()
- 位置: L327-329
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentCharset`

## MozCachedOHTTPChannel.contentCharset()
- 位置: L331-333
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentCharset`

## MozCachedOHTTPChannel.contentLength()
- 位置: L341-343
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentLength`

## MozCachedOHTTPChannel.contentLength()
- 位置: L345-347
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentLength`

## MozCachedOHTTPChannel.loadFlags()
- 位置: L354-356
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#loadFlags`

## MozCachedOHTTPChannel.loadFlags()
- 位置: L358-360
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#loadFlags`

## MozCachedOHTTPChannel.loadInfo()
- 位置: L367-369
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#loadInfo`

## MozCachedOHTTPChannel.loadInfo()
- 位置: L371-373
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#loadInfo`

## MozCachedOHTTPChannel.owner()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#owner`

## MozCachedOHTTPChannel.owner()
- 位置: L384-386
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#owner`

## MozCachedOHTTPChannel.securityInfo()
- 位置: L394-396
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#securityInfo`

## MozCachedOHTTPChannel.notificationCallbacks()
- 位置: L403-405
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#notificationCallbacks`

## MozCachedOHTTPChannel.notificationCallbacks()
- 位置: L407-409
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#notificationCallbacks`

## MozCachedOHTTPChannel.loadGroup()
- 位置: L416-418
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#loadGroup`

## MozCachedOHTTPChannel.loadGroup()
- 位置: L420-422
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#loadGroup`

## MozCachedOHTTPChannel.name()
- 位置: L430-432
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#uri.spec`

## MozCachedOHTTPChannel.isPending()
- 位置: L440-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pendingChannel.isPending()`
- 参照: `this.#pendingChannel`

## MozCachedOHTTPChannel.cancel()
- 位置: L450-457
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#pendingChannel)` → `this.#pendingChannel.cancel()`
- 参照: `this.#cancelled`, `this.#pendingChannel`, `this.#status`

## MozCachedOHTTPChannel.suspend()
- 位置: L462-466
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#pendingChannel)` → `this.#pendingChannel.suspend()`
- 参照: `this.#pendingChannel`

## MozCachedOHTTPChannel.resume()
- 位置: L471-475
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#pendingChannel)` → `this.#pendingChannel.resume()`
- 参照: `this.#pendingChannel`

## MozCachedOHTTPChannel.open()
- 位置: L483-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## MozCachedOHTTPChannel.asyncOpen()
- 位置: L498-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#loadResource()`, `this.#loadResource().catch()`, `this.#notifyError()`
- 条件付き依存: `if (this.#cancelled)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`, `this.#cancelled`, `this.#listener`, `this.#status`

## MozCachedOHTTPChannel.#loadResource()
- 位置: async L519-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HOST_MAP.has()`, `this.#extractHostAndResourceURI()`, `this.#loadViaOHTTP()`, `this.#tryCache()`

## MozCachedOHTTPChannel.#extractHostAndResourceURI()
- 位置: L553-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `searchParams.get()`
- 参照: `resourceURL.protocol`, `this.#uri.spec`, `url.host`, `url.search`
- XPCOM: `Services.io`

## MozCachedOHTTPChannel.#tryCache()
- 位置: async L585-616
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT )` → `ChromeUtils.getAllDOMProcesses()`
- 条件付き依存: `if ( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT )` → `parentProcess.getActor()`
- 条件付き依存: `if ( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT )` → `parentActor.tryCache()`
- 条件付き依存: `if (!( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT ))` → `ChromeUtils.domProcessChild.getActor()`
- 条件付き依存: `if (!( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT ))` → `childActor.sendQuery()`
- 条件付き依存: `if (result.success)` → `this.#createInputStreamPump()`
- 条件付き依存: `if (result.success)` → `this.#applyContentHeaders()`
- 条件付き依存: `if (result.success)` → `this.#streamFromCache()`
- 参照: `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`, `resourceURI.spec`, `result.headersObj`, `result.inputStream`, `result.success`
- XPCOM: `Services.appinfo`

## MozCachedOHTTPChannel.#applyContentHeaders()
- 位置: L626-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `headers.get()`
- 条件付き依存: `if (contentTypeHeader)` → `Services.io.parseResponseContentType()`
- 参照: `charSet.value`, `hadCharSet.value`, `this.#contentCharset`, `this.#contentType`
- XPCOM: `Services.io`

## MozCachedOHTTPChannel.#createInputStreamPump()
- 位置: L651-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/input-stream-pump;1"].createInstance()`, `pump.init()`
- 参照: `Ci.nsIInputStreamPump`
- XPCOM: [`nsIInputStreamPump`](../../../netwerk/base/nsIInputStreamPump.idl.md) / `@mozilla.org/network/input-stream-pump;1`

## MozCachedOHTTPChannel.#streamFromCache()
- 位置: L669-684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pump.asyncRead()`, `reject()`, `this.#createCacheStreamListener()`, `this.#safeCloseStream()`

## MozCachedOHTTPChannel.#createCacheStreamListener()
- 位置: L698-718
- 役割: (未記入)
- 触るとき: (未記入)

## onStartRequest()
- 位置: L700-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listener.onStartRequest()`
- 参照: `this.#pendingChannel`, `this.#startedRequest`

## onDataAvailable()
- 位置: L706-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listener.onDataAvailable()`

## onStopRequest()
- 位置: L710-716
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `resolve()`, `this.#listener.onStopRequest()`, `this.#safeCloseStream()`
- 参照: `this.#pendingChannel`

## MozCachedOHTTPChannel.#safeCloseStream()
- 位置: L726-732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `stream.close()`

## MozCachedOHTTPChannel.#loadViaOHTTP()
- 位置: async L744-755
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#createOHTTPChannel()`, `this.#executeOHTTPRequest()`, `this.#protocolHandler.getOHTTPGatewayConfigAndRelayURI()`

## MozCachedOHTTPChannel.#createOHTTPChannel()
- 位置: L769-807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.releaseAssert()`, `lazy.NetUtil.newChannel()`, `this.#ohttpService.newChannel()`
- 参照: `Ci.nsIContentPolicy.TYPE_OTHER`, `Ci.nsIRequest.LOAD_ANONYMOUS`, `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`, `Services.appinfo.remoteType`, `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `ohttpChannel.loadFlags`, `ohttpChannel.loadGroup`, `ohttpChannel.loadInfo`, `ohttpChannel.notificationCallbacks`, `this.#loadFlags`, `this.#loadGroup`, `this.#notificationCallbacks`
- XPCOM: [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIRequest`](../../../docshell/base/nsIDocShell.idl.md) / `Services.appinfo`

## MozCachedOHTTPChannel.#executeOHTTPRequest()
- 位置: L817-880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/pipe;1"].createInstance()`, `cachePipe.init()`, `ohttpChannel.asyncOpen()`, `reject()`, `this.#cleanupCacheOnError()`, `this.#createOHTTPResponseListener()`, `this.#setupStreamTee()`
- 条件付き依存: `if ( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT )` → `ChromeUtils.getAllDOMProcesses()`
- 条件付き依存: `if ( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT )` → `parentProcess.getActor()`
- 条件付き依存: `if ( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT )` → `parentActor.writeCache()`
- 条件付き依存: `if (!( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT ))` → `ChromeUtils.domProcessChild.getActor()`
- 条件付き依存: `if (!( Services.appinfo.processType === Services.appinfo.PROCESS_TYPE_DEFAULT ))` → `childActor.sendAsyncMessage()`
- 参照: `Ci.nsIPipe`, `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`, `cachePipe.inputStream`, `cachePipe.outputStream`, `cacheStreamUpdate.port1`, `cacheStreamUpdate.port2`, `ohttpChannel.URI`, `ohttpChannel.URI.spec`, `this.#pendingChannel`
- XPCOM: [`nsIPipe`](../../../xpcom/io/nsIPipe.idl.md) / `@mozilla.org/pipe;1` / `Services.appinfo`

## MozCachedOHTTPChannel.#createOHTTPResponseListener()
- 位置: L898-946
- 役割: (未記入)
- 触るとき: (未記入)

## onStartRequest()
- 位置: L905-924
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listener.onStartRequest()`, `this.#processCacheControl()`, `this.#processResponseHeaders()`
- 条件付き依存: `if (request instanceof Ci.nsIHttpChannel)` → `request.getResponseHeader()`
- 条件付き依存: `if (contentType)` → `headers.set()`
- 条件付き依存: `if (contentType)` → `this.#applyContentHeaders()`
- 参照: `Ci.nsIHttpChannel`, `this.#startedRequest`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## onDataAvailable()
- 位置: L926-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listener.onDataAvailable()`

## onStopRequest()
- 位置: L930-944
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `this.#finalizeCacheEntry()`, `this.#listener.onStopRequest()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `resolve()`
- 条件付き依存: `if (!(Components.isSuccessCode(status)))` → `reject()`
- 参照: `this.#pendingChannel`

## MozCachedOHTTPChannel.#setupStreamTee()
- 位置: L958-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/network/stream-listener-tee;1" ].createInstance()`, `console.warn()`, `tee.init()`, `this.#safeCloseStream()`
- 参照: `Ci.nsIStreamListenerTee`
- XPCOM: [`nsIStreamListenerTee`](../../../netwerk/base/nsIStreamListenerTee.idl.md) / `@mozilla.org/network/stream-listener-tee;1`

## MozCachedOHTTPChannel.#finalizeCacheEntry()
- 位置: L990-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `console.warn()`
- 条件付き依存: `if (cacheOutputStream)` → `cacheOutputStream.closeWithStatus()`
- 条件付き依存: `if (!Components.isSuccessCode(status))` → `cacheStreamUpdatePort.postMessage()`
- 参照: `Cr.NS_BASE_STREAM_CLOSED`

## MozCachedOHTTPChannel.#cleanupCacheOnError()
- 位置: L1012-1021
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cacheStreamUpdatePort.postMessage()`
- 条件付き依存: `if (cacheOutputStream)` → `cacheOutputStream.closeWithStatus()`
- 参照: `Cr.NS_BASE_STREAM_CLOSED`

## MozCachedOHTTPChannel.#notifyError()
- 位置: L1029-1039
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#startedRequest)` → `this.#listener.onStartRequest()`
- 条件付き依存: `if (this.#listener)` → `this.#listener.onStopRequest()`
- 参照: `this.#listener`, `this.#startedRequest`, `this.#status`

## MozCachedOHTTPChannel.#processResponseHeaders()
- 位置: L1049-1072
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cacheStreamUpdatePort.postMessage()`, `httpChannel.visitResponseHeaders()`
- 参照: `Ci.nsIHttpChannel`, `httpChannel.wrappedJSObject`, `this.#inTestingMode`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## MozCachedOHTTPChannel.visitHeader()
- 位置: L1063-1065
- 役割: (未記入)
- 触るとき: (未記入)

## MozCachedOHTTPChannel.#processCacheControl()
- 位置: L1083-1134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `cacheStreamUpdatePort.postMessage()`, `httpChannel.getResponseHeader()`
- 条件付き依存: `if (cacheControl)` → `Services.io.parseCacheControlHeader()`
- 条件付き依存: `if (cacheControlParseResult.maxAge)` → `Date.now()`
- 条件付き依存: `if ( cacheControlParseResult.noCache || cacheControlParseResult.noStore )` → `cacheStreamUpdatePort.postMessage()`
- 条件付き依存: `if (!expirationTime)` → `httpChannel.getResponseHeader()`
- 条件付き依存: `if (expires)` → `new Date(expires).getTime()`
- 参照: `Ci.nsIHttpChannel`, `cacheControlParseResult.maxAge`, `cacheControlParseResult.noCache`, `cacheControlParseResult.noStore`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `Services.io`
