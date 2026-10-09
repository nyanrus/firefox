# browser/components/shell/ShellService.sys.mjs

source: browser/components/shell/ShellService.sys.mjs
source-hash: e6b3089bd165da3ecb53e7c0771be5803cc8480e
lines: 1440

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `lazy.log.warn()`

## canSetDesktopBackground()
- 位置: L107-122
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.shellService)` → `this.shellService.QueryInterface()`
- 参照: `AppConstants.platform`, `Ci.nsIGNOMEShellService`, `linuxShellService.canSetDesktopBackground`, `this.shellService`
- XPCOM: [`nsIGNOMEShellService`](nsIGNOMEShellService.idl.md)

## getOSUserProfileAgeInDays()
- 位置: async L128-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.stat()`, `Math.round()`, `Services.dirsvc.get()`
- 参照: `(await IOUtils.stat(Services.dirsvc.get("Home", Ci.nsIFile).path)) .creationTime`, `Ci.nsIFile`, `Services.dirsvc.get("Home", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `Services.dirsvc`

## shouldCheckDefaultBrowser()
- 位置: L152-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this._checkedThisSession`
- XPCOM: `Services.prefs`

## shouldCheckDefaultBrowser()
- 位置: L166-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## attemptedSetDefaultThisSession()
- 位置: L174-176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._attemptedSetDefaultThisSession`

## isDefaultBrowser()
- 位置: L178-189
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.shellService)` → `this.shellService.isDefaultBrowser()`
- 参照: `this._checkedThisSession`, `this.shellService`

## isDefaultBrowserAsync()
- 位置: L199-210
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.shellService)` → `this.shellService.isDefaultBrowserAsync()`
- 参照: `this._checkedThisSession`, `this.shellService`

## _userChoiceImpossibleTelemetryResult()
- 位置: L220-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shellService.QueryInterface()`, `winShellService.checkAllProgIDsExist()`, `winShellService.checkBrowserUserChoiceHashes()`
- 参照: `Ci.nsIWindowsShellService`
- XPCOM: [`nsIWindowsShellService`](nsIWindowsShellService.idl.md)

## isOneClickSetDefaultEnabled()
- 位置: L253-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this._userChoiceImpossibleTelemetryResult()`, `this.canRenameUserChoiceAssociationKey()`, `this.isDefaultBrowser()`, `this.isUserChoiceProtectionDriverRunning()`
- 参照: `AppConstants.platform`, `this.shellService`
- XPCOM: `Services.prefs`

## _shouldSetDefaultPDFHandler()
- 位置: L290-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.shellService.getVariable()`, `lazy.log.debug()`, `this.getDefaultPDFHandler()`
- 条件付き依存: `if (handler === null)` → `lazy.log.warn()`
- 条件付き依存: `if (!handler.registered)` → `lazy.log.debug()`
- 条件付き依存: `if (handler.knownBrowser)` → `lazy.log.debug()`
- 参照: `handler.knownBrowser`, `handler.registered`

## getDefaultPDFHandler()
- 位置: L333-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentProgID.startsWith()`, `knownBrowserPrefixes.find()`, `lazy.log.warn()`, `this.queryCurrentDefaultHandlerFor()`
- 条件付き依存: `if (knownBrowserPrefix)` → `lazy.log.debug()`

## setAsDefaultUserChoice()
- 位置: async L387-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.setDefaultUserChoiceResult[telemetryResult].add()`, `lazy.NimbusFeatures.shellService.getVariable()`, `lazy.XreDirProvider.getInstallHash()`, `lazy.log.info()`, `this._throwForWDBAResult()`, `this._userChoiceImpossibleTelemetryResult()`, `this.defaultAgent.setDefaultBrowserUserChoiceAsync()`
- 条件付き依存: `if ( lazy.NimbusFeatures.shellService.getVariable("setDefaultPDFHandler") )` → `this._shouldSetDefaultPDFHandler()`
- 条件付き依存: `if (this._shouldSetDefaultPDFHandler())` → `lazy.log.info()`
- 条件付き依存: `if (this._shouldSetDefaultPDFHandler())` → `extraFileExtensions.push()`
- 条件付き依存: `if (!(this._shouldSetDefaultPDFHandler()))` → `lazy.log.info()`
- 参照: `AppConstants.platform`, `Cr.NS_ERROR_FAILURE`, `Glean.browser.setDefaultUserChoiceResult`, `err.result`, `ex.telemetryResult`

