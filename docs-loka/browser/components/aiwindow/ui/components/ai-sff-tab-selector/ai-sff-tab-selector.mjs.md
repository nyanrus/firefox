# browser/components/aiwindow/ui/components/ai-sff-tab-selector/ai-sff-tab-selector.mjs

source: browser/components/aiwindow/ui/components/ai-sff-tab-selector/ai-sff-tab-selector.mjs
source-hash: e1b681ddb92693aa0d5f713268b369d3b0ac24f3
lines: 164

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AiSffTabSelector.constructor()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.otherTabs`, `this.suggestedTabs`

## AiSffTabSelector.#selectedTabIds()
- 位置: L29-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...this.suggestedTabs, ...this.otherTabs] .filter()`, `[...this.suggestedTabs, ...this.otherTabs] .filter(tab => tab.pressed) .map()`
- 参照: `tab.id`, `tab.pressed`, `this.otherTabs`, `this.suggestedTabs`

## AiSffTabSelector.#updateTab()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.map()`
- 参照: `tab.id`

## AiSffTabSelector.#handleTabToggle()
- 位置: L39-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateTab()`
- 参照: `event.currentTarget`, `this.otherTabs`, `this.suggestedTabs`

## AiSffTabSelector.#handleAccept()
- 位置: L46-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `selectedTabIds.length`, `this.#selectedTabIds`

## AiSffTabSelector.#handleCancel()
- 位置: L61-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AiSffTabSelector.#renderTabList()
- 位置: L70-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#handleTabToggle()`
- 参照: `tab.favicon`, `tab.id`, `tab.pressed`, `tab.title`, `tab.url`

## AiSffTabSelector.render()
- 位置: L112-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderTabList()`
- 参照: `this.#handleAccept`, `this.#handleCancel`, `this.#selectedTabIds.length`, `this.otherTabs`, `this.otherTabs?.length`, `this.suggestedTabs`, `this.suggestedTabs?.length`
