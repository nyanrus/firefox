# browser/extensions/webcompat/shims/google-publisher-tags.js

source: browser/extensions/webcompat/shims/google-publisher-tags.js
source-hash: b3e00b608b6da9aebb2c9416affc1bc44389f514
lines: 565

## <module>
- 役割: (未記入)

## noopthisfn()
- 位置: L18-20
- 役割: (未記入)
- 触るとき: (未記入)

## fireSlotEvent()
- 位置: L30-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cb()`, `eventCallbacks.get()`, `requestAnimationFrame()`, `resolve()`

## recreateIframeForSlot()
- 位置: L42-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(eid)?.remove()`, `slot.getId()`, `slot.getSlotElementId()`
- 条件付き依存: `if (node)` → `document.createElement()`
- 条件付き依存: `if (node)` → `f.setAttribute()`
- 条件付き依存: `if (node)` → `node.appendChild()`
- 参照: `f.id`, `f.srcdoc`, `f.style`

## emptySlotElement()
- 位置: L58-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `node.lastChild.remove()`, `slot.getSlotElementId()`
- 参照: `node?.lastChild`

## getCreatives()
- 位置: L66-74
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.documentElement`

## fetchSlot()
- 位置: L77-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `fetchedSlots.add()`, `slot.getSlotElementId()`, `slotCreatives.get()`, `usedCreatives.has()`, `usedCreatives.set()`
- 条件付き依存: `if (creatives instanceof SizeMapping)` → `creatives.getCreatives()`
- 参照: `creatives?.length`

## displaySlot()
- 位置: async L109-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `emptySlotElement()`, `fetchedSlots.has()`, `fireSlotEvent()`, `recreateIframeForSlot()`, `slot.getSlotElementId()`
- 条件付き依存: `if (!fetchedSlots.has(id))` → `fetchSlot()`
- 条件付き依存: `if (parent)` → `parent.appendChild()`
- 条件付き依存: `if (parent)` → `document.createElement()`

## addEventListener()
- 位置: L137-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eventCallbacks.get()`, `eventCallbacks.get(name).add()`, `eventCallbacks.has()`
- 条件付き依存: `if (!eventCallbacks.has(name))` → `eventCallbacks.set()`

## removeEventListener()
- 位置: L145-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eventCallbacks.has()`
- 条件付き依存: `if (eventCallbacks.has(name))` → `eventCallbacks.get(name).delete()`
- 条件付き依存: `if (eventCallbacks.has(name))` → `eventCallbacks.get()`

## enable()
- 位置: L154-154
- 役割: (未記入)
- 触るとき: (未記入)

## fillSlot()
- 位置: L155-155
- 役割: (未記入)
- 触るとき: (未記入)

## getAttributeKeys()
- 位置: L156-156
- 役割: (未記入)
- 触るとき: (未記入)

## getDisplayAdsCorrelator()
- 位置: L157-157
- 役割: (未記入)
- 触るとき: (未記入)

## getName()
- 位置: L158-158
- 役割: (未記入)
- 触るとき: (未記入)

## getSlotIdMap()
- 位置: L159-161
- 役割: (未記入)
- 触るとき: (未記入)

## getSlots()
- 位置: L162-162
- 役割: (未記入)
- 触るとき: (未記入)

## getVideoStreamCorrelator()
- 位置: L163-163
- 役割: (未記入)
- 触るとき: (未記入)

## isRoadblockingSupported()
- 位置: L164-164
- 役割: (未記入)
- 触るとき: (未記入)

## isSlotAPersistentRoadblock()
- 位置: L165-165
- 役割: (未記入)
- 触るとき: (未記入)

## notifyUnfilledSlots()
- 位置: L166-166
- 役割: (未記入)
- 触るとき: (未記入)

## onImplementationLoaded()
- 位置: L167-167
- 役割: (未記入)
- 触るとき: (未記入)

## refreshAllSlots()
- 位置: L168-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `displaySlot()`, `fetchSlot()`, `slotsById.values()`

## set()
- 位置: L175-175
- 役割: (未記入)
- 触るとき: (未記入)

## setRefreshUnfilledSlots()
- 位置: L176-176
- 役割: (未記入)
- 触るとき: (未記入)

## setVideoSession()
- 位置: L177-177
- 役割: (未記入)
- 触るとき: (未記入)

## slotRenderEnded()
- 位置: L178-178
- 役割: (未記入)
- 触るとき: (未記入)

## setContent()
- 位置: L183-183
- 役割: (未記入)
- 触るとき: (未記入)

## getTargetingValue()
- 位置: L187-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.flat.call()`

## updateTargeting()
- 位置: L197-204
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof map === "object")` → `Object.entries()`
- 条件付き依存: `if (typeof map === "object")` → `targeting.set()`
- 条件付き依存: `if (typeof map === "object")` → `getTargetingValue()`

## defineSlot()
- 位置: L206-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slotCreatives.set()`, `slots.set()`, `slotsById.has()`, `slotsById.set()`, `slotsPerPath.get()`, `slotsPerPath.set()`
- 条件付き依存: `if (slotsById.has(opt_div))` → `document.getElementById(opt_div)?.remove()`
- 条件付き依存: `if (slotsById.has(opt_div))` → `document.getElementById()`
- 条件付き依存: `if (slotsById.has(opt_div))` → `slotsById.get()`

