# browser/components/DefaultBrowserCheck.sys.mjs

source: browser/components/DefaultBrowserCheck.sys.mjs
source-hash: 0434d53806382a731d7b1c65268149e25cd11603
lines: 249

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## prompt()
- 位置: async L16-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.browser.setDefaultResult.accumulateSingleSample()`, `Math.floor()`, `Math.floor(Date.now() / 1000).toString()`, `Services.prefs.setCharPref()`, `ps.asyncConfirmEx()`, `rv.get()`, `shellService.doesAppNeedPin()`, `shellService.doesAppNeedStartMenuPin()`, `win.MozXULElement.insertFTLIfNeeded()`, `win.document.l10n.formatMessages()`, `win.getShellService()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `Services.sysinfo.getProperty()`
- 条件付き依存: `if (buttonNumClicked == 0)` → `shellService.pinToTaskbar()`
- 条件付き依存: `if (buttonNumClicked == 0)` → `this.log.error()`
- 条件付き依存: `if (buttonNumClicked == 0)` → `shellService.pinToStartMenu()`
- 条件付き依存: `if (buttonNumClicked == 0)` → `shellService.setAsDefault()`
- 条件付き依存: `if (checkboxState)` → `Services.prefs.setCharPref()`
- 参照: `AppConstants.platform`, `Services.prompt`, `lazy.CommonDialog.DEFAULT_APP_ICON_CSS`, `ps.BUTTON_POS_0`, `ps.BUTTON_POS_0_DEFAULT`, `ps.BUTTON_POS_1`, `ps.BUTTON_TITLE_IS_STRING`, `ps.MODAL_TYPE_INTERNAL_WINDOW`, `shellService.shouldCheckDefaultBrowser`, `win.browsingContext`
- XPCOM: `Services.prefs` / `Services.prompt` / `Services.sysinfo`

## willCheckDefaultBrowser()
- 位置: async L131-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `lazy.BrowserWindowTracker.getTopWindow()`, `shellService.isDefaultBrowser()`, `win.getShellService()`
- 条件付き依存: `if (Cc["@mozilla.org/gio-service;1"])` → `Cc["@mozilla.org/gio-service;1"].getService()`
- 条件付き依存: `if (isDefault && isStartupCheck)` → `Math.floor(Date.now() / 1000).toString()`
- 条件付き依存: `if (isDefault && isStartupCheck)` → `Math.floor()`
- 条件付き依存: `if (isDefault && isStartupCheck)` → `Date.now()`
- 条件付き依存: `if (isDefault && isStartupCheck)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (isStartupCheck)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (isStartupCheck)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (isStartupCheck)` → `Glean.browser.isUserDefault[isDefault ? "true" : "false"].add()`
- 条件付き依存: `if (isStartupCheck)` → `Glean.browser.isUserDefaultError[ isDefaultError ? "true" : "false" ].add()`
- 条件付き依存: `if (isStartupCheck)` → `Glean.browser.setDefaultAlwaysCheck[ shouldCheck ? "true" : "false" ].add()`
- 条件付き依存: `if (isStartupCheck)` → `Glean.browser.setDefaultDialogPromptRawcount.accumulateSingleSample()`
- 参照: `AppConstants.DEBUG`, `AppConstants.RELEASE_OR_BETA`, `Ci.nsIGIOService`, `Glean.browser.isUserDefault`, `Glean.browser.isUserDefaultError`, `Glean.browser.setDefaultAlwaysCheck`, `gIOSvc.isRunningUnderFlatpak`, `lazy.SessionStartup.RECOVER_SESSION`, `lazy.SessionStartup.onceInitialized`, `lazy.SessionStartup.sessionType`, `shellService.shouldCheckDefaultBrowser`
- XPCOM: [`nsIGIOService`](../../xpcom/system/nsIGIOService.idl.md) / `@mozilla.org/gio-service;1` → `nsGIOService` (toolkit/system/gnome/components.conf) / `Services.prefs`
