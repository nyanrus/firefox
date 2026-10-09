# browser/base/content/browser-trustPanel.js

source: browser/base/content/browser-trustPanel.js
source-hash: 544866fac7ea28417b911a5a790893fa0d5db437
lines: 2139

## <module>
- 役割: ツールバーのトラストパネル(保護の状態・接続の安全性・トラッカー遮断を示す盾アイコンとポップアップ)の制御を gTrustPanelHandler に集約する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `this.#resetToggleSecDelay.bind()`

## TrustPanel.init()
- 位置: L198-222
- 役割: 各ブロッカーを初期化し、保護パネル表示要求とFxAログアウトの observer を登録して、違反警告欄の dismiss イベントを結ぶ。
- 触るとき: 起動時に登録する observer やブロッカーを増減するとき、パネル初期化後に違反警告が効かない不具合を調べるとき。
- 呼び出し先: `Object.values()`, `Services.obs.addObserver()`, `customElements.whenDefined()`, `customElements.whenDefined("breach-alert-panel").then()`, `document.getElementById()`
- 条件付き依存: `if (blocker.init)` → `blocker.init()`
- 条件付き依存: `if (breachAlertElement)` → `breachAlertElement.addEventListener()`
- 条件付き依存: `if (breachAlertElement)` → `this.dismissBreachAlert.bind()`
- 参照: `blocker.init`, `this.#blockers`
- XPCOM: `Services.obs`

## TrustPanel.uninit()
- 位置: L224-233
- 役割: init で登録したブロッカーの後始末と observer の解除を行う。
- 触るとき: ウィンドウを閉じた後にリスナーが残るリークを調べるとき、init に新しい登録を足したとき。
- 呼び出し先: `Object.values()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (blocker.uninit)` → `blocker.uninit()`
- 参照: `blocker.uninit`, `this.#blockers`
- XPCOM: `Services.obs`

## TrustPanel.#popup()
- 位置: L235-237
- 役割: trustpanel-popup 要素を返す。
- 触るとき: パネル要素の id を変えるとき、パネル操作が null 参照になるときに確認する。
- 呼び出し先: `document.getElementById()`

## TrustPanel.#enabled()
- 位置: L239-241
- 役割: trustPanel.featureGate の pref を返し、機能全体の有効・無効を判定する。
- 触るとき: トラストパネルを段階的に公開する条件を変えるとき、機能を無効にしても表示が残るときに確認する。
- 呼び出し先: `UrlbarPrefs.get()`

## TrustPanel.#trackerCountEnabled()
- 位置: L243-248
- 役割: トラッカー件数機能のゲートと有効 pref の両方が真かを返す。
- 触るとき: ツールバーのトラッカー件数表示を出す条件を変えるとき、件数が出ない原因を調べるとき。
- 呼び出し先: `UrlbarPrefs.get()`

## TrustPanel.handleProtectionsButtonEvent()
- 位置: L250-262
- 役割: 盾ボタンのクリック(主ボタン)やキー操作(Space/Enter)でポップアップを開く。
- 触るとき: 盾ボタンの入力方式を増やすとき、キーボードで開けないなどのアクセシビリティ不具合を調べるとき。
- 呼び出し先: `event.stopPropagation()`, `this.showPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## TrustPanel.onContentBlockingEvent()
- 位置: async L264-301
- 役割: コンテンツブロッキングイベントを受け、例外登録の有無と各ブロッカーの遮断・検知状態を更新してから件数とポップアップを更新する。
- 触るとき: トラッカー検知や遮断の表示が遅れる・欠ける問題を調べるとき、ブロッカーを新しく追加するとき。
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`, `Object.values()`, `blocker.isBlocking()`, `blocker.isDetected()`, `this.#updateToolbarTrackerCount()`
- 条件付き依存: `if (this.#popup)` → `this.#updatePopup()`
- 参照: `blocker.activated`, `this.#blockers`, `this.#enabled`, `this.#lastEvent`, `this.#popup`, `this.#uri`, `this.anyDetected`, `this.hasException`, `window.gBrowser.selectedBrowser`

## TrustPanel.#initializePopup()
- 位置: L303-349
- 役割: テンプレートを初回だけ DOM に挿入し、ポップアップ内のボタンやリンクに操作ハンドラを結ぶ。
- 触るとき: ポップアップ内に新しいボタンを足すとき、ボタンを押しても反応しないときに確認する。
- 条件付き依存: `if (!this.#popup)` → `document.getElementById()`
- 条件付き依存: `if (!this.#popup)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-popup-connection") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById()`
- 条件付き依存: `if (!this.#popup)` → `this.#openSecurityInformationSubview()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-blocker-see-all") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#openBlockerSubview()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-privacy-link") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#hidePopup()`
- 条件付き依存: `if (!this.#popup)` → `window.openTrustedLinkIn()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-clear-cookies-button") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#showClearCookiesSubview()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-siteinformation-morelink") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#showSecurityPopup()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-clear-cookie-cancel") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-clear-cookie-clear") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#clearSiteData()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-toggle") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#toggleTrackingProtection()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("identity-popup-remove-cert-exception") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#removeCertException()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-popup-security-httpsonlymode-menulist") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#changeHttpsOnlyPermission()`
- 条件付き依存: `if (!this.#popup)` → `this.#popup.addEventListener()`
- 参照: `this.#popup`, `wrapper.content`

## TrustPanel.showPopup()
- 位置: async L351-400
- 役割: アンカーを開いた状態にし、QWAC 判定を開始してからパネルを開き、侵害状況とトラッカー件数を Glean に記録する。
- 触るとき: パネルを開く経路を変えるとき、開いた時の計測値を追加・変更するとき、開く順序で表示がずれる問題を調べるとき。
- 呼び出し先: `Glean.trustpanel.opened.record()`, `PanelMultiView.openPopup()`, `Promise.all()`, `anchor?.setAttribute()`, `getBreachedStatus()`, `this.#anchor()`, `this.#computeTrackerCount()`, `this.#getApplicableBreaches()`, `this.#hasMonitorAccountOrStoredPasswords()`, `this.#initializePopup()`, `this.#updatePopup()`
- 条件付き依存: `if (this.#isSecureContext && !this.#qwacStatusPromise)` → `QWACs.determineQWACStatus( this.#secInfo, this.#uri, gBrowser.selectedBrowser.browsingContext ).then()`
- 条件付き依存: `if (this.#isSecureContext && !this.#qwacStatusPromise)` → `QWACs.determineQWACStatus()`
- 条件付き依存: `if (qwacStatusPromise == this.#qwacStatusPromise && result)` → `this.#updateSecurityInformationSubview()`
- 参照: `gBrowser.selectedBrowser.browsingContext`, `opts.event`, `opts.reason`, `this.#asciiHost`, `this.#isSecureContext`, `this.#openingReason`, `this.#popup`, `this.#qwac`, `this.#qwacStatusPromise`, `this.#secInfo`, `this.#uri`

