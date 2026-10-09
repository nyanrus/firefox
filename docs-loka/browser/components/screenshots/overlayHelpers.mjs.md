# browser/components/screenshots/overlayHelpers.mjs

source: browser/components/screenshots/overlayHelpers.mjs
source-hash: 1bf1f2cdf0f6503af6f202f3c8ef083fd176e9c5
lines: 611

## <module>
- 役割: (未記入)

## getBoundingClientRect()
- 位置: L30-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ele.getBoundingClientRect()`
- 参照: `ele.getBoundingClientRect`

## setMaxDetectHeight()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)

## setMaxDetectWidth()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)

## getElementFromPoint()
- 位置: async L67-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `doc.defaultView.HTMLIFrameElement.isInstance()`, `doc.elementFromPoint()`
- 条件付き依存: `if (doc.defaultView.HTMLIFrameElement.isInstance(ele))` → `ele.browsingContext.parentWindowContext.windowGlobalChild.getActor()`
- 条件付き依存: `if (doc.defaultView.HTMLIFrameElement.isInstance(ele))` → `actor.sendQuery()`
- 条件付き依存: `if (ele.openOrClosedShadowRoot)` → `ele.openOrClosedShadowRoot.elementFromPoint()`
- 参照: `ele.browsingContext`, `ele.documentGlobal.mozInnerScreenX`, `ele.documentGlobal.mozInnerScreenY`, `ele.openOrClosedShadowRoot`, `rect.bottom`, `rect.left`, `rect.right`, `rect.top`

## getBestRectForElement()
- 位置: L120-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getBoundingClientRect()`
- 条件付き依存: `if (rect && node)` → `evenBetterElement()`
- 条件付き依存: `if (evenBetter)` → `getBoundingClientRect()`
- 条件付き依存: `if (extendNode)` → `getBoundingClientRect()`
- 条件付き依存: `if (extendNode)` → `Math.min()`
- 条件付き依存: `if (extendNode)` → `Math.max()`
- 参照: `combinedRect.height`, `combinedRect.width`, `doc.ELEMENT_NODE`, `extendNode.nextSibling`, `extendNode.nodeType`, `extendRect.bottom`, `extendRect.right`, `extendRect.x`, `extendRect.y`, `lastNode.nextSibling`, `lastNode.parentNode`, `node.parentNode`, `node.tagName`, `parentNode.childNodes`, `parentNode.childNodes.length`, `rect.bottom`, `rect.height`, `rect.right`, `rect.width`, `rect.x`, `rect.y`

## evenBetterElement()
- 位置: L210-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.getAttribute()`
- 条件付き依存: `if (el.getAttribute("role") === "article")` → `getBoundingClientRect()`
- 参照: `doc.ELEMENT_NODE`, `el.getAttribute`, `el.nodeType`, `el.parentNode`, `node.parentNode`, `rect.height`, `rect.width`

## Region.constructor()
- 位置: L242-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetDimensions()`
- 参照: `this.#windowDimensions`

## Region.confineToViewport()
- 位置: L253-255
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#confineToViewport`

## Region.#clampX()
- 位置: L257-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 条件付き依存: `if (this.#confineToViewport)` → `Math.min()`
- 条件付き依存: `if (this.#confineToViewport)` → `Math.max()`
- 参照: `this.#confineToViewport`, `this.#windowDimensions.clientWidth`, `this.#windowDimensions.scrollWidth`, `this.#windowDimensions.scrollX`

## Region.#clampY()
- 位置: L266-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 条件付き依存: `if (this.#confineToViewport)` → `Math.min()`
- 条件付き依存: `if (this.#confineToViewport)` → `Math.max()`
- 参照: `this.#confineToViewport`, `this.#windowDimensions.clientHeight`, `this.#windowDimensions.scrollHeight`, `this.#windowDimensions.scrollY`

## Region.dimensions()
- 位置: L287-305
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dims == null)` → `this.resetDimensions()`
- 参照: `dims.bottom`, `dims.left`, `dims.right`, `dims.top`, `this.bottom`, `this.left`, `this.right`, `this.top`

## Region.setDimensionsFromDOMRect()
- 位置: L313-331
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (rect == null)` → `this.resetDimensions()`
- 参照: `this.#windowDimensions.dimensions`, `this.dimensions`

## Region.dimensions()
- 位置: L333-342
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.bottom`, `this.height`, `this.left`, `this.right`, `this.top`, `this.width`

## Region.isRegionValid()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`, `this.#x2`, `this.#y1`, `this.#y2`

## Region.resetDimensions()
- 位置: L348-355
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`, `this.#x2`, `this.#xOffset`, `this.#y1`, `this.#y2`, `this.#yOffset`

