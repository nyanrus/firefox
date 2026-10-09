# browser/components/places/content/controller.js

source: browser/components/places/content/controller.js
source-hash: 1faf824a5f18446ef453b2e03a1e0ca5b48eadf1
lines: 1782

## <module>
- 役割: 場所 (Places) の選択・コマンド・クリップボード・DnD を司るコントローラーと挿入位置オブジェクトを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyServiceGetter()`

## PlacesInsertionPoint()
- 位置: L33-45
- 役割: 親フォルダー GUID、挿入位置、向き、タグ名を持つ挿入点オブジェクトを作る。
- 触るとき: 貼り付けや DnD の挿入先を新しい情報で表すとき、またはタグへの挿入の扱いを変えるとき。
- 参照: `Ci.nsITreeView.DROP_ON`, `PlacesUtils.bookmarks.DEFAULT_INDEX`, `this._index`, `this.dropNearNode`, `this.guid`, `this.orientation`, `this.tagName`
- XPCOM: `nsITreeView`

## index()
- 位置: L48-50
- 役割: 挿入位置のインデックスを内部の _index に設定する。
- 触るとき: 挿入位置を後から差し替える箇所で、値がどこへ入るかを追うとき。
- 参照: `this._index`

## getIndex()
- 位置: async L52-62
- 役割: 近いノードが指定されていればその位置から挿入インデックスを計算し、無ければ _index を返す。
- 触るとき: 並べ替えや DROP_BEFORE/AFTER で挿入位置がずれるとき。
- 条件付き依存: `if (this.dropNearNode)` → `PlacesUtils.bookmarks.fetch()`
- 参照: `( await PlacesUtils.bookmarks.fetch(this.dropNearNode.bookmarkGuid) ).index`, `Ci.nsITreeView.DROP_BEFORE`, `this._index`, `this.dropNearNode`, `this.dropNearNode.bookmarkGuid`, `this.orientation`
- XPCOM: `nsITreeView`

## isTag()
- 位置: L64-66
- 役割: 挿入先がタグかどうか (tagName が文字列か) を返す。
- 触るとき: タグへの貼り付けだけ許可・禁止を分けたいとき。
- 参照: `this.tagName`

## PlacesController()
- 位置: L73-83
- 役割: ビューを保持し、プロファイル名と ForgetAboutSite を遅延取得するコントローラーを作る。
- 触るとき: コントローラーの生成時に読み込まれる依存を増やすとき。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("ProfD", Ci.nsIFile).leafName`, `this._view`
- XPCOM: [`nsIFile`](../../shell/nsIShellService.idl.md) / `Services.dirsvc`

## PC_LosingOwnership()
- 位置: L99-101
- 役割: クリップボードの所有を失ったとき、切り取り済みノードの一覧を空にする。
- 触るとき: 切り取りの表示が残ったまま貼り付けできてしまうとき。
- 参照: `this.cutNodes`

## PC_terminate()
- 位置: L103-105
- 役割: コントローラー破棄時にクリップボードの所有を解放する。
- 触るとき: ツリーを閉じたあとにクリップボードの状態が残るとき。
- 呼び出し先: `this._releaseClipboardOwnership()`

## PC_supportsCommand()
- 位置: L107-127
- 役割: 無効化されていなければ、対応するコマンド名 (cmd_* と placesCmd_*) かどうかを判定する。
- 触るとき: 新しいコマンドを Places に通すとき、または無効な操作が残っているとき。
- 呼び出し先: `aCommand.substr()`
- 参照: `CMD_PREFIX.length`, `this.disableUserActions`

## PC_isCommandEnabled()
- 位置: L129-236
- 役割: 選択内容、挿入点、クリップボードの状態から、各コマンドを有効にするかを返す。
- 触るとき: メニュー項目がグレーのまま、または有効すぎるとき。コマンドごとの条件を調べる入口。
- 呼び出し先: `PlacesUIUtils.isFolderReadOnly()`, `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.isRootItem()`, `PlacesUtils.nodeIsBookmark()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsQueryGeneratedFolder()`, `PlacesUtils.nodeIsTagQuery()`, `PlacesUtils.nodeIsURI()`, `Services.clipboard.hasDataMatchingFlavors()`, `aCommand.endsWith()`, `this._hasRemovableSelection()`, `this._view.selectedNodes.some()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `PlacesTransactions.topRedoEntry`, `PlacesTransactions.topUndoEntry`, `PlacesUIUtils.PLACES_FLAVORS`, `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_URL`, `PlacesUtils.asQuery(this._view.result.root).queryOptions .excludeItems`, `ip.isTag`, `node.itemId`, `node.parent`, `rootNode.childCount`, `rootNode.containerOpen`, `this._view.hasSelection`, `this._view.insertionPoint`, `this._view.result.root`, `this._view.result.sortingMode`, `this._view.selType`, `this._view.selectedNode`, `this._view.selectedNodes`
- XPCOM: `nsIClipboard` / [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.clipboard`

