# browser/components/places/content/places.js

source: browser/components/places/content/places.js
source-hash: 08f6e3859bf2a9cbb57dd3dc33379bda888ce918
lines: 1646

## <module>
- 役割: ライブラリ(places の整理ウィンドウ)の本体。左のフォルダー一覧、右の内容一覧、検索欄、表示メニュー、インポート、エクスポート、バックアップと復元を扱う
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyScriptGetter()`, `window.addEventListener()`

## _initFolderTree()
- 位置: L52-54
- 役割: 左ペインに出すフォルダー一覧の place: クエリ(左ペイン用、項目除外、クエリ非展開)を設定する
- 触るとき: 左ペインに何を並べるかを変えるとき。excludeItems=1 なので個々のブックマークは出ない
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_LEFT_PANE_QUERY`, `this._places.place`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## selectLeftPaneBuiltIn()
- 位置: L63-102
- 役割: すべてのブックマーク、履歴、ダウンロード、タグの組み込み項目を左ペインで選んで開く。ブックマークのメニュー、ツールバー、未分類は階層として選び直す。未知の名前は例外を投げる
- 触るとき: 左ペインの組み込み項目を増やすとき。ここで未知として扱われた文字列は、次の階層の関数で place: URI か GUID として解釈される
- 呼び出し先: `PlacesUtils.asContainer()`, `this._places.selectItems()`, `this.selectLeftPaneContainerByHierarchy()`
- 参照: `PlacesUtils.asContainer(this._places.selectedNode).containerOpen`, `PlacesUtils.bookmarks.virtualMenuGuid`, `PlacesUtils.bookmarks.virtualToolbarGuid`, `PlacesUtils.bookmarks.virtualUnfiledGuid`, `PlacesUtils.virtualAllBookmarksGuid`, `PlacesUtils.virtualDownloadsGuid`, `PlacesUtils.virtualHistoryGuid`, `PlacesUtils.virtualTagsGuid`, `this._places.selectedNode`

## selectLeftPaneContainerByHierarchy()
- 位置: L115-148
- 役割: 階層の各要素を順に選んで開く。組み込み名、place: URI、GUID の順に解決し、途中の選択イベントは抑止する
- 触るとき: 初期表示やフォルダーを開く操作の後で、左ペインが期待した位置に来ないとき
- 呼び出し先: `PlacesUtils.asContainer()`, `[].concat()`, `container.substr()`, `this.selectLeftPaneBuiltIn()`
- 条件付き依存: `if (container.substr(0, 6) == "place:")` → `this._places.selectPlaceURI()`
- 条件付き依存: `if (!(container.substr(0, 6) == "place:"))` → `this._places.selectItems()`
- 参照: `PlacesUtils.asContainer(this._places.selectedNode).containerOpen`, `this._places.selectedNode`, `this._places.view.selection.selectEventsSuppressed`

## PO_init()
- 位置: L150-276
- 役割: ライブラリを開いたときの初期化。ダウンロード表示の登録、左右ペインのイベントの設定、初期項目の選択、検索と表示メニューの初期化、macOS 用のキー割り当て、コンテキストメニューの整理を行う
- 触るとき: 起動時に一度だけ行う配線を足すとき。window.arguments で開く項目が決まり、履歴を開くときは先頭の子も選ぶ
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
- 役割: load と unload を init と destroy に回し、command と AppCommand を ID で振り分けて、検索、インポート、エクスポート、バックアップ、復元、戻る、進むなどを実行する
- 触るとき: メニュー項目や AppCommand(戻る、進む、検索キー)の動作を追加・変更するとき
- 呼び出し先: `PlacesQueryBuilder.addRow()`, `PlacesSearchBox.findAll()`, `event.stopPropagation()`, `this.back()`, `this.backupBookmarks()`, `this.destroy()`, `this.exportBookmarks()`, `this.forward()`, `this.importFromBrowser()`, `this.importFromFile()`, `this.init()`, `this.onRestoreBookmarksFromFile()`, `this.saveSearch()`, `window.close()`
- 条件付き依存: `if (this._backHistory.length)` → `this.back()`
- 条件付き依存: `if (this._forwardHistory.length)` → `this.forward()`
- 参照: `event.command`, `event.target.id`, `event.type`, `this._backHistory.length`, `this._forwardHistory.length`

