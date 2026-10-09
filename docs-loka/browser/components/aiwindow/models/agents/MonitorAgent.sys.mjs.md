# browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs

source: browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs
source-hash: fb6d7827fd95f6065412ddde08803f83baeba170
lines: 1199

## <module>
- 役割: 監視エージェントの本体。監視の作成、更新、一時停止、削除、手動実行を管理し、保存、変更通知、デスクトップ通知、自動失効、telemetry を扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`, `Object.freeze()`, `console.createInstance()`

## seedNotifiedRunIds()
- 位置: L120-128
- 役割: 起動時に読み込んだ監視の履歴のうち、一致または失敗のものを通知済みとして記録する。
- 触るとき: 再起動時に過去の結果が通知として再表示される問題を調べるとき。
- 条件付き依存: `if (entry.conditionMet || entry.status === "error")` → `gNotifiedRunIds.add()`
- 参照: `entry.conditionMet`, `entry.id`, `entry.status`, `monitor.history`

## isShuttingDown()
- 位置: L130-137
- 役割: アプリ終了が始まっているか(内部フラグまたはシャットダウン段階)を返す。
- 触るとき: 終了処理中に新しい読み込みや保存を止める条件を変えるとき。
- 呼び出し先: `Services.startup.isInOrBeyondShutdownPhase()`
- 参照: `Ci.nsIAppStartup.SHUTDOWN_PHASE_APPSHUTDOWNCONFIRMED`
- XPCOM: [`nsIAppStartup`](../../../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## MonitorAgentShutdownError.constructor()
- 位置: L144-147
- 役割: 終了処理で監視の操作が中断されたことを示す例外を作る。
- 触るとき: 終了中の中断を別扱いにする箇所を追加するとき。
- 呼び出し先: `super()`
- 参照: `this.name`

## activeMonitorCount()
- 位置: L150-158
- 役割: 有効(enabled)な監視の数を数える。一時停止中は数えない。
- 触るとき: 監視の上限(TOTAL_NUM_MONITORS)の判定を変えるとき。
- 呼び出し先: `gMonitors.values()`
- 参照: `monitor.enabled`

## isClockField()
- 位置: L160-162
- 役割: 時・分・曜日の値が整数で範囲内かを判定する。
- 触るとき: スケジュールの時刻フィールドの検証範囲を変えるとき。
- 呼び出し先: `Number.isInteger()`

## buildScheduleTelemetryExtra()
- 位置: L166-185
- 役割: スケジュールの種類と、妥当なら時刻(HH:MM)と曜日を telemetry 用に組み立てる。
- 触るとき: スケジュール関連の telemetry 項目を増やすとき。
- 呼び出し先: `Object.values()`, `Object.values(SCHEDULE_TYPES).includes()`, `isClockField()`
- 条件付き依存: `if (isClockField(schedule.hour, 23) && isClockField(schedule.minute, 59))` → `pad()`
- 参照: `SCHEDULE_TYPES.INTERVAL`, `SCHEDULE_TYPES.WEEKLY`, `extra.check_time`, `extra.check_weekday`, `schedule.hour`, `schedule.minute`, `schedule.type`, `schedule.weekday`, `schedule?.type`

## pad()
- 位置: L175-175
- 役割: 数値を 2 桁の文字列にする(0 埋め)。
- 触るとき: 時刻表示の桁数の形式を変えるとき。
- 呼び出し先: `String()`, `String(value).padStart()`

## monitorTelemetryExtra()
- 位置: L187-200
- 役割: 監視の件数、URL 数、プロンプト長、経過時間、有効状態などを共通の telemetry 項目にまとめる。
- 触るとき: 監視の全 telemetry に共通で載せる項目を増やすとき。
- 呼び出し先: `buildScheduleTelemetryExtra()`, `monitorAgeMs()`
- 参照: `gMonitors?.size`, `monitor.activeSince`, `monitor.enabled`, `monitor.id`, `monitor.monitorPrompt.length`, `monitor.schedule`, `monitor.watchUrls.length`

## buildTelemetryContextExtra()
- 位置: L204-216
- 役割: 呼び出し元が渡した source、chatId、messageSeq を検証して telemetry 項目にする。source は許可リスト外なら unknown になる。
- 触るとき: チャット起点の操作で送る文脈情報の検証条件を変えるとき。
- 呼び出し先: `Number.isInteger()`
- 条件付き依存: `if (source !== undefined)` → `CREATE_SOURCES.has()`
- 参照: `chatId.length`, `extra.chat_id`, `extra.message_seq`, `extra.source`

## buildCreationArgsExtra()
- 位置: L218-225
- 役割: 作成要求の URL 数、プロンプト長、スケジュールを、作成時の telemetry 項目にする。
- 触るとき: 作成要求の telemetry に載せる入力情報を変えるとき。
- 呼び出し先: `Array.isArray()`, `String()`, `buildScheduleTelemetryExtra()`
- 参照: `String(prompt ?? "").length`, `watchUrls.length`

## getCreationErrorCode()
- 位置: L227-242
- 役割: 作成失敗の例外を、中断、storage_error、limit_reached、invalid_input、unknown の順に分類する。
- 触るとき: 作成失敗の telemetry の分類を変えるとき、または作成が失敗した理由の分類結果を調べるとき。
- 呼び出し先: `/invalid|cannot watch more than/i.test()`, `DOMException.isInstance()`
- 参照: `MONITOR_ERROR_CODES.INTERRUPTED`, `MONITOR_ERROR_CODES.UNKNOWN`, `error?.message`

## buildNotificationTelemetryExtra()
- 位置: L246-260
- 役割: 通知に関する telemetry 項目を作る。種類を付け、条件一致の通知では outcome を true にする。
- 触るとき: 通知の telemetry に項目を追加するとき。
- 呼び出し先: `monitorTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.CONDITION_MET`, `extra.outcome`

## recordUpdateTelemetry()
- 位置: L267-289
- 役割: 更新内容に応じて edit、resume、pause の telemetry を送る。enabled だけの変更は edit として送らない。
- 触るとき: 編集、再開、一時停止の telemetry の区分けを変えるとき。
- 呼び出し先: `Object.keys()`, `Object.keys(updates).every()`, `buildTelemetryContextExtra()`, `monitorTelemetryExtra()`
- 条件付き依存: `if (!Object.keys(updates).every(key => key === "enabled"))` → `Glean.smartWindow.agenticActionEditComplete.record()`
- 条件付き依存: `if (monitor.enabled)` → `Glean.smartWindow.agenticActionResume.record()`
- 条件付き依存: `if (!(monitor.enabled))` → `Glean.smartWindow.agenticActionPause.record()`
- 参照: `monitor.enabled`

## init()
- 位置: async L299-327
- 役割: 起動時に監視を読み込み、期限切れのものは即座に停止させ、それ以外は次回の実行を予約する。
- 触るとき: 起動時の監視の再開や、期限切れの監視をどう扱うかを変えるとき。
- 呼び出し先: `gMonitors.values()`, `isShuttingDown()`, `monitor.getExpiryReason()`, `monitor.restore()`, `monitor.scheduleNextRun()`, `this._ensureLoaded()`
- 条件付き依存: `if (expiryReason)` → `this._expireMonitor()`
- 条件付き依存: `if (expiryReason)` → `lazy.log.error()`
- 参照: `monitor.enabled`, `monitor.id`

## uninit()
- 位置: L329-338
- 役割: 終了フラグを立て、読み込み済みの全監視を破棄する。
- 触るとき: アプリ終了時に進行中の監視をどう止めるかを変えるとき。
- 呼び出し先: `gMonitors.values()`, `monitor.dispose()`

## listMonitors()
- 位置: async L340-343
- 役割: 読み込み後、全監視を保存用の平らなオブジェクトの配列で返す。
- 触るとき: 監視一覧の画面に渡すデータの形を変えるとき。
- 呼び出し先: `Array.from()`, `gMonitors.values()`, `monitor.toSerializable()`, `this._ensureLoaded()`

## createMonitor()
- 位置: async L359-399
- 役割: 作成要求を受けて作成 telemetry(submit と complete)を送り、成功時は作成完了の通知を出す。失敗時は分類したエラーコードを送って例外を投げ直す。
- 触るとき: 監視の作成フローや作成時の telemetry を変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionCreateComplete.record()`, `Glean.smartWindow.agenticActionCreateSubmit.record()`, `buildCreationArgsExtra()`, `buildTelemetryContextExtra()`, `gMonitors.get()`, `getCreationErrorCode()`, `monitorTelemetryExtra()`, `this._createMonitor()`, `this._ensureLoaded()`, `this._ensureLoaded().then()`, `this._notifyMonitorCreated()`
- 参照: `gMonitors?.size`

