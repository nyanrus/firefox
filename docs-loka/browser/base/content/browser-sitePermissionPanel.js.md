# browser/base/content/browser-sitePermissionPanel.js

source: browser/base/content/browser-sitePermissionPanel.js
source-hash: 6a4ed1d46f50c1c25423f6e2be25508dde0f4fae
lines: 1270

## <module>
- 役割: サイト権限パネル(identity ボタン側の権限一覧と共有表示)を担う gPermissionPanel と、猶予期間判定の補助関数を定義する
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## _initializePopup()
- 位置: L24-32
- 役割: 権限パネルの template を初回だけ実体化し、popupshown と popuphidden を購読する
- 触るとき: 権限パネルを開く経路や _permissionPopup の初期化タイミングを変えるとき。初期化前は _permissionPopup が null になる点に注意する。
- 条件付き依存: `if (!this._popupInitialized)` → `document.getElementById()`
- 条件付き依存: `if (!this._popupInitialized)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this._popupInitialized)` → `this._permissionPopup.addEventListener()`
- 参照: `this._popupInitialized`, `wrapper.content`

## hidePopup()
- 位置: L34-38
- 役割: 初期化済みの場合だけ権限パネルを閉じる
- 触るとき: identity ボタン以外の経路からパネルを閉じる処理を追加・変更するとき。
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 参照: `this._permissionPopup`, `this._popupInitialized`

## setAnchor()
- 位置: L48-51
- 役割: 権限パネルの表示アンカーと位置を外部から上書きする
- 触るとき: サイドバーなど identity ボックス以外の場所から権限パネルを出すとき。
- 参照: `this._popupAnchorNode`, `this._popupPosition`

## setBrowserOverride()
- 位置: L56-58
- 役割: 権限の対象ブラウザを一時的に指定ブラウザへ差し替える
- 触るとき: 選択中タブ以外のブラウザの権限を扱う処理(サイドバーなど)を書くとき。後始末は clearBrowserOverride で行う。
- 参照: `this._browserOverride`

## clearBrowserOverride()
- 位置: L59-61
- 役割: setBrowserOverride による上書きを外し、選択中ブラウザへ戻す
- 触るとき: 上書きを使った処理の後で対象ブラウザが元に戻らない不具合を調べるとき。
- 参照: `this._browserOverride`

## _activeBrowser()
- 位置: L63-65
- 役割: 上書きがあればそれを、なければ選択中タブのブラウザを返す
- 触るとき: 権限の対象ブラウザをどこから決めるかを変えるとき。
- 参照: `gBrowser.selectedBrowser`, `this._browserOverride`

## browser()
- 位置: L66-68
- 役割: _activeBrowser をそのまま返す公開ゲッター
- 触るとき: 権限一覧の取得や解除処理が対象とするブラウザを参照するとき。
- 参照: `this._activeBrowser`

## _popupAnchor()
- 位置: L70-75
- 役割: パネルの表示アンカーを返す。上書きがなければ identity 権限ボックス
- 触るとき: パネルがどの要素の隣に出るかを変えるとき。setAnchor の呼び出し元と合わせて確認する。
- 参照: `this._identityPermissionBox`, `this._popupAnchorNode`

## _identityPermissionBox()
- 位置: L76-81
- 役割: identity-permission-box 要素を取得し、以後はキャッシュする
- 触るとき: identity ボックスの DOM 構造や ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPermissionBox`

## _permissionGrantedIcon()
- 位置: L82-87
- 役割: permissions-granted-icon 要素を取得してキャッシュする
- 触るとき: 許可済みアイコンの表示や参照先を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionGrantedIcon`

## _permissionPopup()
- 位置: L88-95
- 役割: 初期化後に permission-popup 要素を返し、初期化前は null を返す
- 触るとき: 権限パネルの要素を使う処理で null 判定が必要か確かめるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionPopup`, `this._popupInitialized`

## _permissionPopupMainView()
- 位置: L96-101
- 役割: 権限パネルのメインビュー要素を取得する
- 触るとき: パネル内のビュー構成を変えるとき。キャッシュの delete 対象が _permissionPopupPopupMainView と食い違っており、毎回取り直している(要確認: 意図した実装か)。
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionPopupPopupMainView`

