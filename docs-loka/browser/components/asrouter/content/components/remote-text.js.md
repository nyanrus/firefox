# browser/components/asrouter/content/components/remote-text.js

source: browser/components/asrouter/content/components/remote-text.js
source-hash: 970b7c37f9a93ef4a443c85b8f2b2ad605b67544
lines: 90

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## MozRemoteText.constructor()
- 位置: L14-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `super()`
- 参照: `this._content`, `this._translated`

## MozRemoteText.fluentAttributeValues()
- 位置: L21-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `name.startsWith()`, `this.getAttributeNames()`
- 条件付き依存: `if (name.startsWith("fluent-variable-"))` → `this.getAttribute()`
- 条件付き依存: `if (name.startsWith("fluent-variable-"))` → `value.match()`
- 条件付き依存: `if (value.match(/^\d+/))` → `parseInt()`
- 条件付き依存: `if (name.startsWith("fluent-variable-"))` → `name.replace()`

## MozRemoteText.render()
- 位置: L39-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `RemoteL10n.l10n.setAttributes()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `this._translated .then(() => RemoteL10n.l10n.translateFragment(this._content)) .catch()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `this._translated .then()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `RemoteL10n.l10n.translateFragment()`
- 参照: `console.error`, `this._content`, `this._translated`, `this.fluentAttributeValues`

## MozRemoteText.setVariable()
- 位置: L60-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.render()`, `this.setAttribute()`

## MozRemoteText.observedAttributes()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)

## MozRemoteText.attributeChangedCallback()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.render()`

## MozRemoteText.connectedCallback()
- 位置: L73-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `shadowRoot.appendChild()`, `this.attachShadow()`, `this.render()`
- 参照: `this._content`, `this.shadowRoot`
