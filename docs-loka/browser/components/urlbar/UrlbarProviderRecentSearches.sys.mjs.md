# browser/components/urlbar/UrlbarProviderRecentSearches.sys.mjs

source: browser/components/urlbar/UrlbarProviderRecentSearches.sys.mjs
source-hash: 43fb936974e91b999db21263753a6b2bcc634849
lines: 178

## <module>
- 役割: ユーザーが最近行った検索語を、フォーム履歴から空の検索欄の候補として出すプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderRecentSearches.constructor()
- 位置: L34-37
- 役割: プロバイダーを生成し、エンジン変更の通知(TOPIC_ENGINE_MODIFIED)を監視し始める。
- 触るとき: 既定エンジンの変更を検知する仕組みを変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `super()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`
- XPCOM: `Services.obs`

## UrlbarProviderRecentSearches.type()
- 位置: L42-44
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: 最近の検索結果の種別と並び順を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderRecentSearches.isActive()
- 位置: async L46-60
- 役割: 検索バーの SAP では検索語が空なら起動する。それ以外は機能フラグと suggest 設定が有効で、入力が空、検索モードでなく、ソース指定もないときに起動する。
- 触るとき: 最近の検索候補を出す条件(検索バー、設定、ソース指定)を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.isSearchbarSAP`, `queryContext.restrictSource`, `queryContext.searchString`

## UrlbarProviderRecentSearches.getPriority()
- 位置: L68-70
- 役割: 優先度として 1 を返す(トップサイトと同じ)。
- 触るとき: 空の入力での最近の検索とトップサイトの並び順を変えるとき。

## UrlbarProviderRecentSearches.onEngagement()
- 位置: L77-92
- 役割: 削除が選ばれたとき、フォーム履歴からその検索語を消し、結果を一覧から取り除く。
- 触るとき: 最近の検索の削除メニューの挙動を変えるとき。
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.FormHistory.update()`
- 条件付き依存: `if (details.selType == "dismiss")` → `console.error()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `details.selType`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `result.payload.suggestion`

## UrlbarProviderRecentSearches.startQuery()
- 位置: async L101-168
- 役割: フォーム履歴から検索語を読み、期限切れ(既定変更後の経過または有効期限)を除き、新しい順に上限件数まで検索結果として追加する。
- 触るとき: 表示件数の上限、有効期限の計算、既定エンジン変更の扱いを変えるとき。
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.urlFormatter.formatURLPref()`, `addCallback()`, `lazy.FormHistory.search()`, `lazy.UrlbarPrefs.get()`, `results.filter()`, `results.sort()`
- 条件付き依存: `if (queryContext.searchMode?.engineName)` → `lazy.UrlbarSearchUtils.getEngineByName()`
- 条件付き依存: `if (!(queryContext.searchMode?.engineName))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if (!queryContext.isSearchbarSAP)` → `parseInt()`
- 条件付き依存: `if (!queryContext.isSearchbarSAP)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lastDefaultChanged != -1)` → `Math.min()`
- 条件付き依存: `if ( !queryContext.isSearchbarSAP && results.length > lazy.UrlbarPrefs.get("recentsearches.maxResults") )` → `lazy.UrlbarPrefs.get()`
- 参照: `a.lastUsed`, `b.lastUsed`, `engine.name`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.isPrivate`, `queryContext.isSearchbarSAP`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `result.lastUsed`, `result.value`, `results.length`
- XPCOM: `Services.urlFormatter`

## UrlbarProviderRecentSearches.observe()
- 位置: L170-176
- 役割: 既定エンジンが変わったときに、その時刻を lastDefaultChanged として記録する。
- 触るとき: 既定エンジン変更後に最近の検索を切り替える境界を見直すとき。
- 呼び出し先: `Date.now()`, `Date.now().toString()`, `lazy.UrlbarPrefs.set()`
- 参照: `lazy.SearchUtils.MODIFIED_TYPE.DEFAULT`
