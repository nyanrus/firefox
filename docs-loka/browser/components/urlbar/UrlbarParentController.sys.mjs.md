# browser/components/urlbar/UrlbarParentController.sys.mjs

source: browser/components/urlbar/UrlbarParentController.sys.mjs
source-hash: 7be7375183959d9f388b364a955e036164d2739d
lines: 2620

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Promise.resolve()`, `lazy.UrlbarShared.getLogger()`

## engineToEngineInfo()
- 位置: L63-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.isNew()`
- 参照: `engine.aliases`, `engine.hideOneOffButton`, `engine.id`, `engine.isGeneralPurposeEngine`, `engine.isNewUntil`, `engine.name`, `lazy.AppProvidedConfigEngine`, `lazy.ConfigSearchEngine`

## UrlbarParentController.constructor()
- 位置: L144-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.ProvidersManager.getInstanceForSap()`, `lazy.UrlbarProviderTopSites.addTopSitesListener()`
- 参照: `this.#actor`, `this.#isAddressbar`, `this.#topSitesListener`, `this.engagementEvent`, `this.isPrivate`, `this.manager`, `this.sapName`
- XPCOM: `Services.obs`

## UrlbarParentController.platform()
- 位置: L170-172
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## UrlbarParentController.input()
- 位置: L179-181
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#child?.input`

## UrlbarParentController.browserWindow()
- 位置: L190-192
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#actor?.browsingContext?.topChromeWindow`

## UrlbarParentController.rendersInContentProcess()
- 位置: L201-203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#actor?.browsingContext?.isContent`

## UrlbarParentController.resolveTargetBrowser()
- 位置: L215-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`
- 参照: `browsingContext.top.embedderElement`, `browsingContext?.isContent`, `target?.embedderElement`, `this.#actor?.browsingContext`

## UrlbarParentController.view()
- 位置: L231-233
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#child?.view`

## UrlbarParentController.onBeforeSelection()
- 位置: L245-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.manager .getProvider()`, `this.manager .getProvider(result?.providerName) ?.tryMethod()`
- 参照: `result?.providerName`

## UrlbarParentController.onSelection()
- 位置: L257-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.manager .getProvider()`, `this.manager .getProvider(result?.providerName) ?.tryMethod()`
- 参照: `result?.providerName`

## UrlbarParentController.getHeuristicResult()
- 位置: async L272-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.manager.startQuery()`
- 参照: `queryContext.heuristicResult`

## UrlbarParentController.resolveFallbackNavigation()
- 位置: async L304-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbar.heuristicResultMissing.addToDenominator()`, `Glean.urlbar.heuristicResultMissing.addToNumerator()`, `Services.uriFixup.getFixupURIInfo()`, `browser.getAttribute()`, `console.error()`, `gBrowser.getTabForBrowser()`, `lazy.UrlbarUtils.getPostDataString()`, `navigated()`, `parseInt()`, `this.getHeuristicResult()`, `this.resolveTargetBrowser()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `browser.lastLocationChange`, `gBrowser.getTabForBrowser(browser)?.group?.id`, `gBrowser.selectedBrowser`, `lazy.UrlbarQueryContext`, `options.searchMode`, `options.sources`, `preferredURI.spec`, `searchMode.source`, `this.browserWindow`, `this.isPrivate`, `this.sapName`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## navigated()
- 位置: L320-321
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browser.lastLocationChange`

## UrlbarParentController.startQuery()
- 位置: async L400-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbar.autocompleteFirstResultTime.start()`, `Glean.urlbar.autocompleteSixthResultTime.start()`, `this.cancelQuery()`, `this.manager.startQuery()`, `this.notify()`
- 条件付き依存: `if ( contextWrapper === this._lastQueryContextWrapper && !contextWrapper.done )` → `this.manager.cancelQuery()`
- 条件付き依存: `if ( contextWrapper === this._lastQueryContextWrapper && !contextWrapper.done )` → `this.notify()`
- 参照: `contextWrapper.done`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_FINISHED`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_STARTED`, `queryContext.firstTimerId`, `queryContext.lastResultCount`, `queryContext.sixthTimerId`, `this._lastQueryContextWrapper`

## UrlbarParentController.recordEngagement()
- 位置: L448-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTelemetryUtils.recordedEngagementFromWire()`, `this.engagementEvent.recordFromChild()`
- 参照: `this.liveResults`

