# browser/components/aiwindow/services/MemoryStore.sys.mjs

source: browser/components/aiwindow/services/MemoryStore.sys.mjs
source-hash: 89dc802d8341dae29ce514622ccbac94e652a10b
lines: 1083

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `PathUtils.join()`, `Services.dirsvc.get()`, `console.createInstance()`

## normalizeSourceIds()
- 位置: L79-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `raw.conversation_source_ids`, `raw.history_source_ids`, `raw?.conversation_source_ids`, `raw?.history_source_ids`

## unionSourceIds()
- 位置: L98-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalizeSourceIds()`
- 参照: `an.conversation_source_ids`, `an.history_source_ids`, `bn.conversation_source_ids`, `bn.history_source_ids`

## isComponentSummaries()
- 位置: L120-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `v.every()`
- 参照: `component.memory_summary`, `component.reasoning`

## migrateMemoryStoreVersionOneToTwo()
- 位置: L158-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `computeMemoryFrecency()`, `computeMemoryStrength()`, `memories.map()`, `normalizeSourceIds()`
- 条件付き依存: `if (!m.tags)` → `m.hasOwnProperty()`
- 条件付き依存: `if (m.category)` → `m.tags.push()`
- 条件付き依存: `if (m.intent)` → `m.tags.push()`
- 条件付き依存: `if (!m.updated_at)` → `Date.now()`
- 条件付き依存: `if (!m.recent_accessed_counts)` → `Object.fromEntries()`
- 条件付き依存: `if (!m.recent_accessed_counts)` → `Array.from()`
- 参照: `m.category`, `m.component_summaries`, `m.created_at`, `m.entities`, `m.frecency`, `m.intent`, `m.is_deleted`, `m.keywords`, `m.last_accessed`, `m.reasoning`, `m.recent_accessed_counts`, `m.score`, `m.sensitivity_category`, `m.source`, `m.source_ids`, `m.source_ids.conversation_source_ids.length`, `m.source_ids.history_source_ids.length`, `m.sources`, `m.strength`, `m.tags`, `m.type`, `m.updated_at`

## loadMemories()
- 位置: async L276-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.profiler.IsActive()`, `console.error()`, `gJSONFile.load()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `IOUtils.stat()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `(stat.size / 1048576).toFixed()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `ChromeUtils.now()`
- 条件付き依存: `if (markerData)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!(!data || typeof data !== "object"))` → `Array.isArray()`
- 条件付き依存: `if (!(data.version === MEMORY_STORE_VERSION && Array.isArray(data.memories)))` → `Array.isArray()`
- 条件付き依存: `if ( typeof data.version === "number" && data.version === 1 && Array.isArray(data.memories) )` → `migrateMemoryStoreVersionOneToTwo()`
- 条件付き依存: `if (!( typeof data.version === "number" && data.version === 1 && Array.isArray(data.memories) ))` → `lazy.console.warn()`
- 条件付き依存: `if (!(!data || typeof data !== "object"))` → `memories.map()`
- 条件付き依存: `if (isMemoriesMigrated)` → `gJSONFile?.saveSoon()`
- 条件付き依存: `if (isMemoriesMigrated)` → `Services.obs.notifyObservers()`
- 参照: `data.memories`, `data.meta?.last_chat_memory_ts`, `data.meta?.last_generation_run_ts`, `data.meta?.last_history_memory_ts`, `data.meta?.last_session_memory_ts`, `data.version`, `gJSONFile.data`, `lazy.gStorePath`, `markerData.sizeLabel`, `markerData.startTime`, `mem.merge_count`, `stat.size`
- XPCOM: `Services.obs` / `Services.profiler`

## ensureInitialized()
- 位置: async L385-395
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!gInitPromise)` → `loadMemories()`

## requestSave()
- 位置: async L400-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gJSONFile?.saveSoon()`, `this.ensureInitialized()`

## testOnlyFlush()
- 位置: async L410-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gJSONFile._save()`, `this.ensureInitialized()`

