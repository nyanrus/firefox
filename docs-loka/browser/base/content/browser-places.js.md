# browser/base/content/browser-places.js

source: browser/base/content/browser-places.js
source-hash: 20220bd0969b96d2ec8c297fb349ca1935338364
lines: 2407

## <module>
- 役割: (未記入)
- 呼び出し先: `BookmarkingUI.maybeShowOtherBookmarksFolder()`, `BookmarkingUI.maybeShowOtherBookmarksFolder().then()`, `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `document .getElementById()`, `document .getElementById("PlacesToolbar") ?._placesView?.updateNodesVisibility()`

## _element()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## panel()
- 位置: L62-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.addEventListener()`, `this._createPanelIfNeeded()`, `this._element()`
- 参照: `element.hidden`, `this.panel`

## handleEvent()
- 位置: L82-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.classList.contains()`, `clearTimeout()`, `document.getElementById()`, `eventMatchesKey()`, `this.panel.hidePopup()`
- 条件付き依存: `if (aEvent.originalTarget == this.panel)` → `this._handlePopupHiddenEvent().catch()`
- 条件付き依存: `if (aEvent.originalTarget == this.panel)` → `this._handlePopupHiddenEvent()`
- 条件付き依存: `if (eventMatchesKey(aEvent, accessKey))` → `this.panel.hidePopup()`
- 条件付き依存: `if (this._isNewBookmark && !this._isComposing)` → `clearTimeout()`
- 条件付き依存: `if (this._isNewBookmark && !this._isComposing)` → `setTimeout()`
- 条件付き依存: `if (this._isNewBookmark && !this._isComposing)` → `this.panel.matches()`
- 条件付き依存: `if (!this.panel.matches(":hover"))` → `this.panel.hidePopup()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_RETURN`, `aEvent.currentTarget`, `aEvent.defaultPrevented`, `aEvent.keyCode`, `aEvent.originalTarget`, `aEvent.target`, `aEvent.target.id`, `aEvent.type`, `console.error`, `this._autoCloseTimeout`, `this._autoCloseTimer`, `this._autoCloseTimerEnabled`, `this._cancelOnPopupHidden`, `this._closePanelQuickForTesting`, `this._isComposing`, `this._isNewBookmark`, `this._removeBookmarksOnPopupHidden`, `this.panel`

## _handlePopupHiddenEvent()
- 位置: async L189-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `bookmarkState.save()`, `gEditItemOverlay.uninitPanel()`, `this._element()`, `this._storeRecentlyUsedFolder()`
- 条件付き依存: `if (!this._isNewBookmark)` → `PlacesTransactions.Remove(guidsForRemoval).transact()`
- 条件付き依存: `if (!this._isNewBookmark)` → `PlacesTransactions.Remove()`
- 条件付き依存: `if (!(!this._isNewBookmark))` → `BookmarkingUI.star.removeAttribute()`
- 条件付き依存: `if (this._isNewBookmark)` → `this.showConfirmation()`
- 参照: `this._cancelOnPopupHidden`, `this._element("editBookmarkPanel_showForNewBookmarks").checked`, `this._isNewBookmark`, `this._itemGuids`, `this._removeBookmarksOnPopupHidden`
- XPCOM: `Services.prefs`

## showEditBookmarkPopup()
- 位置: async L229-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.bookmarks.fetch()`, `document.l10n.setAttributes()`, `gEditItemOverlay.initPanel()`, `this._element()`, `this._itemGuids.push()`, `this.panel.openPopup()`
- 条件付き依存: `if (this._isNewBookmark)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._isNewBookmark))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (this.userHasTags === undefined)` → `PlacesUtils.bookmarks.fetchTags()`
- 条件付き依存: `if (!this.userHasTags)` → `hiddenRows.push()`
- 参照: `BookmarkingUI.anchor`, `bookmark.guid`, `fetchedTags.length`, `this._element("editBookmarkPanel_showForNewBookmarks").checked`, `this._isNewBookmark`, `this._itemGuids`, `this._itemGuids.length`, `this.panel.state`, `this.showForNewBookmarks`, `this.userHasTags`

## onPanelReady()
- 位置: L266-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fn()`, `target.addEventListener()`
- 参照: `target.parentNode`, `this.panel`

## _createPanelIfNeeded()
- 位置: L307-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._element()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `this._element()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `template.content.cloneNode()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `template.replaceWith()`

## SU_removeBookmarkButtonCommand()
- 位置: L317-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.hidePopup()`
- 参照: `this._removeBookmarksOnPopupHidden`

## _storeRecentlyUsedFolder()
- 位置: async L322-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.bookmarks.userContentRoots.includes()`, `PlacesUtils.metadata.get()`, `PlacesUtils.metadata.set()`, `lastUsedFolderGuids.indexOf()`, `lastUsedFolderGuids.pop()`
- 条件付き依存: `if ( didChangeFolder && selectedFolderGuid !== PlacesUtils.bookmarks.mobileGuid )` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (index > 1)` → `lastUsedFolderGuids.splice()`
- 条件付き依存: `if (index > 1)` → `lastUsedFolderGuids.unshift()`
- 条件付き依存: `if (index == -1)` → `lastUsedFolderGuids.unshift()`
- 参照: `PlacesUIUtils.LAST_USED_FOLDERS_META_KEY`, `PlacesUIUtils.maxRecentFolders`, `PlacesUtils.bookmarks.mobileGuid`, `lastUsedFolderGuids.length`
- XPCOM: `Services.prefs`

