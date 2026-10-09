# browser/components/customizableui/PanelMultiView.sys.mjs

source: browser/components/customizableui/PanelMultiView.sys.mjs
source-hash: 122165dba992614f41a7fdafe23dd74a74e0ed8c
lines: 2200

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/inspector/deep-tree-walker;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `Services.strings.createBundle()`

## constructor()
- 位置: L43-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.isDeadWrapper()`, `this.#walker.init()`
- 参照: `node.documentGlobal`, `node.documentGlobal.location`, `this.#onlyWantElements`, `this.#showAnonymousContent`, `this.#walker.showAnonymousContent`, `this.#walker.showDocumentsAsNodes`, `this.#walker.showSubDocuments`, `this.filter`

## currentNode()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#walker.currentNode`

## currentNode()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#walker.currentNode`, `this.#walker.root`

## parentNode()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#walker.parentNode()`

## root()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#walker.root`

## previousNode()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#previousGoodNodeInRoot()`

## nextNode()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#nextGoodNodeInRoot()`

## #getLastPreOrderDepthFirstNodeIn()
- 位置: L88-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `last.lastChild`, `last?.lastChild`

## previousSibling()
- 位置: L96-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#walker.previousSibling()`, `this.isSkippedNode()`

## #previousGoodNodeInRoot()
- 位置: L104-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `previousNode?.getRootNode()`, `this.#walker.previousNode()`, `this.isSkippedNode()`
- 参照: `previousNode?.getRootNode()?.host`, `this.#walker`, `this.#walker.currentNode`

## #nextGoodNodeInRoot()
- 位置: L127-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#walker.nextNode()`, `this.isSkippedNode()`
- 参照: `currentNode.shadowRoot`, `this.#showAnonymousContent`, `this.#walker`, `this.#walker.showAnonymousContent`

## firstChild()
- 位置: L158-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#nextGoodNodeInRoot()`, `this.isSkippedNode()`
- 参照: `this.#walker.currentNode`, `this.#walker.root`

## lastChild()
- 位置: L169-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getLastPreOrderDepthFirstNodeIn()`, `this.#previousGoodNodeInRoot()`, `this.isSkippedNode()`
- 参照: `this.#walker.currentNode`, `this.#walker.root`

## isSkippedNode()
- 位置: L183-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.filter()`
- 参照: `Node.ELEMENT_NODE`, `NodeFilter.FILTER_ACCEPT`, `node.nodeType`, `this.#onlyWantElements`

## constructor()
- 位置: L213-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 参照: `this._blockersPromise`, `this.node`

## forNode()
- 位置: L235-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNodeToObjectMap.get()`
- 条件付き依存: `if (!associatedToNode)` → `gNodeToObjectMap.set()`

## document()
- 位置: L249-251
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.node.ownerDocument`

## window()
- 位置: L258-260
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.node.documentGlobal`

## _getBoundsWithoutFlushing()
- 位置: L274-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.windowUtils.getBoundsWithoutFlushing()`

## dispatchCustomEvent()
- 位置: L290-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.node.dispatchEvent()`
- 参照: `event.defaultPrevented`, `this.window.CustomEvent`

## dispatchAsyncEvent()
- 位置: async L326-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blockersPromise.then()`, `this._blockersPromise.catch()`, `this.dispatchCustomEvent()`
- 条件付き依存: `if (blockers.size)` → `this.window.setTimeout()`
- 条件付き依存: `if (blockers.size)` → `Promise.race()`
- 条件付き依存: `if (blockers.size)` → `Promise.all()`
- 条件付き依存: `if (blockers.size)` → `results.some()`
- 条件付き依存: `if (blockers.size)` → `console.error()`
- 参照: `blockers.size`, `this._blockersPromise`

## addBlocker()
- 位置: L334-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blockers.add()`, `console.error()`, `promise.catch()`

## openPopup()
- 位置: async L393-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelNode.openPopup()`, `panelNode.querySelector()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode(panelMultiViewNode).openPopup()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode()`

## hidePopup()
- 位置: L417-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelNode.querySelector()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode(panelMultiViewNode).hidePopup()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode()`
- 条件付き依存: `if (!(panelMultiViewNode))` → `panelNode.hidePopup()`

## removePopup()
- 位置: L440-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelNode.querySelector()`, `panelNode.remove()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode()`
- 条件付き依存: `if (panelMultiViewNode)` → `panelMultiView._moveOutKids()`
- 条件付き依存: `if (panelMultiViewNode)` → `panelMultiView.disconnect()`

