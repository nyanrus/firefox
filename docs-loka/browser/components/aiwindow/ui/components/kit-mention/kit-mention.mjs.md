# browser/components/aiwindow/ui/components/kit-mention/kit-mention.mjs

source: browser/components/aiwindow/ui/components/kit-mention/kit-mention.mjs
source-hash: d47dd8adb1bcd4ead16879c42714c14d82804971
lines: 86

## <module>
- 役割: Kit のアニメーションを一定時間だけ重ねて見せる、イースターエッグ用の kit-mention 要素を定義するモジュール。
- 呼び出し先: `customElements.define()`

## KitMention.constructor()
- 位置: L31-34
- 役割: show を false にして非表示で初期化する。
- 触るとき: 初期状態の表示を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.show`

## KitMention.disconnectedCallback()
- 位置: L36-42
- 役割: 要素が DOM から外れたとき、残っている非表示用のタイマーを止める。
- 触るとき: 要素が外れた後にタイマーが動き続けないよう後始末を変えるとき。
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.#hideTimeoutId !== null)` → `clearTimeout()`
- 参照: `this.#hideTimeoutId`

## KitMention.trigger()
- 位置: L44-57
- 役割: value が MENTION_DEFINITE で、かつその会話 ID でまだ表示していなければ show を true にし、VISIBLE_MS 後に隠すタイマーを張る。
- 触るとき: アニメーションを出す条件や、会話ごとに一度だけに抑える仕組みを変えるとき。
- 呼び出し先: `setTimeout()`
- 参照: `this.#hideTimeoutId`, `this.#shownForConvId`, `this.show`

## KitMention.reset()
- 位置: L59-66
- 役割: 表示済みの会話 ID を忘れ、表示中なら隠してタイマーを止める。
- 触るとき: 新しい会話で再びアニメーションを出したいとき、または前の会話の表示が残るときに確認するとき。
- 条件付き依存: `if (this.#hideTimeoutId !== null)` → `clearTimeout()`
- 参照: `this.#hideTimeoutId`, `this.#shownForConvId`, `this.show`

## KitMention.render()
- 位置: L68-82
- 役割: スタイルシートの link を入れ、show が true のときだけ kit.svg を aria-hidden で描く。
- 触るとき: 表示する画像や支援技術への扱いを変えるとき。
- 呼び出し先: `html()`
- 参照: `this.show`
