# browser/components/aiwindow/ui/components/smartwindow-group-tabs/smartwindow-group-tabs.mjs

source: browser/components/aiwindow/ui/components/smartwindow-group-tabs/smartwindow-group-tabs.mjs
source-hash: baf5b9ef7ff4132108ba6621c19da0a9247d33c6
lines: 451

## <module>
- 役割: 「タブをグループ化」パネルのカード(提案と最近のグループ)と、その横に出るフライアウトを定義するモジュール。
- 呼び出し先: `customElements.define()`

## favicon()
- 位置: L21-32
- 役割: タブ情報の iconUrl を表示する img を作り、読み込みに失敗したら既定の favicon に差し替える。
- 触るとき: タブのアイコン表示や、読み込み失敗時の代替画像を変えるとき。
- 呼び出し先: `html()`
- 参照: `e.target.src`, `info.iconUrl`

## SmartwindowGroupTabsCard.constructor()
- 位置: L48-56
- 役割: 表示状態(計算中・提案・最近のグループ・重複数・タブグループ数)を初期化し、keydown を #onKeyDown に繋ぐ。
- 触るとき: パネルの初期状態を変えるとき、またはカード内のキー操作が効かないときに配線を確認するとき。
- 呼び出し先: `super()`, `this.#onKeyDown()`, `this.addEventListener()`
- 参照: `this.computing`, `this.duplicates`, `this.recent`, `this.suggestions`, `this.tabGroups`

## SmartwindowGroupTabsCard.createRenderRoot()
- 位置: L58-60
- 役割: shadow DOM を作らず、自身を描画先にする。
- 触るとき: スタイルシートがカードに届かない、または他のスタイルが効いてしまう問題を調べるとき。

## SmartwindowGroupTabsCard.connectedCallback()
- 位置: L62-68
- 役割: swgt-card クラス、role=dialog、見出しとの aria-labelledby、tabindex=-1 を付ける。
- 触るとき: カードのダイアログ属性やフォーカスの受け方を変えるとき。
- 呼び出し先: `super.connectedCallback()`, `this.classList.add()`, `this.setAttribute()`

## SmartwindowGroupTabsCard.#emit()
- 位置: L70-72
- 役割: 指定した型と detail で CustomEvent を自身から発火する。
- 触るとき: 親へ通知するイベント名を追加・変更するとき。
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowGroupTabsCard.#favicons()
- 位置: L74-78
- 役割: 先頭3件のタブの favicon を並べたアイコン群を返す。支援技術からは隠す。
- 触るとき: 提案行に並べるアイコンの数や表示を変えるとき。
- 呼び出し先: `favicon()`, `html()`, `tabInfos.slice()`, `tabInfos.slice(0, 3).map()`

## SmartwindowGroupTabsCard.#rows()
- 位置: L80-82
- 役割: カード内の .swgt-row 要素を文書順に配列で返す。
- 触るとき: 行の並びを前提にするキー操作を変えるとき。
- 呼び出し先: `this.querySelectorAll()`

## SmartwindowGroupTabsCard.#focusRowAt()
- 位置: L84-89
- 役割: 行が1つ以上あれば index を行数で割った余りの行にフォーカスする。負の値は末尾から数える。
- 触るとき: 行へのフォーカス移動で端を越えたときの扱いを変えるとき。
- 条件付き依存: `if (rows.length)` → `rows.at(index % rows.length)?.focus()`
- 条件付き依存: `if (rows.length)` → `rows.at()`
- 参照: `rows.length`, `this.#rows`

## SmartwindowGroupTabsCard.#moveRowFocus()
- 位置: L91-100
- 役割: 現在フォーカス中の行から direction だけ移動する。行の外にいれば下向きは先頭、上向きは末尾に移す。
- 触るとき: 上下キーで行をたどる挙動を変えるとき。
- 呼び出し先: `this.#focusRowAt()`, `this.#rows.indexOf()`, `this.ownerDocument.activeElement?.closest()`
- 条件付き依存: `if (current < 0)` → `this.#focusRowAt()`

