# browser/components/places/content/treeView.js

source: browser/components/places/content/treeView.js
source-hash: 28e584f7163d2a7dc5c18d6c60f98a7afcd49110
lines: 1856

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## makeNodeDetailsKey()
- 位置: L21-32
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `nodeOrDetails.itemId`, `nodeOrDetails.time`, `nodeOrDetails.uri`

## PlacesTreeView()
- 位置: L34-44
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aContainer._controller`, `aContainer.flatList`, `this._controller`, `this._element`, `this._flatList`, `this._nodeDetails`, `this._result`, `this._rootNode`, `this._rows`, `this._selection`, `this._tree`

## wrappedJSObject()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)

## PTV__finishInit()
- 位置: L60-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sortingChanged()`
- 条件付き依存: `if (!(!this._rootNode.containerOpen))` → `this.invalidateContainer()`
- 参照: `selection.selectEventsSuppressed`, `this._result.sortingMode`, `this._rootNode`, `this._rootNode.containerOpen`, `this.selection`

## uninit()
- 位置: L82-93
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._editingObservers)` → `this._editingObservers.values()`
- 条件付き依存: `if (this._editingObservers)` → `observer.disconnect()`
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 参照: `this._editingObservers`, `this._result`

## PTV__isPlainContainer()
- 位置: L117-139
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_DATE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_DATE_SITE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_LEFT_PANE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_ROOTS_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_SITE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_TAGS_ROOT`, `Ci.nsINavHistoryQueryResultNode`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER_SHORTCUT`, `aContainer.queryOptions.resultType`, `aContainer.type`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryQueryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__getRowForNode()
- 位置: L167-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `PlacesUtils.nodeAncestors()`, `this._isPlainContainer()`
- 条件付き依存: `if (parent == this._rootNode)` → `this._rows.indexOf()`
- 条件付き依存: `if (!parentIsPlain)` → `this._rows.indexOf()`
- 条件付き依存: `if (parent == this._rootNode)` → `this._rootNode.getChildIndex()`
- 条件付き依存: `if (!(useNodeIndex && typeof aParentRow == "number"))` → `this._rows.indexOf()`
- 条件付き依存: `if (row == -1 && aForceBuild)` → `this._getRowForNode()`
- 条件付き依存: `if (row == -1 && aForceBuild)` → `parent.getChildIndex()`
- 条件付き依存: `if (row != -1)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (row != -1)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (row != -1)` → `this._nodeDetails.set()`
- 参照: `aNode.parent`, `ancestor.containerOpen`, `ancestors.length`, `this._rootNode`, `this._rows`

## PTV__getParentByChildRow()
- 位置: L244-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getNodeForRow()`, `this._rows.lastIndexOf()`
- 参照: `node.parent`, `this._rootNode`

## PTV__getNodeForRow()
- 位置: L264-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeNodeDetailsKey()`, `parent.getChild()`, `this._getParentByChildRow()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`
- 条件付き依存: `if (!rowNode)` → `this._rootNode.getChild()`
- 条件付き依存: `if (!rowNode)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (!rowNode)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (!rowNode)` → `this._nodeDetails.set()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `rowNode.getChild()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `this._nodeDetails.set()`
- 参照: `Ci.nsINavHistoryContainerResultNode`, `this._rows`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__buildVisibleSection()
- 位置: L321-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aContainer.getChild()`, `makeNodeDetailsKey()`, `this._isPlainContainer()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`, `this._rows .splice()`, `this._rows .splice(0, aFirstChildRow) .concat()`
- 条件付き依存: `if (sortingMode != Ci.nsINavHistoryQueryOptions.SORT_BY_NONE)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (sortingMode != Ci.nsINavHistoryQueryOptions.SORT_BY_NONE)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (sortingMode != Ci.nsINavHistoryQueryOptions.SORT_BY_NONE)` → `this._rows.splice()`
- 条件付き依存: `if (uri)` → `Services.xulStore.getValue()`
- 条件付き依存: `if (uri)` → `PlacesUIUtils.obfuscateUrlForXulStore()`
- 条件付き依存: `if (isopen != curChild.containerOpen)` → `aToOpen.push()`
- 条件付き依存: `if (curChild.containerOpen && curChild.childCount > 0)` → `this._buildVisibleSection()`
- 参照: `Ci.nsINavHistoryContainerResultNode`, `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `aContainer.childCount`, `aContainer.containerOpen`, `curChild.childCount`, `curChild.containerOpen`, `curChild.type`, `curChild.uri`, `document.documentURI`, `this._flatList`, `this._result.sortingMode`, `this._rows`, `this._rows.length`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.xulStore`

