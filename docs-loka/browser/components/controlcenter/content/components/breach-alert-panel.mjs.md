# browser/components/controlcenter/content/components/breach-alert-panel.mjs

source: browser/components/controlcenter/content/components/breach-alert-panel.mjs
source-hash: ff8e1b21d9a4203c30e111b2220e056fbdf478d4
lines: 123

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## BreachAlert.constructor()
- 位置: L24-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.breachStatus`, `this.hidden`

## BreachAlert._handleCta()
- 位置: async L30-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.trustpanel.breachAlertDiscoveredMonitor.record()`, `this._dismissBreach()`, `this.documentGlobal.switchToTabHavingURI()`
- 参照: `this.hidden`

## BreachAlert._handleDismiss()
- 位置: async L42-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.trustpanel.breachAlertDismissed.record()`, `this._dismissBreach()`
- 参照: `this.breachStatus`, `this.hidden`

## BreachAlert._dismissBreach()
- 位置: async L52-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 条件付き依存: `if (!this.breachNames)` → `console.warn()`
- 参照: `this.breachNames`

## BreachAlert.render()
- 位置: L67-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this._handleCta`, `this._handleDismiss`, `this.breachStatus`, `this.hidden`
