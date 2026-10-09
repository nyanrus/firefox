# browser/components/tabbrowser/content/drag-and-drop.js

source: browser/components/tabbrowser/content/drag-and-drop.js
source-hash: 51542b55a2f4dcb6f0ab2c29b6c77c017284d48d
lines: 2970

## <module>
- 役割: タブストリップのドラッグ&ドロップ処理を担う window.TabDragAndDrop クラスを、グローバルを漏らさないブロック内で定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## elementToMove()
- 位置: L45-53
- 役割: タブや分割ビューはそのまま、グループラベルはその外側のコンテナ要素を、位置・寸法計算用に返す。
- 触るとき: ドラッグ中の要素の位置や大きさの基準要素を調べるとき。
- 呼び出し先: `isSplitViewWrapper()`, `isTab()`, `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(element))` → `element.closest()`
- 参照: `element.tagName`

## constructor()
- 位置: L69-71
- 役割: 親の tabbrowser-tabs 要素を保持する。
- 触るとき: このクラスの生成元や保持する参照を確認するとき。
- 参照: `this._tabbrowserTabs`

## init()
- 位置: L73-83
- 役割: ピン留めドロップ表示、ピン留め促進カード、ドロップインジケータの要素を取得する。
- 触るとき: ドラッグ用 UI 要素の取得元を変えるとき。
- 呼び出し先: `document.getElementById()`, `this._tabbrowserTabs.querySelector()`
- 参照: `this._dragToPinPromoCard`, `this._pinnedDropIndicator`, `this._tabDropIndicator`

## handle_dragstart()
- 位置: L87-107
- 役割: ドラッグ開始時に対象のタブ、グループラベル、分割ビューを特定し、startTabDrag を呼ぶ。
- 触るとき: どの要素からドラッグを始められるかを変えるとき。
- 呼び出し先: `isSplitViewWrapper()`, `this._getDragTarget()`, `this._tabbrowserTabs.previewPanel?.deactivate()`, `this.startTabDrag()`
- 参照: `tab.splitview`, `tab.visible`, `this._tabbrowserTabs._isCustomizing`

## handle_dragover()
- 位置: L109-275
- 役割: ドラッグ中に、タブの移動アニメーション、リンクのホバー選択、ドロップインジケータ位置の更新を行う。
- 触るとき: ドラッグ中の見た目やインジケータの位置がおかしいとき。
- 呼び出し先: `Math.round()`, `arrowScrollbox.getBoundingClientRect()`, `event.dataTransfer.mozGetDataAt()`, `event.preventDefault()`, `event.stopPropagation()`, `this.finishAnimateTabMove()`, `this.getDropEffectForTabDrag()`
- 条件付き依存: `if (pixelsToScroll)` → `arrowScrollbox.scrollByPixels()`
- 条件付き依存: `if ( (dropEffect == "move" || dropEffect == "copy") && document == draggedTab.ownerDocument && !draggedTab._dragData.fromTabList )` → `this.#isAnimatingMoveTogetherSelectedTabs()`
- 条件付き依存: `if ( (dropEffect == "move" || dropEffect == "copy") && document == draggedTab.ownerDocument && !draggedTab._dragData.fromTabList )` → `this.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if ( (dropEffect == "move" || dropEffect == "copy") && document == draggedTab.ownerDocument && !draggedTab._dragData.fromTabList )` → `this._updateTabStylesOnDrag()`
- 条件付き依存: `if (dropEffect == "move")` → `this.#setMovingTabMode()`
- 条件付き依存: `if (dropEffect == "move")` → `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`
- 条件付き依存: `if (this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab))` → `this._animateExpandedPinnedTabMove()`
- 条件付き依存: `if (dropEffect == "move")` → `this._animateTabMove()`
- 条件付き依存: `if (dropEffect == "link")` → `this._getDragTarget()`
- 条件付き依存: `if (!this.#dragTime)` → `Date.now()`
- 条件付き依存: `if (target)` → `isTabGroupLabel()`
- 条件付き依存: `if (target)` → `Date.now()`
- 条件付き依存: `if (target)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (target)` → `isTab()`
- 条件付き依存: `if (pixelsToScroll)` → `Math.min()`
- 条件付き依存: `if (!(pixelsToScroll))` → `this._getDropIndex()`
- 条件付き依存: `if (!(pixelsToScroll))` → `isSplitViewWrapper()`
- 条件付き依存: `if (!(pixelsToScroll))` → `isTabGroupLabel()`
- 条件付き依存: `if (newIndex == children.length)` → `children.at(-1).getBoundingClientRect()`
- 条件付き依存: `if (newIndex == children.length)` → `children.at()`
- 条件付き依存: `if (!(newIndex == children.length))` → `children[newIndex].getBoundingClientRect()`
- 参照: `arrowScrollbox._scrollButtonDown`, `arrowScrollbox._scrollButtonUp`, `arrowScrollbox.scrollClientRect`, `arrowScrollbox.scrollIncrement`, `children.length`, `draggedTab._dragData.expandGroupOnDrop`, `draggedTab._dragData.fromTabList`, `draggedTab.group.collapsed`, `draggedTab.group.collapsedByDrag`, `draggedTab.ownerDocument`, `event.originalTarget`, `gBrowser.pinnedTabCount`, `ind.clientHeight`, `ind.clientWidth`, `ind.hidden`, `ind.style.transform`, `itemRect.bottom`, `itemRect.left`, `itemRect.right`, `rect.left`, `rect.right`, `rect.top`, `scrollRect.bottom`, `scrollRect.height`, `scrollRect.left`, `scrollRect.right`, `scrollRect.top`, `scrollRect.width`, `target.group.collapsed`, `this.#dragTime`, `this._rtlMode`, `this._tabDropIndicator`, `this._tabbrowserTabs.arrowScrollbox`, `this._tabbrowserTabs.clientWidth`, `this._tabbrowserTabs.dragAndDropElements`, `this._tabbrowserTabs.overflowing`, `this._tabbrowserTabs.selectedItem`, `this._tabbrowserTabs.verticalMode`
- XPCOM: `Services.prefs`

