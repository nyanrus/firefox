# browser/components/reportbrokensite/content/components/url-input.mjs

source: browser/components/reportbrokensite/content/components/url-input.mjs
source-hash: cb3751bfe2f567f2a1dc56068897bd114f6ac3a2
lines: 128

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## UrlInputCustomElement.checkValidity()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.checkValidity()`

## UrlInputCustomElement.requestBlur()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.blur()`

## UrlInputCustomElement.#updateUrl()
- 位置: L38-50
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (url?.hostname)` → `url.href.split()`
- 条件付き依存: `if (url?.hostname)` → `post.join()`
- 条件付き依存: `if (url?.hostname)` → `this.emphasizedUrlText.setHTML()`
- 参照: `input.value`, `this.emphasizedUrlText.innerText`, `url.hostname`, `url?.hostname`

## UrlInputCustomElement.#updateFavicon()
- 位置: L52-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.wrapper.classList.toggle()`
- 参照: `this.faviconImg.src`

## UrlInputCustomElement.willUpdate()
- 位置: L58-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changes.has()`
- 条件付き依存: `if (changes.has("url"))` → `this.#updateUrl()`
- 条件付き依存: `if (changes.has("favicon"))` → `this.#updateFavicon()`
- 参照: `this.hasUpdated`

## UrlInputCustomElement.firstUpdated()
- 位置: L70-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.firstUpdated()`, `this.#updateFavicon()`, `this.#updateUrl()`

## UrlInputCustomElement.#fireEvent()
- 位置: L76-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## UrlInputCustomElement.#resetClicked()
- 位置: L82-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fireEvent()`

## UrlInputCustomElement.#inputEdited()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fireEvent()`

## UrlInputCustomElement.#inputChanged()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fireEvent()`
- 参照: `this.input.value`

## UrlInputCustomElement.render()
- 位置: L94-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#inputChanged`, `this.#inputEdited`, `this.#resetClicked`