## _createMonitor()
- 位置: async L401-423
- 役割: 上限を確認し、URL とスケジュールから監視を作って保存し、次回実行を予約して初期スナップショットを背景で取得する。
- 触るとき: 監視の新規作成の検証や保存の順序を変えるとき。
- 呼び出し先: `Schedule.fromJSON()`, `activeMonitorCount()`, `gMonitors.delete()`, `gMonitors.set()`, `monitor.scheduleNextRun()`, `this._ensureLoaded()`, `this._refreshInitialSnapshot()`, `this._saveAndNotify()`, `trimAndFilterWatchUrls()`
- 参照: `monitor.id`

## updateMonitor()
- 位置: async L435-548
- 役割: 監視の定義や有効状態を更新する。定義が変わると初期スナップショットを撮り直し、再開時は期限の起点を今に戻す。保存に失敗したら元の値に戻す。
- 触るとき: 監視の編集で何が編集扱いになるか(定義の変更、再開、一時停止)を変えるとき。
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
- 役割: pause の指定に応じて有効状態を切り替え、updateMonitor に任せる。pause が未指定なら現在の状態を反転する。
- 触るとき: 一時停止と再開の入口の振る舞いを変えるとき。
- 呼び出し先: `gMonitors.get()`, `this._ensureLoaded()`, `this.updateMonitor()`
- 参照: `monitor.enabled`

