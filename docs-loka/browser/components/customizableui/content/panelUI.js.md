# browser/components/customizableui/content/panelUI.js

source: browser/components/customizableui/content/panelUI.js
source-hash: fb77346559b4c285a40418e5ec2bf83db64564fd
lines: 1435

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineConstant()`

## cloneHelpMenuItem()
- 位置: L60-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.classList.add()`, `document.createXULElement()`, `node.getAttribute()`, `node.hasAttribute()`
- 条件付き依存: `if (node.hasAttribute(attrName))` → `button.setAttribute()`
- 条件付き依存: `if (node.hasAttribute(attrName))` → `node.getAttribute()`
- 条件付き依存: `if (l10nId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (node.id == "help_reportBrokenSite")` → `button.removeAttribute()`
- 条件付き依存: `if (node.id == "help_reportBrokenSite")` → `button.classList.add()`
- 条件付き依存: `if (node.id == "help_reportBrokenSite")` → `button.setAttribute()`
- 参照: `button.id`, `node.id`

## kEvents()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)

## kNotificationEvents()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)

## kElements()
- 位置: L108-117
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: L123-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `CustomizableUI.registerPanelNode()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `this._initElements()`, `this._showAIMenuItem()`, `this._showReferralsMenuItem()`, `this._showTabGroupsMenuItem()`, `this.menuButton.addEventListener()`, `this.updateNotifications()`, `this.updateOverflowStatus()`, `window.addEventListener()`
- 条件付き依存: `if (newValue)` → `window.removeEventListener()`
- 条件付き依存: `if (newValue)` → `window.addEventListener()`
- 条件付き依存: `if (!(newValue))` → `window.addEventListener()`
- 条件付き依存: `if (!(newValue))` → `window.removeEventListener()`
- 条件付き依存: `if (this.autoHideToolbarInFullScreen)` → `window.addEventListener()`
- 条件付き依存: `if (!(this.autoHideToolbarInFullScreen))` → `window.addEventListener()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `Services.appinfo.OS`, `this._initialized`, `this.autoHideToolbarInFullScreen`, `this.overflowFixedList`, `this.overflowFixedList.hidden`, `this.overflowFixedList.previousElementSibling.hidden`
- XPCOM: `Services.appinfo` / `Services.obs`

## _initElements()
- 位置: L243-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `this.__defineGetter__()`
- 参照: `this.kElements`

## _ensureEventListenersAdded()
- 位置: L256-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addEventListeners()`
- 参照: `this._eventListenersAdded`

## _addEventListeners()
- 位置: L263-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelMultiView.getViewNode( document, "appMenu-libraryView" ).addEventListener()`, `helpView.addEventListener()`, `this._onLibraryCommand.bind()`, `this.mainView.addEventListener()`, `this.panel.addEventListener()`
- 参照: `this._eventListenersAdded`, `this._onHelpCommand`, `this._onHelpViewShow`, `this._onLibraryCommand`, `this._onMainViewShow`, `this.kEvents`

## _removeEventListeners()
- 位置: L282-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelMultiView.getViewNode( document, "appMenu-libraryView" ).removeEventListener()`, `helpView.removeEventListener()`, `this.mainView.removeEventListener()`, `this.panel.removeEventListener()`
- 参照: `this._eventListenersAdded`, `this._onHelpCommand`, `this._onHelpViewShow`, `this._onLibraryCommand`, `this.kEvents`

## uninit()
- 位置: L298-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `Services.obs.removeObserver()`, `this._removeEventListeners()`, `this.menuButton.removeEventListener()`, `window.removeEventListener()`
- 条件付き依存: `if (this._notificationPanel)` → `this.notificationPanel.removeEventListener()`
- 参照: `this._notificationPanel`, `this.kEvents`, `this.kNotificationEvents`
- XPCOM: `Services.obs`

## toggle()
- 位置: L330-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`, `this._ensureEventListenersAdded()`
- 条件付き依存: `if (this.panel.state == "open")` → `this.hide()`
- 条件付き依存: `if (this.panel.state == "closed")` → `this.show()`
- 参照: `this.panel.state`

