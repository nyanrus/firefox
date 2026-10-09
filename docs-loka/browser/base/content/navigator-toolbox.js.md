# browser/base/content/navigator-toolbox.js

source: browser/base/content/navigator-toolbox.js
source-hash: a24b4daf8639d4cceae79b19611ff82659f43f61
lines: 579

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `document .getElementById()`, `document .getElementById("identity-box") .addEventListener()`, `document .getElementById("sidebar-container") .addEventListener()`, `document .getElementById("trust-icon-container") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `event.target.closest()`, `gIdentityHandler.onDragStart()`, `gProtectionsHandler.onTrackingProtectionIconHoveredOrFocused()`, `navigatorToolbox.addEventListener()`, `pbInfoPanel?.addEventListener()`, `trackingProtectionIconContainer.addEventListener()`, `widgetOverflow.addEventListener()`

## onPopupShowing()
- 位置: L16-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkingUI.onPopupShowing()`, `document .getElementById()`, `document .getElementById("PlacesToolbar") ._placesView._onChevronPopupShowing()`
- 参照: `PlacesUtils.bookmarks.menuGuid`, `PlacesUtils.bookmarks.mobileGuid`, `PlacesUtils.bookmarks.toolbarGuid`, `PlacesUtils.bookmarks.unfiledGuid`, `event.target.id`, `event.target.parentNode._placesView`

## onCommand()
- 位置: L45-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarkingUI.onCommand()`, `BookmarkingUI.toggleBookmarksToolbar()`, `BookmarksEventHandler.onCommand()`, `FirefoxViewHandler.openTab()`, `MigrationUtils.showMigrationWizard()`, `PlacesCommandHook.searchBookmarks()`, `PlacesToolbarHelper.onPlaceholderCommand()`, `SidebarController.toggle()`, `element.classList.contains()`, `event.target.closest()`
- 条件付き依存: `if (element.classList.contains("content-analysis-indicator"))` → `ContentAnalysis.showPanel()`
- 条件付き依存: `if (!(element.classList.contains("content-analysis-indicator")))` → `element.classList.contains()`
- 条件付き依存: `if ( element.classList.contains("private-browsing-indicator-button") )` → `document.getElementById()`
- 条件付き依存: `if (panel.state == "open")` → `panel.hidePopup()`
- 条件付き依存: `if (panel.state == "closed")` → `panel.openPopup()`
- 参照: `MigrationUtils.MIGRATION_ENTRYPOINTS.BOOKMARKS_TOOLBAR`, `element.id`, `panel.state`

## onMouseDown()
- 位置: L130-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserPageActions.mainButtonClicked()`, `DownloadsIndicatorView.onCommand()`, `FirefoxViewHandler.openToolbarMouseEvent()`, `PanelUI.showSubView()`, `event.target.closest()`, `gSync.toggleAccountPanel()`, `gTabsPanel.showAllTabsPanel()`, `gUnifiedExtensions.togglePanel()`
- 参照: `element.id`

## onMouseUp()
- 位置: L180-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarksEventHandler.onMouseUp()`, `event.target.closest()`
- 参照: `element.id`

## onClick()
- 位置: L202-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BookmarksEventHandler.onClick()`, `BrowserCommands.home()`, `BrowserPageActions.doCommandForAction()`, `FullPageTranslationsPanel.open()`, `PageActions.actionForID()`, `PageProxyClickHandler()`, `UrlbarPrefs.get()`, `checkForMiddleClick()`, `event.target.closest()`, `gBrowser.handleNewTabMiddleClick()`, `gIdentityHandler.handleIdentityButtonEvent()`, `gPermissionPanel.handleIdentityButtonEvent()`, `gProtectionsHandler.handleProtectionsButtonEvent()`, `gTrustPanelHandler.handleProtectionsButtonEvent()`
- 条件付き依存: `if (isLeftClick)` → `AboutReaderParent.toggleReaderMode()`
- 条件付き依存: `if (isLeftClick)` → `PictureInPicture.toggleUrlbar()`
- 条件付き依存: `if (isLeftClick)` → `FullZoom.resetFromURLBar()`
- 条件付き依存: `if (isLeftClick && event.target.localName == "a")` → `PlacesCommandHook.showPlacesOrganizer()`
- 条件付き依存: `if (UrlbarPrefs.get("trustPanel.featureGate"))` → `gTrustPanelHandler.handleProtectionsButtonEvent()`
- 条件付き依存: `if (isLeftClick)` → `gBrowser.openSplitViewMenu()`
- 条件付き依存: `if (isLeftClick)` → `AIWindowUI.toggleSidebar()`
- 参照: `element._placesView`, `element.id`, `element.parentNode._placesView`, `event.button`, `event.target.localName`

## onKeyPress()
- 位置: L337-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserPageActions.doCommandForAction()`, `BrowserPageActions.mainButtonClicked()`, `DownloadsIndicatorView.onCommand()`, `FullPageTranslationsPanel.open()`, `PageActions.actionForID()`, `PanelUI.showSubView()`, `event.target.closest()`, `gIdentityHandler.handleIdentityButtonEvent()`, `gPermissionPanel.handleIdentityButtonEvent()`, `gProtectionsHandler.handleProtectionsButtonEvent()`, `gSync.toggleAccountPanel()`, `gTabsPanel.showAllTabsPanel()`, `gTrustPanelHandler.handleProtectionsButtonEvent()`, `gUnifiedExtensions.togglePanel()`
- 条件付き依存: `if (isLikeLeftClick)` → `AboutReaderParent.toggleReaderMode()`
- 条件付き依存: `if (isLikeLeftClick)` → `PictureInPicture.toggleUrlbar()`
- 条件付き依存: `if (isLikeLeftClick)` → `FullZoom.resetFromURLBar()`
- 条件付き依存: `if (isLikeLeftClick && event.target.localName == "a")` → `PlacesCommandHook.showPlacesOrganizer()`
- 条件付き依存: `if (isLikeLeftClick)` → `BrowserCommands.home()`
- 条件付き依存: `if (isLikeLeftClick)` → `gBrowser.openSplitViewMenu()`
- 条件付き依存: `if (isLikeLeftClick)` → `AIWindowUI.toggleSidebar()`
- 参照: `element.id`, `event.key`, `event.target.localName`

## onDragAndDrop()
- 位置: L476-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesMenuDNDHandler.onDragEnter()`, `PlacesMenuDNDHandler.onDragLeave()`, `PlacesMenuDNDHandler.onDragOver()`, `PlacesMenuDNDHandler.onDrop()`, `event.target.closest()`
- 条件付き依存: `if (event.type === "dragenter" || event.type === "dragover")` → `ToolbarDropHandler.onDragOver()`
- 条件付き依存: `if (event.type === "drop")` → `ToolbarDropHandler.onDropNewTabButtonObserver()`
- 条件付き依存: `if (event.type === "dragenter" || event.type === "dragover")` → `DownloadsIndicatorView.onDragOver()`
- 条件付き依存: `if (event.type === "drop")` → `DownloadsIndicatorView.onDrop()`
- 条件付き依存: `if (event.type === "drop")` → `ToolbarDropHandler.onDropNewWindowButtonObserver()`
- 条件付き依存: `if (event.type == "drop")` → `ToolbarDropHandler.onDropHomeButtonObserver()`
- 参照: `HomePage.locked`, `element.id`, `event.dropEffect`, `event.type`
