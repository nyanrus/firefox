# browser/components/backup/resources/AddonsBackupResource.sys.mjs

source: browser/components/backup/resources/AddonsBackupResource.sys.mjs
source-hash: 3bc95746c9d42eec82e6d541d219240edf3c174d
lines: 172

## <module>
- 役割: (未記入)

## AddonsBackupResource.key()
- 位置: L11-13
- 役割: (未記入)
- 触るとき: (未記入)

## AddonsBackupResource.requiresEncryption()
- 位置: L15-17
- 役割: (未記入)
- 触るとき: (未記入)

## AddonsBackupResource.backup()
- 位置: async L19-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`, `BackupResource.copySqliteDatabases()`, `IOUtils.getChildren()`, `IOUtils.makeDirectory()`, `PathUtils.join()`, `childFilePath.endsWith()`
- 条件付き依存: `if (childFilePath.endsWith(".xpi"))` → `PathUtils.filename()`
- 条件付き依存: `if (childFilePath.endsWith(".xpi"))` → `xpiFiles.push()`
- 参照: `PathUtils.profileDir`

## AddonsBackupResource.recover()
- 位置: async L74-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`

## AddonsBackupResource.measure()
- 位置: async L90-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getDirectorySize()`, `BackupResource.getFileSize()`, `Glean.browserBackup.browserExtensionDataSize.set()`, `Glean.browserBackup.extensionsJsonSize.set()`, `Glean.browserBackup.extensionsXpiDirectorySize.set()`, `Glean.browserBackup.storageSyncSize.set()`, `Number.isInteger()`, `PathUtils.join()`
- 条件付き依存: `if (Number.isInteger(extensionStorePermissionsDataSize))` → `Glean.browserBackup.extensionStorePermissionsDataSize.set()`
- 条件付き依存: `if (Number.isInteger(extensionsStorageSize))` → `Glean.browserBackup.extensionsStorageSize.set()`
- 参照: `PathUtils.profileDir`

## shouldExclude()
- 位置: L133-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filePath.endsWith()`

## shouldExclude()
- 位置: L156-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.filename()`, `PathUtils.filename(filePath).startsWith()`
