# browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs

source: browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs
source-hash: d217b2de3e0f4e6ca33c51cb30127ec74163fced
lines: 248

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `Components.ID()`

## reportFailure()
- 位置: L57-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PolicyFailures.report()`, `lazy.log.error()`

## init()
- 位置: L65-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.manager.QueryInterface()`, `blockArray.push()`, `blocklist[i].toLowerCase()`, `exceptionArray.push()`, `exceptionlist[i].toLowerCase()`, `lazy.log.debug()`, `registrar.isContractIDRegistered()`, `reportFailure()`
- 条件付き依存: `if (!registrar.isContractIDRegistered(this.contractID))` → `registrar.registerFactory()`
- 条件付き依存: `if (!registrar.isContractIDRegistered(this.contractID))` → `Services.catMan.addCategoryEntry()`
- 条件付き依存: `if (!this._observerAdded)` → `Services.obs.addObserver()`
- 参照: `Ci.nsIComponentRegistrar`, `blocklist.length`, `exceptionArray.length`, `exceptionlist.length`, `this._blockPatterns`, `this._exceptionsPatterns`, `this._observerAdded`, `this.classDescription`, `this.classID`, `this.contractID`
- XPCOM: [`nsIComponentRegistrar`](../../../../xpcom/components/nsIComponentRegistrar.idl.md) / `Services.catMan` / `Services.obs`

## asyncOnChannelRedirect()
- 位置: L143-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback.onRedirectVerifyCallback()`, `this.isAllowed()`
- 条件付き依存: `if ( (contentType == Ci.nsIContentPolicy.TYPE_DOCUMENT || contentType == Ci.nsIContentPolicy.TYPE_SUBDOCUMENT || contentType == Ci.nsIContentPolicy.TYPE_OBJECT) ...)` → `oldChannel.cancel()`
- 条件付き依存: `if ( (contentType == Ci.nsIContentPolicy.TYPE_DOCUMENT || contentType == Ci.nsIContentPolicy.TYPE_SUBDOCUMENT || contentType == Ci.nsIContentPolicy.TYPE_OBJECT) ...)` → `callback.onRedirectVerifyCallback()`
- 参照: `Ci.nsIContentPolicy.TYPE_DOCUMENT`, `Ci.nsIContentPolicy.TYPE_OBJECT`, `Ci.nsIContentPolicy.TYPE_SUBDOCUMENT`, `Cr.NS_ERROR_BLOCKED_BY_POLICY`, `Cr.NS_OK`, `newChannel.URI.spec`, `newChannel.loadInfo.externalContentPolicyType`
- XPCOM: [`nsIContentPolicy`](../../../../dom/base/nsIContentPolicy.idl.md)

## shouldLoad()
- 位置: L158-176
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(contentLocation.scheme == "view-source"))` → `url.toLowerCase().startsWith()`
- 条件付き依存: `if (!(contentLocation.scheme == "view-source"))` → `url.toLowerCase()`
- 条件付き依存: `if (url.toLowerCase().startsWith("about:reader?"))` → `lazy.ReaderMode.getOriginalUrl()`
- 条件付き依存: `if (url.toLowerCase().startsWith("about:reader?"))` → `url.substring()`
- 条件付き依存: `if ( contentType == Ci.nsIContentPolicy.TYPE_DOCUMENT || contentType == Ci.nsIContentPolicy.TYPE_SUBDOCUMENT || contentType == Ci.nsIContentPolicy.TYPE_OBJECT )` → `this.isAllowed()`
- 参照: `Ci.nsIContentPolicy.ACCEPT`, `Ci.nsIContentPolicy.REJECT_POLICY`, `Ci.nsIContentPolicy.TYPE_DOCUMENT`, `Ci.nsIContentPolicy.TYPE_OBJECT`, `Ci.nsIContentPolicy.TYPE_SUBDOCUMENT`, `contentLocation.pathQueryRef`, `contentLocation.scheme`, `contentLocation.spec`, `loadInfo.externalContentPolicyType`
- XPCOM: [`nsIContentPolicy`](../../../../dom/base/nsIContentPolicy.idl.md)

## shouldProcess()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIContentPolicy.ACCEPT`
- XPCOM: [`nsIContentPolicy`](../../../../dom/base/nsIContentPolicy.idl.md)

## observe()
- 位置: L180-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `channel.getResponseHeader()`, `subject.QueryInterface()`, `this.isAllowed()`
- 条件付き依存: `if (!url)` → `URL.parse()`
- 条件付き依存: `if (url && !this.isAllowed(url.href))` → `channel.cancel()`
- 参照: `Ci.nsIContentPolicy.TYPE_DOCUMENT`, `Ci.nsIContentPolicy.TYPE_OBJECT`, `Ci.nsIContentPolicy.TYPE_SUBDOCUMENT`, `Ci.nsIHttpChannel`, `Cr.NS_ERROR_BLOCKED_BY_POLICY`, `channel.URI.spec`, `channel.isDocument`, `channel.loadInfo.externalContentPolicyType`, `channel.responseStatus`, `url.href`
- XPCOM: [`nsIContentPolicy`](../../../../dom/base/nsIContentPolicy.idl.md) / [`nsIHttpChannel`](../../../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## createInstance()
- 位置: L217-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.QueryInterface()`

## isAllowed()
- 位置: L220-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._blockPatterns?.matches()`, `this.normalizeURL()`
- 条件付き依存: `if (this._blockPatterns?.matches(normalizedURL))` → `this._exceptionsPatterns.matches()`
- 参照: `this._exceptionsPatterns`

## normalizeURL()
- 位置: L237-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `parsed.hostname.endsWith()`, `parsed.href.toLowerCase()`
- 条件付き依存: `if (parsed.hostname.endsWith("."))` → `parsed.hostname.replace()`
- 参照: `parsed.hostname`
