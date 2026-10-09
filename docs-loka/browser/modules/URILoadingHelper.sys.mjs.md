# browser/modules/URILoadingHelper.sys.mjs

source: browser/modules/URILoadingHelper.sys.mjs
source-hash: 6f88bf621d9c423954d59deb2798fb37303dd04e
lines: 1134

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`

## saveLink()
- 位置: L26-61
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("isContentWindowPrivate" in params)` → `window.saveURL()`
- 条件付き依存: `if (!params.initiatingDoc)` → `console.error()`
- 条件付き依存: `if (!("isContentWindowPrivate" in params))` → `window.saveURL()`
- 参照: `params.initiatingDoc`, `params.isContentWindowPrivate`, `params.originPrincipal`, `params.referrerInfo`

## openInWindow()
- 位置: L63-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/supports-PRBool;1" ].createInstance()`, `Cc[ "@mozilla.org/supports-PRUint32;1" ].createInstance()`, `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`, `Cc["@mozilla.org/supports-string;1"].createInstance()`, `Services.ww.openWindow()`, `sa.appendElement()`
- 条件付き依存: `if (triggeringRemoteType)` → `extraOptions.setPropertyAsACString()`
- 条件付き依存: `if (params.hasValidUserGestureActivation !== undefined)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.textDirectiveUserActivation !== undefined)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (forceAllowDataURI)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.fromExternal !== undefined)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `extraOptions.setPropertyAsACString()`
- 条件付き依存: `if (globalHistoryOptions.triggeringSponsoredURLVisitTimeMS)` → `extraOptions.setPropertyAsUint64()`
- 条件付き依存: `if (globalHistoryOptions.triggeringSource)` → `extraOptions.setPropertyAsACString()`
- 条件付き依存: `if (params.schemelessInput !== undefined)` → `extraOptions.setPropertyAsUint32()`
- 条件付き依存: `if (params.aiWindow)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (chromeless)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.aswebauth)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (params.frameID != undefined && sourceWindow)` → `waitForWindowStartup().then()`
- 条件付き依存: `if (params.frameID != undefined && sourceWindow)` → `waitForWindowStartup()`
- 条件付き依存: `if (params.frameID != undefined && sourceWindow)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (resolveOnContentBrowserCreated)` → `waitForWindowStartup().then()`
- 条件付き依存: `if (resolveOnContentBrowserCreated)` → `waitForWindowStartup()`
- 条件付き依存: `if (resolveOnContentBrowserCreated)` → `resolveOnContentBrowserCreated()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsISupportsPRBool`, `Ci.nsISupportsPRUint32`, `Ci.nsISupportsString`, `Ci.nsIWritablePropertyBag2`, `allowThirdPartyFixupSupports.data`, `globalHistoryOptions.triggeringSource`, `globalHistoryOptions.triggeringSponsoredURL`, `globalHistoryOptions.triggeringSponsoredURLVisitTimeMS`, `globalHistoryOptions?.triggeringSponsoredURL`, `lazy.ReferrerInfo`, `params.aiWindow`, `params.aswebauth`, `params.frameID`, `params.fromExternal`, `params.hasValidUserGestureActivation`, `params.private`, `params.schemelessInput`, `params.textDirectiveUserActivation`, `referrerInfo.originalReferrer`, `referrerInfo.referrerPolicy`, `sourceWindow.gBrowser.selectedBrowser`, `userContextIdSupports.data`, `win.gBrowser.selectedBrowser`, `wuri.data`
- XPCOM: [`nsIMutableArray`](../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsPRUint32`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-PRBool;1` / `@mozilla.org/supports-PRUint32;1` / `@mozilla.org/supports-string;1` / `Services.obs` / `Services.ww`

## waitForWindowStartup()
- 位置: L192-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## removeObservers()
- 位置: L194-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## delayedStartupObserver()
- 位置: L201-206
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aSubject == win)` → `removeObservers()`
- 条件付き依存: `if (aSubject == win)` → `resolve()`

