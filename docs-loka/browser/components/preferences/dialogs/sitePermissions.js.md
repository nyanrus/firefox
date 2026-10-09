# browser/components/preferences/dialogs/sitePermissions.js

source: browser/components/preferences/dialogs/sitePermissions.js
source-hash: a26eb90f41c23b138c7a55e80ed2637527931476
lines: 777

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetter()`, `gSitePermissionsManager.onLoad()`, `window.addEventListener()`

## _getCapabilityString()
- 位置: L86-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`

## PermissionGroup.constructor()
- 位置: L107-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `perm.principal`, `perm.principal.origin`, `this.origin`, `this.perms`, `this.principal`

## PermissionGroup.addPermission()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.perms.push()`

## PermissionGroup.removePermission()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.perms.filter()`
- 参照: `p.type`, `perm.type`, `this.perms`

## PermissionGroup.capability()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#changedCapability`

## PermissionGroup.capability()
- 位置: L121-126
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#changedCapability`, `this.savedCapability`

## PermissionGroup.revert()
- 位置: L127-129
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#changedCapability`

## PermissionGroup.savedCapability()
- 位置: L130-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `perm.type.split()`
- 参照: `SitePermissions.PERM_KEY_DELIMITER`, `perm.capability`, `perm.type`, `this.perms`

## onLoad()
- 位置: L176-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 参照: `document.mozSubdialogReady`, `window.arguments`

## init()
- 位置: async L181-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("siteCol") .addEventListener()`, `document .getElementById("statusCol") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.pauseObserving()`, `document.l10n.resumeObserving()`, `document.l10n.setAttributes()`, `document.l10n.translateElements()`, `this._list.addEventListener()`, `this._loadPermissions()`, `this._searchBox.addEventListener()`, `this._searchBox.focus()`, `this._watchPermissionPrefChange()`, `this.buildPermissionsList()`, `this.onPermissionKeyPress()`, `this.onPermissionSelect()`, `window.addEventListener()`
- 条件付き依存: `if (!this._isObserving)` → `Services.obs.addObserver()`
- 条件付き依存: `if (l10n.disableLabel)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (l10n.disableDescription)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (params.permissionType == "autoplay-media")` → `this.buildAutoplayMenulist()`
- 参照: `document.documentElement`, `event.target`, `l10n.description`, `l10n.disableDescription`, `l10n.disableLabel`, `l10n.window`, `params.permissionType`, `this._checkbox`, `this._defaultPermissionStatePrefName`, `this._disableExtensionButton`, `this._isObserving`, `this._list`, `this._permissionsDisableDescription`, `this._removeAllButton`, `this._removeButton`, `this._searchBox`, `this._setAutoplayPref`, `this._setAutoplayPref.hidden`, `this._type`
- XPCOM: `Services.obs`

## uninit()
- 位置: L264-272
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._isObserving)` → `Services.obs.removeObserver()`
- 参照: `this._isObserving`, `this._setAutoplayPref`, `this._setAutoplayPref.hidden`
- XPCOM: `Services.obs`

## observe()
- 位置: L274-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PERMISSION_STATES.includes()`, `permission.type.split()`, `subject.QueryInterface()`, `this.buildPermissionsList()`
- 条件付き依存: `if (data === "cleared")` → `this._permissionGroups.clear()`
- 条件付き依存: `if (data === "cleared")` → `this._permissionsToChange.clear()`
- 条件付き依存: `if (data === "cleared")` → `this._permissionsToDelete.clear()`
- 条件付き依存: `if (data === "cleared")` → `this._loadPermissions()`
- 条件付き依存: `if (data === "cleared")` → `this.buildPermissionsList()`
- 条件付き依存: `if (data == "added")` → `this._addPermissionToList()`
- 条件付き依存: `if (!(data == "added"))` → `this._permissionGroups.get()`
- 条件付き依存: `if (data == "changed")` → `group.removePermission()`
- 条件付き依存: `if (data == "changed")` → `group.addPermission()`
- 条件付き依存: `if (data == "deleted")` → `group.removePermission()`
- 条件付き依存: `if (!group.perms.length)` → `this._removePermissionFromList()`
- 参照: `Ci.nsIPermission`, `SitePermissions.PERM_KEY_DELIMITER`, `group.perms.length`, `permission.capability`, `permission.principal.origin`, `this._type`
- XPCOM: [`nsIPermission`](../../../../netwerk/base/nsIPermission.idl.md)

## handleEvent()
- 位置: L322-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onAllPermissionsDelete()`, `this.onApplyChanges()`, `this.onPermissionDelete()`, `this.uninit()`, `window.close()`
- 参照: `event.target.id`, `event.type`

