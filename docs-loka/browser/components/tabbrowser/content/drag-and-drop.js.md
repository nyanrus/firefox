# browser/components/tabbrowser/content/drag-and-drop.js

source: browser/components/tabbrowser/content/drag-and-drop.js
source-hash: 51542b55a2f4dcb6f0ab2c29b6c77c017284d48d
lines: 2970

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## elementToMove()
- 位置: L45-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSplitViewWrapper()`, `isTab()`, `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(element))` → `element.closest()`

## constructor()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L73-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._tabbrowserTabs.querySelector()`

## handle_dragstart()
- 位置: L87-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSplitViewWrapper()`, `this._getDragTarget()`, `this._tabbrowserTabs.previewPanel?.deactivate()`, `this.startTabDrag()`

## handle_dragover()
- 位置: L109-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `arrowScrollbox.getBoundingClientRect()`, `event.dataTransfer.mozGetDataAt()`, `event.preventDefault()`, `event.stopPropagation()`, `this.finishAnimateTabMove()`, `this.getDropEffectForTabDrag()`
- 条件付き依存: `if (pixelsToScroll)` → `arrowScrollbox.scrollByPixels()`
- 条件付き依存: `if ( (dropEffect == "move" || dropEffect == "copy") && document == draggedTab.ownerDocument && !draggedTab._dragData.fromTabList )` → `this.#isAnimatingMoveTogetherSelectedTabs()`
- 条件付き依存: `if ( (dropEffect == "move" || dropEffect == "copy") && document == draggedTab.ownerDocument && !draggedTab._dragData.fromTabList )` → `this.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if ( (dropEffect == "move" || dropEffect == "copy") && document == draggedTab.ownerDocument && !draggedTab._dragData.fromTabList )` → `this._updateTabStylesOnDrag()`
- 条件付き依存: `if (dropEffect == "move")` → `this.#setMovingTabMode()`
- 条件付き依存: `if (dropEffect == "move")` → `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`
- 条件付き依存: `if (this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab))` → `this._animateExpandedPinnedTabMove()`
- 条件付き依存: `if (dropEffect == "move")` → `this._animateTabMove()`
- 条件付き依存: `if (dropEffect == "link")` → `this._getDragTarget()`
- 条件付き依存: `if (!this.#dragTime)` → `Date.now()`
- 条件付き依存: `if (target)` → `isTabGroupLabel()`
- 条件付き依存: `if (target)` → `Date.now()`
- 条件付き依存: `if (target)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (target)` → `isTab()`
- 条件付き依存: `if (pixelsToScroll)` → `Math.min()`
- 条件付き依存: `if (!(pixelsToScroll))` → `this._getDropIndex()`
- 条件付き依存: `if (!(pixelsToScroll))` → `isSplitViewWrapper()`
- 条件付き依存: `if (!(pixelsToScroll))` → `isTabGroupLabel()`
- 条件付き依存: `if (newIndex == children.length)` → `children.at(-1).getBoundingClientRect()`
- 条件付き依存: `if (newIndex == children.length)` → `children.at()`
- 条件付き依存: `if (!(newIndex == children.length))` → `children[newIndex].getBoundingClientRect()`
- XPCOM: `Services.prefs`

