# browser/modules/SitePermissions.sys.mjs

source: browser/modules/SitePermissions.sys.mjs
source-hash: d8be7e764416d2d74aacb70214117e688b05c6a5
lines: 1170

## <module>
- 役割: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.prefs.getBranch()`, `Services.strings.createBundle()`, `SitePermissions.invalidatePermissionList.bind()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## observe()
- 位置: L16-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`, `subject.QueryInterface()`, `subject?.QueryInterface()`
- 条件付き依存: `if (browser?.documentGlobal)` → `browser.dispatchEvent()`
- 参照: `Ci.nsIPermission`, `Ci.nsISupportsPRUint64`, `bc?.embedderElement`, `browser.documentGlobal.CustomEvent`, `browser?.documentGlobal`, `subject.QueryInterface(Ci.nsIPermission).browserId`, `subject?.QueryInterface(Ci.nsISupportsPRUint64).data`
- XPCOM: [`nsIPermission`](../../netwerk/base/nsIPermission.idl.md) / [`nsISupportsPRUint64`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## set()
- 位置: L49-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `browser.addProgressListener()`, `this._stateByBrowser.get()`, `this._stateByBrowser.has()`
- 条件付き依存: `if (!this._stateByBrowser.has(browser))` → `this._stateByBrowser.set()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `browser.contentPrincipal.origin`, `browser.currentURI`
- XPCOM: [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)

## onLocationChange()
- 位置: L74-86
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWebProgress.isTopLevel && (hasLeftPage || isReload))` → `GloballyBlockedPermissions.remove()`
- 条件付き依存: `if (aWebProgress.isTopLevel && (hasLeftPage || isReload))` → `browser.removeProgressListener()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aLocation.prePath`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## remove()
- 位置: L94-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._stateByBrowser.get()`
- 参照: `browser.contentPrincipal.origin`

## getAll()
- 位置: L107-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._stateByBrowser.get()`
- 条件付き依存: `if (entry && entry[origin])` → `Object.keys()`
- 条件付き依存: `if (entry && entry[origin])` → `permissions.push()`
- 条件付き依存: `if (entry && entry[origin])` → `gPermissions.get(id).getDefault()`
- 条件付き依存: `if (entry && entry[origin])` → `gPermissions.get()`
- 参照: `SitePermissions.SCOPE_GLOBAL`, `browser.contentPrincipal.origin`

## copy()
- 位置: L126-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._stateByBrowser.get()`
- 条件付き依存: `if (entry)` → `this._stateByBrowser.set()`

## getAllByPrincipal()
- 位置: L175-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms .getAllForPrincipal()`, `Services.perms .getAllForPrincipal(principal) .filter()`, `SitePermissions.getForPrincipal()`, `gPermissions.get()`, `permissions.map()`, `this.isSupportedPrincipal()`
- 参照: `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `SitePermissions.ALLOW`, `SitePermissions.getForPrincipal( principal, "WebExtensions-unlimitedStorage" ).state`, `entry.disabled`, `entry.id`, `permission.capability`, `permission.expireType`, `permission.type`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`, `this.SCOPE_SESSION`
- XPCOM: `Services.perms`

## getAllForBrowser()
- 位置: L241-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GloballyBlockedPermissions.getAll()`, `Object.values()`, `this.getAllByPrincipal()`, `this.isSupportedPrincipal()`
- 条件付き依存: `if (browserId && this.isSupportedPrincipal(browser.contentPrincipal))` → `Services.perms.getAllForBrowser()`
- 参照: `browser.browserId`, `browser.contentPrincipal`, `perm.capability`, `perm.type`, `permission.id`, `this.SCOPE_TEMPORARY`
- XPCOM: `Services.perms`

## getAllPermissionDetailsForBrowser()
- 位置: L285-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAllForBrowser()`, `this.getAllForBrowser(browser).map()`, `this.getPermissionLabel()`

## isSupportedPrincipal()
- 位置: L303-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isSupportedScheme()`
- 参照: `Ci.nsIPrincipal`, `principal.scheme`
- XPCOM: [`nsIPrincipal`](../../docshell/base/nsIDocShell.idl.md)

## isSupportedScheme()
- 位置: L321-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http", "https", "moz-extension", "file"].includes()`

## listPermissions()
- 位置: L330-335
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._permissionsArray === null)` → `gPermissions.getEnabledPermissions()`
- 参照: `this._permissionsArray`

## isSitePermission()
- 位置: L343-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPermissions.has()`

