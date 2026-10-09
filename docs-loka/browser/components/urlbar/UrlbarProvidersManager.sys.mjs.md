# browser/components/urlbar/UrlbarProvidersManager.sys.mjs

source: browser/components/urlbar/UrlbarProvidersManager.sys.mjs
source-hash: bc6837e21126c8ab79847749ead384c782871d5e
lines: 1167

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## ProvidersManager.constructor()
- 位置: L263-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.entries()`, `info.supportedSAPs.includes()`, `localProviderModules.filter()`, `this.registerMuxer()`, `this.registerProvider()`
- 参照: `providerInfo.module`, `providerInfo.name`, `this.muxers`, `this.providers`, `this.providersByNotificationType`, `this.queries`

## ProvidersManager.getInstanceForSap()
- 位置: L326-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gProvidersManagerPerSap.get()`
- 条件付き依存: `if (!manager)` → `gProvidersManagerPerSap.set()`

## ProvidersManager.registerProvider()
- 位置: L341-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.values()`, `Object.values(lazy.UrlbarShared.PROVIDER_TYPE).includes()`, `lazy.logger.info()`, `this.providers.splice()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `this.providers.findIndex()`
- 条件付き依存: `if (typeof provider[notificationType] === "function")` → `this.providersByNotificationType[notificationType].add()`
- 参照: `lazy.UrlbarProvider`, `lazy.UrlbarShared.PROVIDER_TYPE`, `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`, `p.type`, `provider.name`, `provider.type`, `this.providers.length`, `this.providersByNotificationType`

## ProvidersManager.unregisterProvider()
- 位置: L379-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(this.providersByNotificationType).forEach()`, `lazy.logger.info()`, `providers.delete()`, `this.providers.findIndex()`
- 条件付き依存: `if (index != -1)` → `this.providers.splice()`
- 参照: `p.name`, `provider.name`, `this.providersByNotificationType`

## ProvidersManager.getProvider()
- 位置: L399-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.providers.find()`
- 参照: `p.name`

## ProvidersManager.registerMuxer()
- 位置: L409-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.info()`, `this.muxers.set()`
- 参照: `lazy.UrlbarMuxer`, `muxer.name`

## ProvidersManager.unregisterMuxer()
- 位置: L423-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.info()`, `this.muxers.delete()`
- 参照: `muxer.name`

## ProvidersManager.startQuery()
- 位置: async L437-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.keywords.ensureCacheInitialized()`, `lazy.Region.init()`, `lazy.UrlbarSearchUtils.init()`, `lazy.UrlbarTokenizer.tokenize()`, `lazy.logger.debug()`, `lazy.logger.error()`, `lazy.logger.info()`, `query.start()`, `queryContext.providers.includes()`, `this.muxers.get()`, `this.providers.filter()`, `this.queries.set()`, `updateSourcesIfEmpty()`
- 条件付き依存: `if (restrictToken)` → `lazy.UrlbarShared.SEARCH_MODE_RESTRICT.has()`
- 参照: `p.name`, `query.canceled`, `queryContext.canceled`, `queryContext.muxer`, `queryContext.providers`, `queryContext.restrictSource`, `queryContext.restrictToken`, `queryContext.searchString`, `queryContext.sources`, `queryContext.sources.length`, `queryContext.tokens`, `restrictToken.value`, `this.providers`

## ProvidersManager.cancelQuery()
- 位置: L531-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.info()`, `query.cancel()`, `this.queries.delete()`, `this.queries.get()`
- 条件付き依存: `if (!ProvidersManager.interruptLevel)` → `lazy.PlacesUtils.promiseLargeCacheDBConnection()`
- 条件付き依存: `if (!ProvidersManager.interruptLevel)` → `db.interrupt()`
- 参照: `ProvidersManager.interruptLevel`, `queryContext.canceled`, `queryContext.searchString`

## ProvidersManager.runInCriticalSection()
- 位置: async L558-565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `taskFn()`
- 参照: `this.interruptLevel`

