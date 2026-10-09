# browser/components/asrouter/content/components/menu-message/menu-message.mjs

source: browser/components/asrouter/content/components/menu-message/menu-message.mjs
source-hash: 3a7fd6b672c5169b1c7f642c78700c7db5803a17
lines: 244

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## MenuMessage.constructor()
- 位置: L41-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.addEventListener()`
- 条件付き依存: `if (this.shadowRoot.activeElement === this.primaryButton)` → `this.closeButton.focus()`
- 条件付き依存: `if (!(this.shadowRoot.activeElement === this.primaryButton))` → `this.primaryButton.focus()`
- 参照: `event.code`, `this.imagePosition`, `this.layout`, `this.primaryButton`, `this.primaryButtonSize`, `this.shadowRoot.activeElement`

## MenuMessage.handleClose()
- 位置: L71-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`

## MenuMessage.handlePrimaryButton()
- 位置: L80-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## MenuMessage.isRowLayout()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.layout`

## MenuMessage.isSplitLayout()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.layout`

## MenuMessage.renderIllustration()
- 位置: L94-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.documentGlobal.getComputedStyle()`
- 参照: `this.documentGlobal.getComputedStyle(this).direction`, `this.imageURL`, `this.rtlImageURL`

## MenuMessage.renderSplitLayout()
- 位置: L109-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.renderIllustration()`
- 参照: `this.buttonText`, `this.handleClose`, `this.handlePrimaryButton`, `this.primaryButtonSize`, `this.primaryText`, `this.secondaryText`

## MenuMessage.renderRowLayout()
- 位置: L144-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.renderIllustration()`
- 参照: `this.buttonText`, `this.handleClose`, `this.handlePrimaryButton`, `this.logoURL`, `this.primaryButtonSize`, `this.primaryText`, `this.secondaryText`

## MenuMessage.renderColumnLayout()
- 位置: L182-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.renderIllustration()`
- 参照: `this.buttonText`, `this.handleClose`, `this.handlePrimaryButton`, `this.logoURL`, `this.primaryButtonSize`, `this.primaryText`, `this.secondaryText`

## MenuMessage.renderBody()
- 位置: L216-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderColumnLayout()`
- 条件付き依存: `if (this.isSplitLayout)` → `this.renderSplitLayout()`
- 条件付き依存: `if (this.isRowLayout)` → `this.renderRowLayout()`
- 参照: `this.isRowLayout`, `this.isSplitLayout`

## MenuMessage.render()
- 位置: L226-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.renderBody()`
- 参照: `this.imagePosition`, `this.imageURL`, `this.layout`, `this.logoURL`
