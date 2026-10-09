# browser/components/aboutlogins/content/components/generic-dialog.mjs

source: browser/components/aboutlogins/content/components/generic-dialog.mjs
source-hash: 8d9ddc9d36c19b9f6580b01309707e05da42d73c
lines: 64

## <module>
- 役割: about:logins の汎用ダイアログ generic-dialog を定義する。閉じるボタン・オーバーレイ・Escape で閉じる。
- 呼び出し先: `customElements.define()`

## GenericDialog.constructor()
- 位置: L11-14
- 役割: _promise を null で初期化する。
- 触るとき: ダイアログ生成直後の状態を見直すとき(このファイル内で _promise は他に参照されない)。
- 呼び出し先: `super()`
- 参照: `this._promise`

## GenericDialog.connectedCallback()
- 位置: L16-23
- 役割: initDialog で shadow root を作り、ライト DOM の閉じるボタンと shadow 内のオーバーレイを取得する。
- 触るとき: 閉じるボタンのクラス名や配置を変えて、取得先を合わせる必要があるとき。
- 呼び出し先: `initDialog()`, `shadowRoot.querySelector()`, `this.querySelector()`
- 参照: `this._dismissButton`, `this._overlay`, `this.shadowRoot`

## GenericDialog.handleEvent()
- 位置: L25-40
- 役割: Escape キーと、閉じるボタンまたはオーバーレイのクリックで hide を呼ぶ。
- 触るとき: ダイアログが閉じない、または意図せず閉じる問題を調べるとき。
- 呼び出し先: `event.currentTarget.classList.contains()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.key === "Escape" && !event.defaultPrevented)` → `this.hide()`
- 条件付き依存: `if ( event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") )` → `this.hide()`
- 参照: `event.defaultPrevented`, `event.key`, `event.type`

## GenericDialog.show()
- 位置: L42-50
- 役割: キーボード操作を無効化し、自身と親 host の hidden を解除してから、閉じるボタン・オーバーレイ・window にリスナーを登録する。
- 触るとき: ダイアログ表示時に親要素の表示状態が連動しない問題を調べるとき。
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._dismissButton.addEventListener()`, `this._overlay.addEventListener()`, `window.addEventListener()`
- 参照: `this.hidden`, `this.parentNode.host.hidden`

## GenericDialog.hide()
- 位置: L52-60
- 役割: キーボード操作を戻し、リスナーを外してから自身と親 host を非表示にする。
- 触るとき: ダイアログを閉じた後に親 host が残る、またはフォーカスが戻らない問題を調べるとき。
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._dismissButton.removeEventListener()`, `this._overlay.removeEventListener()`, `window.removeEventListener()`
- 参照: `this.hidden`, `this.parentNode.host.hidden`
