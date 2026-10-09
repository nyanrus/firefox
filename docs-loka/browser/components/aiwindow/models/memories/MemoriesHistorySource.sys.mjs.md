# browser/components/aiwindow/models/memories/MemoriesHistorySource.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesHistorySource.sys.mjs
source-hash: 62635e660f0c1985c55587863e006e3dd6da7c06
lines: 1164

## <module>
- 役割: (未記入)
- 呼び出し先: `BlockListManager.initializeFromDefault()`, `ChromeUtils.defineESModuleGetters()`

## getDistanceThreshold()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `Number.parseFloat()`, `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getRecentHistory()
- 位置: async L124-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.withConnectionWrapper()`, `_mgr.matchAtWordBoundary()`, `_sensitiveInfoDetector.containsSensitiveInfo()`, `_sensitiveInfoDetector.containsSensitiveKeywords()`, `console.error()`, `db.execute()`, `out.push()`, `row.getResultByName()`, `safeDecodeURIComponent()`, `sanitizeUntrustedContent()`, `title.toLowerCase()`
- 条件付き依存: `if (sinceMicros != null)` → `Math.max()`
- 条件付き依存: `if (!(sinceMicros != null))` → `Math.max()`
- 条件付き依存: `if (!(sinceMicros != null))` → `Date.now()`
- 条件付き依存: `if (onlyTitle)` → `sanitizeTitle()`

## sessionizeVisits()
- 位置: L352-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Number.isFinite()`, `new Date(curStartMs).toISOString()`, `rows // Keep only rows with a valid timestamp .filter()`, `rows // Keep only rows with a valid timestamp .filter(row => Number.isFinite(row.visitDateMicros)) .map()`
- 参照: `a.visitTimeMs`, `b.visitTimeMs`, `opts.gapSec`, `opts.maxSessionSec`, `row.session_id`, `row.session_start_iso`, `row.session_start_ms`, `row.visitDateMicros`, `row.visitTimeMs`

## generateProfileInputs()
- 位置: L413-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Number()`, `Object.entries()`, `Object.keys()`, `bySession.get()`, `bySession.get(sessionId).push()`, `bySession.has()`, `bySession.keys()`, `isFiniteNumber()`, `items .filter()`, `items .filter(Number.isFinite) .map()`, `items.filter()`, `normalizeEpochSeconds()`, `preparedInputs.push()`, `searchItems.map()`, `searchItems.map(r => r.title).filter()`
- 条件付き依存: `if (!bySession.has(sessionId))` → `bySession.set()`
- 条件付き依存: `if (tsList.length)` → `Math.min()`
- 条件付き依存: `if (tsList.length)` → `Math.max()`
- 参照: `Number.isFinite`, `Object.keys(m).length`, `r.domain`, `r.domainFrequencyPct`, `r.frequencyPct`, `r.host`, `r.source`, `r.title`, `r.visitDateMicros`, `row.session_id`, `searchItems.length`, `sessionTimes.end_time`, `sessionTimes.start_time`, `tsList.length`

## aggregateSessions()
- 位置: L528-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Date.now()`, `Math.max()`, `Number()`, `Number.isFinite()`, `Object.create()`, `Object.entries()`, `Object.keys()`, `Object.values()`, `getOrInit()`, `rec.sessions.add()`, `round2()`
- 条件付き依存: `if (hasSearchContent)` → `getOrInit()`
- 条件付き依存: `if (hasSearchContent)` → `Number()`
- 条件付き依存: `if (hasSearchContent)` → `rec.search_titles.add()`
- 条件付き依存: `if (hasSearchContent)` → `Math.max()`
- 条件付き依存: `if (hasSearchContent)` → `toSeconds()`
- 参照: `preparedInputs.length`, `rec.last_searched`, `rec.last_seen`, `rec.num_sessions`, `rec.score`, `rec.search_count`, `rec.search_titles`, `rec.session_importance`, `rec.sessions`, `rec.sessions.size`, `search_titles.length`, `session.domain_scores`, `session.search_events`, `session.session_end_time`, `session.session_id`, `session.session_start_time`, `session.title_scores`