## show()
- 位置: L351-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.openPopup()`, `document.documentElement.hasAttribute()`, `this._ensureShortcutsShown()`, `this._getPanelAnchor()`, `this.ensureReady()`
- 条件付き依存: `if (ASRouter.initialized)` → `ASRouter.sendTriggerMessage()`
- 参照: `ASRouter.initialized`, `MenuMessage.SOURCES.APP_MENU`, `aEvent.type`, `console.error`, `gBrowser.selectedBrowser`, `this.menuButton`, `this.panel`, `this.panel.state`

## hide()
- 位置: L386-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `document.documentElement.hasAttribute()`
- 参照: `this.panel`

## observe()
- 位置: L394-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openAboutDialog()`, `this.updateNotifications()`
- 条件付き依存: `if (subject == window)` → `this._showAIMenuItem()`
- 条件付き依存: `if (this._notifications)` → `this.updateNotifications()`
- 参照: `AppMenuNotifications.notifications`, `this._notifications`

## handleEvent()
- 位置: L421-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.preventDefault()`, `aEvent.target.closest()`, `aEvent.type.startsWith()`, `this._onNotificationButtonEvent()`, `this._updatePanelButton()`, `this.onCommand()`, `this.updateNotifications()`, `updateEditUIVisibility()`
- 条件付き依存: `if (aEvent.type == "popupshown")` → `CustomizableUI.addPanelCloseListeners()`
- 条件付き依存: `if (aEvent.type == "popuphiding")` → `updateEditUIVisibility()`
- 条件付き依存: `if (aEvent.type == "popuphidden")` → `CustomizableUI.removePanelCloseListeners()`
- 条件付き依存: `if (aEvent.type == "popuphidden")` → `MenuMessage.hideAppMenuMessage()`
- 条件付き依存: `if ( aEvent.button == 0 && (AppConstants.platform != "macosx" || !aEvent.ctrlKey) )` → `this.toggle()`
- 条件付き依存: `if (aEvent.key == " " || aEvent.key == "Enter")` → `this.toggle()`
- 条件付き依存: `if (aEvent.key == " " || aEvent.key == "Enter")` → `aEvent.stopPropagation()`
- 条件付き依存: `if (novaFxaButton)` → `gSync.toggleAccountPanel()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.key`, `aEvent.target`, `aEvent.type`, `gBrowser.selectedBrowser`, `this.panel`

## onCommand()
- 位置: L498-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkingUI.showSubView()`, `BrowserCommands.fullScreen()`, `LoginHelper.openPasswordManager()`, `gSync.toggleAccountPanel()`, `openPreferences()`, `setTimeout()`, `target.closest()`, `target.closest("panel").hidePopup()`, `this._onBannerItemSelected()`, `this.showMoreToolsPanel()`, `this.showSubView()`
- 参照: `target.id`

## isReady()
- 位置: L538-540
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isReady`

## isNotificationPanelOpen()
- 位置: L542-546
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.notificationPanel.state`

## ensureReady()
- 位置: async L560-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureEventListenersAdded()`
- 参照: `this._isReady`, `this.panel.hidden`, `window.delayedStartupPromise`

## showHelpView()
- 位置: L575-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureEventListenersAdded()`, `this.multiView.showSubView()`

## showMoreToolsPanel()
- 位置: L585-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `document.getElementById()`, `this.showSubView()`
- XPCOM: `Services.obs`

