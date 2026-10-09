# browser/components/tabbrowser/content/tabs.mjs

source: browser/components/tabbrowser/content/tabs.mjs
source-hash: d8775258e178fdeb17964996a86e7cefbb991b33
lines: 1792

## <module>
- 役割: タブ列の要素 MozTabbrowserTabs を定義し、カスタム要素として登録するモジュール。
- 呼び出し先: `customElements.define()`

## MozTabbrowserTabs.constructor()
- 位置: L18-55
- 役割: タブ選択・グループ・クリック・ドラッグなど、タブ列が受け取る各種イベントのリスナーを登録する。
- 触るとき: タブ列に新しいイベントを受けさせたいとき、リスナーの登録漏れや順序(キャプチャ)を調べるとき。
- 呼び出し先: `super()`, `this.addEventListener()`

## MozTabbrowserTabs.init()
- 位置: L57-211
- 役割: スクロールボックス、プリファレンス監視、リサイズ監視、ドラッグ処理などタブ列の初期設定をまとめて行う。
- 触るとき: タブ列の起動時の状態、初期化順、関連プリファレンスの扱いを変更・調査するとき。
- 呼び出し先: `CustomizableUI.addListener()`, `DynamicShortcutTooltip.getText()`, `Math.max()`, `Object.defineProperty()`, `Services.prefs.addObserver()`, `Services.prefs.getIntPref()`, `Services.startup.getStartupInfo()`, `Services.startup.getStartupInfo().start.getTime()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `document .getElementById()`, `document .getElementById("tabs-newtab-button") .addEventListener()`, `document .getElementById("vertical-tabs-newtab-button") .addEventListener()`, `document.getElementById()`, `this.#updateTabMinWidth()`, `this._fullscreenMutationObserver.observe()`, `this._updateNewTabVisibility()`, `this.arrowScrollbox.addEventListener()`, `this.baseConnect()`, `this.getAttribute()`, `this.newTabButton.setAttribute()`, `this.observe()`, `this.pinnedTabsContainer.setAttribute()`, `this.querySelector()`, `this.tabDragAndDrop.init()`, `this.updateWheelListeners()`, `window.addEventListener()`
- 条件付き依存: `if (gMultiProcessBrowser)` → `this.tabbox.tabpanels.setAttribute()`
- 参照: `document.documentElement`, `this._animateElement`, `this._blockDblClick`, `this._closeButtonsUpdatePending`, `this._closingTabsSpacer`, `this._fullscreenMutationObserver`, `this._hasTabTempMaxWidth`, `this._hiddenSoundPlayingTabs`, `this._lastTabClosedByMouse`, `this._scrollButtonWidth`, `this._tabClipWidth`, `this._tabDefaultMaxWidth`, `this._tabMinWidthPref`, `this.allTabs`, `this.allTabs[0].label`, `this.arrowScrollbox`, `this.arrowScrollbox._canScrollToElement`, `this.arrowScrollbox._getScrollableElements`, `this.boundObserve`, `this.emptyTabTitle`, `this.pinnedTabsContainer`, `this.previewPanel`, `this.startupTime`, `this.tabDragAndDrop`, `this.tooltip`, `window.TabDragAndDrop`
- XPCOM: `Services.prefs` / `Services.startup`

## this.arrowScrollbox._getScrollableElements()
- 位置: L71-87
- 役割: スクロール可能な要素として、固定されていないタブ(選択中の折りたたみグループは overflow コンテナも)を返すよう上書きする。
- 触るとき: タブ列のスクロール対象や折りたたみグループ周りのスクロール位置がおかしいとき。
- 呼び出し先: `this.ariaFocusableItems.reduce()`, `this.arrowScrollbox._canScrollToElement()`
- 条件付き依存: `if (this.arrowScrollbox._canScrollToElement(item))` → `elements.push()`
- 条件付き依存: `if (this.arrowScrollbox._canScrollToElement(item))` → `isTab()`
- 条件付き依存: `if ( isTab(item) && item.group && item.group.collapsed && item.selected )` → `elements.push()`
- 参照: `item.group`, `item.group.collapsed`, `item.group.overflowContainer`, `item.selected`

## this.arrowScrollbox._canScrollToElement()
- 位置: L88-93
- 役割: 固定タブ以外の要素をスクロール先にできると判定する。
- 触るとき: 固定タブがスクロール対象に含まれる/含まれない問題を調べるとき。
- 呼び出し先: `isTab()`
- 参照: `element.pinned`

## get()
- 位置: L104-104
- 役割: マウスホイール1回分のスクロール量としてタブの最小幅の設定値を返す。
- 触るとき: タブ列のホイールスクロール量を変えるとき。
- 参照: `this._tabMinWidthPref`

## handleResize()
- 位置: L128-131
- 役割: ウィンドウのリサイズやフルスクリーン切替時に閉じるボタンの表示とタブ選択後の位置合わせを更新する。
- 触るとき: リサイズ後の閉じるボタン表示やスクロール位置のずれを調べるとき。
- 呼び出し先: `this._handleTabSelect()`, `this._updateCloseButtons()`

## this.boundObserve()
- 位置: L139-139
- 役割: プリファレンス監視の通知を this.observe に転送する束縛済み関数。
- 触るとき: プリファレンス監視の登録・解除まわりを調べるとき。
- 呼び出し先: `this.observe()`

## MozTabbrowserTabs.attributeChangedCallback()
- 位置: L213-221
- 役割: orient 属性の変更時に overflow を消し、タブ最小幅と固定タブ領域の向きを更新する。
- 触るとき: 縦タブと横タブの切替時のスタイルや状態の不整合を調べるとき。
- 呼び出し先: `super.attributeChangedCallback()`
- 条件付き依存: `if (attrName == "orient")` → `this.removeAttribute()`
- 条件付き依存: `if (attrName == "orient")` → `this.#updateTabMinWidth()`
- 条件付き依存: `if (attrName == "orient")` → `this.pinnedTabsContainer?.setAttribute()`

## MozTabbrowserTabs.handleEvent()
- 位置: L225-256
- 役割: mouseout/mousemove/mouseleave を処理し、それ以外は on_<イベント名> メソッドへ振り分ける。
- 触るとき: イベントの振り分けや未対応イベントのエラーを調べるとき、タブ幅ロック解除の契機を見るとき。
- 呼び出し先: `document.getElementById()`, `this.#isMovingTab()`, `this.previewPanel?.deactivate()`
- 条件付き依存: `if ( document.getElementById("tabContextMenu").state != "open" && !this.#isMovingTab() )` → `this._unlockTabSizing()`
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `aEvent.relatedTarget`, `aEvent.type`, `document.getElementById("tabContextMenu").state`, `relatedTarget.ownerDocument`

## MozTabbrowserTabs.on_TabSelect()
- 位置: L261-273
- 役割: タブ選択時、折りたたみグループが絡む場合は可視タブのキャッシュを破棄し、選択処理を呼ぶ。
- 触るとき: タブ選択後の可視タブ一覧やスクロール位置の問題を調べるとき。
- 呼び出し先: `this._handleTabSelect()`
- 条件付き依存: `if (previousTab.group?.collapsed || newTab.group?.collapsed)` → `this._invalidateCachedVisibleTabs()`
- 参照: `newTab.group?.collapsed`, `previousTab.group?.collapsed`

