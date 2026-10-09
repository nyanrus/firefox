# browser/actors/PageStyleChild.sys.mjs

source: browser/actors/PageStyleChild.sys.mjs
source-hash: 3970d010b05abff61aad4fa325c0931491e6ec82
lines: 200

## <module>
- 役割: (未記入)

## PageStyleChild.actorCreated()
- 位置: L6-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectAndSendSheets()`
- 参照: `document.readyState`, `this.browsingContext`, `this.browsingContext.associatedWindow`

## PageStyleChild.handleEvent()
- 位置: L25-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectAndSendSheets()`
- 条件付き依存: `if (this.browsingContext.top === this.browsingContext)` → `this.sendAsyncMessage()`
- 参照: `event?.type`, `this.browsingContext`, `this.browsingContext.top`

## PageStyleChild.receiveMessage()
- 位置: L40-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._switchStylesheet()`
- 参照: `msg.data.title`, `msg.name`, `this.browsingContext`, `this.browsingContext.authorStyleDisabledDefault`, `this.browsingContext.top`, `this.docShell.docViewer.authorStyleDisabled`

## PageStyleChild._collectLinks()
- 位置: L63-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(link.relList).some()`, `document.querySelectorAll()`, `r.toLowerCase()`, `result.push()`
- 参照: `link.href`, `link.namespaceURI`, `link.relList`

## PageStyleChild._switchStylesheet()
- 位置: L86-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`
- 条件付き依存: `if (title)` → `this._collectLinks()`
- 条件付き依存: `if (title)` → `docStyleSheets.some()`
- 条件付き依存: `if (title)` → `links.some()`
- 参照: `document.styleSheets`, `link.disabled`, `link.title`, `sheet.disabled`, `sheet.title`, `this.document`

## PageStyleChild.#collectAndSendSheets()
- 位置: L127-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectStyleSheets()`, `this.sendAsyncMessage()`, `window.requestIdleCallback()`
- 参照: `this.browsingContext.associatedWindow`, `this.document.preferredStyleSheetSet`, `window.closed`

## PageStyleChild.#collectStyleSheets()
- 位置: L147-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.matchMedia()`, `result.push()`, `sheet.ownerNode.nodeName.toLowerCase()`, `this._collectLinks()`
- 参照: `content.document`, `content.matchMedia(media).matches`, `document.preferredStyleSheetSet`, `document.styleSheets`, `link.disabled`, `link.media`, `link.sheet?.disabled`, `link.title`, `sheet.disabled`, `sheet.href`, `sheet.media.mediaText`, `sheet.ownerNode`, `sheet.title`
