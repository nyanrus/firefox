# browser/components/extensions/parent/ext-search.js

source: browser/components/extensions/parent/ext-search.js
source-hash: 61f88ed4f74b458bb7cbbc53cf5303017d186c63
lines: 124

## <module>
- 役割: search WebExtension API の実装。検索エンジン一覧の取得と、検索の読み込みを SearchService と SearchUIUtils に委ねる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getAPI()
- 位置: L21-122
- 役割: search 名前空間のオブジェクト(get, search, query)を組み立てて返す。
- 触るとき: 拡張から見える search API に新しいメソッドを足すときや、検索系 API 呼び出しの入口を辿るとき。

## getTarget()
- 位置: L22-35
- 役割: disposition、tabId、既定の開き方から、結果を開く先の tab と where を決める。
- 触るとき: search.search や search.query で検索結果が現在のタブに開かれるか新規タブに開かれるかがおかしいとき。disposition と tabId の同時指定はエラーになる。
- 条件付き依存: `if (tabId)` → `tabTracker.getTab()`

## get()
- 位置: async L39-70
- 役割: 表示中の検索エンジン一覧と既定エンジンを取得し、名前、既定かどうか、alias、アイコン URL を返す。
- 触るとき: search.get の返す項目を増やすときや、他拡張や blob: のアイコンが拡張側で表示されないとき。blob: と他拡張の moz-extension: の URL は data: URL に変換される。
- 呼び出し先: `ExtensionUtils.isExtensionUrl()`, `Promise.all()`, `SearchService.getDefault()`, `SearchService.getVisibleEngines()`, `engine.getIconURL()`, `favIconUrl.startsWith()`, `visibleEngines.map()`
- 条件付き依存: `if ( favIconUrl && (favIconUrl.startsWith("blob:") || (ExtensionUtils.isExtensionUrl(favIconUrl) && !favIconUrl.startsWith(context.extension.baseURL))) )` → `ExtensionUtils.makeDataURI()`
- 参照: `SearchService.promiseInitialized`, `context.extension.baseURL`, `defaultEngine.name`, `engine.alias`, `engine.name`

## search()
- 位置: async L72-100
- 役割: engine 名が指定されていればそのエンジンを解決し、無ければ既定の NEW_TAB 相当で検索を読み込む。
- 触るとき: search.search に存在しないエンジン名を渡したときのエラーや、エンジン指定の扱いを確認するとき。
- 呼び出し先: `SearchUIUtils.loadSearch()`, `getTarget()`
- 条件付き依存: `if (searchProperties.engine)` → `SearchService.getEngineByName()`
- 参照: `SearchService.promiseInitialized`, `context.principal`, `searchProperties.disposition`, `searchProperties.engine`, `searchProperties.query`, `searchProperties.tabId`, `windowTracker.topWindow`

## query()
- 位置: async L102-119
- 役割: テキストで検索を実行する。既定の開き先は CURRENT_TAB。
- 触るとき: search.query の既定の開き先を変えるときや、検索文字列が SearchUIUtils.loadSearch にどう渡るか確認するとき。
- 呼び出し先: `SearchUIUtils.loadSearch()`, `getTarget()`
- 参照: `SearchService.promiseInitialized`, `context.principal`, `queryProperties.disposition`, `queryProperties.tabId`, `queryProperties.text`, `windowTracker.topWindow`
