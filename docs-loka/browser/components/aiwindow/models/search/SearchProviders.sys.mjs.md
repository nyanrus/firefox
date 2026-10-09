# browser/components/aiwindow/models/search/SearchProviders.sys.mjs

source: browser/components/aiwindow/models/search/SearchProviders.sys.mjs
source-hash: 045a129f4b1da348ee34a3a339e20d8cdc5908c5
lines: 267

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## annotateSearchError()
- 位置: L52-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`
- 参照: `annotated.httpStatus`, `annotated.searchErrorCategory`

## SearchProvider.search()
- 位置: async L85-87
- 役割: (未記入)
- 触るとき: (未記入)

## ExaSearchProvider._fetch()
- 位置: L101-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`

## ExaSearchProvider.search()
- 位置: async L117-216
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `ExaSearchProvider._extractSnippet()`, `normalized.push()`
- 参照: `item.publishedDate`, `item.title`, `item.url`, `raw.results`, `raw?.results`, `result.publishedDate`

## ExaSearchProvider._extractSnippet()
- 位置: L258-265
- 役割: (未記入)
- 触るとき: (未記入)
