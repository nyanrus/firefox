# browser/components/search/SERPCategorization.sys.mjs

source: browser/components/search/SERPCategorization.sys.mjs
source-hash: c29fe45ab3aa42aadf4f76d635ceb652b1e41e84
lines: 1752

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/security/hash;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## Categorizer.init()
- 位置: async L126-133
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.enabled)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.enabled)` → `SERPDomainToCategoriesMap.init()`
- 条件付き依存: `if (this.enabled)` → `SERPCategorizationEventScheduler.init()`
- 条件付き依存: `if (this.enabled)` → `SERPCategorizationRecorder.init()`
- 参照: `this.enabled`

## Categorizer.uninit()
- 位置: async L135-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SERPCategorizationEventScheduler.uninit()`, `SERPCategorizationRecorder.uninit()`, `SERPDomainToCategoriesMap.uninit()`, `lazy.logConsole.debug()`

## Categorizer.enabled()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.serpEventTelemetryCategorization`

## Categorizer.maybeCategorizeSERP()
- 位置: async L158-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SERPDomainToCategoriesMap.version.toString()`, `this.applyCategorizationLogic()`
- 条件付き依存: `if (SERPDomainToCategoriesMap.empty)` → `SERPCategorizationRecorder.recordMissingImpressionTelemetry()`
- 参照: `SERPDomainToCategoriesMap.empty`, `results.category`, `results.num_domains`, `results.num_inconclusive`, `results.num_unknown`, `resultsToReport.mappings_version`, `resultsToReport.organic_category`, `resultsToReport.organic_num_domains`, `resultsToReport.organic_num_inconclusive`, `resultsToReport.organic_num_unknown`, `resultsToReport.sponsored_category`, `resultsToReport.sponsored_num_domains`, `resultsToReport.sponsored_num_inconclusive`, `resultsToReport.sponsored_num_unknown`

## Categorizer.applyCategorizationLogic()
- 位置: async L197-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SERPDomainToCategoriesMap.get()`, `domainsCount.toString()`, `finalCategory.toString()`, `inconclusivesCount.toString()`, `unknownsCount.toString()`
- 条件付き依存: `if (!(unknownsCount + inconclusivesCount == domainsCount))` → `Object.values()`
- 条件付き依存: `if (!(unknownsCount + inconclusivesCount == domainsCount))` → `Math.log2()`
- 条件付き依存: `if (adjustedScore == maxScore)` → `topCategories.push()`
- 条件付き依存: `if (adjustedScore == maxScore)` → `Number()`
- 条件付き依存: `if (!(unknownsCount + inconclusivesCount == domainsCount))` → `this.#chooseRandomlyFrom()`
- 参照: `CATEGORIZATION_SETTINGS.INCONCLUSIVE`, `CATEGORIZATION_SETTINGS.MINIMUM_SCORE`, `CATEGORIZATION_SETTINGS.STARTING_RANK`, `categoryCandidates.length`, `categoryCandidates[0].category`, `topCategories.length`

## Categorizer.#chooseRandomlyFrom()
- 位置: L258-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`
- 参照: `categories.length`

## CategorizationEventScheduler.init()
- 位置: L302-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/useridleservice;1"].getService()`, `Services.obs.addObserver()`, `lazy.logConsole.debug()`, `this.#idleService.addIdleObserver()`
- 参照: `CATEGORIZATION_SETTINGS.IDLE_TIMEOUT_SECONDS`, `Ci.nsIUserIdleService`, `this.#browserToCallbackMap`, `this.#idleService`, `this.#init`
- XPCOM: `nsIUserIdleService` / `@mozilla.org/widget/useridleservice;1` / `Services.obs`

## CategorizationEventScheduler.uninit()
- 位置: L331-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.logConsole.debug()`, `this.#idleService.removeIdleObserver()`
- 参照: `CATEGORIZATION_SETTINGS.IDLE_TIMEOUT_SECONDS`, `this.#browserToCallbackMap`, `this.#idleService`, `this.#init`
- XPCOM: `Services.obs`

