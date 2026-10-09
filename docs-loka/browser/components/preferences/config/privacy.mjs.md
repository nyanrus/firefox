# browser/components/preferences/config/privacy.mjs

source: browser/components/preferences/config/privacy.mjs
source-hash: 861d8072279985811ef01ac4523795c3c379e7f5
lines: 4197

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Ci.nsICookieService.BEHAVIOR_ACCEPT.toString()`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN.toString()`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN.toString()`, `Ci.nsICookieService.BEHAVIOR_REJECT.toString()`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN.toString()`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER.toString()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`, `window.addEventListener()`

## gParentalControlsService()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/parental-controls-service;1"].getService()`
- 参照: `Ci.nsIParentalControlsService`
- XPCOM: [`nsIParentalControlsService`](../../../../toolkit/components/parentalcontrols/nsIParentalControlsService.idl.md) / `@mozilla.org/parental-controls-service;1`

## isPackagedApp()
- 位置: L48-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- XPCOM: `Services.sysinfo`

## PrivacySettingHelpers.showHttpsOnlyModeExceptions()
- 位置: L60-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## PrivacySettingHelpers._isCustomCleaningPrefPresent()
- 位置: L79-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `SANITIZE_ON_SHUTDOWN_PREFS_ONLY_V2.some()`
- 参照: `Preferences.get(pref).value`

## PrivacySettingHelpers.resetCleaningPrefs()
- 位置: L88-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `SANITIZE_ON_SHUTDOWN_PREFS_ONLY_V2.forEach()`
- 参照: `Preferences.get(pref).value`

## PrivacySettingHelpers.clearPrivateDataNow()
- 位置: L98-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `gSubDialog.open()`
- 参照: `ts.value`

## closingCallback()
- 位置: L107-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `ts.value`
- XPCOM: `Services.obs`

## PrivacySettingHelpers.showCertificates()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## PrivacySettingHelpers.showSecurityDevices()
- 位置: L127-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## PrivacySettingHelpers.showDoHExceptions()
- 位置: L131-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## PrivacySettingHelpers.reloadAllOtherTabs()
- 位置: L143-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `document.querySelectorAll()`, `lazy.BrowserWindowTracker.orderedWindows.forEach()`
- 条件付き依存: `if (tab.pinned || tab.selected)` → `otherGBrowser.reloadTab()`
- 条件付き依存: `if (!(tab.pinned || tab.selected))` → `otherGBrowser.discardBrowser()`
- 参照: `Preferences.getSetting("reloadTabsHint").value`, `notification.hidden`, `otherGBrowser.tabs`, `tab.pinned`, `tab.selected`, `win.gBrowser`, `window.browsingContext.topChromeWindow.gBrowser.selectedTab`

## PrivacySettingHelpers.maybeNotifyUserToReload()
- 位置: L169-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`
- 条件付き依存: `if (shouldShow)` → `document.querySelectorAll()`
- 参照: `Preferences.getSetting("reloadTabsHint").value`, `lazy.BrowserWindowTracker.orderedWindows.length`, `notification.hidden`, `tabbrowser.tabs.length`, `window.browsingContext.topChromeWindow.gBrowser`

## PrivacySettingHelpers.updateCryptominingLists()
- 位置: L191-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `[ "urlclassifier.features.cryptomining.blacklistTables", "urlclassifier.features.cryptomining.whitelistTables", ] .map()`, `lazy.listManager.forceUpdates()`
- XPCOM: `Services.prefs`

## PrivacySettingHelpers.updateFingerprintingLists()
- 位置: L206-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `lazy.listManager.forceUpdates()`
- XPCOM: `Services.prefs`

## PrivacySettingHelpers.onBaselineAllowListSettingChange()
- 位置: async L216-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers._confirmBaselineAllowListDisable()`
- 条件付き依存: `if (value)` → `PrivacySettingHelpers.maybeNotifyUserToReload()`
- 条件付き依存: `if (confirmed)` → `PrivacySettingHelpers.maybeNotifyUserToReload()`
- 参照: `setting.value`

