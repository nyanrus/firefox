# browser/components/aiwindow/models/search/SearchProviders.sys.mjs

source: browser/components/aiwindow/models/search/SearchProviders.sys.mjs
source-hash: 045a129f4b1da348ee34a3a339e20d8cdc5908c5
lines: 267

## <module>
- 役割: Web検索の提供元を定義する。基底クラスと、MLPAの検索APIを呼ぶExaSearchProviderを置き、エラーを分類して結果を統一形式にする。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## annotateSearchError()
- 位置: L52-58
- 役割: エラーに分類とHTTPステータスを付けて返す。オブジェクトでない場合はErrorに包む。メッセージは変えない。
- 触るとき: 検索エラーの分類がテレメトリに正しく出ないとき、分類の値を増やすとき。
- 呼び出し先: `String()`
- 参照: `annotated.httpStatus`, `annotated.searchErrorCategory`

## SearchProvider.search()
- 位置: async L85-87
- 役割: 検索の基底クラスの仮の実装で、呼ばれると未実装の例外を投げる。
- 触るとき: 新しい検索の提供元を作るとき、継承先で search を必ず実装する。

## ExaSearchProvider._fetch()
- 位置: L101-101
- 役割: テストで差し替えられるよう、fetchをそのまま包んだ静的な関数。
- 触るとき: 検索のリクエストをテストでモックするとき。
- 呼び出し先: `fetch()`

## ExaSearchProvider.search()
- 位置: async L117-216
- 役割: 空でないクエリを確かめ、検索のエンドポイントと認証トークンを用意して、15秒のタイムアウト付きでPOSTする。非2xxやJSONの解析失敗、タイムアウト、ネットワーク失敗はそれぞれ分類して投げ、成功なら正規化した結果と生の応答を返す。
- 触るとき: 検索が失敗する理由、件数の上限、タイムアウトの長さ、リクエストの形を変えるとき。
- 呼び出し先: `ExaSearchProvider._fetch()`, `ExaSearchProvider._normalizeResults()`, `JSON.stringify()`, `Math.max()`, `Math.min()`, `Number.isInteger()`, `Services.prefs.getStringPref()`, `annotateSearchError()`, `controller.abort()`, `lazy.clearTimeout()`, `lazy.setTimeout()`, `openAIEngine.getFxAccountToken()`, `query.trim()`, `response.json()`
- 条件付き依存: `if (!endpoint)` → `annotateSearchError()`
- 条件付き依存: `if (!token)` → `annotateSearchError()`
- 条件付き依存: `if (err?.name === "AbortError")` → `annotateSearchError()`
- 条件付き依存: `if (!response.ok)` → `response.text()`
- 条件付き依存: `if (!response.ok)` → `annotateSearchError()`
- 条件付き依存: `if (!response.ok)` → `body.slice()`
- 参照: `ExaSearchProvider.MAX_RESULTS`, `SEARCH_ERROR_CATEGORY.CONFIG`, `SEARCH_ERROR_CATEGORY.HTTP`, `SEARCH_ERROR_CATEGORY.NETWORK`, `SEARCH_ERROR_CATEGORY.TIMEOUT`, `controller.signal`, `err?.name`, `options.maxResults`, `response.ok`, `response.status`, `response.statusText`
- XPCOM: `Services.prefs`

## ExaSearchProvider._normalizeResults()
- 位置: L228-248
- 役割: 応答のresults配列から、URLが文字列の項目だけを取り出し、タイトル、URL、スニペット、公開日(あれば)を持つ形に整える。
- 触るとき: 検索結果の項目が表示で欠けるとき、取り出す項目を増やすとき。
- 呼び出し先: `Array.isArray()`, `ExaSearchProvider._extractSnippet()`, `normalized.push()`
- 参照: `item.publishedDate`, `item.title`, `item.url`, `raw.results`, `raw?.results`, `result.publishedDate`

## ExaSearchProvider._extractSnippet()
- 位置: L258-265
- 役割: 項目のtext、snippet、summaryの順で最初に見つかった文字列を返し、無ければ空文字を返す。
- 触るとき: 検索結果の要約文が空になる原因を調べるとき、フィールド名の候補を増やすとき。
