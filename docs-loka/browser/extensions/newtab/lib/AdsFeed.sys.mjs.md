# browser/extensions/newtab/lib/AdsFeed.sys.mjs

source: browser/extensions/newtab/lib/AdsFeed.sys.mjs
source-hash: 5c84a92f2a1cdf74b9f81a5c5b15d0b5354c52ef
lines: 683

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AdsFeed.constructor()
- 位置: L62-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.adsClient`, `this.cache`, `this.enabled`, `this.lastUpdated`, `this.loaded`, `this.spocPlacements`, `this.spocs`, `this.tiles`

## AdsFeed._resetCache()
- 位置: async L73-77
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.cache)` → `this.cache.set()`
- 参照: `this.cache`

## AdsFeed.resetAdsFeed()
- 位置: async L79-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`, `this._resetCache()`, `this.store.dispatch()`
- 参照: `at.ADS_RESET`, `this.enabled`, `this.lastUpdated`, `this.loaded`, `this.spocPlacements`, `this.spocs`, `this.tiles`

## AdsFeed.deleteUserAdsData()
- 位置: async L95-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `headers.append()`, `lazy.ContextId.request()`, `this.fetch()`, `this.store.getState()`
- 参照: `state.Prefs.values`

## AdsFeed.isAdsFeedEnabled()
- 位置: L118-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## AdsFeed.isEnabled()
- 位置: L123-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.deleteUserAdsData()`, `this.isAdsFeedEnabled()`, `this.store.getState()`
- 参照: `this.enabled`, `this.loaded`, `this.store.getState().Prefs.values`

## AdsFeed.fetch()
- 位置: L175-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`

## AdsFeed._normalizeTileData()
- 位置: L186-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`
- 条件付き依存: `if (responseTilesData?.length)` → `formattedTileDataArray.push()`
- 参照: `responseTilesData?.length`, `tile.block_key`, `tile.callbacks.click`, `tile.callbacks.impression`, `tile.image_url`, `tile.name`, `tile.url`

## AdsFeed.getSupportedAdTypes()
- 位置: L218-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## AdsFeed.getAdsData()
- 位置: async L239-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`, `this.cache.get()`, `this.getSupportedAdTypes()`, `this.update()`
- 条件付き依存: `if (!ads?.lastUpdated || !adsCacheValid)` → `this.fetchData()`
- 条件付き依存: `if (!ads?.lastUpdated || !adsCacheValid)` → `this.Date().now()`
- 条件付き依存: `if (!ads?.lastUpdated || !adsCacheValid)` → `this.Date()`
- 参照: `ads.lastUpdated`, `ads?.lastUpdated`, `data.lastUpdated`, `data.spocPlacements`, `data.spocs`, `data.tiles`, `supportedAdTypes.spocs`, `supportedAdTypes.tiles`, `this.adsClient`, `this.lastUpdated`, `this.spocPlacements`, `this.spocs`, `this.tiles`

## AdsFeed.fetchData()
- 位置: async L287-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `blockedSponsors.split()`, `headers.append()`, `lazy.ContextId.request()`, `this.store.getState()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[ PREF_TILES_PLACEMENTS ]?.split(`,`) .map(s => s.trim()) .filter()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[ PREF_TILES_PLACEMENTS ]?.split(`,`) .map()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[ PREF_TILES_PLACEMENTS ]?.split()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `s.trim()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[PREF_TILES_COUNTS]?.split(`,`) .map(s => s.trim()) .filter(item => item) .map()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[PREF_TILES_COUNTS]?.split(`,`) .map(s => s.trim()) .filter()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[PREF_TILES_COUNTS]?.split(`,`) .map()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `state.Prefs.values[PREF_TILES_COUNTS]?.split()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `parseInt()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `tilesPlacementsArray.map()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `placements.push()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[ PREF_SPOC_PLACEMENTS ]?.split(`,`) .map(s => s.trim()) .filter()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[ PREF_SPOC_PLACEMENTS ]?.split(`,`) .map()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[ PREF_SPOC_PLACEMENTS ]?.split()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `s.trim()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[PREF_SPOC_COUNTS]?.split(`,`) .map(s => s.trim()) .filter(item => item) .map()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[PREF_SPOC_COUNTS]?.split(`,`) .map(s => s.trim()) .filter()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[PREF_SPOC_COUNTS]?.split(`,`) .map()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `state.Prefs.values[PREF_SPOC_COUNTS]?.split()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `parseInt()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `spocPlacementsArray.map()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `placements.push()`
- 条件付き依存: `if (this.adsClient)` → `this._fetchWithAdsClient()`
- 条件付き依存: `if (marsOhttpEnabled && ohttpConfigURL && ohttpRelayURL)` → `lazy.ObliviousHTTP.getOHTTPConfig()`
- 条件付き依存: `if (!config)` → `console.error()`
- 条件付き依存: `if (marsOhttpEnabled && ohttpConfigURL && ohttpRelayURL)` → `lazy.ObliviousHTTP.ohttpRequest()`
- 条件付き依存: `if (!(marsOhttpEnabled && ohttpConfigURL && ohttpRelayURL))` → `this.fetch()`
- 条件付き依存: `if (response && response.status === 200)` → `response.json()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `Object.keys(responseData) .filter(key => key.startsWith("newtab_tile_")) .reduce()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `Object.keys(responseData) .filter()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `Object.keys()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `key.startsWith()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `this._normalizeTileData()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `Object.keys(responseData) .filter(key => !key.startsWith("newtab_tile_")) .reduce()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `Object.keys(responseData) .filter()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `Object.keys()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `key.startsWith()`
- 参照: `filteredRespDataNonTiles.newtab_spocs`, `normalizedTileData.tiles`, `response.status`, `response.statusText`, `returnData.spocPlacements`, `returnData.spocs`, `returnData.tiles`, `state.Prefs.values`, `state.Prefs.values?.adsBackendConfig`, `supportedAdTypes.spocs`, `supportedAdTypes.tiles`, `this.adsClient`, `this.store.getState().Prefs.values`
- XPCOM: `Services.prefs`

