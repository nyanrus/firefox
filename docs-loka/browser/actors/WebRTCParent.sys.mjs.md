# browser/actors/WebRTCParent.sys.mjs

source: browser/actors/WebRTCParent.sys.mjs
source-hash: a517455fe18d17b355d41d5c6e497bfdd120bb96
lines: 1821

## <module>
- 役割: WebRTC の親プロセス側アクター。子からの許可要求を受け、OS 権限・サイト権限・既存の許可を確認して許可か拒否を返し、必要ならプロンプトを表示する。共有インジケーターの更新も担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## WebRTCParent.didDestroy()
- 位置: L23-32
- 役割: ウィンドウ破棄時に録音を停止し、ストリームの関連付けと activePerms を解放する。
- 触るとき: ページ遷移後や閉じた後に許可や共有状態が残るときに見る。
- 呼び出し先: `lazy.webrtcUI.activePerms.delete()`, `lazy.webrtcUI.forgetStreamsFromBrowserContext()`, `this.stopRecording()`
- 参照: `this.browsingContext`, `this.manager.outerWindowId`

## WebRTCParent.getBrowser()
- 位置: L34-36
- 役割: 最上位のブラウズコンテキストの embedderElement(タブのブラウザー要素)を返す。
- 触るとき: 許可やプロンプトをどのブラウザー要素に紐付けるかを変えるとき。
- 参照: `this.browsingContext.top.embedderElement`

## WebRTCParent.receiveMessage()
- 位置: L38-139
- 役割: 子からの rtcpeer:Request、webrtc:Request、停止、キャンセル、インジケーター更新を振り分けて処理する。
- 触るとき: 子アクターから届くメッセージを追加・変更するとき。
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
- 役割: webrtcUI から共有状態を取り出し、タブとサイドバーのブラウザーに反映する。
- 触るとき: 共有インジケーターがタブに出ない、または古いままのときに見る。
- 呼び出し先: `isSidebarBrowser()`, `lazy.webrtcUI.updateIndicators()`, `this.getBrowser()`
- 条件付き依存: `if (tabbrowser)` → `tabbrowser.updateBrowserSharing()`
- 条件付き依存: `if (isSidebarBrowser(browser))` → `browser.browsingContext.topChromeWindow.SidebarController?._permissions.updateFromBrowserState()`
- 参照: `aData.windowId`, `browser._sharingState`, `browser.documentGlobal.gBrowser`, `browsingContext.top`, `state.browsingContext`, `state.windowId`, `this.browsingContext`

## WebRTCParent.denyRequest()
- 位置: L168-173
- 役割: 子へ webrtc:Deny を送り、要求を拒否する。
- 触るとき: 要求の拒否経路や子の保留解消を調べるとき。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `aRequest.callID`, `aRequest.windowID`

## WebRTCParent.denyRequestNoPermission()
- 位置: L181-187
- 役割: OS 権限がないことを示す noOSPermission 付きで webrtc:Deny を送る。
- 触るとき: OS 権限が無い場合の拒否理由を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `aRequest.callID`, `aRequest.windowID`

## WebRTCParent.checkOSPermission()
- 位置: async L194-238
- 役割: カメラ、マイク、画面共有の OS 権限を順に確認し、必要なら要求する。フェイクデバイス使用時は確認を省く。
- 触るとき: OS 権限の確認順や省略条件を変えるとき。
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
- 役割: 個別デバイスの OS 権限状態を見て、拒否なら false、未決定なら要求の結果を返す。
- 触るとき: 未決定の権限を要求する流れを調べるとき。
- 条件付き依存: `if (devicePermission == lazy.OSPermissions.PERMISSION_STATE_NOTDETERMINED)` → `requestPermissionFunc()`
- 参照: `lazy.OSPermissions.PERMISSION_STATE_DENIED`, `lazy.OSPermissions.PERMISSION_STATE_NOTDETERMINED`, `lazy.OSPermissions.PERMISSION_STATE_RESTRICTED`

