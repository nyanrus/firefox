# browser/components/backup/BackupService.sys.mjs

source: browser/components/backup/BackupService.sys.mjs
source-hash: c7c998d7fb2a5d46540cfd6d692bce0134923164
lines: 5758

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Components.Constructor()`, `Object.freeze()`, `Services.prefs.getBoolPref()`, `Services.urlFormatter.formatURLPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`, `console.createInstance()`

## onUpdateScheduledBackups()
- 位置: L136-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.get()`
- 条件付き依存: `if (bs)` → `bs.onUpdateScheduledBackups()`

## onUpdateLocationDirPath()
- 位置: async L158-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.get()`
- 条件付き依存: `if (bs)` → `bs.onUpdateLocationDirPath()`

## transform()
- 位置: L206-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `JSON.stringify()`, `Object.keys()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## onUpdateBackupErrorCode()
- 位置: L233-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.get()`
- 条件付き依存: `if (bs)` → `bs.onUpdateBackupErrorCode()`

## onUpdateLastBackupFileName()
- 位置: L246-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.get()`
- 条件付き依存: `if (bs)` → `bs.onUpdateLastBackupFileName()`

## BinaryReadableStream.constructor()
- 位置: L294-296
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#channel`

## BinaryReadableStream.start()
- 位置: L304-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/streamConverters;1"].getService()`, `ChromeUtils.generateQI()`, `streamConv.asyncConvertData()`, `this.#channel.asyncOpen()`
- 参照: `Ci.nsIStreamConverterService`
- XPCOM: [`nsIStreamConverterService`](../../../netwerk/streamconv/nsIStreamConverterService.idl.md) / `@mozilla.org/streamConverters;1`

## BinaryReadableStream.onStartRequest()
- 位置: L348-356
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(request instanceof Ci.nsIChannel))` → `Components.Exception()`
- 参照: `Ci.nsIChannel`, `Cr.NS_ERROR_UNEXPECTED`, `request.contentType`, `this._enabled`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md)

## BinaryReadableStream.onDataAvailable()
- 位置: L372-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `binStream.readArrayBuffer()`, `controller.enqueue()`, `textDecoder.decode()`
- 条件付き依存: `if (this._done)` → `Components.Exception()`
- 参照: `Cr.NS_BINDING_ABORTED`, `bytes.buffer`, `lazy.BinaryInputStream`, `this._done`, `this._enabled`

## BinaryReadableStream.onStopRequest()
- 位置: L396-403
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._enabled && !this._done)` → `controller.close()`
- 参照: `this._done`, `this._enabled`

## BinaryReadableStream.onAfterLastPart()
- 位置: L405-416
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._done)` → `controller.error()`
- 参照: `ERRORS.CORRUPTED_ARCHIVE`, `this._done`

## DecoderDecryptorTransformer.constructor()
- 位置: L453-455
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#decryptor`

## DecoderDecryptorTransformer.transform()
- 位置: async L468-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chunks.pop()`, `this.#buffer.split()`, `this.#buffer.split("\n").filter()`, `this.#processChunk()`
- 参照: `this.#buffer`

## DecoderDecryptorTransformer.flush()
- 位置: async L500-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#processChunk()`
- 参照: `this.#buffer`

## DecoderDecryptorTransformer.#processChunk()
- 位置: async L517-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ArchiveUtils.stringToArray()`
- 条件付き依存: `if (this.#decryptor)` → `this.#decryptor.decrypt()`
- 条件付き依存: `if (this.#decryptor)` → `controller.enqueue()`
- 条件付き依存: `if (!(this.#decryptor))` → `controller.enqueue()`
- 参照: `ERRORS.CORRUPTED_ARCHIVE`, `this.#decryptor`

## FileWriterStream.constructor()
- 位置: L569-572
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#decryptor`, `this.#destPath`

## FileWriterStream.start()
- 位置: async L579-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/binaryoutputstream;1"].createInstance()`, `IOUtils.getFile()`, `lazy.FileUtils.openSafeFileOutputStream()`, `this.#binStream.setOutputStream()`
- 参照: `Ci.nsIBinaryOutputStream`, `this.#binStream`, `this.#destPath`, `this.#outStream`
- XPCOM: [`nsIBinaryOutputStream`](../../../xpcom/io/nsIBinaryOutputStream.idl.md) / `@mozilla.org/binaryoutputstream;1`

## FileWriterStream.write()
- 位置: L595-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#binStream.writeByteArray()`

## FileWriterStream.close()
- 位置: L605-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FileUtils.closeSafeFileOutputStream()`, `this.#decryptor.isDone()`
- 条件付き依存: `if (this.#decryptor && !this.#decryptor.isDone())` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#decryptor && !this.#decryptor.isDone())` → `controller.error()`
- 参照: `ERRORS.DECRYPTION_FAILED`, `this.#decryptor`, `this.#outStream`

## FileWriterStream.abort()
- 位置: async L625-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `lazy.FileUtils.closeSafeFileOutputStream()`, `lazy.logConsole.error()`
- 参照: `this.#destPath`, `this.#outStream`

## BackupService.backoffSeconds()
- 位置: L695-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.pow()`
- 参照: `BackupService.#errorRetries`

## BackupService.archiveEnabledStatus()
- 位置: L710-755
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.NimbusFeatures.backupService.getVariable()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(BACKUP_ARCHIVE_ENABLED_PREF_NAME))` → `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## BackupService.restoreEnabledStatus()
- 位置: L762-806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.NimbusFeatures.backupService.getVariable()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(BACKUP_RESTORE_ENABLED_PREF_NAME))` → `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## BackupService.#backupInProgress()
- 位置: L816-821
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#_state.backupInProgress != val)` → `this.stateUpdate()`
- 参照: `this.#_state.backupInProgress`

## BackupService.#backupInProgress()
- 位置: L828-830
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#_state.backupInProgress`

## BackupService.stateUpdate()
- 位置: L836-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## BackupService.setRecoveryError()
- 位置: L845-848
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stateUpdate()`
- 参照: `this.#_state.recoveryErrorCode`

## BackupService.setEmbeddedComponentPersistentData()
- 位置: L858-861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stateUpdate()`
- 参照: `this.#_state.embeddedComponentPersistentData`

## BackupService.DEFAULT_PARENT_DIR_PATH()
- 位置: L1029-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BackupService.docsDirFolderPath?.path`, `BackupService.oneDriveFolderPath?.path`

## BackupService.BACKUP_DIR_NAME()
- 位置: L1042-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!BackupService.#backupFolderName)` → `lazy.DownloadPaths.sanitize()`
- 条件付き依存: `if (!BackupService.#backupFolderName)` → `lazy.gFluentStrings.formatValueSync()`
- 参照: `BackupService.#backupFolderName`

## BackupService.BACKUP_DIR_PREF_NAME()
- 位置: L1056-1058
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.BACKUP_DIR_TRANSLATION()
- 位置: L1069-1074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gFluentStrings.formatValueSync()`
- 参照: `BackupService.#backupFolderName`

## BackupService.BACKUP_FILE_NAME()
- 位置: L1082-1089
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!BackupService.#backupFileName)` → `lazy.DownloadPaths.sanitize()`
- 条件付き依存: `if (!BackupService.#backupFileName)` → `lazy.gFluentStrings.formatValueSync()`
- 参照: `BackupService.#backupFileName`

## BackupService.PROFILE_FOLDER_NAME()
- 位置: L1097-1099
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.SNAPSHOTS_FOLDER_NAME()
- 位置: L1107-1109
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.MANIFEST_FILE_NAME()
- 位置: L1116-1118
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.MANIFEST_SCHEMA()
- 位置: L1135-1144
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!BackupService.#manifestSchemaPromise)` → `BackupService.getSchemaForVersion()`
- 参照: `BackupService.#manifestSchemaPromise`, `SCHEMAS.BACKUP_MANIFEST`, `lazy.ArchiveUtils.SCHEMA_VERSION`

## BackupService.POST_RECOVERY_FILE_NAME()
- 位置: L1152-1154
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.ARCHIVE_ENCRYPTION_STATE_FILE()
- 位置: L1162-1164
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.SCHEMAS()
- 位置: L1171-1173
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.RECOVERY_ZIP_FILE_NAME()
- 位置: L1181-1183
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.STATUS_OBSERVER_PREFS()
- 位置: L1192-1199
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.getSchemaForVersion()
- 位置: async L1210-1226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`, `response.json()`
- 参照: `ERRORS.UNKNOWN`, `SCHEMAS.ARCHIVE_JSON_BLOCK`, `SCHEMAS.BACKUP_MANIFEST`

## BackupService.COMPRESSION_LEVEL()
- 位置: L1233-1235
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIZipWriter.COMPRESSION_BEST`
- XPCOM: `nsIZipWriter`

