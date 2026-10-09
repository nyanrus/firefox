# browser/components/aiwindow/ui/components/memories-icon-button/memories-icon-button.mjs

source: browser/components/aiwindow/ui/components/memories-icon-button/memories-icon-button.mjs
source-hash: b5ac24e361ac56aeea60f389697ed150304c20ad
lines: 80

## <module>
- 役割: AI Memories の有効・無効を切り替えるアイコン型ボタン memories-icon-button を定義するモジュール。
- 呼び出し先: `customElements.define()`

## MemoriesIconButton.#onClick()
- 位置: L28-37
- 役割: pressed を反転させ、新しい値を入れた aiwindow-memories-toggle:on-change を発火する。
- 触るとき: 記憶の on/off の通知内容を変えるとき、または親がこの切り替えを受け取れない理由を調べるとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.pressed`

## MemoriesIconButton.willUpdate()
- 位置: L39-41
- 役割: show が false のとき hidden 属性を付けて要素を隠す。
- 触るとき: ボタンを表示する条件(show)の扱いを変えるとき。
- 呼び出し先: `this.toggleAttribute()`
- 参照: `this.show`

## MemoriesIconButton.render()
- 位置: L43-76
- 役割: show が false なら何も描かず、true なら pressed に応じたアイコンとツールチップの ID で moz-button を描き、aria-pressed を付ける。
- 触るとき: 記憶ボタンの見た目、アイコン、ツールチップ、無効化の条件を変えるとき。
- 呼び出し先: `String()`, `html()`, `this.#onClick()`
- 参照: `this.disabled`, `this.pressed`, `this.show`