## handle_drop()
- 位置: L278-750
- 役割: ドロップ時に、タブの複製・移動・ピン留め変更・グループ化・他ウィンドウからの取り込み・URL のリンクを開く処理を振り分ける。
- 触るとき: ドロップ後のタブ位置、グループ化、ウィンドウ間移動、URL ドロップの不具合を調べるとき。
- 呼び出し先: `dt.mozTypesAt()`, `event.stopPropagation()`, `gBrowser.TabMetrics.userTriggeredContext()`, `this._pinnedDropIndicator.hasAttribute()`, `this._resetTabsAfterDrop()`
- 条件付き依存: `if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE)` → `dt.mozGetDataAt()`
- 条件付き依存: `if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE)` → `draggedTab.container.tabDragAndDrop.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if (this._rtlMode)` → `movingTabs?.reverse()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `this._getDropIndex()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `gBrowser.duplicateTab()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `duplicatedTabs.push()`
- 条件付き依存: `if (draggedTab && dropEffect == "copy")` → `gBrowser.moveTabsBefore()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `Math.round()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `this._tabbrowserTabs.dragAndDropElements.slice()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`
- 条件付き依存: `if (!(this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab)))` → `tabs.at()`
- 条件付き依存: `if (!(this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab)))` → `movingTabs.at()`
- 条件付き依存: `if (!(this._tabbrowserTabs.isContainerVerticalPinnedGrid(draggedTab)))` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `Math.min()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `Math.max()`
- 条件付き依存: `if (!(this._tabbrowserTabs.verticalMode))` → `Math.min()`
- 条件付き依存: `if (!(this._tabbrowserTabs.verticalMode))` → `Math.max()`
- 条件付き依存: `if (fromTabList)` → `this._getDropIndex()`
- 条件付き依存: `if (dropIndex && dropIndex > movingTabs[0].elementIndex)` → `isSplitViewWrapper()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `movingTabs.some()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `isTab()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `dragToPinTargets.some()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `el.contains()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `this._tabbrowserTabs.arrowScrollbox.contains()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `isTabGroupLabel()`
- 条件付き依存: `if (draggedTab && draggedTab.container == this._tabbrowserTabs)` → `isSplitViewWrapper()`
- 条件付き依存: `if (shouldPin || shouldUnpin)` → `isTab()`
- 条件付き依存: `if (shouldPin && isTab(item))` → `gBrowser.pinTab()`
- 条件付き依存: `if (shouldPin && isTab(item))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (shouldUnpin)` → `gBrowser.unpinTab()`
- 条件付き依存: `if (shouldUnpin)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (shouldTranslate)` → `Date.now()`
- 条件付き依存: `if (shouldTranslate)` → `elementToMove()`
- 条件付き依存: `if (shouldTranslate)` → `item.toggleAttribute()`
- 条件付き依存: `if (gReduceMotion)` → `postTransitionCleanup()`
- 条件付き依存: `if (!(gReduceMotion))` → `item.addEventListener()`
- 条件付き依存: `if (shouldTranslate)` → `translationPromises.push()`
- 条件付き依存: `if (shouldTranslate)` → `Promise.all(translationPromises).then()`
- 条件付き依存: `if (shouldTranslate)` → `Promise.all()`
- 条件付き依存: `if (shouldTranslate)` → `this.finishAnimateTabMove()`
- 条件付き依存: `if (shouldTranslate)` → `moveTabs()`
- 条件付き依存: `if (!(shouldTranslate))` → `this.finishAnimateTabMove()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `gBrowser.addTabGroup()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(shouldCreateGroupOnDrop))` → `isTabGroupLabel()`
- 条件付き依存: `if (!(shouldCreateGroupOnDrop))` → `isTab()`
- 条件付き依存: `if (!(shouldCreateGroupOnDrop))` → `isSplitViewWrapper()`
- 条件付き依存: `if (dropElement.group != draggedTab.group)` → `dropElement.group.addTabs()`
- 条件付き依存: `if (!( shouldDropIntoCollapsedTabGroup && isTabGroupLabel(dropElement) && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) ))` → `moveTabs()`
- 条件付き依存: `if (!( shouldDropIntoCollapsedTabGroup && isTabGroupLabel(dropElement) && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) ))` → `this._tabbrowserTabs._notifyBackgroundTab()`
- 条件付き依存: `if (!( shouldDropIntoCollapsedTabGroup && isTabGroupLabel(dropElement) && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) ))` → `movingTabs.at()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._expandGroupOnDrop()`
- 条件付き依存: `if (!(draggedTab && draggedTab.container == this._tabbrowserTabs))` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._getDropIndex()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `gBrowser.adoptTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `draggedTab.ownerDocument.getElementById()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this.#releaseSpaceInScrolledContent()`
- 条件付き依存: `if (draggedTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (draggedTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (draggedTab)` → `this._getDropIndex()`
- 条件付き依存: `if (!(tab.selected))` → `isSplitViewWrapper()`
- 条件付き依存: `if (isSplitViewWrapper(tab))` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (droppedIntoPinnedArea)` → `unpinnedSplitViews.push()`
- 条件付き依存: `if (!(isSplitViewWrapper(tab)))` → `isTab()`
- 条件付き依存: `if (isTab(tab))` → `gBrowser.adoptTab()`
- 条件付き依存: `if (selectedTab)` → `gBrowser.adoptTab()`
- 条件付き依存: `if (movingTabs.length > 1)` → `isSplitViewWrapper()`
- 条件付き依存: `if (movingTabs.length > 1)` → `firstElement.tabs.at()`
- 条件付き依存: `if (movingTabs.length > 1)` → `lastElement.tabs.at()`
- 条件付き依存: `if ( !(isSplitViewWrapper(firstElement) && firstElement == lastElement) )` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (unpinnedSplitViews.length)` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (unpinnedSplitViews.length)` → `firstUnpinnedSplitView.tabs.at()`
- 条件付き依存: `if (unpinnedSplitViews.length)` → `lastUnpinnedSplitView.tabs.at()`
- 条件付き依存: `if (!(draggedTab))` → `Services.droppedLinkHandler.dropLinks()`
- 条件付き依存: `if (!(draggedTab))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(draggedTab))` → `this._getDragTarget()`
- 条件付き依存: `if (!(draggedTab))` → `this._tabbrowserTabs.selectedItem.getAttribute()`
- 条件付き依存: `if (!(draggedTab))` → `isTab()`
- 条件付き依存: `if (!(draggedTab))` → `this._getDropIndex()`
- 条件付き依存: `if (!(draggedTab))` → `links.map()`
- 条件付き依存: `if (!(draggedTab))` → `Services.droppedLinkHandler.getPolicyContainer()`
- 条件付き依存: `if (!(draggedTab))` → `Services.droppedLinkHandler.getTriggeringPrincipal()`
- 条件付き依存: `if (!(draggedTab))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( urls.length >= Services.prefs.getIntPref("browser.tabs.maxOpenBeforeWarn") )` → `lazy.OpenInTabsUtils.promiseConfirmOpenInTabs()`
- 条件付き依存: `if (!(draggedTab))` → `gBrowser.loadTabs()`
- 参照: `activeEntry.hasUserInteraction`, `draggedTab._dragData`, `draggedTab._dragData.movingTabs`, `draggedTab._dragData.tabGroupCreationColor`, `draggedTab._dragData.tabHeight`, `draggedTab._dragData.tabWidth`, `draggedTab._dragData.translateX`, `draggedTab._dragData.translateY`, `draggedTab.container`, `draggedTab.currentIndex`, `draggedTab.group`, `draggedTab.pinned`, `dropElement.group`, `dt.dropEffect`, `event.dataTransfer`, `event.shiftKey`, `event.target`, `gBrowser.TabMetrics.METRIC_ACTION.ADOPT`, `gBrowser.TabMetrics.METRIC_SOURCE.DRAG_AND_DROP`, `gBrowser.pinnedTabCount`, `item.style.transform`, `link.url`, `links.length`, `movingTabs.length`, `movingTabs[0].elementIndex`, `nextItem.group`, `tab.currentIndex`, `tab.selected`, `tabs.length`, `tabs[tabs.length - 1].currentIndex`, `tabs[tabs.length - 1].elementIndex`, `targetTab?.linkedBrowser?.browsingContext ?.activeSessionHistoryEntry`, `this.#dropAnimationEndTime`, `this._dragToPinPromoCard`, `this._rtlMode`, `this._tabDropIndicator.hidden`, `this._tabbrowserTabs`, `this._tabbrowserTabs.dragAndDropElements`, `this._tabbrowserTabs.pinnedTabsContainer`, `this._tabbrowserTabs.selectedItem`, `this._tabbrowserTabs.verticalMode`, `unpinnedSplitViews.length`, `urls.length`
- XPCOM: `Services.droppedLinkHandler` / `Services.prefs`

## moveTabs()
- 位置: L448-476
- 役割: ドロップ位置情報に従い、移動中のタブを指定位置、または基準要素の前後へ移動する。
- 触るとき: ドロップ後のタブ配置の決め方を変えるとき。
- 条件付き依存: `if (dropIndex !== undefined)` → `isSplitViewWrapper()`
- 条件付き依存: `if (fromTabList && isSplitViewWrapper(tab))` → `gBrowser.moveTabBefore()`
- 条件付き依存: `if (!(fromTabList && isSplitViewWrapper(tab)))` → `gBrowser.moveTabTo()`
- 条件付き依存: `if (dropElement && dropBefore)` → `gBrowser.moveTabsBefore()`
- 条件付き依存: `if (dropElement && dropBefore != undefined)` → `gBrowser.moveTabsAfter()`
- 参照: `this._tabbrowserTabs.dragAndDropElements`

## postTransitionCleanup()
- 位置: L504-507
- 役割: ドロップ移動の遷移後に tabdrop-samewindow 属性を外して Promise を解決する。
- 触るとき: ドロップアニメーション後の後始末を調べるとき。
- 呼び出し先: `item.removeAttribute()`, `resolve()`

