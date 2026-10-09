# browser/components/places/content/places.js

source: browser/components/places/content/places.js
source-hash: 08f6e3859bf2a9cbb57dd3dc33379bda888ce918
lines: 1646

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyScriptGetter()`, `window.addEventListener()`

## _initFolderTree()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_LEFT_PANE_QUERY`, `this._places.place`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## selectLeftPaneBuiltIn()
- 位置: L63-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asContainer()`, `this._places.selectItems()`, `this.selectLeftPaneContainerByHierarchy()`
- 参照: `PlacesUtils.asContainer(this._places.selectedNode).containerOpen`, `PlacesUtils.bookmarks.virtualMenuGuid`, `PlacesUtils.bookmarks.virtualToolbarGuid`, `PlacesUtils.bookmarks.virtualUnfiledGuid`, `PlacesUtils.virtualAllBookmarksGuid`, `PlacesUtils.virtualDownloadsGuid`, `PlacesUtils.virtualHistoryGuid`, `PlacesUtils.virtualTagsGuid`, `this._places.selectedNode`

## selectLeftPaneContainerByHierarchy()
- 位置: L115-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asContainer()`, `[].concat()`, `container.substr()`, `this.selectLeftPaneBuiltIn()`
- 条件付き依存: `if (container.substr(0, 6) == "place:")` → `this._places.selectPlaceURI()`
- 条件付き依存: `if (!(container.substr(0, 6) == "place:"))` → `this._places.selectItems()`
- 参照: `PlacesUtils.asContainer(this._places.selectedNode).containerOpen`, `this._places.selectedNode`, `this._places.view.selection.selectEventsSuppressed`

## PO_init()
- 位置: L150-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentArea.focus()`, `ContentArea.init()`, `ContentArea.setContentViewForQueryString()`, `PlacesSearchBox.init()`, `Services.policies.isAllowed()`, `ViewMenu.fillWithColumns()`, `ViewMenu.init()`, `ViewMenu.showHideColumn()`, `columnsContextPopup.addEventListener()`, `contextMenu.removeChild()`, `document .getElementById()`, `document .getElementById("OrganizerCommand:Back") .setAttribute()`, `document .getElementById("fileRestorePopup") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `event.stopPropagation()`, `placeContentElement.addEventListener()`, `this._backHistory.splice()`, `this._initFolderTree()`, `this._places.addEventListener()`, `this.onPlaceSelected()`, `this.onPlacesListClick()`, `this.openFlatContainer()`, `this.populateRestoreMenu()`, `this.selectLeftPaneContainerByHierarchy()`, `this.updateDetailsPane()`, `window.addEventListener()`
- 条件付き依存: `if (historyNode.childCount > 0)` → `this._places.selectNode()`
- 条件付き依存: `if (historyNode.childCount > 0)` → `historyNode.getChild()`
- 条件付き依存: `if (leftPaneSelection === "History")` → `Glean.library.opened.history.add()`
- 条件付き依存: `if (!(leftPaneSelection === "History"))` → `Glean.library.opened.bookmarks.add()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `findMenuItem.setAttribute()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `findKey.setAttribute()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `document.getElementById(elements[i]).setAttribute()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `document .getElementById("organizeButton") .addEventListener()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `document .getElementById()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `document.getElementById("placeContent").focus()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document .getElementById("OrganizerCommand_browserImport") .setAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document .getElementById()`
- 参照: `AppConstants.platform`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_DESCENDING`, `Ci.nsINavHistoryService.TRANSITION_DOWNLOAD`, `elements.length`, `event.detail`, `event.target`, `historyNode.childCount`, `this._backHistory.length`, `this._places`, `this._places.selectedNode`, `window.arguments`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryService`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.policies`

## PO_handleEvent()
- 位置: L280-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesQueryBuilder.addRow()`, `PlacesSearchBox.findAll()`, `event.stopPropagation()`, `this.back()`, `this.backupBookmarks()`, `this.destroy()`, `this.exportBookmarks()`, `this.forward()`, `this.importFromBrowser()`, `this.importFromFile()`, `this.init()`, `this.onRestoreBookmarksFromFile()`, `this.saveSearch()`, `window.close()`
- 条件付き依存: `if (this._backHistory.length)` → `this.back()`
- 条件付き依存: `if (this._forwardHistory.length)` → `this.forward()`
- 参照: `event.command`, `event.target.id`, `event.type`, `this._backHistory.length`, `this._forwardHistory.length`