## showSubView()
- 位置: async L603-730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `aAnchor.closest()`, `this._ensureEventListenersAdded()`, `this._ensureShortcutsShown()`, `this.ensurePanicViewInitialized()`, `viewNode.hasAttribute()`
- 条件付き依存: `if (!viewNode)` → `console.error()`
- 条件付き依存: `if (!aAnchor)` → `console.error()`
- 条件付き依存: `if (container && !viewNode.hasAttribute("disallowSubView"))` → `container.showSubView()`
- 条件付き依存: `if (!aAnchor.open)` → `document.createXULElement()`
- 条件付き依存: `if (!aAnchor.open)` → `tempPanel.setAttribute()`
- 条件付き依存: `if (!aAnchor.open)` → `viewNode.hasAttribute()`
- 条件付き依存: `if (viewNode.hasAttribute("neverhidden"))` → `tempPanel.setAttribute()`
- 条件付き依存: `if (!aAnchor.open)` → `aAnchor.getAttribute()`
- 条件付き依存: `if (aAnchor.getAttribute("tabspecific"))` → `tempPanel.setAttribute()`
- 条件付き依存: `if (aAnchor.getAttribute("locationspecific"))` → `tempPanel.setAttribute()`
- 条件付き依存: `if (this._disableAnimations)` → `tempPanel.setAttribute()`
- 条件付き依存: `if (!aAnchor.open)` → `document.getElementById("mainPopupSet").appendChild()`
- 条件付き依存: `if (!aAnchor.open)` → `document.getElementById()`
- 条件付き依存: `if (!aAnchor.open)` → `multiView.setAttribute()`
- 条件付き依存: `if (!aAnchor.open)` → `multiView.appendChild()`
- 条件付き依存: `if (!aAnchor.open)` → `tempPanel.appendChild()`
- 条件付き依存: `if (!aAnchor.open)` → `viewNode.classList.add()`
- 条件付き依存: `if (aAnchor.parentNode.id == "PersonalToolbar")` → `tempPanel.classList.add()`
- 条件付き依存: `if (!aAnchor.open)` → `this._getPanelAnchor()`
- 条件付き依存: `if (aAnchor != anchor && aAnchor.id)` → `anchor.setAttribute()`
- 条件付き依存: `if (!aAnchor.open)` → `PanelMultiView.openPopup()`
- 条件付き依存: `if (!aAnchor.open)` → `console.error()`
- 条件付き依存: `if (viewShown)` → `CustomizableUI.addPanelCloseListeners()`
- 条件付き依存: `if (viewShown)` → `tempPanel.addEventListener()`
- 条件付き依存: `if (!(viewShown))` → `panelRemover()`
- 参照: `AppConstants.platform`, `aAnchor.id`, `aAnchor.open`, `aAnchor.parentNode.id`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.key`, `aEvent.type`, `tempPanel.ariaLabel`, `tempPanel.ariaLabelledByElements`, `tempPanel.role`, `this._disableAnimations`, `viewNode.dataset.panelname`, `viewNode.dataset.panelrole`, `viewNode.id`

## panelRemover()
- 位置: L689-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.removePopup()`, `viewNode.classList.remove()`
- 条件付き依存: `if (viewShown)` → `CustomizableUI.removePanelCloseListeners()`
- 条件付き依存: `if (viewShown)` → `tempPanel.removeEventListener()`
- 参照: `aAnchor.open`, `event.target`

## ensurePanicViewInitialized()
- 位置: L737-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`
- 参照: `panelView._initialized`, `panelView.id`, `this.panic`

## disableSingleSubviewPanelAnimations()
- 位置: L755-757
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disableAnimations`

## enableSingleSubviewPanelAnimations()
- 位置: L759-761
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disableAnimations`

## updateOverflowStatus()
- 位置: L763-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.navbar.hasAttribute()`, `this.overflowFixedList.hasChildNodes()`
- 条件付き依存: `if (hasKids && !this.navbar.hasAttribute("nonemptyoverflow"))` → `this.navbar.setAttribute()`
- 条件付き依存: `if (hasKids && !this.navbar.hasAttribute("nonemptyoverflow"))` → `this.overflowPanel.setAttribute()`
- 条件付き依存: `if (!(hasKids && !this.navbar.hasAttribute("nonemptyoverflow")))` → `this.navbar.hasAttribute()`
- 条件付き依存: `if (!hasKids && this.navbar.hasAttribute("nonemptyoverflow"))` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (!hasKids && this.navbar.hasAttribute("nonemptyoverflow"))` → `this.overflowPanel.removeAttribute()`
- 条件付き依存: `if (!hasKids && this.navbar.hasAttribute("nonemptyoverflow"))` → `this.navbar.removeAttribute()`
- 参照: `this.overflowPanel`

## onWidgetAfterDOMChange()
- 位置: L775-779
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aContainer == this.overflowFixedList)` → `this.updateOverflowStatus()`
- 参照: `this.overflowFixedList`

## onAreaReset()
- 位置: L781-785
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aContainer == this.overflowFixedList)` → `this.updateOverflowStatus()`
- 参照: `this.overflowFixedList`

## _updatePanelButton()
- 位置: L791-806
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (state == "open" || state == "showing")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(state == "open" || state == "showing"))` → `document.l10n.setAttributes()`
- 参照: `this.menuButton`, `this.menuButton.open`, `this.panel`

## _onMainViewShow()
- 位置: L808-823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.getAttribute()`, `updateZoomUI()`
- 条件付き依存: `if (messageId)` → `MenuMessage.recordMenuMessageTelemetry()`
- 条件付き依存: `if (messageId)` → `ASRouter.getMessageById()`
- 条件付き依存: `if (messageId)` → `ASRouter.addImpression()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `MenuMessage.SOURCES.APP_MENU`, `event.target`, `gBrowser.selectedBrowser`