## deleteMonitor()
- 位置: async L591-617
- 役割: 監視を破棄して一覧から外し、保存から消す。失敗したら元に戻す。成功すると変更通知と削除の telemetry を送る。
- 触るとき: 監視の削除手順や削除に失敗したときの戻し方を変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionDelete.record()`, `Services.obs.notifyObservers()`, `buildTelemetryContextExtra()`, `gMonitors.delete()`, `gMonitors.get()`, `gMonitors.set()`, `gSnapshotRefreshPromises.delete()`, `lazy.MonitorStore.deleteMonitor()`, `monitor.dispose()`, `monitor.restore()`, `monitor.scheduleNextRun()`, `monitorTelemetryExtra()`, `this._ensureLoaded()`, `this._updateActionGauges()`
- 参照: `MONITOR_ERROR_CODES.CANCELED`
- XPCOM: `Services.obs`

## runNow()
- 位置: async L619-626
- 役割: 指定の監視を手動実行(manual)で 1 回走らせる。
- 触るとき: 今すぐ確認ボタンの動作を変えるとき。
- 呼び出し先: `gMonitors.get()`, `monitor.run()`, `this._ensureLoaded()`

## _ensureLoaded()
- 位置: async L628-651
- 役割: 監視の読み込みを 1 回だけ行い、終了中なら例外を投げる。読み込み中の呼び出しは同じ読み込みを待つ。
- 触るとき: 読み込みの重複や、終了中の操作の扱いを変えるとき。
- 呼び出し先: `isShuttingDown()`, `this._loadMonitors()`, `this._loadMonitors().catch()`

## _loadMonitors()
- 位置: async L653-672
- 役割: 保存済みの監視を復元する。壊れたものは警告を出して飛ばし、読み込み後に通知済み履歴を整える。
- 触るとき: 保存データが壊れていたときの扱いや、起動時の読み込み順を変えるとき。
- 呼び出し先: `Monitor.fromJSON()`, `isShuttingDown()`, `lazy.MonitorStore.listMonitors()`, `lazy.log.warn()`, `monitors.set()`, `monitors.values()`, `seedNotifiedRunIds()`, `this._updateActionGauges()`
- 参照: `error.message`, `monitor.id`

## _refreshInitialSnapshot()
- 位置: L681-705
- 役割: 初期スナップショットを背景で取得し、完了後に監視を保存する。失敗は警告ログだけで、呼び出し元には影響させない。
- 触るとき: 作成や編集の後の基準ページの取得タイミングを変えるとき。
- 呼び出し先: `gMonitors?.get()`, `gSnapshotRefreshPromises.get()`, `gSnapshotRefreshPromises.set()`, `lazy.log.warn()`, `monitor .ensureInitialSnapshot()`, `monitor .ensureInitialSnapshot() .then()`, `refreshPromise .catch()`
- 条件付き依存: `if (gMonitors?.get(monitor.id) === monitor)` → `this._saveAndNotify()`
- 条件付き依存: `if (gSnapshotRefreshPromises.get(monitor.id) === refreshPromise)` → `gSnapshotRefreshPromises.delete()`
- 参照: `error.message`, `monitor.id`

## _saveAndNotify()
- 位置: async L707-723
- 役割: 監視 1 件、または全件を保存し、表示用の値を更新して変更通知を出す。1 件保存のときは条件一致と失敗の通知を判定する。
- 触るとき: 保存と通知をまとめて行う経路を変えるとき、または保存のたびに通知が出る理由を追うとき。
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
- 役割: 有効と停止中の監視数を、計測用のゲージに書き込む。
- 触るとき: 監視数の計測値の定義を変えるとき。
- 呼び出し先: `Glean.smartWindow.agentActiveActions[AGENT_TYPE].set()`, `Glean.smartWindow.agentPausedActions[AGENT_TYPE].set()`, `activeMonitorCount()`
- 参照: `Glean.smartWindow.agentActiveActions`, `Glean.smartWindow.agentPausedActions`, `gMonitors.size`

## _telemetryExtra()
- 位置: L736-738
- 役割: 監視 1 件の共通 telemetry 項目を返す。Monitor 側の buildRunTelemetryExtra から呼ばれる。
- 触るとき: 実行系 telemetry の共通項目を Monitor 側と合わせて変えるとき。
- 呼び出し先: `monitorTelemetryExtra()`

## _expireMonitor()
- 位置: async L748-775
- 役割: 監視を自動停止し、理由と時刻を記録して保存する。保存に失敗したら元に戻し、次の予定時刻に再予約する。成功すると pause の telemetry と期限切れの通知を出す。
- 触るとき: 自動停止の記録や失敗時のリトライのタイミングを変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionPause.record()`, `Object.assign()`, `lazy.log.info()`, `monitor.clearTimer()`, `monitor.schedule.getNextRunTime()`, `monitor.schedule.getNextRunTime(now).toISOString()`, `monitor.scheduleNextRun()`, `monitorTelemetryExtra()`, `new Date().toISOString()`, `this._notifyExpired()`, `this._saveAndNotify()`
- 参照: `monitor.enabled`, `monitor.expiry`, `monitor.id`, `monitor.nextRunTime`, `monitor.updatedAt`

