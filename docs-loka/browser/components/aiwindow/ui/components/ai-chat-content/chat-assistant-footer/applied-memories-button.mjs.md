# browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/applied-memories-button.mjs

source: browser/components/aiwindow/ui/components/ai-chat-content/chat-assistant-footer/applied-memories-button.mjs
source-hash: 71788348bd958e2bce90343fd8913b3d548641ad
lines: 412

## <module>
- 役割: アシスタント回答の「メモリーを使用」ボタンと、適用メモリーのポップオーバーを定義する。
- 呼び出し先: `customElements.define()`

## AppliedMemoriesButton.constructor()
- 位置: L61-70
- 役割: メッセージ ID、適用メモリー、開閉状態を初期化し、document 監視用のハンドラーを bind する。
- 触るとき: ポップオーバーの既定の開閉状態を変えるとき、またはハンドラーの this が外れて動かないときに見る。
- 呼び出し先: `super()`, `this._onDocumentClick.bind()`, `this._onKeyDown.bind()`
- 参照: `this._onDocumentClick`, `this._onKeyDown`, `this.appliedMemories`, `this.messageId`, `this.open`, `this.showCallout`

## AppliedMemoriesButton.connectedCallback()
- 位置: L72-76
- 役割: document の click とこの要素の keydown にリスナーを登録する。
- 触るとき: 外側クリックや Escape で閉じない不具合を調べるときに見る。
- 呼び出し先: `document.addEventListener()`, `super.connectedCallback()`, `this.addEventListener()`
- 参照: `this._onDocumentClick`, `this._onKeyDown`

## AppliedMemoriesButton.disconnectedCallback()
- 位置: L78-82
- 役割: connectedCallback で登録した document の click と keydown のリスナーを外す。
- 触るとき: 要素を外した後にリスナーが残ってメモリー欄が動くような不具合を見るときに見る。
- 呼び出し先: `document.removeEventListener()`, `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this._onDocumentClick`, `this._onKeyDown`

## AppliedMemoriesButton.willUpdate()
- 位置: L84-89
- 役割: showCallout が真になったとき、説明付きポップオーバーを表示する状態を立てる。
- 触るとき: 最初に適用されたメッセージで説明を出す条件を変えるときに見る。
- 呼び出し先: `changedProperties.has()`, `super.willUpdate()`
- 参照: `this.#showCalloutState`, `this.showCallout`

## AppliedMemoriesButton.updated()
- 位置: L91-97
- 役割: showCallout が変わったら #syncCalloutOpenState を呼び、必要なら開く。
- 触るとき: 説明の自動表示が二重に開く、または開かないときに見る。
- 呼び出し先: `changedProperties.has()`, `super.updated()`
- 条件付き依存: `if (changedProperties.has("showCallout"))` → `this.#syncCalloutOpenState()`

## AppliedMemoriesButton.#syncCalloutOpenState()
- 位置: L99-109
- 役割: showCallout が真で未開なら開き、先頭の削除ボタンへフォーカスして開閉を通知する。
- 触るとき: 説明の自動表示時のフォーカス位置や通知内容を変えるときに見る。
- 呼び出し先: `this.#dispatchToggleAppliedMemories()`, `this.#focusDeleteButtonAt()`, `this.toggleAttribute()`, `this.updateComplete.then()`
- 参照: `this.open`, `this.showCallout`

## AppliedMemoriesButton.#dispatchToggleAppliedMemories()
- 位置: L111-122
- 役割: toggle-applied-memories を messageId と開閉状態 open 付きで発火する。
- 触るとき: 開閉通知を親が受け取れないとき、または通知の detail を変えるときに見る。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.messageId`

## AppliedMemoriesButton._hasMemories()
- 位置: L124-126
- 役割: 適用メモリーが 1 件以上あるかを返す。
- 触るとき: メモリーが無いメッセージでボタンを隠す条件を変えるときに見る。
- 呼び出し先: `Array.isArray()`
- 参照: `this.appliedMemories`, `this.appliedMemories.length`

## AppliedMemoriesButton._visibleMemories()
- 位置: L128-130
- 役割: 適用メモリーの先頭 5 件を返す。
- 触るとき: ポップオーバーに出す件数の上限を変えるときに見る。
- 呼び出し先: `this.appliedMemories.slice()`

## AppliedMemoriesButton.#onTriggerClick()
- 位置: L132-149
- 役割: ボタン押下で開閉を反転させ、閉じるとき説明状態を消し、先頭へフォーカスして通知する。
- 触るとき: トリガーの開閉動作や閉じた後の説明状態の扱いを変えるときに見る。
- 呼び出し先: `event.stopPropagation()`, `this.#dispatchToggleAppliedMemories()`, `this.toggleAttribute()`
- 条件付き依存: `if (this.open)` → `this.updateComplete.then()`
- 条件付き依存: `if (this.open)` → `this.#focusDeleteButtonAt()`
- 参照: `this.#showCalloutState`, `this._hasMemories`, `this.open`

## AppliedMemoriesButton._onPopoverClick()
- 位置: L151-153
- 役割: ポップオーバー内のクリックが外側のクリック処理に届かないよう伝播を止める。
- 触るとき: ポップオーバー内を押しても閉じてしまうときに見る。
- 呼び出し先: `event.stopPropagation()`

