# browser/components/aiwindow/ui/modules/AIWindowTabStatesManager.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowTabStatesManager.sys.mjs
source-hash: 17b2cc833de8e2c3e39f19cb85bc0a97e7a7fd3f
lines: 1147

## <module>
- 役割: Smart Window のタブごとの状態(入力、会話 id、サイドバーの開閉)を管理し、全画面チャットとサイドバーの表示を揃える。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## hasInputContent()
- 位置: L76-78
- 役割: スマートバーの入力にテキストかメンションが1つでもあるかを返す。
- 触るとき: 入力が空かどうかで全画面からサイドバーへ移すかを決める条件を変えるとき。
- 呼び出し先: `Boolean()`
- 参照: `input?.mentions?.length`, `input?.text`

## AIWindowTabStatesManager.constructor()
- 位置: L107-109
- 役割: 渡されたウィンドウに対して #init を呼び、状態の管理を始める。
- 触るとき: ウィンドウごとの初期化の順序を変えるとき。
- 呼び出し先: `this.#init()`

## AIWindowTabStatesManager.getActiveConversation()
- 位置: L117-120
- 役割: 選択中のタブの会話を返す。状態がなければ null を返す。
- 触るとき: 選択中タブの会話を別の機能が参照する箇所を調べるとき。
- 呼び出し先: `this.#tabStates.get()`
- 参照: `this.#tabStates.get(tab)?.state?.conversation`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.getTabConversationId()
- 位置: L131-140
- 役割: タブの会話 id を返す。メッセージが0件の新規会話は null とし、未読込の復元会話は id を返す。
- 触るとき: 空の新規チャットを会話として扱うかを変えるとき、復元直後のタブの扱いを調べるとき。
- 呼び出し先: `this.#tabStates.get()`
- 参照: `state.conversation`, `state.conversation.messageCount`, `state.conversationId`, `state?.conversationId`, `this.#tabStates.get(tab)?.state`

## AIWindowTabStatesManager.getConversationTab()
- 位置: L149-158
- 役割: 指定した会話 id を持つタブを、ウィンドウのタブ一覧から探して返す。
- 触るとき: 既に開いている会話のタブへ切り替える処理を変えるとき。
- 呼び出し先: `tabs.find()`, `this.#tabStates.get()`
- 参照: `tabState.state.conversationId`, `this.#window.gBrowser.tabs`

## AIWindowTabStatesManager.openSidebarForReturningUser()
- 位置: async L165-190
- 役割: 復元完了を待ってから、選択中タブの設定に従いサイドバーを開く。既に開いていれば何もしない。
- 触るとき: 起動後にサイドバーを自動で開く条件を変えるとき。
- 呼び出し先: `getKeepSidebarOpenState()`, `lazy.AIWindowUI.isSidebarOpen()`, `this.#getTabState()`
- 条件付き依存: `if ( getKeepSidebarOpenState( this.#getTabState(tab)?.state, lazy.sidebarOpenByDefault ) )` → `lazy.AIWindowUI.openSidebar()`
- 参照: `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser.currentURI.spec`, `tabState?.state?.keepSidebarOpen`, `this.#getTabState(tab)?.state`, `this.#restorePromise`, `this.#window`, `this.#window.gBrowser.selectedTab`

## AIWindowTabStatesManager.#init()
- 位置: L199-215
- 役割: タブ用と ai-window 用のイベントリスナーを登録し、既存タブの状態と復元処理を準備する。
- 触るとき: タブ状態の管理がいつ始まるか、どのイベントを購読しているかを調べるとき。
- 呼び出し先: `tabContainer.addEventListener()`, `this.#addWindowEventListeners()`, `this.#getTabsListener()`, `this.#restoreInitialTabSidebar()`, `this.#setUpInitialTabs()`, `this.#window.gBrowser.addProgressListener()`
- 参照: `this.#restorePromise`, `this.#tabStates`, `this.#tabsListener`, `this.#window`, `this.#window.gBrowser.tabContainer`

