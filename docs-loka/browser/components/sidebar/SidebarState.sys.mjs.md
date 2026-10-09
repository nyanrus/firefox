# browser/components/sidebar/SidebarState.sys.mjs

source: browser/components/sidebar/SidebarState.sys.mjs
source-hash: 3fd531790ab22394931fb457d6263bb337618a1f
lines: 939

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## SidebarState.constructor()
- 位置: L101-109
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `controller.sidebarRevampEnabled`, `controller.sidebarRevampVisibility`, `this.#controller`, `this.#props.launcherVisible`, `this.defaultLauncherVisible`, `this.revampEnabled`, `this.revampVisibility`

## SidebarState.#launcherEl()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller.sidebarMain`

## SidebarState.#launcherContainerEl()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller.sidebarContainer`

## SidebarState.#launcherSplitterEl()
- 位置: L134-136
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller.launcherSplitter`

## SidebarState.#sidebarBoxEl()
- 位置: L143-145
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller._box`

## SidebarState.#panelEl()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller._box`

## SidebarState.#pinnedTabsContainerEl()
- 位置: L161-163
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller._pinnedTabsContainer`

## SidebarState.#pinnedTabsItemsWrapper()
- 位置: L170-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pinnedTabsContainerEl?.shadowRoot?.querySelector()`

## SidebarState.#toolsContainer()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller.sidebarMain?.buttonsWrapper`

## SidebarState.#toolsButtonGroup()
- 位置: L190-192
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller.sidebarMain?.buttonGroup`

## SidebarState.#controllerGlobal()
- 位置: L197-199
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#launcherContainerEl.documentGlobal`

## SidebarState.initializeState()
- 位置: L205-219
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.verticalTabsEnabled`, `this.#controllerGlobal.toolbar.visible`, `this.#props.launcherExpanded`, `this.defaultLauncherVisible`, `this.launcherExpanded`, `this.launcherVisible`

## SidebarState.loadCurrentState()
- 位置: L228-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `props.hasOwnProperty()`, `this.#controller.hide()`
- 条件付き依存: `if (this.command && this.panelOpen)` → `this.#controller.showInitially()`
- 参照: `props.hidden`, `props.launcherVisible`, `props.panelOpen`, `this.#controller.SidebarManager.hasSidebarLauncherBeenVisible`, `this.#panelEl.style.width`, `this.#props`, `this.command`, `this.defaultLauncherVisible`, `this.launcherExpanded`, `this.launcherHiddenWithPanel`, `this.launcherVisible`, `this.panelOpen`, `this.revampVisibility`

## SidebarState.toggle()
- 位置: L330-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`
- 参照: `this.#props`

## SidebarState.getProperties()
- 位置: L341-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `convertToInt()`
- 参照: `this.bookmarksExpandedFolders`, `this.collapsedPinnedTabsHeight`, `this.collapsedToolsHeight`, `this.command`, `this.expandedLauncherWidth`, `this.expandedPinnedTabsHeight`, `this.expandedToolsHeight`, `this.launcherExpanded`, `this.launcherVisible`, `this.launcherWidth`, `this.panelOpen`, `this.panelWidth`, `this.pinnedTabsHeight`, `this.toolsHeight`

## SidebarState.panelOpen()
- 位置: L367-369
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.panelOpen`

## SidebarState.panelOpen()
- 位置: L371-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `boxEl.toggleAttribute()`, `contentAreaEl.toggleAttribute()`, `this.#controller.requestMaxWidthUpdate()`, `this.#controllerGlobal.document.getElementById()`
- 条件付き依存: `if (open)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (mainEl?.toggleAttribute)` → `mainEl.toggleAttribute()`
- 参照: `mainEl?.toggleAttribute`, `this.#controller._box`, `this.#controller.sidebarContainer`, `this.#props.panelOpen`, `this.launcherHiddenWithPanel`, `this.launcherVisible`, `this.revampEnabled`
- XPCOM: `Services.prefs`

## SidebarState.panelWidth()
- 位置: L401-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `convertToInt()`
- 参照: `this.#panelEl?.style.width`

## SidebarState.panelWidth()
- 位置: L407-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.requestMaxWidthUpdate()`

## SidebarState.expandedPinnedTabsHeight()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.expandedPinnedTabsHeight`

## SidebarState.expandedPinnedTabsHeight()
- 位置: L415-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePinnedTabsHeight()`
- 参照: `this.#props.expandedPinnedTabsHeight`

## SidebarState.collapsedPinnedTabsHeight()
- 位置: L420-422
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.collapsedPinnedTabsHeight`

## SidebarState.collapsedPinnedTabsHeight()
- 位置: L424-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePinnedTabsHeight()`
- 参照: `this.#props.collapsedPinnedTabsHeight`

## SidebarState.expandedToolsHeight()
- 位置: L429-431
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.expandedToolsHeight`

## SidebarState.expandedToolsHeight()
- 位置: L433-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateToolsHeight()`
- 参照: `this.#props.expandedToolsHeight`

