# nsIFileInputStream (netwerk/base/nsIFileStreams.idl)

source: netwerk/base/nsIFileStreams.idl
source-hash: c15aa4f8df14260745c4124e2059fd3807ed5caa

- 継承: nsIInputStream
- 役割: An input stream that allows you to read from a file.
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md)

## メソッド / 属性
- `void init(nsIFile file, long ioFlags, long perm, long behaviorFlags)`: @param file          file to read from
- `const long CLOSE_ON_EOF`: If this is set, the file will close automatically when the end of the
- `const long REOPEN_ON_REWIND`: If this is set, the file will be reopened whenever we reach the start of
- `const long DEFER_OPEN`: If this is set, the file will be opened (i.e., a call to
- `const long SHARE_DELETE`: This flag has no effect and is totally ignored on any platform except

# nsIFileOutputStream (netwerk/base/nsIFileStreams.idl)

source: netwerk/base/nsIFileStreams.idl
source-hash: c15aa4f8df14260745c4124e2059fd3807ed5caa

- 継承: nsIOutputStream
- 役割: An output stream that lets you stream to a file.
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md), [`browser/components/extensions/parent/ext-tabs.js`](../../browser/components/extensions/parent/ext-tabs.js.md)

## メソッド / 属性
- `void init(nsIFile file, long ioFlags, long perm, long behaviorFlags)`: @param file          file to write to
- `void preallocate(long long length)`: @param length        asks the operating system to allocate storage for
- `const long DEFER_OPEN`: See the same constant in nsIFileInputStream. The deferred open will

# nsIFileRandomAccessStream (netwerk/base/nsIFileStreams.idl)

source: netwerk/base/nsIFileStreams.idl
source-hash: c15aa4f8df14260745c4124e2059fd3807ed5caa

- 継承: nsIRandomAccessStream
- 役割: A stream that allows you to read from a file or stream to a file.
- 実装: (未記入)

## メソッド / 属性
- `void init(nsIFile file, long ioFlags, long perm, long behaviorFlags)`: @param file          file to read from or stream to
- `const long DEFER_OPEN`: See the same constant in nsIFileInputStream. The deferred open will

# nsIFileMetadata (netwerk/base/nsIFileStreams.idl)

source: netwerk/base/nsIFileStreams.idl
source-hash: c15aa4f8df14260745c4124e2059fd3807ed5caa

- 継承: nsISupports
- 役割: An interface that allows you to get some metadata like file size and
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute long long size`: File size in bytes.
- `readonly attribute long long lastModified`: File last modified time in milliseconds from midnight (00:00:00),
- `PRFileDescPtr getFileDescriptor()`: The internal file descriptor. It can be used for memory mapping of the

# nsIAsyncFileMetadata (netwerk/base/nsIFileStreams.idl)

source: netwerk/base/nsIFileStreams.idl
source-hash: c15aa4f8df14260745c4124e2059fd3807ed5caa

- 継承: nsIFileMetadata
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void asyncFileMetadataWait(nsIFileMetadataCallback aCallback, nsIEventTarget aEventTarget)`: Asynchronously wait for the object to be ready.

# nsIFileMetadataCallback (netwerk/base/nsIFileStreams.idl)

source: netwerk/base/nsIFileStreams.idl
source-hash: c15aa4f8df14260745c4124e2059fd3807ed5caa

- 継承: nsISupports
- 役割: This is a companion interface for
- 実装: (未記入)

## メソッド / 属性
- `void onFileMetadataReady(nsIAsyncFileMetadata aObject)`: Called to indicate that the nsIFileMetadata object is ready.
