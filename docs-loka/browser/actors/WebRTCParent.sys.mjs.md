# browser/actors/WebRTCParent.sys.mjs

source: browser/actors/WebRTCParent.sys.mjs
source-hash: a517455fe18d17b355d41d5c6e497bfdd120bb96
lines: 1821

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## WebRTCParent.didDestroy()
- 位置: L23-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.webrtcUI.activePerms.delete()`, `lazy.webrtcUI.forgetStreamsFromBrowserContext()`, `this.stopRecording()`
- 参照: `this.browsingContext`, `this.manager.outerWindowId`

## WebRTCParent.getBrowser()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.browsingContext.top.embedderElement`

## WebRTCParent.receiveMessage()
- 位置: L38-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Object.assign()`, `Object.freeze()`, `blocker()`, `console.error()`, `lazy.webrtcUI.emitter.emit()`, `this.getBrowser()`, `this.sendAsyncMessage()`, `this.stopRecording()`, `this.updateIndicators()`
- 条件付き依存: `if (decision)` → `lazy.webrtcUI.emitter.emit()`
- 条件付き依存: `if (!(decision))` → `lazy.webrtcUI.emitter.emit()`
- 条件付き依存: `if (browser.fxrPermissionPrompt)` → `browser.fxrPermissionPrompt()`
- 条件付き依存: `if (!(browser.fxrPermissionPrompt))` → `prompt()`
- 条件付き依存: `if (!(browser.fxrPermissionPrompt))` → `this.getBrowser()`
- 条件付き依存: `if (browser)` → `removePrompt()`
- 条件付き依存: `if (data.windowId)` → `lazy.webrtcUI.streamAddedOrRemoved()`
- 参照: `aMessage.data`, `aMessage.data.mediaSource`, `aMessage.data.rawID`, `aMessage.data.windowID`, `aMessage.name`, `browser.fxrPermissionPrompt`, `data.documentURI`, `data.isThirdPartyOrigin`, `data.origin`, `data.principal`, `data.remove`, `data.windowId`, `err.message`, `lazy.webrtcUI.peerConnectionBlockers`, `params.callID`, `params.windowID`, `this.browsingContext`, `this.manager.documentPrincipal.origin`, `this.manager.documentURI?.spec`, `this.manager.topWindowContext.documentPrincipal`, `this.manager.topWindowContext.documentPrincipal.origin`

## WebRTCParent.updateIndicators()
- 位置: L141-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSidebarBrowser()`, `lazy.webrtcUI.updateIndicators()`, `this.getBrowser()`
- 条件付き依存: `if (tabbrowser)` → `tabbrowser.updateBrowserSharing()`
- 条件付き依存: `if (isSidebarBrowser(browser))` → `browser.browsingContext.topChromeWindow.SidebarController?._permissions.updateFromBrowserState()`
- 参照: `aData.windowId`, `browser._sharingState`, `browser.documentGlobal.gBrowser`, `browsingContext.top`, `state.browsingContext`, `state.windowId`, `this.browsingContext`

## WebRTCParent.denyRequest()
- 位置: L168-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `aRequest.callID`, `aRequest.windowID`

## WebRTCParent.denyRequestNoPermission()
- 位置: L181-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `aRequest.callID`, `aRequest.windowID`

