# browser/extensions/newtab/lib/RemoteRenderer.sys.mjs

source: browser/extensions/newtab/lib/RemoteRenderer.sys.mjs
source-hash: 39918264d1d1911bbc24e506c69ab9b0d6c34b20
lines: 779

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Object.freeze()`, `XPCOMUtils.declareLazy()`

## cacheStorage()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cache2.diskCacheStorage()`
- 参照: `Services.loadContextInfo.default`
- XPCOM: `Services.cache2` / `Services.loadContextInfo`

## logConsole()
- 位置: L44-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `console.createInstance()`
- XPCOM: `Services.prefs`

## RemoteRenderer.BUNDLED_VERSION()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BUNDLED_MANIFEST.version`

## RemoteRenderer.REVALIDATION_DEBOUNCE_RATE_MS()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)

## RemoteRenderer.constructor()
- 位置: L104-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.RemoteSettings()`, `lazy.logConsole.log()`, `this.maybeRevalidate()`
- 参照: `RemoteRenderer.REVALIDATION_DEBOUNCE_RATE_MS`, `lazy.DeferredTask`, `this.#revalidateDebouncer`, `this.#rsClient`
- XPCOM: `Services.obs`

## RemoteRenderer.observe()
- 位置: L119-124
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === QUIT_TOPIC)` → `this.onShutdown()`
- 条件付き依存: `if (topic === QUIT_TOPIC)` → `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## RemoteRenderer.onShutdown()
- 位置: L126-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cacheStorage.asyncDoomURI()`
- 参照: `this.#cacheEntryURIsToDoomAtShutdown`

## RemoteRenderer.willDoomOnShutdown()
- 位置: L140-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doomedURI.equals()`, `this.#cacheEntryURIsToDoomAtShutdown.find()`

## RemoteRenderer.doomCacheEntryOnShutdown()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cacheEntryURIsToDoomAtShutdown.push()`

## RemoteRenderer.assign()
- 位置: async L166-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#revalidateDebouncer.arm()`, `this.#revalidateDebouncer.disarm()`, `this.resetCache()`
- 条件付き依存: `if (lazy.remoteRendererVersion)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.remoteRendererVersion)` → `Services.vc.compare()`
- 条件付き依存: `if (Services.vc.compare(RemoteRenderer.BUNDLED_VERSION, version) < 0)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (Services.vc.compare(RemoteRenderer.BUNDLED_VERSION, version) < 0)` → `this.makeManifestEntryURI()`
- 条件付き依存: `if (Services.vc.compare(RemoteRenderer.BUNDLED_VERSION, version) < 0)` → `this.makeScriptEntryURI()`
- 条件付き依存: `if (Services.vc.compare(RemoteRenderer.BUNDLED_VERSION, version) < 0)` → `this.makeStyleEntryURI()`
- 条件付き依存: `if (Services.vc.compare(RemoteRenderer.BUNDLED_VERSION, version) < 0)` → `lazy.cacheStorage.exists()`
- 条件付き依存: `if (Services.vc.compare(RemoteRenderer.BUNDLED_VERSION, version) < 0)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (manifestExists && scriptExists && styleExists)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (manifestExists && scriptExists && styleExists)` → `this.getCachedEntryStream()`
- 条件付き依存: `if (manifestStream)` → `this.pumpInputStreamToString()`
- 条件付き依存: `if (manifestStream)` → `JSON.parse()`
- 条件付き依存: `if (manifestExists && scriptExists && styleExists)` → `lazy.logConsole.warn()`
- 参照: `RemoteRenderer.BUNDLED_VERSION`, `lazy.remoteRendererVersion`
- XPCOM: `Services.vc`

## RemoteRenderer.#makeEntryURI()
- 位置: L301-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- XPCOM: `Services.io`

## RemoteRenderer.makeManifestEntryURI()
- 位置: L314-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#makeEntryURI()`

## RemoteRenderer.makeScriptEntryURI()
- 位置: L326-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#makeEntryURI()`

