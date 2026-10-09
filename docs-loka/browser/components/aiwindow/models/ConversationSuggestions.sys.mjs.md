# browser/components/aiwindow/models/ConversationSuggestions.sys.mjs

source: browser/components/aiwindow/models/ConversationSuggestions.sys.mjs
source-hash: 165a67894edb49d1c1df35cd7e69afdb93f853a1
lines: 978

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## _setLoadPromptForTesting()
- 位置: L58-70
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedLoadPromptDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.loadPrompt`

## _setBuildConversationForTesting()
- 位置: L73-89
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedBuildConversationDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.buildConversation`

## _setGetConversationsByIdForTesting()
- 位置: L92-108
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedGetConversationsByIdDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.getConversationsById`

## _clearResumeActivityCacheForTesting()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_resumeActivityCache.clear()`

## trimConversation()
- 位置: L136-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.content.trim()`, `out.slice()`
- 条件付き依存: `if ( (m.role === MESSAGE_ROLE.USER || m.role === MESSAGE_ROLE.ASSISTANT) && m.content && m.content.trim() )` → `out.push()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `MESSAGE_ROLE.USER`, `m.content`, `m.role`

## addMemoriesToPrompt()
- 位置: async L160-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoriesGetterForSuggestionPrompts.getMemorySummariesForPrompt()`
- 条件付き依存: `if (memorySummaries.length)` → `memorySummaries.map(s => `- ${s}`).join()`
- 条件付き依存: `if (memorySummaries.length)` → `memorySummaries.map()`
- 条件付き依存: `if (memorySummaries.length)` → `lazy.renderPrompt()`
- 参照: `memorySummaries.length`

## cleanInferenceOutput()
- 位置: L181-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(result.finalOutput || "").trim()`, `l.trim()`, `line.replace()`, `lines .map()`, `lines .map(line => line.replace(/^[-*\d.)\[\]]+\s*/, "")) .filter()`, `lines .map(line => line.replace(/^[-*\d.)\[\]]+\s*/, "")) .filter(p => p.length) .map()`, `p.replace()`, `p.replace(/\.$/, "").replace()`, `text .split()`, `text .split(/\n+/) .map()`, `text .split(/\n+/) .map(l => l.trim()) .filter()`
- 参照: `p.length`, `result.finalOutput`

## unpackJsonArrayOutput()
- 位置: L201-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.console.warn()`, `lazy.parseAndExtractJSON()`, `parsed.filter()`
- 条件付き依存: `if (!Array.isArray(parsed))` → `lazy.console.warn()`
- 参照: `item.headline`, `item.id`, `item.status`

## formatJson()
- 位置: L235-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `String()`

## getRandom()
- 位置: L275-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`
- 参照: `arr.length`

## getPrompts()
- 位置: async L288-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `ids.map()`, `this.browsingPrompts.filter()`, `this.getRandom()`
- 条件付き依存: `if (browsingPrompt)` → `ids.push()`
- 参照: `browsingPrompt.id`, `p.minTabs`, `p.needsHistory`, `this.planningPrompts`, `this.writingPrompts`, `validBrowsingPrompts.length`
- XPCOM: `Services.prefs`

