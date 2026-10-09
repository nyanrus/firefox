# browser/components/extensions/parent/ext-windows.js

source: browser/components/extensions/parent/ext-windows.js
source-hash: 8dbd38ea54b734e9f9603d9bbeedf8e566b7feaa
lines: 582

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `fire.async()`, `this.extension.windowManager.convert()`, `this.windowEventRegistrar()`, `windowTracker.getId()`

## sanitizePositionParams()
- 位置: L16-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/gfx/screenmanager;1"].getService()`, `Math.max()`, `Math.min()`, `Math.round()`, `screen.GetAvailRectDisplayPix()`, `screenManager.screenForRect()`
- 参照: `Ci.nsIScreenManager`, `availHeight.value`, `availLeft.value`, `availTop.value`, `availWidth.value`, `params.height`, `params.left`, `params.top`, `params.width`, `window.desktopToDeviceScale`, `window.devicePixelRatio`, `window.outerHeight`, `window.outerWidth`, `window.screenX`, `window.screenY`, `window?.screenEdgeSlopX`, `window?.screenEdgeSlopY`
- XPCOM: `nsIScreenManager` / `@mozilla.org/gfx/screenmanager;1`

## windowEventRegistrar()
- 位置: L81-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## listener2()
- 位置: L84-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.canAccessWindow()`
- 条件付き依存: `if (extension.canAccessWindow(window))` → `listener()`

## unregister()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)

## onFocusChanged()
- 位置: L109-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## listener()
- 位置: L114-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Promise.resolve().then()`, `extension.canAccessWindow()`
- 条件付き依存: `if (window.document.readyState !== "complete")` → `window.addEventListener()`
- 条件付き依存: `if (window && extension.canAccessWindow(window))` → `windowTracker.isBrowserWindow()`
- 条件付き依存: `if (windowTracker.isBrowserWindow(window))` → `windowTracker.getId()`
- 条件付き依存: `if (windowId !== lastOnFocusChangedWindowId)` → `fire.async()`
- 参照: `Services.focus.activeWindow`, `Window.WINDOW_ID_NONE`, `window.document.readyState`
- XPCOM: `Services.focus`

