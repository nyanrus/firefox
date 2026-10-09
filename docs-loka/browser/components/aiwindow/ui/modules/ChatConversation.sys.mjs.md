# browser/components/aiwindow/ui/modules/ChatConversation.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatConversation.sys.mjs
source-hash: 266e22cdd9950903415360f510834bbda2d8602e
lines: 1330

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## _setLoadPromptForTesting()
- 位置: L88-105
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedLoadPromptDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.loadPrompt`

## lazy.loadPrompt()
- 位置: async L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fn()`

## ChatConversation.constructor()
- 位置: L207-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`, `super()`, `this.rehydrateCitationsPool()`, `this.rehydrateHistoryResultsPool()`
- 条件付き依存: `if (messages.length)` → `this.#updateActiveBranchTipMessageId()`
- 参照: `CONVERSATION_STATUS.ACTIVE`, `messages.length`, `params.status`, `this.description`, `this.memoriesToggled`, `this.pageMeta`, `this.pageUrl`, `this.pendingRetry`, `this.status`, `this.title`, `this.transientStarterUrl`, `this.transientStarters`, `this.urlTokenizer`

## ChatConversation.on()
- 位置: L267-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emitter.on()`

## ChatConversation.off()
- 位置: L270-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emitter.off()`

## ChatConversation.emit()
- 位置: L273-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emitter.emit()`

## ChatConversation.stashPendingBrowserActionTelemetry()
- 位置: L284-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pendingBrowserActionTelemetry.set()`

## ChatConversation.takePendingBrowserActionTelemetry()
- 位置: L295-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pendingBrowserActionTelemetry.delete()`, `this.#pendingBrowserActionTelemetry.get()`

## ChatConversation.pendingBrowserActionTelemetryCount()
- 位置: L307-309
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pendingBrowserActionTelemetry.size`

## ChatConversation.convertUrlToToken()
- 位置: L324-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.urlTokenizer.encodeToken()`

## ChatConversation.handleChunk()
- 位置: L333-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `consumeStreamChunk()`
- 条件付き依存: `if (tokens)` → `currentMessage?.addTokens()`
- 条件付き依存: `if (plainText || tokens)` → `this.emit()`
- 条件付き依存: `if (plainText || tokens)` → `lazy.ChatStore.persistStreamingMessage()`
- 参照: `currentMessage.content.body`, `currentMessage?.content`, `this.urlTokenizer.tokenToUrl`

## ChatConversation.receiveResponse()
- 位置: async L356-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ChatStore.endStreamingWrites()`, `lazy.ChatStore.updateConversation()`, `super.receiveResponse()`, `this.#getCurrentAssistantResponse()`
- 条件付き依存: `if (this.#historyResultsPool.size)` → `this.getHistoryResultsSnapshot()`
- 条件付き依存: `if (this.#pendingCitationUrls.size)` → `this.getCitationsSnapshot()`
- 条件付き依存: `if (this.urlTokenizer.urlToToken.size)` → `stripUnresolvedUrlTokens()`
- 条件付き依存: `if (result.currentMessage?.content?.body)` → `this.emit()`
- 条件付き依存: `if (!result.pendingToolCalls?.length)` → `this.promptEmbeddedMemories.map()`
- 条件付き依存: `if (!result.pendingToolCalls?.length)` → `lazy.MemoriesManager.resolveUsedMemories()`
- 条件付き依存: `if (memoriesApplied.length)` → `this.emit()`
- 条件付き依存: `if (!result.pendingToolCalls?.length)` → `this.emit()`
- 参照: `currentMessage.citations`, `currentMessage.content.body`, `currentMessage.content?.body`, `currentMessage.historyResults`, `currentMessage.memoriesApplied`, `currentMessage.tokens?.existing_memory`, `memoriesApplied.length`, `memory.id`, `memoryIds.length`, `result.currentMessage.content.body`, `result.currentMessage?.content?.body`, `result.fullResponseText`, `result.pendingToolCalls`, `result.pendingToolCalls?.length`, `result.usage`, `this.#historyResultsPool.size`, `this.#pendingCitationUrls.size`, `this.id`, `this.promptEmbeddedMemories`, `this.urlTokenizer.urlToToken.size`