## BackupService.ARCHIVE_TEMPLATE()
- 位置: L1243-1245
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.RECOVERY_OSKEYSTORE_LABEL()
- 位置: L1256-1258
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_APP_BASENAME`

## BackupService.WRITE_BACKUP_LOCK_NAME()
- 位置: L1266-1268
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.REGENERATION_DEBOUNCE_RATE_MS()
- 位置: L1276-1278
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.oneDriveFolderPath()
- 位置: L1285-1294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `oneDriveDir.exists()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## BackupService.docsDirFolderPath()
- 位置: L1302-1312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `lazy.logConsole.warn()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## BackupService.probeDefaultDirAccess()
- 位置: async L1323-1333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`
- 参照: `BackupService.DEFAULT_PARENT_DIR_PATH`

## BackupService.init()
- 位置: L1346-1360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings.profileRestore.submit()`, `this.#instance.checkForPostRecovery()`, `this.#instance.initBackupScheduler()`, `this.#instance.initStatusObservers()`
- 参照: `this.#instance`

## BackupService.uninit()
- 位置: L1368-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#instance)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#instance)` → `this.#instance.uninitBackupScheduler()`
- 条件付き依存: `if (this.#instance)` → `this.#instance.uninitStatusObservers()`
- 参照: `this.#instance`

## BackupService.get()
- 位置: L1385-1393
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ERRORS.UNINITIALIZED`, `this.#instance`

## BackupService.constructor()
- 位置: L1401-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `lazy.logConsole.debug()`, `super()`, `this.#postRecoveryPromise.then()`, `this.#resources.set()`, `this.#setRestoredProfileDataMetric()`
- 条件付き依存: `if ( !this.#backupWriteAbortController.signal.aborted && this.archiveEnabledStatus.enabled )` → `this.createBackupOnIdleDispatch()`
- 参照: `BackupService.REGENERATION_DEBOUNCE_RATE_MS`, `lazy.DeferredTask`, `resource.key`, `this.#backupWriteAbortController`, `this.#backupWriteAbortController.signal.aborted`, `this.#lastSeenArchiveStatus`, `this.#lastSeenRestoreStatus`, `this.#postRecoveryPromise`, `this.#postRecoveryResolver`, `this.#regenerationDebouncer`, `this.archiveEnabledStatus`, `this.archiveEnabledStatus.enabled`, `this.restoreEnabledStatus`

## BackupService.postRecoveryComplete()
- 位置: L1444-1446
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#postRecoveryPromise`

## BackupService.#setRestoredProfileDataMetric()
- 位置: L1458-1497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserBackup.restoredProfileData.set()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`
- 条件付き依存: `if (!backupMetadata)` → `JSON.parse()`
- 条件付き依存: `if (!backupMetadata)` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (payload.is_restored)` → `new Date(backupMetadata.date).getTime()`
- 参照: `backupMetadata.appName`, `backupMetadata.appVersion`, `backupMetadata.buildID`, `backupMetadata.date`, `backupMetadata.healthTelemetryEnabled`, `backupMetadata.intermediateProfileCreationDate`, `backupMetadata.legacyClientID`, `backupMetadata.osBuildNumber`, `backupMetadata.osName`, `backupMetadata.osVersion`, `backupMetadata.restoreSource`, `payload.backup_app_name`, `payload.backup_app_version`, `payload.backup_build_id`, `payload.backup_legacy_client_id`, `payload.backup_os_build_number`, `payload.backup_os_name`, `payload.backup_os_version`, `payload.backup_timestamp`, `payload.intermediate_profile_creation_date`, `payload.is_restored`, `payload.restore_source`
- XPCOM: `Services.prefs`