## TrustPanel.#hidePopup()
- 位置: async L402-408
- 役割: パネルを閉じ、popuphidden が来るまで待つ。
- 触るとき: パネルを閉じてから続きの処理をしたいとき(例: 閉じた後に再読み込みする)に使う。
- 呼び出し先: `PanelMultiView.hidePopup()`, `this.#popup.addEventListener()`
- 参照: `this.#popup`

## TrustPanel.#isWebPage()
- 位置: L417-421
- 役割: 現在の URI が http または https かを返す。
- 触るとき: スキャン中の盾を Web ページに限定する条件を変えるとき、about: ページで盾が変わる原因を調べるとき。
- 呼び出し先: `this.#uri.schemeIs()`
- 参照: `this.#uri`

## TrustPanel.#isSameSite()
- 位置: L432-442
- 役割: 2 つの URI の eTLD+1 が一致するかを返し、例外時は false とする。
- 触るとき: 同一サイト遷移の扱いを変えるとき、同じサイト内の遷移で盾がリセットされる不具合を調べるとき。
- 呼び出し先: `Services.eTLD.getBaseDomain()`
- XPCOM: `Services.eTLD`

## TrustPanel.resetIconForNavigation()
- 位置: L449-475
- 役割: 遷移開始時に別サイトへの遷移なら盾を「スキャン中」表示へ直接戻し、同一サイトなら表示を保つ。
- 触るとき: 遷移中の盾の見た目を変えるとき、前ページの安全表示が一瞬残る問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `icon.classList.add()`, `icon.classList.remove()`, `this.#isSameSite()`
- 参照: `icon.classList`, `this.#blockersChecked`, `this.#enabled`, `this.#sameSiteNavigation`, `this.#trackerCountEnabled`, `this.#uri`

## TrustPanel.onNavigationComplete()
- 位置: L486-498
- 役割: 読み込み完了時に件数を更新し、まだ検査が終わっていなければ検査済みにして盾を更新する。
- 触るとき: 読み込み完了後もスキャン表示が消えない問題を調べるとき、完了時の件数ずれを直すとき。
- 呼び出し先: `this.#updateToolbarTrackerCount()`
- 条件付き依存: `if (!this.#blockersChecked)` → `this.#updateUrlbarIcon()`
- 参照: `this.#blockersChecked`, `this.#enabled`, `this.#trackerCountEnabled`, `this.#uri`

## TrustPanel.updateIdentity()
- 位置: L500-554
- 役割: セキュリティ状態・URI・同一サイト/同一タブ判定を保存し、盾・件数を更新してから侵害チェックを非同期で始める。
- 触るとき: アドレスバーの状態更新に新しい情報を足すとき、タブ切り替えや遷移で盾が誤った状態になる問題を調べるとき。
- 呼び出し先: `WebExtensionPolicy.getByURI()`, `this.#checkForBreaches()`, `this.#isSameSite()`, `this.#updateToolbarTrackerCount()`, `this.#updateUrlbarIcon()`
- 条件付き依存: `if (this.#uri?.spec != uri.spec && this.#popup?.state == "open")` → `PanelMultiView.hidePopup()`
- 参照: `gBrowser.securityUI.secInfo`, `gBrowser.selectedBrowser`, `this.#blockersChecked`, `this.#breachedStatus`, `this.#enabled`, `this.#lastBrowser`, `this.#pageExtensionPolicy`, `this.#popup`, `this.#popup?.state`, `this.#qwac`, `this.#qwacStatusPromise`, `this.#sameSiteNavigation`, `this.#sameTabNavigation`, `this.#secInfo`, `this.#state`, `this.#uri`, `this.#uri?.spec`, `this.#uriHasHost`, `uri.host`, `uri.spec`

## TrustPanel.#checkForBreaches()
- 位置: async L557-577
- 役割: 現在のページの侵害情報を非同期に取得し、まだ同じページなら侵害状態を保存して盾を更新する。
- 触るとき: 侵害アラートの判定やタイミングを変えるとき、遅れて盾が切り替わる問題を調べるとき。
- 呼び出し先: `Promise.all()`, `getBreachedStatus()`, `this.#getApplicableBreaches()`, `this.#hasMonitorAccountOrStoredPasswords()`
- 条件付き依存: `if (breachedStatus !== "disabled" && breachedStatus !== "not-breached")` → `this.#updateUrlbarIcon()`
- 参照: `this.#asciiHost`, `this.#breachedStatus`, `this.#uri`

## TrustPanel.#anchor()
- 位置: L585-593
- 役割: 表示中の盾アイコンを優先し、なければ identity ボックスをポップアップのアンカーとして返す。
- 触るとき: 盾が隠れる構成でポップアップの位置がずれる問題を調べるとき、ツールバー構成を変えるとき。
- 呼び出し先: `anchors.find()`, `document.getElementById()`, `element.checkVisibility()`
- 参照: `PopupNotifications.CHECK_VISIBILITY_OPTIONS`

## TrustPanel.#updateUrlbarIcon()
- 位置: L595-681
- 役割: セキュリティ・侵害・保護の有効性・件数などから盾のクラス集合を決め、不要なクラスを外して付け直す。初回表示時は計測を送る。
- 触るとき: 盾の見た目の条件(安全、警告、侵害、スキャン中など)を変えるとき、盾の色やアニメーションが想定と違うときに確認する。
- 呼び出し先: `document.getElementById()`, `icon.classList.add()`, `icon.classList.toggle()`, `icon.setAttribute()`, `targetClasses.add()`, `targetClasses.has()`, `this.#computeTrackerCount()`, `this.#isSecurePage()`, `this.#isWebPage()`, `this.#tooltipText()`
- 条件付き依存: `if (this.#isSecurePage() && this.#breachedStatus === "breached")` → `targetClasses.add()`
- 条件付き依存: `if (!this.#trackingProtectionEnabled)` → `targetClasses.add()`
- 条件付き依存: `if (this.#isAboutNetErrorPage || this.#isCertUserOverridden)` → `targetClasses.add()`
- 条件付き依存: `if (this.#sameTabNavigation && !this.#sameSiteNavigation)` → `targetClasses.add()`
- 条件付き依存: `if (this.#trackerCountEnabled && this.#computeTrackerCount() > 0)` → `targetClasses.add()`
- 条件付き依存: `if (browser.lastAnimatedBreachURI !== this.#uri?.spec)` → `targetClasses.add()`
- 条件付き依存: `if (browser.lastAnimatedBreachURI !== this.#uri?.spec)` → `Glean.trustpanel.breachAlertShieldAnimated.record()`
- 条件付き依存: `if (!(browser.lastAnimatedBreachURI !== this.#uri?.spec))` → `icon.classList.contains()`
- 条件付き依存: `if (icon.classList.contains("breach-animating"))` → `targetClasses.add()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `this.#isFirstVisit(this.#uri.host).then()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `this.#isFirstVisit()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `Glean.trustpanel.trackerCountShown.record()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `targetClasses.has()`
- 条件付き依存: `if (!targetClasses.has(cls))` → `icon.classList.remove()`
- 参照: `browser.lastAnimatedBreachURI`, `browser.lastTrackerCountShownURI`, `gBrowser.selectedBrowser`, `icon.classList`, `this.#blockersChecked`, `this.#breachedStatus`, `this.#isAboutNetErrorPage`, `this.#isCertUserOverridden`, `this.#isInternalSecurePage`, `this.#sameSiteNavigation`, `this.#sameTabNavigation`, `this.#trackerCountEnabled`, `this.#trackingProtectionEnabled`, `this.#uri.host`, `this.#uri?.spec`

