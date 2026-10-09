# browser/components/aiwindow/ui/modules/TabManagementService.sys.mjs

source: browser/components/aiwindow/ui/modules/TabManagementService.sys.mjs
source-hash: e445201e38866f42cb5612e70c74e500cd60b217
lines: 1015

## <module>
- 役割: AI Window からのタブ操作 (閉じる、元に戻す、グループ化、開く、切り替え) を行うサービス。閉じたタブの復元は SessionStore に任せ、操作ごとの照合情報だけを保持する。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## TabManagementService.constructor()
- 位置: L51-53
- 役割: SessionStore を引数で差し替えられるようにし、省略時は実物を使う。
- 触るとき: テストで SessionStore をモックに差し替えたいとき。
- 参照: `this.#sessionStore`

## TabManagementService.restoreTabs()
- 位置: async L101-199
- 役割: 操作 ID に紐づく閉じたタブを、SessionStore の undoCloseTab で一つずつ復元し、元に選んでいたタブへ戻す。全件成功したときだけ操作の記録を消す。
- 触るとき: 元に戻す操作が一部だけ失敗する、または記録が残り続けるとき。
- 呼び出し先: `failedTabs.push()`, `lazy.console.error()`, `operation.windowRef?.get()`, `this.#findClosedTabIndexForOperationTab()`, `this.#recentCloseOperations.get()`, `this.#sessionStore.undoCloseTab()`, `window.gBrowser.tabs.includes()`
- 条件付き依存: `if (!operation)` → `lazy.console.warn()`
- 条件付き依存: `if (!window?.gBrowser)` → `lazy.console.warn()`
- 条件付き依存: `if (!window?.gBrowser)` → `operation.closedTabs.map()`
- 条件付き依存: `if (closedTabIndex == null)` → `failedTabs.push()`
- 条件付き依存: `if (restoredTab)` → `restoredTabs.push()`
- 条件付き依存: `if (!(restoredTab))` → `failedTabs.push()`
- 条件付き依存: `if (!failedTabs.length)` → `this.#recentCloseOperations.delete()`
- 参照: `closedOperationTab.url`, `error.message`, `failedTabs.length`, `operation.closedTabs`, `operation.closedTabs.length`, `restoredTabs.length`, `window.gBrowser.selectedTab`, `window?.gBrowser`

## TabManagementService.storeClosedTabsForUndo()
- 位置: L212-232
- 役割: 閉じたタブの照合情報を新しい操作 ID で保存する。保存数が 10 件に達していれば最も古いものを消す。
- 触るとき: 元に戻せる操作の保持件数や ID の形式を変えるとき。
- 呼び出し先: `Cu.getWeakReference()`, `Date.now()`, `this.#recentCloseOperations.set()`
- 条件付き依存: `if (this.#recentCloseOperations.size >= this.#MAX_STORED_OPERATIONS)` → `this.#recentCloseOperations.keys().next()`
- 条件付き依存: `if (this.#recentCloseOperations.size >= this.#MAX_STORED_OPERATIONS)` → `this.#recentCloseOperations.keys()`
- 条件付き依存: `if (this.#recentCloseOperations.size >= this.#MAX_STORED_OPERATIONS)` → `this.#recentCloseOperations.delete()`
- 参照: `closedTabs?.length`, `this.#MAX_STORED_OPERATIONS`, `this.#operationCounter`, `this.#recentCloseOperations.keys().next().value`, `this.#recentCloseOperations.size`

## TabManagementService.getStoredTabsForUndo()
- 位置: L240-242
- 役割: 操作 ID に対応する保存済みの情報を返す。無ければ null。
- 触るとき: 元に戻す操作の記録が残っているかを確かめるとき。
- 呼び出し先: `this.#recentCloseOperations.get()`

## TabManagementService.createTabGroup()
- 位置: async L268-347
- 役割: 有効なタブだけを addTabGroup でグループにする。色の指定が無ければ未使用の色を選ぶ。作成結果と失敗したタブを返す。
- 触るとき: タブグループの作成条件、ラベル、色の決め方を変えるとき。
- 呼び出し先: `lazy.console.error()`, `this.#getNextUnusedColor()`, `this.#validateTabsForGrouping()`, `window.gBrowser.addTabGroup()`
- 条件付き依存: `if (!tabs?.length)` → `lazy.console.warn()`
- 参照: `error.message`, `group.color`, `group.id`, `group.label`, `group.tabs.length`, `tabs?.length`, `validTabs.length`, `window?.gBrowser`

