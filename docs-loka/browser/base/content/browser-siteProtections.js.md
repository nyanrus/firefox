# browser/base/content/browser-siteProtections.js

source: browser/base/content/browser-siteProtections.js
source-hash: db1d8e05d21269aaa84cb3e431d5998560595929
lines: 2948

## <module>
- 役割: 保護パネル(シールドアイコン)のカテゴリ群(トラッキング、Cookie、SNS、fingerprinting、マイニング)と gProtectionsHandler を定義する
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## ProtectionCategory.constructor()
- 位置: L49-99
- 役割: カテゴリ ID と pref、遮断・許可のフラグを受け取り、DOM 参照の遅延取得を用意する
- 触るとき: 保護カテゴリを新しく足すとき。pref が bool でなければ enabled は自動では監視されず、flags の既定値(shim、allow)の扱いを確かめる。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `MozXULElement.insertFTLIfNeeded()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getPrefType()`, `document.getElementById()`
- 条件付き依存: `if ( Services.prefs.getPrefType(this.prefEnabled) == Services.prefs.PREF_BOOL )` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if ( Services.prefs.getPrefType(this.prefEnabled) == Services.prefs.PREF_BOOL )` → `this.updateCategoryItem.bind()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `Services.prefs.PREF_BOOL`, `this._flags`, `this._id`, `this.prefEnabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.prefs`

## ProtectionCategory.init()
- 位置: L103-103
- 役割: 子クラスが初期化時に上書きするための空の既定実装
- 触るとき: カテゴリごとに pref 監視などを足すとき。gProtectionsHandler.init から呼ばれる。

## ProtectionCategory.uninit()
- 位置: L104-104
- 役割: 子クラスが後始末を上書きするための空の既定実装
- 触るとき: 監視を登録したカテゴリで解除漏れがないか確かめるとき。gProtectionsHandler.uninit から呼ばれる。

## ProtectionCategory.enabled()
- 位置: L107-109
- 役割: カテゴリの有効状態(_enabled、bool pref の値)を返す
- 触るとき: カテゴリの有効判定を子クラスで置き換えたいとき。Fingerprinting や ThirdPartyCookies が上書きしている。
- 参照: `this._enabled`

## ProtectionCategory.categoryItem()
- 位置: L118-127
- 役割: パネルのカテゴリボタン要素を遅延取得し、結果をキャッシュする
- 触るとき: カテゴリボタンの DOM id を変えるとき。popup 生成前に呼ぶと null になり得るため、呼び出し側でガードする(bug 1543537 のコメント参照)。
- 呼び出し先: `document.getElementById()`
- 参照: `this._categoryItem`, `this._id`

## ProtectionCategory.blockingEnabled()
- 位置: L134-136
- 役割: 既定では enabled と同じで、ブロック中かどうかの判定に使う
- 触るとき: ブロック中の見出し文言や blocked クラスの付与条件を変えるとき。SocialTracking が上書きしている。
- 参照: `this.enabled`

## ProtectionCategory.subViewTitleL10nId()
- 位置: L145-147
- 役割: blocking の真偽から、サブビューの見出し l10n ID を l10nKeys.title から選ぶ
- 触るとき: カテゴリの見出し文言を変えるとき。ThirdPartyCookies は挙動 pref ごとに別の ID を返すため上書きしている。
- 参照: `this.l10nKeys.title`

## ProtectionCategory.updateCategoryItem()
- 位置: L156-167
- 役割: パネル生成後にカテゴリボタンへ blocked と subviewbutton-nav を付け外しする
- 触るとき: カテゴリボタンの見た目が有効状態と合わないとき。popup 未生成なら false を返し、後で再度呼ばれる前提。
- 呼び出し先: `this.categoryItem.classList.toggle()`
- 参照: `gProtectionsHandler._protectionsPopup`, `this.enabled`

## ProtectionCategory.updateSubView()
- 位置: async L173-202
- 役割: 一覧を作り直し、cryptominers、fingerprinters、socialblock の見出し文言を設定する
- 触るとき: マイニング、fingerprinting、SNS のサブビューの文言や shim 許可ヒントを変えるとき。
- 呼び出し先: `this._generateSubViewListItems()`, `this.subViewList.append()`
- 条件付き依存: `if (l10nId)` → `document.l10n.setAttributes()`
- 参照: `gProtectionsHandler.hasException`, `this._id`, `this.blockingEnabled`, `this.subView`, `this.subViewList.textContent`, `this.subViewShimAllowHint.hidden`

