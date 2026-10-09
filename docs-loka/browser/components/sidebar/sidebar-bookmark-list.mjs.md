# browser/components/sidebar/sidebar-bookmark-list.mjs

source: browser/components/sidebar/sidebar-bookmark-list.mjs
source-hash: 63533637c149bc565bd05b201f3a713fd2c78a5b
lines: 840

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SidebarBookmarkList.constructor()
- 位置: L59-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.bookmarksContext`, `this.expandedFolderGuids`, `this.getItemHeight`, `this.readOnly`

## this.getItemHeight()
- 位置: L68-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#itemHeightGetter()`

## SidebarBookmarkList.#onContainingDetailsToggle()
- 位置: L72-84
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#containingDetails?.open)` → `this.shadowRoot ?.querySelector("virtual-list") ?.triggerIntersectionObserver()`
- 条件付き依存: `if (this.#containingDetails?.open)` → `this.shadowRoot ?.querySelector()`
- 条件付き依存: `if (!(this.#containingDetails?.open))` → `this.treeView.clearSelectionForList()`
- 参照: `this.#containingDetails?.open`

## SidebarBookmarkList.connectedCallback()
- 位置: L86-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#containingDetails?.addEventListener()`, `this.closest()`
- 参照: `this.#containingDetails`, `this.#onContainingDetailsToggle`

## SidebarBookmarkList.disconnectedCallback()
- 位置: L95-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#clearHoverFolderExpand()`, `this.#containingDetails?.removeEventListener()`
- 参照: `this.#containingDetails`, `this.#onContainingDetailsToggle`

## SidebarBookmarkList.findSublistForGuid()
- 位置: L113-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `folder?.parentElement?.querySelector()`, `this.shadowRoot.querySelector()`

## SidebarBookmarkList.renderItemForGuid()
- 位置: async L132-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabItems?.findIndex()`, `virtualList.getSubListForItem()`
- 参照: `item.guid`, `subList.isVisible`, `subList.updateComplete`, `this.rootVirtualListEl`, `this.updateComplete`, `virtualList.isVisible`, `virtualList.updateComplete`

## SidebarBookmarkList.willUpdate()
- 位置: L159-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changes.has()`, `super.willUpdate()`
- 参照: `this.getItemHeight`

## this.getItemHeight()
- 位置: L164-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#itemHeightGetter()`

## SidebarBookmarkList.#itemHeightGetter()
- 位置: L175-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.children.reduce()`, `this.#itemHeightGetter()`, `this.expandedFolderGuids.has()`
- 参照: `item.children`, `item.guid`

## SidebarBookmarkList.itemTemplate()
- 位置: L199-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.currentTarget.primaryActionHandler()`, `html()`, `ifDefined()`, `this.#getBestTitleForItem()`, `this.isTabItemSelected()`, `this.treeView?.isActiveNode()`
- 条件付き依存: `if (!tabItem.url && !tabItem.children)` → `html()`
- 条件付き依存: `if (!tabItem.children.length)` → `html()`
- 条件付き依存: `if (!tabItem.children.length)` → `ifDefined()`
- 条件付き依存: `if (!tabItem.children.length)` → `this.#onFolderAuxClick()`
- 条件付き依存: `if (!tabItem.children.length)` → `this.#updateFolderTooltip()`
- 条件付き依存: `if (tabItem.children !== undefined)` → `html()`
- 条件付き依存: `if (tabItem.children !== undefined)` → `this.expandedFolderGuids.has()`
- 条件付き依存: `if (tabItem.children !== undefined)` → `this.#onFolderToggle()`
- 条件付き依存: `if (tabItem.children !== undefined)` → `ifDefined()`
- 条件付き依存: `if (tabItem.children !== undefined)` → `this.#onFolderAuxClick()`
- 条件付き依存: `if (tabItem.children !== undefined)` → `this.#updateFolderTooltip()`
- 参照: `tabItem.canClose`, `tabItem.children`, `tabItem.children.length`, `tabItem.closeRequested`, `tabItem.closedId`, `tabItem.guid`, `tabItem.icon`, `tabItem.indicators`, `tabItem.isPlaceContainer`, `tabItem.isTagContainer`, `tabItem.isTagsRoot`, `tabItem.primaryL10nArgs`, `tabItem.primaryL10nId`, `tabItem.secondaryActionClass`, `tabItem.secondaryL10nArgs`, `tabItem.secondaryL10nId`, `tabItem.tabElement`, `tabItem.url`, `this.activeIndex`, `this.currentActiveElementId`, `this.expandedFolderGuids`, `this.hasPopup`, `this.onPrimaryAction`, `this.onSecondaryAction`, `this.readOnly`, `this.searchQuery`, `this.secondaryActionClass`

