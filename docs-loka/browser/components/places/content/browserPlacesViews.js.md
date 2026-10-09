# browser/components/places/content/browserPlacesViews.js

source: browser/components/places/content/browserPlacesViews.js
source-hash: 968c6ed81b97d7f4f34005bfd85bdf3e2496f641
lines: 2502

## <module>
- 役割: ブックマークのツールバー、メニュー、パネルビュー (PlacesViewBase と派生の PlacesToolbar、PlacesMenu、PlacesPanelview) を実装する。結果ノードの変化を DOM に反映し、ドラッグ&ドロップや右クリックメニューを扱う。
- 呼び出し先: `ChromeUtils.generateQI()`

## PlacesViewBase.constructor()
- 位置: L18-26
- 役割: ルートと表示要素を保持し、_init を呼んでから PlacesController を作って place を設定し、表示要素にコントローラーを登録する。
- 触るとき: 新しいブックマーク表示を作る経路 (ツールバー、メニュー、パネル) の初期化順序を変えるとき、コントローラーが登録されない問題を調べるとき。
- 呼び出し先: `this._init()`, `this._viewElt.controllers.appendController()`
- 参照: `this._controller`, `this._rootElt`, `this._viewElt`, `this.place`

## PlacesViewBase.associatedElement()
- 位置: L31-33
- 役割: ビューの表示要素 (_viewElt) を返す。
- 触るとき: ビューに対応する要素を外から参照する箇所を変えるとき。
- 参照: `this._viewElt`

## PlacesViewBase.controllers()
- 位置: L35-37
- 役割: 表示要素の controllers を返す。
- 触るとき: ビューに付いたコントローラーの取得や登録の経路を調べるとき。
- 参照: `this._viewElt.controllers`

## PlacesViewBase.rootElement()
- 位置: L42-44
- 役割: ビューのルート要素 (_rootElt) を返す。
- 触るとき: ビューの根となる要素を参照する箇所を変えるとき。
- 参照: `this._rootElt`

## PlacesViewBase.place()
- 位置: L58-60
- 役割: 現在のクエリ文字列 (_place) を返す。
- 触るとき: ビューが表示しているクエリを確認するとき。
- 参照: `this._place`

## PlacesViewBase.place()
- 位置: L61-70
- 役割: クエリ文字列を保存し、queryStringToQuery で変換して executeQuery を実行し、その結果にこのビューを observer として登録する。
- 触るとき: ビューの表示内容を別のクエリに切り替える処理や、結果が更新されない問題を調べるとき。
- 呼び出し先: `history.executeQuery()`, `history.queryStringToQuery()`, `result.addObserver()`
- 参照: `PlacesUtils.history`, `options.value`, `query.value`, `this._place`

## PlacesViewBase.result()
- 位置: L73-75
- 役割: 現在の結果オブジェクト (_result) を返す。
- 触るとき: ビューが保持する結果を参照する箇所を調べるとき。
- 参照: `this._result`

## PlacesViewBase.result()
- 位置: L76-103
- 役割: 古い結果の observer と開いた状態を外し、新しい結果のルートから DOM 対応表を作って containerOpen を true にし、描画 (invalidateContainer) を起こす。null なら表示を捨てる。
- 触るとき: 結果の切り替えや、ビューを空にする処理を変えるとき、古い結果の observer が残る問題を調べるとき。
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 条件付き依存: `if (val)` → `this._domNodes.set()`
- 参照: `this._domNodes`, `this._result`, `this._resultNode`, `this._resultNode.containerOpen`, `this._rootElt`, `this._rootElt._built`, `this._rootElt._placesNode`, `this._rootElt.localName`, `val.root`

## PlacesViewBase._getDOMNodeForPlacesNode()
- 位置: L115-126
- 役割: Places ノードに対応する DOM 要素を対応表から引く。allowMissing が false で無ければ例外を投げる。
- 触るとき: ノードと DOM の対応が無いときの例外や、対応表の作り方を変えるとき。
- 呼び出し先: `this._domNodes.get()`
- 参照: `aPlacesNode.type`

## PlacesViewBase.controller()
- 位置: L128-130
- 役割: ビューの PlacesController を返す。
- 触るとき: コマンドの処理先となるコントローラーを参照する箇所を調べるとき。
- 参照: `this._controller`

## PlacesViewBase.selType()
- 位置: L132-134
- 役割: 選択の種類として「single」を返す。
- 触るとき: 複数選択に対応するビューを作るとき、この既定値を上書きする必要があるとき。

## PlacesViewBase.selectItems()
- 位置: L135-135
- 役割: 何もしない (既定の選択操作の空実装)。
- 触るとき: 項目選択の挙動を持つ派生ビューを作るとき、ここを上書きする。

## PlacesViewBase.selectAll()
- 位置: L136-136
- 役割: 何もしない (全選択の空実装)。
- 触るとき: 全選択に対応するビューを作るとき、ここを上書きする。

## PlacesViewBase.selectedNode()
- 位置: L138-153
- 役割: コンテキストメニューが開いている間、トリガーのノードに対応する Places ノードを返す。ルート要素や対象外なら null。
- 触るとき: 右クリックや操作の対象ノードの判定を変えるとき、ルートを選んだ場合の扱いを調べるとき。
- 参照: `anchor._placesNode`, `anchor.parentNode`, `this._contextMenuShown`, `this._contextMenuShown.triggerNode`, `this._rootElt`

## PlacesViewBase.hasSelection()
- 位置: L155-157
- 役割: selectedNode が null でないかを返す。
- 触るとき: 選択があるときだけ有効になるメニュー項目の判定を変えるとき。
- 参照: `this.selectedNode`

## PlacesViewBase.selectedNodes()
- 位置: L159-162
- 役割: 選択中ノードを 1 件の配列、無ければ空配列で返す。
- 触るとき: 複数対象のコマンド (削除、コピーなど) の対象一覧を調べるとき。
- 参照: `this.selectedNode`

## PlacesViewBase.singleClickOpens()
- 位置: L164-166
- 役割: 常に true を返す。シングルクリックで開く挙動を示す。
- 触るとき: クリックで開く挙動を派生ビューごとに変えたいとき。

## PlacesViewBase.removableSelectionRanges()
- 位置: L168-181
- 役割: 右クリック元がメニューポップアップ、または Places 以外の要素なら空配列を、それ以外なら選択中ノードの配列を返す。
- 触るとき: 削除できる選択範囲の判定を変えるとき、静的な要素上の右クリックで削除が出る問題を調べるとき。
- 参照: `PlacesUIUtils.lastContextMenuTriggerNode`, `popupNode._placesNode`, `popupNode.localName`, `this.selectedNodes`

## PlacesViewBase.draggableSelection()
- 位置: L183-185
- 役割: ドラッグ中の要素 (_draggedElt) を 1 件の配列で返す。
- 触るとき: ドラッグ対象の取り方を変えるとき。
- 参照: `this._draggedElt`

