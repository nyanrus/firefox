# browser/base/content/browser-places.js

source: browser/base/content/browser-places.js
source-hash: 20220bd0969b96d2ec8c297fb349ca1935338364
lines: 2407

## <module>
- 役割: ブックマーク編集パネル（StarUI）、ブックマーク・履歴メニューのイベント処理、ブックマークツールバーと管理ブックマーク、スターボタン（BookmarkingUI）を担うファイル。
- 呼び出し先: `BookmarkingUI.maybeShowOtherBookmarksFolder()`, `BookmarkingUI.maybeShowOtherBookmarksFolder().then()`, `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `document .getElementById()`, `document .getElementById("PlacesToolbar") ?._placesView?.updateNodesVisibility()`

## _element()
- 位置: L57-59
- 役割: ID で DOM 要素を取得する小さな helper。
- 触るとき: 編集パネルの各要素を参照する箇所で、取得方法をまとめて変えたいとき。
- 呼び出し先: `document.getElementById()`

## panel()
- 位置: L62-79
- 役割: 編集パネルを初回参照時に生成し、イベントを登録して要素を返す（以後は値をキャッシュ）。
- 触るとき: パネルが初めて開くときにイベントが届かない、または生成タイミングを変えたいとき。
- 呼び出し先: `element.addEventListener()`, `this._createPanelIfNeeded()`, `this._element()`
- 参照: `element.hidden`, `this.panel`

## handleEvent()
- 位置: L82-184
- 役割: 編集パネルのキー、マウス、IME 合成、popupshown/popuphidden を処理し、新規ブックマークは一定時間後に自動で閉じる。
- 触るとき: 編集パネルの自動クローズ条件や Escape・Enter の挙動を変えるとき。
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
- 役割: パネルを閉じたときの後処理。キャンセルなら何もせず、削除指定なら Remove かスター解除を行い、通常時は設定保存・最近のフォルダー更新・確認ヒント表示を行う。
- 触るとき: パネルを閉じたときに保存するか破棄するかの分岐を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `bookmarkState.save()`, `gEditItemOverlay.uninitPanel()`, `this._element()`, `this._storeRecentlyUsedFolder()`
- 条件付き依存: `if (!this._isNewBookmark)` → `PlacesTransactions.Remove(guidsForRemoval).transact()`
- 条件付き依存: `if (!this._isNewBookmark)` → `PlacesTransactions.Remove()`
- 条件付き依存: `if (!(!this._isNewBookmark))` → `BookmarkingUI.star.removeAttribute()`
- 条件付き依存: `if (this._isNewBookmark)` → `this.showConfirmation()`
- 参照: `this._cancelOnPopupHidden`, `this._element("editBookmarkPanel_showForNewBookmarks").checked`, `this._isNewBookmark`, `this._itemGuids`, `this._removeBookmarksOnPopupHidden`
- XPCOM: `Services.prefs`

## showEditBookmarkPopup()
- 位置: async L229-305
- 役割: 既存ブックマーク件数とタグの有無から、タイトル・削除ボタン文言・隠す行を決めて編集パネルを初期化し、スター付近に開く。
- 触るとき: 編集パネルの表示内容（タイトル、削除ボタン文言、隠す行）を変えるとき。
- 呼び出し先: `PlacesUtils.bookmarks.fetch()`, `document.l10n.setAttributes()`, `gEditItemOverlay.initPanel()`, `this._element()`, `this._itemGuids.push()`, `this.panel.openPopup()`
- 条件付き依存: `if (this._isNewBookmark)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._isNewBookmark))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (this.userHasTags === undefined)` → `PlacesUtils.bookmarks.fetchTags()`
- 条件付き依存: `if (!this.userHasTags)` → `hiddenRows.push()`
- 参照: `BookmarkingUI.anchor`, `bookmark.guid`, `fetchedTags.length`, `this._element("editBookmarkPanel_showForNewBookmarks").checked`, `this._isNewBookmark`, `this._itemGuids`, `this._itemGuids.length`, `this.panel.state`, `this.showForNewBookmarks`, `this.userHasTags`

## onPanelReady()
- 位置: L266-281
- 役割: パネルの親要素に capture 付きの popupshown リスナーを一度だけ登録し、表示後に fn を呼ぶ。
- 触るとき: パネルが表示された直後に、他のリスナーより先に処理を走らせたいとき。
- 呼び出し先: `fn()`, `target.addEventListener()`
- 参照: `target.parentNode`, `this.panel`

## _createPanelIfNeeded()
- 位置: L307-315
- 役割: 編集パネルの DOM が無ければ FTL を読み込み、テンプレートを複製して差し替える。
- 触るとき: 編集パネルの初回表示が遅い、または DOM が無い状態で参照されて失敗する問題を調べるとき。
- 呼び出し先: `this._element()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `this._element()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `template.content.cloneNode()`
- 条件付き依存: `if (!this._element("editBookmarkPanel"))` → `template.replaceWith()`

## SU_removeBookmarkButtonCommand()
- 位置: L317-320
- 役割: 削除ボタンで削除フラグを立ててパネルを閉じ、実際の削除はパネルが閉じた後の処理に任せる。
- 触るとき: 編集パネルの削除ボタンを即時削除からクローズ時の削除に変える、といった変更をするとき。
- 呼び出し先: `this.panel.hidePopup()`
- 参照: `this._removeBookmarksOnPopupHidden`

## _storeRecentlyUsedFolder()
- 位置: async L322-366
- 役割: 変更された保存先を既定値に保存し、最近使ったフォルダーのリストを先頭に更新して上限数まで切り詰める（index が 1 の項目は先頭へ移動しない）。
- 触るとき: 最近使ったフォルダーの並びや保存先の既定値を変えるとき。
- 呼び出し先: `PlacesUtils.bookmarks.userContentRoots.includes()`, `PlacesUtils.metadata.get()`, `PlacesUtils.metadata.set()`, `lastUsedFolderGuids.indexOf()`, `lastUsedFolderGuids.pop()`
- 条件付き依存: `if ( didChangeFolder && selectedFolderGuid !== PlacesUtils.bookmarks.mobileGuid )` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (index > 1)` → `lastUsedFolderGuids.splice()`
- 条件付き依存: `if (index > 1)` → `lastUsedFolderGuids.unshift()`
- 条件付き依存: `if (index == -1)` → `lastUsedFolderGuids.unshift()`
- 参照: `PlacesUIUtils.LAST_USED_FOLDERS_META_KEY`, `PlacesUIUtils.maxRecentFolders`, `PlacesUtils.bookmarks.mobileGuid`, `lastUsedFolderGuids.length`
- XPCOM: `Services.prefs`