## TabManagementService.openTabs()
- 位置: L363-393
- 役割: URL ごとに背景タブを開き、失敗した URL は理由と共に集める。ウィンドウが無効なら例外を投げる。
- 触るとき: AI Window から新しいタブを開く挙動を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `failedUrls.push()`, `lazy.console.error()`, `openedTabs.push()`, `window.gBrowser.addTab()`
- 条件付き依存: `if (!urls?.length)` → `lazy.console.warn()`
- 参照: `error.message`, `urls?.length`, `window?.gBrowser`
- XPCOM: `Services.scriptSecurityManager`

## TabManagementService.switchToTab()
- 位置: L402-408
- 役割: 指定のタブを、そのウィンドウで選択状態にする。引数が無効なら警告を出すだけ。
- 触るとき: 既存のタブへ切り替える挙動を変えるとき。
- 条件付き依存: `if (!tab || !window?.gBrowser)` → `lazy.console.warn()`
- 参照: `window.gBrowser.selectedTab`, `window?.gBrowser`

## TabManagementService.findOpenTab()
- 位置: L420-440
- 役割: URL を正規化し、そのウィンドウで閉じかけでなく URL が完全に一致するタブを探す。除外集合に入るタブは対象外。
- 触るとき: 同じページを二重に開かないための照合条件を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `excludeTabs?.has()`, `window.gBrowser.tabs.find()`
- 参照: `Services.io.newURI(url).spec`, `tab.closing`, `tab.linkedBrowser?.currentURI?.spec`, `window?.gBrowser`
- XPCOM: `Services.io`

## TabManagementService.resolveOrOpenTabs()
- 位置: async L458-503
- 役割: URL ごとに既存のタブを探し、ピン留めやグループ化されていなければ既存を再利用する。無ければ一件ずつ新しく開く。
- 触るとき: 既存のタブを再利用する条件や、統合数の数え方を変えるとき。
- 呼び出し先: `failedUrls.push()`, `resolvedTabs.push()`, `this.findOpenTab()`, `this.openTabs()`
- 条件付き依存: `if (!tabs?.length)` → `lazy.console.warn()`
- 条件付き依存: `if (existingTab && !existingTab.pinned && !existingTab.group)` → `claimedTabs.add()`
- 条件付き依存: `if (existingTab && !existingTab.pinned && !existingTab.group)` → `resolvedTabs.push()`
- 参照: `existingTab.group`, `existingTab.pinned`, `tabs?.length`, `window?.gBrowser`

## TabManagementService.ungroupTabs()
- 位置: async L521-567
- 役割: グループ ID で探し、中のタブを一つずつグループから外す。タブ自体は閉じない。
- 触るとき: グループの解除、または取り消しの挙動を調べるとき。
- 呼び出し先: `lazy.console.error()`, `tabsInGroup.map()`, `window.gBrowser.tabGroups.find()`, `window.gBrowser.ungroupTab()`
- 参照: `error.message`, `g.id`, `group.tabs`, `tab.label`, `tab.linkedBrowser?.currentURI?.spec`, `tab.linkedPanel`, `window?.gBrowser`

## TabManagementService.getTabGroups()
- 位置: L593-602
- 役割: ウィンドウのタブグループを読み取り専用の情報にする。表示できるタブが一つも無いグループは除いて返す。
- 触るとき: AI Window に渡すグループ一覧の内容を変えるとき。
- 呼び出し先: `this.#getTabGroupInfo()`, `window.gBrowser.tabGroups .map()`, `window.gBrowser.tabGroups .map(group => this.#getTabGroupInfo(group)) .filter()`
- 条件付き依存: `if (!window?.gBrowser)` → `lazy.console.warn()`
- 参照: `group.tabCount`, `window?.gBrowser`

