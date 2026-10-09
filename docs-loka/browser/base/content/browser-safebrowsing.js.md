# browser/base/content/browser-safebrowsing.js

source: browser/base/content/browser-safebrowsing.js
source-hash: 4079fa41bd5a02664c3d82ca57b18bd52d92bea4
lines: 115

## <module>
- 役割: Safe Browsing 関連のメニュー制御と、フィッシング・誤検知の報告先 URL 生成を担う gSafeBrowsing オブジェクトを定義する。

## setReportPhishingMenu()
- 位置: L6-45
- 役割: ヘルプメニューの「フィッシングを報告」「誤検知を報告」項目の表示と有効/無効を、現在のページ状態に応じて切り替える。
- 触るとき: ヘルプメニューの報告項目が警告ページや http(s) 以外のページで出てしまう、またはポリシーで無効化されているのに押せるといった不具合を調べるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `docURI.spec.startsWith()`, `document.getElementById()`, `uri.schemeIs()`
- 条件付き依存: `if (disabledByPolicy || isPhishingPage || !isReportablePage)` → `reportMenu.setAttribute()`
- 条件付き依存: `if (!(disabledByPolicy || isPhishingPage || !isReportablePage))` → `reportMenu.removeAttribute()`
- 条件付き依存: `if (disabledByPolicy || !isPhishingPage || !isReportablePage)` → `reportErrorMenu.setAttribute()`
- 条件付き依存: `if (!(disabledByPolicy || !isPhishingPage || !isReportablePage))` → `reportErrorMenu.removeAttribute()`
- 参照: `gBrowser.currentURI`, `gBrowser.selectedBrowser.documentURI`, `reportErrorMenu.hidden`, `reportMenu.hidden`
- XPCOM: `Services.policies`

## getReportURL()
- 位置: L58-71
- 役割: 報告先の URL を SafeBrowsing.getReportURL に委ねて生成する。info 省略時は現在ページの URL からクエリを除いた値を使う。
- 触るとき: 報告 URL に含める情報を変えたいとき、またはクエリ文字列を報告に含めないという前提を崩す変更を入れるとき。
- 呼び出し先: `SafeBrowsing.getReportURL()`
- 条件付き依存: `if (pageUri instanceof Ci.nsIURL)` → `pageUri.mutate().setQuery("").finalize()`
- 条件付き依存: `if (pageUri instanceof Ci.nsIURL)` → `pageUri.mutate().setQuery()`
- 条件付き依存: `if (pageUri instanceof Ci.nsIURL)` → `pageUri.mutate()`
- 参照: `Ci.nsIURL`, `gBrowser.currentURI`, `pageUri.asciiSpec`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md)

## reportFalseDeceptiveSite()
- 位置: L73-113
- 役割: about:blocked の欺瞞ページを持つブラウジングコンテキストを探し、報告 URL を新しいタブで開く。報告 URL がなければアラートを出す。
- 触るとき: 誤検知の報告ボタンを押しても何も開かない、または子フレームの欺瞞ページで報告が動かないといった問題を追うとき。
- 呼び出し先: `contextsToVisit.pop()`, `contextsToVisit.push()`, `docURI.spec.startsWith()`
- 条件付き依存: `if ( docURI && docURI.spec.startsWith("about:blocked?e=deceptiveBlocked") )` → `global.getActor()`
- 条件付き依存: `if ( docURI && docURI.spec.startsWith("about:blocked?e=deceptiveBlocked") )` → `actor.sendQuery("DeceptiveBlockedDetails").then()`
- 条件付き依存: `if ( docURI && docURI.spec.startsWith("about:blocked?e=deceptiveBlocked") )` → `actor.sendQuery()`
- 条件付き依存: `if ( docURI && docURI.spec.startsWith("about:blocked?e=deceptiveBlocked") )` → `gSafeBrowsing.getReportURL()`
- 条件付き依存: `if (reportUrl)` → `openTrustedLinkIn()`
- 条件付き依存: `if (!(reportUrl))` → `Services.strings.createBundle()`
- 条件付き依存: `if (!(reportUrl))` → `Services.prompt.alert()`
- 条件付き依存: `if (!(reportUrl))` → `bundle.GetStringFromName()`
- 条件付き依存: `if (!(reportUrl))` → `bundle.formatStringFromName()`
- 参照: `contextsToVisit.length`, `currentContext.children`, `currentContext.currentWindowGlobal`, `data.blockedInfo`, `data.blockedInfo.provider`, `gBrowser.selectedBrowser.browsingContext`, `global.documentURI`
- XPCOM: `Services.prompt` / `Services.strings`
