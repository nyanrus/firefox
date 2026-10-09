# browser/base/content/aboutDialog-appUpdater.js

source: browser/base/content/aboutDialog-appUpdater.js
source-hash: 879b827299c0231c08f1a4fd41750ad14712563c
lines: 323

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetter()`

## onUnload()
- 位置: L31-36
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gAppUpdater)` → `gAppUpdater.destroy()`

## appUpdater()
- 位置: L38-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings.createBundle()`, `document.getElementById()`, `this._appUpdater.addListener()`, `this._appUpdater.check()`
- 条件付き依存: `if (this.updateDeck)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (this.updateDeck)` → `document.querySelectorAll()`
- 条件付き依存: `if (this.updateDeck)` → `document.l10n.setArgs()`
- 条件付き依存: `if (this.updateDeck)` → `manualLink.closest()`
- 条件付き依存: `if (this.updateDeck)` → `document.getElementById()`
- 条件付き依存: `if (this.updateDeck)` → `console.error()`
- 参照: `document.getElementById("failedLink").href`, `manualLink.href`, `manualURL.href`, `manualURL.origin`, `manualURL.pathname`, `this._appUpdateListener`, `this._appUpdater`, `this.bundle`, `this.options`, `this.updateDeck`, `this.updatingMinDisplayTimerId`
- XPCOM: `Services.strings` / `Services.urlFormatter`

## this._appUpdateListener()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onAppUpdateStatus()`

## destroy()
- 位置: L79-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stopCurrentCheck()`
- 条件付き依存: `if (this.updatingMinDisplayTimerId)` → `clearTimeout()`
- 参照: `this.updatingMinDisplayTimerId`

## stopCurrentCheck()
- 位置: L86-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._appUpdater.removeListener()`, `this._appUpdater.stop()`
- 参照: `this._appUpdateListener`

## update()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._appUpdater.update`

## selectedPanel()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.updateDeck?.selectedPanel`

## _onAppUpdateStatus()
- 位置: L99-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `document.getElementById()`, `setTimeout()`, `this.checkingForUpdatesDelayPromise.then()`, `this.selectPanel()`
- 条件付き依存: `if (!args.length)` → `DownloadUtils.getTransferTotal()`
- 条件付き依存: `if (downloadStatus)` → `document.l10n.setArgs()`
- 条件付き依存: `if (!args.length)` → `this.selectPanel()`
- 条件付き依存: `if (!(!args.length))` → `DownloadUtils.getTransferTotal()`
- 条件付き依存: `if (!(downloadStatus))` → `this.selectPanel()`
- 条件付き依存: `if (Services.policies.isAllowed("appUpdate"))` → `this.selectPanel()`
- 条件付き依存: `if (!(Services.policies.isAllowed("appUpdate")))` → `this.selectPanel()`
- 条件付き依存: `if (this.updateDeck)` → `document.getElementById()`
- 条件付き依存: `if (this.update.detailsURL)` → `this.selectPanel()`
- 条件付き依存: `if (!(this.update.detailsURL))` → `this.selectPanel()`
- 参照: `AppUpdater.STATUS.CHECKING`, `AppUpdater.STATUS.CHECKING_FAILED`, `AppUpdater.STATUS.DOWNLOADING`, `AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `AppUpdater.STATUS.DOWNLOAD_FAILED`, `AppUpdater.STATUS.INTERNAL_ERROR`, `AppUpdater.STATUS.MANUAL_UPDATE`, `AppUpdater.STATUS.NEVER_CHECKED`, `AppUpdater.STATUS.NO_UPDATER`, `AppUpdater.STATUS.NO_UPDATES_FOUND`, `AppUpdater.STATUS.OTHER_INSTANCE_HANDLING_UPDATES`, `AppUpdater.STATUS.READY_FOR_RESTART`, `AppUpdater.STATUS.STAGING`, `AppUpdater.STATUS.UNSUPPORTED_SYSTEM`, `AppUpdater.STATUS.UPDATE_DISABLED_BY_POLICY`, `args.length`, `this.checkingForUpdatesDelayPromise`, `this.update.detailsURL`, `this.update.selectedPatch`, `this.update.selectedPatch.size`, `this.updateDeck`, `this.updatingMinDisplayTimerId`, `unsupportedLink.href`
- XPCOM: `Services.policies`

## selectPanel()
- 位置: L207-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `panel.querySelector()`
- 条件付き依存: `if (aChildID == "downloadAndInstall")` → `/a\d+$/.test()`
- 条件付き依存: `if (/a\d+$/.test(updateVersion))` → `buildID.slice()`
- 条件付き依存: `if (typeof this.options.selectPanel === "function")` → `this.options.selectPanel()`
- 条件付き依存: `if (aChildID == "downloadAndInstall")` → `this.bundle.formatStringFromName()`
- 条件付き依存: `if (aChildID == "downloadAndInstall")` → `this.bundle.GetStringFromName()`
- 条件付き依存: `if (this.options.buttonAutoFocus)` → `Promise.resolve()`
- 条件付き依存: `if (document.readyState != "complete")` → `window.addEventListener()`
- 条件付き依存: `if (this.options.buttonAutoFocus)` → `promise.then()`
- 条件付き依存: `if ( !document.commandDispatcher.focusedElement || // don't steal the focus // except from the other buttons document.commandDispatcher.focusedElement.localName ...)` → `button.focus()`
- 参照: `button.accessKey`, `button.label`, `document.commandDispatcher.focusedElement`, `document.commandDispatcher.focusedElement.localName`, `document.readyState`, `gAppUpdater.update.buildID`, `gAppUpdater.update.displayVersion`, `icon.className`, `this.options.buttonAutoFocus`, `this.options.selectPanel`, `this.updateDeck.selectedPanel`

## checkForUpdates()
- 位置: L269-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._appUpdater.check()`

## buttonRestartAfterDownload()
- 位置: L277-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.startup.quit()`, `gAppUpdater.selectPanel()`
- 条件付き依存: `if (cancelQuit.data)` → `gAppUpdater.selectPanel()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.restartInSafeMode()`
- 条件付き依存: `if ( !Services.startup.quit( Ci.nsIAppStartup.eAttemptQuit | Ci.nsIAppStartup.eRestart ) )` → `gAppUpdater.selectPanel()`
- 参照: `AUS.currentState`, `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsIApplicationUpdateService.STATE_PENDING`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsIApplicationUpdateService`](../../../toolkit/mozapps/update/nsIUpdateService.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## startDownload()
- 位置: L319-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._appUpdater.allowUpdateDownload()`
