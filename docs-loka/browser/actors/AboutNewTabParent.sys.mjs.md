# browser/actors/AboutNewTabParent.sys.mjs

source: browser/actors/AboutNewTabParent.sys.mjs
source-hash: 1b0427ef7444efa08c1ba18b207cf2285ae98f07
lines: 222

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutNewTabParent.loadedTabs()
- 位置: L17-19
- 役割: (未記入)
- 触るとき: (未記入)

## AboutNewTabParent.getTabDetails()
- 位置: L21-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gLoadedTabs.get()`
- 参照: `this.browsingContext.top.embedderElement`

## AboutNewTabParent.handleEvent()
- 位置: L26-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "SwapDocShells")` → `gLoadedTabs.get()`
- 条件付き依存: `if (tabDetails)` → `gLoadedTabs.delete()`
- 条件付き依存: `if (tabDetails)` → `gLoadedTabs.set()`
- 条件付き依存: `if (tabDetails)` → `oldBrowser.removeEventListener()`
- 条件付き依存: `if (tabDetails)` → `newBrowser.addEventListener()`
- 参照: `event.detail`, `event.type`, `tabDetails.browser`, `this.browsingContext.top.embedderElement`

## AboutNewTabParent.makeTransientIfDisabledAndInitial()
- 位置: L48-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `sh.getEntryAtIndex()`
- 条件付き依存: `if (entry.URI.spec === "about:newtab")` → `entry.setTransient()`
- 参照: `entry.URI.spec`, `sh.count`, `this.browsingContext.sessionHistory`
- XPCOM: `Services.prefs`

## AboutNewTabParent.receiveMessage()
- 位置: async L64-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addEventListener()`, `gLoadedTabs.delete()`, `gLoadedTabs.set()`, `rendererActor.assignRenderer()`, `tabDetails.browser.removeEventListener()`, `this.browsingContext.currentWindowGlobal.getActor()`, `this.getTabDetails()`, `this.makeTransientIfDisabledAndInitial()`, `this.notifyActivityStreamChannel()`
- 条件付き依存: `if (!browsingContext.isDiscarded)` → `lazy.ASRouter.sendTriggerMessage()`
- 条件付き依存: `if (!tabDetails)` → `this.getByBrowsingContext()`
- 参照: `browsingContext.isDiscarded`, `browsingContext.top.embedderElement`, `lazy.ASRouter.waitForInitialized`, `lazy.AboutNewTab.activityStream`, `lazy.AboutNewTab.activityStreamPromise`, `message.data.portID`, `message.data.url`, `message.name`, `tabDetails.browser`, `this.browsingContext`

## AboutNewTabParent.notifyActivityStreamChannel()
- 位置: L161-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `channel[name]()`, `this.getChannel()`
- 条件付き依存: `if (!tabDetails)` → `this.getTabDetails()`
- 条件付き依存: `if (!channel)` → `AboutNewTabParent.#queuedMessages.push()`
- 参照: `message.data`

## AboutNewTabParent.getByBrowsingContext()
- 位置: L191-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutNewTabParent.loadedTabs.values()`
- 参照: `tabDetails.browsingContext`

## AboutNewTabParent.getChannel()
- 位置: L201-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.activityStream?.store?.getMessageChannel()`

## AboutNewTabParent.flushQueuedMessagesFromContent()
- 位置: L214-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.notifyActivityStreamChannel()`
- 参照: `AboutNewTabParent.#queuedMessages`
