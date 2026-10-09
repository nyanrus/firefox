# browser/components/backup/ArchiveEncryptionState.sys.mjs

source: browser/components/backup/ArchiveEncryptionState.sys.mjs
source-hash: 84f0f6422e58f04a514bc4ab841ee7a07fef84b8
lines: 349

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## ArchiveEncryptionState.VERSION()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)

## ArchiveEncryptionState.GENERATED_RECOVERY_CODE_LENGTH()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)

## ArchiveEncryptionState.publicKey()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state.publicKey`

## ArchiveEncryptionState.backupAuthKey()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state.backupAuthKey`

## ArchiveEncryptionState.salt()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state.salt`

## ArchiveEncryptionState.nonce()
- 位置: L99-101
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state.nonce`

## ArchiveEncryptionState.wrappedSecrets()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state.wrappedSecrets`

## ArchiveEncryptionState.constructor()
- 位置: L113-121
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ArchiveEncryptionState.#isInternalConstructing`, `lazy.BackupError`, `lazy.ERRORS.UNKNOWN`

## ArchiveEncryptionState.#enable()
- 位置: async L140-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `crypto.getRandomValues()`, `crypto.subtle.encrypt()`, `crypto.subtle.exportKey()`, `crypto.subtle.generateKey()`, `lazy.ArchiveUtils.computeBackupKeys()`, `lazy.OSKeyStore.exportRecoveryPhrase()`, `lazy.logConsole.debug()`, `salt.set()`, `textEncoder.encode()`
- 条件付き依存: `if (!recoveryCode)` → `Math.floor()`
- 条件付き依存: `if (!recoveryCode)` → `crypto.getRandomValues()`
- 参照: `ArchiveEncryptionState.GENERATED_RECOVERY_CODE_LENGTH`, `ArchiveEncryptionState.VERSION`, `SALT_SUFFIX.length`, `charset.length`, `keyPair.privateKey`, `keyPair.publicKey`, `recoveryCode.length`, `saltPrefix.length`, `this.#state`

## ArchiveEncryptionState.serialize()
- 位置: async L245-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.subtle.exportKey()`, `lazy.ArchiveUtils.arrayToBase64()`
- 参照: `ArchiveEncryptionState.VERSION`, `this.#state.backupAuthKey`, `this.#state.nonce`, `this.#state.publicKey`, `this.#state.salt`, `this.#state.wrappedSecrets`

## ArchiveEncryptionState.#deserialize()
- 位置: async L275-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.subtle.importKey()`, `lazy.ArchiveUtils.stringToArray()`, `lazy.logConsole.debug()`
- 参照: `ArchiveEncryptionState.VERSION`, `lazy.BackupError`, `lazy.ERRORS.UNSUPPORTED_BACKUP_VERSION`, `stateData.backupAuthKey`, `stateData.nonce`, `stateData.publicKey`, `stateData.salt`, `stateData.version`, `stateData.wrappedSecrets`, `this.#state`

## ArchiveEncryptionState.initialize()
- 位置: async L338-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `instance.#enable()`
- 条件付き依存: `if (typeof stateDataOrRecoveryCode == "object")` → `instance.#deserialize()`
- 参照: `ArchiveEncryptionState.#isInternalConstructing`
