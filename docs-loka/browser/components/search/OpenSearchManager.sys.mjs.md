# browser/components/search/OpenSearchManager.sys.mjs

source: browser/components/search/OpenSearchManager.sys.mjs
source-hash: 9cef0f93c090c991a7bdc340e16c3efbf19a411a
lines: 250

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _OpenSearchManager.constructor()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## _OpenSearchManager.observe()
- 位置: L55-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addMaybeOfferedEngine()`, `this.#removeMaybeOfferedEngine()`
- 参照: `engine.name`, `subject.wrappedJSObject`

## _OpenSearchManager.addEngine()
- 位置: L87-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engines.push()`, `lazy.SearchService.getEngineByName()`, `this.#hiddenEngines.get()`, `this.#offeredEngines.get()`, `this.#offeredEngines.get(browser)?.some()`
- 条件付き依存: `if (shouldBeHidden)` → `this.#hiddenEngines.set()`
- 条件付き依存: `if (!(shouldBeHidden))` → `this.#offeredEngines.set()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `this.updateOpenSearchBadge()`
- 参照: `browser.documentGlobal`, `e.title`, `engine.href`, `engine.title`, `lazy.SearchService.hasSuccessfullyInitialized`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.icon()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browser.mIconURL`

## _OpenSearchManager.updateOpenSearchBadge()
- 位置: L136-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getInstallableEngines()`, `urlbar.addSearchEngineHelper.setEnginesFromBrowser()`, `urlbar.searchModeSwitcher.toggleAddEnginesBadge()`, `win.document.getElementById()`, `win.document.querySelectorAll()`
- 条件付き依存: `if (engines && engines.length)` → `searchBar.setAttribute()`
- 条件付き依存: `if (!(engines && engines.length))` → `searchBar.removeAttribute()`
- 参照: `engines.length`, `engines?.length`, `urlbar.controller`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.#addMaybeOfferedEngine()
- 位置: L165-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hiddenEngines.get()`, `this.#offeredEngines.get()`
- 条件付き依存: `if (hiddenEngines[i].title == engineName)` → `offeredEngines.push()`
- 条件付き依存: `if (offeredEngines.length == 1)` → `this.#offeredEngines.set()`
- 条件付き依存: `if (hiddenEngines[i].title == engineName)` → `hiddenEngines.splice()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `this.updateOpenSearchBadge()`
- 参照: `hiddenEngines.length`, `hiddenEngines[i].title`, `lazy.BrowserWindowTracker.orderedWindows`, `offeredEngines.length`, `win.gBrowser.browsers`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.#removeMaybeOfferedEngine()
- 位置: L189-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hiddenEngines.get()`, `this.#offeredEngines.get()`
- 条件付き依存: `if (offeredEngines[i].title == engineName)` → `hiddenEngines.push()`
- 条件付き依存: `if (hiddenEngines.length == 1)` → `this.#hiddenEngines.set()`
- 条件付き依存: `if (offeredEngines[i].title == engineName)` → `offeredEngines.splice()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `this.updateOpenSearchBadge()`
- 参照: `hiddenEngines.length`, `lazy.BrowserWindowTracker.orderedWindows`, `offeredEngines.length`, `offeredEngines[i].title`, `win.gBrowser.browsers`, `win.gBrowser.selectedBrowser`

## _OpenSearchManager.getEngines()
- 位置: L221-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#offeredEngines.get()`

## _OpenSearchManager.getInstallableEngines()
- 位置: L236-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `this.getEngines()`
- XPCOM: `Services.policies`

## _OpenSearchManager.clearEngines()
- 位置: L243-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hiddenEngines.delete()`, `this.#offeredEngines.delete()`
