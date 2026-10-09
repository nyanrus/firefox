# browser/components/tabnotes/CanonicalURLChild.sys.mjs

source: browser/components/tabnotes/CanonicalURLChild.sys.mjs
source-hash: bbdcd475d3c55e843568460185903425ba2c902f
lines: 76

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## CanonicalURLChild.handleEvent()
- 位置: L23-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#discoverCanonicalUrl()`, `this.contentWindow.setTimeout()`
- 参照: `event.type`

## CanonicalURLChild.receiveMessage()
- 位置: L47-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cleanNoncanonicalUrl()`, `this.#discoverCanonicalUrl()`, `this.sendAsyncMessage()`
- 参照: `msg.data.pushStateUrl`, `msg.name`

## CanonicalURLChild.#discoverCanonicalUrl()
- 位置: L64-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(candidates).filter()`, `lazy.findCandidates()`, `lazy.pickCanonicalUrl()`, `this.sendAsyncMessage()`
- 参照: `this.document`