## handle_drop()
- 位置: L278-750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dt.mozTypesAt()`, `event.stopPropagation()`, `gBrowser.TabMetrics.userTriggeredContext()`, `this._pinnedDropIndicator.hasAttribute()`, `this._resetTabsAfterDrop()`
- 条件付き依存: `if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE)` → `dt.mozGetDataAt()`
- 条件付き依存: `if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE)` → `draggedTab.container.tabDragAndDrop.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if (this._rtlMode)` → `movingTabs?.reverse()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `this._getDropIndex()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `gBrowser.duplicateTab()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `duplicatedTabs.push()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `gBrowser.moveTabsBefore()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `Math.round()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `this._tabbrowserTabs.dragAndDropElements.slice()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`
- 条件付き依存: `if (!(this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab)))` → `tabs.at()`
- 条件付き依存: `if (!(this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab)))` → `movingTabs.at()`
- 条件付き依存: `if (!(this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab)))` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `Math.min()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `Math.max()`
- 条件付き依存: `if (!(this._tabbrowserTabs.verticalMode))` → `Math.min()`
- 条件付き依存: `if (!(this._tabbrowserTabs.verticalMode))` → `Math.max()`
- 条件付き依存: `if (fromTabList)` → `this._getDropIndex()`
- 条件付き依存: `if (dropIndex && dropIndex > movingTabs[0].elementIndex)` → `isSplitViewWrapper()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `movingTabs.some()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `isTab()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `dragToPinTargets.some()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `el.contains()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `this._tabbrowserTabs.arrowScrollbox.contains()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `isTabGroupLabel()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `isSplitViewWrapper()`
- 条件付き依存: `if (shouldPin || shouldUnpin)` → `isTab()`
- 条件付き依存: `if (shouldPin && isTab(item))` → `gBrowser.pinTab()`
- 条件付き依存: `if (shouldPin && isTab(item))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (shouldUnpin)` → `gBrowser.unpinTab()`
- 条件付き依存: `if (shouldUnpin)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (shouldTranslate)` → `Date.now()`
- 条件付き依存: `if (shouldTranslate)` → `elementToMove()`
- 条件付き依存: `if (shouldTranslate)` → `item.toggleAttribute()`
- 条件付き依存: `if (gReduceMotion)` → `postTransitionCleanup()`
- 条件付き依存: `if (!(gReduceMotion))` → `item.addEventListener()`
- 条件付き依存: `if (shouldTranslate)` → `translationPromises.push()`
- 条件付き依存: `if (shouldTranslate)` → `Promise.all(translationPromises).then()`
- 条件付き依存: `if (shouldTranslate)` → `Promise.all()`
- 条件付き依存: `if (shouldTranslate)` → `this.finishAnimateTabMove()`
- 条件付き依存: `if (shouldTranslate)` → `moveTabs()`
- 条件付き依存: `if (!(shouldTranslate))` → `this.finishAnimateTabMove()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `gBrowser.addTabGroup()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(shouldCreateGroupOnDrop))` → `isTabGroupLabel()`
- 条件付き依存: `if (!(shouldCreateGroupOnDrop))` → `isTab()`
- 条件付き依存: `if (!(shouldCreateGroupOnDrop))` → `isSplitViewWrapper()`
- 条件付き依存: `if (dropElement.group != draggedTab.group)` → `dropElement.group.addTabs()`
- 条件付き依存: `if (!( shouldDropIntoCollapsedTabGroup && isTabGroupLabel(dropElement) && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) ))` → `moveTabs()`
- 条件付き依存: `if (!( shouldDropIntoCollapsedTabGroup && isTabGroupLabel(dropElement) && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) ))` → `this._tabbrowserTabs._notifyBackgroundTab()`
- 条件付き依存: `if (!( shouldDropIntoCollapsedTabGroup && isTabGroupLabel(dropElement) && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) ))` → `movingTabs.at()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._expandGroupOnDrop()`
- 条件付き依存: `if (!(draggedTab && draggedTab.container == this._tabbrowserTabs))` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._getDropIndex()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `gBrowser.adoptTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `draggedTab.ownerDocument.getElementById()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this.#releaseSpaceInScrolledContent()`
- 条件付き依存: `if (draggedTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (draggedTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (draggedTab)` → `this._getDropIndex()`
- 条件付き依存: `if (!(tab.selected))` → `isSplitViewWrapper()`
- 条件付き依存: `if (isSplitViewWrapper(tab))` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (droppedIntoPinnedArea)` → `unpinnedSplitViews.push()`
- 条件付き依存: `if (!(isSplitViewWrapper(tab)))` → `isTab()`
- 条件付き依存: `if (isTab(tab))` → `gBrowser.adoptTab()`
- 条件付き依存: `if (selectedTab)` → `gBrowser.adoptTab()`
- 条件付き依存: `if (movingTabs.length > 1)` → `isSplitViewWrapper()`
- 条件付き依存: `if (movingTabs.length > 1)` → `firstElement.tabs.at()`
- 条件付き依存: `if (movingTabs.length > 1)` → `lastElement.tabs.at()`
- 条件付き依存: `if ( !(isSplitViewWrapper(firstElement) && firstElement == lastElement) )` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (unpinnedSplitViews.length)` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (unpinnedSplitViews.length)` → `firstUnpinnedSplitView.tabs.at()`
- 条件付き依存: `if (unpinnedSplitViews.length)` → `lastUnpinnedSplitView.tabs.at()`
- 条件付き依存: `if (!(draggedTab))` → `Services.droppedLinkHandler.dropLinks()`
- 条件付き依存: `if (!(draggedTab))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(draggedTab))` → `this._getDragTarget()`
- 条件付き依存: `if (!(draggedTab))` → `this._tabbrowserTabs.selectedItem.getAttribute()`
- 条件付き依存: `if (!(draggedTab))` → `isTab()`
- 条件付き依存: `if (!(draggedTab))` → `this._getDropIndex()`
- 条件付き依存: `if (!(draggedTab))` → `links.map()`
- 条件付き依存: `if (!(draggedTab))` → `Services.droppedLinkHandler.getPolicyContainer()`
- 条件付き依存: `if (!(draggedTab))` → `Services.droppedLinkHandler.getTriggeringPrincipal()`
- 条件付き依存: `if (!(draggedTab))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( urls.length >= Services.prefs.getIntPref("browser.tabs.maxOpenBeforeWarn") )` → `lazy.OpenInTabsUtils.promiseConfirmOpenInTabs()`
- 条件付き依存: `if (!(draggedTab))` → `gBrowser.loadTabs()`
- XPCOM: `Services.droppedLinkHandler` / `Services.prefs`

## moveTabs()
- 位置: L448-476
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dropIndex !== undefined)` → `isSplitViewWrapper()`
- 条件付き依存: `if (fromTabList && isSplitViewWrapper(tab))` → `gBrowser.moveTabBefore()`
- 条件付き依存: `if (!(fromTabList && isSplitViewWrapper(tab)))` → `gBrowser.moveTabTo()`
- 条件付き依存: `if (dropElement && dropBefore)` → `gBrowser.moveTabsBefore()`
- 条件付き依存: `if (dropElement && dropBefore != undefined)` → `gBrowser.moveTabsAfter()`

