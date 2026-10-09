# browser/components/aiwindow/models/memories/MemoriesManager.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesManager.sys.mjs
source-hash: 7965e44ff13e5c5700749a50f3f92a2b5001b4d9
lines: 860

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## takeMostRecentSessions()
- 位置: L98-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sessions .slice()`, `sessions .slice() .sort()`, `sessions .slice() .sort((a, b) => b.session_end_ms - a.session_end_ms) .slice()`, `sessions .slice() .sort((a, b) => b.session_end_ms - a.session_end_ms) .slice(0, maxSessions) .reverse()`
- 参照: `a.session_end_ms`, `b.session_end_ms`, `sessions.length`

## MemoriesManager.ensureConversationForGeneration()
- 位置: async L131-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildFresh()`
- 条件付き依存: `if (!this.#generationConversationPromise)` → `buildFresh()`
- 条件付き依存: `if (!conversation?.isReady)` → `buildFresh()`
- 参照: `conversation?.isReady`, `this.#generationConversationPromise`

## buildFresh()
- 位置: async L132-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildConversation()`
- 参照: `MODEL_FEATURES.MEMORIES_INITIAL_GENERATION_SYSTEM`, `this.#generationConversationPromise`

## MemoriesManager.ensureConversationForUsage()
- 位置: async L164-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildFresh()`
- 条件付き依存: `if (!this.#usageConversationPromise)` → `buildFresh()`
- 条件付き依存: `if (!conversation?.isReady)` → `buildFresh()`
- 参照: `conversation?.isReady`, `this.#usageConversationPromise`

## buildFresh()
- 位置: async L165-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildConversation()`
- 参照: `MODEL_FEATURES.MEMORIES_MESSAGE_CLASSIFICATION_SYSTEM`, `this.#usageConversationPromise`

## MemoriesManager.runMemoryMaintenance()
- 位置: async L205-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `MemoryStore.getMemories()`, `MemoryStore.hardDeleteMemory()`, `allMemories.filter()`, `classifyMemoryAndCapStrength()`, `computeMemoryFrecency()`, `computeMemoryStrength()`, `isShouldDeleteMemoryDueToDecay()`
- 条件付き依存: `if (isShouldDeleteMemoryDueToDecay(memory))` → `MemoryStore.hardDeleteMemory()`
- 条件付き依存: `if (changed)` → `MemoryStore.requestSave()`
- 参照: `mem.is_deleted`, `memory.frecency`, `memory.id`, `memory.is_deleted`, `memory.recent_accessed_counts`, `memory.strength`, `memory.updated_at`

## MemoriesManager.generateMemoriesFromSessions()
- 位置: async L289-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildSessions()`, `console.error()`, `openAIEngine.isRetryableError()`, `runHeuristicGate()`, `runSessionMemoryPipeline()`, `sessions.filter()`, `takeMostRecentSessions()`, `this.ensureConversationForGeneration()`, `this.getLastSessionMemoryTimestamp()`, `this.getSessionMemoryDeltaStartMs()`, `this.saveMemories()`, `this.shouldEnableMemoriesFromSchedulers()`
- 条件付き依存: `if (historyEnabled)` → `this._getRecentHistory()`
- 条件付き依存: `if (conversationEnabled)` → `this._getRecentChats()`
- 条件付き依存: `if (retainedSessions.length < gatedSessions.length)` → `lazy.console.debug()`
- 条件付き依存: `if (!retainedSessions.length)` → `sessions.reduce()`
- 条件付き依存: `if (!retainedSessions.length)` → `Math.max()`
- 条件付き依存: `if (maxSessionEndMs > watermarkMs)` → `this.setLastSessionMemoryTimestamp()`
- 条件付き依存: `if (!retainedSessions.length)` → `lazy.console.debug()`
- 条件付き依存: `if (result.processedThroughMs > 0)` → `this.setLastSessionMemoryTimestamp()`
- 条件付き依存: `if (result.processedThroughMs > 0)` → `Math.max()`
- 参照: `gatedSessions.length`, `result.memories`, `result.processedThroughMs`, `retainedSessions.length`, `runHeuristicGate(session).decision`, `session.session_end_ms`

## MemoriesManager.mergeMemories()
- 位置: async L408-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.addMemory()`, `MemoryStore.getMemories()`, `allMemories.filter()`, `createMergedMemories()`, `getMergeMemoryCandidates()`, `mergedMemoryIds.add()`, `mergedMemoryIds.has()`, `this.ensureConversationForGeneration()`, `this.hardDeleteMemoryById()`
- 参照: `memory.type`, `mergeableMemories.length`, `saved.id`

## MemoriesManager.getAllMemories()
- 位置: async L462-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.getMemories()`

## MemoriesManager.getMemoriesByID()
- 位置: async L473-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.getMemories()`

## MemoriesManager.resolveUsedMemories()
- 位置: async L490-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.getAllMemories()).filter()`, `Date.now()`, `MemoryStore.requestSave()`, `ids.has()`, `this.getAllMemories()`
- 参照: `ids.size`, `memory.id`, `memory.last_accessed`, `memory.lifetime_accessed_count`, `memory.recent_accessed_counts`, `used.length`

## MemoriesManager.getMemoriesByAttribute()
- 位置: async L525-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.getMemories()`

