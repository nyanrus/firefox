# browser/components/aiwindow/ui/modules/TabManagementService.sys.mjs

source: browser/components/aiwindow/ui/modules/TabManagementService.sys.mjs
source-hash: e445201e38866f42cb5612e70c74e500cd60b217
lines: 1015

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## TabManagementService.constructor()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionStore`

## TabManagementService.restoreTabs()
- 位置: async L101-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `failedTabs.push()`, `lazy.console.error()`, `operation.windowRef?.get()`, `this.#findClosedTabIndexForOperationTab()`, `this.#recentCloseOperations.get()`, `this.#sessionStore.undoCloseTab()`, `window.gBrowser.tabs.includes()`
- 条件付き依存: `if (!operation)` → `lazy.console.warn()`
- 条件付き依存: `if (!window?.gBrowser)` → `lazy.console.warn()`
- 条件付き依存: `if (!window?.gBrowser)` → `operation.closedTabs.map()`
- 条件付き依存: `if (closedTabIndex == null)` → `failedTabs.push()`
- 条件付き依存: `if (restoredTab)` → `restoredTabs.push()`
- 条件付き依存: `if (!(restoredTab))` → `failedTabs.push()`
- 条件付き依存: `if (!failedTabs.length)` → `this.#recentCloseOperations.delete()`
- 参照: `closedOperationTab.url`, `error.message`, `failedTabs.length`, `operation.closedTabs`, `operation.closedTabs.length`, `restoredTabs.length`, `window.gBrowser.selectedTab`, `window?.gBrowser`

## TabManagementService.storeClosedTabsForUndo()
- 位置: L212-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `Date.now()`, `this.#recentCloseOperations.set()`
- 条件付き依存: `if (this.#recentCloseOperations.size >= this.#MAX_STORED_OPERATIONS)` → `this.#recentCloseOperations.keys().next()`
- 条件付き依存: `if (this.#recentCloseOperations.size >= this.#MAX_STORED_OPERATIONS)` → `this.#recentCloseOperations.keys()`
- 条件付き依存: `if (this.#recentCloseOperations.size >= this.#MAX_STORED_OPERATIONS)` → `this.#recentCloseOperations.delete()`
- 参照: `closedTabs?.length`, `this.#MAX_STORED_OPERATIONS`, `this.#operationCounter`, `this.#recentCloseOperations.keys().next().value`, `this.#recentCloseOperations.size`

## TabManagementService.getStoredTabsForUndo()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recentCloseOperations.get()`

## TabManagementService.createTabGroup()
- 位置: async L268-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.error()`, `this.#getNextUnusedColor()`, `this.#validateTabsForGrouping()`, `window.gBrowser.addTabGroup()`
- 条件付き依存: `if (!tabs?.length)` → `lazy.console.warn()`
- 参照: `error.message`, `group.color`, `group.id`, `group.label`, `group.tabs.length`, `tabs?.length`, `validTabs.length`, `window?.gBrowser`

## TabManagementService.openTabs()
- 位置: L363-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `failedUrls.push()`, `lazy.console.error()`, `openedTabs.push()`, `window.gBrowser.addTab()`
- 条件付き依存: `if (!urls?.length)` → `lazy.console.warn()`
- 参照: `error.message`, `urls?.length`, `window?.gBrowser`
- XPCOM: `Services.scriptSecurityManager`

## TabManagementService.switchToTab()
- 位置: L402-408
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!tab || !window?.gBrowser)` → `lazy.console.warn()`
- 参照: `window.gBrowser.selectedTab`, `window?.gBrowser`

## TabManagementService.findOpenTab()
- 位置: L420-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `excludeTabs?.has()`, `window.gBrowser.tabs.find()`
- 参照: `Services.io.newURI(url).spec`, `tab.closing`, `tab.linkedBrowser?.currentURI?.spec`, `window?.gBrowser`
- XPCOM: `Services.io`

## TabManagementService.resolveOrOpenTabs()
- 位置: async L458-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `failedUrls.push()`, `resolvedTabs.push()`, `this.findOpenTab()`, `this.openTabs()`
- 条件付き依存: `if (!tabs?.length)` → `lazy.console.warn()`
- 条件付き依存: `if (existingTab && !existingTab.pinned && !existingTab.group)` → `claimedTabs.add()`
- 条件付き依存: `if (existingTab && !existingTab.pinned && !existingTab.group)` → `resolvedTabs.push()`
- 参照: `existingTab.group`, `existingTab.pinned`, `tabs?.length`, `window?.gBrowser`

## TabManagementService.ungroupTabs()
- 位置: async L521-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.error()`, `tabsInGroup.map()`, `window.gBrowser.tabGroups.find()`, `window.gBrowser.ungroupTab()`
- 参照: `error.message`, `g.id`, `group.tabs`, `tab.label`, `tab.linkedBrowser?.currentURI?.spec`, `tab.linkedPanel`, `window?.gBrowser`

