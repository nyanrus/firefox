# browser/components/tabbrowser/TabUnloader.sys.mjs

source: browser/components/tabbrowser/TabUnloader.sys.mjs
source-hash: ac31a260565465c062b31fdd204acc86324fefbe
lines: 517

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.prefs.getIntPref()`, `XPCOMUtils.declareLazy()`

## isNonDiscardable()
- 位置: L53-59
- 役割: (未記入)
- 触るとき: (未記入)

## isPinned()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)

## isLoading()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)

## usingPictureInPicture()
- 位置: L69-72
- 役割: (未記入)
- 触るとき: (未記入)

## playingMedia()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)

## usingWebRTC()
- 位置: L78-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.browsingContext?.currentWindowGlobal?.hasActivePeerConnections()`, `lazy.webrtcUI.browserHasStreams()`

## isPrivate()
- 位置: L92-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`

## getMinTabCount()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)

## getNow()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## iterateTabs()
- 位置: L106-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`
- XPCOM: `Services.wm`

## iterateBrowsingContexts()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.iterateBrowsingContexts()`

## iterateProcesses()
- 位置: L121-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.iterateBrowsingContexts()`

## calculateMemoryUsage()
- 位置: async L141-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.requestProcInfo()`, `processMap.get()`
- 条件付き依存: `if (!processInfo)` → `processMap.set()`

## init()
- 位置: L164-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/xpcom/memory-watcher;1"].getService()`, `watcher.registerTabUnloader()`
- XPCOM: [`nsIAvailableMemoryWatcherBase`](../../../xpcom/base/nsIAvailableMemoryWatcherBase.idl.md) / `@mozilla.org/xpcom/memory-watcher;1`

## isDiscardable()
- 位置: L171-176
- 役割: (未記入)
- 触るとき: (未記入)

## unloadTabAsync()
- 位置: async L179-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/xpcom/memory-watcher;1"].getService()`, `Services.prefs.getBoolPref()`, `this.unloadLeastRecentlyUsedTab()`, `watcher.onUnloadAttemptCompleted()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("browser.tabs.unloadOnLowMemory", true))` → `watcher.onUnloadAttemptCompleted()`
- 条件付き依存: `if (this._isUnloading)` → `Services.console.logStringMessage()`
- 条件付き依存: `if (this._isUnloading)` → `watcher.onUnloadAttemptCompleted()`
- XPCOM: [`nsIAvailableMemoryWatcherBase`](../../../xpcom/base/nsIAvailableMemoryWatcherBase.idl.md) / `@mozilla.org/xpcom/memory-watcher;1` / `Services.console` / `Services.prefs`

## getSortedTabs()
- 位置: async L239-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `determineTabBaseWeight()`, `tabMethods.getMinTabCount()`, `tabMethods.getNow()`, `tabMethods.iterateTabs()`, `tabs.sort()`, `this.isDiscardable()`
- 条件付き依存: `if (weight != -1)` → `tabs.push()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `getAllProcesses()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `tabs.splice()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `adjustForResourceUse()`
- 条件付き依存: `if (lowestWeightedCount > 1)` → `tabs.concat()`

## unloadLeastRecentlyUsedTab()
- 位置: async L322-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabInfo.gBrowser.discardBrowser()`, `tabInfo.gBrowser.prepareDiscardBrowser()`, `this.getSortedTabs()`, `this.isDiscardable()`
- 条件付き依存: `if (tabInfo.gBrowser.discardBrowser(tabInfo.tab))` → `Services.console.logStringMessage()`
- 条件付き依存: `if (tabInfo.gBrowser.discardBrowser(tabInfo.tab))` → `tabInfo.tab.updateLastUnloadedByTabUnloader()`
- XPCOM: `Services.console`

## determineTabBaseWeight()
- 位置: L359-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabMethods[criteriaType[CRITERIA_METHOD]]()`

## getAllProcesses()
- 位置: L390-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `processMap.get()`, `tab.processes.get()`, `tabMethods.iterateProcesses()`
- 条件付き依存: `if (processInfo)` → `processInfo.tabSet.add()`
- 条件付き依存: `if (!(processInfo))` → `processMap.set()`
- 条件付き依存: `if (!(tabProcessEntry))` → `tab.processes.set()`

## adjustForResourceUse()
- 位置: async L455-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.processes.values()`, `tabMethods.calculateMemoryUsage()`, `tabs.sort()`