## CategorizationEventScheduler.observe()
- 位置: L351-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.logConsole.debug()`, `this.#sendAllCallbacks()`, `this.uninit()`
- 条件付き依存: `if ( this.#mostRecentMs && Date.now() - this.#mostRecentMs >= CATEGORIZATION_SETTINGS.WAKE_TIMEOUT_MS )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( this.#mostRecentMs && Date.now() - this.#mostRecentMs >= CATEGORIZATION_SETTINGS.WAKE_TIMEOUT_MS )` → `this.#sendAllCallbacks()`
- 参照: `CATEGORIZATION_SETTINGS.WAKE_TIMEOUT_MS`, `this.#mostRecentMs`

## CategorizationEventScheduler.addCallback()
- 位置: L375-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.logConsole.debug()`, `this.#browserToCallbackMap?.set()`
- 参照: `this.#mostRecentMs`

## CategorizationEventScheduler.sendCallback()
- 位置: L381-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserToCallbackMap?.get()`
- 条件付き依存: `if (callback)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (callback)` → `callback()`
- 条件付き依存: `if (callback)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (callback)` → `this.#browserToCallbackMap.delete()`
- XPCOM: `Services.obs`

## CategorizationEventScheduler.#sendAllCallbacks()
- 位置: L394-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`, `Services.obs.notifyObservers()`
- 条件付き依存: `if (browsers)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (browsers)` → `this.sendCallback()`
- 参照: `this.#browserToCallbackMap`, `this.#mostRecentMs`
- XPCOM: `Services.obs`

## CategorizationRecorder.init()
- 位置: async L422-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `this.submitPing()`
- 参照: `this.#init`, `this.#serpCategorizationsCount`
- XPCOM: `Services.obs` / `Services.prefs`

## CategorizationRecorder.uninit()
- 位置: L439-451
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#init)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#init)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (this.#init)` → `this.#resetCategorizationRecorderData()`
- 参照: `this.#init`, `this.#serpCategorizationsCount`
- XPCOM: `Services.obs` / `Services.prefs`

