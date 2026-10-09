# browser/components/aiwindow/ui/modules/MonitorPanel.sys.mjs

source: browser/components/aiwindow/ui/modules/MonitorPanel.sys.mjs
source-hash: 8794ae8ba62364f658ecb57cab2c7a263804e8d4
lines: 435

## <module>
- 役割: スマートウィンドウのツールバーから開く「タスク」パネルを作り、監視（Monitor）の一覧表示・作成・開く操作を仲介する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## toggleMonitorPanel()
- 位置: L54-67
- 役割: パネルが開いていれば閉じ、閉じていれば開く。
- 触るとき: ツールバーのボタンを押したときの開閉の動きを変えるとき。
- 呼び出し先: `doc.getElementById()`, `this.showMonitorPanel()`
- 条件付き依存: `if (existing)` → `existing.hidePopup()`
- 参照: `win?.document`

## showCreateForm()
- 位置: L74-87
- 役割: パネルを作成フォームの画面で開く。既に開いていればその画面へ切り替える。
- 触るとき: 作成フォームを開く別の入口を追加・変更するとき。
- 呼び出し先: `doc.getElementById()`, `this.showMonitorPanel()`
- 条件付き依存: `if (existing)` → `this._openCreateView()`
- 参照: `win?.document`

## showMonitorPanel()
- 位置: L94-146
- 役割: 注意の印を消費してパネルを作り、ボタンの横に表示する。閉じられたら購読と ARIA 状態を後始末する。
- 触るとき: パネルの表示位置、表示時の購読や注意の印の扱いを変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `button.setAttribute()`, `doc.getElementById()`, `lazy.AIWindow.takeMonitorAttentionIds()`, `lazy.CustomizableUI.getWidget()`, `lazy.CustomizableUI.getWidget(BUTTON_ID)?.forWindow()`, `panel.addEventListener()`, `panel.openPopup()`, `panel.remove()`, `popupSet.appendChild()`, `this._createPanel()`, `this._syncContents()`
- 条件付き依存: `if (create)` → `this._openCreateView()`
- 参照: `lazy.CustomizableUI.getWidget(BUTTON_ID)?.forWindow(win)?.anchor`, `lazy.MONITOR_AGENTS_CHANGED_TOPIC`, `panel._contents.attentionIds`, `win.document`
- XPCOM: `Services.obs`

## onMonitorsChanged()
- 位置: L114-114
- 役割: 監視の変更通知を受けて、パネルの内容を読み直す。
- 触るとき: パネルが古い一覧のままになる、または更新が過剰に走る問題を調べるとき。
- 呼び出し先: `this._syncContents()`

## _createPanel()
- 位置: L152-200
- 役割: パネル、見出し、監視一覧の要素を組み立て、作成・キャンセル・送信などのイベントを結びつける。
- 触るとき: パネルの構成要素やイベントの割り当てを増やす・変えるとき。
- 呼び出し先: `contents.addEventListener()`, `doc.createElement()`, `doc.createXULElement()`, `header.appendChild()`, `heading.appendChild()`, `panel.append()`, `panel.hidePopup()`, `panel.setAttribute()`, `this._onCreateSubmit()`, `this._onOpenTask()`, `this._openCreateView()`, `this._setView()`, `win.switchToTabHavingURI()`
- 参照: `contents.draft`, `contents.maxMonitors`, `event.detail`, `event.detail.draft`, `event.detail.id`, `header.className`, `heading.id`, `lazy.TOTAL_NUM_MONITORS`, `panel._contents`, `panel._header`, `panel._title`, `panel.id`, `win.document`

## _onOpenTask()
- 位置: L221-240
- 役割: 監視の行を開いたとき、その監視が見ているページを名前付きのタブグループで開く。既にあればそのグループを選択する。
- 触るとき: 監視の行を押したときの動作を変えるとき。許可されていない URL は開かない。
- 呼び出し先: `(monitor?.watchUrls ?? []).filter()`, `panel._contents.monitors?.find()`, `panel.hidePopup()`, `this._existingTaskGroup()`, `this._groupTaskTabs()`, `this._openTaskTabs()`
- 参照: `existingGroup.collapsed`, `existingGroup.tabs`, `lazy.isAllowedWatchUrl`, `m.id`, `monitor.monitorName`, `monitor?.watchUrls`, `urls.length`, `win.gBrowser.selectedTab`

