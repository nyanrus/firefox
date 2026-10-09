# browser/components/customizableui/content/panelUI.js

source: browser/components/customizableui/content/panelUI.js
source-hash: fb77346559b4c285a40418e5ec2bf83db64564fd
lines: 1435

## <module>
- 役割: アプリメニュー（ハンバーガーメニュー）の表示・サブビュー遷移・通知バナーの状態を管理する PanelUI を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineConstant()`

## cloneHelpMenuItem()
- 位置: L60-87
- 役割: menu_HelpPopup のメニュー項目から属性と l10n ID を写した toolbarbutton を作り、サブビュー用の id とクラスを付ける。
- 触るとき: ヘルプ画面に並ぶボタンの見た目や、コマンドの引き継ぎを変えるとき。
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
- 役割: パネルで監視する popup 系イベント（showing/shown/hiding/hidden）の一覧を返す。
- 触るとき: パネルのイベント購読対象を増減するとき。

## kNotificationEvents()
- 位置: L100-102
- 役割: 通知パネルで監視するボタン系イベント（buttoncommand など）の一覧を返す。
- 触るとき: 通知ボタンの操作を受けるイベントを追加するとき。

## kElements()
- 位置: L108-117
- 役割: アプリメニューで使う DOM 要素の id の対応表を返す。
- 触るとき: アプリメニューの要素 id を変えたり、新しい要素を参照させたりするとき。

## init()
- 位置: L123-241
- 役割: 要素参照の遅延取得を設定し、メニューボタンのイベント、オブザーバー、設定値の監視、オーバーフロー領域の登録、通知の初期取得を行う。
- 触るとき: 起動時の初期化順序や監視する pref を変えるとき、またはアプリメニューが起動直後に正しく出ない問題を調べるとき。
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
- 役割: kElements の各要素を、初回参照時に getElementById で取得してキャッシュする getter を定義する。
- 触るとき: 要素の取得タイミングを変えるとき。
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `this.__defineGetter__()`
- 参照: `this.kElements`

## _ensureEventListenersAdded()
- 位置: L256-261
- 役割: パネルのイベントリスナーがまだなければ _addEventListeners を呼ぶ。
- 触るとき: リスナーの遅延登録の条件を変えるとき。
- 呼び出し先: `this._addEventListeners()`
- 参照: `this._eventListenersAdded`

## _addEventListeners()
- 位置: L263-280
- 役割: パネル、ヘルプビュー、ライブラリビュー、メインビューにイベントリスナーを付ける。
- 触るとき: アプリメニューのどのビューのどの操作を拾うかを変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelMultiView.getViewNode( document, "appMenu-libraryView" ).addEventListener()`, `helpView.addEventListener()`, `this._onLibraryCommand.bind()`, `this.mainView.addEventListener()`, `this.panel.addEventListener()`
- 参照: `this._eventListenersAdded`, `this._onHelpCommand`, `this._onHelpViewShow`, `this._onLibraryCommand`, `this._onMainViewShow`, `this.kEvents`

## _removeEventListeners()
- 位置: L282-296
- 役割: _addEventListeners で付けたリスナーをすべて外し、登録済みフラグを戻す。
- 触るとき: リスナーの付け外しを対で変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelMultiView.getViewNode( document, "appMenu-libraryView" ).removeEventListener()`, `helpView.removeEventListener()`, `this.mainView.removeEventListener()`, `this.panel.removeEventListener()`
- 参照: `this._eventListenersAdded`, `this._onHelpCommand`, `this._onHelpViewShow`, `this._onLibraryCommand`, `this.kEvents`

## uninit()
- 位置: L298-322
- 役割: リスナー、オブザーバー、ウィンドウイベント、CustomizableUI の購読を解除する。
- 触るとき: ウィンドウを閉じる時の後始末を変えるとき。
- 呼び出し先: `CustomizableUI.removeListener()`, `Services.obs.removeObserver()`, `this._removeEventListeners()`, `this.menuButton.removeEventListener()`, `window.removeEventListener()`
- 条件付き依存: `if (this._notificationPanel)` → `this.notificationPanel.removeEventListener()`
- 参照: `this._notificationPanel`, `this.kEvents`, `this.kNotificationEvents`
- XPCOM: `Services.obs`

## toggle()
- 位置: L330-342
- 役割: カスタマイズ中なら何もせず、開いていれば閉じ、閉じていれば開く。
- 触るとき: メニューボタンのクリックやキー操作で開閉が反転しない問題を調べるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`, `this._ensureEventListenersAdded()`
- 条件付き依存: `if (this.panel.state == "open")` → `this.hide()`
- 条件付き依存: `if (this.panel.state == "closed")` → `this.show()`
- 参照: `this.panel.state`

