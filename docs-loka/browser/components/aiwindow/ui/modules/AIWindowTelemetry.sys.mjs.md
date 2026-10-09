# browser/components/aiwindow/ui/modules/AIWindowTelemetry.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowTelemetry.sys.mjs
source-hash: 4bcf2b984a5be18a7639f9fb0137686777d95a21
lines: 44

## <module>
- 役割: Smart Window の計測呼び出しをまとめる。現在は履歴グリッドの操作を Glean に記録する。

## recordHistoryGridEvent()
- 位置: L18-42
- 役割: 履歴グリッドの描画イベントなら historyDisplayed を、項目クリックなら historyClick を、会話 id やメッセージ数などを添えて記録する。
- 触るとき: 履歴グリッドの計測項目や値を変えるとき、どの操作でどのイベントが送られるかを調べるとき。
- 呼び出し先: `Glean.smartWindow.historyClick.record()`, `Glean.smartWindow.historyDisplayed.record()`
- 参照: `aiWindow.conversationId`, `aiWindow.conversationMessageCount`, `aiWindow.mode`, `item.resultCount`, `item.resultIndex`
