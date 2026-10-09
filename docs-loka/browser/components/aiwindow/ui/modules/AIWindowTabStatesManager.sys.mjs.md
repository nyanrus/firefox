# browser/components/aiwindow/ui/modules/AIWindowTabStatesManager.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowTabStatesManager.sys.mjs
source-hash: 17b2cc833de8e2c3e39f19cb85bc0a97e7a7fd3f
lines: 1147

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## hasInputContent()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `input?.mentions?.length`, `input?.text`

## AIWindowTabStatesManager.constructor()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#init()`

## AIWindowTabStatesManager.getActiveConversation()
- 位置: L117-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabStates.get()`
- 参照: `this.#tabStates.get(tab)?.state?.conversation`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.getTabConversationId()
- 位置: L131-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabStates.get()`
- 参照: `state.conversation`, `state.conversation.messageCount`, `state.conversationId`, `state?.conversationId`, `this.#tabStates.get(tab)?.state`

## AIWindowTabStatesManager.getConversationTab()
- 位置: L149-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.find()`, `this.#tabStates.get()`
- 参照: `tabState.state.conversationId`, `this.#window.gBrowser.tabs`

## AIWindowTabStatesManager.openSidebarForReturningUser()
- 位置: async L165-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getKeepSidebarOpenState()`, `lazy.AIWindowUI.isSidebarOpen()`, `this.#getTabState()`
- 条件付き依存: `if ( getKeepSidebarOpenState( this.#getTabState(tab)?.state, lazy.sidebarOpenByDefault ) )` → `lazy.AIWindowUI.openSidebar()`
- 参照: `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser.currentURI.spec`, `tabState?.state?.keepSidebarOpen`, `this.#getTabState(tab)?.state`, `this.#restorePromise`, `this.#window`, `this.#window.gBrowser.selectedTab`

## AIWindowTabStatesManager.#init()
- 位置: L199-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabContainer.addEventListener()`, `this.#addWindowEventListeners()`, `this.#getTabsListener()`, `this.#restoreInitialTabSidebar()`, `this.#setUpInitialTabs()`, `this.#window.gBrowser.addProgressListener()`
- 参照: `this.#restorePromise`, `this.#tabStates`, `this.#tabsListener`, `this.#window`, `this.#window.gBrowser.tabContainer`

## AIWindowTabStatesManager.uninit()
- 位置: L220-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabContainer.removeEventListener()`, `this.#removeWindowEventListeners()`, `this.#window.gBrowser.removeProgressListener()`
- 参照: `this.#tabStates`, `this.#tabsListener`, `this.#window`, `this.#window.gBrowser.tabContainer`

## AIWindowTabStatesManager.#addWindowEventListeners()
- 位置: L237-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.addEventListener()`
- 参照: `this.#onAIWindowConnected`, `this.#onCloseSidebar`, `this.#onContextChipsChanged`, `this.#onConversationChanged`, `this.#onConversationCleared`, `this.#onConversationOpened`, `this.#onModelChanged`, `this.#onSidebarNavigating`, `this.#onSidebarToggle`, `this.#onSmartbarInput`

## AIWindowTabStatesManager.#removeWindowEventListeners()
- 位置: L292-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.removeEventListener()`
- 参照: `this.#onAIWindowConnected`, `this.#onCloseSidebar`, `this.#onConversationChanged`, `this.#onConversationCleared`, `this.#onConversationOpened`, `this.#onModelChanged`, `this.#onSidebarNavigating`, `this.#onSidebarToggle`, `this.#onSmartbarInput`

## AIWindowTabStatesManager.#setUpInitialTabs()
- 位置: L345-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addTabState()`, `this.#tabStates.has()`, `this.#window.gBrowser.tabs.forEach()`

## AIWindowTabStatesManager.handleEvent()
- 位置: L362-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onTabClose()`, `this.#onTabOpen()`, `this.#onTabRestoring()`, `this.#onTabSelect()`
- 参照: `event.type`

## AIWindowTabStatesManager.#onTabOpen()
- 位置: L390-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.tabsOpened.add()`, `this.#addTabState()`
- 参照: `event.target`

## AIWindowTabStatesManager.#onTabSelect()
- 位置: async L413-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getKeepSidebarOpenState()`, `this.#getTabState()`, `this.#openSidebarForTab()`
- 条件付き依存: `if (tabUrl === lazy.AIWINDOW_URL)` → `lazy.AIWindowUI.restoreMemoriesState()`
- 条件付き依存: `if (tabUrl === lazy.AIWINDOW_URL)` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `Promise.resolve()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `tab.hasAttribute()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `lazy.SessionStore.isTabRestoring()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `this.#getTabState()`
- 条件付き依存: `if (!shouldKeepSidebar)` → `lazy.AIWindowUI.updateSidebarInput()`
- 条件付き依存: `if (!shouldKeepSidebar)` → `lazy.AIWindowUI.closeSidebar()`
- 参照: `event.target`, `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser?.currentURI?.spec`, `tabState?.state`, `tabState?.state?.conversationId`, `this.#window`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.#onTabRestoring()
- 位置: async L476-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getKeepSidebarOpenState()`, `this.#openSidebarForTab()`, `this.#refreshTabStateFromSession()`
- 参照: `event.target`, `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser?.currentURI?.spec`, `tabState.state`, `tabState.state?.conversationId`, `this.#window`, `this.#window.gBrowser.selectedTab`

