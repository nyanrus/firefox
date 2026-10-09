# browser/modules/FaviconLoader.sys.mjs

source: browser/modules/FaviconLoader.sys.mjs
source-hash: 6f6a5b456ae4910edabe6c0fa7dacbf60c0c92c9
lines: 760

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Components.Constructor()`

## decodeImage()
- 位置: async L57-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `decoder.decode()`, `image.allocationSize()`, `image.copyTo()`
- 条件付き依存: `if ( image.displayWidth > MAX_ICON_SIZE || image.displayHeight > MAX_ICON_SIZE )` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`, `image.displayHeight`, `image.displayWidth`, `image.format`, `result.image`

## convertImage()
- 位置: async L105-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeImage()`
- 条件付き依存: `if (type == TYPE_ICO)` → `decoder.tracks[0].getSizes()`
- 条件付き依存: `if (sizes.length > 1)` → `Promise.all()`
- 条件付き依存: `if (sizes.length > 1)` → `sizes.map()`
- 条件付き依存: `if (sizes.length > 1)` → `decodeImage()`
- 参照: `decoder.tracks`, `decoder.tracks.ready`, `sizes.length`

## FaviconLoad.constructor()
- 位置: L143-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newChannelFromURI()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this.channel instanceof Ci.nsIHttpChannel)` → `this.channel.QueryInterface()`
- 条件付き依存: `if (this.channel instanceof Ci.nsIHttpChannel)` → `Cc["@mozilla.org/referrer-info;1"].createInstance()`
- 条件付き依存: `if (iconInfo.node.nodeType == iconInfo.node.DOCUMENT_NODE)` → `referrerInfo.initWithDocument()`
- 条件付き依存: `if (!(iconInfo.node.nodeType == iconInfo.node.DOCUMENT_NODE))` → `referrerInfo.initWithElement()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("network.http.tailing.enabled", true) && this.channel instanceof Ci.nsIClassOfService )` → `this.channel.addClassFlags()`
- 参照: `Ci.nsIClassOfService`, `Ci.nsIClassOfService.Tail`, `Ci.nsIClassOfService.Throttleable`, `Ci.nsIContentPolicy.TYPE_INTERNAL_IMAGE_FAVICON`, `Ci.nsIHttpChannel`, `Ci.nsIHttpChannelInternal`, `Ci.nsILoadInfo.SEC_ALLOW_CHROME`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_INHERITS_SEC_CONTEXT`, `Ci.nsILoadInfo.SEC_COOKIES_INCLUDE`, `Ci.nsILoadInfo.SEC_DISALLOW_SCRIPT`, `Ci.nsILoadInfo.SEC_REQUIRE_CORS_INHERITS_SEC_CONTEXT`, `Ci.nsIReferrerInfo`, `Ci.nsIRequest.LOAD_BACKGROUND`, `Ci.nsIRequest.LOAD_BYPASS_CACHE`, `Ci.nsIRequest.LOAD_FROM_CACHE`, `Ci.nsIRequest.VALIDATE_NEVER`, `iconInfo.iconUri`, `iconInfo.isForceReload`, `iconInfo.node`, `iconInfo.node.DOCUMENT_NODE`, `iconInfo.node.crossOrigin`, `iconInfo.node.documentGlobal.document.documentLoadGroup`, `iconInfo.node.nodePrincipal`, `iconInfo.node.nodeType`, `this.channel`, `this.channel.blockAuthPrompt`, `this.channel.loadFlags`, `this.channel.loadGroup`, `this.channel.notificationCallbacks`, `this.channel.referrerInfo`, `this.icon`
- XPCOM: [`nsIClassOfService`](../../netwerk/base/nsIClassOfService.idl.md) / [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md) / [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md) / [`nsIHttpChannelInternal`](../../netwerk/protocol/http/nsIHttpChannelInternal.idl.md) / [`nsILoadInfo`](../../dom/base/nsIContentPolicy.idl.md) / [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / [`nsIRequest`](../../docshell/base/nsIDocShell.idl.md) / `@mozilla.org/referrer-info;1` / `Services.io` / `Services.prefs`

## FaviconLoad.load()
- 位置: L212-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `this._deferred.promise.then()`, `this._deferred.reject()`, `this.channel.asyncOpen()`, `this.dataBuffer.getOutputStream()`
- 参照: `this._deferred`, `this._deferred.promise`, `this.dataBuffer`, `this.stream`

## cleanup()
- 位置: L216-220
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.channel`, `this.dataBuffer`, `this.stream`

## FaviconLoad.cancel()
- 位置: L240-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.channel.cancel()`
- 参照: `Cr.NS_BINDING_ABORTED`, `this.channel`

## FaviconLoad.onStartRequest()
- 位置: L248-248
- 役割: (未記入)
- 触るとき: (未記入)

## FaviconLoad.onDataAvailable()
- 位置: L250-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stream.writeFrom()`

