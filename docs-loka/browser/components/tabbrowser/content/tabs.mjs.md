# browser/components/tabbrowser/content/tabs.mjs

source: browser/components/tabbrowser/content/tabs.mjs
source-hash: d8775258e178fdeb17964996a86e7cefbb991b33
lines: 1792

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## MozTabbrowserTabs.constructor()
- 位置: L18-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.addEventListener()`

## MozTabbrowserTabs.init()
- 位置: L57-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `DynamicShortcutTooltip.getText()`, `Math.max()`, `Object.defineProperty()`, `Services.prefs.addObserver()`, `Services.prefs.getIntPref()`, `Services.startup.getStartupInfo()`, `Services.startup.getStartupInfo().start.getTime()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `document .getElementById()`, `document .getElementById("tabs-newtab-button") .addEventListener()`, `document .getElementById("vertical-tabs-newtab-button") .addEventListener()`, `document.getElementById()`, `this.#updateTabMinWidth()`, `this._fullscreenMutationObserver.observe()`, `this._updateNewTabVisibility()`, `this.arrowScrollbox.addEventListener()`, `this.baseConnect()`, `this.getAttribute()`, `this.newTabButton.setAttribute()`, `this.observe()`, `this.pinnedTabsContainer.setAttribute()`, `this.querySelector()`, `this.tabDragAndDrop.init()`, `this.updateWheelListeners()`, `window.addEventListener()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `this.tabbox.tabpanels.setAttribute()`
- XPCOM: `Services.prefs` / `Services.startup`

## this.arrowScrollbox._getScrollableElements()
- 位置: L71-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ariaFocusableItems.reduce()`, `this.arrowScrollbox._canScrollToElement()`
- 条件付き依存: `if (this.arrowScrollbox._canScrollToElement(item))` → `elements.push()`
- 条件付き依存: `if (this.arrowScrollbox._canScrollToElement(item))` → `isTab()`
- 条件付き依存: `if ( isTab(item) && item.group && item.group.collapsed && item.selected )` → `elements.push()`

## this.arrowScrollbox._canScrollToElement()
- 位置: L88-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isTab()`

## get()
- 位置: L104-104
- 役割: (未記入)
- 触るとき: (未記入)

## handleResize()
- 位置: L128-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleTabSelect()`, `this._updateCloseButtons()`

## this.boundObserve()
- 位置: L139-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observe()`

## MozTabbrowserTabs.attributeChangedCallback()
- 位置: L213-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.attributeChangedCallback()`
- 条件付き依存: `if (attrName == "orient")` → `this.removeAttribute()`
- 条件付き依存: `if (attrName == "orient")` → `this.#updateTabMinWidth()`
- 条件付き依存: `if (attrName == "orient")` → `this.pinnedTabsContainer?.setAttribute()`

## MozTabbrowserTabs.handleEvent()
- 位置: L225-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.#isMovingTab()`, `this.previewPanel?.deactivate()`
- 条件付き依存: `if ( document.getElementById("tabContextMenu").state != "open" && !this.#isMovingTab() )` → `this._unlockTabSizing()`
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`

## MozTabbrowserTabs.on_TabSelect()
- 位置: L261-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleTabSelect()`
- 条件付き依存: `if (previousTab.group?.collapsed || newTab.group?.collapsed)` → `this._invalidateCachedVisibleTabs()`

## MozTabbrowserTabs.on_TabClose()
- 位置: L275-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hiddenSoundPlayingStatusChanged()`

## MozTabbrowserTabs.on_TabAttrModified()
- 位置: L279-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.detail.changed.includes()`
- 条件付き依存: `if ( event.detail.changed.includes("soundplaying") && !event.target.visible )` → `this._hiddenSoundPlayingStatusChanged()`
- 条件付き依存: `if ( event.detail.changed.includes("soundplaying") || event.detail.changed.includes("muted") || event.detail.changed.includes("activemedia-blocked") )` → `this.updateTabSoundLabel()`

