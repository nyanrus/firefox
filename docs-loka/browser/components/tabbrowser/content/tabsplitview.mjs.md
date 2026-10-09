# browser/components/tabbrowser/content/tabsplitview.mjs

source: browser/components/tabbrowser/content/tabsplitview.mjs
source-hash: 525dc14c8df28cf6d9223cad8c7f7a052d1beb87
lines: 502

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`, `document.getElementById()`

## MozTabSplitViewWrapper.hasActiveTab()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabSplitViewWrapper.shouldMoveAllTabsAtOnce()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabSplitViewWrapper.group()
- 位置: L74-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isTabGroup()`

## MozTabSplitViewWrapper.state()
- 位置: L86-91
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabSplitViewWrapper.hasActiveTab()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozTabSplitViewWrapper.multiselected()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabSplitViewWrapper.constructor()
- 位置: L104-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`

## MozTabSplitViewWrapper.connectedCallback()
- 位置: L114-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observeTabChanges()`, `this.#restorePanelWidths()`, `this.documentGlobal.addEventListener()`
- 条件付き依存: `if (this.hasActiveTab)` → `this.#activate()`
- 条件付き依存: `if (!this._hasUsedSplitView)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## MozTabSplitViewWrapper.disconnectedCallback()
- 位置: L142-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deactivate()`, `this.#resetPanelWidths()`, `this.#tabChangeObserver?.disconnect()`, `this.container.dispatchEvent()`, `this.documentGlobal.removeEventListener()`

## MozTabSplitViewWrapper.#observeTabChanges()
- 位置: L155-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabChangeObserver.observe()`
- 条件付き依存: `if (this.tabs.length)` → `this.tabs.some()`
- 条件付き依存: `if (this.tabs.length)` → `this.tabs.forEach()`
- 条件付き依存: `if (this.tabs.length)` → `tab.setAttribute()`
- 条件付き依存: `if (this.tabs.length)` → `tab.updateSplitViewAriaLabel()`
- 条件付き依存: `if (this.tabs.length)` → `this.dispatchEvent()`
- 条件付き依存: `if (!(this.tabs.length))` → `this.remove()`
- 条件付き依存: `if (!this.#tabChangeObserver)` → `mutations.some()`
- 条件付き依存: `if ( this.tabs.length == 1 && mutations.some(mutation => mutation.removedNodes.length == 1) )` → `this.unsplitTabs()`

## MozTabSplitViewWrapper.splitViewId()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`, `this.getAttribute()`

## MozTabSplitViewWrapper.splitViewId()
- 位置: L195-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setAttribute()`

## MozTabSplitViewWrapper.tabs()
- 位置: L202-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.children).filter()`, `node.matches()`

## MozTabSplitViewWrapper.visible()
- 位置: L206-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabs.every()`

## MozTabSplitViewWrapper.pinned()
- 位置: L210-212
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabSplitViewWrapper.splitview()
- 位置: L220-222
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabSplitViewWrapper.panels()
- 位置: L229-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (el)` → `panels.push()`

## MozTabSplitViewWrapper.#activate()
- 位置: L243-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.showSplitViewPanels()`, `this.container.dispatchEvent()`, `updateUrlbarButton.arm()`

## MozTabSplitViewWrapper.#deactivate()
- 位置: L258-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabpanels.removeTabsFromSplitview()`, `this.#tabs.filter()`, `this.container.dispatchEvent()`, `updateUrlbarButton.arm()`

## MozTabSplitViewWrapper.#suspend()
- 位置: L277-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabpanels.suspendSplitViewPanels()`, `this.#tabs.filter()`, `this.container.dispatchEvent()`, `updateUrlbarButton.arm()`

## MozTabSplitViewWrapper.#resetPanelWidths()
- 位置: L294-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.getAttribute()`
- 条件付き依存: `if (width)` → `this.#storedPanelWidths.set()`
- 条件付き依存: `if (width)` → `panel.removeAttribute()`
- 条件付き依存: `if (width)` → `panel.style.removeProperty()`

## MozTabSplitViewWrapper.#restorePanelWidths()
- 位置: L308-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#storedPanelWidths.get()`
- 条件付き依存: `if (width)` → `panel.setAttribute()`
- 条件付き依存: `if (width)` → `panel.style.setProperty()`

## MozTabSplitViewWrapper.resetRightPanelWidth()
- 位置: L322-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.removeAttribute()`, `panel.style.removeProperty()`, `this.#storedPanelWidths.delete()`

## MozTabSplitViewWrapper.addTabs()
- 位置: L337-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.adoptTab()`, `gBrowser.moveTabToSplitView()`, `gBrowser.tabs.at()`, `isBlankPageURL()`, `this.appendChild()`
- 条件付き依存: `if (!(indexOfReplacedTab > -1 && indexOfReplacedTab < this.#tabs.length))` → `this.#tabs.push()`
- 条件付き依存: `if (this.hasActiveTab)` → `this.#activate()`
- 条件付き依存: `if (!isBlankPageURL(tabURI) && tabURI !== "about:opentabs")` → `tabs.indexOf()`
- 条件付き依存: `if (!isBlankPageURL(tabURI) && tabURI !== "about:opentabs")` → `String()`
- 条件付き依存: `if (!isBlankPageURL(tabURI) && tabURI !== "about:opentabs")` → `Glean.splitview.uriCount[label].add()`

## MozTabSplitViewWrapper.unsplitTabs()
- 位置: L386-420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aboutOpenTabs.forEach()`, `gBrowser.handleTabMove()`, `gBrowser.removeTab()`, `gBrowser.tabContainer.insertBefore()`, `this.#tabs.filter()`
- 条件付き依存: `if (telemetryTrigger)` → `Glean.splitview.end.record()`

## MozTabSplitViewWrapper.replaceTab()
- 位置: L425-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.removeTab()`, `this.#activate()`, `this.addTabs()`, `this.tabs.indexOf()`

## MozTabSplitViewWrapper.reverseTabs()
- 位置: L446-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.moveTabBefore()`
- 条件付き依存: `if (this.hasActiveTab)` → `gBrowser.showSplitViewPanels()`
- 条件付き依存: `if (this.hasActiveTab)` → `updateUrlbarButton.arm()`
- 条件付き依存: `if (trigger)` → `Glean.splitview.reverse.record()`

## MozTabSplitViewWrapper.close()
- 位置: L469-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.removeTabs()`
- 条件付き依存: `if (trigger)` → `Glean.splitview.end.record()`

## MozTabSplitViewWrapper.on_TabSelect()
- 位置: L487-498
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.hasActiveTab)` → `this.#activate()`
- 条件付き依存: `if (wasActive && !event.detail.previousTabInAdoptedSplitView)` → `this.#suspend()`