## _permissionPopupMainViewHeaderLabel()
- 位置: L102-107
- 役割: パネルヘッダーのラベル要素を取得する
- 触るとき: ホスト名入りのヘッダー文言を変えるとき。_refreshPermissionPopup が文言を設定する。
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionPopupMainViewHeaderLabel`

## _permissionList()
- 位置: L108-113
- 役割: 権限項目を並べるコンテナ要素を取得する
- 触るとき: 権限項目の追加先や並び順を変えるとき。updateSitePermissions が項目を消して作り直す場所。
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionList`

## _defaultPermissionAnchor()
- 位置: L114-119
- 役割: anchorfor の無い権限項目の既定の挿入先を返す
- 触るとき: 専用アンカーを持たない新しい権限種別がどこに入るかを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._defaultPermissionAnchor`

## _permissionReloadHint()
- 位置: L120-125
- 役割: 権限解除後に出す再読み込みヒント要素を取得する
- 触るとき: 解除後の再読み込み案内の表示条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._permissionReloadHint`

## _permissionAnchors()
- 位置: L126-134
- 役割: blocked-permissions-container の子を permission-id ごとの辞書にする
- 触るとき: ブロック中の権限アイコンを追加し、data-permission-id を割り当てるとき。
- 呼び出し先: `anchor.getAttribute()`, `document.getElementById()`
- 参照: `document.getElementById("blocked-permissions-container") .children`, `this._permissionAnchors`

## _geoSharingIcon()
- 位置: L136-139
- 役割: 位置情報の共有中アイコン要素を取得する
- 触るとき: 位置情報共有の表示を変えるとき。updateSharingIndicator が属性を付け外しする。
- 呼び出し先: `document.getElementById()`
- 参照: `this._geoSharingIcon`

## _xrSharingIcon()
- 位置: L141-144
- 役割: XR 共有中アイコン要素を取得する
- 触るとき: XR 共有の表示を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._xrSharingIcon`

## _serialSharingIcon()
- 位置: L146-151
- 役割: シリアルポート共有中アイコン要素を取得する
- 触るとき: シリアルポート共有の表示を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._serialSharingIcon`

## _webRTCSharingIcon()
- 位置: L153-158
- 役割: カメラ・マイク・画面共有中アイコン要素を取得する
- 触るとき: WebRTC 共有の一時停止表示や猶予期間の表示を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._webRTCSharingIcon`

## _refreshPermissionPopup()
- 位置: L164-175
- 役割: パネルのホスト名入りヘッダーを更新し、権限一覧を描き直す
- 触るとき: パネル表示時や権限変更後にヘッダーや一覧が古いままのとき。対象は _browserOverride があればそれで決まる。
- 呼び出し先: `gIdentityHandler.getHostForDisplay()`, `gNavigatorBundle.getFormattedString()`, `this.updateSitePermissions()`
- 参照: `this._browserOverride?.currentURI`, `this._permissionPopupMainViewHeaderLabel.textContent`

## hidePermissionIcons()
- 位置: L181-183
- 役割: identity 権限ボックスの hasPermissions 属性を外し、権限アイコンを隠す
- 触るとき: プロキシ異常など権限アイコンを出さない状態を追加するとき。gIdentityHandler から呼ばれる。
- 呼び出し先: `this._identityPermissionBox.removeAttribute()`

## refreshPermissionIcons()
- 位置: L189-242
- 役割: ブロック中の権限とポップアップ遮断の有無からアイコンを出し分ける
- 触るとき: identity ボックスの権限アイコンの表示条件(ブロック、ポップアップ、常に確認)を変えるとき。判定は gBrowser.selectedBrowser を基準にする。
- 呼び出し先: `Object.values()`, `SitePermissions.getAllForBrowser()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `icon.removeAttribute()`, `this._identityPermissionBox.toggleAttribute()`
- 条件付き依存: `if (icon)` → `icon.setAttribute()`
- 条件付き依存: `if ( gBrowser.selectedBrowser.popupAndRedirectBlocker.getBlockedPopupCount() || gBrowser.selectedBrowser.popupAndRedirectBlocker.isRedirectBlocked() )` → `icon.setAttribute()`
- 参照: `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`, `SitePermissions.PROMPT`, `SitePermissions.UNKNOWN`, `gBrowser.selectedBrowser`, `permission.id`, `permission.state`, `permissionAnchors.popup`, `this._gumShowAlwaysAsk`, `this._permissionAnchors`

