# browser/base/content/browser-siteIdentity.js

source: browser/base/content/browser-siteIdentity.js
source-hash: 16b222280f856e697f11fee76798cc2afe0bc239
lines: 1458

## <module>
- 役割: サイトアイデンティティ（アドレスバー左の鍵・ID アイコン）と、そのポップアップの表示・更新を担う gIdentityHandler を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _isBrokenConnection()
- 位置: L76-78
- 役割: セキュリティ状態のビットに STATE_IS_BROKEN が立っているかを返す（混在コンテンツや弱い暗号など）。
- 触るとき: 接続が壊れている扱いの条件を追加・変更するとき、またはアイコンの警告色が出る理由を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IS_BROKEN`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isSecureConnection()
- 位置: L87-96
- 役割: STATE_IS_SECURE が立ち、かつファイル URI で読み込んでいないときに真を返す。埋め込み browser の状態は反映しない。
- 触るとき: 安全な接続と判定する条件を変えるとき、または file: ページで鍵が出ない理由を追うとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IS_SECURE`, `this._isURILoadedFromFile`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isEV()
- 位置: L98-107
- 役割: EV 証明書の状態ビットが立ち、ファイル URI でないときに真を返す。
- 触るとき: EV 表示（組織名の表示など）の条件を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_EV_TOPLEVEL`, `this._isURILoadedFromFile`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isAssociatedIdentity()
- 位置: L109-111
- 役割: STATE_IDENTITY_ASSOCIATED のビットを返す（別ページに関連付けられた ID）。
- 触るとき: 関連付けられた ID の表示（中立アイコン）の判定を見直すとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_ASSOCIATED`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isMixedActiveContentLoaded()
- 位置: L113-117
- 役割: 混在のアクティブコンテンツが読み込まれたかのビットを返す。
- 触るとき: 混在コンテンツの警告表示（mixedActiveContent）の条件を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isMixedActiveContentBlocked()
- 位置: L119-123
- 役割: 混在のアクティブコンテンツがブロックされたかのビットを返す。
- 触るとき: ブロック済みの混在コンテンツの表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_MIXED_ACTIVE_CONTENT`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isMixedPassiveContentLoaded()
- 位置: L125-129
- 役割: 混在のパッシブコンテンツ（表示系）が読み込まれたかのビットを返す。
- 触るとき: パッシブな混在コンテンツの警告表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_DISPLAY_CONTENT`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isContentHttpsOnlyModeUpgraded()
- 位置: L131-135
- 役割: HTTPS-Only Mode でコンテンツが HTTPS に昇格されたかのビットを返す。
- 触るとき: HTTPS-Only 昇格の表示（upgraded）の判定を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isContentHttpsOnlyModeUpgradeFailed()
- 位置: L137-142
- 役割: HTTPS-Only Mode の昇格に失敗したかのビットを返す。
- 触るとき: 昇格失敗（failed-top や failed-sub）の表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADE_FAILED`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isContentHttpsFirstModeUpgraded()
- 位置: L144-149
- 役割: HTTPS-First Mode で昇格されたかのビットを返す。
- 触るとき: HTTPS-First の昇格表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED_FIRST`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isCertUserOverridden()
- 位置: L151-153
- 役割: 利用者が証明書エラーを例外として許可しているかのビットを返す。
- 触るとき: 証明書の例外許可時の表示（verified_by_you）を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_CERT_USER_OVERRIDDEN`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isCertErrorPage()
- 位置: L155-166
- 役割: about:certerror、または nssFailure2 の about:neterror かを判定する。
- 触るとき: 証明書エラーページでの鍵アイコンや接続の扱いを変えるとき。
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isSecurelyConnectedAboutNetErrorPage()
- 位置: L168-178
- 役割: about:neterror のうち接続問題を伴わないエラー（httpErrorPage、serverError）かを判定する。
- 触るとき: 接続は安全だがエラーページである場合の表示を変えるとき。
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isAboutNetErrorPage()
- 位置: L180-183
- 役割: 現在の文書が about:neterror かを判定する。
- 触るとき: ネットエラーページの表示（中立アイコン、接続種別）を変えるとき。
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isAboutHttpsOnlyErrorPage()
- 位置: L185-190
- 役割: 現在の文書が about:httpsonlyerror かを判定する。
- 触るとき: HTTPS-Only のエラーページでの表示や権限変更の経路を追うとき。
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isPotentiallyTrustworthy()
- 位置: L192-198
- 役割: 接続が壊れておらず、安全なコンテキストか chrome URI のときに真を返す（localhost などローカルのリソース）。
- 触るとき: ローカルリソースを安全扱いする条件を変えるとき。
- 参照: `gBrowser.selectedBrowser.documentURI?.scheme`, `this._isBrokenConnection`, `this._isSecureContext`

## _isAboutBlockedPage()
- 位置: L200-203
- 役割: 現在の文書が about:blocked かを判定する。
- 触るとき: about:blocked ページでの表示（中立アイコン）を変えるとき。
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _initializePopup()
- 位置: L206-213
- 役割: テンプレートのポップアップを一度だけ展開し、リスナーを登録する。
- 触るとき: ID ポップアップの初回表示を遅らせたい、または展開の順序を変えたいとき。
- 条件付き依存: `if (!this._popupInitialized)` → `document.getElementById()`
- 条件付き依存: `if (!this._popupInitialized)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this._popupInitialized)` → `this._initializePopupListeners()`
- 参照: `this._popupInitialized`, `wrapper.content`

## _initializePopupListeners()
- 位置: L215-245
- 役割: ポップアップの popupshown と popuphidden を登録し、各ボタン ID に対応する command ハンドラを付ける。
- 触るとき: ID ポップアップに新しいボタンを追加するとき。
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `document.getElementById(id).addEventListener()`, `popup.addEventListener()`, `this.onPopupHidden()`, `this.onPopupShown()`
- 参照: `this._identityPopup`

## "identity-popup-security-button"()
- 位置: L225-227
- 役割: セキュリティ詳細のサブビューを開く。
- 触るとき: セキュリティ詳細ビューへの入り方を変えるとき。
- 呼び出し先: `this.showSecuritySubView()`

## "identity-popup-security-httpsonlymode-menulist"()
- 位置: L228-230
- 役割: HTTPS-Only の例外メニューの選択を changeHttpsOnlyPermission に渡す。
- 触るとき: HTTPS-Only の例外設定の変更処理の入口を追うとき。
- 呼び出し先: `this.changeHttpsOnlyPermission()`

## "identity-popup-clear-sitedata-button"()
- 位置: L231-233
- 役割: 「サイトデータを消去」ボタンの command を clearSiteData に渡す。
- 触るとき: サイトデータ消去の経路を変えるとき。
- 呼び出し先: `this.clearSiteData()`

## "identity-popup-remove-cert-exception"()
- 位置: L234-236
- 役割: 証明書例外の削除ボタンを removeCertException に渡す。
- 触るとき: 証明書例外の取り消し操作を変えるとき。
- 呼び出し先: `this.removeCertException()`

## "identity-popup-more-info"()
- 位置: L237-239
- 役割: 「詳細情報」ボタンを handleMoreInfoClick に渡す。
- 触るとき: ページ情報（詳細）を開く経路を変えるとき。
- 呼び出し先: `this.handleMoreInfoClick()`

## hidePopup()
- 位置: L247-251
- 役割: ポップアップが初期化済みなら PanelMultiView で閉じる。
- 触るとき: ID ポップアップを他の操作から閉じる条件を追加するとき。
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 参照: `this._identityPopup`, `this._popupInitialized`

## _identityPopup()
- 位置: L254-260
- 役割: id identity-popup の要素を、初期化後に初回参照でキャッシュして返す。未初期化なら null。
- 触るとき: ID ポップアップ要素の参照先を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopup`, `this._popupInitialized`

