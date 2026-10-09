# browser/actors/WebRTCChild.sys.mjs

source: browser/actors/WebRTCChild.sys.mjs
source-hash: 7710de00d187ea804a0699b40e251b48864a353e
lines: 579

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`

## init()
- 位置: L32-39
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initted)` → `Services.cpmm.sharedData.addEventListener()`
- 条件付き依存: `if (!this._initted)` → `this._updateCameraMuteState()`
- 条件付き依存: `if (!this._initted)` → `this._updateMicrophoneMuteState()`
- 参照: `this._initted`
- XPCOM: `Services.cpmm`

## handleEvent()
- 位置: L41-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.changedKeys.includes()`
- 条件付き依存: `if (event.changedKeys.includes("WebRTC:GlobalCameraMute"))` → `this._updateCameraMuteState()`
- 条件付き依存: `if (event.changedKeys.includes("WebRTC:GlobalMicrophoneMute"))` → `this._updateMicrophoneMuteState()`

## _updateCameraMuteState()
- 位置: L50-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.sharedData.get()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.cpmm` / `Services.obs`

## _updateMicrophoneMuteState()
- 位置: L58-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.sharedData.get()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.cpmm` / `Services.obs`

## WebRTCChild.actorCreated()
- 位置: L71-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.suppressNotifications`

## WebRTCChild.handleEvent()
- 位置: L84-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActorForWindow()`
- 条件付き依存: `if (actor)` → `contentWindow.pendingGetUserMediaRequests.keys()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (actor)` → `contentWindow.pendingPeerConnectionRequests.keys()`
- 参照: `aEvent.target.defaultView`

## WebRTCChild.observe()
- 位置: L99-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleGUMRequest()`, `handleGUMStop()`, `handlePCRequest()`, `removeBrowserSpecificIndicator()`, `updateIndicators()`

## WebRTCChild.receiveMessage()
- 位置: L119-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.wm.getOuterWindowWithId()`, `allowedDevices.appendElement()`, `contentWindow.pendingGetUserMediaRequests.get()`, `denyGUMRequest()`, `forgetGUMRequest()`, `forgetPCRequest()`
- 参照: `Ci.nsIMutableArray`, `aMessage.data`, `aMessage.data.callID`, `aMessage.data.devices`, `aMessage.data.suppressNotifications`, `aMessage.data.windowID`, `aMessage.name`, `this.suppressNotifications`
- XPCOM: [`nsIMutableArray`](../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1` / `Services.obs` / `Services.wm`

## getActorForWindow()
- 位置: L202-214
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (windowGlobal)` → `windowGlobal.getActor()`
- 参照: `window.windowGlobalChild`

## handlePCRequest()
- 位置: L216-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getOuterWindowWithId()`, `contentWindow.pendingPeerConnectionRequests.add()`, `getActorForWindow()`
- 条件付き依存: `if (!contentWindow.pendingPeerConnectionRequests)` → `setupPendingListsInitially()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `contentWindow.document.documentURI`, `contentWindow.pendingPeerConnectionRequests`
- XPCOM: `Services.wm`

## handleGUMStop()
- 位置: L238-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getOuterWindowWithId()`, `getActorForWindow()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `aSubject.mediaSource`, `aSubject.rawID`, `aSubject.windowID`
- XPCOM: `Services.wm`

## handleGUMRequest()
- 位置: L253-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GlobalMuteListener.init()`, `Services.wm.getOuterWindowWithId()`, `aSubject.getAudioOutputOptions()`, `aSubject.getConstraints()`, `prompt()`
- 参照: `aSubject.callID`, `aSubject.devices`, `aSubject.isHandlingUserInput`, `aSubject.isSecure`, `aSubject.type`, `aSubject.windowID`
- XPCOM: `Services.wm`

