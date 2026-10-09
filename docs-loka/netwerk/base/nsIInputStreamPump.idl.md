# nsIInputStreamPump (netwerk/base/nsIInputStreamPump.idl)

source: netwerk/base/nsIInputStreamPump.idl
source-hash: 7469567a24f726b72d07a28b82e42909d6310baf

- 継承: nsIRequest
- 役割: nsIInputStreamPump
- 実装: (未記入)
- 使っているJS: [`browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs`](../../browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs.md)

## メソッド / 属性
- `void init(nsIInputStream aStream, unsigned long aSegmentSize, unsigned long aSegmentCount, boolean aCloseWhenDone, nsISerialEventTarget aMainThreadTarget)`: Initialize the input stream pump.
- `void reset()`: (未記入)
- `void asyncRead(nsIStreamListener aListener)`: asyncRead causes the input stream to be read in chunks and delivered
