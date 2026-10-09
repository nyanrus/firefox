# browser/components/genai/content/chatbot-promo.mjs

source: browser/components/genai/content/chatbot-promo.mjs
source-hash: 62dd01ba515020c05a4be7ded7ec32662b4b25ff
lines: 135

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.freeze()`, `customElements.define()`

## ChatbotPromo.#onVisibilityChange()
- 位置: L38-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeFireImpression()`

## ChatbotPromo.constructor()
- 位置: L40-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.message`

## ChatbotPromo.updated()
- 位置: L45-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `this.#maybeFireImpression()`
- 条件付き依存: `if ( changedProperties.has("message") && this.message && !this.#impressionFired && !this.#maybeFireImpression() )` → `this.ownerDocument.addEventListener()`
- 参照: `this.#impressionFired`, `this.#onVisibilityChange`, `this.message`

## ChatbotPromo.disconnectedCallback()
- 位置: L61-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.ownerDocument.removeEventListener()`
- 参照: `this.#onVisibilityChange`

## ChatbotPromo.#maybeFireImpression()
- 位置: L69-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`, `this.ownerDocument.removeEventListener()`
- 参照: `SIDEBAR_CHATBOT_PROMO_EVENTS.IMPRESSION`, `this.#impressionFired`, `this.#onVisibilityChange`, `this.ownerDocument.visibilityState`

## ChatbotPromo.#dispatch()
- 位置: L85-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## ChatbotPromo.#handlePrimary()
- 位置: L91-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 参照: `SIDEBAR_CHATBOT_PROMO_EVENTS.PRIMARY`

## ChatbotPromo.#handleClose()
- 位置: L93-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`
- 参照: `SIDEBAR_CHATBOT_PROMO_EVENTS.CLOSE`

## ChatbotPromo.render()
- 位置: L95-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `content.additionalActionText`, `content.heading`, `content.message`, `content.primaryActionText`, `content.type`, `this.#handleClose`, `this.#handlePrimary`, `this.message`
