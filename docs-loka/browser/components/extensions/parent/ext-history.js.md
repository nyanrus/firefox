# browser/components/extensions/parent/ext-history.js

source: browser/components/extensions/parent/ext-history.js
source-hash: 864038ae3c049c6e33520ba82324bae029a02522
lines: 325

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `TRANSITION_TYPE_TO_TRANSITIONS_MAP.set()`

## getTransitionType()
- 位置: L28-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TRANSITION_TO_TRANSITION_TYPES_MAP.get()`

## getTransition()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TRANSITION_TYPE_TO_TRANSITIONS_MAP.get()`

## convertRowToHistoryItem()
- 位置: L47-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.toDate()`, `PlacesUtils.toDate( row.getResultByName("last_visit_date") ).getTime()`, `row.getResultByName()`

## convertRowToVisitItem()
- 位置: L62-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.toDate()`, `PlacesUtils.toDate(row.getResultByName("visit_date")).getTime()`, `String()`, `getTransition()`, `row.getResultByName()`

## accumulateNavHistoryResults()
- 位置: L75-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `converter()`, `resultSet.getNextRow()`, `results.push()`

## executeAsyncQuery()
- 位置: L82-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.asyncExecuteLegacyQuery()`

## handleResult()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `accumulateNavHistoryResults()`

## handleError()
- 位置: L89-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`
- 参照: `error.message`, `error.result`

## handleCompletion()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## onVisited()
- 位置: L105-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.addListener()`

## listener()
- 位置: L106-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 参照: `event.lastKnownTitle`, `event.pageGuid`, `event.typedCount`, `event.url`, `event.visitCount`, `event.visitTime`

## unregister()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.removeListener()`

## convert()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)

## onVisitRemoved()
- 位置: L130-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.addListener()`

## listener()
- 位置: L131-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 条件付き依存: `if (!event.isPartialVisistsRemoval)` → `removedURLs.push()`
- 条件付き依存: `if (removedURLs.length)` → `fire.sync()`
- 参照: `event.isPartialVisistsRemoval`, `event.type`, `event.url`, `removedURLs.length`

## unregister()
- 位置: L159-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.removeListener()`

## convert()
- 位置: L165-167
- 役割: (未記入)
- 触るとき: (未記入)

## onTitleChanged()
- 位置: L170-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.addListener()`

## listener()
- 位置: L171-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 参照: `event.pageGuid`, `event.title`, `event.url`

## unregister()
- 位置: L184-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.removeListener()`

## convert()
- 位置: L190-192
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L197-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "history", event: "onTitleChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "history", event: "onVisitRemoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "history", event: "onVisited", extensionApi: this, }).api()`

## addUrl()
- 位置: L200-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.insert()`, `PlacesUtils.history.insert(pageInfo).then()`, `Promise.reject()`, `getTransitionType()`
- 条件付き依存: `if (details.visitTime)` → `normalizeTime()`
- 参照: `details.title`, `details.transition`, `details.url`, `details.visitTime`, `error.message`

## deleteAll()
- 位置: L227-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.clear()`

## deleteRange()
- 位置: L231-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history .removeVisitsByFilter()`, `PlacesUtils.history .removeVisitsByFilter(newFilter) .then()`, `normalizeTime()`
- 参照: `filter.endTime`, `filter.startTime`

## deleteUrl()
- 位置: L242-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.remove()`, `PlacesUtils.history.remove(url).then()`
- 参照: `details.url`

## search()
- 位置: L248-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `PlacesUtils.history.getNewQuery()`, `PlacesUtils.history.getNewQueryOptions()`, `PlacesUtils.toPRTime()`, `executeAsyncQuery()`, `normalizeTime()`
- 条件付き依存: `if (beginTime > endTime)` → `Promise.reject()`
- 参照: `Number.MAX_VALUE`, `historyQuery.beginTime`, `historyQuery.endTime`, `historyQuery.searchTerms`, `options.SORT_BY_DATE_DESCENDING`, `options.includeHidden`, `options.maxResults`, `options.sortingMode`, `query.endTime`, `query.maxResults`, `query.startTime`, `query.text`

## getVisits()
- 位置: L279-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.getNewQuery()`, `PlacesUtils.history.getNewQueryOptions()`, `Services.io.newURI()`, `executeAsyncQuery()`
- 条件付き依存: `if (!url)` → `Promise.reject()`
- 参照: `details.url`, `historyQuery.uri`, `options.RESULTS_AS_VISIT`, `options.SORT_BY_DATE_DESCENDING`, `options.includeHidden`, `options.resultType`, `options.sortingMode`
- XPCOM: `Services.io`
