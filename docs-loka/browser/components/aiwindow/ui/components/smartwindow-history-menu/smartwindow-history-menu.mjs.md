# browser/components/aiwindow/ui/components/smartwindow-history-menu/smartwindow-history-menu.mjs

source: browser/components/aiwindow/ui/components/smartwindow-history-menu/smartwindow-history-menu.mjs
source-hash: 366fc55006b85ac59c48180b99fb0c43cc9797cf
lines: 230

## <module>
- 役割: スマートウィンドウの履歴メニュー(サイドバーの「…」メニューと、フルページの新規・履歴・その他の行)を定義するモジュール。
- 呼び出し先: `customElements.define()`

## SmartwindowHistoryMenu.constructor()
- 位置: L40-45
- 役割: 表示モードを sidebar、最近のチャットを空、表示中の画面を main にして初期化する。
- 触るとき: 初期表示の画面やモードを変えるとき。
- 呼び出し先: `super()`
- 参照: `this.mode`, `this.recentChats`, `this.view`

## SmartwindowHistoryMenu.#dispatch()
- 位置: L47-55
- 役割: smartwindow-history-menu:種別 の名前で、バブルしてシャドウ境界を越える CustomEvent を発火する。
- 触るとき: 親へ送る履歴メニューのイベント名や detail の形式を変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowHistoryMenu.#requestRecentChats()
- 位置: L57-57
- 役割: 最近のチャット一覧の更新を親に依頼する request-recent-chats を発火する。
- 触るとき: 最近のチャット一覧をいつ更新させるかを変えるとき。
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onNewChat()
- 位置: L59-59
- 役割: new-chat を発火する。
- 触るとき: 新規チャットの操作を親に伝える経路を変えるとき。
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onViewAllChats()
- 位置: L61-61
- 役割: view-all-chats を発火する。
- 触るとき: すべてのチャットを開く操作の経路を変えるとき。
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onOpenSettings()
- 位置: L63-63
- 役割: open-settings を発火する。
- 触るとき: 設定を開く操作の経路を変えるとき。
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onOpenChat()
- 位置: L65-67
- 役割: 指定チャットの conversationId を入れた open-chat を発火する。
- 触るとき: チャットを開くときに親へ渡す情報を変えるとき。
- 呼び出し先: `this.#dispatch()`

## SmartwindowHistoryMenu.#onSidebarMenuShown()
- 位置: L70-73
- 役割: メニューが開いたら表示画面を main に戻し、最近のチャット一覧の更新を依頼する。
- 触るとき: メニューを開いたときの初期画面や更新の挙動を変えるとき。
- 呼び出し先: `this.#requestRecentChats()`
- 参照: `this.view`

## SmartwindowHistoryMenu.#onChatHistoryNavClick()
- 位置: L76-80
- 役割: 伝播を止めてメニューを開いたままにし、最近のチャット一覧の更新を依頼してから画面を chats に切り替える。
- 触るとき: チャット履歴への移動や、クリック後にメニューが閉じてしまう問題を調べるとき。
- 呼び出し先: `event.stopPropagation()`, `this.#requestRecentChats()`
- 参照: `this.view`

## SmartwindowHistoryMenu.#onBackClick()
- 位置: L82-85
- 役割: 伝播を止めてから画面を main に戻す。
- 触るとき: 履歴画面の戻る操作を変えるとき。
- 呼び出し先: `event.stopPropagation()`
- 参照: `this.view`

## SmartwindowHistoryMenu.#recentChatRowTemplate()
- 位置: L90-103
- 役割: チャット1件の panel-item を描く。外部ページの URL があればそのサイトのアイコンを重ね、about: ページなら履歴のアイコンを使う。クリックで open-chat を発火する。
- 触るとき: チャット行の見た目やアイコンの選び方を変えるとき。
- 呼び出し先: `chat.pageUrl.startsWith()`, `html()`, `styleMap()`, `this.#onOpenChat()`
- 参照: `chat.id`, `chat.pageUrl`, `chat.title`

## SmartwindowHistoryMenu.#recentChatsListTemplate()
- 位置: L105-118
- 役割: 最近のチャットの行を並べ、1件以上あれば区切り線を入れ、最後に「すべてのチャット」の行を置く。
- 触るとき: 最近のチャット一覧の構成や区切りを変えるとき。
- 呼び出し先: `html()`, `styleMap()`, `this.#recentChatRowTemplate()`, `this.recentChats.map()`
- 参照: `this.#onViewAllChats`, `this.recentChats.length`

## SmartwindowHistoryMenu.#mainViewTemplate()
- 位置: L120-132
- 役割: チャット履歴へ移る行と設定の行の2つの panel-item を返す。
- 触るとき: メイン画面の項目を増減するとき。
- 呼び出し先: `html()`
- 参照: `this.#onChatHistoryNavClick`, `this.#onOpenSettings`

## SmartwindowHistoryMenu.#chatHistoryViewTemplate()
- 位置: L134-153
- 役割: 戻るボタン、見出し、区切り線、最近のチャット一覧で履歴画面を組み立てる。
- 触るとき: 履歴画面のヘッダーや構成を変えるとき。
- 呼び出し先: `html()`, `this.#recentChatsListTemplate()`
- 参照: `this.#onBackClick`

## SmartwindowHistoryMenu.#sidebarTemplate()
- 位置: L155-175
- 役割: 「…」の moz-button と panel-list を組み立て、画面が chats なら履歴画面、それ以外はメイン画面を入れる。
- 触るとき: サイドバーのメニューのボタンや画面の切り替えを変えるとき。
- 呼び出し先: `html()`, `this.#chatHistoryViewTemplate()`, `this.#mainViewTemplate()`
- 参照: `this.#onSidebarMenuShown`, `this.view`

## SmartwindowHistoryMenu.#fullpageTemplate()
- 位置: L177-214
- 役割: フルページの新規チャット、チャット履歴(開くと一覧を更新)、その他(設定のみ)の3つのボタンと、それぞれのメニューを描く。
- 触るとき: フルページの操作ボタンの構成や、メニューの中身を変えるとき。
- 呼び出し先: `html()`, `this.#recentChatsListTemplate()`
- 参照: `this.#onNewChat`, `this.#onOpenSettings`, `this.#requestRecentChats`

## SmartwindowHistoryMenu.render()
- 位置: L216-226
- 役割: スタイルシートを読み込み、mode が fullpage ならフルページ用、それ以外はサイドバー用の要素を描く。
- 触るとき: モードによる出し分けや全体の描画を変えるとき。
- 呼び出し先: `html()`, `this.#fullpageTemplate()`, `this.#sidebarTemplate()`
- 参照: `this.mode`
