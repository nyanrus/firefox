# browser/components/uitour/UITour.sys.mjs

source: browser/components/uitour/UITour.sys.mjs
source-hash: f258f90651baa263fb7fcdfea05e06ea6d6b61d2
lines: 2070

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Services.prefs.getBoolPref()`, `UITour.init()`

## clearAvailableTargetsCache()
- 位置: L75-77
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.availableTargetsCache`

## addTargetListener()
- 位置: L103-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelPopup.addEventListener()`
- 参照: `aDocument.defaultView.PanelUI.panel`

## removeTargetListener()
- 位置: L108-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelPopup.removeEventListener()`
- 参照: `aDocument.defaultView.PanelUI.panel`

## query()
- 位置: L159-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `aDocument.getElementById()`, `searchbar.querySelector()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("browser.search.widget.new"))` → `aDocument.getElementById()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("browser.search.widget.new"))` → `searchbar.querySelector()`
- XPCOM: `Services.prefs`

## query()
- 位置: L173-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UITour.isElementVisible()`
- 参照: `aDocument.defaultView.gBrowser.selectedTab`, `selectedtab.iconImage`

## query()
- 位置: L193-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDocument.getElementById()`
- 参照: `node.hidden`

## init()
- 位置: L209-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.obs.addObserver()`, `Services.urlFormatter.formatURLPref()`, `lazy.CustomizableUI.addListener()`, `lazy.log.debug()`, `listenerMethods.reduce()`
- 参照: `lazy.UIState.ON_UPDATE`, `this.url`
- XPCOM: `Services.obs` / `Services.urlFormatter`

## listener[method]()
- 位置: L228-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearAvailableTargetsCache()`