## MozTabbrowserTabs.on_TabClose()
- 位置: L275-277
- 役割: 閉じられたタブについて、非表示で音を出していたタブの状態更新を依頼する。
- 触るとき: 音を出す非表示タブを閉じたときの表示を調べるとき。
- 呼び出し先: `this._hiddenSoundPlayingStatusChanged()`
- 参照: `event.target`

## MozTabbrowserTabs.on_TabAttrModified()
- 位置: L279-293
- 役割: 音再生・ミュート・メディアブロックの属性変更を受けて、非表示タブの状態とタブの音ラベルを更新する。
- 触るとき: タブの音関連の表示やラベルの更新条件を変えるとき。
- 呼び出し先: `event.detail.changed.includes()`
- 条件付き依存: `if ( event.detail.changed.includes("soundplaying") && !event.target.visible )` → `this._hiddenSoundPlayingStatusChanged()`
- 条件付き依存: `if ( event.detail.changed.includes("soundplaying") || event.detail.changed.includes("muted") || event.detail.changed.includes("activemedia-blocked") )` → `this.updateTabSoundLabel()`
- 参照: `event.target`, `event.target.visible`

## MozTabbrowserTabs.on_TabHide()
- 位置: L295-299
- 役割: 音を出しているタブが隠れたとき、非表示タブの音状態を更新する。
- 触るとき: タブを隠したときの音アイコン表示を調べるとき。
- 条件付き依存: `if (event.target.soundPlaying)` → `this._hiddenSoundPlayingStatusChanged()`
- 参照: `event.target`, `event.target.soundPlaying`

## MozTabbrowserTabs.on_TabShow()
- 位置: L301-305
- 役割: 音を出しているタブが再表示されたとき、非表示タブの音状態を更新する。
- 触るとき: タブを再表示したときの音アイコン表示を調べるとき。
- 条件付き依存: `if (event.target.soundPlaying)` → `this._hiddenSoundPlayingStatusChanged()`
- 参照: `event.target`, `event.target.soundPlaying`

## MozTabbrowserTabs.on_TabHoverStart()
- 位置: L307-313
- 役割: タブのホバープレビューが有効なら、プレビューパネルを読み込んでそのタブ用に開始する。
- 触るとき: タブのホバープレビューの出方や有効条件を変えるとき。
- 呼び出し先: `this.ensureTabPreviewPanelLoaded()`, `this.previewPanel.activate()`
- 参照: `event.target`, `this._showTabHoverPreview`

## MozTabbrowserTabs.on_TabHoverEnd()
- 位置: L315-317
- 役割: ホバーが終わったタブのプレビューパネルを止める。
- 触るとき: ホバープレビューが消えない/早く消える問題を調べるとき。
- 呼び出し先: `this.previewPanel?.deactivate()`
- 参照: `event.target`

## MozTabbrowserTabs.on_TabNoteIconHoverStart()
- 位置: L319-328
- 役割: タブのメモアイコンにホバーしたとき、メモ用のプレビューパネルを開始する。
- 触るとき: メモアイコンのホバー表示を変更・調査するとき。
- 呼び出し先: `this.ensureTabPreviewPanelLoaded()`, `this.previewPanel.activateNotePanel()`
- 参照: `event.detail.noteIconElement`, `event.target`, `this._showTabHoverPreview`

## MozTabbrowserTabs.on_TabNoteIconHoverEnd()
- 位置: L330-335
- 役割: メモアイコンのホバー終了でメモパネルを閉じ、タブに戻る場合は通常のプレビューを再開する。
- 触るとき: メモパネルとタブプレビューの切り替わりを調べるとき。
- 呼び出し先: `this.previewPanel?.deactivateNotePanel()`
- 条件付き依存: `if (event.detail.returningToTab)` → `this.previewPanel?.activate()`
- 参照: `event.detail.returningToTab`, `event.target`

## MozTabbrowserTabs.cancelTabGroupPreview()
- 位置: L337-339
- 役割: タブグループのプレビュー表示待ちを取り消す。
- 触るとき: グループのプレビューが意図せず開く/閉じるときの調査。
- 呼び出し先: `this.previewPanel?.panelOpener.clear()`

## MozTabbrowserTabs.showTabGroupPreview()
- 位置: L341-347
- 役割: グループのホバープレビューが有効なら、そのグループのプレビューを開く。
- 触るとき: タブグループのプレビュー表示条件を変えるとき。
- 呼び出し先: `this.ensureTabPreviewPanelLoaded()`, `this.previewPanel.activate()`
- 参照: `this._showTabGroupHoverPreview`

## MozTabbrowserTabs.on_TabGroupLabelHoverStart()
- 位置: L349-351
- 役割: グループラベルへのホバー開始時にそのグループのプレビューを表示する。
- 触るとき: グループラベルにホバーしたときの挙動を変えるとき。
- 呼び出し先: `this.showTabGroupPreview()`
- 参照: `event.target.group`

## MozTabbrowserTabs.on_TabGroupLabelHoverEnd()
- 位置: L353-355
- 役割: グループラベルからホバーが外れたときにグループのプレビューを止める。
- 触るとき: グループのプレビューが残る問題を調べるとき。
- 呼び出し先: `this.previewPanel?.deactivate()`
- 参照: `event.target.group`

## MozTabbrowserTabs.on_TabGroupExpand()
- 位置: L357-360
- 役割: グループ展開時に可視タブのキャッシュを破棄し、そのグループをアニメーション中として記録する。
- 触るとき: グループ展開時のスクロールやオーバーフロー判定の問題を調べるとき。
- 呼び出し先: `this.#animatingGroups.add()`, `this._invalidateCachedVisibleTabs()`
- 参照: `event.target.id`

## MozTabbrowserTabs.on_TabGroupCollapse()
- 位置: L362-366
- 役割: グループ折りたたみ時に可視タブのキャッシュ破棄、タブ幅ロック解除、アニメーション中の記録を行う。
- 触るとき: グループ折りたたみ時のタブ幅やスクロールの挙動を調べるとき。
- 呼び出し先: `this.#animatingGroups.add()`, `this._invalidateCachedVisibleTabs()`, `this._unlockTabSizing()`
- 参照: `event.target.id`

## MozTabbrowserTabs.on_TabGroupAnimationComplete()
- 位置: L368-374
- 役割: グループのアニメーション完了後、次のフレームでアニメーション中の記録を消す。
- 触るとき: アニメーション直後のオーバーフロー処理の順序を調べるとき。
- 呼び出し先: `this.#animatingGroups.delete()`, `window.requestAnimationFrame()`
- 参照: `event.target.id`

## MozTabbrowserTabs.on_TabGroupCreate()
- 位置: L376-378
- 役割: グループ作成時にタブ一覧のキャッシュを破棄する。
- 触るとき: グループ作成後にタブ一覧が古いままになる問題を調べるとき。
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_TabGroupRemoved()
- 位置: L380-382
- 役割: グループ削除時にタブ一覧のキャッシュを破棄する。
- 触るとき: グループ削除後にタブ一覧が古いままになる問題を調べるとき。
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_SplitViewCreated()
- 位置: L384-386
- 役割: 分割表示の作成時にタブ一覧のキャッシュを破棄する。
- 触るとき: 分割表示作成後のタブ一覧の不整合を調べるとき。
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_SplitViewRemoved()
- 位置: L388-390
- 役割: 分割表示の解除時にタブ一覧のキャッシュを破棄する。
- 触るとき: 分割表示解除後のタブ一覧の不整合を調べるとき。
- 呼び出し先: `this._invalidateCachedTabs()`

