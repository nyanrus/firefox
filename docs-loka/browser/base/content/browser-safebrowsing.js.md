# browser/base/content/browser-safebrowsing.js

source: browser/base/content/browser-safebrowsing.js
source-hash: 4079fa41bd5a02664c3d82ca57b18bd52d92bea4
lines: 115

## <module>
- 役割: (未記入)

## setReportPhishingMenu()
- 位置: L6-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `docURI.spec.startsWith()`, `document.getElementById()`, `uri.schemeIs()`
- 条件付き依存: `if (disabledByPolicy || isPhishingPage || !isReportablePage)` → `reportMenu.setAttribute()`
- 条件付き依存: `if (!(disabledByPolicy || isPhishingPage || !isReportablePage))` → `reportMenu.removeAttribute()`
- 条件付き依存: `if (disabledByPolicy || !isPhishingPage || !isReportablePage)` → `reportErrorMenu.setAttribute()`
- 条件付き依存: `if (!(disabledByPolicy || !isPhishingPage || !isReportablePage))` → `reportErrorMenu.removeAttribute()`
- 参照: `gBrowser.currentURI`, `gBrowser.selectedBrowser.documentURI`, `reportErrorMenu.hidden`, `reportMenu.hidden`
- XPCOM: `Services.policies`

## getReportURL()
- 位置: L58-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SafeBrowsing.getReportURL()`
- 条件付き依存: `if (pageUri instanceof Ci.nsIURL)` → `pageUri.mutate().setQuery("").finalize()`
- 条件付き依存: `if (pageUri instanceof Ci.nsIURL)` → `pageUri.mutate().setQuery()`
- 条件付き依存: `if (pageUri instanceof Ci.nsIURL)` → `pageUri.mutate()`
- 参照: `Ci.nsIURL`, `gBrowser.currentURI`, `pageUri.asciiSpec`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md)

## reportFalseDeceptiveSite()
- 位置: L73-113
- 役割: (未記入)
- 触るとき: (未記入)
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