## UrlbarParentController.resetEngagement()
- 位置: L461-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engagementEvent.reset()`

## UrlbarParentController.startTrackingBuiltBounce()
- 位置: L473-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engagementEvent.startTrackingBuiltBounce()`

## UrlbarParentController.recordSearchMode()
- 位置: L484-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.BrowserSearchTelemetry.recordSearchMode()`

## UrlbarParentController.recordAutofillBackspace()
- 位置: L500-502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarUtils.recordAutofillBackspace()`

## UrlbarParentController.recordAutofillDeletion()
- 位置: L507-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbar.autofillDeletion.add()`

## UrlbarParentController.dismissAutofill()
- 位置: async L522-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarAutofill.inputContextMenuDismissal[action].add()`, `lazy.UrlbarUtils.dismissAutofill()`
- 参照: `Glean.urlbarAutofill.inputContextMenuDismissal`

## UrlbarParentController.clearAutofillBackspaceEntryForUrl()
- 位置: L541-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarUtils.clearAutofillBackspaceEntryForUrl()`

## UrlbarParentController.handleAutofillReintegration()
- 位置: L554-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#doHandleAutofillReintegration()`, `this.#doHandleAutofillReintegration(url).catch()`
- 参照: `UrlbarParentController._lastAutofillReintegrationPromise`, `console.error`

## UrlbarParentController.#doHandleAutofillReintegration()
- 位置: async L559-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarAutofill.reintegration[level].add()`, `lazy.UrlbarUtils.reintegrateAutofill()`
- 条件付き依存: `if (backspaceBlock)` → `Glean.urlbarAutofill.reintegrationAfterBackspace[ level ].accumulateSingleSample()`
- 条件付き依存: `if (backspaceBlock)` → `Date.now()`
- 参照: `Glean.urlbarAutofill.reintegration`, `Glean.urlbarAutofill.reintegrationAfterBackspace`, `backspaceBlock.blockedAt`

## UrlbarParentController.recordSearchForm()
- 位置: L586-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchForm()`, `lazy.SearchService.getEngineById()`
- 参照: `this.sapName`

## UrlbarParentController.recordSearch()
- 位置: L610-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordSearchForBrowser()`
- 参照: `this.browserWindow.gBrowser.selectedBrowser`

## UrlbarParentController.#recordSearchForBrowser()
- 位置: L621-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `lazy.ASRouter.sendTriggerMessage()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.SearchService.getEngineById()`
- 条件付き依存: `if (totalSearches < 100)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `new Date().toISOString()`
- 条件付き依存: `if (this.sapName == "newtab_searchbar")` → `lazy.AboutNewTab.getVisitId()`
- 条件付き依存: `if (engine)` → `lazy.UrlbarUtils.addToFormHistory( this.isPrivate || opensInPrivateWindow, query, engine.name ).catch()`
- 条件付き依存: `if (engine)` → `lazy.UrlbarUtils.addToFormHistory()`
- 参照: `console.error`, `details.isOneOff`, `details.isSuggestion`, `details.newtabSessionId`, `engine.name`, `this.#actor.browsingContext.top.embedderElement`, `this.isPrivate`, `this.sapName`
- XPCOM: `Services.prefs`

## UrlbarParentController.recordSearchInOpenedTab()
- 位置: L691-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordSearchForBrowser()`, `this.browserWindow.gBrowser.tabContainer.addEventListener()`
- 参照: `tabEvent.target.linkedBrowser`

## UrlbarParentController.recordZeroPrefix()
- 位置: L710-712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarZeroprefix2[kind][this.sapName].add()`
- 参照: `Glean.urlbarZeroprefix2`, `this.sapName`

