# browser/extensions/ipp-activator/extension/conditions/url.js

source: browser/extensions/ipp-activator/extension/conditions/url.js
source-hash: df7669385ccf76e5cd29528e9feacd74040d6286
lines: 61

## <module>
- 役割: (未記入)

## ConditionUrl.init()
- 位置: async L15-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.tabs.get()`, `browser.tabs.onUpdated.addListener()`, `super.init()`
- 参照: `tab?.url`, `this.#onTabUpdated`, `this.#tabId`, `this.#url`, `this.factory?.context?.tabId`

## this.#onTabUpdated()
- 位置: L28-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._notifyChange()`
- 参照: `changeInfo.url`, `this.#tabId`, `this.#url`

## ConditionUrl.uninit()
- 位置: L41-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.uninit()`
- 条件付き依存: `if (this.#onTabUpdated)` → `browser.tabs.onUpdated.removeListener()`
- 参照: `this.#onTabUpdated`

## ConditionUrl.check()
- 位置: L49-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `console.warn()`, `pattern.test()`
- 参照: `this.#url`, `this.desc?.pattern`
