# browser/extensions/newtab/lib/TopSitesFeed.sys.mjs

source: browser/extensions/newtab/lib/TopSitesFeed.sys.mjs
source-hash: fc396dba31f6fa06cfd924296705f7cc705e45f6
lines: 2853

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/protocol;1?name=http"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## getTopSitesCount()
- 位置: L158-165
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `prefValues.trainhopConfig?.topSites?.maxSitesPerRow`

## smartshortcutsEnabled()
- 位置: L174-181
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `values.trainhopConfig?.smartShortcuts?.enabled`

## getShortHostnameForCurrentSearch()
- 位置: L184-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortHostname()`
- 参照: `lazy.SearchService.defaultEngine.searchUrlDomain`

## TopSitesTelemetry.constructor()
- 位置: L191-194
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.allSponsoredTiles`, `this.sponsoredTilesConfigured`

## TopSitesTelemetry._tileProviderForTiles()
- 位置: L196-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tileProvider()`
- 参照: `tiles.length`

## TopSitesTelemetry._tileProvider()
- 位置: L201-203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tile.partner`

## TopSitesTelemetry._buildPropertyKey()
- 位置: L205-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortURL()`, `this._tileProvider()`

## TopSitesTelemetry._getFilteredTiles()
- 位置: L215-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.entries()`, `Object.entries(this.allSponsoredTiles) .filter()`, `Object.keys()`, `Object.keys(notPreviouslyFilteredTiles).filter()`, `currentTiles.map()`, `remainingTiles.includes()`, `this._buildPropertyKey()`
- 参照: `this.allSponsoredTiles`, `v.display_fail_reason`

## TopSitesTelemetry.setSponsoredTilesConfigured()
- 位置: L239-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.topsites.sponsoredTilesConfigured.set()`, `lazy.NimbusFeatures.pocketNewtab.getVariable()`
- 参照: `this.sponsoredTilesConfigured`

## TopSitesTelemetry.clearTilesForProvider()
- 位置: L249-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(this.allSponsoredTiles) .filter()`, `Object.entries(this.allSponsoredTiles) .filter(([k]) => k.startsWith(provider)) .map()`, `k.startsWith()`
- 参照: `this.allSponsoredTiles`

## TopSitesTelemetry._getAdvertiser()
- 位置: L255-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortURL()`
- 参照: `tile.label`, `tile.title`

## TopSitesTelemetry.setTiles()
- 位置: L262-278
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tiles && tiles.length)` → `this._tileProviderForTiles()`
- 条件付き依存: `if (tiles && tiles.length)` → `this.clearTilesForProvider()`
- 条件付き依存: `if (tiles && tiles.length)` → `this._buildPropertyKey()`
- 条件付き依存: `if (tiles && tiles.length)` → `this._getAdvertiser(sponsoredTile).toLowerCase()`
- 条件付き依存: `if (tiles && tiles.length)` → `this._getAdvertiser()`
- 参照: `this.allSponsoredTiles`, `tiles.length`

## TopSitesTelemetry._setDisplayFailReason()
- 位置: L280-288
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.allSponsoredTiles`, `tileToUpdate.display_fail_reason`, `tileToUpdate.display_position`

## TopSitesTelemetry.determineFilteredTilesAndSetToOversold()
- 位置: L290-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getFilteredTiles()`, `this._setDisplayFailReason()`

## TopSitesTelemetry.determineFilteredTilesAndSetToDismissed()
- 位置: L295-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getFilteredTiles()`, `this._setDisplayFailReason()`

## TopSitesTelemetry._setTilePositions()
- 位置: L300-350
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.allSponsoredTiles)` → `currentTiles.forEach()`
- 条件付き依存: `if (this.allSponsoredTiles)` → `this._buildPropertyKey()`
- 条件付き依存: `if ( tile && (tile.display_fail_reason === undefined || tile.display_fail_reason === null) )` → `tilePositionsAssigned.push()`
- 条件付き依存: `if (this.allSponsoredTiles)` → `Object.keys(this.allSponsoredTiles).forEach()`
- 条件付き依存: `if (this.allSponsoredTiles)` → `Object.keys()`
- 条件付き依存: `if (!tile.display_fail_reason && !tile.display_position)` → `tilesMissingPosition.push()`
- 条件付き依存: `if (tilesMissingPosition.length)` → `tilePositionsAssigned.includes()`
- 条件付き依存: `if (!tilePositionsAssigned.includes(i))` → `tilesMissingPosition.shift()`
- 条件付き依存: `if (this.allSponsoredTiles)` → `this._detectErrorConditionAndSetUnresolved()`
- 参照: `item.sponsored_position`, `this.allSponsoredTiles`, `this.allSponsoredTiles[tileProperty].display_position`, `this.sponsoredTilesConfigured`, `tile.display_fail_reason`, `tile.display_position`, `tilesMissingPosition.length`

## TopSitesTelemetry._detectErrorConditionAndSetUnresolved()
- 位置: L353-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(this.allSponsoredTiles).forEach()`
- 参照: `this.allSponsoredTiles`, `tile.display_fail_reason`, `tile.display_position`

## TopSitesTelemetry.finalizeNewtabPingFields()
- 位置: L366-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.topsites.sponsoredTilesReceived.set()`, `JSON.stringify()`, `Object.values()`, `this._setTilePositions()`
- 参照: `this.allSponsoredTiles`

## ContileIntegration.constructor()
- 位置: L377-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this._lastPeriodicUpdate`, `this._sites`, `this._sov`, `this._topSitesFeed`, `this.cache`

## ContileIntegration.sites()
- 位置: L386-388
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._sites`

## ContileIntegration.sov()
- 位置: L390-392
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._sov`

## ContileIntegration.periodicUpdate()
- 位置: L394-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (now - this._lastPeriodicUpdate >= CONTILE_UPDATE_INTERVAL)` → `this.refresh()`
- 参照: `this._lastPeriodicUpdate`

## ContileIntegration.refresh()
- 位置: async L402-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._fetchSites()`, `this._topSitesFeed.allocatePositions()`
- 条件付き依存: `if (updateDefaultSites)` → `this._topSitesFeed._readDefaults()`

## ContileIntegration._resetContileCache()
- 位置: L413-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `this.cache.set()`
- XPCOM: `Services.prefs`

## ContileIntegration._filterBlockedSponsors()
- 位置: L427-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `blocklist.includes()`, `lazy.NewTabUtils.shortURL()`, `tiles.filter()`
- 参照: `this._topSitesFeed._currentSearchHostname`
- XPCOM: `Services.prefs`

## ContileIntegration._extractCacheValidFor()
- 位置: L459-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.parseInt()`, `cacheHeader.match()`, `isNaN()`, `this._topSitesFeed.store.getState()`
- 条件付き依存: `if (!cacheHeader && !unifiedAdsTilesEnabled)` → `lazy.log.warn()`
- 参照: `this._topSitesFeed.store.getState().Prefs.values`