## PlacesViewBase.insertionPoint()
- 位置: L187-238
- 役割: 履歴クエリなら null を返す。選択がなければ末尾、選択があれば選択ノードの前か、フォルダーなら中の末尾を挿入位置にして PlacesInsertionPoint を作る。controller が挿入を禁じると null。
- 触るとき: 貼り付けやドロップの挿入位置の決め方を変えるとき、履歴ビューで挿入を許さない条件を調べるとき。
- 呼び出し先: `PlacesUtils.asQuery()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsQuery()`, `this.controller.disallowInsertion()`
- 条件付き依存: `if (!( !popupNode._placesNode || popupNode._placesNode == this._resultNode || popupNode._placesNode.itemId == -1 || !selectedNode.parent ))` → `container.getChildIndex()`
- 条件付き依存: `if (!( !popupNode._placesNode || popupNode._placesNode == this._resultNode || popupNode._placesNode.itemId == -1 || !selectedNode.parent ))` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(container))` → `PlacesUtils.asQuery()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsITreeView.DROP_BEFORE`, `Ci.nsITreeView.DROP_ON`, `PlacesUIUtils.lastContextMenuTriggerNode`, `PlacesUtils.asQuery(container).query.tags`, `PlacesUtils.asQuery(resultNode).queryOptions.queryType`, `PlacesUtils.bookmarks.DEFAULT_INDEX`, `popupNode._placesNode`, `popupNode._placesNode.itemId`, `selectedNode.parent`, `this._resultNode`, `this.selectedNode`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../../toolkit/components/places/nsINavHistoryService.idl.md) / `nsITreeView`

## PlacesViewBase.buildContextMenu()
- 位置: L240-295
- 役割: 空でないフォルダーのポップアップの余白で右クリックされたら false を返す。それ以外はコマンドを更新し、ブックマークツールバー由来なら表示切替などのサブメニューを挿入したうえで controller に任せる。
- 触るとき: 右クリックメニューの項目 (「他のブックマーク」、ツールバー表示切替、管理メニュー) を変えるとき。
- 呼び出し先: `aPopup.querySelector()`, `bookmarksToolbar?.contains()`, `document.getElementById()`, `existingOtherBookmarksItem?.remove()`, `existingSubmenu?.remove()`, `this.controller.buildContextMenu()`, `window.updateCommands()`
- 条件付き依存: `if (bookmarksToolbar?.contains(aPopup.triggerNode))` → `manageBookmarksMenu.removeAttribute()`
- 条件付き依存: `if (bookmarksToolbar?.contains(aPopup.triggerNode))` → `BookmarkingUI.buildBookmarksToolbarSubmenu()`
- 条件付き依存: `if (bookmarksToolbar?.contains(aPopup.triggerNode))` → `aPopup.insertBefore()`
- 条件付き依存: `if ( aPopup.triggerNode.id === "OtherBookmarks" || aPopup.triggerNode.id === "PlacesChevron" || aPopup.triggerNode.id === "PlacesToolbarItems" || aPopup.triggerN...)` → `BookmarkingUI.buildShowOtherBookmarksMenuItem()`
- 条件付き依存: `if (otherBookmarksMenuItem)` → `aPopup.insertBefore()`
- 条件付き依存: `if (!(bookmarksToolbar?.contains(aPopup.triggerNode)))` → `manageBookmarksMenu.setAttribute()`
- 参照: `aPopup.triggerNode`, `aPopup.triggerNode.id`, `aPopup.triggerNode.parentNode.id`, `menu.nextElementSibling`, `this._contextMenuShown`, `triggerNode._placesNode?.childCount`, `triggerNode?.localName`

## PlacesViewBase.destroyContextMenu()
- 位置: L297-299
- 役割: _contextMenuShown を null に戻す。
- 触るとき: コンテキストメニューの後始末で選択状態が残る問題を調べるとき。
- 参照: `this._contextMenuShown`

## PlacesViewBase.clearAllContents()
- 位置: L301-311
- 役割: ポップアップの子要素を、panel-header 以外すべて削除し、マーカーと空項目の参照を外す。
- 触るとき: ポップアップの中身を全部消すときの範囲 (panel-header を残す条件) を変えるとき。
- 呼び出し先: `kid.classList.contains()`
- 条件付き依存: `if (!kid.classList.contains("panel-header"))` → `kid.remove()`
- 参照: `aPopup._emptyMenuitem`, `aPopup._endMarker`, `aPopup._startMarker`, `aPopup.firstElementChild`, `kid.nextElementSibling`

## PlacesViewBase._cleanPopup()
- 位置: L313-336
- 役割: 開始マーカーと終了マーカーの間にある Places 項目を削除する。aDelay が真なら削除を次の表示時まで遅らせる (macOS のネイティブメニューのゾンビ項目対策、bug 733419)。
- 触るとき: ポップアップ内の項目を消す手順を変えるとき、macOS のネイティブメニューで古い項目が残る問題を調べるとき。
- 呼び出し先: `this._ensureMarkers()`
- 条件付き依存: `if (sibling._placesNode && !aDelay)` → `aPopup.removeChild()`
- 条件付き依存: `if (sibling._placesNode && aDelay)` → `aPopup._delayedRemovals.push()`
- 参照: `aPopup._delayedRemovals`, `aPopup._endMarker`, `aPopup._startMarker`, `child.nextElementSibling`, `sibling._placesNode`

## PlacesViewBase._rebuildPopup()
- 位置: L338-359
- 役割: 結果ノードが開いていれば、既存の項目を消して子を順に作り直し、0 件なら空の表示を出す。最後に _built を true にする。
- 触るとき: フォルダーメニューの中身の作り直し方や、空フォルダーの表示条件を変えるとき。
- 呼び出し先: `this._cleanPopup()`
- 条件付き依存: `if (cc > 0)` → `this._setEmptyPopupStatus()`
- 条件付き依存: `if (cc > 0)` → `document.createDocumentFragment()`
- 条件付き依存: `if (cc > 0)` → `resultNode.getChild()`
- 条件付き依存: `if (cc > 0)` → `this._insertNewItemToPopup()`
- 条件付き依存: `if (cc > 0)` → `aPopup.insertBefore()`
- 条件付き依存: `if (!(cc > 0))` → `this._setEmptyPopupStatus()`
- 参照: `aPopup._built`, `aPopup._endMarker`, `aPopup._placesNode`, `resultNode.childCount`, `resultNode.containerOpen`

## PlacesViewBase._removeChild()
- 位置: L361-363
- 役割: 子要素を DOM から削除する。
- 触るとき: 子要素の削除方法を派生ビューで変えたいとき。
- 呼び出し先: `aChild.remove()`

## PlacesViewBase._setEmptyPopupStatus()
- 位置: L365-391
- 役割: 空のフォルダーの場合は emptyplacesresult を付けて「空」の無効項目を入れ、空でなければ属性と項目を外す。静的な項目があるときは入れない。
- 触るとき: 空フォルダーの表示 (無効項目の文言や出す条件) を変えるとき。
- 条件付き依存: `if (!aPopup._emptyMenuitem)` → `document.createXULElement()`
- 条件付き依存: `if (!aPopup._emptyMenuitem)` → `aPopup._emptyMenuitem.setAttribute()`
- 条件付き依存: `if (!aPopup._emptyMenuitem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (aEmpty)` → `aPopup.setAttribute()`
- 条件付き依存: `if ( !aPopup._startMarker.previousElementSibling && !aPopup._endMarker.nextElementSibling )` → `aPopup.insertBefore()`
- 条件付き依存: `if (!(aEmpty))` → `aPopup.removeAttribute()`
- 条件付き依存: `if (!(aEmpty))` → `aPopup.removeChild()`
- 参照: `aPopup._emptyMenuitem`, `aPopup._emptyMenuitem.className`, `aPopup._endMarker`, `aPopup._endMarker.nextElementSibling`, `aPopup._startMarker.previousElementSibling`

## PlacesViewBase._createDOMNodeForPlacesNode()
- 位置: L393-457
- 役割: ノードの種類に応じて、セパレーター、URL の menuitem、またはフォルダーの menu (中に places-popup を持つ) を作り、label、image、scheme を設定して対応表に入れる。
- 触るとき: メニュー項目の見た目や属性 (ファビコン、scheme、コンテナ属性) を変えるとき。
- 呼び出し先: `this._domNodes.delete()`, `this._domNodes.has()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR)` → `document.createXULElement()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI)` → `document.createXULElement()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI)` → `element.setAttribute()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI)` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_URI))` → `PlacesUtils.containerTypes.includes()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `document.createXULElement()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `element.setAttribute()`
- 条件付き依存: `if (aPlacesNode.type == Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY)` → `element.setAttribute()`
- 条件付き依存: `if (aPlacesNode.type == Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY)` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(aPlacesNode))` → `element.setAttribute()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsTagQuery(aPlacesNode)))` → `PlacesUtils.nodeIsDay()`
- 条件付き依存: `if (PlacesUtils.nodeIsDay(aPlacesNode))` → `element.setAttribute()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsDay(aPlacesNode)))` → `PlacesUtils.nodeIsHost()`
- 条件付き依存: `if (PlacesUtils.nodeIsHost(aPlacesNode))` → `element.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `PlacesUtils.asContainer()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.setAttribute()`
- 条件付き依存: `if (!this._nativeView)` → `popup.setAttribute()`
- 条件付き依存: `if (!this._nativeView)` → `popup.toggleAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `element.appendChild()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `this._domNodes.set()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `element.setAttribute()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUIUtils.getBestTitle()`
- 条件付き依存: `if (icon)` → `element.setAttribute()`
- 条件付き依存: `if (icon)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (!this._domNodes.has(aPlacesNode))` → `this._domNodes.set()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_QUERY`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `aPlacesNode.icon`, `aPlacesNode.type`, `aPlacesNode.uri`, `element._placesNode`, `element.className`, `popup._placesNode`, `this._nativeView`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesViewBase._insertNewItemToPopup()
- 位置: L459-464
- 役割: ノードから DOM 要素を作り、指定の位置に挿入して返す。
- 触るとき: ポップアップに項目を挿入する処理を変えるとき。
- 呼び出し先: `aInsertionNode.insertBefore()`, `this._createDOMNodeForPlacesNode()`

## PlacesViewBase.toggleCutNode()
- 位置: L466-478
- 役割: 対象の要素 (ポップアップならその親の menu) に cutting 属性を付けるか外す。
- 触るとき: 切り取り中の項目の見た目 (半透明など) の判定を変えるとき。
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (aValue)` → `elt.setAttribute()`
- 条件付き依存: `if (!(aValue))` → `elt.removeAttribute()`
- 参照: `elt.localName`, `elt.parentNode`

## PlacesViewBase.nodeURIChanged()
- 位置: L480-497
- 役割: URL が変わったノードの scheme 属性を更新する。
- 触るとき: URL 変更時にアイコンや scheme の表示が古いままになる問題を調べるとき。
- 呼び出し先: `PlacesUIUtils.guessUrlSchemeForUI()`, `elt.setAttribute()`, `this._getDOMNodeForPlacesNode()`
- 参照: `aPlacesNode.uri`, `elt.localName`, `elt.parentNode`

## PlacesViewBase.nodeIconChanged()
- 位置: L499-515
- 役割: ルート以外の要素の image 属性を、一旦外してから新しいアイコンで設定し直す。
- 触るとき: アイコン更新が反映されない問題を調べるとき。
- 呼び出し先: `ChromeUtils.encodeURIForSrcset()`, `elt.removeAttribute()`, `elt.setAttribute()`, `this._getDOMNodeForPlacesNode()`
- 参照: `aPlacesNode.icon`, `elt.localName`, `elt.parentNode`, `this._rootElt`

## PlacesViewBase.nodeTitleChanged()
- 位置: L517-539
- 役割: ルート以外の要素の label を更新する。新しいタイトルが空で、ツールバーボタン以外なら URL から作った名前を使う。
- 触るとき: タイトル変更時の表示名の決め方を変えるとき、空タイトルの扱いを調べるとき。
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (!aNewTitle && elt.localName != "toolbarbutton")` → `elt.setAttribute()`
- 条件付き依存: `if (!aNewTitle && elt.localName != "toolbarbutton")` → `PlacesUIUtils.getBestTitle()`
- 条件付き依存: `if (!(!aNewTitle && elt.localName != "toolbarbutton"))` → `elt.setAttribute()`
- 参照: `elt.localName`, `elt.parentNode`, `this._rootElt`

## PlacesViewBase.nodeRemoved()
- 位置: L541-561
- 役割: 親が構築済みなら子の要素を削除し、空になったら空表示と追加コマンド項目を更新する。
- 触るとき: 項目削除時の DOM 更新や、削除後に空表示が出ない問題を調べるとき。
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt._built)` → `parentElt.removeChild()`
- 条件付き依存: `if (parentElt._startMarker.nextElementSibling == parentElt._endMarker)` → `this._mayAddCommandsItems()`
- 条件付き依存: `if (parentElt._startMarker.nextElementSibling == parentElt._endMarker)` → `this._setEmptyPopupStatus()`
- 参照: `elt.localName`, `elt.parentNode`, `parentElt._built`, `parentElt._endMarker`, `parentElt._startMarker.nextElementSibling`

