# browser/actors/RefreshBlockerParent.sys.mjs

source: browser/actors/RefreshBlockerParent.sys.mjs
source-hash: a68077c3a9164c023ecdaeb49ad3ab8c2617db38
lines: 18

## <module>
- 役割: (未記入)

## RefreshBlockerParent.receiveMessage()
- 位置: L6-16
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gBrowser)` → `gBrowser.refreshBlocked()`
- 参照: `browser.documentGlobal.gBrowser`, `message.data`, `message.name`, `this.browsingContext.top.embedderElement`