## showConfirmation()
- 位置: L368-397
- 役割: 「ブックマークに保存」のヒントを、表示回数が 3 回未満のときだけ出す。アンカーはライブラリかブックマークボタン、無ければアプリメニュー。
- 触るとき: 保存確認ヒントの表示回数制限や表示位置を変えるとき。
- 呼び出し先: `ConfirmationHint.show()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- 条件付き依存: `if (window.toolbar.visible)` → `document.getElementById()`
- 条件付き依存: `if (window.toolbar.visible)` → `element.getAttribute()`
- 条件付き依存: `if (!anchor)` → `document.getElementById()`
- 参照: `window.toolbar.visible`
- XPCOM: `Services.prefs`

## bookmarkPage()
- 位置: async L410-472
- 役割: 現在ページの既存ブックマークを調べ、無ければタイトルとエラーページ判定を含めて新規作成し、設定に応じて編集パネルを開くか確認ヒントだけ出す。
- 触るとき: スターや「ブックマークに追加」の流れを変えるとき、エラーページでタイトルが付かない問題を調べるとき。
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
- 役割: リンク先 URL の既存ブックマークがあれば編集ダイアログ、無ければ追加ダイアログを開き、確定した guid を返す。
- 触るとき: リンクのコンテキストメニューからブックマークを追加・編集する流れを変えるとき。
- 呼び出し先: `PlacesUIUtils.showBookmarkDialog()`, `PlacesUtils.bookmarks.fetch()`, `Services.io.newURI()`
- 条件付き依存: `if (bm)` → `PlacesUIUtils.promiseNodeLikeFromFetchInfo()`
- 条件付き依存: `if (bm)` → `PlacesUIUtils.showBookmarkDialog()`
- 参照: `PlacesUIUtils.defaultParentGuid`, `window.top`
- XPCOM: `Services.io`

## bookmarkTabs()
- 位置: async L520-528
- 役割: 渡されたタブ（省略時は表示中の非固定タブ）を重複除去して、一括ブックマーク用ダイアログに渡す。
- 触るとき: すべてのタブをブックマークする対象（固定タブの扱いなど）を変えるとき。
- 呼び出し先: `Object.assign()`, `PlacesCommandHook.getUniquePages()`, `PlacesCommandHook.getUniquePages(tabs).map()`, `PlacesUIUtils.showBookmarkPagesDialog()`, `Services.io.createExposableURI()`, `gBrowser.visibleTabs.filter()`
- 参照: `page.uri`, `tab.pinned`
- XPCOM: `Services.io`

## getUniquePages()
- 位置: L534-549
- 役割: タブ群を spec で重複排除し、uri と title の配列を返す。タイトルは contentTitle、無ければタブのラベル。
- 触るとき: 一括ブックマークの重複判定やタイトルの取り方を変えるとき。
- 呼び出し先: `tabs.forEach()`
- 条件付き依存: `if (!(spec in uniquePages))` → `URIs.push()`
- 参照: `browser.contentTitle`, `browser.currentURI`, `tab.label`, `tab.linkedBrowser`, `uri.spec`

## showPlacesOrganizer()
- 位置: L559-574
- 役割: 開いているライブラリがあれば指定項目を選んで前面に出し、無ければ places.xhtml を開く。
- 触るとき: ライブラリを開く経路や選択できる項目名を追加・変更するとき。
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (!organizer || organizer.closed)` → `openDialog()`
- 条件付き依存: `if (!(!organizer || organizer.closed))` → `organizer.PlacesOrganizer.selectLeftPaneContainerByHierarchy()`
- 条件付き依存: `if (!(!organizer || organizer.closed))` → `organizer.focus()`
- 参照: `organizer.closed`
- XPCOM: `Services.wm`

## searchBookmarks()
- 位置: async L576-583
- 役割: 最前面のウィンドウ（無ければ新規作成）の URL バーを、ブックマーク検索モードにする。
- 触るとき: ブックマーク検索のショートカットやメニューからの入口を変えるとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `BrowserWindowTracker.promiseOpenWindow()`, `win.gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.BOOKMARK`

## searchTabs()
- 位置: async L585-593
- 役割: 最前面のウィンドウを前面に出し、URL バーを開いているタブの検索モードにする。検索モードの入口は引数で渡す。
- 触るとき: タブ検索の入口（メニュー・ショートカット）を追加するとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `BrowserWindowTracker.promiseOpenWindow()`, `win.focus()`, `win.gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`

## searchHistory()
- 位置: async L595-602
- 役割: 最前面のウィンドウ（無ければ新規作成）の URL バーを、履歴の検索モードにする。
- 触るとき: 履歴検索の入口や検索モードの指定を変えるとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `BrowserWindowTracker.promiseOpenWindow()`, `win.gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.HISTORY`

## HistoryMenu.constructor()
- 位置: L607-609
- 役割: 履歴メニューを、履歴の上位 15 件（sort=4、maxResults=15）を表示する PlacesMenu として初期化する。
- 触るとき: 履歴メニューに出す件数や並び順を変えるとき。
- 呼び出し先: `super()`

## HistoryMenu._init()
- 位置: L614-626
- 役割: 基底クラスの初期化後、閉じたタブ・非表示タブ・閉じたウィンドウ・同期タブ・リモートタブ促進の DOM 要素を id で取得して保持する。
- 触るとき: 履歴メニューに項目を追加して、その参照を持たせるとき。
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `super._init()`

## HistoryMenu.toggleHiddenTabs()
- 位置: L628-632
- 役割: 表示中のタブ数が全タブ数より少ないときだけ、非表示タブのメニューを表示する。
- 触るとき: 非表示タブがあるのにメニューが出ない、または出っぱなしになる問題を見るとき。
- 参照: `gBrowser.tabs.length`, `gBrowser.visibleTabs.length`, `this.hiddenTabsMenu.hidden`, `window.gBrowser`

## HistoryMenu.toggleRecentlyClosedTabs()
- 位置: L634-642
- 役割: 閉じたタブの数が 0 なら「最近閉じたタブ」サブメニューを無効化し、1 以上なら有効化する。
- 触るとき: 閉じたタブ履歴の有無によるサブメニューの有効化判定を変えるとき。
- 呼び出し先: `SessionStore.getClosedTabCount()`
- 条件付き依存: `if (SessionStore.getClosedTabCount() == 0)` → `this.undoTabMenu.setAttribute()`
- 条件付き依存: `if (!(SessionStore.getClosedTabCount() == 0))` → `this.undoTabMenu.removeAttribute()`

## HistoryMenu.populateUndoSubmenu()
- 位置: L647-670
- 役割: 「最近閉じたタブ」サブメニューの既存項目を消し、閉じたタブが無ければ無効化して戻る。あれば RecentlyClosedTabsAndWindowsMenuUtils のタブ断片を追加する。
- 触るとき: 閉じたタブ一覧の項目内容や並びを変えるとき、またはサブメニューが古い内容のまま残るとき。
- 呼び出し先: `RecentlyClosedTabsAndWindowsMenuUtils.getTabsFragment()`, `SessionStore.getClosedTabCount()`, `this.undoTabMenu.removeAttribute()`, `undoPopup.appendChild()`, `undoPopup.firstChild.remove()`, `undoPopup.hasChildNodes()`
- 条件付き依存: `if (SessionStore.getClosedTabCount() == 0)` → `this.undoTabMenu.setAttribute()`
- 参照: `this.undoTabMenu.menupopup`

