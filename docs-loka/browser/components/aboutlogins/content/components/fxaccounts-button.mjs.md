# browser/components/aboutlogins/content/components/fxaccounts-button.mjs

source: browser/components/aboutlogins/content/components/fxaccounts-button.mjs
source-hash: 0217e8a621f3163110d5c5e04a76da3cf4280c20
lines: 80

## <module>
- 役割: about:logins のアカウント(FxA)ボタン fxaccounts-button を定義し、ログイン状態に応じた表示を行う。
- 呼び出し先: `customElements.define()`

## FxAccountsButton.connectedCallback()
- 位置: L6-28
- 役割: 初回接続時にテンプレートを shadow DOM に複製して要素を取得し、有効化ボタンの click を監視してから render する。
- 触るとき: アカウントボタンのテンプレートを変えて参照要素を合わせる必要があるとき。
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `shadowRoot.appendChild()`, `shadowRoot.querySelector()`, `template.content.cloneNode()`, `this._enableButton.addEventListener()`, `this.attachShadow()`, `this.render()`
- 参照: `this._avatarButton`, `this._emailText`, `this._enableButton`, `this._extraText`, `this._loggedInView`, `this._loggedOutView`, `this._manageAccountLink`, `this.shadowRoot`

## FxAccountsButton.handleEvent()
- 位置: L30-38
- 役割: 有効化ボタンが押されたら AboutLoginsSyncEnable を document に発行する。
- 触るとき: Sync 有効化の経路を変えて、受け取る親側(AboutLoginsParent)との接続を確認するとき。
- 条件付き依存: `if (event.target == this._enableButton)` → `document.dispatchEvent()`
- 参照: `event.target`, `this._enableButton`

## FxAccountsButton.render()
- 位置: L40-57
- 役割: ログイン済みか否かで表示を切り替え、メールとアカウント管理リンクを設定し、アバター URL か既定の avatar-color.svg を --avatar-url に入れる。
- 触るとき: ログイン状態ごとの表示内容や既定アバターを変えるとき。
- 呼び出し先: `this._manageAccountLink.setAttribute()`
- 条件付き依存: `if (this._avatarURL)` → `this._avatarButton.style.setProperty()`
- 条件付き依存: `if (!(this._avatarURL))` → `this._avatarButton.style.setProperty()`
- 参照: `this._accountURL`, `this._avatarURL`, `this._email`, `this._emailText.textContent`, `this._loggedIn`, `this._loggedInView.hidden`, `this._loggedOutView.hidden`

## FxAccountsButton.updateState()
- 位置: L69-77
- 役割: state から hidden(fxAccountsEnabled の否定)、ログイン状態・メール・アバター URL・アカウント URL を保持し、render を呼ぶ。
- 触るとき: 親から渡す FxA 状態の項目を増やすとき、または FxA 無効時に隠す条件を変えるとき。
- 呼び出し先: `this.render()`
- 参照: `state.accountURL`, `state.avatarURL`, `state.email`, `state.fxAccountsEnabled`, `state.loggedIn`, `this._accountURL`, `this._avatarURL`, `this._email`, `this._loggedIn`, `this.hidden`
