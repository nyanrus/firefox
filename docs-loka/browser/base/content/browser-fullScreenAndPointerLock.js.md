# browser/base/content/browser-fullScreenAndPointerLock.js

source: browser/base/content/browser-fullScreenAndPointerLock.js
source-hash: d9756908a7fb6ed43db4c1b528391c8f7446a2cf
lines: 1267

## <module>
- 役割: ウィンドウ全画面化、DOM 全画面化、ポインターロックの警告表示、ツールバーの自動収納を管理する
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Object.values()`, `Object.values(PermissionUI) .filter()`

## constructor()
- 位置: L15-19
- 役割: コールバックと遅延時間を保持し、タイマー ID を 0 にする。
- 触るとき: 警告の表示・非表示タイマーの生成条件を変えるとき。
- 参照: `this._delay`, `this._func`, `this._id`

## start()
- 位置: L20-23
- 役割: 動いているタイマーを取り消してから、遅延後にコールバックを実行するタイマーを張り直す。
- 触るとき: 警告の遅延表示や自動非表示の再開始の挙動を変えるとき。
- 呼び出し先: `setTimeout()`, `this._handle()`, `this.cancel()`
- 参照: `this._delay`, `this._id`

## cancel()
- 位置: L24-29
- 役割: 張られているタイマーがあれば取り消し、ID を 0 に戻す。
- 触るとき: タイマーの取り消し漏れを確認するとき。
- 条件付き依存: `if (this._id)` → `clearTimeout()`
- 参照: `this._id`

## _handle()
- 位置: L30-33
- 役割: タイマー発火時に ID を 0 にして、保存したコールバックを呼ぶ。
- 触るとき: タイマー発火後の処理の順序を調べるとき。
- 呼び出し先: `this._func()`
- 参照: `this._id`

## delay()
- 位置: L34-36
- 役割: 設定された遅延時間を返す getter。
- 触るとき: 遅延が 0 以下の扱いを確認するとき。
- 参照: `this._delay`

## showPointerLock()
- 位置: L39-46
- 役割: 全画面中でなければ、ポインターロックの警告を設定時間だけ表示する。
- 触るとき: ポインターロックごとの警告表示条件を変えるとき。
- 条件付き依存: `if (!document.fullscreenElement)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (!document.fullscreenElement)` → `this.show()`
- 参照: `document.fullscreenElement`
- XPCOM: `Services.prefs`

## _getTimeout()
- 位置: L48-55
- 役割: キーボードロック有無に応じた警告の表示時間を、設定から読んで返す。
- 触るとき: 警告の表示時間の決め方を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (keyboardLockEnabled)` → `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## showFullScreen()
- 位置: L60-72
- 役割: トップレベルのサイトの origin を示す全画面警告を、遅延付きで表示する。
- 触るとき: 全画面警告の内容や表示遅延を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `this._getTimeout()`, `this.show()`
- 参照: `browsingContext.top.currentWindowGlobal.documentPrincipal.originNoSuffix`
- XPCOM: `Services.prefs`

## show()
- 位置: L76-166
- 役割: 警告要素のイベント監視とタイマーを初回に設定し、ドメイン名と終了ボタンの文言を入れて表示状態にする。
- 触るとき: 警告の表示内容・表示タイミング・イベント処理を変えるとき。
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
- 役割: 表示中の警告が指定 id と一致すればタイマーを止め、状態を戻して監視を外し、フォーカスをコンテンツへ戻す。
- 触るとき: 警告を閉じる後始末を追加・変更するとき。
- 呼び出し先: `gBrowser.selectedBrowser.focus()`, `this._doHide()`, `this._element .querySelector()`, `this._element .querySelector(".pointerlockfswarning-domain-text") .removeAttribute()`, `this._element.querySelector()`, `this._element.removeEventListener()`, `this._timeoutHide.cancel()`, `this._timeoutShow.cancel()`, `window.removeEventListener()`
- 条件付き依存: `if (buttonElement)` → `buttonElement.removeAttribute()`
- 参照: `this._element`, `this._element.id`, `this._state`, `this._timeoutHide`, `this._timeoutShow`

## _state()
- 位置: L220-227
- 役割: 警告要素の属性(hidden・ontop・onscreen)から現在の状態を返し、どれも無ければ hiding とする。
- 触るとき: 警告の状態判定を変えるとき。
- 呼び出し先: `this._element.hasAttribute()`
- 参照: `this._STATES`

## _doHide()
- 位置: L229-234
- 役割: 警告のポップオーバーを閉じ、hidden 属性を付けて非表示にする。
- 触るとき: 警告の非表示処理を変えるとき。
- 呼び出し先: `this._element.hidePopover()`
- 参照: `this._element.hidden`

## _state()
- 位置: L236-252
- 役割: 警告の状態を切り替える。hidden 以外はすぐ属性を変え、hidden は transitionend や close で非表示にする。
- 触るとき: 警告の状態遷移の規則を変えるとき。
- 条件付き依存: `if (currentState != "hiding")` → `this._element.removeAttribute()`
- 条件付き依存: `if (currentState == "hidden")` → `this._element.showPopover()`
- 条件付き依存: `if (newState != "hidden")` → `this._element.setAttribute()`
- 参照: `this._lastState`, `this._state`

## handleEvent()
- 位置: L254-309
- 役割: マウス移動・フォーカス・トランジションの各イベントに応じて、警告の表示・隠す・保持を切り替える。
- 触るとき: マウスやフォーカスによる警告の出し入れを変えるとき。
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
- 役割: ポインターロックが有効かどうかを返す。
- 触るとき: ポインターロック中かの判定元を調べるとき。
- 参照: `this._isActive`

## entered()
- 位置: L323-327
- 役割: ポインターロック開始を記録し、通知を出して警告を表示する。
- 触るとき: ポインターロック開始時の処理を変えるとき。
- 呼び出し先: `PointerlockFsWarning.showPointerLock()`, `Services.obs.notifyObservers()`
- 参照: `this._isActive`
- XPCOM: `Services.obs`

## exited()
- 位置: L329-332
- 役割: ポインターロック終了を記録し、ポインターロックの警告を閉じる。
- 触るとき: ポインターロック終了時の処理を変えるとき。
- 呼び出し先: `PointerlockFsWarning.close()`
- 参照: `this._isActive`

## moveDocumentPiPForFullscreen()
- 位置: L339-362
- 役割: 全画面時に Document PiP ウィンドウを画面の右下へ、画面の半分以内の大きさで移動・リサイズする。
- 触るとき: 全画面時の PiP の配置や大きさを変えるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `win.moveTo()`, `win.resizeTo()`
- 参照: `win.outerHeight`, `win.outerWidth`, `win.screen`

## moveAllDocumentPiPForFullscreen()
- 位置: L364-371
- 役割: 開いている全ブラウザウィンドウのうち Document PiP のものについて、全画面用の配置を適用する。
- 触るとき: 全画面切り替え時の PiP 一括移動の条件を変えるとき。
- 呼び出し先: `Services.wm.getEnumerator()`
- 条件付き依存: `if (win.browsingContext?.isDocumentPiP)` → `moveDocumentPiPForFullscreen()`
- 参照: `win.browsingContext?.isDocumentPiP`
- XPCOM: `Services.wm`

## init()
- 位置: L374-400
- 役割: 全画面用の設定値と DOM イベントを登録し、起動時に既に全画面なら toggle を呼ぶ。
- 触るとき: 全画面の起動時の初期化を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `addEventListener()`, `document.getElementById()`, `notificationExitButton.addEventListener()`
- 条件付き依存: `if (window.fullScreen)` → `this.toggle()`
- 参照: `this.exitDomFullScreen`, `window.fullScreen`

## uninit()
- 位置: L402-404
- 役割: 全画面の後始末(cleanup)を呼ぶ。
- 触るとき: 全画面の終了処理を追加するとき。
- 呼び出し先: `this.cleanup()`

## willToggle()
- 位置: L406-412
- 役割: 全画面に入る・出る直前に、documentElement の inFullscreen 属性を付け外しする。
- 触るとき: 全画面切り替えの前段で見た目を変えるとき。
- 条件付き依存: `if (aWillEnterFullscreen)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!(aWillEnterFullscreen))` → `document.documentElement.removeAttribute()`

## fullScreenToggler()
- 位置: L414-418
- 役割: 全画面時に表示されるツールバー呼び出し用の要素を遅延取得する getter。
- 触るとき: ツールバーを呼び出すボタンの扱いを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.fullScreenToggler`