## SidebarBookmarkList.#getBestTitleForItem()
- 位置: L317-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUIUtils.getBestTitleForUri()`, `lazy.PlacesUIUtils.promptLocalization.formatValueSync()`
- 参照: `tabItem.title`, `tabItem.uri`

## SidebarBookmarkList.stylesheets()
- 位置: L325-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `super.stylesheets()`

## SidebarBookmarkList.render()
- 位置: L335-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.stylesheets()`
- 条件付き依存: `if (this.searchQuery && !this.tabItems.length)` → `this.emptySearchResultsTemplate()`
- 参照: `this.#onDragEnd`, `this.#onDragLeave`, `this.#onDragOver`, `this.#onDragStart`, `this.#onDrop`, `this.activeIndex`, `this.getItemHeight`, `this.handleFocusElementInRow`, `this.itemTemplate`, `this.searchQuery`, `this.tabItems`, `this.tabItems.length`

## SidebarBookmarkList.#onFolderToggle()
- 位置: L364-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `e.target.open`

## SidebarBookmarkList.#onFolderAuxClick()
- 位置: L374-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `this.dispatchEvent()`
- 参照: `e.button`

## SidebarBookmarkList.#updateFolderTooltip()
- 位置: L388-395
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(el.scrollWidth > el.clientWidth))` → `el.removeAttribute()`
- 参照: `e.currentTarget`, `el.clientWidth`, `el.scrollWidth`, `el.title`

## SidebarBookmarkList.#findBookmarkElement()
- 位置: L397-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.classList?.contains()`
- 条件付き依存: `if (details?.guid)` → `el.textContent.trim()`
- 条件付き依存: `if (el.classList?.contains("bookmark-folder-label") && el.guid)` → `el.textContent.trim()`
- 参照: `Node.ELEMENT_NODE`, `details.guid`, `details?.guid`, `el.guid`, `el.localName`, `el.nodeType`, `el.parentElement`, `el.title`, `el.url`

## SidebarBookmarkList.#findDropTarget()
- 位置: L425-481
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.classList?.contains()`
- 条件付き依存: `if (el.localName === "sidebar-bookmark-row" && el.guid)` → `el.getBoundingClientRect()`
- 条件付き依存: `if (details?.guid)` → `el.getBoundingClientRect()`
- 条件付き依存: `if (el.classList?.contains("bookmark-folder-label") && el.guid)` → `el.getBoundingClientRect()`
- 条件付き依存: `if (el.classList?.contains("bookmark-separator") && el.guid)` → `el.getBoundingClientRect()`
- 参照: `Node.ELEMENT_NODE`, `details.guid`, `details?.guid`, `el.guid`, `el.id`, `el.localName`, `el.nodeType`, `el.parentElement`, `rect.height`, `rect.top`

## SidebarBookmarkList.#getSupportedFlavor()
- 位置: L483-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `types.includes()`
- 参照: `dataTransfer.types`, `lazy.PlacesUIUtils.SUPPORTED_FLAVORS`

## SidebarBookmarkList.#showDropIndicator()
- 位置: L493-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `indicator.classList.add()`, `listEl.getBoundingClientRect()`, `listEl.querySelector()`, `target.element.getBoundingClientRect()`, `this.shadowRoot?.querySelector()`
- 条件付き依存: `if (activeDropList && activeDropList !== this)` → `previousList.#cleanupIndicator()`
- 条件付き依存: `if (target.orientation === DROP_ON)` → `target.element.setAttribute()`
- 条件付き依存: `if (target.orientation === DROP_ON)` → `indicator.classList.remove()`
- 参照: `indicator.style.top`, `itemRect.height`, `itemRect.top`, `listRect.top`, `previousList.#dropTarget`, `target.orientation`