## HistoryMenu.toggleRecentlyClosedWindows()
- 位置: L672-680
- 役割: 閉じたウィンドウの数が 0 なら「最近閉じたウィンドウ」サブメニューを無効化し、1 以上なら有効化する。
- 触るとき: 閉じたウィンドウ履歴の有無による有効化判定を変えるとき。
- 呼び出し先: `SessionStore.getClosedWindowCount()`
- 条件付き依存: `if (SessionStore.getClosedWindowCount() == 0)` → `this.undoWindowMenu.setAttribute()`
- 条件付き依存: `if (!(SessionStore.getClosedWindowCount() == 0))` → `this.undoWindowMenu.removeAttribute()`

## HistoryMenu.populateUndoWindowSubmenu()
- 位置: L685-710
- 役割: 「最近閉じたウィンドウ」サブメニューの既存項目を消し、無ければ無効化する。あれば RecentlyClosedTabsAndWindowsMenuUtils のウィンドウ断片を「すべて復元」なしで追加する。
- 触るとき: 閉じたウィンドウ一覧の内容や「すべて復元」の有無を変えるとき。
- 呼び出し先: `RecentlyClosedTabsAndWindowsMenuUtils.getWindowsFragment()`, `SessionStore.getClosedWindowCount()`, `this.undoWindowMenu.removeAttribute()`, `undoPopup.appendChild()`, `undoPopup.firstChild.remove()`, `undoPopup.hasChildNodes()`
- 条件付き依存: `if (SessionStore.getClosedWindowCount() == 0)` → `this.undoWindowMenu.setAttribute()`
- 参照: `this.undoWindowMenu.menupopup`

## HistoryMenu.toggleTabsFromOtherComputers()
- 位置: L712-740
- 役割: 同期の促進状態があれば促進項目を出して同期タブ項目を隠し、無ければ条件に応じて同期タブ項目の表示を切り替える。
- 触るとき: 「他の端末のタブ」と同期促進の出し分けを変えるとき。
- 呼び出し先: `PlacesUIUtils.shouldShowTabsFromOtherComputersMenuitem()`
- 条件付き依存: `if (this.remoteTabsPromo)` → `gSync.getSyncPromoState()`
- 参照: `this.remoteTabsPromo`, `this.remoteTabsPromo.dataset.action`, `this.remoteTabsPromo.hidden`, `this.syncTabsMenuitem`, `this.syncTabsMenuitem.hidden`

## HistoryMenu._onPopupShowing()
- 位置: L742-754
- 役割: 基底の処理の後、ルートの履歴メニューを開くたびに非表示タブ・閉じたタブ・閉じたウィンドウ・他端末のタブの各表示を更新する（サブメニューでは何もしない）。
- 触るとき: 履歴メニューを開いたときに更新すべき表示を増やすとき。
- 呼び出し先: `super._onPopupShowing()`, `this.toggleHiddenTabs()`, `this.toggleRecentlyClosedTabs()`, `this.toggleRecentlyClosedWindows()`, `this.toggleTabsFromOtherComputers()`
- 参照: `aEvent.target`, `this.rootElement`

## HistoryMenu._onCommand()
- 位置: L756-769
- 役割: 履歴項目の command を受け、プライベートでなければ入力済みとして記録し、そのリンクを UI リンクとして開く。
- 触るとき: 履歴項目をクリックしたときの開き方や入力履歴への記録を変えるとき。
- 呼び出し先: `BrowserUtils.getRootEvent()`
- 条件付き依存: `if (placesNode)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `PlacesUIUtils.markPageAsTyped()`
- 条件付き依存: `if (placesNode)` → `openUILink()`
- 条件付き依存: `if (placesNode)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 参照: `aEvent.target._placesNode`, `placesNode.uri`
- XPCOM: `Services.scriptSecurityManager`

## onMouseUp()
- 位置: L789-815
- 役割: ブックマークメニュー項目の mouseup で、中クリックや修飾キー付きクリックならメニューを閉じないよう closemenu を一時的に none にし、ポップアップが閉じたら戻す。
- 触るとき: 中クリックや修飾キーでタブを開いたときにメニューが閉じてしまう挙動を変えるとき。
- 条件付き依存: `if (modifKey || aEvent.button == 1)` → `target.setAttribute()`
- 条件付き依存: `if (modifKey || aEvent.button == 1)` → `menupopup.addEventListener()`
- 条件付き依存: `if (modifKey || aEvent.button == 1)` → `target.removeAttribute()`
- 条件付き依存: `if (!(modifKey || aEvent.button == 1))` → `target.removeAttribute()`
- 参照: `AppConstants.platform`, `PlacesUIUtils.openInTabClosesMenu`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.originalTarget`, `target.parentNode`, `target.tagName`

## BEH_onClick()
- 位置: L817-859
- 役割: ブックマークのクリックで、中クリックか修飾キー付きクリックのときだけ処理する。フォルダーなら中のリンクを一括でタブに開き、リンクなら onCommand に任せる。
- 触るとき: ブックマークを中クリックや修飾キーでタブに開く挙動を変えるとき。
- 呼び出し先: `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if ( PlacesUIUtils.openInTabClosesMenu && (tag == "menuitem" || tag == "menu") )` → `closeMenus()`
- 条件付き依存: `if (target.localName == "menu" || target.localName == "toolbarbutton")` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 条件付き依存: `if (aEvent.button == 1 && !(tag == "menuitem" || tag == "menu"))` → `this.onCommand()`
- 条件付き依存: `if (aEvent.button == 1 && !(tag == "menuitem" || tag == "menu"))` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.button == 1 && !(tag == "menuitem" || tag == "menu"))` → `aEvent.stopPropagation()`
- 参照: `AppConstants.platform`, `PlacesUIUtils.openInTabClosesMenu`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.originalTarget`, `aEvent.shiftKey`, `aEvent.target`, `target._placesNode`, `target.localName`, `target.tagName`

## BEH_onCommand()
- 位置: L869-889
- 役割: ブックマーク項目の command で対象ノードを開き、個人用ツールバー上なら計測を送る。同期プロモのアクションなら同期側に渡す。
- 触るとき: ブックマークを開く経路や、ツールバーからの利用を計測する箇所を変えるとき。
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
- 役割: ブックマークのツールチップを、ツリー・Places ノード・targetURI のどれかから組み立てる。ラベルが切れているか URL がある場合だけ表示する。
- 触るとき: ブックマークのツールチップの表示条件や内容（タイトルと URL）を変えるとき。
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
- 役割: ラベル要素の scrollWidth が clientWidth より大きい（省略されている）かを返す。
- 触るとき: ツールチップの省略判定を別の種類の要素にも広げるとき。
- 参照: `label.clientWidth`, `label.scrollWidth`

## PMDH_onDragEnter()
- 位置: L987-1023
- 役割: メニューへのドラッグ進入時に、静的なコンテナなら一定時間後にポップアップを自動で開き、閉じるための予約を取り消す。
- 触るとき: ドラッグ中の自動展開（ばね読み込み）の遅延や対象を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `event.preventDefault()`, `event.stopPropagation()`, `popup.openPopup()`, `popup.setAttribute()`, `this._isStaticContainer()`, `this._loadTimer.initWithCallback()`
- 条件付き依存: `if (this._closeTimer && this._closingTimerNode === event.currentTarget)` → `this._closeTimer.cancel()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `PlacesControllerDragHelper.currentDropTarget`, `event.currentTarget`, `event.target`, `event.target.menupopup`, `popup.state`, `this._closeTimer`, `this._closingTimerNode`, `this._loadTimer`, `this._springLoadDelayMs`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PMDH_onDragLeave()
- 位置: L1028-1070
- 役割: メニューからドラッグが外れたとき、自動で開いたポップアップを一定時間後に閉じる予約をする。ドラッグ先がその階層内なら閉じない。
- 触るとき: ドラッグ中に自動展開したメニューが早く閉じる問題を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `popup.hasAttribute()`, `this._closeTimer.initWithCallback()`, `this._isStaticContainer()`
- 条件付き依存: `if (this._loadTimer)` → `this._loadTimer.cancel()`
- 条件付き依存: `if (!inHierarchy && popup && popup.hasAttribute("autoopened"))` → `popup.removeAttribute()`
- 条件付き依存: `if (!inHierarchy && popup && popup.hasAttribute("autoopened"))` → `popup.hidePopup()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `PlacesControllerDragHelper.currentDropTarget`, `event.currentTarget`, `event.relatedTarget`, `event.relatedTarget.parentNode`, `event.target`, `event.target.menupopup`, `node.parentNode`, `this._closeDelayMs`, `this._closeTimer`, `this._closingTimerNode`, `this._loadTimer`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PMDH__isContainer()
- 位置: L1078-1089
- 役割: 要素が menu、または type=menu の toolbarbutton で、Places ビューの外にある静的コンテナかを判定する。
- 触るとき: ドラッグ対象となる静的メニューの範囲を変えるとき。
- 呼び出し先: `node.getAttribute()`, `node.menupopup.hasAttribute()`, `node.parentNode.hasAttribute()`
- 参照: `node.localName`, `node.menupopup`

## PMDH_onDragOver()
- 位置: L1097-1107
- 役割: メニューへのドラッグオーバーで、ブックマークメニューの直下に挿入できれば drop を許可する。
- 触るとき: ブックマークメニューへのドロップ可否の条件を変えるとき。
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `event.stopPropagation()`
- 条件付き依存: `if (ip && PlacesControllerDragHelper.canDrop(ip, event.dataTransfer))` → `event.preventDefault()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `PlacesUtils.bookmarks.menuGuid`, `event.dataTransfer`, `event.target`

