# browser/components/urlbar/actors/UrlbarParent.sys.mjs

source: browser/components/urlbar/actors/UrlbarParent.sys.mjs
source-hash: 9fce7a61a8af8519313f5a6362f595d4b8045073
lines: 366

## <module>
- 役割: urlbar のメッセージパス用アクターの親側。子からのメッセージを UrlbarParentController へ振り分け、子のコントローラーを代理するプロキシを作る。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarParent.receiveMessage()
- 位置: L52-248
- 役割: 子からのメッセージを名前で振り分ける。GetContainers はそのまま返し、Init と Destroy でコントローラーを作成・破棄する。その他は InstanceId に対応するコントローラーのメソッドを呼び、結果を返すものは Promise で返す。
- 触るとき: 子から親への新しいメッセージを追加する、または特定の操作がコントローラーに届かないときに見る。
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
- 役割: 子から来た結果の wire 形式を、コントローラーの liveResults を使って UrlbarResult に戻す。
- 触るとき: 結果オブジェクトの同一性が崩れる、または選択した結果が解決できないときに見る。
- 呼び出し先: `lazy.UrlbarResult.fromWire()`
- 参照: `controller.liveResults`

## UrlbarParent.didDestroy()
- 位置: L264-272
- 役割: ウィンドウグローバルが破棄されるとき、保持している全コントローラーを destroy して Map を空にする。
- 触るとき: ウィンドウを閉じた後にコントローラーが残る問題を調べるときに見る。
- 呼び出し先: `controller.destroy()`, `this.#messageControllers.clear()`, `this.#messageControllers.values()`

## sendToChild()
- 位置: L290-295
- 役割: マネージャーが無い、または閉じている場合は送信せず、そうでなければ子へ非同期メッセージを送る。
- 触るとき: ウィンドウを閉じた後に送信で例外が出る問題を調べるときに見る。
- 呼び出し先: `actor.sendAsyncMessage()`
- 参照: `actor.manager`, `actor.manager.isClosed`

## makeChildControllerProxy()
- 位置: L332-338
- 役割: 子側コントローラーの親側代理を作る。input と view の代理を含み、isProxy を真にする。
- 触るとき: 親側で子のコントローラーを呼ぶ代理に新しい対象を加えるときに見る。
- 呼び出し先: `makeProxy()`

## makeProxy()
- 位置: L351-365
- 役割: INVOKABLE_CONTENT_ACTIONS[target] に列挙されたメソッドごとに、子へ InvokeContentAction を送る転送関数を作る。
- 触るとき: 代理経由で呼べるメソッドを増やす、または代理の呼び出しが届かないときに見る。
- 参照: `Symbol.toStringTag`, `UrlbarShared.INVOKABLE_CONTENT_ACTIONS`

## proxy[method]()
- 位置: L355-361
- 役割: 引数を付けて sendToChild で InvokeContentAction を送る転送関数。
- 触るとき: 親から子へ転送される引数の形式を確かめるときに見る。
- 呼び出し先: `sendToChild()`