## WebRTCParent.checkOSPermission()
- 位置: async L194-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (camNeeded || micNeeded)` → `lazy.OSPermissions.getMediaCapturePermissionState()`
- 条件付き依存: `if (camNeeded)` → `this.checkAndGetOSPermission()`
- 条件付き依存: `if (micNeeded)` → `this.checkAndGetOSPermission()`
- 条件付き依存: `if (scrNeeded)` → `lazy.OSPermissions.getScreenCapturePermissionState()`
- 条件付き依存: `if (scrStatus.value == lazy.OSPermissions.PERMISSION_STATE_DENIED)` → `lazy.OSPermissions.maybeRequestScreenCapturePermission()`
- 参照: `camStatus.value`, `lazy.OSPermissions.PERMISSION_STATE_DENIED`, `lazy.OSPermissions.requestAudioCapturePermission`, `lazy.OSPermissions.requestVideoCapturePermission`, `micStatus.value`, `scrStatus.value`
- XPCOM: `Services.prefs`

## WebRTCParent.checkAndGetOSPermission()
- 位置: async L246-260
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (devicePermission == lazy.OSPermissions.PERMISSION_STATE_NOTDETERMINED)` → `requestPermissionFunc()`
- 参照: `lazy.OSPermissions.PERMISSION_STATE_DENIED`, `lazy.OSPermissions.PERMISSION_STATE_NOTDETERMINED`, `lazy.OSPermissions.PERMISSION_STATE_RESTRICTED`

## WebRTCParent.stopRecording()
- 位置: L262-280
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (browsingContext == this.browsingContext)` → `this.deactivateDevicePerm()`
- 参照: `lazy.webrtcUI._streams`, `state.devices`, `this.browsingContext`

## WebRTCParent.activateDevicePerm()
- 位置: L286-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.webrtcUI.activePerms .get()`, `lazy.webrtcUI.activePerms .get(this.manager.outerWindowId) .set()`, `lazy.webrtcUI.activePerms.has()`
- 条件付き依存: `if (!lazy.webrtcUI.activePerms.has(this.manager.outerWindowId))` → `lazy.webrtcUI.activePerms.set()`
- 参照: `this.manager.outerWindowId`

## WebRTCParent.deactivateDevicePerm()
- 位置: L303-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.webrtcUI.activePerms.get()`, `lazy.webrtcUI.activePerms.has()`, `map.delete()`
- 条件付き依存: `if (gracePeriodMs > 0)` → `[aMediaSource, aId].join()`
- 条件付き依存: `if (gracePeriodMs > 0)` → `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.SCOPE_TEMPORARY`, `lazy.webrtcUI.deviceGracePeriodTimeoutMs`, `this.browsingContext.top.embedderElement`, `this.manager.outerWindowId`

## WebRTCParent.checkRequestAllowed()
- 位置: L357-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.webrtcUI.activePerms.get()`, `perms.testExactPermissionFromPrincipal()`, `this.checkOSPermission()`, `this.checkOSPermission(!!camera, !!microphone, false).then()`
- 条件付き依存: `if (audioOutputDevices?.length)` → `audioOutputDevices.find()`
- 条件付き依存: `if (audioOutputDevices?.length)` → `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if (audioOutputDevices?.length)` → `["speaker", device.id].join()`
- 条件付き依存: `if (audioOutputDevices?.length)` → `this.getBrowser()`
- 条件付き依存: `if (audioOutputDevices?.length)` → `this.sendAsyncMessage()`
- 条件付き依存: `if ( perms.testExactPermissionFromPrincipal(aPrincipal, "MediaManagerVideo") )` → `perms.removeFromPrincipal()`
- 条件付き依存: `if (audioInputDevices.length)` → `isAllowed()`
- 条件付き依存: `if (videoInputDevices.length)` → `isAllowed()`
- 条件付き依存: `if (camera)` → `perms.addFromPrincipal()`
- 条件付き依存: `if (camera)` → `devices.push()`
- 条件付き依存: `if (camera)` → `this.activateDevicePerm()`
- 条件付き依存: `if (microphone)` → `devices.push()`
- 条件付き依存: `if (microphone)` → `this.activateDevicePerm()`
- 条件付き依存: `if (havePermission)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!(havePermission))` → `this.denyRequestNoPermission()`
- 参照: `aRequest.secondOrigin`, `aRequest.secure`, `aRequest.sharingScreen`, `audioInputDevices.length`, `audioOutputDevices?.length`, `camera.deviceIndex`, `camera.mediaSource`, `camera.rawId`, `device.deviceIndex`, `device.id`, `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.getForPrincipal( aPrincipal, ["speaker", device.id].join("^"), this.getBrowser() ).state`, `microphone.deviceIndex`, `microphone.mediaSource`, `microphone.rawId`, `perms.ALLOW_ACTION`, `perms.EXPIRE_SESSION`, `this.manager.outerWindowId`, `videoInputDevices.length`