## TabManagementService.getTabGroupById()
- 位置: L616-631
- 役割: ID でグループを一つ探し、表示できるタブがあれば情報を返す。無ければ null。
- 触るとき: 個別のグループ情報を取得する経路を変えるとき。
- 呼び出し先: `this.#getTabGroupInfo()`, `window.gBrowser.tabGroups.find()`
- 条件付き依存: `if (!groupId || !window?.gBrowser)` → `lazy.console.warn()`
- 参照: `g.id`, `groupInfo.tabCount`, `window?.gBrowser`

## TabManagementService.#getTabGroupInfo()
- 位置: L642-669
- 役割: グループ内のタブのうち、非表示、閉じかけ、許可されていない URL、新規ページを除く。残したタブのタイトルは無害化する。
- 触るとき: グループ情報としてモデルや UI に出す URL やタイトルの条件を変えるとき。
- 呼び出し先: `isAllowedURLProtocol()`, `isNewPageUrl()`
- 条件付き依存: `if ( !tab.hidden && !tab.closing && isAllowedURLProtocol(url) && !isNewPageUrl(url) )` → `tabs.push()`
- 条件付き依存: `if ( !tab.hidden && !tab.closing && isAllowedURLProtocol(url) && !isNewPageUrl(url) )` → `sanitizeUntrustedContent()`
- 参照: `group.color`, `group.id`, `group.label`, `group.tabs`, `tab.closing`, `tab.hidden`, `tab.label`, `tab.lastAccessed`, `tab.linkedBrowser?.currentURI?.spec`, `tabs.length`

## TabManagementService.#getNextUnusedColor()
- 位置: L678-697
- 役割: TAB_GROUP_COLORS の中で、まだ使われていない最初の色を返す。全部使われていればランダムに選ぶ。
- 触るとき: 新しいグループの色の割り当て方を変えるとき。
- 呼び出し先: `Math.floor()`, `Math.random()`, `TabManagementService.TAB_GROUP_COLORS.find()`, `usedColors.has()`, `window.gBrowser.getAllTabGroups()`, `window.gBrowser.getAllTabGroups().map()`
- 参照: `TabManagementService.TAB_GROUP_COLORS`, `TabManagementService.TAB_GROUP_COLORS.length`, `group.color`

## TabManagementService.getGroupingRejection()
- 位置: L714-729
- 役割: タブをグループに入れられない理由を返す。無効なタブ、ピン留め、グループ化済み、閉じかけのいずれか。問題が無ければ null。
- 触るとき: グループ化できない理由の種類や判定の順序を変えるとき。
- 参照: `tab.closing`, `tab.documentGlobal`, `tab.group`, `tab.pinned`, `tab?.linkedBrowser`

## TabManagementService.#validateTabsForGrouping()
- 位置: L731-745
- 役割: 各タブを getGroupingRejection で判定し、有効なタブと理由付きの失敗したタブに振り分ける。
- 触るとき: グループ化の前段の振り分けを変えるとき。
- 呼び出し先: `tabs.forEach()`, `this.getGroupingRejection()`, `validTabs.push()`
- 条件付き依存: `if (reason)` → `failedTabs.push()`

## TabManagementService.closeTabs()
- 位置: async L755-796
- 役割: 有効なタブを閉じ、閉じたタブの情報を元に戻す操作として保存する。操作 ID と失敗したタブを返す。
- 触るとき: タブを閉じる操作の結果や、元に戻す操作 ID の受け渡しを変えるとき。
- 呼び出し先: `this.#performTabClosing()`, `this.#validateTabsForClosing()`
- 条件付き依存: `if (!tabs?.length)` → `lazy.console.warn()`
- 条件付き依存: `if (closedTabs.length)` → `this.storeClosedTabsForUndo()`
- 条件付き依存: `if (error)` → `lazy.console.error()`
- 条件付き依存: `if (error)` → `failedTabs.push()`
- 参照: `closedTabs.length`, `error.message`, `tabs.length`, `tabs?.length`, `window?.gBrowser`

