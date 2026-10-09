# browser/components/aboutlogins/content/components/confirmation-dialog.mjs

source: browser/components/aboutlogins/content/components/confirmation-dialog.mjs
source-hash: 91a9c3a9d74fd59d321331c5445ab65776ce86ea
lines: 106

## <module>
- 役割: about:logins の確認ダイアログ custom element confirmation-dialog を定義する。
- 呼び出し先: `customElements.define()`

## ConfirmationDialog.constructor()
- 位置: L8-11
- 役割: 結果を返すための Promise 変数 _promise を null で初期化する。
- 触るとき: 確認ダイアログの内部状態の初期値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this._promise`

## ConfirmationDialog.connectedCallback()
- 位置: L13-29
- 役割: 初回接続時にテンプレートを shadow DOM に複製し、ボタン・メッセージ・タイトル・オーバーレイの要素参照を保持する。
- 触るとき: テンプレートのクラス名や構造を変えて、参照するセレクタを合わせる必要があるとき。
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `shadowRoot.appendChild()`, `template.content.cloneNode()`, `this.attachShadow()`, `this.shadowRoot.querySelector()`
- 参照: `this._buttons`, `this._cancelButton`, `this._confirmButton`, `this._dismissButton`, `this._message`, `this._overlay`, `this._title`, `this.shadowRoot`

## ConfirmationDialog.handleEvent()
- 位置: L31-55
- 役割: keydown で繰り返し入力を防ぎ Escape で取消す。click はキャンセル系(取消ボタン・閉じるボタン・オーバーレイ)なら onCancel、確定ボタンなら onConfirm を呼ぶ。
- 触るとき: Escape やオーバーレイ押下で確認が取消されない、または誤って確定される問題を調べるとき。
- 呼び出し先: `event.currentTarget.classList.contains()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.repeat)` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape" && !event.defaultPrevented)` → `this.onCancel()`
- 条件付き依存: `if ( event.target.classList.contains("cancel-button") || event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") )` → `this.onCancel()`
- 条件付き依存: `if (!( event.target.classList.contains("cancel-button") || event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") ))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("confirm-button"))` → `this.onConfirm()`
- 参照: `event.defaultPrevented`, `event.key`, `event.repeat`, `event.type`

## ConfirmationDialog.hide()
- 位置: L57-66
- 役割: キーボード操作の制限を解除し、各ボタン・オーバーレイ・window のリスナーを外してから非表示にする。
- 触るとき: ダイアログを閉じた後もリスナーが残ってキー入力を奪う問題を調べるとき。
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._cancelButton.removeEventListener()`, `this._confirmButton.removeEventListener()`, `this._dismissButton.removeEventListener()`, `this._overlay.removeEventListener()`, `window.removeEventListener()`
- 参照: `this.hidden`

## ConfirmationDialog.show()
- 位置: L68-93
- 役割: キーボード操作を無効化し、タイトル・本文・確定ボタンラベルを l10n で設定してからリスナーを登録し、確定ボタンにフォーカスして結果の Promise を返す。
- 触るとき: 削除確認など呼び出し側が await する結果や、表示直後の初期フォーカスを変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`, `setKeyboardAccessForNonDialogElements()`, `this._cancelButton.addEventListener()`, `this._confirmButton.addEventListener()`, `this._confirmButton.focus()`, `this._dismissButton.addEventListener()`, `this._overlay.addEventListener()`, `window.addEventListener()`
- 参照: `this._confirmButton`, `this._message`, `this._promise`, `this._reject`, `this._resolve`, `this._title`, `this.hidden`

## ConfirmationDialog.onCancel()
- 位置: L95-98
- 役割: Promise を reject して dialog を hide する。
- 触るとき: 取消時に呼び出し側へ例外として伝わる挙動を変えるとき。
- 呼び出し先: `this._reject()`, `this.hide()`

## ConfirmationDialog.onConfirm()
- 位置: L100-103
- 役割: Promise を resolve して dialog を hide する。
- 触るとき: 確定時の結果を呼び出し側に返す処理を変えるとき。
- 呼び出し先: `this._resolve()`, `this.hide()`