## _identityBox()
- 位置: L261-264
- 役割: id identity-box の要素を取得してキャッシュする。
- 触るとき: アイデンティティボックスの class を変える箇所を追うとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityBox`

## _identityIconBox()
- 位置: L265-269
- 役割: id identity-icon-box の要素を取得してキャッシュする。ポップアップのアンカーにも使う。
- 触るとき: ID ポップアップの表示位置（アンカー）を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityIconBox`

## _identityPopupMultiView()
- 位置: L270-275
- 役割: ポップアップ内の multiView 要素を取得してキャッシュする。
- 触るとき: ポップアップ内のサブビュー切り替えを扱うとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupMultiView`

## _identityPopupMainView()
- 位置: L276-281
- 役割: メインビュー要素を取得してキャッシュする。
- 触るとき: メインビューの属性（footerVisible など）を操作するとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupMainView`

## _identityPopupMainViewHeaderLabel()
- 位置: L282-287
- 役割: メインビューのヘッダー文字列の要素を取得してキャッシュする。
- 触るとき: ポップアップのヘッダー（サイト情報）の表示を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupMainViewHeaderLabel`

## _identityPopupSecurityView()
- 位置: L288-293
- 役割: セキュリティビュー要素を取得してキャッシュする。
- 触るとき: セキュリティビューのヘッダー（ホスト名つき）を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupSecurityView`

## _identityPopupHttpsOnlyMode()
- 位置: L294-299
- 役割: HTTPS-Only の行の要素を取得してキャッシュする。
- 触るとき: HTTPS-Only の行の表示条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupHttpsOnlyMode`

## _identityPopupHttpsOnlyModeMenuList()
- 位置: L300-305
- 役割: HTTPS-Only の例外メニューリストを取得してキャッシュする。
- 触るとき: 例外メニューの選択値の読み書きを追うとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupHttpsOnlyModeMenuList`

