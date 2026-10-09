# browser/components/urlbar/MerinoClient.sys.mjs

source: browser/components/urlbar/MerinoClient.sys.mjs
source-hash: a2a49093bed73d9cc9b831b58a1d6d76c4376acb
lines: 812

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## logger()
- 位置: L50-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.getLogger()`
- 参照: `this.#name`

## MerinoClient.SEARCH_PARAMS()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)

## MerinoClient.constructor()
- 位置: L100-107
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#allowOhttp`, `this.#cachePeriodMs`, `this.#name`

## MerinoClient.name()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#name`

## MerinoClient.sessionTimeoutMs()
- 位置: L123-125
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionTimeoutMs`

## MerinoClient.sessionTimeoutMs()
- 位置: L126-128
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionTimeoutMs`

## MerinoClient.sessionID()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionID`

## MerinoClient.sequenceNumber()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sequenceNumber`

## MerinoClient.lastFetchStatus()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastFetchStatus`

## MerinoClient.fetch()
- 位置: async L176-415
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetSession()`

## recordResponse()
- 位置: L287-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lazy.logger.debug()`
- 参照: `this.#lastFetchStatus`

## callback()
- 位置: L298-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordResponse()`, `this.#lazy.logger.debug()`

## MerinoClient.autoCompleteWeatherLocation()
- 位置: async L436-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fetch()`

## MerinoClient.fetchWeatherReport()
- 位置: async L481-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.fetch()`
- 条件付き依存: `if (!locationName)` → `this.#resolveGeoParams()`
- 条件付き依存: `if (!locationName)` → `Object.assign()`

## MerinoClient.fetchHourlyForecasts()
- 位置: async L551-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `URL.parse()`, `fetch()`, `lazy.UrlbarPrefs.get()`, `response.json()`, `this.#lazy.logger.debug()`, `this.#lazy.logger.error()`, `this.#resolveGeoParams()`, `url.searchParams.set()`
- 条件付き依存: `if (!url)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (locationName)` → `url.searchParams.set()`
- 条件付き依存: `if (source)` → `url.searchParams.set()`

## MerinoClient.#resolveGeoParams()
- 位置: async L626-648
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!city && !country && !region)` → `lazy.GeolocationUtils.geolocation()`
- 参照: `geolocation.city`, `geolocation.country_code`, `geolocation.region`, `geolocation.region_code`, `params.city`, `params.country`, `params.region`

## MerinoClient.resetSession()
- 位置: L653-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#nextSessionResetDeferred?.resolve()`, `this.#sessionTimer?.cancel()`
- 参照: `this.#nextSessionResetDeferred`, `this.#sequenceNumber`, `this.#sessionID`, `this.#sessionTimer`

## MerinoClient.cancelTimeoutTimer()
- 位置: L665-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#timeoutTimer?.cancel()`

## MerinoClient.waitForNextResponse()
- 位置: L677-682
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#nextResponseDeferred)` → `Promise.withResolvers()`
- 参照: `this.#nextResponseDeferred`, `this.#nextResponseDeferred.promise`

## MerinoClient.waitForNextSessionReset()
- 位置: L690-695
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#nextSessionResetDeferred)` → `Promise.withResolvers()`
- 参照: `this.#nextSessionResetDeferred`, `this.#nextSessionResetDeferred.promise`

## MerinoClient.#fetch()
- 位置: async L716-754
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionTimer`

## MerinoClient._test_timeoutTimer()
- 位置: L762-764
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#timeoutTimer`

## MerinoClient._test_fetchController()
- 位置: L766-768
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#fetchController`
