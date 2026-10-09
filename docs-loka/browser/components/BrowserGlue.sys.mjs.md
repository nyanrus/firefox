# browser/components/BrowserGlue.sys.mjs

source: browser/components/BrowserGlue.sys.mjs
source-hash: 4a292baaec92880c7a17709b207117edec1920c4
lines: 1720

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/weave/service;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyServiceGetters()`

## BrowserGlue()
- 位置: L163-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`, `this._init()`
- 参照: `Ci.nsIUserIdleService`
- XPCOM: `nsIUserIdleService`

## BG__setPrefToSaveSession()
- 位置: L179-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.savePrefFile()`
- 条件付き依存: `if (!lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._saveSession`
- XPCOM: `Services.prefs`

## BG_observe()
- 位置: async L198-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.console.logStringMessage()`, `Services.console.reset()`, `Services.obs.removeObserver()`, `addons.some()`, `console.error()`, `lazy.AddonManager.getAddonsByIDs()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.DownloadsViewableInternally.register()`, `lazy.LaunchOnLogin.isSupported()`, `lazy.PdfJs.init()`, `lazy.PlacesBrowserStartup.backendInitComplete()`, `lazy.SearchService.getEngineById()`, `subject.QueryInterface()`, `subject.findFlag()`, `subject.handleFlag()`, `this._beforeUIStartup()`, `this._dispose()`, `this._earlyBlankFirstPaint()`, `this._onFirstWindowLoaded()`, `this._onQuitApplicationGranted()`, `this._onQuitRequest()`, `this._onSafeModeRestart()`, `this._onWindowsRestored()`, `this._openPreferences()`, `this._setPrefToSaveSession()`
- 条件付き依存: `if (OBSERVE_LASTWINDOW_CLOSE_TOPICS)` → `this._onQuitRequest()`
- 条件付き依存: `if (OBSERVE_LASTWINDOW_CLOSE_TOPICS)` → `this._setPrefToSaveSession()`
- 条件付き依存: `if (data == "places-browser-init-complete")` → `lazy.PlacesBrowserStartup.notifyIfInitializationComplete()`
- 条件付き依存: `if (data == "add-breaches-sync-handler")` → `this._addBreachesSyncHandler()`
- 条件付き依存: `if (!linkHandled.data)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!linkHandled.data)` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (win)` → `JSON.parse()`
- 条件付き依存: `if (win)` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (win)` → `win.openTrustedLinkIn()`
- 条件付き依存: `if (addons.some(addon => addon))` → `this._notifyUnsignedAddonsDisabled()`
- 条件付き依存: `if (lazy.LaunchOnLogin.isSupported())` → `lazy.StartupOSIntegration.checkForLaunchOnLogin()`
- 参照: `BrowserInitState.isLaunchOnLogin`, `BrowserInitState.isTaskbarTab`, `Ci.nsISupportsPRBool`, `Ci.nsISupportsString`, `JSON.parse(data).disabled`, `data.href`, `linkHandled.data`, `subject.QueryInterface(Ci.nsISupportsString).data`, `subject.data`, `this._isNewProfile`, `win.gBrowser.selectedBrowser`
- XPCOM: [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `Services.console` / `Services.obs`

## BG__init()
- 位置: L342-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DesktopActorRegistry.init()`, `os.addObserver()`
- 条件付き依存: `if (OBSERVE_LASTWINDOW_CLOSE_TOPICS)` → `os.addObserver()`
- 参照: `Services.obs`
- XPCOM: `Services.obs`

## BG__dispose()
- 位置: L370-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutHomeStartupCache.uninit()`, `lazy.ContentBlockingPrefs.uninit()`
- 条件付き依存: `if (this._lateTasksIdleObserver)` → `this._userIdleService.removeIdleObserver()`
- 条件付き依存: `if (this._gmpInstallManager)` → `this._gmpInstallManager.uninit()`
- 参照: `this._gmpInstallManager`, `this._lateTasksIdleObserver`

## BG__beforeUIStartup()
- 位置: L393-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.prefHasUserValue()`, `lazy.BrowserUtils.callModulesFromCategory()`, `lazy.DistributionManagement.applyCustomizations()`, `lazy.SessionStartup.init()`, `this._migrateUI()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.ww.openWindow()`
- 条件付き依存: `if (!Services.prefs.prefHasUserValue(PREF_PDFJS_ISDEFAULT_CACHE_STATE))` → `lazy.PdfJs.checkIsDefault()`
- 条件付き依存: `if (!AppConstants.NIGHTLY_BUILD && this._isNewProfile)` → `lazy.FormAutofillUtils.setOSAuthEnabled()`
- 条件付き依存: `if (!AppConstants.NIGHTLY_BUILD && this._isNewProfile)` → `lazy.LoginHelper.setOSAuthEnabled()`
- 参照: `AppConstants.NIGHTLY_BUILD`, `Services.appinfo.inSafeMode`, `this._isNewProfile`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.prefs` / `Services.ww`

## _checkForOldBuildUpdates()
- 位置: L429-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( AppConstants.MOZ_UPDATER && Services.prefs.getBoolPref("app.update.checkInstallTime") )` → `new Date().getTime()`
- 条件付き依存: `if ( AppConstants.MOZ_UPDATER && Services.prefs.getBoolPref("app.update.checkInstallTime") )` → `buildID.slice()`
- 条件付き依存: `if ( AppConstants.MOZ_UPDATER && Services.prefs.getBoolPref("app.update.checkInstallTime") )` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (buildDate + acceptableAge < today)` → `Cc["@mozilla.org/updates/update-service;1"] .getService(Ci.nsIApplicationUpdateService) .checkForBackgroundUpdates()`
- 条件付き依存: `if (buildDate + acceptableAge < today)` → `Cc["@mozilla.org/updates/update-service;1"] .getService()`
- 参照: `AppConstants.MOZ_UPDATER`, `Ci.nsIApplicationUpdateService`, `Services.appinfo.appBuildID`
- XPCOM: [`nsIApplicationUpdateService`](../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-service;1` → `UpdateService` (toolkit/mozapps/update/components.conf) / `Services.appinfo` / `Services.prefs`

## _onSafeModeRestart()
- 位置: async L463-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.prompt.asyncConfirmEx()`, `lazy.gBrandBundle.GetStringFromName()`, `rv.get()`, `strings.GetStringFromName()`, `strings.formatStringFromName()`
- 条件付き依存: `if (!cancelQuit.data)` → `Services.startup.restartInSafeMode()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIPrompt.MODAL_TYPE_INTERNAL_WINDOW`, `Ci.nsISupportsPRBool`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `cancelQuit.data`, `lazy.gBrowserBundle`, `window.browsingContext`
- XPCOM: [`nsIAppStartup`](../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsIPrompt`](../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs` / `Services.prompt` / `Services.startup`

## _notifyUnsignedAddonsDisabled()
- 位置: L512-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.gNavigatorBundle.getString()`, `win.gNotificationBox.appendNotification()`
- 参照: `win.gNotificationBox.PRIORITY_WARNING_MEDIUM`

## callback()
- 位置: L531-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.BrowserAddonUI.openAddonsMgr()`

## _earlyBlankFirstPaint()
- 位置: L549-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.importESModule()`, `ChromeUtils.now()`, `Glean.browserTimings.startupTimeline.blankWindowShown.set()`, `Services.telemetry.msSinceProcessStart()`, `Services.ww.openWindow()`, `TelemetryTimestamps.add()`, `appWin.showInitialViewer()`, `cmdLine.findFlag()`, `docElt.setAttribute()`, `getValue()`, `lazy.StartupOSIntegration.isPrivateBrowsingAllowedInRegistry()`, `shouldCreateWindow()`, `win.docShell.treeOwner .QueryInterface()`, `win.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (hiddenTitlebar)` → `win.windowUtils.setCustomTitlebar()`
- 条件付き依存: `if (sizemode == "maximized")` → `docElt.setAttribute()`
- 条件付き依存: `if (!(sizemode == "maximized"))` → `win.resizeTo()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `Services.appinfo.drawInTitlebar`, `appWin.outerToInnerHeightDifferenceInCSSPixels`, `appWin.outerToInnerWidthDifferenceInCSSPixels`, `win.document.documentElement`, `win.openTime`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / `Services.appinfo` / `Services.telemetry` / `Services.ww`

## shouldCreateWindow()
- 位置: L552-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.shouldResistFingerprinting()`, `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `cmdLine.findFlag()`, `getValue()`
- 参照: `AppConstants.platform`, `Services.startup.showedPreXULSkeletonUI`, `Services.startup.wasSilentlyStarted`
- XPCOM: `Services.prefs` / `Services.startup`

## getValue()
- 位置: L701-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.xulStore.getValue()`
- 参照: `AppConstants.BROWSER_CHROME_URL`
- XPCOM: `Services.xulStore`

## _firstWindowTelemetry()
- 位置: L710-713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.gfxDisplay.scaling.accumulateSingleSample()`
- 参照: `aWindow.devicePixelRatio`

## BG__onFirstWindowLoaded()
- 位置: L716-754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `channel.listen()`, `lazy.BrowserUtils.callModulesFromCategory()`, `this._checkForOldBuildUpdates()`, `this._firstWindowTelemetry()`
- 条件付き依存: `if (data.command == "request")` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (data.command == "request")` → `Troubleshoot.snapshot().then()`
- 条件付き依存: `if (data.command == "request")` → `Troubleshoot.snapshot()`
- 条件付き依存: `if (data.command == "request")` → `channel.send()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue("services.sync.username"))` → `lazy.WeaveService.init()`
- 参照: `data.command`, `lazy.WebChannel`, `snapshotData.crashes`, `snapshotData.modifiedPreferences`, `snapshotData.printingPreferences`
- XPCOM: `Services.prefs`

## _onQuitApplicationGranted()
- 位置: L763-805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.trackStartupCrashEnd()`, `console.error()`, `failureHandler()`, `lazy.BrowserUtils.callModulesFromCategory()`, `task()`, `this._setPrefToSaveSession()`
- 参照: `Services.fog`
- XPCOM: `Services.fog` / `Services.startup`

## failureHandler()
- 位置: L764-774
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (Cu.isInAutomation)` → `Cc["@mozilla.org/xpcom/debug;1"] .getService(Ci.nsIDebug2) .abort()`
- 条件付き依存: `if (Cu.isInAutomation)` → `Cc["@mozilla.org/xpcom/debug;1"] .getService()`
- 参照: `Ci.nsIDebug2`, `Cu.isInAutomation`, `ex.fileName`, `ex.filename`, `ex.lineNumber`
- XPCOM: [`nsIDebug2`](../../xpcom/base/nsIDebug2.idl.md) / `@mozilla.org/xpcom/debug;1`

## _monitorWebcompatReporterPref()
- 位置: L807-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (enabled && !addon.isActive)` → `addon.enable()`
- 条件付き依存: `if (!enabled && addon.isActive)` → `addon.disable()`
- 参照: `addon.isActive`
- XPCOM: `Services.prefs`

## BG__onWindowsRestored()
- 位置: L825-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUsageTelemetry.init()`, `lazy.ExtensionsUI.init()`, `lazy.Interactions.init()`, `lazy.PageDataService.init()`, `lazy.PreonboardingSplash.maybeShowStartupSplash()`, `lazy.Sanitizer.onStartup()`, `lazy.SearchSERPTelemetry.init()`, `lazy.SessionWindowUI.maybeShowRestoreSessionInfoBar()`, `this._monitorWebcompatReporterPref()`, `this._scheduleStartupIdleTasks()`, `this._userIdleService.addIdleObserver()`
- 条件付き依存: `if (!(AppConstants.MOZ_REQUIRE_SIGNING))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (signingRequired)` → `lazy.AddonManager.getStartupChanges()`
- 条件付き依存: `if (signingRequired)` → `lazy.AddonManager.getAddonsByIDs(disabledAddons).then()`
- 条件付き依存: `if (signingRequired)` → `lazy.AddonManager.getAddonsByIDs()`
- 条件付き依存: `if (addon.signedState <= lazy.AddonManager.SIGNEDSTATE_MISSING)` → `this._notifyUnsignedAddonsDisabled()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.CrashFileCleaner.init()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.CrashFileCleaner.scheduleCleanup()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.UnsubmittedCrashHandler.init()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.UnsubmittedCrashHandler.scheduleCheckForUnsubmittedCrashReports()`
- 条件付き依存: `if (AppConstants.ASAN_REPORTER)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (AppConstants.ASAN_REPORTER)` → `AsanReporter.init()`
- 条件付き依存: `if (AppConstants.ENABLE_WEBDRIVER)` → `lazy.RemoteControlBanner.init()`
- 参照: `AppConstants.ASAN_REPORTER`, `AppConstants.ENABLE_WEBDRIVER`, `AppConstants.MOZ_CRASHREPORTER`, `AppConstants.MOZ_REQUIRE_SIGNING`, `addon.signedState`, `lazy.AddonManager.SIGNEDSTATE_MISSING`, `lazy.AddonManager.STARTUP_CHANGE_DISABLED`, `lazy.MigrationUtils`, `this._lateTasksIdleObserver`, `this._windowsWereRestored`
- XPCOM: `Services.prefs`

## this._lateTasksIdleObserver()
- 位置: L883-892
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "idle")` → `idleService.removeIdleObserver()`
- 条件付き依存: `if (topic == "idle")` → `this._scheduleBestEffortUserIdleTasks()`
- 参照: `this._lateTasksIdleObserver`

## _scheduleStartupIdleTasks()
- 位置: L928-1227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.BrowserUtils.callModulesFromCategory()`, `runIdleTasks()`
- 参照: `AppConstants.MOZ_TELEMETRY_REPORTING`, `AppConstants.MOZ_UPDATER`, `AppConstants.MOZ_UPDATE_AGENT`, `AppConstants.platform`
- XPCOM: `Services.prefs`

## runIdleTasks()
- 位置: L929-955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.now()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task.task()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `console.error()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.addProfilerMarker()`
- 参照: `Services.startup.shuttingDown`, `task.condition`, `task.name`, `task.timeout`
- XPCOM: `Services.startup`

## task()
- 位置: L966-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SafeBrowsing.init()`

## task()
- 位置: L985-995
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PushService.wrappedJSObject.ensureReady()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `ex.result`

## task()
- 位置: L1004-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`
- 参照: `Services.logins`
- XPCOM: `Services.logins`

## task()
- 位置: L1017-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addBreachAlertsPrefObserver()`

## task()
- 位置: L1024-1026
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeShowDefaultBrowserPrompt()`

## task()
- 位置: L1031-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ScreenshotsUtils.monitorScreenshotsPref()`

## task()
- 位置: L1038-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy.setTimeout()`
- 参照: `Services.startup.trackStartupCrashEnd`
- XPCOM: `Services.startup` / `Services.tm`

## task()
- 位置: L1049-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/handler-service;1" ].getService()`, `handlerService.asyncInit()`
- 参照: `Ci.nsIHandlerService`
- XPCOM: [`nsIHandlerService`](../../uriloader/exthandler/nsIHandlerService.idl.md) / `@mozilla.org/uriloader/handler-service;1`

## task()
- 位置: L1059-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.WebProtocolHandlerRegistrar.prototype.init()`

## task()
- 位置: L1067-1090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `new lazy.TRRRacer().run()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref(enabledPref, false)))` → `Services.prefs.addObserver()`
- 参照: `lazy.TRRRacer`
- XPCOM: `Services.prefs`

## observer()
- 位置: L1078-1088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.removeObserver()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `new lazy.TRRRacer().run()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `Services.prefs.setBoolPref()`
- 参照: `lazy.TRRRacer`
- XPCOM: `Services.prefs`

## task()
- 位置: async L1096-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( // Not in automation: the button changes CUI state, // breaking tests. Check this first, so that the module // doesn't load if it doesn't have to. !Cu.isInA...)` → `lazy.AWToolbarButton.maybeAddSetupButton()`
- 参照: `Cu.isInAutomation`, `lazy.AWToolbarButton.hasToolbarButtonEnabled`

## task()
- 位置: L1111-1113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterDefaultConfig()`, `lazy.ASRouterNewTabHook.createInstance()`

## task()
- 位置: async L1119-1138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/updates/update-service-stub;1" ].getService()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `BackgroundUpdate.scheduleFirefoxMessagingSystemTargetingSnapshotting()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `console.error()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `BackgroundUpdate.maybeScheduleBackgroundUpdateTask()`
- 参照: `Ci.nsIApplicationUpdateServiceStub`, `updateServiceStub.updateDisabledForTesting`
- XPCOM: [`nsIApplicationUpdateServiceStub`](../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-service-stub;1` → `UpdateServiceStub` (toolkit/mozapps/update/components.conf)

## task()
- 位置: L1144-1149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/login-detection-service;1" ].getService()`, `loginDetection.init()`
- 参照: `Ci.nsILoginDetectionService`
- XPCOM: [`nsILoginDetectionService`](../../dom/ipc/nsILoginDetectionService.idl.md) / `@mozilla.org/login-detection-service;1`

## task()
- 位置: async L1155-1160
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.WeaveService.enabled)` → `lazy.WeaveService.whenLoaded()`
- 条件付き依存: `if (lazy.WeaveService.enabled)` → `lazy.WeaveService.Weave.Service.scheduler.autoConnect()`
- 参照: `lazy.WeaveService.enabled`

## task()
- 位置: L1166-1171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## task()
- 位置: async L1177-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DAPIncrementality.startup()`, `lazy.DAPTelemetrySender.startup()`, `lazy.DAPVisitCounter.startup()`

## task()
- 位置: L1187-1189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.ensureJSOracleStarted()`

## task()
- 位置: L1195-1197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BackupService.init()`

## task()
- 位置: L1206-1206
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.sysinfo.diskInfo`
- XPCOM: `Services.sysinfo`

## task()
- 位置: L1211-1221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserInitState._resolveStartupIdleTask()`, `ChromeUtils.idleDispatch()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## _scheduleBestEffortUserIdleTasks()
- 位置: L1242-1288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`, `function RemoteSettingsInit() { lazy.RemoteSettings.init(); this._addBreachesSyncHandler(); }.bind()`, `lazy.BrowserUtils.callModulesFromCategory()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.now()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `console.error()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.addProfilerMarker()`
- 参照: `Services.startup.shuttingDown`, `task.name`
- XPCOM: `Services.startup`

## GMPInstallManagerSimpleCheckAndInstall()
- 位置: L1244-1252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `this._gmpInstallManager.simpleCheckAndInstall()`, `this._gmpInstallManager.simpleCheckAndInstall().catch()`
- 参照: `this._gmpInstallManager`

## RemoteSettingsInit()
- 位置: L1254-1257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings.init()`, `this._addBreachesSyncHandler()`

## searchBackgroundChecks()
- 位置: L1259-1261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.runBackgroundChecks()`

## _addBreachesSyncHandler()
- 位置: L1290-1299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "signon.management.page.breach-alerts.enabled", false ) )` → `lazy.LoginBreaches.subscribeToBreachUpdates()`
- XPCOM: `Services.prefs`

## _addBreachAlertsPrefObserver()
- 位置: L1301-1313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `clearVulnerablePasswordsIfBreachAlertsDisabled()`
- XPCOM: `Services.prefs`

## clearVulnerablePasswordsIfBreachAlertsDisabled()
- 位置: async L1303-1307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(BREACH_ALERTS_PREF))` → `lazy.LoginBreaches.clearAllPotentiallyVulnerablePasswords()`
- XPCOM: `Services.prefs`

## _registerQuitSource()
- 位置: L1316-1318
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._quitSource`

