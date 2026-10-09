# browser/components/preferences/widgets/nav-notice/nav-notice.mjs

source: browser/components/preferences/widgets/nav-notice/nav-notice.mjs
source-hash: 58a935fbb8bfdc7dab54297027459cf8e8de5275
lines: 47

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## NavNotice.willUpdate()
- 位置: L25-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (this.theme?.themeBg && this.theme?.themeFg)` → `this.style.setProperty()`
- 条件付き依存: `if (!(this.theme?.themeBg && this.theme?.themeFg))` → `this.style.removeProperty()`
- 参照: `this.theme.themeBg`, `this.theme.themeFg`, `this.theme?.themeBg`, `this.theme?.themeFg`

## NavNotice.render()
- 位置: L37-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ifDefined()`, `literal()`, `staticHtml()`
- 参照: `this.href`, `this.iconSrc`, `this.label`, `this.supportPage`
