# browser/components/ipprotection/IPProtectionPanel.sys.mjs

source: browser/components/ipprotection/IPProtectionPanel.sys.mjs
source-hash: 9e1f042a96920432d15b659ecf67c83cfc5ae923
lines: 1363

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## IPProtectionPanel.loadCustomElements()
- 位置: L110-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptloader.loadSubScriptWithOptions()`, `hasCustomElements.add()`, `hasCustomElements.has()`
- 参照: `IPProtectionPanel.CUSTOM_ELEMENTS_SCRIPT`
- XPCOM: `Services.scriptloader`

## IPProtectionPanel.#locationsKeyListener()
- 位置: L169-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `[backButton, listTabStop, promoButton].filter()`, `e.preventDefault()`, `e.stopPropagation()`, `listItems.find()`, `listItems.includes()`, `locationsList.querySelectorAll()`, `nextTabOnlyElement?.focus()`, `tabOnlyElements.indexOf()`, `view.contains()`, `view.querySelector()`
- 条件付き依存: `if (e.code === "ArrowRight" || e.code === "ArrowLeft")` → `e.preventDefault()`
- 条件付き依存: `if (e.code === "ArrowRight" || e.code === "ArrowLeft")` → `e.stopPropagation()`
- 条件付き依存: `if (isBackArrow)` → `this.panelMultiView?.goBack()`
- 条件付き依存: `if (e.code === "ArrowDown" || e.code === "ArrowUp")` → `e.preventDefault()`
- 条件付き依存: `if (e.code === "ArrowDown" || e.code === "ArrowUp")` → `e.stopPropagation()`
- 条件付き依存: `if (e.code === "ArrowDown" || e.code === "ArrowUp")` → `view.contains()`
- 条件付き依存: `if (e.code === "ArrowDown" || e.code === "ArrowUp")` → `listItems.includes()`
- 条件付き依存: `if (e.code === "ArrowDown" || e.code === "ArrowUp")` → `listItems.indexOf()`
- 条件付き依存: `if (e.code === "ArrowDown" || e.code === "ArrowUp")` → `nextListItem?.focus()`
- 条件付き依存: `if (e.code === "Enter" || e.code === "NumpadEnter" || e.code === "Space")` → `view.contains()`
- 条件付き依存: `if (view.contains(focused) && focused === backButton)` → `e.preventDefault()`
- 条件付き依存: `if (view.contains(focused) && focused === backButton)` → `e.stopPropagation()`
- 条件付き依存: `if (view.contains(focused) && focused === backButton)` → `this.panelMultiView?.goBack()`
- 条件付き依存: `if (e.code === "Enter" || e.code === "NumpadEnter" || e.code === "Space")` → `focused?.hasAttribute()`
- 条件付き依存: `if (focused?.hasAttribute("aria-disabled"))` → `e.preventDefault()`
- 条件付き依存: `if (focused?.hasAttribute("aria-disabled"))` → `e.stopPropagation()`
- 条件付き依存: `if (e.shiftKey)` → `backButton?.focus()`
- 条件付き依存: `if (!(e.shiftKey))` → `(promoButton ?? backButton)?.focus()`
- 参照: `Services.locale.isAppLocaleRTL`, `e.code`, `e.shiftKey`, `item.tabIndex`, `listItems.length`, `tabOnlyElements.length`, `this.#locationsClosedByKeyboard`, `this.locationsView`, `view.ownerDocument.activeElement`
- XPCOM: `Services.locale`

## IPProtectionPanel.#panelKeyListener()
- 位置: L293-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.moveFocus()`, `e.preventDefault()`, `e.stopPropagation()`
- 参照: `Services.focus.FLAG_BYKEY`, `Services.focus.MOVEFOCUS_BACKWARD`, `Services.focus.MOVEFOCUS_FORWARD`, `e.target.documentGlobal`
- XPCOM: `Services.focus`

## IPProtectionPanel.gBrowser()
- 位置: L318-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.get()`
- 参照: `win?.gBrowser`

## IPProtectionPanel.toolbarButton()
- 位置: L329-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPProtection.getToolbarButton()`, `this.#window.get()`

