# browser/components/backup/content/turn-on-scheduled-backups.mjs

source: browser/components/backup/content/turn-on-scheduled-backups.mjs
source-hash: c6976397d7a6888dc378d6487e84b474aa9236f5
lines: 546

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `customElements.define()`

## getEnableErrorL10nId()
- 位置: L27-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ERRORS.UNKNOWN`

## TurnOnScheduledBackups.queries()
- 位置: L113-124
- 役割: (未記入)
- 触るとき: (未記入)

## TurnOnScheduledBackups.constructor()
- 位置: L126-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._newIconURL`, `this._newLabel`, `this._newPath`, `this._passwordsMatch`, `this._pendingConfirmDetail`, `this._showPasswordOptions`, `this.backupServiceState`, `this.defaultIconURL`, `this.defaultLabel`, `this.defaultPath`, `this.disableSubmit`, `this.enableBackupErrorCode`

## TurnOnScheduledBackups.showDefaultFilePath()
- 位置: L148-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._newPath`, `this.backupServiceState?.embeddedComponentPersistentData?.path`

## TurnOnScheduledBackups.connectedCallback()
- 位置: L155-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`, `this.dispatchEvent()`

## TurnOnScheduledBackups.handleEvent()
- 位置: L173-231
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.embeddedFxBackupOptIn)` → `this.dispatchEvent()`
- 条件付き依存: `if (readAccessGranted)` → `this.dispatchEvent()`
- 条件付き依存: `if ( event.key === "Enter" && (event.originalTarget.id == "backup-location-filepicker-input-default" || event.originalTarget.id == "backup-location-filepicker-in...)` → `event.preventDefault()`
- 参照: `ERRORS.DEFAULT_DIR_ACCESS_DENIED`, `ERRORS.NONE`, `event.detail`, `event.key`, `event.originalTarget.id`, `event.type`, `this._inputPassValue`, `this._newIconURL`, `this._newLabel`, `this._newPath`, `this._passwordsMatch`, `this._pendingConfirmDetail`, `this.defaultIconURL`, `this.defaultLabel`, `this.defaultPath`, `this.embeddedFxBackupOptIn`, `this.enableBackupErrorCode`

## TurnOnScheduledBackups.handleChooseLocation()
- 位置: async L233-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `window.browsingContext`

## TurnOnScheduledBackups.close()
- 位置: L244-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## TurnOnScheduledBackups.handleConfirm()
- 位置: L253-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 条件付き依存: `if ( this.embeddedFxBackupOptIn && this.backupIsEncrypted && !detail.password )` → `this.dispatchEvent()`
- 参照: `detail.password`, `this._inputPassValue`, `this._passwordsMatch`, `this._pendingConfirmDetail`, `this._showPasswordOptions`, `this.backupIsEncrypted`, `this.embeddedFxBackupOptIn`, `this.source`

## TurnOnScheduledBackups.handleTogglePasswordOptions()
- 位置: L284-287
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._passwordsMatch`, `this._showPasswordOptions`, `this.passwordOptionsCheckboxEl?.checked`

## TurnOnScheduledBackups.updated()
- 位置: L289-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.updated()`
- 参照: `this._showPasswordOptions`, `this.hideFilePathChooser`, `this.passwordOptionsCheckboxEl`, `this.passwordOptionsCheckboxEl.checked`

## TurnOnScheduledBackups.reset()
- 位置: L303-334
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.passwordOptionsExpandedEl)` → `passwordElement.reset()`
- 条件付き依存: `if ( this.embeddedFxBackupOptIn && this.backupServiceState?.embeddedComponentPersistentData )` → `this.dispatchEvent()`
- 参照: `this._inputPassValue`, `this._newIconURL`, `this._newLabel`, `this._newPath`, `this._passwordsMatch`, `this._pendingConfirmDetail`, `this._showPasswordOptions`, `this.backupServiceState?.embeddedComponentPersistentData`, `this.disableSubmit`, `this.embeddedFxBackupOptIn`, `this.enableBackupErrorCode`, `this.passwordOptionsCheckboxEl.checked`, `this.passwordOptionsExpandedEl`

## TurnOnScheduledBackups.defaultFilePathInputTemplate()
- 位置: L336-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.#placeholderIconURL`, `this.defaultIconURL`, `this.defaultLabel`

## TurnOnScheduledBackups.customFilePathInputTemplate()
- 位置: L366-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#placeholderIconURL`, `this._newIconURL`, `this._newLabel`, `this.backupServiceState?.embeddedComponentPersistentData?.iconURL`, `this.backupServiceState?.embeddedComponentPersistentData?.label`

## TurnOnScheduledBackups.errorTemplate()
- 位置: L387-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getEnableErrorL10nId()`, `html()`
- 参照: `this.enableBackupErrorCode`

## TurnOnScheduledBackups.allOptionsTemplate()
- 位置: L397-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.customFilePathInputTemplate()`, `this.defaultFilePathInputTemplate()`, `this.passwordsTemplate()`
- 参照: `this._showPasswordOptions`, `this.filePathLabelL10nId`, `this.handleChooseLocation`, `this.handleTogglePasswordOptions`, `this.showDefaultFilePath`

## TurnOnScheduledBackups.passwordsTemplate()
- 位置: L453-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.createPasswordLabelL10nId`, `this.embeddedFxBackupOptIn`, `this.supportBaseLink`

## TurnOnScheduledBackups.contentTemplate()
- 位置: L464-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.allOptionsTemplate()`, `this.errorTemplate()`
- 参照: `ERRORS.NONE`, `this._newPath`, `this._passwordsMatch`, `this._showPasswordOptions`, `this.backupServiceState?.embeddedComponentPersistentData?.path`, `this.close`, `this.defaultLabel`, `this.disableSubmit`, `this.embeddedFxBackupOptIn`, `this.enableBackupErrorCode`, `this.handleConfirm`, `this.turnOnBackupCancelBtnL10nId`, `this.turnOnBackupConfirmBtnL10nId`, `this.turnOnBackupHeaderL10nId`

## TurnOnScheduledBackups.render()
- 位置: L534-542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.contentTemplate()`
