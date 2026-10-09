# browser/components/aiwindow/ui/components/ai-tasks/ai-tasks.mjs

source: browser/components/aiwindow/ui/components/ai-tasks/ai-tasks.mjs
source-hash: b2e8dc06bc38511836c2759d4f643d16956f7c78
lines: 556

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITasks.constructor()
- 位置: L72-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._constants`, `this.dialogOpen`, `this.monitors`

## AITasks.connectedCallback()
- 位置: async L82-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `super.connectedCallback()`, `this.#initializeActor()`, `this.#initializeActor().catch()`, `this.addEventListener()`, `this.handleMonitorCancel.bind()`, `this.handleMonitorCheckNow.bind()`, `this.handleMonitorDelete.bind()`, `this.handleMonitorOpen.bind()`, `this.handleMonitorPause.bind()`, `this.handleMonitorSubmit.bind()`, `this.loadMonitors()`, `this.loadMonitors().catch()`
- 参照: `this.boundHandleMonitorCancel`, `this.boundHandleMonitorCheckNow`, `this.boundHandleMonitorDelete`, `this.boundHandleMonitorOpen`, `this.boundHandleMonitorPause`, `this.boundHandleMonitorSubmit`

## AITasks.#initializeActor()
- 位置: async L134-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success && result.constants)` → `Object.freeze()`
- 条件付き依存: `if (result?.success && result.constants)` → `this.requestUpdate()`
- 参照: `MONITOR_ACTIONS.REQUEST_CONSTANTS`, `result.constants`, `result?.success`, `this._constants`

## AITasks.#dispatchMonitorAction()
- 位置: L162-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addEventListener()`, `this.dispatchEvent()`

## handleResponse()
- 位置: L167-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `this.removeEventListener()`
- 参照: `event.detail`

## handleError()
- 位置: L173-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`, `this.removeEventListener()`
- 参照: `event.detail?.error`

## AITasks.disconnectedCallback()
- 位置: L194-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this.boundHandleMonitorCancel`, `this.boundHandleMonitorCheckNow`, `this.boundHandleMonitorDelete`, `this.boundHandleMonitorOpen`, `this.boundHandleMonitorPause`, `this.boundHandleMonitorSubmit`

## AITasks.isMaxMonitorsReached()
- 位置: L232-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.monitors.filter()`
- 参照: `monitor.enabled`, `this._constants.TOTAL_NUM_MONITORS`, `this.monitors.filter(monitor => monitor.enabled).length`

## AITasks.isMonitorRegionSupported()
- 位置: L242-244
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._constants.isMonitorRegionSupported`

## AITasks.#dialog()
- 位置: L246-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`

## AITasks.openDialog()
- 位置: L252-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dialog?.showModal()`
- 参照: `this.dialogOpen`

## AITasks.closeDialog()
- 位置: L259-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dialog?.close()`
- 参照: `this.dialogOpen`

## AITasks.handleMonitorDelete()
- 位置: async L271-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success && result?.deleted)` → `this.loadMonitors()`
- 条件付き依存: `if (!result?.success)` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_DELETE_MONITOR`, `event.detail`, `result?.deleted`, `result?.error`, `result?.success`

## AITasks.handleMonitorPause()
- 位置: async L295-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success)` → `this.loadMonitors()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_PAUSE_MONITOR`, `event.detail`, `result?.error`, `result?.success`

## AITasks.handleMonitorCheckNow()
- 位置: async L317-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success)` → `this.loadMonitors()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_RUN_MONITOR`, `event.detail`, `result?.error`, `result?.success`

## AITasks.handleMonitorOpen()
- 位置: async L340-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `event.stopPropagation()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (!result?.success)` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_OPEN_URL`, `event.detail`, `result?.error`, `result?.success`

## AITasks.handleMonitorSubmit()
- 位置: L364-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateMonitor()`
- 条件付き依存: `if (event.detail?.mode === "create")` → `this.createMonitor()`
- 参照: `event.detail`, `event.detail?.mode`

## AITasks.handleMonitorCancel()
- 位置: L374-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closeDialog()`

## AITasks.createMonitor()
- 位置: async L383-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`, `this.#toMonitorSchedule()`, `this.closeDialog()`, `this.loadMonitors()`
- 条件付き依存: `if (!result?.success)` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_CREATE_MONITOR`, `result?.error`, `result?.success`

## AITasks.updateMonitor()
- 位置: async L415-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`, `this.#toMonitorSchedule()`
- 条件付き依存: `if (result?.success)` → `this.loadMonitors()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_UPDATE_MONITOR`, `result?.error`, `result?.success`

## AITasks.#toMonitorSchedule()
- 位置: L447-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `[ this._constants.SCHEDULE_TYPES.DAILY, this._constants.SCHEDULE_TYPES.WEEKLY, ].includes()`, `schedule.time.split()`, `schedule.time.split(":").map()`
- 参照: `schedule.frequency`, `schedule.time`, `schedule.weekday`, `schedule?.frequency`, `this._constants.SCHEDULE_TYPES.DAILY`, `this._constants.SCHEDULE_TYPES.WEEKLY`

## AITasks.loadMonitors()
- 位置: async L473-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_LIST_MONITORS`, `result.monitors`, `result?.error`, `result?.success`, `this.monitors`

## AITasks.render()
- 位置: L488-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.openDialog()`
- 参照: `this._constants.SCHEDULE_TYPES`, `this._constants.TOTAL_NUM_URLS_IN_MONITOR`, `this._constants.smartWindowSupportUrl`, `this.dialogOpen`, `this.isMaxMonitorsReached`, `this.isMonitorRegionSupported`, `this.monitors`
