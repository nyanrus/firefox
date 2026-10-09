# browser/components/sidebar/sidebar-panel-switcher.mjs

source: browser/components/sidebar/sidebar-panel-switcher.mjs
source-hash: ff46c2cb9d627314744dd9f851800aa791ae2c6d
lines: 129

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SidebarPanelSwitcher.constructor()
- 位置: L34-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.items`, `this.label`, `this.open`

## SidebarPanelSwitcher.#controller()
- 位置: L41-44
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext.embedderWindowGlobal.browsingContext.window .SidebarController`

## SidebarPanelSwitcher.#currentView()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller.currentID`, `this.view`

## SidebarPanelSwitcher.connectedCallback()
- 位置: L50-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#updateLabel()`, `window.addEventListener()`

## SidebarPanelSwitcher.disconnectedCallback()
- 位置: L58-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `window.removeEventListener()`

## SidebarPanelSwitcher.handleEvent()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateLabel()`

## SidebarPanelSwitcher.willUpdate()
- 位置: L67-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("view"))` → `this.#updateLabel()`

## SidebarPanelSwitcher.#updateLabel()
- 位置: async L73-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.find()`, `this.#controller.getRevampSwitcherItems()`
- 参照: `item.view`, `items.find(item => item.view === this.#currentView)?.label`, `this.#currentView`, `this.label`

## SidebarPanelSwitcher.#onButtonClick()
- 位置: async L79-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.getRevampSwitcherItems()`, `this.panelList.toggle()`
- 参照: `this.items`, `this.updateComplete`

## SidebarPanelSwitcher.#onItemClick()
- 位置: L87-91
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (view !== this.#currentView)` → `this.#controller.show()`
- 参照: `this.#currentView`

## SidebarPanelSwitcher.render()
- 位置: L93-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#onItemClick()`, `this.items.map()`
- 参照: `item.label`, `item.view`, `this.#currentView`, `this.#onButtonClick`, `this.label`, `this.open`
