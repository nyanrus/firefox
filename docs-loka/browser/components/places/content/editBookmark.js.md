# browser/components/places/content/editBookmark.js

source: browser/components/places/content/editBookmark.js
source-hash: d3180c5b1e662de5edbad124c16dfffc7f369cdf
lines: 1328

## <module>
- 役割: ブックマーク編集パネル (gEditItemOverlay) を定義する。フィールドやフォルダーツリーを遅延取得し、星ボタンとライブラリの両方から使われる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `MozXULElement.parseXULToFragment()`, `customElements.get()`, `folderTree.addEventListener()`, `gEditItemOverlay._element()`, `gEditItemOverlay._element("folderTreeRow").prepend()`, `gEditItemOverlay.onFolderTreeSelect()`

## _setPaneInfo()
- 位置: L39-128
- 役割: 初期化情報 (node か uris) から表示用の状態オブジェクトを作り、_paneInfo に保存する。
- 触るとき: パネルに渡すノードの種類 (単体、複数、タグ、フォルダーショートカット) によって表示が変わるとき。
- 呼び出し先: `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsTagQuery()`, `PlacesUtils.nodeIsURI()`, `Services.io.newURI()`
- 条件付き依存: `if (isTag)` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (addedMultipleBookmarks)` → `node.children.map()`
- 条件付き依存: `if (node && isItem)` → `PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER_SHORTCUT`, `PlacesUtils.asQuery(node).query.tags.length`, `aInitInfo.addedMultipleBookmarks`, `aInitInfo.focusedElement`, `aInitInfo.node`, `aInitInfo.onPanelReady`, `aInitInfo.postData`, `aInitInfo.uris`, `c.url`, `node.parent`, `node.query.tags`, `node.title`, `node.type`, `node.uri`, `parent.bookmarkGuid`, `this._paneInfo`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.io`

## initialized()
- 位置: L130-132
- 役割: _paneInfo があるかどうかを返す。
- 触るとき: パネルが初期化済みかを判定してから値を読むとき。
- 参照: `this._paneInfo`

## concreteGuid()
- 位置: L140-149
- 役割: 初期化済みで単体のブックマークなら、その GUID を返す。タグや複数選択では null。
- 触るとき: 編集中の対象 GUID を外へ渡す箇所で、どの項目を指すかを確認するとき。
- 参照: `this._paneInfo.bulkTagging`, `this._paneInfo.isTag`, `this._paneInfo.itemGuid`, `this.initialized`

## uri()
- 位置: L151-159
- 役割: 単体なら対象の URI、複数選択なら先頭の URI を返す。
- 触るとき: 編集対象の URL を表示や保存に使う箇所を追うとき。
- 参照: `this._paneInfo.bulkTagging`, `this._paneInfo.uri`, `this._paneInfo.uris`, `this.initialized`

## multiEdit()
- 位置: L161-163
- 役割: 複数ブックマークを一括でタグ付けする状態かを返す。
- 触るとき: 複数選択時だけ隠す項目や入力を分けるとき。
- 参照: `this._paneInfo.bulkTagging`, `this.initialized`

## readOnly()
- 位置: L166-184
- 役割: フォルダーショートカット、項目でもタグでもない対象、読み取り専用の親の中の非ブックマークのときに読み取り専用と判定する。
- 触るとき: 編集できない項目が編集可能に見えるとき、または読み取り専用の条件を増やすとき。
- 参照: `this._paneInfo.isBookmark`, `this._paneInfo.isFolderShortcut`, `this._paneInfo.isItem`, `this._paneInfo.isParentReadOnly`, `this._paneInfo.isTag`, `this.initialized`

## didChangeFolder()
- 位置: L186-188
- 役割: 保存先フォルダーを今回の編集で変えたかを返す。
- 触るとき: 閉じるときに既定の保存先フォルダーを更新すべきか判断するとき。
- 参照: `this._didChangeFolder`

## _initNamePicker()
- 位置: L194-204
- 役割: 名前欄に、タイトルがなければタグ名か空文字を入れる。
- 触るとき: 名前が空欄で表示されたり、タグの名前が出なかったりするとき。
- 呼び出し先: `this._initTextField()`
- 参照: `this._namePicker`, `this._paneInfo.addedMultipleBookmarks`, `this._paneInfo.bulkTagging`, `this._paneInfo.tag`, `this._paneInfo.title`

