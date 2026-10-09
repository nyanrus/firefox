# browser/components/aiwindow/ui/modules/ChatConversation.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatConversation.sys.mjs
source-hash: 266e22cdd9950903415360f510834bbda2d8602e
lines: 1330

## <module>
- 役割: チャット会話の中核クラス。メッセージ管理、URL トークン、履歴・引用プール、記憶と実時間情報の注入、UI 向けイベントを担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## _setLoadPromptForTesting()
- 位置: L88-105
- 役割: テスト用に lazy.loadPrompt を差し替え、null で元の定義に戻す。
- 触るとき: テストでシステムプロンプトの内容やバージョンを固定したいとき。テスト後に null で戻さないと後続テストに影響する。
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedLoadPromptDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.loadPrompt`

## lazy.loadPrompt()
- 位置: async L94-99
- 役割: 差し替え後の loadPrompt。文字列の戻り値を {prompt, version} に揃える。
- 触るとき: テストのモックが文字列を返すケースで、呼び出し側が同じ形を受け取れるかを確認するとき。
- 呼び出し先: `fn()`

## ChatConversation.constructor()
- 位置: L207-265
- 役割: Conversation を初期化し、URL トークナイザーと履歴・引用プールを DB 上のメッセージから復元する。
- 触るとき: 会話を DB から読み込んだときにどの状態が復元されるかを確認・変えるとき。transient なフィールドの初期値を足すときもここ。
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`, `super()`, `this.rehydrateCitationsPool()`, `this.rehydrateHistoryResultsPool()`
- 条件付き依存: `if (messages.length)` → `this.#updateActiveBranchTipMessageId()`
- 参照: `CONVERSATION_STATUS.ACTIVE`, `messages.length`, `params.status`, `this.description`, `this.memoriesToggled`, `this.pageMeta`, `this.pageUrl`, `this.pendingRetry`, `this.status`, `this.title`, `this.transientStarterUrl`, `this.transientStarters`, `this.urlTokenizer`

## ChatConversation.on()
- 位置: L267-269
- 役割: 内部 EventEmitter に購読を登録する。
- 触るとき: chat-conversation:message-update などのイベントを購読する側の挙動を調べるとき。
- 呼び出し先: `this.#emitter.on()`

## ChatConversation.off()
- 位置: L270-272
- 役割: 内部 EventEmitter の購読を解除する。
- 触るとき: UI の破棄時にリスナーが残って二重に呼ばれる問題を調べるとき。
- 呼び出し先: `this.#emitter.off()`

## ChatConversation.emit()
- 位置: L273-275
- 役割: 内部 EventEmitter でイベントを発火する。
- 触るとき: 会話の状態変化を UI へ通知するイベント名や引数を変えるとき。
- 呼び出し先: `this.#emitter.emit()`

## ChatConversation.stashPendingBrowserActionTelemetry()
- 位置: L284-286
- 役割: 確認待ちのタブ操作の browser_action_submit テレメトリ情報を toolCallId 単位で保存する。
- 触るとき: manage_tabs の確認を待つ間にテレメトリ情報が失われる、または別の呼び出しと混ざる問題を調べるとき。
- 呼び出し先: `this.#pendingBrowserActionTelemetry.set()`

## ChatConversation.takePendingBrowserActionTelemetry()
- 位置: L295-299
- 役割: toolCallId に対応する保存済みテレメトリ情報を取り出し、Map から削除する。
- 触るとき: 確認結果が返った後にテレメトリが二重送信・欠落しないか確認するとき。
- 呼び出し先: `this.#pendingBrowserActionTelemetry.delete()`, `this.#pendingBrowserActionTelemetry.get()`

## ChatConversation.pendingBrowserActionTelemetryCount()
- 位置: L307-309
- 役割: 保留中のテレメトリ情報の件数を返す（テスト用）。
- 触るとき: テストで保留情報が後始末されているかを検証するとき。
- 参照: `this.#pendingBrowserActionTelemetry.size`

