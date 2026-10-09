# browser/components/aiwindow/models/ManageTabs.sys.mjs

source: browser/components/aiwindow/models/ManageTabs.sys.mjs
source-hash: cc9b8299d2f7fb8bcc1cebe2eb79bc1851b889bb
lines: 467

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## findMatchingAIWindowTabs()
- 位置: L39-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `validUrls.has()`
- 条件付き依存: `if (validUrls.has(url))` → `matchedTabs.push()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser?.currentURI?.spec`, `tab.linkedPanel`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## shouldRequireUserConfirmation()
- 位置: L71-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.some()`
- 条件付き依存: `if (topAIWin)` → `tabs.filter(({ win }) => win === topAIWin).map()`
- 条件付き依存: `if (topAIWin)` → `tabs.filter()`
- 条件付き依存: `if (topAIWin)` → `topAIWin.gBrowser.tabs.every()`
- 条件付き依存: `if (topAIWin)` → `topWinTabs.has()`
- 参照: `securityProperties?.untrustedInput`, `tab.pinned`, `topWinTabs.size`, `win.gBrowser.selectedTab`

## runManageTabsFlow()
- 位置: async L101-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `gatherTabs()`, `lazy.ToolUITelemetry.recordBrowserActionComplete()`, `shouldRequireUserConfirmation()`, `toolHandler.getToolResults()`, `toolHandler.takeUIAction()`
- 条件付き依存: `if (toolHandler.action === GROUP_TABS)` → `offerChatTab()`
- 条件付き依存: `if ( state.askConfirmation || shouldRequireUserConfirmation( gatheredResult.matchedTabs, gatheredResult.topAIWin, state.conversation.securityProperties ) )` → `lazy.ToolUI.registerTabKeys()`
- 条件付き依存: `if ( state.askConfirmation || shouldRequireUserConfirmation( gatheredResult.matchedTabs, gatheredResult.topAIWin, state.conversation.securityProperties ) )` → `state.conversation.stashPendingBrowserActionTelemetry()`
- 条件付き依存: `if ( state.askConfirmation || shouldRequireUserConfirmation( gatheredResult.matchedTabs, gatheredResult.topAIWin, state.conversation.securityProperties ) )` → `toolHandler.getConfirmationProperties()`
- 条件付き依存: `if (!result || !result.operationIds?.length)` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 参照: `gatheredResult.earlyResult`, `gatheredResult.matchedTabs`, `gatheredResult.summarizedTabInfo`, `gatheredResult.tabKeyByToken`, `gatheredResult.tabs`, `gatheredResult.topAIWin`, `result.operationIds`, `result.operationIds?.length`, `state.askConfirmation`, `state.baseTelemetryInfo`, `state.conversation`, `state.conversation.securityProperties`, `state.toolCallId`, `state.validUrls`, `telemetryValues.affectedCount`, `telemetryValues.failedCount`, `telemetryValues.telemetryResult`, `toolHandler.action`, `toolHandler.failureError`, `toolHandler.failureMessage`, `toolHandler.verb`

## offerChatTab()
- 位置: L206-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `gathered.tabKeyByToken.set()`, `gathered.tabs.push()`, `lazy.ToolUI.findChatTab()`, `sanitizeUntrustedContent()`
- 参照: `chatTab.documentGlobal?.gBrowser?.selectedTab`, `chatTab.label`, `chatTab.linkedBrowser?.currentURI?.spec`, `chatTab.permanentKey`, `chatTab.pinned`, `chatTab.userContextId`, `conversation?.id`
- XPCOM: `Services.uuid`

## gatherTabs()
- 位置: async L229-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `findMatchingAIWindowTabs()`, `matchedTabs.map()`, `sanitizeUntrustedContent()`, `tabKeyByToken.set()`, `tabs.map()`
- 条件付き依存: `if (!matchedTabs.length)` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 参照: `matchedTabs.length`, `tab.label`, `tab.permanentKey`, `tab.pinned`, `tab.userContextId`, `win.gBrowser.selectedTab`
- XPCOM: `Services.uuid`

## takeUIAction()
- 位置: async L290-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ToolUI.closeSelectedTabs()`
- 参照: `gatheredResult.tabKeyByToken`, `gatheredResult.tabs`, `gatheredResult.topAIWin`

## getConfirmationProperties()
- 位置: L298-300
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gatheredResult.tabs`

## getToolResults()
- 位置: L302-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(result.failedTabs ?? []) .map()`, `(result.failedTabs ?? []) .map(failedTab => failedTab.tab?.permanentKey) .filter()`, `closedTabs.filter()`, `failedKeys.has()`, `gatheredResult.tabKeyByToken.get()`, `gatheredResult.tabs.map()`, `lazy.ToolUITelemetry.browserActionResult()`
- 参照: `closedTabs.filter(tab => tab.closed).length`, `closedTabs.length`, `failedTab.tab?.permanentKey`, `result.failedTabs`, `tab.closed`

## makeGroupTabsToolHandler()
- 位置: L343-425
- 役割: (未記入)
- 触るとき: (未記入)

## getLabel()
- 位置: async L344-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allVisible.filter()`, `gatheredResult.matchedTabs .filter()`, `gatheredResult.matchedTabs .filter(m => m.win === gatheredResult.topAIWin) .map()`, `manager.getPredictedLabelForGroup()`, `rawTabs.includes()`
- 条件付き依存: `if (rawLabel)` → `sanitizeUntrustedContent(rawLabel, true).slice(0, 40).trim()`
- 条件付き依存: `if (rawLabel)` → `sanitizeUntrustedContent(rawLabel, true).slice()`
- 条件付き依存: `if (rawLabel)` → `sanitizeUntrustedContent()`
- 参照: `gatheredResult.topAIWin`, `gatheredResult.topAIWin.gBrowser.visibleTabs`, `lazy.SmartTabGroupingManager`, `m.tab`, `m.win`, `t.pinned`

## getConfirmationProperties()
- 位置: async L367-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLabel()`
- 参照: `gatheredResult.tabs`

## takeUIAction()
- 位置: async L374-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLabel()`, `lazy.ToolUI.createTabGroup()`
- 参照: `gathered.tabKeyByToken`, `gathered.tabs`, `gathered.topAIWin`, `result.group.id`, `result?.group?.id`

## getToolResults()
- 位置: L391-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(result.failedTabs ?? []) .map()`, `(result.failedTabs ?? []) .map(failedTab => failedTab.tab?.linkedPanel) .filter()`, `failedPanels.has()`, `gatheredResult.tabs.map()`, `groupedTabs.filter()`, `lazy.ToolUITelemetry.browserActionResult()`
- 参照: `failedTab.tab?.linkedPanel`, `groupedTabs.filter(tab => tab.grouped).length`, `groupedTabs.length`, `result.failedTabs`, `result.label`, `tab.grouped`

## manageTabsAction()
- 位置: async L434-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeHandler()`, `runManageTabsFlow()`

## [CLOSE_TABS]()
- 位置: L446-446
- 役割: (未記入)
- 触るとき: (未記入)

## [GROUP_TABS]()
- 位置: L447-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeGroupTabsToolHandler()`
