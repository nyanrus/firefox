# browser/components/migration/FirefoxSelectableProfileMigrator.sys.mjs

source: browser/components/migration/FirefoxSelectableProfileMigrator.sys.mjs
source-hash: a90bea865b178bc4615d3b5f3b7ab4a2953bfa30
lines: 104

## <module>
- 役割: (未記入)

## FirefoxSelectableProfileMigrator.key()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_APP_NAME`

## FirefoxSelectableProfileMigrator.getAllProfiles()
- 位置: async L39-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileService.getAllProfiles()`, `SelectableProfileService.startupMigrationInit()`, `rootDir.equals()`, `rootDir.exists()`, `rootDir.isReadable()`
- 条件付き依存: `if ( rootDir.exists() && rootDir.isReadable() && !rootDir.equals(MigrationUtils.profileStartup.directory) )` → `availableProfiles.set()`
- 参照: `MigrationUtils.profileStartup.directory`, `profile.name`, `profile.path`, `profile.rootDir`

## FirefoxSelectableProfileMigrator.getResourcesInternal()
- 位置: L62-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[profiles].filter()`, `resources.concat()`, `super.getResourcesInternal()`
- 参照: `MigrationUtils.resourceTypes`, `types.OTHERDATA`

## savePrefs()
- 位置: L68-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.savePrefFile()`, `currentProfileDir.clone()`, `newPrefsFile.append()`
- XPCOM: `Services.prefs`

## migrate()
- 位置: async L81-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.get()`, `aCallback()`, `savePrefs()`
- 条件付き依存: `if (storeID)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (storeID)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.env` / `Services.prefs`
