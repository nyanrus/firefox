# browser/components/enterprisepolicies/schemas/schema.sys.mjs

source: browser/components/enterprisepolicies/schemas/schema.sys.mjs
source-hash: c6ae1297a3715e3ddf0ca4f6630ebf60090e41d3
lines: 80

## <module>
- 役割: (未記入)
- 呼び出し先: `dereference()`

## refName()
- 位置: L12-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ref.startsWith()`
- 条件付き依存: `if (ref.startsWith(prefix))` → `ref.slice()`
- 参照: `prefix.length`

## dereference()
- 位置: L25-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.entries()`, `dereference()`
- 条件付き依存: `if (Array.isArray(node))` → `node.map()`
- 条件付き依存: `if (Array.isArray(node))` → `dereference()`
- 条件付き依存: `if (typeof node.$ref == "string")` → `refName()`
- 条件付き依存: `if (typeof node.$ref == "string")` → `Object.hasOwn()`
- 条件付き依存: `if (typeof node.$ref == "string")` → `seen.has()`
- 条件付き依存: `if (typeof node.$ref == "string")` → `dereference()`
- 条件付き依存: `if (typeof node.$ref == "string")` → `new Set(seen).add()`
- 条件付き依存: `if (typeof node.$ref == "string")` → `Object.entries()`
- 条件付き依存: `if (key != "$ref")` → `dereference()`
- 参照: `node.$ref`

## modifySchemaForTests()
- 位置: L73-79
- 役割: (未記入)
- 触るとき: (未記入)
