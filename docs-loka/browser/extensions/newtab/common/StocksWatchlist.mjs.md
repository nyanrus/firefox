# browser/extensions/newtab/common/StocksWatchlist.mjs

source: browser/extensions/newtab/common/StocksWatchlist.mjs
source-hash: 8f07409184fefee6205ac65701297a4f6f76482b
lines: 66

## <module>
- 役割: (未記入)

## normalize()
- 位置: L7-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(symbol ?? "") .trim()`, `String(symbol ?? "") .trim() .toUpperCase()`

## parseWatchlist()
- 位置: L21-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(pref ?? "").split()`, `normalize()`, `out.push()`, `seen.add()`, `seen.has()`
- 参照: `out.length`

## serializeWatchlist()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `symbols.join()`

## addToWatchlist()
- 位置: L50-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalize()`, `symbols.includes()`
- 参照: `symbols.length`

## removeFromWatchlist()
- 位置: L62-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalize()`, `symbols.filter()`
