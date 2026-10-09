# browser/fxr/content/permissions.js

source: browser/fxr/content/permissions.js
source-hash: 66c21cdb3f2ef783fde72aea36fccb01ce9f3b81
lines: 146

## <module>
- 役割: (未記入)

## FxrPermissionPromptPrototype.constructor()
- 位置: L20-24
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.request`, `this.responseCallback`, `this.targetBrowser`

## FxrPermissionPromptPrototype.showPrompt()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.defaultDeny()`

## FxrPermissionPromptPrototype.defaultDeny()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleResponse()`

## FxrPermissionPromptPrototype.handleResponse()
- 位置: L37-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.responseCallback()`
- 条件付き依存: `if (allowed)` → `this.allow()`
- 条件付き依存: `if (!(allowed))` → `this.deny()`

## FxrWebRTCPrompt.showPrompt()
- 位置: L50-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.showPrompt()`
- 条件付き依存: `if (typeName !== "Microphone" && typeName !== "Camera")` → `this.defaultDeny()`
- 参照: `this.request.requestTypes`

## FxrWebRTCPrompt.allow()
- 位置: L63-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `this.targetBrowser.sendMessageToActor()`
- 条件付き依存: `if (audioDevices.length)` → `allowedDevices.push()`
- 条件付き依存: `if (videoDevices.length)` → `Services.perms.addFromPrincipal()`
- 条件付き依存: `if (videoDevices.length)` → `allowedDevices.push()`
- 参照: `Services.perms.ALLOW_ACTION`, `Services.perms.EXPIRE_SESSION`, `audioDevices.length`, `audioDevices[0].deviceIndex`, `this.request`, `this.request.callID`, `this.request.origin`, `this.request.windowID`, `videoDevices.length`, `videoDevices[0].deviceIndex`
- XPCOM: `Services.perms` / `Services.scriptSecurityManager`

## FxrWebRTCPrompt.deny()
- 位置: L103-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.targetBrowser.sendMessageToActor()`
- 参照: `this.request.callID`, `this.request.windowID`

## FxrContentPrompt.showPrompt()
- 位置: L117-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.showPrompt()`, `this.request.types.QueryInterface()`, `types.queryElementAt()`
- 条件付き依存: `if (types.length != 1)` → `this.defaultDeny()`
- 条件付き依存: `if (type !== "geolocation")` → `this.defaultDeny()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `types.length`, `types.queryElementAt(0, Ci.nsIContentPermissionType).type`
- XPCOM: [`nsIArray`](../../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md)

## FxrContentPrompt.allow()
- 位置: L138-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.request.allow()`

## FxrContentPrompt.deny()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.request.cancel()`
