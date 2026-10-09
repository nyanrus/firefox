# browser/components/aiwindow/ui/components/agent-monitor-item/agent-monitor-item.mjs

source: browser/components/aiwindow/ui/components/agent-monitor-item/agent-monitor-item.mjs
source-hash: 223c886c6932be24279037724735ec77bf5734fe
lines: 1190

## <module>
- 役割: (未記入)
- 呼び出し先: `Array.from()`, `Math.floor()`, `Object.freeze()`, `String()`, `String(hour24).padStart()`, `String(minute).padStart()`, `customElements.define()`, `timeDate.setHours()`, `timeDate.toLocaleTimeString()`

## nextTimeOption()
- 位置: L87-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `now.getHours()`, `now.getMinutes()`
- 参照: `TIME_OPTIONS.length`, `TIME_OPTIONS[0].value`, `TIME_OPTIONS[slot].value`

## AgentMonitorItem.constructor()
- 位置: L202-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nextTimeOption()`, `super()`
- 参照: `SCHEDULE_TYPES.DAILY`, `this.#draftName`, `this.agent`, `this.alertDescription`, `this.canResume`, `this.checkFrequency`, `this.draft`, `this.editing`, `this.expanded`, `this.fieldErrors`, `this.maxWatchUrls`, `this.mode`, `this.pageUrls`, `this.pendingUrl`, `this.pendingUrlError`, `this.scheduleTime`, `this.scheduleWeekday`, `this.selfContained`, `this.showLastResult`

## AgentMonitorItem.willUpdate()
- 位置: L227-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changed.has()`
- 条件付き依存: `if (changed.has("agent"))` → `this.#seedFromAgent()`
- 条件付き依存: `if (changed.has("agent") || changed.has("draft"))` → `this.#applyDraft()`

## AgentMonitorItem.disconnectedCallback()
- 位置: L237-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.#draftPersistTimer)` → `this.#flushDraft()`
- 参照: `this.#draftPersistTimer`

## AgentMonitorItem.#seedFromAgent()
- 位置: L244-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `seededUrls.filter()`, `u?.trim()`
- 条件付き依存: `if (schedule)` → `Number()`
- 参照: `schedule.frequency`, `schedule.time`, `schedule.weekday`, `this.#draftName`, `this.agent`, `this.agent?.schedule`, `this.alertDescription`, `this.checkFrequency`, `this.expanded`, `this.fieldErrors`, `this.pageUrls`, `this.pendingUrl`, `this.pendingUrlError`, `this.scheduleTime`, `this.scheduleWeekday`, `u?.trim().length`, `watchUrls?.length`

## AgentMonitorItem.#applyDraft()
- 位置: L280-315
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (schedule?.weekday !== undefined)` → `Number()`
- 参照: `schedule.frequency`, `schedule.time`, `schedule.weekday`, `schedule?.frequency`, `schedule?.time`, `schedule?.weekday`, `this.#draftName`, `this.alertDescription`, `this.checkFrequency`, `this.draft`, `this.editing`, `this.expanded`, `this.pageUrls`, `this.pendingUrl`, `this.scheduleTime`, `this.scheduleWeekday`

## AgentMonitorItem.#persistDraft()
- 位置: L323-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.#clearDraftTimer()`, `this.#flushDraft()`
- 条件付き依存: `if (!debounce)` → `this.#flushDraft()`
- 参照: `this.#draftPersistTimer`, `this.editing`, `this.mode`

## AgentMonitorItem.#flushDraft()
- 位置: L338-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`
- 参照: `this.#monitorName`, `this.alertDescription`, `this.checkFrequency`, `this.editing`, `this.pageUrls`, `this.pendingUrl`, `this.scheduleTime`, `this.scheduleWeekday`

## AgentMonitorItem.#discardDraft()
- 位置: L356-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`

## AgentMonitorItem.#clearDraftTimer()
- 位置: L361-366
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#draftPersistTimer)` → `clearTimeout()`
- 参照: `this.#draftPersistTimer`

## AgentMonitorItem.#dispatch()
- 位置: L368-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AgentMonitorItem.#monitorName()
- 位置: L374-376
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#draftName`, `this.agent?.monitorName`

## AgentMonitorItem.focusName()
- 位置: L378-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`, `this.shadowRoot?.querySelector(".monitor-name-input")?.focus()`

## AgentMonitorItem.#optionIcon()
- 位置: L392-394
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selfContained`