## ProtectionCategory._generateSubViewListItems()
- 位置: async L213-232
- 役割: content blocking log を JSON で読み、各 origin の行を fragment にまとめる
- 触るとき: サブビューに載る一覧の元データを変えるとき。getBlockerCount もこれを使うので件数も変わる。
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `document.createDocumentFragment()`, `fragment.appendChild()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `this._createListItem()`

## ProtectionCategory.getBlockerCount()
- 位置: async L239-242
- 役割: 一覧の行数を返す(件数表示用)
- 触るとき: カテゴリごとの件数表示を変えるとき。
- 呼び出し先: `this._generateSubViewListItems()`
- 参照: `items?.childElementCount`

## ProtectionCategory._createListItem()
- 位置: L256-293
- 役割: origin 1件分の行を作る。検出されていなければ空を返し、許可なら allowed を付ける
- 触るとき: 一覧に出す条件(検出、許可、shim 許可)を変えるとき。TrackingProtection と ThirdPartyCookies は独自版を持つ。
- 呼び出し先: `actions.some()`, `document.createElementNS()`, `document.createXULElement()`, `label.setAttribute()`, `listItem.append()`, `listItem.classList.toggle()`, `this.isAllowing()`, `this.isBlocking()`, `this.isShimming()`
- 条件付き依存: `if (shimAllowed)` → `listItem.append()`
- 条件付き依存: `if (shimAllowed)` → `this._getShimAllowIndicator()`
- 参照: `label.className`, `label.tooltipText`, `label.value`, `listItem.className`, `this._flags.allow`

## ProtectionCategory._getShimAllowIndicator()
- 位置: L301-311
- 役割: shim で許可された項目に付けるアイコン要素を作る
- 触るとき: shim 許可の表示アイコンや、その説明文の l10n ID を変えるとき。
- 呼び出し先: `allowIndicator.classList.add()`, `document.createXULElement()`, `document.l10n.setAttributes()`

## ProtectionCategory.isBlocking()
- 位置: L317-319
- 役割: state のビットに block フラグが立っているかを返す
- 触るとき: 遮断とみなすフラグを変えるとき。カテゴリごとに上書きされることが多い。
- 参照: `this._flags.block`

## ProtectionCategory.isAllowing()
- 位置: L325-327
- 役割: state のビットに load フラグが立っているかを返す
- 触るとき: 読み込まれた(許可された)とみなすフラグを変えるとき。TrackingProtection は上書きしている。
- 参照: `this._flags.load`

## ProtectionCategory.isDetected()
- 位置: L334-336
- 役割: 遮断か許可のどちらかなら検出されたとみなす
- 触るとき: カテゴリを『検出なし』に分類する条件を変えるとき。ThirdPartyCookies は別の判定を持つ。
- 呼び出し先: `this.isAllowing()`, `this.isBlocking()`

## ProtectionCategory.isShimming()
- 位置: L343-345
- 役割: shim フラグが立ち、かつ許可されている状態かを返す
- 触るとき: shim による許可と通常の許可を区別する処理を変えるとき。_createListItem の allowed 判定で使う。
- 呼び出し先: `this.isAllowing()`
- 参照: `this._flags.shim`

## FingerprintingProtection.constructor()
- 位置: L361-382
- 役割: fingerprinting 用の 3 つの pref と、その有効値を保持する領域を初期化する
- 触るとき: fingerprinting 保護の pref を足したり参照先を変えたりするとき。
- 呼び出し先: `super()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_FINGERPRINTING_CONTENT`, `Ci.nsIWebProgressListener.STATE_BLOCKED_FINGERPRINTING_CONTENT`, `Ci.nsIWebProgressListener.STATE_LOADED_FINGERPRINTING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_FINGERPRINTING_CONTENT`, `this.enabledFPB`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## FingerprintingProtection.init()
- 位置: L384-393
- 役割: 有効値を読み直し、3 つの pref の監視を初回だけ登録する
- 触るとき: fingerprinting の pref 変更が反映されないとき、監視の登録漏れを調べる。
- 呼び出し先: `this.updateEnabled()`
- 条件付き依存: `if (!this.#isInitialized)` → `Services.prefs.addObserver()`
- 参照: `this.#isInitialized`, `this.prefEnabled`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## FingerprintingProtection.uninit()
- 位置: L395-405
- 役割: 初期化済みなら 3 つの pref の監視を解除する
- 触るとき: パネル破棄時に監視が残らないかを確かめるとき。
- 条件付き依存: `if (this.#isInitialized)` → `Services.prefs.removeObserver()`
- 参照: `this.#isInitialized`, `this.prefEnabled`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## FingerprintingProtection.updateEnabled()
- 位置: L407-413
- 役割: 3 つの pref を読み直し、有効フラグ群を更新する
- 触るとき: fingerprinting の有効判定に使う pref を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.enabledFPB`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.prefEnabled`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## FingerprintingProtection.observe()
- 位置: L415-418
- 役割: pref が変わったら有効フラグを読み直し、カテゴリボタンを更新する
- 触るとき: pref 変更後にボタンの見た目が古いままになるとき。
- 呼び出し先: `this.updateCategoryItem()`, `this.updateEnabled()`

## FingerprintingProtection.enabled()
- 位置: L420-426
- 役割: 通常の保護、FPP のグローバル、プライベートウィンドウでの FPP のいずれかが有効なら true
- 触るとき: fingerprinting カテゴリを有効と見なす条件を変えるとき。
- 参照: `this.enabledFPB`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.isWindowPrivate`

## FingerprintingProtection.isBlocking()
- 位置: L428-442
- 役割: FPP が有効な文脈では疑わしい fingerprinting のフラグも遮断に含めて判定する
- 触るとき: 疑わしい fingerprinting を遮断扱いにするかを変えるとき。末尾の TODO(bug 1864914)も関係する。
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_SUSPICIOUS_FINGERPRINTING`, `this._flags.block`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.isWindowPrivate`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.constructor()
- 位置: L482-532
- 役割: ETP の通常、プライベート、メール追跡の pref と、ブロックリストの pref を保持する
- 触るとき: トラッキング保護の pref やリストの参照先を足すとき。load は null で、許可判定は独自に持つ。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_EMAILTRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_BLOCKED_TRACKING_CONTENT`, `this.emailTrackingProtectionEnabledGlobally`, `this.emailTrackingProtectionEnabledInPrivateWindows`, `this.enabledGlobally`, `this.enabledInPrivateWindows`, `this.prefAnnotationsLevel2Enabled`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabledInPrivateWindows`, `this.prefTrackingAnnotationTable`, `this.prefTrackingTable`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.init()
- 位置: L534-550
- 役割: 有効値を読み直し、4 つの pref の監視を初回だけ登録する
- 触るとき: ETP の切り替えが反映されないとき、監視の登録漏れを調べる。
- 呼び出し先: `this.updateEnabled()`
- 条件付き依存: `if (!this.#isInitialized)` → `Services.prefs.addObserver()`
- 参照: `this.#isInitialized`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabled`, `this.prefEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## TrackingProtection.uninit()
- 位置: L552-566
- 役割: 初期化済みなら 4 つの pref の監視を解除する
- 触るとき: パネル破棄時に監視が残らないかを確かめるとき。
- 条件付き依存: `if (this.#isInitialized)` → `Services.prefs.removeObserver()`
- 参照: `this.#isInitialized`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabled`, `this.prefEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## TrackingProtection.observe()
- 位置: L568-571
- 役割: pref 変更時に有効フラグを読み直し、カテゴリボタンを更新する
- 触るとき: ETP のオンオフ後にボタン表示がずれるとき。
- 呼び出し先: `this.updateCategoryItem()`, `this.updateEnabled()`

## TrackingProtection.trackingProtectionLevel2Enabled()
- 位置: L573-576
- 役割: トラッキングのブロックリストに content-track-digest256 が含まれるかを返す
- 触るとき: 厳格リスト(Level 2)が有効かを判定する条件を変えるとき。_createListItem の注釈専用項目の除外で使う。
- 呼び出し先: `this.trackingTable.includes()`

## TrackingProtection.enabled()
- 位置: L578-586
- 役割: 通常、メール追跡、プライベートウィンドウのいずれかで有効なら true
- 触るとき: トラッキング保護を有効と見なす条件を変えるとき。
- 参照: `this.emailTrackingProtectionEnabledGlobally`, `this.emailTrackingProtectionEnabledInPrivateWindows`, `this.enabledGlobally`, `this.enabledInPrivateWindows`, `this.isWindowPrivate`

## TrackingProtection.updateEnabled()
- 位置: L588-600
- 役割: 通常、プライベート、メール追跡の 4 つの pref を読み直す
- 触るとき: トラッキング保護の有効判定に使う pref を増やすとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.emailTrackingProtectionEnabledGlobally`, `this.emailTrackingProtectionEnabledInPrivateWindows`, `this.enabledGlobally`, `this.enabledInPrivateWindows`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabled`, `this.prefEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## TrackingProtection.isAllowingLevel1()
- 位置: L602-608
- 役割: STATE_LOADED_LEVEL_1 のビットが立っているかを返す
- 触るとき: Level 1 の許可判定を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_LEVEL_1_TRACKING_CONTENT`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.isAllowingLevel2()
- 位置: L610-616
- 役割: STATE_LOADED_LEVEL_2 のビットが立っているかを返す
- 触るとき: Level 2 の許可判定を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_LEVEL_2_TRACKING_CONTENT`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.isAllowing()
- 位置: L618-620
- 役割: Level 1 か Level 2 のどちらかで許可とみなす
- 触るとき: トラッキングの許可判定の基準を変えるとき。
- 呼び出し先: `this.isAllowingLevel1()`, `this.isAllowingLevel2()`

## TrackingProtection.updateSubView()
- 位置: async L622-669
- 役割: 一覧を作り、空なら空表示を入れる。ページが変わっていなければ一覧と見出しを反映する
- 触るとき: トラッキング一覧の空表示や、読み込み途中でページが変わった時の古い結果の扱いを変えるとき。
- 呼び出し先: `this._generateSubViewListItems()`
- 条件付き依存: `if (!items.childNodes.length)` → `document.createXULElement()`
- 条件付き依存: `if (!items.childNodes.length)` → `emptyImage.classList.add()`
- 条件付き依存: `if (!items.childNodes.length)` → `emptyLabel.classList.add()`
- 条件付き依存: `if (!items.childNodes.length)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!items.childNodes.length)` → `items.appendChild()`
- 条件付き依存: `if (!items.childNodes.length)` → `this.subViewList.classList.add()`
- 条件付き依存: `if (!(!items.childNodes.length))` → `this.subViewList.classList.remove()`
- 条件付き依存: `if ( previousURI == gBrowser.currentURI.spec && previousWindow == gBrowser.selectedBrowser.innerWindowID )` → `this.subViewList.append()`
- 条件付き依存: `if ( previousURI == gBrowser.currentURI.spec && previousWindow == gBrowser.selectedBrowser.innerWindowID )` → `document.l10n.setAttributes()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.innerWindowID`, `gProtectionsHandler.hasException`, `items.childNodes.length`, `this.enabled`, `this.subView`, `this.subViewList.textContent`, `this.subViewShimAllowHint.hidden`

## TrackingProtection._createListItem()
- 位置: async L671-722
- 役割: 検出された origin の行を作る。厳格リスト用の注釈だけの項目は除外する
- 触るとき: 厳格リストで注釈だけされた項目を一覧に出すかどうかを変えるとき。
- 呼び出し先: `actions.some()`, `document.createElementNS()`, `document.createXULElement()`, `label.setAttribute()`, `listItem.append()`, `listItem.classList.toggle()`, `this.isAllowing()`, `this.isBlocking()`, `this.isShimming()`
- 条件付き依存: `if (shimAllowed)` → `listItem.append()`
- 条件付き依存: `if (shimAllowed)` → `this._getShimAllowIndicator()`
- 参照: `Ci.nsIWebProgressListener .STATE_LOADED_LEVEL_2_TRACKING_CONTENT`, `label.className`, `label.tooltipText`, `label.value`, `listItem.className`, `this._flags.allow`, `this.annotationsLevel2Enabled`, `this.trackingProtectionLevel2Enabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## ThirdPartyCookies.constructor()
- 位置: L737-775
- 役割: cookieBehavior の pref を対象にし、フラグ処理を使わないカテゴリとして作る
- 触るとき: Cookie の挙動値の扱いや、表示用の値の一覧を変えるとき。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `document.getElementById()`, `super()`, `this.updateCategoryItem.bind()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.prefEnabled`, `this.prefEnabledValues`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.isBlocking()
- 位置: L777-793
- 役割: cookie の遮断系フラグ(トラッカー、SNS、全面、権限、外部、パーティション)のどれかが立っているかを返す
- 触るとき: どの cookie 遮断状態を『遮断中』に数えるかを変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_ALL`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_BY_PERMISSION`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_FOREIGN`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_SOCIALTRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_TRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_PARTITIONED_TRACKER`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## ThirdPartyCookies.isDetected()
- 位置: L795-820
- 役割: 挙動 pref に応じて読み込まれた cookie のフラグを検出とみなす
- 触るとき: cookie の検出条件を変えるとき。SNS の有効状態も検出判定に入る。
- 呼び出し先: `this.isBlocking()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED`, `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED_SOCIALTRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED_TRACKER`, `SocialTracking.enabled`, `this.behaviorPref`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## ThirdPartyCookies.updateCategoryItem()
- 位置: L822-855
- 役割: 親の処理の後、挙動 pref に応じた cookie カテゴリのラベルを設定する
- 触るとき: cookie カテゴリのラベル文言を変えるとき。未知の挙動値のときはラベルを空にする。
- 呼び出し先: `document.l10n.setAttributes()`, `super.updateCategoryItem()`
- 条件付き依存: `if (!(!this.enabled))` → `console.error()`
- 条件付き依存: `if (!(!this.enabled))` → `this.categoryLabel.removeAttribute()`
- 参照: `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.behaviorPref`, `this.categoryLabel`, `this.categoryLabel.textContent`, `this.enabled`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.enabled()
- 位置: L857-859
- 役割: cookieBehavior が有効値一覧に含まれるかを返す
- 触るとき: cookie 保護を有効と見なす挙動値を変えるとき。
- 呼び出し先: `this.prefEnabledValues.includes()`
- 参照: `this.behaviorPref`

## ThirdPartyCookies._generateSubViewListItems()
- 位置: L861-887
- 役割: log を分類し、挙動に応じて対象カテゴリの行を fragment にまとめる(同期)
- 触るとき: cookie 一覧に載るカテゴリ(初回パーティを含めるか等)を変えるとき。
- 呼び出し先: `JSON.parse()`, `categoryNames.push()`, `document.createDocumentFragment()`, `fragment.appendChild()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `this._createListItem()`, `this._processContentBlockingLog()`
- 参照: `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `itemsToShow.length`, `this.behaviorPref`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.updateSubView()
- 位置: L889-977
- 役割: カテゴリごとに見出し付きの箱を作り、挙動に応じて見出しを隠してタイトルを設定する
- 触るとき: cookie サブビューの構成や見出しの出し分けを変えるとき。
- 呼び出し先: `JSON.parse()`, `box.appendChild()`, `categoryNames.push()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `this._createListItem()`, `this._processContentBlockingLog()`, `this.subViewList.appendChild()`, `this.subViewTitleL10nId()`
- 条件付き依存: `if (l10nId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!this.enabled)` → `document.l10n.setAttributes()`
- 参照: `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `box.className`, `gProtectionsHandler.hasException`, `itemsToShow.length`, `label.className`, `this.behaviorPref`, `this.enabled`, `this.subView`, `this.subViewHeading.hidden`, `this.subViewHeading.nextSibling.hidden`, `this.subViewHeading.nextSibling.nodeName`, `this.subViewList.textContent`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.subViewTitleL10nId()
- 位置: L987-1011
- 役割: 挙動 pref と遮断の真偽から見出し ID を選ぶ。未知の値は null を返す
- 触るとき: 挙動ごとの cookie 見出し文言を変えるとき。
- 呼び出し先: `console.error()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.behaviorPref`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies._getExceptionState()
- 位置: L1013-1028
- 役割: 3rdPartyStorage の origin 権限を先に調べ、無ければ cookie の権限を返す
- 触るとき: cookie の例外(許可か拒否か)の判定元を変えるとき。cookie 例外は親ドメインから継承されるため、親を含めて判定する。
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 参照: `Services.perms.UNKNOWN_ACTION`, `gBrowser.contentPrincipal`
- XPCOM: `Services.perms` / `Services.scriptSecurityManager`

## ThirdPartyCookies._clearException()
- 位置: L1030-1052
- 役割: origin の 3rdPartyStorage 権限を消し、親ドメインの cookie 権限も消す
- 触るとき: 例外解除ボタンで消える権限の範囲を変えるとき。
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `Services.perms.getAllForPrincipal()`
- 条件付き依存: `if (perm.type == "3rdPartyStorage^" + origin)` → `Services.perms.removePermission()`
- 条件付き依存: `if ( perm.type == "cookie" && Services.eTLD.hasRootDomain(host, perm.principal.host) )` → `Services.perms.removePermission()`
- 参照: `Services.io.newURI(origin).host`, `Services.perms.all`, `gBrowser.contentPrincipal`, `perm.principal.host`, `perm.type`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.perms`

## ThirdPartyCookies._processContentBlockingLog()
- 位置: L1056-1136
- 役割: http の origin を初回パーティ、トラッカー、外部に振り分け、許可と遮断の状態を付ける
- 触るとき: cookie 一覧の分類ルールを変えるとき。基底ドメイン取得で IP やサフィックスのエラーだけは握りつぶし、それ以外は投げ直す。
- 呼び出し先: `Object.entries()`, `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `TrackingProtection.isAllowing()`, `origin.startsWith()`, `this._getExceptionState()`, `this.isBlocking()`, `this.isDetected()`
- 条件付き依存: `if (isFirstParty)` → `newLog.firstParty.push()`
- 条件付き依存: `if (isTracker)` → `newLog.trackers.push()`
- 条件付き依存: `if (!(isTracker))` → `newLog.thirdParty.push()`
- 参照: `Cr.NS_ERROR_HOST_IS_IP_ADDRESS`, `Cr.NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS`, `e.result`, `gBrowser.currentURI`, `info.isAllowed`
- XPCOM: `Services.eTLD` / `Services.io`

## ThirdPartyCookies._createListItem()
- 位置: L1138-1193
- 役割: 例外状態と一致する行にだけ、状態ラベルと解除ボタンを付けて返す
- 触るとき: cookie の例外表示や解除ボタンの挙動を変えるとき。解除時は _clearException の後、ボタンと許可表示を外す。
- 呼び出し先: `document.createElementNS()`, `document.createXULElement()`, `label.setAttribute()`, `listItem.append()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `listItem.classList.add()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `document.createXULElement()`
- 条件付き依存: `if (isAllowed)` → `listItem.classList.toggle()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `removeException.appendChild()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `removeException.addEventListener()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `this._clearException()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `removeException.remove()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `listItem.classList.toggle()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `listItem.append()`
- 参照: `Services.perms.ALLOW_ACTION`, `Services.perms.DENY_ACTION`, `label.className`, `label.value`, `listItem.className`, `listItem.tooltipText`, `removeException.className`, `stateLabel.className`
- XPCOM: `Services.perms`

## SocialTrackingProtection.constructor()
- 位置: L1208-1244
- 役割: SNS 追跡保護と cookie 挙動の pref を監視し、有効判定に使う値を用意する
- 触るとき: SNS 追跡保護の設定の参照元を変えるとき。cookie 挙動は拒否するかどうかの bool に変換して保持する。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `[ Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER, Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN, ].includes()`, `super()`, `this.updateCategoryItem.bind()`
- 参照: `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `Ci.nsIWebProgressListener.STATE_BLOCKED_SOCIALTRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_LOADED_SOCIALTRACKING_CONTENT`, `this.prefCookieBehavior`, `this.prefEnabled`, `this.prefSTPCookieEnabled`, `this.prefStpTpEnabled`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## SocialTrackingProtection.blockingEnabled()
- 位置: L1246-1251
- 役割: SNS 保護か cookie 拒否のどちらかが有効で、かつ enabled なら true
- 触るとき: SNS カテゴリを『遮断中』と表示する条件を変えるとき。
- 参照: `this.enabled`, `this.rejectTrackingCookies`, `this.socialTrackingProtectionEnabled`

## SocialTrackingProtection.isBlockingCookies()
- 位置: L1253-1259
- 役割: SNS トラッカーの cookie 遮断フラグが立っているかを返す
- 触るとき: SNS の cookie 遮断を判定するビットを変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_SOCIALTRACKER`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## SocialTrackingProtection.isBlocking()
- 位置: L1261-1263
- 役割: 親の遮断判定か cookie 遮断のどちらかなら遮断とみなす
- 触るとき: SNS の遮断判定に cookie を含めるかを変えるとき。
- 呼び出し先: `super.isBlocking()`, `this.isBlockingCookies()`

## SocialTrackingProtection.isAllowing()
- 位置: L1265-1275
- 役割: SNS 保護が有効なら親の許可判定、無効なら SNS の cookie 読み込みフラグを見る
- 触るとき: SNS の許可判定が保護の有効状態でどう変わるかを確かめるとき。
- 条件付き依存: `if (this.socialTrackingProtectionEnabled)` → `super.isAllowing()`
- 参照: `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED_SOCIALTRACKER`, `this.socialTrackingProtectionEnabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## SocialTrackingProtection.updateCategoryItem()
- 位置: L1277-1291
- 役割: パネル生成後、有効なら uidisabled を外し、遮断中なら blocked を付ける
- 触るとき: SNS カテゴリボタンの無効化や遮断表示を変えるとき。親の updateCategoryItem は呼ばない。
- 呼び出し先: `this.categoryItem.classList.toggle()`
- 条件付き依存: `if (this.enabled)` → `this.categoryItem.removeAttribute()`
- 条件付き依存: `if (!(this.enabled))` → `this.categoryItem.setAttribute()`
- 参照: `gProtectionsHandler._protectionsPopup`, `this.blockingEnabled`, `this.enabled`

## _initializePopup()
- 位置: L1347-1387
- 役割: パネルの template を初回だけ取り出し、イベントを張り、件数の説明クリックを接続する
- 触るとき: パネルの初期化順序や、ツールチップの接続先を変えるとき。popupshown と popuphidden は二度登録されている(要確認: 意図した重複か)。
- 条件付き依存: `if (!this._protectionsPopup)` → `document.getElementById()`
- 条件付き依存: `if (!this._protectionsPopup)` → `this._protectionsPopup.addEventListener()`
- 条件付き依存: `if (!this._protectionsPopup)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this._protectionsPopup)` → `this.maybeSetMilestoneCounterText()`
- 条件付き依存: `if (!this._protectionsPopup)` → `Object.values()`
- 条件付き依存: `if (!this._protectionsPopup)` → `blocker.updateCategoryItem()`
- 条件付き依存: `if (!this._protectionsPopup)` → `notBlockingWhy.addEventListener()`
- 条件付き依存: `if (!this._protectionsPopup)` → `document .getElementById( "protections-popup-trackers-blocked-counter-description" ) .addEventListener()`
- 条件付き依存: `if (!this._protectionsPopup)` → `document .getElementById()`
- 条件付き依存: `if (!this._protectionsPopup)` → `gProtectionsHandler.openProtections()`
- 参照: `this._protectionsPopup`, `this.blockers`, `wrapper.content`, `wrapper.content.firstElementChild`

## openTooltip()
- 位置: L1365-1367
- 役割: not-blocking の理由ツールチップを開く
- 触るとき: 理由ツールチップを開く契機(マウスオーバー、フォーカス)を変えるとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById(event.target.tooltip).openPopup()`
- 参照: `event.target`, `event.target.tooltip`

