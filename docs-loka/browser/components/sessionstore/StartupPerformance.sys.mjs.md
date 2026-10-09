# browser/components/sessionstore/StartupPerformance.sys.mjs

source: browser/components/sessionstore/StartupPerformance.sys.mjs
source-hash: ce5a7af623592758c59937388f750f944e790685
lines: 240

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## init()
- 位置: L51-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## latestRestoredTimeStamp()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._latestRestoredTimeStamp`

## isRestored()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isRestored`

## _onRestorationStarts()
- 位置: L77-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Date.now()`, `Glean.sessionRestore.numberOfEagerTabsRestored.accumulateSingleSample()`, `Glean.sessionRestore.numberOfTabsRestored.accumulateSingleSample()`, `Glean.sessionRestore.numberOfWindowsRestored.accumulateSingleSample()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.obs.removeObserver()`, `console.error()`, `this._promiseFinished.then()`
- 条件付き依存: `if (isAutoRestore)` → `Glean.sessionRestore.autoRestoreDurationUntilEagerTabsRestored.accumulateSingleSample()`
- 条件付き依存: `if (!(isAutoRestore))` → `Glean.sessionRestore.manualRestoreDurationUntilEagerTabsRestored.accumulateSingleSample()`
- 参照: `this.RESTORED_TOPIC`, `this._isRestored`, `this._latestRestoredTimeStamp`, `this._promiseFinished`, `this._resolveFinished`, `this._startTimeStamp`, `this._totalNumberOfEagerTabs`, `this._totalNumberOfTabs`, `this._totalNumberOfWindows`
- XPCOM: `Services.obs`

## _startTimer()
- 位置: L135-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `console.error()`, `lazy.setTimeout()`, `this._resolveFinished()`
- 条件付き依存: `if (this._deadlineTimer)` → `lazy.clearTimeout()`
- 参照: `this._deadlineTimer`, `this._hasFired`, `this._resolveFinished`
- XPCOM: `Services.obs`

## observe()
- 位置: L160-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._onRestorationStarts()`, `this._promiseFinished.then()`, `this._startTimer()`, `win.gBrowser.tabContainer.addEventListener()`, `win.gBrowser.tabContainer.removeEventListener()`
- 参照: `ex.stack`, `this._totalNumberOfTabs`, `this._totalNumberOfWindows`, `win.gBrowser.tabContainer`, `win.gBrowser.tabContainer.itemCount`

## observer()
- 位置: L207-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Date.now()`
- 参照: `this._latestRestoredTimeStamp`, `this._totalNumberOfEagerTabs`
