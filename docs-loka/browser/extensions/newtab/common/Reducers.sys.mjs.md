# browser/extensions/newtab/common/Reducers.sys.mjs

source: browser/extensions/newtab/common/Reducers.sys.mjs
source-hash: fdae2da139a69b6850ded3962129946060c8379a
lines: 1488

## <module>
- 役割: (未記入)

## App()
- 位置: L312-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `INITIAL_STATE.App`, `action.data`, `action.data?.wallpaperCategory`, `action.type`, `at.DISCOVERY_STREAM_SPOCS_UPDATE`, `at.HIDE_PERSONALIZE`, `at.INIT`, `at.SHOW_PERSONALIZE`, `at.TOP_SITES_UPDATED`, `at.WALLPAPERS_CUSTOM_SET`, `at.WEATHER_UPDATE`, `prevState.isForStartupCache`

## TopSites()
- 位置: L364-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `action.data.urls.includes()`, `prevState.rows.filter()`, `prevState.rows.map()`
- 条件付き依存: `if (row && row.url === action.data.url)` → `Object.assign()`
- 条件付き依存: `if (site && site.url === action.data.url)` → `Object.assign()`
- 条件付き依存: `if (site && action.data.urls.includes(site.url))` → `Object.assign()`
- 参照: `INITIAL_STATE.TopSites`, `action.data`, `action.data.index`, `action.data.links`, `action.data.positions`, `action.data.pref`, `action.data.preview`, `action.data.ready`, `action.data.screenshot`, `action.data.searchShortcuts`, `action.data.url`, `action.type`, `at.PLACES_BOOKMARKS_REMOVED`, `at.PLACES_BOOKMARK_ADDED`, `at.PLACES_LINKS_DELETED`, `at.PREVIEW_REQUEST`, `at.PREVIEW_REQUEST_CANCEL`, `at.PREVIEW_RESPONSE`, `at.SCREENSHOT_UPDATED`, `at.SOV_UPDATED`, `at.TOP_SITES_CANCEL_EDIT`, `at.TOP_SITES_CLOSE_SEARCH_SHORTCUTS_MODAL`, `at.TOP_SITES_EDIT`, `at.TOP_SITES_OPEN_SEARCH_SHORTCUTS_MODAL`, `at.TOP_SITES_PREFS_UPDATED`, `at.TOP_SITES_UPDATED`, `at.UPDATE_SEARCH_SHORTCUTS`, `newSite.bookmarkDateCreated`, `newSite.bookmarkGuid`, `newSite.bookmarkTitle`, `prevState.editForm`, `prevState.editForm.index`, `prevState.editForm.previewUrl`, `row.url`, `site.url`

## Dialog()
- 位置: L492-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `INITIAL_STATE.Dialog`, `action.data`, `action.type`, `at.DIALOG_CANCEL`, `at.DIALOG_CLOSE`, `at.DIALOG_OPEN`

## Prefs()
- 位置: L506-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `INITIAL_STATE.Prefs`, `action.data`, `action.data.name`, `action.data.value`, `action.data.values`, `action.type`, `at.MULTIPLE_PREFS_CHANGED`, `at.PREFS_INITIAL_VALUES`, `at.PREF_CHANGED`, `prevState.values`

