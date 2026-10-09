# browser/components/aiwindow/ui/components/ai-chat-content/ai-chat-content.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/ai-chat-content.mjs
source-hash: dc75ea5e2228ceb26270cf05b4807cd1280548df
lines: 2031

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIChatContent.constructor()
- 位置: L166-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `UI_TYPES.AGENT_MONITOR`, `UI_TYPES.AITAB`, `UI_TYPES.AI_ACTION_RESULT`, `UI_TYPES.CANCELLED_COMPONENT`, `UI_TYPES.RETRY_COMPONENT`, `UI_TYPES.TAB_GROUP_CONFIRMATION`, `UI_TYPES.WEBSITE_CONFIRMATION`, `this.#uiRenderMap`, `this.assistantIsLoading`, `this.assistantResponseAnnouncement`, `this.conversationId`, `this.conversationState`, `this.errorObj`, `this.followUpSuggestions`, `this.isSearching`, `this.seenUrls`

## [UI_TYPES.AITAB]()
- 位置: L177-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderAITab()`

## [UI_TYPES.TAB_GROUP_CONFIRMATION]()
- 位置: L178-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderTabGroupConfirmation()`

## [UI_TYPES.WEBSITE_CONFIRMATION]()
- 位置: L180-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderWebsiteConfirmation()`

## [UI_TYPES.AI_ACTION_RESULT]()
- 位置: L182-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderActionResult()`

## [UI_TYPES.CANCELLED_COMPONENT]()
- 位置: L183-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderCancelledComponent()`

## [UI_TYPES.RETRY_COMPONENT]()
- 位置: L184-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderRetryComponent()`

## [UI_TYPES.AGENT_MONITOR]()
- 位置: L185-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderAgentMonitorComponent()`

## AIChatContent.connectedCallback()
- 位置: L204-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchClientError()`, `installClientErrorListeners()`, `super.connectedCallback()`, `this.#initEventListeners()`, `this.#initFooterActionListeners()`, `this.#initOverflowObserver()`, `this.#initScrollListener()`, `this.#scrollPositions.clear()`, `this.dispatchEvent()`, `this.ownerDocument.l10n .formatValue()`, `this.ownerDocument.l10n .formatValue("smart-window-default-tab-group-label") .then()`
- 条件付き依存: `if (label)` → `this.requestUpdate()`
- 参照: `this.#defaultTabGroupLabel`, `this.#removeClientErrorListeners`

## AIChatContent.disconnectedCallback()
- 位置: L231-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#overflowObserver?.disconnect()`, `this.#removeClientErrorListeners()`, `this.#teardownScrollListener()`
- 条件付き依存: `if (this.#overflowRafId)` → `cancelAnimationFrame()`
- 参照: `this.#overflowObserver`, `this.#overflowRafId`, `this.#removeClientErrorListeners`

## AIChatContent.updated()
- 位置: L244-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updated()`, `this.#maybeFocusAgentMonitorCard()`

## AIChatContent.#maybeFocusAgentMonitorCard()
- 位置: L253-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#focusMonitorNameInput()`, `this.conversationState.findLast()`
- 参照: `UI_TYPES.AGENT_MONITOR`, `card.messageId`, `card.toolUIData.toolCallId`, `msg.isRestored`, `msg.toolUIData.properties?.mode`, `msg?.toolUIData?.uiType`, `this.#focusedMonitorCardId`

## AIChatContent.#focusMonitorNameInput()
- 位置: async L271-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `item.getAttribute()`, `this.shadowRoot?.querySelector()`
- 条件付き依存: `if (item.isConnected && item.getAttribute("mode") === "create")` → `item.focusName()`
- 参照: `item.isConnected`, `item.updateComplete`

## AIChatContent.#dispatchAction()
- 位置: L285-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#handleSetMode()
- 位置: L300-305
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (mode)` → `this.setAttribute()`
- 参照: `event.detail?.mode`

## AIChatContent.#initEventListeners()
- 位置: L310-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleAssetsReady.bind()`, `this.#handleSeenUrls.bind()`, `this.#handleSetGenerating.bind()`, `this.#handleSetMode.bind()`, `this.#onFollowUpSelected.bind()`, `this.addEventListener()`, `this.messageEvent.bind()`, `this.openAccountSignInAfterError.bind()`, `this.openNewChatAfterError.bind()`, `this.removeAppliedMemoryEvent.bind()`, `this.retryUserMessageAfterError.bind()`, `this.truncateEvent.bind()`
- 参照: `event.detail`, `this.#pendingAnnouncementMessageId`, `this.assistantResponseAnnouncement`