## SidebarState.collapsedToolsHeight()
- 位置: L438-440
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.collapsedToolsHeight`

## SidebarState.collapsedToolsHeight()
- 位置: L442-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateToolsHeight()`
- 参照: `this.#props.collapsedToolsHeight`

## SidebarState.defaultLauncherVisible()
- 位置: L447-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["hide-sidebar", "hide-launcher"].includes()`
- 参照: `lazy.verticalTabsEnabled`, `this.revampEnabled`, `this.revampVisibility`

## SidebarState.launcherHiddenWithPanel()
- 位置: L474-476
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.revampVisibility`

## SidebarState.launcherVisible()
- 位置: L478-480
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.launcherVisible`

## SidebarState.launcherEverVisible()
- 位置: L482-484
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#launcherEverVisible`

## SidebarState.updateVisibility()
- 位置: L493-524
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.defaultLauncherVisible`, `this.launcherExpanded`, `this.launcherVisible`, `this.revampVisibility`

## SidebarState.launcherVisible()
- 位置: L526-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#launcherEl.requestUpdate()`, `this.#updateTabbrowser()`
- 条件付き依存: `if (!this.revampEnabled)` → `this.#controller._disableLauncherDragging()`
- 条件付き依存: `if (!this.revampEnabled)` → `this.#updateTabbrowser()`
- 条件付き依存: `if (visible)` → `this.#controller._enableLauncherDragging()`
- 条件付き依存: `if (!(visible))` → `this.#controller._disableLauncherDragging()`
- 参照: `this.#launcherContainerEl.hidden`, `this.#launcherEverVisible`, `this.#launcherSplitterEl.hidden`, `this.#props.launcherVisible`, `this.#sidebarBoxEl.style.paddingInlineStart`, `this.panelOpen`, `this.revampEnabled`

## SidebarState.launcherExpanded()
- 位置: L551-553
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.launcherExpanded`

## SidebarState.launcherExpanded()
- 位置: L555-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `boxEl?.toggleAttribute()`, `contentAreaEl.toggleAttribute()`, `tabContainer.toggleAttribute()`, `this.#controller.updateToolbarButton()`, `this.#controllerGlobal.document.getElementById()`, `this.#launcherSplitterEl?.toggleAttribute()`, `this.handleUpdateToolsHeightOnLauncherExpanded()`
- 条件付き依存: `if (expanded && !previousExpanded)` → `Glean.sidebar.expand.record()`
- 条件付き依存: `if (mainEl?.toggleAttribute)` → `mainEl.toggleAttribute()`
- 条件付き依存: `if (!this.launcherDragActive)` → `this.#updateLauncherWidth()`
- 条件付き依存: `if ( !this.pinnedTabsDragActive && this.#controller.sidebarRevampVisibility !== "expand-on-hover" )` → `this.updatePinnedTabsHeight()`
- 参照: `mainEl?.toggleAttribute`, `this.#controller._box`, `this.#controller.sidebarContainer`, `this.#controller.sidebarRevampVisibility`, `this.#controllerGlobal.gBrowser`, `this.#launcherEl.expanded`, `this.#props.launcherExpanded`, `this.launcherDragActive`, `this.pinnedTabsDragActive`, `this.revampEnabled`

## SidebarState.launcherDragActive()
- 位置: L597-599
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.launcherDragActive`

## SidebarState.launcherDragActive()
- 位置: L601-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rootEl.toggleAttribute()`
- 条件付き依存: `if (this.#controller.sidebarRevampVisibility === "expand-on-hover")` → `this.#controller.toggleExpandOnHover()`
- 条件付き依存: `if (active)` → `this.#launcherEl.toggleAttribute()`
- 条件付き依存: `if (!(active))` → `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing()`
- 参照: `this.#controller.sidebarRevampVisibility`, `this.#controllerGlobal.document.documentElement`, `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing( this.#launcherContainerEl ).width`, `this.#launcherContainerEl`, `this.#props.launcherDragActive`, `this.expandedLauncherWidth`, `this.launcherExpanded`, `this.launcherVisible`, `this.launcherWidth`, `this.revampVisibility`

## SidebarState.pinnedTabsDragActive()
- 位置: L637-639
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.pinnedTabsDragActive`

## SidebarState.pinnedTabsDragActive()
- 位置: L641-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!active)` → `Math.min()`
- 参照: `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing( this.#pinnedTabsContainerEl ).height`, `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing( this.#pinnedTabsItemsWrapper ).height`, `this.#pinnedTabsContainerEl`, `this.#pinnedTabsItemsWrapper`, `this.#props.launcherExpanded`, `this.#props.pinnedTabsDragActive`, `this.collapsedPinnedTabsHeight`, `this.expandedPinnedTabsHeight`, `this.pinnedTabsHeight`

