# browser/components/aiwindow/ui/modules/AIWindow.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindow.sys.mjs
source-hash: 75005a4dad5fc61e8da004ff3bc483239b3bb2fe
lines: 1731

## <module>
- 役割: (未記入)
- 呼び出し先: `AIWindow._forEachWindow()`, `AIWindow._onAIWindowEnabledPrefChange.bind()`, `AIWindow._startSchedulers()`, `AIWindow._updateGroupTabsWidgetRegistration()`, `AIWindow._updateMonitorButtonForWindow()`, `AIWindow._updateMonitorWidgetRegistration()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.setPrototypeOf()`, `Services.io.newURI()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## init()
- 位置: L166-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `lazy.NimbusFeatures.smartWindow.onUpdate()`, `lazy.PlacesUtils.observers.addListener()`, `lazy.SmartWindowTelemetry.init()`, `lazy.getAllModelsData()`, `this._aiWindowTabStateManagers.has()`, `this._updateGroupTabsWidgetRegistration()`, `this._updateMonitorWidgetRegistration()`, `this._updateSwitcherWidgetRegistration()`, `this._windowStates.has()`, `this.isAIWindowActive()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._windowStates.set()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._updateHamburgerMenuPosition()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._initializeAskButtonOnToolbox()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `windowArgs.hasKey()`
- 条件付き依存: `if ( windowArgs instanceof Ci.nsIPropertyBag2 && windowArgs.hasKey("aiwindow-trigger") )` → `this.recordOpenWindowTelemetry()`
- 条件付き依存: `if ( windowArgs instanceof Ci.nsIPropertyBag2 && windowArgs.hasKey("aiwindow-trigger") )` → `windowArgs.getPropertyAsAString()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `this._aiWindowTabStateManagers.set()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `this._markActiveStart()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `win.delayedStartupPromise.then()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `this._startSchedulers()`
- 参照: `Ci.nsIPropertyBag2`, `lazy.AIWindowTabStatesManager`, `lazy.ChatStore`, `lazy.ONLOGOUT_NOTIFICATION`, `this._initialized`, `this.handlePlacesEvents`, `this.onNimbusUpdate`, `win?.arguments`
- XPCOM: [`nsIPropertyBag2`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.obs` / `Services.prefs`

## _startSchedulers()
- 位置: L224-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MemoriesSchedulers.maybeRunAndSchedule()`, `lazy.TelemetryScheduler.maybeInit()`

## handlePlacesEvents()
- 位置: L229-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ChatStore.deleteAllUrlsFromMessages()`
- 条件付き依存: `if ( event.reason == PlacesVisitRemoved.REASON_DELETED && !event.isPartialVisistsRemoval )` → `lazy.ChatStore.deleteUrlFromMessages()`
- 参照: `PlacesVisitRemoved.REASON_DELETED`, `event.isPartialVisistsRemoval`, `event.reason`, `event.type`, `event.url`

## uninit()
- 位置: L250-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.NimbusFeatures.smartWindow.offUpdate()`, `lazy.PlacesUtils.observers.removeListener()`
- 参照: `lazy.ONLOGOUT_NOTIFICATION`, `this._initialized`, `this.handlePlacesEvents`, `this.onNimbusUpdate`
- XPCOM: `Services.obs` / `Services.prefs`

## onNimbusUpdate()
- 位置: L269-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.smartWindow.getVariable()`
- 条件付き依存: `if (lazy.NimbusFeatures.smartWindow.getVariable("enabled"))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L275-291
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === lazy.ONLOGOUT_NOTIFICATION)` → `this._onAccountLogout()`
- 条件付き依存: `if (topic === "tabstrip-orientation-change")` → `this._onTabstripOrientationChange()`
- 条件付き依存: `if ( topic === "browser-region-updated" || topic === "nsPref:changed" )` → `this._updateMonitorWidgetRegistration()`
- 条件付き依存: `if (topic === lazy.MONITOR_CONDITION_MET_TOPIC)` → `this.showMonitorAttention()`
- 条件付き依存: `if (topic === lazy.MONITOR_RUN_FAILED_TOPIC)` → `this.showMonitorErrorAttention()`
- 参照: `lazy.MONITOR_CONDITION_MET_TOPIC`, `lazy.MONITOR_RUN_FAILED_TOPIC`, `lazy.ONLOGOUT_NOTIFICATION`

## _onAccountLogout()
- 位置: L295-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `this.isAIWindowActive()`
- 条件付き依存: `if (!win.closed && this.isAIWindowActive(win))` → `this.toggleAIWindow()`
- 参照: `win.closed`
- XPCOM: `Services.wm`

## hasActiveAIWindows()
- 位置: L306-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `this.isAIWindowActiveAndEnabled()`
- 参照: `win.closed`
- XPCOM: `Services.wm`

## _reconcileNewTabPages()
- 位置: L315-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `currentURI.equalsExceptRef()`, `homePagePrefURIs.some()`, `lazy.HomePage.parseCustomHomepageURLs()`, `lazy.HomePage.parseCustomHomepageURLs( homePagePref ).flatMap()`
- 条件付き依存: `if ( currentURI.equalsExceptRef(newTabPrefURI) || currentURI.equalsExceptRef(aboutNewTabURI) || currentURI.equalsExceptRef(aboutHomeURI) || homePagePrefURIs.some...)` → `this.hasActiveChatInBrowser()`
- 条件付き依存: `if ( currentURI.equalsExceptRef(newTabPrefURI) || currentURI.equalsExceptRef(aboutNewTabURI) || currentURI.equalsExceptRef(aboutHomeURI) || homePagePrefURIs.some...)` → `browser.loadURI()`
- 参照: `browser.currentURI`, `browser?.currentURI`, `tab.linkedBrowser`, `win.BROWSER_NEW_TAB_URL`, `win.gBrowser.tabs`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## hasActiveChatInBrowser()
- 位置: L356-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindowElement.classList.contains()`, `browser?.contentDocument?.querySelector()`

