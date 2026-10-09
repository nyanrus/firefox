# browser/components/aiwindow/ui/components/ai-action-confirmation/ai-action-confirmation.mjs

source: browser/components/aiwindow/ui/components/ai-action-confirmation/ai-action-confirmation.mjs
source-hash: c522faef0e4345de37c8172b487b038568fad812
lines: 284

## <module>
- 役割: (未記入)
- 呼び出し先: `createRef()`, `customElements.define()`

## AIActionConfirmation.constructor()
- 位置: L49-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.canUndo`, `this.isExpanded`, `this.labelL10nArgs`, `this.labelL10nId`, `this.tabs`

## AIActionConfirmation.#handleUndo()
- 位置: L58-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIActionConfirmation.#handleToggle()
- 位置: L67-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.isExpanded`, `this.tabs.length`

## AIActionConfirmation.#handleTabClick()
- 位置: L87-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.dispatchEvent()`
- 参照: `tab.url`

## AIActionConfirmation.#updateOverflowState()
- 位置: L117-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `scroller.hasAttribute()`, `this.#updateListScrollFade()`
- 条件付き依存: `if (overflowing !== scroller.hasAttribute("data-overflowing"))` → `scroller.toggleAttribute()`
- 参照: `list.clientHeight`, `list.scrollHeight`, `list?.parentElement`, `this.#tabsListRef.value`

## AIActionConfirmation.#handleScroll()
- 位置: L135-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.supports()`, `this.#updateListScrollFade()`

## AIActionConfirmation.#updateListScrollFade()
- 位置: L142-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.supports()`, `progress.toFixed()`, `requestAnimationFrame()`, `scroller.style.setProperty()`
- 参照: `list?.parentElement`, `this.#scrollAnimationId`, `this.#tabsListRef.value`

## AIActionConfirmation.#renderTab()
- 位置: L172-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handleTabClick()`
- 参照: `tab.iconSrc`, `tab.title`, `tab.url`

## AIActionConfirmation.updated()
- 位置: L192-212
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#resizeObserver)` → `this.#updateOverflowState()`
- 条件付き依存: `if (this.#observedList)` → `this.#resizeObserver.unobserve()`
- 条件付き依存: `if (this.#observedList)` → `this.#observedList.removeEventListener()`
- 条件付き依存: `if (list)` → `this.#resizeObserver.observe()`
- 条件付き依存: `if (list)` → `list.addEventListener()`
- 参照: `this.#handleScroll`, `this.#observedList`, `this.#resizeObserver`, `this.#tabsListRef.value`

## AIActionConfirmation.disconnectedCallback()
- 位置: L214-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#observedList?.removeEventListener()`, `this.#resizeObserver?.disconnect()`
- 条件付き依存: `if (this.#scrollAnimationId)` → `cancelAnimationFrame()`
- 参照: `this.#handleScroll`, `this.#observedList`, `this.#resizeObserver`, `this.#scrollAnimationId`

## AIActionConfirmation.render()
- 位置: L226-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `ref()`, `this.#renderTab()`, `this.tabs.map()`
- 参照: `this.#handleToggle`, `this.#handleUndo`, `this.#tabsListRef`, `this.canUndo`, `this.isExpanded`, `this.labelL10nArgs`, `this.labelL10nId`, `this.tabs.length`
