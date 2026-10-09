# browser/modules/PermissionUI.sys.mjs

source: browser/modules/PermissionUI.sys.mjs
source-hash: f998d42c4ca564c43d299cb458d52028c115d7f2
lines: 2829

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## PermissionPrompt.browser()
- 位置: L173-175
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.principal()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.type()
- 位置: L192-194
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.permissionKey()
- 位置: L207-209
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.usePermissionManager()
- 位置: L217-219
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.temporaryPermissionURI()
- 位置: L225-227
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.temporaryPermissionExpireTimeMS()
- 位置: L233-235
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.popupOptions()
- 位置: L246-248
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.postPromptEnabled()
- 位置: L259-261
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.requiresUserInput()
- 位置: L267-269
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.notificationID()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.anchorID()
- 位置: L297-299
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.message()
- 位置: L309-311
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.hintText()
- 位置: L320-322
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.getPrincipalName()
- 位置: L330-336
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `principal.addonPolicy`, `principal.addonPolicy.name`, `principal.hostPort`, `this.principal`

## PermissionPrompt.cancel()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.allow()
- 位置: L354-356
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.promptActions()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.postPromptActions()
- 位置: L402-404
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.onBeforeShow()
- 位置: L416-418
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.onBeforeShowAsync()
- 位置: L431-431
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.onShown()
- 位置: L437-437
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.onAfterShow()
- 位置: L443-443
- 役割: (未記入)
- 触るとき: (未記入)

## PermissionPrompt.prompt()
- 位置: async L457-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popupNotificationActions.push()`, `this.#showNotification()`, `this.onBeforeShowAsync()`
- 条件付き依存: `if (this.usePermissionManager && this.permissionKey)` → `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if (state == lazy.SitePermissions.BLOCK)` → `this.cancel()`
- 条件付き依存: `if ( state == lazy.SitePermissions.ALLOW && !this.request.isRequestDelegatedToUnsafeThirdParty && !this.request.ignoreAllowSitePermission )` → `this.allow()`
- 条件付き依存: `if (this.permissionKey)` → `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if (this.postPromptEnabled)` → `this.onBeforeShowAsync()`
- 条件付き依存: `if (this.postPromptEnabled)` → `this.postPrompt()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `this.cancel()`
- 条件付き依存: `if (!chromeWin.PopupNotifications)` → `this.cancel()`
- 参照: `Ci.nsIStandardURL`, `action.disableSecurityDelay`, `action.dismiss`, `chromeWin.PopupNotifications`, `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `promptAction.accessKey`, `promptAction.action`, `promptAction.dismiss`, `promptAction.label`, `this.browser`, `this.browser.documentGlobal`, `this.permissionKey`, `this.postPromptEnabled`, `this.principal`, `this.principal.URI`, `this.promptActions`, `this.request.hasValidTransientUserGestureActivation`, `this.request.ignoreAllowSitePermission`, `this.request.isRequestDelegatedToUnsafeThirdParty`, `this.requiresUserInput`, `this.temporaryPermissionURI`, `this.usePermissionManager`
- XPCOM: [`nsIStandardURL`](../../netwerk/base/nsIStandardURL.idl.md)

## callback()
- 位置: L542-598
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (promptAction.callback)` → `promptAction.callback()`
- 条件付き依存: `if ( (state && state.checkboxChecked && state.source != "esc-press") || promptAction.scope == lazy.SitePermissions.SCOPE_PERSISTENT )` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if ( (state && state.checkboxChecked && state.source != "esc-press") || promptAction.scope == lazy.SitePermissions.SCOPE_PERSISTENT )` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!( (state && state.checkboxChecked && state.source != "esc-press") || promptAction.scope == lazy.SitePermissions.SCOPE_PERSISTENT ))` → `this.browser.contentPrincipal.equals()`
- 条件付き依存: `if (this.browser.contentPrincipal.equals(this.principal))` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (promptAction.action == lazy.SitePermissions.ALLOW)` → `this.allow()`
- 条件付き依存: `if (!(promptAction.action == lazy.SitePermissions.ALLOW))` → `this.cancel()`
- 条件付き依存: `if (this.permissionKey)` → `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_SESSION`, `lazy.SitePermissions.SCOPE_TEMPORARY`, `promptAction.action`, `promptAction.callback`, `promptAction.scope`, `state.checkboxChecked`, `state.source`, `this.browser`, `this.permissionKey`, `this.principal`, `this.temporaryPermissionExpireTimeMS`, `this.usePermissionManager`

## PermissionPrompt.postPrompt()
- 位置: L617-677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popupNotificationActions.push()`, `this.#showNotification()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `chromeWin.document.getElementById()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `anchor.addEventListener()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `anchor.removeAttribute()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `anchor.setAttribute()`
- 参照: `browser.documentGlobal`, `chromeWin.PopupNotifications`, `chromeWin.gReduceMotion`, `promptAction.accessKey`, `promptAction.label`, `this.anchorID`, `this.browser`, `this.permissionKey`, `this.postPromptActions`, `this.principal`

