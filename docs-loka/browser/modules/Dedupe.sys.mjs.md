# browser/modules/Dedupe.sys.mjs

source: browser/modules/Dedupe.sys.mjs
source-hash: eedca8a0ee35c20d68e4c1db1928f3dacd19d4f4
lines: 37

## <module>
- 役割: 複数の配列をグループ単位で重複排除する Dedupe クラスを定義する。

## Dedupe.constructor()
- 位置: L6-8
- 役割: createKey を受け取って保持し、省略時は defaultCreateKey を鍵関数に使う。
- 触るとき: 値の同一性を判定する鍵を呼び出し側で差し替えたい(オブジェクトの一部を鍵にする等)ときに見る。
- 参照: `this.createKey`, `this.defaultCreateKey`

## Dedupe.defaultCreateKey()
- 位置: L10-12
- 役割: 値をそのまま鍵として返す恒等関数。
- 触るとき: 文字列や数値の配列を、値の一致だけで重複排除するときの既定の挙動を確かめるときに見る。

## Dedupe.group()
- 位置: L20-35
- 役割: 引数のグループを順に見て、各鍵の最初の値だけを残し、前のグループに出た鍵は除いた配列を返す。
- 触るとき: 複数の候補元を並べ、先に渡したグループを優先して後のグループの重複を落としたいときに見る。
- 呼び出し先: `Array.from()`, `globalKeys.add()`, `globalKeys.has()`, `m.values()`, `result.map()`, `result.push()`, `this.createKey()`, `valueMap.forEach()`, `valueMap.has()`
- 条件付き依存: `if (!globalKeys.has(key) && !valueMap.has(key))` → `valueMap.set()`
