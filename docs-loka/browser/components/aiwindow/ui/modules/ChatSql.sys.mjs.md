# browser/components/aiwindow/ui/modules/ChatSql.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatSql.sys.mjs
source-hash: 896b988b9bd3f7a8ff963090f7815d13c1702152
lines: 612

## <module>
- 役割: チャット DB の SQL 文（表・索引の定義、会話とメッセージの取得・削除、テレメトリ）を集めたモジュール。

## getConversationMessagesSql()
- 位置: L333-348
- 役割: 指定件数の会話 ID に属するメッセージを、ordinal 順に復元用の列付きで取得する SQL を返す。
- 触るとき: 会話を読み込んだときに取得する列を増やす・並びを変えるとき、またはメッセージの項目が欠ける問題を調べるとき。
- 呼び出し先: `new Array(amount).fill()`, `new Array(amount).fill("?").join()`

## getDeleteMessagesByIdsSql()
- 位置: L350-354
- 役割: 指定件数のプレースホルダを持つメッセージ削除の SQL を返す。
- 触るとき: メッセージ削除の対象の絞り込みを変えるとき。
- 呼び出し先: `new Array(amount).fill()`, `new Array(amount).fill("?").join()`

## getDeleteConversationsByIdsSql()
- 位置: L356-361
- 役割: 指定件数のプレースホルダを持つ会話削除の SQL を返す。
- 触るとき: 会話の一括削除で対象がずれる問題を調べるとき。
- 呼び出し先: `new Array(amount).fill()`, `new Array(amount).fill("?").join()`

## getDeleteEmptyConversationsSql()
- 位置: L363-373
- 役割: メッセージを一件も持たない会話だけを、指定 ID の中から削除する SQL を返す。
- 触るとき: メッセージが残っている会話を誤って消さないよう条件を変えるとき。
- 呼び出し先: `new Array(amount).fill()`, `new Array(amount).fill("?").join()`

## getUniformSamplingByConvIdsSql()
- 位置: L582-588
- 役割: 指定会話の llm_telemetry からサンプリング確率を取得する SQL を返す。
- 触るとき: 会話の再読み込み後にテレメトリのサンプリング状態が引き継がれない問題を調べるとき。
- 呼び出し先: `new Array(amount).fill()`, `new Array(amount).fill("?").join()`