## getViewNode()
- 位置: L467-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `viewCacheTemplate?.content.querySelector()`

## ensureUnloadHandlerRegistered()
- 位置: L483-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gWindowsWithUnloadHandler.add()`, `gWindowsWithUnloadHandler.has()`, `this.forNode()`, `this.forNode(panelMultiViewNode).disconnect()`, `window.addEventListener()`, `window.document.querySelectorAll()`

## #panel()
- 位置: L507-509
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.node.parentNode`

## #transitioning()
- 位置: L517-523
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (val)` → `this.node.setAttribute()`
- 条件付き依存: `if (!(val))` → `this.node.removeAttribute()`

## constructor()
- 位置: L525-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `super()`
- 参照: `this._openPopupPromise`

## connect()
- 位置: L536-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `PanelMultiView.ensureUnloadHandlerRegistered()`, `["goBack", "showSubView"].forEach()`, `offscreenViewContainer.append()`, `offscreenViewContainer.classList.add()`, `offscreenViewStack.classList.add()`, `this.#panel.addEventListener()`, `this.document.createXULElement()`, `this.node.prepend()`, `viewContainer.append()`, `viewContainer.classList.add()`, `viewStack.classList.add()`
- 参照: `this._offscreenViewStack`, `this._viewContainer`, `this._viewStack`, `this.connected`, `this.node`, `this.openViews`, `this.window`

## value()
- 位置: L571-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this[method]()`

## disconnect()
- 位置: L581-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel.removeEventListener()`, `this.document.documentElement.removeEventListener()`
- 参照: `this._openPopupCancelCallback`, `this._openPopupPromise`, `this._transitionDetails`, `this._viewContainer`, `this._viewStack`, `this.connected`, `this.node`

## openPopup()
- 位置: async L642-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["open", "showing"].includes()`, `cancelCallback()`, `openPopupPromise.then()`, `this.#panel.openPopup()`, `this.#panel.setAttribute()`, `this.#showMainView()`, `this._openPopupPromise.catch()`, `this.dispatchCustomEvent()`
- 条件付き依存: `if (!this.connected)` → `this.connect()`
- 条件付き依存: `if (!(await this.#showMainView()))` → `cancelCallback()`
- 条件付き依存: `if (this.#panel.state == "closed" && this.openViews.length)` → `this.dispatchCustomEvent()`
- 参照: `MouseEvent.MOZ_SOURCE_KEYBOARD`, `options.triggerEvent`, `options.triggerEvent.type`, `options.triggerEvent?.inputSource`, `this.#panel.state`, `this._openPopupCancelCallback`, `this._openPopupPromise`, `this.connected`, `this.node`, `this.openViews`, `this.openViews.length`, `this.openViews[0].focusWhenActive`

## this._openPopupCancelCallback()
- 位置: L649-664
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (canCancel && this.node)` → `this.dispatchCustomEvent()`
- 参照: `this._openPopupCancelCallback`, `this.node`

## hidePopup()
- 位置: L775-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["open", "showing"].includes()`, `this.closeAllViews()`
- 条件付き依存: `if (["open", "showing"].includes(this.#panel.state))` → `this.#panel.hidePopup()`
- 条件付き依存: `if (!(["open", "showing"].includes(this.#panel.state)))` → `this._openPopupCancelCallback()`
- 参照: `this.#panel.state`, `this.connected`, `this.node`

## _moveOutKids()
- 位置: L803-817
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `this.document.getElementById()`, `this.node?.getAttribute()`, `viewCache.moveBefore()`
- 参照: `this._viewStack.children`

## showSubView()
- 位置: L831-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#showSubView()`, `this.#showSubView(viewIdOrNode, anchor).catch()`
- 参照: `console.error`