## _initLocationField()
- 位置: L206-211
- 役割: URL 欄に対象 URL の spec を入れる。URL 項目でなければ例外を投げる。
- 触るとき: URL 欄の初期値が違うとき、または URL 以外の項目で呼ばれたとき。
- 呼び出し先: `this._initTextField()`
- 参照: `this._locationField`, `this._paneInfo.isURI`, `this._paneInfo.uri.spec`

## _initKeywordField()
- 位置: async L213-245
- 役割: キーワード欄を初期化し、新規でなければ同じ URL の既存キーワードを検索して入れる。
- 触るとき: 既存のキーワードが欄に出ないとき、または POST データ付きのキーワードの扱いを変えるとき。
- 呼び出し先: `this._initTextField()`
- 条件付き依存: `if (!newKeyword)` → `PlacesUtils.keywords.fetch()`
- 条件付き依存: `if (!newKeyword)` → `entries.push()`
- 条件付き依存: `if (postData)` → `entries.find()`
- 条件付き依存: `if (existingKeyword)` → `this._initTextField()`
- 参照: `e.postData`, `entries.length`, `entries[0].keyword`, `sameEntry.keyword`, `this._keyword`, `this._keywordField`, `this._paneInfo.isBookmark`, `this._paneInfo.postData`, `this._paneInfo.uri.spec`

## _initAllTags()
- 位置: async L247-253
- 役割: 全タグを取得し、小文字名から元の名前への Map を作る。
- 触るとき: タグ選択リストの候補が足りないとき、またはタグの大文字小文字の扱いを確かめるとき。
- 呼び出し先: `PlacesUtils.bookmarks.fetchTags()`, `tag.name.toLowerCase()`, `this._allTags?.set()`
- 参照: `tag.name`, `this._allTags`

## initPanel()
- 位置: async L273-479
- 役割: 情報を受け取り、行の出し分け、各欄の初期化、フォーカス、タグ一覧の構築をまとめて行う。
- 触るとき: 編集パネルを開いたときに表示が崩れる、または特定の行が出ないとき。最初に読むべき関数。
- 呼び出し先: `PlacesUtils.nodeIsFolderOrShortcut()`, `Promise.withResolvers()`, `deferred.resolve()`, `showOrCollapse()`, `this._setPaneInfo()`, `this.makeNewStateObject()`
- 条件付き依存: `if (this.initialized)` → `this.uninitPanel()`
- 条件付き依存: `if ( aInfo.isNewBookmark && parentGuid == PlacesUtils.bookmarks.toolbarGuid )` → `this._autoshowBookmarksToolbar()`
- 条件付き依存: `if (!this._observersAdded)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._observersAdded)` → `PlacesUtils.observers.addListener()`
- 条件付き依存: `if (!this._observersAdded)` → `window.addEventListener()`
- 条件付き依存: `if (!this._observersAdded)` → `document.getElementById()`
- 条件付き依存: `if (!this._observersAdded)` → `panel.addEventListener()`
- 条件付き依存: `if ( showOrCollapse( "nameRow", !bulkTagging || addedMultipleBookmarks, "name" ) )` → `this._initNamePicker()`
- 条件付き依存: `if (isURI)` → `this._initLocationField()`
- 条件付き依存: `if (showOrCollapse("keywordRow", isBookmark, "keyword"))` → `this._initKeywordField().catch()`
- 条件付き依存: `if (showOrCollapse("keywordRow", isBookmark, "keyword"))` → `this._initKeywordField()`
- 条件付き依存: `if (showOrCollapse("tagsRow", isBookmark || bulkTagging, "tags"))` → `this._initTagsField()`
- 条件付き依存: `if (!(showOrCollapse("tagsRow", isBookmark || bulkTagging, "tags")))` → `this._element()`
- 条件付き依存: `if (!this._element("tagsSelectorRow").hidden)` → `this.toggleTagsSelector().catch()`
- 条件付き依存: `if (!this._element("tagsSelectorRow").hidden)` → `this.toggleTagsSelector()`
- 条件付き依存: `if (showOrCollapse("folderRow", isItem, "folderPicker"))` → `this._initFolderMenuList(parentGuid).catch()`
- 条件付き依存: `if (showOrCollapse("folderRow", isItem, "folderPicker"))` → `this._initFolderMenuList()`
- 条件付き依存: `if (showOrCollapse("selectionCount", bulkTagging))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (showOrCollapse("selectionCount", bulkTagging))` → `this._element()`
- 条件付き依存: `if (onPanelReady)` → `onPanelReady()`
- 条件付き依存: `if (!(onPanelReady))` → `focusElement()`
- 条件付き依存: `if (isBookmark || bulkTagging)` → `this._initAllTags()`
- 条件付き依存: `if (isBookmark || bulkTagging)` → `this._rebuildTagsSelectorList()`
- 参照: `PlacesUtils.bookmarks.toolbarGuid`, `aInfo.isNewBookmark`, `aInfo.node`, `aInfo.node.type`, `aInfo.node?.children`, `aInfo.node?.index`, `console.error`, `this._bookmarkState`, `this._didChangeFolder`, `this._element("tagsSelectorRow").hidden`, `this._initPanelDeferred`, `this._instance`, `this._keywordField.readOnly`, `this._locationField.readOnly`, `this._namePicker.readOnly`, `this._observersAdded`, `this._paneInfo`, `this._updateTagsDeferred`, `this._updateTagsDeferred.promise`, `this.handlePlacesEvents`, `this.initialized`, `this.readOnly`, `this.transactionPromises`, `uris.length`

