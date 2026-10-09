# browser/components/customizableui/CustomizableWidgets.sys.mjs

source: browser/components/customizableui/CustomizableWidgets.sys.mjs
source-hash: 488c6036ddeb844b995a316d7ac0a048ef8b2a46
lines: 846

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `CustomizableWidgets.push()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## setAttributes()
- 位置: L67-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (!value)` → `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute(name))` → `aNode.removeAttribute()`
- 条件付き依存: `if (aAttrs.shortcutId)` → `doc.getElementById()`
- 条件付き依存: `if (shortcut)` → `additionalArgs.push()`
- 条件付き依存: `if (shortcut)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (name == "label" || name == "tooltiptext")` → `lazy.CustomizableUI.getLocalizedProperty()`
- 条件付き依存: `if (!(!value))` → `aNode.setAttribute()`
- 参照: `aAttrs.id`, `aAttrs.shortcutId`, `aNode.ownerDocument`

## handleEvent()
- 位置: L113-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onPanelMultiViewHidden()`, `this.onSubViewShowing()`, `this.onWindowUnload()`
- 条件付き依存: `if (target.id == "appMenuRecentlyClosedTabs")` → `PanelUI.showSubView()`
- 条件付き依存: `if (target.id == "appMenuRecentlyClosedWindows")` → `PanelUI.showSubView()`
- 条件付き依存: `if (target.id == "appMenuSearchHistory")` → `PlacesCommandHook.searchHistory()`
- 参照: `event.type`, `target.documentGlobal`, `target.id`, `this.id`, `this.recentlyClosedTabsPanel`, `this.recentlyClosedWindowsPanel`

## onViewShowing()
- 位置: L140-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `lazy.PanelMultiView.getViewNode()`, `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedTabsPanel ).addEventListener()`, `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedWindowsPanel ).addEventListener()`, `lazy.SessionStore.getClosedTabCount()`, `lazy.SessionStore.getClosedWindowCount()`, `panelview.addEventListener()`, `panelview.panelMultiView.addEventListener()`, `window.addEventListener()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_DESCENDING`, `document.defaultView`, `event.target`, `lazy.PanelMultiView.getViewNode( document, "appMenu-restoreSession" ).hidden`, `lazy.PanelMultiView.getViewNode( document, "appMenuRecentlyClosedTabs" ).disabled`, `lazy.PanelMultiView.getViewNode( document, "appMenuRecentlyClosedWindows" ).disabled`, `lazy.SessionStore.canRestoreLastSession`, `panelview.ownerDocument`, `this._panelMenuView`, `this.recentlyClosedTabsPanel`, `this.recentlyClosedWindowsPanel`, `window.PlacesPanelview`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## onViewHiding()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`

## onPanelMultiViewHidden()
- 位置: L196-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelMultiView.removeEventListener()`
- 条件付き依存: `if (this._panelMenuView)` → `this._panelMenuView.uninit()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedTabsPanel ).removeEventListener()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedWindowsPanel ).removeEventListener()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode( document, this.viewId ).removeEventListener()`
- 参照: `event.target`, `panelMultiView.ownerDocument`, `this._panelMenuView`, `this.recentlyClosedTabsPanel`, `this.recentlyClosedWindowsPanel`, `this.viewId`

## onWindowUnload()
- 位置: L217-221
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._panelMenuView`

## onSubViewShowing()
- 位置: L222-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `body.appendChild()`, `document.createXULElement()`, `element.classList.contains()`, `lazy.CustomizableUI.addShortcut()`, `panelview.appendChild()`, `this._panelMenuView._setEmptyPopupStatus()`, `this._panelMenuView.clearAllContents()`, `utils.getTabsFragment()`, `utils.getWindowsFragment()`
- 参照: `body.children`, `body.className`, `document.defaultView`, `element.tagName`, `event.target`, `event.target.ownerDocument`, `fragment.childElementCount`, `lazy.RecentlyClosedTabsAndWindowsMenuUtils`, `panelview.id`, `this.recentlyClosedTabsPanel`

