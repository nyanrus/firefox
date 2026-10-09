# browser/components/places/PlacesUIUtils.sys.mjs

source: browser/components/places/PlacesUIUtils.sys.mjs
source-hash: 16b4b7bf0e18fba11ea3f7b91fd680a831c2fd83
lines: 2121

## <module>
- 役割: ブックマークと履歴の Places UI で共通に使うヘルパー群。ブックマーク編集状態 (BookmarkState)、ダイアログ表示、コンテキストメニュー、ドラッグ&ドロップ、サイドバーのクリック処理をまとめる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `["toolbar", "menu", "unfiled"].includes()`, `lazy.PlacesUtils.bookmarks .fetch()`, `lazy.PlacesUtils.bookmarks .fetch({ guid: prefValue }) .then()`

## BookmarkState.constructor()
- 位置: L61-93
- 役割: info から元の状態 (_originalState) を組み立て、変更を溜める _newState を空で作る。タグは区切り文字で分割する。
- 触るとき: ブックマーク編集ダイアログに渡す初期値の扱い (タグの分割、タグコンテナの判定、autosave の既定値 false) を変えるとき。
- 呼び出し先: `info.uris?.map()`, `tags .trim()`, `tags .trim() .split()`, `tags .trim() .split(/\s*,\s*/) .filter()`
- 参照: `info.isTag`, `info.itemGuid`, `info.parentGuid`, `info.postData`, `info.tag`, `info.title`, `info.uri?.spec`, `tag.length`, `this._autosave`, `this._bulkTaggingUrls`, `this._children`, `this._guid`, `this._isFolder`, `this._isTagContainer`, `this._newState`, `this._originalState`, `this._postData`, `uri.spec`

## BookmarkState._titleChanged()
- 位置: async L101-104
- 役割: 編集されたタイトルを _newState に記録し、autosave が有効なら save を呼ぶ。
- 触るとき: タイトル欄の入力がいつ保存されるかを変えるとき、タイトルが保存されない問題を調べるとき。
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.title`

## BookmarkState._locationChanged()
- 位置: async L112-115
- 役割: 編集された URL を _newState.uri に記録し、autosave が有効なら保存する。
- 触るとき: URL 欄の変更が保存に反映されないとき、URL 編集の経路を追うとき。
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.uri`

## BookmarkState._tagsChanged()
- 位置: async L123-126
- 役割: 編集されたタグ文字列を _newState.tags に記録し、autosave が有効なら保存する。
- 触るとき: タグ欄の変更の保存タイミングや、タグ差分の計算に入る前の値を変えるとき。
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.tags`

## BookmarkState._keywordChanged()
- 位置: async L134-137
- 役割: キーワードの変更を _newState.keyword に記録し、autosave が有効なら保存する。
- 触るとき: キーワード欄の変更が保存されるタイミングを変えるとき。
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.keyword`

## BookmarkState._parentGuidChanged()
- 位置: async L145-148
- 役割: 変更後の親 guid を _newState.parentGuid に記録し、autosave が有効なら保存する。
- 触るとき: ダイアログのフォルダー選択で親を変えたときの保存経路を調べるとき。
- 呼び出し先: `this._maybeSave()`
- 参照: `this._newState.parentGuid`

## BookmarkState._maybeSave()
- 位置: async L153-157
- 役割: autosave が有効なときだけ save() を await する。
- 触るとき: 編集内容を即時保存する仕組みを変えるとき。
- 条件付き依存: `if (this._autosave)` → `this.save()`
- 参照: `this._autosave`

## BookmarkState._createBookmark()
- 位置: async L164-189
- 役割: NewBookmark のトランザクションを作り、キーワードがあれば続けて EditKeyword を積んで batch 実行し、作成された guid を返す。
- 触るとき: 新規ブックマークの作成時に反映される項目 (タイトル、URL、タグ、キーワード) を変えるとき。
- 呼び出し先: `lazy.PlacesTransactions.NewBookmark()`, `lazy.PlacesTransactions.batch()`
- 条件付き依存: `if (this._newState.keyword)` → `transactions.push()`
- 条件付き依存: `if (this._newState.keyword)` → `lazy.PlacesTransactions.EditKeyword()`
- 参照: `this._guid`, `this._newState.keyword`, `this._newState.tags`, `this._newState.title`, `this._newState.uri`, `this._originalState.index`, `this._originalState.title`, `this._originalState.uri`, `this._postData`, `this.parentGuid`

## BookmarkState._createFolder()
- 位置: async L196-222
- 役割: NewFolder のトランザクションを作り、一括タグ付け用の URL があれば Tag/Untag を追加して batch 実行し、作成したフォルダーの guid を返す。
- 触るとき: 複数ページをまとめてフォルダーに入れる際の子項目やタグの扱いを変えるとき。
- 呼び出し先: `lazy.PlacesTransactions.NewFolder()`, `lazy.PlacesTransactions.batch()`
- 条件付き依存: `if (this._bulkTaggingUrls)` → `this._appendTagsTransactions()`
- 参照: `this._bulkTaggingUrls`, `this._children`, `this._guid`, `this._newState.tags`, `this._newState.title`, `this._originalState.index`, `this._originalState.tags`, `this._originalState.title`, `this.parentGuid`

## BookmarkState.parentGuid()
- 位置: L224-226
- 役割: 変更後の親 guid があればそれを、なければ元の親 guid を返す。
- 触るとき: 親フォルダーの変更が保存先に反映されない問題を調べるとき。
- 参照: `this._newState.parentGuid`, `this._originalState.parentGuid`

