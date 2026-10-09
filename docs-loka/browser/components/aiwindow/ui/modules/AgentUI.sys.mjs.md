# browser/components/aiwindow/ui/modules/AgentUI.sys.mjs

source: browser/components/aiwindow/ui/modules/AgentUI.sys.mjs
source-hash: 3ab6da408bdc72aa96fc75e82fcffbfdbc49b724
lines: 785

## <module>
- 役割: チャット内のエージェントカード(現在は監視カード)の操作を受け、監視の作成、編集、削除、確認などを MonitorAgent に仲介する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `console.createInstance()`, `this.#handleCancelMonitor.bind()`, `this.#handleCheckMonitor.bind()`, `this.#handleDeleteMonitor.bind()`, `this.#handleMonitorCommand.bind()`, `this.#handlePauseMonitor.bind()`, `this.#handleSaveMonitorDraft.bind()`, `this.#handleUpdateMonitor.bind()`, `this.handleCreateMonitor.bind()`

## AgentUI.handleUpdate()
- 位置: async L105-125
- 役割: カードからの更新を、メッセージの toolCallId が一致するときだけ updateType に対応するハンドラーへ振り分ける。
- 触るとき: カードのボタンを押しても反応しない、または未知の updateType の扱いを変えるとき。
- 呼び出し先: `conversation?.messages?.find()`, `handler()`
- 条件付き依存: `if (typeof handler !== "function")` → `lazy.console.error()`
- 参照: `m.id`, `message?.toolUIData?.toolCallId`, `this.#UPDATE_TYPE_HANDLERS`

## AgentUI.#handleMonitorCommand()
- 位置: async L162-216
- 役割: /watch で現在のページを監視できれば監視カードを会話に追加する。監視できないページは案内を出す。全画面では空のカードを出す。上限に達していれば上限の案内を出す。
- 触るとき: /watch で出るカードの条件、全画面時の扱い、上限の判定を変えるとき。
- 呼び出し先: `conversation.addAssistantMessage()`, `conversation.addUIToolToCurrentMessage()`, `crypto.randomUUID()`, `lazy.MonitorAgent.listMonitors()`, `lazy.isAllowedWatchUrl()`, `lazy.l10n.formatValueSync()`, `monitors.filter()`
- 条件付き依存: `if (raw)` → `conversation.addUserMessage()`
- 条件付き依存: `if (raw)` → `conversation.emit()`
- 条件付き依存: `if (!isFullPage)` → `conversation.addAssistantWithL10nMessage()`
- 条件付き依存: `if (activeCount >= lazy.TOTAL_NUM_MONITORS)` → `conversation.addAssistantWithL10nMessage()`
- 参照: `AGENT_UI_TYPES.MONITOR_ITEM`, `lazy.TOTAL_NUM_MONITORS`, `monitor.enabled`, `monitors.filter(monitor => monitor.enabled).length`

## AgentUI.handleCreateMonitor()
- 位置: async L225-299
- 役割: カードの入力から監視を作成し、カードを表示状態に差し替える。自動確認が指定されていれば、直後に一度チェックを走らせる。
- 触るとき: 監視の作成内容や作成後のカードの表示、初回チェックの条件を変えるとき。
- 呼び出し先: `conversation.emit()`, `lazy.MonitorAgent.createMonitor()`, `lazy.MonitorUIUtils.resolveWatchUrlTitles()`, `lazy.console.error()`, `lazy.l10n.formatValueSync()`, `this.#buildMonitorArgs()`, `this.#formatScheduleSummary()`, `this.#setMessageL10n()`, `this.#statusForKind()`
- 条件付き依存: `if (!args.prompt || !args.watchUrls.length)` → `lazy.console.warn()`
- 条件付き依存: `if (updateData?.autoExpandAndCheck)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (updateData?.autoExpandAndCheck)` → `lazy.MonitorAgent.runNow()`
- 条件付き依存: `if (updateData?.autoExpandAndCheck)` → `lazy.console.error()`
- 参照: `args.pageTitle`, `args.prompt`, `args.watchUrls`, `args.watchUrls.length`, `message.toolUIData`, `message.toolUIDraft`, `message?.toolUIData?.properties?.agent`, `updateData?.autoExpandAndCheck`, `updateData?.schedule`
- XPCOM: `Services.tm`

## AgentUI.#handleCancelMonitor()
- 位置: async L308-314
- 役割: 作成カードの下書きを消し、キャンセルの案内文に差し替える。監視は作らない。
- 触るとき: 作成をキャンセルしたときの会話の表示や後処理を変えるとき。
- 呼び出し先: `conversation.updateToolUI()`, `this.#setMessageL10n()`
- 参照: `message.toolUIDraft`

## AgentUI.#handleSaveMonitorDraft()
- 位置: L323-326
- 役割: カードの入力途中の内容をメッセージの下書きに保存し、カードを作り直しても残るようにする。
- 触るとき: カードの入力内容が消える不具合を調べるとき、下書きに保存する項目を増やすとき。
- 参照: `message.toolUIDraft`, `updateData?.draft`

