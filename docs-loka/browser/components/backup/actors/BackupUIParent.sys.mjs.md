# browser/components/backup/actors/BackupUIParent.sys.mjs

source: browser/components/backup/actors/BackupUIParent.sys.mjs
source-hash: c20b416f1d159b4288af8b3e93db51c79657e0d0
lines: 376

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## BackupUIParent.constructor()
- 位置: L49-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BackupService.init()`, `super()`
- 参照: `this.#bs`, `this.#obs`

## this.#obs()
- 位置: L57-61
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "backup-service-status-updated")` → `this.sendState()`

## BackupUIParent.actorCreated()
- 位置: L67-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this.#bs.addEventListener()`, `this.#bs.loadEncryptionState()`
- 参照: `this.#obs`
- XPCOM: `Services.obs`

## BackupUIParent.didDestroy()
- 位置: L78-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this.#bs.removeEventListener()`
- 参照: `this.#obs`
- XPCOM: `Services.obs`

## BackupUIParent.handleEvent()
- 位置: L89-93
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "BackupService:StateUpdate")` → `this.sendState()`
- 参照: `event.type`

## BackupUIParent.#triggerCreateBackup()
- 位置: async L102-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `this.#bs.createBackup()`
- 参照: `e.cause`, `lazy.ERRORS.UNKNOWN`