## openPopup()
- 位置: L249-291
- 役割: 全画面中なら解除を待ってから、他のパネルを閉じて権限パネルを開く
- 触るとき: 権限パネルの開き方や全画面との競合(bug 1557041 の経緯)を扱うとき。全画面時は observe で開き直す。
- 呼び出し先: `Array.from()`, `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `document.querySelectorAll()`, `this._initializePopup()`, `this._refreshPermissionPopup()`
- 条件付き依存: `if (document.fullscreen)` → `Services.obs.addObserver()`
- 条件付き依存: `if (document.fullscreen)` → `window.addEventListener()`
- 条件付き依存: `if (document.fullscreen)` → `document.exitFullscreen()`
- 参照: `console.error`, `document.fullscreen`, `this._event`, `this._exitedEventReceived`, `this._permissionPopup`, `this._permissionReloadHint.hidden`, `this._popupAnchor`, `this._popupPosition`
- XPCOM: `Services.obs`

## updateSharingIndicator()
- 位置: L298-363
- 役割: カメラ・マイク・位置情報などの共有状態から共有アイコンを付け替える
- 触るとき: 共有表示(一時停止、猶予期間、XR、シリアル)を変えるとき。パネルが開いていれば updateSitePermissions も呼ぶ。
- 呼び出し先: `this._geoSharingIcon.removeAttribute()`, `this._identityPermissionBox.toggleAttribute()`, `this._serialSharingIcon.removeAttribute()`, `this._webRTCSharingIcon.removeAttribute()`, `this._xrSharingIcon.removeAttribute()`
- 条件付き依存: `if (this._sharingState.webRTC.sharing)` → `this._webRTCSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.webRTC.paused)` → `this._webRTCSharingIcon.setAttribute()`
- 条件付き依存: `if (!(this._sharingState.webRTC.sharing))` → `hasMicCamGracePeriodsSolely()`
- 条件付き依存: `if (micGrace || camGrace)` → `this._webRTCSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.geo)` → `this._geoSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.xr)` → `this._xrSharingIcon.setAttribute()`
- 条件付き依存: `if (this._sharingState.serial)` → `this._serialSharingIcon.setAttribute()`
- 条件付き依存: `if (this._popupInitialized && this._permissionPopup.state != "closed")` → `this.updateSitePermissions()`
- 参照: `browser._sharingState`, `gBrowser.selectedBrowser`, `this._permissionPopup.state`, `this._popupInitialized`, `this._sharingState`, `this._sharingState.geo`, `this._sharingState.serial`, `this._sharingState.webRTC`, `this._sharingState.webRTC.paused`, `this._sharingState.webRTC.sharing`, `this._sharingState.xr`

## handleIdentityButtonEvent()
- 位置: L368-397
- 役割: identity ボタンの左クリック、Space、Enter を受けてパネルを開く
- 触るとき: identity ボタンの操作条件を変えるとき。URL が編集中でも共有中か永続検索語なら開く例外を確認する。
- 呼び出し先: `event.stopPropagation()`, `gURLBar.getAttribute()`, `gURLBar.hasAttribute()`, `this.openPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`, `this._sharingState`

## handleEvent()
- 位置: L399-432
- 役割: パネル表示中だけ focus を監視し、外側へフォーカスが移ったらパネルを閉じる
- 触るとき: パネルの自動的な閉じ方(フォーカス離脱、noautohide)を変えるとき。
- 呼び出し先: `elem.compareDocumentPosition()`, `this._permissionPopup.hasAttribute()`
- 条件付き依存: `if (event.target == this._permissionPopup)` → `window.addEventListener()`
- 条件付き依存: `if (event.target == this._permissionPopup)` → `window.removeEventListener()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this._permissionPopup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `event.target`, `event.type`, `this._permissionPopup`