## AgentUI.#handleUpdateMonitor()
- 位置: async L334-375
- 役割: 表示カードの編集内容を既存の監視に保存し、表示状態に戻す。タイトルや URL が空なら既存の値を残す。
- 触るとき: 監視の編集で保存される項目を増やすとき、編集後にカードの値が古いままになる不具合を調べるとき。
- 呼び出し先: `conversation.emit()`, `lazy.MonitorAgent.updateMonitor()`, `lazy.MonitorUIUtils.resolveWatchUrlTitles()`, `lazy.console.error()`, `this.#buildSchedule()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 参照: `agent.monitorName`, `agent.url`, `message.toolUIData`, `message.toolUIDraft`, `message?.toolUIData?.properties?.agent`, `updateData.condition`, `updateData.monitorName`, `updateData.schedule`, `updateData.watchUrls`, `updateData?.id`

## AgentUI.#handleDeleteMonitor()
- 位置: async L383-430
- 役割: 確認ダイアログを経て既存の監視を削除する。確定したらカードを外し、キャンセルならカードは残す。
- 触るとき: 監視の削除の流れや、削除後に出す案内を変えるとき。
- 呼び出し先: `conversation.updateToolUI()`, `lazy.MonitorUIUtils.deleteMonitorWithConfirmation()`, `lazy.l10n.formatValueSync()`, `this.#setMessageL10n()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 条件付き依存: `if (!browsingContext)` → `lazy.console.warn()`
- 条件付き依存: `if (!result.success)` → `lazy.console.error()`
- 参照: `agent.monitorName`, `message?.toolUIData?.properties?.agent`, `result.cancelled`, `result.error`, `result.success`, `updateData?.id`, `window?.gBrowser?.selectedBrowser?.browsingContext`

## AgentUI.#handlePauseMonitor()
- 位置: async L439-466
- 役割: 監視の有効と無効を切り替え、カードの状態表示を一時停止または監視中に変える。
- 触るとき: 一時停止の扱いや、一時停止中のカードの表示を変えるとき。
- 呼び出し先: `conversation.emit()`, `lazy.MonitorAgent.updateMonitor()`, `lazy.console.error()`, `this.#statusForKind()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 参照: `message.toolUIData`, `message.toolUIData.properties`, `message?.toolUIData?.properties?.agent`, `updateData?.id`, `updateData?.paused`

## AgentUI.#handleCheckMonitor()
- 位置: async L475-494
- 役割: 既存の監視を今すぐ一度実行し、その後に会話内のカードの履歴を監視の内容に合わせて更新する。
- 触るとき: 今すぐ確認の挙動や、確認後に履歴が反映されない不具合を調べるとき。
- 呼び出し先: `lazy.MonitorAgent.runNow()`, `lazy.console.error()`, `this.#loadMonitorsById()`, `this.#syncConversationHistory()`
- 条件付き依存: `if (!id)` → `lazy.console.warn()`
- 参照: `updateData?.id`

## AgentUI.observeMonitorChanges()
- 位置: L502-523
- 役割: 会話を監視対象に加える。共通の observer がなければ登録し、すぐに全会話の履歴を同期する。
- 触るとき: 監視カードを表示する会話を開いたときの同期の流れを変えるとき。
- 呼び出し先: `lazy.console.error()`, `this.#observedConversations.add()`, `this.#syncAllMonitorHistories()`, `this.#syncAllMonitorHistories().catch()`
- 条件付き依存: `if (!this.#monitorObserver)` → `Services.obs.addObserver()`
- 参照: `lazy.MONITOR_AGENTS_CHANGED_TOPIC`, `this.#monitorObserver`
- XPCOM: `Services.obs`

## this.#monitorObserver()
- 位置: L509-513
- 役割: MONITOR_AGENTS_CHANGED_TOPIC の通知を受けて、全会話の監視カードの履歴を同期する関数。
- 触るとき: 監視の変更通知を受けてもカードが更新されない不具合を調べるとき。
- 呼び出し先: `lazy.console.error()`, `this.#syncAllMonitorHistories()`, `this.#syncAllMonitorHistories().catch()`

## AgentUI.unobserveMonitorChanges()
- 位置: L530-543
- 役割: 会話を監視対象から外す。監視対象が無くなったら共通の observer を外して解除する。
- 触るとき: 会話を閉じたときに通知の購読が残らないかを確かめるとき。
- 呼び出し先: `this.#observedConversations.delete()`
- 条件付き依存: `if (!this.#observedConversations.size && this.#monitorObserver)` → `Services.obs.removeObserver()`
- 参照: `lazy.MONITOR_AGENTS_CHANGED_TOPIC`, `this.#monitorObserver`, `this.#observedConversations.size`
- XPCOM: `Services.obs`