## _handleCheckboxUIUpdates()
- 位置: L346-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getPrefType()`, `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (pref != Services.prefs.PREF_INVALID)` → `Services.prefs.getIntPref()`
- 参照: `Services.prefs.PREF_INVALID`, `SitePermissions.BLOCK`, `this._checkbox.checked`, `this._checkbox.disabled`, `this._checkbox.hidden`, `this._currentDefaultPermissionsState`, `this._defaultPermissionStatePrefName`, `this._permissionsDisableDescription.hidden`
- XPCOM: `Services.prefs`

## _watchPermissionPrefChange()
- 位置: L372-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `this._handleCheckboxUIUpdates()`, `window.addEventListener()`
- 条件付き依存: `if (this._type == "desktop-notification")` → `this._handleWebNotificationsDisable()`
- 条件付き依存: `if (this._type == "desktop-notification")` → `this._disableExtensionButton.addEventListener()`
- 条件付き依存: `if (this._type == "desktop-notification")` → `makeDisableControllingExtension()`
- 参照: `this._defaultPermissionStatePrefName`, `this._type`
- XPCOM: `Services.prefs`

## observer()
- 位置: L387-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleCheckboxUIUpdates()`
- 条件付き依存: `if (this._type == "desktop-notification")` → `this._handleWebNotificationsDisable()`
- 参照: `this._type`

## _handleWebNotificationsDisable()
- 位置: async L405-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (prefLocked)` → `hideControllingExtension()`
- 条件付き依存: `if (!(prefLocked))` → `handleControllingExtension()`
- 参照: `this._checkbox.disabled`
- XPCOM: `Services.prefs`

## _getCapabilityL10nId()
- 位置: L419-450
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( type in sitePermissionsConfig && sitePermissionsConfig[type]._getCapabilityString )` → `sitePermissionsConfig[type]._getCapabilityString()`
- 参照: `Services.perms.ALLOW_ACTION`, `Services.perms.DENY_ACTION`, `Services.perms.PROMPT_ACTION`, `element.tagName`, `sitePermissionsConfig[type]._getCapabilityString`
- XPCOM: `Services.perms`

## _addPermissionToList()
- 位置: L452-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PERMISSION_STATES.includes()`, `SitePermissions.isSupportedPrincipal()`, `lazy.isTrailingDotPolicyDuplicate()`, `perm.type.split()`, `this._permissionGroups.get()`
- 条件付き依存: `if (group)` → `group.addPermission()`
- 条件付き依存: `if (!(group))` → `this._permissionGroups.set()`
- 参照: `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `Services.scriptSecurityManager.DEFAULT_PRIVATE_BROWSING_ID`, `SitePermissions.PERM_KEY_DELIMITER`, `group.origin`, `perm.capability`, `perm.expireType`, `perm.principal`, `perm.principal.origin`, `perm.principal.privateBrowsingId`, `this._type`
- XPCOM: `Services.perms` / `Services.scriptSecurityManager`

## _removePermissionFromList()
- 位置: L477-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementsByAttribute()`, `this._permissionGroups.delete()`, `this._permissionsToChange.delete()`
- 条件付き依存: `if (permissionlistitem)` → `permissionlistitem.remove()`

## _loadPermissions()
- 位置: L489-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addPermissionToList()`
- 参照: `Services.perms.all`
- XPCOM: `Services.perms`

## _createPermissionListItem()
- 位置: L496-546
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.getAvailableStates()`, `SitePermissions.getAvailableStates(this._type).filter()`, `document.createXULElement()`, `richlistitem.appendChild()`, `richlistitem.setAttribute()`, `row.appendChild()`, `states.includes()`
- 条件付き依存: `if (!states.includes(permissionGroup.savedCapability))` → `states.unshift()`
- 条件付き依存: `if (states.length == 1)` → `document.createXULElement()`
- 条件付き依存: `if (states.length == 1)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (states.length == 1)` → `this._getCapabilityL10nId()`
- 条件付き依存: `if (!(states.length == 1))` → `document.createXULElement()`
- 条件付き依存: `if (!(states.length == 1))` → `siteStatus.appendItem()`
- 条件付き依存: `if (!(states.length == 1))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(states.length == 1))` → `this._getCapabilityL10nId()`
- 条件付き依存: `if (!(states.length == 1))` → `siteStatus.addEventListener()`
- 条件付き依存: `if (!(states.length == 1))` → `this.onPermissionChange()`
- 条件付き依存: `if (!(states.length == 1))` → `Number()`
- 参照: `SitePermissions.UNKNOWN`, `permissionGroup.capability`, `permissionGroup.origin`, `permissionGroup.savedCapability`, `siteStatus.className`, `siteStatus.value`, `states.length`, `this._type`, `website.className`, `website.textContent`

## onPermissionKeyPress()
- 位置: L548-561
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && event.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `this.onPermissionDelete()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && event.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `event.preventDefault()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `event.keyCode`, `this._list.selectedItem`

## _setRemoveButtonState()
- 位置: L563-572
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._list`, `this._list.itemCount`, `this._list.selectedIndex`, `this._removeAllButton.disabled`, `this._removeButton.disabled`

