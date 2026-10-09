# browser/components/asrouter/content/components/asrouter-newtab-message/asrouter-newtab-message.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/asrouter-newtab-message.mjs
source-hash: a1528ad680b0f8c3e88ad366f9b1d33fc335fb8c
lines: 461

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ASRouterNewTabMessage.connectedCallback()
- 位置: L65-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#startPolling()`, `this.ownerDocument.addEventListener()`
- 参照: `this.#onVisibilityChange`, `this.messageData?.content?.states?.length`

## this.#onVisibilityChange()
- 位置: L71-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#evaluateStates()`

## ASRouterNewTabMessage.disconnectedCallback()
- 位置: L79-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#teardownTriggers()`

## ASRouterNewTabMessage.updated()
- 位置: L92-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("isIntersecting") && this.isIntersecting)` → `this.#evaluateStates()`
- 参照: `this.isIntersecting`

## ASRouterNewTabMessage.#teardownTriggers()
- 位置: L98-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopPolling()`
- 条件付き依存: `if (this.#onVisibilityChange)` → `this.ownerDocument.removeEventListener()`
- 参照: `this.#onVisibilityChange`

## ASRouterNewTabMessage.#startPolling()
- 位置: L109-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `globalThis.setInterval()`, `this.#evaluateStates()`
- 参照: `this.#pollTimer`

## ASRouterNewTabMessage.#stopPolling()
- 位置: L119-124
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#pollTimer)` → `globalThis.clearInterval()`
- 参照: `this.#pollTimer`

## ASRouterNewTabMessage.#evaluateStates()
- 位置: L134-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `states.map()`, `this.dispatchEvent()`
- 参照: `state.targeting`, `states?.length`, `this.#reachedFinalState`, `this.isIntersecting`, `this.messageData?.content?.states`, `this.ownerDocument.visibilityState`

## ASRouterNewTabMessage.setMatchedState()
- 位置: L163-179
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (matched?.final)` → `this.#teardownTriggers()`
- 参照: `matched?.content`, `matched?.final`, `this.#reachedFinalState`, `this._matchedContent`, `this.messageData?.content?.states`

## ASRouterNewTabMessage.#currentContent()
- 位置: L188-193
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._matchedContent`, `this.messageData?.content`

## ASRouterNewTabMessage.specialMessageAction()
- 位置: L210-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NEWTAB_DISPATCH_ACTION_TYPES.has()`, `this.dispatchEvent()`
- 条件付き依存: `if (NEWTAB_DISPATCH_ACTION_TYPES.has(action?.type) && this.dispatch)` → `this.dispatch()`
- 参照: `action?.type`, `this.dispatch`

## ASRouterNewTabMessage.#handleXButton()
- 位置: L229-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleDismiss()`, `this.handleBlock()`

## ASRouterNewTabMessage.#handleDismiss()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleDismiss()`

## ASRouterNewTabMessage.#handlePrimaryButton()
- 位置: L238-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#currentContent()`, `this.handleClick()`
- 条件付き依存: `if (primaryButton?.action?.type)` → `this.specialMessageAction()`
- 条件付き依存: `if (primaryButton?.action?.dismiss)` → `this.#handleDismiss()`
- 参照: `primaryButton.action`, `primaryButton?.action?.dismiss`, `primaryButton?.action?.type`

## ASRouterNewTabMessage.#handleSecondaryButton()
- 位置: L249-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#currentContent()`, `this.handleClick()`
- 条件付き依存: `if (secondaryButton?.action?.type)` → `this.specialMessageAction()`
- 条件付き依存: `if (secondaryButton?.action?.dismiss)` → `this.#handleDismiss()`
- 参照: `secondaryButton.action`, `secondaryButton?.action?.dismiss`, `secondaryButton?.action?.type`

## ASRouterNewTabMessage.#renderHeading()
- 位置: L260-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (typeof value === "string")` → `html()`
- 参照: `value.string_id`

## ASRouterNewTabMessage.#renderBody()
- 位置: L273-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (typeof value === "string")` → `html()`
- 参照: `value.string_id`

## ASRouterNewTabMessage.#renderSecondaryButton()
- 位置: L283-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handleSecondaryButton.bind()`
- 参照: `secondaryButton.label`, `secondaryButton.label.string_id`, `secondaryButton.type`

## ASRouterNewTabMessage.#renderPrimaryButtonContent()
- 位置: L304-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handlePrimaryButton.bind()`
- 条件付き依存: `if (typeof primaryButton.label === "string")` → `html()`
- 条件付き依存: `if (typeof primaryButton.label === "string")` → `this.#handlePrimaryButton.bind()`
- 参照: `primaryButton.iconSrc`, `primaryButton.label`, `primaryButton.label.string_id`, `primaryButton.type`

## ASRouterNewTabMessage.#hasResponsiveImage()
- 位置: L334-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `content?.imageSrcDarkNarrow`, `content?.imageSrcDarkResponsive`, `content?.imageSrcNarrow`, `content?.imageSrcResponsive`

## ASRouterNewTabMessage.#renderImage()
- 位置: L359-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `content?.imageSrc`

## ASRouterNewTabMessage.#renderPrimaryButton()
- 位置: L406-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderPrimaryButtonContent()`, `this.#renderSecondaryButton()`

## ASRouterNewTabMessage.render()
- 位置: L416-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#currentContent()`, `this.#handleXButton.bind()`, `this.#hasResponsiveImage()`, `this.#renderBody()`, `this.#renderHeading()`, `this.#renderImage()`, `this.#renderPrimaryButton()`
- 参照: `content?.body`, `content?.heading`, `content?.hideDismissButton`, `content?.primaryButton`, `content?.secondaryButton`, `this.cssOverride`
