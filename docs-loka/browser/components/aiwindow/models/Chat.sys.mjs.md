# browser/components/aiwindow/models/Chat.sys.mjs

source: browser/components/aiwindow/models/Chat.sys.mjs
source-hash: 31ba4ca3eda2888e56fa6e93c0d2ef8a9ea24bec
lines: 855

## <module>
- 役割: AI ウィンドウのチャット本体で、モデルの応答ストリームを受け取りツール呼び出しを実行しながら会話を進める Chat オブジェクトを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.assign()`, `console.createInstance()`

## executeToolByName()
- 位置: async L48-132
- 役割: ツール名で switch し、対応する toolFns やページ内容取得・検索の関数を呼んで結果を返す。未知の名前は unknownTool エラーにする。
- 触るとき: 新しいツールを追加して実行経路に繋ぐとき、またはツール実行時の Glean 記録(ページ取得・検索引き渡し)を変えるとき。
- 呼び出し先: `GetPageContent.getPageContentText()`, `Glean.smartWindow.getPageContent.record()`, `Glean.smartWindow.searchHandoff.record()`, `RunSearch.runSearch()`, `lazy.SearchService.getDefault()`, `result.reduce()`, `toolFns.addMemory()`, `toolFns.getNavigationInfo()`, `toolFns.getOpenTabs()`, `toolFns.getSkill()`, `toolFns.getUserMemories()`, `toolFns.manageTabs()`, `toolFns.searchBrowsingHistory()`
- 条件付き依存: `if (uiData)` → `conversation.addUIToolToCurrentMessage()`
- 参照: `conversation.engine?.model`, `conversation.id`, `conversation.messageCount`, `curr?.length`, `engine.name`, `err.clientReason`

## runGenerateAiTab()
- 位置: async L190-216
- 役割: AITab 生成ツールの入口で、UI カードを creating 状態にしてから toolFns.createAITab を呼び、完了時に UI データを更新する。
- 触るとき: AITab 生成の進行表示が更新されない、または生成失敗時の UI 後始末を直したいとき。
- 呼び出し先: `toolFns.createAITab()`
- 条件付き依存: `if (toolCallId)` → `conversation.addUIToolToCurrentMessage()`
- 条件付き依存: `if (toolCallId && uiData)` → `conversation.addUIToolToCurrentMessage()`
- 参照: `UI_TYPES.AITAB`

## splitDirectAnswerStream()
- 位置: L240-248
- 役割: ツール結果が directAnswerStream(非同期イテラブル)を持つときだけ取り出し、残りを toolBody として分離する。
- 触るとき: search_the_web の直接回答を会話履歴に入れずにストリーム表示したいとき、またはツール結果の形を変えるとき。
- 参照: `Symbol.asyncIterator`, `result?.directAnswerStream`

## filterFeatureGatedTools()
- 位置: L263-279
- 役割: AITab 系ツールの pref が off なら除外し、search_the_web の設定を経路に合うものへ差し替えて返す(元の配列は変更しない)。
- 触るとき: モデルに提示するツール一覧を機能フラグで出し分けたいとき、または search_the_web の説明文と実行経路がずれるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `searchTheWebToolConfig()`
- 条件付き依存: `if (searchTheWebConfig)` → `filtered.map()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(AITAB_PREF, false))` → `filtered.filter()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(AITAB_PREF, false))` → `AITAB_TOOLS.has()`
- 参照: `t.function?.name`
- XPCOM: `Services.prefs`

## recordToolCallEvent()
- 位置: L322-332
- 役割: ツール呼び出しごとに smart_window.tool_call の Glean イベントを、場所・会話 ID・ツール名・モデル・プロンプト版・エラー種別つきで記録する。
- 触るとき: ツール呼び出しのテレメトリ項目を増やす、またはエラー分類の値を追加するとき。
- 呼び出し先: `Glean.smartWindow.toolCall.record()`
- 参照: `conversation.engine?.model`, `conversation.id`, `conversation.messageCount`, `conversation.systemPromptVersion`

## classifyStreamingError()
- 位置: L355-367
- 役割: clientReason などの分類情報がないストリームエラーに、オフラインか接続失敗かの clientReason を付ける。
- 触るとき: ストリーム失敗時にユーザーへ出すエラー種別が想定と違うとき。
- 参照: `Services.io.offline`, `err.clientReason`, `err.error`, `err.metadata?.errorMessage`
- XPCOM: `Services.io`

## logConversationStream()
- 位置: L369-389
- 役割: chat のストリーム進行を [Chat][Turn n][action] の形式で debug ログに出し、失敗しても例外を外へ出さない。
- 触るとき: ストリームの送受信やツール実行のログを追加・調整するとき、またはログの書式を揃えるとき。
- 呼び出し先: `action.padEnd()`, `lazy.console.error()`
- 条件付き依存: `if (data)` → `lazy.console.debug()`
- 条件付き依存: `if (!(data))` → `lazy.console.debug()`

## fetchWithHistory()
- 位置: async L410-853
- 役割: fxA トークンと browsingContext を確認した後、モデル応答をループで受けてツール呼び出しを実行し、ツールが無くなるまで続ける。重複検索・記憶無効・AITab 完了・直接回答・検索引き渡しの各分岐も扱う。
- 触るとき: チャットの応答生成フロー全体(ツールの繰り返し、検索の重複防止、記憶の無効化、中断処理)を変えるとき、または応答が途中で止まる原因を追うとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `FEATURE_GATED_HANDLERS.get()`, `JSON.parse()`, `String()`, `TOOLS_WITH_PENDING_ACTION_LOG.has()`, `classifyStreamingError()`, `console.error()`, `conversation.addAssistantMessage()`, `conversation.addToolCallMessage()`, `conversation.currentTurnIndex()`, `conversation.receiveResponse()`, `conversation.updateToolCallMessage()`, `expandUrlTokensInToolParams()`, `filterFeatureGatedTools()`, `lazy.AIWindow.chatStore ?.updateConversation()`, `lazy.AIWindow.chatStore ?.updateConversation(conversation) .catch()`, `lazy.AIWindow.chatStore?.updateConversation()`, `lazy.AIWindow.chatStore?.updateConversation(conversation).catch()`, `logConversationStream()`, `openAIEngine.getFxAccountToken()`, `recordToolCallEvent()`, `splitDirectAnswerStream()`, `streamModelResponse()`, `structuredClone()`
- 条件付き依存: `if (!fxAccountToken)` → `console.error()`
- 条件付き依存: `if (!pendingToolCalls || pendingToolCalls.length === 0)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!pendingToolCalls || pendingToolCalls.length === 0)` → `logConversationStream()`
- 条件付き依存: `if (!conversation.engine?.isCustomEndpoint)` → `runLLMaJTelemetry()`
- 条件付き依存: `if (signal?.aborted)` → `logConversationStream()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `pendingToolCalls.slice()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `conversation.addAssistantMessage()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `conversation.addToolCallMessage()`
- 条件付き依存: `if (firstPending?.name === SEARCH_THE_WEB && searchExecuted)` → `recordToolCallEvent()`
- 条件付き依存: `if (firstPending?.name === GET_USER_MEMORIES)` → `conversation.messages.findLast()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `pendingToolCalls.slice()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `conversation.addAssistantMessage()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `conversation.addToolCallMessage()`
- 条件付き依存: `if (lastUserMessage.memoriesEnabled === false)` → `recordToolCallEvent()`
- 条件付き依存: `if (TOOLS_WITH_PENDING_ACTION_LOG.has(toolName))` → `conversation.addToolCallMessage()`
- 条件付き依存: `if (featureGatedHandler)` → `featureGatedHandler()`
- 条件付き依存: `if (result.requiresSearchHandoff)` → `dispatchTool()`
- 条件付き依存: `if (!(featureGatedHandler))` → `dispatchTool()`
- 条件付き依存: `if (toolName === GENERATE_AITAB && !aiTabSucceeded)` → `conversation.messages.findLast()`
- 条件付き依存: `if (message)` → `conversation.updateToolUI()`
- 条件付き依存: `if (toolName === MANAGE_TABS || aiTabSucceeded)` → `conversation.securityProperties.commit()`
- 条件付き依存: `if (directAnswerStream)` → `conversation.receiveResponse()`
- 条件付き依存: `if (directAnswerStream)` → `logConversationStream()`
- 条件付き依存: `if (!win || win.closed)` → `console.error()`
- 条件付き依存: `if (isSearchHandoff)` → `lazy.AIWindow.openSidebarAndContinue()`
- 参照: `Cu.isInAutomation`, `MESSAGE_ROLE.USER`, `browsingContext?.embedderElement`, `content.name`, `conversation._searchExecutedTurn`, `conversation.engine?.isCustomEndpoint`, `conversation.tokenToUrl`, `err.clientReason`, `firstPending?.name`, `functionSpec.arguments`, `functionSpec?.arguments`, `functionSpec?.name`, `fxaError.clientReason`, `lastToolCall.function`, `lastToolCall.function.arguments`, `lastUserMessage.memoriesEnabled`, `m.role`, `m.toolUIData?.toolCallId`, `originalEmbedderElement?.documentGlobal`, `pendingToolCalls.length`, `pendingToolCalls[0]?.function`, `response.fullResponseText`, `response.pendingToolCalls`, `response.usage`, `result.requiresSearchHandoff`, `result.success`, `result.toolResult`, `result?.error`, `signal?.aborted`, `split.directAnswerStream`, `split.toolBody`, `tc.function.arguments`, `tc.function.name`, `tc.id`, `this.lastUsage`, `toolParams.query`, `win.closed`

## streamModelResponse()
- 位置: L451-477
- 役割: 会話のスナップショットを作り、ツール一覧と tool_choice auto を付けて runWithGenerator のストリームを返す(実際の送信はイテレーション時)。
- 触るとき: モデルへ送るリクエストの形(ツール一覧や推論パラメータ)を変えるとき。
- 呼び出し先: `conversation.compactChatCompletions()`, `conversation.runWithGenerator()`, `conversation.securityProperties.getLogText()`, `lazy.console.log()`, `logConversationStream()`, `snapshot.at()`
- 参照: `conversation.id`

## dispatchTool()
- 位置: L686-694
- 役割: 現在のツール呼び出しの引数を使って executeToolByName を呼ぶ、fetchWithHistory 内の閉包。feature gated ハンドラーからの RUN_SEARCH 再実行にも使われる。
- 触るとき: ツール実行時に渡す引数や文脈を変えたいとき、または検索引き渡し後にどのツールが呼ばれるか追うとき。
- 呼び出し先: `executeToolByName()`