## IPProtectionPanel.active()
- 位置: L338-343
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.panel`, `this.panel.state`

## IPProtectionPanel.locationsView()
- 位置: L345-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PanelMultiView.getViewNode()`
- 参照: `IPProtectionPanel.LOCATIONS_PANELVIEW`, `this.panel`, `this.panel.ownerDocument`

## IPProtectionPanel.panelMultiView()
- 位置: L355-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel?.querySelector()`

## IPProtectionPanel.isExceptionsFeatureEnabled()
- 位置: L363-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## IPProtectionPanel.isInclusionsFeatureEnabled()
- 位置: L374-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## IPProtectionPanel.isDefaultBrowser()
- 位置: L381-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ShellService.isDefaultBrowser()`

## IPProtectionPanel.isPremium()
- 位置: L386-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getBandwidthUsage()`
- 参照: `lazy.IPProtectionService.authProvider.hasUpgraded`, `this.isDefaultBrowser`

## IPProtectionPanel.constructor()
- 位置: L402-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `Services.prefs.getBoolPref()`, `this.#addPrefObserver()`, `this.#addProgressListener()`, `this.#addProxyListeners()`, `this.#getBandwidthUsage()`, `this.#getSiteData()`, `this.#handleEvent.bind()`, `this.#handlePrefChange.bind()`, `this.#window.get()`
- 条件付き依存: `if (win)` → `IPProtectionPanel.loadCustomElements()`
- 参照: `lazy.EGRESS_LOCATION`, `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVATING`, `lazy.IPPProxyStates.ACTIVE`, `lazy.IPPProxyStates.PAUSED`, `lazy.IPProtectionServerlist.countries`, `lazy.IPProtectionService.authProvider.hasUpgraded`, `lazy.IPProtectionService.authProvider.isEnrolling`, `lazy.IPProtectionService.state`, `lazy.IPProtectionStates.UNAUTHENTICATED`, `lazy.UPGRADE_NOT_AVAILABLE`, `this.#window`, `this.handleEvent`, `this.handlePrefChange`, `this.isExceptionsFeatureEnabled`, `this.isInclusionsFeatureEnabled`, `this.isPremium`, `this.progressListener`, `this.state`
- XPCOM: `Services.prefs`

## onLocationChange()
- 位置: L439-458
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.active && aLocationURI)` → `this.#updateSiteData()`
- 参照: `aWebProgress.isTopLevel`, `this.active`, `this.gBrowser?.selectedBrowser`

## IPProtectionPanel.setState()
- 位置: L485-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 条件付き依存: `if (this.active)` → `this.updateState()`
- 参照: `this.active`, `this.state`

## IPProtectionPanel.updateState()
- 位置: L499-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `this.updateComponentState()`
- 参照: `this.components`, `this.state`

## IPProtectionPanel.updateComponentState()
- 位置: L515-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.requestUpdate()`, `this.components.has()`
- 条件付き依存: `if (!this.components.has(element))` → `this.components.add()`
- 参照: `element.state`, `element?.isConnected`, `this.state`

## IPProtectionPanel.#startProxy()
- 位置: async L528-560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handledElsewhere.includes()`, `lazy.IPPProxyManager.start()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.#window.get()`
- 条件付き依存: `if (!this.isPremium && country)` → `lazy.IPProtectionServerlist.getLocation()`
- 条件付き依存: `if (error && !handledElsewhere.includes(error))` → `this.#errorMessage()`
- 条件付き依存: `if (error && !handledElsewhere.includes(error))` → `this.setState()`
- 条件付き依存: `if (error && !handledElsewhere.includes(error))` → `this.toolbarButton?.updateState()`
- 参照: `lazy.ERRORS.CANCELED`, `lazy.ERRORS.NOT_READY`, `lazy.ERRORS.QUOTA_EXHAUSTED`, `location?.country.locked`, `this.isPremium`, `this.state.location`

## IPProtectionPanel.#errorMessage()
- 位置: L562-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[lazy.ERRORS.NETWORK, lazy.ERRORS.VPN_UNAVAILABLE].includes()`
- 参照: `lazy.ERRORS.GENERIC`, `lazy.ERRORS.NETWORK`, `lazy.ERRORS.VPN_UNAVAILABLE`

## IPProtectionPanel.#stopProxy()
- 位置: async L569-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.stop()`

