# browser/components/sidebar/sidebar-bookmarks.mjs

source: browser/components/sidebar/sidebar-bookmarks.mjs
source-hash: 288a2c55d8d5d46eca939566652bc88cb9f85a83
lines: 1566

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `customElements.define()`

## SidebarBookmarks.#onPlacesEvents()
- 位置: async L66-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBookmarksList()`
- 条件付き依存: `if (this.searchQuery)` → `this.#searchBookmarks()`
- 条件付き依存: `if (this.searchQuery)` → `this.searchQuery.toLowerCase()`
- 参照: `this.bookmarks`, `this.searchQuery`, `this.searchResults`

## SidebarBookmarks.#initContextMenuItems()
- 位置: L80-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `q()`
- 参照: `this.#contextMenuItems`

## q()
- 位置: L81-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contextMenu.querySelector()`

## SidebarBookmarks.constructor()
- 位置: L143-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.onSearchQuery.bind()`
- 参照: `lazy.SidebarTreeView`, `this.bookmarks`, `this.onSearchQuery`, `this.searchQuery`, `this.searchResults`, `this.treeView`

## SidebarBookmarks.connectedCallback()
- 位置: L152-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.observers.addListener()`, `super.connectedCallback()`, `this.addContextMenuListeners()`, `this.addSidebarFocusedListeners()`
- 参照: `this.#onPlacesEvents`, `this.#placesEventTypes`

## SidebarBookmarks.disconnectedCallback()
- 位置: L162-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.observers.removeListener()`, `super.disconnectedCallback()`, `this.removeContextMenuListeners()`, `this.removeSidebarFocusedListeners()`
- 参照: `this.#onPlacesEvents`, `this.#placesEventTypes`

## SidebarBookmarks.firstUpdated()
- 位置: async L172-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#expandedFolderGuids.add()`, `this.getBookmarksList()`, `this.requestUpdate()`
- 参照: `this.bookmarks`, `this.sidebarController._state.bookmarksExpandedFolders`

## SidebarBookmarks.handleSidebarFocusedEvent()
- 位置: L180-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchInput?.focus()`

## SidebarBookmarks.getNodesInOrder()
- 位置: L184-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectNodesFromList()`
- 参照: `this.bookmarkList`

## SidebarBookmarks.#collectNodesFromList()
- 位置: L190-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `list.tabItems.entries()`
- 条件付き依存: `if (isFolder)` → `this.#collectNodesFromFolder()`
- 条件付き依存: `if (!(isFolder))` → `nodes.push()`
- 参照: `item.children`, `item.url`

## SidebarBookmarks.domNode()
- 位置: L201-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `list.shadowRoot.querySelector()`
- 参照: `item.guid`

## SidebarBookmarks.#collectNodesFromFolder()
- 位置: L211-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#expandedFolderGuids.has()`
- 条件付き依存: `if (folder.children.length)` → `nodes.push()`
- 条件付き依存: `if (isExpanded)` → `list.findSublistForGuid()`
- 条件付き依存: `if (sublist)` → `this.#collectNodesFromList()`
- 条件付き依存: `if (!(folder.children.length))` → `nodes.push()`
- 参照: `folder.children.length`, `folder.guid`

## SidebarBookmarks.domNode()
- 位置: L219-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `list.shadowRoot.querySelector()`
- 参照: `folder.guid`

## SidebarBookmarks.domNode()
- 位置: L237-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `list.shadowRoot.querySelector()`
- 参照: `folder.guid`

## SidebarBookmarks.setExpanded()
- 位置: L246-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.setExpanded()`
- 条件付き依存: `if (node.type === "folder")` → `node.list?.findSublistForGuid()`
- 条件付き依存: `if (node.type === "folder")` → `sublist?.closest()`
- 条件付き依存: `if (expanded)` → `this.#expandedFolderGuids.add()`
- 条件付き依存: `if (!(expanded))` → `this.#expandedFolderGuids.delete()`
- 参照: `details.open`, `node.item.guid`, `node.type`

