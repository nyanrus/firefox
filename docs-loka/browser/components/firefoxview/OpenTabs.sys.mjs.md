# browser/components/firefoxview/OpenTabs.sys.mjs

source: browser/components/firefoxview/OpenTabs.sys.mjs
source-hash: f6e0c928c7b81edf0e8e7ddda4c12cd4cbe5d890
lines: 451

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## lastSeenActiveSort()
- 位置: L54-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.lastSeenActive`, `a.selected`, `b.lastSeenActive`, `b.selected`

## OpenTabsTarget.constructor()
- 位置: L92-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `options.exclusiveWindow`, `options.usePrivateWindows`, `this.everyWindowCallbackId`, `this.exclusiveWindow`, `this.exclusiveWindow.windowGlobalChild.innerWindowId`, `this.usePrivateWindows`

## OpenTabsTarget.exclusiveWindow()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#exclusiveWindowWeakRef?.get()`

## OpenTabsTarget.exclusiveWindow()
- 位置: L109-115
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (newValue)` → `Cu.getWeakReference()`
- 参照: `this.#exclusiveWindowWeakRef`

## OpenTabsTarget.includeWindowFilter()
- 位置: L117-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `this.#exclusiveWindowWeakRef`, `this.exclusiveWindow`, `this.usePrivateWindows`, `win.closed`, `win.gBrowser`

## OpenTabsTarget.currentWindows()
- 位置: L128-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.readyWindows.filter()`, `this.includeWindowFilter()`

## OpenTabsTarget.readyWindowsPromise()
- 位置: L137-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from( Services.wm.getEnumerator("navigator:browser") ).filter()`, `Promise.allSettled()`, `Promise.allSettled( windowList.map(win => win.delayedStartupPromise) ).then()`, `Services.wm.getEnumerator()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `windowList.filter()`, `windowList.map()`
- 参照: `this.#exclusiveWindowWeakRef`, `this.exclusiveWindow`, `this.includeWindowFilter`, `this.usePrivateWindows`, `win.delayedStartupPromise`
- XPCOM: `Services.wm`

## OpenTabsTarget.haveListenersForEvent()
- 位置: L157-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.els.hasListenersFor()`
- XPCOM: `Services.els`

## OpenTabsTarget.haveAnyListeners()
- 位置: L168-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.haveListenersForEvent()`

## OpenTabsTarget.addEventListener()
- 位置: L181-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.addEventListener()`
- 条件付き依存: `if (!hadListeners && this.haveAnyListeners)` → `this.start()`
- 参照: `this.haveAnyListeners`

## OpenTabsTarget.removeEventListener()
- 位置: L196-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.removeEventListener()`
- 条件付き依存: `if (hadListeners && !this.haveAnyListeners)` → `this.stop()`
- 参照: `this.haveAnyListeners`

## OpenTabsTarget.start()
- 位置: L209-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `this.#unwatchWindow()`, `this.#watchWindow()`
- 参照: `this.#started`, `this.everyWindowCallbackId`

## OpenTabsTarget.stop()
- 位置: L225-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `changedWindows.clear()`, `sourceEvents.clear()`, `this.#dispatchChangesTask?.disarm()`, `this.#watchedWindows.clear()`
- 条件付き依存: `if (this.#started)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this.#changedWindowsByType`, `this.#sourceEventsByType`, `this.#started`, `this.everyWindowCallbackId`

## OpenTabsTarget.#watchWindow()
- 位置: L244-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabContainer.addEventListener()`, `this.#scheduleEventDispatch()`, `this.#watchedWindows.add()`, `this.includeWindowFilter()`, `win.addEventListener()`
- 参照: `win.gBrowser`, `win.windowGlobalChild.innerWindowId`

## OpenTabsTarget.#unwatchWindow()
- 位置: L276-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#watchedWindows.has()`
- 条件付き依存: `if (this.#watchedWindows.has(win))` → `this.#watchedWindows.delete()`
- 条件付き依存: `if (this.#watchedWindows.has(win))` → `tabContainer.removeEventListener()`
- 条件付き依存: `if (this.#watchedWindows.has(win))` → `win.removeEventListener()`
- 条件付き依存: `if (this.#watchedWindows.has(win))` → `this.#scheduleEventDispatch()`
- 参照: `win.gBrowser`, `win.windowGlobalChild.innerWindowId`

## OpenTabsTarget.#scheduleEventDispatch()
- 位置: L312-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#changedWindowsByType[eventType].add()`, `this.#dispatchChangesTask.arm()`, `this.#sourceEventsByType[eventType].add()`, `this.haveListenersForEvent()`
- 条件付き依存: `if (!this.#dispatchChangesTask)` → `this.#dispatchChanges()`
- 参照: `lazy.DeferredTask`, `this.#changedWindowsByType`, `this.#dispatchChangesTask`, `this.#sourceEventsByType`

## OpenTabsTarget.#dispatchChanges()
- 位置: L329-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `sourceEvents?.clear()`, `this.#dispatchChangesTask?.disarm()`, `this.haveListenersForEvent()`
- 条件付き依存: `if (this.haveListenersForEvent(eventType) && changedWindowIds.size)` → `this.dispatchEvent()`
- 条件付き依存: `if (this.haveListenersForEvent(eventType) && changedWindowIds.size)` → `changedWindowIds.clear()`
- 参照: `changedWindowIds.size`, `this.#changedWindowsByType`, `this.#sourceEventsByType`

## OpenTabsTarget.getTabsForWindow()
- 位置: L355-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.currentWindows.includes()`
- 条件付き依存: `if (this.currentWindows.includes(win))` → `win.gBrowser.openTabs.filter()`
- 条件付き依存: `if (this.currentWindows.includes(win))` → `tabs.toSorted()`
- 参照: `tab.hidden`

## OpenTabsTarget.getAllTabs()
- 位置: L368-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.currentWindows.flatMap()`, `this.getTabsForWindow()`

## OpenTabsTarget.getRecentTabs()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAllTabs()`, `this.getAllTabs().sort()`

## OpenTabsTarget.handleEvent()
- 位置: L380-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getClassName()`, `TAB_ATTRS_TO_WATCH.includes()`, `TAB_CHANGE_EVENTS.includes()`, `TAB_RECENCY_CHANGE_EVENTS.includes()`, `detail.changed.some()`
- 条件付き依存: `if (TAB_RECENCY_CHANGE_EVENTS.includes(type))` → `this.#scheduleEventDispatch()`
- 条件付き依存: `if (TAB_CHANGE_EVENTS.includes(type))` → `this.#scheduleEventDispatch()`
- 参照: `target.documentGlobal`, `win.windowGlobalChild.innerWindowId`

## constructor()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## observe()
- 位置: L414-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.perWindowInstances.get()`
- 条件付き依存: `if (winTarget)` → `winTarget.stop()`
- 条件付き依存: `if (winTarget)` → `this.perWindowInstances.delete()`

## getTabsTargetForWindow()
- 位置: L430-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gExclusiveWindows.perWindowInstances.get()`, `gExclusiveWindows.perWindowInstances.set()`