## getNodeFromDocument()
- 位置: L236-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDocument.getElementById()`, `aDocument.querySelector()`, `viewCacheTemplate.content.querySelector()`

## onPageEvent()
- 位置: L244-671
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `BACKGROUND_PAGE_ACTIONS_ALLOWED.has()`, `Promise.resolve()`, `Promise.resolve() .then()`, `Promise.resolve() .then(() => { return lazy.FxAccounts.canConnectAccount(); }) .then()`, `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`, `Services.scriptSecurityManager.createNullPrincipal()`, `browser.loadURI()`, `enginePromise.catch()`, `lazy.AIWindow.launchWindow()`, `lazy.AIWindow.launchWindow(browser, false, "bedrock").then()`, `lazy.AboutReaderParent.forceShowReaderIcon()`, `lazy.AboutReaderParent.toggleReaderMode()`, `lazy.FxAccounts.canConnectAccount()`, `lazy.FxAccounts.config .promiseConnectDeviceURI()`, `lazy.FxAccounts.config .promiseConnectDeviceURI("sync", data.entrypoint || "uitour") .then()`, `lazy.FxAccounts.config.promiseConnectAccountURI()`, `lazy.FxAccounts.config.promiseEmailURI()`, `lazy.ResetProfile.resetSupported()`, `lazy.log.debug()`, `targetPromise .then()`, `targetPromise .then(target => { this.addNavBarWidget(target, browser, data.callbackID); }) .catch()`, `targetPromise.then()`, `this._populateURLParams()`, `this.addNavBarWidget()`, `this.getConfiguration()`, `this.getTarget()`, `this.hideHighlight()`, `this.hideInfo()`, `this.hideMenu()`, `this.highlightEffects.includes()`, `this.noautohideMenus.add()`, `this.noautohideMenus.delete()`, `this.selectSearchEngine()`, `this.sendPageCallback()`, `this.setConfiguration()`, `this.showHighlight()`, `this.showHome()`, `this.showInfo()`, `this.showMenu()`, `this.showNewTab()`, `this.showProtectionReport()`, `window.getShellService()`, `window.openPreferences()`
- 条件付き依存: `if (!window.gBrowser)` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (typeof aEvent.detail != "object")` → `lazy.log.warn()`
- 条件付き依存: `if (typeof action != "string" || !action)` → `lazy.log.warn()`
- 条件付き依存: `if (typeof data != "object")` → `lazy.log.warn()`
- 条件付き依存: `if ( (aEvent.pageVisibilityState == "hidden" || aEvent.pageVisibilityState == "unloaded") && !BACKGROUND_PAGE_ACTIONS_ALLOWED.has(action) )` → `lazy.log.warn()`
- 条件付き依存: `if (!target.node)` → `lazy.log.error()`
- 条件付き依存: `if (typeof data.icon == "string")` → `this.resolveURL()`
- 条件付き依存: `if (typeof buttonData.icon == "string")` → `this.resolveURL()`
- 条件付き依存: `if ( typeof buttonData == "object" && typeof buttonData.label == "string" && typeof buttonData.callbackID == "string" )` → `buttons.push()`
- 条件付き依存: `if (buttons.length == MAX_BUTTONS)` → `lazy.log.warn()`
- 条件付き依存: `if (typeof data.showCallbackID == "string")` → `this.sendPageCallback()`
- 条件付き依存: `if (typeof data.configuration != "string")` → `lazy.log.warn()`
- 条件付き依存: `if (typeof data.pane != "string" && typeof data.pane != "undefined")` → `lazy.log.warn()`
- 条件付き依存: `if (!canConnect)` → `lazy.log.warn()`
- 条件付き依存: `if (!this._populateURLParams(url, data.extraURLParams))` → `lazy.log.warn()`
- 条件付き依存: `if (AppConstants.IS_ESR)` → `lazy.log.warn()`
- 条件付き依存: `if (lazy.AIWindow.isBlocked)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!success)` → `lazy.log.warn()`
- 条件付き依存: `if (lazy.ResetProfile.resetSupported())` → `lazy.ResetProfile.openConfirmationDialog()`
- 条件付き依存: `if (shell)` → `shell.pinToTaskbar().catch()`
- 条件付き依存: `if (shell)` → `shell.pinToTaskbar()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("browser.search.widget.new"))` → `searchbar.updateGoButtonVisibility()`
- 条件付き依存: `if (typeof data.callbackID == "string")` → `this.sendPageCallback()`
- 条件付き依存: `if (tabBrowser && tabBrowser.browsers.length > 1)` → `tabBrowser.removeTab()`
- 条件付き依存: `if (tabBrowser && tabBrowser.browsers.length > 1)` → `tabBrowser.getTabForBrowser()`
- 条件付き依存: `if (action != "getConfiguration")` → `this.initForBrowser()`
- 参照: `AppConstants.IS_ESR`, `aEvent.detail`, `aEvent.detail.action`, `aEvent.detail.data`, `aEvent.pageVisibilityState`, `browser.documentGlobal`, `browser.documentGlobal.gBrowser`, `button.iconURL`, `button.style`, `buttonData.callbackID`, `buttonData.icon`, `buttonData.label`, `buttonData.style`, `buttons.length`, `console.error`, `data.buttons`, `data.buttons.length`, `data.callbackID`, `data.closeButtonCallbackID`, `data.configuration`, `data.effect`, `data.email`, `data.entrypoint`, `data.extraURLParams`, `data.hash`, `data.icon`, `data.identifier`, `data.name`, `data.pane`, `data.showCallbackID`, `data.target`, `data.targetCallbackID`, `data.term`, `data.text`, `data.title`, `data.value`, `data.wallpaper`, `infoOptions.closeButtonCallback`, `infoOptions.targetCallback`, `lazy.AIWindow.isBlocked`, `lazy.log.error`, `searchbar.value`, `tabBrowser.browsers.length`, `target.node`, `url.URI`, `window.gBrowser`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager` / `Services.wm`

## callback()
- 位置: L345-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendPageCallback()`

## infoOptions.closeButtonCallback()
- 位置: L372-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendPageCallback()`
- 参照: `data.closeButtonCallbackID`

## infoOptions.targetCallback()
- 位置: L377-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendPageCallback()`
- 参照: `data.targetCallbackID`

## initForBrowser()
- 位置: L673-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tourBrowsersByWindow.get()`, `this.tourBrowsersByWindow.get(window).add()`, `this.tourBrowsersByWindow.has()`, `window.addEventListener()`
- 条件付き依存: `if (gBrowser)` → `gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (!this.tourBrowsersByWindow.has(window))` → `this.tourBrowsersByWindow.set()`
- 条件付き依存: `if (!this._initForBrowserObserverAdded)` → `Services.obs.addObserver()`
- 参照: `this._initForBrowserObserverAdded`, `window.gBrowser`
- XPCOM: `Services.obs`

## handleEvent()
- 位置: L692-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.teardownTourForWindow()`
- 条件付き依存: `if (aEvent.detail && aEvent.detail.previousTab)` → `this.tourBrowsersByWindow.get()`
- 条件付き依存: `if (aEvent.detail && aEvent.detail.previousTab)` → `openTourWindows.has()`
- 条件付き依存: `if (openTourWindows.has(previousTab.linkedBrowser))` → `this.teardownTourForBrowser()`
- 参照: `aEvent.detail`, `aEvent.detail.previousTab`, `aEvent.target`, `aEvent.target.documentGlobal`, `aEvent.type`, `previousTab.linkedBrowser`

