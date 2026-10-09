# browser/components/places/content/treeView.js

source: browser/components/places/content/treeView.js
source-hash: 28e584f7163d2a7dc5c18d6c60f98a7afcd49110
lines: 1856

## <module>
- 役割: places の一覧(ライブラリやサイドバーなど)に結果ノードを表示する nsITreeView 実装 PlacesTreeView を定義する。行の管理、ノード変更の追随、並び替え、ドラッグ&ドロップを含む
- 呼び出し先: `ChromeUtils.generateQI()`

## makeNodeDetailsKey()
- 位置: L21-32
- 役割: uri、time、itemId の三つから uri*time*itemId の文字列キーを作る。足りないときは空文字を返す
- 触るとき: ノードを同一視する仕組みを変えるとき。_nodeDetails への登録と削除がこのキーで対応しているので、キーの形を変えると選択の復元が効かなくなる
- 参照: `nodeOrDetails.itemId`, `nodeOrDetails.time`, `nodeOrDetails.uri`

## PlacesTreeView()
- 位置: L34-44
- 役割: ツリービューの内部状態(結果、ツリー、行の配列、_nodeDetails など)を初期化するコンストラクター
- 触るとき: ビューに新しい状態を持たせるとき
- 参照: `aContainer._controller`, `aContainer.flatList`, `this._controller`, `this._element`, `this._flatList`, `this._nodeDetails`, `this._result`, `this._rootNode`, `this._rows`, `this._selection`, `this._tree`

## wrappedJSObject()
- 位置: L47-49
- 役割: JS 側の実体として自分自身を返す getter
- 触るとき: XPCOM 越しに受け取ったビューを JS の実体として扱う箇所を追うとき

## PTV__finishInit()
- 位置: L60-80
- 役割: 結果とツリーがそろった後に、ルートを開くか再構築し、並び替えの表示を反映する。その間は選択の通知を抑止する
- 触るとき: ツリーを結果に接続した直後の初期表示がおかしいとき
- 呼び出し先: `this.sortingChanged()`
- 条件付き依存: `if (!(!this._rootNode.containerOpen))` → `this.invalidateContainer()`
- 参照: `selection.selectEventsSuppressed`, `this._result.sortingMode`, `this._rootNode`, `this._rootNode.containerOpen`, `this.selection`

## uninit()
- 位置: L82-93
- 役割: 編集中の MutationObserver を切断し、結果から自分の監視を外して参照の循環を断つ
- 触るとき: ツリーを破棄した後も結果が通知を送り続けて、メモリが解放されないとき
- 条件付き依存: `if (this._editingObservers)` → `this._editingObservers.values()`
- 条件付き依存: `if (this._editingObservers)` → `observer.disconnect()`
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 参照: `this._editingObservers`, `this._result`

## PTV__isPlainContainer()
- 位置: L117-139
- 役割: 子を後から遅延構築してよい単純なコンテナーかを判定する。フォルダーや、日付・サイト・タグの根などの特殊なクエリ結果は対象外
- 触るとき: 遅延構築の対象を変えるとき。判定が変わると行の計算方式が切り替わる
- 参照: `Ci.nsINavHistoryQueryOptions.RESULTS_AS_DATE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_DATE_SITE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_LEFT_PANE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_ROOTS_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_SITE_QUERY`, `Ci.nsINavHistoryQueryOptions.RESULTS_AS_TAGS_ROOT`, `Ci.nsINavHistoryQueryResultNode`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER_SHORTCUT`, `aContainer.queryOptions.resultType`, `aContainer.type`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryQueryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__getRowForNode()
- 位置: L167-235
- 役割: ノードの行番号を求める。親が単純コンテナーなら親の行と添字から計算し、そうでなければ rows を検索する。非表示のノードには例外を投げる
- 触るとき: 行番号がずれる、または「Invisible node」の例外が出るとき。aForceBuild が true なら未構築の行も計算する
- 呼び出し先: `Array.from()`, `PlacesUtils.nodeAncestors()`, `this._isPlainContainer()`
- 条件付き依存: `if (parent == this._rootNode)` → `this._rows.indexOf()`
- 条件付き依存: `if (!parentIsPlain)` → `this._rows.indexOf()`
- 条件付き依存: `if (parent == this._rootNode)` → `this._rootNode.getChildIndex()`
- 条件付き依存: `if (!(useNodeIndex && typeof aParentRow == "number"))` → `this._rows.indexOf()`
- 条件付き依存: `if (row == -1 && aForceBuild)` → `this._getRowForNode()`
- 条件付き依存: `if (row == -1 && aForceBuild)` → `parent.getChildIndex()`
- 条件付き依存: `if (row != -1)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (row != -1)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (row != -1)` → `this._nodeDetails.set()`
- 参照: `aNode.parent`, `ancestor.containerOpen`, `ancestors.length`, `this._rootNode`, `this._rows`

## PTV__getParentByChildRow()
- 位置: L244-255
- 役割: 指定行のノードの親と、その親の行番号を返す。親がルートなら [ルート, -1] を返す
- 触るとき: 親行を引く処理(getParentIndex など)の結果が違うとき
- 呼び出し先: `this._getNodeForRow()`, `this._rows.lastIndexOf()`
- 参照: `node.parent`, `this._rootNode`

## PTV__getNodeForRow()
- 位置: L264-304
- 役割: 行番号のノードを返す。未構築の行は、直前の既知の行から子を取り出して rows へ入れる
- 触るとき: 遅延構築された行で別のノードが返るとき、または大きなフォルダーで行の取り出しが遅いとき
- 呼び出し先: `makeNodeDetailsKey()`, `parent.getChild()`, `this._getParentByChildRow()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`
- 条件付き依存: `if (!rowNode)` → `this._rootNode.getChild()`
- 条件付き依存: `if (!rowNode)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (!rowNode)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (!rowNode)` → `this._nodeDetails.set()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `rowNode.getChild()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (rowNode instanceof Ci.nsINavHistoryContainerResultNode)` → `this._nodeDetails.set()`
- 参照: `Ci.nsINavHistoryContainerResultNode`, `this._rows`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__buildVisibleSection()
- 位置: L321-400
- 役割: コンテナーの子を rows に書き込み、並び替え中は区切り線を除く。開いているべき子は再帰的に展開し、xulstore の open 状態と食い違うコンテナーは aToOpen に積む
- 触るとき: フォルダーを開いたときの行の並び、または開閉状態の保存と復元を変えるとき
- 呼び出し先: `aContainer.getChild()`, `makeNodeDetailsKey()`, `this._isPlainContainer()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`, `this._rows .splice()`, `this._rows .splice(0, aFirstChildRow) .concat()`
- 条件付き依存: `if (sortingMode != Ci.nsINavHistoryQueryOptions.SORT_BY_NONE)` → `this._nodeDetails.delete()`
- 条件付き依存: `if (sortingMode != Ci.nsINavHistoryQueryOptions.SORT_BY_NONE)` → `makeNodeDetailsKey()`
- 条件付き依存: `if (sortingMode != Ci.nsINavHistoryQueryOptions.SORT_BY_NONE)` → `this._rows.splice()`
- 条件付き依存: `if (uri)` → `Services.xulStore.getValue()`
- 条件付き依存: `if (uri)` → `PlacesUIUtils.obfuscateUrlForXulStore()`
- 条件付き依存: `if (isopen != curChild.containerOpen)` → `aToOpen.push()`
- 条件付き依存: `if (curChild.containerOpen && curChild.childCount > 0)` → `this._buildVisibleSection()`
- 参照: `Ci.nsINavHistoryContainerResultNode`, `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `aContainer.childCount`, `aContainer.containerOpen`, `curChild.childCount`, `curChild.containerOpen`, `curChild.type`, `curChild.uri`, `document.documentURI`, `this._flatList`, `this._result.sortingMode`, `this._rows`, `this._rows.length`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.xulStore`