## isAllowed()
- 位置: L412-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[mediaSource, rawId].join()`, `lazy.SitePermissions.getForPrincipal()`, `map?.get()`, `this.getBrowser()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.getForPrincipal( aPrincipal, [mediaSource, rawId].join("^"), this.getBrowser() ).state`, `lazy.SitePermissions.getForPrincipal(aPrincipal, permissionID).state`

## prompt()
- 位置: L495-1409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `allowedOrActiveCameraOrMicrophone()`, `chromeDoc.defaultView.PopupNotifications.show()`, `getPromptBrowser()`, `getPromptMessageId()`, `lazy.SitePermissions.getForPrincipal()`, `localization .formatMessagesSync()`, `localization .formatMessagesSync(actionL10nIds) .map()`, `maybeShowPopupNotificationInSidebar()`, `msg.attributes.reduce()`, `principal.schemeIs()`, `shouldShowAlwaysRemember()`, `type.toLowerCase()`
- 条件付き依存: `if (isBackground)` → `aActor.denyRequest()`
- 条件付き依存: `if (isPopup)` → `aActor.checkRequestAllowed()`
- 条件付き依存: `if (!aActor.checkRequestAllowed(aRequest, principal, aBrowser))` → `aActor.denyRequest()`
- 条件付き依存: `if ( lazy.SitePermissions.getForPrincipal(principal, permissionID, aBrowser) .state == lazy.SitePermissions.BLOCK )` → `aActor.denyRequest()`
- 条件付き依存: `if (isFile)` → `localization.formatValueSync()`
- 条件付き依存: `if (!(isFile))` → `localization.formatValueSync()`
- 条件付き依存: `if (!(isFile))` → `lazy.webrtcUI.getHostOrExtensionName()`
- 条件付き依存: `if (reqAudioOutput || (notificationSilencingEnabled && sharingScreen))` → `actionL10nIds.push()`
- 条件付き依存: `if (!(reqAudioOutput || (notificationSilencingEnabled && sharingScreen)))` → `actionL10nIds.push()`
- 条件付き依存: `if (shouldShowAlwaysRemember())` → `localization.formatValueSync()`
- 条件付き依存: `if (shouldShowAlwaysRemember())` → `getRememberCheckboxLabel()`
- 条件付き依存: `if (notificationSilencingEnabled && sharingScreen)` → `localization.formatValueSync()`
- 条件付き依存: `if (aRequest.secondOrigin)` → `lazy.webrtcUI.getHostOrExtensionName()`
- 条件付き依存: `if (promptBrowser != aBrowser)` → `promptWindow.addEventListener()`
- 参照: `aRequest.callID`, `aRequest.origin`, `aRequest.secondOrigin`, `aRequest.secure`, `audioInputDevices.length`, `audioOutputDevices.length`, `chromeDoc.defaultView`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.getForPrincipal(principal, permissionID, aBrowser) .state`, `mainMessage.accesskey`, `mainMessage.label`, `notification.callID`, `options.checkbox`, `options.secondName`, `principal.URI`, `principal.addonPolicy`, `principal.addonPolicy.extension.views`, `principal.isAddonOrExpandedAddonPrincipal`, `promptBrowser.browsingContext.topChromeWindow?.document`, `secondaryActions.length`, `secondaryActions[i].accessKey`, `secondaryActions[i].label`, `secondaryMessages[i].accesskey`, `secondaryMessages[i].label`, `videoInputDevices.length`, `view.viewType`, `view.xulBrowser`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## callback()
- 位置: L631-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.denyRequest()`
- 条件付き依存: `if (!isNotNowLabelEnabled)` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!isNotNowLabelEnabled)` → `aActor.getBrowser()`
- 参照: `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_TEMPORARY`