## SidebarBookmarks.onPrimaryAction()
- 位置: L264-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.link.bookmarks.add()`, `list.dispatchEvent()`, `navigateToLink()`, `originalEvent.getModifierState()`, `row.getRootNode()`, `this.treeView.resetSelection()`
- 条件付き依存: `if (originalEvent.shiftKey)` → `list.dispatchEvent()`
- 条件付き依存: `if ( (originalEvent.type === "click" && originalEvent.getModifierState("Accel")) || (originalEvent.type === "keydown" && originalEvent.code === "Space") )` → `list.toggleRowSelection()`
- 条件付き依存: `if ( (originalEvent.type === "click" && originalEvent.getModifierState("Accel")) || (originalEvent.type === "keydown" && originalEvent.code === "Space") )` → `list.dispatchEvent()`
- 参照: `e.detail`, `e.originalTarget`, `originalEvent.code`, `originalEvent.shiftKey`, `originalEvent.type`, `row.getRootNode().host`, `row.guid`, `row.url`

## SidebarBookmarks.handleContextMenuEvent()
- 位置: L302-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `deleteBookmark.setAttribute()`, `editBookmark.setAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `openAllBookmarks.setAttribute()`, `selectedItems.some()`, `this.#hasClipboardData()`, `this.findTriggerNode()`, `this.treeView.getSelectedTabItems()`
- 条件付き依存: `if (!this.triggerNode)` → `this.#findSeparatorElement()`
- 条件付き依存: `if (!(separatorEl))` → `this.#findFolderElement()`
- 条件付き依存: `if (folderEl)` → `folderEl.classList.contains()`
- 条件付き依存: `if (folderEl)` → `folderEl.querySelector("summary")?.textContent?.trim()`
- 条件付き依存: `if (folderEl)` → `folderEl.querySelector()`
- 条件付き依存: `if (folderEl)` → `folderEl.textContent?.trim()`
- 条件付き依存: `if (folderEl)` → `lazy.PlacesUtils.isRootItem()`
- 条件付き依存: `if (!(folderEl))` → `this.findTriggerNode()`
- 条件付き依存: `if (!(this.findTriggerNode(e, "moz-input-search")))` → `e.preventDefault()`
- 条件付き依存: `if (!this.#contextMenuItems)` → `this.#initContextMenuItems()`
- 条件付き依存: `if (isMultiSelect)` → `this.#configureMultiSelectContextMenu()`
- 条件付き依存: `if (this.triggerNode.isPlaceContainer || this.triggerNode.isTagContainer)` → `this.#configureSmartFolderContextMenu()`
- 条件付き依存: `if (isFolder)` → `this.triggerNode.children?.some()`
- 条件付き依存: `if (isFolder)` → `deleteBookmark.setAttribute()`
- 条件付き依存: `if (isFolder)` → `JSON.stringify()`
- 条件付き依存: `if (!(isFolder))` → `deleteBookmark.removeAttribute()`
- 参照: `addBookmark.hidden`, `addFolder.hidden`, `addSeparator.hidden`, `child.isPlaceContainer`, `child.url`, `copyLink.hidden`, `editBookmark.hidden`, `el.disabled`, `el.hidden`, `folderEl.dataset.folderKind`, `folderEl.guid`, `folderEl.querySelector( "sidebar-bookmark-list" )?.tabItems`, `item.guid`, `lazy.PrivateBrowsingUtils.enabled`, `openAllBookmarks.disabled`, `openInContainerTab.hidden`, `openInPrivateWindow.hidden`, `paste.hidden`, `selectedItems.length`, `sepAdd.hidden`, `sepEditCopy.hidden`, `separatorEl.guid`, `showInFolder.hidden`, `sortByName.disabled`, `this.#contextMenuItems`, `this.searchQuery`, `this.selectedItems`, `this.topWindow`, `this.triggerNode`, `this.triggerNode.guid`, `this.triggerNode.isEmpty`, `this.triggerNode.isFolder`, `this.triggerNode.isPlaceContainer`, `this.triggerNode.isRootFolder`, `this.triggerNode.isSeparator`, `this.triggerNode.isTagContainer`
- XPCOM: `Services.prefs`

