# browser/components/aboutlogins/content/components/generic-dialog.mjs

source: browser/components/aboutlogins/content/components/generic-dialog.mjs
source-hash: 8d9ddc9d36c19b9f6580b01309707e05da42d73c
lines: 64

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## GenericDialog.constructor()
- 位置: L11-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._promise`

## GenericDialog.connectedCallback()
- 位置: L16-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `initDialog()`, `shadowRoot.querySelector()`, `this.querySelector()`
- 参照: `this._dismissButton`, `this._overlay`, `this.shadowRoot`

## GenericDialog.handleEvent()
- 位置: L25-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.currentTarget.classList.contains()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.key === "Escape" && !event.defaultPrevented)` → `this.hide()`
- 条件付き依存: `if ( event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") )` → `this.hide()`
- 参照: `event.defaultPrevented`, `event.key`, `event.type`

## GenericDialog.show()
- 位置: L42-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._dismissButton.addEventListener()`, `this._overlay.addEventListener()`, `window.addEventListener()`
- 参照: `this.hidden`, `this.parentNode.host.hidden`

## GenericDialog.hide()
- 位置: L52-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._dismissButton.removeEventListener()`, `this._overlay.removeEventListener()`, `window.removeEventListener()`
- 参照: `this.hidden`, `this.parentNode.host.hidden`
