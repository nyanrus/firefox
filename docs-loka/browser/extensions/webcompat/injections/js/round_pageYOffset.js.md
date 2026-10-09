# browser/extensions/webcompat/injections/js/round_pageYOffset.js

source: browser/extensions/webcompat/injections/js/round_pageYOffset.js
source-hash: 1af02699893b57dd686a9214f4a2f96740a403c3
lines: 19

## <module>
- 役割: (未記入)
- 呼び出し先: `(window.__webcompat ?? new Set()).add()`, `Object.defineProperty()`, `Object.getOwnPropertyDescriptor()`

## desc.get()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `get.call()`