## addMemory()
- 位置: async L472-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `makeMemoryId()`, `this.ensureInitialized()`, `this.updateMemory()`, `updateMemoriesCountMetric()`
- 条件付き依存: `if (!memory)` → `normalizeSourceIds()`
- 条件付き依存: `if (!memory)` → `Object.fromEntries()`
- 条件付き依存: `if (!memory)` → `Array.from()`
- 条件付き依存: `if (!memory)` → `gState.memories.push()`
- 条件付き依存: `if (!memory)` → `gJSONFile?.saveSoon()`
- 条件付き依存: `if (!memory)` → `Services.obs.notifyObservers()`
- 参照: `memoryPartial.component_summaries`, `memoryPartial.created_at`, `memoryPartial.frecency`, `memoryPartial.is_deleted`, `memoryPartial.keywords`, `memoryPartial.last_accessed`, `memoryPartial.last_merged`, `memoryPartial.lifetime_accessed_count`, `memoryPartial.memory_summary`, `memoryPartial.merge_count`, `memoryPartial.reasoning`, `memoryPartial.recent_accessed_counts`, `memoryPartial.sensitivity_category`, `memoryPartial.source_ids`, `memoryPartial.sources`, `memoryPartial.strength`, `memoryPartial.tags`, `memoryPartial.type`, `memoryPartial.updated_at`, `source_ids.conversation_source_ids.length`, `source_ids.history_source_ids.length`
- XPCOM: `Services.obs`

## updateMemory()
- 位置: async L553-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Date.now()`, `MEMORY_SENSIVITITY_CATEGORIES.includes()`, `MEMORY_TYPES.includes()`, `Number.isFinite()`, `Object.values()`, `Object.values(v).every()`, `Services.obs.notifyObservers()`, `gJSONFile?.saveSoon()`, `gState.memories.find()`, `isComponentSummaries()`, `this.ensureInitialized()`, `v.every()`, `val.every()`, `validator()`
- 条件付き依存: `if (prop in updates && validator(updates[prop]))` → `Array.isArray()`
- 条件付き依存: `if (updates.source_ids)` → `unionSourceIds()`
- 条件付き依存: `if (isComponentSummaries(updates.component_summaries))` → `[...memory.component_summaries, ...updates.component_summaries].map()`
- 参照: `component.memory_summary`, `i.id`, `memory.component_summaries`, `memory.source_ids`, `memory.updated_at`, `updates.component_summaries`, `updates.source_ids`, `updates.updated_at`
- XPCOM: `Services.obs`

## softDeleteMemory()
- 位置: async L652-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this.updateMemory()`, `updateMemoriesCountMetric()`
- XPCOM: `Services.obs`

## hardDeleteMemory()
- 位置: async L667-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoryRemovedPanel.record()`, `Services.obs.notifyObservers()`, `gJSONFile?.saveSoon()`, `gState.memories.findIndex()`, `gState.memories.splice()`, `this.ensureInitialized()`, `updateMemoriesCountMetric()`
- 参照: `gState.memories.length`, `i.id`
- XPCOM: `Services.obs`

## computeMemoriesHash()
- 位置: L693-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `str.charCodeAt()`
- 参照: `m.id`, `m.memory_summary`, `str.length`

## _clearEmbeddingsCache()
- 位置: L712-715
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.memoryCacheKey`, `this.memoryEmbeddingsCache`

## getRelevantMemories()
- 位置: async L728-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `cosSim()`, `message.toLowerCase()`, `similarities .filter()`, `similarities .filter(m => m.similarity >= similarityThreshold) .sort()`, `similarities .filter(m => m.similarity >= similarityThreshold) .sort((a, b) => b.similarity - a.similarity) .slice()`, `this.computeMemoriesHash()`, `this.embeddingsGenerator.embed()`, `this.getMemories()`, `this.memoryEmbeddingsCache.map()`
- 条件付き依存: `if (!this.embeddingsGenerator)` → `embeddingsGeneratorFactory.forGeneral()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `memories.map()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.memory_summary?.toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.reasoning?.toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.tags?.join(" ").toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.tags?.join()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `[tags, summary, reasoning] .filter(part => part?.trim()) .join(". ") .toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `[tags, summary, reasoning] .filter(part => part?.trim()) .join()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `[tags, summary, reasoning] .filter()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `part?.trim()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `this.embeddingsGenerator.embedMany()`
- 参照: `a.similarity`, `b.similarity`, `m.similarity`, `memories.length`, `queryEmbedding.length`, `queryResult.output`, `result.output`, `this.embeddingsGenerator`, `this.memoryCacheKey`, `this.memoryEmbeddingsCache`

