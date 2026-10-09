# browser/components/aiwindow/ui/components/smartwindow-prompts/smartwindow-prompts.mjs

source: browser/components/aiwindow/ui/components/smartwindow-prompts/smartwindow-prompts.mjs
source-hash: ce519bfa4239587390a858935ae4fb212b4b1777
lines: 330

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartWindowPrompts.constructor()
- 位置: L35-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.canScrollEnd`, `this.canScrollStart`, `this.mode`, `this.prompts`

## SmartWindowPrompts.disconnectedCallback()
- 位置: L43-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#resizeObserver?.disconnect()`
- 参照: `this.#observedContainer`, `this.#resizeObserver`

## SmartWindowPrompts.updated()
- 位置: L50-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (container && container !== this.#observedContainer)` → `this.#resizeObserver?.disconnect()`
- 条件付き依存: `if (container && container !== this.#observedContainer)` → `this.#updateScrollState()`
- 条件付き依存: `if (container && container !== this.#observedContainer)` → `this.#resizeObserver.observe()`
- 条件付き依存: `if (changedProperties.has("prompts") || changedProperties.has("mode"))` → `this.#updateScrollState()`
- 参照: `this.#observedContainer`, `this.#resizeObserver`, `this.#scrollContainer`

## SmartWindowPrompts.#scrollContainer()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## SmartWindowPrompts.#updateScrollState()
- 位置: L76-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 参照: `container.clientWidth`, `container.scrollLeft`, `container.scrollWidth`, `this.#scrollContainer`, `this.canScrollEnd`, `this.canScrollStart`, `this.mode`

## SmartWindowPrompts.#scrollToAdjacentPill()
- 位置: L103-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Math.max()`, `Math.min()`, `container.getBoundingClientRect()`, `isAtOrPastStart()`, `pill.getBoundingClientRect()`, `pills.findIndex()`, `pills[targetIndex].scrollIntoView()`, `this.matches()`
- 参照: `container.children`, `containerRect.left`, `containerRect.right`, `pills.length`, `this.#scrollContainer`

## isAtOrPastStart()
- 位置: L116-117
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `rect.left`, `rect.right`

## SmartWindowPrompts.#promptSelected()
- 位置: L132-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `swPrompt.content`, `swPrompt.memory`

## SmartWindowPrompts.#hasInteracted()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.currentTarget.classList.add()`

## SmartWindowPrompts.#promptDismissed()
- 位置: L156-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.stopPropagation()`, `this.dispatchEvent()`
- 参照: `swPrompt.memory`

## SmartWindowPrompts.#renderFavicons()
- 位置: L174-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `previewIcons.slice()`, `visibleIcons.map()`
- 参照: `e.target.src`, `icon.iconSrc`, `previewIcons.length`, `previewIcons?.length`, `visibleIcons.length`

## SmartWindowPrompts.#renderSkeletonPrompt()
- 位置: L213-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## SmartWindowPrompts.#renderScrollButtons()
- 位置: L222-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#scrollToAdjacentPill()`
- 参照: `this.canScrollEnd`, `this.canScrollStart`, `this.mode`

## SmartWindowPrompts.#renderPrompt()
- 位置: L260-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#promptDismissed()`, `this.#promptSelected()`, `this.#renderFavicons()`
- 参照: `swPrompt.previewIcons`, `swPrompt.text`, `swPrompt.type`, `this.#hasInteracted`, `this.mode`

## SmartWindowPrompts.render()
- 位置: L296-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `this.#renderPrompt()`, `this.#renderScrollButtons()`, `this.#renderSkeletonPrompt()`, `this.#updateScrollState()`, `this.prompts.map()`
- 条件付き依存: `if (!this.prompts.length)` → `html()`
- 参照: `swPrompt.type`, `this.canScrollEnd`, `this.canScrollStart`, `this.prompts.length`