## PO_destroy()
- 位置: L347-347
- 役割: 後始末を行わない空の実装
- 触るとき: ウィンドウを閉じるときに解放すべきものが増えたら、ここに書く

## location()
- 位置: L350-352
- 役割: 現在表示中の place: URI を返す getter
- 触るとき: 戻る、進むの履歴と現在の表示先がずれていないか調べるとき
- 参照: `this._location`

## location()
- 位置: L354-392
- 役割: 表示先の URI を設定する。空または同じ値なら何もしない。前の URI を戻る履歴へ積み、進む履歴を消し、左ペインを選び直して、戻る、進むボタンの状態を更新する
- 触るとき: 戻る、進むの履歴が重複して積まれる、またはボタンの有効状態が合わないとき
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
- 役割: 戻る履歴の先頭を取り出して表示する。現在の URI は進む履歴の先頭へ積む
- 触るとき: 戻る操作の動作や、履歴の積み方を変えるとき
- 呼び出し先: `this._backHistory.shift()`, `this._forwardHistory.unshift()`
- 参照: `this._location`, `this.location`

## PO_forward()
- 位置: L403-408
- 役割: 進む履歴の先頭を取り出して表示する。現在の URI は戻る履歴の先頭へ積む
- 触るとき: 進む操作の動作を変えるとき
- 呼び出し先: `this._backHistory.unshift()`, `this._forwardHistory.shift()`
- 参照: `this._location`, `this.location`

## PO_onPlaceSelected()
- 位置: L422-458
- 役割: 左ペインの選択に合わせて右ペインの場所を切り替える。選択が前と同じなら検索欄や範囲は変えず、変わったときは検索欄を空にし、検索範囲と詳細欄を更新する
- 触るとき: 左ペインを選んだ後に検索欄の文字や右ペインの内容が前のまま残るとき
- 呼び出し先: `input.clear()`, `input.editor?.clearUndoRedo()`, `this._setSearchScopeForNode()`, `this.updateDetailsPane()`
- 参照: `ContentArea.currentPlace`, `PlacesSearchBox.searchFilter`, `node.uri`, `this._cachedLeftPaneSelectedURI`, `this._places.hasSelection`, `this._places.selectedNode`, `this.location`

## PO__setScopeForNode()
- 位置: L466-480
- 役割: 選ばれたノードに応じて検索範囲を履歴、ダウンロード、ブックマークのいずれかにする。それ以外はブックマークにする
- 触るとき: 左ペインを変えたときに検索の対象範囲が意図と違うとき
- 呼び出し先: `PlacesUtils.nodeIsHistoryContainer()`
- 条件付き依存: `if ( PlacesUtils.nodeIsHistoryContainer(aNode) || itemGuid == PlacesUtils.virtualHistoryGuid )` → `PlacesQueryBuilder.setScope()`
- 条件付き依存: `if (itemGuid == PlacesUtils.virtualDownloadsGuid)` → `PlacesQueryBuilder.setScope()`
- 条件付き依存: `if (!(itemGuid == PlacesUtils.virtualDownloadsGuid))` → `PlacesQueryBuilder.setScope()`
- 参照: `PlacesUtils.virtualDownloadsGuid`, `PlacesUtils.virtualHistoryGuid`, `aNode.bookmarkGuid`