## BookmarkState.save()
- 位置: async L233-310
- 役割: 未保存なら新規作成、既存なら変更分 (URL、タイトル、タグ、キーワード、親) をトランザクションにして batch 実行し、_originalState を更新する。タグコンテナはタグのリネームとして扱う。
- 触るとき: ブックマーク編集の保存で実行される操作の種類や順序を変えるとき、保存後も古い状態が残る問題を調べるとき。
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
- 役割: 新旧のタグを比べ、追加分は Tag、削除分は Untag のトランザクションを transactions に積む。
- 触るとき: タグ差分の計算や、タグを付ける対象 URL の指定を変えるとき。
- 呼び出し先: `newTags.filter()`, `newTags.includes()`, `originalTags.filter()`, `originalTags.includes()`
- 条件付き依存: `if (addedTags.length)` → `transactions.push()`
- 条件付き依存: `if (addedTags.length)` → `lazy.PlacesTransactions.Tag()`
- 条件付き依存: `if (removedTags.length)` → `transactions.push()`
- 条件付き依存: `if (removedTags.length)` → `lazy.PlacesTransactions.Untag()`
- 参照: `addedTags.length`, `removedTags.length`

## obfuscateUrlForXulStore()
- 位置: L376-384
- 役割: place: URL の後ろを md5 でハッシュ化し、xulstore のキーに使える「place:」形式の文字列を返す。place: 以外を渡すと例外になる。
- 触るとき: xulstore に保存するキーの形式を変えるとき、place: 以外の URL を渡して例外になる原因を調べるとき。
- 呼び出し先: `lazy.PlacesUtils.md5()`, `url.indexOf()`, `url.startsWith()`, `url.substring()`

## showBookmarkDialog()
- 位置: async L399-424
- 役割: 新しい Deferred を作り、ブックマークダイアログを gDialogBox または openDialog で開く。閉じた後に bookmarkState があれば save して guid を返し、なければ undefined を返す。
- 触るとき: ブックマーク追加・編集ダイアログの表示方法や、閉じた後の保存と結果の受け渡しを変えるとき。
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
- 役割: URIList が複数ならフォルダー追加、1件なら単一ブックマークの情報を作り、showBookmarkDialog で開く。空なら何もしない。
- 触るとき: 複数タブをまとめてブックマークする際の既定の振る舞いを変えるとき。
- 呼び出し先: `PlacesUIUtils.showBookmarkDialog()`
- 参照: `URIList.length`, `URIList[0].title`, `URIList[0].uri`, `bookmarkDialogInfo.URIList`, `bookmarkDialogInfo.title`, `bookmarkDialogInfo.type`, `bookmarkDialogInfo.uri`

## PUIU_getViewForNode()
- 位置: L462-498
- 役割: DOM ノードから祖先をたどり、Places のビュー (_placesView や places-tree) を返す。見つからなければ null。
- 触るとき: コンテキストメニューや操作元からどの Places ビューを対象にするかを決める箇所を変えるとき。
- 呼び出し先: `Cu.isDeadWrapper()`, `Element.isInstance()`, `node.getAttribute()`
- 参照: `node._placesNode`, `node._placesView`, `node.localName`, `node.menupopup._placesView`, `node.parentNode`

## getControllerForCommand()
- 位置: L507-527
- 役割: 直前のコンテキストメニュー元が managed-bookmarks なら管理用コントローラー、そうでなければビューかフォーカス中の command dispatcher からコマンドのコントローラーを返す。
- 触るとき: メニューのコマンドがどのコントローラーで処理されるかを調べるとき、管理ブックマークのコマンドが効かない問題を調べるとき。
- 呼び出し先: `win.top.document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if (popupNode)` → `popupNode.closest()`
- 条件付き依存: `if (popupNode)` → `this.getViewForNode()`
- 条件付き依存: `if (view && view._contextMenuShown)` → `view.controllers.getControllerForCommand()`
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`, `this.managedBookmarksController`, `view._contextMenuShown`

## updateCommands()
- 位置: L534-559
- 役割: 対象の Places コマンドごとに isCommandEnabled を調べ、win.goSetCommandEnabled で有効・無効を反映する。
- 触るとき: Places 系コマンドが有効にならない、または有効になりすぎる不具合を調べるとき、コマンドを追加するとき。
- 呼び出し先: `controller.isCommandEnabled()`, `this.getControllerForCommand()`, `win.goSetCommandEnabled()`

## doCommand()
- 位置: L567-573
- 役割: 現在のコントローラーで対象コマンドが有効なら、lastContextMenuCommand に記録したうえで実行する。
- 触るとき: メニューやショートカットから Places コマンドを実行する経路を変えるとき。
- 呼び出し先: `controller.isCommandEnabled()`, `this.getControllerForCommand()`
- 条件付き依存: `if (controller && controller.isCommandEnabled(command))` → `controller.doCommand()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`

## PUIU_markPageAsTyped()
- 位置: L586-590
- 役割: URL を getFixupURIInfo で補正してから、履歴に入力された遷移 (TRANSITION_TYPED) として記録する。
- 触るとき: URL バーや履歴メニューからの訪問を typed として残す挙動を調べるとき。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `lazy.PlacesUtils.history.markPageAsTyped()`
- 参照: `Services.uriFixup.getFixupURIInfo(aURL).preferredURI`
- XPCOM: `Services.uriFixup`

## PUIU_markPageAsFollowedBookmark()
- 位置: L602-606
- 役割: URL の次の訪問を、ブックマーク経由の遷移 (TRANSITION_BOOKMARK) として履歴に記録させる。
- 触るとき: ブックマーク経由の訪問が履歴上どう分類されるかを変えるとき。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `lazy.PlacesUtils.history.markPageAsFollowedBookmark()`
- 参照: `Services.uriFixup.getFixupURIInfo(aURL).preferredURI`
- XPCOM: `Services.uriFixup`

## PUIU_markPageAsFollowedLink()
- 位置: L617-621
- 役割: URL のフレーム内の訪問を TRANSITION_FRAMED_LINK として記録させ、ユーザー操作による訪問と自動訪問を区別できるようにする。
- 触るとき: フレーム内の訪問の分類を変えるとき、自動訪問が除外される理由を調べるとき。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `lazy.PlacesUtils.history.markPageAsFollowedLink()`
- 参照: `Services.uriFixup.getFixupURIInfo(aURL).preferredURI`
- XPCOM: `Services.uriFixup`

## setCharsetForPage()
- 位置: async L632-647
- 役割: ページの文字コードを履歴に保存する。プライベートウィンドウでは何もせず、utf-8 は null にして既存の設定を消す。
- 触るとき: ブックマークの文字コード設定の保存や、プライベートウィンドウでの扱いを変えるとき。
- 呼び出し先: `charset.toLowerCase()`, `lazy.PlacesUtils.history.update()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `lazy.PlacesUtils.CHARSET_ANNO`

