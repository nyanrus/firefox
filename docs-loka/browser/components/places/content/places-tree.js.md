# browser/components/places/content/places-tree.js

source: browser/components/places/content/places-tree.js
source-hash: e51d68cd6898e9fc5057ce1017b7f8169a3246c2
lines: 887

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`, `customElements.get()`

## MozPlacesTree.constructor()
- 位置: L15-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.commandDispatcher.updateCommands()`, `event.preventDefault()`, `event.stopPropagation()`, `super()`, `this._controller.setDataTransfer()`, `this.addEventListener()`, `this.controller.canMoveNode()`, `this.getCellAt()`, `this.getFirstVisibleRow()`, `this.treeBody.getBoundingClientRect()`, `this.view.canDrop()`, `this.view.nodeForTreeIndex()`, `win.document.commandDispatcher.updateCommands()`
- 条件付き依存: `if (this.disableUserActions)` → `event.preventDefault()`
- 条件付き依存: `if (this.disableUserActions)` → `event.stopPropagation()`
- 条件付き依存: `if (!node.parent)` → `event.preventDefault()`
- 条件付き依存: `if (!node.parent)` → `event.stopPropagation()`
- 条件付き依存: `if (!(cell.row == -1))` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsContainer(node) && eventY > rowHeight * 0.75 ))` → `PlacesUtils.nodeIsContainer()`
- 参照: `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesControllerDragHelper.currentDropTarget`, `cell.row`, `event.clientX`, `event.clientY`, `event.dataTransfer`, `event.dataTransfer.effectAllowed`, `event.target.localName`, `node.parent`, `nodes.length`, `this._cachedInsertionPoint`, `this._isDragSource`, `this.disableUserActions`, `this.result.root`, `this.rowHeight`, `this.selectedNodes`, `this.treeBody.getBoundingClientRect().y`, `win.parent`, `window.top`
- XPCOM: `nsITreeView`

## MozPlacesTree.connectedCallback()
- 位置: L134-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.delayConnectedCallback()`, `window.addEventListener()`
- 参照: `this._active`, `this._contextMenuShown`, `this.disconnectedCallback`, `this.place`

## MozPlacesTree.controller()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._controller`

## MozPlacesTree.disableUserActions()
- 位置: L156-162
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (val)` → `this.setAttribute()`
- 条件付き依存: `if (!(val))` → `this.removeAttribute()`

## MozPlacesTree.disableUserActions()
- 位置: L164-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.view()
- 位置: L173-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.getOwnPropertyDescriptor()`, `Object.getOwnPropertyDescriptor( // eslint-disable-next-line no-undef XULTreeElement.prototype, "view" ).set.call()`
- 参照: `XULTreeElement.prototype`, `this._view`

## MozPlacesTree.view()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._view`

## MozPlacesTree.associatedElement()
- 位置: L188-190
- 役割: (未記入)
- 触るとき: (未記入)

