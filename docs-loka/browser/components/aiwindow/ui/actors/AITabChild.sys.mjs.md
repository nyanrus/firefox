# browser/components/aiwindow/ui/actors/AITabChild.sys.mjs

source: browser/components/aiwindow/ui/actors/AITabChild.sys.mjs
source-hash: 4b884342ece3fbb456eaff8044694e98674f36c2
lines: 65

## <module>
- 役割: (未記入)

## AITabChild.handleEvent()
- 位置: L11-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `this.#query()`, `this.sendAsyncMessage()`
- 参照: `event.detail`, `event.type`

## AITabChild.#query()
- 位置: L33-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#respond()`, `this.sendQuery()`, `this.sendQuery(event.type, event.detail) .then()`
- 参照: `error.message`, `event.detail`, `event.type`

## AITabChild.#respond()
- 位置: L52-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `event.target.dispatchEvent()`
- 参照: `event.type`, `this.contentWindow`, `this.contentWindow.CustomEvent`