## _notifyExpired()
- 位置: L786-836
- 役割: 自動停止の通知を出す。本文は失効理由ごとに変え、再開ボタンとクリック時の処理(再開、またはタスク画面を開く)を付ける。
- 触るとき: 自動停止の通知文言やボタンを変えるとき。通知はミュート中でも出す。
- 呼び出し先: `expiryRuleDays()`, `this._showMonitorAlert()`
- 条件付き依存: `if (!bodyId)` → `lazy.log.error()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_ACTIONS.RESUME`, `NOTIFICATION_TYPES.EXPIRED`, `monitor.id`, `monitor.runCount`

## recordClick()
- 位置: L794-802
- 役割: 期限切れ通知を閉じたときの理由を telemetry に記録する。
- 触るとき: 期限切れ通知の操作の telemetry 項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionNotificationClose.record()`, `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.EXPIRED`

## onClick()
- 位置: L813-825
- 役割: 期限切れ通知がクリックされたとき、再開なら監視を再開し、本文クリックならタスク画面を開く。
- 触るとき: 期限切れ通知のクリック後の動作を変えるとき。
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `recordClick()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `this.pauseMonitor(id, false).catch()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `this.pauseMonitor()`
- 条件付き依存: `if (action === NOTIFICATION_ACTIONS.RESUME)` → `lazy.log.error()`
- 条件付き依存: `if (!action)` → `recordClick()`
- 条件付き依存: `if (!action)` → `this._openWatchedUrl()`
- 参照: `NOTIFICATION_ACTIONS.RESUME`

## _notifyIfConditionMet()
- 位置: L850-888
- 役割: 直近の履歴が条件一致なら、監視の通知済み ID に加えて一致の通知を出す。ミュート中は通知を出さず、通知を出したら表示の telemetry を送る。
- 触るとき: 条件一致時の通知を出す条件やミュートの扱いを変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `gNotifiedRunIds.add()`, `gNotifiedRunIds.has()`, `monitor.history.at()`, `this._runNotificationActions()`, `this._showMonitorAlert()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.CONDITION_MET`, `entry.conditionMet`, `entry.id`, `entry.resultExplanation`, `entry.status`, `monitor.id`, `monitor.notificationsMuted`, `monitor.runCount`, `monitor.watchUrls.length`
- XPCOM: `Services.obs`

## _notifyIfRunFailed()
- 位置: L901-943
- 役割: 直近の履歴が失敗なら、キャンセルと中断を除いて失敗の通知を出す。ミュート中は通知を出さない。
- 触るとき: 実行失敗の通知をどの失敗に出すかを変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `UNREPORTED_ERROR_CODES.has()`, `gNotifiedRunIds.add()`, `gNotifiedRunIds.has()`, `monitor.history.at()`, `this._runNotificationActions()`, `this._showMonitorAlert()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.RUN_FAILED`, `entry.errorCode`, `entry.id`, `entry.status`, `monitor.id`, `monitor.notificationsMuted`, `monitor.runCount`
- XPCOM: `Services.obs`

## _runNotificationActions()
- 位置: L957-1004
- 役割: 実行に関する通知の共通ボタン(スヌーズ、無視)と、本文クリックで監視対象ページを開く処理を組み立てる。
- 触るとき: 実行結果の通知に付けるボタンやクリック時の動作を変えるとき。
- 参照: `NOTIFICATION_ACTIONS.DISMISS`, `NOTIFICATION_ACTIONS.SNOOZE`, `monitor.id`, `monitor.watchUrls`

## recordClick()
- 位置: L960-968
- 役割: 実行結果の通知を閉じたときの理由を telemetry に記録する。
- 触るとき: 実行結果の通知の操作の telemetry を変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionNotificationClose.record()`, `buildNotificationTelemetryExtra()`

