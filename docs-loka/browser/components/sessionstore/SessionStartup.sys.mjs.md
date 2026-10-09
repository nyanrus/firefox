# browser/components/sessionstore/SessionStartup.sys.mjs

source: browser/components/sessionstore/SessionStartup.sys.mjs
source-hash: 85c725f7eb8d0f88f8f9fea31be3e1e0736852a8
lines: 507

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.withResolvers()`, `XPCOMUtils.declareLazy()`

## init()
- 位置: L87-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `lazy.SessionFile.read()`, `lazy.SessionFile.read().then()`, `lazy.sessionStoreLogger.debug()`, `lazy.sessionStoreLogger.error()`, `this._onSessionFileRead()`
- 条件付き依存: `if (!AppConstants.DEBUG)` → `lazy.StartupPerformance.init()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `gOnceInitializedDeferred.resolve()`
- 条件付き依存: `if (this._resumingAfterOsRestart)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (!Services.appinfo.restartedByOS)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this._resumingAfterOsRestart)` → `Services.prefs.setBoolPref()`
- 参照: `AppConstants.DEBUG`, `Services.appinfo.restartedByOS`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `result.origin`, `this._initialized`, `this._resumeSessionOnce`, `this._resumingAfterOsRestart`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.prefs`

## _createSupportsString()
- 位置: L141-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 参照: `Ci.nsISupportsString`, `string.data`
- XPCOM: [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`

## _recordSessionAvailability()
- 位置: L160-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.startupSessionAvailability.record()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `lazy.sessionStoreLogger.debug()`
- 参照: `Services.appinfo.restartedByOS`, `fileStates.clean`, `fileStates.cleanBackup`, `fileStates.recovery`, `fileStates.recoveryBackup`, `fileStates.upgradeBackup`, `this._resumeSessionOnce`, `this._resumingAfterOsRestart`
- XPCOM: `Services.appinfo` / `Services.prefs`

## _onSessionFileRead()
- 位置: L193-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.shutdownOk[ this._previousSessionCrashed ? "false" : "true" ].add()`, `Glean.sessionRestore.shutdownSuccessSessionStartup.record()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.tm.idleDispatchToMainThread()`, `gOnceInitializedDeferred.resolve()`, `initialState.windows.reduce()`, `lazy.BrowserUsageTelemetry.updateMaxTabPinnedCount()`, `lazy.CrashMonitor.previousCheckpoints.then()`, `lazy.sessionStoreLogger.debug()`, `this._createSupportsString()`, `this._previousSessionCrashed.toString()`, `this._recordSessionAvailability()`, `this.isAutomaticRestoreEnabled()`, `win.tabs.reduce()`
- 条件付き依存: `if (stateString != source)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (stateString != source)` → `JSON.parse()`
- 条件付き依存: `if (stateString != source)` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if (this._initialState == null)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (this._initialState == null)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (this._initialState == null)` → `gOnceInitializedDeferred.resolve()`
- 条件付き依存: `if (!isAutomaticRestoreEnabled && this._initialState)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (this.sessionType == this.NO_SESSION)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (!(this.sessionType == this.NO_SESSION))` → `Services.obs.addObserver()`
- 参照: `Glean.sessionRestore.shutdownOk`, `crashReasons.FINAL_STATE_WRITING_INCOMPLETE`, `crashReasons.SESSION_STATE_FLAG_MISSING`, `initialState.savedGroups.length`, `supportsStateString.data`, `tab.pinned`, `this.NO_SESSION`, `this._initialState`, `this._initialState.lastSessionState`, `this._initialState.session`, `this._initialState.session.state`, `this._initialized`, `this._previousSessionCrashed`, `this._sessionType`, `this.sessionType`
- XPCOM: `Services.obs` / `Services.tm`

## observe()
- 位置: L354-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.sessionStoreLogger.debug()`
- 参照: `this.NO_SESSION`, `this._didRestore`, `this._initialState`, `this._sessionType`
- XPCOM: `Services.obs`

## onceInitialized()
- 位置: L373-375
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gOnceInitializedDeferred.promise`

## state()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._initialState`

## isAutomaticRestoreEnabled()
- 位置: L392-404
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._resumeSessionEnabled === null)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this._resumeSessionEnabled === null)` → `Services.prefs.getIntPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._resumeSessionEnabled`
- XPCOM: `Services.prefs`

## willRestore()
- 位置: L411-416
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.RECOVER_SESSION`, `this.RESUME_SESSION`, `this.sessionType`

## willRestoreAsCrashed()
- 位置: L424-426
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.RECOVER_SESSION`, `this.sessionType`

## willOverrideHomepage()
- 位置: L436-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `this._initialState.windows.filter()`, `this.isAutomaticRestoreEnabled()`, `this.onceInitialized.then()`, `this.willRestore()`, `this.willRestoreAsCrashed()`, `w.tabs.some()`
- 参照: `t.pinned`, `this._didRestore`, `this._initialState`, `this._initialState.windows`, `w._maybeDontRestoreTabs`

## sessionType()
- 位置: L470-488
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._sessionType === null)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this._sessionType === null)` → `this.isAutomaticRestoreEnabled()`
- 参照: `this.DEFER_SESSION`, `this.NO_SESSION`, `this.RECOVER_SESSION`, `this.RESUME_SESSION`, `this._initialState`, `this._previousSessionCrashed`, `this._sessionType`
- XPCOM: `Services.prefs`

## previousSessionCrashed()
- 位置: L493-495
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._previousSessionCrashed`

## resetForTest()
- 位置: L497-500
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._resumeSessionEnabled`, `this._sessionType`
