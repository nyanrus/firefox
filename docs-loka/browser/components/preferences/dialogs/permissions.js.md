# browser/components/preferences/dialogs/permissions.js

source: browser/components/preferences/dialogs/permissions.js
source-hash: 4daf0a79e7df9304336e0661897f9f69a70f926f
lines: 827

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetter()`, `gPermissionManager.onLoad()`, `window.addEventListener()`

## Permission()
- 位置: L65-70
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `principal.origin`, `this.capability`, `this.origin`, `this.principal`, `this.type`

## onLoad()
- 位置: L85-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 参照: `document.mozSubdialogReady`, `window.arguments`

## init()
- 位置: async L103-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `document .getElementById()`, `document .getElementById("permissionsDialogCloseKey") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.setAttributes()`, `document.l10n.translateElements()`, `gPermissionManager.buildPermissionsList()`, `gPermissionManager.onHostInput()`, `gPermissionManager.onHostKeyPress()`, `gPermissionManager.onPermissionKeyPress()`, `gPermissionManager.onPermissionSelect()`, `gPermissionManager.onWindowKeyPress()`, `gPermissionManager.uninit()`, `siteCol.addEventListener()`, `statusCol.addEventListener()`, `this._list.addEventListener()`, `this._loadPermissions()`, `this._urlField.addEventListener()`, `this._urlField.focus()`, `this.addCommandListeners()`, `this.buildPermissionsList()`, `this.onApplyChanges()`, `this.onHostInput()`, `window.addEventListener()`, `window.close()`
- 条件付き依存: `if (!this._isObserving)` → `Services.obs.addObserver()`
- 条件付き依存: `if (this._hideStatusColumn)` → `statusCol.removeAttribute()`
- 条件付き依存: `if (this._hideStatusColumn)` → `siteCol.setAttribute()`
- 参照: `document.documentElement`, `document.getElementById("btnAdd").hidden`, `document.getElementById("btnAllow").hidden`, `document.getElementById("btnBlock").hidden`, `document.getElementById("btnCookieSession").hidden`, `document.getElementById("btnDisableETP").hidden`, `document.getElementById("btnHttpsOnlyOff").hidden`, `document.getElementById("btnHttpsOnlyOffTmp").hidden`, `document.getElementById("urlLabel").hidden`, `event.target`, `l10n.description`, `l10n.window`, `params.addVisible`, `params.allowVisible`, `params.blockVisible`, `params.capabilityFilter`, `params.disableETPVisible`, `params.forcedHTTP`, `params.hideStatusColumn`, `params.permissionType`, `params.prefilledHost`, `params.sessionVisible`, `statusCol.hidden`, `this._btnAdd`, `this._btnAllow`, `this._btnBlock`, `this._btnCookieSession`, `this._btnDisableETP`, `this._btnHttpsOnlyOff`, `this._btnHttpsOnlyOffTmp`, `this._capabilityFilter`, `this._forcedHTTP`, `this._hideStatusColumn`, `this._isObserving`, `this._list`, `this._removeAllButton`, `this._removeButton`, `this._type`, `this._urlField`, `this._urlField.hidden`, `this._urlField.value`
- XPCOM: `Services.obs`

## addCommandListeners()
- 位置: L214-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPermissionManager.addPermission()`, `gPermissionManager.onAllPermissionsDelete()`, `gPermissionManager.onPermissionDelete()`, `window.addEventListener()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`, `event.target.id`
- XPCOM: [`nsICookiePermission`](../../../../netwerk/cookie/nsICookiePermission.idl.md) / [`nsIHttpsOnlyModePermission`](../../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md)