## observe()
- 位置: L722-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `lazy.UIState.get()`, `lazy.log.debug()`, `this.notify()`, `this.tourBrowsersByWindow.get()`
- 条件付き依存: `if (!messageManager || aSubject == messageManager)` → `this.teardownTourForBrowser()`
- 参照: `browser.messageManager`, `lazy.UIState.ON_UPDATE`, `syncState.status`, `window.closed`
- XPCOM: `Services.wm`

## _populateURLParams()
- 位置: L760-830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.warn()`
- 条件付き依存: `if (typeof extraURLParams != "string")` → `lazy.log.warn()`
- 条件付き依存: `if (extraURLParams)` → `JSON.parse()`
- 条件付き依存: `if (typeof urlParams != "object")` → `lazy.log.warn()`
- 条件付き依存: `if (urlParams)` → `urlParams.flow_begin_time.toString()`
- 条件付き依存: `if ( (urlParams.flow_begin_time && urlParams.flow_begin_time.toString().length !== FLOW_BEGIN_TIME_LENGTH) || (urlParams.flow_id && urlParams.flow_id.length !== ...)` → `lazy.log.warn()`
- 条件付き依存: `if (urlParams)` → `name.startsWith()`
- 条件付き依存: `if (urlParams)` → `reSimpleString.test()`
- 条件付き依存: `if ( typeof name != "string" || !validName || !reSimpleString.test(name) )` → `lazy.log.warn()`
- 条件付き依存: `if (urlParams)` → `url.searchParams.append()`
- 参照: `urlParams.flow_begin_time`, `urlParams.flow_begin_time.toString().length`, `urlParams.flow_id`, `urlParams.flow_id.length`

## teardownTourForBrowser()
- 位置: async L834-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.hideHighlight()`, `this.hideInfo()`, `this.noautohideMenus.clear()`, `this.removePanelListeners()`, `this.tourBrowsersByWindow.get()`
- 条件付き依存: `if (aTourPageClosing && openTourBrowsers)` → `openTourBrowsers.delete()`
- 条件付き依存: `if (!openTourBrowsers || openTourBrowsers.size == 0)` → `this.teardownTourForWindow()`
- 参照: `openTourBrowsers.size`

## removePanelListeners()
- 位置: async L862-886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.node.removeEventListener()`
- 条件付き依存: `if (panel.node.state != "closed")` → `panel.node.addEventListener()`
- 条件付き依存: `if (panel.node.state != "closed")` → `this.hideMenu()`
- 参照: `aWindow.PanelUI.panel`, `panel.events`, `panel.name`, `panel.node.state`, `this.onAppMenuHiding`, `this.onAppMenuSubviewShowing`, `this.onPanelHidden`

## teardownTourForWindow()
- 位置: L891-897
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.gBrowser.tabContainer.removeEventListener()`, `aWindow.removeEventListener()`, `lazy.log.debug()`, `this.tourBrowsersByWindow.delete()`

## isSafeScheme()
- 位置: L900-908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowedSchemes.has()`
- 条件付き依存: `if (!allowedSchemes.has(aURI.scheme))` → `lazy.log.error()`
- 参照: `aURI.scheme`

## resolveURL()
- 位置: L910-922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `this.isSafeScheme()`
- 参照: `aBrowser.currentURI`, `uri.spec`
- XPCOM: `Services.io`

## sendPageCallback()
- 位置: L924-931
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `global.getActor()`, `lazy.log.debug()`
- 参照: `aBrowser.browsingContext`, `contextToVisit.currentWindowGlobal`

## isElementVisible()
- 位置: L933-940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElement.documentGlobal.getComputedStyle()`
- 参照: `aElement.ownerDocument.hidden`, `targetStyle.display`, `targetStyle.visibility`

## getTarget()
- 位置: L942-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.PanelUI.ensureReady()`, `aWindow.PanelUI.ensureReady() .then()`, `lazy.log.debug()`, `resolve()`, `this.targets.get()`
- 条件付き依存: `if (typeof aTargetName != "string" || !aTargetName)` → `lazy.log.warn()`
- 条件付き依存: `if (typeof aTargetName != "string" || !aTargetName)` → `Promise.reject()`
- 条件付き依存: `if (!targetObject)` → `lazy.log.warn()`
- 条件付き依存: `if (!targetObject)` → `Promise.reject()`
- 条件付き依存: `if (typeof targetQuery == "function")` → `targetQuery()`
- 条件付き依存: `if (typeof targetQuery == "function")` → `lazy.log.warn()`
- 条件付き依存: `if (!(typeof targetQuery == "function"))` → `this.getNodeFromDocument()`
- 参照: `aWindow.document`, `lazy.log.error`, `targetObject.addTargetListener`, `targetObject.allowAdd`, `targetObject.infoPanelOffsetX`, `targetObject.infoPanelOffsetY`, `targetObject.infoPanelPosition`, `targetObject.query`, `targetObject.removeTargetListener`, `targetObject.widgetName`

## targetIsInAppMenu()
- 位置: L991-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `targetElement.id.startsWith()`
- 条件付き依存: `if (aTarget.widgetName)` → `doc.getElementById()`
- 条件付き依存: `if (aTarget.widgetName)` → `lazy.PanelMultiView.getViewNode()`
- 参照: `aTarget.node`, `aTarget.node.documentGlobal.document`, `aTarget.widgetName`

## _setMenuStateForAnnotation()
- 位置: L1012-1046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (aShouldOpen == panelIsOpen)` → `lazy.log.debug()`
- 条件付き依存: `if (aShouldOpen == panelIsOpen)` → `Promise.resolve()`
- 条件付き依存: `if (aShouldOpen)` → `lazy.log.debug()`
- 条件付き依存: `if (aShouldOpen)` → `this.showMenu()`
- 条件付き依存: `if (!(aShouldOpen))` → `this.noautohideMenus.has()`
- 条件付き依存: `if (!this.noautohideMenus.has("appMenu"))` → `lazy.log.debug()`
- 条件付き依存: `if (!this.noautohideMenus.has("appMenu"))` → `menu.addEventListener()`
- 条件付き依存: `if (!this.noautohideMenus.has("appMenu"))` → `this.hideMenu()`
- 参照: `aWindow.PanelUI.panel`, `menu.state`

## _ensureTarget()
- 位置: async L1055-1087
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `aTarget.node.closest()`, `this.isElementVisible()`, `this.targetIsInAppMenu()`
- 条件付き依存: `if ( !aTarget.node.closest("panelview") && !this.isElementVisible(aTarget.node) )` → `Promise.reject()`
- 条件付き依存: `if (!shouldOpenAppMenu)` → `menuClosePromises.push()`
- 条件付き依存: `if (!shouldOpenAppMenu)` → `this._setMenuStateForAnnotation()`
- 条件付き依存: `if (shouldOpenAppMenu)` → `this._setMenuStateForAnnotation()`
- 参照: `aTarget.name`, `aTarget.node`, `aTarget.targetName`

## _correctAnchor()
- 位置: async L1098-1114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.closest()`, `this.getTarget()`
- 条件付き依存: `if (node.closest("#widget-overflow-mainView"))` → `lazy.CustomizableUI.getWidget(node.id).forWindow()`
- 条件付き依存: `if (node.closest("#widget-overflow-mainView"))` → `lazy.CustomizableUI.getWidget()`
- 参照: `aTarget.node`, `aTarget.targetName`, `lazy.CustomizableUI.getWidget(node.id).forWindow(aChromeWindow) .anchor`, `node.id`, `refreshedTarget.node`

## showHighlight()
- 位置: async L1129-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.warn()`, `showHighlightElement()`, `this._correctAnchor()`, `this._ensureTarget()`

## showHighlightElement()
- 位置: L1130-1203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `aChromeWindow.getComputedStyle()`, `highlightAnchor.classList.contains()`, `highlightAnchor.getAttribute()`, `highlightAnchor.getBoundingClientRect()`, `highlightWindow.getComputedStyle()`, `highlighter.parentElement.openPopup()`, `highlighter.parentElement.setAttribute()`, `highlighter.setAttribute()`, `parseFloat()`, `this._addAnnotationPanelMutationObserver()`, `this.getHighlightAndMaybeCreate()`, `this.targetIsInAppMenu()`
- 条件付き依存: `if (effect == "random")` → `Math.floor()`
- 条件付き依存: `if (effect == "random")` → `Math.random()`
- 条件付き依存: `if (this.targetIsInAppMenu(aTarget))` → `highlighter.classList.remove()`
- 条件付き依存: `if (!(this.targetIsInAppMenu(aTarget)))` → `highlighter.classList.add()`
- 条件付き依存: `if ( highlighter.parentElement.state == "showing" || highlighter.parentElement.state == "open" )` → `lazy.log.debug()`
- 条件付き依存: `if ( highlighter.parentElement.state == "showing" || highlighter.parentElement.state == "open" )` → `highlighter.parentElement.hidePopup()`
- 参照: `aChromeWindow.document`, `aChromeWindow.getComputedStyle(highlighter).animationName`, `aTarget.targetName`, `highlightStyle.minHeight`, `highlightStyle.minWidth`, `highlighter.parentElement`, `highlighter.parentElement.hidden`, `highlighter.parentElement.state`, `highlighter.style.height`, `highlighter.style.width`, `targetRect.height`, `targetRect.width`, `this.highlightEffects`, `this.highlightEffects.length`

## _hideHighlightElement()
- 位置: L1214-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `highlighter.parentElement.hidePopup()`, `highlighter.removeAttribute()`, `this._removeAnnotationPanelMutationObserver()`, `this.getHighlightAndMaybeCreate()`
- 参照: `aWindow.document`, `highlighter.parentElement`

## hideHighlight()
- 位置: L1221-1224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideHighlightElement()`, `this._setMenuStateForAnnotation()`

## showInfo()
- 位置: async L1239-1363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.warn()`, `showInfoElement()`, `this._correctAnchor()`, `this._ensureTarget()`

## showInfoElement()
- 位置: L1248-1354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aAnchorEl.focus()`, `document.createXULElement()`, `document.getElementById()`, `el.setAttribute()`, `this._addAnnotationPanelMutationObserver()`, `this.getTooltipAndMaybeCreate()`, `tooltip.addEventListener()`, `tooltip.openPopup()`, `tooltip.setAttribute()`, `tooltipButtons.appendChild()`, `tooltipButtons.firstChild.remove()`, `tooltipClose.addEventListener()`, `tooltipClose.removeEventListener()`
- 条件付き依存: `if (tooltip.state == "showing" || tooltip.state == "open")` → `tooltip.hidePopup()`
- 条件付き依存: `if (button.iconURL)` → `el.setAttribute()`
- 条件付き依存: `if (button.style == "link")` → `el.setAttribute()`
- 条件付き依存: `if (button.style == "primary")` → `el.setAttribute()`
- 条件付き依存: `if (isButton)` → `el.addEventListener()`
- 条件付き依存: `if (isButton)` → `tooltip.hidePopup()`
- 条件付き依存: `if (isButton)` → `callback()`
- 条件付き依存: `if (aOptions.targetCallback && aAnchor.addTargetListener)` → `aAnchor.addTargetListener()`
- 条件付き依存: `if (aOptions.targetCallback && aAnchor.removeTargetListener)` → `aAnchor.removeTargetListener()`
- 条件付き依存: `if (tooltip.state == "closed")` → `document.defaultView.addEventListener()`
- 条件付き依存: `if (tooltip.state == "closed")` → `tooltip.openPopup()`
- 参照: `aAnchor.addTargetListener`, `aAnchor.infoPanelPosition`, `aAnchor.removeTargetListener`, `aAnchor.targetName`, `aButtons.length`, `aChromeWindow.document`, `aOptions.targetCallback`, `button.callback`, `button.iconURL`, `button.label`, `button.style`, `tooltip.state`, `tooltipButtons.firstChild`, `tooltipButtons.hidden`, `tooltipDesc.textContent`, `tooltipIcon.hidden`, `tooltipIcon.src`, `tooltipTitle.textContent`

## closeButtonCallback()
- 位置: L1304-1309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideInfo()`
- 条件付き依存: `if (aOptions && aOptions.closeButtonCallback)` → `aOptions.closeButtonCallback()`
- 参照: `aOptions.closeButtonCallback`, `document.defaultView`

## targetCallback()
- 位置: L1312-1318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aOptions.targetCallback()`
- 参照: `aAnchor.targetName`, `event.type`

## getHighlightContainerAndMaybeCreate()
- 位置: L1365-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!highlightContainer)` → `document.getElementById()`
- 条件付き依存: `if (!highlightContainer)` → `wrapper.replaceWith()`
- 参照: `wrapper.content`

## getTooltipAndMaybeCreate()
- 位置: L1378-1386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!tooltip)` → `document.getElementById()`
- 条件付き依存: `if (!tooltip)` → `wrapper.replaceWith()`
- 参照: `wrapper.content`

## getHighlightAndMaybeCreate()
- 位置: L1388-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!highlight)` → `document.getElementById()`
- 条件付き依存: `if (!highlight)` → `wrapper.replaceWith()`
- 参照: `wrapper.content`

