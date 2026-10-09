# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/AppMenu.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/AppMenu.sys.mjs
source-hash: c044b557c645968ae169d71bc296292f63249bbe
lines: 78

## <module>
- 役割: (未記入)

## init()
- 位置: L8-8
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: async L13-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `reopenAppMenu()`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L22-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.waitForEvent()`, `Services.wm.getMostRecentWindow()`, `browserWindow.document.getElementById()`, `browserWindow.document.getElementById("appMenu-library-button").click()`, `reopenAppMenu()`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L38-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.waitForEvent()`, `Services.wm.getMostRecentWindow()`, `browserWindow.document.getElementById()`, `browserWindow.document.getElementById("appMenu-help-button2").click()`, `reopenAppMenu()`
- XPCOM: `Services.wm`

## reopenAppMenu()
- 位置: async L54-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.waitForEvent()`, `browserWindow.PanelUI.hide()`, `browserWindow.PanelUI.show()`
- 参照: `browserWindow.PanelUI.panel`

## verifyConfigHelper()
- 位置: L64-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isCustomizing()`

## isCustomizing()
- 位置: L71-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.document.documentElement.hasAttribute()`
- XPCOM: `Services.wm`
