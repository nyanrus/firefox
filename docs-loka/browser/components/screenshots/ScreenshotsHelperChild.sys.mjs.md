# browser/components/screenshots/ScreenshotsHelperChild.sys.mjs

source: browser/components/screenshots/ScreenshotsHelperChild.sys.mjs
source-hash: 550c3fb13c728f99b2eafc4d3a994d2706337278
lines: 48

## <module>
- 役割: (未記入)

## ScreenshotsHelperChild.receiveMessage()
- 位置: L17-22
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name === "ScreenshotsHelper:GetElementRectFromPoint")` → `this.getBestElementRectFromPoint()`
- 参照: `message.data`, `message.name`

## ScreenshotsHelperChild.getBestElementRectFromPoint()
- 位置: async L24-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getElementFromPoint()`
- 条件付き依存: `if (!rect)` → `getBestRectForElement()`
- 参照: `rect.bottom`, `rect.left`, `rect.right`, `rect.top`, `this.contentWindow.mozInnerScreenX`, `this.contentWindow.mozInnerScreenY`, `this.document`