## PTV__countVisibleRowsForNodeAtRow()
- 位置: L410-431
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsINavHistoryContainerResultNode`, `node.indentLevel`, `rowNode.indentLevel`, `this._rows`, `this._rows.length`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__getSelectedNodesInRange()
- 位置: L433-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `nodesInfo.push()`, `selection.getRangeAt()`, `selection.getRangeCount()`, `this._tree.getFirstVisibleRow()`, `this._tree.getLastVisibleRow()`
- 参照: `max.value`, `min.value`, `this._rows`, `this.selection`

## PTV__getNewRowForRemovedNode()
- 位置: L486-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeNodeDetailsKey()`, `this._getRowForNode()`, `this._nodeDetails.get()`
- 条件付き依存: `if (parent)` → `PlacesUtils.nodeAncestors()`
- 条件付き依存: `if (parent)` → `this._getRowForNode()`
- 参照: `aOldNode.parent`, `ancestor.containerOpen`

## PTV__restoreSelection()
- 位置: L525-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getNewRowForRemovedNode()`
- 条件付き依存: `if (row != -1)` → `selection.rangedSelect()`
- 条件付き依存: `if (aNodesInfo.length == 1 && selection.count == 0)` → `Math.min()`
- 条件付き依存: `if (scrollToRow != -1)` → `this._tree.ensureRowIsVisible()`
- 参照: `aNodesInfo.length`, `aNodesInfo[0].oldRow`, `aNodesInfo[0].wasVisible`, `nodeInfo.node`, `nodeInfo.wasVisible`, `selection.count`, `this._rows.length`, `this.selection`

## PTV__convertPRTimeToString()
- 位置: L564-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dateObj.getTime()`, `dateObj.getTimezoneOffset()`, `new Date(midnight).getTimezoneOffset()`, `this._dateFormatter.format()`, `this._todayFormatter.format()`

## _todayFormatter()
- 位置: L587-596
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.intl.DateTimeFormat`, `this.__todayFormatter`
- XPCOM: `Services.intl`

## _dateFormatter()
- 位置: L599-611
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.intl.DateTimeFormat`, `this.__dateFormatter`
- XPCOM: `Services.intl`

## PTV__getColumnType()
- 位置: L622-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aColumn.element.getAttribute()`
- 参照: `aColumn.id`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_UNKNOWN`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`

## PTV__sortTypeToColumnType()
- 位置: L644-676
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_DATEADDED_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATEADDED_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_LASTMODIFIED_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_LASTMODIFIED_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TAGS_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TAGS_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TITLE_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TITLE_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_URI_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_URI_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_VISITCOUNT_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_VISITCOUNT_DESCENDING`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_UNKNOWN`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV_nodeInserted()
- 位置: L679-752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asContainer()`, `PlacesUtils.nodeIsContainer()`, `PlacesUtils.nodeIsSeparator()`, `console.assert()`, `makeNodeDetailsKey()`, `this._isPlainContainer()`, `this._nodeDetails.set()`, `this._rows.splice()`, `this._tree.rowCountChanged()`, `this.isSorted()`
- 条件付き依存: `if (aParentNode != this._rootNode)` → `this._getRowForNode()`
- 条件付き依存: `if (aParentNode.childCount == 1)` → `this._tree.invalidateRow()`
- 条件付き依存: `if (!(aNewIndex == 0 || this._isPlainContainer(aParentNode) || cc == 0))` → `PlacesUtils.nodeIsSeparator()`
- 条件付き依存: `if (!(aNewIndex == 0 || this._isPlainContainer(aParentNode) || cc == 0))` → `this.isSorted()`
- 条件付き依存: `if (!(aNewIndex == 0 || this._isPlainContainer(aParentNode) || cc == 0))` → `aParentNode.getChild()`
- 条件付き依存: `if (!separatorsAreHidden || PlacesUtils.nodeIsSeparator(node))` → `this._getRowForNode()`
- 条件付き依存: `if (row < 0)` → `aParentNode.getChild()`
- 条件付き依存: `if (row < 0)` → `this._getRowForNode()`
- 条件付き依存: `if (row < 0)` → `this._countVisibleRowsForNodeAtRow()`
- 条件付き依存: `if ( PlacesUtils.nodeIsContainer(aNode) && PlacesUtils.asContainer(aNode).containerOpen )` → `this.invalidateContainer()`
- 参照: `PlacesUtils.asContainer(aNode).containerOpen`, `aParentNode.childCount`, `this._result`, `this._rootNode`, `this._tree`

