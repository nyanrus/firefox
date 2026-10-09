# browser/components/tabbrowser/content/tab-context-menu.js

source: browser/components/tabbrowser/content/tab-context-menu.js
source-hash: be3252ae5f20fdd94e266372a5ccb1eec234fb6d
lines: 1495

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## _ensureMenuArranged()
- 位置: L355-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `new this.MenuSectionLayout(layout, { dynamicItemSelectors: this.DYNAMIC_MENU_ITEM_SELECTORS, }).arrange()`, `this._hideUnusedSectionItems()`, `this._updateL10nIds()`
- 条件付き依存: `if (!this._altTabContextMenuPrefObserved)` → `XPCOMUtils.defineLazyPreferenceGetter()`

## _updateL10nIds()
- 位置: L397-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPopupMenu.querySelectorAll()`
- 条件付き依存: `if (item._classicL10nId == null)` → `item.getAttribute()`
- 条件付き依存: `if (id)` → `item.setAttribute()`

## _hideUnusedSectionItems()
- 位置: L412-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `this.MenuSectionLayout.placementsFor()`

## _updateMoveTabToFlattenedVisibility()
- 位置: L438-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `byId()`

## byId()
- 位置: L443-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## _updateToggleMuteMenuItems()
- 位置: L481-493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["muted", "soundplaying"].forEach()`, `aConditionFn()`
- 条件付き依存: `if (!aConditionFn || aConditionFn(attr))` → `aTab.hasAttribute()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `aTab.toggleMuteMenuItem.setAttribute()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `aTab.toggleMultiSelectMuteMenuItem.setAttribute()`
- 条件付き依存: `if (!(aTab.hasAttribute(attr)))` → `aTab.toggleMuteMenuItem.removeAttribute()`
- 条件付き依存: `if (!(aTab.hasAttribute(attr)))` → `aTab.toggleMultiSelectMuteMenuItem.removeAttribute()`

