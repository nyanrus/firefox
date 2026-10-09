# browser/components/customizableui/content/sync-promo.mjs

source: browser/components/customizableui/content/sync-promo.mjs
source-hash: ab21f695c6812105fad6418242c7706d99f6d044
lines: 184

## <module>
- 役割: アプリメニューの履歴・ブックマーク画面に出す、Sync 導入を促す閉じられるプロモ（sync-promo 要素）を定義・描画する。
- 呼び出し先: `customElements.define()`, `window.MozXULElement?.insertFTLIfNeeded()`

## SyncPromo.constructor()
- 位置: L74-79
- 役割: 既定の promoType を history にし、表示状態を null に初期化する。disconnectedCallback を this に束縛する。
- 触るとき: プロモの初期状態や unload 時の解除処理の束縛を変えるとき。
- 呼び出し先: `super()`, `this.disconnectedCallback.bind()`
- 参照: `this._promoState`, `this.disconnectedCallback`, `this.promoType`

## SyncPromo.#onViewShowing()
- 位置: L82-82
- 役割: 親の panelview が表示されるたびに状態を再評価する。
- 触るとき: パネル再表示時にプロモが古い状態のまま残る問題を調べるとき。
- 呼び出し先: `this.#refresh()`

## observe()
- 位置: L85-85
- 役割: Sync の状態更新・デバイス一覧更新・dismiss 用 pref の変化を受けて再評価する observer。
- 触るとき: どの通知で表示状態を更新するかを変えるとき。
- 呼び出し先: `this.#refresh()`

## SyncPromo.#dismissedPrefBranch()
- 位置: L87-89
- 役割: promoType ごとの dismiss 用 pref のブランチ名を返す。
- 触るとき: 閉じた状態の保存先 pref 名を変えるとき。
- 参照: `this.promoType`

## SyncPromo.connectedCallback()
- 位置: L91-104
- 役割: 通知と pref の監視を登録し、親 panelview の ViewShowing と unload を結びつけて、すぐ一度状態を更新する。
- 触るとき: プロモが DOM に入ったときの購読処理や、表示更新のきっかけを変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `super.connectedCallback()`, `this.#panelview?.addEventListener()`, `this.#refresh()`, `this.closest()`, `window.addEventListener()`
- 参照: `this.#dismissedPrefBranch`, `this.#observer`, `this.#onViewShowing`, `this.#panelview`, `this.disconnectedCallback`
- XPCOM: `Services.obs` / `Services.prefs`

## SyncPromo.disconnectedCallback()
- 位置: L106-114
- 役割: connectedCallback で登録した通知・pref・イベントの購読をすべて解除する。
- 触るとき: プロモの破棄時にリスナーが残ってリークする問題を調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `super.disconnectedCallback()`, `this.#panelview?.removeEventListener()`, `window.removeEventListener()`
- 参照: `this.#dismissedPrefBranch`, `this.#observer`, `this.#onViewShowing`, `this.#panelview`, `this.disconnectedCallback`
- XPCOM: `Services.obs` / `Services.prefs`

## SyncPromo.#config()
- 位置: L116-118
- 役割: promoType に対応する PROMO_CONFIG の設定（導線と文言の一式）を返す。
- 触るとき: 新しいプロモの種類を追加したり、導線の名前を変えたりするとき。
- 参照: `this.promoType`

## SyncPromo.#dismissedPref()
- 位置: L120-122
- 役割: 状態名から、その状態が閉じられたかを示す pref 名を組み立てる。
- 触るとき: 閉じた状態ごとの保存キーの形式を変えるとき。
- 参照: `this.#dismissedPrefBranch`

## SyncPromo.#refresh()
- 位置: L124-134
- 役割: gSync から現在の Sync プロモ状態を取り、閉じられていれば null にして、表示状態と hidden を更新する。
- 触るとき: どの状態で何を出すか、閉じた後にどう隠すかを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.#dismissedPref()`, `window.gSync?.getSyncPromoState()`
- 参照: `this._promoState`, `this.hidden`
- XPCOM: `Services.prefs`

## SyncPromo.#onDismiss()
- 位置: L136-140
- 役割: 閉じられたときに現在の状態の dismiss pref を true にして、再評価する。
- 触るとき: 閉じるボタンの保存の挙動を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.preventDefault()`, `this.#dismissedPref()`, `this.#refresh()`
- 参照: `this._promoState`
- XPCOM: `Services.prefs`

## SyncPromo.#onCta()
- 位置: L142-151
- 役割: CTA クリックで gSync.handleSyncPromoAction を呼び、続けて所属するパネルを閉じる。
- 触るとき: CTA の遷移先やパネルを閉じるタイミングを変えるとき。
- 呼び出し先: `event.preventDefault()`, `window.CustomizableUI.hidePanelForNode()`, `window.gSync.handleSyncPromoAction()`
- 参照: `this.#config.entryPoint`, `this._promoState`

## SyncPromo.render()
- 位置: L153-181
- 役割: 状態に対応する見出し・CTA・画像を持つ moz-promo を描画する。状態がなければ何も描かない。
- 触るとき: プロモの見た目や CTA の結び付けを変えるとき。
- 呼び出し先: `html()`
- 参照: `this.#config.variants`, `this.#onCta`, `this.#onDismiss`, `this._promoState`, `variant.cta`, `variant.heading`, `variant.image`