## AgentMonitorItem.#validateForm()
- 位置: L398-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["name", "condition", "pages"].filter()`, `invalid.includes()`, `this.#monitorName.trim()`, `this.alertDescription?.trim()`, `this.pendingUrl.trim()`
- 条件付き依存: `if (this.pendingUrl.trim())` → `this.#addUrl()`
- 条件付き依存: `if (this.pendingUrlError && !invalid.includes("pages"))` → `invalid.push()`
- 参照: `errors.condition`, `errors.name`, `errors.pages`, `this.fieldErrors`, `this.mode`, `this.pageUrls.length`, `this.pendingUrlError`

## AgentMonitorItem.#clearFieldError()
- 位置: L423-427
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.fieldErrors`

## AgentMonitorItem.#focusField()
- 位置: L429-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector(selector)?.focus()`

## AgentMonitorItem.#onNameInput()
- 位置: L438-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearFieldError()`, `this.#persistDraft()`
- 参照: `event.target.value`, `event.type`, `this.#draftName`

## AgentMonitorItem.#onCardClick()
- 位置: L445-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.closest()`, `this.#onToggle()`

## AgentMonitorItem.#onToggle()
- 位置: L452-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 参照: `this.expanded`

## AgentMonitorItem.#onEditToggle()
- 位置: L457-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 条件付き依存: `if (this.editing)` → `this.#persistDraft()`
- 条件付き依存: `if (!(this.editing))` → `this.#discardDraft()`
- 参照: `this.editing`

## AgentMonitorItem.#onConditionInput()
- 位置: L469-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearFieldError()`, `this.#persistDraft()`
- 参照: `event.target.value`, `event.type`, `this.alertDescription`

## AgentMonitorItem.#onPresetClick()
- 位置: L475-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearFieldError()`, `this.#persistDraft()`
- 参照: `this.alertDescription`

## AgentMonitorItem.#normalizeUrl()
- 位置: L484-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.trim()`, `value.includes()`
- 参照: `new URL(candidate).href`

## AgentMonitorItem.#isSameUrl()
- 位置: L501-507
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `new URL(a).href`, `new URL(b).href`

## AgentMonitorItem.#validateAndNormalizeURL()
- 位置: L510-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#normalizeUrl()`

## AgentMonitorItem.#addUrl()
- 位置: L522-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearFieldError()`, `this.#isSameUrl()`, `this.#persistDraft()`, `this.#validateAndNormalizeURL()`, `this.pageUrls.some()`, `this.pendingUrl.trim()`
- 参照: `this.maxWatchUrls`, `this.pageUrls`, `this.pageUrls.length`, `this.pendingUrl`, `this.pendingUrlError`

## AgentMonitorItem.#removeUrl()
- 位置: L551-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#persistDraft()`, `this.pageUrls.filter()`
- 参照: `this.pageUrls`

## AgentMonitorItem.#displayUrl()
- 位置: L556-562
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `new URL(url).hostname`

## AgentMonitorItem.#onPendingUrlInput()
- 位置: L564-570
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#persistDraft()`
- 参照: `event.target.value`, `this.pendingUrl`, `this.pendingUrlError`

## AgentMonitorItem.#onPendingUrlKeydown()
- 位置: L572-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.#addUrl()`
- 参照: `event.key`

## AgentMonitorItem.#onCancel()
- 位置: L580-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`

## AgentMonitorItem.#onSubmit()
- 位置: async L587-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`, `this.#validateForm()`, `this.alertDescription.trim()`
- 条件付き依存: `if (invalidFields.length)` → `this.#focusField()`
- 条件付き依存: `if (this.editing)` → `this.#dispatch()`
- 参照: `invalidFields.length`, `this.#monitorName`, `this.agent?.id`, `this.checkFrequency`, `this.editing`, `this.mode`, `this.pageUrls`, `this.scheduleTime`, `this.scheduleWeekday`, `this.updateComplete`

## AgentMonitorItem.#renderStatusChip()
- 位置: L618-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.agent?.status?.kind`

## AgentMonitorItem.#renderLastCheckedCondition()
- 位置: L624-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#transformHistoryItem()`
- 参照: `mostRecentItem.conditionMet`, `normalizedItem.resultState`, `this.agent?.history`

## AgentMonitorItem.#renderFieldError()
- 位置: L643-651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `error.args`, `error.id`

## AgentMonitorItem.#renderConditionField()
- 位置: L653-684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `presets.map()`, `this.#onPresetClick()`, `this.#renderFieldError()`
- 参照: `presets.length`, `this.#onConditionInput`, `this.agent?.conditionPresets`, `this.alertDescription`, `this.fieldErrors.condition`

