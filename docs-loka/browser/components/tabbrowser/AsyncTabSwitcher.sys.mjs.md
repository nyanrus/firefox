# browser/components/tabbrowser/AsyncTabSwitcher.sys.mjs

source: browser/components/tabbrowser/AsyncTabSwitcher.sys.mjs
source-hash: 294ee4fa7ca9575d18959bb006cf5ba7b9c97b2c
lines: 1499

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## AsyncTabSwitcher.constructor()
- 位置: L63-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `initialBrowser.preserveLayers()`, `this.log()`, `this.setTabState()`, `this.tabbrowser.getTabForBrowser()`, `this.window.addEventListener()`, `this.window.document.addEventListener()`
- 条件付き依存: `if (!this.windowHidden)` → `this.log()`
- 条件付き依存: `if (!this.windowHidden)` → `this.setTabState()`

## AsyncTabSwitcher.destroy()
- 位置: L174-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.document.removeEventListener()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this.unloadTimer)` → `this.clearTimer()`
- 条件付き依存: `if (this.loadTimer)` → `this.clearTimer()`

## AsyncTabSwitcher.setTimer()
- 位置: L198-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## AsyncTabSwitcher.clearTimer()
- 位置: L208-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `timer.cancel()`

## AsyncTabSwitcher.getTabState()
- 位置: L212-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabState.get()`
- 条件付き依存: `if (state === undefined)` → `this.setTabStateNoAction()`

## AsyncTabSwitcher.setTabStateNoAction()
- 位置: L238-244
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (state == this.STATE_UNLOADED)` → `this.tabState.delete()`
- 条件付き依存: `if (!(state == this.STATE_UNLOADED))` → `this.tabState.set()`

## AsyncTabSwitcher.setTabState()
- 位置: L246-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabState()`, `this.setTabStateNoAction()`
- 条件付き依存: `if (state == this.STATE_LOADING)` → `this.assert()`
- 条件付き依存: `if (state == this.STATE_LOADING)` → `this.warmingTabs.has()`
- 条件付き依存: `if (browser.hasLayers)` → `this.onLayersReady()`
- 条件付き依存: `if (state == this.STATE_UNLOADING)` → `this.unwarmTab()`
- 条件付き依存: `if (!browser.hasLayers)` → `this.onLayersCleared()`
- 条件付き依存: `if (state == this.STATE_LOADED)` → `this.maybeActivateDocShell()`
- 条件付き依存: `if (!tab.linkedBrowser.isRemoteBrowser)` → `this.getTabState()`
- 条件付き依存: `if (!tab.linkedBrowser.isRemoteBrowser)` → `this.assert()`

## AsyncTabSwitcher.windowHidden()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)

## AsyncTabSwitcher.tabLayerCache()
- 位置: L306-308
- 役割: (未記入)
- 触るとき: (未記入)

## AsyncTabSwitcher.finish()
- 位置: L310-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`, `this.destroy()`, `this.getTabState()`, `this.log()`, `this.tabbrowser.dispatchEvent()`, `this.window.document.commandDispatcher.unlock()`

## AsyncTabSwitcher.updateDisplay()
- 位置: L338-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabState()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `this.requestedTab.hasAttribute()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `requestedBrowser.currentURI.schemeIs()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `this.logging()`
- 条件付き依存: `if (this.logging())` → `this.addLogFlag()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `this.addLogFlag()`
- 条件付き依存: `if (!shouldBeBlank && this.blankTab)` → `this.blankTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (this.blankTab)` → `this.blankTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (shouldBeBlank && this.blankTab !== showTab)` → `this.blankTab.linkedBrowser.setAttribute()`
- 条件付き依存: `if (!needSpinner && this.spinnerTab)` → `this.noteSpinnerHidden()`
- 条件付き依存: `if (!needSpinner && this.spinnerTab)` → `this.tabbrowser.tabpanels.removeAttribute()`
- 条件付き依存: `if (!needSpinner && this.spinnerTab)` → `this.spinnerTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (this.spinnerTab)` → `this.spinnerTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (!(this.spinnerTab))` → `this.noteSpinnerDisplayed()`
- 条件付き依存: `if (needSpinner && this.spinnerTab !== showTab)` → `this.tabbrowser.tabpanels.toggleAttribute()`
- 条件付き依存: `if (needSpinner && this.spinnerTab !== showTab)` → `this.spinnerTab.linkedBrowser.toggleAttribute()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `this.tabbrowser._adjustFocusBeforeTabSwitch()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `this.maybeVisibleTabs.add()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `this.tabbrowser.tabContainer.getRelatedElement()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if (index != -1)` → `this.log()`
- 条件付き依存: `if (index != -1)` → `this.tinfo()`
- 条件付き依存: `if (index != -1)` → `tabpanels.updateSelectedIndex()`
- 条件付き依存: `if (!(requestedTabState == this.STATE_LOADED))` → `this.noteMakingTabVisibleWithoutLayers()`
- 条件付き依存: `if (showTab === this.requestedTab)` → `this.tabbrowser._adjustFocusAfterTabSwitch()`
- 条件付き依存: `if (showTab === this.requestedTab)` → `this.window.gURLBar.afterTabSwitchFocusChange()`
- 条件付き依存: `if (showTab === this.requestedTab)` → `this.maybeActivateDocShell()`

## AsyncTabSwitcher.assert()
- 位置: L481-490
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!cond)` → `dump()`
- 条件付き依存: `if (!cond)` → `Error()`

