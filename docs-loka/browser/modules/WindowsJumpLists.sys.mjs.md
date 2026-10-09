# browser/modules/WindowsJumpLists.sys.mjs

source: browser/modules/WindowsJumpLists.sys.mjs
source-hash: 5ddca6c37763b5261cceb156fded5f37035e218a
lines: 579

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.prefs.getBoolPref()`, `Services.prefs.getBranch()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyServiceGetter()`, `console.createInstance()`

## _getString()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy._stringBundle.GetStringFromName()`

## title()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_getString()`

## description()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_getString()`

## title()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_getString()`

## description()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_getString()`

## title()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_getString()`

## description()
- 位置: L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_getString()`

## constructor()
- 位置: L138-149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._builder`, `this._isBuilding`, `this._maxItemCount`, `this._showFrequent`, `this._showRecent`, `this._showTasks`, `this._shuttingDown`, `this._tasks`

## refreshPrefs()
- 位置: L151-156
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._maxItemCount`, `this._showFrequent`, `this._showRecent`, `this._showTasks`

## updateShutdownState()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._shuttingDown`

## delete()
- 位置: L162-164
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._builder`

## buildList()
- 位置: async L176-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `console.error()`, `this._builder.checkForRemovals()`
- 条件付き依存: `if (!(this._builder instanceof Ci.nsIJumpListBuilder))` → `console.error()`
- 条件付き依存: `if (!this._showRecent)` → `this._clearRecentsList()`
- 条件付き依存: `if (!this._showFrequent && !this._showTasks)` → `this._deleteActiveJumpList()`
- 条件付き依存: `if (removedURLs.length)` → `this._clearHistory()`
- 条件付き依存: `if (this._showTasks)` → `this._tasks.map()`
- 条件付き依存: `if (this._showFrequent)` → `lazy.PlacesUtils.promiseDBConnection()`
- 条件付き依存: `if (this._showFrequent)` → `conn.executeCached()`
- 条件付き依存: `if (this._showFrequent)` → `Services.io.newURI()`
- 条件付き依存: `if (this._showFrequent)` → `row.getResultByName()`
- 条件付き依存: `if (this._showFrequent)` → `this._builder.obtainAndCacheFaviconAsync()`
- 条件付き依存: `if (this._showFrequent)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (this._showFrequent)` → `customDescriptions.push()`
- 条件付き依存: `if (this._showFrequent)` → `_getString()`
- 条件付き依存: `if (!this._shuttingDown)` → `this._builder.populateJumpList()`
- 参照: `Ci.nsIFile`, `Ci.nsIJumpListBuilder`, `Ci.nsINavHistoryService.TRANSITION_EMBED`, `Ci.nsINavHistoryService.TRANSITION_FRAMED_LINK`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).path`, `removedURLs.length`, `task.args`, `task.description`, `task.iconIndex`, `task.title`, `this._builder`, `this._isBuilding`, `this._maxItemCount`, `this._showFrequent`, `this._showRecent`, `this._showTasks`, `this._shuttingDown`, `uri.spec`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `nsIJumpListBuilder` / [`nsINavHistoryService`](../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.dirsvc` / `Services.io`

## _clearRecentsList()
- 位置: L293-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._builder.clearRecentsList()`

## _deleteActiveJumpList()
- 位置: L297-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._builder.clearJumpList()`

## _clearHistory()
- 位置: L317-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `URL.parse()`, `uriSpecsToRemove .map()`, `uriSpecsToRemove .map(spec => URL.parse(spec)?.URI) .filter()`
- 条件付き依存: `if (URIsToRemove.length)` → `lazy.PlacesUtils.history.remove(URIsToRemove).catch()`
- 条件付き依存: `if (URIsToRemove.length)` → `lazy.PlacesUtils.history.remove()`
- 参照: `URIsToRemove.length`, `URL.parse(spec)?.URI`, `console.error`

## WTBJL_startup()
- 位置: async L344-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._initObs()`, `this._initTaskbar()`, `this._refreshPrefs()`, `this._updateTimer()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.enabled)` → `tasksCfg.push()`
- 条件付き依存: `if (this._blocked)` → `this._builder._deleteActiveJumpList()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `lazy._taskbarService.available`, `this._blocked`, `this._builder._tasks`, `this._pbBuilder._tasks`

## WTBJL_update()
- 位置: L374-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._builder.buildList()`
- 条件付き依存: `if (!this._builtPb)` → `this._pbBuilder.buildList()`
- 参照: `this._blocked`, `this._builtPb`, `this._enabled`, `this._shuttingDown`

## WTBJL__shutdown()
- 位置: L395-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._builder.updateShutdownState()`, `this._free()`, `this._pbBuilder.updateShutdownState()`
- 参照: `this._shuttingDown`

## WTBJL__refreshPrefs()
- 位置: L406-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy._prefs.getBoolPref()`, `lazy._prefs.getIntPref()`, `this._builder.refreshPrefs()`, `this._pbBuilder.refreshPrefs()`
- 参照: `this._enabled`

## WTBJL__initTaskbar()
- 位置: async L425-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `builder.isAvailable()`, `lazy._taskbarService.createJumpListBuilder()`, `pbBuilder.isAvailable()`
- 参照: `this._builder`, `this._pbBuilder`

## WTBJL__initObs()
- 位置: L448-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.PlacesUtils.observers.addListener()`, `lazy._prefs.addObserver()`, `this.update.bind()`
- 参照: `this._placesObserver`
- XPCOM: `Services.obs`

## WTBJL__freeObs()
- 位置: L464-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy._prefs.removeObserver()`
- 条件付き依存: `if (this._placesObserver)` → `lazy.PlacesUtils.observers.removeListener()`
- 参照: `this._placesObserver`
- XPCOM: `Services.obs`

## WTBJL__updateTimer()
- 位置: L476-488
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._timer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._timer)` → `this._timer.initWithCallback()`
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._timer)` → `lazy._prefs.getIntPref()`
- 条件付き依存: `if ((!this._enabled || this._shuttingDown) && this._timer)` → `this._timer.cancel()`
- 参照: `Ci.nsITimer`, `this._enabled`, `this._shuttingDown`, `this._timer`, `this._timer.TYPE_REPEATING_SLACK`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## WTBJL__updateIdleObserver()
- 位置: L491-502
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._hasIdleObserver)` → `lazy._idle.addIdleObserver()`
- 条件付き依存: `if ( (!this._enabled || this._shuttingDown) && this._hasIdleObserver )` → `lazy._idle.removeIdleObserver()`
- 参照: `this._enabled`, `this._hasIdleObserver`, `this._shuttingDown`

## WTBJL__free()
- 位置: L504-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._builder.delete()`, `this._freeObs()`, `this._pbBuilder.delete()`, `this._updateIdleObserver()`, `this._updateTimer()`

## WTBJL_clearJumpList()
- 位置: async L520-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._unblockJumpList()`
- 条件付き依存: `if (unblockPromise)` → `console.error()`
- 参照: `this._blocked`

## WTBJL_updateJumpList()
- 位置: L532-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.update()`
- 参照: `this._blocked`

## WTBJL_notify()
- 位置: L537-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `this._updateIdleObserver()`, `this.update()`
- XPCOM: `Services.tm`

## WTBJL_observe()
- 位置: L545-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy._prefs.getBoolPref()`, `this._refreshPrefs()`, `this._shutdown()`, `this._updateIdleObserver()`, `this._updateTimer()`, `this.update()`
- 条件付き依存: `if (this._enabled && !lazy._prefs.getBoolPref(PREF_TASKBAR_ENABLED))` → `this._builder._deleteActiveJumpList()`
- 条件付き依存: `if (this._timer)` → `this._timer.cancel()`
- 参照: `this._enabled`, `this._timer`
- XPCOM: `Services.tm`