## PO_onPlacesListClick()
- 位置: L490-506
- 役割: 左ペインのツリー本体での中クリックを、コンテナーの中身をまとめてタブで開く処理へ回す
- 触るとき: 左ペインの中クリックで開く範囲や動作を変えるとき
- 条件付き依存: `if (node)` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (middleClick && PlacesUtils.nodeIsContainer(node))` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 参照: `aEvent.button`, `aEvent.detail`, `aEvent.target.localName`, `this._places`, `this._places.selectedNode`

## PO_updateDetailsPane()
- 位置: L511-527
- 役割: 詳細欄が有効なときに限り、フォーカスがある一覧の選択を集めて詳細欄を更新する。入力欄にフォーカスがあるときは更新しない
- 触るとき: 詳細欄が選択に追従しない、または入力中の値が消えるおそれがあるとき
- 呼び出し先: `PlacesUIUtils.getViewForNode()`
- 条件付き依存: `if (view)` → `this._fillDetailsPane()`
- 参照: `ContentArea.currentViewOptions.showDetailsPane`, `document.activeElement`, `view.selectedNode`, `view.selectedNodes`

## openFlatContainer()
- 位置: L535-542
- 役割: フラット表示でコンテナーが開かれたとき、ブックマークなら親を開いてその項目を選び、クエリなら place: URI を選ぶ
- 触るとき: フラット表示でフォルダーを開いた後の遷移先を変えるとき
- 条件付き依存: `if (aContainer.bookmarkGuid)` → `PlacesUtils.asContainer()`
- 条件付き依存: `if (aContainer.bookmarkGuid)` → `this._places.selectItems()`
- 条件付き依存: `if (!(aContainer.bookmarkGuid))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(aContainer))` → `this._places.selectPlaceURI()`
- 参照: `PlacesUtils.asContainer(this._places.selectedNode).containerOpen`, `aContainer.bookmarkGuid`, `aContainer.uri`, `this._places.selectedNode`

## PO_getCurrentOptions()
- 位置: L549-552
- 役割: 右ペインの現在の結果ルートのクエリオプションを返す
- 触るとき: 右ペインの検索や並び替えが、どの種類のクエリを前提にしているかを確かめるとき
- 呼び出し先: `PlacesUtils.asQuery()`
- 参照: `ContentArea.currentView.result.root`, `PlacesUtils.asQuery(ContentArea.currentView.result.root) .queryOptions`

## PO_importFromBrowser()
- 位置: L558-563
- 役割: 他のブラウザからの移行ウィザードを、places の入口を示して開く
- 触るとき: 移行ウィザードの入口の扱いや計測を変えるとき
- 呼び出し先: `MigrationUtils.showMigrationWizard()`
- 参照: `MigrationUtils.MIGRATION_ENTRYPOINTS.PLACES`

## PO_importFromFile()
- 位置: L568-588
- 役割: HTML ファイルを選ばせ、選ばれたファイルの URL を BookmarkHTMLUtils に渡してブックマークを読み込む
- 触るとき: ブックマークの HTML インポートの入口や、対象ファイルの種類を変えるとき
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesUIUtils.promptLocalization.formatValueSync()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterHTML`, `Ci.nsIFilePicker.modeOpen`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback_done()
- 位置: L570-577
- 役割: ファイルが選ばれたら BookmarkHTMLUtils.importFromURL を呼ぶ。キャンセルなら何もしない。失敗は console.error に出す
- 触るとき: インポートが始まらない、または失敗が見えないときに見る
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel && fp.fileURL)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel && fp.fileURL)` → `BookmarkHTMLUtils.importFromURL(fp.fileURL.spec).catch()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel && fp.fileURL)` → `BookmarkHTMLUtils.importFromURL()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `console.error`, `fp.fileURL`, `fp.fileURL.spec`
- XPCOM: `nsIFilePicker`

