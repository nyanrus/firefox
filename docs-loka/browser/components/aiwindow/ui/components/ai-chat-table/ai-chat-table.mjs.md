# browser/components/aiwindow/ui/components/ai-chat-table/ai-chat-table.mjs

source: browser/components/aiwindow/ui/components/ai-chat-table/ai-chat-table.mjs
source-hash: 49952b2c26a0c35b5568a108089c480171b15f29
lines: 132

## <module>
- 役割: チャットメッセージ内のMarkdown表を描画するカスタム要素 ai-chat-table を定義する。
- 呼び出し先: `customElements.define()`

## AIChatTable.constructor()
- 位置: L23-26
- 役割: isOverflowing を false で初期化する。
- 触るとき: 表の横はみ出し表示の初期状態を変えたいとき、または表示前に持たせる状態を追加するとき。
- 呼び出し先: `super()`
- 参照: `this.isOverflowing`

## AIChatTable.firstUpdated()
- 位置: L28-36
- 役割: 描画後にスクロールコンテナを取得し、ResizeObserver でコンテナと表を監視して、はみ出し判定を一度計算する。
- 触るとき: 表が横に広がっても案内が出ない、または案内が古いままになる不具合を調べるとき。
- 呼び出し先: `this.#observeTable()`, `this.#resizeObserver.observe()`, `this.#updateOverflow()`, `this.renderRoot.querySelector()`
- 参照: `this.#resizeObserver`, `this.#scrollContainer`

## AIChatTable.disconnectedCallback()
- 位置: L38-44
- 役割: DOM から外れたとき ResizeObserver を切断し、コンテナと表の参照をクリアする。
- 触るとき: 要素を取り外した後も監視が残って通知が続く不具合を調べるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.#resizeObserver?.disconnect()`
- 参照: `this.#observedTable`, `this.#resizeObserver`, `this.#scrollContainer`

## AIChatTable.#observeTable()
- 位置: L46-58
- 役割: 子の table を取得し、前回と同じなら何もせず、違えば旧表の監視を外して新しい表を監視対象にする。
- 触るとき: ストリーミング更新などで表が差し替わった後も、はみ出し判定が古い表を見ているとき。
- 呼び出し先: `this.querySelector()`
- 条件付き依存: `if (this.#observedTable)` → `this.#resizeObserver?.unobserve()`
- 条件付き依存: `if (table)` → `this.#resizeObserver?.observe()`
- 参照: `this.#observedTable`

## AIChatTable.#onSlotChange()
- 位置: L60-63
- 役割: slot の中身が変わったとき、表の監視先を付け替えてからはみ出し判定を再計算する。
- 触るとき: 表が後から差し込まれる、または入れ替わる経路の挙動を変えるとき。
- 呼び出し先: `this.#observeTable()`, `this.#updateOverflow()`

## AIChatTable.#updateOverflow()
- 位置: L65-71
- 役割: スクロールコンテナの scrollWidth と clientWidth の差が 1px を超えるかで isOverflowing を決める。
- 触るとき: はみ出し案内を出す判定の閾値を変えるとき、または案内が出ない原因を調べるとき。
- 参照: `container.clientWidth`, `container.scrollWidth`, `this.#scrollContainer`, `this.isOverflowing`

## AIChatTable.#messageId()
- 位置: L80-82
- 役割: 描画されているシャドウルートのホストの data-message-id から親メッセージの ID を読む。
- 触るとき: 表コピーで送られるメッセージ ID が空になる、または親メッセージ側の属性名を変えるとき。
- 呼び出し先: `this.getRootNode()`
- 参照: `this.getRootNode()?.host?.dataset.messageId`

## AIChatTable.#handleCopyTable()
- 位置: L84-95
- 役割: コピーボタンのクリックで、messageId と lineRange を detail に載せた copy-table イベントを発火する。
- 触るとき: 表のコピー機能の受け手を変えるとき、または detail に載せる情報を増やすとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.#messageId`, `this.lineRange`

## AIChatTable.render()
- 位置: L97-128
- 役割: 表のラッパー、メッセージ ID と行範囲がそろう時だけのコピーボタン、スクロールコンテナ、はみ出し時の案内ラベルを描画する。
- 触るとき: コピーボタンが出ない条件や、はみ出し案内の位置・文言を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.#handleCopyTable`, `this.#messageId`, `this.#onSlotChange`, `this.isOverflowing`, `this.lineRange`