## ChatConversation.convertUrlToToken()
- 位置: L324-326
- 役割: URL を UrlTokenizer でトークン文字列に変換する。
- 触るとき: LLM に渡す URL のトークン化の仕様を変えるとき、またはトークンが付与されない原因を調べるとき。
- 呼び出し先: `this.urlTokenizer.encodeToken()`

## ChatConversation.handleChunk()
- 位置: L333-351
- 役割: ストリームの 1 チャンクを解析し、本文とトークンを現在のアシスタントメッセージに反映して通知・保存する。
- 触るとき: ストリーミング中の表示更新や、トークン由来の URL 展開が途中で崩れる問題を調べるとき。
- 呼び出し先: `consumeStreamChunk()`
- 条件付き依存: `if (tokens)` → `currentMessage?.addTokens()`
- 条件付き依存: `if (plainText || tokens)` → `this.emit()`
- 条件付き依存: `if (plainText || tokens)` → `lazy.ChatStore.persistStreamingMessage()`
- 参照: `currentMessage.content.body`, `currentMessage?.content`, `this.urlTokenizer.tokenToUrl`

## ChatConversation.receiveResponse()
- 位置: async L356-445
- 役割: 応答ストリームを処理し、履歴・引用のスナップショット付与、未解決 URL トークンの除去、記憶の確定、保存、完了通知を行う。
- 触るとき: 1 ターンの後処理（完了イベントの発火時期や記憶の適用）を変えるとき。ストリームが中断された時に何が保存されるかを調べるときも。
- 呼び出し先: `lazy.ChatStore.endStreamingWrites()`, `lazy.ChatStore.updateConversation()`, `super.receiveResponse()`, `this.#getCurrentAssistantResponse()`
- 条件付き依存: `if (this.#historyResultsPool.size)` → `this.getHistoryResultsSnapshot()`
- 条件付き依存: `if (this.#pendingCitationUrls.size)` → `this.getCitationsSnapshot()`
- 条件付き依存: `if (this.urlTokenizer.urlToToken.size)` → `stripUnresolvedUrlTokens()`
- 条件付き依存: `if (result.currentMessage?.content?.body)` → `this.emit()`
- 条件付き依存: `if (!result.pendingToolCalls?.length)` → `this.promptEmbeddedMemories.map()`
- 条件付き依存: `if (!result.pendingToolCalls?.length)` → `lazy.MemoriesManager.resolveUsedMemories()`
- 条件付き依存: `if (memoriesApplied.length)` → `this.emit()`
- 条件付き依存: `if (!result.pendingToolCalls?.length)` → `this.emit()`
- 参照: `currentMessage.citations`, `currentMessage.content.body`, `currentMessage.content?.body`, `currentMessage.historyResults`, `currentMessage.memoriesApplied`, `currentMessage.tokens?.existing_memory`, `memoriesApplied.length`, `memory.id`, `memoryIds.length`, `result.currentMessage.content.body`, `result.currentMessage?.content?.body`, `result.fullResponseText`, `result.pendingToolCalls`, `result.pendingToolCalls?.length`, `result.usage`, `this.#historyResultsPool.size`, `this.#pendingCitationUrls.size`, `this.id`, `this.promptEmbeddedMemories`, `this.urlTokenizer.urlToToken.size`

