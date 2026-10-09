# browser/components/sessionstore/SessionStore.sys.mjs

source: browser/components/sessionstore/SessionStore.sys.mjs
source-hash: 9fa4c8e8ccd31587442cec02e0563099dc65cd51
lines: 9611

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Date.now()`, `Promise.withResolvers()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.declareLazy()`

## blankURI()
- 位置: L365-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- XPCOM: `Services.io`

## _SessionStore.resetNextClosedId()
- 位置: L402-404
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#nextClosedId`

## _SessionStore.getNextSplitViewId()
- 位置: L512-518
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Number.MAX_SAFE_INTEGER`, `this.#maxSplitViewId`

## _SessionStore.savedGroups()
- 位置: L530-532
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#savedGroups`

## _SessionStore.shouldRestoreLastSession()
- 位置: L556-558
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#shouldRestoreLastSession`

## _SessionStore.#removeClosedAction()
- 位置: L586-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lastClosedActions.findIndex()`
- 条件付き依存: `if (closedActionIndex > -1)` → `this.#lastClosedActions.splice()`
- 参照: `obj.closedId`, `obj.type`

## _SessionStore.#addClosedAction()
- 位置: L604-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lastClosedActions.push()`
- 条件付き依存: `if (this.#lastClosedActions.length > maxLength)` → `this.#lastClosedActions.slice()`
- 参照: `this.#lastClosedActions`, `this.#lastClosedActions.length`, `this.#max_tabs_undo`, `this.#max_windows_undo`

## _SessionStore.lastClosedActions()
- 位置: L621-623
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastClosedActions`

## _SessionStore.popLastClosedAction()
- 位置: L633-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lastClosedActions.pop()`

## _SessionStore.resetLastClosedActions()
- 位置: L640-642
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastClosedActions`

## _SessionStore.logger()
- 位置: L655-657
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#log`

## _SessionStore.promiseAllWindowsRestored()
- 位置: L684-686
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#deferredAllWindowsRestored.promise`

## _SessionStore.promiseInitialized()
- 位置: L698-700
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#deferredInitialized.promise`

## _SessionStore.canRestoreLastSession()
- 位置: L708-710
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `LastSession.canRestore`

## _SessionStore.canRestoreLastSession()
- 位置: L712-716
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!val)` → `LastSession.clear()`

## _SessionStore.lastClosedObjectType()
- 位置: L723-743
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#closedWindows.length)` → `Services.wm.getEnumerator()`
- 条件付き依存: `if (this.#closedWindows.length)` → `this.#windowIds.get()`
- 条件付き依存: `if (windowState && windowState._closedTabs[0])` → `tabTimestamps.push()`
- 条件付き依存: `if (this.#closedWindows.length)` → `tabTimestamps.sort()`
- 参照: `tabTimestamps.length`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[0].closedAt`, `this.#windows`, `this.LAST_ACTION_CLOSED_TAB`, `this.LAST_ACTION_CLOSED_WINDOW`, `windowState._closedTabs`, `windowState._closedTabs[0].closedAt`
- XPCOM: `Services.wm`

## _SessionStore.willAutoRestore()
- 位置: L749-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`
- 参照: `PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.prefs`

## _SessionStore.init()
- 位置: L761-779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.startupTimeline.sessionRestoreInitialized.set()`, `Services.obs.addObserver()`, `Services.telemetry.msSinceProcessStart()`, `this.#initPrefs()`, `this.#log.debug()`, `this.promiseAllWindowsRestored.finally()`
- 参照: `this.#initialized`
- XPCOM: `Services.obs` / `Services.telemetry`

## _SessionStore.#initSession()
- 位置: L784-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.startupInitSession.start()`, `Glean.sessionRestore.startupInitSession.stopAndAccumulate()`, `ss.willRestore()`, `this.#log.debug()`, `this.#prefBranch.getBoolPref()`, `this.#recordSessionDecision()`
- 条件付き依存: `if (state)` → `this.#initSplitViewIds()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `this.#prepDataForDeferredRestore()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `iniState.windows.some()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `this.#log.debug()`
- 条件付き依存: `if (remainingState.windows.length)` → `LastSession.setState()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `Glean.browserEngagement.sessionrestoreInterstitial.deferred_restore.add()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `LastSession.setState()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `ss.willRestoreAsCrashed()`
- 条件付き依存: `if (restoreAsCrashed)` → `this.#log.debug()`
- 条件付き依存: `if (restoreAsCrashed)` → `this.#needsRestorePage()`
- 条件付き依存: `if (decision.interstitialReason)` → `Glean.browserEngagement.sessionrestoreInterstitial[ `shown_${decision.interstitialReason}` ].add()`
- 条件付き依存: `if (decision.interstitialReason)` → `this.#log.debug()`
- 条件付き依存: `if (!(decision.interstitialReason))` → `this.#hasSingleTabWithURL()`
- 条件付き依存: `if ( this.#hasSingleTabWithURL(state.windows, "about:welcomeback") )` → `this.#log.debug()`
- 条件付き依存: `if ( this.#hasSingleTabWithURL(state.windows, "about:welcomeback") )` → `Glean.browserEngagement.sessionrestoreInterstitial.shown_only_about_welcomeback.add()`
- 条件付き依存: `if (!restoreAsCrashed)` → `Glean.browserEngagement.sessionrestoreInterstitial.autorestore.add()`
- 条件付き依存: `if (!restoreAsCrashed)` → `this.#log.debug()`
- 条件付き依存: `if (!restoreAsCrashed)` → `this.#removeExplicitlyClosedTabs()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `this.#updateSessionStartTime()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `state.windows.forEach()`
- 条件付き依存: `if (state)` → `state?.windows?.forEach()`
- 条件付き依存: `if (state)` → `state?._closedWindows?.forEach()`
- 条件付き依存: `if (state)` → `this.#log.error()`
- 条件付き依存: `if ( !lazy.RunState.isQuitting && this.#prefBranch.getBoolPref("sessionstore.resume_session_once") )` → `this.#prefBranch.setBoolPref()`
- 参照: `Glean.browserEngagement.sessionrestoreInterstitial`, `aWindow.__lastSessionWindowID`, `decision.action`, `decision.initError`, `decision.interstitialReason`, `ex.name`, `iniState.savedGroups`, `iniState.savedGroups.length`, `iniState.windows.length`, `lazy.E10SUtils.SERIALIZED_SYSTEMPRINCIPAL`, `lazy.RunState.isQuitting`, `lazy.SessionStartup`, `remainingState.windows.length`, `ss.DEFER_SESSION`, `ss.RESUME_SESSION`, `ss.previousSessionCrashed`, `ss.sessionType`, `ss.state`, `state.lastSessionState`, `state.savedGroups`, `state.session`, `state.session.recentCrashes`, `state.windows`, `state.windows.length`, `state.windows[0].sizemode`, `state.windows[0].tabs`, `state.windows[0].tabs[0].entries`, `state.windows[0].tabs[0].entries[0].triggeringPrincipal_base64`, `state.windows[0].tabs[0].entries[0].url`, `state?.savedGroups`, `this.#isUserConfiguredRestore`, `this.#recentCrashes`, `this.#savedGroups`, `win._maybeDontRestoreTabs`, `win.tabs.length`

## _SessionStore.#recordSessionDecision()
- 位置: L980-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.startupSessionDecision.record()`, `this.#log.debug()`
- 参照: `PrivateBrowsingUtils.permanentPrivateBrowsing`, `Services.appinfo.restartedByOS`, `decision.action`, `decision.initError`, `decision.interstitialReason`, `extra.init_error`, `extra.interstitial_reason`, `extra.previous_session_crashed`, `extra.resume_reason`, `ss.DEFER_SESSION`, `ss.NO_SESSION`, `ss.RECOVER_SESSION`, `ss.RESUME_SESSION`, `ss.previousSessionCrashed`, `ss.sessionType`
- XPCOM: `Services.appinfo`

## _SessionStore.#removeExplicitlyClosedTabs()
- 位置: L1030-1080
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (state.windows.length == 1)` → `winData.tabs.pop()`
- 条件付き依存: `if (state.windows.length == 1)` → `this.historyIndex()`
- 条件付き依存: `if (state.windows.length == 1)` → `Math.min()`
- 条件付き依存: `if (state.windows.length == 1)` → `Math.max()`
- 条件付き依存: `if (state.windows.length == 1)` → `Date.now()`
- 条件付き依存: `if (state.windows.length == 1)` → `this.#shouldSaveTabState()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.#saveClosedTabData()`
- 条件付き依存: `if (!(state.windows.length == 1))` → `winData.tabs.some()`
- 条件付き依存: `if (winData.tabs.some(this.#shouldSaveTabState))` → `Date.now()`
- 条件付き依存: `if (winData.tabs.some(this.#shouldSaveTabState))` → `state._closedWindows.unshift()`
- 条件付き依存: `if (!(state.windows.length == 1))` → `state.windows.splice()`
- 参照: `state.windows`, `state.windows.length`, `tabState.entries`, `tabState.entries.length`, `tabState.entries[activeIndex].title`, `tabState.entries[activeIndex].url`, `tabState.image`, `this.#shouldSaveTabState`, `winData._closedTabs`, `winData._lastClosedTabGroupCount`, `winData._maybeDontRestoreTabs`, `winData.closedAt`, `winData.tabs.length`

## _SessionStore.#initPrefs()
- 位置: L1091-1139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.newTabOnRestoreEnabled.set()`, `Services.prefs.addObserver()`, `Services.prefs.getBranch()`, `this.#prefBranch.addObserver()`, `this.#prefBranch.getBoolPref()`, `this.#prefBranch.getIntPref()`
- 参照: `lazy.sessionStoreLogger`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedTabsFromClosedWindowsEnabled`, `this.#log`, `this.#max_tabs_undo`, `this.#max_windows_undo`, `this.#prefBranch`, `this.#restore_on_demand`
- XPCOM: `Services.prefs`

## _SessionStore.#uninit()
- 位置: L1145-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabRestoreQueue.reset()`, `lazy.RunState.setClosing()`, `lazy.SessionSaver.cancel()`
- 条件付き依存: `if (this.#sessionInitialized)` → `lazy.SessionSaver.run()`
- 参照: `this.#initialized`, `this.#sessionInitialized`

## _SessionStore.observe()
- 位置: L1175-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `this.#notifyOfClosedObjectsChange()`, `this.#onBeforeBrowserWindowShown()`, `this.#onClose()`, `this.#onClose(/** @type {ChromeWindow} */ (aSubject)).then()`, `this.#onFinalTabStateUpdateComplete()`, `this.#onIdleDaily()`, `this.#onLastWindowCloseGranted()`, `this.#onPrefChange()`, `this.#onPurgeDomainData()`, `this.#onPurgeSessionHistory()`, `this.#onQuitApplication()`, `this.#onQuitApplicationGranted()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (userContextId)` → `this.#forgetTabsWithUserContextId()`
- 条件付き依存: `if (permanentKey)` → `this.#maybeRecreateSHistoryListener()`
- 条件付き依存: `if (permanentKey)` → `this.#browserSHistoryListener.get(permanentKey)?.unregister()`
- 条件付き依存: `if (permanentKey)` → `this.#browserSHistoryListener.get()`
- 参照: `( browsingContext.embedderElement )?.permanentKey`, `( browsingContext?.embedderElement )?.permanentKey`, `JSON.parse(aData).userContextId`, `browsingContext.embedderElement`, `browsingContext.isContent`, `browsingContext.top`, `browsingContext?.embedderElement`
- XPCOM: `Services.obs`

## _SessionStore.#getOrCreateSHistoryListener()
- 位置: L1265-1276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserSHistoryListener.get()`, `this.#createSHistoryListener()`
- 参照: `browsingContext.top`

## _SessionStore.#maybeRecreateSHistoryListener()
- 位置: L1282-1288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserSHistoryListener.get()`
- 条件付き依存: `if (!listener || listener._browserId != browsingContext.browserId)` → `listener?.unregister()`
- 条件付き依存: `if (!listener || listener._browserId != browsingContext.browserId)` → `this.#createSHistoryListener()`
- 参照: `browsingContext.browserId`, `listener._browserId`

## _SessionStore.#createSHistoryListener()
- 位置: L1290-1417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sessionHistory.addSHistoryListener()`, `this.#browserSHistoryListener.set()`
- 条件付き依存: `if (collectImmediately && (!isAboutBlank || sessionHistory.count !== 0))` → `listener.collect()`
- 参照: `browsingContext.currentURI?.spec`, `browsingContext.sessionHistory`, `sessionHistory.count`

## SHistoryListener.constructor()
- 位置: L1296-1304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`
- 参照: `browsingContext.browserId`, `this.QueryInterface`, `this._browserId`, `this._fromIndex`

## SHistoryListener.unregister()
- 位置: L1306-1312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`, `SessionStore.#browserSHistoryListener.delete()`, `bc?.sessionHistory?.removeSHistoryListener()`
- 参照: `this._browserId`

## SHistoryListener.collect()
- 位置: L1314-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.collectSessionHistory.start()`, `Glean.sessionRestore.collectSessionHistory.stopAndAccumulate()`, `lazy.SessionHistory.collectFromParent()`
- 条件付き依存: `if (writeToCache)` → `SessionStore.#onTabStateUpdate()`
- 参照: `browsingContext.currentURI?.spec`, `browsingContext.currentWindowGlobal?.browsingContext?.window`, `browsingContext.embedderElement?.documentGlobal`, `browsingContext.sessionHistory`, `this._fromIndex`

## SHistoryListener.collectFrom()
- 位置: L1351-1374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`
- 条件付き依存: `if (bc?.embedderElement?.frameLoader)` → `bc.embedderElement.frameLoader.requestSHistoryUpdate()`
- 参照: `bc?.embedderElement?.frameLoader`, `this._browserId`, `this._fromIndex`

## SHistoryListener.OnHistoryNewEntry()
- 位置: L1376-1381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryGotoIndex()
- 位置: L1382-1384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryPurge()
- 位置: L1385-1387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryReload()
- 位置: L1388-1391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryReplaceEntry()
- 位置: L1392-1394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryTruncate()
- 位置: L1395-1395
- 役割: (未記入)
- 触るとき: (未記入)

## SHistoryListener.OnDocumentViewerEvicted()
- 位置: L1396-1396
- 役割: (未記入)
- 触るとき: (未記入)

## SHistoryListener.OnHistoryCommit()
- 位置: L1397-1397
- 役割: (未記入)
- 触るとき: (未記入)

## SHistoryListener.OnEntryUpdated()
- 位置: L1398-1398
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.#onTabStateUpdate()
- 位置: L1419-1438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabState.update()`, `this.#closingTabMap.get()`, `this.#crashedBrowsers.has()`, `this.#saveStateDelayed()`
- 条件付き依存: `if (closedTab)` → `lazy.TabState.copyFromCache()`
- 参照: `closedTab.tabData.state`

## _SessionStore.#onFinalTabStateUpdateComplete()
- 位置: L1443-1491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.TabStateFlusher.resolveAll()`, `this.#browserSHistoryListener.get()`, `this.#browserSHistoryListener.get(permanentKey)?.unregister()`, `this.#closingTabMap.has()`, `this.#crashedBrowsers.has()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(permanentKey)?.unregister()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#closingTabMap.get()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#closingTabMap.delete()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#shouldSaveTabState()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `closedTabs.indexOf()`
- 条件付き依存: `if (shouldSave && index == -1)` → `this.#saveClosedTabData()`
- 条件付き依存: `if (!shouldSave && index > -1)` → `this.#removeClosedTabData()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#cleanupOrphanedClosedGroups()`
- 参照: `browser.permanentKey`, `tabData.permanentKey`, `tabData.state`
- XPCOM: `Services.obs`

## _SessionStore.updateSessionStoreFromChild()
- 位置: L1509-1558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getOrCreateSHistoryListener()`, `this.#isCurrentEpoch()`, `this.#onTabStateUpdate()`
- 条件付き依存: `if (listener)` → `lazy.SessionHistory.collectNonWebControlledLoadingSession()`
- 条件付き依存: `if (listener)` → `listener.collect()`
- 参照: `browser?.documentGlobal`, `browser?.permanentKey`, `browsingContext.currentWindowGlobal?.browsingContext?.window`, `browsingContext.isReplaced`, `update.data.historychange`, `update.epoch`, `update.sHistoryNeeded`

## _SessionStore.handleEvent()
- 位置: L1568-1670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearRestoringWindows()`, `this.#maybeRestoreTabContent()`, `this.#notifyOfClosedObjectsChange()`, `this.#onTabAdd()`, `this.#onTabBrowserInserted()`, `this.#onTabHide()`, `this.#onTabRemove()`, `this.#onTabSelect()`, `this.#onTabShow()`, `this.#saveStateDelayed()`
- 条件付き依存: `if (detail.adoptedTab)` → `this.#moveCustomTabValue()`
- 条件付き依存: `if (detail.adoptedBy)` → `this.#moveCustomTabValue()`
- 条件付き依存: `if (detail.adoptedBy)` → `this.#onMoveToNewWindow()`
- 条件付き依存: `if (!detail.skipSessionStore)` → `this.#onTabClose()`
- 条件付き依存: `if (!(/** @type {CustomEvent} */ (aEvent).detail?.skipSessionStore))` → `this.#onTabGroupRemoveRequested()`
- 条件付き依存: `if (!(/** @type {CustomEvent} */ (aEvent).detail?.skipSessionStore))` → `this.#notifyOfClosedObjectsChange()`
- 条件付き依存: `if (/** @type {FrameCrashedEvent} */ (aEvent).isTopFrame)` → `this.#onBrowserCrashed()`
- 条件付き依存: `if ( browser.namespaceURI == XUL_NS && browser.localName == "browser" && browser.frameLoader && browser.permanentKey )` → `this.#resetEpoch()`
- 参照: `(aEvent).detail.tabs`, `(aEvent).detail?.skipSessionStore`, `(aEvent).isTopFrame`, `(aEvent.currentTarget).documentGlobal`, `aEvent.currentTarget`, `aEvent.originalTarget`, `aEvent.type`, `browser.frameLoader`, `browser.localName`, `browser.namespaceURI`, `browser.permanentKey`, `detail.adoptedBy`, `detail.adoptedBy.linkedBrowser`, `detail.adoptedTab`, `detail.inMultiselection`, `detail.skipSessionStore`, `tab.linkedBrowser`

## _SessionStore.#generateWindowID()
- 位置: L1678-1680
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#nextWindowID`

## _SessionStore.ensureInitialized()
- 位置: L1688-1697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#sessionInitialized && !this.#windowIds.has(window))` → `this.#onLoad()`
- 参照: `this.#sessionInitialized`

## _SessionStore.#onLoad()
- 位置: L1705-1791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `aWindow.docShell.treeOwner .QueryInterface()`, `aWindow.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `aWindow.document.documentElement.hasAttribute()`, `aWindow.gBrowser.addEventListener()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `tabbrowser.tabContainer.addEventListener()`, `this.#generateWindowID()`, `this.#isWindowLoaded()`, `this.#onTabBrowserInserted()`, `this.#windowIds.get()`, `this.#windowIds.set()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!aWindow.toolbar.visible)` → `this.#windowIds.get()`
- 条件付き依存: `if (aWindow.document.documentElement.hasAttribute("taskbartab"))` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActiveAndEnabled(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (aWindow.document.documentElement.hasAttribute(ARG_CHROMELESS_WINDOW))` → `this.#windowIds.get()`
- 条件付き依存: `if ( aWindow.document.documentElement.hasAttribute( ARG_WEB_EXTENSION_POPUP_WINDOW ) )` → `this.#windowIds.get()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `aWindow.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow).chromeFlags`, `aWindow.gBrowser`, `aWindow.toolbar.visible`, `lazy.RunState.isQuitting`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._restoring`, `this.#windows[this.#windowIds.get(aWindow)].args`, `this.#windows[this.#windowIds.get(aWindow)].isAIWindow`, `this.#windows[this.#windowIds.get(aWindow)].isPopup`, `this.#windows[this.#windowIds.get(aWindow)].isPrivate`, `this.#windows[this.#windowIds.get(aWindow)].isTaskbarTab`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md)

