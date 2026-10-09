# browser/extensions/newtab/lib/SmartShortcutsRanker/RankShortcuts.mjs

source: browser/extensions/newtab/lib/SmartShortcutsRanker/RankShortcuts.mjs
source-hash: b1f1cbe4077db39a8fe660a97208d07fc5245c6e
lines: 1034

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## gateRuntimeConfigByEngagement()
- 位置: L92-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(engagement.clicks ?? []).reduce()`, `(engagement.impressions ?? []).reduce()`, `Number.isFinite()`, `Object.hasOwn()`
- 参照: `engagement.clicks`, `engagement.impressions`, `gatedConfig.eta`, `gatedConfig.weights`, `gatedConfig.weights.thom`, `gatedConfig.weights?.thom`, `prefs.min_exp_clicks`, `prefs.min_exp_impressions`, `runtimeConfig?.weights`

## smartshortcutsEnabled()
- 位置: L135-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `prefValues?.trainhopConfig?.smartShortcuts?.enabled`

## roundNum()
- 位置: L148-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `Number()`, `Object.is()`, `isFinite()`, `x.toPrecision()`

## getOpenTabURLsFromSessionLive()
- 位置: async L164-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Math.max()`, `lazy.SessionStore.getBrowserState()`
- 条件付き依存: `if (url)` → `urls.push()`
- 参照: `entry?.url`, `lazy.SessionStore.promiseInitialized`, `state?.windows`, `tab.entries`, `tab.entries.length`, `tab.index`, `win?.tabs`

## getOpenTabsWithPlacesFromSessionLive()
- 位置: async L186-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOpenTabURLsFromSessionLive()`, `out.push()`, `url.startsWith()`
- 条件付き依存: `if (url.startsWith("http"))` → `lazy.PlacesUtils.history.fetch()`
- 参照: `(await lazy.PlacesUtils.history.fetch(url))?.guid`

## getIsOpen()
- 位置: async L209-233
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!isStartup?.isStartup)` → `getOpenTabsWithPlacesFromSessionLive()`
- 条件付き依存: `if (!isStartup?.isStartup)` → `openTabs.map(t => t.guid).filter()`
- 条件付き依存: `if (!isStartup?.isStartup)` → `openTabs.map()`
- 条件付き依存: `if (!isStartup?.isStartup)` → `openGuids.has()`
- 参照: `isStartup?.isStartup`, `t.guid`

## fetchVisitCountsByGuid()
- 位置: async L242-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`, `String()`, `String(guid).replace()`, `activityStreamProvider.executePlacesQuery()`, `guidList .map()`, `guidList .map(guid => `('${String(guid).replace(/'/g, "''")}')`) .join()`, `topsites.map()`
- 参照: `lazy.NewTabUtils`, `site.guid`, `topsites?.length`

## fetchLast10VisitsByGuid()
- 位置: async L280-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `String()`, `activityStreamProvider.executePlacesQuery()`, `g.replace()`, `guids .map()`, `guids .map(g => `('${g.replace(/'/g, "''")}')`) .join()`, `guids.map()`, `out[guid].push()`, `topsites.map()`
- 参照: `lazy.NewTabUtils`, `s.guid`, `topsites?.length`

## fetchBookmarkedFlags()
- 位置: async L336-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(guid).replace()`, `activityStreamProvider.executePlacesQuery()`, `guidList .map()`, `guidList .map(guid => `('${String(guid).replace(/'/g, "''")}')`) .join()`, `topsites.map()`
- 参照: `lazy.NewTabUtils`, `site.guid`, `topsites.length`

## fetchDailyVisitsSpecific()
- 位置: async L399-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activityStreamProvider.executePlacesQuery()`, `guid.replace()`, `guidList .map()`, `guidList .map(guid => `('${guid.replace(/'/g, "''")}')`) .join()`, `topsites.map()`
- 条件付き依存: `if (!histograms[key])` → `Array(7).fill()`
- 条件付き依存: `if (!histograms[key])` → `Array()`
- 条件付き依存: `if (!histograms[site.guid])` → `Array(7).fill()`
- 条件付き依存: `if (!histograms[site.guid])` → `Array()`
- 参照: `lazy.NewTabUtils`, `site.guid`, `topsites.length`

## fetchDailyVisitsAll()
- 位置: async L454-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `Array(7).fill()`, `activityStreamProvider.executePlacesQuery()`
- 参照: `lazy.NewTabUtils`

## fetchHourlyVisitsSpecific()
- 位置: async L483-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activityStreamProvider.executePlacesQuery()`, `guid.replace()`, `guidList .map()`, `guidList .map(guid => `('${guid.replace(/'/g, "''")}')`) .join()`, `topsites.map()`
- 条件付き依存: `if (!histograms[key])` → `Array(24).fill()`
- 条件付き依存: `if (!histograms[key])` → `Array()`
- 条件付き依存: `if (!histograms[site.guid])` → `Array(24).fill()`
- 条件付き依存: `if (!histograms[site.guid])` → `Array()`
- 参照: `lazy.NewTabUtils`, `site.guid`, `topsites.length`

## fetchHourlyVisitsAll()
- 位置: async L538-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `Array(24).fill()`, `activityStreamProvider.executePlacesQuery()`
- 参照: `lazy.NewTabUtils`

