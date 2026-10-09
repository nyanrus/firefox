# browser/actors/RefreshBlockerParent.sys.mjs

source: browser/actors/RefreshBlockerParent.sys.mjs
source-hash: a68077c3a9164c023ecdaeb49ad3ab8c2617db38
lines: 18

## <module>
- 役割: リフレッシュ阻止の通知を受け、タブの gBrowser に伝える親側アクター。

## RefreshBlockerParent.receiveMessage()
- 位置: L6-16
- 役割: RefreshBlocker:Blocked を受け、トップのタブ要素の gBrowser.refreshBlocked に渡す。
- 触るとき: 阻止通知の受け先や渡す情報を変えるとき。
- 条件付き依存: `if (gBrowser)` → `gBrowser.refreshBlocked()`
- 参照: `browser.documentGlobal.gBrowser`, `message.data`, `message.name`, `this.browsingContext.top.embedderElement`
