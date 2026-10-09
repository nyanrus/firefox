# browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs

source: browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs
source-hash: 838512efba972e47fb90d301081416d1ce3cbde1
lines: 415

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `openAddonsUrl()`, `openUrlFun()`

## openUrlFun()
- 位置: L32-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openUrl()`
- 参照: `controller.browserWindow`

## openUrl()
- 位置: L34-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.startsWith()`
- 条件付き依存: `if (url.startsWith("about:"))` → `Services.io.newURI()`
- 条件付き依存: `if (url.startsWith("about:"))` → `window.switchToTabHavingURI()`
- 条件付き依存: `if (!(url.startsWith("about:")))` → `window.gBrowser.addTab()`
- 条件付き依存: `if (!(url.startsWith("about:")))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `uri.hasRef`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## openAddonsUrl()
- 位置: L49-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.BrowserAddonUI.openAddonsMgr()`

## currentWindow()
- 位置: L57-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`

## currentBrowser()
- 位置: L58-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentWindow()`
- 参照: `currentWindow().gBrowser.selectedBrowser`

## unmutedAudioTabs()
- 位置: L60-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(win.gBrowser.tabs).filter()`, `lazy.BrowserWindowTracker.orderedWindows.flatMap()`, `tab.hasAttribute()`
- 参照: `tab.muted`, `tab.soundPlaying`, `win.gBrowser.tabs`

## onPick()
- 位置: L92-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.top.PlacesCommandHook.showPlacesOrganizer()`

## onPick()
- 位置: L105-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.document .getElementById()`, `controller.browserWindow.document .getElementById("Tools:Sanitize") .doCommand()`

## isUnsupported()
- 位置: L116-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onPick()
- 位置: L149-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.FirefoxViewHandler.openTab()`

## isUnsupported()
- 位置: L160-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DevToolsShim.isDevToolsUser()`, `lazy.DevToolsShim.isEnabled()`

## isInactive()
- 位置: L165-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentWindow()`, `lazy.DevToolsShim.hasToolboxForTab()`, `win.gBrowser.currentURI.spec.startsWith()`
- 参照: `win.gBrowser.selectedTab`

## onPick()
- 位置: L172-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openInspector()`
- 参照: `controller.browserWindow`

## isUnsupported()
- 位置: L180-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DevToolsShim.isEnabled()`

## isInactive()
- 位置: L181-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentBrowser()`, `currentBrowser().currentURI.spec.startsWith()`

## onPick()
- 位置: L183-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openColorPicker()`
- 参照: `controller.browserWindow`

## onPick()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.top.PlacesCommandHook.showPlacesOrganizer()`

## isInactive()
- 位置: L205-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `unmutedAudioTabs()`
- 参照: `unmutedAudioTabs().length`

## onPick()
- 位置: L206-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.toggleMuteAudio()`, `unmutedAudioTabs()`

## isUnsupported()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onPick()
- 位置: L219-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.document.getElementById()`, `controller.browserWindow.document.getElementById("cmd_print").doCommand()`

## onPick()
- 位置: L227-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.OpenBrowserWindow()`

## isUnsupported()
- 位置: L235-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResetProfile.resetSupported()`

## onPick()
- 位置: L236-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResetProfile.openConfirmationDialog()`
- 参照: `controller.browserWindow`

## isUnsupported()
- 位置: L250-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onPick()
- 位置: L253-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/gfx/printsettings-service;1"] .getService()`, `controller.browserWindow.PrintUtils.startPrintWindow()`
- 参照: `Ci.nsIPrintSettingsService`, `controller.browserWindow.PrintUtils.SAVE_TO_PDF_PRINTER`, `controller.browserWindow.gBrowser.selectedBrowser.browsingContext`
- XPCOM: `nsIPrintSettingsService` / `@mozilla.org/gfx/printsettings-service;1`

## isUnsupported()
- 位置: L272-274
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ScreenshotsUtils.screenshotsEnabled`

## onPick()
- 位置: L275-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `controller.browserWindow`
- XPCOM: `Services.obs`

## isUnsupported()
- 位置: L300-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.TranslationsParent.AIFeature.isEnabled`
- XPCOM: `Services.prefs`

## onPick()
- 位置: async L309-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TranslationsParent.openAboutTranslationsPage()`
- 参照: `controller.browserWindow`

## isUnsupported()
- 位置: L322-323
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_UPDATER`, `lazy.AUS.canUsuallyCheckForUpdates`

## isInactive()
- 位置: L324-325
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIApplicationUpdateService.STATE_PENDING`, `lazy.AUS.currentState`
- XPCOM: [`nsIApplicationUpdateService`](../../../toolkit/mozapps/update/nsIUpdateService.idl.md)

## isInactive()
- 位置: L332-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentBrowser()`
- 参照: `currentBrowser().currentURI.scheme`

## onPick()
- 位置: L333-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openUrl()`
- 参照: `controller.browserWindow`, `controller.browserWindow.gBrowser.currentURI.spec`

## isUnsupported()
- 位置: L343-343
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ExperimentAPI.labsEnabled`

## openInspector()
- 位置: L348-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DevToolsShim.showToolboxForTab()`
- 参照: `window.gBrowser.selectedTab`

## openColorPicker()
- 位置: L354-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DevToolsShim.initDevTools()`, `window.document.getElementById()`, `window.document.getElementById("menu_eyedropper")?.doCommand()`

## restartBrowser()
- 位置: L364-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.restartInSafeMode()`
- 条件付き依存: `if (!(Services.appinfo.inSafeMode))` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## QuickActionsLoaderDefault.load()
- 位置: async L395-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `actionData.l10nCommands.map()`, `lazy.ActionsProviderQuickActions.addAction()`, `lazy.gFluentStrings.formatMessages()`, `messages .map()`, `messages .map(({ value }) => value.split(",").map(x => x.trim().toLowerCase())) .flat()`, `value.split()`, `value.split(",").map()`, `x.trim()`, `x.trim().toLowerCase()`
- 参照: `actionData.commands`

## QuickActionsLoaderDefault.ensureLoaded()
- 位置: async L408-413
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#loadedPromise)` → `this.load()`
- 参照: `this.#loadedPromise`