## _SessionStore.#initializeWindow()
- 位置: L1805-2007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isStopped)` → `lazy.RunState.setRunning()`
- 条件付き依存: `if (aInitialState)` → `lazy.SessionSaver.updateLastSaveTime()`
- 条件付き依存: `if (isPrivateWindow || isTaskbarTab)` → `this.#log.debug()`
- 条件付き依存: `if (isPrivateWindow || isTaskbarTab)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (isPrivateWindow || isTaskbarTab)` → `this.#deferredAllWindowsRestored.resolve()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `Glean.sessionRestore.startupTimeline.sessionRestoreRestoring.set()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `Services.telemetry.msSinceProcessStart()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `this.#globalState.setFromState()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `lazy.SessionCookies.restore()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `this.#isCmdLineEmpty()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `this.#restoreWindows()`
- 条件付き依存: `if (!(aInitialState))` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(aInitialState))` → `this.#deferredAllWindowsRestored.resolve()`
- 条件付き依存: `if (!(lazy.RunState.isStopped))` → `this.#isWindowLoaded()`
- 条件付き依存: `if (this.#deferredInitialState && isRegularWindow)` → `lazy.SessionStartup.willRestore()`
- 条件付き依存: `if (lazy.SessionStartup.willRestore())` → `this.#globalState.setFromState()`
- 条件付き依存: `if (lazy.SessionStartup.willRestore())` → `this.#restoreWindows()`
- 条件付き依存: `if (closedWindowState)` → `lazy.SessionStartup.willRestore()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" || !lazy.SessionStartup.willRestore() )` → `this.#prepDataForDeferredRestore()`
- 条件付き依存: `if (!normalTabsState.windows.length)` → `this.#removeClosedWindow()`
- 条件付き依存: `if (!( AppConstants.platform == "macosx" || !lazy.SessionStartup.willRestore() ))` → `this.#removeClosedWindow()`
- 条件付き依存: `if (newWindowState)` → `this.#isCmdLineEmpty()`
- 条件付き依存: `if (newWindowState)` → `this.#restoreWindow()`
- 条件付き依存: `if (newWindowState)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if ( this.#restoreLastWindow && aWindow.toolbar.visible && this.#closedWindows.length && !isPrivateWindow )` → `this.#prefBranch.setBoolPref()`
- 条件付き依存: `if (!( this.#restoreLastWindow && aWindow.toolbar.visible && this.#closedWindows.length && !isPrivateWindow ))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `LastSession.getState()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `this.#globalState.setFromState()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `lazy.SessionCookies.restore()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `this.#restoreWindows()`
- 参照: `AppConstants.platform`, `aInitialState.cookies`, `aInitialState.windows`, `aInitialState.windows.length`, `aWindow.toolbar.visible`, `appTabsState.windows`, `appTabsState.windows.length`, `lastSessionState.cookies`, `lazy.RunState.isStopped`, `lazy.SessionStartup.state`, `newWindowState.__lastSessionWindowID`, `normalTabsState.windows`, `normalTabsState.windows.length`, `normalTabsState.windows[0].__lastSessionWindowID`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[i].isPopup`, `this.#cmdLineHadURLOnStartup`, `this.#deferredInitialState`, `this.#deferredInitialState.windows`, `this.#deferredInitialState.windows.length`, `this.#isUserConfiguredRestore`, `this.#restoreCount`, `this.#restoreLastWindow`, `this.#shouldRestoreLastSession`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].isTaskbarTab`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.telemetry`

## _SessionStore.#onBeforeBrowserWindowShown()
- 位置: L2015-2113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WINDOW_SHOWING_PROMISES.get()`, `aWindow.document.documentElement.hasAttribute()`, `this.#log.error()`, `this.#onLoad()`, `this.#promiseReadyForInitialization .then()`
- 条件付き依存: `if (deferred)` → `deferred.resolve()`
- 条件付き依存: `if (deferred)` → `WINDOW_SHOWING_PROMISES.delete()`
- 条件付き依存: `if (this.#sessionInitialized)` → `this.#log.debug()`
- 条件付き依存: `if (this.#sessionInitialized)` → `this.#initializeWindow()`
- 条件付き依存: `if (!this.#promiseReadyForInitialization)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.#promiseReadyForInitialization)` → `Promise.all()`
- 条件付き依存: `if (aWindow.closed)` → `this.#log.debug()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `this.#initSession()`
- 条件付き依存: `if (initialState)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `Glean.sessionRestore.startupOnloadInitialWindow.start()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `this.#initializeWindow()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `Glean.sessionRestore.startupOnloadInitialWindow.stopAndAccumulate()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `this.#deferredInitialized.resolve()`
- 参照: `aWindow.browsingContext.isDocumentPiP`, `aWindow.closed`, `lazy.SessionStartup.onceInitialized`, `this.#promiseReadyForInitialization`, `this.#sessionInitialized`
- XPCOM: `Services.obs`

## obs()
- 位置: L2057-2062
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWindow == subject)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aWindow == subject)` → `resolve()`
- XPCOM: `Services.obs`

## _SessionStore.#onClose()
- 位置: L2125-2323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Promise.resolve()`, `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `aWindow.gBrowser.removeEventListener()`, `event.initEvent()`, `tabbrowser.tabContainer.removeEventListener()`, `this.#isWindowLoaded()`, `this.#onTabRemove()`, `this.#windowIds.get()`
- 条件付き依存: `if (!isFullyLoaded)` → `this.#windowIds.has()`
- 条件付き依存: `if (!this.#windowIds.has(aWindow))` → `this.#windowIds.set()`
- 条件付き依存: `if (!this.#windowIds.has(aWindow))` → `this.#generateWindowID()`
- 条件付き依存: `if (!isFullyLoaded)` → `WINDOW_RESTORE_IDS.get()`
- 条件付き依存: `if (!isFullyLoaded)` → `this.#windowIds.get()`
- 条件付き依存: `if (!isFullyLoaded)` → `WINDOW_RESTORE_IDS.delete()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#collectWindowData()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#tabClosingByWindowMap.set()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Date.now()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#isLastRestorableWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Object.values(this.#windows).filter()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Object.values()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#log.debug()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Object.values(this.#windows).some()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(this.willAutoRestore))` → `Services.obs.notifyObservers()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && isLastRegularWindow && !winData.isTaskbarTab && !winData.isPrivate && taskbarTabsRemains )` → `this.getCurrentState()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && isLastRegularWindow && !winData.isTaskbarTab && !winData.isPrivate && taskbarTabsRemains )` → `lazy.PrivacyFilter.filterPrivateWindowsAndTabs()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && isLastRegularWindow && !winData.isTaskbarTab && !winData.isPrivate && taskbarTabsRemains )` → `LastSession.setState()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#saveableClosedWindowData.add()`
- 条件付き依存: `if (!winData.isPrivate && !winData.isTaskbarTab)` → `this.#maybeSaveClosedWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.TabStateFlusher.flushWindow(aWindow).then()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.TabStateFlusher.flushWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `WINDOW_FLUSHING_PROMISES.delete()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#tabClosingByWindowMap.has()`
- 条件付き依存: `if (this.#tabClosingByWindowMap.has(browser.permanentKey))` → `this.#tabClosingByWindowMap.get()`
- 条件付き依存: `if (this.#tabClosingByWindowMap.has(browser.permanentKey))` → `lazy.TabState.copyFromCache()`
- 条件付き依存: `if (this.#tabClosingByWindowMap.has(browser.permanentKey))` → `this.#tabClosingByWindowMap.delete()`
- 条件付き依存: `if (!isLastWindow && winData.closedId > -1)` → `this.#addClosedAction()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#cleanUpWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#saveStateDelayed()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `WINDOW_FLUSHING_PROMISES.set()`
- 条件付き依存: `if (!(lazy.RunState.isRunning))` → `this.#cleanUpWindow()`
- 参照: `AppConstants.platform`, `Object.values(this.#windows).filter( wData => !wData.isPrivate && !wData.isTaskbarTab ).length`, `aWindow.gBrowser`, `browser.permanentKey`, `lazy.RunState.isRunning`, `tab.linkedBrowser.permanentKey`, `tabbrowser.browsers`, `tabbrowser.selectedBrowser.contentTitle`, `tabbrowser.selectedTab.label`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `this.#restoreWithoutRestart`, `this.#shouldRestoreLastSession`, `this.#statesToRestore`, `this.#statesToRestore[restoreID].windows`, `this.#windowToFocus`, `this.#windows`, `this.LAST_ACTION_CLOSED_WINDOW`, `this.willAutoRestore`, `wData.isPrivate`, `wData.isTaskbarTab`, `winData._shouldRestore`, `winData.busy`, `winData.closedAt`, `winData.closedId`, `winData.isPrivate`, `winData.isTaskbarTab`, `winData.title`
- XPCOM: `Services.obs` / `Services.prefs`

## _SessionStore.#cleanUpWindow()
- 位置: L2340-2352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DyingWindowCache.set()`, `lazy.TabStateFlusher.resolveAll()`, `this.#saveableClosedWindowData.delete()`, `this.#windowIds.delete()`

## _SessionStore.#maybeSaveClosedWindow()
- 位置: L2371-2447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#saveableClosedWindowData.has()`
- 条件付き依存: `if ( lazy.RunState.isRunning && this.#saveableClosedWindowData.has(winData) )` → `winData.tabs.some()`
- 条件付き依存: `if ( lazy.RunState.isRunning && this.#saveableClosedWindowData.has(winData) )` → `this.#closedWindows.indexOf()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#closedWindows.findIndex()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#closedWindows.splice()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#capClosedWindows()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#saveOpenTabGroupsOnClose()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#log.debug()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" && this.#closedWindows.length == 1 )` → `window.document.getElementById()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" && this.#closedWindows.length == 1 )` → `historyMenu.menupopup.dispatchEvent()`
- 条件付き依存: `if (alreadyStored)` → `this.#removeClosedWindow()`
- 条件付き依存: `if (!shouldStore)` → `this.#log.warn()`
- 参照: `AppConstants.platform`, `Services.appShell.hiddenDOMWindow`, `lazy.RunState.isRunning`, `this.#closedObjectsChanged`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedWindows.length`, `this.#nextClosedId`, `this.#shouldSaveTabState`, `win.closedAt`, `winData._closedTabs.length`, `winData.closedAt`, `winData.closedId`, `winData.tabs.length`, `window.CustomEvent`
- XPCOM: `Services.appShell`

## _SessionStore.#saveOpenTabGroupsOnClose()
- 位置: L2464-2503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedWinData.groups.map()`, `lazy.TabGroupState.savedInClosedWindow()`, `newlySavedTabGroups.has()`, `newlySavedTabGroups.set()`, `newlySavedTabGroups.values()`, `this.#recordSavedTabGroupState()`, `this.#shouldSaveTabState()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.formatTabStateForSavedGroup()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `newlySavedTabGroups.get(tabState.groupId).tabs.push()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `newlySavedTabGroups.get()`
- 参照: `closedWinData.closedId`, `closedWinData.groups`, `closedWinData.tabs`, `closedWinData.tabs.length`, `tabGroupState.id`, `tabGroupState.saveOnWindowClose`, `tabState.groupId`

## _SessionStore.formatTabStateForSavedGroup()
- 位置: L2516-2533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `Math.min()`
- 参照: `tabState.entries`, `tabState.entries.length`, `tabState.entries[activeIndex].title`, `tabState.entries[activeIndex].url`, `tabState.image`, `tabState.index`, `this.#nextClosedId`

## _SessionStore.#onQuitApplicationGranted()
- 位置: L2543-2666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.RunState.setQuitting()`, `this.#collectWindowData()`, `this.#log.debug()`, `this.#windowIds.get()`
- 条件付き依存: `if (!syncShutdown)` → `Glean.sessionRestore.shutdownType.async.add()`
- 条件付き依存: `if (!syncShutdown)` → `this.#flushAllWindowsAsync()`
- 条件付き依存: `if (!syncShutdown)` → `Math.max()`
- 条件付き依存: `if (!syncShutdown)` → `this.#looseTimer()`
- 条件付き依存: `if (!syncShutdown)` → `observeTopic()`
- 条件付き依存: `if (!syncShutdown)` → `promises.push()`
- 条件付き依存: `if (!syncShutdown)` → `defers.map()`
- 条件付き依存: `if (!syncShutdown)` → `Promise.race(promises) .then()`
- 条件付き依存: `if (!syncShutdown)` → `Promise.race()`
- 条件付き依存: `if (!syncShutdown)` → `defers.forEach()`
- 条件付き依存: `if (!syncShutdown)` → `deferred.reject()`
- 条件付き依存: `if (!syncShutdown)` → `Services.tm.spinEventLoopUntil()`
- 条件付き依存: `if (!(!syncShutdown))` → `Glean.sessionRestore.shutdownType.sync.add()`
- 参照: `deferred.promise`, `lazy.AsyncShutdown.DELAY_CRASH_MS`, `lazy.SessionSaver.lastSaveTime`, `this.#orderedBrowserWindows`, `this.#windows`, `this.#windows[this.#windowIds.get(window)].zIndex`
- XPCOM: `Services.tm`

## observeTopic()
- 位置: L2591-2627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `deferred.promise.then()`
- XPCOM: `Services.obs`

## observer()
- 位置: L2593-2616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.shutdownFlushAllOutcomes.oop_frameloader_crashed.add()`, `deferred.resolve()`, `subject.QueryInterface()`, `subject.get()`, `this.#log.debug()`
- 条件付き依存: `if (subject.get("abnormal"))` → `this.#log.debug()`
- 条件付き依存: `if (subject.get("abnormal"))` → `Glean.sessionRestore.shutdownFlushAllOutcomes.abnormal_content_shutdown.add()`
- 条件付き依存: `if (subject.get("abnormal"))` → `deferred.resolve()`
- 参照: `Ci.nsIPropertyBag2`
- XPCOM: [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## cleanup()
- 位置: L2617-2623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this.#log.error()`
- XPCOM: `Services.obs`

## _SessionStore.#flushAllWindowsAsync()
- 位置: async L2686-2728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DirtyWindows.clear()`, `Glean.sessionRestore.shutdownFlushAllOutcomes.complete.add()`, `WINDOW_FLUSHING_PROMISES.clear()`, `lazy.TabStateFlusher.flushWindow()`, `this.#getTopWindow()`, `this.#windowIds.get()`, `window.docShell.treeOwner.QueryInterface()`, `windowPromises.set()`
- 条件付き依存: `if (this.#windowIds.get(win) && this.#windows[this.#windowIds.get(win)])` → `this.#collectWindowData()`
- 条件付き依存: `if (activeWindow)` → `this.#windowIds.get()`
- 参照: `Ci.nsIBaseWindow`, `baseWin.visibility`, `progress.current`, `progress.total`, `this.#activeWindowSSiCache`, `this.#browserWindows`, `this.#windows`, `windowPromises.size`
- XPCOM: `nsIBaseWindow`

## _SessionStore.#onLastWindowCloseGranted()
- 位置: L2733-2739
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#restoreLastWindow`

## _SessionStore.#onQuitApplication()
- 位置: L2747-2777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#uninit()`
- 条件付き依存: `if (!PrivateBrowsingUtils.permanentPrivateBrowsing)` → `this.#prefBranch.getBoolPref()`
- 条件付き依存: `if ( aData == "os-restart" && !this.#prefBranch.getBoolPref("sessionstore.resume_session_once") )` → `this.#prefBranch.setBoolPref()`
- 条件付き依存: `if (!PrivateBrowsingUtils.permanentPrivateBrowsing)` → `this.#prefBranch.setBoolPref()`
- 条件付き依存: `if (aData == "restart" || aData == "os-restart")` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aData != "restart")` → `LastSession.clear()`
- 参照: `PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.obs`

## _SessionStore.purgeDataForPrivateWindow()
- 位置: L2784-2821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.get()`
- 条件付き依存: `if (windowData._closedTabs.length)` → `this.#removeClosedTabData()`
- 条件付き依存: `if (windowData.closedGroups.length)` → `this.#removeClosedTabData()`
- 参照: `closedGroup.tabs`, `closedGroup.tabs.length`, `lazy.RunState.isQuitting`, `this.#closedObjectsChanged`, `this.#windows`, `windowData._closedTabs`, `windowData._closedTabs.length`, `windowData._lastClosedTabGroupCount`, `windowData.closedGroups`, `windowData.closedGroups.length`, `windowData.lastClosedTabGroupId`