## TrustPanel.#updatePopup()
- 位置: async L683-693
- 役割: 接続状態・カスタムルート・TLS ログ・保護状態の属性をポップアップに設定し、メイン画面を更新する。
- 触るとき: ポップアップ先頭の接続表示に項目を足すとき、属性が古いまま残るときに確認する。
- 呼び出し先: `this.#connectionState()`, `this.#hasCustomRoot()`, `this.#popup.setAttribute()`, `this.#popup.toggleAttribute()`, `this.#tlsKeyLoggingEnabled()`, `this.#trackingProtectionStatus()`, `this.#updateMainView()`

## TrustPanel.#updateMainView()
- 位置: async L695-807
- 役割: 侵害の有無でグラフィックを切り替え、ホスト名・ETP トグル・ラベル・Cookie 削除・ブロッカー欄などメイン画面の全要素を現在の状態に合わせる。
- 触るとき: メイン画面の表示項目を増やすとき、サイトを移動したあとに古い情報が残る問題を調べるとき。
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `PrivateBrowsingUtils.isWindowPrivate()`, `document.getElementById()`, `document.l10n.setAttributes()`, `getBreachedStatus()`, `hostElement.setAttribute()`, `this.#connectionLabel()`, `this.#getApplicableBreaches()`, `this.#hasMonitorAccountOrStoredPasswords()`, `this.#updateAttribute()`, `this.#updateBlockerView()`, `this.#updateToolbarTrackerCount()`, `toggle.toggleAttribute()`
- 条件付き依存: `if (breachedStatus !== "disabled" && breachedStatus !== "not-breached")` → `applicableBreaches.map()`
- 条件付き依存: `if (this.#uri)` → `PlacesUtils.favicons.getFaviconForPage()`
- 条件付き依存: `if (this.#uri)` → `document.getElementById()`
- 条件付き依存: `if (!isPrivate)` → `SiteDataManager.getBaseDomainFromHost()`
- 条件付き依存: `if (!isPrivate)` → `SiteDataManager.hasSiteData(baseDomain).then()`
- 条件付き依存: `if (!isPrivate)` → `SiteDataManager.hasSiteData()`
- 条件付き依存: `if (!isPrivate)` → `this.#updateAttribute()`
- 条件付き依存: `if (!isPrivate)` → `document.getElementById()`
- 参照: `assets.description`, `assets.header`, `assets.innerDescription`, `assets.label`, `breach.Name`, `breachAlertGraphicSection.breachNames`, `breachAlertGraphicSection.breachStatus`, `breachAlertGraphicSection.hidden`, `document.getElementById("trustpanel-popup-icon").src`, `favicon?.uri.spec`, `graphicSection.hidden`, `this.#asciiHost`, `this.#displayHost`, `this.#trackingProtectionEnabled`, `this.#uri`, `this.#uri.host`, `window.gBrowser.selectedBrowser`

## TrustPanel.#computeTrackerCount()
- 位置: L809-818
- 役割: 選択中タブのコンテンツブロッキングログから、プライバシー指標の対象になるエントリ数を数える。
- 触るとき: トラッカー件数の数え方を変えるとき、件数が表示と一致しないときに確認する。
- 呼び出し先: `JSON.parse()`, `Object.values()`, `Object.values(log).filter()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `identifyType()`
- 参照: `logEntriesToCount.length`

## TrustPanel.#updateToolbarTrackerCount()
- 位置: L820-850
- 役割: 件数を計算し、0 より大きければ検査済みにして初回表示 pref を立て、件数表示の各要素を更新してから盾を更新する。
- 触るとき: ツールバーの件数表示の文言や更新タイミングを変えるとき、件数の表示が古いままになる問題を調べるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `document.getElementById()`, `document.l10n.setArgs()`, `this.#computeTrackerCount()`, `this.#updateUrlbarIcon()`
- 条件付き依存: `if (count > 0 && !UrlbarPrefs.get("trackerCountShown"))` → `UrlbarPrefs.set()`
- 条件付き依存: `if (trackerCountLongform)` → `document.l10n.setArgs()`
- 参照: `this.#blockersChecked`, `this.#trackerCountEnabled`, `trackerCountShortform.textContent`

## TrustPanel.#updateBlockerView()
- 位置: L852-887
- 役割: ブロック済みと検知のみのブロッカーを分け、各ボタン欄・スマートブロック欄・件数ヘッダーを更新する。件数 0 の時は欄を隠す。
- 触るとき: 遮断項目の並びや欄の表示条件を変えるとき、過渡的な件数の誤表示を調べるとき。
- 呼び出し先: `Object.values()`, `blocker.isBlocking()`, `document .getElementById()`, `document .getElementById("trustpanel-smartblock-section") .toggleAttribute()`, `document.getElementById()`, `document.l10n.setArgs()`, `this.#addButtons()`, `this.#addSmartblockEmbedToggles()`, `this.#computeTrackerCount()`, `this.#updateAttribute()`
- 条件付き依存: `if (blocker.isBlocking(this.#lastEvent))` → `blocked.push()`
- 条件付き依存: `if (!(blocker.isBlocking(this.#lastEvent)))` → `blocker.isDetected()`
- 条件付き依存: `if (blocker.isDetected(this.#lastEvent))` → `detected.push()`
- 参照: `this.#blockers`, `this.#lastEvent`

## TrustPanel.#showSecurityPopup()
- 位置: async L889-892
- 役割: トラストパネルを閉じてからページ情報ダイアログのセキュリティタブを開く。
- 触るとき: セキュリティ詳細への導線を変えるとき、ページ情報の表示が開かない問題を調べるとき。
- 呼び出し先: `this.#hidePopup()`, `window.BrowserCommands.pageInfo()`

## TrustPanel.#removeCertException()
- 位置: L894-905
- 役割: 現在のホストの証明書例外を消し、キャッシュを無視して再読み込みしてからパネルを閉じる。
- 触るとき: 証明書の例外解除の挙動を変えるとき、例外を消しても警告が残るときに確認する。
- 呼び出し先: `BrowserCommands.reloadSkipCache()`, `Cc["@mozilla.org/security/certoverride;1"].getService()`, `PanelMultiView.hidePopup()`, `overrideService.clearValidityOverride()`
- 参照: `Ci.nsICertOverrideService`, `gBrowser.contentPrincipal.originAttributes`, `this.#popup`, `this.#uri.host`, `this.#uri.port`
- XPCOM: `nsICertOverrideService` / `@mozilla.org/security/certoverride;1`

## TrustPanel.#trackingProtectionStatus()
- 位置: L907-912
- 役割: 安全でないページなら warning、保護が有効なら enabled、無効なら disabled を返す。
- 触るとき: ポップアップの保護状態の表示色や文言を変えるとき、判定が想定と違うときに確認する。
- 呼び出し先: `this.#isSecurePage()`
- 参照: `this.#trackingProtectionEnabled`