## PO_destroy()
- 位置: L347-347
- 役割: (未記入)
- 触るとき: (未記入)

## location()
- 位置: L350-352
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._location`

## location()
- 位置: L354-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._places.selectPlaceURI()`, `this.updateDetailsPane()`
- 条件付き依存: `if (this.location)` → `this._backHistory.unshift()`
- 条件付き依存: `if (this.location)` → `this._forwardHistory.splice()`
- 条件付き依存: `if (!this._backHistory.length)` → `document .getElementById("OrganizerCommand:Back") .setAttribute()`
- 条件付き依存: `if (!this._backHistory.length)` → `document .getElementById()`
- 条件付き依存: `if (!(!this._backHistory.length))` → `document .getElementById("OrganizerCommand:Back") .removeAttribute()`
- 条件付き依存: `if (!(!this._backHistory.length))` → `document .getElementById()`
- 条件付き依存: `if (!this._forwardHistory.length)` → `document .getElementById("OrganizerCommand:Forward") .setAttribute()`
- 条件付き依存: `if (!this._forwardHistory.length)` → `document .getElementById()`
- 条件付き依存: `if (!(!this._forwardHistory.length))` → `document .getElementById("OrganizerCommand:Forward") .removeAttribute()`
- 条件付き依存: `if (!(!this._forwardHistory.length))` → `document .getElementById()`
- 参照: `ContentArea.currentPlace`, `this._backHistory.length`, `this._forwardHistory.length`, `this._location`, `this._places.hasSelection`, `this.location`

## PO_back()
- 位置: L397-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._backHistory.shift()`, `this._forwardHistory.unshift()`
- 参照: `this._location`, `this.location`

## PO_forward()
- 位置: L403-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._backHistory.unshift()`, `this._forwardHistory.shift()`
- 参照: `this._location`, `this.location`

## PO_onPlaceSelected()
- 位置: L422-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `input.clear()`, `input.editor?.clearUndoRedo()`, `this._setSearchScopeForNode()`, `this.updateDetailsPane()`
- 参照: `ContentArea.currentPlace`, `PlacesSearchBox.searchFilter`, `node.uri`, `this._cachedLeftPaneSelectedURI`, `this._places.hasSelection`, `this._places.selectedNode`, `this.location`

## PO__setScopeForNode()
- 位置: L466-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsHistoryContainer()`
- 条件付き依存: `if ( PlacesUtils.nodeIsHistoryContainer(aNode) || itemGuid == PlacesUtils.virtualHistoryGuid )` → `PlacesQueryBuilder.setScope()`
- 条件付き依存: `if (itemGuid == PlacesUtils.virtualDownloadsGuid)` → `PlacesQueryBuilder.setScope()`
- 条件付き依存: `if (!(itemGuid == PlacesUtils.virtualDownloadsGuid))` → `PlacesQueryBuilder.setScope()`
- 参照: `PlacesUtils.virtualDownloadsGuid`, `PlacesUtils.virtualHistoryGuid`, `aNode.bookmarkGuid`

## PO_onPlacesListClick()
- 位置: L490-506
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node)` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (middleClick && PlacesUtils.nodeIsContainer(node))` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 参照: `aEvent.button`, `aEvent.detail`, `aEvent.target.localName`, `this._places`, `this._places.selectedNode`

## PO_updateDetailsPane()
- 位置: L511-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`
- 条件付き依存: `if (view)` → `this._fillDetailsPane()`
- 参照: `ContentArea.currentViewOptions.showDetailsPane`, `document.activeElement`, `view.selectedNode`, `view.selectedNodes`

