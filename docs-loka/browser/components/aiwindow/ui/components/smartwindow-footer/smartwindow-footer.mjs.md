# browser/components/aiwindow/ui/components/smartwindow-footer/smartwindow-footer.mjs

source: browser/components/aiwindow/ui/components/smartwindow-footer/smartwindow-footer.mjs
source-hash: 0a0928a85019079837c06430176ed18aba6d5a41
lines: 58

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartwindowFooter.handleActionClick()
- 位置: L14-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_ACTIONS.includes()`, `topWin.FirefoxViewHandler.openTab()`
- 条件付き依存: `if (!ALLOWED_ACTIONS.includes(action))` → `console.warn()`
- 参照: `window.browsingContext.topChromeWindow`

## SmartwindowFooter.render()
- 位置: L24-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.handleActionClick()`