## show()
- 位置: L351-381
- 役割: 準備完了を待ってから ASRouter にメニュー表示を通知し、メニューボタンを基準にパネルを開く。
- 触るとき: メニューを開くときの前処理や、表示位置の基準を変えるとき。
- 呼び出し先: `PanelMultiView.openPopup()`, `document.documentElement.hasAttribute()`, `this._ensureShortcutsShown()`, `this._getPanelAnchor()`, `this.ensureReady()`
- 条件付き依存: `if (ASRouter.initialized)` → `ASRouter.sendTriggerMessage()`
- 参照: `ASRouter.initialized`, `MenuMessage.SOURCES.APP_MENU`, `aEvent.type`, `console.error`, `gBrowser.selectedBrowser`, `this.menuButton`, `this.panel`, `this.panel.state`

## hide()
- 位置: L386-392
- 役割: カスタマイズ中を除き、PanelMultiView 経由でパネルを閉じる。
- 触るとき: メニューを閉じる経路を変えるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `document.documentElement.hasAttribute()`
- 参照: `this.panel`

## observe()
- 位置: L394-419
- 役割: AI ウィンドウ状態、フルスクリーン、通知、更新進捗のオブザーバー通知を受けて、それぞれの表示更新や About ダイアログを開く。
- 触るとき: 通知トピックごとの反応を追加・変更するとき。
- 呼び出し先: `openAboutDialog()`, `this.updateNotifications()`
- 条件付き依存: `if (subject == window)` → `this._showAIMenuItem()`
- 条件付き依存: `if (this._notifications)` → `this.updateNotifications()`
- 参照: `AppMenuNotifications.notifications`, `this._notifications`

## handleEvent()
- 位置: L421-491
- 役割: パネルの開閉イベントで通知・ボタン状態を更新し、mousedown・キー・フルスクリーン・クリック・コマンドを振り分ける。
- 触るとき: アプリメニューのイベント処理全般や、Ctrl+クリック（macOS）の扱いを調べるとき。
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
- 役割: メインビューのボタン ID ごとに、サブビュー表示・設定・パスワード・全画面などの処理へ振り分ける。
- 触るとき: アプリメニューの項目を追加したり、項目の動作を変えたりするとき。
- 呼び出し先: `BookmarkingUI.showSubView()`, `BrowserCommands.fullScreen()`, `LoginHelper.openPasswordManager()`, `gSync.toggleAccountPanel()`, `openPreferences()`, `setTimeout()`, `target.closest()`, `target.closest("panel").hidePopup()`, `this._onBannerItemSelected()`, `this.showMoreToolsPanel()`, `this.showSubView()`
- 参照: `target.id`

## isReady()
- 位置: L538-540
- 役割: パネルの準備（ensureReady）が終わっているかを返す。
- 触るとき: 準備前にメニューを参照する処理の順序を調べるとき。
- 参照: `this._isReady`

## isNotificationPanelOpen()
- 位置: L542-546
- 役割: 通知パネルが showing または open なら true を返す。
- 触るとき: 通知パネルの表示判定を使う箇所を変えるとき。
- 参照: `this.notificationPanel.state`

## ensureReady()
- 位置: async L560-569
- 役割: delayedStartupPromise を待ち、リスナーを付けてパネルを使える状態にする。
- 触るとき: 起動前にメニューを開こうとした時の待ち方を変えるとき。
- 呼び出し先: `this._ensureEventListenersAdded()`
- 参照: `this._isReady`, `this.panel.hidden`, `window.delayedStartupPromise`

