# browser/components/tabbrowser/Tabbrowser.sys.mjs

source: browser/components/tabbrowser/Tabbrowser.sys.mjs
source-hash: 430e1137a15f0aa8c5f39fd76127f825b2751c69
lines: 11180

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `XPCOMUtils.declareLazy()`

## tabLocalization()
- 位置: L66-74
- 役割: (未記入)
- 触るとき: (未記入)

## getTotalMemoryUsage()
- 位置: async L118-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.requestProcInfo()`

## handleDroppedLink()
- 位置: async L132-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Services.prefs.getIntPref()`, `browser.getAttribute()`, `lazy.UrlbarUtils.getShortcutOrURIAndPostData()`, `postDatas.push()`, `urls.push()`
- 条件付き依存: `if (event)` → `event.preventDefault()`
- 条件付き依存: `if (event)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( links.length >= Services.prefs.getIntPref("browser.tabs.maxOpenBeforeWarn") )` → `lazy.OpenInTabsUtils.promiseConfirmOpenInTabs()`
- 条件付き依存: `if (lastLocationChange == browser.lastLocationChange)` → `tabbrowser.loadTabs()`
- 条件付き依存: `if (lastLocationChange == browser.lastLocationChange)` → `tabbrowser.getTabForBrowser()`
- XPCOM: `Services.prefs`

## Tabbrowser.create()
- 位置: L227-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gBrowser.init()`

## Tabbrowser.destroy()
- 位置: L232-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gBrowser.destroy()`

## Tabbrowser.init()
- 位置: L236-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.getIntPref()`, `this.#setFindbarData()`, `this.#setupEventListeners()`, `this.#setupInitialBrowserAndTab()`, `this.document.addEventListener()`, `this.document.getElementById()`, `this.document.querySelector()`, `this.document.querySelector("title").removeAttribute()`, `this.documentGlobal .matchMedia()`, `this.documentGlobal .matchMedia("(prefers-color-scheme: dark)") .addEventListener()`, `this.documentGlobal.addEventListener()`, `this.tabContainer.init()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.display.document_color_use") == 2)` → `Services.prefs.getCharPref()`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#defaultDropLinkHandler()
- 位置: L282-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleDroppedLink()`, `this.getTabBrowser()`

## Tabbrowser.ownerDocument()
- 位置: L310-312
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.TabMetrics()
- 位置: L316-318
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.tabLocalization()
- 位置: L320-322
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.constructor()
- 位置: L324-327
- 役割: (未記入)
- 触るとき: (未記入)

## has()
- 位置: L499-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `parseInt()`

## get()
- 位置: L505-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `parseInt()`

## Tabbrowser.activeSplitView()
- 位置: L528-530
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.splitViewBrowsers()
- 位置: L537-545
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#activeSplitView)` → `browsers.push()`

## Tabbrowser.tabs()
- 位置: L554-556
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.tabGroups()
- 位置: L558-560
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.splitViews()
- 位置: L562-564
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.tabsInCollapsedTabGroups()
- 位置: L566-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabGroups .filter()`, `this.tabGroups .filter(tabGroup => tabGroup.collapsed) .flatMap()`, `this.tabGroups .filter(tabGroup => tabGroup.collapsed) .flatMap(tabGroup => tabGroup.tabs) .filter()`

## Tabbrowser.addEventListener()
- 位置: L573-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabpanels.addEventListener()`

## Tabbrowser.removeEventListener()
- 位置: L577-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabpanels.removeEventListener()`

## Tabbrowser.dispatchEvent()
- 位置: L581-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabpanels.dispatchEvent()`

## Tabbrowser.recordTabMetrics()
- 位置: L593-612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tab.actions[action].add()`, `Glean.tab.interaction.record()`, `Glean.tab.tabCount[action].add()`

## Tabbrowser.openTabs()
- 位置: L618-620
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.nonHiddenTabs()
- 位置: L625-627
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.visibleTabs()
- 位置: L632-634
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.pinnedTabCount()
- 位置: L636-643
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.setSelectedTab()
- 位置: L645-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.documentElement.hasAttribute()`, `this.documentGlobal.gSharedTabWarning.willShowSharedTabWarning()`, `this.recordTabMetrics()`

## Tabbrowser.selectedTab()
- 位置: L670-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setSelectedTab()`

## Tabbrowser.selectedTab()
- 位置: L674-676
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.selectedBrowser()
- 位置: L678-680
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.selectedBrowsers()
- 位置: L682-687
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#setupInitialBrowserAndTab()
- 位置: L689-875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`, `Tabbrowser.#generateUniquePanelID()`, `Tabbrowser.#tabFilters.set()`, `Tabbrowser.#tabListeners.set()`, `URILoadingWrapper.fixupAndLoadURIString.bind()`, `URILoadingWrapper.loadURI.bind()`, `browser.setAttribute()`, `browser.webProgress.addProgressListener()`, `extraOptions?.hasKey()`, `filter.addProgressListener()`, `lazy.AIWindow.isAIWindowActive()`, `tabArgument.hasAttribute()`, `this.#tabForBrowser.set()`, `this.#updateUserContextUIIndicator()`, `this.appendStatusPanel()`, `this.createBrowser()`, `this.documentGlobal.docShell.treeOwner .QueryInterface()`, `this.documentGlobal.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `this.documentGlobal.gBrowserInit.getTabToAdopt()`, `this.getPanel()`, `this.shouldActivateDocShell()`, `this.tabpanels.appendChild()`
- 条件付き依存: `if (extraOptions?.hasKey("triggeringRemoteType"))` → `extraOptions.getPropertyAsACString()`
- 条件付き依存: `if (tabArgument && tabArgument.hasAttribute("usercontextid"))` → `parseInt()`
- 条件付き依存: `if (tabArgument && tabArgument.hasAttribute("usercontextid"))` → `tabArgument.getAttribute()`
- 条件付き依存: `if (openWindowInfo.isRemote)` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (!(openWindowInfo))` → `Array.isArray()`
- 条件付き依存: `if (uriToLoad && typeof uriToLoad == "string")` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (Cu.isInAutomation)` → `ChromeUtils.releaseAssert()`
- 条件付き依存: `if (this.documentGlobal.gBrowserAllowScriptsToCloseInitialTabs)` → `browser.setAttribute()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActive(this.documentGlobal))` → `Array.isArray()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `browser.toggleAttribute()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `lazy.AIWindow.isAIWindowContentPage()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `Services.io.newURI()`
- 条件付き依存: `if (userContextId)` → `tab.setAttribute()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.setTabStyle()`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1` / `Services.io`

## Tabbrowser.#updateUserContextUIIndicator()
- 位置: L877-931
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hbox.setAttribute()`, `lazy.ContextualIdentityService.getPublicIdentityFromId()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `replaceContainerClass()`, `this.document.getElementById()`, `this.selectedBrowser.getAttribute()`
- 条件付き依存: `if (!userContextId)` → `this.document.getElementById()`
- 条件付き依存: `if (!userContextId)` → `replaceContainerClass()`
- 条件付き依存: `if (!identity)` → `replaceContainerClass()`

## replaceContainerClass()
- 位置: L878-891
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `className.startsWith()`, `element.classList.contains()`
- 条件付き依存: `if (className.startsWith(prefix))` → `element.classList.remove()`
- 条件付き依存: `if (value)` → `element.classList.add()`

## Tabbrowser.canGoBack()
- 位置: L939-941
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.canGoBackIgnoringUserInteraction()
- 位置: L947-949
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.canGoForward()
- 位置: L954-956
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.goBack()
- 位置: L965-967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.goBack()`

## Tabbrowser.goForward()
- 位置: L976-978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.goForward()`

## Tabbrowser.reload()
- 位置: L984-986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.reload()`

## Tabbrowser.reloadWithFlags()
- 位置: L988-1073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ReducedProtectionNotification.markUserReload()`, `lazy.SitePermissions.clearTemporaryBlockPermissions()`, `reloadBrowser()`, `this.documentGlobal.gIdentityHandler.hidePopup()`, `this.documentGlobal.gPermissionPanel.hidePopup()`, `this.updateBrowserRemotenessByURL()`
- 条件付き依存: `if (tab.linkedPanel)` → `loadBrowserURI()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tab.addEventListener()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `loadBrowserURI()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `this.#insertBrowser()`
- 条件付き依存: `if (!(this.updateBrowserRemotenessByURL(browser, urlSpec)))` → `unchangedRemoteness.push()`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## reloadBrowser()
- 位置: L1044-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (sessionHistory)` → `sessionHistory.reload()`
- 条件付き依存: `if (!(sessionHistory))` → `browsingContext.reload()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tab.addEventListener()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tab.linkedBrowser.browsingContext.reload()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tabbrowser.#insertBrowser()`

## loadBrowserURI()
- 位置: L1067-1072
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.loadURI()`

## Tabbrowser.stop()
- 位置: L1078-1080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.stop()`

## Tabbrowser.loadURI()
- 位置: L1088-1090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.loadURI()`

## Tabbrowser.fixupAndLoadURIString()
- 位置: L1097-1099
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.fixupAndLoadURIString()`

## Tabbrowser.gotoIndex()
- 位置: L1107-1109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedBrowser.gotoIndex()`

## Tabbrowser.currentURI()
- 位置: L1114-1116
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.finder()
- 位置: L1121-1123
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.docShell()
- 位置: L1129-1131
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.webNavigation()
- 位置: L1136-1138
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.webProgress()
- 位置: L1143-1145
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.contentWindow()
- 位置: L1151-1153
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.sessionHistory()
- 位置: L1158-1160
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.contentDocument()
- 位置: L1166-1168
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.contentTitle()
- 位置: L1173-1175
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.contentPrincipal()
- 位置: L1180-1182
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.securityUI()
- 位置: L1187-1189
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.fullZoom()
- 位置: L1194-1196
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.fullZoom()
- 位置: L1198-1200
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.textZoom()
- 位置: L1205-1207
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.textZoom()
- 位置: L1209-1211
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.isSyntheticDocument()
- 位置: L1217-1219
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.userTypedValue()
- 位置: L1226-1228
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.userTypedValue()
- 位置: L1230-1232
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#setFindbarData()
- 位置: L1234-1253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sharedData.has()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `this.document.getElementById()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `keyEl .getAttribute("modifiers") .replace()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `keyEl .getAttribute()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `sharedData.set()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `keyEl.getAttribute()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `mods.includes()`
- XPCOM: `Services.ppmm`

## Tabbrowser.isFindBarInitialized()
- 位置: L1263-1265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#findBars.has()`

## Tabbrowser.getCachedFindBar()
- 位置: L1274-1276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#findBars.get()`

## Tabbrowser.clearLastFindValue()
- 位置: L1281-1283
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.getFindBar()
- 位置: async L1292-1305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#pendingFindBars.get()`, `this.getCachedFindBar()`
- 条件付き依存: `if (!pendingFindBar)` → `this.#createFindBar()`
- 条件付き依存: `if (!pendingFindBar)` → `Tabbrowser.#pendingFindBars.set()`

## Tabbrowser.#createFindBar()
- 位置: async L1313-1335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#findBars.set()`, `Tabbrowser.#pendingFindBars.delete()`, `aTab.dispatchEvent()`, `browser.parentNode.insertAdjacentElement()`, `event.initEvent()`, `this.document.createEvent()`, `this.document.createXULElement()`, `this.documentGlobal.requestAnimationFrame()`, `this.getBrowserForTab()`

## Tabbrowser.appendStatusPanel()
- 位置: L1337-1342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.insertAdjacentElement()`

## Tabbrowser.#updateTabBarForPinnedTabs()
- 位置: L1344-1348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabContainer._handleTabSelect()`, `this.tabContainer._unlockTabSizing()`, `this.tabContainer._updateCloseButtons()`

## Tabbrowser.#notifyPinnedStatus()
- 位置: L1350-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.dispatchEvent()`, `this.recordTabMetrics()`

## Tabbrowser.pinTab()
- 位置: L1388-1405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.setAttribute()`, `this.#handleTabMove()`, `this.#notifyPinnedStatus()`, `this.#updateTabBarForPinnedTabs()`, `this.document.getElementById()`, `this.pinnedTabsContainer.insertBefore()`, `this.showTab()`

## Tabbrowser.unpinTab()
- 位置: L1417-1433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.removeAttribute()`, `this.#handleTabMove()`, `this.#notifyPinnedStatus()`, `this.#updateTabBarForPinnedTabs()`, `this.tabContainer.arrowScrollbox.prepend()`

## Tabbrowser.previewTab()
- 位置: L1435-1446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`

## Tabbrowser.getBrowserAtIndex()
- 位置: L1448-1450
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.getBrowserForOuterWindowID()
- 位置: L1452-1460
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.getTabForBrowser()
- 位置: L1462-1464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabForBrowser.get()`

## Tabbrowser.getPanel()
- 位置: L1466-1468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserContainer()`

## Tabbrowser.getBrowserContainer()
- 位置: L1470-1472
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.getTabNotificationDeck()
- 位置: L1475-1486
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#tabNotificationDeck)` → `this.document.getElementById()`
- 条件付き依存: `if (!this.#tabNotificationDeck)` → `template.replaceWith()`

## Tabbrowser.getNotificationBox()
- 位置: L1489-1503
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!browser._notificationBox)` → `element.setAttribute()`
- 条件付き依存: `if (!browser._notificationBox)` → `this.#insertNotificationBox()`

## Tabbrowser.#insertNotificationBox()
- 位置: L1517-1533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isBrowserInActiveSplitView()`, `this.getTabNotificationDeck()`, `this.getTabNotificationDeck().append()`
- 条件付き依存: `if (this.#isBrowserInActiveSplitView(browser))` → `this.getBrowserContainer()`
- 条件付き依存: `if (this.#isBrowserInActiveSplitView(browser))` → `browserContainer.prepend()`
- 条件付き依存: `if (browser == this.selectedBrowser)` → `this.#updateVisibleNotificationBox()`

## Tabbrowser.#isBrowserInActiveSplitView()
- 位置: L1535-1538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabForBrowser()`

## Tabbrowser.readNotificationBox()
- 位置: L1540-1543
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#updateVisibleNotificationBox()
- 位置: L1545-1561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationBox.stack.getAttribute()`, `this.getTabNotificationDeck()`, `this.readNotificationBox()`

## Tabbrowser.getTabDialogBox()
- 位置: L1563-1573
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.getTabFromAudioEvent()
- 位置: L1575-1583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabForBrowser()`

## Tabbrowser._callProgressListeners()
- 位置: L1585-1622
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aCallGlobalListeners && aBrowser == this.selectedBrowser)` → `callListeners()`
- 条件付き依存: `if (aCallTabsListeners)` → `aArguments.unshift()`
- 条件付き依存: `if (aCallTabsListeners)` → `callListeners()`

## callListeners()
- 位置: L1594-1607
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aMethod in p)` → `p[aMethod].apply()`
- 条件付き依存: `if (aMethod in p)` → `console.error()`

## Tabbrowser.setDefaultIcon()
- 位置: L1630-1634
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aURI && aURI.spec in FAVICON_DEFAULTS)` → `this.setIcon()`