## SidebarBookmarkList.#cleanupIndicator()
- 位置: L523-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listEl?.querySelector()`, `listEl?.querySelector(".drag-indicator")?.classList.remove()`, `this.#clearHoverFolderExpand()`, `this.shadowRoot?.querySelector()`
- 条件付き依存: `if (this.#dropTarget?.orientation === DROP_ON)` → `this.#dropTarget.element.removeAttribute()`
- 参照: `this.#dropTarget?.orientation`

## SidebarBookmarkList.#scheduleHoverFolderExpand()
- 位置: L538-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.#clearHoverFolderExpand()`
- 条件付き依存: `if (!shouldArm)` → `this.#clearHoverFolderExpand()`
- 参照: `detailsEl.isConnected`, `detailsEl.open`, `target.element`, `target.element.localName`, `target.element.open`, `target.guid`, `target.orientation`, `target?.isFolder`, `this.#hoverFolderGuid`, `this.#hoverFolderTimer`

## SidebarBookmarkList.#clearHoverFolderExpand()
- 位置: L563-569
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#hoverFolderTimer)` → `clearTimeout()`
- 参照: `this.#hoverFolderGuid`, `this.#hoverFolderTimer`

## SidebarBookmarkList.#onDragStart()
- 位置: L571-627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.composedPath()`, `e.dataTransfer.clearData()`, `e.dataTransfer.setData()`, `e.stopPropagation()`, `this.#findBookmarkElement()`
- 条件付き依存: `if (this.readOnly)` → `e.preventDefault()`
- 条件付き依存: `if (this.readOnly)` → `e.stopPropagation()`
- 条件付き依存: `if (!item)` → `e.preventDefault()`
- 条件付き依存: `if (item.isSeparator)` → `JSON.stringify()`
- 条件付き依存: `if (item.isFolder)` → `lazy.PlacesUtils.isRootItem()`
- 条件付き依存: `if (lazy.PlacesUtils.isRootItem(item.guid))` → `lazy.PlacesUtils.bookmarks.createVirtualLinkToRoot()`
- 条件付き依存: `if (lazy.PlacesUtils.isRootItem(item.guid))` → `JSON.stringify()`
- 条件付き依存: `if (!(lazy.PlacesUtils.isRootItem(item.guid)))` → `JSON.stringify()`
- 条件付き依存: `if (!(item.isFolder))` → `JSON.stringify()`
- 条件付き依存: `if (url)` → `e.dataTransfer.setData()`
- 参照: `e.dataTransfer.effectAllowed`, `item.guid`, `item.isFolder`, `item.isSeparator`, `item.title`, `item.url`, `lazy.PlacesUtils.TYPE_PLAINTEXT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR`, `lazy.PlacesUtils.TYPE_X_MOZ_URL`, `lazy.PlacesUtils.instanceId`, `payload.uri`, `this.#draggedGuid`, `this.readOnly`

## SidebarBookmarkList.#onDragOver()
- 位置: L629-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.composedPath()`, `e.preventDefault()`, `e.stopPropagation()`, `lazy.PlacesUIUtils.PLACES_FLAVORS.includes()`, `this.#findDropTarget()`, `this.#getSupportedFlavor()`, `this.#isFixedSortFolderTarget()`, `this.#scheduleHoverFolderExpand()`, `this.#showDropIndicator()`
- 条件付き依存: `if (this.readOnly)` → `this.#cleanupIndicator()`
- 条件付き依存: `if (!target)` → `this.#getFolderDropTarget()`
- 条件付き依存: `if ( !target || target.guid === this.#draggedGuid || this.#isFixedSortFolderTarget(target) )` → `this.#cleanupIndicator()`
- 条件付き依存: `if ( this.#dropTarget?.orientation === DROP_ON && (this.#dropTarget.element !== target.element || target.orientation !== DROP_ON) )` → `this.#dropTarget.element.removeAttribute()`
- 参照: `e.clientY`, `e.dataTransfer`, `e.dataTransfer.dropEffect`, `target.element`, `target.guid`, `target.orientation`, `this.#draggedGuid`, `this.#dropTarget`, `this.#dropTarget.element`, `this.#dropTarget?.orientation`, `this.readOnly`