## UrlbarParentController.checkKeywordURIFixup()
- 位置: L727-738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarUtils.getURIFixupInfo()`, `this.resolveTargetBrowser()`
- 条件付き依存: `if (fixupInfo)` → `this.browserWindow.gKeywordURIFixup.check()`
- 参照: `this.browserWindow.gBrowser.selectedBrowser`, `this.isPrivate`

## UrlbarParentController.cancelQuery()
- 位置: L744-762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbar.autocompleteFirstResultTime.cancel()`, `Glean.urlbar.autocompleteSixthResultTime.cancel()`, `this.manager.cancelQuery()`, `this.notify()`
- 参照: `lazy.UrlbarShared.NOTIFICATIONS.QUERY_CANCELLED`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_FINISHED`, `queryContext.firstTimerId`, `queryContext.sixthTimerId`, `this._lastQueryContextWrapper`, `this._lastQueryContextWrapper.done`

## UrlbarParentController.receiveResults()
- 位置: L769-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.notify()`
- 条件付き依存: `if (queryContext.lastResultCount < 1 && queryContext.results.length >= 1)` → `Glean.urlbar.autocompleteFirstResultTime.stopAndAccumulate()`
- 条件付き依存: `if (queryContext.lastResultCount < 6 && queryContext.results.length >= 6)` → `Glean.urlbar.autocompleteSixthResultTime.stopAndAccumulate()`
- 条件付き依存: `if (queryContext.firstResultChanged)` → `this.notify()`
- 参照: `lazy.UrlbarShared.NOTIFICATIONS.QUERY_FIRST_RESULT`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_RESULTS`, `queryContext.firstResultChanged`, `queryContext.firstTimerId`, `queryContext.lastResultCount`, `queryContext.results.length`, `queryContext.sixthTimerId`

## UrlbarParentController.setChild()
- 位置: L802-804
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#child`

## UrlbarParentController.openSERP()
- 位置: L821-845
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.UrlbarUtils.getSearchQueryUrl()`, `this.browserWindow.openTrustedLinkIn()`, `this.resolveTargetBrowser()`
- 参照: `searchEngine.name`, `this.sapName`

## UrlbarParentController.openSearchForm()
- 位置: L859-868
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchForm()`, `lazy.SearchService.getEngineById()`, `this.browserWindow.openTrustedLinkIn()`, `this.resolveTargetBrowser()`
- 参照: `searchEngine.searchForm`, `this.sapName`

## UrlbarParentController.openPreferences()
- 位置: L880-882
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserWindow.openPreferences()`

## UrlbarParentController.openContainerCreationPanel()
- 位置: L891-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContainerCreationPanel.open()`
- 参照: `this.browserWindow`

## UrlbarParentController.getEngineIconURL()
- 位置: async L903-910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.UrlbarUtils.getEngineIconUrl()`
- 条件付き依存: `if (!engine)` → `lazy.logger.warn()`

## UrlbarParentController.markEngineAsUsed()
- 位置: L918-927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineById()`
- 条件付き依存: `if (!engine)` → `lazy.logger.warn()`
- 条件付き依存: `if (engine instanceof lazy.ConfigSearchEngine && !engine.hasBeenUsed)` → `engine.markAsUsed()`
- 参照: `engine.hasBeenUsed`, `lazy.ConfigSearchEngine`

## UrlbarParentController.speculativeConnect()
- 位置: L942-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarUtils.getUrlFromResult()`, `url.startsWith()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( (lazy.UrlbarPrefs.get("suggest.searches") || context.isSearchbarSAP) && lazy.UrlbarPrefs.get("browser.search.suggest.enabled") )` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if ( (lazy.UrlbarPrefs.get("suggest.searches") || context.isSearchbarSAP) && lazy.UrlbarPrefs.get("browser.search.suggest.enabled") )` → `lazy.UrlbarUtils.setupSpeculativeConnection()`
- 条件付き依存: `if (result.autofill)` → `lazy.UrlbarUtils.getUrlFromResult()`
- 条件付き依存: `if (result.autofill)` → `lazy.UrlbarUtils.setupSpeculativeConnection()`
- 条件付き依存: `if (url.startsWith("http"))` → `lazy.UrlbarUtils.setupSpeculativeConnection()`
- 参照: `context.isPrivate`, `context.isSearchbarSAP`, `context.results.length`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `result.autofill`, `result.heuristic`, `result.payload.engine`, `result.type`, `this.browserWindow`

## UrlbarParentController.loadURL()
- 位置: L1030-1085
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarUtils.loadRequestToUrl()`, `this.browserWindow.openTrustedLinkIn()`, `this.resolveTargetBrowser()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.#prepareAddressbarLoad()`
- 条件付き依存: `if (!params.avoidBrowserFocus)` → `browser.focus()`
- 参照: `Cr.NS_ERROR_LOAD_SHOWED_ERRORPAGE`, `browser.browserId`, `ex.result`, `params.avoidBrowserFocus`, `params.initiatedByURLBar`, `params.initiatingDoc`, `params.postData`, `params.targetBrowser`, `this.#isAddressbar`, `this.browserWindow.document`, `this.browserWindow.gBrowser.selectedBrowser`, `this.rendersInContentProcess`

