# browser/components/aiwindow/ui/components/ai-chat-content/ai-chat-content.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/ai-chat-content.mjs
source-hash: dc75ea5e2228ceb26270cf05b4807cd1280548df
lines: 2031

## <module>
- 役割: AI ウィンドウの会話領域（メッセージ列、ツール UI、スクロール、確認カード）を描画する ai-chat-content 要素を定義する。
- 呼び出し先: `customElements.define()`

## AIChatContent.constructor()
- 位置: L166-202
- 役割: ツール UI 種別ごとの描画関数の対応表を作り、既定の状態と seenUrls を初期化する。
- 触るとき: 新しいツール UI 種別を足すとき、または会話の初期状態を変えるときに見る。
- 呼び出し先: `super()`
- 参照: `UI_TYPES.AGENT_MONITOR`, `UI_TYPES.AITAB`, `UI_TYPES.AI_ACTION_RESULT`, `UI_TYPES.CANCELLED_COMPONENT`, `UI_TYPES.RETRY_COMPONENT`, `UI_TYPES.TAB_GROUP_CONFIRMATION`, `UI_TYPES.WEBSITE_CONFIRMATION`, `this.#uiRenderMap`, `this.assistantIsLoading`, `this.assistantResponseAnnouncement`, `this.conversationId`, `this.conversationState`, `this.errorObj`, `this.followUpSuggestions`, `this.isSearching`, `this.seenUrls`

## [UI_TYPES.AITAB]()
- 位置: L177-177
- 役割: aitab 種別のツール UI を #renderAITab で描画する。
- 触るとき: AI タブのツール UI の表示を変えるとき、または aitab 種別が出ないときに見る。
- 呼び出し先: `this.#renderAITab()`

## [UI_TYPES.TAB_GROUP_CONFIRMATION]()
- 位置: L178-179
- 役割: タブグループ確認カード種別を #renderTabGroupConfirmation で描画する。
- 触るとき: タブグループの確認カードの表示を変えるとき、またはカードが出ないときに見る。
- 呼び出し先: `this.#renderTabGroupConfirmation()`

## [UI_TYPES.WEBSITE_CONFIRMATION]()
- 位置: L180-181
- 役割: サイト確認カード種別を #renderWebsiteConfirmation で描画する。
- 触るとき: サイト確認カードの表示を変えるとき、またはカードが出ないときに見る。
- 呼び出し先: `this.#renderWebsiteConfirmation()`

## [UI_TYPES.AI_ACTION_RESULT]()
- 位置: L182-182
- 役割: アクション結果種別を #renderActionResult で描画する。
- 触るとき: アクション結果の表示を変えるとき、または結果が出ないときに見る。
- 呼び出し先: `this.#renderActionResult()`

## [UI_TYPES.CANCELLED_COMPONENT]()
- 位置: L183-183
- 役割: キャンセル済みの表示を #renderCancelledComponent で描画する。
- 触るとき: キャンセル時の表示を変えるときに見る。
- 呼び出し先: `this.#renderCancelledComponent()`

## [UI_TYPES.RETRY_COMPONENT]()
- 位置: L184-184
- 役割: 再試行ボタン種別を #renderRetryComponent で描画する。
- 触るとき: 再試行の表示や文言を変えるとき、またはボタンが出ないときに見る。
- 呼び出し先: `this.#renderRetryComponent()`

## [UI_TYPES.AGENT_MONITOR]()
- 位置: L185-185
- 役割: エージェント監視カード種別を #renderAgentMonitorComponent で描画する。
- 触るとき: 監視カードの表示を変えるとき、または監視カードが出ないときに見る。
- 呼び出し先: `this.#renderAgentMonitorComponent()`

## AIChatContent.connectedCallback()
- 位置: L204-229
- 役割: イベントリスナー、フッター操作、オーバーフロー監視、スクロール監視、エラー監視を登録し、タブグループ既定名を取得する。
- 触るとき: 要素の起動時に何が接続されるかを確認するとき、または初期化順を変えるときに見る。
- 呼び出し先: `dispatchClientError()`, `installClientErrorListeners()`, `super.connectedCallback()`, `this.#initEventListeners()`, `this.#initFooterActionListeners()`, `this.#initOverflowObserver()`, `this.#initScrollListener()`, `this.#scrollPositions.clear()`, `this.dispatchEvent()`, `this.ownerDocument.l10n .formatValue()`, `this.ownerDocument.l10n .formatValue("smart-window-default-tab-group-label") .then()`
- 条件付き依存: `if (label)` → `this.requestUpdate()`
- 参照: `this.#defaultTabGroupLabel`, `this.#removeClientErrorListeners`

## AIChatContent.disconnectedCallback()
- 位置: L231-242
- 役割: オーバーフロー監視、アニメーションフレーム、スクロール監視、エラー監視を後始末する。
- 触るとき: 要素を外した後にタイマーやリスナーが残る不具合を調べるときに見る。
- 呼び出し先: `super.disconnectedCallback()`, `this.#overflowObserver?.disconnect()`, `this.#removeClientErrorListeners()`, `this.#teardownScrollListener()`
- 条件付き依存: `if (this.#overflowRafId)` → `cancelAnimationFrame()`
- 参照: `this.#overflowObserver`, `this.#overflowRafId`, `this.#removeClientErrorListeners`

## AIChatContent.updated()
- 位置: L244-247
- 役割: 描画後に、エージェント監視の新規カードへフォーカスを移す処理を呼ぶ。
- 触るとき: 描画後のフォーカス移動を変えるとき、またはカードにフォーカスが移らないときに見る。
- 呼び出し先: `super.updated()`, `this.#maybeFocusAgentMonitorCard()`