## TabManagementService.getTabGroups()
- 位置: L593-602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabGroupInfo()`, `window.gBrowser.tabGroups .map()`, `window.gBrowser.tabGroups .map(group => this.#getTabGroupInfo(group)) .filter()`
- 条件付き依存: `if (!window?.gBrowser)` → `lazy.console.warn()`
- 参照: `group.tabCount`, `window?.gBrowser`

## TabManagementService.getTabGroupById()
- 位置: L616-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabGroupInfo()`, `window.gBrowser.tabGroups.find()`
- 条件付き依存: `if (!groupId || !window?.gBrowser)` → `lazy.console.warn()`
- 参照: `g.id`, `groupInfo.tabCount`, `window?.gBrowser`

## TabManagementService.#getTabGroupInfo()
- 位置: L642-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isAllowedURLProtocol()`, `isNewPageUrl()`
- 条件付き依存: `if ( !tab.hidden && !tab.closing && isAllowedURLProtocol(url) && !isNewPageUrl(url) )` → `tabs.push()`
- 条件付き依存: `if ( !tab.hidden && !tab.closing && isAllowedURLProtocol(url) && !isNewPageUrl(url) )` → `sanitizeUntrustedContent()`
- 参照: `group.color`, `group.id`, `group.label`, `group.tabs`, `tab.closing`, `tab.hidden`, `tab.label`, `tab.lastAccessed`, `tab.linkedBrowser?.currentURI?.spec`, `tabs.length`

## TabManagementService.#getNextUnusedColor()
- 位置: L678-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`, `TabManagementService.TAB_GROUP_COLORS.find()`, `usedColors.has()`, `window.gBrowser.getAllTabGroups()`, `window.gBrowser.getAllTabGroups().map()`
- 参照: `TabManagementService.TAB_GROUP_COLORS`, `TabManagementService.TAB_GROUP_COLORS.length`, `group.color`

## TabManagementService.getGroupingRejection()
- 位置: L714-729
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab.closing`, `tab.documentGlobal`, `tab.group`, `tab.pinned`, `tab?.linkedBrowser`

## TabManagementService.#validateTabsForGrouping()
- 位置: L731-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.forEach()`, `this.getGroupingRejection()`, `validTabs.push()`
- 条件付き依存: `if (reason)` → `failedTabs.push()`

## TabManagementService.closeTabs()
- 位置: async L755-796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#performTabClosing()`, `this.#validateTabsForClosing()`
- 条件付き依存: `if (!tabs?.length)` → `lazy.console.warn()`
- 条件付き依存: `if (closedTabs.length)` → `this.storeClosedTabsForUndo()`
- 条件付き依存: `if (error)` → `lazy.console.error()`
- 条件付き依存: `if (error)` → `failedTabs.push()`
- 参照: `closedTabs.length`, `error.message`, `tabs.length`, `tabs?.length`, `window?.gBrowser`

## TabManagementService.#validateTabsForClosing()
- 位置: L807-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.filter()`
- 条件付き依存: `if (!tabInWindow)` → `failedTabs.push()`
- 条件付き依存: `if (tab.closing)` → `failedTabs.push()`
- 参照: `tab.closing`, `tab.documentGlobal`, `tab?.linkedBrowser`

## TabManagementService.#performTabClosing()
- 位置: async L839-867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `closedTabs.push()`, `this.#getTabInfo()`, `window.gBrowser.removeTab()`

## TabManagementService.#compareClosedTabTimestamps()
- 位置: L869-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `matches.slice()`
- 参照: `bestMatch.closedAt`, `bestMatch.index`, `match.closedAt`

## TabManagementService.#findClosedTabIndexForOperationTab()
- 位置: L894-918
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedTabData.entries()`, `this.#closedTabMatchesOperationTab()`, `this.#compareClosedTabTimestamps()`, `this.#getClosedTabData()`
- 条件付き依存: `if (this.#closedTabMatchesOperationTab(closedTab, operationTab))` → `matches.push()`
- 参照: `closedTab.closedAt`, `closedTab.state?.closedAt`, `matches.length`, `matches[0].index`, `operationTab.operationTimestamp`

## TabManagementService.#closedTabMatchesOperationTab()
- 位置: L928-938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#normalizeClosedTab()`
- 参照: `closedTabInfo.url`, `closedTabInfo.userContextId`, `operationTab.url`, `operationTab.userContextId`

## TabManagementService.#getClosedTabData()
- 位置: L947-950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `this.#sessionStore.getClosedTabDataForWindow()`

## TabManagementService.#normalizeClosedTab()
- 位置: L965-984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `entries.at()`
- 参照: `activeEntry?.title`, `activeEntry?.url`, `closedTab?.state`, `closedTab?.title`, `closedTab?.userContextId`, `state.entries`, `state.index`, `state.originAttributes?.userContextId`, `state.pinned`, `state.title`, `state.url`, `state.userContextId`

## TabManagementService.#getTabInfo()
- 位置: L999-1011
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.getAttribute()`
- 参照: `browser.contentPrincipal`, `browser.currentURI?.spec`, `principal?.originAttributes?.userContextId`, `tab.label`, `tab.linkedBrowser`, `tab.userContextId`
