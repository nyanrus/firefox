# browser/extensions/newtab/lib/InferredPersonalizationFeed.sys.mjs

source: browser/extensions/newtab/lib/InferredPersonalizationFeed.sys.mjs
source-hash: 9c87360d3a42ad668786bfbdfdcfccb10bca6c28
lines: 707

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## timeMSToSeconds()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`

## computeAverageCTRFromTopics()
- 位置: L86-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sumTopics()`
- 参照: `AggregateResultKeys.FEATURE`, `AggregateResultKeys.VALUE`

## sumTopics()
- 位置: L94-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `KNOWN_TOPICS.has()`

## InferredPersonalizationFeed.constructor()
- 位置: L121-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.cache`, `this.loaded`

## InferredPersonalizationFeed.reset()
- 位置: async L126-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`, `this.store.dispatch()`
- 条件付き依存: `if (this.cache)` → `this.cache.set()`
- 参照: `at.INFERRED_PERSONALIZATION_RESET`, `this.cache`, `this.loaded`

## InferredPersonalizationFeed.isEnabled()
- 位置: L138-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## InferredPersonalizationFeed.isStoreData()
- 位置: L145-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs.values?.trainhopConfig ?.newTabSectionsExperiment?.personalizationStoreFeaturesEnabled`

## InferredPersonalizationFeed.init()
- 位置: async L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadInterestVector()`

## InferredPersonalizationFeed.queryDatabaseForTimeIntervals()
- 位置: async L154-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `results.push()`, `this.fetchInferredPersonalizationSummary()`
- 参照: `interval.end`, `interval.start`

## InferredPersonalizationFeed.getInferredModelData()
- 位置: async L172-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dsCache.get()`, `this.PersistentCache()`, `this.store.getState()`
- 条件付き依存: `if (modelOverrideRaw)` → `JSON.parse()`
- 参照: `this.store.getState().Prefs.values`

## InferredPersonalizationFeed._getDebugOverrides()
- 位置: async L200-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`, `this.store?.getState()`
- 条件付き依存: `if (typeof prefValue === "string" && prefValue)` → `JSON.parse()`
- 条件付き依存: `if (typeof prefValue === "string" && prefValue)` → `console.error()`
- 参照: `this.store?.getState?.()?.Prefs?.values`

## InferredPersonalizationFeed.setDebuggingInterestFeaturesOverride()
- 位置: async L233-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `ac.SetPref()`, `this.cache.set()`, `this.store?.dispatch()`

## InferredPersonalizationFeed.getDebuggingInterestFeaturesSupported()
- 位置: async L267-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FeatureModel.fromJSON()`, `model.getInterestFeaturesSupported()`, `this._getDebugOverrides()`, `this.cache.get()`, `this.getInferredModelData()`
- 条件付き依存: `if (interestVector)` → `Object.keys(features).forEach()`
- 条件付き依存: `if (interestVector)` → `Object.keys()`
- 参照: `features[featureName].currentValue`, `features[featureName].overrideValue`, `inferredModel.model_data`, `interestVector?.data?.coarseInferredInterests`

## InferredPersonalizationFeed.generateInterestVector()
- 位置: async L301-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `model.computeInterestVectors()`, `model.getDateIntervals()`, `this.Date()`, `this.Date().now()`, `this.queryDatabaseForTimeIntervals()`
- 条件付き依存: `if ( model.modelType === MODEL_TYPE.CLICK_IMP_PAIR || model.modelType === MODEL_TYPE.CTR )` → `this.queryDatabaseForTimeIntervals()`
- 条件付き依存: `if ( model.modelType === MODEL_TYPE.CLICK_IMP_PAIR || model.modelType === MODEL_TYPE.CTR )` → `model.computeInterestVector()`
- 条件付き依存: `if (model.modelType === MODEL_TYPE.CTR)` → `this._getDebugOverrides()`
- 条件付き依存: `if (model.modelType === MODEL_TYPE.CTR)` → `model.hasBayesianSmoothing()`
- 条件付き依存: `if (model.modelType === MODEL_TYPE.CTR)` → `computeAverageCTRFromTopics()`
- 条件付き依存: `if (model.modelType === MODEL_TYPE.CTR)` → `model.computeCTRInterestVectors()`
- 条件付き依存: `if (model.modelType === MODEL_TYPE.CTR)` → `lazy.NewTabUtils.getUtcOffset()`
- 参照: `AggregateResultKeys.FEATURE`, `AggregateResultKeys.FORMAT_ENUM`, `AggregateResultKeys.VALUE`, `MODEL_TYPE.CLICKS`, `MODEL_TYPE.CLICK_IMP_PAIR`, `MODEL_TYPE.CTR`, `interests.inferredInterests`, `model.modelType`