## getHeight()
- 位置: L223-223
- 役割: (未記入)
- 触るとき: (未記入)

## getWidth()
- 位置: L224-224
- 役割: (未記入)
- 触るとき: (未記入)

## addService()
- 位置: L235-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `services.add()`

## clearTargeting()
- 位置: L240-246
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (k === undefined)` → `targeting.clear()`
- 条件付き依存: `if (!(k === undefined))` → `targeting.delete()`

## defineSizeMapping()
- 位置: L247-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slotCreatives.set()`

## get()
- 位置: L251-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `attributes.get()`

## getAdUnitPath()
- 位置: L252-252
- 役割: (未記入)
- 触るとき: (未記入)

## getAttributeKeys()
- 位置: L253-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `attributes.keys()`

## getCategoryExclusions()
- 位置: L254-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`

## getClickUrl()
- 位置: L255-255
- 役割: (未記入)
- 触るとき: (未記入)

## getCollapseEmptyDiv()
- 位置: L256-256
- 役割: (未記入)
- 触るとき: (未記入)

## getConfig()
- 位置: L257-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.freeze()`

## getContentUrl()
- 位置: L270-270
- 役割: (未記入)
- 触るとき: (未記入)

## getDivStartsCollapsed()
- 位置: L271-271
- 役割: (未記入)
- 触るとき: (未記入)

## getDomId()
- 位置: L272-272
- 役割: (未記入)
- 触るとき: (未記入)

## getEscapedQemQueryId()
- 位置: L273-273
- 役割: (未記入)
- 触るとき: (未記入)

## getFirstLook()
- 位置: L274-274
- 役割: (未記入)
- 触るとき: (未記入)

## getId()
- 位置: L275-275
- 役割: (未記入)
- 触るとき: (未記入)

## getHtml()
- 位置: L276-276
- 役割: (未記入)
- 触るとき: (未記入)

## getName()
- 位置: L277-277
- 役割: (未記入)
- 触るとき: (未記入)

## getOutOfPage()
- 位置: L278-278
- 役割: (未記入)
- 触るとき: (未記入)

## getResponseInformation()
- 位置: L279-279
- 役割: (未記入)
- 触るとき: (未記入)

## getServices()
- 位置: L280-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`

## getSizes()
- 位置: L281-281
- 役割: (未記入)
- 触るとき: (未記入)

## getSlotElementId()
- 位置: L282-282
- 役割: (未記入)
- 触るとき: (未記入)

## getSlotId()
- 位置: L283-283
- 役割: (未記入)
- 触るとき: (未記入)

## getTargeting()
- 位置: L284-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTargeting.get()`, `targeting.get()`

## getTargetingKeys()
- 位置: L285-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.of()`, `gTargeting.keys()`, `targeting.keys()`

## getTargetingMap()
- 位置: L289-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.fromEntries()`, `gTargeting.entries()`, `targeting.entries()`

## set()
- 位置: L294-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `attributes.set()`

## setCategoryExclusion()
- 位置: L298-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `exclusions.add()`

## setClickUrl()
- 位置: L302-305
- 役割: (未記入)
- 触るとき: (未記入)

## setCollapseEmptyDiv()
- 位置: L306-309
- 役割: (未記入)
- 触るとき: (未記入)

## setConfig()
- 位置: L310-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.enrties()`
- 条件付き依存: `if (key == "targeting")` → `updateTargeting()`

## setTargeting()
- 位置: L325-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTargetingValue()`, `targeting.set()`

## toString()
- 位置: L329-329
- 役割: (未記入)
- 触るとき: (未記入)

## updateTargetingFromMap()
- 位置: L330-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateTargeting()`

## clear()
- 位置: L351-351
- 役割: (未記入)
- 触るとき: (未記入)

## clearTargeting()
- 位置: L354-360
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (k === undefined)` → `gTargeting.clear()`
- 条件付き依存: `if (!(k === undefined))` → `gTargeting.delete()`

## collapseEmptyDivs()
- 位置: L361-361
- 役割: (未記入)
- 触るとき: (未記入)

## defineOutOfPagePassback()
- 位置: L362-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defineSlot()`

## definePassback()
- 位置: L363-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defineSlot()`

## disableInitialLoad()
- 位置: L364-367
- 役割: (未記入)
- 触るとき: (未記入)

## display()
- 位置: L368-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defineSlot()`, `displaySlot()`

## enable()
- 位置: L372-372
- 役割: (未記入)
- 触るとき: (未記入)

## enableAsyncRendering()
- 位置: L373-373
- 役割: (未記入)
- 触るとき: (未記入)

## enableLazyLoad()
- 位置: L374-374
- 役割: (未記入)
- 触るとき: (未記入)

## enableSingleRequest()
- 位置: L375-375
- 役割: (未記入)
- 触るとき: (未記入)

## enableSyncRendering()
- 位置: L376-376
- 役割: (未記入)
- 触るとき: (未記入)

## enableVideoAds()
- 位置: L377-377
- 役割: (未記入)
- 触るとき: (未記入)

## forceExperiment()
- 位置: L378-378
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: L379-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAttributes.get()`