## WebRTCParent.stopRecording()
- 位置: L262-280
- 役割: このブラウズコンテキストが使用中のデバイスのうち、指定されたもの(無指定なら全て)を停止させる。
- 触るとき: 共有停止後も権限や猶予期間が残る問題を調べるとき。
- 条件付き依存: `if (browsingContext == this.browsingContext)` → `this.deactivateDevicePerm()`
- 参照: `lazy.webrtcUI._streams`, `state.devices`, `this.browsingContext`

## WebRTCParent.activateDevicePerm()
- 位置: L286-293
- 役割: 使用中のデバイスを activePerms に登録する。猶予期間付きの許可判定で参照される。
- 触るとき: デバイスを使用中と記録する条件を変えるとき。
- 呼び出し先: `lazy.webrtcUI.activePerms .get()`, `lazy.webrtcUI.activePerms .get(this.manager.outerWindowId) .set()`, `lazy.webrtcUI.activePerms.has()`
- 条件付き依存: `if (!lazy.webrtcUI.activePerms.has(this.manager.outerWindowId))` → `lazy.webrtcUI.activePerms.set()`
- 参照: `this.manager.outerWindowId`

## WebRTCParent.deactivateDevicePerm()
- 位置: L303-348
- 役割: 使用中の記録を外し、カメラかマイクなら一時的な猶予許可を付与する。
- 触るとき: 停止直後の再要求で再プロンプトが出る、または出ない問題を調べるとき。
- 呼び出し先: `lazy.webrtcUI.activePerms.get()`, `lazy.webrtcUI.activePerms.has()`, `map.delete()`
- 条件付き依存: `if (gracePeriodMs > 0)` → `[aMediaSource, aId].join()`
- 条件付き依存: `if (gracePeriodMs > 0)` → `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.SCOPE_TEMPORARY`, `lazy.webrtcUI.deviceGracePeriodTimeoutMs`, `this.browsingContext.top.embedderElement`, `this.manager.outerWindowId`

## WebRTCParent.checkRequestAllowed()
- 位置: L357-492
- 役割: 使用中の記録とサイト権限で要求を満たせるか判定し、満たせれば webrtc:Allow を送る。画面共有は常にプロンプトする。
- 触るとき: 許可済みなのに毎回プロンプトが出る、または逆の問題を調べるとき。
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
- 役割: デバイスが使用中か、サイト権限で許可済みかを判定する。
- 触るとき: デバイス単位の許可判定ルールを変えるとき。
- 呼び出し先: `[mediaSource, rawId].join()`, `lazy.SitePermissions.getForPrincipal()`, `map?.get()`, `this.getBrowser()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.getForPrincipal( aPrincipal, [mediaSource, rawId].join("^"), this.getBrowser() ).state`, `lazy.SitePermissions.getForPrincipal(aPrincipal, permissionID).state`