## checkURLSecurity()
- 位置: L659-675
- 役割: ブックマークなら常に許可し、それ以外で javascript: か data: の URL なら警告を出して拒否する。
- 触るとき: 履歴やライブラリから危険な URL を開く前の検査を変えるとき、ブックマーク済みの javascript: が開ける理由を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.nodeIsBookmark()`, `uri.schemeIs()`
- 条件付き依存: `if (uri.schemeIs("javascript") || uri.schemeIs("data"))` → `PlacesUIUtils.promptLocalization.formatValuesSync()`
- 条件付き依存: `if (uri.schemeIs("javascript") || uri.schemeIs("data"))` → `Services.prompt.alert()`
- 参照: `aURINode.uri`
- XPCOM: `Services.io` / `Services.prompt`

## canUserRemove()
- 位置: L685-714
- 役割: 親がクエリか読み取り専用フォルダーかを見て、ノードが削除できるかを返す。ルートや左ペインの仮想項目は削除不可。
- 触るとき: 「削除」メニューが出ない・出すぎるといった問題を調べるとき、削除不可の項目の条件を変えるとき。
- 呼び出し先: `lazy.PlacesUtils.nodeIsQuery()`, `this.isFolderReadOnly()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsQuery(parentNode))` → `lazy.PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsFolderOrShortcut(aNode))` → `lazy.PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsFolderOrShortcut(aNode))` → `lazy.PlacesUtils.isRootItem()`
- 条件付き依存: `if (!(lazy.PlacesUtils.nodeIsFolderOrShortcut(aNode)))` → `lazy.PlacesUtils.isVirtualLeftPaneItem()`
- 参照: `aNode.bookmarkGuid`, `aNode.itemId`, `aNode.parent`

## isFolderReadOnly()
- 位置: L734-746
- 役割: フォルダーノードの guid が Places のルート (rootGuid) かどうかを返す。フォルダーやショートカット以外を渡すと例外を投げる。
- 触るとき: 読み取り専用フォルダーの定義を変えるとき、ルートに対する操作が拒否される理由を調べるとき。
- 呼び出し先: `lazy.PlacesUtils.getConcreteItemGuid()`, `lazy.PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `lazy.PlacesUtils.bookmarks.rootGuid`

## openTabset()
- 位置: L757-829
- 役割: 渡された URL 群を、ブラウザーウィンドウが無ければ新規ウィンドウで、あれば loadTabs で新規タブとして開く。非プライベート時は遷移種別も記録する。
- 触るとき: ブックマークや履歴から複数タブで開く挙動や、プライベートウィンドウでの扱いを変えるとき。
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
- 役割: 容器ノードまたは選択ノードから URL を集め、confirmOpenInTabs で確認したうえで updateTelemetry を呼び、openTabset で開く。
- 触るとき: 「すべてをタブで開く」や複数選択をタブで開くときの確認や計測を変えるとき。
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
- 役割: イベントの修飾キーから開き方 (where) を決める。ブックマークを tab で開く設定なら、現在のタブを tab に変え、空のタブなら current に戻してから _openNodeIn に渡す。
- 触るとき: Enter やクリックでノードを開く先 (現在のタブ、新しいタブ等) の判定を変えるとき。
- 呼び出し先: `lazy.BrowserUtils.whereToOpenLink()`, `lazy.PlacesUtils.nodeIsBookmark()`, `this._openNodeIn()`
- 条件付き依存: `if (this.loadBookmarksInTabs && lazy.PlacesUtils.nodeIsBookmark(aNode))` → `aNode.uri.startsWith()`
- 条件付き依存: `if (this.loadBookmarksInTabs && lazy.PlacesUtils.nodeIsBookmark(aNode))` → `getBrowserWindow()`
- 参照: `aEvent.target.documentGlobal`, `browserWindow?.gBrowser.selectedTab.isEmpty`, `this.loadBookmarksInTabs`

## PUIU_openNodeIn()
- 位置: L910-913
- 役割: ビューのウィンドウを求め、指定の開き方とプライベートの指定を付けて _openNodeIn に渡す。
- 触るとき: 呼び出し元から指定の場所でノードを開く経路を変えるとき。
- 呼び出し先: `this._openNodeIn()`
- 参照: `aView.ownerWindow`

