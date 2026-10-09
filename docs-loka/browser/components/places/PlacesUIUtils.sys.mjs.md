# browser/components/places/PlacesUIUtils.sys.mjs

source: browser/components/places/PlacesUIUtils.sys.mjs
source-hash: 16b4b7bf0e18fba11ea3f7b91fd680a831c2fd83
lines: 2121

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `["toolbar", "menu", "unfiled"].includes()`, `lazy.PlacesUtils.bookmarks .fetch()`, `lazy.PlacesUtils.bookmarks .fetch({ guid: prefValue }) .then()`

## BookmarkState.constructor()
- 位置: L61-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info.uris?.map()`, `tags .trim()`, `tags .trim() .split()`, `tags .trim() .split(/\s*,\s*/) .filter()`
- 参照: `info.isTag`, `info.itemGuid`, `info.parentGuid`, `info.postData`, `info.tag`, `info.title`, `info.uri?.spec`, `tag.length`, `this._autosave`, `this._bulkTaggingUrls`, `this._children`, `this._guid`, `this._isFolder`, `this._isTagContainer`, `this._newState`, `this._originalState`, `this._postData`, `uri.spec`

## BookmarkState._titleChanged()
- 位置: async L101-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.title`

## BookmarkState._locationChanged()
- 位置: async L112-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.uri`

## BookmarkState._tagsChanged()
- 位置: async L123-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.tags`

## BookmarkState._keywordChanged()
- 位置: async L134-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.keyword`

## BookmarkState._parentGuidChanged()
- 位置: async L145-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.parentGuid`

## BookmarkState._maybeSave()
- 位置: async L153-157
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._autosave)` → `this.save()`
- 参照: `this._autosave`

## BookmarkState._createBookmark()
- 位置: async L164-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesTransactions.NewBookmark()`, `lazy.PlacesTransactions.batch()`
- 条件付き依存: `if (this._newState.keyword)` → `transactions.push()`
- 条件付き依存: `if (this._newState.keyword)` → `lazy.PlacesTransactions.EditKeyword()`
- 参照: `this._guid`, `this._newState.keyword`, `this._newState.tags`, `this._newState.title`, `this._newState.uri`, `this._originalState.index`, `this._originalState.title`, `this._originalState.uri`, `this._postData`, `this.parentGuid`

## BookmarkState._createFolder()
- 位置: async L196-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesTransactions.NewFolder()`, `lazy.PlacesTransactions.batch()`
- 条件付き依存: `if (this._bulkTaggingUrls)` → `this._appendTagsTransactions()`
- 参照: `this._bulkTaggingUrls`, `this._children`, `this._guid`, `this._newState.tags`, `this._newState.title`, `this._originalState.index`, `this._originalState.tags`, `this._originalState.title`, `this.parentGuid`

## BookmarkState.parentGuid()
- 位置: L224-226
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._newState.parentGuid`, `this._originalState.parentGuid`

