# browser/modules/CanvasPermissionPromptHelper.sys.mjs

source: browser/modules/CanvasPermissionPromptHelper.sys.mjs
source-hash: 0bbbb3d25bf3f3fcf8b8a048546e59a795c9030a
lines: 117

## <module>
- 役割: canvas の権限を求めるポップアップを表示し、選ばれた許可・拒否を権限として保存するモジュール。

## observe()
- 位置: L14-115
- 役割: canvas 権限の確認通知を受け、サイトごとの許可・ブロック選択を出すポップアップを表示する。
- 触るとき: プロンプトの文言、ボタン、既定のチェック状態を変えるとき。プライベートウィンドウでは「覚える」欄を出さない。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `Services.urlFormatter.formatURLPref()`, `gNavigatorBundle.getFormattedString()`, `gNavigatorBundle.getString()`, `window.PopupNotifications.show()`
- 条件付き依存: `if (checkbox.show)` → `gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIDOMWindow`, `aSubject.docShell.chromeEventHandler`, `browser?.documentGlobal`, `checkbox.checked`, `checkbox.label`, `checkbox.show`, `principal.host`, `this._notificationIcon`, `this._permissionsPrompt`, `this._permissionsPromptHideDoorHanger`
- XPCOM: [`nsIDOMWindow`](../../dom/base/nsISlowScriptDebug.idl.md) / `Services.scriptSecurityManager` / `Services.urlFormatter`

## setCanvasPermission()
- 位置: L45-54
- 役割: サイトの canvas 権限を許可または拒否として保存する。覚えるかどうかで有効期間を永続かセッション限りにする。
- 触るとき: 権限の保存期間や対象の扱いを変えるとき。
- 呼び出し先: `Services.perms.addFromPrincipal()`
- 参照: `Ci.nsIPermissionManager.EXPIRE_NEVER`, `Ci.nsIPermissionManager.EXPIRE_SESSION`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## callback()
- 位置: L59-64
- 役割: 「許可」が選ばれた時、覚える欄の状態を使って許可を保存する。
- 触るとき: 許可ボタンの動作を変えるとき。
- 呼び出し先: `setCanvasPermission()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `state.checkboxChecked`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## callback()
- 位置: L71-76
- 役割: 「ブロック」が選ばれた時、覚える欄の状態を使って拒否を保存する。
- 触るとき: ブロックボタンの動作を変えるとき。
- 呼び出し先: `setCanvasPermission()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`, `state.checkboxChecked`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## eventCallback()
- 位置: L96-104
- 役割: 通知が表示された時に、警告文を設定する。
- 触るとき: 表示時の警告文を変えるとき。this.browser を参照しているので、呼び出し元での this の扱いを確かめる(要確認)。
- 条件付き依存: `if (e == "showing")` → `this.browser.ownerDocument.getElementById()`
- 条件付き依存: `if (e == "showing")` → `gBrowserBundle.GetStringFromName()`
- 参照: `this.browser.ownerDocument.getElementById( "canvas-permissions-prompt-warning" ).textContent`
