# browser/components/places/content/bookmarksSidebar.js

source: browser/components/places/content/bookmarksSidebar.js
source-hash: ef6ca91f3c5145852059976b094ea7e0fd625fa9
lines: 195

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Glean.browserUiInteraction.sidebarBookmarks.open_in_new_container_tab.add()`, `PlacesUIUtils.onSidebarTreeClick()`, `PlacesUIUtils.onSidebarTreeKeyPress()`, `PlacesUIUtils.onSidebarTreeMouseMove()`, `PlacesUIUtils.setMouseoverURL()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `XPCOMUtils.defineLazyScriptGetter()`, `bhTooltip.addEventListener()`, `bhTooltip.removeAttribute()`, `clearCumulativeCounter()`, `document .getElementById()`, `document .getElementById("placesCommands") .addEventListener()`, `document .getElementById("placesContext_open_newcontainertab_popup") .addEventListener()`, `document .getElementById("search-box") .addEventListener()`, `document .getElementById("sidebar-panel-close") .addEventListener()`, `document.getElementById()`, `document.getElementById("search-box").focus()`, `recordDialogResult()`, `view.addEventListener()`, `window.addEventListener()`, `window.top.BookmarksEventHandler.fillInBHTooltip()`, `window.top.document.documentElement.getAttribute()`

## recordDialogResult()
- 位置: async L132-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUiInteraction.sidebarBookmarks[`${labelPrefix}_${outcome}`].add()`
- 参照: `Glean.browserUiInteraction.sidebarBookmarks`, `PlacesUIUtils.lastBookmarkDialogDeferred`, `deferred.promise`

## searchBookmarks()
- 位置: L144-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!(!value))` → `Glean.sidebar.search.bookmarks.add()`
- 条件付き依存: `if (!(!value))` → `Glean.browserUiInteraction.sidebarBookmarks.search.add()`
- 条件付き依存: `if (!(!value))` → `tree.applyFilter()`
- 参照: `PlacesUtils.bookmarks.userContentRoots`, `event.currentTarget`, `tree.place`

## updateTelemetry()
- 位置: L159-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.bookmarksSidebar.cumulativeSearches.accumulateSingleSample()`, `Glean.sidebar.link.bookmarks.add()`, `clearCumulativeCounter()`
- 条件付き依存: `if (openAllBookmarks)` → `Glean.browserUiInteraction.sidebarBookmarks.open_all_bookmarks.add()`
- 参照: `urlsOpened.length`

## clearCumulativeCounter()
- 位置: L171-173
- 役割: (未記入)
- 触るとき: (未記入)

## closeSidebarPanel()
- 位置: L184-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `e.target.getAttribute()`, `window.browsingContext.embedderWindowGlobal.browsingContext.window.SidebarController.toggle()`
