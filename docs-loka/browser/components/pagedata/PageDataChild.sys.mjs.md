# browser/components/pagedata/PageDataChild.sys.mjs

source: browser/components/pagedata/PageDataChild.sys.mjs
source-hash: 1b617cdda1272a5565bbe1e8eb87a05985b454df
lines: 123

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## PageDataChild.actorCreated()
- 位置: L39-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `this.#isContentWindowPrivate`, `this.contentWindow`

## PageDataChild.didDestroy()
- 位置: L47-51
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#deferTimer)` → `this.#deferTimer.cancel()`
- 参照: `this.#deferTimer`

## PageDataChild.#deferReady()
- 位置: L57-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deferTimer.initWithCallback()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!this.#deferTimer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT_LOW_PRIORITY`, `lazy.READY_DELAY`, `this.#deferTimer`, `this.document.documentURI`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PageDataChild.receiveMessage()
- 位置: L84-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PageDataSchema.collectPageData()`
- 条件付き依存: `if (this.document.readystate == "complete")` → `this.#deferReady()`
- 参照: `msg.name`, `this.#isContentWindowPrivate`, `this.document`, `this.document.readystate`

## PageDataChild.handleEvent()
- 位置: L110-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deferReady()`
- 参照: `event.type`, `this.#isContentWindowPrivate`
