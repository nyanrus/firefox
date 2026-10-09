# browser/components/urlbar/UrlbarProviderOpenTabs.sys.mjs

source: browser/components/urlbar/UrlbarProviderOpenTabs.sys.mjs
source-hash: ec57e44f3aecf51662164c588d0ecc44a8bfaf87
lines: 390

## <module>
- 役割: 開いているタブを登録・解除し、moz_openpages_temp に保持する。プロバイダー自体は検索せず、Places プロバイダーがその一時テーブルを結合して使う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `addToMemoryTable()`, `addToMemoryTable(url, userContextId, groupId, count).catch()`, `lazy.PlacesUtils.largeCacheDBConnDeferred.promise.then()`, `lazy.UrlbarShared.getLogger()`

## UrlbarProviderOpenTabs.constructor()
- 位置: L40-42
- 役割: プロバイダーを生成する(super のみ)。
- 触るとき: コンストラクタに初期状態を足すときのみ。
- 呼び出し先: `super()`

## UrlbarProviderOpenTabs.type()
- 位置: L47-49
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: 開いているタブ関連の種別を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderOpenTabs.isActive()
- 位置: async L56-60
- 役割: 常に false を返し、このプロバイダー単独では検索しない。
- 触るとき: 開いているタブの候補が出ない原因を調べるとき、このプロバイダーは候補の供給元でないと知っておく。

## UrlbarProviderOpenTabs.getOpenTabUrlsForUserContextId()
- 位置: L76-103
- 役割: 指定のコンテナ(userContextId)に開いている URL を、グループ ID と組にした配列で返す。
- 触るとき: コンテナごとの開いているタブ一覧を取り出す処理を変えるとき。
- 呼び出し先: `Array.from()`, `Number()`, `gOpenTabUrls.get()`, `groupEntries.forEach()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `parseInt()`, `result.add()`, `urls.keys()`

## UrlbarProviderOpenTabs.getOpenTabUrls()
- 位置: L111-140
- 役割: 開いている URL を重複なしで集め、URL ごとに (userContextId, groupId) の集合を返す。プライベートウィンドウ時はプライベート用コンテナだけを見る。
- 触るとき: タブが開いているかの判定に使う URL 集合の作り方を変えるとき。
- 条件付き依存: `if (isInPrivateWindow)` → `UrlbarProviderOpenTabs.getOpenTabUrlsForUserContextId()`
- 条件付き依存: `if (isInPrivateWindow)` → `uniqueUrls.set()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `gOpenTabUrls.forEach()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `groups.forEach()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `urls.keys()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `uniqueUrls.get()`
- 条件付き依存: `if (!userContextAndGroupIds)` → `uniqueUrls.set()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `userContextAndGroupIds.add()`
- 参照: `lazy.UrlbarShared.PRIVATE_USER_CONTEXT_ID`

## UrlbarProviderOpenTabs.getDatabaseRegisteredOpenTabsForTests()
- 位置: async L148-160
- 役割: moz_openpages_temp の全行を読み、テスト用にオブジェクトの配列へ変換して返す。
- 触るとき: 開いているタブの登録状態をテストで確認したいとき。
- 呼び出し先: `conn.execute()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `r.getResultByName()`, `rows.map()`

## UrlbarProviderOpenTabs.registerOpenTab()
- 位置: async L190-231
- 役割: userContextId とグループ ID を正規化してメモリ上の二重マップの件数を増やし、一時テーブルへも反映する。
- 触るとき: タブが開かれたときの登録処理や、コンテナ・タブグループの扱いを変えるとき。
- 呼び出し先: `Number()`, `Number.isInteger()`, `addToMemoryTable()`, `addToMemoryTable(url, userContextId, groupId).catch()`, `contextEntries.get()`, `gOpenTabUrls.get()`, `groupEntries.get()`, `groupEntries.set()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `lazy.logger.info()`, `parseInt()`
- 条件付き依存: `if (!Number.isInteger(userContextId))` → `lazy.logger.error()`
- 条件付き依存: `if (!contextEntries)` → `gOpenTabUrls.set()`
- 条件付き依存: `if (!groupEntries)` → `contextEntries.set()`
- 参照: `console.error`

## UrlbarProviderOpenTabs.unregisterOpenTab()
- 位置: async L241-286
- 役割: メモリ上の件数を 1 減らし、0 になれば URL を外し、一時テーブルからも減算する。未登録の解除はエラーを出して止める。
- 触るとき: タブを閉じたときに候補が残る、または二重に消える問題を調べるとき。
- 呼び出し先: `Number()`, `gOpenTabUrls.get()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `lazy.logger.info()`, `parseInt()`
- 条件付き依存: `if (contextEntries)` → `contextEntries.get()`
- 条件付き依存: `if (groupEntries)` → `groupEntries.get()`
- 条件付き依存: `if (oldCount == 0)` → `console.error()`
- 条件付き依存: `if (oldCount == 1)` → `groupEntries.delete()`
- 条件付き依存: `if (!(oldCount == 1))` → `groupEntries.set()`
- 条件付き依存: `if (groupEntries)` → `removeFromMemoryTable(url, userContextId, groupId).catch()`
- 条件付き依存: `if (groupEntries)` → `removeFromMemoryTable()`
- 参照: `console.error`

## UrlbarProviderOpenTabs.startQuery()
- 位置: async L295-331
- 役割: 一時テーブルの全行を読み、各行を TAB_SWITCH 結果として追加する。クエリが変わったら読み込みを打ち切る。
- 触るとき: タブ切り替え結果の内容(タブグループ、コンテナ情報)を変えるとき。現在はトークンを処理しない暫定実装である点に注意する。
- 呼び出し先: `UrlbarUtils.getUserContextData()`, `addCallback()`, `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `row.getResultByName()`
- 条件付き依存: `if (instance != this.queryInstance)` → `cancel()`
- 参照: `UrlbarProviderOpenTabs.promiseDBPopulated`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `this.queryInstance`

## addToMemoryTable()
- 位置: async L343-362
- 役割: メモリテーブルが初期化済みなら、moz_openpages_temp に URL・コンテナ・グループを挿入し、既にあれば件数を増やす。
- 触るとき: 一時テーブルへの書き込みの排他制御や、挿入時の件数の扱いを変えるとき。
- 呼び出し先: `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.ProvidersManager.runInCriticalSection()`
- 参照: `UrlbarProviderOpenTabs.memoryTableInitialized`

## removeFromMemoryTable()
- 位置: async L372-389
- 役割: 初期化済みなら、moz_openpages_temp の該当行の open_count を 1 減らす。
- 触るとき: タブを閉じたときの一時テーブル更新を調べるとき。行は削除されず件数だけ減る点に注意する。
- 呼び出し先: `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.ProvidersManager.runInCriticalSection()`
- 参照: `UrlbarProviderOpenTabs.memoryTableInitialized`
