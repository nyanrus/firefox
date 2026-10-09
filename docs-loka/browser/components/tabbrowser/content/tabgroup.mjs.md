# browser/components/tabbrowser/content/tabgroup.mjs

source: browser/components/tabbrowser/content/tabgroup.mjs
source-hash: 98ebd520d6d3ee5e7519a3ad6ff46c1beaba185a
lines: 816

## <module>
- 役割: tab-group カスタム要素 MozTabbrowserTabGroup を定義して登録する。
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## MozTabbrowserTabGroup.constructor()
- 位置: L75-84
- 役割: ホバープレビュー有効化の pref を遅延取得するよう設定する。
- 触るとき: hoverPreview の pref 連携を変えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`

## MozTabbrowserTabGroup.inheritedAttributes()
- 位置: L86-90
- 役割: ラベル要素に text と tooltiptext を継承させる属性対応を返す。
- 触るとき: ラベルの文字やツールチップの反映元を変えるとき。

## MozTabbrowserTabGroup.connectedCallback()
- 位置: L92-161
- 役割: DOM 接続時に監視・リスナー登録と初回のみのラベル/オーバーフロー要素の初期化をし TabGroupCreate を発火する。
- 触るとき: グループ作成時の初期化や接続時のイベント登録を調べるとき。
- 呼び出し先: `Services.obs.addObserver()`, `e.preventDefault()`, `gBrowser.tabGroupMenu.openEditModal()`, `this.#labelContainerElement.addEventListener()`, `this.#labelElement.addEventListener()`, `this.#observeTabChanges()`, `this.#updateLabelAriaAttributes()`, `this.addEventListener()`, `this.appendChild()`, `this.dispatchEvent()`, `this.documentGlobal.addEventListener()`, `this.initializeAttributeInheritance()`, `this.overflowContainer.querySelector()`, `this.querySelector()`
- 参照: `gBrowser.tabContainer`, `this.#labelContainerElement`, `this.#labelElement`, `this.#labelElement.container`, `this.#labelElement.group`, `this.#labelElement.pinned`, `this.#labelElement.splitview`, `this.#overflowCountLabel`, `this.#removeObserver`, `this.#wasCreatedByAdoption`, `this._initialized`, `this.constructor.fragment`, `this.overflowContainer`, `this.resetDefaultGroupName`, `this.saveOnWindowClose`, `this.textContent`
- XPCOM: `Services.obs`

## MozTabbrowserTabGroup.resetDefaultGroupName()
- 位置: L163-167
- 役割: 既定名のキャッシュを消し、aria 属性とツールチップを更新し直す。
- 触るとき: ロケール変更時の既定名の扱いを調べるとき。
- 呼び出し先: `this.#updateLabelAriaAttributes()`, `this.#updateTooltip()`
- 参照: `this.#defaultGroupName`

## MozTabbrowserTabGroup.#removeObserver()
- 位置: L169-178
- 役割: ロケール変更の observer を一度だけ解除する。
- 触るとき: observer の解除漏れやリークを調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.#observerRemoved`, `this.resetDefaultGroupName`
- XPCOM: `Services.obs`

## MozTabbrowserTabGroup.disconnectedCallback()
- 位置: L180-186
- 役割: 接続解除時にイベントリスナー、変更監視、observer を外す。
- 触るとき: 要素が DOM から外れた際の後始末を調べるとき。
- 呼び出し先: `this.#removeObserver()`, `this.#tabChangeObserver?.disconnect()`, `this.documentGlobal.removeEventListener()`, `this.removeEventListener()`
- 参照: `this.#removeObserver`

## MozTabbrowserTabGroup.appendChild()
- 位置: L188-190
- 役割: 子ノードを末尾のオーバーフロー表示の直前に挿入する。
- 触るとき: グループへの子の追加位置がずれるとき。
- 呼び出し先: `this.insertBefore()`
- 参照: `this.overflowContainer`

