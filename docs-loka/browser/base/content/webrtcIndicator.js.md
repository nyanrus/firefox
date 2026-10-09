# browser/base/content/webrtcIndicator.js

source: browser/base/content/webrtcIndicator.js
source-hash: aedb10cd7a00201145834456def5515a2ed74595
lines: 594

## <module>
- 役割: WebRTC のグローバルインジケーター(共有中の表示と、カメラ・マイクのグローバルミュート)を制御するウィンドウのスクリプト。
- 呼び出し先: `ChromeUtils.importESModule()`, `WebRTCIndicator.init()`, `XPCOMUtils.defineLazyServiceGetter()`

## updateIndicatorState()
- 位置: L26-28
- 役割: webrtcUI から呼ばれる公開関数。WebRTCIndicator.updateIndicatorState に委譲する。
- 触るとき: 共有状態が変わってもインジケーターが更新されないときに、呼び出し元から届いているかを確かめるときに見る。
- 呼び出し先: `WebRTCIndicator.updateIndicatorState()`

## closingInternally()
- 位置: L42-44
- 役割: webrtcUI が閉じる前に呼ぶ公開関数。WebRTCIndicator.closingInternally に委譲する。
- 触るとき: インジケーターを閉じたときに共有が止まってしまう、または止まらないときに見る。
- 呼び出し先: `WebRTCIndicator.closingInternally()`

## init()
- 位置: L50-78
- 役割: load と unload を登録し、グローバルミュートとインジケーター非表示の pref を読み、非表示なら setVisibility(false) を呼ぶ。
- 触るとき: 起動時にインジケーターが見えない、またはミュートの表示が出ないときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `addEventListener()`
- 条件付き依存: `if (this.hideGlobalIndicator)` → `this.setVisibility()`
- 参照: `Services.appinfo.isWayland`, `this.hideGlobalIndicator`, `this.isClosingInternally`, `this.loaded`, `this.positionCustomized`, `this.showGlobalMuteToggles`, `this.statusBar`, `this.statusBarMenus`, `this.updatingIndicatorState`
- XPCOM: `Services.appinfo` / `Services.prefs`

## setVisibility()
- 位置: L87-95
- 役割: ウィンドウの visibility を設定し、文書の visible 属性にも同じ値を書いてテストから判定できるようにする。
- 触るとき: インジケーターの表示・非表示が切り替わらないときに見る。
- 呼び出し先: `document.documentElement.setAttribute()`, `window.docShell.treeOwner.QueryInterface()`
- 参照: `Ci.nsIBaseWindow`, `baseWin.visibility`
- XPCOM: `nsIBaseWindow`

## updateIndicatorState()
- 位置: L101-228
- 役割: カメラ・マイク・画面共有の状態を読み、ステータスバーのメニューを増減し、表示と非表示を切り替え、ミュート属性とラベルを更新してから、サイズと位置を整える。
- 触るとき: インジケーターの項目や位置が共有状態と食い違うとき、またはステータスバーの項目を足すときに見る。
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
- 役割: ウィンドウが大きくなって画面外にはみ出したとき、画面内に収まるよう moveTo で位置を補正する。
- 触るとき: インジケーターが画面端から見切れると報告されたときに見る。
- 呼び出し先: `Math.max()`, `Math.min()`, `window.moveTo()`
- 参照: `document.documentElement.clientWidth`, `screen.availLeft`, `screen.availWidth`, `window.screenX`, `window.screenY`

