# browser/actors/PageInfoPreviewChild.sys.mjs

source: browser/actors/PageInfoPreviewChild.sys.mjs
source-hash: 1c7279829757d94dde973c4e79b42e22014a8d86
lines: 38

## <module>
- 役割: (未記入)

## PageInfoPreviewChild.receiveMessage()
- 位置: async L6-12
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name === "PageInfoPreview:resize")` → `this.resize()`
- 参照: `message.data`, `message.name`, `this.contentWindow.document`

## PageInfoPreviewChild.resize()
- 位置: L14-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 参照: `data.height`, `data.width`, `img.height`, `img.naturalHeight`, `img.naturalWidth`, `img.width`