## uninit()
- 位置: L259-264
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._isObserving)` → `Services.obs.removeObserver()`
- 参照: `this._isObserving`
- XPCOM: `Services.obs`

## observe()
- 位置: L266-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subject.QueryInterface()`
- 条件付き依存: `if (data === "cleared")` → `this._permissions.clear()`
- 条件付き依存: `if (data === "cleared")` → `this._permissionsToAdd.clear()`
- 条件付き依存: `if (data === "cleared")` → `this._permissionsToDelete.clear()`
- 条件付き依存: `if (data === "cleared")` → `this._loadPermissions()`
- 条件付き依存: `if (data === "cleared")` → `this.buildPermissionsList()`
- 条件付き依存: `if (data == "added")` → `this._addPermissionToList()`
- 条件付き依存: `if (data == "added")` → `this.buildPermissionsList()`
- 条件付き依存: `if (data == "changed")` → `this._permissions.get()`
- 条件付き依存: `if (p)` → `this._handleCapabilityChange()`
- 条件付き依存: `if (!(p))` → `this._addPermissionToList()`
- 条件付き依存: `if (data == "changed")` → `this.buildPermissionsList()`
- 条件付き依存: `if (data == "deleted")` → `this._removePermissionFromList()`
- 参照: `Ci.nsIPermission`, `p.capability`, `permission.capability`, `permission.principal.origin`, `permission.type`, `this._type`
- XPCOM: [`nsIPermission`](../../../../netwerk/base/nsIPermission.idl.md)

## _handleCapabilityChange()
- 位置: L305-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementsByAttribute()`, `document.l10n.setAttributes()`, `permissionlistitem.querySelector()`, `this._getCapabilityL10nId()`
- 参照: `perm.capability`, `perm.origin`

## _isCapabilitySupported()
- 位置: L316-328
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`, `this._type`
- XPCOM: [`nsICookiePermission`](../../../../netwerk/cookie/nsICookiePermission.idl.md) / [`nsIHttpsOnlyModePermission`](../../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md)

## _getCapabilityL10nId()
- 位置: L330-346
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._type == "https-only-load-insecure")` → `this._getHttpsOnlyCapabilityL10nId()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`, `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`, `this._type`
- XPCOM: [`nsICookiePermission`](../../../../netwerk/cookie/nsICookiePermission.idl.md) / [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md)

## _getHttpsOnlyCapabilityL10nId()
- 位置: L348-357
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsIPermissionManager.ALLOW_ACTION`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md)

## _addPermissionToList()
- 位置: L359-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.isTrailingDotPolicyDuplicate()`, `this._isCapabilitySupported()`, `this._permissions.set()`
- 参照: `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `Services.scriptSecurityManager.DEFAULT_PRIVATE_BROWSING_ID`, `p.origin`, `perm.capability`, `perm.expireType`, `perm.principal`, `perm.principal.privateBrowsingId`, `perm.type`, `this._capabilityFilter`, `this._type`
- XPCOM: `Services.perms` / `Services.scriptSecurityManager`

## _addOrModifyPermission()
- 位置: L392-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._permissions.get()`
- 条件付き依存: `if (!existingPermission)` → `this._permissionsToAdd.set()`
- 条件付き依存: `if (!existingPermission)` → `this._addPermissionToList()`
- 条件付き依存: `if (!existingPermission)` → `this.buildPermissionsList()`
- 条件付き依存: `if (existingPermission.capability != capability)` → `this._permissionsToAdd.set()`
- 条件付き依存: `if (existingPermission.capability != capability)` → `this._handleCapabilityChange()`
- 参照: `existingPermission.capability`, `principal.origin`, `this._type`

## _addNewPrincipalToList()
- 位置: L407-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `list.push()`, `uri.host?.includes()`
- 参照: `list.length`, `list[list.length - 1].origin`
- XPCOM: `Services.scriptSecurityManager`

## addPermission()
- 位置: L416-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.prompt.alert()`, `Services.scriptSecurityManager.createContentPrincipal()`, `document.getElementById()`, `document.l10n .formatValues()`, `document.l10n .formatValues([ { id: "permissions-invalid-uri-title" }, { id: "permissions-invalid-uri-label" }, ]) .then()`, `input_url.startsWith()`, `principal.origin.startsWith()`, `principals.push()`, `textbox.focus()`, `textbox.value.trim()`, `this._addNewPrincipalToList()`, `this._addOrModifyPermission()`, `this._setRemoveButtonState()`, `this.onHostInput()`, `uri.host.includes()`, `uri.schemeIs()`
- 条件付き依存: `if (this._forcedHTTP && uri.schemeIs("https"))` → `uri.mutate().setScheme("http").finalize()`
- 条件付き依存: `if (this._forcedHTTP && uri.schemeIs("https"))` → `uri.mutate().setScheme()`
- 条件付き依存: `if (this._forcedHTTP && uri.schemeIs("https"))` → `uri.mutate()`
- 条件付き依存: `if (!this._forcedHTTP)` → `this._addNewPrincipalToList()`
- 条件付き依存: `if (!this._forcedHTTP)` → `Services.io.newURI()`
- 条件付き依存: `if (this._type == "trackingprotection")` → `principals.map()`
- 参照: `Ci.nsIURL`, `lazy.contentBlockingAllowList.computeContentBlockingAllowListPrincipal`, `textbox.value`, `this._forcedHTTP`, `this._type`
- XPCOM: [`nsIURL`](../../../../netwerk/base/nsIURL.idl.md) / `Services.io` / `Services.prompt` / `Services.scriptSecurityManager`