## ChatConversation.#getCurrentAssistantResponse()
- 位置: L447-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messages .filter()`, `this.messages .filter( message => message.role === MESSAGE_ROLE.ASSISTANT && message?.content?.type === "text" ) .at()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `message.role`, `message?.content?.type`

## ChatConversation.renderState()
- 位置: L463-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RESTORABLE_ROLES.includes()`, `this.messages.filter()`
- 参照: `content?.l10nId`, `message.toolUIData`

## ChatConversation._createMessage()
- 位置: L481-483
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.id`

## ChatConversation.addUserMessage()
- 位置: L497-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dismissPendingUndos()`, `this.#pendingCitationUrls.clear()`, `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.USER`, `content.contextMentions`, `content.contextPageUrl`, `pageUrl.href`, `this.messages.length`, `userOpts.contextMentions`, `userOpts.contextMentions?.length`

## ChatConversation.resolvePendingToolConfirmation()
- 位置: L538-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ChatStore.updateConversation()`, `lazy.ChatStore.updateConversation(this).catch()`, `lazy.console.error()`, `this.emit()`, `this.messages.at()`
- 参照: `MESSAGE_ROLE.TOOL`, `message.content`, `message.content?.body?.pending`, `message.content?.tool_call_id`, `message?.role`

## ChatConversation.#dismissPendingUndos()
- 位置: L570-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`
- 参照: `confirmedData?.operationIds?.length`, `m.toolUIData`, `td.properties`, `td.properties?.confirmedData`, `td.properties?.undoDismissed`, `td.uiType`, `this.messages`, `this.messages.length`

## ChatConversation.addAssistantMessage()
- 位置: L604-623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `assistantOpts.modelId`, `this.engine?.model`

## ChatConversation.addAssistantWithL10nMessage()
- 位置: L636-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 条件付き依存: `if (message)` → `this.emit()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `assistantOpts.modelId`, `this.engine?.model`

## ChatConversation.addToolCallMessage()
- 位置: L667-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 条件付き依存: `if (message)` → `this.emit()`
- 参照: `MESSAGE_ROLE.TOOL`, `this.engine?.model`, `toolOpts.modelId`

## ChatConversation.updateToolCallMessage()
- 位置: L701-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`
- 条件付き依存: `if (!message)` → `this.addToolCallMessage()`
- 参照: `message.content`

## ChatConversation.loadSystemPrompt()
- 位置: async L718-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.loadPrompt()`, `this.setSystemMessage()`
- 参照: `MODEL_FEATURES.CHAT`, `SYSTEM_PROMPT_TYPE.TEXT`, `opts.model`, `this.engine?.model`

## ChatConversation.generatePrompt()
- 位置: async L746-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addUserMessage()`, `this.injectRealTimeContext()`, `this.securityProperties.commit()`
- 条件付き依存: `if (!this.messages.length)` → `this.loadSystemPrompt()`
- 条件付き依存: `if (!skipUserDispatch)` → `this.emit()`
- 条件付き依存: `if (userOpts?.memoriesEnabled)` → `this.injectMemoriesContext()`
- 条件付き依存: `if (userOpts?.memoriesEnabled)` → `lazy.console.error()`
- 参照: `this.messages.length`, `userOpts?.contextMentions`, `userOpts?.memoriesEnabled`

## ChatConversation.retryMessage()
- 位置: async L804-821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.retryMessage()`, `this.#pendingCitationUrls.clear()`, `this.#updateActiveBranchTipMessageId()`
- 参照: `MESSAGE_ROLE.USER`, `err.clientReason`, `message.role`, `removed.length`

## ChatConversation.injectRealTimeContext()
- 位置: async L836-855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.buildBrowserContextPrompt()`
- 参照: `this.#lastBrowserContext`, `this.engine?.model`, `this.securityProperties`, `userMessage.content.userContext`, `userMessage.content.userContext.realTimeContext`, `userMessage?.content`

