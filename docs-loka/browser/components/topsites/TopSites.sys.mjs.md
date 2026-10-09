# browser/components/topsites/TopSites.sys.mjs

source: browser/components/topsites/TopSites.sys.mjs
source-hash: d71acc56c1ec22a82167d698c92685a6aa953d1a
lines: 1395

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## getShortHostnameForCurrentSearch()
- 位置: L72-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortHostname()`
- 参照: `lazy.SearchService.defaultEngine.searchUrlDomain`

## _TopSites.constructor()
- 位置: L90-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `this.handlePlacesEvents.bind()`
- 参照: `lazy.LinksCache`, `lazy.NewTabUtils.activityStreamLinks`, `lazy.NewTabUtils.pinnedLinks`, `newOptions.numItems`, `oldOptions.numItems`, `this._dedupeKey`, `this._faviconProvider`, `this._tippyTopProvider`, `this.dedupe`, `this.frecentCache`, `this.handlePlacesEvents`, `this.pinnedCache`

## _TopSites.init()
- 位置: async L120-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.#addObservers()`, `this._readDefaults()`, `this.updateCustomSearchShortcuts()`
- 参照: `this.#initPromise`

## _TopSites.uninit()
- 位置: L137-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.#removeObservers()`, `this.frecentCache.expire()`, `this.pinnedCache.expire()`
- 参照: `this.#initPromise`, `this.#searchShortcuts`, `this.#sites`

## _TopSites.#addObservers()
- 位置: L147-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `lazy.PlacesUtils.observers.addListener()`
- 参照: `this.#hasObservers`, `this.handlePlacesEvents`
- XPCOM: `Services.obs` / `Services.prefs`

## _TopSites.#removeObservers()
- 位置: L169-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.PlacesUtils.observers.removeListener()`
- 参照: `this.#hasObservers`, `this.handlePlacesEvents`
- XPCOM: `Services.obs` / `Services.prefs`

## _TopSites._reset()
- 位置: L190-196
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cu.isInAutomation`, `this.#searchShortcuts`, `this.#sites`

## _TopSites.observe()
- 位置: L198-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `data.startsWith()`, `this._readDefaults()`, `this.frecentCache.expire()`, `this.pinnedCache.expire()`, `this.refresh()`
- 条件付き依存: `if ( data === "engine-default" && Services.prefs.getBoolPref(NO_DEFAULT_SEARCH_TILE_PREF, true) )` → `getShortHostnameForCurrentSearch()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF))` → `this.updateCustomSearchShortcuts()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF)))` → `this.unpinAllSearchShortcuts()`
- 条件付き依存: `if (data.startsWith(DEFAULT_SITES_EXPERIMENTS_PREF_BRANCH))` → `this._readDefaults()`
- 参照: `this._currentSearchHostname`
- XPCOM: `Services.prefs`