## PMDH_onDrop()
- 位置: L1115-1123
- 役割: メニューへのドロップを、ブックマークメニューフォルダーの末尾への挿入として処理する。
- 触るとき: メニューへドロップした項目の挿入位置を変えるとき。
- 呼び出し先: `PlacesControllerDragHelper.onDrop()`, `event.stopPropagation()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `PlacesUtils.bookmarks.menuGuid`, `event.dataTransfer`

## _viewElt()
- 位置: L1131-1133
- 役割: id が PlacesToolbar の要素を返す。
- 触るとき: ブックマークツールバーのビュー要素の参照先を変えるとき。
- 呼び出し先: `document.getElementById()`

## init()
- 位置: async L1139-1142
- 役割: ツールバーの内容を読み込める状態（canLoadToolbarContentPromise）になるまで待ち、_realInit を呼ぶ。
- 触るとき: 起動時にブックマークツールバーの描画を始めるタイミングを変えるとき。
- 呼び出し先: `this._realInit()`
- 参照: `PlacesUIUtils.canLoadToolbarContentPromise`

## _realInit()
- 位置: L1147-1193
- 役割: ビュー要素があり窓が閉じていなければ CustomizableUI と表示切替のリスナーを登録し、親ツールバーが表示中なら PlacesToolbar を生成する。PersonalToolbar なら空メッセージも更新する。
- 触るとき: ツールバーが非表示やカスタマイズ中のときにビューを作らない条件を変えるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `document.getElementById()`, `getComputedStyle()`, `this._getParentToolbar()`
- 条件付き依存: `if (!this._isObservingToolbars)` → `window.addEventListener()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.updateEmptyToolbarMessage() .finally(() => { toolbar.toggleAttribute("initialized", true); }) .catch()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.updateEmptyToolbarMessage() .finally()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.updateEmptyToolbarMessage()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `toolbar.toggleAttribute()`
- 参照: `PlacesUtils.bookmarks.toolbarGuid`, `console.error`, `getComputedStyle(toolbar, "").display`, `this._isCustomizing`, `this._isObservingToolbars`, `this._viewElt`, `toolbar.collapsed`, `toolbar.id`, `viewElt._placesView`, `window.closed`

