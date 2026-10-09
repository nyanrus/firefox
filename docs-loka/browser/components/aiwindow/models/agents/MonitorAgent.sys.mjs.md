# browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs

source: browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs
source-hash: fb6d7827fd95f6065412ddde08803f83baeba170
lines: 1199

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`, `Object.freeze()`, `console.createInstance()`

## seedNotifiedRunIds()
- 位置: L120-128
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (entry.conditionMet || entry.status === "error")` → `gNotifiedRunIds.add()`
- 参照: `entry.conditionMet`, `entry.id`, `entry.status`, `monitor.history`

## isShuttingDown()
- 位置: L130-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.isInOrBeyondShutdownPhase()`
- 参照: `Ci.nsIAppStartup.SHUTDOWN_PHASE_APPSHUTDOWNCONFIRMED`
- XPCOM: [`nsIAppStartup`](../../../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## MonitorAgentShutdownError.constructor()
- 位置: L144-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.name`

## activeMonitorCount()
- 位置: L150-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.values()`
- 参照: `monitor.enabled`

## isClockField()
- 位置: L160-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`

## buildScheduleTelemetryExtra()
- 位置: L166-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(SCHEDULE_TYPES).includes()`, `isClockField()`
- 条件付き依存: `if (isClockField(schedule.hour, 23) && isClockField(schedule.minute, 59))` → `pad()`
- 参照: `SCHEDULE_TYPES.INTERVAL`, `SCHEDULE_TYPES.WEEKLY`, `extra.check_time`, `extra.check_weekday`, `schedule.hour`, `schedule.minute`, `schedule.type`, `schedule.weekday`, `schedule?.type`

## pad()
- 位置: L175-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(value).padStart()`

## monitorTelemetryExtra()
- 位置: L187-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildScheduleTelemetryExtra()`, `monitorAgeMs()`
- 参照: `gMonitors?.size`, `monitor.activeSince`, `monitor.enabled`, `monitor.id`, `monitor.monitorPrompt.length`, `monitor.schedule`, `monitor.watchUrls.length`

## buildTelemetryContextExtra()
- 位置: L204-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`
- 条件付き依存: `if (source !== undefined)` → `CREATE_SOURCES.has()`
- 参照: `chatId.length`, `extra.chat_id`, `extra.message_seq`, `extra.source`

## buildCreationArgsExtra()
- 位置: L218-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `String()`, `buildScheduleTelemetryExtra()`
- 参照: `String(prompt ?? "").length`, `watchUrls.length`

## getCreationErrorCode()
- 位置: L227-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/invalid|cannot watch more than/i.test()`, `DOMException.isInstance()`
- 参照: `MONITOR_ERROR_CODES.INTERRUPTED`, `MONITOR_ERROR_CODES.UNKNOWN`, `error?.message`

## buildNotificationTelemetryExtra()
- 位置: L246-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `monitorTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.CONDITION_MET`, `extra.outcome`

## recordUpdateTelemetry()
- 位置: L267-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(updates).every()`, `buildTelemetryContextExtra()`, `monitorTelemetryExtra()`
- 条件付き依存: `if (!Object.keys(updates).every(key => key === "enabled"))` → `Glean.smartWindow.agenticActionEditComplete.record()`
- 条件付き依存: `if (monitor.enabled)` → `Glean.smartWindow.agenticActionResume.record()`
- 条件付き依存: `if (!(monitor.enabled))` → `Glean.smartWindow.agenticActionPause.record()`
- 参照: `monitor.enabled`

## init()
- 位置: async L299-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.values()`, `isShuttingDown()`, `monitor.getExpiryReason()`, `monitor.restore()`, `monitor.scheduleNextRun()`, `this._ensureLoaded()`
- 条件付き依存: `if (expiryReason)` → `this._expireMonitor()`
- 条件付き依存: `if (expiryReason)` → `lazy.log.error()`
- 参照: `monitor.enabled`, `monitor.id`

## uninit()
- 位置: L329-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.values()`, `monitor.dispose()`

## listMonitors()
- 位置: async L340-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `gMonitors.values()`, `monitor.toSerializable()`, `this._ensureLoaded()`

