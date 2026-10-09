# browser/components/aboutlogins/content/components/login-filter.mjs

source: browser/components/aboutlogins/content/components/login-filter.mjs
source-hash: 157dbe1d65062867b6809f68891c792e60fc9799
lines: 100

## <module>
- 役割: about:logins の検索欄 login-filter を定義し、入力に応じて一覧を絞り込むイベントを発行する。
- 呼び出し先: `customElements.define()`

## LoginFilter.#loginList()
- 位置: L8-10
- 役割: document から login-list 要素を取得する。
- 触るとき: 一覧要素の取得方法を変えるとき。
- 呼び出し先: `document.querySelector()`

## LoginFilter.connectedCallback()
- 位置: L12-27
- 役割: 初回接続時にテンプレートを shadow DOM に複製し、入力欄を取得して input・keydown と AboutLoginsFilterLogins のリスナーを登録する。
- 触るとき: 検索欄のテンプレートや、外部から絞り込みを受け取る経路を変えるとき。
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginFilterTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `this._input.addEventListener()`, `this.addEventListener()`, `this.attachShadow()`, `this.shadowRoot.querySelector()`, `window.addEventListener()`
- 参照: `this._input`, `this.shadowRoot`

## LoginFilter.focus()
- 位置: L29-31
- 役割: 入力欄にフォーカスを移す。
- 触るとき: about:logins の初期フォーカスや検索欄へのフォーカス移動を変えるとき。
- 呼び出し先: `this._input.focus()`

## LoginFilter.handleEvent()
- 位置: L33-45
- 役割: AboutLoginsFilterLogins では入力欄の値を更新し、input では入力値で絞り込みを発行し、keydown ではキー操作を処理する。
- 触るとき: 検索欄のイベント処理の振り分けを変えるとき。
- 呼び出し先: `this.#filterLogins()`, `this.#input()`, `this.#keyDown()`
- 参照: `event.detail`, `event.originalTarget.value`, `event.type`

## LoginFilter.#filterLogins()
- 位置: L47-51
- 役割: 受け取った文字列が現在の値と違うときだけ入力欄の値を更新する。
- 触るとき: 外部からの絞り込み指示を反映する条件を変えるとき。
- 参照: `this.value`

## LoginFilter.#input()
- 位置: L53-55
- 役割: 入力値を受けて絞り込みイベントを発行する。
- 触るとき: 入力に対する絞り込みのトリガーを変えるとき。
- 呼び出し先: `this._dispatchFilterEvent()`

## LoginFilter.#keyDown()
- 位置: L57-76
- 役割: 上下キーで一覧の前後を選択し、Escape で入力を空にし、Enter で選択中の項目を実行する。いずれも既定動作を止める。
- 触るとき: 検索欄のキーボード操作を増やしたり、一覧との連携を変えるとき。
- 呼び出し先: `e.preventDefault()`, `this.#loginList.clickSelected()`, `this.#loginList.selectNext()`, `this.#loginList.selectPrevious()`
- 参照: `e.code`, `this.value`

## LoginFilter.value()
- 位置: L78-80
- 役割: 入力欄の現在の値を返す(getter)。
- 触るとき: 検索欄の値を外から読む箇所を変えるとき。
- 参照: `this._input.value`

## LoginFilter.value()
- 位置: L82-85
- 役割: 入力欄に値を設定し、その値で絞り込みイベントを発行する(setter)。
- 触るとき: 検索欄の値をプログラムから設定する箇所を変えるとき。
- 呼び出し先: `this._dispatchFilterEvent()`
- 参照: `this._input.value`

## LoginFilter._dispatchFilterEvent()
- 位置: L87-97
- 役割: AboutLoginsFilterLogins を値付きで発行し、filterList のテレメトリを記録する。
- 触るとき: 絞り込みイベントの形式や記録されるテレメトリを変えるとき。
- 呼び出し先: `recordTelemetryEvent()`, `this.dispatchEvent()`