## generateConversationStartersSidebar()
- 位置: async L324-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.race()`, `String()`, `cleanInferenceOutput()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `formatJson()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `new Date().toISOString()`, `new Date().toISOString().slice()`, `openAIEngine.getFxAccountToken()`, `prompts.slice()`, `prompts.slice(0, n).map()`, `sanitizeUntrustedContent()`, `signal.throwIfAborted()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `formatJson()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `contextTabs.slice(1).map()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `contextTabs.slice()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if (useMemories)` → `lazy.loadPrompt()`
- 条件付き依存: `if (useMemories)` → `addMemoriesToPrompt()`
- 条件付き依存: `if (signal.aborted)` → `reject()`
- 条件付き依存: `if (!(signal.aborted))` → `signal.addEventListener()`
- 条件付き依存: `if (!(signal.aborted))` → `reject()`
- 条件付き依存: `if (e.name !== "AbortError")` → `lazy.console.warn()`
- 参照: `Services.locale.appLocaleAsBCP47`, `contextTabs.length`, `contextTabs[0].title`, `contextTabs[0].url`, `e.name`, `lazy.MODEL_FEATURES.CONVERSATION_STARTERS_SIDEBAR_SYSTEM`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_ASSISTANT_LIMITATIONS`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_MEMORIES`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_SIDEBAR_STARTER`, `new AbortController().signal`, `signal.aborted`, `signal.reason`, `t.title`, `t.url`
- XPCOM: `Services.locale`

## generateFollowupPrompts()
- 位置: async L440-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Promise.all()`, `String()`, `cleanInferenceOutput()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `formatJson()`, `lazy.buildConversation()`, `lazy.console.warn()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `new Date().toISOString()`, `new Date().toISOString().slice()`, `openAIEngine.getFxAccountToken()`, `prompts.slice()`, `prompts.slice(0, n).map()`, `sanitizeUntrustedContent()`, `trimConversation()`
- 条件付き依存: `if (useMemories)` → `lazy.loadPrompt()`
- 条件付き依存: `if (useMemories)` → `addMemoriesToPrompt()`
- 参照: `Object.keys(currentTab).length`, `currentTab.title`, `currentTab.url`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_ASSISTANT_LIMITATIONS`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_FOLLOWUP`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_MEMORIES`

## getMemorySummariesForPrompt()
- 位置: async L514-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoriesManager.getAllMemories()`, `String()`, `String(memory_summary ?? "").trim()`, `memorySummaries.push()`, `seenSummaries.add()`, `seenSummaries.has()`, `summaryText.toLowerCase()`
- 参照: `memorySummaries.length`

## getMemoriesForResumeActivityConversationStarter()
- 位置: async L547-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `MemoriesManager.getMemoriesByAttribute()`, `memories.filter()`, `memories.slice()`, `memories.sort()`
- 参照: `a.created_at`, `a.last_merged`, `b.created_at`, `b.last_merged`, `lazy.MEMORY_FILTER_COMPARATOR.EQUAL_TO`, `lazy.MEMORY_SENSITIVITY_CATEGORY_NOT_SENSITIVE`, `memory?.source_ids`, `sourceIds.history_source_ids`, `sourceIds.history_source_ids.length`

## attachUrlsToMemory()
- 位置: L590-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy .getHistorySourceIdsFromMemory()`, `lazy .getHistorySourceIdsFromMemory(memory) .map()`, `lazy .getHistorySourceIdsFromMemory(memory) .map(urlHash => urlsByHash.get(urlHash)) .filter()`, `lazy .getHistorySourceIdsFromMemory(memory) .map(urlHash => urlsByHash.get(urlHash)) .filter(Boolean) .sort()`, `urlsByHash.get()`
- 参照: `a.lastVisitDate`, `b.lastVisitDate`

## formatChatsForResumeActivityPrompt()
- 位置: async L608-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[MESSAGE_ROLE.SYSTEM, MESSAGE_ROLE.TOOL].includes()`, `chatsById.set()`, `conversation.messages .filter()`, `conversation.messages .filter( message => ![MESSAGE_ROLE.SYSTEM, MESSAGE_ROLE.TOOL].includes(message.role) ) .slice()`, `lazy.getConversationSourceIdsFromMemory()`, `lazy.getConversationsById()`, `memories.flatMap()`
- 条件付き依存: `if ( bodyOrContent && bodyOrContent.length > lazy.MESSAGE_LENGTH_THRESHOLD )` → `bodyOrContent.substring()`
- 参照: `MESSAGE_ROLE.SYSTEM`, `MESSAGE_ROLE.TOOL`, `bodyOrContent.length`, `conversation.id`, `lazy.MESSAGE_LENGTH_THRESHOLD`, `lazy.ROLE_LABEL`, `message.content`, `message.content?.body`, `message.role`

## buildMemoryInputBlock()
- 位置: L656-689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `chatsById.get()`, `formattedMessagesForResumeActivity .split()`, `formattedMessagesForResumeActivity .split("\n") .map()`, `formattedMessagesForResumeActivity .split("\n") .map(line => ` ${line}`) .join()`, `lazy .getConversationSourceIdsFromMemory()`, `lazy .getConversationSourceIdsFromMemory(memory) .map()`, `lazy .getConversationSourceIdsFromMemory(memory) .map(conversationId => chatsById.get(conversationId)) .filter()`, `sanitizeUntrustedContent()`, `urls .map()`, `urls .map(url => ` - ${sanitizeUntrustedContent(url.title)}`) .join()`
- 条件付き依存: `if (chats.length)` → `chats.join()`
- 参照: `a.updatedDate`, `b.updatedDate`, `chats.length`, `memory.frecency`, `memory.memory_summary`, `memory.reasoning`, `url.title`