## closeTooltip()
- 位置: L1368-1370
- 役割: not-blocking の理由ツールチップを閉じる
- 触るとき: 理由ツールチップを閉じる契機(マウスアウト、ブラー)を変えるとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById(event.target.tooltip).hidePopup()`
- 参照: `event.target.tooltip`

## _hidePopup()
- 位置: L1389-1393
- 役割: パネルが作られていれば閉じる
- 触るとき: パネルを外部から閉じる経路を足すとき。
- 条件付き依存: `if (this._protectionsPopup)` → `PanelMultiView.hidePopup()`
- 参照: `this._protectionsPopup`

## iconBox()
- 位置: L1396-1401
- 役割: tracking-protection-icon-box 要素を取得し、以後はキャッシュする
- 触るとき: シールドアイコンの属性(active、hasException)を付ける場所を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.iconBox`

## _protectionsPopupMultiView()
- 位置: L1402-1407
- 役割: パネル内の multiView 要素を取得する
- 触るとき: サブビューへの切り替え(showSubView)の対象を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMultiView`

## _protectionsPopupMainView()
- 位置: L1408-1413
- 役割: パネルのメインビュー要素を取得する
- 触るとき: メインビューの構成を変えるとき。本体の他の箇所からは参照がない(要確認: テストでのみ使うか)。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMainView`

