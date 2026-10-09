# browser/components/aiwindow/models/memories/MemoriesSessionGate.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesSessionGate.sys.mjs
source-hash: 00dcfcf79952fdd02d0430af725b63f6a9b57f7a
lines: 128

## <module>
- 役割: セッション束をLLMの記憶パイプラインに渡す前に、構造上内容が無いと分かるセッションを捨てるヒューリスティックゲート。

## runHeuristicGate()
- 位置: L48-74
- 役割: セッションを閲覧側とチャット側に分けて判定し、両方がスキップ相当の時だけKEEPかSKIPを返す。
- 触るとき: セッションが記憶対象から落ちた理由を知りたいとき、またはKEEP/SKIPの方針(片方でも通すか)を変えたいとき。
- 呼び出し先: `checkBrowse()`, `checkChat()`
- 参照: `session.chat_count`, `session.search_count`, `session.visit_count`

## checkBrowse()
- 位置: L76-115
- 役割: 閲覧履歴の検索クエリ数とドメイン・タイトルから、検索エンジンだけ、認証や短縮URLだけ、意味あるタイトルも無い、の3条件で閲覧分をスキップ判定する。
- 触るとき: 検索エンジンのみの閲覧や認証画面だけのセッションが記憶に残る/残らないの判断を調整するとき。
- 呼び出し先: `SEARCH_ENGINE_DOMAINS.has()`, `SKIP_ONLY_DOMAINS.has()`, `domains.every()`
- 条件付き依存: `if (queryCount === 0)` → `session.titles.filter()`
- 条件付き依存: `if (queryCount === 0)` → `GENERIC_TITLES.has()`
- 条件付き依存: `if (queryCount === 0)` → `NAV_TITLE_PATTERNS.some()`
- 条件付き依存: `if (queryCount === 0)` → `re.test()`
- 参照: `domains.length`, `meaningfulTitles.length`, `session.domains`, `session.search_queries.length`, `t.length`

## checkChat()
- 位置: L117-127
- 役割: チャットの各メッセージを小文字化して、最小長以上で定型語(hi、thanksなど)でないものが1件もなければスキップ判定する。
- 触るとき: 挨拶だけのチャットを記憶対象から外す基準を変えるとき、TRIVIAL_MESSAGESや最小文字数を見直すとき。
- 呼び出し先: `TRIVIAL_MESSAGES.has()`, `msg.content.trim()`, `msg.content.trim().toLowerCase()`, `session.chats.some()`
- 参照: `body.length`, `msg.content`
