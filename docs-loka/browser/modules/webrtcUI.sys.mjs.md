# browser/modules/webrtcUI.sys.mjs

source: browser/modules/webrtcUI.sys.mjs
source-hash: cc85adce900d89042cf01bf277904c59d77cf7e9
lines: 1107

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## init()
- 位置: L87-104
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.initialized)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## uninit()
- 位置: L106-111
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.initialized)` → `Services.obs.removeObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L113-119
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (webrtcUI.showGlobalIndicator)` → `showOrCreateMenuForWindow()`
- 参照: `webrtcUI.showGlobalIndicator`

## showGlobalIndicator()
- 位置: L139-150
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `indicators.showCameraIndicator`, `indicators.showMicrophoneIndicator`, `indicators.showScreenSharingIndicator`, `this.perTabIndicators`

## showCameraIndicator()
- 位置: L152-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`
- 参照: `indicators.showCameraIndicator`, `this.perTabIndicators`, `this.showIndicatorsOnMacos14AndAbove`

## showMicrophoneIndicator()
- 位置: L170-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`
- 参照: `indicators.showMicrophoneIndicator`, `this.perTabIndicators`, `this.showIndicatorsOnMacos14AndAbove`

## showScreenSharingIndicator()
- 位置: L188-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppConstants.isPlatformAndVersionAtLeast()`, `list.sort()`, `precedence.indexOf()`
- 条件付き依存: `if (indicators.showScreenSharingIndicator)` → `list.push()`
- 参照: `indicators.showScreenSharingIndicator`, `this.perTabIndicators`, `this.showIndicatorsOnMacos14AndAbove`

## getActiveStreams()
- 位置: L216-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser?.documentGlobal.gBrowser?.getTabForBrowser()`, `webrtcUI._streams .filter()`
- 参照: `aStream.state`, `aStream.topBrowsingContext.embedderElement`, `state.browser`, `state.camera`, `state.devices`, `state.documentURI`, `state.microphone`, `state.screen`, `state.window`

## browserHasStreams()
- 位置: L254-262
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `stream.topBrowsingContext.embedderElement`, `this._streams`

## getCombinedStateForBrowser()
- 位置: L268-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabState.screen.includes()`
- 条件付き依存: `if (stream.topBrowsingContext == aTopBrowsingContext)` → `combine()`
- 条件付き依存: `if (tabState.screen)` → `tabState.screen.startsWith()`
- 条件付き依存: `if (!(tabState.screen.startsWith("Screen")))` → `tabState.screen.startsWith()`
- 条件付き依存: `if (!(tabState.screen.startsWith("Window")))` → `tabState.screen.startsWith()`
- 参照: `Ci.nsIMediaManagerService.STATE_CAPTURE_DISABLED`, `Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED`, `stream.state.browser`, `stream.state.camera`, `stream.state.microphone`, `stream.state.screen`, `stream.state.window`, `stream.topBrowsingContext`, `tabState.camera`, `tabState.microphone`, `tabState.paused`, `tabState.screen`, `tabState.sharing`, `tabState.showCameraIndicator`, `tabState.showMicrophoneIndicator`, `tabState.showScreenSharingIndicator`, `this._streams`
- XPCOM: [`nsIMediaManagerService`](../../dom/media/nsIMediaManager.idl.md)

