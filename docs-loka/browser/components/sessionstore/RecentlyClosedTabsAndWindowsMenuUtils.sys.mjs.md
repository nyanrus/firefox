# browser/components/sessionstore/RecentlyClosedTabsAndWindowsMenuUtils.sys.mjs

source: browser/components/sessionstore/RecentlyClosedTabsAndWindowsMenuUtils.sys.mjs
source-hash: dccf3fcb38c8b0ec94f37309ad8905df18aed7d4
lines: 662

## <module>
- 役割: 最近閉じたタブ・タブグループ・ウィンドウを、メニューとパネル用の UI 要素にして再度開く処理をまとめる。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## l10n()
- 位置: L14-14
- 役割: 最近閉じたタブ用の文字列を読む Localization を遅延生成する。
- 触るとき: メニューの表示文字列を追加・変更するとき、参照ファイルを確認するとき。

## getClosedTabGroupsById()
- 位置: L27-34
- 役割: 閉じたタブグループの一覧を ID をキーにした Map にする。
- 触るとき: タブが閉じたグループに属するかを判定する元データを変えるとき。
- 呼び出し先: `closedTabGroups.forEach()`, `closedTabGroupsById.set()`, `lazy.SessionStore.getClosedTabGroups()`
- 参照: `tabGroup.id`

