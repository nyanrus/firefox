# browser/components/urlbar/UrlbarProviderHistoryUrlHeuristic.sys.mjs

source: browser/components/urlbar/UrlbarProviderHistoryUrlHeuristic.sys.mjs
source-hash: 16eae7f62bd1d10b24d136c8819ff4b29abd8dff
lines: 132

## <module>
- 役割: 入力が http(s) の URL として解釈できるとき、その URL が履歴かブックマークにタイトル付きで存在すればヒューリスティック結果として返すプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderHistoryUrlHeuristic.type()
- 位置: L28-30
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: URL 結果を他のヒューリスティック結果と比べた順序を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderHistoryUrlHeuristic.isActive()
- 位置: async L39-50
- 役割: fixupInfo の href があり、検索ではなく、スキームが http で始まり、長さが MAX_TEXT_LENGTH 以下のときだけ起動する。
- 触るとき: URL 扱いされる入力の条件を変えたり、長い URL で DB を引かないようにする条件を調べるとき。
- 呼び出し先: `queryContext.fixupInfo.scheme.startsWith()`
- 参照: `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `queryContext.fixupInfo.href.length`, `queryContext.fixupInfo.isSearch`, `queryContext.fixupInfo?.href`

## UrlbarProviderHistoryUrlHeuristic.startQuery()
- 位置: async L59-65
- 役割: #getResult で結果を取り、クエリがまだ同じインスタンスなら結果を追加する。
- 触るとき: 非同期の応答が古いクエリで返ったときに結果を捨てる挙動を変えるとき。
- 呼び出し先: `this.#getResult()`
- 条件付き依存: `if (result && instance === this.queryInstance)` → `addCallback()`
- 参照: `this.queryInstance`

## UrlbarProviderHistoryUrlHeuristic.#getResult()
- 位置: async L67-130
- 役割: 入力 URL からプレフィックスを除いた形で moz_places を検索し、最適な 1 件のタイトルを取る。タイトルがなければ null を返す。
- 触るとき: http/https や www の違いを吸収する一致条件、またはタイトルの優先順(履歴優先かブックマーク優先か)を変えるとき。
- 呼び出し先: `connection.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `resultSet[0].getResultByName()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.fixupInfo.href`, `resultSet.length`