## AIChatContent.#initFooterActionListeners()
- 位置: L380-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text .split()`, `text .split("\n") .slice()`, `text .split("\n") .slice(lineRange[0], lineRange[1]) .join()`, `this.#dispatchAction()`, `this.#getAssistantMessageBody()`, `this.addEventListener()`
- 参照: `event.detail`, `this.#onPanelShown`

## AIChatContent.#onPanelShown()
- 位置: L435-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `event.composedPath()`, `panel.getAttribute()`, `panel.getBoundingClientRect()`, `parseFloat()`, `this.#topSpacing()`
- 参照: `bounds.height`, `bounds.top`, `panel.style.maxHeight`, `panel.style.top`, `panel?.localName`, `window.innerHeight`

## AIChatContent.#topSpacing()
- 位置: L457-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getComputedStyle()`, `parseFloat()`, `this.shadowRoot?.querySelector()`
- 参照: `getComputedStyle(innerWrapper).paddingBlockStart`

## AIChatContent.#initOverflowObserver()
- 位置: L465-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#overflowObserver.observe()`, `this.#updateOverflowState()`, `this.shadowRoot.querySelector()`, `this.updateComplete.then()`
- 参照: `this.#overflowObserver`

## AIChatContent.#updateOverflowState()
- 位置: L482-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateJumpButtonState()`, `this.shadowRoot?.querySelector()`, `wrapper.toggleAttribute()`
- 参照: `innerWrapper.children.length`, `this.#wrapper`, `wrapper.clientHeight`, `wrapper.scrollHeight`

## AIChatContent.#wrapper()
- 位置: L503-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIChatContent.#jumpButton()
- 位置: L507-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIChatContent.#initScrollListener()
- 位置: L511-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `jumpButton.addEventListener()`, `this.updateComplete.then()`, `wrapper.addEventListener()`
- 参照: `this.#jumpButton`, `this.#jumpClickHandler`, `this.#scrollHandler`, `this.#wrapper`, `this.isConnected`

## this.#scrollHandler()
- 位置: L521-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `this.#updateJumpButtonState()`
- 参照: `this.#scrollRafId`

## this.#jumpClickHandler()
- 位置: L530-532
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `wrapper.scrollHeight`, `wrapper.scrollTop`

## AIChatContent.#updateJumpButtonState()
- 位置: L538-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `jumpButton.hasAttribute()`, `wrapper.hasAttribute()`
- 条件付き依存: `if (jumpButton.hasAttribute("visible") !== show)` → `jumpButton.toggleAttribute()`
- 条件付き依存: `if (wrapper.hasAttribute("scrolled-to-bottom") !== atBottom)` → `wrapper.toggleAttribute()`
- 参照: `this.#jumpButton`, `this.#wrapper`, `wrapper.clientHeight`, `wrapper.scrollHeight`, `wrapper.scrollTop`

## AIChatContent.#teardownScrollListener()
- 位置: L558-571
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#scrollRafId)` → `cancelAnimationFrame()`
- 条件付き依存: `if (this.#scrollHandler)` → `this.#wrapper?.removeEventListener()`
- 条件付き依存: `if (this.#jumpClickHandler)` → `this.#jumpButton?.removeEventListener()`
- 参照: `this.#jumpClickHandler`, `this.#scrollHandler`, `this.#scrollRafId`

## AIChatContent.#getAssistantMessageBody()
- 位置: L573-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.conversationState.find()`
- 参照: `m?.messageId`, `m?.role`, `msg?.body`

## AIChatContent.#onFollowUpSelected()
- 位置: L585-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `event.detail.text`, `this.followUpSuggestions`

## AIChatContent.#handleSeenUrls()
- 位置: L604-611
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.conversationId == conversationId)` → `this.seenUrls.union()`
- 参照: `this.conversationId`, `this.seenUrls`

## AIChatContent.messageEvent()
- 位置: L613-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#checkConversationState()`, `this.#restoreChatScrollPosition()`, `this.#setMessageComplete()`, `this.handleAIResponseEvent()`, `this.handleLoadingEvent()`, `this.handleToolMessageEvent()`, `this.handleUserPromptEvent()`
- 条件付き依存: `if (!message || typeof message !== "object")` → `dispatchClientError()`
- 条件付き依存: `if (message?.content?.isError)` → `this.handleErrorEvent()`
- 参照: `event.detail`, `message.convId`, `message.role`, `message?.content`, `message?.content?.isError`, `this.errorObj`

