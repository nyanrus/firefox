# browser/components/backup/resources/PlacesBackupResource.sys.mjs

source: browser/components/backup/resources/PlacesBackupResource.sys.mjs
source-hash: aa808df22ed9d9b0a1aa456b1b8c0251a27c589e
lines: 88

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PlacesBackupResource.key()
- 位置: L18-20
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesBackupResource.requiresEncryption()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesBackupResource.priority()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesBackupResource.canBackupResource()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BackupResource.backingUpPlaces`

## PlacesBackupResource.backup()
- 位置: async L34-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copySqliteDatabases()`, `MeasurementUtils.measure()`, `PathUtils.join()`, `Promise.all()`, `lazy.PlacesDBUtils.removeDownloadsMetadataFromDb()`
- 参照: `Glean.browserBackup.faviconsTime`, `Glean.browserBackup.placesTime`, `PathUtils.profileDir`

## PlacesBackupResource.recover()
- 位置: async L68-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`

## PlacesBackupResource.measure()
- 位置: async L78-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getFileSize()`, `Glean.browserBackup.faviconsSize.set()`, `Glean.browserBackup.placesSize.set()`, `PathUtils.join()`
- 参照: `PathUtils.profileDir`