## openFlatContainer()
- 位置: L535-542
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aContainer.bookmarkGuid)` → `PlacesUtils.asContainer()`
- 条件付き依存: `if (aContainer.bookmarkGuid)` → `this._places.selectItems()`
- 条件付き依存: `if (!(aContainer.bookmarkGuid))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(aContainer))` → `this._places.selectPlaceURI()`
- 参照: `PlacesUtils.asContainer(this._places.selectedNode).containerOpen`, `aContainer.bookmarkGuid`, `aContainer.uri`, `this._places.selectedNode`

## PO_getCurrentOptions()
- 位置: L549-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.asQuery()`
- 参照: `ContentArea.currentView.result.root`, `PlacesUtils.asQuery(ContentArea.currentView.result.root) .queryOptions`

## PO_importFromBrowser()
- 位置: L558-563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.showMigrationWizard()`
- 参照: `MigrationUtils.MIGRATION_ENTRYPOINTS.PLACES`

## PO_importFromFile()
- 位置: L568-588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesUIUtils.promptLocalization.formatValueSync()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterHTML`, `Ci.nsIFilePicker.modeOpen`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback_done()
- 位置: L570-577
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel && fp.fileURL)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel && fp.fileURL)` → `BookmarkHTMLUtils.importFromURL(fp.fileURL.spec).catch()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel && fp.fileURL)` → `BookmarkHTMLUtils.importFromURL()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `console.error`, `fp.fileURL`, `fp.fileURL.spec`
- XPCOM: `nsIFilePicker`

## PO_exportBookmarks()
- 位置: L593-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesUIUtils.promptLocalization.formatValueSync()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterHTML`, `Ci.nsIFilePicker.modeSave`, `fp.defaultString`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback_done()
- 位置: L595-602
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `BookmarkHTMLUtils.exportToFile(fp.file.path).catch()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `BookmarkHTMLUtils.exportToFile()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `console.error`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## PO_populateRestoreMenu()
- 位置: L619-679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadUtils.convertByteUnits()`, `IOUtils.stat()`, `PathUtils.filename()`, `PlacesBackups.getBackupFiles()`, `PlacesBackups.getBookmarkCountForFile()`, `PlacesBackups.getDateForFile()`, `PlacesUtils.getFormattedString()`, `dateFormatter.format()`, `document.createXULElement()`, `document.getElementById()`, `m.addEventListener()`, `m.setAttribute()`, `restorePopup.firstChild.remove()`, `restorePopup.insertBefore()`, `this.onRestoreMenuItemClick()`
- 条件付き依存: `if (count != null)` → `document.l10n.formatMessages()`
- 条件付き依存: `if (count != null)` → `msg.attributes.find()`
- 参照: `(await IOUtils.stat(file)).size`, `Services.intl.DateTimeFormat`, `attr.name`, `backupFiles.length`, `msg.attributes.find( attr => attr.name === "value" )?.value`, `restorePopup.childNodes.length`
- XPCOM: `Services.intl`

## onRestoreMenuItemClick()
- 位置: async L686-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.filename()`, `PlacesBackups.getBackupFiles()`, `aMenuItem.getAttribute()`
- 条件付き依存: `if (PathUtils.filename(backupFilePath) == backupName)` → `PlacesOrganizer.restoreBookmarksFromFile()`

## PO_onRestoreBookmarksFromFile()
- 位置: L701-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.dirsvc.get()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeOpen`, `fp.displayDirectory`, `window.browsingContext`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `nsIFilePicker` / `@mozilla.org/filepicker;1` / `Services.dirsvc`