## #showSubView()
- 位置: async L849-946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelView.forNode()`, `anchor?.getAttribute()`, `anchor?.removeAttribute()`, `anchor?.setAttribute()`, `prevPanelView.captureKnownSize()`, `this.#activateView()`, `this.#openView()`, `this.#transitionViews()`, `this.openViews.includes()`, `this.openViews[0].node.getAttribute()`, `viewNode.getAttribute()`
- 条件付き依存: `if (!viewNode)` → `console.error()`
- 条件付き依存: `if (!this.openViews.length)` → `console.error()`
- 条件付き依存: `if (this.openViews.includes(nextPanelView))` → `console.error()`
- 条件付き依存: `if (!(await this.#openView(nextPanelView)))` → `prevPanelView.isOpenIn()`
- 条件付き依存: `if (l10nId)` → `viewNode.getAttribute()`
- 条件付き依存: `if (l10nId)` → `JSON.parse()`
- 条件付き依存: `if (l10nId)` → `viewNode.ownerDocument.l10n.formatMessages()`
- 条件付き依存: `if (l10nId)` → `msg.attributes.find()`
- 条件付き依存: `if (anchor)` → `viewNode.classList.add()`
- 参照: `a.name`, `msg.attributes.find(a => a.name === "title")?.value`, `nextPanelView.focusWhenActive`, `nextPanelView.headerText`, `nextPanelView.mainview`, `nextPanelView.minMaxHeight`, `nextPanelView.minMaxWidth`, `prevPanelView._doingKeyboardActivation`, `prevPanelView.active`, `prevPanelView.knownHeight`, `prevPanelView.knownWidth`, `prevPanelView.node`, `this.document`, `this.openViews`, `this.openViews.length`, `viewNode.id`

## goBack()
- 位置: L951-953
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#goBack()`, `this.#goBack().catch()`
- 参照: `console.error`

## #goBack()
- 位置: async L962-986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prevPanelView.captureKnownSize()`, `this.#activateView()`, `this.#closeLatestView()`, `this.#transitionViews()`
- 参照: `nextPanelView.node`, `prevPanelView.active`, `prevPanelView.node`, `this.openViews`, `this.openViews.length`

## #showMainView()
- 位置: async L994-1027
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelView.forNode()`, `this.#openView()`, `this.node.getAttribute()`
- 条件付き依存: `if (oldPanelMultiViewNode)` → `PanelMultiView.forNode(oldPanelMultiViewNode).hidePopup()`
- 条件付き依存: `if (oldPanelMultiViewNode)` → `PanelMultiView.forNode()`
- 条件付き依存: `if (oldPanelMultiViewNode)` → `this.window.promiseDocumentFlushed()`
- 参照: `nextPanelView.headerText`, `nextPanelView.mainview`, `nextPanelView.minMaxHeight`, `nextPanelView.minMaxWidth`, `nextPanelView.node.panelMultiView`, `nextPanelView.visible`, `this.document`

## #openView()
- 位置: async L1041-1083
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelView.dispatchAsyncEvent()`, `panelView.node.hasAttribute()`, `style.removeProperty()`, `this.#panel.toggleAttribute()`, `this.openViews.push()`
- 条件付き依存: `if (panelView.node.parentNode != this._viewStack)` → `this._viewStack.appendChild()`
- 条件付き依存: `if (canceled)` → `this.#closeLatestView()`
- 参照: `panelView.node`, `panelView.node.panelMultiView`, `panelView.node.parentNode`, `this._viewStack`, `this.node`, `this.openViews.length`

## #activateView()
- 位置: L1092-1101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelView.isOpenIn()`
- 条件付き依存: `if (panelView.focusWhenActive)` → `panelView.focusFirstNavigableElement()`
- 条件付き依存: `if (panelView.isOpenIn(this))` → `panelView.dispatchCustomEvent()`
- 参照: `panelView.active`, `panelView.focusWhenActive`

## #closeLatestView()
- 位置: L1110-1119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelView.clearNavigation()`, `panelView.dispatchCustomEvent()`, `this.openViews.pop()`
- 参照: `panelView.node.panelMultiView`, `panelView.visible`