## showConfirmation()
- 位置: L368-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ConfirmationHint.show()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- 条件付き依存: `if (window.toolbar.visible)` → `document.getElementById()`
- 条件付き依存: `if (window.toolbar.visible)` → `element.getAttribute()`
- 条件付き依存: `if (!anchor)` → `document.getElementById()`
- 参照: `window.toolbar.visible`
- XPCOM: `Services.prefs`

## bookmarkPage()
- 位置: async L410-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.promiseNodeLikeFromFetchInfo()`, `PlacesUtils.bookmarks.fetch()`, `Services.io.createExposableURI()`, `StarUI.showEditBookmarkPopup()`, `URL.fromURI()`, `gURLBar.handleRevert()`
- 条件付き依存: `if (browser.documentURI)` → `/^about:(neterror|certerror|blocked)/.test()`
- 条件付き依存: `if (isErrorPage)` → `PlacesUtils.history.fetch()`
- 条件付き依存: `if (isNewBookmark)` → `console.error()`
- 条件付き依存: `if (!StarUI.showForNewBookmarks)` → `PlacesTransactions.NewBookmark(info).transact()`
- 条件付き依存: `if (!StarUI.showForNewBookmarks)` → `PlacesTransactions.NewBookmark()`
- 条件付き依存: `if (!(!StarUI.showForNewBookmarks))` → `BookmarkingUI.star.setAttribute()`
- 条件付き依存: `if (charset)` → `PlacesUIUtils.setCharsetForPage(url, charset, window).catch()`
- 条件付き依存: `if (charset)` → `PlacesUIUtils.setCharsetForPage()`
- 条件付き依存: `if (!showEditUI)` → `StarUI.showConfirmation()`
- 参照: `PlacesUIUtils.defaultParentGuid`, `PlacesUtils.bookmarks.unsavedGuid`, `StarUI.showForNewBookmarks`, `browser.characterSet`, `browser.contentTitle`, `browser.currentURI`, `browser.documentURI`, `browser.documentURI.spec`, `console.error`, `entry.title`, `gBrowser.selectedBrowser`, `info.guid`, `info.title`, `url.href`
- XPCOM: `Services.io`

## bookmarkLink()
- 位置: async L484-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.showBookmarkDialog()`, `PlacesUtils.bookmarks.fetch()`, `Services.io.newURI()`
- 条件付き依存: `if (bm)` → `PlacesUIUtils.promiseNodeLikeFromFetchInfo()`
- 条件付き依存: `if (bm)` → `PlacesUIUtils.showBookmarkDialog()`
- 参照: `PlacesUIUtils.defaultParentGuid`, `window.top`
- XPCOM: `Services.io`

## bookmarkTabs()
- 位置: async L520-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `PlacesCommandHook.getUniquePages()`, `PlacesCommandHook.getUniquePages(tabs).map()`, `PlacesUIUtils.showBookmarkPagesDialog()`, `Services.io.createExposableURI()`, `gBrowser.visibleTabs.filter()`
- 参照: `page.uri`, `tab.pinned`
- XPCOM: `Services.io`

## getUniquePages()
- 位置: L534-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.forEach()`
- 条件付き依存: `if (!(spec in uniquePages))` → `URIs.push()`
- 参照: `browser.contentTitle`, `browser.currentURI`, `tab.label`, `tab.linkedBrowser`, `uri.spec`

## showPlacesOrganizer()
- 位置: L559-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (!organizer || organizer.closed)` → `openDialog()`
- 条件付き依存: `if (!(!organizer || organizer.closed))` → `organizer.PlacesOrganizer.selectLeftPaneContainerByHierarchy()`
- 条件付き依存: `if (!(!organizer || organizer.closed))` → `organizer.focus()`
- 参照: `organizer.closed`
- XPCOM: `Services.wm`

## searchBookmarks()
- 位置: async L576-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `BrowserWindowTracker.promiseOpenWindow()`, `win.gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.BOOKMARK`

## searchTabs()
- 位置: async L585-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `BrowserWindowTracker.promiseOpenWindow()`, `win.focus()`, `win.gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`

## searchHistory()
- 位置: async L595-602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `BrowserWindowTracker.promiseOpenWindow()`, `win.gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.HISTORY`

## HistoryMenu.constructor()
- 位置: L607-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## HistoryMenu._init()
- 位置: L614-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `super._init()`

## HistoryMenu.toggleHiddenTabs()
- 位置: L628-632
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.tabs.length`, `gBrowser.visibleTabs.length`, `this.hiddenTabsMenu.hidden`, `window.gBrowser`

## HistoryMenu.toggleRecentlyClosedTabs()
- 位置: L634-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getClosedTabCount()`
- 条件付き依存: `if (SessionStore.getClosedTabCount() == 0)` → `this.undoTabMenu.setAttribute()`
- 条件付き依存: `if (!(SessionStore.getClosedTabCount() == 0))` → `this.undoTabMenu.removeAttribute()`

## HistoryMenu.populateUndoSubmenu()
- 位置: L647-670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RecentlyClosedTabsAndWindowsMenuUtils.getTabsFragment()`, `SessionStore.getClosedTabCount()`, `this.undoTabMenu.removeAttribute()`, `undoPopup.appendChild()`, `undoPopup.firstChild.remove()`, `undoPopup.hasChildNodes()`
- 条件付き依存: `if (SessionStore.getClosedTabCount() == 0)` → `this.undoTabMenu.setAttribute()`
- 参照: `this.undoTabMenu.menupopup`

## HistoryMenu.toggleRecentlyClosedWindows()
- 位置: L672-680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.getClosedWindowCount()`
- 条件付き依存: `if (SessionStore.getClosedWindowCount() == 0)` → `this.undoWindowMenu.setAttribute()`
- 条件付き依存: `if (!(SessionStore.getClosedWindowCount() == 0))` → `this.undoWindowMenu.removeAttribute()`