## getIsEmpty()
- 位置: async L1195-1201
- 役割: ビューが無ければ true、あれば再構築の完了を待ち、ツールバーの子が無いかを返す。
- 触るとき: ブックマークが無いときの空メッセージ表示の判定を調べるとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById("PlacesToolbarItems").hasChildNodes()`, `this._viewElt._placesView.promiseRebuilt()`
- 参照: `this._viewElt._placesView`

## handleEvent()
- 位置: L1203-1211
- 役割: toolbarvisibilitychange で、対象が自分の親ツールバーなら表示をリセットする。
- 触るとき: ツールバーの表示切替の後にブックマークビューが作り直されない問題を調べるとき。
- 呼び出し先: `this._getParentToolbar()`
- 条件付き依存: `if (event.target == this._getParentToolbar(this._viewElt))` → `this._resetView()`
- 参照: `event.target`, `event.type`, `this._viewElt`

## PTH_uninit()
- 位置: L1216-1222
- 役割: 表示切替のリスナーと CustomizableUI のリスナーを外す。
- 触るとき: ウィンドウ閉じ時のブックマークツールバーの後始末を変えるとき。
- 呼び出し先: `CustomizableUI.removeListener()`
- 条件付き依存: `if (this._isObservingToolbars)` → `window.removeEventListener()`
- 参照: `this._isObservingToolbars`

## PTH_customizeStart()
- 位置: L1224-1233
- 役割: カスタマイズ開始時に既存ビューを uninit し、カスタマイズ中フラグを立てる。
- 触るとき: カスタマイズモードでブックマークツールバーのビューを外す挙動を変えるとき。
- 条件付き依存: `if (viewElt && viewElt._placesView)` → `viewElt._placesView.uninit()`
- 参照: `this._isCustomizing`, `this._viewElt`, `viewElt._placesView`

## PTH_customizeDone()
- 位置: L1235-1238
- 役割: カスタマイズ中フラグを下ろし、init を呼んでビューを作り直す。
- 触るとき: カスタマイズ終了後にブックマークツールバーが戻らない問題を調べるとき。
- 呼び出し先: `this.init()`
- 参照: `this._isCustomizing`

## onPlaceholderCommand()
- 位置: L1240-1249
- 役割: 個人用ブックマークのプレースホルダーが溢れているかパネルにある場合、ライブラリのツールバー項目を開く。
- 触るとき: 溢れた状態でのブックマーク項目のクリックの挙動を変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `widgetGroup.forWindow()`
- 条件付き依存: `if ( widget.overflowed || widgetGroup.areaType == CustomizableUI.TYPE_PANEL )` → `PlacesCommandHook.showPlacesOrganizer()`
- 参照: `CustomizableUI.TYPE_PANEL`, `widget.overflowed`, `widgetGroup.areaType`

## _getParentToolbar()
- 位置: L1251-1259
- 役割: 要素の祖先をたどり、最初の toolbar 要素を返す。無ければ null。
- 触るとき: 親ツールバーを判定する条件を変えるとき。
- 参照: `element.localName`, `element.parentNode`

## onWidgetUnderflow()
- 位置: L1261-1268
- 役割: 個人用ブックマークがこのウィンドウで溢れたとき、ビューを作り直す（_resetView）。
- 触るとき: 溢れで壊れたブックマークツールバーを直す処理を追うとき。
- 条件付き依存: `if (aNode.id == "personal-bookmarks" && win == window)` → `this._resetView()`
- 参照: `aNode.documentGlobal`, `aNode.id`

## onWidgetAdded()
- 位置: L1270-1279
- 役割: カスタマイズ中でなければ、個人用ブックマークの項目が追加されたときにビューを作り直す。
- 触るとき: メニューやツールバーへの追加操作の後にブックマーク項目が壊れる問題を調べるとき。
- 条件付き依存: `if (aWidgetId == "personal-bookmarks" && !this._isCustomizing)` → `this._resetView()`
- 参照: `this._isCustomizing`

## _resetView()
- 位置: L1281-1292
- 役割: ビューが存在すれば uninit し、init で作り直す。
- 触るとき: ブックマークツールバーのビューの再構築条件を変えるとき。
- 条件付き依存: `if (this._viewElt._placesView)` → `this._viewElt._placesView.uninit()`
- 条件付き依存: `if (this._viewElt)` → `this.init()`
- 参照: `this._viewElt`, `this._viewElt._placesView`

## populateManagedBookmarks()
- 位置: async L1294-1311
- 役割: 管理ブックマークのポップアップが空のときだけ、ステータスバーへの URL 表示リスナーを付けて中身を構築する。
- 触るとき: ポリシーの管理ブックマークのメニューを開いたときの中身や構築の仕方を変えるとき。
- 呼び出し先: `Services.policies.getActivePolicies()`, `XULBrowserWindow.setOverLink()`, `document.createDocumentFragment()`, `popup.addEventListener()`, `popup.appendChild()`, `popup.hasChildNodes()`, `this.addManagedBookmarks()`
- 参照: `Services.policies.getActivePolicies().ManagedBookmarks`, `event.target.link`
- XPCOM: `Services.policies`

## addManagedBookmarks()
- 位置: async L1316-1384
- 役割: 管理ブックマークの配列を再帰的にメニュー項目へ変換する。フォルダーは menu と menupopup、項目は favicon を検証して menuitem にする。URL は https を補って解析し、それでも無効なら捨てる。
- 触るとき: ポリシーの管理ブックマークの表示、URL の補正、favicon の扱いを変えるとき。
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
- 役割: 管理ブックマークのリンクを開く。javascript: URL は信頼されたリンクとして現在のタブで開き、それ以外は UI リンクとして開く。
- 触るとき: 管理ブックマークを開くときの URL 種別ごとの扱いを変えるとき。
- 呼び出し先: `/^javascript:/i.test()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `openUILink()`
- 条件付き依存: `if (/^javascript:/i.test(link))` → `openTrustedLinkIn()`
- 参照: `event.target.link`
- XPCOM: `Services.scriptSecurityManager`

## onDragStartManaged()
- 位置: L1401-1421
- 役割: 管理ブックマークのドラッグ開始時、link があれば URL・プレーンテキスト・HTML の 3 形式のデータを載せる。
- 触るとき: 管理ブックマークをドラッグしたときに渡すデータ形式を変えるとき。
- 呼び出し先: `addData()`
- 参照: `PlacesUtils.TYPE_HTML`, `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_URL`, `event.dataTransfer`, `event.target.label`, `event.target.link`, `node.title`, `node.type`, `node.uri`

## addData()
- 位置: L1413-1416
- 役割: onDragStartManaged 内の補助関数。ノードを指定の形式でラップし、dataTransfer に index 0 で設定する。
- 触るとき: ドラッグデータの形式を増やすとき。
- 呼び出し先: `PlacesUtils.wrapNode()`, `dt.mozSetDataAt()`

## button()
- 位置: L1433-1437
- 役割: CustomizableUI からブックマークボタンの DOM を取得し、以後はキャッシュする。
- 触るとき: ブックマークボタンのウィジェットの取り方を変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `widgetGroup.forWindow()`
- 参照: `this.BOOKMARK_BUTTON_ID`, `this.button`, `widgetGroup.forWindow(window).node`

## star()
- 位置: L1439-1442
- 役割: スターボタン要素を id で取得してキャッシュする。
- 触るとき: スターボタンの DOM を参照する箇所の扱いを見直すとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.STAR_ID`, `this.star`

## starBox()
- 位置: L1444-1447
- 役割: スターのボックス要素を取得してキャッシュする。
- 触るとき: スターのツールチップ文言（編集・追加）を設定する先を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.STAR_BOX_ID`, `this.starBox`

## anchor()
- 位置: L1449-1452
- 役割: ブックマーク用ページアクションのパネルアンカーを返す。
- 触るとき: ブックマーク編集パネルの表示位置を変えるとき。
- 呼び出し先: `BrowserPageActions.panelAnchorNodeForAction()`, `PageActions.actionForID()`
- 参照: `PageActions.ACTION_ID_BOOKMARK`

## stringbundleset()
- 位置: L1454-1457
- 役割: stringbundleset 要素を取得してキャッシュする。
- 触るとき: 文字列バンドル要素を参照する箇所を追うとき（このファイル内の利用箇所は要確認）。
- 呼び出し先: `document.getElementById()`
- 参照: `this.stringbundleset`

