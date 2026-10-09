# browser/components/firefoxview/ChatsController.sys.mjs

source: browser/components/firefoxview/ChatsController.sys.mjs
source-hash: 2700572c45ad706d7913aa1bf651849e0f744385
lines: 445

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ChatsController.constructor()
- 位置: L61-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `host.addController()`
- 参照: `lazy.AIWindow.chatStore`, `options?.searchResultsLimit`, `this.cache`, `this.chatStore`, `this.host`, `this.searchQuery`, `this.searchResultsLimit`

## ChatsController.deleteChat()
- 位置: async L75-81
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (convID)` → `this.chatStore.deleteConversationById()`
- 条件付き依存: `if (convID)` → `this.updateCache()`
- 参照: `this.host.triggerNode.closedId`

## ChatsController.onSearchQuery()
- 位置: L90-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateCache()`
- 参照: `e.detail.query`, `this.searchQuery`

## ChatsController.totalChats()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.cache.entries`

## ChatsController.searchResults()
- 位置: L109-114
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.cache.entries`, `this.cache.entries?.length`, `this.cache.entries[0].items`, `this.cache.searchQuery`

## ChatsController.totalVisitsCount()
- 位置: L121-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.totalChats.reduce()`
- 参照: `entry.items.length`

## ChatsController.isChatEmpty()
- 位置: L133-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.totalChats.length`

## ChatsController.updateCache()
- 位置: async L142-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getAllChatsGroupedByDate()`, `this.#getChatsForSearchQuery()`, `this.#normalizeChat()`, `this.host.requestUpdate()`
- 参照: `this.cache`, `this.searchQuery`

## ChatsController.#normalizeChat()
- 位置: L170-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`
- 条件付き依存: `if (pageUrl)` → `JSON.stringify()`
- 参照: `chat.closedId`, `chat.convId`, `chat.icon`, `chat.pageUrl`, `chat.primaryL10nArgs`, `chat.primaryL10nId`, `chat.secondaryL10nArgs`, `chat.secondaryL10nId`, `chat.time`, `chat.title`, `chat.updatedDate`, `chat.url`, `chat.urls`, `chat.urls.length`, `lazy.AIWindow.newTabURL`, `mostRecentPage?.href`

## ChatsController.#getChatsForSearchQuery()
- 位置: async L204-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversations.forEach()`, `getLogger()`, `getLogger("ChatsController").error()`, `this.chatStore.search()`
- 参照: `conv.convId`, `conv.id`, `conv.pageMeta?.urls`, `conv.urls`, `e.message`, `e.stack`

## ChatsController.#getAllChatsGroupedByDate()
- 位置: async L230-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fetchChats()`, `this.#getChatsForDate()`, `this.#setTodaysDate()`
- 参照: `chats.length`

## ChatsController.#getChatsForDate()
- 位置: L246-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chatsByDay.forEach()`, `chatsByMonth.forEach()`, `entries.push()`, `this.#getChatsByDay()`, `this.#getChatsByMonth()`, `this.#getChatsFromToday()`, `this.#getChatsFromYesterday()`
- 条件付き依存: `if (chatsFromToday.length)` → `entries.push()`
- 条件付き依存: `if (chatsFromYesterday.length)` → `entries.push()`
- 参照: `chatsFromToday.length`, `chatsFromYesterday.length`

## ChatsController.#getChatsFromToday()
- 位置: L290-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chats.filter()`, `this.#todaysDate.getTime()`
- 参照: `chat.updatedDate`

## ChatsController.#getChatsFromYesterday()
- 位置: L304-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chats.filter()`, `this.#todaysDate.getTime()`, `this.#yesterdaysDate.getTime()`
- 参照: `chat.updatedDate`

## ChatsController.#getChatsByDay()
- 位置: L320-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chatDate.getDate()`, `chatDate.getFullYear()`, `chatDate.getMonth()`, `this.#isSameMonth()`, `this.#yesterdaysDate.getTime()`
- 条件付き依存: `if (currentDayChats.length)` → `chatsPerDay.push()`
- 条件付き依存: `if (!(dayKey !== currentDay))` → `currentDayChats.push()`
- 参照: `chat.updatedDate`, `currentDayChats.length`, `this.#todaysDate`

## ChatsController.#getChatsByMonth()
- 位置: L362-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chatDate.getFullYear()`, `chatDate.getMonth()`, `this.#isSameMonth()`, `this.#yesterdaysDate.getTime()`
- 条件付き依存: `if (currentMonthChats.length)` → `chatsPerMonth.push()`
- 条件付き依存: `if (!(monthKey !== currentMonth))` → `currentMonthChats.push()`
- 参照: `chat.updatedDate`, `currentMonthChats.length`, `this.#todaysDate`

## ChatsController.#isSameMonth()
- 位置: L404-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dateToCheck.getFullYear()`, `dateToCheck.getMonth()`, `month.getFullYear()`, `month.getMonth()`

## ChatsController.#setTodaysDate()
- 位置: L414-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `now.getDate()`, `now.getFullYear()`, `now.getMonth()`
- 参照: `this.#todaysDate`, `this.#yesterdaysDate`

## ChatsController.#fetchChats()
- 位置: async L433-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLogger()`, `getLogger("ChatsController").error()`, `this.chatStore.chatHistoryView()`