## callback()
- 位置: L649-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.denyRequest()`, `aActor.getBrowser()`, `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`

## callback()
- 位置: L671-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.denyRequest()`, `aActor.getBrowser()`, `clearTemporaryGrants()`
- 条件付き依存: `if (!isPersistent)` → `maybeClearAlwaysAsk()`
- 条件付き依存: `if (reqAudioInput)` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!isPersistent && !sharingScreen)` → `maybeClearAlwaysAsk()`
- 条件付き依存: `if (reqVideoInput)` → `lazy.SitePermissions.setForPrincipal()`
- 参照: `aState?.checkboxChecked`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_TEMPORARY`

## callback()
- 位置: L750-750
- 役割: (未記入)
- 触るとき: (未記入)

## eventCallback()
- 位置: L762-1271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.checkRequestAllowed()`, `chromeDoc.defaultView.PopupNotifications.panel.setAttribute()`, `describedByIDs.join()`, `doc.getElementById()`, `listDevices()`
- 条件付き依存: `if ( (reqVideoInput != "Screen" && reqVideoInput != "Camera") || aTopic == "dismissed" || aTopic == "removed" )` → `doc.getElementById()`
- 条件付き依存: `if (menuPopup?._commandEventListener)` → `menuPopup.removeEventListener()`
- 条件付き依存: `if (aTopic == "removed")` → `stopWatchingPromptWindow()`
- 条件付き依存: `if (aTopic == "removed" && notification && withoutUserResponse)` → `aActor.denyRequest()`
- 条件付き依存: `if ( aTopic == "shown" && !notification.wasDismissed && reqAudioOutput )` → `doc.getElementById()`
- 条件付き依存: `if ( aTopic == "shown" && !notification.wasDismissed && reqAudioOutput )` → `doc.querySelector()`
- 条件付き依存: `if ( aTopic == "shown" && !notification.wasDismissed && reqAudioOutput )` → `focusElement.focus()`
- 条件付き依存: `if (!notification.wasDismissed && isRequestingCamera)` → `onCameraPromptShown()`
- 条件付き依存: `if (aActor.checkRequestAllowed(aRequest, principal, aBrowser))` → `this.remove()`
- 条件付き依存: `if (sharingScreen)` → `doc.getElementById()`
- 条件付き依存: `if (sharingScreen)` → `listScreenShareDevices()`
- 条件付き依存: `if (sharingScreen)` → `checkDisabledWindowMenuItem()`
- 条件付き依存: `if (!(sharingScreen))` → `notificationElement.removeAttribute()`
- 条件付き依存: `if (!(sharingScreen))` → `doc.getElementById()`
- 条件付き依存: `if (isRequestingCamera)` → `listDevices()`
- 条件付き依存: `if (isRequestingCamera)` → `doc.getElementById()`
- 条件付き依存: `if (isRequestingCamera)` → `getOrCreateWebRTCPreviewEl()`
- 条件付き依存: `if (isRequestingCamera)` → `cameraMenuPopup.querySelector()`
- 条件付き依存: `if (cameraMenuPopup)` → `cameraMenuPopup.addEventListener()`
- 条件付き依存: `if (!sharingAudio)` → `listDevices()`
- 参照: `audioOutputDevices.length`, `cameraMenuPopup._commandEventListener`, `cameraMenuPopup.querySelector("[selected]")?.deviceId`, `doc.getElementById("webRTC-selectCamera").hidden`, `doc.getElementById("webRTC-selectMicrophone").hidden`, `doc.getElementById("webRTC-selectSpeaker").hidden`, `doc.getElementById("webRTC-selectWindowOrScreen").hidden`, `menuPopup._commandEventListener`, `menuPopup?._commandEventListener`, `notification.wasDismissed`, `this.browser?.browsingContext?.topChromeWindow?.document`, `this.mainAction.callback`, `warningBox.hidden`, `webrtcPreview.deviceId`, `webrtcPreview.mediaSource`, `webrtcPreview.showPreviewControlButtons`, `webrtcPreviewSection.hidden`

## listDevices()
- 位置: L852-904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addDeviceToList()`, `doc.getElementById()`, `itemParent.removeChild()`
- 条件付き依存: `if (IDPrefix == "webRTC-selectSpeaker")` → `doc.getElementById()`
- 条件付き依存: `if (!(IDPrefix == "webRTC-selectSpeaker"))` → `doc.getElementById()`
- 条件付き依存: `if (IDPrefix == "webRTC-selectSpeaker")` → `item.addEventListener()`
- 条件付き依存: `if (IDPrefix == "webRTC-selectSpeaker")` → `event.target.closest("popupnotification").button.click()`
- 条件付き依存: `if (IDPrefix == "webRTC-selectSpeaker")` → `event.target.closest()`
- 条件付き依存: `if (devices.length == 1)` → `describedByIDs.push()`
- 参照: `aRequest.audioOutputId`, `device.deviceIndex`, `device.id`, `device.name`, `device.rawId`, `devices.length`, `devices[0].name`, `item.deviceId`, `itemParent.lastChild`, `itemParent.parentNode`, `label.hidden`, `label.value`, `list.hidden`, `list.selectedIndex`

