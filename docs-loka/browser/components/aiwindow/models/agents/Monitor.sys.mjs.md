# browser/components/aiwindow/models/agents/Monitor.sys.mjs

source: browser/components/aiwindow/models/agents/Monitor.sys.mjs
source-hash: 87657b2c7ccda9329bdcc854bdf176d4e49877ab
lines: 1188

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `String()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## [MONITOR_EXPIRY_REASONS.NO_MATCH]()
- 位置: L89-89
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.expiryNoMatchDays`

## [MONITOR_EXPIRY_REASONS.MAX_AGE]()
- 位置: L90-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.expiryMaxAgeDays`

## MonitorRunError.constructor()
- 位置: L105-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.code`, `this.name`

## MonitorLimitError.constructor()
- 位置: L121-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `MONITOR_ERROR_CODES.ACTIVE_LIMIT`, `this.code`, `this.limit`, `this.name`

## Monitor.constructor()
- 位置: L207-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `String()`, `String(monitorPrompt ?? "").trim()`, `String(title ?? "").trim()`, `crypto.randomUUID()`, `new Date().toISOString()`, `schedule.getNextRunTime()`, `schedule.getNextRunTime(lastRunTime).toISOString()`, `trimAndFilterWatchUrls()`
- 参照: `schedule?.getNextRunTime`, `this.activeSince`, `this.createdAt`, `this.enabled`, `this.expiry`, `this.history`, `this.id`, `this.initialSnapshot`, `this.lastMatchAt`, `this.lastRunTime`, `this.monitorPrompt`, `this.nextRunTime`, `this.notificationsMuted`, `this.runCount`, `this.schedule`, `this.title`, `this.updatedAt`, `this.watchUrls`, `this.watchUrls.length`

## Monitor.fromJSON()
- 位置: L266-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Schedule.fromJSON()`, `latestMatchTime()`, `normalizeLoadedHistory()`
- 参照: `savedMonitor.activeSince`, `savedMonitor.createdAt`, `savedMonitor.enabled`, `savedMonitor.expiry`, `savedMonitor.history`, `savedMonitor.id`, `savedMonitor.initialSnapshot`, `savedMonitor.lastMatchAt`, `savedMonitor.lastRunTime`, `savedMonitor.monitorPrompt`, `savedMonitor.nextRunTime`, `savedMonitor.notificationsMuted`, `savedMonitor.runCount`, `savedMonitor.schedule`, `savedMonitor.title`, `savedMonitor.updatedAt`, `savedMonitor.watchUrls`, `savedMonitor?.id`

## Monitor.run()
- 位置: async L302-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Math.round()`, `String()`, `abortController.abort()`, `checkedAt.toISOString()`, `crypto.randomUUID()`, `getCancelCode()`, `getRunReason()`, `lazy.MonitorAgent._saveAndNotify()`, `monitorErrorCode()`, `new Date().toISOString()`, `recordRunEnd()`, `recordRunRequest()`, `scheduledRunDelayMs()`, `this.#finishRun()`, `this.addHistoryEntry()`, `this.runMonitorCheck()`, `this.schedule .getNextRunTime()`, `this.schedule .getNextRunTime(this.lastRunTime) .toISOString()`, `withTimeout()`
- 条件付き依存: `if (!this.enabled || new Date(this.nextRunTime) > checkedAt)` → `this.scheduleNextRun()`
- 条件付き依存: `if (!manual)` → `this.getExpiryReason()`
- 条件付き依存: `if (expiryReason)` → `lazy.MonitorAgent._expireMonitor()`
- 条件付き依存: `if (timedOut && checkPromise)` → `checkPromise.catch()`
- 参照: `abortController.signal`, `abortController.signal.reason`, `error.message`, `historyEntry.checkedAt`, `historyEntry.conditionMet`, `historyEntry.errorCode`, `historyEntry.resultExplanation`, `historyEntry.status`, `result.conditionMet`, `result.explanation`, `this.#abortController`, `this.#disposed`, `this.#running`, `this.enabled`, `this.id`, `this.lastMatchAt`, `this.lastRunTime`, `this.nextRunTime`, `this.runCount`, `this.updatedAt`

