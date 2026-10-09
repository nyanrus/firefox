# browser/extensions/webcompat/shims/google-analytics-legacy.js

source: browser/extensions/webcompat/shims/google-analytics-legacy.js
source-hash: 561b145d54c747963188d18f80877fb1d5ce2c38
lines: 147

## <module>
- 役割: (未記入)

## noopfn()
- 位置: L19-19
- 役割: (未記入)
- 触るとき: (未記入)

## push()
- 位置: L30-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/(^|\.)_link$/.test()`, `Array.isArray()`
- 条件付き依存: `if (typeof a === "function")` → `a()`
- 条件付き依存: `if ( typeof a[0] === "string" && /(^|\.)_link$/.test(a[0]) && typeof a[1] === "string" )` → `window.location.assign()`
- 条件付き依存: `if ( a[0] === "_set" && a[1] === "hitCallback" && typeof a[2] === "function" )` → `a[2]()`

## _getLinkerUrl()
- 位置: L72-72
- 役割: (未記入)
- 触るとき: (未記入)

## _getTracker()
- 位置: L124-124
- 役割: (未記入)
- 触るとき: (未記入)

## _getTrackerByName()
- 位置: L125-125
- 役割: (未記入)
- 触るとき: (未記入)