## _protectionsPopupMainViewHeaderLabel()
- 位置: L1414-1419
- 役割: パネルヘッダーのラベル要素を取得する
- 触るとき: ヘッダー文言(ホスト名入り)を変えるとき。refreshProtectionsPopup が文言 ID を設定する。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMainViewHeaderLabel`

## _protectionsPopupTPSwitch()
- 位置: L1420-1425
- 役割: ETP のスイッチ要素を取得する
- 触るとき: ETP トグルの見た目や toggle イベントの接続先を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupTPSwitch`

## _protectionsPopupCategoryList()
- 位置: L1426-1431
- 役割: カテゴリボタンを並べるリスト要素を取得する
- 触るとき: カテゴリの並び替えの挿入先を変えるとき。reorderCategoryItems が使う。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupCategoryList`

## _protectionsPopupBlockingHeader()
- 位置: L1432-1437
- 役割: 『遮断中』見出しの要素を取得する
- 触るとき: 遮断中見出しの出し分けを変えるとき。reorderCategoryItems が表示を切り替える。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupBlockingHeader`

## _protectionsPopupNotBlockingHeader()
- 位置: L1438-1443
- 役割: 『許可中』見出しの要素を取得する
- 触るとき: 許可中見出しの出し分けを変えるとき。reorderCategoryItems が表示を切り替える。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupNotBlockingHeader`

## _protectionsPopupNotFoundHeader()
- 位置: L1444-1449
- 役割: 『検出なし』見出しの要素を取得する
- 触るとき: 検出なしの見出しや、その下に並ぶカテゴリの扱いを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupNotFoundHeader`

## _protectionsPopupSmartblockContainer()
- 位置: L1450-1455
- 役割: SmartBlock の埋め込み枠の要素を取得する
- 触るとき: SmartBlock の枠を出す条件を変えるとき。reorderCategoryItems と _addSmartblockEmbedToggles が表示を切り替える。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSmartblockContainer`

## _protectionsPopupSmartblockDescription()
- 位置: L1456-1460
- 役割: SmartBlock の説明文の要素を取得する
- 触るとき: SmartBlock の説明文を差し替えるとき。本ファイル内で参照されていない(要確認: 削除してよいか)。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSmartblockDescription`

## _protectionsPopupSmartblockToggleContainer()
- 位置: L1461-1465
- 役割: SmartBlock のトグルを入れる箱の要素を取得する
- 触るとき: SmartBlock のトグルの追加先や中身の作り直しを変えるとき。_addSmartblockEmbedToggles が中身を入れ替える。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSmartblockToggleContainer`

## _protectionsPopupSettingsButton()
- 位置: L1466-1471
- 役割: パネルの設定ボタン要素を取得する
- 触るとき: 設定ボタンの導線を変えるとき。本ファイル内では参照がなく、onCommand は ID で分岐している(要確認)。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSettingsButton`

## _protectionsPopupFooter()
- 位置: L1472-1477
- 役割: パネルのフッター要素を取得する
- 触るとき: フッターの表示を変えるとき。本ファイル内では参照がない(要確認)。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupFooter`

## _protectionsPopupTrackersCounterBox()
- 位置: L1478-1483
- 役割: ブロック件数の箱の要素を取得する
- 触るとき: 件数を出す条件(0件で隠す)を変えるとき。setTrackersBlockedCounter が showing 属性を付ける。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupTrackersCounterBox`

## _protectionsPopupTrackersCounterDescription()
- 位置: L1484-1490
- 役割: ブロック件数の説明文の要素を取得する
- 触るとき: 件数の説明文や、最初の記録日のツールチップを変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupTrackersCounterDescription`

## _protectionsPopupFooterProtectionTypeLabel()
- 位置: L1491-1497
- 役割: フッターの保護種別ラベルの要素を取得する
- 触るとき: 標準、厳格、カスタムの表示を変えるとき。getTrackingProtectionLabel の結果を入れる。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupFooterProtectionTypeLabel`

## _trackingProtectionIconTooltipLabel()
- 位置: L1498-1503
- 役割: シールドアイコンのツールチップ文言の要素を取得する
- 触るとき: ツールチップ文言(無効、有効、検出なし)を変えるとき。showXxxTooltipForTPIcon が設定する。
- 呼び出し先: `document.getElementById()`
- 参照: `this._trackingProtectionIconTooltipLabel`

## _trackingProtectionIconContainer()
- 位置: L1504-1509
- 役割: シールドアイコンのコンテナ要素を取得する
- 触るとき: アイコンの開閉状態(open 属性)や説明の l10n を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._trackingProtectionIconContainer`

## noTrackersDetectedDescription()
- 位置: L1511-1516
- 役割: 検出がなかったときの説明要素を取得する
- 触るとき: 検出なし時の説明の表示条件を変えるとき。updatePanelForBlockingEvent が hidden を切り替える。
- 呼び出し先: `document.getElementById()`
- 参照: `this.noTrackersDetectedDescription`

## _protectionsPopupMilestonesText()
- 位置: L1518-1523
- 役割: マイルストーン文言の要素を取得する
- 触るとき: マイルストーン表示の文言を変えるとき。maybeSetMilestoneCounterText が設定する。
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMilestonesText`

