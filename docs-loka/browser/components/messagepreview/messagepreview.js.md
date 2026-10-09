# browser/components/messagepreview/messagepreview.js

source: browser/components/messagepreview/messagepreview.js
source-hash: 95029f0ecade899add6c1d68edea0f15e5d400ce
lines: 47

## <module>
- 役割: (未記入)
- 呼び出し先: `decodeMessageFromUrl()`, `document .querySelector()`, `document .querySelector("#light-switch") .addEventListener()`, `document.addEventListener()`

## fromBinary()
- 位置: L12-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String.fromCharCode()`, `atob()`, `binary.charCodeAt()`, `decodeURIComponent()`
- 参照: `binary.length`, `bytes.buffer`, `bytes.length`

## decodeMessageFromUrl()
- 位置: L21-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.searchParams.has()`
- 条件付き依存: `if (url.searchParams.has("json"))` → `url.searchParams.get()`
- 条件付き依存: `if (url.searchParams.has("json"))` → `fromBinary()`
- 参照: `document.location.href`
