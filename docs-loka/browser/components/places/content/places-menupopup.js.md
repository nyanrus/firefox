# browser/components/places/content/places-menupopup.js

source: browser/components/places/content/places-menupopup.js
source-hash: a0affb9ecff8d39290d24b8474b1fbc7605d931c
lines: 697

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## closingPopupEndsDrag()
- 位置: L11-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popup.querySelectorAll()`
- 参照: `childPopup.isWaylandDragSource`, `popup.isWaylandDragSource`, `popup.isWaylandPopup`

## MozPlacesPopup.constructor()
- 位置: L33-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.addEventListener()`

## MozPlacesPopup.markup()
- 位置: L50-64
- 役割: (未記入)
- 触るとき: (未記入)

## MozPlacesPopup.connectedCallback()
- 位置: L66-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.delayConnectedCallback()`
- 参照: `this._overFolder`

## MozPlacesPopup.elt()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.elt`

## MozPlacesPopup.elt()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.elt`

## MozPlacesPopup.openTimer()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.openTimer`

## MozPlacesPopup.openTimer()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.openTimer`

## MozPlacesPopup.hoverTime()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.hoverTime`

## MozPlacesPopup.hoverTime()
- 位置: L103-105
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.hoverTime`

## MozPlacesPopup.closeTimer()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.closeTimer`

## MozPlacesPopup.closeTimer()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folder.closeTimer`

## MozPlacesPopup.closeMenuTimer()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._closeMenuTimer`

## MozPlacesPopup.closeMenuTimer()
- 位置: L117-119
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._closeMenuTimer`

## OF__setTimer()
- 位置: L121-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `timer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## OF__notify()
- 位置: L127-180
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTimer == this._folder.openTimer)` → `this._folder.elt.lastElementChild.setAttribute()`
- 条件付き依存: `if (aTimer == this._folder.openTimer)` → `this._folder.elt.lastElementChild.openPopup()`
- 条件付き依存: `if (aTimer == this._folder.closeTimer)` → `PlacesControllerDragHelper.draggingOverChildNode()`
- 条件付き依存: `if (aTimer == this._folder.closeTimer)` → `this.clear()`
- 条件付き依存: `if (aTimer == this._folder.closeTimer)` → `closingPopupEndsDrag()`
- 条件付き依存: `if (!draggingOverChild && !closingPopupEndsDrag(this._self))` → `this.closeParentMenus()`
- 条件付き依存: `if (aTimer == this.closeMenuTimer)` → `PlacesControllerDragHelper.getSession()`
- 条件付き依存: `if (aTimer == this.closeMenuTimer)` → `PlacesControllerDragHelper.draggingOverChildNode()`
- 条件付き依存: `if (hidePopup)` → `closingPopupEndsDrag()`
- 条件付き依存: `if (!closingPopupEndsDrag(popup))` → `popup.hidePopup()`
- 条件付き依存: `if (!closingPopupEndsDrag(popup))` → `this.closeParentMenus()`
- 条件付き依存: `if (popup.isWaylandDragSource)` → `this.setTimer()`
- 参照: `popup.isWaylandDragSource`, `popup.parentNode`, `this._closeMenuTimer`, `this._folder.closeTimer`, `this._folder.elt`, `this._folder.openTimer`, `this._self`, `this.closeMenuTimer`, `this.hoverTime`

## OF__closeParentMenus()
- 位置: L185-201
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (parent.localName == "menupopup" && parent._placesNode)` → `PlacesControllerDragHelper.draggingOverChildNode()`
- 条件付き依存: `if (parent.localName == "menupopup" && parent._placesNode)` → `parent.hidePopup()`
- 参照: `parent._placesNode`, `parent.localName`, `parent.parentNode`, `popup.parentNode`, `this._self`

## OF__clear()
- 位置: L206-227
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._folder.elt && this._folder.elt.lastElementChild)` → `popup.hasAttribute()`
- 条件付き依存: `if (this._folder.elt && this._folder.elt.lastElementChild)` → `closingPopupEndsDrag()`
- 条件付き依存: `if ( !popup.hasAttribute("dragover") && !closingPopupEndsDrag(popup) )` → `popup.hidePopup()`
- 条件付き依存: `if (this._folder.elt && this._folder.elt.lastElementChild)` → `this._folder.elt.removeAttribute()`
- 条件付き依存: `if (this._folder.openTimer)` → `this._folder.openTimer.cancel()`
- 条件付き依存: `if (this._folder.closeTimer)` → `this._folder.closeTimer.cancel()`
- 参照: `this._folder.closeTimer`, `this._folder.elt`, `this._folder.elt.lastElementChild`, `this._folder.openTimer`

## MozPlacesPopup._indicatorBar()
- 位置: L231-238
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__indicatorBar)` → `this.shadowRoot.querySelector()`
- 参照: `this.__indicatorBar`