## PTV__countVisibleRowsForNodeAtRow()
- 位置: L410-431
- 役割: コンテナーが占める行数を、同じかより浅い階層の行が現れるまで数える
- 触るとき: 折りたたみで消す行数や、挿入位置の計算がずれるとき
- 参照: `Ci.nsINavHistoryContainerResultNode`, `node.indentLevel`, `rowNode.indentLevel`, `this._rows`, `this._rows.length`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__getSelectedNodesInRange()
- 位置: L433-472
- 役割: 置き換えられる行の範囲と重なる選択範囲について、ノード、元の行番号、表示中かどうかを控える
- 触るとき: 行をまとめて差し替える前に選択を保つ仕組みを変えるとき
- 呼び出し先: `Math.max()`, `Math.min()`, `nodesInfo.push()`, `selection.getRangeAt()`, `selection.getRangeCount()`, `this._tree.getFirstVisibleRow()`, `this._tree.getLastVisibleRow()`
- 参照: `max.value`, `min.value`, `this._rows`, `this.selection`

## PTV__getNewRowForRemovedNode()
- 位置: L486-515
- 役割: 削除または移動されたノードの新しい行を探す。親が残っていれば同じノードの行を求め、無ければ itemId、uri、time の一致する控えから探す
- 触るとき: 削除や移動の後に選択がどの行へ移るかを調べるとき。親が閉じていると -1 になる
- 呼び出し先: `makeNodeDetailsKey()`, `this._getRowForNode()`, `this._nodeDetails.get()`
- 条件付き依存: `if (parent)` → `PlacesUtils.nodeAncestors()`
- 条件付き依存: `if (parent)` → `this._getRowForNode()`
- 参照: `aOldNode.parent`, `ancestor.containerOpen`

## PTV__restoreSelection()
- 位置: L525-562
- 役割: 控えた選択を新しい行へ選び直す。表示範囲内にあった選択が一つあれば、その行が見えるようスクロールする
- 触るとき: ツリーの更新後に選択が外れる、または別の行が選ばれるとき
- 呼び出し先: `this._getNewRowForRemovedNode()`
- 条件付き依存: `if (row != -1)` → `selection.rangedSelect()`
- 条件付き依存: `if (aNodesInfo.length == 1 && selection.count == 0)` → `Math.min()`
- 条件付き依存: `if (scrollToRow != -1)` → `this._tree.ensureRowIsVisible()`
- 参照: `aNodesInfo.length`, `aNodesInfo[0].oldRow`, `aNodesInfo[0].wasVisible`, `nodeInfo.node`, `nodeInfo.wasVisible`, `selection.count`, `this._rows.length`, `this.selection`