## prompt()
- 位置: L495-1409
- 役割: 要求内容に応じてプロンプトを組み立てて表示する。アドオン、既拒否の即時拒否、デバイス選択 UI、許可と拒否の処理を含む。
- 触るとき: 許可プロンプトの表示内容や動作を変えるとき。
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
- 役割: スピーカー選択や画面共有の「今はしない」「ブロック」で拒否し、必要なら一時的な BLOCK を設定する。
- 触るとき: スピーカーや画面共有の拒否時の保存範囲を変えるとき。
- 呼び出し先: `aActor.denyRequest()`
- 条件付き依存: `if (!isNotNowLabelEnabled)` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!isNotNowLabelEnabled)` → `aActor.getBrowser()`
- 参照: `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_TEMPORARY`

## callback()
- 位置: L649-658
- 役割: スピーカー選択や画面共有の「常にブロック」で拒否し、永続の BLOCK を設定する。
- 触るとき: 常にブロックの保存先や挙動を変えるとき。
- 呼び出し先: `aActor.denyRequest()`, `aActor.getBrowser()`, `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`

## callback()
- 位置: L671-726
- 役割: カメラやマイクの「今はしない」「ブロック」で拒否し、保存指定に応じて永続または一時の BLOCK を設定し、猶予許可を消す。
- 触るとき: カメラやマイクの拒否時の保存範囲や猶予許可の扱いを変えるとき。
- 呼び出し先: `aActor.denyRequest()`, `aActor.getBrowser()`, `clearTemporaryGrants()`
- 条件付き依存: `if (!isPersistent)` → `maybeClearAlwaysAsk()`
- 条件付き依存: `if (reqAudioInput)` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!isPersistent && !sharingScreen)` → `maybeClearAlwaysAsk()`
- 条件付き依存: `if (reqVideoInput)` → `lazy.SitePermissions.setForPrincipal()`
- 参照: `aState?.checkboxChecked`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_TEMPORARY`

## callback()
- 位置: L750-750
- 役割: PopupNotifications の要件を満たすための空の仮 callback。実際の許可処理は showing 時に差し替える。
- 触るとき: 許可ボタンの動作を調べるときは this.mainAction.callback を見る。

## eventCallback()
- 位置: L762-1271
- 役割: 通知のイベント(swapping、showing、shown、removed 等)を処理する。表示時に既許可なら自動許可し、初回表示でデバイス選択 UI を組み立てる。
- 触るとき: プロンプトの表示状態に応じた UI 処理を変えるとき。
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
- 役割: カメラ、マイク、スピーカーの選択リストを作り直す。デバイスが一つだけならラベル表示に切り替える。
- 触るとき: デバイス選択 UI の表示が崩れるときに見る。
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
- 役割: 選択中のウィンドウ項目が無効なら、通知に invalidselection を付けて許可を押せないようにする。
- 触るとき: 画面共有で許可ボタンの有効無効が合わないときに見る。
- 呼び出し先: `doc.getElementById()`, `item.hasAttribute()`
- 条件付き依存: `if (!item || item.hasAttribute("disabled"))` → `notificationElement.setAttribute()`
- 条件付き依存: `if (!(!item || item.hasAttribute("disabled")))` → `notificationElement.removeAttribute()`
- 参照: `list.selectedItem`

## listScreenShareDevices()
- 位置: L920-1076
- 役割: 画面共有の選択肢を作る。PipeWire 時は単一項目にし、モニターに番号を振り、アプリ名と窓数を整形する。
- 触るとき: 画面共有の選択肢の表示名や並びを変えるとき。
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
- 役割: 画面共有の選択が変わったとき、危険なソースの警告を出し、プレビューを開始する。
- 触るとき: 画面共有のプレビューや警告の出し方を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `checkDisabledWindowMenuItem()`, `doc.getElementById()`, `perms.addFromPrincipal()`
- 条件付き依存: `if (scary)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (scary)` → `lazy.OSPermissions.getScreenCapturePermissionState()`
- 条件付き依存: `if (scrStatus.value == lazy.OSPermissions.PERMISSION_STATE_DENIED)` → `lazy.OSPermissions.maybeRequestScreenCapturePermission()`
- 条件付き依存: `if ( (!isPipeWireDetected || mediaSource == "browser") && Services.prefs.getBoolPref( "media.getdisplaymedia.previews.enabled", true ) )` → `webrtcPreview.startPreview()`
- 参照: `Services.perms`, `event.target`, `lazy.OSPermissions.PERMISSION_STATE_DENIED`, `perms.ALLOW_ACTION`, `perms.EXPIRE_SESSION`, `scrStatus.value`, `warningBox.hidden`, `webrtcPreviewSection.hidden`
- XPCOM: `Services.perms` / `Services.prefs` / `Services.scriptSecurityManager`

## addDeviceToList()
- 位置: L1078-1090
- 役割: リストに項目を追加し、tooltip と devicetype を設定する。index が -1 の項目は無効化する。
- 触るとき: 選択リストの項目の属性を変えるとき。
- 呼び出し先: `item.setAttribute()`, `list.appendItem()`
- 条件付き依存: `if (type)` → `item.setAttribute()`
- 条件付き依存: `if (deviceIndex == "-1")` → `item.setAttribute()`

## cameraMenuPopup._commandEventListener()
- 位置: L1137-1145
- 役割: カメラ選択が変わったら、そのカメラでプレビューを開始する。
- 触るとき: カメラプレビューの切り替えを調べるとき。
- 呼び出し先: `webrtcPreview.startPreview()`
- 参照: `event.target`, `webrtcPreviewSection.hidden`

## this.mainAction.callback()
- 位置: async L1169-1267
- 役割: 許可ボタンの処理。選ばれたデバイスについて許可を作り、必要なら永続化し、OS 権限を確認してから webrtc:Allow を送る。何も選ばれなければ拒否する。
- 触るとき: 許可後に子へ渡すデバイスや記憶の扱いを変えるとき。
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
- 役割: 「次回も許可」チェックボックスを出すかを決める。プライベートブラウズ、委譲、スピーカーの要求では出さない。
- 触るとき: チェックボックスの表示条件を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `aRequest.secondOrigin`

## getRememberCheckboxLabel()
- 位置: L1294-1307
- 役割: 要求種別に応じた「記憶」チェックボックスのローカライズ ID を返す。
- 触るとき: チェックボックスの文言を変えるとき。

## onUnload()
- 位置: L1398-1404
- 役割: PiP ウィンドウが閉じたとき、まだ有効なアクターなら要求を拒否する。
- 触るとき: PiP 上の許可プロンプトが閉じた後に要求が残る問題を調べるとき。
- 呼び出し先: `aActor.denyRequest()`
- 参照: `aActor.manager`, `aActor.manager.isClosed`

## stopWatchingPromptWindow()
- 位置: L1406-1407
- 役割: PiP ウィンドウの unload 監視を解除する関数を作る。
- 触るとき: PiP 上のプロンプトの後片付けを変えるとき。
- 呼び出し先: `promptWindow.removeEventListener()`

## getPromptMessageId()
- 位置: L1419-1515
- 役割: 要求種別、委譲の有無、ファイル由来かに応じて、プロンプト文言のローカライズ ID を返す。
- 触るとき: プロンプトの文言を追加・変更するとき。

## allowedOrActiveCameraOrMicrophone()
- 位置: L1524-1559
- 役割: カメラかマイクに許可があるか、またはブラウザー内で使用中かを判定する。
- 触るとき: 拒否ボタンを「今はしない」にするかなどの判定を調べるとき。
- 呼び出し先: `browser.browsingContext .getAllBrowsingContextsInSubtree()`, `browser.browsingContext .getAllBrowsingContextsInSubtree() // Only keep the outerWindowIds .map()`, `lazy.SitePermissions.getAllForBrowser()`, `lazy.SitePermissions.getAllForBrowser(browser).some()`, `lazy.webrtcUI.activePerms.get()`, `map.values()`, `perm.id.startsWith()`, `types.includes()`
- 参照: `bc.currentWindowGlobal?.outerWindowId`, `lazy.SitePermissions.ALLOW`, `perm.state`

