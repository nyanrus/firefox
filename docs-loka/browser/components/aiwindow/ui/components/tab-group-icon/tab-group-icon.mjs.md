# browser/components/aiwindow/ui/components/tab-group-icon/tab-group-icon.mjs

source: browser/components/aiwindow/ui/components/tab-group-icon/tab-group-icon.mjs
source-hash: e749da7167d6a31fea8c567e5d772454e1490da4
lines: 60

## <module>
- 役割: タブグループ名の頭文字を色付きの箱で示す tab-group-icon 要素を定義する
- 呼び出し先: `customElements.define()`

## TabGroupIcon.constructor()
- 位置: L23-27
- 役割: label と color を空文字で初期化する
- 触るとき: 未指定時の既定の見た目を調べるとき
- 呼び出し先: `super()`
- 参照: `this.color`, `this.label`

## TabGroupIcon.willUpdate()
- 位置: L29-41
- 役割: color が変わったとき --tab-group-color と --tab-group-text-color を自要素の style に設定する(未指定は gray)
- 触るとき: 色トークンの対応や、色が反映されない問題を調べるとき
- 呼び出し先: `changedProperties.has()`, `this.style.setProperty()`
- 参照: `this.color`

## TabGroupIcon.#initial()
- 位置: L44-46
- 役割: label の前後空白を除き、先頭の 1 文字(サロゲート対応)を大文字にして返す
- 触るとき: 表示される文字の決め方(空の場合や絵文字の扱い)を変えるとき
- 呼び出し先: `(Array.from(this.label?.trim() ?? "")[0] ?? "").toUpperCase()`, `Array.from()`, `this.label?.trim()`

## TabGroupIcon.render()
- 位置: L48-56
- 役割: タブグループ名の頭文字を aria-hidden の span として描く
- 触るとき: アイコンの DOM 構造や支援技術向けの隠し方を変えるとき
- 呼び出し先: `html()`
- 参照: `this.#initial`