## RemoteRenderer.makeStyleEntryURI()
- 位置: L338-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#makeEntryURI()`

## RemoteRenderer.resetCache()
- 位置: L346-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- 条件付き依存: `if (remoteRendererVersion)` → `this.makeManifestEntryURI()`
- 条件付き依存: `if (remoteRendererVersion)` → `this.makeScriptEntryURI()`
- 条件付き依存: `if (remoteRendererVersion)` → `this.makeStyleEntryURI()`
- 条件付き依存: `if (remoteRendererVersion)` → `this.doomCacheEntryOnShutdown()`
- XPCOM: `Services.prefs`

## RemoteRenderer.writeCacheEntry()
- 位置: async L370-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cacheStorage.asyncOpenURI()`
- 参照: `Ci.nsICacheStorage.OPEN_TRUNCATE`
- XPCOM: [`nsICacheStorage`](../../../../netwerk/cache2/nsICacheStorage.idl.md)

## RemoteRenderer.onCacheEntryCheck()
- 位置: L377-379
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICacheEntryOpenCallback.ENTRY_WANTED`
- XPCOM: [`nsICacheEntryOpenCallback`](../../../../netwerk/cache2/nsICacheEntryOpenCallback.idl.md)

## RemoteRenderer.onCacheEntryAvailable()
- 位置: async L380-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/io/arraybuffer-input-stream;1" ].createInstance()`, `Components.isSuccessCode()`, `Date.now()`, `Date.now().toString()`, `entry.openOutputStream()`, `entry.setMetaDataElement()`, `inputStream.setData()`, `lazy.NetUtil.asyncCopy()`, `outputStream.close()`, `reject()`, `resolve()`
- 条件付き依存: `if (!Components.isSuccessCode(status))` → `reject()`
- 条件付き依存: `if (Components.isSuccessCode(result))` → `resolveWrite()`
- 条件付き依存: `if (!(Components.isSuccessCode(result)))` → `rejectWrite()`
- 参照: `Ci.nsIArrayBufferInputStream`, `arrayBuffer.byteLength`
- XPCOM: [`nsIArrayBufferInputStream`](../../../../netwerk/base/nsIArrayBufferInputStream.idl.md) / `@mozilla.org/io/arraybuffer-input-stream;1`

## RemoteRenderer.updateFromRemoteSettings()
- 位置: async L431-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Services.prefs.setCharPref()`, `this.makeManifestEntryURI()`, `this.makeScriptEntryURI()`, `this.makeStyleEntryURI()`, `this.writeCacheEntry()`
- XPCOM: `Services.prefs`

## RemoteRenderer.getScriptResource()
- 位置: async L453-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cacheStorage.exists()`, `lazy.logConsole.warn()`, `scriptStream.QueryInterface()`, `this.getCachedEntryStream()`, `this.makeScriptEntryURI()`
- 条件付き依存: `if (!entryExists)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!entryExists)` → `this.#fallbackToBundledScriptStream()`
- 条件付き依存: `if (!scriptStream)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!scriptStream)` → `this.#fallbackToBundledScriptStream()`
- 参照: `Ci.nsIInputStream`, `renderer.appProps.manifest`
- XPCOM: [`nsIInputStream`](../../../../docshell/base/nsIDocShell.idl.md)

## RemoteRenderer.#fallbackToBundledScriptStream()
- 位置: async L496-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/io/arraybuffer-input-stream;1" ].createInstance()`, `fetch()`, `inputStream.setData()`, `lazy.logConsole.error()`, `response.arrayBuffer()`, `this.resetCache()`
- 参照: `Ci.nsIArrayBufferInputStream`, `buffer.byteLength`
- XPCOM: [`nsIArrayBufferInputStream`](../../../../netwerk/base/nsIArrayBufferInputStream.idl.md) / `@mozilla.org/io/arraybuffer-input-stream;1`

