# browser/base/content/pageinfo/security.js

source: browser/base/content/pageinfo/security.js
source-hash: 09e979dfc03c884a0a6c48898445d2bccdf53032
lines: 445

## <module>
- 役割: ページ情報ダイアログの「セキュリティ」タブを作るスクリプト。接続の暗号化状態、証明書、サイトデータ、保存済みパスワード、訪問回数を集めて表示する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## init()
- 位置: async L22-26
- 役割: uri と windowInfo を保持し、_getSecurityInfo で接続のセキュリティ情報を取得して securityInfo に入れる。
- 触るとき: セキュリティタブに渡す入力が変わったとき、または securityInfo が null になる条件を調べるとき。
- 呼び出し先: `this._getSecurityInfo()`
- 参照: `this.securityInfo`, `this.uri`, `this.windowInfo`

## viewCert()
- 位置: L28-41
- 役割: 証明書チェーンを DER の base64 にして about:certificate のURLを作り、既存のブラウザタブで開く。タブが無ければ新しいウィンドウで開く。
- 触るとき: 証明書表示の経路(URLの形式や開き方)を変えるとき。引数の既定値は securityInfo.certChain。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `certChain.map()`, `certs.map()`, `certsStringURL.join()`, `elem.getBase64DERString()`, `encodeURIComponent()`
- 条件付き依存: `if (win)` → `win.switchToTabHavingURI()`
- 条件付き依存: `if (!(win))` → `URILoadingHelper.openTrustedLinkIn()`
- 参照: `this.securityInfo.certChain`

## viewQWAC()
- 位置: L43-45
- 役割: QWAC の証明書を1件の配列にして viewCert に渡す。
- 触るとき: QWAC 証明書の表示ボタンの動作を変えるとき。
- 呼び出し先: `this.viewCert()`
- 参照: `this.securityInfo.qwac`