## TrustPanel.#updateSecurityInformationSubview()
- 位置: L914-949
- 役割: セキュリティ詳細画面のヘッダー、接続・混在コンテンツ・暗号・HTTPS-Only 状態の属性、CA・所有者・所在地の文言を更新する。
- 触るとき: セキュリティ詳細に新しい項目を足すとき、接続情報の表示が古いときに確認する。
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `element.toggleAttribute()`, `this.#ciphersState()`, `this.#connectionState()`, `this.#hasCustomRoot()`, `this.#httpsOnlyState()`, `this.#mixedContentState()`, `this.#supplementalText()`, `this.#tlsKeyLoggingEnabled()`, `this.#updateAttribute()`
- 参照: `document.getElementById("identity-popup-content-owner").textContent`, `document.getElementById("identity-popup-content-supplemental").textContent`, `document.getElementById("identity-popup-content-verifier").textContent`, `this.#displayHost`, `this.#isBrokenConnection`

## TrustPanel.#openSecurityInformationSubview()
- 位置: L951-956
- 役割: セキュリティ詳細を更新してからサブビューを開く。
- 触るとき: セキュリティ詳細の開き方を変えるとき、開いたときに古い情報が出る問題を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `this.#updateSecurityInformationSubview()`
- 参照: `event.target`

## TrustPanel.#openBlockerSubview()
- 位置: L958-968
- 役割: 遮断一覧のヘッダーを設定し、件数欄を更新してから遮断一覧のサブビューを開く。
- 触るとき: 遮断一覧の画面遷移を変えるとき、一覧を開いても件数が合わないときに確認する。
- 呼び出し先: `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `document.getElementById()`, `document.l10n.setAttributes()`, `this.#updateBlockerView()`
- 参照: `event.target`, `this.#displayHost`

## TrustPanel.#openBlockerDetailsSubview()
- 位置: async L970-1011
- 役割: 選んだブロッカーの件数・見出し・説明・一覧項目を取得して詳細サブビューに設定し、開く。
- 触るとき: ブロッカーごとの詳細画面に項目を足すとき、見出しや一覧が別ブロッカーのものになる問題を調べるとき。
- 呼び出し先: `blocker._generateSubViewListItems()`, `blocker.getBlockerCount()`, `blocker.subViewTitleL10nId()`, `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `document.getElementById()`, `document.getElementById("trustpanel-blocker-items").replaceChildren()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (titleL10nId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (titleL10nId)` → `document.getElementById()`
- 参照: `blocker.l10nKeys.content`, `blocker.l10nKeys.general`, `event.target`

## TrustPanel.#showClearCookiesSubview()
- 位置: async L1013-1022
- 役割: Cookie 削除確認のヘッダーを設定し、そのサブビューを開く。
- 触るとき: Cookie 削除の確認画面の文言や遷移を変えるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `document.getElementById()`, `document.l10n.setAttributes()`
- 参照: `event.target`, `this.#displayHost`

## TrustPanel.#addButtons()
- 位置: async L1024-1052
- 役割: ブロッカーごとにボタンを作り、件数付きのラベルとアイコンを設定して詳細へのクリックを結ぶ。対象が空なら欄を隠す。
- 触るとき: 遮断一覧やブロッカーのボタン文言を変えるとき、ボタンを押したときに別ブロッカーが開く問題を調べるとき。
- 呼び出し先: `Promise.all()`, `blocker.getBlockerCount()`, `blockers.map()`, `button.addEventListener()`, `button.classList.add()`, `button.setAttribute()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `sectionElement .querySelector()`, `sectionElement .querySelector(".trustpanel-blocker-buttons") .replaceChildren()`, `this.#openBlockerDetailsSubview()`
- 参照: `blocker.iconSrc`, `blocker.l10nKeys.general`, `blockers.length`, `sectionElement.hidden`

## TrustPanel.#trackingProtectionEnabled()
- 位置: L1054-1059
- 役割: 現在のサイトが例外リストに入っておらず、かつ許可リストの対象になっているかで保護が有効かを返す。
- 触るとき: サイト単位の保護のオン・オフ判定を変えるとき、トグルの状態が合わないときに確認する。
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`
- 参照: `window.gBrowser.selectedBrowser`

## TrustPanel.#hasMonitorAccount()
- 位置: async L1061-1082
- 役割: FxA にサインインし Monitor の OAuth クライアントが接続されているかを返す。取得に失敗すると false。
- 触るとき: 侵害アラートの出し分け条件を変えるとき、Monitor 利用者判定が外れる問題を調べるとき。
- 呼び出し先: `UIState.get()`, `attachedClients.some()`, `console.warn()`, `fxAccounts.listAttachedOAuthClients()`
- 参照: `UIState.STATUS_SIGNED_IN`, `client.id`, `state.status`, `this.#clearFxaOauthClientCache`

## TrustPanel.#hasStoredPasswords()
- 位置: async L1084-1092
- 役割: 保存済みログインが 1 件以上あるかを返し、失敗時は false とする。
- 触るとき: 侵害アラートの判定条件に保存パスワードを使うとき、パスワード件数が取れない問題を調べるとき。
- 呼び出し先: `Services.logins.countLoginsAsync()`, `console.warn()`
- XPCOM: `Services.logins`

## TrustPanel.#hasMonitorAccountOrStoredPasswords()
- 位置: async L1094-1098
- 役割: Monitor 利用者か保存済みパスワードがあれば真を返す。
- 触るとき: 侵害アラートを出さない条件を変えるとき、どちらの判定が効いているか確認するとき。
- 呼び出し先: `this.#hasMonitorAccount()`, `this.#hasStoredPasswords()`

## TrustPanel.#isFirstVisit()
- 位置: async L1100-1114
- 役割: 履歴 DB で同じホストへの過去の訪問が 2 秒の余裕を除いて無いかを調べる。
- 触るとき: トラッカー件数の計測で初回訪問かどうかを判定し直すとき、履歴の扱いを変えるとき。
- 呼び出し先: `PlacesUtils.promiseDBConnection()`, `conn.executeCached()`, `host.split()`, `host.split("").reverse()`, `host.split("").reverse().join()`
- 参照: `rows.length`

## TrustPanel.#isSecurePage()
- 位置: L1116-1133
- 役割: 内部の安全ページなら真、証明書エラーなら偽とし、接続が安全か、壊れているか、潜在的に信頼できるかの順で安全かを決める。
- 触るとき: 盾を安全表示にする条件を変えるとき、特定の画面だけ安全表示が誤る問題を調べるとき。
- 参照: `this.#isBrokenConnection`, `this.#isCertErrorPage`, `this.#isCertUserOverridden`, `this.#isInternalSecurePage`, `this.#isPotentiallyTrustworthy`, `this.#isSecureConnection`

## TrustPanel.#isInternalSecurePage()
- 位置: L1135-1146
- 役割: about: ページの対応モジュールが IS_SECURE_CHROME_UI フラグを持つかを返す。
- 触るとき: 内部ページを安全扱いにするかを変えるとき、about ページの盾が想定と違うときに確認する。
- 呼び出し先: `this.#uri?.schemeIs()`
- 条件付き依存: `if (this.#uri?.schemeIs("about"))` → `E10SUtils.getAboutModule()`
- 条件付き依存: `if (module)` → `module.getURIFlags()`
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `this.#uri`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md)