## AIChatContent.#maybeFocusAgentMonitorCard()
- 位置: L253-269
- 役割: 新規作成モードの監視カードを探し、未フォーカスなら名前入力へフォーカスする。
- 触るとき: /watch などで作られたカードに自動フォーカスする条件を変えるとき、または同じカードへ何度もフォーカスするときに見る。
- 呼び出し先: `this.#focusMonitorNameInput()`, `this.conversationState.findLast()`
- 参照: `UI_TYPES.AGENT_MONITOR`, `card.messageId`, `card.toolUIData.toolCallId`, `msg.isRestored`, `msg.toolUIData.properties?.mode`, `msg?.toolUIData?.uiType`, `this.#focusedMonitorCardId`

## AIChatContent.#focusMonitorNameInput()
- 位置: async L271-283
- 役割: 監視カードの描画完了を待ってから、接続中かつ作成モードなら名前入力にフォーカスする。
- 触るとき: 監視カードの名前入力の初期フォーカスが効かないときに見る。
- 呼び出し先: `CSS.escape()`, `item.getAttribute()`, `this.shadowRoot?.querySelector()`
- 条件付き依存: `if (item.isConnected && item.getAttribute("mode") === "create")` → `item.focusName()`
- 参照: `item.isConnected`, `item.updateComplete`

## AIChatContent.#dispatchAction()
- 位置: L285-296
- 役割: AIChatContent:DispatchAction を action と追加情報付きで発火し、アクターへ渡す。
- 触るとき: UI の操作を親プロセスに渡す経路を変えるとき、または操作が届かないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#handleSetMode()
- 位置: L300-305
- 役割: アクターから届いた mode を属性に反映し、スタイルから参照できるようにする。
- 触るとき: サイドバーとフルページの見た目の切り替えが効かないときに見る。
- 条件付き依存: `if (mode)` → `this.setAttribute()`
- 参照: `event.detail?.mode`

## AIChatContent.#initEventListeners()
- 位置: L310-373
- 役割: アクターからのメッセージ、切り詰め、メモリー削除、既出 URL、生成状態、資産準備などのイベントを接続する。
- 触るとき: アクターから届くイベントを増やすとき、または特定のイベントが処理されないときに見る。
- 呼び出し先: `this.#handleAssetsReady.bind()`, `this.#handleSeenUrls.bind()`, `this.#handleSetGenerating.bind()`, `this.#handleSetMode.bind()`, `this.#onFollowUpSelected.bind()`, `this.addEventListener()`, `this.messageEvent.bind()`, `this.openAccountSignInAfterError.bind()`, `this.openNewChatAfterError.bind()`, `this.removeAppliedMemoryEvent.bind()`, `this.retryUserMessageAfterError.bind()`, `this.truncateEvent.bind()`
- 参照: `event.detail`, `this.#pendingAnnouncementMessageId`, `this.assistantResponseAnnouncement`

## AIChatContent.#initFooterActionListeners()
- 位置: L380-430
- 役割: フッターや適用メモリーの子要素から出るイベントを受け、アクターへの操作として転送する。コピーは本文を取り出して渡す。
- 触るとき: フッターのボタンの操作内容を変えるとき、またはボタンを押しても親に届かないときに見る。
- 呼び出し先: `text .split()`, `text .split("\n") .slice()`, `text .split("\n") .slice(lineRange[0], lineRange[1]) .join()`, `this.#dispatchAction()`, `this.#getAssistantMessageBody()`, `this.addEventListener()`
- 参照: `event.detail`, `this.#onPanelShown`

## AIChatContent.#onPanelShown()
- 位置: L435-453
- 役割: shown の panel-list がヘッダーに被る場合、その分だけ下へずらし最大高さも縮める。
- 触るとき: メニューがチャットヘッダーの下に隠れる・ヘッダーのクリックを奪う問題を直すとき、またはパネルの位置計算を変えるときに見る。
- 呼び出し先: `Math.max()`, `event.composedPath()`, `panel.getAttribute()`, `panel.getBoundingClientRect()`, `parseFloat()`, `this.#topSpacing()`
- 参照: `bounds.height`, `bounds.top`, `panel.style.maxHeight`, `panel.style.top`, `panel?.localName`, `window.innerHeight`

## AIChatContent.#topSpacing()
- 位置: L457-463
- 役割: チャット一覧が上端に確保している padding-block-start の値を px で返す。
- 触るとき: ヘッダーの高さやチャット一覧の余白を変えるとき、パネルの位置補正がずれないか確認するときに見る。
- 呼び出し先: `getComputedStyle()`, `parseFloat()`, `this.shadowRoot?.querySelector()`
- 参照: `getComputedStyle(innerWrapper).paddingBlockStart`

## AIChatContent.#initOverflowObserver()
- 位置: L465-474
- 役割: 内側のラッパーのサイズ変化を ResizeObserver で監視し、溢れ状態を更新する。
- 触るとき: 会話が増減してもスクロールのフェードや jump ボタンが更新されないときに見る。
- 呼び出し先: `this.#overflowObserver.observe()`, `this.#updateOverflowState()`, `this.shadowRoot.querySelector()`, `this.updateComplete.then()`
- 参照: `this.#overflowObserver`

## AIChatContent.#updateOverflowState()
- 位置: L482-501
- 役割: スクロールできるかで overflowing 属性を付け外しし、jump ボタンの状態も更新する。
- 触るとき: スクロールのフェード表示の判定基準（10px の余白）を変えるとき、または表示が追随しないときに見る。
- 呼び出し先: `this.#updateJumpButtonState()`, `this.shadowRoot?.querySelector()`, `wrapper.toggleAttribute()`
- 参照: `innerWrapper.children.length`, `this.#wrapper`, `wrapper.clientHeight`, `wrapper.scrollHeight`