## SmartwindowGroupTabsCard.#onKeyDown()
- 位置: L102-123
- 役割: 修飾キーが無いときだけ上下・Home・End を処理して行を移動し、既定動作を止める。
- 触るとき: カード内のキーボード操作を追加・変更するとき。
- 呼び出し先: `event.preventDefault()`, `this.#focusRowAt()`, `this.#moveRowFocus()`
- 参照: `event.altKey`, `event.ctrlKey`, `event.key`, `event.metaKey`, `event.shiftKey`

## SmartwindowGroupTabsCard.#emitPreview()
- 位置: L125-131
- 役割: detail に anchor(押された要素)と source(hover か focus)を加えて preview を発火する。
- 触るとき: プレビューのきっかけや渡す情報を変えるとき。
- 呼び出し先: `this.#emit()`
- 参照: `event.currentTarget`

## SmartwindowGroupTabsCard.#onRowFocus()
- 位置: L133-138
- 役割: refocused-by-panel が付いた行では何もせず、それ以外はフォーカスによる preview を発火する。
- 触るとき: パネルを閉じた後のフォーカス復帰でプレビューが勝手に出る問題を調べるとき。
- 呼び出し先: `event.currentTarget.hasAttribute()`, `this.#emitPreview()`

## SmartwindowGroupTabsCard.#onRowKeyDown()
- 位置: L140-145
- 役割: 左右矢印で既定動作を止め、preview-enter を発火する。
- 触るとき: 右矢印でフライアウトを開く操作を変えるとき。
- 条件付き依存: `if (event.key === "ArrowRight" || event.key === "ArrowLeft")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "ArrowRight" || event.key === "ArrowLeft")` → `this.#emit()`
- 参照: `event.currentTarget`, `event.key`

## SmartwindowGroupTabsCard.#suggestionRow()
- 位置: L147-167
- 役割: 提案グループを1つのボタン行にし、件数付きのラベルと先頭タブの favicon を載せる。hover・focus で preview、クリックで create-one を発火する。
- 触るとき: 提案行の表示や、その行が出すイベントの組み合わせを変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#emit()`, `this.#emitPreview()`, `this.#favicons()`, `this.#onRowFocus()`, `this.#onRowKeyDown()`
- 参照: `suggestion.id`, `suggestion.label`, `suggestion.tabInfos`, `suggestion.tabInfos.length`

## SmartwindowGroupTabsCard.#recentRow()
- 位置: L169-187
- 役割: 最近作ったグループの行を、グループ色の CSS 変数を付けたアイコンとラベルで描き、クリックで select-group を発火する。
- 触るとき: 最近のグループの色や選択時の動作を変えるとき。
- 呼び出し先: `html()`, `styleMap()`, `this.#emit()`
- 参照: `entry.color`, `entry.id`, `entry.label`

## SmartwindowGroupTabsCard.render()
- 位置: L189-302
- 役割: 見出し、提案、最近のグループ、ungroup、タブグループ表示、重複を閉じる行を条件に応じて組み立てる。提案も最近も無ければ案内文を出す。
- 触るとき: パネルの構成や表示条件、案内文の出し分けを変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#emit()`, `this.#emitPreview()`, `this.#onRowFocus()`, `this.#onRowKeyDown()`, `this.#recentRow()`, `this.#suggestionRow()`, `this.recent.map()`, `this.suggestions.map()`
- 参照: `e.currentTarget`, `this.computing`, `this.duplicates`, `this.recent.length`, `this.suggestions.length`, `this.tabGroups`

## SmartwindowGroupTabsFlyout.createRenderRoot()
- 位置: L321-323
- 役割: shadow DOM を作らず、自身を描画先にする。
- 触るとき: フライアウトのスタイルが効かない問題を調べるとき。

