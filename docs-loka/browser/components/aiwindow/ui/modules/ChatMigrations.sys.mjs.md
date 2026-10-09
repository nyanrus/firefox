# browser/components/aiwindow/ui/modules/ChatMigrations.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatMigrations.sys.mjs
source-hash: e988d2acf016fb11a48cc71222ca61dda667024b
lines: 252

## <module>
- 役割: チャット DB のスキーマ移行（バージョン 2〜12）を並べた配列を定義する。ChatStore.applyMigrations が順に呼ぶ。

## applyV2()
- 位置: async L25-29
- 役割: 会話 ID 付きのメッセージ索引を作る。
- 触るとき: 会話ごとのメッセージ取得が遅い、または索引が無い環境で検索が遅いと調べるとき。
- 条件付き依存: `if (version < 2)` → `conn.execute()`

## getColumns()
- 位置: async L42-45
- 役割: PRAGMA table_info で表の列名の集合を返す。
- 触るとき: 移行で列の有無を見て二重追加を避ける処理を新しく書くとき。
- 呼び出し先: `columns.map()`, `conn.execute()`
- 参照: `c.name`

## applyV3()
- 位置: async L48-69
- 役割: message 表の insights 系の列を memories 系の名前に改名する。
- 触るとき: 記憶機能の列名を読む箇所を調べるとき、または古い DB の列名が残る問題を見るとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV4()
- 位置: async L73-86
- 役割: message 表に page_history_deleted 列を追加する。
- 触るとき: ページ URL の履歴削除の扱いを変えるとき、または列が無いことによる読み込み失敗を調べるとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV5()
- 位置: async L89-102
- 役割: conversation 表に security_properties_jsonb 列を追加する。
- 触るとき: 会話のセキュリティ状態の保存形式を変えるとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV6()
- 位置: async L105-118
- 役割: conversation 表に seen_urls_jsonb 列を追加する。
- 触るとき: 既読 URL の永続化を変えるとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV7()
- 位置: async L121-157
- 役割: conversation 表に memories_toggled 列を追加し、直近のユーザー発言の値で埋める。
- 触るとき: 記憶のオン・オフの既定値の決まり方を変えるとき、または移行後の値が合わない問題を調べるとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV8()
- 位置: async L161-172
- 役割: message 表に tool_ui_data_jsonb 列を追加する。
- 触るとき: ツール UI データの保存先を変えるとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV9()
- 位置: async L175-181
- 役割: LLM テレメトリ用の表を作る。
- 触るとき: LLM 呼び出しのテレメトリ項目を変えるとき。
- 呼び出し先: `conn.execute()`

## applyV10()
- 位置: async L184-197
- 役割: conversation 表に serp_urls_for_anonymous_fetch_jsonb 列を追加する。
- 触るとき: 匿名取得用の検索結果 URL の保存を変えるとき。
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV11()
- 位置: async L201-218
- 役割: ツール結果用の表を作り、既存の tool_ui_data を移し替える。
- 触るとき: ツール結果の保存形式を変えるとき、または移行後にツール UI が欠ける問題を調べるとき。
- 呼び出し先: `conn.execute()`

## applyV12()
- 位置: async L223-232
- 役割: メッセージの親 ID・版の根・日付と役割の索引を作り、未使用の ordinal 索引を削除する。
- 触るとき: メッセージの削除や検索が遅い問題を索引の面から調べるとき。
- 呼び出し先: `conn.execute()`
