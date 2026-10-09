# browser/components/aiwindow/ui/components/aitab-page/aitab-page.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-page.mjs
source-hash: 1c8dca9d162cc1f0fe0700289b23cdc57ca14e02
lines: 294

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITabPage.constructor()
- 位置: L44-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#renderCards.bind()`, `this.#renderHighlights.bind()`, `this.#renderList.bind()`, `this.#renderRankedTable.bind()`, `this.#renderSourceLinks.bind()`, `this.#renderTextBlock.bind()`, `this.#renderTimeline.bind()`, `this.#renderers.set()`
- 参照: `this.#renderers`, `this.page`, `this.status`

## AITabPage.connectedCallback()
- 位置: L59-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `super.connectedCallback()`, `this.#loadPage()`, `this.#loadPage().catch()`
- 参照: `this.status`

## AITabPage.pageName()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URLSearchParams(window.location.search).get()`
- 参照: `window.location.search`

## AITabPage.#loadPage()
- 位置: async L77-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#request()`
- 参照: `response.page`, `response?.error`, `response?.success`, `this.page`, `this.pageName`, `this.status`

## AITabPage.#deletePage()
- 位置: async L97-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#request()`
- 参照: `response?.error`, `response?.success`, `this.page`, `this.status`

## AITabPage.#request()
- 位置: L114-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addEventListener()`, `this.dispatchEvent()`

## onResponse()
- 位置: L116-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `this.removeEventListener()`
- 参照: `event.detail`

## onError()
- 位置: L120-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`, `this.removeEventListener()`
- 参照: `event.detail?.error`

## AITabPage.#renderHeader()
- 位置: L134-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `html()`, `this.#deletePage()`, `this.#deletePage().catch()`
- 参照: `document.title`, `header.references?.items`, `header.subhead`, `header.title`, `this.page?.createdAtLabel`, `this.status`

## AITabPage.#renderHighlights()
- 位置: L158-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `highlights.component.toLowerCase()`, `html()`, `this.#renderBlock()`
- 参照: `highlights.items`, `highlights.title`

## AITabPage.#renderSourceLinks()
- 位置: L173-175
- 役割: (未記入)
- 触るとき: (未記入)

## AITabPage.#renderTextBlock()
- 位置: L177-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `textBlock.component.toLowerCase()`, `this.#renderBlock()`
- 参照: `textBlock.lead`, `textBlock.paragraphs`, `textBlock.references`

## AITabPage.#renderRankedTable()
- 位置: L190-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `rankedTable.component.toLowerCase()`, `this.#renderBlock()`
- 参照: `rankedTable.columns`, `rankedTable.description`, `rankedTable.rows`, `rankedTable.title`

## AITabPage.#renderCards()
- 位置: L204-206
- 役割: (未記入)
- 触るとき: (未記入)

## AITabPage.#renderTimeline()
- 位置: L208-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderBlock()`, `timeline.component.toLowerCase()`
- 参照: `timeline.description`, `timeline.items`, `timeline.title`

## AITabPage.#renderList()
- 位置: L221-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `list.component.toLowerCase()`, `this.#renderBlock()`
- 参照: `list.description`, `list.groups`, `list.layout`, `list.title`

## AITabPage.#renderBlock()
- 位置: L235-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `block.html`, `block.type`, `block?.type`

## AITabPage.#renderFooter()
- 位置: L247-249
- 役割: (未記入)
- 触るとき: (未記入)

## AITabPage.#renderStatus()
- 位置: L251-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.status`

## AITabPage.render()
- 位置: L259-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderPage()`, `this.#renderStatus()`
- 参照: `this.status`

## AITabPage.#renderPage()
- 位置: L269-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `children.slice()`, `html()`, `this.#renderBlocks()`, `this.#renderFooter()`, `this.#renderHeader()`
- 参照: `children[0]?.component`, `this.page.children`

## AITabPage.#renderBlocks()
- 位置: L280-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `block.component?.toLowerCase()`, `blocks.map()`, `html()`, `renderer()`, `this.#renderers.get()`
