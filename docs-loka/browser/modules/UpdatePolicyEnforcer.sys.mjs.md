# browser/modules/UpdatePolicyEnforcer.sys.mjs

source: browser/modules/UpdatePolicyEnforcer.sys.mjs
source-hash: f087af5f3a02159e69d6ab99bbdb29d95b2184fa
lines: 267

## <module>
- 役割: 更新の適用後にポリシーで決まった時刻に強制再起動する予定を組み、再起動前の通知バーを出す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## forceRestart()
- 位置: L24-29
- 役割: 終了確認を待たずに Firefox を強制終了して再起動する。
- 触るとき: 強制再起動の方法や、再起動前に閉じられる処理を変えるとき。
- 呼び出し先: `Services.startup.quit()`, `lazy.logConsole.warn()`
- 参照: `Services.startup.eForceQuit`, `Services.startup.eRestart`
- XPCOM: `Services.startup`

## infobarDispatchCallback()
- 位置: L31-39
- 役割: 通知バーの RESTART_APP 操作を受けたら forceRestart を呼び、それ以外は debug ログに残す。
- 触るとき: 通知バーのボタン操作と再起動の対応を変えるとき。
- 条件付き依存: `if (action?.type === "USER_ACTION" && action.data?.type === "RESTART_APP")` → `forceRestart()`
- 条件付き依存: `if (!(action?.type === "USER_ACTION" && action.data?.type === "RESTART_APP"))` → `lazy.logConsole.debug()`
- 参照: `action.data?.type`, `action?.type`

## showNotificationToolbar()
- 位置: L42-85
- 役割: 再起動予定時刻を属性に持つ、閉じられない通知バーを最近使われたブラウザーウィンドウの選択中タブに表示する。
- 触るとき: 再起動前の通知の文言、優先度、ボタンを変えるとき。
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.InfoBar.showInfoBarMessage()`, `lazy.logConsole.info()`
- 参照: `restartZonedDateTime.epochMilliseconds`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## testingOnly_resetTasks()
- 位置: L90-97
- 役割: テスト専用で、予約済みの通知タスクと再起動タスクを解除して状態を捨てる。
- 触るとき: テストの間で予約が残って次のテストに影響する問題を調べるとき。
- 呼び出し先: `deferredRestartTasks?.notificationTask?.disarm()`, `deferredRestartTasks?.restartTask?.disarm()`
- 参照: `Cu.isInAutomation`

## testingOnly_getTaskStatus()
- 位置: L102-114
- 役割: テスト専用で、2つのタスクがそれぞれ予約中かを返す。作られていなければ null を返す。
- 触るとき: テストで再起動の予約が入ったかどうかを確認するとき。
- 参照: `Cu.isInAutomation`, `deferredRestartTasks.notificationTask?.isArmed`, `deferredRestartTasks.restartTask?.isArmed`

## calculateSchedule()
- 位置: L131-172
- 役割: 通知開始時刻を現在時刻に通知期間(時間)を足した時刻とし、その日の再起動時刻を求める。通知から1時間未満しかない場合は24時間後に回す。
- 触るとき: 通知期間や再起動時刻の計算を変えるとき、再起動予定が翌日にずれる理由を調べるとき。
- 呼び出し先: `Temporal.Duration.compare()`, `Temporal.Duration.from()`, `Temporal.Now.timeZoneId()`, `Temporal.PlainTime.from()`, `lazy.logConsole.debug()`, `notificationInstant.toZonedDateTimeISO()`, `notificationZonedDateTime.until()`, `notificationZonedDateTime.withPlainTime()`, `nowInstant.add()`
- 条件付き依存: `if ( Temporal.Duration.compare( notificationZonedDateTime.until(restartZonedDateTime), Temporal.Duration.from({ hours: 1 }) ) < 0 )` → `restartZonedDateTime.add()`
- 条件付き依存: `if ( Temporal.Duration.compare( notificationZonedDateTime.until(restartZonedDateTime), Temporal.Duration.from({ hours: 1 }) ) < 0 )` → `Temporal.Duration.from()`
- 参照: `restartTimeOfDay.Hour`, `restartTimeOfDay.Minute`

## createScheduledRestartTasks()
- 位置: L175-196
- 役割: 通知用と再起動用の ScheduledTask を作って両方予約し、再起動用にはスリープ復帰後の遅延として5分を渡す。
- 触るとき: 予約タスクのタイミングや遅延の扱いを変えるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.info()`, `notificationTask.arm()`, `restartTask.arm()`, `showNotificationToolbar()`
- 参照: `lazy.ScheduledTask`, `notificationZonedDateTime.epochMilliseconds`, `restartZonedDateTime.epochMilliseconds`

## getCompulsoryRestartPolicy()
- 位置: L199-220
- 役割: app.update.compulsory_restart の JSON を読み、通知期間と再起動時刻(時・分)が数値として揃っていれば返し、そうでなければ null を返す。
- 触るとき: ポリシーの設定形式を変えるとき、ポリシーが効かない原因を調べるとき。
- 呼び出し先: `Services.prefs.getStringPref()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (compulsoryRestartSettingStr)` → `JSON.parse()`
- 条件付き依存: `if ( typeof compulsoryRestartSetting?.NotificationPeriodHours === "number" && typeof compulsoryRestartSetting?.RestartTimeOfDay === "object" && typeof compulsory...)` → `lazy.logConsole.debug()`
- 参照: `compulsoryRestartSetting.RestartTimeOfDay.Hour`, `compulsoryRestartSetting.RestartTimeOfDay.Minute`, `compulsoryRestartSetting?.NotificationPeriodHours`, `compulsoryRestartSetting?.RestartTimeOfDay`
- XPCOM: `Services.prefs`

## handleCompulsoryUpdatePolicy()
- 位置: L225-248
- 役割: 予約済みでなくポリシーがあれば、現在時刻から再起動の計画を作って予約する。計画が不正なら error ログに残す。
- 触るとき: 更新のステージ後に強制再起動の予約が入らない問題を調べるとき。
- 条件付き依存: `if (!deferredRestartTasks)` → `getCompulsoryRestartPolicy()`
- 条件付き依存: `if (compulsoryRestartSetting)` → `Temporal.Now.instant()`
- 条件付き依存: `if (compulsoryRestartSetting)` → `calculateSchedule()`
- 条件付き依存: `if (restartZonedDateTime && notificationZonedDateTime)` → `createScheduledRestartTasks()`
- 条件付き依存: `if (!(restartZonedDateTime && notificationZonedDateTime))` → `lazy.logConsole.error()`
- 条件付き依存: `if (!(restartZonedDateTime && notificationZonedDateTime))` → `JSON.stringify()`
- 参照: `compulsoryRestartSetting.NotificationPeriodHours`, `compulsoryRestartSetting.RestartTimeOfDay`

## observe()
- 位置: L251-258
- 役割: update-downloaded または update-staged を受けたら handleCompulsoryUpdatePolicy を呼ぶ。
- 触るとき: 予約を始めるきっかけとなる更新の通知を増やす・減らすとき。
- 呼び出し先: `handleCompulsoryUpdatePolicy()`

## registerObservers()
- 位置: L262-265
- 役割: update-downloaded と update-staged を監視対象として登録する。
- 触るとき: 予約が始まらない問題で、監視が登録されているか確認するとき。
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`
