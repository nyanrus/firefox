# browser/components/preferences/config/permissions-data.mjs

source: browser/components/preferences/config/permissions-data.mjs
source-hash: e25447b12a375e2e94f33d3f505b7ac6bf586129
lines: 758

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`

## AlertsServiceDND()
- 位置: L16-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/alerts-service;1"] .getService()`, `Cc["@mozilla.org/alerts-service;1"] .getService(Ci.nsIAlertsService) .QueryInterface()`
- 参照: `Ci.nsIAlertsDoNotDisturb`, `Ci.nsIAlertsService`, `alertsService.manualDoNotDisturb`
- XPCOM: [`nsIAlertsDoNotDisturb`](../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / [`nsIAlertsService`](../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / `@mozilla.org/alerts-service;1`

## showPermissionExceptions()
- 位置: L75-98
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dialogType === "site")` → `window.gSubDialog.open()`
- 条件付き依存: `if (!(dialogType === "site"))` → `window.gSubDialog.open()`

## onUserClick()
- 位置: L117-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## onUserClick()
- 位置: L125-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## onUserClick()
- 位置: L133-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## visible()
- 位置: L138-140
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enabledLNA.value`

## onUserClick()
- 位置: L148-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## visible()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enabledLNA.value`

## onUserClick()
- 位置: L161-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## onUserClick()
- 位置: L169-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## visible()
- 位置: L171-173
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `enabledSpeakerControl.value`

## onUserClick()
- 位置: L181-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## onUserClick()
- 位置: L188-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## onUserClick()
- 位置: L197-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## get()
- 位置: L216-224
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.popupPolicy.locked`, `deps.popupPolicy.value`, `deps.redirectPolicy.locked`, `deps.redirectPolicy.value`

## set()
- 位置: L225-232
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.popupPolicy.locked`, `deps.popupPolicy.value`, `deps.redirectPolicy.locked`, `deps.redirectPolicy.value`

## disabled()
- 位置: L233-234
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `popupPolicy.locked`, `redirectPolicy.locked`

## onUserClick()
- 位置: L243-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## disabled()
- 位置: L248-251
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `popupPolicy.locked`, `popupPolicy.value`, `redirectPolicy.locked`, `redirectPolicy.value`

## onUserClick()
- 位置: L263-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showPermissionExceptions()`

## disabled()
- 位置: L268-270
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `warnAddonInstall.locked`, `warnAddonInstall.value`

## get()
- 位置: L274-276
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AlertsServiceDND?.manualDoNotDisturb`

## set()
- 位置: L277-281
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AlertsServiceDND`, `lazy.AlertsServiceDND.manualDoNotDisturb`

## visible()
- 位置: L282-284
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AlertsServiceDND`

## visible()
- 位置: L294-295
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.MOZ_DATA_REPORTING`, `privacySegmentation.value`

## visible()
- 位置: L299-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## getControlConfig()
- 位置: L308-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- 参照: `config.controlAttrs`
- XPCOM: `Services.urlFormatter`

## visible()
- 位置: L324-324
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SelectableProfileService.isEnabled`

## onUserClick()
- 位置: L328-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gMainPane.manageProfiles()`

## visible()
- 位置: L333-338
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.submitHealthReportBox.value`, `lazy.AppConstants.MOZ_DATA_REPORTING`

## getControlConfig()
- 位置: L347-358
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `setting.value`

## visible()
- 位置: L364-364
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.MOZ_DATA_REPORTING`

## get()
- 位置: L365-367
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.submitHealthReportBox.pref.value`

## visible()
- 位置: L376-376
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.MOZ_NORMANDY`

## disabled()
- 位置: L379-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- 参照: `normandyEnabled.value`, `submitHealthReportBox.value`
- XPCOM: `Services.policies`

## get()
- 位置: L391-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- 参照: `normandyEnabled.value`, `submitHealthReportBox.value`
- XPCOM: `Services.policies`

## visible()
- 位置: L421-422
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.MOZ_DATA_REPORTING`, `lazy.AppConstants.MOZ_NORMANDY`

## disabled()
- 位置: L423-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- XPCOM: `Services.policies`

## get()
- 位置: L424-429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- XPCOM: `Services.policies`

## visible()
- 位置: L434-434
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.MOZ_DATA_REPORTING`

## visible()
- 位置: L439-440
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AppConstants.MOZ_CRASHREPORTER`, `lazy.AppConstants.MOZ_DATA_REPORTING`

## setup()
- 位置: L454-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`, `this._originalStateOfDataCollectionPrefs.set()`
- 参照: `dataCollectionPrefDeps[pref].value`

## visible()
- 位置: L461-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Object.keys()`, `profilesEnabledOn.some()`, `this._originalStateOfDataCollectionPrefs.get()`
- 参照: `currentProfile.id`, `dataCollectionPrefDeps.profilesBackupEnabled.value`, `dataCollectionPrefDeps[pref].value`, `lazy.SelectableProfileService`