## AIChatContent.#wrapper()
- 位置: L503-505
- 役割: スクロール対象の .chat-content-wrapper 要素を返す。
- 触るとき: スクロール領域のクラス名を変えるとき、またはスクロールの監視先がずれるときに見る。
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIChatContent.#jumpButton()
- 位置: L507-509
- 役割: 最下部へ戻るボタン（.jump-to-bottom-button）を返す。
- 触るとき: ボタンのクラス名を変えるとき、またはボタンが反応しないときに見る。
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIChatContent.#initScrollListener()
- 位置: L511-536
- 役割: 描画後にラッパーのスクロールと jump ボタンのクリックにハンドラーを付ける。
- 触るとき: スクロール監視の開始タイミングを変えるとき、または jump ボタンが効かないときに見る。
- 呼び出し先: `jumpButton.addEventListener()`, `this.updateComplete.then()`, `wrapper.addEventListener()`
- 参照: `this.#jumpButton`, `this.#jumpClickHandler`, `this.#scrollHandler`, `this.#wrapper`, `this.isConnected`

## this.#scrollHandler()
- 位置: L521-529
- 役割: スクロール時に次のフレームで jump ボタンの状態を更新するよう予約する（同フレームの重複は捨てる）。
- 触るとき: スクロール中のボタン表示が遅れる・重すぎるといった性能や表示の問題を見るときに見る。
- 呼び出し先: `requestAnimationFrame()`, `this.#updateJumpButtonState()`
- 参照: `this.#scrollRafId`

## this.#jumpClickHandler()
- 位置: L530-532
- 役割: ラッパーの scrollTop を最下部へ移す。
- 触るとき: ラッパーを最下部へ瞬間的に移す。最下部への移動方法を変えるとき、または jump ボタンを押しても移動しないときに見る。
- 参照: `wrapper.scrollHeight`, `wrapper.scrollTop`

## AIChatContent.#updateJumpButtonState()
- 位置: L538-556
- 役割: 下端からの距離が高さの半分を超えたら jump ボタンを表示し、最下部なら scrolled-to-bottom を付ける。
- 触るとき: ボタンを出す距離の閾値を変えるとき、または最下部判定がずれるときに見る。
- 呼び出し先: `jumpButton.hasAttribute()`, `wrapper.hasAttribute()`
- 条件付き依存: `if (jumpButton.hasAttribute("visible") !== show)` → `jumpButton.toggleAttribute()`
- 条件付き依存: `if (wrapper.hasAttribute("scrolled-to-bottom") !== atBottom)` → `wrapper.toggleAttribute()`
- 参照: `this.#jumpButton`, `this.#wrapper`, `wrapper.clientHeight`, `wrapper.scrollHeight`, `wrapper.scrollTop`

## AIChatContent.#teardownScrollListener()
- 位置: L558-571
- 役割: 保留中のフレーム要求と、スクロールと jump ボタンのリスナーを外す。
- 触るとき: 要素を外した後にスクロールのリスナーや予約が残る不具合を見るときに見る。
- 条件付き依存: `if (this.#scrollRafId)` → `cancelAnimationFrame()`
- 条件付き依存: `if (this.#scrollHandler)` → `this.#wrapper?.removeEventListener()`
- 条件付き依存: `if (this.#jumpClickHandler)` → `this.#jumpButton?.removeEventListener()`
- 参照: `this.#jumpClickHandler`, `this.#scrollHandler`, `this.#scrollRafId`

## AIChatContent.#getAssistantMessageBody()
- 位置: L573-583
- 役割: messageId に一致するアシスタント発言の本文を返し、無ければ空文字を返す。
- 触るとき: コピー対象の本文の取り方を変えるとき、またはコピーが空になるときに見る。
- 呼び出し先: `this.conversationState.find()`
- 参照: `m?.messageId`, `m?.role`, `msg?.body`

## AIChatContent.#onFollowUpSelected()
- 位置: L585-594
- 役割: 選ばれた提案の文を AIChatContent:DispatchFollowUp で送り、提案一覧を空にする。
- 触るとき: フォローアップ提案の送信内容を変えるとき、または提案を押しても送信されないときに見る。
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `event.detail.text`, `this.followUpSuggestions`

## AIChatContent.#handleSeenUrls()
- 位置: L604-611
- 役割: 会話 ID が同じなら既出 URL を結合し、違えば会話 ID と既出 URL を入れ替える。
- 触るとき: 会話切り替え時に既出 URL が前の会話から残る、または混ざるときに見る。
- 条件付き依存: `if (this.conversationId == conversationId)` → `this.seenUrls.union()`
- 参照: `this.conversationId`, `this.seenUrls`

## AIChatContent.messageEvent()
- 位置: L613-658
- 役割: アクターからのメッセージを role ごとに振り分け、読み込み・応答・ツール・ユーザー・完了・復元・クリアの各処理へ渡す。
- 触るとき: 新しい role を追加するとき、または会話イベントが誤った処理に入るときに見る。
- 呼び出し先: `this.#checkConversationState()`, `this.#restoreChatScrollPosition()`, `this.#setMessageComplete()`, `this.handleAIResponseEvent()`, `this.handleLoadingEvent()`, `this.handleToolMessageEvent()`, `this.handleUserPromptEvent()`
- 条件付き依存: `if (!message || typeof message !== "object")` → `dispatchClientError()`
- 条件付き依存: `if (message?.content?.isError)` → `this.handleErrorEvent()`
- 参照: `event.detail`, `message.convId`, `message.role`, `message?.content`, `message?.content?.isError`, `this.errorObj`

## AIChatContent.#handleSetGenerating()
- 位置: L660-666
- 役割: 生成中フラグを更新し、生成が止まったら検索中フラグを落として再描画する。
- 触るとき: 生成中の表示（読み込み表示や停止）が残る不具合を調べるときに見る。
- 呼び出し先: `this.requestUpdate()`
- 参照: `event.detail?.isGenerating`, `this.assistantIsLoading`, `this.isSearching`