## PO_exportBookmarks()
- 位置: L593-614
- 役割: 保存先を選ばせ、ブックマークを HTML として書き出す。既定のファイル名は bookmarks.html
- 触るとき: 書き出しの形式や既定の名前を変えるとき
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesUIUtils.promptLocalization.formatValueSync()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterHTML`, `Ci.nsIFilePicker.modeSave`, `fp.defaultString`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback_done()
- 位置: L595-602
- 役割: 保存先が決まったら BookmarkHTMLUtils.exportToFile を呼ぶ。キャンセル時は何もしない
- 触るとき: 書き出しが行われない、または失敗が見えないときに見る
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `BookmarkHTMLUtils.exportToFile(fp.file.path).catch()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `BookmarkHTMLUtils.exportToFile()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `console.error`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## PO_populateRestoreMenu()
- 位置: L619-679
- 役割: 復元メニューの既存の項目を消し、利用できるバックアップごとに日付、サイズ、件数を並べた項目を作る。項目は「ファイルから」の前に入れる
- 触るとき: バックアップの一覧に出す情報を変えるとき。件数は取得できたときだけ付く
- 呼び出し先: `DownloadUtils.convertByteUnits()`, `IOUtils.stat()`, `PathUtils.filename()`, `PlacesBackups.getBackupFiles()`, `PlacesBackups.getBookmarkCountForFile()`, `PlacesBackups.getDateForFile()`, `PlacesUtils.getFormattedString()`, `dateFormatter.format()`, `document.createXULElement()`, `document.getElementById()`, `m.addEventListener()`, `m.setAttribute()`, `restorePopup.firstChild.remove()`, `restorePopup.insertBefore()`, `this.onRestoreMenuItemClick()`
- 条件付き依存: `if (count != null)` → `document.l10n.formatMessages()`
- 条件付き依存: `if (count != null)` → `msg.attributes.find()`
- 参照: `(await IOUtils.stat(file)).size`, `Services.intl.DateTimeFormat`, `attr.name`, `backupFiles.length`, `msg.attributes.find( attr => attr.name === "value" )?.value`, `restorePopup.childNodes.length`
- XPCOM: `Services.intl`

## onRestoreMenuItemClick()
- 位置: async L686-695
- 役割: メニューで選ばれた項目のファイル名に一致するバックアップを探し、見つかれば復元を始める
- 触るとき: 復元メニューの項目と実際のファイルがずれて、別のバックアップが復元されないか確かめるとき
- 呼び出し先: `PathUtils.filename()`, `PlacesBackups.getBackupFiles()`, `aMenuItem.getAttribute()`
- 条件付き依存: `if (PathUtils.filename(backupFilePath) == backupName)` → `PlacesOrganizer.restoreBookmarksFromFile()`

## PO_onRestoreBookmarksFromFile()
- 位置: L701-720
- 役割: ファイル選択ダイアログを開き、JSON 系のファイルを選ばせる。初期の場所はデスクトップ
- 触るとき: ファイルからの復元で選べる形式や、初期の場所を変えるとき
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.dirsvc.get()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeOpen`, `fp.displayDirectory`, `window.browsingContext`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `nsIFilePicker` / `@mozilla.org/filepicker;1` / `Services.dirsvc`

## fpCallback()
- 位置: L704-708
- 役割: 選ばれたファイルのパスを restoreBookmarksFromFile に渡す。キャンセル時は何もしない
- 触るとき: ファイルを選んだ後の復元の流れを追うとき
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `this.restoreBookmarksFromFile()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## PO_restoreBookmarksFromFile()
- 位置: L728-756
- 役割: 拡張子が json か jsonlz4 かを確かめ、確認で了承されたら既存のブックマークを置き換えて読み込む。読み込みに失敗すると解析エラーを表示する
- 触るとき: 復元できるファイルの条件や確認の文言を変えるとき。置き換えのため、既存のブックマークは消える
- 呼び出し先: `BookmarkJSONUtils.importFromFile()`, `PlacesOrganizer._showErrorAlert()`, `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.prompt.confirm()`, `aFilePath.toLowerCase()`, `aFilePath.toLowerCase().endsWith()`
- 条件付き依存: `if ( !aFilePath.toLowerCase().endsWith("json") && !aFilePath.toLowerCase().endsWith("jsonlz4") )` → `this._showErrorAlert()`
- XPCOM: `Services.prompt`

## PO__showErrorAlert()
- 位置: L758-764
- 役割: ローカライズされたタイトルと本文を使い、エラーのアラートを表示する
- 触るとき: 新しいエラーの文言を出すとき。この関数に渡す l10n ID を足す
- 呼び出し先: `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.prompt.alert()`
- XPCOM: `Services.prompt`

## PO_backupBookmarks()
- 位置: L771-794
- 役割: デスクトップを既定の場所にして、日付入りの既定名で保存ダイアログを開く。保存は JSON 形式
- 触るとき: バックアップの既定の場所や名前の決まり方を変えるとき
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `PlacesBackups.getFilenameForDate()`, `PlacesUIUtils.promptLocalization.formatValuesSync()`, `Services.dirsvc.get()`, `fp.appendFilter()`, `fp.init()`, `fp.open()`
- 参照: `Ci.nsIFile`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeSave`, `fp.defaultExtension`, `fp.defaultString`, `fp.displayDirectory`, `window.browsingContext`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `nsIFilePicker` / `@mozilla.org/filepicker;1` / `Services.dirsvc`

