# browser/extensions/webcompat/templates/hide_alerts.js

source: browser/extensions/webcompat/templates/hide_alerts.js
source-hash: 47b90fda3d151a65b1b6ccdd84bfd5f5bb48f4eb
lines: 22

## <module>
- 役割: (未記入)

## window.alert()
- 位置: L10-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alert()`, `msg?.toLowerCase()`
- 条件付き依存: `if (lc)` → `lc.includes()`