## HistoryMenu.populateUndoWindowSubmenu()
- 位置: L685-710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RecentlyClosedTabsAndWindowsMenuUtils.getWindowsFragment()`, `SessionStore.getClosedWindowCount()`, `this.undoWindowMenu.removeAttribute()`, `undoPopup.appendChild()`, `undoPopup.firstChild.remove()`, `undoPopup.hasChildNodes()`
- 条件付き依存: `if (SessionStore.getClosedWindowCount() == 0)` → `this.undoWindowMenu.setAttribute()`
- 参照: `this.undoWindowMenu.menupopup`

## HistoryMenu.toggleTabsFromOtherComputers()
- 位置: L712-740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.shouldShowTabsFromOtherComputersMenuitem()`
- 条件付き依存: `if (this.remoteTabsPromo)` → `gSync.getSyncPromoState()`
- 参照: `this.remoteTabsPromo`, `this.remoteTabsPromo.dataset.action`, `this.remoteTabsPromo.hidden`, `this.syncTabsMenuitem`, `this.syncTabsMenuitem.hidden`

## HistoryMenu._onPopupShowing()
- 位置: L742-754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super._onPopupShowing()`, `this.toggleHiddenTabs()`, `this.toggleRecentlyClosedTabs()`, `this.toggleRecentlyClosedWindows()`, `this.toggleTabsFromOtherComputers()`
- 参照: `aEvent.target`, `this.rootElement`

## HistoryMenu._onCommand()
- 位置: L756-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getRootEvent()`
- 条件付き依存: `if (placesNode)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `PlacesUIUtils.markPageAsTyped()`
- 条件付き依存: `if (placesNode)` → `openUILink()`
- 条件付き依存: `if (placesNode)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `aEvent.target._placesNode`, `placesNode.uri`
- XPCOM: `Services.scriptSecurityManager`

## onMouseUp()
- 位置: L789-815
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (modifKey || aEvent.button == 1)` → `target.setAttribute()`
- 条件付き依存: `if (modifKey || aEvent.button == 1)` → `menupopup.addEventListener()`
- 条件付き依存: `if (modifKey || aEvent.button == 1)` → `target.removeAttribute()`
- 条件付き依存: `if (!(modifKey || aEvent.button == 1))` → `target.removeAttribute()`
- 参照: `AppConstants.platform`, `PlacesUIUtils.openInTabClosesMenu`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.originalTarget`, `target.parentNode`, `target.tagName`

## BEH_onClick()
- 位置: L817-859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if ( PlacesUIUtils.openInTabClosesMenu && (tag == "menuitem" || tag == "menu") )` → `closeMenus()`
- 条件付き依存: `if (target.localName == "menu" || target.localName == "toolbarbutton")` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 条件付き依存: `if (aEvent.button == 1 && !(tag == "menuitem" || tag == "menu"))` → `this.onCommand()`
- 条件付き依存: `if (aEvent.button == 1 && !(tag == "menuitem" || tag == "menu"))` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.button == 1 && !(tag == "menuitem" || tag == "menu"))` → `aEvent.stopPropagation()`
- 参照: `AppConstants.platform`, `PlacesUIUtils.openInTabClosesMenu`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.originalTarget`, `aEvent.shiftKey`, `aEvent.target`, `target._placesNode`, `target.localName`, `target.tagName`

## BEH_onCommand()
- 位置: L869-889
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target._placesNode)` → `PlacesUIUtils.openNodeWithEvent()`
- 条件付き依存: `if (target._placesNode)` → `target.closest()`
- 条件付き依存: `if (target.closest("#PersonalToolbar"))` → `Glean.browserEngagement.bookmarksToolbarBookmarkOpened.add()`
- 条件付き依存: `if (target.closest("#PersonalToolbar"))` → `AIWindow.isAIWindowActive()`
- 条件付き依存: `if (target.closest("#PersonalToolbar"))` → `AIWindow.isAIWindowNewTabPage()`
- 条件付き依存: `if ( gBookmarksToolbarVisibility == "newtab" && AIWindow.isAIWindowActive(window) && AIWindow.isAIWindowNewTabPage(gBrowser.currentURI) )` → `Glean.smartWindow.bookmarkbar.opened.add()`
- 条件付き依存: `if (eventAction)` → `gSync.handleSyncPromoAction()`
- 参照: `aEvent.originalTarget`, `gBrowser.currentURI`, `target._placesNode`, `target.dataset.action`

