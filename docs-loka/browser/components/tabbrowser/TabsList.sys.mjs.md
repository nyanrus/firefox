# browser/components/tabbrowser/TabsList.sys.mjs

source: browser/components/tabbrowser/TabsList.sys.mjs
source-hash: 31be6bf62ddbf74d4e4943da7adb2197adab5503
lines: 976

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## setAttributes()
- 位置: L18-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (value)` → `element.setAttribute()`
- 条件付き依存: `if (!(value))` → `element.removeAttribute()`

## getTabFromRow()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.closest()`

## getTabGroupFromRow()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.closest()`

## getRowVariant()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.closest()`, `element.closest("toolbaritem")?.getAttribute()`

## TabsListBase.domRefreshComplete()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## TabsListBase.constructor()
- 位置: L78-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filterFn()`

## TabsListBase.rows()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabToElement.values()`

## TabsListBase.#ownsEvent()
- 位置: L126-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`

## TabsListBase.handleEvent()
- 位置: L131-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleCommand()`, `this.#ownsEvent()`, `this._moveTab()`, `this._onClick()`, `this._onDragEnd()`, `this._onDragLeave()`, `this._onDragOver()`, `this._onDragStart()`, `this._onDrop()`, `this._refreshDOM()`, `this._tabAttrModified()`, `this._tabClose()`, `this.filterFn()`
- 条件付き依存: `if (!this.filterFn(event.target))` → `this._tabClose()`

## TabsListBase.#handleCommand()
- 位置: L183-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("all-tabs-mute-button"))` → `getTabFromRow(event.target)?.toggleMuteAudio()`
- 条件付き依存: `if (event.target.classList.contains("all-tabs-mute-button"))` → `getTabFromRow()`
- 条件付き依存: `if (!(event.target.classList.contains("all-tabs-mute-button")))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("all-tabs-close-button"))` → `getTabFromRow()`
- 条件付き依存: `if (tab)` → `this.gBrowser.removeTab()`
- 条件付き依存: `if (tab)` → `lazy.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(event.target.classList.contains("all-tabs-close-button")))` → `getRowVariant()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB)` → `getTabFromRow()`
- 条件付き依存: `if (tab)` → `this._selectTab()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB_GROUP)` → `getTabGroupFromRow(event.target)?.select()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB_GROUP)` → `getTabGroupFromRow()`

## TabsListBase._selectTab()
- 位置: L208-219
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.gBrowser.selectedTab != tab)` → `this.gBrowser.setSelectedTab()`
- 条件付き依存: `if (this.gBrowser.selectedTab != tab)` → `this.gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(this.gBrowser.selectedTab != tab))` → `this.gBrowser.tabContainer._handleTabSelect()`

## TabsListBase._populate()
- 位置: L224-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._populateDOM()`, `this._setupListeners()`

## TabsListBase._populateDOM()
- 位置: L229-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addElement()`, `this.doc.createDocumentFragment()`, `this.filterFn()`
- 条件付き依存: `if (tab.group && tab.group.id != currentGroupId)` → `fragment.appendChild()`
- 条件付き依存: `if (tab.group && tab.group.id != currentGroupId)` → `this._createGroupRow()`
- 条件付き依存: `if (!tabHiddenByGroup || this.onlyHiddenTabs)` → `fragment.appendChild()`
- 条件付き依存: `if (!tabHiddenByGroup || this.onlyHiddenTabs)` → `this._createRow()`

## TabsListBase._addElement()
- 位置: L253-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.containerNode.appendChild()`

## TabsListBase._cleanup()
- 位置: L260-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanupDOM()`, `this._cleanupListeners()`, `this._clearDropTarget()`

## TabsListBase._cleanupDOM()
- 位置: L266-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.remove()`, `this.containerNode .querySelectorAll()`, `this.containerNode .querySelectorAll(":scope toolbaritem") .forEach()`

## TabsListBase._refreshDOM()
- 位置: L273-289
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#domRefreshPromise)` → `this.containerNode.documentGlobal.requestAnimationFrame()`
- 条件付き依存: `if (this.listenersRegistered)` → `this._cleanupDOM()`
- 条件付き依存: `if (this.listenersRegistered)` → `this._populateDOM()`
- 条件付き依存: `if (this.#domRefreshPromise)` → `resolve()`

## TabsListBase._setupListeners()
- 位置: L291-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.containerNode.addEventListener()`, `this.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (this.dropIndicator)` → `this.containerNode.addEventListener()`

## TabsListBase._cleanupListeners()
- 位置: L318-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.containerNode.removeEventListener()`, `this.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this.dropIndicator)` → `this.containerNode.removeEventListener()`