## MozTabbrowserTabs.on_transitionend()
- 位置: L395-418
- 役割: タブの max-width トランジション終了時に、開くアニメーションの完了処理または閉じるタブの削除完了を行い、TabAnimationEnd を発火する。
- 触るとき: タブの開閉アニメーション完了後の処理や TabAnimationEnd の発火を調べるとき。
- 呼び出し先: `event.target?.closest()`, `tab.dispatchEvent()`, `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("fadein"))` → `this.openAnimationFinished()`
- 条件付き依存: `if (this.openAnimationFinished(tab))` → `this._updateCloseButtons()`
- 条件付き依存: `if (!(this.openAnimationFinished(tab)))` → `this._handleNewTab()`
- 条件付き依存: `if (tab.closing)` → `gBrowser._endRemoveTab()`
- 参照: `event.propertyName`, `tab.closing`

## MozTabbrowserTabs.on_dblclick()
- 位置: L420-443
- 役割: タブ列の空き領域をダブルクリックしたとき、条件を満たせば新しいタブを開く。
- 触るとき: タブバーのダブルクリックで新規タブが開く条件を変えるとき。
- 呼び出し先: `event.preventDefault()`
- 条件付き依存: `if (!this._blockDblClick)` → `BrowserCommands.openTab()`
- 参照: `CustomTitlebar.enabled`, `event.button`, `event.composedTarget.localName`, `event.target`, `this._blockDblClick`, `this.arrowScrollbox`, `this.verticalMode`