## ContileIntegration._loadTilesFromCache()
- 位置: async L480-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.round()`, `Services.prefs.getIntPref()`, `lazy.log.info()`, `this._topSitesFeed._telemetryUtility.setSponsoredTilesConfigured()`
- 条件付き依存: `if (now <= lastFetch + validFor)` → `this.cache.get()`
- 条件付き依存: `if (now <= lastFetch + validFor)` → `this._topSitesFeed._telemetryUtility.setTiles()`
- 条件付き依存: `if (now <= lastFetch + validFor)` → `this._filterBlockedSponsors()`
- 条件付き依存: `if (now <= lastFetch + validFor)` → `this._topSitesFeed._telemetryUtility.determineFilteredTilesAndSetToDismissed()`
- 条件付き依存: `if (now <= lastFetch + validFor)` → `lazy.log.info()`
- 条件付き依存: `if (now <= lastFetch + validFor)` → `lazy.log.warn()`
- 参照: `cachedData.contile`, `this._sites`
- XPCOM: `Services.prefs`

## ContileIntegration._getMaxNumFromContile()
- 位置: L516-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pocketNewtab.getVariable()`

## ContileIntegration._normalizeTileData()
- 位置: L534-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `Object.keys()`, `Object.keys(data).filter()`, `placementIds.filter()`, `placementIds.includes()`
- 条件付き依存: `if (tile)` → `formattedTileData.push()`
- 参照: `tile.attributions`, `tile.block_key`, `tile.callbacks.click`, `tile.callbacks.impression`, `tile.image_url`, `tile.name`, `tile.url`

## ContileIntegration.sovEnabled()
- 位置: L570-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._topSitesFeed.store.getState()`
- 参照: `this._topSitesFeed.store.getState().Prefs`, `values?.trainhopConfig?.sov?.enabled`

## ContileIntegration.csvToInts()
- 位置: L576-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`, `s.trim()`, `val .split()`, `val .split(",") .map()`, `val .split(",") .map(s => s.trim()) .filter()`, `val .split(",") .map(s => s.trim()) .filter(item => item) .map()`

## ContileIntegration.generateSov()
- 位置: L607-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `this._topSitesFeed.store.getState()`, `this.csvToInts()`
- 参照: `this._topSitesFeed.store.getState().Prefs`, `trainhopSovConfig.amp`, `trainhopSovConfig.frec`, `trainhopSovConfig.name`, `values?.trainhopConfig?.sov`

