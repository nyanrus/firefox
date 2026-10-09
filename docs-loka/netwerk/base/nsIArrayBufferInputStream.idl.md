# nsIArrayBufferInputStream (netwerk/base/nsIArrayBufferInputStream.idl)

source: netwerk/base/nsIArrayBufferInputStream.idl
source-hash: d6a576636c7c2af794372bd296feb93b412ac19e

- 継承: nsIInputStream
- 役割: nsIArrayBufferInputStream
- 実装: (未記入)
- 使っているJS: [`browser/extensions/newtab/lib/RemoteRenderer.sys.mjs`](../../browser/extensions/newtab/lib/RemoteRenderer.sys.mjs.md)

## メソッド / 属性
- `void setData(jsval buffer, uint64_t byteOffset, uint64_t byteLen)`: SetData - assign an ArrayBuffer to the input stream.
- `void setDataNative(Bytes bytes, uint64_t byteLen)`: SetData - assign data to the input stream.