## BookmarkState.save()
- 位置: async L233-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.keys()`, `lazy.PlacesTransactions.EditKeyword()`, `lazy.PlacesTransactions.EditTitle()`, `lazy.PlacesTransactions.Move()`, `this._appendTagsTransactions()`, `transactions.push()`
- 条件付き依存: `if (this._guid === lazy.PlacesUtils.bookmarks.unsavedGuid)` → `this._createFolder()`
- 条件付き依存: `if (this._guid === lazy.PlacesUtils.bookmarks.unsavedGuid)` → `this._createBookmark()`
- 条件付き依存: `if (this._isTagContainer && this._newState.title)` → `lazy.PlacesTransactions.RenameTag({ oldTag: this._originalState.title, tag: this._newState.title, }) .transact() .catch()`
- 条件付き依存: `if (this._isTagContainer && this._newState.title)` → `lazy.PlacesTransactions.RenameTag({ oldTag: this._originalState.title, tag: this._newState.title, }) .transact()`
- 条件付き依存: `if (this._isTagContainer && this._newState.title)` → `lazy.PlacesTransactions.RenameTag()`
- 条件付き依存: `if (this._newState.uri)` → `transactions.push()`
- 条件付き依存: `if (this._newState.uri)` → `lazy.PlacesTransactions.EditUrl()`
- 条件付き依存: `if (transactions.length)` → `lazy.PlacesTransactions.batch()`
- 参照: `Object.keys(this._newState).length`, `console.error`, `lazy.PlacesUtils.bookmarks.unsavedGuid`, `this._bulkTaggingUrls`, `this._guid`, `this._isFolder`, `this._isTagContainer`, `this._newState`, `this._newState.parentGuid`, `this._newState.title`, `this._newState.uri`, `this._originalState`, `this._originalState.keyword`, `this._originalState.tags`, `this._originalState.title`, `this._originalState.uri`, `this._postData`, `transactions.length`

## BookmarkState._appendTagsTransactions()
- 位置: L326-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `newTags.filter()`, `newTags.includes()`, `originalTags.filter()`, `originalTags.includes()`
- 条件付き依存: `if (addedTags.length)` → `transactions.push()`
- 条件付き依存: `if (addedTags.length)` → `lazy.PlacesTransactions.Tag()`
- 条件付き依存: `if (removedTags.length)` → `transactions.push()`
- 条件付き依存: `if (removedTags.length)` → `lazy.PlacesTransactions.Untag()`
- 参照: `addedTags.length`, `removedTags.length`

## obfuscateUrlForXulStore()
- 位置: L376-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.md5()`, `url.indexOf()`, `url.startsWith()`, `url.substring()`

## showBookmarkDialog()
- 位置: async L399-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `this.lastBookmarkDialogDeferred.resolve()`
- 条件付き依存: `if (!aParentWindow)` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (aParentWindow.gDialogBox)` → `aParentWindow.gDialogBox.open()`
- 条件付き依存: `if (!(aParentWindow.gDialogBox))` → `aParentWindow.openDialog()`
- 条件付き依存: `if (aInfo.bookmarkState)` → `aInfo.bookmarkState.save()`
- 条件付き依存: `if (aInfo.bookmarkState)` → `this.lastBookmarkDialogDeferred.resolve()`
- 参照: `aInfo.bookmarkState`, `aParentWindow.gDialogBox`, `this.lastBookmarkDialogDeferred`
- XPCOM: `Services.wm`

## showBookmarkPagesDialog()
- 位置: async L437-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.showBookmarkDialog()`
- 参照: `URIList.length`, `URIList[0].title`, `URIList[0].uri`, `bookmarkDialogInfo.URIList`, `bookmarkDialogInfo.title`, `bookmarkDialogInfo.type`, `bookmarkDialogInfo.uri`

## PUIU_getViewForNode()
- 位置: L462-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.isDeadWrapper()`, `Element.isInstance()`, `node.getAttribute()`
- 参照: `node._placesNode`, `node._placesView`, `node.localName`, `node.menupopup._placesView`, `node.parentNode`

## getControllerForCommand()
- 位置: L507-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.top.document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if (popupNode)` → `popupNode.closest()`
- 条件付き依存: `if (popupNode)` → `this.getViewForNode()`
- 条件付き依存: `if (view && view._contextMenuShown)` → `view.controllers.getControllerForCommand()`
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`, `this.managedBookmarksController`, `view._contextMenuShown`

## updateCommands()
- 位置: L534-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.isCommandEnabled()`, `this.getControllerForCommand()`, `win.goSetCommandEnabled()`

## doCommand()
- 位置: L567-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.isCommandEnabled()`, `this.getControllerForCommand()`
- 条件付き依存: `if (controller && controller.isCommandEnabled(command))` → `controller.doCommand()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`

## PUIU_markPageAsTyped()
- 位置: L586-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `lazy.PlacesUtils.history.markPageAsTyped()`
- 参照: `Services.uriFixup.getFixupURIInfo(aURL).preferredURI`
- XPCOM: `Services.uriFixup`

## PUIU_markPageAsFollowedBookmark()
- 位置: L602-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `lazy.PlacesUtils.history.markPageAsFollowedBookmark()`
- 参照: `Services.uriFixup.getFixupURIInfo(aURL).preferredURI`
- XPCOM: `Services.uriFixup`

## PUIU_markPageAsFollowedLink()
- 位置: L617-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `lazy.PlacesUtils.history.markPageAsFollowedLink()`
- 参照: `Services.uriFixup.getFixupURIInfo(aURL).preferredURI`
- XPCOM: `Services.uriFixup`

## setCharsetForPage()
- 位置: async L632-647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `charset.toLowerCase()`, `lazy.PlacesUtils.history.update()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `lazy.PlacesUtils.CHARSET_ANNO`

