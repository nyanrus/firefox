# browser/components/aiwindow/ui/modules/AIWindowMenu.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowMenu.sys.mjs
source-hash: db92c5821874e1786ad56d663680a0088c3a306c
lines: 127

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AIWindowMenu.constructor()
- 位置: L19-19
- 役割: (未記入)
- 触るとき: (未記入)

## AIWindowMenu.addMenuitems()
- 位置: async L27-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addChatsMenuitem()`, `this.#addRecentChats()`
- 参照: `event.target`

## AIWindowMenu.#addChatsMenuitem()
- 位置: L32-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.isAIWindowActiveAndEnabled()`, `this.#addChatsMenuitemToHistory()`, `this.#removeChatsMenuitem()`

## AIWindowMenu.#removeChatsMenuitem()
- 位置: L42-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.querySelector()`
- 参照: `chatsMenuitem.hidden`

## AIWindowMenu.#addChatsMenuitemToHistory()
- 位置: L47-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.querySelector()`
- 参照: `chatsMenuitem.hidden`

## AIWindowMenu.#addRecentChats()
- 位置: async L52-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.chatStore.findRecentConversations()`, `AIWindow.isAIWindowActiveAndEnabled()`, `this.#addRecentChatMenuitems()`, `this.#addRecentChatsMenuitemHeader()`, `this.#removeChatsMenuitems()`
- 参照: `items.length`

## AIWindowMenu.#removeChatsMenuitems()
- 位置: L70-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.querySelector()`, `next.hasAttribute()`, `toRemove.remove()`
- 参照: `next.hasAttribute`, `next.nextSibling`, `separator.hidden`, `startingElement.hidden`, `startingElement?.nextElementSibling`

## AIWindowMenu.#addRecentChatsMenuitemHeader()
- 位置: L86-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu.querySelector()`
- 参照: `chatsHeader.hidden`, `separator.hidden`

## AIWindowMenu.#addRecentChatMenuitems()
- 位置: L94-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chatsHeader.insertAdjacentElement()`, `document.createXULElement()`, `document.getElementById()`, `items.pop()`, `menuItem.addEventListener()`, `menuItem.classList.add()`, `menuItem.setAttribute()`
- 参照: `item.id`, `item.title`, `items.length`, `this.#onRecentChatMenuitemClick`, `win.document`

## AIWindowMenu.#onRecentChatMenuitemClick()
- 位置: async L110-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.chatStore.findConversationById()`, `AIWindowUI.reopenConversationInTab()`, `event.target.getAttribute()`, `lazy.BrowserUtils.whereToOpenLink()`
- 参照: `event.target.documentGlobal`
