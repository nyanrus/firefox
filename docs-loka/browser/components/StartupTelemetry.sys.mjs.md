# browser/components/StartupTelemetry.sys.mjs

source: browser/components/StartupTelemetry.sys.mjs
source-hash: 3ff41474da5020938e27779c750578029cc1dcd3
lines: 550

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _willUseExpensiveTelemetry()
- 位置: L35-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `AppConstants.MOZ_TELEMETRY_REPORTING`
- XPCOM: `Services.prefs`

## _runIdleTasks()
- 位置: L45-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.now()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `console.error()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task.toSource()`
- 参照: `Services.startup.shuttingDown`
- XPCOM: `Services.startup`

## browserIdleStartup()
- 位置: L66-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._runIdleTasks()`, `this.aiControlBlocking()`, `this.contentBlocking()`, `this.dataSanitization()`, `this.globalPrivacyControl()`, `this.httpsOnlyState()`, `this.initFOG()`, `this.launchOnLoginState()`, `this.osAuthEnabled()`, `this.pipEnabled()`, `this.sslKeylogFile()`, `this.startupConditions()`
- 条件付き依存: `if (this._willUseExpensiveTelemetry)` → `tasks.push()`
- 条件付き依存: `if (this._willUseExpensiveTelemetry)` → `lazy.PlacesDBUtils.telemetry()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `tasks.push()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.pinningStatus()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.isDefaultHandler()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `tasks.push()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.macDockStatus()`
- 参照: `AppConstants.platform`, `this._willUseExpensiveTelemetry`

## bestEffortIdleStartup()
- 位置: L106-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OsEnvironment.reportAllowedAppSources()`, `this._runIdleTasks()`, `this.primaryPasswordEnabled()`
- 条件付き依存: `if (AppConstants.platform == "win" && this._willUseExpensiveTelemetry)` → `tasks.push()`
- 条件付き依存: `if (AppConstants.platform == "win" && this._willUseExpensiveTelemetry)` → `lazy.BrowserUsageTelemetry.reportProfileCount()`
- 条件付き依存: `if (AppConstants.platform == "win" && this._willUseExpensiveTelemetry)` → `lazy.BrowserUsageTelemetry.reportInstallationTelemetry()`
- 参照: `AppConstants.platform`, `this._willUseExpensiveTelemetry`

## initFOG()
- 位置: async L126-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings.fxAccountsClientInfo.setEnabled()`, `JSON.stringify()`, `Services.fog.applyServerKnobsConfig()`, `Services.fog.initializeFOG()`, `lazy.NimbusFeatures.glean.getAllEnrollments()`, `lazy.NimbusFeatures.glean.onUpdate()`, `lazy.NimbusFeatures.gleanInternalSdk.getVariable()`, `lazy.NimbusFeatures.gleanInternalSdk.onUpdate()`, `lazy.TelemetryReportingPolicy.ensureUserIsNotified()`, `lazy.UsageReporting.ensureInitialized()`
- 条件付き依存: `if (typeof cfg === "object" && cfg !== null)` → `Services.fog.applyServerKnobsConfig()`
- 条件付き依存: `if (typeof cfg === "object" && cfg !== null)` → `JSON.stringify()`
- 参照: `enrollment.value.gleanMetricConfiguration`
- XPCOM: `Services.fog`

## startupConditions()
- 位置: L168-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.startup.isCold.set()`, `Glean.startup.secondsSinceLastOsRestart.set()`, `Math.round()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- 条件付き依存: `if (ex.name !== "NS_ERROR_NOT_IMPLEMENTED")` → `console.error()`
- 参照: `Services.startup.secondsSinceLastOSRestart`, `ex.name`
- XPCOM: `Services.prefs` / `Services.startup`

## contentBlocking()
- 位置: L197-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.contentblocking.category.set()`, `Glean.contentblocking.cookieBehavior.accumulateSingleSample()`, `Glean.contentblocking.cryptominingBlockingEnabled.set()`, `Glean.contentblocking.fingerprintingBlockingEnabled.set()`, `Glean.contentblocking.trackingProtectionEnabled[ tpEnabled ? "true" : "false" ].add()`, `Glean.contentblocking.trackingProtectionPbmDisabled[ !tpPBEnabled ? "true" : "false" ].add()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prefs.getStringPref()`
- 参照: `Glean.contentblocking.trackingProtectionEnabled`, `Glean.contentblocking.trackingProtectionPbmDisabled`
- XPCOM: `Services.prefs`

