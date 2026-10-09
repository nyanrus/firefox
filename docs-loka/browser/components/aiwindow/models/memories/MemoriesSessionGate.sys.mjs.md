# browser/components/aiwindow/models/memories/MemoriesSessionGate.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesSessionGate.sys.mjs
source-hash: 00dcfcf79952fdd02d0430af725b63f6a9b57f7a
lines: 128

## <module>
- 役割: (未記入)

## runHeuristicGate()
- 位置: L48-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkBrowse()`, `checkChat()`
- 参照: `session.chat_count`, `session.search_count`, `session.visit_count`

## checkBrowse()
- 位置: L76-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SEARCH_ENGINE_DOMAINS.has()`, `SKIP_ONLY_DOMAINS.has()`, `domains.every()`
- 条件付き依存: `if (queryCount === 0)` → `session.titles.filter()`
- 条件付き依存: `if (queryCount === 0)` → `GENERIC_TITLES.has()`
- 条件付き依存: `if (queryCount === 0)` → `NAV_TITLE_PATTERNS.some()`
- 条件付き依存: `if (queryCount === 0)` → `re.test()`
- 参照: `domains.length`, `meaningfulTitles.length`, `session.domains`, `session.search_queries.length`, `t.length`

## checkChat()
- 位置: L117-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TRIVIAL_MESSAGES.has()`, `msg.content.trim()`, `msg.content.trim().toLowerCase()`, `session.chats.some()`
- 参照: `body.length`, `msg.content`