## closeAllViews()
- 位置: L1124-1129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeLatestView()`
- 参照: `this.openViews.length`

## #transitionViews()
- 位置: async L1148-1341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelView.forNode()`, `deepestNode.style.removeProperty()`, `nextPanelView.focusSelectedElement()`, `nextPanelView.isOpenIn()`, `nextPanelView.node.style.removeProperty()`, `this.#cleanupTransitionPhase()`, `this.#panel.style.removeProperty()`, `this._getBoundsWithoutFlushing()`, `this.window.matchMedia()`, `this.window.promiseDocumentFlushed()`, `viewNode.getAttribute()`, `window.promiseDocumentFlushed()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `Object.assign()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `viewNode.customRectGetter()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `header.classList.contains()`
- 条件付き依存: `if (header && header.classList.contains("panel-header"))` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (header && header.classList.contains("panel-header"))` → `this._getBoundsWithoutFlushing()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `nextPanelView.isOpenIn()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._offscreenViewStack.appendChild()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._getBoundsWithoutFlushing()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `nextPanelView.isOpenIn()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._viewStack.appendChild()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._offscreenViewStack.style.removeProperty()`
- 条件付き依存: `if (viewNode.getAttribute("mainview"))` → `this._viewContainer.style.removeProperty()`
- 条件付き依存: `if (viewNode.getAttribute("mainview"))` → `this.#panel.setAttribute()`
- 条件付き依存: `if (!(viewNode.getAttribute("mainview")))` → `this.#panel.removeAttribute()`
- 条件付き依存: `if ( this.window.matchMedia("(prefers-reduced-motion: no-preference)") .matches && !viewNode.getAttribute("no-panelview-transition") )` → `this._viewContainer.addEventListener()`
- 参照: `TRANSITION_PHASES.PREPARE`, `TRANSITION_PHASES.START`, `TRANSITION_PHASES.TRANSITION`, `deepestNode.style.outline`, `details.cancelListener`, `details.listener`, `details.phase`, `details.resolve`, `nextPanelView.knownHeight`, `nextPanelView.knownWidth`, `nextPanelView.visible`, `olderView.knownHeight`, `prevPanelView.knownHeight`, `prevPanelView.knownWidth`, `prevPanelView.visible`, `rect.height`, `rect.width`, `this.#panel`, `this.#panel.style.height`, `this.#panel.style.width`, `this.#transitioning`, `this._getBoundsWithoutFlushing(header).height`, `this._offscreenViewStack.style.minHeight`, `this._transitionDetails`, `this._viewContainer.style.height`, `this._viewContainer.style.minHeight`, `this._viewContainer.style.width`, `this._viewStack.style.marginInlineStart`, `this._viewStack.style.transform`, `this._viewStack.style.transition`, `this._viewStack.style.willChange`, `this.window.RTL_UI`, `this.window.matchMedia("(prefers-reduced-motion: no-preference)") .matches`, `viewNode.customRectGetter`, `viewNode.firstElementChild`, `viewNode.style.width`, `viewRect.height`, `viewRect.width`

## details.listener()
- 位置: L1290-1306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `this._viewContainer.removeEventListener()`
- 参照: `details.listener`, `ev.propertyName`, `ev.target`, `this._viewStack`

## details.cancelListener()
- 位置: L1310-1320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `this._viewContainer.removeEventListener()`
- 参照: `details.cancelListener`, `ev.target`, `this._viewStack`

## #cleanupTransitionPhase()
- 位置: L1348-1382
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (phase >= TRANSITION_PHASES.START)` → `this.#panel.removeAttribute()`
- 条件付き依存: `if (phase >= TRANSITION_PHASES.START)` → `this._viewContainer.style.removeProperty()`
- 条件付き依存: `if (phase >= TRANSITION_PHASES.PREPARE)` → `this._viewStack.style.removeProperty()`
- 条件付き依存: `if (phase >= TRANSITION_PHASES.TRANSITION)` → `this._viewStack.style.removeProperty()`
- 条件付き依存: `if (listener)` → `this._viewContainer.removeEventListener()`
- 条件付き依存: `if (cancelListener)` → `this._viewContainer.removeEventListener()`
- 条件付き依存: `if (resolve)` → `resolve()`
- 参照: `TRANSITION_PHASES.PREPARE`, `TRANSITION_PHASES.START`, `TRANSITION_PHASES.TRANSITION`, `this.#transitioning`, `this._transitionDetails`

## handleEvent()
- 位置: L1390-1467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.type.startsWith()`, `currentView.keyNavigation()`, `this.#activateView()`, `this.#cleanupTransitionPhase()`, `this.#panel.removeEventListener()`, `this._viewContainer.removeAttribute()`, `this._viewContainer.setAttribute()`, `this._viewContainer.style.removeProperty()`, `this._viewStack.style.removeProperty()`, `this.closeAllViews()`, `this.dispatchCustomEvent()`, `this.document.documentElement.removeEventListener()`, `this.node.hasAttribute()`, `this.openViews.forEach()`
- 条件付き依存: `if (!panelView.ignoreMouseMove)` → `panelView.clearNavigation()`
- 条件付き依存: `if (!this.node.hasAttribute("disablekeynav"))` → `this.document.documentElement.addEventListener()`
- 条件付き依存: `if (!this.node.hasAttribute("disablekeynav"))` → `this.#panel.addEventListener()`
- 参照: `aEvent.target`, `aEvent.type`, `panelView.ignoreMouseMove`, `this.#panel`, `this.#transitioning`, `this.node`, `this.openViews`, `this.openViews.length`