## AIChatContent.#handleAssetsReady()
- 位置: L678-745
- 役割: 親が解決したサムネイルとファビコン状態を履歴結果と引用元へ反映し、変化があれば再描画する。
- 触るとき: 履歴グリッドの画像や引用元のファビコンが更新されないときに見る。
- 呼び出し先: `this.conversationState.find()`, `this.requestUpdate()`
- 条件付き依存: `if (entry.historyResultsMap)` → `entry.historyResultsMap.get()`
- 条件付き依存: `if (entry.citations?.length)` → `images.map()`
- 条件付き依存: `if (entry.citations?.length)` → `entry.citations.map()`
- 条件付き依存: `if (entry.citations?.length)` → `faviconByUrl.has()`
- 条件付き依存: `if (entry.citations?.length)` → `faviconByUrl.get()`
- 参照: `citation.hasFavicon`, `citation.url`, `entry.citations`, `entry.citations?.length`, `entry.historyResultsMap`, `event.detail`, `images?.length`, `msg?.messageId`, `record.hasFavicon`, `record.image`

## AIChatContent.#requestCitationFavicons()
- 位置: L753-773
- 役割: ファビコン状態が未確定の引用 URL をまとめて親へ問い合わせる。
- 触るとき: 引用元のファビコンが既定のまま変わらないときに見る。
- 呼び出し先: `citations .filter()`, `citations .filter(citation => citation?.url && citation.hasFavicon === undefined) .map()`, `this.dispatchEvent()`
- 参照: `citation.hasFavicon`, `citation.url`, `citation?.url`, `items.length`, `this.conversationId`

## AIChatContent.#restoreChatScrollPosition()
- 位置: async L775-824
- 役割: 保存していた会話のスクロール位置を復元し、末尾にいた場合や応答待ちの場合は最下部へ移す。
- 触るとき: 会話を開き直したときの位置がずれる、または最下部に行かないときに見る。
- 呼び出し先: `requestAnimationFrame()`, `this.#scrollPositions.get()`, `this.conversationState.findLast()`, `this.shadowRoot.querySelector()`, `wrapper.scrollTo()`
- 条件付き依存: `if (savedPosition?.contentHeight)` → `this.shadowRoot ?.querySelector(".chat-inner-wrapper") ?.style.setProperty()`
- 条件付き依存: `if (savedPosition?.contentHeight)` → `this.shadowRoot ?.querySelector()`
- 条件付き依存: `if (!goToBottom)` → `wrapper.scrollTo()`
- 条件付き依存: `if (lastChild)` → `lastChild.scrollIntoView()`
- 参照: `m.convId`, `savedPosition.contentHeight`, `savedPosition.scrollTop`, `savedPosition.wasAtBottom`, `savedPosition.wasWaitingForResponse`, `savedPosition?.contentHeight`, `this.#wrapper`, `this.shadowRoot.querySelector( ".chat-inner-wrapper" )?.lastElementChild`, `this.updateComplete`, `wrapper.scrollHeight`

## AIChatContent.#kitMention()
- 位置: L826-828
- 役割: 描画内の kit-mention 要素を取得する。
- 触るとき: kit-mention の初期化やリセットが効かないときに見る。
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIChatContent.#setMessageComplete()
- 位置: L830-859
- 役割: 完了メッセージに isLastChunk、履歴スナップショット、引用元を反映し、読み上げ用の待ち状態を立てる。
- 触るとき: 応答完了時の履歴や引用の固定の仕方を変えるとき、または完了後の読み上げが出ないときに見る。
- 呼び出し先: `this.conversationState.findLast()`, `this.requestUpdate()`
- 条件付き依存: `if (records?.length)` → `records.map()`
- 条件付き依存: `if (message.citations?.length)` → `this.#requestCitationFavicons()`
- 参照: `assistantLastMessage.citations`, `assistantLastMessage.historyResultsMap`, `assistantLastMessage.isLastChunk`, `message.citations`, `message.citations?.length`, `message.content?.id`, `message.historyResults`, `msg?.messageId`, `record.url`, `records?.length`, `this.#pendingAnnouncementMessageId`, `this.assistantResponseAnnouncement`

## AIChatContent.#clearAssistantResponseAnnouncement()
- 位置: L861-864
- 役割: 読み上げ待ちの ID と読み上げ用の文言を空に戻す。
- 触るとき: 読み上げが古い応答を読んでしまう、または読み上げが消えないときに見る。
- 参照: `this.#pendingAnnouncementMessageId`, `this.assistantResponseAnnouncement`

## AIChatContent.#checkConversationState()
- 位置: L871-901
- 役割: 会話 ID が変わったか同じ会話の再読込かを判定し、変わったら保存したスクロール位置を残して状態を空にする。
- 触るとき: 会話切り替え時に表示が残る、またはスクロール位置の保存が効かないときに見る。
- 呼び出し先: `this.conversationState.find()`, `this.conversationState.findLast()`
- 条件付き依存: `if (convIdChanged && lastMessage?.convId && this.#wrapper)` → `this.saveScrollPosition()`
- 条件付き依存: `if (convIdChanged || isReloadingSameConvo)` → `this.#clearAssistantResponseAnnouncement()`
- 条件付き依存: `if (convIdChanged || isReloadingSameConvo)` → `this.#kitMention?.reset()`
- 条件付き依存: `if (convIdChanged)` → `this.shadowRoot ?.querySelector(".chat-inner-wrapper") ?.style.removeProperty()`
- 条件付き依存: `if (convIdChanged)` → `this.shadowRoot ?.querySelector()`
- 条件付き依存: `if (convIdChanged || isReloadingSameConvo)` → `this.requestUpdate()`
- 参照: `firstMessage.convId`, `firstMessage.ordinal`, `lastMessage?.convId`, `message.convId`, `message.ordinal`, `this.#wrapper`, `this.conversationState`, `this.followUpSuggestions`, `this.isSearching`