## checkURLSecurity()
- 位置: L659-675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.nodeIsBookmark()`, `uri.schemeIs()`
- 条件付き依存: `if (uri.schemeIs("javascript") || uri.schemeIs("data"))` → `PlacesUIUtils.promptLocalization.formatValuesSync()`
- 条件付き依存: `if (uri.schemeIs("javascript") || uri.schemeIs("data"))` → `Services.prompt.alert()`
- 参照: `aURINode.uri`
- XPCOM: `Services.io` / `Services.prompt`

## canUserRemove()
- 位置: L685-714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.nodeIsQuery()`, `this.isFolderReadOnly()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsQuery(parentNode))` → `lazy.PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsFolderOrShortcut(aNode))` → `lazy.PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsFolderOrShortcut(aNode))` → `lazy.PlacesUtils.isRootItem()`
- 条件付き依存: `if (!(lazy.PlacesUtils.nodeIsFolderOrShortcut(aNode)))` → `lazy.PlacesUtils.isVirtualLeftPaneItem()`
- 参照: `aNode.bookmarkGuid`, `aNode.itemId`, `aNode.parent`

## isFolderReadOnly()
- 位置: L734-746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.getConcreteItemGuid()`, `lazy.PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `lazy.PlacesUtils.bookmarks.rootGuid`

## openTabset()
- 位置: L757-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `browserWindow.gBrowser.loadTabs()`, `getBrowserWindow()`, `item.uri.startsWith()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `tabs.entries()`, `urls.push()`
- 条件付き依存: `if (item.isBookmark)` → `this.markPageAsFollowedBookmark()`
- 条件付き依存: `if (!(item.isBookmark))` → `this.markPageAsTyped()`
- 条件付き依存: `if (where == "window")` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (where == "window")` → `urls.forEach()`
- 条件付き依存: `if (where == "window")` → `stringsToLoad.appendElement()`
- 条件付き依存: `if (where == "window")` → `lazy.PlacesUtils.toISupportsString()`
- 条件付き依存: `if (where == "window")` → `args.appendElement()`
- 条件付き依存: `if (where == "window")` → `Services.ww.openWindow()`
- 条件付き依存: `if (item.isBookmark && !item.uri.startsWith("javascript:"))` → `lazy.WebNavigationManager.setRecentTabTransitionData()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `aItemsToOpen.length`, `item.isBookmark`, `item.uri`, `tab.linkedBrowser`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1` / `Services.scriptSecurityManager` / `Services.ww`

## openMultipleLinksInTabs()
- 位置: L844-867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OpenInTabsUtils.confirmOpenInTabs()`, `lazy.PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsContainer(nodeOrNodes))` → `lazy.PlacesUtils.getURLsForContainerNode()`
- 条件付き依存: `if (!(lazy.PlacesUtils.nodeIsContainer(nodeOrNodes)))` → `lazy.PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsURI(nodeOrNodes[i]))` → `urlsToOpen.push()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsURI(nodeOrNodes[i]))` → `lazy.PlacesUtils.nodeIsBookmark()`
- 条件付き依存: `if (window.updateTelemetry)` → `window.updateTelemetry()`
- 条件付き依存: `if (lazy.OpenInTabsUtils.confirmOpenInTabs(urlsToOpen.length, window))` → `this.openTabset()`
- 参照: `nodeOrNodes.length`, `nodeOrNodes[i].uri`, `urlsToOpen.length`, `view.ownerWindow`, `window.updateTelemetry`

## PUIU_openNodeWithEvent()
- 位置: L880-895
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.whereToOpenLink()`, `lazy.PlacesUtils.nodeIsBookmark()`, `this._openNodeIn()`
- 条件付き依存: `if (this.loadBookmarksInTabs && lazy.PlacesUtils.nodeIsBookmark(aNode))` → `aNode.uri.startsWith()`
- 条件付き依存: `if (this.loadBookmarksInTabs && lazy.PlacesUtils.nodeIsBookmark(aNode))` → `getBrowserWindow()`
- 参照: `aEvent.target.documentGlobal`, `browserWindow?.gBrowser.selectedTab.isEmpty`, `this.loadBookmarksInTabs`

