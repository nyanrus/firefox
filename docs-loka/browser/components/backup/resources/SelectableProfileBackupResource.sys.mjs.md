# browser/components/backup/resources/SelectableProfileBackupResource.sys.mjs

source: browser/components/backup/resources/SelectableProfileBackupResource.sys.mjs
source-hash: 65237f18752ff1454c1589d1966b466a0a2c67b3
lines: 222

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## SelectableProfileBackupResource.key()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## SelectableProfileBackupResource.requiresEncryption()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)

## SelectableProfileBackupResource.canBackupResource()
- 位置: L45-48
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SelectableProfileService.currentProfile`

## SelectableProfileBackupResource.backup()
- 位置: async L50-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `IOUtils.writeJSON()`, `JSON.stringify()`, `PathUtils.join()`, `Services.sysinfo.get()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (!selectableProfile)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (selectableProfile.hasCustomAvatar)` → `PathUtils.parent()`
- 条件付き依存: `if (selectableProfile.hasCustomAvatar)` → `lazy.SelectableProfileService.currentProfile.getAvatarPath()`
- 条件付き依存: `if (selectableProfile.hasCustomAvatar)` → `BackupResource.copyFiles()`
- 条件付き依存: `if (selectableProfile.hasCustomAvatar)` → `lazy.logConsole.debug()`
- 参照: `PathUtils.profileDir`, `Services.dns.myHostName`, `lazy.SelectableProfileService.currentProfile`, `selectableProfile.avatar`, `selectableProfile.hasCustomAvatar`, `selectableProfile.name`, `selectableProfile.theme`
- XPCOM: `Services.dns` / `Services.sysinfo`

## SelectableProfileBackupResource.recover()
- 位置: async L113-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getFile()`, `IOUtils.readJSON()`, `JSON.stringify()`, `PathUtils.join()`, `lazy.SelectableProfileService.getAllProfiles()`, `lazy.SelectableProfileService.getProfileByPath()`, `lazy.SelectableProfileService.hasCreatedSelectableProfiles()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `newProfile.setNameAsync()`, `newProfile.setThemeAsync()`, `profilesArray.some()`
- 条件付き依存: `if (!lazy.SelectableProfileService.hasCreatedSelectableProfiles())` → `lazy.logConsole.error()`
- 条件付き依存: `if (!newProfile)` → `lazy.logConsole.error()`
- 条件付き依存: `if (isDupe)` → `lazy.l10n.formatValue()`
- 条件付き依存: `if (isDupe)` → `Date.now()`
- 条件付き依存: `if (metadata.hasCustomAvatar)` → `PathUtils.join()`
- 条件付き依存: `if (metadata.hasCustomAvatar)` → `IOUtils.exists()`
- 条件付き依存: `if (!(await IOUtils.exists(avatarRecoveryFilePath)))` → `lazy.logConsole.error()`
- 条件付き依存: `if (metadata.hasCustomAvatar)` → `File.createFromFileName()`
- 条件付き依存: `if (metadata.hasCustomAvatar)` → `newProfile.setAvatar()`
- 条件付き依存: `if (!(metadata.hasCustomAvatar))` → `newProfile.setAvatar()`
- 参照: `metadata.avatar`, `metadata.deviceName`, `metadata.hasCustomAvatar`, `metadata.name`, `metadata.theme`, `newProfile.id`, `p.id`, `p.name`

## SelectableProfileBackupResource.postRecovery()
- 位置: async L199-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SelectableProfileService.enableTheme()`, `lazy.logConsole.warn()`
- 参照: `postRecoveryEntry?.themeId`

## SelectableProfileBackupResource.measure()
- 位置: async L218-220
- 役割: (未記入)
- 触るとき: (未記入)