## BackupService.state()
- 位置: L1506-1520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.freeze()`, `Object.keys()`, `structuredClone()`
- 条件付き依存: `if ( !Object.keys(this.#_state.defaultParent).length || !this.#_state.defaultParent.path )` → `PathUtils.filename()`
- 条件付き依存: `if ( !Object.keys(this.#_state.defaultParent).length || !this.#_state.defaultParent.path )` → `this.getIconFromFilePath()`
- 参照: `BackupService.DEFAULT_PARENT_DIR_PATH`, `Object.keys(this.#_state.defaultParent).length`, `this.#_state`, `this.#_state.defaultParent`, `this.#_state.defaultParent.path`

## BackupService.resolveArchiveDestFolderPath()
- 位置: async L1530-1550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.makeDirectory()`, `Services.sysinfo.getProperty()`, `lazy.logConsole.warn()`
- 条件付き依存: `if (Services.sysinfo.getProperty("name") === "Windows_NT")` → `this.#createDesktopIni()`
- 参照: `ERRORS.FILE_SYSTEM_ERROR`
- XPCOM: `Services.sysinfo`

## BackupService.resolveDownloadLink()
- 位置: async L1570-1584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## BackupService.createAndPopulateStagingFolder()
- 位置: async L1607-1768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.#resources.values()).sort()`, `BackupResource.getDirectorySize()`, `Glean.browserBackup.totalBackupSize.accumulate()`, `IOUtils.makeDirectory()`, `IOUtils.writeJSON()`, `MeasurementUtils.fuzzByteSize()`, `PathUtils.join()`, `lazy.JsonSchema.validate()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `lazy.logConsole.log()`, `new resourceClass().backup()`, `this.#createBackupManifest()`, `this.#finalizeStagingFolder()`, `this.#prepareStagingFolder()`, `this.#resources.values()`
- 条件付き依存: `if (encState === undefined)` → `this.loadEncryptionState()`
- 条件付き依存: `if (!(encState === undefined))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (resourceClass.requiresEncryption && !encryptionEnabled)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!resourceClass.canBackupResource)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (manifestEntry === undefined)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!(manifestEntry === undefined))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!schemaValidationResult.valid)` → `lazy.logConsole.error()`
- 参照: `BACKUP_STEPS.CREATE_BACKUP_CREATE_BACKUPS_FOLDER`, `BACKUP_STEPS.CREATE_BACKUP_CREATE_MANIFEST`, `BACKUP_STEPS.CREATE_BACKUP_CREATE_STAGING_FOLDER`, `BACKUP_STEPS.CREATE_BACKUP_FINALIZE_STAGING`, `BACKUP_STEPS.CREATE_BACKUP_LOAD_ENCSTATE`, `BACKUP_STEPS.CREATE_BACKUP_RUN_BACKUP`, `BACKUP_STEPS.CREATE_BACKUP_VERIFY_MANIFEST`, `BACKUP_STEPS.CREATE_BACKUP_WRITE_MANIFEST`, `BackupService.MANIFEST_FILE_NAME`, `BackupService.MANIFEST_SCHEMA`, `BackupService.PROFILE_FOLDER_NAME`, `BackupService.SNAPSHOTS_FOLDER_NAME`, `a.priority`, `b.priority`, `manifest.resources`, `resourceClass.canBackupResource`, `resourceClass.key`, `resourceClass.requiresEncryption`, `schemaValidationResult.valid`

## BackupService.createBackup()
- 位置: async L1801-1972
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getFileSize()`, `BackupService.maybeAddToEnabledListPref()`, `Date.now()`, `Glean.browserBackup.backupStart.record()`, `Glean.browserBackup.compressedArchiveSize.accumulate()`, `Glean.browserBackup.created.record()`, `Glean.browserBackup.error.record()`, `Glean.browserBackup.totalBackupTime.cancel()`, `Glean.browserBackup.totalBackupTime.start()`, `Glean.browserBackup.totalBackupTime.stopAndAccumulate()`, `IOUtils.remove()`, `JSON.stringify()`, `Math.floor()`, `MeasurementUtils.fuzzByteSize()`, `PathUtils.join()`, `Services.prefs.clearUserPref()`, `Services.prefs.setIntPref()`, `Services.prefs.setStringPref()`, `String()`, `lazy.logConsole.debug()`, `lazy.logConsole.log()`, `locks.request()`, `this.#compressStagingFolder()`, `this.#compressStagingFolder( stagingPath, backupDirPath ).finally()`, `this.classifyLocationForTelemetry()`, `this.createAndPopulateStagingFolder()`, `this.createArchive()`, `this.finalizeSingleFileArchive()`, `this.resolveArchiveDestFolderPath()`, `this.stateUpdate()`
- 条件付き依存: `if (!status.enabled)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#backupInProgress)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (encState === undefined)` → `this.loadEncryptionState()`
- 参照: `BACKUP_STEPS.CREATE_BACKUP_COMPRESS_STAGING`, `BACKUP_STEPS.CREATE_BACKUP_CREATE_ARCHIVE`, `BACKUP_STEPS.CREATE_BACKUP_ENTRYPOINT`, `BACKUP_STEPS.CREATE_BACKUP_FINALIZE_ARCHIVE`, `BACKUP_STEPS.CREATE_BACKUP_RESOLVE_DESTINATION`, `BackupService.#errorRetries`, `BackupService.ARCHIVE_TEMPLATE`, `BackupService.WRITE_BACKUP_LOCK_NAME`, `ERRORS.NONE`, `ERRORS.UNKNOWN`, `PathUtils.profileDir`, `e.cause`, `lazy.backupDirPref`, `manifest.meta`, `result.currentStep`, `result.error`, `status.enabled`, `status.reason`, `this.#_state.encryptionEnabled`, `this.#_state.lastBackupDate`, `this.#backupInProgress`, `this.#backupWriteAbortController.signal`, `this.archiveEnabledStatus`
- XPCOM: `Services.prefs`

## BackupService.classifyLocationForTelemetry()
- 位置: L1987-2018
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Services.dirsvc.get()`, `candidate.equals()`, `lazy.nsLocalFile()`
- 参照: `Ci.nsIFile`, `e.name`, `lazy.nsLocalFile(path).parent?.parent`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## BackupService.generateArchiveDateSuffix()
- 位置: L2029-2045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: ``${date.getDate()}`.padStart()`, ``${date.getHours()}`.padStart()`, ``${date.getMilliseconds()}`.padStart()`, ``${date.getMinutes()}`.padStart()`, ``${date.getMonth() + 1}`.padStart()`, ``${date.getSeconds()}`.padStart()`, `date.getDate()`, `date.getFullYear()`, `date.getFullYear().toString()`, `date.getHours()`, `date.getMilliseconds()`, `date.getMinutes()`, `date.getMonth()`, `date.getSeconds()`

## BackupService.finalizeSingleFileArchive()
- 位置: async L2062-2112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.move()`, `PathUtils.filename()`, `PathUtils.join()`, `Services.prefs.setStringPref()`, `childFileName.endsWith()`, `childFileName.startsWith()`, `lazy.logConsole.log()`, `nameParts.join()`, `this.generateArchiveDateSuffix()`
- 条件付き依存: `if (storeID)` → `nameParts.push()`
- 条件付き依存: `if (childFileName == FILENAME)` → `lazy.logConsole.warn()`
- 条件付き依存: `if ( childFileName.startsWith(FILENAME_PREFIX) && childFileName.endsWith(".html") )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( childFileName.startsWith(FILENAME_PREFIX) && childFileName.endsWith(".html") )` → `IOUtils.remove()`
- 参照: `BackupService.BACKUP_FILE_NAME`, `lazy.SelectableProfileService.storeID`, `metadata.date`, `metadata.profileName`
- XPCOM: `Services.prefs`

## BackupService.#prepareStagingFolder()
- 位置: async L2125-2193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.getChildren()`, `PathUtils.join()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (folderEntries)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (folderEntries)` → `IOUtils.remove()`
- 条件付き依存: `if (folderEntries)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (folderEntries)` → `unremovableContents.push()`
- 条件付き依存: `if (!(await IOUtils.exists(potentialStagingPath)))` → `IOUtils.makeDirectory()`
- 参照: `ERRORS.FILE_SYSTEM_ERROR`, `e.stack`, `error.stack`, `error.unremovableContents`, `lazy.maximumNumberOfUnremovableStagingItems`

## BackupService.#compressStagingFolder()
- 位置: async L2208-2242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getDirectory()`, `IOUtils.getFile()`, `PathUtils.filename()`, `PathUtils.join()`, `lazy.logConsole.log()`, `this.#compressChildren()`, `writer.close()`, `writer.processQueue()`
- 参照: `lazy.ZipWriter`

## BackupService.onStartRequest()
- 位置: L2229-2231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`

## BackupService.onStopRequest()
- 位置: L2232-2235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.log()`, `resolve()`

## BackupService.#compressChildren()
- 位置: async L2257-2277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.stat()`
- 条件付き依存: `if (childState.type == "directory")` → `this.#compressChildren()`
- 条件付き依存: `if (!(childState.type == "directory"))` → `IOUtils.getFile()`
- 条件付き依存: `if (!(childState.type == "directory"))` → `childFile.getRelativePath()`
- 条件付き依存: `if (!(childState.type == "directory"))` → `writer.addEntryFile()`
- 参照: `BackupService.COMPRESSION_LEVEL`, `childState.type`

## BackupService.decompressRecoveryFile()
- 位置: async L2289-2326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getFile()`, `IOUtils.remove()`, `lazy.logConsole.error()`, `lazy.logConsole.log()`, `recoveryArchive.close()`, `recoveryArchive.test()`, `this.#decompressChildren()`
- 参照: `ERRORS.CORRUPTED_ARCHIVE`, `ERRORS.DECOMPRESSION_FAILED`, `e.message`, `lazy.ZipReader`

## BackupService.#decompressChildren()
- 位置: async L2341-2381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reader.findEntries()`, `reader.getEntry()`
- 条件付き依存: `if (childEntry.isDirectory)` → `this.#decompressChildren()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `reader.getInputStream()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `childEntryName.split()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `PathUtils.join()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `IOUtils.getFile()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `Cc[ "@mozilla.org/network/file-output-stream;1" ].createInstance()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `outputStream.init()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `lazy.NetUtil.asyncCopy()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `outputStream.close()`
- 条件付き依存: `if (!(childEntry.isDirectory))` → `resolve()`
- 参照: `Ci.nsIFileOutputStream`, `Ci.nsIFileOutputStream.DEFER_OPEN`, `childEntry.isDirectory`
- XPCOM: [`nsIFileOutputStream`](../../../netwerk/base/nsIFileStreams.idl.md) / `@mozilla.org/network/file-output-stream;1`

## BackupService.renderTemplate()
- 位置: async L2398-2506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `fetch()`, `lazy.gDOMLocalization.setArgs()`, `lazy.gDOMLocalization.setAttributes()`, `lazy.gDOMLocalization.translateFragment()`, `logoResponse.blob()`, `new DOMParser().parseFromString()`, `new Date().getTime()`, `new Date(backupMetadata.date).getTime()`, `reader.addEventListener()`, `reader.readAsDataURL()`, `resolve()`, `scriptResponse.text()`, `serializer .serializeToString()`, `serializer .serializeToString(templateDOM) .replace()`, `serializer .serializeToString(templateDOM) .replace("{{styles}}", stylesText) .replace()`, `stylesResponse.text()`, `stylesText.includes()`, `stylesText.replace()`, `supportURI.searchParams.set()`, `templateDOM.documentElement.setAttribute()`, `templateDOM.querySelector()`, `templateResponse.text()`, `this.resolveDownloadLink()`
- 参照: `AppConstants.MOZ_UPDATE_CHANNEL`, `ERRORS.UNKNOWN`, `Services.locale.appLocaleAsBCP47`, `backupMetadata.date`, `backupMetadata.machineName`, `creationDeviceNode.textContent`, `downloadLink.href`, `logoNode.src`, `reader.result`, `supportLink.href`, `supportURI.href`, `templateDOM.documentElement`
- XPCOM: `Services.locale` / `Services.urlFormatter`

## BackupService.createArchive()
- 位置: async L2532-2587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `this.renderTemplate()`, `worker .post()`, `worker.terminate()`
- 参照: `BackupError.fromMsg`, `BackupError.name`, `ERRORS.UNKNOWN`, `encState.backupAuthKey`, `encState.nonce`, `encState.publicKey`, `encState.salt`, `encState.wrappedSecrets`, `lazy.ArchiveUtils.ARCHIVE_CHUNK_MAX_BYTES_SIZE`, `lazy.BasePromiseWorker`, `options.chunkSize`, `worker.ExceptionHandlers`

## BackupService.#createExtractionChannel()
- 位置: L2601-2618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/input-stream-channel;1"] .createInstance()`, `Cc["@mozilla.org/network/input-stream-channel;1"] .createInstance(Ci.nsIInputStreamChannel) .QueryInterface()`, `channel.setURI()`, `lazy.NetUtil.newChannel()`
- 参照: `Ci.nsIChannel`, `Ci.nsIInputStreamChannel`, `channel.contentStream`, `channel.contentType`, `channel.loadInfo`, `httpChan.URI`, `httpChan.loadInfo`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIInputStreamChannel`](../../../netwerk/base/nsIInputStreamChannel.idl.md) / `@mozilla.org/network/input-stream-channel;1`

## BackupService.#extractJSONFromArchive()
- 位置: async L2634-2785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/network/file-input-stream;1" ].createInstance()`, `Cc["@mozilla.org/streamConverters;1"].getService()`, `ChromeUtils.generateQI()`, `extractionChannel.asyncOpen()`, `fileInputStream.init()`, `fileInputStream.seek()`, `streamConv.asyncConvertData()`, `this.#createExtractionChannel()`
- 参照: `Ci.nsIFileInputStream`, `Ci.nsIFileInputStream.CLOSE_ON_EOF`, `Ci.nsISeekableStream.NS_SEEK_SET`, `Ci.nsIStreamConverterService`
- XPCOM: [`nsIFileInputStream`](../../../netwerk/base/nsIFileStreams.idl.md) / [`nsISeekableStream`](../../../xpcom/io/nsISeekableStream.idl.md) / [`nsIStreamConverterService`](../../../netwerk/streamconv/nsIStreamConverterService.idl.md) / `@mozilla.org/network/file-input-stream;1` / `@mozilla.org/streamConverters;1`

## BackupService.onStartRequest()
- 位置: L2696-2704
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(request instanceof Ci.nsIChannel))` → `Components.Exception()`
- 参照: `Ci.nsIChannel`, `Cr.NS_ERROR_UNEXPECTED`, `request.contentType`, `this._enabled`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md)

## BackupService.onDataAvailable()
- 位置: L2720-2739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `binStream.readArrayBuffer()`, `textDecoder.decode()`
- 条件付き依存: `if (this._done)` → `Components.Exception()`
- 参照: `Cr.NS_BINDING_ABORTED`, `lazy.BinaryInputStream`, `this._buffer`, `this._done`, `this._enabled`

## BackupService.onStopRequest()
- 位置: L2744-2761
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._enabled && !this._done)` → `JSON.parse()`
- 条件付き依存: `if (this._enabled && !this._done)` → `resolve()`
- 条件付き依存: `if (this._enabled && !this._done)` → `reject()`
- 参照: `ERRORS.CORRUPTED_ARCHIVE`, `this._buffer`, `this._done`, `this._enabled`

## BackupService.onAfterLastPart()
- 位置: L2763-2774
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._done)` → `reject()`
- 参照: `ERRORS.CORRUPTED_ARCHIVE`, `this._done`

## BackupService.createBinaryReadableStream()
- 位置: async L2801-2819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/network/file-input-stream;1" ].createInstance()`, `fileInputStream.init()`, `fileInputStream.seek()`, `this.#createExtractionChannel()`
- 参照: `Ci.nsIFileInputStream`, `Ci.nsIFileInputStream.CLOSE_ON_EOF`, `Ci.nsISeekableStream.NS_SEEK_SET`
- XPCOM: [`nsIFileInputStream`](../../../netwerk/base/nsIFileStreams.idl.md) / [`nsISeekableStream`](../../../xpcom/io/nsISeekableStream.idl.md) / `@mozilla.org/network/file-input-stream;1`

