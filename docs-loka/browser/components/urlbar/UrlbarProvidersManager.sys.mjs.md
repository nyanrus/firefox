# browser/components/urlbar/UrlbarProvidersManager.sys.mjs

source: browser/components/urlbar/UrlbarProvidersManager.sys.mjs
source-hash: bc6837e21126c8ab79847749ead384c782871d5e
lines: 1167

## <module>
- 役割: urlbar の検索で、各プロバイダーの isActive と優先度で問い合わせ先を決め、クエリごとの Query で結果を集めてマクサーに並べさせる ProvidersManager と Query を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## ProvidersManager.constructor()
- 位置: L263-309
- 役割: SAP 名に対応するプロバイダーを登録し、マクサーを読み込んで保持する。
- 触るとき: SAP ごとに使うプロバイダーやマクサーの組合せを変えたいとき、この登録の流れを見る。
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.entries()`, `info.supportedSAPs.includes()`, `localProviderModules.filter()`, `this.registerMuxer()`, `this.registerProvider()`
- 参照: `providerInfo.module`, `providerInfo.name`, `this.muxers`, `this.providers`, `this.providersByNotificationType`, `this.queries`

## ProvidersManager.getInstanceForSap()
- 位置: L326-333
- 役割: SAP 名ごとに一つだけ ProvidersManager を作って再利用する。
- 触るとき: 同じ SAP で別々のマネージャーが作られる問題を調べるとき見る。
- 呼び出し先: `gProvidersManagerPerSap.get()`
- 条件付き依存: `if (!manager)` → `gProvidersManagerPerSap.set()`

## ProvidersManager.registerProvider()
- 位置: L341-371
- 役割: UrlbarProvider のインスタンスと種別を検査して登録し、HEURISTIC は一覧の先頭側に入れ、通知の種類ごとの集合にも追加する。
- 触るとき: プロバイダーの登録順や種別による並びを変えたいとき、または登録時に例外が出る原因を調べるとき見る。
- 呼び出し先: `Object.keys()`, `Object.values()`, `Object.values(lazy.UrlbarShared.PROVIDER_TYPE).includes()`, `lazy.logger.info()`, `this.providers.splice()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `this.providers.findIndex()`
- 条件付き依存: `if (typeof provider[notificationType] === "function")` → `this.providersByNotificationType[notificationType].add()`
- 参照: `lazy.UrlbarProvider`, `lazy.UrlbarShared.PROVIDER_TYPE`, `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`, `p.type`, `provider.name`, `provider.type`, `this.providers.length`, `this.providersByNotificationType`

## ProvidersManager.unregisterProvider()
- 位置: L379-389
- 役割: 名前が一致するプロバイダーを一覧から外し、通知の集合からも削除する。
- 触るとき: プロバイダーを外したあとに通知が届く不具合を調べるとき見る。
- 呼び出し先: `Object.values()`, `Object.values(this.providersByNotificationType).forEach()`, `lazy.logger.info()`, `providers.delete()`, `this.providers.findIndex()`
- 条件付き依存: `if (index != -1)` → `this.providers.splice()`
- 参照: `p.name`, `provider.name`, `this.providersByNotificationType`

## ProvidersManager.getProvider()
- 位置: L399-401
- 役割: 名前に一致するプロバイダーを一覧から探して返す。
- 触るとき: 特定のプロバイダーを名前で参照する箇所を調べるとき見る。
- 呼び出し先: `this.providers.find()`
- 参照: `p.name`

## ProvidersManager.registerMuxer()
- 位置: L409-415
- 役割: UrlbarMuxer のインスタンスを検査し、名前をキーにしてマクサーを登録する。
- 触るとき: 新しいマクサーを追加するとき、または同名のマクサーの扱いを確かめるとき見る。
- 呼び出し先: `lazy.logger.info()`, `this.muxers.set()`
- 参照: `lazy.UrlbarMuxer`, `muxer.name`

## ProvidersManager.unregisterMuxer()
- 位置: L423-427
- 役割: マクサーのオブジェクトか名前を受け取り、そのマクサーを登録から外す。
- 触るとき: マクサーの差し替えや外し方を変えるとき見る。
- 呼び出し先: `lazy.logger.info()`, `this.muxers.delete()`
- 参照: `muxer.name`

