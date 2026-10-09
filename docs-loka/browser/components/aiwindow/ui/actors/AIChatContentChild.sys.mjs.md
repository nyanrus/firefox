# browser/components/aiwindow/ui/actors/AIChatContentChild.sys.mjs

source: browser/components/aiwindow/ui/actors/AIChatContentChild.sys.mjs
source-hash: 0f2ae3565a128cb7c728df1a37059d1c185012e0
lines: 147

## <module>
- 役割: チャット画面のコンテンツ側と親プロセスをつなぐ子アクター。コンテンツからのイベントを親へ送り、親からのメッセージを画面のai-chat-content要素へ届ける。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## AIChatContentChild.handleEvent()
- 位置: L65-90
- 役割: 許可されたイベント名だけを通し、コピー操作ならクリップボードへ書いてから、イベントの詳細を親へ送る。
- 触るとき: チャットの画面からのコピーや操作が親に届かないとき、許可するイベント名を増やすとき。
- 呼び出し先: `AIChatContentChild.#VALID_EVENTS_FROM_CONTENT.has()`, `copyActions.includes()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!AIChatContentChild.#VALID_EVENTS_FROM_CONTENT.has(event.type))` → `console.warn()`
- 条件付き依存: `if (isCopyAction)` → `lazy.ClipboardHelper.copyString()`
- 参照: `event.detail`, `event.type`, `this.windowContext`

## AIChatContentChild.receiveMessage()
- 位置: async L92-105
- 役割: 親からのメッセージ名を対応表で画面のイベント名に変え、その内容を画面へ届ける。未知の名前は警告して何もしない。
- 触るとき: 親からの新しいメッセージを画面に届けるための対応を追加するとき。
- 呼び出し先: `this.#dispatchToChatContent()`
- 条件付き依存: `if (!mapping)` → `console.warn()`
- 参照: `AIChatContentChild.#EVENT_MAPPINGS_FROM_PARENT`, `mapping.event`, `message.data`, `message.name`

## AIChatContentChild.#dispatchToChatContent()
- 位置: L107-130
- 役割: ai-chat-content要素を探し、ペイロードを内容側のウィンドウへ複製して、バブルするCustomEventとして発火する。失敗時はエラーを記録し、クライアントエラーとして親へ報告する。
- 触るとき: チャットの画面で親からの通知が反映されないと調べるとき、ペイロードの複製で失敗が起きると調べるとき。
- 呼び出し先: `Cu.cloneInto()`, `chatContent.dispatchEvent()`, `console.error()`, `this.#reportDispatchFailure()`, `this.document.querySelector()`
- 条件付き依存: `if (!chatContent)` → `console.error()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`

## AIChatContentChild.#reportDispatchFailure()
- 位置: L132-145
- 役割: 配信の失敗を、クライアントエラーの詳細にしてAIChatContent:ClientErrorで親へ送る。送信自体の失敗は警告だけにする。
- 触るとき: 配信の失敗がテレメトリに出ないと調べるとき、報告の形式を変えるとき。
- 呼び出し先: `console.warn()`, `serializeClientErrorDetail()`, `this.sendAsyncMessage()`