## callback()
- 位置: L639-659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (promptAction.callback)` → `promptAction.callback()`
- 参照: `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_SESSION`, `promptAction.action`, `promptAction.callback`, `this.permissionKey`

## PermissionPrompt.#showNotification()
- 位置: L679-744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.splice()`, `options.hasOwnProperty()`, `this.onBeforeShow()`
- 条件付き依存: `if (postPrompt || this.onBeforeShow() !== false)` → `chromeWin.PopupNotifications.show()`
- 参照: `actions.length`, `options.dismissed`, `options.displayURI`, `options.eventCallback`, `options.hideClose`, `options.hintText`, `options.persistent`, `this.anchorID`, `this.browser`, `this.browser.documentGlobal`, `this.hintText`, `this.message`, `this.notificationID`, `this.popupOptions`, `this.principal.URI`

## options.eventCallback()
- 位置: L696-723
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "shown" && !postPrompt)` → `this.onShown()`
- 条件付き依存: `if (withoutUserResponse)` → `this.cancel()`
- 条件付き依存: `if (topic == "removed" && !postPrompt)` → `this.onAfterShow()`

## PermissionPromptForRequest.browser()
- 位置: L756-764
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.request.element`, `this.request.window.docShell.chromeEventHandler`

## PermissionPromptForRequest.principal()
- 位置: L766-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `request.getDelegatePrincipal()`, `this.request.QueryInterface()`
- 参照: `Ci.nsIContentPermissionRequest`, `this.type`
- XPCOM: [`nsIContentPermissionRequest`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md)

## PermissionPromptForRequest.cancel()
- 位置: L771-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.request.cancel()`

## PermissionPromptForRequest.allow()
- 位置: L775-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.request.allow()`

## SitePermsAddonInstallRequest.installSitePermAddon()
- 位置: async L794-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.console.logMessage()`, `lazy.AddonManager.installSitePermsAddonFromWebpage()`, `onError()`, `onSuccess()`, `scriptError.initWithWindowID()`, `scriptErrorClass.createInstance()`, `this.getInstallErrorMessage()`
- 参照: `Ci.nsIScriptError`, `err.message`, `this.browser`, `this.browser.browsingContext.currentWindowGlobal.innerWindowId`, `this.permName`, `this.principal`
- XPCOM: [`nsIScriptError`](../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## SitePermsAddonInstallRequest.prompt()
- 位置: L824-841
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.allow()`, `this.cancel()`, `this.installSitePermAddon()`
- 条件付き依存: `if (this.principal.isLoopbackHost || !lazy.sitePermsAddonsProviderEnabled)` → `super.prompt()`
- 参照: `lazy.sitePermsAddonsProviderEnabled`, `this.principal.isLoopbackHost`

## SitePermsAddonInstallRequest.getInstallErrorMessage()
- 位置: L850-852
- 役割: (未記入)
- 触るとき: (未記入)

## GeolocationPermissionPrompt.constructor()
- 位置: L863-874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `request.types.QueryInterface()`, `super()`, `types.queryElementAt()`
- 条件付き依存: `if (perm.options.length)` → `perm.options.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `perm.options.length`, `this.request`, `this.systemPermissionMsg`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## GeolocationPermissionPrompt.type()
- 位置: L876-878
- 役割: (未記入)
- 触るとき: (未記入)

## GeolocationPermissionPrompt.permissionKey()
- 位置: L880-882
- 役割: (未記入)
- 触るとき: (未記入)

## GeolocationPermissionPrompt.popupOptions()
- 位置: L884-912
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (this.request.isRequestDelegatedToUnsafeThirdParty)` → `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `options.secondName`, `this.browser.documentGlobal`, `this.request.isRequestDelegatedToUnsafeThirdParty`, `this.request.principal`
- XPCOM: `Services.urlFormatter`

## GeolocationPermissionPrompt.notificationID()
- 位置: L914-916
- 役割: (未記入)
- 触るとき: (未記入)

## GeolocationPermissionPrompt.anchorID()
- 位置: L918-920
- 役割: (未記入)
- 触るとき: (未記入)

## GeolocationPermissionPrompt.message()
- 位置: L922-940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`, `this.principal.schemeIs()`
- 条件付き依存: `if (this.principal.schemeIs("file"))` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (this.request.isRequestDelegatedToUnsafeThirdParty)` → `lazy.gBrowserBundle.formatStringFromName()`
- 参照: `this.request.isRequestDelegatedToUnsafeThirdParty`

## GeolocationPermissionPrompt.hintText()
- 位置: L942-960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrandBundle.GetStringFromName()`
- 条件付き依存: `if (this.systemPermissionMsg == "sysdlg")` → `lazy.gBrowserBundle.formatStringFromName()`
- 条件付き依存: `if (this.systemPermissionMsg == "syssetting")` → `lazy.gBrowserBundle.formatStringFromName()`
- 参照: `this.systemPermissionMsg`

