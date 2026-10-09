# browser/components/aiwindow/ui/modules/AutoTabGrouping.sys.mjs

source: browser/components/aiwindow/ui/modules/AutoTabGrouping.sys.mjs
source-hash: 4a1e9e2c7997cfa6a62762386e9f88f768c2126f
lines: 1215

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## titleLength()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.reduce()`
- 参照: `tab.label?.length`

## _getState()
- 位置: L139-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._state.get()`
- 条件付き依存: `if (!state)` → `this._state.set()`

## toggleGroupTabsPanel()
- 位置: L162-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.warn()`, `this._panels.get()`, `this.showGroupTabsPanel()`, `this.showGroupTabsPanel(win, { source }).catch()`
- 条件付き依存: `if (existing)` → `existing.hidePopup()`

## _getButtonAnchor()
- 位置: L180-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`, `lazy.CustomizableUI.getWidget(BUTTON_ID).forWindow()`
- 参照: `lazy.CustomizableUI.getWidget(BUTTON_ID).forWindow(win).anchor`

## showGroupTabsPanel()
- 位置: async L192-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.smartWindow.autoTabGroupMenuOpened.record()`, `Glean.smartWindow.autoTabGroupWindowDisplay.record()`, `Services.obs.addObserver()`, `button.setAttribute()`, `doc.getElementById()`, `lazy.CustomizableUI.hidePanelForNode()`, `panel._card.focus()`, `panel.addEventListener()`, `panel.openPopup()`, `popupSet.appendChild()`, `this._buildPanelSkeleton()`, `this._computeSuggestions()`, `this._getButtonAnchor()`, `this._getState()`, `this._panels.get()`, `this._panels.set()`, `this._syncCard()`, `this._withTimeout()`, `this._withTimeout(done, lazy.timeoutMs).then()`, `win.addEventListener()`
- 参照: `lazy.timeoutMs`, `panel._card.updateComplete`, `panel._waitedOut`, `state.computed`, `state.computing`, `state.recent.length`, `state.suggestions`, `state.suggestions.length`, `win.closed`, `win.document`, `win.gBrowser.tabs.length`, `win?.gBrowser`
- XPCOM: `Services.obs`

## onMouseDown()
- 位置: L218-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.contains()`, `panel._flyoutPanel?.contains()`, `panel.contains()`, `panel.hidePopup()`, `target.closest()`
- 参照: `event.target`, `target.closest?.("menupopup")?.triggerNode`

## onKeyDown()
- 位置: L230-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `panel.hidePopup()`
- 条件付き依存: `if (flyoutState && flyoutState !== "closed")` → `this._leaveFlyout()`
- 参照: `event.key`, `panel._flyoutPanel?.state`, `panel._restoreFocus`

## onDeactivate()
- 位置: L245-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideFlyout()`

## observe()
- 位置: L246-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onGroupsChanged()`

## teardown()
- 位置: L264-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.setAttribute()`, `panel._flyoutPanel?.remove()`, `panel.remove()`, `this._cancelHideFlyout()`, `this._getState()`, `this._panels.get()`, `win.removeEventListener()`
- 条件付き依存: `if (observingGroups)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._panels.get(win) === panel)` → `this._panels.delete()`
- 条件付き依存: `if (panel._restoreFocus)` → `anchor.focus()`
- 参照: `panel._restoreFocus`, `this._getState(win).recent`
- XPCOM: `Services.obs`

## _buildPanelSkeleton()
- 位置: L329-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `card.addEventListener()`, `doc.createElement()`, `panel.appendChild()`, `panel.setAttribute()`, `this._closeDuplicateTabs()`, `this._createById()`, `this._createPanel()`, `this._createSuggestions()`, `this._dismissPreviewOnRow()`, `this._focusFlyout()`, `this._getState()`, `this._getState(win).suggestions.slice()`, `this._scheduleHideFlyout()`, `this._selectGroup()`, `this._showPreview()`, `this._ungroupRecent()`
- 参照: `e.detail`, `e.detail.anchor`, `e.detail.id`, `e.detail.source`, `panel._activeRow`, `panel._card`, `panel._dismissedRow`, `panel._duplicateTabs`, `panel._flyoutPanel`, `panel._focusFlyoutController`, `panel._hideTimer`, `panel._restoreFocus`, `panel._waitedOut`, `win.document`

