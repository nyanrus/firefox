# browser/extensions/newtab/lib/DiscoveryStreamFeed.sys.mjs

source: browser/extensions/newtab/lib/DiscoveryStreamFeed.sys.mjs
source-hash: d9f035acfd2d361815be3c5082794b7d5dd1907c
lines: 3127

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/protocol;1?name=http"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## DiscoveryStreamFeed.constructor()
- 位置: L159-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onPocketExperimentUpdated.bind()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.PersistentCache`, `this._prefCache`, `this.adsClient`, `this.cache`, `this.loaded`, `this.locale`, `this.onPocketExperimentUpdated`
- XPCOM: `Services.locale`

## DiscoveryStreamFeed.onPocketExperimentUpdated()
- 位置: L173-180
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( reason !== "feature-experiment-loaded" && reason !== "feature-rollout-loaded" )` → `this.pocketNewTabExperimentChanged()`

## DiscoveryStreamFeed.pocketNewTabExperimentChanged()
- 位置: L182-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`, `this.store.dispatch()`
- 参照: `at.INFERRED_PERSONALIZATION_CLEAR_INTEREST_VECTOR`

## DiscoveryStreamFeed.config()
- 位置: L190-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `console.error()`, `this.store.getState()`
- 参照: `this._prefCache.config`, `this._prefCache.config.enabled`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.resetConfigDefauts()
- 位置: L214-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.dispatch()`
- 参照: `at.CLEAR_PREF`

## DiscoveryStreamFeed.region()
- 位置: L223-225
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.Region.home`

## DiscoveryStreamFeed.isContextualAds()
- 位置: L227-247
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._isContextualAds === undefined)` → `this.store.getState()`
- 参照: `state.Prefs.values`, `this._isContextualAds`

## DiscoveryStreamFeed.doLocalInferredRerank()
- 位置: L249-272
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._doLocalInferredRerank === undefined)` → `this.store.getState()`
- 参照: `state.Prefs.values`, `state.Prefs.values.inferredPersonalizationConfig ?.local_popular_today_rerank`, `this._doLocalInferredRerank`, `this.store.getState().InferredPersonalization ?.inferredTelemetrySettingsOverrides?.local_popular_today_rerank`

## DiscoveryStreamFeed.showSponsoredStories()
- 位置: L274-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.showStories()
- 位置: L282-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpaceOverridden()`, `this.store.getState()`
- 参照: `SPACE_IDS.STORIES`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.sectionsOrderingKey()
- 位置: L294-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `prefs.trainhopConfig?.sections?.ordering`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.sectionsAdAllowedRanks()
- 位置: L305-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Number.isInteger()`, `ranks.some()`, `this.store.getState()`
- 条件付き依存: `if (!Array.isArray(ranks))` → `pref.split(",").map()`
- 条件付き依存: `if (!Array.isArray(ranks))` → `pref.split()`
- 参照: `lazy.SectionsLayoutManager.AD_ALLOWED_RANKS`, `prefs.trainhopConfig?.sections?.adAllowedRanks`, `ranks?.length`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed._resolveLayoutOverride()
- 位置: L327-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `names.every()`, `sections.some()`, `this.store.getState()`
- 条件付き依存: `if (names?.length && names.every(name => configs[name]))` → `names.map()`
- 参照: `lazy.SectionsLayoutManager.DEFAULT_SECTION_LAYOUT`, `names?.length`, `prefs.trainhopConfig?.clientLayout?.enabled`, `section.layout`, `this.sectionsOrderingKey`, `this.store.getState().Prefs.values`, `this.store.getState().SectionsLayout`

## DiscoveryStreamFeed._applySectionLayouts()
- 位置: L363-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SectionsLayoutManager.DEFAULT_SECTION_LAYOUT.slice()`, `lazy.maskLayoutAds()`, `override.slice()`, `sections.forEach()`, `sections.sort()`, `this._resolveLayoutOverride()`
- 参照: `a.receivedRank`, `b.receivedRank`, `cycleLayouts.length`, `override.length`, `section.layout`, `sections.length`, `this.sectionsAdAllowedRanks`

## DiscoveryStreamFeed.setupConfig()
- 位置: L395-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_CONFIG_SETUP`, `this.config`

## DiscoveryStreamFeed.setupDevtoolsState()
- 位置: async L408-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`, `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_DEV_BLOCKS`, `at.DISCOVERY_STREAM_DEV_IMPRESSIONS`, `cachedData.recsBlocks`, `cachedData.recsImpressions`

## DiscoveryStreamFeed.setupPrefs()
- 位置: L430-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToPreloaded()`, `ac.BroadcastToContent()`, `hideDescriptionsRegions?.includes()`, `lazy.NimbusFeatures.pocketNewtab.getEnrollmentMetadata()`, `nimbusConfig.hideDescriptionsRegions ?.split()`, `nimbusConfig.hideDescriptionsRegions ?.split(",") .map()`, `s.trim()`, `this.configureFollowedSections()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `at.DISCOVERY_STREAM_EXPERIMENT_DATA`, `at.DISCOVERY_STREAM_PREFS_SETUP`, `experimentMetadata?.branch`, `experimentMetadata?.slug`, `nimbusConfig.compactImages`, `nimbusConfig.descLines`, `nimbusConfig.hideDescriptions`, `nimbusConfig.imageGradient`, `nimbusConfig.newSponsoredLabel`, `nimbusConfig.readTime`, `nimbusConfig.titleLines`, `this.store.getState().Prefs.values`, `this.store.getState().Prefs.values?.pocketConfig`

## DiscoveryStreamFeed.configureFollowedSections()
- 位置: async L488-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `ac.BroadcastToContent()`, `this.cache.get()`, `this.store.dispatch()`, `this.store.getState()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `followedSectionsString.split(",").map()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `followedSectionsString.split()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `s.trim()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `blockedSectionsString.split(",").map()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `blockedSectionsString.split()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `Array.from(sectionTopics).reduce()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `Array.from()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `followedSections.includes()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `blockedSections.includes()`
- 条件付き依存: `if ( sectionPersonalization && Object.keys(sectionPersonalization).length === 0 )` → `this.cache.set()`
- 参照: `Object.keys(sectionPersonalization).length`, `at.SECTION_PERSONALIZATION_UPDATE`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.uninitPrefs()
- 位置: L539-542
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._prefCache`

