# browser/base/content/browser-fullScreenAndPointerLock.js

source: browser/base/content/browser-fullScreenAndPointerLock.js
source-hash: d9756908a7fb6ed43db4c1b528391c8f7446a2cf
lines: 1267

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Object.values()`, `Object.values(PermissionUI) .filter()`

## constructor()
- 位置: L15-19
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._delay`, `this._func`, `this._id`

## start()
- 位置: L20-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this._handle()`, `this.cancel()`
- 参照: `this._delay`, `this._id`

## cancel()
- 位置: L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._id)` → `clearTimeout()`
- 参照: `this._id`

## _handle()
- 位置: L30-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._func()`
- 参照: `this._id`

## delay()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._delay`

## showPointerLock()
- 位置: L39-46
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!document.fullscreenElement)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (!document.fullscreenElement)` → `this.show()`
- 参照: `document.fullscreenElement`
- XPCOM: `Services.prefs`

## _getTimeout()
- 位置: L48-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (keyboardLockEnabled)` → `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## showFullScreen()
- 位置: L60-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `this._getTimeout()`, `this.show()`
- 参照: `browsingContext.top.currentWindowGlobal.documentPrincipal.originNoSuffix`
- XPCOM: `Services.prefs`

## show()
- 位置: L76-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `this._element.querySelector()`
- 条件付き依存: `if (!this._element)` → `document.getElementById()`
- 条件付き依存: `if (!this._element)` → `this._element.addEventListener()`
- 条件付き依存: `if (!this._element)` → `window.addEventListener()`
- 条件付き依存: `if (timeout > 0)` → `window.addEventListener()`
- 条件付き依存: `if (!this._element)` → `window.removeEventListener()`
- 条件付き依存: `if (!this._element)` → `this._timeoutHide.start()`
- 条件付き依存: `if (!(!host))` → `textElem.removeAttribute()`
- 条件付き依存: `if (!(!host))` → `BrowserUtils.formatURIForDisplay()`
- 条件付き依存: `if (!(!host))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (Services.focus.activeWindow == window)` → `this._timeoutHide.start()`
- 参照: `AppConstants.platform`, `Services.focus.activeWindow`, `gIdentityHandler.pointerlockFsWarningClassName`, `textElem.hidden`, `this.Timeout`, `this._element`, `this._element.dataset.identity`, `this._origin`, `this._state`, `this._timeoutHide`, `this._timeoutHide.delay`, `this._timeoutShow`, `uri.host`
- XPCOM: `Services.focus` / `Services.io`

## close()
- 位置: L175-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.selectedBrowser.focus()`, `this._doHide()`, `this._element .querySelector()`, `this._element .querySelector(".pointerlockfswarning-domain-text") .removeAttribute()`, `this._element.querySelector()`, `this._element.removeEventListener()`, `this._timeoutHide.cancel()`, `this._timeoutShow.cancel()`, `window.removeEventListener()`
- 条件付き依存: `if (buttonElement)` → `buttonElement.removeAttribute()`
- 参照: `this._element`, `this._element.id`, `this._state`, `this._timeoutHide`, `this._timeoutShow`

## _state()
- 位置: L220-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._element.hasAttribute()`
- 参照: `this._STATES`

## _doHide()
- 位置: L229-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._element.hidePopover()`
- 参照: `this._element.hidden`

## _state()
- 位置: L236-252
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currentState != "hiding")` → `this._element.removeAttribute()`
- 条件付き依存: `if (currentState == "hidden")` → `this._element.showPopover()`
- 条件付き依存: `if (newState != "hidden")` → `this._element.setAttribute()`
- 参照: `this._lastState`, `this._state`

## handleEvent()
- 位置: L254-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._timeoutHide.cancel()`, `this._timeoutHide.start()`
- 条件付き依存: `if (event.clientY != 0)` → `this._timeoutShow.cancel()`
- 条件付き依存: `if (this._timeoutShow.delay >= 0)` → `this._timeoutShow.start()`
- 条件付き依存: `if (state != "onscreen")` → `this._element.getBoundingClientRect()`
- 条件付き依存: `if (event.clientY <= elemRect.bottom + 50)` → `this._timeoutHide.start()`
- 条件付き依存: `if (event.clientY > elemRect.bottom + 50)` → `this._timeoutHide.cancel()`
- 条件付き依存: `if (this._state == "hiding")` → `this._doHide()`
- 条件付き依存: `if (this._state == "onscreen")` → `window.dispatchEvent()`
- 参照: `elemRect.bottom`, `event.clientY`, `event.type`, `this._lastState`, `this._state`, `this._timeoutShow.delay`

