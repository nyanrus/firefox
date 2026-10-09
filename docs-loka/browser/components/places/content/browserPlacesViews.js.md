# browser/components/places/content/browserPlacesViews.js

source: browser/components/places/content/browserPlacesViews.js
source-hash: 968c6ed81b97d7f4f34005bfd85bdf3e2496f641
lines: 2502

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## PlacesViewBase.constructor()
- 位置: L18-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._init()`, `this._viewElt.controllers.appendController()`
- 参照: `this._controller`, `this._rootElt`, `this._viewElt`, `this.place`

## PlacesViewBase.associatedElement()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._viewElt`

## PlacesViewBase.controllers()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._viewElt.controllers`

## PlacesViewBase.rootElement()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._rootElt`

## PlacesViewBase.place()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._place`

## PlacesViewBase.place()
- 位置: L61-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `history.executeQuery()`, `history.queryStringToQuery()`, `result.addObserver()`
- 参照: `PlacesUtils.history`, `options.value`, `query.value`, `this._place`

## PlacesViewBase.result()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._result`

## PlacesViewBase.result()
- 位置: L76-103
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 条件付き依存: `if (val)` → `this._domNodes.set()`
- 参照: `this._domNodes`, `this._result`, `this._resultNode`, `this._resultNode.containerOpen`, `this._rootElt`, `this._rootElt._built`, `this._rootElt._placesNode`, `this._rootElt.localName`, `val.root`

## PlacesViewBase._getDOMNodeForPlacesNode()
- 位置: L115-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._domNodes.get()`
- 参照: `aPlacesNode.type`

## PlacesViewBase.controller()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._controller`

## PlacesViewBase.selType()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.selectItems()
- 位置: L135-135
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.selectAll()
- 位置: L136-136
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.selectedNode()
- 位置: L138-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `anchor._placesNode`, `anchor.parentNode`, `this._contextMenuShown`, `this._contextMenuShown.triggerNode`, `this._rootElt`

## PlacesViewBase.hasSelection()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectedNode`

## PlacesViewBase.selectedNodes()
- 位置: L159-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectedNode`

## PlacesViewBase.singleClickOpens()
- 位置: L164-166
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.removableSelectionRanges()
- 位置: L168-181
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`, `popupNode._placesNode`, `popupNode.localName`, `this.selectedNodes`

## PlacesViewBase.draggableSelection()
- 位置: L183-185
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._draggedElt`

## PlacesViewBase.insertionPoint()
- 位置: L187-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsQuery()`, `this.controller.disallowInsertion()`
- 条件付き依存: `if (!( !popupNode._placesNode || popupNode._placesNode == this._resultNode || popupNode._placesNode.itemId == -1 || !selectedNode.parent ))` → `container.getChildIndex()`
- 条件付き依存: `if (!( !popupNode._placesNode || popupNode._placesNode == this._resultNode || popupNode._placesNode.itemId == -1 || !selectedNode.parent ))` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(container))` → `PlacesUtils.asQuery()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUIUtils.lastContextMenuTriggerNode`, `PlacesUtils.asQuery(container).query.tags`, `PlacesUtils.asQuery(resultNode).queryOptions.queryType`, `PlacesUtils.bookmarks.DEFAULT_INDEX`, `popupNode._placesNode`, `popupNode._placesNode.itemId`, `selectedNode.parent`, `this._resultNode`, `this.selectedNode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## PlacesViewBase.buildContextMenu()
- 位置: L240-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPopup.querySelector()`, `bookmarksToolbar?.contains()`, `document.getElementById()`, `existingOtherBookmarksItem?.remove()`, `existingSubmenu?.remove()`, `this.controller.buildContextMenu()`, `window.updateCommands()`
- 条件付き依存: `if (bookmarksToolbar?.contains(aPopup.triggerNode))` → `manageBookmarksMenu.removeAttribute()`
- 条件付き依存: `if (bookmarksToolbar?.contains(aPopup.triggerNode))` → `BookmarkingUI.buildBookmarksToolbarSubmenu()`
- 条件付き依存: `if (bookmarksToolbar?.contains(aPopup.triggerNode))` → `aPopup.insertBefore()`
- 条件付き依存: `if ( aPopup.triggerNode.id === "OtherBookmarks" || aPopup.triggerNode.id === "PlacesChevron" || aPopup.triggerNode.id === "PlacesToolbarItems" || aPopup.triggerN...)` → `BookmarkingUI.buildShowOtherBookmarksMenuItem()`
- 条件付き依存: `if (otherBookmarksMenuItem)` → `aPopup.insertBefore()`
- 条件付き依存: `if (!(bookmarksToolbar?.contains(aPopup.triggerNode)))` → `manageBookmarksMenu.setAttribute()`
- 参照: `aPopup.triggerNode`, `aPopup.triggerNode.id`, `aPopup.triggerNode.parentNode.id`, `menu.nextElementSibling`, `this._contextMenuShown`, `triggerNode._placesNode?.childCount`, `triggerNode?.localName`

## PlacesViewBase.destroyContextMenu()
- 位置: L297-299
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._contextMenuShown`

## PlacesViewBase.clearAllContents()
- 位置: L301-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `kid.classList.contains()`
- 条件付き依存: `if (!kid.classList.contains("panel-header"))` → `kid.remove()`
- 参照: `aPopup._emptyMenuitem`, `aPopup._endMarker`, `aPopup._startMarker`, `aPopup.firstElementChild`, `kid.nextElementSibling`