## isInfoOnTarget()
- 位置: L1398-1405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTooltipAndMaybeCreate()`, `tooltip.getAttribute()`
- 参照: `aChromeWindow.document`, `tooltip.state`

## _hideInfoElement()
- 位置: L1407-1416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._removeAnnotationPanelMutationObserver()`, `this.getTooltipAndMaybeCreate()`, `tooltip.hidePopup()`, `tooltipButtons.firstChild.remove()`
- 参照: `aWindow.document`, `tooltipButtons.firstChild`

## hideInfo()
- 位置: L1418-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideInfoElement()`, `this._setMenuStateForAnnotation()`

## showMenu()
- 位置: L1423-1485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (!aOptions.autohide)` → `menu.node.setAttribute()`
- 条件付き依存: `if (menu.node.state != "open")` → `this.recreatePopup()`
- 条件付き依存: `if (aOpenCallback)` → `menu.node.addEventListener()`
- 条件付き依存: `if (aMenuName == "appMenu")` → `menu.node.addEventListener()`
- 条件付き依存: `if (aMenuName == "appMenu")` → `menu.show()`
- 条件付き依存: `if (aMenuName == "bookmarks")` → `aWindow.document.getElementById()`
- 条件付き依存: `if (aMenuName == "bookmarks")` → `openMenuButton()`
- 条件付き依存: `if (aOpenCallback)` → `urlbar.panel.addEventListener()`
- 条件付き依存: `if (aMenuName == "urlbar")` → `urlbar.focus()`
- 条件付き依存: `if (aMenuName == "urlbar")` → `urlbar.select()`
- 条件付き依存: `if (aMenuName == "urlbar")` → `urlbar.startQuery()`
- 参照: `aOptions.autohide`, `aWindow.PanelUI.panel`, `aWindow.gURLBar`, `menu.node`, `menu.node.state`, `menu.onPanelHidden`, `menu.onPopupHiding`, `menu.onViewShowing`, `menu.show`, `this.onAppMenuHiding`, `this.onAppMenuSubviewShowing`, `this.onPanelHidden`, `urlbar.value`

