# nsIEncodedChannel (netwerk/base/nsIEncodedChannel.idl)

source: netwerk/base/nsIEncodedChannel.idl
source-hash: d2bd154bd82680a9f6bdfbee71e7a8a993ad44b2

- 継承: nsISupports
- 役割: A channel interface which allows special handling of encoded content
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIUTF8StringEnumerator contentEncodings`: This attribute holds the MIME types corresponding to the content
- `attribute boolean applyConversion`: This attribute controls whether or not content conversion should be
- `attribute boolean hasContentDecompressed`: This attribute indicates the content has been decompressed in
- `void doApplyContentConversions(nsIStreamListener aNextListener, nsIStreamListener aNewNextListener, nsISupports aCtxt)`: This function will start converters if they are available.
