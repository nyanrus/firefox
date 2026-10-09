# browser/components/aboutlogins/content/components/remove-logins-dialog.mjs

source: browser/components/aboutlogins/content/components/remove-logins-dialog.mjs
source-hash: 94cd6ef13e678cf6c9ac6ad117a56b1f2731f0f8
lines: 118

## <module>
- 役割: ログイン削除の確認ダイアログ(remove-logins-dialog 要素)を定義し、確認チェックボックスが付いた Promise で結果を返す
- 呼び出し先: `customElements.define()`

## RemoveLoginsDialog.constructor()
- 位置: L8-11
- 役割: 保留中の Promise を null で初期化する
- 触るとき: ダイアログの内部状態を増やすとき
- 呼び出し先: `super()`
- 参照: `this._promise`

## RemoveLoginsDialog.connectedCallback()
- 位置: L13-31
- 役割: テンプレートから shadow DOM を組み立て、ボタン、メッセージ、チェックボックスの参照を取る
- 触るとき: ダイアログ内の要素を追加・改名したとき
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `shadowRoot.appendChild()`, `template.content.cloneNode()`, `this.attachShadow()`, `this.shadowRoot.querySelector()`
- 参照: `this._buttons`, `this._cancelButton`, `this._checkbox`, `this._checkboxLabel`, `this._confirmButton`, `this._dismissButton`, `this._message`, `this._overlay`, `this._title`, `this.shadowRoot`

## RemoveLoginsDialog.handleEvent()
- 位置: L33-53
- 役割: Escape とキャンセル系の操作で取り消し、確定ボタンで確定、チェックボックスで確定ボタンの有効無効を切り替える
- 触るとき: 削除の確定条件や取り消しの経路を変えるとき。確定はチェックを入れた後にだけ可能
- 呼び出し先: `event.currentTarget.classList.contains()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.key === "Escape" && !event.defaultPrevented)` → `this.onCancel()`
- 条件付き依存: `if ( event.target.classList.contains("cancel-button") || event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") )` → `this.onCancel()`
- 条件付き依存: `if (!( event.target.classList.contains("cancel-button") || event.currentTarget.classList.contains("dismiss-button") || event.target.classList.contains("overlay") ))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("confirm-button"))` → `this.onConfirm()`
- 条件付き依存: `if (!(event.target.classList.contains("confirm-button")))` → `event.target.classList.contains()`
- 参照: `event.defaultPrevented`, `event.key`, `event.type`, `this._checkbox.checked`, `this._confirmButton.disabled`

## RemoveLoginsDialog.hide()
- 位置: L55-67
- 役割: キー・クリックの監視を外し、チェックを外して非表示にする。キーボード操作を再び有効にする
- 触るとき: ダイアログを閉じた後にリスナーや状態が残る不具合を調べるとき
- 呼び出し先: `setKeyboardAccessForNonDialogElements()`, `this._cancelButton.removeEventListener()`, `this._checkbox.removeEventListener()`, `this._confirmButton.removeEventListener()`, `this._dismissButton.removeEventListener()`, `this._overlay.removeEventListener()`, `window.removeEventListener()`
- 参照: `this._checkbox.checked`, `this.hidden`

## RemoveLoginsDialog.show()
- 位置: L69-104
- 役割: 件数入りで見出し、本文、ボタン、チェック文言を設定し、監視を付け、確定を無効にしてチェックボックスへフォーカスし、結果の Promise を返す
- 触るとき: 削除確認の文言や初期フォーカスを変えるとき。Promise は確定で resolve、取り消しで reject される
- 呼び出し先: `document.l10n.setAttributes()`, `setKeyboardAccessForNonDialogElements()`, `this._cancelButton.addEventListener()`, `this._checkbox.addEventListener()`, `this._checkbox.focus()`, `this._confirmButton.addEventListener()`, `this._dismissButton.addEventListener()`, `this._overlay.addEventListener()`, `window.addEventListener()`
- 参照: `this._checkboxLabel`, `this._confirmButton`, `this._confirmButton.disabled`, `this._message`, `this._promise`, `this._reject`, `this._resolve`, `this._title`, `this.hidden`

## RemoveLoginsDialog.onCancel()
- 位置: L106-109
- 役割: Promise を reject して閉じる
- 触るとき: 取り消し時の後続処理(呼び出し元の catch 側)を調べるとき
- 呼び出し先: `this._reject()`, `this.hide()`

## RemoveLoginsDialog.onConfirm()
- 位置: L111-114
- 役割: Promise を resolve して閉じる
- 触るとき: 削除確定後の後続処理を変えるとき
- 呼び出し先: `this._resolve()`, `this.hide()`
