# browser/components/aiwindow/ui/modules/ToolUI.sys.mjs

source: browser/components/aiwindow/ui/modules/ToolUI.sys.mjs
source-hash: e221153ad9d9d4d802c9a950df9eedef9d2c6735
lines: 1462

## <module>
- 役割: AI Window のツール UI (タブ操作の確認カード、AI タブを開く、元に戻す、再試行) からの更新を受けて、タブの閉じる・グループ化・開く処理と、その計測を振り分ける。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`, `this.#handleCancelTabSelection.bind()`, `this.#handleConfirmTabGroupSelection.bind()`, `this.#handleConfirmationTabSelection.bind()`, `this.#handleOpenAITab.bind()`, `this.#handleOpenAndGroupTabsSelection.bind()`, `this.#handleRetryPrompt.bind()`, `this.#handleUndoTabClose.bind()`, `this.#handleUndoTabGroup.bind()`

## ToolUI.registerTabKeys()
- 位置: L142-146
- 役割: 確認カードの選択トークンと、タブの永続キーの対応表を、ツール呼び出し ID ごとに保存する。空なら何もしない。
- 触るとき: 確認カードを出す時点で、選ばれたタブとの紐付けの仕方を変えるとき。
- 条件付き依存: `if (toolCallId && tokenToKey?.size)` → `this.#tabKeysByToolCall.set()`
- 参照: `tokenToKey?.size`

## ToolUI.clearTabKeys()
- 位置: L153-155
- 役割: ツール呼び出し ID に紐づく対応表を削除する。確認が完了またはキャンセルされたときに呼ばれる。
- 触るとき: 確認の後も対応表が残り、古いタブを指してしまう問題を追うとき。
- 呼び出し先: `this.#tabKeysByToolCall.delete()`

## ToolUI.#getConfirmationReason()
- 位置: L157-168
- 役割: 選択されたタブにピン留め、選択中、単独のタブがあれば対応する理由を返し、それ以外は user_action を返す。
- 触るとき: 確認カードの理由 (reason) の分類を変えるとき。
- 呼び出し先: `tabs.some()`
- 参照: `t.pinned`, `t.selected`, `tabs.length`

## ToolUI.#verifyAndCollectTabs()
- 位置: L181-236
- 役割: 選択されたトークンを永続キーで、AI Window の生きているタブに照合し、ウィンドウごとのタブ配列を返す。一件も一致しなければ null。
- 触るとき: 確認後に閉じたタブが見つからない、または別ウィンドウのタブが混ざるとき。
- 呼び出し先: `claimedTabs.add()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows.filter()`, `tabsByWindow.get()`, `tabsByWindow.get(match.window).push()`, `tabsByWindow.has()`, `tokenToKey.get()`
- 条件付き依存: `if (!win)` → `lazy.console.error()`
- 条件付き依存: `if (!tokenToKey?.size)` → `lazy.console.warn()`
- 条件付き依存: `if (permanentKey)` → `candidateWindow.gBrowser.tabs.find()`
- 条件付き依存: `if (permanentKey)` → `claimedTabs.has()`
- 条件付き依存: `if (!match)` → `lazy.console.warn()`
- 条件付き依存: `if (!tabsByWindow.has(match.window))` → `tabsByWindow.set()`
- 条件付き依存: `if (verifiedCount === 0)` → `lazy.console.warn()`
- 参照: `match.tab`, `match.window`, `selectedTab.token`, `selectedTab.url`, `t.permanentKey`, `tokenToKey?.size`

## ToolUI.closeSelectedTabs()
- 位置: async L246-282
- 役割: 照合したタブをウィンドウごとに TabManagementService.closeTabs で閉じ、元に戻す操作 ID と失敗したタブを集める。
- 触るとき: 確認後の閉じる処理の結果の集計を変えるとき。
- 呼び出し先: `lazy.tabManagementService.closeTabs()`, `tabs.find()`, `this.#verifyAndCollectTabs()`
- 条件付き依存: `if (result.failedTabs.length)` → `failedTabs.push()`
- 条件付き依存: `if (result.operationId)` → `operationIds.push()`
- 参照: `activeTab.smartWindowActionSource`, `ownerWindow.gBrowser.selectedTab`, `result.failedTabs`, `result.failedTabs.length`, `result.operationId`, `result.requestedCount`

