# browser/components/shell/ScreenshotChild.sys.mjs

source: browser/components/shell/ScreenshotChild.sys.mjs
source-hash: 994cb1a27e657bc97382f680a5675d2930461b90
lines: 32

## <module>
- 役割: (未記入)

## ScreenshotChild.receiveMessage()
- 位置: L6-11
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name == "GetDimensions")` → `this.getDimensions()`
- 参照: `message.name`

## ScreenshotChild.getDimensions()
- 位置: async L13-30
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.document.readyState != "complete")` → `this.contentWindow.addEventListener()`
- 参照: `contentWindow.innerHeight`, `contentWindow.innerWidth`, `contentWindow.scrollMaxX`, `contentWindow.scrollMaxY`, `contentWindow.scrollMinX`, `contentWindow.scrollMinY`, `this.document.readyState`