## MozTabbrowserTabGroup.#observeTabChanges()
- 位置: L192-248
- 役割: 子の増減を監視し、空ならグループを削除、そうでなければ aria 番号・アクティブ状態・オーバーフロー表示を更新する。
- 触るとき: グループ内タブ増減に伴う更新や空グループの自動削除を調べるとき。
- 呼び出し先: `this.#tabChangeObserver.observe()`
- 条件付き依存: `if (!this.tabs.length)` → `this.dispatchEvent()`
- 条件付き依存: `if (!this.tabs.length)` → `this.remove()`
- 条件付き依存: `if (!this.tabs.length)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(!this.tabs.length))` → `tabs.forEach()`
- 条件付き依存: `if (!(!this.tabs.length))` → `tab.setAttribute()`
- 条件付き依存: `if (!(!this.tabs.length))` → `this.#updateOverflowLabel()`
- 条件付き依存: `if (!(!this.tabs.length))` → `this.#updateLastTabOrSplitViewAttr()`
- 条件付き依存: `if (!this.#tabChangeObserver)` → `Tabbrowser.isTab()`
- 条件付き依存: `if (Tabbrowser.isTab(addedNode))` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (!(Tabbrowser.isTab(addedNode)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(addedNode))` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (Tabbrowser.isTab(removedNode))` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (!(Tabbrowser.isTab(removedNode)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(removedNode))` → `this.#updateTabAriaHidden()`
- 参照: `addedNode.tabs`, `mutation.addedNodes`, `mutation.removedNodes`, `removedNode.tabs`, `tab.selected`, `tabs.length`, `this.#removedByAdoption`, `this.#tabChangeObserver`, `this.hasActiveTab`, `this.tabs`, `this.tabs.length`, `window.MutationObserver`
- XPCOM: `Services.obs`

## MozTabbrowserTabGroup.color()
- 位置: L250-252
- 役割: 現在のグループ色コードを返す。
- 触るとき: 色の読み出しを追うとき。
- 参照: `this.#colorCode`

## MozTabbrowserTabGroup.color()
- 位置: L257-288
- 役割: 色コードを保存し、色に対応する CSS 変数を設定して、変化時に TabGroupUpdate を発火する。
- 触るとき: グループ色の見た目や CSS 変数を変えるとき。
- 呼び出し先: `this.style.setProperty()`
- 条件付き依存: `if (diff)` → `this.dispatchEvent()`
- 参照: `this.#colorCode`

## MozTabbrowserTabGroup.defaultGroupName()
- 位置: L290-297
- 役割: 名前未設定時の既定名をローカライズ文字列から取得してキャッシュする。
- 触るとき: 無名グループの表示名を変えるとき。
- 条件付き依存: `if (!this.#defaultGroupName)` → `gBrowser.tabLocalization.formatValueSync()`
- 参照: `this.#defaultGroupName`

## MozTabbrowserTabGroup.id()
- 位置: L299-301
- 役割: id 属性を返す。
- 触るとき: グループ ID の参照を追うとき。
- 呼び出し先: `this.getAttribute()`

## MozTabbrowserTabGroup.id()
- 位置: L303-305
- 役割: id 属性を設定する。
- 触るとき: グループ ID の設定箇所を追うとき。
- 呼び出し先: `this.setAttribute()`

## MozTabbrowserTabGroup.hasActiveTab()
- 位置: L310-312
- 役割: hasactivetab 属性の有無を返す。
- 触るとき: 選択タブを含むグループかの判定を追うとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.hasActiveTab()
- 位置: L317-319
- 役割: hasactivetab 属性を切り替える。
- 触るとき: アクティブタブ属性の更新箇所を追うとき。
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTabGroup.label()
- 位置: L321-323
- 役割: グループ名を返す。
- 触るとき: 名前の読み出しを追うとき。
- 参照: `this.#label`

## MozTabbrowserTabGroup.label()
- 位置: L325-337
- 役割: グループ名を保存し、属性・aria・ツールチップを更新して、変化時に TabGroupUpdate を発火する。
- 触るとき: グループ名の変更処理や通知を調べるとき。
- 呼び出し先: `this.#updateLabelAriaAttributes()`, `this.#updateTooltip()`, `this.setAttribute()`
- 条件付き依存: `if (diff)` → `this.dispatchEvent()`
- 参照: `this.#label`

## MozTabbrowserTabGroup.name()
- 位置: L340-342
- 役割: label の別名として名前を返す。
- 触るとき: name と label の対応を確認するとき。
- 参照: `this.label`

## MozTabbrowserTabGroup.name()
- 位置: L344-346
- 役割: label の別名として名前を設定する。
- 触るとき: name と label の対応を確認するとき。
- 参照: `this.label`

## MozTabbrowserTabGroup.collapsed()
- 位置: L348-350
- 役割: collapsed 属性の有無を返す。
- 触るとき: 折りたたみ状態の判定を追うとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.collapsed()
- 位置: L352-386
- 役割: 折りたたみ状態を切り替え、aria・オーバーフロー表示を更新し、イベントとアニメーション完了通知を発火する。
- 触るとき: 折りたたみ/展開の挙動やアニメーション完了通知を調べるとき。
- 呼び出し先: `Promise.allSettled()`, `Promise.allSettled(pendingAnimationPromises).then()`, `["min-width", "max-width"].includes()`, `gBrowser.tabContainer.previewPanel?.deactivate()`, `tab .getAnimations()`, `tab .getAnimations() .filter()`, `tab .getAnimations() .filter(anim => ["min-width", "max-width"].includes(anim.transitionProperty) ) .map()`, `this.#updateLabelAriaAttributes()`, `this.#updateOverflowLabel()`, `this.#updateTabAriaHidden()`, `this.#updateTooltip()`, `this.dispatchEvent()`, `this.tabs.flatMap()`, `this.toggleAttribute()`
- 参照: `anim.finished`, `anim.transitionProperty`, `tab.style.maxWidth`, `this.collapsed`, `this.tabs`

## MozTabbrowserTabGroup.lastSeenActive()
- 位置: L389-391
- 役割: グループへの最終追加時刻と各タブの最終アクティブ時刻の最大値を返す。
- 触るとき: グループの最近使用順の判定を調べるとき。
- 呼び出し先: `Math.max()`, `this.tabs.map()`
- 参照: `t.lastSeenActive`, `this.#lastAddedTo`

## MozTabbrowserTabGroup.#updateLabelAriaAttributes()
- 位置: async L393-418
- 役割: 折りたたみ状態に応じてラベルの aria 属性と説明文を設定する。
- 触るとき: グループラベルのアクセシビリティを調べるとき。
- 呼び出し先: `gBrowser.tabLocalization.formatValue()`, `this.#labelElement?.setAttribute()`
- 条件付き依存: `if (this.collapsed)` → `this.#labelElement?.setAttribute()`
- 条件付き依存: `if (this.collapsed)` → `this.hasAttribute()`
- 条件付き依存: `if (!(this.collapsed))` → `this.#labelElement?.removeAttribute()`
- 条件付き依存: `if (!(this.collapsed))` → `this.#labelElement?.setAttribute()`
- 参照: `this.#label`, `this.collapsed`, `this.defaultGroupName`

## MozTabbrowserTabGroup.#updateTooltip()
- 位置: async L420-438
- 役割: 折りたたみ状態に応じたラベルのツールチップ文字列を設定する(ホバープレビュー有効時の折りたたみでは消す)。
- 触るとき: グループラベルのツールチップを変えるとき。
- 呼び出し先: `gBrowser.tabLocalization .formatValue()`, `gBrowser.tabLocalization .formatValue(tooltipKey, { tabGroupName, }) .then()`
- 参照: `this.#label`, `this._showTabGroupHoverPreview`, `this.collapsed`, `this.dataset.tooltip`, `this.defaultGroupName`

## MozTabbrowserTabGroup.#updateTabAriaHidden()
- 位置: L443-458
- 役割: 折りたたまれたグループ内の非選択タブ/分割ビューに aria-hidden を付け外しする。
- 触るとき: 折りたたみ時にスクリーンリーダーから隠れるタブを調べるとき。
- 条件付き依存: `if (tab.splitview)` → `tab.splitview.tabs.some()`
- 条件付き依存: `if ( tab.group?.collapsed && !tab.splitview.tabs.some(splitViewTab => splitViewTab.selected) )` → `tab.splitview.setAttribute()`
- 条件付き依存: `if (!( tab.group?.collapsed && !tab.splitview.tabs.some(splitViewTab => splitViewTab.selected) ))` → `tab.splitview.removeAttribute()`
- 条件付き依存: `if (tab.group?.collapsed && !tab.selected)` → `tab.setAttribute()`
- 条件付き依存: `if (!(tab.group?.collapsed && !tab.selected))` → `tab.removeAttribute()`
- 参照: `splitViewTab.selected`, `tab.group?.collapsed`, `tab.selected`, `tab.splitview`

## MozTabbrowserTabGroup.#updateOverflowLabel()
- 位置: L460-489
- 役割: 折りたたみ時に表示する残りタブ数のラベルとツールチップを更新する。
- 触るとき: オーバーフロー数の表示や文言を調べるとき。
- 条件付き依存: `if (this.overflowContainer)` → `this.overflowContainer.querySelector()`
- 条件付き依存: `if (this.overflowContainer)` → `this.toggleAttribute()`
- 条件付き依存: `if (this.overflowContainer)` → `gBrowser.tabLocalization .formatValue("tab-group-overflow-count", { tabCount: tabCount - overflowOffset, }) .then()`
- 条件付き依存: `if (this.overflowContainer)` → `gBrowser.tabLocalization .formatValue()`
- 条件付き依存: `if (this.overflowContainer)` → `overflowCountLabel.setAttribute()`
- 参照: `gBrowser.selectedTab.splitview`, `overflowCountLabel.textContent`, `tabs.length`, `this.hasActiveTab`, `this.overflowContainer`, `this.tabs`

## MozTabbrowserTabGroup.#updateLastTabOrSplitViewAttr()
- 位置: L491-503
- 役割: グループ末尾のタブまたは分割ビューに last-tab-or-split-view 属性を付け替える。
- 触るとき: グループ末尾要素のスタイルがおかしいとき。
- 呼び出し先: `this.querySelector()`
- 条件付き依存: `if (prevLastTabOrSplitView !== currentLastTabOrSplitView)` → `prevLastTabOrSplitView?.removeAttribute()`
- 条件付き依存: `if (prevLastTabOrSplitView !== currentLastTabOrSplitView)` → `currentLastTabOrSplitView.setAttribute()`
- 参照: `lastTab.splitview`, `this.tabs`, `this.tabs.length`

## MozTabbrowserTabGroup.pinned()
- 位置: L511-513
- 役割: 常に false を返し、タブや分割ビューと同じ形で扱えるようにする。
- 触るとき: タブ/グループ共通処理での pinned の扱いを調べるとき。

## MozTabbrowserTabGroup.splitview()
- 位置: L518-520
- 役割: 常に null を返す。
- 触るとき: タブ/グループ共通処理での splitview の扱いを調べるとき。

## MozTabbrowserTabGroup.group()
- 位置: L525-527
- 役割: 常に null を返す。
- 触るとき: タブ/グループ共通処理での group の扱いを調べるとき。

## MozTabbrowserTabGroup.tabs()
- 位置: L532-540
- 役割: 分割ビューを展開した、グループ内の tab 要素の配列を返す。
- 触るとき: グループ内タブの列挙結果を調べるとき。
- 呼び出し先: `Array.from()`, `childrenArray.filter()`, `node.matches()`
- 条件付き依存: `if (childrenArray[i].tagName == "tab-split-view-wrapper")` → `childrenArray.splice()`
- 参照: `childrenArray.length`, `childrenArray[i].tabs`, `childrenArray[i].tagName`, `this.children`

## MozTabbrowserTabGroup.tabsAndSplitViews()
- 位置: L545-549
- 役割: グループ直下のタブと分割ビューラッパーの配列を返す。
- 触るとき: 分割ビューを含む直下要素の列挙を調べるとき。
- 呼び出し先: `Array.from()`, `Array.from(this.children).filter()`, `node.matches()`
- 参照: `node.tagName`, `this.children`

## MozTabbrowserTabGroup.isTabVisibleInGroup()
- 位置: L555-568
- 役割: ドラッグ中や折りたたみ中の非選択タブを除き、タブがグループ内で見えるかを返す。
- 触るとき: タブの可視判定が合わないとき。
- 参照: `tab.multiselected`, `tab.selected`, `tab.splitview?.hasActiveTab`, `this.collapsed`, `this.isBeingDragged`

## MozTabbrowserTabGroup.labelElement()
- 位置: L573-575
- 役割: ラベル要素を返す。
- 触るとき: ラベル要素の参照元を追うとき。
- 参照: `this.#labelElement`

## MozTabbrowserTabGroup.labelContainerElement()
- 位置: L580-582
- 役割: ラベルコンテナ要素を返す。
- 触るとき: ラベルコンテナの参照元を追うとき。
- 参照: `this.#labelContainerElement`

## MozTabbrowserTabGroup.overflowCountLabel()
- 位置: L584-586
- 役割: オーバーフロー数ラベルの要素を返す。
- 触るとき: オーバーフロー数ラベルの参照元を追うとき。
- 参照: `this.#overflowCountLabel`

## MozTabbrowserTabGroup.wasCreatedByAdoption()
- 位置: L591-593
- 役割: グループが他ウィンドウからの移動で作られたかのフラグを設定する。
- 触るとき: ウィンドウ間移動での TabGroupCreate の adopting 値を調べるとき。
- 参照: `this.#wasCreatedByAdoption`

## MozTabbrowserTabGroup.removedByAdoption()
- 位置: L602-604
- 役割: グループが閉じられず他ウィンドウへ移るためのフラグを設定する。
- 触るとき: ウィンドウ間移動での TabGroupRemoved の adopting 値を調べるとき。
- 参照: `this.#removedByAdoption`

## MozTabbrowserTabGroup.isBeingDragged()
- 位置: L609-611
- 役割: movingtabgroup 属性の有無を返す。
- 触るとき: ドラッグ中判定を追うとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.isBeingDragged()
- 位置: L616-618
- 役割: movingtabgroup 属性を切り替える。
- 触るとき: ドラッグ中属性の更新箇所を追うとき。
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTabGroup.hoverPreviewPanelActive()
- 位置: L623-625
- 役割: previewpanelactive 属性の有無を返す。
- 触るとき: ホバープレビュー表示中の判定を追うとき。
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTabGroup.hoverPreviewPanelActive()
- 位置: L630-633
- 役割: previewpanelactive 属性を切り替え、aria 属性を更新する。
- 触るとき: ホバープレビュー表示時のラベル説明を調べるとき。
- 呼び出し先: `this.#updateLabelAriaAttributes()`, `this.toggleAttribute()`

## MozTabbrowserTabGroup.addTabs()
- 位置: L642-685
- 役割: タブや分割ビューをグループへ追加し、別ウィンドウのものは取り込み、固定は解除し、メトリクスを記録する。
- 触るとき: グループへのタブ追加やウィンドウ間の取り込みを調べるとき。
- 呼び出し先: `Date.now()`, `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `tabsOrSplitViews.reduce()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (metricsContext?.isUserTriggered)` → `gBrowser.TabMetrics.decomposedContext()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabOrSplitView))` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabOrSplitView))` → `gBrowser.tabs.at()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabOrSplitView))` → `gBrowser.moveSplitViewToExistingGroup()`
- 条件付き依存: `if (tabOrSplitView.pinned)` → `tabOrSplitView.documentGlobal.gBrowser.unpinTab()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabOrSplitView)))` → `gBrowser.adoptTab()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabOrSplitView)))` → `gBrowser.tabs.at()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabOrSplitView)))` → `gBrowser.moveTabToExistingGroup()`
- 参照: `gBrowser.TabMetrics.METRIC_ACTION.MOVE`, `gBrowser.tabs.at(-1).index`, `item.tabs.length`, `metricsContext?.isUserTriggered`, `tabOrSplitView.documentGlobal`, `tabOrSplitView.pinned`, `tabOrSplitView.selected`, `this.#lastAddedTo`, `this.documentGlobal`

