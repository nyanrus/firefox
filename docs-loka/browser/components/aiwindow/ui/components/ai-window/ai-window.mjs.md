# browser/components/aiwindow/ui/components/ai-window/ai-window.mjs

source: browser/components/aiwindow/ui/components/ai-window/ai-window.mjs
source-hash: db6ce5328c6e057ead9af9765357fda40a03e7a9
lines: 3958

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `console.createInstance()`, `customElements.define()`

## formatResumeTabGroupLabel()
- 位置: L212-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `headline.replace()`, `headline.replace(RESUME_HEADLINE_PREFIX_RE, "").trim()`, `headline.trim()`, `stripped.charAt()`, `stripped.charAt(0).toUpperCase()`, `stripped.slice()`

## getErrorCode()
- 位置: L230-236
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `error.error`, `error.metadata?.errorMessage`, `error.status`

## resolveModelResponseError()
- 位置: L238-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getErrorCode()`
- 参照: `error.clientReason`, `error.name`, `error.status`

## AIWindow.#kitMention()
- 位置: L306-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`

## AIWindow.#memoriesIconShown()
- 位置: L310-316
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#hasMemories`, `this.memoriesConversationPref`, `this.memoriesHistoryPref`

## AIWindow.#resumeActivityEnabled()
- 位置: L320-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures[NIMBUS_FEATURE_SMART_WINDOW].getVariable()`
- 参照: `lazy.NimbusFeatures`

## AIWindow.#resumeActivityMemoriesEnabled()
- 位置: L329-335
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#hasMemories`, `this.#memoriesToggled`, `this.memoriesConversationPref`, `this.memoriesHistoryPref`

## AIWindow.#hostBrowser()
- 位置: L359-361
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext?.embedderElement`

## AIWindow.#detectModeFromContext()
- 位置: L363-367
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `this.#hostBrowser?.id`

## AIWindow.#syncHistoryState()
- 位置: L376-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.history.replaceState()`
- 参照: `MODE.FULLPAGE`, `this.#conversation?.id`, `this.isConnected`, `this.mode`, `window.history.state`

## AIWindow.#getPendingConversationId()
- 位置: L395-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hostBrowser?.getAttribute()`
- 参照: `window.history.state?.conversationId`

## AIWindow.#getBrowserContainer()
- 位置: L410-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## AIWindow.syncSmartbarMemoriesStateFromConversation()
- 位置: async L414-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#syncMemoriesButtonUI()`
- 参照: `this.#conversation.memoriesToggled`, `this.#conversation?.memoriesToggled`, `this.#memoriesToggled`, `this.#smartbar`

## AIWindow.focusSmartbar()
- 位置: async L425-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartbar.focus()`
- 参照: `this.#smartbar`, `this.#smartbarReadyPromise`

## AIWindow.#refreshHasMemories()
- 位置: async L434-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MemoriesManager.getAllMemories()`, `lazy.log.error()`
- 参照: `memories?.length`, `this.#hasMemories`

## AIWindow.#syncMemoriesButtonUI()
- 位置: async L444-457
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.memoriesConversationPref && !this.memoriesHistoryPref)` → `this.#refreshHasMemories()`
- 参照: `this.#memoriesButton`, `this.#memoriesButton.pressed`, `this.#memoriesButton.show`, `this.#memoriesIconShown`, `this.#memoriesToggled`, `this.memoriesConversationPref`, `this.memoriesHistoryPref`

## AIWindow.#recordChatInteraction()
- 位置: L465-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (interactionCount < MAX_INTERACTION_COUNT)` → `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## AIWindow.constructor()
- 位置: L479-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.ResumeActivity.isSectionHiddenForSession()`, `lazy.getCurrentModelChoiceId()`, `super()`, `this.#detectModeFromContext()`, `this.#hostBrowser?.getAttribute()`, `this.#onMistralReleasePrefChanged()`, `this.#setModelChoice()`, `this.#syncMemoriesButtonUI()`, `this.#syncTopSites()`, `this.requestUpdate()`
- 条件付き依存: `if (this.#hostBrowser?.getAttribute("data-conversation-id"))` → `this.classList.add()`
- 参照: `MODE.FULLPAGE`, `lazy.ChatConversation`, `this.#browser`, `this.#conversation`, `this.#resolveSmartbarReady`, `this.#smartbar`, `this.#smartbarReadyPromise`, `this.isGenerating`, `this.mistralReleasePref`, `this.mode`, `this.promoMessage`, `this.recentChats`, `this.resumeCards`, `this.resumeCardsEmptyReason`, `this.resumeCardsLoading`, `this.resumeSectionHidden`, `this.showDisclaimer`, `this.showFooter`, `this.showStarters`, `this.startersResolved`, `this.topSites`, `this.userPrompt`

## AIWindow.#topChromeWindow()
- 位置: L564-566
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext?.topChromeWindow`

## AIWindow.#attachConversationListeners()
- 位置: L568-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AgentUI.observeMonitorChanges()`, `this.#conversation.on()`
- 参照: `this.#conversation`, `this.#onMessageComplete`, `this.#onMessageUpdate`, `this.#onSeenUrlsUpdated`

## AIWindow.#removeConversationListeners()
- 位置: L588-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AgentUI.unobserveMonitorChanges()`, `this.#conversation.off()`
- 参照: `this.#conversation`, `this.#onMessageComplete`, `this.#onMessageUpdate`, `this.#onSeenUrlsUpdated`

## AIWindow.#onSeenUrlsUpdated()
- 位置: L608-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getAIChatContentActor()`
- 条件付き依存: `if (actor)` → `this.#dispatchSeenUrls()`

## AIWindow.#onMessageUpdate()
- 位置: L615-637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchMessageToChatContent()`
- 条件付き依存: `if (this.mode === MODE.FULLPAGE && message.kit)` → `this.#kitMention?.trigger()`
- 条件付き依存: `if (message.toolUIData)` → `lazy.ToolUI.handleUIDisplayTelemetry()`
- 参照: `MODE.FULLPAGE`, `message.convId`, `message.kit`, `message.toolUIData`, `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.onMemoriesApplied()
- 位置: L639-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoryApplied.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#getDataConvId()
- 位置: L652-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hostBrowser?.getAttribute()`
- 参照: `this.#conversation`, `this.#conversation.id`