## DiscoveryStreamFeed.fetchFromEndpoint()
- 位置: async L544-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `allowed.some()`, `clearTimeout()`, `console.error()`, `controller.abort()`, `endpoint.startsWith()`, `item.trim()`, `response.json()`, `setTimeout()`, `this.store .getState()`, `this.store .getState() .Prefs.values[PREF_ENDPOINTS].split()`, `this.store .getState() .Prefs.values[PREF_ENDPOINTS].split(",") .map()`, `this.store .getState() .Prefs.values[PREF_ENDPOINTS].split(",") .map(item => item.trim()) .filter()`
- 条件付き依存: `if (!endpoint)` → `console.error()`
- 条件付き依存: `if (useOhttp && ohttpConfigURL && ohttpRelayURL)` → `lazy.ObliviousHTTP.getOHTTPConfig()`
- 条件付き依存: `if (!config)` → `console.error()`
- 条件付き依存: `if (options.headers && options.headers instanceof Headers)` → `Object.fromEntries()`
- 条件付き依存: `if (useOhttp && ohttpConfigURL && ohttpRelayURL)` → `lazy.ObliviousHTTP.ohttpRequest()`
- 条件付き依存: `if (!(useOhttp && ohttpConfigURL && ohttpRelayURL))` → `fetch()`
- 参照: `error.message`, `options.headers`, `response.ok`, `response.status`, `this.store .getState() .Prefs.values`
- XPCOM: `Services.prefs`

## DiscoveryStreamFeed._fetchSpocsWithAdsClient()
- 位置: async L634-701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `lazy.AdsClient.requestOptions()`, `placementSpocs.map()`, `placements.map()`, `requests.push()`, `spocs.entries()`, `spocs.entries().map()`, `this.adsClient.requestSpocAds()`, `this.store.getState()`
- 条件付き依存: `if (content)` → `content.taxonomy.replace("-", "").replace()`
- 条件付き依存: `if (content)` → `content.taxonomy.replace()`
- 参照: `content.categories`, `lazy.MozAdsIabContent`, `lazy.MozAdsIabContentTaxonomy`, `lazy.MozAdsPlacementRequestWithCount`, `p.placement`, `spoc.blockKey`, `spoc.callbacks`, `spoc.caps`, `spoc.caps.capKey`, `spoc.caps.day`, `spoc.domain`, `spoc.excerpt`, `spoc.format`, `spoc.imageUrl`, `spoc.ranking`, `spoc.ranking.itemScore`, `spoc.ranking.personalizationModels`, `spoc.ranking.priority`, `spoc.sponsor`, `spoc.sponsoredByOverride`, `spoc.title`, `spoc.url`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.spocsOnDemand()
- 位置: L703-713
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._spocsOnDemand === undefined)` → `this.store.getState()`
- 参照: `spocsOnDemandConfig.enabled`, `this._spocsOnDemand`, `this.showSponsoredStories`, `this.store.getState().Prefs`, `values.trainhopConfig?.spocsOnDemand`

## DiscoveryStreamFeed.spocsCacheUpdateTime()
- 位置: L715-743
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._spocsCacheUpdateTime === undefined)` → `this.store.getState()`
- 参照: `spocsOnDemandConfig.timeout`, `this._spocsCacheUpdateTime`, `this.spocsOnDemand`, `this.store.getState().Prefs`, `values.trainhopConfig?.spocsOnDemand`

## DiscoveryStreamFeed.isExpired()
- 位置: L754-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.store.getState()`
- 参照: `feed.lastUpdated`, `feed.sectionsEnabled`, `spocs.lastUpdated`, `this.spocsCacheUpdateTime`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed._checkExpirationPerComponent()
- 位置: async L784-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(feeds).some()`, `this.cache.get()`, `this.isExpired()`
- 参照: `this.showSponsoredStories`, `this.showStories`

## DiscoveryStreamFeed.updatePlacements()
- 位置: L801-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `layout.filter()`, `row.components.filter()`, `sendUpdate()`
- 条件付き依存: `if (placement?.name && !placementsMap[placement.name])` → `placements.push()`
- 参照: `at.DISCOVERY_STREAM_SPOCS_PLACEMENTS`, `c.placement`, `c.spocs`, `component.placement`, `placement.name`, `placement?.name`, `r.components`, `r.components.length`, `this.showSponsoredStories`

## DiscoveryStreamFeed.addEndpointQuery()
- 位置: L839-852
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `params.entries()`, `urlObject.searchParams.append()`, `urlObject.toString()`

## DiscoveryStreamFeed.parseGridPositions()
- 位置: L854-875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `csvPositions.map()`, `isNaN()`, `parseInt()`

## DiscoveryStreamFeed.generateFeedUrl()
- 位置: L877-881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## DiscoveryStreamFeed.loadLayout()
- 位置: L883-1013
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getHardcodedLayout()`, `pocketConfig.ctaButtonSponsors ?.split()`, `pocketConfig.ctaButtonSponsors ?.split(",") .map()`, `pocketConfig.widgetPositions?.split()`, `prepConfArr()`, `s.trim()`, `s.trim().toLowerCase()`, `sendUpdate()`, `this.generateFeedUrl()`, `this.locale.startsWith()`, `this.parseGridPositions()`, `this.store.getState()`, `this.store.getState().Prefs.values[PREF_SPOC_POSITIONS]?.split()`
- 条件付き依存: `if (spocSiteId)` → `newUrl.searchParams.set()`
- 条件付き依存: `if (layoutData.spocs)` → `this.store.getState()`
- 条件付き依存: `if (layoutData.spocs)` → `this.addEndpointQuery()`
- 条件付き依存: `if ( url && url !== this.store.getState().DiscoveryStream.spocs.spocs_endpoint )` → `sendUpdate()`
- 条件付き依存: `if ( url && url !== this.store.getState().DiscoveryStream.spocs.spocs_endpoint )` → `this.updatePlacements()`
- 参照: `at.DISCOVERY_STREAM_LAYOUT_UPDATE`, `at.DISCOVERY_STREAM_SPOCS_ENDPOINT`, `layoutData.layout`, `layoutData.spocs`, `layoutData.spocs.url`, `newUrl.href`, `pocketConfig.compactGrid`, `pocketConfig.ctaButtonVariant`, `pocketConfig.fourCardLayout`, `pocketConfig.hideCardBackground`, `pocketConfig.hybridLayout`, `pocketConfig.newFooterSection`, `pocketConfig.pocketStoriesHeadlineId`, `pocketConfig.spocAdTypes`, `pocketConfig.spocZoneIds`, `spocAdTypes?.length`, `spocZoneIds?.length`, `this.config.hardcoded_basic_layout`, `this.store.getState().DiscoveryStream.spocs.spocs_endpoint`, `this.store.getState().Prefs.values`, `this.store.getState().Prefs.values?.pocketConfig`

## prepConfArr()
- 位置: L923-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `arr ?.split()`, `arr ?.split(",") .filter()`, `arr ?.split(",") .filter(item => item) .map()`, `parseInt()`

## DiscoveryStreamFeed.buildFeedPromise()
- 位置: L1024-1066
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!newFeeds[url])` → `this.getComponentFeed()`
- 条件付き依存: `if (!newFeeds[url])` → `feedPromise .then()`
- 条件付き依存: `if (!newFeeds[url])` → `this.filterRecommendations()`
- 条件付き依存: `if (!newFeeds[url])` → `sendUpdate()`
- 条件付き依存: `if (!newFeeds[url])` → `console.error()`
- 条件付き依存: `if (!newFeeds[url])` → `newFeedsPromises.push()`
- 参照: `at.DISCOVERY_STREAM_FEED_UPDATE`, `component.feed`

