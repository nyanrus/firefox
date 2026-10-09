# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/WindowSize.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/WindowSize.sys.mjs
source-hash: 5956aecbd7b02ae64852499bef3c8edcdbd724b3
lines: 69

## <module>
- 役割: (未記入)

## init()
- 位置: L9-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L16-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `setTimeout()`, `toggleFullScreen()`
- XPCOM: `Services.wm`

## waitToLeaveFS()
- 位置: L24-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.maximize()`, `resolve()`

## applyConfig()
- 位置: async L34-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.restore()`, `setTimeout()`, `toggleFullScreen()`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L47-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `setTimeout()`, `toggleFullScreen()`
- XPCOM: `Services.wm`

## toggleFullScreen()
- 位置: L60-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TestUtils.waitForCondition()`, `browserWindow.document.documentElement.hasAttribute()`
- 参照: `browserWindow.fullScreen`