## MozPlacesTree.flatList()
- 位置: L192-201
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.flatList != val)` → `this.setAttribute()`
- 参照: `this.flatList`, `this.place`

## MozPlacesTree.flatList()
- 位置: L203-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.result()
- 位置: L207-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view.QueryInterface()`
- 参照: `Ci.nsINavHistoryResultObserver`, `this.view.QueryInterface(Ci.nsINavHistoryResultObserver).result`
- XPCOM: [`nsINavHistoryResultObserver`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## MozPlacesTree.place()
- 位置: L215-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.queryStringToQuery()`, `this.load()`, `this.setAttribute()`
- 参照: `options.value`, `query.value`

## MozPlacesTree.place()
- 位置: L224-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.selectedCount()
- 位置: L228-230
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view?.selection?.count`

## MozPlacesTree.hasSelection()
- 位置: L232-234
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectedCount`

## MozPlacesTree.selectedNodes()
- 位置: L236-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nodes.push()`, `resultview.nodeForTreeIndex()`, `selection.getRangeAt()`, `selection.getRangeCount()`
- 参照: `max.value`, `min.value`, `this.hasSelection`, `this.view`, `this.view.selection`

## MozPlacesTree.removableSelectionRanges()
- 位置: L256-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nodes.push()`, `selection.getRangeAt()`, `selection.getRangeCount()`, `this.view.getParentIndex()`, `this.view.isContainer()`
- 条件付き依存: `if (!(this.view.getParentIndex(j) in containers))` → `range.push()`
- 条件付き依存: `if (!(this.view.getParentIndex(j) in containers))` → `resultview.nodeForTreeIndex()`
- 参照: `max.value`, `min.value`, `this.hasSelection`, `this.view`, `this.view.selection`

## MozPlacesTree.draggableSelection()
- 位置: L312-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...selectedNodes].filter()`, `selectedNodes.has()`
- 参照: `ancestor.parent`, `node.parent`, `this.selectedNodes`

## MozPlacesTree.selectedNode()
- 位置: L333-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selection.getRangeAt()`, `this.view.nodeForTreeIndex()`
- 参照: `min.value`, `this.selectedCount`, `this.view.selection`

## MozPlacesTree.singleClickOpens()
- 位置: L346-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.insertionPoint()
- 位置: L350-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.nodeIsQuery()`, `resultView.isContainer()`, `selection.getRangeAt()`, `selection.getRangeCount()`, `this._getInsertionPoint()`
- 条件付き依存: `if (!this.hasSelection)` → `this._getInsertionPoint()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUtils.asQuery(resultNode).queryOptions.queryType`, `max.value`, `resultView.selection`, `selection.count`, `this._cachedInsertionPoint`, `this.flatList`, `this.hasSelection`, `this.result.root`, `this.view`, `this.view.rowCount`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## MozPlacesTree.isDragSource()
- 位置: L421-423
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isDragSource`

## MozPlacesTree.ownerWindow()
- 位置: L425-427
- 役割: (未記入)
- 触るとき: (未記入)

## MozPlacesTree.active()
- 位置: L429-431
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._active`

## MozPlacesTree.active()
- 位置: L433-435
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._active`

## MozPlacesTree.applyFilter()
- 位置: L437-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.history.getNewQuery()`, `PlacesUtils.nodeIsHistoryContainer()`, `PlacesUtils.nodeIsTagQuery()`, `queryNode.queryOptions.clone()`, `this.load()`
- 条件付き依存: `if (folderRestrict)` → `query.setParents()`
- 条件付き依存: `if (folderRestrict)` → `Glean.sidebar.search.bookmarks.add()`
- 参照: `options.QUERY_TYPE_BOOKMARKS`, `options.RESULTS_AS_ROOTS_QUERY`, `options.RESULTS_AS_TAGS_ROOT`, `options.RESULTS_AS_URI`, `options.includeHidden`, `options.queryType`, `options.resultType`, `query.searchTerms`, `this.result.root`

## MozPlacesTree.load()
- 位置: L468-493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.history.executeQuery()`, `result.addObserver()`, `this.getAttribute()`
- 条件付き依存: `if (!this._controller)` → `this.controllers.appendController()`
- 条件付き依存: `if ( this.getAttribute("selectfirstnode") == "true" && treeView.rowCount > 0 )` → `treeView.selection.select()`
- 参照: `this._cachedInsertionPoint`, `this._controller`, `this._controller.disableUserActions`, `this.disableUserActions`, `this.view`, `treeView.rowCount`

## MozPlacesTree.selectPlaceURI()
- 位置: L503-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.assert()`, `findNode()`
- 条件付き依存: `if (child)` → `this.selectNode()`
- 条件付き依存: `if (!(child))` → `selection.clearSelection()`
- 参照: `this.hasSelection`, `this.result.root`, `this.selectedNode.uri`, `this.view.selection`

## findNode()
- 位置: L509-546
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.getChild()`, `nodesURIChecked.includes()`, `nodesURIChecked.push()`
- 条件付き依存: `if (!(childURI == placeURI))` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (PlacesUtils.nodeIsContainer(child))` → `findNode()`
- 条件付き依存: `if (PlacesUtils.nodeIsContainer(child))` → `PlacesUtils.asContainer()`
- 参照: `child.uri`, `container.childCount`, `container.containerOpen`, `container.uri`

## MozPlacesTree.selectNode()
- 位置: L572-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureRowIsVisible()`, `view.selection.select()`, `view.treeIndexForNode()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `parents.push()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `view.treeIndexForNode()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `view.isContainer()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `view.isContainerOpen()`
- 条件付き依存: `if ( index != -1 && view.isContainer(index) && !view.isContainerOpen(index) )` → `view.toggleOpenState()`
- 参照: `node.parent`, `parent.containerOpen`, `parent.parent`, `parents.length`, `this.result.root`, `this.view`

## MozPlacesTree.toggleCutNode()
- 位置: L611-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view.toggleCutNode()`

## MozPlacesTree._getInsertionPoint()
- 位置: L615-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsTagQuery()`, `console.assert()`, `this.controller.disallowInsertion()`
- 条件付き依存: `if (index != -1)` → `resultview.nodeForTreeIndex()`
- 条件付き依存: `if (index != -1)` → `resultview.isContainer()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `this.controller.disallowInsertion()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (!(queryOptions.excludeItems || queryOptions.excludeQueries))` → `container.getChildIndex()`
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUtils.asQuery(container).query.tags`, `PlacesUtils.asQuery(result.root).queryOptions`, `container.containerOpen`, `lastSelected.containerOpen`, `lastSelected.hasChildren`, `lastSelected.parent`, `queryOptions.excludeItems`, `queryOptions.excludeQueries`, `queryOptions.sortingMode`, `result.root`, `this.result`, `this.view`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## MozPlacesTree.selectAll()
- 位置: L695-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view.selection.selectAll()`

## MozPlacesTree.selectItems()
- 位置: L709-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findNodes()`, `resultview.treeIndexForNode()`, `selection.clearSelection()`, `selection.rangedSelect()`
- 条件付き依存: `if (firstValidTreeIndex >= 0)` → `this.ensureRowIsVisible()`
- 参照: `nodes.length`, `nodesToOpen.length`, `nodesToOpen[i].containerOpen`, `result.suppressNotifications`, `selection.selectEventsSuppressed`, `this.flatList`, `this.result`, `this.result.root`, `this.view`, `this.view.selection`

## findNodes()
- 位置: L748-815
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asContainer()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsContainer()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsQuery()`, `checkedGuidsSet.add()`, `checkedGuidsSet.has()`, `findNodes()`, `guids.indexOf()`, `node.getChild()`
- 条件付き依存: `if (index == -1)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (concreteGuid != node.bookmarkGuid)` → `guids.indexOf()`
- 条件付き依存: `if (index != -1)` → `nodes.push()`
- 条件付き依存: `if (index != -1)` → `guids.splice()`
- 条件付き依存: `if (foundOne)` → `nodesToOpen.unshift()`
- 参照: `PlacesUIUtils.virtualAllBookmarksGuid`, `guids.length`, `node.bookmarkGuid`, `node.childCount`, `node.containerOpen`

## MozPlacesTree.buildContextMenu()
- 位置: L860-863
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.buildContextMenu()`
- 参照: `this._contextMenuShown`

## MozPlacesTree.destroyContextMenu()
- 位置: L865-865
- 役割: (未記入)
- 触るとき: (未記入)

## MozPlacesTree.disconnectedCallback()
- 位置: L867-880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.removeEventListener()`
- 条件付き依存: `if (this._controller)` → `this._controller.terminate()`
- 条件付き依存: `if (this._controller)` → `this.controllers.removeController()`
- 条件付き依存: `if (this.view)` → `this.view.uninit()`
- 参照: `this._controller`, `this.disconnectedCallback`, `this.view`
