# browser/extensions/webcompat/injections/js/hide_alerts.js

source: browser/extensions/webcompat/injections/js/hide_alerts.js
source-hash: 21574a0c33887636b1bb7ca0c623a58f2face3ff
lines: 61

## <module>
- 役割: (未記入)

## window.alert()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.postMessage()`
- 参照: `location.origin`

## maybeAlert()
- 位置: L20-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alert()`, `msg?.toLowerCase()`
- 条件付き依存: `if (lc)` → `lc.includes()`
- 条件付き依存: `if (lc.includes(alertToHide))` → `window.hide_alerts_status.blocked.push()`
- 条件付き依存: `if (lc)` → `window.hide_alerts_status.allowed.push()`
