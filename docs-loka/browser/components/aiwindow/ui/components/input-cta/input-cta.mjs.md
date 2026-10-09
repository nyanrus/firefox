# browser/components/aiwindow/ui/components/input-cta/input-cta.mjs

source: browser/components/aiwindow/ui/components/input-cta/input-cta.mjs
source-hash: acb20e58b6a092cd70d83717e0ffed7660f9a2f3
lines: 273

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## InputCta.constructor()
- 位置: L54-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.randomUUID()`, `super()`
- 参照: `this._menuId`, `this._searchSubpanelId`, `this.action`, `this.searchEngineInfo`, `this.searchEngines`, `this.submitDisabled`

## InputCta.actionLabelId()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.action`

## InputCta.buttonIconSrc()
- 位置: L68-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.action`

## InputCta.searchIconUrl()
- 位置: L75-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.searchEngineInfo.icon`, `this.searchEngineInfo?.icon`

## InputCta.#mainPanel()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.getElementById()`
- 参照: `this._menuId`

## InputCta.#searchSubpanel()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.getElementById()`
- 参照: `this._searchSubpanelId`

## InputCta.#mozButton()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot?.querySelector()`

## InputCta.#setAction()
- 位置: L93-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InputCta.ACTIONS.includes()`, `this.dispatchEvent()`
- 参照: `this.action`

## InputCta.#onAction()
- 位置: L111-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.action`, `this.submitDisabled`

## InputCta.#onSearchEngineSelect()
- 位置: L125-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `engine.name`

## InputCta.#onSearchItemClick()
- 位置: L135-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `requestAnimationFrame()`, `this.#mainPanel?.hide()`, `this.#searchSubpanel?.show()`
- 参照: `this.#mozButton.chevronButtonEl`

## InputCta.#onBackClick()
- 位置: L143-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `requestAnimationFrame()`, `this.#mainPanel?.show()`, `this.#searchSubpanel?.hide()`
- 参照: `this.#mozButton.chevronButtonEl`

## InputCta.willUpdate()
- 位置: L151-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InputCta.ACTIONS.includes()`, `changedProps.has()`
- 条件付き依存: `if ( changedProps.has("action") && this.action && !InputCta.ACTIONS.includes(this.action) )` → `console.warn()`
- 条件付き依存: `if (this.searchIconUrl)` → `this.style.setProperty()`
- 条件付き依存: `if (!(this.searchIconUrl))` → `this.style.removeProperty()`
- 参照: `this.action`, `this.searchIconUrl`

## InputCta.updated()
- 位置: async L172-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProps.has()`
- 条件付き依存: `if (this.submitDisabled && this.action != "stop")` → `mainButton.setAttribute()`
- 条件付き依存: `if (!(this.submitDisabled && this.action != "stop"))` → `mainButton.removeAttribute()`
- 参照: `this.#mozButton?.buttonEl`, `this.#mozButton?.updateComplete`, `this.action`, `this.submitDisabled`

## InputCta.render()
- 位置: L191-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InputCta.ACTIONS.filter()`, `JSON.stringify()`, `html()`, `repeat()`, `styleMap()`, `this.#onBackClick()`, `this.#onSearchEngineSelect()`, `this.#onSearchItemClick()`, `this.#setAction()`
- 参照: `engine.icon`, `engine.name`, `this.#onAction`, `this._menuId`, `this._searchSubpanelId`, `this.action`, `this.actionLabelId`, `this.buttonIconSrc`, `this.searchEngineInfo.name`, `this.searchEngines`