## TrustPanel.#clearSiteData()
- 位置: L1148-1152
- 役割: 現在のベースドメインのサイトデータを削除してからパネルを閉じる。
- 触るとき: サイトデータ削除の対象範囲を変えるとき、削除後も Cookie 欄が有効なままのときに確認する。
- 呼び出し先: `SiteDataManager.getBaseDomainFromHost()`, `SiteDataManager.remove()`, `this.#hidePopup()`
- 参照: `this.#uri.host`

## TrustPanel.#toggleTrackingProtection()
- 位置: L1154-1163
- 役割: 保護の状態に応じて許可リストへ追加または削除し、パネルを閉じてページを再読み込みする。
- 触るとき: サイト単位の保護トグルの挙動を変えるとき、切り替え後に再読み込みされない問題を調べるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `window.BrowserCommands.reload()`
- 条件付き依存: `if (this.#trackingProtectionEnabled)` → `ContentBlockingAllowList.add()`
- 条件付き依存: `if (!(this.#trackingProtectionEnabled))` → `ContentBlockingAllowList.remove()`
- 参照: `this.#popup`, `this.#trackingProtectionEnabled`, `window.gBrowser.selectedBrowser`

## TrustPanel.#isHttpsOnlyModeActive()
- 位置: L1165-1167
- 役割: 通常の HTTPS-Only Mode、または秘密ウィンドウ用の設定が有効かを返す。
- 触るとき: HTTPS-Only の有効判定を変えるとき、秘密ウィンドウだけ判定がずれる問題を調べるとき。

## TrustPanel.#isHttpsFirstModeActive()
- 位置: L1169-1174
- 役割: HTTPS-Only が無効で、HTTPS-First(通常または秘密ウィンドウ用)が有効なら真を返す。
- 触るとき: HTTPS-First の判定を変えるとき、HTTPS-Only との優先関係を確認するとき。
- 呼び出し先: `this.#isHttpsOnlyModeActive()`

## TrustPanel.#isSchemelessHttpsFirstModeActive()
- 位置: L1175-1181
- 役割: HTTPS-Only と HTTPS-First が無効で、スキームなし HTTPS-First が有効なら真を返す。
- 触るとき: スキームなし HTTPS-First の表示条件を変えるとき、三つのモードの優先関係を確認するとき。
- 呼び出し先: `this.#isHttpsFirstModeActive()`, `this.#isHttpsOnlyModeActive()`

## TrustPanel.#getIdentityData()
- 位置: L1186-1211
- 役割: 証明書から組織名、サブジェクトの各フィールド、市・州・国、CA 名を取り出して返す。
- 触るとき: 証明書情報の表示項目を増やすとき、証明書の項目が欠けた場合の表示を確認するとき。
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split(",").forEach()`
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split()`
- 条件付き依存: `if (cert.subjectName)` → `v.split()`
- 参照: `cert.issuerCommonName`, `cert.issuerOrganization`, `cert.organization`, `cert.subjectName`, `result.caOrg`, `result.cert`, `result.city`, `result.country`, `result.state`, `result.subjectNameFields`, `result.subjectNameFields.C`, `result.subjectNameFields.L`, `result.subjectNameFields.ST`, `result.subjectOrg`, `this.#secInfo.serverCert`

## TrustPanel.#isSecureContext()
- 位置: L1213-1237
- 役割: securityUI の安全なコンテキスト判定を返す。PDF ビューアでは URI から信頼性を判定し直す。
- 触るとき: PDF ビューアで盾が誤って安全表示になる問題を調べるとき、安全コンテキストの判定元を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `console.error()`
- 参照: `gBrowser.contentPrincipal?.originNoSuffix`, `gBrowser.securityUI.isSecureContext`, `gBrowser.selectedBrowser.documentURI`, `principal.isOriginPotentiallyTrustworthy`
- XPCOM: `Services.scriptSecurityManager`

## TrustPanel.#hasCustomRoot()
- 位置: L1245-1252
- 役割: 安全な接続で、ユーザー例外がなく、証明書チェーンのルートが組み込みでないとき真を返す。
- 触るとき: インポートされたルート証明書の表示を変えるとき、カスタムルートの警告が出ない問題を調べるとき。
- 参照: `this.#isCertUserOverridden`, `this.#isSecureConnection`, `this.#secInfo`, `this.#secInfo.isBuiltCertChainRootBuiltInRoot`

## TrustPanel.#tlsKeyLoggingEnabled()
- 位置: L1260-1266
- 役割: 環境変数 SSLKEYLOGFILE が設定され、かつ安全な接続で例外がないとき真を返す。
- 触るとき: TLS 鍵ログ表示の条件を変えるとき、環境変数による表示を調べるとき。
- 呼び出し先: `Services.env.exists()`
- 参照: `this.#isCertUserOverridden`, `this.#isSecureConnection`
- XPCOM: `Services.env`

## TrustPanel.#isBrokenConnection()
- 位置: L1273-1275
- 役割: ウェブ進行状態に STATE_IS_BROKEN が立っているかを返す。
- 触るとき: 壊れた接続の判定に依存する表示(混在コンテンツ、暗号の弱さ)を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IS_BROKEN`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isSecureConnection()
- 位置: L1284-1293
- 役割: ファイル読み込みでなく、進行状態に STATE_IS_SECURE が立っているかを返す。
- 触るとき: 安全な接続の判定を変えるとき、埋め込みブラウザの状態を誤って使う問題を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IS_SECURE`, `this.#isURILoadedFromFile`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#displayHost()
- 位置: L1298-1305
- 役割: 現在の URI をベースドメインの表示用文字列にして返す。URI がなければ null。
- 触るとき: パネルに表示するサイト名の形式を変えるとき、IDN やポート付きのホストの表示を確認するとき。
- 呼び出し先: `BrowserUtils.formatURIForDisplay()`
- 参照: `this.#uri`

## TrustPanel.#asciiHost()
- 位置: L1310-1319
- 役割: 現在の URI の ASCII 形式のホスト名を返す。失敗時は null。
- 触るとき: 侵害リストなど保存データと照合するとき、表示用ホストを使わずにこちらを使う。
- 参照: `this.#uri`, `this.#uri.asciiHost`

