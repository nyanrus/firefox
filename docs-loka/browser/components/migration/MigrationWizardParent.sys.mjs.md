# browser/components/migration/MigrationWizardParent.sys.mjs

source: browser/components/migration/MigrationWizardParent.sys.mjs
source-hash: cea5d6b33c8f23c73afb799e5ebc7076b61de26c
lines: 863

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## MigrationWizardParent.didDestroy()
- 位置: L50-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.finishMigration()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## MigrationWizardParent.receiveMessage()
- 位置: async L63-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `MigrationUtils.availableFileMigrators.values()`, `MigrationUtils.getMigrator()`, `Promise.all()`, `availableMigrators.push()`, `lazy.FileUtils.File()`, `migrator.getPermissions()`, `results .flat()`, `results .flat() .filter()`, `results .flat() .filter(result => result) .sort()`, `results.push()`, `safariMigrator.getPermissions()`, `this.#getMigratorAndProfiles()`, `this.#openAboutAddons()`, `this.#openURL()`, `this.#recordEvent()`, `this.#selectManualPasswordFile()`, `this.#serializeFileMigrator()`
- 条件付き依存: `if (!gHasOpenedBefore)` → `Glean.migration.timeToProduceMigratorList.start()`
- 条件付き依存: `if (!gHasOpenedBefore)` → `Glean.migration.timeToProduceMigratorList.stop()`
- 条件付き依存: `if ( migrationDetails.type == lazy.MigrationWizardConstants.MIGRATOR_TYPES.BROWSER )` → `this.#doBrowserMigration()`
- 条件付き依存: `if ( migrationDetails.type == lazy.MigrationWizardConstants.MIGRATOR_TYPES.FILE )` → `this.#doFileMigration()`
- 条件付き依存: `if ( message.data.type == lazy.MigrationWizardConstants.MIGRATOR_TYPES.BROWSER )` → `MigrationUtils.getMigrator()`
- 条件付き依存: `if ( message.data.type == lazy.MigrationWizardConstants.MIGRATOR_TYPES.BROWSER )` → `migrator.hasPermissions()`
- 条件付き依存: `if (await IOUtils.exists(pwAppFile.path))` → `pwAppFile.launch()`
- 参照: `E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `MigrationUtils.availableMigratorKeys`, `a.lastModifiedDate`, `b.lastModifiedDate`, `lazy.MigrationWizardConstants.MIGRATOR_TYPES.BROWSER`, `lazy.MigrationWizardConstants.MIGRATOR_TYPES.FILE`, `message.data`, `message.data.args`, `message.data.key`, `message.data.type`, `message.data.url`, `message.data.where`, `message.name`, `migrationDetails.key`, `migrationDetails.type`, `pwAppFile.path`, `this.browsingContext.topChromeWindow`, `this.manager.isInProcess`, `this.manager.remoteType`

## MigrationWizardParent.#recordEvent()
- 位置: L200-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserMigration[type + "Wizard"].record()`
- 参照: `Glean.browserMigration`

## MigrationWizardParent.#doFileMigration()
- 位置: async L222-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `MigrationUtils.getFileMigrator()`, `fileMigrator.getFilePickerConfig()`, `fileMigrator.migrate()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `lazy.gFluentStrings.formatValues()`, `resolve()`, `this.sendAsyncMessage()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeOpen`, `Ci.nsIFilePicker.returnCancel`, `e.message`, `fileMigrator.displayedResourceTypes`, `fileMigrator.progressHeaderL10nID`, `fileMigrator.successHeaderL10nID`, `filePickerConfig.filters`, `filePickerConfig.title`, `filter.extensionPattern`, `filter.title`, `fp.file.path`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.LOADING`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## MigrationWizardParent.#selectManualPasswordFile()
- 位置: async L305-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `MigrationUtils.getFileMigrator()`, `fileMigrator.getFilePickerConfig()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `resolve()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeOpen`, `Ci.nsIFilePicker.returnCancel`, `filePickerConfig.filters`, `filePickerConfig.title`, `filter.extensionPattern`, `filter.title`, `fp.file.path`, `lazy.PasswordFileMigrator.key`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## MigrationWizardParent.#doBrowserMigration()
- 位置: async L355-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserMigration.sourceBrowser.accumulateSingleSample()`, `MigrationUtils.getMigrator()`, `MigrationUtils.getSourceIdForTelemetry()`, `console.error()`, `migrator.getMigrateData()`, `migrator.migrate()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!migrationDetails.autoMigration)` → `gleanMigrationUsage[migrationDetails.key].accumulateSingleSample()`
- 条件付き依存: `if (!migrationDetails.autoMigration)` → `Math.log2()`
- 条件付き依存: `if (migrationDetails.manualPasswordFilePath)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (migrationDetails.manualPasswordFilePath)` → `lazy.LoginCSVImport.importFromCSV()`
- 条件付き依存: `if (migrationDetails.manualPasswordFilePath)` → `summary.filter()`
- 条件付き依存: `if (migrationDetails.manualPasswordFilePath)` → `MigrationUtils.notifyLoginsManuallyImported()`
- 条件付き依存: `if (migrationDetails.manualPasswordFilePath)` → `lazy.gFluentStrings.formatValue()`
- 条件付き依存: `if (!foundResourceTypeName)` → `console.error()`
- 条件付き依存: `if (!success)` → `Glean.browserMigration.errors[ migrationDetails.key ].accumulateSingleSample()`
- 条件付き依存: `if (!success)` → `Math.log2()`
- 条件付き依存: `if (!success)` → `lazy.gFluentStrings.formatValue()`
- 条件付き依存: `if (!success)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if ( details?.progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS )` → `lazy.gFluentStrings.formatValue()`
- 条件付き依存: `if ( details?.progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO )` → `lazy.gFluentStrings.formatValue()`
- 条件付き依存: `if ( details?.progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO )` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (!( foundResourceTypeName == lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.EXTENSIONS ))` → `this.#getStringForImportQuantity()`
- 条件付き依存: `if (!(!foundResourceTypeName))` → `this.sendAsyncMessage()`
- 参照: `Glean.browserMigration.errors`, `Glean.browserMigration.usage`, `MigrationUtils.resourceTypes`, `details.importedExtensions.length`, `details.totalExtensions.length`, `details?.progressValue`, `entry.result`, `extraArgs.extensions`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.EXTENSIONS`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`, `lazy.MigrationWizardConstants.EXTENSIONS_IMPORT_RESULT.ALL_MATCHED`, `lazy.MigrationWizardConstants.EXTENSIONS_IMPORT_RESULT.NONE_MATCHED`, `lazy.MigrationWizardConstants.EXTENSIONS_IMPORT_RESULT.PARTIAL_MATCH`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.LOADING`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.WARNING`, `migrationDetails.autoMigration`, `migrationDetails.key`, `migrationDetails.manualPasswordFilePath`, `migrationDetails.profile`, `migrationDetails.resourceTypes`, `migrationDetails.resourceTypes.length`, `summary.filter(entry => entry.result == "added").length`
- XPCOM: `Services.urlFormatter`

