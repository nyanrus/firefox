# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/assistant-message-footer.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/assistant-message-footer.mjs
source-hash: c0f88ef6eba1ae7478e75bfd1756af9f61f87db4
lines: 174

## <module>
- 役割: アシスタント回答の下に出るコピー、再試行、評価、適用メモリーのボタン列を定義する。
- 呼び出し先: `customElements.define()`

## AssistantMessageFooter.constructor()
- 位置: L54-60
- 役割: メッセージ ID を null、適用メモリーを空、再試行は表示の既定値で初期化する。
- 触るとき: footer に渡す既定値を変えるとき、または再試行ボタンが出ない原因を探すときに見る。
- 呼び出し先: `super()`
- 参照: `this.appliedMemories`, `this.hideRetry`, `this.messageId`, `this.showCallout`

## AssistantMessageFooter.events()
- 位置: L67-74
- 役割: コピー・再試行・高評価・低評価それぞれのイベント名を返す。
- 触るとき: 親が受け取るイベント名を変えるとき、ここと親のリスナーを合わせて直す。

## AssistantMessageFooter.#emit()
- 位置: L76-83
- 役割: 共通設定（bubbles、composed）に detail を足して CustomEvent を発火する。
- 触るとき: イベントの伝播設定や detail の形を変えるとき、または親にイベントが届かないときに見る。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.constructor.eventBehaviors`

## AssistantMessageFooter.#emitCopy()
- 位置: L85-87
- 役割: copy-message を messageId 付きで発火する。
- 触るとき: コピー操作の通知内容を変えるとき、または親のコピー処理が動かないときに見る。
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.copy`, `this.messageId`

## AssistantMessageFooter.#emitRetry()
- 位置: L89-91
- 役割: retry-message を messageId 付きで発火する。
- 触るとき: 再生成の依頼内容を変えるとき、または再試行が効かないときに見る。
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.retry`, `this.messageId`

## AssistantMessageFooter.#emitThumbsUp()
- 位置: L93-95
- 役割: thumbs-up を messageId 付きで発火する。
- 触るとき: 高評価の送信処理を変えるとき、または高評価が親に届かないときに見る。
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.thumbsUp`, `this.messageId`

## AssistantMessageFooter.#emitThumbsDown()
- 位置: L97-101
- 役割: thumbs-down を messageId 付きで発火する。
- 触るとき: 低評価の送信処理を変えるとき、または低評価が親に届かないときに見る。
- 呼び出し先: `this.#emit()`
- 参照: `this.constructor.events.thumbsDown`, `this.messageId`

## AssistantMessageFooter.render()
- 位置: L103-170
- 役割: 評価・コピー・再試行（hideRetry 時は省略）のボタンと applied-memories-button を並べる。
- 触るとき: footer のボタン構成や並び順を変えるとき、または hide-retry を付けたときに再試行が消えるか確認するときに見る。
- 呼び出し先: `html()`, `this.#emitCopy()`, `this.#emitRetry()`, `this.#emitThumbsDown()`, `this.#emitThumbsUp()`
- 参照: `this.appliedMemories`, `this.hideRetry`, `this.messageId`, `this.showCallout`