## TrustPanel.#isEV()
- 位置: L1321-1330
- 役割: ファイル読み込みでなく、トップレベルの EV 状態フラグが立っているかを返す。
- 触るとき: EV 証明書の表示や組織名の表示条件を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_EV_TOPLEVEL`, `this.#isURILoadedFromFile`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isAssociatedIdentity()
- 位置: L1332-1334
- 役割: 進行状態の関連付け済み ID フラグを返す。
- 触るとき: 関連付けられた ID の表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_ASSOCIATED`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isMixedActiveContentLoaded()
- 位置: L1336-1340
- 役割: 混在するアクティブコンテンツが読み込まれたかを返す。
- 触るとき: 混在コンテンツの警告表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isMixedActiveContentBlocked()
- 位置: L1342-1346
- 役割: 混在するアクティブコンテンツが遮断されたかを返す。
- 触るとき: 遮断された混在コンテンツの表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_MIXED_ACTIVE_CONTENT`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isMixedPassiveContentLoaded()
- 位置: L1348-1352
- 役割: 混在する受動コンテンツが読み込まれたかを返す。
- 触るとき: 受動的な混在コンテンツの警告表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_DISPLAY_CONTENT`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isContentHttpsOnlyModeUpgraded()
- 位置: L1354-1358
- 役割: HTTPS-Only Mode により HTTPS へ昇格されたかを返す。
- 触るとき: 昇格済みの表示を変えるとき、HTTPS-Only の状態表示を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isContentHttpsOnlyModeUpgradeFailed()
- 位置: L1360-1365
- 役割: HTTPS-Only Mode の昇格が失敗したかを返す。
- 触るとき: 昇格失敗時の表示(top と sub の区別)を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADE_FAILED`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isContentHttpsFirstModeUpgraded()
- 位置: L1367-1372
- 役割: HTTPS-First により HTTPS へ昇格されたかを返す。
- 触るとき: HTTPS-First の昇格表示を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED_FIRST`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isCertUserOverridden()
- 位置: L1374-1376
- 役割: ユーザーが証明書エラーを例外登録しているかを返す。
- 触るとき: 証明書例外時の盾や文言を変えるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_CERT_USER_OVERRIDDEN`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isCertErrorPage()
- 位置: L1378-1389
- 役割: 証明書エラーのページ(about:certerror、または nssFailure2 の neterror)かを判定する。
- 触るとき: 証明書エラーページでの盾や接続表示を変えるとき。
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isSecurelyConnectedAboutNetErrorPage()
- 位置: L1391-1401
- 役割: about:neterror のうち接続問題がない httpErrorPage と serverError を真とする。
- 触るとき: 安全な接続のままのネットエラーページの扱いを変えるとき、その種類を追加するとき。
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isAboutNetErrorPage()
- 位置: L1403-1406
- 役割: 現在のページが about:neterror かを返す。
- 触るとき: ネットエラーページでの盾の警告表示や接続ラベルを変えるとき。
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isAboutHttpsOnlyErrorPage()
- 位置: L1408-1413
- 役割: 現在のページが about:httpsonlyerror かを返す。
- 触るとき: HTTPS-Only のエラーページでの表示を変えるとき。
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isPotentiallyTrustworthy()
- 位置: L1415-1421
- 役割: 接続が壊れておらず、安全なコンテキストか chrome ページのとき真を返す。
- 触るとき: 信頼できる発生元(localhost など)の表示を変えるとき。
- 参照: `gBrowser.selectedBrowser.documentURI?.scheme`, `this.#isBrokenConnection`, `this.#isSecureContext`

## TrustPanel.#isAboutBlockedPage()
- 位置: L1423-1426
- 役割: 現在のページが about:blocked かを返す。
- 触るとき: about:blocked ページの接続表示を変えるとき。
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isURILoadedFromFile()
- 位置: L1428-1430
- 役割: 現在の URI が file: スキームかを返す。
- 触るとき: ローカルファイルの扱いを変えるとき、file の接続表示を調べるとき。
- 呼び出し先: `this.#uri.schemeIs()`

## TrustPanel.qwacStatusPromise()
- 位置: L1436-1438
- 役割: QWAC 判定の Promise を返す。主にテスト用。
- 触るとき: QWAC 判定を待つテストを書くとき、判定結果が遅れる問題を調べるとき。
- 参照: `this.#qwacStatusPromise`

## TrustPanel.#supplementalText()
- 位置: L1440-1477
- 役割: 安全な接続なら CA 名を、EV または QWAC なら組織名と所在地を組み立てて、補足・検証者・所有者の文言を返す。
- 触るとき: セキュリティ詳細の補足文言の形式を変えるとき、EV や QWAC の表示が出ない問題を調べるとき。
- 条件付き依存: `if (this.#isSecureConnection)` → `this.#getIdentityData()`
- 条件付き依存: `if (this.#isEV || this.#qwac)` → `this.#getIdentityData()`
- 条件付き依存: `if (identityData.state && identityData.country)` → `gNavigatorBundle.getFormattedString()`
- 参照: `identityData.caOrg`, `identityData.city`, `identityData.country`, `identityData.state`, `identityData.subjectOrg`, `this.#getIdentityData().caOrg`, `this.#isEV`, `this.#isSecureConnection`, `this.#qwac`, `this.#secInfo.serverCert`

## TrustPanel.#tooltipText()
- 位置: L1479-1515
- 役割: 接続状態に応じて盾のツールチップ文言を決める。HTTP 混在や例外の場合は専用の文言にする。
- 触るとき: 盾のツールチップ文言を変えるとき、非安全接続の注意文が出ない問題を調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!this.#isCertUserOverridden)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!this.#isCertUserOverridden)` → `this.#getIdentityData()`
- 条件付き依存: `if (this.#isMixedActiveContentLoaded)` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && warnTextOnInsecure )` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!this.#isPotentiallyTrustworthy)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (this.#isCertUserOverridden)` → `gNavigatorBundle.getString()`
- 参照: `this.#getIdentityData().caOrg`, `this.#isBrokenConnection`, `this.#isCertUserOverridden`, `this.#isMixedActiveContentLoaded`, `this.#isPotentiallyTrustworthy`, `this.#isSecureConnection`, `this.#uriHasHost`

## TrustPanel.#connectionState()
- 位置: L1517-1550
- 役割: ページの種類と証明書状態から接続種別を決め、ポップアップの connection 属性に使う文字列を返す。
- 触るとき: 接続種別を増やすとき、ページごとに表示アイコンが違う問題を調べるとき。
- 参照: `this.#isAboutBlockedPage`, `this.#isAboutHttpsOnlyErrorPage`, `this.#isAboutNetErrorPage`, `this.#isAssociatedIdentity`, `this.#isCertErrorPage`, `this.#isCertUserOverridden`, `this.#isEV`, `this.#isInternalSecurePage`, `this.#isPotentiallyTrustworthy`, `this.#isSecureConnection`, `this.#isSecurelyConnectedAboutNetErrorPage`, `this.#isURILoadedFromFile`, `this.#pageExtensionPolicy`, `this.#qwac`

## TrustPanel.#connectionLabel()
- 位置: L1552-1560
- 役割: ネットエラーなら接続失敗、安全なら安全、それ以外は非安全の l10n ID を返す。
- 触るとき: 接続ラベルの文言を変えるとき、ラベルが誤る問題を調べるとき。
- 呼び出し先: `this.#isSecurePage()`
- 参照: `this.#isAboutNetErrorPage`

## TrustPanel.#mixedContentState()
- 位置: L1562-1573
- 役割: 受動の読み込み、能動の読み込み、能動の遮断を配列にして混在コンテンツ属性の値を作る。
- 触るとき: 混在コンテンツの表示属性を増やすとき、組み合わせに応じた表示を確認するとき。
- 条件付き依存: `if (this.#isMixedPassiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this.#isMixedActiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this.#isMixedActiveContentBlocked)` → `mixedcontent.push()`
- 参照: `this.#isMixedActiveContentBlocked`, `this.#isMixedActiveContentLoaded`, `this.#isMixedPassiveContentLoaded`

