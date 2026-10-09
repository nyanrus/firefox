# browser/components/aiwindow/ui/components/ai-chat-table/ai-chat-table.mjs

source: browser/components/aiwindow/ui/components/ai-chat-table/ai-chat-table.mjs
source-hash: 49952b2c26a0c35b5568a108089c480171b15f29
lines: 132

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIChatTable.constructor()
- 位置: L23-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.isOverflowing`

## AIChatTable.firstUpdated()
- 位置: L28-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observeTable()`, `this.#resizeObserver.observe()`, `this.#updateOverflow()`, `this.renderRoot.querySelector()`
- 参照: `this.#resizeObserver`, `this.#scrollContainer`

## AIChatTable.disconnectedCallback()
- 位置: L38-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#resizeObserver?.disconnect()`
- 参照: `this.#observedTable`, `this.#resizeObserver`, `this.#scrollContainer`

## AIChatTable.#observeTable()
- 位置: L46-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`
- 条件付き依存: `if (this.#observedTable)` → `this.#resizeObserver?.unobserve()`
- 条件付き依存: `if (table)` → `this.#resizeObserver?.observe()`
- 参照: `this.#observedTable`

## AIChatTable.#onSlotChange()
- 位置: L60-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observeTable()`, `this.#updateOverflow()`

## AIChatTable.#updateOverflow()
- 位置: L65-71
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `container.clientWidth`, `container.scrollWidth`, `this.#scrollContainer`, `this.isOverflowing`

## AIChatTable.#messageId()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`
- 参照: `this.getRootNode()?.host?.dataset.messageId`

## AIChatTable.#handleCopyTable()
- 位置: L84-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.#messageId`, `this.lineRange`

## AIChatTable.render()
- 位置: L97-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#handleCopyTable`, `this.#messageId`, `this.#onSlotChange`, `this.isOverflowing`, `this.lineRange`