## PrivacySettingHelpers.onBaselineCheckboxChange()
- 位置: async L239-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers._confirmBaselineAllowListDisable()`
- 条件付き依存: `if (event.target.checked)` → `PrivacySettingHelpers.maybeNotifyUserToReload()`
- 条件付き依存: `if (confirmed)` → `PrivacySettingHelpers.maybeNotifyUserToReload()`
- 条件付き依存: `if (!(confirmed))` → `Services.prefs.setBoolPref()`
- 参照: `event.target.checked`, `event.target.slot`
- XPCOM: `Services.prefs`

## PrivacySettingHelpers._confirmBaselineAllowListDisable()
- 位置: async L265-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncConfirmEx()`, `document.l10n.formatValues()`, `propertyBag.get()`, `result.QueryInterface()`
- 参照: `Ci.nsIPropertyBag2`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_CONTENT`, `window.browsingContext`
- XPCOM: [`nsIPropertyBag2`](../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.prompt`

## PrivacySettingHelpers.shouldDisableETPCategoryControls()
- 位置: L296-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`
- 参照: `policy?.Cookies?.Locked`, `policy?.EnableTrackingProtection?.Category`, `policy?.EnableTrackingProtection?.Locked`
- XPCOM: `Services.policies`

## visible()
- 位置: L1618-1619
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `trustPanelBreachAlertsFeatureGate.value`, `trustPanelFeatureGate.value`

## WarningSettingConfig.constructor()
- 位置: L1655-1667
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dismissAllPrefId`, `this.dismissedPrefId`, `this.extensionControlled`, `this.extensionStoreId`, `this.id`, `this.prefMapping`, `this.prefMapping.dismissAll`, `this.prefMapping.dismissed`, `this.problematic`

## WarningSettingConfig.visible()
- 位置: L1675-1682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.problematic()`
- 参照: `this.dismissAll?.value`, `this.dismissed?.value`, `this.extensionControlled`

## WarningSettingConfig.reset()
- 位置: L1688-1694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (this[getter].hasUserValue)` → `this[getter].reset()`
- 参照: `this.prefMapping`, `this[getter].hasUserValue`

## WarningSettingConfig.dismiss()
- 位置: L1699-1703
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dismissed`, `this.dismissed.value`

## WarningSettingConfig.setup()
- 位置: L1713-1752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.keys()`, `Preferences.get()`, `extensionListenerCleanup()`, `this[getter].off()`, `this[getter].on()`
- 条件付き依存: `if (this.extensionStoreId)` → `lazy.Management.on()`
- 条件付き依存: `if (this.extensionStoreId)` → `updateExtensionControlled()`
- 参照: `this.extensionStoreId`, `this.prefMapping`

## updateExtensionControlled()
- 位置: async L1721-1737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionSettingsStore.getSetting()`, `lazy.ExtensionSettingsStore.initialize()`, `lazy.Management.asyncLoadSettingsModules()`
- 条件付き依存: `if (info?.id)` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (this.extensionControlled !== controlled)` → `emitChange()`
- 参照: `info.id`, `info?.id`, `this.extensionControlled`, `this.extensionStoreId`

## extensionListenerCleanup()
- 位置: L1741-1743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Management.off()`

## WarningSettingConfig.onUserClick()
- 位置: L1761-1774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityPreferencesWarnings.warningDismissed.record()`, `Glean.securityPreferencesWarnings.warningFixed.record()`, `this.dismiss()`, `this.reset()`
- 参照: `event.target.id`

## makeSecurityWarningItems()
- 位置: L1935-1958
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SECURITY_WARNINGS.map()`

## getControlConfig()
- 位置: L1959-1964
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!config.items)` → `this.makeSecurityWarningItems()`
- 参照: `config.items`

## get()
- 位置: L1971-1971
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: L1977-1977
- 役割: (未記入)
- 触るとき: (未記入)

## loadTrackerCount()
- 位置: async L1984-1998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `day.getResultByName()`, `emitChange()`, `events.reduce()`, `lazy.TrackingDBService.getEventsByDateRange()`, `now.getTime()`
- 参照: `this.cachedValue`

## setup()
- 位置: L1999-2001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadTrackerCount()`

## get()
- 位置: L2002-2004
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.cachedValue`