## observe()
- 位置: L434-446
- 役割: fullscreen-painted を受け、全画面解除後に openPopup をやり直す
- 触るとき: 全画面解除後にパネルを開き直す経路を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `this.openPopup()`
- 参照: `this._event`, `this._exitedEventReceived`
- XPCOM: `Services.obs`

## onLocationChange()
- 位置: L448-452
- 役割: ページ遷移時に再読み込みヒントを隠す
- 触るとき: ページ遷移時にパネルの案内表示をどう扱うかを変えるとき。
- 参照: `this._permissionPopup.state`, `this._permissionReloadHint.hidden`, `this._popupInitialized`

## updateSitePermissions()
- 位置: L457-665
- 役割: 対象ブラウザの権限を集め、項目を作り直して一覧へ入れる
- 触るとき: パネルに出る権限の種類や順序、3rdPartyStorage と 3rdPartyFrameStorage の統合、共有中の権限の補完を変えるとき。
- 呼び出し先: `Services.eTLD.getSite()`, `Services.io.newURI()`, `SitePermissions.getAllPermissionDetailsForBrowser()`, `e.remove()`, `permission.id.split()`, `permissions .map()`, `permissions.filter()`, `thirdPartyStorageSites.has()`, `this._permissionList .querySelectorAll()`, `this._permissionList .querySelectorAll(permissionItemSelector) .forEach()`, `this._permissionList.querySelector()`, `this.browser.popupAndRedirectBlocker.getBlockedPopupCount()`, `this.browser.popupAndRedirectBlocker.isRedirectBlocked()`
- 条件付き依存: `if (this._sharingState?.geo)` → `permissions.find()`
- 条件付き依存: `if (!(geoPermission))` → `permissions.push()`
- 条件付き依存: `if (this._sharingState?.xr)` → `permissions.find()`
- 条件付き依存: `if (!(xrPermission))` → `permissions.push()`
- 条件付き依存: `if (this._sharingState?.serial)` → `permissions.find()`
- 条件付き依存: `if (!(serialPermission))` → `permissions.push()`
- 条件付き依存: `if (webrtcState[id])` → `permission.id.split()`
- 条件付き依存: `if (!found)` → `permissions.push()`
- 条件付き依存: `if (id == "open-protocol-handler")` → `this._createProtocolHandlerPermissionItem()`
- 条件付き依存: `if (permContainer)` → `anchor.appendChild()`
- 条件付き依存: `if (!(id == "open-protocol-handler"))` → `["camera", "screen", "microphone", "speaker"].includes()`
- 条件付き依存: `if (["camera", "screen", "microphone", "speaker"].includes(id))` → `this._createWebRTCPermissionItem()`
- 条件付き依存: `if (["camera", "screen", "microphone", "speaker"].includes(id))` → `anchor.appendChild()`
- 条件付き依存: `if (!(["camera", "screen", "microphone", "speaker"].includes(id)))` → `this._createPermissionItem()`
- 条件付き依存: `if (id == "3rdPartyFrameStorage")` → `this._permissionList.querySelector()`
- 条件付き依存: `if (!(["camera", "screen", "microphone", "speaker"].includes(id)))` → `anchor.appendChild()`
- 条件付き依存: `if (id == "popup" && showBlockedIndicator)` → `this._createBlockedPopupIndicator()`
- 条件付き依存: `if (id == "geo" && permission.state === SitePermissions.ALLOW)` → `this._createGeoLocationLastAccessIndicator()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `SitePermissions.getDefault()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `this._createPermissionItem()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `this._defaultPermissionAnchor.appendChild()`
- 条件付き依存: `if (showBlockedIndicator && !hasBlockedIndicator)` → `this._createBlockedPopupIndicator()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.PERM_KEY_DELIMITER`, `SitePermissions.PROMPT`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_REQUEST`, `geoPermission.sharingState`, `perm.id`, `permission.sharingState`, `permission.state`, `serialPermission.sharingState`, `this._defaultPermissionAnchor`, `this._gumShowAlwaysAsk`, `this._permissionLabelIndex`, `this._sharingState`, `this._sharingState.webRTC`, `this._sharingState?.geo`, `this._sharingState?.serial`, `this._sharingState?.webRTC`, `this._sharingState?.xr`, `this.browser`, `this.browser._sharingState`, `xrPermission.sharingState`
- XPCOM: `Services.eTLD` / `Services.io`

