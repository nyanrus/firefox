# browser/components/migration/FirefoxProfileMigrator.sys.mjs

source: browser/components/migration/FirefoxProfileMigrator.sys.mjs
source-hash: 97ea4c32aee10eb88d04f037f991f721b368fb7a
lines: 502

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## FirefoxProfileMigrator.key()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_APP_NAME`

## FirefoxProfileMigrator.displayNameL10nID()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)

## FirefoxProfileMigrator.brandImage()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)

## FirefoxProfileMigrator.getAllProfiles()
- 位置: async L61-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/toolkit/profile-service;1" ].getService()`, `rootDir.equals()`, `rootDir.exists()`, `rootDir.isReadable()`
- 条件付き依存: `if ( rootDir.exists() && rootDir.isReadable() && !rootDir.equals(MigrationUtils.profileStartup.directory) )` → `allProfiles.set()`
- 参照: `Ci.nsIToolkitProfileService`, `MigrationUtils.profileStartup.directory`, `profile.name`, `profile.rootDir`, `profileService.profiles`, `rootDir.path`
- XPCOM: [`nsIToolkitProfileService`](../../../toolkit/profile/nsIToolkitProfileService.idl.md) / `@mozilla.org/toolkit/profile-service;1`

## FirefoxProfileMigrator.getSourceProfiles()
- 位置: async L85-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...profiles.values()] .map()`, `[...profiles.values()] .map(p => ({ id: p.id, name: p.name, })) .sort()`, `profiles.values()`, `this.getAllProfiles()`
- 参照: `p.id`, `p.name`

## sorter()
- 位置: L86-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.name .toLocaleLowerCase()`, `a.name .toLocaleLowerCase() .localeCompare()`, `b.name.toLocaleLowerCase()`

## FirefoxProfileMigrator._getFileObject()
- 位置: L102-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dir.clone()`, `file.append()`, `file.exists()`

## FirefoxProfileMigrator.getSourceProfileDir()
- 位置: async L119-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `sourceProfileDir.initWithPath()`
- 参照: `Ci.nsIFile`, `aProfile.id`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/file/local;1`

## FirefoxProfileMigrator.getResources()
- 位置: async L128-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sourceProfileDir.equals()`, `sourceProfileDir.exists()`, `sourceProfileDir.isReadable()`, `this.getResourcesInternal()`, `this.getSourceProfileDir()`
- 参照: `MigrationUtils.profileStartup.directory`

## FirefoxProfileMigrator.getLastUsedDate()
- 位置: L150-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## FirefoxProfileMigrator.getResourcesInternal()
- 位置: L167-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.get()`, `Services.env.set()`, `getFileResource()`
- 条件付き依存: `if (resetSession === RESTORE_SESSION)` → `this._getFileObject()`
- 条件付き依存: `if (resetSession === NEW_SESSION)` → `configureHomepage()`
- 条件付き依存: `if (resetSession === NEW_SESSION)` → `savePrefs()`
- 参照: `MigrationUtils.resourceTypes`, `lazy.PlacesBackups.profileRelativeFolderPath`, `types.COOKIES`, `types.FORMDATA`, `types.HISTORY`, `types.OTHERDATA`, `types.PASSWORDS`, `types.SESSION`
- XPCOM: `Services.env`

## getFileResource()
- 位置: L168-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getFileObject()`
- 条件付き依存: `if (file)` → `files.push()`
- 参照: `files.length`

## FirefoxProfileMigrator.migrate()
- 位置: L181-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `file.copyTo()`

## readOldPrefs()
- 位置: async L191-202
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!_oldRawPrefsMemoized)` → `PathUtils.join()`
- 条件付き依存: `if (!_oldRawPrefsMemoized)` → `IOUtils.exists()`
- 条件付き依存: `if (await IOUtils.exists(prefsPath))` → `IOUtils.readUTF8()`
- 参照: `sourceProfileDir.path`

