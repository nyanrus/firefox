# browser/components/aiwindow/ui/components/ai-website-chip/ai-website-chip.mjs

source: browser/components/aiwindow/ui/components/ai-website-chip/ai-website-chip.mjs
source-hash: 8f22c7ca2bee1de7aa1a6955c019906b3a467fbe
lines: 233

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIWebsiteChip.constructor()
- 位置: L59-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.href`, `this.iconSrc`, `this.isTabGroup`, `this.itemRole`, `this.label`, `this.openLinkEvent`, `this.removable`, `this.size`, `this.tabGroupColor`, `this.type`

## AIWebsiteChip.connectedCallback()
- 位置: L73-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.getRootNode()`
- 参照: `this.#parentHost`, `this.getRootNode()?.host`

## AIWebsiteChip.disconnectedCallback()
- 位置: L78-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.#parentHost?.isConnected)` → `this.#parentHost.dispatchEvent()`
- 参照: `this.#parentHost`, `this.#parentHost?.isConnected`, `this.label`, `this.type`

## AIWebsiteChip.#isEmpty()
- 位置: L97-99
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.label`, `this.type`

## AIWebsiteChip.#isRemovable()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.removable`

## AIWebsiteChip.#handleClick()
- 位置: L105-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.label`

## AIWebsiteChip.#handleRemove()
- 位置: L115-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `e.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.label`

## AIWebsiteChip.#handleAnchorClick()
- 位置: L127-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `this.dispatchEvent()`
- 参照: `e.altKey`, `e.button`, `e.ctrlKey`, `e.metaKey`, `e.shiftKey`, `this.href`, `this.openLinkEvent`

## AIWebsiteChip.render()
- 位置: L152-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 条件付き依存: `if (isEmpty)` → `html()`
- 条件付き依存: `if (this.isTabGroup)` → `html()`
- 条件付き依存: `if (!(this.isTabGroup))` → `html()`
- 参照: `e.target.src`, `this.#handleAnchorClick`, `this.#handleClick`, `this.#handleRemove`, `this.#isEmpty`, `this.#isRemovable`, `this.href`, `this.iconSrc`, `this.isTabGroup`, `this.itemRole`, `this.label`, `this.tabGroupColor`