## BEH_fillInBHTooltip()
- 位置: L891-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.nodeIsURI()`, `aEvent.target.querySelector()`
- 条件付き依存: `if (aTooltip.triggerNode.localName == "treechildren")` → `tree.getCellAt()`
- 条件付き依存: `if (cell.row == -1)` → `aEvent.preventDefault()`
- 条件付き依存: `if (aTooltip.triggerNode.localName == "treechildren")` → `tree.view.nodeForTreeIndex()`
- 条件付き依存: `if (aTooltip.triggerNode.localName == "treechildren")` → `tree.isCellCropped()`
- 条件付き依存: `if (!(tooltipNode._placesNode))` → `tooltipNode.getAttribute()`
- 条件付き依存: `if (!(aTooltip.triggerNode.localName == "treechildren"))` → `isLabelCropped()`
- 条件付き依存: `if (!(aTooltip.triggerNode.localName == "treechildren"))` → `tooltipNode.querySelector()`
- 条件付き依存: `if (!node && !targetURI)` → `aEvent.preventDefault()`
- 条件付き依存: `if (!cropped && !url)` → `aEvent.preventDefault()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aTooltip.triggerNode`, `aTooltip.triggerNode.localName`, `aTooltip.triggerNode.parentNode`, `cell.col`, `cell.row`, `node.title`, `node.uri`, `tooltipNode._placesNode`, `tooltipNode.label`, `tooltipNode.localName`, `tooltipTitle.hidden`, `tooltipTitle.textContent`, `tooltipUrl.hidden`, `tooltipUrl.value`

## isLabelCropped()
- 位置: L920-921
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `label.clientWidth`, `label.scrollWidth`

## PMDH_onDragEnter()
- 位置: L987-1023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `event.preventDefault()`, `event.stopPropagation()`, `popup.openPopup()`, `popup.setAttribute()`, `this._isStaticContainer()`, `this._loadTimer.initWithCallback()`
- 条件付き依存: `if (this._closeTimer && this._closingTimerNode === event.currentTarget)` → `this._closeTimer.cancel()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `PlacesControllerDragHelper.currentDropTarget`, `event.currentTarget`, `event.target`, `event.target.menupopup`, `popup.state`, `this._closeTimer`, `this._closingTimerNode`, `this._loadTimer`, `this._springLoadDelayMs`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PMDH_onDragLeave()
- 位置: L1028-1070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `popup.hasAttribute()`, `this._closeTimer.initWithCallback()`, `this._isStaticContainer()`
- 条件付き依存: `if (this._loadTimer)` → `this._loadTimer.cancel()`
- 条件付き依存: `if (!inHierarchy && popup && popup.hasAttribute("autoopened"))` → `popup.removeAttribute()`
- 条件付き依存: `if (!inHierarchy && popup && popup.hasAttribute("autoopened"))` → `popup.hidePopup()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `PlacesControllerDragHelper.currentDropTarget`, `event.currentTarget`, `event.relatedTarget`, `event.relatedTarget.parentNode`, `event.target`, `event.target.menupopup`, `node.parentNode`, `this._closeDelayMs`, `this._closeTimer`, `this._closingTimerNode`, `this._loadTimer`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PMDH__isContainer()
- 位置: L1078-1089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.getAttribute()`, `node.menupopup.hasAttribute()`, `node.parentNode.hasAttribute()`
- 参照: `node.localName`, `node.menupopup`

## PMDH_onDragOver()
- 位置: L1097-1107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `event.stopPropagation()`
- 条件付き依存: `if (ip && PlacesControllerDragHelper.canDrop(ip, event.dataTransfer))` → `event.preventDefault()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `PlacesUtils.bookmarks.menuGuid`, `event.dataTransfer`, `event.target`

## PMDH_onDrop()
- 位置: L1115-1123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesControllerDragHelper.onDrop()`, `event.stopPropagation()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `PlacesUtils.bookmarks.menuGuid`, `event.dataTransfer`

## _viewElt()
- 位置: L1131-1133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## init()
- 位置: async L1139-1142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._realInit()`
- 参照: `PlacesUIUtils.canLoadToolbarContentPromise`

## _realInit()
- 位置: L1147-1193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `document.getElementById()`, `getComputedStyle()`, `this._getParentToolbar()`
- 条件付き依存: `if (!this._isObservingToolbars)` → `window.addEventListener()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.updateEmptyToolbarMessage() .finally(() => { toolbar.toggleAttribute("initialized", true); }) .catch()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.updateEmptyToolbarMessage() .finally()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.updateEmptyToolbarMessage()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `toolbar.toggleAttribute()`
- 参照: `PlacesUtils.bookmarks.toolbarGuid`, `console.error`, `getComputedStyle(toolbar, "").display`, `this._isCustomizing`, `this._isObservingToolbars`, `this._viewElt`, `toolbar.collapsed`, `toolbar.id`, `viewElt._placesView`, `window.closed`

## getIsEmpty()
- 位置: async L1195-1201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("PlacesToolbarItems").hasChildNodes()`, `this._viewElt._placesView.promiseRebuilt()`
- 参照: `this._viewElt._placesView`

## handleEvent()
- 位置: L1203-1211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getParentToolbar()`
- 条件付き依存: `if (event.target == this._getParentToolbar(this._viewElt))` → `this._resetView()`
- 参照: `event.target`, `event.type`, `this._viewElt`

## PTH_uninit()
- 位置: L1216-1222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`
- 条件付き依存: `if (this._isObservingToolbars)` → `window.removeEventListener()`
- 参照: `this._isObservingToolbars`

## PTH_customizeStart()
- 位置: L1224-1233
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (viewElt && viewElt._placesView)` → `viewElt._placesView.uninit()`
- 参照: `this._isCustomizing`, `this._viewElt`, `viewElt._placesView`

## PTH_customizeDone()
- 位置: L1235-1238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 参照: `this._isCustomizing`

## onPlaceholderCommand()
- 位置: L1240-1249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `widgetGroup.forWindow()`
- 条件付き依存: `if ( widget.overflowed || widgetGroup.areaType == CustomizableUI.TYPE_PANEL )` → `PlacesCommandHook.showPlacesOrganizer()`
- 参照: `CustomizableUI.TYPE_PANEL`, `widget.overflowed`, `widgetGroup.areaType`

## _getParentToolbar()
- 位置: L1251-1259
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `element.localName`, `element.parentNode`

## onWidgetUnderflow()
- 位置: L1261-1268
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNode.id == "personal-bookmarks" && win == window)` → `this._resetView()`
- 参照: `aNode.documentGlobal`, `aNode.id`