## AIChatContent.saveScrollPosition()
- 位置: L904-930
- 役割: 末尾付近にいたか、応答待ちかを判定し、会話 ID ごとにスクロール位置を保存する。
- 触るとき: 会話を切り替えて戻ったときの位置がずれるときに見る。末尾判定の 50px を変えるとき、もここを見る。
- 呼び出し先: `innerWrapper?.style.getPropertyValue()`, `this.#scrollPositions.set()`, `this.shadowRoot.querySelector()`
- 条件付き依存: `if (lastChild)` → `lastChild.getBoundingClientRect()`
- 条件付き依存: `if (lastChild)` → `wrapper.getBoundingClientRect()`
- 参照: `innerWrapper?.lastElementChild`, `lastChildRect.bottom`, `lastMessage.convId`, `lastMessage.isLastChunk`, `lastMessage.role`, `this.assistantIsLoading`, `this.isSearching`, `wrapper.scrollTop`, `wrapperRect.bottom`

## AIChatContent.handleLoadingEvent()
- 位置: L932-937
- 役割: 読み上げ待ちを消し、検索中フラグを読み込みイベントの値で更新して再描画する。
- 触るとき: 検索中の表示が切り替わらないとき、または読み込みイベントの形を変えるときに見る。
- 呼び出し先: `this.#clearAssistantResponseAnnouncement()`, `this.requestUpdate()`
- 参照: `event.detail`, `this.isSearching`

## AIChatContent.handleErrorEvent()
- 位置: L939-943
- 役割: 検索中を解除し、受け取ったエラーを errorObj に入れて再描画する。
- 触るとき: エラー表示が出ない、または古いエラーが残るときに見る。
- 呼び出し先: `this.requestUpdate()`
- 参照: `this.errorObj`, `this.isSearching`

## AIChatContent.handleToolMessageEvent()
- 位置: L950-975
- 役割: action-log 種別のツール結果だけを、そのメッセージ位置の状態として登録する。
- 触るとき: 操作ログの表示対象を増やすとき、またはツールの結果が一覧に出ないときに見る。
- 呼び出し先: `ACCEPTED_UI_TYPES.includes()`, `this.requestUpdate()`
- 参照: `UI_TYPES.ACTION_LOG`, `actionLog.pendingLabel`, `actionLog.row`, `actionLog.uiType`, `actionLog?.uiType`, `content.name`, `content.tool_call_id`, `content?.name`, `event.detail`, `this.conversationState`

## AIChatContent.handleUserPromptEvent()
- 位置: L983-1001
- 役割: ユーザー発言を会話の位置へ登録し、既存でなければ読み上げ待ちを消して末尾へスクロールする。
- 触るとき: ユーザー発言の登録内容を変えるとき、または送信後の位置がずれるときに見る。
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (!isPreviousMessage)` → `this.#clearAssistantResponseAnnouncement()`
- 条件付き依存: `if (!isPreviousMessage)` → `this.#scrollUserMessageIntoView()`
- 参照: `content.body`, `content.contextMentions`, `content.contextPageUrl`, `event.detail`, `this.conversationState`, `this.followUpSuggestions`

## AIChatContent.retryUserMessageAfterError()
- 位置: L1003-1018
- 役割: 直前のメッセージを本文とメンション付きで retry-after-error として送り直す。
- 触るとき: エラー後の再試行で送る内容を変えるとき、または再試行の本文が欠けるときに見る。
- 呼び出し先: `this.#dispatchAction()`, `this.conversationState.findLast()`
- 参照: `lastMessage.body`, `lastMessage.contextMentions`

## AIChatContent.#isAIResponseValid()
- 位置: L1020-1026
- 役割: 本文が文字列、翻訳 ID、またはツール UI データのいずれかがあれば表示可能と判定する。
- 触るとき: 空の応答を表示対象から外す条件を変えるときに見る。
- 参照: `content.body`, `content?.body`, `content?.l10nId`

## AIChatContent.handleAIResponseEvent()
- 位置: L1034-1111
- 役割: 応答を会話の位置へ登録する。履歴と引用を組み、追加の提案、キットの起動、ツール UI の削除を判断する。
- 触るとき: アシスタント応答で表示される項目（メモリー、履歴、提案、ツール UI）を増やすとき、または応答の一部が表示されないときに見る。
- 呼び出し先: `followUpSuggestions.slice()`, `historyResults.map()`, `this.#isAIResponseValid()`, `this.requestUpdate()`
- 条件付き依存: `if (isToolUICleared)` → `this.conversationState.filter()`
- 条件付き依存: `if (citations.length)` → `this.#requestCitationFavicons()`
- 条件付き依存: `if (kit && !isPreviousMessage)` → `this.#kitMention?.trigger()`
- 参照: `citations.length`, `content.body`, `content.l10nArgs`, `content.l10nId`, `content.link`, `event.detail`, `historyResults.length`, `message.messageId`, `message.toolUIData`, `record.url`, `this.conversationState`, `this.conversationState[ordinal]?.isLastChunk`, `this.followUpSuggestions`, `this.isSearching`, `webSearchQueries.length`

## AIChatContent.#scrollUserMessageIntoView()
- 位置: L1113-1139
- 役割: 最後のユーザー発言を先頭へ合わせ、後続の要求で上書きされたら中断する。
- 触るとき: 送信後の自動スクロール位置を変えるとき、またはスクロールが途中で止まるときに見る。
- 呼び出し先: `lastMessage.parentNode.style.setProperty()`, `requestAnimationFrame()`, `this.shadowRoot?.querySelectorAll()`, `this.updateComplete.then()`
- 条件付き依存: `if (scrollReq == this.#lastScrollReq)` → `lastMessage.scrollIntoView()`
- 参照: `lastMessage.offsetTop`, `msgs.length`, `msgs?.length`, `this.#lastScrollReq`