## PlacesViewBase._cleanPopup()
- 位置: L313-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureMarkers()`
- 条件付き依存: `if (sibling._placesNode && !aDelay)` → `aPopup.removeChild()`
- 条件付き依存: `if (sibling._placesNode && aDelay)` → `aPopup._delayedRemovals.push()`
- 参照: `aPopup._delayedRemovals`, `aPopup._endMarker`, `aPopup._startMarker`, `child.nextElementSibling`, `sibling._placesNode`

## PlacesViewBase._rebuildPopup()
- 位置: L338-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanPopup()`
- 条件付き依存: `if (cc > 0)` → `this._setEmptyPopupStatus()`
- 条件付き依存: `if (cc > 0)` → `document.createDocumentFragment()`
- 条件付き依存: `if (cc > 0)` → `resultNode.getChild()`
- 条件付き依存: `if (cc > 0)` → `this._insertNewItemToPopup()`
- 条件付き依存: `if (cc > 0)` → `aPopup.insertBefore()`
- 条件付き依存: `if (!(cc > 0))` → `this._setEmptyPopupStatus()`
- 参照: `aPopup._built`, `aPopup._endMarker`, `aPopup._placesNode`, `resultNode.childCount`, `resultNode.containerOpen`

## PlacesViewBase._removeChild()
- 位置: L361-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aChild.remove()`

## PlacesViewBase._setEmptyPopupStatus()
- 位置: L365-391
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!aPopup._emptyMenuitem)` → `document.createXULElement()`
- 条件付き依存: `if (!aPopup._emptyMenuitem)` → `aPopup._emptyMenuitem.setAttribute()`
- 条件付き依存: `if (!aPopup._emptyMenuitem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (aEmpty)` → `aPopup.setAttribute()`
- 条件付き依存: `if ( !aPopup._startMarker.previousElementSibling && !aPopup._endMarker.nextElementSibling )` → `aPopup.insertBefore()`
- 条件付き依存: `if (!(aEmpty))` → `aPopup.removeAttribute()`
- 条件付き依存: `if (!(aEmpty))` → `aPopup.removeChild()`
- 参照: `aPopup._emptyMenuitem`, `aPopup._emptyMenuitem.className`, `aPopup._endMarker`, `aPopup._endMarker.nextElementSibling`, `aPopup._startMarker.previousElementSibling`

## PlacesViewBase._createDOMNodeForPlacesNode()
- 位置: L393-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._domNodes.delete()`, `this._domNodes.has()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR)` → `document.createXULElement()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI)` → `document.createXULElement()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI)` → `element.setAttribute()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI)` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI))` → `PlacesUtils.containerTypes.includes()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `document.createXULElement()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `element.setAttribute()`
- 条件付き依存: `if (aPlacesNode.type == Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY)` → `element.setAttribute()`
- 条件付き依存: `if (aPlacesNode.type == Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY)` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(aPlacesNode))` → `element.setAttribute()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(aPlacesNode)))` → `PlacesUtils.nodeIsDay()`
- 条件付き依存: `if (PlacesUtils.nodeIsDay(aPlacesNode))` → `element.setAttribute()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsDay(aPlacesNode)))` → `PlacesUtils.nodeIsHost()`
- 条件付き依存: `if (PlacesUtils.nodeIsHost(aPlacesNode))` → `element.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `PlacesUtils.asContainer()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.setAttribute()`
- 条件付き依存: `if (!this._nativeView)` → `popup.setAttribute()`
- 条件付き依存: `if (!this._nativeView)` → `popup.toggleAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `element.appendChild()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `this._domNodes.set()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `element.setAttribute()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUIUtils.getBestTitle()`
- 条件付き依存: `if (icon)` → `element.setAttribute()`
- 条件付き依存: `if (icon)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (!this._domNodes.has(aPlacesNode))` → `this._domNodes.set()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `aPlacesNode.icon`, `aPlacesNode.type`, `aPlacesNode.uri`, `element._placesNode`, `element.className`, `popup._placesNode`, `this._nativeView`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesViewBase._insertNewItemToPopup()
- 位置: L459-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aInsertionNode.insertBefore()`, `this._createDOMNodeForPlacesNode()`

## PlacesViewBase.toggleCutNode()
- 位置: L466-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (aValue)` → `elt.setAttribute()`
- 条件付き依存: `if (!(aValue))` → `elt.removeAttribute()`
- 参照: `elt.localName`, `elt.parentNode`

## PlacesViewBase.nodeURIChanged()
- 位置: L480-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.guessUrlSchemeForUI()`, `elt.setAttribute()`, `this._getDOMNodeForPlacesNode()`
- 参照: `aPlacesNode.uri`, `elt.localName`, `elt.parentNode`

## PlacesViewBase.nodeIconChanged()
- 位置: L499-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.encodeURIForSrcset()`, `elt.removeAttribute()`, `elt.setAttribute()`, `this._getDOMNodeForPlacesNode()`
- 参照: `aPlacesNode.icon`, `elt.localName`, `elt.parentNode`, `this._rootElt`

## PlacesViewBase.nodeTitleChanged()
- 位置: L517-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (!aNewTitle && elt.localName != "toolbarbutton")` → `elt.setAttribute()`
- 条件付き依存: `if (!aNewTitle && elt.localName != "toolbarbutton")` → `PlacesUIUtils.getBestTitle()`
- 条件付き依存: `if (!(!aNewTitle && elt.localName != "toolbarbutton"))` → `elt.setAttribute()`
- 参照: `elt.localName`, `elt.parentNode`, `this._rootElt`

## PlacesViewBase.nodeRemoved()
- 位置: L541-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt._built)` → `parentElt.removeChild()`
- 条件付き依存: `if (parentElt._startMarker.nextElementSibling == parentElt._endMarker)` → `this._mayAddCommandsItems()`
- 条件付き依存: `if (parentElt._startMarker.nextElementSibling == parentElt._endMarker)` → `this._setEmptyPopupStatus()`
- 参照: `elt.localName`, `elt.parentNode`, `parentElt._built`, `parentElt._endMarker`, `parentElt._startMarker.nextElementSibling`