## onWidgetAdded()
- 位置: L1270-1279
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId == "personal-bookmarks" && !this._isCustomizing)` → `this._resetView()`
- 参照: `this._isCustomizing`

## _resetView()
- 位置: L1281-1292
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._viewElt._placesView)` → `this._viewElt._placesView.uninit()`
- 条件付き依存: `if (this._viewElt)` → `this.init()`
- 参照: `this._viewElt`, `this._viewElt._placesView`

## populateManagedBookmarks()
- 位置: async L1294-1311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`, `XULBrowserWindow.setOverLink()`, `document.createDocumentFragment()`, `popup.addEventListener()`, `popup.appendChild()`, `popup.hasChildNodes()`, `this.addManagedBookmarks()`
- 参照: `Services.policies.getActivePolicies().ManagedBookmarks`, `event.target.link`
- XPCOM: `Services.policies`

## addManagedBookmarks()
- 位置: async L1316-1384
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (entry.children)` → `document.createXULElement()`
- 条件付き依存: `if (entry.name)` → `submenu.setAttribute()`
- 条件付き依存: `if (!(entry.name))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (entry.children)` → `submenu.setAttribute()`
- 条件付き依存: `if (entry.children)` → `submenu.classList.add()`
- 条件付き依存: `if (entry.children)` → `submenu.appendChild()`
- 条件付き依存: `if (entry.children)` → `menu.appendChild()`
- 条件付き依存: `if (entry.children)` → `this.addManagedBookmarks()`
- 条件付き依存: `if (entry.name && entry.url)` → `URL.parse()`
- 条件付き依存: `if (!parsed)` → `URL.parse()`
- 条件付き依存: `if (!parsed)` → `console.error()`
- 条件付き依存: `if (entry.favicon)` → `URL.parse()`
- 条件付き依存: `if (entry.favicon)` → `this.MANAGED_BOOKMARK_FAVICON_SCHEMES.includes()`
- 条件付き依存: `if ( iconURL && this.MANAGED_BOOKMARK_FAVICON_SCHEMES.includes(iconURL.protocol) )` → `FaviconUtils.getMozRemoteImageURL()`
- 条件付き依存: `if (!( iconURL && this.MANAGED_BOOKMARK_FAVICON_SCHEMES.includes(iconURL.protocol) ))` → `console.error()`
- 条件付き依存: `if (!( iconURL && this.MANAGED_BOOKMARK_FAVICON_SCHEMES.includes(iconURL.protocol) ))` → `this.MANAGED_BOOKMARK_FAVICON_SCHEMES.join()`
- 条件付き依存: `if (parsed.protocol != "javascript:")` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (entry.name && entry.url)` → `document.createXULElement()`
- 条件付き依存: `if (entry.name && entry.url)` → `menuitem.setAttribute()`
- 条件付き依存: `if (imageURL)` → `menuitem.setAttribute()`
- 条件付き依存: `if (entry.name && entry.url)` → `menuitem.classList.add()`
- 条件付き依存: `if (entry.name && entry.url)` → `menu.appendChild()`
- 参照: `children.length`, `entry.children`, `entry.favicon`, `entry.name`, `entry.url`, `iconURL.protocol`, `menuitem.link`, `parsed.protocol`, `parsed?.href`

## openManagedBookmark()
- 位置: L1386-1399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^javascript:/i.test()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `openUILink()`
- 条件付き依存: `if (/^javascript:/i.test(link))` → `openTrustedLinkIn()`
- 参照: `event.target.link`
- XPCOM: `Services.scriptSecurityManager`

## onDragStartManaged()
- 位置: L1401-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addData()`
- 参照: `PlacesUtils.TYPE_HTML`, `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_URL`, `event.dataTransfer`, `event.target.label`, `event.target.link`, `node.title`, `node.type`, `node.uri`

## addData()
- 位置: L1413-1416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.wrapNode()`, `dt.mozSetDataAt()`

## button()
- 位置: L1433-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `widgetGroup.forWindow()`
- 参照: `this.BOOKMARK_BUTTON_ID`, `this.button`, `widgetGroup.forWindow(window).node`

## star()
- 位置: L1439-1442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.STAR_ID`, `this.star`

## starBox()
- 位置: L1444-1447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.STAR_BOX_ID`, `this.starBox`

## anchor()
- 位置: L1449-1452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserPageActions.panelAnchorNodeForAction()`, `PageActions.actionForID()`
- 参照: `PageActions.ACTION_ID_BOOKMARK`

## stringbundleset()
- 位置: L1454-1457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.stringbundleset`

## toolbar()
- 位置: L1459-1462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.toolbar`

