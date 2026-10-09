# browser/components/places/content/places-menupopup.js

source: browser/components/places/content/places-menupopup.js
source-hash: a0affb9ecff8d39290d24b8474b1fbc7605d931c
lines: 697

## <module>
- 役割: places-popup と places-popup-arrow のカスタム要素を定義し、ブックマーク/履歴メニューのドラッグ&ドロップと先に開くフォルダー制御を担う。
- 呼び出し先: `customElements.define()`

## closingPopupEndsDrag()
- 位置: L11-24
- 役割: Wayland でドラッグ元のポップアップが閉じるとドラッグが取り消されるかを判定する。
- 触るとき: Wayland でメニューを閉じた途端にドラッグが中断される問題を調べるとき。
- 呼び出し先: `popup.querySelectorAll()`
- 参照: `childPopup.isWaylandDragSource`, `popup.isWaylandDragSource`, `popup.isWaylandPopup`

## MozPlacesPopup.constructor()
- 位置: L33-48
- 役割: dragstart、drop、dragover などの DnD 関連イベントを自身のハンドラへ登録する。
- 触るとき: メニューに新しい DnD イベントを扱わせるとき、または登録漏れで反応しないとき。
- 呼び出し先: `super()`, `this.addEventListener()`

## MozPlacesPopup.markup()
- 位置: L50-64
- 役割: ドロップ位置の表示バーと矢印付きスクロールボックスを含む shadow DOM の雛形を返す。
- 触るとき: メニューの内部構造やドロップインジケーターの見た目を変えるとき。

## MozPlacesPopup.connectedCallback()
- 位置: L66-229
- 役割: フォルダーのホバー展開に使う _overFolder 状態オブジェクトを初期化する。
- 触るとき: ドラッグ中のサブメニュー展開・閉じ遅延の状態を理解したり、初期値を変えたりするとき。
- 呼び出し先: `this.delayConnectedCallback()`
- 参照: `this._overFolder`

## MozPlacesPopup.elt()
- 位置: L86-88
- 役割: ホバー中のフォルダー要素 (_folder.elt) を返す。
- 触るとき: どのフォルダーがドラッグ先として保持されているかを確認するとき。
- 参照: `this._folder.elt`

## MozPlacesPopup.elt()
- 位置: L89-91
- 役割: ホバー中のフォルダー要素 (_folder.elt) を設定する。
- 触るとき: ドラッグ先フォルダーの切り替え時に要素が正しく差し替わらないとき。
- 参照: `this._folder.elt`

## MozPlacesPopup.openTimer()
- 位置: L93-95
- 役割: フォルダーを開くタイマーを返す。
- 触るとき: ホバー展開のタイマーが残ったまま開かないときに状態を確認するとき。
- 参照: `this._folder.openTimer`

## MozPlacesPopup.openTimer()
- 位置: L96-98
- 役割: フォルダーを開くタイマーを設定する。
- 触るとき: 展開タイマーの作成・破棄の順序を変えるとき。
- 参照: `this._folder.openTimer`

## MozPlacesPopup.hoverTime()
- 位置: L100-102
- 役割: ホバーで展開や閉じるまでの待ち時間を返す。既定値は 350 ミリ秒。
- 触るとき: ドラッグ中の展開の速さを変えたいとき、または値を外から読みたいとき。
- 参照: `this._folder.hoverTime`

## MozPlacesPopup.hoverTime()
- 位置: L103-105
- 役割: ホバーで展開や閉じるまでの待ち時間を設定する。
- 触るとき: 展開待ち時間を変えるとき、または外部から設定して挙動が変わるとき。
- 参照: `this._folder.hoverTime`

## MozPlacesPopup.closeTimer()
- 位置: L107-109
- 役割: 閉じるタイマーを返す。
- 触るとき: ドラッグを離れたフォルダーが閉じない原因を調べるとき。
- 参照: `this._folder.closeTimer`

## MozPlacesPopup.closeTimer()
- 位置: L110-112
- 役割: 閉じるタイマーを設定する。
- 触るとき: dragleave 後に閉じ処理を遅らせる仕組みを変えるとき。
- 参照: `this._folder.closeTimer`

## MozPlacesPopup.closeMenuTimer()
- 位置: L114-116
- 役割: 親メニューを閉じるタイマーを返す。
- 触るとき: サブメニューからドラッグを離したあとに親が閉じるかを調べるとき。
- 参照: `this._closeMenuTimer`

## MozPlacesPopup.closeMenuTimer()
- 位置: L117-119
- 役割: 親メニューを閉じるタイマーを設定する。
- 触るとき: Wayland でドラッグ終了まで閉じるのを待つ処理を変えるとき。
- 参照: `this._closeMenuTimer`

