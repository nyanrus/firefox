# browser/components/firefoxview/opentabs.mjs

source: browser/components/firefoxview/opentabs.mjs
source-hash: bbd99161d089f8aef8734cfa560cb91598c11c0d
lines: 1076

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `customElements.define()`

## OpenTabsInView.constructor()
- 位置: L81-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `super()`, `this.getWindow()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(this.currentWindow))` → `lazy.getTabsTargetForWindow()`
- 参照: `lazy.NonPrivateTabs`, `this._started`, `this.currentWindow`, `this.openTabsTarget`, `this.recentBrowsing`, `this.searchQuery`, `this.sortOption`, `this.windows`
- XPCOM: `Services.prefs`

## OpenTabsInView.start()
- 位置: L100-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `card.requestUpdate()`, `card.viewVisibleCallback()`, `this.#getAllTabUrls()`, `this.#setupTabChangeListener()`, `this._updateWindowList()`, `this.openTabsTarget.readyWindowsPromise.finally()`, `this.viewCards.forEach()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.recentBrowsingElement.addEventListener()`
- 参照: `card.paused`, `lazy.BookmarkList`, `this._started`, `this.bookmarkList`, `this.initialWindowsReady`, `this.recentBrowsing`, `this.viewCards`

## OpenTabsInView.shouldUpdate()
- 位置: L132-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.shouldUpdate()`
- 参照: `this.initialWindowsReady`

## OpenTabsInView.disconnectedCallback()
- 位置: L139-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.stop()`

## OpenTabsInView.stop()
- 位置: L144-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `card.viewHiddenCallback()`, `this.bookmarkList.removeListeners()`, `this.openTabsTarget.removeEventListener()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.recentBrowsingElement.removeEventListener()`
- 参照: `card.paused`, `this._started`, `this.paused`, `this.recentBrowsing`, `this.viewCards`

## OpenTabsInView.viewVisibleCallback()
- 位置: L169-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.start()`

## OpenTabsInView.viewHiddenCallback()
- 位置: L173-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stop()`

## OpenTabsInView.#setupTabChangeListener()
- 位置: L177-185
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.sortOption === "recency")` → `this.openTabsTarget.addEventListener()`
- 条件付き依存: `if (this.sortOption === "recency")` → `this.openTabsTarget.removeEventListener()`
- 条件付き依存: `if (!(this.sortOption === "recency"))` → `this.openTabsTarget.removeEventListener()`
- 条件付き依存: `if (!(this.sortOption === "recency"))` → `this.openTabsTarget.addEventListener()`
- 参照: `this.sortOption`

## OpenTabsInView.#getAllTabUrls()
- 位置: L187-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openTabsTarget .getAllTabs()`, `this.openTabsTarget .getAllTabs() .map()`, `this.openTabsTarget .getAllTabs() .map(({ linkedBrowser }) => linkedBrowser?.currentURI?.spec) .filter()`
- 参照: `linkedBrowser?.currentURI?.spec`

## OpenTabsInView.render()
- 位置: L194-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `classMap()`, `html()`, `map()`, `this.openTabsTarget.getTabsForWindow()`, `this.windows.forEach()`, `when()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.getRecentBrowsingTemplate()`
- 条件付き依存: `if (!(win === this.currentWindow))` → `otherWindows.push()`
- 参照: `this.bookmarkList`, `this.currentWindow`, `this.currentWindow.windowGlobalChild .innerWindowId`, `this.onChangeSortOption`, `this.onSearchQuery`, `this.paused`, `this.recentBrowsing`, `this.searchQuery`, `this.sortOption`, `this.windows.length`, `win.windowGlobalChild.innerWindowId`

## OpenTabsInView.onSearchQuery()
- 位置: L318-325
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.recentBrowsing)` → `Glean.firefoxviewNext.searchInitiatedSearch.record()`
- 参照: `e.detail.query`, `this.recentBrowsing`, `this.searchQuery`

## OpenTabsInView.onChangeSortOption()
- 位置: L327-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setupTabChangeListener()`
- 条件付き依存: `if (!this.recentBrowsing)` → `Services.prefs.setStringPref()`
- 参照: `e.target.value`, `this.recentBrowsing`, `this.sortOption`
- XPCOM: `Services.prefs`