## AIChatContent.truncateEvent()
- 位置: L1141-1157
- 役割: 指定の応答より後ろの会話状態を削除する。
- 触るとき: 途中から会話を切り詰めるときに、どこまで残るかを確認するときに見る。
- 呼び出し先: `this.conversationState.findIndex()`, `this.conversationState.slice()`, `this.requestUpdate()`
- 参照: `event.detail`, `m?.messageId`, `m?.role`, `this.conversationState`

## AIChatContent.removeAppliedMemoryEvent()
- 位置: L1159-1169
- 役割: 該当応答の適用メモリーから指定 ID のものを外して再描画する。
- 触るとき: メモリー削除の表示が残るときに見る。該当応答が無いと例外になるので注意。
- 呼び出し先: `msg.appliedMemories.filter()`, `this.conversationState.find()`, `this.requestUpdate()`
- 参照: `event.detail`, `m?.messageId`, `m?.role`, `memory?.id`, `msg.appliedMemories`

## AIChatContent.openNewChatAfterError()
- 位置: L1171-1177
- 役割: AIChatContent:DispatchNewChat を発火し、新しいチャットを開くよう親に伝える。
- 触るとき: エラー後の新規チャット導線を変えるときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#getVisibleChips()
- 位置: L1189-1203
- 役割: ユーザー発言の文脈チップのうち、タブグループの所属を除き、同じページなら現在ページの chip を隠す。
- 触るとき: 文脈チップの表示条件を変えるとき、または同じページの chip が重複するときに見る。
- 呼び出し先: `isTabGroupMember()`, `msg.contextMentions.filter()`
- 条件付き依存: `if (shouldHideDuplicatePageChip)` → `chips.filter()`
- 条件付き依存: `if (shouldHideDuplicatePageChip)` → `URL.parse()`
- 参照: `URL.parse(chip.url)?.href`, `chip.url`, `msg.contextMentions?.length`, `msg.pageUrl`, `msg.role`

## AIChatContent.openAccountSignInAfterError()
- 位置: L1205-1211
- 役割: AIChatContent:AccountSignIn を発火し、サインインを親に依頼する。
- 触るとき: エラー後のサインイン導線を変えるとき、またはサインインが始まらないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#buildTabsRow()
- 位置: L1213-1222
- 役割: タブ配列が空でなければ、ラベル ID とタブの URL・タイトルを 1 行分にまとめる。
- 触るとき: タブ一覧の行の作り方を変えるとき、またはタブが一覧に出ないときに見る。
- 呼び出し先: `tabs.map()`
- 参照: `tab.title`, `tab.url`, `tabs.length`

## AIChatContent.#getCloseTabsData()
- 位置: L1224-1240
- 役割: 閉じたタブの件数とタブ行から、閉じた結果のラベルと要約（翻訳 ID と件数）を組み立てる。
- 触るとき: タブを閉じた後の結果表示の文言や行の内容を変えるとき、または件数がずれるときに見る。
- 呼び出し先: `this.#buildTabsRow()`
- 参照: `confirmedData.selectedTabs`, `selectedTabs.length`

## AIChatContent.#getRestoreTabsData()
- 位置: L1242-1266
- 役割: 元に戻したタブの件数から、閉じたタブ行と復元済み行を持つ結果を組み立てる。
- 触るとき: 閉じたタブを元に戻した後の表示（行の構成や文言）を変えるときに見る。
- 呼び出し先: `originalClosedTabs.map()`
- 参照: `originalClosedTabs.length`

## AIChatContent.#getGroupTabsData()
- 位置: L1268-1290
- 役割: グループ化した結果の件数（グループ全体の件数を優先）と要約を組み立てる。
- 触るとき: タブのグループ化結果の文言や件数の出し方を変えるとき、または件数が選択数とずれるときに見る。
- 呼び出し先: `this.#buildTabsRow()`
- 参照: `confirmedData.group`, `confirmedData.selectedTabs`, `group.label`, `group.tabCount`, `selectedTabs.length`, `this.#defaultTabGroupLabel`

## AIChatContent.#getSwitchedTabData()
- 位置: L1292-1299
- 役割: 既に開いていたタブへ切り替えた結果を、タイトルか URL を使った要約で返す。
- 触るとき: 既存タブへの切り替え結果の文言を変えるとき、または切り替えの表示が出ないときに見る。
- 参照: `tab?.title`, `tab?.url`

## AIChatContent.#getOpenTabsData()
- 位置: L1301-1339
- 役割: 切り替え、全て既存タブ、新規開き・グループ化の 3 通りに分けて開くタブの結果を組み立てる。
- 触るとき: タブを開く操作の結果表示の分岐を変えるとき、または要約の文言が状況に合わないときに見る。
- 呼び出し先: `this.#buildTabsRow()`
- 条件付き依存: `if (confirmedData.switched)` → `this.#getSwitchedTabData()`
- 条件付き依存: `if (tabCount && confirmedData.mergedCount === tabCount)` → `this.#getGroupTabsData()`
- 参照: `confirmedData.group`, `confirmedData.mergedCount`, `confirmedData.selectedTabs`, `confirmedData.switched`, `group.label`, `selectedTabs.length`, `this.#defaultTabGroupLabel`

## AIChatContent.#getUngroupedTabsData()
- 位置: L1341-1367
- 役割: グループ解除の結果として、元のグループ行と解除済み件数の行を組み立てる。
- 触るとき: グループ解除後の表示の行構成や文言を変えるとき、または行の件数が合わないときに見る。
- 呼び出し先: `originalGroupedTabs.map()`
- 参照: `originalGroupedTabs.length`