## OF__setTimer()
- 位置: L121-125
- 役割: 指定ミリ秒後に notify を呼ぶ一回限りの nsITimer を作る。
- 触るとき: ホバー展開や閉じ処理の遅延時間を変えるとき、またはタイマーの生成方法を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `timer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## OF__notify()
- 位置: L127-180
- 役割: 展開・閉じ・メニュー閉じの各タイマーが発火したときに、対応する処理を実行する。
- 触るとき: ドラッグ中にフォルダーが開かない、または閉じすぎるときに真っ先に読む関数。
- 条件付き依存: `if (aTimer == this._folder.openTimer)` → `this._folder.elt.lastElementChild.setAttribute()`
- 条件付き依存: `if (aTimer == this._folder.openTimer)` → `this._folder.elt.lastElementChild.openPopup()`
- 条件付き依存: `if (aTimer == this._folder.closeTimer)` → `PlacesControllerDragHelper.draggingOverChildNode()`
- 条件付き依存: `if (aTimer == this._folder.closeTimer)` → `this.clear()`
- 条件付き依存: `if (aTimer == this._folder.closeTimer)` → `closingPopupEndsDrag()`
- 条件付き依存: `if (!draggingOverChild && !closingPopupEndsDrag(this._self))` → `this.closeParentMenus()`
- 条件付き依存: `if (aTimer == this.closeMenuTimer)` → `PlacesControllerDragHelper.getSession()`
- 条件付き依存: `if (aTimer == this.closeMenuTimer)` → `PlacesControllerDragHelper.draggingOverChildNode()`
- 条件付き依存: `if (hidePopup)` → `closingPopupEndsDrag()`
- 条件付き依存: `if (!closingPopupEndsDrag(popup))` → `popup.hidePopup()`
- 条件付き依存: `if (!closingPopupEndsDrag(popup))` → `this.closeParentMenus()`
- 条件付き依存: `if (popup.isWaylandDragSource)` → `this.setTimer()`
- 参照: `popup.isWaylandDragSource`, `popup.parentNode`, `this._closeMenuTimer`, `this._folder.closeTimer`, `this._folder.elt`, `this._folder.openTimer`, `this._self`, `this.closeMenuTimer`, `this.hoverTime`

## OF__closeParentMenus()
- 位置: L185-201
- 役割: ドラッグ中の子を含まない親の places メニューを順に閉じる。
- 触るとき: サブメニューを閉じた後に親メニューが残るときや、親を閉じない条件を変えるとき。
- 条件付き依存: `if (parent.localName == "menupopup" && parent._placesNode)` → `PlacesControllerDragHelper.draggingOverChildNode()`
- 条件付き依存: `if (parent.localName == "menupopup" && parent._placesNode)` → `parent.hidePopup()`
- 参照: `parent._placesNode`, `parent.localName`, `parent.parentNode`, `popup.parentNode`, `this._self`

## OF__clear()
- 位置: L206-227
- 役割: 展開中のフォルダーを閉じ、関連するスタイルとタイマーを解除する。
- 触るとき: ドラッグを別の場所へ移したあとにメニューやタイマーが残るときに調べる。
- 条件付き依存: `if (this._folder.elt && this._folder.elt.lastElementChild)` → `popup.hasAttribute()`
- 条件付き依存: `if (this._folder.elt && this._folder.elt.lastElementChild)` → `closingPopupEndsDrag()`
- 条件付き依存: `if ( !popup.hasAttribute("dragover") && !closingPopupEndsDrag(popup) )` → `popup.hidePopup()`
- 条件付き依存: `if (this._folder.elt && this._folder.elt.lastElementChild)` → `this._folder.elt.removeAttribute()`
- 条件付き依存: `if (this._folder.openTimer)` → `this._folder.openTimer.cancel()`
- 条件付き依存: `if (this._folder.closeTimer)` → `this._folder.closeTimer.cancel()`
- 参照: `this._folder.closeTimer`, `this._folder.elt`, `this._folder.elt.lastElementChild`, `this._folder.openTimer`

## MozPlacesPopup._indicatorBar()
- 位置: L231-238
- 役割: shadow DOM 内のドロップインジケーター要素を取得してキャッシュする。
- 触るとき: ドロップ位置の線が表示されないとき、または表示要素の参照を変えるとき。
- 条件付き依存: `if (!this.__indicatorBar)` → `this.shadowRoot.querySelector()`
- 参照: `this.__indicatorBar`

## MozPlacesPopup._rootView()
- 位置: L246-251
- 役割: このポップアップを管理するビュー (PlacesUIUtils.getViewForNode の結果) を取得してキャッシュする。
- 触るとき: ポップアップから controller やドラッグ元の情報へ辿るとき。
- 条件付き依存: `if (!this.__rootView)` → `PlacesUIUtils.getViewForNode()`
- 参照: `this.__rootView`

## MozPlacesPopup._hideDropIndicator()
- 位置: L260-273
- 役割: ドラッグ先が places ノードの範囲内にない場合に true を返し、インジケーターを隠すべきか判定する。
- 触るとき: メニューの外側や区切り以外でドロップ線が出てしまうとき。
- 呼び出し先: `this._endMarker.compareDocumentPosition()`, `this._startMarker.compareDocumentPosition()`
- 参照: `Node.DOCUMENT_POSITION_FOLLOWING`, `Node.DOCUMENT_POSITION_PRECEDING`, `aEvent.target`, `target._placesNode`

## MozPlacesPopup._getDropPoint()
- 位置: L284-374
- 役割: マウス位置に応じて、挿入位置とドロップ先フォルダーを決める。
- 触るとき: ドロップ位置が上下どちらにずれるか、フォルダー内に入るかを調べるとき。
- 呼び出し先: `PlacesUIUtils.isFolderReadOnly()`, `PlacesUtils.getConcreteItemGuid()`, `PlacesUtils.nodeIsFolderOrShortcut()`, `PlacesUtils.nodeIsTagQuery()`, `elt.getBoundingClientRect()`, `this._rootView.controller.disallowInsertion()`
- 条件付き依存: `if (!elt._placesNode)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (!elt._placesNode)` → `elt.getAttribute()`
- 条件付き依存: `if (!elt._placesNode)` → `elt.lastElementChild.hasAttribute()`
- 条件付き依存: `if (eventY - eltY < eltHeight * 0.2)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (eventY - eltY < eltHeight * 0.8)` → `PlacesUtils.getConcreteItemGuid()`
- 条件付き依存: `if (eventY - eltY <= eltHeight / 2)` → `PlacesUtils.getConcreteItemGuid()`
- 参照: `Ci.nsITreeView.DROP_AFTER`, `Ci.nsITreeView.DROP_BEFORE`, `aEvent.clientY`, `aEvent.target`, `dropPoint.folderElt`, `dropPoint.ip`, `elt._placesNode`, `elt._placesNode.title`, `elt.lastElementChild`, `elt.localName`, `elt.parentNode`, `this._placesNode`
- XPCOM: `nsITreeView`

## MozPlacesPopup._cleanupDragDetails()
- 位置: L376-383
- 役割: ドロップまたはドラッグ終了時に、ドラッグ用の属性と状態をリセットする。
- 触るとき: ドラッグ後に dragover などの属性が残るとき。
- 呼び出し先: `this.removeAttribute()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `this._indicatorBar.hidden`, `this._rootView._draggedElt`