## initShortcutWeights()
- 位置: L566-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`
- 参照: `meta.def`, `meta.pref`, `prefValues?.trainhopConfig?.smartShortcuts`

## checkWeights()
- 位置: L590-607
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `Object.keys()`
- 参照: `Object.keys(all_weights.current).length`, `all_weights.current`, `all_weights.new_init`, `all_weights.old_init`

## fetchShortcutInteractions()
- 位置: async L617-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activityStreamProvider.executePlacesQuery()`, `guid.replace()`, `guidList .map()`, `guidList .map(guid => `('${guid.replace(/'/g, "''")}')`) .join()`, `guidList.map()`, `interactionMap.get()`, `interactionMap.has()`, `interactions.map()`, `topsites.map()`
- 参照: `interactionMap.get(guid).clicks`, `interactionMap.get(guid).impressions`, `lazy.NewTabUtils`, `site.guid`, `topsites.length`

## RankShortcutsProvider.constructor()
- 位置: L672-674
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`, `this.sc_obj`

## RankShortcutsProvider.rankShortcutsWorker()
- 位置: L675-683
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BasePromiseWorker`, `this._rankShortcutsWorker`

## RankShortcutsProvider.getHourlySeasonalityData()
- 位置: async L693-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `fetchHourlyVisitsSpecific()`
- 条件付き依存: `if (!startup && (missing || expired))` → `fetchHourlyVisitsAll()`
- 条件付き依存: `if (!startup && (missing || expired))` → `this.rankShortcutsWorker.post()`
- 条件付き依存: `if (!startup && (missing || expired))` → `this.sc_obj.set()`
- 条件付き依存: `if (!startup && (missing || expired))` → `Date.now()`
- 参照: `cache.pvec`, `cache.timestamp`, `cache?.pvec`, `isStartup.isStartup`, `shortcut_cache.hourly_seasonality`

## RankShortcutsProvider.getDailySeasonalityData()
- 位置: async L737-770
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `fetchDailyVisitsSpecific()`
- 条件付き依存: `if (!startup && (missing || expired))` → `fetchDailyVisitsAll()`
- 条件付き依存: `if (!startup && (missing || expired))` → `this.rankShortcutsWorker.post()`
- 条件付き依存: `if (!startup && (missing || expired))` → `this.sc_obj.set()`
- 条件付き依存: `if (!startup && (missing || expired))` → `Date.now()`
- 参照: `cache.pvec`, `cache.timestamp`, `cache?.pvec`, `isStartup.isStartup`, `shortcut_cache?.daily_seasonality`

## RankShortcutsProvider.getLatestInteractions()
- 位置: async L781-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Date.now()`, `Math.floor()`, `Math.max()`, `Number()`, `Object.create()`, `activityStreamProvider.executePlacesQuery()`, `this.sc_obj.set()`
- 条件付き依存: `if (tlu > 1e11)` → `Math.floor()`
- 参照: `cache_data.time_last_update`, `lazy.NewTabUtils`, `r.clicks`, `r.guid`, `r.impressions`

## RankShortcutsProvider.fetchRefreFeatures()
- 位置: async L828-841
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetchLast10VisitsByGuid()`, `fetchVisitCountsByGuid()`, `this.rankShortcutsWorker.post()`

## RankShortcutsProvider.rankTopSites()
- 位置: async L852-1032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isNaN()`, `Object.fromEntries()`, `["rece", "freq", "refre", "unid"].some()`, `checkWeights()`, `features.includes()`, `features.map()`, `features?.includes()`, `fetchBookmarkedFlags()`, `fetchShortcutInteractions()`, `final_scores.some()`, `gateRuntimeConfigByEngagement()`, `getIsOpen()`, `initShortcutWeights()`, `smartshortcutsEnabled()`, `sortKeysValues()`, `sortedSites.concat()`, `this.fetchRefreFeatures()`, `this.getDailySeasonalityData()`, `this.getHourlySeasonalityData()`, `this.getLatestInteractions()`, `this.rankShortcutsWorker.post()`, `this.sc_obj.get()`, `this.sc_obj.set()`, `topsites.reduce()`, `withGuid.map()`
- 条件付き依存: `if (site.guid && typeof site.guid === "string")` → `withG.push()`
- 条件付き依存: `if (!(site.guid && typeof site.guid === "string"))` → `withoutG.push()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `Object.fromEntries()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `Object.entries(rankingWeights ?? {}).map()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `Object.entries()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `isFinite()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `roundNum()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `combined.forEach()`
- 条件付き依存: `if (prefValues?.trainhopConfig?.smartShortcuts?.telem || SMART_TELEM)` → `Object.entries(raw).map()`
- 参照: `g.guid`, `learningConfig.eta`, `output.norms`, `output.score_map`, `output.score_map[g.guid].final`, `output?.score_map`, `prefValues.trainhopConfig?.smartShortcuts`, `prefValues.trainhopConfig?.smartShortcuts?.click_bonus`, `prefValues.trainhopConfig?.smartShortcuts?.eta`, `prefValues.trainhopConfig?.smartShortcuts?.features`, `prefValues.trainhopConfig?.smartShortcuts?.negative_prior`, `prefValues.trainhopConfig?.smartShortcuts?.positive_prior`, `prefValues.trainhopConfig?.smartShortcuts?.tau`, `prefValues?.trainhopConfig?.smartShortcuts?.telem`, `rankingConfig.weights`, `refrec_scores?.freq`, `refrec_scores?.rece`, `refrec_scores?.refre`, `refrec_scores?.unid`, `s.guid`, `s.scores`, `s.weights`, `sc_cache.init_weights`, `sc_cache.norms`, `sc_cache.score_map`, `sc_cache.weights`, `site.guid`, `t.frecency`, `t.guid`
