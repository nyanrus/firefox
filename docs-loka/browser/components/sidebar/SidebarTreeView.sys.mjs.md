# browser/components/sidebar/SidebarTreeView.sys.mjs

source: browser/components/sidebar/SidebarTreeView.sys.mjs
source-hash: 11c6bd847e058b25e677af27a25ccb1c87b15167
lines: 657

## <module>
- 役割: (未記入)

## SidebarTreeView.constructor()
- 位置: L61-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `host.addController()`
- 参照: `this.host`, `this.multiSelect`, `this.selectedRows`

## SidebarTreeView.hostConnected()
- 位置: L69-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.host.addEventListener()`

## SidebarTreeView.hostDisconnected()
- 位置: L77-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.host.removeEventListener()`

## SidebarTreeView.treeNodes()
- 位置: L90-95
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._treeNodes)` → `this.host.getNodesInOrder()`
- 参照: `this._treeNodes`

## SidebarTreeView.hostUpdated()
- 位置: L97-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.requestVirtualListUpdate()`, `this.#invalidateCachedTreeNodes()`, `this.#updateTabStop()`, `this.treeNodes .values()`, `this.treeNodes .values() .map()`, `this.treeNodes .values() .map(node => node.list) .filter()`
- 参照: `list?.rootVirtualListEl`, `node.list`

## SidebarTreeView.handleEvent()
- 位置: L116-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearSelection()`, `this.#extendSelection()`, `this.#handleFocusRow()`, `this.#invalidateCachedTreeNodes()`, `this.#setAnchor()`
- 参照: `event.detail.guid`, `event.detail.row.guid`, `event.originalTarget`, `event.type`

## SidebarTreeView.#invalidateCachedTreeNodes()
- 位置: L140-142
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._treeNodes`

## SidebarTreeView.#setAnchor()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#selectionAnchor`

## SidebarTreeView.#resetAnchor()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setAnchor()`

## SidebarTreeView.isSelected()
- 位置: L152-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selection?.has()`, `this.selectedRows.get()`

## SidebarTreeView.toggleSelection()
- 位置: L157-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.requestVirtualListUpdate()`, `selection.has()`, `this.#getSelectedGuids()`
- 条件付き依存: `if (selection.has(guid))` → `selection.delete()`
- 条件付き依存: `if (!selection.size)` → `this.selectedRows.delete()`
- 条件付き依存: `if (!(selection.has(guid)))` → `selection.add()`
- 参照: `selection.size`

## SidebarTreeView.selectAllInList()
- 位置: L170-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.requestVirtualListUpdate()`, `selection.add()`, `this.#getSelectedGuids()`
- 参照: `list.tabItems`

## SidebarTreeView.#getSelectedGuids()
- 位置: L178-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedRows.get()`
- 条件付き依存: `if (!selection)` → `this.selectedRows.set()`

## SidebarTreeView.handleKeydown()
- 位置: L192-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.getModifierState()`, `event.key.toUpperCase()`, `event.preventDefault()`, `this.#collapseOrMoveUpToHeader()`, `this.#navigate()`
- 条件付き依存: `if (accel && event.key.toUpperCase() === this.selectAllShortcut)` → `this.#selectAll()`
- 条件付き依存: `if (from.localName === "summary")` → `this.#expandOrMoveDownFromHeader()`
- 参照: `event.code`, `event.originalTarget`, `event.shiftKey`, `from.localName`, `this.multiSelect`, `this.selectAllShortcut`

## SidebarTreeView.selectAllShortcut()
- 位置: L247-259
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._selectAllShortcut)` → `localization.formatMessagesSync()`
- 参照: `message.attributes`, `message.attributes[0].value`, `this._selectAllShortcut`

## SidebarTreeView.#selectAll()
- 位置: L267-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.originalTarget.getRootNode()`
- 条件付き依存: `if (list?.tabItems)` → `event.preventDefault()`
- 条件付き依存: `if (list?.tabItems)` → `this.selectAllInList()`
- 参照: `event.originalTarget.getRootNode().host`, `list?.tabItems`, `this.multiSelect`

## SidebarTreeView.#collapseOrMoveUpToHeader()
- 位置: L284-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.closest()`, `from.getRootNode()`, `this.#findNode()`, `this.host.setExpanded()`
- 条件付き依存: `if (container.localName === "moz-card")` → `container.classList.contains()`
- 条件付き依存: `if (container.classList.contains("nested-card"))` → `this.#focusElement()`
- 条件付き依存: `if (parentDetails)` → `this.#focusElement()`
- 条件付き依存: `if (parentDetails)` → `parentDetails.querySelector()`
- 条件付き依存: `if (parentCard?.summaryEl)` → `this.#focusElement()`
- 参照: `container.localName`, `container.parentElement.summaryEl`, `from.getRootNode().host`, `parentCard.summaryEl`, `parentCard?.summaryEl`, `this.treeNodes`

