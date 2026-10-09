# browser/components/firefoxview/syncedtabs.mjs

source: browser/components/firefoxview/syncedtabs.mjs
source-hash: 405f019e0f649aa1f7f9a02c2cec92003911a14d
lines: 457

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## pairDeviceCallback()
- 位置: L36-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.fxaMobileSync.record()`
- 参照: `TabsSetupFlowManager.secondaryDeviceConnected`

## signupCallback()
- 位置: L40-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.fxaContinueSync.record()`

## SyncedTabsInView.constructor()
- 位置: L43-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`, `super()`, `this.onSearchQuery.bind()`
- 参照: `this._id`, `this._started`, `this.cumulativeSearches`, `this.fullyUpdated`, `this.maxTabsLength`, `this.onSearchQuery`, `this.recentBrowsing`, `this.showAll`

## SyncedTabsInView.start()
- 位置: L72-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.addSyncObservers()`, `this.controller.updateStates()`, `this.onVisibilityChange()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.recentBrowsingElement.addEventListener()`
- 参照: `this._started`, `this.onSearchQuery`, `this.recentBrowsing`

## SyncedTabsInView.stop()
- 位置: L89-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabsSetupFlowManager.updateViewVisibility()`, `this.controller.removeSyncObservers()`, `this.onVisibilityChange()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.recentBrowsingElement.removeEventListener()`
- 参照: `this._id`, `this._started`, `this.onSearchQuery`, `this.recentBrowsing`

## SyncedTabsInView.disconnectedCallback()
- 位置: L106-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.stop()`

## SyncedTabsInView.viewVisibleCallback()
- 位置: L111-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.start()`

## SyncedTabsInView.viewHiddenCallback()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stop()`

## SyncedTabsInView.onVisibilityChange()
- 位置: L119-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleVisibilityInCardContainer()`
- 条件付き依存: `if (isVisible && isOpen)` → `this.update()`
- 条件付き依存: `if (isVisible && isOpen)` → `TabsSetupFlowManager.updateViewVisibility()`
- 条件付き依存: `if (!(isVisible && isOpen))` → `TabsSetupFlowManager.updateViewVisibility()`
- 参照: `this._id`, `this.isVisible`, `this.open`

## SyncedTabsInView.generateMessageCard()
- 位置: L135-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.controller.handleEvent()`
- 参照: `this.recentBrowsing`, `this.selectedTab`

## SyncedTabsInView.onOpenLink()
- 位置: L167-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.syncedTabsTabs.record()`, `navigateToLink()`
- 条件付き依存: `if (this.controller.searchQuery)` → `Glean.firefoxview.cumulativeSearches[ this.recentBrowsing ? "recentbrowsing" : "syncedtabs" ].accumulateSingleSample()`
- 参照: `Glean.firefoxview.cumulativeSearches`, `this.controller.searchQuery`, `this.cumulativeSearches`, `this.recentBrowsing`

## SyncedTabsInView.onContextMenu()
- 位置: L182-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.querySelector()`, `e.target.querySelector("panel-list").toggle()`
- 参照: `e.detail.originalEvent`, `e.originalTarget`, `this.triggerNode`

## SyncedTabsInView.onCloseTab()
- 位置: L187-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (tertiaryActionClass === "dismiss-button")` → `this.controller.requestCloseRemoteTab()`
- 条件付き依存: `if (tertiaryActionClass === "undo-button")` → `this.controller.removePendingTabToClose()`
- 参照: `e.originalTarget`

## SyncedTabsInView.panelListTemplate()
- 位置: L199-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `this.copyLink`, `this.openInNewPrivateWindow`, `this.openInNewWindow`

## SyncedTabsInView.noDeviceTabsTemplate()
- 位置: L223-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`, `ifDefined()`, `when()`
- 参照: `this.controller.searchQuery`, `this.recentBrowsing`

## SyncedTabsInView.onSearchQuery()
- 位置: L259-268
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.recentBrowsing)` → `Glean.firefoxviewNext.searchInitiatedSearch.record()`
- 参照: `e.detail.query`, `this.controller.searchQuery`, `this.cumulativeSearches`, `this.recentBrowsing`, `this.showAll`

## SyncedTabsInView.deviceTemplate()
- 位置: L270-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.panelListTemplate()`
- 参照: `this.controller.searchQuery`, `this.maxTabsLength`, `this.onCloseTab`, `this.onContextMenu`, `this.onOpenLink`, `this.recentBrowsing`, `this.showAll`

## SyncedTabsInView.generateTabList()
- 位置: L293-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.getRenderInfo()`
- 条件付き依存: `if (tabItems.length)` → `this.deviceTemplate()`
- 条件付き依存: `if (tabItems.length)` → `html()`
- 条件付き依存: `if (tabItems.length)` → `renderArray.push()`
- 条件付き依存: `if (tabItems.length)` → `this.isShowAllLinkVisible()`
- 条件付き依存: `if (this.isShowAllLinkVisible(tabItems))` → `renderArray.push()`
- 条件付き依存: `if (this.isShowAllLinkVisible(tabItems))` → `html()`
- 条件付き依存: `if (!(tabItems.length))` → `renderArray.push()`
- 条件付き依存: `if (!(tabItems.length))` → `this.noDeviceTabsTemplate()`
- 条件付き依存: `if (!(tabItems.length))` → `Boolean()`
- 参照: `renderInfo[id].deviceType`, `renderInfo[id].name`, `renderInfo[id].tabItems`, `renderInfo[id].tabs.length`, `tabItems.length`, `this.enableShowAll`, `this.recentBrowsing`

## SyncedTabsInView.isShowAllLinkVisible()
- 位置: L345-352
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabItems.length`, `this.controller.searchQuery`, `this.maxTabsLength`, `this.recentBrowsing`, `this.showAll`

## SyncedTabsInView.enableShowAll()
- 位置: L354-366
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `event.preventDefault()`
- 条件付き依存: `if ( event.type == "click" || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `Glean.firefoxviewNext.searchShowAllShowallbutton.record()`
- 参照: `event.code`, `event.type`, `this.showAll`

## SyncedTabsInView.generateCardContent()
- 位置: L368-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.getMessageCard()`, `this.generateMessageCard()`, `this.generateTabList()`

## SyncedTabsInView.render()
- 位置: L375-449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `html()`, `renderArray.push()`
- 条件付き依存: `if (!this.recentBrowsing)` → `renderArray.push()`
- 条件付き依存: `if (!this.recentBrowsing)` → `html()`
- 条件付き依存: `if (!this.recentBrowsing)` → `when()`
- 条件付き依存: `if (!this.recentBrowsing)` → `this.controller.handleEvent()`
- 条件付き依存: `if (this.recentBrowsing)` → `renderArray.push()`
- 条件付き依存: `if (this.recentBrowsing)` → `html()`
- 条件付き依存: `if (this.recentBrowsing)` → `this.generateCardContent()`
- 条件付き依存: `if (!(this.recentBrowsing))` → `renderArray.push()`
- 条件付き依存: `if (!(this.recentBrowsing))` → `html()`
- 条件付き依存: `if (!(this.recentBrowsing))` → `this.generateCardContent()`
- 参照: `TabsSetupFlowManager.isTabSyncSetupComplete`, `this.controller.currentSetupStateIndex`, `this.controller.currentSyncedTabs.length`, `this.onSearchQuery`, `this.open`, `this.recentBrowsing`
- XPCOM: `Services.prefs`

## SyncedTabsInView.updated()
- 位置: L451-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleVisibilityInCardContainer()`
- 参照: `this.fullyUpdated`
