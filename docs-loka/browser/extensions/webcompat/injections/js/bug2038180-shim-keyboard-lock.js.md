# browser/extensions/webcompat/injections/js/bug2038180-shim-keyboard-lock.js

source: browser/extensions/webcompat/injections/js/bug2038180-shim-keyboard-lock.js
source-hash: d91d1d99f9065333171dbed4ee1bd2624617a994
lines: 171

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Object.getOwnPropertyDescriptor()`

## get()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fullscreenDesc.get.call()`

## get()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fullscreenElementDesc.get.call()`

## animationFrame()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`

## dispatchFakeFullscreenChange()
- 位置: L46-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.dispatchEvent()`

## clearPendingFullscreen()
- 位置: L55-61
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pendingFullscreen?.abortController)` → `pendingFullscreen.abortController.abort()`
- 参照: `pendingFullscreen?.abortController`

## Element.prototype.requestFullscreen()
- 位置: L63-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `animationFrame()`, `clearPendingFullscreen()`, `dispatchFakeFullscreenChange()`, `origRequestFullscreen.call()`
- 条件付き依存: `if ("keyboardLock" in options)` → `origRequestFullscreen.call()`
- 条件付き依存: `if (locked)` → `origRequestFullscreen.call()`
- 参照: `abortController.signal.aborted`, `pendingFullscreen?.element`

## lock()
- 位置: async L121-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (pendingFullscreen)` → `clearPendingFullscreen()`
- 条件付き依存: `if (pendingFullscreen)` → `origRequestFullscreen.call()`
- 条件付き依存: `if (document.fullscreenElement && navigator.userActivation.isActive)` → `origRequestFullscreen.call()`
- 参照: `document.fullscreenElement`, `navigator.userActivation.isActive`

## unlock()
- 位置: L145-158
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( lockStateChanged && document.fullscreenElement && navigator.userActivation.isActive )` → `origRequestFullscreen.call()`
- 参照: `document.fullscreenElement`, `navigator.userActivation.isActive`

## Permissions.prototype.query()
- 位置: L163-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `origPermissionsQuery.call()`
- 条件付き依存: `if (permissionDesc.name === "keyboard-lock")` → `Promise.resolve()`
- 参照: `permissionDesc.name`
