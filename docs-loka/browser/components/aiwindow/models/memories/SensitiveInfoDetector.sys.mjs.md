# browser/components/aiwindow/models/memories/SensitiveInfoDetector.sys.mjs

source: browser/components/aiwindow/models/memories/SensitiveInfoDetector.sys.mjs
source-hash: b1153cdc708c06fd4cf93688fe9c469ba9020c52
lines: 536

## <module>
- 役割: (未記入)

## validateCreditCard()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CreditCard.isValidNumber()`

## isPublicIPv4()
- 位置: L421-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ip.split()`, `ip.split(".").map()`, `isNaN()`, `parts.some()`
- 参照: `parts.length`

## validateRoutingNumber()
- 位置: L452-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^\d{9}$/.test()`, `routingNumber.split()`, `routingNumber.split("").map()`

## SensitiveInfoDetector.constructor()
- 位置: L470-472
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.patterns`

## SensitiveInfoDetector.containsSensitiveInfo()
- 位置: L480-502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `text.match()`
- 条件付き依存: `if (pattern.validator)` → `pattern.validator()`
- 参照: `pattern.regex`, `pattern.validator`, `this.patterns`

## SensitiveInfoDetector.containsSensitiveKeywords()
- 位置: L511-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `keyword.endsWith()`, `pattern.test()`, `text.toLowerCase()`
- 条件付き依存: `if (keyword.endsWith("y"))` → `keyword.slice()`
