# browser/extensions/ipp-activator/extension/bg.js

source: browser/extensions/ipp-activator/extension/bg.js
source-hash: e7239701fc26933e1e5178044cdda7804cc1677c
lines: 450

## <module>
- 役割: (未記入)

## IPPAddonActivator.constructor()
- 位置: L27-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.ippActivator.onDynamicTabBreakagesUpdated.addListener()`, `browser.ippActivator.onDynamicWebRequestBreakagesUpdated.addListener()`, `this.#init()`, `this.#ippExceptionsChanged.bind()`, `this.#loadAndRebuildBreakages()`, `this.#loadAndRebuildBreakages().then()`, `this.#onRequest.bind()`, `this.#tabActivated.bind()`, `this.#tabRemoved.bind()`, `this.#tabUpdated.bind()`
- 参照: `this.ippExceptionsChanged`, `this.onRequest`, `this.tabActivated`, `this.tabRemoved`, `this.tabUpdated`

## IPPAddonActivator.#init()
- 位置: async L46-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registerListeners()`
- 参照: `this.#initialized`

## IPPAddonActivator.#fetchBaseBreakages()
- 位置: async L57-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `fetch()`, `res.json()`

## IPPAddonActivator.#loadAndRebuildBreakages()
- 位置: async L67-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `browser.ippActivator.getDynamicTabBreakages()`, `browser.ippActivator.getDynamicWebRequestBreakages()`, `console.warn()`
- 条件付き依存: `if (!this.#tabBaseBreakages)` → `browser.ippActivator.getTabBreakagesUrl()`
- 条件付き依存: `if (!this.#tabBaseBreakages)` → `this.#fetchBaseBreakages()`
- 条件付き依存: `if (!this.#tabBaseBreakages)` → `browser.runtime.getURL()`
- 条件付き依存: `if (!this.#webrequestBaseBreakages)` → `browser.ippActivator.getWebRequestBreakagesUrl()`
- 条件付き依存: `if (!this.#webrequestBaseBreakages)` → `this.#fetchBaseBreakages()`
- 条件付き依存: `if (!this.#webrequestBaseBreakages)` → `browser.runtime.getURL()`
- 条件付き依存: `if (this.#initialized)` → `this.#registerListeners()`
- 参照: `this.#initialized`, `this.#tabBaseBreakages`, `this.#tabBreakages`, `this.#webrequestBaseBreakages`, `this.#webrequestBreakages`

## IPPAddonActivator.#registerListeners()
- 位置: L110-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `browser.ippActivator.onIPPExceptionsChanged.addListener()`, `this.#unregisterListeners()`
- 条件付き依存: `if (needTabUpdated)` → `browser.tabs.onUpdated.addListener()`
- 条件付き依存: `if (needWebRequest)` → `browser.webRequest.onBeforeRequest.addListener()`
- 条件付き依存: `if (needActivation)` → `browser.tabs.onActivated.addListener()`
- 条件付き依存: `if (needActivation)` → `browser.tabs.onRemoved.addListener()`
- 参照: `this.#tabBreakages`, `this.#tabBreakages.length`, `this.#webrequestBreakages`, `this.#webrequestBreakages.length`, `this.ippExceptionsChanged`, `this.onRequest`, `this.tabActivated`, `this.tabRemoved`, `this.tabUpdated`

## IPPAddonActivator.#unregisterListeners()
- 位置: L150-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.ippActivator.onIPPExceptionsChanged.removeListener()`, `browser.tabs.onActivated.hasListener()`, `browser.tabs.onRemoved.hasListener()`, `browser.tabs.onUpdated.hasListener()`, `browser.webRequest.onBeforeRequest.hasListener()`, `this.#pendingTabs.clear()`, `this.#pendingWebRequests.clear()`
- 条件付き依存: `if (browser.tabs.onUpdated.hasListener(this.tabUpdated))` → `browser.tabs.onUpdated.removeListener()`
- 条件付き依存: `if (browser.tabs.onActivated.hasListener(this.tabActivated))` → `browser.tabs.onActivated.removeListener()`
- 条件付き依存: `if (browser.tabs.onRemoved.hasListener(this.tabRemoved))` → `browser.tabs.onRemoved.removeListener()`
- 条件付き依存: `if (browser.webRequest.onBeforeRequest.hasListener(this.onRequest))` → `browser.webRequest.onBeforeRequest.removeListener()`
- 参照: `this.ippExceptionsChanged`, `this.onRequest`, `this.tabActivated`, `this.tabRemoved`, `this.tabUpdated`

## IPPAddonActivator.#ippExceptionsChanged()
- 位置: async L175-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Promise.allSettled()`, `browser.ippActivator.hasExclusion()`, `browser.tabs.get()`, `tabIds.map()`, `this.#stateByTab.keys()`
- 条件付き依存: `if (await browser.ippActivator.hasExclusion(tab.url))` → `this.#dropTabState()`
- 参照: `tab.url`, `tab?.url`, `this.#stateByTab.size`