## SidebarBookmarks.#configureSmartFolderContextMenu()
- 位置: L463-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deleteBookmark.removeAttribute()`, `deleteBookmark.setAttribute()`, `editBookmark.setAttribute()`, `openAllBookmarks.setAttribute()`
- 参照: `addBookmark.hidden`, `addFolder.hidden`, `addSeparator.hidden`, `copy.hidden`, `copyLink.hidden`, `cut.hidden`, `deleteBookmark.hidden`, `editBookmark.disabled`, `editBookmark.hidden`, `node.isEmpty`, `node.isPlaceContainer`, `node.isTagContainer`, `node.isTagsRoot`, `openAllBookmarks.disabled`, `openAllBookmarks.hidden`, `openInContainerTab.hidden`, `openInPrivateWindow.hidden`, `openInTab.hidden`, `openInWindow.hidden`, `paste.hidden`, `sepAdd.hidden`, `sepCutCopy.hidden`, `sepEditCopy.hidden`, `sepOpenAll.hidden`, `sepOpenOptions.hidden`, `sepSort.hidden`, `showInFolder.hidden`, `sortByName.hidden`, `this.#contextMenuItems`

## SidebarBookmarks.#configureMultiSelectContextMenu()
- 位置: L532-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `deleteBookmark.setAttribute()`, `editBookmark.setAttribute()`, `openAllBookmarks.setAttribute()`, `this.#hasClipboardData()`
- 参照: `copy.hidden`, `copyLink.hidden`, `cut.hidden`, `deleteBookmark.hidden`, `editBookmark.disabled`, `editBookmark.hidden`, `openAllBookmarks.disabled`, `openAllBookmarks.hidden`, `openInContainerTab.hidden`, `openInPrivateWindow.hidden`, `openInTab.hidden`, `openInWindow.hidden`, `paste.hidden`, `selectedItems.length`, `sepCutCopy.hidden`, `sepEditCopy.hidden`, `sepOpenAll.hidden`, `sepOpenOptions.hidden`, `sepSort.hidden`, `showInFolder.hidden`, `sortByName.hidden`, `this.#contextMenuItems`

## SidebarBookmarks.#findSeparatorElement()
- 位置: L592-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.explicitOriginalTarget.flattenedTreeParentNode?.getRootNode()`, `e.originalTarget.flattenedTreeParentNode?.getRootNode()`, `el?.classList?.contains()`
- 参照: `e.explicitOriginalTarget`, `e.explicitOriginalTarget.flattenedTreeParentNode?.getRootNode().host`, `e.originalTarget.flattenedTreeParentNode`, `e.originalTarget.flattenedTreeParentNode?.getRootNode().host`

## SidebarBookmarks.#findFolderElement()
- 位置: L607-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.composedPath()`, `e.explicitOriginalTarget.flattenedTreeParentNode?.getRootNode()`, `e.originalTarget.flattenedTreeParentNode?.getRootNode()`, `el?.classList?.contains()`
- 参照: `details?.guid`, `e.explicitOriginalTarget`, `e.explicitOriginalTarget.flattenedTreeParentNode?.getRootNode().host`, `e.originalTarget.flattenedTreeParentNode`, `e.originalTarget.flattenedTreeParentNode?.getRootNode().host`, `el.guid`, `el.parentElement`, `el?.localName`

## SidebarBookmarks.handleCommandEvent()
- 位置: L633-712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.hasAttribute()`, `lazy.BrowserUtils.copyLink()`, `this.#addItem()`, `this.#addSeparator()`, `this.#copyBookmarks()`, `this.#cutBookmarks()`, `this.#deleteBookmarks()`, `this.#editBookmarkOrFolder()`, `this.#openBookmarks()`, `this.#paste()`, `this.#sortByName()`, `this.showInFolder()`, `this.showInFolder(this.triggerNode.guid).catch()`, `this.topWindow.openTrustedLinkIn()`
- 条件付き依存: `if (e.target.hasAttribute("data-usercontextid"))` → `parseInt()`
- 条件付き依存: `if (e.target.hasAttribute("data-usercontextid"))` → `e.target.getAttribute()`
- 条件付き依存: `if (e.target.hasAttribute("data-usercontextid"))` → `this.topWindow.openTrustedLinkIn()`
- 条件付き依存: `if (e.target.hasAttribute("data-usercontextid"))` → `Glean.browserUiInteraction.sidebarBookmarks.open_in_new_container_tab.add()`
- 条件付き依存: `if (label)` → `Glean.browserUiInteraction.sidebarBookmarks[label].add()`
- 参照: `Glean.browserUiInteraction.sidebarBookmarks`, `console.error`, `e.target.id`, `this.selectedItems`, `this.triggerNode`, `this.triggerNode.guid`, `this.triggerNode.title`, `this.triggerNode.url`

