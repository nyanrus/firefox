# browser/extensions/webcompat/injections/js/modify_meta_viewport.js

source: browser/extensions/webcompat/injections/js/modify_meta_viewport.js
source-hash: 4fe0a1e547249c994f549851246f4b24c85c9eec
lines: 79

## <module>
- 役割: (未記入)
- 呼び出し先: `browser.runtime.connect()`, `document.addEventListener()`, `port.onMessage.addListener()`

## check()
- 位置: L12-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(metaViewport.content ?? "") .split()`, `(metaViewport.content ?? "") .split(",") .map()`, `(metaViewport.content ?? "") .split(",") .map(r => r.trim()) .reduce()`, `Array.isArray()`, `Object.entries()`, `Object.entries(content) .map()`, `Object.entries(content) .map(([k, v]) => `${k}=${v}`) .join()`, `document.querySelector()`, `i.trim()`, `item.split()`, `item.split("=").map()`, `metaViewport.setAttribute()`, `only_if_equals.includes()`, `only_if_not_equals.includes()`, `r.trim()`
- 参照: `metaViewport.content`