## GeolocationPermissionPrompt.promptActions()
- 位置: L962-979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## GeolocationPermissionPrompt.#updateGeoSharing()
- 位置: L981-1004
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.updateBrowserSharing()`, `lazy.ContentPrefService2.set()`, `new Date().toString()`
- 参照: `this.browser`, `this.browser.currentURI.host`, `this.browser.documentGlobal.gBrowser`, `this.browser.loadContext`

## GeolocationPermissionPrompt.allow()
- 位置: L1006-1009
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.allow()`, `this.#updateGeoSharing()`

## GeolocationPermissionPrompt.cancel()
- 位置: L1011-1014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.cancel()`, `this.#updateGeoSharing()`

## GeolocationPermissionPrompt.ignoreAllowSitePermission()
- 位置: L1016-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.request.ignoreAllowSitePermission`

## XRPermissionPrompt.constructor()
- 位置: L1029-1032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.request`

## XRPermissionPrompt.type()
- 位置: L1034-1036
- 役割: (未記入)
- 触るとき: (未記入)

## XRPermissionPrompt.permissionKey()
- 位置: L1038-1040
- 役割: (未記入)
- 触るとき: (未記入)

## XRPermissionPrompt.popupOptions()
- 位置: L1042-1063
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## XRPermissionPrompt.notificationID()
- 位置: L1065-1067
- 役割: (未記入)
- 触るとき: (未記入)

## XRPermissionPrompt.anchorID()
- 位置: L1069-1071
- 役割: (未記入)
- 触るとき: (未記入)

## XRPermissionPrompt.message()
- 位置: L1073-1081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`, `this.principal.schemeIs()`
- 条件付き依存: `if (this.principal.schemeIs("file"))` → `lazy.gBrowserBundle.GetStringFromName()`

## XRPermissionPrompt.promptActions()
- 位置: L1083-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## XRPermissionPrompt.#updateXRSharing()
- 位置: L1098-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `devicePermOrigins.add()`, `gBrowser.updateBrowserSharing()`, `this.browser.getDevicePermissionOrigins()`
- 条件付き依存: `if (!state)` → `devicePermOrigins.delete()`
- 参照: `this.browser`, `this.browser.documentGlobal.gBrowser`, `this.principal.origin`

## XRPermissionPrompt.allow()
- 位置: L1113-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.allow()`, `this.#updateXRSharing()`

## XRPermissionPrompt.cancel()
- 位置: L1118-1121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.cancel()`, `this.#updateXRSharing()`

## LNAPermissionPromptBase.constructor()
- 位置: L1136-1139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.request`

## LNAPermissionPromptBase.onBeforeShow()
- 位置: L1141-1148
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof this.request.notifyShown === "function")` → `this.request.notifyShown()`
- 参照: `this.request.notifyShown`

## LNAPermissionPromptBase.onShown()
- 位置: L1150-1152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#startTimeoutTimer()`

## LNAPermissionPromptBase.onAfterShow()
- 位置: L1154-1156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearTimeoutTimer()`

## LNAPermissionPromptBase.cancel()
- 位置: L1158-1160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.cancel()`

## LNAPermissionPromptBase.allow()
- 位置: L1162-1164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.allow()`

## LNAPermissionPromptBase.temporaryPermissionExpireTimeMS()
- 位置: L1166-1169
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.lnaTemporaryPermissionExpireTimeMs`