## onTransitionEnd()
- 位置: L511-521
- 役割: 対象要素の transform の遷移終了を待ち、リスナーを外して後始末を呼ぶ。
- 触るとき: ドロップアニメーションの完了検知を調べるとき。
- 呼び出し先: `item.removeEventListener()`, `postTransitionCleanup()`
- 参照: `transitionendEvent.originalTarget`, `transitionendEvent.propertyName`

## handle_dragend()
- 位置: L752-921
- 役割: ドラッグ終了時に状態を片付け、どこにも落とされなかった場合は画面位置に合わせて新規ウィンドウへタブを切り出す。
- 触るとき: タブを外へドラッグして新ウィンドウにする挙動(位置やサイズ)を調べるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `Services.prefs.getBoolPref()`, `draggedTab.hasAttribute()`, `dt.mozGetDataAt()`, `event.stopPropagation()`, `isTabGroupLabel()`, `screen.GetAvailRectDisplayPix()`, `this._resetTabsAfterDrop()`, `this.finishAnimateTabMove()`, `this.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedTab))` → `this._expandGroupOnDrop()`
- 条件付き依存: `if (tabAxisPos > tabAxisStart && tabAxisPos < tabAxisEnd)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (gBrowser.tabs.length == 1)` → `window.resizeTo()`
- 条件付き依存: `if (gBrowser.tabs.length == 1)` → `window.moveTo()`
- 条件付き依存: `if (gBrowser.tabs.length == 1)` → `window.focus()`
- 条件付き依存: `if (!(gBrowser.tabs.length == 1))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(gBrowser.tabs.length == 1))` → `gBrowser.replaceTabsWithWindow()`
- 参照: `availHeight.value`, `availWidth.value`, `availX.value`, `availY.value`, `draggedTab._dragData`, `draggedTab._dragData.offsetX`, `draggedTab._dragData.offsetY`, `draggedTab.group`, `dt.dropEffect`, `dt.mozUserCancelled`, `event.dataTransfer`, `event.screen`, `event.screenX`, `event.screenY`, `gBrowser.TabMetrics.METRIC_SOURCE.DRAG_AND_DROP`, `gBrowser.tabs.length`, `props.screenX`, `props.screenY`, `props.suppressinitialfullscreen`, `rect.height`, `rect.left`, `rect.right`, `rect.top`, `rect.width`, `screen.contentsScaleFactor`, `screen.defaultCSSScaleFactor`, `this._tabbrowserTabs .verticalMode`, `this._tabbrowserTabs._isCustomizing`, `this._tabbrowserTabs._sidebarPositionStart`, `this._tabbrowserTabs.arrowScrollbox`, `this._tabbrowserTabs.verticalMode`, `window.desktopToDeviceScale`, `window.devicePixelRatio`, `window.fullScreen`, `window.mozInnerScreenX`, `window.mozInnerScreenY`, `window.outerHeight`, `window.outerWidth`, `window.screenX`, `window.screenY`
- XPCOM: `Services.prefs`

## handle_dragleave()
- 位置: L923-937
- 役割: ドラッグがタブストリップから出たらドロップインジケータを隠す。
- 触るとき: ドラッグ離脱時の表示解除を調べるとき。
- 呼び出し先: `event.stopPropagation()`
- 参照: `event.relatedTarget`, `target.parentNode`, `this.#dragTime`, `this._tabDropIndicator.hidden`, `this._tabbrowserTabs`

## _rtlMode()
- 位置: L941-943
- 役割: 横並びで RTL UI のときに真を返す getter。
- 触るとき: RTL 時に左右を反転する箇所を調べるとき。
- 参照: `this._tabbrowserTabs.verticalMode`

## #setMovingTabMode()
- 位置: L945-954
- 役割: movingtab 属性を切り替え、モードに応じて古いドラッグ状態の監視を開始・停止する。
- 触るとき: ドラッグ中の見た目(movingtab)の切り替えを調べるとき。
- 呼び出し先: `gNavToolbox.toggleAttribute()`, `this._tabbrowserTabs.toggleAttribute()`
- 条件付き依存: `if (movingTab)` → `this.#startStaleDragCheck()`
- 条件付き依存: `if (!(movingTab))` → `this.#stopStaleDragCheck()`

## #dragSession()
- 位置: L956-960
- 役割: このウィンドウの現在のドラッグセッションを nsIDragService から取得する。
- 触るとき: ドラッグセッションの有無の判定を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/dragservice;1"] .getService()`, `Cc["@mozilla.org/widget/dragservice;1"] .getService(Ci.nsIDragService) .getCurrentSession()`
- 参照: `Ci.nsIDragService`
- XPCOM: `nsIDragService` / `@mozilla.org/widget/dragservice;1`

## #startStaleDragCheck()
- 位置: L969-981
- 役割: 一定間隔でドラッグセッションの存在を確認し、無ければ復旧するタイマーと mousedown 監視を開始する。
- 触るとき: ドラッグ後にタブバーが操作不能になる問題を調べるとき。
- 呼び出し先: `setInterval()`, `window.addEventListener()`
- 条件付き依存: `if (!this.#dragSession)` → `this.#recoverFromStaleDrag()`
- 参照: `this.#dragSession`, `this.#onMouseDown`, `this.#staleDragCheckTimer`

## #stopStaleDragCheck()
- 位置: L983-993
- 役割: 古いドラッグの監視タイマーと mousedown リスナーを止める。
- 触るとき: 古いドラッグ監視の停止条件を調べるとき。
- 呼び出し先: `clearInterval()`, `window.removeEventListener()`
- 参照: `this.#dropAnimationEndTime`, `this.#onMouseDown`, `this.#staleDragCheckTimer`

## #onMouseDown()
- 位置: L995-1002
- 役割: 主ボタンの押下を、ドラッグが終了している証拠として復旧処理を呼ぶ。
- 触るとき: ドラッグ終了イベントが来ない場合の復旧経路を調べるとき。
- 条件付き依存: `if (event.button == 0)` → `this.#recoverFromStaleDrag()`
- 参照: `event.button`

## #recoverFromStaleDrag()
- 位置: L1004-1041
- 役割: ドロップアニメーション中でなければドラッグを強制終了し、移動状態をリセットしてテレメトリを記録する。
- 触るとき: ドラッグが終わらず固まる不具合の復旧処理を変えるとき。
- 呼び出し先: `Date.now()`, `Glean.tab.staleDragRecovery[label].add()`, `session?.endDragSession()`, `this._resetTabsAfterDrop()`, `this._tabbrowserTabs.dragAndDropElements.find()`, `this.finishAnimateTabMove()`
- 条件付き依存: `if (draggedItem)` → `this.finishMoveTogetherSelectedTabs()`
- 条件付き依存: `if (draggedItem)` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(draggedItem))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (isTabGroupLabel(draggedItem))` → `this._expandGroupOnDrop()`
- 参照: `Glean.tab.staleDragRecovery`, `draggedItem._dragData`, `draggedItem.group`, `item._dragData`, `this.#dragSession`, `this.#dropAnimationEndTime`

