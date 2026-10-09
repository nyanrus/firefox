# browser/components/shell/CustomIconManager.sys.mjs

source: browser/components/shell/CustomIconManager.sys.mjs
source-hash: 768a0b686f946f34afb654558622863c49cc7401
lines: 826

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.createInstance()`

## resolveVariant()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `entry.variants`

## resolveResourceId()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveVariant()`
- 参照: `resolveVariant(entry, scheme).iconResourceId`

## resolvePreview()
- 位置: L138-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveVariant()`
- 参照: `resolveVariant(entry, scheme).preview`

## browserExePath()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `Services.dirsvc`

## installShortcutEntries()
- 位置: async L187-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ShellService.enumerateInstallShortcuts()`, `lazy.logConsole.error()`
- 参照: `lazy.WinTaskbar.defaultGroupId`

## governingStartMenuShortcut()
- 位置: L205-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `locations.has()`

## shouldDisableCustomIcon()
- 位置: L222-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `governingStartMenuShortcut()`, `state.locations.has()`
- 参照: `state.locations`, `state.slotTakenByOtherInstall`

## testOnlyGoverningStartMenuShortcut()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `governingStartMenuShortcut()`

## testOnlyShouldDisableCustomIcon()
- 位置: L246-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shouldDisableCustomIcon()`

## applyIconToWindowsShortcuts()
- 位置: async L263-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries .filter()`, `entries .filter(entry => entry.location != "CommonPrograms") .map()`, `entries.map()`, `entries.map(entry => entry.path).join()`, `installShortcutEntries()`, `lazy.ShellService.setShortcutsIcon()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`
- 条件付き依存: `if (!shortcuts.length)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (ex.result == Cr.NS_ERROR_NOT_AVAILABLE)` → `lazy.logConsole.error()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `entries.length`, `entry.location`, `entry.path`, `ex.result`, `lazy.WinTaskbar.defaultGroupId`, `shortcuts.length`

## applyRuntimeWindowsIcon()
- 位置: L323-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.WinTaskbar.setAllWindowIcons()`, `lazy.logConsole.error()`

## osColorScheme()
- 位置: L347-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `key.close()`, `key.hasValue()`, `key.open()`, `lazy.logConsole.warn()`
- 条件付き依存: `if (key.hasValue("SystemUsesLightTheme"))` → `key.readIntValue()`
- 参照: `Ci.nsIWindowsRegKey`, `Ci.nsIWindowsRegKey.ACCESS_READ`, `Ci.nsIWindowsRegKey.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`

## supported()
- 位置: L385-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.sysinfo`

## apply()
- 位置: async L407-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `Services.sysinfo.getProperty()`, `applyIconToWindowsShortcuts()`, `applyRuntimeWindowsIcon()`, `browserExePath()`, `osColorScheme()`, `resolveResourceId()`
- 条件付き依存: `if (!updated)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (id !== previousId)` → `Glean.customIcon.changed.record()`
- 参照: `AppConstants.platform`, `this.currentId`
- XPCOM: `Services.prefs` / `Services.sysinfo`

## revert()
- 位置: async L460-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `applyIconToWindowsShortcuts()`, `applyRuntimeWindowsIcon()`, `browserExePath()`
- 条件付き依存: `if (ICON_CATALOG[previousId] && previousId !== "default")` → `Glean.customIcon.changed.record()`
- 参照: `AppConstants.platform`, `this.currentId`
- XPCOM: `Services.prefs`

## applyRuntimeOverrideForStartup()
- 位置: L493-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `applyRuntimeWindowsIcon()`, `osColorScheme()`, `resolveResourceId()`, `this.registerObservers()`
- 参照: `this.currentId`, `this.supported`

## registerObservers()
- 位置: L512-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.logConsole.debug()`
- XPCOM: `Services.obs`