## getTabsFragment()
- 位置: L46-132
- 役割: 閉じたタブを UI 要素の断片にする。グループは一まとまりで出し、最後に「すべて開く」を付ける。
- 触るとき: 閉じたタブの一覧に出る範囲を変えるとき。対象は設定に応じて全ウィンドウと閉じたウィンドウ(プライベートでない場合)。
- 呼び出し先: `doc.createDocumentFragment()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStore.getClosedTabCount()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `lazy.SessionStore.getWindows()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `closedTabSets.push()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `lazy.SessionStore.getClosedTabDataForWindow()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `lazy.SessionStore.getClosedTabCountFromClosedWindows()`
- 条件付き依存: `if ( !isPrivate && lazy.closedTabsFromClosedWindowsEnabled && lazy.SessionStore.getClosedTabCountFromClosedWindows() )` → `closedTabSets.push()`
- 条件付き依存: `if ( !isPrivate && lazy.closedTabsFromClosedWindowsEnabled && lazy.SessionStore.getClosedTabCountFromClosedWindows() )` → `lazy.SessionStore.getClosedTabDataFromClosedWindows()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `getClosedTabGroupsById()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `closedTabSets.forEach()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `tabSet.forEach()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCount({ sourceWindow: aWindow, }) )` → `closedTabGroupsById.has()`
- 条件付き依存: `if (aTagName == "menuitem")` → `createTabGroupSubmenu()`
- 条件付き依存: `if (aTagName == "menuitem")` → `closedTabGroupsById.get()`
- 条件付き依存: `if (!(aTagName == "menuitem"))` → `createTabGroupSubpanel()`
- 条件付き依存: `if (!(aTagName == "menuitem"))` → `closedTabGroupsById.get()`
- 条件付き依存: `if (!(groupId && closedTabGroupsById.has(groupId)))` → `createEntry()`
- 条件付き依存: `if (!isEmpty)` → `createRestoreAllEntry()`
- 参照: `aWindow.document`, `lazy.closedTabsFromAllWindowsEnabled`, `lazy.closedTabsFromClosedWindowsEnabled`, `tab.closedInTabGroupId`, `tab.title`

## getWindowsFragment()
- 位置: L143-191
- 役割: 閉じたウィンドウを UI 要素の断片にする。各ウィンドウは選択中のタブの情報で表し、「すべて開く」を付ける。
- 触るとき: 閉じたウィンドウのメニュー表示や並び順を変えるとき。
- 呼び出し先: `doc.createDocumentFragment()`, `lazy.SessionStore.getClosedWindowData()`
- 条件付き依存: `if (selectedTab)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (selectedTab)` → `createEntry()`
- 条件付き依存: `if (closedWindowData.length)` → `createRestoreAllEntry()`
- 参照: `aWindow.document`, `closedWindowData.length`, `closedWindowData[i].closedAt`, `tabs.length`

## onRestoreAllTabsCommand()
- 位置: L199-259
- 役割: 「すべてのタブを開く」の実行時に、対象の全ウィンドウと閉じたウィンドウのタブを順に開き直す。
- 触るとき: 一括で開き直す対象の範囲や順序を変えるとき。
- 呼び出し先: `getClosedTabGroupsById()`, `lazy.SessionStore.getClosedTabDataForWindow()`, `lazy.SessionStore.getWindows()`, `lazy.SessionStore.undoCloseTab()`, `lazy.SessionStore.undoCloseTabGroup()`, `undoAllInTabData()`
- 条件付き依存: `if (lazy.closedTabsFromClosedWindowsEnabled)` → `lazy.SessionStore.getClosedTabDataFromClosedWindows()`
- 条件付き依存: `if (lazy.closedTabsFromClosedWindowsEnabled)` → `undoAllInTabData()`
- 条件付き依存: `if (lazy.closedTabsFromClosedWindowsEnabled)` → `lazy.SessionStore.undoClosedTabFromClosedWindow()`
- 条件付き依存: `if (lazy.closedTabsFromClosedWindowsEnabled)` → `lazy.SessionStore.undoCloseTabGroup()`
- 参照: `aEvent.target.documentGlobal`, `lazy.closedTabsFromAllWindowsEnabled`, `lazy.closedTabsFromClosedWindowsEnabled`, `tab.closedId`, `tab.sourceClosedId`, `tabs[0].sourceClosedId`, `tabs[0].state.groupId`

## undoAllInTabData()
- 位置: L206-219
- 役割: タブのデータを先頭から取り出し、グループなら所属タブ数だけまとめてグループ用の関数へ、そうでなければ一つずつ個別の関数へ渡す。
- 触るとき: 一括で開き直すときのグループの扱いを変えるとき。
- 呼び出し先: `closedTabGroupsById.has()`
- 条件付き依存: `if (currentTabGroupId && closedTabGroupsById.has(currentTabGroupId))` → `closedTabGroupsById.get()`
- 条件付き依存: `if (currentTabGroupId && closedTabGroupsById.has(currentTabGroupId))` → `tabData.splice()`
- 条件付き依存: `if (currentTabGroupId && closedTabGroupsById.has(currentTabGroupId))` → `tabGroupMethod()`
- 条件付き依存: `if (!(currentTabGroupId && closedTabGroupsById.has(currentTabGroupId)))` → `tabData.splice()`
- 条件付き依存: `if (!(currentTabGroupId && closedTabGroupsById.has(currentTabGroupId)))` → `tabMethod()`
- 参照: `currentTabGroup.tabs.length`, `tabData.length`, `tabData[0].state.groupId`

## onRestoreAllWindowsCommand()
- 位置: L267-272
- 役割: 閉じたウィンドウをすべて ID 指定で開き直す。
- 触るとき: 「すべてのウィンドウを開く」の動きを変えるとき。
- 呼び出し先: `lazy.SessionStore.getClosedWindowData()`, `lazy.SessionStore.undoCloseById()`

## _undoCloseMiddleClick()
- 位置: L281-305
- 役割: 中クリックで閉じたタブを開き、そのタブを末尾に移し、親のパネルを閉じる。
- 触るとき: 中クリックの振る舞いを変えるとき、またはツールバーのパネルで中クリックが効かない原因を調べるとき。
- 呼び出し先: `aEvent.originalTarget.hasAttribute()`, `aEvent.target.closest()`, `aEvent.view.gBrowser.moveTabToEnd()`
- 条件付き依存: `if (aEvent.originalTarget.hasAttribute("source-closed-id"))` → `lazy.SessionStore.undoClosedTabFromClosedWindow()`
- 条件付き依存: `if (aEvent.originalTarget.hasAttribute("source-closed-id"))` → `aEvent.originalTarget.getAttribute()`
- 条件付き依存: `if (!(aEvent.originalTarget.hasAttribute("source-closed-id")))` → `lazy.SessionWindowUI.undoCloseTab()`
- 条件付き依存: `if (!(aEvent.originalTarget.hasAttribute("source-closed-id")))` → `aEvent.originalTarget.getAttribute()`
- 条件付き依存: `if (ancestorPanel)` → `ancestorPanel.hidePopup()`
- 参照: `aEvent.button`, `aEvent.view`

## setTabGroupColorProperties()
- 位置: L312-329
- 役割: タブグループの色を、要素の CSS 変数(通常、反転、淡色、背景)に設定する。
- 触るとき: 閉じたタブグループの配色を変えるとき。
- 呼び出し先: `element.style.setProperty()`
- 参照: `tabGroup.color`

## createTabGroupSubmenu()
- 位置: L346-392
- 役割: タブグループ用のメニュー項目を作り、中に各タブと「グループを開く」を入れる。
- 触るとき: メニューで閉じたタブグループの見た目や中の項目を変えるとき。
- 呼び出し先: `aDocument.createXULElement()`, `aDocument.l10n.setAttributes()`, `aFragment.appendChild()`, `aTabGroup.tabs.forEach()`, `createEntry()`, `element.appendChild()`, `element.classList.add()`, `lazy.SessionStore.undoCloseTabGroup()`, `menuPopup.appendChild()`, `reopenTabGroupItem.addEventListener()`, `setTabGroupColorProperties()`
- 条件付き依存: `if (aTabGroup.name)` → `element.setAttribute()`
- 条件付き依存: `if (!(aTabGroup.name))` → `aDocument.l10n.setAttributes()`
- 参照: `aTabGroup.id`, `aTabGroup.name`, `tab.title`

## createTabGroupSubpanel()
- 位置: L409-484
- 役割: タブグループ用のツールバーボタンを作り、開くとタブ一覧のパネルビューが出る形にする。同じ ID のパネルは作り直す。
- 触るとき: パネルの中の閉じたタブグループの表示を変えるとき。
- 呼び出し先: `aDocument.createXULElement()`, `aDocument.documentGlobal.PanelUI.showSubView()`, `aDocument.getElementById()`, `aDocument.l10n.setAttributes()`, `aFragment.appendChild()`, `aTabGroup.tabs.forEach()`, `createEntry()`, `element.addEventListener()`, `element.classList.add()`, `element.setAttribute()`, `lazy.SessionStore.undoCloseTabGroup()`, `panelview.appendChild()`, `reopenTabGroupItem.addEventListener()`, `reopenTabGroupItem.classList.add()`, `setTabGroupColorProperties()`
- 条件付き依存: `if (aTabGroup.name)` → `element.setAttribute()`
- 条件付き依存: `if (!(aTabGroup.name))` → `aDocument.l10n.setAttributes()`
- 条件付き依存: `if (panelview)` → `panelview.remove()`
- 参照: `aTabGroup.id`, `aTabGroup.name`, `panelBody.className`, `panelview.id`, `tab.title`

## createEntry()
- 位置: L507-606
- 役割: 閉じたタブやウィンドウ一つ分の UI 要素を作り、クリック時の復元処理、ファビコン、ツールチップ、ショートカットを設定する。
- 触るとき: 閉じたタブの項目が正しい復元処理に繋がらないとき、または項目の表示属性を変えるとき。先頭の項目には復元のショートカットを割り当てる。
- 呼び出し先: `aDocument.createXULElement()`, `aParent.appendChild()`, `element.setAttribute()`, `lazy.SessionStore.historyIndex()`
- 条件付き依存: `if (aTooltipText)` → `element.setAttribute()`
- 条件付き依存: `if (aClosedTab.image)` → `lazy.PlacesUIUtils.getImageURL()`
- 条件付き依存: `if (aClosedTab.image)` → `element.setAttribute()`
- 条件付き依存: `if (aClosedTab.image)` → `ChromeUtils.encodeURIForSrcset()`
- 条件付き依存: `if (aIsWindowsFragment)` → `element.addEventListener()`
- 条件付き依存: `if (aIsWindowsFragment)` → `lazy.SessionWindowUI.undoCloseWindow()`
- 条件付き依存: `if (typeof closedTab.sourceClosedId == "number")` → `element.setAttribute()`
- 条件付き依存: `if (typeof closedTab.sourceClosedId == "number")` → `String()`
- 条件付き依存: `if (typeof closedTab.sourceClosedId == "number")` → `element.addEventListener()`
- 条件付き依存: `if (typeof closedTab.sourceClosedId == "number")` → `lazy.SessionStore.undoClosedTabFromClosedWindow()`
- 条件付き依存: `if (!(typeof closedTab.sourceClosedId == "number"))` → `element.setAttribute()`
- 条件付き依存: `if (!(typeof closedTab.sourceClosedId == "number"))` → `String()`
- 条件付き依存: `if (!(typeof closedTab.sourceClosedId == "number"))` → `element.addEventListener()`
- 条件付き依存: `if (!(typeof closedTab.sourceClosedId == "number"))` → `lazy.SessionWindowUI.undoCloseTab()`
- 条件付き依存: `if (aTagName == "menuitem")` → `element.setAttribute()`
- 条件付き依存: `if (aTagName == "toolbarbutton")` → `element.setAttribute()`
- 条件付き依存: `if (activeIndex >= 0 && tabData.entries[activeIndex])` → `element.setAttribute()`
- 条件付き依存: `if (!aIsWindowsFragment && aTagName != "menuitem")` → `element.addEventListener()`
- 条件付き依存: `if (aIndex == 0)` → `element.setAttribute()`
- 参照: `(aClosedTab).state`, `(event.target).documentGlobal`, `RecentlyClosedTabsAndWindowsMenuUtils._undoCloseMiddleClick`, `aClosedTab.image`, `closedTab.closedId`, `closedTab.sourceClosedId`, `closedTab.sourceWindowId`, `event.target`, `tabData.entries`, `tabData.entries[activeIndex].url`

## createRestoreAllEntry()
- 位置: L625-661
- 役割: 「すべて開く」の項目を作り、ウィンドウ用かタブ用かに応じた命令を付ける。メニューでは区切り線も入れる。
- 触るとき: 「すべて開く」の文言や区切りの表示を変えるとき。
- 呼び出し先: `aDocument.createXULElement()`, `aFragment.appendChild()`, `lazy.l10n.formatValueSync()`, `restoreAllElements.addEventListener()`, `restoreAllElements.classList.add()`, `restoreAllElements.setAttribute()`
- 条件付き依存: `if (aTagName == "toolbarbutton")` → `restoreAllElements.classList.add()`
- 条件付き依存: `if (aTagName == "menuitem")` → `aFragment.appendChild()`
- 条件付き依存: `if (aTagName == "menuitem")` → `aDocument.createXULElement()`
- 参照: `RecentlyClosedTabsAndWindowsMenuUtils.onRestoreAllTabsCommand`, `RecentlyClosedTabsAndWindowsMenuUtils.onRestoreAllWindowsCommand`