## setAsDefaultPDFHandlerUserChoice()
- 位置: async L441-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.XreDirProvider.getInstallHash()`, `this._throwForWDBAResult()`, `this.defaultAgent.setDefaultExtensionHandlersUserChoice()`
- 参照: `AppConstants.platform`, `Cr.NS_ERROR_FAILURE`, `err.result`

## _maybeShowSetDefaultGuidanceNotification()
- 位置: async L457-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.shellService.getVariable()`
- 条件付き依存: `if ( lazy.NimbusFeatures.shellService.getVariable( "setDefaultGuidanceNotifications" ) && // Disable showing toast notification from Firefox Background Tasks. !l...)` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if ( lazy.NimbusFeatures.shellService.getVariable( "setDefaultGuidanceNotifications" ) && // Disable showing toast notification from Firefox Background Tasks. !l...)` → `lazy.ASRouter.sendTriggerMessage()`
- 参照: `lazy.ASRouter.waitForInitialized`, `lazy.BackgroundTasks?.isBackgroundTaskMode`
- XPCOM: `Services.wm`

## setDefaultBrowser()
- 位置: async L475-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`, `this._maybeShowSetDefaultGuidanceNotification()`, `this.shellService.setDefaultBrowser()`
- 条件付き依存: `if (!Services.policies.isAllowed("setDefaultBrowser"))` → `lazy.log.warn()`
- 条件付き依存: `if ( AppConstants.platform == "win" && Services.prefs.getBoolPref("browser.shell.setDefaultBrowserUserChoice") )` → `this.setAsDefaultUserChoice()`
- 条件付き依存: `if ( AppConstants.platform == "win" && Services.prefs.getBoolPref("browser.shell.setDefaultBrowserUserChoice") )` → `lazy.log.warn()`
- 参照: `AppConstants.platform`, `this._attemptedSetDefaultThisSession`
- XPCOM: `Services.policies` / `Services.prefs`

## setAsDefault()
- 位置: async L505-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.isUserDefault[!setAsDefaultError ? "true" : "false"].add()`, `Glean.browser.setDefaultError[setAsDefaultError ? "true" : "false"].add()`, `ShellService.setDefaultBrowser()`, `console.error()`
- 参照: `Glean.browser.isUserDefault`, `Glean.browser.setDefaultError`

## _isWindows11()
- 位置: L526-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.isWindows10BuildOrLater()`
- XPCOM: `Services.sysinfo`

## getBundledPdfFile()
- 位置: L538-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `file.append()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `Services.dirsvc`

## setAsDefaultPDFHandler()
- 位置: async L565-578
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this._setAsDefaultPDFHandlerMac()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this._setAsDefaultPDFHandlerWin()`
- 参照: `AppConstants.platform`

## _setAsDefaultPDFHandlerMac()
- 位置: async L592-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.setDefaultPdfHandlerAttempt.record()`, `lazy.log.debug()`, `this.isDefaultHandlerFor()`, `this.shellService.isDefaultHandlerAWebBrowserFor()`, `this.shellService.setAsDefaultHandlerFor()`
- 参照: `this.shellService.canSetAsDefaultHandler`

## _setAsDefaultPDFHandlerWin()
- 位置: async L633-736
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.browser.setDefaultPdfHandlerAttempt.record()`, `Glean.browser.setDefaultPdfHandlerUserChoiceResult.Success.add()`, `Glean.browser.setDefaultPdfHandlerUserChoiceResult[telemetryResult].add()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `lazy.log.debug()`, `this._isWindows11()`, `this.getDefaultPDFHandler()`, `this.isDefaultHandlerFor()`, `this.setAsDefaultPDFHandlerUserChoice()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `this.getBundledPdfFile()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `Services.io.newFileURI()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `lazy.WindowsSetDefaultRedirect.arm()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `this._isWindows11()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `this.shellService.launchSetDefaultAppPicker()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `lazy.WindowsSetDefaultRedirect.clear()`
- 条件付き依存: `if ( !success && Services.prefs.getBoolPref( "browser.shell.setDefaultPDFHandler.useOpenWith", false ) )` → `lazy.log.debug()`
- 条件付き依存: `if (!success && this._isWindows11())` → `this.shellService.launchModernSettingsDialogDefaultApps()`
- 条件付き依存: `if (!success && this._isWindows11())` → `Glean.browser.setDefaultPdfHandlerModernSettingsResult.Success.add()`
- 条件付き依存: `if (!success && this._isWindows11())` → `Glean.browser.setDefaultPdfHandlerModernSettingsResult.Failure.add()`
- 条件付き依存: `if (!success && this._isWindows11())` → `lazy.log.debug()`
- 参照: `Ci.nsIWindowsShellService.OPEN_WITH_SET_HANDLER`, `Ci.nsIWindowsShellService.OPEN_WITH_SET_HANDLER_WIN10`, `Glean.browser.setDefaultPdfHandlerUserChoiceResult`, `Services.io.newFileURI(this.getBundledPdfFile("blank.pdf")).spec`, `e.telemetryResult`, `lazy.ScheduledTask`, `lazy.WindowsSetDefaultRedirect.TYPE.FILE`, `this.getBundledPdfFile("confused_fox.pdf").path`, `this.getDefaultPDFHandler().knownBrowser`
- XPCOM: [`nsIWindowsShellService`](nsIWindowsShellService.idl.md) / `Services.io` / `Services.prefs`

## setAsDefaultProtocolHandler()
- 位置: async L750-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.browser.setDefaultProtocolHandlerAttempt.record()`, `Services.prefs.getIntPref()`, `lazy.WindowsSetDefaultRedirect.arm()`, `lazy.WindowsSetDefaultRedirect.clear()`, `lazy.log.debug()`, `this._isWindows11()`, `this.isDefaultHandlerFor()`, `this.shellService.launchSetDefaultAppPicker()`
- 条件付き依存: `if (!success)` → `this.shellService.launchModernSettingsDialogDefaultApps()`
- 条件付き依存: `if (!success)` → `Glean.browser.setDefaultProtocolHandlerModernSettingsResult.Success.add()`
- 条件付き依存: `if (!success)` → `Glean.browser.setDefaultProtocolHandlerModernSettingsResult.Failure.add()`
- 条件付き依存: `if (!success)` → `lazy.log.debug()`
- 参照: `AppConstants.platform`, `Ci.nsIWindowsShellService.OPEN_WITH_PROTOCOL_MESSAGING`, `Ci.nsIWindowsShellService.OPEN_WITH_SET_HANDLER`, `Ci.nsIWindowsShellService.OPEN_WITH_SET_HANDLER_WIN10`, `lazy.ScheduledTask`, `lazy.WindowsSetDefaultRedirect.TYPE.PROTOCOL`
- XPCOM: [`nsIWindowsShellService`](nsIWindowsShellService.idl.md) / `Services.prefs`

## isDefaultHandlerFor()
- 位置: L843-848
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "win" || AppConstants.platform == "macosx")` → `this.shellService.isDefaultHandlerFor()`
- 参照: `AppConstants.platform`

## canSetAsDefaultPDFHandler()
- 位置: L857-865
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `this.shellService.canSetAsDefaultHandler`

## doesAppNeedPin()
- 位置: async L872-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-taskbar;1"].getService()`, `Services.sysinfo.getProperty()`, `lazy.NimbusFeatures.shellService.getVariable()`, `this.shellService.canPinToTaskbar()`, `this.shellService.isCurrentAppPinnedToTaskbar()`
- 参照: `AppConstants.platform`, `Ci.nsIWinTaskbar`, `Components.Exception`, `Cr.NS_ERROR_NOT_AVAILABLE`, `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`, `this.macDockSupport.isAppInDock`, `winTaskbar.defaultGroupId`, `winTaskbar.defaultPrivateGroupId`
- XPCOM: `nsIWinTaskbar` / `@mozilla.org/windows-taskbar;1` / `Services.appinfo` / `Services.sysinfo`

## pinToTaskbar()
- 位置: async L934-952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.doesAppNeedPin()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.shellService.pinCurrentAppToTaskbar()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.macDockSupport.ensureAppIsPinnedToDock()`
- 参照: `AppConstants.platform`

## pinToStartMenu()
- 位置: async L961-973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doesAppNeedStartMenuPin()`
- 条件付き依存: `if (await this.doesAppNeedStartMenuPin())` → `this.shellService.pinCurrentAppToStartMenu()`
- 条件付き依存: `if (await this.doesAppNeedStartMenuPin())` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (await this.doesAppNeedStartMenuPin())` → `lazy.log.warn()`
- XPCOM: `Services.prefs`

## doesAppNeedStartMenuPin()
- 位置: async L986-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.sysinfo.getProperty()`, `this.shellService.isCurrentAppPinnedToStartMenu()`
- 参照: `AppConstants.platform`, `Components.Exception`, `Cr.NS_ERROR_NOT_AVAILABLE`, `Services.appinfo.PROCESS_TYPE_DEFAULT`, `Services.appinfo.processType`
- XPCOM: `Services.appinfo` / `Services.prefs` / `Services.sysinfo`

## recordWasPreviouslyPinnedToStartMenu()
- 位置: async L1017-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.sysinfo.getProperty()`, `this.shellService.isCurrentAppPinnedToStartMenu()`
- 条件付き依存: `if ( !isPinned && Services.prefs.getBoolPref(MSIX_PREVIOUSLY_PINNED_PREF, false) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( !isPinned && Services.prefs.getBoolPref(MSIX_PREVIOUSLY_PINNED_PREF, false) )` → `Glean.startMenu.manuallyUnpinnedSinceLastLaunch.record()`
- XPCOM: `Services.prefs` / `Services.sysinfo`

## _throwForWDBAResult()
- 位置: L1031-1047
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cr.NS_ERROR_WDBA_BUILD`, `Cr.NS_ERROR_WDBA_HASH_CHECK`, `Cr.NS_ERROR_WDBA_NO_PROGID`, `Cr.NS_ERROR_WDBA_REJECTED`, `Cr.NS_OK`

## shortcutIconType()
- 位置: L1049-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## writeShortcutIcon()
- 位置: async L1068-1084
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/binaryinputstream;1"].createInstance()`, `IOUtils.write()`, `bis.readArrayBuffer()`, `bis.setInputStream()`, `lazy.imgTools.encodeScaledImage()`, `stream.available()`
- 参照: `Ci.nsIBinaryInputStream`, `ShellService.shortcutIconType.mimeType`, `file.path`, `newByteArray.buffer`
- XPCOM: [`nsIBinaryInputStream`](../../../xpcom/io/nsIBinaryInputStream.idl.md) / `@mozilla.org/binaryinputstream;1`

## createLinuxDesktopEntry()
- 位置: async L1106-1164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeUTF8()`, `ShellService._findStartupCommand()`, `ShellService._getLinuxDesktopEntryPath()`, `ShellService.requestInstallDynamicLauncher()`, `appId.split()`, `argv.map()`, `argv.map(arg => `"${escapeArg(arg)}"`).join()`, `argv.unshift()`, `escapeArg()`, `ini.QueryInterface()`, `ini.setString()`, `ini.writeToString()`, `lazy.iniParserFactory.createINIParser()`, `segments.map()`, `segments.map(isValidSegment).includes()`
- 参照: `AppConstants.platform`, `Ci.nsIINIParserWriter`, `this.desktopEntryApi`
- XPCOM: [`nsIINIParserWriter`](nsIGNOMEShellService.idl.md)

## isValidSegment()
- 位置: L1123-1124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `segment.match()`

## escapeArg()
- 位置: L1141-1141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `arg.replaceAll()`

## _findStartupCommand()
- 位置: async L1198-1259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `Promise.allSettled()`, `Services.dirsvc.get()`, `ShellService.getArgv0()`, `argv0.includes()`, `candidates.map()`, `file.equals()`, `file.initWithPath()`, `lazy.Subprocess.pathSearch()`, `results.filter()`, `wanted.initWithPath()`
- 条件付き依存: `if (argv0.includes("/"))` → `wanted.setRelativePath()`
- 条件付き依存: `if (argv0.includes("/"))` → `Services.dirsvc.get()`
- 条件付き依存: `if (argv0 !== "")` → `lazy.Subprocess.pathSearch()`
- 条件付き依存: `if (!(argv0.includes("/")))` → `wanted.initWithFile()`
- 条件付き依存: `if (file.equals(wanted))` → `PathUtils.filename()`
- 参照: `AppConstants.MOZ_APP_NAME`, `AppConstants.MOZ_UPDATE_CHANNEL`, `Ci.nsIFile`, `file.target`, `got.status`, `wanted.leafName`, `wanted.path`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `@mozilla.org/file/local;1` / `Services.dirsvc`

## deleteLinuxDesktopEntry()
- 位置: async L1269-1288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `ShellService._getLinuxDesktopEntryPath()`, `ShellService.requestUninstallDynamicLauncher()`
- 参照: `AppConstants.platform`, `this.desktopEntryApi`

## desktopEntryApi()
- 位置: L1290-1313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["filesystem", "dynamiclauncher"].includes()`
- 参照: `AppConstants.platform`, `lazy.DESKTOP_ENTRY_API`, `lazy.gioService.isRunningUnderFlatpak`, `lazy.gioService.isRunningUnderSnap`

## _getLinuxDesktopEntryPath()
- 位置: L1321-1337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.isAbsolute()`, `PathUtils.join()`, `Services.env.get()`
- 条件付き依存: `if (!dataHome || !PathUtils.isAbsolute(dataHome))` → `Services.dirsvc.get()`
- 条件付き依存: `if (!dataHome || !PathUtils.isAbsolute(dataHome))` → `PathUtils.join()`
- 参照: `Ci.nsIFile`, `home.path`, `this.desktopEntryApi`
- XPCOM: [`nsIFile`](nsIShellService.idl.md) / `Services.dirsvc` / `Services.env`

## requestCreateAndPinSecondaryTile()
- 位置: async L1339-1351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `lazy.secondaryTileService.requestCreateAndPin()`, `this._secondaryTileListener()`
- 参照: `resolver.promise`

## requestDeleteSecondaryTile()
- 位置: async L1353-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `lazy.secondaryTileService.requestDelete()`, `this._secondaryTileListener()`
- 参照: `resolver.promise`

## _secondaryTileListener()
- 位置: L1364-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`
- 参照: `Ci.nsISecondaryTileListener`
- XPCOM: [`nsISecondaryTileListener`](nsISecondaryTile.idl.md)

## succeeded()
- 位置: L1367-1369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolver.resolve()`

## failed()
- 位置: L1370-1374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hresult.toString()`, `hresult.toString(16).padStart()`, `resolver.reject()`

## get()
- 位置: L1416-1429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.warn()`, `name.toString()`
- 参照: `target.shellService`

## WDBAError.constructor()
- 位置: L1433-1438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.exitCode`, `this.telemetryResult`
