# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Preferences.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Preferences.sys.mjs
source-hash: 6f37f7022e1c87d30eec958c1f20ad513bb2d961
lines: 169

## <module>
- 役割: (未記入)

## init()
- 位置: L11-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `primary.replace()`
- 条件付き依存: `if (!(primary == "panePrivacy" && customFn))` → `prefHelper.bind()`
- 参照: `customFn.name`, `this.configurations`, `this.configurations[configName].applyConfig`, `this.configurations[configName].selectors`

## this.configurations[configName].applyConfig()
- 位置: async L32-34
- 役割: (未記入)
- 触るとき: (未記入)

## prefHelper()
- 位置: async L48-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `browserWindow.openPreferences()`, `content.window.gSubDialog.close()`, `selectedBrowser.documentGlobal.SpecialPowers.spawn()`
- 条件付き依存: `if (selectedBrowser.currentURI.specIgnoringRef == "about:preferences")` → `primary.replace()`
- 条件付き依存: `if ( selectedBrowser.currentURI.spec == "about:preferences#" + primary.replace(/^pane/, "") )` → `Promise.resolve()`
- 条件付き依存: `if (!( selectedBrowser.currentURI.spec == "about:preferences#" + primary.replace(/^pane/, "") ))` → `browserWindow.requestAnimationFrame()`
- 条件付き依存: `if (!(selectedBrowser.currentURI.specIgnoringRef == "about:preferences"))` → `TestUtils.topicObserved()`
- 条件付き依存: `if (customFn)` → `paintPromise()`
- 条件付き依存: `if (customFn)` → `customFn()`
- 参照: `browserWindow.gBrowser.selectedBrowser`, `content.window.gSubDialog`, `content.window.gSubDialog._topDialog`, `selectedBrowser.currentURI.spec`, `selectedBrowser.currentURI.specIgnoringRef`
- XPCOM: `Services.wm`

## paintPromise()
- 位置: L94-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.addEventListener()`, `resolve()`

## tabsGroup()
- 位置: async L106-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.SpecialPowers.spawn()`, `content.document .querySelector()`, `content.document .querySelector('setting-group[groupid="tabs"]') .scrollIntoView()`

## cacheGroup()
- 位置: async L118-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.SpecialPowers.spawn()`, `content.document .querySelector()`, `content.document .querySelector('setting-group[groupid="cookiesAndSiteData2"]') .scrollIntoView()`

## connectionDialog()
- 位置: async L130-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.SpecialPowers.spawn()`, `content.document.getElementById()`, `content.document.getElementById("connectionSettings").click()`

## clearRecentHistoryDialog()
- 位置: async L140-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.SpecialPowers.spawn()`, `content.document.getElementById()`, `content.document.getElementById("clearSiteDataButton").click()`

## certManager()
- 位置: async L150-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.SpecialPowers.spawn()`, `content.document.getElementById()`, `content.document.getElementById("viewCertificatesButton").click()`

## deviceManager()
- 位置: async L160-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.SpecialPowers.spawn()`, `content.document.getElementById()`, `content.document.getElementById("viewSecurityDevicesButton").click()`
