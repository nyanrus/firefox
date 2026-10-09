# browser/components/permissions/ContentPermissionPrompt.sys.mjs

source: browser/components/permissions/ContentPermissionPrompt.sys.mjs
source-hash: e71b4c79bb6f7c65509efe135b4a712b46b1dfdc
lines: 148

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `Components.ID()`

## createPermissionPrompt()
- 位置: L41-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PermissionUI.DesktopNotificationPermissionPrompt`, `lazy.PermissionUI.GeolocationPermissionPrompt`, `lazy.PermissionUI.LocalNetworkPermissionPrompt`, `lazy.PermissionUI.LoopbackNetworkPermissionPrompt`, `lazy.PermissionUI.MIDIPermissionPrompt`, `lazy.PermissionUI.PersistentStoragePermissionPrompt`, `lazy.PermissionUI.SerialPermissionPrompt`, `lazy.PermissionUI.SpeechRecognitionModelDownloadPermissionPrompt`, `lazy.PermissionUI.StorageAccessPermissionPrompt`, `lazy.PermissionUI.XRPermissionPrompt`

## ContentPermissionPrompt()
- 位置: L82-82
- 役割: (未記入)
- 触るとき: (未記入)

## prompt()
- 位置: L104-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `combinedIntegration.createPermissionPrompt()`, `console.error()`, `lazy.Integration.contentPermission.getCombined()`, `permissionPrompt.prompt()`, `request.cancel()`, `request.types.QueryInterface()`, `types.queryElementAt()`
- 条件付き依存: `if (request.element && request.element.fxrPermissionPrompt)` → `request.element.fxrPermissionPrompt()`
- 条件付き依存: `if (types.length != 1)` → `Components.Exception()`
- 条件付き依存: `if (!permissionPrompt)` → `Components.Exception()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Cr.NS_ERROR_FAILURE`, `Cr.NS_ERROR_UNEXPECTED`, `request.element`, `request.element.fxrPermissionPrompt`, `types.length`, `types.queryElementAt(0, Ci.nsIContentPermissionType).type`
- XPCOM: [`nsIArray`](../../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md)