## openMenuButton()
- 位置: L1425-1436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aMenuBtn.hasMenu()`, `aMenuBtn.openMenu()`
- 条件付き依存: `if (aOpenCallback)` → `aOpenCallback()`
- 条件付き依存: `if (aOpenCallback)` → `aMenuBtn.addEventListener()`
- 参照: `aMenuBtn.open`

## menu.show()
- 位置: L1445-1445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.PanelUI.show()`

## hideMenu()
- 位置: L1487-1503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (aMenuName == "appMenu")` → `aWindow.PanelUI.hide()`
- 条件付き依存: `if (aMenuName == "bookmarks")` → `aWindow.document.getElementById()`
- 条件付き依存: `if (aMenuName == "bookmarks")` → `closeMenuButton()`
- 条件付き依存: `if (aMenuName == "urlbar")` → `aWindow.gURLBar.view.close()`

## closeMenuButton()
- 位置: L1489-1493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aMenuBtn.hasMenu()`
- 条件付き依存: `if (aMenuBtn && aMenuBtn.hasMenu())` → `aMenuBtn.openMenu()`

## _showPage()
- 位置: L1506-1520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^[a-zA-Z0-9_-]+$/.test()`, `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`, `aWindow.gURLBar.focus()`, `aWindow.openLinkIn()`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## showNewTab()
- 位置: L1522-1524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._showPage()`