## constructor()
- 位置: L1474-1501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.window.addEventListener()`
- 参照: `this.#_arrowNavigableWalker`, `this.#_tabNavigableWalker`, `this.active`, `this.focusWhenActive`

## isOpenIn()
- 位置: L1511-1513
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `panelMultiView.node`, `this.node.panelMultiView`

## mainview()
- 位置: L1525-1531
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `this.node.setAttribute()`
- 条件付き依存: `if (!(value))` → `this.node.removeAttribute()`

## visible()
- 位置: L1541-1549
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `this.node.setAttribute()`
- 条件付き依存: `if (!(value))` → `this.node.removeAttribute()`
- 参照: `this.active`, `this.focusWhenActive`

## minMaxWidth()
- 位置: L1558-1566
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(value))` → `style.removeProperty()`
- 参照: `style.maxWidth`, `style.minWidth`, `this.node.style`

## minMaxHeight()
- 位置: L1575-1583
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(value))` → `style.removeProperty()`
- 参照: `style.maxHeight`, `style.minHeight`, `this.node.style`

## headerText()
- 位置: L1600-1674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ensureHeaderSeparator()`, `h1.appendChild()`, `header.append()`, `header.classList.add()`, `this.document.createElement()`, `this.document.createXULElement()`, `this.node.getAttribute()`, `this.node.prepend()`, `this.node.querySelector()`
- 条件付き依存: `if (header)` → `header.querySelector()`
- 条件付き依存: `if (headerBackButton)` → `headerBackButton.remove()`
- 条件付き依存: `if (value)` → `this.node.getAttribute()`
- 条件付き依存: `if ( !isMainView && !headerBackButton && !this.node.getAttribute("no-back-button") )` → `header.prepend()`
- 条件付き依存: `if ( !isMainView && !headerBackButton && !this.node.getAttribute("no-back-button") )` → `this.createHeaderBackButton()`
- 条件付き依存: `if (value)` → `header.querySelector()`
- 条件付き依存: `if (value)` → `ensureHeaderSeparator()`
- 条件付き依存: `if (!(value))` → `this.node.getAttribute()`
- 条件付き依存: `if (header.nextSibling.tagName == "toolbarseparator")` → `header.nextSibling.remove()`
- 条件付き依存: `if ( !this.node.getAttribute("has-custom-header") && !this.node.getAttribute("mainview-with-header") )` → `header.remove()`
- 条件付き依存: `if (!isMainView)` → `this.createHeaderBackButton()`
- 条件付き依存: `if (!isMainView)` → `header.append()`
- 参照: `header.nextSibling.tagName`, `header.querySelector(".panel-header > h1 > span").textContent`, `span.textContent`

## ensureHeaderSeparator()
- 位置: L1601-1606
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (headerNode.nextSibling.tagName != "toolbarseparator")` → `this.document.createXULElement()`
- 条件付き依存: `if (headerNode.nextSibling.tagName != "toolbarseparator")` → `this.node.insertBefore()`
- 参照: `headerNode.nextSibling`, `headerNode.nextSibling.tagName`

## createHeaderBackButton()
- 位置: L1679-1695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `backButton.addEventListener()`, `backButton.blur()`, `backButton.setAttribute()`, `lazy.gBundle.GetStringFromName()`, `this.document.createXULElement()`, `this.node.panelMultiView.goBack()`
- 参照: `backButton.className`

## dispatchCustomEvent()
- 位置: L1706-1709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.ensureSubviewListeners()`, `super.dispatchCustomEvent()`
- 参照: `this.node`

## captureKnownSize()
- 位置: L1718-1722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getBoundsWithoutFlushing()`
- 参照: `rect.height`, `rect.width`, `this.knownHeight`, `this.knownWidth`, `this.node`

## #isNavigableWithTabOnly()
- 位置: L1733-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `element.dataset?.navigableWithTabOnly`, `element.localName`

