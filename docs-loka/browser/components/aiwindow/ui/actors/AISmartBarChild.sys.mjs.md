# browser/components/aiwindow/ui/actors/AISmartBarChild.sys.mjs

source: browser/components/aiwindow/ui/actors/AISmartBarChild.sys.mjs
source-hash: e6949695361b3383b1d98215c14b794f2f35b5e3
lines: 43

## <module>
- 役割: urlbar 側から届いた smartbar への問い合わせを、コンテンツ文書の smartbar-commit イベントに変換する子アクター。

## AISmartBarChild.receiveMessage()
- 位置: L16-41
- 役割: AskFromParent を受けると、送信内容を detail に詰めた smartbar-commit イベントを作り、文書に発火する。action は常に "chat" に固定される。
- 触るとき: urlbar から AI チャットへの送信が smartbar 側に届かないとき、または detail のフィールド(contextMentions など)が欠けるときに見る。
- 条件付き依存: `if (msg.name === "AskFromParent")` → `this.contentWindow.document.dispatchEvent()`
- 参照: `msg.data`, `msg.name`, `this.contentWindow.CustomEvent`