## AIWindowTabStatesManager.uninit()
- 位置: L220-232
- 役割: 登録したリスナーをすべて外し、状態とウィンドウへの参照を破棄する。
- 触るとき: ウィンドウを閉じたときの後始末に漏れがないか確認するとき。
- 呼び出し先: `tabContainer.removeEventListener()`, `this.#removeWindowEventListeners()`, `this.#window.gBrowser.removeProgressListener()`
- 参照: `this.#tabStates`, `this.#tabsListener`, `this.#window`, `this.#window.gBrowser.tabContainer`

## AIWindowTabStatesManager.#addWindowEventListeners()
- 位置: L237-287
- 役割: ai-window:* の9種類のイベントをウィンドウに登録する。
- 触るとき: 新しい ai-window イベントを購読させるとき、対応するハンドラーを探すとき。
- 呼び出し先: `this.#window.addEventListener()`
- 参照: `this.#onAIWindowConnected`, `this.#onCloseSidebar`, `this.#onContextChipsChanged`, `this.#onConversationChanged`, `this.#onConversationCleared`, `this.#onConversationOpened`, `this.#onModelChanged`, `this.#onSidebarNavigating`, `this.#onSidebarToggle`, `this.#onSmartbarInput`

## AIWindowTabStatesManager.#removeWindowEventListeners()
- 位置: L292-337
- 役割: #addWindowEventListeners で登録したイベントを同じ組で外す。
- 触るとき: イベントの登録を増減させたとき、解除側も揃っているか確かめるとき。
- 呼び出し先: `this.#window.removeEventListener()`
- 参照: `this.#onAIWindowConnected`, `this.#onCloseSidebar`, `this.#onConversationChanged`, `this.#onConversationCleared`, `this.#onConversationOpened`, `this.#onModelChanged`, `this.#onSidebarNavigating`, `this.#onSidebarToggle`, `this.#onSmartbarInput`

## AIWindowTabStatesManager.#setUpInitialTabs()
- 位置: L345-353
- 役割: ウィンドウ作成時に既にあるタブのうち、状態が未登録のものへ空の状態を登録する。
- 触るとき: 起動直後の最初のタブの状態が抜ける不具合を調べるとき。
- 呼び出し先: `this.#addTabState()`, `this.#tabStates.has()`, `this.#window.gBrowser.tabs.forEach()`

## AIWindowTabStatesManager.handleEvent()
- 位置: L362-380
- 役割: タブコンテナーの TabOpen、TabSelect、TabClose、SSTabRestoring を、対応するハンドラーへ振り分ける。
- 触るとき: タブ関連のイベントの処理先を変えるとき、どの動きがどのイベントで起きるかを確かめるとき。
- 呼び出し先: `this.#onTabClose()`, `this.#onTabOpen()`, `this.#onTabRestoring()`, `this.#onTabSelect()`
- 参照: `event.type`

## AIWindowTabStatesManager.#onTabOpen()
- 位置: L390-393
- 役割: 新しいタブに空の状態を登録し、tabsOpened 計測を1加算する。
- 触るとき: タブを開いたときの計測や初期状態を変えるとき。
- 呼び出し先: `Glean.smartWindow.tabsOpened.add()`, `this.#addTabState()`
- 参照: `event.target`

## AIWindowTabStatesManager.#onTabSelect()
- 位置: async L413-464
- 役割: タブ選択時に、保存された会話や sidebar の状態に応じてサイドバーを開くか閉じる。復元中のタブは SSTabRestoring の処理に任せる。
- 触るとき: タブを切り替えたときサイドバーが勝手に開閉する、または空の会話が増える不具合を調べるとき。
- 呼び出し先: `getKeepSidebarOpenState()`, `this.#getTabState()`, `this.#openSidebarForTab()`
- 条件付き依存: `if (tabUrl === lazy.AIWINDOW_URL)` → `lazy.AIWindowUI.restoreMemoriesState()`
- 条件付き依存: `if (tabUrl === lazy.AIWINDOW_URL)` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `Promise.resolve()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `tab.hasAttribute()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `lazy.SessionStore.isTabRestoring()`
- 条件付き依存: `if (!tabState?.state?.conversationId)` → `this.#getTabState()`
- 条件付き依存: `if (!shouldKeepSidebar)` → `lazy.AIWindowUI.updateSidebarInput()`
- 条件付き依存: `if (!shouldKeepSidebar)` → `lazy.AIWindowUI.closeSidebar()`
- 参照: `event.target`, `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser?.currentURI?.spec`, `tabState?.state`, `tabState?.state?.conversationId`, `this.#window`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.#onTabRestoring()
- 位置: async L476-503
- 役割: SessionStore が復元したタブの会話 id を状態に読み込み、そのタブが選択中で条件を満たすならサイドバーを開く。
- 触るとき: アプリ再起動後や復元時に会話がサイドバーに出ない不具合を調べるとき。
- 呼び出し先: `getKeepSidebarOpenState()`, `this.#openSidebarForTab()`, `this.#refreshTabStateFromSession()`
- 参照: `event.target`, `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser?.currentURI?.spec`, `tabState.state`, `tabState.state?.conversationId`, `this.#window`, `this.#window.gBrowser.selectedTab`

