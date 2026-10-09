# browser/components/aiwindow/ui/components/ai-tasks/ai-tasks.mjs

source: browser/components/aiwindow/ui/components/ai-tasks/ai-tasks.mjs
source-hash: b2e8dc06bc38511836c2759d4f643d16956f7c78
lines: 556

## <module>
- 役割: AI Window のタスク画面で、監視(モニター)の一覧表示と作成・編集・削除を行う ai-tasks を定義する。
- 呼び出し先: `customElements.define()`

## AITasks.constructor()
- 位置: L72-78
- 役割: 定数を既定値で用意し、monitors を空配列、dialogOpen を false にする。
- 触るとき: 起動直後の既定の上限値や表示を変えたいとき。
- 呼び出し先: `super()`
- 参照: `this._constants`, `this.dialogOpen`, `this.monitors`

## AITasks.connectedCallback()
- 位置: async L82-127
- 役割: アクターの初期化と監視一覧の読み込みを非同期で始め、6 種類の agent-monitor-item イベントとリンクのイベントを購読する。
- 触るとき: イベントが届かない、または要素を付けた直後に一覧が出ない不具合を調べるとき。
- 呼び出し先: `console.warn()`, `super.connectedCallback()`, `this.#initializeActor()`, `this.#initializeActor().catch()`, `this.addEventListener()`, `this.handleMonitorCancel.bind()`, `this.handleMonitorCheckNow.bind()`, `this.handleMonitorDelete.bind()`, `this.handleMonitorOpen.bind()`, `this.handleMonitorPause.bind()`, `this.handleMonitorSubmit.bind()`, `this.loadMonitors()`, `this.loadMonitors().catch()`
- 参照: `this.boundHandleMonitorCancel`, `this.boundHandleMonitorCheckNow`, `this.boundHandleMonitorDelete`, `this.boundHandleMonitorOpen`, `this.boundHandleMonitorPause`, `this.boundHandleMonitorSubmit`

## AITasks.#initializeActor()
- 位置: async L134-150
- 役割: RequestConstants でアクターから定数を取り、成功したら凍結して保存し、再描画を要求する。失敗はコンソールに出すだけ。
- 触るとき: 上限数や地域対応の値がアクター側の値と食い違うとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success && result.constants)` → `Object.freeze()`
- 条件付き依存: `if (result?.success && result.constants)` → `this.requestUpdate()`
- 参照: `MONITOR_ACTIONS.REQUEST_CONSTANTS`, `result.constants`, `result?.success`, `this._constants`

## AITasks.#dispatchMonitorAction()
- 位置: L162-192
- 役割: SmartWindowTasks:<action> イベントを発火し、応答か失敗の一回限りの待ち受けを張って、その結果で Promise を解決または拒否する。
- 触るとき: アクターへの要求が返ってこない、またはエラーの扱いを変えるとき。新しいアクションを足すときも通る。
- 呼び出し先: `this.addEventListener()`, `this.dispatchEvent()`

## handleResponse()
- 位置: L167-171
- 役割: 応答を受けたら、エラー側の待ち受けを外してから結果の detail で解決する。
- 触るとき: 応答後にリスナーが残るなど、待ち受けの後始末を調べるとき。
- 呼び出し先: `resolve()`, `this.removeEventListener()`
- 参照: `event.detail`

## handleError()
- 位置: L173-177
- 役割: エラーを受けたら応答側の待ち受けを外し、detail の error かの既定文言で拒否する。
- 触るとき: アクターのエラー文言が画面に出ない、または拒否の扱いを変えるとき。
- 呼び出し先: `reject()`, `this.removeEventListener()`
- 参照: `event.detail?.error`

## AITasks.disconnectedCallback()
- 位置: L194-222
- 役割: connectedCallback で登録した 6 種類のイベントの待ち受けを外す。
- 触るとき: 要素を外した後もイベントに反応し続ける不具合を調べるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this.boundHandleMonitorCancel`, `this.boundHandleMonitorCheckNow`, `this.boundHandleMonitorDelete`, `this.boundHandleMonitorOpen`, `this.boundHandleMonitorPause`, `this.boundHandleMonitorSubmit`

## AITasks.isMaxMonitorsReached()
- 位置: L232-235
- 役割: enabled な監視の数が上限 TOTAL_NUM_MONITORS 以上かを返す。一時停止中の監視は数えない。
- 触るとき: 監視の上限判定や、作成ボタン・再開可否の条件を変えるとき。
- 呼び出し先: `this.monitors.filter()`
- 参照: `monitor.enabled`, `this._constants.TOTAL_NUM_MONITORS`, `this.monitors.filter(monitor => monitor.enabled).length`

## AITasks.isMonitorRegionSupported()
- 位置: L242-244
- 役割: アクターから受けた isMonitorRegionSupported の値を返す。
- 触るとき: 地域で監視が使えないときの表示を調べるとき。
- 参照: `this._constants.isMonitorRegionSupported`

## AITasks.#dialog()
- 位置: L246-248
- 役割: シャドウルート内の dialog 要素を取得する。
- 触るとき: 作成ダイアログの開閉処理が効かないときに参照先を確かめるとき。
- 呼び出し先: `this.shadowRoot.querySelector()`

## AITasks.openDialog()
- 位置: L252-257
- 役割: dialogOpen を true にして、作成用カードを描画させたうえで dialog を modal で開く。
- 触るとき: 作成ダイアログが開くタイミングや、開くたびに空の状態になる仕組みを変えるとき。
- 呼び出し先: `this.#dialog?.showModal()`
- 参照: `this.dialogOpen`

## AITasks.closeDialog()
- 位置: L259-262
- 役割: dialogOpen を false にして、dialog を閉じる。
- 触るとき: 作成後やキャンセル後にダイアログが閉じない不具合を調べるとき。
- 呼び出し先: `this.#dialog?.close()`
- 参照: `this.dialogOpen`

