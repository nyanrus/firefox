# browser/components/aiwindow/models/Chat.sys.mjs

source: browser/components/aiwindow/models/Chat.sys.mjs
source-hash: 31ba4ca3eda2888e56fa6e93c0d2ef8a9ea24bec
lines: 855

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.assign()`, `console.createInstance()`

## executeToolByName()
- 位置: async L48-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.getPageContentText()`, `Glean.smartWindow.getPageContent.record()`, `Glean.smartWindow.searchHandoff.record()`, `RunSearch.runSearch()`, `lazy.SearchService.getDefault()`, `result.reduce()`, `toolFns.addMemory()`, `toolFns.getNavigationInfo()`, `toolFns.getOpenTabs()`, `toolFns.getSkill()`, `toolFns.getUserMemories()`, `toolFns.manageTabs()`, `toolFns.searchBrowsingHistory()`
- 条件付き依存: `if (uiData)` → `conversation.addUIToolToCurrentMessage()`
- 参照: `conversation.engine?.model`, `conversation.id`, `conversation.messageCount`, `curr?.length`, `engine.name`, `err.clientReason`

## runGenerateAiTab()
- 位置: async L190-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolFns.createAITab()`
- 条件付き依存: `if (toolCallId)` → `conversation.addUIToolToCurrentMessage()`
- 条件付き依存: `if (toolCallId && uiData)` → `conversation.addUIToolToCurrentMessage()`
- 参照: `UI_TYPES.AITAB`

## splitDirectAnswerStream()
- 位置: L240-248
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Symbol.asyncIterator`, `result?.directAnswerStream`

## filterFeatureGatedTools()
- 位置: L263-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `searchTheWebToolConfig()`
- 条件付き依存: `if (searchTheWebConfig)` → `filtered.map()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(AITAB_PREF, false))` → `filtered.filter()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(AITAB_PREF, false))` → `AITAB_TOOLS.has()`
- 参照: `t.function?.name`
- XPCOM: `Services.prefs`

## recordToolCallEvent()
- 位置: L322-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.toolCall.record()`
- 参照: `conversation.engine?.model`, `conversation.id`, `conversation.messageCount`, `conversation.systemPromptVersion`

## classifyStreamingError()
- 位置: L355-367
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.io.offline`, `err.clientReason`, `err.error`, `err.metadata?.errorMessage`
- XPCOM: `Services.io`

## logConversationStream()
- 位置: L369-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.padEnd()`, `lazy.console.error()`
- 条件付き依存: `if (data)` → `lazy.console.debug()`
- 条件付き依存: `if (!(data))` → `lazy.console.debug()`

## fetchWithHistory()
- 位置: async L410-853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `FEATURE_GATED_HANDLERS.get()`, `JSON.parse()`, `String()`, `TOOLS_WITH_PENDING_ACTION_LOG.has()`, `classifyStreamingError()`, `console.error()`, `conversation.addAssistantMessage()`, `conversation.addToolCallMessage()`, `conversation.currentTurnIndex()`, `conversation.receiveResponse()`, `conversation.updateToolCallMessage()`, `expandUrlTokensInToolParams()`, `filterFeatureGatedTools()`, `lazy.AIWindow.chatStore ?.updateConversation()`, `lazy.AIWindow.chatStore ?.updateConversation(conversation) .catch()`, `lazy.AIWindow.chatStore?.updateConversation()`, `lazy.AIWindow.chatStore?.updateConversation(conversation).catch()`, `logConversationStream()`, `openAIEngine.getFxAccountToken()`, `recordToolCallEvent()`, `splitDirectAnswerStream()`, `streamModelResponse()`, `structuredClone()`
- 条件付き依存: `if (!fxAccountToken)` → `console.error()`
- 条件付き依存: `if (!pendingToolCalls || pendingToolCalls.length === 0)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!pendingToolCalls || pendingToolCalls.length === 0)` → `logConversationStream()`
- 条件付き依存: `if (!conversation.engine?.isCustomEndpoint)` → `runLLMaJTelemetry()`
- 条件付き依存: `if (signal?.aborted)` → `logConversationStream()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `pendingToolCalls.slice()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `conversation.addAssistantMessage()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `conversation.addToolCallMessage()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `recordToolCallEvent()`
- 条件付き依存: `if (firstPending?.name === GET_USER_MEMORIES)` → `conversation.messages.findLast()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `pendingToolCalls.slice()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `conversation.addAssistantMessage()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `conversation.addToolCallMessage()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `recordToolCallEvent()`
- 条件付き依存: `if (TOOLS_WITH_PENDING_ACTION_LOG.has(toolName))` → `conversation.addToolCallMessage()`
- 条件付き依存: `if (featureGatedHandler)` → `featureGatedHandler()`
- 条件付き依存: `if (result.requiresSearchHandoff)` → `dispatchTool()`
- 条件付き依存: `if (!(featureGatedHandler))` → `dispatchTool()`
- 条件付き依存: `if (toolName === GENERATE_AITAB && !aiTabSucceeded)` → `conversation.messages.findLast()`
- 条件付き依存: `if (message)` → `conversation.updateToolUI()`
- 条件付き依存: `if (toolName === MANAGE_TABS || aiTabSucceeded)` → `conversation.securityProperties.commit()`
- 条件付き依存: `if (directAnswerStream)` → `conversation.receiveResponse()`
- 条件付き依存: `if (directAnswerStream)` → `logConversationStream()`
- 条件付き依存: `if (!win || win.closed)` → `console.error()`
- 条件付き依存: `if (isSearchHandoff)` → `lazy.AIWindow.openSidebarAndContinue()`
- 参照: `Cu.isInAutomation`, `MESSAGE_ROLE.USER`, `browsingContext?.embedderElement`, `content.name`, `conversation._searchExecutedTurn`, `conversation.engine?.isCustomEndpoint`, `conversation.tokenToUrl`, `err.clientReason`, `firstPending?.name`, `functionSpec.arguments`, `functionSpec?.arguments`, `functionSpec?.name`, `fxaError.clientReason`, `lastToolCall.function`, `lastToolCall.function.arguments`, `lastUserMessage.memoriesEnabled`, `m.role`, `m.toolUIData?.toolCallId`, `originalEmbedderElement?.documentGlobal`, `pendingToolCalls.length`, `pendingToolCalls[0]?.function`, `response.fullResponseText`, `response.pendingToolCalls`, `response.usage`, `result.requiresSearchHandoff`, `result.success`, `result.toolResult`, `result?.error`, `signal?.aborted`, `split.directAnswerStream`, `split.toolBody`, `tc.function.arguments`, `tc.function.name`, `tc.id`, `this.lastUsage`, `toolParams.query`, `win.closed`

## streamModelResponse()
- 位置: L451-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.compactChatCompletions()`, `conversation.runWithGenerator()`, `conversation.securityProperties.getLogText()`, `lazy.console.log()`, `logConversationStream()`, `snapshot.at()`
- 参照: `conversation.id`

## dispatchTool()
- 位置: L686-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `executeToolByName()`
