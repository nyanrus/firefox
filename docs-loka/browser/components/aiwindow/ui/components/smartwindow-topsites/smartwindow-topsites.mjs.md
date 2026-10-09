# browser/components/aiwindow/ui/components/smartwindow-topsites/smartwindow-topsites.mjs

source: browser/components/aiwindow/ui/components/smartwindow-topsites/smartwindow-topsites.mjs
source-hash: 690911458907ad346a19696280792384499ccbf1
lines: 76

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartWindowTopSites.constructor()
- 位置: L20-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.sites`

## SmartWindowTopSites.#siteSelected()
- 位置: L25-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `site.url`

## SmartWindowTopSites.#iconSrc()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `site.favicon`, `site.tippyTopIcon`, `site.url`

## SmartWindowTopSites.render()
- 位置: L39-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `html()`, `this.#iconSrc()`, `this.#siteSelected()`, `this.sites.map()`
- 条件付き依存: `if (!this.sites.length)` → `html()`
- 参照: `site.hostname`, `site.label`, `site.url`, `this.sites.length`