## invalidatePermissionList()
- 位置: L357-361
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._permissionsArray`

## getAvailableStates()
- 位置: L372-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `this.getDefault()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).states )` → `gPermissions.get()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.BLOCK`, `SitePermissions.PROMPT`, `SitePermissions.UNKNOWN`, `gPermissions.get(permissionID).states`, `this.UNKNOWN`

## getDefault()
- 位置: L406-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `this._defaultPrefBranch.getIntPref()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getDefault )` → `gPermissions.get(permissionID).getDefault()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getDefault )` → `gPermissions.get()`
- 参照: `gPermissions.get(permissionID).getDefault`, `this.UNKNOWN`

## setDefault()
- 位置: L429-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`, `gPermissions.get()`, `gPermissions.has()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).setDefault )` → `gPermissions.get(permissionID).setDefault()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).setDefault )` → `gPermissions.get()`
- 参照: `gPermissions.get(permissionID).setDefault`
- XPCOM: `Services.prefs`

## getForPrincipal()
- 位置: L459-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getDefault()`, `this.isSupportedPrincipal()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `gPermissions.has()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `gPermissions.get()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).exactHostMatch )` → `Services.perms.getPermissionObject()`
- 条件付き依存: `if (!( gPermissions.has(permissionID) && gPermissions.get(permissionID).exactHostMatch ))` → `Services.perms.getPermissionObject()`
- 条件付き依存: `if (browserId)` → `Services.perms.getForBrowser()`
- 参照: `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `SitePermissions.PROMPT`, `browser.browserId`, `browser.contentPrincipal`, `gPermissions.get(permissionID).exactHostMatch`, `permission.capability`, `permission.expireType`, `result.scope`, `result.state`, `tempPerm.capability`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`, `this.SCOPE_SESSION`, `this.SCOPE_TEMPORARY`
- XPCOM: `Services.perms`

## setForPrincipal()
- 位置: L547-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getDefault()`
- 条件付き依存: `if (scope == this.SCOPE_GLOBAL && state == this.BLOCK)` → `GloballyBlockedPermissions.set()`
- 条件付き依存: `if (GloballyBlockedPermissions.set(browser, permissionID))` → `browser.dispatchEvent()`
- 条件付き依存: `if (permissionID != "cookie")` → `this.removeFromPrincipal()`
- 条件付き依存: `if (scope == this.SCOPE_TEMPORARY)` → `Number.isInteger()`
- 条件付き依存: `if (browserId)` → `Services.perms.addFromPrincipalForBrowser()`
- 条件付き依存: `if (!(scope == this.SCOPE_TEMPORARY))` → `this.isSupportedPrincipal()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `Services.perms.addFromPrincipal()`
- 参照: `Services.perms.EXPIRE_NEVER`, `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `SitePermissions.temporaryPermissionExpireTime`, `browser.browserId`, `browser.contentPrincipal`, `browser.documentGlobal.CustomEvent`, `this.ALLOW_COOKIES_FOR_SESSION`, `this.BLOCK`, `this.SCOPE_GLOBAL`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`, `this.SCOPE_SESSION`, `this.SCOPE_TEMPORARY`, `this.UNKNOWN`
- XPCOM: `Services.perms`

## removeFromPrincipal()
- 位置: L635-655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isSupportedPrincipal()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `Services.perms.removeFromPrincipal()`
- 条件付き依存: `if (browserId)` → `Services.perms.removeFromPrincipalForBrowser()`
- 参照: `browser.browserId`, `browser.contentPrincipal`
- XPCOM: `Services.perms`

## clearTemporaryBlockPermissions()
- 位置: L663-671
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (browserId)` → `Services.perms.removeByActionForBrowser()`
- 参照: `Services.perms.DENY_ACTION`, `browser.browserId`
- XPCOM: `Services.perms`