## OpenTabsInView.getRecentBrowsingTemplate()
- 位置: L345-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.openTabsTarget.getRecentTabs()`
- 参照: `this.bookmarkList`, `this.paused`, `this.searchQuery`

## OpenTabsInView.handleEvent()
- 位置: L356-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getAllTabUrls()`, `this._updateWindowList()`, `this.bookmarkList.setTrackedUrls()`
- 条件付き依存: `if (this.recentBrowsing && type === "MozInputSearch:search")` → `this.onSearchQuery()`
- 条件付き依存: `if (windowIds?.length)` → `this.shadowRoot.querySelector()`
- 条件付き依存: `if (this.searchQuery)` → `cardForWin?.updateSearchResults()`
- 条件付き依存: `if (windowIds?.length)` → `cardForWin?.requestUpdate()`
- 条件付き依存: `if (!(windowIds?.length))` → `this.shadowRoot.querySelector()`
- 参照: `detail.windowIds`, `this.recentBrowsing`, `this.searchQuery`, `window.windowGlobalChild.innerWindowId`, `windowIds?.length`

## OpenTabsInView._updateWindowList()
- 位置: async L395-397
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.openTabsTarget.currentWindows`, `this.windows`

## OpenTabsInViewCard.constructor()
- 位置: L425-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `lazy.OpenTabsController`, `this.controller`, `this.cumulativeSearches`, `this.devices`, `this.recentBrowsing`, `this.searchQuery`, `this.searchResults`, `this.showAll`, `this.showMore`, `this.tabs`, `this.title`

## OpenTabsInViewCard.openContextMenu()
- 位置: L445-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabContextMenu.toggle()`
- 参照: `e.detail`, `e.originalTarget`

## OpenTabsInViewCard.getMaxTabsLength()
- 位置: L453-460
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(this.recentBrowsing && !this.showAll))` → `this.classList.contains()`
- 参照: `OpenTabsInViewCard.MAX_TABS_FOR_COMPACT_HEIGHT`, `this.recentBrowsing`, `this.showAll`, `this.showMore`

## OpenTabsInViewCard.isShowAllLinkVisible()
- 位置: L462-469
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.recentBrowsing`, `this.searchQuery`, `this.searchResults.length`, `this.showAll`

## OpenTabsInViewCard.isShowMoreLinkVisible()
- 位置: L471-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.classList.contains()`
- 参照: `(this.searchQuery ? this.searchResults : this.tabs).length`, `OpenTabsInViewCard.MAX_TABS_FOR_COMPACT_HEIGHT`, `this.searchQuery`, `this.searchResults`, `this.tabs`

## OpenTabsInViewCard.toggleShowMore()
- 位置: L480-489
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `event.preventDefault()`
- 参照: `event.code`, `event.type`, `this.showMore`

## OpenTabsInViewCard.enableShowAll()
- 位置: L491-503
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `event.preventDefault()`
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `Glean.firefoxviewNext.searchShowAllShowallbutton.record()`
- 参照: `event.code`, `event.type`, `this.showAll`

## OpenTabsInViewCard.onTabListRowClick()
- 位置: L505-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(event.explicitOriginalTarget.classList).includes()`, `Glean.firefoxviewNext.openTabTabs.record()`, `browserWindow.focus()`
- 条件付き依存: `if (this.searchQuery)` → `Glean.firefoxview.cumulativeSearches[ this.recentBrowsing ? "recentbrowsing" : "opentabs" ].accumulateSingleSample()`
- 参照: `Glean.firefoxview.cumulativeSearches`, `browserWindow.gBrowser.selectedTab`, `event.explicitOriginalTarget.classList`, `event.originalTarget.tabElement`, `tab.documentGlobal`, `this.cumulativeSearches`, `this.recentBrowsing`, `this.searchQuery`, `this.title`

## OpenTabsInViewCard.closeTab()
- 位置: L531-538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.closeOpenTabTabs.record()`, `lazy.TabMetrics.userTriggeredContext()`, `tab?.documentGlobal.gBrowser.removeTab()`
- 参照: `event.originalTarget.tabElement`

## OpenTabsInViewCard.viewVisibleCallback()
- 位置: L540-542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.getRootNode().host.toggleVisibilityInCardContainer()`

## OpenTabsInViewCard.viewHiddenCallback()
- 位置: L544-546
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.getRootNode().host.toggleVisibilityInCardContainer()`

## OpenTabsInViewCard.firstUpdated()
- 位置: L548-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.getRootNode().host.toggleVisibilityInCardContainer()`