## ChatConversation.injectMemoriesContext()
- 位置: async L877-898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `constructMemories()`, `this.#getPreviousRelevantMemories()`, `this.securityProperties.setPrivateData()`
- 参照: `memoriesContext.message.content`, `memoriesContext.relevantMemories`, `this.engine?.model`, `userMessage.content.relevantMemories`, `userMessage.content.userContext`, `userMessage.content.userContext.memoriesContext`, `userMessage?.content`

## ChatConversation.#getPreviousRelevantMemories()
- 位置: L907-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userMessages .slice()`, `userMessages .slice(1) .flatMap()`
- 条件付き依存: `if (this.messages[i].role === MESSAGE_ROLE.USER)` → `userMessages.push()`
- 参照: `MESSAGE_ROLE.USER`, `message.content?.relevantMemories`, `this.messages`, `this.messages.length`, `this.messages[i].role`, `userMessages.length`

## ChatConversation.getSitesList()
- 位置: L936-956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `message.pageUrl.protocol.startsWith()`, `seen.has()`, `this.messages.forEach()`
- 条件付き依存: `if (!seen.has(message.pageUrl.href))` → `seen.add()`
- 条件付き依存: `if (!seen.has(message.pageUrl.href))` → `deduped.push()`
- 参照: `message.pageUrl`, `message.pageUrl.href`

## ChatConversation.getMostRecentPageVisited()
- 位置: L964-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sites.pop()`, `this.getSitesList()`
- 参照: `sites.length`

## ChatConversation.getMessagesInChatCompletionsFormat()
- 位置: L979-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `baseWire.filter()`, `filteredSrc.findLastIndex()`, `getRoleLabel()`, `getRoleLabel(MESSAGE_ROLE.USER).toLowerCase()`, `isWireFiltered()`, `super.getMessagesInChatCompletionsFormat()`, `this.messages.filter()`
- 条件付き依存: `if (msg.role === getRoleLabel(MESSAGE_ROLE.USER).toLowerCase())` → `resolveMentionUrls()`
- 条件付き依存: `if (userContext)` → `Object.values(userContext).map()`
- 条件付き依存: `if (userContext)` → `Object.values()`
- 条件付き依存: `if (userContext)` → `getRoleLabel(MESSAGE_ROLE.USER).toLowerCase()`
- 条件付き依存: `if (userContext)` → `getRoleLabel()`
- 条件付き依存: `if (userContext)` → `msgsForAPI.splice()`
- 条件付き依存: `if (applyUrlTokens)` → `replaceUrlsWithTokens()`
- 参照: `MESSAGE_ROLE.USER`, `filteredSrc[lastUserMsgIdx].content.userContext`, `msg.content`, `msg.role`, `this.messages`

## isWireFiltered()
- 位置: L980-990
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `MESSAGE_ROLE.ASSISTANT`, `MESSAGE_ROLE.SYSTEM`, `SYSTEM_PROMPT_TYPE.MEMORIES`, `SYSTEM_PROMPT_TYPE.REAL_TIME`, `m.role`, `m?.content?.body`, `m?.content?.type`

## ChatConversation.#updateActiveBranchTipMessageId()
- 位置: L1031-1036
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messages .filter()`, `this.messages .filter(m => m.isActiveBranch) .sort()`, `this.messages .filter(m => m.isActiveBranch) .sort((a, b) => b.ordinal - a.ordinal) .shift()`
- 参照: `a.ordinal`, `b.ordinal`, `m.isActiveBranch`, `this.activeBranchTipMessageId`, `this.messages .filter(m => m.isActiveBranch) .sort((a, b) => b.ordinal - a.ordinal) .shift()?.id`

## ChatConversation.messages()
- 位置: L1038-1042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateActiveBranchTipMessageId()`
- 参照: `super.messages`

## ChatConversation.messages()
- 位置: L1044-1046
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `super.messages`