## PTV__convertPRTimeToString()
- 位置: L564-582
- 役割: PRTime のマイクロ秒を表示用の文字列にする。当日なら時刻だけ、それ以外は日付と時刻を返す
- 触るとき: 訪問日、追加日、更新日の列の表示形式を変えるとき。当日かどうかは端末のローカル時刻の深夜で判定する
- 呼び出し先: `dateObj.getTime()`, `dateObj.getTimezoneOffset()`, `new Date(midnight).getTimezoneOffset()`, `this._dateFormatter.format()`, `this._todayFormatter.format()`

## _todayFormatter()
- 位置: L587-596
- 役割: 当日用の時刻書式(timeStyle short)の DateTimeFormat を初回だけ作って使い回す getter
- 触るとき: 当日の時刻の書式を変えるとき
- 参照: `Services.intl.DateTimeFormat`, `this.__todayFormatter`
- XPCOM: `Services.intl`

## _dateFormatter()
- 位置: L599-611
- 役割: 日付と時刻の書式(dateStyle short、timeStyle short)の DateTimeFormat を初回だけ作って使い回す getter
- 触るとき: 日付の列の書式を変えるとき
- 参照: `Services.intl.DateTimeFormat`, `this.__dateFormatter`
- XPCOM: `Services.intl`

## PTV__getColumnType()
- 位置: L622-642
- 役割: 列要素の anonid か id から COLUMN_TYPE の定数を返す。知らない列は COLUMN_TYPE_UNKNOWN を返す
- 触るとき: 列を新しく追加するとき。ここに対応を足さないと、その列のセルは空欄になる
- 呼び出し先: `aColumn.element.getAttribute()`
- 参照: `aColumn.id`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_UNKNOWN`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`

## PTV__sortTypeToColumnType()
- 位置: L644-676
- 役割: 並び替えモードを [列の種類, 降順かどうか] の組に変える。知らないモードは UNKNOWN と昇順を返す
- 触るとき: 並び替えモードを増やすとき、またはどの列の見出しに矢印が付くかを調べるとき
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_DATEADDED_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATEADDED_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_LASTMODIFIED_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_LASTMODIFIED_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TAGS_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TAGS_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TITLE_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_TITLE_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_URI_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_URI_DESCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_VISITCOUNT_ASCENDING`, `Ci.nsINavHistoryQueryOptions.SORT_BY_VISITCOUNT_DESCENDING`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_UNKNOWN`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV_nodeInserted()
- 位置: L679-752
- 役割: 結果に子が追加されたとき、その行番号を求めて rows に挿入し、ツリーに行数の変化を知らせる。並び替え中の非表示の区切り線は無視する
- 触るとき: ブックマークや履歴の追加で行の位置がずれるとき。挿入位置は次の見える兄弟を探すか、末尾から数えるかの二通りで決まる
- 呼び出し先: `PlacesUtils.asContainer()`, `PlacesUtils.nodeIsContainer()`, `PlacesUtils.nodeIsSeparator()`, `console.assert()`, `makeNodeDetailsKey()`, `this._isPlainContainer()`, `this._nodeDetails.set()`, `this._rows.splice()`, `this._tree.rowCountChanged()`, `this.isSorted()`
- 条件付き依存: `if (aParentNode != this._rootNode)` → `this._getRowForNode()`
- 条件付き依存: `if (aParentNode.childCount == 1)` → `this._tree.invalidateRow()`
- 条件付き依存: `if (!(aNewIndex == 0 || this._isPlainContainer(aParentNode) || cc == 0))` → `PlacesUtils.nodeIsSeparator()`
- 条件付き依存: `if (!(aNewIndex == 0 || this._isPlainContainer(aParentNode) || cc == 0))` → `this.isSorted()`
- 条件付き依存: `if (!(aNewIndex == 0 || this._isPlainContainer(aParentNode) || cc == 0))` → `aParentNode.getChild()`
- 条件付き依存: `if (!separatorsAreHidden || PlacesUtils.nodeIsSeparator(node))` → `this._getRowForNode()`
- 条件付き依存: `if (row < 0)` → `aParentNode.getChild()`
- 条件付き依存: `if (row < 0)` → `this._getRowForNode()`
- 条件付き依存: `if (row < 0)` → `this._countVisibleRowsForNodeAtRow()`
- 条件付き依存: `if ( PlacesUtils.nodeIsContainer(aNode) && PlacesUtils.asContainer(aNode).containerOpen )` → `this.invalidateContainer()`
- 参照: `PlacesUtils.asContainer(aNode).containerOpen`, `aParentNode.childCount`, `this._result`, `this._rootNode`, `this._tree`

## PTV_nodeRemoved()
- 位置: L770-831
- 役割: ノードとその子の行を rows から取り除き、そのノードが唯一選ばれていた場合は次の行を選ぶ。ルートの削除は未実装として例外を投げる
- 触るとき: 削除後の選択位置がおかしいとき、または行数の食い違いを調べるとき
- 呼び出し先: `Math.min()`, `PlacesUtils.nodeIsSeparator()`, `console.assert()`, `makeNodeDetailsKey()`, `selection.getRangeCount()`, `this._countVisibleRowsForNodeAtRow()`, `this._getRowForNode()`, `this._nodeDetails.delete()`, `this._rows.splice()`, `this._tree.rowCountChanged()`, `this.isSorted()`
- 条件付き依存: `if (aNode == this._rootNode)` → `Components.Exception()`
- 条件付き依存: `if (oldRow < 0)` → `Components.Exception()`
- 条件付き依存: `if (selection.getRangeCount() == 1)` → `selection.getRangeAt()`
- 条件付き依存: `if (selection.getRangeCount() == 1)` → `this.nodeForTreeIndex()`
- 条件付き依存: `if (aParentNode != this._rootNode && !aParentNode.hasChildren)` → `this._tree.invalidateRow()`
- 条件付き依存: `if (rowToSelect != -1)` → `this.selection.rangedSelect()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`, `Cr.NS_ERROR_UNEXPECTED`, `aParentNode.hasChildren`, `max.value`, `min.value`, `this._result`, `this._rootNode`, `this._rows.length`, `this._tree`, `this.selection`

