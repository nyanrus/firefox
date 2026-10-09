# browser/components/firefoxview/recentlyclosed.mjs

source: browser/components/firefoxview/recentlyclosed.mjs
source-hash: b09a73b2cb9de0128a639eb72129036372ca30cc
lines: 486

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## getWindow()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext.embedderWindowGlobal.browsingContext.window`

## RecentlyClosedTabsInView.constructor()
- 位置: L37-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._started`, `this.boundObserve`, `this.cumulativeSearches`, `this.firstUpdateComplete`, `this.fullyUpdated`, `this.maxTabsLength`, `this.recentBrowsing`, `this.recentlyClosedTabs`, `this.searchQuery`, `this.searchResults`, `this.showAll`

## this.boundObserve()
- 位置: L40-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observe()`

## RecentlyClosedTabsInView.observe()
- 位置: L67-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getWindow()`
- 条件付き依存: `if ( topic == SS_NOTIFY_CLOSED_OBJECTS_CHANGED || (topic == SS_NOTIFY_BROWSER_SHUTDOWN_FLUSH && subject.documentGlobal == getWindow()) )` → `this.updateRecentlyClosedTabs()`
- 参照: `subject.documentGlobal`

## RecentlyClosedTabsInView.start()
- 位置: L77-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this.toggleVisibilityInCardContainer()`, `this.updateRecentlyClosedTabs()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.recentBrowsingElement.addEventListener()`
- 参照: `this._started`, `this.boundObserve`, `this.paused`, `this.recentBrowsing`
- XPCOM: `Services.obs`

## RecentlyClosedTabsInView.stop()
- 位置: L104-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this.toggleVisibilityInCardContainer()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.recentBrowsingElement.removeEventListener()`
- 参照: `this._started`, `this.boundObserve`, `this.recentBrowsing`
- XPCOM: `Services.obs`

## RecentlyClosedTabsInView.disconnectedCallback()
- 位置: L129-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.stop()`

## RecentlyClosedTabsInView.handleEvent()
- 位置: L134-138
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.recentBrowsing && event.type === "MozInputSearch:search")` → `this.onSearchQuery()`
- 参照: `event.type`, `this.recentBrowsing`

## RecentlyClosedTabsInView.viewHiddenCallback()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stop()`

## RecentlyClosedTabsInView.viewVisibleCallback()
- 位置: L147-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.start()`

## RecentlyClosedTabsInView.firstUpdated()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.firstUpdateComplete`

## RecentlyClosedTabsInView.getTabStateValue()
- 位置: L155-165
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab.state.entries`, `tab.state.index`

## RecentlyClosedTabsInView.updateRecentlyClosedTabs()
- 位置: L167-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `getWindow()`, `lazy.SessionStore.getClosedTabData()`, `recentlyClosedTabsData.sort()`, `this.normalizeRecentlyClosedData()`, `this.requestUpdate()`
- 条件付き依存: `if (Services.prefs.getBoolPref(INCLUDE_CLOSED_TABS_FROM_CLOSED_WINDOWS))` → `recentlyClosedTabsData.push()`
- 条件付き依存: `if (Services.prefs.getBoolPref(INCLUDE_CLOSED_TABS_FROM_CLOSED_WINDOWS))` → `lazy.SessionStore.getClosedTabDataFromClosedWindows()`
- 条件付き依存: `if (this.searchQuery)` → `this.#updateSearchResults()`
- 参照: `a.closedAt`, `b.closedAt`, `this.recentlyClosedTabs`, `this.searchQuery`
- XPCOM: `Services.prefs`

## RecentlyClosedTabsInView.normalizeRecentlyClosedData()
- 位置: L186-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `this.getTabStateValue()`, `this.recentlyClosedTabs.forEach()`
- 参照: `recentlyClosedItem.closedAt`, `recentlyClosedItem.icon`, `recentlyClosedItem.image`, `recentlyClosedItem.primaryL10nArgs`, `recentlyClosedItem.primaryL10nId`, `recentlyClosedItem.secondaryL10nArgs`, `recentlyClosedItem.secondaryL10nId`, `recentlyClosedItem.time`, `recentlyClosedItem.title`, `recentlyClosedItem.url`

