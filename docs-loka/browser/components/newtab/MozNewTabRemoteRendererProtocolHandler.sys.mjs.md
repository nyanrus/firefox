# browser/components/newtab/MozNewTabRemoteRendererProtocolHandler.sys.mjs

source: browser/components/newtab/MozNewTabRemoteRendererProtocolHandler.sys.mjs
source-hash: 421c2bbd06f693febbf6833a0aed1873715cc068
lines: 110

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## MozNewTabRemoteRendererProtocolHandler.#getActor()
- 位置: L14-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `globalChild.getActor()`
- 参照: `browsingContext.window.windowGlobalChild`, `loadInfo.browsingContext`

## MozNewTabRemoteRendererProtocolHandler.allowPort()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)

## MozNewTabRemoteRendererProtocolHandler.newChannel()
- 位置: L55-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Cc["@mozilla.org/network/input-stream-channel;1"] .createInstance(Ci.nsIInputStreamChannel) .QueryInterface()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Cc["@mozilla.org/network/input-stream-channel;1"] .createInstance()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `innerChannel.setURI()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Services.io.newSuspendableChannelWrapper()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `suspendedChannel.suspend()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Promise.resolve() .then()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Promise.resolve()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `this.#getActor()`
- 条件付き依存: `if (!actor)` → `Components.Exception()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `actor.sendQuery()`
- 条件付き依存: `if (result.success)` → `suspendedChannel.resume()`
- 条件付き依存: `if (!(result.success))` → `innerChannel.cancel()`
- 条件付き依存: `if (!(result.success))` → `suspendedChannel.resume()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `console.error()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `innerChannel.cancel()`
- 条件付き依存: `if ( Services.appinfo.remoteType === lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `suspendedChannel.resume()`
- 参照: `Ci.nsIChannel`, `Ci.nsIInputStreamChannel`, `Cr.NS_ERROR_FAILURE`, `Cr.NS_ERROR_INVALID_ARG`, `Cr.NS_ERROR_NOT_AVAILABLE`, `Services.appinfo.remoteType`, `innerChannel.contentStream`, `innerChannel.contentType`, `innerChannel.loadInfo`, `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `result.contentType`, `result.inputStream`, `result.success`, `uri.spec`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIInputStreamChannel`](../../../netwerk/base/nsIInputStreamChannel.idl.md) / `@mozilla.org/network/input-stream-channel;1` / `Services.appinfo` / `Services.io`