## AsyncTabSwitcher.maybeClearLoadTimer()
- 位置: L492-501
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.loadTimer)` → `this.clearTimer()`

## AsyncTabSwitcher.loadRequestedTab()
- 位置: L504-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`, `this.handleEvent()`, `this.log()`, `this.setTabState()`, `this.setTimer()`, `this.tinfo()`

## AsyncTabSwitcher.maybeActivateDocShell()
- 位置: L520-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabState()`
- 条件付き依存: `if ( tab == this.requestedTab && canCheckDocShellState && state == this.STATE_LOADED && !browser.docShellIsActive && !this.windowHidden )` → `this.logState()`
- 条件付き依存: `if ( tab == this.requestedTab && canCheckDocShellState && state == this.STATE_LOADED && !browser.docShellIsActive && !this.windowHidden )` → `browser.preserveLayers()`

## AsyncTabSwitcher.preActions()
- 位置: L549-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`
- 条件付き依存: `if (!tab.linkedBrowser)` → `this.tabState.delete()`
- 条件付き依存: `if (!tab.linkedBrowser)` → `this.tabLayerCache.splice()`
- 条件付き依存: `if (!tab.linkedBrowser)` → `this.unwarmTab()`
- 条件付き依存: `if (this.spinnerTab && !this.spinnerTab.linkedBrowser)` → `this.noteSpinnerHidden()`
- 条件付き依存: `if (this.loadingTab && !this.loadingTab.linkedBrowser)` → `this.maybeClearLoadTimer()`

