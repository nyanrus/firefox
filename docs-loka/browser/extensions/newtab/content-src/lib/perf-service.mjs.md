# browser/extensions/newtab/content-src/lib/perf-service.mjs

source: browser/extensions/newtab/content-src/lib/perf-service.mjs
source-hash: f1f2d7fda1b5bc714281d8214b4788d977d54401
lines: 108

## <module>
- 役割: (未記入)

## _PerfService()
- 位置: L7-15
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `options.performanceObj`, `this._perf`

## mark()
- 位置: L26-30
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof this._perf.mark === "function")` → `this._perf.mark()`
- 参照: `this._perf.mark`

## getEntriesByName()
- 位置: L40-45
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof this._perf.getEntriesByName === "function")` → `this._perf.getEntriesByName()`
- 参照: `this._perf.getEntriesByName`

## timeOrigin()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._perf.timeOrigin`

## absNow()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._perf.now()`
- 参照: `this.timeOrigin`

## getMostRecentAbsMarkStartByName()
- 位置: L95-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getEntriesByName()`
- 参照: `entries.length`, `mostRecentEntry.startTime`, `this._perf.timeOrigin`