## SidebarState.toolsDragActive()
- 位置: L666-668
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.toolsDragActive`

## SidebarState.toolsDragActive()
- 位置: L670-693
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!active && this.#toolsContainer)` → `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing()`
- 参照: `this.#controller.sidebarRevampVisibility`, `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing( this.#toolsContainer ).height`, `this.#launcherEl.shouldShowOverflowButton`, `this.#props.launcherExpanded`, `this.#props.toolsDragActive`, `this.#toolsContainer`, `this.collapsedToolsHeight`, `this.expandedToolsHeight`, `this.maxToolsHeight`, `this.toolsHeight`

## SidebarState.maxToolsHeight()
- 位置: L695-719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing()`
- 参照: `this.#props.launcherExpanded`, `this.#toolsButtonGroup`, `this.#toolsButtonGroup.children`, `this.#toolsButtonGroup.children.length`, `toolRect.height`

## SidebarState.launcherHoverActive()
- 位置: L721-723
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.launcherHoverActive`

## SidebarState.launcherHoverActive()
- 位置: L725-727
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.launcherHoverActive`

## SidebarState.launcherWidth()
- 位置: L729-731
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.launcherWidth`

## SidebarState.launcherWidth()
- 位置: L733-743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`
- 条件付き依存: `if (!document.documentElement.hasAttribute("inDOMFullscreen"))` → `this.#controller.requestMaxWidthUpdate()`
- 参照: `this.#controllerGlobal`, `this.#props.launcherWidth`, `this.launcherDragActive`, `this.launcherExpanded`

## SidebarState.expandedLauncherWidth()
- 位置: L745-747
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.expandedLauncherWidth`

## SidebarState.expandedLauncherWidth()
- 位置: L749-752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateLauncherWidth()`
- 参照: `this.#props.expandedLauncherWidth`

## SidebarState.#updateLauncherWidth()
- 位置: L758-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#launcherEl.toggleAttribute()`
- 参照: `this.#launcherContainerEl.style.width`, `this.expandedLauncherWidth`, `this.launcherExpanded`

## SidebarState.pinnedTabsHeight()
- 位置: L770-772
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.pinnedTabsHeight`

## SidebarState.pinnedTabsHeight()
- 位置: L774-781
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.verticalTabsEnabled`, `this.#props.pinnedTabsHeight`, `this.collapsedPinnedTabsHeight`, `this.expandedPinnedTabsHeight`, `this.launcherExpanded`

## SidebarState.toolsHeight()
- 位置: L783-785
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.toolsHeight`

## SidebarState.toolsHeight()
- 位置: L787-794
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.toolsHeight`, `this.collapsedToolsHeight`, `this.expandedToolsHeight`, `this.launcherExpanded`

## SidebarState.updatePinnedTabsHeight()
- 位置: L800-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing()`
- 参照: `lazy.verticalTabsEnabled`, `this.#controllerGlobal.windowUtils.getBoundsWithoutFlushing( itemsWrapper ).height`, `this.#pinnedTabsContainerEl`, `this.#pinnedTabsContainerEl.style.height`, `this.#pinnedTabsItemsWrapper`, `this.collapsedPinnedTabsHeight`, `this.expandedPinnedTabsHeight`, `this.launcherExpanded`, `this.pinnedTabsDragActive`

## SidebarState.handleUpdateToolsHeightOnLauncherExpanded()
- 位置: L838-848
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#controller.sidebarRevampVisibility !== "expand-on-hover")` → `this.updateToolsHeight()`
- 参照: `this.#controller.sidebarRevampVisibility`, `this.#props.launcherExpanded`, `this.#toolsContainer`, `this.#toolsContainer.style.height`, `this.toolsDragActive`

## SidebarState.updateToolsHeight()
- 位置: L853-879
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.verticalTabsEnabled`, `this.#props.collapsedToolsHeight`, `this.#props.expandedToolsHeight`, `this.#toolsContainer`, `this.#toolsContainer.style.height`, `this.launcherExpanded`

## SidebarState.#updateTabbrowser()
- 位置: L881-891
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `tabbox.toggleAttribute()`
- 参照: `doc.documentElement`, `this.#controllerGlobal.document`, `this.#navToolboxCollapsed`

## SidebarState.navToolboxCollapsed()
- 位置: L893-895
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#navToolboxCollapsed`

## SidebarState.navToolboxCollapsed()
- 位置: L897-903
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateTabbrowser()`
- 参照: `this.#navToolboxCollapsed`, `this.launcherVisible`

## SidebarState.command()
- 位置: L905-907
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#props.command`

## SidebarState.command()
- 位置: L909-921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.sidebars.has()`
- 条件付き依存: `if (id && id !== this.#props.command)` → `this.#controller._box.setAttribute()`
- 条件付き依存: `if (!id)` → `this.#controller._box.setAttribute()`
- 参照: `this.#props.command`

## convertToInt()
- 位置: L932-938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNaN()`, `parseInt()`
