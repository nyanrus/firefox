# browser/base/content/pageinfo/permissions.js

source: browser/base/content/pageinfo/permissions.js
source-hash: a4a5bd39ce8645e35bef5f87d88516f146942e59
lines: 246

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `EXCLUDE_PERMS.includes()`, `SitePermissions.getPermissionLabel()`, `SitePermissions.listPermissions()`, `SitePermissions.listPermissions() .filter()`, `firstLabel.localeCompare()`

## observe()
- 位置: L31-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic == "perm-changed")` → `aSubject.QueryInterface()`
- 条件付き依存: `if (aTopic == "perm-changed")` → `permission.matches()`
- 条件付き依存: `if (aTopic == "perm-changed")` → `gPermissions.includes()`
- 条件付き依存: `if ( permission.matches(gPermPrincipal, true) && gPermissions.includes(permission.type) )` → `initRow()`
- 参照: `Ci.nsIPermission`, `permission.type`
- XPCOM: [`nsIPermission`](../../../../netwerk/base/nsIPermission.idl.md)

## getExcludedPermissions()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)

## onLoadPermission()
- 位置: L48-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.isSupportedPrincipal()`, `document.getElementById()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `document.getElementById()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `initRow()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `Services.obs.addObserver()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `window.addEventListener()`
- 参照: `hostText.value`, `permTab.hidden`, `uri.displayPrePath`
- XPCOM: `Services.obs`

## onUnloadPermission()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## initRow()
- 位置: L70-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `Services.prefs.prefIsLocked()`, `SitePermissions.getDefault()`, `SitePermissions.getForPrincipal()`, `[SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL].includes()`, `createRow()`, `document.getElementById()`, `setRadioState()`
- 条件付き依存: `if (aPartId == "cookie")` → `Services.perms.testPermissionFromPrincipal()`
- 条件付き依存: `if (state == SitePermissions.UNKNOWN)` → `command.setAttribute()`
- 条件付き依存: `if (state == SitePermissions.UNKNOWN)` → `document.getElementById()`
- 条件付き依存: `if (!(state == SitePermissions.UNKNOWN))` → `command.removeAttribute()`
- 条件付き依存: `if (aPartId == "cookie")` → `setRadioState()`
- 条件付き依存: `if (aPartId == "cookie")` → `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (locked)` → `command.setAttribute()`
- 条件付き依存: `if (state != defaultState)` → `command.removeAttribute()`
- 条件付き依存: `if (!(state != defaultState))` → `command.setAttribute()`
- 条件付き依存: `if ( [SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL].includes(scope) )` → `checkbox.setAttribute()`
- 条件付き依存: `if ( [SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL].includes(scope) )` → `command.setAttribute()`
- 参照: `SitePermissions.SCOPE_GLOBAL`, `SitePermissions.SCOPE_POLICY`, `SitePermissions.UNKNOWN`, `checkbox.checked`, `checkbox.disabled`, `radioGroup.selectedItem`
- XPCOM: `Services.perms` / `Services.policies` / `Services.prefs`

## createRow()
- 位置: L156-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.getAvailableStates()`, `SitePermissions.getMultichoiceStateLabel()`, `SitePermissions.getPermissionLabel()`, `checkbox.addEventListener()`, `checkbox.setAttribute()`, `command.addEventListener()`, `command.setAttribute()`, `controls.appendChild()`, `controls.setAttribute()`, `document.createXULElement()`, `document.getElementById()`, `document.getElementById("pageInfoCommandSet").appendChild()`, `document.getElementById("permList").appendChild()`, `document.l10n.setAttributes()`, `label.setAttribute()`, `onCheckboxClick()`, `onRadioClick()`, `radio.setAttribute()`, `radiogroup.appendChild()`, `radiogroup.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `spacer.setAttribute()`

## onCheckboxClick()
- 位置: L217-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (checkbox.checked)` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (checkbox.checked)` → `command.setAttribute()`
- 条件付き依存: `if (!(checkbox.checked))` → `onRadioClick()`
- 条件付き依存: `if (!(checkbox.checked))` → `command.removeAttribute()`
- 参照: `checkbox.checked`

## onRadioClick()
- 位置: L229-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.setForPrincipal()`, `document.getElementById()`
- 条件付き依存: `if (radioGroup.selectedItem)` → `parseInt()`
- 条件付き依存: `if (radioGroup.selectedItem)` → `radioGroup.selectedItem.id.split()`
- 条件付き依存: `if (!(radioGroup.selectedItem))` → `SitePermissions.getDefault()`
- 参照: `radioGroup.selectedItem`

## setRadioState()
- 位置: L240-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `radio.radioGroup.selectedItem`
