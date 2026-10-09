# browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs

source: browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs
source-hash: bfec6e881f1350c84255653442105996cc44b8f0
lines: 714

## <module>
- 役割: AI ウィンドウが閲覧履歴を検索する処理を定義する。意味検索、Places の文字列検索、期間指定の一覧を使い分け、結果を統合して返す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isoToMicroseconds()
- 位置: L23-29
- 役割: ISO 日時文字列を moz_places 形式のマイクロ秒に変換する。空や不正な値は null を返す。
- 触るとき: 期間指定の境界が効かない、または時刻がずれるとき。
- 呼び出し先: `Number.isFinite()`, `new Date(iso).getTime()`

## buildHistoryRow()
- 位置: L53-105
- 役割: SQL の行か Places のノードから、タイトル・URL・最終訪問・訪問回数・関連度・サムネイルを持つ共通形式に変換する。意味検索の行は 1 から距離を引いた値を関連度にする。
- 触るとき: 履歴結果に載せる項目を増やす、または関連度の算出を変えるとき。
- 条件付き依存: `if (!fromNode)` → `row.getResultByName()`
- 条件付き依存: `if (typeof lastVisitRaw === "number")` → `new Date(Math.round(lastVisitRaw / 1000)).toISOString()`
- 条件付き依存: `if (typeof lastVisitRaw === "number")` → `Math.round()`
- 条件付き依存: `if (lastVisitRaw instanceof Date)` → `lastVisitRaw.toISOString()`
- 条件付き依存: `if (!(!fromNode))` → `lazy.PlacesUtils.toDate()`
- 条件付き依存: `if (!(!fromNode))` → `lastVisitDate.toISOString()`
- 参照: `row.accessCount`, `row.frecency`, `row.time`, `row.title`, `row.uri`

## mergeHistoryResultsRRF()
- 位置: L132-195
- 役割: 意味検索と Places 検索の順位を Reciprocal Rank Fusion(k=60)で合算し、URL で重複を除いて順位・新しさ・訪問回数の順に並べ替える。
- 触るとき: 二つの検索結果の混ぜ方や順位の付け方を変えるとき。
- 呼び出し先: `Number.isFinite()`, `byUrl.get()`, `byUrl.has()`, `byUrl.values()`, `entries.slice()`, `entries.slice(0, historyLimit).map()`, `entries.sort()`, `new Date(entry.visitDate).getTime()`
- 条件付き依存: `if (!byUrl.has(row.url))` → `byUrl.set()`
- 参照: `a._rrf`, `a._visitMs`, `a.visitCount`, `b._rrf`, `b._visitMs`, `b.visitCount`, `byUrl.get(row.url)._rrf`, `entry._rrf`, `entry._visitMs`, `entry.title`, `entry.visitCount`, `entry.visitDate`, `keywordRows.length`, `row.title`, `row.url`, `row.visitCount`, `row.visitDate`, `semanticRows.length`