## _onHelpViewShow()
- 位置: L825-902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `buildHelpMenu()`, `byId.get()`, `cloneHelpMenuItem()`, `document.createDocumentFragment()`, `document.getElementById()`, `fragment.appendChild()`, `group.map()`, `group.map(id => byId.get(id)).filter()`, `helpMenu.getElementsByTagName()`, `items.appendChild()`, `items.firstChild.remove()`, `remaining.add()`, `remaining.delete()`, `this.getElementsByTagName()`
- 条件付き依存: `if (node.id)` → `byId.set()`
- 条件付き依存: `if (fragment.firstChild)` → `fragment.appendChild()`
- 条件付き依存: `if (fragment.firstChild)` → `document.createXULElement()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.nova.enabled", false))` → `items.querySelector()`
- 条件付き依存: `if (switchDeviceButton)` → `document.createElementNS()`
- 条件付き依存: `if (switchDeviceButton)` → `novaPromo.setAttribute()`
- 条件付き依存: `if (switchDeviceButton)` → `link.setAttribute()`
- 条件付き依存: `if (switchDeviceButton)` → `link.addEventListener()`
- 条件付き依存: `if (switchDeviceButton)` → `e.preventDefault()`
- 条件付き依存: `if (switchDeviceButton)` → `openSwitchingDevicesPage()`
- 条件付き依存: `if (switchDeviceButton)` → `novaPromo.appendChild()`
- 条件付き依存: `if (switchDeviceButton)` → `switchDeviceButton.replaceWith()`
- 参照: `fragment.firstChild`, `items.firstChild`, `link.href`, `link.id`, `link.slot`, `node.hidden`, `node.id`, `nodes.length`, `novaPromo.id`
- XPCOM: `Services.prefs`

## _onHelpCommand()
- 位置: L904-946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ReportBrokenSite.handleParentMenuButtonCommand()`, `Services.policies.getSupportMenu()`, `Services.scriptSecurityManager.createNullPrincipal()`, `gSafeBrowsing.getReportURL()`, `gSafeBrowsing.reportFalseDeceptiveSite()`, `openAboutDialog()`, `openFeedbackPage()`, `openHelpLink()`, `openSwitchingDevicesPage()`, `openTroubleshootingPage()`, `openTrustedLinkIn()`, `openUILink()`, `safeModeRestart()`, `toOpenWindowByType()`
- 参照: `Services.policies.getSupportMenu().URL.href`, `aEvent.target`, `aEvent.target.id`
- XPCOM: `Services.policies` / `Services.scriptSecurityManager`

## _onLibraryCommand()
- 位置: L948-962
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkingUI.showSubView()`, `DownloadsPanel.showDownloadsHistory()`, `this.showSubView()`
- 参照: `aEvent.target`, `button.documentGlobal`, `button.id`

## _hidePopup()
- 位置: L964-972
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isNotificationPanelOpen)` → `this.notificationPanel.hidePopup()`
- 参照: `this._notificationPanel`, `this.isNotificationPanelOpen`

## selectAndMarkItem()
- 位置: async L980-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`, `markItem()`, `this.panel.addEventListener()`
- 条件付き依存: `if (this.panel.state == "hiding")` → `this.panel.addEventListener()`
- 条件付き依存: `if (this.panel.state != "open")` → `this.panel.addEventListener()`
- 条件付き依存: `if (this.panel.state != "open")` → `this.show()`
- 参照: `this.mainView`, `this.panel.state`

## viewShownCB()
- 位置: L1004-1017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `viewHidingCB()`
- 条件付き依存: `if (itemIds.length)` → `window.document.getElementById()`
- 条件付き依存: `if (itemIds.length)` → `subItem?.closest()`
- 条件付き依存: `if (event.target.id == subItem?.closest("panelview")?.id)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (event.target.id == subItem?.closest("panelview")?.id)` → `markItem()`
- 参照: `event.target`, `event.target.id`, `itemIds.length`, `subItem?.closest("panelview")?.id`
- XPCOM: `Services.tm`

## viewHidingCB()
- 位置: L1019-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `currentView.ignoreMouseMove`

