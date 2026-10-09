# browser/components/aiwindow/ui/components/ai-chat-grid/ai-chat-grid.mjs

source: browser/components/aiwindow/ui/components/ai-chat-grid/ai-chat-grid.mjs
source-hash: b5ab5d92bf937972b0e6213d5bad1e040fa9f738
lines: 126

## <module>
- 役割: 項目をグリッド表示と一覧表示で切り替えられる ai-chat-grid 要素を定義する。
- 呼び出し先: `customElements.define()`

## AIChatGrid.showGrid()
- 位置: L21-23
- 役割: 現在の表示が grid かどうかを返す。
- 触るとき: グリッド表示時だけの表示や aria 状態を変えるときに見る。
- 参照: `this.view`

## AIChatGrid.showList()
- 位置: L25-27
- 役割: 現在の表示が list かどうかを返す。
- 触るとき: 一覧表示時だけの表示や aria 状態を変えるときに見る。
- 参照: `this.view`

## AIChatGrid.switchView()
- 位置: L29-31
- 役割: 押されたボタンの id を view に入れて表示を切り替える。
- 触るとき: 切り替えボタンの id を変えるとき、または切り替えても表示が変わらないときに見る。
- 参照: `event.target.id`, `this.view`

## AIChatGrid.renderGridControls()
- 位置: L33-66
- 役割: showSwitch が真のときだけ一覧と grid の切り替えボタン群を描画する。
- 触るとき: 切り替えボタンの見た目や出す条件を変えるときに見る。
- 条件付き依存: `if (this.showSwitch)` → `html()`
- 参照: `this.showGrid`, `this.showList`, `this.showSwitch`, `this.switchView`

## AIChatGrid.renderItems()
- 位置: L68-81
- 役割: items を view に応じて rowItem か gridItem で描画する。
- 触るとき: 表示する項目の並びや描画方法を変えるとき、または項目が表示されないときに見る。
- 呼び出し先: `items.map()`, `this.renderItem()`
- 参照: `this.gridItem`, `this.items`, `this.rowItem`, `this.view`

## AIChatGrid.renderItem()
- 位置: L83-89
- 役割: 渡された描画関数が関数なら項目に適用し、それ以外は何も描画しない。
- 触るとき: 項目の描画関数が未指定のときに何も出ない理由を確認するときに見る。
- 条件付き依存: `if (typeof itemComponent === "function")` → `itemComponent()`

## AIChatGrid.gridStyle()
- 位置: L91-93
- 役割: スクロール領域のクラス名として「scroll-area」と view を並べて返す。
- 触るとき: グリッドのレイアウト用クラスを変えるとき、または CSS が効かないときに見る。
- 参照: `this.view`

## AIChatGrid.renderLoading()
- 位置: L95-103
- 役割: 読み込み中のスケルトン画像を描画する。
- 触るとき: 読み込み中の見た目を変えるとき、またはスケルトンが表示されないときに見る。
- 呼び出し先: `html()`

## AIChatGrid.renderGrid()
- 位置: L105-112
- 役割: 切り替えボタンと項目の入ったスクロール領域を描画する。
- 触るとき: グリッド全体の構造や part 名を変えるとき、または外部スタイルが届かないときに見る。
- 呼び出し先: `html()`, `this.gridStyle()`, `this.renderGridControls()`, `this.renderItems()`
- 参照: `this.view`

## AIChatGrid.render()
- 位置: L114-122
- 役割: 読み込み中ならスケルトン、そうでなければグリッドを描画する。
- 触るとき: 読み込み状態の分岐を変えるとき、または読み込みが終わらない表示を調べるときに見る。
- 呼び出し先: `html()`, `this.renderGrid()`, `this.renderLoading()`
- 参照: `this.loading`
