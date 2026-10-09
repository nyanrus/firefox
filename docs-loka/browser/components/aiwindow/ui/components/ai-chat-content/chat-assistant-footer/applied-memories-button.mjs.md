# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/applied-memories-button.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/applied-memories-button.mjs
source-hash: 71788348bd958e2bce90343fd8913b3d548641ad
lines: 412

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AppliedMemoriesButton.constructor()
- 位置: L61-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this._onDocumentClick.bind()`, `this._onKeyDown.bind()`
- 参照: `this._onDocumentClick`, `this._onKeyDown`, `this.appliedMemories`, `this.messageId`, `this.open`, `this.showCallout`

## AppliedMemoriesButton.connectedCallback()
- 位置: L72-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `super.connectedCallback()`, `this.addEventListener()`
- 参照: `this._onDocumentClick`, `this._onKeyDown`

## AppliedMemoriesButton.disconnectedCallback()
- 位置: L78-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.removeEventListener()`, `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this._onDocumentClick`, `this._onKeyDown`

## AppliedMemoriesButton.willUpdate()
- 位置: L84-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.willUpdate()`
- 参照: `this.#showCalloutState`, `this.showCallout`

## AppliedMemoriesButton.updated()
- 位置: L91-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.updated()`
- 条件付き依存: `if (changedProperties.has("showCallout"))` → `this.#syncCalloutOpenState()`

## AppliedMemoriesButton.#syncCalloutOpenState()
- 位置: L99-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToggleAppliedMemories()`, `this.#focusDeleteButtonAt()`, `this.toggleAttribute()`, `this.updateComplete.then()`
- 参照: `this.open`, `this.showCallout`

## AppliedMemoriesButton.#dispatchToggleAppliedMemories()
- 位置: L111-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.messageId`

## AppliedMemoriesButton._hasMemories()
- 位置: L124-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `this.appliedMemories`, `this.appliedMemories.length`

## AppliedMemoriesButton._visibleMemories()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.appliedMemories.slice()`

## AppliedMemoriesButton.#onTriggerClick()
- 位置: L132-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.#dispatchToggleAppliedMemories()`, `this.toggleAttribute()`
- 条件付き依存: `if (this.open)` → `this.updateComplete.then()`
- 条件付き依存: `if (this.open)` → `this.#focusDeleteButtonAt()`
- 参照: `this.#showCalloutState`, `this._hasMemories`, `this.open`

## AppliedMemoriesButton._onPopoverClick()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`

## AppliedMemoriesButton._onDocumentClick()
- 位置: L155-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closePopover()`
- 参照: `this.open`

## AppliedMemoriesButton._onKeyDown()
- 位置: L162-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`, `this.#closePopover()`, `this.#focusDeleteButtonAt()`, `this.#moveDeleteFocus()`, `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector(".memories-trigger")?.focus()`
- 条件付き依存: `if ( !event.shiftKey && this.shadowRoot.activeElement === this.shadowRoot.querySelector(".retry-without-memories-button") )` → `this.#closePopover()`
- 参照: `event.key`, `event.shiftKey`, `this.open`, `this.shadowRoot.activeElement`

## AppliedMemoriesButton.#deleteButtons()
- 位置: L201-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popover.querySelectorAll()`, `this.shadowRoot.querySelector()`

## AppliedMemoriesButton.#moveDeleteFocus()
- 位置: L208-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.indexOf()`, `this.#focusDeleteButtonAt()`
- 参照: `items.length`, `this.#deleteButtons`, `this.shadowRoot.activeElement`

## AppliedMemoriesButton.#focusDeleteButtonAt()
- 位置: L219-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.forEach()`, `items[index].focus()`
- 参照: `item.tabIndex`, `items.length`, `this.#deleteButtons`

## AppliedMemoriesButton.#closePopover()
- 位置: L233-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToggleAppliedMemories()`, `this.requestUpdate()`, `this.toggleAttribute()`
- 参照: `this.#showCalloutState`, `this.open`

## AppliedMemoriesButton._onRemoveMemory()
- 位置: L242-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.messageId`

## AppliedMemoriesButton._onRetryWithoutMemories()
- 位置: L257-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.messageId`

## AppliedMemoriesButton._onManageMemories()
- 位置: L271-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AppliedMemoriesButton.renderCallout()
- 位置: L280-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.dispatchEvent()`

## AppliedMemoriesButton.renderPopover()
- 位置: L304-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this._onManageMemories()`, `this._onPopoverClick()`, `this._onRemoveMemory()`, `this._onRetryWithoutMemories()`, `this.renderCallout()`, `visibleMemories.map()`
- 参照: `memory.memory_summary`, `this.#showCalloutState`, `this._hasMemories`, `this._visibleMemories`, `this.open`

## AppliedMemoriesButton.render()
- 位置: L383-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#onTriggerClick()`, `this.renderPopover()`
- 参照: `this._hasMemories`, `this.open`