## TrustPanel.#ciphersState()
- 位置: L1575-1587
- 役割: 接続が壊れ、混在コンテンツが無いときに weak を、それ以外は空文字を返す。
- 触るとき: 弱い暗号の判定条件を変えるとき、弱い暗号の表示が出ない問題を調べるとき。
- 参照: `this.#isBrokenConnection`, `this.#isMixedActiveContentLoaded`, `this.#isMixedPassiveContentLoaded`

## TrustPanel.#httpsOnlyState()
- 位置: L1589-1642
- 役割: HTTPS-Only/First の有効モードに応じて例外メニューの表示と値を更新し、例外・昇格失敗・昇格成功の状態文字列を返す。
- 触るとき: HTTPS の状態表示を増やすとき、例外や昇格失敗の表示が想定と違うときに確認する。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this.#isHttpsFirstModeActive()`, `this.#isHttpsOnlyModeActive()`, `this.#isSchemelessHttpsFirstModeActive()`
- 条件付き依存: `if ( isHttpsFirstModeActive || isHttpsOnlyModeActive || isSchemelessHttpsFirstModeActive )` → `this.#getHttpsOnlyPermission()`
- 条件付き依存: `if ( isHttpsFirstModeActive || isHttpsOnlyModeActive || isSchemelessHttpsFirstModeActive )` → `document.getElementById()`
- 参照: `document.getElementById( "trustpanel-popup-security-httpsonlymode" ).hidden`, `document.getElementById( "trustpanel-popup-security-httpsonlymode-menulist" ).value`, `document.getElementById( "trustpanel-popup-security-menulist-off-item" ).hidden`, `this.#isAboutHttpsOnlyErrorPage`, `this.#isContentHttpsFirstModeUpgraded`, `this.#isContentHttpsOnlyModeUpgradeFailed`, `this.#isContentHttpsOnlyModeUpgraded`