## removePrompt()
- 位置: L1561-1567
- 役割: callID が一致するプロンプトを、ブラウザー側と PiP 側から探して削除する。
- 触るとき: 取り消された要求のプロンプトが消えないときに見る。
- 呼び出し先: `removePromptFrom()`
- 条件付き依存: `if (!removePromptFrom(aBrowser, aCallId))` → `removePromptFrom()`
- 条件付き依存: `if (!removePromptFrom(aBrowser, aCallId))` → `getDocumentPiPBrowser()`

## removePromptFrom()
- 位置: L1569-1580
- 役割: 指定ブラウザーのウィンドウから callID が一致する通知を探し、一致すれば削除する。
- 触るとき: 通知の削除対象の判定を変えるとき。
- 呼び出し先: `chromeWin?.PopupNotifications.getNotification()`, `notification.remove()`
- 参照: `aBrowser?.browsingContext?.topChromeWindow`, `notification.callID`

## clearTemporaryGrants()
- 位置: L1589-1611
- 役割: カメラやマイクの一時的な猶予許可(キー付きの一時許可)を削除する。
- 触るとき: 拒否後も猶予許可が残るときに見る。
- 呼び出し先: `lazy.SitePermissions.getAllForBrowser()`, `lazy.SitePermissions.removeFromPrincipal()`, `perm.id.split()`, `perms .filter()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.PERM_KEY_DELIMITER`, `lazy.SitePermissions.SCOPE_TEMPORARY`, `perm.id`, `perm.scope`, `perm.state`