## toggle()
- 位置: L420-476
- 役割: 全画面の状態に合わせてメニュー、macOS の表示、ツールバーの収納、ショートカットキー、PiP の配置をまとめて切り替える。
- 触るとき: 全画面の入退場時に整える要素を追加・変更するとき。
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
- 役割: DOM 全画面中なら全画面を終了する。
- 触るとき: DOM 全画面の終了経路を調べるとき。
- 条件付き依存: `if (document.fullscreenElement)` → `document.exitFullscreen()`
- 参照: `document.fullscreenElement`

## shiftMacToolbarDown()
- 位置: L495-513
- 役割: macOS 全画面で、メニューバーの表示量に応じてツールバーを下へずらす値を受け取り、必要ならツールバーを表示する。
- 触るとき: macOS の全画面でのメニューバー表示と、ツールバーの位置を変えるとき。
- 呼び出し先: `this.updateMacToolbarShift()`
- 条件付き依存: `if (typeof shiftSize !== "number")` → `console.error()`
- 条件付き依存: `if (shiftSize > 0 && !wasRevealed && !this.fullScreenToggler.hidden)` → `this.showNavToolbox()`
- 参照: `this._menubarShift`, `this.fullScreenToggler.hidden`

## updateMacToolbarShift()
- 位置: L521-537
- 役割: 折りたたみ中は 0、それ以外はメニューバーのずれ量を CSS 変数とツールボックスの translate に反映する。
- 触るとき: macOS 全画面のツールバー位置計算を変えるとき。
- 呼び出し先: `document.documentElement.style.setProperty()`, `gNavToolbox.classList.toggle()`, `shiftSize.toFixed()`
- 参照: `gNavToolbox.style.translate`, `this._currentToolbarShift`, `this._isChromeCollapsed`, `this._menubarShift`