## PlacesViewBase.nodeHistoryDetailsChanged()
- 位置: L566-566
- 役割: 何もしない。履歴の詳細変更は通知しない設定 (skipHistoryDetailsNotifications) のため。
- 触るとき: 履歴の詳細を表示するビューを作るとき、この空実装と skipHistoryDetailsNotifications を見直す。

## PlacesViewBase.nodeTagsChanged()
- 位置: L567-567
- 役割: 何もしない (タグ変更の通知を無視する空実装)。
- 触るとき: タグ表示を持つビューを作るとき、ここで更新を入れる。

## PlacesViewBase.nodeDateAddedChanged()
- 位置: L568-568
- 役割: 何もしない (追加日変更の通知を無視する空実装)。
- 触るとき: 追加日を表示するビューを作るとき、ここで更新を入れる。

## PlacesViewBase.nodeLastModifiedChanged()
- 位置: L569-569
- 役割: 何もしない (最終更新日変更の通知を無視する空実装)。
- 触るとき: 最終更新日を表示するビューを作るとき、ここで更新を入れる。

## PlacesViewBase.nodeKeywordChanged()
- 位置: L570-570
- 役割: 何もしない (キーワード変更の通知を無視する空実装)。
- 触るとき: キーワードを表示するビューを作るとき、ここで更新を入れる。

## PlacesViewBase.sortingChanged()
- 位置: L571-571
- 役割: 何もしない (並び替え変更の通知を無視する空実装)。
- 触るとき: 並び替えに追従させるビューを作るとき、ここで再構築を入れる。

## PlacesViewBase.batching()
- 位置: L572-572
- 役割: 何もしない (バッチ更新の通知を無視する空実装)。
- 触るとき: バッチ通知に応じて描画を止めたり再開させたりする処理を入れるとき。

## PlacesViewBase.nodeInserted()
- 位置: L574-591
- 役割: 親の要素が構築済みなら、挿入位置 (開始マーカーからの相対位置) に新しい項目を入れ、コマンド項目と空表示を更新する。
- 触るとき: 項目追加時の表示位置の計算や、追加直後に「すべて開く」などが出ない問題を調べるとき。
- 呼び出し先: `Array.prototype.indexOf.call()`, `this._getDOMNodeForPlacesNode()`, `this._insertNewItemToPopup()`, `this._mayAddCommandsItems()`, `this._setEmptyPopupStatus()`
- 参照: `parentElt._built`, `parentElt._endMarker`, `parentElt._startMarker`, `parentElt.children`

## PlacesViewBase.nodeMoved()
- 位置: L593-630
- 役割: 移動した要素を、新しい親の中で新しい位置へ移し替える。親が未構築なら何もしない。ルート自体の移動は無視する。
- 触るとき: 項目の移動時の表示更新や、移動後の位置がずれる問題を調べるとき。
- 呼び出し先: `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt._built)` → `parentElt.removeChild()`
- 条件付き依存: `if (parentElt._built)` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if (parentElt._built)` → `parentElt.insertBefore()`
- 参照: `elt.localName`, `elt.parentNode`, `parentElt._built`, `parentElt._startMarker`, `parentElt.children`, `this._rootElt`

## PlacesViewBase.containerStateChanged()
- 位置: L632-639
- 役割: コンテナが開かれたか閉じられたときに invalidateContainer を呼ぶ。
- 触るとき: フォルダーの開閉に伴う再構築の条件を変えるとき。
- 条件付き依存: `if ( aNewState == Ci.nsINavHistoryContainerResultNode.STATE_OPENED || aNewState == Ci.nsINavHistoryContainerResultNode.STATE_CLOSED )` → `this.invalidateContainer()`
- 参照: `Ci.nsINavHistoryContainerResultNode.STATE_CLOSED`, `Ci.nsINavHistoryContainerResultNode.STATE_OPENED`
- XPCOM: [`nsINavHistoryContainerResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesViewBase._isPopupOpen()
- 位置: L649-651
- 役割: 要素の親が open なら true を返す。派生クラスで上書きできる。
- 触るとき: 開いているポップアップだけ即時に更新する判定を変えるとき。
- 参照: `elt.parentNode.open`

## PlacesViewBase.invalidateContainer()
- 位置: L653-661
- 役割: 対象コンテナの _built を false にし、ポップアップが開いていれば直ちに作り直す。
- 触るとき: コンテナの再構築のきっかけを追加・変更するとき、開いたメニューが古いままになる問題を調べるとき。
- 呼び出し先: `this._getDOMNodeForPlacesNode()`, `this._isPopupOpen()`
- 条件付き依存: `if (this._isPopupOpen(elt))` → `this._rebuildPopup()`
- 参照: `elt._built`

## PlacesViewBase.uninit()
- 位置: L663-686
- 役割: 結果の observer を外して containerOpen を閉じ、コントローラーを終了して表示要素から外し、_placesView を削除する。
- 触るとき: ビューを破棄するときの後始末を変えるとき、破棄後にイベントや observer が残る問題を調べるとき。
- 条件付き依存: `if (this._result)` → `this._result.removeObserver()`
- 条件付き依存: `if (this._controller)` → `this._controller.terminate()`
- 条件付き依存: `if (this._controller)` → `this._viewElt.controllers.removeController()`
- 参照: `this._controller`, `this._result`, `this._resultNode`, `this._resultNode.containerOpen`, `this._viewElt._placesView`

## PlacesViewBase.isRTL()
- 位置: L688-695
- 役割: 表示要素の direction が rtl かを一度だけ判定し、結果を _isRTL に保存して返す。
- 触るとき: RTL の配置に依存する処理 (ドロップの位置やオーバーフローの計算) を調べるとき。
- 呼び出し先: `document.defaultView.getComputedStyle()`
- 参照: `document.defaultView.getComputedStyle(this._viewElt).direction`, `this._isRTL`, `this._viewElt`

## PlacesViewBase.ownerWindow()
- 位置: L697-699
- 役割: このビューが属するウィンドウ (window) を返す。
- 触るとき: ビューのウィンドウを使う処理の対象を確認するとき。

## PlacesViewBase._mayAddCommandsItems()
- 位置: L707-794
- 役割: ルート以外のポップアップで URL 項目が 2 件以上あれば「すべてをタブで開く」と、URL が 1 件以上あれば「フォルダーを共有」を追加し、条件を外れたら取り除く。
- 触るとき: フォルダーメニュー末尾の追加項目の表示条件を変えるとき、共有機能の有効化に伴う表示を調べるとき。
- 条件付き依存: `if (aPopup._endOptOpenAllInTabs)` → `aPopup.removeChild()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `document.createXULElement()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `aPopup.appendChild()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `aPopup._endOptOpenAllInTabs.setAttribute()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `aPopup._endOptOpenAllInTabs.addEventListener()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `PlacesUIUtils.openMultipleLinksInTabs()`
- 条件付き依存: `if (!aPopup._endOptOpenAllInTabs)` → `PlacesUIUtils.getViewForNode()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `document.createXULElement()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `aPopup._endOptShareFolder.setAttribute()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `aPopup._endOptShareFolder.addEventListener()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `ContentSharingUtils.createShareableLinkFromBookmarkFolders()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( numURINodes > 0 && ContentSharingUtils.isEnabled && !aPopup._endOptShareFolder )` → `aPopup.appendChild()`
- 条件付き依存: `if ( aPopup._endOptShareFolder && (!ContentSharingUtils.isEnabled || !numURINodes) )` → `aPopup.removeChild()`
- 参照: `ContentSharingUtils.isEnabled`, `aPopup._endOptOpenAllInTabs`, `aPopup._endOptOpenAllInTabs.className`, `aPopup._endOptSeparator`, `aPopup._endOptSeparator.className`, `aPopup._endOptShareFolder`, `aPopup._endOptShareFolder.className`, `aPopup._placesNode.childCount`, `aPopup.firstElementChild`, `currentChild._placesNode`, `currentChild.localName`, `currentChild.nextElementSibling`, `event.currentTarget`, `event.currentTarget.parentNode._placesNode`, `this._rootElt`

## PlacesViewBase._ensureMarkers()
- 位置: L796-832
- 役割: Places 項目を挟む、非表示の開始・終了の区切り要素を作り、先頭の静的項目や afterplacescontent の位置に合わせて配置する。
- 触るとき: Places 項目と静的な項目の並び順を変えるとき、区切りの位置がずれる問題を調べるとき。
- 呼び出し先: `aPopup.appendChild()`, `aPopup.insertBefore()`, `child.hasAttribute()`, `document.createXULElement()`
- 条件付き依存: `if (child.hasAttribute("afterplacescontent"))` → `aPopup.insertBefore()`
- 条件付き依存: `if (child._placesNode && !child._placesView && !firstNonStaticNodeFound)` → `aPopup.insertBefore()`
- 条件付き依存: `if (!firstNonStaticNodeFound)` → `aPopup.insertBefore()`
- 参照: `aPopup._endMarker`, `aPopup._endMarker.hidden`, `aPopup._startMarker`, `aPopup._startMarker.hidden`, `aPopup.children`, `aPopup.firstElementChild`, `child._placesNode`, `child._placesView`

## PlacesViewBase._onPopupShowing()
- 位置: L834-866
- 役割: マーカーを確保し、遅延削除分を消す。このビューのフォルダーなら、再帰するショートカットは空として表示し、そうでなければ開いて未構築なら作り直し、コマンド項目を更新する。
- 触るとき: フォルダーメニューを開いたときの読み込みや、再帰ショートカットの表示を変えるとき。
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `this._ensureMarkers()`
- 条件付き依存: `if ("_delayedRemovals" in popup)` → `popup.removeChild()`
- 条件付き依存: `if ("_delayedRemovals" in popup)` → `popup._delayedRemovals.shift()`
- 条件付き依存: `if (popup._placesNode && PlacesUIUtils.getViewForNode(popup) == this)` → `this.#isPopupForRecursiveFolderShortcut()`
- 条件付き依存: `if (this.#isPopupForRecursiveFolderShortcut(popup))` → `this._setEmptyPopupStatus()`
- 条件付き依存: `if (!popup._built)` → `this._rebuildPopup()`
- 条件付き依存: `if (popup._placesNode && PlacesUIUtils.getViewForNode(popup) == this)` → `this._mayAddCommandsItems()`
- 参照: `aEvent.originalTarget`, `popup._built`, `popup._delayedRemovals.length`, `popup._placesNode`, `popup._placesNode.containerOpen`