## fpCallback()
- 位置: L704-708
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `this.restoreBookmarksFromFile()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## PO_restoreBookmarksFromFile()
- 位置: L728-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkJSONUtils.importFromFile()`, `PlacesOrganizer._showErrorAlert()`, `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.prompt.confirm()`, `aFilePath.toLowerCase()`, `aFilePath.toLowerCase().endsWith()`
- 条件付き依存: `if ( !aFilePath.toLowerCase().endsWith("json") && !aFilePath.toLowerCase().endsWith("jsonlz4") )` → `this._showErrorAlert()`
- XPCOM: `Services.prompt`

## PO__showErrorAlert()
- 位置: L758-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.prompt.alert()`
- XPCOM: `Services.prompt`

## PO_backupBookmarks()
- 位置: L771-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesBackups.getFilenameForDate()`, `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.dirsvc.get()`, `fp.appendFilter()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeSave`, `fp.defaultExtension`, `fp.defaultString`, `fp.displayDirectory`, `window.browsingContext`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `nsIFilePicker` / `@mozilla.org/filepicker;1` / `Services.dirsvc`

## fpCallback_done()
- 位置: L774-781
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `PlacesBackups.saveBookmarksToJSONFile(fp.file.path).catch()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `PlacesBackups.saveBookmarksToJSONFile()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `console.error`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## PO__fillDetailsPane()
- 位置: L796-879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsSeparator()`, `document.getElementById()`, `gEditItemOverlay.uninitPanel()`
- 条件付き依存: `if (selectedNode && !PlacesUtils.nodeIsSeparator(selectedNode))` → `gEditItemOverlay .initPanel({ node: selectedNode, hiddenRows: ["folderPicker"], }) .catch()`
- 条件付き依存: `if (selectedNode && !PlacesUtils.nodeIsSeparator(selectedNode))` → `gEditItemOverlay .initPanel()`
- 条件付き依存: `if (selectedNode && !PlacesUtils.nodeIsSeparator(selectedNode))` → `console.error()`
- 条件付き依存: `if (!selectedNode && aNodeList[0])` → `aNodeList.every()`
- 条件付き依存: `if (aNodeList.every(PlacesUtils.nodeIsURI))` → `aNodeList.map()`
- 条件付き依存: `if (aNodeList.every(PlacesUtils.nodeIsURI))` → `Services.io.newURI()`
- 条件付き依存: `if (aNodeList.every(PlacesUtils.nodeIsURI))` → `gEditItemOverlay .initPanel({ uris, hiddenRows: ["folderPicker", "location", "keyword", "name"], }) .catch()`
- 条件付き依存: `if (aNodeList.every(PlacesUtils.nodeIsURI))` → `gEditItemOverlay .initPanel()`
- 条件付き依存: `if (aNodeList.every(PlacesUtils.nodeIsURI))` → `console.error()`
- 条件付き依存: `if (!(aNodeList.every(PlacesUtils.nodeIsURI)))` → `document.getElementById()`
- 条件付き依存: `if (!(aNodeList.every(PlacesUtils.nodeIsURI)))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(!selectedNode && aNodeList[0]))` → `document.getElementById()`
- 条件付き依存: `if (itemsCount == 0)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(itemsCount == 0))` → `document.l10n.setAttributes()`
- 参照: `ContentArea.currentView.result`, `ContentArea.currentView.result.root`, `PlacesUtils.nodeIsURI`, `aNodeList.length`, `gEditItemOverlay.concreteGuid`, `gEditItemOverlay.multiEdit`, `gEditItemOverlay.uri`, `infoBox.hidden`, `itemsCountBox.hidden`, `node.uri`, `rootNode.childCount`, `rootNode.containerOpen`, `selectItemDesc.hidden`, `selectedNode.bookmarkGuid`, `selectedNode.uri`
- XPCOM: `Services.io`

## searchFilter()
- 位置: L895-897
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## folders()
- 位置: L906-911
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PlacesUtils.bookmarks.userContentRoots`, `this._folders`, `this._folders.length`