## postTransitionCleanup()
- 位置: L504-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.removeAttribute()`, `resolve()`

## onTransitionEnd()
- 位置: L511-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.removeEventListener()`, `postTransitionCleanup()`

## handle_dragend()
- 位置: L752-921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `Services.prefs.getBoolPref()`, `draggedTab.hasAttribute()`, `dt.mozGetDataAt()`, `event.stopPropagation()`, `isTabGroupLabel()`, `screen.GetAvailRectDisplayPix()`, `this._resetTabsAfterDrop()`, `this.finishAnimateTabMove()`, `this.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._expandGroupOnDrop()`
- 条件付き依存: `if (tabAxisPos > tabAxisStart && tabAxisPos < tabAxisEnd)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (gBrowser.tabs.length == 1)` → `window.resizeTo()`
- 条件付き依存: `if (gBrowser.tabs.length == 1)` → `window.moveTo()`
- 条件付き依存: `if (gBrowser.tabs.length == 1)` → `window.focus()`
- 条件付き依存: `if (!(gBrowser.tabs.length == 1))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(gBrowser.tabs.length == 1))` → `gBrowser.replaceTabsWithWindow()`
- XPCOM: `Services.prefs`

## handle_dragleave()
- 位置: L923-937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`

## _rtlMode()
- 位置: L941-943
- 役割: (未記入)
- 触るとき: (未記入)

## #setMovingTabMode()
- 位置: L945-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNavToolbox.toggleAttribute()`, `this._tabbrowserTabs.toggleAttribute()`
- 条件付き依存: `if (movingTab)` → `this.#startStaleDragCheck()`
- 条件付き依存: `if (!(movingTab))` → `this.#stopStaleDragCheck()`