## AIWindow.connectedCallback()
- 位置: L660-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `installClientErrorListeners()`, `lazy.SmartWindowTelemetry.recordClientError()`, `super.connectedCallback()`, `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#loadAvailableModels()`, `this.#loadPendingConversation()`, `this.#registerSwapDocShellsListener()`, `this.#setupWindowModeObserver()`, `this.documentGlobal.addEventListener()`, `this.getClientErrorContext()`, `this.ownerDocument.addEventListener()`, `this.remove()`, `this.setAttribute()`
- 参照: `this.#handleModelChange`, `this.#handleOpenModelSettings`, `this.#handleSmartbarCommit`, `this.#handleStopGeneration`, `this.#onCustomEndpointPrefChanged`, `this.#onHistoryMenuEvent`, `this.#onModelChoicePrefChanged`, `this.#onPanelShowing`, `this.#removeClientErrorListeners`, `this.#topSitesObserver`, `this.documentGlobal`, `this.mode`, `window.browsingContext?.topChromeWindow`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#topSitesObserver()
- 位置: L700-700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#syncTopSites()`

## AIWindow.conversationId()
- 位置: L733-735
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#conversation?.id`

## AIWindow.conversationMessageCount()
- 位置: L737-739
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#conversation.messageCount`

## AIWindow.conversation()
- 位置: L746-748
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#conversation`

## AIWindow.#registerSwapDocShellsListener()
- 位置: L750-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#swapDocShellsChromeWindow?.addEventListener()`, `this.#swapDocShellsChromeWindow?.removeEventListener()`
- 参照: `this.#handleEndSwapDocShells`, `this.#swapDocShellsChromeWindow`

