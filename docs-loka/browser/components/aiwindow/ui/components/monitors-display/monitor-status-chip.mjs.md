# browser/components/aiwindow/ui/components/monitors-display/monitor-status-chip.mjs

source: browser/components/aiwindow/ui/components/monitors-display/monitor-status-chip.mjs
source-hash: d25bfc284b7438b2bbb75d4856a3a62ad9cde3b4
lines: 41

## <module>
- 役割: 監視が監視中か一時停止かを示すピル型の表示 monitor-status-chip を定義するモジュール。
- 呼び出し先: `customElements.define()`

## MonitorStatusChip.render()
- 位置: L26-37
- 役割: kind に対応する状態の Fluent ID があれば span に入れて描き、無ければ何も描かない。スタイルシートは常に読み込む。
- 触るとき: 状態の文言の出し分けを変えるとき、または想定外の kind を渡したときの表示を確認するとき。
- 呼び出し先: `html()`
- 参照: `this.kind`