## #makeNavigableTreeWalker()
- 位置: L1759-1816
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.node`

## filter()
- 位置: L1760-1812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.checkVisibility()`, `node.classList.contains()`, `node.localName.toLowerCase()`, `this.#isNavigableWithTabOnly()`, `this._getBoundsWithoutFlushing()`
- 条件付き依存: `if ( localName == "button" || localName == "toolbarbutton" || localName == "checkbox" || localName == "a" || localName == "moz-button" || localName == "moz-box-b...)` → `node.hasAttribute()`
- 条件付き依存: `if ( localName != "browser" && localName != "iframe" && localName != "input" && !node.hasAttribute("tabindex") && node.dataset?.capturesFocus !== "true" )` → `node.setAttribute()`
- 参照: `NodeFilter.FILTER_ACCEPT`, `NodeFilter.FILTER_REJECT`, `NodeFilter.FILTER_SKIP`, `bounds.height`, `bounds.width`, `node.dataset?.capturesFocus`, `node.disabled`

## _tabNavigableWalker()
- 位置: L1828-1833
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#_tabNavigableWalker)` → `this.#makeNavigableTreeWalker()`
- 参照: `this.#_tabNavigableWalker`

## #arrowNavigableWalker()
- 位置: L1842-1847
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#_arrowNavigableWalker)` → `this.#makeNavigableTreeWalker()`
- 参照: `this.#_arrowNavigableWalker`

## selectedElement()
- 位置: L1857-1859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._selectedElement.get()`
- 参照: `this._selectedElement`

## selectedElement()
- 位置: L1861-1867
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(!value))` → `Cu.getWeakReference()`
- 参照: `this._selectedElement`

## focusFirstNavigableElement()
- 位置: L1878-1894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focusSelectedElement()`, `walker.currentNode.classList.contains()`, `walker.firstChild()`, `walker.nextNode()`
- 参照: `this.#arrowNavigableWalker`, `this._tabNavigableWalker`, `this.selectedElement`, `walker.currentNode`, `walker.root`

## focusLastNavigableElement()
- 位置: L1903-1909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focusSelectedElement()`, `walker.lastChild()`
- 参照: `this.#arrowNavigableWalker`, `this._tabNavigableWalker`, `this.selectedElement`, `walker.currentNode`, `walker.root`

## moveSelection()
- 位置: L1920-1959
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!oldSel)` → `this.node.compareDocumentPosition()`
- 条件付き依存: `if (oldSel)` → `walker.nextNode()`
- 条件付き依存: `if (oldSel)` → `walker.previousNode()`
- 条件付き依存: `if (!newSel)` → `walker.firstChild()`
- 条件付き依存: `if (!newSel)` → `walker.lastChild()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `oldSel.shadowRoot.activeElement`, `oldSel?.shadowRoot?.activeElement`, `this.#arrowNavigableWalker`, `this._tabNavigableWalker`, `this.document.activeElement`, `this.selectedElement`, `walker.currentNode`, `walker.root`

## keyNavigation()
- 位置: L1980-2172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.classList.contains()`, `button.focus()`, `isContextMenuOpen()`, `stop()`, `tabOnly()`, `target.dispatchEvent()`, `this.focusFirstNavigableElement()`, `this.focusLastNavigableElement()`, `this.moveSelection()`, `this.node.compareDocumentPosition()`
- 条件付き依存: `if ( (!this.window.RTL_UI && keyCode == "ArrowLeft") || (this.window.RTL_UI && keyCode == "ArrowRight") )` → `this.node.panelMultiView.goBack()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `button.buttonEl`, `button.localName`, `button?.localName`, `details.composed`, `event.altKey`, `event.code`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `event.target.documentGlobal.MouseEvent`, `event.target.documentGlobal.PointerEvent`, `focus.dataset?.capturesFocus`, `focus.localName`, `focus.open`, `focus.shadowRoot.activeElement`, `focus.tagName`, `focus?.shadowRoot?.activeElement`, `this._doingKeyboardActivation`, `this.active`, `this.document.activeElement`, `this.ignoreMouseMove`, `this.selectedElement`, `this.window.RTL_UI`

## stop()
- 位置: L2018-2021
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`

## tabOnly()
- 位置: L2027-2032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isNavigableWithTabOnly()`

## isContextMenuOpen()
- 位置: L2038-2052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contextNode.getAttribute()`, `focus.closest()`, `this.document.getElementById()`
- 参照: `popup.state`

## focusSelectedElement()
- 位置: L2181-2187
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (selected)` → `Services.focus.setFocus()`
- 参照: `Services.focus.FLAG_BYKEY`, `this.selectedElement`
- XPCOM: `Services.focus`

## clearNavigation()
- 位置: L2192-2198
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (selected)` → `selected.blur()`
- 参照: `this.selectedElement`
