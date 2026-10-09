# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Buttons.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Buttons.sys.mjs
source-hash: b0b4bb74d185877151affff497097e341e50b5c5
lines: 97

## <module>
- 役割: (未記入)

## init()
- 位置: L8-10
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createWidget()`

## applyConfig()
- 位置: async L15-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_NAVBAR`

## applyConfig()
- 位置: async L25-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_TABSTRIP`

## applyConfig()
- 位置: async L35-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`

## verifyConfig()
- 位置: async L42-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 参照: `browserWindow.PanelUI.panel.state`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeWidgetFromArea()`

## verifyConfig()
- 位置: async L58-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.document.documentElement.hasAttribute()`
- XPCOM: `Services.wm`

## createWidget()
- 位置: L72-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.createWidget()`, `Services.wm.getMostRecentWindow()`, `browserWindow.document.createElementNS()`, `browserWindow.document.createTextNode()`, `browserWindow.document.documentElement.appendChild()`, `st.appendChild()`
- XPCOM: `Services.wm`