## AIWindowTabStatesManager.#openSidebarForTab()
- 位置: async L514-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.openSidebar()`, `lazy.AIWindowUI.updateSidebarModel()`, `this.#resolveTabModelChoice()`, `this.#updateSidebarState()`
- 条件付き依存: `if (tabState?.state?.conversationId && !conversation)` → `this.#computeConversation()`
- 参照: `tabState.state?.conversation`, `tabState?.state?.conversationId`, `this.#window`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.#refreshTabStateFromSession()
- 位置: L546-565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.SessionStore.getCustomTabValue()`, `this.#tabStates.get()`
- 条件付き依存: `if (saved?.conversationId)` → `this.#tabStates.set()`
- 参照: `saved?.conversationId`, `tabState.state`, `this.#tabStates`

## AIWindowTabStatesManager.setTabStateConversation()
- 位置: L575-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 参照: `conversation.id`

## AIWindowTabStatesManager.#resolveTabModelChoice()
- 位置: L591-594
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabState.state?.modelChoiceId`

## AIWindowTabStatesManager.#computeConversation()
- 位置: async L606-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ChatStore.findConversationById()`
- 条件付き依存: `if (found)` → `this.#getTabState()`
- 参照: `tabState?.state?.conversation`, `tabState?.state?.conversationId`

## AIWindowTabStatesManager.#onTabClose()
- 位置: L632-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeEventListeners()`
- 参照: `event.target`

## AIWindowTabStatesManager.#addTabState()
- 位置: L643-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabStates.set()`

## AIWindowTabStatesManager.#removeEventListeners()
- 位置: L654-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabStates.delete()`

## AIWindowTabStatesManager.#onAIWindowConnected()
- 位置: async L665-719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasInputContent()`, `lazy.ChatStore.findConversationById()`, `this.#getTabState()`
- 条件付き依存: `if (!tabState.state?.conversationId)` → `this.#getTabState()`
- 条件付き依存: `if (needsSidebar)` → `lazy.AIWindowUI.updateSidebarInput()`
- 条件付き依存: `if (mode === "sidebar" && selectedTab === tab)` → `this.#updateSidebarState()`
- 条件付き依存: `if (mode === "sidebar" && selectedTab === tab)` → `lazy.AIWindowUI.updateSidebarModel()`
- 条件付き依存: `if (mode === "sidebar" && selectedTab === tab)` → `this.#resolveTabModelChoice()`
- 参照: `conversation.messages.length`, `event.detail`, `lazy.AIWINDOW_URL`, `stateUpdate.mode`, `tabState.state`, `tabState.state.input`, `tabState.state?.conversationId`, `this.#window`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.#updateSidebarState()
- 位置: L721-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.updateSidebarContextChips()`, `lazy.AIWindowUI.updateSidebarInput()`
- 参照: `tabState?.state?.contextChips`, `tabState?.state?.input`, `tabState?.state?.removedImplicitContextChip`, `this.#window`

## AIWindowTabStatesManager.#restoreInitialTabSidebar()
- 位置: async L739-779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `getKeepSidebarOpenState()`, `lazy.AIWindowUI.openSidebar()`, `lazy.ChatStore.findConversationById()`, `lazy.SessionStore.getCustomTabValue()`, `this.#getTabState()`
- 参照: `lazy.AIWINDOW_URL`, `lazy.SessionStore.promiseAllWindowsRestored`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser?.currentURI?.spec`, `this.#window`, `this.#window.gBrowser.selectedTab`

## AIWindowTabStatesManager.#getTabState()
- 位置: L792-852
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabStates.get()`
- 条件付き依存: `if (tabState.state === null)` → `lazy.SessionStore.getCustomTabValue()`
- 条件付き依存: `if (tabState.state === null)` → `JSON.parse()`
- 条件付き依存: `if (tabState.state === null)` → `this.#tabStates.set()`
- 条件付き依存: `if (newState)` → `this.#tabStates.set()`
- 条件付き依存: `if (conversationId && keepSidebarOpen !== false)` → `lazy.SessionStore.setCustomTabValue()`
- 条件付き依存: `if (conversationId && keepSidebarOpen !== false)` → `JSON.stringify()`
- 条件付き依存: `if (!(conversationId && keepSidebarOpen !== false))` → `lazy.SessionStore.deleteCustomTabValue()`
- 参照: `newState.tab`, `oldState.input`, `oldState.mode`, `tabState.state`, `tabState.state.input`, `tabState.state.mode`, `this.#tabStates`

