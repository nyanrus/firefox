# browser/components/firefoxview/chats.mjs

source: browser/components/firefoxview/chats.mjs
source-hash: 5ed931be9a7ebcec49ecb04c21f23b299a89fb12
lines: 311

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`, `customElements.define()`

## ChatsInView.constructor()
- 位置: L44-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._started`, `this.cumulativeSearches`, `this.fullyUpdated`, `this.maxTabsLength`

## ChatsInView.disconnectedCallback()
- 位置: L57-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.stop()`

## ChatsInView.viewVisibleCallback()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.start()`

## ChatsInView.viewHiddenCallback()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stop()`

## ChatsInView.willUpdate()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.fullyUpdated`

## ChatsInView.updated()
- 位置: L74-79
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.lists?.length)` → `this.toggleVisibilityInCardContainer()`
- 参照: `this.fullyUpdated`, `this.lists?.length`

## ChatsInView.getUpdateComplete()
- 位置: async L81-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.cards).map()`, `Promise.all()`, `super.getUpdateComplete()`
- 参照: `card.updateComplete`, `this.cards`

## ChatsInView.start()
- 位置: L86-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.updateCache()`, `this.toggleVisibilityInCardContainer()`
- 参照: `this._started`

## ChatsInView.stop()
- 位置: L97-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleVisibilityInCardContainer()`
- 参照: `this._started`

## ChatsInView.onPrimaryAction()
- 位置: async L106-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.getMostRecentPageVisited()`, `event.preventDefault()`, `lazy.AIWindow.chatStore.findConversationById()`
- 条件付き依存: `if (!convId)` → `lazy.log.error()`
- 条件付き依存: `if (!conversation)` → `lazy.log.error()`
- 条件付き依存: `if (mostRecentPage?.href)` → `lazy.URILoadingHelper.openTrustedLinkIn()`
- 条件付き依存: `if (!(mostRecentPage?.href))` → `lazy.URILoadingHelper.openTrustedLinkIn()`
- 参照: `event.detail?.item`, `event.message`, `event.stack`, `event.target.documentGlobal`, `item?.convId`, `lazy.AIWindow.newTabURL`, `mostRecentPage.href`, `mostRecentPage?.href`, `this.controller.searchQuery`, `this.cumulativeSearches`

## resolveOnContentBrowserCreated()
- 位置: async L135-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.openSidebar()`
- 参照: `targetBrowser.documentGlobal`

## resolveOnContentBrowserCreated()
- 位置: async L149-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.openInFullWindow()`

## ChatsInView.onSecondaryAction()
- 位置: L161-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelList.toggle()`
- 参照: `e.detail.originalEvent`, `e.originalTarget`, `this.triggerNode`

## ChatsInView.deleteChat()
- 位置: L166-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.controller .deleteChat()`, `this.controller .deleteChat() .catch()`
- 参照: `e.message`, `e.stack`

## ChatsInView.onSearchQuery()
- 位置: L174-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.onSearchQuery()`
- 参照: `this.controller.searchQuery`, `this.cumulativeSearches`

## ChatsInView.panelListTemplate()
- 位置: L181-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.deleteChat`

## ChatsInView.cardsTemplate()
- 位置: L196-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emptyMessageTemplate()`
- 条件付き依存: `if (this.controller.searchQuery)` → `this.#searchResultsTemplate()`
- 条件付き依存: `if (!this.controller.isChatEmpty)` → `this.#chatCardsTemplate()`
- 参照: `this.controller.isChatEmpty`, `this.controller.searchQuery`

## ChatsInView.#chatCardsTemplate()
- 位置: L205-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `chat.l10nId.includes()`, `html()`, `this.controller.totalChats.map()`
- 参照: `chat.items`, `chat.items[0].time`, `chat.l10nId`, `this.maxTabsLength`, `this.onPrimaryAction`, `this.onSecondaryAction`

## ChatsInView.#emptyMessageTemplate()
- 位置: L232-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `html()`
- 参照: `this.selectedTab`
- XPCOM: `Services.prefs`

## ChatsInView.#searchResultsTemplate()
- 位置: L252-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`, `when()`
- 参照: `this.controller.searchQuery`, `this.controller.searchResults`, `this.controller.searchResults.length`, `this.onPrimaryAction`, `this.onSecondaryAction`

## ChatsInView.render()
- 位置: L288-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.panelListTemplate()`
- 参照: `this.cardsTemplate`, `this.onSearchQuery`, `this.selectedTab`
