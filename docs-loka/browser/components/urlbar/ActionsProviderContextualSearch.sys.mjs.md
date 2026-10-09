# browser/components/urlbar/ActionsProviderContextualSearch.sys.mjs

source: browser/components/urlbar/ActionsProviderContextualSearch.sys.mjs
source-hash: f966cb15a14b45aea81cc85c30b3846419a66723
lines: 452

## <module>
- 役割: 表示中のサイトや入力語に合う検索エンジンを urlbar に「○○で検索」として提示し、選ばれたら検索を実行するアクションプロバイダ。
- 呼び出し先: `ChromeUtils.generateQI()`, `XPCOMUtils.declareLazy()`

## ProviderContextualSearch.constructor()
- 位置: L63-71
- 役割: ホストごとのエンジン・訪問記録のキャッシュを用意し、history-cleared を受けるリスナーを登録する。
- 触るとき: 履歴消去後にエンジン候補が古いまま残る問題を調べるとき。
- 呼び出し先: `PlacesObservers.addListener()`, `super()`, `this.handlePlacesEvents.bind()`
- 参照: `this.#placesObserver`

## ProviderContextualSearch.name()
- 位置: L73-75
- 役割: プロバイダ名 "ActionsProviderContextualSearch" を返す。
- 触るとき: 結果の providerName でこのプロバイダを識別する箇所を追うとき。

