# browser/components/firefoxview/HistoryController.sys.mjs

source: browser/components/firefoxview/HistoryController.sys.mjs
source-hash: bd8049229f6dfd246963119cad9bc4ebc0b9ad23
lines: 531

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## HistoryController.constructor()
- 位置: L69-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `host.addController()`
- 参照: `lazy.PlacesQuery`, `this.component`, `this.historyCache`, `this.host`, `this.placesQuery`, `this.searchQuery`, `this.searchResultsLimit`, `this.sortOption`

## HistoryController.hostConnected()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.placesQuery.observeHistory()`, `this.updateCache()`

## HistoryController.hostDisconnected()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.placesQuery.close()`

## HistoryController.deleteFromHistory()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.history.remove()`
- 参照: `this.host.triggerNode.url`

## HistoryController.onSearchQuery()
- 位置: L106-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateCache()`
- 参照: `e.detail.query`, `this.searchQuery`

## HistoryController.onChangeSortOption()
- 位置: L111-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateCache()`
- 参照: `e.target.value`, `this.sortOption`

## HistoryController.historyVisits()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.historyCache.entries`

## HistoryController.isHistoryPending()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.historyCache.entries`

## HistoryController.searchResults()
- 位置: L124-129
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.historyCache.entries`, `this.historyCache.entries?.length`, `this.historyCache.entries[0].items`, `this.historyCache.searchQuery`

## HistoryController.totalVisitsCount()
- 位置: L131-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.historyVisits.reduce()`
- 参照: `entry.items.length`

## HistoryController.isHistoryEmpty()
- 位置: L138-140
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.historyVisits.length`

## HistoryController.updateCache()
- 位置: async L149-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getVisitsForSearchQuery()`, `this.#getVisitsForSortOption()`, `this.host.requestUpdate()`
- 条件付き依存: `if (sortOption === "datesite" && !searchQuery)` → `this.#normalizeVisit()`
- 条件付き依存: `if (!(sortOption === "datesite" && !searchQuery))` → `this.#normalizeVisit()`
- 参照: `this.historyCache`, `this.searchQuery`, `this.sortOption`

## HistoryController.#normalizeVisit()
- 位置: L186-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `this.placesQuery.getStartOfDayTimestamp()`, `visit.date.getTime()`
- 参照: `this.sortOption`, `visit.date`, `visit.guid`, `visit.icon`, `visit.pageGuid`, `visit.primaryL10nArgs`, `visit.primaryL10nId`, `visit.secondaryL10nArgs`, `visit.secondaryL10nId`, `visit.time`, `visit.title`, `visit.url`

## HistoryController.#getVisitsForSearchQuery()
- 位置: async L213-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLogger()`, `getLogger("HistoryController").warn()`, `this.placesQuery.searchHistory()`
- 参照: `this.searchResultsLimit`

## HistoryController.#getVisitsForSortOption()
- 位置: async L229-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getVisitsForDate()`, `this.#getVisitsForDateSite()`, `this.#getVisitsForLastVisited()`, `this.#getVisitsForSite()`, `this.#setTodaysDate()`
- 条件付き依存: `if (!historyMap)` → `this.#fetchHistory()`

## HistoryController.#setTodaysDate()
- 位置: L254-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `now.getDate()`, `now.getFullYear()`, `now.getMonth()`
- 参照: `this.#todaysDate`, `this.#yesterdaysDate`

## HistoryController.#getVisitsForDate()
- 位置: L274-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries.push()`, `this.#getVisitsByDay()`, `this.#getVisitsByMonth()`, `this.#getVisitsFromToday()`, `this.#getVisitsFromYesterday()`, `visitsByDay.forEach()`, `visitsByMonth.forEach()`
- 条件付き依存: `if (visitsFromToday.length)` → `entries.push()`
- 条件付き依存: `if (visitsFromYesterday.length)` → `entries.push()`
- 参照: `this.component`, `visitsFromToday.length`, `visitsFromYesterday.length`

## HistoryController.#getVisitsFromToday()
- 位置: L313-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cachedHistory.get()`, `this.placesQuery.getStartOfDayTimestamp()`
- 参照: `this.#todaysDate`

## HistoryController.#getVisitsFromYesterday()
- 位置: L319-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cachedHistory.get()`, `this.placesQuery.getStartOfDayTimestamp()`
- 参照: `this.#yesterdaysDate`

## HistoryController.#getVisitsByDay()
- 位置: L336-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cachedHistory.entries()`, `this.#isSameDate()`
- 条件付き依存: `if (!( this.#isSameDate(date, this.#todaysDate) || this.#isSameDate(date, this.#yesterdaysDate) ))` → `this.#isSameMonth()`
- 条件付き依存: `if (!(!this.#isSameMonth(date, this.#todaysDate)))` → `visitsPerDay.push()`
- 参照: `this.#todaysDate`, `this.#yesterdaysDate`

## HistoryController.#getVisitsByMonth()
- 位置: L364-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cachedHistory.entries()`, `this.#isSameDate()`, `this.#isSameMonth()`, `this.placesQuery.getStartOfMonthTimestamp()`
- 条件付き依存: `if (month !== previousMonth)` → `visitsPerMonth.push()`
- 条件付き依存: `if (this.sortOption === "datesite")` → `this.#mergeMaps()`
- 条件付き依存: `if (this.sortOption === "datesite")` → `visitsPerMonth.at()`
- 条件付き依存: `if (!(this.sortOption === "datesite"))` → `visitsPerMonth .at(-1) .concat()`
- 条件付き依存: `if (!(this.sortOption === "datesite"))` → `visitsPerMonth .at()`
- 参照: `this.#todaysDate`, `this.#yesterdaysDate`, `this.sortOption`, `visitsPerMonth.length`

## HistoryController.#isSameDate()
- 位置: L402-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `date.getDate()`, `dateToCheck.getDate()`, `this.#isSameMonth()`

## HistoryController.#isSameMonth()
- 位置: L417-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dateToCheck.getFullYear()`, `dateToCheck.getMonth()`, `month.getFullYear()`, `month.getMonth()`

## HistoryController.#mergeMaps()
- 位置: L431-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `map.get()`, `map.set()`, `oldVisits?.concat()`

## HistoryController.#getVisitsForSite()
- 位置: L446-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `a.domain.localeCompare()`, `historyMap.entries()`
- 参照: `b.domain`

## HistoryController.#getVisitsForDateSite()
- 位置: L461-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries.push()`, `sortItems()`, `this.#getVisitsByDay()`, `this.#getVisitsByMonth()`, `this.#getVisitsFromToday()`, `this.#getVisitsFromYesterday()`, `visitsByDay.forEach()`, `visitsByMonth.forEach()`
- 条件付き依存: `if (visitsFromToday.length)` → `entries.push()`
- 条件付き依存: `if (visitsFromToday.length)` → `sortItems()`
- 条件付き依存: `if (visitsFromYesterday.length)` → `entries.push()`
- 条件付き依存: `if (visitsFromYesterday.length)` → `sortItems()`
- 参照: `this.component`, `visitsFromToday.length`, `visitsFromYesterday.length`

## sortItems()
- 位置: L474-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDomain.localeCompare()`, `items.sort()`

## HistoryController.#getVisitsForLastVisited()
- 位置: L519-521
- 役割: (未記入)
- 触るとき: (未記入)

## HistoryController.#fetchHistory()
- 位置: async L523-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.placesQuery.getHistory()`
- 参照: `this.sortOption`
