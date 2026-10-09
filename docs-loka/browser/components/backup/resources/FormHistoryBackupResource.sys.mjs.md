# browser/components/backup/resources/FormHistoryBackupResource.sys.mjs

source: browser/components/backup/resources/FormHistoryBackupResource.sys.mjs
source-hash: ad02510187a2da06fdc0bee81f1576fb0764883a
lines: 89

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## FormHistoryBackupResource.key()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)

## FormHistoryBackupResource.requiresEncryption()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)

## FormHistoryBackupResource.canBackupResource()
- 位置: L47-60
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.isBrowsingHistoryEnabled`, `lazy.isFormDataClearedOnShutdown`, `lazy.isSanitizeOnShutdownEnabled`

## FormHistoryBackupResource.backup()
- 位置: async L62-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copySqliteDatabases()`
- 参照: `PathUtils.profileDir`

## FormHistoryBackupResource.recover()
- 位置: async L74-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`

## FormHistoryBackupResource.measure()
- 位置: async L82-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getFileSize()`, `Glean.browserBackup.formHistorySize.set()`, `PathUtils.join()`
- 参照: `PathUtils.profileDir`
