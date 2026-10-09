# browser/components/aiwindow/ui/modules/ToolUI.sys.mjs

source: browser/components/aiwindow/ui/modules/ToolUI.sys.mjs
source-hash: e221153ad9d9d4d802c9a950df9eedef9d2c6735
lines: 1462

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`, `this.#handleCancelTabSelection.bind()`, `this.#handleConfirmTabGroupSelection.bind()`, `this.#handleConfirmationTabSelection.bind()`, `this.#handleOpenAITab.bind()`, `this.#handleOpenAndGroupTabsSelection.bind()`, `this.#handleRetryPrompt.bind()`, `this.#handleUndoTabClose.bind()`, `this.#handleUndoTabGroup.bind()`

## ToolUI.registerTabKeys()
- 位置: L142-146
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (toolCallId && tokenToKey?.size)` → `this.#tabKeysByToolCall.set()`
- 参照: `tokenToKey?.size`

## ToolUI.clearTabKeys()
- 位置: L153-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabKeysByToolCall.delete()`

## ToolUI.#getConfirmationReason()
- 位置: L157-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.some()`
- 参照: `t.pinned`, `t.selected`, `tabs.length`

## ToolUI.#verifyAndCollectTabs()
- 位置: L181-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `claimedTabs.add()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows.filter()`, `tabsByWindow.get()`, `tabsByWindow.get(match.window).push()`, `tabsByWindow.has()`, `tokenToKey.get()`
- 条件付き依存: `if (!win)` → `lazy.console.error()`
- 条件付き依存: `if (!tokenToKey?.size)` → `lazy.console.warn()`
- 条件付き依存: `if (permanentKey)` → `candidateWindow.gBrowser.tabs.find()`
- 条件付き依存: `if (permanentKey)` → `claimedTabs.has()`
- 条件付き依存: `if (!match)` → `lazy.console.warn()`
- 条件付き依存: `if (!tabsByWindow.has(match.window))` → `tabsByWindow.set()`
- 条件付き依存: `if (verifiedCount === 0)` → `lazy.console.warn()`
- 参照: `match.tab`, `match.window`, `selectedTab.token`, `selectedTab.url`, `t.permanentKey`, `tokenToKey?.size`

## ToolUI.closeSelectedTabs()
- 位置: async L246-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.tabManagementService.closeTabs()`, `tabs.find()`, `this.#verifyAndCollectTabs()`
- 条件付き依存: `if (result.failedTabs.length)` → `failedTabs.push()`
- 条件付き依存: `if (result.operationId)` → `operationIds.push()`
- 参照: `activeTab.smartWindowActionSource`, `ownerWindow.gBrowser.selectedTab`, `result.failedTabs`, `result.failedTabs.length`, `result.operationId`, `result.requestedCount`

## ToolUI.#recordTabConfirmationResponse()
- 位置: L298-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ToolUITelemetry.recordBrowserActionPromptResponse()`
- 参照: `conversation.id`, `conversation.messageCount`

## ToolUI.#recordConfirmedBrowserActionComplete()
- 位置: L329-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.takePendingBrowserActionTelemetry()`, `lazy.ToolUITelemetry.recordBrowserActionComplete()`

## ToolUI.#summarizeTabActionOutcome()
- 位置: L361-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ToolUITelemetry.browserActionResult()`

## ToolUI.#recordAbandonedTabConfirmation()
- 位置: L378-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordConfirmedBrowserActionComplete()`, `this.#recordTabConfirmationResponse()`
- 参照: `selectedTabs.length`

## ToolUI.#finalizeTabActionConfirmation()
- 位置: L413-459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `conversation.messages.at()`, `conversation.resolvePendingToolConfirmation()`, `conversation.updateToolUI()`, `selectedTabs.map()`, `this.#recordTabConfirmationResponse()`
- 条件付き依存: `if (resultInfo)` → `this.#recordConfirmedBrowserActionComplete()`
- 参照: `UI_TYPES.AI_ACTION_RESULT`, `confirmationMessage.action`, `conversation.messages.at(-1)?.content?.body?.action`, `selectedTabs.length`

## ToolUI.#handleConfirmationTabSelection()
- 位置: async L468-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#finalizeTabActionConfirmation()`, `this.#summarizeTabActionOutcome()`, `this.#tabKeysByToolCall.get()`, `this.clearTabKeys()`, `this.closeSelectedTabs()`
- 条件付き依存: `if (!result)` → `this.#recordAbandonedTabConfirmation()`
- 参照: `result.failedTabs.length`, `result.operationIds`, `result.operationIds.length`, `result.requestedCount`, `selectedTabs.length`

