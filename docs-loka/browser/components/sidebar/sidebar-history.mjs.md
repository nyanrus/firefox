# browser/components/sidebar/sidebar-history.mjs

source: browser/components/sidebar/sidebar-history.mjs
source-hash: 0efe90481418267ed17527418f61a6dcc365303a
lines: 627

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SidebarHistory.constructor()
- 位置: L42-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `super()`, `this.handlePopupEvent.bind()`
- 参照: `lazy.HistoryController`, `lazy.SidebarTreeView`, `this.controller`, `this.handlePopupEvent`, `this.treeView`
- XPCOM: `Services.prefs`

## SidebarHistory.connectedCallback()
- 位置: L52-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesObservers.addListener()`, `doc.getElementById()`, `super.connectedCallback()`, `this._contextMenu.addEventListener()`, `this._menu.addEventListener()`, `this.addContextMenuListeners()`, `this.addSidebarFocusedListeners()`, `this.controller.updateCache()`
- 参照: `this.#placesRemovedObserver`, `this._menu`, `this._menuSortByDate`, `this._menuSortByDateSite`, `this._menuSortByLastVisited`, `this._menuSortByMostVisited`, `this._menuSortBySite`, `this.handlePopupEvent`, `this.topWindow`

## SidebarHistory.disconnectedCallback()
- 位置: L79-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesObservers.removeListener()`, `super.disconnectedCallback()`, `this._contextMenu.removeEventListener()`, `this._menu.removeEventListener()`, `this.removeContextMenuListeners()`, `this.removeSidebarFocusedListeners()`
- 参照: `this.#placesRemovedObserver`, `this.handlePopupEvent`

## SidebarHistory.handleEvent()
- 位置: L92-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.handleEvent()`, `this.updateContextMenu()`
- 参照: `e.type`

## SidebarHistory.#placesRemovedObserver()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView.resetSelection()`

## SidebarHistory.isMultipleRowsSelected()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView.getSelectedTabItems()`
- 参照: `this.treeView.getSelectedTabItems().length`

## SidebarHistory.updateContextMenu()
- 位置: L113-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.classList.contains()`
- 参照: `child.hidden`, `child.id`, `lazy.PrivateBrowsingUtils.enabled`, `this._contextMenu.children`, `this.isMultipleRowsSelected`

## SidebarHistory.handleContextMenuEvent()
- 位置: L131-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findTriggerNode()`
- 条件付き依存: `if (!this.triggerNode)` → `e.preventDefault()`
- 条件付き依存: `if (this.triggerNode.localName === "sidebar-tab-row")` → `row.getRootNode()`
- 条件付き依存: `if (this.triggerNode.localName === "sidebar-tab-row")` → `list.isTabItemSelected()`
- 条件付き依存: `if (!list.isTabItemSelected(row))` → `this.treeView.resetSelection()`
- 条件付き依存: `if (!list.isTabItemSelected(row))` → `this.treeView.selectRowInList()`
- 条件付き依存: `if (!list.isTabItemSelected(row))` → `list.dispatchEvent()`
- 参照: `row.getRootNode().host`, `row.guid`, `this.triggerNode`, `this.triggerNode.localName`

## SidebarHistory.handleCommandEvent()
- 位置: async L159-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarHistory[ `bookmark_tab_${outcome}` ].add()`, `Glean.browserUiInteraction.sidebarHistory[ `clear_all_website_data_${outcome}` ].add()`, `Glean.browserUiInteraction.sidebarHistory[ `clear_history_${outcome}` ].add()`, `lazy.Sanitizer.showUI()`, `super.handleCommandEvent()`, `this.#changeSortOption()`, `this.#deleteMultipleFromHistory()`, `this.#deleteMultipleFromHistory().catch()`, `this.#openAllInTabs()`, `this.controller.deleteFromHistory()`, `this.controller.deleteFromHistory().catch()`, `this.forgetAboutThisSite()`
- 条件付き依存: `if (label)` → `Glean.browserUiInteraction.sidebarHistory[label].add()`
- 参照: `Glean.browserUiInteraction.sidebarHistory`, `console.error`, `e.target.id`, `this.topWindow`

## SidebarHistory.#changeSortOption()
- 位置: L237-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarSortHistory.record()`, `Services.prefs.setStringPref()`, `this.controller.onChangeSortOption()`, `this.treeView.resetSelection()`
- XPCOM: `Services.prefs`

## SidebarHistory.#openAllInTabs()
- 位置: L253-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OpenInTabsUtils.confirmOpenInTabs()`, `lazy.PlacesUIUtils.openTabset()`, `tabset.push()`, `this.treeView.getSelectedTabItems()`, `this.treeView.getSelectedTabItems().map()`
- 参照: `item.url`, `this.topWindow`, `urls.length`

## SidebarHistory.#deleteMultipleFromHistory()
- 位置: L269-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.history.remove()`, `this.treeView .getSelectedTabItems()`, `this.treeView .getSelectedTabItems() .map()`
- 参照: `item.pageGuid`

## SidebarHistory.handlePopupEvent()
- 位置: L277-281
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.type == "popuphidden")` → `this.menuButton.setAttribute()`
- 参照: `e.type`