## _getDropIndex()
- 位置: L1043-1068
- 役割: イベント位置の対象要素の中央との前後関係から、ドロップ先の要素インデックスを返す。
- 触るとき: ドロップ位置のインデックス計算がずれるとき。
- 呼び出し先: `elementToMove()`, `this._getDragTarget()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `elementForSize.getBoundingClientRect()`
- 条件付き依存: `if (!(this._tabbrowserTabs.verticalMode))` → `elementForSize.getBoundingClientRect()`
- 参照: `elementForSize.getBoundingClientRect().height`, `elementForSize.getBoundingClientRect().width`, `elementForSize.screenX`, `elementForSize.screenY`, `event.screenX`, `event.screenY`, `item.elementIndex`, `item.splitview`, `this._rtlMode`, `this._tabbrowserTabs.dragAndDropElements.length`, `this._tabbrowserTabs.verticalMode`

## _getDragTarget()
- 位置: L1087-1135
- 役割: イベントが起きたタブ、グループラベル、分割ビューを探し、ignoreSides 指定時は中央部以外を除外する。
- 触るとき: ドラッグ対象の判定領域を変えるとき。
- 呼び出し先: `isSplitViewWrapper()`, `isTab()`, `isTabGroupLabel()`
- 条件付き依存: `if ( findClosestTarget && target === this._tabbrowserTabs.arrowScrollbox && !this._tabbrowserTabs.verticalMode )` → `this.#getHorizontalScrollboxDragTarget()`
- 条件付き依存: `if (target && ignoreSides)` → `target.getBoundingClientRect()`
- 条件付き依存: `if (target && ignoreSides)` → `isTab()`
- 条件付き依存: `if (isTab(target) && target.splitview)` → `target.splitview.tabs.reverse()`
- 条件付き依存: `if (isTab(target) && target.splitview)` → `lTab.getBoundingClientRect()`
- 条件付き依存: `if (isTab(target) && target.splitview)` → `rTab.getBoundingClientRect()`
- 参照: `event.screenX`, `event.screenY`, `lTab.getBoundingClientRect().width`, `lTab.screenX`, `rTab.getBoundingClientRect().width`, `rTab.screenX`, `target.parentNode`, `target.screenX`, `target.screenY`, `target.splitview`, `target.splitview.tabs`, `this._tabbrowserTabs.arrowScrollbox`, `this._tabbrowserTabs.verticalMode`, `window.RTL_UI`

## #getHorizontalScrollboxDragTarget()
- 位置: L1150-1159
- 役割: スクロールボックス上の余白でのイベントを、横方向の位置が重なる要素に対応付ける。
- 触るとき: タブの隙間でドロップしたときの対象判定を調べるとき。
- 呼び出し先: `this._tabbrowserTabs.dragAndDropElements.find()`

## isWithinBounds()
- 位置: L1151-1157
- 役割: 要素の横幅(必要なら両端25%を除く)の範囲にイベントの X が入るかを返す。
- 触るとき: 横方向の当たり判定を調べるとき。
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `el.screenX`, `event.screenX`

## #isMovingTab()
- 位置: L1161-1163
- 役割: tabs 要素に movingtab 属性があるかを返す。
- 触るとき: ドラッグ移動中かの判定を使う箇所を調べるとき。
- 呼び出し先: `this._tabbrowserTabs.hasAttribute()`

## _setIsDraggingTabGroup()
- 位置: L1177-1180
- 役割: タブグループのドラッグ中フラグを設定し、表示中タブのキャッシュを無効化する。
- 触るとき: グループドラッグ中の表示タブ計算を調べるとき。
- 呼び出し先: `this._tabbrowserTabs._invalidateCachedVisibleTabs()`
- 参照: `tabGroup.isBeingDragged`

## _expandGroupOnDrop()
- 位置: L1189-1211
- 役割: ドラッグのために畳んだタブグループを、アニメーション完了後に予約領域を解放しつつ展開し直す。
- 触るとき: グループをドラッグ後に展開が戻る挙動を調べるとき。
- 呼び出し先: `draggedTab.ownerDocument.getElementById()`, `group.addEventListener()`, `isTabGroupLabel()`, `this.#releaseSpaceInScrolledContent()`
- 参照: `draggedTab.group`, `group.collapsed`, `group.collapsedByDrag`

## _triggerDragOverGrouping()
- 位置: L1216-1222
- 役割: グループ化の候補表示(movingtab-group とターゲット属性)を有効にする。
- 触るとき: ドラッグ中のグループ化ハイライトを調べるとき。
- 呼び出し先: `dropElement.toggleAttribute()`, `this._clearDragOverGroupingTimer()`, `this._tabbrowserTabs.removeAttribute()`, `this._tabbrowserTabs.toggleAttribute()`

## _clearDragOverGroupingTimer()
- 位置: L1224-1229
- 役割: グループ化判定用のタイマーがあれば解除する。
- 触るとき: グループ化の遅延タイマーの扱いを調べるとき。
- 条件付き依存: `if (this._dragOverGroupingTimer)` → `clearTimeout()`
- 参照: `this._dragOverGroupingTimer`

## _setDragOverGroupColor()
- 位置: L1231-1254
- 役割: ドラッグ先グループの色用 CSS 変数を設定し、色指定が無ければ削除する。
- 触るとき: ドラッグ中のグループ色表示を変えるとき。
- 呼び出し先: `this._tabbrowserTabs.style.setProperty()`
- 条件付き依存: `if (!groupColorCode)` → `this._tabbrowserTabs.style.removeProperty()`

## _resetGroupTarget()
- 位置: L1259-1261
- 役割: 要素から dragover-groupTarget 属性を外す。
- 触るとき: グループ化ハイライトの解除を調べるとき。
- 呼び出し先: `element?.removeAttribute()`