## ToolUI.#handleCancelTabSelection()
- 位置: L518-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.resolvePendingToolConfirmation()`, `conversation.updateToolUI()`, `this.#recordConfirmedBrowserActionComplete()`, `this.#recordTabConfirmationResponse()`, `this.clearTabKeys()`
- 参照: `UI_TYPES.CANCELLED_COMPONENT`, `updateData?.actionType`, `updateData?.reason`

## ToolUI.#handleConfirmTabGroupSelection()
- 位置: async L560-608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#finalizeTabActionConfirmation()`, `this.#summarizeTabActionOutcome()`, `this.#tabKeysByToolCall.get()`, `this.clearTabKeys()`, `this.createTabGroup()`
- 条件付き依存: `if (!result?.success)` → `this.#recordAbandonedTabConfirmation()`
- 参照: `result.error`, `result.group`, `result.group.id`, `result.group.tabCount`, `result?.success`, `selectedTabs.length`

## ToolUI.#handleOpenAndGroupTabsSelection()
- 位置: async L619-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#finalizeTabActionConfirmation()`, `this.clearTabKeys()`, `this.findChatTab()`, `this.openOrGroupTabs()`
- 参照: `conversation?.id`, `result.group`, `result.group.id`, `result.group?.id`, `result.mergedCount`, `result.switched`, `result?.success`

## ToolUI.#handleUndoTabGroup()
- 位置: async L657-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `conversation.updateToolUI()`, `lazy.ToolUITelemetry.recordBrowserActionUndo()`, `lazy.tabManagementService.ungroupTabs()`, `ungroupedTabs.push()`
- 条件付き依存: `if (!operationIds.length)` → `lazy.console.error()`
- 条件付き依存: `if (!result?.success)` → `lazy.console.error()`
- 条件付き依存: `if (!result?.success)` → `lazy.ToolUITelemetry.recordBrowserActionUndo()`
- 条件付き依存: `if (!result?.success)` → `Math.max()`
- 参照: `UI_TYPES.AI_ACTION_RESULT`, `conversation.id`, `conversation.messageCount`, `operationIds.length`, `result.ungroupedTabs`, `result?.error`, `result?.success`, `result?.ungroupedTabs?.length`, `ungroupedTabs.length`

## ToolUI.#handleUndoTabClose()
- 位置: async L738-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `conversation.updateToolUI()`, `lazy.ToolUITelemetry.recordBrowserActionUndo()`, `lazy.console.error()`, `lazy.console.log()`, `lazy.tabManagementService.restoreTabs()`
- 条件付き依存: `if (!operationIds.length)` → `lazy.console.error()`
- 条件付き依存: `if (result.failedTabs.length)` → `failedTabs.push()`
- 参照: `UI_TYPES.AI_ACTION_RESULT`, `conversation.id`, `conversation.messageCount`, `error?.name`, `failedTabs.length`, `operationIds.length`, `result.failedTabs`, `result.failedTabs.length`, `result.requestedCount`, `result.restoredCount`

## ToolUI.#handleRetryPrompt()
- 位置: async L841-845
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.updateToolUI()`

## ToolUI.#findLastAssistantTextMessage()
- 位置: L854-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messages.findLast()`
- 参照: `lazy.MESSAGE_ROLE.ASSISTANT`, `message.content?.type`, `message.role`

## ToolUI.#canOriginTabJoinGroup()
- 位置: L883-890
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `groupTabs.includes()`
- 参照: `originTab.documentGlobal`, `originTab.splitview`

## ToolUI.findChatTab()
- 位置: L906-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...win.gBrowser.tabs].find()`, `lazy.AIWindow.getChatTabConversationId()`, `lazy.AIWindow.isAIWindowActive()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## ToolUI.#dropLoneChatTab()
- 位置: L943-958
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.tabManagementService.getGroupingRejection()`, `selections.find()`, `tokenToKey?.get()`, `windowTabs.filter()`
- 参照: `chatSelection.token`, `groupable.length`, `groupable[0].permanentKey`, `selection.isChatTab`, `selections.length`, `tab.permanentKey`

## ToolUI.createTabGroup()
- 位置: async L983-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.tabManagementService.createTabGroup()`, `result.failedTabs.push()`, `tabsByWindow.get()`, `tabsByWindow.has()`, `this.#dropLoneChatTab()`, `this.#verifyAndCollectTabs()`
- 条件付き依存: `if (!groupWindow)` → `tabsByWindow.get()`
- 参照: `ownerTabs.length`, `tabsByWindow.get(groupWindow).length`

