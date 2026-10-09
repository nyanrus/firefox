# browser/actors/BlockedSiteChild.sys.mjs

source: browser/actors/BlockedSiteChild.sys.mjs
source-hash: c0cd55117d29b00f7605d8dde949db41647943e3
lines: 170

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getSiteBlockedErrorDetails()
- 位置: L11-25
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (docShell.failedChannel)` → `docShell.failedChannel.QueryInterface()`
- 参照: `Ci.nsIClassifiedChannel`, `classifiedChannel.matchedList`, `classifiedChannel.matchedProvider`, `docShell.failedChannel`
- XPCOM: [`nsIClassifiedChannel`](../../netwerk/base/nsIClassifiedChannel.idl.md)

## BlockedSiteChild.receiveMessage()
- 位置: L28-33
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (msg.name == "DeceptiveBlockedDetails")` → `getSiteBlockedErrorDetails()`
- 参照: `msg.name`, `this.docShell`

## BlockedSiteChild.handleEvent()
- 位置: L35-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "AboutBlockedLoaded")` → `this.onAboutBlockedLoaded()`
- 条件付き依存: `if (event.type == "click" && event.button == 0)` → `this.onClick()`
- 参照: `event.button`, `event.type`

## BlockedSiteChild.onAboutBlockedLoaded()
- 位置: L43-145
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/e=malwareBlocked/.test()`, `event.target.getAttribute()`, `getSiteBlockedErrorDetails()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!(/e=malwareBlocked/.test(ownerDoc.documentURI)))` → `/e=unwantedBlocked/.test()`
- 条件付き依存: `if (!(/e=unwantedBlocked/.test(ownerDoc.documentURI)))` → `/e=harmfulBlocked/.test()`
- 参照: `event.target.ownerDocument`, `ownerDoc.documentURI`, `ownerDoc.location.href`, `this.docShell`