## prompt()
- 位置: L277-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[audio, ...(audio.advanced || [])].some()`, `[video, ...(video.advanced || [])].some()`, `aContentWindow.document.permDelegateHandler.QueryInterface()`, `aContentWindow.pendingGetUserMediaRequests.set()`, `device.QueryInterface()`, `getActorForWindow()`, `permDelegateHandler.maybeUnsafePermissionDelegate()`
- 条件付き依存: `if (audio && (device.mediaSource == "microphone") != sharingAudio)` → `audioInputDevices.push()`
- 条件付き依存: `if (audio && (device.mediaSource == "microphone") != sharingAudio)` → `devices.push()`
- 条件付き依存: `if (video && (device.mediaSource == "camera") != sharingScreen)` → `videoInputDevices.push()`
- 条件付き依存: `if (video && (device.mediaSource == "camera") != sharingScreen)` → `devices.push()`
- 条件付き依存: `if (aRequestType == "selectaudiooutput")` → `audioOutputDevices.push()`
- 条件付き依存: `if (aRequestType == "selectaudiooutput")` → `devices.push()`
- 条件付き依存: `if (videoInputDevices.length)` → `requestTypes.push()`
- 条件付き依存: `if (audioInputDevices.length)` → `requestTypes.push()`
- 条件付き依存: `if (audioOutputDevices.length)` → `requestTypes.push()`
- 条件付き依存: `if (!requestTypes.length)` → `denyGUMRequest()`
- 条件付き依存: `if (!aContentWindow.pendingGetUserMediaRequests)` → `setupPendingListsInitially()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `Ci.nsIMediaDevice`, `Ci.nsIPermissionDelegateHandler`, `aAudioOutputOptions.deviceId`, `aConstraints.audio`, `aConstraints.picture`, `aConstraints.video`, `aContentWindow.document.documentURI`, `aContentWindow.document.nodePrincipal.origin`, `aContentWindow.pendingGetUserMediaRequests`, `audio.advanced`, `audio.mediaSource`, `audioInputDevices.length`, `audioOutputDevices.length`, `device.canRequestOsLevelPrompt`, `device.id`, `device.mediaSource`, `device.rawId`, `device.rawName`, `device.scary`, `device.type`, `deviceObject.scary`, `devices.length`, `requestTypes.length`, `video.advanced`, `video.mediaSource`, `videoInputDevices.length`
- XPCOM: [`nsIMediaDevice`](../../dom/media/nsIMediaDevice.idl.md) / [`nsIPermissionDelegateHandler`](../../dom/interfaces/base/nsIPermissionDelegateHandler.idl.md)

## hasInherentConstraints()
- 位置: L301-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[deviceId].flat()`

## denyGUMRequest()
- 位置: L426-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.wm.getOuterWindowWithId()`
- 条件付き依存: `if (contentWindow.pendingGetUserMediaRequests)` → `forgetGUMRequest()`
- 参照: `aData.callID`, `aData.noOSPermission`, `aData.windowID`, `contentWindow.pendingGetUserMediaRequests`
- XPCOM: `Services.obs` / `Services.wm`

## forgetGUMRequest()
- 位置: L444-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aContentWindow.pendingGetUserMediaRequests.delete()`, `forgetPendingListsEventually()`

## forgetPCRequest()
- 位置: L449-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aContentWindow.pendingPeerConnectionRequests.delete()`, `forgetPendingListsEventually()`

## setupPendingListsInitially()
- 位置: L454-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aContentWindow.addEventListener()`
- 参照: `WebRTCChild.handleEvent`, `aContentWindow.pendingGetUserMediaRequests`, `aContentWindow.pendingPeerConnectionRequests`

## forgetPendingListsEventually()
- 位置: L463-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aContentWindow.removeEventListener()`
- 参照: `WebRTCChild.handleEvent`, `aContentWindow.pendingGetUserMediaRequests`, `aContentWindow.pendingGetUserMediaRequests.size`, `aContentWindow.pendingPeerConnectionRequests`, `aContentWindow.pendingPeerConnectionRequests.size`

## updateIndicators()
- 位置: L475-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aSubject.getProperty()`, `getActorForWindow()`
- 条件付き依存: `if (actor)` → `getTabStateForContentWindow()`
- 条件付き依存: `if (actor)` → `getInnerWindowIDForWindow()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `Ci.nsIPropertyBag`, `actor.suppressNotifications`, `tabState.browser`, `tabState.screen`, `tabState.suppressNotifications`, `tabState.window`, `tabState.windowId`
- XPCOM: [`nsIPropertyBag`](../../toolkit/components/passwordmgr/nsILoginManager.idl.md)

## removeBrowserSpecificIndicator()
- 位置: L506-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getOuterWindowWithId()`, `getActorForWindow()`, `getTabStateForContentWindow()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `contentWindow.document.documentURI`, `tabState.windowId`
- XPCOM: `Services.wm`

## getTabStateForContentWindow()
- 位置: L523-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.MediaManagerService.mediaCaptureWindowState()`
- 条件付き依存: `if (Array.isArray(devices.value))` → `devices.value.map()`
- 参照: `browser.value`, `camera.value`, `device.mediaSource`, `device.rawId`, `device.scary`, `device.type`, `devices.value`, `lazy.MediaManagerService.STATE_NOCAPTURE`, `microphone.value`, `screen.value`, `window.value`

## getInnerWindowIDForWindow()
- 位置: L576-578
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aContentWindow.windowGlobalChild.innerWindowId`
