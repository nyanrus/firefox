# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-error/chat-assistant-error.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-error/chat-assistant-error.mjs
source-hash: 003f7d20a5f05370c566801212515e3eb932e39e
lines: 187

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ChatAssistantError.constructor()
- 位置: L37-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.setGenericError()`

## ChatAssistantError.willUpdate()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changed.has()`
- 条件付き依存: `if (changed.has("error"))` → `this.getErrorInformation()`

## ChatAssistantError.openNewChat()
- 位置: L48-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## ChatAssistantError.openAccountSignIn()
- 位置: L56-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## ChatAssistantError.retryAssistantMessage()
- 位置: L64-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## ChatAssistantError.setGenericError()
- 位置: L72-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.retryAssistantMessage.bind()`
- 参照: `this.actionButton`, `this.errorText`

## ChatAssistantError.getErrorInformation()
- 位置: L82-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openNewChat.bind()`, `this.setGenericError()`
- 条件付き依存: `if (this.error.clientReason === "fxaTokenUnavailable")` → `this.openAccountSignIn.bind()`
- 参照: `ERROR_CODES.BUDGET_EXCEEDED`, `ERROR_CODES.CHAT_MAX_LENGTH`, `ERROR_CODES.FASTLY_BLOCKED`, `ERROR_CODES.FASTLY_WAF_RATE_LIMIT`, `ERROR_CODES.MAX_USERS_REACHED`, `ERROR_CODES.RATE_LIMIT_EXCEEDED`, `ERROR_CODES.UPSTREAM_RATE_LIMIT`, `this.actionButton`, `this.error`, `this.error.clientReason`, `this.error.error`, `this.error.httpStatus`, `this.errorText`

## ChatAssistantError.render()
- 位置: L152-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.actionButton`, `this.actionButton?.action`, `this.actionButton?.label`, `this.errorText.args`, `this.errorText?.args`, `this.errorText?.body`, `this.errorText?.header`
