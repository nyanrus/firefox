# browser/components/places/Interactions.sys.mjs

source: browser/components/places/Interactions.sys.mjs
source-hash: cf647ed30ec2c40aa10f3e372e4d603d3f251896
lines: 845

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.now()`, `Promise.resolve()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.createInstance()`

## monotonicNow()
- 位置: L71-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## _Interactions.init()
- 位置: L185-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.registerWindowActor()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.wm.getMostRecentBrowserWindow()`, `lazy.idleService.addIdleObserver()`
- 条件付き依存: `if (!win.closed)` → `this.#registerWindow()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `lazy.pageViewIdleTime`, `this.#activeWindow`, `this.#initialized`, `win.closed`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.wm`

## _Interactions.uninit()
- 位置: L223-227
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#initialized)` → `lazy.idleService.removeIdleObserver()`
- 参照: `lazy.pageViewIdleTime`, `this.#initialized`

## _Interactions.reset()
- 位置: async L233-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.consumeInteractionData()`, `ChromeUtils.now()`, `lazy.logConsole.debug()`, `this.store.reset()`
- 参照: `_Interactions.interactionUpdatePromise`, `this.#interactions`, `this.#userIsIdle`, `this._pageViewStartTime`

## _Interactions.store()
- 位置: L250-255
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#store`

## _Interactions.registerNewInteraction()
- 位置: L265-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.InteractionsBlocklist.isUrlBlocklisted()`, `lazy.logConsole.debug()`, `monotonicNow()`, `this.#interactions.get()`, `this.#interactions.set()`, `this.#pruneOldRecentInteractions()`, `this.#recentInteractions.get()`, `this.#recentInteractions.set()`
- 条件付き依存: `if (interaction && interaction.url != docInfo.url)` → `this.registerEndOfInteraction()`
- 条件付き依存: `if (lazy.InteractionsBlocklist.isUrlBlocklisted(docInfo.url))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (docInfo.isActive && browser.documentGlobal == this.#activeWindow)` → `ChromeUtils.now()`
- 参照: `browser.browsingContext.useGlobalHistory`, `browser.documentGlobal`, `docInfo.isActive`, `docInfo.referrer`, `docInfo.url`, `interaction.url`, `lazy.isHistoryEnabled`, `this.#activeWindow`, `this._pageViewStartTime`

## _Interactions.registerEndOfInteraction()
- 位置: L323-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#interactions.delete()`, `this.#updateInteraction()`
- 参照: `browser.browsingContext.useGlobalHistory`, `lazy.isHistoryEnabled`

## _Interactions.#updateInteraction()
- 位置: L350-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_Interactions.#updateInteraction_async()`
- 参照: `this.#activeWindow`, `this.#interactions`, `this.#userIsIdle`, `this._pageViewStartTime`, `this.store`

## _Interactions.getRecentInteractionsForBrowser()
- 位置: async L367-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recentInteractions.get()`, `this.#updateInteraction()`
- 参照: `_Interactions.interactionUpdatePromise`

## _Interactions.#pruneOldRecentInteractions()
- 位置: L382-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `interactions.filter()`, `this.#recentInteractions.get()`
- 条件付き依存: `if (interactionstoTrack.length)` → `this.#recentInteractions.set()`
- 条件付き依存: `if (!(interactionstoTrack.length))` → `this.#recentInteractions.delete()`
- 参照: `interaction.updated_at`, `interactionstoTrack.length`

## _Interactions.interactionUpdatePromise()
- 位置: L414-416
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `_Interactions.interactionUpdatePromise`

## _Interactions.#updateInteraction_async()
- 位置: async L434-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.collectScrollingData()`, `ChromeUtils.consumeInteractionData()`, `ChromeUtils.now()`, `_Interactions.interactionUpdatePromise .then()`, `_Interactions.interactionUpdatePromise .then(async () => ChromeUtils.collectScrollingData()) .then()`, `console.error()`, `interactions.get()`, `lazy.logConsole.debug()`, `monotonicNow()`, `store.add()`
- 条件付き依存: `if (!activeWindow || (browser && browser.documentGlobal != activeWindow))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (userIsIdle)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!interaction)` → `lazy.logConsole.debug()`
- 参照: `Interactions._pageViewStartTime`, `_Interactions.interactionUpdatePromise`, `activeWindow.gBrowser.selectedTab.linkedBrowser`, `browser.documentGlobal`, `interaction.keypresses`, `interaction.scrollingDistance`, `interaction.scrollingTime`, `interaction.totalViewTime`, `interaction.typingTime`, `interaction.updated_at`, `interactionData.Typing`, `result.interactionTimeInMilliseconds`, `result.scrollingDistanceInPixels`, `typing.interactionCount`, `typing.interactionTimeInMilliseconds`

## _Interactions.#onActivateWindow()
- 位置: L505-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.logConsole.debug()`
- 参照: `this.#activeWindow`, `this._pageViewStartTime`

