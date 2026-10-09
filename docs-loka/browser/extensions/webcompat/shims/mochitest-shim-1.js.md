# browser/extensions/webcompat/shims/mochitest-shim-1.js

source: browser/extensions/webcompat/shims/mochitest-shim-1.js
source-hash: ffd848e13dc1ac2019a0d4a39757f3491431d262
lines: 89

## <module>
- 役割: (未記入)

## channel.port1.onmessage()
- 位置: L19-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingMessages.get()`
- 条件付き依存: `if (resolve)` → `pendingMessages.delete()`
- 条件付き依存: `if (resolve)` → `resolve()`
- 参照: `event.data`

## reconnect()
- 位置: L27-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingMessages.values()`, `window.dispatchEvent()`
- 参照: `channel.port2`

## go()
- 位置: async L52-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `cl.add()`, `cl.remove()`, `document.createElement()`, `document.getElementById()`, `document.head.appendChild()`, `sendMessageToAddon()`, `window.shimPromiseResolve()`
- 条件付き依存: `if (window !== top)` → `window.optInPromiseResolve()`
- 参照: `o.classList`, `o.innerText`, `s.onerror`, `s.src`, `window.doingOptIn`

## s.onerror()
- 位置: L73-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.optInPromiseResolve()`