## MozTabbrowserTabGroup.ungroupTabs()
- 位置: L693-707
- 役割: TabGroupUngroup を発火し、全タブと分割ビューをグループから外す。
- 触るとき: グループ解除の処理を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `this.dispatchEvent()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(this.tabsAndSplitViews[i]))` → `gBrowser.ungroupSplitView()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(this.tabsAndSplitViews[i])))` → `Tabbrowser.isTab()`
- 条件付き依存: `if (Tabbrowser.isTab(this.tabsAndSplitViews[i]))` → `gBrowser.ungroupTab()`
- 参照: `TabMetrics.UNKNOWN_CONTEXT`, `this.tabsAndSplitViews`, `this.tabsAndSplitViews.length`

## MozTabbrowserTabGroup.save()
- 位置: L715-723
- 役割: グループを SessionStore に保存済みグループとして追加し TabGroupSaved を発火する。
- 触るとき: タブグループの保存処理を調べるとき。
- 呼び出し先: `SessionStore.addSavedTabGroup()`, `this.dispatchEvent()`
- 参照: `TabMetrics.UNKNOWN_CONTEXT`

## MozTabbrowserTabGroup.saveAndClose()
- 位置: L725-728
- 役割: グループを保存してから閉じる。
- 触るとき: 保存して閉じる操作を調べるとき。
- 呼び出し先: `gBrowser.removeTabGroup()`, `this.save()`
- 参照: `TabMetrics.UNKNOWN_CONTEXT`