## closedObserver()
- 位置: L208-212
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aSubject == win)` → `removeObservers()`

## openInCurrentTab()
- 位置: L257-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.getDynamicProtocolFlags()`, `params.resolveOnContentBrowserCreated()`, `targetBrowser.fixupAndLoadURIString()`
- 条件付き依存: `if ( params.forceAboutBlankViewerInCurrent && (!uriObj || Services.io.getDynamicProtocolFlags(uriObj) & URI_INHERITS_SECURITY_CONTEXT) )` → `targetBrowser.createAboutBlankDocumentViewer()`
- 参照: `Ci.nsIProtocolHandler`, `Ci.nsIWebNavigation.LOAD_FLAGS_ALLOW_POPUPS`, `Ci.nsIWebNavigation.LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP`, `Ci.nsIWebNavigation.LOAD_FLAGS_DISALLOW_INHERIT_PRINCIPAL`, `Ci.nsIWebNavigation.LOAD_FLAGS_ERROR_LOAD_CHANGES_RV`, `Ci.nsIWebNavigation.LOAD_FLAGS_FIXUP_SCHEME_TYPOS`, `Ci.nsIWebNavigation.LOAD_FLAGS_FORCE_ALLOW_DATA_URI`, `Ci.nsIWebNavigation.LOAD_FLAGS_FROM_EXTERNAL`, `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `params.allowInheritPrincipal`, `params.allowPopups`, `params.allowThirdPartyFixup`, `params.forceAboutBlankViewerInCurrent`, `params.forceAllowDataURI`, `params.fromExternal`, `params.indicateErrorPageLoad`, `params.originPrincipal`, `params.originStoragePrincipal`
- XPCOM: [`nsIProtocolHandler`](../../netwerk/base/nsIIOService.idl.md) / [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md) / `Services.io`

## updatePrincipals()
- 位置: L329-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `useOAForPrincipal()`
- 参照: `params.originPrincipal`, `params.originStoragePrincipal`, `params.triggeringPrincipal`

## useOAForPrincipal()
- 位置: L336-349
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (principal && principal.isContentPrincipal)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (principal && principal.isContentPrincipal)` → `Services.scriptSecurityManager.principalWithOA()`
- 参照: `params.private`, `principal.isContentPrincipal`, `principal.originAttributes.firstPartyDomain`
- XPCOM: `Services.scriptSecurityManager`

## _createNullPrincipalFromTabUserContextId()
- 位置: L359-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `lazy.BrowserWindowTracker.getTopWindow()`, `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("usercontextid"))` → `tab.getAttribute()`
- 参照: `window.gBrowser.selectedTab`
- XPCOM: `Services.scriptSecurityManager`

## openLinkIn()
- 位置: L489-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.willLoadInBackground()`, `Object.assign()`, `openInCurrentTab()`, `resolveOnContentBrowserCreated()`, `resolveOnNewTabCreated()`, `this._resolveInitialTargetWindow()`, `updatePrincipals()`, `w.focus()`, `w.gBrowser.addTab()`, `w.isBlankPageURL()`
- 条件付き依存: `if (where == "save")` → `saveLink()`
- 条件付き依存: `if (!w || where == "window")` → `openInWindow()`
- 条件付き依存: `if (where == "current")` → `URL.parse()`
- 条件付き依存: `if (where == "current")` → `w.gBrowser.getTabForBrowser()`
- 条件付き依存: `if ( !allowPinnedTabHostChange && tab.pinned && url != "about:crashcontent" )` → `uriObj.schemeIs()`
- 条件付き依存: `if (params.frameID != undefined && w)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!params.initiatedByURLBar && targetBrowser)` → `lazy.handleBounceEventTrigger()`
- 条件付き依存: `if ( !params.avoidBrowserFocus && !focusUrlBar && targetBrowser == w.gBrowser.selectedBrowser )` → `targetBrowser.focus()`
- 参照: `Ci.nsIReferrerInfo.EMPTY`, `URL.parse(url)?.URI`, `lazy.AboutNewTab.willNotifyUser`, `lazy.ReferrerInfo`, `params.avoidBrowserFocus`, `params.chromeless`, `params.eventDetail`, `params.frameID`, `params.fromExternal`, `params.initiatedByURLBar`, `params.openerBrowser`, `params.referrerInfo`, `params.relatedToCurrent`, `params.schemelessInput`, `params.targetBrowser`, `params.userContextId`, `tab.pinned`, `tabUsedForLoad.linkedBrowser`, `targetBrowser.browsingContext.originAttributes.userContextId`, `targetBrowser.currentURI.host`, `uriObj.host`, `w.FirefoxViewHandler.tab`, `w.document.activeElement`, `w.gBrowser.selectedBrowser`, `w.gURLBar.inputField`
- XPCOM: [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / `Services.obs`

## _resolveInitialTargetWindow()
- 位置: L710-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTargetWindow()`
- 条件付き依存: `if (where === "tab" || where === "tabshifted")` → `this.getTargetWindow()`
- 参照: `params.relatedToCurrent`, `params.targetBrowser`, `params.targetBrowser.documentGlobal`, `win.top`