## ChatConversation.#getCurrentAssistantResponse()
- 位置: L447-455
- 役割: テキスト型のアシスタントメッセージのうち最後のものを返す。
- 触るとき: ストリーム中の応答を書き込む対象がずれていないか確認するとき。対象はテキスト型に限られる点に注意。
- 呼び出し先: `this.messages .filter()`, `this.messages .filter( message => message.role === MESSAGE_ROLE.ASSISTANT && message?.content?.type === "text" ) .at()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `message.role`, `message?.content?.type`

## ChatConversation.renderState()
- 位置: L463-479
- 役割: チャット画面に描画するメッセージだけを絞り込んで返す。
- 触るとき: 画面に出す・出さないの条件（function 型、空の text 型、l10nId 付きなど）を変えるとき。
- 呼び出し先: `RESTORABLE_ROLES.includes()`, `this.messages.filter()`
- 参照: `content?.l10nId`, `message.toolUIData`

## ChatConversation._createMessage()
- 位置: L481-483
- 役割: 会話 ID を付けて ChatMessage を生成する。
- 触るとき: 新しいメッセージを作る経路で会話 ID が正しく入っているか確認するとき。
- 参照: `this.id`

## ChatConversation.addUserMessage()
- 位置: L497-528
- 役割: ユーザーメッセージを新しいターンとして追加し、引用とページ URL を付与する。直前の引用と取り消し表示もリセットする。
- 触るとき: 送信時のターン番号の扱いや、コンテキストメンションの保存形式を変えるとき。
- 呼び出し先: `this.#dismissPendingUndos()`, `this.#pendingCitationUrls.clear()`, `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.USER`, `content.contextMentions`, `content.contextPageUrl`, `pageUrl.href`, `this.messages.length`, `userOpts.contextMentions`, `userOpts.contextMentions?.length`

## ChatConversation.resolvePendingToolConfirmation()
- 位置: L538-556
- 役割: 末尾の確認待ちツールメッセージを確定結果の本文で置き換えて保存する。
- 触るとき: 確認 UI の承認・キャンセル後も確認待ちの表示が残る問題を調べるとき。
- 呼び出し先: `lazy.ChatStore.updateConversation()`, `lazy.ChatStore.updateConversation(this).catch()`, `lazy.console.error()`, `this.emit()`, `this.messages.at()`
- 参照: `MESSAGE_ROLE.TOOL`, `message.content`, `message.content?.body?.pending`, `message.content?.tool_call_id`, `message?.role`

## ChatConversation.#dismissPendingUndos()
- 位置: L570-594
- 役割: 直前の ai-action-result のうち未消化の取り消し操作を undoDismissed にする。
- 触るとき: 新しいユーザー発言で取り消しボタンが消える条件を変えるとき。
- 呼び出し先: `this.emit()`
- 参照: `confirmedData?.operationIds?.length`, `m.toolUIData`, `td.properties`, `td.properties?.confirmedData`, `td.properties?.undoDismissed`, `td.uiType`, `this.messages`, `this.messages.length`

## ChatConversation.addAssistantMessage()
- 位置: L604-623
- 役割: 現在のターンにテキストまたは関数型のアシスタントメッセージを追加し、モデル ID を補う。
- 触るとき: アシスタント側メッセージの型や、どのモデルの応答かの記録を調べるとき。
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `assistantOpts.modelId`, `this.engine?.model`