## Monitor.runMonitorCheck()
- 位置: async L441-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Promise.all()`, `String()`, `categorizeError()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `extractMonitorPageContent()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `makeJSONSchemaBlob()`, `now.toISOString()`, `openAIEngine.getFxAccountToken()`, `renderPrompt()`, `this.parseMonitorResult()`, `this.watchUrls.join()`, `throwIfAborted()`, `withAbortSignal()`
- 条件付き依存: `if (!initialSnapshot)` → `this.ensureInitialSnapshot()`
- 条件付き依存: `if (!initialSnapshot)` → `throwIfAborted()`
- 条件付き依存: `if (!initialSnapshot)` → `lazy.log.warn()`
- 条件付き依存: `if (runStats)` → `recordRunStart()`
- 条件付き依存: `if (runStats)` → `Math.round()`
- 条件付き依存: `if (runStats)` → `ChromeUtils.now()`
- 参照: `MODEL_FEATURES.AGENT_MONITOR`, `MONITOR_ERROR_CODES.MODEL`, `MONITOR_ERROR_CODES.PROMPT_LOAD`, `MONITOR_ERROR_CODES.UNKNOWN`, `conversation.engine?.model`, `error.message`, `initialSnapshot?.capturedAt`, `initialSnapshot?.pageContent`, `runStats.model`, `runStats.modelLatencyMs`, `this.initialSnapshot`, `this.monitorPrompt`, `this.watchUrls`

## Monitor.captureInitialSnapshot()
- 位置: async L582-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AbortSignal.any()`, `extractMonitorPageContent()`, `lazy.buildConversation()`, `new Date().toISOString()`, `throwIfAborted()`, `urlListsEqual()`
- 参照: `MODEL_FEATURES.AGENT_MONITOR`, `abortController.signal`, `this.#snapshotAbortController`, `this.id`, `this.initialSnapshot`, `this.watchUrls`

## Monitor.cancelSnapshotCapture()
- 位置: L625-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#snapshotAbortController?.abort()`
- 参照: `this.#snapshotCapture`

## Monitor.ensureInitialSnapshot()
- 位置: async L641-658
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#snapshotCapture)` → `this.captureInitialSnapshot({ conversation, signal, }).finally()`
- 条件付き依存: `if (!this.#snapshotCapture)` → `this.captureInitialSnapshot()`
- 参照: `this.#snapshotCapture`, `this.initialSnapshot`

## Monitor.scheduleNextRun()
- 位置: L664-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.max()`, `Number.isNaN()`, `lazy.log.error()`, `nextRun.getTime()`, `this.clearTimer()`, `this.run()`
- 条件付き依存: `if (!nextRun || Number.isNaN(nextRun.getTime()))` → `this.schedule .getNextRunTime(this.lastRunTime) .toISOString()`
- 条件付き依存: `if (!nextRun || Number.isNaN(nextRun.getTime()))` → `this.schedule .getNextRunTime()`
- 参照: `lazy.ScheduledTask`, `this.#disposed`, `this.#timer`, `this.enabled`, `this.lastRunTime`, `this.nextRunTime`

## Monitor.getExpiryReason()
- 位置: L701-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.parse()`, `Math.max()`, `Number.isFinite()`, `expiryRuleElapsed()`
- 参照: `MONITOR_EXPIRY_REASONS.MAX_AGE`, `MONITOR_EXPIRY_REASONS.NO_MATCH`, `this.activeSince`, `this.lastMatchAt`

## Monitor.parseMonitorResult()
- 位置: L726-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `fenced[1].trim()`, `parsed.explanation.trim()`, `raw.match()`, `response?.finalOutput?.trim()`
- 参照: `parsed.conditionMet`, `parsed.explanation`

## Monitor.toSerializable()
- 位置: L763-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.history.map()`, `this.watchUrls.slice()`
- 参照: `this.activeSince`, `this.createdAt`, `this.enabled`, `this.expiry`, `this.id`, `this.initialSnapshot`, `this.lastMatchAt`, `this.lastRunTime`, `this.monitorPrompt`, `this.nextRunTime`, `this.notificationsMuted`, `this.runCount`, `this.schedule`, `this.title`, `this.updatedAt`

## Monitor.clearTimer()
- 位置: L787-792
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#timer)` → `this.#timer.disarm()`
- 参照: `this.#timer`

## Monitor.dispose()
- 位置: L799-813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortController?.abort()`, `this.#snapshotAbortController?.abort()`, `this.clearTimer()`
- 参照: `MONITOR_ERROR_CODES.CANCELED`, `MONITOR_ERROR_CODES.INTERRUPTED`, `this.#disposed`

## Monitor.restore()
- 位置: L815-817
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#disposed`

## Monitor.addHistoryEntry()
- 位置: L819-824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.history.push()`
- 条件付き依存: `if (this.history.length > MAX_HISTORY_ENTRIES)` → `this.history.shift()`
- 参照: `this.history.length`

## Monitor.#finishRun()
- 位置: L826-834
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#disposed && this.enabled)` → `this.scheduleNextRun()`
- 参照: `this.#abortController`, `this.#disposed`, `this.#running`, `this.enabled`

