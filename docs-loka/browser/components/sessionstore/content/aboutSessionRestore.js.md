# browser/components/sessionstore/content/aboutSessionRestore.js

source: browser/components/sessionstore/content/aboutSessionRestore.js
source-hash: 4cba943f1aafd8e738cc3fb85233d3e0e957d057
lines: 507

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`

## window.onload()
- 位置: L51-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `document.createEvent()`, `document.getElementById()`, `errorTryAgainButton.addEventListener()`, `errorTryAgainButton.focus()`, `event.initUIEvent()`, `getTabList()`, `getTryAgainButton()`, `initTreeView()`, `sessionData.dispatchEvent()`, `tabListTree.addEventListener()`
- 条件付き依存: `if (button)` → `button.addEventListener()`
- 条件付き依存: `if (errorCancelButton)` → `errorCancelButton.addEventListener()`
- 参照: `errorTryAgainButton.disabled`, `sessionData.value`, `toggleTabs.onclick`

## toggleHiddenTabs()
- 位置: L56-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabList()`, `initTreeView()`, `toggleTabs.classList.contains()`, `toggleTabs.classList.toggle()`
- 参照: `getTabList().hidden`

## isTreeViewVisible()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabList()`
- 参照: `getTabList().hidden`

## initTreeView()
- 位置: async L113-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWinData.tabs.map()`, `document.l10n.formatValues()`, `gStateObject.windows.forEach()`, `gTreeData.push()`, `getTabList()`, `isTreeViewVisible()`, `l10nIds.push()`, `lazy.PlacesUIUtils.getImageURL()`, `tabList.view.selection.select()`
- 参照: `aTabData.entries`, `aTabData.image`, `aTabData.index`, `entry.title`, `entry.url`, `gStateObject.windows.length`, `tabList.view`, `winState.tabs`

## updateTabListVisibility()
- 位置: L164-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `getTabList()`, `initTreeView()`
- 参照: `( document.getElementById("radioRestoreChoose") ).checked`, `getTabList().hidden`

## restoreSession()
- 位置: L173-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `getBrowserWindow()`, `getTryAgainButton()`, `isTreeViewVisible()`, `top.openDialog()`
- 条件付き依存: `if (isTreeViewVisible())` → `gTreeData.some()`
- 条件付き依存: `if (!gTreeData.some(aItem => aItem.checked))` → `startNewSession()`
- 条件付き依存: `if (isTreeViewVisible())` → `treeView.isContainer()`
- 条件付き依存: `if (gTreeData[t].checked === 0)` → `gStateObject.windows[ix].tabs.filter()`
- 条件付き依存: `if (!gTreeData[t].checked)` → `gStateObject.windows.splice()`
- 条件付き依存: `if (top.gBrowser.tabs.length == 1)` → `lazy.SessionStore.setWindowState()`
- 参照: `aItem.checked`, `gStateObject.windows`, `gStateObject.windows.length`, `gStateObject.windows[ix].tabs`, `gTreeData.length`, `gTreeData[t].checked`, `gTreeData[t].tabs`, `gTreeData[t].tabs[aIx].checked`, `getTryAgainButton().disabled`, `top.gBrowser.tabs.length`, `top.location.href`
- XPCOM: `Services.obs`

## observe()
- 位置: L218-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.SessionStore.setWindowState()`, `tabbrowser.getTabForBrowser()`, `tabbrowser.removeTab()`
- 参照: `top.gBrowser`, `window.docShell.chromeEventHandler`
- XPCOM: `Services.obs`

## startNewSession()
- 位置: L233-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `getBrowserWindow().gBrowser.loadURI()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `getBrowserWindow()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `Services.io.newURI()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (!(Services.prefs.getIntPref("browser.startup.page") == 0))` → `getBrowserWindow().BrowserCommands.home()`
- 条件付き依存: `if (!(Services.prefs.getIntPref("browser.startup.page") == 0))` → `getBrowserWindow()`
- XPCOM: `Services.io` / `Services.prefs` / `Services.scriptSecurityManager`

## onListClick()
- 位置: L245-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `treeView.treeBox.getCellAt()`
- 条件付き依存: `if (cell.col)` → `treeView.isContainer()`
- 条件付き依存: `if ( (aEvent.button == 1 || (aEvent.button == 0 && aEvent.detail == 2) || accelKey) && cell.col.id == "title" && !treeView.isContainer(cell.row) )` → `restoreSingleTab()`
- 条件付き依存: `if ( (aEvent.button == 1 || (aEvent.button == 0 && aEvent.detail == 2) || accelKey) && cell.col.id == "title" && !treeView.isContainer(cell.row) )` → `aEvent.stopPropagation()`
- 条件付き依存: `if (cell.col.id == "restore")` → `toggleRowChecked()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.clientX`, `aEvent.clientY`, `aEvent.ctrlKey`, `aEvent.detail`, `aEvent.metaKey`, `aEvent.shiftKey`, `cell.col`, `cell.col.id`, `cell.row`

## onListKeyDown()
- 位置: L272-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.preventDefault()`, `getTabList()`, `toggleRowChecked()`, `treeView.isContainer()`
- 条件付き依存: `if (aEvent.ctrlKey && !treeView.isContainer(ix))` → `restoreSingleTab()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `aEvent.ctrlKey`, `aEvent.keyCode`, `aEvent.shiftKey`, `getTabList().currentIndex`