## PUIU__openNodeIn()
- 位置: L915-969
- 役割: 安全性と URI 判定を通ったノードについて、履歴の遷移種別を記録してから openTrustedLinkIn で開き、updateTelemetry を呼ぶ。
- 触るとき: ノードを開く最終段階 (バックグラウンド設定、コンテナ、計測) を変えるとき。
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
- 役割: ブックマーク由来 (javascript: 以外) のタブが作られたとき、auto_bookmark の遷移データを設定するコールバックを作る。
- 触るとき: ブックマークから開いたタブの遷移種別の計測を変えるとき。
- 呼び出し先: `lazy.WebNavigationManager.setRecentTabTransitionData()`

## isURILike()
- 位置: L979-984
- 役割: 結果ノードなら nodeIsURI で、DOM 要素なら uri 属性の有無で、URI を表すかを判定する。
- 触るとき: 開けるノードかどうかの判定を変えるとき。
- 条件付き依存: `if (aNode instanceof Ci.nsINavHistoryResultNode)` → `lazy.PlacesUtils.nodeIsURI()`
- 参照: `Ci.nsINavHistoryResultNode`, `aNode.uri`
- XPCOM: [`nsINavHistoryResultNode`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## guessUrlSchemeForUI()
- 位置: L994-996
- 役割: 文字列の最初のコロンより前をスキームとして返す簡易な判定。nsIURI を使わないので UI 用途に限る。
- 触るとき: UI 表示用の簡易なスキーム判定が必要なとき。
- 呼び出し先: `href.indexOf()`, `href.substr()`

## PUIU_getBestTitle()
- 位置: L998-1008
- 役割: ノードのタイトルを返す。空で URI のノードなら getBestTitleForUri で作り、それも無ければ places-no-title の文言を返す。
- 触るとき: ツリーやメニューに表示する名前が空になる問題を調べるとき。
- 呼び出し先: `lazy.PlacesUtils.nodeIsURI()`, `this.promptLocalization.formatValueSync()`
- 条件付き依存: `if (!aNode.title && lazy.PlacesUtils.nodeIsURI(aNode))` → `PlacesUIUtils.getBestTitleForUri()`
- 参照: `aNode.title`, `aNode.uri`

## getBestTitleForUri()
- 位置: L1020-1039
- 役割: URI のホストとファイル名 (ない場合は path と query) からタイトル文字列を作る。解析に失敗したら空文字を返す。
- 触るとき: タイトルの無いブックマークの表示名の形式を変えるとき、doNotCutTitle による省略の挙動を確認するとき。
- 呼び出し先: `Services.io.newURI()`, `parsedURI.QueryInterface()`
- 参照: `Ci.nsIURL`, `Services.locale.ellipsis`, `parsedURI.QueryInterface(Ci.nsIURL).fileName`, `parsedURI.host`, `parsedURI.pathQueryRef`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md) / `Services.io` / `Services.locale`

## shouldShowTabsFromOtherComputersMenuitem()
- 位置: L1041-1046
- 役割: Sync (Weave) が設定済みで、初回同期が notReady でないかを返す。
- 触るとき: 「他のデバイスのタブ」メニュー項目を出す条件を変えるとき。
- 呼び出し先: `lazy.Weave.Status.checkSetup()`, `lazy.Weave.Svc.PrefBranch.getCharPref()`
- 参照: `lazy.CLIENT_NOT_CONFIGURED`

