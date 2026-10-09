# browser/components/firefoxview/viewpage.mjs

source: browser/components/firefoxview/viewpage.mjs
source-hash: 36f416b0c7f1efb1fc49078deeb0842b2d2cfa5e
lines: 253

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ViewPageContent.properties()
- 位置: L33-38
- 役割: (未記入)
- 触るとき: (未記入)

## ViewPageContent.constructor()
- 位置: L39-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.paused`

## ViewPageContent.ownerViewPage()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closest()`

## ViewPageContent.isVisible()
- 位置: L49-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isConnected`, `this.ownerDocument.visibilityState`, `this.ownerViewPage.selectedTab`

## ViewPageContent.viewVisibleCallback()
- 位置: L59-59
- 役割: (未記入)
- 触るとき: (未記入)

## ViewPageContent.viewHiddenCallback()
- 位置: L64-64
- 役割: (未記入)
- 触るとき: (未記入)

## ViewPageContent.getWindow()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext.embedderWindowGlobal.browsingContext.window`

## ViewPageContent.isSelectedBrowserTab()
- 位置: L70-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`
- 参照: `gBrowser.selectedBrowser.browsingContext`, `window.browsingContext`

## ViewPageContent.copyLink()
- 位置: L75-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.copyLink()`, `this.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.title`, `this.triggerNode.url`

## ViewPageContent.openInNewWindow()
- 位置: L80-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`, `this.getWindow().openTrustedLinkIn()`, `this.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.url`

## ViewPageContent.openInNewPrivateWindow()
- 位置: L87-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`, `this.getWindow().openTrustedLinkIn()`, `this.recordContextMenuTelemetry()`
- 参照: `this.triggerNode.url`

## ViewPageContent.recordContextMenuTelemetry()
- 位置: L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.contextMenuTabs.record()`
- 参照: `event.target.panel.dataset.tabType`

## ViewPageContent.shouldUpdate()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.shouldUpdate()`
- 参照: `this.paused`

## ViewPage.properties()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)

## ViewPage.constructor()
- 位置: L121-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `super()`, `this.onResize.bind()`, `this.onTabSelect.bind()`
- 参照: `this.onResize`, `this.onTabSelect`, `this.recentBrowsing`, `this.recentBrowsingElement`, `this.selectedTab`

## ViewPage.recentBrowsingElement()
- 位置: L129-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closest()`

## ViewPage.onResize()
- 位置: L133-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateAllVirtualLists()`, `this.windowResizeTask?.arm()`
- 参照: `lazy.DeferredTask`, `this.windowResizeTask`

## ViewPage.onTabSelect()
- 位置: L142-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`
- 条件付き依存: `if (win.FirefoxViewHandler.tab?.selected && isForegroundTab)` → `this.viewVisibleCallback()`
- 条件付き依存: `if (!(win.FirefoxViewHandler.tab?.selected && isForegroundTab))` → `this.viewHiddenCallback()`
- 参照: `gBrowser.selectedBrowser`, `target.documentGlobal`, `this.paused`, `win.FirefoxViewHandler.tab?.selected`, `window.docShell?.chromeEventHandler`

## ViewPage.connectedCallback()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`

## ViewPage.disconnectedCallback()
- 位置: L162-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.getWindow()`, `this.getWindow().removeEventListener()`
- 参照: `this.onResize`, `this.onTabSelect`

## ViewPage.updateAllVirtualLists()
- 位置: L168-194
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.recentBrowsing)` → `this.querySelectorAll()`
- 条件付き依存: `if (this.recentBrowsing)` → `viewComponents.forEach()`
- 条件付き依存: `if (this.recentBrowsing)` → `viewComponent.nodeName.includes()`
- 条件付き依存: `if (viewComponent.nodeName.includes("OPENTABS"))` → `viewComponent.viewCards.forEach()`
- 条件付き依存: `if (viewComponent.nodeName.includes("OPENTABS"))` → `currentTabLists.push()`
- 条件付き依存: `if (!(viewComponent.nodeName.includes("OPENTABS")))` → `viewComponent.shadowRoot.querySelectorAll()`
- 条件付き依存: `if (this.recentBrowsing)` → `tabLists.push()`
- 条件付き依存: `if (!(this.recentBrowsing))` → `this.shadowRoot.querySelectorAll()`
- 条件付き依存: `if (!this.paused)` → `tabLists.forEach()`
- 条件付き依存: `if (!tabList.updatesPaused && tabList.rootVirtualListEl?.isVisible)` → `tabList.rootVirtualListEl.recalculateAfterWindowResize()`
- 参照: `tabList.rootVirtualListEl?.isVisible`, `tabList.updatesPaused`, `this.paused`, `this.recentBrowsing`, `viewCard.tabList`

## ViewPage.toggleVisibilityInCardContainer()
- 位置: L196-230
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!isOpenTabs)` → `this.shadowRoot.querySelectorAll()`
- 条件付き依存: `if (!(!isOpenTabs))` → `this.viewCards.forEach()`
- 条件付き依存: `if (viewCard.cardEl)` → `cards.push()`
- 条件付き依存: `if (viewCard.cardEl)` → `tabLists.push()`
- 条件付き依存: `if (tabLists.length && cards.length)` → `cards.forEach()`
- 条件付き依存: `if (!(cardEl.visible !== !this.paused))` → `Array.from(tabLists).some()`
- 条件付き依存: `if (!(cardEl.visible !== !this.paused))` → `Array.from()`
- 条件付き依存: `if ( cardEl.isExpanded && Array.from(tabLists).some( tabList => tabList.updatesPaused !== this.paused ) )` → `tabLists.forEach()`
- 参照: `cardEl.isExpanded`, `cardEl.visible`, `cards.length`, `tabList.updatesPaused`, `tabLists.length`, `this.paused`, `viewCard.cardEl`, `viewCard.tabList`

## ViewPage.enter()
- 位置: L232-240
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isVisible)` → `this.viewVisibleCallback()`
- 条件付き依存: `if (this.isVisible)` → `this.getWindow().addEventListener()`
- 条件付き依存: `if (this.isVisible)` → `this.getWindow()`
- 参照: `this.isVisible`, `this.onResize`, `this.onTabSelect`, `this.paused`, `this.selectedTab`

## ViewPage.exit()
- 位置: L242-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWindow()`, `this.getWindow().removeEventListener()`, `this.viewHiddenCallback()`
- 条件付き依存: `if (!this.windowResizeTask?.isFinalized)` → `this.windowResizeTask?.finalize()`
- 参照: `this.onResize`, `this.onTabSelect`, `this.paused`, `this.selectedTab`, `this.windowResizeTask?.isFinalized`
