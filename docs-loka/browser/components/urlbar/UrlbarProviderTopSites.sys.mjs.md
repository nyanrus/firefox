# browser/components/urlbar/UrlbarProviderTopSites.sys.mjs

source: browser/components/urlbar/UrlbarProviderTopSites.sys.mjs
source-hash: 412fa55be76f1292684d9eb5c4bc1a115ce42b19
lines: 510

## <module>
- 役割: about:newtab のトップサイトを、入力が空のときの候補として出す UrlbarProviderTopSites を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## sameUrlIgnoringRef()
- 位置: L43-52
- 役割: 二つの URL を # 以降を除いて比べ、同じかどうかを返す。どちらかが空なら false を返す。
- 触るとき: 現在のページと候補の URL が同じかを判定する箇所の一致条件を変えるとき見る。
- 呼び出し先: `url1.replace()`, `url2.replace()`

## UrlbarProviderTopSites.constructor()
- 位置: L58-60
- 役割: 基底の UrlbarProvider をそのまま初期化するだけのコンストラクターである。
- 触るとき: プロバイダーに初期状態を持たせるとき、ここに処理を足す。
- 呼び出し先: `super()`

## UrlbarProviderTopSites.PRIORITY()
- 位置: L62-65
- 役割: 優先度を 1 とし、Places の結果より先に出るようにする。
- 触るとき: トップサイトと履歴・ブックマークの前後関係を変えたいとき、この値を見る。

## UrlbarProviderTopSites.type()
- 位置: L70-72
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: トップサイト結果を他の結果種別とどう混ぜるかを変えるとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderTopSites.isActive()
- 位置: async L81-87
- 役割: 入力が空で、ソース制限と検索モードのいずれも掛かっていないときだけ有効にする。
- 触るとき: 入力欄が空のときにトップサイトが出ない、または入力中に出てしまう問題を調べるとき見る。
- 呼び出し先: `queryContext.restrictInSearchMode()`
- 参照: `queryContext.restrictSource`, `queryContext.searchString`