## checkDisabledWindowMenuItem()
- 位置: L910-918
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `item.hasAttribute()`
- 条件付き依存: `if (!item || item.hasAttribute("disabled"))` → `notificationElement.setAttribute()`
- 条件付き依存: `if (!(!item || item.hasAttribute("disabled")))` → `notificationElement.removeAttribute()`
- 参照: `list.selectedItem`

## listScreenShareDevices()
- 位置: L920-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addDeviceToList()`, `doc .getElementById()`, `doc .getElementById("webRTC-selectWindow-menulist") .removeAttribute()`, `doc.createXULElement()`, `doc.getElementById()`, `getOrCreateWebRTCPreviewEl()`, `localization.formatValueSync()`, `menupopup.addEventListener()`, `menupopup.appendChild()`, `menupopup.parentNode.removeAttribute()`, `menupopup.removeChild()`
- 条件付き依存: `if (device.canRequestOsLevelPrompt)` → `addDeviceToList()`
- 条件付き依存: `if (device.canRequestOsLevelPrompt)` → `localization.formatValueSync()`
- 条件付き依存: `if (device.name == "Primary Monitor")` → `localization.formatValueSync()`
- 条件付き依存: `if (!(device.name == "Primary Monitor"))` → `localization.formatValueSync()`
- 条件付き依存: `if (type == "application")` → `name.split()`
- 条件付き依存: `if (type == "application")` → `localization.formatValueSync()`
- 条件付き依存: `if (type == "application")` → `parseInt()`
- 参照: `device.canRequestOsLevelPrompt`, `device.mediaSource`, `device.name`, `device.rawId`, `device.scary`, `devices.length`, `doc.getElementById("webRTC-all-windows-shared").hidden`, `item.deviceId`, `item.mediaSource`, `item.scary`, `menupopup._commandEventListener`, `menupopup.lastChild`, `menupopup.parentNode`, `menupopup.parentNode.selectedItem`, `webrtcPreview.showPreviewControlButtons`

## menupopup._commandEventListener()
- 位置: L1010-1074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `checkDisabledWindowMenuItem()`, `doc.getElementById()`, `perms.addFromPrincipal()`
- 条件付き依存: `if (scary)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (scary)` → `lazy.OSPermissions.getScreenCapturePermissionState()`
- 条件付き依存: `if (scrStatus.value == lazy.OSPermissions.PERMISSION_STATE_DENIED)` → `lazy.OSPermissions.maybeRequestScreenCapturePermission()`
- 条件付き依存: `if ( (!isPipeWireDetected || mediaSource == "browser") && Services.prefs.getBoolPref( "media.getdisplaymedia.previews.enabled", true ) )` → `webrtcPreview.startPreview()`
- 参照: `Services.perms`, `event.target`, `lazy.OSPermissions.PERMISSION_STATE_DENIED`, `perms.ALLOW_ACTION`, `perms.EXPIRE_SESSION`, `scrStatus.value`, `warningBox.hidden`, `webrtcPreviewSection.hidden`
- XPCOM: `Services.perms` / `Services.prefs` / `Services.scriptSecurityManager`

## addDeviceToList()
- 位置: L1078-1090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.setAttribute()`, `list.appendItem()`
- 条件付き依存: `if (type)` → `item.setAttribute()`
- 条件付き依存: `if (deviceIndex == "-1")` → `item.setAttribute()`