## PlacesViewBase.nodeHistoryDetailsChanged()
- 位置: L566-566
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.nodeTagsChanged()
- 位置: L567-567
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.nodeDateAddedChanged()
- 位置: L568-568
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.nodeLastModifiedChanged()
- 位置: L569-569
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.nodeKeywordChanged()
- 位置: L570-570
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.sortingChanged()
- 位置: L571-571
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.batching()
- 位置: L572-572
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase.nodeInserted()
- 位置: L574-591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.indexOf.call()`, `this._getDOMNodeForPlacesNode()`, `this._insertNewItemToPopup()`, `this._mayAddCommandsItems()`, `this._setEmptyPopupStatus()`
- 参照: `parentElt._built`, `parentElt._endMarker`, `parentElt._startMarker`, `parentElt.children`

## PlacesViewBase.nodeMoved()
- 位置: L593-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt._built)` → `parentElt.removeChild()`
- 条件付き依存: `if (parentElt._built)` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if (parentElt._built)` → `parentElt.insertBefore()`
- 参照: `elt.localName`, `elt.parentNode`, `parentElt._built`, `parentElt._startMarker`, `parentElt.children`, `this._rootElt`

## PlacesViewBase.containerStateChanged()
- 位置: L632-639
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aNewState == Ci.nsINavHistoryContainerResultNode.STATE_OPENED || aNewState == Ci.nsINavHistoryContainerResultNode.STATE_CLOSED )` → `this.invalidateContainer()`
- 参照: `Ci.nsINavHistoryContainerResultNode.STATE_CLOSED`, `Ci.nsINavHistoryContainerResultNode.STATE_OPENED`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesViewBase._isPopupOpen()
- 位置: L649-651
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `elt.parentNode.open`

## PlacesViewBase.invalidateContainer()
- 位置: L653-661
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getDOMNodeForPlacesNode()`, `this._isPopupOpen()`
- 条件付き依存: `if (this._isPopupOpen(elt))` → `this._rebuildPopup()`
- 参照: `elt._built`

## PlacesViewBase.uninit()
- 位置: L663-686
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 条件付き依存: `if (this._controller)` → `this._controller.terminate()`
- 条件付き依存: `if (this._controller)` → `this._viewElt.controllers.removeController()`
- 参照: `this._controller`, `this._result`, `this._resultNode`, `this._resultNode.containerOpen`, `this._viewElt._placesView`

## PlacesViewBase.isRTL()
- 位置: L688-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.defaultView.getComputedStyle()`
- 参照: `document.defaultView.getComputedStyle(this._viewElt).direction`, `this._isRTL`, `this._viewElt`

## PlacesViewBase.ownerWindow()
- 位置: L697-699
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesViewBase._mayAddCommandsItems()
- 位置: L707-794
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aPopup._endOptOpenAllInTabs)` → `aPopup.removeChild()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `document.createXULElement()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `aPopup.appendChild()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `aPopup._endOptOpenAllInTabs.setAttribute()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `aPopup._endOptOpenAllInTabs.addEventListener()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `PlacesUIUtils.getViewForNode()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `document.createXULElement()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `aPopup._endOptShareFolder.setAttribute()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `aPopup._endOptShareFolder.addEventListener()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `ContentSharingUtils.createShareableLinkFromBookmarkFolders()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `aPopup.appendChild()`
- 条件付き依存: `if ( aPopup._endOptShareFolder && (!ContentSharingUtils.isEnabled || !numURINodes) )` → `aPopup.removeChild()`
- 参照: `ContentSharingUtils.isEnabled`, `aPopup._endOptOpenAllInTabs`, `aPopup._endOptOpenAllInTabs.className`, `aPopup._endOptSeparator`, `aPopup._endOptSeparator.className`, `aPopup._endOptShareFolder`, `aPopup._endOptShareFolder.className`, `aPopup._placesNode.childCount`, `aPopup.firstElementChild`, `currentChild._placesNode`, `currentChild.localName`, `currentChild.nextElementSibling`, `event.currentTarget`, `event.currentTarget.parentNode._placesNode`, `this._rootElt`

## PlacesViewBase._ensureMarkers()
- 位置: L796-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPopup.appendChild()`, `aPopup.insertBefore()`, `child.hasAttribute()`, `document.createXULElement()`
- 条件付き依存: `if (child.hasAttribute("afterplacescontent"))` → `aPopup.insertBefore()`
- 条件付き依存: `if (child._placesNode && !child._placesView && !firstNonStaticNodeFound)` → `aPopup.insertBefore()`
- 条件付き依存: `if (!firstNonStaticNodeFound)` → `aPopup.insertBefore()`
- 参照: `aPopup._endMarker`, `aPopup._endMarker.hidden`, `aPopup._startMarker`, `aPopup._startMarker.hidden`, `aPopup.children`, `aPopup.firstElementChild`, `child._placesNode`, `child._placesView`

## PlacesViewBase._onPopupShowing()
- 位置: L834-866
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `this._ensureMarkers()`
- 条件付き依存: `if ("_delayedRemovals" in popup)` → `popup.removeChild()`
- 条件付き依存: `if ("_delayedRemovals" in popup)` → `popup._delayedRemovals.shift()`
- 条件付き依存: `if (popup._placesNode && PlacesUIUtils.getViewForNode(popup) == this)` → `this.#isPopupForRecursiveFolderShortcut()`
- 条件付き依存: `if (this.#isPopupForRecursiveFolderShortcut(popup))` → `this._setEmptyPopupStatus()`
- 条件付き依存: `if (!popup._built)` → `this._rebuildPopup()`
- 条件付き依存: `if (popup._placesNode && PlacesUIUtils.getViewForNode(popup) == this)` → `this._mayAddCommandsItems()`
- 参照: `aEvent.originalTarget`, `popup._built`, `popup._delayedRemovals.length`, `popup._placesNode`, `popup._placesNode.containerOpen`