## handleEvent()
- 位置: L539-554
- 役割: 全画面の前後イベントと macOS のメニューバー表示更新を、対応する処理へ振り分ける。
- 触るとき: 全画面関連のイベントの受け口を追加するとき。
- 呼び出し先: `this.shiftMacToolbarDown()`, `this.toggle()`, `this.willToggle()`
- 参照: `event.detail`, `event.type`

## _logWarningPermissionPromptFS()
- 位置: L556-573
- 役割: 全画面での権限プロンプトの扱いを、コンソールに警告として記録する。
- 触るとき: 全画面での権限プロンプト関連の警告文言を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/scripterror;1"].createInstance()`, `Services.console.logMessage()`, `consoleMsg.initWithWindowID()`, `gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIScriptError`, `Ci.nsIScriptError.warningFlag`, `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.innerWindowID`
- XPCOM: [`nsIScriptError`](../../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## _handlePermPromptShow()
- 位置: L575-586
- 役割: 権限を全画面で許可しない設定のとき、権限プロンプトが出たら全画面を終了して警告を残す。
- 触るとき: 全画面中の権限プロンプトの扱いを変えるとき。
- 呼び出し先: `PopupNotifications.getNotification()`, `PopupNotifications.getNotification( this._permissionNotificationIDs ).filter()`
- 条件付き依存: `if ( !FullScreen.permissionsFullScreenAllowed && window.fullScreen && PopupNotifications.getNotification( this._permissionNotificationIDs ).filter(n => !n.dismis...)` → `this.exitDomFullScreen()`
- 条件付き依存: `if ( !FullScreen.permissionsFullScreenAllowed && window.fullScreen && PopupNotifications.getNotification( this._permissionNotificationIDs ).filter(n => !n.dismis...)` → `this._logWarningPermissionPromptFS()`
- 参照: `FullScreen.permissionsFullScreenAllowed`, `PopupNotifications.getNotification( this._permissionNotificationIDs ).filter(n => !n.dismissed).length`, `n.dismissed`, `this._permissionNotificationIDs`, `window.fullScreen`

## enterDomFullscreen()
- 位置: L588-694
- 役割: DOM 全画面に入る要求を処理する。リモートなら子プロセスへ伝え、全画面を続けられない場合は中止し、権限プロンプト・検索バー・アドオン導入を整える。
- 触るとき: DOM 全画面の開始条件や後処理を変えるとき。
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
- 役割: ウィンドウが全画面でなくなったとき、マウス・キー・ポップアップの監視を外す。
- 触るとき: 全画面終了時に外す監視を追加するとき。
- 条件付き依存: `if (!window.fullScreen)` → `this._mouseTargetRectObserver?.disconnect()`
- 条件付き依存: `if (!window.fullScreen)` → `this._collapsedToolboxObserver?.disconnect()`
- 条件付き依存: `if (!window.fullScreen)` → `MousePosTracker.removeListener()`
- 条件付き依存: `if (!window.fullScreen)` → `document.removeEventListener()`
- 条件付き依存: `if (!window.fullScreen)` → `gURLBar.controller.removeListener()`
- 参照: `this._expandedMouseTargetRect`, `this._keyToggleCallback`, `this._launcherEdgeListener`, `this._setPopupOpen`, `window.fullScreen`

## _toggleShortcutKeys()
- 位置: L710-727
- 役割: 全画面の状態に応じて、全画面の開始・終了ショートカットを有効・無効に切り替える。
- 触るとき: 全画面のショートカットの扱いを変えるとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById(id)?.removeAttribute()`, `document.getElementById(id)?.setAttribute()`
- 参照: `window.fullScreen`

## cleanupDomFullscreen()
- 位置: L739-782
- 役割: DOM 全画面の後始末を、OOP の親フレームから順に子へ伝えて進める。
- 触るとき: DOM 全画面の終了処理の順序を変えるとき。
- 呼び出し先: `PointerlockFsWarning.close()`, `PopupNotifications.panel.removeEventListener()`, `document.documentElement.removeAttribute()`, `document.documentElement.toggleAttribute()`, `gBrowser.tabContainer.removeEventListener()`, `this._getNextMsgRecipientActor()`, `this._handlePermPromptShow()`
- 条件付き依存: `if (target)` → `target.sendAsyncMessage()`
- 参照: `target.waitingForChildExitFullscreen`, `this._isChromeCollapsed`, `this.exitDomFullScreen`

## _abortEnterFullscreen()
- 位置: L784-797
- 役割: 全画面への移行を中止するため、次のタスクで全画面を終了し、計測中のタイマーを取り消す。
- 触るとき: 全画面移行の失敗時の後始末を変えるとき。
- 呼び出し先: `document.exitFullscreen()`, `document.exitFullscreen().catch()`, `setTimeout()`
- 条件付き依存: `if (aActor.timerId)` → `Glean.fullscreen.change.cancel()`
- 参照: `aActor.timerId`

## _getNextMsgRecipientActor()
- 位置: L817-878
- 役割: キャッシュを辿るか OOP の境界を越えて、全画面メッセージの次の送り先アクターと同プロセスの子 BrowsingContext を返す。
- 触るとき: 全画面メッセージが別プロセスの親へどう伝わるかを調べるとき。
- 呼び出し先: `aActor.hasBeenDestroyed()`, `target.hasBeenDestroyed()`
- 条件付き依存: `if (aUseCache && aActor.nextMsgRecipient)` → `actor.hasBeenDestroyed()`
- 条件付き依存: `if (parentBC && parentBC.currentWindowGlobal)` → `parentBC.currentWindowGlobal.getActor()`
- 参照: `aActor.browsingContext`, `aActor.nextMsgRecipient`, `aActor.requestOrigin`, `actor.nextMsgRecipient`, `actor.windowContext`, `actor.windowContext.isInBFCache`, `childBC.currentWindowGlobal`, `childBC.currentWindowGlobal.osPid`, `childBC.parent`, `parentBC.currentWindowGlobal`, `parentBC.currentWindowGlobal.osPid`, `target.windowContext?.isInBFCache`

## _isRemoteBrowser()
- 位置: L880-882
- 役割: マルチプロセス有効時で、対象 browser がリモートなら真を返す。
- 触るとき: リモートブラウザ向けの分岐条件を見るとき。
- 呼び出し先: `aBrowser.hasAttribute()`

## getMouseTargetRect()
- 位置: L899-916
- 役割: ツールバーが収納中に、サイドバーの側(左右端)から表示を呼び戻すマウス領域を計算する。
- 触るとき: 端からのツールバー呼び出しの範囲を変えるとき。
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `SidebarController.sidebarContainer`, `container.hidden`, `document.documentElement`, `window.windowUtils.getBoundsWithoutFlushing(container).left`

## onMouseEnter()
- 位置: L917-921
- 役割: 端の領域にマウスが入ったとき、ツールバーを表示する。ただし抑止中は無視する。
- 触るとき: 端からの呼び出し動作を変えるとき。
- 条件付き依存: `if (!this._suppressEnter)` → `FullScreen.showNavToolbox()`
- 参照: `this._suppressEnter`

## _watchLauncherEdge()
- 位置: L924-935
- 役割: 収納中に端の監視を登録する。最初の位置は呼び出し扱いせず、既に端にあっても即座には戻さない。
- 触るとき: 端の監視の開始条件を変えるとき。
- 呼び出し先: `MousePosTracker.addListener()`, `MousePosTracker.removeListener()`, `document.documentElement.hasAttribute()`
- 参照: `listener._suppressEnter`, `this._launcherEdgeListener`

## getMouseTargetRect()
- 位置: L937-939
- 役割: 収納時にツールバーを隠すマウス領域として、保存済みの領域を返す。
- 触るとき: ツールバーを隠す領域の参照元を調べるとき。
- 参照: `this._mouseTargetRect`

## _mouseTargetRectFromBounds()
- 位置: L944-951
- 役割: タブパネルの矩形から、上 50px を除いた領域を作る。
- 触るとき: ツールバーを隠す領域の幅や余白を変えるとき。
- 参照: `rect.bottom`, `rect.left`, `rect.right`, `rect.top`

## _updateMouseTargetRect()
- 位置: L960-972
- 役割: レイアウトが落ち着いた後にタブパネルの矩形を測り直し、マウス領域を更新する。
- 触るとき: リサイズやサイドバーの表示に応じた領域更新を変えるとき。
- 呼び出し先: `this._mouseTargetRectFromBounds()`, `window .promiseDocumentFlushed()`, `window .promiseDocumentFlushed(() => window.windowUtils.getBoundsWithoutFlushing(gBrowser.tabpanels) ) .then()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `gBrowser.tabpanels`, `this._mouseTargetRect`, `window.fullScreen`

## _expandCallback()
- 位置: L975-977
- 役割: ツールバー呼び出し要素にマウスやドラッグが来たら、ツールバーを表示する。
- 触るとき: 呼び出しボタンの反応を変えるとき。
- 呼び出し先: `FullScreen.showNavToolbox()`

## onMouseEnter()
- 位置: L979-981
- 役割: マウスがコンテンツ領域に入ったら、ツールバーを収納する。
- 触るとき: 収納の契機を変えるとき。
- 呼び出し先: `this.hideNavToolbox()`

## _keyToggleCallback()
- 位置: L983-992
- 役割: Escape で収納し、F6 で表示する。
- 触るとき: 全画面中のキー操作による表示切り替えを変えるとき。
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_ESCAPE)` → `FullScreen.hideNavToolbox()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_F6)` → `FullScreen.showNavToolbox()`
- 参照: `aEvent.DOM_VK_ESCAPE`, `aEvent.DOM_VK_F6`, `aEvent.keyCode`

## _setPopupOpen()
- 位置: L998-1018
- 役割: 収納を妨げるポップアップの開閉を追跡し、閉じたら収納を再試行する。
- 触るとき: ポップアップが収納を妨げる条件を変えるとき。
- 呼び出し先: `target.getAttribute()`
- 条件付き依存: `if (aEvent.type == "popuphidden")` → `FullScreen.hideNavToolbox()`
- 参照: `FullScreen._isChromeCollapsed`, `FullScreen._isPopupOpen`, `aEvent.originalTarget`, `aEvent.type`, `target.id`, `target.localName`

## onViewOpen()
- 位置: L1021-1025
- 役割: URL バーの候補表示が開いたら、収納を妨げる状態にする。
- 触るとき: URL バーの候補表示と収納の関係を変えるとき。
- 参照: `this._isChromeCollapsed`, `this._isPopupOpen`

## onViewClose()
- 位置: L1028-1031
- 役割: URL バーの候補表示が閉じたら、収納を妨げる状態を外して収納を再試行する。
- 触るとき: 候補表示を閉じた後の収納動作を変えるとき。
- 呼び出し先: `this.hideNavToolbox()`
- 参照: `this._isPopupOpen`

## navToolboxHidden()
- 位置: L1033-1035
- 役割: ナビゲーションツールボックスが収納中かを返す。
- 触るとき: 収納状態の参照元を調べるとき。
- 参照: `this._isChromeCollapsed`

## updateAutohideMenuitem()
- 位置: L1038-1043
- 役割: 自動非表示メニューの checked 状態を、設定値に合わせて更新する。
- 触るとき: 自動非表示メニューの表示を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `aItem.toggleAttribute()`
- XPCOM: `Services.prefs`

## setAutohide()
- 位置: L1044-1051
- 役割: 自動非表示の設定を反転させ、すぐに収納を再試行する。
- 触るとき: 自動非表示の切り替え動作を変えるとき。
- 呼び出し先: `FullScreen.hideNavToolbox()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _setCollapsedToolboxMargin()
- 位置: L1056-1061
- 役割: 収納時にツールボックスを自身の高さ分だけ上へずらす margin-top を、変化があるときだけ設定する。
- 触るとき: 収納時のずらし量の設定方法を変えるとき。
- 参照: `gNavToolbox.style.marginTop`

