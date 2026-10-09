# browser/extensions/webcompat/injections/js/bug2021850-aladhan.com-unblock-fetch-requests.js

source: browser/extensions/webcompat/injections/js/bug2021850-aladhan.com-unblock-fetch-requests.js
source-hash: 68a3de98ccbc1818da2a7cad61c5b2e1db45afb2
lines: 25

## <module>
- 役割: (未記入)

## window.fetch()
- 位置: L17-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`
- 条件付き依存: `if (options.headers)` → `console.error()`
- 参照: `options.headers`
