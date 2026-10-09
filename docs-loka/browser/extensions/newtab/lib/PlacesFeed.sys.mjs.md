# browser/extensions/newtab/lib/PlacesFeed.sys.mjs

source: browser/extensions/newtab/lib/PlacesFeed.sys.mjs
source-hash: 53c4a0efc92a4fe1afb2ea271617bad85f41e426
lines: 469

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PlacesObserver.constructor()
- 位置: L39-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `this.handlePlacesEvent.bind()`
- 参照: `this.QueryInterface`, `this.dispatch`, `this.handlePlacesEvent`

## PlacesObserver.handlePlacesEvent()
- 位置: L45-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatch()`, `url.startsWith()`
- 条件付き依存: `if (isRemovedFromStore)` → `removedPages.push()`
- 条件付き依存: `if ( isTagging || (itemType === lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK && source !== lazy.PlacesUtils.bookmarks.SOURCES.IMPORT && source !== lazy.PlacesUtils.b...)` → `removedBookmarks.push()`
- 条件付き依存: `if (removedPages.length || removedBookmarks.length)` → `this.dispatch()`
- 条件付き依存: `if (removedPages.length)` → `this.dispatch()`
- 条件付き依存: `if (removedBookmarks.length)` → `this.dispatch()`
- 参照: `at.PLACES_BOOKMARKS_REMOVED`, `at.PLACES_BOOKMARK_ADDED`, `at.PLACES_HISTORY_CLEARED`, `at.PLACES_LINKS_CHANGED`, `at.PLACES_LINKS_DELETED`, `lazy.PlacesUtils.bookmarks.SOURCES.IMPORT`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE_ON_STARTUP`, `lazy.PlacesUtils.bookmarks.SOURCES.SYNC`, `lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK`, `removedBookmarks.length`, `removedPages.length`

## PlacesFeed.constructor()
- 位置: L135-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.customDispatch.bind()`
- 参照: `this.customDispatch`, `this.placesChangedTimer`, `this.placesObserver`

## PlacesFeed.addObservers()
- 位置: L141-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.PlacesUtils.observers.addListener()`
- 参照: `this.placesObserver.handlePlacesEvent`
- XPCOM: `Services.obs`

## PlacesFeed.setTimeout()
- 位置: L156-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PlacesFeed.customDispatch()
- 位置: L162-181
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(this.placesChangedTimer))` → `this.setTimeout()`
- 条件付き依存: `if (!(this.placesChangedTimer))` → `this.store.dispatch()`
- 条件付き依存: `if (!(this.placesChangedTimer))` → `ac.OnlyToMain()`
- 条件付き依存: `if (!(action.type === at.PLACES_LINKS_CHANGED))` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (!(action.type === at.PLACES_LINKS_CHANGED))` → `this.store.dispatch()`
- 条件付き依存: `if (!(action.type === at.PLACES_LINKS_CHANGED))` → `ac.BroadcastToContent()`
- 参照: `action.type`, `at.PLACES_LINKS_CHANGED`, `this.placesChangedTimer`, `this.placesChangedTimer.delay`
- XPCOM: `Services.tm`

## PlacesFeed.removeObservers()
- 位置: L183-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.PlacesUtils.observers.removeListener()`
- 条件付き依存: `if (this.placesChangedTimer)` → `this.placesChangedTimer.cancel()`
- 参照: `this.placesChangedTimer`, `this.placesObserver.handlePlacesEvent`
- XPCOM: `Services.obs`

## PlacesFeed.observe()
- 位置: L206-215
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === LINK_BLOCKED_EVENT)` → `this.store.dispatch()`
- 条件付き依存: `if (topic === LINK_BLOCKED_EVENT)` → `ac.BroadcastToContent()`
- 参照: `at.PLACES_LINK_BLOCKED`

