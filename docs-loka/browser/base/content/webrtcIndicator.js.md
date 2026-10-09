# browser/base/content/webrtcIndicator.js

source: browser/base/content/webrtcIndicator.js
source-hash: aedb10cd7a00201145834456def5515a2ed74595
lines: 594

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `WebRTCIndicator.init()`, `XPCOMUtils.defineLazyServiceGetter()`

## updateIndicatorState()
- 位置: L26-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebRTCIndicator.updateIndicatorState()`

## closingInternally()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebRTCIndicator.closingInternally()`

## init()
- 位置: L50-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `addEventListener()`
- 条件付き依存: `if (this.hideGlobalIndicator)` → `this.setVisibility()`
- 参照: `Services.appinfo.isWayland`, `this.hideGlobalIndicator`, `this.isClosingInternally`, `this.loaded`, `this.positionCustomized`, `this.showGlobalMuteToggles`, `this.statusBar`, `this.statusBarMenus`, `this.updatingIndicatorState`
- XPCOM: `Services.appinfo` / `Services.prefs`

## setVisibility()
- 位置: L87-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.setAttribute()`, `window.docShell.treeOwner.QueryInterface()`
- 参照: `Ci.nsIBaseWindow`, `baseWin.visibility`
- XPCOM: `nsIBaseWindow`

## updateIndicatorState()
- 位置: L101-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `displayShare.setAttribute()`, `document.getElementById()`, `showScreenSharingIndicator.startsWith()`, `this.updateWindowAttr()`
- 条件付き依存: `if (this.statusBar)` → `document.getElementById()`
- 条件付き依存: `if (this.statusBar)` → `this.statusBarMenus.has()`
- 条件付き依存: `if (shouldShow && !this.statusBarMenus.has(menu))` → `this.statusBar.addItem()`
- 条件付き依存: `if (shouldShow && !this.statusBarMenus.has(menu))` → `this.statusBarMenus.add()`
- 条件付き依存: `if (!(shouldShow && !this.statusBarMenus.has(menu)))` → `this.statusBarMenus.has()`
- 条件付き依存: `if (!shouldShow && this.statusBarMenus.has(menu))` → `this.statusBar.removeItem()`
- 条件付き依存: `if (!shouldShow && this.statusBarMenus.has(menu))` → `this.statusBarMenus.delete()`
- 条件付き依存: `if (!this.showGlobalMuteToggles && !webrtcUI.showScreenSharingIndicator)` → `this.setVisibility()`
- 条件付き依存: `if (!this.hideGlobalIndicator)` → `this.setVisibility()`
- 条件付き依存: `if (this.showGlobalMuteToggles)` → `this.updateWindowAttr()`
- 条件付き依存: `if (sharingWindow)` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (sharingWindow)` → `activeStreams.some()`
- 条件付き依存: `if (sharingWindow)` → `devices.some()`
- 条件付き依存: `if (window.windowState != window.STATE_MINIMIZED)` → `window.sizeToContent()`
- 条件付き依存: `if (AppConstants.platform == "linux")` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (window.windowState != window.STATE_MINIMIZED)` → `this.ensureOnScreen()`
- 条件付き依存: `if (!this.positionCustomized)` → `this.centerOnLatestBrowser()`
- 参照: `AppConstants.platform`, `docElStyle.maxHeight`, `docElStyle.maxWidth`, `docElStyle.minHeight`, `docElStyle.minWidth`, `document.documentElement`, `document.documentElement.style`, `this.hideGlobalIndicator`, `this.loaded`, `this.positionCustomized`, `this.showGlobalMuteToggles`, `this.statusBar`, `this.updatingIndicatorState`, `webrtcUI.showCameraIndicator`, `webrtcUI.showMicrophoneIndicator`, `webrtcUI.showScreenSharingIndicator`, `window.STATE_MINIMIZED`, `window.windowState`

## ensureOnScreen()
- 位置: L235-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `window.moveTo()`
- 参照: `document.documentElement.clientWidth`, `screen.availLeft`, `screen.availWidth`, `window.screenX`, `window.screenY`

## centerOnLatestBrowser()
- 位置: L249-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.windowUtils.getBoundsWithoutFlushing()`, `webrtcUI.getActiveStreams()`, `window.moveTo()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `activeStreams.length`, `activeStreams[activeStreams.length - 1].browser`, `browser.documentGlobal`, `browserRect.left`, `browserRect.top`, `browserRect.width`, `browserWindow.mozInnerScreenX`, `browserWindow.mozInnerScreenY`, `document.documentElement`

## handleEvent()
- 位置: L283-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onChange()`, `this.onClick()`, `this.onClose()`, `this.onCommand()`, `this.onLoad()`, `this.onPopupHiding()`, `this.onPopupShowing()`, `this.onUnload()`
- 条件付き依存: `if (window.windowState != window.STATE_MINIMIZED)` → `this.updateIndicatorState()`
- 参照: `event.type`, `this.positionCustomized`, `this.updatingIndicatorState`, `window.STATE_MINIMIZED`, `window.windowState`

