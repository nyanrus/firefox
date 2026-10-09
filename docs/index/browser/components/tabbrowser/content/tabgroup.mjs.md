# browser/components/tabbrowser/content/tabgroup.mjs

source: browser/components/tabbrowser/content/tabgroup.mjs
source-hash: 98ebd520d6d3ee5e7519a3ad6ff46c1beaba185a
lines: 816

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## MozTabbrowserTabGroup.constructor()
- 位置: L75-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`

## MozTabbrowserTabGroup.inheritedAttributes()
- 位置: L86-90
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.connectedCallback()
- 位置: L92-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `e.preventDefault()`, `gBrowser.tabGroupMenu.openEditModal()`, `this.#labelContainerElement.addEventListener()`, `this.#labelElement.addEventListener()`, `this.#observeTabChanges()`, `this.#updateLabelAriaAttributes()`, `this.addEventListener()`, `this.appendChild()`, `this.dispatchEvent()`, `this.documentGlobal.addEventListener()`, `this.initializeAttributeInheritance()`, `this.overflowContainer.querySelector()`, `this.querySelector()`
- XPCOM: `Services.obs`

## MozTabbrowserTabGroup.resetDefaultGroupName()
- 位置: L163-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateLabelAriaAttributes()`, `this.#updateTooltip()`

## MozTabbrowserTabGroup.#removeObserver()
- 位置: L169-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## MozTabbrowserTabGroup.disconnectedCallback()
- 位置: L180-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeObserver()`, `this.#tabChangeObserver?.disconnect()`, `this.documentGlobal.removeEventListener()`, `this.removeEventListener()`

## MozTabbrowserTabGroup.appendChild()
- 位置: L188-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.insertBefore()`

## MozTabbrowserTabGroup.#observeTabChanges()
- 位置: L192-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabChangeObserver.observe()`
- 条件付き依存: `if (!this.tabs.length)` → `this.dispatchEvent()`
- 条件付き依存: `if (!this.tabs.length)` → `this.remove()`
- 条件付き依存: `if (!this.tabs.length)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(!this.tabs.length))` → `tabs.forEach()`
- 条件付き依存: `if (!(!this.tabs.length))` → `tab.setAttribute()`
- 条件付き依存: `if (!(!this.tabs.length))` → `this.#updateOverflowLabel()`
- 条件付き依存: `if (!(!this.tabs.length))` → `this.#updateLastTabOrSplitViewAttr()`
- 条件付き依存: `if (!this.#tabChangeObserver)` → `Tabbrowser.isTab()`
- 条件付き依存: `if (Tabbrowser.isTab(addedNode))` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (!(Tabbrowser.isTab(addedNode)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(addedNode))` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (Tabbrowser.isTab(removedNode))` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (!(Tabbrowser.isTab(removedNode)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(removedNode))` → `this.#updateTabAriaHidden()`
- XPCOM: `Services.obs`

## MozTabbrowserTabGroup.color()
- 位置: L250-252
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.color()
- 位置: L257-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.style.setProperty()`
- 条件付き依存: `if (diff)` → `this.dispatchEvent()`

## MozTabbrowserTabGroup.defaultGroupName()
- 位置: L290-297
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#defaultGroupName)` → `gBrowser.tabLocalization.formatValueSync()`

## MozTabbrowserTabGroup.id()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## MozTabbrowserTabGroup.id()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setAttribute()`

## MozTabbrowserTabGroup.hasActiveTab()
- 位置: L310-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.hasActiveTab()
- 位置: L317-319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTabGroup.label()
- 位置: L321-323
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.label()
- 位置: L325-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateLabelAriaAttributes()`, `this.#updateTooltip()`, `this.setAttribute()`
- 条件付き依存: `if (diff)` → `this.dispatchEvent()`

## MozTabbrowserTabGroup.name()
- 位置: L340-342
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.name()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.collapsed()
- 位置: L348-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.collapsed()
- 位置: L352-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `Promise.allSettled(pendingAnimationPromises).then()`, `["min-width", "max-width"].includes()`, `gBrowser.tabContainer.previewPanel?.deactivate()`, `tab .getAnimations()`, `tab .getAnimations() .filter()`, `tab .getAnimations() .filter(anim => ["min-width", "max-width"].includes(anim.transitionProperty) ) .map()`, `this.#updateLabelAriaAttributes()`, `this.#updateOverflowLabel()`, `this.#updateTabAriaHidden()`, `this.#updateTooltip()`, `this.dispatchEvent()`, `this.tabs.flatMap()`, `this.toggleAttribute()`

## MozTabbrowserTabGroup.lastSeenActive()
- 位置: L389-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.tabs.map()`

## MozTabbrowserTabGroup.#updateLabelAriaAttributes()
- 位置: async L393-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabLocalization.formatValue()`, `this.#labelElement?.setAttribute()`
- 条件付き依存: `if (this.collapsed)` → `this.#labelElement?.setAttribute()`
- 条件付き依存: `if (this.collapsed)` → `this.hasAttribute()`
- 条件付き依存: `if (!(this.collapsed))` → `this.#labelElement?.removeAttribute()`
- 条件付き依存: `if (!(this.collapsed))` → `this.#labelElement?.setAttribute()`

## MozTabbrowserTabGroup.#updateTooltip()
- 位置: async L420-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabLocalization .formatValue()`, `gBrowser.tabLocalization .formatValue(tooltipKey, { tabGroupName, }) .then()`

## MozTabbrowserTabGroup.#updateTabAriaHidden()
- 位置: L443-458
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tab.splitview)` → `tab.splitview.tabs.some()`
- 条件付き依存: `if ( tab.group?.collapsed && !tab.splitview.tabs.some(splitViewTab => splitViewTab.selected) )` → `tab.splitview.setAttribute()`
- 条件付き依存: `if (!( tab.group?.collapsed && !tab.splitview.tabs.some(splitViewTab => splitViewTab.selected) ))` → `tab.splitview.removeAttribute()`
- 条件付き依存: `if (tab.group?.collapsed && !tab.selected)` → `tab.setAttribute()`
- 条件付き依存: `if (!(tab.group?.collapsed && !tab.selected))` → `tab.removeAttribute()`

## MozTabbrowserTabGroup.#updateOverflowLabel()
- 位置: L460-489
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.overflowContainer)` → `this.overflowContainer.querySelector()`
- 条件付き依存: `if (this.overflowContainer)` → `this.toggleAttribute()`
- 条件付き依存: `if (this.overflowContainer)` → `gBrowser.tabLocalization .formatValue("tab-group-overflow-count", { tabCount: tabCount - overflowOffset, }) .then()`
- 条件付き依存: `if (this.overflowContainer)` → `gBrowser.tabLocalization .formatValue()`
- 条件付き依存: `if (this.overflowContainer)` → `overflowCountLabel.setAttribute()`

## MozTabbrowserTabGroup.#updateLastTabOrSplitViewAttr()
- 位置: L491-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`
- 条件付き依存: `if (prevLastTabOrSplitView !== currentLastTabOrSplitView)` → `prevLastTabOrSplitView?.removeAttribute()`
- 条件付き依存: `if (prevLastTabOrSplitView !== currentLastTabOrSplitView)` → `currentLastTabOrSplitView.setAttribute()`

## MozTabbrowserTabGroup.pinned()
- 位置: L511-513
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.splitview()
- 位置: L518-520
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.group()
- 位置: L525-527
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.tabs()
- 位置: L532-540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `childrenArray.filter()`, `node.matches()`
- 条件付き依存: `if (childrenArray[i].tagName == "tab-split-view-wrapper")` → `childrenArray.splice()`

## MozTabbrowserTabGroup.tabsAndSplitViews()
- 位置: L545-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.children).filter()`, `node.matches()`

## MozTabbrowserTabGroup.isTabVisibleInGroup()
- 位置: L555-568
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.labelElement()
- 位置: L573-575
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.labelContainerElement()
- 位置: L580-582
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.overflowCountLabel()
- 位置: L584-586
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.wasCreatedByAdoption()
- 位置: L591-593
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.removedByAdoption()
- 位置: L602-604
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroup.isBeingDragged()
- 位置: L609-611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.isBeingDragged()
- 位置: L616-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTabGroup.hoverPreviewPanelActive()
- 位置: L623-625
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.hoverPreviewPanelActive()
- 位置: L630-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateLabelAriaAttributes()`, `this.toggleAttribute()`

