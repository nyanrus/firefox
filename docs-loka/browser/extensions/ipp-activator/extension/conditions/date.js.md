# browser/extensions/ipp-activator/extension/conditions/date.js

source: browser/extensions/ipp-activator/extension/conditions/date.js
source-hash: bfffeacf934799323e9478de31289ee9647e74fd
lines: 41

## <module>
- 役割: (未記入)

## ConditionDate.init()
- 位置: async L14-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.init()`, `this.#parse()`
- 参照: `this.#end`, `this.#start`, `this.desc?.end`, `this.desc?.start`

## ConditionDate.#parse()
- 位置: L20-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.parse()`, `Number.isFinite()`

## ConditionDate.check()
- 位置: L28-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 参照: `this.#end`, `this.#start`