## MigrationWizardParent.#getMigratorAndProfiles()
- 位置: async L595-640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Glean.migration.discoveredMigrators[key].add()`, `MigrationUtils.getMigrator()`, `console.error()`, `migrator.getSourceProfiles()`, `migrator.hasPermissions()`, `this.#serializeMigratorAndProfile()`
- 条件付き依存: `if (!(await migrator.hasPermissions()))` → `migrator.canGetPermissions()`
- 条件付き依存: `if (!(await migrator.hasPermissions()))` → `this.#serializeMigratorAndProfile()`
- 条件付き依存: `if (Array.isArray(sourceProfiles))` → `Glean.migration.discoveredMigrators[key].add()`
- 条件付き依存: `if (Array.isArray(sourceProfiles))` → `result.push()`
- 条件付き依存: `if (Array.isArray(sourceProfiles))` → `this.#serializeMigratorAndProfile()`
- 参照: `Glean.migration.discoveredMigrators`, `migrator?.enabled`, `sourceProfiles.length`

## MigrationWizardParent.#serializeMigratorAndProfile()
- 位置: async L665-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `migrator.getLastUsedDate()`, `migrator.getMigrateData()`
- 条件付き依存: `if ( profileMigrationData & MigrationUtils.resourceTypes[resourceType] || (MigrationUtils.resourceTypes[resourceType] == MigrationUtils.resourceTypes.PASSWORDS &...)` → `availableResourceTypes.push()`
- 条件付き依存: `if (!(migrator.constructor.key == lazy.InternalTestingProfileMigrator.key))` → `lazy.gFluentStrings.formatValue()`
- 参照: `MigrationUtils.resourceTypes`, `MigrationUtils.resourceTypes.PASSWORDS`, `lazy.InternalTestingProfileMigrator.key`, `lazy.MigrationWizardConstants.MIGRATOR_TYPES.BROWSER`, `lazy.SafariProfileMigrator?.key`, `migrator.constructor.brandImage`, `migrator.constructor.displayNameL10nID`, `migrator.constructor.key`, `migrator.showsManualPasswordImport`

## MigrationWizardParent.#getStringForImportQuantity()
- 位置: L743-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.getImportedCount()`, `lazy.MigrationWizardConstants.USES_FAVORITES.includes()`, `lazy.gFluentStrings.formatValue()`
- 参照: `MigrationUtils.HISTORY_MAX_AGE_IN_DAYS`, `lazy.FirefoxProfileMigrator.key`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES .PAYMENT_METHODS`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.BOOKMARKS`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.FORMDATA`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.HISTORY`, `lazy.MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`

## MigrationWizardParent.#serializeFileMigrator()
- 位置: async L811-825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gFluentStrings.formatValue()`
- 参照: `fileMigrator.constructor.brandImage`, `fileMigrator.constructor.displayNameL10nID`, `fileMigrator.constructor.key`, `fileMigrator.enabled`, `lazy.MigrationWizardConstants.MIGRATOR_TYPES.FILE`

## MigrationWizardParent.#openAboutAddons()
- 位置: L834-836
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.openTrustedLinkIn()`

## MigrationWizardParent.#openURL()
- 位置: L849-861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `Services.urlFormatter.formatURL()`, `window.openLinkIn()`
- 参照: `browser.documentGlobal`
- XPCOM: `Services.scriptSecurityManager` / `Services.urlFormatter`