## SidebarBookmarks.onSecondaryAction()
- 位置: L714-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deleteBookmarks()`
- 参照: `e.detail.item`, `this.triggerNode`

## SidebarBookmarks.#editBookmarkOrFolder()
- 位置: async L719-742
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarBookmarks[ `${labelPrefix}_${outcome}` ].add()`, `lazy.PlacesUIUtils.promiseNodeLikeFromFetchInfo()`, `lazy.PlacesUIUtils.showBookmarkDialog()`, `lazy.PlacesUtils.bookmarks.fetch()`
- 参照: `Glean.browserUiInteraction.sidebarBookmarks`, `bookmark.guid`, `bookmark.isFolder`, `bookmark.isRootFolder`, `this.topWindow`

## SidebarBookmarks.#deleteBookmarks()
- 位置: async L744-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bookmarks.map()`, `bookmarks.some()`, `lazy.PlacesTransactions.Remove()`, `lazy.PlacesTransactions.Remove({ guids: bookmarks.map(b => b.guid), }).transact()`
- 参照: `b.guid`

## SidebarBookmarks.showInFolder()
- 位置: async L753-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.bookmarks.fetch()`, `this.#expandedFolderGuids.add()`, `this.#renderAncestorChain()`, `this.#scrollAndFocusBookmarkRow()`, `this.requestUpdate()`
- 参照: `ancestor.guid`, `fetchInfo.parentGuid`, `fetchInfo.path`, `this.#expandedFolderGuids`, `this.searchInput`, `this.searchInput.value`, `this.searchQuery`, `this.searchResults`, `this.sidebarController._state.bookmarksExpandedFolders`, `this.updateComplete`

## SidebarBookmarks.#renderAncestorChain()
- 位置: async L792-805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.findSublistForGuid()`, `list?.renderItemForGuid()`
- 参照: `ancestor.guid`, `fetchInfo.path`, `this.bookmarkList`

## SidebarBookmarks.#scrollAndFocusBookmarkRow()
- 位置: async L807-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findRow()`, `list.requestVirtualListUpdate()`, `row.mainEl?.focus()`, `row.scrollIntoView()`, `this.#waitForElement()`, `this.treeView.resetSelection()`, `this.treeView.selectRowInList()`
- 参照: `row.guid`, `this.bookmarkList`

## findRow()
- 位置: L808-825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `details.querySelector()`, `findRow()`
- 参照: `list.folderEls`, `list.rowEls`, `row.guid`

## SidebarBookmarks.#waitForElement()
- 位置: async L840-852
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `probe()`, `this.documentGlobal.requestAnimationFrame()`
- 参照: `this.bookmarkList?.updateComplete`

## SidebarBookmarks.#addItem()
- 位置: async L854-873
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarBookmarks[label].add()`, `lazy.PlacesUIUtils.showBookmarkDialog()`, `this.#getInsertionPoint()`
- 参照: `Glean.browserUiInteraction.sidebarBookmarks`, `dialogInfo.defaultInsertionPoint`, `dialogInfo.hiddenRows`, `this.topWindow`

## SidebarBookmarks.#getInsertionPoint()
- 位置: async L885-903
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.bookmarks.fetch()`
- 参照: `fetchInfo.parentGuid`, `node.guid`, `node.isFolder`, `this.triggerNode`

## getIndex()
- 位置: L890-890
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PlacesUtils.bookmarks.DEFAULT_INDEX`