## _notBlockingWhyLink()
- 位置: L1525-1530
- 役割: 『なぜ遮断しないか』のリンク要素を取得する
- 触るとき: 理由ツールチップの割り当てを変えるとき。refreshProtectionsPopup が tooltip 属性を付ける。
- 呼び出し先: `document.getElementById()`
- 参照: `this._notBlockingWhyLink`

## init()
- 位置: L1551-1636
- 役割: パネル用の pref を lazy getter として登録し、各カテゴリの init と履歴消去、SmartBlock の通知の購読を行う
- 触るとき: 起動時に読む pref を足すとき。pref の変更時にマイルストーン表示を更新するコールバックもここで決まる。
- 呼び出し先: `JSON.parse()`, `Object.values()`, `Services.obs.addObserver()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `parseInt()`, `this._resetToggleSecDelay.bind()`, `this.maybeSetMilestoneCounterText()`
- 条件付き依存: `if (blocker.init)` → `blocker.init()`
- 参照: `blocker.init`, `this._resetToggleSecDelay`, `this.blockers`
- XPCOM: `Services.obs`

## uninit()
- 位置: L1638-1647
- 役割: 各カテゴリの uninit を呼び、履歴消去と SmartBlock の通知の購読を解除する
- 触るとき: パネル破棄時の後始末に漏れがないかを確かめるとき。
- 呼び出し先: `Object.values()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (blocker.uninit)` → `blocker.uninit()`
- 参照: `blocker.uninit`, `this.blockers`
- XPCOM: `Services.obs`

## getTrackingProtectionLabel()
- 位置: L1649-1662
- 役割: category pref の値(strict、custom、その他は standard)から保護種別の l10n ID を返す
- 触るとき: フッターに出す保護種別の表示や、category pref の値域を変えるとき。
- 呼び出し先: `Services.prefs.getStringPref()`
- 参照: `this.PREF_CB_CATEGORY`
- XPCOM: `Services.prefs`

## openPreferences()
- 位置: L1664-1666
- 役割: プライバシー設定のトラッキング保護ページを開く
- 触るとき: 設定ボタンや各サブビューの設定導線の遷移先を変えるとき。
- 呼び出し先: `openPreferences()`

## openProtections()
- 位置: L1668-1679
- 役割: about:protections を開き、マイルストーン表示用の pref を消す
- 触るとき: レポート画面への導線や、マイルストーン表示を既読にする条件を変えるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `switchToTabHavingURI()`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## showTrackersSubview()
- 位置: async L1681-1686
- 役割: トラッキングのサブビューを最新化してから表示する
- 触るとき: トラッキングのカテゴリボタンから一覧を開く流れを変えるとき。
- 呼び出し先: `TrackingProtection.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showSocialblockerSubview()
- 位置: async L1688-1693
- 役割: SNS 追跡のサブビューを最新化してから表示する
- 触るとき: SNS カテゴリのボタンから一覧を開く流れを変えるとき。
- 呼び出し先: `SocialTracking.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showCookiesSubview()
- 位置: async L1695-1700
- 役割: cookie のサブビューを最新化してから表示する
- 触るとき: cookie カテゴリのボタンから一覧を開く流れを変えるとき。
- 呼び出し先: `ThirdPartyCookies.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showFingerprintersSubview()
- 位置: async L1702-1707
- 役割: fingerprinting のサブビューを最新化してから表示する
- 触るとき: fingerprinting カテゴリのボタンから一覧を開く流れを変えるとき。
- 呼び出し先: `Fingerprinting.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showCryptominersSubview()
- 位置: async L1709-1714
- 役割: マイニングのサブビューを最新化してから表示する
- 触るとき: マイニングのカテゴリボタンから一覧を開く流れを変えるとき。
- 呼び出し先: `Cryptomining.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## shieldHistogramAdd()
- 位置: L1716-1723
- 役割: シールド関連の値を、プライベートウィンドウでなければ Glean に記録する
- 触るとき: シールドの計測値や記録条件を変えるとき。
- 呼び出し先: `Glean.contentblocking.trackingProtectionShield.accumulateSingleSample()`, `PrivateBrowsingUtils.isWindowPrivate()`

## cryptominersHistogramAdd()
- 位置: L1725-1727
- 役割: マイニングの遮断や許可の件数を Glean に 1 加算する
- 触るとき: マイニングの計測項目を増やすとき。
- 呼び出し先: `Glean.contentblocking.cryptominersBlockedCount[value].add()`
- 参照: `Glean.contentblocking.cryptominersBlockedCount`

## fingerprintersHistogramAdd()
- 位置: L1729-1731
- 役割: fingerprinting の遮断や許可の件数を Glean に 1 加算する
- 触るとき: fingerprinting の計測項目を増やすとき。
- 呼び出し先: `Glean.contentblocking.fingerprintersBlockedCount[value].add()`
- 参照: `Glean.contentblocking.fingerprintersBlockedCount`

## handleProtectionsButtonEvent()
- 位置: L1733-1745
- 役割: シールドボタンのクリック、Enter、Space を受けてパネルを shieldButtonClicked で開く
- 触るとき: シールドボタンの操作条件を変えるとき。左クリック以外は無視する。
- 呼び出し先: `event.stopPropagation()`, `this.showProtectionsPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## onPopupShown()
- 位置: L1747-1785
- 役割: パネル表示時に、フォーカス監視、情報メッセージ、テレメトリ、アイコンの open 属性、SmartBlock 経由の操作遅延、ReportBrokenSite の更新を行う
- 触るとき: パネルが開いた時に必要な処理を足すとき。トースト表示ではテレメトリを送らない。
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `PopupNotifications.suppressWhileOpen()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `window.addEventListener()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._protectionsPopupTPSwitch.addEventListener()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._insertProtectionsPanelInfoMessage()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `event.target.hasAttribute()`
- 条件付き依存: `if (!event.target.hasAttribute("toast"))` → `Glean.securityUiProtectionspopup.openProtectionsPopup.record()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._trackingProtectionIconContainer.setAttribute()`
- 条件付き依存: `if (this._protectionsPopupOpeningReason == "embedPlaceholderButton")` → `this._disablePopupToggles()`
- 条件付き依存: `if (this._protectionsPopupOpeningReason == "embedPlaceholderButton")` → `setTimeout()`
- 条件付き依存: `if (this._protectionsPopupOpeningReason == "embedPlaceholderButton")` → `this._enablePopupToggles()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `ReportBrokenSite.updateParentMenu()`
- 参照: `event.target`, `this._protectionsPopup`, `this._protectionsPopupButtonDelay`, `this._protectionsPopupOpeningReason`, `this._protectionsPopupSmartblockContainer.hidden`, `this._protectionsPopupToggleDelayTimer`

## onPopupHidden()
- 位置: L1787-1800
- 役割: パネル非表示時に、フォーカス監視、トグルの遅延タイマー、開いた理由を後始末する
- 触るとき: パネルを閉じた後に状態が残る不具合を調べるとき。
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `window.removeEventListener()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._protectionsPopupTPSwitch.removeEventListener()`
- 条件付き依存: `if (this._protectionsPopupToggleDelayTimer)` → `clearTimeout()`
- 条件付き依存: `if (this._protectionsPopupToggleDelayTimer)` → `this._enablePopupToggles()`
- 参照: `event.target`, `this._protectionsPopup`, `this._protectionsPopupOpeningReason`, `this._protectionsPopupToggleDelayTimer`

## onTrackingProtectionIconHoveredOrFocused()
- 位置: async L1802-1827
- 役割: シールドのホバーやフォーカスで、件数、保護種別、最初の記録日を先読みしてフッターを更新する
- 触るとき: フッターのデータを取得するタイミングを変えるとき。_updatingFooter で多重実行を防いでいる。
- 呼び出し先: `TrackingDBService.sumAllEvents()`, `document.l10n.setAttributes()`, `this._initializePopup()`, `this.getTrackingProtectionLabel()`, `this.maybeUpdateEarliestRecordedDateTooltip()`, `this.setTrackersBlockedCounter()`
- 参照: `this._protectionsPopupFooterProtectionTypeLabel`, `this._updatingFooter`