## _createPanel()
- 位置: L400-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.setAttribute()`, `win.document.createXULElement()`
- 参照: `panel.id`

## _ensureFlyoutPanel()
- 位置: L418-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `flyoutEl.addEventListener()`, `flyoutPanel.addEventListener()`, `flyoutPanel.appendChild()`, `flyoutPanel.setAttribute()`, `panel.hidePopup()`, `this._cancelHideFlyout()`, `this._createPanel()`, `this._flyoutHasFocus()`, `this._leaveFlyout()`, `this._releaseActiveRow()`, `this._scheduleHideFlyout()`, `this._selectTab()`, `win.document.createElement()`, `win.document.getElementById()`, `win.document.getElementById("mainPopupSet").appendChild()`
- 条件付き依存: `if (event.relatedTarget)` → `this._scheduleHideFlyout()`
- 参照: `e.detail.id`, `e.detail.index`, `event.relatedTarget`, `flyoutPanel._flyoutEl`, `panel._activeRow`, `panel._dismissedRow`, `panel._flyoutPanel`, `panel._flyoutPanel?.parentNode`

## _syncCard()
- 位置: L480-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getState()`, `this._hideFlyout()`, `this._pruneRecent()`, `this._tabGroupCount()`, `win.gBrowser.getAllDuplicateTabsToClose()`
- 参照: `card.computing`, `card.duplicates`, `card.recent`, `card.suggestions`, `card.tabGroups`, `panel._card`, `panel._waitedOut`, `state.computing`, `state.recent`, `state.suggestions`, `win.gBrowser.getAllDuplicateTabsToClose().length`

## _onGroupsChanged()
- 位置: L502-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel._flyoutPanel?.contains()`, `panel.contains()`, `this._flyoutListsGroups()`, `this._getState()`, `this._pruneRecent()`, `this._renderFlyout()`, `this._tabGroupCount()`
- 条件付き依存: `if (!card.tabGroups)` → `this._hideFlyout()`
- 条件付き依存: `if (!focusInUse)` → `this._focusFlyout()`
- 参照: `card.recent`, `card.tabGroups`, `panel._card`, `this._getState(win).recent`, `win.document.activeElement`

## _flyoutListsGroups()
- 位置: L531-540
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `flyoutPanel._flyoutEl.duplicates`, `flyoutPanel._flyoutEl.groupsListId`, `flyoutPanel._flyoutEl.suggestion`, `flyoutPanel?.state`, `panel._flyoutPanel`

## _takenGroupLabels()
- 位置: L550-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ ...win.gBrowser.getAllTabGroups().map(group => group.label), ...saved, ].filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.SessionStore.savedGroups.map()`, `win.gBrowser.getAllTabGroups()`, `win.gBrowser.getAllTabGroups().map()`
- 参照: `group.label`, `group.name`

## _tabGroupCount()
- 位置: L564-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.gBrowser.getAllTabGroups()`
- 参照: `win.SessionStore.savedGroups.length`, `win.gBrowser.getAllTabGroups().length`

## _createById()
- 位置: L571-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getState()`, `this._getState(win).suggestions.find()`
- 条件付き依存: `if (suggestion)` → `this._createSuggestions()`
- 参照: `s.id`

## _showPreview()
- 位置: L590-598
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (groups)` → `this._showFlyout()`
- 条件付き依存: `if (duplicates)` → `this._showDuplicatesFlyout()`
- 条件付き依存: `if (!(duplicates))` → `this._showFlyoutById()`

## _showFlyoutById()
- 位置: L600-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getState()`, `this._getState(win).suggestions.find()`
- 条件付き依存: `if (suggestion)` → `this._showFlyout()`
- 参照: `s.id`

## _showDuplicatesFlyout()
- 位置: L617-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AutoTabGroupingSuggestions.toTabInfo()`, `tabs.map()`, `this._showFlyout()`, `win.gBrowser.getAllDuplicateTabsToClose()`
- 条件付き依存: `if (!tabs.length)` → `this._hideFlyout()`
- 参照: `panel._duplicateTabs`, `tabs.length`

## _showFlyout()
- 位置: L643-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorRow.classList.add()`, `anchorRow.setAttribute()`, `this._cancelHideFlyout()`, `this._ensureFlyoutPanel()`, `this._renderFlyout()`
- 条件付き依存: `if (groups)` → `this._flyoutListsGroups()`
- 条件付き依存: `if (panel._activeRow && panel._activeRow !== anchorRow)` → `panel._activeRow.classList.remove()`
- 条件付き依存: `if (panel._activeRow && panel._activeRow !== anchorRow)` → `panel._activeRow.setAttribute()`
- 条件付き依存: `if (showing)` → `flyoutPanel.moveToAnchor()`
- 条件付き依存: `if (!(showing))` → `flyoutPanel.openPopup()`
- 参照: `flyoutPanel._flyoutEl.suggestion`, `flyoutPanel.state`, `panel._activeRow`