## InferredPersonalizationFeed.loadInterestVector()
- 位置: async L374-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.Date()`, `this.Date().now()`, `this.cache.get()`, `this.cache.set()`, `this.store.dispatch()`, `this.store.getState()`
- 条件付き依存: `if ( !interest_vector?.lastUpdated || !( this.Date().now() - interest_vector.lastUpdated < interestVectorRefreshHours * HOURS_TO_MS ) )` → `this.Date().now()`
- 条件付き依存: `if ( !interest_vector?.lastUpdated || !( this.Date().now() - interest_vector.lastUpdated < interestVectorRefreshHours * HOURS_TO_MS ) )` → `this.Date()`
- 条件付き依存: `if (needsCleanup)` → `this.clearOldData()`
- 条件付き依存: `if (needsCleanup)` → `this.Date().now()`
- 条件付き依存: `if (needsCleanup)` → `this.Date()`
- 条件付き依存: `if ( !interest_vector?.lastUpdated || !( this.Date().now() - interest_vector.lastUpdated < interestVectorRefreshHours * HOURS_TO_MS ) )` → `this.getInferredModelData()`
- 条件付き依存: `if (inferredModel && inferredModel.model_data)` → `FeatureModel.fromJSON()`
- 条件付き依存: `if (inferredModel && inferredModel.model_data)` → `this.generateInterestVector()`
- 参照: `at.INFERRED_PERSONALIZATION_UPDATE`, `inferredModel.model_data`, `inferredModel.model_id`, `inferredModel.privacy_overrides`, `interest_vector.data.coarseInferredInterests`, `interest_vector.data.coarsePrivateInferredInterests`, `interest_vector.data.inferredInterests`, `interest_vector.lastUpdated`, `interest_vector?.lastClearedDB`, `interest_vector?.lastUpdated`, `this.loaded`, `this.store.getState().Prefs`, `values?.inferredPersonalizationConfig?.history_cull_days`, `values?.inferredPersonalizationConfig?.iv_refresh_frequency_hours`

## InferredPersonalizationFeed.handleDiscoveryStreamImpressionStats()
- 位置: async L441-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["organic"].includes()`
- 条件付き依存: `if (["organic"].includes(type))` → `this.recordInferredPersonalizationImpression()`
- 参照: `action.data`

## InferredPersonalizationFeed.handleDiscoveryStreamUserEvent()
- 位置: async L458-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["organic"].includes()`
- 条件付き依存: `if (["organic"].includes(card_type))` → `this.recordInferredPersonalizationClick()`
- 参照: `action.data.action_position`, `action.data.value`, `action.data?.event`

## InferredPersonalizationFeed.recordInferredPersonalizationImpression()
- 位置: async L479-481
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordInferredPersonalizationInteraction()`

## InferredPersonalizationFeed.recordInferredPersonalizationClick()
- 位置: async L482-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordInferredPersonalizationInteraction()`

## InferredPersonalizationFeed.fetchInferredPersonalizationImpression()
- 位置: async L490-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fetchInferredPersonalizationInteraction()`

