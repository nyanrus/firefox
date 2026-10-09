# browser/components/aiwindow/ui/components/ai-chat-message/ai-chat-message.mjs

source: browser/components/aiwindow/ui/components/ai-chat-message/ai-chat-message.mjs
source-hash: 74c13e6e882e5c1c34fd069647065f77e3024c95
lines: 848

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.values()`, `customElements.define()`, `this.#chatMessageSanitizer.allowAttribute()`, `this.#chatMessageSanitizer.allowElement()`

## AIChatMessage.constructor()
- 位置: L100-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.conversationId`, `this.historyResults`, `this.seenUrls`

## AIChatMessage.connectedCallback()
- 位置: L128-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#initLinkNavigationListener()`

## AIChatMessage.#initLinkNavigationListener()
- 位置: L133-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.addEventListener()`
- 条件付き依存: `if (target.tagName === "A" && target.href)` → `event.preventDefault()`
- 条件付き依存: `if (target.tagName === "A" && target.href)` → `this.dispatchEvent()`
- 参照: `event.altKey`, `event.button`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `event.target`, `target.href`, `target.parentElement`, `target.tagName`, `this.shadowRoot`

## AIChatMessage.willUpdate()
- 位置: L165-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changed.has()`, `this.#urlsUnfurledInMessage.intersection()`
- 参照: `this.#unfurledUrlsNeedUpdating`, `this.#urlsUnfurledInMessage.intersection(this.seenUrls).size`, `this.seenUrls`

## AIChatMessage.updated()
- 位置: L186-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changed.has()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `this.shadowRoot?.querySelector()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `(messageEl.innerText || messageEl.textContent || "") .replace(/\s+/g, " ") .trim()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `(messageEl.innerText || messageEl.textContent || "") .replace()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `this.dispatchEvent()`
- 参照: `messageEl.innerText`, `messageEl.textContent`, `this.complete`, `this.messageId`, `this.role`

## AIChatMessage.#getIconSrc()
- 位置: L204-210
- 役割: (未記入)
- 触るとき: (未記入)

## AIChatMessage.#replaceWebsiteMentions()
- 位置: L239-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.replaceWith()`, `href.startsWith()`, `href.substring()`, `params.get()`, `root.ownerDocument.createElement()`, `root.querySelectorAll()`
- 条件付き依存: `if (!(isTabGroup))` → `this.#getIconSrc()`
- 参照: `MENTION_PREFIX.length`, `a.textContent`, `chip.href`, `chip.iconSrc`, `chip.isTabGroup`, `chip.label`, `chip.tabGroupColor`, `chip.type`, `linkHref.length`

## AIChatMessage.#unfurlUnseenLinks()
- 位置: L296-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `isSettingsURL()`, `isSmartPageURL()`, `root.querySelectorAll()`, `this.seenUrls.has()`
- 条件付き依存: `if ( !parsed || (parsed.protocol !== "http:" && parsed.protocol !== "https:") )` → `anchor.removeAttribute()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `this.#urlsUnfurledInMessage.add()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `URL.parse()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `textContent.trim()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `doc.createElement()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `disclosure.append()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `anchor.replaceWith()`
- 参照: `anchor.href`, `anchor.ownerDocument`, `label.className`, `label.textContent`, `link.href`, `link.textContent`, `parsed.protocol`, `this.#urlsUnfurledInMessage`

## AIChatMessage.#isHistoryItem()
- 位置: L353-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `li.querySelector()`, `this.historyResults.has()`
- 参照: `link.href`

## AIChatMessage.#replaceHistoryResults()
- 位置: L370-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `items.some()`, `list.querySelectorAll()`, `lists.forEach()`, `root.querySelectorAll()`, `this.#isHistoryItem()`
- 条件付き依存: `if (this.complete)` → `items.every()`
- 条件付き依存: `if (this.complete)` → `this.#isHistoryItem()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `items.map()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `this.historyResults.get()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `li.querySelector()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `list.replaceWith()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `this.#getHistoryListGrid()`
- 参照: `allListItems.length`, `items.length`, `li.querySelector("a[href]").href`, `list.style.display`, `this.complete`, `this.historyResults?.size`