## SidebarHistory.handleSidebarFocusedEvent()
- 位置: L283-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchTextbox?.focus()`

## SidebarHistory.handleNavigateToLink()
- 位置: L287-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.link.history.add()`, `navigateToLink()`, `this.treeView.resetSelection()`, `this.treeView.selectRowInList()`
- 参照: `e.currentTarget`, `e.originalTarget.guid`, `e.originalTarget.url`

## SidebarHistory.onPrimaryAction()
- 位置: L294-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.dispatchEvent()`, `originalEvent.getModifierState()`, `this.handleNavigateToLink()`
- 条件付き依存: `if (originalEvent.shiftKey)` → `list.dispatchEvent()`
- 条件付き依存: `if ( (originalEvent.type === "click" && originalEvent.getModifierState("Accel")) || (originalEvent.type === "keydown" && originalEvent.code === "Space") )` → `list.toggleRowSelection()`
- 条件付き依存: `if ( (originalEvent.type === "click" && originalEvent.getModifierState("Accel")) || (originalEvent.type === "keydown" && originalEvent.code === "Space") )` → `list.dispatchEvent()`
- 参照: `e.currentTarget`, `e.detail`, `e.originalTarget`, `originalEvent.code`, `originalEvent.shiftKey`, `originalEvent.type`, `row.guid`

## SidebarHistory.onSecondaryAction()
- 位置: L326-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.deleteFromHistory()`, `this.controller.deleteFromHistory().catch()`
- 参照: `console.error`, `e.detail.item`, `this.triggerNode`

## SidebarHistory.onMiddleClickAction()
- 位置: L331-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleNavigateToLink()`

## SidebarHistory.onKeyDown()
- 位置: L335-344
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (e.code === "Delete" || e.code === "Backspace") && e.composedTarget.localName === "sidebar-tab-row" )` → `e.preventDefault()`
- 条件付き依存: `if ( (e.code === "Delete" || e.code === "Backspace") && e.composedTarget.localName === "sidebar-tab-row" )` → `this.controller.deleteFromHistory().catch()`
- 条件付き依存: `if ( (e.code === "Delete" || e.code === "Backspace") && e.composedTarget.localName === "sidebar-tab-row" )` → `this.controller.deleteFromHistory()`
- 参照: `console.error`, `e.code`, `e.composedTarget`, `e.composedTarget.localName`, `this.triggerNode`

## SidebarHistory.cardsTemplate()
- 位置: L349-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emptyMessageTemplate()`
- 条件付き依存: `if (this.controller.searchResults)` → `this.#searchResultsTemplate()`
- 条件付き依存: `if (!this.controller.isHistoryEmpty)` → `this.#historyCardsTemplate()`
- 参照: `this.controller.isHistoryEmpty`, `this.controller.isHistoryPending`, `this.controller.searchResults`

## SidebarHistory.#historyCardsTemplate()
- 位置: L361-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `historyVisits.map()`, `html()`, `this.#dateCardTemplate()`, `this.#siteCardTemplate()`, `this.#tabListTemplate()`, `this.getTabItems()`
- 参照: `this.controller`, `this.controller.sortOption`

## SidebarHistory.#dateCardTemplate()
- 位置: L389-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `items.map()`, `this.#siteCardTemplate()`, `this.#tabListTemplate()`, `this.getTabItems()`
- 参照: `items.length`, `items[0].time`, `items[0][1][0].time`, `this.#onCardToggle`, `this.keydownHandler`

## SidebarHistory.#siteCardTemplate()
- 位置: L415-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `this.#tabListTemplate()`, `this.getTabItems()`
- 参照: `this.#onCardToggle`, `this.keydownHandler`

## SidebarHistory.#onCardToggle()
- 位置: L440-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SidebarHistory.#emptyMessageTemplate()
- 位置: L444-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `html()`
- XPCOM: `Services.prefs`

## SidebarHistory.#searchResultsTemplate()
- 位置: L498-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#tabListTemplate()`, `this.getTabItems()`, `when()`
- 参照: `this.controller.searchQuery`, `this.controller.searchResults`, `this.controller.searchResults.length`

## SidebarHistory.#tabListTemplate()
- 位置: L525-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.controller.sortOption`, `this.handleFocusElementToCard`, `this.onKeyDown`, `this.onMiddleClickAction`, `this.onPrimaryAction`, `this.onSecondaryAction`

## SidebarHistory.onSearchQuery()
- 位置: L541-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarHistory.search.add()`, `this.controller.onSearchQuery()`, `this.treeView.resetActiveNode()`

## SidebarHistory.getTabItems()
- 位置: L547-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.map()`

## SidebarHistory.openMenu()
- 位置: L555-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._menu.openPopup()`, `this.menuButton.setAttribute()`
- 参照: `e.target`, `this.sidebarController._positionStart`

## SidebarHistory.willUpdate()
- 位置: L563-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._menuSortByDate.toggleAttribute()`, `this._menuSortByDateSite.toggleAttribute()`, `this._menuSortByLastVisited.toggleAttribute()`, `this._menuSortByMostVisited.toggleAttribute()`, `this._menuSortBySite.toggleAttribute()`
- 参照: `this.controller.sortOption`

## SidebarHistory.render()
- 位置: L586-623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.stylesheet()`
- 参照: `this.cardsTemplate`, `this.onSearchQuery`, `this.openMenu`, `this.view`
