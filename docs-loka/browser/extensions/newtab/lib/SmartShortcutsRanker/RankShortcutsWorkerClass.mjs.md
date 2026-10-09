# browser/extensions/newtab/lib/SmartShortcutsRanker/RankShortcutsWorkerClass.mjs

source: browser/extensions/newtab/lib/SmartShortcutsRanker/RankShortcutsWorkerClass.mjs
source-hash: aff2def399a67532389878f20a36aa5367a2f864
lines: 563

## <module>
- 役割: (未記入)

## interpolateWrappedHistogram()
- 位置: L14-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`
- 参照: `hist.length`

## bayesHist()
- 位置: L37-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `vec.map()`, `vec.reduce()`
- 参照: `pvec.length`, `vec.length`

## getCurrentHourOfDay()
- 位置: L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `now.getHours()`, `now.getMinutes()`, `now.getSeconds()`

## getCurrentDayOfWeek()
- 位置: L54-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `now.getDay()`

## sumNorm()
- 位置: L76-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `vec.reduce()`
- 条件付き依存: `if (!Number.isFinite(vsum) || vsum !== 0)` → `vec.map()`
- 参照: `vec.length`

## normUpdate()
- 位置: L101-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.sqrt()`, `Number.isFinite()`, `vals.map()`
- 参照: `input_normobj.mean`, `input_normobj.var`, `normobj.beta`, `normobj.mean`, `normobj.var`, `vals.length`

## normHistDict()
- 位置: L138-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `Array(t).fill()`, `Object.entries()`, `Object.keys()`, `hist.map()`, `row.map()`
- 参照: `dict[keys[0]].length`, `keys.length`

## computeLinearScore()
- 位置: L176-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`

## processSeasonality()
- 位置: L186-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(b_hists).map()`, `Object.entries(hists).map()`, `Object.entries(sitegiventime).map()`, `Object.fromEntries()`, `bayesHist()`, `guids.map()`, `interpolateWrappedHistogram()`, `normHistDict()`, `sumNorm()`

## buildFrecencyFeatures()
- 位置: async L257-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.exp()`, `Math.floor()`, `Math.log()`, `Object.entries()`, `days_visited.add()`, `time_scores.push()`, `time_scores.reduce()`, `type_scores.push()`, `type_scores.reduce()`
- 参照: `byFeature.freq`, `byFeature.rece`, `byFeature.refre`, `byFeature.unid`, `days_visited.size`, `visits.length`

## _projectByGuid()
- 位置: L312-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `guids.map()`

## _applyVectorFeature()
- 位置: L314-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `guids.forEach()`, `normUpdate()`

## weightedSampleTopSites()
- 位置: async L329-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `Object.keys()`, `computeLinearScore()`, `input.features.includes()`, `input.features.map()`, `input.guid.map()`
- 条件付き依存: `if (input.features.includes(namei))` → `_applyVectorFeature()`
- 条件付き依存: `if (input.features.includes(namei))` → `dictFeatures[namei]()`
- 条件付き依存: `if (input.features.includes("ctr"))` → `input.impressions.map()`
- 条件付き依存: `if (input.features.includes("ctr"))` → `Number.isFinite()`
- 条件付き依存: `if (input.features.includes("ctr"))` → `_applyVectorFeature()`
- 条件付き依存: `if (input.features.includes("thom"))` → `thompsonSampleSort()`
- 条件付き依存: `if (input.features.includes("thom"))` → `input.impressions.map()`
- 条件付き依存: `if (input.features.includes("thom"))` → `Math.max()`
- 条件付き依存: `if (input.features.includes("thom"))` → `input.clicks.map()`
- 条件付き依存: `if (input.features.includes("thom"))` → `normUpdate()`
- 条件付き依存: `if (input.features.includes("thom"))` → `input.guid.forEach()`
- 条件付き依存: `if (input.features.includes("frec"))` → `normUpdate()`
- 条件付き依存: `if (input.features.includes("frec"))` → `input.guid.forEach()`
- 条件付き依存: `if (input.features.includes("hour"))` → `processSeasonality()`
- 条件付き依存: `if (input.features.includes("hour"))` → `getCurrentHourOfDay()`
- 条件付き依存: `if (input.features.includes("hour"))` → `_applyVectorFeature()`
- 条件付き依存: `if (input.features.includes("daily"))` → `processSeasonality()`
- 条件付き依存: `if (input.features.includes("daily"))` → `getCurrentDayOfWeek()`
- 条件付き依存: `if (input.features.includes("daily"))` → `_applyVectorFeature()`
- 条件付き依存: `if (input.features.includes("bias"))` → `input.guid.forEach()`
- 参照: `input.alpha`, `input.beta`, `input.clicks`, `input.daily_seasonality`, `input.frecency`, `input.guid`, `input.hourly_seasonality`, `input.norms`, `input.norms.frec`, `input.norms.thom`, `input.tau`, `input.weights`, `score_map[g].bias`, `score_map[g].final`, `score_map[g].frec`, `score_map[g].thom`, `updated_norms.frec`, `updated_norms.thom`

## bmark()
- 位置: L342-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_projectByGuid()`
- 参照: `input.bmark_scores`, `input.guid`

## open()
- 位置: L343-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_projectByGuid()`
- 参照: `input.guid`, `input.open_scores`

## rece()
- 位置: L344-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_projectByGuid()`
- 参照: `input.guid`, `input.rece_scores`

## freq()
- 位置: L345-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_projectByGuid()`
- 参照: `input.freq_scores`, `input.guid`

## refre()
- 位置: L346-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_projectByGuid()`
- 参照: `input.guid`, `input.refre_scores`

## unid()
- 位置: L347-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_projectByGuid()`
- 参照: `input.guid`, `input.unid_scores`

## clampWeights()
- 位置: L457-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.hypot()`, `Object.values()`
- 条件付き依存: `if (norm > maxNorm)` → `Object.fromEntries()`
- 条件付き依存: `if (norm > maxNorm)` → `Object.entries(weights).map()`
- 条件付き依存: `if (norm > maxNorm)` → `Object.entries()`

## updateWeights()
- 位置: L489-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`, `Object.keys()`
- 条件付き依存: `if ( score_map && score_map[guid] && typeof score_map[guid].final === "number" )` → `Math.exp()`
- 条件付き依存: `if (do_clamp)` → `clampWeights()`
- 参照: `data[guid].clicks`, `data[guid].impressions`, `features.length`, `input.click_bonus`, `input.scores`, `score_map[guid].final`

## RankShortcutsWorker.weightedSampleTopSites()
- 位置: async L550-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `weightedSampleTopSites()`

## RankShortcutsWorker.sumNorm()
- 位置: async L553-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sumNorm()`

## RankShortcutsWorker.updateWeights()
- 位置: async L556-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateWeights()`

## RankShortcutsWorker.buildFrecencyFeatures()
- 位置: async L559-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildFrecencyFeatures()`
