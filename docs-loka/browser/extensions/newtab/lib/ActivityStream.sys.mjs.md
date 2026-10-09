# browser/extensions/newtab/lib/ActivityStream.sys.mjs

source: browser/extensions/newtab/lib/ActivityStream.sys.mjs
source-hash: efc5491413413bc3212a24b739af64112c0501ae
lines: 2984

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `FEEDS_CONFIG.set()`, `JSON.stringify()`, `Object.entries()`, `PREFS_CONFIG.set()`, `XPCOMUtils.defineLazyServiceGetter()`, `marketGate()`

## csvHasValue()
- 位置: L225-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(csvString || "") .split()`, `(csvString || "") .split(",") .map()`, `(csvString || "") .split(",") .map(s => s.trim()) .filter()`, `(csvString || "") .split(",") .map(s => s.trim()) .filter(item => item) .includes()`, `s.trim()`

## csvPrefHasValue()
- 位置: L233-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `csvHasValue()`
- XPCOM: `Services.prefs`

## shouldInitializeFeeds()
- 位置: L241-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## useInferredPersonalization()
- 位置: L252-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## useSov()
- 位置: L259-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## useContextualAds()
- 位置: L266-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## matchesLegacyRegionStoriesConfig()
- 位置: L283-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LEGACY_REGION_STORIES_LOCALES[geo]?.includes()`, `csvHasValue()`, `lazy.NimbusFeatures.pocketNewtab.getVariable()`

## getStoriesTrainhopPayload()
- 位置: L300-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.NimbusFeatures.newtabTrainhop.getAllEnrollments()`
- 参照: `enrollment.meta?.isRollout`, `enrollment?.value`, `item.payload`, `item?.type`, `value.payload`, `value?.type`

## storiesRegionLocaleMatches()
- 位置: L337-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `RegionLocaleMap.fromJSON()`, `RegionLocaleMap.fromJSON(json, { fallback: STORIES_REGION_LOCALE_DEFAULT, }).matches()`, `Services.prefs.getStringPref()`, `getStoriesTrainhopPayload()`
- 条件付き依存: `if (Array.isArray(entries))` → `new RegionLocaleMap(entries).matches()`
- 参照: `getStoriesTrainhopPayload()?.config`
- XPCOM: `Services.prefs`

## showSpocs()
- 位置: L352-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pocketNewtab.getVariable()`, `s.trim()`, `spocsGeo.includes()`, `spocsGeoString.split()`, `spocsGeoString.split(",").map()`

## showWeather()
- 位置: L359-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## getDefaultWidgetSize()
- 位置: L374-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getWeatherWidgetSize()
- 位置: L408-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `getDefaultWidgetSize()`
- XPCOM: `Services.prefs`

## showWeatherOptIn()
- 位置: L430-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WEATHER_OPTIN_REGIONS.includes()`

## showTopicsSelection()
- 位置: L434-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## showTopicLabels()
- 位置: L441-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## showSectionLayout()
- 位置: L448-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPrefHasValue()`

## marketPref()
- 位置: L493-500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MARKET_PREF_FALLBACKS.get()`, `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## marketAllows()
- 位置: L502-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowed.trim()`, `csvHasValue()`, `marketPref()`

## prefIsSet()
- 位置: L510-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `marketPref()`, `marketPref(prefName).trim()`

## skipsNightlyDefault()
- 位置: L522-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WIDGET_REGISTRY.some()`
- 参照: `widget.enabledPref`, `widget.skipNightlyDefault`, `widget.systemEnabledPref`

## marketGateEnabled()
- 位置: L530-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## marketGate()
- 位置: L542-576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `marketAllows()`, `marketGateEnabled()`, `prefIsSet()`, `prefKey.replace()`, `skipsNightlyDefault()`
- 条件付き依存: `if (!marketGateEnabled())` → `prefKey.startsWith()`
- 参照: `AppConstants.NIGHTLY_BUILD`
- XPCOM: `Services.prefs`

## getValue()
- 位置: L653-654
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DEFAULT_SITES.get()`, `lazy.DEFAULT_SITES.has()`

## getValue()
- 位置: L865-865
- 役割: (未記入)
- 触るとき: (未記入)

## getValue()
- 位置: L1802-1802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `marketGateEnabled()`

## getValue()
- 位置: L1809-1809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `marketGateEnabled()`

## getValue()
- 位置: L1825-1825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `marketGateEnabled()`

## getValue()
- 位置: L1841-1841
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `marketGateEnabled()`

## getValue()
- 位置: L2077-2093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["DE", "FR", "GB", "IT", "JP", "US"].includes()`, `searchShortcuts.join()`
- 条件付き依存: `if (geo === "CN")` → `searchShortcuts.push()`
- 条件付き依存: `if (!(geo === "CN"))` → `["BY", "KZ", "RU", "TR"].includes()`
- 条件付き依存: `if (["BY", "KZ", "RU", "TR"].includes(geo))` → `searchShortcuts.push()`
- 条件付き依存: `if (!(["BY", "KZ", "RU", "TR"].includes(geo)))` → `searchShortcuts.push()`
- 条件付き依存: `if (["DE", "FR", "GB", "IT", "JP", "US"].includes(geo))` → `searchShortcuts.push()`