## PlacesFeed.openLink()
- 位置: L220-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `["http", "https"].includes()`, `console.error()`, `lazy.BrowserUtils.whereToOpenLink()`, `win.openTrustedLinkIn()`
- 条件付き依存: `if (referrer)` → `Components.Constructor()`
- 条件付き依存: `if (referrer)` → `Services.io.newURI()`
- 条件付き依存: `if (typedBonus)` → `lazy.PlacesUtils.history.markPageAsTyped()`
- 条件付き依存: `if (typedBonus)` → `Services.io.newURI()`
- 条件付き依存: `if (action.data.original_url)` → `lazy.PlacesUtils.history.insert()`
- 参照: `Ci.nsIReferrerInfo.UNSAFE_URL`, `action._target.browser`, `action._target.window`, `action.data`, `action.data.dwell_label`, `action.data.is_sponsored`, `action.data.open_url`, `action.data.original_url`, `action.data.type`, `action.data.url`, `lazy.PlacesUtils.history.TRANSITION_TYPED`, `params.referrerInfo`, `params.resolveOnContentBrowserCreated`, `uri.scheme`
- XPCOM: [`nsIReferrerInfo`](../../../../docshell/shistory/nsISHEntry.idl.md) / `Services.io`

## params.resolveOnContentBrowserCreated()
- 位置: L238-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.dispatch()`
- 参照: `action.data.dwell_label`, `at.DWELL_LINK_OPENED`

## PlacesFeed.fillSearchTopSiteTerm()
- 位置: async L304-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_target.window.gURLBar.search()`, `lazy.SearchService.getEngineByAlias()`
- 参照: `data.label`

## PlacesFeed._getDefaultSearchEngine()
- 位置: L312-316
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SearchService`

## PlacesFeed.addToBlockedTopSitesSponsors()
- 位置: L324-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `JSON.stringify()`, `Services.prefs.getStringPref()`, `Services.prefs.setStringPref()`, `lazy.NewTabUtils.shortURL()`, `urls.map()`
- XPCOM: `Services.prefs`

## PlacesFeed.addToUnifiedAdsBlockedAdsList()
- 位置: L352-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.setStringPref()`, `blockedAdsArray.join()`
- 条件付き依存: `if (!(blockedAdsPref === ""))` → `blockedAdsPref .split(",") .map(s => s.trim()) .filter()`
- 条件付き依存: `if (!(blockedAdsPref === ""))` → `blockedAdsPref .split(",") .map()`
- 条件付き依存: `if (!(blockedAdsPref === ""))` → `blockedAdsPref .split()`
- 条件付き依存: `if (!(blockedAdsPref === ""))` → `s.trim()`
- 条件付き依存: `if (!(blockedAdsPref === ""))` → `blockedAdsArray.concat()`
- XPCOM: `Services.prefs`

## PlacesFeed.onAction()
- 位置: L380-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.tm.dispatchToMainThread()`, `Services.urlFormatter.formatURLPref()`, `lazy.NewTabUtils.activityStreamLinks.addBookmark()`, `lazy.NewTabUtils.activityStreamLinks.deleteBookmark()`, `lazy.NewTabUtils.activityStreamLinks.deleteHistoryEntry()`, `this.addObservers()`, `this.fillSearchTopSiteTerm()`, `this.openLink()`, `this.removeObservers()`, `win.openTrustedLinkIn()`
- 条件付き依存: `if (action.data)` → `action.data.forEach()`
- 条件付き依存: `if (action.data)` → `lazy.NewTabUtils.activityStreamLinks.blockURL()`
- 条件付き依存: `if (isSponsoredTopSite)` → `sponsoredTopSites.push()`
- 条件付き依存: `if (unifiedAdsTilesEnabled)` → `sponsoredBlockKeys.push()`
- 条件付き依存: `if (sponsoredTopSites.length)` → `this.addToBlockedTopSitesSponsors()`
- 条件付き依存: `if (sponsoredBlockKeys.length)` → `this.addToUnifiedAdsBlockedAdsList()`
- 条件付き依存: `if (forceBlock)` → `lazy.NewTabUtils.activityStreamLinks.blockURL()`
- 参照: `action._target.window`, `action.data`, `action.data.where`, `action.type`, `at.ABOUT_SPONSORED_TOP_SITES`, `at.BLOCK_URL`, `at.BOOKMARK_URL`, `at.DELETE_BOOKMARK_BY_ID`, `at.DELETE_HISTORY_URL`, `at.FILL_SEARCH_TERM`, `at.INIT`, `at.OPEN_LINK`, `at.OPEN_NEW_WINDOW`, `at.OPEN_PRIVATE_WINDOW`, `at.UNINIT`, `sponsoredBlockKeys.length`, `sponsoredTopSites.length`
- XPCOM: `Services.prefs` / `Services.tm` / `Services.urlFormatter`
