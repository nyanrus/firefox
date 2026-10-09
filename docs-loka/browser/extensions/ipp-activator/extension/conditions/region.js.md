# browser/extensions/ipp-activator/extension/conditions/region.js

source: browser/extensions/ipp-activator/extension/conditions/region.js
source-hash: 8f95c5b05c631601807e11a04d65c2e5789f3865
lines: 43

## <module>
- 役割: (未記入)

## ConditionRegion.init()
- 位置: async L14-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.ippActivator.getRegion()`, `browser.ippActivator.onRegionChanged.addListener()`, `super.init()`
- 参照: `this.#listener`, `this.#region`

## this.#listener()
- 位置: L19-24
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (next !== this.#region)` → `this._notifyChange()`
- 参照: `this.#region`

## ConditionRegion.uninit()
- 位置: L28-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.uninit()`
- 条件付き依存: `if (this.#listener)` → `browser.ippActivator.onRegionChanged.removeListener()`
- 参照: `this.#listener`

## ConditionRegion.check()
- 位置: L36-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `list.includes()`
- 参照: `this.#region`, `this.desc.regions`, `this.desc?.regions`