## PTV_nodeMoved()
- 位置: L833-893
- 役割: 移動の前に元の行と選択を控え、rows から外してから nodeInserted で新しい親の下へ入れ直し、選択を戻す
- 触るとき: ドラッグ&ドロップや並び替えでノードを移した後に、選択が保たれないとき
- 呼び出し先: `PlacesUtils.nodeIsSeparator()`, `console.assert()`, `makeNodeDetailsKey()`, `this._countVisibleRowsForNodeAtRow()`, `this._getRowForNode()`, `this._getSelectedNodesInRange()`, `this._nodeDetails.delete()`, `this._rows.splice()`, `this._tree.rowCountChanged()`, `this.isSorted()`, `this.nodeInserted()`
- 条件付き依存: `if (oldRow < 0)` → `Components.Exception()`
- 条件付き依存: `if (aOldParent != this._rootNode && !aOldParent.hasChildren)` → `this._tree.invalidateRow()`
- 条件付き依存: `if (nodesToReselect.length)` → `this._restoreSelection()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `aOldParent.hasChildren`, `nodesToReselect.length`, `this._result`, `this._rootNode`, `this._tree`, `this.selection.selectEventsSuppressed`

## PTV__invalidateCellValue()
- 位置: L895-928
- 役割: 指定した種類の列のセルを再描画させる。更新日の列も一緒に再描画し、タイトル列では画像のキャッシュも捨てる
- 触るとき: タイトル、URL、日付などの値が変わったのに表示が古いままのとき
- 呼び出し先: `console.assert()`, `this._findColumnByType()`, `this._getRowForNode()`
- 条件付き依存: `if (aColumnType == this.COLUMN_TYPE_TITLE)` → `this._tree.removeImageCacheEntry()`
- 条件付き依存: `if (column && !column.element.hidden)` → `this._tree.invalidateCell()`
- 条件付き依存: `if (aColumnType != this.COLUMN_TYPE_LASTMODIFIED)` → `this._findColumnByType()`
- 条件付き依存: `if (lastModifiedColumn && !lastModifiedColumn.hidden)` → `this._tree.invalidateCell()`
- 参照: `column.element.hidden`, `lastModifiedColumn.hidden`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TITLE`, `this._result`, `this._rootNode`, `this._tree`

## PTV_nodeTitleChanged()
- 位置: L930-932
- 役割: タイトル列のセルを無効化して、再描画させる
- 触るとき: タイトルを変えても一覧に反映されないとき
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TITLE`

## PTV_nodeURIChanged()
- 位置: L934-944
- 役割: 旧 URL のキーを _nodeDetails から消し、新しいキーを登録してから URL 列を無効化する
- 触るとき: URL を変えた後に、そのノードの選択や行の対応が外れるとき
- 呼び出し先: `makeNodeDetailsKey()`, `this._invalidateCellValue()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`
- 参照: `aNode.itemId`, `aNode.time`, `this.COLUMN_TYPE_URI`

## PTV_nodeIconChanged()
- 位置: L946-948
- 役割: アイコンが変わったとき、タイトル列のセルを無効化する
- 触るとき: アイコンが一覧に出ない、または古いとき
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TITLE`

## PTV_nodeHistoryDetailsChanged()
- 位置: L950-965
- 役割: 訪問日時が変わったとき、旧い日時のキーを消して新しいキーを登録し、日付と訪問回数の列を無効化する
- 触るとき: 履歴の訪問情報が変わった後に、表示や選択が合わないとき
- 呼び出し先: `makeNodeDetailsKey()`, `this._invalidateCellValue()`, `this._nodeDetails.delete()`, `this._nodeDetails.set()`
- 参照: `aNode.itemId`, `aNode.uri`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_VISITCOUNT`

## PTV_nodeTagsChanged()
- 位置: L967-969
- 役割: タグの列のセルを無効化する
- 触るとき: タグ列の表示が古いままのとき
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TAGS`

## nodeKeywordChanged()
- 位置: L971-971
- 役割: キーワードの変更通知を受けるが、何もしない空の実装
- 触るとき: キーワードの変更を一覧の表示に反映させたいとき。この空の実装が原因かどうかをまず確かめる

