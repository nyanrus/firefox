# browser/components/asrouter/content/components/remote-text.js

source: browser/components/asrouter/content/components/remote-text.js
source-hash: 970b7c37f9a93ef4a443c85b8f2b2ad605b67544
lines: 90

## <module>
- 役割: 親ウィンドウの ASRouter 画面で Fluent 文字列を翻訳して表示する remote-text カスタム要素を定義する。
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## MozRemoteText.constructor()
- 位置: L14-19
- 役割: 内容の要素と翻訳の待ち合わせ用 Promise を初期化する。
- 触るとき: 要素の初期状態や翻訳の直列化の前提を変えるとき。
- 呼び出し先: `Promise.resolve()`, `super()`
- 参照: `this._content`, `this._translated`

## MozRemoteText.fluentAttributeValues()
- 位置: L21-37
- 役割: fluent-variable-* 属性を集め、接頭辞を除いた名前の値の辞書を作る。数字で始まる値は整数に変換する。
- 触るとき: Fluent の変数の渡し方や数値の扱いを変えるとき。
- 呼び出し先: `name.startsWith()`, `this.getAttributeNames()`
- 条件付き依存: `if (name.startsWith("fluent-variable-"))` → `this.getAttribute()`
- 条件付き依存: `if (name.startsWith("fluent-variable-"))` → `value.match()`
- 条件付き依存: `if (value.match(/^\d+/))` → `parseInt()`
- 条件付き依存: `if (name.startsWith("fluent-variable-"))` → `name.replace()`

## MozRemoteText.render()
- 位置: L39-52
- 役割: fluent-remote-id と内容要素があれば RemoteL10n で属性を設定し、翻訳を直列に積んでエラーを console に出す。
- 触るとき: 翻訳が反映されない、または順序がずれる問題を調べるとき。
- 呼び出し先: `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `RemoteL10n.l10n.setAttributes()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `this._translated .then(() => RemoteL10n.l10n.translateFragment(this._content)) .catch()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `this._translated .then()`
- 条件付き依存: `if (this.getAttribute("fluent-remote-id") && this._content)` → `RemoteL10n.l10n.translateFragment()`
- 参照: `console.error`, `this._content`, `this._translated`, `this.fluentAttributeValues`

## MozRemoteText.setVariable()
- 位置: L60-63
- 役割: fluent-variable-名 の属性を設定し、render で再翻訳する。
- 触るとき: 表示中の文字列の変数を外から差し替える経路を変えるとき。
- 呼び出し先: `this.render()`, `this.setAttribute()`

## MozRemoteText.observedAttributes()
- 位置: L65-67
- 役割: 値の変化を監視する属性として fluent-remote-id を返す。
- 触るとき: 監視する属性を増やすとき。

## MozRemoteText.attributeChangedCallback()
- 位置: L69-71
- 役割: 監視する属性が変わった時に render を呼ぶ。
- 触るとき: 属性変更で再描画されない問題を調べるとき。
- 呼び出し先: `this.render()`

## MozRemoteText.connectedCallback()
- 位置: L73-85
- 役割: 初めて接続された時に shadow root と内容の span を作って描画する。既にあれば何もしない。
- 触るとき: 要素を取り外して付け直した時の状態保持の挙動を変えるとき。
- 呼び出し先: `document.createElement()`, `shadowRoot.appendChild()`, `this.attachShadow()`, `this.render()`
- 参照: `this._content`, `this.shadowRoot`