## FaviconLoad.asyncOnChannelRedirect()
- 位置: L254-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback.onRedirectVerifyCallback()`
- 参照: `Cr.NS_OK`, `this.channel`

## FaviconLoad.onStopRequest()
- 位置: async L262-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `Date.now()`, `stream.readArrayBuffer()`, `this._deferred.reject()`, `this._deferred.resolve()`, `this.dataBuffer.newInputStream()`, `this.stream.close()`
- 条件付き依存: `if (statusCode == Cr.NS_BINDING_ABORTED)` → `this._deferred.reject()`
- 条件付き依存: `if (statusCode == Cr.NS_BINDING_ABORTED)` → `Components.Exception()`
- 条件付き依存: `if (!(statusCode == Cr.NS_BINDING_ABORTED))` → `this._deferred.reject()`
- 条件付き依存: `if (!(statusCode == Cr.NS_BINDING_ABORTED))` → `Components.Exception()`
- 条件付き依存: `if (!this.channel.requestSucceeded)` → `this._deferred.reject()`
- 条件付き依存: `if (!this.channel.requestSucceeded)` → `Components.Exception()`
- 条件付き依存: `if (!(this.icon.iconUri.filePath == "/favicon.ico"))` → `this.channel.isNoStoreResponse()`
- 条件付き依存: `if (this.channel instanceof Ci.nsICacheInfoChannel)` → `Math.min()`
- 条件付き依存: `if (type != "image/svg+xml")` → `Cc["@mozilla.org/image/loader;1"].createInstance()`
- 条件付き依存: `if (type != "image/svg+xml")` → `sniffer.getMIMETypeFromContent()`
- 条件付き依存: `if (!type)` → `Components.Exception()`
- 条件付き依存: `if (type != "image/svg+xml")` → `convertImage()`
- 条件付き依存: `if (!(type != "image/svg+xml"))` → `blobAsDataURL()`
- 参照: `Ci.nsICacheInfoChannel`, `Ci.nsIContentSniffer`, `Ci.nsIHttpChannel`, `Cr.NS_BINDING_ABORTED`, `Cr.NS_ERROR_FAILURE`, `Cr.NS_ERROR_NOT_AVAILABLE`, `buffer.byteLength`, `ex.result`, `octets.length`, `this.channel`, `this.channel.cacheTokenExpirationTime`, `this.channel.contentType`, `this.channel.requestSucceeded`, `this.channel.responseStatus`, `this.channel.responseStatusText`, `this.dataBuffer.length`, `this.icon.beforePageShow`, `this.icon.iconUri.filePath`, `this.icon.iconUri.spec`, `this.stream`
- XPCOM: [`nsICacheInfoChannel`](../../netwerk/base/nsICacheInfoChannel.idl.md) / [`nsIContentSniffer`](../../netwerk/base/nsIContentSniffer.idl.md) / [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `@mozilla.org/image/loader;1` → `imgLoader` (image/build/components.conf)

## FaviconLoad.getInterface()
- 位置: L385-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `iid.equals()`
- 参照: `Ci.nsIChannelEventSink`, `Cr.NS_ERROR_NO_INTERFACE`
- XPCOM: [`nsIChannelEventSink`](../../netwerk/base/nsIChannelEventSink.idl.md)

## extractIconSize()
- 位置: L400-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.linkIconSizesAttr.usage.accumulateSingleSample()`
- 条件付き依存: `if (aSizes.length)` → `size.toLowerCase()`
- 条件付き依存: `if (!(size.toLowerCase() == "any"))` → `re.exec()`
- 条件付き依存: `if (values && values.length > 1)` → `parseInt()`
- 条件付き依存: `if (width > 0)` → `Glean.linkIconSizesAttr.dimension.accumulateSingleSample()`
- 参照: `SIZES_TELEMETRY_ENUM.ANY`, `SIZES_TELEMETRY_ENUM.DIMENSION`, `SIZES_TELEMETRY_ENUM.INVALID`, `SIZES_TELEMETRY_ENUM.NO_SIZES`, `aSizes.length`, `values.length`

## getLinkIconURI()
- 位置: L442-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `uri.mutate()`, `uri.mutate().setUserPass()`, `uri.mutate().setUserPass("").finalize()`
- 参照: `aLink.href`, `aLink.ownerDocument`, `targetDoc.characterSet`
- XPCOM: `Services.io`

