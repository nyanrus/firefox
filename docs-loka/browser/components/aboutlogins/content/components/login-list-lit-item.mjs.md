# browser/components/aboutlogins/content/components/login-list-lit-item.mjs

source: browser/components/aboutlogins/content/components/login-list-lit-item.mjs
source-hash: 92568e2ba41769bf8876a5a3dd10eadec2e8a47d
lines: 172

## <module>
- 役割: ログイン一覧行の lit 版コンポーネント(list-item、new-list-item、login-list-item)を定義し、カスタム要素として登録する
- 呼び出し先: `customElements.define()`

## ListItem.properties()
- 位置: L15-20
- 役割: 行の共通プロパティ(icon、selected)を宣言する
- 触るとき: 行の共通属性を増やすとき

## ListItem.constructor()
- 位置: L22-26
- 役割: icon を空、selected を false で初期化する
- 触るとき: 初期値を変えるとき
- 呼び出し先: `super()`
- 参照: `this.icon`, `this.selected`

## ListItem.render()
- 位置: L28-39
- 役割: 選択状態のクラスを付けた li と、icon 画像、login-info と notificationIcon の slot を描画する
- 触るとき: 行の共通マークアップや選択時の見た目を変えるとき
- 呼び出し先: `classMap()`, `html()`
- 参照: `this.icon`, `this.selected`

## NewListItem.constructor()
- 位置: L48-53
- 役割: id を new-login-list-item に固定し、selected と仮 icon を初期化する
- 触るとき: 新規作成行の初期状態を変えるとき
- 呼び出し先: `super()`
- 参照: `this.icon`, `this.id`, `this.selected`

## NewListItem.render()
- 位置: L55-72
- 役割: 新規作成行の表示文字列を data-l10n-id 付きで描画する
- 触るとき: 新規作成行に出す文言を変えるとき
- 呼び出し先: `html()`
- 参照: `this.icon`, `this.selected`

## LoginListItem.properties()
- 位置: L76-84
- 役割: ログイン行のプロパティ(favicon、title、username、notificationIcon、selected)を宣言し、title と username は属性に反映させる
- 触るとき: 一覧行に新しく表示する情報を追加するとき

## LoginListItem.constructor()
- 位置: L86-93
- 役割: ログイン行の各プロパティを空または false で初期化する
- 触るとき: ログイン行の初期値を変えるとき
- 呼び出し先: `super()`
- 参照: `this.favicon`, `this.notificationIcon`, `this.selected`, `this.title`, `this.username`

## LoginListItem.render()
- 位置: L94-166
- 役割: notificationIcon に応じて host に breached または vulnerable クラスを付け、タイトルとユーザー名(空なら未入力の文言)と警告アイコンを描画する
- 触るとき: 侵害・脆弱の警告アイコンの出し分けや、ユーザー名が無い場合の表示を変えるとき
- 呼び出し先: `choose()`, `html()`, `this.classList.add()`, `this.classList.remove()`, `when()`
- 参照: `this.favicon`, `this.notificationIcon`, `this.selected`, `this.title`, `this.username`