## parseAggregateDays()
- 位置: L794-811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...days].filter()`, `dayList.split()`, `token.trim()`, `trimmed.match()`
- 条件付き依存: `if (range)` → `Number()`
- 条件付き依存: `if (range)` → `days.add()`
- 条件付き依存: `if (!(range))` → `days.add()`
- 条件付き依存: `if (!(range))` → `Number()`

## resolveFilterField()
- 位置: L823-839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `field.match()`, `this.parseAggregateDays()`, `this.parseAggregateDays(dayList).reduce()`

## getMemories()
- 位置: async L886-966
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(MEMORY_FILTER_COMPARATOR).includes()`, `this.ensureInitialized()`, `validators.field()`, `validators.value()`
- 条件付き依存: `if (!includeSoftDeleted)` → `res.filter()`
- 条件付き依存: `if (memoryIds.size)` → `res.filter()`
- 条件付き依存: `if (memoryIds.size)` → `memoryIds.has()`
- 条件付き依存: `if (!Object.values(MEMORY_FILTER_COMPARATOR).includes(comparator))` → `lazy.console.error()`
- 条件付き依存: `if (!validators.field(field))` → `lazy.console.error()`
- 条件付き依存: `if (!validators.value(value))` → `lazy.console.error()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `( await this.getRelevantMemories(value, topK, similarityThreshold) ).map()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `this.getRelevantMemories()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `res.filter()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `semanticMatches.has()`
- 条件付き依存: `if (predicate)` → `res.filter()`
- 条件付き依存: `if (predicate)` → `predicate()`
- 条件付き依存: `if (predicate)` → `this.resolveFilterField()`
- 条件付き依存: `if (sortBy)` → `[...res].sort()`
- 参照: `MEMORY_FILTER_COMPARATOR.LIKE`, `gState.memories`, `i.id`, `i.is_deleted`, `memoryIds.size`

## getMeta()
- 位置: async L973-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredClone()`, `this.ensureInitialized()`
- 参照: `gState.meta`

## updateMeta()
- 位置: async L989-1007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `gJSONFile?.saveSoon()`, `this.ensureInitialized()`, `updateMemoriesLastUpdatedMetric()`, `validator()`
- 参照: `gState.meta`

## updateMemoriesCountMetric()
- 位置: L1010-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoriesCount.conversation.set()`, `Glean.smartWindow.memoriesCount.history.set()`, `Glean.smartWindow.memoriesCount.session.set()`, `memory.sources?.includes()`, `updateMemoriesLastUpdatedMetric()`
- 条件付き依存: `if (!(memory.sources?.includes(CONVERSATION)))` → `memory.sources?.includes()`
- 条件付き依存: `if (!(memory.sources?.includes(HISTORY)))` → `memory.sources?.includes()`
- 参照: `gState.memories`, `memory.is_deleted`

## updateMemoriesLastUpdatedMetric()
- 位置: L1035-1046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.smartWindow.memoriesLastUpdated.set()`, `Math.max()`
- 参照: `gState.meta.last_chat_memory_ts`, `gState.meta.last_history_memory_ts`, `gState.meta.last_session_memory_ts`

## hashStringToHex()
- 位置: L1055-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hash.toString()`, `hash.toString(16).padStart()`, `str.charCodeAt()`
- 参照: `str.length`

## makeMemoryId()
- 位置: L1073-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(memoryPartial.memory_summary || "").trim()`, `(memoryPartial.memory_summary || "").trim().toLowerCase()`, `hashStringToHex()`
- 参照: `memoryPartial.id`, `memoryPartial.memory_summary`
