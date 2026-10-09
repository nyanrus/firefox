# browser/extensions/newtab/lib/TelemetryFeed.sys.mjs

source: browser/extensions/newtab/lib/TelemetryFeed.sys.mjs
source-hash: 72bf1186057c070fd680100ed9a0efdbf73a1d8b
lines: 3171

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## isCardColumnSupported()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`
- 参照: `AppConstants.MOZ_APP_VERSION`
- XPCOM: `Services.vc`

## isAdEligiblePositionSupported()
- 位置: L73-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`
- 参照: `AppConstants.MOZ_APP_VERSION`
- XPCOM: `Services.vc`

## TelemetryFeed.constructor()
- 位置: L253-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `this.getOrCreateImpressionId()`
- 参照: `GleanSessionType.PrivateGleanSession`, `lazy.NewTabContentPing`, `this._aboutHomeSeen`, `this._adsClient`, `this._browserOpenNewtabStart`, `this._classifySite`, `this._gleanSessionInitialized`, `this._impressionId`, `this._initialized`, `this._prefs`, `this._privateRandomContentTelemetryProbablityValues`, `this.gleanSessionType`, `this.newtabContentPing`, `this.sessions`

## TelemetryFeed.telemetryEnabled()
- 位置: L284-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`

## TelemetryFeed.privatePingEnabled()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`

## TelemetryFeed.privatePingInferredInterestsEnabled()
- 位置: L292-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`

## TelemetryFeed.trainhopClickOnlyEnabled()
- 位置: L306-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs.values?.trainhopConfig?.newtabPrivatePing ?.clickOnly`

## TelemetryFeed.trainhopOptimizeInferredEnabled()
- 位置: L320-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs.values?.trainhopConfig?.newtabPrivatePing ?.optimizeInferred`

## TelemetryFeed.sectionsPersonalizationEnabled()
- 位置: L327-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`

## TelemetryFeed.inferredInterests()
- 位置: L331-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 参照: `this.store?.getState()?.InferredPersonalization ?.coarsePrivateInferredInterests`

## TelemetryFeed.inferredTelemetrySettingsOverrides()
- 位置: L336-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 参照: `this.store?.getState()?.InferredPersonalization ?.inferredTelemetrySettingsOverrides`

## TelemetryFeed.hasRecordedClicksInCIV()
- 位置: L348-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `coarsePrivate.values.some()`, `this.store?.getState()`
- 参照: `coarsePrivate.values`, `coarsePrivate.values.length`, `inferredPersonalization.coarsePrivateInferredInterests`, `inferredPersonalization.inferredInterests?.clicks`, `inferredPersonalization?.initialized`, `this.store?.getState()?.InferredPersonalization`

## TelemetryFeed.initializeGleanSession()
- 位置: L379-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasRecordedClicksInCIV()`, `this.sovEnabled()`
- 参照: `GleanSessionType.NormalGleanSession`, `GleanSessionType.PrivateGleanSession`, `this._gleanSessionInitialized`, `this.gleanSessionType`, `this.privatePingEnabled`, `this.privatePingInferredInterestsEnabled`, `this.trainhopClickOnlyEnabled`, `this.trainhopOptimizeInferredEnabled`

## TelemetryFeed.initializeMac()
- 位置: L410-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AdsClient.isEnabled()`, `this.store?.getState()`
- 条件付き依存: `if (lazy.AdsClient.isEnabled(this.store?.getState()?.Prefs.values))` → `lazy.AdsClient.getClient()`
- 参照: `this._adsClient`, `this.store?.getState()?.Prefs.values`

## TelemetryFeed.#clearEventBuffer()
- 位置: L426-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`
- 条件付き依存: `if (!(sessionId === undefined))` → `this.#eventBuffer.filter()`
- 条件付き依存: `if (recordToContentPing && this.privatePingEnabled)` → `this.newtabContentPing.recordEvent()`
- 参照: `event.sessionId`, `this.#eventBuffer`, `this.#eventBuffer.length`, `this.privatePingEnabled`

## TelemetryFeed.#discardEventBuffer()
- 位置: L456-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#eventBuffer.filter()`
- 参照: `event.sessionId`, `this.#eventBuffer`

## TelemetryFeed.#flushBufferedEventsOnUninit()
- 位置: L469-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings.newtab.submit()`, `Services.prefs.getBoolPref()`, `this.#clearEventBuffer()`
- 参照: `GleanSessionType.PrivateGleanSession`, `this.#eventBuffer.length`, `this.gleanSessionType`, `this.telemetryEnabled`
- XPCOM: `Services.prefs`

## TelemetryFeed.recordOrQueueEvent()
- 位置: L498-507
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.gleanSessionType === GleanSessionType.NormalGleanSession)` → `this.#eventBuffer.push()`
- 条件付き依存: `if (!(this.gleanSessionType === GleanSessionType.NormalGleanSession))` → `callback()`
- 条件付き依存: `if (this.privatePingEnabled)` → `this.newtabContentPing.recordEvent()`
- 参照: `GleanSessionType.NormalGleanSession`, `this.gleanSessionType`, `this.privatePingEnabled`

## TelemetryFeed.transitionToPrivateSession()
- 位置: L513-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearEventBuffer()`
- 参照: `GleanSessionType.PrivateGleanSession`, `this.gleanSessionType`

## TelemetryFeed.clientInfo()
- 位置: L522-524
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ClientEnvironmentBase`

## TelemetryFeed.canSendUnifiedAdsSpocCallbacks()
- 位置: L526-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`
- 参照: `this.SHOW_SPONSORED_STORIES_ENABLED`

## TelemetryFeed.canSendUnifiedAdsTilesCallbacks()
- 位置: L534-540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`
- 参照: `this.SHOW_SPONSORED_TOPSITES_ENABLED`

## TelemetryFeed.telemetryClientId()
- 位置: L542-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `lazy.ClientID.getClientID()`
- 参照: `this.telemetryClientId`