## showOrCollapse()
- 位置: L344-361
- 役割: 行の表示/非表示を切り替え、表示したときは行 ID を visibleRows に記録する。
- 触るとき: hiddenRows の指定で行を隠す条件を変えるとき、または行が消えたままのとき。
- 呼び出し先: `document.getElementsByClassName()`
- 条件付き依存: `if (visible && "hiddenRows" in aInfo && nameInHiddenRows)` → `aInfo.hiddenRows.includes()`
- 条件付き依存: `if (visible)` → `visibleRows.add()`
- 参照: `cell.hidden`

## focusElement()
- 位置: L419-449
- 役割: 最初に編集された欄 (preferred) か最初の入力欄に、フォーカスと選択を移す。
- 触るとき: パネルを開いたときにどの欄へフォーカスが行くかを変えるとき。
- 条件付き依存: `if (focusedElement === "preferred")` → `this._element()`
- 条件付き依存: `if (focusedElement === "preferred")` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (focusedElement === "first")` → `document .getElementById("editBookmarkPanelContent") .querySelector()`
- 条件付き依存: `if (focusedElement === "first")` → `document .getElementById()`
- 条件付き依存: `if (elt)` → `elt.focus()`
- 条件付き依存: `if (elt)` → `elt.select()`
- 参照: `elt.parentNode.hidden`
- XPCOM: `Services.prefs`

## _getCommonTags()
- 位置: L486-510
- 役割: 複数 URI の全てに共通するタグを求めてキャッシュする。
- 触るとき: 複数選択時にタグ欄へ共通のタグだけ出すべきなのに余計なタグが出るとき。キャッシュの書き込み先に食い違いがある点も確認する。
- 呼び出し先: `PlacesUtils.tagging.getTagsForURI()`, `curentURITags.includes()`, `uris.shift()`
- 条件付き依存: `if (!curentURITags.includes(tag))` → `commonTags.delete()`
- 参照: `commonTags.size`, `this._cachedCommonTags`, `this._paneInfo`, `this._paneInfo._cachedCommonTags`, `this._paneInfo.cachedCommonTags`, `this._paneInfo.uris`

## _initTextField()
- 位置: L512-520
- 役割: 値が違うときだけ欄へ設定し、編集の Undo 履歴を消す。
- 触るとき: 欄の値を外部から設定したあとに Ctrl+Z で前の値が戻ってしまうとき。
- 条件付き依存: `if (aElement.value != aValue)` → `aElement.editor?.clearUndoRedo()`
- 参照: `aElement.value`

## _appendFolderItemToMenupopup()
- 位置: L534-544
- 役割: フォルダーのメニュー項目を作ってポップアップ末尾へ追加し、区切りを表示する。
- 触るとき: 保存先メニューに項目が出ない、またはアイコンやラベルを変えたいとき。
- 呼び出し先: `aMenupopup.appendChild()`, `document.createXULElement()`, `folderMenuItem.setAttribute()`, `this._element()`
- 参照: `folderMenuItem.className`, `folderMenuItem.folderGuid`, `this._element("foldersSeparator").hidden`

## _initFolderMenuList()
- 位置: async L546-623
- 役割: 固定のルートフォルダーと最近使ったフォルダーを並べ、現在の保存先を選択する。
- 触るとき: 保存先メニューの並びや、最近使ったフォルダーの読み込みに問題があるとき。
- 呼び出し先: `Math.min()`, `PlacesUtils.bookmarks.fetch()`, `PlacesUtils.metadata.get()`, `menupopup.removeChild()`, `this._appendFolderItemToMenupopup()`, `this._element()`, `this._folderMenuList.addEventListener()`, `this._getFolderMenuItem()`, `this._onFolderListSelected()`
- 条件付き依存: `if (!this._staticFoldersListBuilt)` → `PlacesUtils.getString()`
- 条件付き依存: `if (!this._staticFoldersListBuilt)` → `this._element()`
- 条件付き依存: `if (bm)` → `PlacesUtils.bookmarks.getLocalizedTitle()`
- 条件付き依存: `if (bm)` → `this._recentFolders.push()`
- 参照: `(await PlacesUtils.bookmarks.fetch(aSelectedFolderGuid)).title`, `PlacesUIUtils.LAST_USED_FOLDERS_META_KEY`, `PlacesUIUtils.maxRecentFolders`, `PlacesUtils.bookmarks.menuGuid`, `PlacesUtils.bookmarks.mobileGuid`, `PlacesUtils.bookmarks.toolbarGuid`, `PlacesUtils.bookmarks.unfiledGuid`, `bmMenuItem.folderGuid`, `bmMenuItem.label`, `menupopup.children.length`, `menupopup.lastElementChild`, `mobileItem.folderGuid`, `mobileItem.hidden`, `mobileItem.label`, `this._element("foldersSeparator").hidden`, `this._folderMenuList.disabled`, `this._folderMenuList.menupopup`, `this._folderMenuList.selectedItem`, `this._folderMenuListListenerAdded`, `this._recentFolders`, `this._recentFolders.length`, `this._recentFolders[i].guid`, `this._recentFolders[i].title`, `this._staticFoldersListBuilt`, `this.readOnly`, `toolbarItem.folderGuid`, `toolbarItem.label`, `unfiledItem.folderGuid`, `unfiledItem.label`

## _onFolderListSelected()
- 位置: L625-633
- 役割: 選択中フォルダーの GUID を selectedGuid 属性へ反映し、専用アイコンの表示を切り替える。
- 触るとき: 保存先メニューの特別なアイコンが正しく出ないとき。
- 条件付き依存: `if (folderGuid)` → `this._folderMenuList.setAttribute()`
- 条件付き依存: `if (!(folderGuid))` → `this._folderMenuList.removeAttribute()`
- 参照: `this.selectedFolderGuid`

## _element()
- 位置: L635-637
- 役割: ID に editBMPanel_ を付けて要素を取得する。
- 触るとき: パネル内の要素を取るときは必ずこれを使うので、ID の付け方を変えるとき。
- 呼び出し先: `document.getElementById()`

## uninitPanel()
- 位置: L639-678
- 役割: 表示を閉じ、オブザーバーとリスナーを外し、パネル状態を初期値へ戻す。
- 触るとき: パネルを閉じたあとにイベントが残って二重に動く、または次回の表示に前の内容が出るとき。
- 呼び出し先: `this._setPaneInfo()`
- 条件付き依存: `if (aHideCollapsibleElements)` → `this._element()`
- 条件付き依存: `if (!folderTreeRow.hidden)` → `this.toggleFolderTreeVisibility()`
- 条件付き依存: `if (!tagsSelectorRow.hidden)` → `this.toggleTagsSelector().catch()`
- 条件付き依存: `if (!tagsSelectorRow.hidden)` → `this.toggleTagsSelector()`
- 条件付き依存: `if (this._observersAdded)` → `PlacesUtils.observers.removeListener()`
- 条件付き依存: `if (this._observersAdded)` → `window.removeEventListener()`
- 条件付き依存: `if (this._observersAdded)` → `document.getElementById()`
- 条件付き依存: `if (this._observersAdded)` → `panel.removeEventListener()`
- 条件付き依存: `if (this._folderMenuListListenerAdded)` → `this._folderMenuList.removeEventListener()`
- 参照: `console.error`, `folderTreeRow.hidden`, `tagsSelectorRow.hidden`, `this._allTags`, `this._bookmarkState`, `this._didChangeFolder`, `this._firstEditedField`, `this._folderMenuListListenerAdded`, `this._observersAdded`, `this.handlePlacesEvents`, `this.transactionPromises`

## selectedFolderGuid()
- 位置: L680-685
- 役割: 保存先メニューで選ばれているフォルダーの GUID を返す。
- 触るとき: 保存先を外へ渡す箇所を追うとき。
- 参照: `this._folderMenuList.selectedItem`, `this._folderMenuList.selectedItem.folderGuid`

## makeNewStateObject()
- 位置: L687-714
- 役割: 項目の情報、追加オプション、タグとキーワードの欄の値から BookmarkState を作る。
- 触るとき: 保存時に渡る状態の中身 (タグやキーワードの取り込み) を変えるとき。
- 条件付き依存: `if ( this._paneInfo.isItem || this._paneInfo.isTag || this._paneInfo.bulkTagging )` → `document.documentElement.getAttribute()`
- 条件付き依存: `if (this._paneInfo.isBookmark)` → `this._element()`
- 条件付き依存: `if (this._paneInfo.bulkTagging)` → `this._element()`
- 参照: `PlacesUIUtils.BookmarkState`, `options.keyword`, `options.tags`, `this._element("tagsField").value`, `this._keyword`, `this._paneInfo`, `this._paneInfo.bulkTagging`, `this._paneInfo.isBookmark`, `this._paneInfo.isItem`, `this._paneInfo.isTag`

## onTagsFieldChange()
- 位置: async L716-733
- 役割: タグ欄が変わったとき、タグを更新してから最初の編集欄を記録する。
- 触るとき: タグを入力したあとに一覧や最初の欄の記録がずれるとき。
- 条件付き依存: `if ( this._paneInfo && (this._paneInfo.isURI || this._paneInfo.bulkTagging) )` → `this._updateTags().then()`
- 条件付き依存: `if ( this._paneInfo && (this._paneInfo.isURI || this._paneInfo.bulkTagging) )` → `this._updateTags()`
- 条件付き依存: `if (this._paneInfo)` → `this._mayUpdateFirstEditField()`
- 参照: `console.error`, `this._initPanelDeferred`, `this._initPanelDeferred.promise`, `this._paneInfo`, `this._paneInfo.bulkTagging`, `this._paneInfo.isURI`

## _updateTags()
- 位置: async L738-769
- 役割: 入力タグを状態へ反映し、保存しないモードでは候補一覧を更新する。図書館ウィンドウでは欄を再構築する。
- 触るとき: タグの追加や削除が保存に反映されない、または一覧が更新されないとき。
- 呼び出し先: `Promise.withResolvers()`, `deferred.resolve()`, `document.documentElement.getAttribute()`, `this._bookmarkState._tagsChanged()`, `this._getTagsArrayFromTagsInputField()`, `this._rebuildTagsSelectorList()`
- 条件付き依存: `if (isLibraryWindow)` → `this._getCommonTags()`
- 条件付き依存: `if (isLibraryWindow)` → `PlacesUtils.tagging.getTagsForURI()`
- 条件付き依存: `if (isLibraryWindow)` → `this._initTextField()`
- 条件付き依存: `if (isLibraryWindow)` → `currentTags.join()`
- 条件付き依存: `if (isLibraryWindow)` → `this._initAllTags()`
- 条件付き依存: `if (!(isLibraryWindow))` → `inputTags.forEach()`
- 条件付き依存: `if (!(isLibraryWindow))` → `this._allTags?.set()`
- 条件付き依存: `if (!(isLibraryWindow))` → `tag.toLowerCase()`
- 参照: `this._paneInfo._cachedCommonTags`, `this._paneInfo.bulkTagging`, `this._paneInfo.uri`, `this._tagsField`, `this._updateTagsDeferred`

## _mayUpdateFirstEditField()
- 位置: L778-793
- 役割: 最初に編集された欄を一度だけ記録し、browser.bookmarks.editDialog.firstEditField に保存する。
- 触るとき: 次回開いたときに最初にフォーカスされる欄がずれるとき、または記録条件を変えるとき。
- 呼び出し先: `Services.prefs.setCharPref()`
- 参照: `this._firstEditedField`, `this._paneInfo.bulkTagging`
- XPCOM: `Services.prefs`

## onNamePickerChange()
- 位置: async L795-817
- 役割: 名前欄の変更を状態へ反映する。タグの場合は空や & を含む名前を拒否して元へ戻す。
- 触るとき: 名前が保存されない、またはタグ名に記号を使えないルールを変えるとき。
- 呼び出し先: `this._bookmarkState._titleChanged()`, `this._mayUpdateFirstEditField()`
- 条件付き依存: `if (this._paneInfo.isTag)` → `tag.includes()`
- 条件付き依存: `if (!tag || tag.includes("&"))` → `this._initNamePicker()`
- 条件付き依存: `if (this._paneInfo.isTag)` → `this._bookmarkState._titleChanged()`
- 参照: `this._initPanelDeferred`, `this._initPanelDeferred.promise`, `this._namePicker.value`, `this._paneInfo.isItem`, `this._paneInfo.isTag`, `this.readOnly`

## onLocationFieldChange()
- 位置: async L819-841
- 役割: URL 欄の入力を URI 修正 (fixup) して、変わっていれば状態へ反映する。不正な URL は無視する。
- 触るとき: URL を書き換えても保存されない、または入力の補正を変えるとき。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `this._bookmarkState._locationChanged()`, `this._paneInfo.uri.equals()`
- 参照: `Services.uriFixup.getFixupURIInfo( this._locationField.value ).preferredURI`, `newURI.spec`, `this._initPanelDeferred`, `this._initPanelDeferred.promise`, `this._locationField.value`, `this._paneInfo.isBookmark`, `this.readOnly`
- XPCOM: `Services.uriFixup`

## onKeywordFieldChange()
- 位置: async L843-851
- 役割: キーワード欄の値を状態へ反映する。
- 触るとき: キーワードの変更が保存されないとき。
- 呼び出し先: `this._bookmarkState._keywordChanged()`
- 参照: `this._initPanelDeferred`, `this._initPanelDeferred.promise`, `this._keywordField.value`, `this._paneInfo.isBookmark`, `this.readOnly`

## toggleFolderTreeVisibility()
- 位置: L853-895
- 役割: フォルダーツリーを開閉する。開くときは RESULTS_AS_ROOTS_QUERY で読み込み、閉じるときは view を外す。
- 触るとき: 保存先ツリーの開閉で見た目が崩れるとき、または閉じたあとも更新が続くとき。
- 呼び出し先: `expander.classList.toggle()`, `this._element()`
- 条件付き依存: `if (!wasHidden)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!wasHidden)` → `this._element()`
- 条件付き依存: `if (!wasHidden)` → `this._folderTree.stopEditing()`
- 条件付き依存: `if (!(!wasHidden))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(!wasHidden))` → `this._element()`
- 条件付き依存: `if (!(!wasHidden))` → `this._folderTree.selectItems()`
- 条件付き依存: `if (!(!wasHidden))` → `this._folderTree.focus()`
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_ROOTS_QUERY`, `folderTreeRow.hidden`, `this._bookmarkState.parentGuid`, `this._element( "chooseFolderMenuItem" ).hidden`, `this._element("chooseFolderSeparator").hidden`, `this._folderTree.place`, `this._folderTree.view`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## _getFolderMenuItem()
- 位置: L911-930
- 役割: 保存先メニューからフォルダーの項目を探し、無ければ作る。上限に達したら末尾の項目を置き換える。
- 触るとき: 最近使ったフォルダーが上限を超えて増えるとき、または同じフォルダーが二重に出るとき。
- 呼び出し先: `Array.prototype.find.call()`, `this._appendFolderItemToMenupopup()`
- 条件付き依存: `if ( menupopup.children.length == STATIC_MENUITEM_COUNT + PlacesUIUtils.maxRecentFolders )` → `menupopup.removeChild()`
- 参照: `PlacesUIUtils.maxRecentFolders`, `item.folderGuid`, `menuItem.hidden`, `menupopup.children`, `menupopup.children.length`, `menupopup.lastElementChild`, `this._folderMenuList.menupopup`

