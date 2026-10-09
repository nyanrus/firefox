# browser/components/aiwindow/models/Message.sys.mjs

source: browser/components/aiwindow/models/Message.sys.mjs
source-hash: 9cf6d7cf037ba5f3df2d20d68cf1e126a0d5dbe6
lines: 79

## <module>
- 役割: Conversation の 1 ターン分にあたる汎用 LLM メッセージのクラス Message を定義し、役割・内容・順序番号・ツール呼び出しの対応づけを保持する。

## Message.constructor()
- 位置: L42-68
- 役割: 必須の ordinal・role・content・turnIndex を受け取り、id と作成日時を自動で補って各フィールドに設定する。
- 触るとき: メッセージに新しい項目を持たせるとき、またはメッセージの既定値(親 ID や usage など)を変えるとき。
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`
- 参照: `this.content`, `this.createdDate`, `this.id`, `this.modelId`, `this.ordinal`, `this.params`, `this.parentMessageId`, `this.role`, `this.toolCallId`, `this.toolName`, `this.turnIndex`, `this.usage`

## Message.addTokens()
- 位置: L77-77
- 役割: 何もしない既定のフック。派生クラス(ChatMessage)が検索や記憶のトークンを処理するため上書きする。
- 触るとき: トークンの副作用をメッセージ種別ごとに変えたいとき、ChatMessage 側の実装を探すとき。
