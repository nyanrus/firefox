# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Tabs.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/Tabs.sys.mjs
source-hash: e9f82e15b5ca179cf9b517de74967a8ab6b27e23
lines: 220

## <module>
- 役割: (未記入)

## init()
- 位置: L13-13
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: async L18-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `allTabTitlesDisplayed()`, `fiveTabsHelper()`, `hoverTab()`, `setTimeout()`
- 参照: `browserWindow.gBrowser.tabs`
- XPCOM: `Services.wm`

## applyConfig()
- 位置: async L32-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.wm.getMostRecentWindow()`, `allTabTitlesDisplayed()`, `browserWindow.gBrowser.addTab()`, `browserWindow.gBrowser.pinTab()`, `browserWindow.gBrowser.selectTabAtIndex()`, `fiveTabsHelper()`, `hoverTab()`, `setTimeout()`
- 参照: `browserWindow.gBrowser.tabContainer.newTabButton`, `browserWindow.gBrowser.tabs`
- XPCOM: `Services.scriptSecurityManager` / `Services.wm`

## applyConfig()
- 位置: async L71-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.wm.getMostRecentWindow()`, `allTabTitlesDisplayed()`, `browserWindow.gBrowser.loadTabs()`, `browserWindow.gBrowser.pinTab()`, `browserWindow.gBrowser.selectTabAtIndex()`, `browserWindow.gBrowser.tabContainer.arrowScrollbox.scrollByIndex()`, `fiveTabsHelper()`, `hoverTab()`, `setTimeout()`
- 参照: `browserWindow.gBrowser.tabs`
- XPCOM: `Services.scriptSecurityManager` / `Services.wm`

## allTabTitlesDisplayed()
- 位置: async L138-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `TestUtils.waitForCondition()`, `getSpec()`, `tabTitlePromises.push()`
- 参照: `browserWindow.gBrowser.tabs`, `tab.label`

## getSpec()
- 位置: L151-157
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab.linkedBrowser`, `tab.linkedBrowser.documentURI`, `tab.linkedBrowser.documentURI.spec`

## tabTitleLoaded()
- 位置: L158-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSpec()`
- 参照: `tab.label`

## fiveTabsHelper()
- 位置: L174-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.wm.getMostRecentWindow()`, `browserWindow.gBrowser.loadTabs()`, `browserWindow.gBrowser.selectTabAtIndex()`, `closeAllButOneTab()`
- XPCOM: `Services.scriptSecurityManager` / `Services.wm`

## closeAllButOneTab()
- 位置: L196-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.wm.getMostRecentWindow()`, `gBrowser.removeTab()`, `gBrowser.selectedBrowser.loadURI()`, `hoverTab()`
- 条件付き依存: `if (gBrowser.selectedTab.pinned)` → `gBrowser.unpinTab()`
- 参照: `browserWindow.gBrowser`, `gBrowser.selectedTab`, `gBrowser.selectedTab.pinned`, `gBrowser.tabContainer.newTabButton`, `gBrowser.tabs.length`
- XPCOM: `Services.io` / `Services.scriptSecurityManager` / `Services.wm`

## hoverTab()
- 位置: L213-219
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (hover)` → `InspectorUtils.addPseudoClassLock()`
- 条件付き依存: `if (!(hover))` → `InspectorUtils.clearPseudoClassLocks()`