## ProvidersManager.notifyEngagementChange()
- 位置: L584-649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["engagement", "abandonment"].includes()`, `results.push()`, `visibleResults.forEach()`, `visibleResultsByProviderName.get()`
- 条件付き依存: `if (!["engagement", "abandonment"].includes(state))` → `lazy.logger.error()`
- 条件付き依存: `if (!results)` → `visibleResultsByProviderName.set()`
- 条件付き依存: `if (!details.isSessionOngoing)` → `this.#notifyImpression()`
- 条件付き依存: `if (details.result)` → `this.#notifyEngagement()`
- 条件付き依存: `if (!(state === "engagement"))` → `this.#notifyAbandonment()`
- 条件付き依存: `if (!details.isSessionOngoing)` → `this.#notifySearchSessionEnd()`
- 参照: `controller.view`, `controller.view.visibleResults`, `details.isSessionOngoing`, `details.result`, `result.providerName`, `this.providersByNotificationType.onAbandonment`, `this.providersByNotificationType.onEngagement`, `this.providersByNotificationType.onImpression`, `this.providersByNotificationType.onSearchSessionEnd`

## ProvidersManager.#notifyEngagement()
- 位置: L651-659
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.result.providerName == provider.name)` → `provider.tryMethod()`
- 条件付き依存: `if (details.result.providerName == provider.name)` → `controller.notify()`
- 参照: `details.result.providerName`, `lazy.UrlbarShared.NOTIFICATIONS.PROVIDER_ENGAGEMENT`, `provider.name`

## ProvidersManager.#notifyImpression()
- 位置: L661-684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `visibleResultsByProviderName.get()`
- 条件付き依存: `if (providerVisibleResults.length)` → `provider.tryMethod()`
- 参照: `provider.name`, `providerVisibleResults.length`

## ProvidersManager.#notifyAbandonment()
- 位置: L686-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `visibleResultsByProviderName.has()`
- 条件付き依存: `if (visibleResultsByProviderName.has(provider.name))` → `provider.tryMethod()`
- 参照: `provider.name`

## ProvidersManager.#notifySearchSessionEnd()
- 位置: L699-713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `provider.tryMethod()`

## Query.constructor()
- 位置: L735-752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.sources.slice()`, `this.context.deferUserSelectionProviders.clear()`, `this.context.pendingHeuristicProviders.clear()`
- 参照: `this.acceptableSources`, `this.canceled`, `this.context`, `this.context.results`, `this.controller`, `this.muxer`, `this.providers`, `this.started`, `this.unsortedResults`

## Query.start()
- 位置: async L757-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.race()`, `activePromises.push()`, `activeProviders.map()`, `lazy.logger.error()`, `lazy.logger.info()`, `provider .isActive()`, `provider .isActive(this.context, this.controller) .then()`, `queryPromises.push()`, `startQuery()`, `this._sleepTimer.promise.then()`
- 条件付き依存: `if (isActive && !this.canceled)` → `provider.tryMethod()`
- 条件付き依存: `if (priority >= maxPriority)` → `activeProviders.push()`
- 条件付き依存: `if (provider.deferUserSelection)` → `this.context.deferUserSelectionProviders.add()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `this.context.pendingHeuristicProviders.add()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `queryPromises.push()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `startQuery(provider).finally()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `startQuery()`
- 条件付き依存: `if (provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC)` → `this.context.pendingHeuristicProviders.delete()`
- 条件付き依存: `if (!this._sleepTimer)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!this.canceled)` → `this._chunkTimer?.fire()`
- 参照: `activeProviders.length`, `lazy.SkippableTimer`, `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`, `p.name`, `provider.deferUserSelection`, `provider.logger`, `provider.name`, `provider.queryInstance`, `provider.type`, `queryPromises.length`, `this._cancelQueries`, `this._sleepTimer`, `this.canceled`, `this.context`, `this.controller`, `this.providers`, `this.started`

## startQuery()
- 位置: async L817-835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `provider.logger.debug()`, `provider.tryMethod()`, `this.add()`
- 条件付き依存: `if (!addedResult)` → `this.context.deferUserSelectionProviders.delete()`
- 参照: `provider.name`, `this.context`, `this.context.searchString`, `this.controller`

## Query.cancel()
- 位置: L892-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.error()`, `provider.logger.debug()`, `provider.tryMethod()`, `this._cancelQueries()`, `this._chunkTimer?.cancel()`, `this._chunkTimer?.cancel().catch()`, `this._sleepTimer?.fire()`, `this._sleepTimer?.fire().catch()`, `this.context.deferUserSelectionProviders.clear()`
- 参照: `provider.queryInstance`, `this.canceled`, `this.context`, `this.context.searchString`, `this.providers`

