# browser/components/aboutlogins/content/components/login-list-section.mjs

source: browser/components/aboutlogins/content/components/login-list-section.mjs
source-hash: 5495f55e28a534f218082196a5d3a783b8a8183b
lines: 35

## <module>
- 役割: (未記入)

## LoginListHeaderFactory.create()
- 位置: L8-16
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `template.content.cloneNode()`, `this.update()`
- 参照: `fragment.firstElementChild`

## LoginListHeaderFactory.update()
- 位置: L18-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `headerItem.querySelector()`
- 条件付き依存: `if (header)` → `header.startsWith()`
- 条件付き依存: `if (header.startsWith(this.ID_PREFIX))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (header.startsWith(this.ID_PREFIX))` → `header.substring()`
- 参照: `headerElement.hidden`, `headerElement.textContent`, `this.ID_PREFIX`, `this.ID_PREFIX.length`