## BackupService.sampleArchive()
- 位置: async L2846-2942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.getSchemaForVersion()`, `IOUtils.exists()`, `IOUtils.getFile()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#extractJSONFromArchive()`, `validator.addSchema()`, `validator.validate()`, `worker .post()`, `worker .post("parseArchiveHeader", [archivePath]) .catch()`, `worker.terminate()`
- 条件付き依存: `if (!schemaValidationResult.valid)` → `lazy.logConsole.error()`
- 参照: `BackupError.fromMsg`, `BackupError.name`, `ERRORS.CORRUPTED_ARCHIVE`, `ERRORS.UNKNOWN`, `ERRORS.UNSUPPORTED_BACKUP_VERSION`, `SCHEMAS.ARCHIVE_JSON_BLOCK`, `SCHEMAS.BACKUP_MANIFEST`, `archiveJSON.encConfig`, `archiveJSON.version`, `lazy.ArchiveUtils.SCHEMA_VERSION`, `lazy.BasePromiseWorker`, `lazy.JsonSchema.Validator`, `schemaValidationResult.valid`, `worker.ExceptionHandlers`

## BackupService.extractCompressedSnapshotFromArchive()
- 位置: async L2967-3026
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getFile()`, `IOUtils.remove()`, `archiveStream.pipeThrough()`, `archiveStream.pipeThrough(binaryDecoder).pipeTo()`, `this.createBinaryReadableStream()`, `this.sampleArchive()`
- 条件付き依存: `if (isEncrypted)` → `lazy.ArchiveDecryptor.initialize()`
- 条件付き依存: `if (decryptor)` → `lazy.nativeOSKeyStore.asyncRecoverSecret()`
- 参照: `BackupService.RECOVERY_OSKEYSTORE_LABEL`, `ERRORS.CORRUPTED_ARCHIVE`, `ERRORS.UNAUTHORIZED`, `decryptor.OSKeyStoreSecret`, `e?.message`

## BackupService.#finalizeStagingFolder()
- 位置: async L3038-3100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.getChildren()`, `IOUtils.move()`, `PathUtils.join()`, `PathUtils.parent()`, `currentDateISO.replace()`, `dateISOStripped.replaceAll()`, `existingBackupPath.match()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `new Date().toISOString()`
- 条件付き依存: `if (!(await IOUtils.exists(stagingPath)))` → `lazy.logConsole.error()`
- 条件付き依存: `if ( existingBackupPath !== renamedBackupPath && existingBackupPath.match(expectedFormatRegex) )` → `IOUtils.remove()`
- 条件付き依存: `if ( existingBackupPath !== renamedBackupPath && existingBackupPath.match(expectedFormatRegex) )` → `lazy.logConsole.debug()`
- 参照: `ERRORS.FILE_SYSTEM_ERROR`

## BackupService.#createBackupManifest()
- 位置: async L3109-3166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(() => { try { return Services.sysinfo.getProperty("build"); } catch { return null; } })()`, `Cc["@mozilla.org/toolkit/profile-service;1"].getService()`, `Services.prefs.getBoolPref()`, `Services.sysinfo.get()`, `Services.sysinfo.getProperty()`, `lazy.ClientID.getClientID()`, `lazy.ClientID.getProfileGroupID()`, `lazy.UIState.get()`, `lazy.fxAccounts.device.getLocalName()`, `new Date().toISOString()`
- 条件付き依存: `if (!profileSvc.currentProfile)` → `PathUtils.split(PathUtils.profileDir).at()`
- 条件付き依存: `if (!profileSvc.currentProfile)` → `PathUtils.split()`
- 条件付き依存: `if (!profileSvc.currentProfile)` → `profileFolder.substring()`
- 条件付き依存: `if (!profileSvc.currentProfile)` → `profileFolder.indexOf()`
- 参照: `AppConstants.MOZ_APP_NAME`, `AppConstants.MOZ_APP_VERSION`, `AppConstants.MOZ_BUILDID`, `Ci.nsIToolkitProfileService`, `PathUtils.profileDir`, `Services.dns.myHostName`, `fxaState.email`, `fxaState.status`, `fxaState.uid`, `lazy.ArchiveUtils.SCHEMA_VERSION`, `lazy.SelectableProfileService.currentProfile`, `lazy.SelectableProfileService.currentProfile.name`, `lazy.UIState.STATUS_SIGNED_IN`, `meta.accountEmail`, `meta.accountID`, `profileSvc.currentProfile`, `profileSvc.currentProfile.name`
- XPCOM: [`nsIToolkitProfileService`](../../../toolkit/profile/nsIToolkitProfileService.idl.md) / `@mozilla.org/toolkit/profile-service;1` / `Services.dns` / `Services.prefs` / `Services.sysinfo`

## BackupService.recoverFromBackupArchive()
- 位置: async L3211-3430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserBackup.restoreComplete.record()`, `Glean.browserBackup.restoreFailed.record()`, `Glean.browserBackup.restoreStarted.record()`, `GleanPings.profileRestore.submit()`, `IOUtils.remove()`, `PathUtils.join()`, `Services.obs.notifyObservers()`, `errorString()`, `ex.message.substring()`, `lazy.ProfileAge()`, `lazy.logConsole.warn()`, `this.#readAndValidateManifest()`, `this.decompressRecoveryFile()`, `this.extractCompressedSnapshotFromArchive()`, `this.stateUpdate()`
- 条件付き依存: `if (this.#_state.recoveryInProgress)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (!(!lazy.SelectableProfileService.isEnabled))` → `lazy.SelectableProfileService.hasCreatedSelectableProfiles()`
- 条件付き依存: `if ( !lazy.SelectableProfileService.hasCreatedSelectableProfiles() && !replacingLegacyWithLegacy )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( !lazy.SelectableProfileService.hasCreatedSelectableProfiles() && !replacingLegacyWithLegacy )` → `lazy.SelectableProfileService.maybeSetupDataStore()`
- 条件付き依存: `if (lazy.SelectableProfileService.currentProfile)` → `this.recoverFromSnapshotFolderIntoSelectableProfile()`
- 条件付き依存: `if (!(lazy.SelectableProfileService.currentProfile))` → `this.recoverFromSnapshotFolder()`
- 条件付き依存: `if (replaceCurrentProfile)` → `this.deleteAndQuitCurrentSelectableProfile()`
- 条件付き依存: `if (replaceCurrentProfile)` → `lazy.logConsole.error()`
- 条件付き依存: `if (recoveryCode)` → `lazy.nativeOSKeyStore.asyncDeleteSecret()`
- 参照: `BackupService.PROFILE_FOLDER_NAME`, `BackupService.RECOVERY_OSKEYSTORE_LABEL`, `BackupService.RECOVERY_ZIP_FILE_NAME`, `DefaultBackupResources.SelectableProfileBackupResource.key`, `ERRORS.PROFILE_CREATION_FAILED`, `ERRORS.RECOVERY_FAILED`, `PathUtils.profileDir`, `RESTORE_STEPS.RESTORE_CREATE_PROFILE`, `RESTORE_STEPS.RESTORE_DECOMPRESS`, `RESTORE_STEPS.RESTORE_ENTRYPOINT`, `RESTORE_STEPS.RESTORE_EXTRACT_SNAPSHOT`, `RESTORE_STEPS.RESTORE_FINALIZE`, `RESTORE_STEPS.RESTORE_PROFILE_SETUP`, `RESTORE_STEPS.RESTORE_READ_MANIFEST`, `ex.cause`, `ex.message`, `ex.resourceKey`, `ex.restoreStep`, `lazy.SelectableProfileService.currentProfile`, `lazy.SelectableProfileService.isEnabled`, `manifest.meta?.isSelectableProfile`, `manifest.resources`, `profileAge.created`, `status.enabled`, `status.reason`, `this.#_state.backupFileInfo?.appVersion`, `this.#_state.backupFileInfo?.osBuildNumber`, `this.#_state.backupFileInfo?.osName`, `this.#_state.backupFileInfo?.osVersion`, `this.#_state.intermediateProfileCreationDate`, `this.#_state.recoveryErrorCode`, `this.#_state.recoveryInProgress`, `this.#_state.restoreID`, `this.#_state.restoreSource`, `this.restoreEnabledStatus`
- XPCOM: `Services.obs`