## _forEachWindow()
- 位置: L365-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`, `ChromeUtils.nondeterministicGetWeakMapKeys(this._windowStates).forEach()`
- 条件付き依存: `if (win && !win.closed)` → `callback()`
- 参照: `this._windowStates`, `win.closed`

## _onAIWindowEnabledPrefChange()
- 位置: L375-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.CustomizableUI.getWidget()`, `this._updateButtonVisibility()`, `this._updateGroupTabsWidgetRegistration()`, `this._updateMonitorWidgetRegistration()`, `this._updateSwitcherWidgetRegistration()`
- 条件付き依存: `if (!this.isAvailable)` → `this._onAccountLogout()`
- 参照: `this.isAvailable`, `widget?.instances`
- XPCOM: `Services.prefs`

## _updateButtonVisibility()
- 位置: L392-396
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node)` → `this.isAIWindowEnabled()`
- 参照: `node.hidden`

## _onTabstripOrientationChange()
- 位置: L398-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._forEachWindow()`, `this._updateHamburgerMenuPosition()`

## _updateHamburgerMenuPosition()
- 位置: L412-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `targetToolbar.querySelector()`, `this.isAIWindowActive()`, `win.document.getElementById()`
- 条件付き依存: `if (this.isAIWindowActive(win) || this.verticalTabsEnabled)` → `titlebarContainer.after()`
- 条件付き依存: `if (isToggling)` → `win.document .getElementById("nav-bar") .querySelector()`
- 条件付き依存: `if (isToggling)` → `win.document .getElementById()`
- 条件付き依存: `if (isToggling)` → `postTabsSpacer.before()`
- 参照: `this.verticalTabsEnabled`