## getValue()
- 位置: L2123-2128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`

## getValue()
- 位置: L2144-2159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `preffedRegions.includes()`, `preffedRegionsString .split()`, `preffedRegionsString .split(",") .map()`, `s.trim()`
- XPCOM: `Services.prefs`

## getValue()
- 位置: L2291-2298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## getValue()
- 位置: L2305-2312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## getValue()
- 位置: L2319-2326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## getValue()
- 位置: L2334-2336
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.caretBlinkCount`
- XPCOM: `Services.appinfo`

## getValue()
- 位置: L2344-2346
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.caretBlinkTime`
- XPCOM: `Services.appinfo`

## factory()
- 位置: L2460-2460
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.StartupCacheInit`

## factory()
- 位置: L2466-2466
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AboutPreferences`

## factory()
- 位置: L2472-2472
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.NewTabInit`

## factory()
- 位置: L2478-2478
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PlacesFeed`

## factory()
- 位置: L2484-2484
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PrefsFeed`

## factory()
- 位置: L2490-2490
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SectionsFeed`

## factory()
- 位置: L2496-2496
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.HighlightsFeed`

## factory()
- 位置: L2502-2503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PREFS_CONFIG.get()`
- 参照: `lazy.TopStoriesFeed`

## getValue()
- 位置: L2507-2526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvHasValue()`, `lazy.NimbusFeatures.pocketNewtab.getVariable()`, `matchesLegacyRegionStoriesConfig()`, `storiesRegionLocaleMatches()`

## factory()
- 位置: L2530-2530
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SystemTickFeed`

## factory()
- 位置: L2536-2536
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.TelemetryFeed`

## factory()
- 位置: L2542-2542
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.FaviconFeed`

## factory()
- 位置: L2548-2548
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.TopSitesFeed`

## factory()
- 位置: L2554-2554
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.DiscoveryStreamFeed`

## factory()
- 位置: L2560-2560
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SectionsLayoutFeed`

## factory()
- 位置: L2566-2566
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.WallpaperFeed`

## factory()
- 位置: L2572-2572
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.WeatherFeed`

## factory()
- 位置: L2578-2578
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.WebNotificationsFeed`

## factory()
- 位置: L2585-2585
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.StocksFeed`

## factory()
- 位置: L2591-2591
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AdsFeed`

## factory()
- 位置: L2597-2597
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.InferredPersonalizationFeed`

## factory()
- 位置: L2604-2604
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SmartShortcutsFeed`

## factory()
- 位置: L2611-2611
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.NewTabAttributionFeed`

## factory()
- 位置: L2617-2617
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.NewTabMessaging`

## factory()
- 位置: L2623-2623
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ListsFeed`

## factory()
- 位置: L2629-2629
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PrivacyFeed`

## factory()
- 位置: L2636-2636
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.RecentSearchesFeed`

## factory()
- 位置: L2642-2642
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PictureOfTheDayFeed`

## factory()
- 位置: L2648-2648
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.TimerFeed`

## factory()
- 位置: L2654-2654
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ExternalComponentsFeed`

## ActivityStream.constructor()
- 位置: L2677-2689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.DefaultPrefs`, `lazy.RemoteRenderer`, `lazy.Store`, `this.#createdInstant`, `this._defaultPrefs`, `this._proxyRegistered`, `this.initialized`, `this.remoteRenderer`, `this.store`
- XPCOM: `Services.prefs`

## ActivityStream.createdInstant()
- 位置: L2697-2699
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#createdInstant`

## ActivityStream.feeds()
- 位置: L2701-2714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FEEDS_CONFIG.get()`, `shouldInitializeFeeds()`

## ActivityStream.init()
- 位置: L2716-2742
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `ac.BroadcastToContent()`, `lazy.NewTabActorRegistry.init()`, `this._defaultPrefs.init()`, `this._updateDynamicPrefs()`, `this.registerNetworkProxy()`, `this.store.init()`
- 参照: `at.INIT`, `at.UNINIT`, `this.feeds`, `this.initialized`, `this.locale`
- XPCOM: `Services.obs` / `Services.prefs`

## ActivityStream.registerNetworkProxy()
- 位置: L2749-2755
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!this._proxyRegistered && enabled)` → `lazy.ProxyService.registerChannelFilter()`
- 参照: `this._proxyRegistered`
- XPCOM: `Services.prefs`

