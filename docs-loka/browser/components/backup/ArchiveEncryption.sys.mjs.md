# browser/components/backup/ArchiveEncryption.sys.mjs

source: browser/components/backup/ArchiveEncryption.sys.mjs
source-hash: 3831f456989acd33b0e8abff883115f32302beed
lines: 628

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## setLastChunkOnNonce()
- 位置: L40-53
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BackupError`, `lazy.ERRORS.ENCRYPTION_FAILED`

## lastChunkSetOnNonce()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)

## incrementNonce()
- 位置: L77-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BigInt()`, `view.getBigUint64()`, `view.setBigUint64()`
- 参照: `ArchiveUtils.ARCHIVE_CHUNK_MAX_BYTES_SIZE`, `ArchiveUtils.ARCHIVE_MAX_BYTES_SIZE`, `lazy.BackupError`, `lazy.ERRORS.ENCRYPTION_FAILED`, `nonce.buffer`

## ArchiveEncryptor.constructor()
- 位置: L156-164
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ArchiveEncryptor.#isInternalConstructing`, `lazy.BackupError`, `lazy.ERRORS.UNKNOWN`

## ArchiveEncryptor.#isDone()
- 位置: L172-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NonceUtils.lastChunkSetOnNonce()`
- 参照: `this.#nonce`

## ArchiveEncryptor.#initialize()
- 位置: async L187-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ArchiveUtils.computeEncryptionKeys()`, `crypto.getRandomValues()`, `crypto.subtle.encrypt()`
- 参照: `this.#authKey`, `this.#encKey`, `this.#publicKey`, `this.#wrappedArchiveKeyMaterial`

## ArchiveEncryptor.encrypt()
- 位置: async L223-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NonceUtils.incrementNonce()`, `crypto.subtle.encrypt()`, `this.#isDone()`, `this.#nonce.subarray()`
- 条件付き依存: `if (isLastChunk)` → `NonceUtils.setLastChunkOnNonce()`
- 参照: `ArchiveUtils.ARCHIVE_CHUNK_MAX_BYTES_SIZE`, `ArchiveUtils.TAG_LENGTH`, `lazy.BackupError`, `lazy.ERRORS.ENCRYPTION_FAILED`, `plaintextChunk.byteLength`, `this.#encKey`, `this.#nonce`

## ArchiveEncryptor.confirm()
- 位置: async L296-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ArchiveUtils.arrayToBase64()`, `JSON.stringify()`, `crypto.subtle.sign()`, `textEncoder.encode()`
- 参照: `ArchiveUtils.SCHEMA_VERSION`, `this.#authKey`, `this.#wrappedArchiveKeyMaterial`

## ArchiveEncryptor.initialize()
- 位置: async L328-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `instance.#initialize()`
- 参照: `ArchiveEncryptor.#isInternalConstructing`

## ArchiveDecryptor.constructor()
- 位置: L386-394
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ArchiveDecryptor.#isInternalConstructing`, `lazy.BackupError`, `lazy.ERRORS.UNKNOWN`

## ArchiveDecryptor.OSKeyStoreSecret()
- 位置: L401-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isDone()`
- 参照: `lazy.BackupError`, `lazy.ERRORS.UNKNOWN`, `this.#_OSKeyStoreSecret`

## ArchiveDecryptor.#initialize()
- 位置: async L424-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ArchiveUtils.computeBackupKeys()`, `ArchiveUtils.computeEncryptionKeys()`, `ArchiveUtils.stringToArray()`, `JSON.parse()`, `JSON.stringify()`, `crypto.subtle.decrypt()`, `crypto.subtle.importKey()`, `crypto.subtle.verify()`, `textDecoder.decode()`, `textEncoder.encode()`
- 条件付き依存: `if (!verified)` → `this.#poisonSelf()`
- 参照: `ArchiveUtils.SCHEMA_VERSION`, `encConfig.confirmation`, `encConfig.nonce`, `encConfig.salt`, `encConfig.wrappedArchiveKeyMaterial`, `encConfig.wrappedSecrets`, `jsonBlock.version`, `lazy.BackupError`, `lazy.ERRORS.CORRUPTED_ARCHIVE`, `lazy.ERRORS.UNAUTHORIZED`, `lazy.ERRORS.UNSUPPORTED_BACKUP_VERSION`, `secrets.OSKeyStoreSecret`, `secrets.privateKey`, `this.#_OSKeyStoreSecret`, `this.#archiveEncKey`, `this.#privateKey`

## ArchiveDecryptor.decrypt()
- 位置: async L524-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NonceUtils.incrementNonce()`, `crypto.subtle.decrypt()`, `this.#nonce.subarray()`, `this.#poisonSelf()`, `this.isDone()`
- 条件付き依存: `if (isLastChunk)` → `NonceUtils.setLastChunkOnNonce()`
- 参照: `ArchiveUtils.ARCHIVE_CHUNK_MAX_BYTES_SIZE`, `ArchiveUtils.TAG_LENGTH`, `ArchiveUtils.TAG_LENGTH_BYTES`, `ciphertextChunk.byteLength`, `lazy.BackupError`, `lazy.ERRORS.DECRYPTION_FAILED`, `this.#archiveEncKey`, `this.#nonce`

## ArchiveDecryptor.#poisonSelf()
- 位置: L590-595
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#_OSKeyStoreSecret`, `this.#archiveEncKey`, `this.#nonce`, `this.#privateKey`

## ArchiveDecryptor.isDone()
- 位置: L603-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NonceUtils.lastChunkSetOnNonce()`
- 参照: `this.#nonce`

## ArchiveDecryptor.initialize()
- 位置: async L621-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `instance.#initialize()`
- 参照: `ArchiveDecryptor.#isInternalConstructing`