## ContileIntegration._fetchSites()
- 位置: async L636-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.NimbusFeatures.newtab.getVariable()`, `lazy.SearchService.init()`, `lazy.log.warn()`, `this._loadTilesFromCache()`, `this._topSitesFeed.store.getState()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_PLACEMENTS ]?.split(`,`) .map(s => s.trim()) .filter()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_PLACEMENTS ]?.split(`,`) .map()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_PLACEMENTS ]?.split()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `s.trim()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_COUNTS ]?.split(`,`) .map(s => s.trim()) .filter(item => item) .map()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_COUNTS ]?.split(`,`) .map(s => s.trim()) .filter()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_COUNTS ]?.split(`,`) .map()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `state.Prefs.values[ PREF_UNIFIED_ADS_COUNTS ]?.split()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `parseInt()`
- 条件付き依存: `if (this._topSitesFeed.adsClient)` → `this._fetchSitesWithAdsClient()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `headers.append()`
- 条件付き依存: `if (marsOhttpEnabled)` → `this._topSitesFeed.fetch()`
- 条件付き依存: `if (marsOhttpEnabled)` → `preflightResponse.json()`
- 条件付き依存: `if (preFlight)` → `headers.append()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `this._topSitesFeed.store.getState()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `Array.from()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `blockedSponsors .split(",") .concat(this._topSitesFeed._currentSearchHostname || []) .filter()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `blockedSponsors .split(",") .concat()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `blockedSponsors .split()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `JSON.stringify()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `lazy.ContextId.request()`
- 条件付き依存: `if (!(this._topSitesFeed.adsClient))` → `placementsArray.map()`
- 条件付き依存: `if (marsOhttpEnabled && ohttpConfigURL && ohttpRelayURL)` → `lazy.ObliviousHTTP.getOHTTPConfig()`
- 条件付き依存: `if (!config)` → `console.error()`
- 条件付き依存: `if (options.headers && options.headers instanceof Headers)` → `Object.fromEntries()`
- 条件付き依存: `if (marsOhttpEnabled && ohttpConfigURL && ohttpRelayURL)` → `lazy.ObliviousHTTP.ohttpRequest()`
- 条件付き依存: `if (!(marsOhttpEnabled && ohttpConfigURL && ohttpRelayURL))` → `this._topSitesFeed.fetch()`
- 条件付き依存: `if (!(unifiedAdsTilesEnabled))` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (!(unifiedAdsTilesEnabled))` → `this._topSitesFeed.fetch()`
- 条件付き依存: `if (response && !response.ok)` → `lazy.log.warn()`
- 条件付き依存: `if (response.status === 304 || response.status >= 500)` → `this._loadTilesFromCache()`
- 条件付き依存: `if (!adsFeedEnabled)` → `Math.round()`
- 条件付き依存: `if (!adsFeedEnabled)` → `Date.now()`
- 条件付き依存: `if (!adsFeedEnabled)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!adsFeedEnabled)` → `this._topSitesFeed._telemetryUtility.setSponsoredTilesConfigured()`
- 条件付き依存: `if (response && response.status === 204)` → `this._topSitesFeed._telemetryUtility.clearTilesForProvider()`
- 条件付き依存: `if (this._sites.length)` → `this.cache.set()`
- 条件付き依存: `if (response && response.status === 200)` → `response.json()`
- 条件付き依存: `if (!(adsFeedEnabled))` → `this._normalizeTileData()`
- 条件付き依存: `if (body?.sov)` → `JSON.parse()`
- 条件付き依存: `if (body?.sov)` → `atob()`
- 条件付き依存: `if (!(body?.sov))` → `this.sovEnabled()`
- 条件付き依存: `if (this.sovEnabled())` → `this.generateSov()`
- 条件付き依存: `if (body?.tiles && Array.isArray(body.tiles))` → `lazy.NimbusFeatures.newtab.getVariable()`
- 条件付き依存: `if (body?.tiles && Array.isArray(body.tiles))` → `this._getMaxNumFromContile()`
- 条件付き依存: `if (body?.tiles && Array.isArray(body.tiles))` → `this._topSitesFeed._telemetryUtility.setTiles()`
- 条件付き依存: `if ( useAdditionalTiles !== undefined && !useAdditionalTiles && tiles.length > maxNumFromContile )` → `this._topSitesFeed._telemetryUtility.determineFilteredTilesAndSetToOversold()`
- 条件付き依存: `if (body?.tiles && Array.isArray(body.tiles))` → `this._filterBlockedSponsors()`
- 条件付き依存: `if (body?.tiles && Array.isArray(body.tiles))` → `this._topSitesFeed._telemetryUtility.determineFilteredTilesAndSetToDismissed()`
- 条件付き依存: `if (tiles.length > maxNumFromContile)` → `lazy.log.info()`
- 条件付き依存: `if (tiles.length > maxNumFromContile)` → `this._topSitesFeed._telemetryUtility.determineFilteredTilesAndSetToOversold()`
- 条件付き依存: `if (body?.tiles && Array.isArray(body.tiles))` → `this.cache.set()`
- 条件付き依存: `if (!unifiedAdsTilesEnabled)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!unifiedAdsTilesEnabled)` → `this._extractCacheValidFor()`
- 条件付き依存: `if (!unifiedAdsTilesEnabled)` → `response.headers.get()`
- 条件付き依存: `if (!(!unifiedAdsTilesEnabled))` → `Services.prefs.setIntPref()`
- 参照: `body.sov`, `body.tiles`, `body?.sov`, `body?.tiles`, `error.message`, `lazy.userAgent`, `options.headers`, `preFlight.geo_location`, `preFlight.geoname_id`, `preFlight.normalized_ua`, `response.ok`, `response.status`, `state.Ads`, `state.Prefs.values`, `state.Prefs.values?.adsBackendConfig`, `this._sites`, `this._sites.length`, `this._sov`, `this._topSitesFeed._currentSearchHostname`, `this._topSitesFeed.adsClient`, `this._topSitesFeed.store.getState().Prefs.values`, `tiles.length`
- XPCOM: `Services.prefs`

## ContileIntegration._fetchSitesWithAdsClient()
- 位置: async L936-975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `lazy.AdsClient.requestOptions()`, `placements.map()`, `this._topSitesFeed.adsClient.requestTileAds()`, `this._topSitesFeed.store.getState()`, `tiles.entries()`, `tiles.entries().map()`
- 参照: `lazy.MozAdsPlacementRequest`, `this._topSitesFeed._currentSearchHostname`, `this._topSitesFeed.store.getState().Prefs.values`, `tile.blockKey`, `tile.callbacks.click`, `tile.callbacks.impression`, `tile.imageUrl`, `tile.name`, `tile.url`

## ContileIntegration.prototype.PersistentCache()
- 位置: L982-984
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## TopSitesFeed.constructor()
- 位置: L990-1023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Promise.resolve()`, `lazy.PageThumbs.addExpirationFilter()`, `this._nimbusChangeListener.bind()`
- 参照: `lazy.LinksCache`, `lazy.NewTabUtils.activityStreamLinks`, `lazy.NewTabUtils.pinnedLinks`, `newOptions.numItems`, `oldOptions.numItems`, `this._broadcastPending`, `this._contile`, `this._dedupeKey`, `this._latestRefreshPromise`, `this._nimbusChangeListener`, `this._refreshGeneration`, `this._telemetryUtility`, `this._tippyTopProvider`, `this._uninitialized`, `this.adsClient`, `this.dedupe`, `this.frecencyBoostProvider`, `this.frecentCache`, `this.pinnedCache`, `this.ranker`

## TopSitesFeed._nimbusChangeListener()
- 位置: L1025-1039
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["feature-experiment-loaded", "feature-rollout-loaded"].includes()`
- 条件付き依存: `if ( !["feature-experiment-loaded", "feature-rollout-loaded"].includes(reason) )` → `this._contile.refresh()`

## TopSitesFeed.init()
- 位置: L1041-1052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `lazy.NimbusFeatures.newtab.onUpdate()`, `this._contile.refresh()`, `this._readDefaults()`, `this.frecencyBoostProvider.init()`
- 参照: `this._nimbusChangeListener`
- XPCOM: `Services.obs` / `Services.prefs`

## TopSitesFeed.uninit()
- 位置: L1054-1064
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.NimbusFeatures.newtab.offUpdate()`, `lazy.PageThumbs.removeExpirationFilter()`, `this.frecencyBoostProvider.uninit()`
- 参照: `this._nimbusChangeListener`, `this._uninitialized`
- XPCOM: `Services.obs` / `Services.prefs`

## TopSitesFeed.observe()
- 位置: L1066-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data.startsWith()`, `this._readDefaults()`, `this.refresh()`, `this.store.getState()`
- 条件付き依存: `if ( data === "engine-default" && this.store.getState().Prefs.values[FILTER_DEFAULT_SEARCH_PREF] )` → `getShortHostnameForCurrentSearch()`
- 条件付き依存: `if ( data === "engine-default" && this.store.getState().Prefs.values[FILTER_DEFAULT_SEARCH_PREF] )` → `this._contile.refresh()`
- 条件付き依存: `if ( data === REMOTE_SETTING_DEFAULTS_PREF || data === DEFAULT_SITES_OVERRIDE_PREF || data.startsWith(DEFAULT_SITES_EXPERIMENTS_PREF_BRANCH) )` → `this._readDefaults()`
- 参照: `this._currentSearchHostname`, `this.store.getState().Prefs.values`

## TopSitesFeed._dedupeKey()
- 位置: L1100-1102
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `site.hostname`

## TopSitesFeed._readContile()
- 位置: L1107-1153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DEFAULT_TOP_SITES.push()`, `Math.min()`, `lazy.NewTabUtils.shortURL()`, `this._telemetryUtility.determineFilteredTilesAndSetToOversold()`
- 参照: `contilePositions.length`, `link.favicon`, `link.faviconSize`, `site.attribution`, `site.click_url`, `site.id`, `site.image_size`, `site.image_url`, `site.impression_url`, `site.name`, `site.url`, `this._contile.sites`, `this._contile.sites.length`, `this._contilePositions`