## savePrefs()
- 位置: L204-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.savePrefFile()`, `currentProfileDir.clone()`, `newPrefsFile.append()`
- XPCOM: `Services.prefs`

## configureHomepage()
- 位置: L213-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- 条件付き依存: `if (resetSession)` → `Services.prefs.setCharPref()`
- 参照: `Services.appinfo.platformBuildID`, `Services.appinfo.platformVersion`
- XPCOM: `Services.appinfo` / `Services.prefs`

## migrate()
- 位置: async L250-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^user_pref\("signon\.storage\.rust\.active",\s*true\)/m.test()`, `aCallback()`, `readOldPrefs()`, `this._getFileObject()`
- 条件付き依存: `if (file)` → `file.copyTo()`
- 条件付き依存: `if ( /^user_pref\("signon\.storage\.rust\.active",\s*true\)/m.test( oldRawPrefs ) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( /^user_pref\("signon\.storage\.rust\.active",\s*true\)/m.test( oldRawPrefs ) )` → `savePrefs()`
- XPCOM: `Services.prefs`

## FirefoxProfileMigrator.migrate()
- 位置: L317-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `aCallback()`, `configureHomepage()`, `currentProfileDir.clone()`, `lazy.SessionMigration.migrate()`, `migrationPromise.then()`, `newSessionFile.append()`, `savePrefs()`, `sessionCheckpoints.copyTo()`
- 参照: `newSessionFile.path`, `sessionFile.path`
- XPCOM: `Services.prefs`

## migrate()
- 位置: async L358-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `aCallback()`
- 条件付き依存: `if (exists)` → `IOUtils.readJSON()`
- 条件付き依存: `if (data && data.accountData && data.accountData.email)` → `IOUtils.copy()`
- 条件付き依存: `if (data && data.accountData && data.accountData.email)` → `PathUtils.join()`
- 条件付き依存: `if (data && data.accountData && data.accountData.email)` → `readOldPrefs()`
- 条件付き依存: `if (data && data.accountData && data.accountData.email)` → `/^user_pref\("services\.sync\.username"/m.test()`
- 条件付き依存: `if (/^user_pref\("services\.sync\.username"/m.test(oldRawPrefs))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (/^user_pref\("services\.sync\.username"/m.test(oldRawPrefs))` → `savePrefs()`
- 参照: `currentProfileDir.path`, `data.accountData`, `data.accountData.email`, `sourceProfileDir.path`
- XPCOM: `Services.prefs`

## migrate()
- 位置: L407-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordMigration()`, `this._getFileObject()`
- 条件付き依存: `if (file)` → `file.copyTo()`

## recordMigration()
- 位置: async L413-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `lazy.ProfileAge()`, `profileTimes.recordProfileReset()`
- 参照: `currentProfileDir.path`

## migrate()
- 位置: async L429-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `dataReportingDir.isDirectory()`, `readOldPrefs()`, `regex.test()`, `this._getFileObject()`
- 条件付き依存: `if (dataReportingDir && dataReportingDir.isDirectory())` → `createSubDir()`
- 条件付き依存: `if (dataReportingDir && dataReportingDir.isDirectory())` → `enumerator.hasMoreElements()`
- 条件付き依存: `if (dataReportingDir && dataReportingDir.isDirectory())` → `file.isDirectory()`
- 条件付き依存: `if (dataReportingDir && dataReportingDir.isDirectory())` → `toCopy.includes()`
- 条件付き依存: `if (dataReportingDir && dataReportingDir.isDirectory())` → `file.copyTo()`
- 条件付き依存: `if (regex.test(oldRawPrefs))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (writePrefs)` → `savePrefs()`
- 参照: `dataReportingDir.directoryEntries`, `enumerator.nextFile`, `file.leafName`
- XPCOM: `Services.prefs`

## createSubDir()
- 位置: L430-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentProfileDir.clone()`, `dir.append()`, `dir.create()`
- 参照: `Ci.nsIFile.DIRECTORY_TYPE`, `lazy.FileUtils.PERMS_DIRECTORY`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md)

## FirefoxProfileMigrator.startupOnlyMigrator()
- 位置: L498-500
- 役割: (未記入)
- 触るとき: (未記入)
