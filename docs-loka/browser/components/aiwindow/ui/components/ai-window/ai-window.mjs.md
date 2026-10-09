# browser/components/aiwindow/ui/components/ai-window/ai-window.mjs

source: browser/components/aiwindow/ui/components/ai-window/ai-window.mjs
source-hash: db6ce5328c6e057ead9af9765357fda40a03e7a9
lines: 3958

## <module>
- 役割: AI Window（スマートウィンドウ）の画面全体を担う ai-window 要素を定義する
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `console.createInstance()`, `customElements.define()`

## formatResumeTabGroupLabel()
- 位置: L212-216
- 役割: 見出し先頭の英語の Pick up 接頭辞を取り除き、先頭を大文字にする
- 触るとき: 再開カードのタブグループ名の表示を変えるとき。英語の暫定処理（Bug 2066263 の前提）なので、見出しのローカライズを入れる際に見直す。
- 呼び出し先: `headline.replace()`, `headline.replace(RESUME_HEADLINE_PREFIX_RE, "").trim()`, `headline.trim()`, `stripped.charAt()`, `stripped.charAt(0).toUpperCase()`, `stripped.slice()`

## getErrorCode()
- 位置: L230-236
- 役割: エラーのコードを取り出し、無ければ HTTP 406 を 7 (fastlyBlocked) とみなす
- 触るとき: モデル応答エラーのコード判定を変えるとき、Fastly に弾かれたときの扱いを確かめるとき。
- 参照: `error.error`, `error.metadata?.errorMessage`, `error.status`

## resolveModelResponseError()
- 位置: L238-251
- 役割: エラーを telemetry 用の名前と HTTP ステータスに変換する
- 触るとき: エラーのテレメトリ名の決め方を変えるとき、新しいエラー種別を足すとき。clientReason、コード表、HTTP ステータス、error.name の順に見る。
- 呼び出し先: `getErrorCode()`
- 参照: `error.clientReason`, `error.name`, `error.status`

## AIWindow.#kitMention()
- 位置: L306-308
- 役割: shadow root 内の kit-mention 要素を返す
- 触るとき: fullpage で Kit を表示する位置や呼び出しを調べるとき。
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIWindow.#memoriesIconShown()
- 位置: L310-316
- 役割: 記憶の設定が有効か既存の記憶があれば true を返す
- 触るとき: 記憶アイコンを出すかどうかの条件を変えるとき。
- 参照: `this.#hasMemories`, `this.memoriesConversationPref`, `this.memoriesHistoryPref`

## AIWindow.#resumeActivityEnabled()
- 位置: L320-326
- 役割: Nimbus の再開アクティビティ変数を読み、無ければ true を返す
- 触るとき: 再開カード機能を Nimbus で無効化する挙動を確かめるとき。(要確認) コメントは pref へのフォールバックと書くが、実装は true に落ちる。
- 呼び出し先: `lazy.NimbusFeatures[NIMBUS_FEATURE_SMART_WINDOW].getVariable()`
- 参照: `lazy.NimbusFeatures`

## AIWindow.#resumeActivityMemoriesEnabled()
- 位置: L329-335
- 役割: 記憶を使う設定が有効で既存の記憶もあるときだけ true を返す
- 触るとき: 再開カードの読み込み表示を記憶の有無で出し分けるとき。
- 参照: `this.#hasMemories`, `this.#memoriesToggled`, `this.memoriesConversationPref`, `this.memoriesHistoryPref`

## AIWindow.#hostBrowser()
- 位置: L359-361
- 役割: このウィンドウを埋め込む browser 要素を返す
- 触るとき: サイドバーとフルページのどちらで動いているか、ホスト側の属性を読む箇所を調べるとき。
- 参照: `window.browsingContext?.embedderElement`

## AIWindow.#detectModeFromContext()
- 位置: L363-367
- 役割: ホストの id が ai-window-browser なら sidebar、それ以外は fullpage を返す
- 触るとき: モード判定の基準を変えるとき。
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `this.#hostBrowser?.id`

## AIWindow.#syncHistoryState()
- 位置: L376-387
- 役割: fullpage のとき、現在の会話 ID を history state に replaceState で書く
- 触るとき: 戻る操作やセッション復元で会話を再開する仕組みを変えるとき。sidebar では何もしない。
- 呼び出し先: `window.history.replaceState()`
- 参照: `MODE.FULLPAGE`, `this.#conversation?.id`, `this.isConnected`, `this.mode`, `window.history.state`

## AIWindow.#getPendingConversationId()
- 位置: L395-402
- 役割: ホストの data-conversation-id、無ければ history state から会話 ID を取る
- 触るとき: 復元する会話 ID の取得元を増やすとき、取得の優先順位を変えるとき。
- 呼び出し先: `this.#hostBrowser?.getAttribute()`
- 参照: `window.history.state?.conversationId`

## AIWindow.#getBrowserContainer()
- 位置: L410-412
- 役割: shadow root の #browser-container を返す
- 触るとき: aichat browser を差し込む先を変えるとき。
- 呼び出し先: `this.renderRoot.querySelector()`

## AIWindow.syncSmartbarMemoriesStateFromConversation()
- 位置: async L414-423
- 役割: 会話に保存された記憶トグルを反映し、記憶ボタンを同期する
- 触るとき: 会話を切り替えたあとに記憶ボタンの押下状態がずれるとき。
- 呼び出し先: `this.#syncMemoriesButtonUI()`
- 参照: `this.#conversation.memoriesToggled`, `this.#conversation?.memoriesToggled`, `this.#memoriesToggled`, `this.#smartbar`

## AIWindow.focusSmartbar()
- 位置: async L425-432
- 役割: スマートバーの準備を待ち、フォーカスできたら true を返す
- 触るとき: 起動直後や新規チャットでスマートバーにフォーカスを移す箇所を調べるとき。
- 呼び出し先: `this.#smartbar.focus()`
- 参照: `this.#smartbar`, `this.#smartbarReadyPromise`

## AIWindow.#refreshHasMemories()
- 位置: async L434-442
- 役割: 保存済みの記憶が 1 件以上あるかを取り、失敗時は false にする
- 触るとき: 記憶の有無の判定方法や、取得失敗時の扱いを変えるとき。
- 呼び出し先: `lazy.MemoriesManager.getAllMemories()`, `lazy.log.error()`
- 参照: `memories?.length`, `this.#hasMemories`

## AIWindow.#syncMemoriesButtonUI()
- 位置: async L444-457
- 役割: 記憶の設定が両方オフなら存在を確認し、ボタンの表示と押下状態を更新する
- 触るとき: 記憶ボタンの表示条件や pressed 状態の決め方を変えるとき。
- 条件付き依存: `if (!this.memoriesConversationPref && !this.memoriesHistoryPref)` → `this.#refreshHasMemories()`
- 参照: `this.#memoriesButton`, `this.#memoriesButton.pressed`, `this.#memoriesButton.show`, `this.#memoriesIconShown`, `this.#memoriesToggled`, `this.memoriesConversationPref`, `this.memoriesHistoryPref`

## AIWindow.#recordChatInteraction()
- 位置: L465-477
- 役割: 会話の送信回数の pref を上限まで 1 増やす
- 触るとき: 利用回数の集計条件を変えるとき。上限は MAX_INTERACTION_COUNT。
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (interactionCount < MAX_INTERACTION_COUNT)` → `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## AIWindow.constructor()
- 位置: L479-562
- 役割: 各 pref の遅延ゲッターを張り、表示状態と会話オブジェクトを初期化する
- 触るとき: 起動時の既定値や pref 監視の対象を追加・変更するとき。data-conversation-id があれば chat-active を付ける。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.ResumeActivity.isSectionHiddenForSession()`, `lazy.getCurrentModelChoiceId()`, `super()`, `this.#detectModeFromContext()`, `this.#hostBrowser?.getAttribute()`, `this.#onMistralReleasePrefChanged()`, `this.#setModelChoice()`, `this.#syncMemoriesButtonUI()`, `this.#syncTopSites()`, `this.requestUpdate()`
- 条件付き依存: `if (this.#hostBrowser?.getAttribute("data-conversation-id"))` → `this.classList.add()`
- 参照: `MODE.FULLPAGE`, `lazy.ChatConversation`, `this.#browser`, `this.#conversation`, `this.#resolveSmartbarReady`, `this.#smartbar`, `this.#smartbarReadyPromise`, `this.isGenerating`, `this.mistralReleasePref`, `this.mode`, `this.promoMessage`, `this.recentChats`, `this.resumeCards`, `this.resumeCardsEmptyReason`, `this.resumeCardsLoading`, `this.resumeSectionHidden`, `this.showDisclaimer`, `this.showFooter`, `this.showStarters`, `this.startersResolved`, `this.topSites`, `this.userPrompt`

## AIWindow.#topChromeWindow()
- 位置: L564-566
- 役割: browsingContext の topChromeWindow を返す
- 触るとき: タブが移った先の親ウィンドウを参照する箇所を変えるとき。
- 参照: `window.browsingContext?.topChromeWindow`

## AIWindow.#attachConversationListeners()
- 位置: L568-586
- 役割: 会話の 3 イベントを購読し、エージェントのモニター監視を始める
- 触るとき: 会話イベントの購読先を追加・変更するとき。
- 呼び出し先: `lazy.AgentUI.observeMonitorChanges()`, `this.#conversation.on()`
- 参照: `this.#conversation`, `this.#onMessageComplete`, `this.#onMessageUpdate`, `this.#onSeenUrlsUpdated`

## AIWindow.#removeConversationListeners()
- 位置: L588-606
- 役割: 同じ 3 イベントの購読を解除し、モニター監視も止める
- 触るとき: 会話を差し替えるときの後始末を変えるとき。
- 呼び出し先: `lazy.AgentUI.unobserveMonitorChanges()`, `this.#conversation.off()`
- 参照: `this.#conversation`, `this.#onMessageComplete`, `this.#onMessageUpdate`, `this.#onSeenUrlsUpdated`

## AIWindow.#onSeenUrlsUpdated()
- 位置: L608-613
- 役割: 見た URL の更新を受け、content actor に seen URLs を送る
- 触るとき: 見た URL の同期経路を変えるとき。
- 呼び出し先: `this.#getAIChatContentActor()`
- 条件付き依存: `if (actor)` → `this.#dispatchSeenUrls()`

## AIWindow.#onMessageUpdate()
- 位置: L615-637
- 役割: fullpage なら chrome 側で Kit を表示し、ツール UI の計測を送ってから content に渡す
- 触るとき: メッセージ更新時の Kit 表示やツール UI の計測を変えるとき。kit トークンは content に渡さない。
- 呼び出し先: `this.#dispatchMessageToChatContent()`
- 条件付き依存: `if (this.mode === MODE.FULLPAGE && message.kit)` → `this.#kitMention?.trigger()`
- 条件付き依存: `if (message.toolUIData)` → `lazy.ToolUI.handleUIDisplayTelemetry()`
- 参照: `MODE.FULLPAGE`, `message.convId`, `message.kit`, `message.toolUIData`, `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.onMemoriesApplied()
- 位置: L639-645
- 役割: 記憶の適用を Glean の memoryApplied で記録する
- 触るとき: 記憶適用のテレメトリを変えるとき。
- 呼び出し先: `Glean.smartWindow.memoryApplied.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#getDataConvId()
- 位置: L652-658
- 役割: 会話オブジェクトの ID を返し、無ければ data-conversation-id を返す
- 触るとき: 会話 ID の取得元の優先順位を変えるとき。
- 呼び出し先: `this.#hostBrowser?.getAttribute()`
- 参照: `this.#conversation`, `this.#conversation.id`

