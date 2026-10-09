# browser/components/enterprisepolicies/EphemeralContainerWatcher.sys.mjs

source: browser/components/enterprisepolicies/EphemeralContainerWatcher.sys.mjs
source-hash: 7c24b11d20c79fe8003573a66a57366ac677dddf
lines: 167

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: L24-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `this._cancelStaleTimers()`, `this._onWindowInit()`, `this._onWindowUninit()`, `this._persistIds()`
- 条件付き依存: `if (!this._initialized)` → `this._clearStaleIds()`
- 条件付き依存: `if (!this._shutdownBlockerAdded)` → `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`
- 条件付き依存: `if (!this._shutdownBlockerAdded)` → `this.clearAll()`
- 参照: `this._ephemeralIds`, `this._initialized`, `this._shutdownBlockerAdded`

## destroy()
- 位置: L57-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.unregisterCallback()`, `this._cancelStaleTimers()`, `this._ephemeralIds.clear()`, `this._persistIds()`
- 参照: `this._initialized`

## _cancelStaleTimers()
- 位置: L70-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ephemeralIds.has()`
- 条件付き依存: `if (!this._ephemeralIds.has(userContextId))` → `task.disarm()`
- 条件付き依存: `if (!this._ephemeralIds.has(userContextId))` → `this._deferredTasks.delete()`
- 参照: `this._deferredTasks`

## _onWindowInit()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.tabContainer.addEventListener()`

## _onWindowUninit()
- 位置: L83-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (closing)` → `this._scheduleCheck()`
- 参照: `this._ephemeralIds`

## handleEvent()
- 位置: L92-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`, `tab.getAttribute()`, `this._ephemeralIds.has()`
- 条件付き依存: `if (this._ephemeralIds.has(userContextId))` → `this._scheduleCheck()`
- 参照: `event.target`

## _scheduleCheck()
- 位置: L104-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.countContainerTabs()`, `task.arm()`, `task.disarm()`, `this._deferredTasks.getOrInsertComputed()`
- 条件付き依存: `if ( lazy.ContextualIdentityService.countContainerTabs(userContextId) == 0 )` → `this._clearData()`
- 参照: `lazy.DeferredTask`

## _clearData()
- 位置: L119-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.deleteDataFromOriginAttributesPattern()`
- XPCOM: `Services.clearData`

## clearAll()
- 位置: L128-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `promises.push()`, `this._clearData()`, `this.destroy()`
- 参照: `this._ephemeralIds`

## _clearStaleIds()
- 位置: L137-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `this._ephemeralIds.has()`
- 条件付き依存: `if (!this._ephemeralIds.has(id))` → `this._clearData()`
- XPCOM: `Services.prefs`

## _persistIds()
- 位置: L154-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`
- 参照: `this._ephemeralIds`
- XPCOM: `Services.prefs`

## flushPendingChecks()
- 位置: async L161-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `t.finalize()`, `tasks.map()`, `this._deferredTasks.clear()`, `this._deferredTasks.values()`
