# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/CustomizeMode.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/CustomizeMode.sys.mjs
source-hash: e7b319fdd67841041178dfc8550f834d3542c0d6
lines: 73

## <module>
- 役割: (未記入)

## init()
- 位置: L8-8
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: L13-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.document.documentElement.hasAttribute()`, `browserWindow.gCustomizeMode.exit()`, `browserWindow.gNavToolbox.addEventListener()`
- 条件付き依存: `if ( !browserWindow.document.documentElement.hasAttribute("customizing") )` → `resolve()`
- XPCOM: `Services.wm`

## onCustomizationEnds()
- 位置: L23-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.gNavToolbox.removeEventListener()`, `resolve()`, `setTimeout()`

## applyConfig()
- 位置: L45-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.document.documentElement.hasAttribute()`, `browserWindow.gCustomizeMode.enter()`, `browserWindow.gNavToolbox.addEventListener()`
- 条件付き依存: `if ( browserWindow.document.documentElement.hasAttribute("customizing") )` → `resolve()`
- XPCOM: `Services.wm`

## onCustomizing()
- 位置: L55-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.gNavToolbox.removeEventListener()`, `resolve()`, `setTimeout()`