## fpCallback_done()
- 位置: L774-781
- 役割: 保存先が決まったら PlacesBackups.saveBookmarksToJSONFile で保存する。失敗は console.error に出す
- 触るとき: バックアップが保存されない、または失敗が見えないときに見る
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `PlacesBackups.saveBookmarksToJSONFile(fp.file.path).catch()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `PlacesBackups.saveBookmarksToJSONFile()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `console.error`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## PO__fillDetailsPane()
- 位置: L796-879
- 役割: 詳細欄を選択内容に合わせる。一つだけ選ばれていれば編集パネルを初期化し、複数の URI なら共通の欄だけを出し、それ以外は件数を表示する。同じ項目を編集中なら何もしない
- 触るとき: 詳細欄に出す欄や件数の文言を変えるとき。編集中の項目を作り直さないための早期の return がある
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
- 役割: 検索欄の要素を返す getter
- 触るとき: 検索欄の要素を参照している箇所を追うとき
- 呼び出し先: `document.getElementById()`

## folders()
- 位置: L906-911
- 役割: 検索対象のフォルダーを返す getter。未設定なら利用者用のブックマークのルートを使う
- 触るとき: ブックマーク検索の対象になるフォルダーを変えるとき
- 参照: `PlacesUtils.bookmarks.userContentRoots`, `this._folders`, `this._folders.length`

## folders()
- 位置: L912-914
- 役割: 検索対象のフォルダーを設定する setter
- 触るとき: 検索範囲を外から設定する箇所を追うとき
- 参照: `this._folders`

## search()
- 位置: L924-979
- 役割: 検索文字列を現在の範囲(ブックマーク、履歴、ダウンロード)に適用する。空文字なら左ペインの内容を再表示する。履歴でない結果から検索するときは、履歴向けのクエリを作り直す。最後に詳細欄を更新する
- 触るとき: 検索結果が出ない、または範囲と違う結果が出るとき。履歴の検索では所要時間と回数を計測している
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
- 役割: 現在の検索範囲に応じて、履歴、ダウンロード、ブックマークのいずれかを検索範囲に設定し、検索欄にフォーカスを移す
- 触るとき: すべてを検索する操作やショートカットで、初期の検索範囲を変えるとき
- 呼び出し先: `PlacesQueryBuilder.setScope()`, `this.focus()`
- 参照: `this.filterCollection`

