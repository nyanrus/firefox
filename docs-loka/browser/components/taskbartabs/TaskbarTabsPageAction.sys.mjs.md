# browser/components/taskbartabs/TaskbarTabsPageAction.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsPageAction.sys.mjs
source-hash: f16f1375296d2011bdea868b7b00c7d48630b33c
lines: 177

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## init()
- 位置: L38-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["win", "linux"].includes()`, `aWindow.document.getElementById()`, `initVisibilityChanges()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.TaskbarTabsUtils.isTaskbarTabWindow()`, `lazy.logConsole.info()`, `taskbarTabsButton.addEventListener()`
- 条件付き依存: `if (isPopupWindow || isPrivate || !isSupportedPlatform)` → `lazy.logConsole.info()`
- 条件付き依存: `if (lazy.TaskbarTabsUtils.isTaskbarTabWindow(aWindow))` → `taskbarTabsButton.setAttribute()`
- 参照: `AppConstants.platform`, `aWindow.toolbar.visible`

## handleEvent()
- 位置: async L71-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TaskbarTabsUtils.isTaskbarTabWindow()`, `lazy.logConsole.debug()`, `this._processingTabs.add()`, `this._processingTabs.delete()`, `this._processingTabs.has()`
- 条件付き依存: `if (this._processingTabs.has(currentTab))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!isTaskbarTabWindow)` → `lazy.logConsole.info()`
- 条件付き依存: `if (!isTaskbarTabWindow)` → `lazy.TaskbarTabs.moveTabIntoTaskbarTab()`
- 条件付き依存: `if (!(!isTaskbarTabWindow))` → `lazy.logConsole.info()`
- 条件付き依存: `if (!(!isTaskbarTabWindow))` → `lazy.TaskbarTabsUtils.getTaskbarTabIdFromWindow()`
- 条件付き依存: `if (!(!isTaskbarTabWindow))` → `lazy.TaskbarTabs.ejectWindow()`
- 条件付き依存: `if (!(!isTaskbarTabWindow))` → `lazy.TaskbarTabs.getCountForId()`
- 条件付き依存: `if (!(await lazy.TaskbarTabs.getCountForId(id)))` → `lazy.logConsole.info()`
- 条件付き依存: `if (!(await lazy.TaskbarTabs.getCountForId(id)))` → `lazy.TaskbarTabs.removeTaskbarTab()`
- 参照: `aEvent.button`, `aEvent.target.documentGlobal`, `window.gBrowser.selectedTab`

## initVisibilityChanges()
- 位置: L124-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `aWindow.addEventListener()`, `aWindow.gBrowser.addProgressListener()`, `observer()`
- XPCOM: `Services.prefs`

## shouldShow()
- 位置: L128-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http", "https", "moz-extension"].includes()`, `lazy.TaskbarTabs.waitUntilReady()`
- 参照: `AppConstants.platform`, `Ci.nsIURL`, `aLocation.scheme`, `lazy.ShellService.desktopEntryApi`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md)

## onLocationChange()
- 位置: L158-162
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `shouldShow()`
- 参照: `aElement.hidden`, `aWebProgress.isTopLevel`

## observer()
- 位置: L165-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TaskbarTabsUtils.isEnabled()`, `shouldShow()`
- 参照: `aElement.hidden`, `aWindow.gBrowser.currentURI`