## dataSanitization()
- 位置: L247-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.datasanitization.privacyClearOnShutdownCache.set()`, `Glean.datasanitization.privacyClearOnShutdownCookies.set()`, `Glean.datasanitization.privacyClearOnShutdownDownloads.set()`, `Glean.datasanitization.privacyClearOnShutdownFormdata.set()`, `Glean.datasanitization.privacyClearOnShutdownHistory.set()`, `Glean.datasanitization.privacyClearOnShutdownOfflineApps.set()`, `Glean.datasanitization.privacyClearOnShutdownOpenWindows.set()`, `Glean.datasanitization.privacyClearOnShutdownSessions.set()`, `Glean.datasanitization.privacyClearOnShutdownSiteSettings.set()`, `Glean.datasanitization.privacySanitizeSanitizeOnShutdown.set()`, `Glean.datasanitization.sessionPermissionExceptions.set()`, `Services.prefs.getBoolPref()`, `["http", "https", "file"].some()`, `permission.principal.schemeIs()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`, `Services.perms.all`, `permission.capability`, `permission.type`
- XPCOM: [`nsICookiePermission`](../../netwerk/cookie/nsICookiePermission.idl.md) / `Services.perms` / `Services.prefs`

## httpsOnlyState()
- 位置: L295-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `_checkHTTPSOnlyPBMPref()`, `_checkHTTPSOnlyPref()`
- XPCOM: `Services.prefs`

## _checkHTTPSOnlyPref()
- 位置: async L298-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.security.httpsOnlyModeEnabled.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabled)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _checkHTTPSOnlyPBMPref()
- 位置: async L318-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.security.httpsOnlyModeEnabledPbm.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabledPBM)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## globalPrivacyControl()
- 位置: L338-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `_checkGPCPref()`
- XPCOM: `Services.prefs`

## _checkGPCPref()
- 位置: async L341-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.security.globalPrivacyControlEnabled.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (feature_enabled)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## aiControlBlocking()
- 位置: L361-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `_checkAiControlPrefs()`
- XPCOM: `Services.prefs`

## _checkAiControlPrefs()
- 位置: async L372-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.aiControlIsBlocking[key].set()`, `Glean.browser.globalAiControlIsBlocking.set()`, `Object.entries()`, `Services.prefs.getStringPref()`
- 参照: `Glean.browser.aiControlIsBlocking`
- XPCOM: `Services.prefs`

## isUsingLauncher()
- 位置: L400-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.get()`
- XPCOM: `Services.env`

## pinningStatus()
- 位置: async L408-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/browser/shell-service;1"].getService()`, `Cc["@mozilla.org/windows-taskbar;1"].getService()`, `Glean.osEnvironment.isTaskbarPinned.set()`, `Glean.osEnvironment.launchMethod.set()`, `Services.sysinfo.getProperty()`, `console.error()`, `shellService.classifyShortcut()`, `shellService.isCurrentAppPinnedToTaskbar()`
- 条件付き依存: `if ( AppConstants.platform === "win" && !Services.sysinfo.getProperty("hasWinPackageId") )` → `Glean.osEnvironment.isTaskbarPinnedPrivate.set()`
- 条件付き依存: `if ( AppConstants.platform === "win" && !Services.sysinfo.getProperty("hasWinPackageId") )` → `shellService.isCurrentAppPinnedToTaskbar()`
- 条件付き依存: `if (!(shortcut))` → `this.isUsingLauncher()`
- 参照: `AppConstants.platform`, `Ci.nsIWinTaskbar`, `Ci.nsIWindowsShellService`, `Services.appinfo.processStartupShortcut`, `lazy.BrowserInitState.isLaunchOnLogin`, `lazy.BrowserInitState.isTaskbarTab`, `winTaskbar.defaultGroupId`, `winTaskbar.defaultPrivateGroupId`
- XPCOM: `nsIWinTaskbar` / [`nsIWindowsShellService`](shell/nsIWindowsShellService.idl.md) / `@mozilla.org/browser/shell-service;1` / `@mozilla.org/windows-taskbar;1` / `Services.appinfo` / `Services.sysinfo`

## isDefaultHandler()
- 位置: L467-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.osEnvironment.isDefaultHandler[x].set()`, `[".pdf", "mailto"].every()`, `lazy.ShellService.isDefaultHandlerFor()`
- 参照: `Glean.osEnvironment.isDefaultHandler`

## launchOnLoginState()
- 位置: async L478-500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.osEnvironment.launchOnLoginState.set()`, `lazy.LaunchOnLogin.isSupported()`
- 条件付き依存: `if (!(!lazy.LaunchOnLogin.isSupported()))` → `lazy.LaunchOnLogin.enablementDetails()`
- 条件付き依存: `if (!(!lazy.LaunchOnLogin.isSupported()))` → `console.error()`
- 参照: `enablementDetails.isAllowedByPolicy`, `enablementDetails.isEnabled`, `enablementDetails.isSupported`

## macDockStatus()
- 位置: L502-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/macdocksupport;1"].getService()`, `Glean.osEnvironment.isKeptInDock.set()`
- 参照: `Cc["@mozilla.org/widget/macdocksupport;1"].getService( Ci.nsIMacDockSupport ).isAppInDock`, `Ci.nsIMacDockSupport`
- XPCOM: `nsIMacDockSupport` / `@mozilla.org/widget/macdocksupport;1`

## sslKeylogFile()
- 位置: L511-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sslkeylogging.enabled.set()`, `Services.env.exists()`
- XPCOM: `Services.env`

## osAuthEnabled()
- 位置: L515-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.formautofill.osAuthEnabled.set()`, `Glean.pwmgr.osAuthEnabled.set()`, `lazy.FormAutofillUtils.getOSAuthEnabled()`, `lazy.LoginHelper.getOSAuthEnabled()`

## primaryPasswordEnabled()
- 位置: L523-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/security/internalkeytoken;1"].createInstance()`, `Glean.primaryPassword.enabled.set()`
- 参照: `Ci.nsIPKCS11Token`, `token.hasPassword`
- XPCOM: `nsIPKCS11Token` / `@mozilla.org/security/internalkeytoken;1`

## pipEnabled()
- 位置: L530-548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `observe()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L534-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.pictureinpicture.toggleEnabled.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabled)` → `Glean.pictureinpictureSettings.enableSettings.record()`
- XPCOM: `Services.prefs`
