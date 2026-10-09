# browser/components/aiwindow/ui/components/smartwindow-history-menu/smartwindow-history-menu.mjs

source: browser/components/aiwindow/ui/components/smartwindow-history-menu/smartwindow-history-menu.mjs
source-hash: 366fc55006b85ac59c48180b99fb0c43cc9797cf
lines: 230

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartwindowHistoryMenu.constructor()
- 位置: L40-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.mode`, `this.recentChats`, `this.view`

## SmartwindowHistoryMenu.#dispatch()
- 位置: L47-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowHistoryMenu.#requestRecentChats()
- 位置: L57-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onNewChat()
- 位置: L59-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onViewAllChats()
- 位置: L61-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onOpenSettings()
- 位置: L63-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onOpenChat()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onSidebarMenuShown()
- 位置: L70-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#requestRecentChats()`
- 参照: `this.view`

## SmartwindowHistoryMenu.#onChatHistoryNavClick()
- 位置: L76-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.#requestRecentChats()`
- 参照: `this.view`

## SmartwindowHistoryMenu.#onBackClick()
- 位置: L82-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`
- 参照: `this.view`

## SmartwindowHistoryMenu.#recentChatRowTemplate()
- 位置: L90-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chat.pageUrl.startsWith()`, `html()`, `styleMap()`, `this.#onOpenChat()`
- 参照: `chat.id`, `chat.pageUrl`, `chat.title`

## SmartwindowHistoryMenu.#recentChatsListTemplate()
- 位置: L105-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `styleMap()`, `this.#recentChatRowTemplate()`, `this.recentChats.map()`
- 参照: `this.#onViewAllChats`, `this.recentChats.length`

## SmartwindowHistoryMenu.#mainViewTemplate()
- 位置: L120-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#onChatHistoryNavClick`, `this.#onOpenSettings`

## SmartwindowHistoryMenu.#chatHistoryViewTemplate()
- 位置: L134-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#recentChatsListTemplate()`
- 参照: `this.#onBackClick`

## SmartwindowHistoryMenu.#sidebarTemplate()
- 位置: L155-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#chatHistoryViewTemplate()`, `this.#mainViewTemplate()`
- 参照: `this.#onSidebarMenuShown`, `this.view`

## SmartwindowHistoryMenu.#fullpageTemplate()
- 位置: L177-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#recentChatsListTemplate()`
- 参照: `this.#onNewChat`, `this.#onOpenSettings`, `this.#requestRecentChats`

## SmartwindowHistoryMenu.render()
- 位置: L216-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#fullpageTemplate()`, `this.#sidebarTemplate()`
- 参照: `this.mode`