## onCreated()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.setAttribute()`

## onCreated()
- 位置: L273-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.setAttribute()`

## onCommand()
- 位置: L281-286
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win.gLazyFindCommand)` → `win.gLazyFindCommand()`
- 参照: `aEvent.target.documentGlobal`, `win.gLazyFindCommand`

## onCreated()
- 位置: L292-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.setAttribute()`

## onCommand()
- 位置: L301-308
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.sidebarRevampEnabled)` → `SidebarController.handleToolbarButtonClick()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `SidebarController.toggle()`
- 参照: `aEvent.target.documentGlobal`, `lazy.sidebarRevampEnabled`

## onCreated()
- 位置: L309-329
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.sidebarRevampEnabled)` → `SidebarController.updateToolbarButton()`
- 条件付き依存: `if (lazy.sidebarRevampEnabled)` → `aNode.setAttribute()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `doc.createXULElement()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `obChecked.setAttribute()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `obPosition.setAttribute()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `aNode.appendChild()`
- 参照: `aNode.documentGlobal`, `aNode.ownerDocument`, `lazy.sidebarRevampEnabled`

## onBuild()
- 位置: L335-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDocument.createXULElement()`, `buttons.forEach()`, `lazy.CustomizableUI.getLocalizedProperty()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `setAttributes()`
- 条件付き依存: `if (aIndex != 0)` → `node.appendChild()`
- 条件付き依存: `if (aIndex != 0)` → `aDocument.createXULElement()`

## onBuild()
- 位置: L395-468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDocument.createXULElement()`, `buttons.forEach()`, `lazy.CustomizableUI.addListener()`, `lazy.CustomizableUI.getLocalizedProperty()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `setAttributes()`
- 条件付き依存: `if (aIndex != 0)` → `node.appendChild()`
- 条件付き依存: `if (aIndex != 0)` → `aDocument.createXULElement()`

## onWidgetInstanceRemoved()
- 位置: L448-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.removeListener()`
- 参照: `this.id`

## onWidgetOverflow()
- 位置: L454-458
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetNode == node)` → `node.documentGlobal.updateEditUIVisibility()`

## onWidgetUnderflow()
- 位置: L459-463
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetNode == node)` → `node.documentGlobal.updateEditUIVisibility()`

## onCommand()
- 位置: L473-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.view.BrowserCommands.forceEncodingDetection()`

## onCommand()
- 位置: L480-483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.MailIntegration.sendLinkForBrowser()`
- 参照: `aEvent.view`, `win.gBrowser.selectedBrowser`

## onCommand()
- 位置: L488-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.openPasswordManager()`
- 参照: `aEvent.view`

## onBuild()
- 位置: L501-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `aDocument.createXULElement()`, `aDocument.l10n.setAttributes()`, `lazy.SharingUtils.populateSharePopup()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `popup.addEventListener()`, `popup.setAttribute()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `node.classList.add()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `node.addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Cu.getWeakReference()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `lazy.SharingUtils.shareOnMacPicker()`
- 参照: `AppConstants.platform`, `aDocument.defaultView.gBrowser.selectedBrowser`, `node.browsersToShare`, `node.contextBrowserToShare`

## onViewShowing()
- 位置: L549-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.l10n.setAttributes()`, `lazy.PanelMultiView.getViewNode()`, `panelview.addEventListener()`, `panelview.querySelector()`, `syncNowBtn.getAttribute()`, `syncNowButton.addEventListener()`
- 参照: `aEvent.target`, `aEvent.target.ownerDocument`, `doc.defaultView.SyncedTabsPanelList`, `panelview.documentGlobal.gSync._isCurrentlySyncing`, `panelview.ownerDocument`, `panelview.syncedTabsPanelList`

## onViewHiding()
- 位置: L575-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PanelMultiView.getViewNode()`, `panelview.removeEventListener()`, `panelview.syncedTabsPanelList.destroy()`, `syncNowButton.removeEventListener()`
- 参照: `aEvent.target`, `aEvent.target.ownerDocument`, `panelview.syncedTabsPanelList`

