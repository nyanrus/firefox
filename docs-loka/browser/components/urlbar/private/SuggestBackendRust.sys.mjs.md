# browser/components/urlbar/private/SuggestBackendRust.sys.mjs

source: browser/components/urlbar/private/SuggestBackendRust.sys.mjs
source-hash: 04b2d57b4cf5dd65d96b78d82909a6ea86a5529c
lines: 983

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## SuggestBackendRust.constructor()
- 位置: L93-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 条件付き依存: `if (!lazy.Utils.shouldSkipRemoteActivity)` → `lazy.SharedRemoteSettingsService.rustService()`
- 参照: `lazy.TaskQueue`, `lazy.Utils.shouldSkipRemoteActivity`, `this.#ingestQueue`, `this.#remoteSettingsService`

## SuggestBackendRust.enablingPreferences()
- 位置: L124-126
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestBackendRust.config()
- 位置: L133-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#config`

## SuggestBackendRust.ingestPromise()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#ingestQueue.emptyPromise`

## SuggestBackendRust.enable()
- 位置: L145-151
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (enabled)` → `this.#init()`
- 条件付き依存: `if (!(enabled))` → `this.#uninit()`

## SuggestBackendRust.query()
- 位置: async L169-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.suggest.queryTime[label].accumulateSingleSample()`, `getSuggestionType()`, `liftSuggestion()`, `liftedSuggestions.push()`, `this.#store.queryWithMetrics()`, `this.logger.debug()`, `types.map()`, `uniqueProviders.add()`
- 条件付き依存: `if (!provider)` → `this.#providerFromSuggestionType()`
- 条件付き依存: `if (feature)` → `SuggestBackendRust.mergeProviderConstraints()`
- 参照: `Glean.suggest.queryTime`, `feature.rustProviderConstraints`, `lazy.SuggestionProviderConstraints`, `lazy.SuggestionQuery`, `suggestion.icon`, `suggestion.iconMimetype`, `suggestion.icon_blob`, `suggestion.provider`, `suggestion.source`, `this.#enabledSuggestionTypes`, `this.#store`

## SuggestBackendRust.cancelQuery()
- 位置: L250-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.interrupt()`
- 参照: `lazy.InterruptKind.READ`

## SuggestBackendRust.getConfigForSuggestionType()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#configsBySuggestionType.get()`

## SuggestBackendRust.ingestEnabledSuggestions()
- 位置: L283-310
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.isEnabled || !feature.isEnabled)` → `this.#providerConstraintsOnLastIngestByFeature.delete()`
- 条件付き依存: `if (!(!this.isEnabled || !feature.isEnabled))` → `this.#providerConstraintsOnLastIngestByFeature.has()`
- 条件付き依存: `if (!(!this.isEnabled || !feature.isEnabled))` → `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (!(!this.isEnabled || !feature.isEnabled))` → `this.#providerConstraintsOnLastIngestByFeature.get()`
- 条件付き依存: `if ( evenIfFresh || !this.#providerConstraintsOnLastIngestByFeature.has(feature) || !lazy.ObjectUtils.deepEqual( providerConstraints, this.#providerConstraintsOn...)` → `this.#providerConstraintsOnLastIngestByFeature.set()`
- 条件付き依存: `if ( evenIfFresh || !this.#providerConstraintsOnLastIngestByFeature.has(feature) || !lazy.ObjectUtils.deepEqual( providerConstraints, this.#providerConstraintsOn...)` → `this.#ingestSuggestionType()`
- 参照: `feature.isEnabled`, `feature.rustProviderConstraints`, `feature.rustSuggestionType`, `this.isEnabled`

## SuggestBackendRust.dismissRustSuggestion()
- 位置: async L321-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lowerSuggestion()`, `this.#store?.dismissBySuggestion()`, `this.logger.error()`

## SuggestBackendRust.dismissByKey()
- 位置: async L339-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.dismissByKey()`, `this.logger.error()`

## SuggestBackendRust.isRustSuggestionDismissed()
- 位置: async L358-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lowerSuggestion()`, `this.#store?.isDismissedBySuggestion()`, `this.logger.error()`

## SuggestBackendRust.isDismissedByKey()
- 位置: async L382-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.isDismissedByKey()`, `this.logger.error()`

## SuggestBackendRust.anyDismissedSuggestions()
- 位置: async L397-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.anyDismissedSuggestions()`, `this.logger.error()`

## SuggestBackendRust.clearDismissedSuggestions()
- 位置: async L410-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.clearDismissedSuggestions()`, `this.logger.error()`

## SuggestBackendRust.fetchGeonames()
- 位置: async L437-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store.fetchGeonames()`
- 参照: `this.#store`

## SuggestBackendRust.fetchGeonameAlternates()
- 位置: async L466-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.fetchGeonameAlternates()`

## SuggestBackendRust.notify()
- 位置: L474-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ingestAll()`, `this.logger.info()`

## SuggestBackendRust.mergeProviderConstraints()
- 位置: L493-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.hasOwnProperty()`, `b.hasOwnProperty()`
- 条件付き依存: `if (!(!a.dynamicSuggestionTypes || !b.dynamicSuggestionTypes))` → `a.dynamicSuggestionTypes.concat(b.dynamicSuggestionTypes).sort()`
- 条件付き依存: `if (!(!a.dynamicSuggestionTypes || !b.dynamicSuggestionTypes))` → `a.dynamicSuggestionTypes.concat()`
- 参照: `a.dynamicSuggestionTypes`, `b.dynamicSuggestionTypes`, `merged.dynamicSuggestionTypes`

## SuggestBackendRust.#storeDataPath()
- 位置: L528-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("ProfD", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `Services.dirsvc`

## SuggestBackendRust.#enabledSuggestionTypes()
- 位置: L548-560
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (feature.isEnabled)` → `this.#providerFromSuggestionType()`
- 条件付き依存: `if (provider)` → `items.push()`
- 参照: `feature.isEnabled`, `feature.rustSuggestionType`, `lazy.QuickSuggest.rustFeatures`