## onLocationChange()
- 位置: L1830-1872
- 役割: 遷移時に、同じページならトーストを出し、シールドの状態と例外を更新し、対象外ページではアイコンを隠す
- 触るとき: ページ遷移時のアイコンの表示やトーストの出し方を変えるとき。読み込み時の計測もここで送る。
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`, `this.cryptominersHistogramAdd()`, `this.fingerprintersHistogramAdd()`, `this.iconBox.toggleAttribute()`, `this.shieldHistogramAdd()`
- 条件付き依存: `if ( this._previousURI == gBrowser.currentURI.spec && this._previousOuterWindowID == gBrowser.selectedBrowser.outerWindowID )` → `this.showProtectionsPopup()`
- 条件付き依存: `if (this._protectionsPopup)` → `this._protectionsPopup.toggleAttribute()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser`, `gBrowser.selectedBrowser.outerWindowID`, `this._previousOuterWindowID`, `this._previousURI`, `this._protectionsPopup`, `this._showToastAfterRefresh`, `this._trackingProtectionIconContainer.hidden`, `this.hadShieldState`, `this.hasException`

## notifyContentBlockingEvent()
- 位置: L1874-1896
- 役割: 読み込み完了後で検出があれば、ブロックイベントを observer へ通知する
- 触るとき: ContentBlocking イベントを受け取る側(CFR など)への通知条件を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.currentURI`, `gBrowser.selectedBrowser`, `this._isStoppedState`, `this.anyDetected`, `uri.asciiHost`, `uri.host`, `uri.spec`
- XPCOM: `Services.obs`

## onStateChange()
- 位置: L1898-1909
- 役割: トップレベルの読み込み状態が変わるたびに、完了フラグを更新してイベントを通知する
- 触るとき: 読み込み完了の判定や、通知を送るタイミングを変えるとき。
- 呼び出し先: `gBrowser.selectedBrowser.getContentBlockingEvents()`, `this.notifyContentBlockingEvent()`
- 参照: `Ci.nsIWebProgressListener.STATE_STOP`, `aWebProgress.isTopLevel`, `this._isStoppedState`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## updatePanelForBlockingEvent()
- 位置: L1915-1942
- 役割: 開いているパネルのカテゴリ状態と属性を更新し、検出があれば並べ替える
- 触るとき: パネルを開いたまま新しいブロックイベントが届いたときの表示を変えるとき。uidisabled のカテゴリは飛ばす。
- 呼び出し先: `Object.values()`, `blocker.categoryItem.classList.toggle()`, `blocker.categoryItem.hasAttribute()`, `blocker.isDetected()`, `this._protectionsPopup.toggleAttribute()`
- 条件付き依存: `if (this.anyDetected)` → `this.reorderCategoryItems()`
- 参照: `this.anyBlocking`, `this.anyDetected`, `this.blockers`, `this.hasException`, `this.noTrackersDetectedDescription.hidden`

## reportBlockingEventTelemetry()
- 位置: L1944-1983
- 役割: シールドの初回状態と、fingerprinting、マイニングの遮断や許可の変化を 1 ページ 1 回として計測する
- 触るとき: 計測の条件を変えるとき。シミュレーションのイベントではシールドの計測を省く。
- 呼び出し先: `Cryptomining.isAllowing()`, `Cryptomining.isBlocking()`, `Fingerprinting.isAllowing()`, `Fingerprinting.isBlocking()`
- 条件付き依存: `if (this.hasException && !this.hadShieldState)` → `this.shieldHistogramAdd()`
- 条件付き依存: `if ( !this.hasException && this.anyBlocking && !this.hadShieldState )` → `this.shieldHistogramAdd()`
- 条件付き依存: `if (fingerprintingBlocking)` → `this.fingerprintersHistogramAdd()`
- 条件付き依存: `if (fingerprintingAllowing)` → `this.fingerprintersHistogramAdd()`
- 条件付き依存: `if (cryptominingBlocking)` → `this.cryptominersHistogramAdd()`
- 条件付き依存: `if (cryptominingAllowing)` → `this.cryptominersHistogramAdd()`
- 参照: `this.anyBlocking`, `this.hadShieldState`, `this.hasException`

## onContentBlockingEvent()
- 位置: L1985-2057
- 役割: ブロックイベントを受けて内部状態、アイコン、ツールチップ、開いているパネル、通知、計測を順に更新する
- 触るとき: ブロック検出時の全体の流れを追うとき。uidisabled のカテゴリは判定から外す。
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`, `Object.values()`, `["showing", "open"].includes()`, `blocker.categoryItem?.hasAttribute()`, `blocker.isBlocking()`, `blocker.isDetected()`, `this.iconBox.toggleAttribute()`, `this.reportBlockingEventTelemetry()`
- 条件付き依存: `if (!ContentBlockingAllowList.canHandle(gBrowser.selectedBrowser))` → `this.iconBox.removeAttribute()`
- 条件付き依存: `if (this.hasException)` → `this.showDisabledTooltipForTPIcon()`
- 条件付き依存: `if (this.anyBlocking)` → `this.showActiveTooltipForTPIcon()`
- 条件付き依存: `if (!(this.anyBlocking))` → `this.showNoTrackerTooltipForTPIcon()`
- 条件付き依存: `if (isPanelOpen)` → `this.updatePanelForBlockingEvent()`
- 条件付き依存: `if (!isSimulated)` → `this.notifyContentBlockingEvent()`
- 参照: `blocker.activated`, `gBrowser.selectedBrowser`, `this._categoryItemOrderInvalidated`, `this._lastEvent`, `this._protectionsPopup?.state`, `this.anyBlocking`, `this.anyDetected`, `this.blockers`, `this.hasException`

## onCommand()
- 位置: L2059-2135
- 役割: パネル内のボタン ID ごとに、サブビュー表示、設定、全レポート、マイルストーン、トーストの処理へ振り分けてテレメトリを記録する
- 触るとき: パネル内のボタンを足すか改名するとき。ボタンごとに分岐を追加する必要がある。
- 呼び出し先: `Glean.securityUiProtectionspopup.clickCookies.record()`, `Glean.securityUiProtectionspopup.clickCryptominers.record()`, `Glean.securityUiProtectionspopup.clickFingerprinters.record()`, `Glean.securityUiProtectionspopup.clickFullReport.record()`, `Glean.securityUiProtectionspopup.clickMilestoneMessage.record()`, `Glean.securityUiProtectionspopup.clickSettings.record()`, `Glean.securityUiProtectionspopup.clickSocial.record()`, `Glean.securityUiProtectionspopup.clickSubviewSettings.record()`, `Glean.securityUiProtectionspopup.clickTrackers.record()`, `PanelMultiView.hidePopup()`, `gProtectionsHandler.openPreferences()`, `gProtectionsHandler.openProtections()`, `gProtectionsHandler.showCookiesSubview()`, `gProtectionsHandler.showCryptominersSubview()`, `gProtectionsHandler.showFingerprintersSubview()`, `gProtectionsHandler.showSocialblockerSubview()`, `gProtectionsHandler.showTrackersSubview()`, `this.showProtectionsPopup()`
- 参照: `event.target.id`, `this._protectionsPopup`

## handleEvent()
- 位置: L2138-2173
- 役割: command、focus、popupshown、popuphidden、toggle を対応する処理へ振り分ける
- 触るとき: gProtectionsHandler が受けるイベントの種類を増やすとき。focus では、パネル外へのフォーカス移動でパネルを閉じる。
- 呼び出し先: `elem.compareDocumentPosition()`, `this._protectionsPopup.hasAttribute()`, `this.onCommand()`, `this.onPopupHidden()`, `this.onPopupShown()`, `this.onTPSwitchCommand()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this._protectionsPopup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `event.type`, `this._protectionsPopup`

## observe()
- 位置: L2175-2201
- 役割: 履歴消去時に最初の記録日を取り直し、SmartBlock の要求でパネルを開く
- 触るとき: 履歴削除後の件数ツールチップや、SmartBlock からのパネル起動を変えるとき。起動は対象タブの browserId が一致し、pref が有効な時だけ。
- 呼び出し先: `this._hidePopup()`, `this.maybeUpdateEarliestRecordedDateTooltip()`, `this.showProtectionsPopup()`
- 参照: `gBrowser.selectedBrowser.browserId`, `subject.browserId`, `this._earliestRecordedDate`, `this.smartblockEmbedsEnabledPref`

