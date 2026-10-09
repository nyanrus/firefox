# browser/extensions/webcompat/injections/js/define_window_chrome.js

source: browser/extensions/webcompat/injections/js/define_window_chrome.js
source-hash: 56811ee43ba30aafaea5219dfd2c5588e740d300
lines: 84

## <module>
- 役割: (未記入)

## generateTimeStamp()
- 位置: L8-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`, `Math.random().toString()`, `parseFloat()`, `r.substr()`
- 条件付き依存: `if (base)` → `(base + Math.random() * factor).toString().substr()`
- 条件付き依存: `if (base)` → `(base + Math.random() * factor).toString()`
- 条件付き依存: `if (base)` → `Math.random()`

## getDetails()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)

## getIsInstalled()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)

## installState()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)

## runningState()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.chrome.app.InstallState.NOT_INSTALLED`

## csi()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)

## loadTimes()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