## _removePermission()
- 位置: L499-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._permissionsToAdd.delete()`, `this._removePermissionFromList()`
- 条件付き依存: `if (!isNewPermission)` → `this._permissionsToDelete.set()`
- 参照: `permission.origin`

## _removePermissionFromList()
- 位置: L511-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementsByAttribute()`, `this._permissions.delete()`
- 条件付き依存: `if (permissionlistitem)` → `permissionlistitem.remove()`

## _loadPermissions()
- 位置: L522-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addPermissionToList()`
- 参照: `Services.perms.all`
- XPCOM: `Services.perms`

## _createPermissionListItem()
- 位置: L529-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `hbox.appendChild()`, `hbox.setAttribute()`, `icon.setAttribute()`, `richlistitem.appendChild()`, `richlistitem.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `this._permissionDisabledByPolicy()`, `this._setSiteIcon()`, `website.setAttribute()`, `website.toggleAttribute()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `document.createXULElement()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `capability.toggleAttribute()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `capability.setAttribute()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `this._getCapabilityL10nId()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `hbox.setAttribute()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `hbox.appendChild()`
- 条件付き依存: `if (!this._hideStatusColumn)` → `row.appendChild()`
- 参照: `permission.capability`, `permission.origin`, `this._hideStatusColumn`

## _setSiteIcon()
- 位置: async L571-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons .getFaviconForPage()`, `lazy.PlacesUtils.favicons .getFaviconForPage(iconURI) .catch()`
- 条件付き依存: `if (favicon)` → `icon.setAttribute()`
- XPCOM: `Services.io`

## onWindowKeyPress()
- 位置: L586-595
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_RETURN && document.activeElement == this._urlField )` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `document.activeElement`, `event.keyCode`, `this._urlField`

## onPermissionKeyPress()
- 位置: L597-610
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && event.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `this.onPermissionDelete()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && event.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `event.preventDefault()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `event.keyCode`, `this._list.selectedItem`

## onHostKeyPress()
- 位置: L612-626
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_RETURN)` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("btnAllow").hidden)` → `document.getElementById("btnAllow").click()`
- 条件付き依存: `if (!document.getElementById("btnAllow").hidden)` → `document.getElementById()`
- 条件付き依存: `if (!(!document.getElementById("btnAllow").hidden))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("btnBlock").hidden)` → `document.getElementById("btnBlock").click()`
- 条件付き依存: `if (!document.getElementById("btnBlock").hidden)` → `document.getElementById()`
- 条件付き依存: `if (!(!document.getElementById("btnBlock").hidden))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("btnHttpsOnlyOff").hidden)` → `document.getElementById("btnHttpsOnlyOff").click()`
- 条件付き依存: `if (!document.getElementById("btnHttpsOnlyOff").hidden)` → `document.getElementById()`
- 条件付き依存: `if (!(!document.getElementById("btnHttpsOnlyOff").hidden))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("btnDisableETP").hidden)` → `document.getElementById("btnDisableETP").click()`
- 条件付き依存: `if (!document.getElementById("btnDisableETP").hidden)` → `document.getElementById()`
- 条件付き依存: `if (!(!document.getElementById("btnDisableETP").hidden))` → `document.getElementById()`
- 条件付き依存: `if (!document.getElementById("btnAdd").hidden)` → `document.getElementById("btnAdd").click()`
- 条件付き依存: `if (!document.getElementById("btnAdd").hidden)` → `document.getElementById()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `document.getElementById("btnAdd").hidden`, `document.getElementById("btnAllow").hidden`, `document.getElementById("btnBlock").hidden`, `document.getElementById("btnDisableETP").hidden`, `document.getElementById("btnHttpsOnlyOff").hidden`, `event.keyCode`

## onHostInput()
- 位置: L628-640
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `siteField.value`, `this._btnAdd.disabled`, `this._btnAdd.hidden`, `this._btnAllow.disabled`, `this._btnAllow.hidden`, `this._btnBlock.disabled`, `this._btnBlock.hidden`, `this._btnCookieSession.disabled`, `this._btnCookieSession.hidden`, `this._btnDisableETP.disabled`, `this._btnDisableETP.hidden`, `this._btnHttpsOnlyOff.disabled`, `this._btnHttpsOnlyOff.hidden`, `this._btnHttpsOnlyOffTmp.disabled`, `this._btnHttpsOnlyOffTmp.hidden`

## _setRemoveButtonState()
- 位置: L642-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._list.querySelectorAll()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE && hasSelection)` → `this._list.selectedItem.getAttribute()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE && hasSelection)` → `this._permissionDisabledByPolicy()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE && hasSelection)` → `this._permissions.get()`
- 参照: `Services.policies.ACTIVE`, `Services.policies.status`, `disabledItems.length`, `this._list`, `this._list.itemCount`, `this._list.selectedIndex`, `this._removeAllButton.disabled`, `this._removeButton.disabled`
- XPCOM: `Services.policies`

