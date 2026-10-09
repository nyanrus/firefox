# browser/components/aboutlogins/content/components/import-error-dialog.mjs

source: browser/components/aboutlogins/content/components/import-error-dialog.mjs
source-hash: 31ad29512ff28d4201b13270b75a3be685df61f8
lines: 60

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ImportErrorDialog.constructor()
- 位置: L8-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._errorMessages`, `this._errorMessages.CONFLICTING_VALUES_ERROR`, `this._errorMessages.FILE_FORMAT_ERROR`, `this._errorMessages.FILE_PERMISSIONS_ERROR`, `this._errorMessages.UNABLE_TO_READ_ERROR`, `this._promise`

## ImportErrorDialog.connectedCallback()
- 位置: L33-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`, `initDialog()`, `shadowRoot.querySelector()`, `this._genericDialog.hide()`, `this.shadowRoot.querySelector()`, `tryImportAgain.addEventListener()`
- 参照: `this._descriptionElement`, `this._focusedElement`, `this._genericDialog`, `this._titleElement`, `this.shadowRoot`

## ImportErrorDialog.show()
- 位置: L51-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this._genericDialog.show()`, `window.AboutLoginsUtils.setFocus()`
- 参照: `this._descriptionElement`, `this._errorMessages`, `this._focusedElement`, `this._titleElement`