## showHelpView()
- 位置: L575-578
- 役割: ヘルプサブビューへ切り替える。
- 触るとき: ヘルプ画面を別の入口から開くとき。
- 呼び出し先: `this._ensureEventListenersAdded()`, `this.multiView.showSubView()`

## showMoreToolsPanel()
- 位置: L585-594
- 役割: その他のツールのサブビューを表示し、DevTools に表示の通知を出す。
- 触るとき: 開発者ツール項目の並びを変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `document.getElementById()`, `this.showSubView()`
- XPCOM: `Services.obs`

## showSubView()
- 位置: async L603-730
- 役割: サブビューを既存の panelmultiview に出すか、無ければ一時的なパネルを作って出し、閉じたら後始末する。ctrl+クリック等の入力は無視する。
- 触るとき: サブビューの開き方や、閉じた後に一時パネルが残る問題を調べるとき。
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
- 役割: 一時パネルを閉じるときに、ビューのクラス・閉じるリスナー・アンカー状態を戻し、パネルを取り除く。
- 触るとき: 一時パネルの後始末の漏れを調べるとき。
- 呼び出し先: `PanelMultiView.removePopup()`, `viewNode.classList.remove()`
- 条件付き依存: `if (viewShown)` → `CustomizableUI.removePanelCloseListeners()`
- 条件付き依存: `if (viewShown)` → `tempPanel.removeEventListener()`
- 参照: `aAnchor.open`, `event.target`

## ensurePanicViewInitialized()
- 位置: L737-748
- 役割: パニックビューを初めて表示するとき、その FTL を読み込み、初期化済みにする。
- 触るとき: パニックボタン関連の表示の初期化を変えるとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`
- 参照: `panelView._initialized`, `panelView.id`, `this.panic`

## disableSingleSubviewPanelAnimations()
- 位置: L755-757
- 役割: 一時パネルのアニメーションを無効にするフラグを立てる。
- 触るとき: 一時パネルの開閉アニメーションを止める箇所を調べるとき。
- 参照: `this._disableAnimations`

## enableSingleSubviewPanelAnimations()
- 位置: L759-761
- 役割: 一時パネルのアニメーション無効フラグを戻す。
- 触るとき: 上記の無効化と対で変えるとき。
- 参照: `this._disableAnimations`

## updateOverflowStatus()
- 位置: L763-773
- 役割: 固定オーバーフロー領域に項目があれば、ナビバーとオーバーフローパネルに印を付け、空なら印を外して閉じる。
- 触るとき: オーバーフローボタンの表示条件を変えるとき。
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
- 役割: 固定オーバーフロー領域の中身が変わったときに updateOverflowStatus を呼ぶ。
- 触るとき: ウィジェットの移動でオーバーフローボタンが更新されない問題を調べるとき。
- 条件付き依存: `if (aContainer == this.overflowFixedList)` → `this.updateOverflowStatus()`
- 参照: `this.overflowFixedList`

## onAreaReset()
- 位置: L781-785
- 役割: 固定オーバーフロー領域がリセットされたとき、同じく状態を更新する。
- 触るとき: 領域リセット時の表示更新を変えるとき。
- 条件付き依存: `if (aContainer == this.overflowFixedList)` → `this.updateOverflowStatus()`
- 参照: `this.overflowFixedList`

## _updatePanelButton()
- 位置: L791-806
- 役割: パネルの状態に合わせて、メニューボタンの open 状態と ARIA 用のラベルを切り替える。
- 触るとき: メニューボタンの開閉表示やラベルを変えるとき。
- 条件付き依存: `if (state == "open" || state == "showing")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(state == "open" || state == "showing"))` → `document.l10n.setAttributes()`
- 参照: `this.menuButton`, `this.menuButton.open`, `this.panel`

## _onMainViewShow()
- 位置: L808-823
- 役割: メインビュー表示時に FxA メニューのメッセージの表示を記録し、ズーム UI を更新する。
- 触るとき: メインビューに出るメッセージのテレメトリや、ズーム表示の更新を変えるとき。
- 呼び出し先: `panelview.getAttribute()`, `updateZoomUI()`
- 条件付き依存: `if (messageId)` → `MenuMessage.recordMenuMessageTelemetry()`
- 条件付き依存: `if (messageId)` → `ASRouter.getMessageById()`
- 条件付き依存: `if (messageId)` → `ASRouter.addImpression()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `MenuMessage.SOURCES.APP_MENU`, `event.target`, `gBrowser.selectedBrowser`