## _SessionStore.#onPurgeSessionHistory()
- 位置: L2826-2873
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LastSession.clear()`, `lazy.SessionFile.wipe()`, `this.#clearRestoringWindows()`, `this.#getTopWindow()`, `this.#windowIds.get()`
- 条件付き依存: `if (win)` → `win.setTimeout()`
- 条件付き依存: `if (win)` → `lazy.SessionSaver.run()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.SessionSaver.run()`
- 参照: `lazy.RunState.isQuitting`, `lazy.RunState.isRunning`, `this.#browserWindows`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#lastClosedActions`, `this.#saveableClosedWindowData`, `this.#windows`, `this.#windows[ix]._closedTabs`, `this.#windows[ix]._closedTabs.length`, `this.#windows[ix].closedGroups`, `this.#windows[ix].closedGroups.length`

## _SessionStore.#onPurgeDomainData()
- 位置: L2881-2955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedTabs[i].state.entries.some()`, `openTabs[j].entries.some()`, `this.#clearRestoringWindows()`, `this.#closedWindows[ix].closedGroups.map()`, `this.#windows[ix].closedGroups.map()`
- 条件付き依存: `if (closedTabs[i].state.entries.some(containsDomain, this))` → `closedTabs.splice()`
- 条件付き依存: `if (openTabs[j].entries.some(containsDomain, this))` → `openTabs.splice()`
- 条件付き依存: `if (!openTabs.length)` → `this.#closedWindows.splice()`
- 条件付き依存: `if (openTabs.length != openTabCount)` → `this.historyIndex()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.SessionSaver.run()`
- 参照: `closedTabs.length`, `g.tabs`, `lazy.RunState.isRunning`, `openTabs.length`, `selectedTab.entries`, `selectedTab.entries.length`, `selectedTab.entries[activeIndex].title`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[ix]._closedTabs`, `this.#closedWindows[ix].selected`, `this.#closedWindows[ix].tabs`, `this.#closedWindows[ix].title`, `this.#windows`, `this.#windows[ix]._closedTabs`

## containsDomain()
- 位置: L2883-2894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `aEntry.children.some()`
- 参照: `Services.io.newURI(aEntry.url).host`, `aEntry.children`, `aEntry.url`
- XPCOM: `Services.eTLD` / `Services.io`

## _SessionStore.#onPrefChange()
- 位置: L2963-3010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.newTabOnRestoreEnabled.set()`, `this.#capClosedWindows()`, `this.#prefBranch.getBoolPref()`, `this.#prefBranch.getIntPref()`
- 条件付き依存: `if (this.#windows[ix]._closedTabs.length > this.#max_tabs_undo)` → `this.#windows[ix]._closedTabs.splice()`
- 参照: `this.#closedObjectsChanged`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedTabsFromClosedWindowsEnabled`, `this.#max_tabs_undo`, `this.#max_windows_undo`, `this.#restore_on_demand`, `this.#windows`, `this.#windows[ix]._closedTabs.length`

## _SessionStore.#onTabAdd()
- 位置: L3018-3020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#saveStateDelayed()`

## _SessionStore.#onTabBrowserInserted()
- 位置: L3030-3048
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_LAZY_STATES.delete()`, `TAB_LAZY_STATES.has()`, `TAB_STATE_FOR_BROWSER.has()`, `browser.addEventListener()`, `lazy.TabStateCache.get()`
- 条件付き依存: `if ( TAB_LAZY_STATES.has(aTab) && !TAB_STATE_FOR_BROWSER.has(browser) && lazy.TabStateCache.get(browser.permanentKey) )` → `lazy.TabState.clone()`
- 条件付き依存: `if ( TAB_LAZY_STATES.has(aTab) && !TAB_STATE_FOR_BROWSER.has(browser) && lazy.TabStateCache.get(browser.permanentKey) )` → `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if ( TAB_LAZY_STATES.has(aTab) && !TAB_STATE_FOR_BROWSER.has(browser) && lazy.TabStateCache.get(browser.permanentKey) )` → `this.#restoreTab()`
- 参照: `aTab.linkedBrowser`, `browser.permanentKey`

## _SessionStore.#onTabRemove()
- 位置: L3060-3066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cleanUpRemovedBrowser()`
- 条件付き依存: `if (!aNoNotification)` → `this.#saveStateDelayed()`

## _SessionStore.#onTabClose()
- 位置: L3078-3089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `lazy.TabState.collect()`, `this.#maybeSaveClosedTab()`
- 参照: `this.#max_tabs_undo`

## _SessionStore.#onTabGroupRemoveRequested()
- 位置: L3095-3127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedGroups.unshift()`, `lazy.TabGroupState.closed()`, `this.#collectClosedTabsForTabGroup()`, `this.#collectSplitViewDataForTabGroup()`, `this.#windowIds.get()`, `this.getSavedTabGroup()`
- 参照: `tabGroup.id`, `tabGroup.tabs`, `tabGroupState.splitViews`, `tabGroupState.tabs`, `tabGroupState.tabs.length`, `this.#closedObjectsChanged`, `this.#max_tabs_undo`, `this.#windows`, `this.#windows[this.#windowIds.get(win)]._lastClosedTabGroupCount`, `this.#windows[this.#windowIds.get(win)].closedGroups`

## _SessionStore.#collectClosedTabsForTabGroup()
- 位置: L3149-3162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `lazy.TabState.collect()`, `tabs.forEach()`, `this.#maybeSaveClosedTab()`
- 参照: `tabState.groupId`

## _SessionStore.#collectSplitViewDataForTabGroup()
- 位置: L3168-3178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `splitViewData.values()`, `tabs.forEach()`
- 条件付き依存: `if (tab.splitview)` → `splitViewData.get()`
- 条件付き依存: `if (!splitViewData.get(tab.splitview.splitViewId))` → `splitViewData.set()`
- 参照: `tab.splitview`, `tab.splitview.splitViewId`, `tab.splitview.state`

## _SessionStore.#onMoveToNewWindow()
- 位置: L3188-3198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabStateCache.get()`, `lazy.TabStateCache.update()`, `lazy.TabStateFlusher.flush()`, `lazy.TabStateFlusher.flush(aFromBrowser).then()`
- 参照: `aFromBrowser.permanentKey`, `aToBrowser.permanentKey`

## _SessionStore.#maybeSaveClosedTab()
- 位置: L3219-3270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `PrivateBrowsingUtils.isWindowPrivate()`, `aWindow.gBrowser.getIcon()`, `this.#closingTabMap.set()`, `this.#shouldSaveTabState()`, `this.#windowIds.get()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.#saveClosedTabData()`
- 参照: `aTab.index`, `aTab.label`, `aTab.linkedBrowser.permanentKey`, `aWindow.FirefoxViewHandler.tab`, `tabState.groupId`, `tabState.isPrivate`, `this.#windows`, `winData._closedTabs`

## _SessionStore.resetBrowserToLazyState()
- 位置: L3279-3335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_LAZY_STATES.set()`, `aTab.removeAttribute()`, `aTab.setAttribute()`, `browser.didStartLoadSinceLastUserTyping()`, `lazy.TabStateCache.get()`, `this.#cleanUpRemovedBrowser()`, `this.#crashedBrowsers.delete()`
- 条件付き依存: `if (shouldUpdateCacheState)` → `lazy.TabStateCache.update()`
- 参照: `aTab.label`, `aTab.linkedBrowser`, `browser.currentURI.spec`, `browser.isConnected`, `browser.permanentKey`, `cacheState.userTypedValue`

## _SessionStore.maybeExitCrashedState()
- 位置: L3345-3350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `uri?.spec?.startsWith()`
- 条件付き依存: `if (uri?.spec?.startsWith("about:tabcrashed"))` → `this.#crashedBrowsers.delete()`
- 参照: `aBrowser.documentURI`, `aBrowser.permanentKey`

## _SessionStore.isBrowserInCrashedSet()
- 位置: L3358-3365
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gDebuggingEnabled)` → `this.#crashedBrowsers.has()`
- 参照: `aBrowser.permanentKey`

## _SessionStore.#cleanUpRemovedBrowser()
- 位置: L3373-3390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `browser.removeEventListener()`
- 条件付き依存: `if (previousState)` → `this.#resetTabRestoringState()`
- 条件付き依存: `if (previousState == TAB_STATE_RESTORING)` → `this.#restoreNextTab()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.#saveClosedTabData()
- 位置: L3406-3455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedTabs.findIndex()`, `closedTabs.splice()`
- 条件付き依存: `if (saveAction)` → `this.#addClosedAction()`
- 条件付き依存: `if ( !tabData.closedInTabGroupId && closedTabs.length > this.#max_tabs_undo )` → `closedTabs.splice()`
- 参照: `closedTabs.length`, `tab.closedAt`, `tabData.closedAt`, `tabData.closedId`, `tabData.closedInGroup`, `tabData.closedInTabGroupId`, `this.#closedObjectsChanged`, `this.#max_tabs_undo`, `this.#nextClosedId`, `this.LAST_ACTION_CLOSED_TAB`, `winData._lastClosedTabGroupCount`, `winData.lastClosedTabGroupId`

## _SessionStore.#removeClosedTabData()
- 位置: L3470-3494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedTabs.splice()`, `this.#removeClosedAction()`
- 条件付き依存: `if (closedTab.permanentKey)` → `this.#closingTabMap.delete()`
- 条件付き依存: `if (closedTab.permanentKey)` → `this.#tabClosingByWindowMap.delete()`
- 参照: `closedTab.closedId`, `closedTab.permanentKey`, `this.#closedObjectsChanged`, `this.LAST_ACTION_CLOSED_TAB`, `winData._lastClosedTabGroupCount`

## _SessionStore.#onTabSelect()
- 位置: L3502-3510
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#maybeRestoreTabContent()`
- 参照: `aWindow.gBrowser.selectedTab`, `aWindow.gBrowser.tabContainer.selectedIndex`, `lazy.RunState.isRunning`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].selected`

## _SessionStore.#maybeRestoreTabContent()
- 位置: L3515-3534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.get(browser) == TAB_STATE_NEEDS_RESTORE)` → `lazy.TabCrashHandler.willShowCrashedTab()`
- 条件付き依存: `if (lazy.TabCrashHandler.willShowCrashedTab(browser))` → `this.#enterCrashedState()`
- 条件付き依存: `if (!(lazy.TabCrashHandler.willShowCrashedTab(browser)))` → `this.#restoreTabContent()`
- 参照: `tab.linkedBrowser`

## _SessionStore.#onTabShow()
- 位置: L3540-3556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `this.#saveStateDelayed()`
- 条件付き依存: `if ( TAB_STATE_FOR_BROWSER.get(aTab.linkedBrowser) == TAB_STATE_NEEDS_RESTORE )` → `TabRestoreQueue.hiddenToVisible()`
- 条件付き依存: `if ( TAB_STATE_FOR_BROWSER.get(aTab.linkedBrowser) == TAB_STATE_NEEDS_RESTORE )` → `this.#restoreNextTab()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.#onTabHide()
- 位置: L3562-3574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `this.#saveStateDelayed()`
- 条件付き依存: `if ( TAB_STATE_FOR_BROWSER.get(aTab.linkedBrowser) == TAB_STATE_NEEDS_RESTORE )` → `TabRestoreQueue.visibleToHidden()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.#onBrowserCrashed()
- 位置: L3582-3587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabStateFlusher.resolveAll()`, `this.#enterCrashedState()`

## _SessionStore.#enterCrashedState()
- 位置: L3597-3612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`, `this.#crashedBrowsers.add()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.has(browser))` → `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (tab)` → `this.#resetLocalTabRestoringState()`
- 参照: `browser.documentGlobal`, `browser.permanentKey`

## _SessionStore.#onIdleDaily()
- 位置: L3617-3642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(this.#windows).map()`, `this.#cleanupOldData()`, `this.#closedWindows.map()`, `this.#notifyOfClosedObjectsChange()`
- 参照: `this.#closedWindows`, `this.#windows`, `this.#windows[key]._closedTabs`, `this.#windows[key].closedGroups`, `winData._closedTabs`, `winData.closedGroups`

## _SessionStore.#cleanupOldData()
- 位置: L3645-3664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.#prefBranch.getIntPref()`
- 条件付き依存: `if (now - data.closedAt > TIME_TO_LIVE)` → `array.splice()`
- 参照: `array.length`, `data.closedAt`, `this.#closedObjectsChanged`

## _SessionStore.getBrowserState()
- 位置: L3673-3683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `this.getCurrentState()`
- 参照: `state.deferredInitialState`, `state.lastSessionState`

## _SessionStore.setBrowserState()
- 位置: L3699-3765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.SessionCookies.restore()`, `this.#getTopWindow()`, `this.#globalState.setFromState()`, `this.#handleClosedWindows()`, `this.#initSplitViewIds()`, `this.#notifyOfClosedObjectsChange()`, `this.#resetRestoringState()`, `this.#restoreWindows()`
- 条件付き依存: `if (!state)` → `Components.Exception()`
- 条件付き依存: `if (!state.windows)` → `Components.Exception()`
- 条件付き依存: `if (!window)` → `this.#openWindowWithState()`
- 条件付き依存: `if (otherWin != window)` → `otherWin.close()`
- 条件付き依存: `if (otherWin != window)` → `this.#onClose()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `state.cookies`, `state.windows`, `state.windows.length`, `this.#browserSetState`, `this.#browserWindows`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#maxSplitViewId`, `this.#restoreCount`

## _SessionStore.getWindowState()
- 位置: L3772-3786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `DyingWindowCache.has()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `Cu.cloneInto()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#getWindowState()`
- 条件付き依存: `if (DyingWindowCache.has(aWindow))` → `DyingWindowCache.get()`
- 条件付き依存: `if (DyingWindowCache.has(aWindow))` → `Cu.cloneInto()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`

## _SessionStore.setWindowState()
- 位置: L3799-3814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#restoreWindows()`, `this.#windowIds.get()`
- 条件付き依存: `if (!this.#windowIds.get(aWindow))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`

## _SessionStore.getTabState()
- 位置: L3826-3840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `TAB_CUSTOM_VALUES.get()`, `lazy.TabState.collect()`, `this.#windowIds.get()`
- 条件付き依存: `if (!aTab || !aTab.documentGlobal)` → `Components.Exception()`
- 条件付き依存: `if (!this.#windowIds.get(aTab.documentGlobal))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTab.documentGlobal`

## _SessionStore.setTabState()
- 位置: L3853-3899
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`, `this.#ensureNoNullsInTabDataList()`, `this.#notifyOfClosedObjectsChange()`, `this.#restoreTab()`, `this.#windowIds.get()`, `this.#windowIds.has()`
- 条件付き依存: `if (typeof tabState == "string")` → `JSON.parse()`
- 条件付き依存: `if (!tabState)` → `Components.Exception()`
- 条件付き依存: `if (typeof tabState != "object")` → `Components.Exception()`
- 条件付き依存: `if (!("entries" in tabState))` → `Components.Exception()`
- 条件付き依存: `if (!window || !this.#windowIds.has(window))` → `Components.Exception()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.has(aTab.linkedBrowser))` → `this.#resetTabRestoringState()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTab.documentGlobal`, `aTab.index`, `aTab.linkedBrowser`, `this.#windows`, `this.#windows[this.#windowIds.get(window)].tabs`, `window.gBrowser.tabs`

## _SessionStore.isTabRestoring()
- 位置: L3907-3909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.getInternalObjectState()
- 位置: L3918-3926
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `TAB_STATE_FOR_BROWSER.get()`, `this.#windowIds.get()`
- 参照: `this.#windows`

## _SessionStore.getObjectTypeForClosedId()
- 位置: L3933-3939
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getClosedWindowDataByClosedId()`
- 参照: `this.LAST_ACTION_CLOSED_TAB`, `this.LAST_ACTION_CLOSED_WINDOW`

## _SessionStore.#getClosedWindowDataByClosedId()
- 位置: L3945-3949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closedWindows.find()`
- 参照: `closedData.closedId`

## _SessionStore.getWindowId()
- 位置: L3964-3966
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.get()`

## _SessionStore.getWindowById()
- 位置: L3973-3982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.get()`
- 参照: `this.#browserWindows`

## _SessionStore.duplicateTab()
- 位置: L4007-4100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `TAB_CUSTOM_VALUES.get()`, `aTab.getAttribute()`, `aWindow.gBrowser.addTrustedTab()`, `aWindow.gBrowser.setDefaultIcon()`, `lazy.TabState.collect()`, `lazy.TabState.copyFromCache()`, `lazy.TabStateFlusher.flush()`, `lazy.TabStateFlusher.flush(browser).then()`, `this.#restoreTab()`, `this.#windowIds.get()`, `uriObj.schemeIs()`
- 条件付き依存: `if (!aTab || !aTab.documentGlobal)` → `Components.Exception()`
- 条件付き依存: `if (!this.#windowIds.get(aTab.documentGlobal))` → `Components.Exception()`
- 条件付き依存: `if (!aWindow.gBrowser)` → `Components.Exception()`
- 条件付き依存: `if (!uriObj || (uriObj && !uriObj.schemeIs("about")))` → `newTab.setAttribute()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTab.documentGlobal`, `aTab.group`, `aTab.linkedBrowser`, `aTab.linkedBrowser.currentURI`, `aTab.linkedBrowser.remoteType`, `aWindow.gBrowser`, `aWindow.gBrowser.selectedTab`, `browser.permanentKey`, `newTab.closing`, `newTab.documentGlobal`, `newTab.linkedBrowser`, `tabState.entries.length`, `tabState.index`, `tabState.pinned`, `window.closed`

## _SessionStore.getWindows()
- 位置: L4110-4125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.#browserWindows).filter()`, `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!aWindowOrOptions)` → `this.#getTopWindow()`
- 条件付き依存: `if (aWindowOrOptions instanceof Ci.nsIDOMWindow)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!(aWindowOrOptions instanceof Ci.nsIDOMWindow))` → `Boolean()`
- 参照: `Ci.nsIDOMWindow`, `aWindowOrOptions.private`, `this.#browserWindows`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md)

