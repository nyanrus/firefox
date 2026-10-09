# browser/components/preferences/dialogs/selectBookmark.js

source: browser/components/preferences/dialogs/selectBookmark.js
source-hash: 068a7fcc6ff2d95be851778f525961bc865011aa
lines: 124

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `SelectBookmarkDialog.init()`, `XPCOMUtils.defineLazyScriptGetter()`, `window.addEventListener()`

## SBD_init()
- 位置: L41-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SelectBookmarkDialog.accept()`, `bookmarks.addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `this.onItemDblClick()`, `this.selectionChanged()`
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_ROOTS_QUERY`, `bookmarks.place`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## SBD_selectionChanged()
- 位置: L59-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("selectBookmarkDialog") .getButton()`, `document.getElementById()`
- 条件付き依存: `if (bookmarks.hasSelection)` → `PlacesUtils.nodeIsSeparator()`
- 参照: `accept.disabled`, `bookmarks.hasSelection`, `bookmarks.selectedNode`

## SBD_onItemDblClick()
- 位置: L73-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsURI()`, `document.getElementById()`
- 条件付き依存: `if (selectedNode && PlacesUtils.nodeIsURI(selectedNode))` → `document .getElementById("selectBookmarkDialog") .getButton("accept") .click()`
- 条件付き依存: `if (selectedNode && PlacesUtils.nodeIsURI(selectedNode))` → `document .getElementById("selectBookmarkDialog") .getButton()`
- 条件付き依存: `if (selectedNode && PlacesUtils.nodeIsURI(selectedNode))` → `document .getElementById()`
- 参照: `bookmarks.selectedNode`

## SBD_accept()
- 位置: L92-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsFolderOrShortcut()`, `document.getElementById()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(selectedNode))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(selectedNode))` → `PlacesUtils.getFolderContents()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(selectedNode))` → `contents.getChild()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(selectedNode))` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node))` → `urls.push()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node))` → `names.push()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsFolderOrShortcut(selectedNode)))` → `urls.push()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsFolderOrShortcut(selectedNode)))` → `names.push()`
- 参照: `PlacesUtils.getFolderContents(concreteGuid).root`, `bookmarks.hasSelection`, `bookmarks.selectedNode`, `contents.childCount`, `contents.containerOpen`, `node.title`, `node.uri`, `selectedNode.title`, `selectedNode.uri`, `window.arguments`, `window.arguments[0].names`, `window.arguments[0].urls`
