# browser/components/aiwindow/ui/actors/SmartWindowTasksParent.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartWindowTasksParent.sys.mjs
source-hash: 2752b3bfb9c1c600f1b11dca988285454b300eec
lines: 138

## <module>
- 役割: Smart Window タスク UI からのモニター操作を MonitorAgent へ橋渡しする親アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `this.#handleCreateMonitor.bind()`, `this.#handleDeleteMonitor.bind()`, `this.#handleGetConstants.bind()`, `this.#handleListMonitors.bind()`, `this.#handleOpenUrl.bind()`, `this.#handlePauseMonitor.bind()`, `this.#handleRunMonitor.bind()`, `this.#handleUpdateMonitor.bind()`

## SmartWindowTasksParent.receiveMessage()
- 位置: async L34-43
- 役割: メッセージ名から対応ハンドラを引いて呼ぶ。未知の名前は警告を出して null を返す。
- 触るとき: モニター操作を新しく足すとき、このハンドラ表と子側の対応表を揃えて更新する。
- 呼び出し先: `handler()`, `this.#messageHandlers.get()`
- 条件付き依存: `if (!handler)` → `console.warn()`

## SmartWindowTasksParent.#handleListMonitors()
- 位置: async L45-60
- 役割: モニター一覧を取得し、各モニターの watchUrl にページタイトルを付けて返す。失敗時は error と code を返す。
- 触るとき: 一覧のタイトルが空になる、または一覧取得が失敗するときに見る。
- 呼び出し先: `Promise.all()`, `console.error()`, `lazy.MonitorAgent.listMonitors()`, `lazy.MonitorUIUtils.resolveWatchUrlTitles()`, `monitors.map()`
- 参照: `error.code`, `error.message`, `monitor.watchUrlTitles`, `monitor.watchUrls`

## SmartWindowTasksParent.#handleCreateMonitor()
- 位置: async L62-70
- 役割: MonitorAgent.createMonitor を呼び、作成したモニターを返す。失敗時は error と code を返す。
- 触るとき: モニター作成のエラーを UI に出す仕組みを変えるとき、または作成が失敗するときに見る。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.createMonitor()`
- 参照: `error.code`, `error.message`

## SmartWindowTasksParent.#handleDeleteMonitor()
- 位置: async L72-80
- 役割: 確認つきのモニター削除に委ねる。data.skipConfirmation が true なら確認を省く(テスト用の経路)。
- 触るとき: 削除の確認を変えるとき、または確認が出ずに消えたときに見る。UI 側の要求で skipConfirmation を立てると確認なしで消えるので注意する。
- 呼び出し先: `lazy.MonitorUIUtils.deleteMonitorWithConfirmation()`
- 参照: `data.id`, `data.skipConfirmation`, `this.browsingContext`

## SmartWindowTasksParent.#handleUpdateMonitor()
- 位置: async L82-93
- 役割: MonitorAgent.updateMonitor に id と updates を渡し、更新後のモニターを返す。失敗時は error と code を返す。
- 触るとき: モニターの設定変更が保存されないときに見る。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.updateMonitor()`
- 参照: `data.id`, `data.updates`, `error.code`, `error.message`

## SmartWindowTasksParent.#handleRunMonitor()
- 位置: async L95-103
- 役割: MonitorAgent.runNow で指定モニターを今すぐ実行し、結果を返す。
- 触るとき: 手動実行が反応しない、または実行結果の形を UI 側と合わせるときに見る。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.runNow()`
- 参照: `data.id`, `error.code`, `error.message`

## SmartWindowTasksParent.#handlePauseMonitor()
- 位置: async L105-113
- 役割: data.pause の値を使って pauseMonitor を呼び、一時停止と再開を切り替える。
- 触るとき: 一時停止や再開が効かないとき、または停止の仕組みを変えるときに見る。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.pauseMonitor()`
- 参照: `data.id`, `data.pause`, `error.code`, `error.message`

## SmartWindowTasksParent.#handleOpenUrl()
- 位置: L115-120
- 役割: モニターの監視 URL を、呼び出し元のトップ chrome ウィンドウで MonitorUIUtils.openMonitorUrl に開かせる。
- 触るとき: モニターのリンクが開かないとき、または開き方(タブかウィンドウか)を変えるときに見る。
- 呼び出し先: `lazy.MonitorUIUtils.openMonitorUrl()`
- 参照: `data?.url`, `this.browsingContext.topChromeWindow`

## SmartWindowTasksParent.#handleGetConstants()
- 位置: L122-136
- 役割: モニター数の上限、URL 数の上限、スケジュール種別、地域対応の有無、サポートページの URL をまとめて返す。
- 触るとき: UI が表示する上限値や対応地域の判定を変えるとき、またはサポート URL を差し替えるときに見る。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.MonitorUIUtils.isMonitorRegionSupported()`
- 参照: `lazy.SCHEDULE_TYPES`, `lazy.TOTAL_NUM_MONITORS`, `lazy.TOTAL_NUM_URLS_IN_MONITOR`
- XPCOM: `Services.urlFormatter`