## IPProtectionPanel.showHelpPage()
- 位置: L578-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target?.closest()`
- 条件付き依存: `if (win)` → `win.openWebLinkIn()`
- 条件付き依存: `if (win)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (panelParent)` → `panelParent.hidePopup()`
- 参照: `LINKS.SUPPORT_SLUG`, `e.target?.documentGlobal`
- XPCOM: `Services.urlFormatter`

## IPProtectionPanel.#handleHeaderButtonKeypress()
- 位置: L594-598
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.code == "Space" || e.code == "Enter")` → `IPProtectionPanel.showHelpPage()`
- 参照: `e.code`

## IPProtectionPanel.showing()
- 位置: L610-655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.#shouldShowBandwidthWarning()`, `this.#updateSiteData()`, `this.setState()`
- 条件付き依存: `if (this.initiatedUpgrade)` → `lazy.IPProtectionService.authProvider.checkForUpgrade()`
- 条件付き依存: `if (this.state.paused)` → `lazy.IPPProxyManager.refreshUsage()`
- 条件付き依存: `if (this.state.bandwidthWarning)` → `lazy.IPProtectionInfobarManager.hideInfobars()`
- 条件付き依存: `if (this.panel)` → `this.updateState()`
- 条件付き依存: `if (!(this.panel))` → `panelView.closest()`
- 条件付き依存: `if (!(this.panel))` → `this.#addPanelListeners()`
- 条件付き依存: `if (!(this.panel))` → `this.#createPanel()`
- 条件付き依存: `if (contentEl)` → `panelView.addEventListener()`
- 条件付き依存: `if (!hasUserEverOpenedPanel)` → `Services.prefs.setBoolPref()`
- 参照: `IPProtectionPanel.CONTENT_TAGNAME`, `contentEl.dataset.capturesFocus`, `panelView.ownerDocument`, `this.#panelKeyListener`, `this.#panelView`, `this.initiatedUpgrade`, `this.isExceptionsFeatureEnabled`, `this.isInclusionsFeatureEnabled`, `this.isPremium`, `this.panel`, `this.state.bandwidthWarning`, `this.state.paused`
- XPCOM: `Services.prefs`

## IPProtectionPanel.hiding()
- 位置: L662-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`, `lazy.IPPOnboardingMessage.readPrefMask()`, `this.destroy()`
- 条件付き依存: `if (this.state.showLocationButtonBadge)` → `Services.prefs.setBoolPref()`
- 参照: `ONBOARDING_PREF_FLAGS.EVER_USED_SITE_EXCEPTIONS`, `this.gBrowser.selectedBrowser`, `this.state.showLocationButtonBadge`
- XPCOM: `Services.prefs`

## IPProtectionPanel.#createPanel()
- 位置: L692-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentArea.appendChild()`, `ownerDocument.createElement()`, `panelView.querySelector()`, `this.components.add()`
- 条件付き依存: `if (headerButton)` → `headerButton.addEventListener()`
- 条件付き依存: `if (headerButton)` → `headerButton.setAttribute()`
- 条件付き依存: `if (headerButton)` → `this.#headerButtons.push()`
- 参照: `IPProtectionPanel.showHelpPage`, `contentArea.children.length`, `this.#handleHeaderButtonKeypress`

## IPProtectionPanel.open()
- 位置: async L723-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`, `this.#window.get()`, `widget.forWindow()`, `window.PanelUI.showSubView()`
- 参照: `IPProtectionPanel.MAIN_PANELVIEW`, `IPProtectionPanel.WIDGET_ID`, `lazy.IPProtection.created`, `this.active`, `widget.forWindow(window).anchor`, `window?.PanelUI`

## IPProtectionPanel.close()
- 位置: L736-738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel?.hidePopup()`

## IPProtectionPanel.startLoginFlow()
- 位置: async L749-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SpecialMessageActions.fxaSignInFlow()`, `this.#window.get()`, `this.close()`
- 参照: `SIGNIN_DATA.extraParams`, `window.gBrowser`