## TopSitesFeed._readDefaults()
- 位置: async L1158-1264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DEFAULT_TOP_SITES.findIndex()`, `DEFAULT_TOP_SITES.push()`, `JSON.parse()`, `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `Services.prefs.prefIsLocked()`, `lazy.NewTabUtils.shortURL()`, `lazy.NimbusFeatures.newtab.getVariable()`, `sponsoredBlocklist.includes()`, `this._getRemoteConfig()`, `this.refresh()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(REMOTE_SETTING_DEFAULTS_PREF))` → `this.refreshDefaults()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(REMOTE_SETTING_DEFAULTS_PREF))` → `this.store.getState()`
- 条件付き依存: `if ( Services.prefs.prefIsLocked(DEFAULT_SITES_OVERRIDE_PREF) || Cu.isInAutomation )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if ( Services.prefs.prefIsLocked(DEFAULT_SITES_OVERRIDE_PREF) || Cu.isInAutomation )` → `this.refreshDefaults()`
- 条件付き依存: `if (contileEnabled)` → `this._readContile()`
- 条件付き依存: `if (siteData.search_shortcut)` → `this.topSiteToSearchTopSite()`
- 参照: `Cu.isInAutomation`, `DEFAULT_TOP_SITES.length`, `link.hostname`, `link.label`, `link.url_urlbar`, `site.hostname`, `siteData.search_shortcut`, `siteData.sponsored_position`, `siteData.title`, `siteData.url`, `siteData.url_urlbar_override`, `this._useRemoteSetting`, `this.store.getState().Prefs.values`
- XPCOM: `Services.prefs`

## TopSitesFeed._contilePositions()
- 位置: L1273-1280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isNaN()`, `lazy.NimbusFeatures.pocketNewtab .getVariable()`, `lazy.NimbusFeatures.pocketNewtab .getVariable(NIMBUS_VARIABLE_CONTILE_POSITIONS) ?.split()`, `lazy.NimbusFeatures.pocketNewtab .getVariable(NIMBUS_VARIABLE_CONTILE_POSITIONS) ?.split(",") .map()`, `parseInt()`
- 参照: `configured?.length`

## TopSitesFeed._maxSponsored()
- 位置: L1285-1291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pocketNewtab.getVariable()`

## TopSitesFeed._adEligiblePositions()
- 位置: L1300-1316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eligible.slice()`, `lazy.NimbusFeatures.newtab.getVariable()`, `positions.map()`, `this.store.getState()`
- 参照: `allocation.position`, `state.Prefs.values`, `state.TopSites.sov`, `this._contile.sov`, `this._contilePositions`, `this._maxSponsored`

## TopSitesFeed.refreshDefaults()
- 位置: L1318-1335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.refresh()`
- 条件付き依存: `if (sites)` → `sites.split()`
- 条件付き依存: `if (sites)` → `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if (sites)` → `DEFAULT_TOP_SITES.push()`
- 参照: `DEFAULT_TOP_SITES.length`, `site.hostname`

## TopSitesFeed._getRemoteConfig()
- 位置: async L1337-1420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `console.error()`, `result.filter()`, `result.sort()`, `this._remoteConfig.get()`, `topsite.exclude_experiments?.some()`, `topsite.exclude_locales?.includes()`, `topsite.exclude_regions?.includes()`, `topsite.include_experiments.every()`, `topsite.include_locales.includes()`, `topsite.include_regions.includes()`
- 条件付き依存: `if (!this._remoteConfig)` → `lazy.RemoteSettings()`
- 条件付き依存: `if (!this._remoteConfig)` → `this._remoteConfig.on()`
- 条件付き依存: `if (!this._remoteConfig)` → `this._readDefaults()`
- 条件付き依存: `if (!result.length)` → `console.error()`
- 条件付き依存: `if (firstTime && failed)` → `this._remoteConfig.db.clear()`
- 条件付き依存: `if (firstTime && failed)` → `this._getRemoteConfig()`
- 参照: `Services.locale.appLocaleAsBCP47`, `a.order`, `b.order`, `lazy.Region.home`, `result.length`, `this._remoteConfig`, `topsite.include_experiments?.length`, `topsite.include_locales?.length`, `topsite.include_regions?.length`
- XPCOM: `Services.locale` / `Services.prefs`

## TopSitesFeed.filterForThumbnailExpiration()
- 位置: L1422-1433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `acc.push()`, `callback()`, `rows.reduce()`, `this.store.getState()`
- 条件付き依存: `if (site.customScreenshotURL)` → `acc.push()`
- 参照: `site.customScreenshotURL`, `site.url`, `this.store.getState().TopSites`

## TopSitesFeed.shouldFilterSearchTile()
- 位置: L1441-1450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SEARCH_FILTERS.includes()`, `this.store.getState()`
- 参照: `this._currentSearchHostname`, `this.store.getState().Prefs.values`

## TopSitesFeed._maybeInsertSearchShortcuts()
- 位置: async L1459-1535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `this.store .getState() .Prefs.values[SEARCH_SHORTCUTS_HAVE_PINNED_PREF].split(",") .filter()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `this.store .getState() .Prefs.values[SEARCH_SHORTCUTS_HAVE_PINNED_PREF].split()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `this.store .getState()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `DEFAULT_TOP_SITES.filter(s => s.searchTopSite).map()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `DEFAULT_TOP_SITES.filter()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `this.store .getState() .Prefs.values[SEARCH_SHORTCUTS_SEARCH_ENGINES_PREF].split()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `shouldPin .map(getSearchProvider) .filter()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `shouldPin .map()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `shouldPin.every()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `prevInsertedShortcuts.includes()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `getTopSitesCount()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `this.store.getState()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `Math.max()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `[...plainPinnedSites].concat()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `Array(emptySlots).fill()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `Array()`
- 条件付き依存: `if (this.store.getState().Prefs.values[SEARCH_SHORTCUTS_EXPERIMENT])` → `tryToInsertSearchShortcut()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `this.store.dispatch()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `ac.SetPref()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `prevInsertedShortcuts.concat(newInsertedShortcuts).join()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `prevInsertedShortcuts.concat()`
- 参照: `newInsertedShortcuts.length`, `plainPinnedSites.length`, `s.hostname`, `s.searchTopSite`, `s.shortURL`, `shortcut.shortURL`, `this._currentSearchHostname`, `this._useRemoteSetting`, `this.store .getState() .Prefs.values`, `this.store.getState().Prefs.values`