## ProvidersManager.startQuery()
- 位置: async L437-524
- 役割: マクサーを選び、providers の絞り込み、キーワードキャッシュ確保、トークン化、ソースの決定を行ってから Query を作り、検索ソースや地域の初期化を待って開始する。
- 触るとき: 検索開始時の準備(トークン化、ソースの決定、キャンセル判定)の順序や、どのプロバイダーを使うかの絞り込みを変えるとき見る。
- 呼び出し先: `lazy.PlacesUtils.keywords.ensureCacheInitialized()`, `lazy.Region.init()`, `lazy.UrlbarSearchUtils.init()`, `lazy.UrlbarTokenizer.tokenize()`, `lazy.logger.debug()`, `lazy.logger.error()`, `lazy.logger.info()`, `query.start()`, `queryContext.providers.includes()`, `this.muxers.get()`, `this.providers.filter()`, `this.queries.set()`, `updateSourcesIfEmpty()`
- 条件付き依存: `if (restrictToken)` → `lazy.UrlbarShared.SEARCH_MODE_RESTRICT.has()`
- 参照: `p.name`, `query.canceled`, `queryContext.canceled`, `queryContext.muxer`, `queryContext.providers`, `queryContext.restrictSource`, `queryContext.restrictToken`, `queryContext.searchString`, `queryContext.sources`, `queryContext.sources.length`, `queryContext.tokens`, `restrictToken.value`, `this.providers`

## ProvidersManager.cancelQuery()
- 位置: L531-549
- 役割: 検索をキャンセルし、Query のキャンセルを呼び、割り込み可能な場合は SQL を中断させて、登録を外す。
- 触るとき: キャンセル後も結果が出る、または SQL が中断されない問題を調べるとき見る。
- 呼び出し先: `lazy.logger.info()`, `query.cancel()`, `this.queries.delete()`, `this.queries.get()`
- 条件付き依存: `if (!ProvidersManager.interruptLevel)` → `lazy.PlacesUtils.promiseLargeCacheDBConnection()`
- 条件付き依存: `if (!ProvidersManager.interruptLevel)` → `db.interrupt()`
- 参照: `ProvidersManager.interruptLevel`, `queryContext.canceled`, `queryContext.searchString`

## ProvidersManager.runInCriticalSection()
- 位置: async L558-565
- 役割: 割り込みレベルを一つ上げてから、渡されたタスクを待ち、終了後に下げる。
- 触るとき: 途中で中断されてはいけない SQL を含むプロバイダー処理を書くとき、この関数で囲む。
- 呼び出し先: `taskFn()`
- 参照: `this.interruptLevel`

## ProvidersManager.notifyEngagementChange()
- 位置: L584-649
- 役割: 表示中の結果をプロバイダーごとに分け、表示通知、選択通知または離脱通知、セッション終了通知をそれぞれ該当するプロバイダーへ送る。
- 触るとき: エンゲージメントやインプレッションを受け取るプロバイダーの振り分けを変えるとき、またはプロバイダーに通知が届かない原因を調べるとき見る。
- 呼び出し先: `["engagement", "abandonment"].includes()`, `results.push()`, `visibleResults.forEach()`, `visibleResultsByProviderName.get()`
- 条件付き依存: `if (!["engagement", "abandonment"].includes(state))` → `lazy.logger.error()`
- 条件付き依存: `if (!results)` → `visibleResultsByProviderName.set()`
- 条件付き依存: `if (!details.isSessionOngoing)` → `this.#notifyImpression()`
- 条件付き依存: `if (details.result)` → `this.#notifyEngagement()`
- 条件付き依存: `if (!(state === "engagement"))` → `this.#notifyAbandonment()`
- 条件付き依存: `if (!details.isSessionOngoing)` → `this.#notifySearchSessionEnd()`
- 参照: `controller.view`, `controller.view.visibleResults`, `details.isSessionOngoing`, `details.result`, `result.providerName`, `this.providersByNotificationType.onAbandonment`, `this.providersByNotificationType.onEngagement`, `this.providersByNotificationType.onImpression`, `this.providersByNotificationType.onSearchSessionEnd`

## ProvidersManager.#notifyEngagement()
- 位置: L651-659
- 役割: 選ばれた結果の提供元のプロバイダーに onEngagement を送り、コントローラーにも通知する。
- 触るとき: 選択時の通知先を変えるとき見る。
- 条件付き依存: `if (details.result.providerName == provider.name)` → `provider.tryMethod()`
- 条件付き依存: `if (details.result.providerName == provider.name)` → `controller.notify()`
- 参照: `details.result.providerName`, `lazy.UrlbarShared.NOTIFICATIONS.PROVIDER_ENGAGEMENT`, `provider.name`

## ProvidersManager.#notifyImpression()
- 位置: L661-684
- 役割: 表示された結果を持つプロバイダーごとに onImpression を送る。
- 触るとき: インプレッションの通知条件や渡す情報を変えるとき見る。
- 呼び出し先: `visibleResultsByProviderName.get()`
- 条件付き依存: `if (providerVisibleResults.length)` → `provider.tryMethod()`
- 参照: `provider.name`, `providerVisibleResults.length`