## OpenTabsInViewCard.render()
- 位置: L552-617
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.classList.contains()`, `this.controller.getTabListItems()`, `this.getMaxTabsLength()`, `this.isShowAllLinkVisible()`, `this.isShowMoreLinkVisible()`, `when()`
- 参照: `this.closeTab`, `this.enableShowAll`, `this.onTabListRowClick`, `this.openContextMenu`, `this.recentBrowsing`, `this.searchQuery`, `this.searchResults`, `this.showMore`, `this.tabs`, `this.title`, `this.toggleShowMore`

## OpenTabsInViewCard.willUpdate()
- 位置: L619-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("searchQuery") || changedProperties.has("tabs"))` → `this.updateSearchResults()`
- 参照: `this.cumulativeSearches`, `this.searchQuery`, `this.showAll`

## OpenTabsInViewCard.updateSearchResults()
- 位置: L631-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchTabList()`, `this.controller.getTabListItems()`
- 参照: `this.searchQuery`, `this.searchResults`, `this.tabs`

## OpenTabsInViewCard.updated()
- 位置: L640-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateBookmarkStars()`

## OpenTabsInViewCard.updateBookmarkStars()
- 位置: async L644-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.indicators.includes()`, `this.bookmarkList.isBookmark()`, `this.controller.getPrimaryL10nId()`
- 条件付き依存: `if (isBookmark && !row.indicators.includes("bookmark"))` → `row.indicators.push()`
- 条件付き依存: `if (!isBookmark && row.indicators.includes("bookmark"))` → `row.indicators.filter()`
- 参照: `row.indicators`, `row.primaryL10nId`, `row.url`, `this.isRecentBrowsing`, `this.tabList.tabItems`

## hasChanged()
- 位置: L670-670
- 役割: (未記入)
- 触るとき: (未記入)

## OpenTabsContextMenu.constructor()
- 位置: L677-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.boundObserve`, `this.devices`, `this.triggerNode`

## this.boundObserve()
- 位置: L680-680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observe()`

## OpenTabsContextMenu.logger()
- 位置: L684-686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLogger()`

## OpenTabsContextMenu.ownerViewPage()
- 位置: L688-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerDocument.querySelector()`

## OpenTabsContextMenu.connectedCallback()
- 位置: L692-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `super.connectedCallback()`, `this.fetchDevices()`
- 参照: `this.boundObserve`, `this.fetchDevicesPromise`
- XPCOM: `Services.obs`

## OpenTabsContextMenu.disconnectedCallback()
- 位置: L699-703
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `super.disconnectedCallback()`
- 参照: `this.boundObserve`
- XPCOM: `Services.obs`

## OpenTabsContextMenu.observe()
- 位置: L705-712
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( topic == TOPIC_DEVICELIST_UPDATED || topic == TOPIC_DEVICESTATE_CHANGED )` → `this.fetchDevices()`
- 参照: `this.fetchDevicesPromise`

## OpenTabsContextMenu.fetchDevices()
- 位置: async L714-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerViewPage.getWindow()`
- 条件付き依存: `if (currentWindow?.gSync)` → `lazy.fxAccounts.device.refreshDeviceList()`
- 条件付き依存: `if (currentWindow?.gSync)` → `this.logger.warn()`
- 条件付き依存: `if (currentWindow?.gSync)` → `currentWindow.gSync.getSendTabTargets()`
- 参照: `currentWindow?.gSync`, `this.devices`

## OpenTabsContextMenu.toggle()
- 位置: async L726-742
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getUpdateComplete()`, `this.panelList.toggle()`
- 条件付き依存: `if (this.panelList?.open)` → `this.panelList.toggle()`
- 条件付き依存: `if (this.devices.length >= 1)` → `Glean.firefoxview.sendTabExposed.record()`
- 条件付き依存: `if (this.devices.length >= 1)` → `String()`
- 参照: `this.devices.length`, `this.fetchDevicesPromise`, `this.panelList?.open`, `this.triggerNode`

## OpenTabsContextMenu.copyLink()
- 位置: L744-747
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.copyLink()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.title`, `this.triggerNode.url`

## OpenTabsContextMenu.closeTab()
- 位置: L749-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab?.documentGlobal.gBrowser.removeTab()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.pinTab()
- 位置: L755-759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab?.documentGlobal.gBrowser.pinTab()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.unpinTab()
- 位置: L761-765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab?.documentGlobal.gBrowser.unpinTab()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.toggleAudio()
- 位置: L767-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.toggleMuteAudio()`, `this.ownerViewPage.recordContextMenuTelemetry()`, `this.triggerNode.indicators.includes()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.moveTabsToStart()
- 位置: L778-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab?.documentGlobal.gBrowser.moveTabsToStart()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.moveTabsToEnd()
- 位置: L784-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab?.documentGlobal.gBrowser.moveTabsToEnd()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.moveTabsToWindow()
- 位置: L790-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab?.documentGlobal.gBrowser.replaceTabsWithWindow()`, `this.ownerViewPage.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.tabElement`