## unregisterObservers()
- 位置: L527-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.logConsole.debug()`
- XPCOM: `Services.obs`

## observe()
- 位置: L539-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `osColorScheme()`, `this.unregisterObservers()`
- 条件付き依存: `if (entry?.variants && osColorScheme() !== gLastAppliedScheme)` → `this.apply(this.currentId).catch()`
- 条件付き依存: `if (entry?.variants && osColorScheme() !== gLastAppliedScheme)` → `this.apply()`
- 条件付き依存: `if (entry?.variants && osColorScheme() !== gLastAppliedScheme)` → `lazy.logConsole.error()`
- 条件付き依存: `if (data == "remote")` → `this.ensureAppliedOrRevert(true /* remoteProfileUpdated */).catch()`
- 条件付き依存: `if (data == "remote")` → `this.ensureAppliedOrRevert()`
- 条件付き依存: `if (data == "remote")` → `lazy.logConsole.error()`
- 参照: `entry?.variants`, `this.currentId`

## ensureAppliedOrRevert()
- 位置: async L590-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.customIcon.current.set()`, `Services.prefs.getBoolPref()`, `applyRuntimeWindowsIcon()`, `osColorScheme()`, `resolveResourceId()`, `shouldDisableCustomIcon()`, `this.getInstallShortcutState()`
- 条件付き依存: `if (!remoteProfileUpdated)` → `lazy.SelectableProfileService.init()`
- 条件付き依存: `if (this.currentId)` → `this.revert()`
- 条件付き依存: `if ( state && shouldDisableCustomIcon( state, Services.prefs.getBoolPref( PREF_PER_USER_START_MENU_SHORTCUT_CREATED, false ) ) )` → `lazy.logConsole.warn()`
- 条件付き依存: `if ( state && shouldDisableCustomIcon( state, Services.prefs.getBoolPref( PREF_PER_USER_START_MENU_SHORTCUT_CREATED, false ) ) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( state && shouldDisableCustomIcon( state, Services.prefs.getBoolPref( PREF_PER_USER_START_MENU_SHORTCUT_CREATED, false ) ) )` → `this.revert()`
- 条件付き依存: `if (remoteProfileUpdated)` → `applyRuntimeWindowsIcon()`
- 条件付き依存: `if (!entry)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (!entry)` → `this.revert()`
- 条件付き依存: `if (entry.variants)` → `this.apply()`
- 参照: `entry.variants`, `this.currentId`, `this.supported`
- XPCOM: `Services.prefs`

## getInstallShortcutState()
- 位置: async L682-706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `Services.dirsvc.get()`, `entries.map()`, `installShortcutEntries()`
- 条件付き依存: `if (await IOUtils.exists(slotPath))` → `slotPath.toLowerCase()`
- 条件付き依存: `if (await IOUtils.exists(slotPath))` → `entries.some()`
- 条件付き依存: `if (await IOUtils.exists(slotPath))` → `entry.path.toLowerCase()`
- 参照: `AppConstants.MOZ_APP_DISPLAYNAME_DO_NOT_USE`, `Ci.nsIFile`, `Services.dirsvc.get("Progs", Ci.nsIFile).path`, `entry.location`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `Services.dirsvc`

## maybeCreatePerUserStartMenuShortcut()
- 位置: async L721-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `governingStartMenuShortcut()`, `lazy.ShellService.createShortcut()`, `lazy.logConsole.error()`, `strings.formatValues()`, `this.getInstallShortcutState()`
- 条件付き依存: `if (governing == kUserShortcut)` → `Services.prefs.setBoolPref()`
- 参照: `AppConstants.MOZ_APP_DISPLAYNAME_DO_NOT_USE`, `Ci.nsIFile`, `lazy.WinTaskbar.defaultGroupId`, `state.locations`, `state.slotTakenByOtherInstall`, `this.supported`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `Services.dirsvc` / `Services.prefs`

## refreshTaskbarButtons()
- 位置: L803-817
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.WinTaskbar.refreshTaskbarButtons()`, `lazy.logConsole.error()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.obs`