## PTV_nodeRemoved()
- 位置: L770-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `PlacesUtils.nodeIsSeparator()`, `console.assert()`, `makeNodeDetailsKey()`, `selection.getRangeCount()`, `this._countVisibleRowsForNodeAtRow()`, `this._getRowForNode()`, `this._nodeDetails.delete()`, `this._rows.splice()`, `this._tree.rowCountChanged()`, `this.isSorted()`
- 条件付き依存: `if (aNode == this._rootNode)` → `Components.Exception()`
- 条件付き依存: `if (oldRow < 0)` → `Components.Exception()`
- 条件付き依存: `if (selection.getRangeCount() == 1)` → `selection.getRangeAt()`
- 条件付き依存: `if (selection.getRangeCount() == 1)` → `this.nodeForTreeIndex()`
- 条件付き依存: `if (aParentNode != this._rootNode && !aParentNode.hasChildren)` → `this._tree.invalidateRow()`
- 条件付き依存: `if (rowToSelect != -1)` → `this.selection.rangedSelect()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`, `Cr.NS_ERROR_UNEXPECTED`, `aParentNode.hasChildren`, `max.value`, `min.value`, `this._result`, `this._rootNode`, `this._rows.length`, `this._tree`, `this.selection`

## PTV_nodeMoved()
- 位置: L833-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsSeparator()`, `console.assert()`, `makeNodeDetailsKey()`, `this._countVisibleRowsForNodeAtRow()`, `this._getRowForNode()`, `this._getSelectedNodesInRange()`, `this._nodeDetails.delete()`, `this._rows.splice()`, `this._tree.rowCountChanged()`, `this.isSorted()`, `this.nodeInserted()`
- 条件付き依存: `if (oldRow < 0)` → `Components.Exception()`
- 条件付き依存: `if (aOldParent != this._rootNode && !aOldParent.hasChildren)` → `this._tree.invalidateRow()`
- 条件付き依存: `if (nodesToReselect.length)` → `this._restoreSelection()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `aOldParent.hasChildren`, `nodesToReselect.length`, `this._result`, `this._rootNode`, `this._tree`, `this.selection.selectEventsSuppressed`

## PTV__invalidateCellValue()
- 位置: L895-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.assert()`, `this._findColumnByType()`, `this._getRowForNode()`
- 条件付き依存: `if (aColumnType == this.COLUMN_TYPE_TITLE)` → `this._tree.removeImageCacheEntry()`
- 条件付き依存: `if (column && !column.element.hidden)` → `this._tree.invalidateCell()`
- 条件付き依存: `if (aColumnType != this.COLUMN_TYPE_LASTMODIFIED)` → `this._findColumnByType()`
- 条件付き依存: `if (lastModifiedColumn && !lastModifiedColumn.hidden)` → `this._tree.invalidateCell()`
- 参照: `column.element.hidden`, `lastModifiedColumn.hidden`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TITLE`, `this._result`, `this._rootNode`, `this._tree`

## PTV_nodeTitleChanged()
- 位置: L930-932
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TITLE`

## PTV_nodeURIChanged()
- 位置: L934-944
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeNodeDetailsKey()`, `this._invalidateCellValue()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`
- 参照: `aNode.itemId`, `aNode.time`, `this.COLUMN_TYPE_URI`

## PTV_nodeIconChanged()
- 位置: L946-948
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TITLE`

## PTV_nodeHistoryDetailsChanged()
- 位置: L950-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeNodeDetailsKey()`, `this._invalidateCellValue()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`
- 参照: `aNode.itemId`, `aNode.uri`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_VISITCOUNT`

## PTV_nodeTagsChanged()
- 位置: L967-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TAGS`

## nodeKeywordChanged()
- 位置: L971-971
- 役割: (未記入)
- 触るとき: (未記入)

## PTV_nodeDateAddedChanged()
- 位置: L973-975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_DATEADDED`

## PTV_nodeLastModifiedChanged()
- 位置: L977-979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_LASTMODIFIED`