## _identityPopupHttpsOnlyModeMenuListOffItem()
- 位置: L306-310
- 役割: 例外メニューの「オフ」項目を取得してキャッシュする。
- 触るとき: プライベートウィンドウで「オフ」項目を隠す条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupHttpsOnlyModeMenuListOffItem`

## _identityPopupSecurityEVContentOwner()
- 位置: L311-316
- 役割: EV の組織名を出す要素を取得してキャッシュする。
- 触るとき: EV の組織名の表示を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupSecurityEVContentOwner`

## _identityPopupContentOwner()
- 位置: L317-322
- 役割: 所有者（組織名）の表示要素を取得してキャッシュする。
- 触るとき: 所有者の表示位置や内容を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupContentOwner`

## _identityPopupContentSupp()
- 位置: L323-328
- 役割: 補足情報（所在地など）の表示要素を取得してキャッシュする。
- 触るとき: 証明書の所在地表示を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupContentSupp`

## _identityPopupContentVerif()
- 位置: L329-334
- 役割: 検証者（CA 名）の表示要素を取得してキャッシュする。
- 触るとき: 検証者表示の文字列を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupContentVerif`

## _identityPopupCustomRootLearnMore()
- 位置: L335-340
- 役割: カスタムルート証明書の「詳細」リンクの要素を取得してキャッシュする。
- 触るとき: カスタムルート（ユーザー追加の CA）の説明リンクを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupCustomRootLearnMore`

## _identityPopupMixedContentLearnMore()
- 位置: L341-346
- 役割: 混在コンテンツの「詳細」リンク（.identity-popup-mcb-learn-more）をすべて配列で取得する。
- 触るとき: 混在コンテンツの説明リンクを追加・変更するとき。
- 呼び出し先: `document.querySelectorAll()`
- 参照: `this._identityPopupMixedContentLearnMore`

## _identityIconLabel()
- 位置: L348-353
- 役割: id identity-icon-label の要素を取得してキャッシュする。
- 触るとき: アイコン横のラベル（Not Secure など）の文字列を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityIconLabel`

## _overrideService()
- 位置: L354-359
- 役割: 証明書オーバーライドサービスを初回参照時に取得してキャッシュする。
- 触るとき: 証明書例外を操作する処理を追うとき。
- 呼び出し先: `Cc[ "@mozilla.org/security/certoverride;1" ].getService()`
- 参照: `Ci.nsICertOverrideService`, `this._overrideService`
- XPCOM: `nsICertOverrideService` / `@mozilla.org/security/certoverride;1`

## _identityIcon()
- 位置: L360-363
- 役割: id identity-icon の要素を取得してキャッシュする。
- 触るとき: アイコン本体のツールチップを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityIcon`

## _clearSiteDataFooter()
- 位置: L364-369
- 役割: 「サイトデータを消去」フッターの要素を取得してキャッシュする。
- 触るとき: フッターの表示条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._clearSiteDataFooter`

## _insecureConnectionTextEnabled()
- 位置: L370-378
- 役割: security.insecure_connection_text.enabled の設定値を遅延取得して保持する。
- 触るとき: 安全でない接続の文言表示をフラグ制御するとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._insecureConnectionTextEnabled`

## _insecureConnectionTextPBModeEnabled()
- 位置: L379-387
- 役割: プライベートブラウジング用の insecure 文言の設定値を遅延取得して保持する。
- 触るとき: プライベートウィンドウだけで文言を出す条件を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._insecureConnectionTextPBModeEnabled`

## _httpsOnlyModeEnabled()
- 位置: L388-396
- 役割: dom.security.https_only_mode の設定値を遅延取得して保持する。
- 触るとき: HTTPS-Only Mode の有効判定を見直すとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsOnlyModeEnabled`

## _httpsOnlyModeEnabledPBM()
- 位置: L397-405
- 役割: プライベートウィンドウ向け HTTPS-Only の設定値を遅延取得して保持する。
- 触るとき: プライベートウィンドウでの HTTPS-Only の判定を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsOnlyModeEnabledPBM`

## _httpsFirstModeEnabled()
- 位置: L406-419
- 役割: dom.security.https_first の設定値を遅延取得して保持する（兄弟の pref とは別登録）。
- 触るとき: HTTPS-First の有効判定を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsFirstModeEnabled`

## _httpsFirstModeEnabledPBM()
- 位置: L420-428
- 役割: プライベートウィンドウ向けの HTTPS-First の設定値を遅延取得して保持する。
- 触るとき: プライベートウィンドウでの HTTPS-First の判定を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsFirstModeEnabledPBM`

## _schemelessHttpsFirstModeEnabled()
- 位置: L429-437
- 役割: dom.security.https_first_schemeless の設定値を遅延取得して保持する。
- 触るとき: スキームなし入力の HTTPS-First 判定を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._schemelessHttpsFirstModeEnabled`