## AIChatContent.#handleSetGenerating()
- 位置: L660-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 参照: `event.detail?.isGenerating`, `this.assistantIsLoading`, `this.isSearching`

## AIChatContent.#handleAssetsReady()
- 位置: L678-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.conversationState.find()`, `this.requestUpdate()`
- 条件付き依存: `if (entry.historyResultsMap)` → `entry.historyResultsMap.get()`
- 条件付き依存: `if (entry.citations?.length)` → `images.map()`
- 条件付き依存: `if (entry.citations?.length)` → `entry.citations.map()`
- 条件付き依存: `if (entry.citations?.length)` → `faviconByUrl.has()`
- 条件付き依存: `if (entry.citations?.length)` → `faviconByUrl.get()`
- 参照: `citation.hasFavicon`, `citation.url`, `entry.citations`, `entry.citations?.length`, `entry.historyResultsMap`, `event.detail`, `images?.length`, `msg?.messageId`, `record.hasFavicon`, `record.image`

## AIChatContent.#requestCitationFavicons()
- 位置: L753-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `citations .filter()`, `citations .filter(citation => citation?.url && citation.hasFavicon === undefined) .map()`, `this.dispatchEvent()`
- 参照: `citation.hasFavicon`, `citation.url`, `citation?.url`, `items.length`, `this.conversationId`

## AIChatContent.#restoreChatScrollPosition()
- 位置: async L775-824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `this.#scrollPositions.get()`, `this.conversationState.findLast()`, `this.shadowRoot.querySelector()`, `wrapper.scrollTo()`
- 条件付き依存: `if (savedPosition?.contentHeight)` → `this.shadowRoot ?.querySelector(".chat-inner-wrapper") ?.style.setProperty()`
- 条件付き依存: `if (savedPosition?.contentHeight)` → `this.shadowRoot ?.querySelector()`
- 条件付き依存: `if (!goToBottom)` → `wrapper.scrollTo()`
- 条件付き依存: `if (lastChild)` → `lastChild.scrollIntoView()`
- 参照: `m.convId`, `savedPosition.contentHeight`, `savedPosition.scrollTop`, `savedPosition.wasAtBottom`, `savedPosition.wasWaitingForResponse`, `savedPosition?.contentHeight`, `this.#wrapper`, `this.shadowRoot.querySelector( ".chat-inner-wrapper" )?.lastElementChild`, `this.updateComplete`, `wrapper.scrollHeight`

## AIChatContent.#kitMention()
- 位置: L826-828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIChatContent.#setMessageComplete()
- 位置: L830-859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.conversationState.findLast()`, `this.requestUpdate()`
- 条件付き依存: `if (records?.length)` → `records.map()`
- 条件付き依存: `if (message.citations?.length)` → `this.#requestCitationFavicons()`
- 参照: `assistantLastMessage.citations`, `assistantLastMessage.historyResultsMap`, `assistantLastMessage.isLastChunk`, `message.citations`, `message.citations?.length`, `message.content?.id`, `message.historyResults`, `msg?.messageId`, `record.url`, `records?.length`, `this.#pendingAnnouncementMessageId`, `this.assistantResponseAnnouncement`

## AIChatContent.#clearAssistantResponseAnnouncement()
- 位置: L861-864
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pendingAnnouncementMessageId`, `this.assistantResponseAnnouncement`

## AIChatContent.#checkConversationState()
- 位置: L871-901
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `innerWrapper?.style.getPropertyValue()`, `this.#scrollPositions.set()`, `this.shadowRoot.querySelector()`
- 条件付き依存: `if (lastChild)` → `lastChild.getBoundingClientRect()`
- 条件付き依存: `if (lastChild)` → `wrapper.getBoundingClientRect()`
- 参照: `innerWrapper?.lastElementChild`, `lastChildRect.bottom`, `lastMessage.convId`, `lastMessage.isLastChunk`, `lastMessage.role`, `this.assistantIsLoading`, `this.isSearching`, `wrapper.scrollTop`, `wrapperRect.bottom`

## AIChatContent.handleLoadingEvent()
- 位置: L932-937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearAssistantResponseAnnouncement()`, `this.requestUpdate()`
- 参照: `event.detail`, `this.isSearching`

## AIChatContent.handleErrorEvent()
- 位置: L939-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 参照: `this.errorObj`, `this.isSearching`

## AIChatContent.handleToolMessageEvent()
- 位置: L950-975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ACCEPTED_UI_TYPES.includes()`, `this.requestUpdate()`
- 参照: `UI_TYPES.ACTION_LOG`, `actionLog.pendingLabel`, `actionLog.row`, `actionLog.uiType`, `actionLog?.uiType`, `content.name`, `content.tool_call_id`, `content?.name`, `event.detail`, `this.conversationState`