## popupHiddenCB()
- 位置: L1026-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.removeEventListener()`, `viewHidingCB()`

## markItem()
- 位置: L1031-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelView.forNode()`, `currentView.focusSelectedElement()`, `item.setAttribute()`, `itemIds.shift()`, `this.panel.addEventListener()`, `window.document.getElementById()`
- 条件付き依存: `if (itemIds.length)` → `this.panel.addEventListener()`
- 参照: `currentView.ignoreMouseMove`, `currentView.selectedElement`, `itemIds.length`

## updateNotifications()
- 位置: L1055-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notifications.filter()`, `shouldSuppressPopupNotifications()`
- 条件付き依存: `if (notificationsChanged)` → `this._clearAllNotifications()`
- 条件付き依存: `if (notificationsChanged)` → `this._hidePopup()`
- 条件付き依存: `if ( (window.fullScreen && FullScreen.navToolboxHidden) || document.fullscreenElement || shouldSuppressPopupNotifications() )` → `this._hidePopup()`
- 条件付き依存: `if (this.panel.state == "showing" || this.panel.state == "open")` → `doorhangers.forEach()`
- 条件付き依存: `if (n.options.onDismissed)` → `n.options.onDismissed()`
- 条件付き依存: `if (this.panel.state == "showing" || this.panel.state == "open")` → `this._hidePopup()`
- 条件付き依存: `if (!notifications[0].options.badgeOnly)` → `this._showBannerItem()`
- 条件付き依存: `if ( (window.fullScreen && this.autoHideToolbarInFullScreen) || Services.focus.activeWindow !== window )` → `this._hidePopup()`
- 条件付き依存: `if ( (window.fullScreen && this.autoHideToolbarInFullScreen) || Services.focus.activeWindow !== window )` → `this._showBadge()`
- 条件付き依存: `if ( (window.fullScreen && this.autoHideToolbarInFullScreen) || Services.focus.activeWindow !== window )` → `this._showBannerItem()`
- 条件付き依存: `if (!( (window.fullScreen && this.autoHideToolbarInFullScreen) || Services.focus.activeWindow !== window ))` → `this._clearBadge()`
- 条件付き依存: `if (!( (window.fullScreen && this.autoHideToolbarInFullScreen) || Services.focus.activeWindow !== window ))` → `this._showNotificationPanel()`
- 条件付き依存: `if (!(doorhangers.length))` → `this._hidePopup()`
- 条件付き依存: `if (!(doorhangers.length))` → `this._showBadge()`
- 条件付き依存: `if (!(doorhangers.length))` → `this._showBannerItem()`
- 参照: `FullScreen.navToolboxHidden`, `Services.focus.activeWindow`, `document.fullscreenElement`, `doorhangers.length`, `n.dismissed`, `n.options.badgeOnly`, `n.options.onDismissed`, `notifications.length`, `notifications[0].options.badgeOnly`, `this._notifications`, `this.autoHideToolbarInFullScreen`, `this.panel.state`, `window.fullScreen`
- XPCOM: `Services.focus`

## _showNotificationPanel()
- 位置: L1113-1140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document .getElementById()`, `document .getElementById("appMenu-notification-popup") .querySelectorAll()`, `document .getElementById("appMenu-notification-popup") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `this._getPanelAnchor()`, `this._refreshNotificationPanel()`, `this.notificationPanel.openPopup()`
- 条件付き依存: `if (notification.options.beforeShowDoorhanger)` → `notification.options.beforeShowDoorhanger()`
- 参照: `notification.options.beforeShowDoorhanger`, `this.isNotificationPanelOpen`, `this.menuButton`

## _clearNotificationPanel()
- 位置: L1142-1147
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `popupnotification.hidden`, `popupnotification.notification`, `this.notificationPanel.children`

## _clearAllNotifications()
- 位置: L1149-1153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearBadge()`, `this._clearBannerItem()`, `this._clearNotificationPanel()`

## notificationPanel()
- 位置: L1155-1171
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._notificationPanel)` → `document.getElementById()`
- 条件付き依存: `if (!this._notificationPanel)` → `template.replaceWith()`
- 条件付き依存: `if (!this._notificationPanel)` → `this._notificationPanel.addEventListener()`
- 参照: `template.content`, `this._notificationPanel`, `this.kEvents`, `this.kNotificationEvents`

## mainView()
- 位置: L1173-1178
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._mainView)` → `PanelMultiView.getViewNode()`
- 参照: `this._mainView`