## PUIU_openNodeIn()
- 位置: L910-913
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openNodeIn()`
- 参照: `aView.ownerWindow`

## PUIU__openNodeIn()
- 位置: L915-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.checkURLSecurity()`, `this.isURILike()`
- 条件付き依存: `if ( aNode && this.checkURLSecurity(aNode, aWindow) && this.isURILike(aNode) )` → `lazy.PlacesUtils.nodeIsBookmark()`
- 条件付き依存: `if ( aNode && this.checkURLSecurity(aNode, aWindow) && this.isURILike(aNode) )` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (isBookmark)` → `this.markPageAsFollowedBookmark()`
- 条件付き依存: `if (!(isBookmark))` → `this.markPageAsTyped()`
- 条件付き依存: `if ( aNode && this.checkURLSecurity(aNode, aWindow) && this.isURILike(aNode) )` → `aNode.uri.startsWith()`
- 条件付き依存: `if ( aNode && this.checkURLSecurity(aNode, aWindow) && this.isURILike(aNode) )` → `aWindow.openTrustedLinkIn()`
- 条件付き依存: `if (aWindow.updateTelemetry)` → `aWindow.updateTelemetry()`
- 参照: `aNode.uri`, `aWindow.updateTelemetry`, `this.loadBookmarksInBackground`

## resolveOnContentBrowserCreated()
- 位置: L949-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.WebNavigationManager.setRecentTabTransitionData()`

## isURILike()
- 位置: L979-984
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNode instanceof Ci.nsINavHistoryResultNode)` → `lazy.PlacesUtils.nodeIsURI()`
- 参照: `Ci.nsINavHistoryResultNode`, `aNode.uri`
- XPCOM: [`nsINavHistoryResultNode`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## guessUrlSchemeForUI()
- 位置: L994-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `href.indexOf()`, `href.substr()`

## PUIU_getBestTitle()
- 位置: L998-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.nodeIsURI()`, `this.promptLocalization.formatValueSync()`
- 条件付き依存: `if (!aNode.title && lazy.PlacesUtils.nodeIsURI(aNode))` → `PlacesUIUtils.getBestTitleForUri()`
- 参照: `aNode.title`, `aNode.uri`

## getBestTitleForUri()
- 位置: L1020-1039
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `parsedURI.QueryInterface()`
- 参照: `Ci.nsIURL`, `Services.locale.ellipsis`, `parsedURI.QueryInterface(Ci.nsIURL).fileName`, `parsedURI.host`, `parsedURI.pathQueryRef`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md) / `Services.io` / `Services.locale`

## shouldShowTabsFromOtherComputersMenuitem()
- 位置: L1041-1046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Weave.Status.checkSetup()`, `lazy.Weave.Svc.PrefBranch.getCharPref()`
- 参照: `lazy.CLIENT_NOT_CONFIGURED`

## promiseNodeLikeFromFetchInfo()
- 位置: async L1061-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.freeze()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `aFetchInfo.guid`, `aFetchInfo.parentGuid`, `aFetchInfo.title`, `aFetchInfo.type`, `aFetchInfo.url`, `aFetchInfo.url.href`, `lazy.PlacesUtils.bookmarks.TYPE_SEPARATOR`
- XPCOM: [`nsINavHistoryResultNode`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## type()
- 位置: L1076-1090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^place:/.test()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `aFetchInfo.type`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `this.uri`, `this.uri.length`
- XPCOM: [`nsINavHistoryResultNode`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## parent()
- 位置: L1092-1094
- 役割: (未記入)
- 触るとき: (未記入)

## batchUpdatesForNode()
- 位置: async L1112-1128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `functionToWrap()`
- 条件付き依存: `if (!resultNode)` → `functionToWrap()`
- 条件付き依存: `if (itemsBeingChanged > ITEM_CHANGED_BATCH_NOTIFICATION_THRESHOLD)` → `resultNode.onBeginUpdateBatch()`
- 条件付き依存: `if (itemsBeingChanged > ITEM_CHANGED_BATCH_NOTIFICATION_THRESHOLD)` → `resultNode.onEndUpdateBatch()`

## handleTransferItems()
- 位置: async L1146-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getResultForBatching()`, `guidsToSelect.flat()`, `lazy.PlacesTransactions.batch()`, `this.batchUpdatesForNode()`
- 条件付き依存: `if (insertionPoint.isTag)` → `items.filter(item => "uri" in item).map()`
- 条件付き依存: `if (insertionPoint.isTag)` → `items.filter()`
- 条件付き依存: `if (insertionPoint.isTag)` → `lazy.PlacesTransactions.Tag()`
- 条件付き依存: `if (!(insertionPoint.isTag))` → `insertionPoint.getIndex()`
- 条件付き依存: `if (!(insertionPoint.isTag))` → `getTransactionsForTransferItems()`
- 参照: `insertionPoint.guid`, `insertionPoint.isTag`, `insertionPoint.tagName`, `item.uri`, `items.length`, `transactions.length`, `urls.length`