## PTV_containerStateChanged()
- 位置: L981-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.invalidateContainer()`

## PTV_invalidateContainer()
- 位置: L985-1121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.assert()`, `makeNodeDetailsKey()`, `this._buildVisibleSection()`, `this._getSelectedNodesInRange()`, `this._nodeDetails.delete()`, `this._restoreSelection()`, `this._rows.splice()`, `this._tree.beginUpdateBatch()`, `this._tree.endUpdateBatch()`, `this._tree.getAttribute()`
- 条件付き依存: `if (this._tree.getAttribute("editing"))` → `this._editingObservers.has()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this.invalidateContainer()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this._editingObservers.get()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `observer.disconnect()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this._editingObservers.delete()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `mutationObserver.observe()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this._editingObservers.set()`
- 条件付き依存: `if (!this._rootNode.containerOpen)` → `this._nodeDetails.clear()`
- 条件付き依存: `if (replaceCount)` → `this._tree.rowCountChanged()`
- 条件付き依存: `if (!(aContainer == this._rootNode))` → `this._getRowForNode()`
- 条件付き依存: `if (!(aContainer == this._rootNode))` → `this._tree.invalidateRow()`
- 条件付き依存: `if (!(aContainer == this._rootNode))` → `this._countVisibleRowsForNodeAtRow()`
- 条件付き依存: `if ( nodesToReselect.length && nodesToReselect.length == oldSelectionCount )` → `this.selection.rangedSelect()`
- 条件付き依存: `if ( nodesToReselect.length && nodesToReselect.length == oldSelectionCount )` → `this._tree.ensureRowIsVisible()`
- 条件付き依存: `if (elementsAddedCount)` → `this._tree.rowCountChanged()`
- 参照: `aContainer.containerOpen`, `item.containerOpen`, `item.parent`, `item.uri`, `nodesToReselect.length`, `parent.parent`, `parent.uri`, `this._editingObservers`, `this._flatList`, `this._result`, `this._rootNode`, `this._rootNode.containerOpen`, `this._rows`, `this._rows.length`, `this._tree`, `this.selection.count`, `this.selection.selectEventsSuppressed`, `toOpenElements.length`
- XPCOM: `Services.tm`

## PTV__findColumnByType()
- 位置: L1124-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.getColumnAt()`, `this._getColumnType()`
- 参照: `columns.count`, `this._columns`, `this._tree.columns`

## PTV__sortingChanged()
- 位置: L1145-1173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.getSortedColumn()`, `this._findColumnByType()`, `this._sortTypeToColumnType()`, `window.updateCommands()`
- 条件付き依存: `if (sortedColumn)` → `sortedColumn.element.removeAttribute()`
- 条件付き依存: `if (column)` → `column.element.setAttribute()`
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `this._result`, `this._tree`, `this._tree.columns`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__batching()
- 位置: L1176-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._inBatchMode)` → `this._tree.beginUpdateBatch()`
- 条件付き依存: `if (!(this._inBatchMode))` → `this._tree.endUpdateBatch()`
- 参照: `this._inBatchMode`, `this.selection.selectEventsSuppressed`

## result()
- 位置: L1187-1189
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._result`

## result()
- 位置: L1190-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 条件付き依存: `if (this._tree && val)` → `this._finishInit()`
- 参照: `this._cellProperties`, `this._cuttingNodes`, `this._result`, `this._result.root`, `this._rootNode`, `this._rootNode.containerOpen`, `this._tree`

## nodeForTreeIndex()
- 位置: L1223-1229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getNodeForRow()`
- 条件付き依存: `if (aIndex > this._rows.length)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this._rows.length`

## treeIndexForNode()
- 位置: L1238-1245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getRowForNode()`

## rowCount()
- 位置: L1248-1250
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._rows.length`

## selection()
- 位置: L1251-1253
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._selection`

