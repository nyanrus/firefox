# browser/extensions/webcompat/injections/js/increase_performance_now_precision.js

source: browser/extensions/webcompat/injections/js/increase_performance_now_precision.js
source-hash: 4fe4ba5758f4d9679db9d9d5a3269e0c99fd80ff
lines: 32

## <module>
- 役割: (未記入)
- 呼び出し先: `(function () { return [performance.now(), performance.now()][1].toString().includes("."); })()`, `[performance.now(), performance.now()][1].toString()`, `[performance.now(), performance.now()][1].toString().includes()`, `performance.now()`

## perf.now()
- 位置: L17-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `now.call()`