## DiscoveryStreamFeed.filterRecommendations()
- 位置: L1071-1089
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (feed?.data?.recommendations?.length)` → `feed.data.recommendations.filter()`
- 条件付き依存: `if (feed?.data?.recommendations?.length)` → `lazy.NewTabUtils.blockedLinks.isBlocked()`
- 参照: `feed.data`, `feed?.data?.recommendations?.length`, `item.url`

## DiscoveryStreamFeed.reduceFeedComponents()
- 位置: L1099-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.components .filter()`, `row.components .filter(component => component && component.feed) .forEach()`, `this.buildFeedPromise()`
- 参照: `component.feed`

## DiscoveryStreamFeed.buildFeedPromises()
- 位置: L1116-1124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `layout .filter()`, `layout .filter(row => row && row.components) .reduce()`, `this.reduceFeedComponents()`
- 参照: `row.components`

## DiscoveryStreamFeed.loadComponentFeeds()
- 位置: async L1126-1148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `sendUpdate()`, `this.buildFeedPromises()`, `this.cache.set()`, `this.store.getState()`
- 参照: `DiscoveryStream.layout`, `at.DISCOVERY_STREAM_FEEDS_UPDATE`

## DiscoveryStreamFeed.getPlacements()
- 位置: L1150-1153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().DiscoveryStream.spocs`

## DiscoveryStreamFeed.placementsForEach()
- 位置: L1157-1159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPlacements()`, `this.getPlacements().forEach()`

## DiscoveryStreamFeed.normalizeSpocsItems()
- 位置: L1172-1223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `spocs.map()`
- 参照: `spoc.alt_text`, `spoc.attributions`, `spoc.block_key`, `spoc.callbacks`, `spoc.caps?.cap_key`, `spoc.caps?.day`, `spoc.domain`, `spoc.excerpt`, `spoc.format`, `spoc.image_url`, `spoc.ranking?.item_score`, `spoc.ranking?.personalization_models`, `spoc.ranking?.priority`, `spoc.sponsor`, `spoc.title`, `spoc.url`, `spocs.context`, `spocs.items`, `spocs.sponsor`, `spocs.title`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.getContextualAdsPlacements()
- 位置: L1227-1319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(feeds).find()`, `getContextualCountPref()`, `getContextualStringPref()`, `placementSpocsArray.map()`, `this.store.getState()`
- 条件付き依存: `if (recsFeed)` → `recsFeed.data.sections.sort()`
- 条件付き依存: `if (recsFeed)` → `iabSections.reduce()`
- 条件付き依存: `if (recsFeed)` → `section.layout.responsiveLayouts[0].tiles .filter(tile => tile.hasAd) .map()`
- 条件付き依存: `if (recsFeed)` → `section.layout.responsiveLayouts[0].tiles .filter()`
- 条件付き依存: `if (billboardEnabled)` → `bannerPlacementsArray.map()`
- 条件付き依存: `if (leaderboardEnabled)` → `bannerPlacementsArray.map()`
- 参照: `a.receivedRank`, `b.receivedRank`, `feed?.data?.sections?.length`, `iabSections[billboardPosition - 2].iab`, `iabSections[billboardPosition - 2]?.iab`, `iabSections[leaderboardPosition - 2].iab`, `iabSections[leaderboardPosition - 2]?.iab`, `section.iab`, `section.layout.responsiveLayouts`, `state.DiscoveryStream.feeds.data`, `state.Prefs.values`, `tile.hasAd`

## getContextualStringPref()
- 位置: L1235-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `s.trim()`, `state.Prefs.values[prefName] ?.split()`, `state.Prefs.values[prefName] ?.split(",") .map()`, `state.Prefs.values[prefName] ?.split(",") .map(s => s.trim()) .filter()`
- 参照: `state.Prefs.values`

## getContextualCountPref()
- 位置: L1242-1248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`, `s.trim()`, `state.Prefs.values[prefName] ?.split()`, `state.Prefs.values[prefName] ?.split(`,`) .map()`, `state.Prefs.values[prefName] ?.split(`,`) .map(s => s.trim()) .filter()`, `state.Prefs.values[prefName] ?.split(`,`) .map(s => s.trim()) .filter(item => item) .map()`
- 参照: `state.Prefs.values`

