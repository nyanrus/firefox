# browser/components/firefoxview/opentabs-tab-list.mjs

source: browser/components/firefoxview/opentabs-tab-list.mjs
source-hash: a29a0371fd2110e2289c0bc2f997fd95b015fe80
lines: 572

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## OpenTabsTabList.constructor()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.pinnedTabs`, `this.pinnedTabsGridView`, `this.unpinnedTabs`

## OpenTabsTabList.willUpdate()
- 位置: L44-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `changes.has()`
- 条件付き依存: `if (changes.has("dateTimeFormat") || changes.has("updatesPaused"))` → `this.clearIntervalTimer()`
- 条件付き依存: `if (!this.updatesPaused && this.dateTimeFormat == "relative")` → `this.startIntervalTimer()`
- 条件付き依存: `if (!this.updatesPaused && this.dateTimeFormat == "relative")` → `this.onIntervalUpdate()`
- 条件付き依存: `if (this.pinnedTabsGridView)` → `this.tabItems.filter()`
- 条件付き依存: `if (this.pinnedTabsGridView)` → `tab.indicators.includes()`
- 条件付き依存: `if (this.maxTabsLength > 0)` → `this.unpinnedTabs.slice()`
- 条件付き依存: `if (this.maxTabsLength > 0)` → `this.tabItems.slice()`
- 参照: `this.activeIndex`, `this.dateTimeFormat`, `this.maxTabsLength`, `this.pinnedTabs`, `this.pinnedTabsGridView`, `this.tabItems`, `this.tabItems.length`, `this.unpinnedTabs`, `this.updatesPaused`

## OpenTabsTabList.handleFocusElementInRow()
- 位置: L80-122
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.code == "ArrowUp")` → `e.preventDefault()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && this.activeIndex >= this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `this.focusPrevRow()`
- 条件付き依存: `if (e.code == "ArrowDown")` → `e.preventDefault()`
- 条件付き依存: `if ( this.pinnedTabsGridView && this.activeIndex < this.pinnedTabs.length )` → `this.focusIndex()`
- 条件付き依存: `if (!( this.pinnedTabsGridView && this.activeIndex < this.pinnedTabs.length ))` → `this.focusNextRow()`
- 条件付き依存: `if (e.code == "ArrowRight")` → `e.preventDefault()`
- 条件付き依存: `if (document.dir == "rtl")` → `fxviewTabRow.moveFocusLeft()`
- 条件付き依存: `if (!(document.dir == "rtl"))` → `fxviewTabRow.moveFocusRight()`
- 条件付き依存: `if (e.code == "ArrowLeft")` → `e.preventDefault()`
- 条件付き依存: `if (document.dir == "rtl")` → `fxviewTabRow.moveFocusRight()`
- 条件付き依存: `if (!(document.dir == "rtl"))` → `fxviewTabRow.moveFocusLeft()`
- 参照: `document.dir`, `e.code`, `e.target`, `this.activeIndex`, `this.pinnedTabs.length`, `this.pinnedTabsGridView`