## PTV_nodeDateAddedChanged()
- 位置: L973-975
- 役割: 追加日の列のセルを無効化する
- 触るとき: 追加日の表示が古いままのとき
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_DATEADDED`

## PTV_nodeLastModifiedChanged()
- 位置: L977-979
- 役割: 更新日の列のセルを無効化する
- 触るとき: 更新日の表示が古いままのとき
- 呼び出し先: `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_LASTMODIFIED`

## PTV_containerStateChanged()
- 位置: L981-983
- 役割: コンテナーの開閉が変わったという通知を、その範囲の再構築へ回す
- 触るとき: フォルダーの開閉が一覧に反映されないとき
- 呼び出し先: `this.invalidateContainer()`

## PTV_invalidateContainer()
- 位置: L985-1121
- 役割: コンテナーの子の行を消して作り直す。ルートが閉じられたときは全行を消す。編集中なら、編集が終わるまで再構築を待つ
- 触るとき: 子の大量の変化や並び替えを一覧に反映させるとき。編集中に行が更新されないときもここを見る
- 呼び出し先: `console.assert()`, `makeNodeDetailsKey()`, `this._buildVisibleSection()`, `this._getSelectedNodesInRange()`, `this._nodeDetails.delete()`, `this._restoreSelection()`, `this._rows.splice()`, `this._tree.beginUpdateBatch()`, `this._tree.endUpdateBatch()`, `this._tree.getAttribute()`
- 条件付き依存: `if (this._tree.getAttribute("editing"))` → `this._editingObservers.has()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this.invalidateContainer()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this._editingObservers.get()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `observer.disconnect()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this._editingObservers.delete()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `mutationObserver.observe()`
- 条件付き依存: `if (!this._editingObservers.has(aContainer))` → `this._editingObservers.set()`
- 条件付き依存: `if (!this._rootNode.containerOpen)` → `this._nodeDetails.clear()`
- 条件付き依存: `if (replaceCount)` → `this._tree.rowCountChanged()`
- 条件付き依存: `if (!(aContainer == this._rootNode))` → `this._getRowForNode()`
- 条件付き依存: `if (!(aContainer == this._rootNode))` → `this._tree.invalidateRow()`
- 条件付き依存: `if (!(aContainer == this._rootNode))` → `this._countVisibleRowsForNodeAtRow()`
- 条件付き依存: `if ( nodesToReselect.length && nodesToReselect.length == oldSelectionCount )` → `this.selection.rangedSelect()`
- 条件付き依存: `if ( nodesToReselect.length && nodesToReselect.length == oldSelectionCount )` → `this._tree.ensureRowIsVisible()`
- 条件付き依存: `if (elementsAddedCount)` → `this._tree.rowCountChanged()`
- 参照: `aContainer.containerOpen`, `item.containerOpen`, `item.parent`, `item.uri`, `nodesToReselect.length`, `parent.parent`, `parent.uri`, `this._editingObservers`, `this._flatList`, `this._result`, `this._rootNode`, `this._rootNode.containerOpen`, `this._rows`, `this._rows.length`, `this._tree`, `this.selection.count`, `this.selection.selectEventsSuppressed`, `toOpenElements.length`
- XPCOM: `Services.tm`

## PTV__findColumnByType()
- 位置: L1124-1143
- 役割: 列の種類から列オブジェクトを探す。結果は _columns にキャッシュされ、見つからなければ null を返す
- 触るとき: 列の種類に応じて表示を変える処理を足すとき
- 呼び出し先: `columns.getColumnAt()`, `this._getColumnType()`
- 参照: `columns.count`, `this._columns`, `this._tree.columns`

## PTV__sortingChanged()
- 位置: L1145-1173
- 役割: 並び替えの列に sortDirection 属性を付け、前の列の属性を消す。並び替えに応じたコマンドの有効・無効も更新する
- 触るとき: 並び替えの矢印が出ない、または古いままのとき
- 呼び出し先: `columns.getSortedColumn()`, `this._findColumnByType()`, `this._sortTypeToColumnType()`, `window.updateCommands()`
- 条件付き依存: `if (sortedColumn)` → `sortedColumn.element.removeAttribute()`
- 条件付き依存: `if (column)` → `column.element.setAttribute()`
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `this._result`, `this._tree`, `this._tree.columns`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV__batching()
- 位置: L1176-1185
- 役割: ツリーの一括更新と選択通知の抑止を切り替える。現在の状態と同じなら何もしない
- 触るとき: 複数の変更をまとめて反映する処理を書くとき。終わりに解除しないと、選択の通知が止まったままになる
- 条件付き依存: `if (this._inBatchMode)` → `this._tree.beginUpdateBatch()`
- 条件付き依存: `if (!(this._inBatchMode))` → `this._tree.endUpdateBatch()`
- 参照: `this._inBatchMode`, `this.selection.selectEventsSuppressed`

## result()
- 位置: L1187-1189
- 役割: 結果オブジェクトを返す getter
- 触るとき: ビューが今どの結果を表示しているかを調べるとき
- 参照: `this._result`

## result()
- 位置: L1190-1212
- 役割: 結果を差し替える setter。古い結果の監視を外してルートを閉じ、新しい結果の監視を登録して、ツリーが付いていれば初期化する
- 触るとき: 表示する結果を切り替えたときに、古い結果の通知が届く、または表示が更新されないとき
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 条件付き依存: `if (this._tree && val)` → `this._finishInit()`
- 参照: `this._cellProperties`, `this._cuttingNodes`, `this._result`, `this._result.root`, `this._rootNode`, `this._rootNode.containerOpen`, `this._tree`

## nodeForTreeIndex()
- 位置: L1223-1229
- 役割: 行番号からノードを返す。行数より大きい値では NS_ERROR_INVALID_ARG の例外を投げる
- 触るとき: 行番号からノードを求める呼び出し元を追うとき。比較が > なので、行数と同じ値では例外が出ずに undefined 相当の結果になる(要確認)
- 呼び出し先: `this._getNodeForRow()`
- 条件付き依存: `if (aIndex > this._rows.length)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this._rows.length`

## treeIndexForNode()
- 位置: L1238-1245
- 役割: ノードの行番号を返す。見えていない、または一覧に無いノードでは -1 を返す
- 触るとき: 選択やフォーカスをノードから行へ変換する処理を追うとき
- 呼び出し先: `this._getRowForNode()`

## rowCount()
- 位置: L1248-1250
- 役割: rows の長さを返す getter。ツリーの行数になる
- 触るとき: 行数が実際の表示と合わないとき
- 参照: `this._rows.length`

## selection()
- 位置: L1251-1253
- 役割: ツリーの選択オブジェクトを返す getter
- 触るとき: 選択の状態を読む処理を追うとき
- 参照: `this._selection`

## selection()
- 位置: L1254-1256
- 役割: ツリーの選択オブジェクトを保持する setter
- 触るとき: 選択オブジェクトを差し替える処理を追うとき
- 参照: `this._selection`

## getRowProperties()
- 位置: L1258-1260
- 役割: 行のプロパティを返さない。常に空文字を返す
- 触るとき: 行単位で CSS 用のプロパティを付けたくなったとき、ここを拡張する

## PTV_getCellProperties()
- 位置: L1262-1333
- 役割: セルのプロパティを組み立てる。URL 列には ltr を付け、タイトル列にはノードの種類に応じた query、区切り線、URL スキームなどを付ける。切り取り中のノードには cutting を付ける
- 触るとき: セルの見た目を種類ごとに変えるとき、または切り取りの表示が出ないとき。タイトル列の結果はノードごとにキャッシュされる
- 呼び出し先: `aColumn.element.getAttribute()`, `this._cellProperties.get()`, `this._cuttingNodes.has()`, `this._getNodeForRow()`
- 条件付き依存: `if (properties === undefined)` → `PlacesUtils.containerTypes.includes()`
- 条件付き依存: `if (nodeType == Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY)` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(node)))` → `PlacesUtils.nodeIsDay()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsDay(node)))` → `PlacesUtils.nodeIsHost()`
- 条件付き依存: `if (!(nodeType == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(node))` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (properties === undefined)` → `this._cellProperties.set()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `PlacesUtils.bookmarks.menuGuid`, `PlacesUtils.bookmarks.toolbarGuid`, `PlacesUtils.bookmarks.unfiledGuid`, `PlacesUtils.bookmarks.virtualMenuGuid`, `PlacesUtils.bookmarks.virtualToolbarGuid`, `PlacesUtils.bookmarks.virtualUnfiledGuid`, `PlacesUtils.virtualAllBookmarksGuid`, `PlacesUtils.virtualDownloadsGuid`, `PlacesUtils.virtualHistoryGuid`, `PlacesUtils.virtualTagsGuid`, `aColumn.id`, `node.bookmarkGuid`, `node.itemId`, `node.type`, `node.uri`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## getColumnProperties()
- 位置: L1335-1337
- 役割: 列のプロパティを返さない。常に空文字を返す
- 触るとき: 列に独自の属性を付けたいとき