## _getSecurityInfo()
- 位置: async L47-168
- 役割: トップレベルのウィンドウでのみ、ブラウザの securityUI から状態フラグ(壊れ、混在、EV)を読み、セキュアコンテキストなら証明書、QWAC の判定、TLS 版、暗号方式、CT の状態を集めて返す。
- 触るとき: ページ情報に出る暗号化や証明書の情報を追加・変更するとき、または http などで情報が空になる理由を調べるとき。
- 呼び出し先: `QWACs.determineQWACStatus()`, `security._getSecurityUI()`
- 参照: `Ci.nsITransportSecurityInfo .CERTIFICATE_TRANSPARENCY_POLICY_COMPLIANT`, `Ci.nsITransportSecurityInfo .CERTIFICATE_TRANSPARENCY_POLICY_NOT_DIVERSE_SCTS`, `Ci.nsITransportSecurityInfo .CERTIFICATE_TRANSPARENCY_POLICY_NOT_ENOUGH_SCTS`, `Ci.nsITransportSecurityInfo.CERTIFICATE_TRANSPARENCY_NOT_APPLICABLE`, `Ci.nsITransportSecurityInfo.SSL_VERSION_3`, `Ci.nsITransportSecurityInfo.TLS_VERSION_1`, `Ci.nsITransportSecurityInfo.TLS_VERSION_1_1`, `Ci.nsITransportSecurityInfo.TLS_VERSION_1_2`, `Ci.nsITransportSecurityInfo.TLS_VERSION_1_3`, `Ci.nsIWebProgressListener.STATE_IDENTITY_EV_TOPLEVEL`, `Ci.nsIWebProgressListener.STATE_IS_BROKEN`, `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_DISPLAY_CONTENT`, `cert.issuerName`, `cert.issuerOrganization`, `retval.certificateTransparency`, `retval.encryptionAlgorithm`, `retval.encryptionStrength`, `retval.version`, `secInfo.certificateTransparencyStatus`, `secInfo.cipherName`, `secInfo.handshakeCertificates`, `secInfo.protocolVersion`, `secInfo.secretKeyLength`, `secInfo.serverCert`, `secInfo.succeededCertChain`, `secInfo.succeededCertChain.length`, `this.uri`, `this.windowInfo.isTopWindow`, `ui.isSecureContext`, `ui.secInfo`, `ui.state`
- XPCOM: [`nsITransportSecurityInfo`](../../../../dom/interfaces/base/nsIBrowser.idl.md) / [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _getSecurityUI()
- 位置: L171-176
- 役割: opener の gBrowser があればその securityUI を返し、無ければ null を返す。
- 触るとき: ページ情報を開いた元ウィンドウの特定方法を変えるとき。
- 参照: `window.opener.gBrowser`, `window.opener.gBrowser.securityUI`

## _updateSiteDataInfo()
- 位置: async L178-219
- 役割: 現在のホストのサイトデータを取得し、サイズと Cookie の有無に応じた説明文を設定する。データが無ければ「なし」にしてサイトデータ削除ボタンを無効にする。
- 触るとき: サイトデータの表示文言や、削除ボタンの有効条件を変えるとき。
- 呼び出し先: `SiteDataManager.getSite()`, `clearSiteDataButton.removeAttribute()`, `document.getElementById()`
- 条件付き依存: `if (!this.siteData)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!this.siteData)` → `clearSiteDataButton.setAttribute()`
- 条件付き依存: `if (usage > 0)` → `DownloadUtils.convertByteUnits()`
- 条件付き依存: `if (this.siteData.cookies.length)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this.siteData.cookies.length))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(usage > 0))` → `document.l10n.setAttributes()`
- 参照: `this.siteData`, `this.siteData.cookies.length`, `this.uri.host`

## clearSiteData()
- 位置: L224-233
- 役割: 削除の確認ダイアログを出し、承認されたら基底ドメインのサイトデータを削除してから表示を更新する。
- 触るとき: サイトデータ削除の範囲や確認の流れを変えるとき。
- 条件付き依存: `if (this.siteData)` → `SiteDataManager.promptSiteDataRemoval()`
- 条件付き依存: `if (SiteDataManager.promptSiteDataRemoval(window, [baseDomain]))` → `SiteDataManager.remove(baseDomain).then()`
- 条件付き依存: `if (SiteDataManager.promptSiteDataRemoval(window, [baseDomain]))` → `SiteDataManager.remove()`
- 条件付き依存: `if (SiteDataManager.promptSiteDataRemoval(window, [baseDomain]))` → `this._updateSiteDataInfo()`
- 参照: `this.siteData`

## viewPasswords()
- 位置: L238-243
- 役割: 現在のホスト名でフィルタしたパスワードマネージャを Pageinfo の入口として開く。
- 触るとき: パスワードマネージャを開く条件や、フィルタに使う値を変えるとき。
- 呼び出し先: `LoginHelper.openPasswordManager()`
- 参照: `this.windowInfo.hostName`

## securityOnLoad()
- 位置: async L246-394
- 役割: セキュリティ情報を読み込み、タブの表示・非表示を決めたうえで、アイデンティティ、プライバシーと履歴、技術的詳細の各欄を埋める。
- 触るとき: セキュリティタブの表示内容をどこから決めているかを追うとき。新しい項目を足すならここに足す。
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `previousVisitCount()`, `realmHasPasswords()`, `security.init()`, `setText()`, `uri.spec.startsWith()`
- 条件付き依存: `if ( !info || (uri.scheme === "about" && !uri.spec.startsWith("about:certerror")) )` → `document.getElementById()`
- 条件付き依存: `if (info.qwac)` → `setText()`
- 条件付き依存: `if (info.isEV)` → `setText()`
- 条件付き依存: `if (!(info.isEV))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(info.isEV))` → `document.getElementById()`
- 条件付き依存: `if (!(info.isEV))` → `setText()`
- 条件付き依存: `if (!(info.cert && !info.isBroken))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(info.cert && !info.isBroken))` → `document.getElementById()`
- 条件付き依存: `if (validity)` → `setText()`
- 条件付き依存: `if (!(validity))` → `document.getElementById()`
- 条件付き依存: `if (uri.scheme == "http" || uri.scheme == "https")` → `SiteDataManager.updateSites().then()`
- 条件付き依存: `if (uri.scheme == "http" || uri.scheme == "https")` → `SiteDataManager.updateSites()`
- 条件付き依存: `if (uri.scheme == "http" || uri.scheme == "https")` → `security._updateSiteDataInfo()`
- 条件付き依存: `if (!(uri.scheme == "http" || uri.scheme == "https"))` → `document.getElementById()`
- 条件付き依存: `if (await realmHasPasswords(uri))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (await realmHasPasswords(uri))` → `document.getElementById()`
- 条件付き依存: `if (!(await realmHasPasswords(uri)))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(await realmHasPasswords(uri)))` → `document.getElementById()`
- 条件付き依存: `if (info.isMixed)` → `pkiBundle.getString()`
- 条件付き依存: `if (!(info.isMixed))` → `pkiBundle.getFormattedString()`
- 条件付き依存: `if (!(info.isMixed))` → `pkiBundle.getString()`
- 条件付き依存: `if (info.isBroken)` → `pkiBundle.getString()`
- 条件付き依存: `if (info.encryptionStrength > 0)` → `pkiBundle.getFormattedString()`
- 条件付き依存: `if (info.encryptionStrength > 0)` → `pkiBundle.getString()`
- 条件付き依存: `if (!(info.encryptionStrength > 0))` → `pkiBundle.getString()`
- 条件付き依存: `if (windowInfo.hostName != null)` → `pkiBundle.getFormattedString()`
- 条件付き依存: `if (!(windowInfo.hostName != null))` → `pkiBundle.getString()`
- 条件付き依存: `if (info.certificateTransparency)` → `pkiBundle.getString()`
- 参照: `ctStatus.hidden`, `ctStatus.value`, `document.getElementById("security-identity-validity-row").hidden`, `document.getElementById("security-privacy-sitedata-row").hidden`, `document.getElementById("securityTab").hidden`, `info.cAName`, `info.cert`, `info.cert.issuerCommonName`, `info.cert.issuerName`, `info.cert.organization`, `info.cert.validity.notAfterLocalDay`, `info.certificateTransparency`, `info.encryptionAlgorithm`, `info.encryptionStrength`, `info.isBroken`, `info.isEV`, `info.isMixed`, `info.qwac`, `info.qwac.issuerOrganization`, `info.qwac.organization`, `info.version`, `security.securityInfo`, `uri.scheme`, `viewCert.collapsed`, `viewQWAC.collapsed`, `windowInfo.hostName`

## setText()
- 位置: L396-406
- 役割: 指定 id の要素に値を入れる。input と label は value に、それ以外は textContent に入れる。要素が無ければ何もしない。
- 触るとき: ページ情報の表示欄への書き込み方法を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `element.localName`, `element.textContent`, `element.value`

## realmHasPasswords()
- 位置: async L412-414
- 役割: uri の prePath に保存済みログインがあるかを非同期に数え、1件以上なら true を返す。
- 触るとき: 保存済みパスワードの有無の判定条件を変えるとき。
- 呼び出し先: `Services.logins.countLoginsAsync()`
- 参照: `uri.prePath`
- XPCOM: `Services.logins`

## previousVisitCount()
- 位置: L421-444
- 役割: 履歴で指定ホストの訪問を今日より前の範囲で数え、その件数を返す。ホストが無ければ 0。
- 触るとき: 履歴の訪問回数の集計範囲(今日を含めるか等)を変えるとき。
- 呼び出し先: `Cc[ "@mozilla.org/browser/nav-history-service;1" ].getService()`, `historyService.executeQuery()`, `historyService.getNewQuery()`, `historyService.getNewQueryOptions()`
- 参照: `Ci.nsINavHistoryService`, `options.RESULTS_AS_VISIT`, `options.resultType`, `query.TIME_RELATIVE_TODAY`, `query.domain`, `query.endTime`, `query.endTimeReference`, `result.root.childCount`, `result.root.containerOpen`
- XPCOM: [`nsINavHistoryService`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `@mozilla.org/browser/nav-history-service;1` → `nsNavHistory` (toolkit/components/places/components.conf)