## AIWindowTabStatesManager.#openSidebarForTab()
- 位置: async L514-533
- 役割: 会話を解決してサイドバーを開き、入力とコンテキストを反映し、タブのモデル選択を適用する。
- 触るとき: サイドバーを開いた直後に表示される会話、入力、モデルの組み合わせを変えるとき。
- 呼び出し先: `lazy.AIWindowUI.openSidebar()`, `lazy.AIWindowUI.updateSidebarModel()`, `this.#resolveTabModelChoice()`, `this.#updateSidebarState()`
- 条件付き依存: `if (tabState?.state?.conversationId && !conversation)` → `this.#computeConversation()`
- 参照: `tabState.state?.conversation`, `tabState?.state?.conversationId`, `this.#window`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.#refreshTabStateFromSession()
- 位置: L546-565
- 役割: SessionStore から保存済みの状態を読み、会話 id があれば状態へ上書きマージする。
- 触るとき: 保存された会話 id をタブ状態に取り込むタイミングを変えるとき。
- 呼び出し先: `JSON.parse()`, `lazy.SessionStore.getCustomTabValue()`, `this.#tabStates.get()`
- 条件付き依存: `if (saved?.conversationId)` → `this.#tabStates.set()`
- 参照: `saved?.conversationId`, `tabState.state`, `this.#tabStates`

## AIWindowTabStatesManager.setTabStateConversation()
- 位置: L575-583
- 役割: タブに開いた会話と会話 id を状態として設定する。会話か タブ がなければ何もしない。
- 触るとき: 会話をタブに紐づけて開く経路を変えるとき。
- 呼び出し先: `this.#getTabState()`
- 参照: `conversation.id`

## AIWindowTabStatesManager.#resolveTabModelChoice()
- 位置: L591-594
- 役割: タブの状態に保存された modelChoiceId を返し、なければ null を返す。
- 触るとき: タブごとのモデル選択の既定値を変えるとき。
- 参照: `tabState.state?.modelChoiceId`

## AIWindowTabStatesManager.#computeConversation()
- 位置: async L606-622
- 役割: 状態に会話があればそれを返す。会話 id だけなら ChatStore から会話を読み、状態へ書き戻す。
- 触るとき: 復元された会話を DB から読み込むタイミングや、読み込み失敗時の扱いを変えるとき。
- 呼び出し先: `lazy.ChatStore.findConversationById()`
- 条件付き依存: `if (found)` → `this.#getTabState()`
- 参照: `tabState?.state?.conversation`, `tabState?.state?.conversationId`

## AIWindowTabStatesManager.#onTabClose()
- 位置: L632-634
- 役割: 閉じられたタブの状態を削除する。
- 触るとき: タブを閉じた後に状態が残る不具合を調べるとき。
- 呼び出し先: `this.#removeEventListeners()`
- 参照: `event.target`

## AIWindowTabStatesManager.#addTabState()
- 位置: L643-645
- 役割: タブに状態が未読込であることを示す空の状態(state が null)を登録する。
- 触るとき: タブ状態の初期値を変えるとき。
- 呼び出し先: `this.#tabStates.set()`

## AIWindowTabStatesManager.#removeEventListeners()
- 位置: L654-656
- 役割: タブの状態を WeakMap から削除する。名前に反して登録解除はしない。
- 触るとき: タブを閉じたときの状態の後始末を変えるとき。
- 呼び出し先: `this.#tabStates.delete()`