## AsyncTabSwitcher.postActions()
- 位置: L591-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`, `this.getTabState()`, `this.logState()`, `this.maybeFinishTabSwitch()`, `this.shouldDeactivateDocShell()`, `this.tabLayerCache.includes()`, `this.updateDisplay()`, `this.warmingTabs.has()`
- 条件付き依存: `if (!this.requestedTab.linkedBrowser.isRemoteBrowser)` → `this.maybeClearLoadTimer()`
- 条件付き依存: `if ( !this.loadTimer && !this.windowHidden && (stateOfRequestedTab == this.STATE_UNLOADED || stateOfRequestedTab == this.STATE_UNLOADING || this.warmingTabs.has(...)` → `this.assert()`
- 条件付き依存: `if ( !this.loadTimer && !this.windowHidden && (stateOfRequestedTab == this.STATE_UNLOADED || stateOfRequestedTab == this.STATE_UNLOADING || this.warmingTabs.has(...)` → `this.loadRequestedTab()`
- 条件付き依存: `if (numBackgroundCached > 0)` → `this.deactivateCachedBackgroundTabs()`
- 条件付き依存: `if (numWarming > lazy.gTabWarmingMax)` → `this.logState()`
- 条件付き依存: `if (this.unloadTimer)` → `this.clearTimer()`
- 条件付き依存: `if (numWarming > lazy.gTabWarmingMax)` → `this.unloadNonRequiredTabs()`
- 条件付き依存: `if (numPending == 0)` → `this.finish()`

## AsyncTabSwitcher.onUnloadTimeout()
- 位置: L699-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.unloadNonRequiredTabs()`

## AsyncTabSwitcher.deactivateCachedBackgroundTabs()
- 位置: L704-712
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tab !== this.requestedTab)` → `browser.preserveLayers()`

## AsyncTabSwitcher.unloadNonRequiredTabs()
- 位置: L718-757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.maybeVisibleTabs.has()`, `this.shouldDeactivateDocShell()`, `this.tabLayerCache.includes()`
- 条件付き依存: `if ( state == this.STATE_LOADED && !this.maybeVisibleTabs.has(tab) && tab !== this.lastVisibleTab && tab !== this.loadingTab && tab !== this.requestedTab && !isI...)` → `this.setTabState()`
- 条件付き依存: `if (numPending)` → `this.setTimer()`
- 条件付き依存: `if (numPending)` → `this.handleEvent()`

## AsyncTabSwitcher.onLoadTimeout()
- 位置: L760-762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.maybeClearLoadTimer()`

## AsyncTabSwitcher.onLayersReady()
- 位置: L765-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`, `this.getTabState()`, `this.logState()`, `this.setTabState()`, `this.tabbrowser.getTabForBrowser()`, `this.unwarmTab()`
- 条件付き依存: `if (this.loadingTab === tab)` → `this.maybeClearLoadTimer()`

## AsyncTabSwitcher.onPaint()
- 位置: L790-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addLogFlag()`, `this.maybeVisibleTabs.clear()`, `this.notePaint()`

## AsyncTabSwitcher.onLayersCleared()
- 位置: L801-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`, `this.getTabState()`, `this.logState()`, `this.setTabState()`, `this.tabbrowser.getTabForBrowser()`

## AsyncTabSwitcher.onRemotenessChange()
- 位置: L817-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logState()`
- 条件付き依存: `if (!tab.linkedBrowser.isRemoteBrowser)` → `this.getTabState()`
- 条件付き依存: `if (this.getTabState(tab) == this.STATE_LOADING)` → `this.onLayersReady()`
- 条件付き依存: `if (!(this.getTabState(tab) == this.STATE_LOADING))` → `this.getTabState()`
- 条件付き依存: `if (this.getTabState(tab) == this.STATE_UNLOADING)` → `this.onLayersCleared()`
- 条件付き依存: `if (!(!tab.linkedBrowser.isRemoteBrowser))` → `this.getTabState()`
- 条件付き依存: `if (this.getTabState(tab) == this.STATE_LOADED)` → `this.setTabState()`

## AsyncTabSwitcher.onTabRemoved()
- 位置: L835-839
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.lastVisibleTab == tab)` → `this.handleEvent()`

## AsyncTabSwitcher.onTabRemovedImpl()
- 位置: L843-845
- 役割: (未記入)
- 触るとき: (未記入)

## AsyncTabSwitcher.onTabDiscarded()
- 位置: L847-849
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleEvent()`

## AsyncTabSwitcher.onTabDiscardedImpl()
- 位置: L854-868
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logState()`, `this.setTabStateNoAction()`, `this.tabLayerCache.indexOf()`, `this.unwarmTab()`
- 条件付き依存: `if (this.loadingTab === tab)` → `this.maybeClearLoadTimer()`
- 条件付き依存: `if (cacheIndex != -1)` → `this.tabLayerCache.splice()`

## AsyncTabSwitcher.onVisibilityChange()
- 位置: L870-887
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.windowHidden)` → `this.shouldDeactivateDocShell()`
- 条件付き依存: `if (state == this.STATE_LOADING || state == this.STATE_LOADED)` → `this.setTabState()`
- 条件付き依存: `if (this.windowHidden)` → `this.maybeClearLoadTimer()`
- 条件付き依存: `if (!(this.windowHidden))` → `this.maybeActivateDocShell()`

## AsyncTabSwitcher.onSwapDocShells()
- 位置: L889-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.swapMap.set()`
- 条件付き依存: `if (otherTabbrowser && otherTabbrowser._switcher)` → `otherTabbrowser.getTabForBrowser()`
- 条件付き依存: `if (otherTabbrowser && otherTabbrowser._switcher)` → `otherSwitcher.getTabState()`

## AsyncTabSwitcher.onEndSwapDocShells()
- 位置: L913-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.maybeClearLoadTimer()`, `this.swapMap.delete()`, `this.swapMap.get()`, `this.tabbrowser.getTabForBrowser()`
- 条件付き依存: `if (ourTab)` → `this.setTabStateNoAction()`

## AsyncTabSwitcher.shouldDeactivateDocShell()
- 位置: L942-948
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PictureInPicture.isOriginatingBrowser()`, `this.tabbrowser._printPreviewBrowsers.has()`, `this.tabbrowser.splitViewBrowsers.includes()`

## AsyncTabSwitcher.shouldActivateDocShell()
- 位置: L950-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabState()`, `this.tabbrowser.getTabForBrowser()`

## AsyncTabSwitcher.activateBrowserForPrintPreview()
- 位置: L956-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabState()`, `this.tabbrowser.getTabForBrowser()`
- 条件付き依存: `if (state != this.STATE_LOADING && state != this.STATE_LOADED)` → `this.setTabState()`
- 条件付き依存: `if (state != this.STATE_LOADING && state != this.STATE_LOADED)` → `this.logState()`
- 条件付き依存: `if (state != this.STATE_LOADING && state != this.STATE_LOADED)` → `this.tinfo()`

## AsyncTabSwitcher.canWarmTab()
- 位置: L967-990
- 役割: (未記入)
- 触るとき: (未記入)

## AsyncTabSwitcher.shouldWarmTab()
- 位置: L992-1003
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canWarmTab()`
- 条件付き依存: `if (this.canWarmTab(tab))` → `this.getTabState()`

## AsyncTabSwitcher.unwarmTab()
- 位置: L1005-1007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.warmingTabs.delete()`

## AsyncTabSwitcher.warmupTab()
- 位置: L1009-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logState()`, `this.queueUnload()`, `this.setTabState()`, `this.shouldWarmTab()`, `this.tinfo()`, `this.warmingTabs.add()`

## AsyncTabSwitcher.cleanUpTabAfterEviction()
- 位置: L1021-1028
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.assert()`, `this.setTabState()`
- 条件付き依存: `if (browser)` → `browser.preserveLayers()`

## AsyncTabSwitcher.evictOldestTabFromCache()
- 位置: L1030-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cleanUpTabAfterEviction()`, `this.tabLayerCache.shift()`

## AsyncTabSwitcher.maybePromoteTabInLayerCache()
- 位置: L1035-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( lazy.gTabCacheSize > 1 && tab.linkedBrowser.isRemoteBrowser && tab.linkedBrowser.currentURI.spec != "about:blank" )` → `this.tabLayerCache.indexOf()`
- 条件付き依存: `if (tabIndex != -1)` → `this.tabLayerCache.splice()`
- 条件付き依存: `if ( lazy.gTabCacheSize > 1 && tab.linkedBrowser.isRemoteBrowser && tab.linkedBrowser.currentURI.spec != "about:blank" )` → `this.tabLayerCache.push()`
- 条件付き依存: `if (this.tabLayerCache.length > lazy.gTabCacheSize)` → `this.evictOldestTabFromCache()`

## AsyncTabSwitcher.requestTab()
- 位置: L1056-1089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `oldBrowser.deprioritize()`, `tab.linkedBrowser.setAttribute()`, `this.getTabState()`, `this.logState()`, `this.queueUnload()`, `this.startTabSwitch()`, `this.tinfo()`
- 条件付き依存: `if (tabState == this.STATE_LOADED)` → `this.maybeVisibleTabs.clear()`
- 条件付き依存: `if (this.lastPrimaryTab && this.lastPrimaryTab != tab)` → `this.lastPrimaryTab.linkedBrowser.removeAttribute()`

## AsyncTabSwitcher.queueUnload()
- 位置: L1091-1093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleEvent()`

## AsyncTabSwitcher.onQueueUnload()
- 位置: L1095-1103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleEvent()`, `this.setTimer()`
- 条件付き依存: `if (this.unloadTimer)` → `this.clearTimer()`

## AsyncTabSwitcher.handleEvent()
- 位置: L1105-1178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onEndSwapDocShells()`, `this.onLayersCleared()`, `this.onLayersReady()`, `this.onLoadTimeout()`, `this.onPaint()`, `this.onQueueUnload()`, `this.onRemotenessChange()`, `this.onSwapDocShells()`, `this.onTabDiscardedImpl()`, `this.onTabRemovedImpl()`, `this.onUnloadTimeout()`, `this.onVisibilityChange()`, `this.postActions()`, `this.preActions()`
- 条件付き依存: `if (this._processing)` → `this.setTimer()`
- 条件付き依存: `if (this._processing)` → `this.handleEvent()`

## AsyncTabSwitcher.startTabSwitch()
- 位置: L1185-1188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.noteStartTabSwitch()`

## AsyncTabSwitcher.maybeFinishTabSwitch()
- 位置: L1196-1218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabState()`
- 条件付き依存: `if (this.requestedTab !== this.blankTab)` → `this.maybePromoteTabInLayerCache()`
- 条件付き依存: `if ( this.switchInProgress && this.requestedTab && (this.getTabState(this.requestedTab) == this.STATE_LOADED || this.requestedTab === this.blankTab) )` → `this.noteFinishTabSwitch()`
- 条件付き依存: `if ( this.switchInProgress && this.requestedTab && (this.getTabState(this.requestedTab) == this.STATE_LOADED || this.requestedTab === this.blankTab) )` → `this.tabbrowser.dispatchEvent()`

## AsyncTabSwitcher.logging()
- 位置: L1223-1237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## AsyncTabSwitcher.tinfo()
- 位置: L1239-1244
- 役割: (未記入)
- 触るとき: (未記入)

## AsyncTabSwitcher.log()
- 位置: L1246-1255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logging()`
- 条件付き依存: `if (this._useDumpForLogging)` → `dump()`
- 条件付き依存: `if (!(this._useDumpForLogging))` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## AsyncTabSwitcher.addLogFlag()
- 位置: L1257-1264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logging()`
- 条件付き依存: `if (subFlags.length)` → `subFlags.map(f => (f ? 1 : 0)).join()`
- 条件付き依存: `if (subFlags.length)` → `subFlags.map()`
- 条件付き依存: `if (this.logging())` → `this._logFlags.push()`

## AsyncTabSwitcher.logState()
- 位置: L1266-1407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabString()`, `this.logging()`, `this.tabbrowser.tabs.map()`
- 条件付き依存: `if (lastMatch == i - 1)` → `unloadedTabsStrings.push()`
- 条件付き依存: `if (lastMatch == i - 1)` → `lastMatch.toString()`
- 条件付き依存: `if (!(lastMatch == i - 1))` → `unloadedTabsStrings.push()`
- 条件付き依存: `if (unloadedTabsStrings.length)` → `unloadedTabsStrings.join()`
- 条件付き依存: `if (this._logFlags.length)` → `this._logFlags.join()`
- 条件付き依存: `if (this._useDumpForLogging)` → `dump()`
- 条件付き依存: `if (!(this._useDumpForLogging))` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## getTabString()
- 位置: L1271-1344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PictureInPicture.isOriginatingBrowser()`, `this.getTabState()`, `this.maybeVisibleTabs.has()`, `this.tabLayerCache.includes()`, `this.warmingTabs.has()`

## AsyncTabSwitcher.noteMakingTabVisibleWithoutLayers()
- 位置: L1409-1418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.performanceInteraction.tabSwitchComposite.cancel()`

## AsyncTabSwitcher.notePaint()
- 位置: L1420-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._tabswitchCompositeTimerId)` → `Glean.performanceInteraction.tabSwitchComposite.stopAndAccumulate()`
- 条件付き依存: `if (this.switchPaintId != -1 && event.transactionId >= this.switchPaintId)` → `ChromeUtils.addProfilerMarker()`

## AsyncTabSwitcher.noteStartTabSwitch()
- 位置: L1436-1451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.browserTabswitch.total.start()`, `Glean.performanceInteraction.tabSwitchComposite.start()`
- 条件付き依存: `if (this._tabswitchTotalTimerId)` → `Glean.browserTabswitch.total.cancel()`
- 条件付き依存: `if (this._tabswitchCompositeTimerId)` → `Glean.performanceInteraction.tabSwitchComposite.cancel()`

## AsyncTabSwitcher.noteFinishTabSwitch()
- 位置: L1453-1464
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._tabswitchTotalTimerId)` → `Glean.browserTabswitch.total.stopAndAccumulate()`
- 条件付き依存: `if (this._tabswitchTotalTimerId)` → `ChromeUtils.addProfilerMarker()`

## AsyncTabSwitcher.noteSpinnerDisplayed()
- 位置: L1466-1482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.browserTabswitch.spinnerVisible.start()`, `Glean.browserTabswitch.spinnerVisibleTrigger[this._loadTimerClearedBy].add()`, `this.assert()`
- 条件付き依存: `if (AppConstants.NIGHTLY_BUILD)` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## AsyncTabSwitcher.noteSpinnerHidden()
- 位置: L1484-1497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.browserTabswitch.spinnerVisible.stopAndAccumulate()`, `this.assert()`, `this.log()`
