# browser/components/urlbar/UrlbarProviderHistoryUrlHeuristic.sys.mjs

source: browser/components/urlbar/UrlbarProviderHistoryUrlHeuristic.sys.mjs
source-hash: 16eae7f62bd1d10b24d136c8819ff4b29abd8dff
lines: 132

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderHistoryUrlHeuristic.type()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderHistoryUrlHeuristic.isActive()
- 位置: async L39-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.fixupInfo.scheme.startsWith()`
- 参照: `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `queryContext.fixupInfo.href.length`, `queryContext.fixupInfo.isSearch`, `queryContext.fixupInfo?.href`

## UrlbarProviderHistoryUrlHeuristic.startQuery()
- 位置: async L59-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getResult()`
- 条件付き依存: `if (result && instance === this.queryInstance)` → `addCallback()`
- 参照: `this.queryInstance`

## UrlbarProviderHistoryUrlHeuristic.#getResult()
- 位置: async L67-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `connection.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `resultSet[0].getResultByName()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.fixupInfo.href`, `resultSet.length`