## _getCachedResumeActivity()
- 位置: L698-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_resumeActivityCache.get()`
- 参照: `entry.inFlight`, `entry.result`

## filterDeletedMemoriesFromResumeActivity()
- 位置: async L712-722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await MemoriesManager.getAllMemories({ includeSoftDeleted: false })).map()`, `MemoriesManager.getAllMemories()`, `currentMemoryIds.has()`, `result.filter()`
- 参照: `filteredResult.length`, `memory.id`, `result.length`

## generateUncachedResumeActivityConversationStarters()
- 位置: async L727-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(card?.headline || "").replace()`, `(card?.status || "").replace()`, `Promise.all()`, `attachUrlsToMemory()`, `buildMemoryInputBlock()`, `cardsById.get()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.securityProperties.commit()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `conversation.setSystemMessage()`, `formatChatsForResumeActivityPrompt()`, `getMemoriesForResumeActivityConversationStarter()`, `lazy.buildConversation()`, `lazy.console.warn()`, `lazy.indexInferenceResultsById()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `lazy.resolveUrlsForMemories()`, `memoriesWithPlaceHashes .map()`, `memoriesWithPlaceHashes .map(memory => attachUrlsToMemory(memory, urlsByHash, MAX_NUM_URLS_PER_MEMORY) ) .filter()`, `memoriesWithUrlsAndTitles.map()`, `memoryInput.join()`, `openAIEngine.getFxAccountToken()`, `result.filter()`, `unpackJsonArrayOutput()`, `urls.map()`
- 参照: `card?.headline`, `card?.status`, `lazy.MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION_STARTER`, `m.memory`, `memoriesWithPlaceHashes.length`, `memoriesWithUrlsAndTitles.length`, `memoryInput.length`, `s.urls.length`

## isResumeActivityLocaleSupported()
- 位置: L824-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RESUME_ACTIVITY_SUPPORTED_LOCALES.some()`, `Services.locale.appLocaleAsBCP47.toLowerCase()`, `appLocale.startsWith()`
- XPCOM: `Services.locale`

## generateResumeActivityConversationStarters()
- 位置: async L840-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoriesManager.getLastSessionMemoryTimestamp()`, `_getCachedResumeActivity()`, `_resumeActivityCache.clear()`, `_resumeActivityCache.get()`, `_resumeActivityCache.set()`, `generateUncachedResumeActivityConversationStarters()`, `isResumeActivityLocaleSupported()`
- 条件付き依存: `if (cached !== undefined)` → `filterDeletedMemoriesFromResumeActivity()`
- 条件付き依存: `if (_resumeActivityCache.get(watermark) === entry)` → `_resumeActivityCache.set()`

## constructConversationToResumeActivity()
- 位置: async L880-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Array.of()`, `Promise.all()`, `[chatSystemPrompt, resumeActivitySystemPrompt].join()`, `buildMemoryInputBlock()`, `conversation.addUserMessage()`, `conversation.securityProperties.commit()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `conversation.setSystemMessage()`, `formatChatsForResumeActivityPrompt()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`
- 条件付き依存: `if ( !resumeActivitySuggestion || !resumeActivitySuggestion.memory || !resumeActivitySuggestion.content )` → `lazy.console.warn()`
- 条件付き依存: `if ( !content.headline || !content.status || !content.previewTabs || !Array.isArray(content.previewTabs) || content.previewTabs.length === 0 )` → `lazy.console.warn()`
- 参照: `content.headline`, `content.previewTabs`, `content.previewTabs.length`, `content.status`, `conversation.engine?.model`, `conversation.promptEmbeddedMemories`, `lazy.ChatConversation`, `lazy.MODEL_FEATURES.CHAT`, `lazy.MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION`, `lazy.SYSTEM_PROMPT_TYPE.TEXT`, `resumeActivitySuggestion.content`, `resumeActivitySuggestion.content.headline`, `resumeActivitySuggestion.content.previewTabs`, `resumeActivitySuggestion.content.status`, `resumeActivitySuggestion.memory`, `resumeActivitySuggestion.memory.id`, `resumeActivitySuggestion.memory.memory_summary`, `userMessage.content.relevantMemories`