## startTabDrag()
- 位置: L1265-1491
- 役割: ドラッグ開始時にデータ転送、ドラッグ画像、_dragData、移動モードをまとめて設定する。
- 触るとき: ドラッグ開始時に積むデータやドラッグ画像を変えるとき。
- 呼び出し先: `clientPos()`, `dt.addElement()`, `dt.mozSetDataAt()`, `dt.setDragImage()`, `event.stopPropagation()`, `isSplitViewWrapper()`, `isTab()`, `isTabGroupLabel()`, `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`, `this.getDropEffectForTabDrag()`
- 条件付き依存: `if (this.expandOnHover)` → `MousePosTracker.removeListener()`
- 条件付き依存: `if (this._tabbrowserTabs.isContainerVerticalPinnedGrid(tab))` → `this._tabbrowserTabs.visibleTabs.slice()`
- 条件付き依存: `if (this._tabbrowserTabs.isContainerVerticalPinnedGrid(tab))` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.selectedTabs.filter()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (!(fromTabList || isTabGroupLabel(tab)))` → `selectedElements.filter()`
- 条件付き依存: `if (!(fromTabList || isTabGroupLabel(tab)))` → `[tab].concat()`
- 条件付き依存: `if (isTab(dtTab))` → `dt.mozSetDataAt()`
- 条件付き依存: `if (!canvas)` → `document.createElementNS()`
- 条件付き依存: `if (isSplitViewWrapper(tab))` → `tab.tabs.find()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `canvas.getContext()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `context.fillRect()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `document.createXULElement()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `this._tabbrowserTabs._dndPanel.setAttribute()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `document.createElementNS()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `wrapper.appendChild()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `this._tabbrowserTabs._dndPanel.appendChild()`
- 条件付き依存: `if (!this._tabbrowserTabs._dndPanel)` → `document.documentElement.appendChild()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `PageThumbs.captureToCanvas(browser, canvas) .then(captureListener) .catch()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `PageThumbs.captureToCanvas(browser, canvas) .then()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `PageThumbs.captureToCanvas()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `console.error()`
- 条件付き依存: `if (!(gMultiProcessBrowser))` → `PageThumbs.captureToCanvas(browser, canvas).catch()`
- 条件付き依存: `if (!(gMultiProcessBrowser))` → `PageThumbs.captureToCanvas()`
- 条件付き依存: `if (!(gMultiProcessBrowser))` → `console.error()`
- 条件付き依存: `if (this._rtlMode)` → `tab._dragData.movingTabs.reverse()`
- 条件付き依存: `if (isMovingInTabStrip)` → `this.#setMovingTabMode()`
- 条件付き依存: `if (tab.multiselected)` → `this._moveTogetherSelectedTabs()`
- 条件付き依存: `if (!(tab.multiselected))` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(tab))` → `this._setIsDraggingTabGroup()`
- 条件付き依存: `if (fromTabList)` → `Glean.browserUiInteraction.allTabsPanelDragstartTabEventCount.add()`
- 参照: `AppConstants.platform`, `canvas.height`, `canvas.mozOpaque`, `canvas.style.height`, `canvas.style.width`, `canvas.width`, `context.fillStyle`, `dataTransferOrderedTabs.length`, `document.defaultView.SidebarController`, `dt.mozCursor`, `dtBrowser.currentURI.spec`, `dtTab.linkedBrowser`, `event.dataTransfer`, `event.screenX`, `event.screenY`, `gBrowser.pinnedTabCount`, `gBrowser.selectedElements`, `gBrowser.tabGroupMenu.nextUnusedColor`, `rect.left`, `rect.right`, `splitViewTab.linkedBrowser`, `t.pinned`, `t.selected`, `tab._dragData`, `tab.group`, `tab.group.collapsed`, `tab.linkedBrowser`, `tab.multiselected`, `tab.pinned`, `this._maxTabsPerRow`, `this._rtlMode`, `this._tabbrowserTabs`, `this._tabbrowserTabs._dndCanvas`, `this._tabbrowserTabs._dndPanel`, `this._tabbrowserTabs._dndPanel.className`, `this._tabbrowserTabs.arrowScrollbox.scrollPosition`, `this._tabbrowserTabs.pinnedTabsContainer`, `this._tabbrowserTabs.pinnedTabsContainer.scrollPosition`, `this._tabbrowserTabs.selectedItem`, `this._tabbrowserTabs.verticalMode`, `this.expandOnHover`, `window.devicePixelRatio`, `window.screenX`, `window.screenY`, `window.windowUtils.getBoundsWithoutFlushing( this._tabbrowserTabs.pinnedTabsContainer ).right`, `wrapper.style.height`, `wrapper.style.width`

## captureListener()
- 位置: L1391-1393
- 役割: サムネイル取得後に updateDragImage でドラッグ画像を更新する(Windows と macOS)。
- 触るとき: ドラッグ画像の更新タイミングを調べるとき。
- 呼び出し先: `dt.updateDragImage()`

## clientPos()
- 位置: L1436-1439
- 役割: 要素の縦または横方向の開始位置(top または left)を返す。
- 触るとき: ドラッグ開始時のオフセット計算を調べるとき。
- 呼び出し先: `ele.getBoundingClientRect()`
- 参照: `rect.left`, `rect.top`, `this._tabbrowserTabs.verticalMode`

## #reserveSpaceInScrolledContent()
- 位置: L1500-1506
- 役割: タブ列末尾の要素にマージンを付け、スクロール内容が縮まないよう領域を確保する。
- 触るとき: ドラッグ中にスクロール位置がずれる問題を調べるとき。
- 参照: `periphery.style.marginBlockStart`, `periphery.style.marginInlineStart`, `this._tabbrowserTabs.verticalMode`

## #releaseSpaceInScrolledContent()
- 位置: L1511-1514
- 役割: 確保していた末尾のマージンを解除する。
- 触るとき: 確保領域が戻らない問題を調べるとき。
- 参照: `periphery.style.marginBlockStart`, `periphery.style.marginInlineStart`

## #marginBoxExtent()
- 位置: L1522-1537
- 役割: 要素のマージンを含む、タブ列の軸方向の占有長を返す。
- 触るとき: 確保する領域の長さの計算を調べるとき。
- 呼び出し先: `parseFloat()`, `window.getComputedStyle()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this._tabbrowserTabs.verticalMode)` → `parseFloat()`
- 参照: `rect.height`, `rect.width`, `style.marginBlockEnd`, `style.marginBlockStart`, `style.marginInlineEnd`, `style.marginInlineStart`, `this._tabbrowserTabs.verticalMode`

## _updateTabStylesOnDrag()
- 位置: L1545-1778
- 役割: ドラッグ開始時に、動かすタブを絶対配置にして、周囲のタブや領域の幅・位置を固定し、レイアウトのずれを防ぐ。
- 触るとき: ドラッグ開始時にタブが飛ぶ・詰まるなどの見た目の問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `elementToMove()`, `isTabGroupLabel()`, `movingTab.setAttribute()`, `movingTabsSet.has()`, `t.hasAttribute()`, `tabStripItemElement.hasAttribute()`, `tabsOrigBounds.set()`, `this._tabbrowserTabs.arrowScrollbox.hasAttribute()`, `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (isPinned && this._tabbrowserTabs.verticalMode)` → `this._tabbrowserTabs.pinnedTabsContainer.setAttribute()`
- 条件付き依存: `if (!movingTabsSet.has(t) && !isTabInCollapsingGroup)` → `suppressTransitionsFor.push()`
- 条件付き依存: `if (suppressTransitionsFor.length)` → `window .promiseDocumentFlushed(() => {}) .then()`
- 条件付き依存: `if (suppressTransitionsFor.length)` → `window .promiseDocumentFlushed()`
- 条件付き依存: `if (suppressTransitionsFor.length)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (movingTabs.length == 2)` → `tabStripItemElement.setAttribute()`
- 条件付き依存: `if (movingTabs.length > 2)` → `tabStripItemElement.setAttribute()`
- 条件付き依存: `if ( !isPinned && this._tabbrowserTabs.arrowScrollbox.hasAttribute("overflowing") )` → `this.#marginBoxExtent()`
- 条件付き依存: `if (expandGroupOnDrop)` → `this.#marginBoxExtent()`
- 条件付き依存: `if ( !isPinned && this._tabbrowserTabs.arrowScrollbox.hasAttribute("overflowing") )` → `this.#reserveSpaceInScrolledContent()`
- 条件付き依存: `if (!( !isPinned && this._tabbrowserTabs.arrowScrollbox.hasAttribute("overflowing") ))` → `this._tabbrowserTabs.pinnedTabsContainer.hasAttribute()`
- 条件付き依存: `if ( isPinned && this._tabbrowserTabs.pinnedTabsContainer.hasAttribute("overflowing") )` → `document.createXULElement()`
- 条件付き依存: `if ( isPinned && this._tabbrowserTabs.pinnedTabsContainer.hasAttribute("overflowing") )` → `this._tabbrowserTabs.pinnedTabsContainer.appendChild()`
- 条件付き依存: `if ( (!isPinned && !tabIsPinned) || (tabIsPinned && isPinned && !isGrid) )` → `setElPosition()`
- 条件付き依存: `if (isGrid && tabIsPinned && isPinned)` → `setGridElPosition()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `SidebarController.expandOnHoverComplete.then()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `requestAnimationFrame()`
- 参照: `SidebarController.sidebarMain.clientWidth`, `movingTab.style.height`, `movingTab.style.left`, `movingTab.style.top`, `movingTab.style.width`, `movingTabs.length`, `periphery.style.left`, `periphery.style.top`, `pinnedContainerRect.height`, `pinnedPeriphery.id`, `pinnedPeriphery.style.marginBlockStart`, `pinnedPeriphery.style.width`, `pinnedRect.height`, `pinnedRect.top`, `pinnedRect.width`, `rect.height`, `rect.left`, `rect.top`, `rect.width`, `suppressTransitionsFor.length`, `t.group`, `t.pinned`, `t.style.maxWidth`, `t.style.transition`, `t.style.width`, `tab._dragData`, `tab.documentGlobal`, `tab.group`, `tab.group.tabsAndSplitViews`, `tab.pinned`, `tabContainerRect.top`, `tabRect.width`, `tabStripItemElement.offsetParent`, `tabStripItemElement.style.pointerEvents`, `this._rtlMode`, `this._tabbrowserTabs`, `this._tabbrowserTabs.arrowScrollbox.scrollbox`, `this._tabbrowserTabs.arrowScrollbox.scrollbox.style.height`, `this._tabbrowserTabs.arrowScrollbox.scrollbox.style.width`, `this._tabbrowserTabs.dragAndDropElements`, `this._tabbrowserTabs.expandOnHover`, `this._tabbrowserTabs.overflowing`, `this._tabbrowserTabs.pinnedTabsContainer`, `this._tabbrowserTabs.pinnedTabsContainer.firstChild`, `this._tabbrowserTabs.pinnedTabsContainer.scrollbox`, `this._tabbrowserTabs.pinnedTabsContainer.scrollbox.style.height`, `this._tabbrowserTabs.pinnedTabsContainer.scrollbox.style.width`, `this._tabbrowserTabs.pinnedTabsContainer.style.minHeight`, `this._tabbrowserTabs.verticalMode`, `unpinnedRect.height`, `unpinnedRect.width`, `window.windowUtils.getBoundsWithoutFlushing( tabStripItemElement.offsetParent ).x`

