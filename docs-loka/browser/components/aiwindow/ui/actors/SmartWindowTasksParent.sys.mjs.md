# browser/components/aiwindow/ui/actors/SmartWindowTasksParent.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartWindowTasksParent.sys.mjs
source-hash: 2752b3bfb9c1c600f1b11dca988285454b300eec
lines: 138

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `this.#handleCreateMonitor.bind()`, `this.#handleDeleteMonitor.bind()`, `this.#handleGetConstants.bind()`, `this.#handleListMonitors.bind()`, `this.#handleOpenUrl.bind()`, `this.#handlePauseMonitor.bind()`, `this.#handleRunMonitor.bind()`, `this.#handleUpdateMonitor.bind()`

## SmartWindowTasksParent.receiveMessage()
- 位置: async L34-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handler()`, `this.#messageHandlers.get()`
- 条件付き依存: `if (!handler)` → `console.warn()`

## SmartWindowTasksParent.#handleListMonitors()
- 位置: async L45-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `console.error()`, `lazy.MonitorAgent.listMonitors()`, `lazy.MonitorUIUtils.resolveWatchUrlTitles()`, `monitors.map()`
- 参照: `error.code`, `error.message`, `monitor.watchUrlTitles`, `monitor.watchUrls`

## SmartWindowTasksParent.#handleCreateMonitor()
- 位置: async L62-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.createMonitor()`
- 参照: `error.code`, `error.message`

## SmartWindowTasksParent.#handleDeleteMonitor()
- 位置: async L72-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorUIUtils.deleteMonitorWithConfirmation()`
- 参照: `data.id`, `data.skipConfirmation`, `this.browsingContext`

## SmartWindowTasksParent.#handleUpdateMonitor()
- 位置: async L82-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.updateMonitor()`
- 参照: `data.id`, `data.updates`, `error.code`, `error.message`

## SmartWindowTasksParent.#handleRunMonitor()
- 位置: async L95-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.runNow()`
- 参照: `data.id`, `error.code`, `error.message`

## SmartWindowTasksParent.#handlePauseMonitor()
- 位置: async L105-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.pauseMonitor()`
- 参照: `data.id`, `data.pause`, `error.code`, `error.message`

## SmartWindowTasksParent.#handleOpenUrl()
- 位置: L115-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorUIUtils.openMonitorUrl()`
- 参照: `data?.url`, `this.browsingContext.topChromeWindow`

## SmartWindowTasksParent.#handleGetConstants()
- 位置: L122-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.MonitorUIUtils.isMonitorRegionSupported()`
- 参照: `lazy.SCHEDULE_TYPES`, `lazy.TOTAL_NUM_MONITORS`, `lazy.TOTAL_NUM_URLS_IN_MONITOR`
- XPCOM: `Services.urlFormatter`
