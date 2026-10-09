# browser/components/aiwindow/models/Tools.sys.mjs

source: browser/components/aiwindow/models/Tools.sys.mjs
source-hash: 8d47e4d3093669626ce086a0eecd76043f372104
lines: 1821

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `console.createInstance()`

## getEmbeddingsGenerator()
- 位置: L93-98
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!_embeddingsGenerator)` → `EmbeddingsGenerator.forGeneral()`

## embedTexts()
- 位置: async L100-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getEmbeddingsGenerator()`, `getEmbeddingsGenerator().embedMany()`
- 参照: `result.output`

## keywordRecall()
- 位置: L105-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `titleTokens.has()`
- 参照: `topicTokens.size`

## selectSearchTheWebPath()
- 位置: L189-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `openAIEngine.usesCustomEndpoint()`
- 参照: `SEARCH_THE_WEB_PATH.ANSWERS`, `SEARCH_THE_WEB_PATH.FAST`, `SEARCH_THE_WEB_PATH.GROUNDED`
- XPCOM: `Services.prefs`

## searchTheWebToolConfig()
- 位置: L351-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectSearchTheWebPath()`
- 参照: `SEARCH_THE_WEB_PATH.ANSWERS`, `SEARCH_THE_WEB_PATH.FAST`

## getTabList()
- 位置: L636-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `tabs.slice()`, `tabs.sort()`
- 条件付き依存: `if (!win.closed && win.gBrowser)` → `lazy.SessionStore.getWindowId()`
- 条件付き依存: `if (!win.closed && win.gBrowser)` → `isAllowedURLProtocol()`
- 条件付き依存: `if (!win.closed && win.gBrowser)` → `isNewPageUrl()`
- 条件付き依存: `if (isAllowedURLProtocol(url) && !isNewPageUrl(url))` → `tabs.push()`
- 条件付き依存: `if (isAllowedURLProtocol(url) && !isNewPageUrl(url))` → `sanitizeUntrustedContent()`
- 参照: `a.lastAccessed`, `b.lastAccessed`, `browser?.currentURI?.spec`, `lazy.BrowserWindowTracker.orderedWindows`, `tab.label`, `tab.lastAccessed`, `tab.linkedBrowser`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## getOpenTabs()
- 位置: async L690-752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation.addSeenUrls()`, `conversation.securityProperties.setPrivateData()`, `getTabList()`, `lazy.console.log()`, `recentTabs.map()`, `tabs.slice()`
- 条件付き依存: `if (topic)` → `ChromeUtils.now()`
- 条件付き依存: `if (topic)` → `tabs.map()`
- 条件付き依存: `if (topic)` → `SmartTabGroupingManager.preprocessText()`
- 条件付き依存: `if (topic)` → `_embeddingFunctions.embedTexts()`
- 条件付き依存: `if (topic)` → `tokenizer.tokenize()`
- 条件付き依存: `if (topic)` → `cosSim()`
- 条件付き依存: `if (topic)` → `_embeddingFunctions.keywordRecall()`
- 条件付き依存: `if (topic)` → `scored.sort()`
- 条件付き依存: `if (topic)` → `tabs.push()`
- 条件付き依存: `if (topic)` → `scored.map()`
- 条件付き依存: `if (topic)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (topic)` → `lazy.console.warn()`
- 参照: `a.score`, `b.score`, `recentTabs.length`, `s.tab`, `t.title`, `tabs.length`

## searchBrowsingHistory()
- 位置: async L780-825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addHistoryResults()`, `conversation.addSeenUrls()`, `conversation.securityProperties.setPrivateData()`, `implSearchBrowsingHistory()`, `lazy.console.log()`, `result.results.map()`, `sanitizeUntrustedContent()`
- 参照: `result.results`

## RunSearch.#ensureTabSelected()
- 位置: L836-840
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab.documentGlobal.gBrowser.selectedTab`, `tab.selected`

