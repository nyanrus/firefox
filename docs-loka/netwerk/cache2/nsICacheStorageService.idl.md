# nsICacheStorageService (netwerk/cache2/nsICacheStorageService.idl)

source: netwerk/cache2/nsICacheStorageService.idl
source-hash: bfa434da06328bb9abd10068ec5d2b19184f47fb

- 継承: nsISupports
- 役割: Provides access to particual cache storages of the network URI cache.
- 実装: (未記入)
- 使っているJS: [`browser/base/content/pageinfo/pageInfo.js`](../../browser/base/content/pageinfo/pageInfo.js.md)

## メソッド / 属性
- `nsICacheStorage memoryCacheStorage(nsILoadContextInfo aLoadContextInfo)`: Get storage where entries will only remain in memory, never written
- `nsICacheStorage diskCacheStorage(nsILoadContextInfo aLoadContextInfo)`: Get storage where entries will be written to disk when not forbidden by
- `nsICacheStorage pinningCacheStorage(nsILoadContextInfo aLoadContextInfo)`: Get storage where entries will be written to disk and marked as pinned.
- `void clearOriginsByPrincipal(nsIPrincipal aPrincipal)`: Evict any cache entry having the same principal origin and OriginAttributes
- `void clearBaseDomain(AString aBaseDomain)`: Evict any cache entry which belongs to a base domain. This includes entries
- `void clearOriginsByOriginAttributes(AString aOriginAttributes)`: Evict any cache entry having the same originAttributes.
- `void clear()`: Evict the whole cache.
- `void clearOriginDictionary(nsIURI aURI)`: Evict any Dictionary cache entry by site
- `void clearAllOriginDictionaries()`: Evict all Dictionary cache entries
- `const uint32_t PURGE_DISK_DATA_ONLY`: Purge only data of disk backed entries.  Metadata are left for
- `const uint32_t PURGE_DISK_ALL`: Purge whole disk backed entries from memory.  Disk files will
- `const uint32_t PURGE_EVERYTHING`: Purge all entries we keep in memory, including memory-storage
- `void purgeFromMemory(uint32_t aWhat)`: Purges data we keep warmed in memory.  Use for tests and for
- `readonly attribute nsIEventTarget ioTarget`: I/O thread target to use for any operations on disk
- `void asyncGetDiskConsumption(nsICacheStorageConsumptionObserver aObserver)`: Asynchronously determine how many bytes of the disk space the cache takes.
- `void asyncVisitAllStorages(nsICacheStorageVisitor aVisitor, boolean aVisitEntries)`: Asynchronously visits all storages of the disk cache and memory cache.

# nsICacheStorageConsumptionObserver (netwerk/cache2/nsICacheStorageService.idl)

source: netwerk/cache2/nsICacheStorageService.idl
source-hash: bfa434da06328bb9abd10068ec5d2b19184f47fb

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onNetworkCacheDiskConsumption(int64_t aDiskSize)`: Callback invoked to answer asyncGetDiskConsumption call. Always triggered