## ChatConversation.addAssistantWithL10nMessage()
- 位置: L636-658
- 役割: Fluent の l10nId で描画するアシスタントメッセージを追加し、更新と完了を通知する。
- 触るとき: 定型の案内文（リンク付きを含む）を追加するとき、または表示が更新されない問題を調べるとき。
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 条件付き依存: `if (message)` → `this.emit()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `assistantOpts.modelId`, `this.engine?.model`

## ChatConversation.addToolCallMessage()
- 位置: L667-683
- 役割: ツール呼び出しのメッセージを追加し、行動ログ表示のために更新を通知する。
- 触るとき: ツール実行の行動ログに表示が出ない・重複する問題を調べるとき。この関数は保存しない点に注意。
- 呼び出し先: `this.addMessage()`, `this.currentTurnIndex()`
- 条件付き依存: `if (message)` → `this.emit()`
- 参照: `MESSAGE_ROLE.TOOL`, `this.engine?.model`, `toolOpts.modelId`

## ChatConversation.updateToolCallMessage()
- 位置: L701-708
- 役割: 既存のツールメッセージの content を差し替えて再通知し、無ければ新規に追加する。
- 触るとき: 実行中の仮行を完了結果で置き換える処理（遅いツールの表示）を変えるとき。
- 呼び出し先: `this.emit()`
- 条件付き依存: `if (!message)` → `this.addToolCallMessage()`
- 参照: `message.content`

## ChatConversation.loadSystemPrompt()
- 位置: async L718-729
- 役割: chat 用システムプロンプトを読み込み、先頭のシステムメッセージを上書きする。
- 触るとき: モデルごとのプロンプトが切り替わらない、または古いままになる問題を調べるとき。
- 呼び出し先: `lazy.loadPrompt()`, `this.setSystemMessage()`
- 参照: `MODEL_FEATURES.CHAT`, `SYSTEM_PROMPT_TYPE.TEXT`, `opts.model`, `this.engine?.model`

## ChatConversation.generatePrompt()
- 位置: async L746-788
- 役割: ユーザー発言を追加し、リアルタイム情報と記憶の文脈を注入してからセキュリティ状態を確定する。
- 触るとき: 送信時に実時間情報や記憶が LLM への入力に入らない問題を調べるとき。注入の順序を変えるなら commit の位置も確認する。
- 呼び出し先: `this.addUserMessage()`, `this.injectRealTimeContext()`, `this.securityProperties.commit()`
- 条件付き依存: `if (!this.messages.length)` → `this.loadSystemPrompt()`
- 条件付き依存: `if (!skipUserDispatch)` → `this.emit()`
- 条件付き依存: `if (userOpts?.memoriesEnabled)` → `this.injectMemoriesContext()`
- 条件付き依存: `if (userOpts?.memoriesEnabled)` → `lazy.console.error()`
- 参照: `this.messages.length`, `userOpts?.contextMentions`, `userOpts?.memoriesEnabled`

## ChatConversation.retryMessage()
- 位置: async L804-821
- 役割: 指定のユーザー発言以降を会話から取り除き、引用とブランチ先端を更新する。
- 触るとき: 再送信で切り詰める範囲を変えるとき、または再送信後にブランチの表示がずれる問題を調べるとき。
- 呼び出し先: `super.retryMessage()`, `this.#pendingCitationUrls.clear()`, `this.#updateActiveBranchTipMessageId()`
- 参照: `MESSAGE_ROLE.USER`, `err.clientReason`, `message.role`, `removed.length`

## ChatConversation.injectRealTimeContext()
- 位置: async L836-855
- 役割: ブラウザやタブの情報を組み立て、ユーザー発言の userContext に realTimeContext として書き込む。
- 触るとき: タブ情報やコンテキストメンションを送信内容に含める仕様を変えるとき。前回と同じ文字列なら書き換えない（プロンプトキャッシュを安定させるため）。
- 呼び出し先: `lazy.buildBrowserContextPrompt()`
- 参照: `this.#lastBrowserContext`, `this.engine?.model`, `this.securityProperties`, `userMessage.content.userContext`, `userMessage.content.userContext.realTimeContext`, `userMessage?.content`

## ChatConversation.injectMemoriesContext()
- 位置: async L877-898
- 役割: 記憶を取得し、ユーザー発言の userContext.memoriesContext に書き込む。
- 触るとき: 記憶が注入されない、または過剰に注入される問題を調べるとき。記憶が返ったときだけ私的データのフラグを立てる点も確認する。
- 呼び出し先: `constructMemories()`, `this.#getPreviousRelevantMemories()`, `this.securityProperties.setPrivateData()`
- 参照: `memoriesContext.message.content`, `memoriesContext.relevantMemories`, `this.engine?.model`, `userMessage.content.relevantMemories`, `userMessage.content.userContext`, `userMessage.content.userContext.memoriesContext`, `userMessage?.content`

## ChatConversation.#getPreviousRelevantMemories()
- 位置: L907-925
- 役割: 直近のユーザー発言が持つ関連記憶を新しい順に集める。現在の発言は除く。
- 触るとき: 文脈用の記憶が直前の発言から正しく引き継がれているかを確認するとき。
- 呼び出し先: `userMessages .slice()`, `userMessages .slice(1) .flatMap()`
- 条件付き依存: `if (this.messages[i].role === MESSAGE_ROLE.USER)` → `userMessages.push()`
- 参照: `MESSAGE_ROLE.USER`, `message.content?.relevantMemories`, `this.messages`, `this.messages.length`, `this.messages[i].role`, `userMessages.length`