## throwIfAborted()
- 位置: L839-847
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `signal.reason`, `signal?.aborted`

## withAbortSignal()
- 位置: async L849-873
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `signal.addEventListener()`, `signal.removeEventListener()`, `throwIfAborted()`

## onAbort()
- 位置: L858-864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`
- 参照: `signal.reason`

## withTimeout()
- 位置: async L875-898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `Promise.race()`, `lazy.setTimeout()`, `onTimeout()`, `reject()`
- 条件付き依存: `if (timeoutId)` → `lazy.clearTimeout()`
- 参照: `error.name`

## latestMatchTime()
- 位置: L900-902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `history.findLast()`
- 参照: `entry?.conditionMet`, `history.findLast(entry => entry?.conditionMet)?.checkedAt`

## expiryRuleDays()
- 位置: L911-918
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `days()`
- 条件付き依存: `if (!days)` → `lazy.log.error()`

## expiryRuleElapsed()
- 位置: L920-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `expiryRuleDays()`, `now.getTime()`

## normalizeLoadedHistory()
- 位置: L927-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `history.map()`
- 参照: `MONITOR_ERROR_CODES.INTERRUPTED`, `entry?.status`

## monitorErrorCode()
- 位置: L956-967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/abort/i.test()`, `categorizeError()`
- 参照: `MONITOR_ERROR_CODES.INTERRUPTED`, `MONITOR_ERROR_CODES.TIMEOUT`, `error.code`, `error?.message`, `error?.name`

## extractMonitorPageContent()
- 位置: async L969-997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.GetPageContent.getPageContent()`, `results .map()`, `results .map(result => result.content) .join()`, `results.some()`, `throwIfAborted()`, `withAbortSignal()`
- 参照: `MONITOR_ERROR_CODES.CONTENT_EXTRACTION`, `result.content`, `result.ok`

## urlListsEqual()
- 位置: L999-1001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.every()`
- 参照: `a.length`, `b.length`

## trimAndFilterWatchUrls()
- 位置: L1003-1013
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `String()`, `String(url ?? "").trim()`, `urls.map()`, `urls.map(url => String(url ?? "").trim()).filter()`
- 参照: `urls.length`

## isAllowedWatchUrl()
- 位置: L1015-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `["http:", "https:"].includes()`
- 参照: `url.protocol`

## scheduledRunDelayMs()
- 位置: L1020-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.parse()`, `Math.max()`, `Number.isFinite()`, `checkedAt.getTime()`

## getRunReason()
- 位置: L1031-1038
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `RUN_REASONS.DELAYED`, `RUN_REASONS.MANUAL`, `RUN_REASONS.TRIGGER_TIME`

## getCancelCode()
- 位置: L1044-1057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ MONITOR_ERROR_CODES.CANCELED, MONITOR_ERROR_CODES.INTERRUPTED, ].includes()`
- 参照: `MONITOR_ERROR_CODES.CANCELED`, `MONITOR_ERROR_CODES.INTERRUPTED`, `abortReason.code`

## buildRunTelemetryExtra()
- 位置: L1059-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorAgent._telemetryExtra()`

## recordRunRequest()
- 位置: L1067-1073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionExecuteRequest.record()`, `buildRunTelemetryExtra()`
- 参照: `extra.delay`, `runStats.delayMs`

## recordRunStart()
- 位置: L1075-1081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionExecuteStart.record()`, `buildRunTelemetryExtra()`
- 参照: `extra.model`, `runStats.model`

## recordRunEnd()
- 位置: L1083-1125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionExecuteComplete.record()`, `buildRunTelemetryExtra()`
- 条件付き依存: `if (cancelCode)` → `Glean.smartWindow.agenticActionExecuteCancel.record()`
- 参照: `completeExtra.delay`, `completeExtra.error_code`, `completeExtra.latency`, `completeExtra.outcome`, `extra.duration`, `extra.model`

## monitorAgeMs()
- 位置: L1133-1136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Date.parse()`, `Math.max()`, `Number.isFinite()`
- 参照: `monitor.createdAt`

## categorizeError()
- 位置: L1147-1187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(error?.message ?? String(error)).toLowerCase()`, `Number()`, `String()`, `message.includes()`, `message.match()`, `patterns.some()`
- 参照: `MONITOR_ERROR_CODES.AUTH`, `MONITOR_ERROR_CODES.MODEL`, `MONITOR_ERROR_CODES.RATE_LIMIT`, `MONITOR_ERROR_CODES.TIMEOUT`, `error.status`, `error?.message`, `error?.status`
