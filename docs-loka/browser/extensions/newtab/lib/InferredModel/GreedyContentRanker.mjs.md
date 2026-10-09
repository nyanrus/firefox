# browser/extensions/newtab/lib/InferredModel/GreedyContentRanker.mjs

source: browser/extensions/newtab/lib/InferredModel/GreedyContentRanker.mjs
source-hash: e59eae8610f3b595a1e9f80f56b888233f7d8993
lines: 26

## <module>
- 役割: (未記入)

## scoreItemInferred()
- 位置: async L8-25
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item.section === RANKED_SECTION)` → `Object.keys(item.features) .filter(key => key.startsWith(FEATURE_PREFIX)) .reduce()`
- 条件付き依存: `if (item.section === RANKED_SECTION)` → `Object.keys(item.features) .filter()`
- 条件付き依存: `if (item.section === RANKED_SECTION)` → `Object.keys()`
- 条件付き依存: `if (item.section === RANKED_SECTION)` → `key.startsWith()`
- 条件付き依存: `if (item.section === RANKED_SECTION)` → `key.slice()`
- 参照: `item.features`, `item.item_score`, `item.score`, `item.section`, `item.server_score`, `weights.inferred_norm`, `weights.local`, `weights.server`
