# browser/components/backup/resources/SiteSettingsBackupResource.sys.mjs

source: browser/components/backup/resources/SiteSettingsBackupResource.sys.mjs
source-hash: 789f8da4f23bfd38f13a0691caa6774354d0670a
lines: 81

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## SiteSettingsBackupResource.key()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)

## SiteSettingsBackupResource.requiresEncryption()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)

## SiteSettingsBackupResource.priority()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)

## SiteSettingsBackupResource.canBackupResource()
- 位置: L40-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.isSanitizeOnShutdownEnabled`, `lazy.isSiteSettingsClearedOnShutdown`

## SiteSettingsBackupResource.backup()
- 位置: async L48-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copySqliteDatabases()`
- 参照: `PathUtils.profileDir`

## SiteSettingsBackupResource.recover()
- 位置: async L62-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`

## SiteSettingsBackupResource.measure()
- 位置: async L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PathUtils.profileDir`