## TrustPanel.#getHttpsOnlyPermission()
- 位置: L1649-1674
- 役割: 現在ページの http 版に対する https-only-load-insecure 権限を読み、0 は有効、1 は無効、2 は一時的に無効、-1 は対象外を返す。
- 触るとき: HTTPS-Only の例外の値の意味を変えるとき、メニューの選択値と権限のずれを調べるとき。
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `SitePermissions.getForPrincipal()`, `uri.mutate()`, `uri.mutate().setScheme()`, `uri.mutate().setScheme("http").finalize()`, `uri.schemeIs()`
- 条件付き依存: `if (uri instanceof Ci.nsINestedURI)` → `uri.QueryInterface()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `uri.QueryInterface(Ci.nsINestedURI).innermostURI`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / `Services.scriptSecurityManager`

## TrustPanel.#changeHttpsOnlyPermission()
- 位置: L1679-1757
- 役割: メニューで選んだ値を http 版の権限として保存または削除し、必要ならエラーページを http へ移すか再読み込みする。
- 触るとき: HTTPS-Only の例外設定の動作を変えるとき、例外変更後に再読み込みされない問題を調べるとき。
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `document.getElementById()`, `newURI.mutate()`, `newURI.mutate().setScheme()`, `newURI.mutate().setScheme("http").finalize()`, `parseInt()`, `this.#getHttpsOnlyPermission()`
- 条件付き依存: `if (oldValue < 0)` → `console.error()`
- 条件付き依存: `if (newURI instanceof Ci.nsINestedURI)` → `newURI.QueryInterface()`
- 条件付き依存: `if (newValue === 0)` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (newValue === 1)` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!(newValue === 1))` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (this.#isAboutHttpsOnlyErrorPage)` → `gBrowser.loadURI()`
- 条件付き依存: `if (this.#isAboutHttpsOnlyErrorPage)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this.#isAboutHttpsOnlyErrorPage)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `BrowserCommands.reloadSkipCache()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `gBrowser.selectedBrowser.focus()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_SESSION`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `menulist.selectedItem.value`, `newURI.QueryInterface(Ci.nsINestedURI).innermostURI`, `this.#isAboutHttpsOnlyErrorPage`, `this.#popup`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## TrustPanel.#addSmartblockEmbedToggles()
- 位置: L1765-1847
- 役割: スマートブロックの埋め込み対象があれば、その遮断・許可を切り替えるトグルをコンテナに作り、対象があったかを返す。
- 触るとき: スマートブロックの埋め込み対象を増やすとき、トグルが重複したり出なかったりする問題を調べるとき。
- 呼び出し先: `PanelMultiView.hidePopup()`, `container.insertAdjacentElement()`, `container.replaceChildren()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.getContentBlockingEvents()`, `shimId.toLowerCase()`, `this.#fetchSmartBlocked()`, `toggle.addEventListener()`, `toggle.setAttribute()`, `toggle.toggleAttribute()`
- 条件付き依存: `if (shimAllowed)` → `existingToggle.setAttribute()`
- 条件付き依存: `if (event.target.pressed)` → `this.#sendUnblockMessageToSmartblock()`
- 条件付き依存: `if (!(event.target.pressed))` → `this.#sendReblockMessageToSmartblock()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `blocked.length`, `event.target.pressed`, `this.#popup`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#fetchSmartBlocked()
- 位置: L1849-1884
- 役割: コンテンツブロッキングログから許可または置換された対象を集め、SMARTBLOCK_EMBED_INFO の URL パターンに一致するものだけ返す。
- 触るとき: スマートブロック対象のサイトを増やすとき、対象が検出されない問題を調べるとき。
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `SMARTBLOCK_EMBED_INFO.find()`, `actions.some()`, `blocked.push()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `matchPatternSet.matches()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `element.matchPatterns`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.observe()
- 位置: async L1886-1919
- 役割: FxA ログアウトで OAuth キャッシュを無効にし、保護パネルを開く要求では該当タブなら主ビューを遮断一覧にして開く。
- 触るとき: パネルを外部から開く経路を追加するとき、ログアウト後に Monitor 判定が古いままの問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `multiview.getAttribute()`, `multiview.setAttribute()`, `this.#initializePopup()`, `this.#popup.addEventListener()`, `this.showPopup()`
- 参照: `gBrowser.selectedBrowser.browserId`, `subject.browserId`, `this.#clearFxaOauthClientCache`, `this.#enabled`

## TrustPanel.handleEvent()
- 位置: L1922-1949
- 役割: パネルの外側へフォーカスが移ったら閉じ、popupshown と popuphidden を各ハンドラへ渡す。
- 触るとき: パネルの閉じ方(フォーカス移動時)を変えるとき、@noautohide の扱いを確認するとき。
- 呼び出し先: `elem.compareDocumentPosition()`, `this.#popup.hasAttribute()`, `this.onPopupHidden()`, `this.onPopupShown()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this.#popup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `event.type`, `this.#popup`

## TrustPanel.onPopupShown()
- 位置: L1951-1962
- 役割: フォーカス監視を始め、通知の抑止を設定する。スマートブロックのボタンから開いた場合はトグルを一定時間無効にして誤クリックを防ぐ。
- 触るとき: パネルを開いたときの初期化を変えるとき、スマートブロックのトグル操作が即座に効いてしまう問題を調べるとき。
- 呼び出し先: `PopupNotifications.suppressWhileOpen()`, `window.addEventListener()`
- 条件付き依存: `if (this.#openingReason == "embedPlaceholderButton")` → `this.#disablePopupToggles()`
- 条件付き依存: `if (this.#openingReason == "embedPlaceholderButton")` → `setTimeout()`
- 条件付き依存: `if (this.#openingReason == "embedPlaceholderButton")` → `this.#enablePopupToggles()`
- 参照: `this.#openingReason`, `this.#popup`, `this.#popupToggleDelayTimer`

## TrustPanel.onPopupHidden()
- 位置: L1964-1969
- 役割: フォーカス監視を外し、盾と identity ボックスの open 属性を外す。
- 触るとき: パネルを閉じたあとに開いたままの表示が残る問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById(id)?.removeAttribute()`, `window.removeEventListener()`

## TrustPanel.#sendUnblockMessageToSmartblock()
- 位置: L1976-1982
- 役割: 選択中タブに対して smartblock:unblock-embed を通知し、埋め込みの遮断を解除させる。
- 触るとき: スマートブロックの解除通知の内容や宛先を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## TrustPanel.#sendReblockMessageToSmartblock()
- 位置: L1989-1995
- 役割: 選択中タブに対して smartblock:reblock-embed を通知し、埋め込みを再び遮断させる。
- 触るとき: スマートブロックの再遮断通知の内容や宛先を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## TrustPanel.#resetToggleSecDelay()
- 位置: L1997-2002
- 役割: トグル無効化の待ち時間タイマーを張り直し、時間後にトグルを有効にする。
- 触るとき: クリックジャッキング対策の待ち時間を変えるとき、トグルが押せない時間が長すぎる問題を調べるとき。
- 呼び出し先: `clearTimeout()`, `setTimeout()`, `this.#enablePopupToggles()`
- 参照: `this.#popupToggleDelayTimer`

## TrustPanel.#disablePopupToggles()
- 位置: L2004-2010
- 役割: パネル内のすべての moz-toggle を無効にし、ポインター押下で待ち時間を延ばすリスナーを付ける。
- 触るとき: パネル内のトグルを無効化する対象を変えるとき、有効化されないトグルの原因を調べるとき。
- 呼び出し先: `this.#popup.querySelectorAll()`, `this.#popup.querySelectorAll("moz-toggle").forEach()`, `toggle.addEventListener()`, `toggle.setAttribute()`
- 参照: `this.#resetToggleReference`

## TrustPanel.#enablePopupToggles()
- 位置: L2013-2024
- 役割: パネル内のトグルを有効にし、保護トグルは許可リストの対象のときだけ有効にする。リスナーも外す。
- 触るとき: トグルの有効化条件を変えるとき、保護トグルが無効のまま残る問題を調べるとき。
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `this.#popup.querySelectorAll()`, `this.#popup.querySelectorAll("moz-toggle").forEach()`, `toggle.removeEventListener()`
- 条件付き依存: `if ( toggle.id != "trustpanel-toggle" || ContentBlockingAllowList.canHandle(window.gBrowser.selectedBrowser) )` → `toggle.removeAttribute()`
- 参照: `this.#resetToggleReference`, `toggle.id`, `window.gBrowser.selectedBrowser`

## TrustPanel.#updateAttribute()
- 位置: L2026-2032
- 役割: 値が真なら属性を設定し、偽なら属性を外す。
- 触るとき: 属性の真偽による表示切り替えを追加するとき、属性が残る問題を調べるとき。
- 条件付き依存: `if (value)` → `elem.setAttribute()`
- 条件付き依存: `if (!(value))` → `elem.removeAttribute()`

## TrustPanel.#getBreachAlertStorage()
- 位置: async L2034-2044
- 役割: 侵害アラート保存先を一度だけ初期化し、以降は同じ Promise を返す。
- 触るとき: 侵害アラートの保存先の初期化タイミングを変えるとき、初期化の二重実行を防ぐとき。
- 条件付き依存: `if (this.#breachAlertStoragePromise === null)` → `initializeStorage()`
- 参照: `this.#breachAlertStoragePromise`

## initializeStorage()
- 位置: async L2036-2040
- 役割: BreachAlertStorage を生成して初期化し、完了後に返す(getBreachAlertStorage 内のローカル関数)。
- 触るとき: 侵害アラート保存先の初期化処理を変えるとき。
- 呼び出し先: `storage.initialize()`

## TrustPanel.#getApplicableBreaches()
- 位置: async L2046-2074
- 役割: サイトに関係する侵害を絞り込み、直近 1 年のものを選び、ユーザーが却下していないものだけを返す。
- 触るとき: 侵害アラートを出す条件(対象ドメイン、期間、却下)を変えるとき、アラートが出ない問題を調べるとき。
- 呼び出し先: `( await breachAlertStorage.getBreachAlertDismissals( recentBreaches.map(breach => breach.Name) ) ).map()`, `Services.eTLD.hasRootDomain()`, `breachAlertStorage.getBreachAlertDismissals()`, `breaches.filter()`, `breachesForSite.filter()`, `dismissedBreachNames.includes()`, `recentBreaches.filter()`, `recentBreaches.map()`, `this.#breachAlertsData.getAllBreaches()`, `this.#getBreachAlertStorage()`
- 参照: `breach.Domain`, `breach.Name`, `breachDismissal.breachName`, `breaches.length`, `recentBreach.Name`
- XPCOM: `Services.eTLD`

## TrustPanel.dismissBreachAlert()
- 位置: async L2076-2096
- 役割: 侵害アラートの却下時刻を保存し、侵害状態を disabled にして主ビューと盾を更新する。
- 触るとき: 侵害アラートの却下の保存方式を変えるとき、却下後も盾が赤いままの問題を調べるとき。
- 呼び出し先: `Date.now()`, `breachAlertStorage.setBreachAlertDismissals()`, `breachNames.map()`, `console.error()`, `this.#getBreachAlertStorage()`, `this.#updateMainView()`, `this.#updateUrlbarIcon()`
- 参照: `event.detail.breachNames`, `this.#breachedStatus`

## isRecentBreach()
- 位置: L2103-2112
- 役割: 侵害日が現在から 1 年以内なら真を返す。
- 触るとき: 侵害を新しいものとみなす期間を変えるとき。
- 呼び出し先: `Temporal.Now.plainDateISO()`, `Temporal.PlainDate.compare()`, `Temporal.PlainDate.from()`, `currentDate.subtract()`
- 参照: `breach.BreachDate`

## getBreachedStatus()
- 位置: L2114-2136
- 役割: pref と Monitor/保存パスワードの有無を見て、無効・侵害・未侵害のいずれかを返す。
- 触るとき: 侵害アラートの状態の判定順を変えるとき、どの条件で無効扱いになるかを確認するとき。
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `breaches.length`