## SuggestBackendRust.#init()
- 位置: L562-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getIntPref()`, `lazy.AsyncShutdown.profileChangeTeardown.addBlocker()`, `lazy.UrlbarPrefs.get()`, `lazy.timerManager.registerTimer()`, `this.#ingestAll()`, `this.#makeStore()`, `this.#migrateBlockedDigests()`, `this.#migrateBlockedDigests().then()`, `this.logger.debug()`
- 参照: `this.#shutdownBlocker`, `this.#store`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#shutdownBlocker()
- 位置: L576-588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store?.interrupt()`
- 参照: `lazy.InterruptKind.READ_WRITE`, `this.#shutdownBlocker`, `this.#store`

## SuggestBackendRust.#makeStore()
- 位置: L616-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `builder.build()`, `lazy.SuggestStoreBuilder.init()`, `lazy.SuggestStoreBuilder.init() .dataPath()`, `lazy.SuggestStoreBuilder.init() .dataPath(this.#storeDataPath) .remoteSettingsService()`, `this.logger.error()`, `this.logger.info()`
- 参照: `AppConstants.SQLITE_LIBRARY_FILENAME`, `this.#remoteSettingsService`, `this.#storeDataPath`

## SuggestBackendRust.#uninit()
- 位置: L647-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AsyncShutdown.profileChangeTeardown.removeBlocker()`, `lazy.timerManager.unregisterTimer()`, `this.#configsBySuggestionType.clear()`, `this.#providerConstraintsOnLastIngestByFeature.clear()`
- 参照: `this.#shutdownBlocker`, `this.#store`

## SuggestBackendRust.#ingestSuggestionType()
- 位置: L670-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.suggest.ingestDownloadTime[label].accumulateSingleSample()`, `Glean.suggest.ingestTime[label].accumulateSingleSample()`, `this.#configsBySuggestionType.set()`, `this.#ingestQueue.queueIdleCallback()`, `this.#providerFromSuggestionType()`, `this.#store.fetchProviderConfig()`, `this.#store.ingest()`, `this.logger.debug()`, `this.logger.error()`
- 参照: `Glean.suggest.ingestDownloadTime`, `Glean.suggest.ingestTime`, `error.reason`, `lazy.SuggestIngestionConstraints`, `lazy.SuggestionProviderConstraints`, `metrics.downloadTimes`, `metrics.ingestionTimes`, `this.#store`

## SuggestBackendRust.#ingestAll()
- 位置: L722-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ingestQueue.queueIdleCallback()`, `this.#store.fetchGlobalConfig()`, `this.ingestEnabledSuggestions()`, `this.logger.debug()`
- 参照: `lazy.QuickSuggest.rustFeatures`, `this.#config`, `this.#store`

## SuggestBackendRust.#providerFromSuggestionType()
- 位置: L749-758
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SuggestionProvider.hasOwnProperty()`, `type.toUpperCase()`
- 条件付き依存: `if (!lazy.SuggestionProvider.hasOwnProperty(key))` → `this.logger.error()`
- 参照: `lazy.SuggestionProvider`

## SuggestBackendRust.#migrateBlockedDigests()
- 位置: async L766-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.getCharPref()`, `this.#migrateBlockedDigestsJson()`, `this.logger.debug()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `error.result`, `this.#store`
- XPCOM: `Services.prefs`

## SuggestBackendRust.#migrateBlockedDigestsJson()
- 位置: async L796-823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Promise.all()`, `promises.push()`, `this.#store.dismissByKey()`, `this.logger.debug()`
- 条件付き依存: `if (!digests)` → `this.logger.debug()`
- 条件付き依存: `if (!Array.isArray(digests))` → `this.logger.debug()`

## SuggestBackendRust._test_store()
- 位置: L825-827
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#store`

## SuggestBackendRust._test_enabledSuggestionTypes()
- 位置: L829-831
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#enabledSuggestionTypes`

## SuggestBackendRust._test_setRemoteSettingsService()
- 位置: async L833-842
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isEnabled)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (this.isEnabled)` → `this.#uninit()`
- 条件付き依存: `if (this.isEnabled)` → `this.#init()`
- 参照: `this.#remoteSettingsService`, `this.ingestPromise`, `this.isEnabled`
- XPCOM: `Services.prefs`

## SuggestBackendRust._test_ingest()
- 位置: async L844-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ingestAll()`
- 参照: `this.ingestPromise`

## getSuggestionType()
- 位置: L876-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSuggestionTypesByCtor.get()`
- 条件付き依存: `if (!type)` → `Object.keys(lazy.Suggestion).find()`
- 条件付き依存: `if (!type)` → `Object.keys()`
- 条件付き依存: `if (type)` → `gSuggestionTypesByCtor.set()`
- 条件付き依存: `if (!(type))` → `console.error()`
- 参照: `lazy.Suggestion`, `suggestion.constructor`

## liftSuggestion()
- 位置: L930-951
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof data == "string")` → `JSON.parse()`
- 参照: `lazy.Suggestion.Dynamic`, `suggestion.dismissalKey`, `suggestion.score`, `suggestion.suggestionType`

## lowerSuggestion()
- 位置: L967-982
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (data !== null && data !== undefined)` → `JSON.stringify()`
- 参照: `lazy.Suggestion.Dynamic`, `suggestion.dismissalKey`, `suggestion.provider`, `suggestion.score`, `suggestion.suggestionType`