## folders()
- 位置: L912-914
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._folders`

## search()
- 位置: L924-979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.library.search.bookmarks.add()`, `PO.getCurrentOptions()`, `PlacesOrganizer.updateDetailsPane()`, `currentView.applyFilter()`
- 条件付き依存: `if (filterString == "")` → `PO.onPlaceSelected()`
- 条件付き依存: `if ( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `PlacesUtils.history.getNewQuery()`
- 条件付き依存: `if ( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `currentOptions.clone()`
- 条件付き依存: `if ( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `currentView.load()`
- 条件付き依存: `if (!( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY ))` → `Glean.library.historySearchTime.start()`
- 条件付き依存: `if (!( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY ))` → `currentView.applyFilter()`
- 条件付き依存: `if (!( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY ))` → `Glean.library.historySearchTime.stopAndAccumulate()`
- 条件付き依存: `if (!( currentOptions.queryType != Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY ))` → `Glean.library.search.history.add()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `ContentArea.currentView`, `PlacesSearchBox.filterCollection`, `currentOptions.RESULTS_AS_URI`, `currentOptions.queryType`, `currentView.searchTerm`, `options.includeHidden`, `options.queryType`, `options.resultType`, `query.searchTerms`, `this.cumulativeBookmarkSearches`, `this.cumulativeHistorySearches`, `this.folders`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## findAll()
- 位置: L984-997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesQueryBuilder.setScope()`, `this.focus()`
- 参照: `this.filterCollection`

## updatePlaceholder()
- 位置: L1002-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this.filterCollection`, `this.searchFilter`

## filterCollection()
- 位置: L1022-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchFilter.getAttribute()`

## filterCollection()
- 位置: L1025-1032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchFilter.setAttribute()`, `this.updatePlaceholder()`
- 参照: `this.filterCollection`

## focus()
- 位置: L1037-1039
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchFilter.focus()`

## init()
- 位置: L1044-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.search()`, `this.searchFilter.addEventListener()`, `this.updatePlaceholder()`
- 参照: `e.target.value`

## value()
- 位置: L1056-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.searchFilter.value`

## value()
- 位置: L1059-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.searchFilter.value`

## updateTelemetry()
- 位置: L1064-1089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.library.cumulativeHistorySearches.accumulateSingleSample()`, `Glean.library.link.history.add()`, `PlacesUtils.nodeIsBookmark()`, `urlsOpened.filter()`
- 条件付き依存: `if (!historyLinks.length)` → `Glean.library.cumulativeBookmarkSearches.accumulateSingleSample()`
- 条件付き依存: `if (!historyLinks.length)` → `Glean.library.link.bookmarks.add()`
- 参照: `PlacesSearchBox.cumulativeBookmarkSearches`, `PlacesSearchBox.cumulativeHistorySearches`, `historyLinks.length`, `link.isBookmark`, `urlsOpened.length`

## setScope()
- 位置: L1107-1133
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (searchStr)` → `PlacesSearchBox.search()`
- 参照: `PlacesSearchBox.filterCollection`, `PlacesSearchBox.folders`, `PlacesSearchBox.searchFilter.value`, `PlacesUtils.bookmarks.userContentRoots`

## init()
- 位置: L1140-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columnsPopup.addEventListener()`, `document.querySelector()`, `event.stopPropagation()`, `sortPopup.addEventListener()`, `this.fillWithColumns()`, `this.populateSortMenu()`, `this.setSortColumn()`, `this.showHideColumn()`
- 参照: `event.target`, `event.target.column`, `event.target.id`

## VM__clean()
- 位置: L1195-1226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popup.firstChild.remove()`, `popup.hasChildNodes()`
- 条件付き依存: `if (startID)` → `document.getElementById()`
- 条件付き依存: `if (endID)` → `document.getElementById()`
- 条件付き依存: `if (startID)` → `popup.removeChild()`
- 参照: `endElement.parentNode`, `startElement.nextSibling`, `startElement.parentNode`

## VM_fillWithColumns()
- 位置: L1247-1296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.getColumnAt()`, `document.createXULElement()`, `document.getElementById()`, `event.stopPropagation()`, `this._clean()`
- 条件付き依存: `if (localize)` → `SORTBY_L10N_IDS.get()`
- 条件付き依存: `if (localize)` → `column.getAttribute()`
- 条件付き依存: `if (localize)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(localize))` → `column.getAttribute()`
- 条件付き依存: `if (!(localize))` → `menuitem.setAttribute()`
- 条件付き依存: `if (type == "radio")` → `menuitem.setAttribute()`
- 条件付き依存: `if (type == "radio")` → `column.hasAttribute()`
- 条件付き依存: `if (column.hasAttribute("sortDirection"))` → `menuitem.setAttribute()`
- 条件付き依存: `if (type == "checkbox")` → `menuitem.setAttribute()`
- 条件付き依存: `if (type == "checkbox")` → `column.getAttribute()`
- 条件付き依存: `if (column.getAttribute("primary") == "true")` → `menuitem.setAttribute()`
- 条件付き依存: `if (!column.hidden)` → `menuitem.setAttribute()`
- 条件付き依存: `if (pivot)` → `popup.insertBefore()`
- 条件付き依存: `if (!(pivot))` → `popup.appendChild()`
- 参照: `column.hidden`, `column.id`, `columns.count`, `columns.getColumnAt(i).element`, `content.columns`, `event.target`, `menuitem.column`, `menuitem.id`

## VM_populateSortMenu()
- 位置: L1304-1332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._getSortColumn()`, `this.fillWithColumns()`
- 条件付き依存: `if (!sortColumn)` → `viewSortAscending.removeAttribute()`
- 条件付き依存: `if (!sortColumn)` → `viewSortDescending.removeAttribute()`
- 条件付き依存: `if (!sortColumn)` → `viewUnsorted.setAttribute()`
- 条件付き依存: `if (!(!sortColumn))` → `sortColumn.getAttribute()`
- 条件付き依存: `if (sortColumn.getAttribute("sortDirection") == "ascending")` → `viewSortAscending.setAttribute()`
- 条件付き依存: `if (sortColumn.getAttribute("sortDirection") == "ascending")` → `viewSortDescending.removeAttribute()`
- 条件付き依存: `if (sortColumn.getAttribute("sortDirection") == "ascending")` → `viewUnsorted.removeAttribute()`
- 条件付き依存: `if (!(sortColumn.getAttribute("sortDirection") == "ascending"))` → `sortColumn.getAttribute()`
- 条件付き依存: `if (sortColumn.getAttribute("sortDirection") == "descending")` → `viewSortDescending.setAttribute()`
- 条件付き依存: `if (sortColumn.getAttribute("sortDirection") == "descending")` → `viewSortAscending.removeAttribute()`
- 条件付き依存: `if (sortColumn.getAttribute("sortDirection") == "descending")` → `viewUnsorted.removeAttribute()`

