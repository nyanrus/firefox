# browser/components/aboutlogins/content/components/login-message-popup.mjs

source: browser/components/aboutlogins/content/components/login-message-popup.mjs
source-hash: 4d6293037b5eb656fea9f6311117be7e26cadaed
lines: 95

## <module>
- 役割: パスワードやオリジンの注意吹き出し(password-warning と origin-warning)を lit で描画するモジュール
- 呼び出し先: `customElements.define()`

## stylesTemplate()
- 位置: L8-12
- 役割: 吹き出し用の stylesheet 要素を返す
- 触るとき: 吹き出しの見た目を別ファイルで管理するとき。読み込み先の CSS を確認する
- 呼び出し先: `html()`

## MessagePopup()
- 位置: L14-26
- 役割: 吹き出しの共通マークアップを描画する。l10n ID があれば data-l10n-id とその引数を、なければ本文を入れる
- 触るとき: 吹き出しの共通構造や ARIA の role を変えるとき。両警告がこれを使う
- 呼び出し先: `JSON.stringify()`, `html()`, `ifDefined()`

## PasswordWarning.properties()
- 位置: L29-37
- 役割: 新規か否か、タイトル、本文、矢印の向き、role を宣言する
- 触るとき: パスワード警告に渡すプロパティを増やすとき

## PasswordWarning.constructor()
- 位置: L39-43
- 役割: 新規フラグを false、矢印の向きを left で初期化する
- 触るとき: パスワード警告の既定値を変えるとき
- 呼び出し先: `super()`
- 参照: `this.arrowDirection`, `this.isNewLogin`

## PasswordWarning.render()
- 位置: L44-65
- 役割: 本文が指定されていればそれを、なければ新規か既存かに応じた文言(追加用か編集用か)を描画する
- 触るとき: パスワード警告の文言の出し分けを変えるとき。既存ログインでは webTitle を引数に渡す
- 呼び出し先: `MessagePopup()`, `html()`, `stylesTemplate()`
- 条件付き依存: `if (this.message)` → `html()`
- 条件付き依存: `if (this.message)` → `stylesTemplate()`
- 条件付き依存: `if (this.message)` → `MessagePopup()`
- 参照: `this.isNewLogin`, `this.message`, `this.role`, `this.webTitle`

## OriginWarning.properties()
- 位置: L69-76
- 役割: l10n ID、本文、矢印の向き、role を宣言する
- 触るとき: オリジン警告に渡すプロパティを増やすとき

## OriginWarning.constructor()
- 位置: L78-81
- 役割: 矢印の向きを left で初期化する
- 触るとき: オリジン警告の既定値を変えるとき
- 呼び出し先: `super()`
- 参照: `this.arrowDirection`

## OriginWarning.render()
- 位置: L83-90
- 役割: 渡された l10n ID と本文で吹き出しを描画する
- 触るとき: オリジン警告の文言の供給元を調べるとき
- 呼び出し先: `MessagePopup()`, `html()`, `stylesTemplate()`
- 参照: `this.l10nId`, `this.message`, `this.role`