## cameraMenuPopup._commandEventListener()
- 位置: L1137-1145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `webrtcPreview.startPreview()`
- 参照: `event.target`, `webrtcPreviewSection.hidden`

## this.mainAction.callback()
- 位置: async L1169-1267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.checkOSPermission()`, `aActor.sendAsyncMessage()`
- 条件付き依存: `if (reqVideoInput)` → `doc.getElementById()`
- 条件付き依存: `if (allowVideoDevice)` → `allowedDevices.push()`
- 条件付き依存: `if (allowVideoDevice)` → `perms.addFromPrincipal()`
- 条件付き依存: `if (allowVideoDevice)` → `videoInputDevices.find()`
- 条件付き依存: `if (allowVideoDevice)` → `aActor.activateDevicePerm()`
- 条件付き依存: `if (!sharingScreen)` → `persistGrantOrPromptPermission()`
- 条件付き依存: `if (reqAudioInput === "Microphone")` → `doc.getElementById()`
- 条件付き依存: `if (allowMic)` → `allowedDevices.push()`
- 条件付き依存: `if (allowMic)` → `audioInputDevices.find()`
- 条件付き依存: `if (allowMic)` → `aActor.activateDevicePerm()`
- 条件付き依存: `if (allowMic)` → `persistGrantOrPromptPermission()`
- 条件付き依存: `if (reqAudioInput === "AudioCapture")` → `allowedDevices.push()`
- 条件付き依存: `if (reqAudioOutput)` → `doc.getElementById()`
- 条件付き依存: `if (allowSpeaker)` → `allowedDevices.push()`
- 条件付き依存: `if (allowSpeaker)` → `audioOutputDevices.find()`
- 条件付き依存: `if (allowSpeaker)` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (allowSpeaker)` → `["speaker", id].join()`
- 条件付き依存: `if (!allowedDevices.length)` → `aActor.denyRequest()`
- 条件付き依存: `if (!havePermission)` → `aActor.denyRequestNoPermission()`
- 参照: `Services.perms`, `aRequest.callID`, `aRequest.windowID`, `aState.checkboxChecked`, `allowedDevices.length`, `doc.getElementById( "webRTC-selectMicrophone-menulist" ).value`, `doc.getElementById( "webRTC-selectSpeaker-richlistbox" ).value`, `doc.getElementById(listId).value`, `lazy.SitePermissions.ALLOW`, `perms.ALLOW_ACTION`, `perms.EXPIRE_SESSION`
- XPCOM: `Services.perms`

## shouldShowAlwaysRemember()
- 位置: L1274-1292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `aRequest.secondOrigin`

## getRememberCheckboxLabel()
- 位置: L1294-1307
- 役割: (未記入)
- 触るとき: (未記入)

## onUnload()
- 位置: L1398-1404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActor.denyRequest()`
- 参照: `aActor.manager`, `aActor.manager.isClosed`

## stopWatchingPromptWindow()
- 位置: L1406-1407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promptWindow.removeEventListener()`

## getPromptMessageId()
- 位置: L1419-1515
- 役割: (未記入)
- 触るとき: (未記入)

