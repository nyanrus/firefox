# browser/components/customizableui/DragPositionManager.sys.mjs

source: browser/components/customizableui/DragPositionManager.sys.mjs
source-hash: e40a321055d9fb8fb8016e9140c9b273d209f715
lines: 477

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## AreaPositionManager.constructor()
- 位置: L61-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DOMRectReadOnly.fromRect()`, `aContainer.getBoundingClientRect()`, `this.update()`
- 参照: `aContainer.documentGlobal.RTL_UI`, `this.#containerInfo`, `this.#rtl`

## AreaPositionManager.update()
- 位置: L96-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lazyStoreGet()`
- 参照: `aContainer.children`, `child.hidden`, `coordinates.height`, `coordinates.left`, `last.left`, `this.#containerInfo.width`, `this.#heightToWidthFactor`, `this.#horizontalDistance`

## AreaPositionManager.find()
- 位置: L141-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#lazyStoreGet()`
- 条件付き依存: `if (closest)` → `this.#lazyStoreGet()`
- 参照: `Number.MAX_VALUE`, `aContainer.children`, `closest.nextElementSibling`, `coordinates.x`, `coordinates.y`, `targetBounds.bottom`, `targetBounds.top`, `this.#containerInfo.left`, `this.#containerInfo.top`, `this.#heightToWidthFactor`, `this.#rtl`

## AreaPositionManager.insertPlaceholder()
- 位置: L203-246
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aIsFromThisArea && !this.#lastPlaceholderInsertion)` → `child.setAttribute()`
- 条件付き依存: `if (isShifted)` → `this.#diffWithNext()`
- 条件付き依存: `if ( aContainer.lastElementChild && aIsFromThisArea && !this.#lastPlaceholderInsertion )` → `aContainer.lastElementChild.getBoundingClientRect()`
- 条件付き依存: `if ( aContainer.lastElementChild && aIsFromThisArea && !this.#lastPlaceholderInsertion )` → `child.removeAttribute()`
- 参照: `aContainer.children`, `aContainer.lastElementChild`, `child.hidden`, `child.style.transform`, `this.#lastPlaceholderInsertion`

## AreaPositionManager.clearPlaceholders()
- 位置: L259-276
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNoTransition)` → `child.setAttribute()`
- 条件付き依存: `if (aNoTransition)` → `child.getBoundingClientRect()`
- 条件付き依存: `if (aNoTransition)` → `child.removeAttribute()`
- 参照: `aContainer.children`, `child.style.transform`, `this.#lastPlaceholderInsertion`

## AreaPositionManager.#diffWithNext()
- 位置: L290-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getVisibleSiblingForDirection()`, `this.#lazyStoreGet()`
- 条件付き依存: `if (next)` → `this.#lazyStoreGet()`
- 条件付き依存: `if (!(next))` → `this.#firstInRow()`
- 条件付き依存: `if (!(aNode == firstNode))` → `this.#moveNextBasedOnPrevious()`
- 参照: `aSize.height`, `aSize.width`, `nodeBounds.top`, `otherBounds.top`, `this.#horizontalDistance`, `this.#rtl`

## AreaPositionManager.#moveNextBasedOnPrevious()
- 位置: L348-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getVisibleSiblingForDirection()`, `this.#lazyStoreGet()`
- 条件付き依存: `if ( (!this.#rtl && xDiff + aNodeBounds.right > bound) || (this.#rtl && xDiff + aNodeBounds.left < bound) )` → `this.#lazyStoreGet()`
- 参照: `aNodeBounds.left`, `aNodeBounds.right`, `this.#containerInfo`, `this.#rtl`

## AreaPositionManager.#lazyStoreGet()
- 位置: L377-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#nodePositionStore.get()`
- 条件付き依存: `if (!rect)` → `DOMRectReadOnly.fromRect()`
- 条件付き依存: `if (!rect)` → `aNode.getBoundingClientRect()`
- 条件付き依存: `if (!rect)` → `this.#nodePositionStore.set()`

## AreaPositionManager.#firstInRow()
- 位置: L398-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `this.#getVisibleSiblingForDirection()`, `this.#lazyStoreGet()`
- 参照: `this.#lazyStoreGet(aNode).top`, `this.#lazyStoreGet(prev).bottom`

## AreaPositionManager.#getVisibleSiblingForDirection()
- 位置: L424-430
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `rv.hidden`

## start()
- 位置: L445-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.getElementById()`, `gManagers.get()`
- 条件付き依存: `if (positionManager)` → `positionManager.update()`
- 条件付き依存: `if (!(positionManager))` → `gManagers.set()`

## stop()
- 位置: L460-462
- 役割: (未記入)
- 触るとき: (未記入)

## getManagerForArea()
- 位置: L471-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gManagers.get()`