## MozTabbrowserTabs.on_TabHide()
- 位置: L295-299
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target.soundPlaying)` → `this._hiddenSoundPlayingStatusChanged()`

## MozTabbrowserTabs.on_TabShow()
- 位置: L301-305
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target.soundPlaying)` → `this._hiddenSoundPlayingStatusChanged()`

## MozTabbrowserTabs.on_TabHoverStart()
- 位置: L307-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureTabPreviewPanelLoaded()`, `this.previewPanel.activate()`

## MozTabbrowserTabs.on_TabHoverEnd()
- 位置: L315-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previewPanel?.deactivate()`

## MozTabbrowserTabs.on_TabNoteIconHoverStart()
- 位置: L319-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureTabPreviewPanelLoaded()`, `this.previewPanel.activateNotePanel()`

## MozTabbrowserTabs.on_TabNoteIconHoverEnd()
- 位置: L330-335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previewPanel?.deactivateNotePanel()`
- 条件付き依存: `if (event.detail.returningToTab)` → `this.previewPanel?.activate()`

## MozTabbrowserTabs.cancelTabGroupPreview()
- 位置: L337-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previewPanel?.panelOpener.clear()`

## MozTabbrowserTabs.showTabGroupPreview()
- 位置: L341-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureTabPreviewPanelLoaded()`, `this.previewPanel.activate()`

## MozTabbrowserTabs.on_TabGroupLabelHoverStart()
- 位置: L349-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showTabGroupPreview()`

## MozTabbrowserTabs.on_TabGroupLabelHoverEnd()
- 位置: L353-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previewPanel?.deactivate()`

## MozTabbrowserTabs.on_TabGroupExpand()
- 位置: L357-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#animatingGroups.add()`, `this._invalidateCachedVisibleTabs()`

## MozTabbrowserTabs.on_TabGroupCollapse()
- 位置: L362-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#animatingGroups.add()`, `this._invalidateCachedVisibleTabs()`, `this._unlockTabSizing()`

## MozTabbrowserTabs.on_TabGroupAnimationComplete()
- 位置: L368-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#animatingGroups.delete()`, `window.requestAnimationFrame()`

## MozTabbrowserTabs.on_TabGroupCreate()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_TabGroupRemoved()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_SplitViewCreated()
- 位置: L384-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_SplitViewRemoved()
- 位置: L388-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_transitionend()
- 位置: L395-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target?.closest()`, `tab.dispatchEvent()`, `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("fadein"))` → `this.openAnimationFinished()`
- 条件付き依存: `if (this.openAnimationFinished(tab))` → `this._updateCloseButtons()`
- 条件付き依存: `if (!(this.openAnimationFinished(tab)))` → `this._handleNewTab()`
- 条件付き依存: `if (tab.closing)` → `gBrowser._endRemoveTab()`

## MozTabbrowserTabs.on_dblclick()
- 位置: L420-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`
- 条件付き依存: `if (!this._blockDblClick)` → `BrowserCommands.openTab()`