## onSidebarTreeClick()
- 位置: L1183-1234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.hasChildURIs()`, `tree.getCellAt()`, `tree.getCoordsForCellItem()`, `tree.view.isContainer()`, `tree.view.nodeForTreeIndex()`, `win.getComputedStyle()`
- 条件付き依存: `if (event.button == 0 && isContainer && !openInTabs)` → `tree.view.toggleOpenState()`
- 条件付き依存: `if ( !mouseInGutter && openInTabs && event.originalTarget.localName == "treechildren" )` → `tree.view.selection.select()`
- 条件付き依存: `if ( !mouseInGutter && openInTabs && event.originalTarget.localName == "treechildren" )` → `this.openMultipleLinksInTabs()`
- 条件付き依存: `if ( !mouseInGutter && !isContainer && event.originalTarget.localName == "treechildren" )` → `tree.view.selection.select()`
- 条件付き依存: `if ( !mouseInGutter && !isContainer && event.originalTarget.localName == "treechildren" )` → `this.openNodeWithEvent()`
- 参照: `AppConstants.platform`, `cell.childElt`, `cell.col`, `cell.row`, `event.button`, `event.clientX`, `event.clientY`, `event.ctrlKey`, `event.metaKey`, `event.originalTarget.localName`, `event.shiftKey`, `event.target.parentNode`, `rect.x`, `tree.documentGlobal`, `tree.selectedNode`, `win.getComputedStyle(tree).direction`

## onSidebarTreeKeyPress()
- 位置: L1236-1243
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.keyCode == event.DOM_VK_RETURN)` → `PlacesUIUtils.openNodeWithEvent()`
- 参照: `event.DOM_VK_RETURN`, `event.keyCode`, `event.target.selectedNode`

## onSidebarTreeMouseMove()
- 位置: L1252-1272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setMouseoverURL()`, `tree.getCellAt()`
- 条件付き依存: `if (cell.row != -1)` → `tree.view.nodeForTreeIndex()`
- 条件付き依存: `if (cell.row != -1)` → `lazy.PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsURI(node))` → `this.setMouseoverURL()`
- 参照: `cell.row`, `event.clientX`, `event.clientY`, `event.target`, `node.uri`, `tree.documentGlobal`, `treechildren.localName`, `treechildren.parentNode`

## setMouseoverURL()
- 位置: L1274-1281
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win.top.XULBrowserWindow)` → `win.top.XULBrowserWindow.setOverLink()`
- 参照: `win.top.XULBrowserWindow`

## maybeToggleBookmarkToolbarVisibility()
- 位置: async L1294-1331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `xulStore.hasValue()`
- 条件付き依存: `if ( aForceVisible || !xulStore.hasValue(BROWSER_DOCURL, "PersonalToolbar", "collapsed") )` → `xulStore.hasValue()`
- 条件付き依存: `if (aForceVisible || toolbarIsCustomized)` → `uncollapseToolbar()`
- 条件付き依存: `if ( aForceVisible || !xulStore.hasValue(BROWSER_DOCURL, "PersonalToolbar", "collapsed") )` → `lazy.PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if (numBookmarksOnToolbar > this.NUM_TOOLBAR_BOOKMARKS_TO_UNHIDE)` → `uncollapseToolbar()`
- 参照: `( await lazy.PlacesUtils.bookmarks.fetch( lazy.PlacesUtils.bookmarks.toolbarGuid ) ).childCount`, `AppConstants.BROWSER_CHROME_URL`, `Services.xulStore`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `this.NUM_TOOLBAR_BOOKMARKS_TO_UNHIDE`
- XPCOM: `Services.xulStore`

