# browser/extensions/ipp-activator/extension/conditions/vpn.js

source: browser/extensions/ipp-activator/extension/conditions/vpn.js
source-hash: e6f4bd4e2115997e71551a54f653d3a2ba0cc476
lines: 42

## <module>
- 役割: (未記入)

## ConditionVPN.init()
- 位置: async L14-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.ippActivator.isIPPActive()`, `browser.ippActivator.onIPPActivated.addListener()`, `super.init()`
- 参照: `this.#ippActive`, `this.#listener`

## this.#listener()
- 位置: L19-24
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (next !== this.#ippActive)` → `this._notifyChange()`
- 参照: `this.#ippActive`

## ConditionVPN.uninit()
- 位置: L28-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.uninit()`
- 条件付き依存: `if (this.#listener)` → `browser.ippActivator.onIPPActivated.removeListener()`
- 参照: `this.#listener`

## ConditionVPN.check()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#ippActive`, `this.desc.active`