## IPProtectionPanel.enroll()
- 位置: async L775-803
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.ipprotection.enrollment.record()`, `Glean.ipprotection.getStarted.record()`, `lazy.CustomizableUI.getPlacementOfWidget()`, `lazy.IPProtectionService.authProvider.enroll()`, `this.setState()`, `this.startLoginFlow()`
- 条件付き依存: `if (placement && !this.active)` → `this.open()`
- 参照: `IPProtectionPanel.WIDGET_ID`, `result?.error`, `result?.isEnrolledAndEntitled`, `this.active`

## IPProtectionPanel.showLocationSelector()
- 位置: async L813-863
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#createPanel()`, `this.panelMultiView?.showSubView()`, `view.addEventListener()`, `view.querySelectorAll()`, `view.removeEventListener()`
- 条件付き依存: `if (this.#locationsClosedByKeyboard)` → `locationButton?.focus()`
- 条件付き依存: `if (keyboardActivated)` → `view.querySelector()`
- 条件付き依存: `if (keyboardActivated)` → `listTabStop?.focus()`
- 参照: `IPProtectionPanel.LOCATIONS_PANELVIEW`, `IPProtectionPanel.LOCATIONS_TAGNAME`, `el.dataset.capturesFocus`, `this.#locationsClosedByKeyboard`, `this.#locationsKeyListener`, `this.locationsView`

## IPProtectionPanel.destroy()
- 位置: L868-901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `button.removeEventListener()`, `component.remove()`, `this.#panelView?.removeEventListener()`, `this.#removePanelListeners()`, `this.components.delete()`
- 条件付き依存: `if (this.state.error)` → `this.setState()`
- 条件付き依存: `if (this.state.error)` → `this.toolbarButton?.updateState()`
- 参照: `IPProtectionPanel.showHelpPage`, `this.#handleHeaderButtonKeypress`, `this.#headerButtons`, `this.#panelKeyListener`, `this.#panelView`, `this.components`, `this.panel`, `this.panel.ownerDocument`, `this.state.error`

## IPProtectionPanel.uninit()
- 位置: L903-908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removePrefObserver()`, `this.#removeProgressListener()`, `this.#removeProxyListeners()`, `this.destroy()`

## IPProtectionPanel.#addPanelListeners()
- 位置: L910-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.addEventListener()`
- 参照: `this.handleEvent`

## IPProtectionPanel.#removePanelListeners()
- 位置: L930-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.removeEventListener()`
- 参照: `this.handleEvent`

## IPProtectionPanel.#addProxyListeners()
- 位置: L956-985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.addEventListener()`, `lazy.IPPSiteRuleManager.addEventListener()`, `lazy.IPPUsageHelper.addEventListener()`, `lazy.IPProtectionServerlist.addEventListener()`, `lazy.IPProtectionService.addEventListener()`, `lazy.IPProtectionService.authProvider.addEventListener()`
- 参照: `this.handleEvent`

## IPProtectionPanel.#removeProxyListeners()
- 位置: L987-1016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.removeEventListener()`, `lazy.IPPSiteRuleManager.removeEventListener()`, `lazy.IPPUsageHelper.removeEventListener()`, `lazy.IPProtectionServerlist.removeEventListener()`, `lazy.IPProtectionService.authProvider.removeEventListener()`, `lazy.IPProtectionService.removeEventListener()`
- 参照: `this.handleEvent`

## IPProtectionPanel.#shouldShowBandwidthWarning()
- 位置: L1018-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPUsageHelper.getDismissedThresholds()`
- 参照: `lazy.IPPUsageHelper.getDismissedThresholds().panel`, `lazy.IPPUsageHelper.state`

## IPProtectionPanel.#addProgressListener()
- 位置: L1031-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.gBrowser)` → `this.gBrowser.addTabsProgressListener()`
- 参照: `this.gBrowser`, `this.progressListener`

## IPProtectionPanel.#removeProgressListener()
- 位置: L1037-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.gBrowser)` → `this.gBrowser.removeTabsProgressListener()`
- 参照: `this.gBrowser`, `this.progressListener`

## IPProtectionPanel.#addPrefObserver()
- 位置: L1043-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`
- 参照: `this.handlePrefChange`
- XPCOM: `Services.prefs`

