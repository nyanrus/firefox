# browser/components/aiwindow/ui/components/ai-sff-tab-selector/ai-sff-tab-selector.mjs

source: browser/components/aiwindow/ui/components/ai-sff-tab-selector/ai-sff-tab-selector.mjs
source-hash: e1b681ddb92693aa0d5f713268b369d3b0ac24f3
lines: 164

## <module>
- 役割: Smart Form Fill で入力元にするタブを選ぶ画面 ai-sff-tab-selector を定義する。
- 呼び出し先: `customElements.define()`

## AiSffTabSelector.constructor()
- 位置: L22-27
- 役割: suggestedTabs と otherTabs を空配列で初期化する。
- 触るとき: 候補タブが届く前の初期表示を変えたいとき。
- 呼び出し先: `super()`
- 参照: `this.otherTabs`, `this.suggestedTabs`

## AiSffTabSelector.#selectedTabIds()
- 位置: L29-33
- 役割: 両方のリストから pressed のタブを集め、その id の配列を返す。
- 触るとき: 選択数の上限判定や、完了時に送るタブ id を変えるとき。
- 呼び出し先: `[...this.suggestedTabs, ...this.otherTabs] .filter()`, `[...this.suggestedTabs, ...this.otherTabs] .filter(tab => tab.pressed) .map()`
- 参照: `tab.id`, `tab.pressed`, `this.otherTabs`, `this.suggestedTabs`

## AiSffTabSelector.#updateTab()
- 位置: L35-37
- 役割: 指定の id のタブだけ pressed を差し替えた新しい配列を返す。
- 触るとき: トグル状態の更新の仕方を変えるとき。
- 呼び出し先: `tabs.map()`
- 参照: `tab.id`

## AiSffTabSelector.#handleTabToggle()
- 位置: L39-44
- 役割: トグルの押下状態を、同じ id のタブを含む両方のリストに反映する。
- 触るとき: 片方のリストだけ選択状態がずれる不具合を調べるとき。
- 呼び出し先: `this.#updateTab()`
- 参照: `event.currentTarget`, `this.otherTabs`, `this.suggestedTabs`

## AiSffTabSelector.#handleAccept()
- 位置: L46-59
- 役割: 選択数が 1 件以上で MAX_SELECTED_TABS 以下のときだけ、id 一覧を付けて tabs-selected を発火する。
- 触るとき: 完了ボタンが押せない、または上限の扱いを変えるとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `selectedTabIds.length`, `this.#selectedTabIds`

## AiSffTabSelector.#handleCancel()
- 位置: L61-68
- 役割: bubbles と composed を付けた cancel イベントを発火する。
- 触るとき: キャンセル後に親が何をするかを追うとき。
- 呼び出し先: `this.dispatchEvent()`

## AiSffTabSelector.#renderTabList()
- 位置: L70-110
- 役割: 見出しと、各タブのトグル付きリストを描画する。scrollable のときは別のクラスを付け、上限到達時は未選択のトグルを無効にする。
- 触るとき: タブ一覧の見た目や、選択上限に達したときの無効化条件を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#handleTabToggle()`
- 参照: `tab.favicon`, `tab.id`, `tab.pressed`, `tab.title`, `tab.url`

## AiSffTabSelector.render()
- 位置: L112-160
- 役割: 選択数を数え、タイトル、候補とその他の一覧(空なら非表示)、キャンセルと完了のボタンを描画する。完了は 0 件か上限超えで無効。
- 触るとき: 完了ボタンの有効条件や、一覧の出し分けを変えるとき。
- 呼び出し先: `html()`, `this.#renderTabList()`
- 参照: `this.#handleAccept`, `this.#handleCancel`, `this.#selectedTabIds.length`, `this.otherTabs`, `this.otherTabs?.length`, `this.suggestedTabs`, `this.suggestedTabs?.length`