## PlacesViewBase._addEventListeners()
- 位置: L868-872
- 役割: 指定のイベント名すべてに、このオブジェクトをリスナーとして登録する。
- 触るとき: ビューに監視するイベントを追加するとき。
- 呼び出し先: `aObject.addEventListener()`
- 参照: `aEventNames.length`

## PlacesViewBase._removeEventListeners()
- 位置: L874-878
- 役割: 指定のイベント名すべてについて、このオブジェクトのリスナー登録を外す。
- 触るとき: ビューの後始末でイベントの登録解除の漏れを調べるとき。
- 呼び出し先: `aObject.removeEventListener()`
- 参照: `aEventNames.length`

## PlacesViewBase.#isPopupForRecursiveFolderShortcut()
- 位置: L887-905
- 役割: フォルダーのショートカットが、親のビューにすでに現れるフォルダーを指していれば true を返す。祖先をたどって guid を比べる。
- 触るとき: フォルダーの再帰的なショートカットで無限に展開される問題を調べるとき、判定条件を変えるとき。
- 呼び出し先: `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `parentView._placesNode`, `parentView.parentNode?.parentNode`, `parentView?._placesNode`, `popup._placesNode`, `popup.parentNode?.parentNode`

## PlacesToolbar.constructor()
- 位置: L917-950
- 役割: ツールバーの初期化時間を計測しつつ基底を作り、ドラッグと各種ポップアップのイベント、ウィンドウの unload を登録する。ResizeObserver を付け、タブバー上ならタブの開閉も監視する。
- 触るとき: ブックマークツールバーの初期化で登録されるイベントや、タブバーに置かれた場合の挙動を変えるとき。
- 呼び出し先: `Glean.bookmarksToolbar.init.start()`, `Glean.bookmarksToolbar.init.stopAndAccumulate()`, `document.getElementById()`, `super()`, `this._addEventListeners()`, `this._resizeObserver.observe()`, `this.updateNodesVisibility()`
- 条件付き依存: `if ( this._viewElt.parentNode.parentNode == document.getElementById("TabsToolbar") )` → `this._addEventListeners()`
- 参照: `gBrowser.tabContainer`, `this._cbEvents`, `this._dragRoot`, `this._resizeObserver`, `this._rootElt`, `this._viewElt.parentNode.parentNode`

## PlacesToolbar._init()
- 位置: L958-990
- 役割: ドロップ先の状態 (_overFolder) を用意し、ドロップ表示やシェブロンの要素を遅延取得する getter を定義し、_placesView を設定してドラッグ用のルートを決める。
- 触るとき: ツールバーの内部状態や要素参照の作り方を変えるとき。基底の constructor から呼ばれる点に注意。
- 呼び出し先: `BookmarkingUI.toolbar.contains()`, `document.getElementById()`, `thisView.__defineGetter__()`
- 参照: `BookmarkingUI.toolbar`, `this._dragRoot`, `this._overFolder`, `this._viewElt`, `this._viewElt._placesView`

## PlacesToolbar.uninit()
- 位置: L1010-1043
- 役割: ツールバーに登録したイベント、ResizeObserver、タブの監視、シェブロンと「他のブックマーク」の子ビューを外してから基底の uninit を呼ぶ。
- 触るとき: ツールバーを破棄するときの後始末漏れを調べるとき。
- 呼び出し先: `super.uninit()`, `this._chevronPopup.uninit()`, `this._removeEventListeners()`
- 条件付き依存: `if (this._dragRoot)` → `this._removeEventListeners()`
- 条件付き依存: `if (this._resizeObserver)` → `this._resizeObserver.disconnect()`
- 条件付き依存: `if (this._chevron._placesView)` → `this._chevron._placesView.uninit()`
- 条件付き依存: `if (this._otherBookmarks?._placesView)` → `this._otherBookmarks._placesView.uninit()`
- 参照: `gBrowser.tabContainer`, `this._cbEvents`, `this._chevron._placesView`, `this._dragRoot`, `this._otherBookmarks?._placesView`, `this._resizeObserver`, `this._rootElt`

## PlacesToolbar.promiseRebuilt()
- 位置: L1048-1050
- 役割: 進行中の再構築の Promise を返す。再構築中でなければ undefined。
- 触るとき: ツールバーの再構築完了を待つ処理を追加するとき。
- 参照: `this._rebuilding?.promise`

## PlacesToolbar._isAlive()
- 位置: L1052-1054
- 役割: 結果とルート要素の両方が残っているかを返す。非同期処理の途中で破棄されていないかの確認に使う。
- 触るとき: 非同期の再構築や表示更新で、破棄後に DOM を触らないための判定を変えるとき。
- 参照: `this._resultNode`, `this._rootElt`

## PlacesToolbar._runBeforeFrameRender()
- 位置: L1056-1066
- 役割: requestAnimationFrame の中で callback を実行し、その結果で解決する Promise を返す。例外は reject する。
- 触るとき: 描画の直前に DOM を操作する処理を追加するとき。
- 呼び出し先: `callback()`, `reject()`, `resolve()`, `window.requestAnimationFrame()`

## PlacesToolbar._rebuild()
- 位置: async L1068-1146
- 役割: ドロップ先の状態を消し、ツールバーの子を全部消してから、1 フレーム目に画面に入りそうな数 (画面幅の 1.5 倍を項目の高さで割った数) を作り、残りを次のフレームで追加する。最後にシェブロンを作り直し、「他のブックマーク」を再表示する。
- 触るとき: ツールバーの作り直し方、初期表示の件数の見積もり、再構築後に「他のブックマーク」を出す条件を変えるとき。
- 呼び出し先: `BookmarkingUI.maybeShowOtherBookmarksFolder()`, `BookmarkingUI.maybeShowOtherBookmarksFolder().catch()`, `document.getElementById()`, `otherBookmarks?.remove()`, `this._chevronPopup.hasAttribute()`, `this._rootElt.firstChild.remove()`, `this._rootElt.hasChildNodes()`
- 条件付き依存: `if (this._overFolder.elt)` → `this._clearOverFolder()`
- 条件付き依存: `if (cc > 0)` → `this._runBeforeFrameRender()`
- 条件付き依存: `if (cc > 0)` → `this._insertNewItem()`
- 条件付き依存: `if (cc > 0)` → `this._resultNode.getChild()`
- 条件付き依存: `if (cc > 0)` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (cc > 0)` → `Math.min()`
- 条件付き依存: `if (cc > 0)` → `parseInt()`
- 条件付き依存: `if (cc > 0)` → `document.createDocumentFragment()`
- 条件付き依存: `if (cc > 0)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (cc > 0)` → `this._rootElt.appendChild()`
- 条件付き依存: `if (cc > 0)` → `this.updateNodesVisibility()`
- 参照: `console.error`, `elt.clientHeight`, `elt.localName`, `this._chevronPopup.place`, `this._isAlive`, `this._openedMenuButton`, `this._overFolder.elt`, `this._resultNode.childCount`, `this._rootElt`, `this.place`, `window.screen.width`

