# browser/components/aiwindow/models/memories/Memories.sys.mjs

source: browser/components/aiwindow/models/memories/Memories.sys.mjs
source-hash: f658af0ec5e46ea7e26da9471d537d4c5fc4cad3
lines: 922

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## runSessionMemoryPipeline()
- 位置: async L106-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `applyQualityAndSensitivityFilter()`, `batch.reduce()`, `candidateMemories.map()`, `candidateMemories.push()`, `console.error()`, `generateInitialMemoriesList()`, `mapFilteredMemoriesToInitialList()`, `openAIEngine.isRetryableError()`, `sessions.slice()`
- 条件付き依存: `if (openAIEngine.isRetryableError(e))` → `lazy.setTimeout()`
- 参照: `candidateMemories.length`, `filteredSummaries.length`, `memory.memory_summary`, `session.session_end_ms`, `sessions.length`

## computeMemoryStrength()
- 位置: L214-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.min()`, `Math.round()`, `Math.sqrt()`, `Object.values()`, `Object.values(memory.source_ids).reduce()`, `daysSince()`, `memory.sources.includes()`
- 参照: `memory.created_at`, `memory.last_accessed`, `memory.last_merged`, `memory.lifetime_accessed_count`, `memory.merge_count`, `memory.source_ids`, `sourceIds.length`

## daysSince()
- 位置: L228-228
- 役割: (未記入)
- 触るとき: (未記入)

## classifyMemoryAndCapStrength()
- 位置: L265-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (daysSinceCreated < minAgeDays)` → `Math.min()`
- 参照: `memory.created_at`, `memory.strength`, `memory.type`

## isShouldDeleteMemoryDueToDecay()
- 位置: L298-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.exp()`
- 参照: `memory.created_at`, `memory.last_accessed`, `memory.strength`

## computeMemoryFrecency()
- 位置: L319-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.pow()`
- 参照: `memory.recent_accessed_counts`

## formatListForPrompt()
- 位置: L337-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.map()`, `list.map(item => `- "${item}"`).join()`

## getFormattedMemoryAttributeList()
- 位置: L347-354
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (attributeName === CATEGORIES)` → `formatListForPrompt()`
- 条件付き依存: `if (attributeName === INTENTS)` → `formatListForPrompt()`

## renderSessionsForPrompt()
- 位置: L365-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blocks.join()`, `blocks.join("\n\n").trim()`, `blocks.push()`, `lines.join()`, `lines.push()`, `new Date(session.session_start_ms).toISOString()`, `new Date(session.session_start_ms).toISOString().slice()`, `sessions.forEach()`
- 条件付き依存: `if (session.search_queries.length)` → `lines.push()`
- 条件付き依存: `if (session.titles.length)` → `lines.push()`
- 条件付き依存: `if (session.chats.length)` → `message.content.trim()`
- 条件付き依存: `if (content)` → `chatLines.push()`
- 条件付き依存: `if (chatLines.length)` → `lines.push()`
- 参照: `chatLines.length`, `message.content`, `session.chats`, `session.chats.length`, `session.search_queries`, `session.search_queries.length`, `session.session_start_ms`, `session.titles`, `session.titles.length`

## sanitizeMemory()
- 位置: L416-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Math.round()`, `Number.isFinite()`, `deriveSource()`
- 条件付き依存: `if ( memory.memory_summary && memory.memory_summary.length > MAX_MEMORY_SUMMARY_LENGTH )` → `console.warn()`
- 参照: `memory.category`, `memory.entities`, `memory.evidence`, `memory.intent`, `memory.memory_summary`, `memory.memory_summary.length`, `memory.reasoning`, `memory.score`

## deriveSource()
- 位置: L473-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `evidence.map()`, `types.has()`
- 参照: `e?.type`, `evidence.length`

## attributeSourceIds()
- 位置: L509-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `msg.content.includes()`, `session.chats?.some()`, `session.search_queries.includes()`, `session.titles.includes()`
- 条件付き依存: `if (inBrowse)` → `session.history_source_ids.forEach()`
- 条件付き依存: `if (inBrowse)` → `historyIds.add()`
- 条件付き依存: `if (inChat)` → `session.conversation_source_ids.forEach()`
- 条件付き依存: `if (inChat)` → `conversationIds.add()`
- 参照: `item.value`, `item?.value`, `msg.content`