## IPProtectionPanel.#removePrefObserver()
- 位置: L1055-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- 参照: `this.handlePrefChange`
- XPCOM: `Services.prefs`

## IPProtectionPanel.#handlePrefChange()
- 位置: L1067-1088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `this.#shouldShowBandwidthWarning()`, `this.setState()`
- 条件付き依存: `if (!this.#shouldShowBandwidthWarning())` → `this.setState()`
- XPCOM: `Services.prefs`

## IPProtectionPanel.#getSiteData()
- 位置: L1100-1110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSitePrincipal()`, `lazy.IPPSiteRuleManager.canManage()`, `lazy.IPPSiteRuleManager.getRule()`
- 参照: `lazy.IPPPrincipalRules.DEFAULT`, `lazy.IPPPrincipalRules.EXCLUDED`, `lazy.IPPPrincipalRules.INCLUDED`, `this.gBrowser`

## IPProtectionPanel.#getBandwidthUsage()
- 位置: L1120-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( lazy.BANDWIDTH_USAGE_ENABLED && lazy.IPPProxyManager.usageInfo?.max != null )` → `Number()`
- 条件付き依存: `if ( lazy.BANDWIDTH_USAGE_ENABLED && lazy.IPProtectionService.authProvider.maxBytes != null )` → `Number()`
- 参照: `lazy.BANDWIDTH_USAGE_ENABLED`, `lazy.IPPProxyManager.usageInfo.max`, `lazy.IPPProxyManager.usageInfo.remaining`, `lazy.IPPProxyManager.usageInfo.reset`, `lazy.IPPProxyManager.usageInfo?.max`, `lazy.IPProtectionService.authProvider.maxBytes`