## onClick()
- 位置: L981-1002
- 役割: 実行結果の通知がクリックされたとき、本文なら対象ページを開き、スヌーズ、無視のボタンなら対応する処理を呼ぶ。
- 触るとき: 実行結果の通知のボタンの挙動を変えるとき。
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
- 役割: 監視の作成直後に、最初の URL のホスト名と残りの件数を入れた通知を出す。クリックでタスク画面を開く。
- 触るとき: 作成時の通知の文言や telemetry を変えるとき。
- 呼び出し先: `URL.parse()`, `this._showMonitorAlert()`
- 条件付き依存: `if (shown)` → `Glean.smartWindow.agenticActionNotificationDisplay.record()`
- 条件付き依存: `if (shown)` → `buildNotificationTelemetryExtra()`
- 参照: `NOTIFICATION_TYPES.CREATED`, `URL.parse(monitor.watchUrls[0])?.hostname`, `monitor.runCount`, `monitor.watchUrls`, `monitor.watchUrls.length`

## onClick()
- 位置: L1021-1033
- 役割: 作成時の通知が本文クリックされたら、作成通知の閉じ telemetry を送ってタスク画面を開く。
- 触るとき: 作成時の通知のクリック後の動作を変えるとき。
- 条件付き依存: `if (!action)` → `Glean.smartWindow.agenticActionNotificationClose.record()`
- 条件付き依存: `if (!action)` → `buildNotificationTelemetryExtra()`
- 条件付き依存: `if (!action)` → `this._openWatchedUrl()`
- 参照: `NOTIFICATION_TYPES.CREATED`