## createMonitor()
- 位置: async L359-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionCreateComplete.record()`, `Glean.smartWindow.agenticActionCreateSubmit.record()`, `buildCreationArgsExtra()`, `buildTelemetryContextExtra()`, `gMonitors.get()`, `getCreationErrorCode()`, `monitorTelemetryExtra()`, `this._createMonitor()`, `this._ensureLoaded()`, `this._ensureLoaded().then()`, `this._notifyMonitorCreated()`
- 参照: `gMonitors?.size`

## _createMonitor()
- 位置: async L401-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Schedule.fromJSON()`, `activeMonitorCount()`, `gMonitors.delete()`, `gMonitors.set()`, `monitor.scheduleNextRun()`, `this._ensureLoaded()`, `this._refreshInitialSnapshot()`, `this._saveAndNotify()`, `trimAndFilterWatchUrls()`
- 参照: `monitor.id`

## updateMonitor()
- 位置: async L435-548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.assign()`, `Object.fromEntries()`, `Object.keys()`, `Object.keys(next).map()`, `gMonitors.get()`, `monitor.scheduleNextRun()`, `monitor.watchUrls.slice()`, `new Date().toISOString()`, `recordUpdateTelemetry()`, `this._ensureLoaded()`, `this._saveAndNotify()`, `urlListsEqual()`
- 条件付き依存: `if ("monitorPrompt" in updates)` → `String(updates.monitorPrompt ?? "").trim()`
- 条件付き依存: `if ("monitorPrompt" in updates)` → `String()`
- 条件付き依存: `if ("watchUrls" in updates)` → `trimAndFilterWatchUrls()`
- 条件付き依存: `if ("title" in updates)` → `String(updates.title ?? "").trim()`
- 条件付き依存: `if ("title" in updates)` → `String()`
- 条件付き依存: `if ("schedule" in updates)` → `Schedule.fromJSON()`
- 条件付き依存: `if ("schedule" in updates)` → `next.schedule .getNextRunTime(new Date().toISOString()) .toISOString()`
- 条件付き依存: `if ("schedule" in updates)` → `next.schedule .getNextRunTime()`
- 条件付き依存: `if ("schedule" in updates)` → `new Date().toISOString()`
- 条件付き依存: `if (!monitor.enabled && next.enabled)` → `activeMonitorCount()`
- 条件付き依存: `if (!monitor.enabled && next.enabled)` → `next.schedule .getNextRunTime(new Date().toISOString()) .toISOString()`
- 条件付き依存: `if (!monitor.enabled && next.enabled)` → `next.schedule .getNextRunTime()`
- 条件付き依存: `if (!monitor.enabled && next.enabled)` → `new Date().toISOString()`
- 条件付き依存: `if (definitionChanged)` → `monitor.cancelSnapshotCapture()`
- 条件付き依存: `if (definitionChanged)` → `this._refreshInitialSnapshot()`
- 参照: `monitor.activeSince`, `monitor.enabled`, `monitor.expiry`, `monitor.monitorPrompt`, `monitor.nextRunTime`, `monitor.schedule`, `monitor.title`, `monitor.watchUrls`, `next.activeSince`, `next.enabled`, `next.expiry`, `next.initialSnapshot`, `next.monitorPrompt`, `next.nextRunTime`, `next.schedule`, `next.title`, `next.updatedAt`, `next.watchUrls`, `next.watchUrls.length`, `previous.enabled`, `updates.enabled`, `updates.monitorPrompt`, `updates.schedule`, `updates.title`, `updates.watchUrls`

## pauseMonitor()
- 位置: async L560-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.get()`, `this._ensureLoaded()`, `this.updateMonitor()`
- 参照: `monitor.enabled`

## deleteMonitor()
- 位置: async L591-617
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionDelete.record()`, `Services.obs.notifyObservers()`, `buildTelemetryContextExtra()`, `gMonitors.delete()`, `gMonitors.get()`, `gMonitors.set()`, `gSnapshotRefreshPromises.delete()`, `lazy.MonitorStore.deleteMonitor()`, `monitor.dispose()`, `monitor.restore()`, `monitor.scheduleNextRun()`, `monitorTelemetryExtra()`, `this._ensureLoaded()`, `this._updateActionGauges()`
- 参照: `MONITOR_ERROR_CODES.CANCELED`
- XPCOM: `Services.obs`

## runNow()
- 位置: async L619-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.get()`, `monitor.run()`, `this._ensureLoaded()`

