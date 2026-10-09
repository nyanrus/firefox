# browser/extensions/newtab/lib/InferredModel/FeatureModel.sys.mjs

source: browser/extensions/newtab/lib/InferredModel/FeatureModel.sys.mjs
source-hash: 602de987bcf0f7e842c77dd27b1cc2340b86013a
lines: 719

## <module>
- 役割: (未記入)

## divideDict()
- 位置: L27-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(denominator).forEach()`, `Object.keys(numerator).forEach()`

## unaryEncodeDiffPrivacy()
- 位置: L50-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bitstring.join()`, `crypto.getRandomValues()`
- 条件付き依存: `if (trueBit === 1)` → `bitstring.push()`
- 条件付き依存: `if (!(trueBit === 1))` → `bitstring.push()`

## dictAdd()
- 位置: L73-79
- 役割: (未記入)
- 触るとき: (未記入)

## dictApply()
- 位置: L88-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(obj).map()`, `Object.fromEntries()`, `fn()`

## DayTimeWeighting.constructor()
- 位置: L105-108
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.pastDays`, `this.relativeWeight`

## DayTimeWeighting.fromJSON()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `json.days`, `json.relative_weight`

## DayTimeWeighting.getDateIntervals()
- 位置: L120-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pastDays.map()`

## DayTimeWeighting.getRelativeWeight()
- 位置: L139-144
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.pastDays.length`, `this.relativeWeight`

## InterestFeatures.constructor()
- 位置: L151-164
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.diff_p`, `this.diff_q`, `this.featureWeights`, `this.name`, `this.thresholds`

## InterestFeatures.fromJSON()
- 位置: L166-174
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `json.diff_p`, `json.diff_q`, `json.features`, `json.thresholds`

## InterestFeatures.applyThresholds()
- 位置: L182-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`
- 参照: `this.thresholds`, `this.thresholds.length`

## InterestFeatures.applyDifferentialPrivacy()
- 位置: L209-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `unaryEncodeDiffPrivacy()`
- 参照: `this.diff_p`, `this.diff_q`, `this.thresholds`, `this.thresholds.length`

## TileImportance.constructor()
- 位置: L226-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 参照: `this.mappings`

## TileImportance.getRelativeCTRForTile()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.mappings`

## TileImportance.fromJSON()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)

## FeatureModel.constructor()
- 位置: L259-283
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.ctrPriorStrength`, `this.dayTimeWeighting`, `this.interestVectorModel`, `this.logScale`, `this.modelId`, `this.modelType`, `this.normalize`, `this.normalizeL1`, `this.privateFeatures`, `this.rescale`, `this.tileImportance`

## FeatureModel.fromJSON()
- 位置: L285-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DayTimeWeighting.fromJSON()`, `InterestFeatures.fromJSON()`, `Object.entries()`, `TileImportance.fromJSON()`
- 参照: `json.clickScale`, `json.ctr_prior_strength`, `json.day_time_weighting`, `json.interest_vector`, `json.log_scale`, `json.model_type`, `json.normalize`, `json.normalize_l1`, `json.private_features`, `json.rescale`, `json.tile_importance`

## FeatureModel.getInterestFeaturesSupported()
- 位置: L309-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 参照: `feature.thresholds`, `feature.thresholds.length`, `this.interestVectorModel`

## FeatureModel.supportsCoarseInterests()
- 位置: L323-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(this.interestVectorModel).every()`
- 参照: `fm.thresholds`, `fm.thresholds.length`, `this.interestVectorModel`

## FeatureModel.supportsCoarsePrivateInterests()
- 位置: L329-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(this.interestVectorModel).every()`
- 参照: `fm.thresholds`, `fm.thresholds.length`, `this.interestVectorModel`

## FeatureModel.getDateIntervals()
- 位置: L342-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dayTimeWeighting.getDateIntervals()`

## FeatureModel.computeInterestVector()
- 位置: L356-433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.values()`, `Object.values(this.interestVectorModel).forEach()`, `dataForIntervals.map()`, `dictAdd()`, `intervalData.forEach()`, `processedPerTimeInterval.forEach()`, `this.dayTimeWeighting.getRelativeWeight()`
- 条件付き依存: `if (featureUsed in intervalRawTotal)` → `dictAdd()`
- 条件付き依存: `if (applyPostProcessing)` → `this.applyPostProcessing()`
- 条件付き依存: `if (this.clickScale && numClicks > 0)` → `dictApply()`
- 条件付き依存: `if (applyThresholding)` → `this.applyThresholding()`
- 参照: `AggregateResultKeys.FEATURE`, `AggregateResultKeys.VALUE`, `interestFeature.featureWeights`, `interestFeature.name`, `this.clickScale`, `this.interestVectorModel`