## tryToInsertSearchShortcut()
- 位置: async L1499-1517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkHasSearchEngine()`, `lazy.NewTabUtils.shortURL()`, `pinnedSites.find()`, `pinnedSites.indexOf()`, `prevInsertedShortcuts.includes()`
- 条件付き依存: `if ( !pinnedSites.find( s => s && lazy.NewTabUtils.shortURL(s) === shortcut.shortURL ) && !prevInsertedShortcuts.includes(shortcut.shortURL) && nextAvailable > -...)` → `this.topSiteToSearchTopSite()`
- 条件付き依存: `if ( !pinnedSites.find( s => s && lazy.NewTabUtils.shortURL(s) === shortcut.shortURL ) && !prevInsertedShortcuts.includes(shortcut.shortURL) && nextAvailable > -...)` → `this._pinSiteAt()`
- 条件付き依存: `if ( !pinnedSites.find( s => s && lazy.NewTabUtils.shortURL(s) === shortcut.shortURL ) && !prevInsertedShortcuts.includes(shortcut.shortURL) && nextAvailable > -...)` → `newInsertedShortcuts.push()`
- 参照: `shortcut.keyword`, `shortcut.shortURL`, `shortcut.url`

## TopSitesFeed.fetch()
- 位置: L1541-1543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`

## TopSitesFeed.fetchFrecencyBoostedSpocs()
- 位置: async L1550-1578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contile.sovEnabled()`, `this.store.getState()`
- 条件付き依存: `if ( this._contile.sovEnabled() && this.store.getState().Prefs.values[SHOW_SPONSORED_PREF] )` → `this.store.getState()`
- 条件付き依存: `if (!randomSponsorEnabled)` → `this.frecencyBoostProvider.fetch()`
- 条件付き依存: `if (candidates.length)` → `this.frecencyBoostedSpocsExposureEvent()`
- 条件付き依存: `if (!candidates.length)` → `this.frecencyBoostProvider.retrieveRandomFrecencyTile()`
- 参照: `candidates.length`, `this.store.getState().Prefs`, `this.store.getState().Prefs.values`, `values?.trainhopConfig?.sov?.numItems`, `values?.trainhopConfig?.sov?.random_sponsor`

## TopSitesFeed.updateFrecencyBoostedSpocs()
- 位置: async L1583-1587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.frecencyBoostProvider.update()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs`, `values?.trainhopConfig?.sov?.numItems`

## TopSitesFeed.frecencyBoostedSpocsExposureEvent()
- 位置: L1595-1602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 条件付き依存: `if (trainhopSovEnabled)` → `this.store.dispatch()`
- 条件付き依存: `if (trainhopSovEnabled)` → `ac.SetPref()`
- 参照: `this.store.getState().Prefs`, `values?.trainhopConfig?.sov?.enabled`

## TopSitesFeed.fetchDiscoveryStreamSpocs()
- 位置: L1609-1680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 条件付き依存: `if (DiscoveryStream)` → `findSponsoredTopsitesPositions()`
- 条件付き依存: `if (discoveryStreamSpocPositions?.length)` → `Math.min()`
- 条件付き依存: `if (discoveryStreamSpocPositions?.length)` → `reformatImageURL()`
- 条件付き依存: `if (discoveryStreamSpocPositions?.length)` → `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if (discoveryStreamSpocPositions?.length)` → `sponsored.push()`
- 参照: `DiscoveryStream.spocs.data`, `DiscoveryStream.spocs.data["sponsored-topsites"]?.items`, `discoveryStreamSpocPositions.length`, `discoveryStreamSpocPositions?.length`, `discoveryStreamSpocPositions[i].index`, `discoveryStreamSpocs.length`, `spoc.flight_id`, `spoc.id`, `spoc.raw_image_src`, `spoc.shim`, `spoc.sponsor`, `spoc.title`, `spoc.url`

## findSponsoredTopsitesPositions()
- 位置: L1616-1625
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DiscoveryStream.layout`, `component.placement?.name`, `component.spocs.positions`, `row.components`

## reformatImageURL()
- 位置: L1632-1640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encodeURIComponent()`

