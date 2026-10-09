# browser/extensions/webcompat/templates/modify_meta_viewport.js

source: browser/extensions/webcompat/templates/modify_meta_viewport.js
source-hash: 4a35f6806dacdae100d464f75e5ec5bfb3acdd53
lines: 76

## <module>
- 役割: (未記入)
- 呼び出し先: `document.addEventListener()`

## check()
- 位置: L10-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(metaViewport.content ?? "") .split()`, `(metaViewport.content ?? "") .split(",") .map()`, `(metaViewport.content ?? "") .split(",") .map(r => r.trim()) .reduce()`, `Array.isArray()`, `Object.entries()`, `Object.entries(content) .map()`, `Object.entries(content) .map(([k, v]) => `${k}=${v}`) .join()`, `document.querySelector()`, `i.trim()`, `item.split()`, `item.split("=").map()`, `metaViewport.setAttribute()`, `only_if_equals.includes()`, `only_if_not_equals.includes()`, `r.trim()`
- 参照: `metaViewport.content`