## getTargetWindow()
- 位置: L741-766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `lazy.BrowserWindowTracker.getTopWindow()`, `top.document.documentElement.getAttribute()`, `top.document.documentElement.hasAttribute()`
- 参照: `top.toolbar.visible`

## openUILink()
- 位置: L793-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getRootEvent()`, `BrowserUtils.whereToOpenLink()`, `this.openLinkIn()`
- 参照: `event.target.ownerDocument`, `params.forceForeground`, `params.ignoreAlt`, `params.ignoreButton`, `params.triggeringPrincipal`

## openTrustedLinkIn()
- 位置: L848-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openLinkIn()`
- 条件付き依存: `if (!params.triggeringPrincipal)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `params.forceForeground`, `params.triggeringPrincipal`
- XPCOM: `Services.scriptSecurityManager`

## openWebLinkIn()
- 位置: L873-885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openLinkIn()`
- 条件付き依存: `if (!params.triggeringPrincipal)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 参照: `params.forceForeground`, `params.triggeringPrincipal`, `params.triggeringPrincipal.isSystemPrincipal`
- XPCOM: `Services.scriptSecurityManager`

## guessUserContextId()
- 位置: L897-928
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currentURIHost == host)` → `containerScores.get()`
- 条件付き依存: `if (currentURIHost == host)` → `containerScores.set()`
- 参照: `aURI.host`, `lazy.BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser.currentURI.host`, `win.gBrowser.visibleTabs`

## switchToTabHavingURI()
- 位置: L965-1132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `switchIfURIInWindow()`
- 条件付き依存: `if (!(aURI instanceof Ci.nsIURI))` → `Services.io.newURI()`
- 条件付き依存: `if (isBrowserWindow && window.gBrowser.selectedTab.isEmpty)` → `this.openTrustedLinkIn()`
- 条件付き依存: `if (!(isBrowserWindow && window.gBrowser.selectedTab.isEmpty))` → `this.openTrustedLinkIn()`
- 参照: `Ci.nsIURI`, `aOpenParams.adoptIntoActiveWindow`, `aOpenParams.ignoreFragment`, `aOpenParams.ignoreQueryString`, `aOpenParams.replaceQueryString`, `aOpenParams.userContextId`, `aURI.spec`, `browserWin.closed`, `lazy.BrowserWindowTracker.orderedWindows`, `window.gBrowser`, `window.gBrowser.selectedTab.isEmpty`
- XPCOM: [`nsIURI`](../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## switchIfURIInWindow()
- 位置: L992-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `browser.getAttribute()`, `cleanURL()`, `ignoreFragment.startsWith()`, `kPrivateBrowsingURLs.has()`
- 条件付き依存: `if (doAdopt)` → `window.gBrowser.adoptTab()`
- 条件付き依存: `if (doAdopt)` → `aWindow.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!doAdopt)` → `aWindow.focus()`
- 条件付き依存: `if ( ignoreFragment == "whenComparingAndReplace" || replaceQueryString )` → `browser.loadURI()`
- 条件付き依存: `if ( ignoreFragment == "whenComparingAndReplace" || replaceQueryString )` → `_createNullPrincipalFromTabUserContextId()`
- 条件付き依存: `if (aSplitView)` → `aSplitView.tabs.includes()`
- 条件付き依存: `if (!(aSplitView.tabs.includes(tabToMove)))` → `aSplitView.tabs.find()`
- 条件付き依存: `if (!(aSplitView.tabs.includes(tabToMove)))` → `aSplitView.replaceTab()`
- 条件付き依存: `if (aSplitView)` → `aSplitView.documentGlobal.focus()`
- 参照: `aOpenParams.triggeringPrincipal`, `aURI.displaySpec`, `aURI.spec`, `aWindow.gBrowser.browsers`, `aWindow.gBrowser.selectedTab`, `aWindow.gBrowser.tabContainer.selectedIndex`, `aWindow.gBrowser.tabs`, `browser.currentURI.displaySpec`, `browsers.length`, `tab.selected`, `window.gBrowser.tabContainer.selectedIndex`

## cleanURL()
- 位置: L1004-1020
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (removeFragment)` → `ret.split()`
- 条件付き依存: `if (removeQuery)` → `ret.split()`
- 条件付き依存: `if (removeQuery)` → `ret .split("?")[0] .concat()`
- 条件付き依存: `if (removeQuery)` → `ret .split()`
- 条件付き依存: `if (removeQuery)` → `"#".concat()`