## PlacesToolbar._insertNewItem()
- 位置: L1148-1206
- 役割: ノードの種類に応じて、区切り線、フォルダー用のメニュー型ボタン (places-popup 付き)、URL のボタンを作り、アイコンを付けて指定位置に挿入する。
- 触るとき: ツールバーのボタンの種類や属性 (type=menu、container、scheme) を変えるとき。
- 呼び出し先: `this._domNodes.delete()`, `this._domNodes.has()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR)` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `button.setAttribute()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUtils.containerTypes.includes()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `PlacesUtils.nodeIsQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(aChild))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.nodeIsQuery(aChild))` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if (PlacesUtils.nodeIsTagQuery(aChild))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `document.createXULElement()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.setAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.toggleAttribute()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `popup.classList.add()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `button.appendChild()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `PlacesUtils.asContainer()`
- 条件付き依存: `if (PlacesUtils.containerTypes.includes(type))` → `this._domNodes.set()`
- 条件付き依存: `if (!(PlacesUtils.containerTypes.includes(type)))` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(aChild))` → `button.setAttribute()`
- 条件付き依存: `if (PlacesUtils.nodeIsURI(aChild))` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (icon)` → `button.setAttribute()`
- 条件付き依存: `if (!this._domNodes.has(aChild))` → `this._domNodes.set()`
- 条件付き依存: `if (aBefore)` → `aInsertionNode.insertBefore()`
- 条件付き依存: `if (!(aBefore))` → `aInsertionNode.appendChild()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `aChild.title`, `aChild.type`, `aChild.uri`, `button._placesNode`, `button.className`, `popup._placesNode`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesToolbar._updateChevronPopupNodesVisibility()
- 位置: L1208-1219
- 役割: シェブロンのポップアップの項目を、ツールバーの同じ位置の項目の表示状態 (visibility) に合わせて隠す。
- 触るとき: オーバーフローしたボタンがシェブロンに正しく出ない問題を調べるとき。
- 参照: `node.hidden`, `node.nextElementSibling`, `this._chevronPopup._startMarker.nextElementSibling`, `this._rootElt.firstElementChild`, `toolbarNode.nextElementSibling`, `toolbarNode.style.visibility`

## PlacesToolbar._onChevronPopupShowing()
- 位置: L1221-1232
- 役割: シェブロンのポップアップが開いたとき、まだ無ければ PlacesMenu を作って中身を表示し、項目の表示を合わせる。
- 触るとき: シェブロンの遅延初期化の条件や、開いたときの表示を変えるとき。
- 呼び出し先: `this._updateChevronPopupNodesVisibility()`
- 参照: `aEvent.target`, `this._chevron._placesView`, `this._chevronPopup`, `this.place`

## PlacesToolbar._onOtherBookmarksPopupShowing()
- 位置: L1234-1245
- 役割: 「他のブックマーク」のポップアップが開いたとき、未分類のブックマーク (unfiled) を対象に PlacesMenu を遅延作成する。
- 触るとき: 「他のブックマーク」メニューの中身の作り方を変えるとき。
- 参照: `PlacesUtils.bookmarks.unfiledGuid`, `aEvent.target`, `this._otherBookmarks._placesView`, `this._otherBookmarksPopup`

## PlacesToolbar.handleEvent()
- 位置: L1247-1308
- 役割: イベントの種類に応じて、unload、オーバーフロー、タブの開閉、ドラッグ、マウス、ポップアップの各ハンドラーに振り分ける。未知のイベントは例外。
- 触るとき: ツールバーが扱うイベントを増やすとき、振り分け先を変えるとき。
- 呼び出し先: `aEvent.stopPropagation()`, `this._isOverflowStateEventRelevant()`, `this._onDragEnd()`, `this._onDragLeave()`, `this._onDragOver()`, `this._onDragStart()`, `this._onDrop()`, `this._onMouseDown()`, `this._onMouseMove()`, `this._onMouseOut()`, `this._onMouseOver()`, `this._onOverflow()`, `this._onPopupHidden()`, `this._onPopupShowing()`, `this._onUnderflow()`, `this.uninit()`, `this.updateNodesVisibility()`
- 参照: `aEvent.type`

## PlacesToolbar._isOverflowStateEventRelevant()
- 位置: L1310-1313
- 役割: オーバーフローのイベントが自要素に対するもので、横方向 (detail > 0) のときだけ true を返す。
- 触るとき: 子要素からのオーバーフロー通知を無視する条件を変えるとき。
- 参照: `aEvent.currentTarget`, `aEvent.detail`, `aEvent.target`

## PlacesToolbar._onOverflow()
- 位置: L1315-1324
- 役割: まだ無ければシェブロンのポップアップに place と type を設定し、シェブロンを表示して表示件数を更新する。
- 触るとき: ツールバーがはみ出したときのシェブロン表示の挙動を変えるとき。
- 呼び出し先: `this._chevronPopup.hasAttribute()`, `this.updateNodesVisibility()`
- 条件付き依存: `if (!this._chevronPopup.hasAttribute("type"))` → `this._chevronPopup.setAttribute()`
- 参照: `this._chevron.collapsed`, `this.place`

## PlacesToolbar._onUnderflow()
- 位置: L1326-1329
- 役割: 表示件数を更新してからシェブロンを畳む。
- 触るとき: はみ出しが解消されたときにシェブロンを隠す条件を変えるとき。
- 呼び出し先: `this.updateNodesVisibility()`
- 参照: `this._chevron.collapsed`

## PlacesToolbar.updateNodesVisibility()
- 位置: L1331-1339
- 役割: 既存のタイマーを取り消し、100ms の一度きりのタイマーを張り直して表示件数の更新を遅らせる。
- 触るとき: 表示件数の更新頻度 (100ms のデバウンス) を変えるとき、連続する変更で更新が走りすぎる問題を調べるとき。
- 呼び出し先: `this._setTimer()`
- 条件付き依存: `if (this._updateNodesVisibilityTimer)` → `this._updateNodesVisibilityTimer.cancel()`
- 参照: `this._updateNodesVisibilityTimer`

## PlacesToolbar._updateNodesVisibilityTimerCallback()
- 位置: async L1341-1404
- 役割: ツールバーの子を左から順に測り、ルートの範囲に収まる件数を求める。ウィンドウが無効、またはレイアウトが無ければ 1 回だけ次のフレームで再試行する。次のフレームで子の数が変わっていなければ _applyChildVisibility を呼ぶ。
- 触るとき: どのブックマークが収まり、どれがシェブロンに回るかの判定を変えるとき、レイアウトの無いときの再試行を調べるとき。
- 呼び出し先: `dwu.getBoundsWithoutFlushing()`, `this._applyChildVisibility()`, `window.promiseDocumentFlushed()`, `window.requestAnimationFrame()`
- 条件付き依存: `if (!this.#pendingVisibilityRetry)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (this._isAlive)` → `this.updateNodesVisibility()`
- 条件付き依存: `if (this._rootElt.children.length != measuredCount)` → `this.updateNodesVisibility()`
- 参照: `childRect.left`, `childRect.right`, `scrollRect.left`, `scrollRect.right`, `scrollRect.width`, `this.#pendingVisibilityRetry`, `this.#updatingNodesVisibility`, `this._isAlive`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.children.length`, `this.isRTL`, `window.closed`, `window.windowUtils`

## PlacesToolbar._applyChildVisibility()
- 位置: L1406-1430
- 役割: 収まる件数までの子に画像を付けて表示し、残りを隠す。シェブロンが開いていれば同期し、BookmarksToolbarVisibilityUpdated を発火する。
- 触るとき: オーバーフローの表示切り替えの結果をほかの UI に伝える処理を変えるとき。
- 呼び出し先: `this._viewElt.dispatchEvent()`
- 条件付き依存: `if (icon)` → `child.setAttribute()`
- 条件付き依存: `if (i < visibleCount)` → `child.style.removeProperty()`
- 条件付き依存: `if (!(i < visibleCount))` → `child.removeAttribute()`
- 条件付き依存: `if (!this._chevron.collapsed && this._chevron.open)` → `this._updateChevronPopupNodesVisibility()`
- 参照: `child._placesNode.icon`, `child.style.visibility`, `children.length`, `this._chevron.collapsed`, `this._chevron.open`, `this._rootElt.children`

## PlacesToolbar.nodeInserted()
- 位置: L1432-1477
- 役割: ツールバー直下への追加では、構築済みの数を揃えるために必要なら末尾を外し、項目を作って挿入する。収まらない位置の追加は作らない。他の親は基底に任せる。
- 触るとき: ツールバーへの項目追加時の描画の範囲や、末尾の扱いを変えるとき。
- 呼び出し先: `super.nodeInserted()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (this._resultNode.childCount - 1 > children.length)` → `this._rootElt.removeChild()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._insertNewItem()`
- 条件付き依存: `if (icon)` → `button.setAttribute()`
- 条件付き依存: `if (icon)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (!(prevSiblingOverflowed))` → `this.updateNodesVisibility()`
- 参照: `aPlacesNode.icon`, `button.style.visibility`, `children.length`, `children[aIndex - 1].style.visibility`, `this._resultNode.childCount`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.lastElementChild`

## PlacesToolbar.nodeRemoved()
- 位置: L1479-1510
- 役割: ツールバー直下の項目を削除し、構築済みの数を揃えるため次の項目を作る。隠れていた項目の削除なら表示更新を省く。
- 触るとき: ツールバーから項目を消したときに次の項目が補充されない問題を調べるとき。
- 呼び出し先: `super.nodeRemoved()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._removeChild()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._insertNewItem()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._resultNode.getChild()`
- 条件付き依存: `if (!overflowed)` → `this.updateNodesVisibility()`
- 参照: `elt.localName`, `elt.parentNode`, `elt.style.visibility`, `this._resultNode.childCount`, `this._rootElt`, `this._rootElt.children.length`

## PlacesToolbar.nodeMoved()
- 位置: L1512-1582
- 役割: ツールバー内での移動を、構築範囲内なら要素を取り外して新しい位置に挿入する。範囲外なら必要な分だけ作る。最後に表示件数を更新する。
- 触るとき: ツールバー内のドラッグ移動の結果が画面に反映されない問題を調べるとき。
- 呼び出し先: `super.nodeMoved()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (elt)` → `this._removeChild()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._insertNewItem()`
- 条件付き依存: `if (this._resultNode.childCount > this._rootElt.children.length)` → `this._resultNode.getChild()`
- 条件付き依存: `if (!elt)` → `this._insertNewItem()`
- 条件付き依存: `if (icon)` → `elt.setAttribute()`
- 条件付き依存: `if (icon)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (!(!elt))` → `this._rootElt.insertBefore()`
- 条件付き依存: `if (parentElt == this._rootElt)` → `this.updateNodesVisibility()`
- 参照: `aPlacesNode.icon`, `elt.localName`, `elt.parentNode`, `this._resultNode.childCount`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.children.length`

## PlacesToolbar.nodeTitleChanged()
- 位置: L1584-1605
- 役割: ルート以外の要素で基底のタイトル更新を呼び、ツールバー直下で表示されている項目なら表示件数を更新する。
- 触るとき: タイトル変更で幅が変わり、オーバーフローの判定がずれる問題を調べるとき。
- 呼び出し先: `super.nodeTitleChanged()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (elt.style.visibility != "hidden")` → `this.updateNodesVisibility()`
- 参照: `elt.localName`, `elt.parentNode`, `elt.style.visibility`, `this._rootElt`

## PlacesToolbar.invalidateContainer()
- 位置: L1607-1632
- 役割: 対象がツールバー自身なら、再構築の Promise を作って _rebuild を走らせ、終わったら完了を通知する。それ以外は基底に任せる。
- 触るとき: ツールバー全体の再構築の条件や、完了通知のタイミングを変えるとき。
- 呼び出し先: `super.invalidateContainer()`, `this._getDOMNodeForPlacesNode()`
- 条件付き依存: `if (!this._rebuilding)` → `Promise.withResolvers()`
- 条件付き依存: `if (elt == this._rootElt)` → `this._rebuild() .catch(console.error) .finally()`
- 条件付き依存: `if (elt == this._rootElt)` → `this._rebuild() .catch()`
- 条件付き依存: `if (elt == this._rootElt)` → `this._rebuild()`
- 条件付き依存: `if (instance == this._rebuildingInstance)` → `this._rebuilding.resolve()`
- 参照: `console.error`, `this._rebuilding`, `this._rebuildingInstance`, `this._rootElt`

## PlacesToolbar._clearOverFolder()
- 位置: L1634-1653
- 役割: ドラッグ中に開いていたフォルダーのメニューを閉じ (dragover が無い場合)、dragover 属性と二つのタイマーを消す。
- 触るとき: ドラッグで開いたフォルダーメニューが閉じない、または閉じすぎる問題を調べるとき。
- 条件付き依存: `if (this._overFolder.elt && this._overFolder.elt.menupopup)` → `this._overFolder.elt.menupopup.hasAttribute()`
- 条件付き依存: `if (!this._overFolder.elt.menupopup.hasAttribute("dragover"))` → `this._overFolder.elt.menupopup.hidePopup()`
- 条件付き依存: `if (this._overFolder.elt && this._overFolder.elt.menupopup)` → `this._overFolder.elt.removeAttribute()`
- 条件付き依存: `if (this._overFolder.openTimer)` → `this._overFolder.openTimer.cancel()`
- 条件付き依存: `if (this._overFolder.closeTimer)` → `this._overFolder.closeTimer.cancel()`
- 参照: `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.elt.menupopup`, `this._overFolder.openTimer`

## PlacesToolbar._getDropPoint()
- 位置: L1666-1791
- 役割: ドロップ位置を求める。フォルダーではボタン幅の 25% で前・中・後を分け、通常の項目では 50% で前後を分ける。シェブロンは末尾に、余白では最初に位置が合う項目の前に入れる。挿入点、表示位置、開くフォルダーを返す。
- 触るとき: ツールバーへのドロップ先の判定 (前後や中に入る境界) を変えるとき、ドロップ位置がずれる問題を調べるとき。
- 呼び出し先: `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `elt.getBoundingClientRect()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if ( elt._placesNode && elt != this._rootElt && elt.localName != "menupopup" )` → `PlacesUIUtils.isFolderReadOnly()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.right - threshold : aEvent.clientX < eltRect.left + threshold )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.right - threshold )` → `PlacesUtils.nodeIsTagQuery()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.right - threshold )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.right - threshold ))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if ( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.left + threshold )` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!( this.isRTL ? aEvent.clientX > eltRect.left + threshold : aEvent.clientX < eltRect.left + threshold ))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (elt == this._chevron)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!(elt == this._chevron))` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!(elt == this._chevron))` → `Math.round()`
- 条件付き依存: `if (!(elt == this._chevron))` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!(elt == this._chevron))` → `canInsertHere()`
- 参照: `Ci.nsITreeView.DROP_BEFORE`, `aEvent.clientX`, `aEvent.target`, `dropPoint.beforeIndex`, `dropPoint.folderElt`, `dropPoint.ip`, `dropPoint.ip.index`, `elt._placesNode`, `elt._placesNode.title`, `elt.localName`, `eltRect.left`, `eltRect.right`, `eltRect.width`, `rect.left`, `rect.right`, `this._chevron`, `this._resultNode`, `this._rootElt`, `this._rootElt.children`, `this._rootElt.children.length`, `this.isRTL`
- XPCOM: `nsITreeView`

## PlacesToolbar._setTimer()
- 位置: L1793-1797
- 役割: 一度きりの nsITimer を作って、100ms などの指定時間後に notify を呼ぶ。
- 触るとき: ツールバーで時間差の処理 (ドラッグ中のフォルダーを開く、閉じる) を追加するとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `timer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## PlacesToolbar.name()
- 位置: L1799-1801
- 役割: nsINamed 用に「PlacesToolbar」を返す。
- 触るとき: タイマーなどの識別名を変えるとき。