## BackupService.deleteAndQuitCurrentSelectableProfile()
- 位置: async L3440-3471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`, `lazy.SelectableProfileService.deleteCurrentProfile()`, `lazy.SelectableProfileService.hasCreatedSelectableProfiles()`, `lazy.logConsole.error()`
- 条件付き依存: `if (!lazy.SelectableProfileService.hasCreatedSelectableProfiles())` → `lazy.logConsole.warn()`
- 条件付き依存: `if (shouldQuit)` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsISupportsPRBool`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs` / `Services.startup`

## BackupService.#readAndValidateManifest()
- 位置: async L3482-3559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.getSchemaForVersion()`, `IOUtils.readJSON()`, `PathUtils.join()`, `Services.vc.compare()`, `lazy.JsonSchema.validate()`
- 条件付き依存: `if (!schemaValidationResult.valid)` → `lazy.logConsole.error()`
- 参照: `AppConstants.MOZ_APP_NAME`, `AppConstants.MOZ_APP_VERSION`, `BackupService.MANIFEST_FILE_NAME`, `ERRORS.CORRUPTED_ARCHIVE`, `ERRORS.UNSUPPORTED_APPLICATION`, `ERRORS.UNSUPPORTED_BACKUP_VERSION`, `SCHEMAS.BACKUP_MANIFEST`, `e.message`, `lazy.ArchiveUtils.SCHEMA_VERSION`, `manifest.isSelectableProfile`, `manifest.meta`, `manifest.version`, `meta.appName`, `meta.appVersion`, `schemaValidationResult.valid`
- XPCOM: `Services.vc`

## BackupService.#getLegacyThemeId()
- 位置: async L3567-3586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DefaultBackupResources.PreferencesBackupResource.getPrefsFromBuffer()`, `IOUtils.read()`, `PathUtils.join()`, `lazy.logConsole.warn()`, `prefs.get()`
- 参照: `DefaultBackupResources.PreferencesBackupResource.key`

## BackupService.#recoverResources()
- 位置: async L3604-3655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `new resourceClass().recover()`, `this.#resources.get()`
- 条件付き依存: `if (!resourceClass)` → `lazy.logConsole.error()`
- 条件付き依存: `if (resourceClass.requiresEncryption && !wasEncrypted)` → `lazy.logConsole.warn()`
- 参照: `ERRORS.RESOURCE_RECOVERY_FAILED`, `e.message`, `e.resourceKey`, `err.resourceKey`, `manifest.resources`, `resourceClass.requiresEncryption`

## BackupService.#writePostRecoveryData()
- 位置: async L3664-3670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeJSON()`, `PathUtils.join()`
- 参照: `BackupService.POST_RECOVERY_FILE_NAME`

## BackupService.recoverFromSnapshotFolder()
- 位置: async L3713-3831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/toolkit/profile-service;1"].getService()`, `IOUtils.getDirectory()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `profileSvc.asyncFlush()`, `profileSvc.createUniqueProfile()`, `this.#recoverResources()`, `this.#writePostRecoveryData()`
- 条件付き依存: `if (!manifest)` → `this.#readAndValidateManifest()`
- 条件付き依存: `if (profileSvc.currentProfile)` → `profileSvc.currentProfile.name.startsWith()`
- 条件付き依存: `if (shouldLaunch)` → `Services.startup.createInstanceWithProfile()`
- 参照: `Ci.nsIToolkitProfileService`, `ERRORS.PROFILE_CREATION_FAILED`, `ERRORS.RECOVERY_FAILED`, `RESTORE_STEPS.RESTORE_CONFIGURE_PROFILE`, `RESTORE_STEPS.RESTORE_CREATE_PROFILE`, `RESTORE_STEPS.RESTORE_LAUNCH_PROFILE`, `RESTORE_STEPS.RESTORE_RECOVER_RESOURCES`, `RESTORE_STEPS.RESTORE_WRITE_POST_RECOVERY`, `e.message`, `err.restoreStep`, `manifest.meta.profileName`, `postRecovery.backupServiceInternal`, `profile.rootDir.path`, `profileSvc.currentProfile`, `profileSvc.currentProfile.name`, `profileSvc.defaultProfile`, `this.#_state.backupFileInfo.appName`, `this.#_state.backupFileInfo.appVersion`, `this.#_state.backupFileInfo.buildID`, `this.#_state.backupFileInfo.date`, `this.#_state.backupFileInfo.healthTelemetryEnabled`, `this.#_state.backupFileInfo.legacyClientID`, `this.#_state.backupFileInfo.osBuildNumber`, `this.#_state.backupFileInfo.osName`, `this.#_state.backupFileInfo.osVersion`, `this.#_state.intermediateProfileCreationDate`, `this.#_state.restoreID`, `this.#_state.restoreSource`
- XPCOM: [`nsIToolkitProfileService`](../../../toolkit/profile/nsIToolkitProfileService.idl.md) / `@mozilla.org/toolkit/profile-service;1` / `Services.startup`

## BackupService.recoverFromSnapshotFolderIntoSelectableProfile()
- 位置: async L3880-4038
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SelectableProfileService.createNewProfile()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#recoverResources()`, `this.#writePostRecoveryData()`
- 条件付き依存: `if (!manifest)` → `this.#readAndValidateManifest()`
- 条件付き依存: `if (profileRootPath)` → `Date.now()`
- 条件付き依存: `if (profileRootPath)` → `PathUtils.join()`
- 条件付き依存: `if (profileRootPath)` → `IOUtils.makeDirectory()`
- 条件付き依存: `if (profileRootPath)` → `IOUtils.getDirectory()`
- 条件付き依存: `if (copiedProfile)` → `lazy.ProfileAge()`
- 条件付き依存: `if (copiedProfile)` → `profileAge.recordProfileCopied()`
- 条件付き依存: `if (replaceCurrentProfile && isLegacyBackup)` → `profile.setAvatar()`
- 条件付き依存: `if (replaceCurrentProfile && isLegacyBackup)` → `currentSelectableProfile.getAvatarFile()`
- 条件付き依存: `if (replaceCurrentProfile && isLegacyBackup)` → `profile.setThemeAsync()`
- 条件付き依存: `if (!replaceCurrentProfile && isLegacyBackup)` → `this.#getLegacyThemeId()`
- 条件付き依存: `if (!replaceCurrentProfile && isLegacyBackup)` → `lazy.SelectableProfileService.getColorsForDefaultTheme()`
- 条件付き依存: `if (!replaceCurrentProfile && isLegacyBackup)` → `profile.setThemeAsync()`
- 条件付き依存: `if (shouldLaunch)` → `lazy.SelectableProfileService.launchInstance()`
- 参照: `DefaultBackupResources.SelectableProfileBackupResource.key`, `ERRORS.PROFILE_CREATION_FAILED`, `ERRORS.RECOVERY_FAILED`, `RESTORE_STEPS.RESTORE_CONFIGURE_PROFILE`, `RESTORE_STEPS.RESTORE_CREATE_PROFILE`, `RESTORE_STEPS.RESTORE_LAUNCH_PROFILE`, `RESTORE_STEPS.RESTORE_RECOVER_RESOURCES`, `RESTORE_STEPS.RESTORE_WRITE_POST_RECOVERY`, `copiedProfile.name`, `currentSelectableProfile.avatar`, `currentSelectableProfile.hasCustomAvatar`, `currentSelectableProfile.name`, `currentSelectableProfile.theme`, `currentTheme.themeId`, `e.message`, `err.restoreStep`, `lazy.SelectableProfileService.currentProfile`, `manifest.meta?.isSelectableProfile`, `postRecovery.backupServiceInternal`, `profile.name`, `profile.path`, `this.#_state.backupFileInfo.appName`, `this.#_state.backupFileInfo.appVersion`, `this.#_state.backupFileInfo.buildID`, `this.#_state.backupFileInfo.date`, `this.#_state.backupFileInfo.healthTelemetryEnabled`, `this.#_state.backupFileInfo.legacyClientID`, `this.#_state.backupFileInfo.osName`, `this.#_state.backupFileInfo.osVersion`, `this.#_state.intermediateProfileCreationDate`, `this.#_state.restoreID`, `this.#_state.restoreSource`