## AIWindow.connectedCallback()
- 位置: L660-731
- 役割: モード属性とモデル一覧を設定し、イベント・pref・トップサイトの監視を張る
- 触るとき: ウィンドウ接続時に張る購読を追加・削除するとき。unload で remove される。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `installClientErrorListeners()`, `lazy.SmartWindowTelemetry.recordClientError()`, `super.connectedCallback()`, `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#loadAvailableModels()`, `this.#loadPendingConversation()`, `this.#registerSwapDocShellsListener()`, `this.#setupWindowModeObserver()`, `this.documentGlobal.addEventListener()`, `this.getClientErrorContext()`, `this.ownerDocument.addEventListener()`, `this.remove()`, `this.setAttribute()`
- 参照: `this.#handleModelChange`, `this.#handleOpenModelSettings`, `this.#handleSmartbarCommit`, `this.#handleStopGeneration`, `this.#onCustomEndpointPrefChanged`, `this.#onHistoryMenuEvent`, `this.#onModelChoicePrefChanged`, `this.#onPanelShowing`, `this.#removeClientErrorListeners`, `this.#topSitesObserver`, `this.documentGlobal`, `this.mode`, `window.browsingContext?.topChromeWindow`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#topSitesObserver()
- 位置: L700-700
- 役割: AboutNewTab のトップサイト変更通知で、トップサイト欄を再同期する
- 触るとき: トップサイトが初回起動時に出ないなど、ストア読み込みの遅れを扱うとき。
- 呼び出し先: `this.#syncTopSites()`

## AIWindow.conversationId()
- 位置: L733-735
- 役割: 会話の ID を返す
- 触るとき: 会話 ID を外から参照するコードを追うとき。
- 参照: `this.#conversation?.id`

## AIWindow.conversationMessageCount()
- 位置: L737-739
- 役割: 会話のメッセージ数を返す
- 触るとき: メッセージ数を計測や表示に使うとき。会話が null なら例外になる。
- 参照: `this.#conversation.messageCount`

## AIWindow.conversation()
- 位置: L746-748
- 役割: 現在の会話オブジェクトを返す
- 触るとき: 外部から会話の中身を読むとき。
- 参照: `this.#conversation`

## AIWindow.#registerSwapDocShellsListener()
- 位置: L750-767
- 役割: chrome window の EndSwapDocShells 購読を付け替える
- 触るとき: タブをウィンドウ間で移動したときに追跡する先を変えるとき。
- 呼び出し先: `this.#swapDocShellsChromeWindow?.addEventListener()`, `this.#swapDocShellsChromeWindow?.removeEventListener()`
- 参照: `this.#handleEndSwapDocShells`, `this.#swapDocShellsChromeWindow`

## AIWindow.handleEvent()
- 位置: L769-775
- 役割: OpenConversation なら会話を開き、会話が空なら新規チャットを作る
- 触るとき: OpenConversation の受け口や、既定の動作を変えるとき。
- 条件付き依存: `if (event.detail)` → `this.openConversation()`
- 条件付き依存: `if (!this.#conversation?.messages?.length)` → `this.onCreateNewChatClick()`
- 参照: `event.detail`, `this.#conversation?.messages?.length`

## AIWindow.#handleEndSwapDocShells()
- 位置: L781-816
- 役割: タブ移動後の状態で、クラシックの新規タブへ戻すか aichat browser を作り直すかを分ける
- 触るとき: タブのドラッグで別ウィンドウへ移したときの表示や会話の復元を直すとき。
- 呼び出し先: `lazy.AIWindow.hasActiveChatInBrowser()`, `lazy.AIWindow.isAIWindowActive()`, `this.#registerSwapDocShellsListener()`, `this.#updateSmartbarAndHeaderVisibility()`
- 条件付き依存: `if (!hasActiveChat)` → `Services.io.newURI()`
- 条件付き依存: `if (!hasActiveChat)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (!hasActiveChat)` → `browser.loadURI()`
- 条件付き依存: `if (!(!hasActiveChat))` → `this.#recreateAIChatBrowser()`
- 条件付き依存: `if (hasActiveChat)` → `this.#recreateAIChatBrowser()`
- 参照: `this.#conversation`, `this.#pendingRestoreConversation`, `win.BROWSER_NEW_TAB_URL`, `window.browsingContext.embedderElement`, `window.browsingContext?.topChromeWindow`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## AIWindow.#recreateAIChatBrowser()
- 位置: L818-825
- 役割: 既存の aichat browser を外して作り直す
- 触るとき: aichat browser の再生成条件を変えるとき。
- 呼び出し先: `this.#browser?.remove()`, `this.#createAIChatBrowser()`, `this.#getBrowserContainer()`

## AIWindow.#createAIChatBrowser()
- 位置: L827-840
- 役割: about:aichatcontent を読む privilegedabout の remote browser を作り、先頭に入れる
- 触るとき: chat content browser の属性や読み込み先を変えるとき。
- 呼び出し先: `browser.setAttribute()`, `container.prepend()`, `this.#updateBrowserTabbable()`, `this.ownerDocument.createXULElement()`
- 参照: `this.#browser`

## AIWindow.#updateBrowserTabbable()
- 位置: L845-854
- 役割: chat-active なら tabindex を外し、そうでなければ -1 にする
- 触るとき: 会話が無いときに空の browser にフォーカスが止まる問題を扱うとき。
- 呼び出し先: `this.classList.contains()`
- 条件付き依存: `if (this.classList.contains("chat-active"))` → `this.#browser.removeAttribute()`
- 条件付き依存: `if (!(this.classList.contains("chat-active")))` → `this.#browser.setAttribute()`
- 参照: `this.#browser`

## AIWindow.#setupWindowModeObserver()
- 位置: L856-869
- 役割: ai-window-state-changed を監視し、自ウィンドウならスマートバーを更新する
- 触るとき: ウィンドウがスマート状態に切り替わったときの表示を調べるとき。
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.#windowModeObserver`
- XPCOM: `Services.obs`

## this.#windowModeObserver()
- 位置: L857-863
- 役割: ウィンドウ状態の変化を受けて表示の更新を呼ぶ
- 触るとき: スマート状態の切り替え通知が届かないときに確認する。
- 条件付き依存: `if (subject == window.browsingContext?.topChromeWindow)` → `this.#updateSmartbarAndHeaderVisibility()`
- 参照: `window.browsingContext?.topChromeWindow`

## AIWindow.#updateSmartbarAndHeaderVisibility()
- 位置: L871-890
- 役割: スマートかどうかでスマートバーと切替ボタン、ヘッダーの表示を切り替える
- 触るとき: スマートモードとクラシックモードの見た目の切り替えを変えるとき。classic-mode 属性も付け外しする。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `this.renderRoot.querySelector()`, `this.toggleAttribute()`
- 参照: `chatHeader.hidden`, `this.#smartbar`, `this.#smartbar.hidden`, `this.#smartbarToggleButton`, `this.#smartbarToggleButton.hidden`, `window.browsingContext.topChromeWindow`

## AIWindow.disconnectedCallback()
- 位置: L892-1014
- 役割: 進行中のスターター生成を中断し、各種の購読・ボタン・スマートバー・会話を後始末する
- 触るとき: ウィンドウを閉じたときにリスナーや参照が残らないよう、後始末の項目を足すとき。
- 呼び出し先: `Services.prefs.removeObserver()`, `super.disconnectedCallback()`, `this.#abortController?.abort()`, `this.#removeClientErrorListeners()`, `this.#removeConversationListeners()`, `this.#resolveSmartbarReady()`, `this.#starterPromptsAbortController?.abort()`, `this.#swapDocShellsChromeWindow?.removeEventListener()`, `this.ownerDocument.removeEventListener()`
- 条件付き依存: `if (this.#visibilityChangeHandler)` → `this.ownerDocument.removeEventListener()`
- 条件付き依存: `if (this.#windowModeObserver)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#topSitesObserver)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#smartbarToggleButton)` → `this.#smartbarToggleButton.remove()`
- 条件付き依存: `if (this.#smartbar)` → `this.#smartbar.removeEventListener()`
- 条件付き依存: `if (this.#smartbar)` → `this.#smartbar.remove()`
- 条件付き依存: `if (this.#smartbarResizeObserver)` → `this.#smartbarResizeObserver.disconnect()`
- 条件付き依存: `if (this.#browser)` → `this.#browser.remove()`
- 参照: `this.#abortController`, `this.#browser`, `this.#conversation`, `this.#handleEndSwapDocShells`, `this.#handleMemoriesToggle`, `this.#handleModelChange`, `this.#handleOpenModelSettings`, `this.#handleSmartbarCommit`, `this.#handleStopGeneration`, `this.#memoriesButton`, `this.#onCustomEndpointPrefChanged`, `this.#onHistoryMenuEvent`, `this.#onModelChoicePrefChanged`, `this.#onPanelShowing`, `this.#openPanel`, `this.#pendingRestoreConversation`, `this.#removeClientErrorListeners`, `this.#smartbar`, `this.#smartbarResizeObserver`, `this.#smartbarToggleButton`, `this.#starterPromptsAbortController`, `this.#swapDocShellsChromeWindow`, `this.#topSitesObserver`, `this.#visibilityChangeHandler`, `this.#windowModeObserver`
- XPCOM: `Services.obs` / `Services.prefs`

## AIWindow.#loadAvailableModels()
- 位置: async L1019-1030
- 役割: モデル一覧を取得し、カスタム endpoint が無ければ先頭の項目を除いて保持する
- 触るとき: モデル選択肢の内容や、カスタム endpoint の扱いを変えるとき。
- 呼び出し先: `lazy.getAllModelsData()`, `lazy.openAIEngine.hasCustomEndpoint()`
- 参照: `this.availableModels`

## AIWindow.#updateSmartbarModels()
- 位置: L1037-1044
- 役割: スマートバーのモデル選択に一覧・選択中・既定の選択肢を渡す
- 触るとき: モデル選択 UI の表示が実際の選択とずれたとき。
- 呼び出し先: `smartbar?.querySelector()`
- 条件付き依存: `if (modelSelect && this.availableModels)` → `lazy.getCurrentModelChoiceId()`
- 参照: `modelSelect.availableModels`, `modelSelect.defaultModelChoiceId`, `modelSelect.selectedModelId`, `this.availableModels`, `this.selectedModelId`

## AIWindow.#onModelChoicePrefChanged()
- 位置: async L1046-1057
- 役割: タブ固有の上書きが無ければ、既定のモデル選択の pref 変更に追従する
- 触るとき: グローバルの既定モデルを変えたときに、タブ側が追従しない問題を調べるとき。
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#switchModel()`, `this.#updateSmartbarModels()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`, `this.availableModels`

## AIWindow.#handleModelChange()
- 位置: async L1059-1063
- 役割: スマートバーからのモデル変更を、タブ固有の上書きとして切り替える
- 触るとき: モデル変更イベントの受け口や上書きの扱いを変えるとき。
- 呼び出し先: `this.#switchModel()`
- 参照: `event.detail.modelChoiceId`

## AIWindow.#onCustomEndpointPrefChanged()
- 位置: async L1065-1076
- 役割: endpoint 変更で一覧を取り直し、上書きが無ければ既定へ切り替える
- 触るとき: カスタム endpoint を設定した後にモデル表示が古いままのとき。
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#loadAvailableModels()`, `this.#updateSmartbarModels()`
- 条件付き依存: `if ( !this.#hasModelChoiceOverride && this.availableModels[defaultModelChoiceId] )` → `this.#switchModel()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`, `this.availableModels`

## AIWindow.#onMistralReleasePrefChanged()
- 位置: async L1079-1093
- 役割: Mistral 切替の pref で、モデルのキャッシュを更新して選択を解決し直す
- 触るとき: Mistral の切り替えで選択が空になるとき。Bug 2053495 の撤去対象。
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `lazy.refreshModelsDataCache()`, `this.#loadAvailableModels()`, `this.#updateSmartbarModels()`
- 条件付き依存: `if ( !this.#hasModelChoiceOverride && this.availableModels[defaultModelChoiceId] )` → `this.#switchModel()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`, `this.availableModels`