## RunSearch.runSearch()
- 位置: async L848-927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RunSearch.#extractSerpContent()`, `RunSearch.#performSearchAndWait()`, `RunSearch.#showSearchingIndicator()`, `console.error()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `lazy.AIWindow.isAIWindowContentPage()`, `lazy.console.log()`, `query.trim()`, `sh.getEntryAtIndex()`, `win.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (!(toolParams.query))` → `ChatStore.getMostRecentMessages()`
- 条件付き依存: `if (targetTab)` → `RunSearch.#ensureTabSelected()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowContentPage(originalBrowser.currentURI))` → `RunSearch.#moveToSidebarIfNeeded()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowContentPage(originalBrowser.currentURI))` → `RunSearch.#ensureTabSelected()`
- 参照: `MESSAGE_ROLE.USER`, `browsingContext.embedderElement`, `browsingContext.topChromeWindow`, `e.message`, `entry.hasUserInteraction`, `originalBrowser.browsingContext?.sessionHistory`, `originalBrowser.currentURI`, `recentUserMessages.length`, `recentUserMessages[0].content.body`, `sh.index`, `toolParams.query`, `win.closed`

## RunSearch.#showSearchingIndicator()
- 位置: L939-956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiBrowser.contentDocument.querySelector()`, `sidebar.querySelector()`, `win.document.getElementById()`
- 条件付き依存: `if (aiWindow?.showSearchingIndicator)` → `aiWindow.showSearchingIndicator()`
- 参照: `aiBrowser?.contentDocument`, `aiWindow?.showSearchingIndicator`

## RunSearch.#moveToSidebarIfNeeded()
- 位置: async L958-960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.moveConversationToSidebar()`

## RunSearch.#performSearchAndWait()
- 位置: async L969-1007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `lazy.AIWindow.focusSidebar()`, `lazy.AIWindow.performSearch()`, `lazy.setTimeout()`, `reject()`, `win.gBrowser.addProgressListener()`, `win.gBrowser.removeProgressListener()`
- 参照: `RunSearch.CONTENT_SETTLE_MS`, `RunSearch.NAVIGATION_TIMEOUT_MS`

## RunSearch.onStateChange()
- 位置: L981-990
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ((stateFlags & complete) === complete)` → `lazy.clearTimeout()`
- 条件付き依存: `if ((stateFlags & complete) === complete)` → `win.gBrowser.removeProgressListener()`
- 条件付き依存: `if ((stateFlags & complete) === complete)` → `resolve()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## RunSearch.onLocationChange()
- 位置: L991-991
- 役割: (未記入)
- 触るとき: (未記入)

## RunSearch.onProgressChange()
- 位置: L992-992
- 役割: (未記入)
- 触るとき: (未記入)

## RunSearch.onStatusChange()
- 位置: L993-993
- 役割: (未記入)
- 触るとき: (未記入)

## RunSearch.onSecurityChange()
- 位置: L994-994
- 役割: (未記入)
- 触るとき: (未記入)

## RunSearch.onContentBlockingEvent()
- 位置: L995-995
- 役割: (未記入)
- 触るとき: (未記入)

## RunSearch.#extractSerpContent()
- 位置: async L1016-1046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `pageExtractor.getText()`, `windowContext.getActor()`
- 参照: `RunSearch.MAX_CHARACTERS`, `browser.browsingContext?.currentWindowContext`, `browser.currentURI?.spec`, `result.links`, `result.text`

## raceAbort()
- 位置: L1058-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promise.catch()`, `promise.then()`, `reject()`, `resolve()`, `signal.addEventListener()`, `signal.removeEventListener()`
- 条件付き依存: `if (signal.aborted)` → `onAbort()`
- 参照: `signal.aborted`

## onAbort()
- 位置: L1065-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`

## GetPageContent.getPageContentText()
- 位置: async L1101-1107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.getPageContent()`, `results.map()`
- 参照: `result.content`

## GetPageContent.getPageContent()
- 位置: async L1124-1207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `GetPageContent.#getPageContentsForSingleURL()`, `Promise.all()`, `console.error()`, `conversation.getAllMentionURLs()`, `isAllowedURLProtocol()`, `lazy.console.log()`, `url_list.map()`
- 条件付き依存: `if (error?.name === "TimeoutError")` → `lazy.console.log()`
- 条件付き依存: `if (error?.name === "BlockedError")` → `lazy.console.log()`
- 参照: `error?.name`, `signal?.aborted`