## _createPermissionItem()
- 位置: L686-868
- 役割: 権限1件分の XUL 行を作り、状態表示と解除ボタンを付けて返す
- 触るとき: 権限行の構成を変えるとき。popup と autoplay-media は状態メニュー付き、ポリシー権限は解除ボタン無しという分岐を確認する。
- 呼び出し先: `SitePermissions.getPermissionLabel()`, `[ SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL, ].includes()`, `container.appendChild()`, `container.classList.add()`, `container.setAttribute()`, `document.createXULElement()`, `img.classList.add()`, `nameLabel.setAttribute()`, `permission.sharingState.includes()`
- 条件付き依存: `if ( permission.state == SitePermissions.BLOCK || permission.state == SitePermissions.AUTOPLAY_BLOCKED_ALL )` → `img.classList.add()`
- 条件付き依存: `if ( permission.sharingState == Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED || (idNoSuffix == "screen" && permission.sharingState && !permission.sharingState...)` → `img.classList.add()`
- 条件付き依存: `if (nowrapLabel)` → `nameLabel.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `document.createXULElement()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `block.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menulist.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `Services.prefs.prefIsLocked()`
- 条件付き依存: `if ( idNoSuffix == "popup" && Services.prefs.prefIsLocked("dom.disable_open_during_load") )` → `menulist.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.getAvailableStates()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.getDefault()`
- 条件付き依存: `if (state == SitePermissions.getDefault(idNoSuffix))` → `menuitem.setAttribute()`
- 条件付き依存: `if (!(state == SitePermissions.getDefault(idNoSuffix)))` → `menuitem.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menuitem.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.getMultichoiceStateLabel()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menupopup.appendChild()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menulist.appendChild()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `menulist.addEventListener()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `container.appendChild()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `container.setAttribute()`
- 条件付き依存: `if ( (idNoSuffix == "popup" && !isPolicyPermission) || idNoSuffix == "autoplay-media" )` → `block.appendChild()`
- 条件付き依存: `if (showStateLabel)` → `this._createStateLabel()`
- 条件付き依存: `if (stateLabel)` → `container.appendChild()`
- 条件付き依存: `if (isContainer)` → `document.createXULElement()`
- 条件付き依存: `if (isContainer)` → `block.setAttribute()`
- 条件付き依存: `if (permClearButton)` → `this._createPermissionClearButton()`
- 条件付き依存: `if (stateLabel)` → `button.appendChild()`
- 条件付き依存: `if (permClearButton)` → `container.appendChild()`
- 条件付き依存: `if (isContainer)` → `block.appendChild()`
- 参照: `Ci.nsIMediaManagerService.STATE_CAPTURE_ENABLED`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`, `SitePermissions.SCOPE_GLOBAL`, `SitePermissions.SCOPE_POLICY`, `gBrowser.contentPrincipal`, `menulist.selectedItem.value`, `menulist.value`, `nameLabel.textContent`, `permission.id`, `permission.scope`, `permission.sharingState`, `permission.state`, `stateLabel.id`, `this ._permissionLabelIndex`
- XPCOM: [`nsIMediaManagerService`](../../../dom/media/nsIMediaManager.idl.md) / `Services.prefs`

## _createStateLabel()
- 位置: L870-889
- 役割: 権限の状態文言を作る。共有中で未許可なら一時許可として表示する
- 触るとき: 一時許可などの状態文言の判定や表示を変えるとき。
- 呼び出し先: `SitePermissions.getCurrentStateLabel()`, `document.createXULElement()`, `label.setAttribute()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.SCOPE_REQUEST`, `aPermission.sharingState`, `label.textContent`, `this ._permissionLabelIndex`

## _removePermPersistentAllow()
- 位置: L891-899
- 役割: 永続の ALLOW 権限だけを principal から削除する
- 触るとき: XR の共有 origin ごとの許可を解除する処理を変えるとき。
- 呼び出し先: `SitePermissions.getForPrincipal()`
- 条件付き依存: `if ( perm.state == SitePermissions.ALLOW && perm.scope == SitePermissions.SCOPE_PERSISTENT )` → `SitePermissions.removeFromPrincipal()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.SCOPE_PERSISTENT`, `perm.scope`, `perm.state`

## _createPermissionClearButton()
- 位置: L901-998
- 役割: 解除ボタンを作り、押下時に権限を削除して再読み込み案内を出す
- 触るとき: 解除時に連動して消す権限(3rdPartyFrameStorage 配下の 3rdPartyStorage、XR の origin)や通知の計測、geo、xr、serial の共有停止を変えるとき。
- 呼び出し先: `SitePermissions.removeFromPrincipal()`, `button.addEventListener()`, `button.setAttribute()`, `clearCallback()`, `container.remove()`, `document.createXULElement()`, `gNavigatorBundle.getString()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `browser.getDevicePermissionOrigins()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `this._removePermPersistentAllow()`
- 条件付き依存: `if (permission.sharingState && idNoSuffix === "xr")` → `origins.clear()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `permission.id.split()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `SitePermissions.getAllForBrowser()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `permissions.filter()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `removePermission.id.split()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `Services.io.newURI()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `Services.eTLD.getSite()`
- 条件付き依存: `if (idNoSuffix == "3rdPartyFrameStorage")` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (idNoSuffix === "desktop-notification")` → `Glean.webNotificationPermission.permissionRevokedToolbar.record()`
- 条件付き依存: `if (idNoSuffix === "desktop-notification")` → `SiteCategory.getCategory()`
- 条件付き依存: `if (idNoSuffix === "geo")` → `gBrowser.updateBrowserSharing()`
- 条件付き依存: `if (idNoSuffix === "xr")` → `gBrowser.updateBrowserSharing()`
- 条件付き依存: `if (idNoSuffix === "serial")` → `SerialDeviceSharingHelper.resetBrowserCount()`
- 条件付き依存: `if (idNoSuffix === "serial")` → `gBrowser.updateBrowserSharing()`
- 条件付き依存: `if (idNoSuffix === "serial")` → `Services.obs.notifyObservers()`
- 参照: `SitePermissions.PERM_KEY_DELIMITER`, `browser.browsingContext`, `browser.contentPrincipal`, `gBrowser.contentPrincipal`, `permission.id`, `permission.sharingState`, `removePermission.id`, `this._permissionReloadHint.hidden`, `this.browser`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.obs` / `Services.scriptSecurityManager`

## _getGeoLocationLastAccess()
- 位置: L1000-1017
- 役割: 現在のページの位置情報最終アクセス時刻を ContentPref から Promise で取り出す
- 触るとき: 位置情報の最終利用時刻の保存キーや取得元を変えるとき。
- 呼び出し先: `ContentPrefService2.getByDomainAndName()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.loadContext`

## handleResult()
- 位置: L1008-1010
- 役割: ContentPref の結果から最終アクセス値を保持する
- 触るとき: 最終アクセス値の読み出し方を変えるとき。
- 参照: `pref.value`

## handleCompletion()
- 位置: L1011-1013
- 役割: 取得の完了時に保持した値で Promise を解決する
- 触るとき: 最終アクセス取得の完了時の扱いを変えるとき。
- 呼び出し先: `resolve()`

## _createGeoLocationLastAccessIndicator()
- 位置: async L1019-1062
- 役割: 位置情報の最終アクセスを相対時刻で示す行を地理情報の項目に追加する
- 触るとき: 最終利用の表示文言や表示条件を変えるとき。非同期で、待つ間にパネルが閉じたり再描画されたりしうる点を確かめる。
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `gNavigatorBundle.getFormattedString()`, `geoContainer.appendChild()`, `indicator.appendChild()`, `indicator.setAttribute()`, `isNaN()`, `text.setAttribute()`, `this._getGeoLocationLastAccess()`, `timeFormat.formatBestUnit()`
- 条件付き依存: `if (isNaN(lastAccess))` → `console.error()`
- 参照: `Services.intl.RelativeTimeFormat`, `text.textContent`
- XPCOM: `Services.intl`

## _createWebRTCPermissionItem()
- 位置: L1074-1113
- 役割: カメラ、マイク、画面、スピーカーの項目を、デバイス単位の許可に合わせて作る
- 触るとき: WebRTC 権限の重複排除(デバイス単位の項目と単一キーの項目のどちらを優先するか)を変えるとき。
- 呼び出し先: `["camera", "screen", "microphone", "speaker"].includes()`, `document.querySelector()`, `this._createPermissionItem()`
- 条件付き依存: `if (item)` → `item.remove()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.PROMPT`, `permission.state`

## clearCallback()
- 位置: L1109-1111
- 役割: WebRTC 項目の解除時に、該当 ID の共有を止める
- 触るとき: WebRTC 項目の解除から共有停止までの流れを変えるとき。
- 呼び出し先: `webrtcUI.clearPermissionsAndStopSharing()`
- 参照: `this.browser`

## _createProtocolHandlerPermissionItem()
- 位置: L1115-1172
- 役割: 外部プロトコル起動の許可を1つのコンテナにまとめ、1件ずつ行を足す
- 触るとき: プロトコルハンドラ権限のまとめ方や解除後の後片付けを変えるとき。最後の1件を消すとコンテナも消える。
- 呼び出し先: `button.appendChild()`, `container.appendChild()`, `document.createXULElement()`, `document.getElementById()`, `gNavigatorBundle.getFormattedString()`, `item.appendChild()`, `item.setAttribute()`, `text.setAttribute()`, `this._createPermissionClearButton()`, `this._createStateLabel()`
- 条件付き依存: `if (!container)` → `this._createPermissionItem()`
- 参照: `text.textContent`

## clearCallback()
- 位置: L1156-1163
- 役割: プロトコルハンドラの項目を解除したとき、残りが無ければコンテナを消す
- 触るとき: プロトコルハンドラ項目の解除後の後片付けを変えるとき。
- 条件付き依存: `if (container.childElementCount <= 1)` → `container.remove()`
- 参照: `container.childElementCount`

## _createBlockedRedirectText()
- 位置: L1174-1184
- 役割: 第三者リダイレクトの遮断を解除するリンク文言を作る
- 触るとき: リダイレクト遮断の解除リンクの文言や動作を変えるとき。
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockFirstRedirect()`, `text.addEventListener()`, `text.setAttribute()`