## _SessionStore.getWindowForTabClosedId()
- 位置: L4133-4151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closedTabs.find()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#windowIds.get()`, `this.getWindows()`
- 参照: `closedTabs.length`, `tab.closedId`, `this.#windows`

## _SessionStore.getLastClosedTabCount()
- 位置: L4163-4175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `Math.min()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `Math.max()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.getClosedTabCountForWindow()`
- 参照: `Components.returnCode`, `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._lastClosedTabGroupCount`

## _SessionStore.resetLastClosedTabCount()
- 位置: L4184-4191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 参照: `Components.returnCode`, `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._lastClosedTabGroupCount`, `this.#windows[this.#windowIds.get(aWindow)].lastClosedTabGroupId`

## _SessionStore.getClosedTabCountForWindow()
- 位置: L4198-4215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DyingWindowCache.get()`, `DyingWindowCache.has()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!DyingWindowCache.has(aWindow))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#getStateForClosedTabsAndClosedGroupTabs( DyingWindowCache.get(aWindow) ).length`, `this.#getStateForClosedTabsAndClosedGroupTabs( this.#windows[this.#windowIds.get(aWindow)] ).length`, `this.#windows`

## _SessionStore.#prepareClosedTabOptions()
- 位置: L4222-4248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `sourceOptions.hasOwnProperty()`
- 条件付き依存: `if (!sourceOptions.sourceWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if (!sourceOptions.hasOwnProperty("private"))` → `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `sourceOptions.private`, `sourceOptions.sourceWindow`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedTabsFromClosedWindowsEnabled`

## _SessionStore.getClosedTabCount()
- 位置: L4256-4272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#prepareClosedTabOptions()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows({ private: sourceOptions.private }) .map(win => this.getClosedTabCountForWindow(win)) .reduce()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows({ private: sourceOptions.private }) .map()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getClosedTabCountForWindow()`
- 条件付き依存: `if (!(sourceOptions.closedTabsFromAllWindows))` → `this.getClosedTabCountForWindow()`
- 条件付き依存: `if (!sourceOptions.private && sourceOptions.closedTabsFromClosedWindows)` → `this.getClosedTabCountFromClosedWindows()`
- 参照: `sourceOptions.closedTabsFromAllWindows`, `sourceOptions.closedTabsFromClosedWindows`, `sourceOptions.private`, `sourceOptions.sourceWindow`

## _SessionStore.getClosedTabCountFromClosedWindows()
- 位置: L4280-4287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closedWindows .map()`, `this.#closedWindows .map( winData => this.#getStateForClosedTabsAndClosedGroupTabs(winData).length ) .reduce()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 参照: `this.#getStateForClosedTabsAndClosedGroupTabs(winData).length`

## _SessionStore.getClosedTabDataForWindow()
- 位置: L4297-4302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getClonedDataForWindow()`
- 参照: `this.#getStateForClosedTabsAndClosedGroupTabs`

## _SessionStore.getClosedTabData()
- 位置: L4310-4323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#prepareClosedTabOptions()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `closedTabData.push()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getClosedTabDataForWindow()`
- 条件付き依存: `if (!(sourceOptions.closedTabsFromAllWindows))` → `closedTabData.push()`
- 条件付き依存: `if (!(sourceOptions.closedTabsFromAllWindows))` → `this.getClosedTabDataForWindow()`
- 参照: `sourceOptions.closedTabsFromAllWindows`, `sourceOptions.private`, `sourceOptions.sourceWindow`

## _SessionStore.getClosedTabDataFromClosedWindows()
- 位置: L4331-4347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `closedTabData.push()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 参照: `tabData.sourceClosedId`, `this.#closedWindows`, `winData.closedId`

## _SessionStore.getClosedTabGroups()
- 位置: L4356-4389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#prepareClosedTabOptions()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `closedTabGroups.push()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.#getClonedDataForWindow()`
- 条件付き依存: `if (sourceOptions.sourceWindow.closedGroups)` → `closedTabGroups.push()`
- 条件付き依存: `if (sourceOptions.sourceWindow.closedGroups)` → `this.#getClonedDataForWindow()`
- 条件付き依存: `if (sourceOptions.closedTabsFromClosedWindows)` → `this.getClosedWindowData()`
- 条件付き依存: `if (sourceOptions.closedTabsFromClosedWindows)` → `closedTabGroups.push()`
- 参照: `groupData.tabs`, `sourceOptions.closedTabsFromAllWindows`, `sourceOptions.closedTabsFromClosedWindows`, `sourceOptions.private`, `sourceOptions.sourceWindow`, `sourceOptions.sourceWindow.closedGroups`, `tabData.sourceClosedId`, `w.closedGroups`, `winData.closedGroups`, `winData.closedId`

## _SessionStore.getLastClosedTabGroupId()
- 位置: L4396-4402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 参照: `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].lastClosedTabGroupId`

## _SessionStore.#getClonedDataForWindow()
- 位置: L4414-4436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `DyingWindowCache.get()`, `DyingWindowCache.has()`, `selector()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!winData && !DyingWindowCache.has(aWindow))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`

## _SessionStore.#getStateForClosedTabsAndClosedGroupTabs()
- 位置: L4449-4485
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( groupIdx < closedGroups.length && (tabIdx >= closedTabs.length || group?.closedAt > tab?.closedAt) )` → `group.tabs.forEach()`
- 条件付き依存: `if ( groupIdx < closedGroups.length && (tabIdx >= closedTabs.length || group?.closedAt > tab?.closedAt) )` → `result.push()`
- 条件付き依存: `if (!( groupIdx < closedGroups.length && (tabIdx >= closedTabs.length || group?.closedAt > tab?.closedAt) ))` → `result.push()`
- 参照: `closedGroups.length`, `closedTabs.length`, `group?.closedAt`, `groupTab._originalGroupStateIndex`, `groupTab._originalStateIndex`, `tab._originalStateIndex`, `tab?.closedAt`, `winData._closedTabs`, `winData.closedGroups`

## _SessionStore.#getClosedTabStateFromUnifiedIndex()
- 位置: L4500-4511
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sourceWinData._closedTabs`, `sourceWinData.closedGroups`, `sourceWinData.closedGroups[tabState._originalGroupStateIndex].tabs`, `tabState._originalGroupStateIndex`, `tabState._originalStateIndex`

## _SessionStore.undoCloseTab()
- 位置: L4524-4600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `PrivateBrowsingUtils.isWindowPrivate()`, `tabbrowser.addTrustedTab()`, `tabbrowser.tabGroups.find()`, `this.#cleanupOrphanedClosedGroups()`, `this.#getClosedTabStateFromUnifiedIndex()`, `this.#getPreferredRemoteType()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedTabData()`, `this.#resolveClosedDataSource()`, `this.#restoreTab()`, `this.#windowIds.get()`
- 条件付き依存: `if (aTargetWindow && !this.#windowIds.get(aTargetWindow))` → `Components.Exception()`
- 条件付き依存: `if (!aTargetWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if ( isPrivateSource !== PrivateBrowsingUtils.isWindowPrivate(aTargetWindow) )` → `Components.Exception()`
- 条件付き依存: `if (!closedTabState)` → `Components.Exception()`
- 条件付き依存: `if (state.entries?.length)` → `this.historyIndex()`
- 条件付き依存: `if (state.entries?.length)` → `Math.min()`
- 条件付き依存: `if (state.entries?.length)` → `Math.max()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTargetWindow.gBrowser`, `g.id`, `sourceWinData.isPrivate`, `state.entries`, `state.entries.length`, `state.entries?.length`, `state.entries[activeIndex].url`, `state.groupId`, `state.pinned`, `state.userContextId`, `tabbrowser.selectedTab`

## _SessionStore.undoClosedTabFromClosedWindow()
- 位置: L4613-4627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `closedTabs.findIndex()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#resolveClosedDataSource()`
- 条件付き依存: `if (closedIndex >= 0)` → `this.undoCloseTab()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `tabData.closedId`

## _SessionStore.#getPreferredRemoteType()
- 位置: L4629-4634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`

## _SessionStore.#resolveClosedDataSource()
- 位置: L4640-4664
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aSource instanceof Ci.nsIDOMWindow)` → `this.#getWindowStateData()`
- 条件付き依存: `if (aSource.sourceWindow instanceof Ci.nsIDOMWindow)` → `this.#getWindowStateData()`
- 条件付き依存: `if (typeof aSource.sourceClosedId == "number")` → `this.#getClosedWindowDataByClosedId()`
- 条件付き依存: `if (!winData)` → `Components.Exception()`
- 条件付き依存: `if (typeof aSource.sourceWindowId == "string")` → `this.getWindowById()`
- 条件付き依存: `if (typeof aSource.sourceWindowId == "string")` → `this.#getWindowStateData()`
- 条件付き依存: `if (!(typeof aSource.sourceWindowId == "string"))` → `Components.Exception()`
- 参照: `Ci.nsIDOMWindow`, `Cr.NS_ERROR_INVALID_ARG`, `aSource.sourceClosedId`, `aSource.sourceWindow`, `aSource.sourceWindowId`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md)

## _SessionStore.forgetClosedTab()
- 位置: L4677-4693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedTabData()`, `this.#resolveClosedDataSource()`
- 条件付き依存: `if (!(aIndex in winData._closedTabs))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `winData._closedTabs`

## _SessionStore.forgetClosedTabGroup()
- 位置: L4707-4728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedTabData()`, `this.#resolveClosedDataSource()`, `winData.closedGroups.findIndex()`, `winData.closedGroups.splice()`
- 条件付き依存: `if (closedGroupIndex < 0)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `closedGroup.tabs`, `closedGroup.tabs.length`, `closedTabGroup.id`, `winData.closedGroups`

## _SessionStore.forgetSavedTabGroup()
- 位置: L4736-4766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `this.#notifyOfClosedObjectsChange()`, `this.#notifyOfSavedTabGroupsChange()`, `this.#removeClosedTabData()`, `this.#savedGroups.findIndex()`, `this.#savedGroups.splice()`
- 条件付き依存: `if (savedGroupIndex < 0)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `savedGroup.tabs`, `savedGroup.tabs.length`, `savedTabGroup.id`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#savedGroups`, `this.#windows`, `winData._lastClosedTabGroupCount`, `winData.lastClosedTabGroupId`

## _SessionStore.forgetClosedWindowById()
- 位置: L4777-4789
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closedWindows.findIndex()`, `this.forgetClosedWindow()`
- 条件付き依存: `if (closedIndex < 0)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `windowState.closedId`

## _SessionStore.forgetClosedTabById()
- 位置: L4804-4853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `closedTabs.find()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 条件付き依存: `if ( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions )` → `this.#resolveClosedDataSource()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `Array.from()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `sourceWindowsData.push()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `this.#windowIds.get()`
- 条件付き依存: `if (closedTabState)` → `this.#getClosedTabStateFromUnifiedIndex()`
- 条件付き依存: `if (closedTabState)` → `this.#removeClosedTabData()`
- 条件付き依存: `if (closedTabState)` → `this.#notifyOfClosedObjectsChange()`
- 参照: `(aSourceOptions) .includePrivate`, `Ci.nsIDOMWindow`, `Cr.NS_ERROR_INVALID_ARG`, `tabData.closedId`, `this.#browserWindows`, `this.#windows`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md)

## _SessionStore.getClosedWindowCount()
- 位置: L4859-4861
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#closedWindows.length`

## _SessionStore.getClosedWindowData()
- 位置: L4866-4872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `this.#trimSavedTabGroupMetadataInClosedWindow()`
- 参照: `this.#closedWindows`

## _SessionStore.#trimSavedTabGroupMetadataInClosedWindow()
- 位置: L4884-4889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `closedWinData.groups?.map()`, `lazy.TabGroupState.abbreviated()`
- 参照: `closedWinData.groups`

## _SessionStore.maybeDontRestoreTabs()
- 位置: L4898-4901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.get()`
- 参照: `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._maybeDontRestoreTabs`

## _SessionStore.#isLastRestorableWindow()
- 位置: L4903-4909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(this.#windows).filter()`, `this.#closedWindows.some()`
- 参照: `Object.values(this.#windows).filter(winData => !winData.isPrivate) .length`, `this.#windows`, `win._shouldRestore`, `winData.isPrivate`

## _SessionStore.undoCloseWindow()
- 位置: L4922-4957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WINDOW_SHOWING_PROMISES.get()`, `WINDOW_SHOWING_PROMISES.get(window).promise.then()`, `this.#notifyOfClosedObjectsChange()`, `this.#openWindowWithState()`, `this.#removeClosedWindow()`, `this.#restoreWindows()`, `this.#trimSavedTabGroupMetadataInClosedWindow()`, `this.getSavedTabGroup()`
- 条件付き依存: `if (!(aIndex in this.#closedWindows))` → `Components.Exception()`
- 条件付き依存: `if (this.getSavedTabGroup(tabGroup.id))` → `this.forgetSavedTabGroup()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `state.windows`, `state.windows[0].closedAt`, `state.windows[0].groups`, `tabGroup.id`, `this.#closedWindows`, `this.#windowToFocus`

## _SessionStore.forgetClosedWindow()
- 位置: L4967-4984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedWindow()`, `this.#saveableClosedWindowData.delete()`
- 条件付き依存: `if (!(aIndex in this.#closedWindows))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#closedWindows`

## _SessionStore.getCustomWindowValue()
- 位置: L4995-5010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `DyingWindowCache.has()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (DyingWindowCache.has(aWindow))` → `DyingWindowCache.get()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `DyingWindowCache.get(aWindow).extData`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].extData`

## _SessionStore.setCustomWindowValue()
- 位置: L5024-5040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#saveStateDelayed()`, `this.#windowIds.get()`, `this.#windowIds.has()`
- 条件付き依存: `if (!this.#windowIds.has(aWindow))` → `Components.Exception()`
- 条件付き依存: `if (!this.#windows[this.#windowIds.get(aWindow)].extData)` → `this.#windowIds.get()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].extData`

## _SessionStore.deleteCustomWindowValue()
- 位置: L5050-5059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#saveStateDelayed()`, `this.#windowIds.get()`
- 条件付き依存: `if ( this.#windowIds.get(aWindow) && this.#windows[this.#windowIds.get(aWindow)].extData && this.#windows[this.#windowIds.get(aWindow)].extData[aKey] )` → `this.#windowIds.get()`
- 参照: `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].extData`

## _SessionStore.getCustomTabValue()
- 位置: L5069-5071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`

## _SessionStore.setCustomTabValue()
- 位置: L5084-5097
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `TAB_CUSTOM_VALUES.has()`, `this.#saveStateDelayed()`
- 条件付き依存: `if (!TAB_CUSTOM_VALUES.has(aTab))` → `TAB_CUSTOM_VALUES.set()`
- 参照: `aTab.documentGlobal`

## _SessionStore.deleteCustomTabValue()
- 位置: L5107-5113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (state && aKey in state)` → `this.#saveStateDelayed()`
- 参照: `aTab.documentGlobal`

## _SessionStore.#moveCustomTabValue()
- 位置: L5119-5128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (state)` → `TAB_CUSTOM_VALUES.set()`
- 条件付き依存: `if (state)` → `TAB_CUSTOM_VALUES.delete()`

## _SessionStore.getLazyTabValue()
- 位置: L5139-5141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_LAZY_STATES.get()`

## _SessionStore.getCustomGlobalValue()
- 位置: L5149-5151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#globalState.get()`

## _SessionStore.setCustomGlobalValue()
- 位置: L5162-5169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#globalState.set()`, `this.#saveStateDelayed()`

## _SessionStore.deleteCustomGlobalValue()
- 位置: L5177-5180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#globalState.delete()`, `this.#saveStateDelayed()`

## _SessionStore.undoCloseById()
- 位置: L5197-5228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.wm.getEnumerator()`, `this.#windowIds.get()`
- 条件付き依存: `if (this.#closedWindows[i].closedId == aClosedId)` → `this.undoCloseWindow()`
- 条件付き依存: `if (windowState)` → `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 条件付き依存: `if (closedTabs[j].closedId == aClosedId)` → `this.undoCloseTab()`
- 参照: `closedTabs.length`, `closedTabs[j].closedId`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[i].closedId`, `this.#windows`
- XPCOM: `Services.wm`

