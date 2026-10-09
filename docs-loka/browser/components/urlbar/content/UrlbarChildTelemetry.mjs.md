# browser/components/urlbar/content/UrlbarChildTelemetry.mjs

source: browser/components/urlbar/content/UrlbarChildTelemetry.mjs
source-hash: 73fef3a888a18f2284a81e82aca222fb4137c935
lines: 375

## <module>
- 役割: (未記入)

## UrlbarChildTelemetry.constructor()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#controller`

## UrlbarChildTelemetry.start()
- 位置: L73-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarTelemetryUtils.startInteractionType()`, `validEvents.includes()`
- 条件付き依存: `if (this.#startEventInfo.interactionType == "topsites")` → `UrlbarTelemetryUtils.startInteractionType()`
- 条件付き依存: `if (!event)` → `console.error()`
- 条件付き依存: `if (this.#controller.input.sapName === "smartbar")` → `validEvents.push()`
- 条件付き依存: `if (!validEvents.includes(event.type))` → `console.error()`
- 条件付き依存: `if (!this.#controller.parentController._lastQueryContextWrapper)` → `this.#controller.parentController.setLastQueryContextCache()`
- 参照: `event.timeStamp`, `event.type`, `this.#controller.input.sapName`, `this.#controller.parentController._lastQueryContextWrapper`, `this.#startEventInfo`, `this.#startEventInfo.interactionType`, `this.#startEventInfo.searchString`

## UrlbarChildTelemetry.record()
- 位置: L141-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarTelemetryUtils.collectSnapshot()`, `console.error()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.engagementData()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.smartbarData()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.buildRecordedEngagement()`
- 条件付き依存: `if (snapshot)` → `engagementData.visibleResults.some()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.buildRecordedDisableCandidate()`
- 条件付き依存: `if (snapshot)` → `this.#resolveExposures()`
- 条件付き依存: `if (snapshot)` → `this.#controller.parentController.recordEngagement()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.recordedEngagementToWire()`
- 参照: `details.isSessionOngoing`, `engagementData.visibleResults`, `r.providerName`, `snapshot.internalDetails`, `snapshot.internalDetails.searchSource`, `snapshot.method`, `this.#controller`, `this.#handlingRecord`, `this.#previousSearchWords`, `this.#startEventInfo`, `view.queryContext`

## UrlbarChildTelemetry.discard()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#startEventInfo`

## UrlbarChildTelemetry.reset()
- 位置: L224-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.parentController.resetEngagement()`
- 参照: `this.#previousSearchWords`

## UrlbarChildTelemetry.addExposure()
- 位置: L235-239
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#addExposureInternal()`
- 参照: `result.exposureTelemetry`

## UrlbarChildTelemetry.addTentativeExposure()
- 位置: L247-251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#tentativeExposures.push()`
- 参照: `result.exposureTelemetry`

## UrlbarChildTelemetry.acceptTentativeExposures()
- 位置: L256-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addExposureInternal()`
- 参照: `this.#tentativeExposures`

## UrlbarChildTelemetry.discardTentativeExposures()
- 位置: L266-268
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#tentativeExposures`

## UrlbarChildTelemetry.#addExposureInternal()
- 位置: L270-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#exposureResults.has()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposureResults.add()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `UrlbarTelemetryUtils.exposureEntry()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposures.push()`

## UrlbarChildTelemetry.#resolveExposures()
- 位置: L292-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarTelemetryUtils.exposureTerminal()`, `exposures.map()`, `this.#exposureResults.delete()`
- 参照: `this.#exposures`, `this.#tentativeExposures`

## UrlbarChildTelemetry.startTrackingBounceEvent()
- 位置: async L321-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarTelemetryUtils.buildEventInfo()`, `UrlbarTelemetryUtils.collectBounceSnapshot()`, `UrlbarTelemetryUtils.engagementData()`, `UrlbarTelemetryUtils.getInteractionType()`, `UrlbarTelemetryUtils.smartbarData()`, `this.#controller.parentController.startTrackingBuiltBounce()`
- 参照: `engagementData.searchMode`, `engagementData.viewIsOpen`, `engagementData.visibleResults`, `smartbarData.chatId`, `smartbarData.intent`, `smartbarData.model`, `snapshot.action`, `snapshot.location`, `snapshot.numChars`, `snapshot.numWords`, `snapshot.provider`, `snapshot.searchMode`, `snapshot.searchWords`, `snapshot.selIndex`, `snapshot.selType`, `snapshot.startEventInfo`, `snapshot.visibleResults`, `snapshot.windowMode`, `this.#controller`, `this.#previousSearchWords`, `this.#startEventInfo`