## _showMonitorAlert()
- 位置: L1062-1102
- 役割: Fluent の文言から通知を作って表示する。監視名をタイトルにし、クリックを受け取る。失敗は例外にせず false を返す。
- 触るとき: デスクトップ通知の表示方法や文言の取り方を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/alerts-service;1"].getService()`, `actions.map()`, `alertsService.showAlert()`, `lazy.l10n.formatValuesSync()`, `lazy.log.error()`
- 参照: `Ci.nsIAlertsService`, `monitor.title`
- XPCOM: [`nsIAlertsService`](../../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / `@mozilla.org/alerts-service;1`

## observe()
- 位置: L1078-1085
- 役割: 通知がクリックされたとき、ボタンの action 名を取り出して onClick に渡す。
- 触るとき: 通知クリックの受け取り方を変えるとき。
- 呼び出し先: `onClick()`, `subject.QueryInterface()`
- 参照: `Ci.nsIAlertAction`, `subject.QueryInterface(Ci.nsIAlertAction).action`
- XPCOM: [`nsIAlertAction`](../../../../../toolkit/components/alerts/nsIAlertsService.idl.md)

## _openWatchedUrl()
- 位置: L1111-1122
- 役割: 通常のウィンドウがあればその新しいタブで URL を開き、無ければ新しいウィンドウを作って開く。
- 触るとき: 通知から監視対象ページを開く先を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.BrowserWindowTracker.openWindow()`
- 条件付き依存: `if (win)` → `win.openTrustedLinkIn()`
- 参照: `Ci.nsISupportsString`, `args.data`
- XPCOM: [`nsISupportsString`](../../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`

## snoozeMonitor()
- 位置: async L1130-1145
- 役割: 今から 24 時間は実行しないよう、スケジュールに沿って次回時刻を進めて予約し、保存する。
- 触るとき: スヌーズの期間や次回時刻の求め方を変えるとき。
- 呼び出し先: `Date.now()`, `gMonitors.get()`, `monitor.schedule.getNextRunTime()`, `monitor.scheduleNextRun()`, `next.getTime()`, `next.toISOString()`, `this._ensureLoaded()`, `this._saveAndNotify()`
- 参照: `monitor.lastRunTime`, `monitor.nextRunTime`

## muteMonitorNotifications()
- 位置: async L1152-1160
- 役割: 監視のデスクトップ通知を止める(notificationsMuted を true にして保存する)。
- 触るとき: 通知の無視ボタンの効果を変えるとき。
- 呼び出し先: `gMonitors.get()`, `this._ensureLoaded()`, `this._saveAndNotify()`
- 参照: `monitor.notificationsMuted`

## _unloadForTesting()
- 位置: L1162-1169
- 役割: テスト用に、監視の状態と通知の記録をすべて初期化する。
- 触るとき: テストごとに監視エージェントを初期状態へ戻すとき。
- 呼び出し先: `gNotifiedRunIds.clear()`, `gSnapshotRefreshPromises.clear()`, `this.uninit()`

## _waitForSnapshotForTesting()
- 位置: async L1177-1192
- 役割: テスト用に、進行中の初期スナップショット取得の完了を待つ。無ければ既存のスナップショットを返す。
- 触るとき: スナップショット取得の完了をテストで待つとき。
- 呼び出し先: `gMonitors.get()`, `gSnapshotRefreshPromises.get()`, `this._ensureLoaded()`
- 参照: `monitor.initialSnapshot`

## _resetForTesting()
- 位置: async L1194-1197
- 役割: テスト用に、監視の状態を初期化してからデータベースを削除する。
- 触るとき: テスト全体で監視の保存データをリセットするとき。
- 呼び出し先: `lazy.MonitorStore.destroyDatabase()`, `this._unloadForTesting()`
