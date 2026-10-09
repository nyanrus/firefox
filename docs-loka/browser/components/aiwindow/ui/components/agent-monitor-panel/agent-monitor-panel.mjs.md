# browser/components/aiwindow/ui/components/agent-monitor-panel/agent-monitor-panel.mjs

source: browser/components/aiwindow/ui/components/agent-monitor-panel/agent-monitor-panel.mjs
source-hash: eebca5f3fe1356a9c87b21240d3cdea18e66ff2e
lines: 304

## <module>
- 役割: AI Window のタスクパネルの中身。モニターの一覧と作成フォームの2画面を切り替えて描画し、操作は親へイベントで渡す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## AgentMonitorPanel.constructor()
- 位置: L67-76
- 役割: プロパティの初期値を設定し、表示は一覧(list)にする。
- 触るとき: パネルを開いたときの初期表示を変えるとき、または初期値の前提を変えるときに見る。
- 呼び出し先: `super()`
- 参照: `this.agent`, `this.attentionIds`, `this.draft`, `this.justCreatedId`, `this.maxMonitors`, `this.monitors`, `this.view`

## AgentMonitorPanel.updated()
- 位置: L78-98
- 役割: 作成画面に切り替わったら作成フォームへフォーカスを移す。画面の遷移の向きに応じて、一覧か作成フォームに slide-in のクラスを付ける。
- 触るとき: 画面遷移の動きが出ないとき、または戻ったときの動きを変えるときに見る。changed.get("view") は変更前の値なので、向きの判定をそれで読むこと。
- 呼び出し先: `changed.get()`, `changed.has()`, `super.updated()`
- 条件付き依存: `if (changed.has("view") && this.view === "create")` → `this.#focusCreateForm()`
- 条件付き依存: `if ( changed.has("view") && changed.get("view") === "create" && !changed.has("justCreatedId") )` → `this.shadowRoot .querySelector(".monitor-list-view") ?.classList.add()`
- 条件付き依存: `if ( changed.has("view") && changed.get("view") === "create" && !changed.has("justCreatedId") )` → `this.shadowRoot .querySelector()`
- 条件付き依存: `if (changed.has("view") && changed.get("view") === "list")` → `this.shadowRoot .querySelector("agent-monitor-item") ?.classList.add()`
- 条件付き依存: `if (changed.has("view") && changed.get("view") === "list")` → `this.shadowRoot .querySelector()`
- 参照: `this.view`

## AgentMonitorPanel.#focusCreateForm()
- 位置: async L100-107
- 役割: 作成フォームの更新を待ってから名前欄にフォーカスする。待つ間に画面が一覧へ戻っていれば何もしない。
- 触るとき: 作成画面を開いたときに名前欄へフォーカスが行かないときに見る。
- 呼び出し先: `this.shadowRoot.querySelector()`
- 条件付き依存: `if (this.view === "create")` → `form?.focusName()`
- 参照: `form?.updateComplete`, `this.view`

## AgentMonitorPanel.#dispatch()
- 位置: L109-113
- 役割: bubbles と composed を付けた CustomEvent を発火する。
- 触るとき: パネルのイベント名や detail の形を変えるときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AgentMonitorPanel.#lastRun()
- 位置: L119-121
- 役割: モニターの履歴の先頭、つまり最新の項目を返す。履歴が無ければ null を返す。
- 触るとき: 行の結果表示が最新の実行と合わないときに見る。
- 参照: `monitor.history`, `monitor.history?.length`

## AgentMonitorPanel.#renderSchedule()
- 位置: L123-133
- 役割: スケジュールの文言 ID と引数を取り、行のメタ情報として描画する。取れなければ nothing を返す。
- 触るとき: 行に出る頻度の表示が合わないときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `lazy.MonitorUIUtils.getScheduleL10n()`
- 参照: `monitor.schedule`, `schedule.args`, `schedule.id`

## AgentMonitorPanel.#renderResult()
- 位置: L135-158
- 役割: 最新の実行結果を行の右に描画する。実行中や未実行は何も出さない。エラーは確認できなかった扱い、条件一致は一致(新着なら点を付ける)、それ以外は不一致とする。
- 触るとき: 行の結果表示や新着の印を変えるときに見る。
- 呼び出し先: `html()`, `this.#lastRun()`
- 条件付き依存: `if (lastRun.status === "error")` → `html()`
- 条件付き依存: `if (lastRun.conditionMet)` → `html()`
- 参照: `lastRun.conditionMet`, `lastRun.status`

## AgentMonitorPanel.#onRowClick()
- 位置: L160-167
- 役割: 監視ページが無い監視は何もしない。ページがあれば open-task イベントを id つきで送る。
- 触るとき: 行をクリックしても開かないとき、または開ける条件を変えるときに見る。
- 呼び出し先: `this.#dispatch()`
- 参照: `monitor.id`, `monitor.watchUrls?.length`

## AgentMonitorPanel.#renderRow()
- 位置: L169-188
- 役割: 状態チップ、名前、スケジュール、結果を含む行のボタンを描画する。ページの無い行は aria-disabled にし、直前に作られた行には data-just-created を付ける。
- 触るとき: 一覧の行の見た目や操作を変えるときに見る。
- 呼び出し先: `html()`, `this.#onRowClick()`, `this.#renderResult()`, `this.#renderSchedule()`
- 参照: `monitor.id`, `monitor.monitorName`, `monitor.status?.kind`, `monitor.watchUrls?.length`, `this.justCreatedId`

## AgentMonitorPanel.#renderSection()
- 位置: L190-200
- 役割: 見出しつきで行を並べる。行が無ければ何も描画しない。
- 触るとき: 新着と監視中の区切りの表示を変えるときに見る。
- 呼び出し先: `html()`, `monitors.map()`, `this.#renderRow()`
- 参照: `monitors.length`

## AgentMonitorPanel.#renderList()
- 位置: L202-239
- 役割: 新着を先に、残りを監視中として並べ、合わせて最大5行にする。監視が1件も無ければ空の案内を出す。最後にフッターを描画する。
- 触るとき: 一覧の件数や並び、空のときの表示を変えるときに見る。
- 呼び出し先: `attention.has()`, `html()`, `this.#renderFooter()`, `this.#renderSection()`, `this.monitors .filter()`, `this.monitors .filter(monitor => !attention.has(monitor.id)) .slice()`, `this.monitors .filter(monitor => attention.has(monitor.id)) .slice()`
- 参照: `monitor.id`, `newMatches.length`, `this.attentionIds`, `this.monitors.length`

## AgentMonitorPanel.#renderFooter()
- 位置: L241-283
- 役割: 有効な監視の数を数え、上限に達していれば作成ボタンを無効にする。作成と管理へのボタンを描画する。
- 触るとき: 監視数の表示や作成の可否を変えるときに見る。一時停止中の監視は数えない。
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#dispatch()`, `this.monitors.filter()`
- 参照: `monitor.enabled`, `this.maxMonitors`, `this.monitors.filter(monitor => monitor.enabled).length`

## AgentMonitorPanel.render()
- 位置: L285-300
- 役割: 作成画面なら agent と draft を渡した agent-monitor-item を、そうでなければ一覧を描画する。作成フォームはパネルの見出しを使うので selfContained を false にする。
- 触るとき: パネル全体の画面の切り替えや、作成フォームに渡す値を変えるときに見る。
- 呼び出し先: `html()`, `this.#renderList()`
- 参照: `this.agent`, `this.draft`, `this.view`
