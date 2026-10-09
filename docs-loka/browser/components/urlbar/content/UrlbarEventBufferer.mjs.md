# browser/components/urlbar/content/UrlbarEventBufferer.mjs

source: browser/components/urlbar/content/UrlbarEventBufferer.mjs
source-hash: 4172241eafb52c6157adb6880e30a98c526f8702
lines: 414

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## UrlbarEventBufferer.logger()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getLogger()`
- 参照: `this.#logger`

## UrlbarEventBufferer.DEFERRING_TIMEOUT_MS()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`

## UrlbarEventBufferer.constructor()
- 位置: L65-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `performance.now()`, `this.input.controller.addListener()`, `this.input.inputField.addEventListener()`
- 参照: `QUERY_STATUS.UKNOWN`, `this.#lastQuery`, `this.input`

## UrlbarEventBufferer.queryStarting()
- 位置: L93-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `performance.now()`
- 条件付き依存: `if (this.#deferringTimeout)` → `clearTimeout()`
- 参照: `QUERY_STATUS.RUNNING`, `this.#deferringTimeout`, `this.#lastQuery`

## UrlbarEventBufferer.onQueryCancelled()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `QUERY_STATUS.COMPLETE`, `this.#lastQuery.status`

## UrlbarEventBufferer.onQueryFinished()
- 位置: L111-113
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `QUERY_STATUS.COMPLETE`, `this.#lastQuery.status`

## UrlbarEventBufferer.onQueryResults()
- 位置: L120-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.replayDeferredEvents()`
- 参照: `QUERY_STATUS.RUNNING_GOT_ALL_HEURISTIC_RESULTS`, `queryContext.pendingHeuristicProviders.size`, `this.#lastQuery.context`, `this.#lastQuery.status`

## UrlbarEventBufferer.handleEvent()
- 位置: L141-152
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "blur")` → `this.logger.debug()`
- 条件付き依存: `if (this.#deferringTimeout)` → `clearTimeout()`
- 参照: `event.type`, `this.#deferringTimeout`, `this.#eventsQueue.length`

## UrlbarEventBufferer.maybeDeferEvent()
- 位置: L162-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `this.shouldDeferEvent()`
- 条件付き依存: `if (this.shouldDeferEvent(event))` → `this.deferEvent()`

## UrlbarEventBufferer.deferEvent()
- 位置: L181-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#eventsQueue.find()`, `this.#eventsQueue.push()`, `this.logger.debug()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `performance.now()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `setTimeout()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `this.replayDeferredEvents()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `Math.max()`
- 参照: `UrlbarEventBufferer.DEFERRING_TIMEOUT_MS`, `event.keyCode`, `event.type`, `item.event`, `this.#deferringTimeout`, `this.#lastQuery.context.searchString`, `this.#lastQuery.startDate`

## UrlbarEventBufferer.replayDeferredEvents()
- 位置: L216-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this.#eventsQueue.shift()`, `this.isSafeToPlayDeferredEvent()`, `this.replayDeferredEvents()`
- 条件付き依存: `if (searchString == this.#lastQuery.context.searchString)` → `callback()`
- 参照: `this.#eventsQueue`, `this.#eventsQueue.length`, `this.#lastQuery.context.searchString`

## UrlbarEventBufferer.shouldDeferEvent()
- 位置: L246-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DEFERRED_KEY_CODES.has()`, `UrlbarContentUtils.getPlatform()`, `performance.now()`, `this.isSafeToPlayDeferredEvent()`
- 条件付き依存: `if (DEFERRED_KEY_CODES.has(event.keyCode))` → `this.input.controller.keyEventMovesCaret()`
- 参照: `KeyEvent.DOM_VK_TAB`, `UrlbarEventBufferer.DEFERRING_TIMEOUT_MS`, `event.ctrlKey`, `event.key`, `event.keyCode`, `this.#eventsQueue.length`, `this.#lastQuery.startDate`, `this.input.isComposing`, `this.input.view.isOpen`, `this.waitingDeferUserSelectionProviders`

## UrlbarEventBufferer.isDeferringEvents()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#eventsQueue.length`

## UrlbarEventBufferer.waitingDeferUserSelectionProviders()
- 位置: L312-314
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastQuery.context?.deferUserSelectionProviders.size`

## UrlbarEventBufferer.isSafeToPlayDeferredEvent()
- 位置: L326-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_RETURN`, `QUERY_STATUS.COMPLETE`, `QUERY_STATUS.RUNNING`, `QUERY_STATUS.UKNOWN`, `event.ctrlKey`, `event.key`, `event.keyCode`, `selectedResult.heuristic`, `this.#lastQuery.status`, `this.input.view.isOpen`, `this.input.view.selectedResult`, `this.lastResultIsSelected`, `this.waitingDeferUserSelectionProviders`

## UrlbarEventBufferer.lastResultIsSelected()
- 位置: L376-384
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `results.length`, `this.#lastQuery.context.results`, `this.input.view.selectedResult`
