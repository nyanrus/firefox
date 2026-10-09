# browser/extensions/webcompat/shims/moat.js

source: browser/extensions/webcompat/shims/moat.js
source-hash: 9957492684395c673f5ac3fb073e70d0d54ab567
lines: 47

## <module>
- 役割: (未記入)

## __A()
- 位置: L25-25
- 役割: (未記入)
- 触るとき: (未記入)

## disableLogging()
- 位置: L26-26
- 役割: (未記入)
- 触るとき: (未記入)

## enableLogging()
- 位置: L27-27
- 役割: (未記入)
- 触るとき: (未記入)

## getMoatTargetingForPage()
- 位置: L28-28
- 役割: (未記入)
- 触るとき: (未記入)

## getMoatTargetingForSlot()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slot?.getSlotElementId()`, `targeting.get()`

## pageDataAvailable()
- 位置: L32-32
- 役割: (未記入)
- 触るとき: (未記入)

## safetyDataAvailable()
- 位置: L33-33
- 役割: (未記入)
- 触るとき: (未記入)

## setMoatTargetingForAllSlots()
- 位置: L34-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slot.getSlotElementId()`, `slot.getTargeting()`, `targeting.set()`, `window.googletag.pubads()`, `window.googletag.pubads().getSlots()`

## setMoatTargetingForSlot()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slot?.getSlotElementId()`, `targeting.set()`

## slotDataAvailable()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.googletag?.pubads()`, `window.googletag?.pubads().getSlots()`
- 参照: `window.googletag?.pubads().getSlots().length`
