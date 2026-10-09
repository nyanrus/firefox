# browser/components/sidebar/sidebar-opentabs.mjs

source: browser/components/sidebar/sidebar-opentabs.mjs
source-hash: 84f3e021b683f5e392492513d178e9cfe3910a90
lines: 444

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SidebarOpenTabs.constructor()
- 位置: L44-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `super()`, `this.handlePopupEvent.bind()`
- 参照: `lazy.OpenTabsController`, `lazy.SidebarTreeView`, `this.controller`, `this.handlePopupEvent`, `this.searchQuery`, `this.sortOption`, `this.treeView`, `this.windows`
- XPCOM: `Services.prefs`

## SidebarOpenTabs.connectedCallback()
- 位置: L57-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SidebarCollapsedWindows.addEventListener()`, `super.connectedCallback()`, `this.#updateWindowList()`, `this._menu.addEventListener()`, `this.addContextMenuListeners()`, `this.addSidebarFocusedListeners()`, `this.openTabsTarget.addEventListener()`, `this.openTabsTarget.readyWindowsPromise.finally()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(topWindow))` → `lazy.getTabsTargetForWindow()`
- 参照: `lazy.NonPrivateTabs`, `this._menu`, `this._menuSortByOrder`, `this._menuSortByRecency`, `this.handlePopupEvent`, `this.initialWindowsReady`, `this.openTabsTarget`, `this.topWindow`

## SidebarOpenTabs.disconnectedCallback()
- 位置: L89-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SidebarCollapsedWindows.removeEventListener()`, `super.disconnectedCallback()`, `this._menu.removeEventListener()`, `this.openTabsTarget.removeEventListener()`, `this.removeContextMenuListeners()`, `this.removeSidebarFocusedListeners()`
- 参照: `this.handlePopupEvent`

## SidebarOpenTabs.shouldUpdate()
- 位置: L103-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.shouldUpdate()`
- 参照: `this.initialWindowsReady`

## SidebarOpenTabs.handleEvent()
- 位置: L110-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.handleEvent()`, `this.#updateWindowList()`, `this.requestUpdate()`
- 参照: `e.type`

## SidebarOpenTabs.handleContextMenuEvent()
- 位置: L125-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contextMenu.querySelector()`, `this.findTriggerNode()`
- 条件付き依存: `if (!this.triggerNode)` → `e.preventDefault()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `privateWindowItem.hidden`, `this.triggerNode`

## SidebarOpenTabs.handleCommandEvent()
- 位置: async L137-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FxAccounts.config.promisePairingURI()`, `super.handleCommandEvent()`, `tabElement?.documentGlobal.gBrowser.removeTabs()`, `this.#changeSortOption()`, `this.topWindow.openTrustedLinkIn()`
- 参照: `e.target.id`, `this.triggerNode`

## SidebarOpenTabs.openMenu()
- 位置: L163-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._menu.openPopup()`, `this.menuButton.setAttribute()`
- 参照: `e.target`, `this.sidebarController._positionStart`

## SidebarOpenTabs.handlePopupEvent()
- 位置: L171-175
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.type == "popuphidden")` → `this.menuButton.setAttribute()`
- 参照: `e.type`

## SidebarOpenTabs.willUpdate()
- 位置: L177-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._menuSortByOrder.toggleAttribute()`, `this._menuSortByRecency.toggleAttribute()`
- 参照: `this.sortOption`

## SidebarOpenTabs.#changeSortOption()
- 位置: L188-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `this.requestUpdate()`
- 参照: `this.sortOption`
- XPCOM: `Services.prefs`

## SidebarOpenTabs.#updateWindowList()
- 位置: L197-199
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.openTabsTarget.currentWindows`, `this.windows`

## SidebarOpenTabs.getTabItemsForWindow()
- 位置: L201-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `this.controller.getTabListItems()`, `this.controller.getTabListItems(tabs, false).map()`, `this.openTabsTarget.getTabsForWindow()`
- 参照: `item.title`, `this.sortOption`

## SidebarOpenTabs.#activateTab()
- 位置: L213-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.focus()`
- 参照: `browserWindow.gBrowser.selectedTab`, `tabElement.documentGlobal`

## SidebarOpenTabs.#getPinnedIconSrc()
- 位置: L222-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.startsWith()`

## SidebarOpenTabs.onPrimaryAction()
- 位置: L237-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.link.open_tabs.add()`, `this.#activateTab()`
- 参照: `e.originalTarget.tabElement`

## SidebarOpenTabs.onSecondaryAction()
- 位置: L242-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabElement.documentGlobal.gBrowser.removeTabs()`
- 参照: `e.detail.item`

## SidebarOpenTabs.#onCardToggle()
- 位置: L250-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 条件付き依存: `if (event.newState === "closed")` → `lazy.SidebarCollapsedWindows.collapseWindowById()`
- 条件付き依存: `if (!(event.newState === "closed"))` → `lazy.SidebarCollapsedWindows.expandWindowById()`
- 参照: `event.currentTarget.dataset.windowId`, `event.newState`

## SidebarOpenTabs.#pinnedTabsTemplate()
- 位置: L263-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `pinnedTabItems.map()`, `this.#activateTab()`, `this.#getPinnedIconSrc()`
- 参照: `item.tabElement`, `item.tabElement?.selected`, `item.title`

## SidebarOpenTabs.#windowCardTemplate()
- 位置: L288-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `item.indicators?.includes()`, `items.filter()`, `lazy.SessionStore.getWindowId()`, `lazy.SidebarCollapsedWindows.isCollapsed()`, `this.#pinnedTabsTemplate()`, `this.getTabItemsForWindow()`, `when()`
- 条件付き依存: `if (this.searchQuery)` → `searchTabList()`
- 参照: `pinnedTabItems.length`, `this.#onCardToggle`, `this.keydownHandler`, `this.onPrimaryAction`, `this.onSecondaryAction`, `this.searchQuery`, `win.windowGlobalChild.innerWindowId`

## SidebarOpenTabs.#windowCardsTemplate()
- 位置: L335-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `searchTabList()`, `this.#windowCardTemplate()`, `this.getTabItemsForWindow()`
- 条件付き依存: `if (!(isCurrent))` → `otherCards.push()`
- 参照: `searchTabList(this.searchQuery, this.getTabItemsForWindow(win)).length`, `this.searchQuery`, `this.topWindow`, `this.windows`

## SidebarOpenTabs.#searchResultsTemplate()
- 位置: L359-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `searchTabList()`, `this.#windowCardsTemplate()`, `this.getTabItemsForWindow()`, `this.windows.reduce()`
- 条件付き依存: `if (!count)` → `html()`
- 条件付き依存: `if (!count)` → `JSON.stringify()`
- 参照: `searchTabList(this.searchQuery, this.getTabItemsForWindow(win)).length`, `this.searchQuery`

## SidebarOpenTabs.handleSidebarFocusedEvent()
- 位置: L394-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchTextbox?.focus()`

## SidebarOpenTabs.onSearchQuery()
- 位置: L398-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView.resetActiveNode()`
- 参照: `e.detail.query`, `this.searchQuery`

## SidebarOpenTabs.render()
- 位置: L403-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#searchResultsTemplate()`, `this.#windowCardsTemplate()`, `this.stylesheet()`
- 参照: `this.onSearchQuery`, `this.openMenu`, `this.searchQuery`