## AIChatContent.#getActionResultData()
- 位置: L1369-1391
- 役割: アクション種別と復元の有無から、対応する結果データ生成関数を選んで呼ぶ。
- 触るとき: 新しいアクション種別を足すとき、または復元時の表示が通常の結果と取り違えられるときに見る。
- 呼び出し先: `method()`, `this.#getCloseTabsData()`, `this.#getGroupTabsData()`, `this.#getRestoreTabsData()`, `this.#getUngroupedTabsData()`
- 参照: `confirmedData.actionType`, `confirmedData.originalClosedTabs`, `confirmedData.originalGroupedTabs`

## open_tabs()
- 位置: L1386-1386
- 役割: 開くタブの結果を組み立てる。取り消し対応は無いため、復元の分岐は持たない。
- 触るとき: open_tabs の結果表示を変えるとき、または取り消しボタンを付けるか検討するときに見る。
- 呼び出し先: `this.#getOpenTabsData()`

## AIChatContent.#renderActionLogGroup()
- 位置: L1400-1421
- 役割: 1 ターンのツール呼び出しを、まとめた ai-action-result として描画し、展開状態を覚えておく。
- 触るとき: 操作ログのまとめ方や展開状態の保持を変えるときに見る。
- 呼び出し先: `html()`, `this.#actionResultExpandState.get()`, `this.#actionResultExpandState.set()`, `this.#buildGroupedActionLogRows()`
- 参照: `e.detail?.isExpanded`, `summary?.l10nArgs`, `summary?.l10nId`, `summary?.link`, `toolMsgs.length`, `toolMsgs[0]?.id`, `toolMsgs[0]?.messageId`, `toolMsgs[toolMsgs.length - 1]?.pendingLabel`

## AIChatContent.#renderToolUI()
- 位置: L1429-1448
- 役割: 復元された確認 UI は再試行用に差し替え、uiType に対応する描画関数を呼ぶ。
- 触るとき: ツール UI の描画を振り分ける条件を変えるとき、または復元された確認カードの表示を調べるときに見る。
- 呼び出し先: `CONFIRMATION_UI_TYPES.includes()`, `renderFn()`
- 参照: `UI_TYPES.RETRY_COMPONENT`, `msg.isRestored`, `msg.toolUIData`, `this.#uiRenderMap`, `toolUIData.properties`, `toolUIData.uiType`

## AIChatContent.#renderAITab()
- 位置: L1450-1462
- 役割: aitab-tool-ui を描画し、タブを開く要求を親へ updateType 付きで送る。
- 触るとき: AI タブのカードの状態や開く要求の内容を変えるとき、に見る。
- 呼び出し先: `html()`, `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.OPEN_AITAB`, `event.detail.openTarget`, `msg.messageId`, `msg.toolUIData.properties?.state`, `msg.toolUIData.properties?.title`, `msg.toolUIData.toolCallId`

## AIChatContent.#handleConfirmationSubmit()
- 位置: L1464-1471
- 役割: サイト確認の送信内容を、タブ選択の更新として親へ送る。
- 触るとき: サイトの確認カードで送信した選択が親に反映されないときに見る。
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CONFIRMATION_TAB_SELECTION`, `event.detail`

## AIChatContent.#handleConfirmationClose()
- 位置: L1473-1480
- 役割: 確認カードを閉じた操作を、タブ選択のキャンセルとして親へ送る。
- 触るとき: 確認カードを閉じた後の処理を変えるとき、または閉じても何も起きないときに見る。
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CANCEL_TAB_SELECTION`, `event.detail`

## AIChatContent.#handleMonitorSubmit()
- 位置: L1482-1494
- 役割: 監視カードの送信を、表示モードに応じて監視の更新か作成として親へ送る。
- 触るとき: 監視の作成と編集の判定を変えるとき、または送信が逆の処理になるときに見る。
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CREATE_WATCH`, `UI_UPDATE_TYPES.UPDATE_WATCH`, `event.detail`, `event.detail?.mode`

## AIChatContent.#handleMonitorCancel()
- 位置: L1496-1504
- 役割: 監視カードのキャンセルを監視のキャンセルとして親へ送る。
- 触るとき: キャンセル時の処理を変えるとき、またはキャンセルが親に届かないときに見る。
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CANCEL_WATCH`, `event.detail`

## AIChatContent.#handleMonitorAction()
- 位置: L1506-1513
- 役割: 監視カードの操作を、渡された更新種別のまま親へ送る。
- 触るとき: 保存、削除、一時停止、今すぐ確認などの操作の対応を変えるときに見る。
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `event.detail`

## AIChatContent.#renderAgentMonitorComponent()
- 位置: L1515-1556
- 役割: agent-monitor-item を描画し、下書き変更、送信、キャンセル、削除、一時停止、今すぐ確認の各イベントを親へ渡す。
- 触るとき: 監視カードの操作を増やすとき、またはカードのイベントが親に届かないときに見る。
- 呼び出し先: `html()`, `this.#handleMonitorAction()`, `this.#handleMonitorCancel()`, `this.#handleMonitorSubmit()`
- 参照: `UI_UPDATE_TYPES.CHECK_WATCH`, `UI_UPDATE_TYPES.DELETE_WATCH`, `UI_UPDATE_TYPES.PAUSE_WATCH`, `UI_UPDATE_TYPES.SAVE_WATCH_DRAFT`, `toolUIData.properties?.agent`, `toolUIData.properties?.mode`, `toolUIData.toolCallId`

## AIChatContent.#handleTabGroupActionSubmit()
- 位置: L1558-1565
- 役割: タブグループ確認の送信を、渡された更新種別のまま親へ送る。
- 触るとき: タブグループ確認の送信内容を変えるとき、または送信が親に届かないときに見る。
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `event.detail`