## #dragSession()
- 位置: L956-960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/dragservice;1"] .getService()`, `Cc["@mozilla.org/widget/dragservice;1"] .getService(Ci.nsIDragService) .getCurrentSession()`
- XPCOM: `nsIDragService` / `@mozilla.org/widget/dragservice;1`

## #startStaleDragCheck()
- 位置: L969-981
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setInterval()`, `window.addEventListener()`
- 条件付き依存: `if (!this.#dragSession)` → `this.#recoverFromStaleDrag()`

## #stopStaleDragCheck()
- 位置: L983-993
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearInterval()`, `window.removeEventListener()`

## #onMouseDown()
- 位置: L995-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.button == 0)` → `this.#recoverFromStaleDrag()`

## #recoverFromStaleDrag()
- 位置: L1004-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.tab.staleDragRecovery[label].add()`, `session?.endDragSession()`, `this._resetTabsAfterDrop()`, `this._tabbrowserTabs.dragAndDropElements.find()`, `this.finishAnimateTabMove()`
- 条件付き依存: `if (draggedItem)` → `this.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if (draggedItem)` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(draggedItem))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedItem))` → `this._expandGroupOnDrop()`

## _getDropIndex()
- 位置: L1043-1068
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elementToMove()`, `this._getDragTarget()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `elementForSize.getBoundingClientRect()`
- 条件付き依存: `if (!(this._tabbrowserTabs.verticalMode))` → `elementForSize.getBoundingClientRect()`

## _getDragTarget()
- 位置: L1087-1135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSplitViewWrapper()`, `isTab()`, `isTabGroupLabel()`
- 条件付き依存: `if ( findClosestTarget && target === this._tabbrowserTabs.arrowScrollbox && !this._tabbrowserTabs.verticalMode )` → `this.#getHorizontalScrollboxDragTarget()`
- 条件付き依存: `if (target && ignoreSides)` → `target.getBoundingClientRect()`
- 条件付き依存: `if (target && ignoreSides)` → `isTab()`
- 条件付き依存: `if (isTab(target) && target.splitview)` → `target.splitview.tabs.reverse()`
- 条件付き依存: `if (isTab(target) && target.splitview)` → `lTab.getBoundingClientRect()`
- 条件付き依存: `if (isTab(target) && target.splitview)` → `rTab.getBoundingClientRect()`

## #getHorizontalScrollboxDragTarget()
- 位置: L1150-1159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabbrowserTabs.dragAndDropElements.find()`

## isWithinBounds()
- 位置: L1151-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## #isMovingTab()
- 位置: L1161-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabbrowserTabs.hasAttribute()`

## _setIsDraggingTabGroup()
- 位置: L1177-1180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabbrowserTabs._invalidateCachedVisibleTabs()`

## _expandGroupOnDrop()
- 位置: L1189-1211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `draggedTab.ownerDocument.getElementById()`, `group.addEventListener()`, `isTabGroupLabel()`, `this.#releaseSpaceInScrolledContent()`

## _triggerDragOverGrouping()
- 位置: L1216-1222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dropElement.toggleAttribute()`, `this._clearDragOverGroupingTimer()`, `this._tabbrowserTabs.removeAttribute()`, `this._tabbrowserTabs.toggleAttribute()`

## _clearDragOverGroupingTimer()
- 位置: L1224-1229
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._dragOverGroupingTimer)` → `clearTimeout()`

## _setDragOverGroupColor()
- 位置: L1231-1254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabbrowserTabs.style.setProperty()`
- 条件付き依存: `if (!groupColorCode)` → `this._tabbrowserTabs.style.removeProperty()`

## _resetGroupTarget()
- 位置: L1259-1261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element?.removeAttribute()`

## startTabDrag()
- 位置: L1265-1491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clientPos()`, `dt.addElement()`, `dt.mozSetDataAt()`, `dt.setDragImage()`, `event.stopPropagation()`, `isSplitViewWrapper()`, `isTab()`, `isTabGroupLabel()`, `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`, `this.getDropEffectForTabDrag()`
- 条件付き依存: `if (this.expandOnHover)` → `MousePosTracker.removeListener()`
- 条件付き依存: `if (this._tabbrowserTabs.isContainerVerticalPinnedGrid(tab))` → `this._tabbrowserTabs.visibleTabs.slice()`
- 条件付き依存: `if (this._tabbrowserTabs.isContainerVerticalPinnedGrid(tab))` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.selectedTabs.filter()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (!(fromTabList || isTabGroupLabel(tab)))` → `selectedElements.filter()`
- 条件付き依存: `if (!(fromTabList || isTabGroupLabel(tab)))` → `[tab].concat()`
- 条件付き依存: `if (isTab(dtTab))` → `dt.mozSetDataAt()`
- 条件付き依存: `if (!canvas)` → `document.createElementNS()`
- 条件付き依存: `if (isSplitViewWrapper(tab))` → `tab.tabs.find()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `canvas.getContext()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `context.fillRect()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `document.createXULElement()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `this._tabbrowserTabs._dndPanel.setAttribute()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `document.createElementNS()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `wrapper.appendChild()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `this._tabbrowserTabs._dndPanel.appendChild()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `document.documentElement.appendChild()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `PageThumbs.captureToCanvas(browser, canvas) .then(captureListener) .catch()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `PageThumbs.captureToCanvas(browser, canvas) .then()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `PageThumbs.captureToCanvas()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `console.error()`
- 条件付き依存: `if (!(gMultiProcessBrowser))` → `PageThumbs.captureToCanvas(browser, canvas).catch()`
- 条件付き依存: `if (!(gMultiProcessBrowser))` → `PageThumbs.captureToCanvas()`
- 条件付き依存: `if (!(gMultiProcessBrowser))` → `console.error()`
- 条件付き依存: `if (this._rtlMode)` → `tab._dragData.movingTabs.reverse()`
- 条件付き依存: `if (isMovingInTabStrip)` → `this.#setMovingTabMode()`
- 条件付き依存: `if (tab.multiselected)` → `this._moveTogetherSelectedTabs()`
- 条件付き依存: `if (!(tab.multiselected))` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(tab))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (fromTabList)` → `Glean.browserUiInteraction.allTabsPanelDragstartTabEventCount.add()`

## captureListener()
- 位置: L1391-1393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dt.updateDragImage()`

