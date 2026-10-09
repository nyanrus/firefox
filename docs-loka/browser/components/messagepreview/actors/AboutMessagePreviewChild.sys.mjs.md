# browser/components/messagepreview/actors/AboutMessagePreviewChild.sys.mjs

source: browser/components/messagepreview/actors/AboutMessagePreviewChild.sys.mjs
source-hash: 3e8234ebdb773592fa8eea91162fd7457b146158
lines: 68

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## log()
- 位置: L8-13
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## AboutMessagePreviewChild.handleEvent()
- 位置: L17-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 参照: `event.type`

## AboutMessagePreviewChild.actorCreated()
- 位置: L21-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.exportFunctions()`

## AboutMessagePreviewChild.exportFunctions()
- 位置: L25-33
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.contentWindow)` → `Cu.exportFunction()`
- 条件付き依存: `if (this.contentWindow)` → `this[name].bind()`
- 参照: `this.contentWindow`

## AboutMessagePreviewChild.MPIsEnabled()
- 位置: L41-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## AboutMessagePreviewChild.MPToggleLights()
- 位置: async L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.matchMedia()`, `this.sendQuery()`
- 参照: `this.contentWindow.matchMedia( "(prefers-color-scheme: dark)" ).matches`

## AboutMessagePreviewChild.MPShowMessage()
- 位置: async L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`