## _isHttpsOnlyModeActive()
- 位置: L439-444
- 役割: 通常の HTTPS-Only の設定、またはプライベートウィンドウで PBM の設定が有効なら真を返す。
- 触るとき: HTTPS-Only が有効かどうかの判定を変えるとき。
- 参照: `this._httpsOnlyModeEnabled`, `this._httpsOnlyModeEnabledPBM`

## _isHttpsFirstModeActive()
- 位置: L445-451
- 役割: HTTPS-Only が無効で、HTTPS-First（通常または PBM）が有効なら真を返す。
- 触るとき: HTTPS-First の有効判定の優先順位を変えるとき。
- 呼び出し先: `this._isHttpsOnlyModeActive()`
- 参照: `this._httpsFirstModeEnabled`, `this._httpsFirstModeEnabledPBM`

## _isSchemelessHttpsFirstModeActive()
- 位置: L452-458
- 役割: HTTPS-Only も HTTPS-First も無効で、スキームなし HTTPS-First が有効なら真を返す。
- 触るとき: スキームなし HTTPS-First の表示条件を変えるとき。
- 呼び出し先: `this._isHttpsFirstModeActive()`, `this._isHttpsOnlyModeActive()`
- 参照: `this._schemelessHttpsFirstModeEnabled`

## clearSiteData()
- 位置: async L463-484
- 役割: ポップアップを閉じるのを待ってから、ベースドメインのサイトデータ消去を確認ダイアログ経由で実行する。
- 触るとき: サイトデータ消去の確認や対象ドメインの決め方を変えるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `SiteDataManager.getBaseDomainFromHost()`, `SiteDataManager.promptSiteDataRemoval()`, `event.stopPropagation()`, `this._identityPopup.addEventListener()`
- 条件付き依存: `if (SiteDataManager.promptSiteDataRemoval(window, [baseDomain]))` → `SiteDataManager.remove()`
- 参照: `this._identityPopup`, `this._uri.host`, `this._uriHasHost`

## handleMoreInfoClick()
- 位置: L490-494
- 役割: ページ情報（displaySecurityInfo）を開き、イベントを止めてポップアップを閉じる。
- 触るとき: 詳細情報ボタンの後の動作を変えるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `displaySecurityInfo()`, `event.stopPropagation()`
- 参照: `this._identityPopup`

## showSecuritySubView()
- 位置: L496-505
- 役割: セキュリティ詳細のサブビューを表示し、非表示ビューの要素からフォーカスを外す。
- 触るとき: セキュリティ詳細ビューに入る際のフォーカス処理を変えるとき。
- 呼び出し先: `Services.focus.clearFocus()`, `document.getElementById()`, `this._identityPopupMultiView.showSubView()`
- XPCOM: `Services.focus`

## removeCertException()
- 位置: L507-525
- 役割: ホストとポート（省略時 443）の証明書オーバーライドを解除し、キャッシュを無視して再読み込みし、ポップアップを閉じる。
- 触るとき: 証明書例外の取り消し後の再読み込みや対象ポートを変えるとき。
- 呼び出し先: `BrowserCommands.reloadSkipCache()`, `this._overrideService.clearValidityOverride()`
- 条件付き依存: `if (!this._uriHasHost)` → `console.error()`
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 参照: `gBrowser.contentPrincipal.originAttributes`, `this._identityPopup`, `this._popupInitialized`, `this._uri.host`, `this._uri.port`, `this._uriHasHost`

