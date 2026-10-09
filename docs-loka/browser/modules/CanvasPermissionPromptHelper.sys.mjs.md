# browser/modules/CanvasPermissionPromptHelper.sys.mjs

source: browser/modules/CanvasPermissionPromptHelper.sys.mjs
source-hash: 0bbbb3d25bf3f3fcf8b8a048546e59a795c9030a
lines: 117

## <module>
- 役割: (未記入)

## observe()
- 位置: L14-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `Services.urlFormatter.formatURLPref()`, `gNavigatorBundle.getFormattedString()`, `gNavigatorBundle.getString()`, `window.PopupNotifications.show()`
- 条件付き依存: `if (checkbox.show)` → `gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIDOMWindow`, `aSubject.docShell.chromeEventHandler`, `browser?.documentGlobal`, `checkbox.checked`, `checkbox.label`, `checkbox.show`, `principal.host`, `this._notificationIcon`, `this._permissionsPrompt`, `this._permissionsPromptHideDoorHanger`
- XPCOM: [`nsIDOMWindow`](../../dom/base/nsISlowScriptDebug.idl.md) / `Services.scriptSecurityManager` / `Services.urlFormatter`

## setCanvasPermission()
- 位置: L45-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.addFromPrincipal()`
- 参照: `Ci.nsIPermissionManager.EXPIRE_NEVER`, `Ci.nsIPermissionManager.EXPIRE_SESSION`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## callback()
- 位置: L59-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setCanvasPermission()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `state.checkboxChecked`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## callback()
- 位置: L71-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setCanvasPermission()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`, `state.checkboxChecked`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## eventCallback()
- 位置: L96-104
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e == "showing")` → `this.browser.ownerDocument.getElementById()`
- 条件付き依存: `if (e == "showing")` → `gBrowserBundle.GetStringFromName()`
- 参照: `this.browser.ownerDocument.getElementById( "canvas-permissions-prompt-warning" ).textContent`