## _SessionStore.#updateTabLabelAndIcon()
- 位置: L5240-5285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.hasAttribute()`
- 条件付き依存: `if (!tabData)` → `lazy.TabState.collect()`
- 条件付き依存: `if (!tabData)` → `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (activePageData.title && activePageData.title != activePageData.url)` → `win.gBrowser.setInitialTabTitle()`
- 条件付き依存: `if (!(activePageData.title && activePageData.title != activePageData.url))` → `win.gBrowser.setInitialTabTitle()`
- 条件付き依存: `if ( !activePageData || (activePageData && activePageData.url != "about:blank") )` → `win.gBrowser.setIcon()`
- 条件付き依存: `if ("image" in tabData)` → `lazy.TabStateCache.update()`
- 参照: `activePageData.title`, `activePageData.url`, `browser.documentGlobal`, `browser.permanentKey`, `tab.linkedBrowser`, `tabData.entries`, `tabData.image`, `tabData.index`

## _SessionStore.#forgetTabsWithUserContextId()
- 位置: L5288-5331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `clearClosedTabs()`, `this.#notifyOfClosedObjectsChange()`, `this.#windowIds.get()`, `windowState.tabs.filter()`
- 条件付き依存: `if (windowState)` → `clearClosedTabs()`
- 条件付き依存: `if (!windowState.tabs.length)` → `this.#removeClosedWindow()`
- 条件付き依存: `if (!windowState.tabs.length)` → `this.#saveableClosedWindowData.delete()`
- 参照: `tab.userContextId`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#windows`, `windowState.tabs`, `windowState.tabs.length`
- XPCOM: `Services.wm`

## clearClosedTabs()
- 位置: L5289-5303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `indexes.reverse()`, `this.#removeClosedTabData()`, `windowState._closedTabs.forEach()`
- 条件付き依存: `if (closedTab.state.userContextId == userContextId)` → `indexes.push()`
- 参照: `closedTab.state.userContextId`, `windowState._closedTabs`

## _SessionStore.restoreLastSession()
- 位置: L5340-5517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LastSession.clear()`, `LastSession.getState()`, `Services.obs.notifyObservers()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.AIWindow.isAIWindowEnabled()`, `lazy.DevToolsShim.restoreDevToolsSession()`, `lazy.SessionCookies.restore()`, `openWindows.concat()`, `this.#canRestoreIntoExistingWindow()`, `this.#getTopWindow()`, `this.#globalState.setFromState()`, `this.#lastSessionWindowIds.get()`, `this.#notifyOfClosedObjectsChange()`, `this.#openWindows()`, `this.#openWindows({ windows: windowsToOpen }).then()`, `this.#restoreWindowsInReversedZOrder()`, `this.#savedGroups.filter()`, `this.#updateSessionStartTime()`, `this.forgetSavedTabGroup()`
- 条件付き依存: `if (!this.canRestoreLastSession)` → `Components.Exception()`
- 条件付き依存: `if (this.#lastSessionWindowIds.get(window))` → `this.#lastSessionWindowIds.get()`
- 条件付き依存: `if (!lastSessionState.windows.length)` → `Components.Exception()`
- 条件付き依存: `if (this.#restoreWithoutRestart)` → `this.#closedWindows.findIndex()`
- 条件付き依存: `if (restoreIndex > -1)` → `this.#closedWindows.splice()`
- 条件付き依存: `if (winState._closedTabs && winState._closedTabs.length)` → `this.#windowIds.get()`
- 条件付き依存: `if (winState._closedTabs && winState._closedTabs.length)` → `curWinState._closedTabs.concat()`
- 条件付き依存: `if (winState._closedTabs && winState._closedTabs.length)` → `curWinState._closedTabs.splice()`
- 条件付き依存: `if (windowToUse)` → `this.#getRemovableHomePages()`
- 条件付き依存: `if (!(windowToUse.gBrowser.tabs.length == removableTabs.length))` → `windowToUse.gBrowser.removeTab()`
- 条件付き依存: `if (!(windowToUse.gBrowser.tabs.length == removableTabs.length))` → `removableTabs.pop()`
- 条件付き依存: `if (windowToUse)` → `this.#updateWindowRestoreState()`
- 条件付き依存: `if (windowToUse)` → `openWindows.push()`
- 条件付き依存: `if (!(windowToUse))` → `windowsToOpen.push()`
- 条件付き依存: `if (this.#restoreWithoutRestart)` → `this.#removeDuplicateClosedWindows()`
- 条件付き依存: `if (closedWindow._closedTabs?.length)` → `this.#resetClosedTabIds()`
- 条件付き依存: `if (lastSessionState._closedWindows)` → `this.#closedWindows.concat()`
- 条件付き依存: `if (lastSessionState._closedWindows)` → `this.#capClosedWindows()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `closedWindow._closedTabs`, `closedWindow._closedTabs?.length`, `closedWindow.closedId`, `curWinState._closedTabs`, `curWinState._closedTabs.length`, `group.id`, `group.removeAfterRestore`, `lastSessionState._closedWindows`, `lastSessionState.cookies`, `lastSessionState.session`, `lastSessionState.session.recentCrashes`, `lastSessionState.windows`, `lastSessionState.windows.length`, `removableTabs.length`, `this.#browserSetState`, `this.#browserWindows`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#max_tabs_undo`, `this.#nextClosedId`, `this.#recentCrashes`, `this.#restoreCount`, `this.#restoreWithoutRestart`, `this.#windows`, `this.canRestoreLastSession`, `win.closedId`, `winState.__lastSessionWindowID`, `winState._closedTabs`, `winState._closedTabs.length`, `winState.closedId`, `winState.isAIWindow`, `windowToUse.gBrowser.tabs.length`
- XPCOM: `Services.obs`

## _SessionStore.#removeDuplicateClosedWindows()
- 位置: L5527-5537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentClosedIds.has()`, `lastSessionState._closedWindows.filter()`, `this.#closedWindows.map()`
- 参照: `lastSessionState._closedWindows`, `win.closedId`, `window.closedId`

## _SessionStore.reviveCrashedTab()
- 位置: L5547-5585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `TAB_CUSTOM_VALUES.get()`, `aTab.removeAttribute()`, `browser.loadURI()`, `lazy.TabState.collect()`, `this.#crashedBrowsers.has()`, `this.#restoreTab()`
- 参照: `aTab.linkedBrowser`, `aTab.userContextId`, `browser.isRemoteBrowser`, `browser.permanentKey`, `lazy.E10SUtils.NOT_REMOTE`, `lazy.blankURI`
- XPCOM: `Services.scriptSecurityManager`

## _SessionStore.reviveAllCrashedTabs()
- 位置: L5590-5596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `this.reviveCrashedTab()`
- 参照: `window.gBrowser.tabs`
- XPCOM: `Services.wm`

## _SessionStore.getSessionHistory()
- 位置: L5612-5628
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (updatedCallback)` → `lazy.TabStateFlusher.flush(tab.linkedBrowser).then()`
- 条件付き依存: `if (updatedCallback)` → `lazy.TabStateFlusher.flush()`
- 条件付き依存: `if (updatedCallback)` → `this.getSessionHistory()`
- 条件付き依存: `if (sessionHistory)` → `updatedCallback()`
- 条件付き依存: `if (tab.linkedBrowser)` → `lazy.TabState.collect()`
- 条件付き依存: `if (tab.linkedBrowser)` → `TAB_CUSTOM_VALUES.get()`
- 参照: `tab.linkedBrowser`, `tabState.entries`, `tabState.index`

## _SessionStore.#canRestoreIntoExistingWindow()
- 位置: L5642-5673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `Object.entries()`, `Object.entries(existingArgs).every()`, `Object.keys()`, `this.#getWindowStateData()`
- 参照: `Object.keys(existingArgs).length`, `Object.keys(previousArgs).length`, `aPreviousState.args`, `aPreviousState.isPopup`, `aPreviousState.isPrivate`, `aPreviousState.isTaskbarTab`, `existingState.args`, `existingState.isPopup`, `existingState.isPrivate`, `existingState.isTaskbarTab`

## _SessionStore.#getImmutableWindowFeatures()
- 位置: L5684-5707
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (winState.isPrivate)` → `features.add()`
- 条件付き依存: `if (winState.isPopup)` → `features.add()`
- 条件付き依存: `if (winState.isTaskbarTab)` → `features.add()`
- 条件付き依存: `if (winState.args?.[ARG_CHROMELESS_WINDOW])` → `features.add()`
- 条件付き依存: `if (winState.args?.[ARG_WEB_EXTENSION_POPUP_WINDOW])` → `features.add()`
- 参照: `winState.args`, `winState.isPopup`, `winState.isPrivate`, `winState.isTaskbarTab`

## _SessionStore.#getRemovableHomePages()
- 位置: L5720-5754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `homePages.includes()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `this.#prefBranch.getIntPref()`
- 条件付き依存: `if (startupPref == 1)` → `homePages.concat()`
- 条件付き依存: `if (startupPref == 1)` → `lazy.HomePage.get(aWindow).split()`
- 条件付き依存: `if (startupPref == 1)` → `lazy.HomePage.get()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActiveAndEnabled(aWindow))` → `homePages.push()`
- 条件付き依存: `if (homePages.includes(tab.linkedBrowser.currentURI.spec))` → `removableTabs.push()`
- 条件付き依存: `if ( tabbrowser.tabs.length > tabbrowser.visibleTabs.length && tabbrowser.visibleTabs.length === removableTabs.length )` → `removableTabs.shift()`
- 参照: `aWindow.gBrowser`, `lazy.AIWindow.initialStartupURL`, `removableTabs.length`, `tab.linkedBrowser.currentURI.spec`, `tabbrowser.pinnedTabCount`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `tabbrowser.visibleTabs.length`

## _SessionStore.#updateWindowFeatures()
- 位置: L5764-5786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.SidebarController.getUIState()`, `aWindow.getWorkspaceID()`, `lazy.AIWindow.isAIWindowActive()`, `this.#getWindowDimension()`, `this.#windowIds.get()`
- 条件付き依存: `if (sidebarUIState)` → `structuredClone()`
- 参照: `this.#windows`, `winData.isAIWindow`, `winData.sidebar`, `winData.sizemode`, `winData.sizemodeBeforeMinimized`, `winData.workspaceID`

## _SessionStore.getCurrentState()
- 位置: L5796-5922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.sessionRestore.collectAllWindowsData.start()`, `Glean.sessionRestore.collectAllWindowsData.stopAndAccumulate()`, `ids.indexOf()`, `ids.push()`, `lazy.DevToolsShim.saveDevToolsSession()`, `lazy.SessionCookies.collect()`, `this.#closedWindows.slice()`, `this.#getTopWindow()`, `this.#globalState.getState()`, `this.#handleClosedWindows()`, `this.#handleClosedWindows().then()`, `this.#notifyOfClosedObjectsChange()`, `total.push()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#isWindowLoaded()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `DirtyWindows.has()`
- 条件付き依存: `if (aUpdateAll || DirtyWindows.has(window) || window == activeWindow)` → `this.#collectWindowData()`
- 条件付き依存: `if (!(aUpdateAll || DirtyWindows.has(window) || window == activeWindow))` → `this.#updateWindowFeatures()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `DirtyWindows.clear()`
- 条件付き依存: `if ( nonPopupCount == 0 && !!lastClosedWindowsCopy.length && lazy.RunState.isQuitting )` → `total.unshift()`
- 条件付き依存: `if ( nonPopupCount == 0 && !!lastClosedWindowsCopy.length && lazy.RunState.isQuitting )` → `lastClosedWindowsCopy.shift()`
- 条件付き依存: `if (activeWindow)` → `this.#windowIds.get()`
- 条件付き依存: `if (LastSession.canRestore)` → `LastSession.getState()`
- 参照: `AppConstants.platform`, `LastSession.canRestore`, `lastClosedWindowsCopy.length`, `lazy.RunState.isQuitting`, `lazy.RunState.isRunning`, `state.cookies`, `state.deferredInitialState`, `state.lastSessionState`, `this.#activeWindowSSiCache`, `this.#deferredInitialState`, `this.#maxSplitViewId`, `this.#orderedBrowserWindows`, `this.#recentCrashes`, `this.#savedGroups`, `this.#sessionStartTime`, `this.#statesToRestore`, `this.#statesToRestore[ix].windows`, `this.#windows`, `this.#windows[ix]._restoring`, `this.#windows[ix].isPopup`, `this.#windows[ix].isTaskbarTab`, `this.#windows[this.#windowIds.get(window)].zIndex`, `total[0].isPopup`, `total[ix].sizemode`, `winData.isPopup`

## _SessionStore.#getWindowState()
- 位置: L5931-5941
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isWindowLoaded()`, `this.#windowIds.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#collectWindowData()`
- 参照: `lazy.RunState.isRunning`, `this.#statesToRestore`, `this.#windows`

## _SessionStore.#getWindowStateData()
- 位置: L5950-5962
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowIds.get()`
- 条件付き依存: `if ( !this.#windowIds.get(aWindow) || !(this.#windowIds.get(aWindow) in this.#windows) )` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`

## _SessionStore.#collectWindowData()
- 位置: L5974-6029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DirtyWindows.remove()`, `TAB_CUSTOM_VALUES.get()`, `lazy.TabGroupState.collect()`, `lazy.TabState.collect()`, `tabMap.set()`, `tabsData.push()`, `this.#isWindowLoaded()`, `this.#lastSessionWindowIds.get()`, `this.#updateWindowFeatures()`, `this.#windowIds.get()`, `winData.groups.push()`, `winData.splitViews.push()`
- 条件付き依存: `if (this.#lastSessionWindowIds.get(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#lastSessionWindowIds.get(aWindow))` → `this.#lastSessionWindowIds.get()`
- 参照: `aWindow.FirefoxViewHandler.tab`, `aWindow.FirefoxViewHandler.tab?.selected`, `aWindow.gBrowser`, `aWindow.gBrowser.splitViews`, `aWindow.gBrowser.tabGroups`, `splitView.state`, `tabbrowser.tabbox.selectedIndex`, `tabbrowser.tabs`, `tabbrowser.tabs[0].label`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].__lastSessionWindowID`, `winData.groups`, `winData.selected`, `winData.splitViews`, `winData.tabs`, `winData.title`

## _SessionStore.#openWindows()
- 位置: L6041-6057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `WINDOW_SHOWING_PROMISES.get()`, `this.#openWindowWithState()`, `windowOpenedPromises.push()`, `windowsOpened.push()`
- 条件付き依存: `if (!winData || !winData.tabs || !winData.tabs[0])` → `this.#log.debug()`
- 参照: `deferred.promise`, `root.windows`, `this.#restoreCount`, `winData.tabs`

## _SessionStore.#resetClosedTabIds()
- 位置: L6069-6075
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `entry.closedId`, `entry.sourceWindowId`, `this.#nextClosedId`

## _SessionStore.#initSplitViewIds()
- 位置: L6077-6099
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#migrateSplitViewIds()`
- 条件付き依存: `if (this.#maxSplitViewId > 0)` → `this.#log.error()`
- 参照: `session.maxSplitViewId`, `state.deferredInitialState`, `state.lastSessionState`, `this.#maxSplitViewId`

## _SessionStore.#migrateSplitViewIds()
- 位置: L6108-6161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `oldToNewMap.get()`, `oldToNewMap.has()`
- 条件付き依存: `if (state._closedWindows?.length)` → `windowsData.push.apply()`
- 条件付き依存: `if (idType === "number")` → `Math.max()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `oldToNewMap.set()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `SessionStore.getNextSplitViewId()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `this.#log.debug()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `oldToNewMap.get()`
- 条件付き依存: `if (winData.splitViews)` → `oldToNewMap.has()`
- 条件付き依存: `if (oldToNewMap.has(splitViewData.id))` → `oldToNewMap.get()`
- 参照: `splitViewData.id`, `state._closedWindows`, `state._closedWindows?.length`, `state.maxSplitViewId`, `state.windows`, `tabData.splitViewId`, `this.#maxSplitViewId`, `winData.splitViews`, `winData.tabs`, `winData.tabs?.length`

