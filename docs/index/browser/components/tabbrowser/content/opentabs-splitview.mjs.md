# browser/components/tabbrowser/content/opentabs-splitview.mjs

source: browser/components/tabbrowser/content/opentabs-splitview.mjs
source-hash: d416a9fd045cec6c215d3dc8fd19efa0a2285cd1
lines: 242

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`, `customElements.define()`, `window.addEventListener()`

## OpenTabsInSplitView.constructor()
- 位置: L38-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `super()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(this.currentWindow))` → `lazy.getTabsTargetForWindow()`

## OpenTabsInSplitView.connectedCallback()
- 位置: L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addListeners()`, `this.currentWindow.addEventListener()`

## OpenTabsInSplitView.disconnectedCallback()
- 位置: L59-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.currentWindow.removeEventListener()`, `this.removeListeners()`

## OpenTabsInSplitView.addListeners()
- 位置: L65-73
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.listenersAdded)` → `this.openTabsTarget.addEventListener()`
- 条件付き依存: `if (!skipUpdate)` → `this.requestUpdate()`

## OpenTabsInSplitView.removeListeners()
- 位置: L75-80
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.listenersAdded)` → `this.openTabsTarget.removeEventListener()`

## OpenTabsInSplitView.handleEvent()
- 位置: L82-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 条件付き依存: `if (this.currentSplitView)` → `this.addListeners()`
- 条件付き依存: `if (this.currentSplitView)` → `this.requestUpdate()`
- 条件付き依存: `if (!(this.currentSplitView))` → `this.removeListeners()`

## OpenTabsInSplitView.getWindow()
- 位置: L98-101
- 役割: (未記入)
- 触るとき: (未記入)

## OpenTabsInSplitView.currentSplitView()
- 位置: L103-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`

## OpenTabsInSplitView.onTabListRowClick()
- 位置: L108-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`
- 条件付き依存: `if (this.currentSplitView)` → `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (this.currentSplitView)` → `this.currentSplitView.replaceTab()`

## OpenTabsInSplitView.allAvailableTabs()
- 位置: L119-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.visibleTabs.filter()`, `this.getWindow()`

## OpenTabsInSplitView.nonSplitViewUnpinnedTabs()
- 位置: L130-143
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.searchQuery)` → `this.searchQuery.toLowerCase()`
- 条件付き依存: `if (this.searchQuery)` → `tabs.filter()`
- 条件付き依存: `if (this.searchQuery)` → `tab.label?.toLowerCase()`
- 条件付き依存: `if (this.searchQuery)` → `tab.linkedBrowser?.currentURI?.spec?.toLowerCase()`
- 条件付き依存: `if (this.searchQuery)` → `title.includes()`
- 条件付き依存: `if (this.searchQuery)` → `url.includes()`

## OpenTabsInSplitView.onSearchQuery()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)

## OpenTabsInSplitView.render()
- 位置: L149-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`, `this.controller.getTabListItems()`, `this.getWindow()`, `when()`
- 条件付き依存: `if ( !allTabs.length || (gBrowser.selectedTab.linkedBrowser.currentURI.spec === BROWSER_OPEN_TABS_URL && !this.currentSplitView) )` → `queueMicrotask()`
- 条件付き依存: `if ( !allTabs.length || (gBrowser.selectedTab.linkedBrowser.currentURI.spec === BROWSER_OPEN_TABS_URL && !this.currentSplitView) )` → `this.getWindow().openTrustedLinkIn()`
- 条件付き依存: `if ( !allTabs.length || (gBrowser.selectedTab.linkedBrowser.currentURI.spec === BROWSER_OPEN_TABS_URL && !this.currentSplitView) )` → `this.getWindow()`