## clientPos()
- 位置: L1436-1439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ele.getBoundingClientRect()`

## #reserveSpaceInScrolledContent()
- 位置: L1500-1506
- 役割: (未記入)
- 触るとき: (未記入)

## #releaseSpaceInScrolledContent()
- 位置: L1511-1514
- 役割: (未記入)
- 触るとき: (未記入)

## #marginBoxExtent()
- 位置: L1522-1537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`, `window.getComputedStyle()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `parseFloat()`

## _updateTabStylesOnDrag()
- 位置: L1545-1778
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `elementToMove()`, `isTabGroupLabel()`, `movingTab.setAttribute()`, `movingTabsSet.has()`, `t.hasAttribute()`, `tabStripItemElement.hasAttribute()`, `tabsOrigBounds.set()`, `this._tabbrowserTabs.arrowScrollbox.hasAttribute()`, `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (isPinned && this._tabbrowserTabs.verticalMode)` → `this._tabbrowserTabs.pinnedTabsContainer.setAttribute()`
- 条件付き依存: `if (!movingTabsSet.has(t) && !isTabInCollapsingGroup)` → `suppressTransitionsFor.push()`
- 条件付き依存: `if (suppressTransitionsFor.length)` → `window .promiseDocumentFlushed(() => {}) .then()`
- 条件付き依存: `if (suppressTransitionsFor.length)` → `window .promiseDocumentFlushed()`
- 条件付き依存: `if (suppressTransitionsFor.length)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (movingTabs.length == 2)` → `tabStripItemElement.setAttribute()`
- 条件付き依存: `if (movingTabs.length > 2)` → `tabStripItemElement.setAttribute()`
- 条件付き依存: `if ( !isPinned && this._tabbrowserTabs.arrowScrollbox.hasAttribute("overflowing") )` → `this.#marginBoxExtent()`
- 条件付き依存: `if (expandGroupOnDrop)` → `this.#marginBoxExtent()`
- 条件付き依存: `if ( !isPinned && this._tabbrowserTabs.arrowScrollbox.hasAttribute("overflowing") )` → `this.#reserveSpaceInScrolledContent()`
- 条件付き依存: `if (!( !isPinned && this._tabbrowserTabs.arrowScrollbox.hasAttribute("overflowing") ))` → `this._tabbrowserTabs.pinnedTabsContainer.hasAttribute()`
- 条件付き依存: `if ( isPinned && this._tabbrowserTabs.pinnedTabsContainer.hasAttribute("overflowing") )` → `document.createXULElement()`
- 条件付き依存: `if ( isPinned && this._tabbrowserTabs.pinnedTabsContainer.hasAttribute("overflowing") )` → `this._tabbrowserTabs.pinnedTabsContainer.appendChild()`
- 条件付き依存: `if ( (!isPinned && !tabIsPinned) || (tabIsPinned && isPinned && !isGrid) )` → `setElPosition()`
- 条件付き依存: `if (isGrid && tabIsPinned && isPinned)` → `setGridElPosition()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `SidebarController.expandOnHoverComplete.then()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `requestAnimationFrame()`