## ToolUI.openAndGroupTabs()
- 位置: async L1048-1088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.tabManagementService.createTabGroup()`, `lazy.tabManagementService.getGroupingRejection()`, `lazy.tabManagementService.resolveOrOpenTabs()`, `resolvedTabs.some()`, `this.#canOriginTabJoinGroup()`
- 条件付き依存: `if (!tabs.length)` → `lazy.console.warn()`
- 参照: `resolvedTabs.length`, `tabs.length`

## ToolUI.openOrSwitchToTab()
- 位置: async L1101-1123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.tabManagementService.findOpenTab()`, `lazy.tabManagementService.openTabs()`, `lazy.tabManagementService.switchToTab()`
- 条件付き依存: `if (existingTab)` → `lazy.tabManagementService.switchToTab()`
- 参照: `openedTabs.length`, `tab.url`

## ToolUI.openOrGroupTabs()
- 位置: async L1136-1141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openAndGroupTabs()`
- 条件付き依存: `if (tabs.length === 1)` → `this.openOrSwitchToTab()`
- 参照: `tabs.length`

## ToolUI.findOriginalUserPrompt()
- 位置: L1151-1179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messages.find()`
- 参照: `assistantMessage.parentMessageId`, `lazy.MESSAGE_ROLE.USER`, `m.id`, `nextMessage.content.body`, `nextMessage.content?.type`, `nextMessage.parentMessageId`, `nextMessage.role`

## ToolUI.#promptActionForUIData()
- 位置: L1187-1193
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `toolUIData.properties?.actionType`, `toolUIData.uiType`

## ToolUI.handleUIDisplayTelemetry()
- 位置: L1195-1211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ToolUITelemetry.recordBrowserActionPrompt()`, `this.#getConfirmationReason()`, `this.#promptActionForUIData()`
- 参照: `tabs.length`, `toolUIData.properties?.tabs`

## ToolUI.#handleOpenAITab()
- 位置: L1231-1276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.linkClick.record()`, `URL.parse()`, `conversation.updateToolUI()`, `lazy.SmartWindowTelemetry.recordUriLoad()`, `lazy.URILoadingHelper.openTrustedLinkIn()`, `lazy.console.error()`, `parsedURL.searchParams.get()`
- 参照: `UI_TYPES.AITAB`, `conversation.id`, `conversation.messageCount`, `message.toolUIData.properties?.state`, `message.toolUIData?.properties?.viewerURL`, `message.toolUIData?.uiType`, `parsedURL.pathname`, `parsedURL?.protocol`, `window.gBrowser.selectedBrowser.browsingContext.originAttributes`, `window?.gBrowser`

## ToolUI.autoCancelActiveConfirmation()
- 位置: async L1307-1370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CONFIRMATION_UI_TYPES.includes()`, `lazy.console.log()`, `this.#findLastAssistantTextMessage()`, `this.#promptActionForUIData()`, `this.handleUpdate()`
- 条件付き依存: `if (!conversation?.messages?.length)` → `lazy.console.log()`
- 条件付き依存: `if (!isActiveConfirmation)` → `lazy.console.log()`
- 条件付き依存: `if (originalUserPrompt)` → `Date.now()`
- 参照: `UI_UPDATE_TYPES.CANCEL_TAB_SELECTION`, `conversation.messages`, `conversation.pendingRetry`, `conversation?.messages?.length`, `lastAssistantTextMessage.id`, `lastAssistantTextMessage.toolUIData`, `lastAssistantTextMessage.toolUIData.properties?.originalUserPrompt`, `lastAssistantTextMessage.toolUIData.toolCallId`, `lastAssistantTextMessage.toolUIData.uiType`, `lastAssistantTextMessage?.toolUIData?.uiType`

## ToolUI.injectRetryToolUIDataIfNeeded()
- 位置: L1379-1413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.randomUUID()`, `lazy.console.log()`
- 参照: `UI_TYPES.RETRY_COMPONENT`, `conversation.pendingRetry`, `conversation.pendingRetry.cancelledUiType`, `conversation.pendingRetry.originalUserPrompt`, `conversation?.pendingRetry`, `lazy.MESSAGE_ROLE.ASSISTANT`, `msg.toolUIData`, `msg?.content?.type`, `msg?.role`

## ToolUI.handleUpdate()
- 位置: async L1428-1460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation?.messages?.find()`, `handler()`
- 条件付き依存: `if (typeof handler !== "function")` → `lazy.console.error()`
- 参照: `m.id`, `message?.toolUIData?.toolCallId`, `this.#UPDATE_TYPE_HANDLERS`