## onFolderMenuListCommand()
- 位置: async L932-992
- 役割: 「フォルダーを選ぶ」ならツリーを開閉し、それ以外では選択フォルダーへ項目を移す。
- 触るとき: 保存先の変更が反映されないとき、またはフォルダー選択のポップアップの流れを変えるとき。
- 呼び出し先: `this._element()`
- 条件付き依存: `if (aEvent.target.id == "editBMPanel_chooseFolderMenuItem")` → `this._getFolderMenuItem()`
- 条件付き依存: `if (menupopup.state == "closed")` → `this.toggleFolderTreeVisibility()`
- 条件付き依存: `if (!(menupopup.state == "closed"))` → `menupopup.addEventListener()`
- 条件付き依存: `if (!(menupopup.state == "closed"))` → `this.toggleFolderTreeVisibility()`
- 条件付き依存: `if (this._bookmarkState.parentGuid != containerGuid)` → `this._bookmarkState._parentGuidChanged()`
- 条件付き依存: `if (containerGuid == PlacesUtils.bookmarks.toolbarGuid)` → `this._autoshowBookmarksToolbar()`
- 条件付き依存: `if (!folderTreeRow.hidden)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( !selectedNode || PlacesUtils.getConcreteItemGuid(selectedNode) != containerGuid )` → `this._folderTree.selectItems()`
- 参照: `PlacesUtils.bookmarks.toolbarGuid`, `aEvent.target.id`, `folderTreeRow.hidden`, `menupopup.isNativeMenu`, `menupopup.state`, `this._bookmarkState._originalState.parentGuid`, `this._bookmarkState._originalState.title`, `this._bookmarkState.parentGuid`, `this._didChangeFolder`, `this._folderMenuList.menupopup`, `this._folderMenuList.selectedItem`, `this._folderMenuList.selectedItem.folderGuid`, `this._folderTree.selectedNode`, `this._paneInfo`

