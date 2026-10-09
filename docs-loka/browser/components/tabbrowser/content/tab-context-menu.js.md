# browser/components/tabbrowser/content/tab-context-menu.js

source: browser/components/tabbrowser/content/tab-context-menu.js
source-hash: be3252ae5f20fdd94e266372a5ccb1eec234fb6d
lines: 1495

## <module>
- 役割: タブのコンテキストメニューの構成定義と、表示時の項目更新や各操作を持つ TabContextMenu オブジェクトを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## _ensureMenuArranged()
- 位置: L355-390
- 役割: 初回表示時と代替構成 pref の変更後に、宣言済みのセクション構成へメニュー項目を並べ替える。
- 触るとき: メニュー項目の並びや classic と代替構成の切り替えを変えるとき。
- 呼び出し先: `console.error()`, `new this.MenuSectionLayout(layout, { dynamicItemSelectors: this.DYNAMIC_MENU_ITEM_SELECTORS, }).arrange()`, `this._hideUnusedSectionItems()`, `this._updateL10nIds()`
- 条件付き依存: `if (!this._altTabContextMenuPrefObserved)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this.DYNAMIC_MENU_ITEM_SELECTORS`, `this.MENU_SECTIONS.altstructure`, `this.MENU_SECTIONS.classic`, `this.MenuSectionLayout`, `this._altTabContextMenu`, `this._altTabContextMenuPrefObserved`, `this._tabContextMenuArranged`

## _updateL10nIds()
- 位置: L397-409
- 役割: 代替構成の有無に応じて、対象項目の data-l10n-id を代替用と元の ID で切り替える。
- 触るとき: 代替構成でメニュー文言が変わらない、または戻らないとき。
- 呼び出し先: `aPopupMenu.querySelectorAll()`
- 条件付き依存: `if (item._classicL10nId == null)` → `item.getAttribute()`
- 条件付き依存: `if (id)` → `item.setAttribute()`
- 参照: `item._classicL10nId`, `item.dataset.altL10nId`

## _hideUnusedSectionItems()
- 位置: L412-426
- 役割: レイアウトで unused に置かれた項目をすべて非表示にする。
- 触るとき: 代替構成で特定項目を隠したい、または意図せず隠れるとき。
- 呼び出し先: `document.querySelector()`, `this.MenuSectionLayout.placementsFor()`
- 参照: `item.hidden`, `layout.tabContextMenu`, `section.name`

## _updateMoveTabToFlattenedVisibility()
- 位置: L438-479
- 役割: 「タブを移動」サブメニューの共有ノードと区切り線の表示を、classic と代替構成に合わせて毎回設定する。
- 触るとき: 移動サブメニュー内のグループ項目や区切り線の表示がおかしいとき。
- 呼び出し先: `byId()`
- 参照: `byId("context_moveSplitViewToNewGroup").hidden`, `byId("context_moveTabToGroup").hidden`, `byId("context_moveTabToNewGroup").hidden`, `groupSeparator.hidden`, `lowerSeparator.hidden`, `newGroup.hidden`, `savedGroups.hidden`, `selectAllSeparator.hidden`, `this._altTabContextMenu`, `upperSeparator.hidden`

## byId()
- 位置: L443-443
- 役割: ID から要素を取得する局所ヘルパー。
- 触るとき: 移動サブメニューの表示制御で要素取得の仕方を変えるとき。
- 呼び出し先: `document.getElementById()`

## _updateToggleMuteMenuItems()
- 位置: L481-493
- 役割: タブの muted と soundplaying 属性をミュート切替項目の属性へ反映する。
- 触るとき: ミュート項目の表示状態が実際のタブ状態とずれるとき。
- 呼び出し先: `["muted", "soundplaying"].forEach()`, `aConditionFn()`
- 条件付き依存: `if (!aConditionFn || aConditionFn(attr))` → `aTab.hasAttribute()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `aTab.toggleMuteMenuItem.setAttribute()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `aTab.toggleMultiSelectMuteMenuItem.setAttribute()`
- 条件付き依存: `if (!(aTab.hasAttribute(attr)))` → `aTab.toggleMuteMenuItem.removeAttribute()`
- 条件付き依存: `if (!(aTab.hasAttribute(attr)))` → `aTab.toggleMultiSelectMuteMenuItem.removeAttribute()`

