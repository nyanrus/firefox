# browser/components/aiwindow/ui/modules/ToolUITelemetry.sys.mjs

source: browser/components/aiwindow/ui/modules/ToolUITelemetry.sys.mjs
source-hash: 45f1b6594e7fff365251c3a08485dad4e5e3c6f4
lines: 120

## <module>
- 役割: AI Window のブラウザ操作(タブ管理ツールなど)の Glean テレメトリを記録するラッパー群。

## recordBrowserActionPrompt()
- 位置: L24-26
- 役割: ブラウザ操作の確認プロンプトが表示された時に browserActionPrompt を記録する。
- 触るとき: 確認プロンプトの表示イベントの項目を増減するとき、または表示件数が想定より少ないと調べるとき。
- 呼び出し先: `Glean.smartWindow.browserActionPrompt.record()`

## recordBrowserActionPromptResponse()
- 位置: L41-43
- 役割: ユーザーが確認プロンプトに応答(confirm/cancel)した時に browserActionPromptResponse を記録する。
- 触るとき: 確認・キャンセルの応答データがダッシュボードに届かないときに、このラッパーが呼ばれているか確認する。
- 呼び出し先: `Glean.smartWindow.browserActionPromptResponse.record()`

## recordBrowserActionUndo()
- 位置: L58-60
- 役割: ブラウザ操作の取り消し(undo)結果を browserActionUndo として記録する。
- 触るとき: undo の結果コードや復元タブ数の計測項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.browserActionUndo.record()`

## recordBrowserActionSubmit()
- 位置: L78-80
- 役割: モデルが manage_tabs などのツールを呼び出した送信時に browserActionSubmit を記録する。
- 触るとき: ツール呼び出しの送信データ(トリガー種別やタブ数)を追加・変更するとき。
- 呼び出し先: `Glean.smartWindow.browserActionSubmit.record()`

## recordBrowserActionComplete()
- 位置: L100-102
- 役割: モデル起因の操作が成功・失敗・キャンセルで終わった時に browserActionComplete を記録する。
- 触るとき: 操作の完了結果の集計がずれたとき、result の値域を変えるとき。
- 呼び出し先: `Glean.smartWindow.browserActionComplete.record()`

## browserActionResult()
- 位置: L112-118
- 役割: 成功したタブ数と要求数から complete 用の result 値(success / partial_success / error)を決める。
- 触るとき: 部分的な成功の扱いを変えるとき、または result が想定と違うと調べるとき。
- 呼び出し先: `Math.max()`