## UrlbarParentController.focusBrowser()
- 位置: L1098-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resolveTargetBrowser()`
- 条件付き依存: `if (browser && browser == selectedBrowser)` → `selectedBrowser.focus()`
- 参照: `this.browserWindow.gBrowser`

## UrlbarParentController.switchToTab()
- 位置: L1128-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `console.error()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`, `lazy.UrlbarShared.isNonPrivateUserContextId()`, `this.browserWindow.switchToTabHavingURI()`
- 条件付き依存: `if (!activeSplitView && prevTab.isEmpty)` → `gBrowser.removeTab()`
- 条件付き依存: `if (!heuristic)` → `this.addToInputHistory()`
- 参照: `gBrowser.selectedTab`, `prevTab.isEmpty`, `prevTab.splitview`, `this.browserWindow`, `this.isPrivate`
- XPCOM: `Services.io`

## UrlbarParentController.addToInputHistory()
- 位置: L1193-1201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarUtils.addToInputHistory()`, `lazy.UrlbarUtils.addToInputHistoryWhenReady()`, `promise.catch()`
- 参照: `console.error`, `this.isPrivate`

## UrlbarParentController.#prepareAddressbarLoad()
- 位置: L1219-1258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.UrlbarUtils.addToUrlbarHistory()`, `this.browserWindow.gInitialPages.includes()`
- 条件付き依存: `if ( where == "current" && browser.currentURI && url === browser.currentURI.spec )` → `this.browserWindow.SitePermissions.clearTemporaryBlockPermissions()`
- 参照: `browser.authPromptAbuseCounter`, `browser.currentURI`, `browser.currentURI.spec`, `browser.initialPageLoadedFromUserAction`, `browser.userTypedValue`, `params.triggeringPrincipal`, `params.triggeringPrincipal.isSystemPrincipal`, `this.browserWindow`

## UrlbarParentController.removeResult()
- 位置: L1274-1297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.results.findIndex()`, `queryContext.results.splice()`, `this.notify()`
- 条件付き依存: `if (!this._lastQueryContextWrapper)` → `console.error()`
- 条件付き依存: `if (index < 0)` → `console.error()`
- 参照: `lazy.UrlbarShared.NOTIFICATIONS.QUERY_RESULT_REMOVED`, `r.id`, `result.heuristic`, `result.id`, `this._lastQueryContextWrapper`

## UrlbarParentController.setLastQueryContextCache()
- 位置: L1304-1308
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastQueryContextWrapper`

## UrlbarParentController.clearLastQueryContextCache()
- 位置: L1313-1315
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastQueryContextWrapper`

## UrlbarParentController.liveResults()
- 位置: L1323-1325
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastQueryContextWrapper?.queryContext.results`

## UrlbarParentController.notify()
- 位置: L1334-1347
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#child.isProxy === true)` → `this.#child.notifyFromWire()`
- 条件付き依存: `if (this.#child.isProxy === true)` → `params.map()`
- 条件付き依存: `if (this.#child.isProxy === true)` → `param.toWire()`
- 条件付き依存: `if (!(this.#child.isProxy === true))` → `this.#child.notify()`
- 参照: `lazy.UrlbarQueryContext`, `this.#child.isProxy`

## UrlbarParentController.destroy()
- 位置: L1357-1363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#engineObserverRegistered)` → `Services.obs.removeObserver()`
- 参照: `this.#engineObserverRegistered`
- XPCOM: `Services.obs`

