# browser/components/aiwindow/ui/components/context-icon-button/context-icon-button.mjs

source: browser/components/aiwindow/ui/components/context-icon-button/context-icon-button.mjs
source-hash: 177b1810a6bac01863976436c3dfe6b5d1d04cc6
lines: 65

## <module>
- 役割: スマートバーのコンテキストメニューを開く、アイコン型の context-icon-button カスタム要素を定義するモジュール。
- 呼び出し先: `customElements.define()`

## ContextIconButton.#onMousedown()
- 位置: L28-31
- 役割: mousedown の伝播と既定動作を止め、パネルリストが閉じず検索欄のフォーカスも保たれるようにする。
- 触るとき: メニューボタンを押したときのフォーカス移動やパネルの開閉の挙動を変えるとき。
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`

## ContextIconButton.#onClick()
- 位置: L33-41
- 役割: aiwindow-context-button:on-click を bubbles・composed で発火し、元の click を detail.originalEvent に入れる。
- 触るとき: メニューを開く合図のイベント内容を変えるとき、または親側でこのイベントを受け取れない理由を調べるとき。
- 呼び出し先: `this.dispatchEvent()`

## ContextIconButton.render()
- 位置: L43-61
- 役割: ghost 型の moz-button(プラスアイコン)を描き、disabled と aria-pressed(active のとき true)を反映する。
- 触るとき: ボタンの見た目、無効化の条件、押下状態の表示を変えるとき。
- 呼び出し先: `html()`, `this.#onClick()`, `this.#onMousedown()`
- 参照: `this.active`, `this.disabled`