## TabManagementService.#validateTabsForClosing()
- 位置: L807-829
- 役割: このウィンドウにあり閉じかけでないタブだけを残す。それ以外は理由付きで失敗に入れる。
- 触るとき: 閉じる対象の除外条件を変えるとき。
- 呼び出し先: `tabs.filter()`
- 条件付き依存: `if (!tabInWindow)` → `failedTabs.push()`
- 条件付き依存: `if (tab.closing)` → `failedTabs.push()`
- 参照: `tab.closing`, `tab.documentGlobal`, `tab?.linkedBrowser`

## TabManagementService.#performTabClosing()
- 位置: async L839-867
- 役割: 閉じる前に各タブの情報を保存してから removeTab で閉じる。最後のタブでもウィンドウは閉じない。例外が起きたら、それまでの結果と例外を返す。
- 触るとき: タブを閉じる順序や、閉じた後の記録の仕組みを変えるとき。
- 呼び出し先: `Date.now()`, `closedTabs.push()`, `this.#getTabInfo()`, `window.gBrowser.removeTab()`

## TabManagementService.#compareClosedTabTimestamps()
- 位置: L869-883
- 役割: 候補が複数あるとき、閉じた時刻が操作時刻に最も近い候補の索引を返す。
- 触るとき: 同じ URL のタブが複数閉じられていたときに、どれを復元するかの選び方を変えるとき。
- 呼び出し先: `Math.abs()`, `matches.slice()`
- 参照: `bestMatch.closedAt`, `bestMatch.index`, `match.closedAt`

## TabManagementService.#findClosedTabIndexForOperationTab()
- 位置: L894-918
- 役割: SessionStore の閉じたタブ一覧から、URL とコンテナ ID が一致するものの索引を返す。複数なら時刻が近いものを選ぶ。
- 触るとき: 元に戻す対象が違うタブになる、または見つからないとき。
- 呼び出し先: `closedTabData.entries()`, `this.#closedTabMatchesOperationTab()`, `this.#compareClosedTabTimestamps()`, `this.#getClosedTabData()`
- 条件付き依存: `if (this.#closedTabMatchesOperationTab(closedTab, operationTab))` → `matches.push()`
- 参照: `closedTab.closedAt`, `closedTab.state?.closedAt`, `matches.length`, `matches[0].index`, `operationTab.operationTimestamp`

## TabManagementService.#closedTabMatchesOperationTab()
- 位置: L928-938
- 役割: 閉じたタブの URL とコンテナ ID が、操作時のタブと両方一致するかを返す。
- 触るとき: 復元対象の照合条件を変えるとき。
- 呼び出し先: `this.#normalizeClosedTab()`
- 参照: `closedTabInfo.url`, `closedTabInfo.userContextId`, `operationTab.url`, `operationTab.userContextId`

## TabManagementService.#getClosedTabData()
- 位置: L947-950
- 役割: SessionStore から、ウィンドウの閉じたタブ一覧を配列として取り出す。配列でなければ空配列にする。
- 触るとき: SessionStore からの取得方法を変えるとき。
- 呼び出し先: `Array.isArray()`, `this.#sessionStore.getClosedTabDataForWindow()`

## TabManagementService.#normalizeClosedTab()
- 位置: L965-984
- 役割: SessionStore の閉じたタブの状態から URL、タイトル、コンテナ ID、ピン留めを取り出す。インデックスは 1 始まりとして扱う。
- 触るとき: SessionStore の形式が変わって照合が外れるとき。
- 呼び出し先: `Math.max()`, `entries.at()`
- 参照: `activeEntry?.title`, `activeEntry?.url`, `closedTab?.state`, `closedTab?.title`, `closedTab?.userContextId`, `state.entries`, `state.index`, `state.originAttributes?.userContextId`, `state.pinned`, `state.title`, `state.url`, `state.userContextId`

## TabManagementService.#getTabInfo()
- 位置: L999-1011
- 役割: タブの ID、URL、タイトル、コンテナ ID を取り出し、後の照合に使う情報を作る。
- 触るとき: 閉じたタブの照合に使う情報を増やす、または減らすとき。
- 呼び出し先: `tab.getAttribute()`
- 参照: `browser.contentPrincipal`, `browser.currentURI?.spec`, `principal?.originAttributes?.userContextId`, `tab.label`, `tab.linkedBrowser`, `tab.userContextId`