## PTV_isContainer()
- 位置: L1339-1360
- 役割: 行が開閉できるコンテナーかを返す。フラットリストでは常に true、展開の無い空のクエリは false を返す
- 触るとき: 空のクエリ結果に開閉の三角が出る、または出ないとき
- 呼び出し先: `PlacesUtils.nodeIsContainer()`, `PlacesUtils.nodeIsQuery()`, `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(node) && !PlacesUtils.nodeIsTagQuery(node))` → `PlacesUtils.asQuery()`
- 参照: `PlacesUtils.asQuery(node).queryOptions.expandQueries`, `node.hasChildren`, `this._flatList`, `this._rows`

## PTV_isContainerOpen()
- 位置: L1362-1369
- 役割: フラットリストでは false を返し、それ以外は行の開閉状態を返す
- 触るとき: 開閉の三角の向きが実際の状態と合わないとき
- 参照: `this._flatList`, `this._rows`, `this._rows[aRow].containerOpen`

## PTV_isContainerEmpty()
- 位置: L1371-1378
- 役割: フラットリストでは true、それ以外は子を持つかどうかの逆を返す
- 触るとき: 空のフォルダーの表示が正しくないとき
- 参照: `this._flatList`, `this._rows`, `this._rows[aRow].hasChildren`

## PTV_isSeparator()
- 位置: L1380-1384
- 役割: 行が区切り線かどうかを返す
- 触るとき: 区切り線の描画を変えるとき
- 呼び出し先: `PlacesUtils.nodeIsSeparator()`
- 参照: `this._rows`

## PTV_isSorted()
- 位置: L1386-1390
- 役割: 結果の並び替えモードが SORT_BY_NONE 以外かどうかを返す
- 触るとき: 並び替え中の表示の制限(区切り線の非表示、ドロップの禁止など)の条件を変えるとき
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `this._result.sortingMode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV_canDrop()
- 位置: L1392-1408
- 役割: ユーザー操作が無効なときと、並び替え中のときは false を返す。それ以外は挿入点を求め、転送データを PlacesControllerDragHelper で判定する
- 触るとき: ドラッグ中に受け入れ可能な場所を変えるとき
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `this._getInsertionPoint()`, `this.isSorted()`
- 条件付き依存: `if (!this._result)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `this._controller.disableUserActions`, `this._result`

