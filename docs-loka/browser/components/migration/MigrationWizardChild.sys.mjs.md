# browser/components/migration/MigrationWizardChild.sys.mjs

source: browser/components/migration/MigrationWizardChild.sys.mjs
source-hash: 5b817c59eb8857184d7835676f9651972a0d8657
lines: 443

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## MigrationWizardChild.isMacOSSequoiaOrLater()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`

## MigrationWizardChild.#populateMigrators()
- 位置: async L59-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `migrators.some()`, `this.sendQuery()`
- 条件付き依存: `if (!hasBrowserMigrators && !allowOnlyFileMigrators)` → `this.setComponentState()`
- 条件付き依存: `if (!hasBrowserMigrators && !allowOnlyFileMigrators)` → `this.#sendTelemetryEvent()`
- 条件付き依存: `if (!(!hasBrowserMigrators && !allowOnlyFileMigrators))` → `this.setComponentState()`
- 参照: `MigrationWizardConstants.MIGRATOR_TYPES.BROWSER`, `MigrationWizardConstants.MIGRATOR_TYPES.FILE`, `MigrationWizardConstants.PAGES.NO_BROWSERS_FOUND`, `MigrationWizardConstants.PAGES.SELECTION`, `lazy.SHOW_IMPORT_ALL_PREF`, `migrator.type`

## MigrationWizardChild.handleEvent()
- 位置: async L96-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordBeginMigrationEvent()`, `this.#requestState()`, `this.#sendTelemetryEvent()`, `this.beginMigration()`, `this.sendAsyncMessage()`, `this.sendQuery()`
- 条件付き依存: `if (event.detail.key == "safari")` → `this.#sendTelemetryEvent()`
- 条件付き依存: `if (event.detail.key == "safari")` → `this.setComponentState()`
- 条件付き依存: `if (!(event.detail.key == "safari"))` → `console.error()`
- 条件付き依存: `if (success)` → `this.#constructExtraArgs()`
- 条件付き依存: `if (success)` → `this.beginMigration()`
- 条件付き依存: `if (path)` → `event.detail.resourceTypes.indexOf()`
- 条件付き依存: `if (path)` → `event.detail.resourceTypes.splice()`
- 条件付き依存: `if (path)` → `this.#constructExtraArgs()`
- 条件付き依存: `if (path)` → `this.beginMigration()`
- 条件付き依存: `if (success)` → `this.#requestState()`
- 参照: `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`, `MigrationWizardConstants.PAGES.SAFARI_PERMISSION`, `event.detail`, `event.detail.key`, `event.detail.manualPasswordFilePath`, `event.detail.type`, `event.detail.url`, `event.detail.where`, `event.detail?.allowOnlyFileMigrators`, `event.target`, `event.type`, `this.#wizardEl`

## MigrationWizardChild.#requestState()
- 位置: async L198-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#populateMigrators()`, `this.#wizardEl.dispatchEvent()`, `this.setComponentState()`
- 参照: `MigrationWizardConstants.PAGES.LOADING`, `this.contentWindow.CustomEvent`

## MigrationWizardChild.#sendTelemetryEvent()
- 位置: L220-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## MigrationWizardChild.#constructExtraArgs()
- 位置: L234-286
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES .PAYMENT_METHODS`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.BOOKMARKS`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.EXTENSIONS`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.FORMDATA`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.HISTORY`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`, `extraArgs.bookmarks`, `extraArgs.extensions`, `extraArgs.formdata`, `extraArgs.history`, `extraArgs.other`, `extraArgs.passwords`, `extraArgs.payment_methods`, `migrationDetails.key`, `migrationDetails.resourceTypes`

## MigrationWizardChild.#recordBeginMigrationEvent()
- 位置: L305-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `String()`, `this.#constructExtraArgs()`, `this.#sendTelemetryEvent()`
- 条件付き依存: `if (migrationDetails.profile)` → `this.#sendTelemetryEvent()`
- 参照: `extraArgs.configured`, `migrationDetails.expandedDetails`, `migrationDetails.key`, `migrationDetails.profile`

## MigrationWizardChild.beginMigration()
- 位置: async L340-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `migrationDetails.resourceTypes.includes()`, `this.#sendTelemetryEvent()`, `this.#wizardEl.dispatchEvent()`, `this.sendQuery()`
- 条件付き依存: `if (migrationDetails.key == "safari")` → `this.#sendTelemetryEvent()`
- 条件付き依存: `if (migrationDetails.key == "safari")` → `this.setComponentState()`
- 条件付き依存: `if (migrationDetails.key == "safari")` → `MigrationWizardChild.isMacOSSequoiaOrLater()`
- 条件付き依存: `if ( migrationDetails.key == "chrome" && AppConstants.platform == "win" )` → `this.#sendTelemetryEvent()`
- 条件付き依存: `if ( migrationDetails.key == "chrome" && AppConstants.platform == "win" )` → `this.setComponentState()`
- 参照: `AppConstants.platform`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`, `MigrationWizardConstants.PAGES .CHROME_WINDOWS_PASSWORD_PERMISSION`, `MigrationWizardConstants.PAGES .SAFARI_PASSWORD_PERMISSION_PRE_SEQUOIA`, `MigrationWizardConstants.PAGES.SAFARI_PASSWORD_PERMISSION`, `migrationDetails.key`, `migrationDetails.manualPasswordFilePath`, `this.contentWindow.CustomEvent`

## MigrationWizardChild.receiveMessage()
- 位置: L390-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#populateMigrators()`, `this.setComponentState()`
- 参照: `MigrationWizardConstants.PAGES.FILE_IMPORT_PROGRESS`, `MigrationWizardConstants.PAGES.PROGRESS`, `message.data.fileImportErrorMessage`, `message.data.key`, `message.data.migratorKey`, `message.data.progress`, `message.data.title`, `message.name`

## MigrationWizardChild.setComponentState()
- 位置: L427-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`, `Cu.waiveXrays(this.#wizardEl).setState()`
- 参照: `this.#wizardEl`, `this.#wizardEl.ownerDocument.defaultView`
