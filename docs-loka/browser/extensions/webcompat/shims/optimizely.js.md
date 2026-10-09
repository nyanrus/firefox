# browser/extensions/webcompat/shims/optimizely.js

source: browser/extensions/webcompat/shims/optimizely.js
source-hash: dcda87421defc47bc1e927a98c9b7e9026f17bb7
lines: 206

## <module>
- 役割: (未記入)

## query()
- 位置: L14-14
- 役割: (未記入)
- 触るとき: (未記入)

## getAttributeValue()
- 位置: L18-18
- 役割: (未記入)
- 触るとき: (未記入)

## waitForAttributeValue()
- 位置: L19-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## getActivationId()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)

## getActiveExperimentIds()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)

## getCampaignStateLists()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)

## getCampaignStates()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)

## getDecisionObject()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)

## getDecisionString()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)

## getExperimentStates()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)

## getPageStates()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)

## getRedirectInfo()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)

## getVariationMap()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)

## isGlobalHoldback()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)

## poll()
- 位置: L77-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fn()`, `setInterval()`

## waitUntil()
- 位置: L85-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `check()`, `setInterval()`
- 条件付き依存: `if (check())` → `resolve()`

## check()
- 位置: L87-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `test()`
- 条件付き依存: `if (test())` → `clearInterval()`
- 条件付き依存: `if (test())` → `resolve()`

## waitForElement()
- 位置: L107-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `waitUntil()`

## observeSelector()
- 位置: L113-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setInterval()`
- 条件付き依存: `if (timeout)` → `setTimeout()`
- 条件付き依存: `if (timeout)` → `clearInterval()`

## check()
- 位置: L116-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelectorAll()`, `fn()`, `observed.add()`, `observed.has()`
- 条件付き依存: `if (opts.once)` → `clearInterval()`
- 参照: `opts.once`

## get()
- 位置: L178-200
- 役割: (未記入)
- 触るとき: (未記入)

## push()
- 位置: L202-202
- 役割: (未記入)
- 触るとき: (未記入)