## PTV__getInsertionPoint()
- 位置: L1410-1498
- 役割: ドロップ位置(行と向き)を、親コンテナーと挿入位置を持つ PlacesInsertionPoint に変換する。開いたフォルダーの上では中へ、並び替え中は末尾へ入れる
- 触るとき: ドロップ先が上下にずれる、またはフォルダーの中へ入らないとき。ドラッグ元の選択による除外もここで判定する
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsTagQuery()`, `this._controller.disallowInsertion()`
- 条件付き依存: `if (index != -1)` → `this.nodeForTreeIndex()`
- 条件付き依存: `if (index != -1)` → `this.isContainer()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `this._element.view.selection.isSelected()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `this._controller.disallowInsertion()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (!(queryOptions.excludeItems || queryOptions.excludeQueries))` → `container.getChildIndex()`
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUtils.asQuery(container).query.tags`, `PlacesUtils.asQuery(this._result.root).queryOptions`, `container.containerOpen`, `lastSelected.containerOpen`, `lastSelected.hasChildren`, `lastSelected.parent`, `queryOptions.excludeItems`, `queryOptions.excludeQueries`, `queryOptions.sortingMode`, `this._element.isDragSource`, `this._result.root`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## drop()
- 位置: async L1500-1520
- 役割: 挿入点を求めて PlacesControllerDragHelper.onDrop に渡し、終わったらドロップ先の表示を消す。例外は console.error に出す
- 触るとき: ドロップ後の処理が失敗する、またはドロップ先の強調が残るとき
- 呼び出し先: `this._getInsertionPoint()`
- 条件付き依存: `if (ip)` → `PlacesControllerDragHelper.onDrop()`
- 条件付き依存: `if (ip)` → `console.error()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._controller.disableUserActions`, `this._tree`

## PTV_getParentIndex()
- 位置: L1522-1525
- 役割: 行の親の行番号を返す
- 触るとき: 親の行へ移動する操作(キーボードなど)の結果がおかしいとき
- 呼び出し先: `this._getParentByChildRow()`

## PTV_hasNextSibling()
- 位置: L1527-1555
- 役割: 同じ親の次の兄弟があるかを返す。未構築の行は、同じ階層の行が現れるか、より浅い行が現れるまで走査する
- 触るとき: ツリーの線や兄弟の範囲の描画がおかしいとき
- 呼び出し先: `this._getNodeForRow()`, `this._isPlainContainer()`
- 参照: `nextNode.parent`, `node.indentLevel`, `node.parent`, `rowNode.indentLevel`, `this._rows`, `this._rows.length`

## getLevel()
- 位置: L1557-1559
- 役割: 行の階層(indentLevel)を返す
- 触るとき: インデントの深さが実際と合わないとき
- 呼び出し先: `this._getNodeForRow()`
- 参照: `this._getNodeForRow(aRow).indentLevel`

## PTV_getImageSrc()
- 位置: L1561-1569
- 役割: タイトル列では node.icon を返し、他の列では空文字を返す
- 触るとき: アイコンが表示されないとき
- 呼び出し先: `this._getColumnType()`, `this._getNodeForRow()`
- 参照: `node.icon`, `this.COLUMN_TYPE_TITLE`

## getCellValue()
- 位置: L1571-1571
- 役割: セルの値を返さない空の実装
- 触るとき: セル値の API を使いたいとき。この空の実装に当たっていないかを先に確かめる

## PTV_getCellText()
- 位置: L1573-1619
- 役割: 列の種類に応じて表示文字列を返す。タイトルは区切り線を空にし、タグは区切りを読点で置き換え、URL は URL ノードだけ、日付は時刻が 0 でなく URL ノードのときだけ表示する
- 触るとき: 一覧の列に出す文字や、空欄にする条件を変えるとき
- 呼び出し先: `PlacesUIUtils.getBestTitle()`, `PlacesUtils.nodeIsSeparator()`, `PlacesUtils.nodeIsURI()`, `node.tags?.replaceAll()`, `this._convertPRTimeToString()`, `this._getColumnType()`, `this._getNodeForRow()`
- 条件付き依存: `if (node.dateAdded)` → `this._convertPRTimeToString()`
- 条件付き依存: `if (node.lastModified)` → `this._convertPRTimeToString()`
- 参照: `node.accessCount`, `node.dateAdded`, `node.lastModified`, `node.time`, `node.uri`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`

## PTV_setTree()
- 位置: L1621-1643
- 役割: ツリーを差し替える。外すときは結果のルートを閉じてメモリと通知を止め、付けるときは _finishInit を呼ぶ
- 触るとき: ツリーの着脱の際にメモリや監視が残るとき
- 呼び出し先: `this.batching()`
- 条件付き依存: `if (aTree)` → `this._finishInit()`
- 参照: `this._result`, `this._rootNode.containerOpen`, `this._tree`

## PTV_toggleOpenState()
- 位置: L1645-1679
- 役割: フラットリストでは onOpenFlatContainer イベントを送って終わる。通常は URL のあるコンテナーの開閉を xulstore に保存または削除し、開閉を反転させる
- 触るとき: フォルダーの開閉を保存する仕組みを変えるとき、またはフラットリストの展開の動きを変えるとき
- 条件付き依存: `if (!this._result)` → `Components.Exception()`
- 条件付き依存: `if (this._flatList && this._element)` → `this._element.dispatchEvent()`
- 条件付き依存: `if (node.containerOpen)` → `Services.xulStore.removeValue()`
- 条件付き依存: `if (node.containerOpen)` → `PlacesUIUtils.obfuscateUrlForXulStore()`
- 条件付き依存: `if (!(node.containerOpen))` → `Services.xulStore.setValue()`
- 条件付き依存: `if (!(node.containerOpen))` → `PlacesUIUtils.obfuscateUrlForXulStore()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `document.documentURI`, `node.containerOpen`, `node.uri`, `this._element`, `this._flatList`, `this._result`, `this._rows`
- XPCOM: `Services.xulStore`

