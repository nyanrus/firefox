# nsIBinaryOutputStream (xpcom/io/nsIBinaryOutputStream.idl)

source: xpcom/io/nsIBinaryOutputStream.idl
source-hash: 8c4ef2f9743b4a1f15d55d1602a1f210453ff7cc

- 継承: nsIOutputStream
- 役割: This interface allows writing of primitive data types (integers,
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md)

## メソッド / 属性
- `void setOutputStream(nsIOutputStream aOutputStream)`: (未記入)
- `void writeBoolean(boolean aBoolean)`: Write a boolean as an 8-bit char to the stream.
- `void write8(uint8_t aByte)`: (未記入)
- `void write16(uint16_t a16)`: (未記入)
- `void write32(uint32_t a32)`: (未記入)
- `void write64(uint64_t a64)`: (未記入)
- `void writeFloat(float aFloat)`: (未記入)
- `void writeDouble(double aDouble)`: (未記入)
- `void writeStringZ(string aString)`: Write an 8-bit pascal style string to the stream.
- `void writeWStringZ(wstring aString)`: Write a 16-bit pascal style string to the stream.
- `void writeUtf8Z(wstring aString)`: Write an 8-bit pascal style string (UTF8-encoded) to the stream.
- `void writeBytes(string aString, uint32_t aLength)`: Write an opaque byte array to the stream.
- `void writeBytesNative(Bytes aBytes)`: Non-scriptable and saner-signature version of the same.
- `void writeByteArray(Array<uint8_t> aBytes)`: Write an opaque byte array to the stream.