## MozTabbrowserTabGroup.on_click()
- 位置: L733-748
- 役割: ラベルまたはオーバーフロー数の左クリックで折りたたみを切り替え、Glean に記録する。
- 触るとき: ラベルクリックでの開閉や関連テレメトリを調べるとき。
- 条件付き依存: `if (isToggleElement && event.button === 0)` → `event.preventDefault()`
- 条件付き依存: `if (isToggleElement && event.button === 0)` → `gBrowser.tabGroupMenu.close()`
- 条件付き依存: `if (isToggleElement && event.button === 0)` → `interactionMetric.add()`
- 参照: `Glean.tabgroup.groupInteractions.collapse`, `Glean.tabgroup.groupInteractions.expand`, `event.button`, `event.target`, `this.#labelElement`, `this.#overflowCountLabel`, `this.collapsed`

## MozTabbrowserTabGroup.on_mouseover()
- 位置: L753-761
- 役割: ラベルコンテナに入った時だけ TabGroupLabelHoverStart を発火する。
- 触るとき: ラベルのホバー開始イベントを調べるとき。
- 呼び出し先: `this.#labelContainerElement.contains()`
- 条件付き依存: `if (!this.#labelContainerElement.contains(event.relatedTarget))` → `this.#labelElement.dispatchEvent()`
- 参照: `event.relatedTarget`