## persistGrantOrPromptPermission()
- 位置: L1624-1640
- 役割: 記憶指定があれば ALLOW、無ければ PROMPT を保存する。既に ALLOW なら何もしない。
- 触るとき: 次回以降の許可の扱いを変えるとき。
- 呼び出し先: `lazy.SitePermissions.getForPrincipal()`, `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.PROMPT`, `lazy.SitePermissions.getForPrincipal(principal, permissionName).state`

## maybeClearAlwaysAsk()
- 位置: L1649-1662
- 役割: 保存されている PROMPT の状態を削除する。一時的な拒否の後に使う。
- 触るとき: 拒否後に permissions.query の結果が誤解を招く問題を調べるとき。
- 呼び出し先: `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if ( lazy.SitePermissions.getForPrincipal(principal, permissionName).state == lazy.SitePermissions.PROMPT )` → `lazy.SitePermissions.removeFromPrincipal()`
- 参照: `lazy.SitePermissions.PROMPT`, `lazy.SitePermissions.getForPrincipal(principal, permissionName).state`

## getOrCreateWebRTCPreviewEl()
- 位置: L1670-1679
- 役割: プレビュー要素が無ければ作成し、プレビュー欄の先頭に入れて返す。
- 触るとき: プレビュー要素の配置や生成方法を変えるとき。
- 呼び出し先: `chromeDoc.getElementById()`, `previewSection.querySelector()`
- 条件付き依存: `if (!previewEl)` → `chromeDoc.createElement()`
- 条件付き依存: `if (!previewEl)` → `previewSection.insertBefore()`
- 参照: `previewEl.id`, `previewSection.firstChild`

## onCameraPromptShown()
- 位置: L1693-1715
- 役割: ユーザー操作によるカメラ要求のときだけ、選択中のカメラでプレビューを自動開始する。
- 触るとき: カメラプレビューが自動で始まる条件を変えるとき。
- 呼び出し先: `cameraMenuPopup?.querySelector()`, `doc.getElementById()`, `webrtcPreview?.startPreview()`
- 参照: `cameraMenuPopup?.querySelector("[selected]")?.deviceId`, `doc.getElementById("webRTC-preview-section").hidden`

## getDocumentPiPBrowser()
- 位置: L1724-1733
- 役割: 指定ブラウザーを開いた Document PiP ウィンドウのブラウザー要素を返す。無ければ null。
- 触るとき: PiP 上のプロンプトや許可の扱いを調べるとき。
- 呼び出し先: `openerBC.group .getToplevels()`, `openerBC.group .getToplevels() .find()`
- 参照: `aBrowser.browsingContext`, `bc.isDocumentPiP`, `bc.opener`, `openerBC.isDocumentPiP`, `pipBC?.embedderElement`

## getPromptBrowser()
- 位置: L1753-1771
- 役割: 画面共有で PiP が前面かつ開いた側が全画面でなければ、プロンプトを PiP 側に出す。それ以外は開いた側に出す。
- 触るとき: プロンプトを出すウィンドウの判定を変えるとき。
- 呼び出し先: `getDocumentPiPBrowser()`
- 参照: `Services.focus.activeWindow`, `aBrowser.browsingContext?.topChromeWindow?.document.fullscreenElement`, `aRequest.sharingScreen`, `pipBrowser?.browsingContext?.topChromeWindow`
- XPCOM: `Services.focus`

## isSidebarBrowser()
- 位置: L1773-1783
- 役割: ブラウザー要素がサイドバーの中のブラウザーかを判定する。
- 触るとき: サイドバーでの共有表示や許可 UI を扱うとき。
- 呼び出し先: `Array.from()`, `Array.from(nestedBrowsers).some()`, `sidebarBrowser.contentDocument.querySelectorAll()`
- 参照: `browser.browsingContext?.topChromeWindow?.SidebarController?.browser`

## maybeShowPopupNotificationInSidebar()
- 位置: L1789-1820
- 役割: 要求元がサイドバーなら、サイドバーの通知として許可プロンプトを出し、通知を返す。サイドバーでなければ null。
- 触るとき: サイドバーでの許可 UI を調べるとき。
- 呼び出し先: `isSidebarBrowser()`, `sidebarPopupNotifications.show()`
- 参照: `aBrowser.browsingContext?.topChromeWindow`, `aRequest.callID`, `notification.callID`, `win?.SidebarPopupNotifications`