## RecentlyClosedTabsInView.onReopenTab()
- 位置: L205-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.tabList.rowEls).indexOf()`, `Date.now()`, `Glean.firefoxviewNext.recentlyClosedTabs.record()`, `getWindow()`, `isNaN()`, `parseInt()`
- 条件付き依存: `if (isNaN(sourceClosedId))` → `lazy.SessionStore.undoCloseById()`
- 条件付き依存: `if (!(isNaN(sourceClosedId)))` → `lazy.SessionStore.undoClosedTabFromClosedWindow()`
- 条件付き依存: `if (this.searchQuery)` → `Glean.firefoxview.cumulativeSearches[ this.recentBrowsing ? "recentbrowsing" : "recentlyclosed" ].accumulateSingleSample()`
- 参照: `Glean.firefoxview.cumulativeSearches`, `e.detail.originalEvent`, `e.originalTarget`, `e.originalTarget.closedId`, `e.originalTarget.sourceClosedId`, `e.originalTarget.time`, `lazy.AppConstants.platform`, `originalEvent.ctrlKey`, `originalEvent.metaKey`, `this.cumulativeSearches`, `this.recentBrowsing`, `this.searchQuery`, `this.tabList.rowEls`, `win.gBrowser.selectedTab`, `win.gBrowser?.selectedTab`

## RecentlyClosedTabsInView.onDismissTab()
- 位置: L257-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.tabList.rowEls).indexOf()`, `Date.now()`, `Glean.firefoxviewNext.dismissClosedTabTabs.record()`, `isNaN()`, `parseInt()`
- 条件付き依存: `if (!isNaN(sourceClosedId))` → `lazy.SessionStore.forgetClosedTabById()`
- 条件付き依存: `if (sourceWindowId)` → `lazy.SessionStore.forgetClosedTabById()`
- 条件付き依存: `if (!(sourceWindowId))` → `lazy.SessionStore.forgetClosedTabById()`
- 参照: `e.originalTarget`, `e.originalTarget.closedId`, `e.originalTarget.sourceClosedId`, `e.originalTarget.sourceWindowId`, `e.originalTarget.time`, `this.recentBrowsing`, `this.tabList.rowEls`

## RecentlyClosedTabsInView.willUpdate()
- 位置: L293-295
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.fullyUpdated`

## RecentlyClosedTabsInView.updated()
- 位置: L297-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleVisibilityInCardContainer()`
- 参照: `this.fullyUpdated`

## RecentlyClosedTabsInView.scheduleUpdate()
- 位置: async L302-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.scheduleUpdate()`
- 条件付き依存: `if (!this.firstUpdateComplete)` → `setTimeout()`
- 参照: `this.firstUpdateComplete`

## RecentlyClosedTabsInView.emptyMessageTemplate()
- 位置: L310-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `html()`
- 参照: `this.recentBrowsing`, `this.selectedTab`
- XPCOM: `Services.prefs`

## RecentlyClosedTabsInView.render()
- 位置: L359-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `this.emptyMessageTemplate()`, `this.isShowAllLinkVisible()`, `when()`
- 参照: `this.enableShowAll`, `this.onDismissTab`, `this.onReopenTab`, `this.onSearchQuery`, `this.recentBrowsing`, `this.recentlyClosedTabs`, `this.recentlyClosedTabs.length`, `this.searchQuery`, `this.searchResults`, `this.selectedTab`, `this.showAll`

## RecentlyClosedTabsInView.onSearchQuery()
- 位置: L442-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateSearchResults()`
- 条件付き依存: `if (!this.recentBrowsing)` → `Glean.firefoxviewNext.searchInitiatedSearch.record()`
- 参照: `e.detail.query`, `this.cumulativeSearches`, `this.recentBrowsing`, `this.searchQuery`, `this.showAll`

## RecentlyClosedTabsInView.#updateSearchResults()
- 位置: L456-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchTabList()`
- 参照: `this.recentlyClosedTabs`, `this.searchQuery`, `this.searchResults`

## RecentlyClosedTabsInView.isShowAllLinkVisible()
- 位置: L462-469
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.recentBrowsing`, `this.searchQuery`, `this.searchResults.length`, `this.showAll`

## RecentlyClosedTabsInView.enableShowAll()
- 位置: L471-483
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `event.preventDefault()`
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `Glean.firefoxviewNext.searchShowAllShowallbutton.record()`
- 参照: `event.code`, `event.type`, `this.showAll`
