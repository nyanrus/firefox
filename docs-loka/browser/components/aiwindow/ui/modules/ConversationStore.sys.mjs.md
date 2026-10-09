# browser/components/aiwindow/ui/modules/ConversationStore.sys.mjs

source: browser/components/aiwindow/ui/modules/ConversationStore.sys.mjs
source-hash: 3b1b8977eead954285ac3b52d10992298afb9731
lines: 244

## <module>
- 役割: 会話の基本部分（Conversation とそのメッセージ）を SQLite に保存する ConversationStore を定義する。チャット用の ChatStore と並ぶ。

## ConversationStore.logPrefix()
- 位置: L51-53
- 役割: ログに付ける接頭辞を返す。
- 触るとき: ログの出どころを見分ける表示を変えるとき。

## ConversationStore.logLevelPref()
- 位置: L55-57
- 役割: このストアのログレベルを決める設定名を返す。
- 触るとき: ログレベルを個別に変えたいとき。

## ConversationStore.shutdownBlockerName()
- 位置: L59-61
- 役割: 終了時ブロッカーの名前を返す。
- 触るとき: 終了時の警告に出る名前を変えるとき。

## ConversationStore.CURRENT_SCHEMA_VERSION()
- 位置: L63-65
- 役割: このストアが想定するスキーマ版を返す。
- 触るとき: スキーマを変えて版を上げるとき。

## ConversationStore.databaseFileName()
- 位置: L67-69
- 役割: 保存先の DB ファイル名を返す。
- 触るとき: 保存先ファイル名を変えるとき。

## ConversationStore.prefBranch()
- 位置: L71-73
- 役割: 保存先などの設定の枝名を返す。
- 触るとき: 設定の名前空間を変えるとき。

## ConversationStore.createEntityStatements()
- 位置: L75-82
- 役割: 新規作成時に作る表と索引の SQL の配列を返す。
- 触るとき: 新しい表や索引を基本会話 DB に加えるとき。

## ConversationStore.migrations()
- 位置: L84-86
- 役割: 移行関数の配列を返す（現状は空）。
- 触るとき: 基本会話 DB の移行を最初に追加するとき。

## ConversationStore.updateConversation()
- 位置: async L95-145
- 役割: 会話と全メッセージを一つのトランザクションで保存する。消えたメッセージの行は削除し、残りを上書きする。
- 触るとき: 基本会話の保存項目や、メッセージを削除する条件を変えるとき。
- 呼び出し先: `Array.from()`, `JSON.stringify()`, `conversation.messages.map()`, `messages.map()`, `this.#ensureConnection()`, `this.connection .executeTransaction()`, `this.connection.executeCached()`, `this.log.error()`, `toJSONOrNull()`
- 条件付き依存: `if (messages.length)` → `this.connection.executeCached()`
- 参照: `conversation.createdDate`, `conversation.feature`, `conversation.id`, `conversation.securityProperties`, `conversation.seenUrls`, `conversation.serpUrlsForAnonymousFetch`, `conversation.updatedDate`, `e.message`, `e.stack`, `m.content`, `m.createdDate`, `m.id`, `m.message_id`, `m.modelId`, `m.ordinal`, `m.params`, `m.parentMessageId`, `m.role`, `m.toolCallId`, `m.toolName`, `m.turnIndex`, `m.usage`, `messages.length`

## ConversationStore.findConversationById()
- 位置: async L153-170
- 役割: ID で会話を読み、そのメッセージを付けて返す。無ければ null。
- 触るとき: 基本会話の読み込みで項目が欠ける問題を調べるとき。
- 呼び出し先: `messageRows.map()`, `this.#ensureConnection()`, `this.#parseMessageRow()`, `this.#parseRow()`, `this.connection.executeCached()`
- 参照: `conversation.messages`, `rows.length`

## ConversationStore.deleteConversationById()
- 位置: async L177-181
- 役割: ID の会話を削除する。メッセージは外部キーで連鎖して消える。
- 触るとき: 会話の削除で残骸が残る問題を調べるとき。
- 呼び出し先: `this.#ensureConnection()`, `this.connection.execute()`

## ConversationStore.#parseRow()
- 位置: L191-205
- 役割: 会話の行を Conversation に変換する。
- 触るとき: 会話の読み込み時の項目の対応を変えるとき。
- 呼び出し先: `parseJSONOrNull()`, `row.getResultByName()`

## ConversationStore.#parseMessageRow()
- 位置: L213-228
- 役割: メッセージの行を Message に変換する。
- 触るとき: メッセージの読み込みで項目が欠ける問題を調べるとき。
- 呼び出し先: `parseJSONOrNull()`, `row.getResultByName()`

## ConversationStore.#ensureConnection()
- 位置: async L230-239
- 役割: DB の接続を確保する。失敗時はログに出して例外を投げ直す。
- 触るとき: 各操作の前の接続確保の扱いを変えるとき。
- 呼び出し先: `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.log.error()`
- 参照: `e.message`, `e.stack`