## _autoshowBookmarksToolbar()
- 位置: L994-1013
- 役割: 項目をブックマークツールバーへ入れたとき、ツールバーが隠れていれば一時的に表示する。
- 触るとき: ツールバーへ追加したのに表示されない、または never 設定を尊重しているか確かめるとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `Services.prefs.getCharPref()`, `document.getElementById()`, `setToolbarVisibility()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `placement.area`, `toolbar.collapsed`
- XPCOM: `Services.prefs`

## onFolderTreeSelect()
- 位置: L1015-1040
- 役割: ツリーで選んだフォルダーを保存先メニューへ反映し、新規フォルダーボタンの有効状態を更新する。
- 触るとき: ツリーで選んだフォルダーがメニューに出ない、または新規ボタンの有効・無効がおかしいとき。
- 呼び出し先: `PlacesUtils.getConcreteItemGuid()`, `folderItem.doCommand()`, `this._element()`, `this._getFolderMenuItem()`
- 参照: `selectedNode.title`, `this._element("folderTreeRow").hidden`, `this._element("newFolderButton").disabled`, `this._folderMenuList.selectedItem`, `this._folderMenuList.selectedItem.folderGuid`, `this._folderTree.insertionPoint`, `this._folderTree.selectedNode`

## _rebuildTagsSelectorList()
- 位置: async L1042-1088
- 役割: 全タグの一覧を作り直し、欄にあるタグにチェックを付け、選択位置を保つ。
- 触るとき: タグ一覧の内容や並び、チェック状態が正しくないとき。
- 呼び出し先: `[...this._allTags.values()].sort()`, `document.createDocumentFragment()`, `document.createXULElement()`, `elt.appendChild()`, `fragment.appendChild()`, `label.setAttribute()`, `tagsInField.includes()`, `tagsSelector.appendChild()`, `tagsSelector.dispatchEvent()`, `tagsSelector.hasChildNodes()`, `tagsSelector.removeChild()`, `this._allTags.values()`, `this._element()`, `this._getTagsArrayFromTagsInputField()`
- 条件付き依存: `if (tagsInField.includes(tag))` → `elt.setAttribute()`
- 条件付き依存: `if (selectedIndex >= 0 && tagsSelector.itemCount > 0)` → `Math.min()`
- 条件付き依存: `if (selectedIndex >= 0 && tagsSelector.itemCount > 0)` → `tagsSelector.ensureIndexIsVisible()`
- 参照: `sortedTags.length`, `tagsSelector.itemCount`, `tagsSelector.lastElementChild`, `tagsSelector.selectedIndex`, `tagsSelector.selectedItem.label`, `tagsSelectorRow.hidden`, `this._allTags`

## toggleTagsSelector()
- 位置: async L1090-1113
- 役割: タグ一覧の表示を切り替え、開くときは一覧を再構築して command リスナーを付ける。
- 触るとき: タグ一覧の開閉が動かないとき、またはイベントが二重に付くとき。
- 呼び出し先: `expander.classList.toggle()`, `this._element()`
- 条件付き依存: `if (tagsSelectorRow.hidden)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (tagsSelectorRow.hidden)` → `this._rebuildTagsSelectorList()`
- 条件付き依存: `if (tagsSelectorRow.hidden)` → `tagsSelector.addEventListener()`
- 条件付き依存: `if (!(tagsSelectorRow.hidden))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(tagsSelectorRow.hidden))` → `tagsSelector.removeEventListener()`
- 参照: `tagsSelectorRow.hidden`

## _getTagsArrayFromTagsInputField()
- 位置: L1121-1127
- 役割: タグ欄の値をカンマ区切りで分け、空の要素を除いた配列を返す。
- 触るとき: タグの区切りや空白の扱いを変えるとき、または余計な空タグが保存されるとき。
- 呼び出し先: `tags .trim()`, `tags .trim() .split()`, `tags .trim() .split(/\s*,\s*/) // Split on commas and remove spaces. .filter()`, `this._element()`
- 参照: `tag.length`, `this._element("tagsField").value`