## MemoriesManager.getLastSessionMemoryTimestamp()
- 位置: async L540-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `MemoryStore.getMeta()`, `[ meta.last_history_memory_ts, meta.last_chat_memory_ts, ].filter()`
- 参照: `legacy.length`, `meta.last_chat_memory_ts`, `meta.last_history_memory_ts`, `meta.last_session_memory_ts`

## MemoriesManager.getSessionMemoryDeltaStartMs()
- 位置: L560-562
- 役割: (未記入)
- 触るとき: (未記入)

## MemoriesManager.setLastSessionMemoryTimestamp()
- 位置: async L570-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.updateMeta()`

## MemoriesManager.getLastGenerationRunTimestamp()
- 位置: async L582-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.getMeta()`
- 参照: `meta.last_generation_run_ts`, `meta.last_session_memory_ts`

## MemoriesManager.setLastGenerationRunTimestamp()
- 位置: async L593-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.updateMeta()`

## MemoriesManager.saveMemories()
- 位置: async L607-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if (Array.isArray(generatedMemories))` → `MemoryStore.addMemory()`
- 条件付き依存: `if (Array.isArray(generatedMemories))` → `persistedMemories.push()`

## MemoriesManager.saveRequestedMemory()
- 位置: async L629-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChatStore.getMostRecentMessages()`, `MemoryStore.addMemory()`, `_sensitiveInfoDetector.containsSensitiveInfo()`, `memorySummary.trim()`, `memorySummary.trim().slice()`
- 参照: `MESSAGE_ROLE.USER`, `recentUserMessages[0]?.content?.body`

## MemoriesManager.enrichExistingMemory()
- 位置: async L675-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.updateMemory()`, `this.memoryClassifyMessage()`
- 条件付き依存: `if (categories[0])` → `tags.push()`
- 条件付き依存: `if (intents[0])` → `tags.push()`

## MemoriesManager.softDeleteMemoryById()
- 位置: async L699-701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.softDeleteMemory()`

## MemoriesManager.hardDeleteMemoryById()
- 位置: async L713-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.hardDeleteMemory()`

## MemoriesManager.memoryClassifyMessage()
- 位置: async L723-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `getFormattedMemoryAttributeList()`, `loadPrompt()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `this.ensureConversationForUsage()`
- 参照: `MODEL_FEATURES.MEMORIES_MESSAGE_CLASSIFICATION_SYSTEM`, `MODEL_FEATURES.MEMORIES_MESSAGE_CLASSIFICATION_USER`, `parsed.categories`, `parsed.intents`

## MemoriesManager._clearEmbeddingsCache()
- 位置: L760-762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore._clearEmbeddingsCache()`

## MemoriesManager.getRelevantMemories()
- 位置: async L774-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoryStore.getRelevantMemories()`

## MemoriesManager.shouldEnableMemoriesFromSchedulers()
- 位置: L802-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.isAIWindowActive()`, `AIWindow.isAIWindowEnabled()`, `EveryWindow.readyWindows.some()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (source === SOURCE_HISTORY)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (source === SOURCE_CONVERSATION)` → `Services.prefs.getBoolPref()`
- 参照: `AIWindowAccountAuth.hasToSConsent`
- XPCOM: `Services.prefs`

## MemoriesManager.countRecentVisits()
- 位置: async L856-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `countRecentVisits()`
