# nsICacheEntryOpenCallback (netwerk/cache2/nsICacheEntryOpenCallback.idl)

source: netwerk/cache2/nsICacheEntryOpenCallback.idl
source-hash: 0116d7cc575825d69fc3895ccc32c64baa61ca92

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/pageinfo/pageInfo.js`](../../browser/base/content/pageinfo/pageInfo.js.md), [`browser/components/mozcachedohttp/actors/MozCachedOHTTPParent.sys.mjs`](../../browser/components/mozcachedohttp/actors/MozCachedOHTTPParent.sys.mjs.md), [`browser/components/newtab/AboutHomeStartupCache.sys.mjs`](../../browser/components/newtab/AboutHomeStartupCache.sys.mjs.md), [`browser/extensions/newtab/lib/RemoteRenderer.sys.mjs`](../../browser/extensions/newtab/lib/RemoteRenderer.sys.mjs.md)

## メソッド / 属性
- `const unsigned long ENTRY_WANTED`: State of the entry determined by onCacheEntryCheck.
- `const unsigned long RECHECK_AFTER_WRITE_FINISHED`: (未記入)
- `const unsigned long ENTRY_NEEDS_REVALIDATION`: (未記入)
- `const unsigned long ENTRY_NOT_WANTED`: (未記入)
- `unsigned long onCacheEntryCheck(nsICacheEntry aEntry)`: Callback to perform any validity checks before the entry should be used.
- `void onCacheEntryAvailable(nsICacheEntry aEntry, boolean aNew, nsresult aResult)`: Callback giving actual result of asyncOpenURI.  It may give consumer the cache
