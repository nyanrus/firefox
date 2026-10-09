# browser/actors/ContentSearchParent.sys.mjs

source: browser/actors/ContentSearchParent.sys.mjs
source-hash: 60758375a7e938f75745a1270c228a6040e8bf22
lines: 759

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: L112-120
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.initialized)` → `lazy.UrlbarPrefs.addObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## searchSuggestionUIStrings()
- 位置: L122-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings.createBundle()`, `searchBundle.GetStringFromName()`
- 参照: `this._searchSuggestionUIStrings`
- XPCOM: `Services.strings`

## destroy()
- 位置: L144-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (!this.initialized)` → `Promise.resolve()`
- 参照: `this._currentEventPromise`, `this._destroyedPromise`, `this._eventQueue.length`, `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L161-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subj.wrappedJSObject.client.addBlocker()`, `this._eventQueue.push()`, `this._processEventQueue()`, `this.destroy()`

## onPrefChanged()
- 位置: L186-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.shouldHandOffToSearchModePrefs.includes()`
- 条件付き依存: `if (lazy.UrlbarPrefs.shouldHandOffToSearchModePrefs.includes(pref))` → `this._eventQueue.push()`
- 条件付き依存: `if (lazy.UrlbarPrefs.shouldHandOffToSearchModePrefs.includes(pref))` → `this._processEventQueue()`

## removeFormHistoryEntry()
- 位置: L196-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._suggestionDataForBrowser()`
- 条件付き依存: `if (browserData?.previousFormHistoryResults)` → `browserData.previousFormHistoryResults.find()`
- 条件付き依存: `if (browserData?.previousFormHistoryResults)` → `lazy.FormHistory.update()`
- 条件付き依存: `if (browserData?.previousFormHistoryResults)` → `console.error()`
- 参照: `browserData?.previousFormHistoryResults`, `e.text`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `result.guid`

## performSearch()
- 位置: L213-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.getSubmission()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.SearchService.getEngineByName()`, `this._ensureDataHasProperties()`
- 条件付き依存: `if (where === "current")` → `this._reply()`
- 条件付き依存: `if (where === "current")` → `browser.loadURI()`
- 条件付き依存: `if (where === "current")` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (where === "current")` → `win.gBrowser.selectedBrowser.getAttribute()`
- 条件付き依存: `if (!(where === "current"))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(where === "current"))` → `win.openTrustedLinkIn()`
- 参照: `browser.documentGlobal`, `data.engineName`, `data.healthReportKey`, `data.originalEvent`, `data.searchString`, `data.selection`, `submission.postData`, `submission.uri`, `submission.uri.spec`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## getSuggestions()
- 位置: async L267-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.fetch()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SearchService.getEngineByName()`, `lazy.SearchSuggestionController.engineOffersSuggestions()`, `nonTailEntries.map()`, `suggestions.local.map()`, `suggestions.remote.filter()`, `this._suggestionDataForBrowser()`
- 参照: `browserData.previousFormHistoryResults`, `e.matchPrefix`, `e.tail`, `e.value`, `suggestions.formHistoryResults`, `suggestions.local`, `suggestions.remote`, `suggestions.term`, `this._currentSuggestion`

## addFormHistoryEntry()
- 位置: async L320-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.FormHistory.update()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `entry.engineName`, `entry.value`, `entry.value.length`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VALUE_LENGTH`

## currentStateObj()
- 位置: async L352-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getVisibleEngines()`, `state.engines.push()`, `this._currentEngineObj()`, `this._getEngineIconURL()`
- 参照: `engine.hideOneOffButton`, `engine.name`, `lazy.ConfigSearchEngine`

## _processEventQueue()
- 位置: L371-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._eventQueue.shift()`, `this._processEventQueue()`, `this["_on" + event.type]()`
- 参照: `event.type`, `this._currentEventPromise`, `this._eventQueue.length`

## _cancelSuggestions()
- 位置: L391-413
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this._currentSuggestion && this._currentSuggestion.browser === browser )` → `this._currentSuggestion.controller.stop()`
- 条件付き依存: `if (actor === m.actor && m.name === "GetSuggestions")` → `this._eventQueue.splice()`
- 条件付き依存: `if (cancelled)` → `this._reply()`
- 参照: `m.actor`, `m.name`, `this._currentSuggestion`, `this._currentSuggestion.browser`, `this._eventQueue`, `this._eventQueue.length`

## _onMessage()
- 位置: async L415-422
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this._initService()`
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 条件付き依存: `if (methodName in this)` → `eventItem.browser.removeEventListener()`
- 参照: `eventItem.name`

