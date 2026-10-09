# browser/components/aiwindow/models/Conversation.sys.mjs

source: browser/components/aiwindow/models/Conversation.sys.mjs
source-hash: 2c4e48cf2993f2d0102e119a5b1df9e2e49ba2ad
lines: 523

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`

## Conversation.constructor()
- 位置: L113-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`
- 条件付き依存: `if (securityProperties != null)` → `SecurityProperties.fromJSON()`
- 参照: `this.#messages`, `this.createdDate`, `this.engine`, `this.feature`, `this.id`, `this.parameters`, `this.securityProperties`, `this.seenUrls`, `this.serpUrlsForAnonymousFetch`, `this.updatedDate`

## Conversation.messages()
- 位置: L146-148
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#messages`

## Conversation.messages()
- 位置: L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#messages`

## Conversation.messageCount()
- 位置: L154-156
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#messages.length`

## Conversation.save()
- 位置: async L166-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ConversationStore.updateConversation()`
- 参照: `this.constructor`, `this.constructor.name`

## Conversation.isReady()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.engine?.engineInstance?.engineStatus`

## Conversation.currentTurnIndex()
- 位置: L185-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#messages.reduce()`
- 参照: `message.turnIndex`

## Conversation.systemPromptVersion()
- 位置: L197-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messages.find()`
- 参照: `MESSAGE_ROLE.SYSTEM`, `m.role`, `sysMsg?.content?.version`

## Conversation.addMessage()
- 位置: L211-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#messages.map()`, `this.#messages.push()`, `this._createMessage()`
- 参照: `m.ordinal`, `this.#messages`, `this.#messages.length`, `this.#messages[this.#messages.length - 1].id`, `this._minNextOrdinal`

## Conversation._createMessage()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)

## Conversation.addUserMessage()
- 位置: L239-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.USER`

## Conversation.addAssistantMessage()
- 位置: L247-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `opts.tool_calls`

## Conversation.setSystemMessage()
- 位置: L271-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messages.unshift()`, `this._createMessage()`
- 参照: `MESSAGE_ROLE.SYSTEM`, `this.#messages`, `this.#messages[0].content`, `this.#messages[0]?.role`

## Conversation.addToolMessage()
- 位置: L288-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.TOOL`

## Conversation.removeLastMessage()
- 位置: L297-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messages.pop()`

## Conversation.clearMessages()
- 位置: L301-303
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#messages`

## Conversation.replaceMessages()
- 位置: L305-307
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#messages`

## Conversation.retryMessage()
- 位置: L316-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#messages.findIndex()`, `this.#messages.map()`, `this.#messages.splice()`
- 参照: `m.id`, `m.ordinal`, `message.id`, `this._minNextOrdinal`

## Conversation.compactChatCompletions()
- 位置: L332-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `compactMessages()`, `this.getMessagesInChatCompletionsFormat()`

## Conversation.getMessagesInChatCompletionsFormat()
- 位置: L341-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messages.map()`
- 条件付き依存: `if (msg.role === "tool")` → `JSON.stringify()`
- 参照: `bodyOrContent.tool_calls`, `message.content`, `message.content?.body`, `message.content?.name`, `message.content?.tool_call_id`, `message.role`, `message.toolCallId`, `message.toolName`, `msg.content`, `msg.name`, `msg.role`, `msg.tool_call_id`, `msg.tool_calls`

## Conversation.handleChunk()
- 位置: L378-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `consumeStreamChunk()`
- 条件付き依存: `if (tokens)` → `currentMessage?.addTokens()`
- 参照: `currentMessage.content.body`, `currentMessage?.content`

## Conversation.receiveResponse()
- 位置: async L400-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createParserState()`, `flushTokenRemainder()`
- 条件付き依存: `if (chunk.text)` → `this.handleChunk()`
- 参照: `chunk.text`, `chunk.toolCalls`, `chunk?.toolCalls?.length`, `chunk?.usage`, `currentMessage.content.body`, `currentMessage?.content`

## Conversation.run()
- 位置: async L439-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engine.run()`, `this.getMessagesInChatCompletionsFormat()`, `this.securityProperties.commit()`
- 参照: `opts.inferenceParams`, `this.parameters`

## Conversation.runWithGenerator()
- 位置: L456-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engine.runWithGenerator()`, `this.getMessagesInChatCompletionsFormat()`, `this.securityProperties.commit()`
- 参照: `opts.args`, `opts.inferenceParams`, `this.parameters`

## Conversation.toJSON()
- 位置: L467-475
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#messages`, `this.createdDate`, `this.feature`, `this.id`, `this.updatedDate`

## Conversation.addSeenUrls()
- 位置: L482-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.seenUrls.add()`

## Conversation.addSerpUrlsForAnonymousFetch()
- 位置: L493-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.serpUrlsForAnonymousFetch.add()`

## Conversation.getAllMentionURLs()
- 位置: L507-521
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (url && !groupId)` → `mentionUrls.add()`
- 参照: `message.content`, `this.messages`
