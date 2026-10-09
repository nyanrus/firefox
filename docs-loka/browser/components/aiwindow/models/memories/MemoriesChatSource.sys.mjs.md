# browser/components/aiwindow/models/memories/MemoriesChatSource.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesChatSource.sys.mjs
source-hash: ea68aced2fbc1bc8760352539753896284f079b6
lines: 161

## <module>
- 役割: ChatStoreからユーザーの発話を取り出し、記憶生成の入力になる形(鮮度スコア付き)に整える。
- 呼び出し先: `BlockListManager.initializeFromDefault()`

## getRecentChats()
- 位置: async L52-100
- 役割: 指定時刻以降のユーザー発話を最大件数まで取得し、ブロックリストと機微情報で除外してから、長さ上限で切って鮮度スコアを付ける。
- 触るとき: 記憶生成に入るチャットが少ない、または機微な発話が混ざると調べるとき。取得件数や半減期を変えるときも見る。
- 呼び出し先: `ChatStore.findMessagesByDate()`, `_mgr.matchAtWordBoundary()`, `_sensitiveInfoDetector.containsSensitiveInfo()`, `_sensitiveInfoDetector.containsSensitiveKeywords()`, `body.toLowerCase()`, `computeFreshnessScore()`, `filtered.map()`, `messages.filter()`
- 条件付き依存: `if (content && content.length > MESSAGE_LENGTH_THRESHOLD)` → `content.substring()`
- 参照: `MESSAGE_ROLE.USER`, `content.length`, `msg.content?.body`, `msg.convId`, `msg.createdDate`, `msg.pageUrl`, `msg.role`

## computeFreshnessScore()
- 位置: L118-133
- 役割: メッセージの経過日数から半減期の指数減衰で鮮度を0から1の範囲で求める。未来や現在の発話は1を返す。
- 触るとき: 古い発話を記憶生成でどれだけ軽く扱うかを変えるとき、半減期の既定値を見直すとき。
- 呼び出し先: `Date.now()`, `Math.exp()`, `Math.max()`, `Math.min()`, `createdDate.getTime()`
- 参照: `Math.LN2`

## _setBlockListManagerForTesting()
- 位置: L135-137
- 役割: テスト用にブロックリストマネージャーを差し替える。
- 触るとき: ブロックリストの判定を含む単体テストを書くとき。

## getConversationsById()
- 位置: async L145-150
- 役割: 会話IDの一覧からChatStoreの会話を並列に取得し、見つからないものを除く。
- 触るとき: 記憶の根拠になった会話の本文を後から引き直す処理を調べるとき。
- 呼び出し先: `ChatStore.findConversationById()`, `Promise.all()`, `conversationIds.map()`, `conversations.filter()`

## getConversationSourceIdsFromMemory()
- 位置: L158-160
- 役割: 記憶オブジェクトのsource_idsから会話ソースIDの配列を取り出す。無ければ空配列を返す。
- 触るとき: 会話削除時に関連する記憶を見つける処理を調べるとき、source_idsの形を変えるとき。
- 参照: `memory.source_ids?.conversation_source_ids`
