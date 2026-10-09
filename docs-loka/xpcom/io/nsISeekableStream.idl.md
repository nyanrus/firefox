# nsISeekableStream (xpcom/io/nsISeekableStream.idl)

source: xpcom/io/nsISeekableStream.idl
source-hash: 5ba11a3d8784ca1d7797316e209b1833d1d0ff20

- 継承: nsITellableStream
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md)

## メソッド / 属性
- `const int32_t NS_SEEK_SET`: (未記入)
- `const int32_t NS_SEEK_CUR`: (未記入)
- `const int32_t NS_SEEK_END`: (未記入)
- `void seek(long whence, long long offset)`: seek
- `void setEOF()`: setEOF