## getIndex()
- 位置: L901-901
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `fetchInfo.index`

## SidebarBookmarks.#addSeparator()
- 位置: async L905-916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesTransactions.NewSeparator()`, `lazy.PlacesTransactions.NewSeparator({ parentGuid: fetchInfo.parentGuid, index: fetchInfo.index, }).transact()`, `lazy.PlacesUtils.bookmarks.fetch()`
- 参照: `fetchInfo.index`, `fetchInfo.parentGuid`, `this.triggerNode.guid`

## SidebarBookmarks.#openBookmarks()
- 位置: async L918-935
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarBookmarks.open_all_bookmarks.add()`, `lazy.OpenInTabsUtils.confirmOpenInTabs()`, `this.topWindow.openTrustedLinkIn()`
- 条件付き依存: `if (item.isFolder)` → `lazy.PlacesUtils.promiseBookmarksTree()`
- 条件付き依存: `if (item.isFolder)` → `urls.push()`
- 条件付き依存: `if (item.isFolder)` → `this.#collectBookmarkUrls()`
- 条件付き依存: `if (item.url)` → `urls.push()`
- 参照: `item.guid`, `item.isFolder`, `item.url`, `this.topWindow`, `urls.length`

## SidebarBookmarks.#collectBookmarkUrls()
- 位置: L937-945
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (child.uri)` → `urls.push()`
- 参照: `child.uri`, `node.children`

## SidebarBookmarks.#sortByName()
- 位置: async L947-949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesTransactions.SortByName()`, `lazy.PlacesTransactions.SortByName(this.triggerNode.guid).transact()`
- 参照: `this.triggerNode.guid`

## SidebarBookmarks.#cutBookmarks()
- 位置: L951-953
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#copyBookmarksToClipboard()`

## SidebarBookmarks.#copyBookmarks()
- 位置: L955-957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#copyBookmarksToClipboard()`

## SidebarBookmarks.#copyBookmarksToClipboard()
- 位置: L971-1020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `bookmarks.filter()`, `bookmarks.map()`, `this.#setClipboard()`, `uriItems .map()`, `uriItems .map(item => `${item.url}${lazy.PlacesUtils.endl}${item.title ?? ""}`) .join()`, `uriItems .map(item => item.url) .join()`, `xMozPlaceEntries.join()`
- 条件付き依存: `if (item.isSeparator)` → `JSON.stringify()`
- 条件付き依存: `if (item.isFolder)` → `lazy.PlacesUtils.isRootItem()`
- 条件付き依存: `if (lazy.PlacesUtils.isRootItem(item.guid))` → `JSON.stringify()`
- 条件付き依存: `if (lazy.PlacesUtils.isRootItem(item.guid))` → `lazy.PlacesUtils.bookmarks.createVirtualLinkToRoot()`
- 条件付き依存: `if (item.isFolder)` → `JSON.stringify()`
- 条件付き依存: `if (uriItems.length)` → `flavors.set()`
- 参照: `item.guid`, `item.isFolder`, `item.isSeparator`, `item.title`, `item.url`, `lazy.PlacesUtils.TYPE_PLAINTEXT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR`, `lazy.PlacesUtils.TYPE_X_MOZ_URL`, `lazy.PlacesUtils.endl`, `lazy.PlacesUtils.instanceId`, `uriItems.length`

## SidebarBookmarks.#setClipboard()
- 位置: L1022-1048
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `Services.clipboard.setData()`, `toISupports()`, `xferable.addDataFlavor()`, `xferable.init()`, `xferable.setTransferData()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsITransferable`, `Services.appinfo.name`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_ACTION`
- XPCOM: `nsIClipboard` / [`nsITransferable`](../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.appinfo` / `Services.clipboard`

