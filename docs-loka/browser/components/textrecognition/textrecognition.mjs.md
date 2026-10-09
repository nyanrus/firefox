# browser/components/textrecognition/textrecognition.mjs

source: browser/components/textrecognition/textrecognition.mjs
source-hash: 54a4ecfdfce387d486a5b67d391a52078375357f
lines: 440

## <module>
- 役割: (未記入)
- 呼び出し先: `window.addEventListener()`, `window.docShell.chromeEventHandler.classList.add()`

## TextRecognitionModal.constructor()
- 位置: L29-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.textrecognitionError.add()`, `Glean.textRecognition.apiPerformance.cancel()`, `Glean.textRecognition.apiPerformance.stopAndAccumulate()`, `TextRecognitionModal.recordInteractionTime()`, `console.error()`, `document.querySelector()`, `document.querySelectorAll()`, `resultsPromise.then()`, `this.runClusteringAndUpdateUI()`, `this.setupCloseHandler()`, `this.setupLink()`, `this.showHeaderByID()`
- 条件付き依存: `if (results.length === 0)` → `this.showHeaderByID()`
- 条件付き依存: `if (results.length === 0)` → `Glean.textRecognition.apiPerformance.stopAndAccumulate()`
- 参照: `results.length`, `this.headerEls`, `this.linkEl`, `this.openLinkIn`, `this.resizeVertically`, `this.textEl`

## TextRecognitionModal.recordInteractionTime()
- 位置: L84-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.textRecognition.interactionTiming.start()`, `window.addEventListener()`

## finish()
- 位置: L87-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.textRecognition.interactionTiming.stopAndAccumulate()`, `window.removeEventListener()`

## TextRecognitionModal.recordTextLengthTelemetry()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.textRecognition.textLength.accumulateSingleSample()`

## TextRecognitionModal.setupCloseHandler()
- 位置: L111-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelector()`, `document .querySelector("#text-recognition-close") .addEventListener()`, `window.close()`

## TextRecognitionModal.setupLink()
- 位置: L122-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `Services.urlFormatter.formatURL()`, `event.preventDefault()`, `this.linkEl.addEventListener()`, `this.openLinkIn()`
- 参照: `this.linkEl.href`
- XPCOM: `Services.scriptSecurityManager` / `Services.urlFormatter`

## TextRecognitionModal.showHeaderByID()
- 位置: L139-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.resizeVertically()`
- 参照: `document.getElementById(id).style.display`, `header.style.display`, `this.headerEls`

## TextRecognitionModal.copy()
- 位置: L151-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/clipboardhelper;1"].getService()`, `clipboard.copyString()`
- 参照: `Ci.nsIClipboardHelper`
- XPCOM: `nsIClipboardHelper` / `@mozilla.org/widget/clipboardhelper;1`

## TextRecognitionModal.runClusteringAndUpdateUI()
- 位置: L164-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.sqrt()`, `TextRecognitionModal.copy()`, `TextRecognitionModal.recordTextLengthTelemetry()`, `centers.push()`, `densityCluster()`, `distSq.quantile()`, `document.createElement()`, `minOrMax()`, `text.trim()`, `this.textEl.appendChild()`
- 参照: `Math.max`, `Math.min`, `cluster.length`, `p.p1.x`, `p.p1.y`, `p.p2.x`, `p.p2.y`, `p.p3.x`, `p.p3.y`, `p.p4.x`, `p.p4.y`, `pCluster.className`, `pCluster.innerText`, `result.quad`, `text.length`, `this.textEl.style.display`

## densityCluster()
- 位置: L246-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `clusters.sort()`, `getNeighborsWithinDistance()`
- 条件付き依存: `if (newNeighbors.length >= minPoints)` → `neighbors.includes()`
- 条件付き依存: `if (!neighbors.includes(newNeighbor))` → `neighbors.push()`
- 条件付き依存: `if (typeof label === "number")` → `clusters[label].push()`
- 条件付き依存: `if (label === noiseLabel)` → `clusters.push()`
- 参照: `labels.length`, `neighbors.length`, `newNeighbors.length`, `points.length`

## getNeighborsWithinDistance()
- 位置: L348-369
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dx * dx + dy * dy < distanceSquared)` → `neighbors.push()`
- 参照: `points.length`

## DistanceSquared.constructor()
- 位置: L384-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#distances.set()`, `this.#getTupleID()`
- 参照: `list.length`, `this.#list`

## DistanceSquared.#getTupleID()
- 位置: L401-405
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#list.length`

## DistanceSquared.get()
- 位置: L414-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#distances.get()`, `this.#getTupleID()`

## DistanceSquared.quantile()
- 位置: L424-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `Math.round()`
- 条件付き依存: `if (!this.#distancesSorted)` → `[...this.#distances.values()].sort()`
- 条件付き依存: `if (!this.#distancesSorted)` → `this.#distances.values()`
- 参照: `this.#distancesSorted`, `this.#distancesSorted.length`