## Tabbrowser.setIcon()
- 位置: L1636-1686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LOCAL_PROTOCOLS.some()`, `aIconURL.startsWith()`, `aTab.getAttribute()`, `makeString()`, `this._callProgressListeners()`, `this.getBrowserForTab()`
- 条件付き依存: `if ( aIconURL && !LOCAL_PROTOCOLS.some(protocol => aIconURL.startsWith(protocol)) )` → `console.error()`
- 条件付き依存: `if (aClearImageFirst)` → `aTab.removeAttribute()`
- 条件付き依存: `if (aIconURL)` → `url.startsWith()`
- 条件付き依存: `if ( lazy.remoteSVGIconDecoding && url.startsWith(lazy.FaviconUtils.SVG_DATA_URI_PREFIX) )` → `this.#getMozRemoteImageURLForSvg()`
- 条件付き依存: `if (aIconURL)` → `aTab.setAttribute()`
- 条件付き依存: `if (!(aIconURL))` → `aTab.removeAttribute()`
- 条件付き依存: `if (aIconURL != aTab.getAttribute("image"))` → `this._tabAttrModified()`

## makeString()
- 位置: L1642-1642
- 役割: (未記入)
- 触るとき: (未記入)
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md)

## Tabbrowser.#maybeRefreshIcons()
- 位置: L1689-1709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `iconURL.startsWith()`, `tab.setAttribute()`, `this.#getMozRemoteImageURLForSvg()`, `this.getBrowserForTab()`

## Tabbrowser.#getMozRemoteImageURLForSvg()
- 位置: L1711-1730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `lazy.FaviconUtils.getMozRemoteImageURL()`, `this.documentGlobal.matchMedia()`

## Tabbrowser.getIcon()
- 位置: L1732-1735
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserForTab()`

## Tabbrowser.setPageInfo()
- 位置: L1737-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aURL)` → `lazy.PlacesUtils.history.update(pageInfo).catch()`
- 条件付き依存: `if (aURL)` → `lazy.PlacesUtils.history.update()`

## Tabbrowser.#populateTitleCache()
- 位置: L1752-1762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.getElementById()`

## Tabbrowser.#determineTaskbarTabTitle()
- 位置: L1802-1852
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getUserContextLabel()`, `lazy.TaskbarTabsUtils.getTaskbarTabIdFromWindow()`, `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (!this.#taskbarTab)` → `lazy.TaskbarTabs.getTaskbarTab(id) .then(tt => { this.#taskbarTab = tt; this.updateTitlebar(); }) .catch()`
- 条件付き依存: `if (!this.#taskbarTab)` → `lazy.TaskbarTabs.getTaskbarTab(id) .then()`
- 条件付き依存: `if (!this.#taskbarTab)` → `lazy.TaskbarTabs.getTaskbarTab()`
- 条件付き依存: `if (!this.#taskbarTab)` → `this.updateTitlebar()`

## Tabbrowser.#determineContentTitle()
- 位置: L1854-1904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `docElement.hasAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getTabForBrowser()`
- 条件付き依存: `if ( docElement.hasAttribute("web-extension-popup-window") || docElement.hasAttribute("chromeless-window") )` → `Services.io.createExposableURI()`
- 条件付き依存: `if (uri.scheme == "moz-extension")` → `WebExtensionPolicy.getByHostname()`
- 条件付き依存: `if (ext && ext.name)` → `this.document.getElementById()`
- 条件付き依存: `if (docElement.hasAttribute("titlepreface"))` → `docElement.getAttribute()`
- 条件付き依存: `if (tab.labelIsContentTitle)` → `tab.getAttribute("label").replace()`
- 条件付き依存: `if (tab.labelIsContentTitle)` → `tab.getAttribute()`
- XPCOM: `Services.io`

## Tabbrowser.getWindowTitleForBrowser()
- 位置: L1906-1950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `docElement.getAttribute()`, `lazy.SelectableProfileService.currentProfile?.name.replace()`, `lazy.SelectableProfileService.getCachedProfileCount()`, `parts.filter()`, `parts.filter(p => !!p).join()`, `this.#determineContentTitle()`, `this.#determineTaskbarTabTitle()`
- 条件付き依存: `if (!this.#cachedTitleInfo)` → `this.#populateTitleCache()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" && contentTitle && isTemporaryPrivateWindow )` → `parts.push()`
- 条件付き依存: `if ( !taskbarTabTitle && (!contentTitle || AppConstants.platform != "macosx") )` → `parts.push()`

## Tabbrowser.updateTitlebar()
- 位置: L1952-1954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindowTitleForBrowser()`

## Tabbrowser.updateCurrentBrowser()
- 位置: L1956-2210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabListeners.get()`, `newBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `newBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `newTab.hasAttribute()`, `newTab.setAttribute()`, `oldBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `oldBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `oldTab.removeAttribute()`, `this.#lastRelatedTabMap.get()`, `this.#updateUserContextUIIndicator()`, `this.#updateVisibleNotificationBox()`, `this._callProgressListeners()`, `this.appendStatusPanel()`, `this.documentGlobal.gPermissionPanel.updateSharingIndicator()`, `this.documentGlobal.gURLBar?.saveSelectionStateForBrowser()`, `this.getBrowserAtIndex()`, `this.getTabForBrowser()`, `this.showTab()`
- 条件付き依存: `if (!aForceUpdate)` → `Glean.browserTabswitch.update.start()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher().requestTab()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher()`
- 条件付き依存: `if (!aForceUpdate)` → `this.document.commandDispatcher.lock()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `oldBrowser.removeAttribute()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `newBrowser.setAttribute()`
- 条件付き依存: `if (oldBrowserPopupsBlocked != newBrowserPopupsBlocked)` → `newBrowser.popupAndRedirectBlocker.sendObserverUpdateBlockedPopupsEvent()`
- 条件付き依存: `if (oldBrowserRedirectBlocked != newBrowserRedirectBlocked)` → `newBrowser.popupAndRedirectBlocker.sendObserverUpdateBlockedRedirectEvent()`
- 条件付き依存: `if (securityUI)` → `this._callProgressListeners()`
- 条件付き依存: `if (securityUI)` → `newBrowser.getContentBlockingEvents()`
- 条件付き依存: `if (listener && listener._stateFlags)` → `this._callProgressListeners()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.recordTimeFromUnloadToReload()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.updateLastAccessed()`
- 条件付き依存: `if (!this.#previewMode)` → `oldTab.updateLastAccessed()`
- 条件付き依存: `if (!this.#previewMode)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (this.documentGlobal == lazy.BrowserWindowTracker.getTopWindow())` → `newTab.updateLastSeenActive()`
- 条件付き依存: `if (this.documentGlobal == lazy.BrowserWindowTracker.getTopWindow())` → `oldTab.updateLastSeenActive()`
- 条件付き依存: `if (!this.#previewMode)` → `Tabbrowser.#findBars.get()`
- 条件付き依存: `if (!this.#previewMode)` → `this.updateTitlebar()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.removeAttribute()`
- 条件付き依存: `if (!this.#previewMode)` → `newBrowser.unselectedTabHover()`
- 条件付き依存: `if (newTab.hasAttribute("busy") && !this._isBusy)` → `this._callProgressListeners()`
- 条件付き依存: `if (!newTab.hasAttribute("busy") && this._isBusy)` → `this._callProgressListeners()`
- 条件付き依存: `if (!this.#previewMode)` → `Tabbrowser.#tabsLeavingAdoptedSplitView.has()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.dispatchEvent()`
- 条件付き依存: `if (!this.#previewMode)` → `this.#checkIfShouldTriggerTabSelectMessage()`
- 条件付き依存: `if (!this.#previewMode)` → `this._tabAttrModified()`
- 条件付き依存: `if (!this.#previewMode)` → `this.#startMultiSelectChange()`
- 条件付き依存: `if (!this.#previewMode)` → `this.clearMultiSelectedTabs()`
- 条件付き依存: `if (this.#multiSelectChangeAdditions.size)` → `this.addToMultiSelectedTabs()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this._adjustFocusBeforeTabSwitch()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this._adjustFocusAfterTabSwitch()`
- 条件付き依存: `if (aForceUpdate || !this.documentGlobal.gMultiProcessBrowser)` → `this.documentGlobal.gURLBar.afterTabSwitchFocusChange()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this.document.commandDispatcher.unlock()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this.dispatchEvent()`
- 条件付き依存: `if (!aForceUpdate)` → `Glean.browserTabswitch.update.stopAndAccumulate()`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## Tabbrowser.#checkIfShouldTriggerTabSelectMessage()
- 位置: async L2219-2269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `[oldTab, newTab].some()`, `[oldTabSpec, newTabSpec].sort()`, `this.#tabSelectTimestamps.filter()`, `this.#tabSelectTimestamps.find()`
- 条件付き依存: `if (existingEntry.count === LIMIT_FOR_TRIGGER)` → `lazy.ASRouter.sendTriggerMessage()`
- 条件付き依存: `if (existingEntry.count === LIMIT_FOR_TRIGGER)` → `this.#tabSelectTimestamps.filter()`
- 条件付き依存: `if (!(existingEntry))` → `this.#tabSelectTimestamps.push()`

## Tabbrowser._adjustFocusBeforeTabSwitch()
- 位置: L2271-2314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.documentGlobal.gURLBar.getBrowserState()`, `this.isFindBarInitialized()`
- 条件付き依存: `if (this.isFindBarInitialized(oldTab))` → `this.getCachedFindBar()`
- 条件付き依存: `if (this.isFindBarInitialized(oldTab))` → `findBar._findField.getAttribute()`
- 条件付き依存: `if (activeEl == oldTab)` → `newTab.focus()`
- 条件付き依存: `if ( this.documentGlobal.gMultiProcessBrowser && activeEl != newBrowser && activeEl != newTab )` → `this.documentGlobal.gURLBar.getBrowserState()`
- 条件付き依存: `if (!keepFocusOnUrlBar)` → `this.document.activeElement.blur()`

## Tabbrowser._adjustFocusAfterTabSwitch()
- 位置: L2316-2447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fm.setFocus()`, `newBrowser.hasAttribute()`, `this.documentGlobal.gURLBar.getBrowserState()`, `this.getBrowserForTab()`
- 条件付き依存: `if (newBrowser.hasAttribute("tabDialogShowing"))` → `newBrowser.tabDialogBox.focus()`
- 条件付き依存: `if (this.documentGlobal.gURLBar.getBrowserState(newBrowser).urlbarFocused)` → `this.document.documentElement.hasAttribute()`
- 条件付き依存: `if (this.document.documentElement.hasAttribute("inDOMFullscreen"))` → `this.documentGlobal.addEventListener()`
- 条件付き依存: `if (!this.documentGlobal.fullScreen || newTab.isEmpty)` → `selectURL()`
- 条件付き依存: `if ( this.documentGlobal.gFindBarInitialized && !this.documentGlobal.gFindBar.hidden && this.selectedTab._findBarFocused )` → `this.documentGlobal.gFindBar._findField.focus()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `fm.getFocusedElementForWindow()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `HTMLAnchorElement.isInstance()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `newFocusedElement.getAttributeNS()`
- XPCOM: `Services.focus`

## selectURL()
- 位置: L2332-2378
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#asyncTabSwitching)` → `this.documentGlobal.gURLBar.inputField.addEventListener()`
- 条件付き依存: `if (this.#asyncTabSwitching)` → `this.documentGlobal.gURLBar.restoreSelectionStateForBrowser()`
- 条件付き依存: `if (!(this.#asyncTabSwitching))` → `this.documentGlobal.gURLBar.restoreSelectionStateForBrowser()`

## Tabbrowser._tabAttrModified()
- 位置: L2449-2462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.dispatchEvent()`

## Tabbrowser.resetBrowserSharing()
- 位置: L2464-2478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.removeAttribute()`, `this._tabAttrModified()`, `this.getTabForBrowser()`
- 条件付き依存: `if (aBrowser == this.selectedBrowser)` → `this.documentGlobal.gPermissionPanel.updateSharingIndicator()`

## Tabbrowser.updateBrowserSharing()
- 位置: L2480-2507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.getTabForBrowser()`
- 条件付き依存: `if (aBrowser._sharingState.webRTC.paused)` → `tab.removeAttribute()`
- 条件付き依存: `if (!(aBrowser._sharingState.webRTC.paused))` → `tab.setAttribute()`
- 条件付き依存: `if (!(aBrowser._sharingState.webRTC?.sharing))` → `tab.removeAttribute()`
- 条件付き依存: `if ("webRTC" in aState)` → `this._tabAttrModified()`
- 条件付き依存: `if (aBrowser == this.selectedBrowser)` → `this.documentGlobal.gPermissionPanel.updateSharingIndicator()`

## Tabbrowser.getTabSharingState()
- 位置: L2509-2521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `state.screen.replace()`

## Tabbrowser.setInitialTabTitle()
- 位置: L2543-2564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (aTitle)` → `aTab.getAttribute()`
- 条件付き依存: `if (!aTab.getAttribute("label"))` → `Tabbrowser.#tabsWithInitialTitle.add()`
- 条件付き依存: `if (aTitle)` → `this.#setTabLabel()`