## combine()
- 位置: L269-283
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIMediaManagerService.STATE_CAPTURE_DISABLED`, `Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED`, `Ci.nsIMediaManagerService.STATE_NOCAPTURE`
- XPCOM: [`nsIMediaManagerService`](../../dom/media/nsIMediaManager.idl.md)

## streamAddedOrRemoved()
- 位置: L379-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `sharedWindowRawDeviceIds.has()`, `this._setSharedData()`, `this.init()`
- 条件付き依存: `if (index < this._streams.length)` → `this._streams.splice()`
- 条件付き依存: `if (mediaSource == "window")` → `sharedWindowRawDeviceIds.add()`
- 条件付き依存: `if (browser.permanentKey)` → `this.allowedSharedBrowsers.add()`
- 条件付き依存: `if (sharedWindowRawDeviceIds.has(rawDeviceId))` → `this.sharedBrowserWindows.add()`
- 条件付き依存: `if (sharedWindowRawDeviceIds.has(rawDeviceId))` → `this.allowedSharedBrowsers.add()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "privacy.webrtc.allowSilencingNotifications", false ) )` → `Cc["@mozilla.org/alerts-service;1"] .getService(Ci.nsIAlertsService) .QueryInterface()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "privacy.webrtc.allowSilencingNotifications", false ) )` → `Cc["@mozilla.org/alerts-service;1"] .getService()`
- 参照: `Ci.nsIAlertsDoNotDisturb`, `Ci.nsIAlertsService`, `aBrowsingContext.top`, `aData.remove`, `alertsService.suppressForScreenSharing`, `browser.permanentKey`, `device.mediaSource`, `device.rawId`, `device.scary`, `lazy.BrowserWindowTracker.orderedWindows`, `selectedBrowser.permanentKey`, `state.devices`, `state.suppressNotifications`, `stream.browsingContext`, `stream.topBrowsingContext.embedderElement`, `this._streams`, `this._streams.length`, `this.allowTabSwitchesForSession`, `this.allowedSharedBrowsers`, `this.sharedBrowserWindows`, `this.sharingScreen`, `this.tabSwitchCountForSession`, `webrtcUI._streams.length`, `win.gBrowser.selectedBrowser`, `win.windowUtils.webrtcRawDeviceId`
- XPCOM: [`nsIAlertsDoNotDisturb`](../../toolkit/components/alerts/nsIAlertsService.idl.md) / [`nsIAlertsService`](../../toolkit/components/alerts/nsIAlertsService.idl.md) / `@mozilla.org/alerts-service;1` / `Services.prefs`

## forgetStreamsFromBrowserContext()
- 位置: L501-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setSharedData()`, `this.perTabIndicators.has()`, `this.updateGlobalIndicator()`
- 条件付き依存: `if (stream.browsingContext == aBrowsingContext)` → `this._streams.splice()`
- 条件付き依存: `if (this.perTabIndicators.has(topBC))` → `this.getCombinedStateForBrowser()`
- 条件付き依存: `if ( !tabState.showCameraIndicator && !tabState.showMicrophoneIndicator && !tabState.showScreenSharingIndicator )` → `this.perTabIndicators.delete()`
- 参照: `aBrowsingContext.top`, `stream.browsingContext`, `tabState.showCameraIndicator`, `tabState.showMicrophoneIndicator`, `tabState.showScreenSharingIndicator`, `this._streams`, `webrtcUI._streams.length`

## stopSharingStreams()
- 位置: L546-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserToSelect.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `this.clearPermissionsAndStopSharing()`, `window.focus()`
- 条件付き依存: `if (stopCameras)` → `ids.push()`
- 条件付き依存: `if (stopMics)` → `ids.push()`
- 条件付き依存: `if (stopScreens || stopWindows)` → `ids.push()`
- 参照: `activeStreams.length`, `browserToSelect.documentGlobal`, `gBrowser.selectedTab`

## clearPermissionsAndStopSharing()
- 位置: L593-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["camera", "screen", "microphone", "speaker"].includes()`, `actor.sendAsyncMessage()`, `lazy.SitePermissions.getAllForBrowser()`, `lazy.SitePermissions.removeFromPrincipal()`, `perm.id.split()`, `perms .filter()`, `sharingState.browsingContext.currentWindowGlobal.getActor()`, `types.filter()`, `types.includes()`, `webrtcUI.forgetActivePermissionsFromBrowser()`, `windowIds.forEach()`
- 条件付き依存: `if (invalidTypes.length)` → `invalidTypes.join()`
- 条件付き依存: `if (types.includes("screen") && sharingState.screen)` → `windowIds.push()`
- 条件付き依存: `if (sharingCameraOrMic)` → `windowIds.push()`
- 参照: `browser._sharingState?.webRTC`, `browser.contentPrincipal`, `invalidTypes.length`, `lazy.SitePermissions.PERM_KEY_DELIMITER`, `perm.id`, `sharingState.screen`, `sharingState?.camera`, `sharingState?.microphone`, `sharingState?.windowId`, `windowIds.length`

## updateIndicators()
- 位置: L660-677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getCombinedStateForBrowser()`, `this.perTabIndicators.has()`, `this.updateGlobalIndicator()`
- 条件付き依存: `if (this.perTabIndicators.has(aTopBrowsingContext))` → `this.perTabIndicators.get()`
- 条件付き依存: `if (!(this.perTabIndicators.has(aTopBrowsingContext)))` → `this.perTabIndicators.set()`
- 参照: `indicators.showCameraIndicator`, `indicators.showMicrophoneIndicator`, `indicators.showScreenSharingIndicator`, `tabState.showCameraIndicator`, `tabState.showMicrophoneIndicator`, `tabState.showScreenSharingIndicator`

