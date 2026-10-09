# browser/components/aboutlogins/content/components/login-intro.mjs

source: browser/components/aboutlogins/content/components/login-intro.mjs
source-hash: bebc7eadffdf782ed53dc24abf2368908edac13a
lines: 65

## <module>
- 役割: about:logins の導入画面 login-intro を定義し、同期状態に応じた見出し・ヘルプリンク・インポート導線を表示する。
- 呼び出し先: `customElements.define()`

## LoginIntro.connectedCallback()
- 位置: L6-15
- 役割: 初回接続時にテンプレートを shadow DOM に複製し、l10n に接続する。
- 触るとき: 導入画面のテンプレートを変えるとき。
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `loginIntroTemplate.content.cloneNode()`, `shadowRoot.appendChild()`, `this.attachShadow()`
- 参照: `this.shadowRoot`

## LoginIntro.focus()
- 位置: L17-20
- 役割: ヘルプリンクにフォーカスを移す。
- 触るとき: about:logins の初期フォーカス先を変えるとき。
- 呼び出し先: `helpLink.focus()`, `this.shadowRoot.querySelector()`

## LoginIntro.handleEvent()
- 位置: L22-38
- 役割: インポート文内のリンクのクリックを、data-l10n-name が import-file-link なら AboutLoginsImportFromFile、それ以外なら AboutLoginsImportFromBrowser に変換して document に発行する。どのクリックでも既定動作を止める。
- 触るとき: インポート導線のリンクを増やすとき、またはリンクの遷移が効かなくなった問題を調べるとき。
- 呼び出し先: `event.currentTarget.classList.contains()`, `event.preventDefault()`
- 条件付き依存: `if ( event.currentTarget.classList.contains("intro-import-text") && event.target.localName == "a" )` → `document.dispatchEvent()`
- 参照: `event.target.dataset.l10nName`, `event.target.localName`

## LoginIntro.updateState()
- 位置: L40-62
- 役割: 見出しの l10n を設定し、同期済みならイラストに logged-in を付け、ヘルプリンク先を support URL に設定する。ファイルインポート項目はクリックを監視し、importVisible に応じて表示を切り替える。
- 触るとき: 同期状態で導入画面の見た目やヘルプ URL を変えるとき、またはインポート導線の表示条件を変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`, `importText.addEventListener()`, `this.shadowRoot .querySelector()`, `this.shadowRoot .querySelector(".illustration") .classList.toggle()`, `this.shadowRoot .querySelector(".intro-help-link") .setAttribute()`, `this.shadowRoot.querySelector()`
- 参照: `importText.hidden`, `syncState.loggedIn`, `window.AboutLoginsUtils.importVisible`, `window.AboutLoginsUtils.supportBaseURL`
