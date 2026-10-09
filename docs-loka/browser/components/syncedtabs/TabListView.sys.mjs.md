# browser/components/syncedtabs/TabListView.sys.mjs

source: browser/components/syncedtabs/TabListView.sys.mjs
source-hash: 308e6b43869b1780c956ccf0fdc7ff14e48adac5
lines: 654

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getContextMenu()
- 位置: L14-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getChromeWindow()`, `getChromeWindow(window).document.getElementById()`

## getTabsFilterContextMenu()
- 位置: L20-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getChromeWindow()`, `getChromeWindow(window).document.getElementById()`

## TabListView()
- 位置: L34-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._attachFixedListeners()`, `this._doc.createElement()`, `this._doc.getElementById()`, `this._doc.querySelector()`, `this._setupContextMenu()`
- 参照: `this._clientTemplate`, `this._doc`, `this._emptyClientTemplate`, `this._tabTemplate`, `this._tabsContainerTemplate`, `this._window`, `this._window.document`, `this.container`, `this.props`, `this.tabsFilter`

## render()
- 位置: L56-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._create()`
- 条件付き依存: `if (state.canUpdateAll)` → `this._update()`
- 条件付き依存: `if (state.canUpdateInput)` → `this._updateSearchBox()`
- 条件付き依存: `if (state.canUpdateInput)` → `this._createList()`
- 参照: `state.canUpdateAll`, `state.canUpdateInput`

## _create()
- 位置: L73-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._attachListListeners()`, `this._clearChilden()`, `this._createList()`, `this._doc.importNode()`, `this._updateSearchBox()`, `this.container.appendChild()`, `this.container.querySelector()`
- 参照: `this._doc.importNode( this._tabsContainerTemplate.content, true ).firstElementChild`, `this._tabsContainerTemplate.content`, `this.list`

## _createList()
- 位置: L89-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearChilden()`
- 条件付き依存: `if (state.filter)` → `this._renderFilteredClient()`
- 条件付き依存: `if (!(state.filter))` → `this._renderClient()`
- 条件付き依存: `if (this.list.firstElementChild)` → `this.list.firstElementChild.querySelector()`
- 条件付き依存: `if (firstTab)` → `firstTab.setAttribute()`
- 参照: `state.clients`, `state.filter`, `this.list`, `this.list.firstElementChild`

## destroy()
- 位置: L108-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._teardownContextMenu()`, `this.container.remove()`

## _update()
- 位置: L113-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.tabs.forEach()`, `this._doc.getElementById()`, `this._updateSearchBox()`, `this._updateTab()`
- 条件付き依存: `if (clientNode)` → `this._updateClient()`
- 参照: `client.id`, `state.clients`

## _renderFilteredClient()
- 位置: L131-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.tabs.forEach()`, `this._renderTab()`, `this.list.appendChild()`

## _updateLastSyncTitle()
- 位置: L138-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getChromeWindow()`, `getChromeWindow(this._window).gSync.formatLastSyncDate()`, `itemNode.setAttribute()`
- 参照: `this._window`

## _renderClient()
- 位置: L146-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.tabs.forEach()`, `itemNode.addEventListener()`, `itemNode.querySelector()`, `tabsList.appendChild()`, `this._createClient()`, `this._createEmptyClient()`, `this._renderTab()`, `this._updateClient()`, `this._updateLastSyncTitle()`, `this.list.appendChild()`
- 参照: `client.lastModified`, `client.tabs.length`

## _renderTab()
- 位置: L167-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._createTab()`, `this._updateTab()`

## _createClient()
- 位置: L173-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._doc.importNode()`
- 参照: `this._clientTemplate.content`, `this._doc.importNode(this._clientTemplate.content, true) .firstElementChild`

## _createEmptyClient()
- 位置: L178-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._doc.importNode()`
- 参照: `this._doc.importNode(this._emptyClientTemplate.content, true) .firstElementChild`, `this._emptyClientTemplate.content`