## setup()
- 位置: L2012-2040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appUpdater.addListener()`, `appUpdater.removeListener()`
- 条件付き依存: `if (!(sharedAppUpdater))` → `appUpdater.check()`
- 条件付き依存: `if (!sharedAppUpdater)` → `appUpdater.stop()`
- 参照: `appUpdater.status`, `lazy.AppConstants.MOZ_UPDATER`, `lazy.AppUpdater`, `lazy.isPackagedApp`, `this.cachedValue`, `window.gAppUpdater?._appUpdater`

## listener()
- 位置: L2024-2027
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this.cachedValue`

## get()
- 位置: L2041-2043
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.cachedValue`

## set()
- 位置: L2044-2046
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.cachedValue`

## visible()
- 位置: L2065-2074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(deps).filter()`
- 条件付き依存: `if (!this._telemetrySent)` → `Glean.securityPreferencesWarnings.warningsShown.record()`
- 参照: `Object.values(deps).filter( depSetting => depSetting.visible ).length`, `depSetting.visible`, `this._telemetrySent`

## get()
- 位置: L2085-2085
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: L2090-2099
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`
- 参照: `JSON.parse(cacheObj)?.subscribed`

## visible()
- 位置: L2108-2109
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## visible()
- 位置: L2114-2115
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## onUserClick()
- 位置: L2116-2121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPProtection.getPanel()`, `lazy.IPProtection.getPanel(window.browsingContext.topChromeWindow)?.enroll()`
- 参照: `window.browsingContext.topChromeWindow`

## visible()
- 位置: L2144-2153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionSiteExceptionsFeatureEnabled.value`, `ipProtectionSiteInclusionsFeatureEnabled.value`, `ipProtectionVisible.value`

## setup()
- 位置: L2164-2179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## observe()
- 位置: L2166-2173
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (subject && topic === "perm-changed")` → `subject.QueryInterface()`
- 条件付き依存: `if (permission.type === "ipp-vpn")` → `emitChange()`
- 参照: `Ci.nsIPermission`, `permission.type`
- XPCOM: [`nsIPermission`](../../../../netwerk/base/nsIPermission.idl.md)

## visible()
- 位置: L2180-2189
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionSiteExceptionsFeatureEnabled.value`, `ipProtectionSiteInclusionsFeatureEnabled.value`, `ipProtectionVisible.value`

