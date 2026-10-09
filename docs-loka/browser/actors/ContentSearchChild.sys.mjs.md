# browser/actors/ContentSearchChild.sys.mjs

source: browser/actors/ContentSearchChild.sys.mjs
source-hash: 3012a16173f8bb3ab341515f00eea1f2726a9a7d
lines: 35

## <module>
- 役割: (未記入)

## ContentSearchChild.handleEvent()
- 位置: L6-12
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "ContentSearchClient")` → `this.sendAsyncMessage()`
- 参照: `event.detail.data`, `event.detail.type`, `event.type`

## ContentSearchChild.receiveMessage()
- 位置: L14-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._fireEvent()`
- 参照: `msg.data`, `msg.name`

## ContentSearchChild._fireEvent()
- 位置: L20-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `this.contentWindow.dispatchEvent()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`