## onLoad()
- 位置: L335-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.dispatchEvent()`, `this.updateIndicatorState()`, `window.addEventListener()`, `window.windowRoot.addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx" || AppConstants.platform == "win")` → `Cc["@mozilla.org/widget/systemstatusbar;1"].getService()`
- 条件付き依存: `if (this.statusBar)` → `window.addEventListener()`
- 参照: `AppConstants.platform`, `Ci.nsISystemStatusBar`, `this.loaded`, `this.statusBar`
- XPCOM: `nsISystemStatusBar` / `@mozilla.org/widget/systemstatusbar;1`

## onClose()
- 位置: L377-418
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this.showGlobalMuteToggles && (webrtcUI.showCameraIndicator || webrtcUI.showMicrophoneIndicator) )` → `event.preventDefault()`
- 条件付き依存: `if ( !this.showGlobalMuteToggles && (webrtcUI.showCameraIndicator || webrtcUI.showMicrophoneIndicator) )` → `this.setVisibility()`
- 条件付き依存: `if (!this.isClosingInternally)` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (!this.isClosingInternally)` → `webrtcUI.stopSharingStreams()`
- 参照: `this.isClosingInternally`, `this.showGlobalMuteToggles`, `webrtcUI.showCameraIndicator`, `webrtcUI.showMicrophoneIndicator`

## onUnload()
- 位置: L420-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.sharedData.flush()`, `Services.ppmm.sharedData.set()`
- 条件付き依存: `if (this.statusBar)` → `this.statusBar.removeItem()`
- 参照: `this.statusBar`, `this.statusBarMenus`
- XPCOM: `Services.ppmm`

## onClick()
- 位置: L432-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `webrtcUI.getActiveStreams()`, `webrtcUI.stopSharingStreams()`, `window.minimize()`
- 参照: `activeStreams.length`, `event.target.id`

## onChange()
- 位置: L468-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleCameraMute()`, `this.toggleMicrophoneMute()`
- 参照: `event.target`, `event.target.id`

## onPopupShowing()
- 位置: L481-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.eventIsForDeviceMenuPopup()`
- 条件付き依存: `if (this.eventIsForDeviceMenuPopup(event))` → `document.documentElement.getAttribute()`
- 条件付き依存: `if (document.documentElement.getAttribute("visible") != "true")` → `window.docShell.treeOwner.QueryInterface()`
- 条件付き依存: `if (this.eventIsForDeviceMenuPopup(event))` → `showStreamSharingMenu()`
- 参照: `Ci.nsIBaseWindow`, `baseWin.visibility`
- XPCOM: `nsIBaseWindow`

## onPopupHiding()
- 位置: L497-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.firstChild.remove()`, `this.eventIsForDeviceMenuPopup()`
- 参照: `event.target`, `menu.firstChild`

## onCommand()
- 位置: L508-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `webrtcUI.showSharingDoorhanger()`
- 参照: `event.target.stream`

## eventIsForDeviceMenuPopup()
- 位置: L521-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["Camera", "Microphone", "Screen"].includes()`, `menupopup.getAttribute()`
- 参照: `event.target`

## toggleMicrophoneMute()
- 位置: L537-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.sharedData.flush()`, `Services.ppmm.sharedData.set()`, `document.l10n.setAttributes()`
- 参照: `toggleEl.checked`
- XPCOM: `Services.ppmm`

## toggleCameraMute()
- 位置: L558-565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.sharedData.flush()`, `Services.ppmm.sharedData.set()`, `document.l10n.setAttributes()`
- 参照: `toggleEl.checked`
- XPCOM: `Services.ppmm`

## updateWindowAttr()
- 位置: L576-583
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `docEl.setAttribute()`
- 条件付き依存: `if (!(value))` → `docEl.removeAttribute()`
- 参照: `document.documentElement`

## closingInternally()
- 位置: L588-590
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isClosingInternally`
