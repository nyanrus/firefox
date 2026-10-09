# browser/components/aboutlogins/content/components/import-details-row.mjs

source: browser/components/aboutlogins/content/components/import-details-row.mjs
source-hash: 8b6fe269a3ed56ffa1f92e1e48203990c67a6ffa
lines: 61

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ImportDetailsRow.constructor()
- 位置: L30-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelector()`, `document .querySelector("#import-details-row-template") .content.cloneNode()`, `document.l10n.connectRoot()`, `document.l10n.setAttributes()`, `rowElement.querySelector()`, `super()`, `this.appendChild()`
- 条件付き依存: `if (uiData.isError)` → `this.classList.add()`
- 参照: `reportRow.field_name`, `reportRow.result`, `rowElement.childNodes`, `rowElement.childNodes.length`, `this._login`, `uiData.isError`, `uiData.message`