## BackupService.checkForPostRecovery()
- 位置: async L4057-4124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.readJSON()`, `IOUtils.remove()`, `PathUtils.join()`, `lazy.logConsole.debug()`, `this.#postRecoveryResolver()`
- 条件付き依存: `if (!(await IOUtils.exists(postRecoveryFile)))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!(await IOUtils.exists(postRecoveryFile)))` → `this.#postRecoveryResolver()`
- 条件付き依存: `if ( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore )` → `Services.prefs.setStringPref()`
- 条件付き依存: `if ( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore )` → `JSON.stringify()`
- 条件付き依存: `if ( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore )` → `Glean.browserBackup.restoredProfileLaunched.record()`
- 条件付き依存: `if ( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore )` → `Services.obs.notifyObservers()`
- 条件付き依存: `if ( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore )` → `GleanPings.postProfileRestore.submit()`
- 条件付き依存: `if (!( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore ))` → `this.#resources.get()`
- 条件付き依存: `if (!resourceClass)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore ))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore ))` → `new resourceClass().postRecovery()`
- 条件付き依存: `if (!( resourceKey == "backupServiceInternal" && postRecoveryEntry.isProfileRestore ))` → `lazy.logConsole.error()`
- 参照: `BackupService.POST_RECOVERY_FILE_NAME`, `PathUtils.profileDir`, `postRecoveryEntry.backupMetadata`, `postRecoveryEntry.isProfileRestore`, `postRecoveryEntry.restoreID`
- XPCOM: `Services.obs` / `Services.prefs`

## BackupService.#getDesktopIni()
- 位置: L4132-4138
- 役割: (未記入)
- 触るとき: (未記入)

## BackupService.#createDesktopIni()
- 位置: async L4148-4173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.setWindowsAttributes()`, `IOUtils.writeUTF8()`, `PathUtils.join()`, `lazy.logConsole.debug()`, `lazy.logConsole.warn()`, `this.#getDesktopIni()`
- 参照: `BackupService.BACKUP_DIR_TRANSLATION`

## BackupService.maybeCleanupDesktopIni()
- 位置: async L4184-4224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `lazy.logConsole.debug()`, `lazy.logConsole.warn()`
- 条件付き依存: `if (await IOUtils.exists(desktopIni))` → `this.#getDesktopIni()`
- 条件付き依存: `if (await IOUtils.exists(desktopIni))` → `IOUtils.stat()`
- 条件付き依存: `if (fileInfo && fileInfo.size == expectedContents.length)` → `IOUtils.readUTF8()`
- 条件付き依存: `if (currentContents == expectedContents)` → `IOUtils.remove()`
- 条件付き依存: `if (await IOUtils.exists(desktopIni))` → `IOUtils.setWindowsAttributes()`
- 参照: `BackupService.BACKUP_DIR_TRANSLATION`, `expectedContents.length`, `fileInfo.size`

## BackupService.setParentDirPath()
- 位置: async L4232-4255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.filename()`, `Services.prefs.setStringPref()`, `lazy.logConsole.error()`
- 条件付き依存: `if (filename != BackupService.BACKUP_DIR_NAME)` → `PathUtils.join()`
- 参照: `BackupService.BACKUP_DIR_NAME`, `ERRORS.FILE_SYSTEM_ERROR`
- XPCOM: `Services.prefs`

## BackupService.onUpdateLocationDirPath()
- 位置: async L4263-4270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserBackup.changeLocation.record()`, `lazy.logConsole.debug()`, `this.stateUpdate()`
- 参照: `this.#_state.backupDirPath`

## BackupService.onUpdateBackupErrorCode()
- 位置: L4279-4284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.stateUpdate()`
- 参照: `this.#_state.backupErrorCode`

## BackupService.onUpdateLastBackupFileName()
- 位置: L4293-4310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.stateUpdate()`
- 条件付き依存: `if (!newLastBackupFileName)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!newLastBackupFileName)` → `Services.prefs.clearUserPref()`
- 参照: `this.#_state.lastBackupDate`, `this.#_state.lastBackupFileName`
- XPCOM: `Services.prefs`

## BackupService.onUpdateProfilesEnabledState()
- 位置: L4317-4325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.stateUpdate()`
- 参照: `lazy.SelectableProfileService.isEnabled`, `this.#_state.selectableProfilesAllowed`

## BackupService.getIconFromFilePath()
- 位置: L4336-4347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.toFileURI()`

## BackupService.setScheduledBackups()
- 位置: L4358-4383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- 条件付き依存: `if (shouldEnableScheduledBackups)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (shouldEnableScheduledBackups)` → `this.setEmbeddedComponentPersistentData()`
- 条件付き依存: `if (shouldEnableScheduledBackups)` → `BackupService.maybeAddToEnabledListPref()`
- 条件付き依存: `if (!(shouldEnableScheduledBackups))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(shouldEnableScheduledBackups))` → `BackupService.maybeRemoveFromEnabledListPref()`
- 参照: `ERRORS.NONE`, `this.#scheduledBackupsToggleSource`
- XPCOM: `Services.prefs`