## _getHttpsOnlyPermission()
- 位置: L532-557
- 役割: 現在ページの http 版の HTTPS-Only 権限を読み、オフ一時（2）、オフ（1）、オン（0）、非対応スキーム（-1）を返す。
- 触るとき: HTTPS-Only の例外の値と状態の対応を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `SitePermissions.getForPrincipal()`, `uri.mutate()`, `uri.mutate().setScheme()`, `uri.mutate().setScheme("http").finalize()`, `uri.schemeIs()`
- 条件付き依存: `if (uri instanceof Ci.nsINestedURI)` → `uri.QueryInterface()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `uri.QueryInterface(Ci.nsINestedURI).innermostURI`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / `Services.scriptSecurityManager`

## changeHttpsOnlyPermission()
- 位置: L562-647
- 役割: メニューの新しい値と現在値を比べ、http 版に権限を設定・削除する。エラーページなら https から http へ遷移させ、それ以外は合計が 3 でなければ再読み込み、3 ならポップアップを更新する。
- 触るとき: HTTPS-Only の例外の切り替え時の再読み込みの有無を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `newURI.mutate()`, `newURI.mutate().setScheme()`, `newURI.mutate().setScheme("http").finalize()`, `parseInt()`, `this._getHttpsOnlyPermission()`, `this.refreshIdentityPopup()`
- 条件付き依存: `if (oldValue < 0)` → `console.error()`
- 条件付き依存: `if (newURI instanceof Ci.nsINestedURI)` → `newURI.QueryInterface()`
- 条件付き依存: `if (newValue === 0)` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (newValue === 1)` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!(newValue === 1))` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (this._isAboutHttpsOnlyErrorPage)` → `gBrowser.loadURI()`
- 条件付き依存: `if (this._isAboutHttpsOnlyErrorPage)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `BrowserCommands.reloadSkipCache()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `gBrowser.selectedBrowser.focus()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_SESSION`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `newURI.QueryInterface(Ci.nsINestedURI).innermostURI`, `this._identityPopup`, `this._identityPopupHttpsOnlyModeMenuList.selectedItem.value`, `this._isAboutHttpsOnlyErrorPage`, `this._popupInitialized`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## getIdentityData()
- 位置: L653-678
- 役割: 証明書から組織名、サブジェクトの各フィールド（L、ST、C）、発行者名を取り出して結果を返す。
- 触るとき: 証明書の表示項目を増やす、または解析方法を変えるとき。
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split(",").forEach()`
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split()`
- 条件付き依存: `if (cert.subjectName)` → `v.split()`
- 参照: `cert.issuerCommonName`, `cert.issuerOrganization`, `cert.organization`, `cert.subjectName`, `result.caOrg`, `result.cert`, `result.city`, `result.country`, `result.state`, `result.subjectNameFields`, `result.subjectNameFields.C`, `result.subjectNameFields.L`, `result.subjectNameFields.ST`, `result.subjectOrg`, `this._secInfo.serverCert`

## _getIsSecureContext()
- 位置: L680-704
- 役割: 通常は securityUI の isSecureContext を返す。pdf.js ページだけは文書 URI から安全判定を計算し、例外時は false を返す。
- 触るとき: PDF ビューアページの安全判定を調べるとき、または isSecureContext の取り方を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `console.error()`
- 参照: `gBrowser.contentPrincipal?.originNoSuffix`, `gBrowser.securityUI.isSecureContext`, `gBrowser.selectedBrowser.documentURI`, `principal.isOriginPotentiallyTrustworthy`
- XPCOM: `Services.scriptSecurityManager`

## updateIdentity()
- 位置: L718-744
- 役割: 状態ビットと URI、セキュリティ情報を設定してアイコンとブロックを更新する。URI が変わったときは QWAC の状態を消し、ポップアップを閉じる。
- 触るとき: セキュリティ状態の変更通知を受けてアイコンを更新する流れを追うとき、またはページ遷移時の表示のリセットを変えるとき。
- 呼び出し先: `this._getIsSecureContext()`, `this.refreshIdentityBlock()`, `this.setURI()`
- 条件付き依存: `if (locationChanged)` → `this.hidePopup()`
- 条件付き依存: `if (locationChanged)` → `gPermissionPanel.hidePopup()`
- 参照: `gBrowser.securityUI.secInfo`, `this._isSecureContext`, `this._qwac`, `this._qwacStatusPromise`, `this._secInfo`, `this._state`, `this._uri`, `this._uri.spec`, `uri.spec`

## getEffectiveHost()
- 位置: L751-764
- 役割: ホストを IDN サービスで表示用に変換して返す。失敗時は uri.host をそのまま返す。
- 触るとき: 国際化ドメイン名の表示を変えるとき。
- 呼び出し先: `this._IDNService.convertToDisplayIDN()`
- 条件付き依存: `if (!this._IDNService)` → `Cc["@mozilla.org/network/idn-service;1"].getService()`
- 参照: `Ci.nsIIDNService`, `this._IDNService`, `this._uri`, `uri.host`
- XPCOM: [`nsIIDNService`](../../../netwerk/dns/nsIIDNService.idl.md) / `@mozilla.org/network/idn-service;1`

## getHostForDisplay()
- 位置: L766-808
- 役割: 表示用のホスト名を決める。about:、chrome:、リーダーモード、拡張機能名の順に上書きし、無ければ spec（ref を除く）を使う。
- 触るとき: ポップアップ見出しに出す名前の決め方を変えるとき。
- 呼び出し先: `ReaderMode.getOriginalUrlObjectForDisplay()`, `this.getEffectiveHost()`, `uri.schemeIs()`
- 参照: `readerStrippedURI.host`, `this._pageExtensionPolicy`, `this._pageExtensionPolicy.name`, `this._uri`, `uri.displaySpec`, `uri.filePath`, `uri.spec`, `uri.specIgnoringRef`