## uncollapseToolbar()
- 位置: L1302-1308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.obs.notifyObservers()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`
- XPCOM: `Services.obs`

## shouldHideOpenMenuItem()
- 位置: L1342-1372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `item.hasAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `item.documentGlobal`, `lazy.ContentSharingUtils.isEnabled`, `lazy.PrivateBrowsingUtils.enabled`
- XPCOM: `Services.prefs`

## managedPlacesContextShowing()
- 位置: async L1374-1424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(menupopup.children).forEach()`, `event.target.documentGlobal.updateCommands()`, `menupopup.triggerNode.hasAttribute()`, `menupopup.triggerNode.menupopup.hasAttribute()`
- 条件付き依存: `if ( menupopup.triggerNode.id == "managed-bookmarks" && !menupopup.triggerNode.menupopup.hasAttribute("hasbeenopened") )` → `window.PlacesToolbarHelper.populateManagedBookmarks()`
- 条件付き依存: `if (isFolder)` → `document.getElementById()`
- 条件付き依存: `if (isFolder)` → `Array.from(menuitems).some()`
- 条件付き依存: `if (isFolder)` → `Array.from()`
- 条件付き依存: `if (!(isFolder))` → `document.getElementById()`
- 条件付き依存: `if (!(isFolder))` → `this.shouldHideOpenMenuItem()`
- 参照: `child.hidden`, `document.getElementById(id).hidden`, `event.target`, `item.hidden`, `menuitem.link`, `menupopup.children`, `menupopup.documentGlobal`, `menupopup.ownerDocument`, `menupopup.triggerNode`, `menupopup.triggerNode.id`, `menupopup.triggerNode.menupopup`, `menupopup.triggerNode.menupopup.children`, `openContainerInTabs_menuitem.disabled`, `openContainerInTabs_menuitem.hidden`, `this.managedBookmarksController.triggerNode`

## placesContextShowing()
- 位置: L1426-1486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `[ "placesContext", "sidebar-history-context-menu", "sidebar-synced-tabs-context-menu", ].includes()`, `menupopup._view.buildContextMenu()`, `menupopup.triggerNode.closest()`, `this.getViewForNode()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.loadBookmarksInTabs", false))` → `menupopup.ownerDocument .getElementById("placesContext_open") .removeAttribute()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.loadBookmarksInTabs", false))` → `menupopup.ownerDocument .getElementById()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.loadBookmarksInTabs", false))` → `menupopup.ownerDocument .getElementById("placesContext_open:newtab") .setAttribute()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.tabs.loadBookmarksInTabs", false)))` → `menupopup.ownerDocument .getElementById("placesContext_open:newtab") .removeAttribute()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.tabs.loadBookmarksInTabs", false)))` → `menupopup.ownerDocument .getElementById()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.tabs.loadBookmarksInTabs", false)))` → `menupopup.ownerDocument .getElementById("placesContext_open") .setAttribute()`
- 条件付き依存: `if (isManaged)` → `this.managedPlacesContextShowing()`
- 条件付き依存: `if (!menupopup._view)` → `event.preventDefault()`
- 条件付き依存: `if (!this.openInTabClosesMenu)` → `menupopup.ownerDocument .getElementById("placesContext_open:newtab") .setAttribute()`
- 条件付き依存: `if (!this.openInTabClosesMenu)` → `menupopup.ownerDocument .getElementById()`
- 条件付き依存: `if (!menupopup._view.buildContextMenu(menupopup))` → `event.preventDefault()`
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`, `event.target`, `menupopup._view`, `menupopup.id`, `menupopup.triggerNode`, `menupopup.triggerNode.triggerNode`, `this.openInTabClosesMenu`
- XPCOM: `Services.prefs`