## _SessionStore.#restoreWindow()
- 位置: L6173-6376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.restoreWindow.start()`, `Glean.sessionRestore.restoreWindow.stopAndAccumulate()`, `lazy.SessionCookies.restore()`, `newClosedTabGroupsData.forEach()`, `this.#isWindowLoaded()`, `this.#lastSessionWindowIds.delete()`, `this.#log.debug()`, `this.#prefBranch.getBoolPref()`, `this.#resetClosedTabIds()`, `this.#restoreSidebar()`, `this.#sendWindowRestoringNotification()`, `this.#setWindowStateBusy()`, `this.#windowIds.get()`
- 条件付き依存: `if ( aWindow && (!this.#windowIds.get(aWindow) || !this.#windows[this.#windowIds.get(aWindow)]) )` → `this.#onLoad()`
- 条件付き依存: `if (winData.workspaceID && lazy.gRestoreWindowsToVirtualDesktop)` → `this.#log.debug()`
- 条件付き依存: `if (winData.workspaceID && lazy.gRestoreWindowsToVirtualDesktop)` → `aWindow.moveToWorkspace()`
- 条件付き依存: `if (overwriteTabs)` → `Math.max()`
- 条件付き依存: `if (overwriteTabs)` → `Math.min()`
- 条件付き依存: `if (!overwriteTabs && firstWindow)` → `Array.from()`
- 条件付き依存: `if (!tabbrowser.tabs[i].selected)` → `tabbrowser.removeTab()`
- 条件付き依存: `if (winData.tabs.length)` → `tabbrowser.createTabsForSessionRestore()`
- 条件付き依存: `if (winData.tabs.length)` → `this.#log.debug()`
- 条件付き依存: `if (winData.tabs.length)` → `tabbrowser.tabGroups.map()`
- 条件付き依存: `if (winData.tabs.length)` → `this.#savedGroups.filter()`
- 条件付き依存: `if (winData.tabs.length)` → `openTabGroupIdsInWindow.has()`
- 条件付き依存: `if (initialTabs)` → `tabbrowser.unpinTab()`
- 条件付き依存: `if (initialTabs)` → `tabbrowser.moveTabTo()`
- 条件付き依存: `if (winData.__lastSessionWindowID)` → `this.#lastSessionWindowIds.set()`
- 条件付き依存: `if (overwriteTabs)` → `this.#windowIds.get()`
- 条件付き依存: `if (winData.extData)` → `this.#windowIds.get()`
- 条件付き依存: `if (!this.#windows[this.#windowIds.get(aWindow)].extData)` → `this.#windowIds.get()`
- 条件付き依存: `if (winData._closedTabs)` → `this.#resetClosedTabIds()`
- 条件付き依存: `if (winData._closedTabs)` → `this.#windowIds.get()`
- 条件付き依存: `if (overwriteTabs || firstWindow)` → `this.#windowIds.get()`
- 条件付き依存: `if (PERSIST_SESSIONS)` → `this.#windows[ this.#windowIds.get(aWindow) ]._closedTabs.filter()`
- 条件付き依存: `if (PERSIST_SESSIONS)` → `this.#windowIds.get()`
- 条件付き依存: `if (!(PERSIST_SESSIONS))` → `newClosedTabsData.concat()`
- 条件付き依存: `if (!(PERSIST_SESSIONS))` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#max_tabs_undo > 0)` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#max_tabs_undo > 0)` → `newClosedTabsData.slice()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.delete()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (winData.tabs.length)` → `this.#restoreTabs()`
- 参照: `aOptions.firstWindow`, `aOptions.overwriteTabs`, `aWindow.gBrowser`, `arrowScrollbox.smoothScroll`, `group.id`, `group.tabs`, `initialTabs.length`, `lazy.gRestoreWindowsToVirtualDesktop`, `savedTabGroup.id`, `tab.removeAfterRestore`, `tabbrowser.browsers.length`, `tabbrowser.tabContainer.arrowScrollbox`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `tabbrowser.tabs[i].selected`, `tabs.length`, `this.#max_tabs_undo`, `this.#restore_on_demand`, `this.#savedGroups`, `this.#statesToRestore`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._closedTabs`, `this.#windows[this.#windowIds.get(aWindow)]._lastClosedTabGroupCount`, `this.#windows[this.#windowIds.get(aWindow)]._restoring`, `this.#windows[this.#windowIds.get(aWindow)].closedGroups`, `this.#windows[this.#windowIds.get(aWindow)].extData`, `this.#windows[this.#windowIds.get(aWindow)].lastClosedTabGroupId`, `winData.__lastSessionWindowID`, `winData._closedTabs`, `winData._lastClosedTabGroupCount`, `winData.closedGroups`, `winData.cookies`, `winData.extData`, `winData.groups`, `winData.groups?.length`, `winData.isPopup`, `winData.lastClosedTabGroupId`, `winData.selected`, `winData.sidebar`, `winData.splitViews`, `winData.splitViews?.length`, `winData.tabs`, `winData.tabs.length`, `winData.tabs[0].entries`, `winData.tabs[0].entries.length`, `winData.workspaceID`

## _SessionStore.#prepareConnectionToHost()
- 位置: L6388-6414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.startsWith()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `ChromeUtils.generateQI()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `Services.io.newURI()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `Services.io.speculativeConnect()`
- 参照: `tab.linkedBrowser.browsingContext`, `tab.userContextId`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## _SessionStore.getInterface()
- 位置: L6396-6402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `iid.equals()`
- 参照: `Ci.nsILoadContext`, `Cr.NS_ERROR_NO_INTERFACE`
- XPCOM: [`nsILoadContext`](../../../docshell/base/nsILoadContext.idl.md)

## _SessionStore.speculativeConnectOnTabHover()
- 位置: L6424-6440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_LAZY_STATES.get()`
- 条件付き依存: `if (tabState && !tabState.connectionPrepared)` → `this.getLazyTabValue()`
- 条件付き依存: `if (tabState && !tabState.connectionPrepared)` → `this.#prepareConnectionToHost()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Object.assign()`
- 参照: `tabState.connectionPrepared`

## _SessionStore.#restoreWindowsFeaturesAndTabs()
- 位置: L6448-6484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `WINDOW_RESTORE_IDS.get()`, `WINDOW_RESTORE_ZINDICES.delete()`, `resizePromise.then()`, `resizePromises.push()`, `this.#restoreWindow()`, `this.#restoreWindowFeatures()`, `this.#sendRestoreCompletedNotifications()`, `this.#sendWindowRestoredNotification()`, `this.#setWindowStateReady()`
- 参照: `state.options`, `state.windows`, `this.#statesToRestore`
- XPCOM: `Services.obs`

## _SessionStore.#restoreWindowsInReversedZOrder()
- 位置: L6493-6502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WINDOW_RESTORE_ZINDICES.get()`, `this.#restoreWindowsFeaturesAndTabs()`, `windows.sort()`
- 参照: `this.#windowToFocus`

## _SessionStore.#restoreWindows()
- 位置: L6515-6608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.DevToolsShim.restoreDevToolsSession()`, `root.windows.splice()`, `this.#canRestoreIntoExistingWindow()`, `this.#log.debug()`, `this.#log.error()`, `this.#openWindows()`, `this.#openWindows(root).then()`, `this.#restoreWindowsInReversedZOrder()`, `this.#sendRestoreCompletedNotifications()`, `this.#updateWindowRestoreState()`, `this.#windowIds.get()`, `windows.unshift()`
- 条件付き依存: `if ( aWindow && (!this.#windowIds.get(aWindow) || !this.#windows[this.#windowIds.get(aWindow)]) )` → `this.#onLoad()`
- 条件付き依存: `if (closedWindow._closedTabs?.length)` → `this.#resetClosedTabIds()`
- 条件付き依存: `if (root._closedWindows)` → `this.#log.debug()`
- 条件付き依存: `if (!root.windows || !root.windows.length)` → `this.#sendRestoreCompletedNotifications()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `this.#getWindowStateData()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `this.#getImmutableWindowFeatures()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `this.#log.warn()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Glean.sessionRestore.windowFeaturesMismatchIgnored.record()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Array.from(existingFeatures).join()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Array.from()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Array.from(requestedFeatures).join()`
- 参照: `aOptions.restoreSource`, `closedWindow._closedTabs`, `closedWindow._closedTabs?.length`, `closedWindow.closedId`, `ex.message`, `root._closedWindows`, `root.windows`, `root.windows.length`, `root.windows?.length`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#nextClosedId`, `this.#windows`

## _SessionStore.#restoreTabs()
- 位置: L6624-6670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTabs.indexOf()`, `this.#ensureNoNullsInTabDataList()`, `this.#windowIds.get()`
- 条件付き依存: `if (!(numTabsInWindow == numTabsToRestore))` → `tabsDataArray.splice()`
- 条件付き依存: `if (aSelectTab > 0 && aSelectTab <= aTabs.length)` → `this.#windowIds.get()`
- 条件付き依存: `if (selectedIndex > -1)` → `this.#restoreTab()`
- 条件付き依存: `if (t != selectedIndex)` → `this.#restoreTab()`
- 参照: `aTabs.length`, `aWindow.gBrowser`, `tabbrowser.selectedTab`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `tabsDataArray.length`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].selected`, `this.#windows[this.#windowIds.get(aWindow)].tabs`

## _SessionStore.#ensureNoNullsInTabDataList()
- 位置: L6675-6698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabDataList.push()`
- 参照: `existingTabEl.lastAccessed`, `tabDataList.length`

## _SessionStore.#restoreTab()
- 位置: L6701-6906
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DirtyWindows.add()`, `Math.max()`, `Math.min()`, `TAB_STATE_FOR_BROWSER.has()`, `lazy.TabStateCache.update()`, `tab.hasAttribute()`, `tab.setAttribute()`, `this.#crashedBrowsers.delete()`, `this.#setWindowStateBusy()`, `this.#setWindowStateReady()`, `this.#updateTabLabelAndIcon()`, `this.#windowIds.get()`, `this.historyIndex()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.has(browser))` → `this.#log.warn()`
- 条件付き依存: `if (tabData.lastAccessed)` → `tab.updateLastAccessed()`
- 条件付き依存: `if (tabData.extData)` → `TAB_CUSTOM_VALUES.set()`
- 条件付き依存: `if (tabData.extData)` → `Cu.cloneInto()`
- 条件付き依存: `if (!(tabData.extData))` → `TAB_CUSTOM_VALUES.delete()`
- 条件付き依存: `if ("attributes" in tabData)` → `lazy.TabAttributes.set()`
- 条件付き依存: `if (isBrowserInserted)` → `this.#startNextEpoch()`
- 条件付き依存: `if (isBrowserInserted)` → `TAB_STATE_FOR_BROWSER.set()`
- 条件付き依存: `if (isBrowserInserted)` → `this.#sendRestoreHistory()`
- 条件付き依存: `if (willRestoreImmediately)` → `this.#restoreTabContent()`
- 条件付き依存: `if (!forceOnDemand)` → `TabRestoreQueue.add()`
- 条件付き依存: `if (!forceOnDemand)` → `TabRestoreQueue.willRestoreSoon()`
- 条件付き依存: `if (activeIndex in tabData.entries)` → `this.#prepareConnectionToHost()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Object.assign()`
- 条件付き依存: `if (!forceOnDemand)` → `this.#restoreNextTab()`
- 条件付き依存: `if (!(isBrowserInserted))` → `TAB_LAZY_STATES.set()`
- 条件付き依存: `if (tabData.pinned)` → `tabbrowser.pinTab()`
- 条件付き依存: `if (!(tabData.pinned))` → `tabbrowser.unpinTab()`
- 条件付き依存: `if (tabData.hidden)` → `tabbrowser.hideTab()`
- 条件付き依存: `if (!(tabData.hidden))` → `tabbrowser.showTab()`
- 条件付き依存: `if (!!tabData.muted != browser.audioMuted)` → `tab.toggleMuteAudio()`
- 条件付き依存: `if (tab.hasAttribute("customizemode"))` → `window.gCustomizeMode.setTab()`
- 参照: `RESTORE_TAB_CONTENT_REASON.NAVIGATE_AND_RESTORE`, `browser.audioMuted`, `browser.isConnected`, `browser.permanentKey`, `options.forceOnDemand`, `options.loadArguments`, `options.restoreContentReason`, `options.restoreImmediately`, `tab.canonicalUrl`, `tab.documentGlobal`, `tab.index`, `tab.linkedBrowser`, `tab.splitview`, `tabData.attributes`, `tabData.canonicalUrl`, `tabData.closedAt`, `tabData.disallow`, `tabData.entries`, `tabData.entries.length`, `tabData.entries[activeIndex].title`, `tabData.entries[activeIndex].url`, `tabData.extData`, `tabData.formdata`, `tabData.hidden`, `tabData.image`, `tabData.index`, `tabData.lastAccessed`, `tabData.muteReason`, `tabData.muted`, `tabData.pinned`, `tabData.scroll`, `tabData.searchMode`, `tabData.storage`, `tabData.userContextId`, `tabData.userTypedClear`, `tabData.userTypedValue`, `tabbrowser.selectedBrowser`, `tabbrowser.selectedTab.splitview`, `this.#windows`, `this.#windows[this.#windowIds.get(window)].tabs`, `window.gBrowser`

## _SessionStore.#restoreTabContent()
- 位置: L6916-6941
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `aTab.hasAttribute()`, `lazy.TabState.clone()`, `this.#markTabAsRestoring()`, `this.#sendRestoreTabContent()`, `window.isBlankPageURL()`
- 条件付き依存: `if (aTab.selected && !window.isBlankPageURL(uri))` → `browser.focus()`
- 参照: `RESTORE_TAB_CONTENT_REASON.SET_STATE`, `aOptions.loadArguments`, `aOptions.restoreContentReason`, `aTab.documentGlobal`, `aTab.linkedBrowser`, `aTab.selected`, `activePageData.url`, `tabData.entries`, `tabData.index`

## _SessionStore.#markTabAsRestoring()
- 位置: L6949-6965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `TAB_STATE_FOR_BROWSER.set()`, `TabRestoreQueue.remove()`, `aTab.removeAttribute()`
- 参照: `aTab.linkedBrowser`, `this.#tabsRestoringCount`

## _SessionStore.#restoreNextTab()
- 位置: L6975-6990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabRestoreQueue.shift()`
- 条件付き依存: `if (tab)` → `this.#restoreTabContent()`
- 参照: `lazy.RunState.isQuitting`, `this.#tabsRestoringCount`

## _SessionStore.#restoreWindowFeatures()
- 位置: L7002-7053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `aWindow.setTimeout()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.AIWindow.isAIWindowEnabled()`, `lazy.AIWindow.shouldOpenAsSmartWindow()`, `lazy.SessionStartup.willRestore()`, `promiseParts.resolve()`, `this.#restoreDimensions()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActive(aWindow) !== shouldBeAIWindow)` → `lazy.AIWindow.toggleAIWindow()`
- 条件付き依存: `if (shouldBeAIWindow)` → `lazy.AIWindow.recordOpenWindowTelemetry()`
- 条件付き依存: `if (minimizedWhilePending)` → `promiseParts.resolve()`
- 参照: `aOptions.firstWindow`, `aOptions.trigger`, `aWinData.height`, `aWinData.isAIWindow`, `aWinData.screenX`, `aWinData.screenY`, `aWinData.sizemode`, `aWinData.sizemodeBeforeMinimized`, `aWinData.width`, `aWindow.STATE_MINIMIZED`, `aWindow.windowState`, `promiseParts.promise`