## MozPlacesPopup.on_DOMMenuItemActive()
- 位置: L385-409
- 役割: 項目にフォーカスが移ったとき、そのリンク先をステータス表示用に XULBrowserWindow へ渡す。
- 触るとき: メニューの項目にカーソルを載せたとき、下部ステータスに URL が出ない不具合を調べるとき。
- 条件付き依存: `if (super.on_DOMMenuItemActive)` → `super.on_DOMMenuItemActive()`
- 条件付き依存: `if (window.XULBrowserWindow)` → `PlacesUtils.nodeIsURI()`
- 条件付き依存: `if (!(placesNode && PlacesUtils.nodeIsURI(placesNode)))` → `elt.hasAttribute()`
- 条件付き依存: `if (elt.hasAttribute("targetURI"))` → `elt.getAttribute()`
- 条件付き依存: `if (linkURI)` → `window.XULBrowserWindow.setOverLink()`
- 参照: `elt._placesNode`, `elt.parentNode`, `event.target`, `placesNode.uri`, `super.on_DOMMenuItemActive`, `window.XULBrowserWindow`

## MozPlacesPopup.on_DOMMenuItemInactive()
- 位置: L411-420
- 役割: 項目から離れたとき、ステータス表示の URL を空にする。
- 触るとき: ステータスバーに古い URL が残るとき。
- 条件付き依存: `if (window.XULBrowserWindow)` → `window.XULBrowserWindow.setOverLink()`
- 参照: `elt.parentNode`, `event.target`, `window.XULBrowserWindow`