## isActive()
- 位置: L319-321
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isActive`

## entered()
- 位置: L323-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PointerlockFsWarning.showPointerLock()`, `Services.obs.notifyObservers()`
- 参照: `this._isActive`
- XPCOM: `Services.obs`

## exited()
- 位置: L329-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PointerlockFsWarning.close()`
- 参照: `this._isActive`

## moveDocumentPiPForFullscreen()
- 位置: L339-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `win.moveTo()`, `win.resizeTo()`
- 参照: `win.outerHeight`, `win.outerWidth`, `win.screen`

## moveAllDocumentPiPForFullscreen()
- 位置: L364-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`
- 条件付き依存: `if (win.browsingContext?.isDocumentPiP)` → `moveDocumentPiPForFullscreen()`
- 参照: `win.browsingContext?.isDocumentPiP`
- XPCOM: `Services.wm`

## init()
- 位置: L374-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `addEventListener()`, `document.getElementById()`, `notificationExitButton.addEventListener()`
- 条件付き依存: `if (window.fullScreen)` → `this.toggle()`
- 参照: `this.exitDomFullScreen`, `window.fullScreen`

## uninit()
- 位置: L402-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cleanup()`

## willToggle()
- 位置: L406-412
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWillEnterFullscreen)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!(aWillEnterFullscreen))` → `document.documentElement.removeAttribute()`

## fullScreenToggler()
- 位置: L414-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.fullScreenToggler`

## toggle()
- 位置: L420-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.documentElement.toggleAttribute()`, `document.getElementById()`, `fstoggler.addEventListener()`, `fullscreenCommand.toggleAttribute()`, `this._toggleShortcutKeys()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.shiftMacToolbarDown()`
- 条件付き依存: `if (!document.fullscreenElement)` → `ToolbarIconColor.inferFromText()`
- 条件付き依存: `if (enterFS)` → `document.addEventListener()`
- 条件付き依存: `if (enterFS)` → `gURLBar.controller.addListener()`
- 条件付き依存: `if (!document.fullscreenElement)` → `this.hideNavToolbox()`
- 条件付き依存: `if (enterFS)` → `moveAllDocumentPiPForFullscreen()`
- 条件付き依存: `if (!(enterFS))` → `this.showNavToolbox()`
- 条件付き依存: `if (!(enterFS))` → `this.cleanup()`
- 参照: `AppConstants.platform`, `document.fullscreenElement`, `document.getElementById("enterFullScreenItem").hidden`, `document.getElementById("exitFullScreenItem").hidden`, `this._expandCallback`, `this._isPopupOpen`, `this._keyToggleCallback`, `this._setPopupOpen`, `this.fullScreenToggler`, `window.fullScreen`
- XPCOM: `Services.prefs`

## exitDomFullScreen()
- 位置: L478-483
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.fullscreenElement)` → `document.exitFullscreen()`
- 参照: `document.fullscreenElement`

## shiftMacToolbarDown()
- 位置: L495-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateMacToolbarShift()`
- 条件付き依存: `if (typeof shiftSize !== "number")` → `console.error()`
- 条件付き依存: `if (shiftSize > 0 && !wasRevealed && !this.fullScreenToggler.hidden)` → `this.showNavToolbox()`
- 参照: `this._menubarShift`, `this.fullScreenToggler.hidden`

## updateMacToolbarShift()
- 位置: L521-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.style.setProperty()`, `gNavToolbox.classList.toggle()`, `shiftSize.toFixed()`
- 参照: `gNavToolbox.style.translate`, `this._currentToolbarShift`, `this._isChromeCollapsed`, `this._menubarShift`

## handleEvent()
- 位置: L539-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shiftMacToolbarDown()`, `this.toggle()`, `this.willToggle()`
- 参照: `event.detail`, `event.type`

