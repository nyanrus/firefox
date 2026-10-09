# browser/components/tabbrowser/NewTabPagePreloading.sys.mjs

source: browser/components/tabbrowser/NewTabPagePreloading.sys.mjs
source-hash: 09b8c8d57f917c079fae7209826f14c1218c5cb8
lines: 198

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## enabled()
- 位置: L33-39
- 役割: (未記入)
- 触るとき: (未記入)

## _createBrowser()
- 位置: L44-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `gBrowser.createBrowser()`, `gBrowser.getPanel()`, `gBrowser.tabpanels.appendChild()`

## _adoptBrowserFromOtherWindow()
- 位置: L65-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows .filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `oldBrowser.swapBrowsers()`, `oldWin.gBrowser.getPanel()`, `oldWin.gBrowser.getPanel(oldBrowser).remove()`, `this._createBrowser()`

## maybeCreatePreloadedBrowser()
- 位置: L96-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `browser.loadURI()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows.filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this._createBrowser()`, `topWindows.indexOf()`, `window.FullZoom.onLocationChange()`, `window.gURLBar.getBrowserState()`
- 条件付き依存: `if (this.browserCounts[countKey] >= this.MAX_COUNT)` → `this._adoptBrowserFromOtherWindow()`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## getPreloadedBrowser()
- 位置: L149-176
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (browser)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (browser)` → `browser.removeAttribute()`
- 条件付き依存: `if (browser)` → `browser.setAttribute()`

## removePreloadedBrowser()
- 位置: L178-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPreloadedBrowser()`
- 条件付き依存: `if (browser)` → `window.gBrowser.getPanel(browser).remove()`
- 条件付き依存: `if (browser)` → `window.gBrowser.getPanel()`
