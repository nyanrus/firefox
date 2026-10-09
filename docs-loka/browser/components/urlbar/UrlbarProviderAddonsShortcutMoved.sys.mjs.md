# browser/components/urlbar/UrlbarProviderAddonsShortcutMoved.sys.mjs

source: browser/components/urlbar/UrlbarProviderAddonsShortcutMoved.sys.mjs
source-hash: efceb85085ccf32552432bd8d3f4da6ca513e194
lines: 177

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderAddonsShortcutMoved.type()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderAddonsShortcutMoved.isActive()
- 位置: async L64-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `queryContext.searchMode.entry`, `queryContext.searchMode?.source`, `queryContext.searchString`
- XPCOM: `Services.prefs`

## UrlbarProviderAddonsShortcutMoved.getViewTemplate()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderAddonsShortcutMoved.getViewUpdate()
- 位置: L82-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `lazy.ShortcutUtils.prettifyShortcut()`
- 参照: `controller.browserWindow.document`

## UrlbarProviderAddonsShortcutMoved.onEngagement()
- 位置: L113-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.switchToTabHavingURI()`, `controller.view.close()`, `this.#stop()`
- 参照: `details.selType`

## UrlbarProviderAddonsShortcutMoved.onImpression()
- 位置: L127-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (shownCount < SHOWN_LIMIT)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!(shownCount < SHOWN_LIMIT))` → `this.#stop()`
- XPCOM: `Services.prefs`

## UrlbarProviderAddonsShortcutMoved.#stop()
- 位置: L141-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## UrlbarProviderAddonsShortcutMoved.startQuery()
- 位置: async L153-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`