## getAttributeKeys()
- 位置: L380-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `gAttributes.keys()`

## getCorrelator()
- 位置: L381-381
- 役割: (未記入)
- 触るとき: (未記入)

## getImaContent()
- 位置: L382-382
- 役割: (未記入)
- 触るとき: (未記入)

## getName()
- 位置: L383-383
- 役割: (未記入)
- 触るとき: (未記入)

## getSlots()
- 位置: L384-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `slots.values()`

## getSlotIdMap()
- 位置: L385-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `s.getId()`, `slots.values()`, `slots.values().forEach()`

## getTagSessionCorrelator()
- 位置: L392-392
- 役割: (未記入)
- 触るとき: (未記入)

## getTargeting()
- 位置: L393-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTargeting.get()`

## getTargetingKeys()
- 位置: L394-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `gTargeting.keys()`

## getTargetingMap()
- 位置: L395-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `gTargeting.entries()`

## getVersion()
- 位置: L396-396
- 役割: (未記入)
- 触るとき: (未記入)

## getVideoContent()
- 位置: L397-397
- 役割: (未記入)
- 触るとき: (未記入)

## isInitialLoadDisabled()
- 位置: L398-398
- 役割: (未記入)
- 触るとき: (未記入)

## isSRA()
- 位置: L399-399
- 役割: (未記入)
- 触るとき: (未記入)

## markAsAmp()
- 位置: L400-400
- 役割: (未記入)
- 触るとき: (未記入)

## refresh()
- 位置: L401-417
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!slts)` → `slots.values()`
- 条件付き依存: `if (!(!slts))` → `Array.isArray()`
- 条件付き依存: `if (slot)` → `fetchSlot()`
- 条件付き依存: `if (slot)` → `displaySlot()`
- 条件付き依存: `if (slot)` → `console.error()`

## set()
- 位置: L419-422
- 役割: (未記入)
- 触るとき: (未記入)

## setCentering()
- 位置: L424-424
- 役割: (未記入)
- 触るとき: (未記入)

## setImaContent()
- 位置: L428-431
- 役割: (未記入)
- 触るとき: (未記入)

## setTargeting()
- 位置: L439-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTargeting.set()`, `getTargetingValue()`

## setVideoContent()
- 位置: L443-446
- 役割: (未記入)
- 触るとき: (未記入)

## updateCorrelator()
- 位置: L447-447
- 役割: (未記入)
- 触るとき: (未記入)

## updateTargetingFromMap()
- 位置: L448-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateTargeting()`

## constructor()
- 位置: L456-458
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#mapping`

## addSize()
- 位置: L459-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `isNaN()`
- 条件付き依存: `if (!( size !== "fluid" && (!Array.isArray(size) || isNaN(size[0]) || isNaN(size[1])) ))` → `this.#mapping?.push()`
- 参照: `this.#mapping`

## build()
- 位置: L470-472
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#mapping`

## companionAds()
- 位置: L484-484
- 役割: (未記入)
- 触るとき: (未記入)

## content()
- 位置: L485-485
- 役割: (未記入)
- 触るとき: (未記入)

## defineOutOfPageSlot()
- 位置: L486-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defineSlot()`

## defineSlot()
- 位置: L487-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defineSlot()`

## destroySlots()
- 位置: L488-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slots.clear()`, `slotsById.clear()`

## disablePublisherConsole()
- 位置: L492-492
- 役割: (未記入)
- 触るとき: (未記入)

## display()
- 位置: L493-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `displaySlot()`, `slotsById.get()`
- 条件付き依存: `if (arg?.getSlotElementId)` → `arg.getSlotElementId()`
- 条件付き依存: `if (!(arg?.nodeType))` → `String()`
- 参照: `arg.id`, `arg?.getSlotElementId`, `arg?.nodeType`

## enableServices()
- 位置: L504-504
- 役割: (未記入)
- 触るとき: (未記入)

## getConfig()
- 位置: L513-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.freeze()`

## getVersion()
- 位置: L526-526
- 役割: (未記入)
- 触るとき: (未記入)

## pubads()
- 位置: L527-527
- 役割: (未記入)
- 触るとき: (未記入)

## setAdIframeTitle()
- 位置: L529-529
- 役割: (未記入)
- 触るとき: (未記入)

## setConfig()
- 位置: L530-542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.enrties()`
- 条件付き依存: `if (key == "targeting")` → `updateTargeting()`

## sizeMapping()
- 位置: L543-543
- 役割: (未記入)
- 触るとき: (未記入)

## run()
- 位置: L546-554
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof fn === "function")` → `fn.call()`
- 条件付き依存: `if (typeof fn === "function")` → `console.error()`