## BG__onQuitRequest()
- 位置: L1320-1507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prompt.confirmEx()`, `lazy.BrowserWindowTracker.getTopWindow()`, `win.gBrowser.tabLocalization.formatMessagesSync()`, `win.gDialogBox.replaceDialogIfOpen()`
- 条件付き依存: `if (shouldWarnForShortcut)` → `win.document.getElementById()`
- 条件付き依存: `if (shouldWarnForShortcut)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (showCloseCurrentTabOption)` → `win.gBrowser.tabLocalization.formatMessagesSync()`
- 条件付き依存: `if (shouldWarnForShortcut)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(shouldWarnForShortcut))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (buttonPressed === 2)` → `win.gBrowser.removeTab()`
- 参照: `Ci.nsISupportsPRBool`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_POS_1_IS_SECONDARY`, `Services.prompt.BUTTON_POS_2`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `aCancelQuit.data`, `checkboxLabel.value`, `closeTabButtonLabel.value`, `lazy.BrowserWindowTracker.orderedWindows`, `quitButtonLabel.value`, `tabbrowser.pinnedTabCount`, `tabbrowser.visibleTabs.length`, `this._quitSource`, `title.value`, `warnOnClose.value`, `win.closed`, `win.gBrowser`, `win.gBrowser.selectedTab`, `win.gBrowser.visibleTabs.length`
- XPCOM: [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `Services.prefs` / `Services.prompt`

## _migrateUI()
- 位置: L1509-1525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (this._isNewProfile)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (profileDataVersion < APP_DATA_VERSION)` → `lazy.ProfileDataUpgrader.upgrade()`
- 参照: `this._isNewProfile`
- XPCOM: `Services.prefs`

## _showUpgradeDialog()
- 位置: async L1527-1564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.addTabsProgressListener()`, `gBrowser.addTrustedTab()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.OnboardingMessageProvider.getUpgradeMessage()`
- 参照: `gBrowser.selectedTab`

## onLocationChange()
- 位置: L1537-1552
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aBrowser === tab.linkedBrowser)` → `lazy.setTimeout()`
- 条件付き依存: `if (aBrowser === tab.linkedBrowser)` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (aBrowser === tab.linkedBrowser)` → `gBrowser.removeTabsProgressListener()`
- 参照: `tab.linkedBrowser`