## IPPAddonActivator.#tabUpdated()
- 位置: async L197-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeNotify()`
- 条件付き依存: `if ("url" in changeInfo)` → `browser.ippActivator.getBaseDomainFromURL()`
- 条件付き依存: `if ("url" in changeInfo)` → `this.#stateByTab.get()`
- 条件付き依存: `if ( entry && entry.domain !== info.baseDomain && entry.domain !== info.host )` → `this.#dropTabState()`
- 条件付き依存: `if ("url" in changeInfo)` → `this.#pendingWebRequests.delete()`
- 条件付き依存: `if (!tab.active)` → `this.#pendingTabs.add()`
- 参照: `changeInfo.status`, `changeInfo.url`, `entry.domain`, `info.baseDomain`, `info.host`, `tab.active`, `tab.url`, `tab?.url`, `this.#tabBreakages`

## IPPAddonActivator.#tabActivated()
- 位置: async L242-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `browser.tabs.get()`, `this.#maybeNotify()`, `this.#pendingTabs.delete()`, `this.#pendingTabs.has()`, `this.#pendingWebRequests.delete()`, `this.#pendingWebRequests.get()`
- 参照: `pendingWrUrls.length`, `tab.active`, `tab.url`, `this.#tabBreakages`, `this.#webrequestBreakages`

## IPPAddonActivator.#maybeNotify()
- 位置: async L280-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `b.domains.includes()`, `breakages.find()`, `browser.ippActivator.getBaseDomainFromURL()`, `browser.ippActivator.getNotifiedDomains()`, `browser.ippActivator.hasExclusion()`, `notified.includes()`, `this.#stateByTab.get()`, `this.#updateNotification()`
- 条件付き依存: `if (!info.baseDomain && !info.host)` → `this.#dropTabState()`
- 条件付き依存: `if (!breakage)` → `breakages.find()`
- 条件付き依存: `if (!breakage)` → `Array.isArray()`
- 条件付き依存: `if (!breakage)` → `b.domains.includes()`
- 条件付き依存: `if (!breakage)` → `this.#dropTabState()`
- 条件付き依存: `if (await browser.ippActivator.hasExclusion(url))` → `this.#dropTabState()`
- 条件付き依存: `if (Array.isArray(notified) && notified.includes(domain))` → `this.#dropTabState()`
- 条件付き依存: `if (entry && entry.domain !== domain)` → `this.#dropTabState()`
- 条件付き依存: `if (breakage.condition !== undefined)` → `factory.create()`
- 条件付き依存: `if (breakage.condition !== undefined)` → `condition.init()`
- 条件付き依存: `if (!entry)` → `this.#stateByTab.set()`
- 条件付き依存: `if (condition)` → `condition.onChange()`
- 条件付き依存: `if (condition)` → `this.#stateByTab.get()`
- 条件付き依存: `if (condition)` → `this.#updateNotification()`
- 参照: `b.domains`, `breakage.condition`, `breakage.l10nId`, `entry.domain`, `info.baseDomain`, `info.host`, `tab.id`

## IPPAddonActivator.#updateNotification()
- 位置: L346-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `browser.ippActivator .showMessage()`, `browser.ippActivator .showMessage({ l10nId: entry.l10nId }, tabId) .then()`, `browser.ippActivator.addNotifiedDomain()`, `entry.condition.check()`, `this.#dropTabState()`, `this.#stateByTab.entries()`, `this.#stateByTab.get()`, `toClose.map()`
- 条件付き依存: `if (entry.shown)` → `browser.ippActivator.hideMessage()`
- 条件付き依存: `if (e.domain === entry.domain)` → `toClose.push()`
- 参照: `e.domain`, `entry.condition`, `entry.domain`, `entry.l10nId`, `entry.shown`

## IPPAddonActivator.#dropTabState()
- 位置: async L394-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stateByTab.delete()`, `this.#stateByTab.get()`
- 条件付き依存: `if (entry.condition)` → `entry.condition.uninit()`
- 条件付き依存: `if (entry.shown)` → `browser.ippActivator.hideMessage()`
- 参照: `entry.condition`, `entry.shown`

## IPPAddonActivator.#onRequest()
- 位置: async L408-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.tabs.get()`
- 条件付き依存: `if (tab.active)` → `this.#maybeNotify()`
- 条件付き依存: `if (!(tab.active))` → `this.#pendingWebRequests.get()`
- 条件付き依存: `if (!(tab.active))` → `set.add()`
- 条件付き依存: `if (!(tab.active))` → `this.#pendingWebRequests.set()`
- 参照: `details.tabId`, `details.url`, `tab.active`, `this.#webrequestBreakages`

## IPPAddonActivator.#tabRemoved()
- 位置: async L436-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pendingTabs.delete()`, `this.#pendingWebRequests.delete()`, `this.#stateByTab.delete()`, `this.#stateByTab.get()`
- 条件付き依存: `if (entry?.condition)` → `entry.condition.uninit()`
- 参照: `entry?.condition`