## updatePlaceholder()
- 位置: L1002-1015
- 役割: 検索欄の案内文を、現在の範囲(履歴、ダウンロード、ブックマーク)に合わせて差し替える
- 触るとき: 検索範囲を増やすときに、案内文の ID を足す
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this.filterCollection`, `this.searchFilter`

## filterCollection()
- 位置: L1022-1024
- 役割: 検索欄の collection 属性から現在の検索範囲の名前を返す getter
- 触るとき: 検索範囲の判定を読む箇所を追うとき
- 呼び出し先: `this.searchFilter.getAttribute()`

## filterCollection()
- 位置: L1025-1032
- 役割: 検索範囲の属性を設定し、変わっていれば案内文を更新する setter
- 触るとき: 検索範囲を切り替えたときに案内文が追従しないとき
- 呼び出し先: `this.searchFilter.setAttribute()`, `this.updatePlaceholder()`
- 参照: `this.filterCollection`

## focus()
- 位置: L1037-1039
- 役割: 検索欄にフォーカスを移す
- 触るとき: 検索欄へ移動するショートカットの動きを変えるとき
- 呼び出し先: `this.searchFilter.focus()`

## init()
- 位置: L1044-1049
- 役割: 検索欄の検索イベント(MozInputSearch:search)に検索処理を結び付け、案内文を初期化する
- 触るとき: 検索欄で検索を確定したときの処理を追うとき
- 呼び出し先: `this.search()`, `this.searchFilter.addEventListener()`, `this.updatePlaceholder()`
- 参照: `e.target.value`

## value()
- 位置: L1056-1058
- 役割: 検索欄の文字を返す getter
- 触るとき: 検索文字列を読む箇所を追うとき
- 参照: `this.searchFilter.value`

## value()
- 位置: L1059-1061
- 役割: 検索欄の文字を設定する setter
- 触るとき: 検索欄の文字を外から書き換える箇所を追うとき
- 参照: `this.searchFilter.value`

## updateTelemetry()
- 位置: L1064-1089
- 役割: 開いたリンクに履歴のものが含まれるかで、ブックマーク用か履歴用の計測を記録する。累積の検索回数も、ここでリセットする
- 触るとき: ライブラリからリンクを開いたときの計測値がずれるとき
- 呼び出し先: `Glean.library.cumulativeHistorySearches.accumulateSingleSample()`, `Glean.library.link.history.add()`, `PlacesUtils.nodeIsBookmark()`, `urlsOpened.filter()`
- 条件付き依存: `if (!historyLinks.length)` → `Glean.library.cumulativeBookmarkSearches.accumulateSingleSample()`
- 条件付き依存: `if (!historyLinks.length)` → `Glean.library.link.bookmarks.add()`
- 参照: `PlacesSearchBox.cumulativeBookmarkSearches`, `PlacesSearchBox.cumulativeHistorySearches`, `historyLinks.length`, `link.isBookmark`, `urlsOpened.length`

## setScope()
- 位置: L1107-1133
- 役割: 検索範囲(履歴、ブックマーク、ダウンロード)を検索欄と検索対象のフォルダーに反映し、検索文字列が残っていれば再検索する
- 触るとき: 左ペインを切り替えたときや、すべてを検索したときに検索範囲が変わらないとき
- 条件付き依存: `if (searchStr)` → `PlacesSearchBox.search()`
- 参照: `PlacesSearchBox.filterCollection`, `PlacesSearchBox.folders`, `PlacesSearchBox.searchFilter.value`, `PlacesUtils.bookmarks.userContentRoots`

## init()
- 位置: L1140-1172
- 役割: 表示メニューの列一覧と並び替えメニューに、コマンドと表示直前の処理を結び付ける
- 触るとき: 表示メニューの項目を増やすとき
- 呼び出し先: `columnsPopup.addEventListener()`, `document.querySelector()`, `event.stopPropagation()`, `sortPopup.addEventListener()`, `this.fillWithColumns()`, `this.populateSortMenu()`, `this.setSortColumn()`, `this.showHideColumn()`
- 参照: `event.target`, `event.target.column`, `event.target.id`

## VM__clean()
- 位置: L1195-1226
- 役割: メニューに動的に作られた項目を、開始 ID と終了 ID の間だけ消す。指定が無ければ全部消す。新しい項目を挿入する位置を返す
- 触るとき: 動的に作るメニューの掃除範囲を変えるとき。開始要素が無いと、存在確認の前に TypeError が出る(要確認)
- 呼び出し先: `popup.firstChild.remove()`, `popup.hasChildNodes()`
- 条件付き依存: `if (startID)` → `document.getElementById()`
- 条件付き依存: `if (endID)` → `document.getElementById()`
- 条件付き依存: `if (startID)` → `popup.removeChild()`
- 参照: `endElement.parentNode`, `startElement.nextSibling`, `startElement.parentNode`

## VM_fillWithColumns()
- 位置: L1247-1296
- 役割: 列の一覧を、ラジオまたはチェックボックスの項目としてメニューに入れる。並び替えの列には印を付け、表示中の列は選択状態にし、主の列は外せないようにする
- 触るとき: 列メニューの項目の印や無効化の条件を変えるとき
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
- 役割: 並び替えメニューに列の一覧を入れ、現在の並び順に合わせて「並べ替えなし」「昇順」「降順」の印を付ける
- 触るとき: 並び替えメニューの印が現在の並びと合わないとき
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
- 役割: メニューで選ばれた列の表示を切り替える。隣の区切り(splitter)も同じ状態に合わせる
- 触るとき: 列を隠した後に区切りだけ残る、といった表示の食い違いを調べるとき
- 呼び出し先: `element.hasAttribute()`
- 参照: `column.hidden`, `column.nextSibling`, `element.column`, `splitter.hidden`, `splitter.localName`

## VM__getSortColumn()
- 位置: L1360-1371
- 役割: sortDirection 属性が昇順か降順の列を探して返す。無ければ null を返す
- 触るとき: 現在の並び替えの列を使う箇所を追うとき
- 呼び出し先: `cols.getColumnAt()`, `column.getAttribute()`, `document.getElementById()`
- 参照: `cols.count`, `cols.getColumnAt(i).element`, `content.columns`

## VM_setSortColumn()
- 位置: L1385-1434
- 役割: 並び替えを設定する。列と向きが両方無ければ並べ替えなし。列の既定の向きは、文字の列では昇順、日付と回数の列では降順。無効な列は例外を投げる
- 触るとき: 列ごとの既定の並び順を変えるとき、または並び替えの指定が効かないときに見る
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
- 役割: 右ペインの表示先の要素を取得し、ツリーを初期化してから表示オプションを適用する
- 触るとき: 右ペインの初期化の順序を変えるとき
- 呼び出し先: `ContentTree.init()`, `document.getElementById()`, `this._setupView()`
- 参照: `this._box`, `this._toolbar`

## CA_getContentViewForQueryString()
- 位置: L1456-1472
- 役割: クエリ文字列に専用の表示が登録されていればそれを返す。関数で登録されたものは初回に呼んで実体を作る。無ければ既定のツリーを返す
- 触るとき: ダウンロードのような特別な表示を差し込んだとき、その問い合わせ先を確かめる
- 呼び出し先: `console.error()`, `this._specialViews.has()`
- 条件付き依存: `if (this._specialViews.has(aQueryString))` → `this._specialViews.get()`
- 条件付き依存: `if (typeof view == "function")` → `view()`
- 条件付き依存: `if (typeof view == "function")` → `this._specialViews.set()`
- 参照: `ContentTree.view`

## CA_setContentViewForQueryString()
- 位置: L1487-1503
- 役割: クエリ文字列に対する専用の表示と、そのオプションを登録する。引数が不正なら例外を投げる
- 触るとき: 専用の表示を新しく登録するとき
- 呼び出し先: `this._specialViews.set()`

## currentView()
- 位置: L1505-1510
- 役割: 右ペインで表示中のパネル(非表示でない最初の子)に対応するビューを返す getter
- 触るとき: 右ペインでどのビューが見えているかを調べるとき
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `[...this._box.children].filter()`
- 参照: `child.hidden`, `this._box.children`

## currentView()
- 位置: L1511-1523
- 役割: 表示するビューを切り替える setter。元のビューを隠して新しいビューを表示し、フォーカスが元のビューにあれば新しいビューへ移す
- 触るとき: 右ペインの表示を切り替えた後にフォーカスが迷子になるとき
- 条件付き依存: `if (document.activeElement == oldView.associatedElement)` → `aNewView.associatedElement.focus()`
- 参照: `aNewView.associatedElement.hidden`, `document.activeElement`, `oldView.associatedElement`, `oldView.associatedElement.hidden`, `this.currentView`

## currentPlace()
- 位置: L1525-1527
- 役割: 表示中のビューの place を返す getter
- 触るとき: 右ペインが今どのクエリを表示しているかを調べるとき
- 参照: `this.currentView.place`

## currentPlace()
- 位置: L1528-1538
- 役割: クエリ文字列に対応するビューを選び、必要なら表示を切り替えて、表示オプションを適用する setter
- 触るとき: 左ペインを変えたときに右ペインの表示が切り替わらないとき
- 呼び出し先: `this.getContentViewForQueryString()`
- 条件付き依存: `if (oldView != newView)` → `this._setupView()`
- 参照: `newView.active`, `newView.place`, `oldView.active`, `this.currentView`

## CA__setupView()
- 位置: L1543-1561
- 役割: 詳細欄の表示の有無と、ツールバーの各ボタンの表示を、現在のビューのオプションに合わせる
- 触るとき: ビューごとにツールバーの項目を出し分けたいとき
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (elt.id == "placesMenu")` → `options.toolbarSet.includes()`
- 条件付き依存: `if (!(elt.id == "placesMenu"))` → `options.toolbarSet.includes()`
- 参照: `detailsPane.hidden`, `elt.childNodes`, `elt.hidden`, `elt.id`, `menuElt.hidden`, `menuElt.id`, `options.showDetailsPane`, `this._toolbar.childNodes`, `this.currentViewOptions`

