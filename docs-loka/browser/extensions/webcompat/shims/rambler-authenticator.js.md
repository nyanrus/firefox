# browser/extensions/webcompat/shims/rambler-authenticator.js

source: browser/extensions/webcompat/shims/rambler-authenticator.js
source-hash: f2250005a9c38ef6b10200cfc7ebc59ab9ebd5a2
lines: 106

## <module>
- 役割: (未記入)

## channel.port1.onmessage()
- 位置: L37-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingMessages.get()`
- 条件付き依存: `if (resolve)` → `pendingMessages.delete()`
- 条件付き依存: `if (resolve)` → `resolve()`
- 参照: `event.data`

## reconnect()
- 位置: L45-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingMessages.values()`, `window.dispatchEvent()`
- 参照: `channel.port2`

## getProfileInfo()
- 位置: L71-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `successCallback()`

## openAuth()
- 位置: L74-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.head.appendChild()`, `helper.openAuth.apply()`, `helper[fn].apply()`, `s.addEventListener()`, `sendMessageToAddon()`, `sendMessageToAddon("optIn").then()`
- 参照: `s.src`, `window.ramblerIdHelper`

## addLoggedCall()
- 位置: L92-96
- 役割: (未記入)
- 触るとき: (未記入)

## ramblerIdHelper[fn]()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callLog.push()`