## allowedOrActiveCameraOrMicrophone()
- 位置: L1524-1559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.browsingContext .getAllBrowsingContextsInSubtree()`, `browser.browsingContext .getAllBrowsingContextsInSubtree() // Only keep the outerWindowIds .map()`, `lazy.SitePermissions.getAllForBrowser()`, `lazy.SitePermissions.getAllForBrowser(browser).some()`, `lazy.webrtcUI.activePerms.get()`, `map.values()`, `perm.id.startsWith()`, `types.includes()`
- 参照: `bc.currentWindowGlobal?.outerWindowId`, `lazy.SitePermissions.ALLOW`, `perm.state`

## removePrompt()
- 位置: L1561-1567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `removePromptFrom()`
- 条件付き依存: `if (!removePromptFrom(aBrowser, aCallId))` → `removePromptFrom()`
- 条件付き依存: `if (!removePromptFrom(aBrowser, aCallId))` → `getDocumentPiPBrowser()`

## removePromptFrom()
- 位置: L1569-1580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeWin?.PopupNotifications.getNotification()`, `notification.remove()`
- 参照: `aBrowser?.browsingContext?.topChromeWindow`, `notification.callID`

## clearTemporaryGrants()
- 位置: L1589-1611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SitePermissions.getAllForBrowser()`, `lazy.SitePermissions.removeFromPrincipal()`, `perm.id.split()`, `perms .filter()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.PERM_KEY_DELIMITER`, `lazy.SitePermissions.SCOPE_TEMPORARY`, `perm.id`, `perm.scope`, `perm.state`

## persistGrantOrPromptPermission()
- 位置: L1624-1640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SitePermissions.getForPrincipal()`, `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.PROMPT`, `lazy.SitePermissions.getForPrincipal(principal, permissionName).state`

## maybeClearAlwaysAsk()
- 位置: L1649-1662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if ( lazy.SitePermissions.getForPrincipal(principal, permissionName).state == lazy.SitePermissions.PROMPT )` → `lazy.SitePermissions.removeFromPrincipal()`
- 参照: `lazy.SitePermissions.PROMPT`, `lazy.SitePermissions.getForPrincipal(principal, permissionName).state`

## getOrCreateWebRTCPreviewEl()
- 位置: L1670-1679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeDoc.getElementById()`, `previewSection.querySelector()`
- 条件付き依存: `if (!previewEl)` → `chromeDoc.createElement()`
- 条件付き依存: `if (!previewEl)` → `previewSection.insertBefore()`
- 参照: `previewEl.id`, `previewSection.firstChild`

## onCameraPromptShown()
- 位置: L1693-1715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cameraMenuPopup?.querySelector()`, `doc.getElementById()`, `webrtcPreview?.startPreview()`
- 参照: `cameraMenuPopup?.querySelector("[selected]")?.deviceId`, `doc.getElementById("webRTC-preview-section").hidden`

## getDocumentPiPBrowser()
- 位置: L1724-1733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openerBC.group .getToplevels()`, `openerBC.group .getToplevels() .find()`
- 参照: `aBrowser.browsingContext`, `bc.isDocumentPiP`, `bc.opener`, `openerBC.isDocumentPiP`, `pipBC?.embedderElement`

## getPromptBrowser()
- 位置: L1753-1771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getDocumentPiPBrowser()`
- 参照: `Services.focus.activeWindow`, `aBrowser.browsingContext?.topChromeWindow?.document.fullscreenElement`, `aRequest.sharingScreen`, `pipBrowser?.browsingContext?.topChromeWindow`
- XPCOM: `Services.focus`

## isSidebarBrowser()
- 位置: L1773-1783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(nestedBrowsers).some()`, `sidebarBrowser.contentDocument.querySelectorAll()`
- 参照: `browser.browsingContext?.topChromeWindow?.SidebarController?.browser`

## maybeShowPopupNotificationInSidebar()
- 位置: L1789-1820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSidebarBrowser()`, `sidebarPopupNotifications.show()`
- 参照: `aBrowser.browsingContext?.topChromeWindow`, `aRequest.callID`, `notification.callID`, `win?.SidebarPopupNotifications`