## ToolUI.#recordTabConfirmationResponse()
- 位置: L298-317
- 役割: 確認カードへの応答 (confirm か cancel) を、ブラウザ操作プロンプトの計測として記録する。
- 触るとき: 確認カードの応答の計測項目を変えるとき。
- 呼び出し先: `lazy.ToolUITelemetry.recordBrowserActionPromptResponse()`
- 参照: `conversation.id`, `conversation.messageCount`

## ToolUI.#recordConfirmedBrowserActionComplete()
- 位置: L329-350
- 役割: 確認時に保存した計測情報があれば、結果と影響したタブ数を足してブラウザ操作の完了として記録する。
- 触るとき: 操作完了の計測が抜ける、または二重に記録されるとき。
- 呼び出し先: `conversation.takePendingBrowserActionTelemetry()`, `lazy.ToolUITelemetry.recordBrowserActionComplete()`

## ToolUI.#summarizeTabActionOutcome()
- 位置: L361-367
- 役割: 成功数と要求数から結果の区分 (成功、一部成功、失敗) と、影響したタブ数、エラーコードを作る。
- 触るとき: 一部だけ成功したときの結果区分を変えるとき。
- 呼び出し先: `lazy.ToolUITelemetry.browserActionResult()`

## ToolUI.#recordAbandonedTabConfirmation()
- 位置: L378-395
- 役割: 対象のタブが無くなっていた確認を、confirm の応答と、エラーによる完了として記録する。
- 触るとき: タブが失われた確認の計測の扱いを変えるとき。
- 呼び出し先: `this.#recordConfirmedBrowserActionComplete()`, `this.#recordTabConfirmationResponse()`
- 参照: `selectedTabs.length`

## ToolUI.#finalizeTabActionConfirmation()
- 位置: L413-459
- 役割: 確認の応答と結果を記録し、ツール UI を AI アクション結果の表示に更新してから、保留中のツール確認を解決して会話を続けられるようにする。
- 触るとき: 確認の後に会話が止まる、または結果カードが出ないとき。
- 呼び出し先: `Date.now()`, `conversation.messages.at()`, `conversation.resolvePendingToolConfirmation()`, `conversation.updateToolUI()`, `selectedTabs.map()`, `this.#recordTabConfirmationResponse()`
- 条件付き依存: `if (resultInfo)` → `this.#recordConfirmedBrowserActionComplete()`
- 参照: `UI_TYPES.AI_ACTION_RESULT`, `confirmationMessage.action`, `conversation.messages.at(-1)?.content?.body?.action`, `selectedTabs.length`

## ToolUI.#handleConfirmationTabSelection()
- 位置: async L468-509
- 役割: 選択されたタブを閉じて結果を最終化する。照合できなければ失敗として記録し、false を返す。
- 触るとき: タブを閉じる確認ボタンの振る舞いを変えるとき。
- 呼び出し先: `Math.max()`, `this.#finalizeTabActionConfirmation()`, `this.#summarizeTabActionOutcome()`, `this.#tabKeysByToolCall.get()`, `this.clearTabKeys()`, `this.closeSelectedTabs()`
- 条件付き依存: `if (!result)` → `this.#recordAbandonedTabConfirmation()`
- 参照: `result.failedTabs.length`, `result.operationIds`, `result.operationIds.length`, `result.requestedCount`, `selectedTabs.length`

## ToolUI.#handleCancelTabSelection()
- 位置: L518-551
- 役割: キャンセルを記録し、結果を cancelled にして、キャンセル表示に切り替える。自動キャンセルと利用者のキャンセルは理由で区別する。
- 触るとき: キャンセル時の表示や、会話に返す文言を変えるとき。
- 呼び出し先: `conversation.resolvePendingToolConfirmation()`, `conversation.updateToolUI()`, `this.#recordConfirmedBrowserActionComplete()`, `this.#recordTabConfirmationResponse()`, `this.clearTabKeys()`
- 参照: `UI_TYPES.CANCELLED_COMPONENT`, `updateData?.actionType`, `updateData?.reason`

## ToolUI.#handleConfirmTabGroupSelection()
- 位置: async L560-608
- 役割: 選択されたタブをグループにし、成功すれば結果を最終化する。失敗時は記録して false を返す。
- 触るとき: グループ化の確認ボタンの振る舞いを変えるとき。
- 呼び出し先: `this.#finalizeTabActionConfirmation()`, `this.#summarizeTabActionOutcome()`, `this.#tabKeysByToolCall.get()`, `this.clearTabKeys()`, `this.createTabGroup()`
- 条件付き依存: `if (!result?.success)` → `this.#recordAbandonedTabConfirmation()`
- 参照: `result.error`, `result.group`, `result.group.id`, `result.group.tabCount`, `result?.success`, `selectedTabs.length`

