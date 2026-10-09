# browser/components/aiwindow/ui/components/smartwindow-resume-section/smartwindow-resume-section.mjs

source: browser/components/aiwindow/ui/components/smartwindow-resume-section/smartwindow-resume-section.mjs
source-hash: ac733577185256b53427953c01d99b3a586f1e17
lines: 211

## <module>
- 役割: スマートウィンドウの再開(resume)カードを折りたたみ可能な一覧で表示する custom element を定義する
- 呼び出し先: `customElements.define()`

## SmartwindowResumeSection.constructor()
- 位置: L36-42
- 役割: プロパティ cards, emptyReason, loading, expanded を初期化する
- 触るとき: 新しい既定状態(空配列・非読込・折りたたみ)を変えたいとき
- 呼び出し先: `super()`
- 参照: `this.cards`, `this.emptyReason`, `this.expanded`, `this.loading`

## SmartwindowResumeSection.#dispatch()
- 位置: L44-52
- 役割: smartwindow-resume-section:<type> の CustomEvent を bubbles/composed 付きで発火する
- 触るとき: 親ページに新しい操作イベントを通知する種類を増やすとき
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowResumeSection.#onToggleClick()
- 位置: L54-56
- 役割: 「もっと見る/折りたたむ」ボタンで expanded を反転させる
- 触るとき: カードの表示件数の切り替え挙動を変えるとき
- 参照: `this.expanded`

## SmartwindowResumeSection.#onHideClick()
- 位置: L58-60
- 役割: セクション非表示ボタンで hide イベントを emptyReason 付きで発火する
- 触るとき: 非表示操作の理由(reason)を親側で判定するロジックを調べるとき
- 呼び出し先: `this.#dispatch()`
- 参照: `this.emptyReason`

## SmartwindowResumeSection.#renderEmptyState()
- 位置: L62-98
- 役割: カードが無いときの空表示を描く(全件非表示か提案なしかで文言を切り替える)
- 触るとき: 空状態の文言や非表示ボタンの配置を変えるとき、新しい emptyReason を追加するとき
- 呼び出し先: `html()`
- 参照: `RESUME_SECTION_EMPTY_REASON.ALL_DISMISSED`, `this.#onHideClick`, `this.emptyReason`

## SmartwindowResumeSection.#renderSkeletonCard()
- 位置: L100-132
- 役割: 読み込み中に出すカード型のスケルトン表示を描く
- 触るとき: 読み込み中の見た目(骨格の形)を調整するとき
- 呼び出し先: `html()`

## SmartwindowResumeSection.#renderLoadingState()
- 位置: L134-152
- 役割: 読み込み中の見出しと COLLAPSED_CARD_COUNT 枚のスケルトンを描く
- 触るとき: 読み込み中に並べるスケルトンの枚数や構成を変えるとき
- 呼び出し先: `Array.from()`, `html()`, `this.#renderSkeletonCard()`

## SmartwindowResumeSection.render()
- 位置: L154-207
- 役割: loading、空、カード一覧の順に分岐して描画し、2枚を超えると「もっと見る」を出す
- 触るとき: 表示状態の分岐条件や折りたたみ時に見せる枚数を変えるとき、カードの渡し方を調べるとき
- 呼び出し先: `JSON.stringify()`, `Math.max()`, `html()`, `this.cards.slice()`, `visibleCards.map()`
- 条件付き依存: `if (this.loading)` → `this.#renderLoadingState()`
- 条件付き依存: `if (!this.cards.length)` → `this.#renderEmptyState()`
- 参照: `memory.id`, `this.#onToggleClick`, `this.cards`, `this.cards.length`, `this.emptyReason`, `this.expanded`, `this.loading`
