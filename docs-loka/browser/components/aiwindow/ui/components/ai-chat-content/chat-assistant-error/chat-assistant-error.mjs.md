# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-error/chat-assistant-error.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-error/chat-assistant-error.mjs
source-hash: 003f7d20a5f05370c566801212515e3eb932e39e
lines: 187

## <module>
- 役割: バックエンドのエラーコードに応じて見出し、本文、ボタンを出す chat-assistant-error 要素を定義する。
- 呼び出し先: `customElements.define()`

## ChatAssistantError.constructor()
- 位置: L37-40
- 役割: エラー表示を既定（汎用エラーと再試行ボタン）で初期化する。
- 触るとき: エラーが無いときに出る既定文言を変えるとき、または初期表示を確認するときに見る。
- 呼び出し先: `super()`, `this.setGenericError()`

## ChatAssistantError.willUpdate()
- 位置: L42-46
- 役割: error プロパティが変わったときに、表示文言とボタンを決め直す。
- 触るとき: エラーを差し替えても古い文言が残るときに見る。
- 呼び出し先: `changed.has()`
- 条件付き依存: `if (changed.has("error"))` → `this.getErrorInformation()`

## ChatAssistantError.openNewChat()
- 位置: L48-54
- 役割: aiChatError:new-chat イベントを発火し、新しい会話を始めてもらう。
- 触るとき: 新規チャットへの導線を変えるとき、または親がこのイベントを受けていないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## ChatAssistantError.openAccountSignIn()
- 位置: L56-62
- 役割: aiChatError:sign-in イベントを発火し、サインインを促す。
- 触るとき: サインイン導線やイベント名を変えるとき、またはサインインボタンが反応しないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## ChatAssistantError.retryAssistantMessage()
- 位置: L64-70
- 役割: aiChatError:retry-message イベントを発火し、直前のメッセージの再送を依頼する。
- 触るとき: 再試行の動作を変えるとき、または再送が走らないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## ChatAssistantError.setGenericError()
- 位置: L72-80
- 役割: 汎用のエラー見出しと再試行ボタンを errorText と actionButton に設定する。
- 触るとき: 既知でないエラーの表示を変えるとき、または汎用文言を差し替えるときに見る。
- 呼び出し先: `this.retryAssistantMessage.bind()`
- 参照: `this.actionButton`, `this.errorText`

## ChatAssistantError.getErrorInformation()
- 位置: L82-150
- 役割: アカウント未認証、エラーコードごとに見出し・本文・ボタンを決める。
- 触るとき: 新しいエラーコードを足すとき、またはエラーコードごとの文言やボタンの対応を直すときに見る。
- 呼び出し先: `this.openNewChat.bind()`, `this.setGenericError()`
- 条件付き依存: `if (this.error.clientReason === "fxaTokenUnavailable")` → `this.openAccountSignIn.bind()`
- 参照: `ERROR_CODES.BUDGET_EXCEEDED`, `ERROR_CODES.CHAT_MAX_LENGTH`, `ERROR_CODES.FASTLY_BLOCKED`, `ERROR_CODES.FASTLY_WAF_RATE_LIMIT`, `ERROR_CODES.MAX_USERS_REACHED`, `ERROR_CODES.RATE_LIMIT_EXCEEDED`, `ERROR_CODES.UPSTREAM_RATE_LIMIT`, `this.actionButton`, `this.error`, `this.error.clientReason`, `this.error.error`, `this.error.httpStatus`, `this.errorText`

## ChatAssistantError.render()
- 位置: L152-183
- 役割: 見出し、任意の本文、任意のボタンを errorText と actionButton から描画する。
- 触るとき: エラー表示の DOM 構造や l10n 属性を変えるとき、または本文やボタンが出ないときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.actionButton`, `this.actionButton?.action`, `this.actionButton?.label`, `this.errorText.args`, `this.errorText?.args`, `this.errorText?.body`, `this.errorText?.header`