## PlacesViewBase._addEventListeners()
- 位置: L868-872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aObject.addEventListener()`
- 参照: `aEventNames.length`

## PlacesViewBase._removeEventListeners()
- 位置: L874-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aObject.removeEventListener()`
- 参照: `aEventNames.length`

## PlacesViewBase.#isPopupForRecursiveFolderShortcut()
- 位置: L887-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `parentView._placesNode`, `parentView.parentNode?.parentNode`, `parentView?._placesNode`, `popup._placesNode`, `popup.parentNode?.parentNode`

## PlacesToolbar.constructor()
- 位置: L917-950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.bookmarksToolbar.init.start()`, `Glean.bookmarksToolbar.init.stopAndAccumulate()`, `document.getElementById()`, `super()`, `this._addEventListeners()`, `this._resizeObserver.observe()`, `this.updateNodesVisibility()`
- 条件付き依存: `if ( this._viewElt.parentNode.parentNode == document.getElementById("TabsToolbar") )` → `this._addEventListeners()`
- 参照: `gBrowser.tabContainer`, `this._cbEvents`, `this._dragRoot`, `this._resizeObserver`, `this._rootElt`, `this._viewElt.parentNode.parentNode`

## PlacesToolbar._init()
- 位置: L958-990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkingUI.toolbar.contains()`, `document.getElementById()`, `thisView.__defineGetter__()`
- 参照: `BookmarkingUI.toolbar`, `this._dragRoot`, `this._overFolder`, `this._viewElt`, `this._viewElt._placesView`

## PlacesToolbar.uninit()
- 位置: L1010-1043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.uninit()`, `this._chevronPopup.uninit()`, `this._removeEventListeners()`
- 条件付き依存: `if (this._dragRoot)` → `this._removeEventListeners()`
- 条件付き依存: `if (this._resizeObserver)` → `this._resizeObserver.disconnect()`
- 条件付き依存: `if (this._chevron._placesView)` → `this._chevron._placesView.uninit()`
- 条件付き依存: `if (this._otherBookmarks?._placesView)` → `this._otherBookmarks._placesView.uninit()`
- 参照: `gBrowser.tabContainer`, `this._cbEvents`, `this._chevron._placesView`, `this._dragRoot`, `this._otherBookmarks?._placesView`, `this._resizeObserver`, `this._rootElt`

## PlacesToolbar.promiseRebuilt()
- 位置: L1048-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._rebuilding?.promise`

## PlacesToolbar._isAlive()
- 位置: L1052-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._resultNode`, `this._rootElt`

## PlacesToolbar._runBeforeFrameRender()
- 位置: L1056-1066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `reject()`, `resolve()`, `window.requestAnimationFrame()`

## PlacesToolbar._rebuild()
- 位置: async L1068-1146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkingUI.maybeShowOtherBookmarksFolder()`, `BookmarkingUI.maybeShowOtherBookmarksFolder().catch()`, `document.getElementById()`, `otherBookmarks?.remove()`, `this._chevronPopup.hasAttribute()`, `this._rootElt.firstChild.remove()`, `this._rootElt.hasChildNodes()`
- 条件付き依存: `if (this._overFolder.elt)` → `this._clearOverFolder()`
- 条件付き依存: `if (cc > 0)` → `this._runBeforeFrameRender()`
- 条件付き依存: `if (cc > 0)` → `this._insertNewItem()`
- 条件付き依存: `if (cc > 0)` → `this._resultNode.getChild()`
- 条件付き依存: `if (cc > 0)` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (cc > 0)` → `Math.min()`
- 条件付き依存: `if (cc > 0)` → `parseInt()`
- 条件付き依存: `if (cc > 0)` → `document.createDocumentFragment()`
- 条件付き依存: `if (cc > 0)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (cc > 0)` → `this._rootElt.appendChild()`
- 条件付き依存: `if (cc > 0)` → `this.updateNodesVisibility()`
- 参照: `console.error`, `elt.clientHeight`, `elt.localName`, `this._chevronPopup.place`, `this._isAlive`, `this._openedMenuButton`, `this._overFolder.elt`, `this._resultNode.childCount`, `this._rootElt`, `this.place`, `window.screen.width`

## PlacesToolbar._insertNewItem()
- 位置: L1148-1206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._domNodes.delete()`, `this._domNodes.has()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR)` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `button.setAttribute()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUtils.containerTypes.includes()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(aChild))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(aChild))` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(aChild))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `document.createXULElement()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.toggleAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.classList.add()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `button.appendChild()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `PlacesUtils.asContainer()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `this._domNodes.set()`
- 条件付き依存: `if (!(PlacesUtils.containerTypes.includes(type)))` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(aChild))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(aChild))` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (icon)` → `button.setAttribute()`
- 条件付き依存: `if (!this._domNodes.has(aChild))` → `this._domNodes.set()`
- 条件付き依存: `if (aBefore)` → `aInsertionNode.insertBefore()`
- 条件付き依存: `if (!(aBefore))` → `aInsertionNode.appendChild()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `aChild.title`, `aChild.type`, `aChild.uri`, `button._placesNode`, `button.className`, `popup._placesNode`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesToolbar._updateChevronPopupNodesVisibility()
- 位置: L1208-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `node.hidden`, `node.nextElementSibling`, `this._chevronPopup._startMarker.nextElementSibling`, `this._rootElt.firstElementChild`, `toolbarNode.nextElementSibling`, `toolbarNode.style.visibility`

