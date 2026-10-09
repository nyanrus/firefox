# browser/actors/WebRTCChild.sys.mjs

source: browser/actors/WebRTCChild.sys.mjs
source-hash: 7710de00d187ea804a0699b40e251b48864a353e
lines: 579

## <module>
- 役割: WebRTC の子プロセス側アクター。getUserMedia と PeerConnection の要求を親へ中継し、親からの許可・拒否・ミュート指示を DOM 側へ反映する。
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`

## init()
- 位置: L32-39
- 役割: GlobalMuteListener を一度だけ初期化し、共有データの変更監視を始めて現在のカメラ・マイクのミュート状態を反映する。
- 触るとき: 全体ミュート(グローバルミュート)が初期状態で効かない、または初期化のタイミングを調べるとき。
- 条件付き依存: `if (!this._initted)` → `Services.cpmm.sharedData.addEventListener()`
- 条件付き依存: `if (!this._initted)` → `this._updateCameraMuteState()`
- 条件付き依存: `if (!this._initted)` → `this._updateMicrophoneMuteState()`
- 参照: `this._initted`
- XPCOM: `Services.cpmm`

## handleEvent()
- 位置: L41-48
- 役割: 共有データの変更キーを見て、カメラまたはマイクのグローバルミュート状態を再反映する。
- 触るとき: 全体ミュートの変更が DOM 側に届かないときに見る。
- 呼び出し先: `event.changedKeys.includes()`
- 条件付き依存: `if (event.changedKeys.includes("WebRTC:GlobalCameraMute"))` → `this._updateCameraMuteState()`
- 条件付き依存: `if (event.changedKeys.includes("WebRTC:GlobalMicrophoneMute"))` → `this._updateMicrophoneMuteState()`

## _updateCameraMuteState()
- 位置: L50-56
- 役割: 共有データの WebRTC:GlobalCameraMute を読み、muteVideo か unmuteVideo を observer で通知する。
- 触るとき: カメラの全体ミュートが反映されない問題を調べるとき。
- 呼び出し先: `Services.cpmm.sharedData.get()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.cpmm` / `Services.obs`

## _updateMicrophoneMuteState()
- 位置: L58-67
- 役割: 共有データの WebRTC:GlobalMicrophoneMute を読み、muteAudio か unmuteAudio を observer で通知する。
- 触るとき: マイクの全体ミュートが反映されない問題を調べるとき。
- 呼び出し先: `Services.cpmm.sharedData.get()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.cpmm` / `Services.obs`

## WebRTCChild.actorCreated()
- 位置: L71-81
- 役割: アクター生成時に suppressNotifications を false にして、画面共有中の通知抑制の初期値を決める。
- 触るとき: 画面共有時の DOM 通知の抑制状態を変えるとき。
- 参照: `this.suppressNotifications`

## WebRTCChild.handleEvent()
- 位置: L84-95
- 役割: ウィンドウの unload 時に、そのウィンドウに残る GUM と PeerConnection の保留要求を親へキャンセル通知する。
- 触るとき: リロードや遷移後も許可プロンプトが残るときに見る。
- 呼び出し先: `getActorForWindow()`
- 条件付き依存: `if (actor)` → `contentWindow.pendingGetUserMediaRequests.keys()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (actor)` → `contentWindow.pendingPeerConnectionRequests.keys()`
- 参照: `aEvent.target.defaultView`

## WebRTCChild.observe()
- 位置: L99-117
- 役割: WebRTC 関連の observer トピックを、対応する処理関数へ振り分ける。
- 触るとき: 新しい WebRTC 通知を追加する、または通知ごとの処理先を調べるとき。
- 呼び出し先: `handleGUMRequest()`, `handleGUMStop()`, `handlePCRequest()`, `removeBrowserSpecificIndicator()`, `updateIndicators()`

## WebRTCChild.receiveMessage()
- 位置: L119-199
- 役割: 親からの許可・拒否・停止・ミュート要求を受け、保留リストを解消して observer 通知を出す。
- 触るとき: 親子間の WebRTC メッセージを追加・変更するとき。
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.wm.getOuterWindowWithId()`, `allowedDevices.appendElement()`, `contentWindow.pendingGetUserMediaRequests.get()`, `denyGUMRequest()`, `forgetGUMRequest()`, `forgetPCRequest()`
- 参照: `Ci.nsIMutableArray`, `aMessage.data`, `aMessage.data.callID`, `aMessage.data.devices`, `aMessage.data.suppressNotifications`, `aMessage.data.windowID`, `aMessage.name`, `this.suppressNotifications`
- XPCOM: [`nsIMutableArray`](../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1` / `Services.obs` / `Services.wm`

## getActorForWindow()
- 位置: L202-214
- 役割: ウィンドウの windowGlobalChild から WebRTC アクターを取り出す。取れなければ null を返す。
- 触るとき: ウィンドウに対応するアクターへ送信する処理を追うとき。
- 条件付き依存: `if (windowGlobal)` → `windowGlobal.getActor()`
- 参照: `window.windowGlobalChild`

## handlePCRequest()
- 位置: L216-236
- 役割: PeerConnection の要求を保留リストに登録し、rtcpeer:Request として親へ送る。
- 触るとき: PeerConnection の許可フローの開始部分を調べるとき。
- 呼び出し先: `Services.wm.getOuterWindowWithId()`, `contentWindow.pendingPeerConnectionRequests.add()`, `getActorForWindow()`
- 条件付き依存: `if (!contentWindow.pendingPeerConnectionRequests)` → `setupPendingListsInitially()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `contentWindow.document.documentURI`, `contentWindow.pendingPeerConnectionRequests`
- XPCOM: `Services.wm`

## handleGUMStop()
- 位置: L238-251
- 役割: 録音・録画デバイスが止まったことを webrtc:StopRecording で親へ送る。
- 触るとき: デバイス停止時のインジケーター更新を調べるとき。
- 呼び出し先: `Services.wm.getOuterWindowWithId()`, `getActorForWindow()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `aSubject.mediaSource`, `aSubject.rawID`, `aSubject.windowID`
- XPCOM: `Services.wm`

## handleGUMRequest()
- 位置: L253-275
- 役割: 全体ミュートを初期化してから、GUM 要求の制約とデバイス情報を集めて prompt へ渡す。
- 触るとき: getUserMedia 要求が DOM 側から届いた後の流れを追うとき。
- 呼び出し先: `GlobalMuteListener.init()`, `Services.wm.getOuterWindowWithId()`, `aSubject.getAudioOutputOptions()`, `aSubject.getConstraints()`, `prompt()`
- 参照: `aSubject.callID`, `aSubject.devices`, `aSubject.isHandlingUserInput`, `aSubject.isSecure`, `aSubject.type`, `aSubject.windowID`
- XPCOM: `Services.wm`

## prompt()
- 位置: L277-424
- 役割: デバイスを入力・出力の種類ごとに分け、要求種別(カメラ、画面、マイク等)を決めて webrtc:Request として親へ送る。デバイスが無ければ即拒否する。
- 触るとき: 許可プロンプトに出る内容や要求種別の判定を変えるとき。
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
- 役割: deviceId、facingMode、groupId のいずれかが指定されているかを判定する。default の deviceId は指定とみなさない。
- 触るとき: 制約付きの要求でプロンプトを省略する条件を調べるとき。
- 呼び出し先: `[deviceId].flat()`

## denyGUMRequest()
- 位置: L426-442
- 役割: OS 権限が無い場合は noOSPermission、それ以外は deny を通知し、保留中の要求を後始末する。
- 触るとき: 拒否時の通知種別や保留要求の後始末を調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.wm.getOuterWindowWithId()`
- 条件付き依存: `if (contentWindow.pendingGetUserMediaRequests)` → `forgetGUMRequest()`
- 参照: `aData.callID`, `aData.noOSPermission`, `aData.windowID`, `contentWindow.pendingGetUserMediaRequests`
- XPCOM: `Services.obs` / `Services.wm`

## forgetGUMRequest()
- 位置: L444-447
- 役割: 保留中の GUM 要求を削除し、保留リストの片付けを予約する。
- 触るとき: 保留要求が残る、または早く消えすぎるときに見る。
- 呼び出し先: `aContentWindow.pendingGetUserMediaRequests.delete()`, `forgetPendingListsEventually()`

## forgetPCRequest()
- 位置: L449-452
- 役割: 保留中の PeerConnection 要求を削除し、保留リストの片付けを予約する。
- 触るとき: PeerConnection の保留要求が残るときに見る。
- 呼び出し先: `aContentWindow.pendingPeerConnectionRequests.delete()`, `forgetPendingListsEventually()`

## setupPendingListsInitially()
- 位置: L454-461
- 役割: ウィンドウに保留用の Map と Set を作り、unload の監視を登録する。既にあれば何もしない。
- 触るとき: 保留リストの初期化条件を変えるとき。
- 呼び出し先: `aContentWindow.addEventListener()`
- 参照: `WebRTCChild.handleEvent`, `aContentWindow.pendingGetUserMediaRequests`, `aContentWindow.pendingPeerConnectionRequests`

## forgetPendingListsEventually()
- 位置: L463-473
- 役割: 両方の保留リストが空なら、ウィンドウ上のリストと unload 監視を外す。
- 触るとき: 保留リストを解放するタイミングを調べるとき。
- 呼び出し先: `aContentWindow.removeEventListener()`
- 参照: `WebRTCChild.handleEvent`, `aContentWindow.pendingGetUserMediaRequests`, `aContentWindow.pendingGetUserMediaRequests.size`, `aContentWindow.pendingPeerConnectionRequests`, `aContentWindow.pendingPeerConnectionRequests.size`

## updateIndicators()
- 位置: L475-504
- 役割: デバイス状態からタブ単位の状態を作り、webrtc:UpdateIndicators で親へ送る。ブラウザ自身のプレビューは無視する。
- 触るとき: 共有インジケーターの表示が実態とずれるときに見る。
- 呼び出し先: `aSubject.getProperty()`, `getActorForWindow()`
- 条件付き依存: `if (actor)` → `getTabStateForContentWindow()`
- 条件付き依存: `if (actor)` → `getInnerWindowIDForWindow()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `Ci.nsIPropertyBag`, `actor.suppressNotifications`, `tabState.browser`, `tabState.screen`, `tabState.suppressNotifications`, `tabState.window`, `tabState.windowId`
- XPCOM: [`nsIPropertyBag`](../../toolkit/components/passwordmgr/nsILoginManager.idl.md)

## removeBrowserSpecificIndicator()
- 位置: L506-521
- 役割: 録画ウィンドウが終わったとき、そのウィンドウの状態を削除扱いにして親へ通知する。
- 触るとき: 録画終了後もインジケーターが残るときに見る。
- 呼び出し先: `Services.wm.getOuterWindowWithId()`, `getActorForWindow()`, `getTabStateForContentWindow()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `contentWindow.document.documentURI`, `tabState.windowId`
- XPCOM: `Services.wm`

## getTabStateForContentWindow()
- 位置: L523-574
- 役割: MediaManagerService からカメラ、マイク、画面などの取得状態を読み、送信用のオブジェクトにまとめる。全て無しなら remove 扱い。
- 触るとき: インジケーターに渡す状態の項目を増やす、または判定を変えるとき。
- 呼び出し先: `Array.isArray()`, `lazy.MediaManagerService.mediaCaptureWindowState()`
- 条件付き依存: `if (Array.isArray(devices.value))` → `devices.value.map()`
- 参照: `browser.value`, `camera.value`, `device.mediaSource`, `device.rawId`, `device.scary`, `device.type`, `devices.value`, `lazy.MediaManagerService.STATE_NOCAPTURE`, `microphone.value`, `screen.value`, `window.value`

## getInnerWindowIDForWindow()
- 位置: L576-578
- 役割: ウィンドウの windowGlobalChild から innerWindowId を返す。
- 触るとき: 内側ウィンドウの ID を必要とする通知を追加するとき。
- 参照: `aContentWindow.windowGlobalChild.innerWindowId`