## PC_doCommand()
- 位置: L238-328
- 役割: コマンド名に応じて、取り消し、切り取り、コピー、貼り付け、削除、開く、作成などの処理へ振り分ける。
- 触るとき: コマンドを押したときに実行される処理を追うとき、または新しい操作を配線するとき。
- 呼び出し先: `PlacesTransactions.redo()`, `PlacesTransactions.redo().catch()`, `PlacesTransactions.undo()`, `PlacesTransactions.undo().catch()`, `PlacesUIUtils.openNodeIn()`, `PlacesUIUtils.showBookmarkPagesDialog()`, `Services.io.newURI()`, `this._view.selectedNodes.map()`, `this.copy()`, `this.cut()`, `this.forgetAboutThisSite()`, `this.forgetAboutThisSite().catch()`, `this.newItem()`, `this.newItem("bookmark").catch()`, `this.newItem("folder").catch()`, `this.newSeparator()`, `this.newSeparator().catch()`, `this.paste()`, `this.paste().catch()`, `this.remove()`, `this.remove("Remove Selection").catch()`, `this.selectAll()`, `this.showBookmarkPropertiesForSelection()`, `this.showInFolder()`, `this.sortFolderByName()`, `this.sortFolderByName().catch()`
- 参照: `console.error`, `node.title`, `node.uri`, `this._lastRemoveOperationFingerprint`, `this._view`, `this._view.selectedNode`, `this._view.selectedNode.bookmarkGuid`, `window.top`
- XPCOM: `Services.io`

## PC_onEvent()
- 位置: L330-330
- 役割: 何もしない (イベント処理の空の受け口)。
- 触るとき: コントローラーへ送られるイベントを追加する必要があるかを確認するとき。

## _hasRemovableSelection()
- 位置: L342-365
- 役割: 選択範囲のどれかがルートか削除不可の項目なら false を返す。
- 触るとき: 削除や切り取りが無効になる条件を変えるとき、または削除できない項目が消えてしまうとき。
- 呼び出し先: `PlacesUIUtils.canUserRemove()`
- 参照: `nodes.length`, `ranges.length`, `this._view.removableSelectionRanges`, `this._view.result.root`

## _isRepeatedRemoveOperation()
- 位置: L373-385
- 役割: 直前の削除と同じ選択かを、選択ノードのハッシュで判定し、今回の指紋を保存する。
- 触るとき: 同じ項目への削除が二重に実行される、または連続削除が止まるとき。
- 呼び出し先: `PlacesUtils.sha256()`, `this._view.selectedNodes .map()`, `this._view.selectedNodes .map(n => n.bookmarkGuid || (n.pageGuid || n.uri) + n.time) .join()`
- 参照: `n.bookmarkGuid`, `n.pageGuid`, `n.time`, `n.uri`, `this._lastRemoveOperationFingerprint`

## _buildSelectionMetadata()
- 位置: L405-407
- 役割: 選択中の各ノードについてメタデータを配列にまとめる。
- 触るとき: コンテキストメニューの表示条件に使うデータの元を追うとき。
- 呼び出し先: `this._selectionMetadataForNode()`, `this._view.selectedNodes.map()`