## MozTabbrowserTabGroup.addTabs()
- 位置: L642-685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `tabsOrSplitViews.reduce()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `gBrowser.TabMetrics.decomposedContext()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabOrSplitView))` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabOrSplitView))` → `gBrowser.tabs.at()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabOrSplitView))` → `gBrowser.moveSplitViewToExistingGroup()`
- 条件付き依存: `if (tabOrSplitView.pinned)` → `tabOrSplitView.documentGlobal.gBrowser.unpinTab()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabOrSplitView)))` → `gBrowser.adoptTab()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabOrSplitView)))` → `gBrowser.tabs.at()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabOrSplitView)))` → `gBrowser.moveTabToExistingGroup()`

## MozTabbrowserTabGroup.ungroupTabs()
- 位置: L693-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `this.dispatchEvent()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(this.tabsAndSplitViews[i]))` → `gBrowser.ungroupSplitView()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(this.tabsAndSplitViews[i])))` → `Tabbrowser.isTab()`
- 条件付き依存: `if (Tabbrowser.isTab(this.tabsAndSplitViews[i]))` → `gBrowser.ungroupTab()`

## MozTabbrowserTabGroup.save()
- 位置: L715-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.addSavedTabGroup()`, `this.dispatchEvent()`

## MozTabbrowserTabGroup.saveAndClose()
- 位置: L725-728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.removeTabGroup()`, `this.save()`

## MozTabbrowserTabGroup.on_click()
- 位置: L733-748
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isToggleElement && event.button === 0)` → `event.preventDefault()`
- 条件付き依存: `if (isToggleElement && event.button === 0)` → `gBrowser.tabGroupMenu.close()`
- 条件付き依存: `if (isToggleElement && event.button === 0)` → `interactionMetric.add()`

## MozTabbrowserTabGroup.on_mouseover()
- 位置: L753-761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#labelContainerElement.contains()`
- 条件付き依存: `if (!this.#labelContainerElement.contains(event.relatedTarget))` → `this.#labelElement.dispatchEvent()`

## MozTabbrowserTabGroup.on_mouseout()
- 位置: L766-774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#labelContainerElement.contains()`
- 条件付き依存: `if (!this.#labelContainerElement.contains(event.relatedTarget))` → `this.#labelElement.dispatchEvent()`

## MozTabbrowserTabGroup.on_TabSelect()
- 位置: L779-790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateOverflowLabel()`
- 条件付き依存: `if (this.hasActiveTab)` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (previousTab.group === this)` → `this.#updateTabAriaHidden()`

## MozTabbrowserTabGroup.on_SplitViewTabChange()
- 位置: L792-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateOverflowLabel()`, `this.#updateTabAriaHidden()`

## MozTabbrowserTabGroup.select()
- 位置: L805-812
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gBrowser.selectedTab.group == this)` → `gBrowser.tabContainer._handleTabSelect()`