## AIWindowTabStatesManager.#onSmartbarInput()
- 位置: L860-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 参照: `event.detail`, `event.detail.tab`

## AIWindowTabStatesManager.#onConversationOpened()
- 位置: L870-885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 参照: `event.detail`, `stateUpdate.mode`

## AIWindowTabStatesManager.#onConversationCleared()
- 位置: L893-907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 条件付き依存: `if (currentTabState?.state)` → `this.#getTabState()`
- 参照: `currentTabState.state`, `currentTabState?.state`, `event.detail`

## AIWindowTabStatesManager.#onConversationChanged()
- 位置: L919-940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.updateStarterPrompts()`
- 条件付き依存: `if (tab && conversation)` → `this.#getTabState()`
- 参照: `conversation.id`, `conversation.messageCount`, `conversation.transientStarterUrl`, `event.detail`, `tab.linkedBrowser.currentURI.spec`, `this.#window`

## AIWindowTabStatesManager.#onModelChanged()
- 位置: L948-956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 参照: `currentTabState.state`, `currentTabState?.state`, `event.detail`

## AIWindowTabStatesManager.#onContextChipsChanged()
- 位置: L964-975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 参照: `currentTabState?.state`, `event.detail`

## AIWindowTabStatesManager.#onSidebarToggle()
- 位置: L983-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 条件付き依存: `if (currentTabState?.state && source === "toggle")` → `this.#getTabState()`
- 条件付き依存: `if (source === "toggle")` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if (isOpen)` → `this.#updateSidebarState()`
- 条件付き依存: `if (!(isOpen))` → `this.#updateEmptyCloseCount()`
- 参照: `currentTabState.state`, `currentTabState?.state`, `currentTabState?.state?.conversation`, `event.detail`, `this.#window`

## AIWindowTabStatesManager.#updateEmptyCloseCount()
- 位置: L1023-1045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`, `["close", "toggle"].includes()`
- 条件付き依存: `if (lazy.sidebarEmptyCloseCount !== 0)` → `Services.prefs.setIntPref()`
- 参照: `conversation?.messageCount`, `lazy.sidebarEmptyCloseCount`
- XPCOM: `Services.prefs`

## AIWindowTabStatesManager.#onSidebarNavigating()
- 位置: L1054-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabState()`
- 参照: `event.detail.tab`

## AIWindowTabStatesManager.#onCloseSidebar()
- 位置: L1063-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.closeSidebar()`
- 参照: `this.#window`

## AIWindowTabStatesManager.#getTabsListener()
- 位置: L1070-1145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## onLocationChange()
- 位置: async L1077-1137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getKeepSidebarOpenState()`, `lazy.AIWindowUI.isSidebarOpen()`, `lazy.AIWindowUI.updateStarterPrompts()`, `this.#tabStates.get()`
- 条件付き依存: `if (!isAiWindowUrl)` → `lazy.SmartWindowTelemetry.recordUriLoad()`
- 条件付き依存: `if (isFullPageMode && isAiWindowUrl && isSidebarOpen)` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if ( isFullPageMode && !isAiWindowUrl && !isSidebarOpen && shouldKeepSidebarOpen )` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if ( isFullPageMode && !isAiWindowUrl && !isSidebarOpen && shouldKeepSidebarOpen )` → `this.#getTabState()`
- 条件付き依存: `if (!isAiWindowUrl && lazy.AIWindowUI.isSidebarOpen(this.#window))` → `lazy.AIWindowUI.updateSidebarInput()`
- 参照: `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `locationURI.spec`, `tabState.state`, `tabState.state.conversation`, `tabState.state.input`, `tabState.state.mode`, `tabState.state?.conversationId`, `this.#tabStates`, `this.#window`, `this.#window.gBrowser.selectedTab`, `webProgress.isTopLevel`

## AIWindowTabStatesManager.onStateChange()
- 位置: L1139-1139
- 役割: (未記入)
- 触るとき: (未記入)

## AIWindowTabStatesManager.onProgressChange()
- 位置: L1140-1140
- 役割: (未記入)
- 触るとき: (未記入)

## AIWindowTabStatesManager.onStatusChange()
- 位置: L1141-1141
- 役割: (未記入)
- 触るとき: (未記入)

## AIWindowTabStatesManager.onSecurityChange()
- 位置: L1142-1142
- 役割: (未記入)
- 触るとき: (未記入)

## AIWindowTabStatesManager.onContentBlockingEvent()
- 位置: L1143-1143
- 役割: (未記入)
- 触るとき: (未記入)
