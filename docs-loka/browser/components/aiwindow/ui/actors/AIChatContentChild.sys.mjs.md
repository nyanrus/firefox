# browser/components/aiwindow/ui/actors/AIChatContentChild.sys.mjs

source: browser/components/aiwindow/ui/actors/AIChatContentChild.sys.mjs
source-hash: 0f2ae3565a128cb7c728df1a37059d1c185012e0
lines: 147

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## AIChatContentChild.handleEvent()
- 位置: L65-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIChatContentChild.#VALID_EVENTS_FROM_CONTENT.has()`, `copyActions.includes()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!AIChatContentChild.#VALID_EVENTS_FROM_CONTENT.has(event.type))` → `console.warn()`
- 条件付き依存: `if (isCopyAction)` → `lazy.ClipboardHelper.copyString()`
- 参照: `event.detail`, `event.type`, `this.windowContext`

## AIChatContentChild.receiveMessage()
- 位置: async L92-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchToChatContent()`
- 条件付き依存: `if (!mapping)` → `console.warn()`
- 参照: `AIChatContentChild.#EVENT_MAPPINGS_FROM_PARENT`, `mapping.event`, `message.data`, `message.name`

## AIChatContentChild.#dispatchToChatContent()
- 位置: L107-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `chatContent.dispatchEvent()`, `console.error()`, `this.#reportDispatchFailure()`, `this.document.querySelector()`
- 条件付き依存: `if (!chatContent)` → `console.error()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`

## AIChatContentChild.#reportDispatchFailure()
- 位置: L132-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `serializeClientErrorDetail()`, `this.sendAsyncMessage()`
