# browser/components/qrcode/QRCodeWorker.worker.mjs

source: browser/components/qrcode/QRCodeWorker.worker.mjs
source-hash: 9a013be6a2db516caca799797995c6705c15ee01
lines: 325

## <module>
- 役割: (未記入)

## QRCodeWorkerImpl.constructor()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connectToPromiseWorker()`

## QRCodeWorkerImpl.#getMargin()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)

## QRCodeWorkerImpl.#getCanvasSize()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getMargin()`

## QRCodeWorkerImpl.#getFinderPatternOrigins()
- 位置: L57-63
- 役割: (未記入)
- 触るとき: (未記入)

## QRCodeWorkerImpl.#forEachVisibleDarkModule()
- 位置: L74-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.hypot()`, `callback()`, `isInFinderPatternCorners()`
- 参照: `matrix.length`, `placement.centerX`, `placement.centerY`, `placement.clearRadius`, `placement.showLogo`

## isInFinderPatternCorners()
- 位置: L76-79
- 役割: (未記入)
- 触るとき: (未記入)

## QRCodeWorkerImpl.#drawFinderPattern()
- 位置: L109-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctx.beginPath()`, `ctx.fill()`, `ctx.roundRect()`
- 参照: `ctx.fillStyle`

## QRCodeWorkerImpl.#drawQRBodyToCanvas()
- 位置: L149-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctx.arc()`, `ctx.beginPath()`, `ctx.fill()`, `ctx.fillRect()`, `this.#drawFinderPattern()`, `this.#forEachVisibleDarkModule()`, `this.#getCanvasSize()`, `this.#getFinderPatternOrigins()`, `this.#getMargin()`
- 参照: `Math.PI`, `ctx.fillStyle`, `matrix.length`

## QRCodeWorkerImpl.#getPreferredLogoSize()
- 位置: L178-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `Math.round()`

## QRCodeWorkerImpl.generateQRMatrix()
- 位置: L189-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QR.encodeToMatrix()`
- 参照: `QR.encodeToMatrix`

## QRCodeWorkerImpl.getLogoPlacement()
- 位置: L206-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.#getCanvasSize()`, `this.#getMargin()`, `this.#getPreferredLogoSize()`

## QRCodeWorkerImpl.generateFullQRCode()
- 位置: async L234-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QR.encodeToMatrix()`, `canvas.convertToBlob()`, `canvas.getContext()`, `new Uint8Array(arrayBuffer).toBase64()`, `pngBlob.arrayBuffer()`, `this.#drawQRBodyToCanvas()`, `this.#getCanvasSize()`, `this.#getMargin()`, `this.getLogoPlacement()`
- 条件付き依存: `if (placement.showLogo)` → `fetch()`
- 条件付き依存: `if (placement.showLogo)` → `response.blob()`
- 条件付き依存: `if (placement.showLogo)` → `Math.round()`
- 条件付き依存: `if (placement.showLogo)` → `globalThis.createImageBitmap()`
- 条件付き依存: `if (placement.showLogo)` → `ctx.drawImage()`
- 条件付き依存: `if (placement.showLogo)` → `logoBitmap.close()`
- 条件付き依存: `if (placement.showLogo)` → `console.warn()`
- 参照: `ctx.imageSmoothingEnabled`, `ctx.imageSmoothingQuality`, `placement.centerX`, `placement.centerY`, `placement.logoSize`, `placement.showLogo`, `response.ok`, `response.status`

## QRCodeWorkerImpl.#connectToPromiseWorker()
- 位置: L300-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.addEventListener()`, `worker.handleMessage()`
- 参照: `PromiseWorker.AbstractWorker`, `error.reason`, `worker.close`, `worker.dispatch`, `worker.postMessage`

## worker.dispatch()
- 位置: L303-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this[method]()`

## worker.close()
- 位置: L310-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.close()`

## worker.postMessage()
- 位置: L312-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.postMessage()`
