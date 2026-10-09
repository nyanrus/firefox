# browser/extensions/ipp-activator/extension/conditions/base.js

source: browser/extensions/ipp-activator/extension/conditions/base.js
source-hash: 184f631fd6151e4ccef70a41fe7d4039b015d90e
lines: 75

## <module>
- 役割: (未記入)

## ConditionBase.constructor()
- 位置: L11-14
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.desc`, `this.factory`

## ConditionBase.init()
- 位置: async L16-18
- 役割: (未記入)
- 触るとき: (未記入)

## ConditionBase.uninit()
- 位置: L20-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.clear()`

## ConditionBase.check()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)

## ConditionBase.onChange()
- 位置: L28-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.add()`, `this.#listeners.delete()`

## ConditionBase._notifyChange()
- 位置: L33-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb()`
- 参照: `this.#listeners`

## ConditionBaseWithSub.constructor()
- 位置: L49-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conditions.map()`, `factory.create()`, `super()`
- 参照: `this.conditions`

## ConditionBaseWithSub.init()
- 位置: async L55-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `c.init()`, `c.onChange()`, `super.init()`, `this.#unsubs.push()`, `this._notifyChange()`
- 参照: `this.conditions`

## ConditionBaseWithSub.uninit()
- 位置: L64-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `c.uninit()`, `super.uninit()`, `this.#unsubs.forEach()`, `this.conditions.forEach()`, `u()`
- 参照: `this.#unsubs`