## AIChatContent.handleUserPromptEvent()
- 位置: L983-1001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (!isPreviousMessage)` → `this.#clearAssistantResponseAnnouncement()`
- 条件付き依存: `if (!isPreviousMessage)` → `this.#scrollUserMessageIntoView()`
- 参照: `content.body`, `content.contextMentions`, `content.contextPageUrl`, `event.detail`, `this.conversationState`, `this.followUpSuggestions`

## AIChatContent.retryUserMessageAfterError()
- 位置: L1003-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchAction()`, `this.conversationState.findLast()`
- 参照: `lastMessage.body`, `lastMessage.contextMentions`

## AIChatContent.#isAIResponseValid()
- 位置: L1020-1026
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `content.body`, `content?.body`, `content?.l10nId`

## AIChatContent.handleAIResponseEvent()
- 位置: L1034-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `followUpSuggestions.slice()`, `historyResults.map()`, `this.#isAIResponseValid()`, `this.requestUpdate()`
- 条件付き依存: `if (isToolUICleared)` → `this.conversationState.filter()`
- 条件付き依存: `if (citations.length)` → `this.#requestCitationFavicons()`
- 条件付き依存: `if (kit && !isPreviousMessage)` → `this.#kitMention?.trigger()`
- 参照: `citations.length`, `content.body`, `content.l10nArgs`, `content.l10nId`, `content.link`, `event.detail`, `historyResults.length`, `message.messageId`, `message.toolUIData`, `record.url`, `this.conversationState`, `this.conversationState[ordinal]?.isLastChunk`, `this.followUpSuggestions`, `this.isSearching`, `webSearchQueries.length`