## _SessionStore.#restoreSidebar()
- 位置: L7064-7070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.SidebarController.markSessionRestoreStateReceived()`, `aWindow.SidebarController.updateUIState()`

## _SessionStore.#restoreDimensions()
- 位置: L7090-7244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.shouldResistFingerprinting()`, `dwu.suppressAnimation()`, `isNaN()`, `lazy.gScreenManager.screenForRect()`, `this.#windowIds.get()`, `win_()`
- 条件付き依存: `if (screen)` → `screen.GetAvailRectDisplayPix()`
- 条件付き依存: `if (screen)` → `Math.max()`
- 条件付き依存: `if (aLeft > screenLeft)` → `Math.max()`
- 条件付き依存: `if (aTop > screenTop)` → `Math.max()`
- 条件付き依存: `if ( !isNaN(aLeft) && !isNaN(aTop) && (aLeft != win_("screenX") || aTop != win_("screenY")) )` → `getBaseWindow(aWindow).setPositionDesktopPix()`
- 条件付き依存: `if ( !isNaN(aLeft) && !isNaN(aTop) && (aLeft != win_("screenX") || aTop != win_("screenY")) )` → `getBaseWindow()`
- 条件付き依存: `if ( !isNaN(aLeft) && !isNaN(aTop) && (aLeft != win_("screenX") || aTop != win_("screenY")) )` → `Math.round()`
- 条件付き依存: `if ( aWidth && aHeight && (aWidth != win_("width") || aHeight != win_("height")) && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `win_()`
- 条件付き依存: `if (aSizeMode != "maximized" || win_("sizemode") != "maximized")` → `aWindow.resizeTo()`
- 条件付き依存: `if ( aSizeMode && win_("sizemode") != aSizeMode && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `aWindow.maximize()`
- 条件付き依存: `if (aSizeModeBeforeMinimized == "maximized")` → `aWindow.maximize()`
- 条件付き依存: `if ( aSizeMode && win_("sizemode") != aSizeMode && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `aWindow.minimize()`
- 条件付き依存: `if ( aSizeMode && win_("sizemode") != aSizeMode && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `aWindow.restore()`
- 条件付き依存: `if (this.#windowToFocus)` → `this.#windowToFocus.focus()`
- 参照: `height.value`, `left.value`, `screen.contentsScaleFactor`, `screen.defaultCSSScaleFactor`, `this.#windowToFocus`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].sizemodeBeforeMinimized`, `top.value`, `width.value`, `win.screenEdgeSlopX`, `win.screenEdgeSlopY`, `win.windowUtils`

## win_()
- 位置: L7100-7100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getWindowDimension()`

## _SessionStore.#saveStateDelayed()
- 位置: L7255-7261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionSaver.runDelayed()`
- 条件付き依存: `if (aWindow)` → `DirtyWindows.add()`

## _SessionStore.#removeClosedWindow()
- 位置: L7274-7287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closedWindows.splice()`, `this.#removeClosedAction()`
- 参照: `closedTab.closedId`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows[index]._closedTabs`, `this.#closedWindows[index].closedId`, `this.LAST_ACTION_CLOSED_TAB`, `this.LAST_ACTION_CLOSED_WINDOW`

## _SessionStore.#notifyOfClosedObjectsChange()
- 位置: L7293-7301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.setTimeout()`
- 参照: `this.#closedObjectsChanged`
- XPCOM: `Services.obs`

## _SessionStore.#notifyOfSavedTabGroupsChange()
- 位置: L7307-7311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.setTimeout()`
- XPCOM: `Services.obs`

## _SessionStore.#updateSessionStartTime()
- 位置: L7320-7325
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `state.session`, `state.session.startTime`, `this.#sessionStartTime`

## _SessionStore.[Symbol.iterator]()
- 位置: L7334-7340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getWindowId()`
- 参照: `Symbol.iterator`, `lazy.BrowserWindowTracker.orderedWindows`, `window.closed`

## _SessionStore.[Symbol.iterator]()
- 位置: L7349-7371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getWindowId()`, `windows.sort()`
- 参照: `Symbol.iterator`, `a.STATE_MINIMIZED`, `a.windowState`, `b.STATE_MINIMIZED`, `b.windowState`, `lazy.BrowserWindowTracker.orderedWindows`, `window.closed`

## _SessionStore.#getTopWindow()
- 位置: L7382-7390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 参照: `options.private`

## _SessionStore.#handleClosedWindows()
- 位置: L7397-7405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Services.wm.getEnumerator()`
- 条件付き依存: `if (window.closed)` → `promises.push()`
- 条件付き依存: `if (window.closed)` → `this.#onClose()`
- 参照: `window.closed`
- XPCOM: `Services.wm`

## _SessionStore.#updateWindowRestoreState()
- 位置: L7417-7427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`, `WINDOW_RESTORE_IDS.set()`
- 条件付き依存: `if ("zIndex" in state.windows[0])` → `WINDOW_RESTORE_ZINDICES.set()`
- 参照: `state.windows`, `state.windows[0].zIndex`, `this.#statesToRestore`

## _SessionStore.#openWindowWithState()
- 位置: L7437-7538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`, `JSON.stringify()`, `Promise.withResolvers()`, `Services.ww.openWindow()`, `WINDOW_ATTRIBUTES.forEach()`, `WINDOW_SHOWING_PROMISES.set()`, `args.appendElement()`, `args.queryElementAt()`, `features.join()`, `isNaN()`, `this.#log.debug()`, `this.#serializePropertyBag()`, `this.#updateWindowRestoreState()`
- 条件付き依存: `if (hasAll)` → `features.push()`
- 条件付き依存: `if (value)` → `features.push()`
- 条件付き依存: `if (!(winState.chromeFlags))` → `features.push()`
- 条件付き依存: `if (winState.isPopup)` → `features.push()`
- 条件付き依存: `if (!(winState.isPopup))` → `features.push()`
- 条件付き依存: `if (aFeature in winState && !isNaN(winState[aFeature]))` → `features.push()`
- 条件付き依存: `if (winState.isPrivate)` → `features.push()`
- 条件付き依存: `if (tab.entries.length)` → `this.historyIndex()`
- 条件付き依存: `if (winState.isAIWindow)` → `lazy.AIWindow.handleAIWindowOptions()`
- 条件付き依存: `if (!args.length)` → `args.appendElement()`
- 条件付き依存: `if (winState.args?.[ARG_WEB_EXTENSION_POPUP_WINDOW])` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (winState.args?.[ARG_CHROMELESS_WINDOW])` → `extraOptions.setPropertyAsBool()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsIWebBrowserChrome.CHROME_ALL`, `Ci.nsIWritablePropertyBag2`, `aState.windows`, `args.length`, `tab.entries`, `tab.entries.length`, `tab.entries[activeIndex].url`, `winState.args`, `winState.chromeFlags`, `winState.closedId`, `winState.isAIWindow`, `winState.isPopup`, `winState.isPrivate`, `winState.selected`, `winState.tabs`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIWebBrowserChrome`](../../../dom/interfaces/base/nsIBrowserChild.idl.md) / [`nsIWritablePropertyBag2`](../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `Services.ww`

## _SessionStore.#serializePropertyBag()
- 位置: L7547-7553
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `bag.enumerator`

## _SessionStore.#isCmdLineEmpty()
- 位置: L7567-7587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aState.windows.every()`, `win.tabs.every()`
- 条件付き依存: `if (!pinnedOnly)` → `Cc["@mozilla.org/browser/clh;1"].getService()`
- 参照: `Cc["@mozilla.org/browser/clh;1"].getService( Ci.nsIBrowserHandler ).defaultArgs`, `Ci.nsIBrowserHandler`, `aState.windows`, `aWindow.arguments`, `tab.pinned`
- XPCOM: [`nsIBrowserHandler`](../nsIBrowserHandler.idl.md) / `@mozilla.org/browser/clh;1`

## _SessionStore.#getWindowDimension()
- 位置: L7602-7666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `baseWin.getPosition()`, `getBaseWindow()`
- 条件付き依存: `if (aWindow.windowState != aWindow.STATE_NORMAL)` → `parseInt()`
- 条件付き依存: `if (aWindow.windowState != aWindow.STATE_NORMAL)` → `docElem.getAttribute()`
- 条件付き依存: `if (attr)` → `aWindow.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (attr)` → `aWindow.docShell.treeOwner .QueryInterface()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `aWindow.STATE_FULLSCREEN`, `aWindow.STATE_MAXIMIZED`, `aWindow.STATE_MINIMIZED`, `aWindow.STATE_NORMAL`, `aWindow.document.documentElement`, `aWindow.outerHeight`, `aWindow.outerWidth`, `aWindow.windowState`, `appWin.outerToInnerHeightDifferenceInCSSPixels`, `appWin.outerToInnerWidthDifferenceInCSSPixels`, `baseWin.devicePixelsPerDesktopPixel`, `x.value`, `y.value`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md)

## _SessionStore.#needsRestorePage()
- 位置: L7678-7722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.#hasSingleTabWithURL()`, `this.#prefBranch.getIntPref()`
- 参照: `Services.appinfo.inSafeMode`, `aState.session`, `aState.session.lastUpdate`, `aState.windows`, `winData.length`
- XPCOM: `Services.appinfo`

## _SessionStore.#hasSingleTabWithURL()
- 位置: L7732-7744
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aWinData.length`, `aWinData[0].tabs`, `aWinData[0].tabs.length`, `aWinData[0].tabs[0].entries`, `aWinData[0].tabs[0].entries.length`, `aWinData[0].tabs[0].entries[0].url`

## _SessionStore.#shouldSaveTabState()
- 位置: L7755-7771
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aTabState.entries`, `aTabState.entries.length`, `aTabState.entries[0]?.url`, `aTabState.splitViewId`, `aTabState.userTypedValue`

## _SessionStore.shouldSaveTabsToGroup()
- 位置: L7784-7795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabState.collect()`, `this.#shouldSaveTabState()`

## _SessionStore.#shouldSaveTab()
- 位置: L7808-7818
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aTabState.attributes`, `aTabState.attributes.customizemode`, `aTabState.entries`, `aTabState.entries.length`, `aTabState.entries[0].url`, `aTabState.userTypedValue`

## _SessionStore.keepOnlyWorthSavingTabs()
- 位置: L7827-7857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aState._closedWindows.some()`, `this.#shouldSaveTab()`
- 条件付き依存: `if (!this.#shouldSaveTab(tab))` → `win.tabs.splice()`
- 条件付き依存: `if ( !win.tabs.length && (aState.windows.length > 1 || closedWindowShouldRestore || (closedWindowShouldRestore == null && (closedWindowShouldRestore = aState._cl...)` → `aState.windows.splice()`
- 参照: `aState.selectedWindow`, `aState.windows`, `aState.windows.length`, `w._shouldRestore`, `win.selected`, `win.tabs`, `win.tabs.length`

## _SessionStore.#prepDataForDeferredRestore()
- 位置: L7880-8067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `defaultState.savedGroups.find()`, `groupsToSave.forEach()`
- 条件付き依存: `if (PERSIST_SESSIONS)` → `Cu.cloneInto()`
- 条件付き依存: `if (window.tabs[tIndex].pinned)` → `newWindowState.tabs.concat()`
- 条件付き依存: `if (window.tabs[tIndex].pinned)` → `window.tabs.splice()`
- 条件付き依存: `if (window.tabs[tIndex].groupId)` → `window.groups.find()`
- 条件付き依存: `if (window.tabs[tIndex].groupId)` → `groupsToSave.get()`
- 条件付き依存: `if (!groupToSave)` → `lazy.TabGroupState.savedInClosedWindow()`
- 条件付き依存: `if (!groupToSave)` → `groupsToSave.set()`
- 条件付き依存: `if (window.tabs[tIndex].groupId)` → `this.formatTabStateForSavedGroup()`
- 条件付き依存: `if (tabData)` → `groupToSave.tabs.push()`
- 条件付き依存: `if (!window.tabs[tIndex].hidden && PERSIST_SESSIONS)` → `Math.min()`
- 条件付き依存: `if (!window.tabs[tIndex].hidden && PERSIST_SESSIONS)` → `Math.max()`
- 条件付き依存: `if (activeIndex in tabState.entries)` → `Date.now()`
- 条件付き依存: `if (activeIndex in tabState.entries)` → `this.#shouldSaveTabState()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.#saveClosedTabData()`
- 条件付き依存: `if (!(alreadySavedGroup))` → `defaultState.savedGroups.push()`
- 条件付き依存: `if (newWindowState.tabs.length)` → `WINDOW_ATTRIBUTES.forEach()`
- 条件付き依存: `if (newWindowState.tabs.length)` → `Date.now()`
- 条件付き依存: `if (newWindowState.tabs.length)` → `Math.random()`
- 条件付き依存: `if ( newWindowState.tabs.length || (PERSIST_SESSIONS && (newWindowState._closedTabs.length || newWindowState.closedGroups.length)) )` → `defaultState.windows.push()`
- 条件付き依存: `if (!window.tabs.length)` → `state.windows.splice()`
- 参照: `alreadySavedGroup.removeAfterRestore`, `defaultState.cookies`, `defaultState.savedGroups`, `defaultState.selectedIndex`, `defaultState.windows.length`, `existingGroup.id`, `group.removeAfterRestore`, `groupState.id`, `groupStateToSave.id`, `groupToSave.removeAfterRestore`, `newWindowState.__lastSessionWindowID`, `newWindowState._closedTabs`, `newWindowState._closedTabs.length`, `newWindowState.closedGroups`, `newWindowState.closedGroups.length`, `newWindowState.selected`, `newWindowState.sidebar`, `newWindowState.tabs`, `newWindowState.tabs.length`, `state.cookies`, `state.savedGroups`, `state.selectedWindow`, `state.windows`, `state.windows.length`, `tabState.entries`, `tabState.entries.length`, `tabState.entries[activeIndex].title`, `tabState.entries[activeIndex].url`, `tabState.image`, `tabState.index`, `window.__lastSessionWindowID`, `window._closedTabs`, `window.closedGroups`, `window.selected`, `window.sidebar`, `window.tabs`, `window.tabs.length`, `window.tabs[tIndex].groupId`, `window.tabs[tIndex].hidden`, `window.tabs[tIndex].pinned`

## _SessionStore.#sendRestoreCompletedNotifications()
- 位置: L8069-8109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserWindows [Symbol.iterator]()`, `this.#browserWindows [Symbol.iterator]() .some()`
- 条件付き依存: `if (this.#restoreCount > 1)` → `this.#log.warn()`
- 条件付き依存: `if (!this.#browserSetState)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!this.#browserSetState)` → `this.#log.debug()`
- 条件付き依存: `if (!this.#browserSetState)` → `this.#maybeOpenNewTabAfterRestore()`
- 条件付き依存: `if (!this.#browserSetState)` → `this.#deferredAllWindowsRestored.resolve()`
- 条件付き依存: `if (!(!this.#browserSetState))` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!anyWindowNotCloaked)` → `lazy.BrowserWindowTracker.openWindow()`
- 参照: `Symbol.iterator`, `this.#browserSetState`, `this.#browserWindows`, `this.#restoreCount`, `window.isCloaked`
- XPCOM: `Services.obs`

