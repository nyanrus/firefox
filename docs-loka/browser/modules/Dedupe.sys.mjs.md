# browser/modules/Dedupe.sys.mjs

source: browser/modules/Dedupe.sys.mjs
source-hash: eedca8a0ee35c20d68e4c1db1928f3dacd19d4f4
lines: 37

## <module>
- 役割: (未記入)

## Dedupe.constructor()
- 位置: L6-8
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.createKey`, `this.defaultCreateKey`

## Dedupe.defaultCreateKey()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)

## Dedupe.group()
- 位置: L20-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `globalKeys.add()`, `globalKeys.has()`, `m.values()`, `result.map()`, `result.push()`, `this.createKey()`, `valueMap.forEach()`, `valueMap.has()`
- 条件付き依存: `if (!globalKeys.has(key) && !valueMap.has(key))` → `valueMap.set()`