## placesContextHiding()
- 位置: L1488-1505
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (menupopup._view)` → `menupopup._view.destroyContextMenu()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`, `PlacesUIUtils.lastContextMenuTriggerNode`, `event.target`, `menupopup._view`, `menupopup.id`

## createContainerTabMenu()
- 位置: L1507-1513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.createUserContextMenu()`
- 参照: `event.target.documentGlobal`

## openInContainerTab()
- 位置: L1515-1541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `parseInt()`, `this._openNodeIn()`, `this.getViewForNode()`, `triggerNode?.closest()`
- 条件付き依存: `if (isManaged)` → `window.openTrustedLinkIn()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`, `this.lastContextMenuTriggerNode`, `triggerNode.documentGlobal`, `triggerNode.documentGlobal.top`, `triggerNode.link`, `view?.ownerWindow`, `view?.selectedNode`

## openSelectionInTabs()
- 位置: L1543-1555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.openSelectionInTabs()`, `event.target.parentNode.triggerNode.closest()`
- 条件付き依存: `if (!(isManaged))` → `PlacesUIUtils.getViewForNode()`
- 参照: `PlacesUIUtils.getViewForNode( PlacesUIUtils.lastContextMenuTriggerNode ).controller`, `PlacesUIUtils.lastContextMenuTriggerNode`, `this.managedBookmarksController`

## openSelectionInTabs()
- 位置: L1560-1573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.openTabset()`
- 条件付き依存: `if (menuitems[i].link)` → `items.push()`
- 参照: `event.target.documentGlobal`, `event.target.parentNode.triggerNode.menupopup.children`, `item.isBookmark`, `item.uri`, `menuitems.length`, `menuitems[i].link`

## isCommandEnabled()
- 位置: L1575-1585
- 役割: (未記入)
- 触るとき: (未記入)

## doCommand()
- 位置: L1587-1611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.copyLink()`, `window.openTrustedLinkIn()`
- 参照: `this.triggerNode.documentGlobal`, `this.triggerNode.label`, `this.triggerNode.link`

## maybeAddImportButton()
- 位置: async L1614-1645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `console.error()`, `db.execute()`, `lazy.PlacesUtils.withConnectionWrapper()`, `rows[0].getResultByName()`
- 条件付き依存: `if (numberOfBookmarks < 3)` → `lazy.CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (numberOfBookmarks < 3)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (numberOfBookmarks < 3)` → `this.removeImportButtonWhenImportSucceeds()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`, `lazy.PlacesUtils.bookmarks.toolbarGuid`
- XPCOM: `Services.policies` / `Services.prefs`

## removeImportButton()
- 位置: L1647-1650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `lazy.CustomizableUI.removeWidgetFromArea()`
- XPCOM: `Services.prefs`

## removeImportButtonWhenImportSucceeds()
- 位置: L1652-1673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (placement?.area != lazy.CustomizableUI.AREA_BOOKMARKS)` → `Services.prefs.clearUserPref()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`, `placement?.area`
- XPCOM: `Services.obs` / `Services.prefs`

## obs()
- 位置: L1661-1670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MigrationUtils.getImportedCount()`
- 条件付き依存: `if ( data == lazy.MigrationUtils.resourceTypes.BOOKMARKS && lazy.MigrationUtils.getImportedCount("bookmarks") > 0 )` → `this.removeImportButton()`
- 条件付き依存: `if ( data == lazy.MigrationUtils.resourceTypes.BOOKMARKS && lazy.MigrationUtils.getImportedCount("bookmarks") > 0 )` → `Services.obs.removeObserver()`
- 参照: `lazy.MigrationUtils.resourceTypes.BOOKMARKS`
- XPCOM: `Services.obs`

## setupSpeculativeConnection()
- 位置: L1684-1707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.io.speculativeConnect()`, `Services.prefs.getBoolPref()`, `url.startsWith()`
- 参照: `window.gBrowser.contentPrincipal`
- XPCOM: `Services.io` / `Services.prefs`