## topkAggregates()
- 位置: L663-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Number()`, `Number.isFinite()`, `Object.entries()`, `Object.entries(aggDomains).map()`, `Object.entries(aggSearches).map()`, `Object.entries(aggTitles).map()`, `domainRanked .slice()`, `domainRanked .slice(0, k_domains) .map()`, `domainRanked.sort()`, `round2()`, `searchRanked .slice()`, `searchRanked .slice(0, k_searches) .map()`, `searchRanked.sort()`, `titleRanked .slice()`, `titleRanked .slice(0, k_titles) .map()`, `titleRanked.sort()`, `withRecency()`
- 条件付き依存: `if (now == null)` → `Date.now()`
- 条件付き依存: `if (!(now == null))` → `Number()`
- 参照: `a.cnt`, `a.last_seen`, `a.ls`, `a.num_sessions`, `a.rank`, `b.cnt`, `b.last_seen`, `b.ls`, `b.num_sessions`, `b.rank`, `info.last_searched`, `info.last_seen`, `info.num_sessions`, `info.score`, `info.search_count`, `info.search_titles`, `info.session_importance`

## withRecency()
- 位置: L798-818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `Math.pow()`, `Number()`, `round2()`, `toSeconds()`

## isFiniteNumber()
- 位置: L820-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`

## normalizeEpochSeconds()
- 位置: L830-835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Number.isFinite()`

## toSeconds()
- 位置: L837-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `Number.isFinite()`

## getOrInit()
- 位置: L845-850
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(key in mapObj))` → `initFn()`

## round2()
- 位置: L852-854
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `Number()`

## safeDecodeURIComponent()
- 位置: L856-865
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeURIComponent()`

## sanitizeTitle()
- 位置: L876-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `title .replace()`, `title .replace(/\\/g, "/") // Replace backslash with forward slash // eslint-disable-next-line no-control-regex .replace()`

## _setBlockListManagerForTesting()
- 位置: L892-894
- 役割: (未記入)
- 触るとき: (未記入)

## _sanitizeTitleForTesting()
- 位置: L896-898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sanitizeTitle()`

## countRecentVisits()
- 位置: async L907-938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `Number()`, `PlacesUtils.withConnectionWrapper()`, `console.error()`, `db.execute()`, `row.getResultByName()`

## getHistorySourceIdsFromMemory()
- 位置: L946-948
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `memory?.source_ids?.history_source_ids`

## resolveUrlsForMemories()
- 位置: async L965-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.withConnectionWrapper()`, `Services.prefs.getBoolPref()`, `bindUrlHashes()`, `console.error()`, `db.execute()`, `getDistanceThreshold()`, `getHistorySourceIdsFromMemory()`, `memories.flatMap()`, `placeholders.join()`, `row.getResultByName()`, `rows.map()`
- 条件付き依存: `if (filterBySummary)` → `resolveUrlsBySummarySimilarity()`
- 参照: `urlHashes.length`
- XPCOM: `Services.prefs`

## bindUrlHashes()
- 位置: L1049-1057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `urlHashes.map()`

## getMemoryEmbeddingText()
- 位置: L1065-1069
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[summary, reasoning].filter()`, `[summary, reasoning].filter(part => part?.trim()).join()`, `memory?.memory_summary?.toLowerCase()`, `memory?.reasoning?.toLowerCase()`, `part?.trim()`

## resolveUrlsBySummarySimilarity()
- 位置: async L1080-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.tensorToSQLBindable()`, `[...resolved].sort()`, `bindUrlHashes()`, `conn.execute()`, `console.error()`, `getHistorySourceIdsFromMemory()`, `getMemoryEmbeddingText()`, `lazy.extractVectorFromTensor()`, `lazy.getPlacesSemanticHistoryManager()`, `placeholders.join()`, `resolved.get()`, `resolved.set()`, `row.getResultByName()`, `semanticManager.embedder.embed()`, `semanticManager.embedder.ensureEngine()`, `semanticManager.getConnection()`, `semanticManager.hasSufficientEntriesForSearching()`
- 条件付き依存: `if (existing)` → `Math.min()`
- 参照: `a.distance`, `b.distance`, `existing.distance`, `semanticManager.isEnabledForSmartWindow`, `urlHashes.length`
