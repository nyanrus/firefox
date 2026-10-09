# nsIBinaryInputStream (xpcom/io/nsIBinaryInputStream.idl)

source: xpcom/io/nsIBinaryInputStream.idl
source-hash: f0aa99da8782c302e13dda3d03788ae53fa4162a

- 継承: nsIInputStream
- 役割: This interface allows consumption of primitive data types from a "binary
- 実装: (未記入)
- 使っているJS: [`browser/components/search/content/addEngine.js`](../../browser/components/search/content/addEngine.js.md), [`browser/components/shell/ShellService.sys.mjs`](../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `void setInputStream(nsIInputStream aInputStream)`: (未記入)
- `boolean readBoolean()`: Read 8-bits from the stream.
- `uint8_t read8()`: (未記入)
- `uint16_t read16()`: (未記入)
- `uint32_t read32()`: (未記入)
- `uint64_t read64()`: (未記入)
- `float readFloat()`: (未記入)
- `double readDouble()`: (未記入)
- `ACString readCString()`: Read an 8-bit pascal style string from the stream.
- `AString readString()`: Read an 16-bit pascal style string from the stream.
- `void readBytes(uint32_t aLength, string aString)`: Read an opaque byte array from the stream.
- `Array<uint8_t> readByteArray(uint32_t aLength)`: Read an opaque byte array from the stream, storing the results
- `uint64_t readArrayBuffer(uint64_t aLength, jsval aArrayBuffer)`: Read opaque bytes from the stream, storing the results in an ArrayBuffer.
