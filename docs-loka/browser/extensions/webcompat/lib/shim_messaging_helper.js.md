# browser/extensions/webcompat/lib/shim_messaging_helper.js

source: browser/extensions/webcompat/lib/shim_messaging_helper.js
source-hash: ee109713a5b5fc4e24ffde58fe199a23a63985b0
lines: 66

## <module>
- 役割: (未記入)

## handleMessage()
- 位置: async L27-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port.postMessage()`, `window.Shims.get()`
- 条件付き依存: `if (origin === location.origin)` → `needsShimHelpers?.includes()`
- 条件付き依存: `if (needsShimHelpers?.includes(message))` → `browser.runtime.sendMessage()`
- 参照: `location.origin`

## port.onmessage()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleMessage()`
- 参照: `data.message`, `data.messageId`