## status()
- 位置: L1467-1474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.star.hasAttribute()`
- 参照: `this.STATUS_STARRED`, `this.STATUS_UNSTARRED`, `this.STATUS_UPDATING`, `this._pendingUpdate`

## BUI_onPopupShowing()
- 位置: L1476-1517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(this.BOOKMARK_BUTTON_ID).forWindow()`, `document.getElementById()`, `this.button.getAttribute()`, `this.button.hasAttribute()`, `this.updateLabel()`
- 条件付き依存: `if ( this.button.getAttribute("cui-areatype") == CustomizableUI.TYPE_PANEL || this.button.hasAttribute("overflowedItem") )` → `this._showSubView()`
- 条件付き依存: `if ( this.button.getAttribute("cui-areatype") == CustomizableUI.TYPE_PANEL || this.button.hasAttribute("overflowedItem") )` → `event.preventDefault()`
- 条件付き依存: `if ( this.button.getAttribute("cui-areatype") == CustomizableUI.TYPE_PANEL || this.button.hasAttribute("overflowedItem") )` → `event.stopPropagation()`
- 条件付き依存: `if (widget.overflowed)` → `event.preventDefault()`
- 条件付き依存: `if (widget.overflowed)` → `widget.node.removeAttribute()`
- 条件付き依存: `if (widget.overflowed)` → `PlacesCommandHook.showPlacesOrganizer()`
- 参照: `CustomizableUI.TYPE_PANEL`, `SidebarController.currentID`, `document.getElementById("BMB_mobileBookmarks").hidden`, `event.target.id`, `this.BOOKMARK_BUTTON_ID`, `this.toolbar.collapsed`, `widget.overflowed`

## updateLabel()
- 位置: L1519-1523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.l10n.setAttributes()`, `element.getAttribute()`

## toggleBookmarksToolbar()
- 位置: L1525-1539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.recordToolbarVisibility()`, `CustomizableUI.setToolbarVisibility()`, `Services.prefs.setCharPref()`
- 参照: `this.toolbar.collapsed`, `this.toolbar.id`
- XPCOM: `Services.prefs`

## isOnNewTabPage()
- 位置: L1541-1574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.isAIWindowNewTabPage()`, `Cu.isESModuleLoaded()`, `PrivateBrowsingUtils.isWindowPrivate()`, `newTabURLs.some()`, `this._newTabURI()`, `this._newTabURI(newTabUriString)?.equalsExceptRef()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `newTabURLs.push()`
- 参照: `AboutNewTab.newTabURL`

## _newTabURI()
- 位置: L1576-1583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._newTabURICache.get()`
- 条件付き依存: `if (uri === undefined)` → `Services.io.newURI()`
- 条件付き依存: `if (uri === undefined)` → `this._newTabURICache.set()`
- XPCOM: `Services.io`

## buildBookmarksToolbarSubmenu()
- 位置: L1586-1651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `menu.appendChild()`, `menu.setAttribute()`, `menuItem.addEventListener()`, `menuItem.setAttribute()`, `menuItem.toggleAttribute()`, `menuItemForNextStateFromKbShortcut.setAttribute()`, `menuItems.map()`, `menuPopup.append()`, `toolbar.getAttribute()`
- 参照: `menuItem.dataset.bookmarksToolbarVisibility`, `menuItem.dataset.visibilityEnum`, `toolbar.id`

## updateEmptyToolbarMessage()
- 位置: async L1659-1710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `document.getElementById()`, `this.toolbar.hasAttribute()`, `this.toolbar.querySelector()`
- 条件付き依存: `if (checkHasBookmarks)` → `PlacesToolbarHelper.getIsEmpty()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `bookmarksToolbarItemsPlacement?.area`, `emptyMsg.hidden`, `this._isCustomizing`

## BUI__uninitView()
- 位置: L1712-1738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (this.button._placesView)` → `this.button._placesView.uninit()`
- 条件付き依存: `if (menubar && menubar._placesView)` → `menubar._placesView.uninit()`
- 条件付き依存: `if (elem && elem._placesView)` → `elem._placesView.uninit()`
- 参照: `elem._placesView`, `menubar._placesView`, `this.button._placesView`

## BUI_customizeStart()
- 位置: L1740-1758
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWindow == window)` → `this._uninitView()`
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage()`
- 条件付き依存: `if (aWindow == window)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (aWindow == window)` → `setToolbarVisibility()`
- 参照: `console.error`, `this._isCustomizing`, `this.toolbar`
- XPCOM: `Services.prefs`

## BUI_widgetAdded()
- 位置: L1760-1767
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId == this.BOOKMARK_BUTTON_ID)` → `this._onWidgetWasMoved()`
- 条件付き依存: `if (aArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `console.error`, `this.BOOKMARK_BUTTON_ID`

## BUI_widgetRemoved()
- 位置: L1769-1776
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId == this.BOOKMARK_BUTTON_ID)` → `this._onWidgetWasMoved()`
- 条件付き依存: `if (aOldArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aOldArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `console.error`, `this.BOOKMARK_BUTTON_ID`

## BUI_widgetReset()
- 位置: L1778-1782
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNode == this.button)` → `this._onWidgetWasMoved()`
- 参照: `this.button`

## BUI_undoWidgetUndoMove()
- 位置: L1784-1788
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNode == this.button)` → `this._onWidgetWasMoved()`
- 参照: `this.button`

## BUI_onWidgetBeforeDOMChange()
- 位置: L1790-1799
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNode.id == "import-button")` → `this._updateImportButton()`
- 参照: `aNode.id`

## BUI_updateImportButton()
- 位置: L1801-1807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.classList.toggle()`
- 参照: `this.toolbar`

## BUI_widgetWasMoved()
- 位置: L1809-1815
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._isCustomizing)` → `this._uninitView()`
- 参照: `this._isCustomizing`

