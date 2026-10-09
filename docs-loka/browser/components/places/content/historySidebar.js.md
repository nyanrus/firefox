# browser/components/places/content/historySidebar.js

source: browser/components/places/content/historySidebar.js
source-hash: 9555027ed08c54fe669e280d240dcba4e84d415c
lines: 194

## <module>
- 役割: 履歴サイドバーのページ全体を組み立てる。Places の共有スクリプトを読み込み、ツリーのイベント接続、表示グループ化の初期化、検索ボックスの接続を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Glean.historySidebar.filterType[gHistoryGrouping].add()`, `GroupBy()`, `PlacesUIUtils.onSidebarTreeClick()`, `PlacesUIUtils.onSidebarTreeKeyPress()`, `PlacesUIUtils.onSidebarTreeMouseMove()`, `PlacesUIUtils.setMouseoverURL()`, `XPCOMUtils.defineLazyScriptGetter()`, `bhTooltip.addEventListener()`, `bhTooltip.removeAttribute()`, `clearCumulativeCounters()`, `document .querySelector()`, `document .querySelector("#viewButton > menupopup") .addEventListener()`, `document.getElementById()`, `event.target.id.slice()`, `gHistoryTree.addEventListener()`, `gSearchBox.addEventListener()`, `gSearchBox.focus()`, `searchHistory()`, `viewButton.getAttribute()`, `viewButton.setAttribute()`, `window.addEventListener()`, `window.top.BookmarksEventHandler.fillInBHTooltip()`, `window.top.document.documentElement.getAttribute()`

## GroupBy()
- 位置: L96-103
- 役割: 履歴サイドバーのグループ化種別を切り替え、利用種別のテレメトリを記録して検索を再実行する。
- 触るとき: 「日付」「サイト」などの表示グループ化の選択肢を増やすとき、またはグループ切り替え時の計測を変えるとき。
- 呼び出し先: `searchHistory()`
- 条件付き依存: `if (groupingType != gHistoryGrouping)` → `Glean.historySidebar.filterType[groupingType].add()`
- 参照: `Glean.historySidebar.filterType`, `gSearchBox.value`

## updateTelemetry()
- 位置: L105-115
- 役割: 検索回数・フィルター回数の累計をテレメトリに送り、開いたリンク数を記録してカウンタを初期化する。
- 触るとき: 履歴サイドバーを閉じるなど区切りのタイミングで利用統計がずれるとき、または送信項目を増やすとき。
- 呼び出し先: `Glean.historySidebar.cumulativeFilterCount.accumulateSingleSample()`, `Glean.historySidebar.cumulativeSearches.accumulateSingleSample()`, `Glean.sidebar.link.history.add()`, `clearCumulativeCounters()`
- 参照: `urlsOpened.length`

## searchHistory()
- 位置: L117-181
- 役割: グループ種別と検索語から Places クエリとソート順を組み立て、履歴ツリーに読み込ませる。
- 触るとき: 検索結果の並びや件数が期待と違うとき、グループ種別ごとの表示形式を変えるとき、隠し履歴を含める条件を見直すとき。
- 呼び出し先: `PlacesUtils.history.getNewQuery()`, `PlacesUtils.history.getNewQueryOptions()`, `gHistoryTree.load()`
- 条件付き依存: `if (gHistoryGrouping == "lastvisited")` → `Glean.historySidebar.lastvisitedTreeQueryTime.start()`
- 条件付き依存: `if (aInput)` → `Glean.sidebar.search.history.add()`
- 条件付き依存: `if (gHistoryGrouping == "lastvisited")` → `Glean.historySidebar.lastvisitedTreeQueryTime.stopAndAccumulate()`
- 参照: `Ci.nsINavHistoryQueryOptions`, `NHQO.RESULTS_AS_DATE_QUERY`, `NHQO.RESULTS_AS_DATE_SITE_QUERY`, `NHQO.RESULTS_AS_SITE_QUERY`, `NHQO.RESULTS_AS_URI`, `NHQO.SORT_BY_DATE_DESCENDING`, `NHQO.SORT_BY_FRECENCY_DESCENDING`, `NHQO.SORT_BY_TITLE_ASCENDING`, `NHQO.SORT_BY_VISITCOUNT_DESCENDING`, `options.includeHidden`, `options.resultType`, `options.sortingMode`, `query.searchTerms`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## clearCumulativeCounters()
- 位置: L183-186
- 役割: 検索回数とフィルター回数の累計カウンタを 0 に戻す。
- 触るとき: テレメトリ送信後や unload 時に累計値が次の区切りへ持ち越されないことを確認するとき。
