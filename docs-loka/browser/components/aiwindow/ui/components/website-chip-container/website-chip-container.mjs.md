# browser/components/aiwindow/ui/components/website-chip-container/website-chip-container.mjs

source: browser/components/aiwindow/ui/components/website-chip-container/website-chip-container.mjs
source-hash: 39f1b62f6627f625eeb3c9ff99545cef7a04515a
lines: 242

## <module>
- 役割: (未記入)
- 呼び出し先: `SmartwindowOverflowRowMixin()`, `customElements.define()`

## WebsiteChipContainer.constructor()
- 位置: L45-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.autoOverflow`, `this.chipSize`, `this.chipType`, `this.isPanelOpen`, `this.removable`, `this.shouldGroupChips`, `this.visibleChipCount`, `this.websites`

## WebsiteChipContainer.overflowContainerSelector()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)

## WebsiteChipContainer.inlineItemCount()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.visibleChipCount`

## WebsiteChipContainer.overflowItems()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isAutoOverflowing`, `this.websites`

## WebsiteChipContainer.#isGrouped()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.shouldGroupChips`, `this.websites.length`

## WebsiteChipContainer.#isAutoOverflowing()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isGrouped`, `this.autoOverflow`

## WebsiteChipContainer.#panel()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## WebsiteChipContainer.#onToggleClick()
- 位置: L82-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel()`
- 条件付き依存: `if (panel)` → `panel.toggle()`
- 参照: `event.currentTarget`, `panel.anchor`

## WebsiteChipContainer.#onOverflowItemSelected()
- 位置: L90-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel()`, `this.#panel()?.hide()`, `this.dispatchEvent()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `event.detail`

## WebsiteChipContainer.#onRemoveWebsite()
- 位置: L106-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `website.groupId`, `website.label`, `website.url`

## WebsiteChipContainer.#renderStackedChips()
- 位置: L121-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#onRemoveWebsite()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `this.chipSize`, `this.chipType`, `this.removable`, `website.color`, `website.iconSrc`, `website.label`, `website.type`, `website.url`

## WebsiteChipContainer.#renderGroupedChips()
- 位置: L135-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## WebsiteChipContainer.#renderChip()
- 位置: L141-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderStackedChips()`
- 参照: `website.historyDeleted`

## WebsiteChipContainer.#renderSmartwindowOverflowRow()
- 位置: L154-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Math.min()`, `String()`, `getTabGroupMentionId()`, `html()`, `overflow.map()`, `repeat()`, `this.#renderChip()`, `this.websites.slice()`
- 参照: `overflow.length`, `this.#onOverflowItemSelected`, `this.#onToggleClick`, `this.isPanelOpen`, `this.visibleCount`, `this.websites`, `this.websites.length`, `website.color`, `website.groupId`, `website.iconSrc`, `website.label`, `website.type`, `website.url`

## WebsiteChipContainer.#renderScrollerRow()
- 位置: L202-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `repeat()`, `this.#renderChip()`
- 参照: `this.websites`

## WebsiteChipContainer.#renderChips()
- 位置: L213-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderScrollerRow()`, `this.#renderSmartwindowOverflowRow()`
- 条件付き依存: `if (this.#isGrouped)` → `this.#renderGroupedChips()`
- 参照: `this.#isAutoOverflowing`, `this.#isGrouped`, `this.websites`

## WebsiteChipContainer.render()
- 位置: L222-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderChips()`
- 参照: `this.websites.length`
