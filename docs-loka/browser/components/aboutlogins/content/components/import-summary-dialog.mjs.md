# browser/components/aboutlogins/content/components/import-summary-dialog.mjs

source: browser/components/aboutlogins/content/components/import-summary-dialog.mjs
source-hash: 3b8433852759bcd4a94d7b38c89bc996796e0dc9
lines: 73

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ImportSummaryDialog.constructor()
- 位置: L8-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._promise`

## ImportSummaryDialog.connectedCallback()
- 位置: L13-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `initDialog()`, `this.shadowRoot.querySelector()`
- 参照: `this._added`, `this._error`, `this._genericDialog`, `this._modified`, `this._noChange`, `this.shadowRoot`

## ImportSummaryDialog.show()
- 位置: L25-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loginRow.result.includes()`, `this._error.querySelector()`, `this._genericDialog.show()`, `this._noChange.querySelector()`, `this._updateCount()`, `window.AboutLoginsUtils.setFocus()`
- 参照: `loginRow.result`, `report.added`, `report.error`, `report.modified`, `report.no_change`, `this._added`, `this._error`, `this._error.querySelector(".result-meta").hidden`, `this._genericDialog._dismissButton`, `this._modified`, `this._noChange`, `this._noChange.querySelector(".result-meta").hidden`

## ImportSummaryDialog._updateCount()
- 位置: L66-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.getAttributes()`
- 条件付き依存: `if (count != document.l10n.getAttributes(component).args.count)` → `document.l10n.setAttributes()`
- 参照: `document.l10n.getAttributes(component).args.count`
