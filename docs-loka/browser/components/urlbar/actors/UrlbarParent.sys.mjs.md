# browser/components/urlbar/actors/UrlbarParent.sys.mjs

source: browser/components/urlbar/actors/UrlbarParent.sys.mjs
source-hash: 9fce7a61a8af8519313f5a6362f595d4b8045073
lines: 366

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarParent.receiveMessage()
- 位置: L52-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.toWire()`, `controller .getHeuristicResult()`, `controller .getHeuristicResult( lazy.UrlbarQueryContext.fromWire(message.data.queryContext) ) .then()`, `controller .resolveFallbackNavigation()`, `controller .resolveFallbackNavigation(message.data.details) .then()`, `controller .startQuery()`, `controller .startQuery( lazy.UrlbarQueryContext.fromWire(message.data.queryContext) ) .then()`, `controller.addToInputHistory()`, `controller.cancelQuery()`, `controller.checkKeywordURIFixup()`, `controller.clearAutofillBackspaceEntryForUrl()`, `controller.clearLastQueryContextCache()`, `controller.dismissAutofill()`, `controller.focusBrowser()`, `controller.getEngineIconURL()`, `controller.handleAutofillReintegration()`, `controller.initEngineStore()`, `controller.loadURL()`, `controller.markEngineAsUsed()`, `controller.onBeforeSelection()`, `controller.onSelection()`, `controller.openContainerCreationPanel()`, `controller.openPreferences()`, `controller.openSERP()`, `controller.openSearchForm()`, `controller.recordAutofillBackspace()`, `controller.recordAutofillDeletion()`, `controller.recordEngagement()`, `controller.recordSearch()`, `controller.recordSearchForm()`, `controller.recordSearchInOpenedTab()`, `controller.recordSearchMode()`, `controller.recordZeroPrefix()`, `controller.removeResult()`, `controller.resetEngagement()`, `controller.setLastQueryContextCache()`, `controller.speculativeConnect()`, `controller.startTrackingBuiltBounce()`, `controller.switchToTab()`, `lazy.UrlbarQueryContext.fromWire()`, `outcome.heuristicResult.toWire()`, `result?.toWire()`, `this.#messageControllers.get()`, `this.#resultFromWire()`
- 条件付き依存: `if (message.name == "GetContainers")` → `UrlbarContentUtils.getContainers()`
- 条件付き依存: `if (message.name == "Init")` → `controller.setChild()`
- 条件付き依存: `if (message.name == "Init")` → `makeChildControllerProxy()`
- 条件付き依存: `if (message.name == "Init")` → `this.#messageControllers.set()`
- 条件付き依存: `if (message.name == "Destroy")` → `this.#messageControllers.get(instanceId)?.destroy()`
- 条件付き依存: `if (message.name == "Destroy")` → `this.#messageControllers.get()`
- 条件付き依存: `if (message.name == "Destroy")` → `this.#messageControllers.delete()`
- 参照: `lazy.UrlbarParentController`, `message.data`, `message.data.action`, `message.data.browserId`, `message.data.details`, `message.data.engineId`, `message.data.engineName`, `message.data.entrypoint`, `message.data.extraArgs`, `message.data.inBackground`, `message.data.input`, `message.data.kind`, `message.data.loadData`, `message.data.options`, `message.data.paneID`, `message.data.payload`, `message.data.queryContext`, `message.data.reason`, `message.data.result`, `message.data.searchData`, `message.data.searchMode`, `message.data.searchString`, `message.data.searchTerms`, `message.data.url`, `message.data.whenReady`, `message.data.where`, `message.data.wire`, `message.name`, `outcome.heuristicResult`

## UrlbarParent.#resultFromWire()
- 位置: L260-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarResult.fromWire()`
- 参照: `controller.liveResults`

## UrlbarParent.didDestroy()
- 位置: L264-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.destroy()`, `this.#messageControllers.clear()`, `this.#messageControllers.values()`

## sendToChild()
- 位置: L290-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`
- 参照: `actor.manager`, `actor.manager.isClosed`

## makeChildControllerProxy()
- 位置: L332-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeProxy()`

## makeProxy()
- 位置: L351-365
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Symbol.toStringTag`, `UrlbarShared.INVOKABLE_CONTENT_ACTIONS`

## proxy[method]()
- 位置: L355-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sendToChild()`
