# browser/extensions/ipp-activator/extension/conditions/cookie.js

source: browser/extensions/ipp-activator/extension/conditions/cookie.js
source-hash: f0549d32c96c40393a66ab11a9a369e8d601ba17
lines: 70

## <module>
- 役割: (未記入)

## ConditionCookie.init()
- 位置: async L13-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `browser.cookies.getAll()`, `super.init()`, `this.factory.retrieveData()`, `this.factory.storeData()`
- 参照: `ConditionCookie.STORAGE_KEY`, `this.desc`

## ConditionCookie.check()
- 位置: L36-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cookie.value.includes()`, `cookies.find()`, `this.factory.retrieveData()`
- 参照: `ConditionCookie.STORAGE_KEY`, `c.name`, `cookie.value`, `this.desc.domain`, `this.desc.name`, `this.desc.value`, `this.desc.value_contain`