## PlacesToolbar._onChevronPopupShowing()
- 位置: L1221-1232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateChevronPopupNodesVisibility()`
- 参照: `aEvent.target`, `this._chevron._placesView`, `this._chevronPopup`, `this.place`

## PlacesToolbar._onOtherBookmarksPopupShowing()
- 位置: L1234-1245
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PlacesUtils.bookmarks.unfiledGuid`, `aEvent.target`, `this._otherBookmarks._placesView`, `this._otherBookmarksPopup`

## PlacesToolbar.handleEvent()
- 位置: L1247-1308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.stopPropagation()`, `this._isOverflowStateEventRelevant()`, `this._onDragEnd()`, `this._onDragLeave()`, `this._onDragOver()`, `this._onDragStart()`, `this._onDrop()`, `this._onMouseDown()`, `this._onMouseMove()`, `this._onMouseOut()`, `this._onMouseOver()`, `this._onOverflow()`, `this._onPopupHidden()`, `this._onPopupShowing()`, `this._onUnderflow()`, `this.uninit()`, `this.updateNodesVisibility()`
- 参照: `aEvent.type`

## PlacesToolbar._isOverflowStateEventRelevant()
- 位置: L1310-1313
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aEvent.currentTarget`, `aEvent.detail`, `aEvent.target`

## PlacesToolbar._onOverflow()
- 位置: L1315-1324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._chevronPopup.hasAttribute()`, `this.updateNodesVisibility()`
- 条件付き依存: `if (!this._chevronPopup.hasAttribute("type"))` → `this._chevronPopup.setAttribute()`
- 参照: `this._chevron.collapsed`, `this.place`

## PlacesToolbar._onUnderflow()
- 位置: L1326-1329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateNodesVisibility()`
- 参照: `this._chevron.collapsed`

## PlacesToolbar.updateNodesVisibility()
- 位置: L1331-1339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setTimer()`
- 条件付き依存: `if (this._updateNodesVisibilityTimer)` → `this._updateNodesVisibilityTimer.cancel()`
- 参照: `this._updateNodesVisibilityTimer`

## PlacesToolbar._updateNodesVisibilityTimerCallback()
- 位置: async L1341-1404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dwu.getBoundsWithoutFlushing()`, `this._applyChildVisibility()`, `window.promiseDocumentFlushed()`, `window.requestAnimationFrame()`
- 条件付き依存: `if (!this.#pendingVisibilityRetry)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (this._isAlive)` → `this.updateNodesVisibility()`
- 条件付き依存: `if (this._rootElt.children.length != measuredCount)` → `this.updateNodesVisibility()`
- 参照: `childRect.left`, `childRect.right`, `scrollRect.left`, `scrollRect.right`, `scrollRect.width`, `this.#pendingVisibilityRetry`, `this.#updatingNodesVisibility`, `this._isAlive`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.children.length`, `this.isRTL`, `window.closed`, `window.windowUtils`

## PlacesToolbar._applyChildVisibility()
- 位置: L1406-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._viewElt.dispatchEvent()`
- 条件付き依存: `if (icon)` → `child.setAttribute()`
- 条件付き依存: `if (i < visibleCount)` → `child.style.removeProperty()`
- 条件付き依存: `if (!(i < visibleCount))` → `child.removeAttribute()`
- 条件付き依存: `if (!this._chevron.collapsed && this._chevron.open)` → `this._updateChevronPopupNodesVisibility()`
- 参照: `child._placesNode.icon`, `child.style.visibility`, `children.length`, `this._chevron.collapsed`, `this._chevron.open`, `this._rootElt.children`

## PlacesToolbar.nodeInserted()
- 位置: L1432-1477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.nodeInserted()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (this._resultNode.childCount - 1 > children.length)` → `this._rootElt.removeChild()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._insertNewItem()`
- 条件付き依存: `if (icon)` → `button.setAttribute()`
- 条件付き依存: `if (icon)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (!(prevSiblingOverflowed))` → `this.updateNodesVisibility()`
- 参照: `aPlacesNode.icon`, `button.style.visibility`, `children.length`, `children[aIndex - 1].style.visibility`, `this._resultNode.childCount`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.lastElementChild`

## PlacesToolbar.nodeRemoved()
- 位置: L1479-1510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.nodeRemoved()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._removeChild()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._insertNewItem()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._resultNode.getChild()`
- 条件付き依存: `if (!overflowed)` → `this.updateNodesVisibility()`
- 参照: `elt.localName`, `elt.parentNode`, `elt.style.visibility`, `this._resultNode.childCount`, `this._rootElt`, `this._rootElt.children.length`

## PlacesToolbar.nodeMoved()
- 位置: L1512-1582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.nodeMoved()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (elt)` → `this._removeChild()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._insertNewItem()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._resultNode.getChild()`
- 条件付き依存: `if (!elt)` → `this._insertNewItem()`
- 条件付き依存: `if (icon)` → `elt.setAttribute()`
- 条件付き依存: `if (icon)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (!(!elt))` → `this._rootElt.insertBefore()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this.updateNodesVisibility()`
- 参照: `aPlacesNode.icon`, `elt.localName`, `elt.parentNode`, `this._resultNode.childCount`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.children.length`

## PlacesToolbar.nodeTitleChanged()
- 位置: L1584-1605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.nodeTitleChanged()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (elt.style.visibility != "hidden")` → `this.updateNodesVisibility()`
- 参照: `elt.localName`, `elt.parentNode`, `elt.style.visibility`, `this._rootElt`

