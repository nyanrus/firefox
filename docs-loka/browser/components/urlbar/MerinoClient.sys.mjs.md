# browser/components/urlbar/MerinoClient.sys.mjs

source: browser/components/urlbar/MerinoClient.sys.mjs
source-hash: a2a49093bed73d9cc9b831b58a1d6d76c4376acb
lines: 812

## <module>
- 役割: urlbar が Merino（サジェスト・天気など）へ問い合わせる MerinoClient クラスと、セッション ID・キャッシュ・タイムアウトを管理する。
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## logger()
- 位置: L50-51
- 役割: 名前付きの UrlbarShared ロガーを遅延生成して返す。
- 触るとき: MerinoClient のログ出力の接頭辞や有効化を変えるとき。
- 呼び出し先: `lazy.UrlbarShared.getLogger()`
- 参照: `this.#name`

## MerinoClient.SEARCH_PARAMS()
- 位置: L57-59
- 役割: URL パラメータ名の定数（q, providers, client_variants, seq, sid）のコピーを返す。
- 触るとき: Merino のクエリパラメータ名を外部から参照する箇所を追うとき。

## MerinoClient.constructor()
- 位置: L100-107
- 役割: クライアント名、OHTTP 利用の可否、キャッシュ期間（ミリ秒、0 で無効）を受け取って保持する。
- 触るとき: クライアントの生成時オプションの意味を確かめるとき。
- 参照: `this.#allowOhttp`, `this.#cachePeriodMs`, `this.#name`

## MerinoClient.name()
- 位置: L113-115
- 役割: クライアント名を返す getter。
- 触るとき: ログや識別でクライアント名を使うとき。
- 参照: `this.#name`

## MerinoClient.sessionTimeoutMs()
- 位置: L123-125
- 役割: セッションのタイムアウト（既定は 5 分）を返す getter。
- 触るとき: セッション失効までの時間を取得する箇所を追うとき。
- 参照: `this.#sessionTimeoutMs`

## MerinoClient.sessionTimeoutMs()
- 位置: L126-128
- 役割: セッションのタイムアウト値を設定する setter。
- 触るとき: テストや特別な経路でタイムアウトを変えるとき。
- 参照: `this.#sessionTimeoutMs`

## MerinoClient.sessionID()
- 位置: L132-134
- 役割: 現在のセッション ID を返す。セッションがなければ null。
- 触るとき: Merino に送られるセッション ID を確かめるとき。
- 参照: `this.#sessionID`

## MerinoClient.sequenceNumber()
- 位置: L141-143
- 役割: 現在のセッションでの連番を返す。セッションがなければ 0。
- 触るとき: 連番が想定どおり増えているかを調べるとき。
- 参照: `this.#sequenceNumber`

## MerinoClient.lastFetchStatus()
- 位置: L148-150
- 役割: 直近の取得結果の状態を返す。コメントは 4 種だが、実際には no_suggestion も記録される。
- 触るとき: 直近の取得が失敗したか、候補が空だったかを判定するとき。
- 参照: `this.#lastFetchStatus`

