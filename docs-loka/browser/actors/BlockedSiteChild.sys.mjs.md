# browser/actors/BlockedSiteChild.sys.mjs

source: browser/actors/BlockedSiteChild.sys.mjs
source-hash: c0cd55117d29b00f7605d8dde949db41647943e3
lines: 170

## <module>
- 役割: セーフブラウジングでブロックされたページのコンテンツ側アクター。ブロック詳細の取得、エラーページのリンク設定、クリックの親への通知を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getSiteBlockedErrorDetails()
- 位置: L11-25
- 役割: 失敗したチャネルの分類情報から、一致したリストとプロバイダー名を取り出す。
- 触るとき: ブロック理由や報告先を決める情報の取得経路を調べるときに見る。
- 条件付き依存: `if (docShell.failedChannel)` → `docShell.failedChannel.QueryInterface()`
- 参照: `Ci.nsIClassifiedChannel`, `classifiedChannel.matchedList`, `classifiedChannel.matchedProvider`, `docShell.failedChannel`
- XPCOM: [`nsIClassifiedChannel`](../../netwerk/base/nsIClassifiedChannel.idl.md)

## BlockedSiteChild.receiveMessage()
- 位置: L28-33
- 役割: DeceptiveBlockedDetails の要求に、ブロック詳細を返す。
- 触るとき: 親側が詐欺サイト判定の詳細を必要とする経路を変えるときに見る。
- 条件付き依存: `if (msg.name == "DeceptiveBlockedDetails")` → `getSiteBlockedErrorDetails()`
- 参照: `msg.name`, `this.docShell`

## BlockedSiteChild.handleEvent()
- 位置: L35-41
- 役割: AboutBlockedLoaded を受けて初期化し、主ボタンの左クリックを onClick に渡す。
- 触るとき: ブロックページのイベント処理の入口を変えるときに見る。
- 条件付き依存: `if (event.type == "AboutBlockedLoaded")` → `this.onAboutBlockedLoaded()`
- 条件付き依存: `if (event.type == "click" && event.button == 0)` → `this.onClick()`
- 参照: `event.button`, `event.type`

## BlockedSiteChild.onAboutBlockedLoaded()
- 位置: L43-145
- 役割: 読み込まれたブロックページに、報告・詳細・サポート・勧告リンクの href を設定し、詳細の表示や勧告文を整える。
- 触るとき: ブロックページのリンク先、勧告文、詳細の初期表示を変えるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `Services.urlFormatter.formatURLPref()`, `doc .getElementById()`, `doc .getElementById("firefox_support") .setAttribute()`, `doc .getElementById("firefox_support_harmful_addons") .setAttribute()`, `doc .getElementById("learn_more_link") .setAttribute()`, `doc .getElementById("report_detection") .setAttribute()`, `doc.getElementById()`, `doc.getElementById("advisory_provider").setAttribute()`, `doc.l10n.setAttributes()`, `getSiteBlockedErrorDetails()`, `lazy.SafeBrowsing.getReportURL()`
- 条件付き依存: `if (desc)` → `doc .getElementById("error_desc_link") .setAttribute()`
- 条件付き依存: `if (desc)` → `doc .getElementById()`
- 条件付き依存: `if (desc)` → `encodeURIComponent()`
- 条件付き依存: `if (showDetails)` → `doc.getElementById()`
- 条件付き依存: `if (showDetails)` → `details.removeAttribute()`
- 条件付き依存: `if (!advisoryUrl)` → `advisoryDesc.remove()`
- 条件付き依存: `if (!advisoryLinkText)` → `advisoryDesc.remove()`
- 参照: `aEvent.detail.err`, `aEvent.detail.url`, `aEvent.target`, `blockedInfo.provider`, `this.docShell`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## BlockedSiteChild.onClick()
- 位置: L147-168
- 役割: クリックされた要素と URL から理由（phishing・malware・unwanted・harmful）を決め、親へ Browser:SiteBlockedError を送る。
- 触るとき: ブロックページ上のボタン操作が親の処理に届かないときに見る。
- 呼び出し先: `/e=malwareBlocked/.test()`, `event.target.getAttribute()`, `getSiteBlockedErrorDetails()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!(/e=malwareBlocked/.test(ownerDoc.documentURI)))` → `/e=unwantedBlocked/.test()`
- 条件付き依存: `if (!(/e=unwantedBlocked/.test(ownerDoc.documentURI)))` → `/e=harmfulBlocked/.test()`
- 参照: `event.target.ownerDocument`, `ownerDoc.documentURI`, `ownerDoc.location.href`, `this.docShell`