## _createTab()
- 位置: L183-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._doc.importNode()`
- 参照: `this._doc.importNode(this._tabTemplate.content, true) .firstElementChild`, `this._tabTemplate.content`

## _clearChilden()
- 位置: L188-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parent.firstChild.remove()`
- 参照: `parent.firstChild`, `this.container`

## _attachFixedListeners()
- 位置: L196-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onFilter.bind()`, `this.onFilterBlur.bind()`, `this.onFilterFocus.bind()`, `this.tabsFilter.addEventListener()`

## _attachListListeners()
- 位置: L203-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.list.addEventListener()`, `this.onClick.bind()`, `this.onKeyDown.bind()`, `this.onMouseUp.bind()`

## _updateSearchBox()
- 位置: L209-214
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (state.inputFocused)` → `this.tabsFilter.focus()`
- 参照: `state.filter`, `state.inputFocused`, `this.tabsFilter.value`

## _updateClient()
- 位置: L223-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `itemNode.querySelector()`, `itemNode.setAttribute()`, `this._updateLastSyncTitle()`
- 条件付き依存: `if (item.closed)` → `itemNode.classList.add()`
- 条件付き依存: `if (!(item.closed))` → `itemNode.classList.remove()`
- 条件付き依存: `if (item.selected)` → `itemNode.classList.add()`
- 条件付き依存: `if (!(item.selected))` → `itemNode.classList.remove()`
- 条件付き依存: `if (item.focused)` → `itemNode.focus()`
- 参照: `item.clientType`, `item.closed`, `item.focused`, `item.id`, `item.lastModified`, `item.name`, `item.selected`, `itemNode.dataset.id`, `itemNode.querySelector(".item-title").textContent`

## _updateTab()
- 位置: L251-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `itemNode.querySelector()`, `itemNode.setAttribute()`
- 条件付き依存: `if (item.selected)` → `itemNode.classList.add()`
- 条件付き依存: `if (!(item.selected))` → `itemNode.classList.remove()`
- 条件付き依存: `if (item.focused)` → `itemNode.focus()`
- 条件付き依存: `if (item.icon)` → `itemNode.querySelector()`
- 参照: `icon.style.backgroundImage`, `item.client`, `item.focused`, `item.icon`, `item.selected`, `item.title`, `item.url`, `itemNode.dataset.url`, `itemNode.querySelector(".item-title").textContent`

## onMouseUp()
- 位置: L272-277
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.which == 2)` → `this.onClick()`
- 参照: `event.which`

## onClick()
- 位置: L279-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`, `itemNode.classList.contains()`, `this._findParentItemNode()`, `this._getSelectionPosition()`, `this.props.onSelectRow()`
- 条件付き依存: `if (url)` → `this.onOpenSelected()`
- 条件付き依存: `if (itemNode.classList.contains("client"))` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (where != "current")` → `this._openAllClientTabs()`
- 条件付き依存: `if ( event.target.classList.contains("item-twisty-container") && event.which != 2 )` → `this.props.onToggleBranch()`
- 参照: `event.target`, `event.which`, `itemNode.dataset.id`, `itemNode.dataset.url`

## onKeyDown()
- 位置: L317-332
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.keyCode == this._window.KeyEvent.DOM_VK_DOWN)` → `event.preventDefault()`
- 条件付き依存: `if (event.keyCode == this._window.KeyEvent.DOM_VK_DOWN)` → `this.props.onMoveSelectionDown()`
- 条件付き依存: `if (event.keyCode == this._window.KeyEvent.DOM_VK_UP)` → `event.preventDefault()`
- 条件付き依存: `if (event.keyCode == this._window.KeyEvent.DOM_VK_UP)` → `this.props.onMoveSelectionUp()`
- 条件付き依存: `if (event.keyCode == this._window.KeyEvent.DOM_VK_RETURN)` → `this.container.querySelector()`
- 条件付き依存: `if (selectedNode.dataset.url)` → `this.onOpenSelected()`
- 条件付き依存: `if (selectedNode)` → `this.props.onToggleBranch()`
- 参照: `event.keyCode`, `selectedNode.dataset.id`, `selectedNode.dataset.url`, `this._window.KeyEvent.DOM_VK_DOWN`, `this._window.KeyEvent.DOM_VK_RETURN`, `this._window.KeyEvent.DOM_VK_UP`

## onBookmarkTab()
- 位置: L334-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSelectedTabNode()`
- 条件付き依存: `if (item)` → `item.querySelector()`
- 条件付き依存: `if (item)` → `this.props.onBookmarkTab()`
- 参照: `item.dataset.url`, `item.querySelector(".item-title").textContent`

