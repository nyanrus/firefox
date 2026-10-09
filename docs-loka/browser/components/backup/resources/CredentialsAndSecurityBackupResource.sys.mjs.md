# browser/components/backup/resources/CredentialsAndSecurityBackupResource.sys.mjs

source: browser/components/backup/resources/CredentialsAndSecurityBackupResource.sys.mjs
source-hash: c2617807bd0019deb91d2ffdafde885f3df932a3
lines: 170

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## CredentialsAndSecurityBackupResource.key()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)

## CredentialsAndSecurityBackupResource.requiresEncryption()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)

## CredentialsAndSecurityBackupResource.backup()
- 位置: async L34-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`, `BackupResource.copySqliteDatabases()`
- 参照: `PathUtils.profileDir`

## CredentialsAndSecurityBackupResource.recover()
- 位置: async L63-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`, `IOUtils.exists()`, `PathUtils.join()`
- 条件付き依存: `if (await IOUtils.exists(AUTOFILL_RECORDS_PATH))` → `this.encryptAutofillData()`
- 条件付き依存: `if (await IOUtils.exists(AUTOFILL_RECORDS_PATH))` → `files.push()`

## CredentialsAndSecurityBackupResource.encryptAutofillData()
- 位置: async L97-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`, `IOUtils.writeJSON()`
- 条件付き依存: `if (oldEncryptedCard)` → `lazy.nativeOSKeyStore.asyncSecretAvailable()`
- 条件付き依存: `if ( await lazy.nativeOSKeyStore.asyncSecretAvailable( lazy.BackupService.RECOVERY_OSKEYSTORE_LABEL ) )` → `lazy.nativeOSKeyStore.asyncDecryptBytes()`
- 条件付き依存: `if ( await lazy.nativeOSKeyStore.asyncSecretAvailable( lazy.BackupService.RECOVERY_OSKEYSTORE_LABEL ) )` → `String.fromCharCode.apply()`
- 条件付き依存: `if (!( await lazy.nativeOSKeyStore.asyncSecretAvailable( lazy.BackupService.RECOVERY_OSKEYSTORE_LABEL ) ))` → `lazy.OSKeyStore.decrypt()`
- 条件付き依存: `if (oldEncryptedCard)` → `lazy.OSKeyStore.encrypt()`
- 参照: `autofillRecords.creditCards`, `lazy.BackupService.RECOVERY_OSKEYSTORE_LABEL`

## CredentialsAndSecurityBackupResource.measure()
- 位置: async L134-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getFileSize()`, `Glean.browserBackup.credentialsDataSize.set()`, `Glean.browserBackup.securityDataSize.set()`, `Number.isInteger()`, `PathUtils.join()`
- 参照: `PathUtils.profileDir`