## refreshProtectionsPopup()
- 位置: L2207-2243
- 役割: ヘッダーのホスト名、トグル、理由リンク、マイルストーン表示、検出状態の属性を描き直す
- 触るとき: パネルを開くたびに更新される内容を変えるとき。マイルストーンは 3 日を過ぎると表示しない。
- 呼び出し先: `Date.now()`, `document.l10n.setAttributes()`, `gIdentityHandler.getHostForDisplay()`, `this._notBlockingWhyLink.setAttribute()`, `this._protectionsPopup.toggleAttribute()`, `this.maybeUpdateEarliestRecordedDateTooltip()`, `this.updateProtectionsToggle()`
- 条件付き依存: `if (this._milestoneTextSet && !expired)` → `this._protectionsPopup.setAttribute()`
- 条件付き依存: `if (this._milestoneTextSet && !expired)` → `NimbusFeatures.privacySecurityMessaging.recordExposureEvent()`
- 条件付き依存: `if (!(this._milestoneTextSet && !expired))` → `this._protectionsPopup.removeAttribute()`
- 参照: `this._milestoneTextSet`, `this._protectionsPopupMainViewHeaderLabel`, `this.anyBlocking`, `this.anyDetected`, `this.hasException`, `this.milestonePref`, `this.milestoneTimestampPref`

## updateProtectionsToggle()
- 位置: L2251-2263
- 役割: ETP トグルの pressed 属性と文言を、現在のホスト名で更新する
- 触るとき: ETP トグルの見た目や文言を変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`, `gIdentityHandler.getHostForDisplay()`, `toggle.toggleAttribute()`
- 参照: `this._TPSwitchCommanding`, `this._protectionsPopupTPSwitch`

## reorderCategoryItems()
- 位置: L2270-2334
- 役割: カテゴリを遮断、許可、検出なしの各セクションへ並べ替え、見出しを出し分けてから SmartBlock のトグルを更新する
- 触るとき: カテゴリの並び順や見出しの表示条件を変えるとき。_categoryItemOrderInvalidated が立っている時だけ実行する。
- 呼び出し先: `Object.values()`, `categoryItem.classList.contains()`, `categoryItem.hasAttribute()`, `categoryItem.parentNode.insertBefore()`, `categoryItem.removeAttribute()`, `this._addSmartblockEmbedToggles()`
- 条件付き依存: `if ( categoryItem.classList.contains("notFound") || categoryItem.hasAttribute("uidisabled") )` → `this._protectionsPopupCategoryList.insertAdjacentElement()`
- 条件付き依存: `if ( categoryItem.classList.contains("notFound") || categoryItem.hasAttribute("uidisabled") )` → `categoryItem.setAttribute()`
- 条件付き依存: `if (categoryItem.classList.contains("blocked") && !this.hasException)` → `categoryItem.parentNode.insertBefore()`
- 参照: `this._categoryItemOrderInvalidated`, `this._protectionsPopupBlockingHeader.hidden`, `this._protectionsPopupNotBlockingHeader.hidden`, `this._protectionsPopupNotFoundHeader`, `this._protectionsPopupNotFoundHeader.hidden`, `this._protectionsPopupSmartblockContainer`, `this._protectionsPopupSmartblockContainer.hidden`, `this.blockers`, `this.hasException`

## _addSmartblockEmbedToggles()
- 位置: L2342-2451
- 役割: SmartBlock 対象の shim された origin に対応するトグルを作り直す。既にあれば pressed を更新する
- 触るとき: SmartBlock の対象サイトや、トグルを出す条件を変えるとき。smartblockEmbedInfo の matchPatterns で対象を判定する。
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `actions.some()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.getContentBlockingEvents()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `matchPatternSet.matches()`, `shimId.toLowerCase()`, `this._protectionsPopupSmartblockToggleContainer.insertAdjacentElement()`, `this._protectionsPopupSmartblockToggleContainer.lastChild.remove()`, `this.smartblockEmbedInfo.find()`, `toggle.addEventListener()`, `toggle.setAttribute()`, `toggle.toggleAttribute()`
- 条件付き依存: `if (shimAllowed)` → `existingToggle.setAttribute()`
- 条件付き依存: `if (newToggleState)` → `this._sendUnblockMessageToSmartblock()`
- 条件付き依存: `if (!(newToggleState))` → `this._sendReblockMessageToSmartblock()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `element.matchPatterns`, `event.target.pressed`, `this._protectionsPopupSmartblockToggleContainer.lastChild`, `this.smartblockEmbedsEnabledPref`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## disableForCurrentPage()
- 位置: L2453-2459
- 役割: 現在のサイトを保護の例外に入れ、必要ならパネルを閉じて再読み込みする
- 触るとき: 例外の登録の流れや、再読み込みの有無を変えるとき。
- 呼び出し先: `ContentBlockingAllowList.add()`
- 条件付き依存: `if (shouldReload)` → `this._hidePopup()`
- 条件付き依存: `if (shouldReload)` → `BrowserCommands.reload()`
- 参照: `gBrowser.selectedBrowser`

## enableForCurrentPage()
- 位置: L2461-2467
- 役割: 現在のサイトを保護の例外から外し、必要なら再読み込みする
- 触るとき: 例外の解除の流れを変えるとき。
- 呼び出し先: `ContentBlockingAllowList.remove()`
- 条件付き依存: `if (shouldReload)` → `this._hidePopup()`
- 条件付き依存: `if (shouldReload)` → `BrowserCommands.reload()`
- 参照: `gBrowser.selectedBrowser`

## onTPSwitchCommand()
- 位置: async L2469-2528
- 役割: ETP トグルで例外を切り替え、タブ切替か 500ms の待ちの後にパネルを閉じてタブを再読み込みする
- 触るとき: ETP の切り替えとトーストの流れを変えるとき。_TPSwitchCommanding で連打を防いでいる。
- 呼び出し先: `PanelMultiView.hidePopup()`, `Promise.race()`, `gBrowser.reloadTab()`, `gBrowser.tabContainer.addEventListener()`, `gBrowser.tabContainer.removeEventListener()`, `setTimeout()`, `this._protectionsPopup.toggleAttribute()`, `this.iconBox.toggleAttribute()`, `this.updateProtectionsToggle()`
- 条件付き依存: `if (newExceptionState)` → `this.showDisabledTooltipForTPIcon()`
- 条件付き依存: `if (!(newExceptionState))` → `this.showNoTrackerTooltipForTPIcon()`
- 条件付き依存: `if (newExceptionState)` → `this.disableForCurrentPage()`
- 条件付き依存: `if (newExceptionState)` → `Glean.securityUiProtectionspopup.clickEtpToggleOff.record()`
- 条件付き依存: `if (!(newExceptionState))` → `this.enableForCurrentPage()`
- 条件付き依存: `if (!(newExceptionState))` → `Glean.securityUiProtectionspopup.clickEtpToggleOn.record()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.outerWindowID`, `gBrowser.selectedTab`, `this._TPSwitchCommanding`, `this._previousOuterWindowID`, `this._previousURI`, `this._protectionsPopup`, `this._showToastAfterRefresh`

## onTabSelectHandler()
- 位置: L2517-2517
- 役割: TabSelect を受けて、待ちを打ち切る Promise を解決する
- 触るとき: ETP の切り替え後の待ちを、タブ切替で早く抜ける条件を変えるとき。
- 呼び出し先: `resolve()`

## setTrackersBlockedCounter()
- 位置: L2530-2553
- 役割: ブロック件数と最初の記録日を表示し、件数が 0 なら件数の箱を隠す
- 触るとき: 件数の文言や 0 件時の表示を変えるとき。
- 呼び出し先: `this._protectionsPopupTrackersCounterBox.toggleAttribute()`
- 条件付き依存: `if (this._earliestRecordedDate)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._earliestRecordedDate))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._earliestRecordedDate))` → `this._protectionsPopupTrackersCounterDescription.removeAttribute()`
- 参照: `this._earliestRecordedDate`, `this._protectionsPopupTrackersCounterDescription`

## maybeSetMilestoneCounterText()
- 位置: async L2562-2583
- 役割: マイルストーン pref の条件を満たす時だけ、最初の記録日から文言を作り、表示可能フラグを立てる
- 触るとき: マイルストーンを出す条件や文言の元データを変えるとき。条件を外れると表示フラグを落とす。
- 呼び出し先: `TrackingDBService.getEarliestRecordedDate()`, `document.l10n.setAttributes()`, `this.milestoneListPref.includes()`
- 参照: `this._milestoneTextSet`, `this._protectionsPopup`, `this._protectionsPopupMilestonesText`, `this.milestonePref`, `this.milestonesEnabledPref`

## showDisabledTooltipForTPIcon()
- 位置: L2585-2594
- 役割: シールドのツールチップを、保護が無効(例外あり)の文言に設定する
- 触るとき: 例外ありの時のツールチップ文言を変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this._trackingProtectionIconContainer`, `this._trackingProtectionIconTooltipLabel`