## newFolder()
- 位置: async L1129-1157
- 役割: 挿入位置 (無ければメニューのフォルダー) にフォルダーを作り、ツリーで名前編集を始める。
- 触るとき: 新規フォルダーが想定の場所に作られない、または作成後の編集が始まらないとき。
- 呼び出し先: `PlacesTransactions.NewFolder()`, `PlacesTransactions.NewFolder({ parentGuid: ip.guid, title, index: await ip.getIndex(), }).transact()`, `PlacesUtils.asContainer()`, `ip.getIndex()`, `promise.catch()`, `this._element()`, `this._folderTree.columns.getFirstColumn()`, `this._folderTree.focus()`, `this._folderTree.selectItems()`, `this._folderTree.startEditing()`, `this.transactionPromises.push()`
- 参照: `PlacesUtils.asContainer(this._folderTree.selectedNode).containerOpen`, `PlacesUtils.bookmarks.menuGuid`, `console.error`, `ip.guid`, `this._element("newFolderButton").label`, `this._folderTree.insertionPoint`, `this._folderTree.selectedNode`, `this._folderTree.view.selection.currentIndex`

## handleEvent()
- 位置: L1160-1209
- 役割: パネル内の change、command、select、unload イベントを、対応する処理へ振り分ける。
- 触るとき: ある欄や項目を操作しても反応しないとき、どのイベントがどの処理に行くかを確かめるとき。
- 呼び出し先: `this._onFolderListSelected()`, `this.newFolder()`, `this.newFolder().catch()`, `this.onFolderMenuListCommand()`, `this.onFolderMenuListCommand(event).catch()`, `this.onKeywordFieldChange()`, `this.onLocationFieldChange()`, `this.onNamePickerChange()`, `this.onNamePickerChange().catch()`, `this.onTagsFieldChange()`, `this.toggleFolderTreeVisibility()`, `this.toggleTagsSelector()`, `this.toggleTagsSelector().catch()`, `this.toggleTagsSelectorItem()`, `this.uninitPanel()`
- 参照: `console.error`, `event.currentTarget.id`, `event.target`, `event.target.id`, `event.type`