## _onHelpViewShow()
- 位置: L825-902
- 役割: ヘルプメニューから表示中の項目を集め、HELP_VIEW_GROUPS の順に clone してサブビューに並べる。nova が有効なら デバイス切替項目を promo に置き換える。
- 触るとき: ヘルプ画面の項目の順序や表示条件、nova のデバイス切替 promo を変えるとき。
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
- 役割: ヘルプサブビュー内の項目 ID ごとに、壊れたサイトの報告・ヘルプ・フィードバック・セーフモード等を起動する。
- 触るとき: ヘルプ項目の動作を追加・変更するとき。
- 呼び出し先: `ReportBrokenSite.handleParentMenuButtonCommand()`, `Services.policies.getSupportMenu()`, `Services.scriptSecurityManager.createNullPrincipal()`, `gSafeBrowsing.getReportURL()`, `gSafeBrowsing.reportFalseDeceptiveSite()`, `openAboutDialog()`, `openFeedbackPage()`, `openHelpLink()`, `openSwitchingDevicesPage()`, `openTroubleshootingPage()`, `openTrustedLinkIn()`, `openUILink()`, `safeModeRestart()`, `toOpenWindowByType()`
- 参照: `Services.policies.getSupportMenu().URL.href`, `aEvent.target`, `aEvent.target.id`
- XPCOM: `Services.policies` / `Services.scriptSecurityManager`

## _onLibraryCommand()
- 位置: L948-962
- 役割: ライブラリのブックマーク・履歴・ダウンロードの各ボタンから、対応する画面を開く。
- 触るとき: ライブラリ項目の遷移先を変えるとき。
- 呼び出し先: `BookmarkingUI.showSubView()`, `DownloadsPanel.showDownloadsHistory()`, `this.showSubView()`
- 参照: `aEvent.target`, `button.documentGlobal`, `button.id`

## _hidePopup()
- 位置: L964-972
- 役割: 通知パネルが開いていれば閉じる。
- 触るとき: 通知パネルを閉じる条件を変えるとき。
- 条件付き依存: `if (this.isNotificationPanelOpen)` → `this.notificationPanel.hidePopup()`
- 参照: `this._notificationPanel`, `this.isNotificationPanelOpen`

