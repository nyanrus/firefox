# browser/extensions/newtab/lib/TopStoriesFeed.sys.mjs

source: browser/extensions/newtab/lib/TopStoriesFeed.sys.mjs
source-hash: 0bed6344ba11903efc06a31e98b7bf1737e68278
lines: 729

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## TopStoriesFeed.constructor()
- 位置: L44-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!this.discoveryStreamEnabled)` → `this.initializeProperties()`
- 参照: `JSON.parse(ds.value).enabled`, `ds.value`, `this.discoveryStreamEnabled`
- XPCOM: `Services.prefs`

## TopStoriesFeed.initializeProperties()
- 位置: L58-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._prefs`, `this.cache`, `this.contentUpdateQueue`, `this.propertiesInitialized`, `this.spocCampaignMap`

## TopStoriesFeed.onInit()
- 位置: async L66-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.enableSection()`, `SectionsManager.sections.get()`, `console.error()`, `this._prefs.get()`, `this.contentUpdateQueue.filter()`, `this.dispatchPocketCta()`, `this.doContentUpdate()`, `this.getApiKeyFromPref()`, `this.loadCachedData()`, `this.produceFinalEndpointUrl()`, `update()`
- 条件付き依存: `if (this.storiesLastUpdated === 0)` → `this.fetchStories()`
- 条件付き依存: `if (this.topicsLastUpdated === 0)` → `this.fetchTopics()`
- 参照: `e.message`, `options.api_key_pref`, `options.read_more_endpoint`, `options.show_spocs`, `options.stories_endpoint`, `options.stories_referrer`, `options.topics_endpoint`, `this.contentUpdateQueue`, `this.discoveryStreamEnabled`, `this.read_more_endpoint`, `this.show_spocs`, `this.storiesLastUpdated`, `this.storiesLoaded`, `this.stories_endpoint`, `this.stories_referrer`, `this.topicsLastUpdated`, `this.topics_endpoint`

## TopStoriesFeed.init()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.onceInitialized()`, `this.onInit.bind()`

## TopStoriesFeed.clearCache()
- 位置: async L117-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`

## TopStoriesFeed.uninit()
- 位置: L123-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.disableSection()`
- 参照: `this.storiesLoaded`

## TopStoriesFeed.dispatchPocketCta()
- 位置: L128-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `ac.AlsoToPreloaded()`, `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.POCKET_CTA`

## TopStoriesFeed.doContentUpdate()
- 位置: L154-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchUpdateEvent()`
- 条件付き依存: `if (!(stories))` → `this.store.getState()`
- 条件付き依存: `if (Sections && Sections.find)` → `Sections.find()`
- 条件付き依存: `if (topics)` → `Object.assign()`
- 参照: `Sections.find`, `Sections.find(s => s.id === SECTION_ID).rows`, `s.id`, `this.read_more_endpoint`, `updateProps.rows`

## TopStoriesFeed.fetchStories()
- 位置: async L175-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `console.error()`, `fetch()`, `response.json()`, `this.cache.set()`, `this.cleanUpTopRecImpressionPref()`, `this.rotate()`, `this.transform()`, `this.updateSettings()`
- 条件付き依存: `if (this.show_spocs && body.spocs)` → `body.spocs.map()`
- 条件付き依存: `if (this.show_spocs && body.spocs)` → `this.transform()`
- 条件付き依存: `if (this.show_spocs && body.spocs)` → `this.cleanUpCampaignImpressionPref()`
- 参照: `body._timestamp`, `body.recommendations`, `body.settings`, `body.spocs`, `error.message`, `response.ok`, `response.status`, `s.campaign_id`, `s.id`, `this.show_spocs`, `this.spocCampaignMap`, `this.spocs`, `this.stories`, `this.storiesLastUpdated`, `this.stories_endpoint`

## TopStoriesFeed.loadCachedData()
- 位置: async L210-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`
- 条件付き依存: `if (stories && !!stories.length && this.storiesLastUpdated === 0)` → `this.updateSettings()`
- 条件付き依存: `if (stories && !!stories.length && this.storiesLastUpdated === 0)` → `this.rotate()`
- 条件付き依存: `if (stories && !!stories.length && this.storiesLastUpdated === 0)` → `this.transform()`
- 条件付き依存: `if (data.stories.spocs && data.stories.spocs.length)` → `data.stories.spocs.map()`
- 条件付き依存: `if (data.stories.spocs && data.stories.spocs.length)` → `this.transform()`
- 条件付き依存: `if (data.stories.spocs && data.stories.spocs.length)` → `this.cleanUpCampaignImpressionPref()`
- 参照: `data.stories`, `data.stories._timestamp`, `data.stories.recommendations`, `data.stories.settings`, `data.stories.spocs`, `data.stories.spocs.length`, `data.topics`, `data.topics._timestamp`, `data.topics.topics`, `s.campaign_id`, `s.id`, `stories.length`, `this.spocCampaignMap`, `this.spocs`, `this.stories`, `this.storiesLastUpdated`, `this.topics`, `this.topicsLastUpdated`, `topics.length`