## swapBrowserForNotification()
- 位置: L679-685
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `stream.browser`, `this._streams`

## forgetActivePermissionsFromBrowser()
- 位置: L695-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.browsingContext .getAllBrowsingContextsInSubtree()`, `aBrowser.browsingContext .getAllBrowsingContextsInSubtree() .map()`, `aBrowser.browsingContext .getAllBrowsingContextsInSubtree() .map(bc => bc.currentWindowGlobal?.outerWindowId) .filter()`, `browserWindowIds.forEach()`, `browserWindowIds.push()`, `this.activePerms.delete()`
- 参照: `aBrowser.outerWindowId`, `bc.currentWindowGlobal?.outerWindowId`

## showSharingDoorhanger()
- 位置: L712-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.focus()`, `browserWindow.gPermissionPanel.openPopup()`
- 条件付き依存: `if (!(aActiveStream.tab))` → `aActiveStream.browser.focus()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `browserWindow.addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `browserWindow.gPermissionPanel.openPopup()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService(Ci.nsIMacDockSupport) .activateApplication()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && !Services.focus.activeWindow)` → `Cc["@mozilla.org/widget/macdocksupport;1"] .getService()`
- 参照: `AppConstants.platform`, `Ci.nsIMacDockSupport`, `Services.focus.activeWindow`, `aActiveStream.browser.documentGlobal`, `aActiveStream.tab`, `browserWindow.gBrowser.selectedTab`
- XPCOM: `nsIMacDockSupport` / `@mozilla.org/widget/macdocksupport;1` / `Services.focus` / `Services.tm`

## updateWarningLabel()
- 位置: L739-744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aMenuList.selectedItem.getAttribute()`, `document.getElementById()`
- 参照: `aMenuList.ownerDocument`, `document.getElementById("webRTC-all-windows-shared").hidden`

## addPeerConnectionBlocker()
- 位置: L770-772
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.peerConnectionBlockers.add()`

## removePeerConnectionBlocker()
- 位置: L774-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.peerConnectionBlockers.delete()`

## on()
- 位置: L778-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emitter.on()`

## off()
- 位置: L782-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emitter.off()`

## getHostOrExtensionName()
- 位置: L786-809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByURI()`
- 条件付き依存: `if (!uri)` → `Services.io.newURI()`
- 条件付き依存: `if (!host)` → `uri.scheme.toLowerCase()`
- 条件付き依存: `if (!(uri && uri.scheme.toLowerCase() == "about"))` → `lazy.syncL10n.formatValueSync()`
- 参照: `addonPolicy?.name`, `uri.hostPort`, `uri.specIgnoringRef`
- XPCOM: `Services.io`

## updateGlobalIndicator()
- 位置: L811-854
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`
- 条件付き依存: `if (this.showGlobalIndicator)` → `showOrCreateMenuForWindow()`
- 条件付き依存: `if (!(this.showGlobalIndicator))` → `doc.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `doc.getElementById()`
- 条件付き依存: `if (!gIndicatorWindow)` → `getGlobalIndicator()`
- 条件付き依存: `if (!(!gIndicatorWindow))` → `gIndicatorWindow.updateIndicatorState()`
- 条件付き依存: `if (!(!gIndicatorWindow))` → `console.error()`
- 条件付き依存: `if (gIndicatorWindow.closingInternally)` → `gIndicatorWindow.closingInternally()`
- 条件付き依存: `if (gIndicatorWindow)` → `gIndicatorWindow.close()`
- 参照: `AppConstants.platform`, `chromeWin.document`, `err.message`, `existingMenu.hidden`, `gIndicatorWindow.closingInternally`, `separator.hidden`, `this.showGlobalIndicator`
- XPCOM: `Services.wm`

