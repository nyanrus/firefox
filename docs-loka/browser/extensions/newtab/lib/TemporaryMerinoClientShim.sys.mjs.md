# browser/extensions/newtab/lib/TemporaryMerinoClientShim.sys.mjs

source: browser/extensions/newtab/lib/TemporaryMerinoClientShim.sys.mjs
source-hash: b6b2062422257a4b21c7a363f7fd886f7584425e
lines: 875

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## logger()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.getLogger()`
- 参照: `this.#name`

## TemporaryMerinoClientShim.SEARCH_PARAMS()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)

## TemporaryMerinoClientShim.constructor()
- 位置: L107-114
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#allowOhttp`, `this.#cachePeriodMs`, `this.#name`

## TemporaryMerinoClientShim.name()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#name`

## TemporaryMerinoClientShim.sessionTimeoutMs()
- 位置: L130-132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionTimeoutMs`

## TemporaryMerinoClientShim.sessionTimeoutMs()
- 位置: L133-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionTimeoutMs`

## TemporaryMerinoClientShim.sessionID()
- 位置: L139-141
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionID`

## TemporaryMerinoClientShim.sequenceNumber()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sequenceNumber`

## TemporaryMerinoClientShim.lastFetchStatus()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastFetchStatus`

## TemporaryMerinoClientShim.fetch()
- 位置: async L187-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.entries()`, `Promise.race()`, `URL.parse()`, `lazy.UrlbarPrefs.get()`, `recordResponse()`, `response.json()`, `suggestions.map()`, `this.#fetch()`, `this.#fetchController?.abort()`, `this.#lazy.logger.debug()`, `this.#lazy.logger.error()`, `this.#nextResponseDeferred?.resolve()`, `this.#sequenceNumber.toString()`, `timer.cancel()`, `url.searchParams.set()`, `url.toString()`
- 条件付き依存: `if (!url)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (clientVariants)` → `url.searchParams.set()`
- 条件付き依存: `if (providers != null)` → `Array.isArray()`
- 条件付き依存: `if (providers != null)` → `providers.join()`
- 条件付き依存: `if (!(providers != null))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (typeof providersString == "string")` → `url.searchParams.set()`
- 条件付き依存: `if (this.#cachePeriodMs && !TemporaryMerinoClientShim._test_disableCache)` → `url.searchParams.sort()`
- 条件付き依存: `if (this.#cachePeriodMs && !TemporaryMerinoClientShim._test_disableCache)` → `url.toString()`
- 条件付き依存: `if (this.#cachePeriodMs && !TemporaryMerinoClientShim._test_disableCache)` → `Date.now()`
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
- 参照: `SEARCH_PARAMS.CLIENT_VARIANTS`, `SEARCH_PARAMS.PROVIDERS`, `SEARCH_PARAMS.QUERY`, `SEARCH_PARAMS.SEQUENCE_NUMBER`, `SEARCH_PARAMS.SESSION_ID`, `TemporaryMerinoClientShim._test_disableCache`, `body?.suggestions?.length`, `controller.signal`, `error.name`, `lazy.SkippableTimer`, `response.status`, `response?.ok`, `response?.status`, `result.elapsedMs`, `result?.response`, `this.#cache`, `this.#cache.dateMs`, `this.#cache.key`, `this.#cache.suggestions`, `this.#cachePeriodMs`, `this.#fetchController`, `this.#lazy.logger`, `this.#nextResponseDeferred`, `this.#sequenceNumber`, `this.#sessionID`, `this.#sessionTimeoutMs`, `this.#sessionTimer`, `this.#timeoutTimer`, `timer.promise`, `uuid.length`
- XPCOM: `Services.uuid`

## callback()
- 位置: L283-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetSession()`

## recordResponse()
- 位置: L299-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lazy.logger.debug()`
- 参照: `this.#lastFetchStatus`

## callback()
- 位置: L310-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordResponse()`, `this.#lazy.logger.debug()`

## TemporaryMerinoClientShim.autoCompleteWeatherLocation()
- 位置: async L451-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fetch()`

## TemporaryMerinoClientShim.fetchWeatherReport()
- 位置: async L496-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fetch()`
- 条件付き依存: `if (!city && !country && !region)` → `lazy.GeolocationUtils.geolocation()`
- 参照: `Services.locale.appLocaleAsBCP47`, `geolocation.city`, `geolocation.country_code`, `geolocation.region`, `geolocation.region_code`, `otherParams.city`, `otherParams.country`, `otherParams.region`
- XPCOM: `Services.locale`

## TemporaryMerinoClientShim.fetchHourlyForecasts()
- 位置: async L580-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `fetch()`, `response.json()`, `this.#lazy.logger.debug()`, `this.#lazy.logger.error()`
- 条件付き依存: `if (!url)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (locationName)` → `url.searchParams.set()`
- 条件付き依存: `if (!city && !country && !region)` → `lazy.GeolocationUtils.geolocation()`
- 条件付き依存: `if (city)` → `url.searchParams.set()`
- 条件付き依存: `if (region)` → `url.searchParams.set()`
- 条件付き依存: `if (country)` → `url.searchParams.set()`
- 条件付き依存: `if (source)` → `url.searchParams.set()`
- 参照: `Services.locale.appLocaleAsBCP47`, `geolocation.city`, `geolocation.country_code`, `geolocation.region`, `geolocation.region_code`
- XPCOM: `Services.locale`

## TemporaryMerinoClientShim.fetchPictureOfTheDay()
- 位置: async L674-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `fetch()`, `response.json()`, `this.#lazy.logger.debug()`, `this.#lazy.logger.error()`
- 条件付き依存: `if (!url)` → `this.#lazy.logger.error()`
- 条件付き依存: `if (source)` → `url.searchParams.set()`
- 条件付き依存: `if (!response.ok)` → `this.#lazy.logger.error()`
- 参照: `response.ok`, `response.status`

## TemporaryMerinoClientShim.resetSession()
- 位置: L712-719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#nextSessionResetDeferred?.resolve()`, `this.#sessionTimer?.cancel()`
- 参照: `this.#nextSessionResetDeferred`, `this.#sequenceNumber`, `this.#sessionID`, `this.#sessionTimer`

## TemporaryMerinoClientShim.cancelTimeoutTimer()
- 位置: L724-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#timeoutTimer?.cancel()`

## TemporaryMerinoClientShim.waitForNextResponse()
- 位置: L736-741
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#nextResponseDeferred)` → `Promise.withResolvers()`
- 参照: `this.#nextResponseDeferred`, `this.#nextResponseDeferred.promise`

## TemporaryMerinoClientShim.waitForNextSessionReset()
- 位置: L749-754
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#nextSessionResetDeferred)` → `Promise.withResolvers()`
- 参照: `this.#nextSessionResetDeferred`, `this.#nextSessionResetDeferred.promise`

## TemporaryMerinoClientShim.#fetch()
- 位置: async L777-817
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

## TemporaryMerinoClientShim._test_sessionTimer()
- 位置: L821-823
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sessionTimer`

## TemporaryMerinoClientShim._test_timeoutTimer()
- 位置: L825-827
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#timeoutTimer`

## TemporaryMerinoClientShim._test_fetchController()
- 位置: L829-831
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#fetchController`
