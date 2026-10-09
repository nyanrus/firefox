# browser/components/pagedata/PageDataService.sys.mjs

source: browser/components/pagedata/PageDataService.sys.mjs
source-hash: b75d192e341c57d82d624e93e845a1fe8e472869
lines: 570

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.createInstance()`

## shift()
- 位置: L46-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `iter.next()`, `set.delete()`, `set.values()`

## PageDataCache.set()
- 位置: L89-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cache.get()`
- 参照: `entry.pageData`

## PageDataCache.get()
- 位置: L105-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cache.get()`
- 参照: `entry?.pageData`

## PageDataCache.lockData()
- 位置: L119-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cache.get()`
- 条件付き依存: `if (entry)` → `entry.actors.add()`
- 条件付き依存: `if (!(entry))` → `this.#cache.set()`

## PageDataCache.unlockData()
- 位置: L139-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entry.actors.delete()`
- 条件付き依存: `if (url)` → `this.#cache.get()`
- 条件付き依存: `if (url)` → `entries.push()`
- 条件付き依存: `if (entry.actors.size == 0)` → `this.#cache.delete()`
- 参照: `entry.actors.size`, `this.#cache`

## PageDataService.constructor()
- 位置: L227-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`, `this.#startBackgroundWorkers()`

## PageDataService.init()
- 位置: L244-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.registerWindowActor()`, `Services.prefs.getBoolPref()`, `lazy.idleService.addIdleObserver()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (!win.closed)` → `tab.linkedBrowser.browsingContext?.currentWindowGlobal.getActor()`
- 条件付き依存: `if (!win.closed)` → `parent.sendAsyncMessage()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `lazy.fetchIdleTime`, `win.closed`, `win.gBrowser.tabs`
- XPCOM: `Services.prefs`

## PageDataService.uninit()
- 位置: L286-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`

## PageDataService.#trackBrowser()
- 位置: L296-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browsers.delete()`, `this.#trackedWindows.delete()`, `this.#trackedWindows.get()`, `this.#trackedWindows.set()`, `this.unlockEntry()`, `window.addEventListener()`
- 条件付き依存: `if (browsers)` → `browsers.add()`
- 参照: `browser.documentGlobal`, `tab.linkedBrowser`

## PageDataService.lockEntry()
- 位置: L336-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pageDataCache.lockData()`

## PageDataService.unlockEntry()
- 位置: L348-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pageDataCache.unlockData()`

## PageDataService.pageLoaded()
- 位置: async L361-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_PROTOCOLS.has()`, `actor.collectPageData()`, `lazy.logConsole.error()`, `this.#backgroundBrowsers.get()`, `this.#isATabBrowser()`
- 条件付き依存: `if (backgroundResolve)` → `backgroundResolve()`
- 条件付き依存: `if (data)` → `this.#trackBrowser()`
- 条件付き依存: `if (data)` → `this.lockEntry()`
- 条件付き依存: `if (data)` → `this.pageDataDiscovered()`
- 参照: `actor.browsingContext?.embedderElement`, `data.url`, `new URL(url).protocol`

## PageDataService.pageDataDiscovered()
- 位置: L407-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#pageDataCache.set()`, `this.emit()`
- 参照: `pageData.data`, `pageData.url`

## PageDataService.getCached()
- 位置: L430-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pageDataCache.get()`

## PageDataService.fetchPageData()
- 位置: async L443-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `actor.collectPageData()`, `browser.fixupAndLoadURIString()`, `lazy.HiddenBrowserManager.withHiddenBrowser()`, `this.#backgroundBrowsers.delete()`, `this.#backgroundBrowsers.set()`
- XPCOM: `Services.scriptSecurityManager`

## PageDataService.observe()
- 位置: L471-483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#startBackgroundWorkers()`
- 参照: `this.#userIsIdle`

## PageDataService.#startBackgroundWorkers()
- 位置: L489-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#backgroundFetch()`
- 参照: `this.#backgroundFetches`, `this.#backgroundQueue.size`, `this.#userIsIdle`, `this.MAX_BACKGROUND_FETCHES`

## PageDataService.#backgroundFetch()
- 位置: async L511-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `shift()`, `this.fetchPageData()`
- 条件付き依存: `if (pageData)` → `this.#pageDataCache.set()`
- 条件付き依存: `if (pageData)` → `this.emit()`
- 参照: `this.#backgroundFetches`, `this.#backgroundQueue`, `this.#userIsIdle`, `this.MAX_BACKGROUND_FETCHES`

## PageDataService.queueFetch()
- 位置: L552-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#backgroundQueue.add()`, `this.#startBackgroundWorkers()`

## PageDataService.#isATabBrowser()
- 位置: L566-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.documentGlobal.gBrowser?.getTabForBrowser()`