## TabsListBase._tabAttrModified()
- 位置: L348-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabToElement.get()`
- 条件付き依存: `if (item)` → `this.filterFn()`
- 条件付き依存: `if (!this.filterFn(tab))` → `this._removeItem()`
- 条件付き依存: `if (!(!this.filterFn(tab)))` → `this._setRowAttributes()`
- 条件付き依存: `if (!(item))` → `this.filterFn()`
- 条件付き依存: `if (this.filterFn(tab))` → `this._addTab()`

## TabsListBase._moveTab()
- 位置: L366-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabToElement.get()`
- 条件付き依存: `if (item)` → `this._removeItem()`
- 条件付き依存: `if (item)` → `this._addTab()`

## TabsListBase._addTab()
- 位置: L379-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._createRow()`, `this.filterFn()`, `this.gBrowser.tabContainer.findNextTab()`
- 条件付き依存: `if (!nextTab)` → `this._addElement()`
- 条件付き依存: `if (!newTab.group && nextTab.group)` → `this.containerNode.querySelector()`
- 条件付き依存: `if (!newTab.group && nextTab.group)` → `this.containerNode.insertBefore()`
- 条件付き依存: `if (!(!newTab.group && nextTab.group))` → `this.tabToElement.get()`
- 条件付き依存: `if (!nextRow)` → `this._addElement()`
- 条件付き依存: `if (!(!nextRow))` → `this.containerNode.insertBefore()`

## TabsListBase._tabClose()
- 位置: L417-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabToElement.get()`
- 条件付き依存: `if (item)` → `this._removeItem()`

## TabsListBase._removeItem()
- 位置: L424-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.remove()`, `this.tabToElement.delete()`, `this.tabToElement.keys()`, `this.tabToElement.keys().some()`
- 条件付き依存: `if ( tab.group && !this.tabToElement.keys().some(t => t.group == tab.group) )` → `this.containerNode .querySelector(`:scope [tab-group-id="${tab.group.id}"]`) ?.remove()`
- 条件付き依存: `if ( tab.group && !this.tabToElement.keys().some(t => t.group == tab.group) )` → `this.containerNode .querySelector()`

## TabsPanel.constructor()
- 位置: L459-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.view.addEventListener()`

## TabsPanel.handleEvent()
- 位置: L469-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.handleEvent()`
- 条件付き依存: `if (event.target == this.panelMultiView)` → `this._cleanup()`
- 条件付き依存: `if (!this.listenersRegistered && event.target == this.view)` → `this._populate()`
- 条件付き依存: `if (!this.listenersRegistered && event.target == this.view)` → `this.gBrowser.translateTabContextMenu()`

## TabsPanel._populate()
- 位置: L490-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getRowVariant()`, `super._populate()`
- 条件付き依存: `if (getRowVariant(row) == ROW_VARIANT_TAB)` → `this._setImageAttributes()`
- 条件付き依存: `if (getRowVariant(row) == ROW_VARIANT_TAB)` → `getTabFromRow()`

## TabsPanel._selectTab()
- 位置: L503-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PanelMultiView.hidePopup()`, `super._selectTab()`, `this.view.closest()`

## TabsPanel._setupListeners()
- 位置: L508-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super._setupListeners()`, `this.panelMultiView.addEventListener()`

## TabsPanel._cleanupListeners()
- 位置: L513-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super._cleanupListeners()`, `this.panelMultiView.removeEventListener()`

## TabsPanel._createRow()
- 位置: L522-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.setAttribute()`, `doc.createXULElement()`, `muteButton.classList.add()`, `muteButton.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `this._setRowAttributes()`, `this.tabToElement.set()`
- 条件付き依存: `if (this.className)` → `row.classList.add()`
- 条件付き依存: `if (tab.userContextId)` → `tab.classList.forEach()`
- 条件付き依存: `if (tab.userContextId)` → `property.startsWith()`
- 条件付き依存: `if ( property.startsWith("identity-color") || property.startsWith("identity-icon") )` → `button.classList.add()`
- 条件付き依存: `if (tab.userContextId)` → `button.classList.add()`
- 条件付き依存: `if (tab.group)` → `row.classList.add()`
- 条件付き依存: `if (!tab.pinned)` → `doc.createXULElement()`
- 条件付き依存: `if (!tab.pinned)` → `closeButton.classList.add()`
- 条件付き依存: `if (!tab.pinned)` → `closeButton.setAttribute()`
- 条件付き依存: `if (!tab.pinned)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!tab.pinned)` → `row.appendChild()`

## TabsPanel._createGroupRow()
- 位置: L605-671
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.classList.add()`, `button.setAttribute()`, `doc.createXULElement()`, `row.appendChild()`, `row.setAttribute()`, `row.style.setProperty()`
- 条件付き依存: `if (group.collapsed)` → `button.classList.add()`
- 条件付き依存: `if (group.label)` → `setName()`
- 条件付き依存: `if (!(group.label))` → `doc.l10n .formatValues([{ id: "tab-group-name-default" }]) .then()`
- 条件付き依存: `if (!(group.label))` → `doc.l10n .formatValues()`
- 条件付き依存: `if (!(group.label))` → `setName()`