## selectAndMarkItem()
- 位置: async L980-1053
- 役割: メニューを開き（必要なら閉じるのを待つ）、指定した ID の項目をサブビューまで順にフォーカスする。
- 触るとき: 外部から特定のメニュー項目へ誘導する機能（ハイライトやフォーカス）を変えるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`, `markItem()`, `this.panel.addEventListener()`
- 条件付き依存: `if (this.panel.state == "hiding")` → `this.panel.addEventListener()`
- 条件付き依存: `if (this.panel.state != "open")` → `this.panel.addEventListener()`
- 条件付き依存: `if (this.panel.state != "open")` → `this.show()`
- 参照: `this.mainView`, `this.panel.state`

## viewShownCB()
- 位置: L1004-1017
- 役割: 次のサブビューが表示されたとき、指定された次の項目がそのビューにあればフォーカスを移し、無ければ残りの指定を捨てる。
- 触るとき: サブビューをまたぐ項目の誘導が途中で止まる問題を調べるとき。
- 呼び出し先: `viewHidingCB()`
- 条件付き依存: `if (itemIds.length)` → `window.document.getElementById()`
- 条件付き依存: `if (itemIds.length)` → `subItem?.closest()`
- 条件付き依存: `if (event.target.id == subItem?.closest("panelview")?.id)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (event.target.id == subItem?.closest("panelview")?.id)` → `markItem()`
- 参照: `event.target`, `event.target.id`, `itemIds.length`, `subItem?.closest("panelview")?.id`
- XPCOM: `Services.tm`

## viewHidingCB()
- 位置: L1019-1024
- 役割: 現在のビューのマウス移動無視を解除し、参照を外す。
- 触るとき: ビュー切替時のハイライトの後始末を変えるとき。
- 参照: `currentView.ignoreMouseMove`

## popupHiddenCB()
- 位置: L1026-1029
- 役割: メニューが閉じたとき、ビューの後始末と ViewShown の購読解除を行う。
- 触るとき: メニューを閉じた後にリスナーが残る問題を調べるとき。
- 呼び出し先: `this.panel.removeEventListener()`, `viewHidingCB()`

## markItem()
- 位置: L1031-1049
- 役割: 指定された次の項目に tabindex を付けてフォーカスし、マウスによるハイライト変更を一時的に無効にする。
- 触るとき: 項目のハイライトや、マウス移動の抑止の条件を変えるとき。
- 呼び出し先: `PanelView.forNode()`, `currentView.focusSelectedElement()`, `item.setAttribute()`, `itemIds.shift()`, `this.panel.addEventListener()`, `window.document.getElementById()`
- 条件付き依存: `if (itemIds.length)` → `this.panel.addEventListener()`
- 参照: `currentView.ignoreMouseMove`, `currentView.selectedElement`, `itemIds.length`

## updateNotifications()
- 位置: L1055-1111
- 役割: 通知の状態（全画面・フォーカス・パネル表示中か）に応じて、ドアハンガー、バッジ、バナー項目のどれを出すかを決める。
- 触るとき: 更新通知などが出る場面（フォーカス・全画面・メニュー表示中）を変えるとき。
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
- 役割: 通知の内容をパネルに入れ、FTL を読み込んでから通知パネルをメニューボタンの横に開く。
- 触るとき: 通知パネルの開き方や読み込み順を変えるとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document .getElementById()`, `document .getElementById("appMenu-notification-popup") .querySelectorAll()`, `document .getElementById("appMenu-notification-popup") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `this._getPanelAnchor()`, `this._refreshNotificationPanel()`, `this.notificationPanel.openPopup()`
- 条件付き依存: `if (notification.options.beforeShowDoorhanger)` → `notification.options.beforeShowDoorhanger()`
- 参照: `notification.options.beforeShowDoorhanger`, `this.isNotificationPanelOpen`, `this.menuButton`

## _clearNotificationPanel()
- 位置: L1142-1147
- 役割: 通知パネルの各通知を隠して参照を外す。
- 触るとき: 通知の表示を消す処理を変えるとき。
- 参照: `popupnotification.hidden`, `popupnotification.notification`, `this.notificationPanel.children`

## _clearAllNotifications()
- 位置: L1149-1153
- 役割: 通知パネル、バッジ、バナー項目をまとめて消す。
- 触るとき: 通知を全部消す条件を変えるとき。
- 呼び出し先: `this._clearBadge()`, `this._clearBannerItem()`, `this._clearNotificationPanel()`

## notificationPanel()
- 位置: L1155-1171
- 役割: 初めて必要になったときにテンプレートを展開し、通知パネルを取得してイベントを付ける。
- 触るとき: 通知パネルの遅延生成を変えるとき。
- 条件付き依存: `if (!this._notificationPanel)` → `document.getElementById()`
- 条件付き依存: `if (!this._notificationPanel)` → `template.replaceWith()`
- 条件付き依存: `if (!this._notificationPanel)` → `this._notificationPanel.addEventListener()`
- 参照: `template.content`, `this._notificationPanel`, `this.kEvents`, `this.kNotificationEvents`

## mainView()
- 位置: L1173-1178
- 役割: メインビューの要素を取得してキャッシュする。
- 触るとき: メインビューの参照先を変えるとき。
- 条件付き依存: `if (!this._mainView)` → `PanelMultiView.getViewNode()`
- 参照: `this._mainView`

## addonNotificationContainer()
- 位置: L1180-1189
- 役割: アドオン通知バナーの入れ物の要素を取得してキャッシュする。
- 触るとき: アドオン通知の表示先を変えるとき。
- 条件付き依存: `if (!this._addonNotificationContainer)` → `PanelMultiView.getViewNode()`
- 参照: `this._addonNotificationContainer`

## _formatDescriptionMessage()
- 位置: L1191-1198
- 役割: 通知メッセージを『<>』で前後に分け、名前を挟んで開始・名前・終了の3つに分ける。
- 触るとき: 通知の説明文の書式（<> で名前を挟む仕様）を変えるとき。
- 呼び出し先: `n.options.message.split()`
- 参照: `n.options.name`, `text.end`, `text.name`, `text.start`

## _refreshNotificationPanel()
- 位置: L1200-1230
- 役割: 通知パネル内の popupnotification の属性（文言・アイコン・詳細 URL）を通知に合わせて設定し、表示する。
- 触るとき: 通知パネルに出る内容の組み立てを変えるとき。
- 呼び出し先: `document.getElementById()`, `popupnotification.setAttribute()`, `popupnotification.show()`, `this._clearNotificationPanel()`, `this._getPopupId()`
- 条件付き依存: `if (notification.options.message)` → `this._formatDescriptionMessage()`
- 条件付き依存: `if (notification.options.message)` → `popupnotification.setAttribute()`
- 条件付き依存: `if (notification.options.onRefresh)` → `notification.options.onRefresh()`
- 条件付き依存: `if (notification.options.popupIconURL)` → `popupnotification.setAttribute()`
- 条件付き依存: `if (notification.options.learnMoreURL)` → `popupnotification.setAttribute()`
- 参照: `desc.end`, `desc.name`, `desc.start`, `notification.options.learnMoreURL`, `notification.options.message`, `notification.options.onRefresh`, `notification.options.popupIconURL`, `popupnotification.notification`

## _showAIMenuItem()
- 位置: L1232-1256
- 役割: AI ウィンドウの有効状態と設定から、新しい AI ウィンドウ・クラシックウィンドウ・チャット履歴の項目の表示を切り替える。
- 触るとき: AI 関連のメニュー項目の出し分け条件を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.documentElement.hasAttribute()`
- 参照: `aiMenuItem.hidden`, `chatHistoryMenuItem.hidden`, `classicWindowMenuItem.hidden`, `this.AIControlDefault`, `this.AIControlSmartWindow`, `this.isAIWindowEnabled`

