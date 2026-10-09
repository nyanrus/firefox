# browser/components/aiwindow/ui/components/ai-action-confirmation/ai-action-confirmation.mjs

source: browser/components/aiwindow/ui/components/ai-action-confirmation/ai-action-confirmation.mjs
source-hash: c522faef0e4345de37c8172b487b038568fad812
lines: 284

## <module>
- 役割: NL ブラウザ操作の完了を示す確認カード。操作の要約、元に戻すボタン、閉じたタブの一覧の開閉を描画する。
- 呼び出し先: `createRef()`, `customElements.define()`

## AIActionConfirmation.constructor()
- 位置: L49-56
- 役割: プロパティの初期値を設定し、ラベル、タブ、元に戻す可否、展開状態を空や既定値にする。
- 触るとき: カードの初期表示を変えるとき、または新しいプロパティを足すときに見る。
- 呼び出し先: `super()`
- 参照: `this.canUndo`, `this.isExpanded`, `this.labelL10nArgs`, `this.labelL10nId`, `this.tabs`

## AIActionConfirmation.#handleUndo()
- 位置: L58-65
- 役割: action-confirmation-undo イベントを発火する。
- 触るとき: 元に戻すボタンが効かないとき、またはイベント名を変えるときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AIActionConfirmation.#handleToggle()
- 位置: L67-79
- 役割: タブが無ければ何もせず、あれば展開状態を反転して action-confirmation-toggle を送る。
- 触るとき: 一覧の開閉が反応しないとき、またはイベントが親に届かないときに見る。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.isExpanded`, `this.tabs.length`

## AIActionConfirmation.#handleTabClick()
- 位置: L87-110
- 役割: リンクの既定の動作を止め、AIChatContent:OpenLink で URL を親へ渡す。修飾キーやボタンの押下があれば preferSwitchToTab を偽にして、開き方を親に任せる。
- 触るとき: タブのリンクが既存タブへ切り替わらないとき、または修飾キーで開き方が変わらないときに見る。
- 呼び出し先: `event.preventDefault()`, `this.dispatchEvent()`
- 参照: `tab.url`

## AIActionConfirmation.#updateOverflowState()
- 位置: L117-128
- 役割: 一覧が枠より高ければ scroller に data-overflowing を付け、そうでなければ外す。続けてスクロールの影を更新する。
- 触るとき: スクロールの影が出ない、または出たままになるときに見る。
- 呼び出し先: `scroller.hasAttribute()`, `this.#updateListScrollFade()`
- 条件付き依存: `if (overflowing !== scroller.hasAttribute("data-overflowing"))` → `scroller.toggleAttribute()`
- 参照: `list.clientHeight`, `list.scrollHeight`, `list?.parentElement`, `this.#tabsListRef.value`

## AIActionConfirmation.#handleScroll()
- 位置: L135-140
- 役割: CSS の scroll() アニメーションが使える環境では何もせず、使えなければスクロールの影を更新する。
- 触るとき: 古い環境でスクロールの影が動かないときに見る。
- 呼び出し先: `CSS.supports()`, `this.#updateListScrollFade()`

## AIActionConfirmation.#updateListScrollFade()
- 位置: L142-167
- 役割: scroll() が使えない環境では、フレームごとに一度だけスクロール量の割合を --action-confirmation-scroll-progress に書き込む。
- 触るとき: スクロールの影の位置や動きを変えるときに見る。
- 呼び出し先: `CSS.supports()`, `progress.toFixed()`, `requestAnimationFrame()`, `scroller.style.setProperty()`
- 参照: `list?.parentElement`, `this.#scrollAnimationId`, `this.#tabsListRef.value`

## AIActionConfirmation.#renderTab()
- 位置: L172-190
- 役割: タブのリンクを li の中に描画する。ファビコンが無ければ既定のファビコンを使い、タイトルを表示する。
- 触るとき: 閉じたタブの一覧の表示を変えるときに見る。
- 呼び出し先: `html()`, `this.#handleTabClick()`
- 参照: `tab.iconSrc`, `tab.title`, `tab.url`

## AIActionConfirmation.updated()
- 位置: L192-212
- 役割: 一覧の要素が変わったら、サイズ監視と scroll のリスナーを付け替える。
- 触るとき: 一覧を開いた後に影やサイズの追従が止まるときに見る。
- 条件付き依存: `if (!this.#resizeObserver)` → `this.#updateOverflowState()`
- 条件付き依存: `if (this.#observedList)` → `this.#resizeObserver.unobserve()`
- 条件付き依存: `if (this.#observedList)` → `this.#observedList.removeEventListener()`
- 条件付き依存: `if (list)` → `this.#resizeObserver.observe()`
- 条件付き依存: `if (list)` → `list.addEventListener()`
- 参照: `this.#handleScroll`, `this.#observedList`, `this.#resizeObserver`, `this.#tabsListRef.value`

## AIActionConfirmation.disconnectedCallback()
- 位置: L214-224
- 役割: サイズ監視を外し、scroll のリスナーと保留中の描画フレームを取り消す。
- 触るとき: カードを外した後も処理が残るときに見る。
- 呼び出し先: `super.disconnectedCallback()`, `this.#observedList?.removeEventListener()`, `this.#resizeObserver?.disconnect()`
- 条件付き依存: `if (this.#scrollAnimationId)` → `cancelAnimationFrame()`
- 参照: `this.#handleScroll`, `this.#observedList`, `this.#resizeObserver`, `this.#scrollAnimationId`

## AIActionConfirmation.render()
- 位置: L226-280
- 役割: ラベル、元に戻すボタン、展開時のタブ一覧を描画する。タブが無ければ展開ボタンを無効にする。
- 触るとき: カードの見た目や展開できる条件を変えるときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `ref()`, `this.#renderTab()`, `this.tabs.map()`
- 参照: `this.#handleToggle`, `this.#handleUndo`, `this.#tabsListRef`, `this.canUndo`, `this.isExpanded`, `this.labelL10nArgs`, `this.labelL10nId`, `this.tabs.length`