## ProviderContextualSearch.isActive()
- 位置: L77-84
- 役割: 入力が空でなく、contextualSearch.enabled が有効、検索モード外、suggest.engines が有効のときに有効にする。
- 触るとき: 検索エンジン候補が出ない条件を調べるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.trimmedSearchString`

## ProviderContextualSearch.queryActions()
- 位置: async L86-92
- 役割: matchEngine で候補エンジンを決め、見つかれば結果を 1 件返す。
- 触るとき: 候補の出し方の入口を確かめるとき。
- 呼び出し先: `this.matchEngine()`
- 条件付き依存: `if (this.#resultEngine)` → `this.#createActionResult()`
- 参照: `this.#resultEngine`

## ProviderContextualSearch.onSearchSessionEnd()
- 位置: L94-99
- 役割: ホストごとのエンジンのキャッシュを空にする。
- 触るとき: 検索セッションをまたいで古いエンジン候補が残る問題を調べるとき。
- 呼び出し先: `this.#hostEngines.clear()`

## ProviderContextualSearch.#createActionResult()
- 位置: async L101-117
- 役割: エンジンのアイコン（なければ既定のアイコン）と「○○で検索」の文言を持つ結果を作る。インストール済みエンジンはモードに入る設定と即検索の設定を付ける。
- 触るとき: 候補の文言・アイコン、または検索モードに入るか即検索するかを変えるとき。
- 呼び出し先: `engine?.getIconURL()`
- 参照: `engine.name`, `engine.title`, `engine?.icon`, `this.name`

## ProviderContextualSearch.matchEngine()
- 位置: async L123-194
- 役割: インストール済みの語一致、現在サイトのホストに対応するエンジン（キャッシュ付き）、ページの OpenSearch の順に探し、既定エンジンと同じものは除く。
- 触るとき: どの検索エンジンを候補に出すかの優先順位を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `this.#hostEngines.has()`, `this.#matchTabToSearchEngine()`
- 条件付き依存: `if (host && !this.#hostEngines.has(host))` → `this.#matchInstalledEngine()`
- 条件付き依存: `if (!hostEngine)` → `lazy.SearchService.findContextualSearchEngineByHost()`
- 条件付き依存: `if (host && !this.#hostEngines.has(host))` → `this.#hostEngines.set()`
- 条件付き依存: `if (host)` → `this.#hostEngines.get()`
- 条件付き依存: `if (browser)` → `lazy.OpenSearchManager.getEngines()`
- 参照: `browser.currentURI.host`, `cachedEngine.engine.name`, `defaultEngine.name`, `hostEngine.engine.name`, `lazy.BrowserWindowTracker.getTopWindow()?.gBrowser.selectedBrowser`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `openSearchEngines.length`, `queryContext.isPrivate`

## ProviderContextualSearch.onLocationChange()
- 位置: async L210-219
- 役割: http(s) のページ遷移で、そのホストが訪問済みキャッシュにあれば訪問済みに更新する。
- 触るとき: 訪問記録キャッシュが遷移に追従しない問題を調べるとき。
- 呼び出し先: `this.#visitedEngineDomains.has()`, `uri.scheme.startsWith()`
- 条件付き依存: `if (this.#visitedEngineDomains.has(uri.host))` → `this.#visitedEngineDomains.set()`
- 参照: `uri.host`

## ProviderContextualSearch.#matchInstalledEngine()
- 位置: async L221-229
- 役割: ホストのドメイン接頭辞（全階層一致）でインストール済みエンジンを探し、最初の 1 件を返す。
- 触るとき: サイトに対応するインストール済みエンジンが見つからないとき。
- 呼び出し先: `lazy.UrlbarSearchUtils.enginesForDomainPrefix()`
- 参照: `engines.length`

## ProviderContextualSearch.#matchTabToSearchEngine()
- 位置: async L234-275
- 役割: 表示可能なエンジンの名前とエイリアスを入力と照合し、直近の訪問がある（または確認不要の）ものを選ぶ。既定エンジンを優先する。
- 触るとき: 入力語でエンジン名を出す条件（文字数や訪問確認）を変えるとき。
- 呼び出し先: `a.toLocaleLowerCase()`, `engine.aliases.map()`, `engine.name.toLocaleLowerCase()`, `engineAliases.some()`, `lazy.SearchService.getVisibleEngines()`, `matches()`, `queryContext.trimmedSearchString.toLocaleLowerCase()`, `this.#engineDomainHasRecentVisits()`, `this.#shouldskipRecentVisitCheck()`
- 参照: `defaultEngine.name`, `engine.name`, `engine.searchUrlDomain`, `lazy.SearchService.defaultEngine`

## matches()
- 位置: L243-244
- 役割: 入力が 3 字未満なら前方一致、それ以上なら部分一致で判定する無名関数。
- 触るとき: エンジン名の一致判定を変えるとき。
- 呼び出し先: `name.includes()`, `name.startsWith()`
- 参照: `search.length`

## ProviderContextualSearch.#engineDomainHasRecentVisits()
- 位置: async L281-300
- 役割: エンジンのドメインについて、直近 30 日に訪問があるか、または外部からの参照があるかを moz_places で調べ、結果をキャッシュする。
- 触るとき: 使っていないエンジンが候補に出る、または出ない原因を調べるとき。
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `this.#visitedEngineDomains.has()`, `this.#visitedEngineDomains.set()`
- 条件付き依存: `if (this.#visitedEngineDomains.has(host))` → `this.#visitedEngineDomains.get()`
- 参照: `rows.length`

## ProviderContextualSearch.#shouldskipRecentVisitCheck()
- 位置: async L302-318
- 役割: 入力が 3 字を超えれば訪問確認を省く。それ以外は、履歴が有効で消去されず永続プライベートでもないときだけ確認を省く。
- 触るとき: 訪問確認を省く条件（文字数や履歴設定）を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `query.length`
- XPCOM: `Services.prefs`

## ProviderContextualSearch.onPick()
- 位置: L326-330
- 役割: pickAction を検索元 searchSource 付きで呼び、例外はコンソールに出す。
- 触るとき: 候補を選んだときの入口を確かめるとき。
- 呼び出し先: `this.pickAction()`, `this.pickAction(queryContext, controller, details.searchSource).catch()`
- 参照: `console.error`, `details.searchSource`

## ProviderContextualSearch.pickAction()
- 位置: async L339-377
- 役割: OpenSearch のエンジンは文書の URI から読み直して作り、検索を実行する。プライベートでなく、インストール済みでなく、ポリシーが許すエンジンなら追加のインストール案内を出す。
- 触るとき: 選択後の検索の実行経路やインストール案内の出し方を変えるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `lazy.SearchService.shouldShowInstallPrompt()`, `this.#performSearch()`
- 条件付き依存: `if (type == OPEN_SEARCH_ENGINE)` → `Services.io.newURI()`
- 条件付き依存: `if (type == OPEN_SEARCH_ENGINE)` → `Services.eTLD.getSchemelessSite()`
- 条件付き依存: `if (type == OPEN_SEARCH_ENGINE)` → `lazy.loadAndParseOpenSearchEngine()`
- 条件付き依存: `if ( !queryContext.isPrivate && type != INSTALLED_ENGINE && Services.policies.isAllowed("installSearchEngine") && (await lazy.SearchService.shouldShowInstallProm...)` → `this.#showInstallPrompt()`
- 参照: `engine.uri`, `lazy.OpenSearchEngine`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.searchString`, `this.#resultEngine`, `this.#resultEngine.key`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.policies`

## ProviderContextualSearch.handlePlacesEvents()
- 位置: L379-381
- 役割: 訪問記録キャッシュを空にする。
- 触るとき: 履歴消去後に訪問済みの判定が残る問題を調べるとき。
- 呼び出し先: `this.#visitedEngineDomains.clear()`

## ProviderContextualSearch.#performSearch()
- 位置: async L392-418
- 役割: モード入りの指定があれば入力欄を検索モードにし、そのあと SearchUIUtils で検索を読み込む。
- 触るとき: 検索の実行先（現在のタブか、検索モードへの移行か）を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.SearchUIUtils.loadSearch()`
- 条件付き依存: `if (enterSearchMode)` → `controller.input.search()`
- 参照: `controller.browserWindow`, `engine.aliases`, `engine.name`
- XPCOM: `Services.scriptSecurityManager`

## ProviderContextualSearch.#showInstallPrompt()
- 位置: L420-446
- 役割: エンジンを追加するか断るかを聞く通知バーを表示する。
- 触るとき: エンジン追加の案内の文言やボタンを変えるとき。
- 呼び出し先: `controller.browserWindow.gNotificationBox.appendNotification()`
- 参照: `controller.browserWindow.gNotificationBox.PRIORITY_INFO_LOW`, `engineData.name`

## ProviderContextualSearch.callback()
- 位置: L424-426
- 役割: 通知バーの追加ボタンで SearchService.addSearchEngine を呼ぶ。
- 触るとき: 追加ボタンを押したときの動作を変えるとき。
- 呼び出し先: `lazy.SearchService.addSearchEngine()`

## ProviderContextualSearch.callback()
- 位置: L430-430
- 役割: 通知バーの「いいえ」ボタンで何もしない。
- 触るとき: 断ったときに別の処理（記録など）を足すとき。
