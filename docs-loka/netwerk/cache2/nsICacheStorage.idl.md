# nsICacheStorage (netwerk/cache2/nsICacheStorage.idl)

source: netwerk/cache2/nsICacheStorage.idl
source-hash: 5e8130a55ae88c0116456fd22f132f748c14053c

- 継承: nsISupports
- 役割: Representation of a cache storage. There can be just-in-mem,
- 実装: (未記入)
- 使っているJS: [`browser/base/content/pageinfo/pageInfo.js`](../../browser/base/content/pageinfo/pageInfo.js.md), [`browser/components/mozcachedohttp/actors/MozCachedOHTTPParent.sys.mjs`](../../browser/components/mozcachedohttp/actors/MozCachedOHTTPParent.sys.mjs.md), [`browser/components/newtab/AboutHomeStartupCache.sys.mjs`](../../browser/components/newtab/AboutHomeStartupCache.sys.mjs.md), [`browser/extensions/newtab/lib/RemoteRenderer.sys.mjs`](../../browser/extensions/newtab/lib/RemoteRenderer.sys.mjs.md)

## メソッド / 属性
- `const uint32_t OPEN_NORMALLY`: Placeholder for specifying "no special flags" during open.
- `const uint32_t OPEN_TRUNCATE`: Rewrite any existing data when opening a URL.
- `const uint32_t OPEN_READONLY`: Only open an existing entry.  Don't create a new one.
- `const uint32_t OPEN_PRIORITY`: Use for first-paint blocking loads.
- `const uint32_t OPEN_BYPASS_IF_BUSY`: Bypass the cache load when write is still in progress.
- `const uint32_t CHECK_MULTITHREADED`: Perform the cache entry check (onCacheEntryCheck invocation) on any thread
- `const uint32_t OPEN_SECRETLY`: Don't automatically update any 'last used' metadata of the entry.
- `const uint32_t OPEN_INTERCEPTED`: Entry is being opened as part of a service worker interception.  Do not
- `const uint32_t OPEN_COMPLETE_ONLY`: Only open an existing entry which is complete (i.e. not being written)
- `const uint32_t OPEN_ALWAYS`: Open even if we're revalidating/etc; used for Dictionary Cache loads
- `void asyncOpenURI(nsIURI aURI, ACString aIdExtension, uint32_t aFlags, nsICacheEntryOpenCallback aCallback)`: Asynchronously opens a cache entry for the specified URI.
- `void asyncOpenURIString(ACString aURI, ACString aIdExtension, uint32_t aFlags, nsICacheEntryOpenCallback aCallback)`: Asynchronously opens a cache entry for the specified URI.
- `nsICacheEntry openTruncate(nsIURI aURI, ACString aIdExtension)`: Immediately opens a new and empty cache entry in the storage, any existing
- `boolean exists(nsIURI aURI, ACString aIdExtension)`: Synchronously check on existance of an entry.  In case of disk entries
- `void getCacheIndexEntryAttrs(nsIURI aURI, ACString aIdExtension, boolean aHasAltData, uint32_t aSizeInKB)`: Synchronously check on existance of alternative data and size of the
- `void asyncDoomURI(nsIURI aURI, ACString aIdExtension, nsICacheEntryDoomCallback aCallback)`: Asynchronously removes an entry belonging to the URI from the cache.
- `void asyncEvictStorage(nsICacheEntryDoomCallback aCallback)`: Asynchronously removes all cached entries under this storage.
- `void asyncVisitStorage(nsICacheStorageVisitor aVisitor, boolean aVisitEntries)`: Visits the storage and its entries.