## _createBlockedPopupText()
- 位置: L1186-1198
- 役割: 遮断したポップアップ数を示し、押すと全て許可するリンクを作る
- 触るとき: ポップアップ遮断の解除リンクや件数表示を変えるとき。
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockAllPopups()`, `text.addEventListener()`, `text.setAttribute()`

## _createBlockedPopupIndicator()
- 位置: L1200-1219
- 役割: 遮断したポップアップとリダイレクトの行を permission-popup-container に追加する
- 触るとき: 遮断表示の行の構成や追加先を変えるとき。sitePermissions.ftl を読み込むので、翻訳 ID を足したときもここを確認する。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document .getElementById()`, `document .getElementById("permission-popup-container") .appendChild()`, `document.createXULElement()`, `indicator.setAttribute()`
- 条件付き依存: `if (aIsRedirectBlocked)` → `indicator.appendChild()`
- 条件付き依存: `if (aIsRedirectBlocked)` → `this._createBlockedRedirectText()`
- 条件付き依存: `if (aTotalBlockedPopups)` → `indicator.appendChild()`
- 条件付き依存: `if (aTotalBlockedPopups)` → `this._createBlockedPopupText()`

## hasMicCamGracePeriodsSolely()
- 位置: L1229-1262
- 役割: カメラかマイクに一時許可の猶予期間があり、永続許可が無いかを判定する
- 触るとき: 共有表示の猶予期間インジケーターを出す条件を変えるとき。updateSharingIndicator から呼ばれる。
- 呼び出し先: `SitePermissions.getAllForBrowser()`, `perm.id.split()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.PERM_KEY_DELIMITER`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_TEMPORARY`, `perm.scope`, `perm.state`
