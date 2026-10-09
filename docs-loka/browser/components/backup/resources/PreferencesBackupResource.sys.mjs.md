# browser/components/backup/resources/PreferencesBackupResource.sys.mjs

source: browser/components/backup/resources/PreferencesBackupResource.sys.mjs
source-hash: 801d932f1ca14b807a1da49460f2cb63afce17cd
lines: 379

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## PreferencesBackupResource.key()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)

## PreferencesBackupResource.requiresEncryption()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)

## PreferencesBackupResource.dataCollectionPrefs()
- 位置: L44-52
- 役割: (未記入)
- 触るとき: (未記入)

## PreferencesBackupResource.addPrefsToIgnoreInBackup()
- 位置: L62-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getChildList()`, `Services.prefs.getPrefType()`, `kIgnoredPrefs.concat()`, `kNimbusPrefExceptionList.includes()`, `prefsOverrideMap.addEntry()`
- 条件付き依存: `if (Services.prefs.getPrefType(pref) !== Services.prefs.PREF_INVALID)` → `prefsOverrideMap.addEntry()`
- 参照: `Services.prefs.PREF_INVALID`
- XPCOM: `Services.prefs`

## PreferencesBackupResource.getPrefsFromBuffer()
- 位置: L106-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.parsePrefsFromBuffer()`
- XPCOM: `Services.prefs`

## addPref()
- 位置: L110-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prefSet.has()`
- 条件付き依存: `if (!prefSet || prefSet.has(name))` → `prefs.set()`

## PreferencesBackupResource.onError()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)

## PreferencesBackupResource.backup()
- 位置: async L128-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`, `IOUtils.getFile()`, `PathUtils.filename()`, `PathUtils.join()`, `PreferencesBackupResource.addPrefsToIgnoreInBackup()`, `Services.prefs.backupPrefFile()`, `lazy.ExperimentAPI._rsLoader.withUpdateLock()`, `lazy.ExperimentAPI.manager.store.getOriginalPrefValuesForAllActiveEnrollments()`
- 参照: `PathUtils.profileDir`
- XPCOM: `Services.prefs`

## PreferencesBackupResource.recover()
- 位置: async L173-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`, `Date.now()`, `IOUtils.exists()`, `IOUtils.getFile()`, `IOUtils.writeUTF8()`, `Math.round()`, `PathUtils.join()`, `prefsFile.append()`
- 条件付き依存: `if (await IOUtils.exists(RECOVERY_SEARCH_PREF_PATH))` → `IOUtils.readJSON()`
- 条件付き依存: `if (await IOUtils.exists(RECOVERY_SEARCH_PREF_PATH))` → `manifestEntry.profilePath.split(/[/\\]/).at()`
- 条件付き依存: `if (await IOUtils.exists(RECOVERY_SEARCH_PREF_PATH))` → `manifestEntry.profilePath.split()`
- 条件付き依存: `if (ORIGINAL_DIR_NAME)` → `PathUtils.filename()`
- 条件付き依存: `if (ORIGINAL_DIR_NAME)` → `searchPrefs.engines.map()`
- 条件付き依存: `if (engine._metaData.loadPathHash)` → `lazy.SearchUtils.getVerificationHash()`
- 条件付き依存: `if ( engine._metaData.loadPathHash == lazy.SearchUtils.getVerificationHash(loadPath, ORIGINAL_DIR_NAME) )` → `lazy.SearchUtils.getVerificationHash()`
- 条件付き依存: `if (ORIGINAL_DIR_NAME)` → `lazy.SearchUtils.getVerificationHash()`
- 条件付き依存: `if ( searchPrefs.metaData.defaultEngineIdHash && searchPrefs.metaData.defaultEngineIdHash == lazy.SearchUtils.getVerificationHash( searchPrefs.metaData.defaultEn...)` → `lazy.SearchUtils.getVerificationHash()`
- 条件付き依存: `if ( searchPrefs.metaData.privateDefaultEngineIdHash && searchPrefs.metaData.privateDefaultEngineIdHash == lazy.SearchUtils.getVerificationHash( searchPrefs.meta...)` → `lazy.SearchUtils.getVerificationHash()`
- 条件付き依存: `if (await IOUtils.exists(RECOVERY_SEARCH_PREF_PATH))` → `IOUtils.writeJSON()`
- 条件付き依存: `if (await IOUtils.exists(RECOVERY_SEARCH_PREF_PATH))` → `PathUtils.join()`
- 条件付き依存: `if (!lazy.SelectableProfileService.isEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!lazy.SelectableProfileService.isEnabled)` → `IOUtils.writeUTF8()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `PathUtils.join()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `IOUtils.read()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `PreferencesBackupResource.getPrefsFromBuffer()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `Services.prefs.getDefaultBranch()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `lazy.SelectableProfileService.getDBPref()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `backupPrefs.has()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `backupPrefs.get()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `defaults.getBoolPref()`
- 条件付き依存: `if (groupPrefValue && !backupPrefValue)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `lazy.SelectableProfileService.addSelectableProfilePrefs()`
- 参照: `AppConstants.platform`, `PreferencesBackupResource.dataCollectionPrefs`, `Services.prefs.prefsJsPreamble`, `engine._loadPath`, `engine._metaData.loadPathHash`, `lazy.SelectableProfileService.currentProfile`, `lazy.SelectableProfileService.isEnabled`, `manifestEntry.profileDirName`, `manifestEntry.profilePath`, `prefsFile.path`, `searchPrefs.engines`, `searchPrefs.metaData.defaultEngineId`, `searchPrefs.metaData.defaultEngineIdHash`, `searchPrefs.metaData.privateDefaultEngineId`, `searchPrefs.metaData.privateDefaultEngineIdHash`
- XPCOM: `Services.prefs`

## PreferencesBackupResource.measure()
- 位置: async L338-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getDirectorySize()`, `BackupResource.getFileSize()`, `Glean.browserBackup.preferencesSize.set()`, `Number.isInteger()`, `PathUtils.join()`
- 参照: `PathUtils.profileDir`