## DiscoveryStreamFeed.getSimpleAdsPlacements()
- 位置: L1323-1337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`, `placementsArray.map()`, `s.trim()`, `state.Prefs.values[PREF_SPOC_COUNTS]?.split()`, `state.Prefs.values[PREF_SPOC_COUNTS]?.split(`,`) .map()`, `state.Prefs.values[PREF_SPOC_COUNTS]?.split(`,`) .map(s => s.trim()) .filter()`, `state.Prefs.values[PREF_SPOC_COUNTS]?.split(`,`) .map(s => s.trim()) .filter(item => item) .map()`, `state.Prefs.values[PREF_SPOC_PLACEMENTS]?.split()`, `state.Prefs.values[PREF_SPOC_PLACEMENTS]?.split(`,`) .map()`, `state.Prefs.values[PREF_SPOC_PLACEMENTS]?.split(`,`) .map(s => s.trim()) .filter()`, `this.store.getState()`
- 参照: `state.Prefs.values`

## DiscoveryStreamFeed.getAdsPlacements()
- 位置: L1339-1346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSimpleAdsPlacements()`
- 条件付き依存: `if (this.isContextualAds)` → `this.getContextualAdsPlacements()`
- 参照: `this.isContextualAds`

## DiscoveryStreamFeed.updateOrRemoveSpocs()
- 位置: async L1348-1366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`, `this.loadSpocs()`, `this.store.getState()`, `this.updatePlacements()`
- 条件付き依存: `if (!this.showSponsoredStories)` → `this.clearSpocs()`
- 参照: `this.showSponsoredStories`, `this.store.getState().DiscoveryStream.layout`

## dispatch()
- 位置: L1349-1350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`

## DiscoveryStreamFeed.loadSpocs()
- 位置: async L1369-1612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `sendUpdate()`, `this.cache.get()`, `this.getPlacements()`, `this.isExpired()`, `this.store.getState()`
- 条件付き依存: `if (placements?.length)` → `headers.append()`
- 条件付き依存: `if (placements?.length)` → `this.store.getState()`
- 条件付き依存: `if (unifiedAdsEnabled && !adsFeedEnabled)` → `this.getAdsPlacements()`
- 条件付き依存: `if (marsOhttpEnabled)` → `this.fetchFromEndpoint()`
- 条件付き依存: `if (preFlight)` → `headers.append()`
- 条件付き依存: `if (unifiedAdsEnabled && !adsFeedEnabled)` → `this.store.getState()`
- 条件付き依存: `if (unifiedAdsEnabled && !adsFeedEnabled)` → `lazy.ContextId.request()`
- 条件付き依存: `if (unifiedAdsEnabled && !adsFeedEnabled)` → `blockedSponsors.split()`
- 条件付き依存: `if (this.adsClient)` → `this._fetchSpocsWithAdsClient()`
- 条件付き依存: `if (!(this.adsClient))` → `this.fetchFromEndpoint()`
- 条件付き依存: `if (!(this.adsClient))` → `JSON.stringify()`
- 条件付き依存: `if (!(adsFeedEnabled))` → `console.error()`
- 条件付き依存: `if (spocsResponse)` → `Date.now()`
- 条件付き依存: `if (spocsResponse)` → `this.getPlacements().map()`
- 条件付き依存: `if (spocsResponse)` → `this.getPlacements()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `unifiedAdsPlacements.reduce()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `accumulator.concat()`
- 条件付き依存: `if (spocsResponse)` → `this.normalizeSpocsItems()`
- 条件付き依存: `if (spocsResponse)` → `this.migrateFlightId()`
- 条件付き依存: `if (spocsResponse)` → `this.frequencyCapSpocs()`
- 条件付き依存: `if (spocsResponse)` → `this.filterBlocked()`
- 条件付き依存: `if (!this.isContextualAds)` → `( await Promise.all( items.map(item => this.normalizeScore(item)) ) ) // Sort by highest scores. .sort()`
- 条件付き依存: `if (!this.isContextualAds)` → `Promise.all()`
- 条件付き依存: `if (!this.isContextualAds)` → `items.map()`
- 条件付き依存: `if (!this.isContextualAds)` → `this.normalizeScore()`
- 条件付き依存: `if (spocsResponse)` → `Promise.all()`
- 条件付き依存: `if (spocsResponse)` → `this.cleanUpFlightImpressionPref()`
- 条件付き依存: `if (!(spocsResponse))` → `console.error()`
- 条件付き依存: `if (!this.adsClient)` → `this.cache.set()`
- 参照: `at.DISCOVERY_STREAM_SPOCS_UPDATE`, `cachedData.spocs`, `currentValue.placement`, `lazy.userAgent`, `normalizedSpocsItems.length`, `placement.name`, `placements.length`, `placements?.length`, `preFlight.geo_location`, `preFlight.geoname_id`, `preFlight.normalized_ua`, `spocsState.lastUpdated`, `spocsState.spocs`, `state.Ads`, `state.DiscoveryStream.spocs.spocs_endpoint`, `state.Prefs.values`, `this.adsClient`, `this.isContextualAds`, `this.showSponsoredStories`, `this.sortItem`, `this.spocsCacheUpdateTime`, `this.spocsOnDemand`, `this.store.getState().Prefs.values`, `this.store.getState().Prefs.values?.adsBackendConfig`, `unifiedAdsPlacements.length`

## DiscoveryStreamFeed.clearSpocs()
- 位置: async L1614-1654
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `headers.append()`, `lazy.ContextId.request()`, `this.fetchFromEndpoint()`, `this.store.getState()`
- 条件付き依存: `if (lazy.ContextId.rotationEnabled)` → `lazy.ContextId.forceRotation()`
- 参照: `lazy.ContextId.rotationEnabled`, `state.Prefs.values`

## DiscoveryStreamFeed.sortItem()
- 位置: L1668-1684
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.priority`, `a.score`, `b.priority`, `b.score`

## DiscoveryStreamFeed.scoreItemsInferred()
- 位置: async L1686-1722
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.doLocalInferredRerank)` → `this.store.getState()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `Object.entries(inferredInterests).reduce()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `Object.entries()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `Number.isFinite()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `Number.isInteger()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `Promise.all()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `items.map()`
- 条件付き依存: `if (this.doLocalInferredRerank)` → `scoreItemInferred()`
- 条件付き依存: `if (!(this.doLocalInferredRerank))` → `(await Promise.all(items.map(item => this.normalizeScore(item)))) // Sort by highest scores. .sort()`
- 条件付き依存: `if (!(this.doLocalInferredRerank))` → `Promise.all()`
- 条件付き依存: `if (!(this.doLocalInferredRerank))` → `items.map()`
- 条件付き依存: `if (!(this.doLocalInferredRerank))` → `this.normalizeScore()`
- 参照: `this.doLocalInferredRerank`, `this.sortItem`, `this.store.getState().InferredPersonalization`, `this.store.getState().Prefs.values?.inferredPersonalizationConfig ?.local_inferred_weight`, `this.store.getState().Prefs.values?.inferredPersonalizationConfig ?.server_inferred_weight`

