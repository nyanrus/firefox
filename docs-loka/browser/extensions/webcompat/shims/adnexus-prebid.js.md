# browser/extensions/webcompat/shims/adnexus-prebid.js

source: browser/extensions/webcompat/shims/adnexus-prebid.js
source-hash: f0f810f0e9941ce07e953277ef2ffbd3e80f9619
lines: 69

## <module>
- 役割: (未記入)

## addAdUnits()
- 位置: L23-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `adUnits.push()`

## offEvent()
- 位置: L30-30
- 役割: (未記入)
- 触るとき: (未記入)

## refreshAds()
- 位置: L32-32
- 役割: (未記入)
- 触るとき: (未記入)

## removeAdUnit()
- 位置: L33-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if (adUnits[i].code === code)` → `adUnits.splice()`
- 参照: `adUnits.length`, `adUnits[i].code`

## renderAd()
- 位置: L45-45
- 役割: (未記入)
- 触るとき: (未記入)

## requestBids()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `params?.bidsBackHandler()`

## setConfig()
- 位置: L49-49
- 役割: (未記入)
- 触るとき: (未記入)

## setTargetingForGPTAsync()
- 位置: L50-50
- 役割: (未記入)
- 触るとき: (未記入)

## push()
- 位置: L53-61
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof fn === "function")` → `fn()`
- 条件付き依存: `if (typeof fn === "function")` → `console.trace()`