## _onMessageGetState()
- 位置: async L424-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._reply()`, `this.currentStateObj()`

## _onMessageGetEngine()
- 位置: async L429-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._reply()`, `this.currentStateObj()`
- 参照: `actor.browsingContext`, `state.currentEngine`, `state.currentPrivateEngine`

## _onMessageGetHandoffSearchModePrefs()
- 位置: L440-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._reply()`

## _onMessageGetStrings()
- 位置: L448-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._reply()`
- 参照: `this.searchSuggestionUIStrings`

## _onMessageSearch()
- 位置: L452-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.performSearch()`

## _onMessageSetCurrentEngine()
- 位置: L456-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `lazy.SearchService.setDefault()`
- 参照: `lazy.SearchService.CHANGE_REASON.USER_SEARCHBAR`

## _onMessageManageEngines()
- 位置: L463-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.documentGlobal.openPreferences()`

## _onMessageGetSuggestions()
- 位置: async L467-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureDataHasProperties()`, `this._reply()`, `this.getSuggestions()`
- 参照: `data.engineName`, `suggestions.local`, `suggestions.remote`, `suggestions.term`

## _onMessageAddFormHistoryEntry()
- 位置: async L484-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addFormHistoryEntry()`

## _onMessageRemoveFormHistoryEntry()
- 位置: L488-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeFormHistoryEntry()`

## _onMessageSpeculativeConnect()
- 位置: L492-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (browser.contentWindow)` → `engine.speculativeConnect()`
- 参照: `browser.contentPrincipal.originAttributes`, `browser.contentWindow`

## _onMessageSearchHandoff()
- 位置: L505-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.getVisitId()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `urlBar.inputField.addEventListener()`
- 条件付き依存: `if (!text)` → `urlBar.setHiddenFocus()`
- 条件付き依存: `if (!(!text))` → `urlBar.handoff()`
- 参照: `browser.documentGlobal`, `data.text`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `win.gURLBar`

## checkFirstChange()
- 位置: L528-540
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeHiddenFocus()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.handoff()`
- 条件付き依存: `if (isFirstChange)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeEventListener()`

## onKeydown()
- 位置: L542-551
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (ev.key.length === 1 && !ev.altKey && !ev.ctrlKey && !ev.metaKey)` → `checkFirstChange()`
- 条件付き依存: `if (ev.key === "Escape")` → `onDone()`
- 参照: `ev.altKey`, `ev.ctrlKey`, `ev.key`, `ev.key.length`, `ev.metaKey`

## onDone()
- 位置: L553-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `urlBar.inputField.removeEventListener()`, `urlBar.removeHiddenFocus()`
- 参照: `ev?.type`

## _onObserve()
- 位置: async L577-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._broadcast()`, `this._currentEngineObj()`, `this.currentStateObj()`
- 参照: `eventItem.data`

## _suggestionDataForBrowser()
- 位置: L602-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._suggestionMap.get()`
- 条件付き依存: `if (!data && create)` → `this._suggestionMap.set()`
- 参照: `lazy.SearchSuggestionController`

## _reply()
- 位置: L616-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`

## _broadcast()
- 位置: L620-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`

## _currentEngineObj()
- 位置: async L626-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getDefault()`, `lazy.SearchService.getDefaultPrivate()`, `this._getEngineIconURL()`
- 参照: `engine.name`, `lazy.ConfigSearchEngine`

## _getEngineIconURL()
- 位置: async L656-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `engine.getIconURL()`, `fetch()`, `response.arrayBuffer()`, `response.headers.get()`, `url.startsWith()`

## _ensureDataHasProperties()
- 位置: L692-698
- 役割: (未記入)
- 触るとき: (未記入)

## _initService()
- 位置: L700-705
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initServicePromise)` → `lazy.SearchService.init()`
- 参照: `this._initServicePromise`

## ContentSearchParent.constructor()
- 位置: L709-713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentSearch.init()`, `gContentSearchActors.add()`, `super()`

## ContentSearchParent.didDestroy()
- 位置: L715-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gContentSearchActors.delete()`

## ContentSearchParent.receiveMessage()
- 位置: L719-757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentSearch._eventQueue.push()`, `ContentSearch._processEventQueue()`, `browser.addEventListener()`
- 条件付き依存: `if (msg.name === "Search")` → `ContentSearch._cancelSuggestions()`
- 参照: `msg.data`, `msg.name`, `this.browsingContext.top.embedderElement`

## handleEvent()
- 位置: L736-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentSearch._suggestionMap.get()`, `browser.removeEventListener()`, `eventItem.browser.addEventListener()`
- 条件付き依存: `if (browserData)` → `ContentSearch._suggestionMap.delete()`
- 条件付き依存: `if (browserData)` → `ContentSearch._suggestionMap.set()`
- 参照: `event.detail`, `eventItem.browser`