## MerinoClient.fetch()
- 位置: async L176-415
- 役割: クエリとプロバイダからURLを組み立て、キャッシュ有効なら期間内の結果を返す。そうでなければセッションと連番を付け、タイムアウト付きで Merino に送り、応答を suggestions にして必要ならキャッシュする。
- 触るとき: Merino の候補が出ない、遅い、重複して呼ばれるといった問題を調べるとき。
- 呼び出し先: `Array.isArray()`, `Object.entries()`, `Promise.race()`, `URL.parse()`, `lazy.UrlbarPrefs.get()`, `recordResponse()`, `response.json()`, `suggestions.map()`, `this.#fetch()`, `this.#fetchController?.abort()`, `this.#lazy.logger.debug()`, `this.#lazy.logger.error()`, `this.#nextResponseDeferred?.resolve()`, `this.#sequenceNumber.toString()`, `timer.cancel()`, `url.searchParams.set()`, `url.toString()`
- 条件付き依存: `if (!url)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (clientVariants)` → `url.searchParams.set()`
- 条件付き依存: `if (providers != null)` → `Array.isArray()`
- 条件付き依存: `if (providers != null)` → `providers.join()`
- 条件付き依存: `if (!(providers != null))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (typeof providersString == "string")` → `url.searchParams.set()`
- 条件付き依存: `if (this.#cachePeriodMs && !MerinoClient._test_disableCache)` → `url.searchParams.sort()`
- 条件付き依存: `if (this.#cachePeriodMs && !MerinoClient._test_disableCache)` → `url.toString()`
- 条件付き依存: `if (this.#cachePeriodMs && !MerinoClient._test_disableCache)` → `Date.now()`
- 条件付き依存: `if ( this.#cache.suggestions && Date.now() < this.#cache.dateMs + this.#cachePeriodMs && this.#cache.key == cacheKey )` → `this.#lazy.logger.debug()`
- 条件付き依存: `if (!this.#sessionID)` → `Services.uuid.generateUUID().toString()`
- 条件付き依存: `if (!this.#sessionID)` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (!this.#sessionID)` → `uuid.substring()`
- 条件付き依存: `if (!this.#sessionID)` → `this.#sessionTimer?.cancel()`
- 条件付き依存: `if (!response?.ok)` → `recordResponse()`
- 条件付き依存: `if (error.name != "AbortError")` → `this.#lazy.logger.error()`
- 条件付き依存: `if (error.name != "AbortError")` → `recordResponse()`
- 条件付き依存: `if (response.status == 204)` → `recordResponse()`
- 条件付き依存: `if (body)` → `this.#lazy.logger.debug()`
- 条件付き依存: `if (!body?.suggestions?.length)` → `recordResponse()`
- 条件付き依存: `if (!Array.isArray(suggestions))` → `this.#lazy.logger.error()`
- 条件付き依存: `if (!Array.isArray(suggestions))` → `recordResponse()`
- 条件付き依存: `if (cacheKey)` → `Date.now()`
- 参照: `MerinoClient._test_disableCache`, `SEARCH_PARAMS.CLIENT_VARIANTS`, `SEARCH_PARAMS.PROVIDERS`, `SEARCH_PARAMS.QUERY`, `SEARCH_PARAMS.SEQUENCE_NUMBER`, `SEARCH_PARAMS.SESSION_ID`, `body?.suggestions?.length`, `controller.signal`, `error.name`, `lazy.SkippableTimer`, `response.status`, `response?.ok`, `response?.status`, `result.elapsedMs`, `result?.response`, `this.#cache`, `this.#cache.dateMs`, `this.#cache.key`, `this.#cache.suggestions`, `this.#cachePeriodMs`, `this.#fetchController`, `this.#lazy.logger`, `this.#nextResponseDeferred`, `this.#sequenceNumber`, `this.#sessionID`, `this.#sessionTimeoutMs`, `this.#sessionTimer`, `this.#timeoutTimer`, `timer.promise`, `uuid.length`
- XPCOM: `Services.uuid`

## callback()
- 位置: L271-271
- 役割: セッションのタイマーが切れたとき resetSession を呼ぶ。
- 触るとき: セッションが期限で新しくなるタイミングを確かめるとき。
- 呼び出し先: `this.resetSession()`

## recordResponse()
- 位置: L287-291
- 役割: 取得結果の状態（success など）を一度だけ記録し、以後の記録を無効にする。
- 触るとき: 取得結果の状態が二重に記録される、または記録されない問題を調べるとき。
- 呼び出し先: `this.#lazy.logger.debug()`
- 参照: `this.#lastFetchStatus`

## callback()
- 位置: L298-302
- 役割: タイムアウトタイマーが切れたとき、状態を timeout として記録する。
- 触るとき: タイムアウト時の扱い（記録や応答の打ち切り）を変えるとき。
- 呼び出し先: `recordResponse()`, `this.#lazy.logger.debug()`

## MerinoClient.autoCompleteWeatherLocation()
- 位置: async L436-447
- 役割: accuweather プロバイダで場所名の候補を取り、先頭の 1 件を返す。
- 触るとき: 天気の場所入力の補完が出ない原因を調べるとき。
- 呼び出し先: `this.fetch()`

## MerinoClient.fetchWeatherReport()
- 位置: async L481-516
- 役割: 場所名があればそれを、なければ都市・地域・国（なければ位置情報）を使い、天気レポートの先頭 1 件を返す。
- 触るとき: 天気カードのデータ取得条件や位置の扱いを変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.fetch()`
- 条件付き依存: `if (!locationName)` → `this.#resolveGeoParams()`
- 条件付き依存: `if (!locationName)` → `Object.assign()`

## MerinoClient.fetchHourlyForecasts()
- 位置: async L551-614
- 役割: 時間別予報の専用エンドポイントに、場所名と位置の情報（常に付与）を付けて直接 fetch し、JSON をそのまま返す。失敗時は null。
- 触るとき: 時間別予報が出ない、または場所が違う問題を調べるとき。
- 呼び出し先: `Object.entries()`, `URL.parse()`, `fetch()`, `lazy.UrlbarPrefs.get()`, `response.json()`, `this.#lazy.logger.debug()`, `this.#lazy.logger.error()`, `this.#resolveGeoParams()`, `url.searchParams.set()`
- 条件付き依存: `if (!url)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (locationName)` → `url.searchParams.set()`
- 条件付き依存: `if (source)` → `url.searchParams.set()`

## MerinoClient.#resolveGeoParams()
- 位置: async L626-648
- 役割: 都市・地域・国が一つも無ければ位置情報から補い、指定のあるものだけを持つオブジェクトを返す。位置情報が取れなければ null。
- 触るとき: 天気の位置の決め方（手入力か自動取得か）を変えるとき。
- 条件付き依存: `if (!city && !country && !region)` → `lazy.GeolocationUtils.geolocation()`
- 参照: `geolocation.city`, `geolocation.country_code`, `geolocation.region`, `geolocation.region_code`, `params.city`, `params.country`, `params.region`

## MerinoClient.resetSession()
- 位置: L653-660
- 役割: セッション ID と連番を消し、タイマーを止め、次のセッション再設定を待つ Promise を解決する。
- 触るとき: セッションをリセットしたあとに古い ID が使われる問題を調べるとき。
- 呼び出し先: `this.#nextSessionResetDeferred?.resolve()`, `this.#sessionTimer?.cancel()`
- 参照: `this.#nextSessionResetDeferred`, `this.#sequenceNumber`, `this.#sessionID`, `this.#sessionTimer`

## MerinoClient.cancelTimeoutTimer()
- 位置: L665-667
- 役割: タイムアウトタイマーを止める。
- 触るとき: 取得の待ちを途中で打ち切る経路を追うとき。
- 呼び出し先: `this.#timeoutTimer?.cancel()`

## MerinoClient.waitForNextResponse()
- 位置: L677-682
- 役割: 次の応答（または通信エラー）が届いたときに解決する Promise を返す。
- 触るとき: 次の応答を待つ呼び出し元の挙動を確かめるとき。
- 条件付き依存: `if (!this.#nextResponseDeferred)` → `Promise.withResolvers()`
- 参照: `this.#nextResponseDeferred`, `this.#nextResponseDeferred.promise`

## MerinoClient.waitForNextSessionReset()
- 位置: L690-695
- 役割: 次のセッション再設定（タイムアウトを含む）で解決する Promise を返す。
- 触るとき: セッション再設定を待つテストや呼び出しを確かめるとき。
- 条件付き依存: `if (!this.#nextSessionResetDeferred)` → `Promise.withResolvers()`
- 参照: `this.#nextSessionResetDeferred`, `this.#nextSessionResetDeferred.promise`

## MerinoClient.#fetch()
- 位置: async L716-754
- 役割: OHTTP が有効で設定があれば OHTTP 経由、なければ通常の fetch で送り、応答時間を状態コード別（OHTTP は接尾辞付き）に Glean へ記録する。
- 触るとき: Merino の通信経路（OHTTP か直接か）や遅延の計測を変えるとき。
- 呼び出し先: `ChromeUtils.now()`, `Glean.urlbarMerino.latencyByResponseStatus[label].accumulateSamples()`, `response.status.toString()`
- 条件付き依存: `if (this.#allowOhttp)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!useOhttp)` → `fetch()`
- 条件付き依存: `if (!(!useOhttp))` → `lazy.ObliviousHTTP.getOHTTPConfig()`
- 条件付き依存: `if (!config)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (!(!useOhttp))` → `this.#lazy.logger.debug()`
- 条件付き依存: `if (!(!useOhttp))` → `lazy.ObliviousHTTP.ohttpRequest()`
- 参照: `Glean.urlbarMerino.latencyByResponseStatus`, `this.#allowOhttp`

## MerinoClient._test_sessionTimer()
- 位置: L758-760
- 役割: テスト用にセッションタイマーを返す。
- 触るとき: テストでセッションタイマーの状態を確かめるとき。
- 参照: `this.#sessionTimer`

## MerinoClient._test_timeoutTimer()
- 位置: L762-764
- 役割: テスト用にタイムアウトタイマーを返す。
- 触るとき: テストで取得のタイムアウトを確かめるとき。
- 参照: `this.#timeoutTimer`

## MerinoClient._test_fetchController()
- 位置: L766-768
- 役割: テスト用に進行中の AbortController を返す。
- 触るとき: テストで中断の挙動を確かめるとき。
- 参照: `this.#fetchController`