## onUserClick()
- 位置: L2190-2204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`
- XPCOM: [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md)

## getControlConfig()
- 位置: L2205-2222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.getAllByTypes()`, `savedExceptions.filter()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`, `perm.capability`, `savedExceptions.filter( perm => perm.capability === Ci.nsIPermissionManager.DENY_ACTION ).length`
- XPCOM: [`nsIPermissionManager`](../../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## visible()
- 位置: L2232-2241
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionSiteInclusionsFeatureEnabled.value`, `ipProtectionVisible.value`, `settingsRedesignEnabled.value`

## onUserClick()
- 位置: L2242-2245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## get()
- 位置: L2251-2251
- 役割: (未記入)
- 触るとき: (未記入)

## visible()
- 位置: L2260-2267
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionAutoStartFeatureEnabled.value`, `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## visible()
- 位置: L2277-2278
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## visible()
- 位置: L2288-2289
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## visible()
- 位置: L2303-2310
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionBandwidthVisible.value`, `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## visible()
- 位置: L2320-2327
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionBandwidthVisible.value`, `ipProtectionNotOptedIn.value`, `ipProtectionVisible.value`

## getControlConfig()
- 位置: L2329-2348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 条件付き依存: `if (usagePref)` → `JSON.parse()`
- 参照: `lazy.BANDWIDTH.BYTES_IN_GB`, `lazy.BANDWIDTH.MAX_IN_GB`
- XPCOM: `Services.prefs`

## visible()
- 位置: L2358-2367
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ipProtectionNotOptedIn.value`, `ipProtectionSubscribedToVpn.value`, `ipProtectionUpgradeNotAvailable.value`, `ipProtectionVisible.value`

## visible()
- 位置: L2381-2383
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.FirefoxRelay.isAvailable`

## disabled()
- 位置: L2384-2386
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `relayFeature.pref.locked`, `savePasswords.value`

## get()
- 位置: L2387-2389
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.FirefoxRelay.isAvailable`, `lazy.FirefoxRelay.isDisabled`

## set()
- 位置: L2390-2396
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (checked)` → `lazy.FirefoxRelay.markAsAvailable()`
- 条件付き依存: `if (!(checked))` → `lazy.FirefoxRelay.markAsDisabled()`

## onUserChange()
- 位置: L2397-2403
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (checked)` → `Glean.relayIntegration.enabledPrefChange.record()`
- 条件付き依存: `if (!(checked))` → `Glean.relayIntegration.disabledPrefChange.record()`

## visible()
- 位置: L2413-2415
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dntHeaderEnabled.value`, `setting.value`

## onUserClick()
- 位置: L2416-2425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dismissButton.shadowRoot.contains()`, `event.target?.shadowRoot?.querySelector()`
- 参照: `dismissButton?.shadowRoot`, `event.originalTarget`, `setting.value`

## get()
- 位置: L2439-2447
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.httpsOnlyEnabled.value`, `deps.httpsOnlyEnabledPBM.value`

## set()
- 位置: L2448-2459
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.httpsOnlyEnabled.value`, `deps.httpsOnlyEnabledPBM.value`

## disabled()
- 位置: L2460-2462
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.httpsOnlyEnabled.locked`, `deps.httpsOnlyEnabledPBM.locked`

## disabled()
- 位置: L2480-2487
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.httpsFirstEnabled.value`, `deps.httpsFirstEnabledPBM.value`, `deps.httpsOnlyEnabled.value`, `deps.httpsOnlyEnabledPBM.value`

## onUserClick()
- 位置: L2488-2490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showHttpsOnlyModeExceptions()`

## get()
- 位置: L2504-2509
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enableSafeBrowsingMalware.value`, `deps.enableSafeBrowsingPhishing.value`

## set()
- 位置: L2510-2513
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enableSafeBrowsingMalware.value`, `deps.enableSafeBrowsingPhishing.value`

## disabled()
- 位置: L2514-2519
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enableSafeBrowsingMalware.locked`, `deps.enableSafeBrowsingPhishing.locked`

## visible()
- 位置: L2545-2547
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `warningSafeBrowsing.visible`

## onMessageBarDismiss()
- 位置: L2548-2550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `warningSafeBrowsing.config.dismiss()`

## disabled()
- 位置: L2556-2558
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enableSafeBrowsing.value`, `selfSetting.locked`

## get()
- 位置: L2580-2584
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.blockUncommonDownloads.value`, `deps.blockUnwantedDownloads.value`

## set()
- 位置: L2585-2614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(malwareTable.value) .split()`, `(malwareTable.value) .split(",") .filter()`, `Preferences.get()`, `lazy.listManager.forceUpdates()`, `malware.join()`, `malware.sort()`
- 条件付き依存: `if (value)` → `malware.includes()`
- 条件付き依存: `if (malware.includes("goog-malware-shavar"))` → `malware.push()`
- 条件付き依存: `if (!(malware.includes("goog-malware-shavar")))` → `malware.push()`
- 条件付き依存: `if (value)` → `malware.push()`
- 参照: `deps.blockUncommonDownloads.value`, `deps.blockUnwantedDownloads.value`, `malwareTable.value`

## disabled()
- 位置: L2615-2622
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.blockDownloads.value`, `deps.blockUncommonDownloads.locked`, `deps.blockUnwantedDownloads.locked`, `deps.enableSafeBrowsing.value`

## setup()
- 位置: L2632-2667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## onUsageChanged()
- 位置: async L2633-2644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `emitChange()`, `lazy.DownloadUtils.convertByteUnits()`, `lazy.SiteDataManager.getCacheSize()`, `lazy.SiteDataManager.getTotalUsage()`
- 参照: `this.isUpdatingSites`, `this.usage`

## onUpdatingSites()
- 位置: L2646-2649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this.isUpdatingSites`

## getControlConfig()
- 位置: L2668-2686
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isUpdatingSites`, `this.usage`

## visible()
- 位置: L2693-2695
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `privateBrowsingAutoStart.value`

## setup()
- 位置: L2702-2729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## onSitesUpdated()
- 位置: async L2703-2706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this.isUpdatingSites`

## onUpdatingSites()
- 位置: L2708-2711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this.isUpdatingSites`

## onUserClick()
- 位置: L2730-2740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## disabled()
- 位置: L2741-2743
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isUpdatingSites`

## setup()
- 位置: L2750-2777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## onSitesUpdated()
- 位置: async L2751-2754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this.isUpdatingSites`

## onUpdatingSites()
- 位置: L2756-2759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this.isUpdatingSites`

## onUserClick()
- 位置: L2778-2782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## disabled()
- 位置: L2783-2785
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isUpdatingSites`

## onPaneShown()
- 位置: L2794-2802
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.detail.category === "panePrivacy" || event.detail.category === "paneSearchResults" )` → `lazy.SiteDataManager.updateSites()`
- 条件付き依存: `if ( event.detail.category === "panePrivacy" || event.detail.category === "paneSearchResults" )` → `window.removeEventListener()`
- 参照: `event.detail.category`

## disabled()
- 位置: L2808-2811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## onUserClick()
- 位置: L2812-2824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## isCookiesAndStorageClearingOnShutdown()
- 位置: L2827-2833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 参照: `Preferences.get("privacy.clearOnShutdown_v2.cache").value`, `Preferences.get("privacy.clearOnShutdown_v2.cookiesAndStorage").value`, `Preferences.get("privacy.sanitize.sanitizeOnShutdown").value`

## setup()
- 位置: L2870-2875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Sanitizer.maybeMigratePrefs()`

## disabled()
- 位置: L2876-2881
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICookieService.BEHAVIOR_REJECT`, `cookieBehavior.value`, `privateBrowsingAutoStart.value`
- XPCOM: [`nsICookieService`](../../../../netwerk/cookie/nsICookieService.idl.md)

## get()
- 位置: L2882-2886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isCookiesAndStorageClearingOnShutdown()`
- 参照: `privateBrowsingAutoStart.value`

## set()
- 位置: L2887-2910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers._isCustomCleaningPrefPresent()`
- 条件付き依存: `if (!sanitizeOnShutdown.value)` → `PrivacySettingHelpers.resetCleaningPrefs()`
- 参照: `clearOnCloseCache.value`, `clearOnCloseCookies.value`, `clearOnCloseStorage.value`, `sanitizeOnShutdown.value`

## onChangePrivateBrowsingAutoStart()
- 位置: async L2928-2951
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `confirmRestartPrompt()`, `revertFn()`
- 条件付き依存: `if (buttonIndex == CONFIRM_RESTART_PROMPT_RESTART_NOW)` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `window._shouldPromptForRestartPBM`
- XPCOM: [`nsIAppStartup`](../../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## get()
- 位置: L2962-2989
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `formFillEnabled.value`, `historyEnabled.value`, `historyModeCustom.value`, `privateBrowsingAutoStart.value`, `sanitizeOnShutdown.value`

## set()
- 位置: L2990-3044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `optionGroupElement?.childElements.find()`
- 条件付き依存: `if (privateBrowsingAutoStart.value !== lastPrivateBrowsingAutoStart)` → `onChangePrivateBrowsingAutoStart()`
- 条件付き依存: `if (cancelFocusElement)` → `cancelFocusElement.focus()`
- 参照: `document.activeElement?.parentElement`, `formFillEnabled.value`, `historyEnabled.value`, `historyModeCustom.value`, `option.value`, `optionGroupElement.localName`, `privateBrowsingAutoStart.value`, `sanitizeOnShutdown.value`, `setting.value`

## disabled()
- 位置: L3045-3052
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `privateBrowsingAutoStart.locked`, `privateBrowsingAutoStart.value`, `sanitizeOnShutdown.locked`, `sanitizeOnShutdown.value`

## getControlConfig()
- 位置: L3053-3081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.options.find()`, `srdSectionEnabled()`
- 参照: `PrivateBrowsingUtils.enabled`, `dontRememberOption.disabled`, `dontRememberOption.hidden`, `opt.value`, `privateBrowsingAutoStart.locked`, `privateBrowsingAutoStart.value`, `setting.value`

## onUserClick()
- 位置: L3086-3089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## onUserChange()
- 位置: L3096-3101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onChangePrivateBrowsingAutoStart()`
- 参照: `setting.value`

## visible()
- 位置: L3102-3104
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PrivateBrowsingUtils.enabled`, `historyMode.value`

## disabled()
- 位置: L3105-3107
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.disabled`

## visible()
- 位置: L3113-3115
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.value`

## disabled()
- 位置: L3116-3118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `privateBrowsingAutoStart.value`

## visible()
- 位置: L3124-3126
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.value`

## disabled()
- 位置: L3127-3129
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `privateBrowsingAutoStart.value`

## visible()
- 位置: L3135-3137
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.value`

## disabled()
- 位置: L3138-3140
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.disabled`, `privateBrowsingAutoStart.value`

## clearOnShutdownInactive()
- 位置: L3150-3152
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `alwaysClear.value`, `privateBrowsingAutoStart.value`

## visible()
- 位置: L3157-3159
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.value`

## onUserClick()
- 位置: L3161-3171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## visible()
- 位置: L3177-3179
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `historyMode.value`

## onUserClick()
- 位置: L3181-3193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## onUserClick()
- 位置: L3199-3203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.clearPrivateDataNow()`
- 参照: `historyMode.value`

## disabled()
- 位置: L3220-3222
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.disableOpenCertManager.locked`

## onUserClick()
- 位置: L3223-3225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showCertificates()`

## disabled()
- 位置: L3230-3232
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.disableOpenDeviceManager.locked`

## onUserClick()
- 位置: L3233-3235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showSecurityDevices()`

## visible()
- 位置: L3240-3250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`
- 参照: `Services.policies.getActivePolicies()?.Certificates ?.ImportEnterpriseRoots`, `lazy.AppConstants.platform`
- XPCOM: `Services.policies`

## onUserClick()
- 位置: L3259-3262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## disabled()
- 位置: L3268-3268
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dohMode.locked`

## onUserClick()
- 位置: L3269-3269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showDoHExceptions()`

## setup()
- 位置: L3275-3282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## setup()
- 位置: L3288-3295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## getControlConfig()
- 位置: L3311-3325
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIDNSService.MODE_NATIVEONLY`, `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRRONLY`, `deps.dohMode.value`
- XPCOM: [`nsIDNSService`](../../../../netwerk/dns/nsIDNSService.idl.md)

## getControlConfig()
- 位置: L3331-3436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 条件付き依存: `if ( (mode == Ci.nsIDNSService.MODE_TRRFIRST || mode == Ci.nsIDNSService.MODE_TRRONLY) && lazy.gParentalControlsService?.parentalControlsEnabled )` → `Services.dns.getTRRSkipReasonName()`
- 条件付き依存: `if (confirmationStatus != Cr.NS_OK)` → `ChromeUtils.getXPCOMErrorName()`
- 条件付き依存: `if (!(confirmationStatus != Cr.NS_OK))` → `Services.dns.getTRRSkipReasonName()`
- 参照: `Ci.nsIDNSService.CONFIRM_DISABLED`, `Ci.nsIDNSService.CONFIRM_OK`, `Ci.nsIDNSService.CONFIRM_TRYING_OK`, `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRRONLY`, `Ci.nsITRRSkipReason.TRR_BAD_URL`, `Ci.nsITRRSkipReason.TRR_PARENTAL_CONTROL`, `Cr.NS_OK`, `Services.dns.currentTrrConfirmationState`, `Services.dns.currentTrrMode`, `Services.dns.currentTrrURI`, `Services.dns.lastConfirmationSkipReason`, `Services.dns.lastConfirmationStatus`, `URL.parse(trrURI)?.hostname`, `lazy.DoHConfigController.currentConfig .providerSteering.providerList`, `lazy.DoHConfigController.currentConfig.providerList`, `lazy.gParentalControlsService?.parentalControlsEnabled`, `resolver.UIName`, `resolver.uri`
- XPCOM: [`nsIDNSService`](../../../../netwerk/dns/nsIDNSService.idl.md) / [`nsITRRSkipReason`](../../../../netwerk/dns/nsITRRSkipReason.idl.md) / `Services.dns`

## disabled()
- 位置: L3446-3446
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dohMode.locked`

## onUserChange()
- 位置: L3447-3463
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `Glean.securityDohSettings.modeChangedButton.record()`
- 参照: `deps.dohFallbackIfCustom.value`

## get()
- 位置: L3464-3477
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIDNSService.MODE_NATIVEONLY`, `Ci.nsIDNSService.MODE_RESERVED1`, `Ci.nsIDNSService.MODE_RESERVED4`, `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRROFF`, `Ci.nsIDNSService.MODE_TRRONLY`, `deps.dohMode.value`
- XPCOM: [`nsIDNSService`](../../../../netwerk/dns/nsIDNSService.idl.md)

## set()
- 位置: L3478-3518
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (deps.dohMode.value == Ci.nsIDNSService.MODE_NATIVEONLY)` → `Services.prefs.clearUserPref()`
- 参照: `Ci.nsIDNSService.MODE_NATIVEONLY`, `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRROFF`, `Ci.nsIDNSService.MODE_TRRONLY`, `deps.dohFallbackIfCustom.value`, `deps.dohMode.value`, `deps.dohURL.pref.value`, `deps.dohURL.value`, `lazy.DoHConfigController.currentConfig.fallbackProviderURI`
- XPCOM: [`nsIDNSService`](../../../../netwerk/dns/nsIDNSService.idl.md) / `Services.prefs`

## disabled()
- 位置: L3529-3529
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dohMode.locked`

## onUserChange()
- 位置: L3530-3540
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (val)` → `Glean.securityDohSettings.modeChangedButton.record()`
- 条件付き依存: `if (!(val))` → `Glean.securityDohSettings.modeChangedButton.record()`

## get()
- 位置: L3541-3552
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRRONLY`, `deps.dohMode.value`
- XPCOM: [`nsIDNSService`](../../../../netwerk/dns/nsIDNSService.idl.md)

## set()
- 位置: L3553-3564
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRRONLY`, `deps.dohMode.value`
- XPCOM: [`nsIDNSService`](../../../../netwerk/dns/nsIDNSService.idl.md)

## visible()
- 位置: L3571-3573
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.dohProviderSelect.value`

## disabled()
- 位置: L3574-3574
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dohMode.locked`, `dohURL.locked`

## set()
- 位置: L3575-3578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `val?.trim()`

## onUserChange()
- 位置: L3579-3584
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.dohURL.value`, `setting.pref.value`

## disabled()
- 位置: L3590-3590
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dohMode.locked`, `dohURL.locked`

## onUserChange()
- 位置: L3591-3595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityDohSettings.providerChoiceValue.record()`

## getControlConfig()
- 位置: L3596-3632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `options.push()`, `resolvers.map()`, `resolvers.some()`
- 条件付き依存: `if (!defaultFound && defaultURI)` → `resolvers.unshift()`
- 参照: `lazy.DoHConfigController.currentConfig.fallbackProviderURI`, `lazy.DoHConfigController.currentConfig.providerList`, `option.l10nId`, `p.uri`, `resolver.UIName`, `resolver.uri`

## get()
- 位置: L3633-3645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvers.some()`
- 参照: `deps.dohCustomProvider.value`, `deps.dohDefaultURL.value`, `deps.dohURL.value`, `lazy.DoHConfigController.currentConfig.providerList`, `p.uri`

## set()
- 位置: L3646-3677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setting.emit()`
- 条件付き依存: `if (val == "custom")` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (val == "custom")` → `customURI?.trim()`
- 条件付き依存: `if (customURI?.trim())` → `customURI?.trim()`
- 条件付き依存: `if (!(val == "custom"))` → `resolvers.some()`
- 参照: `deps.dohCustomProvider.value`, `deps.dohURL.value`, `lazy.DoHConfigController.currentConfig.providerList`, `p.uri`
- XPCOM: `Services.prefs`

## onUserClick()
- 位置: L3682-3685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## get()
- 位置: L3698-3700
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contentBlockingCategory.value`

## set()
- 位置: L3701-3703
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contentBlockingCategory.value`

## getControlConfig()
- 位置: L3704-3718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.shouldDisableETPCategoryControls()`
- 参照: `option.disabled`, `option.id`, `setting.value`

## onUserChange()
- 位置: L3719-3721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.maybeNotifyUserToReload()`

## getControlConfig()
- 位置: L3731-3745
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contentBlockingCategory.value`

## onUserClick()
- 位置: L3750-3753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## setup()
- 位置: L3758-3761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.NimbusFeatures.urlbar.offUpdate()`, `window.NimbusFeatures.urlbar.onUpdate()`

## visible()
- 位置: L3768-3769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.NimbusFeatures.urlbar.getVariable()`

## visible()
- 位置: L3784-3786
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contentBlockingCategory.value`

## onUserChange()
- 位置: L3787-3789
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.onBaselineAllowListSettingChange()`

## onUserChange()
- 位置: L3795-3797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.maybeNotifyUserToReload()`

## onUserClick()
- 位置: L3802-3805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## set()
- 位置: L3811-3814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setting.emit()`
- 参照: `this._showHint`

## get()
- 位置: L3815-3817
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._showHint`

## visible()
- 位置: L3818-3820
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `setting.value`

## onUserClick()
- 位置: L3825-3827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.reloadAllOtherTabs()`

## visible()
- 位置: L3843-3845
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `resistFingerprinting.value`, `resistFingerprintingPBM.value`

## visible()
- 位置: L3851-3853
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contentBlockingCategory.value`

## disabled()
- 位置: L3858-3861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## onUserClick()
- 位置: L3862-3874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## onUserClick()
- 位置: L3884-3887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.maybeNotifyUserToReload()`
- 参照: `contentBlockingCategory.value`

## disabled()
- 位置: L3888-3893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.shouldDisableETPCategoryControls()`
- 参照: `contentBlockingCategory.value`

## onUserClick()
- 位置: L3899-3902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.maybeNotifyUserToReload()`
- 参照: `contentBlockingCategory.value`

## disabled()
- 位置: L3903-3908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.shouldDisableETPCategoryControls()`
- 参照: `contentBlockingCategory.value`

## onUserChange()
- 位置: L3914-3916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.onBaselineAllowListSettingChange()`

## onUserChange()
- 位置: L3922-3924
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.maybeNotifyUserToReload()`

## disabled()
- 位置: L3930-3932
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `cookieBehavior.locked`

## get()
- 位置: L3933-3935
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `cookieBehavior.value`
- XPCOM: [`nsICookieService`](../../../../netwerk/cookie/nsICookieService.idl.md)

## set()
- 位置: L3936-3943
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `cookieBehavior.pref.defaultValue`, `cookieBehavior.value`
- XPCOM: [`nsICookieService`](../../../../netwerk/cookie/nsICookieService.idl.md)

## get()
- 位置: L3993-4000
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `trackingProtectionEnabled.value`, `trackingProtectionEnabledPBM.value`

## set()
- 位置: L4001-4029
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `socialBlockCookies.value`, `trackingProtectionEmailEnabled.value`, `trackingProtectionEmailEnabledPBM.value`, `trackingProtectionEnabled.value`, `trackingProtectionEnabledPBM.value`, `trackingProtectionSocialEnabled.value`

## disabled()
- 位置: L4042-4046
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `trackingProtectionEnabled.locked`, `trackingProtectionEnabledPBM.locked`

## get()
- 位置: L4047-4051
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `trackingProtectionEnabled.value`, `trackingProtectionEnabledPBM.value`

## set()
- 位置: L4052-4079
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `socialBlockCookies.value`, `trackingProtectionEmailEnabled.value`, `trackingProtectionEmailEnabledPBM.value`, `trackingProtectionEnabled.value`, `trackingProtectionEnabledPBM.value`, `trackingProtectionSocialEnabled.value`

## onUserChange()
- 位置: L4085-4087
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.updateCryptominingLists()`

## onUserChange()
- 位置: L4093-4095
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.updateFingerprintingLists()`

## disabled()
- 位置: L4114-4122
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `etpCustomFingerprintingProtectionEnabled.locked`, `etpCustomFingerprintingProtectionEnabledPBM.locked`

## get()
- 位置: L4123-4134
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `etpCustomFingerprintingProtectionEnabled.value`, `etpCustomFingerprintingProtectionEnabledPBM.value`

## set()
- 位置: L4135-4149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `etpCustomFingerprintingProtectionEnabled.value`, `etpCustomFingerprintingProtectionEnabledPBM.value`

## onUserChange()
- 位置: L4150-4152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privacyUiFppClick.checkbox.record()`

## get()
- 位置: L4161-4177
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `etpCustomFingerprintingProtectionEnabled.value`, `etpCustomFingerprintingProtectionEnabledPBM.value`

## set()
- 位置: L4178-4192
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `etpCustomFingerprintingProtectionEnabled.value`, `etpCustomFingerprintingProtectionEnabledPBM.value`

## onUserChange()
- 位置: L4193-4195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privacyUiFppClick.menu.record()`