## onCopyTabLocation()
- 位置: L342-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSelectedTabNode()`
- 条件付き依存: `if (item)` → `this.props.onCopyTabLocation()`
- 参照: `item.dataset.url`

## onOpenSelected()
- 位置: L349-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.whereToOpenLink()`, `this.props.onOpenTab()`

## onOpenSelectedFromContextMenu()
- 位置: L354-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSelectedTabNode()`
- 条件付き依存: `if (item)` → `event.target.getAttribute()`
- 条件付き依存: `if (item)` → `event.target.hasAttribute()`
- 条件付き依存: `if (item)` → `this.props.onOpenTab()`
- 参照: `item.dataset.url`

## onOpenSelectedInContainerTab()
- 位置: L365-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSelectedTabNode()`
- 条件付き依存: `if (item)` → `this.props.onOpenTab()`
- 条件付き依存: `if (item)` → `parseInt()`
- 参照: `event.target?.dataset.usercontextid`, `item.dataset.url`

## onOpenAllInTabs()
- 位置: L375-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSelectedClientNode()`
- 条件付き依存: `if (item)` → `this._openAllClientTabs()`

## onFilter()
- 位置: L382-389
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (query)` → `this.props.onFilter()`
- 条件付き依存: `if (!(query))` → `this.props.onClearFilter()`
- 参照: `event.target.value`

## onFilterFocus()
- 位置: L391-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.props.onFilterFocus()`

## onFilterBlur()
- 位置: L394-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.props.onFilterBlur()`

## _getSelectedTabNode()
- 位置: L398-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isTab()`, `this.container.querySelector()`
- 参照: `item.dataset.url`

## _getSelectedClientNode()
- 位置: L406-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isClient()`, `this.container.querySelector()`

## _setupContextMenu()
- 位置: L415-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getMenu()`, `menu.addEventListener()`, `this._window.addEventListener()`
- 参照: `this._window`

## _teardownContextMenu()
- 位置: L426-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getMenu()`, `menu.removeEventListener()`, `this._window.removeEventListener()`
- 参照: `this._window`

## handleEvent()
- 位置: L438-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`, `event.target.getAttribute()`, `menu.getAttribute()`, `this.handleContentContextMenuCommand()`, `this.handleContextMenu()`, `this.handleTabsFilterContextMenuCommand()`, `this.onOpenSelectedInContainerTab()`
- 条件付き依存: `if ( event.target.getAttribute("id") == "SyncedTabsSidebarTabsFilterContext" )` → `this.handleTabsFilterContextMenuShown()`
- 参照: `event.type`

## handleTabsFilterContextMenuShown()
- 位置: L474-493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.isCommandEnabled()`, `document.commandDispatcher.getControllerForCommand()`, `item.getAttribute()`, `item.hasAttribute()`
- 条件付き依存: `if (focusedElement != this.tabsFilter.inputField)` → `this.tabsFilter.focus()`
- 条件付き依存: `if (controller.isCommandEnabled(command))` → `item.removeAttribute()`
- 条件付き依存: `if (!(controller.isCommandEnabled(command)))` → `item.setAttribute()`
- 参照: `document.commandDispatcher.focusedElement`, `event.target.children`, `event.target.ownerDocument`, `this.tabsFilter.inputField`

