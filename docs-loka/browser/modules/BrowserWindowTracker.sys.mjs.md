# browser/modules/BrowserWindowTracker.sys.mjs

source: browser/modules/BrowserWindowTracker.sys.mjs
source-hash: d90f63e373a7cdc7caee4ff5b9d94a5a57febece
lines: 534

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`

## debug()
- 位置: L44-48
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (DEBUG)` → `dump()`

## _updateCurrentBrowserId()
- 位置: L50-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-PRUint64;1"].createInstance()`, `Services.obs.notifyObservers()`, `_trackedWindows.find()`
- 条件付き依存: `if (DEBUG)` → `debug()`
- 参照: `Ci.nsISupportsPRUint64`, `browser.browserId`, `browser.currentURI?.spec`, `browser.documentGlobal`, `idWrapper.data`, `w.STATE_MINIMIZED`, `w.closed`, `w.windowState`
- XPCOM: [`nsISupportsPRUint64`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRUint64;1` / `Services.obs`

## _handleEvent()
- 位置: L81-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WindowHelper.onActivate()`, `WindowHelper.removeWindow()`, `_updateCurrentBrowserId()`
- 条件付き依存: `if ( event.target.documentGlobal.gBrowser.selectedBrowser === event.target.linkedBrowser )` → `_updateCurrentBrowserId()`
- 参照: `event.currentTarget`, `event.target`, `event.target.documentGlobal.gBrowser.selectedBrowser`, `event.target.linkedBrowser`, `event.type`

## _trackWindowOrder()
- 位置: L108-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_trackedWindows.unshift()`

## _untrackWindowOrder()
- 位置: L112-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_trackedWindows.indexOf()`
- 条件付き依存: `if (idx >= 0)` → `_trackedWindows.splice()`

## topicObserved()
- 位置: L119-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## observer()
- 位置: L121-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `checkFn()`, `reject()`, `resolve()`
- XPCOM: `Services.obs`

## addWindow()
- 位置: L141-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_EVENTS.forEach()`, `WINDOW_EVENTS.forEach()`, `_trackWindowOrder()`, `_updateCurrentBrowserId()`, `window.addEventListener()`, `window.gBrowser.tabContainer.addEventListener()`
- 参照: `window.gBrowser.selectedBrowser`

## removeWindow()
- 位置: L156-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_EVENTS.forEach()`, `WINDOW_EVENTS.forEach()`, `_untrackWindowOrder()`, `window.gBrowser.tabContainer.removeEventListener()`, `window.removeEventListener()`

## onActivate()
- 位置: L168-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_trackWindowOrder()`, `_untrackWindowOrder()`, `_updateCurrentBrowserId()`
- 参照: `window.gBrowser.selectedBrowser`

## getTopWindow()
- 位置: L207-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.document.documentElement.hasAttribute()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.gPreferWindowsOnCurrentVirtualDesktop`, `options.allowFromInactiveWorkspace`, `options.allowPopups`, `options.allowTaskbarTabs`, `options.private`, `win.STATE_MINIMIZED`, `win.closed`, `win.isCloaked`, `win.toolbar.visible`, `win.windowState`

## getPendingWindow()
- 位置: L263-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pendingWindows.values()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `options.private`, `pending.deferred.promise`, `pending.isPrivate`

## registerOpeningWindow()
- 位置: L286-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `this.pendingWindows.set()`
- XPCOM: `Services.obs`

## observer()
- 位置: L297-306
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (window.browsingContext == aSubject)` → `this.pendingWindows.get()`
- 条件付き依存: `if (pending)` → `this.pendingWindows.delete()`
- 条件付き依存: `if (pending)` → `pending.deferred.resolve()`
- 条件付き依存: `if (window.browsingContext == aSubject)` → `Services.obs.removeObserver()`
- 参照: `window.browsingContext`
- XPCOM: `Services.obs`

## openWindow()
- 位置: L337-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.ww.openWindow()`, `lazy.AIWindow.handleAIWindowOptions()`, `lazy.HomePage.get()`, `this.registerOpeningWindow()`, `win.addEventListener()`
- 条件付き依存: `if (!args)` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if ( Services.prefs.getIntPref("browser.startup.page") == 1 && loadURIString == lazy.HomePage.get() )` → `Services.obs.notifyObservers()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsISupportsString`, `args.data`, `lazy.BrowserHandler.defaultArgs`, `lazy.PrivateBrowsingUtils.enabled`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `openerWindow?.STATE_MAXIMIZED`, `openerWindow?.windowState`
- XPCOM: [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1` / `Services.obs` / `Services.prefs` / `Services.ww`

## promiseOpenWindow()
- 位置: async L432-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openWindow()`, `topicObserved()`

## windowCount()
- 位置: L444-446
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `_trackedWindows.length`

## orderedWindows()
- 位置: L448-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getOrderedWindows()`

## getOrderedWindows()
- 位置: L462-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `nonMinimized.concat()`, `windows.filter()`
- 条件付き依存: `if (w.windowState == w.STATE_MINIMIZED)` → `minimized.push()`
- 条件付き依存: `if (!(w.windowState == w.STATE_MINIMIZED))` → `nonMinimized.push()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `w.STATE_MINIMIZED`, `w.windowState`

## getAllVisibleTabs()
- 位置: L490-502
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tab.linkedPanel)` → `tabs.push()`
- 参照: `BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser`, `tab.linkedPanel`, `win.gBrowser.visibleTabs`

## track()
- 位置: L504-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WindowHelper.addWindow()`, `this.pendingWindows.get()`
- 条件付き依存: `if (pending)` → `this.pendingWindows.delete()`
- 条件付き依存: `if (pending)` → `window.delayedStartupPromise.then()`
- 条件付き依存: `if (pending)` → `pending.deferred.resolve()`

## getBrowserById()
- 位置: L516-525
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser`, `tab.linkedBrowser.browserId`, `tab.linkedPanel`, `win.gBrowser.visibleTabs`

## untrackForTestsOnly()
- 位置: L530-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WindowHelper.removeWindow()`
