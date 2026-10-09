# browser/components/aiwindow/ui/components/ai-grouped-chip-container/ai-grouped-chip-container.mjs

source: browser/components/aiwindow/ui/components/ai-grouped-chip-container/ai-grouped-chip-container.mjs
source-hash: 8517b9e1506f92a43d2f8e815a95dee3a8fb9d1a
lines: 139

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIGroupedChipContainer.constructor()
- 位置: L25-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.chips`, `this.isPanelOpen`, `this.openLinkEvent`

## AIGroupedChipContainer.#onTriggerMousedown()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`

## AIGroupedChipContainer.#toggleGroupedPanel()
- 位置: L39-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.toggle()`, `this.shadowRoot.querySelector()`
- 参照: `event.currentTarget`, `panel.anchor`

## AIGroupedChipContainer.#closeGroupedPanel()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector("smartwindow-panel-list")?.hide()`

## AIGroupedChipContainer.#onItemSelected()
- 位置: L49-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeGroupedPanel()`
- 条件付き依存: `if (url)` → `this.dispatchEvent()`
- 参照: `event.detail?.id`, `this.openLinkEvent`

## AIGroupedChipContainer.#renderStackedIcon()
- 位置: L64-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (chip.type == CONTEXT_MENTION_TYPE.TAB_GROUP)` → `html()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `chip.color`, `chip.iconSrc`, `chip.label`, `chip.type`, `e.target.src`

## AIGroupedChipContainer.render()
- 位置: L83-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#onItemSelected()`, `this.#onTriggerMousedown()`, `this.#renderStackedIcon()`, `this.#toggleGroupedPanel()`, `this.chips.map()`
- 参照: `chip.groupId`, `chip.url`, `this.chips`, `this.chips.length`, `this.isPanelOpen`, `w.color`, `w.iconSrc`, `w.label`, `w.type`, `w.url`