## _showTabGroupsMenuItem()
- 位置: L1258-1264
- 役割: browser.tabs.groups.alternateMenu に応じて、タブグループの項目の表示を切り替える。
- 触るとき: タブグループ項目の表示条件を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`
- 参照: `button.hidden`, `this.tabGroupsAlternateMenu`

## _showReferralsMenuItem()
- 位置: L1266-1278
- 役割: browser.referrals.enabled に応じて、紹介（referrals）の項目と区切り線の表示を切り替える。
- 触るとき: 紹介項目の表示条件を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`
- 参照: `button.hidden`, `separator.hidden`, `this.referralsEnabled`

## _showBadge()
- 位置: L1280-1283
- 役割: メニューボタンに通知種別に応じた badge-status 属性を付ける。
- 触るとき: メニューボタンの通知バッジの色や種類を変えるとき。
- 呼び出し先: `this._getBadgeStatus()`, `this.menuButton.setAttribute()`

## _showBannerItem()
- 位置: L1287-1339
- 役割: 更新系の通知（update-*）に限り、メニュー内の色付きバナー項目に文言と説明を設定して表示する。nova の更新再起動はプライベートウィンドウで説明を省く。
- 触るとき: 更新バナーの文言や、対象となる通知の種類を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `document.l10n.setAttributes()`, `supportedIds.includes()`, `this._panelBannerItem.setAttribute()`, `this._panelBannerItem.toggleAttribute()`
- 条件付き依存: `if (!this._panelBannerItem)` → `this.mainView.querySelector()`
- 条件付き依存: `if (isNovaUpdateRestart)` → `this._panelBannerItem.setAttribute()`
- 条件付き依存: `if (!(isNovaUpdateRestart))` → `this._panelBannerItem.removeAttribute()`
- 参照: `notification.id`, `this._panelBannerItem`, `this._panelBannerItem.hidden`, `this._panelBannerItem.notification`
- XPCOM: `Services.prefs`