## PlacesToolbar.invalidateContainer()
- 位置: L1607-1632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.invalidateContainer()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (!this._rebuilding)` → `Promise.withResolvers()`
- 条件付き依存: `if (elt == this._rootElt)` → `this._rebuild() .catch(console.error) .finally()`
- 条件付き依存: `if (elt == this._rootElt)` → `this._rebuild() .catch()`
- 条件付き依存: `if (elt == this._rootElt)` → `this._rebuild()`
- 条件付き依存: `if (instance == this._rebuildingInstance)` → `this._rebuilding.resolve()`
- 参照: `console.error`, `this._rebuilding`, `this._rebuildingInstance`, `this._rootElt`

## PlacesToolbar._clearOverFolder()
- 位置: L1634-1653
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._overFolder.elt && this._overFolder.elt.menupopup)` → `this._overFolder.elt.menupopup.hasAttribute()`
- 条件付き依存: `if (!this._overFolder.elt.menupopup.hasAttribute("dragover"))` → `this._overFolder.elt.menupopup.hidePopup()`
- 条件付き依存: `if (this._overFolder.elt && this._overFolder.elt.menupopup)` → `this._overFolder.elt.removeAttribute()`
- 条件付き依存: `if (this._overFolder.openTimer)` → `this._overFolder.openTimer.cancel()`
- 条件付き依存: `if (this._overFolder.closeTimer)` → `this._overFolder.closeTimer.cancel()`
- 参照: `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.elt.menupopup`, `this._overFolder.openTimer`

## PlacesToolbar._getDropPoint()
- 位置: L1666-1791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `elt.getBoundingClientRect()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `PlacesUIUtils.isFolderReadOnly()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.right - threshold : aEvent.clientX < eltRect.left + threshold )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.right - threshold )` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.right - threshold )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.right - threshold ))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.left + threshold )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.left + threshold ))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (elt == this._chevron)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!(elt == this._chevron))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!(elt == this._chevron))` → `Math.round()`
- 条件付き依存: `if (!(elt == this._chevron))` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!(elt == this._chevron))` → `canInsertHere()`
- 参照: `Ci.nsITreeView.DROP_BEFORE`, `aEvent.clientX`, `aEvent.target`, `dropPoint.beforeIndex`, `dropPoint.folderElt`, `dropPoint.ip`, `dropPoint.ip.index`, `elt._placesNode`, `elt._placesNode.title`, `elt.localName`, `eltRect.left`, `eltRect.right`, `eltRect.width`, `rect.left`, `rect.right`, `this._chevron`, `this._resultNode`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.children.length`, `this.isRTL`
- XPCOM: `nsITreeView`

## PlacesToolbar._setTimer()
- 位置: L1793-1797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `timer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PlacesToolbar.name()
- 位置: L1799-1801
- 役割: (未記入)
- 触るとき: (未記入)

## PlacesToolbar.notify()
- 位置: L1803-1837
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTimer == this._updateNodesVisibilityTimer)` → `this._updateNodesVisibilityTimerCallback()`
- 条件付き依存: `if (aTimer == this._overFolder.openTimer)` → `this._overFolder.elt.menupopup.setAttribute()`
- 条件付き依存: `if (aTimer == this._overFolder.closeTimer)` → `this._clearOverFolder()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `currentPlacesNode.parentNode`, `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.elt.open`, `this._overFolder.openTimer`, `this._rootElt`, `this._updateNodesVisibilityTimer`

## PlacesToolbar._onMouseOver()
- 位置: L1839-1848
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if ( button.parentNode == this._rootElt && button._placesNode && PlacesUtils.nodeIsURI(button._placesNode) )` → `window.XULBrowserWindow.setOverLink()`
- 参照: `aEvent.target`, `aEvent.target._placesNode.uri`, `button._placesNode`, `button.parentNode`, `this._rootElt`

## PlacesToolbar._onMouseOut()
- 位置: L1850-1852
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.XULBrowserWindow.setOverLink()`

## PlacesToolbar._onMouseDown()
- 位置: L1854-1869
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.maybeSpeculativeConnectOnMouseDown()`, `target.getAttribute()`
- 条件付き依存: `if ( aEvent.button == 0 && target.localName == "toolbarbutton" && target.getAttribute("type") == "menu" )` → `aEvent.getModifierState()`
- 参照: `aEvent.button`, `aEvent.shiftKey`, `aEvent.target`, `target.localName`, `this._allowPopupShowing`

## PlacesToolbar._cleanupDragDetails()
- 位置: L1871-1876
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._draggedElt`, `this._dropIndicator.collapsed`

## PlacesToolbar._onDragStart()
- 位置: L1878-1914
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.stopPropagation()`, `draggedElt.getAttribute()`, `this._controller.setDataTransfer()`, `this._rootElt.focus()`
- 条件付き依存: `if ( draggedElt.localName == "toolbarbutton" && draggedElt.getAttribute("type") == "menu" )` → `Math.abs()`
- 条件付き依存: `if (translateY >= Math.abs(translateX / 2))` → `aEvent.preventDefault()`
- 条件付き依存: `if (draggedElt.open)` → `draggedElt.menupopup.hidePopup()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.target`, `draggedElt._placesNode`, `draggedElt.localName`, `draggedElt.open`, `draggedElt.parentNode`, `this._cachedMouseMoveEvent.clientX`, `this._cachedMouseMoveEvent.clientY`, `this._draggedElt`, `this._rootElt`