## showActiveTooltipForTPIcon()
- 位置: L2596-2605
- 役割: シールドのツールチップを、遮断中の文言に設定する
- 触るとき: 遮断中のツールチップ文言を変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this._trackingProtectionIconContainer`, `this._trackingProtectionIconTooltipLabel`

## showNoTrackerTooltipForTPIcon()
- 位置: L2607-2616
- 役割: シールドのツールチップを、検出なしの文言に設定する
- 触るとき: 検出なしのツールチップ文言を変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this._trackingProtectionIconContainer`, `this._trackingProtectionIconTooltipLabel`

## showProtectionsPopup()
- 位置: L2633-2691
- 役割: options に応じてパネルを開く。トーストか通常か、開いた理由の記録、他のパネルを閉じる、アイコンに対して開く
- 触るとき: パネルを開く経路やトーストの扱いを変えるとき。Trust Panel が有効なら何もしない。
- 呼び出し先: `Array.from()`, `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `document.querySelectorAll()`, `this._initializePopup()`, `this._protectionsPopup.toggleAttribute()`, `this.hasOwnProperty()`
- 条件付き依存: `if (this.hasOwnProperty("_lastEvent"))` → `this.updatePanelForBlockingEvent()`
- 条件付き依存: `if (this._toastPanelTimer)` → `clearTimeout()`
- 条件付き依存: `if (!toast)` → `this.refreshProtectionsPopup()`
- 条件付き依存: `if (toast)` → `this._protectionsPopup.addEventListener()`
- 条件付き依存: `if (toast)` → `setTimeout()`
- 条件付き依存: `if (toast)` → `PanelMultiView.hidePopup()`
- 参照: `console.error`, `this._lastEvent`, `this._protectionsPopup`, `this._protectionsPopupOpeningReason`, `this._protectionsPopupToastTimeout`, `this._toastPanelTimer`, `this._trackingProtectionIconContainer`, `this.trustPanelEnabledPref`

## maybeUpdateEarliestRecordedDateTooltip()
- 位置: async L2693-2715
- 役割: 最初の記録日がまだ無ければ取得し、件数の説明文に入れる
- 触るとき: 件数のツールチップの日付を取り直す条件を変えるとき。
- 呼び出し先: `TrackingDBService.getEarliestRecordedDate()`
- 条件付き依存: `if (typeof trackerCount !== "number")` → `TrackingDBService.sumAllEvents()`
- 条件付き依存: `if (date)` → `document.l10n.setAttributes()`
- 参照: `this._earliestRecordedDate`, `this._protectionsPopup`, `this._protectionsPopupTrackersCounterDescription`

## _sendUnblockMessageToSmartblock()
- 位置: L2722-2728
- 役割: SmartBlock のブロック解除を、タブ単位の通知として送る
- 触るとき: webcompat 拡張との通知名や送り先を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## _sendReblockMessageToSmartblock()
- 位置: L2735-2741
- 役割: SmartBlock の再ブロックを、タブ単位の通知として送る
- 触るとき: webcompat 拡張との通知名や送り先を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## _dispatchUserAction()
- 位置: L2746-2773
- 役割: CFR のアクション URL を整形し、SpecialMessageActions で処理して、非プライベートならテレメトリを送る
- 触るとき: 保護パネルの CFR のリンク動作を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.urlFormatter.formatURL()`, `SpecialMessageActions.handleAction()`, `console.error()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `Glean.securityUiProtectionspopup.clickProtectionspopupCfr.record()`
- 参照: `message.content.cta_type`, `message.content.cta_url`, `message.content.cta_where`, `message.id`, `window.gBrowser.selectedBrowser`
- XPCOM: `Services.urlFormatter`

## _attachCommandListener()
- 位置: L2778-2790
- 役割: 要素の mouseup と、Enter または Space の keyup で動作を発火させる
- 触るとき: CFR 要素の操作契機を変えるとき。mousedown と click は PanelMultiView が使うので避けている。
- 呼び出し先: `element.addEventListener()`, `this._dispatchUserAction()`
- 条件付き依存: `if (e.key === "Enter" || e.key === " ")` → `this._dispatchUserAction()`
- 参照: `e.key`

## _insertProtectionsPanelInfoMessage()
- 位置: L2797-2875
- 役割: 情報メッセージを初回に作って展開し、既読後は畳んだ状態にする。パネルを閉じるときに畳む
- 触るとき: 情報メッセージの表示条件や既読 pref を変えるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `container.hasAttribute()`, `doc.getElementById()`, `panelContainer.addEventListener()`
- 条件付き依存: `if (!container.childElementCount)` → `this._createHeroElement()`
- 条件付き依存: `if (!container.childElementCount)` → `container.appendChild()`
- 条件付き依存: `if (!container.childElementCount)` → `infoButton.addEventListener()`
- 条件付き依存: `if ( !this.protectionsPanelMessageSeen && container.hasAttribute("disabled") )` → `toggleMessage()`
- 条件付き依存: `if (!this.protectionsPanelMessageSeen)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( this.protectionsPanelMessageSeen && !container.hasAttribute("disabled") )` → `toggleMessage()`
- 参照: `container.childElementCount`, `event.target.ownerDocument`, `this.protectionsPanelMessageSeen`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## toggleMessage()
- 位置: L2817-2838
- 役割: 情報メッセージの開閉を切り替え、開いた時に impression を送る
- 触るとき: 情報メッセージの開閉の見た目や計測を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `doc.querySelector()`, `panelContainer.hasAttribute()`
- 条件付き依存: `if (learnMoreLink)` → `container.toggleAttribute()`
- 条件付き依存: `if (learnMoreLink)` → `infoButton.toggleAttribute()`
- 条件付き依存: `if (learnMoreLink)` → `panelContainer.toggleAttribute()`
- 条件付き依存: `if ( panelContainer.hasAttribute("infoMessageShowing") && !PrivateBrowsingUtils.isWindowPrivate(window) )` → `Glean.securityUiProtectionspopup.openProtectionspopupCfr.record()`
- 参照: `learnMoreLink.disabled`, `message.id`

## _createElement()
- 位置: L2877-2886
- 役割: XHTML 要素を作り、クラスと l10n ID を付ける
- 触るとき: パネル内の要素を作る共通処理を変えるとき。
- 呼び出し先: `doc.createElementNS()`
- 条件付き依存: `if (options.classList)` → `node.classList.add()`
- 条件付き依存: `if (options.content)` → `doc.l10n.setAttributes()`
- 参照: `options.classList`, `options.content`, `options.content.string_id`

## _createHeroElement()
- 位置: L2888-2921
- 役割: 情報メッセージの見出し、本文、リンクを組み立て、リンクが無ければ全体を操作対象にする
- 触るとき: 情報メッセージの構成や操作の受け付け方を変えるとき。
- 呼び出し先: `messageEl.appendChild()`, `messageEl.classList.add()`, `messageEl.setAttribute()`, `this._createElement()`, `wrapperEl.appendChild()`, `wrapperEl.classList.add()`
- 条件付き依存: `if (message.content.link_text)` → `this._createElement()`
- 条件付き依存: `if (message.content.link_text)` → `wrapperEl.appendChild()`
- 条件付き依存: `if (message.content.link_text)` → `this._attachCommandListener()`
- 条件付き依存: `if (!(message.content.link_text))` → `this._attachCommandListener()`
- 参照: `linkEl.disabled`, `message.content.body`, `message.content.link_text`, `message.content.title`

## _resetToggleSecDelay()
- 位置: L2923-2930
- 役割: pointerdown のたびに、トグル再有効化までの遅延タイマーを張り直す
- 触るとき: クリックジャッキング対策の遅延の扱いを変えるとき。init で bind されている。
- 呼び出し先: `clearTimeout()`, `setTimeout()`, `this._enablePopupToggles()`
- 参照: `this._protectionsPopupButtonDelay`, `this._protectionsPopupToggleDelayTimer`

## _disablePopupToggles()
- 位置: L2932-2938
- 役割: パネル内の moz-toggle を無効化し、pointerdown で遅延を延長する仕掛けを付ける
- 触るとき: SmartBlock 経由で開いた直後の誤操作を防ぐ対策を変えるとき。
- 呼び出し先: `this._protectionsPopup.querySelectorAll()`, `this._protectionsPopup.querySelectorAll("moz-toggle").forEach()`, `toggle.addEventListener()`, `toggle.setAttribute()`
- 参照: `this._resetToggleSecDelay`

## _enablePopupToggles()
- 位置: L2940-2946
- 役割: パネル内の moz-toggle を有効に戻し、pointerdown の仕掛けを外す
- 触るとき: トグルの無効化を解く条件を変えるとき。_disablePopupToggles と対で見る。
- 呼び出し先: `this._protectionsPopup.querySelectorAll()`, `this._protectionsPopup.querySelectorAll("moz-toggle").forEach()`, `toggle.removeAttribute()`, `toggle.removeEventListener()`
- 参照: `this._resetToggleSecDelay`