## updateContextMenu()
- 位置: L495-1114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `SessionStore.getLastClosedTabCount()`, `SharingUtils.ensureShareMenu()`, `TabContextMenu.AIWindow.isAIWindowActiveAndEnabled()`, `TabContextMenu.TabStateFlusher.flush()`, `["http", "https"].includes()`, `aPopupMenu.addEventListener()`, `aPopupMenu.getElementsByAttribute()`, `aPopupMenu.triggerNode.closest()`, `contextMoveTabOptions.setAttribute()`, `document .getElementById()`, `document .getElementById("History:UndoCloseTab") .toggleAttribute()`, `document .getElementById("context_closeTab") .setAttribute()`, `document.getElementById()`, `document.l10n.setArgs()`, `document.l10n.setAttributes()`, `gBrowser._getTabsToTheEndFrom()`, `gBrowser._getTabsToTheStartFrom()`, `gBrowser.allTabsSelected()`, `gBrowser.getDuplicateTabsToClose()`, `gBrowser.openTabs.filter()`, `gBrowser.tabs.filter()`, `gSync.updateTabContextMenu()`, `selectedTabs.every()`, `showFullScreenViewContextMenuItems()`, `this._ensureMenuArranged()`, `this._updateMoveTabToFlattenedVisibility()`, `this._updateToggleMuteMenuItems()`, `this.contextTab.addEventListener()`, `this.contextTab.hasAttribute()`, `this.contextTab.splitview.tabs.at()`, `this.contextTabs.at()`, `this.contextTabs.every()`, `this.contextTabs.map()`, `this.contextTabs.some()`, `visibleOrCollapsedTabs.at()`, `visibleOrCollapsedTabs.every()`
- 条件付き依存: `if (tab.splitview)` → `splitViews.add()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `this.contextTabs.map(t => t.group).filter()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `this.contextTabs.map()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `gBrowser.getAllTabGroups()`
- 条件付き依存: `if (selectedGroupCount == 1)` → `this.contextTabs.every()`
- 条件付き依存: `if (groupToFilter && this.contextTabs.every(t => t.group))` → `openGroupsToMoveTo.filter()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `SessionStore.shouldSaveTabsToGroup()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && SessionStore.shouldSaveTabsToGroup(this.contextTabs) )` → `SessionStore.getSavedTabGroups()`
- 条件付き依存: `if (isAllSplitViewTabs)` → `contextMoveSplitViewToNewGroup.setAttribute()`
- 条件付き依存: `if (!(isAllSplitViewTabs))` → `contextMoveTabToNewGroup.setAttribute()`
- 条件付き依存: `if (isAllSplitViewTabs)` → `contextMoveTabToGroup.setAttribute()`
- 条件付き依存: `if (!(isAllSplitViewTabs))` → `contextMoveTabToGroup.setAttribute()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `document.getElementById()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsMenu .querySelectorAll("[tab-group-id]") .forEach()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsMenu .querySelectorAll()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `el.remove()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsToMoveTo.toReversed().forEach()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsToMoveTo.toReversed()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `this._createTabGroupMenuItem()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `upperSeparator.after()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `savedGroupsMenu.querySelector()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `savedGroupsMenuPopup .querySelectorAll("[tab-group-id]") .forEach()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `savedGroupsMenuPopup .querySelectorAll()`
- 条件付き依存: `if (savedGroupsToMoveTo.length)` → `savedGroupsToMoveTo.forEach()`
- 条件付き依存: `if (savedGroupsToMoveTo.length)` → `this._createTabGroupMenuItem()`
- 条件付き依存: `if (savedGroupsToMoveTo.length)` → `savedGroupsMenuPopup.appendChild()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `JSON.stringify()`
- 条件付き依存: `if (isAllSplitViewTabs)` → `contextUngroupSplitView.setAttribute()`
- 条件付き依存: `if (!(isAllSplitViewTabs))` → `contextUngroupTab.setAttribute()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.contextTabs.every()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.TabNotes.isEligible()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.removeNewBadge()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.tabs.notes.newBadge.enabled", true) )` → `this.addNewBadge()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.TabNotes.has(this.contextTab).then()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.TabNotes.has()`
- 条件付き依存: `if (splitViewEnabled)` → `contextMoveTabToNewSplitView.removeAttribute()`
- 条件付き依存: `if (splitViewEnabled)` → `contextMoveTabToNewSplitView.setAttribute()`
- 条件付き依存: `if (splitViewEnabled)` → `this.contextTabs.filter()`
- 条件付き依存: `if (splitViewEnabled)` → `t.hasAttribute()`
- 条件付き依存: `if (this._unloadTabInContextMenu)` → `this.contextTabs.filter()`
- 条件付き依存: `if (this._unloadTabInContextMenu)` → `unloadTabItem.setAttribute()`
- 条件付き依存: `if (this._unloadTabInContextMenu)` → `JSON.stringify()`
- 条件付き依存: `if (!this._altTabContextMenu)` → `document.getElementById()`
- 条件付き依存: `if (!this._altTabContextMenu)` → `TabContextMenu.GenAI.buildTabMenu()`
- 条件付き依存: `if (!(!this._altTabContextMenu))` → `document.getElementById()`
- 条件付き依存: `if (!(!this._altTabContextMenu))` → `TabContextMenu.GenAI.buildTabSummarizeItem()`
- 条件付き依存: `if (lastTabToMove.pinned)` → `gBrowser.tabContainer.findNextTab()`
- 条件付き依存: `if (!contentSharingShareTabs.hidden)` → `this.addNewBadge()`
- 条件付き依存: `if (this._altTabContextMenu)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._altTabContextMenu))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (this._altTabContextMenu)` → `document .getElementById("context_sendTabToDevice") .setAttribute()`
- 条件付き依存: `if (this._altTabContextMenu)` → `document .getElementById()`
- XPCOM: `Services.prefs`

## _createTabGroupMenuItem()
- 位置: L1116-1151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `item.classList.add()`, `item.setAttribute()`, `item.style.setProperty()`
- 条件付き依存: `if (label)` → `item.setAttribute()`
- 条件付き依存: `if (!(label))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (isSaved)` → `item.classList.add()`

## handleEvent()
- 位置: L1153-1170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.detail.changed.includes()`, `this._updateToggleMuteMenuItems()`
- 条件付き依存: `if (aEvent.target.id == "tabContextMenu")` → `this.contextTab.removeEventListener()`

## createReopenInContainerMenu()
- 位置: L1172-1178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createUserContextMenu()`, `this.contextTab.getAttribute()`