## toolbar()
- 位置: L1459-1462
- 役割: PersonalToolbar 要素を取得してキャッシュする。
- 触るとき: ブックマークツールバーの表示状態を見る箇所を追うとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.toolbar`

## status()
- 位置: L1467-1474
- 役割: スターの状態を返す。更新中なら UPDATING、starred 属性があれば STARRED、無ければ UNSTARRED。
- 触るとき: スターの状態の判定値や更新中の扱いを変えるとき。
- 呼び出し先: `this.star.hasAttribute()`
- 参照: `this.STATUS_STARRED`, `this.STATUS_UNSTARRED`, `this.STATUS_UPDATING`, `this._pendingUpdate`

## BUI_onPopupShowing()
- 位置: L1476-1517
- 役割: ブックマークボタンのポップアップ表示時、溢れやパネル内なら専用サブビューかライブラリを開き、通常時はモバイル・サイドバー・ツールバーの各項目のラベルを更新する。
- 触るとき: ブックマークボタンのドロップダウンの項目や、溢れたときの振る舞いを変えるとき。
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
- 役割: 要素の既存の l10n ID を使い、isVisible 引数を付けて表示文字列を設定する。
- 触るとき: サイドバーやツールバーの表示切替ラベルの文言を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.l10n.setAttributes()`, `element.getAttribute()`

## toggleBookmarksToolbar()
- 位置: L1525-1539
- 役割: ツールバーが折りたたみなら always、そうでなければ never を visibility 設定に保存し、CustomizableUI で切り替えて計測する。
- 触るとき: ブックマークツールバーの表示切替やその計測を変えるとき。
- 呼び出し先: `BrowserUsageTelemetry.recordToolbarVisibility()`, `CustomizableUI.setToolbarVisibility()`, `Services.prefs.setCharPref()`
- 参照: `this.toolbar.collapsed`, `this.toolbar.id`
- XPCOM: `Services.prefs`

## isOnNewTabPage()
- 位置: L1541-1574
- 役割: URI が新規タブ用の URL（about:newtab、about:home、blanktab、プライベートの about:privatebrowsing、スマートウィンドウの新規タブ）かを判定する。
- 触るとき: 新規タブページでのブックマーク表示（ツールバーの新規タブ時表示）を変えるとき。
- 呼び出し先: `AIWindow.isAIWindowNewTabPage()`, `Cu.isESModuleLoaded()`, `PrivateBrowsingUtils.isWindowPrivate()`, `newTabURLs.some()`, `this._newTabURI()`, `this._newTabURI(newTabUriString)?.equalsExceptRef()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `newTabURLs.push()`
- 参照: `AboutNewTab.newTabURL`

## _newTabURI()
- 位置: L1576-1583
- 役割: URL 文字列を nsIURI に変換し、Map でキャッシュして返す。
- 触るとき: 新規タブ URL との比較に使う変換の仕方を変えるとき。
- 呼び出し先: `this._newTabURICache.get()`
- 条件付き依存: `if (uri === undefined)` → `Services.io.newURI()`
- 条件付き依存: `if (uri === undefined)` → `this._newTabURICache.set()`
- XPCOM: `Services.io`

## buildBookmarksToolbarSubmenu()
- 位置: L1586-1651
- 役割: ツールバー表示設定（新規タブ時、常に表示、常に非表示）の 3 項目を持つラジオメニューを作り、現在の設定に checked を付ける。ショートカットは次の状態へ切り替える項目に割り当てる。
- 触るとき: ツールバーのコンテキストメニューの表示設定項目を追加・変更するとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `menu.appendChild()`, `menu.setAttribute()`, `menuItem.addEventListener()`, `menuItem.setAttribute()`, `menuItem.toggleAttribute()`, `menuItemForNextStateFromKbShortcut.setAttribute()`, `menuItems.map()`, `menuPopup.append()`, `toolbar.getAttribute()`
- 参照: `menuItem.dataset.bookmarksToolbarVisibility`, `menuItem.dataset.visibilityEnum`, `toolbar.id`

## updateEmptyToolbarMessage()
- 位置: async L1659-1710
- 役割: ツールバーに表示中の項目があるか、カスタマイズ中か、ブックマーク項目が移動したかで空メッセージの hidden を決め、必要ならブックマークの有無を確認する。
- 触るとき: ブックマークツールバーの空メッセージが出なかったり出っぱなしになったりする問題を調べるとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `document.getElementById()`, `this.toolbar.hasAttribute()`, `this.toolbar.querySelector()`
- 条件付き依存: `if (checkHasBookmarks)` → `PlacesToolbarHelper.getIsEmpty()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `bookmarksToolbarItemsPlacement?.area`, `emptyMsg.hidden`, `this._isCustomizing`

## BUI__uninitView()
- 位置: L1712-1738
- 役割: ボタン、メニューバーのブックマークメニュー、その下の特殊ビューの PlacesView を uninit し、再挿入時の不具合を防ぐ。
- 触るとき: ブックマークメニューの表示を作り直させたいとき、または再挿入で壊れる問題を追うとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (this.button._placesView)` → `this.button._placesView.uninit()`
- 条件付き依存: `if (menubar && menubar._placesView)` → `menubar._placesView.uninit()`
- 条件付き依存: `if (elem && elem._placesView)` → `elem._placesView.uninit()`
- 参照: `elem._placesView`, `menubar._placesView`, `this.button._placesView`

## BUI_customizeStart()
- 位置: L1740-1758
- 役割: このウィンドウのカスタマイズ開始時にビューを uninit し、空メッセージを更新する。表示設定が never でなければツールバーを一時的に表示する。
- 触るとき: カスタマイズモード中のブックマークツールバーの見せ方を変えるとき。
- 条件付き依存: `if (aWindow == window)` → `this._uninitView()`
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage()`
- 条件付き依存: `if (aWindow == window)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (aWindow == window)` → `setToolbarVisibility()`
- 参照: `console.error`, `this._isCustomizing`, `this.toolbar`
- XPCOM: `Services.prefs`

## BUI_widgetAdded()
- 位置: L1760-1767
- 役割: ブックマークボタンが追加されたら移動処理を行い、ブックマーク領域に追加されたら空メッセージを更新する。
- 触るとき: ウィジェットの追加に伴うブックマーク UI の更新を調整するとき。
- 条件付き依存: `if (aWidgetId == this.BOOKMARK_BUTTON_ID)` → `this._onWidgetWasMoved()`
- 条件付き依存: `if (aArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `console.error`, `this.BOOKMARK_BUTTON_ID`

## BUI_widgetRemoved()
- 位置: L1769-1776
- 役割: ブックマークボタンが外れたら移動処理を行い、ブックマーク領域から外れたら空メッセージを更新する。
- 触るとき: ウィジェットの取り外しに伴うブックマーク UI の更新を調整するとき。
- 条件付き依存: `if (aWidgetId == this.BOOKMARK_BUTTON_ID)` → `this._onWidgetWasMoved()`
- 条件付き依存: `if (aOldArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aOldArea == CustomizableUI.AREA_BOOKMARKS)` → `this.updateEmptyToolbarMessage()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `console.error`, `this.BOOKMARK_BUTTON_ID`

## BUI_widgetReset()
- 位置: L1778-1782
- 役割: ブックマークボタンがリセットされたときに移動処理を行う。
- 触るとき: ツールバーのリセット後にブックマークメニューが古いままになる問題を追うとき。
- 条件付き依存: `if (aNode == this.button)` → `this._onWidgetWasMoved()`
- 参照: `this.button`