## GetPageContent.isContentAllowed()
- 位置: L1218-1251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.getTabWithURL()`, `conversation.getAllMentionURLs()`, `conversation.getAllMentionURLs().has()`, `conversation.serpUrlsForAnonymousFetch.has()`, `isAllowedURLProtocol()`
- 参照: `conversation.securityProperties.privateData`, `conversation.securityProperties.untrustedInput`

## GetPageContent.getTabWithURL()
- 位置: L1259-1273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `tab?.linkedBrowser?.currentURI?.spec`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## GetPageContent.#getPageContentsForSingleURL()
- 位置: async L1285-1370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.getTabWithURL()`, `PageExtractorParent.getHeadlessExtractor()`, `mentionedUrls.has()`
- 条件付き依存: `if (!currentWindowContext)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if (tab)` → `currentWindowContext.getActor()`
- 条件付き依存: `if (tab)` → `GetPageContent.#runExtraction()`
- 条件付き依存: `if (tab)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if ( !mentionedUrls.has(url) && conversation.securityProperties.untrustedInput && conversation.securityProperties.privateData )` → `conversation.serpUrlsForAnonymousFetch.has()`
- 条件付き依存: `if (conversation.serpUrlsForAnonymousFetch.has(url))` → `PageExtractorParent.getHeadlessExtractor()`
- 参照: `conversation.securityProperties.privateData`, `conversation.securityProperties.untrustedInput`, `signal?.aborted`, `tab.label`, `tab.linkedBrowser.browsingContext?.currentWindowContext`

## callback()
- 位置: L1338-1346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.#runExtraction()`

## callback()
- 位置: L1360-1368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.#runExtraction()`

## GetPageContent.#runExtraction()
- 位置: async L1389-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addSeenUrls()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `pageExtractor.getText()`, `raceAbort()`, `text?.trim()`
- 参照: `GetPageContent.MAX_CHARACTERS`

## getNavigationInfo()
- 位置: async L1445-1457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SmartWindowNavigationInfo.getRelevantNavigation()`, `query.trim()`

## getUserMemories()
- 位置: async L1465-1475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.securityProperties.setPrivateData()`, `lazy.MemoriesManager.getAllMemories()`, `lazy.console.log()`, `memories.map()`
- 参照: `memory.memory_summary`

## addMemory()
- 位置: async L1488-1513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MemoriesManager.enrichExistingMemory()`, `lazy.MemoriesManager.enrichExistingMemory( result.memory.id, memorySummary ).catch()`, `lazy.MemoriesManager.saveRequestedMemory()`, `lazy.console.error()`, `lazy.console.log()`
- 参照: `conversation.securityProperties.untrustedInput`, `result.action`, `result.memory`, `result.memory.id`, `result.memory.memory_summary`, `result.ok`, `result.reason`

## persistAITabPage()
- 位置: async L1530-1561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AITabStore.deleteVersionsBefore()`, `lazy.AITabStore.deleteVersionsBefore(stored.slug, stored.version).catch()`, `lazy.AITabStore.edit()`, `lazy.console.error()`
- 条件付き依存: `if (!isModification)` → `lazy.AITabStore.create()`
- 参照: `conversation.id`, `e.message`, `metadata.id`, `metadata.title`, `stored.slug`, `stored.version`

## createAITab()
- 位置: async L1580-1657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `conversation.addSeenUrls()`, `conversation.convertUrlToToken()`, `lazy.AITab.buildViewerURL()`, `lazy.AITab.generateAITab()`, `lazy.console.error()`, `lazy.console.log()`, `modify_slug.trim()`, `persistAITabPage()`, `sanitizeUntrustedContent()`
- 参照: `UI_TYPES.AITAB`, `e.message`, `result.error`, `result.metadata?.title`, `stored.slug`, `stored.uuid`

## getSkill()
- 位置: async L1661-1663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSkillPrompt()`
- 参照: `toolParams?.name`

## countOpenAIWindowTabs()
- 位置: L1671-1685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isAllowedURLProtocol()`, `isNewPageUrl()`, `lazy.AIWindow.isAIWindowActive()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser?.currentURI?.spec`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## getActionTrigger()
- 位置: L1694-1701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_ACTIONS.includes()`, `conversation.getLatestUserMentionCount()`

## manageTabs()
- 位置: async L1718-1809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `TAB_ACTIONS.includes()`, `conversation.getLatestUserMentionCount()`, `countOpenAIWindowTabs()`, `getActionTrigger()`, `isAllowedURLProtocol()`, `lazy.ToolUITelemetry.recordBrowserActionSubmit()`, `manageTabsAction()`, `url_tokens.filter()`
- 条件付き依存: `if (actionTrigger === "unsupported")` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 条件付き依存: `if (!Array.isArray(url_tokens))` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 条件付き依存: `if (!validUrls.size)` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 参照: `conversation.id`, `conversation.lastSubmitType`, `conversation.messageCount`, `conversation.systemPromptVersion`, `validUrls.size`
