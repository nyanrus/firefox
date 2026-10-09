# browser/components/urlbar/UrlbarProviderQuickSuggestContextualOptIn.sys.mjs

source: browser/components/urlbar/UrlbarProviderQuickSuggestContextualOptIn.sys.mjs
source-hash: dc45cb3564aa78d686738e1a8c5c67ce9dea1b84
lines: 362

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderQuickSuggestContextualOptIn.constructor()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderQuickSuggestContextualOptIn.type()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderQuickSuggestContextualOptIn.#shouldDisplayContextualOptIn()
- 位置: L80-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.isPrivate`, `queryContext.restrictSource`, `queryContext.searchString`

## UrlbarProviderQuickSuggestContextualOptIn.isActive()
- 位置: async L141-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.UrlbarPrefs.get()`, `this.#dismiss()`, `this.#shouldDisplayContextualOptIn()`

## UrlbarProviderQuickSuggestContextualOptIn.getPriority()
- 位置: L178-180
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderQuickSuggestContextualOptIn.getViewTemplate()
- 位置: L182-184
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderQuickSuggestContextualOptIn.getViewUpdate()
- 位置: L190-208
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderQuickSuggestContextualOptIn.onBeforeSelection()
- 位置: L214-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.getAttribute()`
- 条件付き依存: `if (element.getAttribute("name") == "learn_more")` → `this.#a11yAlertRow()`
- 条件付き依存: `if (element.getAttribute("name") == "learn_more")` → `element.closest()`

## UrlbarProviderQuickSuggestContextualOptIn.#a11yAlertRow()
- 位置: L220-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decription.firstElementChild?.remove()`, `row .querySelector()`, `row .querySelector( ".urlbarView-dynamic-quickSuggestContextualOptIn-description" ) .cloneNode()`, `row.ariaNotify()`, `row.querySelector()`
- 参照: `decription.textContent`, `row.querySelector( ".urlbarView-dynamic-quickSuggestContextualOptIn-title" ).textContent`

## UrlbarProviderQuickSuggestContextualOptIn.onImpression()
- 位置: L242-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if (!firstImpressionTime)` → `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if (!firstImpressionTime)` → `Date.now()`
- 参照: `details.provider`, `this.name`

## UrlbarProviderQuickSuggestContextualOptIn.onEngagement()
- 位置: L271-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleCommand()`
- 参照: `details.result`, `details.selType`

## UrlbarProviderQuickSuggestContextualOptIn._handleCommand()
- 位置: L277-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.browserWindow.openHelpLink()`, `controller.view.close()`, `lazy.UrlbarPrefs.set()`, `this.#dismiss()`, `this.#shouldDisplayContextualOptIn()`
- 条件付き依存: `if (result)` → `controller.removeResult()`
- 参照: `container.hidden`

## UrlbarProviderQuickSuggestContextualOptIn.#dismiss()
- 位置: L310-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`

## UrlbarProviderQuickSuggestContextualOptIn.startQuery()
- 位置: async L334-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`
