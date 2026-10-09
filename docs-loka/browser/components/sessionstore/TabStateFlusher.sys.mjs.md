# browser/components/sessionstore/TabStateFlusher.sys.mjs

source: browser/components/sessionstore/TabStateFlusher.sys.mjs
source-hash: fcffc6be2656ba185bbf5e6f8a6ea184957375ce
lines: 144

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## flush()
- 位置: L19-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabStateFlusherInternal.flush()`

## flushWindow()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabStateFlusherInternal.flushWindow()`

## resolveAll()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabStateFlusherInternal.resolveAll()`

## initEntry()
- 位置: L57-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabStateFlusherInternal.initEntry()`, `new Promise(resolve => { entry.cancel = resolve; }).then()`
- 参照: `entry.cancel`, `entry.cancelPromise`

## flush()
- 位置: L73-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `Promise.resolve()`, `this._requests.get()`
- 条件付き依存: `if (browser && browser.frameLoader)` → `browser.frameLoader.requestTabStateFlush()`
- 条件付き依存: `if (!request)` → `this.initEntry()`
- 条件付き依存: `if (!request)` → `this._requests.set()`
- 参照: `browser.frameLoader`, `browser.permanentKey`, `request.cancelPromise`

## flushWindow()
- 位置: L103-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `window.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (window.gBrowser.getTabForBrowser(browser).linkedPanel)` → `promises.push()`
- 条件付き依存: `if (window.gBrowser.getTabForBrowser(browser).linkedPanel)` → `this.flush()`
- 参照: `window.gBrowser.browsers`, `window.gBrowser.getTabForBrowser(browser).linkedPanel`

## resolveAll()
- 位置: L127-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cancel()`, `this._requests.get()`, `this._requests.has()`
- 条件付き依存: `if (!success)` → `console.error()`
- 参照: `browser.permanentKey`
