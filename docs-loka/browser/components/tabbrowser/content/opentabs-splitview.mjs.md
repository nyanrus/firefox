# browser/components/tabbrowser/content/opentabs-splitview.mjs

source: browser/components/tabbrowser/content/opentabs-splitview.mjs
source-hash: d416a9fd045cec6c215d3dc8fd19efa0a2285cd1
lines: 242

## <module>
- 役割: 分割ビューに追加するタブを選ぶ about:opentabs 用の splitview-opentabs 要素を定義し、unload 時に body を空にする。
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`, `customElements.define()`, `window.addEventListener()`

## OpenTabsInSplitView.constructor()
- 位置: L38-51
- 役割: 所属ウィンドウを求め、プライベートか否かでタブ監視対象を選び、コントローラと検索語を初期化する。
- 触るとき: プライベートウィンドウでの対象タブの選び方を調べるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `super()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(this.currentWindow))` → `lazy.getTabsTargetForWindow()`
- 参照: `( this.documentGlobal.top.browsingContext ).embedderWindowGlobal.browsingContext.window`, `lazy.NonPrivateTabs`, `lazy.OpenTabsController`, `this.controller`, `this.currentWindow`, `this.documentGlobal.top.browsingContext`, `this.listenersAdded`, `this.openTabsTarget`, `this.searchQuery`

## OpenTabsInSplitView.connectedCallback()
- 位置: L53-57
- 役割: 接続時にタブ変更と TabSelect の監視を始める。
- 触るとき: リスナー登録のタイミングを調べるとき。
- 呼び出し先: `super.connectedCallback()`, `this.addListeners()`, `this.currentWindow.addEventListener()`

## OpenTabsInSplitView.disconnectedCallback()
- 位置: L59-63
- 役割: 切断時にタブ変更と TabSelect の監視を解除する。
- 触るとき: リスナー解除漏れを調べるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.currentWindow.removeEventListener()`, `this.removeListeners()`

## OpenTabsInSplitView.addListeners()
- 位置: L65-73
- 役割: 未登録なら TabChange を監視し、必要なら再描画を要求する。
- 触るとき: タブ一覧の自動更新が働かないとき。
- 条件付き依存: `if (!this.listenersAdded)` → `this.openTabsTarget.addEventListener()`
- 条件付き依存: `if (!skipUpdate)` → `this.requestUpdate()`
- 参照: `this.listenersAdded`

## OpenTabsInSplitView.removeListeners()
- 位置: L75-80
- 役割: 登録済みなら TabChange の監視を解除する。
- 触るとき: 不要な更新を止める処理を調べるとき。
- 条件付き依存: `if (this.listenersAdded)` → `this.openTabsTarget.removeEventListener()`
- 参照: `this.listenersAdded`

## OpenTabsInSplitView.handleEvent()
- 位置: L82-96
- 役割: TabChange で再描画し、TabSelect では分割ビュー内かどうかで監視の付け外しを行う。
- 触るとき: タブ選択やタブ変更に対する更新の流れを変えるとき。
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (this.currentSplitView)` → `this.addListeners()`
- 条件付き依存: `if (this.currentSplitView)` → `this.requestUpdate()`
- 条件付き依存: `if (!(this.currentSplitView))` → `this.removeListeners()`
- 参照: `e.type`, `this.currentSplitView`

## OpenTabsInSplitView.getWindow()
- 位置: L98-101
- 役割: このページを埋め込んでいる親のブラウザウィンドウを返す。
- 触るとき: gBrowser など親ウィンドウへのアクセス方法を調べるとき。
- 参照: `(window.browsingContext) .embedderWindowGlobal.browsingContext.window`, `window.browsingContext`

## OpenTabsInSplitView.currentSplitView()
- 位置: L103-106
- 役割: 選択中タブが属する分割ビューを返す。
- 触るとき: 現在の分割ビューの取得元を調べるとき。
- 呼び出し先: `this.getWindow()`
- 参照: `gBrowser.selectedTab.splitview`

## OpenTabsInSplitView.onTabListRowClick()
- 位置: L108-117
- 役割: クリックされたタブで、自身の about:opentabs タブを分割ビュー内で置き換える。
- 触るとき: 一覧からタブを選んだときの分割ビューへの追加動作を変えるとき。
- 呼び出し先: `this.getWindow()`
- 条件付き依存: `if (this.currentSplitView)` → `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (this.currentSplitView)` → `this.currentSplitView.replaceTab()`
- 参照: `event.originalTarget.tabElement`, `this.currentSplitView`, `window.browsingContext.embedderElement`

## OpenTabsInSplitView.allAvailableTabs()
- 位置: L119-128
- 役割: 可視タブのうち、ピン留め・分割済み・about:opentabs を除いたものを返す。
- 触るとき: 一覧に出すタブの条件を変えるとき。
- 呼び出し先: `gBrowser.visibleTabs.filter()`, `this.getWindow()`
- 参照: `tab.pinned`, `tab.splitview`, `tab?.linkedBrowser?.currentURI?.spec`

## OpenTabsInSplitView.nonSplitViewUnpinnedTabs()
- 位置: L130-143
- 役割: 候補タブを、検索語がタイトルか URL に含まれるものに絞って返す。
- 触るとき: タブ検索の絞り込み規則を変えるとき。
- 条件付き依存: `if (this.searchQuery)` → `this.searchQuery.toLowerCase()`
- 条件付き依存: `if (this.searchQuery)` → `tabs.filter()`
- 条件付き依存: `if (this.searchQuery)` → `tab.label?.toLowerCase()`
- 条件付き依存: `if (this.searchQuery)` → `tab.linkedBrowser?.currentURI?.spec?.toLowerCase()`
- 条件付き依存: `if (this.searchQuery)` → `title.includes()`
- 条件付き依存: `if (this.searchQuery)` → `url.includes()`
- 参照: `this.allAvailableTabs`, `this.searchQuery`

## OpenTabsInSplitView.onSearchQuery()
- 位置: L145-147
- 役割: 検索イベントの文字列を searchQuery に設定する。
- 触るとき: 検索入力の反映を調べるとき。
- 参照: `e.detail.query`, `this.searchQuery`

## OpenTabsInSplitView.render()
- 位置: L149-229
- 役割: 候補が無いか分割ビュー外なら about:newtab を開き、そうでなければ検索欄とタブ一覧を描画する。
- 触るとき: ページの表示内容や空のとき newtab へ切り替える挙動を変えるとき。
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`, `this.controller.getTabListItems()`, `this.getWindow()`, `when()`
- 条件付き依存: `if ( !allTabs.length || (gBrowser.selectedTab.linkedBrowser.currentURI.spec === BROWSER_OPEN_TABS_URL && !this.currentSplitView) )` → `queueMicrotask()`
- 条件付き依存: `if ( !allTabs.length || (gBrowser.selectedTab.linkedBrowser.currentURI.spec === BROWSER_OPEN_TABS_URL && !this.currentSplitView) )` → `this.getWindow().openTrustedLinkIn()`
- 条件付き依存: `if ( !allTabs.length || (gBrowser.selectedTab.linkedBrowser.currentURI.spec === BROWSER_OPEN_TABS_URL && !this.currentSplitView) )` → `this.getWindow()`
- 参照: `allTabs.length`, `filteredTabs.length`, `gBrowser.selectedTab.linkedBrowser.currentURI.spec`, `this.allAvailableTabs`, `this.currentSplitView`, `this.nonSplitViewUnpinnedTabs`, `this.onSearchQuery`, `this.onTabListRowClick`, `this.searchQuery`