## DiscoveryStreamFeed.normalizeScore()
- 位置: async L1724-1730
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `item.item_score`, `item.score`

## DiscoveryStreamFeed.filterBlocked()
- 位置: async L1732-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (data?.length)` → `this.readDataPref()`
- 条件付き依存: `if (data?.length)` → `this.cache.get()`
- 条件付き依存: `if (data?.length)` → `data.filter()`
- 条件付き依存: `if (data?.length)` → `lazy.NewTabUtils.blockedLinks.isBlocked()`
- 参照: `cachedData.recsBlocks`, `data?.length`, `item.flight_id`, `item.id`, `item.url`

## DiscoveryStreamFeed.migrateFlightId()
- 位置: L1756-1780
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (spocs && spocs.length)` → `spocs.map()`
- 参照: `s.campaign_id`, `s.caps`, `s.caps.campaign`, `s.caps.flight`, `s.flight_id`, `spocs.length`

## DiscoveryStreamFeed.frequencyCapSpocs()
- 位置: L1787-1808
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (spocs?.length)` → `this.readDataPref()`
- 条件付き依存: `if (spocs?.length)` → `spocs.filter()`
- 条件付き依存: `if (spocs?.length)` → `this.isBelowFrequencyCap()`
- 条件付き依存: `if (!isBelow)` → `caps.push()`
- 条件付き依存: `if (caps.length)` → `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_SPOCS_CAPS`, `caps.length`, `spocs?.length`

## DiscoveryStreamFeed.isBelowFrequencyCap()
- 位置: L1825-1850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 条件付き依存: `if (flightCap)` → `flightImpressions.filter()`
- 条件付き依存: `if (flightCap)` → `Date.now()`
- 参照: `flightCap.count`, `flightCap.period`, `flightImpressions.filter(i => Date.now() - i < flightCap.period * 1000) .length`, `flightImpressions.length`, `spoc.caps`, `spoc.caps.flight`, `spoc.caps.lifetime`, `spoc.flight_id`

## DiscoveryStreamFeed.retryFeed()
- 位置: async L1852-1864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.getComponentFeed()`, `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_FEED_UPDATE`

## DiscoveryStreamFeed.getExperimentInfo()
- 位置: L1866-1879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pocketNewtab.getEnrollmentMetadata()`
- 参照: `experimentMetadata?.branch`, `experimentMetadata?.slug`

## DiscoveryStreamFeed.getComponentFeed()
- 位置: async L1882-2061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`, `this.isExpired()`, `this.store.getState()`
- 条件付き依存: `if (this.isExpired({ cachedData, key: "feed", url: feedUrl, isStartup }))` → `this.formatComponentFeedRequest()`
- 条件付き依存: `if (this.isExpired({ cachedData, key: "feed", url: feedUrl, isStartup }))` → `this.fetchFromEndpoint()`
- 条件付き依存: `if (feedResponse)` → `feedResponse.data.map()`
- 条件付き依存: `if (sectionsEnabled)` → `Object.entries()`
- 条件付き依存: `if (sectionData)` → `recommendations.push()`
- 条件付き依存: `if (sectionData)` → `sections.push()`
- 条件付き依存: `if (sectionsEnabled)` → `this._applySectionLayouts()`
- 条件付き依存: `if (feedResponse)` → `this.scoreItemsInferred()`
- 条件付き依存: `if (sections.length)` → `sections .filter(({ visible }) => visible) .sort((a, b) => a.receivedRank - b.receivedRank) .map()`
- 条件付き依存: `if (sections.length)` → `sections .filter(({ visible }) => visible) .sort()`
- 条件付き依存: `if (sections.length)` → `sections .filter()`
- 条件付き依存: `if (sections.length)` → `this.store.dispatch()`
- 条件付き依存: `if (sections.length)` → `ac.SetPref()`
- 条件付き依存: `if ( feedResponse.interestPicker && feedResponse.interestPicker.sections )` → `feedResponse.interestPicker.sections.map()`
- 条件付き依存: `if ( feedResponse.interestPicker && feedResponse.interestPicker.sections )` → `sections.find()`
- 条件付き依存: `if (feedResponse.inferredLocalModel)` → `this.store.dispatch()`
- 条件付き依存: `if (feedResponse.inferredLocalModel)` → `ac.AlsoToMain()`
- 条件付き依存: `if (feedResponse)` → `this.cleanUpTopRecImpressions()`
- 条件付き依存: `if (feedResponse)` → `this.rotate()`
- 条件付き依存: `if (feedResponse)` → `this.filterBlocked()`
- 条件付き依存: `if (feedResponse)` → `Date.now()`
- 条件付き依存: `if (!(feedResponse))` → `console.error()`
- 条件付き依存: `if (feed?.data?.surfaceId)` → `Glean.newtabContent.surfaceId.set()`
- 条件付き依存: `if (prefs[PREF_PRIVATE_PING_ENABLED] && feed?.data?.surfaceId)` → `this.store.dispatch()`
- 条件付き依存: `if (prefs[PREF_PRIVATE_PING_ENABLED] && feed?.data?.surfaceId)` → `ac.SetPref()`
- 参照: `a.receivedRank`, `at.INFERRED_PERSONALIZATION_MODEL_UPDATE`, `b.receivedRank`, `cachedData.sectionPersonalization`, `feed.data.surfaceId`, `feed?.data?.surfaceId`, `feedResponse.feeds`, `feedResponse.inferredLocalModel`, `feedResponse.interestPicker`, `feedResponse.interestPicker.sections`, `feedResponse.recommendedAt`, `feedResponse.surfaceId`, `found?.followable`, `found?.title`, `item.corpusItemId`, `item.excerpt`, `item.features`, `item.iconUrl`, `item.imageUrl`, `item.isTimeSensitive`, `item.publisher`, `item.receivedRank`, `item.scheduledCorpusItemId`, `item.serverScore`, `item.sourceSectionId`, `item.tileId`, `item.title`, `item.topic`, `item.url`, `item.variantId`, `section.sectionKey`, `sectionData.allowAds`, `sectionData.followable`, `sectionData.iab`, `sectionData.isInitiallyVisible`, `sectionData.layout`, `sectionData.receivedFeedRank`, `sectionData.recommendations`, `sectionData.subtitle`, `sectionData.title`, `sections.length`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.formatComponentFeedRequest()
- 位置: L2063-2142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.entries()`, `Object.entries(sectionPersonalization).map()`, `Services.prefs.getBoolPref()`, `headers.append()`, `lazy.NewTabUtils.getUtcOffset()`, `s.trim()`, `this.getExperimentInfo()`, `this.store.getState()`, `topicsString .split()`, `topicsString .split(",") .map()`, `topicsString .split(",") .map(s => s.trim()) .filter()`
- 条件付き依存: `if (inferredPersonalization && merinoOhttpEnabled)` → `this.store.getState()`
- 条件付き依存: `if (prefs[PREF_INFERRED_INTERESTS_OVERRIDE])` → `JSON.parse()`
- 条件付き依存: `if (prefs[PREF_INFERRED_INTERESTS_OVERRIDE])` → `console.error()`
- 参照: `body.feeds`, `data.followedAt`, `data.isBlocked`, `data.isFollowed`, `prefs.inferredPersonalizationConfig ?.normalized_time_zone_offset`, `this.locale`, `this.region`, `this.store.getState().InferredPersonalization ?.coarsePrivateInferredInterests`, `this.store.getState().Prefs.values`
- XPCOM: `Services.prefs`

## DiscoveryStreamFeed._maybeUpdateCachedData()
- 位置: async L2147-2156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._checkExpirationPerComponent()`
- 条件付き依存: `if (expirationPerComponent.spocs)` → `this.loadSpocs()`
- 条件付き依存: `if (expirationPerComponent.feeds)` → `this.loadComponentFeeds()`
- 参照: `expirationPerComponent.feeds`, `expirationPerComponent.spocs`, `this.store.dispatch`