## _logWarningPermissionPromptFS()
- 位置: L556-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/scripterror;1"].createInstance()`, `Services.console.logMessage()`, `consoleMsg.initWithWindowID()`, `gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIScriptError`, `Ci.nsIScriptError.warningFlag`, `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.innerWindowID`
- XPCOM: [`nsIScriptError`](../../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## _handlePermPromptShow()
- 位置: L575-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PopupNotifications.getNotification()`, `PopupNotifications.getNotification( this._permissionNotificationIDs ).filter()`
- 条件付き依存: `if ( !FullScreen.permissionsFullScreenAllowed && window.fullScreen && PopupNotifications.getNotification( this._permissionNotificationIDs ).filter(n => !n.dismis...)` → `this.exitDomFullScreen()`
- 条件付き依存: `if ( !FullScreen.permissionsFullScreenAllowed && window.fullScreen && PopupNotifications.getNotification( this._permissionNotificationIDs ).filter(n => !n.dismis...)` → `this._logWarningPermissionPromptFS()`
- 参照: `FullScreen.permissionsFullScreenAllowed`, `PopupNotifications.getNotification( this._permissionNotificationIDs ).filter(n => !n.dismissed).length`, `n.dismissed`, `this._permissionNotificationIDs`, `window.fullScreen`

## enterDomFullscreen()
- 位置: L588-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PointerlockFsWarning.close()`, `PopupNotifications.panel.addEventListener()`, `XULBrowserWindow.onEnterDOMFullscreen()`, `document.documentElement.setAttribute()`, `document.documentElement.toggleAttribute()`, `gBrowser.tabContainer.addEventListener()`, `gXPInstallObserver.removeAllNotifications()`, `this._handlePermPromptShow()`, `this._isRemoteBrowser()`
- 条件付き依存: `if (this._isRemoteBrowser(aBrowser))` → `this._getNextMsgRecipientActor()`
- 条件付き依存: `if (!targetActor)` → `this._abortEnterFullscreen()`
- 条件付き依存: `if (this._isRemoteBrowser(aBrowser))` → `targetActor.sendAsyncMessage()`
- 条件付き依存: `if ( !aBrowser || gBrowser.selectedBrowser != aBrowser || // The top-level window has lost focus since the request to enter // full-screen was made. Cancel full-...)` → `this._abortEnterFullscreen()`
- 条件付き依存: `if (!FullScreen.permissionsFullScreenAllowed)` → `PopupNotifications.getNotification( this._permissionNotificationIDs ).filter()`
- 条件付き依存: `if (!FullScreen.permissionsFullScreenAllowed)` → `PopupNotifications.getNotification()`
- 条件付き依存: `if (!FullScreen.permissionsFullScreenAllowed)` → `PopupNotifications.remove()`
- 条件付き依存: `if (notifications.length)` → `this._logWarningPermissionPromptFS()`
- 条件付き依存: `if (gFindBarInitialized)` → `gFindBar.close()`
- 条件付き依存: `if (gXPInstallObserver.removeAllNotifications(aBrowser))` → `gXPInstallObserver.logWarningFullScreenInstallBlocked()`
- 参照: `FullScreen.permissionsFullScreenAllowed`, `Services.focus.activeWindow`, `aActor.requestOrigin`, `document.fullscreenElement`, `gBrowser.selectedBrowser`, `n.dismissed`, `notifications.length`, `targetActor.waitingForChildEnterFullscreen`, `this._permissionNotificationIDs`, `this.exitDomFullScreen`
- XPCOM: `Services.focus`

## cleanup()
- 位置: L696-708
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!window.fullScreen)` → `this._mouseTargetRectObserver?.disconnect()`
- 条件付き依存: `if (!window.fullScreen)` → `this._collapsedToolboxObserver?.disconnect()`
- 条件付き依存: `if (!window.fullScreen)` → `MousePosTracker.removeListener()`
- 条件付き依存: `if (!window.fullScreen)` → `document.removeEventListener()`
- 条件付き依存: `if (!window.fullScreen)` → `gURLBar.controller.removeListener()`
- 参照: `this._expandedMouseTargetRect`, `this._keyToggleCallback`, `this._launcherEdgeListener`, `this._setPopupOpen`, `window.fullScreen`

## _toggleShortcutKeys()
- 位置: L710-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(id)?.removeAttribute()`, `document.getElementById(id)?.setAttribute()`
- 参照: `window.fullScreen`

## cleanupDomFullscreen()
- 位置: L739-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PointerlockFsWarning.close()`, `PopupNotifications.panel.removeEventListener()`, `document.documentElement.removeAttribute()`, `document.documentElement.toggleAttribute()`, `gBrowser.tabContainer.removeEventListener()`, `this._getNextMsgRecipientActor()`, `this._handlePermPromptShow()`
- 条件付き依存: `if (target)` → `target.sendAsyncMessage()`
- 参照: `target.waitingForChildExitFullscreen`, `this._isChromeCollapsed`, `this.exitDomFullScreen`

## _abortEnterFullscreen()
- 位置: L784-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.exitFullscreen()`, `document.exitFullscreen().catch()`, `setTimeout()`
- 条件付き依存: `if (aActor.timerId)` → `Glean.fullscreen.change.cancel()`
- 参照: `aActor.timerId`

## _getNextMsgRecipientActor()
- 位置: L817-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.hasBeenDestroyed()`, `target.hasBeenDestroyed()`
- 条件付き依存: `if (aUseCache && aActor.nextMsgRecipient)` → `actor.hasBeenDestroyed()`
- 条件付き依存: `if (parentBC && parentBC.currentWindowGlobal)` → `parentBC.currentWindowGlobal.getActor()`
- 参照: `aActor.browsingContext`, `aActor.nextMsgRecipient`, `aActor.requestOrigin`, `actor.nextMsgRecipient`, `actor.windowContext`, `actor.windowContext.isInBFCache`, `childBC.currentWindowGlobal`, `childBC.currentWindowGlobal.osPid`, `childBC.parent`, `parentBC.currentWindowGlobal`, `parentBC.currentWindowGlobal.osPid`, `target.windowContext?.isInBFCache`

## _isRemoteBrowser()
- 位置: L880-882
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.hasAttribute()`

## getMouseTargetRect()
- 位置: L899-916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `SidebarController.sidebarContainer`, `container.hidden`, `document.documentElement`, `window.windowUtils.getBoundsWithoutFlushing(container).left`

## onMouseEnter()
- 位置: L917-921
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._suppressEnter)` → `FullScreen.showNavToolbox()`
- 参照: `this._suppressEnter`

## _watchLauncherEdge()
- 位置: L924-935
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MousePosTracker.addListener()`, `MousePosTracker.removeListener()`, `document.documentElement.hasAttribute()`
- 参照: `listener._suppressEnter`, `this._launcherEdgeListener`

## getMouseTargetRect()
- 位置: L937-939
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._mouseTargetRect`

## _mouseTargetRectFromBounds()
- 位置: L944-951
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `rect.bottom`, `rect.left`, `rect.right`, `rect.top`

## _updateMouseTargetRect()
- 位置: L960-972
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._mouseTargetRectFromBounds()`, `window .promiseDocumentFlushed()`, `window .promiseDocumentFlushed(() => window.windowUtils.getBoundsWithoutFlushing(gBrowser.tabpanels) ) .then()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `gBrowser.tabpanels`, `this._mouseTargetRect`, `window.fullScreen`

## _expandCallback()
- 位置: L975-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FullScreen.showNavToolbox()`

## onMouseEnter()
- 位置: L979-981
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideNavToolbox()`

## _keyToggleCallback()
- 位置: L983-992
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_ESCAPE)` → `FullScreen.hideNavToolbox()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_F6)` → `FullScreen.showNavToolbox()`
- 参照: `aEvent.DOM_VK_ESCAPE`, `aEvent.DOM_VK_F6`, `aEvent.keyCode`

## _setPopupOpen()
- 位置: L998-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.getAttribute()`
- 条件付き依存: `if (aEvent.type == "popuphidden")` → `FullScreen.hideNavToolbox()`
- 参照: `FullScreen._isChromeCollapsed`, `FullScreen._isPopupOpen`, `aEvent.originalTarget`, `aEvent.type`, `target.id`, `target.localName`

## onViewOpen()
- 位置: L1021-1025
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isChromeCollapsed`, `this._isPopupOpen`

## onViewClose()
- 位置: L1028-1031
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideNavToolbox()`
- 参照: `this._isPopupOpen`

## navToolboxHidden()
- 位置: L1033-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isChromeCollapsed`

## updateAutohideMenuitem()
- 位置: L1038-1043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `aItem.toggleAttribute()`
- XPCOM: `Services.prefs`

## setAutohide()
- 位置: L1044-1051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FullScreen.hideNavToolbox()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _setCollapsedToolboxMargin()
- 位置: L1056-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gNavToolbox.style.marginTop`

## _updateCollapsedToolboxMargin()
- 位置: L1067-1078
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window .promiseDocumentFlushed()`, `window .promiseDocumentFlushed( () => window.windowUtils.getBoundsWithoutFlushing(gNavToolbox).height ) .then()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this._isChromeCollapsed)` → `this._setCollapsedToolboxMargin()`
- 参照: `this._isChromeCollapsed`, `window.windowUtils.getBoundsWithoutFlushing(gNavToolbox).height`

## showNavToolbox()
- 位置: L1080-1137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `document.documentElement.removeAttribute()`, `gNavToolbox.removeAttribute()`, `this._collapsedToolboxObserver?.disconnect()`
- 条件付き依存: `if (trackMouse)` → `this._mouseTargetRectFromBounds()`
- 条件付き依存: `if (trackMouse)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (trackMouse)` → `this._updateMouseTargetRect()`
- 条件付き依存: `if (!this._mouseTargetRectObserver)` → `this._updateMouseTargetRect()`
- 条件付き依存: `if (trackMouse)` → `this._mouseTargetRectObserver.observe()`
- 条件付き依存: `if (trackMouse)` → `MousePosTracker.removeListener()`
- 条件付き依存: `if (trackMouse)` → `MousePosTracker.addListener()`
- 条件付き依存: `if (this._menubarShift)` → `this.updateMacToolbarShift()`
- 参照: `BrowserHandler.kiosk`, `gBrowser.tabpanels`, `gNavToolbox.style.marginTop`, `this._expandedMouseTargetRect`, `this._hover`, `this._isChromeCollapsed`, `this._launcherEdgeListener`, `this._menubarShift`, `this._mouseTargetRect`, `this._mouseTargetRectObserver`, `this.fullScreenToggler.hidden`
- XPCOM: `Services.obs`

## hideNavToolbox()
- 位置: L1139-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MousePosTracker.removeListener()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `document.documentElement.toggleAttribute()`, `this._collapsedToolboxObserver.observe()`, `this._mouseTargetRectFromBounds()`, `this._mouseTargetRectObserver?.disconnect()`, `this._setCollapsedToolboxMargin()`, `this._watchLauncherEdge()`, `window.matchMedia()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if ( focused && focused.ownerDocument == document && focused.localName == "input" && !BrowserHandler.kiosk )` → `window.addEventListener()`
- 条件付き依存: `if ( aAnimate && window.matchMedia("(prefers-reduced-motion: no-preference)").matches && !BrowserHandler.kiosk )` → `gNavToolbox.setAttribute()`
- 条件付き依存: `if (this._menubarShift)` → `this.updateMacToolbarShift()`
- 条件付き依存: `if (!this._collapsedToolboxObserver)` → `this._updateCollapsedToolboxMargin()`
- 参照: `BrowserHandler.kiosk`, `document.commandDispatcher.focusedElement`, `focused.localName`, `focused.ownerDocument`, `gBrowser.tabpanels`, `this._collapsedToolboxObserver`, `this._expandedMouseTargetRect`, `this._isChromeCollapsed`, `this._isPopupOpen`, `this._menubarShift`, `this.fullScreenToggler.hidden`, `window.matchMedia("(prefers-reduced-motion: no-preference)").matches`, `window.windowUtils.getBoundsWithoutFlushing(gNavToolbox).height`
- XPCOM: `Services.obs` / `Services.prefs`

## retryHideNavToolbox()
- 位置: L1165-1179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `setTimeout()`, `window.removeEventListener()`
- 条件付き依存: `if (window.fullScreen)` → `this.hideNavToolbox()`
- 参照: `window.fullScreen`