## AITasks.handleMonitorDelete()
- 位置: async L271-288
- 役割: 削除要求を送り、成功かつ削除済みの時だけ一覧を再読み込みする。キャンセル時は何もしない。
- 触るとき: 削除後に一覧が更新されない、またはキャンセルの扱いを変えるとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success && result?.deleted)` → `this.loadMonitors()`
- 条件付き依存: `if (!result?.success)` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_DELETE_MONITOR`, `event.detail`, `result?.deleted`, `result?.error`, `result?.success`

## AITasks.handleMonitorPause()
- 位置: async L295-310
- 役割: detail の paused を pause として一時停止・再開を要求し、成功したら一覧を再読み込みする。
- 触るとき: 一時停止や再開の結果が一覧に反映されないとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success)` → `this.loadMonitors()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_PAUSE_MONITOR`, `event.detail`, `result?.error`, `result?.success`

## AITasks.handleMonitorCheckNow()
- 位置: async L317-333
- 役割: RequestRunMonitor で監視を今すぐ実行させ、成功したら一覧を再読み込みする。
- 触るとき: 今すぐ確認ボタンの後の表示更新を調べるとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (result?.success)` → `this.loadMonitors()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_RUN_MONITOR`, `event.detail`, `result?.error`, `result?.success`

## AITasks.handleMonitorOpen()
- 位置: async L340-355
- 役割: イベントの伝播を止め、監視のページ URL を RequestOpenUrl で開かせる。失敗はコンソールに出す。
- 触るとき: 監視に付いたページのリンクが開かない、または伝播の扱いを変えるとき。
- 呼び出し先: `console.error()`, `event.stopPropagation()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (!result?.success)` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_OPEN_URL`, `event.detail`, `result?.error`, `result?.success`

## AITasks.handleMonitorSubmit()
- 位置: L364-369
- 役割: detail の mode が create なら createMonitor、それ以外なら updateMonitor に振り分ける。
- 触るとき: 作成ダイアログと既存カードの編集で送信処理を分けたいとき、または振り分けの条件を変えるとき。
- 呼び出し先: `this.updateMonitor()`
- 条件付き依存: `if (event.detail?.mode === "create")` → `this.createMonitor()`
- 参照: `event.detail`, `event.detail?.mode`

## AITasks.handleMonitorCancel()
- 位置: L374-376
- 役割: 作成用カードがキャンセルされたら、作成ダイアログを閉じる。
- 触るとき: キャンセル後のダイアログの状態を変えるとき。
- 呼び出し先: `this.closeDialog()`

## AITasks.createMonitor()
- 位置: async L383-408
- 役割: カードの値を RequestCreateMonitor に渡して作成する。source は about_page。成功したらダイアログを閉じて一覧を再読み込みする。
- 触るとき: 作成時に送るパラメータや、作成後の遷移を変えるとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`, `this.#toMonitorSchedule()`, `this.closeDialog()`, `this.loadMonitors()`
- 条件付き依存: `if (!result?.success)` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_CREATE_MONITOR`, `result?.error`, `result?.success`

## AITasks.updateMonitor()
- 位置: async L415-438
- 役割: 既存カードの編集内容を title、monitorPrompt、watchUrls、schedule にまとめて RequestUpdateMonitor で送り、成功したら一覧を再読み込みする。
- 触るとき: 編集で保存される項目を増やす、または保存結果が反映されないとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`, `this.#toMonitorSchedule()`
- 条件付き依存: `if (result?.success)` → `this.loadMonitors()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_UPDATE_MONITOR`, `result?.error`, `result?.success`

## AITasks.#toMonitorSchedule()
- 位置: L447-467
- 役割: frequency が daily か weekly で時刻があるときだけ、type、hour、minute(weekly は weekday も)を持つ予定に変換する。それ以外は null。
- 触るとき: 保存される予定の形式を変えるとき、または予定が保存されない原因を調べるとき。
- 呼び出し先: `Number()`, `[ this._constants.SCHEDULE_TYPES.DAILY, this._constants.SCHEDULE_TYPES.WEEKLY, ].includes()`, `schedule.time.split()`, `schedule.time.split(":").map()`
- 参照: `schedule.frequency`, `schedule.time`, `schedule.weekday`, `schedule?.frequency`, `this._constants.SCHEDULE_TYPES.DAILY`, `this._constants.SCHEDULE_TYPES.WEEKLY`

## AITasks.loadMonitors()
- 位置: async L473-486
- 役割: RequestListMonitors で監視一覧を取得し、成功時のみ monitors に入れる。
- 触るとき: 一覧が古いまま、または空で出る原因を調べるとき。
- 呼び出し先: `console.error()`, `this.#dispatchMonitorAction()`
- 条件付き依存: `if (!(result?.success))` → `console.error()`
- 参照: `MONITOR_ACTIONS.REQUEST_LIST_MONITORS`, `result.monitors`, `result?.error`, `result?.success`, `this.monitors`

## AITasks.render()
- 位置: L488-552
- 役割: 作成ダイアログ(開いている時だけ作成カード)、地域非対応時の案内、またはヘッダーの追加ボタンと監視一覧を描画する。
- 触るとき: 追加ボタンの無効条件や、地域非対応時の表示を変えるとき。
- 呼び出し先: `html()`, `this.openDialog()`
- 参照: `this._constants.SCHEDULE_TYPES`, `this._constants.TOTAL_NUM_URLS_IN_MONITOR`, `this._constants.smartWindowSupportUrl`, `this.dialogOpen`, `this.isMaxMonitorsReached`, `this.isMonitorRegionSupported`, `this.monitors`
