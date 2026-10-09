# browser/components/aiwindow/ui/components/ai-grouped-chip-container/ai-grouped-chip-container.mjs

source: browser/components/aiwindow/ui/components/ai-grouped-chip-container/ai-grouped-chip-container.mjs
source-hash: 8517b9e1506f92a43d2f8e815a95dee3a8fb9d1a
lines: 139

## <module>
- 役割: チャット内で3件以上のチップを1つのボタンにまとめ、クリックで一覧パネルを開く ai-grouped-chip-container を定義する。
- 呼び出し先: `customElements.define()`

## AIGroupedChipContainer.constructor()
- 位置: L25-30
- 役割: chips を空配列、openLinkEvent を AIChatContent:OpenLink、isPanelOpen を false にする。
- 触るとき: リンクを開くイベント名の既定値を変えたいとき、またはホストが別のイベント名を渡す経路を調べるとき。
- 呼び出し先: `super()`
- 参照: `this.chips`, `this.isPanelOpen`, `this.openLinkEvent`

## AIGroupedChipContainer.#onTriggerMousedown()
- 位置: L35-37
- 役割: トリガーの mousedown の伝播を止め、パネルのドキュメント全体のライトディスミスに届かないようにする。
- 触るとき: クリックでパネルが一度閉じてすぐ開き直る(ちらつく)不具合を調べるとき。
- 呼び出し先: `event.stopPropagation()`

## AIGroupedChipContainer.#toggleGroupedPanel()
- 位置: L39-43
- 役割: クリックされたボタンをパネルのアンカーに設定してから、パネルの toggle を呼ぶ。
- 触るとき: パネルの出る位置や開閉の契機を変えるとき。
- 呼び出し先: `panel.toggle()`, `this.shadowRoot.querySelector()`
- 参照: `event.currentTarget`, `panel.anchor`

## AIGroupedChipContainer.#closeGroupedPanel()
- 位置: L45-47
- 役割: パネルがあれば hide を呼んで閉じる。
- 触るとき: 項目選択後などにパネルが閉じない、または閉じる経路を追うとき。
- 呼び出し先: `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector("smartwindow-panel-list")?.hide()`

## AIGroupedChipContainer.#onItemSelected()
- 位置: L49-61
- 役割: 選ばれた項目の id(URL)があれば openLinkEvent を bubbles/composed で発火し(preferSwitchToTab: true)、そのあとパネルを閉じる。
- 触るとき: 項目を選んでもリンクが開かない、または既存タブへの切り替え挙動を変えるとき。
- 呼び出し先: `this.#closeGroupedPanel()`
- 条件付き依存: `if (url)` → `this.dispatchEvent()`
- 参照: `event.detail?.id`, `this.openLinkEvent`

## AIGroupedChipContainer.#renderStackedIcon()
- 位置: L64-81
- 役割: タブグループなら tab-group-icon を、それ以外はファビコンの img を返す。読み込み失敗時は既定のファビコンに差し替える。
- 触るとき: 重ねアイコンの見た目や、タブグループと URL の描き分けを変えるとき。
- 呼び出し先: `html()`
- 条件付き依存: `if (chip.type == CONTEXT_MENTION_TYPE.TAB_GROUP)` → `html()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `chip.color`, `chip.iconSrc`, `chip.label`, `chip.type`, `e.target.src`

## AIGroupedChipContainer.render()
- 位置: L83-135
- 役割: chips をパネルのグループ形式に変換し、トリガーボタン(重ねアイコン、件数ラベル、矢印)と smartwindow-panel-list を描画する。
- 触るとき: 件数表示や、パネルに渡す項目(id、label、icon、color)の中身を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#onItemSelected()`, `this.#onTriggerMousedown()`, `this.#renderStackedIcon()`, `this.#toggleGroupedPanel()`, `this.chips.map()`
- 参照: `chip.groupId`, `chip.url`, `this.chips`, `this.chips.length`, `this.isPanelOpen`, `w.color`, `w.iconSrc`, `w.label`, `w.type`, `w.url`