## _SessionStore.#isNewTabURL()
- 位置: L8111-8113
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AboutNewTab.newTabURL`

## _SessionStore.#getActiveURLFromTabData()
- 位置: L8115-8123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `this.historyIndex()`
- 参照: `tabData.entries`, `tabData.entries.length`, `tabData.entries[activeIndex]?.url`, `tabData?.entries?.length`

## _SessionStore.#maybeOpenNewTabAfterRestore()
- 位置: L8125-8213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.startupSessionAutoRestored.record()`, `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.NimbusFeatures.sessionRestoreNewTab.recordExposureEvent()`, `this.#log.debug()`, `this.#windowIds.get()`, `win.gBrowser.addTrustedTab()`
- 条件付き依存: `if (!this.#isUserConfiguredRestore)` → `this.#log.debug()`
- 条件付き依存: `if (!newTabOnRestore || !showSetting)` → `this.#log.debug()`
- 条件付き依存: `if (!newTabOnRestore || !showSetting)` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (this.#cmdLineHadURLOnStartup)` → `this.#log.debug()`
- 条件付き依存: `if (this.#cmdLineHadURLOnStartup)` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (windowState?.tabs?.length)` → `this.#getActiveURLFromTabData()`
- 条件付き依存: `if (windowState?.tabs?.length)` → `this.#isNewTabURL()`
- 条件付き依存: `if (this.#isNewTabURL(selectedURL))` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (this.#isNewTabURL(selectedURL))` → `this.#log.debug()`
- 条件付き依存: `if (windowState?.tabs?.length)` → `windowState.tabs.at()`
- 条件付き依存: `if (this.#isNewTabURL(lastTabURL))` → `win.gBrowser.visibleTabs.at()`
- 条件付き依存: `if (this.#isNewTabURL(lastTabURL))` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (this.#isNewTabURL(lastTabURL))` → `this.#log.debug()`
- 参照: `lazy.AboutNewTab.newTabURL`, `this.#cmdLineHadURLOnStartup`, `this.#isUserConfiguredRestore`, `this.#windows`, `win.gBrowser.selectedTab`, `windowState.selected`, `windowState.tabs`, `windowState?.tabs?.length`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## _SessionStore.#setWindowStateBusyValue()
- 位置: L8223-8233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isWindowLoaded()`, `this.#windowIds.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.get()`
- 参照: `stateToRestore.busy`, `this.#statesToRestore`, `this.#statesToRestore[WINDOW_RESTORE_IDS.get(aWindow)].windows`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].busy`

## _SessionStore.#setWindowStateReady()
- 位置: L8241-8252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowBusyStates.get()`, `this.#windowBusyStates.set()`
- 条件付き依存: `if (newCount == 0)` → `this.#setWindowStateBusyValue()`
- 条件付き依存: `if (newCount == 0)` → `this.#sendWindowStateReadyEvent()`

## _SessionStore.#setWindowStateBusy()
- 位置: L8260-8268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowBusyStates.get()`, `this.#windowBusyStates.set()`
- 条件付き依存: `if (newCount == 1)` → `this.#setWindowStateBusyValue()`
- 条件付き依存: `if (newCount == 1)` → `this.#sendWindowStateBusyEvent()`

## _SessionStore.#sendWindowStateReadyEvent()
- 位置: L8276-8280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendWindowStateBusyEvent()
- 位置: L8288-8292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendWindowRestoringNotification()
- 位置: L8300-8304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendWindowRestoredNotification()
- 位置: L8312-8316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendTabRestoredNotification()
- 位置: L8324-8328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.dispatchEvent()`, `aTab.ownerDocument.createEvent()`, `event.initEvent()`

## _SessionStore.#isWindowLoaded()
- 位置: L8337-8339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WINDOW_RESTORE_IDS.has()`

## _SessionStore.#capClosedWindows()
- 位置: L8346-8368
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (spliceTo < this.#closedWindows.length)` → `this.#closedWindows.splice()`
- 参照: `AppConstants.platform`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[normalWindowIndex].isPopup`, `this.#max_windows_undo`

## _SessionStore.#clearRestoringWindows()
- 位置: L8379-8383
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[i]._shouldRestore`

## _SessionStore.#resetRestoringState()
- 位置: L8388-8391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabRestoreQueue.reset()`
- 参照: `this.#tabsRestoringCount`

## _SessionStore.#resetLocalTabRestoringState()
- 位置: L8400-8430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.delete()`, `TAB_STATE_FOR_BROWSER.get()`, `aTab.removeAttribute()`, `browser.browsingContext.clearRestoreState()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`
- 条件付き依存: `if (!previousState)` → `console.error()`
- 条件付き依存: `if (previousState == TAB_STATE_NEEDS_RESTORE)` → `TabRestoreQueue.remove()`
- 参照: `aTab.linkedBrowser`, `browser.permanentKey`, `this.#tabsRestoringCount`

## _SessionStore.#resetTabRestoringState()
- 位置: L8432-8441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`, `this.#resetLocalTabRestoringState()`
- 条件付き依存: `if (!TAB_STATE_FOR_BROWSER.has(browser))` → `console.error()`
- 参照: `tab.linkedBrowser`

## _SessionStore.#startNextEpoch()
- 位置: L8452-8456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserEpochs.set()`, `this.#getCurrentEpoch()`

## _SessionStore.#getCurrentEpoch()
- 位置: L8465-8467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserEpochs.get()`

## _SessionStore.#isCurrentEpoch()
- 位置: L8481-8483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getCurrentEpoch()`

## _SessionStore.#resetEpoch()
- 位置: L8495-8500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserEpochs.delete()`
- 条件付き依存: `if (frameLoader)` → `frameLoader.requestEpochUpdate()`

## _SessionStore.#looseTimer()
- 位置: L8511-8535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `Math.ceil()`, `Promise.withResolvers()`, `deferred.promise.then()`, `timer.cancel()`, `timer.initWithCallback()`
- 条件付き依存: `if (beats <= 0)` → `this.#log.debug()`
- 条件付き依存: `if (beats <= 0)` → `Glean.sessionRestore.shutdownFlushAllOutcomes.timed_out.add()`
- 条件付き依存: `if (beats <= 0)` → `deferred.resolve()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_REPEATING_PRECISE_CAN_SKIP`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## _SessionStore.#waitForStateStop()
- 位置: L8537-8588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.withResolvers()`, `browser.addProgressListener()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`, `this.#restoreListeners.set()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`, `deferred.promise`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.unregister()
- 位置: L8541-8554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.#restoreListeners.delete()`, `browser.removeProgressListener()`
- 条件付き依存: `if (reject)` → `deferred.reject()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.onStateChange()
- 位置: L8556-8571
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( webProgress.isTopLevel && stateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && stateFlags & Ci.nsIWebProgressListener.STATE_STOP )` → `request.QueryInterface()`
- 条件付き依存: `if (url !== "about:blank" || aboutBlankOK)` → `this.unregister()`
- 条件付き依存: `if (url !== "about:blank" || aboutBlankOK)` → `deferred.resolve()`
- 参照: `Ci.nsIChannel`, `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_STOP`, `request.QueryInterface(Ci.nsIChannel).originalURI.spec`, `webProgress.isTopLevel`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _SessionStore.#listenForNavigations()
- 位置: L8590-8643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `browser.addProgressListener()`, `browser.browsingContext?.sessionHistory?.addSHistoryListener()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`, `this.#restoreListeners.set()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.unregister()
- 位置: L8592-8603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.#restoreListeners.delete()`, `browser.browsingContext?.sessionHistory?.removeSHistoryListener()`, `browser.removeProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.OnHistoryReload()
- 位置: L8605-8608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callbacks.onHistoryReload()`, `this.unregister()`

## _SessionStore.OnHistoryNewEntry()
- 位置: L8611-8611
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.OnHistoryGotoIndex()
- 位置: L8612-8612
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.OnHistoryPurge()
- 位置: L8613-8613
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.OnHistoryReplaceEntry()
- 位置: L8614-8614
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.onStateChange()
- 位置: L8616-8625
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( webProgress.isTopLevel && stateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && stateFlags & Ci.nsIWebProgressListener.STATE_START )` → `this.unregister()`
- 条件付き依存: `if ( webProgress.isTopLevel && stateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && stateFlags & Ci.nsIWebProgressListener.STATE_START )` → `callbacks.onStartRequest()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_START`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _SessionStore.#restoreHistory()
- 位置: L8653-8701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStoreUtils.restoreDocShellState()`, `browser.stop()`, `lazy.SessionHistory.restoreFromParent()`, `promise.then()`, `promise.then(onResolve).catch()`, `this.#tabStateRestorePromises.set()`, `this.#tabStateToRestore.set()`
- 参照: `browser.browsingContext`, `browser.browsingContext.sessionHistory`, `browser.permanentKey`, `data.tabData`, `data.tabData.index`, `data.tabData?.disallow`, `data.tabData?.entries`, `data.tabData?.entries[data.tabData.index - 1]?.url`

## onResolve()
- 位置: L8675-8698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `this.#restoreHistoryComplete()`, `this.#tabStateRestorePromises.delete()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.get(browser) !== TAB_STATE_RESTORING)` → `this.#listenForNavigations()`
- 参照: `browser.permanentKey`

## onHistoryReload()
- 位置: L8680-8683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreTabContentForBrowser()`

## onStartRequest()
- 位置: L8688-8691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreTabContentForBrowser()`, `this.#tabStateToRestore.delete()`
- 参照: `browser.permanentKey`

## _SessionStore.#restoreTabEntry()
- 位置: L8712-8746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `browser.browsingContext.fixupAndLoadURIString()`, `this.#waitForStateStop()`
- 条件付き依存: `if (!haveUserTypedValue && tabData.entries.length)` → `SessionStoreUtils.initializeRestore()`
- 条件付き依存: `if (!haveUserTypedValue && tabData.entries.length)` → `lazy.SessionStoreHelper.buildRestoreData()`
- 条件付き依存: `if (!haveUserTypedValue)` → `this.#waitForStateStop()`
- 条件付き依存: `if (!haveUserTypedValue)` → `browser.browsingContext.loadURI()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP`, `Ci.nsIWebNavigation.LOAD_FLAGS_BYPASS_HISTORY`, `browser.browsingContext`, `lazy.blankURI`, `tabData.entries.length`, `tabData.formdata`, `tabData.scroll`, `tabData.userTypedClear`, `tabData.userTypedValue`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## _SessionStore.#restoreTabContentForBrowser()
- 位置: L8757-8779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `Promise.allSettled(promises).then()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`, `this.#restoreTabContentComplete()`, `this.#restoreTabContentStarted()`, `this.#tabStateRestorePromises.get()`, `this.#tabStateToRestore.delete()`, `this.#tabStateToRestore.get()`
- 条件付き依存: `if (state)` → `promises.push()`
- 条件付き依存: `if (state)` → `this.#restoreTabEntry()`
- 条件付き依存: `if (!(state))` → `promises.push()`
- 条件付き依存: `if (!(state))` → `this.#waitForStateStop()`
- 参照: `browser.permanentKey`, `state.tabData`

## _SessionStore.#sendRestoreTabContent()
- 位置: L8781-8783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreTabContentForBrowser()`

## _SessionStore.#restoreHistoryComplete()
- 位置: L8785-8801
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `event.initEvent()`, `lazy.TabState.collect()`, `tab.dispatchEvent()`, `this.#updateTabLabelAndIcon()`, `win.document.createEvent()`, `win?.gBrowser.getTabForBrowser()`
- 参照: `browser.documentGlobal`

## _SessionStore.#restoreTabContentStarted()
- 位置: L8803-8870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `lazy.TabStateCache.get()`, `win?.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!initiatedBySessionStore || isNavigateAndRestore)` → `lazy.TabStateCache.update()`
- 条件付き依存: `if (!initiatedBySessionStore)` → `this.#markTabAsRestoring()`
- 条件付き依存: `if (!isNavigateAndRestore)` → `lazy.TabState.collect()`
- 条件付き依存: `if (!isNavigateAndRestore)` → `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (tab.selected)` → `win.gURLBar.setURI()`
- 条件付き依存: `if (!isNavigateAndRestore)` → `lazy.TabStateCache.update()`
- 参照: `RESTORE_TAB_CONTENT_REASON.NAVIGATE_AND_RESTORE`, `browser.documentGlobal`, `browser.permanentKey`, `browser.userTypedValue`, `cacheState.searchMode`, `data.reason`, `tab.selected`, `tabData.userTypedClear`, `tabData.userTypedValue`

## _SessionStore.#restoreTabContentComplete()
- 位置: L8872-8905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `SessionStore.#resetLocalTabRestoringState()`, `SessionStore.#restoreNextTab()`, `lazy.TabStateCache.get()`, `this.#sendTabRestoredNotification()`, `win?.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (cacheState.searchMode)` → `win.gURLBar.setSearchMode()`
- 条件付き依存: `if (tab.selected)` → `win.gURLBar.setURI()`
- 条件付き依存: `if (cacheState.searchMode)` → `lazy.TabStateCache.update()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Services.obs.notifyObservers()`
- 参照: `browser.documentGlobal`, `browser.permanentKey`, `browser.userTypedValue`, `cacheState.searchMode`, `cacheState.userTypedValue`, `tab.selected`
- XPCOM: `Services.obs`

## _SessionStore.#sendRestoreHistory()
- 位置: L8919-8933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreHistory()`
- 条件付き依存: `if (options.tabData.storage)` → `SessionStoreUtils.restoreSessionStorageFromParent()`
- 条件付き依存: `if (browser && browser.frameLoader)` → `browser.frameLoader.requestEpochUpdate()`
- 参照: `browser.browsingContext`, `browser.frameLoader`, `options.epoch`, `options.tabData.storage`

## _SessionStore.addSavedTabGroup()
- 位置: L8940-8957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `lazy.TabGroupState.savedInOpenWindow()`, `this.#collectClosedTabsForTabGroup()`, `this.#collectSplitViewDataForTabGroup()`, `this.#recordSavedTabGroupState()`, `this.#windowIds.get()`
- 参照: `tabGroup.documentGlobal`, `tabGroup.tabs`, `tabGroupState.splitViews`, `tabGroupState.tabs`

## _SessionStore.addTabsToSavedGroup()
- 位置: L8968-9007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.addTab.record()`, `PrivateBrowsingUtils.isWindowPrivate()`, `tabGroupState.splitViews.push()`, `tabGroupState.tabs.push()`, `tabs.every()`, `this.#collectClosedTabsForTabGroup()`, `this.#collectSplitViewDataForTabGroup()`, `this.#notifyOfSavedTabGroupsChange()`, `this.getSavedTabGroup()`
- 参照: `TabMetrics.METRIC_GROUP_TYPE.SAVED`, `TabMetrics.METRIC_SOURCE.UNKNOWN`, `TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `metricsContext?.telemetrySource`, `tab.documentGlobal`, `tabGroupState.splitViews`, `tabs.length`, `tabs[0].documentGlobal`, `win.gBrowser.tabContainer.verticalMode`

## _SessionStore.#recordSavedTabGroupState()
- 位置: L9013-9022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notifyOfSavedTabGroupsChange()`, `this.#savedGroups.push()`, `this.getSavedTabGroup()`
- 参照: `savedTabGroupState.id`, `savedTabGroupState.tabs.length`

## _SessionStore.getSavedTabGroup()
- 位置: L9030-9034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#savedGroups.find()`
- 参照: `savedTabGroup.id`

## _SessionStore.getSavedTabGroups()
- 位置: L9041-9043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`
- 参照: `this.#savedGroups`

## _SessionStore.#getClosedTabGroup()
- 位置: L9050-9055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resolveClosedDataSource()`, `winData?.closedGroups.find()`
- 参照: `closedGroup.id`

## _SessionStore.undoCloseTabGroup()
- 位置: L9068-9117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `Glean.tabgroup.groupInteractions.open_recent.add()`, `Glean.tabgroup.reopen.record()`, `PrivateBrowsingUtils.isWindowPrivate()`, `group.select()`, `this.#createTabsForSavedOrClosedTabGroup()`, `this.#getClosedTabGroup()`, `this.#resolveClosedDataSource()`, `this.#windowIds.get()`, `this.forgetClosedTabGroup()`
- 条件付き依存: `if (targetWindow && !this.#windowIds.get(targetWindow))` → `Components.Exception()`
- 条件付き依存: `if (!targetWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if ( isPrivateSource !== PrivateBrowsingUtils.isWindowPrivate(targetWindow) )` → `Components.Exception()`
- 条件付き依存: `if (!tabGroupData)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `TabMetrics.METRIC_REOPEN_TYPE.DELETED`, `TabMetrics.METRIC_SOURCE.RECENT_TABS`, `TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `sourceWinData.isPrivate`, `sourceWinData.lastClosedTabGroupId`, `targetWindow.gBrowser.tabContainer.verticalMode`

## _SessionStore.openSavedTabGroup()
- 位置: L9134-9205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.reopen.record()`, `PrivateBrowsingUtils.isWindowPrivate()`, `group.select()`, `this.#createTabsForSavedOrClosedTabGroup()`, `this.#windowIds.get()`, `this.forgetSavedTabGroup()`, `this.getSavedTabGroup()`
- 条件付き依存: `if (!targetWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if (!this.#windowIds.get(targetWindow))` → `Components.Exception()`
- 条件付き依存: `if (source == TabMetrics.METRIC_SOURCE.SUGGEST)` → `Glean.tabgroup.groupInteractions.open_suggest.add()`
- 条件付き依存: `if (source == TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU)` → `Glean.tabgroup.groupInteractions.open_tabmenu.add()`
- 条件付き依存: `if (source == TabMetrics.METRIC_SOURCE.RECENT_TABS)` → `Glean.tabgroup.groupInteractions.open_recent.add()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(targetWindow))` → `Components.Exception()`
- 条件付き依存: `if (!tabGroupData)` → `Components.Exception()`
- 条件付き依存: `if (tabGroupData.windowClosedId)` → `this.#getClosedWindowDataByClosedId()`
- 条件付き依存: `if (closedWinData)` → `this.#removeSavedTabGroupFromClosedWindow()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `TabMetrics.METRIC_REOPEN_TYPE.SAVED`, `TabMetrics.METRIC_SOURCE.RECENT_TABS`, `TabMetrics.METRIC_SOURCE.SUGGEST`, `TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU`, `TabMetrics.METRIC_SOURCE.UNKNOWN`, `TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `tabGroupData.id`, `tabGroupData.windowClosedId`, `targetWindow.gBrowser.tabContainer.verticalMode`

## _SessionStore.#createTabsForSavedOrClosedTabGroup()
- 位置: L9212-9224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabGroupData.tabs.map()`, `targetWindow.gBrowser.createTabsForSessionRestore()`, `this.#restoreTabs()`
- 参照: `tab.state`, `tabGroupData.splitViews`, `tabs[0].group`

## _SessionStore.#cleanupOrphanedClosedGroups()
- 位置: L9241-9251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (winData.closedGroups[index].tabs.length === 0)` → `winData.closedGroups.splice()`
- 参照: `this.#closedObjectsChanged`, `winData.closedGroups`, `winData.closedGroups.length`, `winData.closedGroups[index].tabs.length`

## _SessionStore.#removeSavedTabGroupFromClosedWindow()
- 位置: L9258-9262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `removeWhere()`
- 参照: `closedWinData.groups`, `closedWinData.tabs`, `tab.groupId`, `tabGroup.id`, `this.#closedObjectsChanged`

## _SessionStore.isFormatVersionCompatible()
- 位置: L9271-9288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Number.isNaN()`, `Number.parseFloat()`

## _SessionStore.validateState()
- 位置: async L9298-9323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `fetch()`, `fetch( "moz-src:///browser/components/sessionstore/session.schema.json" ).then()`, `lazy.JsonSchema.validate()`, `rsp.json()`
- 条件付き依存: `if (!state)` → `this.getCurrentState()`
- 条件付き依存: `if (!result.valid)` → `console.warn()`
- 参照: `ex.message`, `result.errors`, `result.valid`, `state.deferredInitialState`, `state.lastSessionState`

## _SessionStore.historyIndex()
- 位置: L9333-9335
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabData.entries.length`, `tabData.index`

## restoreOnDemand()
- 位置: L9354-9365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateValue()`
- XPCOM: `Services.prefs`

## updateValue()
- 位置: L9355-9360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## restorePinnedTabsOnDemand()
- 位置: L9368-9379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateValue()`
- XPCOM: `Services.prefs`

## updateValue()
- 位置: L9369-9374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## restoreHiddenTabs()
- 位置: L9382-9393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateValue()`
- XPCOM: `Services.prefs`

## updateValue()
- 位置: L9383-9388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## reset()
- 位置: L9397-9399
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tabs`

## add()
- 位置: L9402-9412
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tab.pinned)` → `priority.push()`
- 条件付き依存: `if (tab.hidden)` → `hidden.push()`
- 条件付き依存: `if (!(tab.hidden))` → `visible.push()`
- 参照: `tab.hidden`, `tab.pinned`, `this.tabs`

## remove()
- 位置: L9415-9431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `set.indexOf()`
- 条件付き依存: `if (index == -1)` → `set.indexOf()`
- 条件付き依存: `if (index > -1)` → `set.splice()`
- 参照: `tab.hidden`, `this.tabs`

## shift()
- 位置: L9434-9451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `set.shift()`
- 参照: `hidden.length`, `priority.length`, `this.prefs`, `this.prefs.restoreHiddenTabs`, `this.tabs`, `visible.length`

## hiddenToVisible()
- 位置: L9454-9462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hidden.indexOf()`
- 条件付き依存: `if (index > -1)` → `hidden.splice()`
- 条件付き依存: `if (index > -1)` → `visible.push()`
- 参照: `this.tabs`

## visibleToHidden()
- 位置: L9465-9473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `visible.indexOf()`
- 条件付き依存: `if (index > -1)` → `visible.splice()`
- 条件付き依存: `if (index > -1)` → `hidden.push()`
- 参照: `this.tabs`

## willRestoreSoon()
- 位置: L9484-9506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidateSet.indexOf()`
- 条件付き依存: `if (restorePinned && priority.length)` → `candidateSet.push()`
- 条件付き依存: `if (visible.length)` → `candidateSet.push()`
- 条件付き依存: `if (restoreHiddenTabs && hidden.length)` → `candidateSet.push()`
- 参照: `hidden.length`, `priority.length`, `this.prefs`, `this.tabs`, `visible.length`

## has()
- 位置: L9515-9517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.has()`

## get()
- 位置: L9519-9521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.get()`

## set()
- 位置: L9523-9525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.set()`

## remove()
- 位置: L9527-9529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.delete()`

## has()
- 位置: L9537-9539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.has()`

## add()
- 位置: L9541-9543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.set()`

## remove()
- 位置: L9545-9547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.delete()`

## clear()
- 位置: L9549-9551
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._data`

## canRestore()
- 位置: L9561-9563
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## getState()
- 位置: L9565-9567
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## setState()
- 位置: L9569-9571
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## clear()
- 位置: L9573-9580
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!silent)` → `Services.obs.notifyObservers()`
- 参照: `this._state`
- XPCOM: `Services.obs`

## getBaseWindow()
- 位置: L9592-9594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.docShell.treeOwner.QueryInterface()`
- 参照: `Ci.nsIBaseWindow`
- XPCOM: `nsIBaseWindow`

## removeWhere()
- 位置: L9601-9607
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `predicate()`
- 条件付き依存: `if (predicate(array[i]))` → `array.splice()`
- 参照: `array.length`
