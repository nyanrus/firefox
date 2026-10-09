# browser/components/profiles/content/profiles-theme-card.mjs

source: browser/components/profiles/content/profiles-theme-card.mjs
source-hash: 35cd6b1085a1c6b179bd2d459f68e1c5fe673138
lines: 85

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ProfilesThemeCard.updateThemeImage()
- 位置: L22-46
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.theme.contentColor)` → `window.getComputedStyle()`
- 条件付き依存: `if (!this.theme.contentColor)` → `styles.getPropertyValue()`
- 参照: `document.body`, `this.backgroundImg.src`, `this.backgroundImg.style.fill`, `this.backgroundImg.style.stroke`, `this.imgHolder.style.backgroundColor`, `this.theme`, `this.theme.chromeColor`, `this.theme.contentColor`, `this.theme.id`, `this.theme.toolbarColor`

## ProfilesThemeCard.updated()
- 位置: L48-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updated()`, `this.updateThemeImage()`

## ProfilesThemeCard.render()
- 位置: L53-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.theme`, `this.theme.dataL10nId`, `this.theme.dataL10nTitle`, `this.theme.name`