## AIChatContent.#renderTabGroupConfirmation()
- 位置: L1567-1594
- 役割: ツールの actionType に応じた確認文言と更新種別を選び、ai-website-confirmation を描画する。
- 触るとき: タブグループの確認カードの文言や送信の対応を変えるとき、または actionType 別の表示を足すときに見る。
- 呼び出し先: `html()`, `this.#handleConfirmationClose()`, `this.#handleTabGroupActionSubmit()`
- 参照: `TAB_GROUP_ACTION_CONFIG.group_tabs`, `msg.messageId`, `msg.toolUIData`, `toolUIData.properties?.actionType`, `toolUIData.properties?.tabGroupLabel`, `toolUIData.properties?.tabs`, `toolUIData.toolCallId`

## AIChatContent.#renderWebsiteConfirmation()
- 位置: L1596-1621
- 役割: 閉じるタブの確認カードを描画し、送信と閉じるの操作を親へ渡す。
- 触るとき: タブを閉じる確認カードの文言や操作を変えるときに見る。
- 呼び出し先: `html()`, `this.#handleConfirmationClose()`, `this.#handleConfirmationSubmit()`
- 参照: `msg.messageId`, `msg.toolUIData`, `toolUIData.properties?.tabs`, `toolUIData.toolCallId`

## AIChatContent.#renderActionResult()
- 位置: L1623-1680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#actionResultExpandState.get()`, `this.#actionResultExpandState.set()`, `this.#dispatchToolUIUpdate()`, `this.#getActionResultData()`, `this.#getConfirmationTabs()`
- 参照: `actionResultData.labelL10nArgs`, `actionResultData.labelL10nId`, `confirmedData.actionTimestamp`, `confirmedData.actionType`, `confirmedData.operationIds`, `confirmedData.selectedTabs`, `confirmedData.wasRestored`, `e.detail.isExpanded`, `toolUIData.properties?.confirmedData`, `toolUIData.properties?.undoDismissed`, `toolUIData.toolCallId`, `undoOperationIds.length`

## AIChatContent.#getConfirmationTabs()
- 位置: L1689-1702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(sourceTabs ?? []).map()`
- 参照: `confirmedData.actionType`, `confirmedData.originalClosedTabs`, `confirmedData.originalGroupedTabs`, `confirmedData.selectedTabs`, `tab.iconSrc`, `tab.title`, `tab.url`

## AIChatContent.#renderCancelledComponent()
- 位置: L1704-1706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## AIChatContent.#renderRetryComponent()
- 位置: L1708-1730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handleRetryClick()`
- 参照: `msg.messageId`, `msg.toolUIData`, `msg.toolUIData?.properties?.cancelledUiType`, `toolUIData.properties?.originalUserPrompt`, `toolUIData.toolCallId`

## AIChatContent.#handleRetryClick()
- 位置: L1732-1739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.RETRY_PROMPT`

## AIChatContent.#dispatchToolUIUpdate()
- 位置: L1741-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#renderMessage()
- 位置: L1751-1804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderToolUI()`
- 参照: `UI_TYPES.RETRY_COMPONENT`, `chips?.length`, `msg.appliedMemories`, `msg.body`, `msg.citations`, `msg.citations?.length`, `msg.historyResultsMap`, `msg.isLastChunk`, `msg.messageId`, `msg.messageL10n`, `msg.role`, `msg.showCallout`, `msg.toolUIData`, `msg.toolUIData?.isResumeActivity`, `msg.toolUIData?.uiType`, `this.conversationId`, `this.seenUrls`

## AIChatContent.#renderFollowUpSuggestions()
- 位置: L1806-1817
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.followUpSuggestions.map()`
- 参照: `this.followUpSuggestions?.length`

## AIChatContent.#renderLoader()
- 位置: L1819-1830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.assistantIsLoading`, `this.isSearching`

## AIChatContent.#renderError()
- 位置: L1832-1839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.errorObj`

## AIChatContent.#buildTurnRenderItems()
- 位置: L1851-1939
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appendPendingAssistantTurn()`, `items.push()`
- 条件付き依存: `if (msg.uiType === UI_TYPES.ACTION_LOG)` → `pendingActionLogs.push()`
- 条件付き依存: `if (pendingAssistantMessage)` → `appendPendingAssistantTurn()`
- 参照: `UI_TYPES.ACTION_LOG`, `msg.pageUrl`, `msg.role`, `msg.uiType`, `pendingAssistantMessage?.body`, `this.assistantIsLoading`, `this.conversationState`

## appendPendingAssistantTurn()
- 位置: L1862-1889
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pendingActionLogs.length)` → `items.push()`
- 条件付き依存: `if (pendingAssistantMessage)` → `items.push()`
- 参照: `pendingActionLogs.length`

## AIChatContent.#buildGroupedActionLogRows()
- 位置: L1947-1949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolMsgs.map()`, `toolMsgs.map(msg => msg.row).filter()`
- 参照: `msg.row`

## AIChatContent.#renderMessages()
- 位置: L1951-1965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `repeat()`, `this.#getVisibleChips()`, `this.#renderItemKey()`, `this.#renderMessage()`
- 条件付き依存: `if (type === "action-log")` → `this.#renderActionLogGroup()`

## AIChatContent.#renderItemKey()
- 位置: L1967-1974
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `first?.messageId`, `first?.toolCallId`, `item.msgs`, `item.type`, `msg?.convId`, `msg?.ordinal`

## AIChatContent.render()
- 位置: L1976-2027
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `renderItems.at()`, `renderItems.some()`, `this.#buildTurnRenderItems()`, `this.#renderError()`, `this.#renderFollowUpSuggestions()`, `this.#renderLoader()`, `this.#renderMessages()`
- 参照: `UI_TYPES.AITAB`, `item.isComplete`, `item.type`, `lastItem.msg.toolUIData.properties?.state`, `lastItem.msg?.body`, `lastItem.msg?.role`, `lastItem.msg?.toolUIData?.uiType`, `lastItem?.type`, `this.assistantResponseAnnouncement`