## ProvidersManager.#notifyAbandonment()
- 位置: L686-697
- 役割: 表示された結果を持つプロバイダーに onAbandonment を送る。
- 触るとき: 入力を離れた場合の通知先を変えるとき見る。
- 呼び出し先: `visibleResultsByProviderName.has()`
- 条件付き依存: `if (visibleResultsByProviderName.has(provider.name))` → `provider.tryMethod()`
- 参照: `provider.name`

## ProvidersManager.#notifySearchSessionEnd()
- 位置: L699-713
- 役割: 全てのプロバイダーに onSearchSessionEnd を送る。
- 触るとき: 検索セッション終了時に、プロバイダーの後始末を追加するとき見る。
- 呼び出し先: `provider.tryMethod()`

## Query.constructor()
- 位置: L735-752
- 役割: クエリの文脈を初期化し、結果の一覧、マクサー、コントローラー、プロバイダーを保持し、許可されたソースの写しを作る。
- 触るとき: クエリごとの状態の初期値を変えたいとき見る。
- 呼び出し先: `queryContext.sources.slice()`, `this.context.deferUserSelectionProviders.clear()`, `this.context.pendingHeuristicProviders.clear()`
- 参照: `this.acceptableSources`, `this.canceled`, `this.context`, `this.context.results`, `this.controller`, `this.muxer`, `this.providers`, `this.started`, `this.unsortedResults`

## Query.start()
- 位置: async L757-887
- 役割: isActive を全プロバイダーに問い合わせ、最も高い優先度のプロバイダーだけを選ぶ。ヒューリスティックは即時、それ以外は delay 設定の後に startQuery を走らせ、全て終わるかキャンセルされるまで待つ。
- 触るとき: どのプロバイダーが実際に問い合わせられるか、また遅延の扱いを変えるとき見る。検索の遅さや候補が出ない原因を調べるときにも使う。
- 呼び出し先: `Promise.all()`, `Promise.race()`, `activePromises.push()`, `activeProviders.map()`, `lazy.logger.error()`, `lazy.logger.info()`, `provider .isActive()`, `provider .isActive(this.context, this.controller) .then()`, `queryPromises.push()`, `startQuery()`, `this._sleepTimer.promise.then()`
- 条件付き依存: `if (isActive && !this.canceled)` → `provider.tryMethod()`
- 条件付き依存: `if (priority >= maxPriority)` → `activeProviders.push()`
- 条件付き依存: `if (provider.deferUserSelection)` → `this.context.deferUserSelectionProviders.add()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `this.context.pendingHeuristicProviders.add()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `queryPromises.push()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `startQuery(provider).finally()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `startQuery()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `this.context.pendingHeuristicProviders.delete()`
- 条件付き依存: `if (!this._sleepTimer)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!this.canceled)` → `this._chunkTimer?.fire()`
- 参照: `activeProviders.length`, `lazy.SkippableTimer`, `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`, `p.name`, `provider.deferUserSelection`, `provider.logger`, `provider.name`, `provider.queryInstance`, `provider.type`, `queryPromises.length`, `this._cancelQueries`, `this._sleepTimer`, `this.canceled`, `this.context`, `this.controller`, `this.providers`, `this.started`

## startQuery()
- 位置: async L817-835
- 役割: 一つのプロバイダーの startQuery を、結果の追加関数付きで呼び、結果が一件も無ければ選択の保留を解く。
- 触るとき: プロバイダーが結果を返さなかった場合の後始末を変えるとき見る。
- 呼び出し先: `provider.logger.debug()`, `provider.tryMethod()`, `this.add()`
- 条件付き依存: `if (!addedResult)` → `this.context.deferUserSelectionProviders.delete()`
- 参照: `provider.name`, `this.context`, `this.context.searchString`, `this.controller`

## Query.cancel()
- 位置: L892-909
- 役割: 一度だけキャンセル状態にし、保留の選択を消し、全プロバイダーの cancelQuery を呼んで、タイマーと待機を終わらせる。
- 触るとき: キャンセル時の後片付けの順序や対象を変えるとき見る。
- 呼び出し先: `lazy.logger.error()`, `provider.logger.debug()`, `provider.tryMethod()`, `this._cancelQueries()`, `this._chunkTimer?.cancel()`, `this._chunkTimer?.cancel().catch()`, `this._sleepTimer?.fire()`, `this._sleepTimer?.fire().catch()`, `this.context.deferUserSelectionProviders.clear()`
- 参照: `provider.queryInstance`, `this.canceled`, `this.context`, `this.context.searchString`, `this.providers`

## Query.add()
- 位置: L917-1010
- 役割: プロバイダーの結果を検査して、対象外のソースや検索モードでの不要なヒューリスティック、javascript: の URL を除く。残った結果に ID と提供元を付け、表示用のデータと SERP 判定を行い、一覧に加えて通知を予約する。
- 触るとき: 結果を絞る条件、表示用データの前計算、javascript: URL の除外を変えるときに見る。結果が出ない原因が ここでの除外にあるかを確かめるとき重要である。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `provider.tryMethod()`, `result.payload.url.startsWith()`, `this._notifyResultsFromProvider()`, `this.acceptableSources.includes()`, `this.context.pendingHeuristicProviders.delete()`, `this.context.searchString.startsWith()`, `this.unsortedResults.push()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.DYNAMIC)` → `provider.getViewTemplate()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.DYNAMIC)` → `provider.getViewUpdate()`
- 条件付き依存: `if (result.payload.url)` → `lazy.UrlbarSearchUtils.resultIsSERP()`
- 参照: `lazy.UrlbarProvider`, `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `lazy.UrlbarShared.RESULT_TYPE.KEYWORD`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `provider.name`, `provider.type`, `result.autofill`, `result.commands`, `result.heuristic`, `result.id`, `result.isSERP`, `result.payload.url`, `result.payload.viewTemplate`, `result.payload.viewUpdate`, `result.providerName`, `result.providerType`, `result.source`, `result.type`, `this.canceled`, `this.context.isPrivate`, `this.context.searchMode`, `this.context.searchMode.engineName`, `this.context.trimmedSearchString`, `this.controller`