## InferredPersonalizationFeed.fetchInferredPersonalizationSummary()
- 位置: async L496-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activityStreamProvider.executePlacesQuery()`, `timeMSToSeconds()`
- 参照: `lazy.NewTabUtils`

## InferredPersonalizationFeed.clearOldDataOfTable()
- 位置: async L512-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `db.execute()`, `placesUtils.withConnectionWrapper()`, `this.Date()`, `this.Date().now()`, `timeMSToSeconds()`
- 参照: `lazy.PlacesUtils`

## InferredPersonalizationFeed.clearOldData()
- 位置: async L536-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearOldDataOfTable()`

## InferredPersonalizationFeed.recordInferredPersonalizationInteraction()
- 位置: async L541-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `db.execute()`, `featureValuePairs.map()`, `lazy.PlacesUtils.withConnectionWrapper()`, `this.Date()`, `this.Date().now()`, `timeMSToSeconds()`
- 条件付き依存: `if (extraClickEvent)` → `featureValuePairs.push()`
- 条件付き依存: `if (tile.features)` → `featureValuePairs.concat()`
- 条件付き依存: `if (tile.features)` → `Object.entries()`
- 参照: `tile.features`, `tile.format`, `tile.pos`, `tile.section_position`

## InferredPersonalizationFeed.fetchInferredPersonalizationInteraction()
- 位置: async L588-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activityStreamProvider.executePlacesQuery()`
- 参照: `lazy.NewTabUtils`

## InferredPersonalizationFeed.onPrefChangedAction()
- 位置: async L607-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`
- 条件付き依存: `if (this.isEnabled() && action.data.value)` → `this.loadInterestVector()`
- 条件付き依存: `if (!(this.isEnabled() && action.data.value))` → `this.reset()`
- 参照: `action.data.name`, `action.data.value`

## InferredPersonalizationFeed.onAction()
- 位置: async L620-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.clearOldData()`, `this.getDebuggingInterestFeaturesSupported()`, `this.isEnabled()`, `this.isStoreData()`, `this.onPrefChangedAction()`, `this.reset()`, `this.setDebuggingInterestFeaturesOverride()`, `this.store.dispatch()`
- 条件付き依存: `if (this.isEnabled())` → `this.init()`
- 条件付き依存: `if (this.loaded && this.isEnabled())` → `this.loadInterestVector()`
- 条件付き依存: `if (this.cache)` → `this.cache.set()`
- 条件付き依存: `if (this.isEnabled())` → `this.reset()`
- 条件付き依存: `if (this.isEnabled())` → `this.loadInterestVector()`
- 条件付き依存: `if (this.isEnabled())` → `this.getDebuggingInterestFeaturesSupported()`
- 条件付き依存: `if (this.isEnabled())` → `this.store.dispatch()`
- 条件付き依存: `if (this.isEnabled())` → `ac.BroadcastToContent()`
- 条件付き依存: `if (this.isEnabled() || this.isStoreData())` → `this.handleDiscoveryStreamImpressionStats()`
- 条件付き依存: `if (this.isEnabled() || this.isStoreData())` → `this.handleDiscoveryStreamUserEvent()`
- 参照: `action.data`, `action.type`, `at.DISCOVERY_STREAM_DEV_SYSTEM_TICK`, `at.DISCOVERY_STREAM_IMPRESSION_STATS`, `at.DISCOVERY_STREAM_USER_EVENT`, `at.INFERRED_PERSONALIZATION_CLEAR_INTEREST_VECTOR`, `at.INFERRED_PERSONALIZATION_DEBUG_FEATURES_REQUEST`, `at.INFERRED_PERSONALIZATION_DEBUG_FEATURES_UPDATE`, `at.INFERRED_PERSONALIZATION_DEBUG_OVERRIDES_SET`, `at.INFERRED_PERSONALIZATION_REFRESH`, `at.INIT`, `at.PLACES_HISTORY_CLEARED`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.UNINIT`, `this.cache`, `this.loaded`

## InferredPersonalizationFeed.prototype.PersistentCache()
- 位置: L701-703
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## InferredPersonalizationFeed.prototype.Date()
- 位置: L704-706
- 役割: (未記入)
- 触るとき: (未記入)