## CategorizationRecorder.observe()
- 位置: L453-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (this.#userInteractionStartTime == null)` → `Date.now()`
- 条件付き依存: `if ( this.#userInteractionStartTime && currentTime - this.#userInteractionStartTime >= activityLimitInMs )` → `this.submitPing()`
- 参照: `lazy.activityLimit`, `this.#userInteractionStartTime`

## CategorizationRecorder.recordCategorizationTelemetry()
- 位置: L484-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.serp.categorization.record()`, `lazy.logConsole.debug()`, `this.#incrementCategorizationsCount()`

## CategorizationRecorder.recordMissingImpressionTelemetry()
- 位置: L499-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.serp.categorizationNoMapFound.add()`, `lazy.logConsole.debug()`, `this.#incrementCategorizationsCount()`

## CategorizationRecorder.maybeExtractAndRecordExperimentInfo()
- 位置: L511-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.serp.experimentInfo.set()`, `lazy.NimbusFeatures.search.getEnrollmentMetadata()`, `lazy.NimbusFeatures.search.getVariable()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (!targetExperiment)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (metadata?.slug !== targetExperiment)` → `lazy.NimbusFeatures.search.getEnrollmentMetadata()`
- 条件付き依存: `if (metadata?.slug !== targetExperiment)` → `lazy.logConsole.debug()`
- 参照: `lazy.EnrollmentType.EXPERIMENT`, `lazy.EnrollmentType.ROLLOUT`, `metadata.branch`, `metadata.slug`, `metadata?.slug`

## CategorizationRecorder.submitPing()
- 位置: L545-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings.serpCategorization.submit()`, `lazy.logConsole.debug()`, `this.maybeExtractAndRecordExperimentInfo()`
- 参照: `this.#serpCategorizationsCount`

## CategorizationRecorder.testReset()
- 位置: L564-568
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (Cu.isInAutomation)` → `this.#resetCategorizationRecorderData()`
- 参照: `Cu.isInAutomation`

## CategorizationRecorder.#incrementCategorizationsCount()
- 位置: L570-579
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this.#serpCategorizationsCount >= CATEGORIZATION_SETTINGS.PING_SUBMISSION_THRESHOLD )` → `this.submitPing()`
- 参照: `CATEGORIZATION_SETTINGS.PING_SUBMISSION_THRESHOLD`, `this.#serpCategorizationsCount`

## CategorizationRecorder.#resetCategorizationRecorderData()
- 位置: L581-584
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#serpCategorizationsCount`, `this.#userInteractionStartTime`

## DomainToCategoriesMap.init()
- 位置: async L669-692
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#setupClientAndStore()`, `this.uninit()`
- 条件付き依存: `if (this.#client && this.#store)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#client && this.#store)` → `Services.obs.notifyObservers()`
- 参照: `this.#client`, `this.#init`, `this.#store`
- XPCOM: `Services.obs`

## DomainToCategoriesMap.uninit()
- 位置: async L694-716
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#init)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#init)` → `this.#clearClient()`
- 条件付き依存: `if (this.#init)` → `this.#cancelAndNullifyTimer()`
- 条件付き依存: `if (shouldDeleteStore)` → `this.#store.dropData()`
- 条件付き依存: `if (shouldDeleteStore)` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#store)` → `this.#store.uninit()`
- 条件付き依存: `if (this.#init)` → `Services.obs.notifyObservers()`
- 参照: `this.#init`, `this.#store`
- XPCOM: `Services.obs`

## DomainToCategoriesMap.get()
- 位置: async L726-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gCryptoHash.finish()`, `lazy.gCryptoHash.init()`, `lazy.gCryptoHash.update()`, `new TextEncoder().encode()`, `this.#store.getCategories()`
- 条件付き依存: `if (rawValues?.length)` → `output.push()`
- 参照: `bytes.length`, `lazy.gCryptoHash.SHA256`, `rawValues.length`, `rawValues?.length`, `this.#store`, `this.#store.empty`, `this.#store.ready`

## DomainToCategoriesMap.version()
- 位置: L756-758
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#version`

## DomainToCategoriesMap.empty()
- 位置: L765-770
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#store`, `this.#store.empty`

## DomainToCategoriesMap.overrideMapForTests()
- 位置: async L784-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.exists()`
- 条件付き依存: `if (Cu.isInAutomation || Services.env.exists("XPCSHELL_TEST_PROFILE_DIR"))` → `this.#store.init()`
- 条件付き依存: `if (Cu.isInAutomation || Services.env.exists("XPCSHELL_TEST_PROFILE_DIR"))` → `this.#store.dropData()`
- 条件付き依存: `if (Cu.isInAutomation || Services.env.exists("XPCSHELL_TEST_PROFILE_DIR"))` → `this.#store.insertObject()`
- 参照: `Cu.isInAutomation`
- XPCOM: `Services.env`

## DomainToCategoriesMap.findRecordsForRegion()
- 位置: L814-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordMatchesRegion()`
- 条件付き依存: `if (record.isDefault)` → `defaultRecords.push()`
- 条件付き依存: `if (!(record.isDefault))` → `regionSpecificRecords.push()`
- 参照: `defaultRecords.length`, `record.isDefault`, `records?.length`, `regionSpecificRecords.length`

## DomainToCategoriesMap.recordMatchesRegion()
- 位置: L851-869
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `record.excludeRegions?.includes()`, `record.includeRegions?.includes()`
- 参照: `record.isDefault`

## DomainToCategoriesMap.syncMayModifyStore()
- 位置: async L871-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordsDifferFromStore()`, `syncData.updated.map()`, `this.#store.isDefault()`, `this.findRecordsForRegion()`
- 条件付き依存: `if (this.#store.empty && !currentResult)` → `lazy.logConsole.debug()`
- 参照: `currentResult.isDefault`, `obj.new`, `syncData.created`, `syncData.deleted`, `syncData?.current`, `this.#store.empty`

## recordsDifferFromStore()
- 位置: L891-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findRecordsForRegion()`
- 参照: `result.isDefault`, `result?.records.length`

## DomainToCategoriesMap.#setupClientAndStore()
- 位置: async L915-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.RemoteSettings()`, `lazy.logConsole.debug()`, `this.#clearAndPopulateStore()`, `this.#client.get()`, `this.#client.on()`, `this.#retrieveLatestVersion()`, `this.#store.getVersion()`, `this.#store.init()`, `this.#store.isDefault()`, `this.findRecordsForRegion()`
- 条件付き依存: `if (!records.length)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasMatchingRecords)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#store.empty)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#store.empty)` → `this.#store.dropData()`
- 条件付き依存: `if ( storeVersion == this.#version && !this.#store.empty && storeIsDefault == matchingRecordsAreDefault )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( storeVersion == this.#version && !this.#store.empty && storeIsDefault == matchingRecordsAreDefault )` → `Services.obs.notifyObservers()`
- 参照: `lazy.Region.home`, `matchingRecords?.length`, `records.length`, `result?.isDefault`, `result?.records`, `this.#client`, `this.#onSettingsSync`, `this.#store`, `this.#store.empty`, `this.#version`, `this.empty`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#onSettingsSync()
- 位置: L922-922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sync()`
- 参照: `event.data`

## DomainToCategoriesMap.#clearClient()
- 位置: L979-987
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#client)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#client)` → `this.#client.off()`
- 参照: `this.#client`, `this.#downloadRetries`, `this.#onSettingsSync`

## DomainToCategoriesMap.#retrieveLatestVersion()
- 位置: L999-1006
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `records.reduce()`
- 参照: `record.version`

## DomainToCategoriesMap.#sync()
- 位置: async L1017-1042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `data?.deleted.filter()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#clearAndPopulateStore()`, `this.#client.attachments.deleteDownloaded()`, `this.syncMayModifyStore()`, `this.uninit()`, `toDelete.map()`
- 条件付き依存: `if (!couldModify)` → `lazy.logConsole.debug()`
- 参照: `d.attachment`, `data?.current`, `lazy.Region.home`, `this.#downloadRetries`

## DomainToCategoriesMap.#clearAndPopulateStore()
- 位置: async L1055-1136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Services.obs.notifyObservers()`, `Services.prefs.setBoolPref()`, `fileContents.push()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#cancelAndNullifyTimer()`, `this.#client.attachments.download()`, `this.#createTimerToPopulateMap()`, `this.#retrieveLatestVersion()`, `this.#store.dropData()`, `this.#store.insertFileContents()`, `this.findRecordsForRegion()`
- 条件付き依存: `if (!this.#store)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#store.ready)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!records?.length)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasMatchingRecords)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#version)` → `lazy.logConsole.debug()`
- 参照: `fetchedAttachment.buffer`, `lazy.Region.home`, `records?.length`, `recordsMatchingRegion?.length`, `result?.isDefault`, `result?.records`, `this.#store`, `this.#store.ready`, `this.#version`
- XPCOM: `Services.obs` / `Services.prefs`

## DomainToCategoriesMap.#cancelAndNullifyTimer()
- 位置: L1138-1144
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#downloadTimer)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#downloadTimer)` → `this.#downloadTimer.cancel()`
- 参照: `this.#downloadTimer`

## DomainToCategoriesMap.#createTimerToPopulateMap()
- 位置: L1146-1180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `randomInteger()`, `this.#clearAndPopulateStore()`, `this.#client.get()`, `this.#downloadTimer.initWithCallback()`, `this.uninit()`
- 条件付き依存: `if (!this.#downloadTimer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.base`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.maxAdjust`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.maxTriesPerSession`, `TELEMETRY_CATEGORIZATION_DOWNLOAD_SETTINGS.minAdjust`, `this.#client`, `this.#downloadRetries`, `this.#downloadTimer`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## DomainToCategoriesStore.init()
- 位置: async L1221-1270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#initConnection()`, `this.#rebuildableErrors.includes()`
- 条件付き依存: `if (this.#rebuildableErrors.includes(ex1.name))` → `this.#rebuildStore()`
- 条件付き依存: `if (this.#rebuildableErrors.includes(ex1.name))` → `this.#closeConnection()`
- 条件付き依存: `if (this.#rebuildableErrors.includes(ex1.name))` → `lazy.logConsole.error()`
- 条件付き依存: `if (!this.#connection)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!rebuiltStore)` → `this.#initSchema()`
- 条件付き依存: `if (!rebuiltStore)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!rebuiltStore)` → `this.#closeConnection()`
- 参照: `ex1.name`, `this.#connection`, `this.#init`

## DomainToCategoriesStore.uninit()
- 位置: async L1272-1278
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#init)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#init)` → `this.#closeConnection()`
- 参照: `this.#init`

## DomainToCategoriesStore.ready()
- 位置: L1285-1287
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#init`

## DomainToCategoriesStore.empty()
- 位置: L1294-1296
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#empty`

## DomainToCategoriesStore.dropData()
- 位置: async L1305-1343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connection.tableExists()`
- 条件付き依存: `if (tableExists)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (tableExists)` → `this.#connection.executeTransaction()`
- 条件付き依存: `if (tableExists)` → `this.#connection.execute()`
- 条件付き依存: `if (tableExists)` → `this.#connection.executeCached()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_NAME`, `this.#connection`, `this.#empty`

## DomainToCategoriesStore.insertFileContents()
- 位置: async L1360-1371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `this.#insert()`, `this.dropData()`
- 参照: `fileContents?.length`, `this.#init`

## DomainToCategoriesStore.insertObject()
- 位置: async L1387-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `new TextEncoder().encode()`, `this.insertFileContents()`
- 参照: `Cu.isInAutomation`, `new TextEncoder().encode( JSON.stringify(domainToCategoriesMap) ).buffer`, `this.#init`

## DomainToCategoriesStore.getCategories()
- 位置: async L1408-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.logConsole.error()`, `rows[0].getResultByName()`, `this.#connection.executeCached()`
- 参照: `rows.length`, `this.#init`

## DomainToCategoriesStore.getVersion()
- 位置: async L1446-1469
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#connection)` → `this.#connection.executeCached()`
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.error()`
- 条件付き依存: `if (rows.length)` → `parseInt()`
- 条件付き依存: `if (rows.length)` → `rows[0].getResultByName()`
- 参照: `rows.length`, `this.#connection`

## DomainToCategoriesStore.isDefault()
- 位置: async L1477-1502
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#connection)` → `this.#connection.executeCached()`
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#connection)` → `parseInt()`
- 条件付き依存: `if (this.#connection)` → `rows[0].getResultByName()`
- 参照: `rows.length`, `this.#connection`

## DomainToCategoriesStore.testDelete()
- 位置: async L1507-1512
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (Cu.isInAutomation)` → `this.#closeConnection()`
- 条件付き依存: `if (Cu.isInAutomation)` → `this.#delete()`
- 参照: `Cu.isInAutomation`

## DomainToCategoriesStore.#closeConnection()
- 位置: async L1517-1537
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.#connection)` → `this.#connection.close()`
- 条件付き依存: `if (this.#connection)` → `lazy.logConsole.error()`
- 条件付き依存: `if (this.#asyncShutdownBlocker)` → `lazy.Sqlite.shutdown.removeBlocker()`
- 参照: `this.#asyncShutdownBlocker`, `this.#connection`, `this.#empty`, `this.#init`

## DomainToCategoriesStore.#initSchema()
- 位置: async L1545-1582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `rows[0].getResultByIndex()`, `this.#connection.execute()`, `this.#connection.executeCached()`, `this.#connection.executeTransaction()`, `this.#connection.setSchemaVersion()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_SCHEMA`, `this.#connection`, `this.#empty`

## DomainToCategoriesStore.#delete()
- 位置: async L1590-1605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_FILE`, `PathUtils.profileDir`, `this.#empty`

## DomainToCategoriesStore.#initConnection()
- 位置: async L1614-1645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `lazy.Sqlite.openConnection()`, `lazy.Sqlite.shutdown.addBlocker()`, `lazy.logConsole.error()`, `this.#closeConnection()`, `this.#connection.execute()`
- 参照: `CATEGORIZATION_SETTINGS.STORE_FILE`, `PathUtils.profileDir`, `this.#asyncShutdownBlocker`, `this.#connection`

## this.#asyncShutdownBlocker()
- 位置: async L1629-1632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connection.close()`
- 参照: `this.#connection`

## DomainToCategoriesStore.#insert()
- 位置: async L1661-1716
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `lazy.logConsole.debug()`, `new TextDecoder().decode()`, `this.#connection.executeCached()`, `this.#connection.executeTransaction()`
- 条件付き依存: `if (isDefault)` → `this.#connection.executeCached()`
- 参照: `fileContents?.length`, `this.#empty`

## DomainToCategoriesStore.#rebuildStore()
- 位置: async L1727-1740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#closeConnection()`, `this.#delete()`, `this.#initConnection()`, `this.#initSchema()`

## randomInteger()
- 位置: L1743-1745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`