## handleEvent()
- 位置: L587-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSync.doSync()`, `gSync.openConnectAnotherDevice()`, `gSync.openDevicesManagementPage()`, `gSync.openPrefs()`, `gSync.refreshSyncButtonsTooltip()`
- 参照: `aEvent.target`, `aEvent.type`, `button.documentGlobal`, `button.id`

## onBuild()
- 位置: L630-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `aDocument.createXULElement()`, `aDocument.documentGlobal.addEventListener()`, `aDocument.documentGlobal.gBrowser.addTabsProgressListener()`, `aDocument.documentGlobal.gSync.populateSendTabToolbarButton()`, `aDocument.l10n.setAttributes()`, `enableDisableButton()`, `lazy.CustomizableUI.addListener()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `popup.addEventListener()`, `popup.setAttribute()`
- 参照: `this.id`
- XPCOM: `Services.obs` / `Services.prefs`

## enableDisableButton()
- 位置: L639-644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDocument.documentGlobal.gSync.sendTabToolbarButtonShouldBeEnabled()`
- 参照: `aDocument.documentGlobal.gBrowser.currentURI`, `node.disabled`

## onLocationChange()
- 位置: L661-665
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (webProgress.isTopLevel)` → `enableDisableButton()`
- 参照: `webProgress.isTopLevel`

## onWidgetInstanceRemoved()
- 位置: L674-698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `aDocument.documentGlobal.gBrowser.removeTabsProgressListener()`, `aDocument.documentGlobal.removeEventListener()`, `lazy.CustomizableUI.removeListener()`
- 参照: `this.id`
- XPCOM: `Services.obs` / `Services.prefs`

## onCommand()
- 位置: L718-721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.openPreferences()`
- 参照: `aEvent.target.documentGlobal`

## forgetButtonCalled()
- 位置: L734-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.wm.getMostRecentWindow()`, `doc.getElementById()`, `lazy.Sanitizer.getClearRange()`, `lazy.Sanitizer.sanitize()`, `promise.then()`
- 条件付き依存: `if (otherWindow.closed)` → `console.error()`
- 条件付き依存: `if (otherWindow.PanicButtonNotifier)` → `otherWindow.PanicButtonNotifier.notify()`
- 参照: `aEvent.target.ownerDocument`, `doc.defaultView`, `group.value`, `otherWindow.PanicButtonNotifier`, `otherWindow.PanicButtonNotifierShouldNotify`, `otherWindow.closed`
- XPCOM: `Services.wm`

## handleEvent()
- 位置: L769-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.forgetButtonCalled()`
- 参照: `aEvent.type`

## onViewShowing()
- 位置: L776-792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.querySelector()`, `doc.getElementById()`, `doc.l10n.translateElements()`, `forgetButton.addEventListener()`
- 条件付き依存: `if (eventBlocker)` → `aEvent.detail.addBlocker()`
- 参照: `aEvent.target`, `aEvent.target.documentGlobal`, `group.selectedItem`, `win.document`

## onViewHiding()
- 位置: L793-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.querySelector()`, `forgetButton.removeEventListener()`

## onCommand()
- 位置: L807-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.OpenBrowserWindow()`
- 参照: `e.target.documentGlobal`

## onCreated()
- 位置: L826-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.setAttribute()`

## onCommand()
- 位置: L836-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ScreenshotsUtils.toggle()`
- 参照: `aEvent.currentTarget.documentGlobal`, `lazy.SELECTION_MODES.MINI_WINDOW`, `win.gBrowser.selectedBrowser`