## _Interactions.#onDeactivateWindow()
- 位置: L519-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#updateInteraction()`
- 参照: `this.#activeWindow`

## _Interactions.#onTabSelect()
- 位置: L538-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `lazy.logConsole.debug()`, `this.#interactions.has()`, `this.#updateInteraction()`
- 条件付き依存: `if (browser && this.#interactions.has(browser))` → `this.#interactions.get()`
- 条件付き依存: `if (browser && this.#interactions.has(browser))` → `Date.now()`
- 条件付き依存: `if (timePassedSinceUpdateSeconds >= lazy.breakupIfNoUpdatesForSeconds)` → `this.registerEndOfInteraction()`
- 条件付き依存: `if (timePassedSinceUpdateSeconds >= lazy.breakupIfNoUpdatesForSeconds)` → `this.registerNewInteraction()`
- 参照: `browser.currentURI.spec`, `interaction.updated_at`, `lazy.breakupIfNoUpdatesForSeconds`, `this.#activeWindow?.gBrowser.selectedBrowser`, `this._pageViewStartTime`

## _Interactions.handleEvent()
- 位置: L567-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onActivateWindow()`, `this.#onDeactivateWindow()`, `this.#onTabSelect()`, `this.#unregisterWindow()`
- 参照: `event.detail.previousTab.linkedBrowser`, `event.target`, `event.type`

## _Interactions.observe()
- 位置: L592-610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `lazy.logConsole.debug()`, `this.#onWindowOpen()`, `this.#updateInteraction()`
- 参照: `this.#userIsIdle`, `this._pageViewStartTime`

## _Interactions.#registerWindow()
- 位置: L618-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.addEventListener()`

## _Interactions.#unregisterWindow()
- 位置: L634-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.removeEventListener()`

## _Interactions.#onWindowOpen()
- 位置: L647-661
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registerWindow()`, `win.addEventListener()`, `win.document.documentElement.getAttribute()`

## InteractionsStore.constructor()
- 位置: L698-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `lazy.PlacesUtils.history.shutdownClient.jsclient.addBlocker()`, `this.flush()`
- 参照: `this.pendingPromise`, `this.progress`

## fetchState()
- 位置: L704-704
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.progress`

## InteractionsStore.flush()
- 位置: async L716-722
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#timer)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this.#timer)` → `this.#timerResolve()`
- 条件付き依存: `if (this.#timer)` → `this.#updateDatabase()`
- 参照: `this.#timer`

## InteractionsStore.reset()
- 位置: async L728-741
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`
- 条件付き依存: `if (this.#timer)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this.#timer)` → `this.#timerResolve()`
- 条件付き依存: `if (this.#timer)` → `this.#interactions.clear()`
- 参照: `this.#timer`

## InteractionsStore.add()
- 位置: L751-770
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `interactionsForUrl.set()`, `lazy.logConsole.debug()`, `this.#interactions.get()`
- 条件付き依存: `if (!interactionsForUrl)` → `this.#interactions.set()`
- 条件付き依存: `if (!this.#timer)` → `lazy.setTimeout()`
- 条件付き依存: `if (!this.#timer)` → `this.#updateDatabase().catch(console.error).then()`
- 条件付き依存: `if (!this.#timer)` → `this.#updateDatabase().catch()`
- 条件付き依存: `if (!this.#timer)` → `this.#updateDatabase()`
- 条件付き依存: `if (!this.#timer)` → `this.pendingPromise.then()`
- 参照: `console.error`, `interaction.created_at`, `interaction.url`, `lazy.saveInterval`, `this.#timer`, `this.#timerResolve`, `this.pendingPromise`

## InteractionsStore.#updateDatabase()
- 位置: async L772-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `SQLInsertFragments.join()`, `SQLInsertFragments.push()`, `Services.obs.notifyObservers()`, `db.executeCached()`, `interactions.values()`, `interactionsForUrl.values()`, `lazy.PlacesUtils.withConnectionWrapper()`, `lazy.logConsole.debug()`
- 参照: `Interactions.DOCUMENT_TYPE.GENERIC`, `interaction.created_at`, `interaction.documentType`, `interaction.keypresses`, `interaction.referrer`, `interaction.scrollingDistance`, `interaction.scrollingTime`, `interaction.totalViewTime`, `interaction.typingTime`, `interaction.updated_at`, `interaction.url`, `interactions.size`, `this.#interactions`, `this.#timer`, `this.progress.pendingUpdates`
- XPCOM: `Services.obs`
