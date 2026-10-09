# browser/components/taskbartabs/TaskbarTabsWindowManager.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsWindowManager.sys.mjs
source-hash: 9991e5ba8c49c0fdff28152760266d57e23ec25c
lines: 377

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.createInstance()`

## TaskbarTabsWindowManager.replaceTabWithWindow()
- 位置: async L48-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`, `Glean.webApp.moveToTaskbar.record()`, `args.appendElement()`, `extraOptions.setPropertyAsAString()`, `getTabId()`, `getWindowId()`, `this.#openWindow()`, `this.#tabOriginMap.set()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `extraOptions.setPropertyAsAString()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `getLinuxWindowClass()`
- 参照: `AppConstants.platform`, `Ci.nsIMutableArray`, `Ci.nsIWritablePropertyBag2`, `aTab.documentGlobal`, `aTaskbarTab.id`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIWritablePropertyBag2`](../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1`

## TaskbarTabsWindowManager.openWindow()
- 位置: async L83-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`, `Cc["@mozilla.org/supports-PRUint32;1"].createInstance()`, `Cc["@mozilla.org/supports-string;1"].createInstance()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `args.appendElement()`, `extraOptions.setPropertyAsAString()`, `this.#openWindow()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `extraOptions.setPropertyAsAString()`
- 条件付き依存: `if (AppConstants.platform === "linux")` → `getLinuxWindowClass()`
- 参照: `AppConstants.platform`, `Ci.nsIMutableArray`, `Ci.nsISupportsPRUint32`, `Ci.nsISupportsString`, `Ci.nsIWritablePropertyBag2`, `aTaskbarTab.id`, `aTaskbarTab.startUrl`, `aTaskbarTab.userContextId`, `url.data`, `userContextId.data`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsPRUint32`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-PRUint32;1` / `@mozilla.org/supports-string;1` / `Services.scriptSecurityManager`

## TaskbarTabsWindowManager.#openWindow()
- 位置: async L128-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webApp.activate.record()`, `lazy.BrowserWindowTracker.promiseOpenWindow()`, `this.#attachWindowFocusTelemetry()`, `this.#trackWindow()`, `win.focus()`, `win.gBrowser.getBrowserForTab()`, `win.gBrowser.tabs.forEach()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `lazy.WindowsUIUtils.setWindowIcon()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `Services.sysinfo.getProperty()`
- 条件付き依存: `if (pfn)` → `lazy.WinTaskbar.setGroupIdForWindow()`
- 条件付き依存: `if (!(pfn))` → `lazy.WinTaskbar.setGroupIdForWindow()`
- 参照: `AppConstants.platform`, `aTaskbarTab.id`, `browser.browsingContext.displayMode`
- XPCOM: `Services.sysinfo`

## TaskbarTabsWindowManager.#trackWindow()
- 位置: L176-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.addEventListener()`, `getWindowId()`, `openWindows.add()`, `this.#openWindows.get()`, `this.#untrackWindow()`
- 条件付き依存: `if (typeof openWindows === "undefined")` → `this.#openWindows.set()`

## TaskbarTabsWindowManager.#untrackWindow()
- 位置: L194-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getWindowId()`, `openWindows.delete()`, `this.#openWindows.get()`
- 条件付き依存: `if (openWindows.size === 0)` → `this.#openWindows.delete()`
- 参照: `openWindows.size`

## TaskbarTabsWindowManager.#attachWindowFocusTelemetry()
- 位置: L208-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.addEventListener()`, `focused()`

## focused()
- 位置: L211-215
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (timerId == null)` → `Glean.webApp.usageTime.start()`

## blur()
- 位置: L217-223
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (timerId != null)` → `Glean.webApp.usageTime.stopAndAccumulate()`

## TaskbarTabsWindowManager.ejectWindow()
- 位置: async L242-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.webApp.eject.record()`, `getTabId()`, `getWindowId()`, `lazy.BrowserWindowTracker.getOrderedWindows()`, `lazy.TaskbarTabsUtils.getTaskbarTabIdFromWindow()`, `lazy.logConsole.info()`, `this.#tabOriginMap.delete()`, `this.#tabOriginMap.get()`, `this.#untrackWindow()`, `win.focus()`, `win.gBrowser.getBrowserForTab()`, `windowList.find()`
- 条件付き依存: `if (!(!taskbarTabId))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (matching)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!win)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (win)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (win)` → `win.gBrowser.adoptTab()`
- 条件付き依存: `if (!(win))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!(win))` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 参照: `aWindow.gBrowser.tabs`, `browser.browsingContext.displayMode`, `win.gBrowser.openTabs.length`, `win.gBrowser.tabs`

## TaskbarTabsWindowManager.getCountForId()
- 位置: L320-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openWindows.get()`
- 参照: `this.#openWindows.get(aId)?.size`

## TaskbarTabsWindowManager.testOnlyMockUIUtils()
- 位置: L329-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`
- 参照: `Cu.isInAutomation`

## TaskbarTabsWindowManager.get()
- 位置: L335-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-ui-utils;1"].getService()`
- 参照: `Ci.nsIWindowsUIUtils`
- XPCOM: `nsIWindowsUIUtils` / `@mozilla.org/windows-ui-utils;1`

## getTabId()
- 位置: L353-355
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aTab.permanentKey`

## getWindowId()
- 位置: L363-365
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aWindow.docShell.outerWindowID`

## getLinuxWindowClass()
- 位置: L367-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TaskbarTabsUtils._determineNewDesktopEntryName()`
- 条件付き依存: `if (aTaskbarTab.shortcutRelativePath)` → `aTaskbarTab.shortcutRelativePath.split()`
- 条件付き依存: `if (aTaskbarTab.shortcutRelativePath)` → `subdir[subdir.length - 1].replace()`
- 参照: `aTaskbarTab.id`, `aTaskbarTab.shortcutRelativePath`, `subdir.length`