## Query._notifyResultsFromProvider()
- 位置: L1012-1034
- 役割: 結果を 16ms 単位のチャンクにまとめて通知するタイマーを作り、ヒューリスティックの結果が揃ったら即時に通知する。
- 触るとき: 結果の表示がちらつく、または遅れる問題を調べるとき、チャンクの時間とヒューリスティックの即時通知の条件を見る。
- 条件付き依存: `if ( !this.context.pendingHeuristicProviders.size && provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC )` → `this._chunkTimer.fire().catch()`
- 条件付き依存: `if ( !this.context.pendingHeuristicProviders.size && provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC )` → `this._chunkTimer.fire()`
- 条件付き依存: `if ( !this.context.pendingHeuristicProviders.size && provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC )` → `lazy.logger.error()`
- 参照: `ProvidersManager.chunkResultsDelayMs`, `lazy.SkippableTimer`, `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`, `provider.logger`, `provider.type`, `this._chunkTimer`, `this._chunkTimer.done`, `this.context.pendingHeuristicProviders.size`

## callback()
- 位置: L1020-1020
- 役割: チャンクタイマーの満了時に、結果の通知を行う。
- 触るとき: チャンク通知の内容を変えるとき見る。
- 呼び出し先: `this._notifyResults()`

## Query._notifyResults()
- 位置: L1036-1055
- 役割: マクサーで並べ替え、結果が空なら通知せず、先頭の結果が変わったかを記録してからコントローラーへ渡す。
- 触るとき: 先頭の結果の変化を判定する条件を変えるとき、または結果の通知条件を確かめるとき見る。
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `this.muxer.sort()`
- 条件付き依存: `if (this.controller)` → `this.controller.receiveResults()`
- 参照: `this.context`, `this.context.firstResult`, `this.context.firstResultChanged`, `this.context.results`, `this.context.results.length`, `this.controller`, `this.unsortedResults`

## Query.getProvider()
- 位置: L1065-1067
- 役割: このクエリの中で、名前に一致するプロバイダーを返す。
- 触るとき: クエリ内のプロバイダーを参照する箇所を調べるとき見る。
- 呼び出し先: `this.providers.find()`
- 参照: `p.name`

## updateSourcesIfEmpty()
- 位置: L1077-1166
- 役割: ソースが未指定なら、設定と制限トークンから検索ソースの一覧を決め、使われた制限トークンを返す。タイトルと URL の制限はソースに影響しない。
- 触るとき: どの検索ソースを有効にするか、制限トークンごとの扱いを変えるとき見る。履歴やブックマークが検索に出ない原因を調べるときも見る。
- 呼び出し先: `Object.values()`, `context.tokens.find()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_BOOKMARK || restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG || (!restrictTokenTy...)` → `acceptedSources.push()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY || (!restrictTokenType && lazy.UrlbarPrefs.get("suggest.history")) )` → `acceptedSources.push()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH || !restrictTokenType )` → `acceptedSources.push()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_OPENPAGE || (!restrictTokenType && lazy.UrlbarPrefs.get("suggest.openpage")) )` → `acceptedSources.push()`
- 条件付き依存: `if (!context.isPrivate && !restrictTokenType)` → `acceptedSources.push()`
- 条件付き依存: `if (!restrictTokenType)` → `acceptedSources.push()`
- 参照: `context.isPrivate`, `context.sapName`, `context.sources`, `context.sources.length`, `lazy.UrlbarShared.RESULT_SOURCE`, `lazy.UrlbarShared.RESULT_SOURCE.ADDON`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_NETWORK`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_ACTION`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_BOOKMARK`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_OPENPAGE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_URL`, `restrictToken.type`, `t.type`