## _selectionMetadataForNode()
- 位置: L409-449
- 役割: 1 ノードの種類 (リンク、ブックマーク、フォルダー、クエリ、区切り、タグの子など) を判定してフラグを立てる。
- 触るとき: コンテキストメニューの node-type 判定の種類を増やすとき、またはクエリの種類で誤判定が出るとき。
- 呼び出し先: `PlacesUtils.nodeIsBookmark()`
- 条件付き依存: `if (node.parent)` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsBookmark(node))` → `PlacesUtils.nodeIsTagQuery()`
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_DATE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_DATE_SITE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_SITE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_TAGS_ROOT`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER_SHORTCUT`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `PlacesUtils.asQuery(node.parent).queryOptions.resultType`, `node.parent`, `node.type`, `nodeData.folder`, `nodeData.link`, `nodeData.link_bookmark`, `nodeData.link_bookmark_tag`, `nodeData.query`, `nodeData.query_day`, `nodeData.query_host`, `nodeData.query_tag`, `nodeData.separator`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## _shouldShowMenuItem()
- 位置: L461-521
- 役割: メニュー項目の selection-type と node-type などの属性から、その項目を出すかを判定する。
- 触るとき: メニュー項目が出たり消えたりする条件を属性で変えるとき、または想定外の項目が出るとき。
- 呼び出し先: `PlacesUIUtils.shouldHideOpenMenuItem()`, `aMenuItem.getAttribute()`, `attr.split()`, `rules.some()`, `selectionTypes.includes()`, `selectiontype.split()`
- 条件付き依存: `if (count == 0)` → `selectionTypes.includes()`
- 条件付き依存: `if (count == 0)` → `this._selectionMetadataForNode()`
- 条件付き依存: `if (attr)` → `attr.split()`
- 条件付き依存: `if (attr)` → `aMetaData.some()`
- 条件付き依存: `if (attr)` → `rules.some()`
- 条件付き依存: `if (attr)` → `aMetaData.every()`
- 参照: `aMetaData.length`, `this._view.result.root`

## buildContextMenu()
- 位置: L567-699
- 役割: 項目の属性と選択内容を照らして各項目の表示と有効状態を決め、区切り線と削除・作成の文言を更新する。
- 触るとき: hide-if-no-insertion-point や selection-type など、右クリックメニュー項目の属性を追加・変更して出し分けを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.getElementById()`, `document.l10n.setAttributes()`, `item.getAttribute()`, `this._buildSelectionMetadata()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.contentsharing.enabled") && selectedNode )` → `PlacesUtils.asContainer()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.contentsharing.enabled") && selectedNode )` → `PlacesUtils.hasChildURIs()`
- 条件付き依存: `if (item.localName != "menuseparator")` → `item.getAttribute()`
- 条件付き依存: `if (item.localName != "menuseparator")` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (item.localName != "menuseparator")` → `this._shouldShowMenuItem()`
- 条件付き依存: `if (item.id === "placesContext_deleteBookmark")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (item.id === "placesContext_deleteFolder")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (usableItemCount > 0)` → `document.getElementById()`
- 条件付き依存: `if (!menuItem.hidden)` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (PlacesUtils.nodeIsContainer(containerToUse))` → `PlacesUtils.hasChildURIs()`
- 参照: `PlacesUIUtils.loadBookmarksInBackground`, `PlacesUIUtils.loadBookmarksInTabs`, `aPopup.children`, `aPopup.children.length`, `ip.isTag`, `item.disabled`, `item.hidden`, `item.id`, `item.localName`, `menuItem.disabled`, `menuItem.hidden`, `metadata.length`, `separator.hidden`, `this._view.insertionPoint`, `this._view.result.root`, `this._view.selectedNode`, `this._view.selectedNode.parent`, `this._view.selectedNodes`, `this._view.singleClickOpens`
- XPCOM: `Services.prefs`

## checkIsHttp()
- 位置: L583-583
- 役割: URI が http か https で始まるかを判定する。
- 触るとき: http(s) の子を持つフォルダーかを確かめる判定条件を変えるとき。
- 呼び出し先: `regex.test()`

## PC_selectAll()
- 位置: L704-706
- 役割: ビューの全項目を選択する。
- 触るとき: 全選択コマンドの範囲を変えるとき。
- 呼び出し先: `this._view.selectAll()`

## showBookmarkPropertiesForSelection()
- 位置: L711-721
- 役割: 選択中の項目について、編集ダイアログを保存先の行を隠して開く。
- 触るとき: プロパティ表示の対象や隠す行を変えるとき。
- 呼び出し先: `PlacesUIUtils.showBookmarkDialog()`
- 参照: `this._view.selectedNode`, `window.top`

## PC_openLinksInTabs()
- 位置: L729-741
- 役割: 選択中のリンクを新しいタブで開く。選択が無ければルートのフォルダーを開く。
- 触るとき: 一括でタブに開く挙動 (中クリックや右クリックの項目) を変えるとき。
- 呼び出し先: `PlacesUIUtils.openMultipleLinksInTabs()`
- 参照: `nodes.length`, `this._view`, `this._view.result.root`, `this._view.selectedNode`, `this._view.selectedNodes`

## newItem()
- 位置: async L749-767
- 役割: 挿入位置を指定して新規ブックマークかフォルダーの追加ダイアログを開き、作成した項目を選択する。
- 触るとき: 右クリックの新規作成が違う場所に作られるとき、または作成後の選択を変えるとき。
- 呼び出し先: `PlacesUIUtils.showBookmarkDialog()`
- 条件付き依存: `if (!ip)` → `Components.Exception()`
- 条件付き依存: `if (bookmarkGuid)` → `this._view.selectItems()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `this._view.insertionPoint`, `window.top`

## newSeparator()
- 位置: async L772-783
- 役割: 挿入位置に区切り線を作り、作った項目を選択する。
- 触るとき: 区切り線が想定の位置に入らないとき。
- 呼び出し先: `PlacesTransactions.NewSeparator()`, `ip.getIndex()`, `this._view.selectItems()`, `txn.transact()`
- 条件付き依存: `if (!ip)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `ip.guid`, `this._view.insertionPoint`

## sortFolderByName()
- 位置: async L788-791
- 役割: 選択中フォルダーの子を名前順に並べ替える。
- 触るとき: 名前順の並べ替えが効かない、または並べ替えの取り消しを確かめるとき。
- 呼び出し先: `PlacesTransactions.SortByName()`, `PlacesTransactions.SortByName(guid).transact()`, `PlacesUtils.getConcreteItemGuid()`
- 参照: `this._view.selectedNode`