## normalizeMemoryList()
- 位置: L551-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `list.map()`, `list.map(sanitizeMemory).filter()`
- 条件付き依存: `if (!Array.isArray(list))` → `Array.isArray()`
- 参照: `list.items`

## generateInitialMemoriesList()
- 位置: async L580-650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Date.now()`, `Object.fromEntries()`, `Promise.all()`, `attributeSourceIds()`, `classifyMemoryAndCapStrength()`, `computeMemoryStrength()`, `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `getFormattedMemoryAttributeList()`, `lazy.loadPrompt()`, `normalizeMemoryList()`, `normalizeMemoryList(parsed).map()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `sources.hasOwnProperty()`
- 条件付き依存: `if (sources.hasOwnProperty(SESSIONS))` → `renderSessionsForPrompt()`
- 参照: `MODEL_FEATURES.MEMORIES_INITIAL_GENERATION_SYSTEM`, `MODEL_FEATURES.MEMORIES_INITIAL_GENERATION_USER`, `m.strength`, `memory.category`, `memory.evidence`, `memory.intent`, `memory.keywords`, `memory.memory_summary`, `memory.reasoning`, `memory.source`

## applyQualityAndSensitivityFilter()
- 位置: async L660-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `formatListForPrompt()`, `inputSet.has()`, `lazy.loadPrompt()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `parsed.kept_memories.filter()`, `renderPrompt()`
- 参照: `MODEL_FEATURES.MEMORIES_QUALITY_AND_SENSITIVITY_FILTER_SYSTEM`, `MODEL_FEATURES.MEMORIES_QUALITY_AND_SENSITIVITY_FILTER_USER`, `parsed.kept_memories`

## mapFilteredMemoriesToInitialList()
- 位置: async L705-712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filteredMemoriesList.includes()`, `initialMemories.filter()`
- 参照: `memory.memory_summary`

## getMergeMemoryCandidates()
- 位置: async L722-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `lazy.loadPrompt()`, `makeJSONSchemaBlob()`, `memoriesForPrompt.join()`, `memoriesForPrompt.push()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`
- 参照: `conversation.engine?.model`, `lazy.MODEL_FEATURES.MEMORIES_MERGE`, `memoriesMergeSystemPrompt.prompt`, `memoriesMergeUserPrompt.prompt`, `memory.memory_summary`, `memory.reasoning`

## latestTimestamp()
- 位置: L790-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `timestamps.filter()`
- 参照: `set.length`

## createMergedMemories()
- 位置: L804-921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.isArray()`, `Date.now()`, `Math.max()`, `Math.min()`, `Math.sumPrecise()`, `Object.fromEntries()`, `classifyMemoryAndCapStrength()`, `componentMemories.flatMap()`, `componentMemories.map()`, `componentMemories.reduce()`, `componentMemories.some()`, `componentMemoryIdsToDelete.add()`, `computeMemoryFrecency()`, `computeMemoryStrength()`, `finalMergedMemories.push()`, `latestTimestamp()`, `memories.filter()`, `mergedMemory.component_statements.includes()`
- 参照: `component.memory_summary`, `componentMemories.length`, `mem.component_summaries`, `mem.created_at`, `mem.id`, `mem.keywords`, `mem.last_accessed`, `mem.lifetime_accessed_count`, `mem.memory_summary`, `mem.merge_count`, `mem.reasoning`, `mem.recent_accessed_counts`, `mem.sensitivity_category`, `mem.source_ids?.conversation_source_ids`, `mem.source_ids?.history_source_ids`, `mem.sources`, `mem.tags`, `mem.updated_at`, `mergedMemory.component_statements`, `mergedMemory.new_reasoning`, `mergedMemory.new_reasoning.length`, `mergedMemory.new_statement`, `mergedMemory.new_statement.length`, `mergedMemoryToSave.frecency`, `mergedMemoryToSave.strength`