## SmartwindowGroupTabsFlyout.connectedCallback()
- 位置: L325-328
- 役割: swgt-flyout クラスを付ける。
- 触るとき: フライアウトのスタイルの対象を変えるとき。
- 呼び出し先: `super.connectedCallback()`, `this.classList.add()`

## SmartwindowGroupTabsFlyout.getUpdateComplete()
- 位置: async L330-334
- 役割: 通常の描画完了を待ち、さらに中の tab-groups-list の描画完了も待ってから結果を返す。
- 触るとき: フライアウトの描画完了を待つ側の挙動を変えるとき、または既存グループが描かれる前に操作されると疑うとき。
- 呼び出し先: `super.getUpdateComplete()`, `this.querySelector()`
- 参照: `this.querySelector("tab-groups-list")?.updateComplete`

## SmartwindowGroupTabsFlyout.focusFirstRow()
- 位置: L336-338
- 役割: フライアウト内の最初の行(ROW_SELECTOR)にフォーカスする。
- 触るとき: フライアウトを開いた直後のフォーカス先を変えるとき。
- 呼び出し先: `this.querySelector()`, `this.querySelector(ROW_SELECTOR)?.focus()`

## SmartwindowGroupTabsFlyout.#emit()
- 位置: L340-342
- 役割: 型と detail で CustomEvent を発火する。
- 触るとき: フライアウトから親へ送るイベントを足すとき。
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowGroupTabsFlyout.#onKeyDown()
- 位置: L344-371
- 役割: 上下で隣の行へ、Home・End で先頭と末尾へ移し、左右キーでは close-flyout を発火する。
- 触るとき: フライアウト内のキー操作を変えるとき。
- 呼び出し先: `(event.key === "Home" ? rows[0] : rows.at(-1)).focus()`, `event.preventDefault()`, `event.target.closest()`, `rows.at()`, `rows.indexOf()`, `rows[rows.indexOf(row) + step]?.focus()`, `this.#emit()`, `this.querySelectorAll()`
- 参照: `event.key`

## SmartwindowGroupTabsFlyout.#onGroupsClick()
- 位置: L373-377
- 役割: クリックされた先がボタンなら close-panel を発火し、パネルを閉じさせる。
- 触るとき: グループ一覧で項目を選んだ後にパネルを閉じるかどうかを変えるとき。
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if (event.target.closest("button, moz-button"))` → `this.#emit()`

## SmartwindowGroupTabsFlyout.render()
- 位置: L379-410
- 役割: groupsListId があれば tab-groups-list を keyed で描き直し、重複があれば重複タブ一覧、無ければ提案グループのタブ一覧を描く。
- 触るとき: フライアウトの中身の出し分けを変えるとき、または一覧が古いまま残る理由を調べるとき。
- 呼び出し先: `this.#emit()`, `this.#tabList()`
- 条件付き依存: `if (this.groupsListId)` → `html()`
- 条件付き依存: `if (this.groupsListId)` → `this.#onKeyDown()`
- 条件付き依存: `if (this.groupsListId)` → `this.#onGroupsClick()`
- 条件付き依存: `if (this.groupsListId)` → `keyed()`
- 条件付き依存: `if (this.duplicates?.length)` → `this.#tabList()`
- 条件付き依存: `if (this.duplicates?.length)` → `this.#emit()`
- 参照: `suggestion.id`, `suggestion.label`, `suggestion.tabInfos`, `this.duplicates`, `this.duplicates?.length`, `this.groupsListId`, `this.suggestion`

## SmartwindowGroupTabsFlyout.#tabList()
- 位置: L421-445
- 役割: タブごとにボタン行を並べ、クリックで行の位置を onSelect に渡す。groupLabel の有無で見出し ID を提案グループ用と重複タブ用に切り替える。
- 触るとき: フライアウトの行の表示や、クリック時に渡す情報を変えるとき。
- 呼び出し先: `JSON.stringify()`, `favicon()`, `html()`, `onSelect()`, `tabInfos.map()`, `this.#onKeyDown()`
- 参照: `info.title`
