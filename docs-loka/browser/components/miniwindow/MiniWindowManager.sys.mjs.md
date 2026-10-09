# browser/components/miniwindow/MiniWindowManager.sys.mjs

source: browser/components/miniwindow/MiniWindowManager.sys.mjs
source-hash: 763ea431c7b478b50e190c51a78b02d9deab1876
lines: 286

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## _enabled()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## _log()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.logConsole`

## popRegion()
- 位置: async L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pop()`

## popTab()
- 位置: async L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#pop()`

## #pop()
- 位置: async L83-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.miniWindow.created.record()`, `minisForOriginWin.add()`, `miniwindow.open()`, `this.#ensureObservers()`, `this.#originWinHooks.has()`, `this.#originWinToMinis.get()`, `this._log.debug()`, `this._miniwindows.add()`
- 条件付き依存: `if (!minisForOriginWin)` → `this.#originWinToMinis.set()`
- 条件付き依存: `if (!this.#originWinHooks.has(originWin))` → `this.#hookOriginWin()`
- 条件付き依存: `if (!win)` → `this._log.debug()`
- 条件付き依存: `if (!win)` → `this._unregister()`
- 参照: `browser.currentURI?.spec`, `browser.documentGlobal`, `lazy.MiniWindow`, `originWin.gBrowser.tabs.length`, `tab.linkedBrowser`, `this._enabled`, `this._miniwindows.size`

## _miniWindowForBrowser()
- 位置: L142-149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `mini.browser`, `this._miniwindows`

## _unregister()
- 位置: L151-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `minisForOriginWin.delete()`, `this.#originWinToMinis.get()`, `this._log.debug()`, `this._miniwindows.delete()`
- 条件付き依存: `if (!minisForOriginWin)` → `this._log.debug()`
- 条件付き依存: `if (!minisForOriginWin.size)` → `this.#originWinToMinis.delete()`
- 条件付き依存: `if (!minisForOriginWin.size)` → `this.#unhookOriginWin()`
- 参照: `minisForOriginWin.size`, `miniwindow.originWin`, `this._miniwindows.size`

## #ensureObservers()
- 位置: L167-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.#observing`
- XPCOM: `Services.obs`

## observe()
- 位置: L175-188
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "quit-application-granted")` → `this._log.debug()`
- 条件付き依存: `if (topic === "quit-application-granted")` → `mini.returnToOriginWin()`
- 参照: `this._miniwindows`, `this._miniwindows.size`

## #hookOriginWin()
- 位置: L196-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originWin.addEventListener()`, `this.#originWinHooks.set()`, `this.#putBackMinisForOriginWins()`
- 参照: `abortController.signal`

## #unhookOriginWin()
- 位置: L213-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `abortController.abort()`, `this.#originWinHooks.delete()`, `this.#originWinHooks.get()`, `this.#originWinToMinis.get()`
- 参照: `this.#originWinToMinis.get(originWin)?.size`

## windowsToAvoid()
- 位置: L233-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `wins.push()`
- 条件付き依存: `if (mini.miniWin && mini.miniWin !== win && !mini.miniWin.closed)` → `wins.push()`
- 参照: `mini.miniWin`, `mini.miniWin.closed`, `player.closed`, `this._miniwindows`
- XPCOM: `Services.wm`

## maybeMoveOldestMiniWindow()
- 位置: L256-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `oldest.returnToOriginWin()`, `this.#originWinToMinis.get()`, `this.#originWinToMinis.get(originWin)?.values()`, `this.#originWinToMinis.get(originWin)?.values().next()`
- 参照: `this.#originWinToMinis.get(originWin)?.values().next().value`

## #putBackMinisForOriginWins()
- 位置: L267-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `miniWin.returnToOriginWin()`, `this.#minisForOriginWin()`, `this._log.debug()`
- 参照: `minis.length`

## #minisForOriginWin()
- 位置: L281-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#originWinToMinis.get()`
