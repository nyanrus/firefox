# browser/components/aboutlogins/content/components/login-filter.mjs

source: browser/components/aboutlogins/content/components/login-filter.mjs
source-hash: 157dbe1d65062867b6809f68891c792e60fc9799
lines: 100

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## LoginFilter.#loginList()
- 位置: L8-10
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`

## LoginFilter.connectedCallback()
- 位置: L12-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginFilterTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `this._input.addEventListener()`, `this.addEventListener()`, `this.attachShadow()`, `this.shadowRoot.querySelector()`, `window.addEventListener()`
- 参照: `this._input`, `this.shadowRoot`

## LoginFilter.focus()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._input.focus()`

## LoginFilter.handleEvent()
- 位置: L33-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#filterLogins()`, `this.#input()`, `this.#keyDown()`
- 参照: `event.detail`, `event.originalTarget.value`, `event.type`

## LoginFilter.#filterLogins()
- 位置: L47-51
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.value`

## LoginFilter.#input()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dispatchFilterEvent()`

## LoginFilter.#keyDown()
- 位置: L57-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `this.#loginList.clickSelected()`, `this.#loginList.selectNext()`, `this.#loginList.selectPrevious()`
- 参照: `e.code`, `this.value`

## LoginFilter.value()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._input.value`

## LoginFilter.value()
- 位置: L82-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dispatchFilterEvent()`
- 参照: `this._input.value`

## LoginFilter._dispatchFilterEvent()
- 位置: L87-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `recordTelemetryEvent()`, `this.dispatchEvent()`
