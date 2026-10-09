# browser/modules/ZoomUI.sys.mjs

source: browser/modules/ZoomUI.sys.mjs
source-hash: 667ee95940f1fc17521aecddbefb2bab299f73cc
lines: 206

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`, `Cu.createLoadContext()`, `CustomizableUI.addListener()`, `Services.obs.addObserver()`

## init()
- 位置: L12-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.addEventListener()`, `aWindow.removeEventListener()`

## getGlobalValue()
- 位置: L37-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gContentPrefs.getCachedGlobal()`, `gContentPrefs.getGlobal()`
- 条件付き依存: `if (cachedVal)` → `resolve()`
- 条件付き依存: `if (cachedVal)` → `parseFloat()`
- 参照: `cachedVal.value`

## handleResult()
- 位置: L55-59
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pref.value)` → `parseFloat()`
- 参照: `pref.value`

## handleCompletion()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## handleError()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`

## fullZoomLocationChangeObserver()
- 位置: L71-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateZoomUI()`
- 参照: `aSubject.documentGlobal`

## onEndSwapDocShells()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateZoomUI()`
- 参照: `event.originalTarget`

## onZoomChange()
- 位置: L89-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateZoomUI()`
- 参照: `event.originalTarget`, `event.target.DOCUMENT_NODE`, `event.target.defaultView.top.document`, `event.target.nodeType`, `topDoc.documentElement`, `topDoc.documentGlobal.docShell.chromeEventHandler`

## updateZoomUI()
- 位置: async L115-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `ZoomUI.getGlobalValue()`, `customizableZoomControls.getAttribute()`, `win.FullZoom.updateCommands()`, `win.document.getElementById()`, `win.gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (appMenuZoomReset)` → `appMenuZoomReset.setAttribute()`
- 条件付き依存: `if (customizableZoomReset)` → `customizableZoomReset.setAttribute()`
- 条件付き依存: `if (aAnimate && !win.gReduceMotion)` → `urlbarZoomButton.setAttribute()`
- 条件付き依存: `if (!(aAnimate && !win.gReduceMotion))` → `urlbarZoomButton.removeAttribute()`
- 条件付き依存: `if (!urlbarZoomButton.hidden)` → `urlbarZoomButton.setAttribute()`
- 参照: `aBrowser.browsingContext?.topChromeWindow`, `aBrowser.contentPrincipal`, `aBrowser.contentPrincipal.isNullPrincipal`, `aBrowser.contentPrincipal.spec`, `aBrowser.currentURI.spec`, `aBrowser.documentGlobal`, `urlbarZoomButton.hidden`, `win.ZoomManager.zoom`, `win.gBrowser`, `win.gBrowser.selectedBrowser`, `win.gReduceMotion`

## customizationListener.onWidgetMoved()
- 位置: L192-198
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId == "zoom-controls")` → `updateZoomUI()`
- 参照: `CustomizableUI.windows`, `window.gBrowser.selectedBrowser`

## customizationListener.onWidgetUndoMove()
- 位置: L200-204
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetNode.id == "zoom-controls")` → `updateZoomUI()`
- 参照: `aWidgetNode.documentGlobal.gBrowser.selectedBrowser`, `aWidgetNode.id`