## _initializeAskButtonOnToolbox()
- 位置: L435-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAIWindowActive()`, `win.document.getElementById()`
- 参照: `askButton.hidden`

## _updateGroupTabsButtonVisibility()
- 位置: L449-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAIWindowActive()`
- 条件付き依存: `if (!node.hidden)` → `lazy.AutoTabGroupingSuggestions.preloadModels()`
- 参照: `lazy.AutoTabGroupingSuggestions.isAvailable`, `lazy.autoTabGroupingEnabled`, `node.documentGlobal`, `node.hidden`

## monitorButtonEnabled()
- 位置: L472-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorUIUtils.isMonitorRegionSupported()`, `this.isAIWindowEnabled()`
- 参照: `lazy.agentEnabled`, `lazy.agentToolbarEnabled`

## _updateMonitorWidgetRegistration()
- 位置: L485-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._destroyMonitorWidget()`
- 条件付き依存: `if (this.monitorButtonEnabled && !this.isBlocked)` → `this._createMonitorWidget()`
- 参照: `this.isBlocked`, `this.monitorButtonEnabled`

## _createMonitorWidget()
- 位置: L493-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.CustomizableUI.createWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.MONITOR_CONDITION_MET_TOPIC`, `lazy.MONITOR_RUN_FAILED_TOPIC`, `this._monitorWidgetCreated`
- XPCOM: `Services.obs`

## onCreated()
- 位置: L504-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.setAttribute()`, `this._shouldShowMonitorButton()`, `this._updateMonitorAttentionForNode()`
- 参照: `node.documentGlobal`, `node.hidden`

## onCommand()
- 位置: L513-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.toggleMonitorPanel()`
- 参照: `event.view`

## _destroyMonitorWidget()
- 位置: L522-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.CustomizableUI.destroyWidget()`
- 参照: `lazy.MONITOR_CONDITION_MET_TOPIC`, `lazy.MONITOR_RUN_FAILED_TOPIC`, `this._monitorWidgetCreated`
- XPCOM: `Services.obs`

## _updateMonitorButtonForWindow()
- 位置: L540-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._shouldShowMonitorButton()`, `this._updateMonitorAttentionForNode()`, `win.document.getElementById()`
- 参照: `button.hidden`

## monitorAttentionIds()
- 位置: L556-558
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MonitorAttention.matchedIds`

## hasMonitorAnnouncement()
- 位置: L567-569
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.monitorAnnouncement`

## hasMonitorAttention()
- 位置: L577-579
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MonitorAttention.hasAttention`, `this.hasMonitorAnnouncement`

## takeMonitorAttentionIds()
- 位置: L588-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearMonitorAttention()`
- 参照: `this.monitorAttentionIds`

## showMonitorAttention()
- 位置: L597-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorAttention.recordMatch()`, `this._forEachWindow()`, `this._updateMonitorButtonForWindow()`

## showMonitorErrorAttention()
- 位置: L608-611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorAttention.recordError()`, `this._forEachWindow()`, `this._updateMonitorButtonForWindow()`

## clearMonitorAttention()
- 位置: L617-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorAttention.clearAttention()`, `this._forEachWindow()`, `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (lazy.monitorAnnouncement)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.monitorAnnouncement`
- XPCOM: `Services.prefs`

## _updateMonitorAttentionForNode()
- 位置: L628-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.toggleAttribute()`
- 参照: `this.hasMonitorAttention`

## _shouldShowMonitorButton()
- 位置: L632-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAIWindowActive()`
- 参照: `this.monitorButtonEnabled`

## isDefaultWindow()
- 位置: L636-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.isAIWindowEnabled()`
- 参照: `this.AIWindowEnabledPref`
- XPCOM: `Services.prefs`

## shouldOpenAsSmartWindow()
- 位置: L644-652
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this.isDefaultWindow`

## onFirstWindowReady()
- 位置: async L662-685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStartup.willRestore()`, `this._authorizeAndToggleWindow()`, `this.isAIWindowActive()`, `this.recordLaunchCommandTelemetry()`, `this.shouldOpenAsSmartWindow()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `lazy.AIWindowAccountAuth.ensureAIWindowAccess()`
- 参照: `win.gBrowser.selectedBrowser`