## _existingTaskGroup()
- 位置: L248-257
- 役割: 同じ監視のタブグループが、このウィンドウにまだあれば返す。
- 触るとき: 同じ監視のタブが二重にグループ化される問題を調べるとき。グループは ID で探す（名前は変わるため）。
- 呼び出し先: `this._taskTabGroupIds.get()`, `this._taskTabGroupIds.get(win)?.get()`, `win.gBrowser.tabGroups.find()`
- 参照: `group.id`

## _openTaskTabs()
- 位置: L267-282
- 役割: 監視のページごとにタブを開く。選択されるタブ以外は遅延読み込みにし、ヌルプリンシパルで開く。
- 触るとき: タブを開く方法（読み込みのタイミング、権限、コンテナ）を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `urls.map()`, `win.gBrowser.addTab()`
- XPCOM: `Services.scriptSecurityManager`

## _groupTaskTabs()
- 位置: L293-307
- 役割: 開いたタブを監視の名前のタブグループにまとめ、監視 ID とグループ ID の対応を記録する。
- 触るとき: タブグループの名前や対応の記録方法を変えるとき。
- 呼び出し先: `groupIds.set()`, `this._taskTabGroupIds.get()`, `this._taskTabGroupIds.set()`, `win.gBrowser.addTabGroup()`
- 参照: `group.id`, `lazy.TabMetrics.METRIC_SOURCE.SMART_WINDOW_TASKS`

## _watchableUrl()
- 位置: L314-317
- 役割: 現在のページが監視の対象にできる URL ならその URL を、そうでなければ空文字を返す。
- 触るとき: 作成フォームに初期値として入る URL の条件を変えるとき。
- 呼び出し先: `lazy.isAllowedWatchUrl()`
- 参照: `win.gBrowser?.currentURI?.spec`

## _openCreateView()
- 位置: L321-324
- 役割: 作成フォームの対象 URL を現在のページに合わせてから、作成画面に切り替える。
- 触るとき: 作成フォームを開いたときの初期値を変えるとき。
- 呼び出し先: `this._setView()`, `this._watchableUrl()`
- 参照: `panel._contents.agent`

## _setView()
- 位置: L334-361
- 役割: 見出しと内容を一覧か作成かの画面に揃えて切り替え、作成画面では戻るボタンを付ける。
- 触るとき: 画面の切り替えや戻るボタンの表示を変えるとき。戻るボタンは隠さず追加・削除する。
- 呼び出し先: `backButton.addEventListener()`, `backButton.setAttribute()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `lazy.gBundle.GetStringFromName()`, `panel._header.prepend()`, `panel._header.querySelector()`, `this._setView()`
- 条件付き依存: `if (view === "list")` → `existing?.remove()`
- 参照: `backButton.className`, `panel._contents.view`, `panel._title`, `panel.ownerDocument`

## _syncContents()
- 位置: async L366-385
- 役割: 監視を読み込み、最後に実行された時刻の新しい順に並べ、表示用の形にしてパネルへ渡す。
- 触るとき: 一覧の並び順や表示用の整形を変えるとき、または一覧が古いままになる問題を調べるとき。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.listMonitors()`, `lazy.MonitorUIUtils.formatMonitorForDisplay()`, `monitors .sort()`, `monitors .sort((a, b) => new Date(b.lastRunTime) - new Date(a.lastRunTime)) .map()`
- 参照: `a.lastRunTime`, `b.lastRunTime`, `panel._contents.monitors`, `panel.isConnected`

## _onCreateSubmit()
- 位置: async L391-413
- 役割: 作成フォームの内容で監視を作成し、一覧画面に戻して新しい監視を示す。
- 触るとき: 監視の作成処理や作成後の画面遷移を変えるとき。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.createMonitor()`, `this._setView()`, `this._toAgentSchedule()`
- 参照: `panel._contents.draft`, `panel._contents.justCreatedId`, `panel.isConnected`

## _toAgentSchedule()
- 位置: L422-433
- 役割: フォームの時刻と曜日の形式を、監視エージェントが保存する形式に変換する。
- 触るとき: スケジュールの保存形式や変換の規則を変えるとき。
- 呼び出し先: `Number()`, `schedule.time.split()`, `schedule.time.split(":").map()`
- 参照: `schedule.frequency`, `schedule.weekday`
