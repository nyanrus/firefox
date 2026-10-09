# browser/components/urlbar/UrlbarProviderHeuristicFallback.sys.mjs

source: browser/components/urlbar/UrlbarProviderHeuristicFallback.sys.mjs
source-hash: be9c68d0683c33214e4297cbb5cf189dedfac7a5
lines: 348

## <module>
- 役割: 入力を URL として開くか、既定(または指定)の検索エンジンで検索するかを決める、最終的なフォールバックのヒューリスティック結果を出すプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderHeuristicFallback.constructor()
- 位置: L30-32
- 役割: プロバイダーを生成する(super のみ)。
- 触るとき: コンストラクタに初期状態を足すときのみ。
- 呼び出し先: `super()`

## UrlbarProviderHeuristicFallback.type()
- 位置: L37-39
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: フォールバック結果を他のヒューリスティック結果と並べる順序を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderHeuristicFallback.isActive()
- 位置: async L48-50
- 役割: 検索文字列が空でなければ常に起動する。
- 触るとき: 空でない入力では必ずフォールバックを出すという前提を変えるとき。
- 参照: `queryContext.searchString.length`

## UrlbarProviderHeuristicFallback.getPriority()
- 位置: L57-59
- 役割: 優先度として 0 を返す。
- 触るとき: フォールバック結果の優先度を調整したいとき。

## UrlbarProviderHeuristicFallback.startQuery()
- 位置: async L68-125
- 役割: URL 判定(matchUnknownUrl)に当たればそれを出し、キーワード有効時にオリジンやメールらしい入力なら検索結果も併記する。外れれば検索モードのキーワード結果、最後に既定エンジンの検索結果を出す。
- 触るとき: URL 候補と検索候補をどの順で、どの条件で併記するかを変えるとき。
- 呼び出し先: `this._searchModeKeywordResult()`
- 条件付き依存: `if (queryContext.navigationEnabled)` → `UrlbarProviderHeuristicFallback.matchUnknownUrl()`
- 条件付き依存: `if (result)` → `addCallback()`
- 条件付き依存: `if (result)` → `URL.canParse()`
- 条件付き依存: `if (!URL.canParse(str))` → `lazy.UrlUtils.looksLikeOrigin()`
- 条件付き依存: `if (!URL.canParse(str))` → `lazy.UrlUtils.REGEXP_COMMON_EMAIL.test()`
- 条件付き依存: `if ( queryContext.keywordEnabled && (lazy.UrlUtils.looksLikeOrigin(str, { noIp: true, noPort: true, }) || lazy.UrlUtils.REGEXP_COMMON_EMAIL.test(str)) )` → `this._engineSearchResult()`
- 条件付き依存: `if ( queryContext.keywordEnabled && (lazy.UrlUtils.looksLikeOrigin(str, { noIp: true, noPort: true, }) || lazy.UrlUtils.REGEXP_COMMON_EMAIL.test(str)) )` → `addCallback()`
- 条件付き依存: `if ( queryContext.keywordEnabled || queryContext.restrictSource == lazy.UrlbarShared.RESULT_SOURCE.SEARCH || queryContext.searchMode )` → `this._engineSearchResult()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.keywordEnabled`, `queryContext.navigationEnabled`, `queryContext.restrictSource`, `queryContext.searchMode`, `queryContext.searchString`, `this.queryInstance`

## UrlbarProviderHeuristicFallback.matchUnknownUrl()
- 位置: L127-242
- 役割: 入力を URL に整形できるかを判定し、ホストの無い URL や検索モード時などを除いて URL 結果(表示用タイトル、ファビコン推定付き)を作る。
- 触るとき: 入力が URL として扱われる条件(検索モード、restrictToken、fixupError、ホスト有無)を変えるとき。
- 呼び出し先: `UrlbarUtils.stripURLPrefix()`, `["http:", "https:", "ftp:", "chrome:"].includes()`, `lazy.UrlbarShared.SEARCH_MODE_RESTRICT.has()`, `lazy.UrlbarShared.prepareUrlForDisplay()`, `lazy.UrlbarShared.unEscapeURIForUI()`, `searchUrl.endsWith()`, `uri.toString()`
- 条件付き依存: `if (hostExpected && (searchUrl.endsWith("/") || uri.pathname.length > 1))` → `uri.toString().lastIndexOf()`
- 条件付き依存: `if (hostExpected && (searchUrl.endsWith("/") || uri.pathname.length > 1))` → `uri.toString()`
- 条件付き依存: `if (hostExpected && (searchUrl.endsWith("/") || uri.pathname.length > 1))` → `uri.toString().slice()`
- 参照: `Cr.NS_ERROR_MALFORMED_URI`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.fixupError`, `queryContext.fixupInfo.href`, `queryContext.fixupInfo?.href`, `queryContext.fixupInfo?.isSearch`, `queryContext.keywordEnabled`, `queryContext.navigationInSearchModeEnabled`, `queryContext.restrictSource`, `queryContext.restrictToken?.value`, `queryContext.searchMode`, `queryContext.searchMode.engineName`, `queryContext.searchString`, `queryContext.trimmedSearchString`, `uri.host`, `uri.pathname`, `uri.pathname.length`, `uri.protocol`

## UrlbarProviderHeuristicFallback._searchModeKeywordResult()
- 位置: async L244-299
- 役割: 先頭トークンが検索モード指定語で、後ろに空白が続くときだけ、検索モードへの入り口となる結果を返す。
- 触るとき: 検索モード(@history などの指定語)に入る条件や、検索ソース限定時の挙動を調べるとき。
- 呼び出し先: `UrlbarUtils.substringAfter()`, `lazy.UrlUtils.REGEXP_SPACES_START.test()`, `lazy.UrlbarShared.SEARCH_MODE_RESTRICT.has()`, `query.trimStart()`
- 条件付き依存: `if (queryContext.restrictSource == lazy.UrlbarShared.RESULT_SOURCE.SEARCH)` → `this._engineSearchResult()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.restrictSource`, `queryContext.sapName`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens.length`, `queryContext.tokens[0].value`

## UrlbarProviderHeuristicFallback._engineSearchResult()
- 位置: async L301-346
- 役割: 検索モードのエンジン、なければ既定エンジンで検索結果を作る。先頭の検索制限文字を取り除いて検索語にする。
- 触るとき: 検索結果の検索語の切り出し方や、どのエンジンを使うかを変えるとき。
- 条件付き依存: `if (queryContext.searchMode?.engineName)` → `lazy.UrlbarSearchUtils.getEngineByName()`
- 条件付き依存: `if (!(queryContext.searchMode?.engineName))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if ( queryContext.tokens[0] && queryContext.tokens[0].value === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH )` → `UrlbarUtils.substringAfter( query, queryContext.tokens[0].value ).trim()`
- 条件付き依存: `if ( queryContext.tokens[0] && queryContext.tokens[0].value === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH )` → `UrlbarUtils.substringAfter()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.ICON.SEARCH_GLASS`, `lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.isPrivate`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0].value`