## Sections()
- 位置: L527-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `action.data.dedupeConfigurations.forEach()`, `action.data.urls.includes()`, `newState.map()`, `prevState.filter()`, `prevState.map()`, `section.rows.filter()`, `section.rows.map()`
- 条件付き依存: `if (section && section.id === action.data.id)` → `Object.assign()`
- 条件付き依存: `if (!hasMatch)` → `Object.assign()`
- 条件付き依存: `if (!hasMatch)` → `newState.push()`
- 条件付き依存: `if (section && section.id === action.data.id)` → `section.rows.find()`
- 条件付き依存: `if ( action.data.rows && !!action.data.rows.length && section.rows.find(card => card.pinned) )` → `Array.from()`
- 条件付き依存: `if ( action.data.rows && !!action.data.rows.length && section.rows.find(card => card.pinned) )` → `section.rows.forEach()`
- 条件付き依存: `if (rows[index].guid !== card.guid)` → `rows.splice()`
- 条件付き依存: `if ( action.data.rows && !!action.data.rows.length && section.rows.find(card => card.pinned) )` → `Object.assign()`
- 条件付き依存: `if (section.id === dedupeConf.id)` → `dedupeConf.dedupeFrom.reduce()`
- 条件付き依存: `if (section.id === dedupeConf.id)` → `newState.find()`
- 条件付き依存: `if (section.id === dedupeConf.id)` → `dedupe.group()`
- 条件付き依存: `if (section.id === dedupeConf.id)` → `Object.assign()`
- 条件付き依存: `if (section && section.id === action.data.id && section.rows)` → `section.rows.map()`
- 条件付き依存: `if (card.url === action.data.url)` → `Object.assign()`
- 条件付き依存: `if (section && section.id === action.data.id && section.rows)` → `Object.assign()`
- 条件付き依存: `if (item.url === action.data.url)` → `Object.assign()`
- 条件付き依存: `if (action.data.urls.includes(item.url))` → `Object.assign()`
- 参照: `INITIAL_STATE.Sections`, `action.data`, `action.data.dedupeConfigurations`, `action.data.id`, `action.data.options`, `action.data.rows`, `action.data.rows.length`, `action.data.url`, `action.type`, `at.PLACES_BOOKMARKS_REMOVED`, `at.PLACES_BOOKMARK_ADDED`, `at.PLACES_LINKS_DELETED`, `at.PLACES_LINK_BLOCKED`, `at.SECTION_DEREGISTER`, `at.SECTION_REGISTER`, `at.SECTION_UPDATE`, `at.SECTION_UPDATE_CARD`, `card.guid`, `card.pinned`, `card.url`, `dedupeConf.id`, `dedupeSection.rows`, `item.url`, `newSite.bookmarkDateCreated`, `newSite.bookmarkGuid`, `newSite.bookmarkTitle`, `newSite.type`, `rows[index].guid`, `s.id`, `section.id`, `section.rows`, `site.url`

## Messages()
- 位置: L696-712
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.Messages`, `action.data.isVisible`, `action.data.message`, `action.data.portID`, `action.type`, `at.MESSAGE_SET`, `at.MESSAGE_TOGGLE_VISIBILITY`, `prevState.messageData.messageType`

## Pocket()
- 位置: L714-731
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.Pocket`, `action.data`, `action.data.cta_button`, `action.data.cta_text`, `action.data.cta_url`, `action.data.use_cta`, `action.type`, `at.POCKET_CTA`, `at.POCKET_WAITING_FOR_SPOC`

## InferredPersonalization()
- 位置: L733-760
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.InferredPersonalization`, `action.data`, `action.data.coarseInferredInterests`, `action.data.coarsePrivateInferredInterests`, `action.data.inferredInterests`, `action.data.inferredTelemetrySettingsOverrides`, `action.data.lastUpdated`, `action.type`, `at.INFERRED_PERSONALIZATION_DEBUG_FEATURES_UPDATE`, `at.INFERRED_PERSONALIZATION_RESET`, `at.INFERRED_PERSONALIZATION_UPDATE`

## DiscoveryStream()
- 位置: L763-1083
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNotReady()`, `items.filter()`, `items.map()`, `nextState()`
- 参照: `INITIAL_STATE.DiscoveryStream`, `INITIAL_STATE.DiscoveryStream.spocs`, `INITIAL_STATE.DiscoveryStream.spocs.placements`, `INITIAL_STATE.DiscoveryStream.spocs.spocs_endpoint`, `action.data`, `action.data.compactImages`, `action.data.descLines`, `action.data.feed`, `action.data.hideDescriptions`, `action.data.imageGradient`, `action.data.lastUpdated`, `action.data.layout`, `action.data.newSponsoredLabel`, `action.data.placements`, `action.data.readTime`, `action.data.spocs`, `action.data.spocsCacheUpdateTime`, `action.data.spocsOnDemand`, `action.data.titleLines`, `action.data.url`, `action.data?.card_type`, `action.data?.corpus_item_id`, `action.data?.placement_id`, `action.data?.position`, `action.data?.reporting_url`, `action.data?.scheduled_corpus_item_id`, `action.data?.section`, `action.data?.section_position`, `action.data?.title`, `action.data?.topic`, `action.data?.url`, `action.type`, `at.DISCOVERY_STREAM_CONFIG_CHANGE`, `at.DISCOVERY_STREAM_CONFIG_SETUP`, `at.DISCOVERY_STREAM_DEV_BLOCKS`, `at.DISCOVERY_STREAM_DEV_IMPRESSIONS`, `at.DISCOVERY_STREAM_EXPERIMENT_DATA`, `at.DISCOVERY_STREAM_FEEDS_UPDATE`, `at.DISCOVERY_STREAM_FEED_UPDATE`, `at.DISCOVERY_STREAM_LAYOUT_RESET`, `at.DISCOVERY_STREAM_LAYOUT_UPDATE`, `at.DISCOVERY_STREAM_LINK_BLOCKED`, `at.DISCOVERY_STREAM_PREFS_SETUP`, `at.DISCOVERY_STREAM_SPOCS_CAPS`, `at.DISCOVERY_STREAM_SPOCS_ENDPOINT`, `at.DISCOVERY_STREAM_SPOCS_ONDEMAND_LOAD`, `at.DISCOVERY_STREAM_SPOCS_ONDEMAND_RESET`, `at.DISCOVERY_STREAM_SPOCS_PLACEMENTS`, `at.DISCOVERY_STREAM_SPOCS_UPDATE`, `at.DISCOVERY_STREAM_SPOC_BLOCKED`, `at.DISCOVERY_STREAM_TOPICS_LOADING`, `at.PLACES_BOOKMARKS_REMOVED`, `at.PLACES_BOOKMARK_ADDED`, `at.REPORT_AD_OPEN`, `at.REPORT_AD_SUBMIT`, `at.REPORT_CLOSE`, `at.REPORT_CONTENT_OPEN`, `at.REPORT_CONTENT_SUBMIT`, `at.SECTION_BLOCKED`, `at.SECTION_PERSONALIZATION_UPDATE`, `at.SHOW_PRIVACY_INFO`, `at.TOPIC_SELECTION_SPOTLIGHT_CLOSE`, `at.TOPIC_SELECTION_SPOTLIGHT_OPEN`, `item.url`, `prevState.config`, `prevState.feeds`, `prevState.feeds.data`, `prevState.impressions`, `prevState.report`, `prevState.sectionPersonalization`, `prevState.spocs`, `prevState.spocs.blocked`, `prevState.spocs.frequency_caps`, `prevState.spocs.onDemand`, `prevState.spocs?.onDemand?.loaded`