## setName()
- 位置: L652-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.l10n.setAttributes()`

## TabsPanel._setRowAttributes()
- 位置: L677-703
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.querySelector()`, `setAttributes()`, `tab.getAttribute()`, `this._setImageAttributes()`, `this.doc.l10n.setAttributes()`, `this.gBrowser.getTabTooltip()`

## TabsPanel._setImageAttributes()
- 位置: L709-723
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (image)` → `tab.getAttribute()`
- 条件付き依存: `if (image)` → `setAttributes()`
- 条件付き依存: `if (busy)` → `image.classList.add()`
- 条件付き依存: `if (!(busy))` → `image.classList.remove()`

## TabsPanel._onDragStart()
- 位置: L728-746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getRowVariant()`, `getTabFromRow()`, `getTabGroupFromRow()`, `this._getTargetRowFromEvent()`, `this.gBrowser.tabContainer.tabDragAndDrop.startTabDrag()`

## TabsPanel._getTargetRowFromEvent()
- 位置: L752-754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`

## TabsPanel._isMovingTabs()
- 位置: L760-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.gBrowser.tabContainer.tabDragAndDrop.getDropEffectForTabDrag()`

## TabsPanel._onDragOver()
- 位置: L769-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`, `this._isMovingTabs()`, `this._updateDropTarget()`

## TabsPanel._getRowIndex()
- 位置: L786-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.indexOf.call()`

## TabsPanel._onDrop()
- 位置: L793-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.dataTransfer.mozGetDataAt()`, `event.preventDefault()`, `event.stopPropagation()`, `getRowVariant()`, `getTabFromRow()`, `getTabGroupFromRow()`, `lazy.TabMetrics.userTriggeredContext()`, `this._clearDropTarget()`, `this._isMovingTabs()`, `this._updateDropTarget()`
- 条件付き依存: `if (draggedElement === targetElement)` → `this._clearDropTarget()`
- 条件付き依存: `if (this.dropTargetDirection == -1)` → `this.gBrowser.moveTabBefore()`
- 条件付き依存: `if (!(this.dropTargetDirection == -1))` → `this.gBrowser.moveTabAfter()`

## TabsPanel._onDragLeave()
- 位置: L837-851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearDropTarget()`, `this._isMovingTabs()`

## TabsPanel._onDragEnd()
- 位置: L856-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearDropTarget()`, `this._isMovingTabs()`

## TabsPanel._updateDropTarget()
- 位置: L868-897
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getRowVariant()`, `getTabFromRow()`, `row.getBoundingClientRect()`, `this._getRowIndex()`, `this._getTargetRowFromEvent()`
- 条件付き依存: `if ( getRowVariant(row) === ROW_VARIANT_TAB && getTabFromRow(row).splitview )` → `getTabFromRow()`
- 条件付き依存: `if (tab == tab.splitview.tabs[0])` → `this._setDropTarget()`
- 条件付き依存: `if (tab == tab.splitview.tabs[1])` → `this._setDropTarget()`
- 条件付き依存: `if (!( getRowVariant(row) === ROW_VARIANT_TAB && getTabFromRow(row).splitview ))` → `this._setDropTarget()`

## TabsPanel._setDropTarget()
- 位置: L903-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `holder.getBoundingClientRect()`, `subViewBody.getBoundingClientRect()`
- 条件付き依存: `if (this.dropTargetRow.previousSibling)` → `this.dropTargetRow.previousSibling.getBoundingClientRect()`
- 条件付き依存: `if (!(this.dropTargetRow.previousSibling))` → `this.dropTargetRow.getBoundingClientRect()`
- 条件付き依存: `if (!(this.dropTargetDirection === -1))` → `this.dropTargetRow.getBoundingClientRect()`

## TabsPanel._clearDropTarget()
- 位置: L935-944
- 役割: (未記入)
- 触るとき: (未記入)

## TabsPanel._onClick()
- 位置: L949-974
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.button == 1)` → `this._getTargetRowFromEvent()`
- 条件付き依存: `if (event.button == 1)` → `getRowVariant()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB)` → `getTabFromRow()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB)` → `this.gBrowser.removeTab()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB)` → `lazy.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB_GROUP)` → `getTabGroupFromRow(row)?.saveAndClose()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB_GROUP)` → `getTabGroupFromRow()`
- 条件付き依存: `if (rowVariant == ROW_VARIANT_TAB_GROUP)` → `lazy.TabMetrics.userTriggeredContext()`