## centerOnLatestBrowser()
- 位置: L249-281
- 役割: 最後に共有されたストリームのブラウザを探し、そのブラウザ上端の中央にインジケーターを移動する。
- 触るとき: インジケーターの初期位置がずれるとき、または位置の基準を変えるときに見る。
- 呼び出し先: `browserWindow.windowUtils.getBoundsWithoutFlushing()`, `webrtcUI.getActiveStreams()`, `window.moveTo()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `activeStreams.length`, `activeStreams[activeStreams.length - 1].browser`, `browser.documentGlobal`, `browserRect.left`, `browserRect.top`, `browserRect.width`, `browserWindow.mozInnerScreenX`, `browserWindow.mozInnerScreenY`, `document.documentElement`

## handleEvent()
- 位置: L283-333
- 役割: イベント種別ごとに onLoad、onUnload、onClick、onChange などへ振り分け、ウィンドウ位置の変化で positionCustomized を立てる。
- 触るとき: 新しいイベントを扱うとき、または特定の操作で想定外の処理が走るときに見る。
- 呼び出し先: `this.onChange()`, `this.onClick()`, `this.onClose()`, `this.onCommand()`, `this.onLoad()`, `this.onPopupHiding()`, `this.onPopupShowing()`, `this.onUnload()`
- 条件付き依存: `if (window.windowState != window.STATE_MINIMIZED)` → `this.updateIndicatorState()`
- 参照: `event.type`, `this.positionCustomized`, `this.updatingIndicatorState`, `window.STATE_MINIMIZED`, `window.windowState`

## onLoad()
- 位置: L335-375
- 役割: ステータスバーを取得し、状態を反映し、クリックなどのイベントを登録して AlertActive を発火する。
- 触るとき: インジケーターの初期化処理に項目を足す、または読み込み後の状態が正しくないときに見る。
- 呼び出し先: `document.documentElement.dispatchEvent()`, `this.updateIndicatorState()`, `window.addEventListener()`, `window.windowRoot.addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx" || AppConstants.platform == "win")` → `Cc["@mozilla.org/widget/systemstatusbar;1"].getService()`
- 条件付き依存: `if (this.statusBar)` → `window.addEventListener()`
- 参照: `AppConstants.platform`, `Ci.nsISystemStatusBar`, `this.loaded`, `this.statusBar`
- XPCOM: `nsISystemStatusBar` / `@mozilla.org/widget/systemstatusbar;1`

## onClose()
- 位置: L377-418
- 役割: カメラかマイクを共有中で、グローバルミュートが無効なら閉じる操作を止めて非表示にする。webrtcUI 以外から閉じられた場合は共有ストリームを停止する。
- 触るとき: インジケーターを閉じたのに共有が続く、または閉じられないといったときに見る。
- 条件付き依存: `if ( !this.showGlobalMuteToggles && (webrtcUI.showCameraIndicator || webrtcUI.showMicrophoneIndicator) )` → `event.preventDefault()`
- 条件付き依存: `if ( !this.showGlobalMuteToggles && (webrtcUI.showCameraIndicator || webrtcUI.showMicrophoneIndicator) )` → `this.setVisibility()`
- 条件付き依存: `if (!this.isClosingInternally)` → `webrtcUI.getActiveStreams()`
- 条件付き依存: `if (!this.isClosingInternally)` → `webrtcUI.stopSharingStreams()`
- 参照: `this.isClosingInternally`, `this.showGlobalMuteToggles`, `webrtcUI.showCameraIndicator`, `webrtcUI.showMicrophoneIndicator`

## onUnload()
- 位置: L420-430
- 役割: グローバルのカメラ・マイクのミュート状態を false に戻して共有データを送り、ステータスバーの項目を外す。
- 触るとき: ウィンドウを閉じた後にミュート状態が残ってしまうときに見る。
- 呼び出し先: `Services.ppmm.sharedData.flush()`, `Services.ppmm.sharedData.set()`
- 条件付き依存: `if (this.statusBar)` → `this.statusBar.removeItem()`
- 参照: `this.statusBar`, `this.statusBarMenus`
- XPCOM: `Services.ppmm`

## onClick()
- 位置: L432-466
- 役割: stop-sharing ボタンでは画面・タブ・ウィンドウの共有ストリームを停止し、minimize ボタンではウィンドウを最小化する。
- 触るとき: 共有停止ボタンで止まらない、または他のデバイスも止まってしまうと報告されたときに見る。
- 呼び出し先: `webrtcUI.getActiveStreams()`, `webrtcUI.stopSharingStreams()`, `window.minimize()`
- 参照: `activeStreams.length`, `event.target.id`