## MozPlacesPopup.on_dragstart()
- 位置: L422-441
- 役割: ドラッグ開始時に移動不可なら copyLink にし、ドラッグ元と転送データを設定する。
- 触るとき: メニュー項目のドラッグで移動・コピーの種別がおかしいとき、またはドラッグデータを増やすとき。
- 呼び出し先: `event.stopPropagation()`, `this._rootView.controller.canMoveNode()`, `this._rootView.controller.setDataTransfer()`, `this.setAttribute()`
- 参照: `elt._placesNode`, `event.dataTransfer.effectAllowed`, `event.target`, `this._rootView._draggedElt`

## MozPlacesPopup.on_drop()
- 位置: L443-457
- 役割: ドロップ位置を求め、有効なら PlacesControllerDragHelper でデータを挿入してから後始末をする。
- 触るとき: メニューにドロップしても項目が追加されない、または二重に追加されるとき。
- 呼び出し先: `event.stopPropagation()`, `this._cleanupDragDetails()`, `this._getDropPoint()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop( dropPoint.ip, event.dataTransfer ).catch()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `PlacesControllerDragHelper.onDrop()`
- 条件付き依存: `if (dropPoint && dropPoint.ip)` → `event.preventDefault()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `console.error`, `dropPoint.ip`, `event.dataTransfer`, `event.target`