## ChatConversation.messageCount()
- 位置: L1048-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CHAT_ROLES.includes()`, `this.messages.filter()`
- 参照: `m.role`, `this.messages.filter(m => CHAT_ROLES.includes(m.role)).length`

## ChatConversation.tokenToUrl()
- 位置: L1052-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.urlTokenizer.tokenToUrl`

## ChatConversation.urlToToken()
- 位置: L1056-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.urlTokenizer.urlToToken`

## ChatConversation.getLatestUserMentionCount()
- 位置: L1066-1075
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lastUserMsg?.content?.contextMentions?.filter()`, `lazy.isTabGroupMember()`, `this.messages.findLast()`
- 参照: `MESSAGE_ROLE.USER`, `lastUserMsg?.content?.contextMentions?.filter( m => !lazy.isTabGroupMember(m) ).length`, `m?.role`

## ChatConversation.addSeenUrls()
- 位置: L1082-1085
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.addSeenUrls()`, `this.emit()`
- 参照: `this.seenUrls`

## ChatConversation.#clearToolUI()
- 位置: L1093-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`
- 参照: `message.toolUIData`

## ChatConversation.updateToolUI()
- 位置: async L1105-1128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`
- 条件付き依存: `if (nextUI === null)` → `this.#clearToolUI()`
- 参照: `data.updateData`, `data?.properties`, `message.toolUIData`, `message.toolUIData.properties`, `message.toolUIData.properties.confirmedData`

## ChatConversation.addUIToolToCurrentMessage()
- 位置: L1140-1224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CONFIRMATION_UI_TYPES.includes()`, `this.emit()`, `this.messages .filter()`, `this.messages .filter( m => m.role === MESSAGE_ROLE.ASSISTANT && m.content?.type === "text" ) .at()`
- 条件付き依存: `if (!currentMessage)` → `this.addAssistantMessage()`
- 条件付き依存: `if (lazy.CONFIRMATION_UI_TYPES.includes(uiData.uiType))` → `lazy.ToolUI.findOriginalUserPrompt()`
- 条件付き依存: `if (isUpdate)` → `new Date().toISOString()`
- 条件付き依存: `if (!(isUpdate))` → `new Date().toISOString()`
- 条件付き依存: `if (emitComplete)` → `this.emit()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `currentMessage.toolUIData`, `currentMessage.toolUIData.properties`, `currentMessage.toolUIData.toolCallId`, `currentMessage.toolUIData.updateCount`, `enrichedUIData.properties`, `m.content?.type`, `m.role`, `this.messages`, `uiData.uiType`

## ChatConversation.addHistoryResults()
- 位置: L1236-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.convertTimestamp()`, `this.#historyResultsPool.set()`
- 参照: `lazy.fluentStrings`, `record.timestamp`, `record.url`, `record.visitDate`

## ChatConversation.getHistoryResultsSnapshot()
- 位置: L1253-1255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#historyResultsPool.values()`

## ChatConversation.applyHistoryAssets()
- 位置: L1264-1279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#citationsPool.get()`, `this.#historyResultsPool.get()`
- 参照: `citation.hasFavicon`, `record.hasFavicon`, `record.image`

## ChatConversation.rehydrateHistoryResultsPool()
- 位置: L1286-1292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#historyResultsPool.set()`
- 参照: `message.historyResults`, `record.url`, `this.messages`

## ChatConversation.addCitations()
- 位置: L1299-1306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#citationsPool.get()`, `this.#citationsPool.set()`, `this.#pendingCitationUrls.add()`
- 参照: `record.url`

## ChatConversation.getCitationsSnapshot()
- 位置: L1313-1317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...this.#pendingCitationUrls] .map()`, `[...this.#pendingCitationUrls] .map(url => this.#citationsPool.get(url)) .filter()`, `this.#citationsPool.get()`
- 参照: `this.#pendingCitationUrls`

## ChatConversation.rehydrateCitationsPool()
- 位置: L1322-1328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#citationsPool.set()`
- 参照: `message.citations`, `record.url`, `this.messages`