## Tabbrowser.setTabTitle()
- 位置: L2586-2650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#nonPrintingRegEx.test()`, `Tabbrowser.#tabsWithInitialTitle.has()`, `aTab.hasAttribute()`, `this.#setTabLabel()`, `this.getBrowserForTab()`, `title.trim()`
- 条件付き依存: `if (aTab.hasAttribute("customizemode"))` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (Tabbrowser.#tabsWithInitialTitle.has(aTab))` → `Tabbrowser.#tabsWithInitialTitle.delete()`
- 条件付き依存: `if (browser.currentURI.displaySpec)` → `Services.io.createExposableURI()`
- 条件付き依存: `if (!title)` → `this.documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (title && !this.documentGlobal.isBlankPageURL(title))` → `Tabbrowser.#dataURLRegEx.test()`
- 条件付き依存: `if (title.length <= 500 || !Tabbrowser.#dataURLRegEx.test(title))` → `Services.textToSubURI.unEscapeNonAsciiURI()`
- XPCOM: `Services.io` / `Services.textToSubURI`

## Tabbrowser.setTabLabelForAuthPrompts()
- 位置: L2656-2658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setTabLabel()`

## Tabbrowser.#setTabLabel()
- 位置: L2680-2736
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^about:reader\?url=/.test()`, `Tabbrowser.#dataURLRegEx.test()`, `Tabbrowser.#fullLabels.set()`, `aTab.getAttribute()`, `aTab.setAttribute()`, `aTab.toggleAttribute()`, `dwu.getDirectionFromText()`
- 条件付き依存: `if (isURL && aLabel.length > 500 && Tabbrowser.#dataURLRegEx.test(aLabel))` → `aLabel.substring()`
- 条件付き依存: `if (!isContentTitle)` → `aLabel.replace()`
- 条件付き依存: `if (aLabel.length > TAB_LABEL_MAX_LENGTH)` → `aLabel.substring()`
- 条件付き依存: `if (!beforeTabOpen)` → `this._tabAttrModified()`
- 条件付き依存: `if (aTab.selected)` → `this.updateTitlebar()`
- XPCOM: [`nsIDOMWindowUtils`](../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md)

## Tabbrowser.loadTabs()
- 位置: L2780-2929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `tabs.push()`, `this.addTab()`
- 条件付き依存: `if (typeof elementIndex == "number")` → `this.#elementIndexToTabIndex()`
- 条件付き依存: `if (replace)` → `Tabbrowser.isTabGroupLabel()`
- 条件付き依存: `if (targetTab)` → `this.getBrowserForTab()`
- 条件付き依存: `if (replace)` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if (replace)` → `tabs.push()`
- 条件付き依存: `if (!(replace))` → `this.addTab()`
- 条件付き依存: `if (!(replace))` → `tabs.push()`
- XPCOM: `Services.prefs`

## Tabbrowser.updateBrowserRemoteness()
- 位置: L2945-3088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Tabbrowser.#tabListeners.set()`, `aBrowser.changeRemoteness()`, `aBrowser.construct()`, `aBrowser.destroy()`, `aBrowser.didStartLoadSinceLastUserTyping()`, `aBrowser.getContentBlockingEvents()`, `aBrowser.hasAttribute()`, `aBrowser.webProgress.addProgressListener()`, `evt.initEvent()`, `filter.addProgressListener()`, `listener?.destroy()`, `tab.dispatchEvent()`, `this.#insertBrowser()`, `this._callProgressListeners()`, `this.document.createEvent()`, `this.getTabForBrowser()`, `this.isFindBarInitialized()`
- 条件付き依存: `if (filter)` → `aBrowser.webProgress.removeProgressListener()`
- 条件付き依存: `if (filter)` → `filter.removeProgressListener()`
- 条件付き依存: `if (shouldBeRemote)` → `aBrowser.setAttribute()`
- 条件付き依存: `if (!(shouldBeRemote))` → `aBrowser.removeAttribute()`
- 条件付き依存: `if (hadStartedLoad)` → `aBrowser.urlbarChangeTracker.startedLoad()`
- 条件付き依存: `if (!filter)` → `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`
- 条件付き依存: `if (!filter)` → `Tabbrowser.#tabFilters.set()`
- 条件付き依存: `if (shouldBeRemote)` → `tab.removeAttribute()`
- 条件付き依存: `if (this.isFindBarInitialized(tab))` → `this.getCachedFindBar()`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1`

## Tabbrowser.updateBrowserRemotenessByURL()
- 位置: L3107-3129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `this.getTabForBrowser()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this.updateBrowserRemoteness()`
- 条件付き依存: `if (oldRemoteType != options.remoteType || options.newFrameloader)` → `this.updateBrowserRemoteness()`

## Tabbrowser.createBrowser()
- 位置: L3156-3270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getGlobalForObject()`, `Services.obs.notifyObservers()`, `b.setAttribute()`, `browserContainer.appendChild()`, `browserSidebarContainer.appendChild()`, `lazy.AIWindow.isAIWindowActive()`, `stack.appendChild()`, `this.document.createXULElement()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser || remoteType)` → `b.setAttribute()`
- 条件付き依存: `if (userContextId)` → `b.setAttribute()`
- 条件付き依存: `if (remoteType)` → `b.setAttribute()`
- 条件付き依存: `if (!isPreloadBrowser)` → `b.setAttribute()`
- 条件付き依存: `if (isPreloadBrowser)` → `b.setAttribute()`
- 条件付き依存: `if (initialBrowsingContextGroupId)` → `b.setAttribute()`
- 条件付き依存: `if (name)` → `b.setAttribute()`
- 条件付き依存: `if ( lazy.AIWindow.isAIWindowActive(this.documentGlobal) || lazy.allowTransparentBrowser )` → `b.setAttribute()`
- 条件付き依存: `if (!uriIsAboutBlank || skipLoad)` → `b.setAttribute()`
- XPCOM: `Services.obs`

## Tabbrowser.#createLazyBrowser()
- 位置: L3272-3372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`

## getter()
- 位置: L3283-3283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.hasAttribute()`

## getter()
- 位置: L3286-3286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getLazyTabValue()`

## getter()
- 位置: L3289-3297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.SessionStore.getLazyTabValue()`
- XPCOM: `Services.io`

## getter()
- 位置: L3300-3300
- 役割: (未記入)
- 触るとき: (未記入)

## getter()
- 位置: L3304-3304
- 役割: (未記入)
- 触るとき: (未記入)

## getter()
- 位置: L3307-3307
- 役割: (未記入)
- 触るとき: (未記入)

## getter()
- 位置: L3310-3310
- 役割: (未記入)
- 触るとき: (未記入)

## getter()
- 位置: L3313-3313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.hasAttribute()`

## getter()
- 位置: L3316-3316
- 役割: (未記入)
- 触るとき: (未記入)

## getter()
- 位置: L3320-3331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.addEventListener()`, `browser[name]()`, `this.#insertBrowser()`

## getter()
- 位置: L3334-3341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `aTab.getAttribute()`, `lazy.SessionStore.getLazyTabValue()`

## getter()
- 位置: L3345-3345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getLazyTabValue()`

## getter()
- 位置: L3348-3355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#insertBrowser()`
- 条件付き依存: `if (AppConstants.NIGHTLY_BUILD)` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## setter()
- 位置: L3356-3363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#insertBrowser()`
- 条件付き依存: `if (AppConstants.NIGHTLY_BUILD)` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## Tabbrowser.insertBrowser()
- 位置: L3381-3383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#insertBrowser()`

## Tabbrowser.#insertBrowser()
- 位置: L3385-3493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`, `Tabbrowser.#browserParams.delete()`, `Tabbrowser.#browserParams.get()`, `Tabbrowser.#generateUniquePanelID()`, `Tabbrowser.#tabFilters.set()`, `Tabbrowser.#tabListeners.set()`, `URILoadingWrapper.fixupAndLoadURIString.bind()`, `URILoadingWrapper.loadURI.bind()`, `browser.webProgress.addProgressListener()`, `filter.addProgressListener()`, `this.getPanel()`
- 条件付き依存: `if (!panel.parentNode)` → `this.tabpanels.appendChild()`
- 条件付き依存: `if (aTab.userContextId)` → `browser.setAttribute()`
- 条件付き依存: `if (aTab.selected)` → `this.#updateUserContextUIIndicator()`
- 条件付き依存: `if (aTab.isConnected)` → `aTab.dispatchEvent()`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1`

## Tabbrowser.#mayDiscardBrowser()
- 位置: L3495-3521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.permitUnload()`, `this.getTabDialogBox()`

## Tabbrowser.prepareDiscardBrowser()
- 位置: async L3523-3535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabStateFlusher.flush()`

## Tabbrowser.discardBrowser()
- 位置: L3537-3619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#browserParams.set()`, `Tabbrowser.#findBars.get()`, `Tabbrowser.#tabFilters.delete()`, `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.delete()`, `Tabbrowser.#tabListeners.get()`, `aTab.dispatchEvent()`, `aTab.hasAttribute()`, `aTab.removeAttribute()`, `browser.destroy()`, `browser.webProgress.removeProgressListener()`, `filter.removeProgressListener()`, `lazy.SessionStore.resetBrowserToLazyState()`, `lazy.webrtcUI.forgetStreamsFromBrowserContext()`, `listener.destroy()`, `tabDialogBox.abortAllDialogs()`, `this.#createLazyBrowser()`, `this.#mayDiscardBrowser()`, `this._switcher?.onTabDiscarded()`, `this.getPanel()`, `this.getPanel(browser).remove()`, `this.getTabDialogBox()`, `this.resetBrowserSharing()`
- 条件付き依存: `if (aForceDiscard)` → `aTab.toggleAttribute()`
- 条件付き依存: `if (findBar)` → `findBar.close()`
- 条件付き依存: `if (findBar)` → `findBar.remove()`
- 条件付き依存: `if (findBar)` → `Tabbrowser.#findBars.delete()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `removedAttributes.push()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `aTab.removeAttribute()`
- 条件付き依存: `if (removedAttributes.length)` → `this._tabAttrModified()`

## Tabbrowser.addWebTab()
- 位置: L3628-3641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addTab()`
- 条件付き依存: `if (!params.triggeringPrincipal)` → `Services.scriptSecurityManager.createNullPrincipal()`
- XPCOM: `Services.scriptSecurityManager`

## Tabbrowser.addAdjacentNewTab()
- 位置: L3649-3667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `resolve()`, `this.addTrustedTab()`
- XPCOM: `Services.obs`

## Tabbrowser.addAdjacentTab()
- 位置: L3677-3690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `adjacentTab.group.tabs.at()`, `this.addTab()`

## Tabbrowser.addTrustedTab()
- 位置: L3701-3705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `this.addTab()`
- XPCOM: `Services.scriptSecurityManager`

## Tabbrowser.addTab()
- 位置: L3824-4105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UserInteraction.running()`, `console.error()`, `t?.remove()`, `this.#createBrowserForTab()`, `this.#createTab()`, `this.#determineURIToLoad()`, `this.documentGlobal.gSharedTabWarning.tabAdded()`, `this.getTabForBrowser()`, `this.tabContainer.markTabOpening()`
- 条件付き依存: `if (!UserInteraction.running("browser.tabs.opening", this.documentGlobal))` → `UserInteraction.start()`
- 条件付き依存: `if (insertTab)` → `this.#insertTabAtIndex()`
- 条件付き依存: `if (focusUrlBar)` → `this.documentGlobal.gURLBar.getBrowserState()`
- 条件付き依存: `if (createLazyBrowser)` → `this.#createLazyBrowser()`
- 条件付き依存: `if (lazyBrowserURI)` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`
- 条件付き依存: `if (lazyBrowserURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (insertTab)` → `lazy.SessionStore.setTabState()`
- 条件付き依存: `if (insertTab)` → `lazy.E10SUtils.serializePrincipal()`
- 条件付き依存: `if (!(createLazyBrowser))` → `this.#insertBrowser()`
- 条件付き依存: `if (t?.linkedBrowser)` → `Tabbrowser.#tabFilters.delete()`
- 条件付き依存: `if (t?.linkedBrowser)` → `Tabbrowser.#tabListeners.delete()`
- 条件付き依存: `if (t?.linkedBrowser)` → `this.getPanel(t.linkedBrowser).remove()`
- 条件付き依存: `if (t?.linkedBrowser)` → `this.getPanel()`
- 条件付き依存: `if (insertTab)` → `this.#fireTabOpen()`
- 条件付き依存: `if (insertTab)` → `this.#kickOffBrowserLoad()`
- 条件付き依存: `if (usingPreloadedContent)` → `this.documentGlobal.requestAnimationFrame()`
- 条件付き依存: `if (usingPreloadedContent)` → `t.setAttribute()`
- 条件付き依存: `if (!(usingPreloadedContent))` → `this.documentGlobal.requestAnimationFrame()`
- 条件付き依存: `if (!(usingPreloadedContent))` → `t.setAttribute()`
- 条件付き依存: `if (pinned)` → `this.#notifyPinnedStatus()`

## Tabbrowser.#elementIndexToTabIndex()
- 位置: L4107-4122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `Tabbrowser.isTabGroupLabel()`

## Tabbrowser.#createTabSplitView()
- 位置: L4128-4140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.createXULElement()`
- 条件付き依存: `if (!id)` → `lazy.SessionStore.getNextSplitViewId()`

## Tabbrowser.addTabSplitView()
- 位置: L4160-4223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `splitview.addTabs()`, `this.#createTabSplitView()`, `this.tabContainer.dispatchEvent()`, `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!splitview.tabs.length)` → `splitview.remove()`
- 条件付き依存: `if (trigger && tabGroupInfo)` → `Glean.splitview.start.record()`

## Tabbrowser.showSplitViewPanels()
- 位置: L4230-4243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelEl?.classList.toggle()`, `this.#insertBrowser()`, `this.#insertSplitViewFooter()`, `this.document.getElementById()`
- 条件付き依存: `if (tab.linkedBrowser)` → `panels.push()`

## Tabbrowser.#insertSplitViewFooter()
- 位置: L4250-4260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelEl?.querySelector()`, `this.document.getElementById()`
- 条件付き依存: `if (panelEl)` → `this.document.createXULElement()`
- 条件付き依存: `if (panelEl)` → `footer.setTab()`
- 条件付き依存: `if (panelEl)` → `panelEl.querySelector(".browserStack").appendChild()`
- 条件付き依存: `if (panelEl)` → `panelEl.querySelector()`

## Tabbrowser.openSplitViewMenu()
- 位置: L4262-4269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.openPopup()`, `menu.setAttribute()`, `this.document.getElementById()`

## Tabbrowser.#createTabGroup()
- 位置: L4279-4289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.createXULElement()`

## Tabbrowser.addTabGroup()
- 位置: L4316-4380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `Tabbrowser.isTab()`, `group.addTabs()`, `group.tabs.forEach()`, `lazy.TabStateFlusher.flush()`, `tabsAndSplitViews.some()`, `this.#createTabGroup()`, `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!id)` → `Date.now()`
- 条件付き依存: `if (!id)` → `Math.round()`
- 条件付き依存: `if (!id)` → `Math.random()`
- 条件付き依存: `if (!group.tabs.length)` → `group.remove()`
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `group.dispatchEvent()`

## Tabbrowser.removeTabGroup()
- 位置: async L4391-4445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.dispatchEvent()`, `this.removeTabs()`
- 条件付き依存: `if (this.tabGroupMenu.panel.state != "closed")` → `this.tabGroupMenu.panel.hidePopup()`
- 条件付き依存: `if (!options.skipPermitUnload)` → `this.runBeforeUnloadForTabs()`
- 条件付き依存: `if (cancel)` → `lazy.SessionStore.getSavedTabGroup()`
- 条件付き依存: `if (lazy.SessionStore.getSavedTabGroup(group.id))` → `lazy.SessionStore.forgetSavedTabGroup()`

## Tabbrowser.ungroupTab()
- 位置: L4453-4461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleTabMove()`, `this.tabContainer.insertBefore()`

## Tabbrowser.ungroupSplitView()
- 位置: L4463-4474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `this.#handleTabMove()`, `this.tabContainer.insertBefore()`

## Tabbrowser.adoptTabGroup()
- 位置: L4484-4544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `group.documentGlobal.gBrowser.nonHiddenTabs.every()`, `this.addTabGroup()`
- 条件付き依存: `if (noOtherTabsInWindow)` → `group.dispatchEvent()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(element))` → `this.adoptSplitView()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(element))` → `newTabs.push()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(element)))` → `this.adoptTab()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(element)))` → `newTabs.push()`

## Tabbrowser.adoptSplitView()
- 位置: L4554-4593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabsJoiningAdoptedSplitView.add()`, `Tabbrowser.#tabsJoiningAdoptedSplitView.delete()`, `Tabbrowser.#tabsLeavingAdoptedSplitView.add()`, `newTabs.push()`, `this.addTabSplitView()`, `this.adoptTab()`

## Tabbrowser.getAllTabGroups()
- 位置: L4603-4616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `acc.concat()`, `lazy.BrowserWindowTracker.getOrderedWindows()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (sortByLastSeenActive)` → `groups.sort()`

## Tabbrowser.getTabGroupById()
- 位置: L4618-4629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getOrderedWindows()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`

## Tabbrowser.#determineURIToLoad()
- 位置: L4631-4652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- XPCOM: `Services.io`

## Tabbrowser.#createTab()
- 位置: L4674-4749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `t.classList.add()`, `this.document.createXULElement()`, `this.tabContainer._unlockTabSizing()`
- 条件付き依存: `if (!noInitialLabel)` → `this.documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (this.documentGlobal.isBlankPageURL(uriString))` → `t.setAttribute()`
- 条件付き依存: `if (!(this.documentGlobal.isBlankPageURL(uriString)))` → `this.setInitialTabTitle()`
- 条件付き依存: `if (userContextId)` → `t.setAttribute()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.setTabStyle()`
- 条件付き依存: `if (skipBackgroundNotify)` → `t.setAttribute()`
- 条件付き依存: `if (pinned)` → `t.setAttribute()`
- 条件付き依存: `if (!animate)` → `UserInteraction.update()`
- 条件付き依存: `if (!animate)` → `t.setAttribute()`
- 条件付き依存: `if (!animate)` → `this.documentGlobal.setTimeout()`
- 条件付き依存: `if (!animate)` → `tabContainer._handleNewTab()`
- 条件付き依存: `if (!(!animate))` → `UserInteraction.update()`

## Tabbrowser.#createBrowserForTab()
- 位置: L4785-4880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `Tabbrowser.#browserParams.set()`, `this.#tabForBrowser.set()`, `this.setDefaultIcon()`
- 条件付き依存: `if ( uriIsAboutBlank && !preferredRemoteType && referrerInfo && referrerInfo.originalReferrer )` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if ( uriString == this.documentGlobal.BROWSER_NEW_TAB_URL && !userContextId )` → `lazy.NewTabPagePreloading.getPreloadedBrowser()`
- 条件付き依存: `if (!b)` → `this.createBrowser()`

## Tabbrowser.#kickOffBrowserLoad()
- 位置: L4937-5047
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !usingPreloadedContent && originPrincipal && originStoragePrincipal && uriString )` → `this.documentGlobal.doGetProtocolFlags()`
- 条件付き依存: `if (shouldInheritSecurityContext)` → `browser.createAboutBlankDocumentViewer()`
- 条件付き依存: `if ( !usingPreloadedContent && (!uriIsAboutBlank || !allowInheritPrincipal) && !skipLoad )` → `this.documentGlobal.gInitialPages.includes()`
- 条件付き依存: `if ( !usingPreloadedContent && (!uriIsAboutBlank || !allowInheritPrincipal) && !skipLoad )` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if ( !usingPreloadedContent && (!uriIsAboutBlank || !allowInheritPrincipal) && !skipLoad )` → `console.error()`
- XPCOM: [`nsIProtocolHandler`](../../../netwerk/base/nsIIOService.idl.md)

## Tabbrowser.createTabsForSessionRestore()
- 位置: L5082-5316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.initEvent()`, `lazy.SessionStore.isTabRestoring()`, `splitViewWorkingData.get()`, `splitViewWorkingData.set()`, `splitViewWorkingData.values()`, `tab.dispatchEvent()`, `tab.initialize()`, `tabGroupWorkingData.set()`, `tabGroupWorkingData.values()`, `tabs.push()`, `this.document.createDocumentFragment()`, `this.document.createEvent()`, `this.tabContainer._invalidateCachedTabs()`, `this.tabContainer.appendChild()`
- 条件付き依存: `if (!tabData.pinned)` → `this.unpinTab()`
- 条件付き依存: `if (!(!tabData.pinned))` → `this.pinTab()`
- 条件付き依存: `if (tabData.entries?.length)` → `Math.min()`
- 条件付き依存: `if (tabData.entries?.length)` → `Math.max()`
- 条件付き依存: `if (!tab)` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (!tab)` → `this.addTrustedTab()`
- 条件付き依存: `if (splitView)` → `splitView.tabs.push()`
- 条件付き依存: `if (splitView.tabs.length == splitView.numberOfTabs)` → `this.#createTabSplitView()`
- 条件付き依存: `if (tabData.pinned)` → `this.pinTab()`
- 条件付き依存: `if (tabData.pinned)` → `this.#fireTabOpen()`
- 条件付き依存: `if (tabData.groupId)` → `tabGroupWorkingData.get()`
- 条件付き依存: `if (!splitView)` → `tabGroup.containingTabsFragment.appendChild()`
- 条件付き依存: `if (splitView?.node)` → `tabGroup.containingTabsFragment.appendChild()`
- 条件付き依存: `if (!tabGroup.node)` → `this.#createTabGroup()`
- 条件付き依存: `if (!tabGroup.node)` → `tabsFragment.appendChild()`
- 条件付き依存: `if (tab.hidden)` → `hiddenTabs.set()`
- 条件付き依存: `if (!splitView)` → `tabsFragment.appendChild()`
- 条件付き依存: `if (splitView?.node)` → `splitView.tabs.some()`
- 条件付き依存: `if (splitView.tabs.some(t => t.hidden))` → `splitView.node.toggleAttribute()`
- 条件付き依存: `if (splitView?.node)` → `tabsFragment.appendChild()`
- 条件付き依存: `if (tabWasReused)` → `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (tabGroup.node)` → `tabGroup.node.appendChild()`
- 条件付き依存: `if (splitView.node)` → `splitView.node.addTabs()`
- 条件付き依存: `if (hiddenBy)` → `lazy.SessionStore.setCustomTabValue()`
- 条件付き依存: `if (tabToSelect)` → `this.removeTab()`
- 条件付き依存: `if (tabs.length > 1 || !tabs[0].selected)` → `this.#updateTabsAfterInsert()`
- 条件付き依存: `if (tabs.length > 1 || !tabs[0].selected)` → `this.documentGlobal.TabBarVisibility.update()`
- 条件付き依存: `if (!tab.pinned)` → `this.#fireTabOpen()`
- 条件付き依存: `if (tab.linkedPanel)` → `tab.dispatchEvent()`

## Tabbrowser.moveTabsToStart()
- 位置: L5328-5339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.moveTabToStart()`, `this.recordTabMetrics()`

## Tabbrowser.moveTabsToEnd()
- 位置: L5351-5361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.moveTabToEnd()`, `this.recordTabMetrics()`

## Tabbrowser.warnAboutClosingTabs()
- 位置: L5363-5479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `ps.confirmEx()`, `this.documentGlobal.focus()`, `this.documentGlobal.gDialogBox.replaceDialogIfOpen()`, `this.tabLocalization.formatValuesSync()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `this.documentGlobal.focus()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `this.tabLocalization.formatValuesSync()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `ps.confirmEx()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL && reallyClose && !warnOnClose.value )` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs` / `Services.prompt`

## Tabbrowser.#insertTabAtIndex()
- 位置: L5502-5657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allItems.at()`, `tab.initialize()`, `this.#updateTabsAfterInsert()`, `this.documentGlobal.TabBarVisibility.update()`, `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (typeof elementIndex != "number" && typeof tabIndex != "number")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !bulkOrderedOpen && ((openerTab && insertRelatedAfterCurrent) || Services.prefs.getBoolPref("browser.tabs.insertAfterCurrent")) )` → `this.#lastRelatedTabMap.get()`
- 条件付き依存: `if ( !bulkOrderedOpen && ((openerTab && insertRelatedAfterCurrent) || Services.prefs.getBoolPref("browser.tabs.insertAfterCurrent")) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (previousTab.visible && previousTab.splitview)` → `this.tabContainer.dragAndDropElements.indexOf()`
- 条件付き依存: `if (openerTab)` → `this.#lastRelatedTabMap.set()`
- 条件付き依存: `if (tab.pinned)` → `Math.max()`
- 条件付き依存: `if (tab.pinned)` → `Math.min()`
- 条件付き依存: `if (!(tab.pinned))` → `Math.max()`
- 条件付き依存: `if (!(tab.pinned))` → `Math.min()`
- 条件付き依存: `if (tabGroup)` → `Tabbrowser.isTab()`
- 条件付き依存: `if (tabGroup)` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if ( (Tabbrowser.isTab(itemAfter) && itemAfter.group == tabGroup) || Tabbrowser.isSplitViewWrapper(itemAfter) )` → `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!( (Tabbrowser.isTab(itemAfter) && itemAfter.group == tabGroup) || Tabbrowser.isSplitViewWrapper(itemAfter) ))` → `tabGroup.appendChild()`
- 条件付き依存: `if (!(tabGroup))` → `Tabbrowser.isTab()`
- 条件付き依存: `if (!(tabGroup))` → `Tabbrowser.isTabGroupLabel()`
- 条件付き依存: `if ( (Tabbrowser.isTab(itemAfter) && itemAfter.group?.tabs[0] == itemAfter) || Tabbrowser.isTabGroupLabel(itemAfter) )` → `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!( (Tabbrowser.isTab(itemAfter) && itemAfter.group?.tabs[0] == itemAfter) || Tabbrowser.isTabGroupLabel(itemAfter) ))` → `tabContainer.insertBefore()`
- 条件付き依存: `if (pinned)` → `this.#updateTabBarForPinnedTabs()`
- XPCOM: `Services.prefs`

