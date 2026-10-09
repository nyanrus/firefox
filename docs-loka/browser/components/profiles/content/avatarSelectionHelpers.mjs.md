# browser/components/profiles/content/avatarSelectionHelpers.mjs

source: browser/components/profiles/content/avatarSelectionHelpers.mjs
source-hash: a5797a065d41afdc06d7d8b9f630e75c3174bc2c
lines: 311

## <module>
- 役割: (未記入)

## Region.constructor()
- 位置: L25-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetDimensions()`
- 参照: `this.#viewDimensions`

## Region.#dimensions()
- 位置: L42-60
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dims == null)` → `this.resetDimensions()`
- 参照: `dims.bottom`, `dims.left`, `dims.right`, `dims.top`, `this.bottom`, `this.left`, `this.right`, `this.top`

## Region.resizeToSquare()
- 位置: L71-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.forceSquare()`
- 参照: `this.#dimensions`, `this.#viewDimensions.height`, `this.#viewDimensions.width`, `this.bottom`, `this.left`, `this.right`, `this.top`

## Region.dimensions()
- 位置: L133-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.bottom`, `this.height`, `this.left`, `this.radius`, `this.right`, `this.top`, `this.width`

## Region.resetDimensions()
- 位置: L145-150
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`, `this.#x2`, `this.#y1`, `this.#y2`

## Region.sortCoords()
- 位置: L155-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`, `this.#x2`, `this.#y1`, `this.#y2`

## Region.forceSquare()
- 位置: L164-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 参照: `this.#viewDimensions.height`, `this.#viewDimensions.width`, `this.bottom`, `this.height`, `this.left`, `this.right`, `this.top`, `this.width`

## Region.top()
- 位置: L213-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 参照: `this.#y1`, `this.#y2`

## Region.top()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 参照: `this.#viewDimensions.height`, `this.#y1`

## Region.left()
- 位置: L220-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 参照: `this.#x1`, `this.#x2`

## Region.left()
- 位置: L223-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 参照: `this.#viewDimensions.width`, `this.#x1`

## Region.right()
- 位置: L227-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 参照: `this.#x1`, `this.#x2`

## Region.right()
- 位置: L230-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 参照: `this.#viewDimensions.width`, `this.#x2`

## Region.bottom()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 参照: `this.#y1`, `this.#y2`

## Region.bottom()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 参照: `this.#viewDimensions.height`, `this.#y2`

## Region.width()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 参照: `this.#x1`, `this.#x2`

## Region.height()
- 位置: L244-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 参照: `this.#y1`, `this.#y2`

## Region.radius()
- 位置: L248-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`
- 参照: `this.width`

## Region.x1()
- 位置: L252-254
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x1`

## Region.x2()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#x2`

## Region.y1()
- 位置: L258-260
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#y1`

## Region.y2()
- 位置: L261-263
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#y2`

## ViewDimensions.dimensions()
- 位置: L274-284
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dimensions.devicePixelRatio`, `dimensions.height`, `dimensions.width`, `this.#devicePixelRatio`, `this.#height`, `this.#width`

## ViewDimensions.dimensions()
- 位置: L286-292
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.devicePixelRatio`, `this.height`, `this.width`

## ViewDimensions.width()
- 位置: L294-296
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#width`

## ViewDimensions.height()
- 位置: L298-300
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#height`

## ViewDimensions.devicePixelRatio()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#devicePixelRatio`

## ViewDimensions.reset()
- 位置: L306-309
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#height`, `this.#width`