## BackupUIParent.receiveMessage()
- 位置: async L124-364
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !windowGlobal || (!windowGlobal.isInProcess && windowGlobal.remoteType != lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE) )` → `lazy.logConsole.debug()`
- 条件付き依存: `if (message.name == "RequestState")` → `this.sendState()`
- 条件付き依存: `if (message.name == "TriggerCreateBackup")` → `this.#triggerCreateBackup()`
- 条件付き依存: `if (defaultPath)` → `this.#bs.setParentDirPath()`
- 条件付き依存: `if (!this.#bs.state.backupDirPath)` → `lazy.logConsole.error()`
- 条件付き依存: `if (password)` → `this.#bs.loadEncryptionState()`
- 条件付き依存: `if (await this.#bs.loadEncryptionState())` → `this.#bs.disableEncryption()`
- 条件付き依存: `if (password)` → `this.#bs.enableEncryption()`
- 条件付き依存: `if (password)` → `Glean.browserBackup.passwordAdded.record()`
- 条件付き依存: `if (message.name == "EnableScheduledBackups")` → `this.#bs.setScheduledBackups()`
- 条件付き依存: `if (message.name == "EnableScheduledBackups")` → `lazy.logConsole.error()`
- 条件付き依存: `if (message.name == "EnableScheduledBackups")` → `this.#triggerCreateBackup()`
- 条件付き依存: `if (message.name == "DisableScheduledBackups")` → `this.#bs.cleanupBackupFiles()`
- 条件付き依存: `if (message.name == "DisableScheduledBackups")` → `this.#bs.setScheduledBackups()`
- 条件付き依存: `if (message.name == "ShowFilepicker")` → `Cc["@mozilla.org/filepicker;1"].createInstance()`
- 条件付き依存: `if (message.name == "ShowFilepicker")` → `fp.init()`
- 条件付き依存: `if (filter)` → `fp.appendFilters()`
- 条件付き依存: `if (existingBackupPath)` → `PathUtils.parent()`
- 条件付き依存: `if (existingBackupPath)` → `IOUtils.exists()`
- 条件付き依存: `if (await IOUtils.exists(parentPath))` → `Cc["@mozilla.org/file/local;1"].createInstance()`
- 条件付き依存: `if (await IOUtils.exists(parentPath))` → `dir.initWithPath()`
- 条件付き依存: `if (message.name == "ShowFilepicker")` → `fp.open()`
- 条件付き依存: `if (message.name == "ShowFilepicker")` → `this.#bs.getIconFromFilePath()`
- 条件付き依存: `if (message.name == "ShowFilepicker")` → `PathUtils.filename()`
- 条件付き依存: `if (filter)` → `this.#bs.setBackupFileToRestore()`
- 条件付き依存: `if (alsoDeleteLastBackup)` → `this.#bs.deleteLastBackup()`
- 条件付き依存: `if (alsoDeleteLastBackup)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!(filter))` → `this.#bs.setParentDirPath()`
- 条件付き依存: `if (backupFile)` → `this.#bs.loadBackupFileInfo()`
- 条件付き依存: `if (message.name == "FindBackupsInWellKnownLocations")` → `this.#bs.findBackupsInWellKnownLocations()`
- 条件付き依存: `if (message.name == "ProbeDefaultBackupDir")` → `this.#bs.probeDefaultDirAccess()`
- 条件付き依存: `if (message.name == "PrepareRestoreDialog")` → `this.#bs.findBackupsInWellKnownLocations()`
- 条件付き依存: `if (message.name == "RestoreFromBackupChooseFile")` → `this.#bs.filePickerForRestore()`
- 条件付き依存: `if (!backupFile)` → `lazy.logConsole.error()`
- 条件付き依存: `if (message.name == "RestoreFromBackupFile")` → `this.#bs.recoverFromBackupArchive()`
- 条件付き依存: `if (message.name == "RestoreFromBackupFile")` → `lazy.logConsole.error()`
- 条件付き依存: `if (message.name == "RestoreFromBackupFile")` → `this.#bs.setRecoveryError()`
- 条件付き依存: `if (message.name == "EnableEncryption")` → `this.#bs.enableEncryption()`
- 条件付き依存: `if (wasEncrypted)` → `Glean.browserBackup.passwordChanged.record()`
- 条件付き依存: `if (!(wasEncrypted))` → `Glean.browserBackup.passwordAdded.record()`
- 条件付き依存: `if (message.name == "EnableEncryption")` → `lazy.logConsole.error()`
- 条件付き依存: `if (message.name == "EnableEncryption")` → `this.#triggerCreateBackup()`
- 条件付き依存: `if (message.name == "DisableEncryption")` → `this.#bs.disableEncryption()`
- 条件付き依存: `if (message.name == "DisableEncryption")` → `Glean.browserBackup.passwordRemoved.record()`
- 条件付き依存: `if (message.name == "DisableEncryption")` → `lazy.logConsole.error()`
- 条件付き依存: `if (message.name == "DisableEncryption")` → `this.#triggerCreateBackup()`
- 条件付き依存: `if (message.name == "ShowBackupLocation")` → `this.#bs.showBackupLocation()`
- 条件付き依存: `if (message.name == "QuitCurrentProfile")` → `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`
- 条件付き依存: `if (message.name == "QuitCurrentProfile")` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (message.name == "QuitCurrentProfile")` → `Services.startup.quit()`
- 条件付き依存: `if (message.name == "QuitCurrentProfile")` → `lazy.logConsole.error()`
- 条件付き依存: `if (message.name == "SetEmbeddedComponentPersistentData")` → `this.#bs.setEmbeddedComponentPersistentData()`
- 条件付き依存: `if (message.name == "FlushEmbeddedComponentPersistentData")` → `this.#bs.setEmbeddedComponentPersistentData()`
- 条件付き依存: `if (message.name == "ErrorBarDismissed")` → `Services.prefs.setIntPref()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeGetFolder`, `Ci.nsIFilePicker.modeOpen`, `Ci.nsIFilePicker.returnCancel`, `Ci.nsISupportsPRBool`, `Services.startup.eAttemptQuit`, `cancelQuit.data`, `e.cause`, `fp.displayDirectory`, `fp.file.path`, `lazy.BackupService.DEFAULT_PARENT_DIR_PATH`, `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `lazy.ERRORS.NONE`, `lazy.ERRORS.UNKNOWN`, `message.data`, `message.data.password`, `message.name`, `this.#bs.state.backupDirPath`, `this.#bs.state.backupFileToRestore`, `this.#bs.state.embeddedComponentPersistentData?.path`, `this.#bs.state.encryptionEnabled`, `this.browsingContext`, `this.browsingContext.topChromeWindow`, `this.manager`, `windowGlobal.isInProcess`, `windowGlobal.remoteType`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `nsIFilePicker` / [`nsISupportsPRBool`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/file/local;1` / `@mozilla.org/filepicker;1` / `@mozilla.org/supports-PRBool;1` / `Services.obs` / `Services.prefs` / `Services.startup`

## BackupUIParent.sendState()
- 位置: L370-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `this.#bs.state`