## isNotReady()
- 位置: L765-766
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.data`, `prevState.feeds.loaded`, `prevState.spocs.loaded`

## handlePlacements()
- 位置: L768-795
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!placements || !placements.length)` → `[{ name: "spocs" }].forEach()`
- 条件付き依存: `if (!(!placements || !placements.length))` → `placements.forEach()`
- 参照: `placements.length`, `prevState.spocs`

## forPlacement()
- 位置: L772-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleSites()`
- 参照: `placement.name`, `placementSpocs.items`, `placementSpocs.items.length`

## nextState()
- 位置: L797-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(prevState.feeds.data).reduce()`, `handlePlacements()`, `handleSites()`
- 参照: `prevState.feeds`, `prevState.feeds.data`, `prevState.feeds.data[feed_url].data`, `prevState.feeds.data[feed_url].data.recommendations`, `prevState.spocs`

## updateBookmarkInfo()
- 位置: L989-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item.url === action.data.url)` → `Object.assign()`
- 参照: `action.data`, `action.data.url`, `item.url`

## removeBookmarkInfo()
- 位置: L1006-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.data.urls.includes()`
- 条件付き依存: `if (action.data.urls.includes(item.url))` → `Object.assign()`
- 参照: `item.url`, `newSite.bookmarkDateCreated`, `newSite.bookmarkGuid`, `newSite.bookmarkTitle`, `newSite.context_type`

## Search()
- 位置: L1085-1094
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `INITIAL_STATE.Search`, `action.type`, `at.DISABLE_SEARCH`, `at.SHOW_SEARCH`

## Wallpapers()
- 位置: L1096-1119
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.Wallpapers`, `action.data`, `action.type`, `at.WALLPAPERS_CATEGORY_SET`, `at.WALLPAPERS_CUSTOM_LIBRARY_SET`, `at.WALLPAPERS_CUSTOM_SET`, `at.WALLPAPERS_FEATURE_HIGHLIGHT_COUNTER_INCREMENT`, `at.WALLPAPERS_SET`, `at.WALLPAPER_UPLOAD_RESULT`

## SectionsLayout()
- 位置: L1121-1132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.SectionsLayout`, `action.data.configs`, `action.data.orderings`, `action.type`, `at.SECTIONS_LAYOUT_UPDATE`, `prevState.orderings`

## Notifications()
- 位置: L1134-1161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...prevState.toastQueue].filter()`
- 参照: `INITIAL_STATE.Notifications`, `action.data`, `action.data.showNotifications`, `action.data.toastData`, `action.data.toastId`, `action.type`, `at.HIDE_TOAST_MESSAGE`, `at.SHOW_TOAST_MESSAGE`, `prevState.toastCounter`, `prevState.toastQueue`, `queuedToasts.length`

## addWebNotification()
- 位置: L1164-1176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originIds.includes()`
- 参照: `prevState.byOrigin`, `prevState.notifications`

