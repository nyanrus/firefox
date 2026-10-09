# nsIInputStreamReceiver (netwerk/base/nsICacheInfoChannel.idl)

source: netwerk/base/nsICacheInfoChannel.idl
source-hash: 468072583ca3f7dbaadb645dd75578441456474e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onInputStreamReady(nsIInputStream aStream)`: (未記入)

# nsICacheEntryWriteHandle (netwerk/base/nsICacheInfoChannel.idl)

source: netwerk/base/nsICacheInfoChannel.idl
source-hash: 468072583ca3f7dbaadb645dd75578441456474e

- 継承: nsISupports
- 役割: A light variant of nsICacheInfoChannel, retrievable from
- 実装: (未記入)

## メソッド / 属性
- `nsIAsyncOutputStream openAlternativeOutputStream(ACString type, long long predictedSize)`: Same as nsICacheInfoChannel::openAlternativeOutputStream.

# nsICacheInfoChannel (netwerk/base/nsICacheInfoChannel.idl)

source: netwerk/base/nsICacheInfoChannel.idl
source-hash: 468072583ca3f7dbaadb645dd75578441456474e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/modules/FaviconLoader.sys.mjs`](../../browser/modules/FaviconLoader.sys.mjs.md)

## メソッド / 属性
- `readonly attribute uint32_t cacheTokenFetchCount`: Get the number of times the cache entry has been opened. This attribute is
- `readonly attribute uint32_t cacheTokenExpirationTime`: Get expiration time from cache token. This attribute is equivalent to
- `boolean isFromCache()`: TRUE if this channel's data is being loaded from the cache.  This value
- `boolean hasCacheEntry()`: True if this channel has a corresponding cache entry.  This can be true
- `uint64_t getCacheEntryId()`: The unique ID of the corresponding nsICacheEntry from which the response is
- `attribute unsigned long cacheKey`: Set/get the cache key. This integer uniquely identifies the data in
- `attribute boolean allowStaleCacheContent`: Tells the channel to behave as if the LOAD_FROM_CACHE flag has been set,
- `attribute boolean preferCacheLoadOverBypass`: Tells the priority for LOAD_CACHE is raised over LOAD_BYPASS_CACHE or
- `attribute boolean forceValidateCacheContent`: Tells the channel to be force validated during soft reload.
- `void preferAlternativeDataType(ACString type, ACString contentType, nsICacheInfoChannel_PreferredAlternativeDataDeliveryType deliverAltData)`: Calling this method instructs the channel to serve the alternative data
- `ConstPreferredAlternativeDataTypeArray preferredAlternativeDataTypes()`: Get the preferred alternative data type set by preferAlternativeDataType().
- `readonly attribute ACString alternativeDataType`: Holds the type of the alternative data representation that the channel
- `readonly attribute nsIInputStream alternativeDataInputStream`: If preferAlternativeDataType() has been called passing deliverAltData
- `void getOriginalInputStream(nsIInputStreamReceiver aReceiver)`: Sometimes when the channel is delivering alt-data, we may want to somehow
- `nsICacheEntryWriteHandle getCacheEntryWriteHandle()`: Get a handle to open the alternative output stream for later use.
- `nsIAsyncOutputStream openAlternativeOutputStream(ACString type, long long predictedSize)`: Opens and returns an output stream that a consumer may use to save an
- `nsICacheInfoChannel_CacheDisposition getCacheDisposition()`: Returns the cache disposition for this channel.
