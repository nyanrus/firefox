# browser/components/tabnotes/TabNotesController.sys.mjs

source: browser/components/tabnotes/TabNotesController.sys.mjs
source-hash: 667c767433b36c1e1279440476a4dd9de3b5ea4d
lines: 479

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## TabNotesControllerClass.browserFirstWindowReady()
- 位置: L74-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Services.obs.addObserver()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `this.#init().then()`
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `this.#init()`
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `this.#initWindow()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `this.#isStartupComplete`, `this.TAB_NOTES_ENABLED`
- XPCOM: `Services.obs`

## TabNotesControllerClass.#init()
- 位置: async L101-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (!this.#isInitialized)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#isInitialized)` → `lazy.TabNotes.init()`
- 参照: `this.#isInitialized`

## TabNotesControllerClass.browserWindowDelayedStartup()
- 位置: L117-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`
- 条件付き依存: `if (!this.#isStartupComplete)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `this.#initWindow()`
- 参照: `this.#isStartupComplete`, `this.TAB_NOTES_ENABLED`

## TabNotesControllerClass.#initWindow()
- 位置: L137-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EVENTS.forEach()`, `lazy.TabNotes.isEligible()`, `lazy.logConsole.debug()`, `win.addEventListener()`, `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (tab.canonicalUrl && lazy.TabNotes.isEligible(tab))` → `lazy.TabNotes.has(tab).then()`
- 条件付き依存: `if (tab.canonicalUrl && lazy.TabNotes.isEligible(tab))` → `lazy.TabNotes.has()`
- 参照: `tab.canonicalUrl`, `tab.hasTabNote`, `win.gBrowser.tabs`

## TabNotesControllerClass.browserWindowUnload()
- 位置: L159-164
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `this.#unloadWindow()`
- 条件付き依存: `if (this.TAB_NOTES_ENABLED)` → `lazy.logConsole.debug()`
- 参照: `this.TAB_NOTES_ENABLED`

## TabNotesControllerClass.#unloadWindow()
- 位置: L172-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EVENTS.forEach()`, `lazy.logConsole.debug()`, `win.gBrowser.removeTabsProgressListener()`, `win.removeEventListener()`

## TabNotesControllerClass.browserQuitApplicationGranted()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deinit()`

## TabNotesControllerClass.#deinit()
- 位置: async L194-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabNotes.deinit()`
- 条件付き依存: `if (this.#isInitialized)` → `lazy.logConsole.debug()`
- 参照: `this.#isInitialized`

## TabNotesControllerClass.handleEvent()
- 位置: L205-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `Temporal.Now.instant()`, `browser.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `lazy.TabNotes.get()`, `lazy.TabNotes.get(tab).then()`, `lazy.TabNotes.has()`, `lazy.TabNotes.has(tab).then()`, `lazy.logConsole.debug()`, `now.since()`, `now.since(note.created).total()`, `tab.dispatchEvent()`
- 条件付き依存: `if (telemetrySource)` → `Glean.tabNotes.added.record()`
- 条件付き依存: `if (telemetrySource)` → `Glean.tabNotes.edited.record()`
- 条件付き依存: `if (telemetrySource)` → `Glean.tabNotes.deleted.record()`
- 条件付き依存: `if (note)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (note)` → `Glean.tabNotes.expanded.record()`
- 参照: `event.detail`, `event.target`, `event.type`, `lazy.BrowserWindowTracker.orderedWindows`, `note.created`, `note.text.length`, `tab.canonicalUrl`, `tab.hasTabNote`, `win.gBrowser.tabs`

## TabNotesControllerClass.observe()
- 位置: L317-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DOMException.isInstance()`, `Services.obs.notifyObservers()`, `e.message.includes()`, `lazy.logConsole.debug()`, `parent?.sendAsyncMessage()`, `tab.linkedBrowser.browsingContext?.currentWindowGlobal.getActor()`, `this.#deinit()`, `this.#deinit() .then()`, `this.#init()`, `this.#init() .then()`, `this.#initWindow()`, `this.#resetTab()`, `this.#unloadWindow()`
- 条件付き依存: `if (!( DOMException.isInstance(e) && e.message.includes("Window protocol") ))` → `lazy.logConsole.error()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `win.gBrowser.tabs`
- XPCOM: `Services.obs`

## TabNotesControllerClass.onLocationChange()
- 位置: L395-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.gBrowser.getTabForBrowser()`, `lazy.logConsole.debug()`, `this.#resetTab()`
- 条件付き依存: `if ( aWebProgress.loadType & Ci.nsIDocShell.LOAD_CMD_RELOAD || aWebProgress.loadType & Ci.nsIDocShell.LOAD_CMD_HISTORY )` → `lazy.logConsole.debug()`
- 条件付き依存: `if (aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_HASHCHANGE)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (aWebProgress.loadType & Ci.nsIDocShell.LOAD_CMD_PUSHSTATE)` → `aBrowser.browsingContext?.currentWindowGlobal.getExistingActor()`
- 条件付き依存: `if (parent)` → `parent.sendAsyncMessage()`
- 条件付き依存: `if (parent)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SESSION_STORE)` → `lazy.logConsole.debug()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `Ci.nsIDocShell.LOAD_CMD_PUSHSTATE`, `Ci.nsIDocShell.LOAD_CMD_RELOAD`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_HASHCHANGE`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SESSION_STORE`, `aLocation.spec`, `aWebProgress.isTopLevel`, `aWebProgress.loadType`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabNotesControllerClass.#resetTab()
- 位置: L472-475
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab.canonicalUrl`, `tab.hasTabNote`
