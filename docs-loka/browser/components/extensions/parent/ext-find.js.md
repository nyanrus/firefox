# browser/components/extensions/parent/ext-find.js

source: browser/components/extensions/parent/ext-find.js
source-hash: 4752b8b3dddb29b21880047b09f69d29b01a920a
lines: 271

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getActorForBrowsingContext()
- 位置: L17-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowGlobal.getActor()`
- 参照: `browsingContext.currentWindowGlobal`

## getTopLevelActor()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActorForBrowsingContext()`
- 参照: `browser.browsingContext`

## gatherActors()
- 位置: L26-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gatherActors()`, `getActorForBrowsingContext()`, `list.push()`
- 条件付き依存: `if (actor)` → `list.push()`
- 参照: `browsingContext.children`

## mergeFindResults()
- 位置: L42-78
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (params.includeRangeData && item.result.rangeData)` → `finalResult.rangeData.push()`
- 条件付き依存: `if (params.includeRectData && item.result.rectData)` → `finalResult.rectData.push()`
- 参照: `finalResult.count`, `finalResult.rangeData`, `finalResult.rectData`, `item.result.count`, `item.result.rangeData`, `item.result.rectData`, `params.includeRangeData`, `params.includeRectData`, `range.framePos`

## sendMessageToAllActors()
- 位置: L80-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `gatherActors()`
- 参照: `browser.browsingContext`

## getFindResultsForActor()
- 位置: async L86-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findContext.actor.sendQuery()`
- 参照: `findContext.result`

## queryAllActors()
- 位置: L94-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `gatherActors()`, `getFindResultsForActor()`, `promises.push()`
- 参照: `browser.browsingContext`

## collectFindResults()
- 位置: async L102-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findResults.set()`, `getTopLevelActor()`, `mergeFindResults()`, `queryAllActors()`

## runHighlight()
- 位置: async L108-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.reject()`, `findResults.get()`, `getTopLevelActor()`
- 条件付き依存: `if (!list)` → `Promise.reject()`
- 条件付き依存: `if (highlightAll)` → `highlightPromises.push()`
- 条件付き依存: `if (highlightAll)` → `actor.sendQuery()`
- 条件付き依存: `if (!foundResults && index < list[c].result.count)` → `highlightPromises.push()`
- 条件付き依存: `if (!foundResults && index < list[c].result.count)` → `actor.sendQuery()`
- 条件付き依存: `if (!(!foundResults && index < list[c].result.count))` → `highlightPromises.push()`
- 条件付き依存: `if (!(!foundResults && index < list[c].result.count))` → `actor.sendQuery()`
- 条件付き依存: `if (hasResults)` → `responses.includes()`
- 条件付き依存: `if (responses.includes("OutOfRange") || index >= 0)` → `Promise.reject()`
- 条件付き依存: `if (!(responses.includes("OutOfRange") || index >= 0))` → `responses.includes()`
- 参照: `list.length`, `list[c].actor`, `list[c].result.count`, `params.rangeIndex`

## runFindOperation()
- 位置: L170-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `["about", "chrome", "resource"].includes()`, `tabTracker.getId()`, `tabTracker.getTab()`
- 条件付き依存: `if ( !context.privateBrowsingAllowed && PrivateBrowsingUtils.isBrowserPrivate(browser) )` → `Promise.reject()`
- 条件付き依存: `if ( tab.linkedBrowser.contentPrincipal.isSystemPrincipal || (["about", "chrome", "resource"].includes( tab.linkedBrowser.currentURI.scheme ) && tab.linkedBrowse...)` → `Promise.reject()`
- 条件付き依存: `if (message == "HighlightResults")` → `runHighlight()`
- 条件付き依存: `if (message == "CollectResults")` → `findResults.delete()`
- 条件付き依存: `if (message == "CollectResults")` → `getTopLevelActor()`
- 条件付き依存: `if (message == "CollectResults")` → `collectFindResults()`
- 参照: `context.privateBrowsingAllowed`, `tab.linkedBrowser`, `tab.linkedBrowser.contentPrincipal.isSystemPrincipal`, `tab.linkedBrowser.currentURI.scheme`, `tab.linkedBrowser.currentURI.spec`, `tabTracker.activeTab`

## getAPI()
- 位置: L202-269
- 役割: (未記入)
- 触るとき: (未記入)

## find()
- 位置: L224-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `runFindOperation()`
- 参照: `params.queryphrase`

## highlightResults()
- 位置: L245-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `runFindOperation()`

## removeHighlighting()
- 位置: L257-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `sendMessageToAllActors()`, `tabTracker.getTab()`
- 参照: `context.privateBrowsingAllowed`, `tab.linkedBrowser`, `tabTracker.activeTab`