## Region.sortCoords()
- 位置: L360-367
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`, `this.#x2`, `this.#y1`, `this.#y2`

## Region.shift()
- 位置: L373-392
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#windowDimensions.scrollHeight`, `this.#windowDimensions.scrollWidth`, `this.bottom`, `this.left`, `this.right`, `this.top`

## Region.distance()
- 位置: L397-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.pow()`, `Math.sqrt()`
- 参照: `this.height`, `this.width`

## Region.xOffset()
- 位置: L401-403
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#xOffset`

## Region.xOffset()
- 位置: L404-406
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#xOffset`

## Region.yOffset()
- 位置: L408-410
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#yOffset`

## Region.yOffset()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#yOffset`

## Region.top()
- 位置: L415-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 参照: `this.#y1`, `this.#y2`

## Region.top()
- 位置: L418-420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clampY()`
- 参照: `this.#y1`

## Region.left()
- 位置: L422-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 参照: `this.#x1`, `this.#x2`

## Region.left()
- 位置: L425-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clampX()`
- 参照: `this.#x1`

## Region.right()
- 位置: L429-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 参照: `this.#x1`, `this.#x2`

## Region.right()
- 位置: L432-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clampX()`
- 参照: `this.#x2`

## Region.bottom()
- 位置: L436-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 参照: `this.#y1`, `this.#y2`

## Region.bottom()
- 位置: L439-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clampY()`
- 参照: `this.#y2`

## Region.width()
- 位置: L443-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 参照: `this.#x1`, `this.#x2`

## Region.height()
- 位置: L446-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 参照: `this.#y1`, `this.#y2`

## Region.x1()
- 位置: L450-452
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`

## Region.x2()
- 位置: L453-455
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x2`

## Region.y1()
- 位置: L456-458
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#y1`

## Region.y2()
- 位置: L459-461
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#y2`

## WindowDimensions.dimensions()
- 位置: L477-511
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dimensions.clientHeight`, `dimensions.clientWidth`, `dimensions.devicePixelRatio`, `dimensions.scrollHeight`, `dimensions.scrollMaxX`, `dimensions.scrollMaxY`, `dimensions.scrollMinX`, `dimensions.scrollMinY`, `dimensions.scrollWidth`, `dimensions.scrollX`, `dimensions.scrollY`, `this.#clientHeight`, `this.#clientWidth`, `this.#devicePixelRatio`, `this.#scrollHeight`, `this.#scrollMaxX`, `this.#scrollMaxY`, `this.#scrollMinX`, `this.#scrollMinY`, `this.#scrollWidth`, `this.#scrollX`, `this.#scrollY`

## WindowDimensions.dimensions()
- 位置: L513-529
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.clientHeight`, `this.clientWidth`, `this.devicePixelRatio`, `this.pageScrollX`, `this.pageScrollY`, `this.scrollHeight`, `this.scrollMaxX`, `this.scrollMaxY`, `this.scrollMinX`, `this.scrollMinY`, `this.scrollWidth`, `this.scrollX`, `this.scrollY`

## WindowDimensions.clientWidth()
- 位置: L531-533
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#clientWidth`

## WindowDimensions.clientHeight()
- 位置: L535-537
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#clientHeight`

## WindowDimensions.scrollWidth()
- 位置: L539-541
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollWidth`

## WindowDimensions.scrollHeight()
- 位置: L543-545
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollHeight`

## WindowDimensions.scrollX()
- 位置: L547-549
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollX`, `this.scrollMinX`

## WindowDimensions.pageScrollX()
- 位置: L551-553
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollX`

## WindowDimensions.scrollY()
- 位置: L555-557
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollY`, `this.scrollMinY`

## WindowDimensions.pageScrollY()
- 位置: L559-561
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollY`

## WindowDimensions.scrollMinX()
- 位置: L563-565
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollMinX`

## WindowDimensions.scrollMinY()
- 位置: L567-569
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollMinY`

## WindowDimensions.scrollMaxX()
- 位置: L571-573
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollMaxX`

## WindowDimensions.scrollMaxY()
- 位置: L575-577
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#scrollMaxY`

## WindowDimensions.devicePixelRatio()
- 位置: L579-581
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#devicePixelRatio`

## WindowDimensions.isInViewport()
- 位置: L583-596
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.clientHeight`, `this.clientWidth`, `this.scrollX`, `this.scrollY`

## WindowDimensions.reset()
- 位置: L598-609
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#clientHeight`, `this.#clientWidth`, `this.#scrollHeight`, `this.#scrollMaxX`, `this.#scrollMaxY`, `this.#scrollMinX`, `this.#scrollMinY`, `this.#scrollWidth`, `this.#scrollX`, `this.#scrollY`