## AIWindow.#setModelChoice()
- 位置: L1100-1105
- 役割: 選択中の選択肢 ID を保存し、対応するモデル名を selectedModelId に入れる
- 触るとき: モデル選択の状態をどこで決めるかを調べるとき。対応が無ければ既定のモデル名を使う。
- 呼び出し先: `lazy.getCurrentModelName()`
- 参照: `this.#selectedModelChoiceId`, `this.availableModels`, `this.availableModels?.[modelChoiceId]?.model`, `this.selectedModelId`

## AIWindow.#switchModel()
- 位置: async L1107-1128
- 役割: 選択を設定し、会話があればシステムプロンプトを読み直して、必要なら通知を出す
- 触るとき: モデル切替の副作用（システムプロンプトやイベント）を変えるとき。
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#setModelChoice()`
- 条件付き依存: `if (this.#conversation?.messages.length)` → `this.#conversation.loadSystemPrompt()`
- 条件付き依存: `if (isTabOverride)` → `this.#dispatchChromeEvent()`
- 条件付き依存: `if (isTabOverride)` → `this.#getAIWindowEventOptions()`
- 参照: `this.#conversation?.messages.length`, `this.#hasModelChoiceOverride`, `this.selectedModelId`

## AIWindow.restoreModelChoiceOverride()
- 位置: L1135-1139
- 役割: タブごとのモデル上書きを復元し、無ければ既定の選択に戻す
- 触るとき: タブ切り替え時にモデル選択を復元する挙動を変えるとき。
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#setModelChoice()`, `this.#updateSmartbarModels()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`

## AIWindow.#handleOpenModelSettings()
- 位置: L1141-1143
- 役割: トップのウィンドウで Smart Window の個人設定画面を開く
- 触るとき: モデル設定画面への導線を変えるとき。
- 呼び出し先: `this.#topChromeWindow?.openPreferences()`

## AIWindow.#loadPendingConversation()
- 位置: async L1148-1182
- 役割: data-conversation-id があれば会話を開き、無ければ新規会話の ID をホストに記録する
- 触るとき: 起動時やタブ復元で会話を再開する挙動を変えるとき。継続ストリームが残っていればその続きを実行する。
- 呼び出し先: `lazy.AIWindow.chatStore.findConversationById()`, `this.#getPendingConversationId()`, `this.#hostBrowser?.hasAttribute()`, `this.#resetConversationState()`, `this.openConversation()`
- 条件付き依存: `if (!conversationId)` → `this.#hostBrowser?.setAttribute()`
- 条件付き依存: `if (!conversationId)` → `this.#syncHistoryState()`
- 条件付き依存: `if (conversation)` → `Glean.smartWindow.chatRetrieved.record()`
- 条件付き依存: `if (conversation)` → `Date.now()`
- 条件付き依存: `if (this.#hostBrowser?.hasAttribute("data-continue-streaming"))` → `this.#hostBrowser.removeAttribute()`
- 条件付き依存: `if (this.#hostBrowser?.hasAttribute("data-continue-streaming"))` → `this.#continueAfterToolResult()`
- 参照: `conversation.id`, `conversation.updatedDate`, `this.#conversation.id`, `this.#conversation?.messageCount`, `this.mode`

## AIWindow.firstUpdated()
- 位置: async L1184-1223
- 役割: aichat browser を作り、スマートバーを作成して、会話の差し替えとトップサイト同期を行う
- 触るとき: 初回表示の順序や、隠れたタブでのスマートバー生成のタイミングを変えるとき。
- 呼び出し先: `console.error()`, `error.toString()`, `this.#createAIChatBrowser()`, `this.#getBrowserContainer()`, `this.#loadPendingConversation()`, `this.#loadPendingConversation().catch()`, `this.#swapConversation()`, `this.#syncTopSites()`
- 条件付き依存: `if (doc.hidden)` → `doc.addEventListener()`
- 条件付き依存: `if (!(doc.hidden))` → `this.#getOrCreateSmartbar()`
- 参照: `doc.hidden`, `error.stack`, `this.#conversation`, `this.#visibilityChangeHandler`, `this.ownerDocument`

## this.#visibilityChangeHandler()
- 位置: L1192-1203
- 役割: 隠れていたタブが表示されたときにスマートバーを作り、再開セクションの非表示状態を読み直す
- 触るとき: Hide for now の状態が古いまま残るなど、タブ表示時の再読み込みを調べるとき。
- 条件付き依存: `if (!doc.hidden && !this.#smartbar)` → `this.#getOrCreateSmartbar()`
- 条件付き依存: `if (!doc.hidden)` → `lazy.ResumeActivity.isSectionHiddenForSession()`
- 参照: `doc.hidden`, `this.#smartbar`, `this.resumeSectionHidden`

## AIWindow.updateInput()
- 位置: L1232-1251
- 役割: 保存済みの入力（テキストとメンション）をスマートバーに戻す
- 触るとき: タブ切り替えで入力内容を復元する挙動を変えるとき。メンションは文字オフセットの位置に入れ直す。
- 呼び出し先: `editor.insertMention()`
- 参照: `mentions.length`, `this.#smartbar`, `this.#smartbar.inputField`, `this.#smartbar.value`

## AIWindow.restoreContextChips()
- 位置: L1261-1266
- 役割: タブごとの文脈チップをスマートバーに復元する
- 触るとき: タブ切り替え時の文脈チップの復元を変えるとき。
- 呼び出し先: `this.#smartbar?.restoreContextChips()`

## AIWindow.#getSmartbarInputState()
- 位置: L1275-1288
- 役割: スマートバーの入力をテキストとメンションの文字オフセットに変換して返す
- 触るとき: 入力内容の保存形式を変えるとき。エディタが無ければ空の状態を返す。
- 呼び出し先: `editor.getAllMentions()`, `editor.getAllMentions().map()`, `editor.posToTextOffset()`
- 参照: `editor.plainText`, `lazy.EMPTY_SMARTBAR_INPUT_STATE`, `mention.pos`, `mention.textOffset`, `this.#smartbar?.inputField`

## AIWindow.loadStarterPrompts()
- 位置: async L1299-1496
- 役割: スターターを組み立てて描画する。サイドバーは生成結果を cache し、全画面は再開候補を合成する
- 触るとき: スターターの生成条件や順序、表示先（ピルかカードか）を変えるとき。タブ切替と切断での中断条件もここを見る。
- 呼び出し先: `lazy.NewTabStarterGenerator.getPrompts()`, `lazy.log.error()`, `newTabStarterIds.map()`, `texts.map()`, `this.#getCurrentTab()`, `this.#starterPromptsAbortController?.abort()`, `this.ownerDocument.l10n .formatValues()`, `this.ownerDocument.l10n .formatValues(newTabStarterIds.map(({ l10nId }) => ({ id: l10nId }))) .then()`
- 条件付き依存: `if (clear)` → `this.#renderStarterPrompts()`
- 条件付き依存: `if (this.mode === MODE.SIDEBAR && gBrowser)` → `this.#smartbar.getCurrentContextData()`
- 条件付き依存: `if (this.mode === MODE.SIDEBAR && gBrowser)` → `contextWebsites.map()`
- 条件付き依存: `if (this.mode === MODE.SIDEBAR && gBrowser)` → `JSON.stringify()`
- 条件付き依存: `if (this.mode === MODE.SIDEBAR && gBrowser)` → `this.#sidebarStarterCache.get()`
- 条件付き依存: `if (!sidebarStarters)` → `lazy .generateConversationStartersSidebar()`
- 条件付き依存: `if (!sidebarStarters)` → `lazy.log.error()`
- 条件付き依存: `if (shouldLoadResumeStarters)` → `this.#refreshHasMemories()`
- 条件付き依存: `if (this.#resumeActivityMemoriesEnabled)` → `lazy.generateResumeActivityConversationStarters()`
- 条件付き依存: `if (!(this.resumeCardsPref))` → `this.#renderStarterPrompts()`
- 条件付き依存: `if (!(this.resumeCardsPref))` → `Array(MAX_PILL_COUNT).fill()`
- 条件付き依存: `if (!(this.resumeCardsPref))` → `Array()`
- 条件付き依存: `if (rendersCardsIndependently && !abortController.signal.aborted)` → `this.#renderStarterPrompts()`
- 条件付き依存: `if (sidebarStarters)` → `this.#sidebarStarterCache.delete()`
- 条件付き依存: `if ( this.#sidebarStarterCache.size >= MAX_SIDEBAR_STARTER_CACHE_KEYS )` → `this.#sidebarStarterCache.keys().next()`
- 条件付き依存: `if ( this.#sidebarStarterCache.size >= MAX_SIDEBAR_STARTER_CACHE_KEYS )` → `this.#sidebarStarterCache.keys()`
- 条件付き依存: `if ( this.#sidebarStarterCache.size >= MAX_SIDEBAR_STARTER_CACHE_KEYS )` → `this.#sidebarStarterCache.delete()`
- 条件付き依存: `if (sidebarStarters)` → `this.#sidebarStarterCache.set()`
- 条件付き依存: `if (this.mode === MODE.SIDEBAR && gBrowser)` → `this.#getCurrentTab()`
- 条件付き依存: `if (resumeStartersPromise)` → `this.#applyResumeActivities()`
- 条件付き依存: `if (resumeStartersPromise)` → `this.#getCurrentTab()`
- 条件付き依存: `if (!this.resumeCardsPref && selectedTab === this.#getCurrentTab())` → `this.#resumeActivitiesToStarterPrompts( resumeActivities ).slice()`
- 条件付き依存: `if (!this.resumeCardsPref && selectedTab === this.#getCurrentTab())` → `this.#resumeActivitiesToStarterPrompts()`
- 条件付き依存: `if (!this.resumeCardsPref && selectedTab === this.#getCurrentTab())` → `[...resumeStarters, ...starters].slice()`
- 条件付き依存: `if (!rendersCardsIndependently && !abortController.signal.aborted)` → `this.#renderStarterPrompts()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `abortController.signal.aborted`, `contextWebsite.label`, `contextWebsite.url`, `gBrowser?.tabs.length`, `newTabStarterIds[i].type`, `selectedTab.linkedBrowser.currentURI.spec`, `sidebarStarters?.length`, `this.#canLoadResumeStarters`, `this.#conversation`, `this.#conversation.messageCount`, `this.#conversation.transientStarterUrl`, `this.#conversation.transientStarters`, `this.#conversation?.messageCount`, `this.#memoriesIconShown`, `this.#memoriesToggled`, `this.#resumeActivityEnabled`, `this.#resumeActivityMemoriesEnabled`, `this.#sidebarStarterCache.keys().next().value`, `this.#sidebarStarterCache.size`, `this.#smartbarReadyPromise`, `this.#starterPromptsAbortController`, `this.#starterPromptsAbortController.signal`, `this.conversationId`, `this.isConnected`, `this.mode`, `this.resumeCardsLoading`, `this.resumeCardsPref`, `window.browsingContext?.topChromeWindow.gBrowser`

## AIWindow.#hasValidHeadline()
- 位置: L1498-1500
- 役割: 再開候補の見出しが空白でないかを判定する
- 触るとき: 再開候補を有効とみなす条件を変えるとき。
- 呼び出し先: `content.headline.trim()`

## AIWindow.#applyResumeActivities()
- 位置: L1509-1535
- 役割: 有効で未非表示の再開候補に絞り、空の理由を決めてカードに反映する
- 触るとき: 再開カードの空状態メッセージや表示件数を変えるとき。
- 呼び出し先: `lazy.ResumeActivity.isMemoryDismissed()`, `rawResumeActivities.filter()`, `resumeActivities.slice()`, `this.#hasValidHeadline()`, `validResumeActivities.filter()`
- 条件付き依存: `if (this.resumeCards.length)` → `lazy.ResumeActivity.clearSectionHiddenForSession()`
- 参照: `RESUME_SECTION_EMPTY_REASON.ALL_DISMISSED`, `RESUME_SECTION_EMPTY_REASON.NO_SUGGESTIONS`, `memory.id`, `resumeActivities.length`, `this.resumeCards`, `this.resumeCards.length`, `this.resumeCardsEmptyReason`, `this.resumeSectionHidden`, `validResumeActivities.length`

