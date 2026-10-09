# browser/components/storybook/.storybook/preview.mjs

source: browser/components/storybook/.storybook/preview.mjs
source-hash: b90604d48415a12bc3542c345f4f1eab9e0e7825
lines: 216

## <module>
- 役割: (未記入)
- 呼び出し先: `connectFluent()`, `css()`, `customElements.define()`, `html()`, `importReusableComponents()`, `resolveTheme()`, `setCustomElementsManifest()`, `window.matchMedia()`

## window.RPMSetPref()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)

## window.RPMGetFormatURLPref()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)

## importESModule()
- 位置: L33-37
- 役割: (未記入)
- 触るとき: (未記入)

## declareLazy()
- 位置: L35-35
- 役割: (未記入)
- 触るとき: (未記入)

## importReusableComponents()
- 位置: L45-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `import()`, `key.endsWith()`, `key.startsWith()`, `mozElements.forEach()`
- 条件付き依存: `if ( key.startsWith("dist/bin/chrome/toolkit/content/global/elements/moz-") && key.endsWith(".mjs") )` → `mozElements.add()`
- 条件付き依存: `if ( key.startsWith("dist/bin/chrome/toolkit/content/global/elements/moz-") && key.endsWith(".mjs") )` → `key.split("/").pop().replace()`
- 条件付き依存: `if ( key.startsWith("dist/bin/chrome/toolkit/content/global/elements/moz-") && key.endsWith(".mjs") )` → `key.split("/").pop()`
- 条件付き依存: `if ( key.startsWith("dist/bin/chrome/toolkit/content/global/elements/moz-") && key.endsWith(".mjs") )` → `key.split()`

## WithCommonStyles.connectedCallback()
- 位置: L120-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.classList.add()`

## WithCommonStyles.storyContent()
- 位置: L125-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (this.story)` → `this.story()`
- 参照: `this.story`

## WithCommonStyles.render()
- 位置: L132-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.storyContent()`

## resolveTheme()
- 位置: L146-154
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `mql.matches`
