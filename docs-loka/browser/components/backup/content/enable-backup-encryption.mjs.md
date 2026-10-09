# browser/components/backup/content/enable-backup-encryption.mjs

source: browser/components/backup/content/enable-backup-encryption.mjs
source-hash: cf1e4588dfa52bd31d0498ece8fefc16f8bca1b3
lines: 222

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `customElements.define()`

## getErrorL10nId()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ERRORS.UNKNOWN`

## EnableBackupEncryption.queries()
- 位置: L66-76
- 役割: (未記入)
- 触るとき: (未記入)

## EnableBackupEncryption.constructor()
- 位置: L78-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `VALID_TYPES.SET_PASSWORD`, `this._inputPassValue`, `this._passwordsMatch`, `this.enableEncryptionErrorCode`, `this.supportBaseLink`, `this.type`

## EnableBackupEncryption.connectedCallback()
- 位置: L87-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`

## EnableBackupEncryption.handleEvent()
- 位置: L94-103
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.detail`, `event.type`, `this._inputPassValue`, `this._passwordsMatch`

## EnableBackupEncryption.close()
- 位置: L105-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## EnableBackupEncryption.reset()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.passwordInputsEl.reset()`
- 参照: `this._inputPassValue`, `this._passwordsMatch`, `this.enableEncryptionErrorCode`

## EnableBackupEncryption.handleConfirm()
- 位置: L121-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this._inputPassValue`

## EnableBackupEncryption.descriptionTemplate()
- 位置: L132-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## EnableBackupEncryption.buttonGroupTemplate()
- 位置: L151-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this._passwordsMatch`, `this.close`, `this.handleConfirm`

## EnableBackupEncryption.errorTemplate()
- 位置: L170-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getErrorL10nId()`, `html()`
- 参照: `this.enableEncryptionErrorCode`

## EnableBackupEncryption.contentTemplate()
- 位置: L181-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `VALID_L10N_IDS.get()`, `html()`, `ifDefined()`, `this.buttonGroupTemplate()`, `this.descriptionTemplate()`, `this.errorTemplate()`
- 参照: `VALID_TYPES.SET_PASSWORD`, `this.enableEncryptionErrorCode`, `this.supportBaseLink`, `this.type`

## EnableBackupEncryption.render()
- 位置: L210-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.contentTemplate()`