## updateContextMenu()
- 位置: L495-1114
- 役割: メニュー表示のたびに対象タブを決め、各項目の表示・無効・文言・グループ一覧などを状態に応じて更新する。
- 触るとき: コンテキストメニューの項目の出し分けや有効条件を追加・修正するとき。
- 呼び出し先: `JSON.stringify()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `SessionStore.getLastClosedTabCount()`, `SharingUtils.ensureShareMenu()`, `TabContextMenu.AIWindow.isAIWindowActiveAndEnabled()`, `TabContextMenu.TabStateFlusher.flush()`, `["http", "https"].includes()`, `aPopupMenu.addEventListener()`, `aPopupMenu.getElementsByAttribute()`, `aPopupMenu.triggerNode.closest()`, `contextMoveTabOptions.setAttribute()`, `document .getElementById()`, `document .getElementById("History:UndoCloseTab") .toggleAttribute()`, `document .getElementById("context_closeTab") .setAttribute()`, `document.getElementById()`, `document.l10n.setArgs()`, `document.l10n.setAttributes()`, `gBrowser._getTabsToTheEndFrom()`, `gBrowser._getTabsToTheStartFrom()`, `gBrowser.allTabsSelected()`, `gBrowser.getDuplicateTabsToClose()`, `gBrowser.openTabs.filter()`, `gBrowser.tabs.filter()`, `gSync.updateTabContextMenu()`, `selectedTabs.every()`, `showFullScreenViewContextMenuItems()`, `this._ensureMenuArranged()`, `this._updateMoveTabToFlattenedVisibility()`, `this._updateToggleMuteMenuItems()`, `this.contextTab.addEventListener()`, `this.contextTab.hasAttribute()`, `this.contextTab.splitview.tabs.at()`, `this.contextTabs.at()`, `this.contextTabs.every()`, `this.contextTabs.map()`, `this.contextTabs.some()`, `visibleOrCollapsedTabs.at()`, `visibleOrCollapsedTabs.every()`
- 条件付き依存: `if (tab.splitview)` → `splitViews.add()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `this.contextTabs.map(t => t.group).filter()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `this.contextTabs.map()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `gBrowser.getAllTabGroups()`
- 条件付き依存: `if (selectedGroupCount == 1)` → `this.contextTabs.every()`
- 条件付き依存: `if (groupToFilter && this.contextTabs.every(t => t.group))` → `openGroupsToMoveTo.filter()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `SessionStore.shouldSaveTabsToGroup()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && SessionStore.shouldSaveTabsToGroup(this.contextTabs) )` → `SessionStore.getSavedTabGroups()`
- 条件付き依存: `if (isAllSplitViewTabs)` → `contextMoveSplitViewToNewGroup.setAttribute()`
- 条件付き依存: `if (!(isAllSplitViewTabs))` → `contextMoveTabToNewGroup.setAttribute()`
- 条件付き依存: `if (isAllSplitViewTabs)` → `contextMoveTabToGroup.setAttribute()`
- 条件付き依存: `if (!(isAllSplitViewTabs))` → `contextMoveTabToGroup.setAttribute()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `document.getElementById()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsMenu .querySelectorAll("[tab-group-id]") .forEach()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsMenu .querySelectorAll()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `el.remove()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsToMoveTo.toReversed().forEach()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `openGroupsToMoveTo.toReversed()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `this._createTabGroupMenuItem()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `upperSeparator.after()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `savedGroupsMenu.querySelector()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `savedGroupsMenuPopup .querySelectorAll("[tab-group-id]") .forEach()`
- 条件付き依存: `if (!(!openGroupsToMoveTo.length && !savedGroupsToMoveTo.length))` → `savedGroupsMenuPopup .querySelectorAll()`
- 条件付き依存: `if (savedGroupsToMoveTo.length)` → `savedGroupsToMoveTo.forEach()`
- 条件付き依存: `if (savedGroupsToMoveTo.length)` → `this._createTabGroupMenuItem()`
- 条件付き依存: `if (savedGroupsToMoveTo.length)` → `savedGroupsMenuPopup.appendChild()`
- 条件付き依存: `if (TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled)` → `JSON.stringify()`
- 条件付き依存: `if (isAllSplitViewTabs)` → `contextUngroupSplitView.setAttribute()`
- 条件付き依存: `if (!(isAllSplitViewTabs))` → `contextUngroupTab.setAttribute()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.contextTabs.every()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.TabNotes.isEligible()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.removeNewBadge()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.tabs.notes.newBadge.enabled", true) )` → `this.addNewBadge()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.TabNotes.has(this.contextTab).then()`
- 条件付き依存: `if (this._tabNotesEnabled)` → `this.TabNotes.has()`
- 条件付き依存: `if (splitViewEnabled)` → `contextMoveTabToNewSplitView.removeAttribute()`
- 条件付き依存: `if (splitViewEnabled)` → `contextMoveTabToNewSplitView.setAttribute()`
- 条件付き依存: `if (splitViewEnabled)` → `this.contextTabs.filter()`
- 条件付き依存: `if (splitViewEnabled)` → `t.hasAttribute()`
- 条件付き依存: `if (this._unloadTabInContextMenu)` → `this.contextTabs.filter()`
- 条件付き依存: `if (this._unloadTabInContextMenu)` → `unloadTabItem.setAttribute()`
- 条件付き依存: `if (this._unloadTabInContextMenu)` → `JSON.stringify()`
- 条件付き依存: `if (!this._altTabContextMenu)` → `document.getElementById()`
- 条件付き依存: `if (!this._altTabContextMenu)` → `TabContextMenu.GenAI.buildTabMenu()`
- 条件付き依存: `if (!(!this._altTabContextMenu))` → `document.getElementById()`
- 条件付き依存: `if (!(!this._altTabContextMenu))` → `TabContextMenu.GenAI.buildTabSummarizeItem()`
- 条件付き依存: `if (lastTabToMove.pinned)` → `gBrowser.tabContainer.findNextTab()`
- 条件付き依存: `if (!contentSharingShareTabs.hidden)` → `this.addNewBadge()`
- 条件付き依存: `if (this._altTabContextMenu)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._altTabContextMenu))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (this._altTabContextMenu)` → `document .getElementById("context_sendTabToDevice") .setAttribute()`
- 条件付き依存: `if (this._altTabContextMenu)` → `document .getElementById()`
- 参照: `ContentSharingUtils.isEnabled`, `TabContextMenu.AITAB_ENABLED`, `TabContextMenu.Tabbrowser.prefs.tabGroupsEnabled`, `aPopupMenu.triggerNode`, `aPopupMenu.triggerNode.tab`, `array.length`, `array[index + 1].index`, `bookmarkMultiSelectedTabs.hidden`, `bookmarkTab.hidden`, `closeDuplicateTabsItem.disabled`, `closeOtherTabsItem.disabled`, `closeTabsToTheEndItem.disabled`, `closeTabsToTheStartItem.disabled`, `contentSharingShareTabs.hidden`, `contextAddNote.disabled`, `contextAddNote.hidden`, `contextEditNote.disabled`, `contextEditNote.hidden`, `contextMoveSplitViewToNewGroup.hidden`, `contextMoveTabOptions.disabled`, `contextMoveTabToEnd.disabled`, `contextMoveTabToGroup.hidden`, `contextMoveTabToNewGroup.hidden`, `contextMoveTabToNewSplitView.disabled`, `contextMoveTabToNewSplitView.hidden`, `contextMoveTabToStart.disabled`, `contextPinSelectedTabs.hidden`, `contextPinTab.hidden`, `contextReverseSplitView.hidden`, `contextSeparateSplitView.hidden`, `contextTab.splitview`, `contextUngroupSplitView.hidden`, `contextUngroupTab.hidden`, `contextUnpinSelectedTabs.hidden`, `contextUnpinTab.hidden`, `customizeTabs.length`, `document.getElementById("context_aiSeparator").hidden`, `document.getElementById("context_askChat").hidden`, `document.getElementById("context_askChatSummarize").hidden`, `document.getElementById("context_closeTabOptions").disabled`, `document.getElementById("context_createAITab").hidden`, `document.getElementById("context_duplicateTab").hidden`, `document.getElementById("context_duplicateTabs").hidden`, `document.getElementById("context_openTabInMiniWindow").hidden`, `document.getElementById("context_openTabInWindow").disabled`, `document.getElementById("context_playSelectedTabs").hidden`, `document.getElementById("context_playTab").hidden`, `document.getElementById("context_reloadSelectedTabs").hidden`, `document.getElementById("context_reloadTab").hidden`, `document.getElementById("context_shareSelectedTabsSeparator").hidden`, `element.index`, `gBrowser._getTabsToTheEndFrom(this.contextTab).length`, `gBrowser._getTabsToTheStartFrom(this.contextTab) .length`, `gBrowser.getDuplicateTabsToClose( this.contextTab ).length`, `gBrowser.openTabs.filter( t => !t.multiselected && !t.pinned && !t.hidden ).length`, `gBrowser.openTabs.filter( t => t != this.contextTab && !t.pinned && !t.hidden ).length`, `gBrowser.pinnedTabCount`, `gBrowser.selectedTab`, `gBrowser.selectedTabs`, `gBrowser.tabContainer?.verticalMode`, `gBrowser.tabs.length`, `gBrowser.visibleTabs.length`, `lastTabToMove.group`, `lastTabToMove.pinned`, `lowerSeparator.hidden`, `menuItem.disabled`, `openGroupsToMoveTo.length`, `pinnedTabs.length`, `reopenInContainer.disabled`, `reopenInContainer.hidden`, `savedGroupsMenu.disabled`, `savedGroupsToMoveTo.length`, `selectAllTabs.disabled`, `sibling.pinned`, `splitViews.size`, `t.canonicalUrl`, `t.group`, `t.hidden`, `t.isOpen`, `t.linkedBrowser`, `t.linkedBrowser.currentURI.spec`, `t.linkedBrowser?.isRemoteBrowser`, `t.linkedPanel`, `t.multiselected`, `t.pinned`, `tab.linkedBrowser`, `tab.linkedBrowser.currentURI.scheme`, `tab.splitview`, `this._altTabContextMenu`, `this._tabNotesEnabled`, `this._unloadTabInContextMenu`, `this.contextTab`, `this.contextTab.activeMediaBlocked`, `this.contextTab.hidden`, `this.contextTab.linkedBrowser`, `this.contextTab.multiselected`, `this.contextTab.pinned`, `this.contextTab.splitview`, `this.contextTab.splitview.tabs`, `this.contextTab.toggleMultiSelectMuteMenuItem`, `this.contextTab.toggleMuteMenuItem`, `this.contextTabs`, `this.contextTabs.length`, `this.contextTabs[0].canonicalUrl`, `this.contextTabs[0].group`, `this.multiselected`, `toggleMultiSelectMute.hidden`, `toggleMute.hidden`, `unloadTabItem.hidden`, `unloadableTabs.length`, `upperSeparator.parentNode`, `visibleOrCollapsedTabs.length`
- XPCOM: `Services.prefs`