## removeWebNotifications()
- 位置: L1179-1194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(byOrigin[origin] || []).filter()`
- 参照: `prevState.byOrigin`, `prevState.notifications`, `remaining.length`

## WebNotifications()
- 位置: L1196-1216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addWebNotification()`, `removeWebNotifications()`
- 参照: `INITIAL_STATE.WebNotifications`, `action.data`, `action.data.byOrigin`, `action.data.lastUpdated`, `action.data.notification`, `action.data.notifications`, `action.data.removed`, `action.type`, `at.WEB_NOTIFICATIONS_ADDED`, `at.WEB_NOTIFICATIONS_ERROR`, `at.WEB_NOTIFICATIONS_REMOVED`, `at.WEB_NOTIFICATIONS_UPDATED`

## Weather()
- 位置: L1218-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.Weather`, `action.data`, `action.data.hourlyForecasts`, `action.data.lastUpdated`, `action.data.locationData`, `action.data.suggestions`, `action.type`, `at.WEATHER_LOCATION_DATA_UPDATE`, `at.WEATHER_LOCATION_SEARCH_UPDATE`, `at.WEATHER_LOCATION_SUGGESTIONS_UPDATE`, `at.WEATHER_SEARCH_ACTIVE`, `at.WEATHER_UPDATE`, `prevState.locationData`

## PictureOfTheDay()
- 位置: L1242-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.PictureOfTheDay`, `action.data.author`, `action.data.description`, `action.data.error`, `action.data.imageUrl`, `action.data.lastUpdated`, `action.data.licenseLabel`, `action.data.licenseUrl`, `action.data.publishedDate`, `action.data.sourceUrl`, `action.data.thumbnailUrl`, `action.data.title`, `action.type`, `at.PICTURE_OF_THE_DAY_UPDATE`

## PrivacyWidget()
- 位置: L1265-1279
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.PrivacyWidget`, `action.data`, `action.type`, `at.WIDGETS_PRIVACY_UPDATE`

## RecentSearches()
- 位置: L1281-1292
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.RecentSearches`, `action.data`, `action.type`, `at.WIDGETS_RECENT_SEARCHES_UPDATE`, `prevState.initialized`

## Ads()
- 位置: L1294-1317
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.Ads`, `action.data.spocPlacements`, `action.data.spocs`, `action.data.tiles`, `action.type`, `at.ADS_INIT`, `at.ADS_RESET`, `at.ADS_UPDATE_SPOCS`, `at.ADS_UPDATE_TILES`

## TimerWidget()
- 位置: L1319-1393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`
- 参照: `INITIAL_STATE.TimerWidget`, `action.data`, `action.data.duration`, `action.data.timerType`, `action.data?.timerType`, `action.type`, `at.WIDGETS_TIMER_END`, `at.WIDGETS_TIMER_PAUSE`, `at.WIDGETS_TIMER_PLAY`, `at.WIDGETS_TIMER_RESET`, `at.WIDGETS_TIMER_SET`, `at.WIDGETS_TIMER_SET_DURATION`, `at.WIDGETS_TIMER_SET_TYPE`, `prevState.timerType`, `prevState[timerType]?.isRunning`

## Stocks()
- 位置: L1395-1438
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.Stocks`, `action.data.error`, `action.data.lastUpdated`, `action.data.matches`, `action.data.query`, `action.data.reconciledSymbols`, `action.data.requestId`, `action.data.status`, `action.data.tickers`, `action.data.watchlistTickers`, `action.type`, `at.WIDGETS_STOCKS_SEARCH_CLEAR`, `at.WIDGETS_STOCKS_SEARCH_RESPONSE`, `at.WIDGETS_STOCKS_SEARCH_STARTED`, `at.WIDGETS_STOCKS_UPDATE`, `at.WIDGETS_STOCKS_WATCHLIST_UPDATE`, `prevState.activeRequestId`

## ListsWidget()
- 位置: L1440-1449
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.ListsWidget`, `action.data`, `action.type`, `at.WIDGETS_LISTS_SET`, `at.WIDGETS_LISTS_SET_SELECTED`

## ExternalComponents()
- 位置: L1451-1461
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `INITIAL_STATE.ExternalComponents`, `action.data`, `action.type`, `at.REFRESH_EXTERNAL_COMPONENTS`