## onChange()
- 位置: L468-479
- 役割: マイクとカメラのミュートトグルの変化を、対応する toggleMicrophoneMute または toggleCameraMute に渡す。
- 触るとき: ミュートのトグルが効かないときに、ID と処理の対応を確かめるときに見る。
- 呼び出し先: `this.toggleCameraMute()`, `this.toggleMicrophoneMute()`
- 参照: `event.target`, `event.target.id`

## onPopupShowing()
- 位置: L481-495
- 役割: デバイス用のメニューが開くとき、インジケーターが勝手に出ないよう必要なら非表示を保ち、showStreamSharingMenu を呼ぶ。
- 触るとき: システムトレイのメニューを開いた拍子にインジケーターが表示されるときに見る。
- 呼び出し先: `this.eventIsForDeviceMenuPopup()`
- 条件付き依存: `if (this.eventIsForDeviceMenuPopup(event))` → `document.documentElement.getAttribute()`
- 条件付き依存: `if (document.documentElement.getAttribute("visible") != "true")` → `window.docShell.treeOwner.QueryInterface()`
- 条件付き依存: `if (this.eventIsForDeviceMenuPopup(event))` → `showStreamSharingMenu()`
- 参照: `Ci.nsIBaseWindow`, `baseWin.visibility`
- XPCOM: `nsIBaseWindow`

## onPopupHiding()
- 位置: L497-506
- 役割: デバイスメニューが閉じたら、その子要素をすべて削除する。
- 触るとき: メニューの項目が次回開いたときに残って重複するときに見る。
- 呼び出し先: `menu.firstChild.remove()`, `this.eventIsForDeviceMenuPopup()`
- 参照: `event.target`, `menu.firstChild`

## onCommand()
- 位置: L508-510
- 役割: メニュー項目のコマンドで、対象ストリームの共有ドアハンガーを webrtcUI.showSharingDoorhanger で開く。
- 触るとき: インジケーターのメニュー項目から共有の詳細が開かないときに見る。
- 呼び出し先: `webrtcUI.showSharingDoorhanger()`
- 参照: `event.target.stream`

## eventIsForDeviceMenuPopup()
- 位置: L521-526
- 役割: イベントの対象が type 属性で Camera、Microphone、Screen のいずれかのメニューかを判定する。
- 触るとき: デバイスメニューの種類を増やすとき、またはメニューの判定が外れるときに見る。
- 呼び出し先: `["Camera", "Microphone", "Screen"].includes()`, `menupopup.getAttribute()`
- 参照: `event.target`

## toggleMicrophoneMute()
- 位置: L537-547
- 役割: マイクのグローバルミュートを共有データに書き、そのチェック状態に合わせてトグルのラベルを切り替える。
- 触るとき: マイクのミュートが他のタブに伝わらない、またはラベルが違うときに見る。
- 呼び出し先: `Services.ppmm.sharedData.flush()`, `Services.ppmm.sharedData.set()`, `document.l10n.setAttributes()`
- 参照: `toggleEl.checked`
- XPCOM: `Services.ppmm`

## toggleCameraMute()
- 位置: L558-565
- 役割: カメラのグローバルミュートを共有データに書き、そのチェック状態に合わせてトグルのラベルを切り替える。
- 触るとき: カメラのミュートが他のタブに伝わらない、またはラベルが違うときに見る。
- 呼び出し先: `Services.ppmm.sharedData.flush()`, `Services.ppmm.sharedData.set()`, `document.l10n.setAttributes()`
- 参照: `toggleEl.checked`
- XPCOM: `Services.ppmm`

## updateWindowAttr()
- 位置: L576-583
- 役割: 値が真なら文書の属性を true にし、偽なら属性を削除する。
- 触るとき: インジケーターの表示や装飾が状態と合わないときに、どの属性を使うかを確かめるときに見る。
- 条件付き依存: `if (value)` → `docEl.setAttribute()`
- 条件付き依存: `if (!(value))` → `docEl.removeAttribute()`
- 参照: `document.documentElement`

## closingInternally()
- 位置: L588-590
- 役割: isClosingInternally を true にし、ウィンドウを閉じるときに共有を止めない扱いにする。
- 触るとき: インジケーターが webrtcUI の操作で閉じられるのに共有が止まるときに見る。
- 参照: `this.isClosingInternally`