## TopSitesFeed.getLinksWithDefaults()
- 位置: async L1683-1987
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.topsites.pinnedCount.set()`, `Object.assign()`, `Promise.all()`, `adEligible.has()`, `dedupedSponsored.forEach()`, `frecent.find()`, `getSearchProvider()`, `getTopSitesCount()`, `insertPinned()`, `lazy.FilterAdult.filter()`, `lazy.NewTabUtils.blockedLinks.isBlocked()`, `lazy.NewTabUtils.shortURL()`, `lazy.PlacesUtils.history.pageFrecencyThreshold()`, `lazy.SearchService.init()`, `notBlockedDefaultSites.find()`, `pinned.filter()`, `plainPinned.map()`, `smartshortcutsEnabled()`, `this._adEligiblePositions()`, `this._maybeCapSponsoredLinks()`, `this._maybeInsertSearchShortcuts()`, `this._mergeSponsoredLinks()`, `this._telemetryUtility.determineFilteredTilesAndSetToDismissed()`, `this._telemetryUtility.determineFilteredTilesAndSetToOversold()`, `this._telemetryUtility.setTiles()`, `this.dedupe.group()`, `this.fetchDiscoveryStreamSpocs()`, `this.fetchFrecencyBoostedSpocs()`, `this.frecentCache.request()`, `this.pinnedCache.request()`, `this.shouldFilterSearchTile()`, `this.store.getState()`, `withPinned.forEach()`, `withPinned.slice()`
- 条件付き依存: `if (!this.shouldFilterSearchTile(hostname))` → `frecent.push()`
- 条件付き依存: `if (!this.shouldFilterSearchTile(hostname))` → `this.topSiteToSearchTopSite()`
- 条件付き依存: `if (!(link.sponsored_position && link.hostname === "yandex"))` → `this.shouldFilterSearchTile()`
- 条件付き依存: `if (link.sponsored_position)` → `this._unpinSearchShortcut()`
- 条件付き依存: `if (!(link.sponsored_position))` → `notBlockedDefaultSites.push()`
- 条件付き依存: `if (!(link.sponsored_position))` → `this.topSiteToSearchTopSite()`
- 条件付き依存: `if (await this._maybeInsertSearchShortcuts(plainPinned))` → `this.pinnedCache.expire()`
- 条件付き依存: `if (await this._maybeInsertSearchShortcuts(plainPinned))` → `this.pinnedCache.request()`
- 条件付き依存: `if (link.searchTopSite)` → `getSearchProvider()`
- 条件付き依存: `if (link.searchTopSite)` → `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if (link.searchTopSite)` → `checkHasSearchEngine()`
- 条件付き依存: `if (!copy.favicon)` → `lazy.NewTabUtils.activityStreamProvider._faviconBytesToDataURI()`
- 条件付き依存: `if (!copy.favicon)` → `lazy.NewTabUtils.activityStreamProvider._addFavicons()`
- 条件付き依存: `if (!copy.favicon)` → `copy.__sharedCache.updateLink()`
- 条件付き依存: `if (smartshortcutsEnabled(this.store.getState().Prefs.values))` → `this.ranker.rankTopSites()`
- 条件付き依存: `if (smartshortcutsEnabled(this.store.getState().Prefs.values))` → `lazy.log.warn()`
- 条件付き依存: `if (this._groupedPinsEnabled)` → `pinned.filter(Boolean).map()`
- 条件付き依存: `if (this._groupedPinsEnabled)` → `pinned.filter()`
- 条件付き依存: `if (!(withPinned[index]?.sponsored_position))` → `withPinned.splice()`
- 条件付き依存: `if (link.customScreenshotURL)` → `this._fetchScreenshot()`
- 条件付き依存: `if (link.searchTopSite && !link.isDefault)` → `this._tippyTopProvider.processSite()`
- 条件付き依存: `if (!(link.searchTopSite && !link.isDefault))` → `this._fetchIcon()`
- 条件付き依存: `if (refreshId === null || refreshId === this._refreshGeneration)` → `this._telemetryUtility.finalizeNewtabPingFields()`
- 参照: `SEARCH_FILTERS.length`, `copy.favicon`, `error.message`, `frecent.length`, `frecentSite.screenshot`, `link.__sharedCache`, `link.customScreenshotURL`, `link.hostname`, `link.isDefault`, `link.is_ad_eligible_position`, `link.searchTopSite`, `link.sponsored_position`, `link.typedBonus`, `link.url`, `pinned.filter(Boolean).length`, `prefValues?.trainhopConfig?.smartShortcuts?.over_sample_multiplier`, `searchProvider.keyword`, `searchProvider.url`, `this._currentSearchHostname`, `this._groupedPinsEnabled`, `this._linksWithDefaults`, `this._refreshGeneration`, `this.store.getState().Prefs.values`, `withPinned.length`, `withPinned[index]?.sponsored_position`

## finder()
- 位置: L1828-1828
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `link.url`, `other.url`

## TopSitesFeed._maybeCapSponsoredLinks()
- 位置: L1994-2000
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `links.length`, `this._maxSponsored`

## TopSitesFeed._mergeSponsoredLinks()
- 位置: L2011-2094
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pocketNewtab.getVariable()`, `sponsored.push()`, `this.store.getState()`
- 条件付き依存: `if (sponsoredLinks[SPONSORED_TILE_PARTNER_AMP])` → `sponsoredLinks[SPONSORED_TILE_PARTNER_AMP].filter()`
- 条件付き依存: `if (!this._contile.sov || !sovReady)` → `Object.values(sponsoredLinks).flat()`
- 条件付き依存: `if (!this._contile.sov || !sovReady)` → `Object.values()`
- 条件付き依存: `if (assignedPartner)` → `candidates?.shift()`
- 条件付き依存: `if (assignedPartner)` → `candidate.label?.trim().toLowerCase()`
- 条件付き依存: `if (assignedPartner)` → `candidate.label?.trim()`
- 条件付き依存: `if (candLabel)` → `sponsored.some()`
- 条件付き依存: `if (candLabel)` → `s.label?.trim().toLowerCase()`
- 条件付き依存: `if (candLabel)` → `s.label?.trim()`
- 条件付き依存: `if (!link)` → `sponsoredLinks[partner].shift()`
- 条件付き依存: `if ( lazy.NimbusFeatures.pocketNewtab.getVariable( NIMBUS_VARIABLE_CONTILE_MAX_NUM_SPONSORED ) )` → `sponsored.concat()`
- 参照: `allocation.position`, `candidates.length`, `link.pos`, `link.sponsored_position`, `sponsoredLinks[partner].length`, `this._contile.sov`, `this.store.getState().TopSites.sov`

## TopSitesFeed.refresh()
- 位置: async L2103-2154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `refreshPromise.catch()`, `this.getLinksWithDefaults()`
- 条件付き依存: `if (!this._tippyTopProvider.initialized)` → `this._tippyTopProvider.init()`
- 条件付き依存: `if (this._broadcastPending)` → `this.store.dispatch()`
- 条件付き依存: `if (this._broadcastPending)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (!(this._broadcastPending))` → `this.store.dispatch()`
- 条件付き依存: `if (!(this._broadcastPending))` → `ac.AlsoToPreloaded()`
- 参照: `at.TOP_SITES_UPDATED`, `newAction.meta`, `options.broadcast`, `options.isStartup`, `this._broadcastPending`, `this._latestRefreshPromise`, `this._refreshGeneration`, `this._startedUp`, `this._tippyTopProvider.initialized`, `this._uninitialized`

## TopSitesFeed.allocatePositions()
- 位置: async L2157-2191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`, `allocatedPositions.push()`, `allocation.allocation.map()`, `lazy.ContextId.request()`, `this.store.dispatch()`
- 条件付き依存: `if (ratios.length)` → `lazy.Sampling.ratioSample()`
- 参照: `alloc.percentage`, `allocatedPosition.assignedPartner`, `allocatedPositions.length`, `allocation.allocation`, `allocation.allocation[index].partner`, `allocation.position`, `at.SOV_UPDATED`, `ratios.length`, `this._contile.sov`, `this._contile.sov.allocations`, `this._contile.sov.name`

## TopSitesFeed.updateCustomSearchShortcuts()
- 位置: async L2193-2224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CUSTOM_SEARCH_SHORTCUTS.find()`, `ac.BroadcastToContent()`, `engine.aliases.includes()`, `lazy.SearchService.getAppProvidedEngines()`, `this.store.dispatch()`, `this.store.getState()`
- 条件付き依存: `if (!this._tippyTopProvider.initialized)` → `this._tippyTopProvider.init()`
- 条件付き依存: `if (shortcut)` → `this._tippyTopProvider.processSite()`
- 条件付き依存: `if (shortcut)` → `searchShortcuts.push()`
- 参照: `at.UPDATE_SEARCH_SHORTCUTS`, `s.keyword`, `this._tippyTopProvider.initialized`, `this.store.getState().Prefs.values`