## UrlbarParentController.maybeInitEngineStore()
- 位置: L1375-1386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.isESModuleLoaded()`
- 条件付き依存: `if ( Cu.isESModuleLoaded( "moz-src:///toolkit/components/search/SearchService.sys.mjs" ) && lazy.SearchService.isInitialized )` → `this.initEngineStore()`
- 参照: `lazy.SearchService.isInitialized`

## UrlbarParentController.initEngineStore()
- 位置: async L1388-1415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `engines.findIndex()`, `engines.map()`, `this.#child.updateEngineStore()`
- 条件付き依存: `if (!lazy.SearchService.hasSuccessfullyInitialized)` → `lazy.SearchService.init()`
- 条件付き依存: `if (!lazy.SearchService.hasSuccessfullyInitialized)` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (!defaultEngine || defaultIndex == -1)` → `this.#child.updateEngineStore()`
- 参照: `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `lazy.SearchService.visibleEngines`, `this.#engineObserverRegistered`, `this.#engineStoreInitStarted`, `this.isPrivate`
- XPCOM: `Services.obs`

## UrlbarParentController.#topSitesListener()
- 位置: L1417-1419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view.clearTopSitesCache()`

## UrlbarParentController.observe()
- 位置: L1431-1443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onSearchEngineModified()`, `this.view.clearL10nCache()`

## UrlbarParentController.#onSearchEngineModified()
- 位置: L1449-1485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engineToEngineInfo()`, `sortedEngines.findIndex()`, `this.#child.updateEngineStore()`
- 条件付き依存: `if (!engine.hidden)` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (!(!engine.hidden))` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (!this.isPrivate)` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (this.isPrivate)` → `this.#child.updateEngineStore()`
- 参照: `engine.hidden`, `lazy.SearchService.visibleEngines`, `subject.wrappedJSObject`, `this.isPrivate`

## handleBounceEventTrigger()
- 位置: async L1524-1560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTrackedBounces.delete()`, `gTrackedBounces.get()`, `gTrackedBounces.has()`, `lazy.Interactions.getRecentInteractionsForBrowser()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( totalViewTime != 0 && totalViewTime < lazy.UrlbarPrefs.get("events.bounce.maxSecondsFromLastSearch") * 1000 )` → `tracking.record()`
- 参照: `interaction.created_at`, `interaction.totalViewTime`, `tracking.startTime`

## TelemetryEvent.constructor()
- 位置: L1577-1582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.addObserver()`, `this.#readPingPrefs()`
- 参照: `this._controller`, `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.start()
- 位置: L1601-1668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTelemetryUtils.startInteractionType()`, `validEvents.includes()`
- 条件付き依存: `if (this._startEventInfo.interactionType == "topsites")` → `lazy.UrlbarTelemetryUtils.startInteractionType()`
- 条件付き依存: `if (!event)` → `console.error()`
- 条件付き依存: `if (this._controller.sapName === "smartbar")` → `validEvents.push()`
- 条件付き依存: `if (!validEvents.includes(event.type))` → `console.error()`
- 条件付き依存: `if (!this._controller._lastQueryContextWrapper)` → `this._controller.setLastQueryContextCache()`
- 参照: `event.timeStamp`, `event.type`, `this._controller._lastQueryContextWrapper`, `this._controller.sapName`, `this._startEventInfo`, `this._startEventInfo.interactionType`, `this._startEventInfo.searchString`

## TelemetryEvent.record()
- 位置: L1731-1761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#internalRecord()`
- 参照: `details.isSessionOngoing`, `this.#handlingRecord`, `this._startEventInfo`

## TelemetryEvent.#internalRecord()
- 位置: L1772-1818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engagementData.visibleResults.some()`, `lazy.UrlbarTelemetryUtils.buildRecordedDisableCandidate()`, `lazy.UrlbarTelemetryUtils.buildRecordedEngagement()`, `lazy.UrlbarTelemetryUtils.collectSnapshot()`, `this.#resolveExposureList()`, `this.recordFromChild()`
- 参照: `details.isSessionOngoing`, `engagementData.visibleResults`, `r.providerName`, `snapshot.internalDetails`, `snapshot.internalDetails.searchSource`, `snapshot.method`, `this.#engagementData`, `this.#previousSearchWordsSet`, `this.#smartbarData`, `this._controller._lastQueryContextWrapper`, `this._startEventInfo`

## TelemetryEvent.#searchSourceToSap()
- 位置: L1834-1864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.isBlankPageURL()`, `lazy.ExtensionUtils.isExtensionUrl()`
- 参照: `browserWindow.closed`, `browserWindow.gBrowser.currentURI`, `browserWindow.gBrowser.currentURI.spec`, `this._controller.browserWindow`

## TelemetryEvent.#engagementData()
- 位置: L1874-1879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTelemetryUtils.engagementData()`
- 参照: `this._controller.input`, `this._controller.view`