## AgentUI.#loadMonitorsById()
- 位置: async L551-554
- 役割: 全監視を読み込み、id をキーにした Map を返す。
- 触るとき: 監視の一覧の取得方法や照合の仕方を変えるとき。
- 呼び出し先: `lazy.MonitorAgent.listMonitors()`, `monitors.map()`
- 参照: `monitor.id`

## AgentUI.#syncAllMonitorHistories()
- 位置: async L556-564
- 役割: 監視対象の会話が1つでもあれば監視の一覧を読み、対象の全会話のカードの履歴を同期する。
- 触るとき: 通知を受けたときに同期する会話の範囲を変えるとき。
- 呼び出し先: `this.#loadMonitorsById()`, `this.#syncConversationHistory()`
- 参照: `this.#observedConversations`, `this.#observedConversations.size`

## AgentUI.#syncConversationHistory()
- 位置: L574-603
- 役割: 会話内の監視カードごとに、監視の成功と失敗の履歴を新しい順で入れ替え、内容が変わったときだけ更新を通知する。
- 触るとき: カードの履歴に出す項目(成功と失敗の絞り込み、並び順)を変えるとき。
- 呼び出し先: `(monitor.history ?? []) .filter()`, `(monitor.history ?? []) .filter(entry => entry.status === "success" || entry.status === "error") .reverse()`, `JSON.stringify()`, `byId.get()`, `conversation.emit()`
- 参照: `AGENT_UI_TYPES.MONITOR_ITEM`, `agent.history`, `agent?.id`, `conversation?.messages`, `entry.status`, `message.toolUIData`, `message.toolUIData.properties`, `message.toolUIData.properties?.agent`, `message?.toolUIData?.uiType`, `monitor.history`

## AgentUI.#setMessageL10n()
- 位置: L614-619
- 役割: メッセージの本文を空にし、Fluent の id、引数、リンクを設定して表示する文言を差し替える。
- 触るとき: 差し替え文言の表示方法やリンクの扱いを変えるとき。
- 参照: `message.content.body`, `message.content.l10nArgs`, `message.content.l10nId`, `message.content.link`

## AgentUI.#statusForKind()
- 位置: L628-635
- 役割: 監視中か一時停止かを表す状態表示用のラベル付きオブジェクトを作る。
- 触るとき: カードの状態表示の文言や種類を変えるとき。
- 呼び出し先: `lazy.l10n.formatValueSync()`

## AgentUI.#buildMonitorArgs()
- 位置: L646-659
- 役割: カードの送信内容と元のページ情報から createMonitor の引数を作る。URL は送信内容、なければ元の指定を使う。
- 触るとき: 監視の作成引数(条件、URL、名前、予定)の決め方を変えるとき。
- 呼び出し先: `this.#buildSchedule()`
- 参照: `agent.condition`, `agent.monitorName`, `agent.pageTitle`, `agent.url`, `agent.watchUrls`, `updateData.watchUrls`, `updateData?.condition`, `updateData?.monitorName`, `updateData?.schedule`, `updateData?.watchUrls?.length`

## AgentUI.#buildSchedule()
- 位置: L669-681
- 役割: 頻度が daily なら日次、weekly なら週次の予定を作り、それ以外は既定の間隔(60分)の予定を作る。
- 触るとき: 監視の実行間隔や予定の種類を増やすとき、既定値を変えるとき。
- 呼び出し先: `Number()`, `String()`, `String(schedule?.time ?? "") .split()`, `String(schedule?.time ?? "") .split(":") .map()`
- 参照: `lazy.DailySchedule`, `lazy.IntervalSchedule`, `lazy.WeeklySchedule`, `schedule.weekday`, `schedule?.frequency`, `schedule?.time`

## AgentUI.#formatScheduleSummary()
- 位置: L692-715
- 役割: 予定の時刻から、毎日または毎週の時刻を表す表示文字列を作る。時刻が不正なら空文字を返す。
- 触るとき: カードに出る予定の文言や、週の曜日の計算を変えるとき。
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
- 役割: モニター機能が使えるときだけ、スラッシュコマンドを解析して対応するハンドラーへ渡し、処理したかを返す。パレットからの指定を優先する。
- 触るとき: スマートバーのコマンドが動かない原因を調べるとき、コマンドの優先順位を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `handler()`, `lazy.MonitorUIUtils.isMonitorRegionSupported()`, `parseAgentCommand()`, `value.trim()`
- 参照: `parsed?.prompt`, `parsedCommand.command`, `this.#COMMAND_HANDLERS`
- XPCOM: `Services.prefs`

## AgentUI.isAgentUpdate()
- 位置: L781-783
- 役割: updateType に対応するハンドラーがあるかを返す。
- 触るとき: カードの更新をエージェントに渡すか、別の処理に回すかの判定を変えるとき。
- 参照: `data?.updateType`, `this.#UPDATE_TYPE_HANDLERS`