## TopSitesFeed.topSiteToSearchTopSite()
- 位置: async L2226-2239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkHasSearchEngine()`, `getSearchProvider()`, `lazy.NewTabUtils.shortURL()`
- 参照: `searchProvider.keyword`

## TopSitesFeed._fetchIcon()
- 位置: async L2244-2261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._fetchScreenshot()`, `this._requestRichIcon()`, `this._tippyTopProvider.processSite()`
- 参照: `link.favicon`, `link.faviconSize`, `link.tippyTopIcon`, `link.url`

## TopSitesFeed._fetchScreenshot()
- 位置: async L2270-2293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `lazy.Screenshots.maybeCacheScreenshot()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `at.SCREENSHOT_UPDATED`, `link.screenshot`, `link.url`, `this.store.getState().Prefs.values`

## TopSitesFeed.getScreenshotPreview()
- 位置: async L2301-2312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `lazy.Screenshots.getScreenshotForURL()`, `this.store.dispatch()`
- 参照: `at.PREVIEW_RESPONSE`

## TopSitesFeed._requestRichIcon()
- 位置: L2314-2319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.dispatch()`
- 参照: `at.RICH_ICON_MISSING`

## TopSitesFeed._broadcastPinnedSitesUpdated()
- 位置: L2324-2330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pinnedCache.expire()`, `this.refresh()`

## TopSitesFeed._groupedPins()
- 位置: L2332-2335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.pinnedLinks.links.filter()`

## TopSitesFeed._groupedPinsEnabled()
- 位置: L2342-2344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## TopSitesFeed._saveGroupedPins()
- 位置: L2346-2365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pinnedLinks.links.flatMap()`, `pinnedLinks.save()`, `pins.forEach()`
- 参照: `lazy.NewTabUtils`, `next.length`, `occupied.length`, `pinnedLinks._links`

## TopSitesFeed._pinSiteAt()
- 位置: async L2373-2398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.pinnedLinks.pin()`, `this._clearLinkCustomScreenshot()`
- 条件付き依存: `if (this._groupedPinsEnabled)` → `this._pinSiteAtGrouped()`
- 参照: `this._groupedPinsEnabled`, `toPin.customScreenshotURL`, `toPin.label`, `toPin.searchTopSite`

## TopSitesFeed._pinSiteAtGrouped()
- 位置: async L2407-2451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearLinkCustomScreenshot()`, `this._groupedPins.filter()`, `this._groupedPins.findIndex()`, `this._saveGroupedPins()`
- 条件付き依存: `if (index !== undefined)` → `pins.splice()`
- 条件付き依存: `if (index !== undefined)` → `Math.min()`
- 条件付き依存: `if (existingIndex !== -1)` → `pins.splice()`
- 条件付き依存: `if (!(existingIndex !== -1))` → `pins.push()`
- 条件付き依存: `if (!(existingIndex !== -1))` → `this.store.getState()`
- 条件付き依存: `if (!(existingIndex !== -1))` → `getTopSitesCount()`
- 条件付き依存: `if ( rows[getTopSitesCount(prefs) - 1]?.isPinned && prefs[ROWS_PREF] < TOP_SITES_MAX_ROWS )` → `this.store.dispatch()`
- 条件付き依存: `if ( rows[getTopSitesCount(prefs) - 1]?.isPinned && prefs[ROWS_PREF] < TOP_SITES_MAX_ROWS )` → `ac.SetPref()`
- 参照: `p.url`, `pins.length`, `rows[getTopSitesCount(prefs) - 1]?.isPinned`, `this.store.getState().Prefs.values`, `this.store.getState().TopSites`, `toPin.customScreenshotURL`, `toPin.label`, `toPin.searchTopSite`

## TopSitesFeed._clearLinkCustomScreenshot()
- 位置: async L2453-2462
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (site.customScreenshotURL !== undefined)` → `this.pinnedCache.request()`
- 条件付き依存: `if (site.customScreenshotURL !== undefined)` → `pinned.find()`
- 条件付き依存: `if (link && link.customScreenshotURL !== site.customScreenshotURL)` → `link.__sharedCache.updateLink()`
- 参照: `link.customScreenshotURL`, `pin.url`, `site.customScreenshotURL`, `site.url`

## TopSitesFeed.pin()
- 位置: async L2467-2513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._adjustPinIndexForSponsoredLinks()`
- 条件付き依存: `if (index >= 0)` → `this.store.getState()`
- 条件付き依存: `if (index >= 0)` → `getTopSitesCount()`
- 条件付き依存: `if (pinsPastGrid)` → `this.store.getState()`
- 条件付き依存: `if (evictIndex >= 0)` → `this._pinSiteAt()`
- 条件付き依存: `if (evictIndex >= 0)` → `this._adjustPinIndexForSponsoredLinks()`
- 条件付き依存: `if (!(evictIndex >= 0))` → `this._pinSiteAt()`
- 条件付き依存: `if (pinsPastGrid && prefs[ROWS_PREF] < TOP_SITES_MAX_ROWS)` → `this.store.dispatch()`
- 条件付き依存: `if (pinsPastGrid && prefs[ROWS_PREF] < TOP_SITES_MAX_ROWS)` → `ac.SetPref()`
- 条件付き依存: `if (index >= 0)` → `this._broadcastPinnedSitesUpdated()`
- 条件付き依存: `if (index === -1)` → `lazy.NewTabUtils.blockedLinks.unblock()`
- 条件付き依存: `if (index === -1)` → `this.frecentCache.expire()`
- 条件付き依存: `if (!(index >= 0))` → `this.insert()`
- 参照: `action.data`, `link.isPinned`, `link.sponsored_position`, `site.url`, `this._groupedPinsEnabled`, `this.store.getState().Prefs.values`, `this.store.getState().TopSites`

## TopSitesFeed.unpin()
- 位置: L2518-2522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.pinnedLinks.unpin()`, `this._broadcastPinnedSitesUpdated()`
- 参照: `action.data`

## TopSitesFeed.unpinAllSearchShortcuts()
- 位置: L2524-2534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `this.pinnedCache.expire()`
- 条件付き依存: `if (pinnedLink && pinnedLink.searchTopSite)` → `lazy.NewTabUtils.pinnedLinks.unpin()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links`, `pinnedLink.searchTopSite`
- XPCOM: `Services.prefs`

