# browser/components/syncedtabs/SyncedTabsDeckStore.sys.mjs

source: browser/components/syncedtabs/SyncedTabsDeckStore.sys.mjs
source-hash: 53d5362b9bfbc1ffa26b4a566434aad91a95d79d
lines: 55

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.assign()`

## SyncedTabsDeckStore()
- 位置: L16-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EventEmitter.call()`
- 参照: `this._panels`

## _change()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._panels.map()`, `this.emit()`
- 参照: `this._selectedPanel`

## selectPanel()
- 位置: L34-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._change()`, `this._panels.includes()`
- 参照: `this._selectedPanel`

## setPanels()
- 位置: L47-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._change()`
- 参照: `this._panels`
