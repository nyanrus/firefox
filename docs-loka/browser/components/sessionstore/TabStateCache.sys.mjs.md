# browser/components/sessionstore/TabStateCache.sys.mjs

source: browser/components/sessionstore/TabStateCache.sys.mjs
source-hash: 4f633ff95222d6733f8dbcde7ff93879e2a85662
lines: 163

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## get()
- 位置: L25-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabStateCacheInternal.get()`

## update()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabStateCacheInternal.update()`

## get()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.get()`

## updatePartialStorageChange()
- 位置: L69-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (!(!change[domain]))` → `Object.keys()`
- 参照: `data.storage`

## updatePartialHistoryChange()
- 位置: L110-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (change.fromIdx != kLastIndex)` → `history.entries.splice()`
- 参照: `Number.MAX_SAFE_INTEGER`, `change.entries`, `change.fromIdx`, `data.history`

## update()
- 位置: L138-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this._data.get()`, `this._data.set()`
- 条件付き依存: `if (key == "storagechange")` → `this.updatePartialStorageChange()`
- 条件付き依存: `if (key == "historychange")` → `this.updatePartialHistoryChange()`
- 参照: `newData.historychange`, `newData.storagechange`
