# browser/components/sidebar/sidebar-tab-list.mjs

source: browser/components/sidebar/sidebar-tab-list.mjs
source-hash: 8507f15c631f1efd793144244fd90012a2367ce1
lines: 362

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SidebarTabList.constructor()
- 位置: L18-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.multiSelect`, `this.updatesPaused`

## SidebarTabList.treeView()
- 位置: L47-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `host.getRootNode()`, `this.getRootNode()`
- 参照: `host.getRootNode()?.host`, `host.treeView`, `this.getRootNode()?.host`

## SidebarTabList.#dispatchFocusRowEvent()
- 位置: L58-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.composedPath()`, `this.dispatchEvent()`
- 参照: `row.guid`, `row.localName`

## SidebarTabList.connectedCallback()
- 位置: L72-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`
- 参照: `this.#dispatchFocusRowEvent`

## SidebarTabList.disconnectedCallback()
- 位置: L77-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this.#dispatchFocusRowEvent`

## SidebarTabList.willUpdate()
- 位置: L82-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("tabItems") && Array.isArray(this.tabItems))` → `Services.uuid.generateUUID().toString()`
- 条件付き依存: `if (changedProperties.has("tabItems") && Array.isArray(this.tabItems))` → `Services.uuid.generateUUID()`
- 参照: `item.guid`, `this.tabItems`
- XPCOM: `Services.uuid`

## SidebarTabList.handleFocusElementInRow()
- 位置: L90-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView.handleKeydown()`
- 条件付き依存: `if (!this.treeView)` → `super.handleFocusElementInRow()`
- 条件付き依存: `if (e.defaultPrevented)` → `e.stopPropagation()`
- 参照: `e.defaultPrevented`, `this.treeView`

## SidebarTabList.toggleRowSelection()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView?.toggleSelection()`

## SidebarTabList.clearSelection()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView?.resetSelection()`

## SidebarTabList.selectAll()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView?.selectAllInList()`

## SidebarTabList.itemTemplate()
- 位置: L113-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.currentTarget.primaryActionHandler()`, `html()`, `ifDefined()`, `this.isTabItemSelected()`, `this.treeView?.isActiveNode()`
- 条件付き依存: `if (tabItem.time)` → `tabItem.time.toString()`
- 参照: `stringTime.length`, `tabItem.canClose`, `tabItem.closeRequested`, `tabItem.closedId`, `tabItem.containerObj`, `tabItem.fxaDeviceId`, `tabItem.guid`, `tabItem.icon`, `tabItem.indicators`, `tabItem.primaryL10nArgs`, `tabItem.primaryL10nId`, `tabItem.secondaryActionClass`, `tabItem.secondaryL10nArgs`, `tabItem.secondaryL10nId`, `tabItem.sourceClosedId`, `tabItem.sourceWindowId`, `tabItem.tabElement`, `tabItem.time`, `tabItem.title`, `tabItem.url`, `this.activeIndex`, `this.currentActiveElementId`, `this.dateTimeFormat`, `this.hasPopup`, `this.inactiveWindow`, `this.mediumView`, `this.searchQuery`, `this.secondaryActionClass`, `this.timeMsPref`

## SidebarTabList.isTabItemSelected()
- 位置: L162-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.treeView?.isSelected()`
- 参照: `tabItem.guid`

## SidebarTabList.stylesheets()
- 位置: L166-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `super.stylesheets()`

## SidebarTabRow.willUpdate()
- 位置: L214-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.willUpdate()`
- 条件付き依存: `if (changedProperties.has("tabElement"))` → `this.#tabSelectObserver?.disconnect()`
- 条件付き依存: `if (this.tabElement)` → `this.#tabSelectObserver.observe()`
- 参照: `this.#tabSelectObserver`, `this.current`, `this.tabElement`, `this.tabElement.selected`, `this.tabElement?.selected`

## SidebarTabRow.disconnectedCallback()
- 位置: L234-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#tabSelectObserver?.disconnect()`
- 参照: `this.#tabSelectObserver`

## SidebarTabRow.tooltipText()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.primaryL10nId`, `this.url`

## SidebarTabRow.focus()
- 位置: L248-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HTMLElement.prototype.focus.call()`

## SidebarTabRow.#getContainerClasses()
- 位置: L252-260
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.containerObj)` → `containerClasses.push()`
- 参照: `this.containerObj`

## SidebarTabRow.#containerIndicatorTemplate()
- 位置: L262-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `tabsToCheck.some()`, `this.#getContainerClasses()`, `this.#getContainerClasses().join()`, `this.getRootNode()`, `when()`
- 参照: `tab.containerObj`, `tabList.tabItems`, `this.getRootNode().host`

## SidebarTabRow.#getDomain()
- 位置: L271-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `this.formatURIForDisplay()`
- 参照: `this.url`
- XPCOM: `Services.eTLD` / `Services.io`

## SidebarTabRow.#domainTemplate()
- 位置: L284-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#getDomain()`

## SidebarTabRow.secondaryButtonTemplate()
- 位置: L293-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `this.getIconSrc()`, `when()`
- 参照: `this.hasPopup`, `this.secondaryActionClass`, `this.secondaryActionHandler`, `this.secondaryL10nArgs`, `this.secondaryL10nId`

## SidebarTabRow.render()
- 位置: L313-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `this.#containerIndicatorTemplate()`, `this.#domainTemplate()`, `this.faviconTemplate()`, `this.indicators?.includes()`, `this.secondaryButtonTemplate()`, `this.stylesheets()`, `this.timeTemplate()`, `this.titleTemplate()`, `when()`
- 参照: `this.auxActionHandler`, `this.canClose`, `this.closeRequested`, `this.containerObj`, `this.mediumView`, `this.primaryActionHandler`, `this.primaryL10nArgs`, `this.primaryL10nId`, `this.tooltipText`, `this.url`