## promiseNodeLikeFromFetchInfo()
- 位置: async L1061-1096
- 役割: Bookmarks.fetch の結果から、編集オーバーレイに渡せる読み取り専用のノード風オブジェクトを作る。セパレーターは例外になる。
- 触るとき: ノードを持たない呼び出し元から編集ダイアログを開く経路の項目情報を変えるとき。
- 呼び出し先: `Object.freeze()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `aFetchInfo.guid`, `aFetchInfo.parentGuid`, `aFetchInfo.title`, `aFetchInfo.type`, `aFetchInfo.url`, `aFetchInfo.url.href`, `lazy.PlacesUtils.bookmarks.TYPE_SEPARATOR`
- XPCOM: [`nsINavHistoryResultNode`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## type()
- 位置: L1076-1090
- 役割: promiseNodeLikeFromFetchInfo が返すオブジェクトの type getter。フォルダーならフォルダー種別、URL 付きなら URI 種別を返す。空の URL や place: の URL は例外にする。
- 触るとき: 項目の種別判定の条件を変えるとき、place: の項目で例外が出る理由を調べるとき。
- 呼び出し先: `/^place:/.test()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `aFetchInfo.type`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `this.uri`, `this.uri.length`
- XPCOM: [`nsINavHistoryResultNode`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## parent()
- 位置: L1092-1094
- 役割: promiseNodeLikeFromFetchInfo が返すオブジェクトの parent getter。親フォルダーの guid と種別を持つオブジェクトを返す。
- 触るとき: 編集ダイアログが親フォルダーを参照する箇所の挙動を変えるとき。

## batchUpdatesForNode()
- 位置: async L1112-1128
- 役割: 変更件数が閾値を超えるときだけ結果ノードのバッチ更新を開始・終了し、渡された関数の戻り値をそのまま返す。
- 触るとき: 大量の項目変更時の描画負荷を抑える閾値や、バッチ更新の範囲を変えるとき。
- 呼び出し先: `functionToWrap()`
- 条件付き依存: `if (!resultNode)` → `functionToWrap()`
- 条件付き依存: `if (itemsBeingChanged > ITEM_CHANGED_BATCH_NOTIFICATION_THRESHOLD)` → `resultNode.onBeginUpdateBatch()`
- 条件付き依存: `if (itemsBeingChanged > ITEM_CHANGED_BATCH_NOTIFICATION_THRESHOLD)` → `resultNode.onEndUpdateBatch()`

## handleTransferItems()
- 位置: async L1146-1181
- 役割: ドロップや貼り付けの項目から、タグ先ならタグ付けを、それ以外なら getTransactionsForTransferItems で移動・コピーを作り、バッチ実行して guid を返す。
- 触るとき: ドラッグ&ドロップや貼り付けの結果 (移動かコピーか、選択される guid) を変えるとき。
- 呼び出し先: `getResultForBatching()`, `guidsToSelect.flat()`, `lazy.PlacesTransactions.batch()`, `this.batchUpdatesForNode()`
- 条件付き依存: `if (insertionPoint.isTag)` → `items.filter(item => "uri" in item).map()`
- 条件付き依存: `if (insertionPoint.isTag)` → `items.filter()`
- 条件付き依存: `if (insertionPoint.isTag)` → `lazy.PlacesTransactions.Tag()`
- 条件付き依存: `if (!(insertionPoint.isTag))` → `insertionPoint.getIndex()`
- 条件付き依存: `if (!(insertionPoint.isTag))` → `getTransactionsForTransferItems()`
- 参照: `insertionPoint.guid`, `insertionPoint.isTag`, `insertionPoint.tagName`, `item.uri`, `items.length`, `transactions.length`, `urls.length`

## onSidebarTreeClick()
- 位置: L1183-1234
- 役割: サイドバーのクリックを、ボタンと修飾キー、アイコン左の余白 (ガター) から解釈し、フォルダーの開閉、複数タブで開く、1件開くのいずれかに振り分ける。
- 触るとき: サイドバーのクリック動作を変えるとき、ガター判定や中クリックの扱いを調べるとき。
- 呼び出し先: `lazy.PlacesUtils.hasChildURIs()`, `tree.getCellAt()`, `tree.getCoordsForCellItem()`, `tree.view.isContainer()`, `tree.view.nodeForTreeIndex()`, `win.getComputedStyle()`
- 条件付き依存: `if (event.button == 0 && isContainer && !openInTabs)` → `tree.view.toggleOpenState()`
- 条件付き依存: `if ( !mouseInGutter && openInTabs && event.originalTarget.localName == "treechildren" )` → `tree.view.selection.select()`
- 条件付き依存: `if ( !mouseInGutter && openInTabs && event.originalTarget.localName == "treechildren" )` → `this.openMultipleLinksInTabs()`
- 条件付き依存: `if ( !mouseInGutter && !isContainer && event.originalTarget.localName == "treechildren" )` → `tree.view.selection.select()`
- 条件付き依存: `if ( !mouseInGutter && !isContainer && event.originalTarget.localName == "treechildren" )` → `this.openNodeWithEvent()`
- 参照: `AppConstants.platform`, `cell.childElt`, `cell.col`, `cell.row`, `event.button`, `event.clientX`, `event.clientY`, `event.ctrlKey`, `event.metaKey`, `event.originalTarget.localName`, `event.shiftKey`, `event.target.parentNode`, `rect.x`, `tree.documentGlobal`, `tree.selectedNode`, `win.getComputedStyle(tree).direction`

## onSidebarTreeKeyPress()
- 位置: L1236-1243
- 役割: 選択中のノードがあるときに Enter が押されたら、openNodeWithEvent で開く。
- 触るとき: キーボードでのサイドバー項目の開き方を変えるとき。
- 条件付き依存: `if (event.keyCode == event.DOM_VK_RETURN)` → `PlacesUIUtils.openNodeWithEvent()`
- 参照: `event.DOM_VK_RETURN`, `event.keyCode`, `event.target.selectedNode`

## onSidebarTreeMouseMove()
- 位置: L1252-1272
- 役割: マウス下が URI のノードなら、その URL を setMouseoverURL でステータスに出し、それ以外では空にする。
- 触るとき: ホバー時のリンク先表示の挙動を変えるとき、前のリンク先が残る問題を調べるとき。
- 呼び出し先: `this.setMouseoverURL()`, `tree.getCellAt()`
- 条件付き依存: `if (cell.row != -1)` → `tree.view.nodeForTreeIndex()`
- 条件付き依存: `if (cell.row != -1)` → `lazy.PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (lazy.PlacesUtils.nodeIsURI(node))` → `this.setMouseoverURL()`
- 参照: `cell.row`, `event.clientX`, `event.clientY`, `event.target`, `node.uri`, `tree.documentGlobal`, `treechildren.localName`, `treechildren.parentNode`

## setMouseoverURL()
- 位置: L1274-1281
- 役割: ウィンドウの XULBrowserWindow があれば setOverLink で URL を表示する。ウィンドウ閉鎖中など無い場合は何もしない。
- 触るとき: ステータスバーのリンク表示が残る不具合を調べるとき。
- 条件付き依存: `if (win.top.XULBrowserWindow)` → `win.top.XULBrowserWindow.setOverLink()`
- 参照: `win.top.XULBrowserWindow`

## maybeToggleBookmarkToolbarVisibility()
- 位置: async L1294-1331
- 役割: ブックマークツールバーの collapsed が未保存なら、カスタマイズ済みか項目数が 3 件を超えるとき表示を戻す通知を出す。aForceVisible なら常に表示する。
- 触るとき: 初回起動などでブックマークツールバーを自動表示する条件 (NUM_TOOLBAR_BOOKMARKS_TO_UNHIDE など) を変えるとき。
- 呼び出し先: `xulStore.hasValue()`
- 条件付き依存: `if ( aForceVisible || !xulStore.hasValue(BROWSER_DOCURL, "PersonalToolbar", "collapsed") )` → `xulStore.hasValue()`
- 条件付き依存: `if (aForceVisible || toolbarIsCustomized)` → `uncollapseToolbar()`
- 条件付き依存: `if ( aForceVisible || !xulStore.hasValue(BROWSER_DOCURL, "PersonalToolbar", "collapsed") )` → `lazy.PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if (numBookmarksOnToolbar > this.NUM_TOOLBAR_BOOKMARKS_TO_UNHIDE)` → `uncollapseToolbar()`
- 参照: `( await lazy.PlacesUtils.bookmarks.fetch( lazy.PlacesUtils.bookmarks.toolbarGuid ) ).childCount`, `AppConstants.BROWSER_CHROME_URL`, `Services.xulStore`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `this.NUM_TOOLBAR_BOOKMARKS_TO_UNHIDE`
- XPCOM: `Services.xulStore`

## uncollapseToolbar()
- 位置: L1302-1308
- 役割: browser-set-toolbar-visibility を通知し、ブックマークツールバーを表示させる。
- 触るとき: ツールバー表示の通知方法を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.obs.notifyObservers()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`
- XPCOM: `Services.obs`

## shouldHideOpenMenuItem()
- 位置: L1342-1372
- 役割: 開く系メニュー項目の hide-if-* 属性を見て、プライベートブラウズ、コンテナ、コンテンツ共有の設定に応じて非表示にするかを返す。
- 触るとき: 「開く」系メニュー項目の表示条件を追加・変更するとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `item.hasAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `item.documentGlobal`, `lazy.ContentSharingUtils.isEnabled`, `lazy.PrivateBrowsingUtils.enabled`
- XPCOM: `Services.prefs`

## managedPlacesContextShowing()
- 位置: async L1374-1424
- 役割: 管理ブックマークのメニューを開く前に項目を読み込み、対象がフォルダーか項目かに応じて項目の表示と「タブで開く」の有効状態を決めたうえで、コマンドを更新する。
- 触るとき: 管理ブックマーク (managed-bookmarks) のメニューが空になる、誤った項目が出る問題を調べるとき。
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
- 役割: Places 系コンテキストメニューの表示前に、対象のメニューか判定し、既定の開き先と lastContextMenuTriggerNode を設定してから、ビューに項目を組み立てさせる。
- 触るとき: コンテキストメニュー全体の表示条件や既定項目を変えるとき、メニューが出ない問題を調べるとき。
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
- 役割: メニューを閉じるときビューのコンテキストメニューを破棄し、対象メニューなら lastContextMenuTriggerNode と lastContextMenuCommand をリセットする。
- 触るとき: コンテキストメニューの後始末を変えるとき、閉じた後に古いトリガーが残る問題を調べるとき。
- 条件付き依存: `if (menupopup._view)` → `menupopup._view.destroyContextMenu()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`, `PlacesUIUtils.lastContextMenuTriggerNode`, `event.target`, `menupopup._view`, `menupopup.id`

## createContainerTabMenu()
- 位置: L1507-1513
- 役割: イベントのウィンドウで createUserContextMenu を呼び、コンテナタブ用のサブメニューを作る。
- 触るとき: 「コンテナタブで開く」サブメニューの生成を変えるとき。
- 呼び出し先: `window.createUserContextMenu()`
- 参照: `event.target.documentGlobal`

## openInContainerTab()
- 位置: L1515-1541
- 役割: data-usercontextid のコンテナ ID で、トリガーノード (または選択中ノード) をタブで開く。管理ブックマークは openTrustedLinkIn で直接開く。
- 触るとき: コンテナタブで開く動作や、コンテナ ID の受け渡しを変えるとき。
- 呼び出し先: `event.target.getAttribute()`, `parseInt()`, `this._openNodeIn()`, `this.getViewForNode()`, `triggerNode?.closest()`
- 条件付き依存: `if (isManaged)` → `window.openTrustedLinkIn()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`, `this.lastContextMenuTriggerNode`, `triggerNode.documentGlobal`, `triggerNode.documentGlobal.top`, `triggerNode.link`, `view?.ownerWindow`, `view?.selectedNode`

## openSelectionInTabs()
- 位置: L1543-1555
- 役割: 管理ブックマークなら管理用コントローラー、それ以外は対象ビューのコントローラーを選び、その openSelectionInTabs を呼ぶ。
- 触るとき: 選択項目をタブで開くメニューの振る舞いを、管理ブックマークと通常ビューで分けて変えるとき。
- 呼び出し先: `controller.openSelectionInTabs()`, `event.target.parentNode.triggerNode.closest()`
- 条件付き依存: `if (!(isManaged))` → `PlacesUIUtils.getViewForNode()`
- 参照: `PlacesUIUtils.getViewForNode( PlacesUIUtils.lastContextMenuTriggerNode ).controller`, `PlacesUIUtils.lastContextMenuTriggerNode`, `this.managedBookmarksController`

## openSelectionInTabs()
- 位置: L1560-1573
- 役割: 管理ブックマークの子メニューから link を持つ項目を集め、openTabset で開く。
- 触るとき: 管理ブックマークの「すべてタブで開く」の対象を変えるとき。
- 呼び出し先: `PlacesUIUtils.openTabset()`
- 条件付き依存: `if (menuitems[i].link)` → `items.push()`
- 参照: `event.target.documentGlobal`, `event.target.parentNode.triggerNode.menupopup.children`, `item.isBookmark`, `item.uri`, `menuitems.length`, `menuitems[i].link`

## isCommandEnabled()
- 位置: L1575-1585
- 役割: 管理ブックマーク用のコントローラーで、コピーと3種類の開く操作だけを有効にする。
- 触るとき: 管理ブックマークのメニューで使えるコマンドを増減させるとき。

## doCommand()
- 位置: L1587-1611
- 役割: 管理ブックマーク用のコントローラーで、トリガーのリンクをコピーし、タブや通常・プライベートのウィンドウで開く。
- 触るとき: 管理ブックマークのメニュー操作の結果を変えるとき。
- 呼び出し先: `lazy.BrowserUtils.copyLink()`, `window.openTrustedLinkIn()`
- 参照: `this.triggerNode.documentGlobal`, `this.triggerNode.label`, `this.triggerNode.link`

## maybeAddImportButton()
- 位置: async L1614-1645
- 役割: profileImport が許可されていれば、ツールバー直下の項目が 3 件未満のときインポートボタンをブックマーク領域に追加し、移行の成功を待つ監視を始める。
- 触るとき: 初回起動時のインポートボタンの表示条件を変えるとき、ポリシーで取り込みを禁止した場合の挙動を確認するとき。
- 呼び出し先: `Services.policies.isAllowed()`, `console.error()`, `db.execute()`, `lazy.PlacesUtils.withConnectionWrapper()`, `rows[0].getResultByName()`
- 条件付き依存: `if (numberOfBookmarks < 3)` → `lazy.CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (numberOfBookmarks < 3)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (numberOfBookmarks < 3)` → `this.removeImportButtonWhenImportSucceeds()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`, `lazy.PlacesUtils.bookmarks.toolbarGuid`
- XPCOM: `Services.policies` / `Services.prefs`

## removeImportButton()
- 位置: L1647-1650
- 役割: インポートボタンをツールバーから外し、addedImportButton の設定を消す。
- 触るとき: インポートボタンの後始末を変えるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `lazy.CustomizableUI.removeWidgetFromArea()`
- XPCOM: `Services.prefs`

## removeImportButtonWhenImportSucceeds()
- 位置: L1652-1673
- 役割: ボタンが既定の位置から移動されていれば設定だけ消す。そうでなければ移行 (ItemAfterMigrate/ItemError) の通知を待つオブザーバーを登録する。
- 触るとき: 移行成功時にボタンを外す条件を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (placement?.area != lazy.CustomizableUI.AREA_BOOKMARKS)` → `Services.prefs.clearUserPref()`
- 参照: `lazy.CustomizableUI.AREA_BOOKMARKS`, `placement?.area`
- XPCOM: `Services.obs` / `Services.prefs`

## obs()
- 位置: L1661-1670
- 役割: ブックマーク移行で 1 件以上取り込めたとき removeImportButton を呼び、2 種類のオブザーバーを外す。
- 触るとき: 移行完了後にインポートボタンが消えない、または早く消える問題を調べるとき。
- 呼び出し先: `lazy.MigrationUtils.getImportedCount()`
- 条件付き依存: `if ( data == lazy.MigrationUtils.resourceTypes.BOOKMARKS && lazy.MigrationUtils.getImportedCount("bookmarks") > 0 )` → `this.removeImportButton()`
- 条件付き依存: `if ( data == lazy.MigrationUtils.resourceTypes.BOOKMARKS && lazy.MigrationUtils.getImportedCount("bookmarks") > 0 )` → `Services.obs.removeObserver()`
- 参照: `lazy.MigrationUtils.resourceTypes.BOOKMARKS`
- XPCOM: `Services.obs`

## setupSpeculativeConnection()
- 位置: L1684-1707
- 役割: browser.places.speculativeConnect.enabled が有効で URL が http で始まるなら、speculativeConnect で先行接続する。例外は無視する。
- 触るとき: 投機的接続の条件 (有効化の pref や対象 URL) を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `Services.io.speculativeConnect()`, `Services.prefs.getBoolPref()`, `url.startsWith()`
- 参照: `window.gBrowser.contentPrincipal`
- XPCOM: `Services.io` / `Services.prefs`

## maybeSpeculativeConnectOnMouseDown()
- 位置: L1715-1726
- 役割: 右クリック以外の mousedown で、対象ノードの URL に対して setupSpeculativeConnection を呼ぶ。
- 触るとき: マウス押下時の先行接続の対象を変えるとき。
- 条件付き依存: `if ( event.type == "mousedown" && event.target._placesNode?.uri && event.button != 2 )` → `PlacesUIUtils.setupSpeculativeConnection()`
- 参照: `event.button`, `event.target._placesNode.uri`, `event.target._placesNode?.uri`, `event.target.documentGlobal`, `event.type`

## getImageURL()
- 位置: L1738-1746
- 役割: アイコン URL を getFaviconLinkForIcon で cached-favicon 形式に変換する。URL が不正なら既定のファビコンの spec を返す。
- 触るとき: ブックマークや履歴の一覧で使うアイコンの取得元を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconLinkForIcon()`
- 参照: `lazy.PlacesUtils.favicons.defaultFavicon.spec`, `lazy.PlacesUtils.favicons.getFaviconLinkForIcon( Services.io.newURI(icon) ).spec`
- XPCOM: `Services.io`

## insertTitleStartDiffs()
- 位置: L1766-1815
- 役割: 同じ先頭文字列を持つ長いタイトル同士を比べ、最初に異なる位置を各候補の titleDifferentIndex に書き込む。候補オブジェクトは直接書き換える。
- 触るとき: 似たタイトルを区別するための省略表示や、差分位置の表示を変えるとき。
- 呼び出し先: `candidate.title.slice()`, `longTitles.get()`
- 条件付き依存: `if (matches)` → `findStartDifference()`
- 条件付き依存: `if (matches)` → `matches.push()`
- 条件付き依存: `if (!(matches))` → `longTitles.set()`
- 参照: `candidate.title`, `candidate.title.length`, `candidate.titleDifferentIndex`, `match.title`, `match.titleDifferentIndex`, `this.similarTitlesMinChars`

## findStartDifference()
- 位置: L1767-1780
- 役割: 先頭の similarTitlesMinChars 文字を飛ばし、最初に異なる文字の位置を返す。全部一致なら -1 を返す。
- 触るとき: タイトル差分位置の計算ルールを変えるとき。
- 参照: `PlacesUIUtils.similarTitlesMinChars`, `a.length`, `b.length`

## shareBookmarkFolder()
- 位置: L1820-1833
- 役割: 選択中のノードのうちフォルダーかショートカットのものの guid を集め、ContentSharingUtils で共有リンクを作る。失敗はログに出す。
- 触るとき: 試験中のフォルダー共有の対象や失敗時の扱いを変えるとき。
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `console.error()`, `lazy.ContentSharingUtils.createShareableLinkFromBookmarkFolders()`, `lazy.PlacesUtils.getConcreteItemGuid()`, `lazy.PlacesUtils.nodeIsFolderOrShortcut()`, `view.selectedNodes .filter()`, `view.selectedNodes .filter(n => lazy.PlacesUtils.nodeIsFolderOrShortcut(n)) .map()`
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`

## canMoveUnwrappedNode()
- 位置: L1934-1949
- 役割: ルート項目や、親がルート (rootGuid) の項目は移動不可、それ以外は移動可能と判定する。
- 触るとき: ドラッグで移動できる項目の条件を変えるとき。
- 呼び出し先: `lazy.PlacesUtils.isRootItem()`
- 参照: `lazy.PlacesUtils.bookmarks.rootGuid`, `unwrappedNode.concreteGuid`, `unwrappedNode.guid`, `unwrappedNode.parentGuid`

## getResultForBatching()
- 位置: L1961-1978
- 役割: 左ペインの placesList なら右ペインの placeContent を選び、そのビューの result を返す。なければ null。
- 触るとき: バッチ更新を掛けるビューをどれにするかを変えるとき。
- 呼び出し先: `Element.isInstance()`
- 条件付き依存: `if ( viewOrElement && Element.isInstance(viewOrElement) && viewOrElement.id === "placesList" )` → `viewOrElement.ownerDocument.getElementById()`
- 参照: `viewOrElement.id`, `viewOrElement.result`

## getTransactionsForTransferItems()
- 位置: L1992-2049
- 役割: 同一セッションでない項目は移動させずコピーにする。移動可能なら Move のトランザクションを、そうでなければ getTransactionsForCopy の結果を返す。
- 触るとき: ドロップで移動かコピーかを決める条件を変えるとき、他のアプリからのドロップの扱いを調べるとき。
- 呼び出し先: `PlacesUIUtils.SUPPORTED_FLAVORS.includes()`, `getTransactionsForCopy()`
- 条件付き依存: `if ( !("instanceId" in item) || item.instanceId != lazy.PlacesUtils.instanceId )` → `PlacesUIUtils.PLACES_FLAVORS.includes()`
- 条件付き依存: `if (PlacesUIUtils.PLACES_FLAVORS.includes(item.type))` → `console.error()`
- 条件付き依存: `if (doMove && canMove)` → `canMoveUnwrappedNode()`
- 条件付き依存: `if (doMove)` → `lazy.PlacesTransactions.Move()`
- 条件付き依存: `if (doMove)` → `items.map()`
- 参照: `item.instanceId`, `item.itemGuid`, `item.type`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `lazy.PlacesUtils.instanceId`

## getTransactionsForCopy()
- 位置: L2060-2110
- 役割: 同一セッションの Places 項目は Copy、セパレーターは NewSeparator、その他は NewBookmark のトランザクションを挿入位置を進めながら作る。
- 触るとき: 貼り付けやドロップで複製される内容 (ショートカットを作る条件など) を変えるとき。
- 呼び出し先: `PlacesUIUtils.PLACES_FLAVORS.includes()`, `lazy.PlacesUtils.bookmarks.isVirtualRootItem()`, `lazy.PlacesUtils.isVirtualLeftPaneItem()`, `transactions.push()`
- 条件付き依存: `if ( PlacesUIUtils.PLACES_FLAVORS.includes(item.type) && // For anything that is comming from within this session, we do a // direct copy, otherwise we fallback ...)` → `lazy.PlacesTransactions.Copy()`
- 条件付き依存: `if (item.type == lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR)` → `lazy.PlacesTransactions.NewSeparator()`
- 条件付き依存: `if (!(item.type == lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR))` → `lazy.PlacesTransactions.NewBookmark()`
- 参照: `item.instanceId`, `item.itemGuid`, `item.title`, `item.type`, `item.uri`, `lazy.PlacesUtils.TYPE_PLAINTEXT`, `lazy.PlacesUtils.TYPE_X_MOZ_PLACE_SEPARATOR`, `lazy.PlacesUtils.instanceId`

## getBrowserWindow()
- 位置: L2112-2120
- 役割: 渡されたウィンドウが通常のブラウザーウィンドウならそれを、そうでなければ最前面のブラウザーウィンドウを返す。
- 触るとき: 操作を行うブラウザーウィンドウの選び方を変えるとき。
- 呼び出し先: `aWindow.document.documentElement.getAttribute()`, `lazy.BrowserWindowTracker.getTopWindow()`