## _showSetToDefaultSpotlight()
- 位置: async L1566-1598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.browser.setDefaultResult.accumulateSingleSample()`, `Math.floor()`, `Math.floor(Date.now() / 1000).toString()`, `Services.prefs.setCharPref()`, `console.error()`, `lazy.Spotlight.showSpotlightDialog()`, `shellService.isDefaultBrowserAsync()`, `win.getShellService()`
- 参照: `browser.documentGlobal`, `shellService.shouldCheckDefaultBrowser`
- XPCOM: `Services.prefs`

## _maybeShowDefaultBrowserPrompt()
- 位置: async L1600-1696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.upgradeDialog.triggerReason.record()`, `Services.policies.isAllowed()`, `Services.prefs.getDefaultBranch()`, `Services.prefs.getIntPref()`, `await()`, `defaultPrefs.getBoolPref()`, `lazy.ASRouter.sendTriggerMessage()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.DefaultBrowserCheck.willCheckDefaultBrowser()`, `lazy.NimbusFeatures.upgradeDialog.getVariable()`, `lazy.TelemetryReportingPolicy.ensureUserIsNotified()`
- 条件付き依存: `if (!dialogReason)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!dialogReason)` → `this._showUpgradeDialog()`
- 条件付き依存: `if (willPrompt)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (willPrompt)` → `setToDefaultFeature.ready()`
- 条件付き依存: `if (willPrompt)` → `setToDefaultFeature.recordExposureEvent()`
- 条件付き依存: `if (willPrompt)` → `setToDefaultFeature.getAllVariables()`
- 条件付き依存: `if (showSpotlightPrompt && message)` → `this._showSetToDefaultSpotlight()`
- 条件付き依存: `if (willPrompt)` → `lazy.DefaultBrowserCheck.prompt()`
- 参照: `lazy.ASRouter.waitForInitialized`, `lazy.BrowserHandler.majorUpgrade`, `lazy.BrowserWindowTracker.getTopWindow({ allowFromInactiveWorkspace: true, })?.gBrowser.selectedBrowser`, `lazy.NimbusFeatures.setToDefaultPrompt`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.policies` / `Services.prefs`

## _openPreferences()
- 位置: L1701-1713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (chromeWindow)` → `chromeWindow.openPreferences()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Services.appShell.hiddenDOMWindow.openPreferences()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.appShell`