## PlacesToolbar.notify()
- 位置: L1803-1837
- 役割: タイマーの種類に応じて動く。表示更新のタイマーなら更新を実行し、フォルダーを開くタイマーならそのメニューを開き、閉じるタイマーなら、ドラッグ先がツールバー内なら、そのフォルダーのメニューは閉じずにタイマーと状態だけを消す。
- 触るとき: ドラッグ中のフォルダーの開閉の挙動を変えるとき、タイマーの追加や並び替えを行うとき。
- 条件付き依存: `if (aTimer == this._updateNodesVisibilityTimer)` → `this._updateNodesVisibilityTimerCallback()`
- 条件付き依存: `if (aTimer == this._overFolder.openTimer)` → `this._overFolder.elt.menupopup.setAttribute()`
- 条件付き依存: `if (aTimer == this._overFolder.closeTimer)` → `this._clearOverFolder()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `currentPlacesNode.parentNode`, `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.elt.open`, `this._overFolder.openTimer`, `this._rootElt`, `this._updateNodesVisibilityTimer`

## PlacesToolbar._onMouseOver()
- 位置: L1839-1848
- 役割: ツールバー直下の URL ボタン上にマウスが乗ったら、そのリンク先を XULBrowserWindow の setOverLink で表示する。
- 触るとき: ツールバーのボタンにマウスを乗せたときのステータス表示を変えるとき。
- 呼び出し先: `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if ( button.parentNode == this._rootElt && button._placesNode && PlacesUtils.nodeIsURI(button._placesNode) )` → `window.XULBrowserWindow.setOverLink()`
- 参照: `aEvent.target`, `aEvent.target._placesNode.uri`, `button._placesNode`, `button.parentNode`, `this._rootElt`

## PlacesToolbar._onMouseOut()
- 位置: L1850-1852
- 役割: マウスが離れたら、リンク先の表示を空にする。
- 触るとき: リンク先の表示が残る問題を調べるとき。
- 呼び出し先: `window.XULBrowserWindow.setOverLink()`

## PlacesToolbar._onMouseDown()
- 位置: L1854-1869
- 役割: メニュー型ボタンを左クリックで Shift か Accel を押しているときは、ポップアップを開かないようにする。右クリック以外のマウス押下で投機的接続を行う。
- 触るとき: フォルダーボタンを修飾キー付きでクリックしたときの「すべてをタブで開く」動作を変えるとき。
- 呼び出し先: `PlacesUIUtils.maybeSpeculativeConnectOnMouseDown()`, `target.getAttribute()`
- 条件付き依存: `if ( aEvent.button == 0 && target.localName == "toolbarbutton" && target.getAttribute("type") == "menu" )` → `aEvent.getModifierState()`
- 参照: `aEvent.button`, `aEvent.shiftKey`, `aEvent.target`, `target.localName`, `this._allowPopupShowing`

## PlacesToolbar._cleanupDragDetails()
- 位置: L1871-1876
- 役割: ドラッグの対象と現在のドロップ先を消し、ドロップ位置の表示を隠す。
- 触るとき: ドラッグ終了や破棄の後始末に残りが出る問題を調べるとき。
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._draggedElt`, `this._dropIndicator.collapsed`

## PlacesToolbar._onDragStart()
- 位置: L1878-1914
- 役割: ツールバー直下の項目のドラッグを開始する。フォルダーを下方向に引いた場合はドラッグせずにメニューを開き、それ以外は対象を記録してデータを設定する。
- 触るとき: ツールバーの項目のドラッグ開始条件 (フォルダーを開く操作との区別) を変えるとき。
- 呼び出し先: `aEvent.stopPropagation()`, `draggedElt.getAttribute()`, `this._controller.setDataTransfer()`, `this._rootElt.focus()`
- 条件付き依存: `if ( draggedElt.localName == "toolbarbutton" && draggedElt.getAttribute("type") == "menu" )` → `Math.abs()`
- 条件付き依存: `if (translateY >= Math.abs(translateX / 2))` → `aEvent.preventDefault()`
- 条件付き依存: `if (draggedElt.open)` → `draggedElt.menupopup.hidePopup()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.target`, `draggedElt._placesNode`, `draggedElt.localName`, `draggedElt.open`, `draggedElt.parentNode`, `this._cachedMouseMoveEvent.clientX`, `this._cachedMouseMoveEvent.clientY`, `this._draggedElt`, `this._rootElt`

## PlacesToolbar.#findPrecedingToolbarWidget()
- 位置: L1922-1942
- 役割: ブックマーク領域より前にある、表示中の最後のツールバー要素を返す。無ければ null。
- 触るとき: 項目が 1 件も無いときのドロップ位置の基準を変えるとき。
- 呼び出し先: `child.getBoundingClientRect()`, `this._rootElt.closest()`
- 参照: `child.collapsed`, `child.getBoundingClientRect().width`, `child.hidden`, `toolbar.children`

