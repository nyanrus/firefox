# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-citations/chat-assistant-citations.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-citations/chat-assistant-citations.mjs
source-hash: f4807dbc2283ee77d43c54336a0237b54f2d2ec9
lines: 165

## <module>
- 役割: (未記入)
- 呼び出し先: `SmartwindowOverflowRowMixin()`, `customElements.define()`

## ChatAssistantCitations.constructor()
- 位置: L38-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.citations`, `this.isPanelOpen`

## ChatAssistantCitations.overflowContainerSelector()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)

## ChatAssistantCitations.overflowTriggerSelector()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)

## ChatAssistantCitations.overflowItems()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.citations`

## ChatAssistantCitations.#panel()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`

## ChatAssistantCitations.#onToggleClick()
- 位置: L69-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel()`
- 条件付き依存: `if (panel)` → `panel.toggle()`
- 参照: `event.currentTarget`, `panel.anchor`

## ChatAssistantCitations.#onPanelOpenLink()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel()`, `this.#panel()?.hide()`

## ChatAssistantCitations.#label()
- 位置: L81-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `URL.parse(citation.url)?.hostname`, `citation.title`, `citation.url`

## ChatAssistantCitations.#titleText()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `citation.title`, `citation.url`

## ChatAssistantCitations.#icon()
- 位置: L91-98
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `citation.faviconUrl`, `citation.hasFavicon`, `citation.url`

## ChatAssistantCitations.#renderPill()
- 位置: L100-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#icon()`, `this.#label()`, `this.#titleText()`
- 参照: `citation.url`

## ChatAssistantCitations.render()
- 位置: L113-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Math.min()`, `String()`, `citationsOverflow.map()`, `html()`, `this.#renderPill()`, `this.citations.map()`, `this.citations.slice()`
- 参照: `citationsOverflow.length`, `this.#onPanelOpenLink`, `this.#onToggleClick`, `this.citations.length`, `this.citations?.length`, `this.isPanelOpen`, `this.visibleCount`
