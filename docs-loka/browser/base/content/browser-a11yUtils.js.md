# browser/base/content/browser-a11yUtils.js

source: browser/base/content/browser-a11yUtils.js
source-hash: d9ebd3727fa1bea144e396577c28027eb5c6703d
lines: 75

## <module>
- 役割: (未記入)

## announce()
- 位置: async L31-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.getElementById()`, `label.setAttribute()`, `live.appendChild()`
- 条件付き依存: `if (this._cancelAnnounce)` → `this._cancelAnnounce()`
- 条件付き依存: `if (id)` → `document.l10n.formatValue()`
- 条件付き依存: `if (live.firstChild)` → `live.firstChild.remove()`
- 参照: `live.firstChild`, `this._cancelAnnounce`

## this._cancelAnnounce()
- 位置: L45-45
- 役割: (未記入)
- 触るとき: (未記入)
