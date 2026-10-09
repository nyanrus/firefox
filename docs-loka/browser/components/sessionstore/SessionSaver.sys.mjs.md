# browser/components/sessionstore/SessionSaver.sys.mjs

source: browser/components/sessionstore/SessionSaver.sys.mjs
source-hash: 1b99e507311668ed2d0a8dd3a34554db513e596e
lines: 444

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/useridleservice;1"].getService()`, `Object.freeze()`, `SessionSaverInternal.cancel()`, `SessionSaverInternal.runDelayed()`, `XPCOMUtils.declareLazy()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `idleService.addIdleObserver()`

## notify()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## run()
- 位置: L59-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionSaverInternal.run()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`

## runDelayed()
- 位置: L71-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionSaverInternal.runDelayed()`

## lastSaveTime()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SessionSaverInternal._lastSaveTime`

## updateLastSaveTime()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionSaverInternal.updateLastSaveTime()`

## cancel()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionSaverInternal.cancel()`

## run()
- 位置: L154-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._saveState()`

## runDelayed()
- 位置: L167-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `requestIdleCallback()`, `setTimeout()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`, `this._idleCallbackID`, `this._intervalWhileActive`, `this._intervalWhileIdle`, `this._isIdle`, `this._lastSaveTime`, `this._timeoutID`, `this._wasIdle`

## saveStateAsyncWhenIdle()
- 位置: L188-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._saveStateAsync()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`

## updateLastSaveTime()
- 位置: L205-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 参照: `this._lastSaveTime`

## cancel()
- 位置: L212-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cancelIdleCallback()`, `clearTimeout()`
- 参照: `this._idleCallbackID`, `this._timeoutID`

## observe()
- 位置: L222-240
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._timeoutID && this._wasIdle)` → `clearTimeout()`
- 条件付き依存: `if (this._timeoutID && this._wasIdle)` → `this.runDelayed()`
- 参照: `this._isIdle`, `this._timeoutID`, `this._wasIdle`

## _saveState()
- 位置: L249-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.collectData.start()`, `Glean.sessionRestore.collectData.stopAndAccumulate()`, `lazy.PrivacyFilter.filterPrivateWindowsAndTabs()`, `lazy.SessionStore.getCurrentState()`, `lazy.SessionStore.keepOnlyWorthSavingTabs()`, `this._maybeClearCookiesAndStorage()`, `this._writeState()`, `this.cancel()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `this.updateLastSaveTime()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `Promise.resolve()`
- 条件付き依存: `if (lazy.sessionStoreLogger.debugEnabled)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `state.windows.unshift()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `state._closedWindows.pop()`
- 参照: `AppConstants.platform`, `closedWin._shouldRestore`, `closedWin.closedAt`, `closedWin.closedId`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.sessionStoreLogger.debugEnabled`, `state._closedWindows`, `state._closedWindows.length`, `state._closedWindows[i]._shouldRestore`, `state.deferredInitialState`, `state.deferredInitialState.windows`, `state.windows`

## _maybeClearCookiesAndStorage()
- 位置: L315-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.RunState.isClosing`, `state.cookies`, `state.windows`, `tab.storage`, `window.tabs`
- XPCOM: `Services.prefs`

## _saveStateAsync()
- 位置: L349-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._saveState()`
- 参照: `this._timeoutID`

## _writeState()
- 位置: L360-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionFile.write()`, `lazy.SessionFile.write(state).then()`, `lazy.sessionStoreLogger.error()`, `notify()`, `this.updateLastSaveTime()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`