## ChatConversation.getSitesList()
- 位置: L936-956
- 役割: 会話内のメッセージのページ URL を訪問順に重複なく返す。既定では内部ページを除く。
- 触るとき: 履歴画面で会話に紐づくサイトが欠ける、または内部ページが混ざる問題を調べるとき。
- 呼び出し先: `message.pageUrl.protocol.startsWith()`, `seen.has()`, `this.messages.forEach()`
- 条件付き依存: `if (!seen.has(message.pageUrl.href))` → `seen.add()`
- 条件付き依存: `if (!seen.has(message.pageUrl.href))` → `deduped.push()`
- 参照: `message.pageUrl`, `message.pageUrl.href`

## ChatConversation.getMostRecentPageVisited()
- 位置: L964-968
- 役割: 会話中で最後に訪れた外部サイトの URL を返す。無ければ null。
- 触るとき: 直近のサイトを使う機能の対象が意図どおりか確認するとき。
- 呼び出し先: `sites.pop()`, `this.getSitesList()`
- 参照: `sites.length`

## ChatConversation.getMessagesInChatCompletionsFormat()
- 位置: L979-1029
- 役割: LLM API 向けの形式に変換する。空の応答や旧システム文脈を除き、メンションと URL を解決する。
- 触るとき: LLM に送るメッセージ列の内容（除外条件、文脈の挿入位置、URL トークン）を変えるとき、またはモデルに渡る内容を確認するとき。
- 呼び出し先: `baseWire.filter()`, `filteredSrc.findLastIndex()`, `getRoleLabel()`, `getRoleLabel(MESSAGE_ROLE.USER).toLowerCase()`, `isWireFiltered()`, `super.getMessagesInChatCompletionsFormat()`, `this.messages.filter()`
- 条件付き依存: `if (msg.role === getRoleLabel(MESSAGE_ROLE.USER).toLowerCase())` → `resolveMentionUrls()`
- 条件付き依存: `if (userContext)` → `Object.values(userContext).map()`
- 条件付き依存: `if (userContext)` → `Object.values()`
- 条件付き依存: `if (userContext)` → `getRoleLabel(MESSAGE_ROLE.USER).toLowerCase()`
- 条件付き依存: `if (userContext)` → `getRoleLabel()`
- 条件付き依存: `if (userContext)` → `msgsForAPI.splice()`
- 条件付き依存: `if (applyUrlTokens)` → `replaceUrlsWithTokens()`
- 参照: `MESSAGE_ROLE.USER`, `filteredSrc[lastUserMsgIdx].content.userContext`, `msg.content`, `msg.role`, `this.messages`

## isWireFiltered()
- 位置: L980-990
- 役割: 送信用の履歴から外すメッセージ（空のアシスタント応答、旧式の実時間・記憶のシステム行）を判定する。
- 触るとき: 送信履歴から消してよいメッセージの条件を変えるとき。
- 参照: `MESSAGE_ROLE.ASSISTANT`, `MESSAGE_ROLE.SYSTEM`, `SYSTEM_PROMPT_TYPE.MEMORIES`, `SYSTEM_PROMPT_TYPE.REAL_TIME`, `m.role`, `m?.content?.body`, `m?.content?.type`

## ChatConversation.#updateActiveBranchTipMessageId()
- 位置: L1031-1036
- 役割: アクティブなブランチの最新メッセージ ID を activeBranchTipMessageId に保存する。
- 触るとき: 分岐の末尾を参照する処理が古い ID を指すとき、または messages を入れ替えた後の再計算を確認するとき。
- 呼び出し先: `this.messages .filter()`, `this.messages .filter(m => m.isActiveBranch) .sort()`, `this.messages .filter(m => m.isActiveBranch) .sort((a, b) => b.ordinal - a.ordinal) .shift()`
- 参照: `a.ordinal`, `b.ordinal`, `m.isActiveBranch`, `this.activeBranchTipMessageId`, `this.messages .filter(m => m.isActiveBranch) .sort((a, b) => b.ordinal - a.ordinal) .shift()?.id`