## BackupService.onUpdateScheduledBackups()
- 位置: L4391-4415
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isScheduledBackupsEnabled)` → `Glean.browserBackup.toggleOn.record()`
- 条件付き依存: `if (isScheduledBackupsEnabled)` → `this.classifyLocationForTelemetry()`
- 条件付き依存: `if (!(isScheduledBackupsEnabled))` → `Glean.browserBackup.toggleOff.record()`
- 条件付き依存: `if (this.#_state.scheduledBackupsEnabled != isScheduledBackupsEnabled)` → `Glean.browserBackup.schedulerToggleSource.set()`
- 条件付き依存: `if (this.#_state.scheduledBackupsEnabled != isScheduledBackupsEnabled)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#_state.scheduledBackupsEnabled != isScheduledBackupsEnabled)` → `this.stateUpdate()`
- 参照: `lazy.backupDirPref`, `this.#_state.encryptionEnabled`, `this.#_state.scheduledBackupsEnabled`, `this.#scheduledBackupsToggleSource`

## BackupService.takeMeasurements()
- 位置: async L4422-4470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserBackup.enabled.set()`, `Glean.browserBackup.profDDiskSpace.set()`, `Glean.browserBackup.pswdEncrypted.set()`, `Glean.browserBackup.schedulerEnabled.set()`, `IOUtils.getFile()`, `MeasurementUtils.fuzzByteSize()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `new resourceClass().measure()`, `this.#resources.values()`, `this.loadEncryptionState()`
- 条件付き依存: `if (defaultParentDirPath)` → `PathUtils.join()`
- 条件付き依存: `if (defaultParentDirPath)` → `Glean.browserBackup.locationOnDevice.set()`
- 参照: `BackupService.BACKUP_DIR_NAME`, `BackupService.DEFAULT_PARENT_DIR_PATH`, `PathUtils.profileDir`, `lazy.backupDirPref`, `lazy.scheduledBackupsPref`, `profileDir.diskSpaceAvailable`, `resourceClass.key`, `this.#_state.encryptionEnabled`

## BackupService.loadEncryptionState()
- 位置: L4489-4536
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#encState !== undefined)` → `Promise.resolve()`
- 条件付き依存: `if (!this.#loadEncryptionStatePromise)` → `PathUtils.join()`
- 条件付き依存: `if (!this.#loadEncryptionStatePromise)` → `IOUtils.exists()`
- 条件付き依存: `if (await IOUtils.exists(encStateFile))` → `IOUtils.readJSON()`
- 条件付き依存: `if (await IOUtils.exists(encStateFile))` → `lazy.ArchiveEncryptionState.initialize()`
- 条件付き依存: `if (!this.#loadEncryptionStatePromise)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!this.#loadEncryptionStatePromise)` → `this.stateUpdate()`
- 参照: `BackupService.ARCHIVE_ENCRYPTION_STATE_FILE`, `BackupService.PROFILE_FOLDER_NAME`, `PathUtils.profileDir`, `this.#_state.encryptionEnabled`, `this.#encState`, `this.#loadEncryptionStatePromise`

## BackupService.enableEncryption()
- 位置: async L4550-4588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeJSON()`, `PathUtils.join()`, `encState.serialize()`, `lazy.ArchiveEncryptionState.initialize()`, `lazy.logConsole.debug()`, `this.stateUpdate()`
- 参照: `BackupService.ARCHIVE_ENCRYPTION_STATE_FILE`, `BackupService.PROFILE_FOLDER_NAME`, `ERRORS.INVALID_PASSWORD`, `ERRORS.UNKNOWN`, `PathUtils.profileDir`, `password.length`, `this.#_state.encryptionEnabled`, `this.#encState`

## BackupService.disableEncryption()
- 位置: async L4599-4614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `lazy.logConsole.debug()`, `this.stateUpdate()`
- 参照: `BackupService.ARCHIVE_ENCRYPTION_STATE_FILE`, `BackupService.PROFILE_FOLDER_NAME`, `PathUtils.profileDir`, `this.#_state.encryptionEnabled`, `this.#encState`

## BackupService.initBackupScheduler()
- 位置: L4656-4717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesObservers.addListener()`, `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `Services.prefs.getIntPref()`, `lazy.AddonManager.addAddonListener()`, `lazy.idleService.addIdleObserver()`, `lazy.logConsole.debug()`, `this.onPlacesEvents.bind()`, `this.stateUpdate()`
- 条件付き依存: `if (this.#backupSchedulerInitted)` → `lazy.logConsole.warn()`
- 参照: `this.#_state.lastBackupDate`, `this.#backupSchedulerInitted`, `this.#idleThresholdSeconds`, `this.#observer`, `this.#placesObserver`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#observer()
- 位置: L4682-4684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onObserve()`

## BackupService.uninitBackupScheduler()
- 位置: L4722-4761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesObservers.removeListener()`, `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.AddonManager.removeAddonListener()`, `lazy.idleService.removeIdleObserver()`, `this.#backupWriteAbortController.abort()`, `this.#regenerationDebouncer.disarm()`
- 条件付き依存: `if (!this.#backupSchedulerInitted)` → `lazy.logConsole.warn()`
- 参照: `this.#backupSchedulerInitted`, `this.#idleThresholdSeconds`, `this.#observer`, `this.#placesObserver`
- XPCOM: `Services.obs` / `Services.prefs`

## BackupService.onObserve()
- 位置: L4776-4838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subject.QueryInterface()`, `this.#debounceRegeneration()`, `this.onIdle()`, `this.uninitBackupScheduler()`, `this.uninitStatusObservers()`
- 条件付き依存: `if (data == "removeLogin" || data == "removeAllLogins")` → `this.#debounceRegeneration()`
- 条件付き依存: `if ( data == "remove" && (subject.wrappedJSObject.collectionName == "creditCards" || subject.wrappedJSObject.collectionName == "addresses") )` → `this.#debounceRegeneration()`
- 条件付き依存: `if (data == "deleted")` → `this.#debounceRegeneration()`
- 条件付き依存: `if ( (notification.action == Ci.nsICookieNotification.COOKIE_DELETED || notification.action == Ci.nsICookieNotification.ALL_COOKIES_CLEARED) && !notification.bro...)` → `this.#debounceRegeneration()`
- 条件付き依存: `if (data == SANITIZE_ON_SHUTDOWN_PREF_NAME)` → `this.#debounceRegeneration()`
- 参照: `Ci.nsICookieNotification`, `Ci.nsICookieNotification.ALL_COOKIES_CLEARED`, `Ci.nsICookieNotification.COOKIE_DELETED`, `notification.action`, `notification.browsingContextId`, `subject.wrappedJSObject.collectionName`
- XPCOM: [`nsICookieNotification`](../../../netwerk/cookie/nsICookieNotification.idl.md)

## BackupService.initStatusObservers()
- 位置: L4851-4875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `lazy.NimbusFeatures.backupService.onUpdate()`, `lazy.SelectableProfileService.on()`, `this.#handleStatusChange()`
- 参照: `BackupService.STATUS_OBSERVER_PREFS`, `this.#profileServiceStateObserver`, `this.#statusPrefObserver`
- XPCOM: `Services.prefs`

## this.#statusPrefObserver()
- 位置: L4858-4861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleStatusChange()`

## this.#profileServiceStateObserver()
- 位置: L4869-4870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onUpdateProfilesEnabledState()`

## BackupService.uninitStatusObservers()
- 位置: L4883-4899
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `lazy.NimbusFeatures.backupService.offUpdate()`, `lazy.SelectableProfileService.off()`
- 参照: `BackupService.STATUS_OBSERVER_PREFS`, `this.#profileServiceStateObserver`, `this.#statusPrefObserver`
- XPCOM: `Services.prefs`

## BackupService.#handleStatusChange()
- 位置: L4907-4929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateGleanEnablement()`
- 条件付き依存: `if ( archiveStatus.enabled != this.#lastSeenArchiveStatus || restoreStatus.enabled != this.#lastSeenRestoreStatus )` → `this.#notifyStatusObservers()`
- 条件付き依存: `if (!archiveStatus.enabled)` → `this.cleanupBackupFiles()`
- 参照: `archiveStatus.enabled`, `restoreStatus.enabled`, `this.#_state.archiveEnabledStatus`, `this.#_state.restoreEnabledStatus`, `this.#lastSeenArchiveStatus`, `this.#lastSeenRestoreStatus`, `this.archiveEnabledStatus`, `this.archiveEnabledStatus.enabled`, `this.restoreEnabledStatus`, `this.restoreEnabledStatus.enabled`

## BackupService.#updateGleanEnablement()
- 位置: L4931-4950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserBackup.archiveEnabled.set()`, `Glean.browserBackup.restoreEnabled.set()`
- 条件付き依存: `if (!archiveStatus.enabled)` → `Glean.browserBackup.archiveDisabledReason.set()`
- 条件付き依存: `if (this.#wasArchivePreviouslyDisabled)` → `Glean.browserBackup.archiveDisabledReason.set()`
- 条件付き依存: `if (!restoreStatus.enabled)` → `Glean.browserBackup.restoreDisabledReason.set()`
- 条件付き依存: `if (this.#wasRestorePreviouslyDisabled)` → `Glean.browserBackup.restoreDisabledReason.set()`
- 参照: `archiveStatus.enabled`, `archiveStatus.internalReason`, `restoreStatus.enabled`, `restoreStatus.internalReason`, `this.#wasArchivePreviouslyDisabled`, `this.#wasRestorePreviouslyDisabled`

## BackupService.#notifyStatusObservers()
- 位置: L4956-4962
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.logConsole.log()`
- XPCOM: `Services.obs`

## BackupService.cleanupBackupFiles()
- 位置: async L4964-4978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.deleteLastBackup()`
- 条件付き依存: `if (this.state.encryptionEnabled)` → `this.disableEncryption()`
- 参照: `this.state.encryptionEnabled`

## BackupService.#debounceRegeneration()
- 位置: L4985-4988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#regenerationDebouncer.arm()`, `this.#regenerationDebouncer.disarm()`

## BackupService.onIdle()
- 位置: async L4995-5063
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#takenMeasurements)` → `this.takeMeasurements().catch()`
- 条件付き依存: `if (!this.#takenMeasurements)` → `this.takeMeasurements()`
- 条件付き依存: `if (!this.#takenMeasurements)` → `lazy.logConsole.error()`
- 条件付き依存: `if (lazy.scheduledBackupsPref && this.archiveEnabledStatus.enabled)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.scheduledBackupsPref && this.archiveEnabledStatus.enabled)` → `Math.floor()`
- 条件付き依存: `if (lazy.scheduledBackupsPref && this.archiveEnabledStatus.enabled)` → `Date.now()`
- 条件付き依存: `if (lastBackupDate && lastBackupDate > now)` → `lazy.logConsole.error()`
- 条件付き依存: `if (lastBackupDate && lastBackupDate > now)` → `this.stateUpdate()`
- 条件付き依存: `if (!lastBackupDate)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!(!lastBackupDate))` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( !lastBackupDate || now - lastBackupDate > lazy.minimumTimeBetweenBackupsSeconds )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( !lastBackupDate || now - lastBackupDate > lazy.minimumTimeBetweenBackupsSeconds )` → `this.createBackupOnIdleDispatch()`
- 条件付き依存: `if ( !lastBackupDate || now - lastBackupDate > lazy.minimumTimeBetweenBackupsSeconds )` → `lazy.logConsole.error()`
- 条件付き依存: `if (!( !lastBackupDate || now - lastBackupDate > lazy.minimumTimeBetweenBackupsSeconds ))` → `lazy.logConsole.debug()`
- 参照: `lazy.minimumTimeBetweenBackupsSeconds`, `lazy.scheduledBackupsPref`, `this.#_state.lastBackupDate`, `this.#takenMeasurements`, `this._startupTimeUnixSeconds`, `this.archiveEnabledStatus.enabled`

## BackupService._startupTimeUnixSeconds()
- 位置: L5070-5073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Services.startup.getStartupInfo()`, `Services.startup.getStartupInfo().process.getTime()`
- XPCOM: `Services.startup`

## BackupService.shouldAttemptBackup()
- 位置: L5080-5140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupService.backoffSeconds()`, `Date.now()`, `Math.floor()`, `Number.isFinite()`, `Services.prefs.getStringPref()`
- 条件付き依存: `if (debugInfoStr)` → `JSON.parse()`
- 条件付き依存: `if (debugInfoStr)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (!hasErroredLastAttempt)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (secondsSinceLastAttempt < lazy.minimumTimeBetweenBackupsSeconds / 2)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.isRetryDisabledOnIdle)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (secondsSinceLastAttempt < BackupService.backoffSeconds())` → `lazy.logConsole.debug()`
- 条件付き依存: `if (secondsSinceLastAttempt < BackupService.backoffSeconds())` → `BackupService.backoffSeconds()`
- 参照: `BackupService.#errorRetries`, `lazy.isRetryDisabledOnIdle`, `lazy.minimumTimeBetweenBackupsSeconds`, `parsed?.lastBackupAttempt`
- XPCOM: `Services.prefs`

## BackupService.createBackupOnIdleDispatch()
- 位置: L5153-5214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`, `Promise.withResolvers()`, `lazy.logConsole.debug()`, `resolve()`, `this.#infalliblePathExists()`, `this.shouldAttemptBackup()`
- 条件付き依存: `if (!this.shouldAttemptBackup())` → `Promise.resolve()`
- 条件付き依存: `if (await this.#infalliblePathExists(lazy.backupDirPref))` → `PathUtils.join()`
- 条件付き依存: `if (isScheduledBackupsEnabled)` → `this.createBackup()`
- 条件付き依存: `if (BackupService.#errorRetries > lazy.backupRetryLimit)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (BackupService.#errorRetries > lazy.backupRetryLimit)` → `Glean.browserBackup.backupThrottled.record()`
- 条件付き依存: `if ( deletePreviousBackup && oldBackupFilePath && oldBackupFilePath != possibleArchivePath )` → `lazy.logConsole.log()`
- 条件付き依存: `if ( deletePreviousBackup && oldBackupFilePath && oldBackupFilePath != possibleArchivePath )` → `this.maybeCleanupDesktopIni()`
- 条件付き依存: `if ( deletePreviousBackup && oldBackupFilePath && oldBackupFilePath != possibleArchivePath )` → `IOUtils.remove()`
- 参照: `BackupService.#errorRetries`, `lazy.backupDirPref`, `lazy.backupRetryLimit`, `lazy.scheduledBackupsPref`, `this.#_state.lastBackupFileName`
- XPCOM: `Services.prefs`

## BackupService.onPlacesEvents()
- 位置: L5222-5247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#debounceRegeneration()`
- 条件付き依存: `if (event.reason == PlacesVisitRemoved.REASON_DELETED)` → `this.#debounceRegeneration()`
- 参照: `PlacesVisitRemoved.REASON_DELETED`, `event.reason`, `event.type`

## BackupService.onUninstalled()
- 位置: L5257-5259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#debounceRegeneration()`

## BackupService.setBackupFileToRestore()
- 位置: L5266-5269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stateUpdate()`
- 参照: `this.#_state.backupFileToRestore`

## BackupService.loadBackupFileInfo()
- 位置: async L5279-5318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `lazy.logConsole.debug()`, `this.classifyLocationForTelemetry()`, `this.sampleArchive()`, `this.setRecoveryError()`
- 参照: `ERRORS.NONE`, `archiveJSON?.meta?.appName`, `archiveJSON?.meta?.appVersion`, `archiveJSON?.meta?.buildID`, `archiveJSON?.meta?.date`, `archiveJSON?.meta?.deviceName`, `archiveJSON?.meta?.healthTelemetryEnabled`, `archiveJSON?.meta?.legacyClientID`, `archiveJSON?.meta?.osBuildNumber`, `archiveJSON?.meta?.osName`, `archiveJSON?.meta?.osVersion`, `archiveJSON?.meta?.profileName`, `error.cause`, `this.#_state.backupFileCoarseLocation`, `this.#_state.backupFileInfo`, `this.#_state.restoreID`
- XPCOM: `Services.uuid`

## BackupService.resetLastBackupInternalState()
- 位置: L5323-5329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stateUpdate()`
- 参照: `this.#_state.backupFileInfo`, `this.#_state.backupFileToRestore`, `this.#_state.lastBackupDate`, `this.#_state.lastBackupFileName`

## BackupService.resetDefaultParentInternalState()
- 位置: L5334-5337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stateUpdate()`
- 参照: `this.#_state.defaultParent`

## BackupService.showBackupLocation()
- 位置: async L5343-5356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`
- 条件付き依存: `if (await IOUtils.exists(backupFilePath))` → `new lazy.nsLocalFile(backupFilePath).reveal()`
- 条件付き依存: `if (!(await IOUtils.exists(backupFilePath)))` → `this.resolveArchiveDestFolderPath()`
- 条件付き依存: `if (!(await IOUtils.exists(backupFilePath)))` → `new lazy.nsLocalFile(archiveDestFolderPath).reveal()`
- 参照: `lazy.backupDirPref`, `lazy.lastBackupFileName`, `lazy.nsLocalFile`

## BackupService.findIfABackupFileExists()
- 位置: async L5375-5529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^FirefoxBackup_.*\.html$/.test()`, `IOUtils.getChildren()`, `PathUtils.filename()`, `files.filter()`, `files.push()`, `lazy.logConsole.error()`, `this.stateUpdate()`
- 条件付き依存: `if (this.#_state.backupDirPath)` → `backupPaths.add()`
- 条件付き依存: `if (dirPath)` → `backupPaths.add()`
- 条件付き依存: `if (dirPath)` → `PathUtils.join()`
- 条件付き依存: `if (!anyPathSucceeded && backupPaths.size)` → `this.stateUpdate()`
- 条件付き依存: `if (multipleFiles && maybeBackupFiles.length > 1 && validateFile)` → `maybeBackupFiles.sort()`
- 条件付き依存: `if (multipleFiles && maybeBackupFiles.length > 1 && validateFile)` → `PathUtils.filename()`
- 条件付き依存: `if (multipleFiles && maybeBackupFiles.length > 1 && validateFile)` → `nameA.match()`
- 条件付き依存: `if (multipleFiles && maybeBackupFiles.length > 1 && validateFile)` → `nameB.match()`
- 条件付き依存: `if (multipleFiles && maybeBackupFiles.length > 1 && validateFile)` → `timestampB.localeCompare()`
- 条件付き依存: `if (validateFile)` → `this.loadBackupFileInfo()`
- 条件付き依存: `if (validateFile)` → `lazy.logConsole.log()`
- 条件付き依存: `if (this.#_state.backupFileToRestore === file)` → `this.stateUpdate()`
- 参照: `BackupService.BACKUP_DIR_NAME`, `BackupService.docsDirFolderPath?.path`, `BackupService.oneDriveFolderPath?.path`, `backupPaths.size`, `files.length`, `lazy.lastBackupFileName`, `maybeBackupFiles.length`, `this.#_state.backupDirPath`, `this.#_state.backupFileInfo`, `this.#_state.backupFileToRestore`

## BackupService.findBackupsInWellKnownLocations()
- 位置: async L5557-5593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findIfABackupFileExists()`
- 条件付き依存: `if (source)` → `new Date(backupDate).getTime()`
- 条件付き依存: `if (source)` → `Glean.browserBackup.backupDetectionComplete.record()`
- 参照: `this.#_state.backupFileCoarseLocation`, `this.#_state.backupFileInfo?.date`, `this.#_state.backupFileToRestore`, `this.#_state.restoreID`

## BackupService.editBackupLocation()
- 位置: async L5602-5613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `this.deleteLastBackup()`, `this.setParentDirPath()`

## BackupService.deleteLastBackup()
- 位置: async L5622-5672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `locks.request()`, `this.#infalliblePathExists()`
- 条件付き依存: `if (!lazy.scheduledBackupsPref)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.lastBackupFileName)` → `this.#infalliblePathExists()`
- 条件付き依存: `if (await this.#infalliblePathExists(lazy.backupDirPref))` → `PathUtils.join()`
- 条件付き依存: `if (await this.#infalliblePathExists(lazy.backupDirPref))` → `lazy.logConsole.log()`
- 条件付き依存: `if (await this.#infalliblePathExists(lazy.backupDirPref))` → `IOUtils.remove()`
- 条件付き依存: `if (lazy.lastBackupFileName)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(lazy.lastBackupFileName))` → `lazy.logConsole.log()`
- 条件付き依存: `if (await this.#infalliblePathExists(lazy.backupDirPref))` → `this.maybeCleanupDesktopIni()`
- 条件付き依存: `if (await this.#infalliblePathExists(lazy.backupDirPref))` → `IOUtils.getChildren()`
- 条件付き依存: `if (!children.length)` → `IOUtils.remove()`
- 参照: `BackupService.WRITE_BACKUP_LOCK_NAME`, `children.length`, `lazy.backupDirPref`, `lazy.lastBackupFileName`, `lazy.scheduledBackupsPref`, `this.#backupWriteAbortController.signal`
- XPCOM: `Services.prefs`

## BackupService.#infalliblePathExists()
- 位置: async L5683-5695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `lazy.logConsole.warn()`

## BackupService.maybeAddToEnabledListPref()
- 位置: L5704-5724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `profilesEnabledOn.includes()`
- 条件付き依存: `if (!lazy.SelectableProfileService.currentProfile)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (!profilesEnabledOn.includes(profileID))` → `profilesEnabledOn.push()`
- 参照: `lazy.SelectableProfileService.currentProfile`, `lazy.SelectableProfileService.currentProfile?.id`, `lazy.enabledOnProfilesPref`
- XPCOM: `Services.prefs`

## BackupService.maybeRemoveFromEnabledListPref()
- 位置: async L5733-5756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `lazy.SelectableProfileService.flushSharedPrefToDatabase()`, `lazy.enabledOnProfilesPref.filter()`
- 条件付き依存: `if (!lazy.SelectableProfileService.currentProfile)` → `lazy.logConsole.warn()`
- 参照: `lazy.SelectableProfileService.currentProfile`, `lazy.SelectableProfileService.currentProfile?.id`
- XPCOM: `Services.prefs`