## AIChatContent.#scrollUserMessageIntoView()
- 位置: L1113-1139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lastMessage.parentNode.style.setProperty()`, `requestAnimationFrame()`, `this.shadowRoot?.querySelectorAll()`, `this.updateComplete.then()`
- 条件付き依存: `if (scrollReq == this.#lastScrollReq)` → `lastMessage.scrollIntoView()`
- 参照: `lastMessage.offsetTop`, `msgs.length`, `msgs?.length`, `this.#lastScrollReq`

## AIChatContent.truncateEvent()
- 位置: L1141-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.conversationState.findIndex()`, `this.conversationState.slice()`, `this.requestUpdate()`
- 参照: `event.detail`, `m?.messageId`, `m?.role`, `this.conversationState`

## AIChatContent.removeAppliedMemoryEvent()
- 位置: L1159-1169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `msg.appliedMemories.filter()`, `this.conversationState.find()`, `this.requestUpdate()`
- 参照: `event.detail`, `m?.messageId`, `m?.role`, `memory?.id`, `msg.appliedMemories`

## AIChatContent.openNewChatAfterError()
- 位置: L1171-1177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#getVisibleChips()
- 位置: L1189-1203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isTabGroupMember()`, `msg.contextMentions.filter()`
- 条件付き依存: `if (shouldHideDuplicatePageChip)` → `chips.filter()`
- 条件付き依存: `if (shouldHideDuplicatePageChip)` → `URL.parse()`
- 参照: `URL.parse(chip.url)?.href`, `chip.url`, `msg.contextMentions?.length`, `msg.pageUrl`, `msg.role`

## AIChatContent.openAccountSignInAfterError()
- 位置: L1205-1211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIChatContent.#buildTabsRow()
- 位置: L1213-1222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.map()`
- 参照: `tab.title`, `tab.url`, `tabs.length`

## AIChatContent.#getCloseTabsData()
- 位置: L1224-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildTabsRow()`
- 参照: `confirmedData.selectedTabs`, `selectedTabs.length`

## AIChatContent.#getRestoreTabsData()
- 位置: L1242-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalClosedTabs.map()`
- 参照: `originalClosedTabs.length`

## AIChatContent.#getGroupTabsData()
- 位置: L1268-1290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildTabsRow()`
- 参照: `confirmedData.group`, `confirmedData.selectedTabs`, `group.label`, `group.tabCount`, `selectedTabs.length`, `this.#defaultTabGroupLabel`

## AIChatContent.#getSwitchedTabData()
- 位置: L1292-1299
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab?.title`, `tab?.url`

## AIChatContent.#getOpenTabsData()
- 位置: L1301-1339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildTabsRow()`
- 条件付き依存: `if (confirmedData.switched)` → `this.#getSwitchedTabData()`
- 条件付き依存: `if (tabCount && confirmedData.mergedCount === tabCount)` → `this.#getGroupTabsData()`
- 参照: `confirmedData.group`, `confirmedData.mergedCount`, `confirmedData.selectedTabs`, `confirmedData.switched`, `group.label`, `selectedTabs.length`, `this.#defaultTabGroupLabel`

## AIChatContent.#getUngroupedTabsData()
- 位置: L1341-1367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalGroupedTabs.map()`
- 参照: `originalGroupedTabs.length`

## AIChatContent.#getActionResultData()
- 位置: L1369-1391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `method()`, `this.#getCloseTabsData()`, `this.#getGroupTabsData()`, `this.#getRestoreTabsData()`, `this.#getUngroupedTabsData()`
- 参照: `confirmedData.actionType`, `confirmedData.originalClosedTabs`, `confirmedData.originalGroupedTabs`

## open_tabs()
- 位置: L1386-1386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getOpenTabsData()`

## AIChatContent.#renderActionLogGroup()
- 位置: L1400-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#actionResultExpandState.get()`, `this.#actionResultExpandState.set()`, `this.#buildGroupedActionLogRows()`
- 参照: `e.detail?.isExpanded`, `summary?.l10nArgs`, `summary?.l10nId`, `summary?.link`, `toolMsgs.length`, `toolMsgs[0]?.id`, `toolMsgs[0]?.messageId`, `toolMsgs[toolMsgs.length - 1]?.pendingLabel`

## AIChatContent.#renderToolUI()
- 位置: L1429-1448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CONFIRMATION_UI_TYPES.includes()`, `renderFn()`
- 参照: `UI_TYPES.RETRY_COMPONENT`, `msg.isRestored`, `msg.toolUIData`, `this.#uiRenderMap`, `toolUIData.properties`, `toolUIData.uiType`

## AIChatContent.#renderAITab()
- 位置: L1450-1462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.OPEN_AITAB`, `event.detail.openTarget`, `msg.messageId`, `msg.toolUIData.properties?.state`, `msg.toolUIData.properties?.title`, `msg.toolUIData.toolCallId`

## AIChatContent.#handleConfirmationSubmit()
- 位置: L1464-1471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CONFIRMATION_TAB_SELECTION`, `event.detail`

## AIChatContent.#handleConfirmationClose()
- 位置: L1473-1480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CANCEL_TAB_SELECTION`, `event.detail`

## AIChatContent.#handleMonitorSubmit()
- 位置: L1482-1494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CREATE_WATCH`, `UI_UPDATE_TYPES.UPDATE_WATCH`, `event.detail`, `event.detail?.mode`

## AIChatContent.#handleMonitorCancel()
- 位置: L1496-1504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `UI_UPDATE_TYPES.CANCEL_WATCH`, `event.detail`

## AIChatContent.#handleMonitorAction()
- 位置: L1506-1513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `event.detail`

## AIChatContent.#renderAgentMonitorComponent()
- 位置: L1515-1556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handleMonitorAction()`, `this.#handleMonitorCancel()`, `this.#handleMonitorSubmit()`
- 参照: `UI_UPDATE_TYPES.CHECK_WATCH`, `UI_UPDATE_TYPES.DELETE_WATCH`, `UI_UPDATE_TYPES.PAUSE_WATCH`, `UI_UPDATE_TYPES.SAVE_WATCH_DRAFT`, `toolUIData.properties?.agent`, `toolUIData.properties?.mode`, `toolUIData.toolCallId`

## AIChatContent.#handleTabGroupActionSubmit()
- 位置: L1558-1565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToolUIUpdate()`
- 参照: `event.detail`

## AIChatContent.#renderTabGroupConfirmation()
- 位置: L1567-1594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handleConfirmationClose()`, `this.#handleTabGroupActionSubmit()`
- 参照: `TAB_GROUP_ACTION_CONFIG.group_tabs`, `msg.messageId`, `msg.toolUIData`, `toolUIData.properties?.actionType`, `toolUIData.properties?.tabGroupLabel`, `toolUIData.properties?.tabs`, `toolUIData.toolCallId`

## AIChatContent.#renderWebsiteConfirmation()
- 位置: L1596-1621
- 役割: (未記入)
- 触るとき: (未記入)
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
