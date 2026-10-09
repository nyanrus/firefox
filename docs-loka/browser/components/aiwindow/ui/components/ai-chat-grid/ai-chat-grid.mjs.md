# browser/components/aiwindow/ui/components/ai-chat-grid/ai-chat-grid.mjs

source: browser/components/aiwindow/ui/components/ai-chat-grid/ai-chat-grid.mjs
source-hash: b5ab5d92bf937972b0e6213d5bad1e040fa9f738
lines: 126

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIChatGrid.showGrid()
- 位置: L21-23
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view`

## AIChatGrid.showList()
- 位置: L25-27
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view`

## AIChatGrid.switchView()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.target.id`, `this.view`

## AIChatGrid.renderGridControls()
- 位置: L33-66
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.showSwitch)` → `html()`
- 参照: `this.showGrid`, `this.showList`, `this.showSwitch`, `this.switchView`

## AIChatGrid.renderItems()
- 位置: L68-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.map()`, `this.renderItem()`
- 参照: `this.gridItem`, `this.items`, `this.rowItem`, `this.view`

## AIChatGrid.renderItem()
- 位置: L83-89
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof itemComponent === "function")` → `itemComponent()`

## AIChatGrid.gridStyle()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view`

## AIChatGrid.renderLoading()
- 位置: L95-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## AIChatGrid.renderGrid()
- 位置: L105-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.gridStyle()`, `this.renderGridControls()`, `this.renderItems()`
- 参照: `this.view`

## AIChatGrid.render()
- 位置: L114-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.renderGrid()`, `this.renderLoading()`
- 参照: `this.loading`
