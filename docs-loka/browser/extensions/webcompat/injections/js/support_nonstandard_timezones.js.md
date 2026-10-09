# browser/extensions/webcompat/injections/js/support_nonstandard_timezones.js

source: browser/extensions/webcompat/injections/js/support_nonstandard_timezones.js
source-hash: 2582c0e7ee6ea7cf780e6bd92c4c97634653460d
lines: 65

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Object.getOwnPropertyDescriptor()`, `buildFixed()`, `new Date().toLocaleString()`, `window.__webcompat.add()`

## buildFixed()
- 位置: L13-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `arguments[1]?.timeZone?.toUpperCase()`, `arguments[1]?.timeZone?.toUpperCase().split()`, `arguments[1]?.timeZone?.toUpperCase().split("/").pop()`, `arguments[1]?.timeZone?.toUpperCase().split("/").pop().substr()`, `value.apply()`
- 参照: `arguments[1].timeZone`