## TelemetryEvent.#smartbarData()
- 位置: L1886-1888
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTelemetryUtils.smartbarData()`
- 参照: `this._controller.input`

## TelemetryEvent.recordFromChild()
- 位置: L1917-1959
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#searchSourceToSap()`, `this._controller.manager.notifyEngagementChange()`
- 条件付き依存: `if (!queryContext)` → `console.error()`
- 条件付き依存: `if (built && sap)` → `this.#fillAndRecord()`
- 条件付き依存: `if (sap && exposures?.length)` → `this.#recordExposureList()`
- 条件付き依存: `if (disableBuilt)` → `this.startTrackingDisableSuggest()`
- 参照: `exposures?.length`, `this._controller`, `this._controller._lastQueryContextWrapper`

## TelemetryEvent.#fillAndRecord()
- 位置: L1971-1986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbar[metric].record()`, `lazy.logger.info()`
- 条件付き依存: `if (metric === "engagement" || metric === "abandonment")` → `this.#getAvailableSemanticSources().join()`
- 条件付き依存: `if (metric === "engagement" || metric === "abandonment")` → `this.#getAvailableSemanticSources()`
- 条件付き依存: `if (metric === "engagement" && eventInfo.search_mode)` → `this.#maybeRecordSearchModeUrlLikeQuery()`
- 参照: `Glean.urlbar`, `eventInfo.available_semantic_sources`, `eventInfo.sap`, `eventInfo.search_engine_default_id`, `eventInfo.search_mode`, `lazy.SearchService.defaultEngine.telemetryId`

## TelemetryEvent.#maybeRecordSearchModeUrlLikeQuery()
- 位置: L1996-2010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarSearchmode.urlLikeQuery.addToDenominator()`
- 条件付き依存: `if (fixupInfo?.href && !fixupInfo.isSearch)` → `Glean.urlbarSearchmode.urlLikeQuery.addToNumerator()`
- 参照: `fixupInfo.isSearch`, `fixupInfo?.href`, `heuristicResult.type`, `heuristicResult?.heuristic`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext?.heuristicResult`, `this._controller._lastQueryContextWrapper`

## TelemetryEvent.#recordSearchEngagementTelemetry()
- 位置: L2070-2146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTelemetryUtils.buildEventInfo()`, `lazy.UrlbarTelemetryUtils.getInteractionType()`, `this.#searchSourceToSap()`
- 条件付き依存: `if (built)` → `this.#fillAndRecord()`
- 参照: `engagementData.searchMode`, `engagementData.viewIsOpen`, `this.#engagementData`, `this.#previousSearchWordsSet`, `this._controller.sapName`

## TelemetryEvent.#getOptionalSmartbarTelemetry()
- 位置: L2156-2162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#searchSourceToSap()`
- 参照: `this.#smartbarData`

## TelemetryEvent.#getAvailableSemanticSources()
- 位置: L2172-2192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.error()`
- 条件付き依存: `if ( isSmartbar ? semanticManager.isEnabledForSmartWindow : semanticManager.canUseSemanticSearch )` → `sources.push()`
- 条件付き依存: `if (!sources.length)` → `sources.push()`
- 参照: `lazy.UrlbarProviderSemanticHistorySearch.semanticManager`, `semanticManager.canUseSemanticSearch`, `semanticManager.isEnabledForSmartWindow`, `sources.length`, `this._controller.sapName`

## TelemetryEvent.#resolveExposureList()
- 位置: L2207-2224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `exposures.map()`, `weakResult.get()`
- 条件付き依存: `if (result)` → `this.#exposureResults.delete()`
- 条件付き依存: `if (result)` → `lazy.UrlbarTelemetryUtils.exposureTerminal()`
- 参照: `this.#exposures`, `this.#tentativeExposures`