## currentViewOptions()
- 位置: L1569-1579
- 役割: ツリーの既定オプションに、現在の place に登録された専用オプションを上書きして返す getter
- 触るとき: 専用の表示で詳細欄やツールバーの設定を変えたいとき
- 呼び出し先: `this._specialViews.has()`
- 条件付き依存: `if (this._specialViews.has(this.currentPlace))` → `this._specialViews.get()`
- 参照: `ContentTree.viewOptions`, `this.currentPlace`

## focus()
- 位置: L1581-1583
- 役割: 現在のビューの要素にフォーカスを移す
- 触るとき: ライブラリを開いたときや検索後に、フォーカスの行き先を変えたいとき
- 呼び出し先: `this.currentView.associatedElement.focus()`

## CT_init()
- 位置: L1587-1593
- 役割: ツリーの要素を取得し、キー入力とクリックのイベントを自分に結び付ける
- 触るとき: ツリーでのクリックやキー操作を増やすとき
- 呼び出し先: `document .querySelector()`, `document .querySelector("#placeContent > treechildren") .addEventListener()`, `document.getElementById()`, `this.view.addEventListener()`
- 参照: `this._view`

## view()
- 位置: L1595-1597
- 役割: 右ペインのツリー要素を返す getter
- 触るとき: 右ペインのツリー要素を参照している箇所を追うとき
- 参照: `this._view`

