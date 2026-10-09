# browser/components/aiwindow/ui/components/monitors-display/monitors-display.mjs

source: browser/components/aiwindow/ui/components/monitors-display/monitors-display.mjs
source-hash: a21c9a235c3382453aee9ec1d311b88e57eab34c
lines: 123

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## MonitorsDisplay.constructor()
- 位置: L27-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.canResume`, `this.monitors`, `this.scheduleTypes`, `this.weekdays`

## MonitorsDisplay.buildMonitorStatus()
- 位置: L35-42
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `monitor.enabled`

## MonitorsDisplay.transformMonitorToAgent()
- 位置: L50-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(monitor.history || []).slice()`, `(monitor.history || []).slice().reverse()`, `(monitor.schedule.hour ?? 0) .toString()`, `(monitor.schedule.hour ?? 0) .toString() .padStart()`, `(monitor.schedule.minute ?? 0) .toString()`, `(monitor.schedule.minute ?? 0) .toString() .padStart()`, `monitor.schedule.weekday?.toString()`, `this.buildMonitorStatus()`
- 参照: `monitor.history`, `monitor.id`, `monitor.monitorPrompt`, `monitor.schedule`, `monitor.schedule.hour`, `monitor.schedule.minute`, `monitor.schedule.type`, `monitor.title`, `monitor.watchUrlTitles`, `monitor.watchUrls`

## MonitorsDisplay.render()
- 位置: L77-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.transformMonitorToAgent()`
- 参照: `monitor.id`, `this.canResume`, `this.monitors`, `this.monitors.length`