## _recordSmartWindowUsage()
- 位置: L693-698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## handleAIWindowOptions()
- 位置: L714-786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `args.queryElementAt()`, `console.error()`, `propBag.setPropertyAsBool()`, `this.immersiveViewURIs.some()`, `this.isAIWindowActiveAndEnabled()`, `this.isAIWindowEnabled()`
- 条件付き依存: `if (!args.length)` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if (!args.length)` → `args.appendElement()`
- 条件付き依存: `if (!restoreSessionURL)` → `args.queryElementAt()`
- 条件付き依存: `if (!restoreSessionURL)` → `firstArg.data.split()`
- 条件付き依存: `if (!propBag)` → `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`
- 条件付き依存: `if (!propBag)` → `args.appendElement()`
- 条件付き依存: `if (canInheritAIWindow)` → `propBag.setPropertyAsAString()`
- 条件付き依存: `if (willOpenImmersive)` → `propBag.setPropertyAsBool()`
- 参照: `Ci.nsIMutableArray`, `Ci.nsIPropertyBag2`, `Ci.nsISupportsString`, `Ci.nsIWritablePropertyBag2`, `aiWindowURI.data`, `args.length`, `this.initialStartupURL`, `uri.spec`
- XPCOM: [`nsIMutableArray`](../../../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIPropertyBag2`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / [`nsISupportsString`](../../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-string;1`

## handleAIWindowSwitcher()
- 位置: L793-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PanelMultiView.getViewNode()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this._windowStates.get()`, `this.isAIWindowActive()`, `this.launchWindow()`, `this.toggleAIWindow()`, `view.addEventListener()`
- 条件付き依存: `if (!isPrivateWindow)` → `view.querySelector()`
- 条件付き依存: `if (!isPrivateWindow)` → `classicSwitchButton.toggleAttribute()`
- 条件付き依存: `if (!isPrivateWindow)` → `smartSwitchButton.toggleAttribute()`
- 条件付き依存: `if (!windowState)` → `this._windowStates.set()`
- 参照: `classicSwitchButton.hidden`, `event.target.id`, `smartSwitchButton.hidden`, `win.document`, `win.gBrowser.selectedBrowser`, `windowState.viewInitialized`

## isAIWindowActive()
- 位置: L841-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.document.documentElement.hasAttribute()`

## isAIWindowEnabled()
- 位置: L850-852
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isAvailable`

## isAIWindowActiveAndEnabled()
- 位置: L854-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAIWindowActive()`, `this.isAIWindowEnabled()`

## isOpeningAIWindow()
- 位置: L864-871
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowArgs.hasKey()`
- 参照: `Ci.nsIPropertyBag2`, `win?.arguments`
- XPCOM: [`nsIPropertyBag2`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## isAIWindowContentPage()
- 位置: L879-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWINDOW_URI.equalsExceptRef()`, `FIRSTRUN_URI.equalsExceptRef()`

## isAIWindowNewTabPage()
- 位置: L892-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWINDOW_URI.equalsExceptRef()`

## getChatTabConversationId()
- 位置: L900-910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._aiWindowTabStateManagers .get()`, `this._aiWindowTabStateManagers .get(tab.documentGlobal) ?.getTabConversationId()`, `this.isAIWindowNewTabPage()`
- 参照: `tab.documentGlobal`, `tab.linkedBrowser?.currentURI`

## appMenu()
- 位置: L920-926
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._aiWindowMenu.addMenuitems()`
- 参照: `lazy.AIWindowMenu`, `this._aiWindowMenu`

## newTabURL()
- 位置: L928-930
- 役割: (未記入)
- 触るとき: (未記入)

## firstrunURL()
- 位置: L932-934
- 役割: (未記入)
- 触るとき: (未記入)

## initialStartupURL()
- 位置: L943-945
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasFirstrunCompleted`

## performSearch()
- 位置: async L954-978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `console.error()`, `lazy.AIWindowUI.focusSidebar()`, `lazy.SearchService.getDefault()`, `lazy.SearchUIUtils.loadSearch()`
- XPCOM: `Services.scriptSecurityManager`

## moveConversationToSidebar()
- 位置: async L987-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.moveFullPageToSidebar()`

## focusSidebar()
- 位置: L991-993
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.focusSidebar()`

## openSidebarAndContinue()
- 位置: L1002-1028
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiBrowser?.contentDocument?.querySelector()`, `lazy.AIWindowUI.focusSidebar()`, `lazy.AIWindowUI.openSidebar()`, `sidebar?.querySelector()`, `win.document.getElementById()`
- 条件付き依存: `if (aiWindow?.reloadAndContinue)` → `aiWindow.reloadAndContinue()`
- 条件付き依存: `if (aiBrowser)` → `aiBrowser.setAttribute()`
- 参照: `aiWindow?.reloadAndContinue`

## createAITab()
- 位置: L1040-1092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `[ lazy.l10n.formatValueSync("ai-tab-create-page-prompt", { tabCount: pageUrls.length, }), ...pageUrls, ].join()`, `["http:", "https:"].includes()`, `lazy.URILoadingHelper.openTrustedLinkIn()`, `lazy.l10n.formatValueSync()`, `urls.filter()`
- 参照: `URL.parse(url)?.protocol`, `pageUrls.length`

## resolveOnContentBrowserCreated()
- 位置: L1057-1090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.contentDocument?.querySelector()`, `controller.abort()`, `submit()`, `tab.addEventListener()`, `win.addEventListener()`, `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (browser.contentDocument?.querySelector("ai-window")?.conversation)` → `submit()`
- 参照: `browser.contentDocument?.querySelector("ai-window")?.conversation`, `event.detail.tab`

## submit()
- 位置: L1058-1063
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.contentDocument.querySelector()`, `browser.contentDocument.querySelector("ai-window").submitChatMessage()`

## recordOpenWindowTelemetry()
- 位置: L1104-1119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.openWindow.record()`, `lazy.AIWindowAccountAuth.isSignedIn()`, `lazy.AIWindowAccountAuth.isSignedIn() .then()`, `lazy.AIWindowAccountAuth.isSignedIn() .then(result => { signedIn = result; }) .finally()`
- 参照: `lazy.hasFirstrunCompleted`, `win?.gBrowser?.tabs.length`

## recordLaunchCommandTelemetry()
- 位置: L1130-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.launchCommandInvoked.record()`, `lazy.AIWindowAccountAuth.isSignedIn()`, `lazy.AIWindowAccountAuth.isSignedIn() .then()`, `lazy.AIWindowAccountAuth.isSignedIn() .then(result => { signedIn = result; }) .finally()`

## toggleAIWindow()
- 位置: L1155-1210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAIWindowActive()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `lazy.NewTabPagePreloading.removePreloadedBrowser()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `win.document.documentElement.toggleAttribute()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._reconcileNewTabPages()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._updateHamburgerMenuPosition()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._initializeAskButtonOnToolbox()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._updateGroupTabsButtonVisibility()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `win.document.getElementById()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this._aiWindowTabStateManagers.has()`
- 条件付き依存: `if (!this._aiWindowTabStateManagers.has(win))` → `this._aiWindowTabStateManagers.set()`
- 条件付き依存: `if (lazy.hasFirstrunCompleted)` → `this._aiWindowTabStateManagers .get(win) ?.openSidebarForReturningUser()`
- 条件付き依存: `if (lazy.hasFirstrunCompleted)` → `this._aiWindowTabStateManagers .get()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this._startSchedulers()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this._markActiveStart()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this.recordOpenWindowTelemetry()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `this._consumeActiveDuration()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `this._uninitTabStateManager()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `this._recordSmartWindowUsage()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `Glean.smartWindow.classicSwitch.record()`
- 参照: `lazy.AIWindowTabStatesManager`, `lazy.hasFirstrunCompleted`, `win.BROWSER_NEW_TAB_URL`, `win.gBrowser.tabs.length`
- XPCOM: `Services.obs` / `Services.prefs`

## _uninitTabStateManager()
- 位置: L1212-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.uninit()`, `this._aiWindowTabStateManagers.delete()`, `this._aiWindowTabStateManagers.get()`

## getActiveConversation()
- 位置: L1221-1225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._aiWindowTabStateManagers.get()`, `this._aiWindowTabStateManagers.get(win)?.getActiveConversation()`

## _getTabStateManager()
- 位置: L1227-1229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._aiWindowTabStateManagers.get()`

## restoreTabConversation()
- 位置: L1237-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getTabStateManager()`, `this._getTabStateManager(win)?.setTabStateConversation()`, `win?.gBrowser.getTabForBrowser()`
- 参照: `browser.documentGlobal`

## unloadWindow()
- 位置: L1246-1255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._uninitTabStateManager()`, `this._windowStates.delete()`, `this.isAIWindowActive()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `this._consumeActiveDuration()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `Glean.smartWindow.closeWindow.record()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `this._recordSmartWindowUsage()`
- 参照: `win.gBrowser?.tabs.length`

## _markActiveStart()
- 位置: L1257-1262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._windowStates.get()`
- 条件付き依存: `if (windowState)` → `Date.now()`
- 参照: `windowState.aiActiveStartTime`

## _consumeActiveDuration()
- 位置: L1264-1271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._windowStates.get()`
- 参照: `windowState.aiActiveStartTime`, `windowState?.aiActiveStartTime`

## _authorizeAndToggleWindow()
- 位置: async L1273-1302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.AIWindowAccountAuth.ensureAIWindowAccess()`, `this.toggleAIWindow()`
- 条件付き依存: `if (!lazy.hasFirstrunCompleted)` → `win.gBrowser.loadURI()`
- 条件付き依存: `if (trigger === "startup")` → `Services.io.newURI()`
- 条件付き依存: `if (tab.linkedBrowser?.currentURI?.spec === "about:blank")` → `tab.linkedBrowser.loadURI()`
- 参照: `lazy.hasFirstrunCompleted`, `tab.linkedBrowser?.currentURI?.spec`, `win.gBrowser.selectedBrowser`, `win.gBrowser.tabs`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## launchWindow()
- 位置: async L1304-1347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.AIWindowAccountAuth.canAccessAIWindow()`, `lazy.BrowserWindowTracker.promiseOpenWindow()`, `this.recordLaunchCommandTelemetry()`, `this.recordOpenWindowTelemetry()`
- 条件付き依存: `if (!this.isAllowed)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!openNewWindow)` → `this._authorizeAndToggleWindow()`
- 条件付き依存: `if (!isAuthorized)` → `this._authorizeAndToggleWindow()`
- 参照: `browser.documentGlobal`, `browser?.documentGlobal`, `this.isAllowed`, `this.isBlocked`
- XPCOM: `Services.prefs`

## launchSignInFlow()
- 位置: async L1355-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.AIWindowAccountAuth.promptSignIn()`

## updateImmersiveView()
- 位置: L1370-1435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `currentURI.equalsExceptRef()`, `root.hasAttribute()`, `root.toggleAttribute()`, `this._updateMonitorButtonForWindow()`, `this.isAIWindowActiveAndEnabled()`, `this.shouldUseImmersiveView()`, `win.document.getElementById()`, `win.gBrowser.selectedBrowser?.toggleAttribute()`
- 条件付き依存: `if (!this.isAIWindowActiveAndEnabled(win))` → `root.toggleAttribute()`
- 条件付き依存: `if (!this.isAIWindowActiveAndEnabled(win))` → `root.removeAttribute()`
- 条件付き依存: `if (!this.isAIWindowActiveAndEnabled(win))` → `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (isImmersiveView)` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if (root.hasAttribute("aiwindow-first-run") && !isFirstRunView)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (isFirstRun)` → `selectedTab?.setAttribute()`
- 条件付き依存: `if (!(isFirstRun))` → `selectedTab?.removeAttribute()`
- 参照: `askButton.hidden`, `win.gBrowser.selectedTab`
- XPCOM: `Services.io` / `Services.obs`

## shouldUseImmersiveView()
- 位置: L1443-1450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `immersiveURI.equalsExceptRef()`, `this.immersiveViewURIs.some()`

## getSmartbarForWindow()
- 位置: L1459-1467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindowCE?.shadowRoot.getElementById()`, `contentDocument?.querySelector()`
- 参照: `window.gBrowser.selectedBrowser`

## _createSwitcherWidget()
- 位置: L1469-1494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.createWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.CustomizableUI.AREA_TABSTRIP`, `this._switcherWidgetCreated`

## onCreated()
- 位置: L1483-1487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.classList.add()`, `node.setAttribute()`, `this._updateButtonVisibility()`

## onViewShowing()
- 位置: L1488-1491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleAIWindowSwitcher()`
- 参照: `event.target.documentGlobal`

## _createGroupTabsWidget()
- 位置: L1496-1518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.createWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.CustomizableUI.AREA_TABSTRIP`, `this._groupTabsWidgetCreated`

## onCreated()
- 位置: L1508-1512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.setAttribute()`, `this._updateGroupTabsButtonVisibility()`

## onCommand()
- 位置: L1513-1515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.toggleGroupTabsPanel()`
- 参照: `event.target.documentGlobal`

## _destroyGroupTabsWidget()
- 位置: L1520-1527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`
- 参照: `this._groupTabsWidgetCreated`

## _updateGroupTabsWidgetRegistration()
- 位置: L1534-1540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._destroyGroupTabsWidget()`
- 条件付き依存: `if (lazy.autoTabGroupingEnabled && !this.isBlocked)` → `this._createGroupTabsWidget()`
- 参照: `lazy.autoTabGroupingEnabled`, `this.isBlocked`

## _destroySwitcherWidget()
- 位置: L1542-1549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`
- 参照: `this._switcherWidgetCreated`

## _updateSwitcherWidgetRegistration()
- 位置: L1554-1560
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isBlocked)` → `this._destroySwitcherWidget()`
- 条件付き依存: `if (!(this.isBlocked))` → `this._createSwitcherWidget()`
- 参照: `this.isBlocked`

## id()
- 位置: L1570-1572
- 役割: (未記入)
- 触るとき: (未記入)

## hasDistinctEnabledState()
- 位置: L1579-1582
- 役割: (未記入)
- 触るとき: (未記入)

## isBlocked()
- 位置: L1589-1594
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.AIControlDefault`, `this.AIControlSmartWindow`

## isEnabled()
- 位置: L1601-1606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 参照: `this.isAvailable`
- XPCOM: `Services.prefs`

## isAvailable()
- 位置: L1608-1610
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isAllowed`, `this.isBlocked`

## isAllowed()
- 位置: L1617-1619
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.AIWindowEnabledPref`

## canRunOnDevice()
- 位置: L1626-1629
- 役割: (未記入)
- 触るとき: (未記入)

## isManagedByPolicy()
- 位置: L1636-1641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## makeAvailable()
- 位置: async L1648-1653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## enable()
- 位置: async L1660-1663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## block()
- 位置: async L1670-1676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `lazy.ChatStore.deleteAllConversations()`, `this._removeMemories()`
- XPCOM: `Services.prefs`

## _removeMemories()
- 位置: async L1684-1696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `console.error()`, `lazy.MemoryStore.getMemories()`, `lazy.MemoryStore.hardDeleteMemory()`
- 参照: `memory.id`
- XPCOM: `Services.prefs`