## setElPosition()
- 位置: L1702-1713
- 役割: ドラッグ中のタブの抜けた分、後続の要素を元の位置に見えるようずらす。
- 触るとき: タブを持ち上げたときの他のタブの位置保持を調べるとき。
- 呼び出し先: `tabsOrigBounds.get()`
- 参照: `el.style.left`, `el.style.top`, `origBounds.left`, `origBounds.top`, `rect.height`, `rect.left`, `rect.top`, `rect.width`, `this._rtlMode`, `this._tabbrowserTabs.verticalMode`

## setGridElPosition()
- 位置: L1715-1729
- 役割: ピン留めグリッドで要素を元の位置に見えるよう差分だけずらす。
- 触るとき: 縦タブのピン留めグリッドでのドラッグ時の位置ずれを調べるとき。
- 呼び出し先: `el.getBoundingClientRect()`, `tabsOrigBounds.get()`
- 参照: `el.style.left`, `el.style.top`, `newBounds.x`, `newBounds.y`, `origBounds.x`, `origBounds.y`

## _moveTogetherSelectedTabs()
- 位置: L1783-1952
- 役割: 複数選択タブを、ドラッグ中のタブの周囲に寄せるアニメーションと、他のタブの移動量・新しい位置の計算を準備する。
- 触るとき: 複数選択タブをドラッグしたときに寄せ集める動作や位置の計算を調べるとき。
- 呼び出し先: `addAnimationData()`, `elementToMove()`, `selectedElement.getBoundingClientRect()`, `selectedElements.indexOf()`, `selectedElements.map()`, `selectedElements.some()`, `tab._dragData.movingTabsSet.has()`, `tab.toggleAttribute()`, `this._tabbrowserTabs.isContainerVerticalPinnedGrid()`
- 条件付き依存: `if (unmovingTab.elementIndex > selectedIndices[currentIndex])` → `selectedElements .find(t => t.elementIndex == selectedIndices[currentIndex]) .getBoundingClientRect()`
- 条件付き依存: `if (unmovingTab.elementIndex > selectedIndices[currentIndex])` → `selectedElements .find()`
- 条件付き依存: `if (isGrid)` → `unmovingTab.getBoundingClientRect()`
- 条件付き依存: `if (isGrid)` → `this._tabbrowserTabs.dragAndDropElements[ newIndex ].getBoundingClientRect()`
- 条件付き依存: `if ( !tab._dragData.movingTabsSet.has(item) && (item._moveTogetherSelectedTabsData?.translateX || item._moveTogetherSelectedTabsData?.translateY) && ((item.pinne...)` → `elementToMove()`
- 条件付き依存: `if ( item._moveTogetherSelectedTabsData?.translateX || item._moveTogetherSelectedTabsData?.translateY )` → `elementToMove()`
- 参照: `currentRect.height`, `currentRect.width`, `draggedRect.height`, `draggedRect.width`, `element.style.transform`, `gBrowser.selectedElements`, `item._moveTogetherSelectedTabsData.translateX`, `item._moveTogetherSelectedTabsData.translateY`, `item._moveTogetherSelectedTabsData?.translateX`, `item._moveTogetherSelectedTabsData?.translateY`, `item.pinned`, `oldTabRect.x`, `oldTabRect.y`, `selectedElement.elementIndex`, `selectedElements.length`, `t.elementIndex`, `t.pinned`, `tab._moveTogetherSelectedTabsData`, `tab.pinned`, `this._rtlMode`, `this._tabbrowserTabs.dragAndDropElements`, `this._tabbrowserTabs.verticalMode`, `unmovingTab._moveTogetherSelectedTabsData`, `unmovingTab._moveTogetherSelectedTabsData.translateX`, `unmovingTab._moveTogetherSelectedTabsData.translateY`, `unmovingTab.currentIndex`, `unmovingTab.elementIndex`, `unmovingTab.multiselected`, `unmovingTabRect.x`, `unmovingTabRect.y`

## addAnimationData()
- 位置: L1801-1835
- 役割: 寄せ集める対象のタブに移動量を設定し、遷移完了を待つ準備をする。
- 触るとき: 寄せ集めアニメーションの個別タブの設定を調べるとき。
- 呼び出し先: `movingElement.getBoundingClientRect()`, `movingElement.toggleAttribute()`, `selectedElement.getBoundingClientRect()`
- 条件付き依存: `if (gReduceMotion)` → `postTransitionCleanup()`
- 条件付き依存: `if (!(gReduceMotion))` → `movingElement.addEventListener()`
- 参照: `movingElement._moveTogetherSelectedTabsData`, `movingElement._moveTogetherSelectedTabsData.translateX`, `movingElement._moveTogetherSelectedTabsData.translateY`, `movingTabRect.x`, `movingTabRect.y`, `tabRect.x`, `tabRect.y`

## postTransitionCleanup()
- 位置: L1809-1811
- 役割: 寄せ集めアニメーション中の印(animate)を偽にする。
- 触るとき: 寄せ集めアニメーション完了の扱いを調べるとき。
- 参照: `movingElement._moveTogetherSelectedTabsData.animate`

## onTransitionEnd()
- 位置: L1815-1824
- 役割: 対象タブの transform の遷移終了を待ち、リスナーを外して後始末を呼ぶ。
- 触るとき: 寄せ集めアニメーション完了の検知を調べるとき。
- 呼び出し先: `movingElement.removeEventListener()`, `postTransitionCleanup()`
- 参照: `transitionendEvent.originalTarget`, `transitionendEvent.propertyName`

## #isAnimatingMoveTogetherSelectedTabs()
- 位置: L1954-1961
- 役割: 選択タブのどれかが寄せ集めアニメーション中かを返す。
- 触るとき: アニメーション中にドラッグ処理を待たせる条件を調べるとき。
- 参照: `element._moveTogetherSelectedTabsData?.animate`, `gBrowser.selectedElements`

## finishMoveTogetherSelectedTabs()
- 位置: L1963-1993
- 役割: 選択タブをドラッグ中のタブの前後へ実際に移動し、一時的な移動データと transform を消す。
- 触るとき: 寄せ集めの確定処理を調べるとき。
- 呼び出し先: `elementToMove()`, `gBrowser.moveTabAfter()`, `gBrowser.moveTabBefore()`, `item.removeAttribute()`, `selectedElements.indexOf()`
- 参照: `gBrowser.selectedElements`, `item._moveTogetherSelectedTabsData`, `item.style.transform`, `selectedElements.length`, `tab._moveTogetherSelectedTabsData`, `tab._moveTogetherSelectedTabsData.finished`, `this._tabbrowserTabs.dragAndDropElements`

## _animateExpandedPinnedTabMove()
- 位置: L1997-2179
- 役割: 展開した縦タブのピン留めグリッド上で、ドラッグ中のタブを追従させ、二分探索でドロップ位置を決めて他のタブをずらす。
- 触るとき: 縦タブのピン留めグリッドでのドラッグ並べ替えの不具合を調べるとき。
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `document.getElementById()`, `draggedTab.getBoundingClientRect()`, `event.dataTransfer.mozGetDataAt()`, `getTabShift()`, `movingTabs.includes()`, `tabs.filter()`, `this._tabbrowserTabs.visibleTabs.slice()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (tab != draggedTab)` → `getTabShift()`
- 参照: `dragData.animDropElementIndex`, `dragData.animLastScreenX`, `dragData.animLastScreenY`, `dragData.dropBefore`, `dragData.dropElement`, `dragData.movingTabs`, `dragData.screenX`, `dragData.screenY`, `dragData.tabHeight`, `dragData.tabWidth`, `dragData.translateX`, `dragData.translateY`, `draggedTab._dragData`, `draggedTab.elementIndex`, `draggedTab.screenX`, `draggedTab.screenY`, `event.screenX`, `event.screenY`, `gBrowser.pinnedTabCount`, `periphery.screenY`, `tab.style.transform`, `tabs.length`, `tabs[mid].currentIndex`, `tabs[mid].screenX`, `tabs[mid].screenY`, `this._maxTabsPerRow`, `this._tabbrowserTabs`, `this._tabbrowserTabs.screenX`, `this._tabbrowserTabs.screenY`, `window.windowUtils.getBoundsWithoutFlushing(this._tabbrowserTabs) .width`