## OpenTabsContextMenu.moveMenuTemplate()
- 位置: L796-828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `tabs.indexOf()`
- 参照: `browserWindow?.gBrowser.visibleTabs`, `tab.documentGlobal`, `tabs.length`, `this.moveTabsToEnd`, `this.moveTabsToStart`, `this.moveTabsToWindow`, `this.triggerNode?.tabElement`

## OpenTabsContextMenu.sendTabToDevice()
- 位置: async L830-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxview.clickSendTab.record()`, `String()`, `e.target.getAttribute()`, `this.devices.find()`, `viewPage.recordContextMenuTelemetry()`
- 条件付き依存: `if (device && this.triggerNode)` → `viewPage.getWindow()`
- 条件付き依存: `if (device && this.triggerNode)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (device && this.triggerNode)` → `chromeWindow.gSync.sendTabToDevice()`
- 参照: `dev.id`, `this.devices.length`, `this.ownerViewPage`, `this.triggerNode`, `this.triggerNode.title`, `this.triggerNode.url`

## OpenTabsContextMenu.onSendTabSubmenuClick()
- 位置: L852-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxview.sendTabOpened.record()`, `String()`
- 参照: `this.devices.length`

## OpenTabsContextMenu.onSendTabSignedOutItemClick()
- 位置: L858-867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SpecialMessageActions.fxaSignInFlow()`, `this.ownerViewPage.getWindow()`
- 参照: `this.ownerViewPage.getWindow().gBrowser`

## OpenTabsContextMenu.onSendTabSyncDisabledItemClick()
- 位置: L869-873
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerViewPage .getWindow()`, `this.ownerViewPage .getWindow() .openTrustedLinkIn()`

## OpenTabsContextMenu.onSendTabConnectPhoneItemClick()
- 位置: L875-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FxAccounts.config.promisePairingURI()`, `this.ownerViewPage.getWindow()`, `this.ownerViewPage.getWindow().switchToTabHavingURI()`

## OpenTabsContextMenu.onSendTabNoDeviceItemClick()
- 位置: L885-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `this.ownerViewPage.getWindow()`, `this.ownerViewPage.getWindow().switchToTabHavingURI()`
- XPCOM: `Services.urlFormatter`

## OpenTabsContextMenu.onSendTabVerifyAccountClick()
- 位置: L895-899
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerViewPage .getWindow()`, `this.ownerViewPage .getWindow() .openTrustedLinkIn()`

## OpenTabsContextMenu.sendTabDevicesTemplate()
- 位置: L901-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.devices.map()`
- 参照: `device.id`, `device.name`, `this.sendTabToDevice`

## OpenTabsContextMenu.sendTabAccountUnverifiedTemplate()
- 位置: L913-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.onSendTabVerifyAccountClick`

## OpenTabsContextMenu.sendTabSignedOutTemplate()
- 位置: L935-949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.onSendTabSignedOutItemClick`

## OpenTabsContextMenu.sendTabSyncDisabledTemplate()
- 位置: L951-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.onSendTabSyncDisabledItemClick`

## OpenTabsContextMenu.sendTabSingleDeviceTemplate()
- 位置: L967-987
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.onSendTabConnectPhoneItemClick`, `this.onSendTabNoDeviceItemClick`

## OpenTabsContextMenu.sendTabMultiDeviceTemplate()
- 位置: L989-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.sendTabDevicesTemplate()`
- 参照: `this.onSendTabSubmenuClick`

## OpenTabsContextMenu.sendTabTemplate()
- 位置: L1002-1030
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSync.hasOnlyMobileSendTabTargets()`, `this.ownerViewPage.getWindow()`, `this.sendTabAccountUnverifiedTemplate()`, `this.sendTabMultiDeviceTemplate()`, `this.sendTabSignedOutTemplate()`, `this.sendTabSingleDeviceTemplate()`, `this.sendTabSyncDisabledTemplate()`
- 参照: `gSync.hasNoSendTabTargets`, `gSync.isSignedIn`, `gSync.isSignedInWithSyncDisabled`, `gSync.isUnverified`, `lazy.FXA_ENABLED`, `this.ownerViewPage.getWindow().gSync`

## OpenTabsContextMenu.render()
- 位置: L1032-1073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `tab.hasAttribute()`, `this.moveMenuTemplate()`, `this.sendTabTemplate()`
- 参照: `tab.pinned`, `this.copyLink`, `this.pinTab`, `this.toggleAudio`, `this.triggerNode?.tabElement`, `this.unpinTab`
