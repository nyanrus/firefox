# browser/components/mozcachedohttp/actors/MozCachedOHTTPParent.sys.mjs

source: browser/components/mozcachedohttp/actors/MozCachedOHTTPParent.sys.mjs
source-hash: 815c8e3ee3be798f09a96d1461e4a44750d3e45b
lines: 218

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MozCachedOHTTPParent.receiveMessage()
- 位置: L27-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.reject()`, `Services.io.newURI()`, `this.tryCache()`, `this.writeCache()`
- 条件付き依存: `if ( this.manager.remoteType !== null && this.manager.remoteType !== lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Promise.reject()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `message.data.cacheInputStream`, `message.data.cacheStreamUpdatePort`, `message.data.uriString`, `message.name`, `this.manager.remoteType`
- XPCOM: `Services.io`

## MozCachedOHTTPParent.tryCache()
- 位置: async L62-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cacheEntry .getMetaDataElement()`, `cacheEntry .getMetaDataElement(RESPONSE_HEADER_METADATA_ELEMENT) .split()`, `cacheEntry.openInputStream()`, `headersString.indexOf()`, `headersString.substring()`, `this.#openCacheEntry()`
- 参照: `Ci.nsICacheStorage.OPEN_READONLY`, `RESPONSE_HEADER_KEY_VALUE_DELIMETER.length`, `cacheEntry.dataSize`
- XPCOM: [`nsICacheStorage`](../../../../netwerk/cache2/nsICacheStorage.idl.md)

## MozCachedOHTTPParent.writeCache()
- 位置: async L118-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `cacheEntry.openOutputStream()`, `lazy.NetUtil.asyncCopy()`, `resolve()`, `this.#openCacheEntry()`
- 条件付き依存: `if (!Components.isSuccessCode(writeResult))` → `console.error()`
- 参照: `Ci.nsICacheStorage.OPEN_NORMALLY`, `cacheStreamUpdatePort.onmessage`
- XPCOM: [`nsICacheStorage`](../../../../netwerk/cache2/nsICacheStorage.idl.md)

## cacheStreamUpdatePort.onmessage()
- 位置: L132-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cacheEntry.asyncDoom()`, `cacheEntry.setExpirationTime()`, `cacheEntry.setMetaDataElement()`, `headers.entries()`, `headersStrings.join()`, `headersStrings.push()`
- 参照: `msg.data.expiry`, `msg.data.headersObj`, `msg.data.name`

## MozCachedOHTTPParent.#openCacheEntry()
- 位置: async L186-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cache2.diskCacheStorage()`, `storage.asyncOpenURI()`, `storage.exists()`, `uri.schemeIs()`
- 参照: `Ci.nsICacheStorage.OPEN_READONLY`, `Services.loadContextInfo.anonymous`
- XPCOM: [`nsICacheStorage`](../../../../netwerk/cache2/nsICacheStorage.idl.md) / `Services.cache2` / `Services.loadContextInfo`

## onCacheEntryCheck()
- 位置: L206-206
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICacheEntryOpenCallback.ENTRY_WANTED`
- XPCOM: [`nsICacheEntryOpenCallback`](../../../../netwerk/cache2/nsICacheEntryOpenCallback.idl.md)

## onCacheEntryAvailable()
- 位置: L207-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `resolve()`
- 条件付き依存: `if (!(Components.isSuccessCode(status)))` → `reject()`
