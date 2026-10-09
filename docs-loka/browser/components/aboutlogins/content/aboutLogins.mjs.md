# browser/components/aboutlogins/content/aboutLogins.mjs

source: browser/components/aboutlogins/content/aboutLogins.mjs
source-hash: afab4e6ff2137a05e1321712fc03b3e4bb034ae0
lines: 298

## <module>
- 役割: about:logins のメイン画面の初期化とイベント振り分けを行う。親からの各メッセージで一覧・詳細・同期状態を更新し、確認ダイアログを開き、読み込み時に検索パラメータを整えて検索欄に反映する。
- 呼び出し先: `dialog.show()`, `dialogPromise.then()`, `document .querySelector()`, `document .querySelector("login-list") .shadowRoot.querySelector()`, `document.dispatchEvent()`, `document.documentElement.classList.add()`, `document.documentElement.classList.remove()`, `document.querySelector()`, `gElements.loginItem.loginAdded()`, `gElements.loginItem.loginModified()`, `gElements.loginItem.loginRemoved()`, `gElements.loginItem.setBreaches()`, `gElements.loginItem.setChangePasswordURLs()`, `gElements.loginItem.setVulnerableLogins()`, `gElements.loginItem.showLoginItemError()`, `gElements.loginItem.updateBreaches()`, `gElements.loginItem.updateVulnerableLogins()`, `gElements.loginList.classList.add()`, `gElements.loginList.loginAdded()`, `gElements.loginList.loginModified()`, `gElements.loginList.loginRemoved()`, `gElements.loginList.selectLoginByDomainOrGuid()`, `gElements.loginList.setBreaches()`, `gElements.loginList.setChangePasswordURLs()`, `gElements.loginList.setSortDirection()`, `gElements.loginList.setVulnerableLogins()`, `gElements.loginList.updateBreaches()`, `gElements.loginList.updateVulnerableLogins()`, `handleAllLogins()`, `handleSyncState()`, `interceptFocusKey()`, `recordTelemetryEvent()`, `searchParams.get()`, `searchParams.has()`, `setKeyboardAccessForNonDialogElements()`, `updateNoLogins()`, `window.addEventListener()`, `window.dispatchEvent()`, `window.document.documentElement.classList.remove()`

## exportButton()
- 位置: L21-23
- 役割: メニュー内のエクスポート項目を menu-button の shadow DOM から取得する。
- 触るとき: エクスポート項目の位置やクラス名を変えたとき。
- 呼び出し先: `this.menuButton.shadowRoot.querySelector()`

## removeAllButton()
- 位置: L25-29
- 役割: メニュー内のすべて削除の項目を menu-button の shadow DOM から取得する。
- 触るとき: すべて削除の項目の位置やクラス名を変えたとき。
- 呼び出し先: `this.menuButton.shadowRoot.querySelector()`

## updateNoLogins()
- 位置: L34-40
- 役割: 件数が 0 のとき no-logins クラスを document・一覧・項目に付け、エクスポートとすべて削除を無効化する。
- 触るとき: ログインが無いときの表示や操作の無効化の条件を変えるとき。
- 呼び出し先: `document.documentElement.classList.toggle()`, `gElements.loginItem.classList.toggle()`, `gElements.loginList.classList.toggle()`
- 参照: `gElements.exportButton.disabled`, `gElements.removeAllButton.disabled`

## handleAllLogins()
- 位置: L42-46
- 役割: 一覧に全件を設定し、件数を更新して updateNoLogins を呼ぶ。
- 触るとき: 全件受信時の一覧更新や件数の扱いを変えるとき。
- 呼び出し先: `gElements.loginList.setLogins()`, `updateNoLogins()`
- 参照: `logins.length`

## handleSyncState()
- 位置: L51-56
- 役割: FxA ボタンと導入画面に同期状態を渡し、ログイン状態とパスワード同期の有効状態を保持する。
- 触るとき: 同期状態を受け取る画面を増やすとき、またはダイアログ文言の出し分けに使う状態を変えるとき。
- 呼び出し先: `gElements.fxAccountsButton.updateState()`, `gElements.loginIntro.updateState()`
- 参照: `syncState.loggedIn`, `syncState.passwordSyncEnabled`

## interceptFocusKey()
- 位置: async L233-251
- 役割: about-logins-login-filter2 のラベルから key を取り、Accel とそのキーの組み合わせで検索欄の入力にフォーカスするキーハンドラを登録する。
- 触るとき: 検索欄のショートカットを変えるとき、またはローカライズで key 属性が変わったときに効くか確かめるとき。
- 呼び出し先: `document.addEventListener()`, `document.l10n.formatMessages()`, `event.getModifierState()`, `findKey.attributes .find()`, `findKey.attributes .find(a => a.name == "key") .value.toLowerCase()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `event.preventDefault()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `document .querySelector("login-list") .shadowRoot.querySelector("login-filter") .shadowRoot.querySelector()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `document .querySelector("login-list") .shadowRoot.querySelector()`
- 条件付き依存: `if (event.key == focusKey && event.getModifierState("Accel"))` → `document .querySelector()`
- 参照: `a.name`, `event.key`