## AIWindow.handleEvent()
- 位置: L769-775
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.detail)` → `this.openConversation()`
- 条件付き依存: `if (!this.#conversation?.messages?.length)` → `this.onCreateNewChatClick()`
- 参照: `event.detail`, `this.#conversation?.messages?.length`

## AIWindow.#handleEndSwapDocShells()
- 位置: L781-816
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browser?.remove()`, `this.#createAIChatBrowser()`, `this.#getBrowserContainer()`

## AIWindow.#createAIChatBrowser()
- 位置: L827-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.setAttribute()`, `container.prepend()`, `this.#updateBrowserTabbable()`, `this.ownerDocument.createXULElement()`
- 参照: `this.#browser`

## AIWindow.#updateBrowserTabbable()
- 位置: L845-854
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.classList.contains()`
- 条件付き依存: `if (this.classList.contains("chat-active"))` → `this.#browser.removeAttribute()`
- 条件付き依存: `if (!(this.classList.contains("chat-active")))` → `this.#browser.setAttribute()`
- 参照: `this.#browser`

## AIWindow.#setupWindowModeObserver()
- 位置: L856-869
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.#windowModeObserver`
- XPCOM: `Services.obs`

## this.#windowModeObserver()
- 位置: L857-863
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (subject == window.browsingContext?.topChromeWindow)` → `this.#updateSmartbarAndHeaderVisibility()`
- 参照: `window.browsingContext?.topChromeWindow`

## AIWindow.#updateSmartbarAndHeaderVisibility()
- 位置: L871-890
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `this.renderRoot.querySelector()`, `this.toggleAttribute()`
- 参照: `chatHeader.hidden`, `this.#smartbar`, `this.#smartbar.hidden`, `this.#smartbarToggleButton`, `this.#smartbarToggleButton.hidden`, `window.browsingContext.topChromeWindow`

## AIWindow.disconnectedCallback()
- 位置: L892-1014
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getAllModelsData()`, `lazy.openAIEngine.hasCustomEndpoint()`
- 参照: `this.availableModels`

## AIWindow.#updateSmartbarModels()
- 位置: L1037-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `smartbar?.querySelector()`
- 条件付き依存: `if (modelSelect && this.availableModels)` → `lazy.getCurrentModelChoiceId()`
- 参照: `modelSelect.availableModels`, `modelSelect.defaultModelChoiceId`, `modelSelect.selectedModelId`, `this.availableModels`, `this.selectedModelId`

## AIWindow.#onModelChoicePrefChanged()
- 位置: async L1046-1057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#switchModel()`, `this.#updateSmartbarModels()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`, `this.availableModels`

## AIWindow.#handleModelChange()
- 位置: async L1059-1063
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#switchModel()`
- 参照: `event.detail.modelChoiceId`

## AIWindow.#onCustomEndpointPrefChanged()
- 位置: async L1065-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#loadAvailableModels()`, `this.#updateSmartbarModels()`
- 条件付き依存: `if ( !this.#hasModelChoiceOverride && this.availableModels[defaultModelChoiceId] )` → `this.#switchModel()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`, `this.availableModels`

## AIWindow.#onMistralReleasePrefChanged()
- 位置: async L1079-1093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `lazy.refreshModelsDataCache()`, `this.#loadAvailableModels()`, `this.#updateSmartbarModels()`
- 条件付き依存: `if ( !this.#hasModelChoiceOverride && this.availableModels[defaultModelChoiceId] )` → `this.#switchModel()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`, `this.availableModels`

## AIWindow.#setModelChoice()
- 位置: L1100-1105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelName()`
- 参照: `this.#selectedModelChoiceId`, `this.availableModels`, `this.availableModels?.[modelChoiceId]?.model`, `this.selectedModelId`

## AIWindow.#switchModel()
- 位置: async L1107-1128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#setModelChoice()`
- 条件付き依存: `if (this.#conversation?.messages.length)` → `this.#conversation.loadSystemPrompt()`
- 条件付き依存: `if (isTabOverride)` → `this.#dispatchChromeEvent()`
- 条件付き依存: `if (isTabOverride)` → `this.#getAIWindowEventOptions()`
- 参照: `this.#conversation?.messages.length`, `this.#hasModelChoiceOverride`, `this.selectedModelId`

## AIWindow.restoreModelChoiceOverride()
- 位置: L1135-1139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelChoiceId()`, `this.#setModelChoice()`, `this.#updateSmartbarModels()`
- 参照: `this.#hasModelChoiceOverride`, `this.#smartbar`

## AIWindow.#handleOpenModelSettings()
- 位置: L1141-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#topChromeWindow?.openPreferences()`

## AIWindow.#loadPendingConversation()
- 位置: async L1148-1182
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `error.toString()`, `this.#createAIChatBrowser()`, `this.#getBrowserContainer()`, `this.#loadPendingConversation()`, `this.#loadPendingConversation().catch()`, `this.#swapConversation()`, `this.#syncTopSites()`
- 条件付き依存: `if (doc.hidden)` → `doc.addEventListener()`
- 条件付き依存: `if (!(doc.hidden))` → `this.#getOrCreateSmartbar()`
- 参照: `doc.hidden`, `error.stack`, `this.#conversation`, `this.#visibilityChangeHandler`, `this.ownerDocument`

## this.#visibilityChangeHandler()
- 位置: L1192-1203
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!doc.hidden && !this.#smartbar)` → `this.#getOrCreateSmartbar()`
- 条件付き依存: `if (!doc.hidden)` → `lazy.ResumeActivity.isSectionHiddenForSession()`
- 参照: `doc.hidden`, `this.#smartbar`, `this.resumeSectionHidden`

## AIWindow.updateInput()
- 位置: L1232-1251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editor.insertMention()`
- 参照: `mentions.length`, `this.#smartbar`, `this.#smartbar.inputField`, `this.#smartbar.value`

## AIWindow.restoreContextChips()
- 位置: L1261-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartbar?.restoreContextChips()`

## AIWindow.#getSmartbarInputState()
- 位置: L1275-1288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editor.getAllMentions()`, `editor.getAllMentions().map()`, `editor.posToTextOffset()`
- 参照: `editor.plainText`, `lazy.EMPTY_SMARTBAR_INPUT_STATE`, `mention.pos`, `mention.textOffset`, `this.#smartbar?.inputField`

## AIWindow.loadStarterPrompts()
- 位置: async L1299-1496
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.headline.trim()`

## AIWindow.#applyResumeActivities()
- 位置: L1509-1535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResumeActivity.isMemoryDismissed()`, `rawResumeActivities.filter()`, `resumeActivities.slice()`, `this.#hasValidHeadline()`, `validResumeActivities.filter()`
- 条件付き依存: `if (this.resumeCards.length)` → `lazy.ResumeActivity.clearSectionHiddenForSession()`
- 参照: `RESUME_SECTION_EMPTY_REASON.ALL_DISMISSED`, `RESUME_SECTION_EMPTY_REASON.NO_SUGGESTIONS`, `memory.id`, `resumeActivities.length`, `this.resumeCards`, `this.resumeCards.length`, `this.resumeCardsEmptyReason`, `this.resumeSectionHidden`, `validResumeActivities.length`

## AIWindow.#resumeActivitiesToStarterPrompts()
- 位置: L1537-1547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.previewTabs.map()`, `resumeActivities.map()`
- 参照: `content.headline`

## AIWindow.#renderStarterPrompts()
- 位置: L1563-1585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (this.showStarters && recordTelemetry)` → `this.#starters.filter()`
- 条件付き依存: `if (this.showStarters && recordTelemetry)` → `this.onQuickPromptDisplayed()`
- 参照: `starter.type`, `this.#conversation?.messages?.length`, `this.#starters`, `this.#starters.filter( starter => starter.type === "resume" ).length`, `this.#starters.length`, `this.isConnected`, `this.showStarters`, `this.startersResolved`

## AIWindow.#topSitesEnabled()
- 位置: L1593-1595
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.hideTopSitesPref`, `this.topSitesFeedPref`

## AIWindow.#syncTopSites()
- 位置: L1604-1621
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.mode === MODE.FULLPAGE)` → `Glean.smartWindow.topsitesEnabled.set()`
- 条件付き依存: `if (this.mode === MODE.FULLPAGE && this.#topSitesEnabled)` → `this.#loadTopSites()`
- 参照: `MODE.FULLPAGE`, `this.#topSitesEnabled`, `this.mode`, `this.ownerDocument.hidden`, `this.startersResolved`, `this.topSites`

## AIWindow.#loadTopSites()
- 位置: L1623-1644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(sites ?? []) .filter()`, `(sites ?? []) .filter(site => site?.url && !site.sponsored_position) .slice()`, `lazy.AboutNewTab.getTopSites()`, `lazy.log.error()`
- 条件付き依存: `if (this.topSites.length)` → `Glean.smartWindow.topsitesImpression.record()`
- 参照: `site.sponsored_position`, `site?.url`, `this.isConnected`, `this.topSites`, `this.topSites.length`

## AIWindow.#handleTopSiteSelected()
- 位置: L1652-1663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.topsitesClick.record()`, `lazy.URILoadingHelper.openTrustedLinkIn()`
- 参照: `event.detail`, `this.#topChromeWindow`, `this.topSites.length`

## AIWindow.#handleResumeSectionHide()
- 位置: L1670-1673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResumeActivity.hideSectionForSession()`
- 参照: `this.resumeSectionHidden`

## AIWindow.#handleResumeCardMenuItemSelected()
- 位置: L1682-1702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResumeActivity.dismissMemory()`, `lazy.log.error()`, `this.#handleResumeCardOpenTabs()`, `this.#handleResumeCardOpenTabs(journeyId).catch()`, `this.resumeCards.filter()`
- 参照: `RESUME_SECTION_EMPTY_REASON.ALL_DISMISSED`, `event.detail`, `memory.id`, `this.resumeCards`, `this.resumeCards.length`, `this.resumeCardsEmptyReason`

## AIWindow.#handleResumeCardOpenTabs()
- 位置: async L1710-1723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatResumeTabGroupLabel()`, `lazy.ToolUI.openOrGroupTabs()`, `this.resumeCards.find()`
- 参照: `card.content.headline`, `card?.content.previewTabs`, `memory.id`, `previewTabs?.length`, `this.#topChromeWindow`

## AIWindow.#getOrCreateSmartbar()
- 位置: L1730-1807
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchChromeEvent()`, `this.#getEventTab()`
- 参照: `this.#smartbar?.contextChips`, `this.#smartbar?.removedImplicitContextChip`

## AIWindow.#setupSmartbarFocus()
- 位置: L1826-1846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `smartbar.addEventListener()`, `smartbar.focus()`, `smartbar.inputField.addEventListener()`, `smartbar.toggleAttribute()`
- 条件付き依存: `if (!hasAutoFocused)` → `smartbar.toggleAttribute()`
- 条件付き依存: `if (!isMouseClick)` → `smartbar.removeAttribute()`

## AIWindow.#observeSmartbarHeight()
- 位置: L1848-1862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartbarResizeObserver.observe()`, `updateSmartbarHeight()`
- 参照: `this.#smartbar`, `this.#smartbarResizeObserver`

## updateSmartbarHeight()
- 位置: L1849-1857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartbar.querySelector()`, `this.style.setProperty()`
- 参照: `this.#smartbar.offsetHeight`, `urlbarView.offsetHeight`

## AIWindow.#handleSmartbarInput()
- 位置: L1872-1877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#getSmartbarInputState()`

## AIWindow.#dispatchChromeEvent()
- 位置: L1889-1894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `topChromeWindow?.dispatchEvent()`
- 参照: `topChromeWindow.CustomEvent`, `window?.browsingContext?.topChromeWindow`

## AIWindow.#handleStopGeneration()
- 位置: L1901-1918
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortController.abort()`, `this.#conversation?.getHistoryResultsSnapshot()`, `this.#conversation?.messages ?.filter()`, `this.#conversation?.messages ?.filter( m => m.role == lazy.MESSAGE_ROLE.ASSISTANT && m?.content?.type == "text" ) .at()`, `this.#dispatchMessageToChatContent()`
- 参照: `lastAssistant?.citations`, `lastAssistant?.id`, `lazy.MESSAGE_ROLE.ASSISTANT`, `m.role`, `m?.content?.type`, `this.#abortController`, `this.isGenerating`

## AIWindow.#handleSmartbarCommit()
- 位置: L1926-2033
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allUrls.add()`, `atMentions.push()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.getContextMentionKey()`, `lazy.parseTabGroupMentionId()`, `seenKeys.add()`, `seenKeys.has()`, `this.#getInlineMentions()`
- 条件付き依存: `if (key)` → `seenKeys.add()`
- 条件付き依存: `if (mention.url)` → `allUrls.add()`
- 条件付き依存: `if (groupId)` → `atMentions.push()`
- 条件付き依存: `if (groupId)` → `this.#getTabGroupColor()`
- 参照: `lazy.CONTEXT_MENTION_TYPE.TAB_GROUP`, `mention.id`, `mention.label`, `mention.type`, `mention.url`

## AIWindow.#withTabGroupMembers()
- 位置: L2095-2101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#expandTabGroupMentions()`
- 条件付き依存: `if (tabGroupMembers.length)` → `this.#conversation?.addSeenUrls()`
- 条件付き依存: `if (tabGroupMembers.length)` → `tabGroupMembers.map()`
- 参照: `tabGroupMembers.length`

## AIWindow.#expandTabGroupMentions()
- 位置: L2107-2130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getContextMentionKey()`, `mentions.map()`, `seen.has()`, `this.#getTabGroupMembers()`
- 条件付き依存: `if (!seen.has(key))` → `seen.add()`
- 条件付き依存: `if (!seen.has(key))` → `tabGroupMembers.push()`
- 参照: `lazy.CONTEXT_MENTION_TYPE.TAB_GROUP`, `lazy.MAX_TAB_GROUP_MEMBERS`, `lazy.getContextMentionKey`, `mention.groupId`, `mention.type`, `tabGroupMembers.length`

## AIWindow.#getTabGroup()
- 位置: L2138-2142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#topChromeWindow.gBrowser.tabGroups.find()`
- 参照: `group.id`

## AIWindow.#getTabGroupColor()
- 位置: L2148-2150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTabGroup()`
- 参照: `this.#getTabGroup(groupId)?.color`

## AIWindow.#getTabGroupMembers()
- 位置: L2157-2179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.tabs.map()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.tabManagementService.getTabGroupById()`, `tabGroupLabels.get()`, `this.#getTabGroup()`, `visibleGroup.tabs.slice()`, `visibleGroup.tabs.slice(0, limit).map()`
- 参照: `lazy.CONTEXT_MENTION_TYPE.TAB`, `tab.label`, `tab.linkedBrowser?.currentURI?.spec`, `this.#topChromeWindow`, `visibleGroup.id`, `visibleGroup.label`

## AIWindow.#getInlineMentions()
- 位置: L2186-2192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editor.getAllMentions()`
- 参照: `editor?.getAllMentions`, `this.#smartbar?.inputField`

## AIWindow.submitChatMessage()
- 位置: L2213-2262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.chatSubmit.record()`, `String()`, `String(text ?? "").trim()`, `contextMentions.filter()`, `lazy.ToolUI.autoCancelActiveConfirmation()`, `lazy.ToolUI.autoCancelActiveConfirmation( this.#conversation, this.#topChromeWindow, this.mode ).catch()`, `lazy.isTabGroupMember()`, `lazy.log.error()`, `this.#createUserRoleOpts()`, `this.#fetchAIResponse()`, `this.#recordChatInteraction()`
- 参照: `contextMentions.filter(member => !lazy.isTabGroupMember(member)) .length`, `this.#conversation`, `this.#conversation.lastSubmitType`, `this.#topChromeWindow`, `this.conversationId`, `this.conversationMessageCount`, `this.mode`, `this.modelName`, `trimmed.length`

## AIWindow.#handleMemoriesToggle()
- 位置: async L2264-2290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoriesToggle.record()`, `console.error()`, `lazy.MemoriesManager.getAllMemories()`, `lazy.log.debug()`, `this.#saveMemoriesToggleToConversation()`, `this.#syncMemoriesButtonUI()`
- 参照: `event.detail.pressed`, `memories.length`, `this.#conversation?.messageCount`, `this.#handleMemoriesToggle.name`, `this.#memoriesToggled`, `this.conversationId`, `this.mode`

## AIWindow.#saveMemoriesToggleToConversation()
- 位置: L2292-2300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateConversation()`
- 参照: `this.#conversation`, `this.#conversation.memoriesToggled`, `this.#conversation.messageCount`

## AIWindow.#handlePromptSelected()
- 位置: L2308-2315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onQuickPromptClicked()`
- 条件付き依存: `if (event.detail.type === "resume")` → `this.#handleResumePromptSelected()`
- 参照: `event.detail`, `event.detail.text`, `event.detail.type`

## AIWindow.#handleResumePromptSelected()
- 位置: L2317-2327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#generateResumeActivityConversation()`, `this.#generateResumeActivityConversation(resumePrompt).catch()`, `this.#recordQuickPromptClicked()`
- 参照: `this.#isGeneratingResumeActivityConversation`

## AIWindow.#handleResumeCardResume()
- 位置: L2337-2349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleResumePromptSelected()`, `this.resumeCards.find()`
- 参照: `card.content`, `card.content.headline`, `card.memory`, `event.detail`, `memory.id`

## AIWindow.#handlePromptDismissed()
- 位置: L2357-2368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResumeActivity.dismissMemory()`, `this.#conversation.transientStarters.filter()`, `this.#recordQuickPromptDismissed()`, `this.#renderStarterPrompts()`
- 参照: `event.detail`, `memory.id`, `starter.memory?.id`, `this.#conversation.transientStarters`

## AIWindow.#generateResumeActivityConversation()
- 位置: async L2382-2464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `conversation.injectRealTimeContext()`, `conversation.messages.at()`, `formatResumeTabGroupLabel()`, `resumePrompt.content.previewTabs.map()`, `this.openConversation()`, `this.submitChatMessage()`
- 条件付き依存: `if (this.#resumeActivityMemoriesEnabled)` → `lazy.constructConversationToResumeActivity()`
- 条件付き依存: `if (this.#resumeActivityMemoriesEnabled)` → `lazy.log.error()`
- 条件付き依存: `if (!conversation)` → `this.#buildPlainResumeConversation()`
- 条件付き依存: `if (!conversation)` → `lazy.log.error()`
- 参照: `conversationAtClick?.id`, `resumePrompt.content`, `resumePrompt.content.headline`, `resumePrompt.content.previewTabs?.length`, `resumePrompt.memory`, `resumePrompt.memory.id`, `resumePrompt.text`, `this.#conversation`, `this.#isGeneratingResumeActivityConversation`, `this.#resumeActivityMemoriesEnabled`, `userMessage?.content?.body`

## AIWindow.#buildPlainResumeConversation()
- 位置: async L2481-2492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addUserMessage()`, `conversation.loadSystemPrompt()`, `conversation.securityProperties.commit()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`
- 参照: `lazy.ChatConversation`, `resumePrompt.content.headline`

## AIWindow.onQuickPromptDisplayed()
- 位置: L2502-2510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.quickPromptDisplayed.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#recordQuickPromptClicked()
- 位置: L2518-2526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.quickPromptClicked.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#recordQuickPromptDismissed()
- 位置: L2531-2535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.quickPromptDismissed.record()`
- 参照: `this.conversationId`

## AIWindow.onQuickPromptClicked()
- 位置: L2546-2560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordQuickPromptClicked()`, `this.#smartbar.getCurrentContextData()`, `this.#withTabGroupMembers()`, `this.submitChatMessage()`

## AIWindow.onOpenLink()
- 位置: L2562-2568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.linkClick.record()`
- 参照: `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.#createUserRoleOpts()
- 位置: L2577-2586
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MEMORIES_FLAG_SOURCE.CONVERSATION`, `lazy.MEMORIES_FLAG_SOURCE.GLOBAL`, `lazy.UserRoleOpts`, `this.#memoriesIconShown`, `this.#memoriesToggled`

## AIWindow.#updateConversation()
- 位置: async L2593-2599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.chatStore .updateConversation()`, `lazy.AIWindow.chatStore .updateConversation(this.#conversation) .catch()`, `lazy.log.error()`
- 参照: `this.#conversation`, `updateError.message`

## AIWindow.#addConversationTitle()
- 位置: async L2607-2640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `lazy.generateChatTitle()`, `this.#conversation.messages.find()`, `this.#updateConversation()`
- 参照: `document.title`, `firstUserMessage?.content?.body`, `firstUserMessage?.pageUrl?.href`, `lazy.MESSAGE_ROLE.USER`, `m.role`, `this.#conversation.pageMeta?.description`, `this.#conversation.pageMeta?.title`, `this.#conversation.title`, `this.#conversation.titlePromise`, `this.conversationId`

## AIWindow.#updateTabFavicon()
- 位置: L2642-2648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.classList.contains()`
- 参照: `MODE.FULLPAGE`, `link.href`, `this.mode`

## AIWindow.#resetConversationState()
- 位置: L2650-2658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hostBrowser?.setAttribute()`, `this.#syncHistoryState()`, `this.#updateBrowserTabbable()`, `this.classList.remove()`
- 参照: `this.#conversation.id`

## AIWindow.#setBrowserContainerActiveState()
- 位置: L2660-2679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartbar?.unsuppressStartQuery()`, `this.#updateBrowserTabbable()`, `this.classList.remove()`
- 条件付き依存: `if (isActive)` → `this.classList.add()`
- 条件付き依存: `if (isActive)` → `this.#updateBrowserTabbable()`
- 条件付き依存: `if (isActive)` → `this.#smartbar?.suppressStartQuery()`
- 条件付き依存: `if (isActive)` → `this.#smartbar?.view.close()`
- 参照: `MODE.FULLPAGE`, `this.#smartbar.inputField.showPlaceholderAnimation`, `this.#smartbar?.inputField`, `this.mode`

## AIWindow.#initActiveChatlayout()
- 位置: L2681-2685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setBrowserContainerActiveState()`
- 参照: `this.showFooter`, `this.showStarters`

## AIWindow.#fetchAIResponse()
- 位置: async L2721-2851
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation?.off()`
- 参照: `lazy.MESSAGE_ROLE.ASSISTANT`, `message.role`

## AIWindow.#watchTabCloseForAbort()
- 位置: L2864-2877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeWin?.gBrowser?.getTabForBrowser()`, `tab.addEventListener()`, `tab.removeEventListener()`
- 参照: `MODE.SIDEBAR`, `browsingContext.embedderElement`, `this.mode`, `window.browsingContext?.topChromeWindow`

## onTabClose()
- 位置: L2874-2874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.abort()`

## AIWindow.updated()
- 位置: L2879-2895
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProps.has()`, `super.updated()`
- 条件付き依存: `if (changedProps.has("isGenerating"))` → `this.#getAIChatContentActor()?.setGeneratingOnChatContent()`
- 条件付き依存: `if (changedProps.has("isGenerating"))` → `this.#getAIChatContentActor()`
- 条件付き依存: `if (changedProps.has("availableModels"))` → `this.#setModelChoice()`
- 条件付き依存: `if (this.#smartbar)` → `this.#updateSmartbarModels()`
- 参照: `this.#selectedModelChoiceId`, `this.#smartbar`, `this.#smartbar.assistantIsGenerating`, `this.isGenerating`

## AIWindow.#onMessageComplete()
- 位置: L2897-2942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ToolUI.injectRetryToolUIDataIfNeeded()`, `this.#addConversationTitle()`, `this.#conversation?.getHistoryResultsSnapshot()`, `this.#dispatchMessageToChatContent()`
- 条件付き依存: `if (retryInjected)` → `this.#dispatchMessageToChatContent()`
- 条件付き依存: `if (retryInjected)` → `structuredClone()`
- 条件付き依存: `if (followupCount)` → `this.onQuickPromptDisplayed()`
- 条件付き依存: `if (msg?.memoriesApplied?.length)` → `this.onMemoriesApplied()`
- 参照: `msg.toolUIData`, `msg?.citations`, `msg?.content?.body`, `msg?.id`, `msg?.memoriesApplied?.length`, `msg?.tokens?.followup?.length`, `this.#conversation`

## AIWindow.#getModelRequestLatencyAndDuration()
- 位置: L2944-2950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Math.round()`

## AIWindow.modelName()
- 位置: L2952-2954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentModelName()`

## AIWindow.#getConversationLastMessageAndCount()
- 位置: L2956-2974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conversation.messages.slice()`
- 参照: `message.content?.type`, `message.role`, `this.#conversation`

## AIWindow.#sendModelResponseTelemetryEvent()
- 位置: L2976-3002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.modelResponse.record()`, `resolveModelResponseError()`, `this.#getConversationLastMessageAndCount()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `lastAssistantMessage?.memoriesApplied?.length`, `lastAssistantMessage?.parentMessageId`, `lazy.Chat.lastUsage?.completion_tokens`, `lazy.MESSAGE_ROLE.ASSISTANT`, `this.conversationId`, `this.mode`, `this.modelName`

## AIWindow.getClientErrorContext()
- 位置: L3011-3021
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getConversationLastMessageAndCount()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `lazy.MESSAGE_ROLE.ASSISTANT`, `this.conversationId`, `this.mode`, `this.modelName`

## AIWindow.#sendModelRequestTelemetryEvent()
- 位置: L3023-3037
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.modelRequest.record()`, `this.#getConversationLastMessageAndCount()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `lastUserMessage?.id`, `lastUserMessage?.memoriesApplied?.length`, `lazy.Chat.lastUsage?.completion_tokens`, `lazy.MESSAGE_ROLE.USER`, `this.conversationId`, `this.mode`

## AIWindow.#getBrowsingContext()
- 位置: L3039-3046
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `MODE.SIDEBAR`, `this.mode`, `window.browsingContext`, `window.browsingContext.topChromeWindow.gBrowser.selectedBrowser .browsingContext`

## AIWindow.#handleError()
- 位置: L3048-3065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `getErrorCode()`, `this.#dispatchMessageToChatContent()`, `this.#sendModelResponseTelemetryEvent()`
- 参照: `error.clientReason`, `error.status`

## AIWindow.#dispatchSeenUrls()
- 位置: L3073-3081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.dispatchSeenUrlsToChatContent()`
- 参照: `this.#conversation.id`, `this.#conversation.seenUrls`, `this.#conversation?.id`

## AIWindow.#getAIChatContentActor()
- 位置: L3089-3107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `windowGlobal.getActor()`
- 条件付き依存: `if (!this.#browser)` → `lazy.log.warn()`
- 条件付き依存: `if (!windowGlobal)` → `lazy.log.warn()`
- 参照: `this.#browser`, `this.#browser.browsingContext?.currentWindowGlobal`

## AIWindow.#dispatchMessageToActor()
- 位置: L3116-3150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.dispatchMessageToChatContent()`, `this.#maybeSetMemoriesCalloutData()`
- 条件付き依存: `if (typeof message.role !== "string")` → `lazy.getRoleLabel(newMessage.role).toLowerCase()`
- 条件付き依存: `if (typeof message.role !== "string")` → `lazy.getRoleLabel()`
- 条件付き依存: `if (newMessage.role === "tool")` → `lazy.getActionLogConfigForTool()`
- 条件付き依存: `if (newMessage.role === "tool")` → `lazy.buildActionLogRow()`
- 参照: `cfg.label`, `cfg.link`, `cfg.pendingLabel`, `cfg.show`, `lazy.ACTION_LOG_UI_TYPE`, `message.role`, `newMessage.actionLog`, `newMessage.content?.args`, `newMessage.content?.body`, `newMessage.content?.name`, `newMessage.role`

## AIWindow.#maybeSetMemoriesCalloutData()
- 位置: L3152-3163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- 参照: `lazy.MESSAGE_ROLE.ASSISTANT`, `newMessage.memoriesApplied?.length`, `newMessage.role`, `newMessage.showMemoriesCallout`
- XPCOM: `Services.prefs`

## AIWindow.#dispatchMessageToChatContent()
- 位置: L3165-3168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchMessageToActor()`, `this.#getAIChatContentActor()`

## AIWindow.onContentReady()
- 位置: L3174-3189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getAIChatContentActor()`
- 条件付き依存: `if (this.#pendingRestoreConversation)` → `this.openConversation()`
- 条件付き依存: `if (actor)` → `this.#deliverConversationMessages()`
- 条件付き依存: `if (actor)` → `actor.setGeneratingOnChatContent()`
- 参照: `this.#conversation?.messages?.length`, `this.#pendingMessageDelivery`, `this.#pendingRestoreConversation`, `this.isGenerating`

## AIWindow.#deliverConversationMessages()
- 位置: L3196-3225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conversation.renderState()`, `this.#conversation.renderState().forEach()`, `this.#dispatchMessageToActor()`, `this.#dispatchSeenUrls()`, `this.#setBrowserContainerActiveState()`
- 参照: `this.#conversation`, `this.#conversation.id`, `this.#conversation.messages.length`, `this.#pendingMessageDelivery`

## AIWindow.#getEventTab()
- 位置: L3238-3244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser?.getTabForBrowser()`
- 参照: `gBrowser?.selectedTab`, `this.#hostBrowser`, `window?.browsingContext?.topChromeWindow?.gBrowser`

## AIWindow.#getAIWindowEventOptions()
- 位置: L3256-3272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCurrentTabUrl()`, `this.#getDataConvId()`, `this.#getEventTab()`
- 参照: `this.#conversation`, `this.#hasModelChoiceOverride`, `this.#selectedModelChoiceId`, `this.mode`

## AIWindow.#swapConversation()
- 位置: L3282-3304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#attachConversationListeners()`, `this.#dispatchChromeEvent()`, `this.#getAIWindowEventOptions()`, `this.#kitMention?.reset()`, `this.#removeConversationListeners()`, `this.syncSmartbarMemoriesStateFromConversation()`
- 条件付き依存: `if ( conversation && !conversation.messageCount && conversation.transientStarters?.length )` → `this.#renderStarterPrompts()`
- 参照: `conversation.messageCount`, `conversation.transientStarters`, `conversation.transientStarters?.length`, `this.#conversation`

## AIWindow.openConversation()
- 位置: L3311-3352
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext?.topChromeWindow?.gBrowser?.selectedTab`

## AIWindow.onCreateNewChatClick()
- 位置: L3360-3362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearChat()`

## AIWindow.clearChat()
- 位置: L3364-3405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hostBrowser?.setAttribute()`, `this.#dispatchChromeEvent()`, `this.#dispatchMessageToChatContent()`, `this.#getAIWindowEventOptions()`, `this.#smartbar?.unsuppressStartQuery()`, `this.#swapConversation()`, `this.#syncHistoryState()`, `this.#syncMemoriesButtonUI()`
- 条件付き依存: `if (this.mode !== MODE.FULLPAGE)` → `this.#setBrowserContainerActiveState()`
- 参照: `MODE.FULLPAGE`, `lazy.ChatConversation`, `this.#conversation`, `this.#conversation.id`, `this.#conversation.transientStarters?.length`, `this.#memoriesToggled`, `this.mode`, `this.showStarters`, `window.browsingContext?.embedderElement`

## AIWindow.#onCloseSidebarClick()
- 位置: L3407-3409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchChromeEvent()`

## AIWindow.#refreshRecentChats()
- 位置: async L3412-3426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.map()`, `lazy.AIWindow.chatStore.findRecentConversations()`, `lazy.log.error()`
- 参照: `item.id`, `item.pageUrl`, `item.title`, `this.recentChats`

## AIWindow.#onRecentChatSelected()
- 位置: async L3433-3462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(win.gBrowser.tabs).find()`, `browser?.getAttribute()`, `lazy.AIWindow.chatStore.findConversationById()`, `lazy.AIWindow.isAIWindowContentPage()`, `lazy.AIWindowUI.reopenConversationInTab()`
- 条件付き依存: `if (!win)` → `this.openConversation()`
- 参照: `browser.currentURI`, `tab.linkedBrowser`, `this.#topChromeWindow`, `win.gBrowser.selectedTab`, `win.gBrowser.tabs`

## AIWindow.#onViewAllChatsSelected()
- 位置: L3465-3467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#topChromeWindow?.FirefoxViewHandler.openTab()`

## AIWindow.#onSmartWindowSettingsSelected()
- 位置: L3470-3472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#topChromeWindow?.openPreferences()`

## AIWindow.#onHistoryMenuEvent()
- 位置: L3475-3493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onRecentChatSelected()`, `this.#onSmartWindowSettingsSelected()`, `this.#onViewAllChatsSelected()`, `this.#refreshRecentChats()`, `this.onCreateNewChatClick()`
- 参照: `event.detail.conversationId`, `event.type`

## AIWindow.#onPanelShowing()
- 位置: L3499-3508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.composedPath()`, `panel.hasAttribute()`
- 条件付き依存: `if (panel !== this.#openPanel && this.#openPanel?.open)` → `this.#openPanel.hide()`
- 参照: `panel?.localName`, `this.#openPanel`, `this.#openPanel?.open`

## AIWindow.#historyMenu()
- 位置: L3511-3516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.recentChats`

## AIWindow.showSearchingIndicator()
- 位置: L3518-3526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchMessageToChatContent()`
- 参照: `this.conversationId`

## AIWindow.reloadAndContinue()
- 位置: async L3528-3534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#continueAfterToolResult()`, `this.openConversation()`

## AIWindow.#continueAfterToolResult()
- 位置: async L3536-3563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conversation.messages .filter()`, `this.#dispatchChromeEvent()`, `this.#fetchAIResponse()`, `this.#getAIWindowEventOptions()`
- 条件付き依存: `if (lastToolName === "search_the_web")` → `JSON.parse()`
- 条件付き依存: `if (query)` → `this.showSearchingIndicator()`
- 参照: `lastToolCall.content.body.tool_calls`, `lastToolCall.content.body.tool_calls[0].function.arguments`, `lastToolCall?.content?.body?.tool_calls`, `lastToolCall?.content?.body?.tool_calls?.[0]?.function?.name`, `lazy.MESSAGE_ROLE.ASSISTANT`, `m.role`, `m?.content?.type`

## AIWindow.handleFooterAction()
- 位置: L3565-3613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.retryNoMemories.record()`, `this.#openFeedbackModal()`, `this.#openMemoriesLearnMore()`, `this.#openMemoriesSettings()`, `this.#removeAppliedMemory()`, `this.#retryAfterError()`, `this.#retryFromAssistantMessageId()`
- 条件付き依存: `if (data.open)` → `Glean.smartWindow.memoryAppliedClick.record()`
- 参照: `data.open`, `this.#conversation?.messageCount`, `this.conversationId`, `this.mode`

## AIWindow.handleToolUIUpdate()
- 位置: async L3615-3642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AgentUI.isAgentUpdate()`, `lazy.ToolUI.handleUpdate()`
- 条件付き依存: `if (lazy.AgentUI.isAgentUpdate(data))` → `lazy.AgentUI.handleUpdate()`
- 条件付き依存: `if (retryPrompt)` → `this.submitChatMessage()`
- 参照: `data?.updateData?.prompt`, `data?.updateType`, `lazy.UI_UPDATE_TYPES.RETRY_PROMPT`, `this.#conversation`, `this.#topChromeWindow`, `this.mode`

## AIWindow.#buildChatLogPayload()
- 位置: L3644-3673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messages.filter()`
- 条件付き依存: `if (msg.content?.body?.tool_calls?.length)` → `msg.content.body.tool_calls.filter()`
- 参照: `lazy.GET_PAGE_CONTENT`, `lazy.MESSAGE_ROLE.TOOL`, `messages.length`, `msg.content?.body?.tool_calls?.length`, `msg.content?.name`, `msg.role`, `remaining.length`, `tc.function?.name`, `this.#conversation?.messages`, `withoutPageContent.length`

## AIWindow.applyHistoryAssets()
- 位置: L3683-3689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conversation?.applyHistoryAssets()`
- 参照: `this.conversationId`

## AIWindow.#openFeedbackModal()
- 位置: L3691-3709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FeedbackModal.open()`, `this.#buildChatLogPayload()`
- 参照: `this.#conversation?.messageCount`, `this.#conversation?.systemPromptVersion`, `this.#topChromeWindow?.gBrowser?.selectedBrowser`, `this.modelName`

## AIWindow.#openMemoriesSettings()
- 位置: L3711-3713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#topChromeWindow?.openPreferences()`

## AIWindow.#openMemoriesLearnMore()
- 位置: L3715-3717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#topChromeWindow?.openHelpLink()`

## AIWindow.#getMessageById()
- 位置: L3719-3721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conversation.messages.find()`
- 参照: `m.id`

## AIWindow.#getUserMessageForAssistantId()
- 位置: L3723-3730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getMessageById()`
- 参照: `assistantMsg.parentMessageId`, `assistantMsg?.parentMessageId`

## AIWindow.#retryAfterError()
- 位置: L3732-3746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#fetchAIResponse()`, `this.#fetchAIResponse("", { isRetry: true }) .catch()`
- 条件付き依存: `if (this._isRetrying)` → `console.warn()`
- 参照: `this._isRetrying`

## AIWindow.#retryFromAssistantMessageId()
- 位置: async L3748-3795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `actor?.dispatchTruncateToChatContent()`, `lazy.AIWindow.chatStore.deleteMessages()`, `this.#conversation.retryMessage()`, `this.#fetchAIResponse()`, `this.#getAIChatContentActor()`, `this.#getModelRequestLatencyAndDuration()`, `this.#getUserMessageForAssistantId()`, `this.#handleError()`, `this.#updateConversation()`
- 条件付き依存: `if (this._isRetrying)` → `console.warn()`
- 参照: `e.clientReason`, `this.#memoriesIconShown`, `this.#memoriesToggled`, `this._isRetrying`, `userMsg.content.body`, `userMsg.content.contextMentions`, `userMsg.pageUrl`

## AIWindow.#removeAppliedMemory()
- 位置: async L3797-3826
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor?.dispatchRemoveAppliedMemoryToChatContent()`, `console.error()`, `lazy.MemoriesManager.hardDeleteMemoryById()`, `msg?.memoriesApplied.filter()`, `this.#getAIChatContentActor()`, `this.#getMessageById()`
- 条件付き依存: `if (!deleted)` → `console.warn()`
- 参照: `m.id`, `memory.id`, `msg.memoriesApplied`, `remaining?.length`

## AIWindow.#footerTemplate()
- 位置: L3828-3833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.showFooter`

## AIWindow.#promoTemplate()
- 位置: L3835-3842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.promoMessage`

## AIWindow.render()
- 位置: L3844-3954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#footerTemplate()`, `this.#historyMenu()`, `this.#promoTemplate()`
- 参照: `MODE.FULLPAGE`, `MODE.SIDEBAR`, `this .#handlePromptDismissed`, `this .#handlePromptSelected`, `this .#handleResumeCardMenuItemSelected`, `this .#handleResumeCardResume`, `this .#handleResumeSectionHide`, `this .#handleTopSiteSelected`, `this.#onCloseSidebarClick`, `this.#starters`, `this.isGenerating`, `this.mode`, `this.onCreateNewChatClick`, `this.resumeCards`, `this.resumeCards.length`, `this.resumeCardsEmptyReason`, `this.resumeCardsLoading`, `this.resumeCardsPref`, `this.resumeSectionHidden`, `this.showDisclaimer`, `this.showStarters`, `this.startersResolved`, `this.topSites`