## OpenTabsTabList.focusIndex()
- 位置: async L124-155
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (this.pinnedTabsGridView && index > this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `this.rootVirtualListEl.getItem()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && index > this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `this.rootVirtualListEl.getSubListForItem()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && index > this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `Array.from()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && index > this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `sublist.requestUpdate()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && index > this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `row.scrollIntoView()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && index > this.pinnedTabs.length) || !this.pinnedTabsGridView )` → `row.focus()`
- 条件付き依存: `if (index >= 0 && index < this.rowEls?.length)` → `this.rowEls[index].focus()`
- 参照: `sublist.updateComplete`, `this.activeIndex`, `this.pinnedTabs.length`, `this.pinnedTabsGridView`, `this.rootVirtualListEl.children`, `this.rowEls`, `this.rowEls?.length`

## OpenTabsTabList.#getTabListWrapperClasses()
- 位置: L157-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabsToCheck.some()`
- 条件付き依存: `if (tabsToCheck.some(tab => tab.containerObj))` → `wrapperClasses.push()`
- 参照: `tab.containerObj`, `this.pinnedTabsGridView`, `this.tabItems`, `this.unpinnedTabs`

## OpenTabsTabList.itemTemplate()
- 位置: L168-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `tabItem.indicators?.includes()`
- 条件付き依存: `if (tabItem.time || tabItem.closedAt)` → `(tabItem.time || tabItem.closedAt).toString()`
- 参照: `stringTime.length`, `tabItem.closedAt`, `tabItem.closedId`, `tabItem.containerObj`, `tabItem.icon`, `tabItem.indicators`, `tabItem.pinned`, `tabItem.primaryL10nArgs`, `tabItem.primaryL10nId`, `tabItem.secondaryL10nArgs`, `tabItem.secondaryL10nId`, `tabItem.sourceClosedId`, `tabItem.sourceWindowId`, `tabItem.tabElement`, `tabItem.tertiaryL10nArgs`, `tabItem.tertiaryL10nId`, `tabItem.time`, `tabItem.title`, `tabItem.url`, `this.activeIndex`, `this.compactRows`, `this.currentActiveElementId`, `this.dateTimeFormat`, `this.hasPopup`, `this.pinnedTabsGridView`, `this.searchQuery`, `this.secondaryActionClass`, `this.tertiaryActionClass`, `this.timeMsPref`

## OpenTabsTabList.render()
- 位置: L216-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#getTabListWrapperClasses()`, `this.#getTabListWrapperClasses().join()`, `this.customItemTemplate()`, `this.itemTemplate()`, `this.pinnedTabs.map()`, `this.stylesheets()`, `when()`
- 条件付き依存: `if (this.searchQuery && this.tabItems.length === 0)` → `this.emptySearchResultsTemplate()`
- 参照: `this.activeIndex`, `this.customItemTemplate`, `this.handleFocusElementInRow`, `this.itemTemplate`, `this.pinnedTabs.length`, `this.pinnedTabsGridView`, `this.searchQuery`, `this.tabItems`, `this.tabItems.length`, `this.unpinnedTabs`

## OpenTabsTabRow.constructor()
- 位置: L275-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.indicators`, `this.pinnedTabsGridView`

## OpenTabsTabRow.connectedCallback()
- 位置: L294-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`
- 参照: `this.handleKeydown`

## OpenTabsTabRow.disconnectedCallback()
- 位置: L299-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this.handleKeydown`

## OpenTabsTabRow.handleKeydown()
- 位置: L304-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.indicators?.includes()`
- 条件付き依存: `if ( this.active && this.pinnedTabsGridView && this.indicators?.includes("pinned") && e.key === "m" && e.ctrlKey )` → `this.muteOrUnmuteTab()`
- 参照: `e.ctrlKey`, `e.key`, `this.active`, `this.pinnedTabsGridView`

## OpenTabsTabRow.moveFocusRight()
- 位置: L316-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.indicators?.includes()`
- 条件付き依存: `if (this.pinnedTabsGridView && this.indicators?.includes("pinned"))` → `tabList.focusNextRow()`
- 条件付き依存: `if (!(this.pinnedTabsGridView && this.indicators?.includes("pinned")))` → `this.indicators?.includes()`
- 条件付き依存: `if ( (this.indicators?.includes("soundplaying") || this.indicators?.includes("muted")) && this.currentActiveElementId === "fxview-tab-row-main" )` → `this.focusMediaButton()`
- 条件付き依存: `if ( this.currentActiveElementId === "fxview-tab-row-media-button" || this.currentActiveElementId === "fxview-tab-row-main" )` → `this.focusSecondaryButton()`
- 条件付き依存: `if ( this.tertiaryButtonEl && this.currentActiveElementId === "fxview-tab-row-secondary-button" )` → `this.focusTertiaryButton()`
- 参照: `this.currentActiveElementId`, `this.getRootNode().host`, `this.pinnedTabsGridView`, `this.tertiaryButtonEl`

## OpenTabsTabRow.moveFocusLeft()
- 位置: L339-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.indicators?.includes()`
- 条件付き依存: `if ( this.pinnedTabsGridView && (this.indicators?.includes("pinned") || (tabList.currentActiveElementId === "fxview-tab-row-main" && tabList.activeIndex === tabL...)` → `tabList.focusPrevRow()`
- 条件付き依存: `if ( tabList.currentActiveElementId === "fxview-tab-row-tertiary-button" )` → `this.focusSecondaryButton()`
- 条件付き依存: `if (!( tabList.currentActiveElementId === "fxview-tab-row-tertiary-button" ))` → `this.indicators?.includes()`
- 条件付き依存: `if ( (this.indicators?.includes("soundplaying") || this.indicators?.includes("muted")) && tabList.currentActiveElementId === "fxview-tab-row-secondary-button" )` → `this.focusMediaButton()`
- 条件付き依存: `if (!( (this.indicators?.includes("soundplaying") || this.indicators?.includes("muted")) && tabList.currentActiveElementId === "fxview-tab-row-secondary-button" ))` → `this.focusLink()`
- 参照: `tabList.activeIndex`, `tabList.currentActiveElementId`, `tabList.pinnedTabs.length`, `this.getRootNode().host`, `this.pinnedTabsGridView`

## OpenTabsTabRow.focusMediaButton()
- 位置: L363-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.mediaButtonEl.focus()`
- 参照: `tabList.currentActiveElementId`, `this.getRootNode().host`, `this.mediaButtonEl.id`

## OpenTabsTabRow.#secondaryActionHandler()
- 位置: L369-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.indicators?.includes()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && this.indicators?.includes("pinned") && event.type == "contextmenu") || (event.type == "click" && event.detail && !event.altKey) ...)` → `event.preventDefault()`
- 条件付き依存: `if ( (this.pinnedTabsGridView && this.indicators?.includes("pinned") && event.type == "contextmenu") || (event.type == "click" && event.detail && !event.altKey) ...)` → `this.dispatchEvent()`
- 参照: `event.altKey`, `event.detail`, `event.type`, `this.pinnedTabsGridView`

## OpenTabsTabRow.#faviconTemplate()
- 位置: L389-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `styleMap()`, `this.getImageUrl()`, `this.indicators?.includes()`, `when()`
- 参照: `this.favicon`, `this.muteOrUnmuteTab`, `this.pinnedTabsGridView`, `this.url`

## OpenTabsTabRow.#getContainerClasses()
- 位置: L429-437
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.containerObj)` → `containerClasses.push()`
- 参照: `this.containerObj`

## OpenTabsTabRow.muteOrUnmuteTab()
- 位置: L439-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e?.preventDefault()`, `this.indicators.includes()`, `this.tabElement.toggleMuteAudio()`
- 条件付き依存: `if (document.dir == "rtl")` → `this.moveFocusLeft()`
- 条件付き依存: `if (!(document.dir == "rtl"))` → `this.moveFocusRight()`
- 参照: `document.dir`, `e?.detail`, `e?.type`, `this.currentActiveElementId`, `this.mediaButtonEl`, `this.pinnedTabsGridView`