## toISupports()
- 位置: L1027-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 参照: `Ci.nsISupportsString`, `s.data`
- XPCOM: [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`

## SidebarBookmarks.#hasClipboardData()
- 位置: L1050-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clipboard.hasDataMatchingFlavors()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `lazy.PlacesUtils.TYPE_PLAINTEXT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE`, `lazy.PlacesUtils.TYPE_X_MOZ_URL`
- XPCOM: `nsIClipboard` / `Services.clipboard`

## SidebarBookmarks.#paste()
- 位置: async L1061-1142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/widget/transferable;1" ].createInstance()`, `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `Services.clipboard.getData()`, `[ lazy.PlacesUtils.TYPE_X_MOZ_PLACE, lazy.PlacesUtils.TYPE_X_MOZ_URL, lazy.PlacesUtils.TYPE_PLAINTEXT, ].forEach()`, `actionValue.value .QueryInterface()`, `actionValue.value .QueryInterface(Ci.nsISupportsString) .data.split()`, `actionXferable.addDataFlavor()`, `actionXferable.getTransferData()`, `actionXferable.init()`, `data.value.QueryInterface()`, `lazy.PlacesUIUtils.handleTransferItems()`, `lazy.PlacesUtils.bookmarks.fetch()`, `lazy.PlacesUtils.unwrapNodes()`, `xferable.addDataFlavor()`, `xferable.getAnyTransferData()`, `xferable.init()`
- 条件付き依存: `if (isCut)` → `Services.clipboard.emptyClipboard()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsISupportsString`, `Ci.nsITransferable`, `data.value.QueryInterface(Ci.nsISupportsString).data`, `fetchInfo.parentGuid`, `lazy.PlacesUtils.TYPE_PLAINTEXT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_ACTION`, `lazy.PlacesUtils.TYPE_X_MOZ_URL`, `this.triggerNode.guid`, `this.triggerNode.isFolder`, `type.value`, `validNodes.length`
- XPCOM: `nsIClipboard` / [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## getIndex()
- 位置: async L1126-1126
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PlacesUtils.bookmarks.DEFAULT_INDEX`

## getIndex()
- 位置: async L1131-1131
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `fetchInfo.index`

## SidebarBookmarks.#onFolderToggle()
- 位置: L1144-1154
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isOpen)` → `this.#expandedFolderGuids.add()`
- 条件付き依存: `if (!(isOpen))` → `this.#expandedFolderGuids.delete()`
- 参照: `e.detail`, `this.#expandedFolderGuids`, `this.sidebarController._state.bookmarksExpandedFolders`

## SidebarBookmarks.onSearchQuery()
- 位置: L1156-1165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#searchBookmarks()`, `this.searchQuery.toLowerCase()`, `this.treeView.resetActiveNode()`
- 条件付き依存: `if (this.searchQuery)` → `Glean.browserUiInteraction.sidebarBookmarks.search.add()`
- 参照: `e.detail.query`, `this.bookmarks`, `this.searchQuery`, `this.searchResults`

## SidebarBookmarks.#searchBookmarks()
- 位置: L1167-1180
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (child.children)` → `results.push()`
- 条件付き依存: `if (child.children)` → `this.#searchBookmarks()`
- 条件付き依存: `if (!(child.children))` → `child.title?.toLowerCase().includes()`
- 条件付き依存: `if (!(child.children))` → `child.title?.toLowerCase()`
- 条件付き依存: `if (!(child.children))` → `child.url?.toLowerCase().includes()`
- 条件付き依存: `if (!(child.children))` → `child.url?.toLowerCase()`
- 条件付き依存: `if ( child.title?.toLowerCase().includes(query) || child.url?.toLowerCase().includes(query) )` → `results.push()`
- 参照: `child.children`, `node.children`

## SidebarBookmarks.bookmarkItemTemplate()
- 位置: L1182-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (bookmark.children)` → `html()`
- 条件付き依存: `if (bookmark.children)` → `when()`
- 条件付き依存: `if (bookmark.children)` → `this.getBookmarkList.map()`
- 条件付き依存: `if (bookmark.children)` → `this.bookmarkItemTemplate()`
- 参照: `bookmark.children`, `bookmark.title`, `lazy.virtualListEnabledPref`, `this.bookmarkItemTemplate`

## SidebarBookmarks.getBookmarksList()
- 位置: async L1214-1234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.promiseBookmarksTree()`, `this.#normalizeBookmarkNode()`, `tree.children?.sort()`
- 参照: `a.guid`, `b.guid`, `bookmarks.menuGuid`, `bookmarks.mobileGuid`, `bookmarks.toolbarGuid`, `bookmarks.unfiledGuid`, `lazy.PlacesUtils`