## TelemetryEvent.#recordExposureList()
- 位置: L2238-2273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbar.exposure.record()`, `[...terminalByType].sort()`, `a[0].localeCompare()`, `lazy.logger.debug()`, `terminalByType.set()`, `tuples.map()`, `tuples.map(t => t[0]).join()`, `tuples.map(t => t[1]).join()`
- 条件付き依存: `if (keyword)` → `terminal.toString()`
- 条件付き依存: `if (keyword)` → `lazy.logger.debug()`
- 条件付き依存: `if (keyword)` → `Glean.urlbar.keywordExposure.record()`
- 条件付き依存: `if (keywordExposureRecorded)` → `GleanPings.urlbarKeywordExposure.submit()`

## TelemetryEvent.addExposure()
- 位置: L2288-2292
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#addExposureInternal()`
- 参照: `result.exposureTelemetry`

## TelemetryEvent.addTentativeExposure()
- 位置: L2304-2311
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#tentativeExposures.push()`
- 条件付き依存: `if (result.exposureTelemetry)` → `Cu.getWeakReference()`
- 参照: `result.exposureTelemetry`

## TelemetryEvent.acceptTentativeExposures()
- 位置: L2318-2329
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#tentativeExposures.length)` → `weakResult.get()`
- 条件付き依存: `if (this.#tentativeExposures.length)` → `weakQueryContext.get()`
- 条件付き依存: `if (result && queryContext)` → `this.#addExposureInternal()`
- 参照: `this.#tentativeExposures`, `this.#tentativeExposures.length`

## TelemetryEvent.discardTentativeExposures()
- 位置: L2335-2339
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#tentativeExposures`, `this.#tentativeExposures.length`

## TelemetryEvent.#addExposureInternal()
- 位置: L2341-2357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#exposureResults.has()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposureResults.add()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `lazy.UrlbarTelemetryUtils.exposureEntry()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposures.push()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `Cu.getWeakReference()`

## TelemetryEvent.discard()
- 位置: L2364-2368
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._startEventInfo`

## TelemetryEvent.reset()
- 位置: L2373-2376
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#previousSearchWordsSet`, `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.#readPingPrefs()
- 位置: L2394-2398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this.#recordPref()`
- 参照: `this.#PING_PREFS`

## TelemetryEvent.#recordPref()
- 位置: L2400-2415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (metric)` → `metric.set()`
- 条件付き依存: `if (metric)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get(pref))` → `this.handleDisableSuggest()`
- 参照: `this.#PING_PREFS`

## TelemetryEvent.onPrefChanged()
- 位置: L2417-2419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordPref()`

## TelemetryEvent.onNimbusChanged()
- 位置: L2421-2423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordPref()`

## TelemetryEvent.startTrackingDisableSuggest()
- 位置: L2479-2487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getCurrentTime()`
- 参照: `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.handleDisableSuggest()
- 位置: L2489-2505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#searchSourceToSap()`, `this.getCurrentTime()`
- 条件付き依存: `if (sap)` → `this.#fillAndRecord()`
- 参照: `state.built`, `state.interactionTime`, `state.searchSource`, `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.getCurrentTime()
- 位置: L2507-2509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`

## TelemetryEvent.startTrackingBounceEvent()
- 位置: async L2525-2536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTelemetryUtils.collectBounceSnapshot()`, `this.#recordBounce()`, `this.#searchSourceToSap()`, `this.#startTrackingBounce()`
- 参照: `snapshot.searchSource`, `this.#engagementData.visibleResults`, `this._startEventInfo`

## TelemetryEvent.startTrackingBuiltBounce()
- 位置: async L2548-2559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(viewTime / 1000).toString()`, `this.#fillAndRecord()`, `this.#searchSourceToSap()`, `this.#startTrackingBounce()`
- 参照: `built.eventInfo.view_time`

## TelemetryEvent.#startTrackingBounce()
- 位置: async L2573-2582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `gTrackedBounces.has()`, `gTrackedBounces.set()`, `this._controller.resolveTargetBrowser()`
- 条件付き依存: `if (gTrackedBounces.has(browser))` → `handleBounceEventTrigger()`

## TelemetryEvent.#recordBounce()
- 位置: L2596-2618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getOptionalSmartbarTelemetry()`, `this.#recordSearchEngagementTelemetry()`
- 参照: `snapshot.action`, `snapshot.location`, `snapshot.numChars`, `snapshot.numWords`, `snapshot.provider`, `snapshot.searchMode`, `snapshot.searchSource`, `snapshot.searchWords`, `snapshot.selIndex`, `snapshot.selType`, `snapshot.startEventInfo`, `snapshot.visibleResults`, `snapshot.windowMode`
