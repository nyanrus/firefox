# browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs

source: browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs
source-hash: bfec6e881f1350c84255653442105996cc44b8f0
lines: 714

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isoToMicroseconds()
- 位置: L23-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `new Date(iso).getTime()`

## buildHistoryRow()
- 位置: L53-105
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!fromNode)` → `row.getResultByName()`
- 条件付き依存: `if (typeof lastVisitRaw === "number")` → `new Date(Math.round(lastVisitRaw / 1000)).toISOString()`
- 条件付き依存: `if (typeof lastVisitRaw === "number")` → `Math.round()`
- 条件付き依存: `if (lastVisitRaw instanceof Date)` → `lastVisitRaw.toISOString()`
- 条件付き依存: `if (!(!fromNode))` → `lazy.PlacesUtils.toDate()`
- 条件付き依存: `if (!(!fromNode))` → `lastVisitDate.toISOString()`
- 参照: `row.accessCount`, `row.frecency`, `row.time`, `row.title`, `row.uri`

## mergeHistoryResultsRRF()
- 位置: L132-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `byUrl.get()`, `byUrl.has()`, `byUrl.values()`, `entries.slice()`, `entries.slice(0, historyLimit).map()`, `entries.sort()`, `new Date(entry.visitDate).getTime()`
- 条件付き依存: `if (!byUrl.has(row.url))` → `byUrl.set()`
- 参照: `a._rrf`, `a._visitMs`, `a.visitCount`, `b._rrf`, `b._visitMs`, `b.visitCount`, `byUrl.get(row.url)._rrf`, `entry._rrf`, `entry._visitMs`, `entry.title`, `entry.visitCount`, `entry.visitDate`, `keywordRows.length`, `row.title`, `row.url`, `row.visitCount`, `row.visitDate`, `semanticRows.length`

## searchBrowsingHistoryHybrid()
- 位置: async L217-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Promise.all()`, `mergeHistoryResultsRRF()`, `searchBrowsingHistoryBasic()`, `searchBrowsingHistorySemantic()`
- 条件付き依存: `if (rows.length < historyLimit)` → `lazy.SearchBrowsingHistoryDomainBoost.matchDomains()`
- 条件付き依存: `if (domains?.length)` → `lazy.getPlacesSemanticHistoryManager()`
- 条件付き依存: `if (domains?.length)` → `semanticManager.getConnection()`
- 条件付き依存: `if (domains?.length)` → `lazy.SearchBrowsingHistoryDomainBoost.searchByDomains()`
- 条件付き依存: `if (domains?.length)` → `Math.max()`
- 条件付き依存: `if (domains?.length)` → `lazy.SearchBrowsingHistoryDomainBoost.mergeDedupe()`
- 参照: `domains?.length`, `rows.length`

## searchBrowsingHistoryTimeRange()
- 位置: async L284-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildHistoryRow()`, `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `results.push()`, `rows.push()`

## extractVectorFromTensor()
- 位置: L337-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `ArrayBuffer.isView()`
- 条件付き依存: `if (tensor.output)` → `Array.isArray()`
- 条件付き依存: `if (tensor.output)` → `ArrayBuffer.isView()`
- 参照: `tensor.length`, `tensor.output`

## searchBrowsingHistorySemantic()
- 位置: async L393-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.max()`, `Math.min()`, `buildHistoryRow()`, `conn.execute()`, `conn.executeCached()`, `extractVectorFromTensor()`, `lazy.PlacesUtils.tensorToSQLBindable()`, `lazy.getPlacesSemanticHistoryManager()`, `rows.push()`, `semanticManager.embedder.embed()`, `semanticManager.embedder.ensureEngine()`, `semanticManager.getConnection()`

## backfillThumbnails()
- 位置: async L485-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Map.groupBy()`, `console.error()`, `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `result.getResultByName()`, `rows.filter()`, `rowsByUrl.get()`, `rowsByUrl.keys()`
- 参照: `row.thumbnail`, `row.url`, `rowsMissingThumbnail.length`

## searchBrowsingHistoryBasic()
- 位置: async L536-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildHistoryRow()`, `console.error()`, `currentHistory.executeQuery()`, `currentHistory.getNewQuery()`, `currentHistory.getNewQueryOptions()`, `root.getChild()`, `rows.push()`
- 参照: `Ci.nsINavHistoryQuery.TIME_RELATIVE_EPOCH`, `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_URI`, `Ci.nsINavHistoryQueryOptions.SORT_BY_FRECENCY_DESCENDING`, `lazy.PlacesUtils.history`, `opts.excludeQueries`, `opts.maxResults`, `opts.queryType`, `opts.resultType`, `opts.sortingMode`, `query.beginTime`, `query.beginTimeReference`, `query.endTime`, `query.endTimeReference`, `query.searchTerms`, `result.root`, `root.childCount`, `root.containerOpen`, `rows.length`
- XPCOM: [`nsINavHistoryQuery`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## searchBrowsingHistory()
- 位置: async L628-713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getFloatPref()`, `backfillThumbnails()`, `console.error()`, `isoToMicroseconds()`, `lazy.getPlacesSemanticHistoryManager()`, `searchTerm?.trim()`, `semanticManager.hasSufficientEntriesForSearching()`
- 条件付き依存: `if (!searchTerm?.trim())` → `searchBrowsingHistoryTimeRange()`
- 条件付き依存: `if (canUseSemantic)` → `searchBrowsingHistoryHybrid()`
- 条件付き依存: `if (!(canUseSemantic))` → `searchBrowsingHistoryBasic()`
- 参照: `error.message`, `rows.length`, `semanticManager.isEnabledForSmartWindow`
- XPCOM: `Services.prefs`
