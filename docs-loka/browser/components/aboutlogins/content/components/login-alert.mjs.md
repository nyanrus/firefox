# browser/components/aboutlogins/content/components/login-alert.mjs

source: browser/components/aboutlogins/content/components/login-alert.mjs
source-hash: 69089c2c7c29df2641774493e93ab459d9f66b88
lines: 169

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## LoginAlert.properties()
- 位置: L14-20
- 役割: (未記入)
- 触るとき: (未記入)

## LoginAlert.render()
- 位置: L22-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.icon`, `this.titleId`

## VulnerablePasswordAlert.properties()
- 位置: L39-44
- 役割: (未記入)
- 触るとき: (未記入)

## VulnerablePasswordAlert.constructor()
- 位置: L46-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.changePasswordURL`, `this.hostname`

## VulnerablePasswordAlert.render()
- 位置: L51-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.changePasswordURL`, `this.hostname`

## LoginBreachAlert.properties()
- 位置: L92-99
- 役割: (未記入)
- 触るとき: (未記入)

## LoginBreachAlert.constructor()
- 位置: L101-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.breachName`, `this.changePasswordURL`, `this.date`, `this.hostname`

## LoginBreachAlert.displayHostname()
- 位置: L109-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `this.hostname`, `url?.hostname`

## LoginBreachAlert.handleBreachLinkClick()
- 位置: L114-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`
- 参照: `this.breachName`, `this.displayHostname`

## LoginBreachAlert.render()
- 位置: L128-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `guard()`, `html()`
- 参照: `this.changePasswordURL`, `this.date`, `this.displayHostname`, `this.handleBreachLinkClick`, `this.hostname`
