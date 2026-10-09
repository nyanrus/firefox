# browser/components/places/content/places-tree.js

source: browser/components/places/content/places-tree.js
source-hash: e51d68cd6898e9fc5057ce1017b7f8169a3246c2
lines: 887

## <module>
- 役割: places-tree の要素 (XUL tree を拡張) を定義し、選択・ドラッグ&ドロップ・挿入位置・コンテキストメニューを提供する。
- 呼び出し先: `customElements.define()`, `customElements.get()`

## MozPlacesTree.constructor()
- 位置: L15-132
- 役割: フォーカス、選択、dragstart、dragover、dragend の各リスナーを登録する。
- 触るとき: ツリーにフォーカスや選択を反映させるとき、またはドラッグの許可条件を変えるとき。
- 呼び出し先: `document.commandDispatcher.updateCommands()`, `event.preventDefault()`, `event.stopPropagation()`, `super()`, `this._controller.setDataTransfer()`, `this.addEventListener()`, `this.controller.canMoveNode()`, `this.getCellAt()`, `this.getFirstVisibleRow()`, `this.treeBody.getBoundingClientRect()`, `this.view.canDrop()`, `this.view.nodeForTreeIndex()`, `win.document.commandDispatcher.updateCommands()`
- 条件付き依存: `if (this.disableUserActions)` → `event.preventDefault()`
- 条件付き依存: `if (this.disableUserActions)` → `event.stopPropagation()`
- 条件付き依存: `if (!node.parent)` → `event.preventDefault()`
- 条件付き依存: `if (!node.parent)` → `event.stopPropagation()`
- 条件付き依存: `if (!(cell.row == -1))` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (!( PlacesUtils.nodeIsContainer(node) && eventY > rowHeight * 0.75 ))` → `PlacesUtils.nodeIsContainer()`
- 参照: `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesControllerDragHelper.currentDropTarget`, `cell.row`, `event.clientX`, `event.clientY`, `event.dataTransfer`, `event.dataTransfer.effectAllowed`, `event.target.localName`, `node.parent`, `nodes.length`, `this._cachedInsertionPoint`, `this._isDragSource`, `this.disableUserActions`, `this.result.root`, `this.rowHeight`, `this.selectedNodes`, `this.treeBody.getBoundingClientRect().y`, `win.parent`, `window.top`
- XPCOM: `nsITreeView`

## MozPlacesTree.connectedCallback()
- 位置: L134-150
- 役割: 接続時に active を立て、現在の place で一度ツリーを組み直す。
- 触るとき: ツリーを DOM に追加した直後に中身が空のままになるとき。
- 呼び出し先: `super.connectedCallback()`, `this.delayConnectedCallback()`, `window.addEventListener()`
- 参照: `this._active`, `this._contextMenuShown`, `this.disconnectedCallback`, `this.place`

## MozPlacesTree.controller()
- 位置: L152-154
- 役割: このツリーの PlacesController を返す。
- 触るとき: ツリーからコマンドの処理先を辿るとき。
- 参照: `this._controller`

## MozPlacesTree.disableUserActions()
- 位置: L156-162
- 役割: disableUserActions 属性を設定する。
- 触るとき: ユーザー操作を止めて読み取り専用表示にするとき。
- 条件付き依存: `if (val)` → `this.setAttribute()`
- 条件付き依存: `if (!(val))` → `this.removeAttribute()`

## MozPlacesTree.disableUserActions()
- 位置: L164-166
- 役割: disableUserActions 属性が true かを返す。
- 触るとき: ドラッグや操作を無効にしている状態を確認するとき。
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.view()
- 位置: L173-182
- 役割: 渡されたビューを内部に保存してから、XULTreeElement の view を設定する。
- 触るとき: ツリーのビューを差し替える処理や、古いビューが残るときに確認する。
- 呼び出し先: `Object.getOwnPropertyDescriptor()`, `Object.getOwnPropertyDescriptor( // eslint-disable-next-line no-undef XULTreeElement.prototype, "view" ).set.call()`
- 参照: `XULTreeElement.prototype`, `this._view`

## MozPlacesTree.view()
- 位置: L184-186
- 役割: 内部に保存したビューを返す。
- 触るとき: XUL 側の取得コストを避けて現在のビューを読みたいとき。
- 参照: `this._view`

## MozPlacesTree.associatedElement()
- 位置: L188-190
- 役割: 関連付ける要素として自身を返す。
- 触るとき: コントローラーが自身の要素を参照する経路を変えるとき。

## MozPlacesTree.flatList()
- 位置: L192-201
- 役割: flatList 属性を変え、値が変わったときは最後の place で再読み込みする。
- 触るとき: フラットリスト表示に切り替えたとき、表示が更新されないときに調べる。
- 条件付き依存: `if (this.flatList != val)` → `this.setAttribute()`
- 参照: `this.flatList`, `this.place`

## MozPlacesTree.flatList()
- 位置: L203-205
- 役割: flatList 属性が true かを返す。
- 触るとき: フラット表示かどうかで挿入位置や展開の扱いが変わる箇所を読むとき。
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.result()
- 位置: L207-213
- 役割: ビューから nsINavHistoryResult を取り出す。取得できなければ null を返す。
- 触るとき: ツリーが保持する検索結果へ辿る必要があるとき。
- 呼び出し先: `this.view.QueryInterface()`
- 参照: `Ci.nsINavHistoryResultObserver`, `this.view.QueryInterface(Ci.nsINavHistoryResultObserver).result`
- XPCOM: [`nsINavHistoryResultObserver`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## MozPlacesTree.place()
- 位置: L215-222
- 役割: place 文字列を属性に保存し、クエリに変換して load に渡す。
- 触るとき: ツリーに表示させる検索条件を変えるとき、または place 属性から読み込みが失敗するとき。
- 呼び出し先: `PlacesUtils.history.queryStringToQuery()`, `this.load()`, `this.setAttribute()`
- 参照: `options.value`, `query.value`

## MozPlacesTree.place()
- 位置: L224-226
- 役割: place 属性の値を返す。
- 触るとき: 現在のツリーが表示している place を確認するとき。
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.selectedCount()
- 位置: L228-230
- 役割: 選択中の行数を返す。ビューや選択が無ければ 0。
- 触るとき: 選択数に応じてコマンドの有効・無効を決めるとき。
- 参照: `this.view?.selection?.count`

## MozPlacesTree.hasSelection()
- 位置: L232-234
- 役割: 選択が 1 件以上あるかを返す。
- 触るとき: 選択がないときの挙動を分岐させる判定を読むとき。
- 参照: `this.selectedCount`

## MozPlacesTree.selectedNodes()
- 位置: L236-254
- 役割: 選択範囲の全ノードを配列で返す。
- 触るとき: 複数選択された項目に対して処理をかけるとき、または選択対象の取りこぼしを調べるとき。
- 呼び出し先: `nodes.push()`, `resultview.nodeForTreeIndex()`, `selection.getRangeAt()`, `selection.getRangeCount()`
- 参照: `max.value`, `min.value`, `this.hasSelection`, `this.view`, `this.view.selection`

## MozPlacesTree.removableSelectionRanges()
- 位置: L256-310
- 役割: 選択範囲を範囲ごとに分け、祖先が選ばれている子を除いたノード群を返す。
- 触るとき: 削除や Undo の挿入位置がずれるとき。
- 呼び出し先: `nodes.push()`, `selection.getRangeAt()`, `selection.getRangeCount()`, `this.view.getParentIndex()`, `this.view.isContainer()`
- 条件付き依存: `if (!(this.view.getParentIndex(j) in containers))` → `range.push()`
- 条件付き依存: `if (!(this.view.getParentIndex(j) in containers))` → `resultview.nodeForTreeIndex()`
- 参照: `max.value`, `min.value`, `this.hasSelection`, `this.view`, `this.view.selection`

## MozPlacesTree.draggableSelection()
- 位置: L312-331
- 役割: 選択ノードから、選択済みの祖先を持つものを除いて返す。
- 触るとき: フォルダーとその子をまとめてドラッグしたときに子が二重に動く不具合を調べるとき。
- 呼び出し先: `[...selectedNodes].filter()`, `selectedNodes.has()`
- 参照: `ancestor.parent`, `node.parent`, `this.selectedNodes`

## MozPlacesTree.selectedNode()
- 位置: L333-344
- 役割: 単一選択のときだけそのノードを返し、それ以外は null を返す。
- 触るとき: 1 件選択を前提にした処理がなぜ動かないかを調べるとき。
- 呼び出し先: `selection.getRangeAt()`, `this.view.nodeForTreeIndex()`
- 参照: `min.value`, `this.selectedCount`, `this.view.selection`

## MozPlacesTree.singleClickOpens()
- 位置: L346-348
- 役割: singleclickopens 属性が true かを返す。
- 触るとき: シングルクリックで開く設定に応じてクリック処理を変えるとき。
- 呼び出し先: `this.getAttribute()`

## MozPlacesTree.insertionPoint()
- 位置: L350-419
- 役割: 選択状態から貼り付けや移動の挿入位置を決め、結果をキャッシュする。
- 触るとき: 貼り付けや DnD の挿入先が想定と違うとき。履歴クエリでは null になる点も確認する。
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.nodeIsQuery()`, `resultView.isContainer()`, `selection.getRangeAt()`, `selection.getRangeCount()`, `this._getInsertionPoint()`
- 条件付き依存: `if (!this.hasSelection)` → `this._getInsertionPoint()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUtils.asQuery(resultNode).queryOptions.queryType`, `max.value`, `resultView.selection`, `selection.count`, `this._cachedInsertionPoint`, `this.flatList`, `this.hasSelection`, `this.result.root`, `this.view`, `this.view.rowCount`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## MozPlacesTree.isDragSource()
- 位置: L421-423
- 役割: このツリーがドラッグ元かを返す。
- 触るとき: ドロップ先が同じツリー内からのドラッグかを判定する必要があるとき。
- 参照: `this._isDragSource`

## MozPlacesTree.ownerWindow()
- 位置: L425-427
- 役割: 自身を含むウィンドウを返す。
- 触るとき: ダイアログや通知をどのウィンドウに出すか決めるとき。

## MozPlacesTree.active()
- 位置: L429-431
- 役割: active 状態を設定する。
- 触るとき: 非表示のツリーの更新を止めたり再開したりするとき。
- 参照: `this._active`

## MozPlacesTree.active()
- 位置: L433-435
- 役割: active 状態を返す。
- 触るとき: このツリーがアクティブかどうかを確認するとき。
- 参照: `this._active`

## MozPlacesTree.applyFilter()
- 位置: L437-466
- 役割: 検索語 (と任意でフォルダー範囲) から絞り込みクエリを作り、読み込み直す。
- 触るとき: ブックマーク検索の結果が期待と違うとき、または絞り込みの対象を増やすとき。
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.history.getNewQuery()`, `PlacesUtils.nodeIsHistoryContainer()`, `PlacesUtils.nodeIsTagQuery()`, `queryNode.queryOptions.clone()`, `this.load()`
- 条件付き依存: `if (folderRestrict)` → `query.setParents()`
- 条件付き依存: `if (folderRestrict)` → `Glean.sidebar.search.bookmarks.add()`
- 参照: `options.QUERY_TYPE_BOOKMARKS`, `options.RESULTS_AS_ROOTS_QUERY`, `options.RESULTS_AS_TAGS_ROOT`, `options.RESULTS_AS_URI`, `options.includeHidden`, `options.queryType`, `options.resultType`, `query.searchTerms`, `this.result.root`

## MozPlacesTree.load()
- 位置: L468-493
- 役割: クエリを実行し、ツリービューを作って結果に登録し、必要なら先頭を選択する。
- 触るとき: ツリーの内容を差し替える共通の入口を変えるとき、または表示が古いままのとき。
- 呼び出し先: `PlacesUtils.history.executeQuery()`, `result.addObserver()`, `this.getAttribute()`
- 条件付き依存: `if (!this._controller)` → `this.controllers.appendController()`
- 条件付き依存: `if ( this.getAttribute("selectfirstnode") == "true" && treeView.rowCount > 0 )` → `treeView.selection.select()`
- 参照: `this._cachedInsertionPoint`, `this._controller`, `this._controller.disableUserActions`, `this.disableUserActions`, `this.view`, `treeView.rowCount`

## MozPlacesTree.selectPlaceURI()
- 位置: L503-562
- 役割: 指定 URI のノードを探して選択する。既に選択中ならそのまま返す。
- 触るとき: 特定の URL を選択状態にしたいが見つからないとき。
- 呼び出し先: `console.assert()`, `findNode()`
- 条件付き依存: `if (child)` → `this.selectNode()`
- 条件付き依存: `if (!(child))` → `selection.clearSelection()`
- 参照: `this.hasSelection`, `this.result.root`, `this.selectedNode.uri`, `this.view.selection`

## findNode()
- 位置: L509-546
- 役割: 選んだ URI を、展開しながら深さ優先で探す (訪問済みのクエリは再検索しない)。
- 触るとき: ネストしたフォルダーの中の項目が見つからないとき、探索順や閉じ状態の扱いを確かめるとき。
- 呼び出し先: `container.getChild()`, `nodesURIChecked.includes()`, `nodesURIChecked.push()`
- 条件付き依存: `if (!(childURI == placeURI))` → `PlacesUtils.nodeIsContainer()`
- 条件付き依存: `if (PlacesUtils.nodeIsContainer(child))` → `findNode()`
- 条件付き依存: `if (PlacesUtils.nodeIsContainer(child))` → `PlacesUtils.asContainer()`
- 参照: `child.uri`, `container.childCount`, `container.containerOpen`, `container.uri`

## MozPlacesTree.selectNode()
- 位置: L572-609
- 役割: 親フォルダーを開いてから、ノードを選択して見える位置までスクロールする。
- 触るとき: 選択したノードが開いたフォルダーの中にあって見えないとき。
- 呼び出し先: `this.ensureRowIsVisible()`, `view.selection.select()`, `view.treeIndexForNode()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `parents.push()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `view.treeIndexForNode()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `view.isContainer()`
- 条件付き依存: `if (parent && !parent.containerOpen)` → `view.isContainerOpen()`
- 条件付き依存: `if ( index != -1 && view.isContainer(index) && !view.isContainerOpen(index) )` → `view.toggleOpenState()`
- 参照: `node.parent`, `parent.containerOpen`, `parent.parent`, `parents.length`, `this.result.root`, `this.view`

## MozPlacesTree.toggleCutNode()
- 位置: L611-613
- 役割: 切り取り対象の表示状態をビューに伝える。
- 触るとき: 切り取りした項目の表示が更新されないとき。
- 呼び出し先: `this.view.toggleCutNode()`

## MozPlacesTree._getInsertionPoint()
- 位置: L615-693
- 役割: 選択行とドロップ向きから、親コンテナと挿入インデックスを決めて PlacesInsertionPoint を作る。
- 触るとき: 項目を選んだ位置のどこに貼り付くかが違うとき、または並べ替えのあるビューでの挿入位置を変えるとき。
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsTagQuery()`, `console.assert()`, `this.controller.disallowInsertion()`
- 条件付き依存: `if (index != -1)` → `resultview.nodeForTreeIndex()`
- 条件付き依存: `if (index != -1)` → `resultview.isContainer()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `this.controller.disallowInsertion()`
- 条件付き依存: `if (!( lastSelected.containerOpen && orientation == Ci.nsITreeView.DROP_AFTER && lastSelected.hasChildren ))` → `PlacesUtils.asQuery()`
- 条件付き依存: `if (!(queryOptions.excludeItems || queryOptions.excludeQueries))` → `container.getChildIndex()`
- 参照: `Ci.nsINavHistoryQueryOptions.SORT_BY_NONE`, `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUtils.asQuery(container).query.tags`, `PlacesUtils.asQuery(result.root).queryOptions`, `container.containerOpen`, `lastSelected.containerOpen`, `lastSelected.hasChildren`, `lastSelected.parent`, `queryOptions.excludeItems`, `queryOptions.excludeQueries`, `queryOptions.sortingMode`, `result.root`, `this.result`, `this.view`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## MozPlacesTree.selectAll()
- 位置: L695-697
- 役割: 表示中の全行を選択する。
- 触るとき: 全選択コマンドが効かないとき。
- 呼び出し先: `this.view.selection.selectAll()`

## MozPlacesTree.selectItems()
- 位置: L709-858
- 役割: GUID に一致する項目を探し、必要なフォルダーを開いて選択する。
- 触るとき: ブックマークの編集後に該当項目を選び直すとき、または見つからない項目の扱いを変えるとき。
- 呼び出し先: `findNodes()`, `resultview.treeIndexForNode()`, `selection.clearSelection()`, `selection.rangedSelect()`
- 条件付き依存: `if (firstValidTreeIndex >= 0)` → `this.ensureRowIsVisible()`
- 参照: `nodes.length`, `nodesToOpen.length`, `nodesToOpen[i].containerOpen`, `result.suppressNotifications`, `selection.selectEventsSuppressed`, `this.flatList`, `this.result`, `this.result.root`, `this.view`, `this.view.selection`

## findNodes()
- 位置: L748-815
- 役割: 子を再帰的に探して GUID に一致する項目を集め、見つかったフォルダーを一時的に開く。
- 触るとき: selectItems で見つからない項目が出るとき、または探索範囲を変えるとき。
- 呼び出し先: `PlacesUtils.asContainer()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsContainer()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsQuery()`, `checkedGuidsSet.add()`, `checkedGuidsSet.has()`, `findNodes()`, `guids.indexOf()`, `node.getChild()`
- 条件付き依存: `if (index == -1)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (concreteGuid != node.bookmarkGuid)` → `guids.indexOf()`
- 条件付き依存: `if (index != -1)` → `nodes.push()`
- 条件付き依存: `if (index != -1)` → `guids.splice()`
- 条件付き依存: `if (foundOne)` → `nodesToOpen.unshift()`
- 参照: `PlacesUIUtils.virtualAllBookmarksGuid`, `guids.length`, `node.bookmarkGuid`, `node.childCount`, `node.containerOpen`

## MozPlacesTree.buildContextMenu()
- 位置: L860-863
- 役割: コンテキストメニュー表示済みの印を立て、コントローラーにメニュー構築を任せる。
- 触るとき: 右クリックメニューの項目が出ないとき。
- 呼び出し先: `this.controller.buildContextMenu()`
- 参照: `this._contextMenuShown`

## MozPlacesTree.destroyContextMenu()
- 位置: L865-865
- 役割: 何もしない (メニューの破棄処理は不要)。
- 触るとき: メニュー破棄の後始末を追加する必要があるかを確認するとき。

## MozPlacesTree.disconnectedCallback()
- 位置: L867-880
- 役割: unload リスナーを外し、コントローラーとビューを解放する。
- 触るとき: ツリーを閉じたあとも古いビューが残ってメモリや更新が止まらないとき。
- 呼び出し先: `window.removeEventListener()`
- 条件付き依存: `if (this._controller)` → `this._controller.terminate()`
- 条件付き依存: `if (this._controller)` → `this.controllers.removeController()`
- 条件付き依存: `if (this.view)` → `this.view.uninit()`
- 参照: `this._controller`, `this.disconnectedCallback`, `this.view`
