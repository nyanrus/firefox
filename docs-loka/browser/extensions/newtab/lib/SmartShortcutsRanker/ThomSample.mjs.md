# browser/extensions/newtab/lib/SmartShortcutsRanker/ThomSample.mjs

source: browser/extensions/newtab/lib/SmartShortcutsRanker/ThomSample.mjs
source-hash: 200a099991c8922c9743ea5758e1cd7c87fe2d04
lines: 156

## <module>
- 役割: (未記入)

## sampleNormal()
- 位置: L15-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `Math.log()`, `Math.pow()`, `getRandom()`
- 参照: `Math.random`

## sampleGamma()
- 位置: L57-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.log()`, `Math.pow()`, `Math.sqrt()`, `normalSampler()`, `uniSampler()`
- 参照: `Math.random`

## sortKeysValues()
- 位置: L87-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `paired.map()`, `paired.sort()`, `scores.map()`
- 参照: `a.score`, `b.score`, `p.key`, `p.score`

## sampleBeta()
- 位置: L108-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sampleGamma()`

## thompsonSampleSort()
- 位置: async L126-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `key_array.map()`, `obs_negative.map()`, `obs_positive.map()`, `sampleBeta()`
- 条件付き依存: `if (do_sort)` → `sortKeysValues()`