## getTabList()
- 位置: L293-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## getTryAgainButton()
- 位置: L300-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## getBrowserWindow()
- 位置: L309-314
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `(window.browsingContext) .topChromeWindow`, `window.browsingContext`

## toggleRowChecked()
- 位置: L316-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `treeView.isContainer()`, `treeView.treeBox.invalidateRow()`
- 条件付き依存: `if (treeView.isContainer(aIx))` → `treeView.treeBox.invalidateRow()`
- 条件付き依存: `if (treeView.isContainer(aIx))` → `gTreeData.indexOf()`
- 条件付き依存: `if (!(treeView.isContainer(aIx)))` → `item.parent.tabs.every()`
- 条件付き依存: `if (!(item.parent.tabs.every(isChecked)))` → `item.parent.tabs.some()`
- 条件付き依存: `if (!(treeView.isContainer(aIx)))` → `treeView.treeBox.invalidateRow()`
- 条件付き依存: `if (!(treeView.isContainer(aIx)))` → `gTreeData.indexOf()`
- 条件付き依存: `if (document.getElementById("errorCancel"))` → `getTryAgainButton()`
- 条件付き依存: `if (document.getElementById("errorCancel"))` → `gTreeData.some()`
- 参照: `getTryAgainButton().disabled`, `item.checked`, `item.parent`, `item.parent.checked`, `item.tabs`, `tab.checked`

## isChecked()
- 位置: L317-319
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aItem.checked`

## restoreSingleTab()
- 位置: L351-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.getBoolPref()`, `gTreeData.indexOf()`, `getBrowserWindow()`, `lazy.SessionStore.setTabState()`, `tabbrowser.addWebTab()`
- 参照: `gStateObject.windows`, `gStateObject.windows[item.parent.ix].tabs`, `getBrowserWindow().gBrowser`, `item.parent`, `item.parent.ix`, `tabState.hidden`, `tabbrowser.selectedTab`
- XPCOM: `Services.prefs`

## rowCount()
- 位置: L378-380
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gTreeData.length`

## setTree()
- 位置: L381-383
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.treeBox`

## getCellText()
- 位置: L384-386
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gTreeData[idx].label`

## isContainer()
- 位置: L387-389
- 役割: (未記入)
- 触るとき: (未記入)

## getCellValue()
- 位置: L390-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`
- 参照: `gTreeData[idx].checked`

## isContainerOpen()
- 位置: L393-395
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gTreeData[idx].open`

## isContainerEmpty()
- 位置: L396-398
- 役割: (未記入)
- 触るとき: (未記入)

## isSeparator()
- 位置: L399-401
- 役割: (未記入)
- 触るとき: (未記入)

## isSorted()
- 位置: L402-404
- 役割: (未記入)
- 触るとき: (未記入)

## isEditable()
- 位置: L405-407
- 役割: (未記入)
- 触るとき: (未記入)

## canDrop()
- 位置: L408-410
- 役割: (未記入)
- 触るとき: (未記入)

## getLevel()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isContainer()`

## getParentIndex()
- 位置: L415-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isContainer()`
- 条件付き依存: `if (!this.isContainer(idx))` → `this.isContainer()`

## hasNextSibling()
- 位置: L426-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getLevel()`
- 条件付き依存: `if (this.getLevel(t) <= thisLevel)` → `this.getLevel()`
- 参照: `gTreeData.length`

## toggleOpenState()
- 位置: L436-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isContainer()`, `this.treeBox.invalidateRow()`
- 条件付き依存: `if (item.open)` → `this.getLevel()`
- 条件付き依存: `if (item.open)` → `gTreeData.splice()`
- 条件付き依存: `if (item.open)` → `this.treeBox.rowCountChanged()`
- 条件付き依存: `if (!(item.open))` → `gTreeData.splice()`
- 条件付き依存: `if (!(item.open))` → `this.treeBox.rowCountChanged()`
- 参照: `gTreeData.length`, `gTreeData[idx].tabs`, `item.open`, `toinsert.length`

## getCellProperties()
- 位置: L466-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isContainer()`
- 条件付き依存: `if (column.id == "title")` → `this.getImageSrc()`
- 参照: `column.id`, `gTreeData[idx].checked`

## getRowProperties()
- 位置: L481-488
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gTreeData[idx].parent`, `winState.ix`

## getImageSrc()
- 位置: L490-495
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `column.id`, `gTreeData[idx].src`

## setCellValue()
- 位置: L497-497
- 役割: (未記入)
- 触るとき: (未記入)

## setCellText()
- 位置: L498-498
- 役割: (未記入)
- 触るとき: (未記入)

## drop()
- 位置: L499-499
- 役割: (未記入)
- 触るとき: (未記入)

## cycleHeader()
- 位置: L500-500
- 役割: (未記入)
- 触るとき: (未記入)

## cycleCell()
- 位置: L501-501
- 役割: (未記入)
- 触るとき: (未記入)

## selectionChanged()
- 位置: L502-502
- 役割: (未記入)
- 触るとき: (未記入)

## getColumnProperties()
- 位置: L503-505
- 役割: (未記入)
- 触るとき: (未記入)
