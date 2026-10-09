# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/PermissionPrompts.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/PermissionPrompts.sys.mjs
source-hash: 4b8b098e0ab136524e4f79021dcd918b5bfef417
lines: 171

## <module>
- 役割: (未記入)

## init()
- 位置: L16-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L25-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L33-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L41-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L57-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L65-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L73-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## beforeContentFn()
- 位置: L76-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `E10SUtils.wrapHandlingUserInput()`, `content.document.querySelector()`, `element.setUserInput()`

## applyConfig()
- 位置: async L92-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickOn()`, `closeLastTab()`

## applyConfig()
- 位置: async L100-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `clickOn()`, `closeLastTab()`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L110-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Services.prefs.setBoolPref()`, `Services.wm.getMostRecentWindow()`, `TestUtils.waitForCondition()`, `TestUtils.waitForCondition( () => !notification.hidden, "addon install confirmation did not show", 200 ).catch()`, `browserWindow.document.getElementById()`, `clickOn()`, `closeLastTab()`
- 参照: `notification.hidden`
- XPCOM: `Services.prefs` / `Services.wm`

## closeLastTab()
- 位置: async L136-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.removeTab()`

## clickOn()
- 位置: async L144-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.openNewForegroundTab()`, `BrowserTestUtils.waitForEvent()`, `EventUtils.synthesizeClick()`, `Services.wm.getMostRecentWindow()`, `SpecialPowers.spawn()`, `content.document.querySelector()`
- 条件付き依存: `if (beforeContentFn)` → `SpecialPowers.spawn()`
- 参照: `browserWindow.PopupNotifications.panel`, `browserWindow.gBrowser`, `lastTab.documentGlobal`, `lastTab.linkedBrowser`
- XPCOM: `Services.wm`
