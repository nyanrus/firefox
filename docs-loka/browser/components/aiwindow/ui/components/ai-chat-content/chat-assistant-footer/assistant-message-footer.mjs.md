# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/assistant-message-footer.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/assistant-message-footer.mjs
source-hash: c0f88ef6eba1ae7478e75bfd1756af9f61f87db4
lines: 174

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AssistantMessageFooter.constructor()
- 位置: L54-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.appliedMemories`, `this.hideRetry`, `this.messageId`, `this.showCallout`

## AssistantMessageFooter.events()
- 位置: L67-74
- 役割: (未記入)
- 触るとき: (未記入)

## AssistantMessageFooter.#emit()
- 位置: L76-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.constructor.eventBehaviors`

## AssistantMessageFooter.#emitCopy()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.copy`, `this.messageId`

## AssistantMessageFooter.#emitRetry()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.retry`, `this.messageId`

## AssistantMessageFooter.#emitThumbsUp()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.thumbsUp`, `this.messageId`

## AssistantMessageFooter.#emitThumbsDown()
- 位置: L97-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.thumbsDown`, `this.messageId`

## AssistantMessageFooter.render()
- 位置: L103-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#emitCopy()`, `this.#emitRetry()`, `this.#emitThumbsDown()`, `this.#emitThumbsUp()`
- 参照: `this.appliedMemories`, `this.hideRetry`, `this.messageId`, `this.showCallout`