## getWindowShareState()
- 位置: L856-863
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(this.sharingScreen))` → `this.sharedBrowserWindows.has()`
- 参照: `this.SHARING_NONE`, `this.SHARING_SCREEN`, `this.SHARING_WINDOW`, `this.sharingScreen`

## tabAddedWhileSharing()
- 位置: L865-867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.allowedSharedBrowsers.add()`
- 参照: `tab.linkedBrowser.permanentKey`

## shouldShowSharedTabWarning()
- 位置: L869-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.allowedSharedBrowsers.has()`
- 条件付き依存: `if (!this.tabSwitchCountForSession)` → `this.allowedSharedBrowsers.add()`
- 参照: `browser.permanentKey`, `tab.linkedBrowser`, `this.allowTabSwitchesForSession`, `this.tabSwitchCountForSession`

## allowSharedTabSwitch()
- 位置: L896-902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `this.allowedSharedBrowsers.add()`
- 参照: `browser.permanentKey`, `gBrowser.selectedTab`, `tab.linkedBrowser`, `this.allowTabSwitchesForSession`

## _setSharedData()
- 位置: L912-929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.sharedData.set()`, `this.sharedBrowserWindows.has()`
- 条件付き依存: `if (this.sharedBrowserWindows.has(win))` → `sharedTopInnerWindowIds.add()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `this.sharingScreen`, `win.browsingContext.currentWindowGlobal.innerWindowId`
- XPCOM: `Services.ppmm`

## getGlobalIndicator()
- 位置: L932-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ww.openWindow()`
- XPCOM: `Services.ww`

## showStreamSharingMenu()
- 位置: L952-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SHARING_L10NID_BY_TYPE.get()`, `menu.getAttribute()`, `win.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (type == "Camera")` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (type == "Microphone")` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (type == "Screen")` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (!activeStreams.length)` → `event.preventDefault()`
- 条件付き依存: `if (activeStreams.length == 1)` → `doc.createXULElement()`
- 条件付き依存: `if (activeStreams.length == 1)` → `getDisplayHostForStream()`
- 条件付き依存: `if (activeStreams.length == 1)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (activeStreams.length == 1)` → `sharingItem.setAttribute()`
- 条件付き依存: `if (activeStreams.length == 1)` → `menu.appendChild()`
- 条件付き依存: `if (activeStreams.length == 1)` → `controlItem.addEventListener()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `doc.createXULElement()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `sharingItem.setAttribute()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `menu.appendChild()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `getDisplayHostForStream()`
- 条件付き依存: `if (!(activeStreams.length == 1))` → `controlItem.addEventListener()`
- 参照: `activeStreams.length`, `controlItem.stream`, `event.target`, `webrtcUI.showScreenSharingIndicator`, `win.document`

## getDisplayHostForStream()
- 位置: L1024-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `stream.uri`, `uri.displayHost`, `uri.displaySpec`
- XPCOM: `Services.io`

## onTabSharingMenuPopupShowing()
- 位置: L1043-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MEDIA_SOURCE_L10NID_BY_TYPE.get()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `e.target.appendChild()`, `lazy.listFormat.format()`, `lazy.syncL10n.formatValueSync()`, `menuitem.addEventListener()`, `streamInfo.devices.map()`, `webrtcUI.getActiveStreams()`, `webrtcUI.getHostOrExtensionName()`
- 参照: `e.target.ownerDocument`, `menuitem.stream`, `streamInfo.uri`

## onTabSharingMenuPopupHiding()
- 位置: L1063-1067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.lastChild.remove()`
- 参照: `this.lastChild`

## onTabSharingMenuPopupCommand()
- 位置: L1069-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `webrtcUI.showSharingDoorhanger()`
- 参照: `e.target.stream`

## showOrCreateMenuForWindow()
- 位置: L1073-1104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!menu)` → `document.createXULElement()`
- 条件付き依存: `if (!menu)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.createXULElement()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `container.insertBefore()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document.getElementById()`
- 条件付き依存: `if (!menu)` → `popup.addEventListener()`
- 条件付き依存: `if (!menu)` → `menu.appendChild()`
- 条件付き依存: `if (!menu)` → `container.insertBefore()`
- 参照: `AppConstants.platform`, `aWindow.document`, `document.getElementById("tabSharingSeparator").hidden`, `menu.hidden`, `menu.id`, `popup.id`, `separator.id`