## guessType()
- 位置: L456-475
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!icon.type)` → `icon.iconUri.filePath.split(".").pop()`
- 条件付き依存: `if (!icon.type)` → `icon.iconUri.filePath.split()`
- 参照: `icon.type`

## selectIcons()
- 位置: L483-559
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!icon.isRichIcon)` → `guessType()`
- 条件付き依存: `if (!(guessType(icon) == TYPE_SVG))` → `guessType()`
- 条件付き依存: `if (!( icon.width == preferredWidth && guessType(preferredIcon) != TYPE_SVG ))` → `guessType()`
- 参照: `bestSizedIcon.width`, `icon.isRichIcon`, `icon.width`, `iconInfos.length`, `largestRichIcon.width`

## IconLoader.constructor()
- 位置: L562-564
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.actor`

## IconLoader.load()
- 位置: async L566-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TRUSTED_FAVICON_SCHEMES.includes()`, `this._loader.load()`, `this.actor.sendAsyncMessage()`
- 条件付き依存: `if (this._loader)` → `this._loader.icon.iconUri.equals()`
- 条件付き依存: `if (this._loader)` → `this._loader.cancel()`
- 条件付き依存: `if (TRUSTED_FAVICON_SCHEMES.includes(iconInfo.iconUri.scheme))` → `Services.scriptSecurityManager.checkLoadURIWithPrincipal()`
- 条件付き依存: `if (TRUSTED_FAVICON_SCHEMES.includes(iconInfo.iconUri.scheme))` → `this.actor.sendAsyncMessage()`
- 条件付き依存: `if (TRUSTED_FAVICON_SCHEMES.includes(iconInfo.iconUri.scheme))` → `iconInfo.iconUri.schemeIs()`
- 条件付き依存: `if (typeof e.data?.wrappedJSObject?.httpStatus !== "number")` → `console.error()`
- 条件付き依存: `if (e.result != Cr.NS_BINDING_ABORTED)` → `this.actor.sendAsyncMessage()`
- 参照: `Cr.NS_BINDING_ABORTED`, `Services.scriptSecurityManager.ALLOW_CHROME`, `e.data?.wrappedJSObject?.httpStatus`, `e.result`, `iconInfo.beforePageShow`, `iconInfo.iconUri`, `iconInfo.iconUri.scheme`, `iconInfo.iconUri.spec`, `iconInfo.isRichIcon`, `iconInfo.node.nodePrincipal`, `this._loader`
- XPCOM: `Services.scriptSecurityManager`

## IconLoader.cancel()
- 位置: L636-643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._loader.cancel()`
- 参照: `this._loader`

## FaviconLoader.constructor()
- 位置: L647-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadIcons()`
- 参照: `lazy.DeferredTask`, `this.actor`, `this.beforePageShow`, `this.iconInfos`, `this.iconTask`, `this.richIconLoader`, `this.tabIconLoader`

## FaviconLoader.loadIcons()
- 位置: L669-698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `selectIcons()`
- 条件付き依存: `if (isForceReload && (richIcon || tabIcon))` → `this.actor.sendAsyncMessage()`
- 条件付き依存: `if (richIcon)` → `this.richIconLoader.load(richIcon).catch()`
- 条件付き依存: `if (richIcon)` → `this.richIconLoader.load()`
- 条件付き依存: `if (tabIcon)` → `this.tabIconLoader.load(tabIcon).catch()`
- 条件付き依存: `if (tabIcon)` → `this.tabIconLoader.load()`
- 参照: `console.error`, `richIcon.isForceReload`, `tabIcon.isForceReload`, `this.actor.contentWindow.devicePixelRatio`, `this.actor.docShell?.isForceReloading`, `this.beforePageShow`, `this.iconInfos`, `this.iconInfos.length`

## FaviconLoader.addIconFromLink()
- 位置: L700-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeFaviconFromLink()`
- 条件付き依存: `if (iconInfo)` → `this.iconInfos.push()`
- 条件付き依存: `if (iconInfo)` → `this.iconTask.arm()`
- 参照: `iconInfo.beforePageShow`, `this.beforePageShow`

## FaviconLoader.addDefaultIcon()
- 位置: L711-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pageUri.mutate()`, `pageUri.mutate().setPathQueryRef()`, `pageUri.mutate().setPathQueryRef("/favicon.ico").finalize()`, `this.iconInfos.push()`, `this.iconTask.arm()`
- 参照: `this.actor.document`, `this.beforePageShow`

## FaviconLoader.onPageShow()
- 位置: L725-732
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.iconTask.isArmed)` → `this.iconTask.disarm()`
- 条件付き依存: `if (this.iconTask.isArmed)` → `this.loadIcons()`
- 参照: `this.beforePageShow`, `this.iconTask.isArmed`

## FaviconLoader.onPageHide()
- 位置: L734-740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.iconTask.disarm()`, `this.richIconLoader.cancel()`, `this.tabIconLoader.cancel()`
- 参照: `this.iconInfos`

## makeFaviconFromLink()
- 位置: L743-759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extractIconSize()`, `getLinkIconURI()`
- 参照: `aLink.sizes`, `aLink.type`