## PlacesToolbar._onDragOver()
- 位置: L1944-2037
- 役割: ドロップ先を求め、フォルダーかシェブロンの上ならそのメニューを一定時間後に開く。通常の項目の上なら、ドロップ位置の表示をツールバーの向き (RTL も含む) に合わせて動かす。
- 触るとき: ツールバーへのドラッグ時の表示 (ドロップ位置の線、フォルダーの自動展開) を変えるとき。
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `aEvent.preventDefault()`, `aEvent.stopPropagation()`, `this._getDropPoint()`
- 条件付き依存: `if ( !dropPoint || !dropPoint.ip || !PlacesControllerDragHelper.canDrop(dropPoint.ip, dt) )` → `aEvent.stopPropagation()`
- 条件付き依存: `if (this._overFolder.elt != overElt)` → `this._clearOverFolder()`
- 条件付き依存: `if (this._overFolder.elt != overElt)` → `this._setTimer()`
- 条件付き依存: `if (dropPoint.folderElt || aEvent.originalTarget == this._chevron)` → `this._overFolder.elt.hasAttribute()`
- 条件付き依存: `if (!this._overFolder.elt.hasAttribute("dragover"))` → `this._overFolder.elt.setAttribute()`
- 条件付き依存: `if (this.isRTL)` → `Math.ceil()`
- 条件付き依存: `if (this.isRTL)` → `this._rootElt.getBoundingClientRect()`
- 条件付き依存: `if (dropPoint.beforeIndex == -1)` → `this._rootElt.lastElementChild.getBoundingClientRect()`
- 条件付き依存: `if (!(dropPoint.beforeIndex == -1))` → `this._rootElt.children[ dropPoint.beforeIndex ].getBoundingClientRect()`
- 条件付き依存: `if (!(this._rootElt.firstElementChild))` → `this.#findPrecedingToolbarWidget()`
- 条件付き依存: `if (prevWidget)` → `prevWidget.getBoundingClientRect()`
- 条件付き依存: `if (!(this.isRTL))` → `Math.floor()`
- 条件付き依存: `if (!(this.isRTL))` → `this._rootElt.getBoundingClientRect()`
- 条件付き依存: `if (!(dropPoint.folderElt || aEvent.originalTarget == this._chevron))` → `Math.round()`
- 条件付き依存: `if (!(dropPoint.folderElt || aEvent.originalTarget == this._chevron))` → `this._clearOverFolder()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `aEvent.dataTransfer`, `aEvent.originalTarget`, `aEvent.target`, `dropPoint.beforeIndex`, `dropPoint.folderElt`, `dropPoint.ip`, `ind.clientWidth`, `ind.collapsed`, `ind.parentNode.collapsed`, `ind.style.marginInlineStart`, `ind.style.transform`, `prevWidget.getBoundingClientRect().left`, `prevWidget.getBoundingClientRect().right`, `this._chevron`, `this._dropIndicator`, `this._dropIndicator.collapsed`, `this._overFolder.elt`, `this._overFolder.hoverTime`, `this._overFolder.openTimer`, `this._rootElt.children`, `this._rootElt.children[ dropPoint.beforeIndex ].getBoundingClientRect().left`, `this._rootElt.children[ dropPoint.beforeIndex ].getBoundingClientRect().right`, `this._rootElt.firstElementChild`, `this._rootElt.getBoundingClientRect().left`, `this._rootElt.getBoundingClientRect().right`, `this._rootElt.lastElementChild.getBoundingClientRect().left`, `this._rootElt.lastElementChild.getBoundingClientRect().right`, `this.isRTL`

## PlacesToolbar._onDrop()
- 位置: L2039-2053
- 役割: ドロップ先があれば PlacesControllerDragHelper.onDrop で項目を挿入し、後始末をする。
- 触るとき: ツールバーへのドロップの処理を変えるとき、ドロップ後に表示が残る問題を調べるとき。
- 呼び出し先: `aEvent.stopPropagation()`, `this._cleanupDragDetails()`, `this._getDropPoint()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop( dropPoint.ip, aEvent.dataTransfer ).catch()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `aEvent.preventDefault()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `aEvent.dataTransfer`, `aEvent.target`, `console.error`, `dropPoint.ip`

## PlacesToolbar._onDragLeave()
- 位置: L2055-2064
- 役割: ドロップ位置の表示を隠し、フォルダーの上から離れたら閉じるタイマーを張る。
- 触るとき: ドラッグで離れたときのフォルダーメニューの閉じ方を変えるとき。
- 条件付き依存: `if (this._overFolder.elt)` → `this._setTimer()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._dropIndicator.collapsed`, `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.hoverTime`

## PlacesToolbar._onDragEnd()
- 位置: L2066-2068
- 役割: ドラッグ終了時の後始末 (_cleanupDragDetails) を行う。
- 触るとき: ドラッグ終了時に残る状態を増やすとき。
- 呼び出し先: `this._cleanupDragDetails()`

## PlacesToolbar._onPopupShowing()
- 位置: L2070-2083
- 役割: _allowPopupShowing が false なら、フラグを戻したうえでポップアップを開かせない。ボタンのポップアップなら開いたボタンを記録し、基底の処理を呼ぶ。
- 触るとき: ツールバーのメニューを開く条件 (修飾キーによる抑止) や、開いたボタンの追跡を変えるとき。
- 呼び出し先: `super._onPopupShowing()`
- 条件付き依存: `if (!this._allowPopupShowing)` → `aEvent.preventDefault()`
- 参照: `aEvent.target.parentNode`, `parent.localName`, `this._allowPopupShowing`, `this._openedMenuButton`

## PlacesToolbar._onPopupHidden()
- 位置: L2085-2109
- 役割: フォルダー以外のノードは containerOpen を閉じ、ボタンのポップアップなら開いていたボタンの記録と dragover 属性を外す。
- 触るとき: ツールバーのメニューを閉じたときの状態の後始末を変えるとき。
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (parent.localName == "toolbarbutton")` → `parent.hasAttribute()`
- 条件付き依存: `if (parent.hasAttribute("dragover"))` → `parent.removeAttribute()`
- 参照: `aEvent.target`, `parent.localName`, `placesNode.containerOpen`, `popup._placesNode`, `popup.parentNode`, `this._openedMenuButton`

## PlacesToolbar._onMouseMove()
- 位置: L2111-2131
- 役割: メニューを開いたままボタン上を移動したとき、ドラッグ中でなければ、ホバーしたメニュー型ボタンに開く対象を切り替える。
- 触るとき: メニューバーのように隣のフォルダーへホバーで切り替える挙動を変えるとき。
- 呼び出し先: `PlacesControllerDragHelper.getSession()`
- 参照: `aEvent.originalTarget`, `target.localName`, `target.open`, `target.type`, `this._cachedMouseMoveEvent`, `this._openedMenuButton`, `this._openedMenuButton.open`

## PlacesMenu.constructor()
- 位置: L2147-2172
- 役割: ポップアップとその親の menu を対象に基底を作り、表示・非表示・unload・マウスダウンのイベントを登録する。macOS でメニューバー配下なら native view にする。最後に最初の popupshowing を処理する。
- 触るとき: メニュー版のビューが作られる時の登録や、macOS のネイティブメニューの判定を変えるとき。
- 呼び出し先: `super()`, `this._addEventListeners()`, `this._onPopupShowing()`
- 参照: `AppConstants.platform`, `elt.localName`, `elt.parentNode`, `popupShowingEvent.target`, `popupShowingEvent.target.parentNode`, `this._nativeView`, `this._rootElt`, `this._viewElt.parentNode`

## PlacesMenu._init()
- 位置: L2174-2176
- 役割: 表示要素に _placesView として自分を設定する。
- 触るとき: 表示要素からビューを引けるようにする仕組みを変えるとき。
- 参照: `this._viewElt._placesView`

## PlacesMenu._removeChild()
- 位置: L2178-2180
- 役割: 基底の _removeChild をそのまま呼ぶ。
- 触るとき: メニュー固有の子要素削除を入れるとき。
- 呼び出し先: `super._removeChild()`

## PlacesMenu.uninit()
- 位置: L2182-2192
- 役割: 登録したイベントを外してから基底の uninit を呼ぶ。
- 触るとき: メニューを破棄するときの後始末を変えるとき。
- 呼び出し先: `super.uninit()`, `this._removeEventListeners()`
- 参照: `this._rootElt`

## PlacesMenu.handleEvent()
- 位置: L2194-2209
- 役割: unload、popupshowing、popuphidden、mousedown を対応するハンドラーに振り分ける。
- 触るとき: メニューが扱うイベントを増やすとき。
- 呼び出し先: `this._onMouseDown()`, `this._onPopupHidden()`, `this._onPopupShowing()`, `this.uninit()`
- 参照: `aEvent.type`

## PlacesMenu._onPopupHidden()
- 位置: L2211-2230
- 役割: このビューのフォルダー以外は containerOpen を閉じ、自動展開の属性と dragstart 属性を外す。
- 触るとき: メニューを閉じたときの状態の後始末を変えるとき。
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `popup.removeAttribute()`
- 参照: `aEvent.originalTarget`, `placesNode.containerOpen`, `popup._placesNode`

## PlacesMenu._onMouseDown()
- 位置: L2234-2236
- 役割: マウス押下時に投機的接続を行う。
- 触るとき: メニューのマウス押下時の先行接続の挙動を変えるとき。
- 呼び出し先: `PlacesUIUtils.maybeSpeculativeConnectOnMouseDown()`

## PlacesPanelview.constructor()
- 位置: L2242-2250
- 役割: 基底を作り、表示要素に _placesView を設定し、ポップアップの表示を模擬して初期化する。unload を登録し、コンテキストメニューに placesContext を設定する。
- 触るとき: パネルビュー (ブックマークパネルなど) の初期化の順序や、右クリックメニューの対応を変えるとき。
- 呼び出し先: `super()`, `this._addEventListeners()`, `this._onPopupShowing()`, `this._rootElt.setAttribute()`
- 参照: `this._rootElt`, `this._viewElt._placesView`