## copyTemporaryPermissions()
- 位置: L684-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GloballyBlockedPermissions.copy()`
- 条件付き依存: `if (srcBrowserId && destBrowserId && srcBrowserId !== destBrowserId)` → `Services.perms.copyBrowserPermissions()`
- 参照: `destBrowser.browserId`
- XPCOM: `Services.perms`

## getPermissionLabel()
- 位置: L703-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `gStringBundle.formatStringFromName()`, `permissionID.split()`
- 参照: `gPermissions.get(id).labelID`, `this.PERM_KEY_DELIMITER`

## getMultichoiceStateLabel()
- 位置: L739-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `gStringBundle.GetStringFromName()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getMultichoiceStateLabel )` → `gPermissions.get(permissionID).getMultichoiceStateLabel()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getMultichoiceStateLabel )` → `gPermissions.get()`
- 参照: `gPermissions.get(permissionID).getMultichoiceStateLabel`, `this.ALLOW`, `this.ALLOW_COOKIES_FOR_SESSION`, `this.BLOCK`, `this.PROMPT`, `this.UNKNOWN`

## getCurrentStateLabel()
- 位置: L779-813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gStringBundle.GetStringFromName()`
- 条件付き依存: `if ( scope && scope != this.SCOPE_PERSISTENT && scope != this.SCOPE_POLICY )` → `gStringBundle.GetStringFromName()`
- 条件付き依存: `if ( scope && scope != this.SCOPE_PERSISTENT && scope != this.SCOPE_POLICY && scope != this.SCOPE_GLOBAL )` → `gStringBundle.GetStringFromName()`
- 参照: `this.ALLOW`, `this.ALLOW_COOKIES_FOR_SESSION`, `this.BLOCK`, `this.PROMPT`, `this.SCOPE_GLOBAL`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`

## _getId()
- 位置: L817-821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `type.split()`
- 参照: `SitePermissions.PERM_KEY_DELIMITER`

## has()
- 位置: L823-825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getId()`
- 参照: `this._permissions`

## get()
- 位置: L827-834
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getId()`
- 参照: `perm.id`, `this._permissions`

## getEnabledPermissions()
- 位置: L836-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(this._permissions).filter()`
- 参照: `this._permissions`, `this._permissions[id].disabled`

## getDefault()
- 位置: L869-881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `Ci.nsIAutoplay.ALLOWED`, `Ci.nsIAutoplay.BLOCKED`, `Ci.nsIAutoplay.BLOCKED_ALL`, `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`
- XPCOM: [`nsIAutoplay`](../../dom/media/autoplay/nsIAutoplay.idl.md) / `Services.prefs`

## setDefault()
- 位置: L882-890
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`
- 参照: `Ci.nsIAutoplay.ALLOWED`, `Ci.nsIAutoplay.BLOCKED`, `Ci.nsIAutoplay.BLOCKED_ALL`, `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`
- XPCOM: [`nsIAutoplay`](../../dom/media/autoplay/nsIAutoplay.idl.md) / `Services.prefs`

## getMultichoiceStateLabel()
- 位置: L897-913
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gStringBundle.GetStringFromName()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`

## getDefault()
- 位置: L922-931
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cookies.getCookieBehavior()`
- 参照: `Ci.nsICookieService.BEHAVIOR_REJECT`, `SitePermissions.ALLOW`, `SitePermissions.BLOCK`
- XPCOM: [`nsICookieService`](../../netwerk/cookie/nsICookieService.idl.md) / `Services.cookies`

## disabled()
- 位置: L946-948
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.localNetworkAccessPermissionsEnabled`

## disabled()
- 位置: L953-955
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.localNetworkAccessPermissionsEnabled`

## disabled()
- 位置: L970-972
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.setSinkIdEnabled`

## labelID()
- 位置: L981-997
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.framebustingInterventionEnabled`, `SitePermissions.popupBlockerEnabled`

## disabled()
- 位置: L999-1004
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.framebustingInterventionEnabled`, `SitePermissions.popupBlockerEnabled`

## getDefault()
- 位置: L1005-1007
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.BLOCK`

## getDefault()
- 位置: L1011-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.UNKNOWN`
- XPCOM: `Services.prefs`

## disabled()
- 位置: L1048-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.sanitizeOnShutdownEnabled`

## getDefault()
- 位置: L1051-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.UNKNOWN`

## getMultichoiceStateLabel()
- 位置: L1055-1067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gStringBundle.GetStringFromName()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.UNKNOWN`

## disabled()
- 位置: L1075-1077
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.resistFingerprinting`

## disabled()
- 位置: L1082-1084
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.midiPermissionEnabled`

## disabled()
- 位置: L1089-1091
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.midiPermissionEnabled`

## disabled()
- 位置: L1096-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.serialPermissionEnabled`

## getDefault()
- 位置: L1103-1105
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.UNKNOWN`
