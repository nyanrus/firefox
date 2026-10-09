# browser/components/syncedtabs/TabListComponent.sys.mjs

source: browser/components/syncedtabs/TabListComponent.sys.mjs
source-hash: e707715998fa9eb3995914148dd1262fe1410031
lines: 149

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/Log.sys.mjs" ).Log.repository.getLogger()`

## TabListComponent()
- 位置: L25-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._SyncedTabs`, `this._View`, `this._clipboardHelper`, `this._getChromeWindow`, `this._store`, `this._window`

## container()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._view.container`

## init()
- 位置: L47-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `log.debug()`, `this._store.focusInput()`, `this._store.getData()`, `this._store.on()`, `this._view.render()`
- 参照: `this._View`, `this._view`, `this._window`

## onSelectRow()
- 位置: L51-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onSelectRow()`

## onOpenTab()
- 位置: L52-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onOpenTab()`

## onOpenTabs()
- 位置: L53-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onOpenTabs()`

## onMoveSelectionDown()
- 位置: L54-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onMoveSelectionDown()`

## onMoveSelectionUp()
- 位置: L55-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onMoveSelectionUp()`

## onToggleBranch()
- 位置: L56-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onToggleBranch()`

## onBookmarkTab()
- 位置: L57-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onBookmarkTab()`

## onCopyTabLocation()
- 位置: L58-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onCopyTabLocation()`

## onSyncRefresh()
- 位置: L59-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onSyncRefresh()`

## onFilter()
- 位置: L60-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onFilter()`

## onClearFilter()
- 位置: L61-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onClearFilter()`

## onFilterFocus()
- 位置: L62-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onFilterFocus()`

## onFilterBlur()
- 位置: L63-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onFilterBlur()`

## uninit()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._view.destroy()`

## onFilter()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.getData()`

## onClearFilter()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.clearFilter()`

## onFilterFocus()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.focusInput()`

## onFilterBlur()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.blurInput()`

## onSelectRow()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.selectRow()`

## onMoveSelectionDown()
- 位置: L97-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.moveSelectionDown()`

## onMoveSelectionUp()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.moveSelectionUp()`

## onToggleBranch()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.toggleBranch()`

## onBookmarkTab()
- 位置: L109-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._window.top.PlacesCommandHook.bookmarkLink()`, `this._window.top.PlacesCommandHook.bookmarkLink(uri, title).catch()`
- 参照: `console.error`

## onOpenTab()
- 位置: L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._window.openTrustedLinkIn()`

## onOpenTabs()
- 位置: L119-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OpenInTabsUtils.confirmOpenInTabs()`
- 条件付き依存: `if (where == "window")` → `this._window.openDialog()`
- 条件付き依存: `if (where == "window")` → `urls.join()`
- 条件付き依存: `if (!(where == "window"))` → `this._getChromeWindow(this._window).gBrowser.loadTabs()`
- 条件付き依存: `if (!(where == "window"))` → `this._getChromeWindow()`
- 条件付き依存: `if (!(where == "window"))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `this._window`, `this._window.AppConstants.BROWSER_CHROME_URL`, `urls.length`
- XPCOM: `Services.scriptSecurityManager`

## onCopyTabLocation()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clipboardHelper.copyString()`

## onSyncRefresh()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._SyncedTabs.syncTabs()`