## AgentMonitorItem.#renderPagesField()
- 位置: L686-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#addUrl()`, `this.#displayUrl()`, `this.#removeUrl()`, `this.#renderFieldError()`, `this.pageUrls.map()`
- 参照: `this.#onPendingUrlInput`, `this.#onPendingUrlKeydown`, `this.agent?.watchUrlTitles`, `this.fieldErrors.pages`, `this.maxWatchUrls`, `this.pageUrls.length`, `this.pendingUrl`, `this.pendingUrlError`

## AgentMonitorItem.#transformHistoryItem()
- 位置: L739-796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `date.toLocaleDateString()`, `date.toLocaleTimeString()`
- 条件付き依存: `if (item.status === "error")` → `monitorErrorL10nId()`
- 参照: `RESULT_STATES.COULD_NOT_CHECK`, `RESULT_STATES.MET`, `RESULT_STATES.NOT_MET`, `item.checkedAt`, `item.conditionMet`, `item.errorCode`, `item.resultExplanation`, `item.status`

## AgentMonitorItem.#renderHistory()
- 位置: L798-842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `historyItems.map()`, `html()`, `this.#transformHistoryItem()`
- 条件付き依存: `if (normalizedItem.noteL10nId)` → `html()`
- 条件付き依存: `if (normalizedItem.note)` → `html()`
- 参照: `historyItems.length`, `normalizedItem.note`, `normalizedItem.noteL10nId`, `normalizedItem.resultState`, `normalizedItem.when`, `this.agent?.history`

## AgentMonitorItem.#onFrequencyChange()
- 位置: L844-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#persistDraft()`
- 参照: `event.target.value`, `this.checkFrequency`

## AgentMonitorItem.#onScheduleTimeChange()
- 位置: L849-852
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#persistDraft()`
- 参照: `event.target.value`, `this.scheduleTime`

## AgentMonitorItem.#onWeekdayChange()
- 位置: L854-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `this.#persistDraft()`
- 参照: `event.target.value`, `this.scheduleWeekday`

## AgentMonitorItem.#renderScheduleSummary()
- 位置: L859-904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `schedule.time.split()`, `schedule.time.split(":").map()`, `timeDate.getTime()`, `timeDate.setHours()`
- 条件付き依存: `if (fluentId)` → `html()`
- 条件付き依存: `if (fluentId)` → `JSON.stringify()`
- 条件付き依存: `if (fluentId)` → `timeDate.getTime()`
- 参照: `SCHEDULE_TYPES.WEEKLY`, `schedule.frequency`, `schedule.weekday`, `this.agent?.schedule`

## AgentMonitorItem.#renderTimeField()
- 位置: L906-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TIME_OPTIONS.map()`, `html()`, `this.#optionIcon()`
- 参照: `opt.label`, `opt.value`, `this.#onScheduleTimeChange`, `this.scheduleTime`

## AgentMonitorItem.#renderScheduler()
- 位置: L930-982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WEEKDAYS.map()`, `html()`, `this.#optionIcon()`, `this.#renderTimeField()`
- 参照: `SCHEDULE_TYPES.DAILY`, `SCHEDULE_TYPES.WEEKLY`, `day.ftlId`, `day.value`, `this.#onFrequencyChange`, `this.#onWeekdayChange`, `this.checkFrequency`, `this.scheduleWeekday`

## AgentMonitorItem.#renderCreate()
- 位置: L984-1037
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderConditionField()`, `this.#renderFieldError()`, `this.#renderPagesField()`, `this.#renderScheduler()`
- 参照: `this.#monitorName`, `this.#onCancel`, `this.#onNameInput`, `this.#onSubmit`, `this.fieldErrors.name`, `this.selfContained`

## AgentMonitorItem.#renderDisplay()
- 位置: L1039-1067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderExpand()`, `this.#renderLastCheckedCondition()`, `this.#renderStatusChip()`
- 参照: `agent.monitorName`, `this.#onCardClick`, `this.#onToggle`, `this.agent`, `this.expanded`, `this.showLastResult`

## AgentMonitorItem.#renderExpand()
- 位置: L1069-1176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `agent.watchUrls.map()`, `e.stopPropagation()`, `html()`, `this.#dispatch()`, `this.#displayUrl()`, `this.#renderConditionField()`, `this.#renderHistory()`, `this.#renderPagesField()`, `this.#renderScheduleSummary()`, `this.#renderScheduler()`
- 参照: `agent.condition`, `agent.id`, `agent.status?.kind`, `agent.watchUrlTitles`, `agent.watchUrls?.length`, `this.#onEditToggle`, `this.#onSubmit`, `this.agent`, `this.canResume`, `this.editing`

## AgentMonitorItem.render()
- 位置: L1178-1186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderCreate()`, `this.#renderDisplay()`
- 参照: `this.mode`
