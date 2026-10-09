# browser/components/extensions/parent/ext-sessions.js

source: browser/components/extensions/parent/ext-sessions.js
source-hash: 408fa09b5ba55612f09f70324115e2825781a077
lines: 301

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getRecentlyClosed()
- 位置: L17-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getClosedTabDataForWindow()`, `SessionStore.getClosedWindowData()`, `Tab.convertFromSessionStoreClosedData()`, `Window.convertFromSessionStoreClosedData()`, `extension.canAccessWindow()`, `recentlyClosed.push()`, `recentlyClosed.slice()`, `recentlyClosed.sort()`, `windowTracker.browserWindows()`
- 参照: `a.lastModified`, `b.lastModified`, `tab.closedAt`, `window.closedAt`

## createSession()
- 位置: async L51-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `extension.tabManager.convert()`
- 条件付き依存: `if (restored.isChromeWindow)` → `promiseObserved()`
- 条件付き依存: `if (restored.isChromeWindow)` → `extension.windowManager.convert()`
- 参照: `restored.isChromeWindow`, `sessionObj.tab`, `sessionObj.window`

## getEncodedKey()
- 位置: L76-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManagerPrivate.isTemporaryInstallID()`

## onChanged()
- 位置: L90-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## observer()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## unregister()
- 位置: L97-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## convert()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L107-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "sessions", event: "onChanged", extensionApi: this, }).api()`

## getTabParams()
- 位置: L110-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`, `getEncodedKey()`, `tabTracker.getTab()`
- 参照: `extension.id`, `tab.documentGlobal`

## getWindowParams()
- 位置: L119-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getEncodedKey()`, `windowTracker.getWindow()`
- 参照: `extension.id`

## getClosedIdFromSessionId()
- 位置: L125-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `parseInt()`

## getRecentlyClosed()
- 位置: async L137-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getRecentlyClosed()`
- 参照: `SessionStore.promiseInitialized`, `filter.maxResults`

## forgetClosedTab()
- 位置: async L144-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.forgetClosedTabById()`, `SessionStore.getClosedTabDataForWindow()`, `closedTabData.some()`, `getClosedIdFromSessionId()`, `windowTracker.getWindow()`
- 参照: `SessionStore.promiseInitialized`, `closedTab.closedId`

## forgetClosedWindow()
- 位置: async L161-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.forgetClosedWindow()`, `SessionStore.getClosedWindowData()`, `closedWindowData.findIndex()`, `getClosedIdFromSessionId()`
- 参照: `SessionStore.promiseInitialized`, `closedWindow.closedId`

## restore()
- 位置: async L178-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createSession()`
- 条件付き依存: `if (sessionId)` → `getClosedIdFromSessionId()`
- 条件付き依存: `if (closedId !== undefined)` → `SessionStore.getObjectTypeForClosedId()`
- 条件付き依存: `if (SessionStore.getObjectTypeForClosedId(closedId) == "tab")` → `SessionStore.getWindowForTabClosedId()`
- 条件付き依存: `if (closedId !== undefined)` → `SessionStore.undoCloseById()`
- 条件付き依存: `if (SessionStore.lastClosedObjectType == "window")` → `SessionStore.undoCloseWindow()`
- 条件付き依存: `if (!(SessionStore.lastClosedObjectType == "window"))` → `windowTracker.browserWindows()`
- 条件付き依存: `if (!(SessionStore.lastClosedObjectType == "window"))` → `SessionStore.getClosedTabDataForWindow()`
- 条件付き依存: `if (!(SessionStore.lastClosedObjectType == "window"))` → `recentlyClosedTabs.push()`
- 条件付き依存: `if (recentlyClosedTabs.length)` → `recentlyClosedTabs.sort()`
- 条件付き依存: `if (recentlyClosedTabs.length)` → `SessionStore.getWindowForTabClosedId()`
- 条件付き依存: `if (recentlyClosedTabs.length)` → `SessionStore.undoCloseById()`
- 参照: `SessionStore.lastClosedObjectType`, `SessionStore.promiseInitialized`, `a.closedAt`, `b.closedAt`, `extension.privateBrowsingAllowed`, `recentlyClosedTabs.length`, `recentlyClosedTabs[0].closedId`

## setTabValue()
- 位置: L237-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `SessionStore.setCustomTabValue()`, `getTabParams()`

## getTabValue()
- 位置: async L247-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getCustomTabValue()`, `getTabParams()`
- 条件付き依存: `if (value)` → `JSON.parse()`

## removeTabValue()
- 位置: L258-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.deleteCustomTabValue()`, `getTabParams()`

## setWindowValue()
- 位置: L264-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `SessionStore.setCustomWindowValue()`, `getWindowParams()`

## getWindowValue()
- 位置: async L274-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getCustomWindowValue()`, `getWindowParams()`
- 条件付き依存: `if (value)` → `JSON.parse()`

## removeWindowValue()
- 位置: L285-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.deleteCustomWindowValue()`, `getWindowParams()`