## MozTabbrowserTabs.on_click()
- 位置: L445-550
- 役割: 閉じるボタンの連続クリックの誤作動防止と、中クリックでのタブ/グループ閉じ・空き領域での新規タブを処理する。
- 触るとき: タブの中クリック動作や閉じるボタンのダブルクリック対策を調べるとき。
- 条件付き依存: `if (event.eventPhase == Event.CAPTURING_PHASE && event.button == 0)` → `target.classList.contains()`
- 条件付き依存: `if (event.detail > 1 && !target._ignoredCloseButtonClicks)` → `event.stopPropagation()`
- 条件付き依存: `if (event.eventPhase == Event.BUBBLING_PHASE && event.button == 1)` → `event.target?.closest()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (tab.multiselected)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(tab.multiselected))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(tab.multiselected))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(tab))` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(event.target))` → `event.target.group.saveAndClose()`
- 条件付き依存: `if (!(isTabGroupLabel(event.target)))` → `event.originalTarget.closest()`
- 条件付き依存: `if (!(isTabGroupLabel(event.target)))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( event.originalTarget.closest("scrollbox") && !Services.prefs.getBoolPref( "widget.gtk.titlebar-action-middle-click-enabled" ) )` → `visibleTabs.at()`
- 条件付き依存: `if ( event.originalTarget.closest("scrollbox") && !Services.prefs.getBoolPref( "widget.gtk.titlebar-action-middle-click-enabled" ) )` → `winUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if ( (this.verticalMode && event.clientY > endOfTab) || (!this.verticalMode && (this.#rtlMode ? event.clientX < endOfTab : event.clientX > endOfTab)) )` → `BrowserCommands.openTab()`
- 条件付き依存: `if (event.eventPhase == Event.BUBBLING_PHASE && event.button == 1)` → `event.preventDefault()`
- 条件付き依存: `if (event.eventPhase == Event.BUBBLING_PHASE && event.button == 1)` → `event.stopPropagation()`
- 参照: `Event.BUBBLING_PHASE`, `Event.CAPTURING_PHASE`, `event.button`, `event.clientX`, `event.clientY`, `event.detail`, `event.eventPhase`, `event.originalTarget`, `event.target`, `gBrowser.TabMetrics.METRIC_SOURCE.MIDDLE_CLICK`, `tab.multiselected`, `target._ignoredCloseButtonClicks`, `this.#rtlMode`, `this._blockDblClick`, `this._clickedTabBarOnce`, `this.verticalMode`, `this.visibleTabs`, `window.windowUtils`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs.on_keydown()
- 位置: L552-665
- 役割: キー操作に応じて、グループラベルの操作、タブの移動、フォーカス移動、複数選択の切り替えを行う。
- 触るとき: タブ列のキーボードショートカットやフォーカス移動を変えるとき。
- 条件付き依存: `if (keyComboForFocusedElement)` → `isTabGroupLabel()`
- 条件付き依存: `if (isTabGroupLabel(ariaFocusedItem))` → `ariaFocusedItem.click()`
- 条件付き依存: `if (isTabGroupLabel(ariaFocusedItem))` → `event.preventDefault()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabBackward()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabForward()`
- 条件付き依存: `if (RTL_UI)` → `gBrowser.moveTabBackward()`
- 条件付き依存: `if (!(RTL_UI))` → `gBrowser.moveTabForward()`
- 条件付き依存: `if (RTL_UI)` → `gBrowser.moveTabForward()`
- 条件付き依存: `if (!(RTL_UI))` → `gBrowser.moveTabBackward()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabToStart()`
- 条件付き依存: `if (keyComboForMove)` → `gBrowser.moveTabToEnd()`
- 条件付き依存: `if (keyComboForMove)` → `event.preventDefault()`
- 条件付き依存: `if (keyComboForFocus)` → `this.#advanceFocus()`
- 条件付き依存: `if (RTL_UI)` → `this.#advanceFocus()`
- 条件付き依存: `if (!(RTL_UI))` → `this.#advanceFocus()`
- 条件付き依存: `if (keyComboForFocus)` → `this.ariaFocusableItems.at()`
- 条件付き依存: `if (keyComboForFocus)` → `isTab()`
- 条件付き依存: `if (ariaFocusedItem.multiselected)` → `gBrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (!(ariaFocusedItem.multiselected))` → `gBrowser.addToMultiSelectedTabs()`
- 条件付き依存: `if (keyComboForFocus)` → `event.preventDefault()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_END`, `KeyEvent.DOM_VK_HOME`, `KeyEvent.DOM_VK_LEFT`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_RIGHT`, `KeyEvent.DOM_VK_SPACE`, `KeyEvent.DOM_VK_UP`, `ariaFocusedItem.multiselected`, `event.ctrlKey`, `event.keyCode`, `event.metaKey`, `gBrowser.TabMetrics.METRIC_SOURCE.KEYBOARD`, `this.ariaFocusedItem`

## MozTabbrowserTabs.on_focusin()
- 位置: L670-691
- 役割: 選択中タブにフォーカスが入ったときフォーカス状態を立て、グループラベルならプレビューを出す。
- 触るとき: タブ列のキーボードフォーカスの初期位置やプレビュー表示を調べるとき。
- 呼び出し先: `event.relatedTarget?.classList.contains()`, `isTabGroupLabel()`
- 条件付き依存: `if ( !focusReturnedFromGroupPanel && this.tablistHasFocus && isTabGroupLabel(this.ariaFocusedItem) )` → `this.showTabGroupPreview()`
- 参照: `event.target`, `this.ariaFocusedItem`, `this.ariaFocusedItem.group`, `this.selectedItem`, `this.tablistHasFocus`

## MozTabbrowserTabs.on_focusout()
- 位置: L696-701
- 役割: フォーカスが外れたときグループのプレビューを取り消し、選択中タブならフォーカス状態を解除する。
- 触るとき: フォーカスが外れた後の状態が残る問題を調べるとき。
- 呼び出し先: `this.cancelTabGroupPreview()`
- 参照: `event.target`, `this.selectedItem`, `this.tablistHasFocus`

## MozTabbrowserTabs.on_keypress()
- 位置: L703-711
- 役割: 未処理のスペースまたは Enter キーを、対象要素のクリックとして扱う。
- 触るとき: 新規タブボタンのキーボード操作を調べるとき。
- 条件付き依存: `if (event.key == " " || event.key == "Enter")` → `event.preventDefault()`
- 条件付き依存: `if (event.key == " " || event.key == "Enter")` → `event.target.click()`
- 参照: `event.defaultPrevented`, `event.key`

## MozTabbrowserTabs.on_dragstart()
- 位置: L713-715
- 役割: dragstart をタブのドラッグ処理に渡す。
- 触るとき: ドラッグ開始時の処理を追うとき(実体は TabDragAndDrop)。
- 呼び出し先: `this.tabDragAndDrop.handle_dragstart()`

## MozTabbrowserTabs.on_dragover()
- 位置: L717-719
- 役割: dragover をタブのドラッグ処理に渡す。
- 触るとき: ドラッグ中の挙動を追うとき(実体は TabDragAndDrop)。
- 呼び出し先: `this.tabDragAndDrop.handle_dragover()`

## MozTabbrowserTabs.on_drop()
- 位置: L721-723
- 役割: drop をタブのドラッグ処理に渡す。
- 触るとき: ドロップ時の挙動を追うとき(実体は TabDragAndDrop)。
- 呼び出し先: `this.tabDragAndDrop.handle_drop()`

## MozTabbrowserTabs.on_dragend()
- 位置: L725-727
- 役割: dragend をタブのドラッグ処理に渡す。
- 触るとき: ドラッグ終了時の後始末を追うとき(実体は TabDragAndDrop)。
- 呼び出し先: `this.tabDragAndDrop.handle_dragend()`

## MozTabbrowserTabs.on_dragleave()
- 位置: L729-731
- 役割: dragleave をタブのドラッグ処理に渡す。
- 触るとき: ドラッグがタブ列から出たときの挙動を追うとき(実体は TabDragAndDrop)。
- 呼び出し先: `this.tabDragAndDrop.handle_dragleave()`

## MozTabbrowserTabs.on_wheel()
- 位置: L737-741
- 役割: スクロールでタブを切り替える設定のとき、スクロールボックス自体のスクロールを止める。
- 触るとき: ホイールでのタブ切替とスクロールの競合を調べるとき。
- 呼び出し先: `event.stopImmediatePropagation()`

## MozTabbrowserTabs.updateWheelListeners()
- 位置: L743-755
- 役割: スクロールでのタブ切替設定に応じて、スクロールボックスのホイールリスナーを付け外しする。
- 触るとき: ホイールでのタブ切替設定の反映を調べるとき。
- 呼び出し先: `super.updateWheelListeners()`
- 条件付き依存: `if (this.switchByScrolling)` → `this.arrowScrollbox.addEventListener()`
- 条件付き依存: `if (!(this.switchByScrolling))` → `this.arrowScrollbox.removeEventListener()`
- 参照: `this.arrowScrollbox`, `this.switchByScrolling`

## MozTabbrowserTabs.on_overflow()
- 位置: L757-773
- 役割: タブがあふれたとき overflow 属性を付け、閉じるボタンと選択タブの位置を更新する。
- 触るとき: タブがあふれたときの表示やスクロールの挙動を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("tab-preview-panel") ?.setAttribute()`, `this._updateCloseButtons()`, `this.toggleAttribute()`
- 条件付き依存: `if (!this.#animatingGroups.size)` → `this._handleTabSelect()`
- 参照: `event.target`, `this.#animatingGroups.size`, `this.arrowScrollbox`

## MozTabbrowserTabs.on_underflow()
- 位置: L775-798
- 役割: あふれが解消したとき overflow 属性を外し、閉じ途中のタブを削除して閉じるボタンを更新する。
- 触るとき: タブの数が減ってあふれが解消したときの挙動を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("tab-preview-panel") ?.removeAttribute()`, `gBrowser.removeTab()`, `this._updateCloseButtons()`, `this.removeAttribute()`
- 条件付き依存: `if (this._lastTabClosedByMouse)` → `this._expandSpacerBy()`
- 参照: `event.target`, `gBrowser._removingTabs`, `this._lastTabClosedByMouse`, `this._scrollButtonWidth`, `this.arrowScrollbox`, `this.overflowing`

## MozTabbrowserTabs.on_contextmenu()
- 位置: L800-809
- 役割: キーボードのメニューキーでグループラベルにフォーカスがある場合、グループの編集メニューを開く。
- 触るとき: グループラベルのキーボードでのコンテキストメニューを調べるとき。
- 呼び出し先: `isTabGroupLabel()`
- 条件付き依存: `if (event.button == 0 && isTabGroupLabel(this.ariaFocusedItem))` → `gBrowser.tabGroupMenu.openEditModal()`
- 条件付き依存: `if (event.button == 0 && isTabGroupLabel(this.ariaFocusedItem))` → `event.preventDefault()`
- 参照: `event.button`, `this.ariaFocusedItem`, `this.ariaFocusedItem.group`

## MozTabbrowserTabs.on_uidensitychanged()
- 位置: L811-814
- 役割: UI 密度の変更時に閉じるボタンの表示と選択タブの位置を更新する。
- 触るとき: UI 密度変更後のタブ表示の崩れを調べるとき。
- 呼び出し先: `this._handleTabSelect()`, `this._updateCloseButtons()`

## MozTabbrowserTabs.emptyTabTitle()
- 位置: L818-826
- 役割: 通常/プライベートウィンドウに応じた、空タブのタイトル文字列を返す。
- 触るとき: 新規タブの既定タイトルの表示を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `gBrowser.tabLocalization.formatValueSync()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs.tabbox()
- 位置: L828-830
- 役割: タブボックス要素を返す。
- 触るとき: タブパネル側の要素を参照する箇所を調べるとき。
- 呼び出し先: `document.getElementById()`

## MozTabbrowserTabs.newTabButton()
- 位置: L832-834
- 役割: タブ列内の新規タブボタンを返す。
- 触るとき: 新規タブボタンを参照・変更するとき。
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTabs.verticalMode()
- 位置: L836-838
- 役割: orient 属性が vertical かどうか(縦タブか)を返す。
- 触るとき: 縦タブと横タブで挙動を分ける条件を調べるとき。
- 呼び出し先: `this.getAttribute()`

## MozTabbrowserTabs.expandOnHover()
- 位置: L840-842
- 役割: サイドバーの表示設定がホバーで展開かどうかを返す。
- 触るとき: ホバー展開時のタブ列の挙動を調べるとき。
- 参照: `this._sidebarVisibility`

## MozTabbrowserTabs.#rtlMode()
- 位置: L844-846
- 役割: 横タブかつ右から左の UI かどうかを返す。
- 触るとき: RTL 表示でのクリック位置やキー方向の判定を調べるとき。
- 参照: `this.verticalMode`

## MozTabbrowserTabs.overflowing()
- 位置: L848-850
- 役割: overflow 属性があるか(タブがあふれているか)を返す。
- 触るとき: あふれ状態の判定を参照する箇所を調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.allTabs()
- 位置: L853-880
- 役割: 固定タブと通常タブ(グループや分割表示の中身も展開)を並べた全タブ配列をキャッシュ付きで返す。
- 触るとき: タブの並び順や、タブ一覧の取得結果がおかしいときに見る。
- 呼び出し先: `Array.from()`, `pinnedChildren?.at()`, `unpinnedChildren.pop()`
- 条件付き依存: `if (pinnedChildren?.at(-1)?.id == "pinned-tabs-container-periphery")` → `pinnedChildren.pop()`
- 条件付き依存: `if ( unpinnedChildren[i].tagName == "tab-group" || unpinnedChildren[i].tagName == "tab-split-view-wrapper" )` → `unpinnedChildren.splice()`
- 参照: `pinnedChildren?.at(-1)?.id`, `this.#allTabs`, `this.arrowScrollbox.children`, `this.pinnedTabsContainer.children`, `unpinnedChildren.length`, `unpinnedChildren[i].tabs`, `unpinnedChildren[i].tagName`

## MozTabbrowserTabs.allGroups()
- 位置: L882-887
- 役割: スクロールボックス直下のタブグループ要素を返す。
- 触るとき: グループ一覧の取得を調べるとき。
- 呼び出し先: `Array.from()`, `children.filter()`
- 参照: `node.tagName`, `this.arrowScrollbox.children`

## MozTabbrowserTabs.allSplitViews()
- 位置: L889-904
- 役割: 直下とグループ内にある分割表示ラッパーを集めて返す。
- 触るとき: 分割表示の一覧取得を調べるとき。
- 呼び出し先: `Array.from()`
- 条件付き依存: `if (node.tagName == "tab-split-view-wrapper")` → `splitViews.push()`
- 条件付き依存: `if (node.tagName == "tab-group")` → `splitViews.push()`
- 条件付き依存: `if (node.tagName == "tab-group")` → `Array.from(node.children).filter()`
- 条件付き依存: `if (node.tagName == "tab-group")` → `Array.from()`
- 参照: `child.tagName`, `node.children`, `node.tagName`, `this.arrowScrollbox.children`

## MozTabbrowserTabs.openTabs()
- 位置: L910-915
- 役割: 閉じ途中のタブと Firefox View を除く全タブをキャッシュ付きで返す。
- 触るとき: 開いているタブの集合の定義を調べるとき。
- 条件付き依存: `if (!this.#openTabs)` → `this.allTabs.filter()`
- 参照: `tab.isOpen`, `this.#openTabs`

## MozTabbrowserTabs.nonHiddenTabs()
- 位置: L921-926
- 役割: openTabs から隠しタブを除いたものをキャッシュ付きで返す。
- 触るとき: 隠しタブを除いた一覧の定義を調べるとき。
- 条件付き依存: `if (!this.#nonHiddenTabs)` → `this.openTabs.filter()`
- 参照: `tab.hidden`, `this.#nonHiddenTabs`

## MozTabbrowserTabs.visibleTabs()
- 位置: L932-937
- 役割: 隠しタブと折りたたみグループ内のタブを除いた可視タブをキャッシュ付きで返す。
- 触るとき: 可視タブの定義や、キャッシュが古くなる問題を調べるとき。
- 条件付き依存: `if (!this.#visibleTabs)` → `this.openTabs.filter()`
- 参照: `tab.visible`, `this.#visibleTabs`

## MozTabbrowserTabs.tablistHasFocus()
- 位置: L943-945
- 役割: タブ列(選択タブ)にキーボードフォーカスがあるかを属性から返す。
- 触るとき: フォーカス状態の判定を参照する箇所を調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.tablistHasFocus()
- 位置: L950-952
- 役割: タブ列にフォーカスがあるかを属性として設定する。
- 触るとき: フォーカス状態の更新箇所を調べるとき。
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTabs.ariaFocusableItems()
- 位置: L970-1001
- 役割: キーボードフォーカスの対象になるタブとグループラベルを表示順にキャッシュ付きで返す。
- 触るとき: タブ列のフォーカス順やキーボード操作の対象を変えるとき。
- 呼び出し先: `Array.from()`, `isTab()`
- 条件付き依存: `if (isTab(child))` → `focusableItems.push()`
- 条件付き依存: `if (isTab(child) && child.visible)` → `focusableItems.push()`
- 条件付き依存: `if (!(isTab(child) && child.visible))` → `isTabGroup()`
- 条件付き依存: `if (isTabGroup(child))` → `focusableItems.push()`
- 条件付き依存: `if (isTabGroup(child))` → `child.tabs.filter()`
- 条件付き依存: `if (child.tagName == "tab-split-view-wrapper")` → `child.tabs.filter()`
- 条件付き依存: `if (child.tagName == "tab-split-view-wrapper")` → `focusableItems.push()`
- 参照: `child.labelElement`, `child.tagName`, `child.visible`, `tab.visible`, `this.#focusableItems`, `this.arrowScrollbox.children`, `this.pinnedTabsContainer.children`

## MozTabbrowserTabs.dragAndDropElements()
- 位置: L1010-1051
- 役割: ドラッグ対象のタブ・グループラベル・分割表示を順に並べ、各要素の番号を振って返す。
- 触るとき: ドラッグ&ドロップの対象要素や並び番号を調べるとき。
- 呼び出し先: `Array.from()`, `isSplitViewWrapper()`, `isTab()`, `isTabGroup()`
- 条件付き依存: `if (isTabGroup(child))` → `dragAndDropElements.push()`
- 条件付き依存: `if (isTabGroup(child))` → `child.tabsAndSplitViews.filter()`
- 条件付き依存: `if (isTabGroup(child))` → `tabsAndSplitViews.forEach()`
- 条件付き依存: `if (!(isTabGroup(child)))` → `dragAndDropElements.push()`
- 参照: `child.elementIndex`, `child.labelElement`, `child.labelElement.elementIndex`, `child.visible`, `ele.elementIndex`, `node.visible`, `this.#dragAndDropElements`, `this.arrowScrollbox.children`, `this.pinnedTabsContainer.children`

## MozTabbrowserTabs.#advanceFocus()
- 位置: L1059-1077
- 役割: ARIA フォーカスを前後の項目へ移し、端で止め、グループラベルならプレビューを出す。
- 触るとき: Ctrl+矢印でのフォーカス移動の端の挙動を調べるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `isTabGroupLabel()`, `this.ariaFocusableItems.indexOf()`
- 条件付き依存: `if (isTabGroupLabel(this.ariaFocusedItem))` → `this.showTabGroupPreview()`
- 参照: `this.ariaFocusableItems`, `this.ariaFocusableItems.length`, `this.ariaFocusedItem`, `this.ariaFocusedItem.group`

## MozTabbrowserTabs._invalidateCachedTabs()
- 位置: L1079-1082
- 役割: 全タブのキャッシュと可視タブ系のキャッシュを破棄する。
- 触るとき: タブ構成の変更後に古い一覧が残る問題を調べるとき。
- 呼び出し先: `this._invalidateCachedVisibleTabs()`
- 参照: `this.#allTabs`

## MozTabbrowserTabs._invalidateCachedVisibleTabs()
- 位置: L1084-1093
- 役割: 開いている/非表示でない/可視タブ、フォーカス対象、ドラッグ対象のキャッシュを破棄する。
- 触るとき: 可視性が変わった後の一覧の不整合を調べるとき。
- 参照: `this.#dragAndDropElements`, `this.#focusableItems`, `this.#nonHiddenTabs`, `this.#openTabs`, `this.#visibleTabs`

## MozTabbrowserTabs.#isMovingTab()
- 位置: L1095-1097
- 役割: movingtab 属性があるか(タブ移動中か)を返す。
- 触るとき: タブ移動中の状態判定を調べるとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabs.isContainerVerticalPinnedGrid()
- 位置: L1099-1106
- 役割: 固定タブが縦タブの展開時グリッド表示の中にあるかを返す。
- 触るとき: 縦タブでの固定タブのグリッド表示条件を調べるとき。
- 呼び出し先: `this.hasAttribute()`
- 参照: `tab.pinned`, `this.expandOnHover`, `this.verticalMode`

## MozTabbrowserTabs.advanceSelectedTab()
- 位置: L1114-1125
- 役割: 基底クラスの処理で選択タブを前後に進め、変わった場合はタブ操作の計測を記録する。
- 触るとき: キーボードショートカットでのタブ切替と、その計測記録を調べるとき。
- 呼び出し先: `super.advanceSelectedTab()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.sourceForEvent()`
- 参照: `gBrowser.TabMetrics.METRIC_ACTION.ACTIVATE`, `gBrowser.selectedTab`

## MozTabbrowserTabs.advanceSelectedItem()
- 位置: L1138-1201
- 役割: 矢印キー操作で選択タブまたはグループラベルを前後に移し、グループのパネルが開いていればそこへフォーカスを渡す。
- 触るとき: タブ列を矢印キーでたどる挙動や端での折り返しを変えるとき。
- 呼び出し先: `ariaFocusableItems.indexOf()`, `isTab()`, `isTabGroupLabel()`, `this.cancelTabGroupPreview()`
- 条件付き依存: `if (groupPanel && groupPanel.isActive)` → `groupPanel.focusPanel()`
- 条件付き依存: `if (!(aWrap))` → `Math.min()`
- 条件付き依存: `if (!(aWrap))` → `Math.max()`
- 条件付き依存: `if (isTab(newItem))` → `this._selectNewTab()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (isTabGroupLabel(this.ariaFocusedItem))` → `this.showTabGroupPreview()`
- 参照: `ariaFocusableItems.length`, `gBrowser.TabMetrics.METRIC_ACTION.ACTIVATE`, `gBrowser.TabMetrics.METRIC_SOURCE.KEYBOARD`, `gBrowser.selectedTab`, `groupPanel.isActive`, `this.ariaFocusedItem`, `this.ariaFocusedItem.group`, `this.previewPanel?.tabGroupPanel`, `this.selectedItem`

## MozTabbrowserTabs.ensureTabPreviewPanelLoaded()
- 位置: L1203-1210
- 役割: タブのホバープレビュー用モジュールを初回だけ読み込み、パネルを作る。
- 触るとき: プレビューパネルの遅延読み込みを調べるとき。
- 条件付き依存: `if (!this.previewPanel)` → `ChromeUtils.importESModule()`
- 参照: `ChromeUtils.importESModule( "chrome://browser/content/tabbrowser/tab-hover-preview.mjs" ).default`, `this.previewPanel`

## MozTabbrowserTabs.appendChild()
- 位置: L1212-1214
- 役割: 末尾の挿入として insertBefore(tab, null) を呼ぶ。
- 触るとき: タブ要素を末尾に追加する経路を調べるとき。
- 呼び出し先: `this.insertBefore()`

## MozTabbrowserTabs.insertBefore()
- 位置: L1216-1227
- 役割: 指定ノードの前(未指定なら末尾の周辺要素の前)にタブを挿入する。
- 触るとき: タブ要素の挿入位置を調べるとき。
- 呼び出し先: `node.before()`
- 参照: `this.arrowScrollbox`, `this.arrowScrollbox.lastChild`

## MozTabbrowserTabs.#updateTabMinWidth()
- 位置: L1229-1234
- 役割: タブ最小幅の設定値を CSS 変数 --tab-min-width-pref に反映する。
- 触るとき: タブの最小幅の設定が見た目に反映される経路を調べるとき。
- 呼び出し先: `this.style.setProperty()`
- 参照: `this._tabMinWidthPref`

## MozTabbrowserTabs._isCustomizing()
- 位置: L1236-1238
- 役割: ツールバーのカスタマイズモード中かどうかを返す。
- 触るとき: カスタマイズモード中のタブ列の挙動を調べるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`

## MozTabbrowserTabs._selectNewTab()
- 位置: L1243-1247
- 役割: 画面共有の警告を出す場合を除き、基底クラスの新規タブ選択を呼ぶ。
- 触るとき: 画面共有中にキーボードでタブを切り替えたときの警告を調べるとき。
- 呼び出し先: `gSharedTabWarning.willShowSharedTabWarning()`
- 条件付き依存: `if (!gSharedTabWarning.willShowSharedTabWarning(aNewTab))` → `super._selectNewTab()`

## MozTabbrowserTabs.observe()
- 位置: L1249-1320
- 役割: コンテナ関連プリファレンスの変更時に、各新規タブボタンのコンテナメニュー、ツールチップ、長押し設定を作り直す。
- 触るとき: 新規タブボタンのコンテナ選択メニューやツールチップを変えるとき。
- 呼び出し先: `DynamicShortcutTooltip.cache.delete()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `button.removeAttribute()`, `document.getElementById()`
- 条件付き依存: `if (button.menupopup)` → `button.menupopup.remove()`
- 条件付き依存: `if (containersEnabled)` → `button.setAttribute()`
- 条件付き依存: `if (containersEnabled)` → `document .getElementById("new-tab-button-popup") .cloneNode()`
- 条件付き依存: `if (containersEnabled)` → `document .getElementById()`
- 条件付き依存: `if (containersEnabled)` → `popup.removeAttribute()`
- 条件付き依存: `if (containersEnabled)` → `popup.setAttribute()`
- 条件付き依存: `if (containersEnabled)` → `popup.addEventListener()`
- 条件付き依存: `if (containersEnabled)` → `button.prepend()`
- 条件付き依存: `if (!(containersEnabled))` → `button.removeAttribute()`
- 条件付き依存: `if (containersEnabled && !newTabLeftClickOpensContainersMenu)` → `gClickAndHoldListenersOnElement.add()`
- 条件付き依存: `if (!(containersEnabled && !newTabLeftClickOpensContainersMenu))` → `gClickAndHoldListenersOnElement.remove()`
- 参照: `DynamicShortcutTooltip.nodeToTooltipMap`, `button.id`, `button.menupopup`, `popup.className`, `this.newTabButton`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs._updateCloseButtons()
- 位置: L1322-1365
- 役割: タブ幅としきい値を見て、閉じるボタンを選択タブだけに出すか全タブに出すかを属性で切り替える。
- 触るとき: タブの閉じるボタンの表示条件を変えるとき。
- 呼び出し先: `rect()`, `this.visibleTabs .slice()`, `this.visibleTabs .slice(gBrowser.pinnedTabCount) .find()`, `window.requestAnimationFrame()`
- 条件付き依存: `if (this.overflowing)` → `this.setAttribute()`
- 条件付き依存: `if (tab && rect(tab).width <= this._tabClipWidth)` → `this.setAttribute()`
- 条件付き依存: `if (!(tab && rect(tab).width <= this._tabClipWidth))` → `this.removeAttribute()`
- 参照: `gBrowser.pinnedTabCount`, `rect(tab).width`, `t.splitview`, `this._closeButtonsUpdatePending`, `this._tabClipWidth`, `this.overflowing`

## rect()
- 位置: L1350-1352
- 役割: 要素の領域をレイアウト再計算なしで取得する補助関数。
- 触るとき: 閉じるボタン判定でのサイズ取得を調べるとき。
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## MozTabbrowserTabs._handleTabSelect()
- 位置: L1370-1375
- 役割: 選択タブがスクロールで見えるようにし、選択済みフラグを更新する。
- 触るとき: タブ選択後のスクロール追従を調べるとき。
- 呼び出し先: `this.#ensureTabIsVisible()`
- 参照: `selectedTab._notselectedsinceload`, `this.selectedItem`

## MozTabbrowserTabs.#ensureTabIsVisible()
- 位置: L1381-1386
- 役割: タブがあふれ中のスクロールボックスにある場合、そのタブが見えるようスクロールする。
- 触るとき: 選択・新規タブが画面外に隠れる問題を調べるとき。
- 呼び出し先: `tab.closest()`
- 条件付き依存: `if (arrowScrollbox?.overflowing)` → `arrowScrollbox.ensureElementIsVisible()`
- 参照: `arrowScrollbox?.overflowing`

## MozTabbrowserTabs._lockTabSizing()
- 位置: L1391-1477
- 役割: タブを閉じた直後にマウス位置の閉じるボタンが動かないよう、タブ幅を固定するか余白を広げる。
- 触るとき: 連続でタブを閉じるときのタブ幅の固定や余白の挙動を変えるとき。
- 呼び出し先: `tabs.at()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!this._tabDefaultMaxWidth)` → `parseFloat()`
- 条件付き依存: `if (!this._tabDefaultMaxWidth)` → `window.getComputedStyle()`
- 条件付き依存: `if (aTabWidth === undefined)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this.overflowing)` → `this.arrowScrollbox.hasAttribute()`
- 条件付き依存: `if (this.overflowing)` → `this._expandSpacerBy()`
- 条件付き依存: `if (!(this.overflowing))` → `tab.style.setProperty()`
- 条件付き依存: `if (!isEndTab)` → `tabsToReset.push()`
- 条件付き依存: `if (tabsToReset.length)` → `window .promiseDocumentFlushed(() => {}) .then()`
- 条件付き依存: `if (tabsToReset.length)` → `window .promiseDocumentFlushed()`
- 条件付き依存: `if (tabsToReset.length)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (!(this.overflowing))` → `gBrowser.addEventListener()`
- 条件付き依存: `if (!(this.overflowing))` → `window.addEventListener()`
- 参照: `aClosingTab.index`, `aClosingTab?.owner`, `gBrowser.pinnedTabCount`, `tab.animationsEnabled`, `tabs.at(-1).index`, `tabs.length`, `tabsToReset.length`, `this._hasTabTempMaxWidth`, `this._lastTabClosedByMouse`, `this._scrollButtonWidth`, `this._tabDefaultMaxWidth`, `this.arrowScrollbox._scrollButtonDown`, `this.overflowing`, `this.verticalMode`, `this.visibleTabs`, `window.getComputedStyle(tabs[numPinned]).maxWidth`, `window.windowUtils.getBoundsWithoutFlushing( tabs[numPinned] ).width`, `window.windowUtils.getBoundsWithoutFlushing( this.arrowScrollbox._scrollButtonDown ).width`

## MozTabbrowserTabs._expandSpacerBy()
- 位置: L1479-1485
- 役割: 閉じ中タブ用スペーサーの幅を指定ピクセル分広げ、マウス移動の監視を始める。
- 触るとき: あふれ中にタブを閉じたときの余白の挙動を調べるとき。
- 呼び出し先: `gBrowser.addEventListener()`, `parseFloat()`, `this.toggleAttribute()`, `window.addEventListener()`
- 参照: `spacer.style.width`, `this._closingTabsSpacer`

## MozTabbrowserTabs._unlockTabSizing()
- 位置: L1487-1506
- 役割: 固定したタブ幅とスペーサーを元に戻し、マウス監視を解除する。
- 触るとき: タブ幅の固定が解除されない/早すぎる問題を調べるとき。
- 呼び出し先: `gBrowser.removeEventListener()`, `this.hasAttribute()`, `window.removeEventListener()`
- 条件付き依存: `if (this.hasAttribute("using-closing-tabs-spacer"))` → `this.removeAttribute()`
- 参照: `tabs.length`, `tabs[i].style.maxWidth`, `this._closingTabsSpacer.style.width`, `this._hasTabTempMaxWidth`, `this.allTabs`

## MozTabbrowserTabs._notifyBackgroundTab()
- 位置: L1508-1601
- 役割: 背景で開いたタブがあふれ中の領域外なら、必要に応じてスクロールし、強調表示を短時間付ける。
- 触るとき: 背景タブを開いたときのスクロールや強調表示を変えるとき。
- 条件付き依存: `if (!this._backgroundTabScrollPromise)` → `window .promiseDocumentFlushed()`
- 条件付き依存: `if (!this._backgroundTabScrollPromise)` → `this._lastTabToScrollIntoView.getBoundingClientRect()`
- 条件付き依存: `if (!(selectedTab.pinned))` → `selectedTab.getBoundingClientRect()`
- 条件付き依存: `if (this._lastTabToScrollIntoView != tabToScrollIntoView)` → `this._notifyBackgroundTab()`
- 条件付き依存: `if (this.arrowScrollbox.smoothScroll)` → `Math.max()`
- 条件付き依存: `if ( !selectedRect || (this.verticalMode ? Math.max( tabRect.bottom - selectedRect.top, selectedRect.bottom - tabRect.top ) <= scrollRect.height : Math.max( tabR...)` → `this.#ensureTabIsVisible()`
- 条件付き依存: `if (this.arrowScrollbox.smoothScroll)` → `this.arrowScrollbox.scrollByPixels()`
- 条件付き依存: `if (!this._backgroundTabScrollPromise)` → `this._animateElement.hasAttribute()`
- 条件付き依存: `if (!this._animateElement.hasAttribute("highlight"))` → `this._animateElement.toggleAttribute()`
- 条件付き依存: `if (!this._animateElement.hasAttribute("highlight"))` → `setTimeout()`
- 条件付き依存: `if (!this._animateElement.hasAttribute("highlight"))` → `ele.removeAttribute()`
- 参照: `aTab.pinned`, `aTab.visible`, `scrollRect.bottom`, `scrollRect.height`, `scrollRect.left`, `scrollRect.right`, `scrollRect.top`, `scrollRect.width`, `selectedRect.bottom`, `selectedRect.left`, `selectedRect.right`, `selectedRect.top`, `selectedTab.bottom`, `selectedTab.left`, `selectedTab.pinned`, `selectedTab.right`, `selectedTab.top`, `tabRect.bottom`, `tabRect.left`, `tabRect.right`, `tabRect.top`, `this.#rtlMode`, `this._animateElement`, `this._backgroundTabScrollPromise`, `this._lastTabToScrollIntoView`, `this.arrowScrollbox.scrollClientRect`, `this.arrowScrollbox.smoothScroll`, `this.overflowing`, `this.selectedItem`, `this.verticalMode`

## MozTabbrowserTabs.tabAnimationsInProgress()
- 位置: L1609-1611
- 役割: 開く途中のタブと閉じる途中のタブの合計数を返す。
- 触るとき: タブのアニメーション中かの判定を参照するとき。
- 参照: `gBrowser._removingTabs.size`, `this.#openingTabs.size`

## MozTabbrowserTabs.openAnimationFinished()
- 位置: L1619-1621
- 役割: そのタブが開くアニメーション中の集合に含まれないかを返す。
- 触るとき: タブの開くアニメーション完了判定を調べるとき。
- 呼び出し先: `this.#openingTabs.has()`

## MozTabbrowserTabs.markTabOpening()
- 位置: L1628-1630
- 役割: 新しく追加したタブを開く途中の集合に登録する。
- 触るとき: タブ追加時のアニメーション状態の管理を調べるとき。
- 呼び出し先: `this.#openingTabs.add()`

## MozTabbrowserTabs.cancelTabOpening()
- 位置: L1637-1639
- 役割: 閉じ始めたタブを開く途中の集合から外す。
- 触るとき: 開くアニメーション中にタブが閉じられた場合の扱いを調べるとき。
- 呼び出し先: `this.#openingTabs.delete()`

## MozTabbrowserTabs._handleNewTab()
- 位置: L1641-1665
- 役割: 新規タブの追加完了時に、閉じるボタン更新、選択またはスクロール通知、新規タブページの先読み、計測終了を行う。
- 触るとき: タブ追加直後の後処理や先読みのタイミングを調べるとき。
- 呼び出し先: `UserInteraction.running()`, `tab.hasAttribute()`, `this.#openingTabs.delete()`, `this._updateCloseButtons()`
- 条件付き依存: `if (tab.hasAttribute("selected"))` → `this._handleTabSelect()`
- 条件付き依存: `if (!(tab.hasAttribute("selected")))` → `tab.hasAttribute()`
- 条件付き依存: `if (!tab.hasAttribute("skipbackgroundnotify"))` → `this._notifyBackgroundTab()`
- 条件付き依存: `if (tab.linkedPanel)` → `NewTabPagePreloading.maybeCreatePreloadedBrowser()`
- 条件付き依存: `if (UserInteraction.running("browser.tabs.opening", window))` → `UserInteraction.finish()`
- 参照: `tab.container`, `tab.linkedPanel`

## MozTabbrowserTabs._canAdvanceToTab()
- 位置: L1667-1669
- 役割: 閉じ途中でないタブだけを選択移動の対象にする。
- 触るとき: キーボードでのタブ切替で飛ばす対象を調べるとき。
- 参照: `aTab.closing`

## MozTabbrowserTabs.getRelatedElement()
- 位置: L1676-1698
- 役割: タブに対応するパネル要素を返し、選択中で未接続なら browser を接続してから返す。
- 触るとき: タブとパネルの対応や遅延ブラウザーの接続タイミングを調べるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!aTab.linkedPanel)` → `gBrowser.insertBrowser()`
- 参照: `aTab.linkedPanel`, `aTab.selected`, `gBrowser._initialized`, `this.tabbox.tabpanels.firstElementChild`

## MozTabbrowserTabs._updateNewTabVisibility()
- 位置: L1700-1724
- 役割: 新規タブボタンがタブ列に隣接しているかを調べ、hasadjacentnewtabbutton 属性を切り替える。
- 触るとき: 新規タブボタンの位置とインライン表示の条件を調べるとき。
- 呼び出し先: `this.toggleAttribute()`, `unwrap()`, `wrap()`
- 参照: `sib.hidden`, `sib.id`, `wrap(sib).nextElementSibling`

## wrap()
- 位置: L1702-1703
- 役割: カスタマイズ時のパレット項目の包みがあればそれを返す補助関数。
- 触るとき: カスタマイズモードでの隣接判定を調べるとき。
- 参照: `n.parentNode`, `n.parentNode.localName`

## unwrap()
- 位置: L1704-1705
- 役割: パレット項目の包みから中の要素を取り出す補助関数。
- 触るとき: カスタマイズモードでの隣接判定を調べるとき。
- 参照: `n.firstElementChild`, `n.localName`

## MozTabbrowserTabs.onWidgetAfterDOMChange()
- 位置: L1726-1733
- 役割: タブツールバーのカスタマイズ対象で変更があったとき、新規タブボタンの隣接状態を更新する。
- 触るとき: ツールバーのカスタマイズ後に新規タブボタンの表示が崩れるとき。
- 条件付き依存: `if ( aContainer.ownerDocument == document && aContainer.id == "TabsToolbar-customization-target" )` → `this._updateNewTabVisibility()`
- 参照: `aContainer.id`, `aContainer.ownerDocument`

## MozTabbrowserTabs.onAreaNodeRegistered()
- 位置: L1735-1739
- 役割: TabsToolbar 領域の登録時に、新規タブボタンの隣接状態を更新する。
- 触るとき: ツールバー領域の登録時の新規タブボタン表示を調べるとき。
- 条件付き依存: `if (aContainer.ownerDocument == document && aArea == "TabsToolbar")` → `this._updateNewTabVisibility()`
- 参照: `aContainer.ownerDocument`

## MozTabbrowserTabs.onAreaReset()
- 位置: L1741-1743
- 役割: 領域のリセット時に onAreaNodeRegistered と同じ更新を行う。
- 触るとき: ツールバーのリセット後の新規タブボタン表示を調べるとき。
- 呼び出し先: `this.onAreaNodeRegistered()`

## MozTabbrowserTabs._hiddenSoundPlayingStatusChanged()
- 位置: L1745-1756
- 役割: 非表示で音を出しているタブの集合を更新し、hiddensoundplaying 属性を付け外しする。
- 触るとき: 隠れたタブの音再生を示す表示の条件を調べるとき。
- 条件付き依存: `if (!isClosed && tab.soundPlaying && !tab.visible)` → `this._hiddenSoundPlayingTabs.add()`
- 条件付き依存: `if (!isClosed && tab.soundPlaying && !tab.visible)` → `this.toggleAttribute()`
- 条件付き依存: `if (!(!isClosed && tab.soundPlaying && !tab.visible))` → `this._hiddenSoundPlayingTabs.delete()`
- 条件付き依存: `if (this._hiddenSoundPlayingTabs.size == 0)` → `this.removeAttribute()`
- 参照: `opts.closed`, `tab.soundPlaying`, `tab.visible`, `this._hiddenSoundPlayingTabs.size`

## MozTabbrowserTabs.destroy()
- 位置: L1758-1764
- 役割: プリファレンス監視とカスタマイズのリスナーを解除し、プレビューパネルをリセットする。
- 触るとき: 終了時の後始末やリスナーの解除漏れを調べるとき。
- 呼び出し先: `CustomizableUI.removeListener()`, `this.previewPanel?.forceReset()`
- 条件付き依存: `if (this.boundObserve)` → `Services.prefs.removeObserver()`
- 参照: `this.boundObserve`
- XPCOM: `Services.prefs`

## MozTabbrowserTabs.updateTabSoundLabel()
- 位置: L1766-1786
- 役割: タブの音声ボタンに、ミュート/解除/ブロック解除の aria-label を設定する。
- 触るとき: 音声ボタンのアクセシビリティ用ラベルを変えるとき。
- 呼び出し先: `gBrowser.tabLocalization.formatMessagesSync()`
- 条件付き依存: `if (tab.audioButton)` → `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("muted") || tab.hasAttribute("soundplaying"))` → `tab.audioButton.setAttribute()`
- 条件付き依存: `if (!(tab.hasAttribute("muted") || tab.hasAttribute("soundplaying")))` → `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("activemedia-blocked"))` → `tab.audioButton.setAttribute()`
- 参照: `mute.attributes`, `mute.attributes[0].value`, `tab.audioButton`, `tab.linkedBrowser.audioMuted`, `unblock.attributes`, `unblock.attributes[0].value`, `unmute.attributes`, `unmute.attributes[0].value`