## DiscoveryStreamFeed.scoreFeeds()
- 位置: async L2158-2195
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (feedsState.data)` → `Object.keys(feedsState.data).map()`
- 条件付き依存: `if (feedsState.data)` → `Object.keys()`
- 条件付き依存: `if (feed.personalized)` → `Promise.resolve()`
- 条件付き依存: `if (feedsState.data)` → `this.scoreItemsInferred()`
- 条件付き依存: `if (feedsState.data)` → `feedPromise.then()`
- 条件付き依存: `if (feedsState.data)` → `this.store.dispatch()`
- 条件付き依存: `if (feedsState.data)` → `ac.AlsoToPreloaded()`
- 条件付き依存: `if (feedsState.data)` → `Promise.all()`
- 条件付き依存: `if (feedsState.data)` → `this.cache.set()`
- 参照: `at.DISCOVERY_STREAM_FEED_UPDATE`, `feed.data`, `feed.data.recommendations`, `feed.personalized`, `feedsState.data`

## DiscoveryStreamFeed.refreshAll()
- 位置: async L2206-2244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.loadLayout()`, `this.store.dispatch()`
- 条件付き依存: `if (this.showStories)` → `this.store.getState()`
- 条件付き依存: `if (!(this.spocsOnDemand && isSystemTick))` → `this.loadSpocs( dispatch, isStartup && spocsStartupCacheEnabled ).catch()`
- 条件付き依存: `if (!(this.spocsOnDemand && isSystemTick))` → `this.loadSpocs()`
- 条件付き依存: `if (!(this.spocsOnDemand && isSystemTick))` → `console.error()`
- 条件付き依存: `if (!(this.spocsOnDemand && isSystemTick))` → `promises.push()`
- 条件付き依存: `if (this.showStories)` → `this.loadComponentFeeds(dispatch, isStartup).catch()`
- 条件付き依存: `if (this.showStories)` → `this.loadComponentFeeds()`
- 条件付き依存: `if (this.showStories)` → `console.error()`
- 条件付き依存: `if (this.showStories)` → `promises.push()`
- 条件付き依存: `if (this.showStories)` → `Promise.all()`
- 条件付き依存: `if (isStartup)` → `this._maybeUpdateCachedData()`
- 参照: `this.showStories`, `this.spocsOnDemand`, `this.store.dispatch`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.rotate()
- 位置: async L2249-2271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `active.concat()`, `this.cache.get()`
- 条件付き依存: `if ( impressions[item.id] && Date.now() - impressions[item.id] >= DEFAULT_RECS_ROTATION_TIME )` → `expired.push()`
- 条件付き依存: `if (!( impressions[item.id] && Date.now() - impressions[item.id] >= DEFAULT_RECS_ROTATION_TIME ))` → `active.push()`
- 参照: `cachedData.recsImpressions`, `item.id`

## DiscoveryStreamFeed.enableStories()
- 位置: L2273-2278
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.config.enabled)` → `this.refreshAll()`
- 参照: `this.config.enabled`

## DiscoveryStreamFeed.enable()
- 位置: async L2280-2283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.refreshAll()`
- 参照: `this.loaded`

## DiscoveryStreamFeed.reset()
- 位置: async L2285-2289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetCache()`, `this.resetDataPrefs()`, `this.resetState()`

## DiscoveryStreamFeed.resetCache()
- 位置: async L2291-2293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetAllCache()`

## DiscoveryStreamFeed.resetContentCache()
- 位置: async L2295-2299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`

## DiscoveryStreamFeed.resetBlocks()
- 位置: async L2301-2312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`, `this.cache.set()`, `this.refreshAll()`, `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_DEV_BLOCKS`, `cachedData.recsBlocks`

## DiscoveryStreamFeed.resetContentFeed()
- 位置: async L2314-2316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`

## DiscoveryStreamFeed.resetSpocs()
- 位置: async L2318-2320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`

## DiscoveryStreamFeed.resetAllCache()
- 位置: async L2322-2329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetContentCache()`
- 参照: `this._doLocalInferredRerank`, `this._isContextualAds`, `this._spocsCacheUpdateTime`, `this._spocsOnDemand`

## DiscoveryStreamFeed.resetDataPrefs()
- 位置: L2331-2334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.writeDataPref()`