## TelemetryFeed.processStartTs()
- 位置: L549-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.startup.getStartupInfo()`, `startupInfo.process.getTime()`
- 参照: `this.processStartTs`
- XPCOM: `Services.startup`

## TelemetryFeed.init()
- 位置: L559-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.deletionRequest.impressionId.set()`, `Glean.newtab.locale.set()`, `this._beginObservingNewtabPingPrefs()`
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!lazy.ContextId.rotationEnabled)` → `Glean.deletionRequest.contextId.set()`
- 条件付き依存: `if (!lazy.ContextId.rotationEnabled)` → `lazy.ContextId.requestSynchronously()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.ContextId.rotationEnabled`, `this._impressionId`, `this._initialized`, `this.browserOpenNewtabStart`
- XPCOM: `Services.locale` / `Services.obs`

## TelemetryFeed.getOrCreateImpressionId()
- 位置: L586-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`
- 条件付き依存: `if (!impressionId)` → `String()`
- 条件付き依存: `if (!impressionId)` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (!impressionId)` → `this._prefs.set()`
- XPCOM: `Services.uuid`

## TelemetryFeed.browserOpenNewtabStart()
- 位置: L595-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Math.round()`
- 参照: `this._browserOpenNewtabStart`, `this.processStartTs`

## TelemetryFeed.getFollowedSections()
- 位置: L611-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 条件付き依存: `if (sections)` → `Object.entries(sections).filter()`
- 条件付き依存: `if (sections)` → `Object.entries()`
- 条件付き依存: `if (sections)` → `followed.sort()`
- 条件付き依存: `if (sections)` → `followed.slice(0, 2).map()`
- 条件付き依存: `if (sections)` → `followed.slice()`
- 参照: `a[1].followedAt`, `b[1].followedAt`, `info.isFollowed`, `this.store?.getState()?.DiscoveryStream.sectionPersonalization`

## TelemetryFeed.setLoadTriggerInfo()
- 位置: L631-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.saveSessionPerfData()`
- 参照: `this._browserOpenNewtabStart`

## TelemetryFeed.userPreferences()
- 位置: L672-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this._prefs.get()`

## TelemetryFeed.redactNewTabPing()
- 位置: L692-743
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.content_redacted`

## TelemetryFeed.addSession()
- 位置: L752-804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uuid.generateUUID()`, `String()`, `this.sessions.set()`
- 参照: `session.perf.load_trigger_ts`, `this._aboutHomeSeen`, `this.processStartTs`
- XPCOM: `Services.uuid`

## TelemetryFeed.endSession()
- 位置: async L811-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.newtab.closed.record()`, `Math.round()`, `Services.prefs.getBoolPref()`, `this.#stopDwellClock()`, `this.sessions.delete()`, `this.sessions.get()`
- 条件付き依存: `if (!session.perf.visibility_event_rcvd_ts)` → `this.#discardEventBuffer()`
- 条件付き依存: `if (!session.perf.visibility_event_rcvd_ts)` → `this.sessions.delete()`
- 条件付き依存: `if ( this.telemetryEnabled && Services.prefs.getBoolPref(PREF_NEWTAB_PING_ENABLED, true) )` → `Math.round()`
- 条件付き依存: `if (dwellMs > 0)` → `Glean.newtab.dwellTime.accumulateSingleSample()`
- 条件付き依存: `if ( this.telemetryEnabled && Services.prefs.getBoolPref(PREF_NEWTAB_PING_ENABLED, true) )` → `this.#clearEventBuffer()`
- 条件付き依存: `if ( this.telemetryEnabled && Services.prefs.getBoolPref(PREF_NEWTAB_PING_ENABLED, true) )` → `Glean.newtab[metric]?.set()`
- 条件付き依存: `if ( this.telemetryEnabled && Services.prefs.getBoolPref(PREF_NEWTAB_PING_ENABLED, true) )` → `GleanPings.newtab.submit()`
- 条件付き依存: `if (this.privatePingEnabled)` → `this.configureContentPing()`
- 参照: `Glean.newtab`, `GleanSessionType.PrivateGleanSession`, `session.dwellTimeMs`, `session.max_scroll_threshold`, `session.perf.load_trigger_ts`, `session.perf.topsites_first_painted_ts`, `session.perf.visibility_event_rcvd_ts`, `session.session_duration`, `session.session_id`, `this.gleanSessionType`, `this.privatePingEnabled`, `this.processStartTs`, `this.telemetryEnabled`
- XPCOM: `Services.prefs`

## TelemetryFeed.getActiveChromeWindow()
- 位置: L886-888
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.focus.activeWindow`
- XPCOM: `Services.focus`

## TelemetryFeed.now()
- 位置: L895-897
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`

## TelemetryFeed.isDwellTargetInForeground()
- 位置: L911-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.browserRef?.deref()`, `this.getActiveChromeWindow()`
- 参照: `browser?.documentGlobal`, `win.closed`, `win.gBrowser?.selectedBrowser`

## TelemetryFeed.#dwellTargets()
- 位置: L931-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openedPages.values()`, `this.sessions.values()`

## TelemetryFeed.#onUserInteractionActive()
- 位置: L944-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dwellTargets()`, `this.#syncOpenedPages()`, `this.getActiveChromeWindow()`, `this.isDwellTargetInForeground()`, `this.now()`
- 条件付き依存: `if (!( // Newtab sessions have no committed flag. Only opened pages wait. (target.committed ?? true) && this.isDwellTargetInForeground(target, activeWindow) ))` → `this.#stopDwellClock()`
- 参照: `target.committed`, `target.dwellStartedAt`, `this.#lastActiveAt`, `this.#openedPages.size`, `this.#userActive`, `this.sessions.size`

## TelemetryFeed.#onUserInteractionInactive()
- 位置: L977-984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dwellTargets()`, `this.#stopDwellClock()`, `this.#syncOpenedPages()`, `this.now()`
- 参照: `this.#lastActiveAt`, `this.#userActive`

