# browser/extensions/newtab/lib/WeatherFeed.sys.mjs

source: browser/extensions/newtab/lib/WeatherFeed.sys.mjs
source-hash: 9d25bfc6e0c9d7e122a1318bb00324b6a550521e
lines: 499

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WeatherFeed.constructor()
- 位置: L44-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.cache`, `this.fetchDelayAfterComingOnlineMs`, `this.fetchIntervalMs`, `this.fetchTimer`, `this.hourlyForecasts`, `this.lastFetchTimeMs`, `this.lastUpdated`, `this.loaded`, `this.locationData`, `this.merino`, `this.retryTimer`, `this.suggestions`, `this.timeoutMS`

## WeatherFeed.resetCache()
- 位置: async L60-64
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.cache)` → `this.cache.set()`
- 参照: `this.cache`

## WeatherFeed.resetWeather()
- 位置: async L66-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetCache()`
- 参照: `this.hourlyForecasts`, `this.lastUpdated`, `this.loaded`, `this.suggestions`

## WeatherFeed.isEnabled()
- 位置: L74-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs`, `values.trainhopConfig?.weather?.enabled`

## WeatherFeed.init()
- 位置: async L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadWeather()`

## WeatherFeed.stopFetching()
- 位置: L89-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearTimeout()`
- 参照: `this.fetchTimer`, `this.hourlyForecasts`, `this.merino`, `this.retryTimer`, `this.suggestions`

## WeatherFeed.fetch()
- 位置: async L103-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._fetchHelper()`, `this.update()`
- 条件付き依存: `if (!this.merino)` → `this.MerinoClient()`
- 条件付き依存: `if (this.suggestions.length || this.hourlyForecasts.length)` → `this.store.getState()`
- 条件付き依存: `if (this.suggestions.length || this.hourlyForecasts.length)` → `this.Date().now()`
- 条件付き依存: `if (this.suggestions.length || this.hourlyForecasts.length)` → `this.Date()`
- 条件付き依存: `if (this.suggestions.length || this.hourlyForecasts.length)` → `this.cache.set()`
- 条件付き依存: `if (hasLocationData && this.suggestions.length)` → `this.cache.set()`
- 参照: `data.city_name`, `this.hourlyForecasts`, `this.hourlyForecasts.length`, `this.lastUpdated`, `this.locationData`, `this.merino`, `this.store.getState().Prefs.values`, `this.suggestions`, `this.suggestions.length`

## WeatherFeed.loadWeather()
- 位置: async L140-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`, `this.cache.get()`
- 条件付き依存: `if ( !weather?.lastUpdated || !(this.Date().now() - weather.lastUpdated < WEATHER_UPDATE_TIME) )` → `this.fetch()`
- 条件付き依存: `if (!this.lastUpdated)` → `this.update()`
- 参照: `locationData?.city`, `this.hourlyForecasts`, `this.lastUpdated`, `this.loaded`, `this.locationData`, `this.suggestions`, `weather.hourlyForecasts`, `weather.lastUpdated`, `weather.suggestions`, `weather?.lastUpdated`

## WeatherFeed.update()
- 位置: L163-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.WEATHER_UPDATE`, `this.hourlyForecasts`, `this.lastUpdated`, `this.locationData`, `this.suggestions`

## WeatherFeed.restartFetchTimer()
- 位置: L177-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearTimeout()`, `this.fetch()`, `this.setTimeout()`
- 参照: `this.fetchIntervalMs`, `this.fetchTimer`, `this.retryTimer`

## WeatherFeed.fetchLocationAutocomplete()
- 位置: async L186-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.merino.autoCompleteWeatherLocation()`, `this.store.getState()`
- 条件付き依存: `if (!this.merino)` → `this.MerinoClient()`
- 条件付き依存: `if (data?.locations.length)` → `this.store.dispatch()`
- 条件付き依存: `if (data?.locations.length)` → `ac.BroadcastToContent()`
- 参照: `at.WEATHER_LOCATION_SUGGESTIONS_UPDATE`, `data.locations`, `data?.locations.length`, `this.merino`, `this.store.getState().Weather.locationSearchString`

## WeatherFeed.onPrefChangedAction()
- 位置: async L210-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fetch()`, `this.isEnabled()`
- 条件付き依存: `if (enabled && !this.loaded)` → `this.loadWeather()`
- 条件付き依存: `if (!enabled && this.loaded)` → `this.resetWeather()`
- 条件付き依存: `if (!this.hourlyForecasts?.length)` → `this.fetch()`
- 参照: `action.data.name`, `this.hourlyForecasts?.length`, `this.loaded`