## AIWindow.#resumeActivitiesToStarterPrompts()
- 位置: L1537-1547
- 役割: 再開候補をスターター形式（type resume、プレビューアイコン付き）に変換する
- 触るとき: 再開候補をピルとして出すときの項目や見た目を変えるとき。
- 呼び出し先: `content.previewTabs.map()`, `resumeActivities.map()`
- 参照: `content.headline`

## AIWindow.#renderStarterPrompts()
- 位置: L1563-1585
- 役割: スターターを状態に入れて表示フラグを立て、必要なら表示テレメトリを送って再描画する
- 触るとき: スターター行の表示条件や表示テレメトリを変えるとき。会話にメッセージがあれば空にする。
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (this.showStarters && recordTelemetry)` → `this.#starters.filter()`
- 条件付き依存: `if (this.showStarters && recordTelemetry)` → `this.onQuickPromptDisplayed()`
- 参照: `starter.type`, `this.#conversation?.messages?.length`, `this.#starters`, `this.#starters.filter( starter => starter.type === "resume" ).length`, `this.#starters.length`, `this.isConnected`, `this.showStarters`, `this.startersResolved`

## AIWindow.#topSitesEnabled()
- 位置: L1593-1595
- 役割: トップサイトを使うかを、非表示 pref が off かつフィード pref が on で判定する
- 触るとき: トップサイト欄の表示条件を変えるとき。
- 参照: `this.hideTopSitesPref`, `this.topSitesFeedPref`

## AIWindow.#syncTopSites()
- 位置: L1604-1621
- 役割: 全画面モードならトップサイトを読み込み、そうでなければ空にする
- 触るとき: トップサイト欄の表示と、その計測のタイミングを変えるとき。非表示のタブでは starter の待ちを飛ばす。
- 条件付き依存: `if (this.mode === MODE.FULLPAGE)` → `Glean.smartWindow.topsitesEnabled.set()`
- 条件付き依存: `if (this.mode === MODE.FULLPAGE && this.#topSitesEnabled)` → `this.#loadTopSites()`
- 参照: `MODE.FULLPAGE`, `this.#topSitesEnabled`, `this.mode`, `this.ownerDocument.hidden`, `this.startersResolved`, `this.topSites`

## AIWindow.#loadTopSites()
- 位置: L1623-1644
- 役割: AboutNewTab から取得し、URL があり広告でない先頭 8 件を保持して表示を計測する
- 触るとき: トップサイトの絞り込み条件や件数上限を変えるとき。
- 呼び出し先: `(sites ?? []) .filter()`, `(sites ?? []) .filter(site => site?.url && !site.sponsored_position) .slice()`, `lazy.AboutNewTab.getTopSites()`, `lazy.log.error()`
- 条件付き依存: `if (this.topSites.length)` → `Glean.smartWindow.topsitesImpression.record()`
- 参照: `site.sponsored_position`, `site?.url`, `this.isConnected`, `this.topSites`, `this.topSites.length`

## AIWindow.#handleTopSiteSelected()
- 位置: L1652-1663
- 役割: 選択されたトップサイトを現在のタブで開き、クリックを計測する
- 触るとき: トップサイトを押したあとの遷移先や計測項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.topsitesClick.record()`, `lazy.URILoadingHelper.openTrustedLinkIn()`
- 参照: `event.detail`, `this.#topChromeWindow`, `this.topSites.length`

## AIWindow.#handleResumeSectionHide()
- 位置: L1670-1673
- 役割: 再開セクションをセッション中は隠す
- 触るとき: Hide for now の挙動を変えるとき。
- 呼び出し先: `lazy.ResumeActivity.hideSectionForSession()`
- 参照: `this.resumeSectionHidden`

## AIWindow.#handleResumeCardMenuItemSelected()
- 位置: L1682-1702
- 役割: 再開カードのメニューを処理する。open-tabs はタブを開き、snooze はそのカードを隠す
- 触るとき: カードのメニュー項目を追加・変更するとき。snooze は残りのカードが無くなると空の理由を更新する。
- 呼び出し先: `lazy.ResumeActivity.dismissMemory()`, `lazy.log.error()`, `this.#handleResumeCardOpenTabs()`, `this.#handleResumeCardOpenTabs(journeyId).catch()`, `this.resumeCards.filter()`
- 参照: `RESUME_SECTION_EMPTY_REASON.ALL_DISMISSED`, `event.detail`, `memory.id`, `this.resumeCards`, `this.resumeCards.length`, `this.resumeCardsEmptyReason`

## AIWindow.#handleResumeCardOpenTabs()
- 位置: async L1710-1723
- 役割: カードのプレビュータブを ToolUI でグループにまとめて開く
- 触るとき: 再開カードからタブを開く動作（グループ化や単一タブの扱い）を変えるとき。
- 呼び出し先: `formatResumeTabGroupLabel()`, `lazy.ToolUI.openOrGroupTabs()`, `this.resumeCards.find()`
- 参照: `card.content.headline`, `card?.content.previewTabs`, `memory.id`, `previewTabs?.length`, `this.#topChromeWindow`

## AIWindow.#getOrCreateSmartbar()
- 位置: L1730-1807
- 役割: moz-smartbar と切替ボタンを作って差し込み、イベントを張って表示を更新する
- 触るとき: スマートバーの生成方法や購読するイベントを変えるとき。既にあれば作らず参照だけを更新する。
- 呼び出し先: `smartbar.querySelector()`, `this.#updateSmartbarAndHeaderVisibility()`, `this.renderRoot.querySelector()`, `this.syncSmartbarMemoriesStateFromConversation()`
- 条件付き依存: `if (!smartbar)` → `doc.createElement()`
- 条件付き依存: `if (!smartbar)` → `smartbar.setAttribute()`
- 条件付き依存: `if (!smartbar)` → `smartbar.classList.add()`
- 条件付き依存: `if (!smartbar)` → `smartbar.addEventListener()`
- 条件付き依存: `if (!smartbar)` → `this.#resolveSmartbarReady()`
- 条件付き依存: `if (!smartbar)` → `this.#setupSmartbarFocus()`
- 条件付き依存: `if (!smartbar)` → `this.#observeSmartbarHeight()`
- 条件付き依存: `if (!smartbar)` → `this.#updateSmartbarModels()`
- 条件付き依存: `if (!smartbar)` → `smartbarWrapper.appendChild()`
- 条件付き依存: `if (!smartbar)` → `this.renderRoot.querySelector("#smartbar-slot").append()`
- 条件付き依存: `if (!smartbar)` → `this.renderRoot.querySelector()`
- 条件付き依存: `if (!toggleButton)` → `doc.createElement()`
- 条件付き依存: `if (!toggleButton)` → `toggleButton.setAttribute()`
- 条件付き依存: `if (!toggleButton)` → `toggleButton.addEventListener()`
- 条件付き依存: `if (chromeWindow)` → `lazy.AIWindow.toggleAIWindow()`
- 条件付き依存: `if (!toggleButton)` → `this.renderRoot.querySelector("#smartbar-slot").append()`
- 条件付き依存: `if (!toggleButton)` → `this.renderRoot.querySelector()`
- 参照: `MODE.SIDEBAR`, `smartbar.id`, `smartbar.isSidebarMode`, `smartbarWrapper.id`, `this.#handleContextChips`, `this.#handleMemoriesToggle`, `this.#handleSmartbarInput`, `this.#memoriesButton`, `this.#smartbar`, `this.#smartbarToggleButton`, `this.mode`, `toggleButton.iconSrc`, `toggleButton.id`, `toggleButton.type`, `window.browsingContext?.topChromeWindow`

## AIWindow.#handleContextChips()
- 位置: L1815-1824
- 役割: 文脈チップの状態を ai-window:context-chips-changed で送る
- 触るとき: 文脈チップの保存経路を調べるとき。
- 呼び出し先: `this.#dispatchChromeEvent()`, `this.#getEventTab()`
- 参照: `this.#smartbar?.contextChips`, `this.#smartbar?.removedImplicitContextChip`

## AIWindow.#setupSmartbarFocus()
- 位置: L1826-1846
- 役割: 初回の自動フォーカスではフォーカス枠を出さず、マウス操作時は枠を出す
- 触るとき: スマートバーのフォーカス枠の出し方を変えるとき。
- 呼び出し先: `smartbar.addEventListener()`, `smartbar.focus()`, `smartbar.inputField.addEventListener()`, `smartbar.toggleAttribute()`
- 条件付き依存: `if (!hasAutoFocused)` → `smartbar.toggleAttribute()`
- 条件付き依存: `if (!isMouseClick)` → `smartbar.removeAttribute()`

## AIWindow.#observeSmartbarHeight()
- 位置: L1848-1862
- 役割: 閉じた時のスマートバー高さを監視し、サイズ変化のたびに更新する
- 触るとき: スマートバーの高さに依存するレイアウトを変えるとき。
- 呼び出し先: `this.#smartbarResizeObserver.observe()`, `updateSmartbarHeight()`
- 参照: `this.#smartbar`, `this.#smartbarResizeObserver`

## updateSmartbarHeight()
- 位置: L1849-1857
- 役割: 結果一覧を除いたスマートバーの高さを --smartbar-height に書く
- 触るとき: 結果一覧の高さの計算方法を変えるとき。.urlbarView が唯一の可変要素という前提に依存する。
- 呼び出し先: `this.#smartbar.querySelector()`, `this.style.setProperty()`
- 参照: `this.#smartbar.offsetHeight`, `urlbarView.offsetHeight`

## AIWindow.#handleSmartbarInput()
- 位置: L1872-1877
- 役割: スマートバーの入力状態を ai-window:smartbar-input で送る
- 触るとき: 入力内容の保存や同期のタイミングを変えるとき。
- 呼び出し先: `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#getSmartbarInputState()`

## AIWindow.#dispatchChromeEvent()
- 位置: L1889-1894
- 役割: トップレベルの chrome window に指定のイベントを発火する
- 触るとき: chrome 側へ状態を通知する経路を調べるとき。
- 呼び出し先: `topChromeWindow?.dispatchEvent()`
- 参照: `topChromeWindow.CustomEvent`, `window?.browsingContext?.topChromeWindow`

## AIWindow.#handleStopGeneration()
- 位置: L1901-1918
- 役割: 生成を中止し、最後の応答を完了扱いにして chat content に送る
- 触るとき: 生成停止時の後始末や、最後のメッセージの扱いを変えるとき。
- 呼び出し先: `this.#abortController.abort()`, `this.#conversation?.getHistoryResultsSnapshot()`, `this.#conversation?.messages ?.filter()`, `this.#conversation?.messages ?.filter( m => m.role == lazy.MESSAGE_ROLE.ASSISTANT && m?.content?.type == "text" ) .at()`, `this.#dispatchMessageToChatContent()`
- 参照: `lastAssistant?.citations`, `lastAssistant?.id`, `lazy.MESSAGE_ROLE.ASSISTANT`, `m.role`, `m?.content?.type`, `this.#abortController`, `this.isGenerating`