## onPermissionDelete()
- 位置: L574-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `richlistitem.getAttribute()`, `this._permissionGroups.get()`, `this._permissionsToDelete.set()`, `this._removePermissionFromList()`, `this._setRemoveButtonState()`
- 参照: `permissionGroup.origin`, `this._list.selectedItem`

## onAllPermissionsDelete()
- 位置: L585-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._permissionGroups.values()`, `this._permissionsToDelete.set()`, `this._removePermissionFromList()`, `this._setRemoveButtonState()`
- 参照: `permissionGroup.origin`

## onPermissionSelect()
- 位置: L594-596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setRemoveButtonState()`

## onPermissionChange()
- 位置: L598-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._permissionGroups.get()`, `this._setRemoveButtonState()`
- 条件付き依存: `if (capability == group.savedCapability)` → `group.revert()`
- 条件付き依存: `if (capability == group.savedCapability)` → `this._permissionsToChange.delete()`
- 条件付き依存: `if (!(capability == group.savedCapability))` → `this._permissionsToChange.set()`
- 参照: `group.capability`, `group.origin`, `group.savedCapability`, `perm.origin`

## onApplyChanges()
- 位置: L615-659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.removeFromPrincipal()`, `SitePermissions.setForPrincipal()`, `this._permissionsToChange.values()`, `this._permissionsToDelete.values()`, `this.uninit()`
- 条件付き依存: `if (this._type === "desktop-notification")` → `this._permissionsToDelete.values()`
- 条件付き依存: `if (this._type === "desktop-notification")` → `Glean.webNotificationPermission.permissionRevokedPreferences.record()`
- 条件付き依存: `if (this._type === "desktop-notification")` → `SiteCategory.getCategory()`
- 条件付き依存: `if (this._checkbox.checked)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (this._currentDefaultPermissionsState == SitePermissions.BLOCK)` → `Services.prefs.setIntPref()`
- 参照: `SitePermissions.BLOCK`, `SitePermissions.UNKNOWN`, `group.capability`, `group.perms`, `group.principal`, `perm.principal`, `perm.type`, `this._checkbox.checked`, `this._currentDefaultPermissionsState`, `this._defaultPermissionStatePrefName`, `this._type`
- XPCOM: `Services.prefs`

## buildPermissionsList()
- 位置: L661-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `document.createDocumentFragment()`, `frag.appendChild()`, `item.remove()`, `permissionGroup.origin.includes()`, `this._createPermissionListItem()`, `this._list.appendChild()`, `this._list.querySelectorAll()`, `this._permissionGroups.values()`, `this._searchBox.value.toLowerCase()`, `this._searchBox.value.toLowerCase().trim()`, `this._setRemoveButtonState()`, `this._sortPermissions()`
- 参照: `this._list`

## buildAutoplayMenulist()
- 位置: async L689-714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `Services.prefs.prefIsLocked()`, `SitePermissions.getAvailableStates()`, `SitePermissions.getDefault()`, `SitePermissions.setDefault()`, `document.createXULElement()`, `document.getElementById()`, `document.getElementById("setAutoplayPref").appendChild()`, `document.l10n.pauseObserving()`, `document.l10n.resumeObserving()`, `document.l10n.setAttributes()`, `document.l10n.translateFragment()`, `menulist.addEventListener()`, `menulist.appendItem()`, `menulist.menupopup.setAttribute()`, `this._getCapabilityL10nId()`
- 参照: `menulist.disabled`, `menulist.value`
- XPCOM: `Services.prefs`

## _sortPermissions()
- 位置: L716-773
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
- 位置: L732-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.getAttribute()`, `b.getAttribute()`, `comp.compare()`

## sortFunc()
- 位置: L741-746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.querySelector()`, `b.querySelector()`, `parseInt()`
- 参照: `a.querySelector(".website-status").value`, `b.querySelector(".website-status").value`