## AIWindowTabStatesManager.#onAIWindowConnected()
- 位置: async L665-719
- 役割: ai-window の接続時に、全画面の会話をサイドバーへ移す条件を満たせば入力を反映し、サイドバーの接続時は入力とモデルを同期する。
- 触るとき: 全画面からサイドバーへ会話を移す挙動や、接続直後の入力の反映を変えるとき。
- 呼び出し先: `hasInputContent()`, `lazy.ChatStore.findConversationById()`, `this.#getTabState()`
- 条件付き依存: `if (!tabState.state?.conversationId)` → `this.#getTabState()`
- 条件付き依存: `if (needsSidebar)` → `lazy.AIWindowUI.updateSidebarInput()`
- 条件付き依存: `if (mode === "sidebar" && selectedTab === tab)` → `this.#updateSidebarState()`
- 条件付き依存: `if (mode === "sidebar" && selectedTab === tab)` → `lazy.AIWindowUI.updateSidebarModel()`
- 条件付き依存: `if (mode === "sidebar" && selectedTab === tab)` → `this.#resolveTabModelChoice()`
- 参照: `conversation.messages.length`, `event.detail`, `lazy.AIWINDOW_URL`, `stateUpdate.mode`, `tabState.state`, `tabState.state.input`, `tabState.state?.conversationId`, `this.#window`, `this.#window?.gBrowser.selectedTab`

## AIWindowTabStatesManager.#updateSidebarState()
- 位置: L721-731
- 役割: サイドバーに、タブの入力内容とコンテキストチップを反映する。
- 触るとき: サイドバーに出る入力やチップの値の元を追うとき。
- 呼び出し先: `lazy.AIWindowUI.updateSidebarContextChips()`, `lazy.AIWindowUI.updateSidebarInput()`
- 参照: `tabState?.state?.contextChips`, `tabState?.state?.input`, `tabState?.state?.removedImplicitContextChip`, `this.#window`

## AIWindowTabStatesManager.#restoreInitialTabSidebar()
- 位置: async L739-779
- 役割: 起動時に SessionStore の全ウィンドウ復元を待ち、選択中タブに保存された会話があればサイドバーを開く。
- 触るとき: 起動直後にサイドバーが開く条件や、復元完了を待つ順序を変えるとき。
- 呼び出し先: `JSON.parse()`, `getKeepSidebarOpenState()`, `lazy.AIWindowUI.openSidebar()`, `lazy.ChatStore.findConversationById()`, `lazy.SessionStore.getCustomTabValue()`, `this.#getTabState()`
- 参照: `lazy.AIWINDOW_URL`, `lazy.SessionStore.promiseAllWindowsRestored`, `lazy.sidebarOpenByDefault`, `tab.linkedBrowser?.currentURI?.spec`, `this.#window`, `this.#window.gBrowser.selectedTab`

## AIWindowTabStatesManager.#getTabState()
- 位置: L792-852
- 役割: タブの状態を返す。引数があれば状態をマージし、会話 id と keepSidebarOpen を SessionStore へ保存または削除する。
- 触るとき: タブの状態に項目を足すとき、SessionStore に何を保存するかを変えるとき。
- 呼び出し先: `this.#tabStates.get()`
- 条件付き依存: `if (tabState.state === null)` → `lazy.SessionStore.getCustomTabValue()`
- 条件付き依存: `if (tabState.state === null)` → `JSON.parse()`
- 条件付き依存: `if (tabState.state === null)` → `this.#tabStates.set()`
- 条件付き依存: `if (newState)` → `this.#tabStates.set()`
- 条件付き依存: `if (conversationId && keepSidebarOpen !== false)` → `lazy.SessionStore.setCustomTabValue()`
- 条件付き依存: `if (conversationId && keepSidebarOpen !== false)` → `JSON.stringify()`
- 条件付き依存: `if (!(conversationId && keepSidebarOpen !== false))` → `lazy.SessionStore.deleteCustomTabValue()`
- 参照: `newState.tab`, `oldState.input`, `oldState.mode`, `tabState.state`, `tabState.state.input`, `tabState.state.mode`, `this.#tabStates`

