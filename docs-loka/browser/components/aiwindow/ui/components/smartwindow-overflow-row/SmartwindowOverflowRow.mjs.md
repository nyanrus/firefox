# browser/components/aiwindow/ui/components/smartwindow-overflow-row/SmartwindowOverflowRow.mjs

source: browser/components/aiwindow/ui/components/smartwindow-overflow-row/SmartwindowOverflowRow.mjs
source-hash: 635e04556769e24c2d247a8cd92cb089256cb135
lines: 209

## <module>
- 役割: (未記入)

## SmartwindowOverflowRowMixin()
- 位置: L11-208
- 役割: (未記入)
- 触るとき: (未記入)

## constructor()
- 位置: L22-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.visibleCount`

## overflowContainerSelector()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)

## overflowItemSelector()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## overflowTriggerSelector()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)

## maxInlineItems()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)

## inlineItemCount()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)

## isWidthAware()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`
- 参照: `this.inlineItemCount`

## overflowItems()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)

## isMeasuring()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#measureRaf`

## connectedCallback()
- 位置: L85-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 条件付き依存: `if (this.hasUpdated)` → `this.syncOverflowMode()`
- 参照: `this.hasUpdated`

## disconnectedCallback()
- 位置: L92-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#stopMeasuring()`

## updated()
- 位置: L97-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updated()`, `this.syncOverflowMode()`

## syncOverflowMode()
- 位置: L105-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#setVisibleCount()`, `this.#stopMeasuring()`
- 条件付き依存: `if (this.isWidthAware)` → `this.#observeWidth()`
- 条件付き依存: `if (this.isWidthAware)` → `this.scheduleOverflowMeasure()`
- 参照: `this.inlineItemCount`, `this.isWidthAware`

## scheduleOverflowMeasure()
- 位置: L116-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `this.#measureOverflow()`
- 参照: `this.#measureRaf`, `this.isWidthAware`

## #observeWidth()
- 位置: L126-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resizeObserver.observe()`, `this.scheduleOverflowMeasure()`
- 参照: `entries[0]?.contentBoxSize`, `entries[0]?.contentBoxSize?.[0]?.inlineSize`, `this.#lastWidth`, `this.#resizeObserver`, `this.#widthChanged`

## #stopMeasuring()
- 位置: L139-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cancelAnimationFrame()`, `this.#resizeObserver?.disconnect()`
- 参照: `this.#lastWidth`, `this.#measureRaf`, `this.#resizeObserver`

## #setVisibleCount()
- 位置: L147-151
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.visibleCount`

## #measureOverflow()
- 位置: L153-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `child.getBoundingClientRect()`, `container.querySelector()`, `container.querySelectorAll()`, `cumulativeItemWidths.at()`, `cumulativeItemWidths.push()`, `getComputedStyle()`, `parseFloat()`, `this.#setVisibleCount()`, `this.renderRoot?.querySelector()`, `trigger?.getBoundingClientRect()`
- 条件付き依存: `if ( children.length <= this.maxInlineItems && cumulativeItemWidths.at(-1) - columnGap <= container.clientWidth )` → `this.#setVisibleCount()`
- 参照: `child.getBoundingClientRect().width`, `children.length`, `container.clientWidth`, `getComputedStyle(container).columnGap`, `items.length`, `this.#widthChanged`, `this.maxInlineItems`, `this.overflowContainerSelector`, `this.overflowItemSelector`, `this.overflowItems`, `this.overflowTriggerSelector`, `this.visibleCount`, `trigger?.getBoundingClientRect().width`
