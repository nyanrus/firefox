# browser/components/places/InteractionsParent.sys.mjs

source: browser/components/places/InteractionsParent.sys.mjs
source-hash: cd781e0fab96a497663cdb6c38c96b6fde47b9b3
lines: 38

## <module>
- 役割: Interactions の子アクターからの通知を受け、タブ単位のインタラクション記録へ渡す親側の JSWindowActor。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## InteractionsParent.receiveMessage()
- 位置: L16-36
- 役割: Interactions:PageLoaded は registerNewInteraction へ、Interactions:PageHide は registerEndOfInteraction へ振り分ける。
- 触るとき: 子プロセスから送られるメッセージ名や渡すデータ(referrer など)を変えるとき、タブを閉じた後の離脱通知が欠ける問題を調べるとき。
- 呼び出し先: `lazy.Interactions.registerEndOfInteraction()`, `lazy.Interactions.registerNewInteraction()`
- 参照: `msg.data.referrer`, `msg.name`, `this.browsingContext.embedderElement`, `this.browsingContext.isActive`, `this.browsingContext?.embedderElement`, `this.manager.documentURI.specIgnoringRef`