## VM_showHideColumn()
- 位置: L1340-1353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.hasAttribute()`
- 参照: `column.hidden`, `column.nextSibling`, `element.column`, `splitter.hidden`, `splitter.localName`

## VM__getSortColumn()
- 位置: L1360-1371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cols.getColumnAt()`, `column.getAttribute()`, `document.getElementById()`
- 参照: `cols.count`, `cols.getColumnAt(i).element`, `content.columns`

## VM_setSortColumn()
- 位置: L1385-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aDirection || colLookupTable[columnId].dir).toUpperCase()`, `colLookupTable.hasOwnProperty()`, `document.getElementById()`
- 条件付き依存: `if (aColumn)` → `aColumn.getAttribute()`
- 条件付き依存: `if (!aDirection)` → `this._getSortColumn()`
- 条件付き依存: `if (sortColumn)` → `sortColumn.getAttribute()`
- 条件付き依存: `if (!(aColumn))` → `this._getSortColumn()`
- 条件付き依存: `if (!(aColumn))` → `sortColumn.getAttribute()`
- 参照: `Ci.nsINavHistoryQueryOptions`, `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `colLookupTable[columnId].dir`, `colLookupTable[columnId].key`, `document.getElementById("placeContent").result`, `result.sortingMode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## CA_init()
- 位置: L1440-1445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentTree.init()`, `document.getElementById()`, `this._setupView()`
- 参照: `this._box`, `this._toolbar`