## BUI_customizeEnd()
- 位置: L1817-1822
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage()`
- 参照: `console.error`, `this._isCustomizing`

## init()
- 位置: L1824-1831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `document.getElementById()`, `this.updateEmptyToolbarMessage()`, `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (importButton)` → `this._updateImportButton()`
- 参照: `console.error`, `importButton.parentNode`

## BUI_uninit()
- 位置: L1835-1856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `this._uninitView()`, `this.updateBookmarkPageMenuItem()`
- 条件付き依存: `if (this._hasBookmarksObserver)` → `PlacesUtils.observers.removeListener()`
- 参照: `this._hasBookmarksObserver`, `this._pendingUpdate`, `this.handlePlacesEvents`

## BUI_onLocationChange()
- 位置: L1858-1863
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.currentURI.equals()`, `this.updateStarState()`
- 参照: `this._uri`

## BUI_updateStarState()
- 位置: L1865-1917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.bookmarks .fetch()`, `PlacesUtils.bookmarks .fetch({ url: this._uri }, b => guids.add(b.guid), { concurrent: true }) .catch()`, `guids.add()`, `this._itemGuids.clear()`, `this._updateStar()`
- 条件付き依存: `if (!this._hasBookmarksObserver)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._hasBookmarksObserver)` → `PlacesUtils.observers.addListener()`
- 条件付き依存: `if (!this._hasBookmarksObserver)` → `console.error()`
- 参照: `b.guid`, `console.error`, `gBrowser.currentURI`, `this._hasBookmarksObserver`, `this._itemGuids`, `this._itemGuids.size`, `this._pendingUpdate`, `this._uri`, `this.handlePlacesEvents`

## BUI__updateStar()
- 位置: L1919-1963
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `Services.obs.notifyObservers()`, `ShortcutUtils.prettifyShortcut()`, `document.getElementById()`, `document.l10n.setAttributes()`, `element.toggleAttribute()`, `this.updateBookmarkPageMenuItem()`
- 条件付き依存: `if (!this.starBox)` → `this.updateBookmarkPageMenuItem()`
- 参照: `this.BOOKMARK_BUTTON_SHORTCUT`, `this._itemGuids.size`, `this.star`, `this.starBox`
- XPCOM: `Services.obs`

## updateBookmarkPageMenuItem()
- 位置: L1972-2050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.getElementById()`
- 条件付き依存: `if (menuItem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (panelMenuToolbarButton)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `document.getElementById()`
- 条件付き依存: `if (shortcutElem)` → `ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (shortcutElem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(shortcutElem))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (document.getElementById("page-action-buttons"))` → `document.l10n.formatMessages([{ id: menuItemL10nId }]).then()`
- 条件付き依存: `if (document.getElementById("page-action-buttons"))` → `document.l10n.formatMessages()`
- 条件付き依存: `if (document.getElementById("page-action-buttons"))` → `BrowserPageActions.panelButtonNodeForActionID()`
- 条件付き依存: `if (panelButton)` → `panelButton.setAttribute()`
- 参照: `AppConstants.platform`, `PageActions.ACTION_ID_BOOKMARK`, `l10n[0].attributes`, `l10n[0].attributes[0].value`, `this.BOOKMARK_BUTTON_SHORTCUT`, `this._itemGuids.size`, `this._latestMenuItemL10nId`

## BUI_onMainMenuPopupShowing()
- 位置: L2052-2066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `gSync.getSyncPromoState()`
- 参照: `document.getElementById("menu_mobileBookmarks").hidden`, `event.target.id`, `remoteTabsPromo.dataset.action`, `remoteTabsPromo.hidden`

## showSubView()
- 位置: L2068-2070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._showSubView()`

## _showSubView()
- 位置: L2072-2082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `anchor.setAttribute()`, `document.getElementById()`, `this.updateLabel()`, `view.addEventListener()`
- 参照: `this.BOOKMARK_BUTTON_ID`, `this.toolbar.collapsed`

## BUI_onCommand()
- 位置: L2084-2102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(this.BOOKMARK_BUTTON_ID).forWindow()`, `this.button.getAttribute()`, `this.onStarCommand()`
- 条件付き依存: `if (this.button.getAttribute("cui-areatype") == CustomizableUI.TYPE_PANEL)` → `this._showSubView()`
- 条件付き依存: `if (widget.overflowed)` → `widget.node.removeAttribute()`
- 参照: `CustomizableUI.TYPE_PANEL`, `aEvent.currentTarget`, `aEvent.target`, `this.BOOKMARK_BUTTON_ID`, `widget.overflowed`

## onStarCommand()
- 位置: L2104-2112
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this._pendingUpdate && (aEvent.type != "click" || aEvent.button == 0) )` → `PlacesCommandHook.bookmarkPage()`
- 参照: `aEvent.button`, `aEvent.type`, `this._pendingUpdate`

## BUI_handleEvent()
- 位置: L2114-2130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onPanelMenuViewHiding()`, `this.onPanelMenuViewShowing()`
- 条件付き依存: `if (aEvent.target.id == "panelMenu_searchBookmarks")` → `PlacesCommandHook.searchBookmarks()`
- 条件付き依存: `if (aEvent.target.id == "panelMenu_viewBookmarksToolbar")` → `this.toggleBookmarksToolbar()`
- 参照: `aEvent.target.id`, `aEvent.type`

## BUI_onViewShowing()
- 位置: L2132-2157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addShortcut()`, `document.getElementById()`, `panelview.addEventListener()`, `panelview.getElementsByTagName()`, `panelview.removeEventListener()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_BOOKMARKS`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATEADDED_DESCENDING`, `aEvent.target`, `staticButtons.length`, `this._panelMenuView`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## BUI_onViewHiding()
- 位置: L2159-2165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.removeEventListener()`, `this._panelMenuView.uninit()`
- 参照: `aEvent.target`, `this._panelMenuView`