## _renderFlyout()
- 位置: L696-713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._flyoutHasFocus()`
- 条件付き依存: `if (refocus)` → `this._focusFlyout()`
- 参照: `flyoutEl.duplicates`, `flyoutEl.groupsListId`, `flyoutEl.suggestion`, `panel._flyoutPanel._flyoutEl`, `this._nextId`

## _hideFlyout()
- 位置: L722-734
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `flyoutPanel.addEventListener()`, `flyoutPanel?.hidePopup()`, `this._cancelHideFlyout()`, `this._releaseActiveRow()`
- 参照: `flyoutPanel.state`, `panel._flyoutPanel`

## _releaseActiveRow()
- 位置: L743-750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel._focusFlyoutController?.abort()`
- 条件付き依存: `if (panel._activeRow)` → `panel._activeRow.classList.remove()`
- 条件付き依存: `if (panel._activeRow)` → `panel._activeRow.setAttribute()`
- 参照: `panel._activeRow`

## _focusFlyout()
- 位置: async L752-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `flyoutPanel.addEventListener()`, `panel._focusFlyoutController?.abort()`
- 条件付き依存: `if (flyoutPanel.state === "open")` → `focusFirstTab()`
- 参照: `flyoutPanel._flyoutEl.updateComplete`, `flyoutPanel.state`, `panel._flyoutPanel`, `panel._focusFlyoutController`, `panel._focusFlyoutController.signal`

## focusFirstTab()
- 位置: L759-759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `flyoutPanel._flyoutEl.focusFirstRow()`

## _leaveFlyout()
- 位置: L780-786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row?.focus()`, `this._hideFlyout()`
- 参照: `panel._activeRow`, `panel._dismissedRow`

## _selectTab()
- 位置: L796-807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.hidePopup()`, `this._getState()`, `this._getState(win).suggestions.find()`, `win.gBrowser.tabs.includes()`
- 参照: `panel._duplicateTabs`, `s.id`, `tab.closing`, `this._getState(win).suggestions.find(s => s.id === id)?.tabs`, `win.gBrowser.selectedTab`

## _selectGroup()
- 位置: L817-824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entry.group.select()`, `panel.hidePopup()`, `this._getState()`, `this._getState(win).recent.find()`, `this._isGroupLive()`
- 参照: `e.id`, `entry.group`

## _flyoutHasFocus()
- 位置: L826-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel._flyoutPanel?.contains()`
- 参照: `panel.ownerDocument.activeElement`

## _dismissPreviewOnRow()
- 位置: L831-846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`, `row.classList.contains()`
- 条件付き依存: `if ( row && row !== panel._activeRow && !row.classList.contains("swgt-flyout-row") )` → `this._hideFlyout()`
- 参照: `panel._activeRow`

## _scheduleHideFlyout()
- 位置: L848-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setTimeout()`, `this._cancelHideFlyout()`, `this._flyoutHasFocus()`, `this._hideFlyout()`
- 参照: `panel._hideTimer`

## _cancelHideFlyout()
- 位置: L859-864
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (panel._hideTimer)` → `lazy.clearTimeout()`
- 参照: `panel._hideTimer`

## _createSuggestions()
- 位置: L878-938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.autoTabGroupAccepted.record()`, `Glean.smartWindow.autoTabGroupCompleted.record()`, `consumed.has()`, `lazy.console.warn()`, `state.suggestions.filter()`, `state.suggestions.findIndex()`, `suggestions.map()`, `this._creatableTabs()`, `this._focusAfterRowRemoved()`, `this._getState()`, `this._pruneSuggestions()`, `this._syncCard()`, `win.gBrowser.addTabGroup()`
- 条件付き依存: `if (group)` → `state.recent.unshift()`
- 参照: `e.name`, `lazy.TabMetrics.METRIC_SOURCE.SMART_WINDOW_GROUP_SUGGESTIONS`, `lazy.minTabsPerGroup`, `s.id`, `state.suggestions`, `suggestion.color`, `suggestion.id`, `suggestion.label`, `tabs.length`, `this._nextId`, `win.gBrowser.tabs`