## RemoteRenderer.getStyleResource()
- 位置: async L533-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cacheStorage.exists()`, `lazy.logConsole.warn()`, `styleStream.QueryInterface()`, `this.getCachedEntryStream()`, `this.makeStyleEntryURI()`
- 条件付き依存: `if (!entryExists)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!entryExists)` → `this.#fallbackToBundledStyleStream()`
- 条件付き依存: `if (!styleStream)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!styleStream)` → `this.#fallbackToBundledStyleStream()`
- 参照: `Ci.nsIInputStream`, `renderer.appProps.manifest`
- XPCOM: [`nsIInputStream`](../../../../docshell/base/nsIDocShell.idl.md)

## RemoteRenderer.#fallbackToBundledStyleStream()
- 位置: async L576-602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/io/arraybuffer-input-stream;1" ].createInstance()`, `fetch()`, `inputStream.setData()`, `lazy.logConsole.error()`, `response.arrayBuffer()`, `this.resetCache()`
- 参照: `Ci.nsIArrayBufferInputStream`, `buffer.byteLength`
- XPCOM: [`nsIArrayBufferInputStream`](../../../../netwerk/base/nsIArrayBufferInputStream.idl.md) / `@mozilla.org/io/arraybuffer-input-stream;1`

## RemoteRenderer.maybeRevalidate()
- 位置: async L610-627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`, `this.getExpectedVersionFromRemoteSettings()`
- 条件付き依存: `if (Services.vc.compare(currentVersion, latestVersion) < 0)` → `this.fetchLatestContent()`
- 条件付き依存: `if ( newContent && newContent.manifest && newContent.js && newContent.css )` → `this.updateFromRemoteSettings()`
- 参照: `RemoteRenderer.BUNDLED_VERSION`, `lazy.remoteRendererVersion`, `newContent.css`, `newContent.js`, `newContent.manifest`
- XPCOM: `Services.vc`

## RemoteRenderer.getExpectedVersionFromRemoteSettings()
- 位置: async L635-654
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#rsClient.get()`
- 参照: `records.length`, `records[0]?.version`

## RemoteRenderer.fetchLatestContent()
- 位置: async L662-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `console.error()`, `new TextEncoder().encode()`, `records.find()`, `this.#rsClient.attachments.download()`, `this.#rsClient.get()`
- 条件付き依存: `if (!jsRecord || !cssRecord)` → `console.error()`
- 参照: `cssAttachment.buffer`, `cssRecord.attachment.filename`, `jsAttachment.buffer`, `jsRecord.attachment.filename`, `manifest.buffer`, `r.type`, `records.length`

## RemoteRenderer.getCachedEntryStream()
- 位置: async L713-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cacheEntry.openInputStream()`, `this.openCacheEntry()`

## RemoteRenderer.openCacheEntry()
- 位置: async L728-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cacheStorage.asyncOpenURI()`
- 参照: `Ci.nsICacheStorage.OPEN_READONLY`
- XPCOM: [`nsICacheStorage`](../../../../netwerk/cache2/nsICacheStorage.idl.md)

## RemoteRenderer.onCacheEntryCheck()
- 位置: L735-737
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICacheEntryOpenCallback.ENTRY_WANTED`
- XPCOM: [`nsICacheEntryOpenCallback`](../../../../netwerk/cache2/nsICacheEntryOpenCallback.idl.md)

## RemoteRenderer.onCacheEntryAvailable()
- 位置: L738-744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`
- 条件付き依存: `if (isNew || !Components.isSuccessCode(status))` → `resolve()`
- 条件付き依存: `if (!(isNew || !Components.isSuccessCode(status)))` → `resolve()`

## RemoteRenderer.pumpInputStreamToString()
- 位置: L757-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `lazy.NetUtil.asyncFetch()`, `lazy.NetUtil.readInputStreamToString()`, `reject()`, `resolve()`, `stream.available()`
- 条件付き依存: `if (!Components.isSuccessCode(status))` → `reject()`
