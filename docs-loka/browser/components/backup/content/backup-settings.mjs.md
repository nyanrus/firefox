# browser/components/backup/content/backup-settings.mjs

source: browser/components/backup/content/backup-settings.mjs
source-hash: 4d87a81a27e8c2e5e4a5ef225bbdb7e85a2a6fe0
lines: 534

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## BackupSettings.queries()
- 位置: L37-63
- 役割: (未記入)
- 触るとき: (未記入)

## BackupSettings.dialogs()
- 位置: L65-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.disableBackupEncryptionDialogEl`, `this.enableBackupEncryptionDialogEl`, `this.restoreFromBackupDialogEl`, `this.turnOffScheduledBackupsDialogEl`, `this.turnOnScheduledBackupsDialogEl`

## BackupSettings.constructor()
- 位置: L79-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `ERRORS.NONE`, `this._enableEncryptionTypeAttr`, `this.backupServiceState`

## BackupSettings.connectedCallback()
- 位置: L109-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`, `this.dispatchEvent()`

## BackupSettings.handleErrorBarDismiss()
- 位置: L121-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## BackupSettings.handleEvent()
- 位置: L128-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialog?.close()`, `this.dispatchEvent()`
- 条件付き依存: `if (this.restoreFromBackupDialogEl)` → `this.restoreFromBackupDialogEl.showModal()`
- 参照: `event.detail.backupPassword`, `event.type`, `this.dialogs`, `this.restoreFromBackupDialogEl`

## BackupSettings.handleBackupTrigger()
- 位置: L163-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## BackupSettings.handleShowScheduledBackups()
- 位置: L171-183
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this.backupServiceState.scheduledBackupsEnabled && this.turnOnScheduledBackupsDialogEl )` → `this.turnOnScheduledBackupsDialogEl.showModal()`
- 条件付き依存: `if ( this.backupServiceState.scheduledBackupsEnabled && this.turnOffScheduledBackupsDialogEl )` → `this.turnOffScheduledBackupsDialogEl.showModal()`
- 参照: `this.backupServiceState.scheduledBackupsEnabled`, `this.turnOffScheduledBackupsDialogEl`, `this.turnOnScheduledBackupsDialogEl`

## BackupSettings.handleToggleBackupEncryption()
- 位置: async L185-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`
- 条件付き依存: `if (toggledToDisable && this.disableBackupEncryptionDialogEl)` → `this.disableBackupEncryptionDialogEl.showModal()`
- 条件付き依存: `if (!(toggledToDisable && this.disableBackupEncryptionDialogEl))` → `this.enableBackupEncryptionDialogEl.showModal()`
- 参照: `event.target.checked`, `event.target.slot`, `this._enableEncryptionTypeAttr`, `this.backupServiceState.encryptionEnabled`, `this.disableBackupEncryptionDialogEl`, `this.updateComplete`

## BackupSettings.handleChangePassword()
- 位置: async L207-213
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.enableBackupEncryptionDialogEl)` → `this.enableBackupEncryptionDialogEl.showModal()`
- 参照: `this._enableEncryptionTypeAttr`, `this.enableBackupEncryptionDialogEl`, `this.updateComplete`

## BackupSettings.turnOnScheduledBackupsDialogTemplate()
- 位置: L215-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.backupServiceState.defaultParent`, `this.backupServiceState.supportBaseLink`, `this.handleTurnOnScheduledBackupsDialogClose`

## BackupSettings.turnOffScheduledBackupsDialogTemplate()
- 位置: L232-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## BackupSettings.restoreFromBackupDialogTemplate()
- 位置: L240-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## BackupSettings.restoreFromBackupTemplate()
- 位置: L246-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.restoreFromBackupDialogTemplate()`
- 参照: `this.backupServiceState.scheduledBackupsEnabled`, `this.handleShowRestoreDialog`

## BackupSettings.handleShowRestoreDialog()
- 位置: L259-271
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.restoreFromBackupDialogEl)` → `this.dispatchEvent()`
- 条件付き依存: `if (this.restoreFromBackupDialogEl)` → `this.restoreFromBackupDialogEl.showModal()`
- 参照: `this.restoreFromBackupDialogEl`

## BackupSettings.handleLocationPickerClick()
- 位置: L273-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.composedPath()`, `e.composedPath().includes()`, `e.stopPropagation()`, `this.handleEditBackupLocation()`, `this.shadowRoot?.querySelector()`

## BackupSettings.handleShowBackupLocation()
- 位置: L286-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## BackupSettings.handleEditBackupLocation()
- 位置: L294-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `window.browsingContext`

## BackupSettings.handleTurnOnScheduledBackupsDialogClose()
- 位置: L306-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.turnOnScheduledBackupsEl.reset()`

## BackupSettings.handleEnableBackupEncryptionDialogClose()
- 位置: L310-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.enableBackupEncryptionEl.reset()`

## BackupSettings.enableBackupEncryptionDialogTemplate()
- 位置: L314-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this._enableEncryptionTypeAttr`, `this.backupServiceState.supportBaseLink`, `this.handleEnableBackupEncryptionDialogClose`

## BackupSettings.disableBackupEncryptionDialogTemplate()
- 位置: L327-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## BackupSettings.lastBackupInfoTemplate()
- 位置: L333-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.backupServiceState.lastBackupDate`, `this.backupServiceState.lastBackupFileName`

## BackupSettings.backupLocationTemplate()
- 位置: L361-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.backupServiceState`, `this.handleShowBackupLocation`

## handleEvent()
- 位置: L370-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleLocationPickerClick()`

## BackupSettings.sensitiveDataTemplate()
- 位置: L384-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.backupServiceState.encryptionEnabled`, `this.handleChangePassword`

## handleEvent()
- 位置: L391-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleToggleBackupEncryption()`

## BackupSettings.inProgressMessageBarTemplate()
- 位置: L414-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## BackupSettings.errorBarTemplate()
- 位置: L424-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getErrorL10nId()`, `html()`
- 参照: `this.backupServiceState.backupErrorCode`, `this.handleErrorBarDismiss`

## BackupSettings.render()
- 位置: L446-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `this.backupLocationTemplate()`, `this.disableBackupEncryptionDialogTemplate()`, `this.enableBackupEncryptionDialogTemplate()`, `this.errorBarTemplate()`, `this.inProgressMessageBarTemplate()`, `this.lastBackupInfoTemplate()`, `this.restoreFromBackupTemplate()`, `this.sensitiveDataTemplate()`, `this.turnOffScheduledBackupsDialogTemplate()`, `this.turnOnScheduledBackupsDialogTemplate()`
- 条件付き依存: `if (!this.showInProgress)` → `clearTimeout()`
- 条件付き依存: `if (!this.showInProgress)` → `setTimeout()`
- 条件付き依存: `if (!this.showInProgress)` → `this.requestUpdate()`
- 参照: `this.MESSAGE_BAR_BUFFER`, `this.backupServiceState.archiveEnabledStatus`, `this.backupServiceState.backupErrorCode`, `this.backupServiceState.backupInProgress`, `this.backupServiceState.lastBackupDate`, `this.backupServiceState.restoreEnabledStatus`, `this.backupServiceState.scheduledBackupsEnabled`, `this.handleBackupTrigger`, `this.handleShowScheduledBackups`, `this.inProgressTimeout`, `this.showInProgress`
