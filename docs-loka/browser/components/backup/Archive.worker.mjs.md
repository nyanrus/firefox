# browser/components/backup/Archive.worker.mjs

source: browser/components/backup/Archive.worker.mjs
source-hash: fd2d62cd9be531bc11045b7d9d6b48aacca80c78
lines: 454

## <module>
- 役割: (未記入)

## ArchiveWorker.constructor()
- 位置: L25-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connectToPromiseWorker()`

## ArchiveWorker.#generateBoundary()
- 位置: L38-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`, `Math.random().toString()`, `Math.random().toString(36).slice()`, `new Date().getTime()`

## ArchiveWorker.#computeChunkBase64Bytes()
- 位置: L60-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`
- 参照: `ArchiveUtils.TAG_LENGTH_BYTES`

## ArchiveWorker.constructArchive()
- 位置: async L109-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ArchiveUtils.arrayToBase64()`, `IOUtils.openFileForSyncReading()`, `IOUtils.writeUTF8()`, `JSON.stringify()`, `Math.ceil()`, `Math.min()`, `compressedBackupSnapshotFile.close()`, `compressedBackupSnapshotFile.readBytesInto()`, `textEncoder.encode()`, `this.#computeChunkBase64Bytes()`, `this.#generateBoundary()`
- 条件付き依存: `if (encryptionArgs)` → `ArchiveEncryptor.initialize()`
- 条件付き依存: `if (encryptor)` → `encryptor.confirm()`
- 条件付き依存: `if (leftoverChunkBytes)` → `this.#computeChunkBase64Bytes()`
- 条件付き依存: `if (encryptor)` → `encryptor.encrypt()`
- 参照: `ArchiveUtils.INLINE_MIME_END_MARKER`, `ArchiveUtils.INLINE_MIME_START_MARKER`, `ArchiveUtils.SCHEMA_VERSION`, `ERRORS.FILE_SYSTEM_ERROR`, `compressedBackupSnapshotFile.size`, `encryptionArgs.backupAuthKey`, `encryptionArgs.nonce`, `encryptionArgs.publicKey`, `encryptionArgs.salt`, `encryptionArgs.wrappedSecrets`, `textEncoder.encode(serializedJsonBlock).length`

## ArchiveWorker.parseArchiveHeader()
- 位置: L288-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.openFileForSyncReading()`, `Math.min()`, `combinedBuffer.set()`, `decodedHeader.match()`, `decodedString.match()`, `parseInt()`, `syncReadFile.close()`, `syncReadFile.readBytesInto()`, `textDecoder.decode()`
- 条件付き依存: `if (markerMatches)` → `textEncoder.encode()`
- 条件付き依存: `if (markerMatches)` → `decodedString.indexOf()`
- 条件付き依存: `if (markerMatches)` → `ArchiveUtils.countReplacementCharacters()`
- 条件付き依存: `if (markerMatches)` → `decodedString.slice()`
- 参照: `ArchiveUtils.ARCHIVE_FILE_VERSION`, `ArchiveUtils.INLINE_MIME_START_MARKER`, `ERRORS.CORRUPTED_ARCHIVE`, `ERRORS.UNKNOWN`, `ERRORS.UNSUPPORTED_BACKUP_VERSION`, `buffer.byteLength`, `headerBuffer.byteLength`, `oldBuffer.byteLength`, `syncReadFile.size`, `textEncoder.encode(match).byteLength`, `textEncoder.encode(substringUpToMatch).byteLength`

## ArchiveWorker.#connectToPromiseWorker()
- 位置: L429-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.addEventListener()`, `this.#worker.callMainThread.bind()`, `this.#worker.handleMessage()`
- 参照: `PromiseWorker.AbstractWorker`, `error.reason`, `self.callMainThread`, `this.#worker`, `this.#worker.close`, `this.#worker.dispatch`, `this.#worker.postMessage`

## this.#worker.dispatch()
- 位置: L431-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this[method]()`
- 参照: `ERRORS.INTERNAL_ERROR`

## this.#worker.close()
- 位置: L440-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.close()`

## this.#worker.postMessage()
- 位置: L441-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.postMessage()`