## _updateCollapsedToolboxMargin()
- 位置: L1067-1078
- 役割: 収納中のツールボックスの高さを、レイアウト確定後に測って margin-top を合わせ直す。
- 触るとき: 高さ変化に伴う収納位置のずれを直すとき。
- 呼び出し先: `window .promiseDocumentFlushed()`, `window .promiseDocumentFlushed( () => window.windowUtils.getBoundsWithoutFlushing(gNavToolbox).height ) .then()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this._isChromeCollapsed)` → `this._setCollapsedToolboxMargin()`
- 参照: `this._isChromeCollapsed`, `window.windowUtils.getBoundsWithoutFlushing(gNavToolbox).height`

## showNavToolbox()
- 位置: L1080-1137
- 役割: 収納中のツールバーを表示し、マウス追跡とサイズ監視を始める。
- 触るとき: ツールバーを表示する条件や副作用を変えるとき。
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
- 役割: 自動非表示が有効で、ポップアップやフォーカスがなければツールバーを収納する。フォーカス中は次の操作後に再試行する。
- 触るとき: ツールバーを収納する条件を変えるとき。
- 呼び出し先: `MousePosTracker.removeListener()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `document.documentElement.toggleAttribute()`, `this._collapsedToolboxObserver.observe()`, `this._mouseTargetRectFromBounds()`, `this._mouseTargetRectObserver?.disconnect()`, `this._setCollapsedToolboxMargin()`, `this._watchLauncherEdge()`, `window.matchMedia()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if ( focused && focused.ownerDocument == document && focused.localName == "input" && !BrowserHandler.kiosk )` → `window.addEventListener()`
- 条件付き依存: `if ( aAnimate && window.matchMedia("(prefers-reduced-motion: no-preference)").matches && !BrowserHandler.kiosk )` → `gNavToolbox.setAttribute()`
- 条件付き依存: `if (this._menubarShift)` → `this.updateMacToolbarShift()`
- 条件付き依存: `if (!this._collapsedToolboxObserver)` → `this._updateCollapsedToolboxMargin()`
- 参照: `BrowserHandler.kiosk`, `document.commandDispatcher.focusedElement`, `focused.localName`, `focused.ownerDocument`, `gBrowser.tabpanels`, `this._collapsedToolboxObserver`, `this._expandedMouseTargetRect`, `this._isChromeCollapsed`, `this._isPopupOpen`, `this._menubarShift`, `this.fullScreenToggler.hidden`, `window.matchMedia("(prefers-reduced-motion: no-preference)").matches`, `window.windowUtils.getBoundsWithoutFlushing(gNavToolbox).height`
- XPCOM: `Services.obs` / `Services.prefs`

## retryHideNavToolbox()
- 位置: L1165-1179
- 役割: フォーカスが外れた後に、キーかクリックを契機として収納を再試行する。
- 触るとき: フォーカス外れ後の収納再試行を変えるとき。
- 呼び出し先: `requestAnimationFrame()`, `setTimeout()`, `window.removeEventListener()`
- 条件付き依存: `if (window.fullScreen)` → `this.hideNavToolbox()`
- 参照: `window.fullScreen`
