# browser/components/sidebar/sidebar-syncedtabs.mjs

source: browser/components/sidebar/sidebar-syncedtabs.mjs
source-hash: 416ccc546d145b0f835e8e56482b07f51ee8ca84
lines: 477

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SyncedTabsInSidebar.constructor()
- 位置: L34-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.onSearchQuery.bind()`, `this.onSecondaryAction.bind()`
- 参照: `lazy.SidebarTreeView`, `this.onSearchQuery`, `this.onSecondaryAction`, `this.treeView`

## SyncedTabsInSidebar.connectedCallback()
- 位置: L41-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.syncedTabs.sidebarToggle.record()`, `super.connectedCallback()`, `this.addContextMenuListeners()`, `this.addSidebarFocusedListeners()`, `this.controller.addSyncObservers()`, `this.controller.updateStates()`, `this.controller.updateStates().then()`
- 参照: `this.controller.isSyncedTabsLoaded`

## SyncedTabsInSidebar.disconnectedCallback()
- 位置: L55-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.syncedTabs.sidebarToggle.record()`, `super.disconnectedCallback()`, `this.controller.removeSyncObservers()`, `this.removeContextMenuListeners()`, `this.removeSidebarFocusedListeners()`
- 参照: `this.controller.isSyncedTabsLoaded`

## SyncedTabsInSidebar.#setContextMenuItemsVisibility()
- 位置: L67-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contextMenu.querySelector()`
- 参照: `contextMenu.children`, `contextMenu.querySelector(selector).hidden`, `lastSeparator.hidden`, `menuChild.hidden`, `menuChild.localName`

## SyncedTabsInSidebar.handleContextMenuEvent()
- 位置: L100-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findTriggerNode()`
- 条件付き依存: `if (triggerNode)` → `contextMenu.querySelector()`
- 条件付き依存: `if (triggerNode)` → `closeTabMenuItem.setAttribute()`
- 条件付き依存: `if (triggerNode)` → `this.#setContextMenuItemsVisibility()`
- 条件付き依存: `if (!(triggerNode))` → `e.composedTarget.closest()`
- 条件付き依存: `if ((triggerNode = e.composedTarget.closest("summary")))` → `this.#setContextMenuItemsVisibility()`
- 条件付き依存: `if (!((triggerNode = e.composedTarget.closest("summary"))))` → `this.findTriggerNode()`
- 条件付き依存: `if (!this.triggerNode)` → `e.preventDefault()`
- 参照: `closeTabMenuItem.disabled`, `lazy.PrivateBrowsingUtils.enabled`, `privateWindowMenuItem.hidden`, `this._contextMenu`, `this.triggerNode`, `this.triggerNode.canClose`, `this.triggerNode.secondaryL10nArgs`

## SyncedTabsInSidebar.handleCommandEvent()
- 位置: async L154-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarSyncedTabs[ `bookmark_tab_${outcome}` ].add()`, `super.handleCommandEvent()`, `this.openAllSyncedTabs()`, `this.requestOrRemoveTabToClose()`, `this.topWindow.gSync.openConnectAnotherDevice()`, `this.topWindow.gSync.openDevicesManagementPage()`
- 条件付き依存: `if (label)` → `Glean.browserUiInteraction.sidebarSyncedTabs[label].add()`
- 参照: `Glean.browserUiInteraction.sidebarSyncedTabs`, `e.target.id`, `this.triggerNode.fxaDeviceId`, `this.triggerNode.secondaryActionClass`, `this.triggerNode.url`

## SyncedTabsInSidebar.openAllSyncedTabs()
- 位置: L203-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `card.querySelector()`, `tabList?.tabItems?.map()`, `tabList?.tabItems?.map(item => item.url).filter()`, `this.topWindow.gBrowser.loadTabs()`, `this.triggerNode.getRootNode()`
- 参照: `item.url`, `this.triggerNode.getRootNode().host`, `urls?.length`
- XPCOM: `Services.scriptSecurityManager`

## SyncedTabsInSidebar.handleSidebarFocusedEvent()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchTextbox?.focus()`

## SyncedTabsInSidebar.#onCardToggle()
- 位置: L220-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SyncedTabsInSidebar.handleNavigateToLink()
- 位置: L224-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.link.synced_tabs.add()`, `navigateToLink()`, `this.treeView.resetSelection()`

## SyncedTabsInSidebar.onSecondaryAction()
- 位置: L231-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestOrRemoveTabToClose()`
- 参照: `e.originalTarget`

## SyncedTabsInSidebar.requestOrRemoveTabToClose()
- 位置: L236-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (secondaryActionClass === "dismiss-button")` → `this.controller.requestCloseRemoteTab()`
- 条件付き依存: `if (secondaryActionClass === "undo-button")` → `this.controller.removePendingTabToClose()`

## SyncedTabsInSidebar.messageCardTemplate()
- 位置: L260-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.controller.handleEvent()`

## SyncedTabsInSidebar.deviceTemplate()
- 位置: L298-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.getDeviceIconSrc()`
- 参照: `this.#onCardToggle`, `this.controller.searchQuery`, `this.handleNavigateToLink`, `this.keydownHandler`, `this.onSecondaryAction`

## SyncedTabsInSidebar.noDeviceTabsTemplate()
- 位置: L329-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.getDeviceIconSrc()`

## SyncedTabsInSidebar.noSearchResultsTemplate()
- 位置: L347-358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`, `this.getDeviceIconSrc()`
- 参照: `this.controller.searchQuery`

## SyncedTabsInSidebar.deviceListTemplate()
- 位置: L365-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(this.controller.getRenderInfo()).map()`, `this.controller.getRenderInfo()`, `this.noDeviceTabsTemplate()`
- 条件付き依存: `if (tabItems.length)` → `this.deviceTemplate()`
- 条件付き依存: `if (tabItems.length)` → `this.getTabItems()`
- 条件付き依存: `if (tabs.length)` → `this.noSearchResultsTemplate()`
- 参照: `tabItems.length`, `tabs.length`

## SyncedTabsInSidebar.getTabItems()
- 位置: L382-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `items .map()`, `this.controller.isURLQueuedToClose()`
- 参照: `item.closeRequested`, `item.fxaDeviceId`, `item.url`, `this.controller.lastClosedURL`

## SyncedTabsInSidebar.getDeviceIconSrc()
- 位置: L426-439
- 役割: (未記入)
- 触るとき: (未記入)

## SyncedTabsInSidebar.render()
- 位置: L441-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.controller.getMessageCard()`, `this.deviceListTemplate()`, `this.messageCardTemplate()`, `this.stylesheet()`, `when()`
- 参照: `this.onSearchQuery`

## SyncedTabsInSidebar.onSearchQuery()
- 位置: L468-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarSyncedTabs.search.add()`, `this.requestUpdate()`, `this.treeView.resetActiveNode()`
- 参照: `e.detail.query`, `this.controller.searchQuery`
