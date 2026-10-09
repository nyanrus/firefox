# browser/components/newtab/SponsorProtection.sys.mjs

source: browser/components/newtab/SponsorProtection.sys.mjs
source-hash: 32fb5d0b573b8ae945329b11ff09ab81d218061c
lines: 236

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`, `console.createInstance()`

## _SponsorProtection.constructor()
- 位置: L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.#debugEnabled`
- XPCOM: `Services.prefs`

## _SponsorProtection.enabled()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SPONSOR_PROTECTION_ENABLED`

## _SponsorProtection.debugEnabled()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#debugEnabled`

## _SponsorProtection.addProtectedBrowser()
- 位置: L81-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#protectedBrowsers.add()`
- 条件付き依存: `if (!this.#observerAndFilterAdded)` → `this.#addObserverAndChannelFilter()`
- 参照: `browser.permanentKey`, `this.#observerAndFilterAdded`, `this.enabled`

## _SponsorProtection.removeProtectedBrowser()
- 位置: L105-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#protectedBrowsers.delete()`
- 参照: `browser.permanentKey`

## _SponsorProtection.isProtectedBrowser()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#protectedBrowsers.has()`
- 参照: `browser.permanentKey`

## _SponsorProtection.#addObserverAndChannelFilter()
- 位置: L126-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.ProxyService.registerChannelFilter()`, `lazy.logConsole.debug()`
- 参照: `this.#observerAndFilterAdded`
- XPCOM: `Services.obs`

## _SponsorProtection.#removeObserverAndChannelFilter()
- 位置: L138-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.ProxyService.unregisterChannelFilter()`, `lazy.logConsole.debug()`
- 参照: `this.#observerAndFilterAdded`
- XPCOM: `Services.obs`

## _SponsorProtection.observe()
- 位置: L161-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `Glean.newtab.sponsNavTrafficRecvd.accumulate()`, `Glean.newtab.sponsNavTrafficSent.accumulate()`, `Math.round()`, `lazy.logConsole.debug()`, `this.#protectedBrowsers.has()`
- 条件付き依存: `if ( !ChromeUtils.nondeterministicGetWeakSetKeys(this.#protectedBrowsers) .length )` → `this.#removeObserverAndChannelFilter()`
- 参照: `ChromeUtils.nondeterministicGetWeakSetKeys(this.#protectedBrowsers) .length`, `Ci.nsIHttpChannel`, `browser.currentURI.spec`, `browser.permanentKey`, `browsingContext?.top.embedderElement`, `channel.URI.spec`, `channel.loadInfo`, `channel.requestSize`, `channel.transferSize`, `this.#protectedBrowsers`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## _SponsorProtection.applyFilter()
- 位置: L215-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback.onProxyFilterResult()`, `this.#protectedBrowsers.has()`
- 条件付き依存: `if (!browser || !this.#protectedBrowsers.has(browser))` → `callback.onProxyFilterResult()`
- 参照: `browsingContext?.top.embedderElement`, `channel.loadInfo`
