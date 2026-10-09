# browser/components/downloads/content/allDownloadsView.js

source: browser/components/downloads/content/allDownloadsView.js
source-hash: e82abc481aaa14c4c90c89ef9eeb855fdf1acf40
lines: 954

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Object.setPrototypeOf()`, `document.addEventListener()`, `document.getElementById()`, `dropNode.addEventListener()`, `richListBox._placesView.onDragOver()`, `richListBox._placesView.onDrop()`, `richListBox.addEventListener()`, `this._placesView.onContextMenu()`, `this._placesView.onDoubleClick()`, `this._placesView.onDragStart()`, `this._placesView.onKeyPress()`, `this._placesView.onScroll()`, `this._placesView.onSelect()`

## HistoryDownloadElementShell()
- 位置: L45-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `this.element.classList.add()`
- 参照: `this._download`, `this.element`, `this.element._shell`

## download()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._download`

## onStateChanged()
- 位置: L64-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateState()`
- 条件付き依存: `if (this.element.selected)` → `goUpdateDownloadCommands()`
- 条件付き依存: `if (!(this.element.selected))` → `goUpdateCommand()`
- 参照: `this._targetFileChecked`, `this.element.selected`

## onChanged()
- 位置: L79-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.stateOfDownload()`
- 条件付き依存: `if (this._downloadState !== newState)` → `this.onStateChanged()`
- 条件付き依存: `if (!(this._downloadState !== newState))` → `this._updateStateInner()`
- 参照: `this._downloadState`, `this.active`, `this.download`

## isCommandEnabled()
- 位置: L95-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.DownloadElementShell.prototype.isCommandEnabled.call()`
- 参照: `this.active`

## downloadsCmd_unblock()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.confirmUnblock()`

## downloadsCmd_unblockAndSave()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.confirmUnblock()`

## downloadsCmd_chooseUnblock()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.confirmUnblock()`

## downloadsCmd_chooseOpen()
- 位置: L117-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.confirmUnblock()`

## matchesSearchTerm()
- 位置: L124-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.download.source.originalUrl || this.download.source.url) .toLowerCase()`, `(this.download.source.originalUrl || this.download.source.url) .toLowerCase() .includes()`, `DownloadsViewUI.getDisplayName()`, `aTerm.toLowerCase()`, `displayName.toLowerCase()`, `displayName.toLowerCase().includes()`
- 参照: `this.download`, `this.download.source.originalUrl`, `this.download.source.url`

## doDefaultCommand()
- 位置: L140-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isCommandEnabled()`
- 条件付き依存: `if ( command == "downloadsCmd_open" && event && (event.shiftKey || event.ctrlKey || event.metaKey || event.button == 1) )` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if ( command == "downloadsCmd_open" && event && (event.shiftKey || event.ctrlKey || event.metaKey || event.button == 1) )` → `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if ( command == "downloadsCmd_open" && event && (event.shiftKey || event.ctrlKey || event.metaKey || event.button == 1) )` → `["window", "tabshifted", "tab"].includes()`
- 条件付き依存: `if (command && this.isCommandEnabled(command))` → `this.doCommand()`
- 参照: `event.button`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `this.currentDefaultCommandName`

## onSelect()
- 位置: L169-191
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._targetFileChecked)` → `this.download .refresh() .catch(console.error) .then()`
- 条件付き依存: `if (!this._targetFileChecked)` → `this.download .refresh() .catch()`
- 条件付き依存: `if (!this._targetFileChecked)` → `this.download .refresh()`
- 参照: `console.error`, `this._targetFileChecked`, `this.active`, `this.download.target.path`

## onDownloadButton()
- 位置: L202-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`, `event.target.closest("richlistitem")._shell.onButton()`

## onDownloadClick()
- 位置: L206-206
- 役割: (未記入)
- 触るとき: (未記入)

## DownloadsPlacesView()
- 位置: L221-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getIndicatorData()`, `this._downloadsData.addView()`, `this._downloadsData.removeView()`, `this._ensureVisibleElementsAreActive()`, `window.addEventListener()`, `window.controllers.insertControllerAt()`, `window.controllers.removeController()`
- 条件付き依存: `if (aSuppressionFlag === DownloadsCommon.SUPPRESS_ALL_DOWNLOADS_OPEN)` → `DownloadsCommon.getIndicatorData()`
- 参照: `DownloadsCommon.SUPPRESS_ALL_DOWNLOADS_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `this._active`, `this._downloadsData`, `this._initiallySelectedElement`, `this._richlistbox`, `this._richlistbox._placesView`, `this._searchTerm`, `this._viewItemsForDownloads`, `this._waitingForInitialData`, `this.result`, `window.opener`