## CA_getContentViewForQueryString()
- 位置: L1456-1472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._specialViews.has()`
- 条件付き依存: `if (this._specialViews.has(aQueryString))` → `this._specialViews.get()`
- 条件付き依存: `if (typeof view == "function")` → `view()`
- 条件付き依存: `if (typeof view == "function")` → `this._specialViews.set()`
- 参照: `ContentTree.view`

## CA_setContentViewForQueryString()
- 位置: L1487-1503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._specialViews.set()`

## currentView()
- 位置: L1505-1510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `[...this._box.children].filter()`
- 参照: `child.hidden`, `this._box.children`

## currentView()
- 位置: L1511-1523
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.activeElement == oldView.associatedElement)` → `aNewView.associatedElement.focus()`
- 参照: `aNewView.associatedElement.hidden`, `document.activeElement`, `oldView.associatedElement`, `oldView.associatedElement.hidden`, `this.currentView`

## currentPlace()
- 位置: L1525-1527
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentView.place`

## currentPlace()
- 位置: L1528-1538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getContentViewForQueryString()`
- 条件付き依存: `if (oldView != newView)` → `this._setupView()`
- 参照: `newView.active`, `newView.place`, `oldView.active`, `this.currentView`

## CA__setupView()
- 位置: L1543-1561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (elt.id == "placesMenu")` → `options.toolbarSet.includes()`
- 条件付き依存: `if (!(elt.id == "placesMenu"))` → `options.toolbarSet.includes()`
- 参照: `detailsPane.hidden`, `elt.childNodes`, `elt.hidden`, `elt.id`, `menuElt.hidden`, `menuElt.id`, `options.showDetailsPane`, `this._toolbar.childNodes`, `this.currentViewOptions`

## currentViewOptions()
- 位置: L1569-1579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._specialViews.has()`
- 条件付き依存: `if (this._specialViews.has(this.currentPlace))` → `this._specialViews.get()`
- 参照: `ContentTree.viewOptions`, `this.currentPlace`

## focus()
- 位置: L1581-1583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.currentView.associatedElement.focus()`

## CT_init()
- 位置: L1587-1593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelector()`, `document .querySelector("#placeContent > treechildren") .addEventListener()`, `document.getElementById()`, `this.view.addEventListener()`
- 参照: `this._view`

## view()
- 位置: L1595-1597
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._view`

## viewOptions()
- 位置: L1599-1605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.seal()`

## CT_openSelectedNode()
- 位置: L1607-1610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.openNodeWithEvent()`
- 参照: `this.view`, `view.selectedNode`

## handleEvent()
- 位置: L1612-1621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onClick()`, `this.onKeyPress()`
- 参照: `event.type`

## CT_onClick()
- 位置: L1623-1638
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node)` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node) && (doubleClick || middleClick))` → `this.openSelectedNode()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsURI(node) && (doubleClick || middleClick)))` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (middleClick && PlacesUtils.nodeIsContainer(node))` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 参照: `aEvent.button`, `aEvent.detail`, `this.view`, `this.view.selectedNode`

## CT_onKeyPress()
- 位置: L1640-1644
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_RETURN)` → `this.openSelectedNode()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.keyCode`