## AIWindowTabStatesManager.#onSmartbarInput()
- 位置: L860-862
- 役割: スマートバーの入力イベントを受け、その内容をタブの状態へ保存する。
- 触るとき: 入力内容がタブ切り替え後も残る仕組みを追うとき。
- 呼び出し先: `this.#getTabState()`
- 参照: `event.detail`, `event.detail.tab`

## AIWindowTabStatesManager.#onConversationOpened()
- 位置: L870-885
- 役割: 会話が開かれたイベントを受け、タブの会話と会話 id を状態へ保存する。全画面モードの時だけ mode も保存する。
- 触るとき: 会話を開いたときにタブ状態へ何を書くかを変えるとき。
- 呼び出し先: `this.#getTabState()`
- 参照: `event.detail`, `stateUpdate.mode`

## AIWindowTabStatesManager.#onConversationCleared()
- 位置: L893-907
- 役割: 会話がクリアされたとき、既存の状態を保ったまま新しい空の会話 id と会話で置き換える。
- 触るとき: チャットをクリアした後にタブを切り替えて戻ったとき、同じ会話が再利用される仕組みを変えるとき。
- 呼び出し先: `this.#getTabState()`
- 条件付き依存: `if (currentTabState?.state)` → `this.#getTabState()`
- 参照: `currentTabState.state`, `currentTabState?.state`, `event.detail`

## AIWindowTabStatesManager.#onConversationChanged()
- 位置: L919-940
- 役割: 会話が切り替わったイベントを受け、タブの状態を更新する。会話が空なら、URL が前回と違う場合に開始プロンプトを読み込む。
- 触るとき: 空のチャットに出る開始プロンプトの再読込条件を変えるとき。
- 呼び出し先: `lazy.AIWindowUI.updateStarterPrompts()`
- 条件付き依存: `if (tab && conversation)` → `this.#getTabState()`
- 参照: `conversation.id`, `conversation.messageCount`, `conversation.transientStarterUrl`, `event.detail`, `tab.linkedBrowser.currentURI.spec`, `this.#window`

## AIWindowTabStatesManager.#onModelChanged()
- 位置: L948-956
- 役割: スマートバーでモデルが選ばれたとき、そのモデルの id をタブの状態へ保存する。
- 触るとき: タブごとのモデル選択が保存されない不具合を調べるとき。
- 呼び出し先: `this.#getTabState()`
- 参照: `currentTabState.state`, `currentTabState?.state`, `event.detail`

## AIWindowTabStatesManager.#onContextChipsChanged()
- 位置: L964-975
- 役割: コンテキストチップの変更を受け、チップの一覧と暗黙チップの削除状態をタブの状態へ保存する。
- 触るとき: チップの追加や削除がタブを切り替えたあとに残るかを確かめるとき。
- 呼び出し先: `this.#getTabState()`
- 参照: `currentTabState?.state`, `event.detail`

## AIWindowTabStatesManager.#onSidebarToggle()
- 位置: L983-1010
- 役割: サイドバーの開閉を受け、ユーザー操作なら keepSidebarOpen を更新する。開けば会話を渡して開き、閉じれば空クローズ回数を更新する。
- 触るとき: サイドバーを開いたまま保つ判定や、空のまま閉じた回数の集計を変えるとき。
- 呼び出し先: `this.#getTabState()`
- 条件付き依存: `if (currentTabState?.state && source === "toggle")` → `this.#getTabState()`
- 条件付き依存: `if (source === "toggle")` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if (isOpen)` → `this.#updateSidebarState()`
- 条件付き依存: `if (!(isOpen))` → `this.#updateEmptyCloseCount()`
- 参照: `currentTabState.state`, `currentTabState?.state`, `currentTabState?.state?.conversation`, `event.detail`, `this.#window`

## AIWindowTabStatesManager.#updateEmptyCloseCount()
- 位置: L1023-1045
- 役割: サイドバーを閉じたとき、会話がなければ空クローズ回数を1増やして2で止め、会話があれば0に戻す。
- 触るとき: 「閉じたままにするか」の案内を出す条件や回数を変えるとき。
- 呼び出し先: `Services.prefs.setIntPref()`, `["close", "toggle"].includes()`
- 条件付き依存: `if (lazy.sidebarEmptyCloseCount !== 0)` → `Services.prefs.setIntPref()`
- 参照: `conversation?.messageCount`, `lazy.sidebarEmptyCloseCount`
- XPCOM: `Services.prefs`