## associatedElement()
- 位置: L275-277
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._richlistbox`

## active()
- 位置: L279-281
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._active`

## active()
- 位置: L282-287
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._active)` → `this._ensureVisibleElementsAreActive()`
- 参照: `this._active`

## _ensureVisibleElementsAreActive()
- 位置: L298-314
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (debounce)` → `setTimeout()`
- 条件付き依存: `if (debounce)` → `this._internalEnsureVisibleElementsAreActive()`
- 条件付き依存: `if (!(debounce))` → `this._internalEnsureVisibleElementsAreActive()`
- 参照: `this._ensureVisibleTimer`, `this._richlistbox.firstChild`, `this.active`

## _internalEnsureVisibleElementsAreActive()
- 位置: L316-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._richlistbox.getBoundingClientRect()`, `winUtils.nodesFromRect()`
- 条件付き依存: `if (this._ensureVisibleTimer)` → `clearTimeout()`
- 条件付き依存: `if (node.localName === "richlistitem" && node._shell)` → `node._shell.ensureActive()`
- 条件付き依存: `if (nodeBelowVisibleArea && nodeBelowVisibleArea._shell)` → `nodeBelowVisibleArea._shell.ensureActive()`
- 条件付き依存: `if (nodeAboveVisibleArea && nodeAboveVisibleArea._shell)` → `nodeAboveVisibleArea._shell.ensureActive()`
- 参照: `firstVisibleNode.previousSibling`, `lastVisibleNode.nextSibling`, `node._shell`, `node.localName`, `nodeAboveVisibleArea._shell`, `nodeBelowVisibleArea._shell`, `rlbRect.height`, `rlbRect.left`, `rlbRect.top`, `rlbRect.width`, `this._ensureVisibleTimer`, `this._richlistbox.firstChild`, `window.windowUtils`

## place()
- 位置: L378-380
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._place`

## place()
- 位置: L381-388
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._place`, `this.searchTerm`

## selectedNodes()
- 位置: L390-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.filter.call()`
- 参照: `element._shell.download.placesNode`, `this._richlistbox.selectedItems`

## selectedNode()
- 位置: L397-400
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `selectedNodes.length`, `this.selectedNodes`

## hasSelection()
- 位置: L402-404
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectedNodes.length`

## controller()
- 位置: L406-408
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._richlistbox.controller`

## searchTerm()
- 位置: L410-412
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._searchTerm`

## searchTerm()
- 位置: L413-425
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._searchTerm != aValue)` → `this._richlistbox.clearSelection()`
- 条件付き依存: `if (this._searchTerm != aValue)` → `element._shell.matchesSearchTerm()`
- 条件付き依存: `if (this._searchTerm != aValue)` → `this._ensureVisibleElementsAreActive()`
- 参照: `element.hidden`, `this._richlistbox.childNodes`, `this._searchTerm`

## _ensureInitialSelection()
- 位置: L442-455
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (firstDownloadElement != this._initiallySelectedElement)` → `firstDownloadElement._shell.ensureActive()`
- 参照: `this._initiallySelectedElement`, `this._richlistbox.currentItem`, `this._richlistbox.firstChild`, `this._richlistbox.selectedItem`

## onDownloadBatchStarting()
- 位置: L466-471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createDocumentFragment()`
- 参照: `this._richlistbox.suppressOnSelect`, `this.batchFragment`, `this.oldSuppressOnSelect`

## onDownloadBatchEnded()
- 位置: L473-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `goUpdateDownloadCommands()`, `this._ensureInitialSelection()`, `this._ensureVisibleElementsAreActive()`
- 条件付き依存: `if (this.batchFragment.childElementCount)` → `this._prependBatchFragment()`
- 条件付き依存: `if (this._waitingForInitialData)` → `this._richlistbox.dispatchEvent()`
- 参照: `this._richlistbox.suppressOnSelect`, `this._waitingForInitialData`, `this.batchFragment`, `this.batchFragment.childElementCount`, `this.oldSuppressOnSelect`

