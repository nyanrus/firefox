# browser/base/content/utilityOverlay.js

source: browser/base/content/utilityOverlay.js
source-hash: 3b8782f6fc3a2ad1b40aa17af34db482b998691b
lines: 605

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Components.Constructor()`, `Object.defineProperty()`

## get()
- 位置: L42-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.isAIWindowActive()`, `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `ExtensionUtils.isExtensionUrl()`
- 参照: `AIWindow.newTabURL`, `AboutNewTab.newTabURL`, `AboutNewTab.newTabURLOverridden`, `PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.prefs`

## isBlankPageURL()
- 位置: L84-91
- 役割: (未記入)
- 触るとき: (未記入)

## doGetProtocolFlags()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.getDynamicProtocolFlags()`
- XPCOM: `Services.io`

## openUILink()
- 位置: L97-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URILoadingHelper.openUILink()`

## openTrustedLinkIn()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URILoadingHelper.openTrustedLinkIn()`

## openWebLinkIn()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URILoadingHelper.openWebLinkIn()`

## openLinkIn()
- 位置: L126-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URILoadingHelper.openLinkIn()`

## checkForMiddleClick()
- 位置: L133-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.hasAttribute()`
- 条件付き依存: `if (event.button == 1)` → `document.createEvent()`
- 条件付き依存: `if (event.button == 1)` → `cmdEvent.initCommandEvent()`
- 条件付き依存: `if (event.button == 1)` → `node.dispatchEvent()`
- 条件付き依存: `if (event.button == 1)` → `event.stopPropagation()`
- 条件付き依存: `if (event.button == 1)` → `event.preventDefault()`
- 条件付き依存: `if (event.button == 1)` → `closeMenus()`
- 参照: `event.altKey`, `event.button`, `event.ctrlKey`, `event.inputSource`, `event.metaKey`, `event.shiftKey`, `event.target`, `event.target.tagName`

## createUserContextMenu()
- 位置: L181-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContextualIdentityService.getPublicIdentities()`, `ContextualIdentityService.getPublicIdentities().forEach()`, `ContextualIdentityService.getUserContextLabel()`, `MozXULElement.insertFTLIfNeeded()`, `createMenuItem()`, `docfrag.appendChild()`, `document.createDocumentFragment()`, `document.createElement()`, `document.createXULElement()`, `menuitem.setAttribute()`, `target.appendChild()`, `target.firstChild.remove()`, `target.hasChildNodes()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `createMenuItem()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `menuitem.setAttribute()`
- 条件付き依存: `if (!isContextMenu)` → `menuitem.setAttribute()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `docfrag.appendChild()`
- 条件付き依存: `if (excludeUserContextId || showDefaultTab)` → `createSeparator()`
- 条件付き依存: `if (isPanelList)` → `ContextualIdentityService.getContainerIconURL()`
- 条件付き依存: `if (isPanelList)` → `menuitem.style.setProperty()`
- 条件付き依存: `if (isPanelList)` → `ContextualIdentityService.getContainerColorCode()`
- 条件付き依存: `if (!(isPanelList))` → `menuitem.classList.add()`
- 条件付き依存: `if (showAddContainer || showManageContainers)` → `docfrag.appendChild()`
- 条件付き依存: `if (showAddContainer || showManageContainers)` → `createSeparator()`
- 条件付き依存: `if (showAddContainer)` → `createMenuItem()`
- 条件付き依存: `if (showAddContainer)` → `onActivate()`
- 条件付き依存: `if (showAddContainer)` → `ContainerCreationPanel.open()`
- 条件付き依存: `if (showAddContainer)` → `docfrag.appendChild()`
- 条件付き依存: `if (showManageContainers)` → `createMenuItem()`
- 条件付き依存: `if (showManageContainers)` → `onActivate()`
- 条件付き依存: `if (showManageContainers)` → `openPreferences()`
- 条件付き依存: `if (showManageContainers)` → `docfrag.appendChild()`
- 参照: `event.target`, `identity.color`, `identity.icon`, `identity.userContextId`

## onActivate()
- 位置: L204-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `item.addEventListener()`
- 条件付き依存: `if (!isPanelList)` → `activateEvent.stopPropagation()`

## panelListReplacements()
- 位置: L220-221
- 役割: (未記入)
- 触るとき: (未記入)

## createMenuItem()
- 位置: L223-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.createXULElement()`
- 条件付き依存: `if (name)` → `setLabel()`
- 条件付き依存: `if (!(name))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(name))` → `panelListReplacements()`

## setLabel()
- 位置: L227-233
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(isPanelList))` → `item.setAttribute()`
- 参照: `item.textContent`