## ToolUI.#handleOpenAndGroupTabsSelection()
- 位置: async L619-648
- 役割: チャットのタブを起点に、選ばれたタブを開いてグループにする。成功すれば結果を最終化する。
- 触るとき: 開いてグループにする操作の結果が画面に反映されないとき。
- 呼び出し先: `this.#finalizeTabActionConfirmation()`, `this.clearTabKeys()`, `this.findChatTab()`, `this.openOrGroupTabs()`
- 参照: `conversation?.id`, `result.group`, `result.group.id`, `result.group?.id`, `result.mergedCount`, `result.switched`, `result?.success`

## ToolUI.#handleUndoTabGroup()
- 位置: async L657-729
- 役割: 操作 ID ごとにグループを解除し、戻したタブ数と経過時間を記録する。失敗があれば記録して false を返す。
- 触るとき: グループ化の取り消しの挙動や計測を変えるとき。
- 呼び出し先: `Date.now()`, `Math.max()`, `conversation.updateToolUI()`, `lazy.ToolUITelemetry.recordBrowserActionUndo()`, `lazy.tabManagementService.ungroupTabs()`, `ungroupedTabs.push()`
- 条件付き依存: `if (!operationIds.length)` → `lazy.console.error()`
- 条件付き依存: `if (!result?.success)` → `lazy.console.error()`
- 条件付き依存: `if (!result?.success)` → `lazy.ToolUITelemetry.recordBrowserActionUndo()`
- 条件付き依存: `if (!result?.success)` → `Math.max()`
- 参照: `UI_TYPES.AI_ACTION_RESULT`, `conversation.id`, `conversation.messageCount`, `operationIds.length`, `result.ungroupedTabs`, `result?.error`, `result?.success`, `result?.ungroupedTabs?.length`, `ungroupedTabs.length`

## ToolUI.#handleUndoTabClose()
- 位置: async L738-832
- 役割: 操作 ID ごとに閉じたタブを復元し、成功、一部成功、失敗の区分を決めて計測し、ツール UI を更新する。例外は失敗として記録する。
- 触るとき: 閉じたタブの取り消しの結果区分や表示を変えるとき。
- 呼び出し先: `Date.now()`, `Math.max()`, `conversation.updateToolUI()`, `lazy.ToolUITelemetry.recordBrowserActionUndo()`, `lazy.console.error()`, `lazy.console.log()`, `lazy.tabManagementService.restoreTabs()`
- 条件付き依存: `if (!operationIds.length)` → `lazy.console.error()`
- 条件付き依存: `if (result.failedTabs.length)` → `failedTabs.push()`
- 参照: `UI_TYPES.AI_ACTION_RESULT`, `conversation.id`, `conversation.messageCount`, `error?.name`, `failedTabs.length`, `operationIds.length`, `result.failedTabs`, `result.failedTabs.length`, `result.requestedCount`, `result.restoredCount`

## ToolUI.#handleRetryPrompt()
- 位置: async L841-845
- 役割: 再試行の表示のため、ツール UI を null に更新して消す。
- 触るとき: 再試行カードの消え方を変えるとき。
- 呼び出し先: `conversation.updateToolUI()`

## ToolUI.#findLastAssistantTextMessage()
- 位置: L854-862
- 役割: 会話の中で最後のアシスタントのテキストメッセージを探して返す。無ければ null。
- 触るとき: 自動キャンセルの対象となる確認カードの特定条件を変えるとき。
- 呼び出し先: `messages.findLast()`
- 参照: `lazy.MESSAGE_ROLE.ASSISTANT`, `message.content?.type`, `message.role`

## ToolUI.#canOriginTabJoinGroup()
- 位置: L883-890
- 役割: チャットのタブがグループを作るウィンドウにあり、分割表示でなく、まだ含まれていなければ true を返す。
- 触るとき: チャットのタブをグループに含める条件を変えるとき。
- 呼び出し先: `groupTabs.includes()`
- 参照: `originTab.documentGlobal`, `originTab.splitview`