## DiscoveryStreamFeed.resetState()
- 位置: L2336-2343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.setupPrefs()`, `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_LAYOUT_RESET`, `this.loaded`

## DiscoveryStreamFeed.onPrefChange()
- 位置: async L2345-2352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.reset()`
- 条件付き依存: `if (this.config.enabled)` → `this.enable()`
- 参照: `this.config.enabled`

## DiscoveryStreamFeed.configReset()
- 位置: L2358-2366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_CONFIG_CHANGE`, `this._prefCache.config`, `this.config`

## DiscoveryStreamFeed.recordFlightImpression()
- 位置: L2368-2376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.readDataPref()`, `this.writeDataPref()`, `timeStamps.push()`

## DiscoveryStreamFeed.recordTopRecImpression()
- 位置: async L2378-2391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`
- 条件付き依存: `if (!impressions[recId])` → `Date.now()`
- 条件付き依存: `if (!impressions[recId])` → `this.cache.set()`
- 条件付き依存: `if (!impressions[recId])` → `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_DEV_IMPRESSIONS`, `cachedData.recsImpressions`

## DiscoveryStreamFeed.recordBlockRecId()
- 位置: async L2393-2406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`
- 条件付き依存: `if (!blocks[recId])` → `this.cache.set()`
- 条件付き依存: `if (!blocks[recId])` → `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_DEV_BLOCKS`, `cachedData.recsBlocks`

## DiscoveryStreamFeed.recordBlockFlightId()
- 位置: L2408-2438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.readDataPref()`, `this.store.getState()`
- 条件付き依存: `if (!flights[flightId])` → `this.writeDataPref()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `this.store.getState()`
- 条件付き依存: `if (blockList !== "")` → `blockList .split(",") .map(s => s.trim()) .filter()`
- 条件付き依存: `if (blockList !== "")` → `blockList .split(",") .map()`
- 条件付き依存: `if (blockList !== "")` → `blockList .split()`
- 条件付き依存: `if (blockList !== "")` → `s.trim()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `blockedAdsArray.push()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `this.store.dispatch()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `ac.SetPref()`
- 条件付き依存: `if (unifiedAdsEnabled)` → `blockedAdsArray.join()`
- 参照: `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.cleanUpFlightImpressionPref()
- 位置: L2440-2457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.map()`, `this.placementsForEach()`
- 条件付き依存: `if (flightIds && flightIds.length)` → `this.cleanUpImpressionPref()`
- 条件付き依存: `if (flightIds && flightIds.length)` → `flightIds.includes()`
- 参照: `flightIds.length`, `newSpocs.items`, `placement.name`, `s.flight_id`

## DiscoveryStreamFeed.cleanUpTopRecImpressions()
- 位置: async L2460-2466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.cleanUpImpressionCache()`

## DiscoveryStreamFeed.writeDataPref()
- 位置: L2468-2470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `ac.SetPref()`, `this.store.dispatch()`

## DiscoveryStreamFeed.readDataPref()
- 位置: L2472-2475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.cleanUpImpressionCache()
- 位置: async L2477-2499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`
- 条件付き依存: `if (impressions)` → `Object.keys(impressions).forEach()`
- 条件付き依存: `if (impressions)` → `Object.keys()`
- 条件付き依存: `if (impressions)` → `isExpired()`
- 条件付き依存: `if (changed)` → `this.cache.set()`
- 条件付き依存: `if (changed)` → `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_DEV_IMPRESSIONS`

## DiscoveryStreamFeed.cleanUpImpressionPref()
- 位置: L2501-2515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(impressions).forEach()`, `isExpired()`, `this.readDataPref()`
- 条件付き依存: `if (changed)` → `this.writeDataPref()`

## DiscoveryStreamFeed.retreiveProfileAge()
- 位置: async L2517-2524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ProfileAge()`, `new Date().getTime()`
- 参照: `profileAccessor.created`

## DiscoveryStreamFeed.topicSelectionImpressionEvent()
- 位置: L2526-2535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.SetPref()`, `new Date().getTime()`, `this.store.dispatch()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.topicSelectionMaybeLaterEvent()
- 位置: async L2537-2547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.SetPref()`, `this.retreiveProfileAge()`, `this.store.dispatch()`

## DiscoveryStreamFeed.onSpocsOnDemandUpdate()
- 位置: async L2549-2558
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.spocsOnDemand)` → `this._checkExpirationPerComponent()`
- 条件付き依存: `if (expirationPerComponent.spocs)` → `this.loadSpocs()`
- 条件付き依存: `if (expirationPerComponent.spocs)` → `this.store.dispatch()`
- 条件付き依存: `if (expirationPerComponent.spocs)` → `ac.BroadcastToContent()`
- 参照: `expirationPerComponent.spocs`, `this.spocsOnDemand`

## DiscoveryStreamFeed.onSystemTick()
- 位置: async L2560-2581
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._checkExpirationPerComponent()`
- 条件付き依存: `if (expired)` → `this.refreshAll()`
- 参照: `expirationPerComponent.feeds`, `expirationPerComponent.spocs`, `this.config.enabled`, `this.loaded`, `this.spocsOnDemand`

## DiscoveryStreamFeed.onTrainhopConfigChanged()
- 位置: async L2583-2592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpacesAssigned()`, `this.resetSpocsOnDemand()`, `this.store.getState()`
- 条件付き依存: `if (isSpacesAssigned(prefs) && this.showStories)` → `this.enableStories()`
- 参照: `this.showStories`, `this.store.getState().Prefs.values`

## DiscoveryStreamFeed.onPrefChangedAction()
- 位置: async L2594-2679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `setTimeout()`, `this.cache.set()`, `this.configReset()`, `this.loadLayout()`, `this.refreshAll()`, `this.resetContentCache()`, `this.resetContentFeed()`, `this.resetSpocsOnDemand()`, `this.store.dispatch()`, `this.updateOrRemoveSpocs()`
- 条件付き依存: `if (!this.showStories)` → `this.clearSpocs()`
- 条件付き依存: `if (action.data.value)` → `this.enableStories()`
- 条件付き依存: `if (action.data.name === "pocketConfig")` → `this.onPrefChange()`
- 条件付き依存: `if (action.data.name === "pocketConfig")` → `this.setupPrefs()`
- 条件付き依存: `if (action.data.name === "trainhopConfig")` → `this.onTrainhopConfigChanged()`
- 参照: `action.data.name`, `action.data.value`, `at.DISCOVERY_STREAM_LAYOUT_RESET`, `at.DISCOVERY_STREAM_TOPICS_LOADING`, `this._doLocalInferredRerank`, `this._isContextualAds`, `this.showStories`

## DiscoveryStreamFeed.resetSpocsOnDemand()
- 位置: L2681-2693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.dispatch()`
- 参照: `at.DISCOVERY_STREAM_SPOCS_ONDEMAND_RESET`, `this._spocsCacheUpdateTime`, `this._spocsOnDemand`, `this.spocsCacheUpdateTime`, `this.spocsOnDemand`