## AppliedMemoriesButton._onDocumentClick()
- 位置: L155-160
- 役割: 開いている時に文書内のクリックがあれば、ポップオーバーを閉じる。
- 触るとき: 外側クリックで閉じる挙動を変えるとき、または閉じない原因を探すときに見る。
- 呼び出し先: `this.#closePopover()`
- 参照: `this.open`

## AppliedMemoriesButton._onKeyDown()
- 位置: L162-199
- 役割: 開いている時の Escape、Tab、矢印、Home、End のキー操作を処理する。
- 触るとき: ポップオーバーのキーボード操作やフォーカス移動を変えるときに見る。
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`, `this.#closePopover()`, `this.#focusDeleteButtonAt()`, `this.#moveDeleteFocus()`, `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector(".memories-trigger")?.focus()`
- 条件付き依存: `if ( !event.shiftKey && this.shadowRoot.activeElement === this.shadowRoot.querySelector(".retry-without-memories-button") )` → `this.#closePopover()`
- 参照: `event.key`, `event.shiftKey`, `this.open`, `this.shadowRoot.activeElement`

## AppliedMemoriesButton.#deleteButtons()
- 位置: L201-206
- 役割: ポップオーバー内の削除ボタン一覧を配列で返す。
- 触るとき: 削除ボタンのクラス名を変えると矢印キーの移動が効かなくなるので、ここを確認する。
- 呼び出し先: `popover.querySelectorAll()`, `this.shadowRoot.querySelector()`

## AppliedMemoriesButton.#moveDeleteFocus()
- 位置: L208-217
- 役割: 現在の削除ボタンから指定方向へ、末尾から先頭へ循環してフォーカスを移す。
- 触るとき: 上下キーの移動の仕方（循環の有無など）を変えるときに見る。
- 呼び出し先: `items.indexOf()`, `this.#focusDeleteButtonAt()`
- 参照: `items.length`, `this.#deleteButtons`, `this.shadowRoot.activeElement`

## AppliedMemoriesButton.#focusDeleteButtonAt()
- 位置: L219-231
- 役割: 指定位置の削除ボタンへ tabIndex を付け替えてフォーカスする。負の値は末尾から数える。
- 触るとき: Home や End でフォーカスが合わないとき、またはタブ順を変えるときに見る。
- 呼び出し先: `items.forEach()`, `items[index].focus()`
- 参照: `item.tabIndex`, `items.length`, `this.#deleteButtons`

## AppliedMemoriesButton.#closePopover()
- 位置: L233-240
- 役割: 開閉状態と説明状態を閉じ、data-open を外して isOpen false の通知を出す。
- 触るとき: 閉じた後に説明が残る、または通知が出ないときに見る。
- 呼び出し先: `this.#dispatchToggleAppliedMemories()`, `this.requestUpdate()`, `this.toggleAttribute()`
- 参照: `this.#showCalloutState`, `this.open`

## AppliedMemoriesButton._onRemoveMemory()
- 位置: L242-255
- 役割: 削除ボタンの click を止め、remove-applied-memory に memory と messageId を載せて発火する。
- 触るとき: 個別のメモリー削除の通知内容を変えるとき、または削除が親に届かないときに見る。
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.messageId`

## AppliedMemoriesButton._onRetryWithoutMemories()
- 位置: L257-269
- 役割: retry-without-memories を messageId 付きで発火し、クリックの伝播を止める。
- 触るとき: メモリーを外して再生成する導線を変えるときに見る。
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.messageId`

## AppliedMemoriesButton._onManageMemories()
- 位置: L271-278
- 役割: manage-memories イベントを発火し、メモリー管理画面への移動を親に任せる。
- 触るとき: メモリー管理への導線を変えるときや、管理画面が開かないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AppliedMemoriesButton.renderCallout()
- 位置: L280-302
- 役割: 初回の説明文と「詳しく見る」ボタンを持つ吹き出しを描画する。
- 触るとき: 初回の説明文やリンク先を変えるとき、またはリンクが反応しないときに見る。
- 呼び出し先: `html()`, `this.dispatchEvent()`

## AppliedMemoriesButton.renderPopover()
- 位置: L304-381
- 役割: 適用メモリーを一覧、削除ボタン、管理・再試行の行とともに描画する。
- 触るとき: ポップオーバーの中身や並び順を変えるとき、またはメモリーが一覧に出ないときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `this._onManageMemories()`, `this._onPopoverClick()`, `this._onRemoveMemory()`, `this._onRetryWithoutMemories()`, `this.renderCallout()`, `visibleMemories.map()`
- 参照: `memory.memory_summary`, `this.#showCalloutState`, `this._hasMemories`, `this._visibleMemories`, `this.open`

## AppliedMemoriesButton.render()
- 位置: L383-408
- 役割: 適用メモリーが無ければ何も描かず、あればトリガーボタンとポップオーバーを描画する。
- 触るとき: トリガーの表示条件や aria-expanded の値を変えるときに見る。
- 呼び出し先: `html()`, `this.#onTriggerClick()`, `this.renderPopover()`
- 参照: `this._hasMemories`, `this.open`