## ToolUI.findChatTab()
- 位置: L906-923
- 役割: AI Window を順に探し、会話 ID が一致するチャットのタブを返す。無ければ null。
- 触るとき: 会話 ID からチャットのタブを見つける経路を変えるとき。
- 呼び出し先: `[...win.gBrowser.tabs].find()`, `lazy.AIWindow.getChatTabConversationId()`, `lazy.AIWindow.isAIWindowActive()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## ToolUI.#dropLoneChatTab()
- 位置: L943-958
- 役割: チャットのタブ以外にグループ化できるタブが残らない場合は、チャットのタブを外す。チャットのタブだけが選ばれた場合は外さない。
- 触るとき: チャットのタブだけのグループができてしまう問題を追うとき。
- 呼び出し先: `lazy.tabManagementService.getGroupingRejection()`, `selections.find()`, `tokenToKey?.get()`, `windowTabs.filter()`
- 参照: `chatSelection.token`, `groupable.length`, `groupable[0].permanentKey`, `selection.isChatTab`, `selections.length`, `tab.permanentKey`

## ToolUI.createTabGroup()
- 位置: async L983-1029
- 役割: 確認された選択を照合し、グループ化するウィンドウを決めて TabManagementService で作る。他ウィンドウのタブは other-window の理由で失敗に入れる。
- 触るとき: グループ化の対象ウィンドウの選び方や、失敗理由を変えるとき。
- 呼び出し先: `lazy.tabManagementService.createTabGroup()`, `result.failedTabs.push()`, `tabsByWindow.get()`, `tabsByWindow.has()`, `this.#dropLoneChatTab()`, `this.#verifyAndCollectTabs()`
- 条件付き依存: `if (!groupWindow)` → `tabsByWindow.get()`
- 参照: `ownerTabs.length`, `tabsByWindow.get(groupWindow).length`

## ToolUI.openAndGroupTabs()
- 位置: async L1048-1088
- 役割: 選ばれた URL を既存のタブか新規のタブに解決し、条件を満たせばチャットのタブも加えてグループにする。統合数を結果に添える。
- 触るとき: 開いてグループにする対象や、チャットのタブを含める条件を変えるとき。
- 呼び出し先: `lazy.tabManagementService.createTabGroup()`, `lazy.tabManagementService.getGroupingRejection()`, `lazy.tabManagementService.resolveOrOpenTabs()`, `resolvedTabs.some()`, `this.#canOriginTabJoinGroup()`
- 条件付き依存: `if (!tabs.length)` → `lazy.console.warn()`
- 参照: `resolvedTabs.length`, `tabs.length`

## ToolUI.openOrSwitchToTab()
- 位置: async L1101-1123
- 役割: URL が一致する既存のタブがあれば切り替え、無ければ背景で新しく開いて切り替える。現在のタブは移動させない。
- 触るとき: 単一のタブを開く操作で、現在のタブが変わってしまう問題を追うとき。
- 呼び出し先: `lazy.tabManagementService.findOpenTab()`, `lazy.tabManagementService.openTabs()`, `lazy.tabManagementService.switchToTab()`
- 条件付き依存: `if (existingTab)` → `lazy.tabManagementService.switchToTab()`
- 参照: `openedTabs.length`, `tab.url`

## ToolUI.openOrGroupTabs()
- 位置: async L1136-1141
- 役割: 選択が一件なら openOrSwitchToTab、複数なら openAndGroupTabs に振り分ける。
- 触るとき: 一件と複数の場合の振り分け条件を変えるとき。
- 呼び出し先: `this.openAndGroupTabs()`
- 条件付き依存: `if (tabs.length === 1)` → `this.openOrSwitchToTab()`
- 参照: `tabs.length`

## ToolUI.findOriginalUserPrompt()
- 位置: L1151-1179
- 役割: アシスタントのメッセージの親を最大 5 段までたどり、最初に見つかったテキストのユーザー発言を返す。無ければ null。
- 触るとき: 再試行に使う元の質問文が取れないとき。
- 呼び出し先: `messages.find()`
- 参照: `assistantMessage.parentMessageId`, `lazy.MESSAGE_ROLE.USER`, `m.id`, `nextMessage.content.body`, `nextMessage.content?.type`, `nextMessage.parentMessageId`, `nextMessage.role`

## ToolUI.#promptActionForUIData()
- 位置: L1187-1193
- 役割: 確認カードの UI 種別に対応するアクション名を返す。properties の actionType があれば優先する。確認カードでなければ null。
- 触るとき: 確認カードのアクション名の対応を変えるとき。
- 参照: `toolUIData.properties?.actionType`, `toolUIData.uiType`