## _ensureLoaded()
- 位置: async L628-651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isShuttingDown()`, `this._loadMonitors()`, `this._loadMonitors().catch()`

## _loadMonitors()
- 位置: async L653-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Monitor.fromJSON()`, `isShuttingDown()`, `lazy.MonitorStore.listMonitors()`, `lazy.log.warn()`, `monitors.set()`, `monitors.values()`, `seedNotifiedRunIds()`, `this._updateActionGauges()`
- 参照: `error.message`, `monitor.id`

## _refreshInitialSnapshot()
- 位置: L681-705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors?.get()`, `gSnapshotRefreshPromises.get()`, `gSnapshotRefreshPromises.set()`, `lazy.log.warn()`, `monitor .ensureInitialSnapshot()`, `monitor .ensureInitialSnapshot() .then()`, `refreshPromise .catch()`
- 条件付き依存: `if (gMonitors?.get(monitor.id) === monitor)` → `this._saveAndNotify()`
- 条件付き依存: `if (gSnapshotRefreshPromises.get(monitor.id) === refreshPromise)` → `gSnapshotRefreshPromises.delete()`
- 参照: `error.message`, `monitor.id`

## _saveAndNotify()
- 位置: async L707-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `gMonitors.has()`, `this._ensureLoaded()`, `this._updateActionGauges()`
- 条件付き依存: `if (monitor && gMonitors.has(monitor.id))` → `lazy.MonitorStore.saveMonitor()`
- 条件付き依存: `if (!(monitor && gMonitors.has(monitor.id)))` → `lazy.MonitorStore.saveMonitors()`
- 条件付き依存: `if (!(monitor && gMonitors.has(monitor.id)))` → `Array.from()`
- 条件付き依存: `if (!(monitor && gMonitors.has(monitor.id)))` → `gMonitors.values()`
- 条件付き依存: `if (monitor)` → `this._notifyIfConditionMet()`
- 条件付き依存: `if (monitor)` → `this._notifyIfRunFailed()`
- 参照: `monitor.id`
- XPCOM: `Services.obs`

## _updateActionGauges()
- 位置: L725-734
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agentActiveActions[AGENT_TYPE].set()`, `Glean.smartWindow.agentPausedActions[AGENT_TYPE].set()`, `activeMonitorCount()`
- 参照: `Glean.smartWindow.agentActiveActions`, `Glean.smartWindow.agentPausedActions`, `gMonitors.size`

## _telemetryExtra()
- 位置: L736-738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `monitorTelemetryExtra()`

## _expireMonitor()
- 位置: async L748-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionPause.record()`, `Object.assign()`, `lazy.log.info()`, `monitor.clearTimer()`, `monitor.schedule.getNextRunTime()`, `monitor.schedule.getNextRunTime(now).toISOString()`, `monitor.scheduleNextRun()`, `monitorTelemetryExtra()`, `new Date().toISOString()`, `this._notifyExpired()`, `this._saveAndNotify()`
- 参照: `monitor.enabled`, `monitor.expiry`, `monitor.id`, `monitor.nextRunTime`, `monitor.updatedAt`

## _notifyExpired()
- 位置: L786-836
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `expiryRuleDays()`, `this._showMonitorAlert()`
- 条件付き依存: `if (!bodyId)` → `lazy.log.error()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_ACTIONS.RESUME`, `NOTIFICATION_TYPES.EXPIRED`, `monitor.id`, `monitor.runCount`

## recordClick()
- 位置: L794-802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionNotificationClose.record()`, `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.EXPIRED`

## onClick()
- 位置: L813-825
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `recordClick()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `this.pauseMonitor(id, false).catch()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `this.pauseMonitor()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `lazy.log.error()`
- 条件付き依存: `if (!action)` → `recordClick()`
- 条件付き依存: `if (!action)` → `this._openWatchedUrl()`
- 参照: `NOTIFICATION_ACTIONS.RESUME`

## _notifyIfConditionMet()
- 位置: L850-888
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `gNotifiedRunIds.add()`, `gNotifiedRunIds.has()`, `monitor.history.at()`, `this._runNotificationActions()`, `this._showMonitorAlert()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.CONDITION_MET`, `entry.conditionMet`, `entry.id`, `entry.resultExplanation`, `entry.status`, `monitor.id`, `monitor.notificationsMuted`, `monitor.runCount`, `monitor.watchUrls.length`
- XPCOM: `Services.obs`

## _notifyIfRunFailed()
- 位置: L901-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `UNREPORTED_ERROR_CODES.has()`, `gNotifiedRunIds.add()`, `gNotifiedRunIds.has()`, `monitor.history.at()`, `this._runNotificationActions()`, `this._showMonitorAlert()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.RUN_FAILED`, `entry.errorCode`, `entry.id`, `entry.status`, `monitor.id`, `monitor.notificationsMuted`, `monitor.runCount`
- XPCOM: `Services.obs`

## _runNotificationActions()
- 位置: L957-1004
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `NOTIFICATION_ACTIONS.DISMISS`, `NOTIFICATION_ACTIONS.SNOOZE`, `monitor.id`, `monitor.watchUrls`

## recordClick()
- 位置: L960-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agenticActionNotificationClose.record()`, `buildNotificationTelemetryExtra()`