## duplicateSelectedTabs()
- 位置: L1179-1188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.duplicateTab()`, `gBrowser.moveTabTo()`, `this.contextTabs.at()`
- 条件付き依存: `if (tab.group)` → `Glean.tabgroup.tabInteractions.duplicate.add()`

## reopenInContainer()
- 位置: L1189-1255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.containers.tabAssignedContainer.record()`, `event.target.getAttribute()`, `gBrowser.addTab()`, `parseInt()`, `tab.getAttribute()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `JSON.parse()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `SessionStore.getTabState()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `E10SUtils.deserializePrincipal()`
- 条件付き依存: `if (!triggeringPrincipal || triggeringPrincipal.isNullPrincipal)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (triggeringPrincipal.isContentPrincipal)` → `Services.scriptSecurityManager.principalWithOA()`
- 条件付き依存: `if (tab.muted && !newTab.muted)` → `newTab.toggleMuteAudio()`
- XPCOM: `Services.scriptSecurityManager`

## closeContextTabs()
- 位置: L1257-1272
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.contextTab.multiselected)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (this.contextTab.multiselected)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(this.contextTab.multiselected))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(this.contextTab.multiselected))` → `gBrowser.TabMetrics.userTriggeredContext()`

## explicitUnloadTabs()
- 位置: L1274-1276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.explicitUnloadTabs()`

## moveTabsToNewGroup()
- 位置: L1278-1304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.addTabGroup()`, `gTabsPanel.hideAllTabsPanel()`

## moveSplitViewToNewGroup()
- 位置: L1306-1337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.addTabGroup()`, `gTabsPanel.hideAllTabsPanel()`
- 条件付き依存: `if (contextTab.splitView)` → `tabsAndSplitViews.includes()`
- 条件付き依存: `if (!tabsAndSplitViews.includes(contextTab.splitView))` → `tabsAndSplitViews.push()`
- 条件付き依存: `if (!(contextTab.splitView))` → `tabsAndSplitViews.push()`

## moveTabsToGroup()
- 位置: L1342-1354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `elementsToMove.add()`, `elementsToMove.values()`, `gBrowser.TabMetrics.userTriggeredContext()`, `group.addTabs()`, `group.documentGlobal.focus()`

## addTabsToSavedGroup()
- 位置: L1356-1385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.addTabsToSavedGroup()`, `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.removeTabs()`
- 条件付き依存: `if (tab.splitview)` → `seen.has()`
- 条件付き依存: `if (!seen.has(splitTab))` → `seen.add()`
- 条件付き依存: `if (!seen.has(splitTab))` → `tabs.push()`
- 条件付き依存: `if (!(tab.splitview))` → `seen.has()`
- 条件付き依存: `if (!seen.has(tab))` → `seen.add()`
- 条件付き依存: `if (!seen.has(tab))` → `tabs.push()`

## ungroupTabsAndSplitViews()
- 位置: L1387-1397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `splitViews.has()`
- 条件付き依存: `if (tab.splitview && !splitViews.has(tab.splitview))` → `splitViews.add()`
- 条件付き依存: `if (tab.splitview && !splitViews.has(tab.splitview))` → `gBrowser.ungroupSplitView()`
- 条件付き依存: `if (!tab.splitview)` → `gBrowser.ungroupTab()`

## moveTabsToSplitView()
- 位置: L1399-1431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.addTabSplitView()`, `tabsToAdd.indexOf()`, `this.contextTabs.includes()`
- 条件付き依存: `if (selectedTabIndex > -1 && selectedTabIndex != 0)` → `tabsToAdd.splice()`
- 条件付き依存: `if (selectedTabIndex > -1 && selectedTabIndex != 0)` → `tabsToAdd.unshift()`
- 条件付き依存: `if (this.contextTabs.length < 2)` → `gBrowser.addTrustedTab()`

## unsplitTabs()
- 位置: L1433-1438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `splitview.unsplitTabs()`, `splitviews.forEach()`, `this.contextTabs.map()`, `this.contextTabs.map(tab => tab.splitview).filter()`

## reverseSplitView()
- 位置: L1440-1442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextTab.splitview?.reverseTabs()`

## addNewBadge()
- 位置: L1447-1453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabLocalization.formatValueSync()`, `menuItem.classList.add()`, `menuItem.setAttribute()`

## removeNewBadge()
- 位置: L1458-1461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menuItem.classList.remove()`, `menuItem.removeAttribute()`