## setElPosition()
- 位置: L1702-1713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabsOrigBounds.get()`

## setGridElPosition()
- 位置: L1715-1729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.getBoundingClientRect()`, `tabsOrigBounds.get()`

## _moveTogetherSelectedTabs()
- 位置: L1783-1952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addAnimationData()`, `elementToMove()`, `selectedElement.getBoundingClientRect()`, `selectedElements.indexOf()`, `selectedElements.map()`, `selectedElements.some()`, `tab._dragData.movingTabsSet.has()`, `tab.toggleAttribute()`, `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`
- 条件付き依存: `if (unmovingTab.elementIndex > selectedIndices[currentIndex])` → `selectedElements .find(t => t.elementIndex == selectedIndices[currentIndex]) .getBoundingClientRect()`
- 条件付き依存: `if (unmovingTab.elementIndex > selectedIndices[currentIndex])` → `selectedElements .find()`
- 条件付き依存: `if (isGrid)` → `unmovingTab.getBoundingClientRect()`
- 条件付き依存: `if (isGrid)` → `this._tabbrowserTabs.dragAndDropElements[ newIndex ].getBoundingClientRect()`
- 条件付き依存: `if ( !tab._dragData.movingTabsSet.has(item) && (item._moveTogetherSelectedTabsData?.translateX || item._moveTogetherSelectedTabsData?.translateY) && ((item.pinne...)` → `elementToMove()`
- 条件付き依存: `if ( item._moveTogetherSelectedTabsData?.translateX || item._moveTogetherSelectedTabsData?.translateY )` → `elementToMove()`

## addAnimationData()
- 位置: L1801-1835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `movingElement.getBoundingClientRect()`, `movingElement.toggleAttribute()`, `selectedElement.getBoundingClientRect()`
- 条件付き依存: `if (gReduceMotion)` → `postTransitionCleanup()`
- 条件付き依存: `if (!(gReduceMotion))` → `movingElement.addEventListener()`

## postTransitionCleanup()
- 位置: L1809-1811
- 役割: (未記入)
- 触るとき: (未記入)

## onTransitionEnd()
- 位置: L1815-1824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `movingElement.removeEventListener()`, `postTransitionCleanup()`

## #isAnimatingMoveTogetherSelectedTabs()
- 位置: L1954-1961
- 役割: (未記入)
- 触るとき: (未記入)

## finishMoveTogetherSelectedTabs()
- 位置: L1963-1993
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elementToMove()`, `gBrowser.moveTabAfter()`, `gBrowser.moveTabBefore()`, `item.removeAttribute()`, `selectedElements.indexOf()`

## _animateExpandedPinnedTabMove()
- 位置: L1997-2179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `document.getElementById()`, `draggedTab.getBoundingClientRect()`, `event.dataTransfer.mozGetDataAt()`, `getTabShift()`, `movingTabs.includes()`, `tabs.filter()`, `this._tabbrowserTabs.visibleTabs.slice()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (tab != draggedTab)` → `getTabShift()`

## getTabShift()
- 位置: L2081-2120
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( tab.currentIndex < draggedTab.elementIndex && tab.currentIndex >= dropIndex )` → `Math.ceil()`
- 条件付き依存: `if ( tab.currentIndex > draggedTab.elementIndex && tab.currentIndex < dropIndex )` → `Math.floor()`

## _animateTabMove()
- 位置: L2182-2713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `bounds()`, `document.getElementById()`, `dragAndDropElements.slice()`, `elementToMove()`, `endEdge()`, `event.dataTransfer.mozGetDataAt()`, `getOverlappedElement()`, `getTabShift()`, `isSplitViewWrapper()`, `isTab()`, `movingTabsSet.has()`, `tabs.filter()`, `this.#clearPinnedDropIndicatorTimer()`, `this._clearDragOverGroupingTimer()`
- 条件付き依存: `if (this._rtlMode)` → `tabs.reverse()`
- 条件付き依存: `if ( (screen < draggedTabScreenAxis || screen > draggedTabScreenAxis + tabSize) && draggedTabScreenAxis + tabSize < endBound && draggedTabScreenAxis > startBound )` → `Math.min()`
- 条件付き依存: `if ( (screen < draggedTabScreenAxis || screen > draggedTabScreenAxis + tabSize) && draggedTabScreenAxis + tabSize < endBound && draggedTabScreenAxis > startBound )` → `Math.max()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `parseFloat()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `window.getComputedStyle()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `this._checkWithinPinnedContainerBounds()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `endEdge()`
- 条件付き依存: `if (!(dropElement))` → `tabs.find()`
- 条件付き依存: `if (!(dropElement))` → `tabs.findLast()`
- 条件付き依存: `if (!(dropElement))` → `Number.isInteger()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `Math.min()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `this._tabbrowserTabs.dragAndDropElements .filter(t => !movingTabsSet.has(t) || t == draggedTab) .at()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `this._tabbrowserTabs.dragAndDropElements .filter()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `movingTabsSet.has()`
- 条件付き依存: `if (dropElement)` → `elementToMove()`
- 条件付き依存: `if (dropElement)` → `getTabShift()`
- 条件付き依存: `if (dropElement)` → `bounds()`
- 条件付き依存: `if (dropElement)` → `greatestOverlap()`
- 条件付き依存: `if (dropElement)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (dropElement)` → `Math.min()`
- 条件付き依存: `if (dropElement)` → `Math.max()`
- 条件付き依存: `if (dropElement)` → `isTabGroupLabel()`
- 条件付き依存: `if ( isTabGroupLabel(draggedTab) && dropElement?.group && (!dropElement.group.collapsed || (dropElement.group.collapsed && dropElement.group.hasActiveTab)) )` → `isTabGroupLabel()`
- 条件付き依存: `if (!(isTabGroupLabel(dropElement)))` → `overlappedGroup.tabsAndSplitViews.findLast()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `movingTabsSet.has()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `isTab()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `isSplitViewWrapper()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `isTabGroupLabel()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `setTimeout()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `this._triggerDragOverGrouping()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `this._setDragOverGroupColor()`
- 条件付き依存: `if (shouldDropIntoCollapsedTabGroup)` → `setTimeout()`
- 条件付き依存: `if (shouldDropIntoCollapsedTabGroup)` → `this._triggerDragOverGrouping()`
- 条件付き依存: `if (shouldDropIntoCollapsedTabGroup)` → `this._setDragOverGroupColor()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._tabbrowserTabs.removeAttribute()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._resetGroupTarget()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `document.querySelector()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `dropElementGroup?.tabs.findLast()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `movingTabsSet.has()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `isTab()`
- 条件付き依存: `if (!( isTab(dropElement) && dropElementGroup && dropElement == lastUnmovingTabInGroup && !dropBefore && overlapPercent < dragOverGroupingThreshold ))` → `isTabGroupLabel()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._setDragOverGroupColor()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._tabbrowserTabs.toggleAttribute()`
- XPCOM: `Services.prefs`

## bounds()
- 位置: L2215-2215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## endEdge()
- 位置: L2231-2231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bounds()`

## getTabShift()
- 位置: L2318-2335
- 役割: (未記入)
- 触るとき: (未記入)

## greatestOverlap()
- 位置: L2381-2400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`

## getOverlappedElement()
- 位置: L2418-2442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `elementToMove()`, `getTabShift()`
- 条件付き依存: `if (!(screen > point))` → `bounds()`

## _checkWithinPinnedContainerBounds()
- 位置: L2715-2778
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._pinnedDropIndicator.hasAttribute()`
- 条件付き依存: `if ( this.#pinnedDropIndicatorTimeout && !inPinnedRange && !inVisibleRange && !isVisible && !isInteractive )` → `this.#resetPinnedDropIndicator()`
- 条件付き依存: `if (!( this.#pinnedDropIndicatorTimeout && !inPinnedRange && !inVisibleRange && !isVisible && !isInteractive ))` → `isTab()`
- 条件付き依存: `if ( isTab(draggedTab) && ((inVisibleRange && !isVisible) || (inPinnedRange && !isInteractive)) )` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (isVisible)` → `this._pinnedDropIndicator.setAttribute()`
- 条件付き依存: `if (!this.#pinnedDropIndicatorTimeout)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (!this.#pinnedDropIndicatorTimeout)` → `setTimeout()`
- 条件付き依存: `if (!this.#pinnedDropIndicatorTimeout)` → `this.#isMovingTab()`
- 条件付き依存: `if (this.#isMovingTab())` → `this._pinnedDropIndicator.setAttribute()`
- 条件付き依存: `if (!inPinnedRange)` → `this._pinnedDropIndicator.removeAttribute()`
- XPCOM: `Services.prefs`

## #clearPinnedDropIndicatorTimer()
- 位置: L2780-2785
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#pinnedDropIndicatorTimeout)` → `clearTimeout()`

## #resetPinnedDropIndicator()
- 位置: L2787-2791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearPinnedDropIndicatorTimer()`, `this._pinnedDropIndicator.removeAttribute()`

## finishAnimateTabMove()
- 位置: L2793-2811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elementToMove()`, `this.#isMovingTab()`, `this.#resetPinnedDropIndicator()`, `this.#setMovingTabMode()`, `this._clearDragOverGroupingTimer()`, `this._resetGroupTarget()`, `this._setDragOverGroupColor()`, `this._tabbrowserTabs.removeAttribute()`

## _resetTabsAfterDrop()
- 位置: L2820-2908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `draggedTabContainer.getElementsByClassName()`, `draggedTabContainer.getElementsByTagName()`, `draggedTabDocument.defaultView.SidebarController.updatePinnedTabsHeightOnResize()`, `draggedTabDocument.getElementById()`, `draggedTabDocument.getElementsByClassName()`, `isTabGroupLabel()`, `label.removeAttribute()`, `pinnedDropIndicator.removeAttribute()`, `pinnedTabsContainer.removeAttribute()`, `pinnedTabsContainer.removeChild()`, `splitviewWrapper.removeAttribute()`, `tab.removeAttribute()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `MousePosTracker.addListener()`
- 条件付き依存: `if (!isTabGroupLabel(draggedTab) || !draggedTab.group.collapsedByDrag)` → `this.#releaseSpaceInScrolledContent()`

## getDropEffectForTabDrag()
- 位置: L2914-2967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.droppedLinkHandler.canDropLink()`, `dt.mozTypesAt()`
- 条件付き依存: `if (isMovingTab)` → `dt.mozGetDataAt()`
- 条件付き依存: `if (isMovingTab)` → `isTab()`
- 条件付き依存: `if (isMovingTab)` → `isTabGroupLabel()`
- 条件付き依存: `if (isMovingTab)` → `isSplitViewWrapper()`
- 条件付き依存: `if (isMovingTab)` → `sourceNode.ownerDocument.documentElement.getAttribute()`
- 条件付き依存: `if ( (isTab(sourceNode) || isTabGroupLabel(sourceNode) || isSplitViewWrapper(sourceNode)) && sourceNode.documentGlobal.isChromeWindow && sourceNode.ownerDocument...)` → `PrivateBrowsingUtils.isWindowPrivate()`
- XPCOM: `Services.droppedLinkHandler`
