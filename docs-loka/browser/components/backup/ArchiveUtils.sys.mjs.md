# browser/components/backup/ArchiveUtils.sys.mjs

source: browser/components/backup/ArchiveUtils.sys.mjs
source-hash: 449465d63494d85770ebacf435f499b5b4744c3f
lines: 321

## <module>
- 役割: (未記入)

## arrayToBase64()
- 位置: L19-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String.fromCharCode()`, `btoa()`
- 参照: `bytes.length`

## stringToArray()
- 位置: L36-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `atob()`, `binaryStr.charCodeAt()`
- 参照: `binaryStr.length`

## SCHEMA_VERSION()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)

## ARCHIVE_FILE_VERSION()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)

## INLINE_MIME_START_MARKER()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)

## INLINE_MIME_END_MARKER()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)

## ARCHIVE_CHUNK_MAX_BYTES_SIZE()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)

## ARCHIVE_MAX_BYTES_SIZE()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)

## TAG_LENGTH()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)

## TAG_LENGTH_BYTES()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.TAG_LENGTH`

## computeBackupKeys()
- 位置: async L150-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.subtle.deriveBits()`, `crypto.subtle.deriveKey()`, `crypto.subtle.importKey()`, `textEncoder.encode()`

## computeEncryptionKeys()
- 位置: async L239-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.subtle.deriveKey()`, `crypto.subtle.importKey()`, `textEncoder.encode()`

## countReplacementCharacters()
- 位置: L308-319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 参照: `str.length`