## AIWindow.#handleSmartbarCommit()
- 位置: L1926-2033
- 役割: 送信を受けてコマンドならそのまま処理し、チャットなら文脈を添えて送り、検索・移動は計測する
- 触るとき: 送信の分岐（チャット・検索・ナビゲーション）や計測項目を変えるとき。
- 呼び出し先: `lazy.log.debug()`, `this.#calculateCurrentMentions()`, `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#smartbar.clearSmartbarInput()`, `triggeringEvent?.type.startsWith()`
- 条件付き依存: `if (action === ACTION.CHAT)` → `lazy.AgentUI.tryHandleCommand()`
- 条件付き依存: `if ( lazy.AgentUI.tryHandleCommand({ command, value, contextPageUrl, conversation: this.#conversation, window: this.#topChromeWindow, isFullPage: this.mode === M...)` → `this.classList.contains()`
- 条件付き依存: `if (!this.classList.contains("chat-active"))` → `this.#initActiveChatlayout()`
- 条件付き依存: `if (allUrls.size)` → `this.#conversation.addSeenUrls()`
- 条件付き依存: `if (action === ACTION.CHAT)` → `this.submitChatMessage()`
- 条件付き依存: `if (action === ACTION.CHAT)` → `this.#withTabGroupMembers()`
- 条件付き依存: `if (action === ACTION.SEARCH)` → `Glean.smartWindow.searchSubmit.record()`
- 条件付き依存: `if (action === ACTION.NAVIGATE)` → `Glean.smartWindow.navigateSubmit.record()`
- 条件付き依存: `if ( this.mode === MODE.SIDEBAR && (action === ACTION.NAVIGATE || action === ACTION.SEARCH) )` → `this.#dispatchChromeEvent()`
- 条件付き依存: `if ( this.mode === MODE.SIDEBAR && (action === ACTION.NAVIGATE || action === ACTION.SEARCH) )` → `this.#getAIWindowEventOptions()`
- 参照: `ACTION.CHAT`, `ACTION.NAVIGATE`, `ACTION.SEARCH`, `MODE.FULLPAGE`, `MODE.SIDEBAR`, `allUrls.size`, `event.detail`, `inlineMentions.length`, `lazy.EMPTY_SMARTBAR_INPUT_STATE`, `this.#conversation`, `this.#handleSmartbarCommit.name`, `this.#topChromeWindow`, `this.conversationId`, `this.conversationMessageCount`, `this.mode`, `this.modelName`, `value.length`

## AIWindow.#calculateCurrentMentions()
- 位置: L2043-2087
- 役割: チップのメンションと @ のメンションを重複排除して結合し、URL 集合を作る
- 触るとき: 送信時の文脈として何を含めるかを変えるとき。タブグループの @ は色を付けて扱う。
- 呼び出し先: `allUrls.add()`, `atMentions.push()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.getContextMentionKey()`, `lazy.parseTabGroupMentionId()`, `seenKeys.add()`, `seenKeys.has()`, `this.#getInlineMentions()`
- 条件付き依存: `if (key)` → `seenKeys.add()`
- 条件付き依存: `if (mention.url)` → `allUrls.add()`
- 条件付き依存: `if (groupId)` → `atMentions.push()`
- 条件付き依存: `if (groupId)` → `this.#getTabGroupColor()`
- 参照: `lazy.CONTEXT_MENTION_TYPE.TAB_GROUP`, `mention.id`, `mention.label`, `mention.type`, `mention.url`

## AIWindow.#withTabGroupMembers()
- 位置: L2095-2101
- 役割: タブグループのメンバーを展開して既見 URL に加え、元のメンションに足す
- 触るとき: タブグループ指定時に送る文脈の範囲を変えるとき。
- 呼び出し先: `this.#expandTabGroupMentions()`
- 条件付き依存: `if (tabGroupMembers.length)` → `this.#conversation?.addSeenUrls()`
- 条件付き依存: `if (tabGroupMembers.length)` → `tabGroupMembers.map()`
- 参照: `tabGroupMembers.length`

## AIWindow.#expandTabGroupMentions()
- 位置: L2107-2130
- 役割: タブグループ指定を、上限までのメンバーに展開する（重複は除く）
- 触るとき: グループ展開の上限や重複判定を変えるとき。上限は MAX_TAB_GROUP_MEMBERS。
- 呼び出し先: `lazy.getContextMentionKey()`, `mentions.map()`, `seen.has()`, `this.#getTabGroupMembers()`
- 条件付き依存: `if (!seen.has(key))` → `seen.add()`
- 条件付き依存: `if (!seen.has(key))` → `tabGroupMembers.push()`
- 参照: `lazy.CONTEXT_MENTION_TYPE.TAB_GROUP`, `lazy.MAX_TAB_GROUP_MEMBERS`, `lazy.getContextMentionKey`, `mention.groupId`, `mention.type`, `tabGroupMembers.length`

## AIWindow.#getTabGroup()
- 位置: L2138-2142
- 役割: 現在のウィンドウのタブグループを ID で探す
- 触るとき: タブグループの参照元を変えるとき。
- 呼び出し先: `this.#topChromeWindow.gBrowser.tabGroups.find()`
- 参照: `group.id`

## AIWindow.#getTabGroupColor()
- 位置: L2148-2150
- 役割: タブグループの色を返す
- 触るとき: @ メンションの色表示を変えるとき。
- 呼び出し先: `this.#getTabGroup()`
- 参照: `this.#getTabGroup(groupId)?.color`

## AIWindow.#getTabGroupMembers()
- 位置: L2157-2179
- 役割: 表示可能なグループのタブを上限まで、ラベル付きの文脈メンションに変換する
- 触るとき: グループのメンバーの絞り込みや表示名を変えるとき。
- 呼び出し先: `group.tabs.map()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.tabManagementService.getTabGroupById()`, `tabGroupLabels.get()`, `this.#getTabGroup()`, `visibleGroup.tabs.slice()`, `visibleGroup.tabs.slice(0, limit).map()`
- 参照: `lazy.CONTEXT_MENTION_TYPE.TAB`, `tab.label`, `tab.linkedBrowser?.currentURI?.spec`, `this.#topChromeWindow`, `visibleGroup.id`, `visibleGroup.label`

## AIWindow.#getInlineMentions()
- 位置: L2186-2192
- 役割: エディタのインラインメンションを取り出す。エディタが無ければ空配列
- 触るとき: インラインメンションの取得元を変えるとき。
- 呼び出し先: `editor.getAllMentions()`
- 参照: `editor?.getAllMentions`, `this.#smartbar?.inputField`

## AIWindow.submitChatMessage()
- 位置: L2213-2262
- 役割: 空でないテキストを整え、計測して AI 応答の取得を始める
- 触るとき: チャット送信の共通処理や計測項目を変えるとき。自動キャンセルと利用回数の加算もここで行う。
- 呼び出し先: `Glean.smartWindow.chatSubmit.record()`, `String()`, `String(text ?? "").trim()`, `contextMentions.filter()`, `lazy.ToolUI.autoCancelActiveConfirmation()`, `lazy.ToolUI.autoCancelActiveConfirmation( this.#conversation, this.#topChromeWindow, this.mode ).catch()`, `lazy.isTabGroupMember()`, `lazy.log.error()`, `this.#createUserRoleOpts()`, `this.#fetchAIResponse()`, `this.#recordChatInteraction()`
- 参照: `contextMentions.filter(member => !lazy.isTabGroupMember(member)) .length`, `this.#conversation`, `this.#conversation.lastSubmitType`, `this.#topChromeWindow`, `this.conversationId`, `this.conversationMessageCount`, `this.mode`, `this.modelName`, `trimmed.length`

## AIWindow.#handleMemoriesToggle()
- 位置: async L2264-2290
- 役割: 記憶トグルの切り替えを計測し、押下状態を保存して UI を同期する
- 触るとき: 記憶トグルの動作や計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.memoriesToggle.record()`, `console.error()`, `lazy.MemoriesManager.getAllMemories()`, `lazy.log.debug()`, `this.#saveMemoriesToggleToConversation()`, `this.#syncMemoriesButtonUI()`
- 参照: `event.detail.pressed`, `memories.length`, `this.#conversation?.messageCount`, `this.#handleMemoriesToggle.name`, `this.#memoriesToggled`, `this.conversationId`, `this.mode`

## AIWindow.#saveMemoriesToggleToConversation()
- 位置: L2292-2300
- 役割: メッセージのある会話にだけ記憶トグルを保存し、会話を更新する
- 触るとき: 会話への保存条件を変えるとき。空の会話へ保存すると制約違反になるため。
- 呼び出し先: `this.#updateConversation()`
- 参照: `this.#conversation`, `this.#conversation.memoriesToggled`, `this.#conversation.messageCount`

## AIWindow.#handlePromptSelected()
- 位置: L2308-2315
- 役割: 提案の選択を受け、再開候補なら再開処理へ、それ以外は通常の提案として送る
- 触るとき: 提案をクリックしたときの分岐を変えるとき。
- 呼び出し先: `this.onQuickPromptClicked()`
- 条件付き依存: `if (event.detail.type === "resume")` → `this.#handleResumePromptSelected()`
- 参照: `event.detail`, `event.detail.text`, `event.detail.type`

## AIWindow.#handleResumePromptSelected()
- 位置: L2317-2327
- 役割: 生成中でなければ再開のクリックを計測し、再開の会話生成を始める
- 触るとき: 再開候補の二重実行防止や計測を変えるとき。
- 呼び出し先: `lazy.log.error()`, `this.#generateResumeActivityConversation()`, `this.#generateResumeActivityConversation(resumePrompt).catch()`, `this.#recordQuickPromptClicked()`
- 参照: `this.#isGeneratingResumeActivityConversation`

## AIWindow.#handleResumeCardResume()
- 位置: L2337-2349
- 役割: 再開カードの操作を、対応するカードの記憶と内容を付けて再開処理へ渡す
- 触るとき: カードから再開する経路を変えるとき。該当カードが無ければ何もしない。
- 呼び出し先: `this.#handleResumePromptSelected()`, `this.resumeCards.find()`
- 参照: `card.content`, `card.content.headline`, `card.memory`, `event.detail`, `memory.id`

## AIWindow.#handlePromptDismissed()
- 位置: L2357-2368
- 役割: 記憶をセッション中無効にし、そのピルを候補から外して再描画し、閉じた操作を計測する
- 触るとき: 提案を閉じた後の後始末や計測を変えるとき。
- 呼び出し先: `lazy.ResumeActivity.dismissMemory()`, `this.#conversation.transientStarters.filter()`, `this.#recordQuickPromptDismissed()`, `this.#renderStarterPrompts()`
- 参照: `event.detail`, `memory.id`, `starter.memory?.id`, `this.#conversation.transientStarters`

## AIWindow.#generateResumeActivityConversation()
- 位置: async L2382-2464
- 役割: 記憶ありで会話を作り、失敗時は記憶なしで補い、会話が変わっていなければ開いて送る
- 触るとき: 再開候補をクリックしたときに作られる会話とグループ確認カードの内容を変えるとき。
- 呼び出し先: `String()`, `conversation.injectRealTimeContext()`, `conversation.messages.at()`, `formatResumeTabGroupLabel()`, `resumePrompt.content.previewTabs.map()`, `this.openConversation()`, `this.submitChatMessage()`
- 条件付き依存: `if (this.#resumeActivityMemoriesEnabled)` → `lazy.constructConversationToResumeActivity()`
- 条件付き依存: `if (this.#resumeActivityMemoriesEnabled)` → `lazy.log.error()`
- 条件付き依存: `if (!conversation)` → `this.#buildPlainResumeConversation()`
- 条件付き依存: `if (!conversation)` → `lazy.log.error()`
- 参照: `conversationAtClick?.id`, `resumePrompt.content`, `resumePrompt.content.headline`, `resumePrompt.content.previewTabs?.length`, `resumePrompt.memory`, `resumePrompt.memory.id`, `resumePrompt.text`, `this.#conversation`, `this.#isGeneratingResumeActivityConversation`, `this.#resumeActivityMemoriesEnabled`, `userMessage?.content?.body`

## AIWindow.#buildPlainResumeConversation()
- 位置: async L2481-2492
- 役割: 見出しだけを使う記憶なしの会話を作り、ユーザー発言を入れて機密属性を設定する
- 触るとき: 記憶を使わない再開の会話の作り方や機密属性を変えるとき。
- 呼び出し先: `conversation.addUserMessage()`, `conversation.loadSystemPrompt()`, `conversation.securityProperties.commit()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`
- 参照: `lazy.ChatConversation`, `resumePrompt.content.headline`