## searchBrowsingHistoryHybrid()
- 位置: async L217-273
- 役割: 意味検索と Places 検索を並列に行い RRF で統合する。結果が上限に満たず一般カテゴリ語なら、ドメイン絞り込みの結果で残りを埋める。
- 触るとき: ハイブリッド検索の取得件数や、カテゴリ語によるドメイン補完の条件を変えるとき。
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
- 役割: 検索語が無いとき、期間内で最終訪問の新しい順に moz_places を取得し、履歴の行に変換する。
- 触るとき: 検索語なしの一覧の並びや件数を変えるとき。
- 呼び出し先: `buildHistoryRow()`, `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `results.push()`, `rows.push()`

## extractVectorFromTensor()
- 位置: L337-373
- 役割: 埋め込みの戻り値(output 付きや入れ子配列)から、先頭のベクトル 1 本を取り出す。空なら例外を投げる。
- 触るとき: 埋め込みモデルの戻り形式が変わって検索が失敗するとき。
- 呼び出し先: `Array.isArray()`, `ArrayBuffer.isView()`
- 条件付き依存: `if (tensor.output)` → `Array.isArray()`
- 条件付き依存: `if (tensor.output)` → `ArrayBuffer.isView()`
- 参照: `tensor.length`, `tensor.output`

## searchBrowsingHistorySemantic()
- 位置: async L393-473
- 役割: 検索語を埋め込み、vec_history で近傍を求めてから距離を再計算し、距離の閾値と期間で絞って返す。候補数に応じて oversample を設定する。
- 触るとき: 意味検索の精度や件数、距離閾値の扱いを変えるとき。
- 呼び出し先: `Math.ceil()`, `Math.max()`, `Math.min()`, `buildHistoryRow()`, `conn.execute()`, `conn.executeCached()`, `extractVectorFromTensor()`, `lazy.PlacesUtils.tensorToSQLBindable()`, `lazy.getPlacesSemanticHistoryManager()`, `rows.push()`, `semanticManager.embedder.embed()`, `semanticManager.embedder.ensureEngine()`, `semanticManager.getConnection()`

## backfillThumbnails()
- 位置: async L485-524
- 役割: サムネイルが無い行について、URL で moz_places の preview_image_url を引いて埋める。失敗しても握りつぶす。
- 触るとき: 履歴グリッドに画像が出ないとき、または画像取得の条件を変えるとき。
- 呼び出し先: `Map.groupBy()`, `console.error()`, `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `result.getResultByName()`, `rows.filter()`, `rowsByUrl.get()`, `rowsByUrl.keys()`
- 参照: `row.thumbnail`, `row.url`, `rowsMissingThumbnail.length`

## searchBrowsingHistoryBasic()
- 位置: async L536-592
- 役割: Places の検索クエリで検索語と期間を指定し、頻度順の URL 一覧を取り出して行に変換する。失敗時は空配列。
- 触るとき: 意味検索が使えない環境での検索結果の出し方を変えるとき。
- 呼び出し先: `buildHistoryRow()`, `console.error()`, `currentHistory.executeQuery()`, `currentHistory.getNewQuery()`, `currentHistory.getNewQueryOptions()`, `root.getChild()`, `rows.push()`
- 参照: `Ci.nsINavHistoryQuery.TIME_RELATIVE_EPOCH`, `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_URI`, `Ci.nsINavHistoryQueryOptions.SORT_BY_FRECENCY_DESCENDING`, `lazy.PlacesUtils.history`, `opts.excludeQueries`, `opts.maxResults`, `opts.queryType`, `opts.resultType`, `opts.sortingMode`, `query.beginTime`, `query.beginTimeReference`, `query.endTime`, `query.endTimeReference`, `query.searchTerms`, `result.root`, `root.childCount`, `root.containerOpen`, `rows.length`
- XPCOM: [`nsINavHistoryQuery`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## searchBrowsingHistory()
- 位置: async L628-713
- 役割: 期間を変換し、検索語が空なら期間一覧、意味検索が使えるならハイブリッド、それ以外は Places 検索で取得する。結果が無ければ案内文を、失敗時はエラーを返す。
- 触るとき: 閲覧履歴ツールの振る舞い(検索の分岐、既定件数、戻り値の message や error)を変えるとき。
- 呼び出し先: `Services.prefs.getFloatPref()`, `backfillThumbnails()`, `console.error()`, `isoToMicroseconds()`, `lazy.getPlacesSemanticHistoryManager()`, `searchTerm?.trim()`, `semanticManager.hasSufficientEntriesForSearching()`
- 条件付き依存: `if (!searchTerm?.trim())` → `searchBrowsingHistoryTimeRange()`
- 条件付き依存: `if (canUseSemantic)` → `searchBrowsingHistoryHybrid()`
- 条件付き依存: `if (!(canUseSemantic))` → `searchBrowsingHistoryBasic()`
- 参照: `error.message`, `rows.length`, `semanticManager.isEnabledForSmartWindow`
- XPCOM: `Services.prefs`