## TopSitesFeed._unpinSearchShortcut()
- 位置: L2536-2558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `lazy.NewTabUtils.pinnedLinks.unpin()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `this.pinnedCache.expire()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `this.store .getState() .Prefs.values[SEARCH_SHORTCUTS_HAVE_PINNED_PREF].split()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `this.store .getState()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `this.store.dispatch()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `ac.SetPref()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `prevInsertedShortcuts.filter(s => s !== vendor).join()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `prevInsertedShortcuts.filter()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links`, `pinnedLink.searchTopSite`, `this.store .getState() .Prefs.values`

## TopSitesFeed._adjustPinIndexForSponsoredLinks()
- 位置: L2565-2583
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `link.sponsored_position`, `site.url`, `this._linksWithDefaults`, `this._linksWithDefaults[i]?.url`

## TopSitesFeed._insertPin()
- 位置: L2588-2635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTopSitesCount()`, `this._adjustPinIndexForSponsoredLinks()`, `this.store.getState()`
- 条件付き依存: `if (this._groupedPinsEnabled)` → `this._insertPinGrouped()`
- 条件付き依存: `if (!pinned[index])` → `this._pinSiteAt()`
- 条件付き依存: `if (!(!pinned[index]))` → `this._pinSiteAt()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links`, `this._groupedPinsEnabled`, `this.store.getState().Prefs.values`

## TopSitesFeed._insertPinGrouped()
- 位置: L2642-2649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTopSitesCount()`, `this._adjustPinIndexForSponsoredLinks()`, `this._pinSiteAtGrouped()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## TopSitesFeed.insert()
- 位置: async L2654-2678
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTopSitesCount()`, `this._broadcastPinnedSitesUpdated()`, `this._clearLinkCustomScreenshot()`, `this._insertPin()`, `this.store.getState()`
- 条件付き依存: `if (this._groupedPinsEnabled)` → `this._insertGrouped()`
- 参照: `action.data`, `action.data.draggedFromIndex`, `action.data.site`, `this._groupedPinsEnabled`, `this.store.getState().Prefs.values`

## TopSitesFeed._insertGrouped()
- 位置: async L2685-2694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._broadcastPinnedSitesUpdated()`, `this._clearLinkCustomScreenshot()`
- 条件付き依存: `if (draggedFromIndex !== undefined)` → `this._insertPinGrouped()`
- 条件付き依存: `if (!(draggedFromIndex !== undefined))` → `this._pinSiteAtGrouped()`
- 参照: `action.data`

## TopSitesFeed.updatePinnedSearchShortcuts()
- 位置: L2696-2730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addedShortcuts.forEach()`, `deletedShortcuts.forEach()`, `getTopSitesCount()`, `lazy.NewTabUtils.pinnedLinks.links.findIndex()`, `lazy.NewTabUtils.pinnedLinks.unpin()`, `this._broadcastPinnedSitesUpdated()`, `this.store.getState()`
- 条件付き依存: `if (this._groupedPinsEnabled)` → `this._updatePinnedSearchShortcutsGrouped()`
- 条件付き依存: `if (index >= 0)` → `lazy.NewTabUtils.pinnedLinks.pin()`
- 条件付き依存: `if (!(index >= 0))` → `this._insertPin()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links.length`, `this._groupedPinsEnabled`, `this.store.getState().Prefs.values`

## TopSitesFeed._updatePinnedSearchShortcutsGrouped()
- 位置: L2736-2747
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deletedShortcuts.map()`, `deletedUrls.has()`, `getTopSitesCount()`, `this._broadcastPinnedSitesUpdated()`, `this._groupedPins.filter()`, `this._saveGroupedPins()`, `this.store.getState()`
- 条件付き依存: `if (pins.length < numberOfSlots)` → `pins.push()`
- 参照: `p.url`, `pins.length`, `this.store.getState().Prefs.values`

## TopSitesFeed.onAction()
- 位置: L2749-2851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AdsClient.isEnabled()`, `lazy.NimbusFeatures.newtab.getVariable()`, `this._contile.periodicUpdate()`, `this._contile.refresh()`, `this.frecentCache.expire()`, `this.getScreenshotPreview()`, `this.init()`, `this.insert()`, `this.pin()`, `this.pinnedCache.expire()`, `this.refresh()`, `this.store.getState()`, `this.uninit()`, `this.unpin()`, `this.updateCustomSearchShortcuts()`, `this.updateFrecencyBoostedSpocs()`, `this.updatePinnedSearchShortcuts()`
- 条件付き依存: `if (lazy.AdsClient.isEnabled(this.store.getState().Prefs.values))` → `lazy.AdsClient.getClient()`
- 条件付き依存: `if (!this._useRemoteSetting)` → `this.refreshDefaults()`
- 条件付き依存: `if ( lazy.NimbusFeatures.newtab.getVariable( NIMBUS_VARIABLE_CONTILE_ENABLED ) )` → `this._contile.refresh()`
- 条件付き依存: `if (!( lazy.NimbusFeatures.newtab.getVariable( NIMBUS_VARIABLE_CONTILE_ENABLED ) ))` → `this.refresh()`
- 条件付き依存: `if (!action.data.value)` → `this._contile._resetContileCache()`
- 条件付き依存: `if (action.data.value)` → `this.updateCustomSearchShortcuts()`
- 条件付き依存: `if (!(action.data.value))` → `this.unpinAllSearchShortcuts()`
- 参照: `action.data`, `action.data.name`, `action.data.url`, `action.data.value`, `action.meta.fromTarget`, `action.type`, `at.ADS_UPDATE_TILES`, `at.DISCOVERY_STREAM_DEV_EXPIRE_CACHE`, `at.DISCOVERY_STREAM_DEV_SYSTEM_TICK`, `at.INIT`, `at.PLACES_HISTORY_CLEARED`, `at.PLACES_LINKS_CHANGED`, `at.PLACES_LINKS_DELETED`, `at.PLACES_LINK_BLOCKED`, `at.PREFS_INITIAL_VALUES`, `at.PREF_CHANGED`, `at.PREVIEW_REQUEST`, `at.SYSTEM_TICK`, `at.TOP_SITES_INSERT`, `at.TOP_SITES_PIN`, `at.TOP_SITES_UNPIN`, `at.UNINIT`, `at.UPDATE_PINNED_SEARCH_SHORTCUTS`, `this._useRemoteSetting`, `this.adsClient`, `this.store.getState().Prefs.values`
