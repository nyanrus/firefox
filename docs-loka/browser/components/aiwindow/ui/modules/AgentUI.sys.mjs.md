# browser/components/aiwindow/ui/modules/AgentUI.sys.mjs

source: browser/components/aiwindow/ui/modules/AgentUI.sys.mjs
source-hash: 3ab6da408bdc72aa96fc75e82fcffbfdbc49b724
lines: 785

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `console.createInstance()`, `this.#handleCancelMonitor.bind()`, `this.#handleCheckMonitor.bind()`, `this.#handleDeleteMonitor.bind()`, `this.#handleMonitorCommand.bind()`, `this.#handlePauseMonitor.bind()`, `this.#handleSaveMonitorDraft.bind()`, `this.#handleUpdateMonitor.bind()`, `this.handleCreateMonitor.bind()`

## AgentUI.handleUpdate()
- 位置: async L105-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation?.messages?.find()`, `handler()`
- 条件付き依存: `if (typeof handler !== "function")` → `lazy.console.error()`
- 参照: `m.id`, `message?.toolUIData?.toolCallId`, `this.#UPDATE_TYPE_HANDLERS`

## AgentUI.#handleMonitorCommand()
- 位置: async L162-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addAssistantMessage()`, `conversation.addUIToolToCurrentMessage()`, `crypto.randomUUID()`, `lazy.MonitorAgent.listMonitors()`, `lazy.isAllowedWatchUrl()`, `lazy.l10n.formatValueSync()`, `monitors.filter()`
- 条件付き依存: `if (raw)` → `conversation.addUserMessage()`
- 条件付き依存: `if (raw)` → `conversation.emit()`
- 条件付き依存: `if (!isFullPage)` → `conversation.addAssistantWithL10nMessage()`
- 条件付き依存: `if (activeCount >= lazy.TOTAL_NUM_MONITORS)` → `conversation.addAssistantWithL10nMessage()`
- 参照: `AGENT_UI_TYPES.MONITOR_ITEM`, `lazy.TOTAL_NUM_MONITORS`, `monitor.enabled`, `monitors.filter(monitor => monitor.enabled).length`

## AgentUI.handleCreateMonitor()
- 位置: async L225-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.emit()`, `lazy.MonitorAgent.createMonitor()`, `lazy.MonitorUIUtils.resolveWatchUrlTitles()`, `lazy.console.error()`, `lazy.l10n.formatValueSync()`, `this.#buildMonitorArgs()`, `this.#formatScheduleSummary()`, `this.#setMessageL10n()`, `this.#statusForKind()`
- 条件付き依存: `if (!args.prompt || !args.watchUrls.length)` → `lazy.console.warn()`
- 条件付き依存: `if (updateData?.autoExpandAndCheck)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (updateData?.autoExpandAndCheck)` → `lazy.MonitorAgent.runNow()`
- 条件付き依存: `if (updateData?.autoExpandAndCheck)` → `lazy.console.error()`
- 参照: `args.pageTitle`, `args.prompt`, `args.watchUrls`, `args.watchUrls.length`, `message.toolUIData`, `message.toolUIDraft`, `message?.toolUIData?.properties?.agent`, `updateData?.autoExpandAndCheck`, `updateData?.schedule`
- XPCOM: `Services.tm`

## AgentUI.#handleCancelMonitor()
- 位置: async L308-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.updateToolUI()`, `this.#setMessageL10n()`
- 参照: `message.toolUIDraft`

## AgentUI.#handleSaveMonitorDraft()
- 位置: L323-326
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `message.toolUIDraft`, `updateData?.draft`

## AgentUI.#handleUpdateMonitor()
- 位置: async L334-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.emit()`, `lazy.MonitorAgent.updateMonitor()`, `lazy.MonitorUIUtils.resolveWatchUrlTitles()`, `lazy.console.error()`, `this.#buildSchedule()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 参照: `agent.monitorName`, `agent.url`, `message.toolUIData`, `message.toolUIDraft`, `message?.toolUIData?.properties?.agent`, `updateData.condition`, `updateData.monitorName`, `updateData.schedule`, `updateData.watchUrls`, `updateData?.id`

## AgentUI.#handleDeleteMonitor()
- 位置: async L383-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.updateToolUI()`, `lazy.MonitorUIUtils.deleteMonitorWithConfirmation()`, `lazy.l10n.formatValueSync()`, `this.#setMessageL10n()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 条件付き依存: `if (!browsingContext)` → `lazy.console.warn()`
- 条件付き依存: `if (!result.success)` → `lazy.console.error()`
- 参照: `agent.monitorName`, `message?.toolUIData?.properties?.agent`, `result.cancelled`, `result.error`, `result.success`, `updateData?.id`, `window?.gBrowser?.selectedBrowser?.browsingContext`