## _prependBatchFragment()
- 位置: L493-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.getOwnPropertyNames()`, `parentNode.insertBefore()`, `parentNode.removeChild()`, `this._richlistbox.prepend()`, `xblFields.set()`
- 条件付き依存: `if (oldActiveElement && oldActiveElement != document.activeElement)` → `oldActiveElement.focus()`
- 参照: `document.activeElement`, `this._richlistbox`, `this._richlistbox.nextSibling`, `this._richlistbox.parentNode`, `this.batchFragment`

## onDownloadAdded()
- 位置: L520-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._viewItemsForDownloads.set()`
- 条件付き依存: `if (insertBefore)` → `this._viewItemsForDownloads .get(insertBefore) .element.insertAdjacentElement()`
- 条件付き依存: `if (insertBefore)` → `this._viewItemsForDownloads .get()`
- 条件付き依存: `if (!(insertBefore))` → `(this.batchFragment || this._richlistbox).prepend()`
- 条件付き依存: `if (this.searchTerm)` → `shell.matchesSearchTerm()`
- 条件付き依存: `if (!this.batchFragment)` → `this._ensureVisibleElementsAreActive()`
- 条件付き依存: `if (!this.batchFragment)` → `goUpdateCommand()`
- 参照: `shell.element`, `shell.element.hidden`, `this._richlistbox`, `this.batchFragment`, `this.searchTerm`

## onDownloadChanged()
- 位置: L545-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._viewItemsForDownloads.get()`, `this._viewItemsForDownloads.get(download).onChanged()`

## onDownloadRemoved()
- 位置: L549-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.remove()`, `this._richlistbox.removeItemFromSelection()`, `this._viewItemsForDownloads.get()`
- 条件付き依存: `if ( (element.nextSibling || element.previousSibling) && this._richlistbox.selectedItems && this._richlistbox.selectedItems.length == 1 && this._richlistbox.sele...)` → `this._richlistbox.selectItem()`
- 条件付き依存: `if (!this.batchFragment)` → `this._ensureVisibleElementsAreActive()`
- 条件付き依存: `if (!this.batchFragment)` → `goUpdateCommand()`
- 参照: `element.nextSibling`, `element.previousSibling`, `this._richlistbox.selectedItems`, `this._richlistbox.selectedItems.length`, `this._viewItemsForDownloads.get(download).element`, `this.batchFragment`

## supportsCommand()
- 位置: L576-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.isCommandName()`
- 参照: `HistoryDownloadElementShell.prototype`, `document.activeElement`, `this._richlistbox`

## isCommandEnabled()
- 位置: L600-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.every.call()`, `Array.prototype.some.call()`, `Services.clipboard.hasDataMatchingFlavors()`, `element._shell.isCommandEnabled()`, `this.canClearDownloads()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `element._shell.download`, `source?.originalUrl`, `source?.url`, `this._richlistbox`, `this._richlistbox.selectedItems`, `this._richlistbox.selectedItems.length`
- XPCOM: `nsIClipboard` / `Services.clipboard`

## _copySelectedDownloadsToClipboard()
- 位置: L631-640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Cc["@mozilla.org/widget/clipboardhelper;1"] .getService()`, `Cc["@mozilla.org/widget/clipboardhelper;1"] .getService(Ci.nsIClipboardHelper) .copyString()`, `urls.join()`
- 参照: `Ci.nsIClipboardHelper`, `element._shell.download`, `source?.originalUrl`, `source?.url`, `this._richlistbox.selectedItems`
- XPCOM: `nsIClipboardHelper` / `@mozilla.org/widget/clipboardhelper;1`

