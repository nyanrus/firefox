# browser/components/aiwindow/ui/components/website-chip-container/website-chip-container.mjs

source: browser/components/aiwindow/ui/components/website-chip-container/website-chip-container.mjs
source-hash: 39f1b62f6627f625eeb3c9ff99545cef7a04515a
lines: 242

## <module>
- 役割: サイトのチップを並べ、件数に応じて折り返し・グループ化・はみ出し表示を切り替える要素を定義する
- 呼び出し先: `SmartwindowOverflowRowMixin()`, `customElements.define()`

## WebsiteChipContainer.constructor()
- 位置: L45-56
- 役割: チップの既定値(種類 context-chip、削除不可、グループ化なし、自動はみ出しなし)を設定する
- 触るとき: 呼び出し側が指定しなかった時の既定の動きを調べるとき
- 呼び出し先: `super()`
- 参照: `this.autoOverflow`, `this.chipSize`, `this.chipType`, `this.isPanelOpen`, `this.removable`, `this.shouldGroupChips`, `this.visibleChipCount`, `this.websites`

## WebsiteChipContainer.overflowContainerSelector()
- 位置: L58-60
- 役割: はみ出し行の共通基盤に渡すスクローラー要素のセレクタ(.chip-container-scroller)を返す
- 触るとき: はみ出し計測の対象要素を別の要素に変えるとき

## WebsiteChipContainer.inlineItemCount()
- 位置: L62-64
- 役割: 基盤に渡す、行内に収める件数として visibleChipCount を返す
- 触るとき: 行内に何件まで出すかの決まり方を調べるとき
- 参照: `this.visibleChipCount`

## WebsiteChipContainer.overflowItems()
- 位置: L66-68
- 役割: 自動はみ出し時のみ全サイトを返し、それ以外は空配列を返す
- 触るとき: はみ出しメニューの候補がどう決まるかを調べるとき
- 参照: `this.#isAutoOverflowing`, `this.websites`

## WebsiteChipContainer.#isGrouped()
- 位置: L70-72
- 役割: shouldGroupChips が true かつ 3 件以上のとき真
- 触るとき: 何件からグループ表示にするかの閾値を変えるとき
- 参照: `this.shouldGroupChips`, `this.websites.length`

## WebsiteChipContainer.#isAutoOverflowing()
- 位置: L74-76
- 役割: autoOverflow が有効で、かつグループ表示でないとき真
- 触るとき: グループ表示と自動はみ出しの優先関係を変えるとき
- 参照: `this.#isGrouped`, `this.autoOverflow`

## WebsiteChipContainer.#panel()
- 位置: L78-80
- 役割: 内部の smartwindow-panel-list 要素を取得する
- 触るとき: はみ出しパネルの参照先を調べるとき
- 呼び出し先: `this.renderRoot.querySelector()`

## WebsiteChipContainer.#onToggleClick()
- 位置: L82-88
- 役割: 押されたボタンを anchor にしてはみ出しパネルを開閉する
- 触るとき: はみ出しパネルの開き方や位置決めを変えるとき
- 呼び出し先: `this.#panel()`
- 条件付き依存: `if (panel)` → `panel.toggle()`
- 参照: `event.currentTarget`, `panel.anchor`

## WebsiteChipContainer.#onOverflowItemSelected()
- 位置: L90-104
- 役割: パネルを閉じ、タブグループ以外の項目は preferSwitchToTab 付きの AIChatContent:OpenLink で開く(既存タブがあれば切り替える)
- 触るとき: はみ出しメニューからの遷移先の決まり方を変えるとき
- 呼び出し先: `this.#panel()`, `this.#panel()?.hide()`, `this.dispatchEvent()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `event.detail`

## WebsiteChipContainer.#onRemoveWebsite()
- 位置: L106-119
- 役割: チップの削除要求を伝播を止めたうえで ai-website-chip:remove として通知する
- 触るとき: チップ削除時に親へ渡す情報を増やすとき
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `website.groupId`, `website.label`, `website.url`

## WebsiteChipContainer.#renderStackedChips()
- 位置: L121-133
- 役割: 1 件をタブグループか通常サイトかに応じた ai-website-chip として描く
- 触るとき: チップ 1 件の表示内容(色、アイコン、削除可否)を変えるとき
- 呼び出し先: `html()`, `this.#onRemoveWebsite()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `this.chipSize`, `this.chipType`, `this.removable`, `website.color`, `website.iconSrc`, `website.label`, `website.type`, `website.url`

## WebsiteChipContainer.#renderGroupedChips()
- 位置: L135-139
- 役割: 全件を ai-grouped-chip-container に渡して 1 つにまとめて描く
- 触るとき: グループ表示の見た目や渡すデータを変えるとき
- 呼び出し先: `html()`

## WebsiteChipContainer.#renderChip()
- 位置: L141-152
- 役割: 履歴から削除済みのサイトは削除済み表示、それ以外は通常のチップを描く
- 触るとき: 削除済みサイトの見せ方を変えるとき
- 呼び出し先: `html()`, `this.#renderStackedChips()`
- 参照: `website.historyDeleted`

## WebsiteChipContainer.#renderSmartwindowOverflowRow()
- 位置: L154-200
- 役割: visibleCount より後ろの項目に data-overflow を付け、残りを数えた「+N more」ボタンとパネルを描く
- 触るとき: はみ出しボタンの文言や、はみ出し項目の並び・パネルの中身を変えるとき
- 呼び出し先: `JSON.stringify()`, `Math.min()`, `String()`, `getTabGroupMentionId()`, `html()`, `overflow.map()`, `repeat()`, `this.#renderChip()`, `this.websites.slice()`
- 参照: `overflow.length`, `this.#onOverflowItemSelected`, `this.#onToggleClick`, `this.isPanelOpen`, `this.visibleCount`, `this.websites`, `this.websites.length`, `website.color`, `website.groupId`, `website.iconSrc`, `website.label`, `website.type`, `website.url`

## WebsiteChipContainer.#renderScrollerRow()
- 位置: L202-211
- 役割: 全チップを 1 行のスクローラーに並べて描く
- 触るとき: はみ出しを使わない通常の横並び表示を変えるとき
- 呼び出し先: `html()`, `repeat()`, `this.#renderChip()`
- 参照: `this.websites`

## WebsiteChipContainer.#renderChips()
- 位置: L213-220
- 役割: グループ表示、自動はみ出し、通常スクローラーの順に描画方法を選ぶ
- 触るとき: どの表示方式が選ばれるかを追うとき、表示方式を増やすとき
- 呼び出し先: `this.#renderScrollerRow()`, `this.#renderSmartwindowOverflowRow()`
- 条件付き依存: `if (this.#isGrouped)` → `this.#renderGroupedChips()`
- 参照: `this.#isAutoOverflowing`, `this.#isGrouped`, `this.websites`

## WebsiteChipContainer.render()
- 位置: L222-238
- 役割: サイトが無ければ何も描かず、あれば共通 CSS を読み込んでチップ領域を描く
- 触るとき: コンテナ全体の空表示や読み込む CSS を変えるとき
- 呼び出し先: `html()`, `this.#renderChips()`
- 参照: `this.websites.length`