## BUI_undoWidgetUndoMove()
- 位置: L1784-1788
- 役割: ブックマークボタンの移動を元に戻したときに移動処理を行う。
- 触るとき: 移動の取り消し操作後の表示更新を追うとき。
- 条件付き依存: `if (aNode == this.button)` → `this._onWidgetWasMoved()`
- 参照: `this.button`

## BUI_onWidgetBeforeDOMChange()
- 位置: L1790-1799
- 役割: インポートボタンの DOM を動かす前に、移動先がツールバーかどうかでボタンのクラスを切り替える。
- 触るとき: インポートボタンをツールバーへ移したときの見た目を追うとき。
- 条件付き依存: `if (aNode.id == "import-button")` → `this._updateImportButton()`
- 参照: `aNode.id`

## BUI_updateImportButton()
- 位置: L1801-1807
- 役割: ボタンがブックマークツールバー内なら bookmark-item、そうでなければ toolbarbutton-1 のクラスを付け替える。
- 触るとき: インポートボタンの見た目の分岐を変えるとき。
- 呼び出し先: `aNode.classList.toggle()`
- 参照: `this.toolbar`

## BUI_widgetWasMoved()
- 位置: L1809-1815
- 役割: カスタマイズ中でなければビューを uninit し、次のポップアップ表示で作り直させる。
- 触るとき: ボタンを移動したあとにブックマークメニューが古いままになる問題を追うとき。
- 条件付き依存: `if (!this._isCustomizing)` → `this._uninitView()`
- 参照: `this._isCustomizing`

## BUI_customizeEnd()
- 位置: L1817-1822
- 役割: カスタマイズ中フラグを下ろし、空メッセージを更新する。
- 触るとき: カスタマイズ終了後の表示更新内容を変えるとき。
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (aWindow == window)` → `this.updateEmptyToolbarMessage()`
- 参照: `console.error`, `this._isCustomizing`

## init()
- 位置: L1824-1831
- 役割: CustomizableUI のリスナーを登録し、インポートボタンのクラスを設定し、空メッセージを更新する。
- 触るとき: ブックマーク UI の起動時の初期化内容を変えるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `document.getElementById()`, `this.updateEmptyToolbarMessage()`, `this.updateEmptyToolbarMessage().catch()`
- 条件付き依存: `if (importButton)` → `this._updateImportButton()`
- 参照: `console.error`, `importButton.parentNode`

## BUI_uninit()
- 位置: L1835-1856
- 役割: ブックマークの既定メニュー項目を戻し、リスナーを外し、ビューを uninit して、保留中の更新を破棄する。
- 触るとき: ウィンドウを閉じるときの後始末を追加・変更するとき。
- 呼び出し先: `CustomizableUI.removeListener()`, `this._uninitView()`, `this.updateBookmarkPageMenuItem()`
- 条件付き依存: `if (this._hasBookmarksObserver)` → `PlacesUtils.observers.removeListener()`
- 参照: `this._hasBookmarksObserver`, `this._pendingUpdate`, `this.handlePlacesEvents`

## BUI_onLocationChange()
- 位置: L1858-1863
- 役割: 現在の URI が前回と同じなら何もせず、違えばスターの状態を更新する。
- 触るとき: ページ遷移でスターが更新されない問題を調べるとき。
- 呼び出し先: `gBrowser.currentURI.equals()`, `this.updateStarState()`
- 参照: `this._uri`

## BUI_updateStarState()
- 位置: L1865-1917
- 役割: 現在の URI のブックマーク guid を取得して _itemGuids に保存し、保留中の更新でなければスターを更新する。初回は Places のブックマーク変更の監視を登録する。guid が既にあれば new Set(...) で統合するが、この統合式は要確認。
- 触るとき: スターの状態判定や、ブックマーク変更を監視する条件を変えるとき。
- 呼び出し先: `PlacesUtils.bookmarks .fetch()`, `PlacesUtils.bookmarks .fetch({ url: this._uri }, b => guids.add(b.guid), { concurrent: true }) .catch()`, `guids.add()`, `this._itemGuids.clear()`, `this._updateStar()`
- 条件付き依存: `if (!this._hasBookmarksObserver)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._hasBookmarksObserver)` → `PlacesUtils.observers.addListener()`
- 条件付き依存: `if (!this._hasBookmarksObserver)` → `console.error()`
- 参照: `b.guid`, `console.error`, `gBrowser.currentURI`, `this._hasBookmarksObserver`, `this._itemGuids`, `this._itemGuids.size`, `this._pendingUpdate`, `this._uri`, `this.handlePlacesEvents`

## BUI__updateStar()
- 位置: L1919-1963
- 役割: スターと関連要素に starred 属性を付け、スターのツールチップを更新し、ページ操作メニューを更新して bookmark-icon-updated を通知する。
- 触るとき: スターの見た目や通知先を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `Services.obs.notifyObservers()`, `ShortcutUtils.prettifyShortcut()`, `document.getElementById()`, `document.l10n.setAttributes()`, `element.toggleAttribute()`, `this.updateBookmarkPageMenuItem()`
- 条件付き依存: `if (!this.starBox)` → `this.updateBookmarkPageMenuItem()`
- 参照: `this.BOOKMARK_BUTTON_SHORTCUT`, `this._itemGuids.size`, `this.star`, `this.starBox`
- XPCOM: `Services.obs`

## updateBookmarkPageMenuItem()
- 位置: L1972-2050
- 役割: 「ブックマークに追加」か「ブックマークを編集」の文言を、メニューバー、パネル、コンテキストメニュー、ページアクションに、ブックマーク状態に応じて設定する。
- 触るとき: ブックマーク済みかどうかでメニューの文言を変えるとき。
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
- 役割: ブックマークメニュー表示時に、同期促進の状態に応じてリモートタブの促進項目を設定し、モバイルブックマークの表示を更新する。
- 触るとき: ブックマークメニューを開いたときの同期促進の出し方を変えるとき。
- 呼び出し先: `document.getElementById()`, `gSync.getSyncPromoState()`
- 参照: `document.getElementById("menu_mobileBookmarks").hidden`, `event.target.id`, `remoteTabsPromo.dataset.action`, `remoteTabsPromo.hidden`

## showSubView()
- 位置: L2068-2070
- 役割: _showSubView を anchor 指定で呼ぶ公開の入口。
- 触るとき: ブックマークのサブビューを外部から開く呼び出し元を追うとき。
- 呼び出し先: `this._showSubView()`

## _showSubView()
- 位置: L2072-2082
- 役割: ブックマークサブビューの ViewShowing と ViewHiding のリスナーを登録し、アンカーに closemenu=none を付け、表示ラベルを更新してから PanelUI でサブビューを開く。
- 触るとき: ブックマークのサブビューの表示処理を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `anchor.setAttribute()`, `document.getElementById()`, `this.updateLabel()`, `view.addEventListener()`
- 参照: `this.BOOKMARK_BUTTON_ID`, `this.toolbar.collapsed`

## BUI_onCommand()
- 位置: L2084-2102
- 役割: ボタン自身の command のみ処理する。パネル内ならサブビューを開き、溢れ中なら閉じるメニューの属性を外してから onStarCommand を呼ぶ。
- 触るとき: ブックマークボタンのクリックで、サブビューとスター処理のどちらに進むかを変えるとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(this.BOOKMARK_BUTTON_ID).forWindow()`, `this.button.getAttribute()`, `this.onStarCommand()`
- 条件付き依存: `if (this.button.getAttribute("cui-areatype") == CustomizableUI.TYPE_PANEL)` → `this._showSubView()`
- 条件付き依存: `if (widget.overflowed)` → `widget.node.removeAttribute()`
- 参照: `CustomizableUI.TYPE_PANEL`, `aEvent.currentTarget`, `aEvent.target`, `this.BOOKMARK_BUTTON_ID`, `widget.overflowed`

