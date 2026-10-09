# browser/components/syncedtabs/EventEmitter.sys.mjs

source: browser/components/syncedtabs/EventEmitter.sys.mjs
source-hash: ed026dc173317b04c6f0547b437b92ada81b352d
lines: 37

## <module>
- 役割: (未記入)

## EventEmitter()
- 位置: L6-8
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._events`

## on()
- 位置: L11-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._events.has()`
- 条件付き依存: `if (this._events.has(event))` → `this._events.get(event).add()`
- 条件付き依存: `if (this._events.has(event))` → `this._events.get()`
- 条件付き依存: `if (!(this._events.has(event)))` → `this._events.set()`

## off()
- 位置: L18-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._events.get()`, `this._events.get(event).delete()`, `this._events.has()`

## emit()
- 位置: L24-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `listener.apply()`, `this._events.get()`, `this._events.get(event).values()`, `this._events.has()`