## PlacesToolbar.#findPrecedingToolbarWidget()
- 位置: L1922-1942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.getBoundingClientRect()`, `this._rootElt.closest()`
- 参照: `child.collapsed`, `child.getBoundingClientRect().width`, `child.hidden`, `toolbar.children`

## PlacesToolbar._onDragOver()
- 位置: L1944-2037
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `aEvent.preventDefault()`, `aEvent.stopPropagation()`, `this._getDropPoint()`
- 条件付き依存: `if ( !dropPoint || !dropPoint.ip || !PlacesControllerDragHelper.canDrop(dropPoint.ip, dt) )` → `aEvent.stopPropagation()`
- 条件付き依存: `if (this._overFolder.elt != overElt)` → `this._clearOverFolder()`
- 条件付き依存: `if (this._overFolder.elt != overElt)` → `this._setTimer()`
- 条件付き依存: `if (dropPoint.folderElt || aEvent.originalTarget == this._chevron)` → `this._overFolder.elt.hasAttribute()`
- 条件付き依存: `if (!this._overFolder.elt.hasAttribute("dragover"))` → `this._overFolder.elt.setAttribute()`
- 条件付き依存: `if (this.isRTL)` → `Math.ceil()`
- 条件付き依存: `if (this.isRTL)` → `this._rootElt.getBoundingClientRect()`
- 条件付き依存: `if (dropPoint.beforeIndex == -1)` → `this._rootElt.lastElementChild.getBoundingClientRect()`
- 条件付き依存: `if (!(dropPoint.beforeIndex == -1))` → `this._rootElt.children[ dropPoint.beforeIndex ].getBoundingClientRect()`
- 条件付き依存: `if (!(this._rootElt.firstElementChild))` → `this.#findPrecedingToolbarWidget()`
- 条件付き依存: `if (prevWidget)` → `prevWidget.getBoundingClientRect()`
- 条件付き依存: `if (!(this.isRTL))` → `Math.floor()`
- 条件付き依存: `if (!(this.isRTL))` → `this._rootElt.getBoundingClientRect()`
- 条件付き依存: `if (!(dropPoint.folderElt || aEvent.originalTarget == this._chevron))` → `Math.round()`
- 条件付き依存: `if (!(dropPoint.folderElt || aEvent.originalTarget == this._chevron))` → `this._clearOverFolder()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `aEvent.dataTransfer`, `aEvent.originalTarget`, `aEvent.target`, `dropPoint.beforeIndex`, `dropPoint.folderElt`, `dropPoint.ip`, `ind.clientWidth`, `ind.collapsed`, `ind.parentNode.collapsed`, `ind.style.marginInlineStart`, `ind.style.transform`, `prevWidget.getBoundingClientRect().left`, `prevWidget.getBoundingClientRect().right`, `this._chevron`, `this._dropIndicator`, `this._dropIndicator.collapsed`, `this._overFolder.elt`, `this._overFolder.hoverTime`, `this._overFolder.openTimer`, `this._rootElt.children`, `this._rootElt.children[ dropPoint.beforeIndex ].getBoundingClientRect().left`, `this._rootElt.children[ dropPoint.beforeIndex ].getBoundingClientRect().right`, `this._rootElt.firstElementChild`, `this._rootElt.getBoundingClientRect().left`, `this._rootElt.getBoundingClientRect().right`, `this._rootElt.lastElementChild.getBoundingClientRect().left`, `this._rootElt.lastElementChild.getBoundingClientRect().right`, `this.isRTL`

## PlacesToolbar._onDrop()
- 位置: L2039-2053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.stopPropagation()`, `this._cleanupDragDetails()`, `this._getDropPoint()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop( dropPoint.ip, aEvent.dataTransfer ).catch()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `aEvent.preventDefault()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `aEvent.dataTransfer`, `aEvent.target`, `console.error`, `dropPoint.ip`

## PlacesToolbar._onDragLeave()
- 位置: L2055-2064
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._overFolder.elt)` → `this._setTimer()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._dropIndicator.collapsed`, `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.hoverTime`

## PlacesToolbar._onDragEnd()
- 位置: L2066-2068
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanupDragDetails()`

## PlacesToolbar._onPopupShowing()
- 位置: L2070-2083
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super._onPopupShowing()`
- 条件付き依存: `if (!this._allowPopupShowing)` → `aEvent.preventDefault()`
- 参照: `aEvent.target.parentNode`, `parent.localName`, `this._allowPopupShowing`, `this._openedMenuButton`

## PlacesToolbar._onPopupHidden()
- 位置: L2085-2109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (parent.localName == "toolbarbutton")` → `parent.hasAttribute()`
- 条件付き依存: `if (parent.hasAttribute("dragover"))` → `parent.removeAttribute()`
- 参照: `aEvent.target`, `parent.localName`, `placesNode.containerOpen`, `popup._placesNode`, `popup.parentNode`, `this._openedMenuButton`

## PlacesToolbar._onMouseMove()
- 位置: L2111-2131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesControllerDragHelper.getSession()`
- 参照: `aEvent.originalTarget`, `target.localName`, `target.open`, `target.type`, `this._cachedMouseMoveEvent`, `this._openedMenuButton`, `this._openedMenuButton.open`

## PlacesMenu.constructor()
- 位置: L2147-2172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this._addEventListeners()`, `this._onPopupShowing()`
- 参照: `AppConstants.platform`, `elt.localName`, `elt.parentNode`, `popupShowingEvent.target`, `popupShowingEvent.target.parentNode`, `this._nativeView`, `this._rootElt`, `this._viewElt.parentNode`

## PlacesMenu._init()
- 位置: L2174-2176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._viewElt._placesView`

## PlacesMenu._removeChild()
- 位置: L2178-2180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super._removeChild()`

## PlacesMenu.uninit()
- 位置: L2182-2192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.uninit()`, `this._removeEventListeners()`
- 参照: `this._rootElt`

## PlacesMenu.handleEvent()
- 位置: L2194-2209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onMouseDown()`, `this._onPopupHidden()`, `this._onPopupShowing()`, `this.uninit()`
- 参照: `aEvent.type`

## PlacesMenu._onPopupHidden()
- 位置: L2211-2230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `popup.removeAttribute()`
- 参照: `aEvent.originalTarget`, `placesNode.containerOpen`, `popup._placesNode`