## AIWindow.onQuickPromptDisplayed()
- 位置: L2502-2510
- 役割: quick_prompt_displayed を、提案数と再開提案数付きで Glean に記録する
- 触るとき: 提案の表示計測の項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.quickPromptDisplayed.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#recordQuickPromptClicked()
- 位置: L2518-2526
- 役割: quick_prompt_clicked を種別と starter フラグ付きで記録する
- 触るとき: 提案クリックの計測項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.quickPromptClicked.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#recordQuickPromptDismissed()
- 位置: L2531-2535
- 役割: quick_prompt_dismissed を記録する
- 触るとき: 提案を閉じた計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.quickPromptDismissed.record()`
- 参照: `this.conversationId`

## AIWindow.onQuickPromptClicked()
- 位置: L2546-2560
- 役割: 提案のクリックを計測し、文脈を添えてチャットとして送る
- 触るとき: 提案文をそのまま送る挙動や、提案に付ける文脈を変えるとき。
- 呼び出し先: `this.#recordQuickPromptClicked()`, `this.#smartbar.getCurrentContextData()`, `this.#withTabGroupMembers()`, `this.submitChatMessage()`

## AIWindow.onOpenLink()
- 位置: L2562-2568
- 役割: リンクのクリックを link_click として計測する
- 触るとき: リンク計測の項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.linkClick.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#createUserRoleOpts()
- 位置: L2577-2586
- 役割: 記憶の有効設定と、その設定の出どころ（グローバルか会話か）を持つ UserRoleOpts を作る
- 触るとき: チャットに渡す記憶の扱いを変えるとき。
- 参照: `lazy.MEMORIES_FLAG_SOURCE.CONVERSATION`, `lazy.MEMORIES_FLAG_SOURCE.GLOBAL`, `lazy.UserRoleOpts`, `this.#memoriesIconShown`, `this.#memoriesToggled`

## AIWindow.#updateConversation()
- 位置: async L2593-2599
- 役割: 会話の状態をストアに保存し、失敗はログに残す
- 触るとき: 会話の保存先や保存のタイミングを調べるとき。
- 呼び出し先: `lazy.AIWindow.chatStore .updateConversation()`, `lazy.AIWindow.chatStore .updateConversation(this.#conversation) .catch()`, `lazy.log.error()`
- 参照: `this.#conversation`, `updateError.message`

## AIWindow.#addConversationTitle()
- 位置: async L2607-2640
- 役割: タイトルが無ければ生成して会話とドキュメントのタイトルに入れ、保存する
- 触るとき: タイトル生成の条件や元にする情報を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `lazy.generateChatTitle()`, `this.#conversation.messages.find()`, `this.#updateConversation()`
- 参照: `document.title`, `firstUserMessage?.content?.body`, `firstUserMessage?.pageUrl?.href`, `lazy.MESSAGE_ROLE.USER`, `m.role`, `this.#conversation.pageMeta?.description`, `this.#conversation.pageMeta?.title`, `this.#conversation.title`, `this.#conversation.titlePromise`, `this.conversationId`

## AIWindow.#updateTabFavicon()
- 位置: L2642-2648
- 役割: 全画面でチャット前のとき、タブのアイコンをチャット用に差し替える
- 触るとき: タブアイコンの切り替え条件を変えるとき。
- 呼び出し先: `document.getElementById()`, `this.classList.contains()`
- 参照: `MODE.FULLPAGE`, `link.href`, `this.mode`

## AIWindow.#resetConversationState()
- 位置: L2650-2658
- 役割: chat-active を外し、ホストに会話 ID を記録して履歴を同期する
- 触るとき: 会話を空に戻すときの後始末を変えるとき。
- 呼び出し先: `this.#hostBrowser?.setAttribute()`, `this.#syncHistoryState()`, `this.#updateBrowserTabbable()`, `this.classList.remove()`
- 参照: `this.#conversation.id`

## AIWindow.#setBrowserContainerActiveState()
- 位置: L2660-2679
- 役割: チャット中の表示に切り替え（提案を止め、検索欄を閉じる）、または元に戻す
- 触るとき: チャットに入ったときと戻ったときの表示の差を変えるとき。
- 呼び出し先: `this.#smartbar?.unsuppressStartQuery()`, `this.#updateBrowserTabbable()`, `this.classList.remove()`
- 条件付き依存: `if (isActive)` → `this.classList.add()`
- 条件付き依存: `if (isActive)` → `this.#updateBrowserTabbable()`
- 条件付き依存: `if (isActive)` → `this.#smartbar?.suppressStartQuery()`
- 条件付き依存: `if (isActive)` → `this.#smartbar?.view.close()`
- 参照: `MODE.FULLPAGE`, `this.#smartbar.inputField.showPlaceholderAnimation`, `this.#smartbar?.inputField`, `this.mode`

## AIWindow.#initActiveChatlayout()
- 位置: L2681-2685
- 役割: スターターと下部を隠してチャット中の状態にする
- 触るとき: チャット開始時のレイアウトを変えるとき。
- 呼び出し先: `this.#setBrowserContainerActiveState()`
- 参照: `this.showFooter`, `this.showStarters`

## AIWindow.#fetchAIResponse()
- 位置: async L2721-2851
- 役割: チャット用エンジンを用意し、入力またはアシスタント枠を作って応答を取得し、計測する
- 触るとき: 応答取得の手順、中止の条件、リトライ時の扱いを変えるとき。エラーは handleError に渡す。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation.on()`, `lazy.Chat.fetchWithHistory()`, `lazy.buildEngineForFeature()`, `lazy.openAIEngine.getFxAccountToken()`, `stopWatchingTabClose()`, `this.#abortController?.abort()`, `this.#getBrowsingContext()`, `this.#getModelRequestLatencyAndDuration()`, `this.#sendModelResponseTelemetryEvent()`, `this.#setBrowserContainerActiveState()`, `this.#starterPromptsAbortController?.abort()`, `this.#updateTabFavicon()`, `this.#watchTabCloseForAbort()`, `this.requestUpdate()`
- 条件付き依存: `if (!skipSystemPromptRefresh)` → `conversation.loadSystemPrompt()`
- 条件付き依存: `if (inputText)` → `conversation.generatePrompt()`
- 条件付き依存: `if (inputText)` → `conversation.addAssistantMessage()`
- 条件付き依存: `if (inputText)` → `this.#sendModelRequestTelemetryEvent()`
- 条件付き依存: `if (ensureAssistantResponse)` → `conversation.addAssistantMessage()`
- 条件付き依存: `if (ensureAssistantResponse)` → `this.#sendModelRequestTelemetryEvent()`
- 条件付き依存: `if (!signal.aborted)` → `this.showSearchingIndicator()`
- 条件付き依存: `if (!signal.aborted)` → `this.#handleError()`
- 条件付き依存: `if (!signal.aborted)` → `this.#getModelRequestLatencyAndDuration()`
- 参照: `assistantMessage.toolUIData`, `conversation.engine`, `conversation.parameters`, `lazy.MODEL_FEATURES.CHAT`, `signal.aborted`, `this.#abortController`, `this.#abortController?.signal`, `this.#conversation`, `this.#selectedModelChoiceId`, `this.conversationId`, `this.isGenerating`, `this.mode`, `this.showDisclaimer`, `this.showFooter`, `this.showStarters`

## onUpdate()
- 位置: L2755-2766
- 役割: 最初のアシスタント更新で最初のトークンまでの時間を計測し、購読を外す
- 触るとき: 最初のトークンまでの計測を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation?.off()`
- 参照: `lazy.MESSAGE_ROLE.ASSISTANT`, `message.role`

## AIWindow.#watchTabCloseForAbort()
- 位置: L2864-2877
- 役割: サイドバーで、所属タブが閉じられたら生成を中止するよう監視する
- 触るとき: タブを閉じたときに生成が止まらない問題を見るとき。全画面では何もしない。
- 呼び出し先: `chromeWin?.gBrowser?.getTabForBrowser()`, `tab.addEventListener()`, `tab.removeEventListener()`
- 参照: `MODE.SIDEBAR`, `browsingContext.embedderElement`, `this.mode`, `window.browsingContext?.topChromeWindow`

## onTabClose()
- 位置: L2874-2874
- 役割: タブが閉じられたとき controller を中止する
- 触るとき: タブ閉鎖時の中止の挙動を変えるとき。
- 呼び出し先: `controller.abort()`

## AIWindow.updated()
- 位置: L2879-2895
- 役割: 生成状態の変化をスマートバーと chat content に伝え、モデル一覧の変化で選択を解決し直す
- 触るとき: 生成中表示やモデル一覧更新の後処理を変えるとき。
- 呼び出し先: `changedProps.has()`, `super.updated()`
- 条件付き依存: `if (changedProps.has("isGenerating"))` → `this.#getAIChatContentActor()?.setGeneratingOnChatContent()`
- 条件付き依存: `if (changedProps.has("isGenerating"))` → `this.#getAIChatContentActor()`
- 条件付き依存: `if (changedProps.has("availableModels"))` → `this.#setModelChoice()`
- 条件付き依存: `if (this.#smartbar)` → `this.#updateSmartbarModels()`
- 参照: `this.#selectedModelChoiceId`, `this.#smartbar`, `this.#smartbar.assistantIsGenerating`, `this.isGenerating`

## AIWindow.#onMessageComplete()
- 位置: L2897-2942
- 役割: メッセージ完了時にタイトル生成と再試行 UI の注入を行い、完了を chat content に送って計測する
- 触るとき: メッセージ完了時の後処理や計測を変えるとき。
- 呼び出し先: `lazy.ToolUI.injectRetryToolUIDataIfNeeded()`, `this.#addConversationTitle()`, `this.#conversation?.getHistoryResultsSnapshot()`, `this.#dispatchMessageToChatContent()`
- 条件付き依存: `if (retryInjected)` → `this.#dispatchMessageToChatContent()`
- 条件付き依存: `if (retryInjected)` → `structuredClone()`
- 条件付き依存: `if (followupCount)` → `this.onQuickPromptDisplayed()`
- 条件付き依存: `if (msg?.memoriesApplied?.length)` → `this.onMemoriesApplied()`
- 参照: `msg.toolUIData`, `msg?.citations`, `msg?.content?.body`, `msg?.id`, `msg?.memoriesApplied?.length`, `msg?.tokens?.followup?.length`, `this.#conversation`

## AIWindow.#getModelRequestLatencyAndDuration()
- 位置: L2944-2950
- 役割: 全体の所要時間と最初のトークンまでの時間をミリ秒で返す
- 触るとき: レイテンシの計測の定義を変えるとき。最初のトークンが無ければ latency は 0。
- 呼び出し先: `ChromeUtils.now()`, `Math.round()`

## AIWindow.modelName()
- 位置: L2952-2954
- 役割: 現在のモデル名を返す
- 触るとき: テレメトリや表示でモデル名を使うとき。
- 呼び出し先: `lazy.getCurrentModelName()`

## AIWindow.#getConversationLastMessageAndCount()
- 位置: L2956-2974
- 役割: 指定ロールの最後のメッセージと、その時点までのテキスト数を返す
- 触るとき: message_seq の数え方を変えるとき。先頭のメッセージは数えない。
- 呼び出し先: `this.#conversation.messages.slice()`
- 参照: `message.content?.type`, `message.role`, `this.#conversation`

## AIWindow.#sendModelResponseTelemetryEvent()
- 位置: L2976-3002
- 役割: model_response を、所要時間・遅延・エラー名・HTTP ステータス付きで記録する
- 触るとき: model_response の項目や値の決め方を変えるとき。
- 呼び出し先: `Glean.smartWindow.modelResponse.record()`, `resolveModelResponseError()`, `this.#getConversationLastMessageAndCount()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `lastAssistantMessage?.memoriesApplied?.length`, `lastAssistantMessage?.parentMessageId`, `lazy.Chat.lastUsage?.completion_tokens`, `lazy.MESSAGE_ROLE.ASSISTANT`, `this.conversationId`, `this.mode`, `this.modelName`

## AIWindow.getClientErrorContext()
- 位置: L3011-3021
- 役割: client_error に付ける場所・会話 ID・応答数・モデル名を返す
- 触るとき: クライアント側エラーの報告項目を変えるとき。content 側から中継されたエラーでも使われる。
- 呼び出し先: `this.#getConversationLastMessageAndCount()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `lazy.MESSAGE_ROLE.ASSISTANT`, `this.conversationId`, `this.mode`, `this.modelName`

