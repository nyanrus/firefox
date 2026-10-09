# browser/components/shell/StartupOSIntegration.sys.mjs

source: browser/components/shell/StartupOSIntegration.sys.mjs
source-hash: 84e32bb8d276bba72160e4be2cdded1b2d3452ed
lines: 302

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetters()`

## WindowsRegPoliciesGetter()
- 位置: L51-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `wrk.close()`, `wrk.hasChild()`, `wrk.open()`
- 条件付き依存: `if (wrk.hasChild("Mozilla\\" + Services.appinfo.name))` → `lazy.WindowsGPOParser.readPolicies()`
- 参照: `Services.appinfo.name`, `wrk.ACCESS_READ`
- XPCOM: `Services.appinfo`

## isPrivateBrowsingAllowedInRegistry()
- 位置: L62-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `WindowsRegPoliciesGetter()`, `lazy.log.debug()`
- 条件付き依存: `if (Services.policies.status > Ci.nsIEnterprisePolicies.UNINITIALIZED)` → `Services.policies.isAllowed()`
- 条件付き依存: `if (Services.policies.status > Ci.nsIEnterprisePolicies.UNINITIALIZED)` → `lazy.log.debug()`
- 条件付き依存: `if (AppConstants.platform !== "win")` → `lazy.log.debug()`
- 条件付き依存: `if (!Cu.isInAutomation)` → `WindowsRegPoliciesGetter()`
- 条件付き依存: `if (machinePolicies && "DisablePrivateBrowsing" in machinePolicies)` → `lazy.log.debug()`
- 条件付き依存: `if (userPolicies && "DisablePrivateBrowsing" in userPolicies)` → `lazy.log.debug()`
- 参照: `AppConstants.platform`, `Ci.nsIEnterprisePolicies.UNINITIALIZED`, `Ci.nsIWindowsRegKey`, `Cu.isInAutomation`, `Services.policies.status`, `machinePolicies.DisablePrivateBrowsing`, `userPolicies.DisablePrivateBrowsing`, `wrk.ROOT_KEY_CURRENT_USER`, `wrk.ROOT_KEY_LOCAL_MACHINE`
- XPCOM: [`nsIEnterprisePolicies`](../../../toolkit/components/enterprisepolicies/nsIEnterprisePolicies.idl.md) / [`nsIWindowsRegKey`](../../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1` / `Services.policies`

## applyCustomIconOnStartup()
- 位置: L135-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.CustomIconManager.applyRuntimeOverrideForStartup()`
- 参照: `AppConstants.platform`

## checkForLaunchOnLogin()
- 位置: L146-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LaunchOnLogin.isSupported()`
- 条件付き依存: `if (!lazy.profileService.startWithLastProfile)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(launchOnLoginPref))` → `Glean.launchOnLogin.lastProfileDisableStartup.record()`
- 条件付き依存: `if (!lazy.profileService.startWithLastProfile)` → `lazy.LaunchOnLogin.disable()`
- 参照: `lazy.profileService.startWithLastProfile`
- XPCOM: `Services.prefs`

## onStartupIdle()
- 位置: async L166-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `safeCall()`, `this.ensureBridgeRegistered()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.sysinfo.getProperty()`
- 条件付き依存: `if (Services.sysinfo.getProperty("hasWinPackageId"))` → `safeCall()`
- 条件付き依存: `if (Services.sysinfo.getProperty("hasWinPackageId"))` → `this.maybePinMSIXToStartMenu()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `safeCall()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.ensurePrivateBrowsingShortcutExists()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `lazy.CustomIconManager.ensureAppliedOrRevert()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `lazy.CustomIconManager.maybeCreatePerUserStartMenuShortcut()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.sysinfo`

## safeCall()
- 位置: async L168-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `fn()`

## ensureBridgeRegistered()
- 位置: async L196-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (defaultProfile && currentProfile == defaultProfile)` → `lazy.FirefoxBridgeExtensionUtils.ensureRegistered()`
- 条件付き依存: `if (!(defaultProfile && currentProfile == defaultProfile))` → `lazy.log.debug()`
- 参照: `lazy.profileService`
- XPCOM: `Services.prefs`

## maybePinMSIXToStartMenu()
- 位置: async L214-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`, `lazy.ShellService.doesAppNeedStartMenuPin()`, `lazy.ShellService.recordWasPreviouslyPinnedToStartMenu()`
- 条件付き依存: `if ( lazy.BrowserHandler.firstRunProfile && (await lazy.ShellService.doesAppNeedStartMenuPin()) )` → `lazy.ShellService.pinToStartMenu()`
- 参照: `lazy.BrowserHandler.firstRunProfile`
- XPCOM: `Services.sysinfo`

## ensurePrivateBrowsingShortcutExists()
- 位置: async L238-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/browser/shell-service;1"].getService()`, `Cc["@mozilla.org/windows-taskbar;1"].getService()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `Services.sysinfo.getProperty()`, `shellService.hasPinnableShortcut()`
- 条件付き依存: `if ( !(await shellService.hasPinnableShortcut( winTaskbar.defaultPrivateGroupId, true )) )` → `Services.dirsvc.get()`
- 条件付き依存: `if ( !(await shellService.hasPinnableShortcut( winTaskbar.defaultPrivateGroupId, true )) )` → `appdir.clone()`
- 条件付き依存: `if ( !(await shellService.hasPinnableShortcut( winTaskbar.defaultPrivateGroupId, true )) )` → `exe.append()`
- 条件付き依存: `if ( !(await shellService.hasPinnableShortcut( winTaskbar.defaultPrivateGroupId, true )) )` → `strings.formatValues()`
- 条件付き依存: `if ( !(await shellService.hasPinnableShortcut( winTaskbar.defaultPrivateGroupId, true )) )` → `shellService.createShortcut()`
- 参照: `Ci.nsIFile`, `Ci.nsIWinTaskbar`, `Ci.nsIWindowsShellService`, `lazy.PrivateBrowsingUtils.enabled`, `winTaskbar.defaultPrivateGroupId`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `nsIWinTaskbar` / [`nsIWindowsShellService`](nsIWindowsShellService.idl.md) / `@mozilla.org/browser/shell-service;1` / `@mozilla.org/windows-taskbar;1` / `Services.dirsvc` / `Services.prefs` / `Services.sysinfo`
