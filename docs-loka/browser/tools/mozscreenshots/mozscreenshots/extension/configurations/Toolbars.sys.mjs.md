# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Toolbars.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Toolbars.sys.mjs
source-hash: 86a00644370167cc04970d28cec27768e97bf8f3
lines: 55

## <module>
- 役割: (未記入)

## init()
- 位置: L6-6
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: async L11-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.document.getElementById()`, `browserWindow.setToolbarVisibility()`, `toggleMenubarIfNecessary()`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L23-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.document.getElementById()`, `browserWindow.setToolbarVisibility()`, `toggleMenubarIfNecessary()`
- XPCOM: `Services.wm`

## verifyConfig()
- 位置: async L33-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 参照: `browserWindow.fullScreen`
- XPCOM: `Services.wm`

## toggleMenubarIfNecessary()
- 位置: L47-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (Services.appinfo.OS != "Darwin" /* && !browserWindow.fullScreen*/)` → `browserWindow.document.getElementById()`
- 条件付き依存: `if (Services.appinfo.OS != "Darwin" /* && !browserWindow.fullScreen*/)` → `browserWindow.setToolbarVisibility()`
- 参照: `Services.appinfo.OS`
- XPCOM: `Services.appinfo` / `Services.wm`
