# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/UIDensities.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/UIDensities.sys.mjs
source-hash: 9fa7cf32bfda6ae28e9c1e52f8b5488265090052
lines: 43

## <module>
- 役割: (未記入)

## init()
- 位置: L6-6
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: async L11-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.gCustomizeMode.setUIDensity()`
- 参照: `browserWindow.gUIDensity.MODE_COMPACT`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L22-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.gCustomizeMode.setUIDensity()`
- 参照: `browserWindow.gUIDensity.MODE_NORMAL`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L33-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.gCustomizeMode.setUIDensity()`
- 参照: `browserWindow.gUIDensity.MODE_TOUCH`
- XPCOM: `Services.wm`
