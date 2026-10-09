# browser/components/aboutlogins/content/components/confirmation-dialog.mjs

source: browser/components/aboutlogins/content/components/confirmation-dialog.mjs
source-hash: 91a9c3a9d74fd59d321331c5445ab65776ce86ea
lines: 106

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ConfirmationDialog.constructor()
- 位置: L8-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._promise`

## ConfirmationDialog.connectedCallback()
- 位置: L13-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `shadowRoot.appendChild()`, `template.content.cloneNode()`, `this.attachShadow()`, `this.shadowRoot.querySelector()`
- 参照: `this._buttons`, `this._cancelButton`, `this._confirmButton`, `this._dismissButton`, `this._message`, `this._overlay`, `this._title`, `this.shadowRoot`

## ConfirmationDialog.handleEvent()
- 位置: L31-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.currentTarget.classList.contains()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.repeat)` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape" && !event.defaultPrevented)` → `this.onCancel()`
- 条件付き依存: `if ( event.target.classList.contains("cancel-button") || event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") )` → `this.onCancel()`
- 条件付き依存: `if (!( event.target.classList.contains("cancel-button") || event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") ))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("confirm-button"))` → `this.onConfirm()`
- 参照: `event.defaultPrevented`, `event.key`, `event.repeat`, `event.type`

## ConfirmationDialog.hide()
- 位置: L57-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._cancelButton.removeEventListener()`, `this._confirmButton.removeEventListener()`, `this._dismissButton.removeEventListener()`, `this._overlay.removeEventListener()`, `window.removeEventListener()`
- 参照: `this.hidden`

## ConfirmationDialog.show()
- 位置: L68-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `setKeyboardAccessForNonDialogElements()`, `this._cancelButton.addEventListener()`, `this._confirmButton.addEventListener()`, `this._confirmButton.focus()`, `this._dismissButton.addEventListener()`, `this._overlay.addEventListener()`, `window.addEventListener()`
- 参照: `this._confirmButton`, `this._message`, `this._promise`, `this._reject`, `this._resolve`, `this._title`, `this.hidden`

## ConfirmationDialog.onCancel()
- 位置: L95-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._reject()`, `this.hide()`

## ConfirmationDialog.onConfirm()
- 位置: L100-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._resolve()`, `this.hide()`