## MozPlacesPopup._rootView()
- 位置: L246-251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__rootView)` → `PlacesUIUtils.getViewForNode()`
- 参照: `this.__rootView`

## MozPlacesPopup._hideDropIndicator()
- 位置: L260-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._endMarker.compareDocumentPosition()`, `this._startMarker.compareDocumentPosition()`
- 参照: `Node.DOCUMENT_POSITION_FOLLOWING`, `Node.DOCUMENT_POSITION_PRECEDING`, `aEvent.target`, `target._placesNode`

## MozPlacesPopup._getDropPoint()
- 位置: L284-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.isFolderReadOnly()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsTagQuery()`, `elt.getBoundingClientRect()`, `this._rootView.controller.disallowInsertion()`
- 条件付き依存: `if (!elt._placesNode)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!elt._placesNode)` → `elt.getAttribute()`
- 条件付き依存: `if (!elt._placesNode)` → `elt.lastElementChild.hasAttribute()`
- 条件付き依存: `if (eventY - eltY < eltHeight * 0.2)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (eventY - eltY < eltHeight * 0.8)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (eventY - eltY <= eltHeight / 2)` → `PlacesUtils.getConcreteItemGuid()`
- 参照: `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `aEvent.clientY`, `aEvent.target`, `dropPoint.folderElt`, `dropPoint.ip`, `elt._placesNode`, `elt._placesNode.title`, `elt.lastElementChild`, `elt.localName`, `elt.parentNode`, `this._placesNode`
- XPCOM: `nsITreeView`

## MozPlacesPopup._cleanupDragDetails()
- 位置: L376-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeAttribute()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._indicatorBar.hidden`, `this._rootView._draggedElt`

## MozPlacesPopup.on_DOMMenuItemActive()
- 位置: L385-409
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (super.on_DOMMenuItemActive)` → `super.on_DOMMenuItemActive()`
- 条件付き依存: `if (window.XULBrowserWindow)` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (!(placesNode && PlacesUtils.nodeIsURI(placesNode)))` → `elt.hasAttribute()`
- 条件付き依存: `if (elt.hasAttribute("targetURI"))` → `elt.getAttribute()`
- 条件付き依存: `if (linkURI)` → `window.XULBrowserWindow.setOverLink()`
- 参照: `elt._placesNode`, `elt.parentNode`, `event.target`, `placesNode.uri`, `super.on_DOMMenuItemActive`, `window.XULBrowserWindow`

## MozPlacesPopup.on_DOMMenuItemInactive()
- 位置: L411-420
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (window.XULBrowserWindow)` → `window.XULBrowserWindow.setOverLink()`
- 参照: `elt.parentNode`, `event.target`, `window.XULBrowserWindow`

## MozPlacesPopup.on_dragstart()
- 位置: L422-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this._rootView.controller.canMoveNode()`, `this._rootView.controller.setDataTransfer()`, `this.setAttribute()`
- 参照: `elt._placesNode`, `event.dataTransfer.effectAllowed`, `event.target`, `this._rootView._draggedElt`

## MozPlacesPopup.on_drop()
- 位置: L443-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this._cleanupDragDetails()`, `this._getDropPoint()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop( dropPoint.ip, event.dataTransfer ).catch()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `event.preventDefault()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `console.error`, `dropPoint.ip`, `event.dataTransfer`, `event.target`

