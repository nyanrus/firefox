# browser/components/aboutlogins/content/components/import-summary-dialog.mjs

source: browser/components/aboutlogins/content/components/import-summary-dialog.mjs
source-hash: 3b8433852759bcd4a94d7b38c89bc996796e0dc9
lines: 73

## <module>
- 役割: インポート結果の件数サマリーダイアログ import-summary-dialog を定義する。
- 呼び出し先: `customElements.define()`

## ImportSummaryDialog.constructor()
- 位置: L8-11
- 役割: _promise を null で初期化する。
- 触るとき: ダイアログ生成直後の状態を見直すとき(このファイル内で _promise は他に参照されない)。
- 呼び出し先: `super()`
- 参照: `this._promise`

## ImportSummaryDialog.connectedCallback()
- 位置: L13-23
- 役割: initDialog で shadow root を作り、追加・変更・変更なし・エラーの各件数表示要素と generic-dialog を取得する。
- 触るとき: 件数表示欄のクラス名をテンプレートで変えたとき。
- 呼び出し先: `initDialog()`, `this.shadowRoot.querySelector()`
- 参照: `this._added`, `this._error`, `this._genericDialog`, `this._modified`, `this._noChange`, `this.shadowRoot`

## ImportSummaryDialog.show()
- 位置: L25-64
- 役割: logins の result を追加・変更・変更なし・エラー(文字列に error を含む)に数え、各件数を l10n に反映する。変更なしとエラーは件数が 0 なら注記を隠し、ダイアログを表示して閉じるボタンにフォーカスする。
- 触るとき: インポート結果の数え方や注記の表示条件を変えるとき。
- 呼び出し先: `loginRow.result.includes()`, `this._error.querySelector()`, `this._genericDialog.show()`, `this._noChange.querySelector()`, `this._updateCount()`, `window.AboutLoginsUtils.setFocus()`
- 参照: `loginRow.result`, `report.added`, `report.error`, `report.modified`, `report.no_change`, `this._added`, `this._error`, `this._error.querySelector(".result-meta").hidden`, `this._genericDialog._dismissButton`, `this._modified`, `this._noChange`, `this._noChange.querySelector(".result-meta").hidden`

## ImportSummaryDialog._updateCount()
- 位置: L66-70
- 役割: 件数が現在の count 引数と違うときだけ l10n の属性を更新する。
- 触るとき: 件数表示の再描画条件を見直すとき。
- 呼び出し先: `document.l10n.getAttributes()`
- 条件付き依存: `if (count != document.l10n.getAttributes(component).args.count)` → `document.l10n.setAttributes()`
- 参照: `document.l10n.getAttributes(component).args.count`