## SidebarBookmarkList.#getFolderDropTarget()
- 位置: L671-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closest()`
- 参照: `parentDetails.guid`, `parentDetails?.guid`

## SidebarBookmarkList.#isFixedSortFolderTarget()
- 位置: L687-693
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `target.element?.dataset?.folderKind`, `target.isFolder`, `target.orientation`

## SidebarBookmarkList.#onDragLeave()
- 位置: L695-710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShadowRoot.isInstance()`, `node.getRootNode()`, `this.#cleanupIndicator()`
- 参照: `e.relatedTarget`, `node.parentNode`, `root.host`, `this.#dropTarget`

## SidebarBookmarkList.#onDrop()
- 位置: L712-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `e.stopPropagation()`, `lazy.PlacesUIUtils.PLACES_FLAVORS.includes()`, `this.#cleanupIndicator()`, `this.#doInsert()`, `this.#getSupportedFlavor()`
- 条件付き依存: `if (this.readOnly)` → `this.#cleanupIndicator()`
- 条件付き依存: `if (flavor === TAB_DROP_TYPE)` → `this.#getNodesFromTabDrop()`
- 条件付き依存: `if (!(flavor === TAB_DROP_TYPE))` → `e.dataTransfer.getData()`
- 条件付き依存: `if (!(flavor === TAB_DROP_TYPE))` → `lazy.PlacesUtils.unwrapNodes()`
- 参照: `e.dataTransfer`, `e.dataTransfer.dropEffect`, `this.#dropTarget`, `this.readOnly`, `validNodes?.length`

## SidebarBookmarkList.#getNodesFromTabDrop()
- 位置: L753-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XULElement.isInstance()`, `dataTransfer.mozGetDataAt()`
- 条件付き依存: `if ( XULElement.isInstance(data) && data.localName === "tab" && data.documentGlobal.isChromeWindow )` → `nodes.push()`
- 条件付き依存: `if (!( XULElement.isInstance(data) && data.localName === "tab" && data.documentGlobal.isChromeWindow ))` → `XULElement.isInstance()`
- 条件付き依存: `if ( XULElement.isInstance(data) && data.localName === "tab-split-view-wrapper" && data.documentGlobal.isChromeWindow )` → `nodes.push()`
- 参照: `data.documentGlobal.isChromeWindow`, `data.label`, `data.linkedBrowser.currentURI`, `data.localName`, `data.tabs`, `dataTransfer.mozItemCount`, `lazy.PlacesUtils.TYPE_X_MOZ_URL`, `tab.label`, `tab.linkedBrowser.currentURI?.spec`, `uri?.spec`

## SidebarBookmarkList.#doInsert()
- 位置: async L789-824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUIUtils.handleTransferItems()`
- 条件付き依存: `if (!(target.orientation === DROP_ON))` → `lazy.PlacesUtils.bookmarks.fetch()`
- 参照: `fetchInfo.parentGuid`, `target.guid`, `target.orientation`

## getIndex()
- 位置: async L795-795
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PlacesUtils.bookmarks.DEFAULT_INDEX`

## getIndex()
- 位置: async L812-815
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `fetchInfo.index`, `target.orientation`

## SidebarBookmarkList.#onDragEnd()
- 位置: L826-830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cleanupIndicator()`
- 参照: `this.#draggedGuid`, `this.#dropTarget`

## SidebarBookmarkRow.tooltipText()
- 位置: L835-837
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.title`, `this.url`