## TelemetryFeed.#startDwellClockIfActive()
- 位置: L993-1001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isDwellTargetInForeground()`
- 条件付き依存: `if ( target.dwellStartedAt === null && this.#userActive && this.isDwellTargetInForeground(target) )` → `this.now()`
- 参照: `target.dwellStartedAt`, `this.#userActive`

## TelemetryFeed.#stopDwellClock()
- 位置: L1009-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.now()`
- 参照: `target.dwellStartedAt`, `target.dwellTimeMs`

## TelemetryFeed.handleDwellLinkOpened()
- 位置: L1024-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DWELL_LABELS.has()`, `this.#openedPages.get()`, `this.#openedPages.set()`
- 条件付き依存: `if (previous)` → `this.#finalizeOpenedPage()`
- 条件付き依存: `if (this.#openedPages.size >= MAX_TRACKED_OPENED_PAGES)` → `this.#finalizeOpenedPage()`
- 条件付き依存: `if (this.#openedPages.size >= MAX_TRACKED_OPENED_PAGES)` → `this.#openedPages.values().next()`
- 条件付き依存: `if (this.#openedPages.size >= MAX_TRACKED_OPENED_PAGES)` → `this.#openedPages.values()`
- 参照: `action.data`, `browser.permanentKey`, `this.#openedPages.size`, `this.#openedPages.values().next().value`

## TelemetryFeed.#syncOpenedPages()
- 位置: L1065-1097
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `page.browserRef.deref()`, `this.#openedPages.values()`
- 条件付き依存: `if (!browser?.isConnected)` → `this.#finalizeOpenedPage()`
- 条件付き依存: `if (!isWebPage || windowId !== page.windowId)` → `this.#finalizeOpenedPage()`
- 参照: `browser.browsingContext?.currentWindowGlobal`, `browser?.isConnected`, `page.committed`, `page.windowId`, `uri?.scheme`, `windowGlobal?.documentURI`, `windowGlobal?.innerWindowId`

## TelemetryFeed.#finalizeOpenedPage()
- 位置: L1108-1121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `this.#openedPages.delete()`, `this.#stopDwellClock()`, `this.now()`
- 条件付き依存: `if (dwellMs > 0 && this.telemetryEnabled)` → `Glean.newtab.openedPageDwellTime?.[page.label]?.accumulateSingleSample()`
- 参照: `Glean.newtab.openedPageDwellTime`, `page.dwellTimeMs`, `page.key`, `page.label`, `this.telemetryEnabled`

## TelemetryFeed.handleNewTabInit()
- 位置: L1129-1149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.data.browser.getAttribute()`, `au.getPortIdOfSender()`, `this.#openedPages.get()`, `this.addSession()`
- 条件付き依存: `if (opened)` → `this.#finalizeOpenedPage()`
- 参照: `action.data.browser`, `action.data.browser.permanentKey`, `action.data.url`, `session.browserRef`, `session.perf.is_preloaded`

## TelemetryFeed.handleNewTabScroll()
- 位置: L1157-1166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `au.getPortIdOfSender()`, `this.sessions.get()`
- 参照: `action.data.threshold`, `session.max_scroll_threshold`

## TelemetryFeed.sovEnabled()
- 位置: L1168-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs`, `values?.trainhopConfig?.sov?.enabled`

## TelemetryFeed.frecencyBoostedHasExposure()
- 位置: L1174-1177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs`

## TelemetryFeed.handleTopSitesSponsoredImpressionStats()
- 位置: async L1179-1277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (type === "impression")` → `Glean.contextualServicesTopsites.impression[ `${source}_${legacyTelemetryPosition}` ].add()`
- 条件付き依存: `if (session)` → `this.sovEnabled()`
- 条件付き依存: `if (this.sovEnabled())` → `this.frecencyBoostedHasExposure()`
- 条件付き依存: `if (this.sovEnabled())` → `isAdEligiblePositionSupported()`
- 条件付き依存: `if (this.sovEnabled())` → `this.recordOrQueueEvent()`
- 条件付き依存: `if (!(this.sovEnabled()))` → `isAdEligiblePositionSupported()`
- 条件付き依存: `if (!(this.sovEnabled()))` → `Glean.topsites.impression.record()`
- 条件付き依存: `if (type === "click")` → `Glean.contextualServicesTopsites.click[ `${source}_${legacyTelemetryPosition}` ].add()`
- 条件付き依存: `if (!(this.sovEnabled()))` → `Glean.topsites.click.record()`
- 条件付き依存: `if (!(type === "click"))` → `console.error()`
- 条件付き依存: `if (this._adsClient)` → `this.sendMacCallbackEvent()`
- 条件付き依存: `if (!(this._adsClient))` → `this.sendUnifiedAdsCallbackEvent()`
- 参照: `Glean.contextualServicesTopsites.click`, `Glean.contextualServicesTopsites.impression`, `data.reporting_url`, `session.session_id`, `this._adsClient`, `this.canSendUnifiedAdsTilesCallbacks`

## TelemetryFeed.handleTopSitesOrganicImpressionStats()
- 位置: L1279-1318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.topsites.click.record()`, `Glean.topsites.impression.record()`, `JSON.stringify()`, `au.getPortIdOfSender()`, `isAdEligiblePositionSupported()`, `this.sessions.get()`
- 参照: `action.data.isPinned`, `action.data.is_ad_eligible_position`, `action.data.position`, `action.data.smart_scores`, `action.data.smart_weights`, `action.data?.type`, `action.data?.visible_topsites`, `session.session_id`

## TelemetryFeed.handleSpocPlaceholderDuration()
- 位置: L1329-1334
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (duration !== undefined && duration >= 0)` → `Glean.pocket.spocPlaceholderDuration.accumulateSingleSample()`
- 参照: `action.data`

## TelemetryFeed.handleUserEvent()
- 位置: L1336-1399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.appearanceExploreMoreThemesClick.record()`, `Glean.newtab.customizePanelOpen.record()`, `Glean.newtab.customizePanelSubpanelOpen.record()`, `Glean.newtab.weatherDetectLocation.record()`, `Glean.topsites.add.record()`, `Glean.topsites.edit.record()`, `Glean.topsites.pin.record()`, `Glean.topsites.unpin.record()`, `au.getPortIdOfSender()`, `this.sessions.get()`
- 参照: `action.data.action_position`, `action.data.has_title_changed`, `action.data.has_url_changed`, `action.data.source`, `action.data?.event`, `session.session_id`

## TelemetryFeed.getAllRecommendations()
- 位置: L1404-1409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(merinoData ?? {}).flatMap()`, `this.store?.getState()`
- 参照: `feed?.data?.recommendations`, `this.store?.getState()?.DiscoveryStream?.feeds.data`

## TelemetryFeed.getAllSections()
- 位置: L1414-1419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(merinoData ?? {}).flatMap()`, `this.store?.getState()`
- 参照: `feed?.data?.sections`, `this.store?.getState()?.DiscoveryStream?.feeds.data`

## TelemetryFeed.getRecommendationCount()
- 位置: L1424-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(merinoData ?? {}).reduce()`, `this.store?.getState()`
- 参照: `feed.data?.recommendations?.length`, `this.store?.getState()?.DiscoveryStream?.feeds.data`

## TelemetryFeed.randomizeOrganicContentEvent()
- 位置: L1441-1512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabContentPing.decideWithProbability()`, `lazy.NewTabContentPing.secureRandIntInRange()`, `this.getAllRecommendations()`
- 条件付き依存: `if (!("n" in this._privateRandomContentTelemetryProbablityValues))` → `this.getRecommendationCount()`
- 条件付き依存: `if (!(cache_key in this._privateRandomContentTelemetryProbablityValues))` → `Math.exp()`
- 条件付き依存: `if (sectionPositions)` → `allRecs.filter()`
- 条件付き依存: `if (sectionPositions)` → `sectionPositions.has()`
- 条件付き依存: `if ( resultItem.section && resultItem.section !== TOP_STORIES_SECTION_NAME && randomItem.section )` → `sectionPositions?.get()`
- 条件付き依存: `if ( resultItem.section && resultItem.section !== TOP_STORIES_SECTION_NAME && randomItem.section )` → `this.getAllSections().find()`
- 条件付き依存: `if ( resultItem.section && resultItem.section !== TOP_STORIES_SECTION_NAME && randomItem.section )` → `this.getAllSections()`
- 参照: `allRecs.length`, `item.is_sponsored`, `randomItem.corpus_item_id`, `randomItem.section`, `randomItem.source_section_id`, `randomItem.topic`, `randomItem.variant_id`, `rec.section`, `resultItem.layout_name`, `resultItem.section`, `resultItem.section_position`, `resultItem.variant_id`, `section.sectionKey`, `session?.sectionPositions`, `this._privateRandomContentTelemetryProbablityValues`, `this._privateRandomContentTelemetryProbablityValues.n`, `this._privateRandomContentTelemetryProbablityValues?.epsilon`, `this.getAllSections().find( section => section.sectionKey === randomItem.section )?.layout?.name`

## TelemetryFeed.handleDiscoveryStreamUserEvent()
- 位置: L1514-1665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.handleUserEvent()`, `this.sessions.get()`
- 条件付き依存: `if ( action.data.source === "POPULAR_TOPICS" || card_type === "topics_widget" )` → `Glean.pocket.topicClick.record()`
- 条件付き依存: `if (action.data.source === "FEATURE_HIGHLIGHT")` → `Glean.newtab.tooltipClick.record()`
- 条件付き依存: `if (!(action.data.source === "FEATURE_HIGHLIGHT"))` → `["spoc", "organic"].includes()`
- 条件付き依存: `if (["spoc", "organic"].includes(card_type))` → `isCardColumnSupported()`
- 条件付き依存: `if (this.trainhopClickOnlyEnabled)` → `this.transitionToPrivateSession()`
- 条件付き依存: `if (["spoc", "organic"].includes(card_type))` → `this.recordOrQueueEvent()`
- 条件付き依存: `if (["spoc", "organic"].includes(card_type))` → `this.randomizeOrganicContentEvent()`
- 条件付き依存: `if (["spoc", "organic"].includes(card_type))` → `Glean.pocket.click.record()`
- 条件付き依存: `if (["spoc", "organic"].includes(card_type))` → `this.redactNewTabPing()`
- 条件付き依存: `if (this._adsClient)` → `this.sendMacCallbackEvent()`
- 条件付き依存: `if (!(this._adsClient))` → `this.sendUnifiedAdsCallbackEvent()`
- 条件付き依存: `if (action.data.event === "FEATURE_HIGHLIGHT_DISMISS")` → `Glean.newtab.featureHighlightDismiss.record()`
- 条件付き依存: `if (action.data.event === "FEATURE_HIGHLIGHT_IMPRESSION")` → `Glean.newtab.featureHighlightImpression.record()`
- 条件付き依存: `if (action.data.event === "FEATURE_HIGHLIGHT_OPEN")` → `Glean.newtab.featureHighlightOpen.record()`
- 参照: `action.data`, `action.data.action_position`, `action.data.event`, `action.data.source`, `action.data.value`, `action.data?.event`, `action.data?.value`, `session.session_id`, `this._adsClient`, `this.canSendUnifiedAdsSpocCallbacks`, `this.sectionsPersonalizationEnabled`, `this.trainhopClickOnlyEnabled`

## TelemetryFeed.sendMacCallbackEvent()
- 位置: async L1671-1696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowed.some()`, `lazy.AdsClient.callbackOptions()`, `url.startsWith()`
- 条件付き依存: `if (event === "impression")` → `this._adsClient.recordImpression()`
- 条件付き依存: `if (event === "click")` → `this._adsClient.recordClick()`
- 参照: `this.allowedEndpoints`

## TelemetryFeed.sendUnifiedAdsCallbackEvent()
- 位置: async L1702-1793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `allowed.some()`, `console.error()`, `data.url.startsWith()`, `url.searchParams.append()`, `url.toString()`
- 条件付き依存: `if (!ohttpRelayURL)` → `console.error()`
- 条件付き依存: `if (!ohttpConfigURL)` → `console.error()`
- 条件付き依存: `if (marsOhttpEnabled)` → `lazy.ObliviousHTTP.getOHTTPConfig()`
- 条件付き依存: `if (!config)` → `console.error()`
- 条件付き依存: `if (marsOhttpEnabled)` → `lazy.ObliviousHTTP.ohttpRequest()`
- 条件付き依存: `if (!(marsOhttpEnabled))` → `fetch()`
- 参照: `data.position`, `data.url`, `this.allowedEndpoints`
- XPCOM: `Services.prefs`

## TelemetryFeed.sendPageTakeoverData()
- 位置: async L1795-1861
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.telemetryEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.newtabpage.enabled"))` → `lazy.ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if ( lazy.AboutNewTab.newTabURLOverridden && !lazy.ExtensionUtils.isExtensionUrl(lazy.AboutNewTab.newTabURL) )` → `this._classifySite()`
- 条件付き依存: `if (this.telemetryEnabled)` → `lazy.ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (this.telemetryEnabled)` → `lazy.ExtensionSettingsStore.getSetting()`
- 条件付き依存: `if (this.telemetryEnabled)` → `lazy.HomePage.get()`
- 条件付き依存: `if (this.telemetryEnabled)` → `["about:home", "about:blank", BLANK_HOMEPAGE_URL].includes()`
- 条件付き依存: `if (this.telemetryEnabled)` → `lazy.ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if ( !["about:home", "about:blank", BLANK_HOMEPAGE_URL].includes( homePageURL ) && !lazy.ExtensionUtils.isExtensionUrl(homePageURL) )` → `this._classifySite()`
- 条件付き依存: `if (this.telemetryEnabled)` → `Glean.newtab.newtabCategory.set()`
- 条件付き依存: `if (this.telemetryEnabled)` → `Glean.newtab.homepageCategory.set()`
- 条件付き依存: `if (this.privatePingEnabled)` → `this.configureContentPing()`
- 条件付き依存: `if (Services.prefs.getBoolPref(PREF_NEWTAB_PING_ENABLED, true))` → `GleanPings.newtab.submit()`
- 参照: `homeExtensionInfo.id`, `lazy.AboutNewTab.newTabURL`, `lazy.AboutNewTab.newTabURLOverridden`, `lazy.HomePage.overridden`, `newtabExtensionInfo.id`, `this.privatePingEnabled`, `this.telemetryEnabled`, `value.home_extension_id`, `value.home_url_category`, `value.newtab_extension_id`, `value.newtab_url_category`
- XPCOM: `Services.prefs`

## TelemetryFeed.configureContentPing()
- 位置: async L1867-1954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.NimbusFeatures.pocketNewtab.getEnrollmentMetadata()`, `this._prefs.get()`, `this.newtabContentPing.scheduleSubmission()`, `this.newtabContentPing.setMaxClickEventsPerDay()`, `this.newtabContentPing.setMaxClickEventsPerWeek()`, `this.newtabContentPing.setMaxEventsPerDay()`, `this.store?.getState()`
- 条件付き依存: `if (!reduceTrackingInformation)` → `this.getFollowedSections()`
- 条件付き依存: `if (PRIVATE_PING_SURFACE_COUNTRY_MAP[surfaceId])` → `PRIVATE_PING_SURFACE_COUNTRY_MAP[ surfaceId ].includes()`
- 条件付き依存: `if (prefs?.inferredPersonalizationConfig?.normalized_time_zone_offset)` → `lazy.NewTabUtils.getUtcOffset()`
- 参照: `experimentMetadata?.branch`, `experimentMetadata?.slug`, `lazy.Region.home`, `prefs?.inferredPersonalizationConfig?.normalized_time_zone_offset`, `prefs?.trainhopConfig?.newtabPrivatePing`, `privateMetrics.country`, `privateMetrics.experimentBranch`, `privateMetrics.experimentName`, `privateMetrics.followedSections`, `privateMetrics.inferredInterests`, `privateMetrics.pingVersion`, `privateMetrics.surfaceId`, `privateMetrics.utcOffset`, `this._privateRandomContentTelemetryProbablityValues`, `this.inferredInterests`, `this.inferredTelemetrySettingsOverrides .random_content_click_probability_epsilon_micro`, `this.inferredTelemetrySettingsOverrides ?.random_content_click_probability_epsilon_micro`, `this.inferredTelemetrySettingsOverrides.daily_click_event_cap`, `this.inferredTelemetrySettingsOverrides?.daily_click_event_cap`, `this.inferredTelemetrySettingsOverrides?.iv_in_telemetry`, `this.privatePingInferredInterestsEnabled`, `this.store?.getState()?.Prefs.values`
- XPCOM: `Services.prefs`

## TelemetryFeed.onAction()
- 位置: async L1956-2120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WALLPAPER_USER_EVENTS.has()`, `au.getPortIdOfSender()`, `this.endSession()`, `this.handleAboutSponsoredTopSites()`, `this.handleBlockUrl()`, `this.handleCardSectionUserEvent()`, `this.handleCarouselUserEvent()`, `this.handleDiscoveryStreamImpressionStats()`, `this.handleDiscoveryStreamUserEvent()`, `this.handleDwellLinkOpened()`, `this.handleInlineSelectionUserEvent()`, `this.handleNewTabInit()`, `this.handleNewTabScroll()`, `this.handlePromoCardUserEvent()`, `this.handleReportAdUserEvent()`, `this.handleReportContentUserEvent()`, `this.handleSetPref()`, `this.handleSpacesUserEvent()`, `this.handleSpocPlaceholderDuration()`, `this.handleTopSitesOrganicImpressionStats()`, `this.handleTopSitesSponsoredImpressionStats()`, `this.handleTopicNavigationUserEvent()`, `this.handleTopicSelectionUserEvent()`, `this.handleUnifiedWidgetContainerAction()`, `this.handleUnifiedWidgetEnabled()`, `this.handleUnifiedWidgetError()`, `this.handleUnifiedWidgetImpression()`, `this.handleUnifiedWidgetUserEvent()`, `this.handleUserEvent()`, `this.handleWeatherUserEvent()`, `this.handleWidgetsHideAll()`, `this.handleWidgetsUserEvent()`, `this.init()`, `this.initializeGleanSession()`, `this.initializeMac()`, `this.recordEnabledWidgets()`, `this.recordPageLayoutVariant()`, `this.saveSessionPerfData()`, `this.sendPageTakeoverData()`, `this.sessions.get()`, `this.uninit()`
- 条件付き依存: `if (WALLPAPER_USER_EVENTS.has(action.type))` → `this.handleWallpaperUserEvent()`
- 条件付き依存: `if (session)` → `action.data.sections.map()`
- 条件付き依存: `if (action.data?.name === "recordsHistory")` → `this.recordEnabledWidgets()`
- 参照: `action.data`, `action.data?.name`, `action.type`, `at.ABOUT_SPONSORED_TOP_SITES`, `at.BLOCK_SECTION`, `at.BLOCK_URL`, `at.CARD_SECTIONS_ORDER`, `at.CARD_SECTION_IMPRESSION`, `at.CAROUSEL_NAVIGATE`, `at.CAROUSEL_TOGGLE_AUTOPLAY`, `at.CLICK_SECTION_LEARN_MORE`, `at.DISCOVERY_STREAM_IMPRESSION_STATS`, `at.DISCOVERY_STREAM_SPOC_PLACEHOLDER_DURATION`, `at.DISCOVERY_STREAM_USER_EVENT`, `at.DWELL_LINK_OPENED`, `at.FOLLOW_SECTION`, `at.INIT`, `at.INLINE_SELECTION_CLICK`, `at.INLINE_SELECTION_IMPRESSION`, `at.NEW_TAB_INIT`, `at.NEW_TAB_SCROLL`, `at.NEW_TAB_UNLOAD`, `at.PREFS_INITIAL_VALUES`, `at.PREF_CHANGED`, `at.PROMO_CARD_CLICK`, `at.PROMO_CARD_DISMISS`, `at.PROMO_CARD_IMPRESSION`, `at.REPORT_AD_SUBMIT`, `at.REPORT_CONTENT_OPEN`, `at.REPORT_CONTENT_SUBMIT`, `at.SAVE_SESSION_PERF_DATA`, `at.SET_PREF`, `at.SPACES_USER_EVENT`, `at.TELEMETRY_USER_EVENT`, `at.TOPIC_NAVIGATION_CLICK`, `at.TOPIC_SELECTION_USER_DISMISS`, `at.TOPIC_SELECTION_USER_OPEN`, `at.TOPIC_SELECTION_USER_SAVE`, `at.TOP_SITES_ORGANIC_IMPRESSION_STATS`, `at.TOP_SITES_SPONSORED_IMPRESSION_STATS`, `at.UNBLOCK_SECTION`, `at.UNFOLLOW_SECTION`, `at.UNINIT`, `at.WEATHER_IMPRESSION`, `at.WEATHER_LOAD_ERROR`, `at.WEATHER_LOCATION_DATA_UPDATE`, `at.WEATHER_OPEN_PROVIDER_URL`, `at.WEATHER_OPT_IN_PROMPT_SELECTION`, `at.WIDGETS_CONTAINER_ACTION`, `at.WIDGETS_ENABLED`, `at.WIDGETS_ERROR`, `at.WIDGETS_HIDE_ALL`, `at.WIDGETS_IMPRESSION`, `at.WIDGETS_LISTS_USER_EVENT`, `at.WIDGETS_LISTS_USER_IMPRESSION`, `at.WIDGETS_TIMER_USER_EVENT`, `at.WIDGETS_TIMER_USER_IMPRESSION`, `at.WIDGETS_USER_EVENT`, `session.sectionPositions`

## TelemetryFeed.handlePromoCardUserEvent()
- 位置: L2122-2141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.promoCardClick.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.promoCardDismiss.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.promoCardImpression.record()`
- 参照: `action.type`, `at.PROMO_CARD_CLICK`, `at.PROMO_CARD_DISMISS`, `at.PROMO_CARD_IMPRESSION`, `session.session_id`

## TelemetryFeed.handleWidgetsUserEvent()
- 位置: L2145-2172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsListsUserEvent.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsListsImpression.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsTimerUserEvent.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsTimerImpression.record()`
- 参照: `action.data.userAction`, `action.type`, `session.session_id`

## TelemetryFeed.handleSpacesUserEvent()
- 位置: L2174-2184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.spacesSwitch.record()`
- 参照: `action.data.method`, `action.data.previous_space`, `action.data.space`, `session.session_id`

## TelemetryFeed.handleUnifiedWidgetUserEvent()
- 位置: L2186-2206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (action.data.action_value !== undefined)` → `String()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsUserEvent.record()`
- 参照: `action.data.action_value`, `action.data.user_action`, `action.data.widget_name`, `action.data.widget_size`, `action.data.widget_source`, `payload.action_value`, `payload.widget_size`, `session.session_id`

## TelemetryFeed.handleUnifiedWidgetImpression()
- 位置: L2208-2222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsImpression.record()`
- 参照: `action.data.widget_name`, `action.data.widget_size`, `payload.widget_size`, `session.session_id`

## TelemetryFeed.handleUnifiedWidgetContainerAction()
- 位置: L2224-2242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsContainerAction.record()`
- 参照: `action.data.action_type`, `action.data.action_value`, `action.data.widget_size`, `payload.action_value`, `payload.widget_size`, `session.session_id`

## TelemetryFeed.handleUnifiedWidgetEnabled()
- 位置: L2244-2261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsEnabled.record()`
- 条件付き依存: `if (session)` → `this.recordEnabledWidgets()`
- 参照: `action.data.enabled`, `action.data.widget_name`, `action.data.widget_size`, `action.data.widget_source`, `payload.widget_size`, `session.session_id`

## TelemetryFeed.recordEnabledWidgets()
- 位置: L2263-2274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.widgetsEnabledList.set()`, `WIDGET_REGISTRY.filter()`, `WIDGET_REGISTRY.filter(w => isWidgetEnabled(w, prefs, widgetsEnabled) ).map()`, `isWidgetEnabled()`, `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs.values`, `w.telemetryName`

## TelemetryFeed.recordPageLayoutVariant()
- 位置: L2278-2284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.pageLayoutVariant.set()`, `resolvePageLayoutVariant()`, `this.store?.getState()`
- 参照: `this.store?.getState()?.Prefs.values`

## TelemetryFeed.handleWidgetsHideAll()
- 位置: L2286-2305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleUnifiedWidgetContainerAction()`
- 条件付き依存: `if (target.active)` → `this.handleUnifiedWidgetEnabled()`
- 参照: `action.data`, `target.active`, `target.telemetryName`

## TelemetryFeed.handleUnifiedWidgetError()
- 位置: L2307-2322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.widgetsError.record()`
- 参照: `action.data.error_type`, `action.data.widget_name`, `action.data.widget_size`, `payload.widget_size`, `session.session_id`

## TelemetryFeed.allowedEndpoints()
- 位置: L2324-2332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.trim()`, `this._prefs .get()`, `this._prefs .get(PREF_ENDPOINTS) .split()`, `this._prefs .get(PREF_ENDPOINTS) .split(",") .map()`, `this._prefs .get(PREF_ENDPOINTS) .split(",") .map(item => item.trim()) .filter()`

## TelemetryFeed.handleReportAdUserEvent()
- 位置: async L2334-2388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowed.some()`, `console.error()`, `reporting_url.startsWith()`
- 条件付き依存: `if (this._adsClient)` → `report_reason.toUpperCase()`
- 条件付き依存: `if (this._adsClient)` → `lazy.AdsClient.callbackOptions()`
- 条件付き依存: `if (this._adsClient)` → `this._adsClient.reportAd()`
- 条件付き依存: `if (!(this._adsClient))` → `url.searchParams.append()`
- 条件付き依存: `if (!(this._adsClient))` → `url.toString()`
- 条件付き依存: `if (!(this._adsClient))` → `fetch()`
- 参照: `action.data`, `lazy.MozAdsReportReason`, `this._adsClient`, `this.allowedEndpoints`

## TelemetryFeed.handleReportContentUserEvent()
- 位置: L2390-2440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtabContent.reportContentOpen.record()`
- 条件付き依存: `if (this.privatePingEnabled)` → `Glean.newtabContent.reportContentSubmit.record()`
- 参照: `action.data`, `action.type`, `this.privatePingEnabled`

## TelemetryFeed.handleCarouselUserEvent()
- 位置: L2442-2468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.carouselNavigate.record()`, `Glean.newtab.carouselToggleAutoplay.record()`, `au.getPortIdOfSender()`, `this.sessions.get()`
- 参照: `action.data`, `action.type`, `session.session_id`

## TelemetryFeed.handleCardSectionUserEvent()
- 位置: L2470-2576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.sectionsBlockSection.record()`
- 条件付き依存: `if (session)` → `this.redactNewTabPing()`
- 条件付き依存: `if (this.privatePingEnabled)` → `this.newtabContentPing.recordEvent()`
- 条件付き依存: `if (session)` → `Glean.newtab.sectionsUnblockSection.record()`
- 条件付き依存: `if (session)` → `this.recordOrQueueEvent()`
- 条件付き依存: `if (session)` → `Glean.newtab.sectionsImpression.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.sectionsFollowSection.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.sectionsUnfollowSection.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.sectionsLearnMore.record()`
- 参照: `action.data`, `action.type`, `session.session_id`, `this.privatePingEnabled`, `this.sectionsPersonalizationEnabled`

## TelemetryFeed.handleInlineSelectionUserEvent()
- 位置: L2578-2602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.inlineSelectionClick.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.inlineSelectionImpression.record()`
- 参照: `action.data`, `action.data.section_position`, `action.type`, `session.session_id`

## TelemetryFeed.handleTopicNavigationUserEvent()
- 位置: L2604-2616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.topicNavigationClick.record()`, `au.getPortIdOfSender()`, `this.sessions.get()`
- 参照: `action.data`, `session.session_id`

## TelemetryFeed.handleTopicSelectionUserEvent()
- 位置: L2618-2644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `Glean.newtab.topicSelectionOpen.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.topicSelectionDismiss.record()`
- 条件付き依存: `if (session)` → `Glean.newtab.topicSelectionTopicsSaved.record()`
- 参照: `action.data.first_save`, `action.data.previous_topics`, `action.data.topics`, `action.type`, `session.session_id`

## TelemetryFeed.handleSetPref()
- 位置: L2646-2679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.weatherChangeDisplay.record()`, `Glean.newtab.widgetsListsChangeDisplay.record()`, `Glean.newtab.widgetsTimerChangeDisplay.record()`, `Glean.topsites.changeDisplay.record()`, `au.getPortIdOfSender()`, `this.recordEnabledWidgets()`, `this.sessions.get()`
- 参照: `action.data.name`, `action.data.value`, `session.session_id`

## TelemetryFeed.handleWeatherUserEvent()
- 位置: L2681-2719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.weatherImpression.record()`, `Glean.newtab.weatherLoadError.record()`, `Glean.newtab.weatherLocationSelected.record()`, `Glean.newtab.weatherOpenProviderUrl.record()`, `Glean.newtab.weatherOptInSelection.record()`, `au.getPortIdOfSender()`, `this.sessions.get()`
- 参照: `action.data`, `action.type`, `session.session_id`

## TelemetryFeed.handleWallpaperUserEvent()
- 位置: L2721-2796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtab.wallpaperCategoryClick.record()`, `Glean.newtab.wallpaperClick.record()`, `Glean.newtab.wallpaperHighlightCtaClick.record()`, `Glean.newtab.wallpaperHighlightDismissed.record()`, `Glean.newtab.wallpaperSavedAdd.record()`, `Glean.newtab.wallpaperSavedClick.record()`, `Glean.newtab.wallpaperSavedRemove.record()`, `au.getPortIdOfSender()`, `this.sessions.get()`
- 参照: `action.data`, `action.type`, `data.saved_wallpaper_count`, `data.wallpaper_source`, `data.was_applied`, `session.session_id`

## TelemetryFeed.handleBlockUrl()
- 位置: L2798-2876
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (this.trainhopClickOnlyEnabled)` → `this.transitionToPrivateSession()`
- 条件付き依存: `if (datum.is_pocket_card)` → `this.recordOrQueueEvent()`
- 条件付き依存: `if (datum.is_pocket_card)` → `Glean.pocket.dismiss.record()`
- 条件付き依存: `if (datum.is_pocket_card)` → `this.redactNewTabPing()`
- 条件付き依存: `if (action.source === "TOP_SITES")` → `this.sovEnabled()`
- 条件付き依存: `if (this.sovEnabled() && isSponsoredTopSite)` → `this.recordOrQueueEvent()`
- 条件付き依存: `if (!(this.sovEnabled() && isSponsoredTopSite))` → `Glean.topsites.dismiss.record()`
- 参照: `action.source`, `datum.card_type`, `datum.format`, `datum.is_pocket_card`, `datum.is_section_followed`, `datum.position`, `datum.received_rank`, `datum.recommended_at`, `datum.section`, `datum.section_position`, `gleanData.is_sponsored`, `session.session_id`, `this.sectionsPersonalizationEnabled`, `this.trainhopClickOnlyEnabled`

## TelemetryFeed.handleAboutSponsoredTopSites()
- 位置: L2878-2900
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.getPortIdOfSender()`, `this.sessions.get()`
- 条件付き依存: `if (session)` → `this.sovEnabled()`
- 条件付き依存: `if (this.privatePingEnabled)` → `this.newtabContentPing.recordEvent()`
- 条件付き依存: `if (!(this.sovEnabled()))` → `Glean.topsites.showPrivacyClick.record()`
- 参照: `session.session_id`, `this.privatePingEnabled`

## TelemetryFeed.handleDiscoveryStreamImpressionStats()
- 位置: L2908-2982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.pocket.impression.record()`, `isAdEligiblePositionSupported()`, `isCardColumnSupported()`, `this.recordOrQueueEvent()`, `this.redactNewTabPing()`, `this.sessions.get()`, `tiles.forEach()`
- 条件付き依存: `if (this._adsClient)` → `this.sendMacCallbackEvent()`
- 条件付き依存: `if (!(this._adsClient))` → `this.sendUnifiedAdsCallbackEvent()`
- 参照: `session.session_id`, `this._adsClient`, `this.canSendUnifiedAdsSpocCallbacks`, `this.sectionsPersonalizationEnabled`, `tile.card_column`, `tile.format`, `tile.is_ad_eligible_position`, `tile.is_list_card`, `tile.is_section_followed`, `tile.layout_name`, `tile.pos`, `tile.received_rank`, `tile.recommended_at`, `tile.section`, `tile.section_position`, `tile.selectedTopics`, `tile.shim`, `tile.source_section_id`, `tile.topic`, `tile.type`, `tile.variant_id`

## TelemetryFeed.saveSessionPerfData()
- 位置: L2997-3043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Services.prefs.getIntPref()`, `this.sessions.get()`
- 条件付き依存: `if (data.visibility_event_rcvd_ts && session.page !== "about:home")` → `this.setLoadTriggerInfo()`
- 条件付き依存: `if ( timestamp && session.page === "about:home" && !lazy.HomePage.overridden && Services.prefs.getIntPref("browser.startup.page") === 1 )` → `lazy.AboutNewTab.maybeRecordTopsitesPainted()`
- 条件付き依存: `if (data.visibility_event_rcvd_ts && !session.newtabOpened)` → `this.#startDwellClockIfActive()`
- 条件付き依存: `if (data.visibility_event_rcvd_ts && !session.newtabOpened)` → `ONBOARDING_ALLOWED_PAGE_VALUES.includes()`
- 条件付き依存: `if (data.visibility_event_rcvd_ts && !session.newtabOpened)` → `Glean.newtab.opened.record()`
- 参照: `data.topsites_first_painted_ts`, `data.visibility_event_rcvd_ts`, `data.window_inner_height`, `data.window_inner_width`, `lazy.HomePage.overridden`, `session.newtabOpened`, `session.page`, `session.perf`, `session.session_id`
- XPCOM: `Services.prefs`

## TelemetryFeed._beginObservingNewtabPingPrefs()
- 位置: L3045-3058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Services.prefs.addObserver()`, `this._setBlockedSponsorsMetrics()`, `this._setNewtabPrefMetrics()`, `this._setTopicSelectionSelectedTopicsMetrics()`
- XPCOM: `Services.prefs`

## TelemetryFeed._stopObservingNewtabPingPrefs()
- 位置: L3060-3064
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## TelemetryFeed.observe()
- 位置: L3066-3085
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onUserInteractionActive()`, `this.#onUserInteractionInactive()`
- 条件付き依存: `if (data === TOP_SITES_BLOCKED_SPONSORS_PREF)` → `this._setBlockedSponsorsMetrics()`
- 条件付き依存: `if (data === TOPIC_SELECTION_SELECTED_TOPICS_PREF)` → `this._setTopicSelectionSelectedTopicsMetrics()`
- 条件付き依存: `if (!(data === TOPIC_SELECTION_SELECTED_TOPICS_PREF))` → `this._setNewtabPrefMetrics()`

## TelemetryFeed._setNewtabPrefMetrics()
- 位置: async L3087-3113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prefs.getPrefType()`, `fullPrefName.slice()`, `metric.set()`
- 条件付き依存: `if (isChanged)` → `Glean.topsites.prefChanged.record()`
- 条件付き依存: `if (isChanged)` → `Services.prefs.getBoolPref()`
- 参照: `ACTIVITY_STREAM_PREF_BRANCH.length`, `Services.prefs.PREF_BOOL`, `Services.prefs.PREF_INT`
- XPCOM: `Services.prefs`

## TelemetryFeed._setBlockedSponsorsMetrics()
- 位置: L3115-3125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`
- 条件付き依存: `if (blocklist)` → `Glean.newtab.blockedSponsors.set()`
- XPCOM: `Services.prefs`

## TelemetryFeed._setTopicSelectionSelectedTopicsMetrics()
- 位置: L3127-3141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 条件付き依存: `if (topiclist)` → `topiclist.split(",").map()`
- 条件付き依存: `if (topiclist)` → `topiclist.split()`
- 条件付き依存: `if (topiclist)` → `s.trim()`
- 条件付き依存: `if (topiclist)` → `Glean.newtab.selectedTopics.set()`
- XPCOM: `Services.prefs`

## TelemetryFeed.uninit()
- 位置: L3143-3169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#finalizeOpenedPage()`, `this.#flushBufferedEventsOnUninit()`, `this.#openedPages.values()`, `this._stopObservingNewtabPingPrefs()`, `this.newtabContentPing.uninit()`
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this.#lastActiveAt`, `this.#userActive`, `this._initialized`, `this.browserOpenNewtabStart`
- XPCOM: `Services.obs`