## MozTabbrowserTabs.on_click()
- 位置: L445-550
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.eventPhase == Event.CAPTURING_PHASE && event.button == 0)` → `target.classList.contains()`
- 条件付き依存: `if (event.detail > 1 && !target._ignoredCloseButtonClicks)` → `event.stopPropagation()`
- 条件付き依存: `if (event.eventPhase == Event.BUBBLING_PHASE && event.button == 1)` → `event.target?.closest()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(tab.multiselected))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(tab.multiselected))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(tab))` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(event.target))` → `event.target.group.saveAndClose()`
- 条件付き依存: `if (!(isTabGroupLabel(event.target)))` → `event.originalTarget.closest()`
- 条件付き依存: `if (!(isTabGroupLabel(event.target)))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( event.originalTarget.closest("scrollbox") && !Services.prefs.getBoolPref( "widget.gtk.titlebar-action-middle-click-enabled" ) )` → `visibleTabs.at()`
- 条件付き依存: `if ( event.originalTarget.closest("scrollbox") && !Services.prefs.getBoolPref( "widget.gtk.titlebar-action-middle-click-enabled" ) )` → `winUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if ( (this.verticalMode && event.clientY > endOfTab) || (!this.verticalMode && (this.#rtlMode ? event.clientX < endOfTab : event.clientX > endOfTab)) )` → `BrowserCommands.openTab()`
- 条件付き依存: `if (event.eventPhase == Event.BUBBLING_PHASE && event.button == 1)` → `event.preventDefault()`
- 条件付き依存: `if (event.eventPhase == Event.BUBBLING_PHASE && event.button == 1)` → `event.stopPropagation()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs.on_keydown()
- 位置: L552-665
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (keyComboForFocusedElement)` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(ariaFocusedItem))` → `ariaFocusedItem.click()`
- 条件付き依存: `if (isTabGroupLabel(ariaFocusedItem))` → `event.preventDefault()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabBackward()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabForward()`
- 条件付き依存: `if (RTL_UI)` → `gBrowser.moveTabBackward()`
- 条件付き依存: `if (!(RTL_UI))` → `gBrowser.moveTabForward()`
- 条件付き依存: `if (RTL_UI)` → `gBrowser.moveTabForward()`
- 条件付き依存: `if (!(RTL_UI))` → `gBrowser.moveTabBackward()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabToStart()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabToEnd()`
- 条件付き依存: `if (keyComboForMove)` → `event.preventDefault()`
- 条件付き依存: `if (keyComboForFocus)` → `this.#advanceFocus()`
- 条件付き依存: `if (RTL_UI)` → `this.#advanceFocus()`
- 条件付き依存: `if (!(RTL_UI))` → `this.#advanceFocus()`
- 条件付き依存: `if (keyComboForFocus)` → `this.ariaFocusableItems.at()`
- 条件付き依存: `if (keyComboForFocus)` → `isTab()`
- 条件付き依存: `if (ariaFocusedItem.multiselected)` → `gBrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (!(ariaFocusedItem.multiselected))` → `gBrowser.addToMultiSelectedTabs()`
- 条件付き依存: `if (keyComboForFocus)` → `event.preventDefault()`

## MozTabbrowserTabs.on_focusin()
- 位置: L670-691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.relatedTarget?.classList.contains()`, `isTabGroupLabel()`
- 条件付き依存: `if ( !focusReturnedFromGroupPanel && this.tablistHasFocus && isTabGroupLabel(this.ariaFocusedItem) )` → `this.showTabGroupPreview()`

## MozTabbrowserTabs.on_focusout()
- 位置: L696-701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancelTabGroupPreview()`

## MozTabbrowserTabs.on_keypress()
- 位置: L703-711
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key == " " || event.key == "Enter")` → `event.preventDefault()`
- 条件付き依存: `if (event.key == " " || event.key == "Enter")` → `event.target.click()`

## MozTabbrowserTabs.on_dragstart()
- 位置: L713-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabDragAndDrop.handle_dragstart()`

## MozTabbrowserTabs.on_dragover()
- 位置: L717-719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabDragAndDrop.handle_dragover()`

## MozTabbrowserTabs.on_drop()
- 位置: L721-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabDragAndDrop.handle_drop()`

## MozTabbrowserTabs.on_dragend()
- 位置: L725-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabDragAndDrop.handle_dragend()`

## MozTabbrowserTabs.on_dragleave()
- 位置: L729-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabDragAndDrop.handle_dragleave()`

## MozTabbrowserTabs.on_wheel()
- 位置: L737-741
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopImmediatePropagation()`

## MozTabbrowserTabs.updateWheelListeners()
- 位置: L743-755
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updateWheelListeners()`
- 条件付き依存: `if (this.switchByScrolling)` → `this.arrowScrollbox.addEventListener()`
- 条件付き依存: `if (!(this.switchByScrolling))` → `this.arrowScrollbox.removeEventListener()`

