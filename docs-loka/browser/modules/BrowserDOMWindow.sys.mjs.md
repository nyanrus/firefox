# browser/modules/BrowserDOMWindow.sys.mjs

source: browser/modules/BrowserDOMWindow.sys.mjs
source-hash: 2cbf419680e8b2943786aeeda290c70af16e6c4a
lines: 557

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.Constructor()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## BrowserDOMWindow.constructor()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win`

## BrowserDOMWindow.setupInWindow()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `win.browserDOMWindow`

## BrowserDOMWindow.teardownInWindow()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `win.browserDOMWindow`

## BrowserDOMWindow.#openURIInNewTab()
- 位置: L88-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TaskbarTabsUtils.isTaskbarTabWindow()`, `this.win.document.documentElement.hasAttribute()`, `win.gBrowser.getBrowserForTab()`
- 条件付き依存: `if (!( this.win.toolbar.visible && !lazy.TaskbarTabsUtils.isTaskbarTabWindow(this.win) && !this.win.document.documentElement.hasAttribute("mini-window") ))` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (aIsExternal && (!aURI || aURI.spec == "about:blank"))` → `win.BrowserCommands.openTab()`
- 条件付き依存: `if (aIsExternal && (!aURI || aURI.spec == "about:blank"))` → `win.focus()`
- 条件付き依存: `if (aWhere == Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT)` → `win.gBrowser.addAdjacentTab()`
- 条件付き依存: `if (!(aWhere == Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT))` → `win.gBrowser.addTab()`
- 条件付き依存: `if (needToFocusWin || (!loadInBackground && aIsExternal))` → `win.focus()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FOREGROUND`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `aURI.spec`, `lazy.loadDivertedInBackground`, `this.win`, `this.win.toolbar.visible`, `win.gBrowser.selectedBrowser`, `win.gBrowser.selectedTab`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / `nsIScriptSecurityManager`

## BrowserDOMWindow.createContentWindow()
- 位置: L183-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getContentWindowOrOpenURI()`

## BrowserDOMWindow.openURI()
- 位置: L205-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getContentWindowOrOpenURI()`
- 条件付き依存: `if (!aURI)` → `console.error()`
- 条件付き依存: `if (!aURI)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`

## BrowserDOMWindow.#getContentWindowOrOpenURI()
- 位置: L238-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/hash-property-bag;1" ].createInstance()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `aURI.schemeIs()`, `console.error()`, `extraOptions.setPropertyAsBool()`, `lazy.URILoadingHelper.guessUserContextId()`, `this.#openURIInNewTab()`, `this.win.PrintUtils.handleStaticCloneCreatedForPrint()`, `this.win.openDialog()`
- 条件付き依存: `if (aOpenWindowInfo && isExternal)` → `console.error()`
- 条件付き依存: `if (aOpenWindowInfo && isExternal)` → `Components.Exception()`
- 条件付き依存: `if (isExternal && aURI && aURI.schemeIs("chrome"))` → `dump()`
- 条件付き依存: `if (isExternal)` → `lazy.NimbusFeatures.externalLinkHandling.recordExposureEvent()`
- 条件付き依存: `if (aWhere == Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW)` → `lazy.NimbusFeatures.externalLinkHandling.getVariable()`
- 条件付き依存: `if (!(isExternal && externalLinkOpeningBehavior != -1))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( aOpenWindowInfo && aOpenWindowInfo.parent && aOpenWindowInfo.parent.window )` → `Services.io.newURI()`
- 条件付き依存: `if (forceAllowDataURI)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (aURI)` → `this.win.gBrowser.fixupAndLoadURIString()`
- 条件付き依存: `if (!lazy.loadDivertedInBackground)` → `this.win.focus()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW`, `Ci.nsIBrowserDOMWindow.OPEN_EXTERNAL`, `Ci.nsIBrowserDOMWindow.OPEN_FORCE_ALLOW_DATA_URI`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FOREGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWWINDOW`, `Ci.nsIBrowserDOMWindow.OPEN_NO_REFERRER`, `Ci.nsIBrowserDOMWindow.OPEN_PRINT_BROWSER`, `Ci.nsIReferrerInfo.EMPTY`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `Ci.nsIWebNavigation.LOAD_FLAGS_FIRST_LOAD`, `Ci.nsIWebNavigation.LOAD_FLAGS_FORCE_ALLOW_DATA_URI`, `Ci.nsIWebNavigation.LOAD_FLAGS_FROM_EXTERNAL`, `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `Ci.nsIWritablePropertyBag2`, `Cr.NS_ERROR_FAILURE`, `aOpenWindowInfo.isRemote`, `aOpenWindowInfo.originAttributes.privateBrowsingId`, `aOpenWindowInfo.originAttributes.userContextId`, `aOpenWindowInfo.parent`, `aOpenWindowInfo.parent.window`, `aOpenWindowInfo.parent.window.document.referrerInfo.referrerPolicy`, `aOpenWindowInfo.parent.window.location.href`, `aOpenWindowInfo?.parent?.top.embedderElement`, `aTriggeringPrincipal.isSystemPrincipal`, `aURI.spec`, `browser.browsingContext`, `lazy.ReferrerInfo`, `lazy.loadDivertedInBackground`, `this.win`, `this.win.gBrowser.selectedBrowser.browsingContext`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / `nsIScriptSecurityManager` / [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md) / [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/hash-property-bag;1` / `Services.io` / `Services.prefs`

## BrowserDOMWindow.createContentWindowInFrame()
- 位置: L450-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getContentWindowOrOpenURIInFrame()`

## BrowserDOMWindow.openURIInFrame()
- 位置: L467-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getContentWindowOrOpenURIInFrame()`

## BrowserDOMWindow.#getContentWindowOrOpenURIInFrame()
- 位置: L487-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#openURIInNewTab()`
- 条件付き依存: `if (aWhere == Ci.nsIBrowserDOMWindow.OPEN_PRINT_BROWSER)` → `this.win.PrintUtils.handleStaticCloneCreatedForPrint()`
- 条件付き依存: `if ( aWhere != Ci.nsIBrowserDOMWindow.OPEN_NEWTAB && aWhere != Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND && aWhere != Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FORE...)` → `dump()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_EXTERNAL`, `Ci.nsIBrowserDOMWindow.OPEN_FORCE_ALLOW_DATA_URI`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_BACKGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_FOREGROUND`, `Ci.nsIBrowserDOMWindow.OPEN_PRINT_BROWSER`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `aParams.isPrivate`, `aParams.openWindowInfo`, `aParams.openerBrowser`, `aParams.openerOriginAttributes`, `aParams.openerOriginAttributes.userContextId`, `aParams.policyContainer`, `aParams.referrerInfo`, `aParams.triggeringPrincipal`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / `nsIScriptSecurityManager`

## BrowserDOMWindow.canClose()
- 位置: L542-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.win.CanCloseWindow()`

## BrowserDOMWindow.tabCount()
- 位置: L549-551
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.gBrowser.tabs.length`
