# browser/modules/UpdatePolicyEnforcer.sys.mjs

source: browser/modules/UpdatePolicyEnforcer.sys.mjs
source-hash: f087af5f3a02159e69d6ab99bbdb29d95b2184fa
lines: 267

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## forceRestart()
- 位置: L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.quit()`, `lazy.logConsole.warn()`
- 参照: `Services.startup.eForceQuit`, `Services.startup.eRestart`
- XPCOM: `Services.startup`

## infobarDispatchCallback()
- 位置: L31-39
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (action?.type === "USER_ACTION" && action.data?.type === "RESTART_APP")` → `forceRestart()`
- 条件付き依存: `if (!(action?.type === "USER_ACTION" && action.data?.type === "RESTART_APP"))` → `lazy.logConsole.debug()`
- 参照: `action.data?.type`, `action?.type`

## showNotificationToolbar()
- 位置: L42-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.InfoBar.showInfoBarMessage()`, `lazy.logConsole.info()`
- 参照: `restartZonedDateTime.epochMilliseconds`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## testingOnly_resetTasks()
- 位置: L90-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferredRestartTasks?.notificationTask?.disarm()`, `deferredRestartTasks?.restartTask?.disarm()`
- 参照: `Cu.isInAutomation`

## testingOnly_getTaskStatus()
- 位置: L102-114
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cu.isInAutomation`, `deferredRestartTasks.notificationTask?.isArmed`, `deferredRestartTasks.restartTask?.isArmed`

## calculateSchedule()
- 位置: L131-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Temporal.Duration.compare()`, `Temporal.Duration.from()`, `Temporal.Now.timeZoneId()`, `Temporal.PlainTime.from()`, `lazy.logConsole.debug()`, `notificationInstant.toZonedDateTimeISO()`, `notificationZonedDateTime.until()`, `notificationZonedDateTime.withPlainTime()`, `nowInstant.add()`
- 条件付き依存: `if ( Temporal.Duration.compare( notificationZonedDateTime.until(restartZonedDateTime), Temporal.Duration.from({ hours: 1 }) ) < 0 )` → `restartZonedDateTime.add()`
- 条件付き依存: `if ( Temporal.Duration.compare( notificationZonedDateTime.until(restartZonedDateTime), Temporal.Duration.from({ hours: 1 }) ) < 0 )` → `Temporal.Duration.from()`
- 参照: `restartTimeOfDay.Hour`, `restartTimeOfDay.Minute`

## createScheduledRestartTasks()
- 位置: L175-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.info()`, `notificationTask.arm()`, `restartTask.arm()`, `showNotificationToolbar()`
- 参照: `lazy.ScheduledTask`, `notificationZonedDateTime.epochMilliseconds`, `restartZonedDateTime.epochMilliseconds`

## getCompulsoryRestartPolicy()
- 位置: L199-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (compulsoryRestartSettingStr)` → `JSON.parse()`
- 条件付き依存: `if ( typeof compulsoryRestartSetting?.NotificationPeriodHours === "number" && typeof compulsoryRestartSetting?.RestartTimeOfDay === "object" && typeof compulsory...)` → `lazy.logConsole.debug()`
- 参照: `compulsoryRestartSetting.RestartTimeOfDay.Hour`, `compulsoryRestartSetting.RestartTimeOfDay.Minute`, `compulsoryRestartSetting?.NotificationPeriodHours`, `compulsoryRestartSetting?.RestartTimeOfDay`
- XPCOM: `Services.prefs`

## handleCompulsoryUpdatePolicy()
- 位置: L225-248
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!deferredRestartTasks)` → `getCompulsoryRestartPolicy()`
- 条件付き依存: `if (compulsoryRestartSetting)` → `Temporal.Now.instant()`
- 条件付き依存: `if (compulsoryRestartSetting)` → `calculateSchedule()`
- 条件付き依存: `if (restartZonedDateTime && notificationZonedDateTime)` → `createScheduledRestartTasks()`
- 条件付き依存: `if (!(restartZonedDateTime && notificationZonedDateTime))` → `lazy.logConsole.error()`
- 条件付き依存: `if (!(restartZonedDateTime && notificationZonedDateTime))` → `JSON.stringify()`
- 参照: `compulsoryRestartSetting.NotificationPeriodHours`, `compulsoryRestartSetting.RestartTimeOfDay`

## observe()
- 位置: L251-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleCompulsoryUpdatePolicy()`

## registerObservers()
- 位置: L262-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`