## AIChatMessage.#getHistoryListGrid()
- 位置: L423-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(gridItems || []).slice()`, `items.forEach()`, `items.some()`, `this.#calculateHistoryGridView()`, `this.#historyGrids.has()`, `this.#historyGrids.set()`, `this.#renderHistoryGridRow.bind()`, `this.#renderHistoryGridTile.bind()`, `this.#requestHistoryAssets()`, `this.dispatchEvent()`, `this.ownerDocument.createElement()`
- 条件付き依存: `if (this.#historyGrids.has(index))` → `this.#historyGrids.get()`
- 参照: `grid.gridItem`, `grid.items`, `grid.loading`, `grid.rowItem`, `grid.showSwitch`, `grid.view`, `historyGrid.items`, `historyGrid.loading`, `historyGrid.view`, `item.image`, `item.resultCount`, `item.resultIndex`, `item.thumbnail`, `items.length`

## AIChatMessage.#requestHistoryAssets()
- 位置: L479-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items .filter()`, `items .filter(item => item?.url) .map()`, `this.dispatchEvent()`
- 参照: `item?.url`, `requestItems.length`, `this.conversationId`, `this.messageId`

## AIChatMessage.#calculateHistoryGridView()
- 位置: L512-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.forEach()`, `this.#getFaviconUri()`
- 参照: `item.faviconUrl`, `item.image`, `item.url`, `items.length`

## AIChatMessage.#renderHistoryGridTile()
- 位置: L537-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.itemClick.bind()`
- 参照: `item.faviconUrl`, `item.hasFavicon`, `item.image`, `item.timestamp`, `item.title`, `item.url`

## AIChatMessage.#renderHistoryGridRow()
- 位置: L561-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#getFaviconUri()`, `this.itemClick.bind()`
- 参照: `item.timestamp`, `item.title`, `item.url`

## AIChatMessage.itemClick()
- 位置: L588-598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIChatMessage.#getFaviconUri()
- 位置: L608-610
- 役割: (未記入)
- 触るとき: (未記入)

## AIChatMessage.#parseMarkdown()
- 位置: L639-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchClientError()`, `element.setHTML()`, `parseMarkdown()`
- 参照: `AIChatMessage.#chatMessageSanitizer`

## AIChatMessage.parseUserMarkdown()
- 位置: L656-659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#parseMarkdown()`, `this.#replaceWebsiteMentions()`

## AIChatMessage.#renderBlockElement()
- 位置: L668-679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchClientError()`, `scratch.setHTML()`, `this.ownerDocument.createElement()`
- 参照: `AIChatMessage.#chatMessageSanitizer`, `scratch.firstElementChild`

## AIChatMessage.#reconcileBlocks()
- 位置: L691-714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.lastElementChild.remove()`, `this.#renderBlockElement()`
- 条件付き依存: `if (container.children[i])` → `container.replaceChild()`
- 条件付き依存: `if (!(container.children[i]))` → `container.append()`
- 参照: `container.children`, `container.children.length`, `newHtml.length`, `this.#blockHtml`

## AIChatMessage.getAssistantMessage()
- 位置: L724-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseMarkdownBlocks()`, `parseMarkdownBlocks(this.message).map()`, `performance.measure()`, `performance.now()`, `this.#reconcileBlocks()`, `this.#replaceHistoryResults()`, `this.#unfurlUnseenLinks()`
- 条件付き依存: `if (this.messageL10n?.id)` → `this.#renderL10nMessage()`
- 条件付き依存: `if (!this.#lastMessageElement)` → `this.ownerDocument.createElement()`
- 条件付き依存: `if (!this.message)` → `messageElement.replaceChildren()`
- 条件付き依存: `if (!this.message)` → `messageElement.classList.remove()`
- 条件付き依存: `if (this.historyResults?.size)` → `messageElement.classList.add()`
- 条件付き依存: `if (!(this.historyResults?.size))` → `messageElement.classList.remove()`
- 参照: `block.html`, `blockHtml.length`, `this.#blockHtml`, `this.#lastMessage`, `this.#lastMessageElement`, `this.#lastMessageElement.className`, `this.#unfurledUrlsNeedUpdating`, `this.historyResults?.size`, `this.message`, `this.messageL10n?.id`, `this.role`

## AIChatMessage.getUserMessage()
- 位置: L797-808
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerDocument.createElement()`, `this.parseUserMarkdown()`
- 参照: `messageElement.className`, `this.message`, `this.role`

## AIChatMessage.#renderL10nMessage()
- 位置: L817-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `link.href`, `link.l10nName`, `this.messageL10n`

## AIChatMessage.render()
- 位置: L831-844
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.getAssistantMessage()`, `this.getUserMessage()`
- 参照: `this.role`