## maybeSpeculativeConnectOnMouseDown()
- 位置: L1715-1726
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.type == "mousedown" && event.target._placesNode?.uri && event.button != 2 )` → `PlacesUIUtils.setupSpeculativeConnection()`
- 参照: `event.button`, `event.target._placesNode.uri`, `event.target._placesNode?.uri`, `event.target.documentGlobal`, `event.type`

## getImageURL()
- 位置: L1738-1746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconLinkForIcon()`
- 参照: `lazy.PlacesUtils.favicons.defaultFavicon.spec`, `lazy.PlacesUtils.favicons.getFaviconLinkForIcon( Services.io.newURI(icon) ).spec`
- XPCOM: `Services.io`

## insertTitleStartDiffs()
- 位置: L1766-1815
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidate.title.slice()`, `longTitles.get()`
- 条件付き依存: `if (matches)` → `findStartDifference()`
- 条件付き依存: `if (matches)` → `matches.push()`
- 条件付き依存: `if (!(matches))` → `longTitles.set()`
- 参照: `candidate.title`, `candidate.title.length`, `candidate.titleDifferentIndex`, `match.title`, `match.titleDifferentIndex`, `this.similarTitlesMinChars`

## findStartDifference()
- 位置: L1767-1780
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PlacesUIUtils.similarTitlesMinChars`, `a.length`, `b.length`

## shareBookmarkFolder()
- 位置: L1820-1833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `console.error()`, `lazy.ContentSharingUtils.createShareableLinkFromBookmarkFolders()`, `lazy.PlacesUtils.getConcreteItemGuid()`, `lazy.PlacesUtils.nodeIsFolderOrShortcut()`, `view.selectedNodes .filter()`, `view.selectedNodes .filter(n => lazy.PlacesUtils.nodeIsFolderOrShortcut(n)) .map()`
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`

## canMoveUnwrappedNode()
- 位置: L1934-1949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.isRootItem()`
- 参照: `lazy.PlacesUtils.bookmarks.rootGuid`, `unwrappedNode.concreteGuid`, `unwrappedNode.guid`, `unwrappedNode.parentGuid`

## getResultForBatching()
- 位置: L1961-1978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Element.isInstance()`
- 条件付き依存: `if ( viewOrElement && Element.isInstance(viewOrElement) && viewOrElement.id === "placesList" )` → `viewOrElement.ownerDocument.getElementById()`
- 参照: `viewOrElement.id`, `viewOrElement.result`

## getTransactionsForTransferItems()
- 位置: L1992-2049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.SUPPORTED_FLAVORS.includes()`, `getTransactionsForCopy()`
- 条件付き依存: `if ( !("instanceId" in item) || item.instanceId != lazy.PlacesUtils.instanceId )` → `PlacesUIUtils.PLACES_FLAVORS.includes()`
- 条件付き依存: `if (PlacesUIUtils.PLACES_FLAVORS.includes(item.type))` → `console.error()`
- 条件付き依存: `if (doMove && canMove)` → `canMoveUnwrappedNode()`
- 条件付き依存: `if (doMove)` → `lazy.PlacesTransactions.Move()`
- 条件付き依存: `if (doMove)` → `items.map()`
- 参照: `item.instanceId`, `item.itemGuid`, `item.type`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `lazy.PlacesUtils.instanceId`

## getTransactionsForCopy()
- 位置: L2060-2110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.PLACES_FLAVORS.includes()`, `lazy.PlacesUtils.bookmarks.isVirtualRootItem()`, `lazy.PlacesUtils.isVirtualLeftPaneItem()`, `transactions.push()`
- 条件付き依存: `if ( PlacesUIUtils.PLACES_FLAVORS.includes(item.type) && // For anything that is comming from within this session, we do a // direct copy, otherwise we fallback ...)` → `lazy.PlacesTransactions.Copy()`
- 条件付き依存: `if (item.type == lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR)` → `lazy.PlacesTransactions.NewSeparator()`
- 条件付き依存: `if (!(item.type == lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR))` → `lazy.PlacesTransactions.NewBookmark()`
- 参照: `item.instanceId`, `item.itemGuid`, `item.title`, `item.type`, `item.uri`, `lazy.PlacesUtils.TYPE_PLAINTEXT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR`, `lazy.PlacesUtils.instanceId`

## getBrowserWindow()
- 位置: L2112-2120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.documentElement.getAttribute()`, `lazy.BrowserWindowTracker.getTopWindow()`