## _createTabGroupMenuItem()
- 位置: L1116-1151
- 役割: タブグループ(開いている/保存済み)用のメニュー項目を、名前とグループ色付きで作る。
- 触るとき: グループ移動メニューの項目の見た目や名前表示を変えるとき。
- 呼び出し先: `document.createXULElement()`, `item.classList.add()`, `item.setAttribute()`, `item.style.setProperty()`
- 条件付き依存: `if (label)` → `item.setAttribute()`
- 条件付き依存: `if (!(label))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (isSaved)` → `item.classList.add()`
- 参照: `group.color`, `group.id`, `group.label`, `group.name`

## handleEvent()
- 位置: L1153-1170
- 役割: popuphidden で保持中のタブ参照を解放し、TabAttrModified でミュート項目を更新する。
- 触るとき: メニューを閉じた後の後始末や、表示中のタブ属性変化への追従を調べるとき。
- 呼び出し先: `aEvent.detail.changed.includes()`, `this._updateToggleMuteMenuItems()`
- 条件付き依存: `if (aEvent.target.id == "tabContextMenu")` → `this.contextTab.removeEventListener()`
- 参照: `aEvent.target`, `aEvent.target.id`, `aEvent.type`, `this.contextTab`, `this.contextTabs`

## createReopenInContainerMenu()
- 位置: L1172-1178
- 役割: 「コンテナで開き直す」サブメニューを、現在のコンテナを除いて生成する。
- 触るとき: コンテナ再オープンのサブメニュー内容を変えるとき。
- 呼び出し先: `createUserContextMenu()`, `this.contextTab.getAttribute()`