## TopStoriesFeed.transform()
- 位置: L235-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Object.assign()`, `items .filter()`, `items .filter(s => !lazy.NewTabUtils.blockedLinks.isBlocked({ url: s.url })) .map()`, `lazy.NewTabUtils.blockedLinks.isBlocked()`, `lazy.NewTabUtils.shortURL()`, `this.normalizeUrl()`
- 参照: `mapped.expiration_timestamp`, `s.campaign_id`, `s.caps`, `s.context`, `s.domain`, `s.excerpt`, `s.expiration_timestamp`, `s.icon`, `s.id`, `s.image_src`, `s.item_score`, `s.published_timestamp`, `s.title`, `s.url`, `this.compareScore`, `this.show_spocs`, `this.stories_referrer`

## TopStoriesFeed.fetchTopics()
- 位置: async L277-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `fetch()`, `response.json()`
- 条件付き依存: `if (topics)` → `Date.now()`
- 条件付き依存: `if (topics)` → `this.cache.set()`
- 参照: `body._timestamp`, `error.message`, `response.ok`, `response.status`, `this.topics`, `this.topicsLastUpdated`, `this.topics_endpoint`

## TopStoriesFeed.dispatchUpdateEvent()
- 位置: L304-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.updateSection()`

## TopStoriesFeed.compareScore()
- 位置: L308-310
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.score`, `b.score`

## TopStoriesFeed.updateSettings()
- 位置: L312-315
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `settings.recsExpireTime`, `settings.spocsPerNewTabs`, `this.recsExpireTime`, `this.spocsPerNewTabs`

## TopStoriesFeed.rotate()
- 位置: L320-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `active.concat()`, `this.readImpressionsPref()`
- 条件付き依存: `if ( impressions[item.guid] && Date.now() - impressions[item.guid] >= maxImpressionAge )` → `expired.push()`
- 条件付き依存: `if (!( impressions[item.guid] && Date.now() - impressions[item.guid] >= maxImpressionAge ))` → `active.push()`
- 参照: `item.guid`, `items.length`, `this.recsExpireTime`

## TopStoriesFeed.getApiKeyFromPref()
- 位置: L345-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `this._prefs.get()`
- XPCOM: `Services.prefs`

## TopStoriesFeed.produceFinalEndpointUrl()
- 位置: L355-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.includes()`, `url.replace()`

