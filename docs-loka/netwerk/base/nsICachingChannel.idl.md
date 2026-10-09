# nsICachingChannel (netwerk/base/nsICachingChannel.idl)

source: netwerk/base/nsICachingChannel.idl
source-hash: 0098a547f0d1ba6e2f40fde2dcf939e33f7a0dbb

- 継承: nsICacheInfoChannel
- 役割: A channel may optionally implement this interface to allow clients
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md)

## メソッド / 属性
- `attribute nsISupports cacheToken`: Set/get the cache token... uniquely identifies the data in the cache.
- `attribute boolean cacheOnlyMetadata`: Instructs the channel to only store the metadata of the entry, and not
- `attribute boolean pin`: Tells the channel to use the pinning storage.
- `void forceCacheEntryValidFor(unsigned long aSecondsToTheFuture)`: Overrides cache validation for a time specified in seconds.
- `const unsigned long LOAD_NO_NETWORK_IO`: Caching channel specific load flags:
- `const unsigned long LOAD_BYPASS_LOCAL_CACHE`: This load flag causes the local cache to be skipped when fetching a
- `const unsigned long LOAD_BYPASS_LOCAL_CACHE_IF_BUSY`: This load flag causes the local cache to be skipped if the request
- `const unsigned long LOAD_ONLY_FROM_CACHE`: This load flag inhibits fetching from the net if the data in the cache
- `const unsigned long LOAD_ONLY_IF_MODIFIED`: This load flag controls what happens when a document would be loaded
