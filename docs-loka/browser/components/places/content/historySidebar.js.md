# browser/components/places/content/historySidebar.js

source: browser/components/places/content/historySidebar.js
source-hash: 9555027ed08c54fe669e280d240dcba4e84d415c
lines: 194

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Glean.historySidebar.filterType[gHistoryGrouping].add()`, `GroupBy()`, `PlacesUIUtils.onSidebarTreeClick()`, `PlacesUIUtils.onSidebarTreeKeyPress()`, `PlacesUIUtils.onSidebarTreeMouseMove()`, `PlacesUIUtils.setMouseoverURL()`, `XPCOMUtils.defineLazyScriptGetter()`, `bhTooltip.addEventListener()`, `bhTooltip.removeAttribute()`, `clearCumulativeCounters()`, `document .querySelector()`, `document .querySelector("#viewButton > menupopup") .addEventListener()`, `document.getElementById()`, `event.target.id.slice()`, `gHistoryTree.addEventListener()`, `gSearchBox.addEventListener()`, `gSearchBox.focus()`, `searchHistory()`, `viewButton.getAttribute()`, `viewButton.setAttribute()`, `window.addEventListener()`, `window.top.BookmarksEventHandler.fillInBHTooltip()`, `window.top.document.documentElement.getAttribute()`

## GroupBy()
- 位置: L96-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchHistory()`
- 条件付き依存: `if (groupingType != gHistoryGrouping)` → `Glean.historySidebar.filterType[groupingType].add()`
- 参照: `Glean.historySidebar.filterType`, `gSearchBox.value`

## updateTelemetry()
- 位置: L105-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.historySidebar.cumulativeFilterCount.accumulateSingleSample()`, `Glean.historySidebar.cumulativeSearches.accumulateSingleSample()`, `Glean.sidebar.link.history.add()`, `clearCumulativeCounters()`
- 参照: `urlsOpened.length`

## searchHistory()
- 位置: L117-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.getNewQuery()`, `PlacesUtils.history.getNewQueryOptions()`, `gHistoryTree.load()`
- 条件付き依存: `if (gHistoryGrouping == "lastvisited")` → `Glean.historySidebar.lastvisitedTreeQueryTime.start()`
- 条件付き依存: `if (aInput)` → `Glean.sidebar.search.history.add()`
- 条件付き依存: `if (gHistoryGrouping == "lastvisited")` → `Glean.historySidebar.lastvisitedTreeQueryTime.stopAndAccumulate()`
- 参照: `Ci.nsINavHistoryQueryOptions`, `NHQO.RESULTS_AS_DATE_QUERY`, `NHQO.RESULTS_AS_DATE_SITE_QUERY`, `NHQO.RESULTS_AS_SITE_QUERY`, `NHQO.RESULTS_AS_URI`, `NHQO.SORT_BY_DATE_DESCENDING`, `NHQO.SORT_BY_FRECENCY_DESCENDING`, `NHQO.SORT_BY_TITLE_ASCENDING`, `NHQO.SORT_BY_VISITCOUNT_DESCENDING`, `options.includeHidden`, `options.resultType`, `options.sortingMode`, `query.searchTerms`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## clearCumulativeCounters()
- 位置: L183-186
- 役割: (未記入)
- 触るとき: (未記入)