## ChatConversation.messages()
- 位置: L1038-1042
- 役割: messages の設定時に親の setter を呼び、ブランチ先端 ID を更新する。
- 触るとき: messages 配列を入れ替える処理を変えるとき。splice は setter を通らないので手動で更新が必要。
- 呼び出し先: `this.#updateActiveBranchTipMessageId()`
- 参照: `super.messages`

## ChatConversation.messages()
- 位置: L1044-1046
- 役割: 親クラスの messages を返す。
- 触るとき: messages の参照先を変えるとき。
- 参照: `super.messages`

## ChatConversation.messageCount()
- 位置: L1048-1050
- 役割: ユーザーとアシスタントのメッセージ数を返す。
- 触るとき: 会話の件数表示や、空の会話の判定を調べるとき。
- 呼び出し先: `CHAT_ROLES.includes()`, `this.messages.filter()`
- 参照: `m.role`, `this.messages.filter(m => CHAT_ROLES.includes(m.role)).length`

## ChatConversation.tokenToUrl()
- 位置: L1052-1054
- 役割: UrlTokenizer のトークンから URL への対応を返す。
- 触るとき: トークンを URL に戻す箇所の参照先を確認するとき。
- 参照: `this.urlTokenizer.tokenToUrl`

## ChatConversation.urlToToken()
- 位置: L1056-1058
- 役割: UrlTokenizer の URL からトークンへの対応を返す。
- 触るとき: URL に割り当てられたトークンを確認するとき。
- 参照: `this.urlTokenizer.urlToToken`

## ChatConversation.getLatestUserMentionCount()
- 位置: L1066-1075
- 役割: 直近のユーザー発言の @メンションのうち、タブグループ以外の数を返す。
- 触るとき: メンション数に応じて表示や送信内容を変えるとき。
- 呼び出し先: `lastUserMsg?.content?.contextMentions?.filter()`, `lazy.isTabGroupMember()`, `this.messages.findLast()`
- 参照: `MESSAGE_ROLE.USER`, `lastUserMsg?.content?.contextMentions?.filter( m => !lazy.isTabGroupMember(m) ).length`, `m?.role`

## ChatConversation.addSeenUrls()
- 位置: L1082-1085
- 役割: 既読 URL を親に追加し、既読一覧の更新を通知する。
- 触るとき: 既読 URL の一覧が UI に反映されない問題を調べるとき。
- 呼び出し先: `super.addSeenUrls()`, `this.emit()`
- 参照: `this.seenUrls`

## ChatConversation.#clearToolUI()
- 位置: L1093-1096
- 役割: メッセージの toolUIData を消して更新を通知する。
- 触るとき: ツールの UI が残ったまま消えない問題を調べるとき。
- 呼び出し先: `this.emit()`
- 参照: `message.toolUIData`

## ChatConversation.updateToolUI()
- 位置: async L1105-1128
- 役割: メッセージのツール UI を次の uiType に遷移させて再描画を通知する。nextUI が null なら消去する。
- 触るとき: 確認ダイアログや結果カードの状態遷移を変えるとき。
- 呼び出し先: `this.emit()`
- 条件付き依存: `if (nextUI === null)` → `this.#clearToolUI()`
- 参照: `data.updateData`, `data?.properties`, `message.toolUIData`, `message.toolUIData.properties`, `message.toolUIData.properties.confirmedData`

