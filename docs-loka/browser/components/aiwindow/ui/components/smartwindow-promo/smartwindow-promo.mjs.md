# browser/components/aiwindow/ui/components/smartwindow-promo/smartwindow-promo.mjs

source: browser/components/aiwindow/ui/components/smartwindow-promo/smartwindow-promo.mjs
source-hash: b21c326a5696c2f0c0dc9be037cd1a7d473ebe1b
lines: 134

## <module>
- 役割: AI Window 内に出す販促メッセージ(asrouter 由来)の smartwindow-promo を定義するモジュール。
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.freeze()`, `customElements.define()`

## SmartwindowPromo.#onVisibilityChange()
- 位置: L36-36
- 役割: 文書が表示状態になったときに impression の記録を試みる。
- 触るとき: 表示回数の記録のタイミングを変えるとき。
- 呼び出し先: `this.#maybeFireImpression()`

## SmartwindowPromo.constructor()
- 位置: L38-41
- 役割: message を null で初期化する。
- 触るとき: メッセージ未設定時の既定の表示を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.message`

## SmartwindowPromo.connectedCallback()
- 位置: L43-51
- 役割: 接続時にすぐ impression を記録できなければ、visibilitychange で再試行するリスナーを登録する。
- 触るとき: 表示回数の記録を遅らせる条件を変えるとき。
- 呼び出し先: `super.connectedCallback()`, `this.#maybeFireImpression()`
- 条件付き依存: `if (!this.#maybeFireImpression())` → `this.ownerDocument.addEventListener()`
- 参照: `this.#onVisibilityChange`

## SmartwindowPromo.disconnectedCallback()
- 位置: L53-59
- 役割: 切断時に visibilitychange のリスナーを外す。
- 触るとき: 要素を外したときのリスナー解除を変えるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.ownerDocument.removeEventListener()`
- 参照: `this.#onVisibilityChange`

## SmartwindowPromo.#maybeFireImpression()
- 位置: L61-75
- 役割: 未記録で文書が表示中なら、リスナーを外して IMPRESSION を一度だけ発火する。記録済みかどうかを返す。
- 触るとき: 表示回数の記録条件や二重記録の防止を変えるとき。
- 呼び出し先: `this.#dispatch()`, `this.ownerDocument.removeEventListener()`
- 参照: `SMARTWINDOW_PROMO_EVENTS.IMPRESSION`, `this.#impressionFired`, `this.#onVisibilityChange`, `this.ownerDocument.visibilityState`

## SmartwindowPromo.#dispatch()
- 位置: L77-81
- 役割: 指定した型のイベントをバブルさせ composed で発火する。
- 触るとき: promo から親へ送るイベントの扱いを変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowPromo.#handlePrimary()
- 位置: L83-83
- 役割: PRIMARY イベントを発火する。
- 触るとき: 主ボタンを押したときの通知を変えるとき。
- 呼び出し先: `this.#dispatch()`
- 参照: `SMARTWINDOW_PROMO_EVENTS.PRIMARY`

## SmartwindowPromo.#handleClose()
- 位置: L84-84
- 役割: CLOSE イベントを発火する。
- 触るとき: 副ボタンを押したときの通知を変えるとき。
- 呼び出し先: `this.#dispatch()`
- 参照: `SMARTWINDOW_PROMO_EVENTS.CLOSE`

## SmartwindowPromo.#handleDismiss()
- 位置: L85-89
- 役割: moz-promo の既定の削除を止め、DISMISS イベントを発火する。
- 触るとき: promo を閉じたときの後始末や削除の扱いを変えるとき。
- 呼び出し先: `event.preventDefault()`, `this.#dispatch()`
- 参照: `SMARTWINDOW_PROMO_EVENTS.DISMISS`

## SmartwindowPromo.render()
- 位置: L91-130
- 役割: メッセージから moz-promo の種類・見出し・本文・画像の属性を設定し、副ボタンと主ボタンを actions スロットに入れて描く。
- 触るとき: 販促の見た目、画像の配置、ボタン構成を変えるとき。
- 呼び出し先: `html()`
- 参照: `content.dismissable`, `content.heading`, `content.imageAlignment`, `content.imageDisplay`, `content.imageSrc`, `content.imageWidth`, `content.message`, `content.primaryActionText`, `content.secondaryActionText`, `content.type`, `this.#handleClose`, `this.#handleDismiss`, `this.#handlePrimary`, `this.message`