## getTabShift()
- 位置: L2081-2120
- 役割: ピン留めグリッドで、ドロップ位置に応じた各タブのずれ量(行の折り返しを含む)を返す。
- 触るとき: グリッド上のタブのずれ量の計算を調べるとき。
- 条件付き依存: `if ( tab.currentIndex < draggedTab.elementIndex && tab.currentIndex >= dropIndex )` → `Math.ceil()`
- 条件付き依存: `if ( tab.currentIndex > draggedTab.elementIndex && tab.currentIndex < dropIndex )` → `Math.floor()`
- 参照: `draggedTab.elementIndex`, `tab.currentIndex`, `tab.elementIndex`, `tab?.currentIndex`, `this._maxTabsPerRow`

## _animateTabMove()
- 位置: L2182-2713
- 役割: ドラッグ中のタブを追従させ、重なり割合からドロップ先とグループ化の可否を判定して、他のタブをずらしてすき間を作る。
- 触るとき: ドラッグ中のタブ並べ替えアニメーション、グループ化の判定、ドロップ位置の決定を調べるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `bounds()`, `document.getElementById()`, `dragAndDropElements.slice()`, `elementToMove()`, `endEdge()`, `event.dataTransfer.mozGetDataAt()`, `getOverlappedElement()`, `getTabShift()`, `isSplitViewWrapper()`, `isTab()`, `movingTabsSet.has()`, `tabs.filter()`, `this.#clearPinnedDropIndicatorTimer()`, `this._clearDragOverGroupingTimer()`
- 条件付き依存: `if (this._rtlMode)` → `tabs.reverse()`
- 条件付き依存: `if ( (screen < draggedTabScreenAxis || screen > draggedTabScreenAxis + tabSize) && draggedTabScreenAxis + tabSize < endBound && draggedTabScreenAxis > startBound )` → `Math.min()`
- 条件付き依存: `if ( (screen < draggedTabScreenAxis || screen > draggedTabScreenAxis + tabSize) && draggedTabScreenAxis + tabSize < endBound && draggedTabScreenAxis > startBound )` → `Math.max()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `parseFloat()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `window.getComputedStyle()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `this._checkWithinPinnedContainerBounds()`
- 条件付き依存: `if (!gBrowser.pinnedTabCount && !this._dragToPinPromoCard.shouldRender)` → `endEdge()`
- 条件付き依存: `if (!(dropElement))` → `tabs.find()`
- 条件付き依存: `if (!(dropElement))` → `tabs.findLast()`
- 条件付き依存: `if (!(dropElement))` → `Number.isInteger()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `Math.min()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `this._tabbrowserTabs.dragAndDropElements .filter(t => !movingTabsSet.has(t) || t == draggedTab) .at()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `this._tabbrowserTabs.dragAndDropElements .filter()`
- 条件付き依存: `if (Number.isInteger(maxElementIndexForDropElement))` → `movingTabsSet.has()`
- 条件付き依存: `if (dropElement)` → `elementToMove()`
- 条件付き依存: `if (dropElement)` → `getTabShift()`
- 条件付き依存: `if (dropElement)` → `bounds()`
- 条件付き依存: `if (dropElement)` → `greatestOverlap()`
- 条件付き依存: `if (dropElement)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (dropElement)` → `Math.min()`
- 条件付き依存: `if (dropElement)` → `Math.max()`
- 条件付き依存: `if (dropElement)` → `isTabGroupLabel()`
- 条件付き依存: `if ( isTabGroupLabel(draggedTab) && dropElement?.group && (!dropElement.group.collapsed || (dropElement.group.collapsed && dropElement.group.hasActiveTab)) )` → `isTabGroupLabel()`
- 条件付き依存: `if (!(isTabGroupLabel(dropElement)))` → `overlappedGroup.tabsAndSplitViews.findLast()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `movingTabsSet.has()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `isTab()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `isSplitViewWrapper()`
- 条件付き依存: `if ( Tabbrowser.prefs.tabGroupsEnabled && (isTab(draggedTab) || isSplitViewWrapper(draggedTab)) && !isPinned && (!numPinned || newDropElementIndex >= numPinned) )` → `isTabGroupLabel()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `setTimeout()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `this._triggerDragOverGrouping()`
- 条件付き依存: `if (shouldCreateGroupOnDrop)` → `this._setDragOverGroupColor()`
- 条件付き依存: `if (shouldDropIntoCollapsedTabGroup)` → `setTimeout()`
- 条件付き依存: `if (shouldDropIntoCollapsedTabGroup)` → `this._triggerDragOverGrouping()`
- 条件付き依存: `if (shouldDropIntoCollapsedTabGroup)` → `this._setDragOverGroupColor()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._tabbrowserTabs.removeAttribute()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._resetGroupTarget()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `document.querySelector()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `dropElementGroup?.tabs.findLast()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `movingTabsSet.has()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `isTab()`
- 条件付き依存: `if (!( isTab(dropElement) && dropElementGroup && dropElement == lastUnmovingTabInGroup && !dropBefore && overlapPercent < dragOverGroupingThreshold ))` → `isTabGroupLabel()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._setDragOverGroupColor()`
- 条件付き依存: `if (!(shouldDropIntoCollapsedTabGroup))` → `this._tabbrowserTabs.toggleAttribute()`
- 参照: `Tabbrowser.prefs.tabGroupsEnabled`, `dragData.animDropElementIndex`, `dragData.animLastScreenPos`, `dragData.dropBefore`, `dragData.dropElement`, `dragData.movingTabs`, `dragData.movingTabsSet`, `dragData.screenX`, `dragData.screenY`, `dragData.shouldCreateGroupOnDrop`, `dragData.shouldDropIntoCollapsedTabGroup`, `dragData.tabGroupCreationColor`, `dragData.tabHeight`, `dragData.tabWidth`, `dragData.translatePos`, `dragData.translateX`, `dragData.translateY`, `draggedTab._dragData`, `draggedTab.elementIndex`, `draggedTab.pinned`, `dropElement.elementIndex`, `dropElement.group`, `dropElement.group.collapsed`, `dropElement.group.color`, `dropElement.group.hasActiveTab`, `dropElement?.currentIndex`, `dropElement?.group`, `dropElementGroup.collapsed`, `dropElementGroup.tabs`, `dropElementGroup?.color`, `ele.visible`, `event.screenX`, `event.screenY`, `gBrowser.pinnedTabCount`, `item.style.transform`, `lastPossibleDropElement?.currentIndex`, `lastPossibleDropElement?.elementIndex`, `lastVisibleTabInGroup.elementIndex`, `lastVisibleTabInGroup?.currentIndex`, `this._dragOverGroupingTimer`, `this._dragToPinPromoCard.shouldRender`, `this._pinnedDropIndicator`, `this._rtlMode`, `this._tabbrowserTabs`, `this._tabbrowserTabs.arrowScrollbox`, `this._tabbrowserTabs.dragAndDropElements`, `this._tabbrowserTabs.verticalMode`, `window.getComputedStyle(this._pinnedDropIndicator).marginInline`
- XPCOM: `Services.prefs`

## bounds()
- 位置: L2215-2215
- 役割: 要素の境界矩形をレイアウトを強制せずに取得する。
- 触るとき: 境界取得の方法を確認するとき。
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## endEdge()
- 位置: L2231-2231
- 役割: 要素の軸方向の終端位置(画面座標)を返す。
- 触るとき: 移動範囲の端の計算を調べるとき。
- 呼び出し先: `bounds()`

## getTabShift()
- 位置: L2318-2335
- 役割: ドロップ位置に応じて、各要素がどれだけ前後にずれるかを返す。
- 触るとき: ドラッグ中に他のタブが避ける量の計算を調べるとき。
- 参照: `draggedTab.elementIndex`, `item.currentIndex`, `item.elementIndex`, `item?.currentIndex`, `this._rtlMode`

## greatestOverlap()
- 位置: L2381-2400
- 役割: 二つの区間の重なりの割合を各々から見て大きい方で返す(0から1)。
- 触るとき: タブが重なったとみなす判定を調べるとき。
- 呼び出し先: `Math.max()`, `Math.min()`

## getOverlappedElement()
- 位置: L2418-2442
- 役割: 移動中のタブの先頭端と重なるタブまたはグループラベルを二分探索で探す。
- 触るとき: ドラッグ中にどのタブの上にいるかの判定を調べるとき。
- 呼び出し先: `Math.floor()`, `elementToMove()`, `getTabShift()`
- 条件付き依存: `if (!(screen > point))` → `bounds()`
- 参照: `tabs.length`

## _checkWithinPinnedContainerBounds()
- 位置: L2715-2778
- 役割: 移動中のタブがピン留め領域に近づいたかで、ピン留めドロップ表示の可視・操作可能状態を切り替える。
- 触るとき: ドラッグでピン留めする際の表示タイミングを調べるとき。
- 呼び出し先: `this._pinnedDropIndicator.hasAttribute()`
- 条件付き依存: `if ( this.#pinnedDropIndicatorTimeout && !inPinnedRange && !inVisibleRange && !isVisible && !isInteractive )` → `this.#resetPinnedDropIndicator()`
- 条件付き依存: `if (!( this.#pinnedDropIndicatorTimeout && !inPinnedRange && !inVisibleRange && !isVisible && !isInteractive ))` → `isTab()`
- 条件付き依存: `if ( isTab(draggedTab) && ((inVisibleRange && !isVisible) || (inPinnedRange && !isInteractive)) )` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (isVisible)` → `this._pinnedDropIndicator.setAttribute()`
- 条件付き依存: `if (!this.#pinnedDropIndicatorTimeout)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (!this.#pinnedDropIndicatorTimeout)` → `setTimeout()`
- 条件付き依存: `if (!this.#pinnedDropIndicatorTimeout)` → `this.#isMovingTab()`
- 条件付き依存: `if (this.#isMovingTab())` → `this._pinnedDropIndicator.setAttribute()`
- 条件付き依存: `if (!inPinnedRange)` → `this._pinnedDropIndicator.removeAttribute()`
- 参照: `tabbrowserTabsRect.width`, `this.#pinnedDropIndicatorTimeout`, `this._rtlMode`, `this._tabbrowserTabs`, `this._tabbrowserTabs.style.maxWidth`, `this._tabbrowserTabs.verticalMode`
- XPCOM: `Services.prefs`

## #clearPinnedDropIndicatorTimer()
- 位置: L2780-2785
- 役割: ピン留めドロップ表示の待機タイマーがあれば解除する。
- 触るとき: ピン留め表示の遅延タイマーの扱いを調べるとき。
- 条件付き依存: `if (this.#pinnedDropIndicatorTimeout)` → `clearTimeout()`
- 参照: `this.#pinnedDropIndicatorTimeout`

## #resetPinnedDropIndicator()
- 位置: L2787-2791
- 役割: タイマーを解除してピン留めドロップ表示の属性(visible と interactive)を外す。
- 触るとき: ピン留め表示の解除条件を調べるとき。
- 呼び出し先: `this.#clearPinnedDropIndicatorTimer()`, `this._pinnedDropIndicator.removeAttribute()`

## finishAnimateTabMove()
- 位置: L2793-2811
- 役割: 移動モードを終えて、transform、グループ化関連の属性、ピン留め表示を元に戻す。
- 触るとき: ドラッグ終了後に見た目が残る問題を調べるとき。
- 呼び出し先: `elementToMove()`, `this.#isMovingTab()`, `this.#resetPinnedDropIndicator()`, `this.#setMovingTabMode()`, `this._clearDragOverGroupingTimer()`, `this._resetGroupTarget()`, `this._setDragOverGroupColor()`, `this._tabbrowserTabs.removeAttribute()`
- 参照: `item.style.transform`, `this._tabbrowserTabs.dragAndDropElements`

## _resetTabsAfterDrop()
- 位置: L2820-2908
- 役割: ドラッグ用に付けた各種スタイルや属性、予約領域、ピン留めの補助要素を、タブ、ラベル、分割ビューから取り除く。
- 触るとき: ドロップ後にタブの位置やサイズがおかしいままになる問題を調べるとき。
- 呼び出し先: `draggedTabContainer.getElementsByClassName()`, `draggedTabContainer.getElementsByTagName()`, `draggedTabDocument.defaultView.SidebarController.updatePinnedTabsHeightOnResize()`, `draggedTabDocument.getElementById()`, `draggedTabDocument.getElementsByClassName()`, `isTabGroupLabel()`, `label.removeAttribute()`, `pinnedDropIndicator.removeAttribute()`, `pinnedTabsContainer.removeAttribute()`, `pinnedTabsContainer.removeChild()`, `splitviewWrapper.removeAttribute()`, `tab.removeAttribute()`
- 条件付き依存: `if (this._tabbrowserTabs.expandOnHover)` → `MousePosTracker.addListener()`
- 条件付き依存: `if (!isTabGroupLabel(draggedTab) || !draggedTab.group.collapsedByDrag)` → `this.#releaseSpaceInScrolledContent()`
- 参照: `arrowScrollbox.scrollbox.style.height`, `arrowScrollbox.scrollbox.style.width`, `document.defaultView.SidebarController`, `draggedTab.group.collapsedByDrag`, `draggedTab?.ownerDocument`, `draggedTabContainer.style.maxWidth`, `draggedTabDocument.documentGlobal.gBrowser.tabContainer`, `groupLabel.style.left`, `groupLabel.style.top`, `label.currentIndex`, `label.style.height`, `label.style.left`, `label.style.maxWidth`, `label.style.pointerEvents`, `label.style.top`, `label.style.width`, `periphery.style.left`, `periphery.style.top`, `pinnedTabsContainer.scrollbox.style.height`, `pinnedTabsContainer.scrollbox.style.width`, `pinnedTabsContainer.style.minHeight`, `splitviewWrapper.style.height`, `splitviewWrapper.style.left`, `splitviewWrapper.style.maxWidth`, `splitviewWrapper.style.pointerEvents`, `splitviewWrapper.style.top`, `splitviewWrapper.style.width`, `tab.style.left`, `tab.style.maxWidth`, `tab.style.pointerEvents`, `tab.style.top`, `tab.style.width`, `this._tabbrowserTabs.expandOnHover`

## getDropEffectForTabDrag()
- 位置: L2914-2967
- 役割: ドラッグ内容から drop effect(move、copy、link、none)を決め、プライベート状態やプロセス構成の違うウィンドウ間は拒否する。
- 触るとき: どのドラッグが受け入れられるか、ウィンドウ間の移動可否を調べるとき。
- 呼び出し先: `Services.droppedLinkHandler.canDropLink()`, `dt.mozTypesAt()`
- 条件付き依存: `if (isMovingTab)` → `dt.mozGetDataAt()`
- 条件付き依存: `if (isMovingTab)` → `isTab()`
- 条件付き依存: `if (isMovingTab)` → `isTabGroupLabel()`
- 条件付き依存: `if (isMovingTab)` → `isSplitViewWrapper()`
- 条件付き依存: `if (isMovingTab)` → `sourceNode.ownerDocument.documentElement.getAttribute()`
- 条件付き依存: `if ( (isTab(sourceNode) || isTabGroupLabel(sourceNode) || isSplitViewWrapper(sourceNode)) && sourceNode.documentGlobal.isChromeWindow && sourceNode.ownerDocument...)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `dt.dropEffect`, `dt.mozItemCount`, `event.dataTransfer`, `sourceNode.documentGlobal`, `sourceNode.documentGlobal.gFissionBrowser`, `sourceNode.documentGlobal.gMultiProcessBrowser`, `sourceNode.documentGlobal.isChromeWindow`, `window.gFissionBrowser`, `window.gMultiProcessBrowser`
- XPCOM: `Services.droppedLinkHandler`