## DiscoveryStreamFeed.onAction()
- 位置: async L2695-2975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `JSON.stringify()`, `Object.keys()`, `ac.BroadcastToContent()`, `ac.SetPref()`, `lazy.AdsClient.isEnabled()`, `lazy.NimbusFeatures.pocketNewtab.offUpdate()`, `lazy.NimbusFeatures.pocketNewtab.onUpdate()`, `lazy.RemoteSettings.pollChanges()`, `this.cache.set()`, `this.configReset()`, `this.filterBlocked()`, `this.loadLayout()`, `this.onPrefChange()`, `this.onPrefChangedAction()`, `this.onSpocsOnDemandUpdate()`, `this.onSystemTick()`, `this.reset()`, `this.resetBlocks()`, `this.resetConfigDefauts()`, `this.resetContentCache()`, `this.retryFeed()`, `this.setupConfig()`, `this.setupDevtoolsState()`, `this.setupPrefs()`, `this.store.dispatch()`, `this.store.getState()`, `this.topicSelectionImpressionEvent()`, `this.topicSelectionMaybeLaterEvent()`, `this.uninitPrefs()`, `this.updateOrRemoveSpocs()`
- 条件付き依存: `if (lazy.AdsClient.isEnabled(this.store.getState().Prefs.values))` → `lazy.AdsClient.getClient()`
- 条件付き依存: `if (this.config.enabled)` → `this.enable()`
- 条件付き依存: `if ( action.data.tiles && action.data.tiles[0] && action.data.tiles[0].id )` → `this.recordTopRecImpression()`
- 条件付き依存: `if (this.showSponsoredStories)` → `this.recordFlightImpression()`
- 条件付き依存: `if (this.showSponsoredStories)` → `this.store.getState()`
- 条件付き依存: `if (this.showSponsoredStories)` → `this.placementsForEach()`
- 条件付き依存: `if (this.showSponsoredStories)` → `this.frequencyCapSpocs()`
- 条件付き依存: `if (frequencyCapped.length)` → `this.cache.set()`
- 条件付き依存: `if (frequencyCapped.length)` → `this.store.dispatch()`
- 条件付き依存: `if (frequencyCapped.length)` → `ac.AlsoToPreloaded()`
- 条件付き依存: `if (spocs && spocs.items && spocs.items.length)` → `spocs.items.filter()`
- 条件付き依存: `if (!blocked)` → `blockedResults.push()`
- 条件付き依存: `if (blockedItems.length)` → `this.cache.set()`
- 条件付き依存: `if (blockedItems.length)` → `this.store.dispatch()`
- 条件付き依存: `if (blockedItems.length)` → `ac.AlsoToPreloaded()`
- 条件付き依存: `if (blockedItems.length)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (flight_id)` → `this.recordBlockFlightId()`
- 条件付き依存: `if (tile_id)` → `this.recordBlockRecId()`
- 参照: `action.data`, `action.data.feed`, `action.data.flightId`, `action.data.name`, `action.data.tiles`, `action.data.tiles[0].id`, `action.data.url`, `action.data.value`, `action.type`, `at.ADS_UPDATE_SPOCS`, `at.BLOCK_URL`, `at.DISCOVERY_STREAM_CONFIG_CHANGE`, `at.DISCOVERY_STREAM_CONFIG_RESET`, `at.DISCOVERY_STREAM_CONFIG_RESET_DEFAULTS`, `at.DISCOVERY_STREAM_CONFIG_SET_VALUE`, `at.DISCOVERY_STREAM_DEV_BLOCKS_RESET`, `at.DISCOVERY_STREAM_DEV_EXPIRE_CACHE`, `at.DISCOVERY_STREAM_DEV_REFRESH_CACHE`, `at.DISCOVERY_STREAM_DEV_SHOW_PLACEHOLDER`, `at.DISCOVERY_STREAM_DEV_SYNC_RS`, `at.DISCOVERY_STREAM_DEV_SYSTEM_TICK`, `at.DISCOVERY_STREAM_IMPRESSION_STATS`, `at.DISCOVERY_STREAM_LINK_BLOCKED`, `at.DISCOVERY_STREAM_RETRY_FEED`, `at.DISCOVERY_STREAM_SPOCS_ONDEMAND_UPDATE`, `at.DISCOVERY_STREAM_SPOCS_UPDATE`, `at.DISCOVERY_STREAM_SPOC_BLOCKED`, `at.DISCOVERY_STREAM_SPOC_IMPRESSION`, `at.INFERRED_PERSONALIZATION_MODEL_UPDATE`, `at.INIT`, `at.PLACES_LINK_BLOCKED`, `at.PREF_CHANGED`, `at.SECTION_PERSONALIZATION_SET`, `at.SECTION_PERSONALIZATION_UPDATE`, `at.SYSTEM_TICK`, `at.TOPIC_SELECTION_IMPRESSION`, `at.TOPIC_SELECTION_MAYBE_LATER`, `at.UNINIT`, `blockedItems.length`, `feed.data`, `feed.data.recommendations`, `feedsState.data`, `frequencyCapped.length`, `placement.name`, `s.url`, `spocs.items`, `spocs.items.length`, `spocsState.data`, `spocsState.lastUpdated`, `this.adsClient`, `this.config.enabled`, `this.onPocketExperimentUpdated`, `this.showSponsoredStories`, `this.spocsCacheUpdateTime`, `this.spocsOnDemand`, `this.store.getState().DiscoveryStream.feeds`, `this.store.getState().DiscoveryStream.spocs`, `this.store.getState().Prefs.values`

## getHardcodedLayout()
- 位置: L2996-3126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `spocPositions.map()`, `widgetPositions.map()`
- 参照: `spocPlacementData.ad_types`, `spocPlacementData.zone_ids`