## MozPlacesPopup.on_dragover()
- 位置: L459-551
- 役割: ドラッグ中の挿入位置を判定し、フォルダー展開の予約と挿入線の位置を更新する。
- 触るとき: ドロップ線の位置がずれるとき、またはドラッグ中のフォルダー展開の条件を変えるとき。
- 呼び出し先: `PlacesControllerDragHelper.canDrop()`, `event.preventDefault()`, `event.stopPropagation()`, `this._getDropPoint()`, `this._hideDropIndicator()`, `this._indicatorBar.parentNode.getBoundingClientRect()`, `this.scrollBox.getBoundingClientRect()`, `this.setAttribute()`
- 条件付き依存: `if ( !dropPoint || !dropPoint.ip || !PlacesControllerDragHelper.canDrop(dropPoint.ip, dt) )` → `event.stopPropagation()`
- 条件付き依存: `if ( this._overFolder.elt && this._overFolder.elt != dropPoint.folderElt )` → `this._overFolder.clear()`
- 条件付き依存: `if (!this._overFolder.elt)` → `this._overFolder.setTimer()`
- 条件付き依存: `if (dropPoint.folderElt)` → `dropPoint.folderElt.setAttribute()`
- 条件付き依存: `if (!(dropPoint.folderElt))` → `this._overFolder.clear()`
- 条件付き依存: `if (scrollDir != 0)` → `this.scrollBox.scrollByIndex()`
- 条件付き依存: `if (dropPoint.folderElt || this._hideDropIndicator(event))` → `event.preventDefault()`
- 条件付き依存: `if (dropPoint.folderElt || this._hideDropIndicator(event))` → `event.stopPropagation()`
- 条件付き依存: `if (scrollDir == 0)` → `elt.getBoundingClientRect()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `dropPoint.folderElt`, `dropPoint.ip`, `elt.getBoundingClientRect().height`, `elt.nextElementSibling`, `elt.screenY`, `event.dataTransfer`, `event.originalTarget`, `event.screenY`, `event.target`, `scrollRect.height`, `scrollRect.y`, `this._indicatorBar.firstElementChild.style.marginTop`, `this._indicatorBar.hidden`, `this._indicatorBar.parentNode.getBoundingClientRect().y`, `this._overFolder.elt`, `this._overFolder.hoverTime`, `this._overFolder.openTimer`, `this.firstElementChild`, `this.scrollBox._scrollButtonDown`, `this.scrollBox._scrollButtonUp`, `this.scrollBox.screenY`

## MozPlacesPopup.on_dragleave()
- 位置: L553-583
- 役割: ドラッグがメニューの外へ出たときに線を消し、閉じ用のタイマーを予約する。
- 触るとき: ドラッグを離したあとにサブメニューが開いたまま残るときに調べる。
- 呼び出し先: `event.stopPropagation()`, `this.contains()`, `this.hasAttribute()`, `this.removeAttribute()`
- 条件付き依存: `if (this._overFolder.elt)` → `this._overFolder.setTimer()`
- 条件付き依存: `if (this.hasAttribute("autoopened") || this.hasAttribute("dragstart"))` → `this._overFolder.setTimer()`
- 参照: `PlacesControllerDragHelper.currentDropTarget`, `event.relatedTarget`, `this._indicatorBar.hidden`, `this._overFolder.closeMenuTimer`, `this._overFolder.closeTimer`, `this._overFolder.elt`, `this._overFolder.hoverTime`

## MozPlacesPopup.on_dragend()
- 位置: L585-587
- 役割: ドラッグ終了時に後始末 (_cleanupDragDetails) を行う。
- 触るとき: ドラッグ終了後に状態が残るときに確認する。
- 呼び出し先: `this._cleanupDragDetails()`

## MozPlacesPopup.uninit()
- 位置: L589-591
- 役割: キャッシュしたビュー参照を破棄する。
- 触るとき: ポップアップを破棄したあとに古いビューを参照してしまうとき。
- 参照: `this.__rootView`

## MozPlacesPopupArrow.constructor()
- 位置: L602-615
- 役割: popupshowing などポップアップの表示イベントを自身のハンドラへ登録する。
- 触るとき: 矢印付きポップアップの表示アニメーションや位置情報を追加するとき。
- 呼び出し先: `super()`, `this.addEventListener()`

## MozPlacesPopupArrow.connectedCallback()
- 位置: L617-628
- 役割: 親の初期化後に属性継承を行い、flip・side・position の既定値を設定する。
- 触るとき: 矢印付きポップアップの既定の向きや位置を変えるとき。
- 呼び出し先: `super.connectedCallback()`, `this.delayConnectedCallback()`, `this.initializeAttributeInheritance()`, `this.setAttribute()`

## MozPlacesPopupArrow._setSideAttribute()
- 位置: L630-655
- 役割: 表示位置の alignment から矢印の side 属性 (left/right/top/bottom) を決める。
- 触るとき: 矢印がアンカーの反対側に出るなど、向きが合わないとき。
- 呼び出し先: `position.indexOf()`
- 条件付き依存: `if (position.indexOf("start_") == 0 || position.indexOf("end_") == 0)` → `this.matches()`
- 条件付き依存: `if (position.indexOf("start_") == 0 || position.indexOf("end_") == 0)` → `position.indexOf()`
- 条件付き依存: `if (position.indexOf("start_") == 0)` → `this.setAttribute()`
- 条件付き依存: `if (!(position.indexOf("start_") == 0))` → `this.setAttribute()`
- 条件付き依存: `if (!(position.indexOf("start_") == 0 || position.indexOf("end_") == 0))` → `position.indexOf()`
- 条件付き依存: `if ( position.indexOf("before_") == 0 || position.indexOf("after_") == 0 )` → `position.indexOf()`
- 条件付き依存: `if (position.indexOf("before_") == 0)` → `this.setAttribute()`
- 条件付き依存: `if (!(position.indexOf("before_") == 0))` → `this.setAttribute()`
- 参照: `event.alignmentPosition`, `this.anchorNode`

## MozPlacesPopupArrow.on_popupshowing()
- 位置: L657-662
- 役割: 自身の表示開始時に animate を open にし、ポインターイベントを無効にする。
- 触るとき: メニュー表示アニメーションが始まらないとき、または表示中のクリックを防ぐ条件を変えるとき。
- 条件付き依存: `if (event.target == this)` → `this.setAttribute()`
- 参照: `event.target`, `this.style.pointerEvents`

## MozPlacesPopupArrow.on_popuppositioned()
- 位置: L664-668
- 役割: 位置が決まったときに _setSideAttribute を呼んで矢印の向きを更新する。
- 触るとき: 表示位置が変わったとき矢印の向きが追随しない不具合を調べるとき。
- 条件付き依存: `if (event.target == this)` → `this._setSideAttribute()`
- 参照: `event.target`

## MozPlacesPopupArrow.on_popupshown()
- 位置: L670-677
- 役割: 表示完了時に panelopen を付け、ポインターイベントの無効化を解除する。
- 触るとき: 表示後にクリックできないなど、表示完了後の状態に問題があるとき。
- 呼び出し先: `this.setAttribute()`, `this.style.removeProperty()`
- 参照: `event.target`

## MozPlacesPopupArrow.on_popuphiding()
- 位置: L679-683
- 役割: 非表示になり始めたとき animate を cancel にする。
- 触るとき: 閉じるアニメーションが途中で止まるとき。
- 条件付き依存: `if (event.target == this)` → `this.setAttribute()`
- 参照: `event.target`

## MozPlacesPopupArrow.on_popuphidden()
- 位置: L685-690
- 役割: 非表示が完了したとき panelopen と animate の属性を外す。
- 触るとき: 閉じたあとも矢印の状態が残るとき。
- 条件付き依存: `if (event.target == this)` → `this.removeAttribute()`
- 参照: `event.target`
