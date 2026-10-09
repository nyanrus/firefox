# browser/components/preferences/config/about-firefox.mjs

source: browser/components/preferences/config/about-firefox.mjs
source-hash: c28905c8da122b090b52b540194e4c0a5c56f0c1
lines: 592

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`

## showUpdatesSettings()
- 位置: L32-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 参照: `AppConstants.MOZ_UPDATER`
- XPCOM: `Services.sysinfo`

## showUpdatesInstallation()
- 位置: L41-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `UpdateUtils.appUpdateAutoSettingIsLocked()`
- 参照: `Services.policies`, `gApplicationUpdateService.manualUpdateOnly`, `this.showUpdatesSettings`
- XPCOM: `Services.policies`

## showBackgroundUpdate()
- 位置: L54-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdateUtils.appUpdateSettingIsLocked()`
- 参照: `AppConstants.MOZ_UPDATE_AGENT`, `UpdateUtils.PER_INSTALLATION_PREFS_SUPPORTED`, `this.showUpdatesInstallation`

## showUpdates()
- 位置: L68-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## checkUpdateInProgress()
- 位置: async L72-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/updates/update-manager;1"].getService()`, `Cc["@mozilla.org/updates/update-service;1"].getService()`, `Services.prompt.confirmEx()`, `aus.init()`, `document.l10n.formatValues()`
- 条件付き依存: `if (rv != 1)` → `aus.stopDownload()`
- 条件付き依存: `if (rv != 1)` → `um.cleanupActiveUpdates()`
- 条件付き依存: `if (rv != 1)` → `UpdateListener.clearPendingAndActiveNotifications()`
- 参照: `Ci.nsIApplicationUpdateService`, `Ci.nsIApplicationUpdateService.STATE_IDLE`, `Ci.nsIPrompt.BUTTON_POS_0`, `Ci.nsIPrompt.BUTTON_POS_1`, `Ci.nsIPrompt.BUTTON_POS_1_DEFAULT`, `Ci.nsIPrompt.BUTTON_TITLE_IS_STRING`, `Ci.nsIUpdateManager`, `aus.currentState`
- XPCOM: [`nsIApplicationUpdateService`](../../../../toolkit/mozapps/update/nsIUpdateService.idl.md) / [`nsIPrompt`](../../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIUpdateManager`](../../../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-manager;1` → `UpdateManager` (toolkit/mozapps/update/components.conf) / `@mozilla.org/updates/update-service;1` → `UpdateService` (toolkit/mozapps/update/components.conf) / `Services.prompt`

## reportUpdatePrefWriteError()
- 位置: async L120-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmEx()`, `document.l10n.formatValues()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_TITLE_OK`, `UpdateUtils.configFilePath`
- XPCOM: `Services.prompt`

## visible()
- 位置: L148-148
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UpdatesHelpers.showUpdatesSettings`

## visible()
- 位置: L153-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UpdatesHelpers.showUpdatesSettings`

## setup()
- 位置: L168-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAppUpdater.destroy()`
- 条件付き依存: `if (gAppUpdater)` → `gAppUpdater.destroy()`
- 参照: `AppConstants.MOZ_UPDATER`

## selectPanel()
- 位置: L176-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this._options`, `this._panel`

## get()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._panel`

## getControlConfig()
- 位置: L187-194
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `config.controlAttrs`, `this._options.linkURL`, `this._options.transfer`, `this._options.updateVersion`

## getControlConfig()
- 位置: L200-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/a\d+$/.test()`, `Services.prefs.getDefaultBranch()`, `Services.prefs.getPrefType()`, `Services.strings.createBundle()`, `bundle.GetStringFromName()`, `defaults.getCharPref()`, `defaults.getStringPref()`
- 条件付き依存: `if (/a\d+$/.test(version))` → `buildID.slice()`
- 条件付き依存: `if (relNotesPrefType != Services.prefs.PREF_INVALID)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (distroId && distroAbout)` → `defaults.getCharPref()`
- 参照: `AppConstants.MOZ_APP_VERSION_DISPLAY`, `Services.appinfo.appBuildID`, `Services.appinfo.is64Bit`, `Services.prefs.PREF_INVALID`, `config.controlAttrs`
- XPCOM: `Services.appinfo` / `Services.prefs` / `Services.strings` / `Services.urlFormatter`

## disabled()
- 位置: L273-273
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.disableShowUpdateHistory.locked`

## onUserClick()
- 位置: L274-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdatesHelpers.showUpdates()`

## visible()
- 位置: L279-279
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UpdatesHelpers.showUpdatesInstallation`

## visible()
- 位置: L284-289
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## pendingValue()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._pendingValue`

## pendingValue()
- 位置: L307-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emitChange()`
- 参照: `this._pendingValue`

## get()
- 位置: async L312-319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdateUtils.getAppUpdateAutoEnabled()`
- 参照: `this._pendingValue`

## set()
- 位置: async L324-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdateUtils.setAppUpdateAutoEnabled()`, `UpdatesHelpers.reportUpdatePrefWriteError()`, `console.error()`, `setTimeout()`
- 条件付き依存: `if (!value)` → `UpdatesHelpers.checkUpdateInProgress()`
- 参照: `this._disableTimeOverPromise`, `this._minUpdatePrefDisableTime`, `this.pendingValue`

## setup()
- 位置: L351-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## disabled()
- 位置: async L357-359
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.pendingValue`

## get()
- 位置: async L382-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdateUtils.readUpdateConfigSetting()`
- 参照: `this._pendingValue`, `this._transitionPerformed`, `this._updateRadioSetting.value`, `this.prefName`

## set()
- 位置: async L404-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UpdateUtils.writeUpdateConfigSetting()`, `UpdatesHelpers.reportUpdatePrefWriteError()`, `console.error()`, `this.emitChange()`
- 参照: `this._pendingValue`, `this.prefName`

## visible()
- 位置: async L420-422
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UpdatesHelpers.showBackgroundUpdate`

## disabled()
- 位置: async L424-426
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._pendingValue`

## setup()
- 位置: L428-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `this._updateRadioSetting.off()`, `this._updateRadioSetting.on()`
- 条件付き依存: `if (UpdatesHelpers.showBackgroundUpdate)` → `BackgroundUpdate.ensureExperimentToRolloutTransitionPerformed()`
- 参照: `UpdatesHelpers.showBackgroundUpdate`, `this._transitionPerformed`, `this._updateRadioSetting`, `this.emitChange`
- XPCOM: `Services.obs`

## visible()
- 位置: L452-453
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.NIGHTLY_BUILD`, `UpdatesHelpers.showUpdatesSettings`