## SidebarBookmarks.#normalizeBookmarkNode()
- 位置: async L1236-1268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(node.children ?? []).map()`, `Promise.allSettled()`, `node.iconUri.startsWith()`, `this.#normalizeBookmarkNode()`
- 条件付き依存: `if (!(node.type === lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER))` → `node.uri?.startsWith()`
- 条件付き依存: `if ( node.type === lazy.PlacesUtils.TYPE_X_MOZ_PLACE && node.uri?.startsWith("place:") )` → `this.#expandPlaceQuery()`
- 条件付き依存: `if (l10nId)` → `bookmarkFolderLocalization.formatMessagesSync()`
- 参照: `lazy.PlacesUtils.TYPE_X_MOZ_PLACE`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `msg.value`, `node.children`, `node.guid`, `node.icon`, `node.iconUri`, `node.title`, `node.type`, `node.uri`, `node.url`

## SidebarBookmarks.#expandPlaceQuery()
- 位置: async L1282-1319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.history.queryStringToQuery()`, `this.#runPlaceQueryAsync()`, `this.#simpleFolderTargetGuid()`
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_TAGS_ROOT`, `node.children`, `node.isPlaceContainer`, `node.isTagContainer`, `node.isTagsRoot`, `node.uri`, `optionsRef.value`, `optionsRef.value.resultType`, `queryRef.value`, `queryRef.value.tags?.length`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## SidebarBookmarks.#runPlaceQueryAsync()
- 位置: L1332-1369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `entries .filter()`, `entries .filter(entry => entry.recurse) .map()`, `entries.map()`, `lazy.PlacesUtils.history.asyncExecuteLegacyQuery()`, `this.#runPlaceQueryAsync()`
- 参照: `entry.node`, `entry.node.children`, `entry.recurse`, `entry.recurse.ancestorKeys`, `entry.recurse.options`, `entry.recurse.query`

## handleResult()
- 位置: L1336-1343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resultSet.getNextRow()`, `this.#convertPlaceRow()`
- 条件付き依存: `if (entry)` → `entries.push()`

## handleError()
- 位置: L1344-1350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`
- 参照: `error.message`, `error.result`

## handleCompletion()
- 位置: L1351-1351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## SidebarBookmarks.#convertPlaceRow()
- 位置: L1383-1465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ancestorKeys.has()`, `lazy.PlacesUtils.history.queryStringToQuery()`, `new Set(ancestorKeys).add()`, `row.getResultByIndex()`, `this.#simpleFolderTargetGuid()`, `url?.startsWith()`
- 条件付き依存: `if (targetGuid)` → `nextKeys.add()`
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_TAGS_ROOT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `node.children`, `optionsRef.value`, `parentOptions.resultType`, `queryRef.value`, `queryRef.value.tags?.length`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## SidebarBookmarks.#simpleFolderTargetGuid()
- 位置: L1477-1494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.isValidGuid()`, `query.getParents()`
- 参照: `options.maxResults`, `query.hasBeginTime`, `query.hasDomain`, `query.hasEndTime`, `query.hasSearchTerms`, `query.hasUri`, `query.parentCount`, `query.tags?.length`

## SidebarBookmarks.#searchResultsTemplate()
- 位置: L1496-1517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`
- 参照: `this.onPrimaryAction`, `this.onSecondaryAction`, `this.searchQuery`, `this.searchResults`, `this.searchResults.length`

## SidebarBookmarks.render()
- 位置: L1519-1562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#openBookmarks()`, `this.#searchResultsTemplate()`, `this.bookmarks.children?.filter()`, `this.stylesheet()`, `when()`
- 参照: `b.children`, `b.children.length`, `b.guid`, `lazy.PlacesUtils.bookmarks.mobileGuid`, `this.#expandedFolderGuids`, `this.#onFolderToggle`, `this.onPrimaryAction`, `this.onSearchQuery`, `this.onSecondaryAction`, `this.searchQuery`