## SidebarTreeView.#expandOrMoveDownFromHeader()
- 位置: L319-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#findNode()`, `this.#navigate()`, `this.host.setExpanded()`
- 参照: `this.treeNodes`

## SidebarTreeView.#focusNode()
- 位置: L334-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.focus()`, `el.scrollIntoView()`, `newList?.requestVirtualListUpdate()`, `prevList?.requestVirtualListUpdate()`, `this.#updateTabStop()`
- 参照: `newList.activeIndex`, `node.domNode`, `node.index`, `node.list`, `node.type`, `this.#activeNode`, `this.#tabStopNode?.list`, `this.#tabStopNode?.type`

## SidebarTreeView.#focusElement()
- 位置: L360-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#findNode()`
- 条件付き依存: `if (node)` → `this.#focusNode()`
- 参照: `this.treeNodes`

## SidebarTreeView.#findNode()
- 位置: L374-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#findNodeIndex()`

## SidebarTreeView.#findNodeIndex()
- 位置: L387-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.getRootNode()`, `nodes.findIndex()`
- 参照: `element.dataset.guid`, `element.getRootNode().host`, `node.card?.summaryEl`, `node.item.guid`, `node.list`, `node.type`

## SidebarTreeView.selectRowInList()
- 位置: L404-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.requestVirtualListUpdate()`, `this.#getSelectedGuids()`, `this.#getSelectedGuids(list).add()`

## SidebarTreeView.#extendSelection()
- 位置: L418-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `list.requestVirtualListUpdate()`, `listsToUpdate.add()`, `rows.findIndex()`, `this.#getSelectedGuids()`, `this.#getSelectedGuids(list).add()`, `this.selectedRows.clear()`, `this.selectedRows.keys()`, `this.treeNodes.filter()`
- 条件付き依存: `if (!anchorList || !anchorGuid)` → `this.#setAnchor()`
- 条件付き依存: `if (!anchorList || !anchorGuid)` → `this.selectRowInList()`
- 条件付き依存: `if (anchorIndex === -1 || targetIndex === -1)` → `this.#clearSelection()`
- 条件付き依存: `if (anchorIndex === -1 || targetIndex === -1)` → `this.#setAnchor()`
- 条件付き依存: `if (anchorIndex === -1 || targetIndex === -1)` → `this.selectRowInList()`
- 参照: `item.guid`, `row.item.guid`, `row.list`, `this.#selectionAnchor`

## SidebarTreeView.#navigate()
- 位置: async L476-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearSelection()`, `this.#findNodeIndex()`, `this.#focusNode()`, `this.host.shadowRoot.querySelector()`
- 条件付き依存: `if (shouldFlushBeforeFocus)` → `requestAnimationFrame()`
- 条件付き依存: `if (boundary.type === "row")` → `this.#extendSelection()`
- 条件付き依存: `if (newSelectionIsRow)` → `this.#setAnchor()`
- 参照: `boundary.item.guid`, `boundary.list`, `boundary.type`, `newSelection.item.guid`, `newSelection.list`, `newSelection.type`, `nodes.length`, `scrollContainer.scrollHeight`, `scrollContainer.scrollTop`, `this.host.documentGlobal`, `this.treeNodes`

## SidebarTreeView.#handleFocusRow()
- 位置: L559-564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setAnchor()`
- 参照: `event.detail.guid`, `event.originalTarget`, `this.#selectionAnchor.guid`

## SidebarTreeView.getSelectedTabItems()
- 位置: L571-581
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `guids.has()`
- 条件付き依存: `if (guids.has(item.guid))` → `items.push()`
- 参照: `item.guid`, `list.tabItems`, `this.selectedRows`

## SidebarTreeView.clearSelectionForList()
- 位置: L583-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedRows.delete()`
- 条件付き依存: `if (this.#selectionAnchor.list === list)` → `this.#resetAnchor()`
- 条件付き依存: `if (this.selectedRows.delete(list))` → `list.requestVirtualListUpdate()`
- 参照: `this.#selectionAnchor.list`

## SidebarTreeView.#clearSelection()
- 位置: L592-598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.requestVirtualListUpdate()`, `this.selectedRows.clear()`, `this.selectedRows.keys()`

## SidebarTreeView.resetSelection()
- 位置: L600-603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearSelection()`, `this.#resetAnchor()`

## SidebarTreeView.resetActiveNode()
- 位置: L605-608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.host.requestUpdate()`
- 参照: `this.#activeNode`

## SidebarTreeView.isActiveNode()
- 位置: L617-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSameNode()`
- 参照: `this.#tabStopNode`

## SidebarTreeView.#updateTabStop()
- 位置: L624-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSameNode()`, `nodes.filter()`, `nodes.some()`
- 参照: `header.card.summaryTabIndex`, `this.#activeNode`, `this.#tabStopNode`, `this.treeNodes`

## isSameNode()
- 位置: L648-656
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.card`, `a.item?.guid`, `a.list`, `a.type`, `b.card`, `b.item?.guid`, `b.list`, `b.type`
