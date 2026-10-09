# nsIStringInputStream (xpcom/io/nsIStringStream.idl)

source: xpcom/io/nsIStringStream.idl
source-hash: 655d299d9daa074b67c2847dcc10f9f83b994cc8

- 継承: nsIInputStream
- 役割: nsIStringInputStream
- 実装: (未記入)
- 使っているJS: [`browser/components/genai/GenAI.sys.mjs`](../../browser/components/genai/GenAI.sys.mjs.md), [`browser/components/newtab/AboutNewTabRedirector.sys.mjs`](../../browser/components/newtab/AboutNewTabRedirector.sys.mjs.md), [`browser/components/urlbar/UrlbarUtils.sys.mjs`](../../browser/components/urlbar/UrlbarUtils.sys.mjs.md)

## メソッド / 属性
- `void setByteStringData(ACString data)`: SetData - assign data to the input stream from a byte string.
- `void setUTF8Data(AUTF8String data)`: SetUTF8Data - encode input data to UTF-8 and assign it to the input
- `void copyData(string data, size_t dataLen)`: NOTE: the following methods are designed to give C++ code added control
- `void adoptData(charPtr data, size_t dataLen)`: AdoptData - assign data to the input stream.  the input stream takes
- `void shareData(string data, size_t dataLen)`: ShareData - assign data to the input stream.  the input stream references
- `void setDataSource(StreamBufferSource source)`: SetDataSource - assign data to the input stream.  the input stream holds
- `size_t SizeOfIncludingThisIfUnshared(MallocSizeOf aMallocSizeOf)`: (未記入)
- `size_t SizeOfIncludingThisEvenIfShared(MallocSizeOf aMallocSizeOf)`: (未記入)
