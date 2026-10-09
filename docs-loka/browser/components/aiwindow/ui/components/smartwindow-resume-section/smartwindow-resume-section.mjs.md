# browser/components/aiwindow/ui/components/smartwindow-resume-section/smartwindow-resume-section.mjs

source: browser/components/aiwindow/ui/components/smartwindow-resume-section/smartwindow-resume-section.mjs
source-hash: ac733577185256b53427953c01d99b3a586f1e17
lines: 211

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartwindowResumeSection.constructor()
- 位置: L36-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.cards`, `this.emptyReason`, `this.expanded`, `this.loading`

## SmartwindowResumeSection.#dispatch()
- 位置: L44-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowResumeSection.#onToggleClick()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.expanded`

## SmartwindowResumeSection.#onHideClick()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 参照: `this.emptyReason`

## SmartwindowResumeSection.#renderEmptyState()
- 位置: L62-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `RESUME_SECTION_EMPTY_REASON.ALL_DISMISSED`, `this.#onHideClick`, `this.emptyReason`

## SmartwindowResumeSection.#renderSkeletonCard()
- 位置: L100-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## SmartwindowResumeSection.#renderLoadingState()
- 位置: L134-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `html()`, `this.#renderSkeletonCard()`

## SmartwindowResumeSection.render()
- 位置: L154-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Math.max()`, `html()`, `this.cards.slice()`, `visibleCards.map()`
- 条件付き依存: `if (this.loading)` → `this.#renderLoadingState()`
- 条件付き依存: `if (!this.cards.length)` → `this.#renderEmptyState()`
- 参照: `memory.id`, `this.#onToggleClick`, `this.cards`, `this.cards.length`, `this.emptyReason`, `this.expanded`, `this.loading`