## _creatableTabs()
- 位置: L948-952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestion.tabs.filter()`, `windowTabs.has()`
- 参照: `t.closing`, `t.group`

## _pruneSuggestions()
- 位置: L960-966
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `state.suggestions.filter()`, `this._creatableTabs()`, `this._getState()`
- 参照: `lazy.minTabsPerGroup`, `state.suggestions`, `this._creatableTabs(windowTabs, s).length`, `win.gBrowser.tabs`

## _focusAfterRowRemoved()
- 位置: async L978-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `Promise.all()`, `card.querySelectorAll()`, `target.focus()`
- 参照: `card.updateComplete`, `panel._card`, `panel._dismissedRow`, `panel.parentNode`, `row?.isConnected`, `rows.length`

## _metricsContext()
- 位置: L991-995
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabMetrics.userTriggeredContext()`
- 参照: `lazy.TabMetrics.METRIC_SOURCE.SMART_WINDOW_GROUP_SUGGESTIONS`

## _isGroupLive()
- 位置: L997-999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.tabGroups.includes()`

## _ungroupRecent()
- 位置: L1009-1042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.autoTabUngroupCompleted.record()`, `Glean.smartWindow.autoTabUngroupRequested.record()`, `entry.group.ungroupTabs()`, `lazy.console.warn()`, `state.recent.slice()`, `this._focusAfterRowRemoved()`, `this._forgetEntries()`, `this._getState()`, `this._isGroupLive()`, `this._metricsContext()`, `this._syncCard()`
- 参照: `e.name`, `entry.group`, `entry.group.tabs.length`, `entry.suggestionId`

## _closeDuplicateTabs()
- 位置: L1053-1105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.smartWindow.closeDuplicateTabsCompleted.record()`, `Glean.smartWindow.closeDuplicateTabsRequested.record()`, `Glean.smartWindow.closeDuplicateTabsStarted.record()`, `Glean.smartWindow.duplicateTabsClosed.record()`, `duplicates.filter()`, `lazy.console.warn()`, `panel.hidePopup()`, `this._getButtonAnchor()`, `titleLength()`, `win.gBrowser.getAllDuplicateTabsToClose()`, `win.gBrowser.removeAllDuplicateTabs()`, `win.gBrowser.tabs.includes()`
- 参照: `closed.length`, `duplicates.length`, `e.name`, `panel._restoreFocus`, `tab.closing`, `win.gBrowser.tabs`, `win.gBrowser.tabs.length`

## _forgetEntries()
- 位置: L1107-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries.map()`, `ids.has()`, `state.recent.filter()`, `this._getState()`
- 参照: `e.id`, `state.recent`

## _pruneRecent()
- 位置: L1113-1119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `state.recent.filter()`, `this._getState()`, `this._isGroupLive()`
- 条件付き依存: `if (dead.length)` → `this._forgetEntries()`
- 参照: `dead.length`, `e.group`

## _withTimeout()
- 位置: L1121-1135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `Promise.race([promise, timeout]).finally()`, `lazy.clearTimeout()`, `lazy.setTimeout()`, `reject()`

## _computeSuggestions()
- 位置: L1144-1213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.smartWindow.autoTabGroupSuggested.record()`, `Glean.smartWindow.autoTabGroupingCompleted.record()`, `Glean.smartWindow.autoTabGroupingRequested.record()`, `Glean.smartWindow.autoTabGroupingStarted.record()`, `lazy.AutoTabGroupingSuggestions.buildProposals()`, `lazy.AutoTabGroupingSuggestions.getCandidateTabs()`, `lazy.AutoTabGroupingSuggestions.toSuggestionData()`, `lazy.console.warn()`, `proposals.map()`, `suggestions.flatMap()`, `this._getState()`, `this._panels.get()`, `this._takenGroupLabels()`, `titleLength()`
- 条件付き依存: `if (state.computed)` → `Promise.resolve()`
- 条件付き依存: `if (!lazy.AutoTabGroupingSuggestions.isAvailable)` → `Promise.resolve()`
- 条件付き依存: `if (candidates.length < lazy.minCandidateTabs)` → `Promise.resolve()`
- 条件付き依存: `if (panel?._waitedOut)` → `this._syncCard()`
- 参照: `candidates.length`, `e.name`, `groupedTabs.length`, `lazy.AutoTabGroupingSuggestions.isAvailable`, `lazy.minCandidateTabs`, `panel?._waitedOut`, `s.tabs`, `state.computePromise`, `state.computed`, `state.computing`, `state.suggestions`, `suggestion.id`, `suggestion.tabs`, `suggestion.tabs.length`, `suggestions.length`, `this._nextId`, `win.gBrowser.tabs.length`
