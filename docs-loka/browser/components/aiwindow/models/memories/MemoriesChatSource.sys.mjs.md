# browser/components/aiwindow/models/memories/MemoriesChatSource.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesChatSource.sys.mjs
source-hash: ea68aced2fbc1bc8760352539753896284f079b6
lines: 161

## <module>
- 役割: (未記入)
- 呼び出し先: `BlockListManager.initializeFromDefault()`

## getRecentChats()
- 位置: async L52-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChatStore.findMessagesByDate()`, `_mgr.matchAtWordBoundary()`, `_sensitiveInfoDetector.containsSensitiveInfo()`, `_sensitiveInfoDetector.containsSensitiveKeywords()`, `body.toLowerCase()`, `computeFreshnessScore()`, `filtered.map()`, `messages.filter()`
- 条件付き依存: `if (content && content.length > MESSAGE_LENGTH_THRESHOLD)` → `content.substring()`
- 参照: `MESSAGE_ROLE.USER`, `content.length`, `msg.content?.body`, `msg.convId`, `msg.createdDate`, `msg.pageUrl`, `msg.role`

## computeFreshnessScore()
- 位置: L118-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.exp()`, `Math.max()`, `Math.min()`, `createdDate.getTime()`
- 参照: `Math.LN2`

## _setBlockListManagerForTesting()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)

## getConversationsById()
- 位置: async L145-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChatStore.findConversationById()`, `Promise.all()`, `conversationIds.map()`, `conversations.filter()`

## getConversationSourceIdsFromMemory()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `memory.source_ids?.conversation_source_ids`