## MozTabbrowserTabGroup.on_mouseout()
- 位置: L766-774
- 役割: ラベルコンテナを出た時だけ TabGroupLabelHoverEnd を発火する。
- 触るとき: ラベルのホバー終了イベントを調べるとき。
- 呼び出し先: `this.#labelContainerElement.contains()`
- 条件付き依存: `if (!this.#labelContainerElement.contains(event.relatedTarget))` → `this.#labelElement.dispatchEvent()`
- 参照: `event.relatedTarget`

## MozTabbrowserTabGroup.on_TabSelect()
- 位置: L779-790
- 役割: タブ選択に応じてアクティブ属性、aria-hidden、オーバーフロー表示を更新する。
- 触るとき: タブ切替時のグループ状態更新を調べるとき。
- 呼び出し先: `this.#updateOverflowLabel()`
- 条件付き依存: `if (this.hasActiveTab)` → `this.#updateTabAriaHidden()`
- 条件付き依存: `if (previousTab.group === this)` → `this.#updateTabAriaHidden()`
- 参照: `event.detail`, `event.target`, `event.target.group`, `previousTab.group`, `this.hasActiveTab`

## MozTabbrowserTabGroup.on_SplitViewTabChange()
- 位置: L792-798
- 役割: 分割ビューのタブ変更時に aria-hidden とオーバーフロー表示を更新する。
- 触るとき: 分割ビュー変更時のグループ表示を調べるとき。
- 呼び出し先: `this.#updateOverflowLabel()`, `this.#updateTabAriaHidden()`
- 参照: `event.target.tabs`

## MozTabbrowserTabGroup.select()
- 位置: L805-812
- 役割: グループを展開し、選択タブがあればスクロールで表示、なければ先頭タブを選択する。
- 触るとき: グループ選択時の挙動を調べるとき。
- 条件付き依存: `if (gBrowser.selectedTab.group == this)` → `gBrowser.tabContainer._handleTabSelect()`
- 参照: `gBrowser.selectedTab`, `gBrowser.selectedTab.group`, `this.collapsed`, `this.tabs`