## selection()
- 位置: L1254-1256
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._selection`

## getRowProperties()
- 位置: L1258-1260
- 役割: (未記入)
- 触るとき: (未記入)

## PTV_getCellProperties()
- 位置: L1262-1333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aColumn.element.getAttribute()`, `this._cellProperties.get()`, `this._cuttingNodes.has()`, `this._getNodeForRow()`
- 条件付き依存: `if (properties === undefined)` → `PlacesUtils.containerTypes.includes()`
- 条件付き依存: `if (nodeType == Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY)` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(node)))` → `PlacesUtils.nodeIsDay()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsDay(node)))` → `PlacesUtils.nodeIsHost()`
- 条件付き依存: `if (!(nodeType == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node))` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (properties === undefined)` → `this._cellProperties.set()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `PlacesUtils.bookmarks.menuGuid`, `PlacesUtils.bookmarks.toolbarGuid`, `PlacesUtils.bookmarks.unfiledGuid`, `PlacesUtils.bookmarks.virtualMenuGuid`, `PlacesUtils.bookmarks.virtualToolbarGuid`, `PlacesUtils.bookmarks.virtualUnfiledGuid`, `PlacesUtils.virtualAllBookmarksGuid`, `PlacesUtils.virtualDownloadsGuid`, `PlacesUtils.virtualHistoryGuid`, `PlacesUtils.virtualTagsGuid`, `aColumn.id`, `node.bookmarkGuid`, `node.itemId`, `node.type`, `node.uri`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## getColumnProperties()
- 位置: L1335-1337
- 役割: (未記入)
- 触るとき: (未記入)

## PTV_isContainer()
- 位置: L1339-1360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsContainer()`, `PlacesUtils.nodeIsQuery()`, `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(node) && !PlacesUtils.nodeIsTagQuery(node))` → `PlacesUtils.asQuery()`
- 参照: `PlacesUtils.asQuery(node).queryOptions.expandQueries`, `node.hasChildren`, `this._flatList`, `this._rows`

## PTV_isContainerOpen()
- 位置: L1362-1369
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._flatList`, `this._rows`, `this._rows[aRow].containerOpen`

## PTV_isContainerEmpty()
- 位置: L1371-1378
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._flatList`, `this._rows`, `this._rows[aRow].hasChildren`

## PTV_isSeparator()
- 位置: L1380-1384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsSeparator()`
- 参照: `this._rows`

## PTV_isSorted()
- 位置: L1386-1390
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `this._result.sortingMode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV_canDrop()
- 位置: L1392-1408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `this._getInsertionPoint()`, `this.isSorted()`
- 条件付き依存: `if (!this._result)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `this._controller.disableUserActions`, `this._result`

## PTV__getInsertionPoint()
- 位置: L1410-1498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsTagQuery()`, `this._controller.disallowInsertion()`
- 条件付き依存: `if (index != -1)` → `this.nodeForTreeIndex()`
- 条件付き依存: `if (index != -1)` → `this.isContainer()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `this._element.view.selection.isSelected()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `this._controller.disallowInsertion()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (!(queryOptions.excludeItems || queryOptions.excludeQueries))` → `container.getChildIndex()`
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUtils.asQuery(container).query.tags`, `PlacesUtils.asQuery(this._result.root).queryOptions`, `container.containerOpen`, `lastSelected.containerOpen`, `lastSelected.hasChildren`, `lastSelected.parent`, `queryOptions.excludeItems`, `queryOptions.excludeQueries`, `queryOptions.sortingMode`, `this._element.isDragSource`, `this._result.root`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## drop()
- 位置: async L1500-1520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getInsertionPoint()`
- 条件付き依存: `if (ip)` → `PlacesControllerDragHelper.onDrop()`
- 条件付き依存: `if (ip)` → `console.error()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._controller.disableUserActions`, `this._tree`

## PTV_getParentIndex()
- 位置: L1522-1525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getParentByChildRow()`

## PTV_hasNextSibling()
- 位置: L1527-1555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getNodeForRow()`, `this._isPlainContainer()`
- 参照: `nextNode.parent`, `node.indentLevel`, `node.parent`, `rowNode.indentLevel`, `this._rows`, `this._rows.length`

## getLevel()
- 位置: L1557-1559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getNodeForRow()`
- 参照: `this._getNodeForRow(aRow).indentLevel`

## PTV_getImageSrc()
- 位置: L1561-1569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getColumnType()`, `this._getNodeForRow()`
- 参照: `node.icon`, `this.COLUMN_TYPE_TITLE`

## getCellValue()
- 位置: L1571-1571
- 役割: (未記入)
- 触るとき: (未記入)

