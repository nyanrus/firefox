# browser/components/aiwindow/ui/modules/AIWindowMenu.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowMenu.sys.mjs
source-hash: db92c5821874e1786ad56d663680a0088c3a306c
lines: 127

## <module>
- 役割: Smart Window 用のメニュー項目を、アプリメニューの履歴の中に表示・更新する。最近のチャットを最大4件並べる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AIWindowMenu.constructor()
- 位置: L19-19
- 役割: 処理を持たない空のコンストラクター。
- 触るとき: インスタンスごとに初期化すべき状態をこのクラスに持たせるとき、ここに足す。

## AIWindowMenu.addMenuitems()
- 位置: async L27-30
- 役割: 履歴メニューの表示時に、Chats 項目の表示切替と最近のチャット一覧の再構築を順に行う。
- 触るとき: 履歴メニューを開いたときに出る項目の順序や内容を変えるとき。
- 呼び出し先: `this.#addChatsMenuitem()`, `this.#addRecentChats()`
- 参照: `event.target`

## AIWindowMenu.#addChatsMenuitem()
- 位置: L32-40
- 役割: 既存の Chats 項目をいったん隠し、Smart Window が有効なときだけ表示し直す。
- 触るとき: Smart Window の有効・無効によって Chats 項目が出たり消えたりする条件を変えるとき。
- 呼び出し先: `AIWindow.isAIWindowActiveAndEnabled()`, `this.#addChatsMenuitemToHistory()`, `this.#removeChatsMenuitem()`

## AIWindowMenu.#removeChatsMenuitem()
- 位置: L42-45
- 役割: #chatsHistoryMenu を隠す。
- 触るとき: Chats 項目を非表示にする経路を追うとき。
- 呼び出し先: `menu.querySelector()`
- 参照: `chatsMenuitem.hidden`

## AIWindowMenu.#addChatsMenuitemToHistory()
- 位置: L47-50
- 役割: #chatsHistoryMenu を表示する。
- 触るとき: Chats 項目を表示する経路を追うとき。
- 呼び出し先: `menu.querySelector()`
- 参照: `chatsMenuitem.hidden`

## AIWindowMenu.#addRecentChats()
- 位置: async L52-68
- 役割: 既存の最近のチャット項目を消したのち、有効なら会話を最大4件取得して見出しと項目を並べる。0件なら何も出さない。
- 触るとき: 最近のチャットの件数や表示条件を変えるとき、履歴メニューにチャットが出ない原因を調べるとき。
- 呼び出し先: `AIWindow.chatStore.findRecentConversations()`, `AIWindow.isAIWindowActiveAndEnabled()`, `this.#addRecentChatMenuitems()`, `this.#addRecentChatsMenuitemHeader()`, `this.#removeChatsMenuitems()`
- 参照: `items.length`

## AIWindowMenu.#removeChatsMenuitems()
- 位置: L70-84
- 役割: 区切り線と最近のチャットの見出しを隠し、data-conv-id を持つ後続の項目を DOM から取り除く。
- 触るとき: 古い最近のチャット項目が残る不具合を調べるとき、メニュー内の項目の並びを変えるとき。
- 呼び出し先: `menu.querySelector()`, `next.hasAttribute()`, `toRemove.remove()`
- 参照: `next.hasAttribute`, `next.nextSibling`, `separator.hidden`, `startingElement.hidden`, `startingElement?.nextElementSibling`

## AIWindowMenu.#addRecentChatsMenuitemHeader()
- 位置: L86-92
- 役割: 区切り線と最近のチャットの見出しを表示する。
- 触るとき: 最近のチャットの見出しを出す条件を変えるとき。
- 呼び出し先: `menu.querySelector()`
- 参照: `chatsHeader.hidden`, `separator.hidden`

## AIWindowMenu.#addRecentChatMenuitems()
- 位置: L94-108
- 役割: 会話ごとに menuitem を作り、タイトルと data-conv-id を設定して command イベントを付け、見出しの直後に挿入する。
- 触るとき: 最近のチャット項目の見た目や属性を変えるとき、クリック時に渡す会話 id を変えるとき。
- 呼び出し先: `chatsHeader.insertAdjacentElement()`, `document.createXULElement()`, `document.getElementById()`, `items.pop()`, `menuItem.addEventListener()`, `menuItem.classList.add()`, `menuItem.setAttribute()`
- 参照: `item.id`, `item.title`, `items.length`, `this.#onRecentChatMenuitemClick`, `win.document`

## AIWindowMenu.#onRecentChatMenuitemClick()
- 位置: async L110-125
- 役割: クリックされた会話を chatStore から引き、開き方を決めて AIWindowUI.reopenConversationInTab で開く。現在のタブ指定は新しいタブに読み替える。
- 触るとき: 最近のチャットを開く先(現在のタブ、新しいタブなど)の挙動を変えるとき。
- 呼び出し先: `AIWindow.chatStore.findConversationById()`, `AIWindowUI.reopenConversationInTab()`, `event.target.getAttribute()`, `lazy.BrowserUtils.whereToOpenLink()`
- 参照: `event.target.documentGlobal`
