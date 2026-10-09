# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/DevTools.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/DevTools.sys.mjs
source-hash: d07b9be0e5065a166387560672faac4c2b5c658f
lines: 75

## <module>
- 役割: (未記入)
- 呼び出し先: `require()`

## showToolboxForSelectedTab()
- 位置: async L11-15
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `gDevTools.showToolboxForTab()`
- 参照: `browserWindow.gBrowser.selectedTab`
- XPCOM: `Services.wm`

## selectToolbox()
- 位置: L17-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolbox.win.document.querySelector()`

## init()
- 位置: L22-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panels.forEach()`
- 参照: `this.configurations`, `this.configurations[panel].applyConfig`

## this.configurations[panel].applyConfig()
- 位置: async L34-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`, `selectToolbox.bind()`, `setTimeout()`, `showToolboxForSelectedTab()`
- 参照: `this.selectors`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L45-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `selectToolbox.bind()`, `setTimeout()`, `showToolboxForSelectedTab()`
- 参照: `this.selectors`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectToolbox.bind()`, `setTimeout()`, `showToolboxForSelectedTab()`
- 参照: `this.selectors`

## verifyConfig()
- 位置: async L58-60
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: async L64-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectToolbox.bind()`, `setTimeout()`, `showToolboxForSelectedTab()`
- 参照: `this.selectors`

## verifyConfig()
- 位置: async L69-71
- 役割: (未記入)
- 触るとき: (未記入)
