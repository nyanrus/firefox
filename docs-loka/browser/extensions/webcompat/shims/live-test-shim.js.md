# browser/extensions/webcompat/shims/live-test-shim.js

source: browser/extensions/webcompat/shims/live-test-shim.js
source-hash: 9fca65bbaf3e6501a0a015e619d37604d3a3313c
lines: 84

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
- 位置: async L52-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `cl.add()`, `cl.remove()`, `document.createElement()`, `document.getElementById()`, `document.head.appendChild()`, `sendMessageToAddon()`
- 参照: `o.classList`, `o.innerText`, `s.src`