## MozTabbrowserTabs.on_overflow()
- 位置: L757-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("tab-preview-panel") ?.setAttribute()`, `this._updateCloseButtons()`, `this.toggleAttribute()`
- 条件付き依存: `if (!this.#animatingGroups.size)` → `this._handleTabSelect()`

## MozTabbrowserTabs.on_underflow()
- 位置: L775-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("tab-preview-panel") ?.removeAttribute()`, `gBrowser.removeTab()`, `this._updateCloseButtons()`, `this.removeAttribute()`
- 条件付き依存: `if (this._lastTabClosedByMouse)` → `this._expandSpacerBy()`

## MozTabbrowserTabs.on_contextmenu()
- 位置: L800-809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isTabGroupLabel()`
- 条件付き依存: `if (event.button == 0 && isTabGroupLabel(this.ariaFocusedItem))` → `gBrowser.tabGroupMenu.openEditModal()`
- 条件付き依存: `if (event.button == 0 && isTabGroupLabel(this.ariaFocusedItem))` → `event.preventDefault()`

## MozTabbrowserTabs.on_uidensitychanged()
- 位置: L811-814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleTabSelect()`, `this._updateCloseButtons()`

## MozTabbrowserTabs.emptyTabTitle()
- 位置: L818-826
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `gBrowser.tabLocalization.formatValueSync()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs.tabbox()
- 位置: L828-830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## MozTabbrowserTabs.newTabButton()
- 位置: L832-834
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTabs.verticalMode()
- 位置: L836-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## MozTabbrowserTabs.expandOnHover()
- 位置: L840-842
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabs.#rtlMode()
- 位置: L844-846
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabs.overflowing()
- 位置: L848-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.allTabs()
- 位置: L853-880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `pinnedChildren?.at()`, `unpinnedChildren.pop()`
- 条件付き依存: `if (pinnedChildren?.at(-1)?.id == "pinned-tabs-container-periphery")` → `pinnedChildren.pop()`
- 条件付き依存: `if ( unpinnedChildren[i].tagName == "tab-group" || unpinnedChildren[i].tagName == "tab-split-view-wrapper" )` → `unpinnedChildren.splice()`

## MozTabbrowserTabs.allGroups()
- 位置: L882-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `children.filter()`

## MozTabbrowserTabs.allSplitViews()
- 位置: L889-904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`
- 条件付き依存: `if (node.tagName == "tab-split-view-wrapper")` → `splitViews.push()`
- 条件付き依存: `if (node.tagName == "tab-group")` → `splitViews.push()`
- 条件付き依存: `if (node.tagName == "tab-group")` → `Array.from(node.children).filter()`
- 条件付き依存: `if (node.tagName == "tab-group")` → `Array.from()`

## MozTabbrowserTabs.openTabs()
- 位置: L910-915
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#openTabs)` → `this.allTabs.filter()`

## MozTabbrowserTabs.nonHiddenTabs()
- 位置: L921-926
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#nonHiddenTabs)` → `this.openTabs.filter()`

## MozTabbrowserTabs.visibleTabs()
- 位置: L932-937
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#visibleTabs)` → `this.openTabs.filter()`

## MozTabbrowserTabs.tablistHasFocus()
- 位置: L943-945
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.tablistHasFocus()
- 位置: L950-952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTabs.ariaFocusableItems()
- 位置: L970-1001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `isTab()`
- 条件付き依存: `if (isTab(child))` → `focusableItems.push()`
- 条件付き依存: `if (isTab(child) && child.visible)` → `focusableItems.push()`
- 条件付き依存: `if (!(isTab(child) && child.visible))` → `isTabGroup()`
- 条件付き依存: `if (isTabGroup(child))` → `focusableItems.push()`
- 条件付き依存: `if (isTabGroup(child))` → `child.tabs.filter()`
- 条件付き依存: `if (child.tagName == "tab-split-view-wrapper")` → `child.tabs.filter()`
- 条件付き依存: `if (child.tagName == "tab-split-view-wrapper")` → `focusableItems.push()`

## MozTabbrowserTabs.dragAndDropElements()
- 位置: L1010-1051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `isSplitViewWrapper()`, `isTab()`, `isTabGroup()`
- 条件付き依存: `if (isTabGroup(child))` → `dragAndDropElements.push()`
- 条件付き依存: `if (isTabGroup(child))` → `child.tabsAndSplitViews.filter()`
- 条件付き依存: `if (isTabGroup(child))` → `tabsAndSplitViews.forEach()`
- 条件付き依存: `if (!(isTabGroup(child)))` → `dragAndDropElements.push()`

## MozTabbrowserTabs.#advanceFocus()
- 位置: L1059-1077
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `isTabGroupLabel()`, `this.ariaFocusableItems.indexOf()`
- 条件付き依存: `if (isTabGroupLabel(this.ariaFocusedItem))` → `this.showTabGroupPreview()`

## MozTabbrowserTabs._invalidateCachedTabs()
- 位置: L1079-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._invalidateCachedVisibleTabs()`

## MozTabbrowserTabs._invalidateCachedVisibleTabs()
- 位置: L1084-1093
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabs.#isMovingTab()
- 位置: L1095-1097
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.isContainerVerticalPinnedGrid()
- 位置: L1099-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.advanceSelectedTab()
- 位置: L1114-1125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.advanceSelectedTab()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.sourceForEvent()`

## MozTabbrowserTabs.advanceSelectedItem()
- 位置: L1138-1201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ariaFocusableItems.indexOf()`, `isTab()`, `isTabGroupLabel()`, `this.cancelTabGroupPreview()`
- 条件付き依存: `if (groupPanel && groupPanel.isActive)` → `groupPanel.focusPanel()`
- 条件付き依存: `if (!(aWrap))` → `Math.min()`
- 条件付き依存: `if (!(aWrap))` → `Math.max()`
- 条件付き依存: `if (isTab(newItem))` → `this._selectNewTab()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (isTabGroupLabel(this.ariaFocusedItem))` → `this.showTabGroupPreview()`

## MozTabbrowserTabs.ensureTabPreviewPanelLoaded()
- 位置: L1203-1210
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.previewPanel)` → `ChromeUtils.importESModule()`

## MozTabbrowserTabs.appendChild()
- 位置: L1212-1214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.insertBefore()`

## MozTabbrowserTabs.insertBefore()
- 位置: L1216-1227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.before()`

## MozTabbrowserTabs.#updateTabMinWidth()
- 位置: L1229-1234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.style.setProperty()`

## MozTabbrowserTabs._isCustomizing()
- 位置: L1236-1238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`

## MozTabbrowserTabs._selectNewTab()
- 位置: L1243-1247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSharedTabWarning.willShowSharedTabWarning()`
- 条件付き依存: `if (!gSharedTabWarning.willShowSharedTabWarning(aNewTab))` → `super._selectNewTab()`

## MozTabbrowserTabs.observe()
- 位置: L1249-1320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DynamicShortcutTooltip.cache.delete()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `button.removeAttribute()`, `document.getElementById()`
- 条件付き依存: `if (button.menupopup)` → `button.menupopup.remove()`
- 条件付き依存: `if (containersEnabled)` → `button.setAttribute()`
- 条件付き依存: `if (containersEnabled)` → `document .getElementById("new-tab-button-popup") .cloneNode()`
- 条件付き依存: `if (containersEnabled)` → `document .getElementById()`
- 条件付き依存: `if (containersEnabled)` → `popup.removeAttribute()`
- 条件付き依存: `if (containersEnabled)` → `popup.setAttribute()`
- 条件付き依存: `if (containersEnabled)` → `popup.addEventListener()`
- 条件付き依存: `if (containersEnabled)` → `button.prepend()`
- 条件付き依存: `if (!(containersEnabled))` → `button.removeAttribute()`
- 条件付き依存: `if (containersEnabled && !newTabLeftClickOpensContainersMenu)` → `gClickAndHoldListenersOnElement.add()`
- 条件付き依存: `if (!(containersEnabled && !newTabLeftClickOpensContainersMenu))` → `gClickAndHoldListenersOnElement.remove()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs._updateCloseButtons()
- 位置: L1322-1365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rect()`, `this.visibleTabs .slice()`, `this.visibleTabs .slice(gBrowser.pinnedTabCount) .find()`, `window.requestAnimationFrame()`
- 条件付き依存: `if (this.overflowing)` → `this.setAttribute()`
- 条件付き依存: `if (tab && rect(tab).width <= this._tabClipWidth)` → `this.setAttribute()`
- 条件付き依存: `if (!(tab && rect(tab).width <= this._tabClipWidth))` → `this.removeAttribute()`

## rect()
- 位置: L1350-1352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## MozTabbrowserTabs._handleTabSelect()
- 位置: L1370-1375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureTabIsVisible()`

## MozTabbrowserTabs.#ensureTabIsVisible()
- 位置: L1381-1386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.closest()`
- 条件付き依存: `if (arrowScrollbox?.overflowing)` → `arrowScrollbox.ensureElementIsVisible()`

## MozTabbrowserTabs._lockTabSizing()
- 位置: L1391-1477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.at()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!this._tabDefaultMaxWidth)` → `parseFloat()`
- 条件付き依存: `if (!this._tabDefaultMaxWidth)` → `window.getComputedStyle()`
- 条件付き依存: `if (aTabWidth === undefined)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this.overflowing)` → `this.arrowScrollbox.hasAttribute()`
- 条件付き依存: `if (this.overflowing)` → `this._expandSpacerBy()`
- 条件付き依存: `if (!(this.overflowing))` → `tab.style.setProperty()`
- 条件付き依存: `if (!isEndTab)` → `tabsToReset.push()`
- 条件付き依存: `if (tabsToReset.length)` → `window .promiseDocumentFlushed(() => {}) .then()`
- 条件付き依存: `if (tabsToReset.length)` → `window .promiseDocumentFlushed()`
- 条件付き依存: `if (tabsToReset.length)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (!(this.overflowing))` → `gBrowser.addEventListener()`
- 条件付き依存: `if (!(this.overflowing))` → `window.addEventListener()`

## MozTabbrowserTabs._expandSpacerBy()
- 位置: L1479-1485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.addEventListener()`, `parseFloat()`, `this.toggleAttribute()`, `window.addEventListener()`

## MozTabbrowserTabs._unlockTabSizing()
- 位置: L1487-1506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.removeEventListener()`, `this.hasAttribute()`, `window.removeEventListener()`
- 条件付き依存: `if (this.hasAttribute("using-closing-tabs-spacer"))` → `this.removeAttribute()`

## MozTabbrowserTabs._notifyBackgroundTab()
- 位置: L1508-1601
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._backgroundTabScrollPromise)` → `window .promiseDocumentFlushed()`
- 条件付き依存: `if (!this._backgroundTabScrollPromise)` → `this._lastTabToScrollIntoView.getBoundingClientRect()`
- 条件付き依存: `if (!(selectedTab.pinned))` → `selectedTab.getBoundingClientRect()`
- 条件付き依存: `if (this._lastTabToScrollIntoView != tabToScrollIntoView)` → `this._notifyBackgroundTab()`
- 条件付き依存: `if (this.arrowScrollbox.smoothScroll)` → `Math.max()`
- 条件付き依存: `if ( !selectedRect || (this.verticalMode ? Math.max( tabRect.bottom - selectedRect.top, selectedRect.bottom - tabRect.top ) <= scrollRect.height : Math.max( tabR...)` → `this.#ensureTabIsVisible()`
- 条件付き依存: `if (this.arrowScrollbox.smoothScroll)` → `this.arrowScrollbox.scrollByPixels()`
- 条件付き依存: `if (!this._backgroundTabScrollPromise)` → `this._animateElement.hasAttribute()`
- 条件付き依存: `if (!this._animateElement.hasAttribute("highlight"))` → `this._animateElement.toggleAttribute()`
- 条件付き依存: `if (!this._animateElement.hasAttribute("highlight"))` → `setTimeout()`
- 条件付き依存: `if (!this._animateElement.hasAttribute("highlight"))` → `ele.removeAttribute()`

## MozTabbrowserTabs.tabAnimationsInProgress()
- 位置: L1609-1611
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabs.openAnimationFinished()
- 位置: L1619-1621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openingTabs.has()`

## MozTabbrowserTabs.markTabOpening()
- 位置: L1628-1630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openingTabs.add()`

## MozTabbrowserTabs.cancelTabOpening()
- 位置: L1637-1639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openingTabs.delete()`

## MozTabbrowserTabs._handleNewTab()
- 位置: L1641-1665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UserInteraction.running()`, `tab.hasAttribute()`, `this.#openingTabs.delete()`, `this._updateCloseButtons()`
- 条件付き依存: `if (tab.hasAttribute("selected"))` → `this._handleTabSelect()`
- 条件付き依存: `if (!(tab.hasAttribute("selected")))` → `tab.hasAttribute()`
- 条件付き依存: `if (!tab.hasAttribute("skipbackgroundnotify"))` → `this._notifyBackgroundTab()`
- 条件付き依存: `if (tab.linkedPanel)` → `NewTabPagePreloading.maybeCreatePreloadedBrowser()`
- 条件付き依存: `if (UserInteraction.running("browser.tabs.opening", window))` → `UserInteraction.finish()`

## MozTabbrowserTabs._canAdvanceToTab()
- 位置: L1667-1669
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabs.getRelatedElement()
- 位置: L1676-1698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!aTab.linkedPanel)` → `gBrowser.insertBrowser()`

## MozTabbrowserTabs._updateNewTabVisibility()
- 位置: L1700-1724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`, `unwrap()`, `wrap()`

## wrap()
- 位置: L1702-1703
- 役割: (未記入)
- 触るとき: (未記入)

## unwrap()
- 位置: L1704-1705
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabs.onWidgetAfterDOMChange()
- 位置: L1726-1733
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aContainer.ownerDocument == document && aContainer.id == "TabsToolbar-customization-target" )` → `this._updateNewTabVisibility()`

## MozTabbrowserTabs.onAreaNodeRegistered()
- 位置: L1735-1739
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aContainer.ownerDocument == document && aArea == "TabsToolbar")` → `this._updateNewTabVisibility()`

