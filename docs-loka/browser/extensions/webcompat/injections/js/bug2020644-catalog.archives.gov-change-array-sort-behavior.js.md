# browser/extensions/webcompat/injections/js/bug2020644-catalog.archives.gov-change-array-sort-behavior.js

source: browser/extensions/webcompat/injections/js/bug2020644-catalog.archives.gov-change-array-sort-behavior.js
source-hash: 2001221b200341324063b21640302679303a2052
lines: 34

## <module>
- 役割: (未記入)
- 呼び出し先: `console.info()`

## prototype.sort()
- 位置: L24-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(arguments[0]).includes()`, `oldSort.apply()`
- 条件付き依存: `if ( typeof arguments[0] == "function" && String(arguments[0]).includes(".objectType)?-1:1") )` → `oldSort.call()`