## onStarCommand()
- 位置: L2104-2112
- 役割: 保留中の更新が無く、左クリックか click 以外のイベントなら PlacesCommandHook.bookmarkPage を呼ぶ。
- 触るとき: スターを押したときに、ブックマーク処理を始める条件を変えるとき。
- 条件付き依存: `if ( !this._pendingUpdate && (aEvent.type != "click" || aEvent.button == 0) )` → `PlacesCommandHook.bookmarkPage()`
- 参照: `aEvent.button`, `aEvent.type`, `this._pendingUpdate`

## BUI_handleEvent()
- 位置: L2114-2130
- 役割: ViewShowing と ViewHiding を対応ハンドラに振り分け、パネル内の command（検索とツールバー表示切替）を処理する。
- 触るとき: ブックマークサブビューの項目を追加したり操作を振り分けたりするとき。
- 呼び出し先: `this.onPanelMenuViewHiding()`, `this.onPanelMenuViewShowing()`
- 条件付き依存: `if (aEvent.target.id == "panelMenu_searchBookmarks")` → `PlacesCommandHook.searchBookmarks()`
- 条件付き依存: `if (aEvent.target.id == "panelMenu_viewBookmarksToolbar")` → `this.toggleBookmarksToolbar()`
- 参照: `aEvent.target.id`, `aEvent.type`

## BUI_onViewShowing()
- 位置: L2132-2157
- 役割: パネル内の toolbarbutton にショートカットを付け、追加日の新しい順に最大 42 件のブックマーク一覧を PlacesPanelview として作る。
- 触るとき: ブックマークのサブビューに出す件数や並びを変えるとき。
- 呼び出し先: `CustomizableUI.addShortcut()`, `document.getElementById()`, `panelview.addEventListener()`, `panelview.getElementsByTagName()`, `panelview.removeEventListener()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_BOOKMARKS`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATEADDED_DESCENDING`, `aEvent.target`, `staticButtons.length`, `this._panelMenuView`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## BUI_onViewHiding()
- 位置: L2159-2165
- 役割: ブックマーク一覧ビューを uninit して破棄し、ViewHiding と command のリスナーを外す。
- 触るとき: サブビューを閉じたあとの後始末に問題があるとき。
- 呼び出し先: `panelview.removeEventListener()`, `this._panelMenuView.uninit()`
- 参照: `aEvent.target`, `this._panelMenuView`

## handlePlacesEvents()
- 位置: L2167-2281
- 役割: Places の bookmark-added、removed、moved、url-changed を受け、このページのスター状態、既定の保存先、ツールバーの計測、その他ブックマークとツールバーの表示更新を行う。
- 触るとき: ブックマークの追加や削除、移動によってスターやツールバー表示が更新される条件を変えるとき。
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
- 役割: ブックマークボタンがこのウィンドウで溢れたら、ビューを uninit して次のポップアップ表示で作り直させる。
- 触るとき: ブックマークボタンが溢れたときの表示を追うとき。
- 呼び出し先: `this._uninitView()`
- 参照: `aNode.documentGlobal`, `aNode.id`, `this.BOOKMARK_BUTTON_ID`

## maybeShowOtherBookmarksFolder()
- 位置: async L2294-2332
- 役割: 未分類のブックマークが 1 件以上あれば「その他のブックマーク」ボタンを作るか表示し、無ければ隠す。設定や配置が外れている場合は隠して終える。
- 触るとき: その他のブックマークの表示条件や非表示処理を変えるとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `PlacesUtils.bookmarks.fetch()`, `document.getElementById()`
- 条件付き依存: `if (!otherBookmarks)` → `PlacesUtils.getFolderContents()`
- 条件付き依存: `if (!otherBookmarks)` → `this.buildOtherBookmarksFolder()`
- 参照: `(await PlacesUtils.bookmarks.fetch(unfiledGuid)) .childCount`, `CustomizableUI.AREA_BOOKMARKS`, `PlacesUtils.bookmarks.unfiledGuid`, `PlacesUtils.getFolderContents(unfiledGuid).root`, `otherBookmarks.hidden`, `placement?.area`, `this._showOtherBookmarksInstance`, `toolbar?._placesView`

## buildShowOtherBookmarksMenuItem()
- 位置: L2334-2366
- 役割: 「その他のブックマークを表示」のチェック式メニュー項目を作る。未分類に項目が入るまで無効にし、クリックで設定を反転させる。
- 触るとき: ツールバーの右クリックメニューのその他ブックマーク項目を変えるとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `PlacesUtils.bookmarks.fetch()`, `PlacesUtils.bookmarks.fetch(PlacesUtils.bookmarks.unfiledGuid).then()`, `Services.prefs.setBoolPref()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `menuItem.addEventListener()`, `menuItem.setAttribute()`, `menuItem.toggleAttribute()`
- 参照: `PlacesUtils.bookmarks.unfiledGuid`, `bm.childCount`, `menuItem.disabled`
- XPCOM: `Services.prefs`

## buildOtherBookmarksFolder()
- 位置: L2368-2405
- 役割: 未分類フォルダーのツールバーボタンと、placespopup 属性付きのポップアップを作り、シェブロンの後ろに挿入して、ビューに参照を保存する。
- 触るとき: その他のブックマークのボタン構造やビューの参照を変えるとき。
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `PlacesUtils.asContainer()`, `chevronButton.parentNode.append()`, `document .getElementById()`, `document .getElementById("PlacesToolbar") ._placesView._onOtherBookmarksPopupShowing()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `otherBookmarksButton.addEventListener()`, `otherBookmarksButton.appendChild()`, `otherBookmarksButton.setAttribute()`, `otherBookmarksPopup.classList.add()`, `otherBookmarksPopup.setAttribute()`, `otherBookmarksPopup.toggleAttribute()`
- 参照: `otherBookmarksButton._placesNode`, `otherBookmarksButton.className`, `otherBookmarksButton.hidden`, `otherBookmarksButton.id`, `otherBookmarksPopup._placesNode`, `otherBookmarksPopup.id`, `placesToolbar._placesView._otherBookmarks`, `placesToolbar._placesView._otherBookmarksPopup`