## handleContentContextMenuCommand()
- 位置: L495-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `this.onBookmarkTab()`, `this.onCopyTabLocation()`, `this.onOpenAllInTabs()`, `this.onOpenSelectedFromContextMenu()`, `this.props.onSyncRefresh()`

## handleTabsFilterContextMenuCommand()
- 位置: L520-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.doCommand()`, `dispatcher.focusedElement.controllers.getControllerForCommand()`, `event.target.getAttribute()`, `getChromeWindow()`
- 参照: `getChromeWindow(this._window).document.commandDispatcher`, `this._window`

## handleContextMenu()
- 位置: L528-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.openPopupAtScreen()`
- 条件付き依存: `if (event.target == this.tabsFilter)` → `getTabsFilterContextMenu()`
- 条件付き依存: `if (!(event.target == this.tabsFilter))` → `this._findParentItemNode()`
- 条件付き依存: `if (itemNode)` → `this._getSelectionPosition()`
- 条件付き依存: `if (itemNode)` → `this.props.onSelectRow()`
- 条件付き依存: `if (!(event.target == this.tabsFilter))` → `getContextMenu()`
- 条件付き依存: `if (!(event.target == this.tabsFilter))` → `this.adjustContextMenu()`
- 参照: `event.screenX`, `event.screenY`, `event.target`, `this._window`, `this.tabsFilter`

## adjustContextMenu()
- 位置: L546-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isTab()`, `this.container.querySelector()`
- 条件付き依存: `if (showTabOptions)` → `el.getAttribute()`
- 条件付き依存: `if (!(el.getAttribute("id") == "syncedTabsOpenSelectedInPrivateWindow"))` → `el.getAttribute()`
- 条件付き依存: `if ( el.getAttribute("id") === "syncedTabsOpenSelectedInContainerTab" )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( el.getAttribute("id") === "syncedTabsOpenSelectedInContainerTab" )` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( el.getAttribute("id") === "syncedTabsOpenSelectedInContainerTab" )` → `getChromeWindow()`
- 条件付き依存: `if (!( el.getAttribute("id") === "syncedTabsOpenSelectedInContainerTab" ))` → `el.getAttribute()`
- 条件付き依存: `if (!(showTabOptions))` → `el.getAttribute()`
- 条件付き依存: `if (el.getAttribute("id") == "syncedTabsOpenAllInTabs")` → `item.querySelectorAll()`
- 条件付き依存: `if (!(el.getAttribute("id") == "syncedTabsOpenAllInTabs"))` → `el.getAttribute()`
- 条件付き依存: `if (!(el.getAttribute("id") == "syncedTabsRefresh"))` → `el.getAttribute()`
- 参照: `el.hidden`, `el.nextElementSibling`, `lazy.PrivateBrowsingUtils.enabled`, `menu.firstElementChild`, `tabs.length`, `this._window`
- XPCOM: `Services.prefs`

## _findParentItemNode()
- 位置: L591-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.classList.contains()`
- 参照: `node.parentNode`, `this._doc.documentElement`, `this.list`

## _findParentBranchNode()
- 位置: L608-623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.classList.contains()`, `node.parentNode.classList.contains()`
- 参照: `node.parentNode`, `this._doc.documentElement`, `this.list`

## _getSelectionPosition()
- 位置: L625-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._findParentBranchNode()`, `this._indexOfNode()`
- 条件付き依存: `if (parent !== itemNode)` → `this._indexOfNode()`
- 参照: `itemNode.parentNode`, `parent.parentNode`

## _indexOfNode()
- 位置: L636-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.indexOf.call()`
- 参照: `parent.children`

## _isTab()
- 位置: L640-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.classList.contains()`

## _isClient()
- 位置: L644-646
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.classList.contains()`

## _openAllClientTabs()
- 位置: L648-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...tabs].map()`, `clientNode.querySelector()`, `this.props.onOpenTabs()`
- 参照: `clientNode.querySelector(".item-tabs-list").children`, `tab.dataset.url`
