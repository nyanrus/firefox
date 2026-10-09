# browser/extensions/newtab/lib/StartupCacheInit.sys.mjs

source: browser/extensions/newtab/lib/StartupCacheInit.sys.mjs
source-hash: f81a158e6110a1bfd67d71e1d9780a6c89942964
lines: 204

## <module>
- 役割: (未記入)

## StartupCacheInit.constructor()
- 位置: L29-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.CustomWallpaperUpdateReply`, `this.DiscoveryStreamSpocsUpdateReply`, `this.PrefChangesReply`, `this.TopsitesUpdatedReply`, `this.WeatherUpdateReply`, `this.loaded`

## StartupCacheInit.stateRequestReply()
- 位置: L39-60
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.TopsitesUpdatedReply)` → `this.sendTopsitesUpdatedReply()`
- 条件付き依存: `if (this.DiscoveryStreamSpocsUpdateReply)` → `this.sendDiscoveryStreamSpocsUpdateReply()`
- 条件付き依存: `if (this.WeatherUpdateReply)` → `this.sendWeatherUpdateReply()`
- 条件付き依存: `if (this.CustomWallpaperUpdateReply)` → `this.sendCustomWallpaperUpdateReply()`
- 条件付き依存: `if (this.PrefChangesReply.size > 0)` → `this.sendPrefChangesReply()`
- 参照: `this.CustomWallpaperUpdateReply`, `this.DiscoveryStreamSpocsUpdateReply`, `this.PrefChangesReply.size`, `this.TopsitesUpdatedReply`, `this.WeatherUpdateReply`

## StartupCacheInit.sendTopsitesUpdatedReply()
- 位置: L64-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `at.TOP_SITES_UPDATED`, `this.store.getState().TopSites.rows`

## StartupCacheInit.sendDiscoveryStreamSpocsUpdateReply()
- 位置: L77-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `at.DISCOVERY_STREAM_SPOCS_UPDATE`, `spocsState.cacheUpdateTime`, `spocsState.data`, `spocsState.lastUpdated`, `spocsState.onDemand.enabled`, `this.store.getState().DiscoveryStream.spocs`

## StartupCacheInit.sendWeatherUpdateReply()
- 位置: L93-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `Weather.lastUpdated`, `Weather.locationData`, `Weather.suggestions`, `at.WEATHER_UPDATE`

## StartupCacheInit.sendCustomWallpaperUpdateReply()
- 位置: L108-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `Wallpapers.uploadedWallpaper`, `at.WALLPAPERS_CUSTOM_SET`

## StartupCacheInit.sendPrefChangesReply()
- 位置: L118-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`, `this.PrefChangesReply`

## StartupCacheInit.uninitFeed()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.uninitFeed()`
- 参照: `at.UNINIT`

## StartupCacheInit.onAction()
- 位置: async L132-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PrefChangesReply.clear()`
- 条件付き依存: `if (this.loaded)` → `this.stateRequestReply()`
- 条件付き依存: `if (this.loaded)` → `this.uninitFeed()`
- 条件付き依存: `if (this.loaded)` → `this.store.getState()`
- 条件付き依存: `if (this.loaded && action.data)` → `this.PrefChangesReply.set()`
- 参照: `action.data`, `action.meta.fromTarget`, `action.type`, `at.DISCOVERY_STREAM_SPOCS_UPDATE`, `at.INIT`, `at.NEW_TAB_STATE_REQUEST_STARTUPCACHE`, `at.NEW_TAB_STATE_REQUEST_WITHOUT_STARTUPCACHE`, `at.PREF_CHANGED`, `at.TOP_SITES_UPDATED`, `at.UNINIT`, `at.WALLPAPERS_CUSTOM_SET`, `at.WEATHER_UPDATE`, `this.CustomWallpaperUpdateReply`, `this.DiscoveryStreamSpocsUpdateReply`, `this.TopsitesUpdatedReply`, `this.WeatherUpdateReply`, `this.loaded`, `this.store.getState().Prefs.values`