## AIWindow.#sendModelRequestTelemetryEvent()
- 位置: L3023-3037
- 役割: model_request を、直前のユーザー発言の ID と数付きで記録する
- 触るとき: リクエスト計測の項目や値の決め方を変えるとき。
- 呼び出し先: `Glean.smartWindow.modelRequest.record()`, `this.#getConversationLastMessageAndCount()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `lastUserMessage?.id`, `lastUserMessage?.memoriesApplied?.length`, `lazy.Chat.lastUsage?.completion_tokens`, `lazy.MESSAGE_ROLE.USER`, `this.conversationId`, `this.mode`

## AIWindow.#getBrowsingContext()
- 位置: L3039-3046
- 役割: サイドバーは選択中タブ、全画面は自ウィンドウの browsing context を返す
- 触るとき: ツールがどのページを対象にするかを変えるとき。
- 参照: `MODE.SIDEBAR`, `this.mode`, `window.browsingContext`, `window.browsingContext.topChromeWindow.gBrowser.selectedBrowser .browsingContext`

## AIWindow.#handleError()
- 位置: L3048-3065
- 役割: エラーをログに出し、エラーメッセージを chat content に送って計測する
- 触るとき: 応答エラーの表示内容や計測の扱いを変えるとき。
- 呼び出し先: `console.error()`, `getErrorCode()`, `this.#dispatchMessageToChatContent()`, `this.#sendModelResponseTelemetryEvent()`
- 参照: `error.clientReason`, `error.status`

## AIWindow.#dispatchSeenUrls()
- 位置: L3073-3081
- 役割: 会話の既見 URL を actor に送る。会話 ID が無ければ何もしない
- 触るとき: 既見 URL の同期経路を調べるとき。
- 呼び出し先: `actor.dispatchSeenUrlsToChatContent()`
- 参照: `this.#conversation.id`, `this.#conversation.seenUrls`, `this.#conversation?.id`

## AIWindow.#getAIChatContentActor()
- 位置: L3089-3107
- 役割: aichat browser から AIChatContent actor を取り出す。無ければ null
- 触るとき: chat content へ届かないメッセージの原因を調べるとき。
- 呼び出し先: `lazy.log.error()`, `windowGlobal.getActor()`
- 条件付き依存: `if (!this.#browser)` → `lazy.log.warn()`
- 条件付き依存: `if (!windowGlobal)` → `lazy.log.warn()`
- 参照: `this.#browser`, `this.#browser.browsingContext?.currentWindowGlobal`

## AIWindow.#dispatchMessageToActor()
- 位置: L3116-3150
- 役割: 記憶の吹き出し情報を付け、ツールは操作ログの行に変換して actor に送る
- 触るとき: chat content に渡すメッセージの形を変えるとき。表示対象外のツール結果は送らない。
- 呼び出し先: `actor.dispatchMessageToChatContent()`, `this.#maybeSetMemoriesCalloutData()`
- 条件付き依存: `if (typeof message.role !== "string")` → `lazy.getRoleLabel(newMessage.role).toLowerCase()`
- 条件付き依存: `if (typeof message.role !== "string")` → `lazy.getRoleLabel()`
- 条件付き依存: `if (newMessage.role === "tool")` → `lazy.getActionLogConfigForTool()`
- 条件付き依存: `if (newMessage.role === "tool")` → `lazy.buildActionLogRow()`
- 参照: `cfg.label`, `cfg.link`, `cfg.pendingLabel`, `cfg.show`, `lazy.ACTION_LOG_UI_TYPE`, `message.role`, `newMessage.actionLog`, `newMessage.content?.args`, `newMessage.content?.body`, `newMessage.content?.name`, `newMessage.role`

## AIWindow.#maybeSetMemoriesCalloutData()
- 位置: L3152-3163
- 役割: 記憶が適用された最初の応答に吹き出し表示を付け、見たことを pref に残す
- 触るとき: 記憶の吹き出しを出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- 参照: `lazy.MESSAGE_ROLE.ASSISTANT`, `newMessage.memoriesApplied?.length`, `newMessage.role`, `newMessage.showMemoriesCallout`
- XPCOM: `Services.prefs`

## AIWindow.#dispatchMessageToChatContent()
- 位置: L3165-3168
- 役割: actor を取り出し、あればメッセージを送る
- 触るとき: chat content への送信経路を調べるとき。
- 呼び出し先: `this.#dispatchMessageToActor()`, `this.#getAIChatContentActor()`

## AIWindow.onContentReady()
- 位置: L3174-3189
- 役割: content 側の準備完了時に、保留中の会話を開くか、メッセージと生成状態を送る
- 触るとき: chat content の準備完了後に状態を送り直す挙動を変えるとき。
- 呼び出し先: `this.#getAIChatContentActor()`
- 条件付き依存: `if (this.#pendingRestoreConversation)` → `this.openConversation()`
- 条件付き依存: `if (actor)` → `this.#deliverConversationMessages()`
- 条件付き依存: `if (actor)` → `actor.setGeneratingOnChatContent()`
- 参照: `this.#conversation?.messages?.length`, `this.#pendingMessageDelivery`, `this.#pendingRestoreConversation`, `this.isGenerating`

## AIWindow.#deliverConversationMessages()
- 位置: L3196-3225
- 役割: 既見 URL を送り、保留中なら会話の全メッセージを順に送って復元完了を知らせる
- 触るとき: 会話を復元して表示する順序を変えるとき。
- 呼び出し先: `this.#conversation.renderState()`, `this.#conversation.renderState().forEach()`, `this.#dispatchMessageToActor()`, `this.#dispatchSeenUrls()`, `this.#setBrowserContainerActiveState()`
- 参照: `this.#conversation`, `this.#conversation.id`, `this.#conversation.messages.length`, `this.#pendingMessageDelivery`

## AIWindow.#getEventTab()
- 位置: L3238-3244
- 役割: ホストのタブを返し、無ければ選択中のタブを返す
- 触るとき: タブ単位の状態をどのタブに紐付けるかを変えるとき。
- 呼び出し先: `gBrowser?.getTabForBrowser()`
- 参照: `gBrowser?.selectedTab`, `this.#hostBrowser`, `window?.browsingContext?.topChromeWindow?.gBrowser`

## AIWindow.#getAIWindowEventOptions()
- 位置: L3256-3272
- 役割: 状態イベント用に入力・モード・URL・会話・モデル上書き・タブを詰めて返す
- 触るとき: chrome 側へ送る状態イベントの項目を変えるとき。
- 呼び出し先: `lazy.getCurrentTabUrl()`, `this.#getDataConvId()`, `this.#getEventTab()`
- 参照: `this.#conversation`, `this.#hasModelChoiceOverride`, `this.#selectedModelChoiceId`, `this.mode`

## AIWindow.#swapConversation()
- 位置: L3282-3304
- 役割: 会話の購読を付け替え、記憶状態を同期し、空の会話なら保存済みのスターターを復元して通知する
- 触るとき: 会話を切り替えるときの手順を変えるとき。
- 呼び出し先: `this.#attachConversationListeners()`, `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#kitMention?.reset()`, `this.#removeConversationListeners()`, `this.syncSmartbarMemoriesStateFromConversation()`
- 条件付き依存: `if ( conversation && !conversation.messageCount && conversation.transientStarters?.length )` → `this.#renderStarterPrompts()`
- 参照: `conversation.messageCount`, `conversation.transientStarters`, `conversation.transientStarters?.length`, `this.#conversation`

## AIWindow.openConversation()
- 位置: L3311-3352
- 役割: メッセージのある会話なら表示を切り替えてメッセージを配信し、無ければ新規チャットにする
- 触るとき: 会話を開く・再開するときの表示の流れを変えるとき。
- 呼び出し先: `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`
- 条件付き依存: `if (conversation?.messageCount)` → `this.#swapConversation()`
- 条件付き依存: `if (conversation?.messageCount)` → `this.#syncHistoryState()`
- 条件付き依存: `if (conversation?.messageCount)` → `this.#updateTabFavicon()`
- 条件付き依存: `if (conversation?.messageCount)` → `this.#hostBrowser?.setAttribute()`
- 条件付き依存: `if (this.#smartbar && this.mode === MODE.SIDEBAR)` → `this.#smartbar.updateContextChips()`
- 条件付き依存: `if (conversation?.messageCount)` → `this.#getAIChatContentActor()`
- 条件付き依存: `if (this.#browser && actor)` → `this.#deliverConversationMessages()`
- 条件付き依存: `if (!(conversation?.messageCount))` → `this.clearChat()`
- 参照: `MODE.SIDEBAR`, `conversation?.messageCount`, `document.title`, `this.#browser`, `this.#conversation.id`, `this.#conversation.title`, `this.#pendingMessageDelivery`, `this.#smartbar`, `this.mode`, `this.showDisclaimer`, `this.showFooter`, `this.showStarters`

## AIWindow.#getCurrentTab()
- 位置: L3354-3358
- 役割: 選択中のタブを返す。無ければ null
- 触るとき: スターター読み込み中にタブが切り替わったかを判定する箇所を調べるとき。
- 参照: `window.browsingContext?.topChromeWindow?.gBrowser?.selectedTab`

## AIWindow.onCreateNewChatClick()
- 位置: L3360-3362
- 役割: 新規チャットとして会話を消去する
- 触るとき: 新規チャットボタンの動作を変えるとき。
- 呼び出し先: `this.clearChat()`

## AIWindow.clearChat()
- 位置: L3364-3405
- 役割: 会話を新しいもの（または渡されたもの）に差し替え、記憶トグルと表示を初期化する
- 触るとき: チャットを消去したときの状態リセットを変えるとき。全画面ではチャット表示を保つ。
- 呼び出し先: `hostBrowser?.setAttribute()`, `this.#dispatchChromeEvent()`, `this.#dispatchMessageToChatContent()`, `this.#getAIWindowEventOptions()`, `this.#smartbar?.unsuppressStartQuery()`, `this.#swapConversation()`, `this.#syncHistoryState()`, `this.#syncMemoriesButtonUI()`
- 条件付き依存: `if (this.mode !== MODE.FULLPAGE)` → `this.#setBrowserContainerActiveState()`
- 参照: `MODE.FULLPAGE`, `lazy.ChatConversation`, `this.#conversation`, `this.#conversation.id`, `this.#conversation.transientStarters?.length`, `this.#memoriesToggled`, `this.mode`, `this.showStarters`, `window.browsingContext?.embedderElement`

## AIWindow.#onCloseSidebarClick()
- 位置: L3407-3409
- 役割: サイドバーを閉じるイベントを chrome に送る
- 触るとき: 閉じるボタンの動作を変えるとき。
- 呼び出し先: `this.#dispatchChromeEvent()`

## AIWindow.#refreshRecentChats()
- 位置: async L3412-3426
- 役割: 最近の会話を取得して履歴メニュー用に保持する。失敗時は空にする
- 触るとき: 履歴メニューの件数や内容を変えるとき。
- 呼び出し先: `items.map()`, `lazy.AIWindow.chatStore.findRecentConversations()`, `lazy.log.error()`
- 参照: `item.id`, `item.pageUrl`, `item.title`, `this.recentChats`