## OpenTabsTabRow.#mediaButtonTemplate()
- 位置: L462-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.indicators?.includes()`, `when()`
- 参照: `this.active`, `this.currentActiveElementId`, `this.muteOrUnmuteTab`

## OpenTabsTabRow.#containerIndicatorTemplate()
- 位置: L487-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `tabsToCheck.some()`, `this.#getContainerClasses()`, `this.#getContainerClasses().join()`, `this.getRootNode()`, `when()`
- 参照: `tab.containerObj`, `tabList.pinnedTabsGridView`, `tabList.tabItems`, `tabList.unpinnedTabs`, `this.getRootNode().host`

## OpenTabsTabRow.#pinnedTabItemTemplate()
- 位置: L498-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.#faviconTemplate()`
- 参照: `this.#secondaryActionHandler`, `this.active`, `this.currentActiveElementId`, `this.hasPopup`, `this.primaryActionHandler`, `this.primaryL10nArgs`, `this.primaryL10nId`

## OpenTabsTabRow.#unpinnedTabItemTemplate()
- 位置: L520-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.#containerIndicatorTemplate()`, `this.#faviconTemplate()`, `this.#mediaButtonTemplate()`, `this.dateTemplate()`, `this.secondaryButtonTemplate()`, `this.tertiaryButtonTemplate()`, `this.timeTemplate()`, `this.titleTemplate()`, `this.urlTemplate()`, `when()`
- 参照: `this.active`, `this.compact`, `this.currentActiveElementId`, `this.primaryActionHandler`, `this.primaryL10nArgs`, `this.primaryL10nId`, `this.url`

## OpenTabsTabRow.render()
- 位置: L547-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#pinnedTabItemTemplate.bind()`, `this.#unpinnedTabItemTemplate.bind()`, `this.indicators?.includes()`, `this.stylesheets()`, `when()`
- 参照: `this.containerObj`, `this.pinnedTabsGridView`