## pointerlockFsWarningClassName()
- 位置: L815-821
- 役割: 安全な接続なら verifiedDomain、そうでなければ unknownIdentity を返す。全画面の警告のクラス名に使う。
- 触るとき: 全画面の警告の見た目を接続状態で変えるとき。
- 参照: `this._isSecureConnection`, `this._uriHasHost`

## _hasCustomRoot()
- 位置: L829-836
- 役割: 安全な接続で、例外が無く、ルートが組み込みでないときに真を返す（ユーザー追加の CA）。
- 触るとき: カスタムルートの警告表示の条件を変えるとき。
- 参照: `this._isCertUserOverridden`, `this._isSecureConnection`, `this._secInfo`, `this._secInfo.isBuiltCertChainRootBuiltInRoot`

## _hasInvalidPageProxyState()
- 位置: L843-850
- 役割: ホストが無く、空白ページで、拡張 URL でないときに真を返す。権限アイコンを隠す条件に使う。
- 触るとき: 空白ページでの権限アイコンの表示を変えるとき。
- 呼び出し先: `ExtensionUtils.isExtensionUrl()`, `isBlankPageURL()`
- 参照: `this._uri`, `this._uri.spec`, `this._uriHasHost`

## _refreshIdentityIcons()
- 位置: L855-968
- 役割: 接続状態ごとに identity-box の class とツールチップ、アイコンのラベルを設定する。内部 UI、拡張、安全、壊れた接続、エラーページ、ローカル、非安全の順で分岐する。
- 触るとき: アイコンの色（class）や文言、ツールチップを状態ごとに変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this._identityIcon.setAttribute()`, `this._identityIconLabel.setAttribute()`
- 条件付き依存: `if (this._isSecureInternalUI)` → `document.getElementById()`
- 条件付き依存: `if (this._isSecureInternalUI)` → `brandBundle.getString()`
- 条件付き依存: `if (this._pageExtensionPolicy)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (this._isMixedActiveContentBlocked)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (!this._isCertUserOverridden)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!this._isCertUserOverridden)` → `this.getIdentityData()`
- 条件付き依存: `if (this._isMixedActiveContentLoaded)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isMixedActiveContentLoaded)` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && warnTextOnInsecure )` → `gNavigatorBundle.getString()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && warnTextOnInsecure )` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isMixedPassiveContentLoaded)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (!(this._isMixedPassiveContentLoaded))` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isCertErrorPage)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!(this._isPotentiallyTrustworthy))` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (warnTextOnInsecure)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (warnTextOnInsecure)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isCertUserOverridden)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isCertUserOverridden)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (this._pageExtensionPolicy)` → `this._identityIcon.setAttribute()`
- 参照: `this._identityBox.className`, `this._identityIconLabel.collapsed`, `this._insecureConnectionTextEnabled`, `this._insecureConnectionTextPBModeEnabled`, `this._isAboutBlockedPage`, `this._isAboutHttpsOnlyErrorPage`, `this._isAboutNetErrorPage`, `this._isAssociatedIdentity`, `this._isBrokenConnection`, `this._isCertErrorPage`, `this._isCertUserOverridden`, `this._isMixedActiveContentBlocked`, `this._isMixedActiveContentLoaded`, `this._isMixedPassiveContentLoaded`, `this._isPotentiallyTrustworthy`, `this._isSecureConnection`, `this._isSecureInternalUI`, `this._pageExtensionPolicy`, `this._pageExtensionPolicy.name`, `this._uriHasHost`, `this.getIdentityData().caOrg`

## refreshIdentityBlock()
- 位置: L973-993
- 役割: アイコンを更新し、権限アイコンを（無効ページなら隠して）更新し、シールドのクロム表示を切り替える。
- 触るとき: アイデンティティブロック全体の再描画の内容を追加するとき。
- 呼び出し先: `gProtectionsHandler._trackingProtectionIconContainer.classList.toggle()`, `this._hasInvalidPageProxyState()`, `this._refreshIdentityIcons()`
- 条件付き依存: `if (this._hasInvalidPageProxyState())` → `gPermissionPanel.hidePermissionIcons()`
- 条件付き依存: `if (!(this._hasInvalidPageProxyState()))` → `gPermissionPanel.refreshPermissionIcons()`
- 参照: `this._identityBox`, `this._isSecureInternalUI`

## getConnectionSecurityInformation()
- 位置: L999-1030
- 役割: 内部 UI、拡張、ファイル、QWAC、EV、例外許可、安全、エラーページなどの順に判定し、接続種別の文字列（secure、file など）を返す。
- 触るとき: ポップアップの connection 属性の値を追加・変更するとき。
- 参照: `this._isAboutBlockedPage`, `this._isAboutHttpsOnlyErrorPage`, `this._isAboutNetErrorPage`, `this._isAssociatedIdentity`, `this._isCertErrorPage`, `this._isCertUserOverridden`, `this._isEV`, `this._isPotentiallyTrustworthy`, `this._isSecureConnection`, `this._isSecureInternalUI`, `this._isSecurelyConnectedAboutNetErrorPage`, `this._isURILoadedFromFile`, `this._pageExtensionPolicy`, `this._qwac`

## refreshIdentityPopup()
- 位置: L1037-1237
- 役割: サイトデータ消去フッター、セキュリティボタン、混在コンテンツ、弱い暗号、HTTPS-Only の状態、EV や QWAC の所有者と所在地を計算し、ポップアップの各要素に反映する。
- 触るとき: ID ポップアップの中身（所有者、混在コンテンツ、HTTPS-Only 状態）を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `document.getElementById()`, `document.l10n.setAttributes()`, `element.toggleAttribute()`, `gNavigatorBundle.getFormattedString()`, `identityPopupPanelView.removeAttribute()`, `mixedcontent.join()`, `this._hasCustomRoot()`, `this._isHttpsFirstModeActive()`, `this._isHttpsOnlyModeActive()`, `this._isSchemelessHttpsFirstModeActive()`, `this._updateAttribute()`, `this.getConnectionSecurityInformation()`, `this.getHostForDisplay()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && this._uriHasHost && !this._pageExtensionPolicy )` → `SiteDataManager.hasSiteData(this._uri.asciiHost).then()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && this._uriHasHost && !this._pageExtensionPolicy )` → `SiteDataManager.hasSiteData()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && this._uriHasHost && !this._pageExtensionPolicy )` → `identityPopupPanelView.setAttribute()`
- 条件付き依存: `if (disableSecurityButton)` → `securityButtonNode.classList.remove()`
- 条件付き依存: `if (!(disableSecurityButton))` → `securityButtonNode.classList.add()`
- 条件付き依存: `if (this._isMixedPassiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this._isMixedActiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this._isMixedActiveContentBlocked)` → `mixedcontent.push()`
- 条件付き依存: `if ( isHttpsFirstModeActive || isHttpsOnlyModeActive || isSchemelessHttpsFirstModeActive )` → `this._getHttpsOnlyPermission()`
- 条件付き依存: `if (this._isEV || this._qwac)` → `this.getIdentityData()`
- 条件付き依存: `if (iData.state && iData.country)` → `gNavigatorBundle.getFormattedString()`
- 参照: `iData.city`, `iData.country`, `iData.state`, `iData.subjectOrg`, `securityButtonNode.disabled`, `this._clearSiteDataFooter.hidden`, `this._identityIconLabel.tooltipText`, `this._identityPopupContentOwner.textContent`, `this._identityPopupContentSupp.textContent`, `this._identityPopupContentVerif.textContent`, `this._identityPopupHttpsOnlyMode.hidden`, `this._identityPopupHttpsOnlyModeMenuList.value`, `this._identityPopupHttpsOnlyModeMenuListOffItem.hidden`, `this._identityPopupMainViewHeaderLabel`, `this._identityPopupSecurityEVContentOwner.textContent`, `this._identityPopupSecurityView`, `this._isAboutHttpsOnlyErrorPage`, `this._isBrokenConnection`, `this._isCertUserOverridden`, `this._isContentHttpsFirstModeUpgraded`, `this._isContentHttpsOnlyModeUpgradeFailed`, `this._isContentHttpsOnlyModeUpgraded`, `this._isEV`, `this._isMixedActiveContentBlocked`, `this._isMixedActiveContentLoaded`, `this._isMixedPassiveContentLoaded`, `this._isSecureConnection`, `this._pageExtensionPolicy`, `this._qwac`, `this._secInfo.serverCert`, `this._uri.asciiHost`, `this._uriHasHost`

## setURI()
- 位置: L1239-1269
- 役割: ネストした URI を内側まで展開して保持し、ホストの有無、内部 UI の判定、拡張の一致、ファイル URI かを設定する。
- 触るとき: view-source などネスト URI の扱いを変えるとき。
- 呼び出し先: `WebExtensionPolicy.getByURI()`, `uri.QueryInterface()`, `uri.schemeIs()`
- 条件付き依存: `if (uri.schemeIs("about"))` → `E10SUtils.getAboutModule()`
- 条件付き依存: `if (module)` → `module.getURIFlags()`
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `Ci.nsINestedURI`, `this._isSecureInternalUI`, `this._isURILoadedFromFile`, `this._pageExtensionPolicy`, `this._uri`, `this._uri.host`, `this._uriHasHost`, `uri.QueryInterface(Ci.nsINestedURI).innerURI`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md)

## handleIdentityButtonEvent()
- 位置: L1274-1292
- 役割: アイデンティティボックスのクリックを、左クリック、Space、Enter のみ受け付け、URL が編集されていなければ _openPopup を呼ぶ。
- 触るとき: ID ポップアップを開く入力の種類を変えるとき。
- 呼び出し先: `event.stopPropagation()`, `gURLBar.getAttribute()`, `this._openPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## _openPopup()
- 位置: L1294-1329
- 役割: ポップアップを初期化し、安全なコンテキストなら QWAC 判定を非同期に開始し、表示内容を更新して他のパネルを閉じ、アイコン位置に開く。
- 触るとき: ID ポップアップを開く前の準備や他パネルとの排他を変えるとき。
- 呼び出し先: `Array.from()`, `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `document.querySelectorAll()`, `this._initializePopup()`, `this.refreshIdentityPopup()`
- 条件付き依存: `if (this._isSecureContext && !this._qwacStatusPromise)` → `QWACs.determineQWACStatus( this._secInfo, this._uri, gBrowser.selectedBrowser.browsingContext ).then()`
- 条件付き依存: `if (this._isSecureContext && !this._qwacStatusPromise)` → `QWACs.determineQWACStatus()`
- 条件付き依存: `if (qwacStatusPromise == this._qwacStatusPromise && result)` → `this.refreshIdentityPopup()`
- 参照: `console.error`, `gBrowser.selectedBrowser.browsingContext`, `this._identityIconBox`, `this._identityPopup`, `this._isSecureContext`, `this._qwac`, `this._qwacStatusPromise`, `this._secInfo`, `this._uri`

## onPopupShown()
- 位置: L1331-1336
- 役割: ID ポップアップが表示されたら通知の抑止を開始し、フォーカス変化の監視を登録する。
- 触るとき: ポップアップ表示中に通知を出さない条件を変えるとき。
- 条件付き依存: `if (event.target == this._identityPopup)` → `PopupNotifications.suppressWhileOpen()`
- 条件付き依存: `if (event.target == this._identityPopup)` → `window.addEventListener()`
- 参照: `event.target`, `this._identityPopup`

## onPopupHidden()
- 位置: L1338-1342
- 役割: ID ポップアップが閉じたらフォーカス変化の監視を外す。
- 触るとき: ポップアップを閉じたあとのフォーカス監視の後始末を変えるとき。
- 条件付き依存: `if (event.target == this._identityPopup)` → `window.removeEventListener()`
- 参照: `event.target`, `this._identityPopup`

## handleEvent()
- 位置: L1344-1360
- 役割: フォーカスが移ってポップアップの祖先でも子孫でもない要素になったとき、noautohide でなければポップアップを閉じる。
- 触るとき: ポップアップが外側クリックやフォーカス移動で閉じる条件を変えるとき。
- 呼び出し先: `elem.compareDocumentPosition()`, `this._identityPopup.hasAttribute()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this._identityPopup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `this._identityPopup`

