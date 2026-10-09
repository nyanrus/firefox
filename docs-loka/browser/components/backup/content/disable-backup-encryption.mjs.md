# browser/components/backup/content/disable-backup-encryption.mjs

source: browser/components/backup/content/disable-backup-encryption.mjs
source-hash: a5457c0f0950d88c2af20ca34bbc7b71b57edc25
lines: 127

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## DisableBackupEncryption.queries()
- 位置: L23-29
- 役割: (未記入)
- 触るとき: (未記入)

## DisableBackupEncryption.constructor()
- 位置: L31-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.disableEncryptionErrorCode`

## DisableBackupEncryption.close()
- 位置: L36-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`, `this.reset()`

## DisableBackupEncryption.reset()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.disableEncryptionErrorCode`

## DisableBackupEncryption.handleConfirm()
- 位置: L50-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## DisableBackupEncryption.errorTemplate()
- 位置: L58-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## DisableBackupEncryption.contentTemplate()
- 位置: L68-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.errorTemplate()`
- 参照: `this.close`, `this.disableEncryptionErrorCode`, `this.handleConfirm`

## DisableBackupEncryption.render()
- 位置: L115-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.contentTemplate()`
