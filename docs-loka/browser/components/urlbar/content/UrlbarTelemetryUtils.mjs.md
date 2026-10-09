# browser/components/urlbar/content/UrlbarTelemetryUtils.mjs

source: browser/components/urlbar/content/UrlbarTelemetryUtils.mjs
source-hash: 9596698cf94409785fb1d8507f3e1bade6c1a580
lines: 876

## <module>
- 役割: (未記入)

## UrlbarTelemetryUtils.actionFromEvent()
- 位置: L44-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isInstance()`
- 条件付き依存: `if (UrlbarShared.isInstance(event, MouseEvent))` → `(event.target).classList.contains()`
- 参照: `details.element.dataset.command`, `details.element?.dataset.command`, `details.selType`, `event.target`, `event.type`

## UrlbarTelemetryUtils.modifiersFromEvent()
- 位置: L88-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allModifiers .filter()`, `allModifiers .filter(m => inputEvent.getModifierState(m)) .map()`, `allModifiers .filter(m => inputEvent.getModifierState(m)) .map(m => m.toLowerCase()) .join()`, `inputEvent.getModifierState()`, `m.toLowerCase()`
- 参照: `inputEvent?.getModifierState`

## UrlbarTelemetryUtils.parseSearchString()
- 位置: L114-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchString .substring()`, `searchString .substring(0, UrlbarShared.MAX_TEXT_LENGTH) .trim()`, `searchString .substring(0, UrlbarShared.MAX_TEXT_LENGTH) .trim() .split()`, `searchString .substring(0, UrlbarShared.MAX_TEXT_LENGTH) .trim() .split(UrlbarShared.REGEXP_SPACES) .filter()`, `searchString.length.toString()`, `searchWords.length.toString()`
- 参照: `UrlbarShared.MAX_TEXT_LENGTH`, `UrlbarShared.REGEXP_SPACES`

## UrlbarTelemetryUtils.startInteractionType()
- 位置: L141-156
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "input")` → `UrlbarShared.isPasteEvent()`
- 参照: `event.type`

## UrlbarTelemetryUtils.collectSnapshot()
- 位置: L175-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actionFromEvent()`, `this.modifiersFromEvent()`, `this.parseSearchString()`
- 条件付き依存: `if (method == "engagement")` → `[ "dismiss", "inaccurate_location", "not_interested", "not_now", "opt_in", "show_less_frequently", ].includes()`
- 参照: `details.element?.dataset.action`, `details.isSessionOngoing`, `details.result?.payload.providesSearchMode`, `details.result?.providerName`, `details.result?.rowIndex`, `details.searchString`, `details.selType`, `startEventInfo.interactionType`

## UrlbarTelemetryUtils.engagementData()
- 位置: L254-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `input.getSearchSource()`
- 参照: `input.searchMode`, `view?.isOpen`, `view?.visibleResults`

## UrlbarTelemetryUtils.smartbarData()
- 位置: L271-280
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `smartbar.conversationTelemetryInfo?.chat_id`, `smartbar.modelName`, `smartbar.smartbarAction`

## UrlbarTelemetryUtils.exposureEntry()
- 位置: L292-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarPrefs.get("keywordExposureResults").has()`, `UrlbarShared.searchEngagementTelemetryType()`
- 参照: `queryContext.isPrivate`, `queryContext.trimmedLowerCaseSearchString`

## UrlbarTelemetryUtils.exposureTerminal()
- 位置: L315-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `endResults?.includes()`
- 参照: `queryContext?.results`, `result.isHiddenExposure`

## UrlbarTelemetryUtils.recordedEngagementToWire()
- 位置: L335-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data.visibleResults?.map()`, `r.toWire()`, `result?.toWire()`
- 参照: `data.internalDetails`, `internalDetails.element`, `internalDetails.event`

## UrlbarTelemetryUtils.recordedEngagementFromWire()
- 位置: L365-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarResult.fromWire()`, `wire.visibleResults?.map()`
- 参照: `wire.internalDetails`, `wire.internalDetails.result`

## UrlbarTelemetryUtils.collectBounceSnapshot()
- 位置: L400-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actionFromEvent()`, `this.parseSearchString()`
- 参照: `details.location`, `details.result?.providerName`, `details.result?.rowIndex`, `details.searchMode`, `details.searchSource`, `details.searchString`, `details.selType`, `details.windowMode`, `startEventInfo.interactionType`

## UrlbarTelemetryUtils.getSearchMode()
- 位置: L450-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `UrlbarShared.LOCAL_SEARCH_MODES.find( m => m.source == searchMode.source )?.telemetryLabel`, `m.source`, `searchMode.engineName`, `searchMode.source`

## UrlbarTelemetryUtils.#isRefined()
- 位置: L463-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `intersect()`

## intersect()
- 位置: L467-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setA.values()`, `setB.has()`
- 参照: `setA.size`

## UrlbarTelemetryUtils.getInteractionType()
- 位置: L495-540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy?.UrlbarUtils.isPersistedSearchTermsEnabled()`, `this.#isRefined()`
- 参照: `searchMode?.entry`, `startEventInfo.interactionType`

## UrlbarTelemetryUtils.buildEventInfo()
- 位置: L597-766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(selIndex + 1).toString()`, `UrlbarPrefs.get()`, `UrlbarShared.searchEngagementTelemetryAction()`, `UrlbarShared.searchEngagementTelemetryGroup()`, `UrlbarShared.searchEngagementTelemetryType()`, `console.error()`, `numChars.toString()`, `numResults.toString()`, `numWords.toString()`, `this.getSearchMode()`, `viewTime.toString()`, `visibleResults .map()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryAction(r)) .filter()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryAction(r)) .filter(v => v) .join()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryGroup(r)) .join()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryType(r)) .join()`
- 条件付き依存: `if (selType == "action")` → `UrlbarShared.searchEngagementTelemetryAction()`
- 条件付き依存: `if (previousEvent == "engagement")` → `UrlbarShared.searchEngagementTelemetryType()`
- 参照: `visibleResults.length`

## UrlbarTelemetryUtils.buildRecordedEngagement()
- 位置: L785-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildRecorded()`
- 参照: `snapshot.method`

## UrlbarTelemetryUtils.buildRecordedDisableCandidate()
- 位置: L817-830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildRecorded()`
- 参照: `this.#buildRecorded( "disable", snapshot, engagementData, smartbarData, previousSearchWords ).built`

## UrlbarTelemetryUtils.#buildRecorded()
- 位置: L832-874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buildEventInfo()`, `this.getInteractionType()`
- 参照: `engagementData.searchMode`, `engagementData.viewIsOpen`, `engagementData.visibleResults`, `interactionResult.interaction`, `interactionResult.previousSearchWords`, `internalDetails.location`, `internalDetails.pickedActionKey`, `internalDetails.provider`, `internalDetails.searchMode`, `internalDetails.searchSource`, `internalDetails.selIndex`, `internalDetails.selType`, `internalDetails.windowMode`, `smartbarData.chatId`, `smartbarData.intent`, `smartbarData.model`, `snapshot.action`, `snapshot.modifiers`, `snapshot.numChars`, `snapshot.numWords`, `snapshot.searchWords`, `snapshot.startEventInfo`