## duplicateSelectedTabs()
- 位置: L1179-1188
- 役割: 対象タブを複製し、最後の対象タブの直後に並べて配置する。
- 触るとき: タブ複製の位置やグループ内複製の telemetry を調べるとき。
- 呼び出し先: `SessionStore.duplicateTab()`, `gBrowser.moveTabTo()`, `this.contextTabs.at()`
- 条件付き依存: `if (tab.group)` → `Glean.tabgroup.tabInteractions.duplicate.add()`
- 参照: `tab.group`, `this.contextTabs`, `this.contextTabs.at(-1).index`

## reopenInContainer()
- 位置: L1189-1255
- 役割: 対象タブを指定コンテナの新しいタブとして開き直し、選択状態とミュート状態を引き継ぐ。
- 触るとき: コンテナ再オープン時の principal の扱いや引き継ぎ内容を調べるとき。
- 呼び出し先: `Glean.containers.tabAssignedContainer.record()`, `event.target.getAttribute()`, `gBrowser.addTab()`, `parseInt()`, `tab.getAttribute()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `JSON.parse()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `SessionStore.getTabState()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `E10SUtils.deserializePrincipal()`
- 条件付き依存: `if (!triggeringPrincipal || triggeringPrincipal.isNullPrincipal)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (triggeringPrincipal.isContentPrincipal)` → `Services.scriptSecurityManager.principalWithOA()`
- 条件付き依存: `if (tab.muted && !newTab.muted)` → `newTab.toggleMuteAudio()`
- 参照: `gBrowser.selectedTab`, `newTab.muted`, `tab.index`, `tab.linkedBrowser.contentPrincipal`, `tab.linkedBrowser.currentURI.spec`, `tab.linkedPanel`, `tab.muteReason`, `tab.muted`, `tab.pinned`, `tabState.triggeringPrincipal_base64`, `this.contextTabs`, `triggeringPrincipal.isContentPrincipal`, `triggeringPrincipal.isNullPrincipal`
- XPCOM: `Services.scriptSecurityManager`

## closeContextTabs()
- 位置: L1257-1272
- 役割: 複数選択なら選択タブ全部、そうでなければ対象タブを閉じる。
- 触るとき: メニューからのタブを閉じる動作や metrics を変えるとき。
- 条件付き依存: `if (this.contextTab.multiselected)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (this.contextTab.multiselected)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(this.contextTab.multiselected))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(this.contextTab.multiselected))` → `gBrowser.TabMetrics.userTriggeredContext()`
- 参照: `gBrowser.TabMetrics.METRIC_SOURCE.TAB_MENU`, `this.contextTab`, `this.contextTab.multiselected`

## explicitUnloadTabs()
- 位置: L1274-1276
- 役割: 対象タブをアンロードするよう gBrowser に依頼する。
- 触るとき: メニューからのタブのアンロード動作を調べるとき。
- 呼び出し先: `gBrowser.explicitUnloadTabs()`
- 参照: `this.contextTabs`

## moveTabsToNewGroup()
- 位置: L1278-1304
- 役割: 対象タブで新しいタブグループを作り、挿入位置を決めて、すべてタブパネルを閉じる。
- 触るとき: 新規グループ作成時の挿入位置や選択の挙動を変えるとき。
- 呼び出し先: `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.addTabGroup()`, `gTabsPanel.hideAllTabsPanel()`
- 参照: `firstUnpinnedTab.splitview`, `gBrowser.TabMetrics.METRIC_SOURCE.TAB_MENU`, `gBrowser.pinnedTabCount`, `gBrowser.selectedTab`, `gBrowser.tabs`, `insertBefore.index`, `this.contextTab`, `this.contextTab.group`, `this.contextTab.splitview`, `this.contextTabs`

## moveSplitViewToNewGroup()
- 位置: L1306-1337
- 役割: 対象タブを、分割ビューはまとめて1単位として新しいタブグループにする。
- 触るとき: 分割ビューを含むグループ化を調べるとき。contextTab.splitView の綴りが他箇所の splitview と異なる(要確認)。
- 呼び出し先: `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.addTabGroup()`, `gTabsPanel.hideAllTabsPanel()`
- 条件付き依存: `if (contextTab.splitView)` → `tabsAndSplitViews.includes()`
- 条件付き依存: `if (!tabsAndSplitViews.includes(contextTab.splitView))` → `tabsAndSplitViews.push()`
- 条件付き依存: `if (!(contextTab.splitView))` → `tabsAndSplitViews.push()`
- 参照: `contextTab.splitView`, `gBrowser.TabMetrics.METRIC_SOURCE.TAB_MENU`, `gBrowser.pinnedTabCount`, `gBrowser.selectedTab`, `gBrowser.tabs`, `insertBefore.index`, `this.contextTab`, `this.contextTab.group`, `this.contextTab.splitview`, `this.contextTabs`

## moveTabsToGroup()
- 位置: L1342-1354
- 役割: 対象タブ(分割ビューは丸ごと)を既存のタブグループに追加する。
- 触るとき: 既存グループへの移動動作を変えるとき。
- 呼び出し先: `Array.from()`, `elementsToMove.add()`, `elementsToMove.values()`, `gBrowser.TabMetrics.userTriggeredContext()`, `group.addTabs()`, `group.documentGlobal.focus()`
- 参照: `gBrowser.TabMetrics.METRIC_SOURCE.TAB_MENU`, `tab.splitview`, `this.contextTabs`

## addTabsToSavedGroup()
- 位置: L1356-1385
- 役割: 対象タブ(分割ビューの全タブを含む)を保存済みグループに追加し、元のタブを閉じる。
- 触るとき: 保存済みグループへの追加と閉じる動作を調べるとき。
- 呼び出し先: `SessionStore.addTabsToSavedGroup()`, `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.removeTabs()`
- 条件付き依存: `if (tab.splitview)` → `seen.has()`
- 条件付き依存: `if (!seen.has(splitTab))` → `seen.add()`
- 条件付き依存: `if (!seen.has(splitTab))` → `tabs.push()`
- 条件付き依存: `if (!(tab.splitview))` → `seen.has()`
- 条件付き依存: `if (!seen.has(tab))` → `seen.add()`
- 条件付き依存: `if (!seen.has(tab))` → `tabs.push()`
- 参照: `gBrowser.TabMetrics.METRIC_SOURCE.TAB_MENU`, `tab.splitview`, `tab.splitview.tabs`, `this.contextTabs`

## ungroupTabsAndSplitViews()
- 位置: L1387-1397
- 役割: 対象のタブと分割ビューをタブグループから外す。
- 触るとき: グループ解除メニューの動作を変えるとき。
- 呼び出し先: `splitViews.has()`
- 条件付き依存: `if (tab.splitview && !splitViews.has(tab.splitview))` → `splitViews.add()`
- 条件付き依存: `if (tab.splitview && !splitViews.has(tab.splitview))` → `gBrowser.ungroupSplitView()`
- 条件付き依存: `if (!tab.splitview)` → `gBrowser.ungroupTab()`
- 参照: `tab.splitview`, `this.contextTabs`

## moveTabsToSplitView()
- 位置: L1399-1431
- 役割: 対象タブで分割ビューを作り、1枚だけなら about:opentabs の新タブと組にする。
- 触るとき: メニューからの分割ビュー作成の動作や telemetry の trigger を変えるとき。
- 呼び出し先: `gBrowser.addTabSplitView()`, `tabsToAdd.indexOf()`, `this.contextTabs.includes()`
- 条件付き依存: `if (selectedTabIndex > -1 && selectedTabIndex != 0)` → `tabsToAdd.splice()`
- 条件付き依存: `if (selectedTabIndex > -1 && selectedTabIndex != 0)` → `tabsToAdd.unshift()`
- 条件付き依存: `if (this.contextTabs.length < 2)` → `gBrowser.addTrustedTab()`
- 参照: `gBrowser.selectedTab`, `this.contextTabs`, `this.contextTabs.length`

## unsplitTabs()
- 位置: L1433-1438
- 役割: 対象タブが属する分割ビューをすべて分割解除する。
- 触るとき: メニューからの分割解除を調べるとき。
- 呼び出し先: `splitview.unsplitTabs()`, `splitviews.forEach()`, `this.contextTabs.map()`, `this.contextTabs.map(tab => tab.splitview).filter()`
- 参照: `tab.splitview`

## reverseSplitView()
- 位置: L1440-1442
- 役割: 対象タブの分割ビューの左右順を入れ替える。
- 触るとき: メニューからの分割ビュー入れ替えを調べるとき。
- 呼び出し先: `this.contextTab.splitview?.reverseTabs()`

## addNewBadge()
- 位置: L1447-1453
- 役割: メニュー項目に「新規」バッジの属性とクラスを付ける。
- 触るとき: 新機能バッジの表示を追加・変更するとき。
- 呼び出し先: `gBrowser.tabLocalization.formatValueSync()`, `menuItem.classList.add()`, `menuItem.setAttribute()`

## removeNewBadge()
- 位置: L1458-1461
- 役割: メニュー項目から「新規」バッジの属性とクラスを外す。
- 触るとき: 新機能バッジの除去が効かないとき。
- 呼び出し先: `menuItem.classList.remove()`, `menuItem.removeAttribute()`