## ToolUI.handleUIDisplayTelemetry()
- 位置: L1195-1211
- 役割: 確認カードが表示されたときに、ブラウザ操作プロンプトの表示計測を記録する。確認カードでなければ何もしない。
- 触るとき: 確認カードの表示時の計測項目を変えるとき。
- 呼び出し先: `lazy.ToolUITelemetry.recordBrowserActionPrompt()`, `this.#getConfirmationReason()`, `this.#promptActionForUIData()`
- 参照: `tabs.length`, `toolUIData.properties?.tabs`

## ToolUI.#handleOpenAITab()
- 位置: L1231-1276
- 役割: AI タブのビューアの URL が about:smartpage で状態が choose のときだけ、現在のタブか新しいタブで開く。成功したらリンクのクリックを記録し、カードを完了にする。
- 触るとき: AI タブを開く条件や遷移先を変えるとき。
- 呼び出し先: `Glean.smartWindow.linkClick.record()`, `URL.parse()`, `conversation.updateToolUI()`, `lazy.SmartWindowTelemetry.recordUriLoad()`, `lazy.URILoadingHelper.openTrustedLinkIn()`, `lazy.console.error()`, `parsedURL.searchParams.get()`
- 参照: `UI_TYPES.AITAB`, `conversation.id`, `conversation.messageCount`, `message.toolUIData.properties?.state`, `message.toolUIData?.properties?.viewerURL`, `message.toolUIData?.uiType`, `parsedURL.pathname`, `parsedURL?.protocol`, `window.gBrowser.selectedBrowser.browsingContext.originAttributes`, `window?.gBrowser`

## ToolUI.autoCancelActiveConfirmation()
- 位置: async L1307-1370
- 役割: 直前のアシスタントメッセージが確認カードなら、理由 auto_cancel で自動的にキャンセルする。元の質問は再試行用に保存する。
- 触るとき: 新しい質問を送ったときに古い確認カードが残る問題を追うとき。
- 呼び出し先: `CONFIRMATION_UI_TYPES.includes()`, `lazy.console.log()`, `this.#findLastAssistantTextMessage()`, `this.#promptActionForUIData()`, `this.handleUpdate()`
- 条件付き依存: `if (!conversation?.messages?.length)` → `lazy.console.log()`
- 条件付き依存: `if (!isActiveConfirmation)` → `lazy.console.log()`
- 条件付き依存: `if (originalUserPrompt)` → `Date.now()`
- 参照: `UI_UPDATE_TYPES.CANCEL_TAB_SELECTION`, `conversation.messages`, `conversation.pendingRetry`, `conversation?.messages?.length`, `lastAssistantTextMessage.id`, `lastAssistantTextMessage.toolUIData`, `lastAssistantTextMessage.toolUIData.properties?.originalUserPrompt`, `lastAssistantTextMessage.toolUIData.toolCallId`, `lastAssistantTextMessage.toolUIData.uiType`, `lastAssistantTextMessage?.toolUIData?.uiType`

## ToolUI.injectRetryToolUIDataIfNeeded()
- 位置: L1379-1413
- 役割: 再試行の保留があり対象がテキストのアシスタントメッセージなら、再試行カードの情報をそのメッセージに付けて保留を消す。
- 触るとき: 再試行カードが出ない、または二回出るとき。
- 呼び出し先: `crypto.randomUUID()`, `lazy.console.log()`
- 参照: `UI_TYPES.RETRY_COMPONENT`, `conversation.pendingRetry`, `conversation.pendingRetry.cancelledUiType`, `conversation.pendingRetry.originalUserPrompt`, `conversation?.pendingRetry`, `lazy.MESSAGE_ROLE.ASSISTANT`, `msg.toolUIData`, `msg?.content?.type`, `msg?.role`

## ToolUI.handleUpdate()
- 位置: async L1428-1460
- 役割: メッセージとツール呼び出し ID が一致するときだけ、更新種別に対応する #UPDATE_TYPE_HANDLERS のハンドラに処理を渡す。未知の種別は false を返す。
- 触るとき: 確認カードの新しい操作種別を追加するとき。
- 呼び出し先: `conversation?.messages?.find()`, `handler()`
- 条件付き依存: `if (typeof handler !== "function")` → `lazy.console.error()`
- 参照: `m.id`, `message?.toolUIData?.toolCallId`, `this.#UPDATE_TYPE_HANDLERS`