## Tabbrowser.#fireTabOpen()
- 位置: L5668-5675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.dispatchEvent()`

## Tabbrowser._getTabsToTheStartFrom()
- 位置: L5681-5703
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabsToStart.push()`

## Tabbrowser._getTabsToTheEndFrom()
- 位置: L5709-5731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabsToEnd.push()`

## Tabbrowser.#uriForDuplicateCheck()
- 位置: L5740-5749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.isTabRestoring()`

## Tabbrowser.getDuplicateTabsToClose()
- 位置: L5751-5807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyEquals()`, `keyForTab()`, `keys.some()`
- 条件付き依存: `if (aTab.multiselected)` → `keyForTab()`
- 条件付き依存: `if (key)` → `keys.push()`
- 条件付き依存: `if (!(aTab.multiselected))` → `keyForTab()`
- 条件付き依存: `if (key && keys.some(k => keyEquals(k, key)))` → `duplicateTabs.push()`

## keyForTab()
- 位置: L5756-5766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#uriForDuplicateCheck()`, `lazy.AIWindow.getChatTabConversationId()`

## keyEquals()
- 位置: L5767-5773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.uri.equals()`

## Tabbrowser.getAllDuplicateTabsToClose()
- 位置: L5809-5837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#uriForDuplicateCheck()`, `lazy.AIWindow.getChatTabConversationId()`, `this.tabs.toSorted()`, `userContextIds.add()`, `userContextIds.has()`, `userContextIdsPerUri.getOrInsertComputed()`
- 条件付き依存: `if (!tab.pinned && userContextIds.has(userContextId))` → `duplicateTabs.push()`

## Tabbrowser.removeDuplicateTabs()
- 位置: L5839-5846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeDuplicateTabs()`, `this.getDuplicateTabsToClose()`

## Tabbrowser.#removeDuplicateTabs()
- 位置: L5848-5863
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.documentGlobal.ConfirmationHint.show()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`

## Tabbrowser.removeAllDuplicateTabs()
- 位置: L5873-5881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeDuplicateTabs()`, `this.document.getElementById()`, `this.getAllDuplicateTabsToClose()`

## Tabbrowser.removeTabsToTheStartFrom()
- 位置: L5891-5903
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getTabsToTheStartFrom()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`

## Tabbrowser.removeTabsToTheEndFrom()
- 位置: L5913-5922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getTabsToTheEndFrom()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`

## Tabbrowser.removeAllTabsBut()
- 位置: L5940-5977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openTabs.filter()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`

## filterFn()
- 位置: L5954-5954
- 役割: (未記入)
- 触るとき: (未記入)

## filterFn()
- 位置: L5956-5956
- 役割: (未記入)
- 触るとき: (未記入)

## filterFn()
- 位置: L5960-5960
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.removeMultiSelectedTabs()
- 位置: L5989-6014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.warnAboutClosingTabs()`
- 条件付き依存: `if (excludePinnedTabs)` → `this.selectedTabs.filter()`
- 条件付き依存: `if (excludePinnedTabs)` → `this.removeTabs()`
- 条件付き依存: `if (excludePinnedTabs)` → `this.clearMultiSelectedTabs()`
- 条件付き依存: `if (!(excludePinnedTabs))` → `this.removeTabs()`

## Tabbrowser.#startRemoveTabs()
- 位置: L6050-6148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`
- 条件付き依存: `if (!skipRemoves && tab.selected)` → `this._findTabToBlurTo()`
- 条件付き依存: `if (toBlurTo)` → `this._getSwitcher().warmupTab()`
- 条件付き依存: `if (toBlurTo)` → `this._getSwitcher()`
- 条件付き依存: `if (!(!skipRemoves && tab.selected))` → `Tabbrowser.#hasBeforeUnload()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Glean.browserTabclose.permitUnloadTime.start()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Tabbrowser.#tabsPendingPermitUnload.add()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `beforeUnloadPromises.push()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `tab.linkedBrowser.asyncPermitUnload("dontUnload").then()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `tab.linkedBrowser.asyncPermitUnload()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Tabbrowser.#tabsPendingPermitUnload.delete()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Glean.browserTabclose.permitUnloadTime.stopAndAccumulate()`
- 条件付き依存: `if (!skipRemoves)` → `this.removeTab()`
- 条件付き依存: `if (!(permitUnload))` → `tabsWithBeforeUnloadPrompt.push()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `console.error()`
- 条件付き依存: `if (!(!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab)))` → `tabsWithoutBeforeUnload.push()`

## Tabbrowser.runBeforeUnloadForTabs()
- 位置: async L6168-6193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabsPendingPermitUnload.add()`, `Tabbrowser.#tabsPendingPermitUnload.delete()`, `console.error()`, `this.#startRemoveTabs()`, `this.getBrowserForTab()`, `this.getBrowserForTab(tab).permitUnload()`