## showHome()
- 位置: L1526-1528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._showPage()`

## showProtectionReport()
- 位置: L1530-1540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`, `aWindow.openLinkIn()`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## _hideAnnotationsForPanel()
- 位置: L1542-1582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `annotationElements.forEach()`, `this.getHighlightContainerAndMaybeCreate()`, `this.getTooltipAndMaybeCreate()`
- 条件付き依存: `if (annotationElement.state != "closed")` → `annotationElement.getAttribute()`
- 条件付き依存: `if (annotationElement.state != "closed")` → `UITour.getTarget(win, targetName) .then()`
- 条件付き依存: `if (annotationElement.state != "closed")` → `UITour.getTarget()`
- 条件付き依存: `if (annotationElement.state != "closed")` → `aTargetPositionCallback()`
- 条件付き依存: `if (annotationElement.state != "closed")` → `hideMethod()`
- 参照: `aEvent.target.documentGlobal`, `aTarget.targetName`, `annotationElement.state`, `lazy.log.error`, `win.document`

## hideHighlightMethod()
- 位置: L1547-1547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideHighlight()`

## hideInfoMethod()
- 位置: L1548-1548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideInfo()`

## hideHighlightMethod()
- 位置: L1551-1551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideHighlightElement()`

## hideInfoMethod()
- 位置: L1552-1552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideInfoElement()`

