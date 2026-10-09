# browser/components/backup/resources/BackupResource.sys.mjs

source: browser/components/backup/resources/BackupResource.sys.mjs
source-hash: 514f36abcb2b006a09385c1e077c8bd9dd4433fd
lines: 412

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## bytesToFuzzyKilobytes()
- 位置: L47-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.max()`, `Math.round()`

## BackupResource.key()
- 位置: L66-71
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BackupError`, `lazy.ERRORS.INTERNAL_ERROR`

## BackupResource.requiresEncryption()
- 位置: L82-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BackupError`, `lazy.ERRORS.INTERNAL_ERROR`

## BackupResource.priority()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)

## BackupResource.getFileSize()
- 位置: async L109-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.stat()`, `bytesToFuzzyKilobytes()`

## BackupResource.getDirectorySize()
- 位置: async L135-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.getChildren()`, `IOUtils.stat()`, `shouldExclude()`
- 条件付き依存: `if (childSize >= 0)` → `bytesToFuzzyKilobytes()`
- 条件付き依存: `if (childType == "directory")` → `this.getDirectorySize()`
- 条件付き依存: `if (childType == "directory")` → `Number.isInteger()`

## BackupResource.copySqliteDatabases()
- 位置: async L196-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `connection.backup()`, `connection?.close()`, `lazy.Sqlite.openConnection()`
- 参照: `BackupResource.SQLITE_PAGES_PER_STEP`, `BackupResource.SQLITE_STEP_DELAY_MS`

## BackupResource.copyFiles()
- 位置: async L240-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`
- 条件付き依存: `if (await IOUtils.exists(sourceFilePath))` → `IOUtils.copy()`

## BackupResource.canBackupResource()
- 位置: L263-266
- 役割: (未記入)
- 触るとき: (未記入)

## BackupResource.backingUpPlaces()
- 位置: L273-290
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.isBrowsingHistoryEnabled`, `lazy.isHistoryClearedOnShutdown`, `lazy.isSanitizeOnShutdownEnabled`

## BackupResource.constructor()
- 位置: L292-292
- 役割: (未記入)
- 触るとき: (未記入)

## BackupResource.measure()
- 位置: async L302-307
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BackupError`, `lazy.ERRORS.INTERNAL_ERROR`

## BackupResource.backup()
- 位置: async L334-339
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BackupError`, `lazy.ERRORS.INTERNAL_ERROR`

## BackupResource.recover()
- 位置: async L370-375
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BackupError`, `lazy.ERRORS.INTERNAL_ERROR`

## BackupResource.postRecovery()
- 位置: async L394-396
- 役割: (未記入)
- 触るとき: (未記入)