## AIWindow.#onRecentChatSelected()
- 位置: async L3433-3462
- 役割: 最近の会話を選ぶと、開いているタブへ移るか、無ければタブとして開き直す
- 触るとき: 履歴からの会話の再開動作を変えるとき。
- 呼び出し先: `Array.from()`, `Array.from(win.gBrowser.tabs).find()`, `browser?.getAttribute()`, `lazy.AIWindow.chatStore.findConversationById()`, `lazy.AIWindow.isAIWindowContentPage()`, `lazy.AIWindowUI.reopenConversationInTab()`
- 条件付き依存: `if (!win)` → `this.openConversation()`
- 参照: `browser.currentURI`, `tab.linkedBrowser`, `this.#topChromeWindow`, `win.gBrowser.selectedTab`, `win.gBrowser.tabs`

## AIWindow.#onViewAllChatsSelected()
- 位置: L3465-3467
- 役割: Firefox View の chats を開く
- 触るとき: すべてのチャットを見る導線を変えるとき。
- 呼び出し先: `this.#topChromeWindow?.FirefoxViewHandler.openTab()`

## AIWindow.#onSmartWindowSettingsSelected()
- 位置: L3470-3472
- 役割: Smart Window の個人設定を開く
- 触るとき: 設定画面への導線を変えるとき。
- 呼び出し先: `this.#topChromeWindow?.openPreferences()`

## AIWindow.#onHistoryMenuEvent()
- 位置: L3475-3493
- 役割: 履歴メニューの各イベントを対応する処理に振り分ける
- 触るとき: 履歴メニューの項目を追加・変更するとき。
- 呼び出し先: `this.#onRecentChatSelected()`, `this.#onSmartWindowSettingsSelected()`, `this.#onViewAllChatsSelected()`, `this.#refreshRecentChats()`, `this.onCreateNewChatClick()`
- 参照: `event.detail.conversationId`, `event.type`

## AIWindow.#onPanelShowing()
- 位置: L3499-3508
- 役割: 新しい popover の panel-list を開くとき、直前の panel を閉じる
- 触るとき: ポップオーバーが重なったり残ったりする問題を調べるとき。
- 呼び出し先: `event.composedPath()`, `panel.hasAttribute()`
- 条件付き依存: `if (panel !== this.#openPanel && this.#openPanel?.open)` → `this.#openPanel.hide()`
- 参照: `panel?.localName`, `this.#openPanel`, `this.#openPanel?.open`

## AIWindow.#historyMenu()
- 位置: L3511-3516
- 役割: モードに応じた履歴メニューの要素を描画する
- 触るとき: 履歴メニューに渡す値を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.recentChats`

## AIWindow.showSearchingIndicator()
- 位置: L3518-3526
- 役割: 検索中の表示を chat content に送る
- 触るとき: 検索中インジケータの表示条件を変えるとき。
- 呼び出し先: `this.#dispatchMessageToChatContent()`
- 参照: `this.conversationId`

## AIWindow.reloadAndContinue()
- 位置: async L3528-3534
- 役割: 会話を開き直し、ツール結果の続きを実行する
- 触るとき: ツール結果を受けて応答を続けさせる経路を調べるとき。
- 呼び出し先: `this.#continueAfterToolResult()`, `this.openConversation()`

## AIWindow.#continueAfterToolResult()
- 位置: async L3536-3563
- 役割: 最後のツールが検索なら検索中表示を出し、会話を開いた通知を送ってから応答を取得する
- 触るとき: ツール実行の後に応答を続ける流れや表示を変えるとき。
- 呼び出し先: `this.#conversation.messages .filter()`, `this.#dispatchChromeEvent()`, `this.#fetchAIResponse()`, `this.#getAIWindowEventOptions()`
- 条件付き依存: `if (lastToolName === "search_the_web")` → `JSON.parse()`
- 条件付き依存: `if (query)` → `this.showSearchingIndicator()`
- 参照: `lastToolCall.content.body.tool_calls`, `lastToolCall.content.body.tool_calls[0].function.arguments`, `lastToolCall?.content?.body?.tool_calls`, `lastToolCall?.content?.body?.tool_calls?.[0]?.function?.name`, `lazy.MESSAGE_ROLE.ASSISTANT`, `m.role`, `m?.content?.type`

## AIWindow.handleFooterAction()
- 位置: L3565-3613
- 役割: フッターの操作（再試行、記憶の削除、フィードバック等）を対応する処理と計測へ振り分ける
- 触るとき: フッターに操作を足すとき、その計測項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.retryNoMemories.record()`, `this.#openFeedbackModal()`, `this.#openMemoriesLearnMore()`, `this.#openMemoriesSettings()`, `this.#removeAppliedMemory()`, `this.#retryAfterError()`, `this.#retryFromAssistantMessageId()`
- 条件付き依存: `if (data.open)` → `Glean.smartWindow.memoryAppliedClick.record()`
- 参照: `data.open`, `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.handleToolUIUpdate()
- 位置: async L3615-3642
- 役割: ツール UI の更新をエージェントか ToolUI に渡し、再試行の依頼なら同じ文を送り直す
- 触るとき: ツール UI のボタン操作の結果を変えるとき。
- 呼び出し先: `lazy.AgentUI.isAgentUpdate()`, `lazy.ToolUI.handleUpdate()`
- 条件付き依存: `if (lazy.AgentUI.isAgentUpdate(data))` → `lazy.AgentUI.handleUpdate()`
- 条件付き依存: `if (retryPrompt)` → `this.submitChatMessage()`
- 参照: `data?.updateData?.prompt`, `data?.updateType`, `lazy.UI_UPDATE_TYPES.RETRY_PROMPT`, `this.#conversation`, `this.#topChromeWindow`, `this.mode`

## AIWindow.#buildChatLogPayload()
- 位置: L3644-3673
- 役割: ページ内容の取得を除いた版と含む版の会話ログを作る
- 触るとき: フィードバック送信に含めるログの範囲を変えるとき。
- 呼び出し先: `messages.filter()`
- 条件付き依存: `if (msg.content?.body?.tool_calls?.length)` → `msg.content.body.tool_calls.filter()`
- 参照: `lazy.GET_PAGE_CONTENT`, `lazy.MESSAGE_ROLE.TOOL`, `messages.length`, `msg.content?.body?.tool_calls?.length`, `msg.content?.name`, `msg.role`, `remaining.length`, `tc.function?.name`, `this.#conversation?.messages`, `withoutPageContent.length`

## AIWindow.applyHistoryAssets()
- 位置: L3683-3689
- 役割: 履歴グリッドで解決したサムネイルやファビコンを、同じ会話の時だけ反映する
- 触るとき: 履歴グリッドの画像キャッシュの扱いを変えるとき。
- 呼び出し先: `this.#conversation?.applyHistoryAssets()`
- 参照: `this.conversationId`

## AIWindow.#openFeedbackModal()
- 位置: L3691-3709
- 役割: フィードバック画面を、モデル名・ターン数・プロンプト版付きで開く
- 触るとき: フィードバック画面に渡す情報を変えるとき。
- 呼び出し先: `lazy.FeedbackModal.open()`, `this.#buildChatLogPayload()`
- 参照: `this.#conversation?.messageCount`, `this.#conversation?.systemPromptVersion`, `this.#topChromeWindow?.gBrowser?.selectedBrowser`, `this.modelName`

## AIWindow.#openMemoriesSettings()
- 位置: L3711-3713
- 役割: 記憶の管理画面を開く
- 触るとき: 記憶設定への導線を変えるとき。
- 呼び出し先: `this.#topChromeWindow?.openPreferences()`

## AIWindow.#openMemoriesLearnMore()
- 位置: L3715-3717
- 役割: 記憶のヘルプページを開く
- 触るとき: 記憶のヘルプリンクを変えるとき。
- 呼び出し先: `this.#topChromeWindow?.openHelpLink()`

## AIWindow.#getMessageById()
- 位置: L3719-3721
- 役割: 会話内のメッセージを ID で探し、無ければ null を返す
- 触るとき: メッセージの参照方法を変えるとき。
- 呼び出し先: `this.#conversation.messages.find()`
- 参照: `m.id`

## AIWindow.#getUserMessageForAssistantId()
- 位置: L3723-3730
- 役割: アシスタント応答の親にあたるユーザー発言を返す
- 触るとき: 再試行で元の質問を取り出す箇所を調べるとき。
- 呼び出し先: `this.#getMessageById()`
- 参照: `assistantMsg.parentMessageId`, `assistantMsg?.parentMessageId`

## AIWindow.#retryAfterError()
- 位置: L3732-3746
- 役割: エラー後の再試行を、再試行中でなければ応答取得し直す
- 触るとき: エラー後の再試行の挙動や二重実行の防止を変えるとき。
- 呼び出し先: `console.error()`, `this.#fetchAIResponse()`, `this.#fetchAIResponse("", { isRetry: true }) .catch()`
- 条件付き依存: `if (this._isRetrying)` → `console.warn()`
- 参照: `this._isRetrying`

## AIWindow.#retryFromAssistantMessageId()
- 位置: async L3748-3795
- 役割: 指定の応答を切り詰めて以降を削除し、元の発言で応答を取り直す
- 触るとき: 再試行（記憶あり・なし）の削除と再生成の手順を変えるとき。
- 呼び出し先: `ChromeUtils.now()`, `actor?.dispatchTruncateToChatContent()`, `lazy.AIWindow.chatStore.deleteMessages()`, `this.#conversation.retryMessage()`, `this.#fetchAIResponse()`, `this.#getAIChatContentActor()`, `this.#getModelRequestLatencyAndDuration()`, `this.#getUserMessageForAssistantId()`, `this.#handleError()`, `this.#updateConversation()`
- 条件付き依存: `if (this._isRetrying)` → `console.warn()`
- 参照: `e.clientReason`, `this.#memoriesIconShown`, `this.#memoriesToggled`, `this._isRetrying`, `userMsg.content.body`, `userMsg.content.contextMentions`, `userMsg.pageUrl`

## AIWindow.#removeAppliedMemory()
- 位置: async L3797-3826
- 役割: 適用された記憶をハード削除し、メッセージと chat content から外す
- 触るとき: 適用済みの記憶の削除の挙動を変えるとき。
- 呼び出し先: `actor?.dispatchRemoveAppliedMemoryToChatContent()`, `console.error()`, `lazy.MemoriesManager.hardDeleteMemoryById()`, `msg?.memoriesApplied.filter()`, `this.#getAIChatContentActor()`, `this.#getMessageById()`
- 条件付き依存: `if (!deleted)` → `console.warn()`
- 参照: `m.id`, `memory.id`, `msg.memoriesApplied`, `remaining?.length`

## AIWindow.#footerTemplate()
- 位置: L3828-3833
- 役割: 表示フラグが立っているときだけフッターを描画する
- 触るとき: フッターの表示条件を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.showFooter`

## AIWindow.#promoTemplate()
- 位置: L3835-3842
- 役割: プロモーションメッセージがあれば描画する
- 触るとき: プロモーション表示の条件を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.promoMessage`

## AIWindow.render()
- 位置: L3844-3954
- 役割: モードごとにヘッダー・会話領域・スマートバー・提案・トップサイト・再開カード・免責を組み立てる
- 触るとき: スマートウィンドウ全体のレイアウトや要素の出し分けを変えるとき。サイドバーと全画面で構成が違う。
- 呼び出し先: `html()`, `this.#footerTemplate()`, `this.#historyMenu()`, `this.#promoTemplate()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `this .#handlePromptDismissed`, `this .#handlePromptSelected`, `this .#handleResumeCardMenuItemSelected`, `this .#handleResumeCardResume`, `this .#handleResumeSectionHide`, `this .#handleTopSiteSelected`, `this.#onCloseSidebarClick`, `this.#starters`, `this.isGenerating`, `this.mode`, `this.onCreateNewChatClick`, `this.resumeCards`, `this.resumeCards.length`, `this.resumeCardsEmptyReason`, `this.resumeCardsLoading`, `this.resumeCardsPref`, `this.resumeSectionHidden`, `this.showDisclaimer`, `this.showStarters`, `this.startersResolved`, `this.topSites`