## ChatConversation.addUIToolToCurrentMessage()
- 位置: L1140-1224
- 役割: 最後のアシスタント応答にツール UI データを付ける。同じ toolCallId なら統合し、確認系 UI には元の発言も添える。
- 触るとき: UI カードが別のメッセージに付く、または進捗更新が件数に反映されない問題を調べるとき。
- 呼び出し先: `lazy.CONFIRMATION_UI_TYPES.includes()`, `this.emit()`, `this.messages .filter()`, `this.messages .filter( m => m.role === MESSAGE_ROLE.ASSISTANT && m.content?.type === "text" ) .at()`
- 条件付き依存: `if (!currentMessage)` → `this.addAssistantMessage()`
- 条件付き依存: `if (lazy.CONFIRMATION_UI_TYPES.includes(uiData.uiType))` → `lazy.ToolUI.findOriginalUserPrompt()`
- 条件付き依存: `if (isUpdate)` → `new Date().toISOString()`
- 条件付き依存: `if (!(isUpdate))` → `new Date().toISOString()`
- 条件付き依存: `if (emitComplete)` → `this.emit()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `currentMessage.toolUIData`, `currentMessage.toolUIData.properties`, `currentMessage.toolUIData.toolCallId`, `currentMessage.toolUIData.updateCount`, `enrichedUIData.properties`, `m.content?.type`, `m.role`, `this.messages`, `uiData.uiType`

## ChatConversation.addHistoryResults()
- 位置: L1236-1244
- 役割: 閲覧履歴の検索結果を URL 単位で会話のプールに統合し、表示用の時刻を付ける。
- 触るとき: 履歴グリッドの件数や時刻表示を変えるとき、または検索結果が次の応答に引き継がれない問題を調べるとき。
- 呼び出し先: `lazy.convertTimestamp()`, `this.#historyResultsPool.set()`
- 参照: `lazy.fluentStrings`, `record.timestamp`, `record.url`, `record.visitDate`

## ChatConversation.getHistoryResultsSnapshot()
- 位置: L1253-1255
- 役割: 履歴結果プールの現在の内容を配列で返す。
- 触るとき: 応答完了時にメッセージへ保存される履歴グリッドの中身を確認するとき。
- 呼び出し先: `this.#historyResultsPool.values()`

## ChatConversation.applyHistoryAssets()
- 位置: L1264-1279
- 役割: サムネイル画像とファビコン有無を、履歴と引用の両プールに URL 単位で反映する。
- 触るとき: サムネイルやファビコンが表示されない問題を調べるとき。サムネイルを要求していない場合は画像を上書きしない点に注意。
- 呼び出し先: `this.#citationsPool.get()`, `this.#historyResultsPool.get()`
- 参照: `citation.hasFavicon`, `record.hasFavicon`, `record.image`

## ChatConversation.rehydrateHistoryResultsPool()
- 位置: L1286-1292
- 役割: 各メッセージに保存された履歴結果から履歴プールを組み直す。
- 触るとき: 会話を読み直した後に履歴グリッドが消える問題を調べるとき。
- 呼び出し先: `this.#historyResultsPool.set()`
- 参照: `message.historyResults`, `record.url`, `this.messages`

## ChatConversation.addCitations()
- 位置: L1299-1306
- 役割: Web 検索の引用を URL 単位で統合し、今ターンの引用として記録する。
- 触るとき: 引用チップの内容や重複の扱いを変えるとき。既存のファビコン情報は残す。
- 呼び出し先: `this.#citationsPool.get()`, `this.#citationsPool.set()`, `this.#pendingCitationUrls.add()`
- 参照: `record.url`

## ChatConversation.getCitationsSnapshot()
- 位置: L1313-1317
- 役割: 今ターンで参照された引用を配列で返す。
- 触るとき: 応答メッセージに付く引用チップの内容を確認するとき。
- 呼び出し先: `[...this.#pendingCitationUrls] .map()`, `[...this.#pendingCitationUrls] .map(url => this.#citationsPool.get(url)) .filter()`, `this.#citationsPool.get()`
- 参照: `this.#pendingCitationUrls`

## ChatConversation.rehydrateCitationsPool()
- 位置: L1322-1328
- 役割: 各メッセージに保存された引用から引用プールを組み直す。
- 触るとき: 会話の再読み込み後に引用チップが消える問題を調べるとき。
- 呼び出し先: `this.#citationsPool.set()`
- 参照: `message.citations`, `record.url`, `this.messages`