## PTV_cycleHeader()
- 位置: L1681-1789
- 役割: 列見出しのクリックで並び替えモードを循環させる。タイトル、URL、日付などは昇順、降順の順に変わり、根がフォルダーのときは三段目で並び替え無しに戻る。訪問回数は降順から始まる
- 触るとき: 並び替えの循環の順番を変えるとき。三段目を使うかどうかは根ノードがフォルダーかどうかで決まる
- 呼び出し先: `Components.Exception()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `this._getColumnType()`
- 条件付き依存: `if (!this._result)` → `Components.Exception()`
- 参照: `Ci.nsINavHistoryQueryOptions`, `Cr.NS_ERROR_INVALID_ARG`, `Cr.NS_ERROR_UNEXPECTED`, `NHQO.SORT_BY_DATEADDED_ASCENDING`, `NHQO.SORT_BY_DATEADDED_DESCENDING`, `NHQO.SORT_BY_DATE_ASCENDING`, `NHQO.SORT_BY_DATE_DESCENDING`, `NHQO.SORT_BY_LASTMODIFIED_ASCENDING`, `NHQO.SORT_BY_LASTMODIFIED_DESCENDING`, `NHQO.SORT_BY_NONE`, `NHQO.SORT_BY_TAGS_ASCENDING`, `NHQO.SORT_BY_TAGS_DESCENDING`, `NHQO.SORT_BY_TITLE_ASCENDING`, `NHQO.SORT_BY_TITLE_DESCENDING`, `NHQO.SORT_BY_URI_ASCENDING`, `NHQO.SORT_BY_URI_DESCENDING`, `NHQO.SORT_BY_VISITCOUNT_ASCENDING`, `NHQO.SORT_BY_VISITCOUNT_DESCENDING`, `this.COLUMN_TYPE_DATE`, `this.COLUMN_TYPE_DATEADDED`, `this.COLUMN_TYPE_LASTMODIFIED`, `this.COLUMN_TYPE_TAGS`, `this.COLUMN_TYPE_TITLE`, `this.COLUMN_TYPE_URI`, `this.COLUMN_TYPE_VISITCOUNT`, `this._result`, `this._result.root`, `this._result.sortingMode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PTV_isEditable()
- 位置: L1791-1828
- 役割: 第一列で、ブックマークのノードのうち区切り線、ルート項目、検索クエリで生成されたフォルダー以外を編集可能と返す
- 触るとき: 名前を変更できる項目の範囲を増減させるとき
- 呼び出し先: `PlacesUtils.isRootItem()`, `PlacesUtils.nodeIsQueryGeneratedFolder()`, `PlacesUtils.nodeIsSeparator()`
- 条件付き依存: `if (!node)` → `console.error()`
- 参照: `aColumn.index`, `node.bookmarkGuid`, `this._rows`

## PTV_setCellText()
- 位置: L1830-1838
- 役割: タイトルが変わったときだけ PlacesTransactions の EditTitle を実行して保存する
- 触るとき: 一覧でその場編集した名前が保存されないとき
- 条件付き依存: `if (node.title != aText)` → `PlacesTransactions.EditTitle({ guid: node.bookmarkGuid, title: aText }) .transact() .catch()`
- 条件付き依存: `if (node.title != aText)` → `PlacesTransactions.EditTitle({ guid: node.bookmarkGuid, title: aText }) .transact()`
- 条件付き依存: `if (node.title != aText)` → `PlacesTransactions.EditTitle()`
- 参照: `console.error`, `node.bookmarkGuid`, `node.title`, `this._rows`

## PTV_toggleCutNode()
- 位置: L1840-1851
- 役割: 切り取り対象のノードの集合に追加または削除し、タイトル列のセルを再描画する
- 触るとき: 切り取りの表示が消えないまま残るとき、または切り取りの操作を足すとき
- 呼び出し先: `this._cuttingNodes.has()`
- 条件付き依存: `if (aValue)` → `this._cuttingNodes.add()`
- 条件付き依存: `if (!(aValue))` → `this._cuttingNodes.delete()`
- 条件付き依存: `if (currentVal != aValue)` → `this._invalidateCellValue()`
- 参照: `this.COLUMN_TYPE_TITLE`

## selectionChanged()
- 位置: L1853-1853
- 役割: 選択の変更通知を受けるが、何もしない空の実装
- 触るとき: 選択の変更に応じて処理を足したいとき、ここに実装する

## cycleCell()
- 位置: L1854-1854
- 役割: セルの巡回を処理しない空の実装
- 触るとき: キーボードでセルを移動する動きを足したいとき、ここに実装する
