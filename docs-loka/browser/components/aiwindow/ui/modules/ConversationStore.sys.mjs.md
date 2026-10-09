# browser/components/aiwindow/ui/modules/ConversationStore.sys.mjs

source: browser/components/aiwindow/ui/modules/ConversationStore.sys.mjs
source-hash: 3b1b8977eead954285ac3b52d10992298afb9731
lines: 244

## <module>
- 役割: (未記入)

## ConversationStore.logPrefix()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.logLevelPref()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.shutdownBlockerName()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.CURRENT_SCHEMA_VERSION()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.databaseFileName()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.prefBranch()
- 位置: L71-73
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.createEntityStatements()
- 位置: L75-82
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.migrations()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)

## ConversationStore.updateConversation()
- 位置: async L95-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `JSON.stringify()`, `conversation.messages.map()`, `messages.map()`, `this.#ensureConnection()`, `this.connection .executeTransaction()`, `this.connection.executeCached()`, `this.log.error()`, `toJSONOrNull()`
- 条件付き依存: `if (messages.length)` → `this.connection.executeCached()`
- 参照: `conversation.createdDate`, `conversation.feature`, `conversation.id`, `conversation.securityProperties`, `conversation.seenUrls`, `conversation.serpUrlsForAnonymousFetch`, `conversation.updatedDate`, `e.message`, `e.stack`, `m.content`, `m.createdDate`, `m.id`, `m.message_id`, `m.modelId`, `m.ordinal`, `m.params`, `m.parentMessageId`, `m.role`, `m.toolCallId`, `m.toolName`, `m.turnIndex`, `m.usage`, `messages.length`

## ConversationStore.findConversationById()
- 位置: async L153-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messageRows.map()`, `this.#ensureConnection()`, `this.#parseMessageRow()`, `this.#parseRow()`, `this.connection.executeCached()`
- 参照: `conversation.messages`, `rows.length`

## ConversationStore.deleteConversationById()
- 位置: async L177-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureConnection()`, `this.connection.execute()`

## ConversationStore.#parseRow()
- 位置: L191-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseJSONOrNull()`, `row.getResultByName()`

## ConversationStore.#parseMessageRow()
- 位置: L213-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseJSONOrNull()`, `row.getResultByName()`

## ConversationStore.#ensureConnection()
- 位置: async L230-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.log.error()`
- 参照: `e.message`, `e.stack`