## onPermissionDelete()
- 位置: L666-677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `richlistitem.getAttribute()`, `this._permissionDisabledByPolicy()`, `this._permissions.get()`, `this._removePermission()`, `this._setRemoveButtonState()`
- 参照: `this._list.selectedItem`

## onAllPermissionsDelete()
- 位置: L679-688
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._permissionDisabledByPolicy()`, `this._permissions.values()`, `this._removePermission()`, `this._setRemoveButtonState()`

## onPermissionSelect()
- 位置: L690-692
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setRemoveButtonState()`

## onApplyChanges()
- 位置: L694-721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.removeFromPrincipal()`, `this._permissionsToAdd.values()`, `this._permissionsToDelete.values()`, `this.uninit()`
- 条件付き依存: `if ( p.capability == Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION )` → `Services.perms.addFromPrincipal()`
- 条件付き依存: `if (!( p.capability == Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION ))` → `Services.perms.addFromPrincipal()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsIPermissionManager.EXPIRE_SESSION`, `p.capability`, `p.principal`, `p.type`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## buildPermissionsList()
- 位置: L723-744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `document.createDocumentFragment()`, `frag.appendChild()`, `item.remove()`, `this._createPermissionListItem()`, `this._list.appendChild()`, `this._list.querySelectorAll()`, `this._permissions.values()`, `this._setRemoveButtonState()`, `this._sortPermissions()`
- 参照: `this._list`

## _permissionDisabledByPolicy()
- 位置: L746-755
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.getPermissionObject()`
- 参照: `Ci.nsIPermissionManager.EXPIRE_POLICY`, `permission.principal`, `permissionObject?.expireType`, `this._type`
- XPCOM: [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## _sortPermissions()
- 位置: L757-821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `c.removeAttribute()`, `cols.forEach()`, `column.setAttribute()`, `frag.appendChild()`, `frag.querySelectorAll()`, `items.forEach()`, `list.previousElementSibling.querySelectorAll()`
- 条件付き依存: `if (!column)` → `document.querySelector()`
- 条件付き依存: `if (!column)` → `column.getAttribute()`
- 条件付き依存: `if (!(!column))` → `column.getAttribute()`
- 条件付き依存: `if (sortDirection === "descending")` → `items.sort()`
- 条件付き依存: `if (sortDirection === "descending")` → `sortFunc()`
- 条件付き依存: `if (!(sortDirection === "descending"))` → `items.sort()`
- 参照: `Services.intl.Collator`, `column.id`
- XPCOM: `Services.intl`

## sortFunc()
- 位置: L773-778
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.getAttribute()`, `b.getAttribute()`, `comp.compare()`

## sortFunc()
- 位置: L782-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a .querySelector()`, `a .querySelector(".website-capability-value") .getAttribute()`, `b .querySelector()`, `b .querySelector(".website-capability-value") .getAttribute()`