## addonNotificationContainer()
- 位置: L1180-1189
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._addonNotificationContainer)` → `PanelMultiView.getViewNode()`
- 参照: `this._addonNotificationContainer`

## _formatDescriptionMessage()
- 位置: L1191-1198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.options.message.split()`
- 参照: `n.options.name`, `text.end`, `text.name`, `text.start`

## _refreshNotificationPanel()
- 位置: L1200-1230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `popupnotification.setAttribute()`, `popupnotification.show()`, `this._clearNotificationPanel()`, `this._getPopupId()`
- 条件付き依存: `if (notification.options.message)` → `this._formatDescriptionMessage()`
- 条件付き依存: `if (notification.options.message)` → `popupnotification.setAttribute()`
- 条件付き依存: `if (notification.options.onRefresh)` → `notification.options.onRefresh()`
- 条件付き依存: `if (notification.options.popupIconURL)` → `popupnotification.setAttribute()`
- 条件付き依存: `if (notification.options.learnMoreURL)` → `popupnotification.setAttribute()`
- 参照: `desc.end`, `desc.name`, `desc.start`, `notification.options.learnMoreURL`, `notification.options.message`, `notification.options.onRefresh`, `notification.options.popupIconURL`, `popupnotification.notification`

## _showAIMenuItem()
- 位置: L1232-1256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.documentElement.hasAttribute()`
- 参照: `aiMenuItem.hidden`, `chatHistoryMenuItem.hidden`, `classicWindowMenuItem.hidden`, `this.AIControlDefault`, `this.AIControlSmartWindow`, `this.isAIWindowEnabled`

## _showTabGroupsMenuItem()
- 位置: L1258-1264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`
- 参照: `button.hidden`, `this.tabGroupsAlternateMenu`

## _showReferralsMenuItem()
- 位置: L1266-1278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`
- 参照: `button.hidden`, `separator.hidden`, `this.referralsEnabled`

## _showBadge()
- 位置: L1280-1283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getBadgeStatus()`, `this.menuButton.setAttribute()`

## _showBannerItem()
- 位置: L1287-1339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `document.l10n.setAttributes()`, `supportedIds.includes()`, `this._panelBannerItem.setAttribute()`, `this._panelBannerItem.toggleAttribute()`
- 条件付き依存: `if (!this._panelBannerItem)` → `this.mainView.querySelector()`
- 条件付き依存: `if (isNovaUpdateRestart)` → `this._panelBannerItem.setAttribute()`
- 条件付き依存: `if (!(isNovaUpdateRestart))` → `this._panelBannerItem.removeAttribute()`
- 参照: `notification.id`, `this._panelBannerItem`, `this._panelBannerItem.hidden`, `this._panelBannerItem.notification`
- XPCOM: `Services.prefs`

## _clearBadge()
- 位置: L1341-1343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.menuButton.removeAttribute()`

## _clearBannerItem()
- 位置: L1345-1350
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._panelBannerItem`, `this._panelBannerItem.hidden`, `this._panelBannerItem.notification`

## _onNotificationButtonEvent()
- 位置: L1352-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `getNotificationFromElement()`
- 条件付き依存: `if (type == "secondarybuttoncommand")` → `AppMenuNotifications.callSecondaryAction()`
- 条件付き依存: `if (!(type == "secondarybuttoncommand"))` → `AppMenuNotifications.callMainAction()`
- 参照: `event.originalTarget`, `notificationEl.notification`

## _onBannerItemSelected()
- 位置: L1378-1388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppMenuNotifications.callMainAction()`, `event.stopPropagation()`
- 参照: `event.originalTarget`, `target.notification`

## _getPopupId()
- 位置: L1390-1392
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `notification.id`

## _getBadgeStatus()
- 位置: L1394-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `notification.id`

## _getPanelAnchor()
- 位置: L1398-1401
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `candidate.badgeStack`, `candidate.icon`

## _ensureShortcutsShown()
- 位置: L1403-1416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShortcutUtils.prettifyShortcut()`, `button.getAttribute()`, `button.setAttribute()`, `document.getElementById()`, `view.hasAttribute()`, `view.querySelectorAll()`, `view.setAttribute()`
- 参照: `this.mainView`

## getLocale()
- 位置: L1425-1427
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## getNotificationFromElement()
- 位置: L1432-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElement.closest()`