## TopStoriesFeed.normalizeUrl()
- 位置: L367-372
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (url)` → `url.replace(/\(/g, "%28").replace()`
- 条件付き依存: `if (url)` → `url.replace()`

## TopStoriesFeed.shouldShowSpocs()
- 位置: L374-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.show_spocs`, `this.store.getState().Prefs.values.showSponsored`

## TopStoriesFeed.dispatchSpocDone()
- 位置: L378-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`
- 参照: `at.POCKET_WAITING_FOR_SPOC`

## TopStoriesFeed.filterSpocs()
- 位置: L383-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.random()`, `spocs.filter()`, `this.isBelowFrequencyCap()`, `this.readImpressionsPref()`, `this.shouldShowSpocs()`, `this.spocs.filter()`
- 参照: `spoc.expiration_timestamp`, `this.spocs`, `this.spocs.length`, `this.spocsPerNewTabs`

## TopStoriesFeed.maybeAddSpoc()
- 位置: L417-449
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.storiesLoaded)` → `updateContent()`
- 条件付き依存: `if (!(this.storiesLoaded))` → `this.contentUpdateQueue.push()`
- 参照: `this.storiesLoaded`

## updateContent()
- 位置: L418-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `ac.OnlyToOneContent()`, `rows.splice()`, `section.rows.slice()`, `this.dispatchSpocDone()`, `this.filterSpocs()`, `this.store .getState()`, `this.store .getState() .Sections.find()`, `this.store.dispatch()`
- 条件付き依存: `if (!spocs.length)` → `this.dispatchSpocDone()`
- 参照: `at.SECTION_UPDATE`, `s.id`, `spocs.length`, `this.stories.length`

## TopStoriesFeed.isBelowFrequencyCap()
- 位置: L466-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.min()`, `campaignImpressions.filter()`
- 参照: `campaignCap.count`, `campaignCap.period`, `campaignImpressions.filter( i => Date.now() - i < campaignCap.period * 1000 ).length`, `campaignImpressions.length`, `spoc.spoc_meta.campaign_id`, `spoc.spoc_meta.caps`, `spoc.spoc_meta.caps.campaign`, `spoc.spoc_meta.caps.lifetime`

## TopStoriesFeed.cleanUpCampaignImpressionPref()
- 位置: L492-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `campaignIds.has()`, `this.cleanUpImpressionPref()`, `this.spocCampaignMap.values()`

## TopStoriesFeed.cleanUpTopRecImpressionPref()
- 位置: L502-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activeStories.has()`, `this.cleanUpImpressionPref()`, `this.stories.map()`
- 参照: `s.guid`

## TopStoriesFeed.cleanUpImpressionPref()
- 位置: L517-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(impressions).forEach()`, `isExpired()`, `this.readImpressionsPref()`
- 条件付き依存: `if (changed)` → `this.writeImpressionsPref()`

## TopStoriesFeed.recordCampaignImpression()
- 位置: L535-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Object.assign()`, `this.readImpressionsPref()`, `this.writeImpressionsPref()`, `timeStamps.push()`

## TopStoriesFeed.recordTopRecImpressions()
- 位置: L548-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.readImpressionsPref()`, `topItems.forEach()`
- 条件付き依存: `if (!impressions[t])` → `Object.assign()`
- 条件付き依存: `if (!impressions[t])` → `Date.now()`
- 条件付き依存: `if (changed)` → `this.writeImpressionsPref()`

## TopStoriesFeed.readImpressionsPref()
- 位置: L564-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `this._prefs.get()`

## TopStoriesFeed.writeImpressionsPref()
- 位置: L569-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `this._prefs.set()`