## viewOptions()
- 位置: L1599-1605
- 役割: ツリーの既定の表示オプション(詳細欄を出すかどうか、ツールバーの項目の一覧)を、項目を増減できない封じたオブジェクトとして返す getter
- 触るとき: 既定のツールバーの項目を変えるとき
- 呼び出し先: `Object.seal()`

## CT_openSelectedNode()
- 位置: L1607-1610
- 役割: 選ばれたノードを、イベントの修飾キーなどに応じた方法で開く
- 触るとき: ノードを開くときの方法(タブやウィンドウ)の判定を変えるとき
- 呼び出し先: `PlacesUIUtils.openNodeWithEvent()`
- 参照: `this.view`, `view.selectedNode`

## handleEvent()
- 位置: L1612-1621
- 役割: click と keypress を、それぞれ onClick と onKeyPress に振り分ける
- 触るとき: ツリーで扱うイベントの種類を増やすとき
- 呼び出し先: `this.onClick()`, `this.onKeyPress()`
- 参照: `event.type`

## CT_onClick()
- 位置: L1623-1638
- 役割: 選ばれた URL のノードは、ダブルクリックか中クリックで開く。コンテナーは中クリックでまとめてタブに開く
- 触るとき: ツリーのクリックで開く条件を変えるとき
- 条件付き依存: `if (node)` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node) && (doubleClick || middleClick))` → `this.openSelectedNode()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsURI(node) && (doubleClick || middleClick)))` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (middleClick && PlacesUtils.nodeIsContainer(node))` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 参照: `aEvent.button`, `aEvent.detail`, `this.view`, `this.view.selectedNode`

## CT_onKeyPress()
- 位置: L1640-1644
- 役割: Enter キーで選ばれたノードを開く
- 触るとき: キー操作の割り当てを変えるとき
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_RETURN)` → `this.openSelectedNode()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.keyCode`
