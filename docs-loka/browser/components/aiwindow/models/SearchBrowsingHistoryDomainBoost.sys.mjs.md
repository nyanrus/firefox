# browser/components/aiwindow/models/SearchBrowsingHistoryDomainBoost.sys.mjs

source: browser/components/aiwindow/models/SearchBrowsingHistoryDomainBoost.sys.mjs
source-hash: 717a9816ee62f56c8d46f8c2d3a8ecaa34d79622
lines: 404

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## normalizeQuery()
- 位置: L231-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(s || "") .toLowerCase()`, `(s || "") .toLowerCase() .replace()`, `(s || "") .toLowerCase() .replace(/[^\p{L}\p{N}]+/gu, " ") .replace()`, `(s || "") .toLowerCase() .replace(/[^\p{L}\p{N}]+/gu, " ") .replace(/\s+/g, " ") .trim()`

## matchDomains()
- 位置: L247-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalizeQuery()`, `q.includes()`, `q.trim()`, `tt.trim()`
- 参照: `cat.domains`, `cat.terms`, `categoriesJson.categories`

## buildDomainUrlWhere()
- 位置: L273-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(raw).toLowerCase()`, `clauses.join()`, `clauses.push()`
- 参照: `clauses.length`

## searchByDomains()
- 位置: async L311-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `buildDomainUrlWhere()`, `buildHistoryRow()`, `conn.executeCached()`, `rows.push()`
- 参照: `domains.length`

## mergeDedupe()
- 位置: L368-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyOf()`, `seen.has()`
- 条件付き依存: `if (!seen.has(k))` → `seen.add()`
- 条件付き依存: `if (!seen.has(k))` → `out.push()`
- 参照: `out.length`

## keyOf()
- 位置: L372-372
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `r?.id`, `r?.url`