## TopStoriesFeed.removeSpocs()
- 位置: async L573-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearCache()`, `this.init()`, `this.uninit()`

## TopStoriesFeed.lazyLoadTopStories()
- 位置: L582-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `this.init()`, `this.store.getState()`
- 条件付き依存: `if (!dsPref)` → `this.store.getState()`
- 条件付き依存: `if (!userPref)` → `this.store.getState()`
- 条件付き依存: `if (!this.discoveryStreamEnabled && !this.propertiesInitialized)` → `this.initializeProperties()`
- 参照: `JSON.parse(dsPref).enabled`, `this.discoveryStreamEnabled`, `this.propertiesInitialized`, `this.store.getState().Prefs.values`, `this.storiesLoaded`

## TopStoriesFeed.handleDisabled()
- 位置: L611-636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.lazyLoadTopStories()`, `this.uninit()`
- 条件付き依存: `if (action.data.name === DISCOVERY_STREAM_PREF)` → `this.lazyLoadTopStories()`
- 条件付き依存: `if (action.data.name === DISCOVERY_STREAM_PREF_ENABLED)` → `this.lazyLoadTopStories()`
- 条件付き依存: `if (action.data.value)` → `this.lazyLoadTopStories()`
- 条件付き依存: `if (!(action.data.value))` → `this.uninit()`
- 参照: `action.data.name`, `action.data.value`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.UNINIT`

## TopStoriesFeed.onAction()
- 位置: async L638-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.doContentUpdate()`, `this.lazyLoadTopStories()`, `this.maybeAddSpoc()`, `this.uninit()`
- 条件付き依存: `if (this.discoveryStreamEnabled)` → `this.handleDisabled()`
- 条件付き依存: `if (Date.now() - this.storiesLastUpdated >= STORIES_UPDATE_TIME)` → `this.fetchStories()`
- 条件付き依存: `if (Date.now() - this.topicsLastUpdated >= TOPICS_UPDATE_TIME)` → `this.fetchTopics()`
- 条件付き依存: `if (action.data === SECTION_ID)` → `this.clearCache()`
- 条件付き依存: `if (action.data === SECTION_ID)` → `this.uninit()`
- 条件付き依存: `if (action.data === SECTION_ID)` → `this.init()`
- 条件付き依存: `if (this.spocs)` → `this.spocs.filter()`
- 条件付き依存: `if (payload.tiles && viewImpression)` → `this.shouldShowSpocs()`
- 条件付き依存: `if (this.shouldShowSpocs())` → `payload.tiles.forEach()`
- 条件付き依存: `if (this.shouldShowSpocs())` → `this.spocCampaignMap.has()`
- 条件付き依存: `if (this.spocCampaignMap.has(t.id))` → `this.recordCampaignImpression()`
- 条件付き依存: `if (this.spocCampaignMap.has(t.id))` → `this.spocCampaignMap.get()`
- 条件付き依存: `if (payload.tiles && viewImpression)` → `payload.tiles .filter(t => !this.spocCampaignMap.has(t.id)) .map()`
- 条件付き依存: `if (payload.tiles && viewImpression)` → `payload.tiles .filter()`
- 条件付き依存: `if (payload.tiles && viewImpression)` → `this.spocCampaignMap.has()`
- 条件付き依存: `if (payload.tiles && viewImpression)` → `this.recordTopRecImpressions()`
- 条件付き依存: `if (action.data.name === DISCOVERY_STREAM_PREF)` → `this.lazyLoadTopStories()`
- 条件付き依存: `if (action.data.value)` → `this.lazyLoadTopStories()`
- 条件付き依存: `if (!(action.data.value))` → `this.uninit()`
- 条件付き依存: `if (action.data.name === "showSponsored" && !action.data.value)` → `this.removeSpocs()`
- 条件付き依存: `if (action.data.name === "pocketCta")` → `this.dispatchPocketCta()`
- 参照: `action.data`, `action.data.name`, `action.data.source`, `action.data.url`, `action.data.value`, `action.meta.fromTarget`, `action.type`, `at.INIT`, `at.NEW_TAB_REHYDRATED`, `at.PLACES_LINK_BLOCKED`, `at.PREF_CHANGED`, `at.SECTION_OPTIONS_CHANGED`, `at.SYSTEM_TICK`, `at.TELEMETRY_IMPRESSION_STATS`, `at.UNINIT`, `payload.tiles`, `s.url`, `t.id`, `this.discoveryStreamEnabled`, `this.spocs`, `this.storiesLastUpdated`, `this.topicsLastUpdated`