## AgentUI.#handlePauseMonitor()
- 位置: async L439-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.emit()`, `lazy.MonitorAgent.updateMonitor()`, `lazy.console.error()`, `this.#statusForKind()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 参照: `message.toolUIData`, `message.toolUIData.properties`, `message?.toolUIData?.properties?.agent`, `updateData?.id`, `updateData?.paused`

## AgentUI.#handleCheckMonitor()
- 位置: async L475-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorAgent.runNow()`, `lazy.console.error()`, `this.#loadMonitorsById()`, `this.#syncConversationHistory()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 参照: `updateData?.id`

## AgentUI.observeMonitorChanges()
- 位置: L502-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.error()`, `this.#observedConversations.add()`, `this.#syncAllMonitorHistories()`, `this.#syncAllMonitorHistories().catch()`
- 条件付き依存: `if (!this.#monitorObserver)` → `Services.obs.addObserver()`
- 参照: `lazy.MONITOR_AGENTS_CHANGED_TOPIC`, `this.#monitorObserver`
- XPCOM: `Services.obs`

## this.#monitorObserver()
- 位置: L509-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.error()`, `this.#syncAllMonitorHistories()`, `this.#syncAllMonitorHistories().catch()`

## AgentUI.unobserveMonitorChanges()
- 位置: L530-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observedConversations.delete()`
- 条件付き依存: `if (!this.#observedConversations.size && this.#monitorObserver)` → `Services.obs.removeObserver()`
- 参照: `lazy.MONITOR_AGENTS_CHANGED_TOPIC`, `this.#monitorObserver`, `this.#observedConversations.size`
- XPCOM: `Services.obs`

## AgentUI.#loadMonitorsById()
- 位置: async L551-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorAgent.listMonitors()`, `monitors.map()`
- 参照: `monitor.id`

## AgentUI.#syncAllMonitorHistories()
- 位置: async L556-564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#loadMonitorsById()`, `this.#syncConversationHistory()`
- 参照: `this.#observedConversations`, `this.#observedConversations.size`

## AgentUI.#syncConversationHistory()
- 位置: L574-603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(monitor.history ?? []) .filter()`, `(monitor.history ?? []) .filter(entry => entry.status === "success" || entry.status === "error") .reverse()`, `JSON.stringify()`, `byId.get()`, `conversation.emit()`
- 参照: `AGENT_UI_TYPES.MONITOR_ITEM`, `agent.history`, `agent?.id`, `conversation?.messages`, `entry.status`, `message.toolUIData`, `message.toolUIData.properties`, `message.toolUIData.properties?.agent`, `message?.toolUIData?.uiType`, `monitor.history`

## AgentUI.#setMessageL10n()
- 位置: L614-619
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `message.content.body`, `message.content.l10nArgs`, `message.content.l10nId`, `message.content.link`

## AgentUI.#statusForKind()
- 位置: L628-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.l10n.formatValueSync()`

## AgentUI.#buildMonitorArgs()
- 位置: L646-659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildSchedule()`
- 参照: `agent.condition`, `agent.monitorName`, `agent.pageTitle`, `agent.url`, `agent.watchUrls`, `updateData.watchUrls`, `updateData?.condition`, `updateData?.monitorName`, `updateData?.schedule`, `updateData?.watchUrls?.length`

## AgentUI.#buildSchedule()
- 位置: L669-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `String()`, `String(schedule?.time ?? "") .split()`, `String(schedule?.time ?? "") .split(":") .map()`
- 参照: `lazy.DailySchedule`, `lazy.IntervalSchedule`, `lazy.WeeklySchedule`, `schedule.weekday`, `schedule?.frequency`, `schedule?.time`

## AgentUI.#formatScheduleSummary()
- 位置: L692-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `String()`, `String(schedule?.time ?? "") .split()`, `String(schedule?.time ?? "") .split(":") .map()`, `lazy.l10n.formatValueSync()`, `when.getTime()`, `when.setHours()`
- 条件付き依存: `if (schedule.frequency === "weekly")` → `Number()`
- 条件付き依存: `if (schedule.frequency === "weekly")` → `when.getDay()`
- 条件付き依存: `if (schedule.frequency === "weekly")` → `when.setDate()`
- 条件付き依存: `if (schedule.frequency === "weekly")` → `when.getDate()`
- 条件付き依存: `if (schedule.frequency === "weekly")` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (schedule.frequency === "weekly")` → `when.getTime()`
- 参照: `schedule.frequency`, `schedule.weekday`, `schedule?.time`

## AgentUI.tryHandleCommand()
- 位置: L729-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `handler()`, `lazy.MonitorUIUtils.isMonitorRegionSupported()`, `parseAgentCommand()`, `value.trim()`
- 参照: `parsed?.prompt`, `parsedCommand.command`, `this.#COMMAND_HANDLERS`
- XPCOM: `Services.prefs`

## AgentUI.isAgentUpdate()
- 位置: L781-783
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `data?.updateType`, `this.#UPDATE_TYPE_HANDLERS`