## AdsFeed._fetchWithAdsClient()
- 位置: async L457-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AdsClient.requestOptions()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `placements.filter(isTile).map()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `placements.filter()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `this.adsClient.requestTileAds()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `Array.from()`
- 条件付き依存: `if (supportedAdTypes.tiles)` → `tiles.values()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `placements .filter(p => !isTile(p)) .map()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `placements .filter()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `isTile()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `this.adsClient.requestSpocAds()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `(spocs.get("newtab_spocs") ?? []).map()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `spocs.get()`
- 条件付き依存: `if (supportedAdTypes.spocs)` → `Object.fromEntries()`
- 参照: `lazy.MozAdsPlacementRequest`, `lazy.MozAdsPlacementRequestWithCount`, `p.count`, `p.placement`, `returnData.spocs`, `returnData.tiles`, `spoc.blockKey`, `spoc.callbacks`, `spoc.caps`, `spoc.caps.capKey`, `spoc.caps.day`, `spoc.domain`, `spoc.excerpt`, `spoc.format`, `spoc.imageUrl`, `spoc.ranking`, `spoc.ranking.itemScore`, `spoc.ranking.personalizationModels`, `spoc.ranking.priority`, `spoc.sponsor`, `spoc.sponsoredByOverride`, `spoc.title`, `spoc.url`, `supportedAdTypes.spocs`, `supportedAdTypes.tiles`, `tile.blockKey`, `tile.callbacks.click`, `tile.callbacks.impression`, `tile.imageUrl`, `tile.name`, `tile.url`

## isTile()
- 位置: L463-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `p.placement?.startsWith()`

## AdsFeed.init()
- 位置: async L534-542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AdsClient.isEnabled()`, `this.isEnabled()`, `this.store.getState()`
- 条件付き依存: `if (lazy.AdsClient.isEnabled(this.store.getState().Prefs.values))` → `lazy.AdsClient.getClient()`
- 条件付き依存: `if (this.isEnabled())` → `this.getAdsData()`
- 参照: `this.adsClient`, `this.store.getState().Prefs.values`

## AdsFeed.update()
- 位置: async L550-590
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.adsClient)` → `this.cache.set()`
- 条件付き依存: `if (this.tiles && this.tiles.length)` → `this.store.dispatch()`
- 条件付き依存: `if (this.tiles && this.tiles.length)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (this.spocs && this.spocs.length)` → `this.store.dispatch()`
- 条件付き依存: `if (this.spocs && this.spocs.length)` → `ac.BroadcastToContent()`
- 参照: `at.ADS_UPDATE_SPOCS`, `at.ADS_UPDATE_TILES`, `this.adsClient`, `this.lastUpdated`, `this.spocPlacements`, `this.spocs`, `this.spocs.length`, `this.tiles`, `this.tiles.length`

## AdsFeed.onPrefChangedAction()
- 位置: async L592-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAdsFeedEnabled()`, `this.isEnabled()`
- 条件付き依存: `if (this.isEnabled())` → `this.getAdsData()`
- 条件付き依存: `if (!(this.isEnabled()))` → `this.deleteUserAdsData()`
- 条件付き依存: `if (!(this.isEnabled()))` → `this.resetAdsFeed()`
- 条件付き依存: `if (action.data.value)` → `this.getAdsData()`
- 条件付き依存: `if (!(action.data.value))` → `this.deleteUserAdsData()`
- 条件付き依存: `if (!(action.data.value))` → `this.resetAdsFeed()`
- 参照: `action.data.name`, `action.data.value`

## AdsFeed.onAction()
- 位置: async L635-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`, `this.isEnabled()`, `this.onPrefChangedAction()`, `this.resetAdsFeed()`
- 条件付き依存: `if (this.isEnabled())` → `this.getAdsData()`
- 参照: `action.type`, `at.DISCOVERY_STREAM_CONFIG_CHANGE`, `at.DISCOVERY_STREAM_DEV_EXPIRE_CACHE`, `at.DISCOVERY_STREAM_DEV_REFRESH_CACHE`, `at.DISCOVERY_STREAM_DEV_SYSTEM_TICK`, `at.INIT`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.UNINIT`

## AdsFeed.prototype.PersistentCache()
- 位置: L672-674
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## AdsFeed.prototype.Date()
- 位置: L676-678
- 役割: (未記入)
- 触るとき: (未記入)

## AdsFeed.prototype.ObliviousHTTP()
- 位置: L680-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ObliviousHTTP()`