## PlacesMenu._onMouseDown()
- 位置: L2234-2236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.maybeSpeculativeConnectOnMouseDown()`

## PlacesPanelview.constructor()
- 位置: L2242-2250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this._addEventListeners()`, `this._onPopupShowing()`, `this._rootElt.setAttribute()`
- 参照: `this._rootElt`, `this._viewElt._placesView`

## PlacesPanelview.events()
- 位置: L2252-2265
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._events`

## PlacesPanelview.handleEvent()
- 位置: L2267-2297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onCommand()`, `this._onDragEnd()`, `this._onDragStart()`, `this._onMouseDown()`, `this._onPopupHidden()`, `this._onViewShown()`, `this.uninit()`
- 参照: `event.button`, `event.type`

## PlacesPanelview._onCommand()
- 位置: L2299-2326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getRootEvent()`, `PlacesUIUtils.openNodeWithEvent()`
- 条件付き依存: `if (button.parentNode.id == "panelMenu_bookmarksMenu")` → `button.setAttribute()`
- 条件付き依存: `if (!(!PlacesUIUtils.openInTabClosesMenu && modifKey))` → `button.removeAttribute()`
- 条件付き依存: `if ( button.parentNode.id != "panelMenu_bookmarksMenu" || (event.type == "click" && event.button == 1 && PlacesUIUtils.openInTabClosesMenu) )` → `this.panelMultiView.closest("panel").hidePopup()`
- 条件付き依存: `if ( button.parentNode.id != "panelMenu_bookmarksMenu" || (event.type == "click" && event.button == 1 && PlacesUIUtils.openInTabClosesMenu) )` → `this.panelMultiView.closest()`
- 参照: `AppConstants.platform`, `PlacesUIUtils.openInTabClosesMenu`, `button._placesNode`, `button.parentNode.id`, `event.button`, `event.ctrlKey`, `event.metaKey`, `event.originalTarget`, `event.type`

## PlacesPanelview.destroyContextMenu()
- 位置: L2328-2331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.destroyContextMenu()`, `this.maybeClosePanel()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`

## PlacesPanelview.maybeClosePanel()
- 位置: L2341-2359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelMultiView.closest()`, `this.panelMultiView.closest("panel").hidePopup()`
- 条件付き依存: `if ( this._viewElt.id != "PanelUI-bookmarks" || PlacesUIUtils.openInTabClosesMenu )` → `this.panelMultiView.closest("panel").hidePopup()`
- 条件付き依存: `if ( this._viewElt.id != "PanelUI-bookmarks" || PlacesUIUtils.openInTabClosesMenu )` → `this.panelMultiView.closest()`
- 参照: `PlacesUIUtils.openInTabClosesMenu`, `this._viewElt.id`

## PlacesPanelview._onDragEnd()
- 位置: L2361-2363
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._draggedElt`

## PlacesPanelview._onDragStart()
- 位置: L2365-2377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this._controller.setDataTransfer()`, `this._rootElt.focus()`
- 参照: `draggedElt._placesNode`, `draggedElt.parentNode`, `event.originalTarget`, `this._draggedElt`, `this._rootElt`

## PlacesPanelview.uninit()
- 位置: L2379-2384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.uninit()`, `this._removeEventListeners()`
- 参照: `this.events`, `this.panelMultiView`

## PlacesPanelview._createDOMNodeForPlacesNode()
- 位置: L2386-2422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._domNodes.delete()`, `this._domNodes.has()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR)` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `element.classList.add()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `element.setAttribute()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUIUtils.getBestTitle()`
- 条件付き依存: `if (icon)` → `element.setAttribute()`
- 条件付き依存: `if (!this._domNodes.has(placesNode))` → `this._domNodes.set()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `element._placesNode`, `placesNode.icon`, `placesNode.type`, `placesNode.uri`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesPanelview._setEmptyPopupStatus()
- 位置: L2424-2453
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!panelview._emptyMenuitem)` → `document.createXULElement()`
- 条件付き依存: `if (!panelview._emptyMenuitem)` → `panelview._emptyMenuitem.setAttribute()`
- 条件付き依存: `if (!panelview._emptyMenuitem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (empty)` → `panelview.setAttribute()`
- 条件付き依存: `if ( !panelview._startMarker || (!panelview._startMarker.previousElementSibling && !panelview._endMarker.nextElementSibling) )` → `panelview.insertBefore()`
- 条件付き依存: `if (!(empty))` → `panelview.removeAttribute()`
- 条件付き依存: `if (!(empty))` → `panelview.removeChild()`
- 参照: `panelview._emptyMenuitem`, `panelview._emptyMenuitem.className`, `panelview._endMarker`, `panelview._endMarker.nextElementSibling`, `panelview._startMarker`, `panelview._startMarker.previousElementSibling`

## PlacesPanelview._isPopupOpen()
- 位置: L2455-2457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelView.forNode()`
- 参照: `PanelView.forNode(this._viewElt).active`, `this._viewElt`

## PlacesPanelview._onPopupHidden()
- 位置: L2459-2472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `event.originalTarget`, `panelview._placesNode`, `placesNode.containerOpen`

## PlacesPanelview._onPopupShowing()
- 位置: L2474-2483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super._onPopupShowing()`
- 条件付き依存: `if (event.originalTarget == this._rootElt)` → `this._addEventListeners()`
- 参照: `event.originalTarget`, `this._rootElt`, `this._viewElt.panelMultiView`, `this.events`, `this.panelMultiView`

## PlacesPanelview._onViewShown()
- 位置: L2485-2496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controllers.getControllerCount()`
- 条件付き依存: `if (!this.controllers.getControllerCount() && this._controller)` → `this.controllers.appendController()`
- 参照: `event.originalTarget`, `this._controller`, `this._viewElt`

## PlacesPanelview._onMouseDown()
- 位置: L2498-2500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.maybeSpeculativeConnectOnMouseDown()`