## handlePlacesEvents()
- 位置: L2167-2281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUIUtils.defaultParentGuid.then()`, `Services.tm.dispatchToMainThread()`, `this._itemGuids.has()`
- 条件付き依存: `if (!ev.isTagging && ev.url && ev.url == this._uri.spec)` → `this._itemGuids.has()`
- 条件付き依存: `if (!this._itemGuids.has(ev.guid))` → `this._itemGuids.add()`
- 条件付き依存: `if (ev.parentGuid === PlacesUtils.bookmarks.toolbarGuid)` → `Glean.browserEngagement.bookmarksToolbarBookmarkAdded.add()`
- 条件付き依存: `if (this._itemGuids.has(ev.guid))` → `this._itemGuids.delete()`
- 条件付き依存: `if ( ev.itemType == PlacesUtils.bookmarks.TYPE_FOLDER && ev.guid == parentGuid )` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (ev.oldParentGuid != PlacesUtils.bookmarks.toolbarGuid)` → `Glean.browserEngagement.bookmarksToolbarBookmarkAdded.add()`
- 条件付き依存: `if (this._itemGuids.has(ev.guid) && ev.url != this._uri.spec)` → `this._itemGuids.delete()`
- 条件付き依存: `if (this._itemGuids.size == 0)` → `this._updateStar()`
- 条件付き依存: `if (!(this._itemGuids.has(ev.guid) && ev.url != this._uri.spec))` → `this._itemGuids.has()`
- 条件付き依存: `if ( !this._itemGuids.has(ev.guid) && ev.url == this._uri.spec )` → `this._itemGuids.add()`
- 条件付き依存: `if (this._itemGuids.size == 1)` → `this._updateStar()`
- 条件付き依存: `if (isStarUpdateNeeded)` → `this._updateStar()`
- 条件付き依存: `if (affectsOtherBookmarksFolder)` → `this.maybeShowOtherBookmarksFolder().catch()`
- 条件付き依存: `if (affectsOtherBookmarksFolder)` → `this.maybeShowOtherBookmarksFolder()`
- 条件付き依存: `if (affectsBookmarksToolbarFolder)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (affectsBookmarksToolbarFolder)` → `this.updateEmptyToolbarMessage()`
- 参照: `PlacesUtils.bookmarks.TYPE_FOLDER`, `PlacesUtils.bookmarks.tagsGuid`, `PlacesUtils.bookmarks.toolbarGuid`, `PlacesUtils.bookmarks.unfiledGuid`, `StarUI.userHasTags`, `console.error`, `ev.guid`, `ev.isTagging`, `ev.itemType`, `ev.oldParentGuid`, `ev.parentGuid`, `ev.type`, `ev.url`, `this._itemGuids.size`, `this._uri.spec`
- XPCOM: `Services.prefs` / `Services.tm`

## onWidgetUnderflow()
- 位置: L2283-2292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._uninitView()`
- 参照: `aNode.documentGlobal`, `aNode.id`, `this.BOOKMARK_BUTTON_ID`

## maybeShowOtherBookmarksFolder()
- 位置: async L2294-2332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `PlacesUtils.bookmarks.fetch()`, `document.getElementById()`
- 条件付き依存: `if (!otherBookmarks)` → `PlacesUtils.getFolderContents()`
- 条件付き依存: `if (!otherBookmarks)` → `this.buildOtherBookmarksFolder()`
- 参照: `(await PlacesUtils.bookmarks.fetch(unfiledGuid)) .childCount`, `CustomizableUI.AREA_BOOKMARKS`, `PlacesUtils.bookmarks.unfiledGuid`, `PlacesUtils.getFolderContents(unfiledGuid).root`, `otherBookmarks.hidden`, `placement?.area`, `this._showOtherBookmarksInstance`, `toolbar?._placesView`

## buildShowOtherBookmarksMenuItem()
- 位置: L2334-2366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `PlacesUtils.bookmarks.fetch()`, `PlacesUtils.bookmarks.fetch(PlacesUtils.bookmarks.unfiledGuid).then()`, `Services.prefs.setBoolPref()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `menuItem.addEventListener()`, `menuItem.setAttribute()`, `menuItem.toggleAttribute()`
- 参照: `PlacesUtils.bookmarks.unfiledGuid`, `bm.childCount`, `menuItem.disabled`
- XPCOM: `Services.prefs`

## buildOtherBookmarksFolder()
- 位置: L2368-2405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `PlacesUtils.asContainer()`, `chevronButton.parentNode.append()`, `document .getElementById()`, `document .getElementById("PlacesToolbar") ._placesView._onOtherBookmarksPopupShowing()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `otherBookmarksButton.addEventListener()`, `otherBookmarksButton.appendChild()`, `otherBookmarksButton.setAttribute()`, `otherBookmarksPopup.classList.add()`, `otherBookmarksPopup.setAttribute()`, `otherBookmarksPopup.toggleAttribute()`
- 参照: `otherBookmarksButton._placesNode`, `otherBookmarksButton.className`, `otherBookmarksButton.hidden`, `otherBookmarksButton.id`, `otherBookmarksPopup._placesNode`, `otherBookmarksPopup.id`, `placesToolbar._placesView._otherBookmarks`, `placesToolbar._placesView._otherBookmarksPopup`