## closeMenus()
- 位置: L321-333
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( node.namespaceURI == "http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul" && (node.tagName == "menupopup" || node.tagName == "popup") )` → `node.hidePopup()`
- 条件付き依存: `if ("tagName" in node)` → `closeMenus()`
- 参照: `node.namespaceURI`, `node.parentNode`, `node.tagName`

## eventMatchesKey()
- 位置: L346-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aKey.getAttribute("key") || "").toLowerCase()`, `aEvent.getModifierState()`, `aKey.getAttribute()`, `modifiers.filter()`
- 条件付き依存: `if (keyModifiers)` → `keyModifiers.split()`
- 条件付き依存: `if (keyModifiers)` → `keyModifiers.forEach()`
- 条件付き依存: `if (!(modifier == "accel"))` → `modifier[0].toUpperCase()`
- 条件付き依存: `if (!(modifier == "accel"))` → `modifier.slice()`
- 条件付き依存: `if (keyModifiers)` → `modifiers.every()`
- 条件付き依存: `if (keyModifiers)` → `keyModifiers.includes()`
- 条件付き依存: `if (keyModifiers)` → `aEvent.getModifierState()`
- 参照: `AppConstants.platform`, `aEvent.key`, `eventModifiers.length`, `keyModifiers.length`

## gatherTextUnder()
- 位置: L384-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.createDocumentEncoder()`, `encoder.encodeToString()`, `encoder.encodeToString().trim()`, `encoder.init()`, `encoder.setContainerNode()`
- 参照: `root.ownerDocument`

## getShellService()
- 位置: L392-394
- 役割: (未記入)
- 触るとき: (未記入)

## isBidiEnabled()
- 位置: L396-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (isRTL)` → `Services.prefs.setBoolPref()`
- 参照: `Services.locale.isAppLocaleRTL`
- XPCOM: `Services.locale` / `Services.prefs`

## openAboutDialog()
- 位置: L411-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `Services.wm.getEnumerator()`, `win.focus()`, `win.openDialog()`
- 参照: `AppConstants.platform`, `win.closed`
- XPCOM: `Services.wm`

## openReferralsPage()
- 位置: L434-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Referrals.openReferralsTab()`

## openPreferences()
- 位置: async L438-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `internalPrefCategoryNameToFriendlyName()`
- 条件付き依存: `if (urlParams[name] !== undefined)` → `params.set()`
- 条件付き依存: `if (!win)` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (!win)` → `Cc[ "@mozilla.org/supports-string;1" ].createInstance()`
- 条件付き依存: `if (!win)` → `windowArguments.appendElement()`
- 条件付き依存: `if (!win)` → `Services.ww.openWindow()`
- 条件付き依存: `if (!(!win))` → `win.switchToTabHavingURI()`
- 条件付き依存: `if (!(!win))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (newLoad)` → `win.switchToTabHavingURI()`
- 条件付き依存: `if (newLoad)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (browser.contentDocument?.readyState != "complete")` → `browser.addEventListener()`
- 条件付き依存: `if (!newLoad && paneID)` → `browser.contentWindow.gotoPref()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsISupportsString`, `browser.contentDocument?.readyState`, `extraArgs.urlParams`, `supportsStringPrefURL.data`, `win.gBrowser.selectedBrowser`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/supports-string;1` / `Services.scriptSecurityManager` / `Services.wm` / `Services.ww`

## internalPrefCategoryNameToFriendlyName()
- 位置: L440-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aName || "").replace()`, `toReplace[4].toLowerCase()`

## openTroubleshootingPage()
- 位置: L526-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openTrustedLinkIn()`

## openFeedbackPage()
- 位置: L533-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `openTrustedLinkIn()`
- XPCOM: `Services.urlFormatter`

## openSwitchingDevicesPage()
- 位置: L541-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getHelpLinkURL()`, `openTrustedLinkIn()`, `parsedUrl.searchParams.set()`
- 参照: `parsedUrl.href`

## buildHelpMenu()
- 位置: L551-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getSupportMenu()`, `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (supportMenu)` → `document.getElementById()`
- 条件付き依存: `if (supportMenu)` → `menuitem.setAttribute()`
- 条件付き依存: `if ("AccessKey" in supportMenu)` → `menuitem.setAttribute()`
- 条件付き依存: `if (typeof gSafeBrowsing != "undefined")` → `gSafeBrowsing.setReportPhishingMenu()`
- 参照: `document.getElementById("feedbackPage").disabled`, `document.getElementById("helpPolicySeparator").hidden`, `document.getElementById("helpSafeMode").disabled`, `document.getElementById("menu_referralsPage").hidden`, `document.getElementById("troubleShooting").disabled`, `menuitem.hidden`, `supportMenu.AccessKey`, `supportMenu.Title`
- XPCOM: `Services.policies` / `Services.prefs`

## isElementVisible()
- 位置: L581-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElement.getBoundingClientRect()`
- 参照: `rect.height`, `rect.width`

## makeURLAbsolute()
- 位置: L592-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeURI()`
- 参照: `makeURI(aUrl, null, makeURI(aBase)).spec`

## getHelpLinkURL()
- 位置: L597-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## openHelpLink()
- 位置: L602-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getHelpLinkURL()`, `openTrustedLinkIn()`
