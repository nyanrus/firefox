# browser/components/aiwindow/models/memories/MemoriesSessions.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesSessions.sys.mjs
source-hash: 922327c1818e8795efa6b564685d5030894fad6d
lines: 201

## <module>
- 役割: (未記入)

## buildSessions()
- 位置: L85-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Number.isFinite()`, `events.push()`, `events.sort()`, `getMessageTimestampMs()`, `sessions.map()`
- 条件付き依存: `if (needNew)` → `sessions.push()`
- 条件付き依存: `if (row.title)` → `cur._titles.add()`
- 条件付き依存: `if (row.urlHash != null)` → `cur._urlHashes.add()`
- 条件付き依存: `if (row.domain)` → `cur._domains.add()`
- 条件付き依存: `if (queryText)` → `cur._queries.add()`
- 条件付き依存: `if (!(ev.kind === KIND_SEARCH))` → `cur.chats.push()`
- 条件付き依存: `if (!(ev.kind === KIND_SEARCH))` → `cur._convIds.add()`
- 参照: `a.timestampMs`, `b.timestampMs`, `cur._lastMs`, `cur._searchCount`, `cur._totalViewTimeMs`, `cur._visitCount`, `cur.session_end_ms`, `cur.session_start_ms`, `ev.kind`, `ev.row`, `ev.timestampMs`, `msg.convId`, `opts.gapSec`, `opts.maxSessionSec`, `row.convId`, `row.domain`, `row.searchQuery`, `row.source`, `row.title`, `row.totalViewTimeMs`, `row.urlHash`, `row.visitDateMicros`, `s._convIds`, `s._domains`, `s._queries`, `s._searchCount`, `s._titles`, `s._totalViewTimeMs`, `s._urlHashes`, `s._visitCount`, `s.chats`, `s.chats.length`, `s.session_end_ms`, `s.session_id`, `s.session_start_ms`

## getMessageTimestampMs()
- 位置: L196-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `msg.createdDate?.getTime()`
- 参照: `msg.createdDate`