## _getURLFromClipboardData()
- 位置: L642-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CLIPBOARD_URL_FLAVORS.forEach()`, `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `Services.clipboard.getData()`, `data.value .QueryInterface()`, `data.value .QueryInterface(Ci.nsISupportsString) .data.split()`, `trans.getAnyTransferData()`, `trans.init()`
- 条件付き依存: `if (url)` → `NetUtil.newURI()`
- 参照: `Ci.nsISupportsString`, `Ci.nsITransferable`, `NetUtil.newURI(url).spec`, `Services.clipboard.kGlobalClipboard`, `trans.addDataFlavor`
- XPCOM: [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## doCommand()
- 位置: L668-688
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element._shell.doCommand()`, `this.isCommandEnabled()`
- 条件付き依存: `if (aCommand in this)` → `this[aCommand]()`
- 参照: `this._richlistbox.selectedItems`

## onEvent()
- 位置: L691-691
- 役割: (未記入)
- 触るとき: (未記入)

## cmd_copy()
- 位置: L693-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._copySelectedDownloadsToClipboard()`

## cmd_selectAll()
- 位置: L697-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._richlistbox.clearSelection()`, `this._richlistbox.getItemAtIndex()`, `this._richlistbox.getNextItem()`
- 条件付き依存: `if (!this.searchTerm)` → `this._richlistbox.selectAll()`
- 条件付き依存: `if (!item.hidden)` → `this._richlistbox.addItemToSelection()`
- 参照: `item.hidden`, `this._richlistbox.suppressOnSelect`, `this.searchTerm`

## cmd_paste()
- 位置: L717-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getURLFromClipboardData()`
- 条件付き依存: `if (url)` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (url)` → `DownloadURL()`
- 参照: `browserWin.document`

## downloadsCmd_clearDownloads()
- 位置: L726-738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `goUpdateCommand()`, `this._downloadsData.removeFinished()`
- 条件付き依存: `if (this._place)` → `PlacesUtils.history .removeVisitsByFilter({ transition: PlacesUtils.history.TRANSITIONS.DOWNLOAD, }) .catch()`
- 条件付き依存: `if (this._place)` → `PlacesUtils.history .removeVisitsByFilter()`
- 参照: `PlacesUtils.history.TRANSITIONS.DOWNLOAD`, `console.error`, `this._place`

## onContextMenu()
- 位置: L740-771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.some.call()`, `DownloadsViewUI.updateContextMenuForElement()`, `contextMenu.querySelector()`, `document.getElementById()`
- 条件付き依存: `if (!download.stopped)` → `goUpdateCommand()`
- 参照: `contextMenu.querySelector(".downloadCopyLocationMenuItem").hidden`, `contextMenu.querySelector(".downloadLinksSeparator").hidden`, `contextMenu.querySelector(".downloadOpenReferrerMenuItem").hidden`, `download.stopped`, `el._shell.download.source?.isDataURICleared`, `el._shell.download.source?.url`, `element._shell`, `element._shell.download`, `this._richlistbox.selectedItem`, `this._richlistbox.selectedItems`

## onKeyPress()
- 位置: L773-799
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (element._shell)` → `element._shell.doDefaultCommand()`
- 条件付き依存: `if (!(aEvent.keyCode == KeyEvent.DOM_VK_RETURN))` → `" ".charCodeAt()`
- 条件付き依存: `if (aEvent.charCode == " ".charCodeAt(0))` → `element._shell.isCommandEnabled()`
- 条件付き依存: `if (element._shell.isCommandEnabled("downloadsCmd_pauseResume"))` → `element._shell.doCommand()`
- 条件付き依存: `if (atLeastOneDownloadToggled)` → `aEvent.preventDefault()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.charCode`, `aEvent.keyCode`, `element._shell`, `selectedElements.length`, `this._richlistbox.selectedItems`

## onDoubleClick()
- 位置: L801-815
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (element._shell)` → `element._shell.doDefaultCommand()`
- 参照: `aEvent.button`, `element._shell`, `selectedElements.length`, `this._richlistbox.selectedItems`

## onScroll()
- 位置: L817-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ensureVisibleElementsAreActive()`

## onSelect()
- 位置: L821-830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `goUpdateDownloadCommands()`
- 条件付き依存: `if (elt._shell)` → `elt._shell.onSelect()`
- 参照: `elt._shell`, `this._richlistbox.selectedItems`

## onDragStart()
- 位置: L832-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newFileURI()`, `dt.addElement()`, `dt.mozSetDataAt()`, `dt.setData()`, `file.exists()`
- 参照: `FileUtils.File`, `Services.io.newFileURI(file).spec`, `aEvent.dataTransfer`, `dt.effectAllowed`, `selectedItem._shell.download.target.path`, `this._richlistbox.selectedItem`
- XPCOM: `Services.io`

## onDragOver()
- 位置: L859-868
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `types.includes()`
- 条件付き依存: `if ( types.includes("text/uri-list") || types.includes("text/x-moz-url") || types.includes("text/plain") )` → `aEvent.preventDefault()`
- 参照: `aEvent.dataTransfer.types`

## onDrop()
- 位置: L870-891
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `DownloadURL()`, `Services.droppedLinkHandler.dropLinks()`, `aEvent.preventDefault()`, `dt.mozGetDataAt()`, `link.url.startsWith()`
- 参照: `aEvent.dataTransfer`, `browserWin.document`, `link.name`, `link.url`, `links.length`
- XPCOM: `Services.droppedLinkHandler`

## DownloadsPlacesView.prototype[methodName]()
- 位置: L899-903
- 役割: (未記入)
- 触るとき: (未記入)

## goUpdateDownloadCommands()
- 位置: L906-916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateCommandsForObject()`
- 参照: `DownloadsPlacesView.prototype`, `HistoryDownloadElementShell.prototype`

## updateCommandsForObject()
- 位置: L907-913
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.isCommandName()`
- 条件付き依存: `if (DownloadsViewUI.isCommandName(name))` → `goUpdateCommand()`