## IPProtectionPanel.#updateSiteData()
- 位置: L1148-1151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSiteData()`, `this.setState()`

## IPProtectionPanel.#handleEvent()
- 位置: L1153-1341
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "IPProtection:Init")` → `this.updateComponentState()`
- 条件付き依存: `if (event.type == "IPProtection:Close")` → `this.close()`
- 条件付き依存: `if (event.type == "IPProtection:UserEnable")` → `this.#startProxy()`
- 条件付き依存: `if (event.type == "IPProtection:UserEnable")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (event.type == "IPProtection:UserEnable")` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (userEnableCount < 3)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (event.type == "IPProtection:UserDisable")` → `this.#stopProxy()`
- 条件付き依存: `if (event.type == "IPProtection:UserDisable")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (event.type == "IPProtection:ClickUpgrade")` → `this.close()`
- 条件付き依存: `if (event.type == "IPProtection:OptIn")` → `this.enroll()`
- 条件付き依存: `if ( event.type == "IPPProxyManager:StateChanged" || event.type == "IPProtectionService:StateChanged" || event.type === "IPPAuthProvider:StateChanged" )` → `this.setState()`
- 条件付き依存: `if ( event.type == "IPPProxyManager:StateChanged" || event.type == "IPProtectionService:StateChanged" || event.type === "IPPAuthProvider:StateChanged" )` → `this.#getBandwidthUsage()`
- 条件付き依存: `if ( event.type == "IPPProxyManager:StateChanged" || event.type == "IPProtectionService:StateChanged" || event.type === "IPPAuthProvider:StateChanged" )` → `this.#shouldShowBandwidthWarning()`
- 条件付き依存: `if (event.type == "SiteRuleManager:RuleChanged")` → `this.#updateSiteData()`
- 条件付き依存: `if (event.type == "IPProtectionServerlist:ListChanged")` → `this.setState()`
- 条件付き依存: `if (event.type == "IPProtection:UserEnableVPNForSite")` → `getSitePrincipal()`
- 条件付き依存: `if (event.type == "IPProtection:UserEnableVPNForSite")` → `lazy.IPPPermissionRules.setRule()`
- 条件付き依存: `if (event.type == "IPProtection:UserEnableVPNForSite")` → `Glean.ipprotection.exclusionToggled.record()`
- 条件付き依存: `if (event.type == "IPProtection:UserDisableVPNForSite")` → `getSitePrincipal()`
- 条件付き依存: `if (event.type == "IPProtection:UserDisableVPNForSite")` → `lazy.IPPPermissionRules.setRule()`
- 条件付き依存: `if (event.type == "IPProtection:UserDisableVPNForSite")` → `Glean.ipprotection.exclusionToggled.record()`
- 条件付き依存: `if (threshold > 0)` → `lazy.IPPUsageHelper.getDismissedThresholds()`
- 条件付き依存: `if (threshold > current.panel)` → `lazy.IPPUsageHelper.setDismissedThresholds()`
- 条件付き依存: `if (event.type == "IPProtection:DismissBandwidthWarning")` → `this.setState()`
- 条件付き依存: `if (usage.unlimited)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (usage.unlimited)` → `this.setState()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `Number()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (lastRecordedThreshold !== threshold)` → `this.#measureBandwidthThreshold()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `usage.reset.toString()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (threshold === 0 && lastResetDate && resetDate !== lastResetDate)` → `this.#sendBandwidthResetTrigger()`
- 条件付き依存: `if (event.type == "IPPProxyManager:UsageChanged")` → `this.setState()`
- 条件付き依存: `if (event.type == "IPPUsageHelper:StateChanged")` → `this.setState()`
- 条件付き依存: `if (event.type == "IPPUsageHelper:StateChanged")` → `this.#shouldShowBandwidthWarning()`
- 条件付き依存: `if (this.state.showLocationButtonBadge)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.state.showLocationButtonBadge)` → `this.setState()`
- 条件付き依存: `if (event.type == "IPProtection:UserShowLocations")` → `Glean.ipprotection.locationSelectorButtonClicked.record()`
- 条件付き依存: `if (event.type == "IPProtection:UserShowLocations")` → `this.showLocationSelector()`
- 条件付き依存: `if (event.type == "IPProtection:UserSelectLocation")` → `Glean.ipprotection.locationChanged.record()`
- 条件付き依存: `if (event.type == "IPProtection:UserSelectLocation")` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (lazy.IPPProxyManager.state === lazy.IPPProxyStates.ACTIVE)` → `lazy.IPPProxyManager.switch()`
- 条件付き依存: `if (event.type == "IPProtection:UserSelectLocation")` → `this.panelMultiView?.goBack()`
- 参照: `BANDWIDTH.FIRST_THRESHOLD`, `BANDWIDTH.SECOND_THRESHOLD`, `BANDWIDTH.THIRD_THRESHOLD`, `current.panel`, `event.detail`, `event.detail.usage`, `event.detail?.keyboardActivated`, `event.detail?.locationButton`, `event.target`, `event.target.documentGlobal`, `event.type`, `lazy.ERRORS.GENERIC`, `lazy.IPPPrincipalRules.DEFAULT`, `lazy.IPPPrincipalRules.EXCLUDED`, `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVATING`, `lazy.IPPProxyStates.ACTIVE`, `lazy.IPPProxyStates.ERROR`, `lazy.IPPProxyStates.PAUSED`, `lazy.IPPUsageHelper.state`, `lazy.IPProtectionServerlist.countries`, `lazy.IPProtectionService.authProvider.hasUpgraded`, `lazy.IPProtectionService.authProvider.isEnrolling`, `lazy.IPProtectionService.state`, `lazy.IPProtectionStates.READY`, `lazy.IPProtectionStates.UNAUTHENTICATED`, `this.initiatedUpgrade`, `this.state.showLocationButtonBadge`, `usage.max`, `usage.remaining`, `usage.reset`, `usage.unlimited`, `win?.gBrowser`
- XPCOM: `Services.prefs`

## IPProtectionPanel.#sendBandwidthResetTrigger()
- 位置: async L1343-1351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.ASRouter.sendTriggerMessage()`
- 参照: `lazy.ASRouter.waitForInitialized`, `win?.gBrowser?.selectedBrowser`
- XPCOM: `Services.wm`

## IPProtectionPanel.#measureBandwidthThreshold()
- 位置: L1353-1361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.ipprotection.bandwidthUsedThreshold.record()`
