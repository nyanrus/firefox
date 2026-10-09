# browser/components/sidebar/sidebar-page.mjs

source: browser/components/sidebar/sidebar-page.mjs
source-hash: 81125816d0315efed7ec08d160c0d1940be4dc29
lines: 318

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SidebarPage.constructor()
- 位置: L20-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.clearDocument.bind()`
- 参照: `this.clearDocument`

## SidebarPage.connectedCallback()
- 位置: L25-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.documentGlobal.addEventListener()`
- 参照: `this._contextMenu`, `this.clearDocument`, `this.topWindow.SidebarController.currentContextMenu`

## SidebarPage.disconnectedCallback()
- 位置: L33-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.documentGlobal.removeEventListener()`
- 参照: `this.clearDocument`

## SidebarPage.topWindow()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.documentGlobal.top`

## SidebarPage.sidebarController()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.topWindow.SidebarController`

## SidebarPage.keydownHandler()
- 位置: L50-60
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._keydownHandler`

## this._keydownHandler()
- 位置: L52-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView?.handleKeydown()`
- 条件付き依存: `if (e.defaultPrevented)` → `e.stopPropagation()`
- 参照: `e.defaultPrevented`

## SidebarPage.getNodesInOrder()
- 位置: L68-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectNodes()`
- 参照: `this.renderRoot`

## SidebarPage.#collectNodes()
- 位置: L74-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.getAttribute()`
- 条件付き依存: `if (isCard)` → `nodes.push()`
- 条件付き依存: `if (el.expanded)` → `this.#collectNodes()`
- 条件付き依存: `if (isTabList)` → `el.tabItems.entries()`
- 条件付き依存: `if (isTabList)` → `nodes.push()`
- 条件付き依存: `if (!(isTabList))` → `this.#collectNodes()`
- 参照: `el.expanded`, `el.localName`, `el.tabItems`

## SidebarPage.domNode()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `el.summaryEl`

## SidebarPage.domNode()
- 位置: L98-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `el.shadowRoot.querySelector()`
- 参照: `item.guid`

## SidebarPage.setExpanded()
- 位置: L120-126
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `node.card.expanded`, `node.card?.expanded`, `node.type`

## SidebarPage.addContextMenuListeners()
- 位置: L128-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contextMenu.addEventListener()`, `this.addEventListener()`
- 参照: `this.placesContextHiding`, `this.placesContextShowing`

## SidebarPage.removeContextMenuListeners()
- 位置: L138-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contextMenu.removeEventListener()`, `this.removeEventListener()`
- 参照: `this.placesContextHiding`, `this.placesContextShowing`

## SidebarPage.addSidebarFocusedListeners()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.topWindow.addEventListener()`

## SidebarPage.removeSidebarFocusedListeners()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.topWindow.removeEventListener()`

## SidebarPage.handleEvent()
- 位置: L159-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleCommandEvent()`, `this.handleContextMenuEvent()`, `this.handleSidebarFocusedEvent()`
- 参照: `e.type`

## SidebarPage.placesContextShowing()
- 位置: L173-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUIUtils.placesContextShowing()`

## SidebarPage.placesContextHiding()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUIUtils.placesContextHiding()`

## SidebarPage.findTriggerNode()
- 位置: L192-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.explicitOriginalTarget.flattenedTreeParentNode.getRootNode()`, `e.originalTarget.flattenedTreeParentNode.getRootNode()`
- 参照: `e.explicitOriginalTarget`, `e.explicitOriginalTarget.flattenedTreeParentNode.getRootNode().host`, `e.originalTarget.flattenedTreeParentNode`, `e.originalTarget.flattenedTreeParentNode.getRootNode().host`, `el?.localName`

## SidebarPage.handleCommandEvent()
- 位置: L215-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.BrowserUtils.copyLink()`, `this.forgetAboutThisSite()`, `this.forgetAboutThisSite().catch()`, `this.topWindow.PlacesCommandHook.bookmarkLink()`, `this.topWindow.openTrustedLinkIn()`
- 参照: `console.error`, `e.target.id`, `this.triggerNode.title`, `this.triggerNode.url`
- XPCOM: `Services.prefs`

## SidebarPage.forgetAboutThisSite()
- 位置: async L270-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsHost()`, `Promise.withResolvers()`, `Services.eTLD.getBaseDomainFromHost()`, `this.topWindow.gDialogBox.open()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsHost(this.triggerNode)))` → `Services.io.newURI()`
- 参照: `Services.io.newURI(this.triggerNode.url).host`, `deferred.promise`, `this.triggerNode`, `this.triggerNode.query.domain`, `this.triggerNode.url`
- XPCOM: `Services.eTLD` / `Services.io`

## onAccept()
- 位置: L289-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.resolve()`

## onCancel()
- 位置: L290-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.resolve()`

## SidebarPage.clearDocument()
- 位置: L300-302
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.documentGlobal.document.body.textContent`

## SidebarPage.stylesheet()
- 位置: L309-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
