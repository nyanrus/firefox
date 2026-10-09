# nsIContentPermissionType (dom/interfaces/base/nsIContentPermissionPrompt.idl)

source: dom/interfaces/base/nsIContentPermissionPrompt.idl
source-hash: 6863ce1d727ae52711d79a580e0bb6749413076e

- 継承: nsISupports
- 役割: Interface provides the request type and its access.
- 実装: (未記入)
- 使っているJS: [`browser/components/permissions/ContentPermissionPrompt.sys.mjs`](../../../browser/components/permissions/ContentPermissionPrompt.sys.mjs.md), [`browser/fxr/content/permissions.js`](../../../browser/fxr/content/permissions.js.md), [`browser/modules/PermissionUI.sys.mjs`](../../../browser/modules/PermissionUI.sys.mjs.md)

## メソッド / 属性
- `readonly attribute ACString type`: The type of the permission request, such as
- `readonly attribute nsIArray options`: The array of available options.

# nsIContentPermissionRequest (dom/interfaces/base/nsIContentPermissionPrompt.idl)

source: dom/interfaces/base/nsIContentPermissionPrompt.idl
source-hash: 6863ce1d727ae52711d79a580e0bb6749413076e

- 継承: nsISupports
- 役割: Interface allows access to a content to request
- 実装: (未記入)
- 使っているJS: [`browser/fxr/content/fxrui.js`](../../../browser/fxr/content/fxrui.js.md), [`browser/modules/PermissionUI.sys.mjs`](../../../browser/modules/PermissionUI.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIArray types`: The array will include the request types. Elements of this array are
- `readonly attribute nsIPrincipal principal`: (未記入)
- `readonly attribute nsIPrincipal topLevelPrincipal`: (未記入)
- `readonly attribute mozIDOMWindow window`: The window or element that the permission request was
- `readonly attribute Element element`: (未記入)
- `readonly attribute boolean hasValidTransientUserGestureActivation`: (未記入)
- `readonly attribute boolean isRequestDelegatedToUnsafeThirdParty`: See nsIPermissionDelegateHandler.maybeUnsafePermissionDelegate.
- `readonly attribute boolean ignoreAllowSitePermission`: If true, ignore SitePermissions that indicate that this request should be permitted.
- `nsIPrincipal getDelegatePrincipal(ACString aType)`: (未記入)
- `void notifyShown()`: Notify that the permission prompt has been shown to the user.
- `void cancel()`: allow or cancel the request
- `void allow(jsval choices)`: (未記入)

# nsIContentPermissionPrompt (dom/interfaces/base/nsIContentPermissionPrompt.idl)

source: dom/interfaces/base/nsIContentPermissionPrompt.idl
source-hash: 6863ce1d727ae52711d79a580e0bb6749413076e

- 継承: nsISupports
- 役割: Allows to show permission prompts via the UI for different types of requests,
- 実装: (未記入)

## メソッド / 属性
- `void prompt(nsIContentPermissionRequest request)`: Called when a request has been made to access
