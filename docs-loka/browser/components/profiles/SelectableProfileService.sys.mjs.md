# browser/components/profiles/SelectableProfileService.sys.mjs

source: browser/components/profiles/SelectableProfileService.sys.mjs
source-hash: e3ffff744b3d0651ac37819b077521d4d9542494
lines: 2304

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.ID()`, `SelectableProfileService.updateEnabledState()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## loadImage()
- 位置: async L304-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.fetchDecodedImage()`, `Services.io.newChannelFromURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (profile.hasCustomAvatar)` → `IOUtils.getFile()`
- 条件付き依存: `if (profile.hasCustomAvatar)` → `profile.getAvatarPath()`
- 条件付き依存: `if (profile.hasCustomAvatar)` → `Services.io.newFileURI()`
- 条件付き依存: `if (!(profile.hasCustomAvatar))` → `Services.io.newURI()`
- 条件付き依存: `if (!(profile.hasCustomAvatar))` → `profile.getAvatarPath()`
- 参照: `Ci.nsIContentPolicy.TYPE_IMAGE`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_SEC_CONTEXT_IS_NULL`, `profile.hasCustomAvatar`
- XPCOM: [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / `Services.io` / `Services.scriptSecurityManager`

## SelectableProfileServiceClass.constructor()
- 位置: L391-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.prefs.addObserver()`, `super()`, `this.#getEnabledState()`, `this.lookAndFeelChanged.bind()`, `this.matchMediaObserver.bind()`, `this.themeObserver.bind()`, `this.updateEnabledState()`
- 参照: `ProfilesDatastoreService.toolkitProfileService`, `lazy.PROFILES_CREATED`, `this.#isEnabled`, `this.#observedPrefs`, `this.#profileService`, `this.lookAndFeelChanged`, `this.matchMediaObserver`, `this.prefObserver`, `this.themeObserver`
- XPCOM: `Services.obs` / `Services.prefs`

## this.prefObserver()
- 位置: L397-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.flushSharedPrefToDatabase()`

## SelectableProfileServiceClass.migrateToProfilesCreatedPref()
- 位置: L423-427
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.groupToolkitProfile?.storeID && !lazy.PROFILES_CREATED)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.PROFILES_CREATED`, `this.groupToolkitProfile?.storeID`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.hasCreatedSelectableProfiles()
- 位置: L429-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.#getEnabledState()
- 位置: L433-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `this.migrateToProfilesCreatedPref()`
- 参照: `lazy.PROFILES_ENABLED`, `this.groupToolkitProfile`, `this.groupToolkitProfile?.storeID`
- XPCOM: `Services.policies`

## SelectableProfileServiceClass.updateEnabledState()
- 位置: L450-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getEnabledState()`
- 条件付き依存: `if (newState != this.#isEnabled)` → `this.emit()`
- 参照: `this.#isEnabled`

## SelectableProfileServiceClass.isEnabled()
- 位置: L458-460
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isEnabled`

## SelectableProfileServiceClass.#setOverlayIcon()
- 位置: L462-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TASKBAR_ICON_CONTROLLERS.has()`
- 条件付き依存: `if (!TASKBAR_ICON_CONTROLLERS.has(win))` → `Cc["@mozilla.org/windows-taskbar;1"] .getService(Ci.nsIWinTaskbar) .getOverlayIconController()`
- 条件付き依存: `if (!TASKBAR_ICON_CONTROLLERS.has(win))` → `Cc["@mozilla.org/windows-taskbar;1"] .getService()`
- 条件付き依存: `if (!TASKBAR_ICON_CONTROLLERS.has(win))` → `TASKBAR_ICON_CONTROLLERS.set()`
- 条件付き依存: `if (!(!TASKBAR_ICON_CONTROLLERS.has(win)))` → `TASKBAR_ICON_CONTROLLERS.get()`
- 条件付き依存: `if (this.#currentProfile.hasCustomAvatar)` → `iconController?.setOverlayIcon()`
- 条件付き依存: `if (!(this.#currentProfile.hasCustomAvatar))` → `iconController?.setOverlayIcon()`
- 参照: `Ci.nsIWinTaskbar`, `this.#badge`, `this.#badge.description`, `this.#badge.iconPaintContext`, `this.#badge.image`, `this.#currentProfile.hasCustomAvatar`, `win.docShell`
- XPCOM: `nsIWinTaskbar` / `@mozilla.org/windows-taskbar;1`

## SelectableProfileServiceClass.#attemptFlushProfileService()
- 位置: async L491-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#profileService.asyncFlush()`, `this.#profileService.asyncFlushCurrentProfile()`

## SelectableProfileServiceClass.storeID()
- 位置: L505-507
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#storeID`

## SelectableProfileServiceClass.groupToolkitProfile()
- 位置: L509-511
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#profileService.currentProfile`

## SelectableProfileServiceClass.currentProfile()
- 位置: L513-515
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#currentProfile`

## SelectableProfileServiceClass.initialized()
- 位置: L517-519
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#initialized`

## SelectableProfileServiceClass.initProfilesData()
- 位置: async L521-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.#attemptFlushProfileService()`
- 参照: `ProfilesDatastoreService.storeID`, `lazy.PROFILES_CREATED`, `this.#storeID`, `this.groupToolkitProfile`, `this.groupToolkitProfile.storeID`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.init()
- 位置: L544-546
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#init()`

## SelectableProfileServiceClass.#init()
- 位置: L556-564
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#initPromise)` → `this.#initialize(isInitial).finally()`
- 条件付き依存: `if (!this.#initPromise)` → `this.#initialize()`
- 参照: `this.#initPromise`

## SelectableProfileServiceClass.#initialize()
- 位置: async L566-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.profiles.active.set()`, `Glean.profiles.profileCount.set()`, `ProfilesDatastoreService.constructor.getDirectory()`, `ProfilesDatastoreService.getConnection()`, `Services.env.get()`, `Services.obs.addObserver()`, `Services.wm.getMostRecentBrowserWindow()`, `prefersDarkQuery?.addEventListener()`, `this.getProfileByPath()`, `this.getProfileCount()`, `this.initWindowTracker()`, `this.setDefaultProfileForGroup()`, `this.updateEnabledState()`, `window?.matchMedia()`
- 条件付き依存: `if (resetProfilePath)` → `this.#updateProfilePath()`
- 条件付き依存: `if (resetProfilePath)` → `ProfilesDatastoreService.constructor.getDirectory()`
- 条件付き依存: `if (resetProfilePath)` → `Services.env.set()`
- 条件付き依存: `if (resetProfilePath && this.#currentProfile)` → `this.getColorsForDefaultTheme()`
- 条件付き依存: `if (!isInitial && !Services.startup.startingUp && !this.#currentProfile)` → `Glean.profiles.currentMissing.record()`
- 条件付き依存: `if (this.#cachedProfileCount)` → `this.#createProfile()`
- 条件付き依存: `if (this.#cachedProfileCount)` → `ProfilesDatastoreService.constructor.getDirectory()`
- 条件付き依存: `if (!(this.#cachedProfileCount))` → `this.#attemptFlushProfileService()`
- 条件付き依存: `if (!(this.#cachedProfileCount))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(this.#cachedProfileCount))` → `this.updateEnabledState()`
- 条件付き依存: `if (!(this.#cachedProfileCount))` → `Glean.profiles.active.set()`
- 条件付き依存: `if (this.groupToolkitProfile.storeID != this.storeID)` → `this.#attemptFlushProfileService()`
- 条件付き依存: `if (this.#currentProfile)` → `this.databaseChanged()`
- 条件付き依存: `if (this.#currentProfile)` → `this.#maybeAddDAUGroupIDToDB()`
- 参照: `ProfilesDatastoreService.constructor.getDirectory("ProfD").path`, `ProfilesDatastoreService.storeID`, `ProfilesDatastoreService.toolkitProfileService`, `Services.startup.startingUp`, `lazy.PROFILES_CREATED`, `this.#cachedProfileCount`, `this.#connection`, `this.#currentProfile`, `this.#initialized`, `this.#profileService`, `this.#storeID`, `this.#windowActivated`, `this.currentProfile.theme`, `this.groupToolkitProfile.storeID`, `this.isEnabled`, `this.lookAndFeelChanged`, `this.matchMediaObserver`, `this.storeID`, `this.themeObserver`
- XPCOM: `Services.env` / `Services.obs` / `Services.prefs` / `Services.startup` / `Services.wm`

## SelectableProfileServiceClass.startupMigrationInit()
- 位置: async L709-725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.getStartupMigrationConnection()`
- 参照: `ProfilesDatastoreService.storeID`, `lazy.MigrationUtils.isStartupMigration`, `this.#connection`, `this.#initialized`, `this.#storeID`

## SelectableProfileServiceClass.uninit()
- 位置: async L727-754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.EveryWindow.unregisterCallback()`, `this.clearPrefObservers()`
- 参照: `this.#badge`, `this.#connection`, `this.#currentProfile`, `this.#everyWindowCallbackId`, `this.#initialized`, `this.lookAndFeelChanged`, `this.themeObserver`
- XPCOM: `Services.obs`

## SelectableProfileServiceClass.initWindowTracker()
- 位置: L756-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.#setOverlayIcon()`, `window.addEventListener()`, `window.gBrowser.updateTitlebar()`, `window.removeEventListener()`
- 参照: `this.#everyWindowCallbackId`

## SelectableProfileServiceClass.handleEvent()
- 位置: async L786-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setOverlayIcon()`, `this.#windowActivated.arm()`
- 参照: `event.target`, `event.type`

## SelectableProfileServiceClass.observe()
- 位置: L796-818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.databaseChanged()`, `this.themeObserver()`
- 条件付き依存: `if (this.#badge && "nsIWinTaskbar" in Ci)` → `this.#setOverlayIcon()`
- 参照: `lazy.EveryWindow.readyWindows`, `this.#badge`

## SelectableProfileServiceClass.deleteProfileGroup()
- 位置: async L825-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.#attemptFlushProfileService()`, `this.getAllProfiles()`
- 参照: `(await this.getAllProfiles()).length`, `this.groupToolkitProfile.storeID`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.execProcess()
- 位置: L841-863
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/process/util;1"].createInstance()`, `ProfilesDatastoreService.constructor.getDirectory()`, `process.init()`, `process.runw()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `appBundle.path.endsWith()`
- 条件付き依存: `if (appBundle.path.endsWith(".app"))` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService(Ci.nsIMacDockSupport) .launchAppBundle()`
- 条件付き依存: `if (appBundle.path.endsWith(".app"))` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService()`
- 参照: `AppConstants.platform`, `Ci.nsIMacDockSupport`, `Ci.nsIProcess`, `aArgs.length`, `executable.parent.parent.parent`
- XPCOM: `nsIMacDockSupport` / [`nsIProcess`](../../../xpcom/threads/nsIProcess.idl.md) / `@mozilla.org/process/util;1` / `@mozilla.org/widget/macdocksupport;1`

## SelectableProfileServiceClass.sendCommandLine()
- 位置: L870-874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/remote;1"] .getService()`, `Cc["@mozilla.org/remote;1"] .getService(Ci.nsIRemoteService) .sendCommandLine()`
- 参照: `Ci.nsIRemoteService`
- XPCOM: [`nsIRemoteService`](../../../toolkit/components/remote/nsIRemoteService.idl.md) / `@mozilla.org/remote;1` → `nsIRemoteService` (toolkit/components/remote/components.conf)

## SelectableProfileServiceClass.launchInstance()
- 位置: L882-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `args.unshift()`, `this.execProcess()`, `this.sendCommandLine()`
- 条件付き依存: `if (aUrls?.length)` → `args.push()`
- 条件付き依存: `if (aUrls?.length)` → `aUrls.flatMap()`
- 条件付き依存: `if (!(aUrls?.length))` → `args.push()`
- 条件付き依存: `if (Services.appinfo.OS === "Darwin")` → `args.unshift()`
- 参照: `Services.appinfo.OS`, `aProfile.path`, `aUrls?.length`
- XPCOM: `Services.appinfo`

## SelectableProfileServiceClass.#notifyRunningInstances()
- 位置: async L918-932
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAllProfiles()`, `this.sendCommandLine()`
- 参照: `profile.id`, `profile.path`, `this.currentProfile?.id`

## SelectableProfileServiceClass.#updateTaskbar()
- 位置: async L934-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.getProfileCount()`
- 条件付き依存: `if (count > 1 && !this.#badge)` → `loadImage()`
- 条件付き依存: `if ("nsIMacDockSupport" in Ci)` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService(Ci.nsIMacDockSupport) .setBadgeImage()`
- 条件付き依存: `if ("nsIMacDockSupport" in Ci)` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService()`
- 条件付き依存: `if ("nsIWinTaskbar" in Ci)` → `this.#setOverlayIcon()`
- 条件付き依存: `if ("nsIWinTaskbar" in Ci)` → `TASKBAR_ICON_CONTROLLERS.get()`
- 条件付き依存: `if ("nsIWinTaskbar" in Ci)` → `iconController?.setOverlayIcon()`
- 参照: `Ci.nsIMacDockSupport`, `Services.startup.startingUp`, `lazy.EveryWindow.readyWindows`, `this.#badge`, `this.#badge.iconPaintContext`, `this.#badge.image`, `this.#currentProfile`, `this.#currentProfile.iconPaintContext`, `this.#currentProfile.name`
- XPCOM: `nsIMacDockSupport` / `@mozilla.org/widget/macdocksupport;1` / `Services.startup`

## SelectableProfileServiceClass.#updateTitlebar()
- 位置: async L978-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.profiles.profileCount.set()`, `this.getProfileCount()`
- 条件付き依存: `if (previousCount <= 1 || this.#cachedProfileCount <= 1)` → `win.gBrowser.updateTitlebar()`
- 参照: `lazy.EveryWindow.readyWindows`, `this.#cachedProfileCount`

## SelectableProfileServiceClass.databaseChanged()
- 位置: async L1002-1021
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateTaskbar()`, `this.#updateTitlebar()`
- 条件付き依存: `if (source === "local" || source === "shutdown")` → `this.#notifyRunningInstances()`
- 条件付き依存: `if (source != "local")` → `this.loadSharedPrefsFromDatabase()`
- 条件付き依存: `if (source != "startup")` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## SelectableProfileServiceClass.getColorsForDefaultTheme()
- 位置: L1033-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `computedStyles.getPropertyValue()`, `window.InspectorUtils.colorToRGBA()`, `window.getComputedStyle()`
- 参照: `bg.a`, `bg.b`, `bg.g`, `bg.r`, `fg.a`, `fg.b`, `fg.g`, `fg.r`, `lazy.NOVA_ENABLED`, `window.document.documentElement`
- XPCOM: `Services.wm`

## SelectableProfileServiceClass.enableTheme()
- 位置: async L1056-1086
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (!theme)` → `PROFILE_THEMES_MAP.get()`
- 条件付き依存: `if (themeEntry?.downloadURL)` → `lazy.AddonManager.getInstallForURL()`
- 条件付き依存: `if (themeEntry?.downloadURL)` → `themeInstall.install()`
- 条件付き依存: `if (themeEntry?.downloadURL)` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (theme)` → `theme.enable()`
- 条件付き依存: `if (!(theme))` → `console.warn()`
- 条件付き依存: `if (data?.theme)` → `Services.obs.notifyObservers()`
- 参照: `data?.theme`, `lazy.LightweightThemeManager.themeData`, `themeEntry.downloadURL`, `themeEntry?.downloadURL`
- XPCOM: `Services.obs`

## SelectableProfileServiceClass.extractThemeColors()
- 位置: L1094-1103
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (theme.id === DEFAULT_THEME_ID || !themeFg || !themeBg)` → `this.getColorsForDefaultTheme()`
- 参照: `theme.accentcolor`, `theme.icon_color`, `theme.id`, `theme.textcolor`, `theme.toolbarColor`, `theme.toolbar_text`

## SelectableProfileServiceClass.updateProfileThemeColors()
- 位置: L1110-1145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `this.extractThemeColors()`, `window.matchMedia()`
- 条件付き依存: `if (theme.id === DEFAULT_THEME_ID || !themeFg || !themeBg)` → `window.addEventListener()`
- 条件付き依存: `if (theme.id === DEFAULT_THEME_ID || !themeFg || !themeBg)` → `this.getColorsForDefaultTheme()`
- 参照: `data.darkTheme`, `data.theme`, `data?.theme`, `theme.id`, `this.currentProfile.theme`, `window.matchMedia("(-moz-system-dark-theme)").matches`
- XPCOM: `Services.wm`

## SelectableProfileServiceClass.themeObserver()
- 位置: L1154-1161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateProfileThemeColors()`
- 参照: `aSubject.wrappedJSObject`

## SelectableProfileServiceClass.matchMediaObserver()
- 位置: L1167-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getColorsForDefaultTheme()`
- 参照: `this.currentProfile.theme`, `this.currentProfile.theme.themeId`

## SelectableProfileServiceClass.lookAndFeelChanged()
- 位置: L1188-1191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateProfileThemeColors()`
- 参照: `lazy.LightweightThemeManager.themeData`

## SelectableProfileServiceClass.flushAllSharedPrefsToDatabase()
- 位置: async L1193-1197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.flushSharedPrefToDatabase()`
- 参照: `SelectableProfileServiceClass.permanentSharedPrefs`

## SelectableProfileServiceClass.flushSharedPrefToDatabase()
- 位置: async L1204-1233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileServiceClass.permanentSharedPrefs.includes()`, `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `Services.prefs.getIntPref()`, `Services.prefs.getPrefType()`, `Services.prefs.prefHasUserValue()`, `this.#observedPrefs.has()`, `this.#setDBPref()`
- 条件付き依存: `if (!this.#observedPrefs.has(prefName))` → `Services.prefs.addObserver()`
- 条件付き依存: `if (!this.#observedPrefs.has(prefName))` → `this.#observedPrefs.add()`
- 条件付き依存: `if ( !SelectableProfileServiceClass.permanentSharedPrefs.includes(prefName) && !Services.prefs.prefHasUserValue(prefName) )` → `this.#deleteDBPref()`
- 参照: `Ci.nsIPrefBranch.PREF_BOOL`, `Ci.nsIPrefBranch.PREF_INT`, `Ci.nsIPrefBranch.PREF_STRING`, `this.prefObserver`
- XPCOM: [`nsIPrefBranch`](../../../netwerk/base/nsINetUtil.idl.md) / `Services.prefs`

## SelectableProfileServiceClass.clearPrefObservers()
- 位置: L1235-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `this.#observedPrefs.clear()`
- 参照: `this.#observedPrefs`, `this.prefObserver`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.#maybeAddDAUGroupIDToDB()
- 位置: async L1257-1280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `this.getDBPref()`
- 条件付き依存: `if (writeToDB)` → `this.#setDBPref()`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.#maybeSetDAUGroupID()
- 位置: async L1293-1303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 条件付き依存: `if (dbValue < Services.prefs.getStringPref(DAU_GROUPID_PREF_NAME, ""))` → `lazy.ClientID.setUsageProfileGroupID()`
- 条件付き依存: `if (dbValue < Services.prefs.getStringPref(DAU_GROUPID_PREF_NAME, ""))` → `console.error()`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.loadSharedPrefsFromDatabase()
- 位置: async L1308-1375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileServiceClass.ignoredSharedPrefs.includes()`, `Services.prefs.addObserver()`, `Services.prefs.getCharPref()`, `permanentSharedPrefsSet.difference()`, `this.#observedPrefs.add()`, `this.clearPrefObservers()`, `this.flushSharedPrefToDatabase()`, `this.getAllDBPrefs()`
- 条件付き依存: `if ( name === GROUPID_PREF_NAME && value !== lazy.TelemetryUtils.knownProfileGroupID && value !== Services.prefs.getCharPref(GROUPID_PREF_NAME, "") )` → `lazy.ClientID.setProfileGroupID()`
- 条件付き依存: `if ( name === GROUPID_PREF_NAME && value !== lazy.TelemetryUtils.knownProfileGroupID && value !== Services.prefs.getCharPref(GROUPID_PREF_NAME, "") )` → `console.error()`
- 条件付き依存: `if (name === DAU_GROUPID_PREF_NAME)` → `this.#maybeSetDAUGroupID()`
- 条件付き依存: `if (name === DAU_GROUPID_PREF_NAME)` → `Services.prefs.addObserver()`
- 条件付き依存: `if (name === DAU_GROUPID_PREF_NAME)` → `this.#observedPrefs.add()`
- 条件付き依存: `if (value === null)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(value === null))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(value === null))` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (!(value === null))` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!(value === null))` → `Services.prefs.clearUserPref()`
- 参照: `SelectableProfileServiceClass.permanentSharedPrefs`, `lazy.TelemetryUtils.knownProfileGroupID`, `this.#observedPrefs`, `this.prefObserver`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.setDefaultProfileForGroup()
- 位置: async L1385-1404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.profilesDefault.updated.record()`, `newRootDir.equals()`, `this.#attemptFlushProfileService()`
- 参照: `aProfile.rootDir`, `this.#profileService.isListOutdated`, `this.currentProfile`, `this.groupToolkitProfile.rootDir`

## SelectableProfileServiceClass.setShowProfileSelectorWindow()
- 位置: async L1412-1415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#attemptFlushProfileService()`
- 参照: `this.groupToolkitProfile.showProfileSelector`

## SelectableProfileServiceClass.createProfileDirs()
- 位置: async L1427-1474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getDirectory()`, `IOUtils.makeDirectory()`, `PathUtils.join()`, `ProfilesDatastoreService.constructor.getDirectory()`, `Promise.all()`, `btoa()`, `lazy.CryptoUtils.generateRandomBytesLegacy()`, `lazy.DownloadPaths.sanitize()`, `salt.match()`, `salt.match(/\w/g).join()`, `salt.match(/\w/g).join("").slice()`
- 参照: `ProfilesDatastoreService.constructor.getDirectory("DefProfLRt").path`, `ProfilesDatastoreService.constructor.getDirectory("DefProfRt").path`

## SelectableProfileServiceClass.createProfileInitialFiles()
- 位置: async L1484-1509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `IOUtils.createUniqueFile()`, `IOUtils.writeJSON()`, `IOUtils.writeUTF8()`, `this.addSelectableProfilePrefs()`
- 条件付き依存: `if (!source)` → `console.error()`
- 参照: `Services.prefs.prefsJsPreamble`, `profileDir.path`
- XPCOM: `Services.prefs`

## SelectableProfileServiceClass.addSelectableProfilePrefs()
- 位置: async L1516-1545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `IOUtils.writeUTF8()`, `JSON.stringify()`, `PathUtils.join()`, `SelectableProfileServiceClass.ignoredSharedPrefs.includes()`, `prefsToAdd.set()`, `sharedPrefs .filter()`, `sharedPrefs .filter( pref => !SelectableProfileServiceClass.ignoredSharedPrefs.includes( pref.name ) ) .map()`, `this.getAllDBPrefs()`
- 参照: `AppConstants.platform`, `pref.name`, `this.storeID`

## SelectableProfileServiceClass.getRelativeProfilePath()
- 位置: L1554-1564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.constructor.getDirectory()`, `aProfilePath.getRelativePath()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `relativePath.replaceAll()`
- 参照: `AppConstants.platform`

## SelectableProfileServiceClass.#createProfile()
- 位置: async L1576-1610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.getAllProfiles()).map()`, `Math.floor()`, `Math.max()`, `Math.random()`, `Services.wm.getMostRecentBrowserWindow()`, `lazy.profilesLocalization.formatMessages()`, `this.createProfileDirs()`, `this.getAllProfiles()`, `this.getRelativeProfilePath()`, `this.insertProfile()`, `window?.matchMedia()`
- 条件付き依存: `if (!existingProfilePath)` → `this.createProfileInitialFiles()`
- 参照: `defaultName.value`, `originalName.value`, `p.id`, `profileData.name`, `profileData.path`, `this.#defaultAvatars`, `this.#defaultAvatars.length`, `window?.matchMedia("(-moz-system-dark-theme)").matches`
- XPCOM: `Services.wm`

## SelectableProfileServiceClass.maybeSetupDataStore()
- 位置: async L1617-1659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#init()`, `this.flushAllSharedPrefsToDatabase()`, `this.initProfilesData()`
- 条件付き依存: `if (!this.#currentProfile)` → `this.#createProfile()`
- 条件付き依存: `if (!this.#currentProfile)` → `this.setShowProfileSelectorWindow()`
- 条件付き依存: `if (Services.appinfo.OS === "Darwin")` → `lazy.setTimeout()`
- 条件付き依存: `if (Services.appinfo.OS === "Darwin")` → `SelectableProfileService.currentProfile.setAvatar()`
- 参照: `SelectableProfileService.currentProfile.avatar`, `Services.appinfo.OS`, `this.#connection`, `this.#currentProfile`, `this.groupToolkitProfile.rootDir`
- XPCOM: `Services.appinfo`

## SelectableProfileServiceClass.insertProfile()
- 位置: async L1672-1700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.notify()`, `keys.forEach()`, `rows[0].getResultByName()`, `this.#connection.execute()`, `this.getProfile()`
- 条件付き依存: `if (!(key in profileData))` → `missing.push()`
- 条件付き依存: `if (missing.length)` → `missing.join()`
- 参照: `missing.length`

## SelectableProfileServiceClass.deleteProfile()
- 位置: async L1702-1724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.notify()`, `this.#connection.execute()`, `this.#profileService.removeProfileFilesByPath()`
- 参照: `aProfile.id`, `aProfile.rootDir`, `this.currentProfile.id`

## SelectableProfileServiceClass.deleteCurrentProfile()
- 位置: async L1729-1784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.execute()`, `profiles.find()`, `this.#connection.executeBeforeShutdown()`, `this.currentProfile.removeDesktopShortcut()`, `this.getAllProfiles()`, `this.setDefaultProfileForGroup()`
- 条件付き依存: `if (profiles.length <= 1)` → `this.createNewProfile()`
- 条件付き依存: `if (profiles.length <= 1)` → `this.setShowProfileSelectorWindow()`
- 条件付き依存: `if (profiles.length <= 1)` → `this.getAllProfiles()`
- 条件付き依存: `if (AppConstants.MOZ_BACKGROUNDTASKS)` → `Cc["@mozilla.org/backgroundtasksrunner;1"].getService()`
- 条件付き依存: `if (AppConstants.MOZ_BACKGROUNDTASKS)` → `Services.dirsvc.get()`
- 条件付き依存: `if (AppConstants.MOZ_BACKGROUNDTASKS)` → `runner.runInDetachedProcess()`
- 参照: `AppConstants.MOZ_BACKGROUNDTASKS`, `Ci.nsIBackgroundTasksRunner`, `Ci.nsIFile`, `lazy.ExperimentAPI.profileId`, `localDir.path`, `p.id`, `profiles.length`, `rootDir.path`, `this.currentProfile.id`
- XPCOM: [`nsIBackgroundTasksRunner`](../../../toolkit/components/backgroundtasks/nsIBackgroundTasksRunner.idl.md) / [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/backgroundtasksrunner;1` / `Services.dirsvc`

## SelectableProfileServiceClass.updateProfile()
- 位置: async L1791-1808
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.notify()`, `aSelectableProfile.toDbObject()`, `this.#connection.execute()`
- 参照: `aSelectableProfile.id`, `this.#badge`, `this.#currentProfile`, `this.#currentProfile.id`

## SelectableProfileServiceClass.#updateProfilePath()
- 位置: async L1818-1835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `aProfileDir.initWithPath()`, `aUpdatedDir.initWithPath()`, `this.#connection.execute()`, `this.getRelativeProfilePath()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/file/local;1`

## SelectableProfileServiceClass.createNewProfile()
- 位置: async L1855-1867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#createProfile()`, `this.maybeSetupDataStore()`
- 条件付き依存: `if (launchProfile)` → `this.launchInstance()`

## SelectableProfileServiceClass.getAllProfiles()
- 位置: async L1875-1885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.#connection.executeCached("SELECT * FROM Profiles;")) .map()`, `p1.name.localeCompare()`, `this.#connection.executeCached()`
- 参照: `p2.name`, `this.#connection`

## SelectableProfileServiceClass.getCachedProfileCount()
- 位置: L1895-1897
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#cachedProfileCount`

## SelectableProfileServiceClass.getProfileCount()
- 位置: async L1905-1915
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rows[0]?.getResultByName()`, `this.#connection.executeCached()`
- 参照: `this.#connection`

## SelectableProfileServiceClass.getProfile()
- 位置: async L1924-1939
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connection.executeCached()`
- 参照: `this.#connection`

## SelectableProfileServiceClass.getProfileByName()
- 位置: async L1948-1963
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connection.execute()`
- 参照: `this.#connection`

## SelectableProfileServiceClass.getProfileByPath()
- 位置: async L1971-1987
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connection.execute()`, `this.getRelativeProfilePath()`
- 参照: `this.#connection`

## SelectableProfileServiceClass.getPrefValueFromRow()
- 位置: L1991-1998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.getResultByName()`

## SelectableProfileServiceClass.getAllDBPrefs()
- 位置: async L2005-2016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await this.#connection.executeCached("SELECT * FROM SharedPrefs;") ).map()`, `row.getResultByName()`, `this.#connection.executeCached()`, `this.getPrefValueFromRow()`

## SelectableProfileServiceClass.getDBPref()
- 位置: async L2025-2038
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connection.execute()`, `this.getPrefValueFromRow()`
- 参照: `rows.length`

## SelectableProfileServiceClass.setDBPref()
- 位置: async L2040-2046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setDBPref()`
- 参照: `Cu.isInAutomation`

## SelectableProfileServiceClass.#setDBPref()
- 位置: async L2054-2065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.notify()`, `this.#connection.execute()`

## SelectableProfileServiceClass.trackPref()
- 位置: async L2068-2070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.flushSharedPrefToDatabase()`

## SelectableProfileServiceClass.deleteDBPref()
- 位置: async L2072-2078
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deleteDBPref()`
- 参照: `Cu.isInAutomation`

## SelectableProfileServiceClass.#deleteDBPref()
- 位置: async L2085-2096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProfilesDatastoreService.notify()`, `this.#connection.executeCached()`

## CommandLineHandler.findDefaultProfilePath()
- 位置: async L2117-2171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/xpcom/ini-parser-factory;1"] .getService()`, `Cc["@mozilla.org/xpcom/ini-parser-factory;1"] .getService(Ci.nsIINIParserFactory) .createINIParser()`, `IOUtils.readUTF8()`, `PathUtils.join()`, `ProfilesDatastoreService.constructor.getDirectory()`, `console.error()`, `iniParser.getString()`, `iniParser.initFromString()`
- 条件付き依存: `if (isRelative)` → `Cc["@mozilla.org/file/local;1"].createInstance()`
- 条件付き依存: `if (isRelative)` → `profileDir.setRelativeDescriptor()`
- 参照: `Ci.nsIFile`, `Ci.nsIINIParserFactory`, `SelectableProfileService.storeID`, `profileDir.path`, `profilesRoot.path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / [`nsIINIParserFactory`](../../../xpcom/ds/nsIINIParser.idl.md) / `@mozilla.org/file/local;1` / `@mozilla.org/xpcom/ini-parser-factory;1`

## CommandLineHandler.openUrls()
- 位置: L2180-2212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/browser/final-clh;1"].createInstance()`, `Cu.createCommandLine()`, `Services.dirsvc.get()`, `console.error()`, `handler.handle()`
- 参照: `Ci.nsICommandLine.STATE_REMOTE_EXPLICIT`, `Ci.nsICommandLineHandler`, `Ci.nsIFile`, `args.length`
- XPCOM: [`nsICommandLine`](../nsIBrowserHandler.idl.md) / [`nsICommandLineHandler`](../../../toolkit/components/commandlines/nsICommandLineHandler.idl.md) / [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/browser/final-clh;1` / `Services.dirsvc`

## CommandLineHandler.redirectCommandLine()
- 位置: async L2214-2239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectableProfileService.execProcess()`, `this.findDefaultProfilePath()`
- 条件付き依存: `if (defaultPath)` → `this.openUrls()`
- 条件付き依存: `if (defaultPath)` → `SelectableProfileService.sendCommandLine()`
- 参照: `SelectableProfileService.currentProfile?.path`

## CommandLineHandler.handle()
- 位置: L2241-2302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cmdLine.handleFlag()`
- 条件付き依存: `if (SelectableProfileService.initialized)` → `SelectableProfileService.databaseChanged("remote").catch()`
- 条件付き依存: `if (SelectableProfileService.initialized)` → `SelectableProfileService.databaseChanged()`
- 条件付き依存: `if ( cmdLine.handleFlag(COMMAND_LINE_ACTIVATE, true) && cmdLine.state != Ci.nsICommandLine.STATE_INITIAL_LAUNCH )` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if (win)` → `win.focus()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT && Services.appinfo.OS === "Darwin" )` → `args.push()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT && Services.appinfo.OS === "Darwin" )` → `cmdLine.getArgument()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT && Services.appinfo.OS === "Darwin" )` → `this.redirectCommandLine(args).catch()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT && Services.appinfo.OS === "Darwin" )` → `this.redirectCommandLine()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT && Services.appinfo.OS === "Darwin" )` → `cmdLine.removeArguments()`
- 参照: `Ci.nsICommandLine.STATE_INITIAL_LAUNCH`, `Ci.nsICommandLine.STATE_REMOTE_EXPLICIT`, `SelectableProfileService.initialized`, `SelectableProfileService.isEnabled`, `Services.appinfo.OS`, `cmdLine.length`, `cmdLine.preventDefault`, `cmdLine.state`, `console.error`
- XPCOM: [`nsICommandLine`](../nsIBrowserHandler.idl.md) / `Services.appinfo` / `Services.wm`
