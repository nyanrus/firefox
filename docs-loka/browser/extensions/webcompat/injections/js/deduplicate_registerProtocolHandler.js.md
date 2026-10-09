# browser/extensions/webcompat/injections/js/deduplicate_registerProtocolHandler.js

source: browser/extensions/webcompat/injections/js/deduplicate_registerProtocolHandler.js
source-hash: 453a531e0b9c1b36a841575d0f9c6e5cf37581a0
lines: 26

## <module>
- 役割: (未記入)
- 呼び出し先: `(window.__webcompat ?? new Set()).add()`, `Object.getPrototypeOf()`

## proto.registerProtocolHandler()
- 位置: L12-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `localStorage.getItem()`, `localStorage.setItem()`, `registerProtocolHandler.call()`