## onAppMenuHiding()
- 位置: L1584-1586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UITour._hideAnnotationsForPanel()`
- 参照: `UITour.targetIsInAppMenu`

## onAppMenuSubviewShowing()
- 位置: L1588-1590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UITour._hideAnnotationsForPanel()`
- 参照: `UITour.targetIsInAppMenu`

## onPanelHidden()
- 位置: L1592-1596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UITour.clearAvailableTargetsCache()`, `UITour.recreatePopup()`, `aEvent.target.removeAttribute()`
- 参照: `aEvent.target`

## recreatePopup()
- 位置: L1598-1610
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aPanel.clientWidth`, `aPanel.hidden`

## getConfiguration()
- 位置: L1612-1720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`, `engines .filter()`, `engines .filter( engine => engine instanceof lazy.AppProvidedConfigEngine ) .map()`, `lazy.ResetProfile.resetSupported()`, `lazy.SearchService.getVisibleEngines()`, `lazy.SearchService.getVisibleEngines() .then()`, `lazy.log.error()`, `this.getAppInfo()`, `this.getAvailableTargets()`, `this.getFxA()`, `this.getFxAConnections()`, `this.sendPageCallback()`
- 参照: `defaultEngine.id`, `engine.id`, `lazy.AppProvidedConfigEngine`, `lazy.SearchService`
- XPCOM: `Services.prefs`

## setConfiguration()
- 位置: async L1722-1740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.getShellService()`, `lazy.log.error()`
- 条件付き依存: `if (shell)` → `shell.setDefaultBrowser()`

## getFxA()
- 位置: L1745-1782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `lazy.fxAccounts.getSignedInUser()`, `lazy.fxAccounts.hasLocalSession()`, `lazy.log.error()`, `this.sendPageCallback()`
- 条件付き依存: `if (!setup)` → `this.sendPageCallback()`
- 条件付き依存: `if (hasSync)` → `Services.prefs.getIntPref()`
- 参照: `result.accountStateOK`, `result.browserServices`, `result.browserServices.sync`
- XPCOM: `Services.prefs`

## getFxAConnections()
- 位置: L1787-1843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `attachedClients .filter()`, `attachedClients .filter(c => !!c.id) .reduce()`, `lazy.fxAccounts.getSignedInUser()`, `lazy.fxAccounts.listAttachedOAuthClients()`, `lazy.log.error()`, `lazy.log.warn()`, `this.sendPageCallback()`
- 条件付き依存: `if (!setup)` → `this.sendPageCallback()`
- 条件付き依存: `if (!devices)` → `lazy.fxAccounts.device.refreshDeviceList()`
- 条件付き依存: `if (!devices)` → `lazy.log.warn()`
- 条件付き依存: `if (devices)` → `Math.max()`
- 条件付き依存: `if (devices)` → `devices .filter(d => !d.isCurrentDevice) .reduce()`
- 条件付き依存: `if (devices)` → `devices .filter()`
- 参照: `c.id`, `c.lastAccessedDaysAgo`, `d.isCurrentDevice`, `d.type`, `devices.length`, `lazy.fxAccounts.device.recentDeviceList`, `result.accountServices`, `result.numDevicesByType`, `result.numOtherDevices`