## handlePlacesEvents()
- 位置: async L1211-1222
- 役割: Places の bookmark-title-changed を受けて、タイトルの表示を更新する。
- 触るとき: 別の場所でブックマーク名を変えたとき、パネルの表示が古いままになるとき。
- 条件付き依存: `if (this._paneInfo.isItem || this._paneInfo.isTag)` → `this._onItemTitleChange()`
- 参照: `event.guid`, `event.id`, `event.title`, `event.type`, `this._paneInfo.isItem`, `this._paneInfo.isTag`

## toggleTagsSelectorItem()
- 位置: L1224-1237
- 役割: 一覧のタグのチェックに合わせてタグ欄を書き換え、タグを更新する。
- 触るとき: 一覧のチェックをつけてもタグ欄に反映されない、または外れないとき。
- 呼び出し先: `item.toggleAttribute()`, `tags.indexOf()`, `tags.join()`, `this._element()`, `this._getTagsArrayFromTagsInputField()`, `this._updateTags()`
- 条件付き依存: `if (curTagIndex == -1)` → `tags.push()`
- 条件付き依存: `if (curTagIndex != -1)` → `tags.splice()`
- 参照: `item.label`, `this._element("tagsField").value`

## _initTagsField()
- 位置: L1239-1250
- 役割: URL か複数選択の共通タグから、タグ欄の初期値を作る。
- 触るとき: タグ欄に既存のタグが出ないとき、または複数選択時の初期値を変えるとき。
- 呼び出し先: `tags.join()`, `this._initTextField()`
- 条件付き依存: `if (this._paneInfo.isURI)` → `PlacesUtils.tagging.getTagsForURI()`
- 条件付き依存: `if (this._paneInfo.bulkTagging)` → `this._getCommonTags()`
- 参照: `this._paneInfo.bulkTagging`, `this._paneInfo.isURI`, `this._paneInfo.uri`, `this._tagsField`

## _onItemTitleChange()
- 位置: L1252-1274
- 役割: フォルダー名が変わったとき、保存先メニューと最近使ったフォルダーの表示を書き換える。
- 触るとき: 別で名前を変えたフォルダーの表示名が古いままのとき。
- 呼び出し先: `this._paneInfo.visibleRows.has()`
- 参照: `folder.folderGuid`, `folder.title`, `menuitem.folderGuid`, `menuitem.label`, `menupopup.children`, `this._folderMenuList.menupopup`, `this._recentFolders`

## bookmarkState()
- 位置: L1281-1283
- 役割: 現在の BookmarkState を返す。
- 触るとき: 保存時に状態を取り出す箇所 (呼び出し元) を追うとき。
- 参照: `this._bookmarkState`