## PTV_getCellText()
- 位置: L1573-1619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getBestTitle()`, `PlacesUtils.nodeIsSeparator()`, `PlacesUtils.nodeIsURI()`, `node.tags?.replaceAll()`, `this._convertPRTimeToString()`, `this._getColumnType()`, `this._getNodeForRow()`
- 条件付き依存: `if (node.dateAdded)` → `this._convertPRTimeToString()`
- 条件付き依存: `if (node.lastModified)` → `this._convertPRTimeToString()`
- 参照: `node.accessCount`, `node.dateAdded`, `node.lastModified`, `node.time`, `node.uri`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`

## PTV_setTree()
- 位置: L1621-1643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.batching()`
- 条件付き依存: `if (aTree)` → `this._finishInit()`
- 参照: `this._result`, `this._rootNode.containerOpen`, `this._tree`

## PTV_toggleOpenState()
- 位置: L1645-1679
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._result)` → `Components.Exception()`
- 条件付き依存: `if (this._flatList && this._element)` → `this._element.dispatchEvent()`
- 条件付き依存: `if (node.containerOpen)` → `Services.xulStore.removeValue()`
- 条件付き依存: `if (node.containerOpen)` → `PlacesUIUtils.obfuscateUrlForXulStore()`
- 条件付き依存: `if (!(node.containerOpen))` → `Services.xulStore.setValue()`
- 条件付き依存: `if (!(node.containerOpen))` → `PlacesUIUtils.obfuscateUrlForXulStore()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `document.documentURI`, `node.containerOpen`, `node.uri`, `this._element`, `this._flatList`, `this._result`, `this._rows`
- XPCOM: `Services.xulStore`

## PTV_cycleHeader()
- 位置: L1681-1789
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `this._getColumnType()`
- 条件付き依存: `if (!this._result)` → `Components.Exception()`
- 参照: `Ci.nsINavHistoryQueryOptions`, `Cr.NS_ERROR_INVALID_ARG`, `Cr.NS_ERROR_UNEXPECTED`, `NHQO.SORT_BY_DATEADDED_ASCENDING`, `NHQO.SORT_BY_DATEADDED_DESCENDING`, `NHQO.SORT_BY_DATE_ASCENDING`, `NHQO.SORT_BY_DATE_DESCENDING`, `NHQO.SORT_BY_LASTMODIFIED_ASCENDING`, `NHQO.SORT_BY_LASTMODIFIED_DESCENDING`, `NHQO.SORT_BY_NONE`, `NHQO.SORT_BY_TAGS_ASCENDING`, `NHQO.SORT_BY_TAGS_DESCENDING`, `NHQO.SORT_BY_TITLE_ASCENDING`, `NHQO.SORT_BY_TITLE_DESCENDING`, `NHQO.SORT_BY_URI_ASCENDING`, `NHQO.SORT_BY_URI_DESCENDING`, `NHQO.SORT_BY_VISITCOUNT_ASCENDING`, `NHQO.SORT_BY_VISITCOUNT_DESCENDING`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`, `this._result`, `this._result.root`, `this._result.sortingMode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV_isEditable()
- 位置: L1791-1828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.isRootItem()`, `PlacesUtils.nodeIsQueryGeneratedFolder()`, `PlacesUtils.nodeIsSeparator()`
- 条件付き依存: `if (!node)` → `console.error()`
- 参照: `aColumn.index`, `node.bookmarkGuid`, `this._rows`

## PTV_setCellText()
- 位置: L1830-1838
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node.title != aText)` → `PlacesTransactions.EditTitle({ guid: node.bookmarkGuid, title: aText }) .transact() .catch()`
- 条件付き依存: `if (node.title != aText)` → `PlacesTransactions.EditTitle({ guid: node.bookmarkGuid, title: aText }) .transact()`
- 条件付き依存: `if (node.title != aText)` → `PlacesTransactions.EditTitle()`
- 参照: `console.error`, `node.bookmarkGuid`, `node.title`, `this._rows`

## PTV_toggleCutNode()
- 位置: L1840-1851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cuttingNodes.has()`
- 条件付き依存: `if (aValue)` → `this._cuttingNodes.add()`
- 条件付き依存: `if (!(aValue))` → `this._cuttingNodes.delete()`
- 条件付き依存: `if (currentVal != aValue)` → `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TITLE`

## selectionChanged()
- 位置: L1853-1853
- 役割: (未記入)
- 触るとき: (未記入)

## cycleCell()
- 位置: L1854-1854
- 役割: (未記入)
- 触るとき: (未記入)
