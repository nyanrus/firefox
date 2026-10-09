# browser/components/places/content/bookmarksSidebar.js

source: browser/components/places/content/bookmarksSidebar.js
source-hash: ef6ca91f3c5145852059976b094ea7e0fd625fa9
lines: 195

## <module>
- 役割: サイドバーのブックマーク表示ページ。Places ツリーのイベント配線、ブックマーク操作の Glean 計測、検索フィルターとサイドバーを閉じる処理を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Glean.browserUiInteraction.sidebarBookmarks.open_in_new_container_tab.add()`, `PlacesUIUtils.onSidebarTreeClick()`, `PlacesUIUtils.onSidebarTreeKeyPress()`, `PlacesUIUtils.onSidebarTreeMouseMove()`, `PlacesUIUtils.setMouseoverURL()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `XPCOMUtils.defineLazyScriptGetter()`, `bhTooltip.addEventListener()`, `bhTooltip.removeAttribute()`, `clearCumulativeCounter()`, `document .getElementById()`, `document .getElementById("placesCommands") .addEventListener()`, `document .getElementById("placesContext_open_newcontainertab_popup") .addEventListener()`, `document .getElementById("search-box") .addEventListener()`, `document .getElementById("sidebar-panel-close") .addEventListener()`, `document.getElementById()`, `document.getElementById("search-box").focus()`, `recordDialogResult()`, `view.addEventListener()`, `window.addEventListener()`, `window.top.BookmarksEventHandler.fillInBHTooltip()`, `window.top.document.documentElement.getAttribute()`

## recordDialogResult()
- 位置: async L132-142
- 役割: ブックマークダイアログの Deferred が解決されるのを待ち、guid の有無で confirmed か cancelled を判定して対応する Glean 指標を加算する。
- 触るとき: ブックマークの追加・編集・フォルダー名変更ダイアログの結果計測を変えるとき、または labelPrefix と Glean 指標名の対応を確認するとき。
- 呼び出し先: `Glean.browserUiInteraction.sidebarBookmarks[`${labelPrefix}_${outcome}`].add()`
- 参照: `Glean.browserUiInteraction.sidebarBookmarks`, `PlacesUIUtils.lastBookmarkDialogDeferred`, `deferred.promise`

## searchBookmarks()
- 位置: L144-157
- 役割: 検索ボックスの入力を受け、空なら tree.place を再設定して絞り込みを解除し、値があれば検索の計測を加算して applyFilter で絞り込む。
- 触るとき: サイドバーのブックマーク検索の挙動や検索回数の計測を変えるとき、検索を空にしたときに一覧が元に戻らない問題を調べるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!(!value))` → `Glean.sidebar.search.bookmarks.add()`
- 条件付き依存: `if (!(!value))` → `Glean.browserUiInteraction.sidebarBookmarks.search.add()`
- 条件付き依存: `if (!(!value))` → `tree.applyFilter()`
- 参照: `PlacesUtils.bookmarks.userContentRoots`, `event.currentTarget`, `tree.place`

## updateTelemetry()
- 位置: L159-169
- 役割: 累積検索回数を Glean に記録し、カウンターをリセットしたうえで開いた URL 数と「すべてのブックマークを開く」の操作を計測する。
- 触るとき: リンクを開いた件数や全件オープンの計測項目を追加・変更するとき、または累積検索回数が正しく送られるか確認するとき。
- 呼び出し先: `Glean.bookmarksSidebar.cumulativeSearches.accumulateSingleSample()`, `Glean.sidebar.link.bookmarks.add()`, `clearCumulativeCounter()`
- 条件付き依存: `if (openAllBookmarks)` → `Glean.browserUiInteraction.sidebarBookmarks.open_all_bookmarks.add()`
- 参照: `urlsOpened.length`

## clearCumulativeCounter()
- 位置: L171-173
- 役割: 累積検索カウンター gCumulativeSearches を 0 に戻す。
- 触るとき: 検索回数の集計区切りを変えるとき、たとえば unload 時や計測送信後にカウンターが残らないようにしたいとき。

## closeSidebarPanel()
- 位置: L184-190
- 役割: 閉じるボタンのクリックを受け、既定動作を止めたうえで view 属性で指定されたサイドバーパネルを SidebarController.toggle で切り替える。
- 触るとき: サイドバーの閉じるボタンが別のパネルを閉じてしまう、または閉じられないといった不具合を調べるとき、閉じるボタンに view 属性を追加・変更するとき。
- 呼び出し先: `e.preventDefault()`, `e.target.getAttribute()`, `window.browsingContext.embedderWindowGlobal.browsingContext.window.SidebarController.toggle()`