## WeatherFeed.checkOptInRegion()
- 位置: async L240-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WEATHER_OPTIN_REGIONS.includes()`, `ac.SetPref()`, `this.isEnabled()`, `this.store.dispatch()`
- 参照: `lazy.Region.home`

## WeatherFeed.onAction()
- 位置: async L248-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.SetPref()`, `this._fetchNormalizedLocation()`, `this.checkOptInRegion()`, `this.fetchLocationAutocomplete()`, `this.isEnabled()`, `this.onPrefChangedAction()`, `this.resetWeather()`, `this.store.dispatch()`
- 条件付き依存: `if (this.isEnabled() && !this.loaded)` → `this.init()`
- 条件付き依存: `if (this.isEnabled())` → `this.loadWeather()`
- 条件付き依存: `if (action.data.name === "system.showWeather")` → `this.checkOptInRegion()`
- 条件付き依存: `if (action.data.city)` → `this.cache.set()`
- 条件付き依存: `if (detectedLocation)` → `this.store.dispatch()`
- 条件付き依存: `if (detectedLocation)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (detectedLocation.key)` → `this.store.dispatch()`
- 条件付き依存: `if (detectedLocation.key)` → `ac.SetPref()`
- 参照: `action.data`, `action.data.adminName`, `action.data.city`, `action.data.country`, `action.data.name`, `action.type`, `at.DISCOVERY_STREAM_DEV_SYSTEM_TICK`, `at.INIT`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.UNINIT`, `at.WEATHER_LOCATION_DATA_UPDATE`, `at.WEATHER_LOCATION_SEARCH_UPDATE`, `at.WEATHER_USER_OPT_IN_LOCATION`, `detectedLocation.administrative_area`, `detectedLocation.country`, `detectedLocation.key`, `detectedLocation.localized_name`, `this.loaded`, `this.locationData`

## WeatherFeed._fetchHelper()
- 位置: async L324-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `attempt()`, `this.restartFetchTimer()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## attempt()
- 位置: async L329-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.resolve()`, `attempt()`, `res()`, `this.merino .fetchHourlyForecasts()`, `this.merino.fetchWeatherReport()`, `this.setTimeout()`, `this.store.getState()`
- 条件付き依存: `if (!locationName)` → `this.store.getState()`
- 条件付き依存: `if (!locationName)` → `lazy.GeolocationUtils.geolocation()`
- 参照: `geolocation.city`, `geolocation.country_code`, `geolocation.region`, `geolocation.region_code`, `prefValues.trainhopConfig?.weather?.weatherOptInEnabled`, `this.locationData?.adminName?.id`, `this.locationData?.city`, `this.locationData?.country?.id`, `this.merino`, `this.retryTimer`, `this.store.getState().Prefs`, `values.trainhopConfig?.widgets?.weatherEnabled`, `values.trainhopConfig?.widgets?.weatherForecastEnabled`

## WeatherFeed._fetchNormalizedLocation()
- 位置: async L443-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.GeolocationUtils.geolocation()`, `this.merino.fetch()`
- 条件付き依存: `if (!this.merino)` → `this.MerinoClient()`
- 参照: `geolocation.city`, `geolocation.region`, `locationData?.[0]?.locations`, `this.merino`

## WeatherFeed.prototype.MerinoClient()
- 位置: L484-486
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MerinoClient`

## WeatherFeed.prototype.PersistentCache()
- 位置: L487-489
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## WeatherFeed.prototype.Date()
- 位置: L490-492
- 役割: (未記入)
- 触るとき: (未記入)

## WeatherFeed.prototype.setTimeout()
- 位置: L493-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setTimeout()`

## WeatherFeed.prototype.clearTimeout()
- 位置: L496-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clearTimeout()`
