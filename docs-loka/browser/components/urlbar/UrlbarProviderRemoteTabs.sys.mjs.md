# browser/components/urlbar/UrlbarProviderRemoteTabs.sys.mjs

source: browser/components/urlbar/UrlbarProviderRemoteTabs.sys.mjs
source-hash: ec3635f3c0d4c34447548959db3e7f3bbf1888b5
lines: 245

## <module>
- 役割: Sync の他端末で開いているタブを URL バーの結果として出す UrlbarProviderRemoteTabs と、その一覧をキャッシュする _cache を定義する。
- 呼び出し先: `Cc["@mozilla.org/weave/service;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## escapeRegExp()
- 位置: L51-53
- 役割: 文字列中の正規表現の特殊文字を backslash でエスケープし、部分一致検索用の RegExp に安全に渡せるようにする。
- 触るとき: 検索語をそのまま RegExp に入れて絞り込む処理を追加・変更するとき、特殊文字で誤マッチや例外が出ないか確かめる場面で見る。
- 呼び出し先: `string.replace()`

## _cache.constructor()
- 位置: L62-71
- 役割: Sync のタブエンジン同期完了とアカウントのリセット(start-over)を監視するオブザーバーを登録する。
- 触るとき: Sync 関連の通知をキャッシュ無効化の契機として増やす・減らすとき、この登録箇所を見る。
- 呼び出し先: `Services.obs.addObserver()`, `this.observe.bind()`
- XPCOM: `Services.obs`

## _cache.#buildItems()
- 位置: async L76-93
- 役割: Sync が ready なら端末一覧を最近使った順に並べ、各端末のタブを {tab, client} の配列に平坦化してキャッシュに保存する。
- 触るとき: リモートタブ候補の並び順や対象データ(どの端末・タブを含めるか)を変えたいとき、ここを変更する。Sync 未初期化時は空配列になる点に注意する。
- 条件付き依存: `if (lazy.weaveXPCService.ready)` → `lazy.SyncedTabs.getTabClients()`
- 条件付き依存: `if (lazy.weaveXPCService.ready)` → `lazy.SyncedTabs.sortTabClientsByLastUsed()`
- 条件付き依存: `if (lazy.weaveXPCService.ready)` → `tabsData.push()`
- 参照: `client.tabs`, `lazy.weaveXPCService.ready`, `this.#tabsData`

## _cache.observe()
- 位置: L95-112
- 役割: tabs エンジンの同期完了時と start-over 時にキャッシュを null に戻し、次回取得で作り直させる。
- 触るとき: 別ユーザーのタブが混ざる、同期後も古いタブが出るといった不整合を調べるとき、無効化のタイミングを確かめる。
- 参照: `this.#tabsData`

## _cache.get()
- 位置: async L121-128
- 役割: シングルトンのキャッシュを返し、無効なら #buildItems() で作り直してから返す。
- 触るとき: リモートタブのデータ取得が毎回重い、または古いままになるといった性能・鮮度の問題を調べるとき見る。
- 条件付き依存: `if (!_cache.#instance.#tabsData)` → `_cache.#instance.#buildItems()`
- 参照: `_cache.#instance`, `_cache.#instance.#tabsData`

## UrlbarProviderRemoteTabs.constructor()
- 位置: L135-137
- 役割: 基底の UrlbarProvider をそのまま初期化するだけの空のコンストラクターである。
- 触るとき: コンストラクターで初期状態を持たせる必要が出たとき、ここに追記する。
- 呼び出し先: `super()`

## UrlbarProviderRemoteTabs.type()
- 位置: L142-144
- 役割: プロバイダー種別として NETWORK を返し、結果のグルーピングや muxer での扱いを決める。
- 触るとき: リモートタブ結果を他のローカル結果と同じ枠で扱うか変えたいとき、この種別を見直す。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.NETWORK`

## UrlbarProviderRemoteTabs.isActive()
- 位置: async L153-162
- 役割: 同期ユーザー名、suggest.remotetab 設定、TABS ソース指定、Sync の ready と enabled を全て満たすときだけ検索を開始させる。
- 触るとき: リモートタブが出ない原因を調べるとき、どの条件で無効化されるかを確かめる。新しい条件を足すときもここに追加する。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.sources.includes()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.syncUsernamePref`, `lazy.weaveXPCService`, `lazy.weaveXPCService.enabled`, `lazy.weaveXPCService.ready`

## UrlbarProviderRemoteTabs.startQuery()
- 位置: async L171-243
- 役割: キャッシュの端末タブを検索語で絞り込み、72時間以内のタブを先に、古いタブを後に、maxResults まで結果として追加する。
- 触るとき: リモートタブの絞り込み条件、表示する件数、最近のタブを優先する規則を変えるとき、この関数を変更する。結果の payload(url、title、device、lastUsed など)を変えるときも見る。
- 呼び出し先: `_cache.get()`, `addCallback()`, `escapeRegExp()`, `queryContext.tokens.map()`, `queryContext.tokens.map(t => t.value).join()`, `re.test()`, `staleTabs.shift()`
- 条件付き依存: `if ( !searchString || searchString == lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE || re.test(tab.url) || (tab.title && re.test(tab.title)) )` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if ( !searchString || searchString == lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE || re.test(tab.url) || (tab.title && re.test(tab.title)) )` → `Date.now()`
- 条件付き依存: `if ( tab.lastUsed <= (Date.now() - RECENT_REMOTE_TAB_THRESHOLD_MS) / 1000 )` → `staleTabs.push()`
- 条件付き依存: `if (!( tab.lastUsed <= (Date.now() - RECENT_REMOTE_TAB_THRESHOLD_MS) / 1000 ))` → `addCallback()`
- 参照: `client.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `lazy.showRemoteIconsPref`, `queryContext.maxResults`, `staleTabs.length`, `t.value`, `tab.lastUsed`, `tab.title`, `tab.url`, `this.queryInstance`
