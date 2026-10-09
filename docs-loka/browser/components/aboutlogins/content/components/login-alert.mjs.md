# browser/components/aboutlogins/content/components/login-alert.mjs

source: browser/components/aboutlogins/content/components/login-alert.mjs
source-hash: 69089c2c7c29df2641774493e93ab459d9f66b88
lines: 169

## <module>
- 役割: about:logins の警告表示 login-alert と、その派生の脆弱パスワード警告・侵害警告を定義する。
- 呼び出し先: `customElements.define()`

## LoginAlert.properties()
- 位置: L14-20
- 役割: variant(反映)、icon、titleId の属性を定義する。
- 触るとき: 警告カードに渡せる属性を増やすとき。

## LoginAlert.render()
- 位置: L22-35
- 役割: スタイルシートとアイコン、タイトル、アクション用とコンテンツ用のスロットを描画する。
- 触るとき: 警告カードの基本の並びや slot の構成を変えるとき。
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.icon`, `this.titleId`

## VulnerablePasswordAlert.properties()
- 位置: L39-44
- 役割: hostname(反映)と changePasswordURL の属性を定義する。
- 触るとき: 脆弱パスワード警告に渡す値を増やすとき。

## VulnerablePasswordAlert.constructor()
- 位置: L46-50
- 役割: hostname と changePasswordURL を空文字で初期化する。
- 触るとき: 警告の既定値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.changePasswordURL`, `this.hostname`

## VulnerablePasswordAlert.render()
- 位置: L51-88
- 役割: info 警告として、説明文・変更ページへのリンク(URL が無ければ hostname を href にする)・詳細リンクを描画する。
- 触るとき: 脆弱パスワード警告の文言やリンク先の決め方を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.changePasswordURL`, `this.hostname`

## LoginBreachAlert.properties()
- 位置: L92-99
- 役割: date、hostname、breachName(反映)と changePasswordURL の属性を定義する。
- 触るとき: 侵害警告に渡す値を増やすとき。

## LoginBreachAlert.constructor()
- 位置: L101-107
- 役割: date・hostname・breachName・changePasswordURL を既定値で初期化する。
- 触るとき: 侵害警告の既定値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.breachName`, `this.changePasswordURL`, `this.date`, `this.hostname`

## LoginBreachAlert.displayHostname()
- 位置: L109-112
- 役割: hostname を URL として解析してホスト名を返し、解析できなければ hostname をそのまま返す。
- 触るとき: 侵害警告に表示するサイト名の形式を変えるとき。
- 呼び出し先: `URL.parse()`
- 参照: `this.hostname`, `url?.hostname`

## LoginBreachAlert.handleBreachLinkClick()
- 位置: L114-126
- 役割: 侵害リンクのクリックで breachAlertLinkClicked テレメトリを発行し、breach_name に breachName か表示用ホスト名を入れる。
- 触るとき: 侵害リンクのテレメトリを変えるとき。
- 呼び出し先: `document.dispatchEvent()`
- 参照: `this.breachName`, `this.displayHostname`

## LoginBreachAlert.render()
- 位置: L128-160
- 役割: error 警告として、侵害日・説明文・変更ページへのリンク(URL が無ければ hostname を href にする)を描画し、リンククリックで記録を発行する。
- 触るとき: 侵害警告の表示内容やリンク先の決め方を変えるとき。
- 呼び出し先: `JSON.stringify()`, `guard()`, `html()`
- 参照: `this.changePasswordURL`, `this.date`, `this.displayHostname`, `this.handleBreachLinkClick`, `this.hostname`