## Tabbrowser.#separateWholeGroups()
- 位置: L6204-6233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabGroupSurvivingTabs.entries()`
- 条件付き依存: `if (tab.group)` → `tabGroupSurvivingTabs.has()`
- 条件付き依存: `if (!tabGroupSurvivingTabs.has(tab.group))` → `tabGroupSurvivingTabs.set()`
- 条件付き依存: `if (tab.group)` → `tabGroupSurvivingTabs.get(tab.group).delete()`
- 条件付き依存: `if (tab.group)` → `tabGroupSurvivingTabs.get()`
- 条件付き依存: `if (!survivingTabs.size)` → `wholeGroups.push()`
- 条件付き依存: `if (!survivingTabs.size)` → `tabs.filter()`
- 条件付き依存: `if (!survivingTabs.size)` → `tabGroup.tabs.includes()`

## Tabbrowser.removeTabs()
- 位置: L6260-6401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.all([...groupRemovalPromises, beforeUnloadComplete]).then()`, `Services.prefs.getBoolPref()`, `Services.tm.spinEventLoopUntilOrQuit()`, `console.error()`, `this.#avoidSingleSelectedTab()`, `this.#startRemoveTabs()`, `this.TabMetrics.decomposedContext()`, `this.removeTab()`
- 条件付き依存: `if ( this.tabs.length == tabs.length && (closeWindowWithLastTab ?? Services.prefs.getBoolPref("browser.tabs.closeWindowWithLastTab")) )` → `this.documentGlobal.closeWindow()`
- 条件付き依存: `if (!skipSessionStore)` → `lazy.SessionStore.resetLastClosedTabCount()`
- 条件付き依存: `if (!skipGroupCheck)` → `Tabbrowser.#separateWholeGroups()`
- 条件付き依存: `if (!skipGroupCheck)` → `groups.map()`
- 条件付き依存: `if (!skipGroupCheck)` → `groupTabsToClose.push()`
- 条件付き依存: `if (!skipSessionStore)` → `group.save()`
- 条件付き依存: `if (!skipGroupCheck)` → `this.removeTabGroup()`
- 条件付き依存: `if (!skipGroupCheck)` → `this.TabMetrics.decomposedContext()`
- 条件付き依存: `if (lastToClose)` → `this.removeTab()`
- 条件付き依存: `if (closedTabCount > 0)` → `this.recordTabMetrics()`
- XPCOM: `Services.prefs` / `Services.tm`

## Tabbrowser.removeCurrentTab()
- 位置: L6409-6411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeTab()`

## Tabbrowser.maybeCloseTabForRetargetedLoad()
- 位置: L6421-6433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTabForBrowser()`, `this.removeTab()`

## Tabbrowser.removeTab()
- 位置: L6465-6611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(triggeringEvent.target).closest()`, `Glean.browserTabclose.timeNoAnim.cancel()`, `Services.prefs.getBoolPref()`, `Tabbrowser.#closeTimeAnimTimerIds.get()`, `Tabbrowser.#closeTimeNoAnimTimerIds.delete()`, `Tabbrowser.#closeTimeNoAnimTimerIds.get()`, `UserInteraction.running()`, `aTab.hasAttribute()`, `aTab.removeAttribute()`, `lazy.MiniWindowManager.maybeMoveOldestMiniWindow()`, `tabbrowser.documentGlobal.getComputedStyle()`, `this.#beginRemoveTab()`, `this.#isLastTabInWindow()`, `this.documentGlobal.setTimeout()`, `this.documentGlobal.windowUtils.getBoundsWithoutFlushing()`, `this.tabContainer.openAnimationFinished()`
- 条件付き依存: `if (UserInteraction.running("browser.tabs.opening", this.documentGlobal))` → `UserInteraction.finish()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Tabbrowser.#closeTimeAnimTimerIds.set()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Glean.browserTabclose.timeAnim.start()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Tabbrowser.#closeTimeNoAnimTimerIds.set()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Glean.browserTabclose.timeNoAnim.start()`
- 条件付き依存: `if (!animate && aTab.closing)` → `this._endRemoveTab()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Glean.browserTabclose.timeAnim.cancel()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeAnimTimerIds.get()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeAnimTimerIds.delete()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Glean.browserTabclose.timeNoAnim.cancel()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeNoAnimTimerIds.get()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeNoAnimTimerIds.delete()`
- 条件付き依存: `if (lockTabSizing)` → `this.tabContainer._lockTabSizing()`
- 条件付き依存: `if (!(lockTabSizing))` → `this.tabContainer._unlockTabSizing()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `Glean.browserTabclose.timeAnim.cancel()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `Tabbrowser.#closeTimeAnimTimerIds.get()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `Tabbrowser.#closeTimeAnimTimerIds.delete()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `this._endRemoveTab()`
- 条件付き依存: `if ( tab.container && tabbrowser.documentGlobal.getComputedStyle(tab).maxWidth == "0.1px" )` → `console.assert()`
- 条件付き依存: `if ( tab.container && tabbrowser.documentGlobal.getComputedStyle(tab).maxWidth == "0.1px" )` → `tabbrowser._endRemoveTab()`
- XPCOM: `Services.prefs`

## Tabbrowser.#shouldCloseWindowWithLastTab()
- 位置: L6619-6624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## Tabbrowser.#isLastTabInWindow()
- 位置: L6636-6643
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#hasBeforeUnload()
- 位置: L6645-6651
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#beginRemoveTab()
- 位置: L6686-6911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#endRemoveArgs.set()`, `Tabbrowser.#hasBeforeUnload()`, `Tabbrowser.#tabsPendingPermitUnload.has()`, `aTab._mouseleave()`, `aTab.dispatchEvent()`, `aTab.hasAttribute()`, `browser.removeAttribute()`, `notificationBox?._stack?.remove()`, `this.#isLastTabInWindow()`, `this._removingTabs.add()`, `this._tabLayerCache.indexOf()`, `this.getBrowserForTab()`, `this.getSuccessor()`, `this.readNotificationBox()`, `this.recordTabMetrics()`, `this.replaceInSuccession()`, `this.setSuccessor()`, `this.tabContainer._invalidateCachedTabs()`, `this.tabContainer._invalidateCachedVisibleTabs()`, `this.tabContainer.cancelTabOpening()`, `this.tabContainer.matches()`
- 条件付き依存: `if (!prewarmed)` → `this._findTabToBlurTo()`
- 条件付き依存: `if (blurTab)` → `this.warmupTab()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Glean.browserTabclose.permitUnloadTime.start()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Tabbrowser.#tabsPendingPermitUnload.add()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `browser.permitUnload()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Tabbrowser.#tabsPendingPermitUnload.delete()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Glean.browserTabclose.permitUnloadTime.stopAndAccumulate()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this._tabLayerCache.splice()`
- 条件付き依存: `if (!screenShareInActiveTab)` → `this.#blurTab()`
- 条件付き依存: `if (closeWindow && closeWindowFastpath && !this._removingTabs.size)` → `this.documentGlobal.closeWindow()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabFilters.get()`
- 条件付き依存: `if (aTab.linkedPanel)` → `browser.webProgress.removeProgressListener()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabListeners.get()`
- 条件付き依存: `if (aTab.linkedPanel)` → `filter.removeProgressListener()`
- 条件付き依存: `if (aTab.linkedPanel)` → `listener.destroy()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabListeners.delete()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabFilters.delete()`
- 条件付き依存: `if (!adoptedByTab && aTab.hasAttribute("soundplaying"))` → `aTab.linkedBrowser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (handOverHover)` → `this.#tabTakingPlaceOf(aTab)?._mouseenter()`
- 条件付き依存: `if (handOverHover)` → `this.#tabTakingPlaceOf()`
- 条件付き依存: `if (newTab)` → `this.addTrustedTab()`
- 条件付き依存: `if (!(newTab))` → `this.documentGlobal.TabBarVisibility.update()`
- 条件付き依存: `if (!adoptedByTab && !this.documentGlobal.gMultiProcessBrowser)` → `browser.contentWindow.windowUtils.disableDialogs()`
- 条件付き依存: `if (browser.registeredOpenURI && !adoptedByTab)` → `browser.getAttribute()`
- 条件付き依存: `if (browser.registeredOpenURI && !adoptedByTab)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (browser.registeredOpenURI && !adoptedByTab)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`

## Tabbrowser.#tabTakingPlaceOf()
- 位置: L6919-6928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`, `closingTab.compareDocumentPosition()`, `this.tabContainer.ariaFocusableItems.find()`

## Tabbrowser._endRemoveTab()
- 位置: L6930-7058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#closeTimeAnimTimerIds.get()`, `Tabbrowser.#closeTimeNoAnimTimerIds.get()`, `Tabbrowser.#endRemoveArgs.delete()`, `Tabbrowser.#endRemoveArgs.get()`, `Tabbrowser.#tabFilters.delete()`, `Tabbrowser.#tabListeners.delete()`, `aTab.remove()`, `browser.remove()`, `panel.remove()`, `this.#blurTab()`, `this.#tabForBrowser.delete()`, `this._removingTabs.delete()`, `this.getBrowserForTab()`, `this.getPanel()`, `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (aCloseWindow)` → `this._endRemoveTab()`
- 条件付き依存: `if (aNewTab)` → `this.documentGlobal.gURLBar.select()`
- 条件付き依存: `if (aTab.linkedPanel)` → `browser.destroy()`
- 条件付き依存: `if (!this.#windowIsClosing)` → `this.tabContainer._updateCloseButtons()`
- 条件付き依存: `if (!this.#windowIsClosing)` → `this.documentGlobal.setTimeout()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.onTabRemoved()`
- 条件付き依存: `if (Tabbrowser.#closeTimeAnimTimerIds.get(aTab))` → `Glean.browserTabclose.timeAnim.stopAndAccumulate()`
- 条件付き依存: `if (Tabbrowser.#closeTimeAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeAnimTimerIds.get()`
- 条件付き依存: `if (Tabbrowser.#closeTimeAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeAnimTimerIds.delete()`
- 条件付き依存: `if (Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab))` → `Glean.browserTabclose.timeNoAnim.stopAndAccumulate()`
- 条件付き依存: `if (Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeNoAnimTimerIds.get()`
- 条件付き依存: `if (Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeNoAnimTimerIds.delete()`
- 条件付き依存: `if (aCloseWindow)` → `this.documentGlobal.closeWindow()`

## Tabbrowser.closeTabsByURI()
- 位置: async L7068-7109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `uriToClose.equals()`, `urisToClose.findIndex()`
- 条件付き依存: `if (matchedIndex > -1)` → `tabsToRemove.push()`
- 条件付き依存: `if (tabsToRemove.length)` → `this.#startRemoveTabs()`
- 条件付き依存: `if (lastToClose)` → `this.removeTab()`

## Tabbrowser.explicitUnloadTabs()
- 位置: async L7111-7180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserEngagement.tabExplicitUnload.record()`, `Math.floor()`, `Promise.all()`, `getTotalMemoryUsage()`, `tabs.map()`, `tabs.some()`, `this.discardBrowser()`, `this.documentGlobal.performance.now()`, `this.prepareDiscardBrowser()`, `this.runBeforeUnloadForTabs()`
- 条件付き依存: `if (tabs.some(tab => tab.selected || tab.splitview?.hasActiveTab))` → `tabs.concat()`
- 条件付き依存: `if (tabs.some(tab => tab.selected || tab.splitview?.hasActiveTab))` → `this.tabContainer.allTabs.filter()`
- 条件付き依存: `if (tab.splitview)` → `tabsToExclude.push()`
- 条件付き依存: `if (tab.splitview)` → `tab.splitview.tabs.filter()`
- 条件付き依存: `if (tabs.some(tab => tab.selected || tab.splitview?.hasActiveTab))` → `this._findTabToBlurTo()`
- 条件付き依存: `if (!(newTab))` → `this.documentGlobal.FirefoxViewHandler.button?.checkVisibility()`
- 条件付き依存: `if (firefoxViewAvailable)` → `this.documentGlobal.FirefoxViewHandler.openTab()`
- 条件付き依存: `if (!(firefoxViewAvailable))` → `this.addTrustedTab()`

## Tabbrowser.handleNewTabMiddleClick()
- 位置: L7190-7206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.hasAttribute()`
- 条件付き依存: `if (event.button == 1)` → `this.documentGlobal.BrowserCommands.openTab()`
- 条件付き依存: `if (event.button == 1)` → `event.stopPropagation()`
- 条件付き依存: `if (event.button == 1)` → `event.preventDefault()`

## Tabbrowser._findTabToBlurTo()
- 位置: L7217-7305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.filter.call()`, `Services.prefs.getBoolPref()`, `excludeTabs.has()`, `new Set(this.tabsInCollapsedTabGroups).difference()`, `tab.hasAttribute()`, `this.getSuccessor()`, `this.tabContainer.findNextTab()`
- 条件付き依存: `if (this.documentGlobal.FirefoxViewHandler.tab)` → `aExcludeTabs.push()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.selectMRUOnClose", false))` → `remainingTabs .filter(t => t !== aTab) .reduce()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.selectMRUOnClose", false))` → `remainingTabs .filter()`
- 条件付き依存: `if (!tab)` → `this.tabContainer.findNextTab()`
- XPCOM: `Services.prefs`

## filter()
- 位置: L7272-7272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `remainingTabs.includes()`

## filter()
- 位置: L7278-7278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `remainingTabs.includes()`

## filter()
- 位置: L7294-7294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eligibleTabs.has()`

## filter()
- 位置: L7300-7300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eligibleTabs.has()`

## Tabbrowser.#blurTab()
- 位置: L7307-7309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._findTabToBlurTo()`

