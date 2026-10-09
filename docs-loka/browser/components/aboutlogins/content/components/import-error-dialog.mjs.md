# browser/components/aboutlogins/content/components/import-error-dialog.mjs

source: browser/components/aboutlogins/content/components/import-error-dialog.mjs
source-hash: 31ad29512ff28d4201b13270b75a3be685df61f8
lines: 60

## <module>
- 役割: インポート失敗時のエラーダイアログ import-error-dialog を定義する。
- 呼び出し先: `customElements.define()`

## ImportErrorDialog.constructor()
- 位置: L8-31
- 役割: エラー種別ごとの title と description の l10n ID を持つ表を作る(競合値・ファイル形式・権限・読み取り不可の4種)。
- 触るとき: 新しいインポートエラー種別を追加して、対応する文言 ID を登録するとき。
- 呼び出し先: `super()`
- 参照: `this._errorMessages`, `this._errorMessages.CONFLICTING_VALUES_ERROR`, `this._errorMessages.FILE_FORMAT_ERROR`, `this._errorMessages.FILE_PERMISSIONS_ERROR`, `this._errorMessages.UNABLE_TO_READ_ERROR`, `this._promise`

## ImportErrorDialog.connectedCallback()
- 位置: L33-49
- 役割: initDialog で shadow root を作り、エラー文の要素と generic-dialog を取得する。「もう一度インポート」ボタンは dialog を閉じて AboutLoginsImportFromFile を発行する。
- 触るとき: インポート失敗後の再試行の流れを変えるとき。
- 呼び出し先: `document.dispatchEvent()`, `initDialog()`, `shadowRoot.querySelector()`, `this._genericDialog.hide()`, `this.shadowRoot.querySelector()`, `tryImportAgain.addEventListener()`
- 参照: `this._descriptionElement`, `this._focusedElement`, `this._genericDialog`, `this._titleElement`, `this.shadowRoot`

## ImportErrorDialog.show()
- 位置: L51-57
- 役割: 指定種別の title と description を l10n に設定し、generic-dialog を表示して先頭の a 要素にフォーカスを移す。未知の種別では例外になる。
- 触るとき: インポート失敗時に表示する種別と文言の対応を確認するとき。
- 呼び出し先: `document.l10n.setAttributes()`, `this._genericDialog.show()`, `window.AboutLoginsUtils.setFocus()`
- 参照: `this._descriptionElement`, `this._errorMessages`, `this._focusedElement`, `this._titleElement`
