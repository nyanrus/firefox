# browser/base/content/navigator-toolbox.js

source: browser/base/content/navigator-toolbox.js
source-hash: a24b4daf8639d4cceae79b19611ff82659f43f61
lines: 579

## <module>
- 役割: navigator-toolbox とウィジェットのオーバーフローパネルに対し、ポップアップ表示・コマンド・マウス・キー・ドラッグのイベントを委譲で受け、クリックされた要素の ID ごとに各ハンドラーへ振り分ける。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `document .getElementById()`, `document .getElementById("identity-box") .addEventListener()`, `document .getElementById("sidebar-container") .addEventListener()`, `document .getElementById("trust-icon-container") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `event.target.closest()`, `gIdentityHandler.onDragStart()`, `gProtectionsHandler.onTrackingProtectionIconHoveredOrFocused()`, `navigatorToolbox.addEventListener()`, `pbInfoPanel?.addEventListener()`, `trackingProtectionIconContainer.addEventListener()`, `widgetOverflow.addEventListener()`

## onPopupShowing()
- 位置: L16-41
- 役割: ポップアップ表示時に、Places の chevron ポップアップや『ブックマーク』系メニューへ PlacesMenu を遅延生成し、ブックマーク用メニューには BookmarkingUI の表示準備も行う。
- 触るとき: ブックマークメニューやツールバーのシェブロン内の内容が表示されないとき、または表示前の初期化の順序を変えるとき。
- 呼び出し先: `BookmarkingUI.onPopupShowing()`, `document .getElementById()`, `document .getElementById("PlacesToolbar") ._placesView._onChevronPopupShowing()`
- 参照: `PlacesUtils.bookmarks.menuGuid`, `PlacesUtils.bookmarks.mobileGuid`, `PlacesUtils.bookmarks.toolbarGuid`, `PlacesUtils.bookmarks.unfiledGuid`, `event.target.id`, `event.target.parentNode._placesView`

## onCommand()
- 位置: L45-117
- 役割: コマンドを closest で対象要素に絞り、ID ごとに Firefox View、ブックマーク、移行ウィザード、サイドバーなどを開く。content-analysis 表示器はパネルを開き、プライベートブラウジング表示器はパネルを開閉する。どれにも当たらなければ例外を投げる。
- 触るとき: ツールバーのブックマーク・インポート・プライベートブラウジング表示器などのクリック動作を変えるとき、または新しいツールバー要素を追加して Missing case の例外が出るとき。
- 呼び出し先: `BookmarkingUI.onCommand()`, `BookmarkingUI.toggleBookmarksToolbar()`, `BookmarksEventHandler.onCommand()`, `FirefoxViewHandler.openTab()`, `MigrationUtils.showMigrationWizard()`, `PlacesCommandHook.searchBookmarks()`, `PlacesToolbarHelper.onPlaceholderCommand()`, `SidebarController.toggle()`, `element.classList.contains()`, `event.target.closest()`
- 条件付き依存: `if (element.classList.contains("content-analysis-indicator"))` → `ContentAnalysis.showPanel()`
- 条件付き依存: `if (!(element.classList.contains("content-analysis-indicator")))` → `element.classList.contains()`
- 条件付き依存: `if ( element.classList.contains("private-browsing-indicator-button") )` → `document.getElementById()`
- 条件付き依存: `if (panel.state == "open")` → `panel.hidePopup()`
- 条件付き依存: `if (panel.state == "closed")` → `panel.openPopup()`
- 参照: `MigrationUtils.MIGRATION_ENTRYPOINTS.BOOKMARKS_TOOLBAR`, `element.id`, `panel.state`

## onMouseDown()
- 位置: L130-176
- 役割: 対象要素ごとに、Firefox View、全タブ一覧、ページアクション、ダウンロード、FxA、拡張機能、ライブラリのパネルを mousedown で開く。該当しなければ例外を投げる。
- 触るとき: ツールバーボタンの開き方を mousedown 基準で変えるとき、またはクリックで開くべきパネルが開かないとき。
- 呼び出し先: `BrowserPageActions.mainButtonClicked()`, `DownloadsIndicatorView.onCommand()`, `FirefoxViewHandler.openToolbarMouseEvent()`, `PanelUI.showSubView()`, `event.target.closest()`, `gSync.toggleAccountPanel()`, `gTabsPanel.showAllTabsPanel()`, `gUnifiedExtensions.togglePanel()`
- 参照: `element.id`

## onMouseUp()
- 位置: L180-198
- 役割: PlacesToolbar や BMB_bookmarksPopup 上の mouseup を BookmarksEventHandler.onMouseUp へ渡す。それ以外は例外を投げる。
- 触るとき: ブックマークツールバーの中クリックなど mouseup 由来の操作を変えるとき。
- 呼び出し先: `BookmarksEventHandler.onMouseUp()`, `event.target.closest()`
- 参照: `element.id`

## onClick()
- 位置: L202-330
- 役割: 左クリックかどうかを判定したうえで、新規タブ、戻る・進む・更新、リーダー表示、PiP、ズームのリセット、ブックマーク星、ホーム、ブックマーク、保護・ID・翻訳、分割表示、AI サイドバーの各ボタンへ振り分ける。中クリックの扱いは checkForMiddleClick などに任せる。該当しなければ例外を投げる。
- 触るとき: ツールバーボタンのクリック挙動を変えるとき、特に左クリックのみで動く機能を追加するとき、または保護パネル(trust panel)の表示切替を調べるとき。
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
- 役割: Enter または Space を左クリック相当とみなし、ツールバーの同じ種類のボタンを onClick と同様に操作する。キー操作で開くパネルを含む。キャプチャ段階で登録され、browser-toolbarKeyNav.js より先に処理される。
- 触るとき: キーボードでツールバーボタンを操作したときの動作がマウス操作と食い違うとき、またはキー操作で新しいボタンを使えるようにするとき。
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
- 役割: 新規タブ、ダウンロード、新規ウィンドウ、ブックマーク、ホームの各ボタンへのドラッグを、dragenter・dragover・dragleave・drop の種類ごとに該当ハンドラーへ渡す。ホームは locked のときドラッグを受け付けない。
- 触るとき: ツールバーボタンへのリンクやブックマークのドロップ動作を変えるとき、またはホームボタンへのドロップが効かない原因を調べるとき。
- 呼び出し先: `PlacesMenuDNDHandler.onDragEnter()`, `PlacesMenuDNDHandler.onDragLeave()`, `PlacesMenuDNDHandler.onDragOver()`, `PlacesMenuDNDHandler.onDrop()`, `event.target.closest()`
- 条件付き依存: `if (event.type === "dragenter" || event.type === "dragover")` → `ToolbarDropHandler.onDragOver()`
- 条件付き依存: `if (event.type === "drop")` → `ToolbarDropHandler.onDropNewTabButtonObserver()`
- 条件付き依存: `if (event.type === "dragenter" || event.type === "dragover")` → `DownloadsIndicatorView.onDragOver()`
- 条件付き依存: `if (event.type === "drop")` → `DownloadsIndicatorView.onDrop()`
- 条件付き依存: `if (event.type === "drop")` → `ToolbarDropHandler.onDropNewWindowButtonObserver()`
- 条件付き依存: `if (event.type == "drop")` → `ToolbarDropHandler.onDropHomeButtonObserver()`
- 参照: `HomePage.locked`, `element.id`, `event.dropEffect`, `event.type`