## AIWindowTabStatesManager.#onSidebarNavigating()
- 位置: L1054-1061
- 役割: サイドバーのスマートバーでの移動や検索を受け、そのタブに保存された入力を空にする。
- 触るとき: 移動後にスマートバーの入力が残る、または消えない不具合を調べるとき。
- 呼び出し先: `this.#getTabState()`
- 参照: `event.detail.tab`

## AIWindowTabStatesManager.#onCloseSidebar()
- 位置: L1063-1065
- 役割: ai-window:close-sidebar を受け、AIWindowUI.closeSidebar をトグル扱いで呼ぶ。
- 触るとき: 外部からサイドバーを閉じる経路を追うとき。
- 呼び出し先: `lazy.AIWindowUI.closeSidebar()`
- 参照: `this.#window`

## AIWindowTabStatesManager.#getTabsListener()
- 位置: L1070-1145
- 役割: 進捗リスナーを作って返す。ページ遷移は onLocationChange で処理し、他の通知は何もしない。
- 触るとき: 進捗リスナーに新しい通知の処理を足すとき。
- 呼び出し先: `ChromeUtils.generateQI()`

## onLocationChange()
- 位置: async L1077-1137
- 役割: 選択中タブでの URL 変化を受け、全画面とサイドバーの間で開閉を切り替え、サイドバーの入力を反映する。タブ切り替えによる通知は無視する。
- 触るとき: URL の変化でサイドバーが開閉する条件、特に全画面チャットからの移動を変えるとき。
- 呼び出し先: `getKeepSidebarOpenState()`, `lazy.AIWindowUI.isSidebarOpen()`, `lazy.AIWindowUI.updateStarterPrompts()`, `this.#tabStates.get()`
- 条件付き依存: `if (!isAiWindowUrl)` → `lazy.SmartWindowTelemetry.recordUriLoad()`
- 条件付き依存: `if (isFullPageMode && isAiWindowUrl && isSidebarOpen)` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if ( isFullPageMode && !isAiWindowUrl && !isSidebarOpen && shouldKeepSidebarOpen )` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if ( isFullPageMode && !isAiWindowUrl && !isSidebarOpen && shouldKeepSidebarOpen )` → `this.#getTabState()`
- 条件付き依存: `if (!isAiWindowUrl && lazy.AIWindowUI.isSidebarOpen(this.#window))` → `lazy.AIWindowUI.updateSidebarInput()`
- 参照: `lazy.AIWINDOW_URL`, `lazy.sidebarOpenByDefault`, `locationURI.spec`, `tabState.state`, `tabState.state.conversation`, `tabState.state.input`, `tabState.state.mode`, `tabState.state?.conversationId`, `this.#tabStates`, `this.#window`, `this.#window.gBrowser.selectedTab`, `webProgress.isTopLevel`

## AIWindowTabStatesManager.onStateChange()
- 位置: L1139-1139
- 役割: 進捗リスナーの状態変化通知。処理は何もしない。
- 触るとき: 状態変化の通知を使う処理を足すとき。

## AIWindowTabStatesManager.onProgressChange()
- 位置: L1140-1140
- 役割: 進捗リスナーの進捗通知。処理は何もしない。
- 触るとき: 読み込みの進捗に応じた処理を足すとき。

## AIWindowTabStatesManager.onStatusChange()
- 位置: L1141-1141
- 役割: 進捗リスナーのステータス通知。処理は何もしない。
- 触るとき: ステータス表示に応じた処理を足すとき。

## AIWindowTabStatesManager.onSecurityChange()
- 位置: L1142-1142
- 役割: 進捗リスナーのセキュリティ状態の通知。処理は何もしない。
- 触るとき: セキュリティ表示に応じた処理を足すとき。

## AIWindowTabStatesManager.onContentBlockingEvent()
- 位置: L1143-1143
- 役割: 進捗リスナーのコンテンツブロックの通知。処理は何もしない。
- 触るとき: コンテンツブロックの表示に応じた処理を足すとき。