## onClick()
- 位置: L981-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (url)` → `recordClick()`
- 条件付き依存: `if (url)` → `this._openWatchedUrl()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.SNOOZE)` → `recordClick()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.SNOOZE)` → `this.snoozeMonitor(id).catch()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.SNOOZE)` → `this.snoozeMonitor()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.SNOOZE)` → `lazy.log.error()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.DISMISS)` → `recordClick()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.DISMISS)` → `this.muteMonitorNotifications(id).catch()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.DISMISS)` → `this.muteMonitorNotifications()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.DISMISS)` → `lazy.log.error()`
- 参照: `NOTIFICATION_ACTIONS.DISMISS`, `NOTIFICATION_ACTIONS.SNOOZE`

## _notifyMonitorCreated()
- 位置: L1013-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `this._showMonitorAlert()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.CREATED`, `URL.parse(monitor.watchUrls[0])?.hostname`, `monitor.runCount`, `monitor.watchUrls`, `monitor.watchUrls.length`

## onClick()
- 位置: L1021-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!action)` → `Glean.smartWindow.agenticActionNotificationClose.record()`
- 条件付き依存: `if (!action)` → `buildNotificationTelemetryExtra()`
- 条件付き依存: `if (!action)` → `this._openWatchedUrl()`
- 参照: `NOTIFICATION_TYPES.CREATED`

## _showMonitorAlert()
- 位置: L1062-1102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/alerts-service;1"].getService()`, `actions.map()`, `alertsService.showAlert()`, `lazy.l10n.formatValuesSync()`, `lazy.log.error()`
- 参照: `Ci.nsIAlertsService`, `monitor.title`
- XPCOM: [`nsIAlertsService`](../../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / `@mozilla.org/alerts-service;1`

## observe()
- 位置: L1078-1085
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onClick()`, `subject.QueryInterface()`
- 参照: `Ci.nsIAlertAction`, `subject.QueryInterface(Ci.nsIAlertAction).action`
- XPCOM: [`nsIAlertAction`](../../../../../toolkit/components/alerts/nsIAlertsService.idl.md)

## _openWatchedUrl()
- 位置: L1111-1122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.BrowserWindowTracker.openWindow()`
- 条件付き依存: `if (win)` → `win.openTrustedLinkIn()`
- 参照: `Ci.nsISupportsString`, `args.data`
- XPCOM: [`nsISupportsString`](../../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`

## snoozeMonitor()
- 位置: async L1130-1145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `gMonitors.get()`, `monitor.schedule.getNextRunTime()`, `monitor.scheduleNextRun()`, `next.getTime()`, `next.toISOString()`, `this._ensureLoaded()`, `this._saveAndNotify()`
- 参照: `monitor.lastRunTime`, `monitor.nextRunTime`

## muteMonitorNotifications()
- 位置: async L1152-1160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.get()`, `this._ensureLoaded()`, `this._saveAndNotify()`
- 参照: `monitor.notificationsMuted`

## _unloadForTesting()
- 位置: L1162-1169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNotifiedRunIds.clear()`, `gSnapshotRefreshPromises.clear()`, `this.uninit()`

## _waitForSnapshotForTesting()
- 位置: async L1177-1192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMonitors.get()`, `gSnapshotRefreshPromises.get()`, `this._ensureLoaded()`
- 参照: `monitor.initialSnapshot`

## _resetForTesting()
- 位置: async L1194-1197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorStore.destroyDatabase()`, `this._unloadForTesting()`