## getAppInfo()
- 位置: L1845-1916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs .getDefaultBranch()`, `Services.prefs .getDefaultBranch("distribution.") .getCharPref()`, `aWindow.getShellService()`, `lazy.ProfileAge()`, `lazy.UpdateUtils.getUpdateChannel()`, `lazy.log.error()`, `this.sendPageCallback()`
- 条件付き依存: `if (shell)` → `shell.isDefaultBrowser()`
- 条件付き依存: `if (shell)` → `shell.doesAppNeedPin()`
- 条件付き依存: `if (AppConstants.platform == "linux")` → `aWindow.getShellService()`
- 条件付き依存: `if (resetDate)` → `Math.floor()`
- 条件付き依存: `if (resetDate)` → `Date.now()`
- 参照: `AppConstants.platform`, `Services.appinfo.version`, `appinfo.canSetDefaultBrowserInBackground`, `appinfo.defaultBrowser`, `appinfo.defaultUpdateChannel`, `appinfo.distribution`, `appinfo.needsPin`, `appinfo.previousSessionEnd`, `appinfo.profileCreatedWeeksAgo`, `appinfo.profileResetWeeksAgo`, `lazy.ASRouter.state.previousSessionEnd`, `lazy.ASRouter.waitForInitialized`, `profileAge.created`, `profileAge.reset`
- XPCOM: `Services.appinfo` / `Services.prefs`

## getAvailableTargets()
- 位置: L1918-1955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.log.error()`, `promises.push()`, `this.availableTargetsCache.get()`, `this.availableTargetsCache.set()`, `this.getTarget()`, `this.sendPageCallback()`, `this.targets.keys()`
- 条件付き依存: `if (data)` → `lazy.log.debug()`
- 条件付き依存: `if (data)` → `data.targets.join()`
- 条件付き依存: `if (data)` → `this.sendPageCallback()`
- 条件付き依存: `if (targetObject.node)` → `targetNames.push()`
- 参照: `targetObject.node`, `targetObject.targetName`

## addNavBarWidget()
- 位置: L1957-1990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `lazy.CustomizableUI.addWidgetToArea()`, `this.sendPageCallback()`
- 条件付き依存: `if (aTarget.node)` → `lazy.log.error()`
- 条件付き依存: `if (!aTarget.allowAdd)` → `lazy.log.error()`
- 条件付き依存: `if (!aTarget.widgetName)` → `lazy.log.error()`
- 参照: `aTarget.allowAdd`, `aTarget.node`, `aTarget.widgetName`, `lazy.CustomizableUI.AREA_NAVBAR`

## _addAnnotationPanelMutationObserver()
- 位置: L1992-2007
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "linux")` → `this._annotationPanelMutationObservers.get()`
- 条件付き依存: `if (AppConstants.platform == "linux")` → `this._annotationPanelMutationObservers.set()`
- 条件付き依存: `if (AppConstants.platform == "linux")` → `observer.observe()`
- 参照: `AppConstants.platform`, `aPanelEl.documentGlobal`, `this._annotationMutationCallback`, `win.MutationObserver`

## _removeAnnotationPanelMutationObserver()
- 位置: L2009-2017
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "linux")` → `this._annotationPanelMutationObservers.get()`
- 条件付き依存: `if (observer)` → `observer.disconnect()`
- 条件付き依存: `if (observer)` → `this._annotationPanelMutationObservers.delete()`
- 参照: `AppConstants.platform`

## _annotationMutationCallback()
- 位置: L2024-2031
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mutation.target.removeAttribute()`

## selectSearchEngine()
- 位置: async L2033-2042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.SearchService.setDefault()`
- 参照: `engine.hidden`, `lazy.SearchService.CHANGE_REASON.UITOUR`

## notify()
- 位置: L2044-2066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `actor.sendAsyncMessage()`, `global.getActor()`, `this.tourBrowsersByWindow.get()`
- 参照: `browser.browsingContext`, `contextToVisit.currentWindowGlobal`, `window.closed`
- XPCOM: `Services.wm`