## FeatureModel.applyThresholding()
- 位置: L443-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (key in this.interestVectorModel)` → `this.interestVectorModel[key].applyThresholds()`
- 条件付き依存: `if (applyDifferentialPrivacy)` → `this.interestVectorModel[ key ].applyDifferentialPrivacy()`
- 参照: `this.interestVectorModel`

## FeatureModel.applyPostProcessing()
- 位置: L463-495
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.logScale)` → `dictApply()`
- 条件付き依存: `if (this.logScale)` → `Math.log()`
- 条件付き依存: `if (this.rescale)` → `Math.max()`
- 条件付き依存: `if (this.rescale)` → `Object.values()`
- 条件付き依存: `if (this.rescale)` → `dictApply()`
- 条件付き依存: `if (this.normalizeL1)` → `Object.values(res).reduce()`
- 条件付き依存: `if (this.normalizeL1)` → `Object.values()`
- 条件付き依存: `if (this.normalizeL1)` → `dictApply()`
- 条件付き依存: `if (this.normalize)` → `Math.sqrt()`
- 条件付き依存: `if (this.normalize)` → `Object.values(res).reduce()`
- 条件付き依存: `if (this.normalize)` → `Object.values()`
- 条件付き依存: `if (this.normalize)` → `dictApply()`
- 参照: `this.logScale`, `this.normalize`, `this.normalizeL1`, `this.rescale`

## FeatureModel.hasBayesianSmoothing()
- 位置: L497-499
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.ctrPriorStrength`

## FeatureModel.applyBayesianSmoothing()
- 位置: L511-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 参照: `this.ctrPriorStrength`

## FeatureModel.computeCTRInterestVectors()
- 位置: L550-644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `divideDict()`, `this.supportsCoarseInterests()`, `this.supportsCoarsePrivateInterests()`
- 条件付き依存: `if (this.supportsCoarseInterests())` → `this.hasBayesianSmoothing()`
- 条件付き依存: `if (this.hasBayesianSmoothing())` → `this.applyBayesianSmoothing()`
- 条件付き依存: `if (!(this.hasBayesianSmoothing()))` → `this.applyPostProcessing()`
- 条件付き依存: `if (this.supportsCoarseInterests())` → `this.applyThresholding()`
- 条件付き依存: `if (this.supportsCoarsePrivateInterests())` → `this.hasBayesianSmoothing()`
- 条件付き依存: `if (this.privateFeatures)` → `Object.fromEntries()`
- 条件付き依存: `if (this.privateFeatures)` → `Object.entries(coarsePrivateValues).filter()`
- 条件付き依存: `if (this.privateFeatures)` → `Object.entries()`
- 条件付き依存: `if (this.privateFeatures)` → `this.privateFeatures.includes()`
- 条件付き依存: `if (this.supportsCoarsePrivateInterests())` → `this.privateFeatures.includes()`
- 条件付き依存: `if (this.supportsCoarsePrivateInterests())` → `this.applyThresholding()`
- 条件付き依存: `if (condensePrivateValues)` → `Object.values()`
- 参照: `coarsePrivateValues.timeZoneOffset`, `coarseValues.timeZoneOffset`, `resultObject.coarseInferredInterests`, `resultObject.coarsePrivateInferredInterests`, `this.interestVectorModel`, `this.privateFeatures`

## FeatureModel.computeInterestVectors()
- 位置: L663-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.computeInterestVector()`, `this.supportsCoarseInterests()`, `this.supportsCoarsePrivateInterests()`
- 条件付き依存: `if (this.supportsCoarseInterests())` → `this.computeInterestVector()`
- 条件付き依存: `if (this.supportsCoarsePrivateInterests())` → `this.computeInterestVector()`
- 条件付き依存: `if (condensePrivateValues)` → `Object.values()`
- 参照: `result.coarseInferredInterests`, `result.coarsePrivateInferredInterests`, `result.inferredInterests`