## observe()
- 位置: L1362-1377
- 役割: perm-changed の通知で、サイト権限の種類が UI に表示されるものなら、アイデンティティブロックを更新する。
- 触るとき: 権限変更がアイコンに反映されない問題を調べるとき。
- 呼び出し先: `SitePermissions.isSitePermission()`, `subject.QueryInterface()`
- 条件付き依存: `if (SitePermissions.isSitePermission(type))` → `this.refreshIdentityBlock()`
- 参照: `Ci.nsIPermission`
- XPCOM: [`nsIPermission`](../../../netwerk/base/nsIPermission.idl.md)

## onDragStart()
- 位置: L1379-1448
- 役割: URL バーのアイコンをドラッグしたとき、URL とタイトルとファビコン入りのドラッグ画像を作り、テキスト、URI リスト、HTML のデータを設定する。
- 触るとき: URL をドラッグしたときのデータ形式や見た目を変えるとき。
- 呼び出し先: `canvas.getContext()`, `ctx.drawImage()`, `ctx.fillRect()`, `ctx.fillText()`, `ctx.measureText()`, `document.createElementNS()`, `dt.setData()`, `dt.setDragImage()`, `gURLBar.getAttribute()`, `gURLBar.view.close()`, `parseInt()`
- 参照: `canvas.width`, `ctx.fillStyle`, `ctx.font`, `ctx.measureText(value).width`, `event.dataTransfer`, `gBrowser.contentTitle`, `gBrowser.currentURI.displaySpec`, `gBrowser.selectedTab.iconImage`, `image.src`, `image.width`, `tabIcon.src`, `window.devicePixelRatio`

## _updateAttribute()
- 位置: L1450-1456
- 役割: 値が真なら属性を設定し、偽なら属性を削除する小さな helper。
- 触るとき: ポップアップの属性の付け外しの扱いを変えるとき。
- 条件付き依存: `if (value)` → `elem.setAttribute()`
- 条件付き依存: `if (!(value))` → `elem.removeAttribute()`
