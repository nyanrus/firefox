# browser/components/aiwindow/ui/components/monitors-display/monitors-display.mjs

source: browser/components/aiwindow/ui/components/monitors-display/monitors-display.mjs
source-hash: a21c9a235c3382453aee9ec1d311b88e57eab34c
lines: 123

## <module>
- 役割: 監視の一覧を agent-monitor-item の並びとして描く monitors-display を定義するモジュール。
- 呼び出し先: `customElements.define()`

## MonitorsDisplay.constructor()
- 位置: L27-33
- 役割: monitors・scheduleTypes・weekdays を空、canResume を true にして初期化する。
- 触るとき: 初期値を変えるとき、または再開ボタンが最初から有効に見える理由を調べるとき。
- 呼び出し先: `super()`
- 参照: `this.canResume`, `this.monitors`, `this.scheduleTypes`, `this.weekdays`

## MonitorsDisplay.buildMonitorStatus()
- 位置: L35-42
- 役割: enabled が真なら watching、偽なら paused の状態オブジェクトを返す。
- 触るとき: 監視の有効・停止の判定基準を変えるとき。
- 参照: `monitor.enabled`

## MonitorsDisplay.transformMonitorToAgent()
- 位置: L50-75
- 役割: 監視データを agent-monitor-item の形に変換する。名前の既定値、先頭の監視 URL、履歴の逆順、時分を2桁にした予定を組み立てる。
- 触るとき: 一覧に出す項目や予定の表記を変えるとき、または DB のフィールド名を変えた影響を確認するとき。
- 呼び出し先: `(monitor.history || []).slice()`, `(monitor.history || []).slice().reverse()`, `(monitor.schedule.hour ?? 0) .toString()`, `(monitor.schedule.hour ?? 0) .toString() .padStart()`, `(monitor.schedule.minute ?? 0) .toString()`, `(monitor.schedule.minute ?? 0) .toString() .padStart()`, `monitor.schedule.weekday?.toString()`, `this.buildMonitorStatus()`
- 参照: `monitor.history`, `monitor.id`, `monitor.monitorPrompt`, `monitor.schedule`, `monitor.schedule.hour`, `monitor.schedule.minute`, `monitor.schedule.type`, `monitor.title`, `monitor.watchUrlTitles`, `monitor.watchUrls`

## MonitorsDisplay.render()
- 位置: L77-119
- 役割: 監視が1件以上なら説明・件数と各項目の一覧を、無ければ空の状態の見出しと説明を描く。
- 触るとき: 監視一覧の見た目、件数の表示、空の状態の文言を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.transformMonitorToAgent()`
- 参照: `monitor.id`, `this.canResume`, `this.monitors`, `this.monitors.length`