## PC_shouldSkipNode()
- 位置: L804-829
- 役割: ノードが既に処理済みのフォルダーの子孫なら、重複処理を避けるために true を返す。
- 触るとき: フォルダーと中の項目を同時に削除・コピーしたときに二重処理が起きるとき。
- 呼び出し先: `isNodeContainedBy()`
- 参照: `pastFolders.length`

## isNodeContainedBy()
- 位置: L812-821
- 役割: ノードの親をたどって、指定の親コンテナに含まれるかを判定する。
- 触るとき: 祖先の判定ロジックを変えるとき、または子孫判定が外れるとき。
- 参照: `cursor.parent`, `node.parent`

## _removeRange()
- 位置: async L843-924
- 役割: 範囲内の各ノードを、タグ解除、履歴削除、ブックマーク削除のどれで扱うか振り分けてトランザクションを作る。
- 触るとき: 削除の対象が種類ごとに違うときや、削除をトランザクション化する条件を変えるとき。
- 呼び出し先: `PlacesUtils.nodeIsTagQuery()`, `this._shouldSkipNode()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(node.parent))` → `transactions.push()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(node.parent))` → `PlacesTransactions.Untag()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(node.parent)))` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(node.parent)))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(node.parent)))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if ( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...)` → `PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if ( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...)` → `urls.add()`
- 条件付き依存: `if ( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...)` → `transactions.push()`
- 条件付き依存: `if ( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...)` → `PlacesTransactions.Untag()`
- 条件付き依存: `if ( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...)` → `Array.from()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...))` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsTagQuery(node) && node.parent && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.resultType == Ci.ns...))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if ( PlacesUtils.nodeIsURI(node) && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.queryType == Ci.nsINavHistoryQueryOptio...)` → `PlacesUtils.history.remove(node.uri).catch()`
- 条件付き依存: `if ( PlacesUtils.nodeIsURI(node) && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.queryType == Ci.nsINavHistoryQueryOptio...)` → `PlacesUtils.history.remove()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsURI(node) && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.queryType == Ci.nsINavHistoryQueryOptio...))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsURI(node) && PlacesUtils.nodeIsQuery(node.parent) && PlacesUtils.asQuery(node.parent).queryOptions.queryType == Ci.nsINavHistoryQueryOptio...))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if ( node.itemId == -1 && PlacesUtils.nodeIsQuery(node) && PlacesUtils.asQuery(node).queryOptions.queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `this._removeHistoryContainer(node).catch()`
- 条件付き依存: `if ( node.itemId == -1 && PlacesUtils.nodeIsQuery(node) && PlacesUtils.asQuery(node).queryOptions.queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `this._removeHistoryContainer()`
- 条件付き依存: `if (!( node.itemId == -1 && PlacesUtils.nodeIsQuery(node) && PlacesUtils.asQuery(node).queryOptions.queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY ))` → `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(node))` → `removedFolders.push()`
- 条件付き依存: `if (!( node.itemId == -1 && PlacesUtils.nodeIsQuery(node) && PlacesUtils.asQuery(node).queryOptions.queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY ))` → `bmGuidsToRemove.push()`
- 条件付き依存: `if (bmGuidsToRemove.length)` → `transactions.push()`
- 条件付き依存: `if (bmGuidsToRemove.length)` → `PlacesTransactions.Remove()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_TAGS_ROOT`, `PlacesUtils.asQuery(node).queryOptions.queryType`, `PlacesUtils.asQuery(node.parent).queryOptions.queryType`, `PlacesUtils.asQuery(node.parent).queryOptions.resultType`, `b.url`, `bmGuidsToRemove.length`, `console.error`, `node.bookmarkGuid`, `node.itemId`, `node.parent`, `node.parent.query.tags`, `node.parent.title`, `node.title`, `node.uri`, `range.length`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## _removeRowsFromBookmarks()
- 位置: async L926-952
- 役割: 削除可能な範囲を集めて _removeRange で変換し、まとめて一括トランザクションとして実行する。
- 触るとき: ブックマーク削除が Undo できない、または一括更新が途中で止まるとき。
- 呼び出し先: `this._removeRange()`
- 条件付き依存: `if (transactions.length)` → `PlacesUIUtils.batchUpdatesForNode()`
- 条件付き依存: `if (transactions.length)` → `PlacesTransactions.batch()`
- 参照: `this._view.removableSelectionRanges`, `this._view.result`, `transactions.length`

## _removeRowsFromHistory()
- 位置: async L958-983
- 役割: 選択中の URL と履歴コンテナを集め、履歴から削除する。履歴の削除は Undo できない。
- 触るとき: 履歴の削除が反映されない、または削除後の表示が古いままのとき。
- 呼び出し先: `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node))` → `URIs.add()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsURI(node)))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsURI(node)))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if ( PlacesUtils.nodeIsQuery(node) && PlacesUtils.asQuery(node).queryOptions.queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `this._removeHistoryContainer(node).catch()`
- 条件付き依存: `if ( PlacesUtils.nodeIsQuery(node) && PlacesUtils.asQuery(node).queryOptions.queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY )` → `this._removeHistoryContainer()`
- 条件付き依存: `if (URIs.size)` → `PlacesUIUtils.batchUpdatesForNode()`
- 条件付き依存: `if (URIs.size)` → `PlacesUtils.history.remove()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `PlacesUtils.asQuery(node).queryOptions.queryType`, `URIs.size`, `console.error`, `node.uri`, `nodes.length`, `this._view.result`, `this._view.selectedNodes`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## _removeHistoryContainer()
- 位置: async L992-1024
- 役割: サイト単位のコンテナならホストで、日単位のコンテナなら時間範囲で履歴を削除する。
- 触るとき: サイトや日付のグループを消したときに範囲が広すぎる・狭すぎるとき。
- 呼び出し先: `PlacesUtils.nodeIsHost()`
- 条件付き依存: `if (PlacesUtils.nodeIsHost(aContainerNode))` → `PlacesUtils.getString()`
- 条件付き依存: `if (PlacesUtils.nodeIsHost(aContainerNode))` → `PlacesUtils.history.removeByFilter()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsHost(aContainerNode)))` → `PlacesUtils.nodeIsDay()`
- 条件付き依存: `if (PlacesUtils.nodeIsDay(aContainerNode))` → `PlacesUtils.history.removeByFilter()`
- 条件付き依存: `if (PlacesUtils.nodeIsDay(aContainerNode))` → `PlacesUtils.toDate()`
- 参照: `aContainerNode.containerOpen`, `aContainerNode.query`, `aContainerNode.title`, `query.beginTime`, `query.endTime`

## remove()
- 位置: async L1029-1059
- 役割: 削除可能か確かめ、連続したキー操作による二重実行を防いでから、ルートの種類に応じて削除を実行する。
- 触るとき: Delete キーでの削除が効かない、または同じ削除が 2 回走るとき。最初に読む削除の入口。
- 呼び出し先: `PlacesUtils.nodeIsFolderOrShortcut()`, `this._hasRemovableSelection()`, `this._isRepeatedRemoveOperation()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(root))` → `this._removeRowsFromBookmarks()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsFolderOrShortcut(root)))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(root))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_BOOKMARKS)` → `this._removeRowsFromBookmarks()`
- 条件付き依存: `if (queryType == Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY)` → `this._removeRowsFromHistory()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_BOOKMARKS`, `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `PlacesUtils.asQuery(root).queryOptions.queryType`, `this._view.result.root`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PC_setDataTransfer()
- 位置: L1068-1105
- 役割: ドラッグ対象のノードを DataTransfer に詰める。URL を持つものは URL・テキスト・HTML も入れる。
- 触るとき: ドラッグで別のアプリに渡るデータの形式を変えるとき、または項目のドラッグ結果がおかしいとき。
- 呼び出し先: `addData()`
- 条件付き依存: `if (node.uri)` → `addURIData()`
- 参照: `PlacesUtils.TYPE_X_MOZ_PLACE`, `aEvent.dataTransfer`, `node.uri`, `nodes.length`, `result.suppressNotifications`, `this._view.draggableSelection`, `this._view.result`

## addData()
- 位置: L1077-1080
- 役割: ノードを指定の形式で包み、DataTransfer の該当位置へ設定する。
- 触るとき: ドラッグで渡す形式を増やしたいとき。
- 呼び出し先: `PlacesUtils.wrapNode()`, `dt.mozSetDataAt()`

## addURIData()
- 位置: L1082-1086
- 役割: URL を持つノードについて、URL・テキスト・HTML の 3 形式を入れる。
- 触るとき: URL の形式の一覧を変えるとき。
- 呼び出し先: `addData()`
- 参照: `PlacesUtils.TYPE_HTML`, `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_URL`

## clipboardAction()
- 位置: L1107-1134
- 役割: クリップボードの操作種別 (copy か cut) を読む。別の起動からの切り取りはコピーとして扱う。
- 触るとき: 貼り付けが移動になったりコピーになったりして想定と違うとき。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `Services.clipboard.getData()`, `action.value .QueryInterface()`, `action.value .QueryInterface(Ci.nsISupportsString) .data.split()`, `xferable.addDataFlavor()`, `xferable.getTransferData()`, `xferable.init()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsISupportsString`, `Ci.nsITransferable`, `PlacesUtils.TYPE_X_MOZ_PLACE_ACTION`, `this.profileName`
- XPCOM: `nsIClipboard` / [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## PC__releaseClipboardOwnership()
- 位置: L1136-1141
- 役割: 切り取り済みノードがあれば、クリップボードを空にする。
- 触るとき: 切り取りの状態が残ったままクリップボードを空にしたいとき。
- 条件付き依存: `if (this.cutNodes.length)` → `Services.clipboard.emptyClipboard()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `this.cutNodes.length`
- XPCOM: `nsIClipboard` / `Services.clipboard`

## PC__clearClipboard()
- 位置: L1143-1157
- 役割: クリップボードに意味の無い型を入れ、切り取り内容を消す。
- 触るとき: 貼り付け後に切り取りの内容が残るとき。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `PlacesUtils.toISupportsString()`, `Services.clipboard.setData()`, `xferable.addDataFlavor()`, `xferable.init()`, `xferable.setTransferData()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsITransferable`
- XPCOM: `nsIClipboard` / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## PC__populateClipboard()
- 位置: L1159-1222
- 役割: ノードを種類別に包み、形式の順 (Places、URL、HTML、テキスト) とアクションを設定してクリップボードへ置く。
- 触るとき: コピーや切り取りで渡すデータの形式や順序を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.wrapNode()`, `aNodes.forEach()`, `addData()`, `content.entries.push()`, `contents.forEach()`, `this._shouldSkipNode()`, `xferable.init()`
- 条件付き依存: `if (PlacesUtils.nodeIsFolderOrShortcut(node))` → `copiedFolders.push()`
- 条件付き依存: `if (content.entries.length)` → `addData()`
- 条件付き依存: `if (content.entries.length)` → `content.entries.join()`
- 条件付き依存: `if (hasData)` → `Services.clipboard.setData()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsITransferable`, `PlacesUtils.TYPE_HTML`, `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_PLACE`, `PlacesUtils.TYPE_X_MOZ_PLACE_ACTION`, `PlacesUtils.TYPE_X_MOZ_URL`, `PlacesUtils.endl`, `content.entries.length`, `content.type`, `this.profileName`
- XPCOM: `nsIClipboard` / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## addData()
- 位置: L1185-1188
- 役割: 形式を追加し、文字列データを転送へ設定する。
- 触るとき: クリップボードへ入れるデータの形式を変えるとき。
- 呼び出し先: `PlacesUtils.toISupportsString()`, `xferable.addDataFlavor()`, `xferable.setTransferData()`

## cutNodes()
- 位置: L1225-1227
- 役割: 切り取り対象のノード一覧を返す。
- 触るとき: 切り取り中の項目が薄く表示されるかを確認するとき。
- 参照: `this._cutNodes`

## cutNodes()
- 位置: L1228-1239
- 役割: 切り取り対象を入れ替える。古い対象の切り取り表示を外し、新しい対象に付ける。
- 触るとき: 切り取り表示が残る、または古い対象に付いたままのとき。
- 呼び出し先: `updateCutNodes()`
- 参照: `this._cutNodes`

## updateCutNodes()
- 位置: L1230-1234
- 役割: 切り取り対象の各ノードに、指定の状態を表示へ伝える。
- 触るとき: 切り取り表示の付け外しを変えるとき。
- 呼び出し先: `self._cutNodes.forEach()`, `self._view.toggleCutNode()`

## PC_copy()
- 位置: L1244-1257
- 役割: 選択中の項目をコピーとしてクリップボードへ置く。通知は一時的に止める。
- 触るとき: コピーで入るデータや通知の扱いを変えるとき。
- 呼び出し先: `this._populateClipboard()`
- 参照: `result.suppressNotifications`, `this._view.result`, `this._view.selectedNodes`

## PC_cut()
- 位置: L1262-1276
- 役割: 選択中の項目を切り取りとしてクリップボードへ置き、切り取り対象として記録する。
- 触るとき: 切り取りの動作や表示を変えるとき。
- 呼び出し先: `this._populateClipboard()`
- 参照: `result.suppressNotifications`, `this._view.result`, `this._view.selectedNodes`, `this.cutNodes`

## paste()
- 位置: async L1281-1364
- 役割: クリップボードの項目を読み、挿入位置へ移動またはコピーする。無効な URL があれば警告を出す。
- 触るとき: 貼り付けで項目が増えない、移動や選択が違うとき、または警告の出し方を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `PlacesUIUtils.handleTransferItems()`, `PlacesUtils.unwrapNodes()`, `Services.clipboard.getData()`, `[ PlacesUtils.TYPE_X_MOZ_PLACE, PlacesUtils.TYPE_X_MOZ_URL, PlacesUtils.TYPE_PLAINTEXT, ].forEach()`, `data.value.QueryInterface()`, `xferable.addDataFlavor()`, `xferable.getAnyTransferData()`, `xferable.init()`
- 条件付き依存: `if (!ip)` → `Components.Exception()`
- 条件付き依存: `if (action == "cut")` → `this._clearClipboard()`
- 条件付き依存: `if (itemsToSelect.length)` → `this._view.selectItems()`
- 条件付き依存: `if (invalidNodes.length)` → `PlacesUIUtils.promptLocalization.formatValuesSync()`
- 条件付き依存: `if (invalidNodes.length)` → `invalidNodes .slice(0, MAX_URI_COUNT) .map()`
- 条件付き依存: `if (invalidNodes.length)` → `invalidNodes .slice()`
- 条件付き依存: `if (invalidNodes.length)` → `encodeURI()`
- 条件付き依存: `if (encodedUri.length > MAX_URI_LENGTH)` → `encodedUri.slice()`
- 条件付き依存: `if (invalidNodes.length)` → `Services.prompt.alert()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsISupportsString`, `Ci.nsITransferable`, `Cr.NS_ERROR_NOT_AVAILABLE`, `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_PLACE`, `PlacesUtils.TYPE_X_MOZ_URL`, `data.value.QueryInterface(Ci.nsISupportsString).data`, `encodedUri.length`, `invalidNodes.length`, `item.uri`, `itemsToSelect.length`, `this._view`, `this._view.insertionPoint`, `this.clipboardAction`, `type.value`
- XPCOM: `nsIClipboard` / [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard` / `Services.prompt`

## disallowInsertion()
- 位置: L1373-1383
- 役割: タグの中と読み取り専用フォルダーには挿入できないと判定する。
- 触るとき: 挿入や DnD を許す先を増やしたり減らしたりするとき。
- 呼び出し先: `PlacesUIUtils.isFolderReadOnly()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsTagQuery()`

## canMoveNode()
- 位置: L1392-1416
- 役割: ブックマーク項目で、親が編集可能なフォルダーか検索結果なら移動可能と判定する。
- 触るとき: ドラッグで移動ではなくコピーになる、または移動できない項目を見分けたいとき。
- 呼び出し先: `PlacesUIUtils.isFolderReadOnly()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsQuery()`, `PlacesUtils.nodeIsTagQuery()`
- 参照: `node.itemId`, `node.parent`

## forgetAboutThisSite()
- 位置: async L1417-1444
- 役割: 選択中のサイトのホストを取り出し、そのサイトのデータ消去ダイアログを開く。
- 触るとき: サイトのデータ消去で対象ホストが違うとき、またはダイアログの渡し方を変えるとき。
- 呼び出し先: `PlacesUtils.nodeIsHost()`, `Services.eTLD.getBaseDomainFromHost()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsHost(this._view.selectedNode)))` → `Services.io.newURI()`
- 条件付き依存: `if (window.gDialogBox)` → `window.gDialogBox.open()`
- 条件付き依存: `if (!(window.gDialogBox))` → `window.openDialog()`
- 参照: `Services.io.newURI(this._view.selectedNode.uri).host`, `this._view.selectedNode`, `this._view.selectedNode.query.domain`, `this._view.selectedNode.uri`, `window.gDialogBox`
- XPCOM: `Services.eTLD` / `Services.io`

## showInFolder()
- 位置: L1446-1487
- 役割: ブラウザー、サイドバー、ライブラリのどれから呼ばれたかで、ブックマークの場所を開いて選択する。
- 触るとき: 「フォルダーで表示」が開く場所や選択を変えるとき、またはどの画面で効かないかを調べるとき。
- 呼び出し先: `document.documentURI.toLowerCase()`, `documentUrl.endsWith()`
- 条件付き依存: `if (documentUrl.endsWith("browser.xhtml"))` → `window.SidebarController._show("viewBookmarksSidebar").then()`
- 条件付き依存: `if (documentUrl.endsWith("browser.xhtml"))` → `window.SidebarController._show()`
- 条件付き依存: `if (documentUrl.endsWith("browser.xhtml"))` → `document.getElementById()`
- 条件付き依存: `if (documentUrl.endsWith("browser.xhtml"))` → `sidebar.contentDocument.querySelector()`
- 条件付き依存: `if (updatedPanel)` → `updatedPanel.showInFolder(aBookmarkGuid).catch()`
- 条件付き依存: `if (updatedPanel)` → `updatedPanel.showInFolder()`
- 条件付き依存: `if (!(updatedPanel))` → `sidebar.contentDocument .getElementById("bookmarks-view") .selectItems()`
- 条件付き依存: `if (!(updatedPanel))` → `sidebar.contentDocument .getElementById()`
- 条件付き依存: `if (!(documentUrl.endsWith("browser.xhtml")))` → `documentUrl.includes()`
- 条件付き依存: `if (documentUrl.includes("sidebar"))` → `document.getElementById()`
- 条件付き依存: `if (documentUrl.includes("sidebar"))` → `searchBox.clear()`
- 条件付き依存: `if (documentUrl.includes("sidebar"))` → `this._view.selectItems()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `PlacesUtils.bookmarks .fetch(aBookmarkGuid, null, { includePath: true }) .then()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `PlacesUtils.bookmarks .fetch()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `b.path.map()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `containers.splice()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `PlacesOrganizer.selectLeftPaneContainerByHierarchy()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `this._view.selectItems()`
- 条件付き依存: `if (!(documentUrl.includes("sidebar")))` → `console.error()`
- 参照: `console.error`, `obj.guid`

## PCDH_draggingOverChildNode()
- 位置: L1514-1523
- 役割: 現在のドロップ先が、指定ノードの子孫かを親をたどって判定する。
- 触るとき: メニューが子を掴んでいるときに閉じないかを確かめるとき。
- 参照: `currentNode.parentNode`, `this.currentDropTarget`

## PCDH__getSession()
- 位置: L1529-1531
- 役割: このウィンドウの現在のドラッグセッションを返す。
- 触るとき: ドラッグ中かどうかの判定に使う箇所を追うとき。
- 呼び出し先: `this.dragService.getCurrentSession()`

## getMostRelevantFlavor()
- 位置: L1539-1543
- 役割: 対応形式の一覧のうち、最初に見つかった形式を返す。
- 触るとき: DnD で受け付ける形式の優先順位を変えるとき。
- 呼び出し先: `Array.from()`, `PlacesUIUtils.SUPPORTED_FLAVORS.find()`, `flavors.includes()`

## PCDH_canDrop()
- 位置: L1555-1646
- 役割: ドラッグされた項目が、そのドロップ先へ入れてよいかを判定する (タグ、自分自身や子孫、javascript: の複数ドロップを拒否)。
- 触るとき: ドロップ線が出ない、または出てはいけない所に出るとき。
- 呼び出し先: `PlacesUtils.unwrapNodes()`, `URL.parse()`, `dragged.uri.startsWith()`, `dt.mozGetDataAt()`, `dt.mozTypesAt()`, `flavor.startsWith()`, `this.getMostRelevantFlavor()`, `validNodes.some()`
- 条件付き依存: `if (dragOverPlacesNode)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (dragOverPlacesNode)` → `PlacesUtils.nodeAncestors()`
- 参照: `Ci.nsINavHistoryResultNode`, `PlacesUtils.TYPE_X_MOZ_PLACE`, `PlacesUtils.TYPE_X_MOZ_PLACE_CONTAINER`, `PlacesUtils.TYPE_X_MOZ_URL`, `URL.parse(n.uri)?.protocol`, `dragOverPlacesNode._placesNode`, `dragOverPlacesNode.parentNode?._placesNode`, `dragged.concreteGuid`, `dragged.itemGuid`, `dragged.type`, `dragged.uri`, `dt.mozItemCount`, `ip.isTag`, `n.uri`, `this.currentDropTarget`, `validNodes.length`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## onDrop()
- 位置: async L1657-1773
- 役割: ドラッグのデータを集め、javascript: の単独ブックマーク化は確認ダイアログを出し、それ以外は挿入位置へ転送する。
- 触るとき: ドロップしたときに項目が追加されない、または javascript: の扱いを変えるとき。
- 呼び出し先: `PlacesUIUtils.handleTransferItems()`, `URL.parse()`, `["copy", "link"].includes()`, `dt.mozGetDataAt()`, `dt.mozTypesAt()`, `duplicable.has()`, `duplicable.set()`, `flavor.startsWith()`, `nodes.some()`, `this.getMostRelevantFlavor()`
- 条件付き依存: `if (duplicable.has(flavor))` → `duplicable.get()`
- 条件付き依存: `if (duplicable.has(flavor))` → `handled.has()`
- 条件付き依存: `if (duplicable.has(flavor))` → `handled.add()`
- 条件付き依存: `if (flavor != TAB_DROP_TYPE)` → `PlacesUtils.unwrapNodes()`
- 条件付き依存: `if (!(flavor != TAB_DROP_TYPE))` → `XULElement.isInstance()`
- 条件付き依存: `if ( XULElement.isInstance(data) && data.localName == "tab" && data.documentGlobal.isChromeWindow )` → `nodes.push()`
- 条件付き依存: `if (!( XULElement.isInstance(data) && data.localName == "tab" && data.documentGlobal.isChromeWindow ))` → `XULElement.isInstance()`
- 条件付き依存: `if ( XULElement.isInstance(data) && data.localName == "tab-split-view-wrapper" && data.documentGlobal.isChromeWindow )` → `data.tabs.forEach()`
- 条件付き依存: `if ( XULElement.isInstance(data) && data.localName == "tab-split-view-wrapper" && data.documentGlobal.isChromeWindow )` → `nodes.push()`
- 条件付き依存: `if (nodes.length == 1 && externalDrag)` → `Services.io.newURI()`
- 条件付き依存: `if (uri?.scheme === "javascript")` → `PlacesUIUtils.showBookmarkDialog()`
- 条件付き依存: `if (uri?.scheme === "javascript")` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (bookmarkGuid && view)` → `view.selectItems()`
- 参照: `PlacesUtils.TYPE_PLAINTEXT`, `PlacesUtils.TYPE_X_MOZ_URL`, `PlacesUtils.unwrapNodes(data, flavor).validNodes`, `URL.parse(n.uri)?.protocol`, `data.documentGlobal.isChromeWindow`, `data.label`, `data.linkedBrowser.currentURI`, `data.localName`, `dt.dropEffect`, `dt.mozItemCount`, `n.uri`, `nodes.length`, `nodes[0].title`, `nodes[0].uri`, `tab.label`, `tab.linkedBrowser.currentURI?.spec`, `uri.spec`, `uri?.scheme`
- XPCOM: `Services.io`