## Query.add()
- 位置: L917-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `provider.tryMethod()`, `result.payload.url.startsWith()`, `this._notifyResultsFromProvider()`, `this.acceptableSources.includes()`, `this.context.pendingHeuristicProviders.delete()`, `this.context.searchString.startsWith()`, `this.unsortedResults.push()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.DYNAMIC)` → `provider.getViewTemplate()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.DYNAMIC)` → `provider.getViewUpdate()`
- 条件付き依存: `if (result.payload.url)` → `lazy.UrlbarSearchUtils.resultIsSERP()`
- 参照: `lazy.UrlbarProvider`, `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `lazy.UrlbarShared.RESULT_TYPE.KEYWORD`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `provider.name`, `provider.type`, `result.autofill`, `result.commands`, `result.heuristic`, `result.id`, `result.isSERP`, `result.payload.url`, `result.payload.viewTemplate`, `result.payload.viewUpdate`, `result.providerName`, `result.providerType`, `result.source`, `result.type`, `this.canceled`, `this.context.isPrivate`, `this.context.searchMode`, `this.context.searchMode.engineName`, `this.context.trimmedSearchString`, `this.controller`

## Query._notifyResultsFromProvider()
- 位置: L1012-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this.context.pendingHeuristicProviders.size && provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC )` → `this._chunkTimer.fire().catch()`
- 条件付き依存: `if ( !this.context.pendingHeuristicProviders.size && provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC )` → `this._chunkTimer.fire()`
- 条件付き依存: `if ( !this.context.pendingHeuristicProviders.size && provider.type == lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC )` → `lazy.logger.error()`
- 参照: `ProvidersManager.chunkResultsDelayMs`, `lazy.SkippableTimer`, `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`, `provider.logger`, `provider.type`, `this._chunkTimer`, `this._chunkTimer.done`, `this.context.pendingHeuristicProviders.size`

## callback()
- 位置: L1020-1020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._notifyResults()`

## Query._notifyResults()
- 位置: L1036-1055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `this.muxer.sort()`
- 条件付き依存: `if (this.controller)` → `this.controller.receiveResults()`
- 参照: `this.context`, `this.context.firstResult`, `this.context.firstResultChanged`, `this.context.results`, `this.context.results.length`, `this.controller`, `this.unsortedResults`

## Query.getProvider()
- 位置: L1065-1067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.providers.find()`
- 参照: `p.name`

## updateSourcesIfEmpty()
- 位置: L1077-1166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `context.tokens.find()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_BOOKMARK || restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG || (!restrictTokenTy...)` → `acceptedSources.push()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY || (!restrictTokenType && lazy.UrlbarPrefs.get("suggest.history")) )` → `acceptedSources.push()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH || !restrictTokenType )` → `acceptedSources.push()`
- 条件付き依存: `if ( restrictTokenType === lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_OPENPAGE || (!restrictTokenType && lazy.UrlbarPrefs.get("suggest.openpage")) )` → `acceptedSources.push()`
- 条件付き依存: `if (!context.isPrivate && !restrictTokenType)` → `acceptedSources.push()`
- 条件付き依存: `if (!restrictTokenType)` → `acceptedSources.push()`
- 参照: `context.isPrivate`, `context.sapName`, `context.sources`, `context.sources.length`, `lazy.UrlbarShared.RESULT_SOURCE`, `lazy.UrlbarShared.RESULT_SOURCE.ADDON`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_NETWORK`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_ACTION`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_BOOKMARK`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_OPENPAGE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_URL`, `restrictToken.type`, `t.type`
