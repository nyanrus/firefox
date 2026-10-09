# browser/components/aboutlogins/content/components/login-command-button.mjs

source: browser/components/aboutlogins/content/components/login-command-button.mjs
source-hash: 9b74185c3a0ea6e35e759d9b9bf7d2543454e7d0
lines: 190

## <module>
- 役割: about:logins のログイン操作ボタン(作成・編集・削除・ユーザー名とパスワードのコピー)を定義する。
- 呼び出し先: `customElements.define()`

## stylesTemplate()
- 位置: L18-26
- 役割: 共通の common.css とボタン用の login-command-button.css を読み込む link 要素の並びを返す。
- 触るとき: ボタンのスタイルシートの読み込み元を変えるとき。
- 呼び出し先: `html()`

## LoginCommandButton()
- 位置: L28-45
- 役割: onClick、l10nId、icon、variant、disabled、buttonText を受け取り、アイコンと文言を持つ button 要素を描画する共通関数。
- 触るとき: 全てのコマンドボタンに共通の属性や構造を変えるとき。
- 呼び出し先: `html()`, `ifDefined()`

## CreateLoginButton.properties()
- 位置: L48-52
- 役割: disabled を反映する属性を定義する。
- 触るとき: 新規作成ボタンに属性を追加するとき。

## CreateLoginButton.constructor()
- 位置: L54-57
- 役割: disabled を false で初期化する。
- 触るとき: 新規作成ボタンの初期状態を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.disabled`

## CreateLoginButton.render()
- 位置: L58-68
- 役割: 新規作成ボタンを icon-button の形式で、作成用の l10n ID と plus アイコン付きで描画する。
- 触るとき: 新規作成ボタンの見た目や文言を変えるとき。
- 呼び出し先: `LoginCommandButton()`, `html()`, `stylesTemplate()`
- 参照: `this.disabled`

## EditButton.properties()
- 位置: L72-76
- 役割: disabled を反映する属性を定義する。
- 触るとき: 編集ボタンに属性を追加するとき。

## EditButton.constructor()
- 位置: L78-81
- 役割: disabled を false で初期化する。
- 触るとき: 編集ボタンの初期状態を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.disabled`

## EditButton.render()
- 位置: L82-92
- 役割: 編集ボタンを ghost-button の形式で、編集文言と edit アイコン付きで描画する。
- 触るとき: 編集ボタンの見た目や文言を変えるとき。
- 呼び出し先: `LoginCommandButton()`, `html()`, `stylesTemplate()`
- 参照: `this.disabled`

## DeleteButton.properties()
- 位置: L96-100
- 役割: disabled を反映する属性を定義する。
- 触るとき: 削除ボタンに属性を追加するとき。

## DeleteButton.constructor()
- 位置: L102-105
- 役割: disabled を false で初期化する。
- 触るとき: 削除ボタンの初期状態を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.disabled`

## DeleteButton.render()
- 位置: L106-114
- 役割: 削除ボタンを ghost-button の形式で、削除文言と delete アイコン付きで描画する。
- 触るとき: 削除ボタンの見た目や文言を変えるとき。
- 呼び出し先: `LoginCommandButton()`, `html()`, `stylesTemplate()`
- 参照: `this.disabled`

## CopyUsernameButton.properties()
- 位置: L118-123
- 役割: copiedText(反映)と disabled を属性として定義する。
- 触るとき: ユーザー名コピーの状態を増やすとき。

## CopyUsernameButton.constructor()
- 位置: L125-129
- 役割: copiedText と disabled を false で初期化する。
- 触るとき: ユーザー名コピーボタンの初期状態を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.copiedText`, `this.disabled`

## CopyUsernameButton.render()
- 位置: L130-148
- 役割: host の class を copied-button か copy-button に切り替え、コピー済みならチェック付きの文言、未コピーならテキスト型のコピー文言のボタンを描画する。
- 触るとき: ユーザー名のコピー後の表示切り替えを変えるとき。
- 呼び出し先: `LoginCommandButton()`, `html()`, `stylesTemplate()`, `when()`
- 参照: `this.className`, `this.copiedText`, `this.disabled`

## CopyPasswordButton.properties()
- 位置: L152-157
- 役割: copiedText(反映)と disabled を属性として定義する。
- 触るとき: パスワードコピーの状態を増やすとき。

## CopyPasswordButton.constructor()
- 位置: L159-163
- 役割: copiedText と disabled を false で初期化する。
- 触るとき: パスワードコピーボタンの初期状態を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.copiedText`, `this.disabled`

## CopyPasswordButton.render()
- 位置: L164-182
- 役割: host の class を copied-button か copy-button に切り替え、コピー済みならチェック付きの文言、未コピーならテキスト型のコピー文言のボタンを描画する。
- 触るとき: パスワードのコピー後の表示切り替えを変えるとき。
- 呼び出し先: `LoginCommandButton()`, `html()`, `stylesTemplate()`, `when()`
- 参照: `this.className`, `this.copiedText`, `this.disabled`