## PlacesPanelview.events()
- 位置: L2252-2265
- 役割: パネルビューの PanelMultiView に登録するイベントの名前一覧 (click、command、dragend、dragstart、ViewHiding、ViewShown、mousedown) を、初回だけ作って返す。
- 触るとき: パネルビューが監視するイベントを増減させるとき。
- 参照: `this._events`

## PlacesPanelview.handleEvent()
- 位置: L2267-2297
- 役割: click (中クリックは command と同じ扱い)、command、ドラッグ、unload、ViewHiding、ViewShown、mousedown を対応するハンドラーに振り分ける。
- 触るとき: パネルビューでのクリックや表示切替のイベント処理を変えるとき。
- 呼び出し先: `this._onCommand()`, `this._onDragEnd()`, `this._onDragStart()`, `this._onMouseDown()`, `this._onPopupHidden()`, `this._onViewShown()`, `this.uninit()`
- 参照: `event.button`, `event.type`

## PlacesPanelview._onCommand()
- 位置: L2299-2326
- 役割: ボタンに紐づくノードを、イベントの修飾キーに従って開く。親が panelMenu_bookmarksMenu でなければ、またはマウス中クリックで openInTabClosesMenu が真のときはパネルを閉じる。
- 触るとき: パネル内のブックマークをクリックしたときの開き方やパネルを閉じるかどうかを変えるとき。
- 呼び出し先: `BrowserUtils.getRootEvent()`, `PlacesUIUtils.openNodeWithEvent()`
- 条件付き依存: `if (button.parentNode.id == "panelMenu_bookmarksMenu")` → `button.setAttribute()`
- 条件付き依存: `if (!(!PlacesUIUtils.openInTabClosesMenu && modifKey))` → `button.removeAttribute()`
- 条件付き依存: `if ( button.parentNode.id != "panelMenu_bookmarksMenu" || (event.type == "click" && event.button == 1 && PlacesUIUtils.openInTabClosesMenu) )` → `this.panelMultiView.closest("panel").hidePopup()`
- 条件付き依存: `if ( button.parentNode.id != "panelMenu_bookmarksMenu" || (event.type == "click" && event.button == 1 && PlacesUIUtils.openInTabClosesMenu) )` → `this.panelMultiView.closest()`
- 参照: `AppConstants.platform`, `PlacesUIUtils.openInTabClosesMenu`, `button._placesNode`, `button.parentNode.id`, `event.button`, `event.ctrlKey`, `event.metaKey`, `event.originalTarget`, `event.type`

## PlacesPanelview.destroyContextMenu()
- 位置: L2328-2331
- 役割: 基底の後始末に加え、直前のコンテキストメニューのコマンドに応じてパネルを閉じるかを判断する (maybeClosePanel)。
- 触るとき: コンテキストメニューの操作の後にパネルが閉じるかどうかを変えるとき。
- 呼び出し先: `super.destroyContextMenu()`, `this.maybeClosePanel()`
- 参照: `PlacesUIUtils.lastContextMenuCommand`

## PlacesPanelview.maybeClosePanel()
- 位置: L2341-2359
- 役割: タブで開く系のコマンドなら、ブックマークパネル以外か openInTabClosesMenu が真のときにパネルを閉じる。ブックマーク作成と履歴項目の削除では閉じる。
- 触るとき: 操作の後にパネルを閉じるかどうかの条件を変えるとき、コマンドを追加するとき。
- 呼び出し先: `this.panelMultiView.closest()`, `this.panelMultiView.closest("panel").hidePopup()`
- 条件付き依存: `if ( this._viewElt.id != "PanelUI-bookmarks" || PlacesUIUtils.openInTabClosesMenu )` → `this.panelMultiView.closest("panel").hidePopup()`
- 条件付き依存: `if ( this._viewElt.id != "PanelUI-bookmarks" || PlacesUIUtils.openInTabClosesMenu )` → `this.panelMultiView.closest()`
- 参照: `PlacesUIUtils.openInTabClosesMenu`, `this._viewElt.id`

## PlacesPanelview._onDragEnd()
- 位置: L2361-2363
- 役割: ドラッグ対象を消す。
- 触るとき: パネルのドラッグ終了時の後始末を変えるとき。
- 参照: `this._draggedElt`

## PlacesPanelview._onDragStart()
- 位置: L2365-2377
- 役割: パネル直下の項目のドラッグを開始し、対象を記録してフォーカスを移し、データを設定する。
- 触るとき: パネル内の項目のドラッグ開始条件を変えるとき。
- 呼び出し先: `event.stopPropagation()`, `this._controller.setDataTransfer()`, `this._rootElt.focus()`
- 参照: `draggedElt._placesNode`, `draggedElt.parentNode`, `event.originalTarget`, `this._draggedElt`, `this._rootElt`

## PlacesPanelview.uninit()
- 位置: L2379-2384
- 役割: PanelMultiView のイベントと unload の登録を外し、参照を消してから基底の uninit を呼ぶ。
- 触るとき: パネルビューの破棄時の後始末を変えるとき。
- 呼び出し先: `super.uninit()`, `this._removeEventListeners()`
- 参照: `this.events`, `this.panelMultiView`

## PlacesPanelview._createDOMNodeForPlacesNode()
- 位置: L2386-2422
- 役割: 区切り線、または URL 用のサブビュー用ボタン (toolbarbutton) を作る。URL 以外の種類は例外になる。
- 触るとき: パネル内の項目の見た目や種類の扱いを変えるとき。
- 呼び出し先: `this._domNodes.delete()`, `this._domNodes.has()`
- 条件付き依存: `if (type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR)` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `document.createXULElement()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `element.classList.add()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `element.setAttribute()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUIUtils.guessUrlSchemeForUI()`
- 条件付き依存: `if (!(type == Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR))` → `PlacesUIUtils.getBestTitle()`
- 条件付き依存: `if (icon)` → `element.setAttribute()`
- 条件付き依存: `if (!this._domNodes.has(placesNode))` → `this._domNodes.set()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_SEPARATOR`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `element._placesNode`, `placesNode.icon`, `placesNode.type`, `placesNode.uri`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)

## PlacesPanelview._setEmptyPopupStatus()
- 位置: L2424-2453
- 役割: パネル版の空表示として無効のボタンを入れる。マーカーが無い外部利用のパネルでも動くように、マーカーの有無を確かめてから挿入する。
- 触るとき: パネルの空フォルダーの表示を変えるとき、マーカーの無い独自パネルで空表示が出ない問題を調べるとき。
- 条件付き依存: `if (!panelview._emptyMenuitem)` → `document.createXULElement()`
- 条件付き依存: `if (!panelview._emptyMenuitem)` → `panelview._emptyMenuitem.setAttribute()`
- 条件付き依存: `if (!panelview._emptyMenuitem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (empty)` → `panelview.setAttribute()`
- 条件付き依存: `if ( !panelview._startMarker || (!panelview._startMarker.previousElementSibling && !panelview._endMarker.nextElementSibling) )` → `panelview.insertBefore()`
- 条件付き依存: `if (!(empty))` → `panelview.removeAttribute()`
- 条件付き依存: `if (!(empty))` → `panelview.removeChild()`
- 参照: `panelview._emptyMenuitem`, `panelview._emptyMenuitem.className`, `panelview._endMarker`, `panelview._endMarker.nextElementSibling`, `panelview._startMarker`, `panelview._startMarker.previousElementSibling`

## PlacesPanelview._isPopupOpen()
- 位置: L2455-2457
- 役割: PanelView.forNode で表示要素の panel が active かを返す。
- 触るとき: パネルが開いているかの判定を変えるとき。
- 呼び出し先: `PanelView.forNode()`
- 参照: `PanelView.forNode(this._viewElt).active`, `this._viewElt`

## PlacesPanelview._onPopupHidden()
- 位置: L2459-2472
- 役割: ViewHiding のときに、フォルダー以外のノードの containerOpen を閉じる。
- 触るとき: パネルを閉じたときの結果の後始末を変えるとき。
- 呼び出し先: `PlacesUIUtils.getViewForNode()`, `PlacesUtils.nodeIsFolderOrShortcut()`
- 参照: `event.originalTarget`, `panelview._placesNode`, `placesNode.containerOpen`

## PlacesPanelview._onPopupShowing()
- 位置: L2474-2483
- 役割: ルート要素からの初回の表示では、PanelMultiView のイベントの監視を始める。その後に基底の処理を呼ぶ。
- 触るとき: パネルの初回表示時の監視の開始条件を変えるとき。
- 呼び出し先: `super._onPopupShowing()`
- 条件付き依存: `if (event.originalTarget == this._rootElt)` → `this._addEventListeners()`
- 参照: `event.originalTarget`, `this._rootElt`, `this._viewElt.panelMultiView`, `this.events`, `this.panelMultiView`

## PlacesPanelview._onViewShown()
- 位置: L2485-2496
- 役割: 自分のビューが表示されたとき、コントローラーが外れていれば付け直す。PanelMultiView が要素を付け替えたときの対策。
- 触るとき: パネルの表示時にコントローラーが無くなる問題を調べるとき。
- 呼び出し先: `this.controllers.getControllerCount()`
- 条件付き依存: `if (!this.controllers.getControllerCount() && this._controller)` → `this.controllers.appendController()`
- 参照: `event.originalTarget`, `this._controller`, `this._viewElt`

## PlacesPanelview._onMouseDown()
- 位置: L2498-2500
- 役割: マウス押下時に投機的接続を行う。
- 触るとき: パネルのマウス押下時の先行接続の挙動を変えるとき。
- 呼び出し先: `PlacesUIUtils.maybeSpeculativeConnectOnMouseDown()`