## _clearBadge()
- 位置: L1341-1343
- 役割: メニューボタンの badge-status 属性を外す。
- 触るとき: バッジを消す条件を変えるとき。
- 呼び出し先: `this.menuButton.removeAttribute()`

## _clearBannerItem()
- 位置: L1345-1350
- 役割: バナー項目の通知参照を外して隠す。
- 触るとき: バナーを消す条件を変えるとき。
- 参照: `this._panelBannerItem`, `this._panelBannerItem.hidden`, `this._panelBannerItem.notification`

## _onNotificationButtonEvent()
- 位置: L1352-1376
- 役割: 通知パネルのボタンクリックを、通知の主要操作または副操作へ渡す。対象が無ければ例外を投げる。
- 触るとき: 通知ボタンの処理を変えるとき。
- 呼び出し先: `event.preventDefault()`, `getNotificationFromElement()`
- 条件付き依存: `if (type == "secondarybuttoncommand")` → `AppMenuNotifications.callSecondaryAction()`
- 条件付き依存: `if (!(type == "secondarybuttoncommand"))` → `AppMenuNotifications.callMainAction()`
- 参照: `event.originalTarget`, `notificationEl.notification`

## _onBannerItemSelected()
- 位置: L1378-1388
- 役割: バナー項目が選ばれたとき、通知の主要操作を呼び、イベントの伝播を止める。
- 触るとき: バナーをクリックしたときの動作を変えるとき。
- 呼び出し先: `AppMenuNotifications.callMainAction()`, `event.stopPropagation()`
- 参照: `event.originalTarget`, `target.notification`

## _getPopupId()
- 位置: L1390-1392
- 役割: 通知 ID から popupnotification の DOM ID（appMenu-<id>-notification）を作る。
- 触るとき: 通知パネル内の要素の ID 規則を変えるとき。
- 参照: `notification.id`

## _getBadgeStatus()
- 位置: L1394-1396
- 役割: バッジの状態として通知 ID をそのまま返す。
- 触るとき: バッジの状態名の規則を変えるとき。
- 参照: `notification.id`

## _getPanelAnchor()
- 位置: L1398-1401
- 役割: アイコンのバッジスタック、なければアイコン、なければ候補要素を、パネルの基準として返す。
- 触るとき: パネルの表示位置の基準を変えるとき。
- 参照: `candidate.badgeStack`, `candidate.icon`

## _ensureShortcutsShown()
- 位置: L1403-1416
- 役割: ビュー内の key 付きボタンに、キーの表示文字列（shortcut 属性）を一度だけ付ける。
- 触るとき: メニュー項目に表示するショートカットの表示を変えるとき。
- 呼び出し先: `ShortcutUtils.prettifyShortcut()`, `button.getAttribute()`, `button.setAttribute()`, `document.getElementById()`, `view.hasAttribute()`, `view.querySelectorAll()`, `view.setAttribute()`
- 参照: `this.mainView`

## getLocale()
- 位置: L1425-1427
- 役割: アプリのロケール（BCP 47 形式）を返す。
- 触るとき: メニュー内でロケールに依存する表示を扱うとき。
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## getNotificationFromElement()
- 位置: L1432-1434
- 役割: DOM 要素を含む popupnotification 要素を、closest で探して返す。
- 触るとき: 通知要素から親の通知を引き直す箇所を変えるとき。
- 呼び出し先: `aElement.closest()`