## MozPlacesPopup.on_dragover()
- 位置: L459-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `event.preventDefault()`, `event.stopPropagation()`, `this._getDropPoint()`, `this._hideDropIndicator()`, `this._indicatorBar.parentNode.getBoundingClientRect()`, `this.scrollBox.getBoundingClientRect()`, `this.setAttribute()`
- 条件付き依存: `if ( !dropPoint || !dropPoint.ip || !PlacesControllerDragHelper.canDrop(dropPoint.ip, dt) )` → `event.stopPropagation()`
- 条件付き依存: `if ( this._overFolder.elt && this._overFolder.elt != dropPoint.folderElt )` → `this._overFolder.clear()`
- 条件付き依存: `if (!this._overFolder.elt)` → `this._overFolder.setTimer()`
- 条件付き依存: `if (dropPoint.folderElt)` → `dropPoint.folderElt.setAttribute()`
- 条件付き依存: `if (!(dropPoint.folderElt))` → `this._overFolder.clear()`
- 条件付き依存: `if (scrollDir != 0)` → `this.scrollBox.scrollByIndex()`
- 条件付き依存: `if (dropPoint.folderElt || this._hideDropIndicator(event))` → `event.preventDefault()`
- 条件付き依存: `if (dropPoint.folderElt || this._hideDropIndicator(event))` → `event.stopPropagation()`
- 条件付き依存: `if (scrollDir == 0)` → `elt.getBoundingClientRect()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `dropPoint.folderElt`, `dropPoint.ip`, `elt.getBoundingClientRect().height`, `elt.nextElementSibling`, `elt.screenY`, `event.dataTransfer`, `event.originalTarget`, `event.screenY`, `event.target`, `scrollRect.height`, `scrollRect.y`, `this._indicatorBar.firstElementChild.style.marginTop`, `this._indicatorBar.hidden`, `this._indicatorBar.parentNode.getBoundingClientRect().y`, `this._overFolder.elt`, `this._overFolder.hoverTime`, `this._overFolder.openTimer`, `this.firstElementChild`, `this.scrollBox._scrollButtonDown`, `this.scrollBox._scrollButtonUp`, `this.scrollBox.screenY`

## MozPlacesPopup.on_dragleave()
- 位置: L553-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.contains()`, `this.hasAttribute()`, `this.removeAttribute()`
- 条件付き依存: `if (this._overFolder.elt)` → `this._overFolder.setTimer()`
- 条件付き依存: `if (this.hasAttribute("autoopened") || this.hasAttribute("dragstart"))` → `this._overFolder.setTimer()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `event.relatedTarget`, `this._indicatorBar.hidden`, `this._overFolder.closeMenuTimer`, `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.hoverTime`

## MozPlacesPopup.on_dragend()
- 位置: L585-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanupDragDetails()`

## MozPlacesPopup.uninit()
- 位置: L589-591
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.__rootView`

## MozPlacesPopupArrow.constructor()
- 位置: L602-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.addEventListener()`

## MozPlacesPopupArrow.connectedCallback()
- 位置: L617-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.delayConnectedCallback()`, `this.initializeAttributeInheritance()`, `this.setAttribute()`

## MozPlacesPopupArrow._setSideAttribute()
- 位置: L630-655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `position.indexOf()`
- 条件付き依存: `if (position.indexOf("start_") == 0 || position.indexOf("end_") == 0)` → `this.matches()`
- 条件付き依存: `if (position.indexOf("start_") == 0 || position.indexOf("end_") == 0)` → `position.indexOf()`
- 条件付き依存: `if (position.indexOf("start_") == 0)` → `this.setAttribute()`
- 条件付き依存: `if (!(position.indexOf("start_") == 0))` → `this.setAttribute()`
- 条件付き依存: `if (!(position.indexOf("start_") == 0 || position.indexOf("end_") == 0))` → `position.indexOf()`
- 条件付き依存: `if ( position.indexOf("before_") == 0 || position.indexOf("after_") == 0 )` → `position.indexOf()`
- 条件付き依存: `if (position.indexOf("before_") == 0)` → `this.setAttribute()`
- 条件付き依存: `if (!(position.indexOf("before_") == 0))` → `this.setAttribute()`
- 参照: `event.alignmentPosition`, `this.anchorNode`

## MozPlacesPopupArrow.on_popupshowing()
- 位置: L657-662
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this)` → `this.setAttribute()`
- 参照: `event.target`, `this.style.pointerEvents`

## MozPlacesPopupArrow.on_popuppositioned()
- 位置: L664-668
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this)` → `this._setSideAttribute()`
- 参照: `event.target`

## MozPlacesPopupArrow.on_popupshown()
- 位置: L670-677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setAttribute()`, `this.style.removeProperty()`
- 参照: `event.target`

## MozPlacesPopupArrow.on_popuphiding()
- 位置: L679-683
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this)` → `this.setAttribute()`
- 参照: `event.target`

## MozPlacesPopupArrow.on_popuphidden()
- 位置: L685-690
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this)` → `this.removeAttribute()`
- 参照: `event.target`
