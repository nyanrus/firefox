# browser/components/urlbar/content/UrlbarParentControllerProxy.mjs

source: browser/components/urlbar/content/UrlbarParentControllerProxy.mjs
source-hash: e8dad112e99881c7b701ef12dcb3bfd70a12b155
lines: 515

## <module>
- 役割: (未記入)

## UrlbarParentControllerProxy.constructor()
- 位置: L38-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.registerMessagePathInput()`, `this.#port.sendAsyncMessage()`
- 参照: `input.isPrivate`, `input.sapName`, `this.#instanceId`

## UrlbarParentControllerProxy.setChild()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.registerChildController()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordEngagement()
- 位置: L68-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.resetEngagement()
- 位置: L78-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.startTrackingBuiltBounce()
- 位置: L92-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearchMode()
- 位置: L105-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordAutofillBackspace()
- 位置: L118-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordAutofillDeletion()
- 位置: L129-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.dismissAutofill()
- 位置: L136-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.clearAutofillBackspaceEntryForUrl()
- 位置: L151-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.handleAutofillReintegration()
- 位置: L164-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearchForm()
- 位置: L177-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearch()
- 位置: L190-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordSearchInOpenedTab()
- 位置: L204-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.recordZeroPrefix()
- 位置: L218-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.checkKeywordURIFixup()
- 位置: L234-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy._lastQueryContextWrapper()
- 位置: L243-245
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.startQuery()
- 位置: L257-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarQueryContext.fromWire()`, `queryContext.toWire()`, `this.#port .sendQuery()`, `this.#port .sendQuery("StartQuery", { instanceId: this.#instanceId, queryContext: queryContext.toWire(), }) .then()`
- 参照: `error?.name`, `this.#instanceId`, `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.getHeuristicResult()
- 位置: async L286-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarResult.fromWire()`, `queryContext.toWire()`, `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.resolveFallbackNavigation()
- 位置: async L301-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarResult.fromWire()`, `this.#port.sendQuery()`
- 参照: `outcome.heuristicResult`, `this.#instanceId`

## UrlbarParentControllerProxy.cancelQuery()
- 位置: L311-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.speculativeConnect()
- 位置: L326-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.toWire()`, `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.loadURL()
- 位置: L342-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.focusBrowser()
- 位置: L356-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.switchToTab()
- 位置: L369-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.addToInputHistory()
- 位置: L385-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.removeResult()
- 位置: L402-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.setLastQueryContextCache()
- 位置: L413-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`, `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.clearLastQueryContextCache()
- 位置: L421-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`, `this.#lastQueryContextWrapper`

## UrlbarParentControllerProxy.onBeforeSelection()
- 位置: L431-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.onSelection()
- 位置: L441-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.toWire()`, `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.initEngineStore()
- 位置: L451-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.getEngineIconURL()
- 位置: L460-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendQuery()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.markEngineAsUsed()
- 位置: L468-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openSERP()
- 位置: L476-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openSearchForm()
- 位置: L488-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openPreferences()
- 位置: L499-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`

## UrlbarParentControllerProxy.openContainerCreationPanel()
- 位置: L508-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#port.sendAsyncMessage()`
- 参照: `this.#instanceId`