## _TopSites.handlePlacesEvents()
- 位置: L252-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.frecentCache.expire()`, `this.refresh()`, `url.startsWith()`
- 条件付き依存: `if (isRemovedFromStore)` → `this.frecentCache.expire()`
- 条件付き依存: `if (isRemovedFromStore)` → `this.refresh()`
- 条件付き依存: `if ( isTagging || (itemType === lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK && source !== lazy.PlacesUtils.bookmarks.SOURCES.IMPORT && source !== lazy.PlacesUtils.b...)` → `this.frecentCache.expire()`
- 条件付き依存: `if ( isTagging || (itemType === lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK && source !== lazy.PlacesUtils.bookmarks.SOURCES.IMPORT && source !== lazy.PlacesUtils.b...)` → `this.refresh()`
- 参照: `lazy.PlacesUtils.bookmarks.SOURCES.IMPORT`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE_ON_STARTUP`, `lazy.PlacesUtils.bookmarks.SOURCES.SYNC`, `lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK`

## _TopSites.getSites()
- 位置: async L320-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredClone()`, `this.init()`
- 参照: `this.#sites`

## _TopSites.getSearchShortcuts()
- 位置: async L325-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredClone()`, `this.init()`
- 参照: `this.#searchShortcuts`

## _TopSites._dedupeKey()
- 位置: L330-332
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `site.hostname`

## _TopSites._readDefaults()
- 位置: async L337-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DEFAULT_TOP_SITES.push()`, `Services.prefs.getBoolPref()`, `Services.prefs.prefIsLocked()`, `lazy.NewTabUtils.shortURL()`, `this._getRemoteConfig()`, `this.refresh()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(REMOTE_SETTING_DEFAULTS_PREF))` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(REMOTE_SETTING_DEFAULTS_PREF))` → `this.refreshDefaults()`
- 条件付き依存: `if ( Services.prefs.prefIsLocked(DEFAULT_SITES_OVERRIDE_PREF) || Cu.isInAutomation )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if ( Services.prefs.prefIsLocked(DEFAULT_SITES_OVERRIDE_PREF) || Cu.isInAutomation )` → `this.refreshDefaults()`
- 条件付き依存: `if (siteData.search_shortcut)` → `this.topSiteToSearchTopSite()`
- 参照: `Cu.isInAutomation`, `DEFAULT_TOP_SITES.length`, `link.label`, `link.url_urlbar`, `siteData.search_shortcut`, `siteData.title`, `siteData.url`, `siteData.url_urlbar_override`, `this._useRemoteSetting`
- XPCOM: `Services.prefs`

## _TopSites.refreshDefaults()
- 位置: async L387-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.refresh()`
- 条件付き依存: `if (sites)` → `sites.split()`
- 条件付き依存: `if (sites)` → `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if (sites)` → `DEFAULT_TOP_SITES.push()`
- 参照: `DEFAULT_TOP_SITES.length`, `site.hostname`

## _TopSites._getRemoteConfig()
- 位置: async L406-489
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

## _TopSites.shouldFilterSearchTile()
- 位置: L497-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SEARCH_FILTERS.includes()`, `Services.prefs.getBoolPref()`
- 参照: `this._currentSearchHostname`
- XPCOM: `Services.prefs`

## _TopSites._maybeInsertSearchShortcuts()
- 位置: async L515-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Services.prefs .getStringPref(SEARCH_SHORTCUTS_HAVE_PINNED_PREF, "") .split(",") .filter()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Services.prefs .getStringPref(SEARCH_SHORTCUTS_HAVE_PINNED_PREF, "") .split()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Services.prefs .getStringPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `DEFAULT_TOP_SITES.filter(s => s.searchTopSite).map()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `DEFAULT_TOP_SITES.filter()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Services.prefs.getStringPref(SEARCH_SHORTCUTS_ENGINES, "").split()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `shouldPin .map(getSearchProvider) .filter()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `shouldPin .map()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `shouldPin.every()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `prevInsertedShortcuts.includes()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Math.max()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `[...plainPinnedSites].concat()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Array(emptySlots).fill()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `Array()`
- 条件付き依存: `if (Services.prefs.getBoolPref(TOP_SITE_SEARCH_SHORTCUTS_PREF, true))` → `tryToInsertSearchShortcut()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `prevInsertedShortcuts.concat(newInsertedShortcuts).join()`
- 条件付き依存: `if (newInsertedShortcuts.length)` → `prevInsertedShortcuts.concat()`
- 参照: `newInsertedShortcuts.length`, `plainPinnedSites.length`, `s.hostname`, `s.searchTopSite`, `s.shortURL`, `shortcut.shortURL`, `this._currentSearchHostname`, `this._useRemoteSetting`
- XPCOM: `Services.prefs`

## tryToInsertSearchShortcut()
- 位置: async L553-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkHasSearchEngine()`, `lazy.NewTabUtils.shortURL()`, `pinnedSites.find()`, `pinnedSites.indexOf()`, `prevInsertedShortcuts.includes()`
- 条件付き依存: `if ( !pinnedSites.find( s => s && lazy.NewTabUtils.shortURL(s) === shortcut.shortURL ) && !prevInsertedShortcuts.includes(shortcut.shortURL) && nextAvailable > -...)` → `this.topSiteToSearchTopSite()`
- 条件付き依存: `if ( !pinnedSites.find( s => s && lazy.NewTabUtils.shortURL(s) === shortcut.shortURL ) && !prevInsertedShortcuts.includes(shortcut.shortURL) && nextAvailable > -...)` → `this._pinSiteAt()`
- 条件付き依存: `if ( !pinnedSites.find( s => s && lazy.NewTabUtils.shortURL(s) === shortcut.shortURL ) && !prevInsertedShortcuts.includes(shortcut.shortURL) && nextAvailable > -...)` → `newInsertedShortcuts.push()`
- 参照: `shortcut.keyword`, `shortcut.shortURL`, `shortcut.url`

## _TopSites.getLinksWithDefaults()
- 位置: async L590-779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Promise.all()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `frecent.find()`, `getSearchProvider()`, `insertPinned()`, `lazy.FilterAdult.filter()`, `lazy.NewTabUtils.blockedLinks.isBlocked()`, `lazy.NewTabUtils.shortURL()`, `lazy.PlacesUtils.history.pageFrecencyThreshold()`, `lazy.SearchService.init()`, `notBlockedDefaultSites.find()`, `notBlockedDefaultSites.push()`, `plainPinned.map()`, `this._maybeInsertSearchShortcuts()`, `this.dedupe.group()`, `this.frecentCache.request()`, `this.pinnedCache.request()`, `this.shouldFilterSearchTile()`, `this.topSiteToSearchTopSite()`, `withPinned.slice()`
- 条件付き依存: `if (!this.shouldFilterSearchTile(hostname))` → `frecent.push()`
- 条件付き依存: `if (!this.shouldFilterSearchTile(hostname))` → `this.topSiteToSearchTopSite()`
- 条件付き依存: `if (await this._maybeInsertSearchShortcuts(plainPinned))` → `this.pinnedCache.expire()`
- 条件付き依存: `if (await this._maybeInsertSearchShortcuts(plainPinned))` → `this.pinnedCache.request()`
- 条件付き依存: `if (link.searchTopSite)` → `getSearchProvider()`
- 条件付き依存: `if (link.searchTopSite)` → `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if (link.searchTopSite)` → `checkHasSearchEngine()`
- 条件付き依存: `if (!copy.favicon)` → `lazy.NewTabUtils.activityStreamProvider._faviconBytesToDataURI()`
- 条件付き依存: `if (!copy.favicon)` → `lazy.NewTabUtils.activityStreamProvider._addFavicons()`
- 条件付き依存: `if (!copy.favicon)` → `copy.__sharedCache.updateLink()`
- 条件付き依存: `if (link.searchTopSite && !link.isDefault)` → `this._tippyTopProvider.processSite()`
- 条件付き依存: `if (!(link.searchTopSite && !link.isDefault))` → `this._fetchIcon()`
- 参照: `SEARCH_FILTERS.length`, `copy.favicon`, `link.__sharedCache`, `link.hostname`, `link.isDefault`, `link.searchTopSite`, `link.typedBonus`, `link.url`, `searchProvider.keyword`, `searchProvider.url`, `this.#sites`
- XPCOM: `Services.prefs`

## finder()
- 位置: L711-711
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `link.url`, `other.url`

## _TopSites.refresh()
- 位置: async L787-806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this.getLinksWithDefaults()`
- 条件付き依存: `if (!this._tippyTopProvider.initialized)` → `this._tippyTopProvider.init()`
- 参照: `options.isStartup`, `this._refreshing`, `this._startedUp`, `this._tippyTopProvider.initialized`
- XPCOM: `Services.obs`

## _TopSites.updateCustomSearchShortcuts()
- 位置: async L808-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CUSTOM_SEARCH_SHORTCUTS.find()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `engine.aliases.includes()`, `lazy.SearchService.getAppProvidedEngines()`
- 条件付き依存: `if (!this._tippyTopProvider.initialized)` → `this._tippyTopProvider.init()`
- 条件付き依存: `if (shortcut)` → `this._tippyTopProvider.processSite()`
- 条件付き依存: `if (shortcut)` → `searchShortcuts.push()`
- 参照: `s.keyword`, `this.#searchShortcuts`, `this._tippyTopProvider.initialized`
- XPCOM: `Services.obs` / `Services.prefs`

## _TopSites.topSiteToSearchTopSite()
- 位置: async L845-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkHasSearchEngine()`, `getSearchProvider()`, `lazy.NewTabUtils.shortURL()`
- 参照: `searchProvider.keyword`

## _TopSites._fetchIcon()
- 位置: async L863-877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._requestRichIcon()`, `this._tippyTopProvider.processSite()`
- 参照: `link.favicon`, `link.faviconSize`, `link.tippyTopIcon`, `link.url`

## _TopSites._requestRichIcon()
- 位置: L879-881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._faviconProvider.fetchIcon()`

## _TopSites._broadcastPinnedSitesUpdated()
- 位置: L886-892
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pinnedCache.expire()`, `this.refresh()`

## _TopSites._pinSiteAt()
- 位置: async L901-910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.pinnedLinks.pin()`
- 参照: `toPin.label`, `toPin.searchTopSite`

## _TopSites.pin()
- 位置: async L915-932
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._adjustPinIndexForSponsoredLinks()`
- 条件付き依存: `if (index >= 0)` → `this._pinSiteAt()`
- 条件付き依存: `if (index >= 0)` → `this._broadcastPinnedSitesUpdated()`
- 条件付き依存: `if (index === -1)` → `lazy.NewTabUtils.blockedLinks.unblock()`
- 条件付き依存: `if (index === -1)` → `this.frecentCache.expire()`
- 条件付き依存: `if (!(index >= 0))` → `this.insert()`
- 参照: `action.data`, `site.url`

## _TopSites.unpin()
- 位置: L937-941
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.pinnedLinks.unpin()`, `this._broadcastPinnedSitesUpdated()`
- 参照: `action.data`

## _TopSites.unpinAllSearchShortcuts()
- 位置: L943-951
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `this.pinnedCache.expire()`
- 条件付き依存: `if (pinnedLink && pinnedLink.searchTopSite)` → `lazy.NewTabUtils.pinnedLinks.unpin()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links`, `pinnedLink.searchTopSite`
- XPCOM: `Services.prefs`

## _TopSites._unpinSearchShortcut()
- 位置: L953-974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.shortURL()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `lazy.NewTabUtils.pinnedLinks.unpin()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `this.pinnedCache.expire()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `Services.prefs.setStringPref()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `prevInsertedShortcuts.filter(s => s !== vendor).join()`
- 条件付き依存: `if ( pinnedLink && pinnedLink.searchTopSite && lazy.NewTabUtils.shortURL(pinnedLink) === vendor )` → `prevInsertedShortcuts.filter()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links`, `pinnedLink.searchTopSite`
- XPCOM: `Services.prefs`

## _TopSites._adjustPinIndexForSponsoredLinks()
- 位置: L981-995
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `link.sponsored_position`, `site.url`, `this.#sites`, `this.#sites[i]?.url`

## _TopSites._insertPin()
- 位置: L1000-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `this._adjustPinIndexForSponsoredLinks()`
- 条件付き依存: `if (!pinned[index])` → `this._pinSiteAt()`
- 条件付き依存: `if (!(!pinned[index]))` → `this._pinSiteAt()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links`
- XPCOM: `Services.prefs`

## _TopSites.insert()
- 位置: async L1046-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `this._broadcastPinnedSitesUpdated()`, `this._insertPin()`
- 参照: `action.data`, `action.data.draggedFromIndex`, `action.data.site`
- XPCOM: `Services.prefs`

## _TopSites.updatePinnedSearchShortcuts()
- 位置: L1067-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `addedShortcuts.forEach()`, `deletedShortcuts.forEach()`, `lazy.NewTabUtils.pinnedLinks.links.findIndex()`, `lazy.NewTabUtils.pinnedLinks.unpin()`, `this._broadcastPinnedSitesUpdated()`
- 条件付き依存: `if (index >= 0)` → `lazy.NewTabUtils.pinnedLinks.pin()`
- 条件付き依存: `if (!(index >= 0))` → `this._insertPin()`
- 参照: `lazy.NewTabUtils.pinnedLinks.links.length`
- XPCOM: `Services.prefs`

## insertPinned()
- 位置: L1106-1134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `links.filter()`, `newLinks.map()`, `pinned.forEach()`, `pinned.map()`, `pinnedUrls.includes()`
- 条件付き依存: `if (!(index > newLinks.length))` → `newLinks.splice()`
- 参照: `link.isPinned`, `link.pinIndex`, `link.url`, `newLinks.length`

## FaviconProvider.constructor()
- 位置: L1141-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._queryForRedirects`

## FaviconProvider.fetchIcon()
- 位置: async L1151-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `getDomain()`, `iconUri.mutate()`, `iconUri.mutate().setRef()`, `iconUri.mutate().setRef("tippytop").finalize()`, `this.#setFaviconForPage()`, `this.getSite()`
- 条件付き依存: `if (!site)` → `this._queryForRedirects.has()`
- 条件付き依存: `if (!this._queryForRedirects.has(url))` → `this._queryForRedirects.add()`
- 条件付き依存: `if (!this._queryForRedirects.has(url))` → `Services.tm.idleDispatchToMainThread()`
- 条件付き依存: `if (!this._queryForRedirects.has(url))` → `this.fetchIconFromRedirects()`
- 参照: `site.image_url`, `this.shouldFetchIcons`
- XPCOM: `Services.io` / `Services.tm`

## FaviconProvider.getSite()
- 位置: async L1177-1183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tippyTop.get()`
- 参照: `sites.length`

## FaviconProvider.tippyTop()
- 位置: L1188-1193
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._tippyTop)` → `lazy.RemoteSettings()`
- 参照: `this._tippyTop`

## FaviconProvider.shouldFetchIcons()
- 位置: L1198-1200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## FaviconProvider.getFaviconInfo()
- 位置: async L1210-1218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.favicons.getFaviconForPage()`
- 参照: `favicon.uri`, `favicon.width`, `lazy.NewTabUtils.activityStreamProvider.THUMB_FAVICON_SIZE`

## FaviconProvider.fetchIconFromRedirects()
- 位置: async L1228-1246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fetchVisitPaths()`
- 条件付き依存: `if (visitPaths.length > 1)` → `visitPaths.pop()`
- 条件付き依存: `if (visitPaths.length > 1)` → `Services.io.newURI()`
- 条件付き依存: `if (visitPaths.length > 1)` → `this.getFaviconInfo()`
- 条件付き依存: `if (iconInfo?.faviconSize >= MIN_FAVICON_SIZE)` → `lazy.PlacesUtils.favicons.tryCopyFavicons()`
- 条件付き依存: `if (iconInfo?.faviconSize >= MIN_FAVICON_SIZE)` → `Services.io.newURI()`
- 条件付き依存: `if (iconInfo?.faviconSize >= MIN_FAVICON_SIZE)` → `lazy.log.debug()`
- 参照: `iconInfo?.faviconSize`, `lastVisit.url`, `lazy.PlacesUtils.favicons.FAVICON_LOAD_NON_PRIVATE`, `visitPaths.length`
- XPCOM: `Services.io`

## FaviconProvider.getFaviconDataURLFromNetwork()
- 位置: async L1255-1294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`, `Promise.withResolvers()`, `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `input.available()`, `input.close()`, `lazy.NetUtil.asyncFetch()`, `lazy.NetUtil.newChannel()`, `lazy.NetUtil.readInputStream()`, `reader.addEventListener()`, `reader.readAsDataURL()`, `request.QueryInterface()`, `resolve()`, `resolver.reject()`, `resolver.resolve()`
- 条件付き依存: `if (!Components.isSuccessCode(status))` → `resolver.resolve()`
- 参照: `Ci.nsIChannel`, `Ci.nsIContentPolicy.TYPE_INTERNAL_IMAGE_FAVICON`, `Ci.nsILoadInfo.SEC_ALLOW_CHROME`, `Ci.nsILoadInfo.SEC_DISALLOW_SCRIPT`, `Ci.nsILoadInfo.SEC_REQUIRE_CORS_INHERITS_SEC_CONTEXT`, `reader.result`, `resolver.promise`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / `Services.io` / `Services.scriptSecurityManager`

## FaviconProvider.#setFaviconForPage()
- 位置: async L1302-1339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `faviconURI.schemeIs()`, `lazy.PlacesUtils.favicons .setFaviconForPage()`, `this.getFaviconDataURLFromNetwork()`, `this.getFaviconInfo()`
- 条件付き依存: `if (faviconURI.schemeIs("data"))` → `lazy.PlacesUtils.favicons .setFaviconForPage( pageURI, faviconURI, faviconURI, 0, /* isRich */ true ) .catch()`
- 条件付き依存: `if (faviconURI.schemeIs("data"))` → `lazy.PlacesUtils.favicons .setFaviconForPage()`
- 参照: `console.error`, `faviconInfo?.faviconSize`

## FaviconProvider.#fetchVisitPaths()
- 位置: async L1354-1391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabUtils.activityStreamProvider.executePlacesQuery()`
- 参照: `lazy.PlacesUtils.history.TRANSITIONS.REDIRECT_PERMANENT`, `lazy.PlacesUtils.history.TRANSITIONS.REDIRECT_TEMPORARY`