## Tabbrowser.swapBrowsersAndCloseOther()
- 位置: L7321-7549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#endRemoveArgs.get()`, `Tabbrowser.#findBars.get()`, `Tabbrowser.#originalRegisteredOpenURIs.set()`, `Tabbrowser.#tabListeners.get()`, `aOtherTab.hasAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SitePermissions.copyTemporaryPermissions()`, `otherBrowser.hasAttribute()`, `remoteBrowser.#beginRemoveTab()`, `this.getBrowserForTab()`, `this.setTabTitle()`
- 条件付き依存: `if (otherBrowser.hasAttribute("usercontextid"))` → `ourBrowser.setAttribute()`
- 条件付き依存: `if (otherBrowser.hasAttribute("usercontextid"))` → `otherBrowser.getAttribute()`
- 条件付き依存: `if (aOtherTab._soundPlayingAttrRemovalTimer)` → `aOtherTab.documentGlobal.clearTimeout()`
- 条件付き依存: `if (aOtherTab._soundPlayingAttrRemovalTimer)` → `aOtherTab.removeAttribute()`
- 条件付き依存: `if (aOtherTab._soundPlayingAttrRemovalTimer)` → `remoteBrowser._tabAttrModified()`
- 条件付き依存: `if (closeWindow)` → `win.windowUtils.suppressAnimation()`
- 条件付き依存: `if (closeWindow)` → `win.docShell.treeOwner.QueryInterface()`
- 条件付き依存: `if (aOtherTab.hasAttribute("muted"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOurTab.linkedPanel)` → `ourBrowser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("muted"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("discarded"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("discarded"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("undiscardable"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("undiscardable"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("soundplaying"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("soundplaying"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("usercontextid"))` → `aOurTab.setUserContextId()`
- 条件付き依存: `if (aOtherTab.hasAttribute("usercontextid"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `aOurTab.setAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `aOtherTab.getAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `lazy.webrtcUI.swapBrowserForNotification()`
- 条件付き依存: `if (aOtherTab.hasAttribute("pictureinpicture"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("pictureinpicture"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("pictureinpicture"))` → `aOtherTab.dispatchEvent()`
- 条件付き依存: `if (isPending)` → `lazy.SessionStore.setTabState()`
- 条件付き依存: `if (isPending)` → `lazy.SessionStore.getTabState()`
- 条件付き依存: `if (isPending)` → `Tabbrowser.#swapRegisteredOpenURIs()`
- 条件付き依存: `if (!ourBrowser.mIconURL && otherBrowser.mIconURL)` → `this.setIcon()`
- 条件付き依存: `if (!(isPending))` → `aOtherTab.hasAttribute()`
- 条件付き依存: `if (isBusy)` → `aOurTab.setAttribute()`
- 条件付き依存: `if (isBusy)` → `modifiedAttrs.push()`
- 条件付き依存: `if (!(isPending))` → `this.#swapBrowserDocShells()`
- 条件付き依存: `if (otherBrowser.registeredOpenURI)` → `otherBrowser.getAttribute()`
- 条件付き依存: `if (otherBrowser.registeredOpenURI)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (otherBrowser.registeredOpenURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (otherFindBar && otherFindBar.findMode == otherFindBar.FIND_NORMAL)` → `this.getFindBar()`
- 条件付き依存: `if (otherFindBar && otherFindBar.findMode == otherFindBar.FIND_NORMAL)` → `ourFindBarPromise.then()`
- 条件付き依存: `if (!wasHidden)` → `ourFindBar.onFindCommand()`
- 条件付き依存: `if (closeWindow)` → `aOtherTab.documentGlobal.close()`
- 条件付き依存: `if (!(closeWindow))` → `remoteBrowser._endRemoveTab()`
- 条件付き依存: `if (aOurTab.selected)` → `this.updateCurrentBrowser()`
- 条件付き依存: `if (modifiedAttrs.length)` → `this._tabAttrModified()`
- XPCOM: `nsIBaseWindow`

## Tabbrowser.swapBrowsers()
- 位置: L7551-7575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Tabbrowser.#tabListeners.set()`, `filter.addProgressListener()`, `filter.removeProgressListener()`, `otherBrowser.webProgress.addProgressListener()`, `otherBrowser.webProgress.removeProgressListener()`, `this.#swapBrowserDocShells()`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## Tabbrowser.#swapBrowserDocShells()
- 位置: L7577-7636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#swapRegisteredOpenURIs()`, `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Tabbrowser.#tabListeners.set()`, `aOtherBrowser.ownerDocument.getElementById()`, `aOurTab.registerAudibleChangeHandler()`, `filter.addProgressListener()`, `filter.removeProgressListener()`, `ourBrowser.ownerDocument.getElementById()`, `ourBrowser.swapDocShells()`, `ourBrowser.webProgress.addProgressListener()`, `ourBrowser.webProgress.removeProgressListener()`, `this.#insertBrowser()`, `this.getBrowserForTab()`
- 条件付き依存: `if (!this._switcher)` → `this.shouldActivateDocShell()`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## Tabbrowser.#swapRegisteredOpenURIs()
- 位置: L7638-7649
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.reloadMultiSelectedTabs()
- 位置: L7651-7653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.reloadTabs()`

## Tabbrowser.reloadTabs()
- 位置: L7655-7663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserForTab()`, `this.getBrowserForTab(tab).reload()`

## Tabbrowser.reloadTab()
- 位置: L7665-7675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.reload()`, `lazy.SitePermissions.clearTemporaryBlockPermissions()`, `this.documentGlobal.gIdentityHandler.hidePopup()`, `this.documentGlobal.gPermissionPanel.hidePopup()`, `this.getBrowserForTab()`

## Tabbrowser.addProgressListener()
- 位置: L7688-7700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#progressListeners.push()`
- 条件付き依存: `if (arguments.length != 1)` → `console.error()`

## Tabbrowser.removeProgressListener()
- 位置: L7708-7712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#progressListeners.filter()`

## Tabbrowser.addTabsProgressListener()
- 位置: L7723-7725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabsProgressListeners.push()`

## Tabbrowser.removeTabsProgressListener()
- 位置: L7733-7737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabsProgressListeners.filter()`

## Tabbrowser.getBrowserForTab()
- 位置: L7739-7741
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.showTab()
- 位置: L7743-7771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.dispatchEvent()`, `aTab.removeAttribute()`, `event.initEvent()`, `lazy.SessionStore.deleteCustomTabValue()`, `this.document.createEvent()`, `this.tabContainer._invalidateCachedVisibleTabs()`, `this.tabContainer._updateCloseButtons()`
- 条件付き依存: `if (aTab.multiselected)` → `this.#updateMultiselectedTabCloseButtonTooltip()`
- 条件付き依存: `if (sibling != aTab)` → `this.showTab()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.toggleAttribute()`

## Tabbrowser.hideTab()
- 位置: L7773-7820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.dispatchEvent()`, `aTab.setAttribute()`, `event.initEvent()`, `this.document.createEvent()`, `this.getSuccessor()`, `this.replaceInSuccession()`, `this.setSuccessor()`, `this.tabContainer._invalidateCachedVisibleTabs()`, `this.tabContainer._updateCloseButtons()`
- 条件付き依存: `if (aTab.multiselected)` → `this.#updateMultiselectedTabCloseButtonTooltip()`
- 条件付き依存: `if (aSource)` → `lazy.SessionStore.setCustomTabValue()`
- 条件付き依存: `if (sibling != aTab)` → `this.hideTab()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.toggleAttribute()`

## Tabbrowser.selectTabAtIndex()
- 位置: L7834-7855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setSelectedTab()`
- 条件付き依存: `if (event)` → `event.preventDefault()`
- 条件付き依存: `if (event)` → `event.stopPropagation()`

## Tabbrowser.replaceTabWithWindow()
- 位置: L7867-7896
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Object.entries()`, `Object.entries(features) .map()`, `Object.entries(features) .map(([key, value]) => `${key}=${value}`) .join()`, `Tabbrowser.isTab()`, `args.appendElement()`, `lazy.BrowserWindowTracker.openWindow()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (this.tabs.length == 1)` → `this.addTrustedTab()`
- 条件付き依存: `if (!this.documentGlobal.gReduceMotion && Tabbrowser.isTab(aTab))` → `aTab.removeAttribute()`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1`

## Tabbrowser.replaceTabsWithWindow()
- 位置: L7908-7992
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTabGroupLabel()`, `elements.includes()`, `this.recordTabMetrics()`, `this.replaceTabWithWindow()`, `win.addEventListener()`, `win.gBrowser.addRangeToMultiSelectedTabs()`, `win.gBrowser.lockClearMultiSelectionOnce()`
- 条件付き依存: `if (Tabbrowser.isTabGroupLabel(contextTab))` → `this.replaceTabWithWindow()`
- 条件付き依存: `if (elements.length == 1)` → `this.replaceTabWithWindow()`
- 条件付き依存: `if (!this.documentGlobal.gReduceMotion)` → `element.removeAttribute()`
- 条件付き依存: `if ( !elements.includes(selectedTab) && !elements.includes(selectedTab.splitview) )` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (element !== selectedTab && element !== selectedTab.splitview)` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (element !== selectedTab && element !== selectedTab.splitview)` → `win.gBrowser.adoptSplitView()`
- 条件付き依存: `if (element !== selectedTab && element !== selectedTab.splitview)` → `win.gBrowser.adoptTab()`
- 条件付き依存: `if (!newTab)` → `element.setAttribute()`

## Tabbrowser.replaceGroupWithWindow()
- 位置: L8003-8010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordTabMetrics()`, `this.replaceTabWithWindow()`

## Tabbrowser.isTab()
- 位置: L8018-8020
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.isTabGroup()
- 位置: L8028-8030
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.isTabGroupLabel()
- 位置: L8038-8040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element?.classList?.contains()`

## Tabbrowser.isSplitViewWrapper()
- 位置: L8048-8050
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#updateTabsAfterInsert()
- 位置: L8052-8074
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.moveTabTo()
- 位置: L8094-8171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`, `Tabbrowser.isTabGroup()`, `Tabbrowser.isTabGroupLabel()`, `this.#handleTabMove()`
- 条件付き依存: `if (typeof elementIndex == "number")` → `this.#elementIndexToTabIndex()`
- 条件付き依存: `if (Tabbrowser.isTab(element) && element.pinned)` → `Math.min()`
- 条件付き依存: `if (!(Tabbrowser.isTab(element) && element.pinned))` → `Math.max()`
- 条件付き依存: `if (movingForwards)` → `Math.min()`
- 条件付き依存: `if (movingForwards && neighbor)` → `neighbor.after()`
- 条件付き依存: `if (!(movingForwards && neighbor))` → `this.tabContainer.insertBefore()`

## Tabbrowser.moveTabBefore()
- 位置: L8181-8183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveTabNextTo()`

## Tabbrowser.moveTabsBefore()
- 位置: L8192-8194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveTabsNextTo()`

## Tabbrowser.moveTabAfter()
- 位置: L8204-8206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveTabNextTo()`

## Tabbrowser.moveTabsAfter()
- 位置: L8215-8217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveTabsNextTo()`

## Tabbrowser.#moveTabNextTo()
- 位置: L8230-8298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTabGroupLabel()`, `this.#handleTabMove()`
- 条件付き依存: `if (moveBefore)` → `getContainer().insertBefore()`
- 条件付き依存: `if (moveBefore)` → `getContainer()`
- 条件付き依存: `if (targetElement)` → `targetElement.after()`
- 条件付き依存: `if (!(targetElement))` → `getContainer().appendChild()`
- 条件付き依存: `if (!(targetElement))` → `getContainer()`

## getContainer()
- 位置: L8280-8283
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#moveTabsNextTo()
- 位置: L8308-8326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveTabNextTo()`, `this.TabMetrics.decomposedContext()`, `this.recordTabMetrics()`

## Tabbrowser.moveTabToSplitView()
- 位置: L8334-8358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`, `aSplitViewWrapper.appendChild()`, `aSplitViewWrapper.insertBefore()`, `this.#handleTabMove()`, `this.removeFromMultiSelectedTabs()`, `this.tabContainer._notifyBackgroundTab()`

## Tabbrowser.moveTabToExistingGroup()
- 位置: L8368-8396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`
- 条件付き依存: `if (aTab.splitview)` → `this.#handleTabMove()`
- 条件付き依存: `if (aTab.splitview)` → `aGroup.appendChild()`
- 条件付き依存: `if (aTab.splitview)` → `this.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (aTab.splitview)` → `this.tabContainer._notifyBackgroundTab()`
- 条件付き依存: `if (!(aTab.splitview))` → `this.#handleTabMove()`
- 条件付き依存: `if (!(aTab.splitview))` → `aGroup.appendChild()`
- 条件付き依存: `if (!(aTab.splitview))` → `this.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (!(aTab.splitview))` → `this.tabContainer._notifyBackgroundTab()`

## Tabbrowser.moveSplitViewToExistingGroup()
- 位置: L8406-8426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `aGroup.appendChild()`, `this.#handleTabMove()`, `this.removeFromMultiSelectedTabs()`, `this.tabContainer._notifyBackgroundTab()`

## Tabbrowser.#getTabMoveState()
- 位置: L8445-8463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`

## Tabbrowser.#notifyOnTabMove()
- 位置: L8473-8510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `tab.dispatchEvent()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `Tabbrowser.#tabsLeavingAdoptedSplitView.has()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `Tabbrowser.#tabsJoiningAdoptedSplitView.has()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `this.recordTabMetrics()`

## Tabbrowser.handleTabMove()
- 位置: L8519-8521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleTabMove()`

## Tabbrowser.#handleTabMove()
- 位置: L8530-8597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`, `Tabbrowser.isTabGroup()`, `moveActionCallback()`, `tabs.map()`, `this.#getTabMoveState()`, `this.#notifyOnTabMove()`, `this.#updateTabsAfterInsert()`, `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (!( Tabbrowser.isTab(element) && element.splitview?.shouldMoveAllTabsAtOnce ))` → `Tabbrowser.isTab()`
- 条件付き依存: `if (!(Tabbrowser.isTab(element)))` → `Tabbrowser.isTabGroup()`
- 条件付き依存: `if (!(Tabbrowser.isTab(element)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (wasFocused)` → `this.selectedTab.focus()`
- 条件付き依存: `if (tab.selected)` → `this.tabContainer._handleTabSelect()`
- 条件付き依存: `if ( Tabbrowser.isTabGroup(element) && previousTabStates[0].tabIndex != currentFirst.tabIndex )` → `element.dispatchEvent()`

## Tabbrowser.adoptTab()
- 位置: L8615-8676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTab()`, `aTab.container.tabDragAndDrop.finishAnimateTabMove()`, `aTab.hasAttribute()`, `this.addWebTab()`, `this.swapBrowsersAndCloseOther()`
- 条件付き依存: `if (typeof elementIndex == "number")` → `this.tabContainer.dragAndDropElements.at()`
- 条件付き依存: `if (!(typeof elementIndex == "number"))` → `this.tabs.at()`
- 条件付き依存: `if (aTab.hasAttribute("usercontextid"))` → `aTab.getAttribute()`
- 条件付き依存: `if (!this.swapBrowsersAndCloseOther(newTab, aTab))` → `this.removeTab()`
- 条件付き依存: `if (tabInGroup)` → `Glean.tabgroup.tabInteractions.remove_other_window.add()`

## Tabbrowser.moveTabForward()
- 位置: L8687-8727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabContainer.findNextTab()`
- 条件付き依存: `if (nextTab)` → `this.#handleTabMove()`
- 条件付き依存: `if (nextTabOrSplitview.group.collapsed)` → `nextTabOrSplitview.group.after()`
- 条件付き依存: `if (!(nextTabOrSplitview.group.collapsed))` → `nextTabOrSplitview.group.insertBefore()`
- 条件付き依存: `if (selectedTab.group != nextTab.group)` → `selectedTab.group.after()`
- 条件付き依存: `if (!(selectedTab.group != nextTab.group))` → `nextTabOrSplitview.after()`
- 条件付き依存: `if (selectedTab.group)` → `selectedTab.group.after()`

## filter()
- 位置: L8694-8694
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.moveTabBackward()
- 位置: L8738-8775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabContainer.findNextTab()`
- 条件付き依存: `if (previousTab)` → `this.#handleTabMove()`
- 条件付き依存: `if (previousTab.group.collapsed)` → `previousTab.group.before()`
- 条件付き依存: `if (!(previousTab.group.collapsed))` → `previousTab.group.append()`
- 条件付き依存: `if (selectedTab.group != previousTab.group)` → `selectedTab.group.before()`
- 条件付き依存: `if (!(selectedTab.group != previousTab.group))` → `previousTabOrSplitview.before()`
- 条件付き依存: `if (selectedTab.group)` → `selectedTab.group.before()`

## filter()
- 位置: L8745-8745
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.moveTabToStart()
- 位置: L8787-8793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.moveTabTo()`

## Tabbrowser.moveTabToEnd()
- 位置: L8805-8811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.moveTabTo()`

## Tabbrowser.duplicateTab()
- 位置: L8823-8835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.duplicateTab()`
- 条件付き依存: `if (aTab.group)` → `Glean.tabgroup.tabInteractions.duplicate.add()`

## Tabbrowser.#updateMultiselectedTabCloseButtonTooltip()
- 位置: L8846-8862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTabsRemovedFromMultiselection?.forEach()`, `selectedTab.querySelector()`, `selectedTabs.forEach()`, `this.document.l10n.setArgs()`, `unselectedTab.querySelector()`

## Tabbrowser.addToMultiSelectedTabs()
- 位置: L8872-8896
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `aTab.setAttribute()`, `this.#multiSelectChangeRemovals.delete()`, `this.#multiSelectedTabsSet.add()`, `this.#startMultiSelectChange()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(aTab))` → `this.addToMultiSelectedTabs()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.setAttribute()`
- 条件付き依存: `if (!this.#multiSelectChangeRemovals.delete(aTab))` → `this.#multiSelectChangeAdditions.add()`

## Tabbrowser.addRangeToMultiSelectedTabs()
- 位置: L8904-8921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `tabs.indexOf()`, `this.addToMultiSelectedTabs()`

## Tabbrowser.removeFromMultiSelectedTabs()
- 位置: L8931-8948
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.removeAttribute()`, `this.#multiSelectChangeAdditions.delete()`, `this.#multiSelectedTabsSet.delete()`, `this.#startMultiSelectChange()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.removeAttribute()`
- 条件付き依存: `if (!this.#multiSelectChangeAdditions.delete(aTab))` → `this.#multiSelectChangeRemovals.add()`

## Tabbrowser.clearMultiSelectedTabs()
- 位置: L8950-8967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeFromMultiSelectedTabs()`

## Tabbrowser.selectAllTabs()
- 位置: L8969-8975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addRangeToMultiSelectedTabs()`

## Tabbrowser.allTabsSelected()
- 位置: L8977-8982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.visibleTabs.every()`

## Tabbrowser.lockClearMultiSelectionOnce()
- 位置: L8984-8987
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.unlockClearMultiSelection()
- 位置: L8989-8992
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#avoidSingleSelectedTab()
- 位置: L9020-9024
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.multiSelectedTabsCount == 1)` → `this.clearMultiSelectedTabs()`

## Tabbrowser.#switchToNextMultiSelectedTab()
- 位置: L9026-9045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`
- 条件付き依存: `if (!(!lastMultiSelectedTab.selected))` → `ChromeUtils.nondeterministicGetWeakSetKeys( this.#multiSelectedTabsSet ).filter()`
- 条件付き依存: `if (!(!lastMultiSelectedTab.selected))` → `ChromeUtils.nondeterministicGetWeakSetKeys()`
- 条件付き依存: `if (!(!lastMultiSelectedTab.selected))` → `selectedTabs.at()`

## Tabbrowser.selectedTabs()
- 位置: L9047-9055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearMultiSelectedTabs()`
- 条件付き依存: `if (tabs.length > 1)` → `this.addToMultiSelectedTabs()`

## Tabbrowser.selectedTabs()
- 位置: L9057-9070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `ChromeUtils.nondeterministicGetWeakSetKeys( this.#multiSelectedTabsSet ).filter()`, `Tabbrowser.#mayTabBeMultiselected()`, `tabs.sort()`, `this.#multiSelectedTabsSet.has()`
- 条件付き依存: `if ( (!this.#multiSelectedTabsSet.has(selectedTab) && Tabbrowser.#mayTabBeMultiselected(selectedTab)) || !tabs.length )` → `tabs.push()`

## Tabbrowser.selectedElements()
- 位置: L9080-9086
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `selectedElements.add()`, `selectedElements.values()`

## Tabbrowser.multiSelectedTabsCount()
- 位置: L9088-9092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `ChromeUtils.nondeterministicGetWeakSetKeys( this.#multiSelectedTabsSet ).filter()`

## Tabbrowser.lastMultiSelectedTab()
- 位置: L9094-9104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lastMultiSelectedTabRef.get()`, `this.#multiSelectedTabsSet.has()`

## Tabbrowser.lastMultiSelectedTab()
- 位置: L9106-9108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`

## Tabbrowser.#mayTabBeMultiselected()
- 位置: L9110-9112
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.#startMultiSelectChange()
- 位置: L9114-9119
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#multiSelectChangeStarted)` → `Promise.resolve().then()`
- 条件付き依存: `if (!this.#multiSelectChangeStarted)` → `Promise.resolve()`
- 条件付き依存: `if (!this.#multiSelectChangeStarted)` → `this.#endMultiSelectChange()`

## Tabbrowser.#endMultiSelectChange()
- 位置: L9121-9153
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!selectedTab.multiselected)` → `this.addToMultiSelectedTabs()`
- 条件付き依存: `if (this.#multiSelectChangeRemovals.size)` → `this.#multiSelectChangeRemovals.has()`
- 条件付き依存: `if (this.#multiSelectChangeRemovals.has(selectedTab))` → `this.#switchToNextMultiSelectedTab()`
- 条件付き依存: `if (this.#multiSelectChangeRemovals.size)` → `this.#avoidSingleSelectedTab()`
- 条件付き依存: `if (noticeable)` → `this.#updateMultiselectedTabCloseButtonTooltip()`
- 条件付き依存: `if (noticeable || this.#multiSelectChangeSelected)` → `this.#multiSelectChangeAdditions.clear()`
- 条件付き依存: `if (noticeable || this.#multiSelectChangeSelected)` → `this.#multiSelectChangeRemovals.clear()`
- 条件付き依存: `if (noticeable || this.#multiSelectChangeSelected)` → `this.tabContainer.dispatchEvent()`

## Tabbrowser.toggleMuteAudioOnMultiSelectedTabs()
- 位置: L9155-9163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.toggleMuteAudio()`, `this.selectedTabs.filter()`

## Tabbrowser.resumeDelayedMediaOnMultiSelectedTabs()
- 位置: L9165-9169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.resumeDelayedMedia()`

## Tabbrowser.pinMultiSelectedTabs()
- 位置: L9179-9191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.pinTab()`, `this.recordTabMetrics()`

## Tabbrowser.unpinMultiSelectedTabs()
- 位置: L9200-9213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.recordTabMetrics()`, `this.unpinTab()`

## Tabbrowser.activateBrowserForPrintPreview()
- 位置: L9215-9221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._printPreviewBrowsers.add()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.activateBrowserForPrintPreview()`

## Tabbrowser.deactivatePrintPreviewBrowsers()
- 位置: L9223-9229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shouldActivateDocShell()`

## Tabbrowser.shouldActivateDocShell()
- 位置: L9236-9246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PictureInPicture.isOriginatingBrowser()`, `this._printPreviewBrowsers.has()`, `this.splitViewBrowsers.includes()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.shouldActivateDocShell()`

## Tabbrowser._getSwitcher()
- 位置: L9248-9253
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.warmupTab()
- 位置: L9255-9259
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher().warmupTab()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher()`

## Tabbrowser.#maybeRequestReplyFromRemoteContent()
- 位置: L9269-9287
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !aEvent.isReplyEventFromRemoteContent && /** @type {MozBrowser} */ (aEvent.target)?.isRemoteBrowser === true )` → `aEvent.requestReplyFromRemoteContent()`

## Tabbrowser.on_keydown()
- 位置: L9289-9353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#maybeRequestReplyFromRemoteContent()`, `aEvent.preventDefault()`, `lazy.KeyboardLockUtils.mustWaitForKeyboardLockRequestedReply()`, `lazy.ShortcutUtils.getSystemActionForEvent()`, `this.TabMetrics.userTriggeredContext()`, `this.moveTabBackward()`, `this.moveTabForward()`
- 条件付き依存: `if (this.multiSelectedTabsCount)` → `this.removeMultiSelectedTabs()`
- 条件付き依存: `if (this.multiSelectedTabsCount)` → `this.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!this.selectedTab.pinned)` → `this.removeCurrentTab()`
- 条件付き依存: `if (!this.selectedTab.pinned)` → `this.TabMetrics.userTriggeredContext()`

## Tabbrowser.#toggleCaretBrowsing()
- 位置: L9355-9420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- 条件付き依存: `if (warn && !browseWithCaretOn)` → `this.tabLocalization.formatValuesSync()`
- 条件付き依存: `if (warn && !browseWithCaretOn)` → `promptService.confirmEx()`
- 条件付き依存: `if (checkValue.value)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs` / `Services.prompt`

## Tabbrowser.on_keypress()
- 位置: L9422-9470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#maybeRequestReplyFromRemoteContent()`, `lazy.ShortcutUtils.getSystemActionForEvent()`, `this.#toggleCaretBrowsing()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.tabContainer.advanceSelectedTab()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `aEvent.preventDefault()`

## Tabbrowser.on_framefocusrequested()
- 位置: L9472-9482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.preventDefault()`, `this.documentGlobal.focus()`, `this.getTabForBrowser()`

## Tabbrowser.on_visibilitychange()
- 位置: L9484-9492
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._switcher)` → `browser.preserveLayers()`

## Tabbrowser.on_TabGroupCollapse()
- 位置: L9494-9498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.tabs.forEach()`, `this.removeFromMultiSelectedTabs()`

## Tabbrowser.on_TabGroupCreateByUser()
- 位置: L9500-9502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabGroupMenu.openCreateModal()`

## Tabbrowser.on_TabGrouped()
- 位置: L9504-9523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#originalRegisteredOpenURIs.get()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (uri)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`

## Tabbrowser.on_TabUngrouped()
- 位置: L9525-9547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#originalRegisteredOpenURIs.get()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (uri)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`

## Tabbrowser.on_TabSplitViewActivate()
- 位置: L9549-9552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveSplitViewNotificationBoxes()`

## Tabbrowser.on_TabSplitViewDeactivate()
- 位置: L9554-9559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveSplitViewNotificationBoxes()`

## Tabbrowser.#moveSplitViewNotificationBoxes()
- 位置: L9567-9574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.readNotificationBox()`
- 条件付き依存: `if (notificationBox?._stack)` → `this.#insertNotificationBox()`

## Tabbrowser.on_activate()
- 位置: L9576-9578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedTab.updateLastSeenActive()`

## Tabbrowser.on_deactivate()
- 位置: L9580-9582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selectedTab.updateLastSeenActive()`

## Tabbrowser.on_change()
- 位置: L9584-9587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeRefreshIcons()`

## Tabbrowser.#isFirstOrLastInTabGroup()
- 位置: L9593-9601
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tab.group)` → `groupTabs.at()`

## Tabbrowser.getTabPids()
- 位置: L9603-9615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `framePids.sort()`, `lazy.E10SUtils.getBrowserPids()`, `pids.concat()`

## Tabbrowser.getTabTooltip()
- 位置: L9626-9698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#isFirstOrLastInTabGroup()`, `labelArray.join()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (includeLabel)` → `labelArray.push()`
- 条件付き依存: `if (includeLabel)` → `Tabbrowser.#fullLabels.get()`
- 条件付き依存: `if (includeLabel)` → `tab.getAttribute()`
- 条件付き依存: `if (Tabbrowser.prefs.showPidAndActiveness)` → `this.getTabPids()`
- 条件付き依存: `if (pids.length)` → `debugStringArray.push()`
- 条件付き依存: `if (pids.length)` → `pids.join()`
- 条件付き依存: `if (tab.linkedBrowser.docShellIsActive)` → `debugStringArray.push()`
- 条件付き依存: `if (Tabbrowser.prefs.showPidAndActiveness)` → `lazy.SponsorProtection.isProtectedBrowser()`
- 条件付き依存: `if (lazy.SponsorProtection.isProtectedBrowser(tab.linkedBrowser))` → `debugStringArray.push()`
- 条件付き依存: `if (debugStringArray.length)` → `labelArray.push()`
- 条件付き依存: `if (debugStringArray.length)` → `debugStringArray.join()`
- 条件付き依存: `if (containerName && tabGroupName)` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (tabGroupName)` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (!(tabGroupName))` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (containerName || tabGroupName)` → `labelArray.push()`
- 条件付き依存: `if (tab.soundPlaying)` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (tab.soundPlaying)` → `labelArray.push()`

## Tabbrowser.createTooltip()
- 位置: L9700-9747
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `event.target.triggerNode?.closest()`, `this.selectedTabs.includes()`, `tooltip.removeAttribute()`
- 条件付き依存: `if (!tab)` → `event.target.triggerNode?.getRootNode()?.host?.closest()`
- 条件付き依存: `if (!tab)` → `event.target.triggerNode?.getRootNode()`
- 条件付き依存: `if (event.target.triggerNode?.getRootNode()?.host?.closest("tab"))` → `event.target.triggerNode?.getRootNode().host.closest()`
- 条件付き依存: `if (event.target.triggerNode?.getRootNode()?.host?.closest("tab"))` → `event.target.triggerNode?.getRootNode()`
- 条件付き依存: `if (!(event.target.triggerNode?.getRootNode()?.host?.closest("tab")))` → `event.preventDefault()`
- 条件付き依存: `if (tab.selected)` → `this.document.getElementById()`
- 条件付き依存: `if (tab.selected)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (!(tab.selected))` → `tab.hasAttribute()`
- 条件付き依存: `if (tab._overPlayingIcon || tab._overAudioButton)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (lazy.showTabCardPreview)` → `event.preventDefault()`
- 条件付き依存: `if (!(tab._overPlayingIcon || tab._overAudioButton))` → `this.getTabTooltip()`

## Tabbrowser.handleEvent()
- 位置: L9749-9756
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`

## Tabbrowser.observe()
- 位置: L9758-9775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.getAttribute()`, `this.#populateTitleCache()`, `this.updateTitlebar()`
- 条件付き依存: `if (tab.getAttribute("usercontextid") == identity.userContextId)` → `lazy.ContextualIdentityService.setTabStyle()`

## Tabbrowser.refreshBlocked()
- 位置: L9777-9816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationBox.getNotificationWithValue()`, `this.getNotificationBox()`
- 条件付き依存: `if (!(notification))` → `notificationBox.appendNotification()`

## Tabbrowser.callback()
- 位置: L9800-9802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`

## Tabbrowser.#generateUniquePanelID()
- 位置: L9819-9823
- 役割: (未記入)
- 触るとき: (未記入)

## Tabbrowser.destroy()
- 位置: L9825-9876
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Tabbrowser.#tabFilters.get()`, `this.document.removeEventListener()`, `this.documentGlobal.removeEventListener()`, `this.tabContainer.destroy()`
- 条件付き依存: `if (browser.registeredOpenURI)` → `browser.getAttribute()`
- 条件付き依存: `if (browser.registeredOpenURI)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (browser.registeredOpenURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (filter)` → `browser.webProgress.removeProgressListener()`
- 条件付き依存: `if (filter)` → `Tabbrowser.#tabListeners.get()`
- 条件付き依存: `if (listener)` → `filter.removeProgressListener()`
- 条件付き依存: `if (listener)` → `listener.destroy()`
- 条件付き依存: `if (filter)` → `Tabbrowser.#tabFilters.delete()`
- 条件付き依存: `if (filter)` → `Tabbrowser.#tabListeners.delete()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.document.removeEventListener()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.destroy()`
- XPCOM: `Services.obs`

## Tabbrowser.#setupEventListeners()
- 位置: L9878-10310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Window.isInstance()`, `browser.addEventListener()`, `browser.didStartLoadSinceLastUserTyping()`, `browser.webProgress.removeProgressListener()`, `event.target.registerAudibleChangeHandler()`, `event.target.unregisterAudibleChangeHandler()`, `evt.initEvent()`, `filter.removeProgressListener()`, `lazy.SitePermissions.setForPrincipal()`, `oldListener.destroy()`, `tab.dispatchEvent()`, `tab.hasAttribute()`, `tab.registerAudibleChangeHandler()`, `tab.unregisterAudibleChangeHandler()`, `this.#activeSplitView.close()`, `this.#activeSplitView.reverseTabs()`, `this.#activeSplitView.unsplitTabs()`, `this.addEventListener()`, `this.document .getElementById()`, `this.document .getElementById("split-view-menu") ?.getAttribute()`, `this.document.createEvent()`, `this.documentGlobal.addEventListener()`, `this.getTabForBrowser()`, `this.getTabFromAudioEvent()`, `this.maybeCloseTabForRetargetedLoad()`, `this.setPageInfo()`, `this.setTabTitle()`, `this.splitViewCommandSet.addEventListener()`, `this.tabContainer.addEventListener()`, `this.tabpanels.addEventListener()`
- 条件付き依存: `if (event.target == this.tabpanels)` → `this.updateCurrentBrowser()`
- 条件付き依存: `if (this.tabs.length == 1 && this.#shouldCloseWindowWithLastTab)` → `this.documentGlobal.close()`
- 条件付き依存: `if (tab)` → `this.removeTab()`
- 条件付き依存: `if (tab)` → `event.preventDefault()`
- 条件付き依存: `if (titleChanged && !tab.selected && !tab.hasAttribute("busy"))` → `tab.setAttribute()`
- 条件付き依存: `if ( event.detail && event.detail.tabPrompt && event.detail.inPermitUnload && Services.focus.activeWindow )` → `this.documentGlobal.focus()`
- 条件付き依存: `if (promptPrincipal.URI && !promptPrincipal.isSystemPrincipal)` → `Services.perms.testPermissionFromPrincipal()`
- 条件付き依存: `if (permission != Services.perms.ALLOW_ACTION)` → `this.getTabDialogBox()`
- 条件付き依存: `if (permission != Services.perms.ALLOW_ACTION)` → `tabPrompt.onNextPromptShowAllowFocusCheckboxFor()`
- 条件付き依存: `if (event.target == this.selectedBrowser)` → `this.documentGlobal.gURLBar.setURI()`
- 条件付き依存: `if (!tab.hasAttribute("activemedia-blocked"))` → `tab.setAttribute()`
- 条件付き依存: `if (!tab.hasAttribute("activemedia-blocked"))` → `this._tabAttrModified()`
- 条件付き依存: `if (tab.hasAttribute("activemedia-blocked"))` → `tab.removeAttribute()`
- 条件付き依存: `if (tab.hasAttribute("activemedia-blocked"))` → `this._tabAttrModified()`
- XPCOM: `Services.focus` / `Services.perms`

## onTabCrashed()
- 位置: L10054-10092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.removeAttribute()`, `this.getTabForBrowser()`, `this.setIcon()`
- 条件付き依存: `if (!event.isTopFrame)` → `lazy.TabCrashHandler.onSubFrameCrash()`
- 条件付き依存: `if (browser === this.preloadedBrowser)` → `lazy.NewTabPagePreloading.removePreloadedBrowser()`
- 条件付き依存: `if (this.selectedBrowser == browser)` → `lazy.TabCrashHandler.onSelectedBrowserCrash()`
- 条件付き依存: `if (!(this.selectedBrowser == browser))` → `lazy.TabCrashHandler.onBackgroundBrowserCrash()`

## tabContextFTLInserter()
- 位置: L10175-10188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabContainer.removeEventListener()`, `this.translateTabContextMenu()`

## didChange()
- 位置: L10227-10278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#tabListeners.set()`, `browser.getContentBlockingEvents()`, `browser.webProgress.addProgressListener()`, `evt.initEvent()`, `filter.addProgressListener()`, `tab.dispatchEvent()`, `this._callProgressListeners()`, `this.document.createEvent()`, `this.isFindBarInitialized()`
- 条件付き依存: `if (hadStartedLoad)` → `browser.urlbarChangeTracker.startedLoad()`
- 条件付き依存: `if (browser.isRemoteBrowser)` → `tab.removeAttribute()`
- 条件付き依存: `if (this.isFindBarInitialized(tab))` → `this.getCachedFindBar()`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## Tabbrowser.translateTabContextMenu()
- 位置: L10313-10329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `this.document .getElementById()`, `this.document .getElementById("tabContextMenu") .querySelectorAll()`, `this.document .getElementById("tabContextMenu") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`, `this.documentGlobal.MozXULElement.insertFTLIfNeeded()`

## Tabbrowser.setSuccessor()
- 位置: L10331-10356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#predecessors.get()`, `Tabbrowser.#successors.get()`, `Tabbrowser.#successors.set()`, `predecessors.add()`
- 条件付き依存: `if (oldSuccessor)` → `Tabbrowser.#predecessors.get(oldSuccessor).delete()`
- 条件付き依存: `if (oldSuccessor)` → `Tabbrowser.#predecessors.get()`
- 条件付き依存: `if (!successorTab)` → `Tabbrowser.#successors.delete()`
- 条件付き依存: `if (!predecessors)` → `Tabbrowser.#predecessors.set()`

## Tabbrowser.getSuccessor()
- 位置: L10364-10366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#successors.get()`

## Tabbrowser.replaceInSuccession()
- 位置: L10375-10382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.#predecessors.get()`
- 条件付き依存: `if (predecessors)` → `Array.from()`
- 条件付き依存: `if (predecessors)` → `this.setSuccessor()`

## Tabbrowser.clearRelatedTabs()
- 位置: L10384-10386
- 役割: (未記入)
- 触るとき: (未記入)

## TabProgressListener.constructor()
- 位置: L10393-10425
- 役割: (未記入)
- 触るとき: (未記入)
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.#documentGlobal()
- 位置: L10427-10429
- 役割: (未記入)
- 触るとき: (未記入)

## TabProgressListener.#tabbrowser()
- 位置: L10431-10433
- 役割: (未記入)
- 触るとき: (未記入)

## TabProgressListener.destroy()
- 位置: L10435-10438
- 役割: (未記入)
- 触るとき: (未記入)

## TabProgressListener._callProgressListeners()
- 位置: L10440-10443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `args.unshift()`, `this.#tabbrowser._callProgressListeners()`

## TabProgressListener._shouldShowProgress()
- 位置: L10445-10460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aRequest.originalURI.schemeIs()`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md)

## TabProgressListener._isForInitialAboutBlank()
- 位置: L10462-10479
- 役割: (未記入)
- 触るとき: (未記入)
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.onProgressChange()
- 位置: L10481-10510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callProgressListeners()`, `this._shouldShowProgress()`, `this._tab.hasAttribute()`
- 条件付き依存: `if (this._totalProgress && this._tab.hasAttribute("busy"))` → `this._tab.setAttribute()`
- 条件付き依存: `if (this._totalProgress && this._tab.hasAttribute("busy"))` → `this.#tabbrowser._tabAttrModified()`

## TabProgressListener.onProgressChange64()
- 位置: L10512-10528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onProgressChange()`

## TabProgressListener.onStateChange()
- 位置: L10531-10776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aRequest.QueryInterface()`, `this._callProgressListeners()`, `this._isForInitialAboutBlank()`
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `this.#documentGlobal.gInitialPages.includes()`
- 条件付き依存: `if ( !( originalLocation && this.#documentGlobal.gInitialPages.includes( originalLocation.spec ) && originalLocation != "about:blank" && this._browser.initialPag...)` → `this._browser.urlbarChangeTracker.startedLoad()`
- 条件付き依存: `if ( !( originalLocation && this.#documentGlobal.gInitialPages.includes( originalLocation.spec ) && originalLocation != "about:blank" && this._browser.initialPag...)` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if ( this._browser.browsingContext.sessionHistory?.count === 0 && (this._browser.initiatedFromNonWebControlled || lazy.BrowserUIUtils.checkEmptyPageOrigin( this....)` → `this.#tabbrowser.setInitialTabTitle()`
- 条件付き依存: `if (this._tab.selected && !this.#tabbrowser.userTypedValue)` → `this.#documentGlobal.gURLBar.setURI()`
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `this._tab.removeAttribute()`
- 条件付き依存: `if (aStateFlags & STATE_START && aStateFlags & STATE_IS_NETWORK)` → `this._shouldShowProgress()`
- 条件付き依存: `if ( !(aStateFlags & Ci.nsIWebProgressListener.STATE_RESTORING) && aWebProgress && aWebProgress.isTopLevel )` → `this._tab.setAttribute()`
- 条件付き依存: `if ( !(aStateFlags & Ci.nsIWebProgressListener.STATE_RESTORING) && aWebProgress && aWebProgress.isTopLevel )` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (aStateFlags & STATE_STOP && aStateFlags & STATE_IS_NETWORK)` → `this._tab.hasAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("busy"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("busy"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (this._tab.hasAttribute("busy"))` → `Components.isSuccessCode()`
- 条件付き依存: `if (this._tab._notselectedsinceload)` → `this._tab.setAttribute()`
- 条件付き依存: `if (!(this._tab._notselectedsinceload))` → `this._tab.removeAttribute()`
- 条件付き依存: `if ( aWebProgress.isTopLevel && !aWebProgress.isLoadingDocument && Components.isSuccessCode(aStatus) && !this.#tabbrowser.tabContainer.tabAnimationsInProgress &&...)` → `this._tab.setAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("progress"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("progress"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `Components.isSuccessCode()`
- 条件付き依存: `if ( this._tab.selected && aStatus != Cr.NS_BINDING_CANCELLED_OLD_LOAD && !isNavigating )` → `this.#documentGlobal.gURLBar.setURI()`
- 条件付き依存: `if (isSuccessful)` → `this._browser.urlbarChangeTracker.finishedLoad()`
- 条件付き依存: `if (shouldRemoveFavicon && this._tab.hasAttribute("image"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (shouldRemoveFavicon && this._tab.hasAttribute("image"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (!shouldRemoveFavicon)` → `this.#tabbrowser.setDefaultIcon()`
- 条件付き依存: `if (modifiedAttrs.length)` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (ignoreBlank)` → `this._callProgressListeners()`
- 条件付き依存: `if (!(ignoreBlank))` → `this._callProgressListeners()`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.onLocationChange()
- 位置: L10779-10965
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topLevel)` → `this._browser.didStartLoadSinceLastUserTyping()`
- 条件付き依存: `if (topLevel)` → `this._tab.hasAttribute()`
- 条件付き依存: `if (isErrorPage && this._tab.hasAttribute("busy"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (isErrorPage && this._tab.hasAttribute("busy"))` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (!isSameDocument)` → `this._tab.hasAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("soundplaying"))` → `this.#documentGlobal.clearTimeout()`
- 条件付き依存: `if (this._tab.hasAttribute("soundplaying"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("soundplaying"))` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (this._tab.hasAttribute("muted"))` → `this._tab.linkedBrowser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (!isSameDocument)` → `this.#tabbrowser.isFindBarInitialized()`
- 条件付き依存: `if (this.#tabbrowser.isFindBarInitialized(this._tab))` → `this.#tabbrowser.getCachedFindBar()`
- 条件付き依存: `if (findBar.findMode != findBar.FIND_NORMAL)` → `findBar.close()`
- 条件付き依存: `if (!isReload)` → `this.#tabbrowser.setTabTitle()`
- 条件付き依存: `if (!isReload && aWebProgress.isLoadingDocument)` → `TabProgressListener.#getTriggeringPrincipalFromHistory()`
- 条件付き依存: `if (triggerer && triggerer.isSystemPrincipal)` → `this.#tabbrowser.clearRelatedTabs()`
- 条件付き依存: `if (!isSameDocument)` → `this.#documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `this._browser.toggleAttribute()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `lazy.AIWindow.isAIWindowActive()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `lazy.AIWindow.isAIWindowContentPage()`
- 条件付き依存: `if (topLevel)` → `this._browser.getAttribute()`
- 条件付き依存: `if (this._browser.registeredOpenURI)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (this._browser.registeredOpenURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (topLevel)` → `this.#documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (!this.#documentGlobal.isBlankPageURL(aLocation.spec))` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`
- 条件付き依存: `if (!this.#documentGlobal.isBlankPageURL(aLocation.spec))` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (this._tab.splitview && aLocation.spec !== "about:opentabs")` → `this._tab.splitview.tabs.indexOf()`
- 条件付き依存: `if (this._tab.splitview && aLocation.spec !== "about:opentabs")` → `String()`
- 条件付き依存: `if (this._tab.splitview && aLocation.spec !== "about:opentabs")` → `Glean.splitview.uriCount[label].add()`
- 条件付き依存: `if (this._tab != this.#tabbrowser.selectedTab)` → `this.#tabbrowser._tabLayerCache.indexOf()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this.#tabbrowser._tabLayerCache.splice()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this.#tabbrowser._getSwitcher().cleanUpTabAfterEviction()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this.#tabbrowser._getSwitcher()`
- 条件付き依存: `if (!this._blank || this._browser.hasContentOpener)` → `this._callProgressListeners()`
- 条件付き依存: `if (topLevel && !isSameDocument)` → `this._callProgressListeners()`
- 条件付き依存: `if (topLevel)` → `Date.now()`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.onStatusChange()
- 位置: L10967-10980
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.onSecurityChange()
- 位置: L10982-10988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.onContentBlockingEvent()
- 位置: L10990-10996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.onRefreshAttempted()
- 位置: L10998-11005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.#getTriggeringPrincipalFromHistory()
- 位置: L11012-11020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sessionHistory.getEntryAtIndex()`

## _normalizeLoadURIOptions()
- 位置: L11029-11045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getAttribute()`

## _loadFlagsToFixupFlags()
- 位置: L11047-11060
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md)

## _fixupURIString()
- 位置: L11062-11081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `this._loadFlagsToFixupFlags()`
- XPCOM: `Services.uriFixup`

## _updateTriggerMetadataForLoad()
- 位置: L11083-11123
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (globalHistoryOptions.triggeringSource == "newtab")` → `lazy.SponsorProtection.addProtectedBrowser()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `Services.uriFixup.getFixupURIInfo()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `this._loadFlagsToFixupFlags()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `browser.setAttribute()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `Date.now()`
- 条件付き依存: `if (!(globalHistoryOptions?.triggeringSponsoredURL))` → `lazy.SponsorProtection.removeProtectedBrowser()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSearchEngine)` → `browser.setAttribute()`
- 条件付き依存: `if (!(globalHistoryOptions?.triggeringSearchEngine))` → `browser.removeAttribute()`
- XPCOM: `Services.uriFixup`

## fixupAndLoadURIString()
- 位置: L11126-11128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalMaybeFixupLoadURI()`

## loadURI()
- 位置: L11129-11131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalMaybeFixupLoadURI()`

## _internalMaybeFixupLoadURI()
- 位置: L11135-11178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._normalizeLoadURIOptions()`, `this._updateTriggerMetadataForLoad()`
- 条件付き依存: `if (!uriString && !uri)` → `Services.io.newURI()`
- 条件付き依存: `if (!uri)` → `this._fixupURIString()`
- 条件付き依存: `if (startedWithURI)` → `browser.webNavigation.loadURI()`
- 条件付き依存: `if (!(startedWithURI))` → `browser.webNavigation.fixupAndLoadURIString()`
- XPCOM: `Services.io`