## MozTabbrowserTabs.onAreaReset()
- 位置: L1741-1743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onAreaNodeRegistered()`

## MozTabbrowserTabs._hiddenSoundPlayingStatusChanged()
- 位置: L1745-1756
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!isClosed && tab.soundPlaying && !tab.visible)` → `this._hiddenSoundPlayingTabs.add()`
- 条件付き依存: `if (!isClosed && tab.soundPlaying && !tab.visible)` → `this.toggleAttribute()`
- 条件付き依存: `if (!(!isClosed && tab.soundPlaying && !tab.visible))` → `this._hiddenSoundPlayingTabs.delete()`
- 条件付き依存: `if (this._hiddenSoundPlayingTabs.size == 0)` → `this.removeAttribute()`

## MozTabbrowserTabs.destroy()
- 位置: L1758-1764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `this.previewPanel?.forceReset()`
- 条件付き依存: `if (this.boundObserve)` → `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs.updateTabSoundLabel()
- 位置: L1766-1786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabLocalization.formatMessagesSync()`
- 条件付き依存: `if (tab.audioButton)` → `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("muted") || tab.hasAttribute("soundplaying"))` → `tab.audioButton.setAttribute()`
- 条件付き依存: `if (!(tab.hasAttribute("muted") || tab.hasAttribute("soundplaying")))` → `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("activemedia-blocked"))` → `tab.audioButton.setAttribute()`