## unregister()
- 位置: L140-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L151-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "windows", event: "onCreated", extensionApi: this, }).api()`, `new EventManager({ context, module: "windows", event: "onFocusChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "windows", event: "onRemoved", extensionApi: this, }).api()`

## get()
- 位置: L179-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `context.canAccessWindow()`, `windowManager.convert()`, `windowTracker.getWindow()`
- 条件付き依存: `if (!window || !context.canAccessWindow(window))` → `Promise.reject()`

## getCurrent()
- 位置: L189-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `context.canAccessWindow()`, `windowManager.convert()`
- 条件付き依存: `if (!context.canAccessWindow(window))` → `Promise.reject()`
- 参照: `context.currentWindow`, `windowTracker.topWindow`

## getLastFocused()
- 位置: L197-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `context.canAccessWindow()`, `windowManager.convert()`
- 条件付き依存: `if (!context.canAccessWindow(window))` → `Promise.reject()`
- 参照: `windowTracker.topWindow`

## getAll()
- 位置: L205-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getInfo.windowTypes.includes()`, `windowManager.getAll()`
- 条件付き依存: `if (doNotCheckTypes || getInfo.windowTypes.includes(win.type))` → `windows.push()`
- 条件付き依存: `if (doNotCheckTypes || getInfo.windowTypes.includes(win.type))` → `win.convert()`
- 参照: `getInfo.windowTypes`, `win.type`

## create()
- 位置: async L218-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.ww.openWindow()`, `[ "minimized", "fullscreen", "docked", "normal", "maximized", ].includes()`, `args.appendElement()`, `features.join()`, `promiseObserved()`, `resolve()`, `sanitizePositionParams()`, `win.convert()`, `window.addEventListener()`, `windowManager.getWrapper()`, `windowTracker.getTopNormalWindow()`
- 条件付き依存: `if (createData.tabId !== null)` → `tabTracker.getTab()`
- 条件付き依存: `if (createData.tabId !== null)` → `context.canAccessWindow()`
- 条件付き依存: `if (createData.tabId !== null)` → `PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (createData.tabId !== null)` → `getCookieStoreIdForTab()`
- 条件付き依存: `if (createData.tabId !== null)` → `args.appendElement()`
- 条件付き依存: `if (createData.url !== null)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `createData.url.map()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `context.uri.resolve()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `context.checkLoadURL()`
- 条件付き依存: `if (!context.checkLoadURL(url, { dontReportErrors: true }))` → `Promise.reject()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `array.appendElement()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `mkstr()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `args.appendElement()`
- 条件付き依存: `if (Array.isArray(createData.url))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (!(Array.isArray(createData.url)))` → `context.uri.resolve()`
- 条件付き依存: `if (!(Array.isArray(createData.url)))` → `args.appendElement()`
- 条件付き依存: `if (!(Array.isArray(createData.url)))` → `mkstr()`
- 条件付き依存: `if (!(Array.isArray(createData.url)))` → `ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (!(Array.isArray(createData.url)))` → `context.checkLoadURL()`
- 条件付き依存: `if (isOnlyMozExtensionUrl)` → `setContentTriggeringPrincipal()`
- 条件付き依存: `if (!(createData.url !== null))` → `HomePage.get().split()`
- 条件付き依存: `if (!(createData.url !== null))` → `HomePage.get()`
- 条件付き依存: `if (!(createData.url !== null))` → `args.appendElement()`
- 条件付き依存: `if (!(createData.url !== null))` → `mkstr()`
- 条件付き依存: `if (!(createData.url !== null))` → `ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (!(createData.url !== null))` → `context.checkLoadURL()`
- 条件付き依存: `if (!context.checkLoadURL(url, { dontReportErrors: true }))` → `setContentTriggeringPrincipal()`
- 条件付き依存: `if (isPopup)` → `Cc[ "@mozilla.org/hash-property-bag;1" ].createInstance()`
- 条件付き依存: `if (isPopup)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (createData.cookieStoreId)` → `Cc[ "@mozilla.org/supports-PRUint32;1" ].createInstance()`
- 条件付き依存: `if (createData.cookieStoreId)` → `getUserContextIdForCookieStoreId()`
- 条件付き依存: `if (createData.cookieStoreId)` → `args.appendElement()`
- 条件付き依存: `if (!(createData.cookieStoreId))` → `args.appendElement()`
- 条件付き依存: `if (!isPopup)` → `features.push()`
- 条件付き依存: `if (!(!isPopup))` → `features.push()`
- 条件付き依存: `if (createData.left === null && createData.top === null)` → `features.push()`
- 条件付き依存: `if (createData.incognito)` → `features.push()`
- 条件付き依存: `if (!(createData.incognito))` → `features.push()`
- 条件付き依存: `if (createData.width !== null)` → `features.push()`
- 条件付き依存: `if (createData.height !== null)` → `features.push()`
- 条件付き依存: `if (createData.left !== null)` → `features.push()`
- 条件付き依存: `if (createData.top !== null)` → `features.push()`
- 条件付き依存: `if ( [ "minimized", "fullscreen", "docked", "normal", "maximized", ].includes(createData.state) )` → `win.setState()`
- 条件付き依存: `if (createData.titlePreface !== null)` → `win.setTitlePreface()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsISupportsPRBool`, `Ci.nsISupportsPRUint32`, `Ci.nsIWritablePropertyBag2`, `PrivateBrowsingUtils.enabled`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `context.principal`, `context.privateBrowsingAllowed`, `createData.allowScriptsToClose`, `createData.cookieStoreId`, `createData.height`, `createData.incognito`, `createData.left`, `createData.state`, `createData.tabId`, `createData.titlePreface`, `createData.top`, `createData.type`, `createData.url`, `createData.width`, `tab.documentGlobal`, `tab.linkedBrowser`, `tab.splitview`, `userContextIdSupports.data`, `window.gBrowserAllowScriptsToCloseInitialTabs`
- XPCOM: [`nsIMutableArray`](../../../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsPRBool`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsPRUint32`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-PRBool;1` / `@mozilla.org/supports-PRUint32;1` / `Services.scriptSecurityManager` / `Services.ww`

## mkstr()
- 位置: L239-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 参照: `Ci.nsISupportsString`, `result.data`
- XPCOM: [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`

## setContentTriggeringPrincipal()
- 位置: L259-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `createData.incognito`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## update()
- 位置: async L517-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sanitizePositionParams()`, `win.convert()`, `win.updateGeometry()`, `windowManager.get()`
- 条件付き依存: `if (updateInfo.focused)` → `win.window.focus()`
- 条件付き依存: `if (updateInfo.state !== null)` → `win.setState()`
- 条件付き依存: `if (updateInfo.drawAttention)` → `win.window.getAttention()`
- 条件付き依存: `if (updateInfo.titlePreface !== null)` → `win.setTitlePreface()`
- 条件付き依存: `if (updateInfo.titlePreface !== null)` → `win.window.gBrowser.updateTitlebar()`
- 参照: `updateInfo.drawAttention`, `updateInfo.focused`, `updateInfo.height`, `updateInfo.left`, `updateInfo.state`, `updateInfo.titlePreface`, `updateInfo.top`, `updateInfo.width`, `win.window`

## remove()
- 位置: L561-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`, `window.close()`, `windowTracker.addListener()`, `windowTracker.getWindow()`
- 条件付き依存: `if (!context.canAccessWindow(window))` → `Promise.reject()`

## listener()
- 位置: L571-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `windowTracker.removeListener()`