## LNAPermissionPromptBase.#startTimeoutTimer()
- 位置: L1171-1192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/scripterror;1"].createInstance()`, `Services.console.logMessage()`, `lazy.setTimeout()`, `scriptError.initWithWindowID()`, `this.#clearTimeoutTimer()`, `this.#removePrompt()`, `this.cancel()`
- 参照: `Ci.nsIScriptError`, `Ci.nsIScriptError.warningFlag`, `lazy.lnaPromptTimeoutMs`, `this.#timeoutTimer`, `this.browser.browsingContext.currentWindowGlobal.innerWindowId`
- XPCOM: [`nsIScriptError`](../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## LNAPermissionPromptBase.#removePrompt()
- 位置: L1194-1203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeWin?.PopupNotifications.getNotification()`
- 条件付き依存: `if (notification)` → `chromeWin.PopupNotifications.remove()`
- 参照: `this.browser`, `this.browser?.documentGlobal`, `this.notificationID`

## LNAPermissionPromptBase.#clearTimeoutTimer()
- 位置: L1205-1210
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#timeoutTimer)` → `lazy.clearTimeout()`
- 参照: `this.#timeoutTimer`

## LoopbackNetworkPermissionPrompt.type()
- 位置: L1221-1223
- 役割: (未記入)
- 触るとき: (未記入)

## LoopbackNetworkPermissionPrompt.permissionKey()
- 位置: L1225-1227
- 役割: (未記入)
- 触るとき: (未記入)

## LoopbackNetworkPermissionPrompt.popupOptions()
- 位置: L1229-1252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## LoopbackNetworkPermissionPrompt.notificationID()
- 位置: L1254-1256
- 役割: (未記入)
- 触るとき: (未記入)

## LoopbackNetworkPermissionPrompt.anchorID()
- 位置: L1258-1260
- 役割: (未記入)
- 触るとき: (未記入)

## LoopbackNetworkPermissionPrompt.message()
- 位置: L1262-1267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`

## LoopbackNetworkPermissionPrompt.promptActions()
- 位置: L1269-1286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## DesktopNotificationPermissionPrompt.constructor()
- 位置: L1304-1318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`
- 参照: `this.request`

## DesktopNotificationPermissionPrompt.type()
- 位置: L1320-1322
- 役割: (未記入)
- 触るとき: (未記入)

## DesktopNotificationPermissionPrompt.permissionKey()
- 位置: L1324-1326
- 役割: (未記入)
- 触るとき: (未記入)

## DesktopNotificationPermissionPrompt.#resolveL10n()
- 位置: L1337-1357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.gFluentStrings.formatMessagesSync()`, `message.attributes?.find()`
- 参照: `attr.name`, `message.attributes?.find( attr => attr.name === "accesskey" )?.value`, `message.value`

## DesktopNotificationPermissionPrompt.#applyTreatmentLabels()
- 位置: L1373-1406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `this.#resolveL10n()`
- 参照: `allowAction.accessKey`, `allowAction.label`, `blockAction.accessKey`, `blockAction.label`, `primary.accessKey`, `primary.value`, `secondary.accessKey`, `secondary.value`, `t.primaryCtaAccessKey`, `t.primaryCtaLabel`, `t.primaryCtaLabelL10nId`, `t.secondaryCtaAccessKey`, `t.secondaryCtaLabel`, `t.secondaryCtaLabelL10nId`, `this.#treatment`, `this.browser`

## DesktopNotificationPermissionPrompt.popupOptions()
- 位置: L1408-1420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `this.getPrincipalName()`
- 参照: `this.#treatment?.logoUrl`
- XPCOM: `Services.urlFormatter`

## DesktopNotificationPermissionPrompt.notificationID()
- 位置: L1422-1424
- 役割: (未記入)
- 触るとき: (未記入)

## DesktopNotificationPermissionPrompt.anchorID()
- 位置: L1426-1428
- 役割: (未記入)
- 触るとき: (未記入)

## DesktopNotificationPermissionPrompt.message()
- 位置: L1430-1451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidate?.includes()`, `lazy.gBrowserBundle.formatStringFromName()`, `this.#resolveL10n()`
- 参照: `resolved?.value`, `this.#treatment?.headline`, `this.#treatment?.headlineL10nId`

## DesktopNotificationPermissionPrompt.hintText()
- 位置: L1453-1459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resolveL10n()`
- 参照: `this.#resolveL10n(this.#treatment?.bodyL10nId)?.value`, `this.#treatment?.body`, `this.#treatment?.bodyL10nId`

## DesktopNotificationPermissionPrompt.promptActions()
- 位置: L1461-1513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.push()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SiteCategory.getCategory()`, `lazy.gBrowserBundle.GetStringFromName()`, `this.#applyTreatmentLabels()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_SESSION`, `this.browser`, `this.principal`

## callback()
- 位置: L1472-1478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## callback()
- 位置: L1500-1506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## DesktopNotificationPermissionPrompt.postPromptActions()
- 位置: L1515-1563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.push()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SiteCategory.getCategory()`, `lazy.gBrowserBundle.GetStringFromName()`, `this.#applyTreatmentLabels()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `this.browser`, `this.principal`

## callback()
- 位置: L1525-1531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## callback()
- 位置: L1550-1556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## DesktopNotificationPermissionPrompt.#resolveTreatment()
- 位置: async L1581-1622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feature.getAllVariables()`, `feature.getEnrollmentMetadata()`, `lazy.SiteCategory.getCategory()`, `lazy.evalPermissionPromptTargeting()`
- 条件付き依存: `if (hasContent)` → `this.#resolveLogoUrl()`
- 参照: `lazy.NimbusFeatures`, `lazy.PERMISSION_UI_FEATURE_ID`, `this.#exposureQualified`, `this.#treatment`, `this.principal`, `vars.activationTargeting`, `vars.body`, `vars.bodyL10nId`, `vars.headline`, `vars.headlineL10nId`, `vars.logoUrl`, `vars.primaryCtaLabel`, `vars.primaryCtaLabelL10nId`, `vars.secondaryCtaLabel`, `vars.secondaryCtaLabelL10nId`, `vars.useSiteFavicon`

## DesktopNotificationPermissionPrompt.#resolveLogoUrl()
- 位置: async L1639-1672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.favicons .getFaviconForPage()`, `lazy.PlacesUtils.favicons .getFaviconForPage(pageURI) .catch()`, `lazy.isValidLogoUrl()`, `this.browser.contentPrincipal.equals()`
- 参照: `pageURI.spec`, `this.browser.mIconURL`, `this.principal`, `this.principal.URI`, `vars.logoUrl`, `vars.useSiteFavicon`

## DesktopNotificationPermissionPrompt.onBeforeShowAsync()
- 位置: async L1682-1690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#resolveTreatment()`
- 参照: `this.#exposureQualified`, `this.#treatment`

## DesktopNotificationPermissionPrompt.prompt()
- 位置: L1692-1718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SiteCategory.getCategory()`, `super.prompt()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `Glean.webNotificationPermission.promptBlocked.record()`
- 参照: `this.principal`, `this.request.hasValidTransientUserGestureActivation`, `this.requiresUserInput`

## DesktopNotificationPermissionPrompt.postPrompt()
- 位置: L1720-1732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webNotificationPermission.iconShown.record()`, `lazy.SiteCategory.getCategory()`, `super.postPrompt()`
- 条件付き依存: `if (this.#exposureQualified)` → `lazy.NimbusFeatures[lazy.PERMISSION_UI_FEATURE_ID].recordExposureEvent()`
- 参照: `lazy.NimbusFeatures`, `lazy.PERMISSION_UI_FEATURE_ID`, `this.#exposureQualified`, `this.principal`

## DesktopNotificationPermissionPrompt.onShown()
- 位置: L1734-1768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webNotificationPermission.promptShown.record()`, `lazy.SiteCategory.getCategory()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `Glean.webNotificationPermission.iconClicked.record()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `lazy.SiteCategory.getCategory()`
- 条件付き依存: `if (this.#exposureQualified)` → `lazy.NimbusFeatures[lazy.PERMISSION_UI_FEATURE_ID].recordExposureEvent()`
- 参照: `lazy.NimbusFeatures`, `lazy.PERMISSION_UI_FEATURE_ID`, `this.#exposureQualified`, `this.principal`, `this.request.hasValidTransientUserGestureActivation`, `this.requiresUserInput`

## LocalNetworkPermissionPrompt.type()
- 位置: L1779-1781
- 役割: (未記入)
- 触るとき: (未記入)

## LocalNetworkPermissionPrompt.permissionKey()
- 位置: L1783-1785
- 役割: (未記入)
- 触るとき: (未記入)

## LocalNetworkPermissionPrompt.popupOptions()
- 位置: L1787-1810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## LocalNetworkPermissionPrompt.notificationID()
- 位置: L1812-1814
- 役割: (未記入)
- 触るとき: (未記入)

## LocalNetworkPermissionPrompt.anchorID()
- 位置: L1816-1818
- 役割: (未記入)
- 触るとき: (未記入)

## LocalNetworkPermissionPrompt.message()
- 位置: L1820-1825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`

## LocalNetworkPermissionPrompt.promptActions()
- 位置: L1827-1844
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## PersistentStoragePermissionPrompt.constructor()
- 位置: L1854-1857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.request`

## PersistentStoragePermissionPrompt.type()
- 位置: L1859-1861
- 役割: (未記入)
- 触るとき: (未記入)

## PersistentStoragePermissionPrompt.permissionKey()
- 位置: L1863-1865
- 役割: (未記入)
- 触るとき: (未記入)

## PersistentStoragePermissionPrompt.popupOptions()
- 位置: L1867-1890
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gFluentStrings.formatValueSync()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## PersistentStoragePermissionPrompt.notificationID()
- 位置: L1892-1894
- 役割: (未記入)
- 触るとき: (未記入)

## PersistentStoragePermissionPrompt.anchorID()
- 位置: L1896-1898
- 役割: (未記入)
- 触るとき: (未記入)

## PersistentStoragePermissionPrompt.message()
- 位置: L1900-1905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`

## PersistentStoragePermissionPrompt.promptActions()
- 位置: L1907-1927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## MIDIPermissionPrompt.constructor()
- 位置: L1938-1950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `perm.options.queryElementAt()`, `request.types.QueryInterface()`, `super()`, `types.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `perm.options.length`, `this.isSysexPerm`, `this.permName`, `this.request`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## MIDIPermissionPrompt.type()
- 位置: L1952-1954
- 役割: (未記入)
- 触るとき: (未記入)

## MIDIPermissionPrompt.permissionKey()
- 位置: L1956-1958
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.permName`

## MIDIPermissionPrompt.popupOptions()
- 位置: L1960-1980
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`

## MIDIPermissionPrompt.notificationID()
- 位置: L1982-1984
- 役割: (未記入)
- 触るとき: (未記入)

## MIDIPermissionPrompt.anchorID()
- 位置: L1986-1988
- 役割: (未記入)
- 触るとき: (未記入)

## MIDIPermissionPrompt.message()
- 位置: L1990-2011
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.principal.schemeIs()`
- 条件付き依存: `if (this.isSysexPerm)` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (!(this.isSysexPerm))` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (this.isSysexPerm)` → `lazy.gBrowserBundle.formatStringFromName()`
- 条件付き依存: `if (!(this.isSysexPerm))` → `lazy.gBrowserBundle.formatStringFromName()`
- 参照: `this.isSysexPerm`

## MIDIPermissionPrompt.promptActions()
- 位置: L2013-2030
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## MIDIPermissionPrompt.getInstallErrorMessage()
- 位置: L2037-2039
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `err.message`

## SerialPermissionPrompt.constructor()
- 位置: L2050-2054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.permName`, `this.request`

## SerialPermissionPrompt.type()
- 位置: L2056-2058
- 役割: (未記入)
- 触るとき: (未記入)

## SerialPermissionPrompt.permissionKey()
- 位置: L2060-2062
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.permName`

## SerialPermissionPrompt.popupOptions()
- 位置: L2064-2071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPrincipalName()`

## SerialPermissionPrompt._populateDeviceList()
- 位置: L2073-2127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `document.createXULElement()`, `document.getElementById()`, `i.toString()`, `menuitem.setAttribute()`, `menupopup.appendChild()`, `menupopup.firstChild.remove()`, `options.queryElementAt()`, `perm.options.QueryInterface()`, `ports.push()`, `this._getDeviceDisplayName()`, `this.request.types.QueryInterface()`, `types.queryElementAt()`
- 条件付き依存: `if (!menulist || !menupopup || !noPortsMsg)` → `console.error()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `menulist.hidden`, `menulist.selectedIndex`, `menupopup.firstChild`, `noPortsMsg.hidden`, `notification.browser.ownerDocument`, `notification.mainAction.disabled`, `options.length`, `options.queryElementAt(i, Ci.nsISupportsString).data`, `parsed.__autoselect__`, `ports.length`, `this._autoselect`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## SerialPermissionPrompt._getDeviceDisplayName()
- 位置: L2129-2145
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `vid.toString(16).padStart()`
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `vid.toString()`
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `pid.toString(16).padStart()`
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `pid.toString()`
- 参照: `port.friendlyName`, `port.friendlyName?.length`, `port.path`, `port.usbProductId`, `port.usbVendorId`

## SerialPermissionPrompt.prompt()
- 位置: async L2147-2180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`, `this._showDevicePicker()`, `this.cancel()`, `this.installSitePermAddon()`, `this.principal.schemeIs()`
- 条件付き依存: `if ( this.principal.isLoopbackHost || this.principal.schemeIs("file") || !lazy.sitePermsAddonsProviderEnabled )` → `this._showDevicePicker()`
- 条件付き依存: `if (hasAddon || !lazy.webserialGated)` → `this._showDevicePicker()`
- 参照: `Services.perms.ALLOW_ACTION`, `lazy.sitePermsAddonsProviderEnabled`, `lazy.webserialGated`, `this.permName`, `this.principal`, `this.principal.isLoopbackHost`
- XPCOM: `Services.perms`

## SerialPermissionPrompt._showDevicePicker()
- 位置: L2182-2275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeWin.PopupNotifications.show()`, `console.error()`, `lazy.gBrowserBundle.GetStringFromName()`, `this.cancel()`, `this.getPrincipalName()`
- 参照: `this.anchorID`, `this.browser`, `this.browser.documentGlobal`, `this.message`, `this.notificationID`

## callback()
- 位置: L2190-2204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `selectedIndex.toString()`, `this.allow()`
- 参照: `menulist.selectedIndex`, `this.browser.ownerDocument`

## callback()
- 位置: L2212-2214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancel()`

## SerialPermissionPrompt.eventCallback()
- 位置: L2225-2258
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "showing")` → `promptInstance._populateDeviceList()`
- 条件付き依存: `if (promptInstance._autoselect)` → `lazy.setTimeout()`
- 条件付き依存: `if (promptInstance._autoselect)` → `document.getElementById()`
- 条件付き依存: `if (menulist && menulist.itemCount > 0)` → `selectAction.callback()`
- 条件付き依存: `if (!(menulist && menulist.itemCount > 0))` → `cancelAction.callback()`
- 条件付き依存: `if (promptInstance._autoselect)` → `notification.remove()`
- 条件付き依存: `if (topic === "showing")` → `console.error()`
- 条件付き依存: `if (topic === "removed")` → `promptInstance.cancel()`
- 参照: `menulist.itemCount`, `promptInstance._autoselect`, `promptInstance.browser.ownerDocument`

## SerialPermissionPrompt.notificationID()
- 位置: L2277-2279
- 役割: (未記入)
- 触るとき: (未記入)

## SerialPermissionPrompt.anchorID()
- 位置: L2281-2283
- 役割: (未記入)
- 触るとき: (未記入)

## SerialPermissionPrompt.message()
- 位置: L2285-2296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.principal.schemeIs()`
- 条件付き依存: `if (this.principal.schemeIs("file"))` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (!(this.principal.schemeIs("file")))` → `lazy.gBrowserBundle.formatStringFromName()`

## SerialPermissionPrompt.getInstallErrorMessage()
- 位置: L2303-2305
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `err.message`

## StorageAccessPermissionPrompt.constructor()
- 位置: L2311-2337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `options.queryElementAt()`, `perm.options.QueryInterface()`, `super()`, `this.request.types.QueryInterface()`, `types.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `lazy.SitePermissions.PERM_KEY_DELIMITER`, `options.length`, `options.queryElementAt(0, Ci.nsISupportsString).data`, `options.queryElementAt(1, Ci.nsISupportsString).data`, `this.#permissionKey`, `this.principal.origin`, `this.principal.siteOrigin`, `this.request`, `this.siteOption`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## StorageAccessPermissionPrompt.usePermissionManager()
- 位置: L2339-2341
- 役割: (未記入)
- 触るとき: (未記入)

## StorageAccessPermissionPrompt.type()
- 位置: L2343-2345
- 役割: (未記入)
- 触るとき: (未記入)

## StorageAccessPermissionPrompt.permissionKey()
- 位置: L2347-2350
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#permissionKey`

## StorageAccessPermissionPrompt.temporaryPermissionURI()
- 位置: L2352-2357
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.siteOption)` → `Services.io.newURI()`
- 参照: `this.siteOption`
- XPCOM: `Services.io`

## StorageAccessPermissionPrompt.prettifyHostPort()
- 位置: L2359-2366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hostport.split()`, `lazy.IDNService.convertToDisplayIDN()`

## StorageAccessPermissionPrompt.popupOptions()
- 位置: L2368-2383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.gBrowserBundle.formatStringFromName()`, `this.prettifyHostPort()`
- 参照: `this.principal.hostPort`
- XPCOM: `Services.urlFormatter`

## StorageAccessPermissionPrompt.notificationID()
- 位置: L2385-2387
- 役割: (未記入)
- 触るとき: (未記入)

## StorageAccessPermissionPrompt.anchorID()
- 位置: L2389-2391
- 役割: (未記入)
- 触るとき: (未記入)

## StorageAccessPermissionPrompt.message()
- 位置: L2393-2404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`, `this.prettifyHostPort()`
- 条件付き依存: `if (this.siteOption)` → `this.siteOption.split("://").at()`
- 条件付き依存: `if (this.siteOption)` → `this.siteOption.split()`
- 参照: `this.principal.hostPort`, `this.siteOption`, `this.topLevelPrincipal.host`

## StorageAccessPermissionPrompt.promptActions()
- 位置: L2406-2435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## StorageAccessPermissionPrompt.callback()
- 位置: L2418-2420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.allow()`

## StorageAccessPermissionPrompt.callback()
- 位置: L2430-2432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.cancel()`

## StorageAccessPermissionPrompt.topLevelPrincipal()
- 位置: L2437-2439
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.request.topLevelPrincipal`

## SpeechRecognitionModelDownloadPermissionPrompt.constructor()
- 位置: L2466-2476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `perm.options.queryElementAt()`, `request.types.QueryInterface()`, `super()`, `types.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `perm.options.queryElementAt( 1, Ci.nsISupportsString ).data`, `perm.options.queryElementAt(0, Ci.nsISupportsString).data`, `this.#progressToken`, `this.#sizeMB`, `this.request`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## SpeechRecognitionModelDownloadPermissionPrompt.type()
- 位置: L2478-2480
- 役割: (未記入)
- 触るとき: (未記入)

## SpeechRecognitionModelDownloadPermissionPrompt.popupOptions()
- 位置: L2485-2490
- 役割: (未記入)
- 触るとき: (未記入)

## SpeechRecognitionModelDownloadPermissionPrompt.notificationID()
- 位置: L2492-2494
- 役割: (未記入)
- 触るとき: (未記入)

## SpeechRecognitionModelDownloadPermissionPrompt.anchorID()
- 位置: L2496-2498
- 役割: (未記入)
- 触るとき: (未記入)

## SpeechRecognitionModelDownloadPermissionPrompt.message()
- 位置: L2500-2505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gFluentStrings.formatValueSync()`
- 参照: `this.#sizeMB`

## SpeechRecognitionModelDownloadPermissionPrompt.promptActions()
- 位置: L2507-2544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gFluentStrings .formatMessagesSync()`, `msg.attributes.reduce()`
- 参照: `allowMessage.accesskey`, `allowMessage.label`, `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `notNowMessage.accesskey`, `notNowMessage.label`, `this.#cancelMessage`, `this.#okMessage`

## callback()
- 位置: L2530-2533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#showProgress()`, `this.allow()`

## callback()
- 位置: L2539-2541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancel()`

## SpeechRecognitionModelDownloadPermissionPrompt.allow()
- 位置: L2546-2552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.allow()`
- 参照: `this.#requestSettled`

## SpeechRecognitionModelDownloadPermissionPrompt.cancel()
- 位置: L2554-2560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.cancel()`
- 参照: `this.#requestSettled`

## SpeechRecognitionModelDownloadPermissionPrompt.observe()
- 位置: L2562-2582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.getPropertyAsAString()`, `props.getPropertyAsBool()`, `props.getPropertyAsInt32()`, `props.getPropertyAsInt64()`, `subject.QueryInterface()`, `this.#updateProgress()`
- 参照: `Ci.nsIPropertyBag2`, `this.#progressToken`
- XPCOM: [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## SpeechRecognitionModelDownloadPermissionPrompt.#notificationElement()
- 位置: L2588-2595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser?.documentGlobal?.document.getElementById()`
- 参照: `this.#notification?.browser`

## SpeechRecognitionModelDownloadPermissionPrompt.#showProgress()
- 位置: L2597-2656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Services.obs.addObserver()`, `lazy.gFluentStrings.formatValueSync()`, `popupNotifications.show()`, `this.#applyProgressUI()`, `this.#resetProgressUI()`, `this.#updateProgress()`
- 参照: `allowMessage.accesskey`, `allowMessage.label`, `browser.documentGlobal.PopupNotifications`, `this.#cancelMessage.accesskey`, `this.#cancelMessage.label`, `this.#downloadStartedAt`, `this.#lastSec`, `this.#notification`, `this.#observingProgress`, `this.#renderedPercent`, `this.anchorID`, `this.browser`
- XPCOM: `Services.obs`

## callback()
- 位置: L2607-2607
- 役割: (未記入)
- 触るとき: (未記入)

## callback()
- 位置: L2613-2619
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#observingProgress)` → `Cc["@mozilla.org/ml-modelhub;1"] .getService(Ci.nsIMLModelHub) .cancelDownload()`
- 条件付き依存: `if (this.#observingProgress)` → `Cc["@mozilla.org/ml-modelhub;1"] .getService()`
- 参照: `Ci.nsIMLModelHub`, `this.#observingProgress`, `this.#progressToken`
- XPCOM: [`nsIMLModelHub`](../../toolkit/components/ml/nsIMLModelHub.idl.md) / `@mozilla.org/ml-modelhub;1` → `MLModelHubService` (toolkit/components/ml/components.conf)

## eventCallback()
- 位置: L2637-2646
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "removed")` → `this.#stopObservingProgress()`
- 参照: `this.#notification`

## SpeechRecognitionModelDownloadPermissionPrompt.#applyProgressUI()
- 位置: L2663-2673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationEl.querySelector()`, `notificationEl.toggleAttribute()`, `this.#notificationElement()`
- 参照: `notificationEl.querySelector( "#speech-recognition-model-download-progress-content" ).hidden`

## SpeechRecognitionModelDownloadPermissionPrompt.#setSecondaryLabel()
- 位置: L2680-2689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationEl.setAttribute()`
- 参照: `message.accesskey`, `message.label`, `secondaryAction.accessKey`, `secondaryAction.label`, `this.#notification.secondaryActions`

## SpeechRecognitionModelDownloadPermissionPrompt.#resetProgressUI()
- 位置: L2691-2709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationEl.querySelector()`, `notificationEl.toggleAttribute()`, `this.#notificationElement()`
- 参照: `notificationEl.querySelector( "#speech-recognition-model-download-progress" ).value`, `notificationEl.querySelector( "#speech-recognition-model-download-progress-content" ).hidden`, `notificationEl.querySelector( "#speech-recognition-model-download-progress-status" ).textContent`

## SpeechRecognitionModelDownloadPermissionPrompt.#updateProgress()
- 位置: L2711-2780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `lazy.gFluentStrings.formatValueSync()`, `notificationEl.hasAttribute()`, `notificationEl.querySelector()`, `notificationEl.setAttribute()`, `notificationEl.toggleAttribute()`, `this.#notificationElement()`, `this.#setProgressStatus()`, `this.#setSecondaryLabel()`, `this.#stopObservingProgress()`
- 条件付き依存: `if (!notificationEl.hasAttribute("model-download-in-progress"))` → `this.#applyProgressUI()`
- 条件付き依存: `if (!notificationEl.hasAttribute("model-download-in-progress"))` → `this.#notificationElement()`
- 条件付き依存: `if (progress.ok)` → `lazy.setTimeout()`
- 条件付き依存: `if (progress.ok)` → `this.#notification?.remove()`
- 参照: `progress.done`, `progress.ok`, `progress.progress`, `progressEl.value`, `statusEl.textContent`, `this.#notification.message`, `this.#okMessage`, `this.#renderedPercent`

## SpeechRecognitionModelDownloadPermissionPrompt.#setProgressStatus()
- 位置: L2786-2805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `lazy.DownloadUtils.getDownloadStatus()`
- 参照: `progress.total`, `progress.totalLoaded`, `statusEl.textContent`, `this.#downloadStartedAt`, `this.#lastSec`

## SpeechRecognitionModelDownloadPermissionPrompt.#stopObservingProgress()
- 位置: L2807-2813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.#observingProgress`
- XPCOM: `Services.obs`