## ActivityStream.unregisterNetworkProxy()
- 位置: L2760-2765
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._proxyRegistered)` → `lazy.ProxyService.unregisterChannelFilter()`
- 参照: `this._proxyRegistered`

## ActivityStream.getImageProxyConfig()
- 位置: L2772-2810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(config.imageProxyHosts || "") .split()`, `(config.imageProxyHosts || "") .split(",") .map()`, `host.trim()`, `this.store.getState()`
- 参照: `config.connectionIsolationKey`, `config.enabled`, `config.failoverProxy`, `config.imageProxyHosts`, `config.proxyAuthHeader`, `config.proxyHost`, `config.proxyPort`, `state.Prefs`, `this.initialized`, `this.store`, `values?.trainhopConfig?.imageProxy`

## ActivityStream.applyFilter()
- 位置: L2820-2855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.imageProxyHosts.includes()`, `lazy.AboutNewTabParent.loadedTabs.has()`, `this.getImageProxyConfig()`
- 条件付き依存: `if (!browser || !lazy.AboutNewTabParent.loadedTabs.has(browser))` → `callback.onProxyFilterResult()`
- 条件付き依存: `if (!config)` → `callback.onProxyFilterResult()`
- 条件付き依存: `if ( config.imageProxyHosts.includes(channel.URI.host) && channel.URI?.scheme === "https" )` → `callback.onProxyFilterResult()`
- 条件付き依存: `if ( config.imageProxyHosts.includes(channel.URI.host) && channel.URI?.scheme === "https" )` → `lazy.ProxyService.newProxyInfo()`
- 条件付き依存: `if (!( config.imageProxyHosts.includes(channel.URI.host) && channel.URI?.scheme === "https" ))` → `callback.onProxyFilterResult()`
- 参照: `browsingContext?.top?.embedderElement`, `channel.URI.host`, `channel.URI?.scheme`, `channel.loadInfo`, `config.connectionIsolationKey`, `config.failoverProxy`, `config.proxyAuthHeader`, `config.proxyHost`, `config.proxyPort`

## ActivityStream._migratePref()
- 位置: L2866-2889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.getPrefType()`, `Services.prefs.prefHasUserValue()`, `Services.prefs[prefGetter]()`, `cbIfNotDefault()`
- 参照: `Services.prefs`, `Services.prefs.PREF_BOOL`, `Services.prefs.PREF_INT`, `Services.prefs.PREF_STRING`
- XPCOM: `Services.prefs`

## ActivityStream.uninit()
- 位置: L2891-2905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.NewTabActorRegistry.uninit()`, `this.store.uninit()`, `this.unregisterNetworkProxy()`
- 条件付き依存: `if (this.geo === "")` → `Services.obs.removeObserver()`
- 参照: `lazy.Region.REGION_TOPIC`, `this.geo`, `this.initialized`
- XPCOM: `Services.obs` / `Services.prefs`

## ActivityStream._updateDynamicPrefs()
- 位置: L2907-2957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PREFS_CONFIG.get()`, `PREFS_CONFIG.keys()`, `prefConfig.getValue()`, `this._defaultPrefs.get()`
- 条件付き依存: `if (this.geo === "")` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.geo !== "")` → `Services.obs.addObserver()`
- 条件付き依存: `if (prefConfig.value !== undefined && prefConfig.value !== newValue)` → `this._defaultPrefs.set()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.Region.REGION_TOPIC`, `lazy.Region.home`, `prefConfig.getValue`, `prefConfig.value`, `this.geo`, `this.locale`
- XPCOM: `Services.locale` / `Services.obs`

## prefConfig.getValue()
- 位置: L2936-2936
- 役割: (未記入)
- 触るとき: (未記入)

## ActivityStream.observe()
- 位置: L2959-2982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateDynamicPrefs()`
- 条件付き依存: `if (data === PREF_MARKET_GATE_ENABLED)` → `this._updateDynamicPrefs()`
- 条件付き依存: `if (data === PREF_IMAGE_PROXY_ENABLED)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabled)` → `this.registerNetworkProxy()`
- 条件付き依存: `if (!(enabled))` → `this.unregisterNetworkProxy()`
- 参照: `lazy.Region.REGION_TOPIC`
- XPCOM: `Services.prefs`
