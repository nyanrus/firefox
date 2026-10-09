# browser/components/customizableui/SearchWidgetTracker.sys.mjs

source: browser/components/customizableui/SearchWidgetTracker.sys.mjs
source-hash: f44f96361d9a8fb5f5533251ba76764bbf4477cb
lines: 127

## <module>
- 役割: (未記入)

## init()
- 位置: L19-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `this._removeWidgetIfUnused()`

## onWidgetAfterDOMChange()
- 位置: L38-42
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node.id == WIDGET_ID && wasRemoval)` → `this._removePersistedWidths()`
- 参照: `node.id`

## onCustomizeStart()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._widgetIsInNavBar`, `this._widgetWasInNavBar`

## onCustomizeEnd()
- 位置: L48-58
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._widgetWasInNavBar && this._widgetIsInNavBar)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!this._widgetWasInNavBar && this._widgetIsInNavBar)` → `new Date().toISOString()`
- 参照: `this._widgetIsInNavBar`, `this._widgetWasInNavBar`
- XPCOM: `Services.prefs`

## _removeWidgetIfUnused()
- 位置: L67-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 条件付き依存: `if (searchBarLastUsed)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (new Date() - new Date(searchBarLastUsed) > saerchBarUnusedThreshold)` → `CustomizableUI.removeWidgetFromArea()`
- 条件付き依存: `if (new Date() - new Date(searchBarLastUsed) > saerchBarUnusedThreshold)` → `Glean.browserUi.customizedWidgets[ "search-container_remove_na_na_auto-unused" ].add()`
- 参照: `Glean.browserUi.customizedWidgets`, `this._widgetIsInNavBar`
- XPCOM: `Services.prefs`

## _removePersistedWidths()
- 位置: L102-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.xulStore.removeValue()`, `searchbar.removeAttribute()`, `searchbar.style.removeProperty()`, `win.document.getElementById()`, `win.gNavToolbox.palette.querySelector()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `CustomizableUI.windows`
- XPCOM: `Services.xulStore`

## _widgetIsInNavBar()
- 位置: L122-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `placement?.area`