## UrlbarProviderTopSites.getPriority()
- 位置: L94-96
- 役割: 静的な PRIORITY の値を返す。
- 触るとき: 優先度を動的に変える必要が出たとき、ここを書き換える。
- 参照: `UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderTopSites.startQuery()
- 位置: async L105-352
- 役割: トップサイトの設定を確かめたうえで、サイトを取得して絞り込み、URL は開いているタブと照合して切り替え結果に変え、検索サイトは検索モードの結果として追加する。last visit と bookmark の判定もここで行う。
- 触るとき: トップサイトの件数上限(maxRichResults と行数)、スポンサー表示、表示される結果種別(タブ切り替え、履歴、ブックマーク、検索)を変えるとき見る。
- 呼び出し先: `Math.min()`, `Services.prefs.getBoolPref()`, `TOP_SITES_ENABLED_PREFS.every()`, `addCallback()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarSearchUtils.engineForAlias()`, `sites.filter()`, `sites.map()`, `sites.slice()`, `this.logger.error()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.topsites.component.enabled"))` → `lazy.TopSites.getSites()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.topsites.component.enabled")))` → `lazy.AboutNewTab.getTopSites()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("sponsoredTopSites"))` → `sites.filter()`
- 条件付き依存: `if (UrlbarProviderTopSites.topSitesRows === undefined)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `lazy.UrlbarProviderOpenTabs.getOpenTabUrls( queryContext.isPrivate ).forEach()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `lazy.UrlbarProviderOpenTabs.getOpenTabUrls()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `userContextIds.add()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.openpage"))` → `tabUrlsToContextIds.set()`
- 条件付き依存: `if (tabUrlsToContextIds)` → `tabUrlsToContextIds.get()`
- 条件付き依存: `if (tabUrlsToContextIds)` → `site.url.replace()`
- 条件付き依存: `if (tabUserContextIds.size)` → `sameUrlIgnoringRef()`
- 条件付き依存: `if (tabUserContextIds.size)` → `UrlbarUtils.getUserContextData()`
- 条件付き依存: `if (tabUserContextIds.size)` → `addCallback()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("resultExplanationsFeatureGate") && lazy.UrlbarPrefs.get("suggest.history") )` → `this.#fetchLastVisit()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("suggest.bookmark"))` → `lazy.PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if (bookmark)` → `bookmark.dateAdded.getTime()`
- 条件付き依存: `if (!engine && site.url)` → `URL.parse()`
- 条件付き依存: `if (host)` → `lazy.UrlbarSearchUtils.enginesForDomainPrefix()`
- 参照: `URL.parse(site.url)?.hostname`, `UrlbarProviderTopSites.topSitesRows`, `engine.name`, `lazy.TOP_SITES_DEFAULT_ROWS`, `lazy.TOP_SITES_MAX_SITES_PER_ROW`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `link.favicon`, `link.hostname`, `link.isPinned`, `link.label`, `link.lastVisitDate`, `link.searchTopSite`, `link.smallFavicon`, `link.sponsored_position`, `link.title`, `link.type`, `link.url`, `link.url_urlbar`, `payload.bookmarkDateMs`, `payload.isBlockable`, `payload.lastVisit`, `payload.sponsoredClickUrl`, `payload.sponsoredTileId`, `payload.url`, `payload.userContext`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.userContextId`, `site.favicon`, `site.isPinned`, `site.isSponsored`, `site.lastVisitDate`, `site.sponsoredClickUrl`, `site.sponsoredTileId`, `site.sponsored_position`, `site.subtype`, `site.title`, `site.type`, `site.url`, `tabUserContextIds.size`, `this.queryInstance`
- XPCOM: `Services.prefs`

## UrlbarProviderTopSites.onImpression()
- 位置: L360-370
- 役割: 非プライベートウィンドウでスポンサー付きのサイトが表示されたとき、表示位置ごとの impression テレメトリを記録する。
- 触るとき: スポンサー枠のインプレッション計測が欠ける、または位置がずれる問題を調べるとき見る。
- 呼び出し先: `providerVisibleResults.forEach()`
- 条件付き依存: `if (result?.payload.isSponsored)` → `Glean.contextualServicesTopsites.impression[`urlbar_${index}`].add()`
- 参照: `Glean.contextualServicesTopsites.impression`, `queryContext.isPrivate`, `result?.payload.isSponsored`

## UrlbarProviderTopSites.onEngagement()
- 位置: async L379-398
- 役割: ブロック可能な結果について、dismiss では新しいタブページからの除外、remove_history では Places の履歴削除を行い、結果を画面から取り除く。
- 触るとき: 削除操作の挙動を変えるとき、または削除後も表示が残る問題を調べるときに見る。
- 呼び出し先: `controller.removeResult()`, `lazy.NewTabUtils.activityStreamLinks.blockURL()`, `lazy.PlacesUtils.history.remove()`
- 参照: `result.payload.isBlockable`, `result.payload.url`

## UrlbarProviderTopSites.getResultCommands()
- 位置: L404-419
- 役割: ブロック可能な結果に対して、トップサイトからの除外と履歴からの削除の二つのコマンドを返す。
- 触るとき: 結果メニューに出す項目を変えたいときに見る。
- 参照: `result.payload.isBlockable`

## UrlbarProviderTopSites.#fetchLastVisit()
- 位置: async L421-451
- 役割: URL に一致する履歴訪問を、恒久・一時のリダイレクト連鎖をたどって最新の訪問日時(秒)を SQL で求める。
- 触るとき: last visit の表示が古い、または欠ける問題を調べるとき見る。リダイレクトの扱いを変えたいときも SQL を見る。
- 呼び出し先: `db.execute()`, `lazy.PlacesUtils.promiseDBConnection()`, `rows[0]?.getResultByName()`
- 参照: `lazy.PlacesUtils.history.TRANSITIONS.REDIRECT_PERMANENT`, `lazy.PlacesUtils.history.TRANSITIONS.REDIRECT_TEMPORARY`, `new URL(url).href`

## UrlbarProviderTopSites.addTopSitesListener()
- 位置: L471-488
- 役割: 初回だけトップサイトの変更通知と関連 pref の監視を登録し、以後は呼び出し元のリスナーを弱参照で保持する。
- 触るとき: トップサイトの変更を他のコンポーネントに知らせる仕組みを使うとき、または通知が来ない原因を調べるとき見る。
- 呼び出し先: `Cu.getWeakReference()`, `UrlbarProviderTopSites.#topSitesListeners.push()`
- 条件付き依存: `if (!UrlbarProviderTopSites.#topSitesListeners)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.topsites.component.enabled"))` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.topsites.component.enabled")))` → `Services.obs.addObserver()`
- 条件付き依存: `if (!UrlbarProviderTopSites.#topSitesListeners)` → `Services.prefs.addObserver()`
- 参照: `UrlbarProviderTopSites.#callTopSitesListeners`, `UrlbarProviderTopSites.#topSitesListeners`
- XPCOM: `Services.obs` / `Services.prefs`

## UrlbarProviderTopSites.#callTopSitesListeners()
- 位置: L490-501
- 役割: 保持中のリスナーを順に呼び出し、既に GC されたリスナーは一覧から取り除く。
- 触るとき: リスナー通知の順序や GC 後の掃除の挙動を変えるとき見る。
- 呼び出し先: `UrlbarProviderTopSites.#topSitesListeners[i].get()`
- 条件付き依存: `if (!listener)` → `UrlbarProviderTopSites.#topSitesListeners.splice()`
- 条件付き依存: `if (!(!listener))` → `listener()`
- 参照: `UrlbarProviderTopSites.#topSitesListeners`, `UrlbarProviderTopSites.#topSitesListeners.length`
