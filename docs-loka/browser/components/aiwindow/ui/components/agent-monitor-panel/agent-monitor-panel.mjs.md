# browser/components/aiwindow/ui/components/agent-monitor-panel/agent-monitor-panel.mjs

source: browser/components/aiwindow/ui/components/agent-monitor-panel/agent-monitor-panel.mjs
source-hash: eebca5f3fe1356a9c87b21240d3cdea18e66ff2e
lines: 304

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## AgentMonitorPanel.constructor()
- 位置: L67-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.agent`, `this.attentionIds`, `this.draft`, `this.justCreatedId`, `this.maxMonitors`, `this.monitors`, `this.view`

## AgentMonitorPanel.updated()
- 位置: L78-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changed.get()`, `changed.has()`, `super.updated()`
- 条件付き依存: `if (changed.has("view") && this.view === "create")` → `this.#focusCreateForm()`
- 条件付き依存: `if ( changed.has("view") && changed.get("view") === "create" && !changed.has("justCreatedId") )` → `this.shadowRoot .querySelector(".monitor-list-view") ?.classList.add()`
- 条件付き依存: `if ( changed.has("view") && changed.get("view") === "create" && !changed.has("justCreatedId") )` → `this.shadowRoot .querySelector()`
- 条件付き依存: `if (changed.has("view") && changed.get("view") === "list")` → `this.shadowRoot .querySelector("agent-monitor-item") ?.classList.add()`
- 条件付き依存: `if (changed.has("view") && changed.get("view") === "list")` → `this.shadowRoot .querySelector()`
- 参照: `this.view`

## AgentMonitorPanel.#focusCreateForm()
- 位置: async L100-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`
- 条件付き依存: `if (this.view === "create")` → `form?.focusName()`
- 参照: `form?.updateComplete`, `this.view`

## AgentMonitorPanel.#dispatch()
- 位置: L109-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AgentMonitorPanel.#lastRun()
- 位置: L119-121
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `monitor.history`, `monitor.history?.length`

## AgentMonitorPanel.#renderSchedule()
- 位置: L123-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `lazy.MonitorUIUtils.getScheduleL10n()`
- 参照: `monitor.schedule`, `schedule.args`, `schedule.id`

## AgentMonitorPanel.#renderResult()
- 位置: L135-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#lastRun()`
- 条件付き依存: `if (lastRun.status === "error")` → `html()`
- 条件付き依存: `if (lastRun.conditionMet)` → `html()`
- 参照: `lastRun.conditionMet`, `lastRun.status`

## AgentMonitorPanel.#onRowClick()
- 位置: L160-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 参照: `monitor.id`, `monitor.watchUrls?.length`

## AgentMonitorPanel.#renderRow()
- 位置: L169-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#onRowClick()`, `this.#renderResult()`, `this.#renderSchedule()`
- 参照: `monitor.id`, `monitor.monitorName`, `monitor.status?.kind`, `monitor.watchUrls?.length`, `this.justCreatedId`

## AgentMonitorPanel.#renderSection()
- 位置: L190-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `monitors.map()`, `this.#renderRow()`
- 参照: `monitors.length`

## AgentMonitorPanel.#renderList()
- 位置: L202-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `attention.has()`, `html()`, `this.#renderFooter()`, `this.#renderSection()`, `this.monitors .filter()`, `this.monitors .filter(monitor => !attention.has(monitor.id)) .slice()`, `this.monitors .filter(monitor => attention.has(monitor.id)) .slice()`
- 参照: `monitor.id`, `newMatches.length`, `this.attentionIds`, `this.monitors.length`

## AgentMonitorPanel.#renderFooter()
- 位置: L241-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#dispatch()`, `this.monitors.filter()`
- 参照: `monitor.enabled`, `this.maxMonitors`, `this.monitors.filter(monitor => monitor.enabled).length`

## AgentMonitorPanel.render()
- 位置: L285-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderList()`
- 参照: `this.agent`, `this.draft`, `this.view`
