# browser/components/backup/resources/CookiesBackupResource.sys.mjs

source: browser/components/backup/resources/CookiesBackupResource.sys.mjs
source-hash: c19619042058b322e1aca67cd36773b5a6eb1eff
lines: 49

## <module>
- 役割: (未記入)

## CookiesBackupResource.key()
- 位置: L11-13
- 役割: (未記入)
- 触るとき: (未記入)

## CookiesBackupResource.requiresEncryption()
- 位置: L15-17
- 役割: (未記入)
- 触るとき: (未記入)

## CookiesBackupResource.canBackupResource()
- 位置: L19-22
- 役割: (未記入)
- 触るとき: (未記入)

## CookiesBackupResource.backup()
- 位置: async L24-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copySqliteDatabases()`
- 参照: `PathUtils.profileDir`

## CookiesBackupResource.recover()
- 位置: async L35-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`

## CookiesBackupResource.measure()
- 位置: async L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getFileSize()`, `Glean.browserBackup.cookiesSize.set()`, `PathUtils.join()`
- 参照: `PathUtils.profileDir`
