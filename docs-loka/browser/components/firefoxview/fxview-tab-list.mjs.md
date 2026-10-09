# browser/components/firefoxview/fxview-tab-list.mjs

source: browser/components/firefoxview/fxview-tab-list.mjs
source-hash: f3a742cbbdd6033cbbbafef3882b9d2501a7e0ff
lines: 1074

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## FxviewTabListBase.constructor()
- 位置: L52-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#register()`, `window.MozXULElement.insertFTLIfNeeded()`
- 参照: `this.activeIndex`, `this.compactRows`, `this.currentActiveElementId`, `this.dateTimeFormat`, `this.hasPopup`, `this.maxTabsLength`, `this.tabItems`, `this.updatesPaused`

## FxviewTabListBase.willUpdate()
- 位置: L90-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `changes.has()`
- 条件付き依存: `if (changes.has("dateTimeFormat") || changes.has("updatesPaused"))` → `this.clearIntervalTimer()`
- 条件付き依存: `if ( !this.updatesPaused && this.dateTimeFormat == "relative" && !window.IS_STORYBOOK )` → `this.startIntervalTimer()`
- 条件付き依存: `if ( !this.updatesPaused && this.dateTimeFormat == "relative" && !window.IS_STORYBOOK )` → `this.onIntervalUpdate()`
- 条件付き依存: `if (this.maxTabsLength > 0)` → `this.tabItems.slice()`
- 参照: `this.activeIndex`, `this.dateTimeFormat`, `this.maxTabsLength`, `this.tabItems`, `this.tabItems.length`, `this.updatesPaused`, `window.IS_STORYBOOK`

## FxviewTabListBase.startIntervalTimer()
- 位置: L113-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setInterval()`, `this.clearIntervalTimer()`, `this.onIntervalUpdate()`
- 参照: `this.intervalID`, `this.timeMsPref`

## FxviewTabListBase.clearIntervalTimer()
- 位置: L121-126
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.intervalID)` → `clearInterval()`
- 参照: `this.intervalID`

## FxviewTabListBase.#register()
- 位置: L128-145
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!window.IS_STORYBOOK)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (!window.IS_STORYBOOK)` → `this.clearIntervalTimer()`
- 条件付き依存: `if (!window.IS_STORYBOOK)` → `this.startIntervalTimer()`
- 条件付き依存: `if (!window.IS_STORYBOOK)` → `this.requestUpdate()`
- 参照: `this.isConnected`, `window.IS_STORYBOOK`

## FxviewTabListBase.connectedCallback()
- 位置: L147-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 条件付き依存: `if ( !this.updatesPaused && this.dateTimeFormat === "relative" && !window.IS_STORYBOOK )` → `this.startIntervalTimer()`
- 参照: `this.dateTimeFormat`, `this.updatesPaused`, `window.IS_STORYBOOK`

## FxviewTabListBase.disconnectedCallback()
- 位置: L158-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.clearIntervalTimer()`

## FxviewTabListBase.getUpdateComplete()
- 位置: async L163-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.rowEls).map()`, `Promise.all()`, `super.getUpdateComplete()`
- 参照: `item.updateComplete`, `this.rowEls`

## FxviewTabListBase.onIntervalUpdate()
- 位置: L168-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.rowEls).forEach()`, `fxviewTabRow.requestUpdate()`, `this.requestUpdate()`
- 参照: `this.rowEls`

## FxviewTabListBase.handleFocusElementInRow()
- 位置: L179-208
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.code == "ArrowUp")` → `e.preventDefault()`
- 条件付き依存: `if (e.code == "ArrowUp")` → `this.focusPrevRow()`
- 条件付き依存: `if (e.code == "ArrowDown")` → `e.preventDefault()`
- 条件付き依存: `if (e.code == "ArrowDown")` → `this.focusNextRow()`
- 条件付き依存: `if (e.code == "ArrowRight")` → `e.preventDefault()`
- 条件付き依存: `if (document.dir == "rtl")` → `fxviewTabRow.moveFocusLeft()`
- 条件付き依存: `if (!(document.dir == "rtl"))` → `fxviewTabRow.moveFocusRight()`
- 条件付き依存: `if (e.code == "ArrowLeft")` → `e.preventDefault()`
- 条件付き依存: `if (document.dir == "rtl")` → `fxviewTabRow.moveFocusRight()`
- 条件付き依存: `if (!(document.dir == "rtl"))` → `fxviewTabRow.moveFocusLeft()`
- 参照: `document.dir`, `e.code`, `e.target`

## FxviewTabListBase.focusPrevRow()
- 位置: L210-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focusIndex()`
- 参照: `this.activeIndex`

## FxviewTabListBase.focusNextRow()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focusIndex()`
- 参照: `this.activeIndex`

## FxviewTabListBase.focusIndex()
- 位置: async L218-238
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (index >= 0 && index < this.rowEls?.length)` → `this.rootVirtualListEl.getItem()`
- 条件付き依存: `if (index >= 0 && index < this.rowEls?.length)` → `this.rootVirtualListEl.getSubListForItem()`
- 条件付き依存: `if (index >= 0 && index < this.rowEls?.length)` → `this.requestVirtualListUpdate()`
- 条件付き依存: `if (index >= 0 && index < this.rowEls?.length)` → `row.scrollIntoView()`
- 条件付き依存: `if (index >= 0 && index < this.rowEls?.length)` → `row.focus()`
- 参照: `this.activeIndex`, `this.rowEls?.length`

## FxviewTabListBase.requestVirtualListUpdate()
- 位置: async L240-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `sublist.requestUpdate()`, `updates.push()`
- 参照: `sublist.updateComplete`, `this.rootVirtualListEl.children`

## FxviewTabListBase.shouldUpdate()
- 位置: L249-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changes.has()`
- 条件付き依存: `if (this.updatesPaused)` → `this.clearIntervalTimer()`
- 参照: `this.updatesPaused`

## FxviewTabListBase.itemTemplate()
- 位置: L258-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (tabItem.time || tabItem.closedAt)` → `(tabItem.time || tabItem.closedAt).toString()`
- 参照: `stringTime.length`, `tabItem.closedAt`, `tabItem.closedId`, `tabItem.icon`, `tabItem.primaryL10nArgs`, `tabItem.primaryL10nId`, `tabItem.secondaryL10nArgs`, `tabItem.secondaryL10nId`, `tabItem.sourceClosedId`, `tabItem.sourceWindowId`, `tabItem.tabElement`, `tabItem.tertiaryL10nArgs`, `tabItem.tertiaryL10nId`, `tabItem.time`, `tabItem.title`, `tabItem.url`, `this.activeIndex`, `this.compactRows`, `this.currentActiveElementId`, `this.dateTimeFormat`, `this.hasPopup`, `this.searchQuery`, `this.secondaryActionClass`, `this.tertiaryActionClass`, `this.timeMsPref`

## FxviewTabListBase.stylesheets()
- 位置: L301-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## FxviewTabListBase.render()
- 位置: L308-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.stylesheets()`
- 条件付き依存: `if (this.searchQuery && !this.tabItems.length)` → `this.emptySearchResultsTemplate()`
- 参照: `this.activeIndex`, `this.getItemHeight`, `this.handleFocusElementInRow`, `this.itemTemplate`, `this.searchQuery`, `this.tabItems`, `this.tabItems.length`

## FxviewTabListBase.emptySearchResultsTemplate()
- 位置: L331-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `escapeHtmlEntities()`, `html()`
- 参照: `this.searchQuery`

## FxviewTabRowBase.constructor()
- 位置: L398-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.active`, `this.currentActiveElementId`

## FxviewTabRowBase.currentFocusable()
- 位置: L410-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.getElementById()`
- 条件付き依存: `if (!focusItem)` → `this.renderRoot.getElementById()`
- 参照: `this.currentActiveElementId`

## FxviewTabRowBase.connectedCallback()
- 位置: L418-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 参照: `this.uri`, `this.url`

## FxviewTabRowBase.focus()
- 位置: L423-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.currentFocusable.focus()`

## FxviewTabRowBase.focusSecondaryButton()
- 位置: L427-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.secondaryButtonEl.focus()`
- 参照: `tabList.currentActiveElementId`, `this.getRootNode().host`, `this.secondaryButtonEl.id`

## FxviewTabRowBase.focusTertiaryButton()
- 位置: L433-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.tertiaryButtonEl.focus()`
- 参照: `tabList.currentActiveElementId`, `this.getRootNode().host`, `this.tertiaryButtonEl.id`

## FxviewTabRowBase.focusLink()
- 位置: L439-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRootNode()`, `this.mainEl.focus()`
- 参照: `tabList.currentActiveElementId`, `this.getRootNode().host`, `this.mainEl.id`

## FxviewTabRowBase.moveFocusRight()
- 位置: L445-454
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.currentActiveElementId === "fxview-tab-row-main")` → `this.focusSecondaryButton()`
- 条件付き依存: `if ( this.tertiaryButtonEl && this.currentActiveElementId === "fxview-tab-row-secondary-button" )` → `this.focusTertiaryButton()`
- 参照: `this.currentActiveElementId`, `this.tertiaryButtonEl`

## FxviewTabRowBase.moveFocusLeft()
- 位置: L456-462
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.currentActiveElementId === "fxview-tab-row-tertiary-button")` → `this.focusSecondaryButton()`
- 条件付き依存: `if (!(this.currentActiveElementId === "fxview-tab-row-tertiary-button"))` → `this.focusLink()`
- 参照: `this.currentActiveElementId`

## FxviewTabRowBase.dateFluentArgs()
- 位置: L464-469
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dateTimeFormat === "date" || dateTimeFormat === "dateTime")` → `JSON.stringify()`

## FxviewTabRowBase.dateFluentId()
- 位置: L471-486
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dateTimeFormat === "relative")` → `Date.now()`
- 参照: `lazy.relativeTimeFormat`

## FxviewTabRowBase.relativeTime()
- 位置: L488-496
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dateTimeFormat === "relative")` → `Date.now()`
- 条件付き依存: `if (elapsed > _nowThresholdMs && lazy.relativeTimeFormat)` → `lazy.relativeTimeFormat.formatBestUnit()`
- 参照: `lazy.relativeTimeFormat`

## FxviewTabRowBase.timeFluentId()
- 位置: L498-503
- 役割: (未記入)
- 触るとき: (未記入)

## FxviewTabRowBase.formatURIForDisplay()
- 位置: L505-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.formatURIStringForDisplay()`
- 参照: `window.IS_STORYBOOK`

## FxviewTabRowBase.getImageUrl()
- 位置: L513-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.startsWith()`
- 条件付き依存: `if (!icon)` → `targetURI?.startsWith()`
- 参照: `window.IS_STORYBOOK`

## FxviewTabRowBase.primaryActionHandler()
- 位置: L533-550
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (event.type == "click" && !event.altKey) || (event.type == "keydown" && event.code == "Enter") || (event.type == "keydown" && event.code == "Space") )` → `event.preventDefault()`
- 条件付き依存: `if (!window.IS_STORYBOOK)` → `this.dispatchEvent()`
- 参照: `event.altKey`, `event.code`, `event.type`, `window.IS_STORYBOOK`

## FxviewTabRowBase.secondaryActionHandler()
- 位置: L552-567
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (event.type == "click" && event.detail && !event.altKey) || // detail=0 is from keyboard (event.type == "click" && !event.detail) )` → `event.preventDefault()`
- 条件付き依存: `if ( (event.type == "click" && event.detail && !event.altKey) || // detail=0 is from keyboard (event.type == "click" && !event.detail) )` → `this.dispatchEvent()`
- 参照: `event.altKey`, `event.detail`, `event.type`

## FxviewTabRowBase.tertiaryActionHandler()
- 位置: L569-584
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (event.type == "click" && event.detail && !event.altKey) || // detail=0 is from keyboard (event.type == "click" && !event.detail) )` → `event.preventDefault()`
- 条件付き依存: `if ( (event.type == "click" && event.detail && !event.altKey) || // detail=0 is from keyboard (event.type == "click" && !event.detail) )` → `this.dispatchEvent()`
- 参照: `event.altKey`, `event.detail`, `event.type`

## FxviewTabRowBase.auxActionHandler()
- 位置: L586-599
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "auxclick" && event.button == 1)` → `event.preventDefault()`
- 条件付き依存: `if (!window.IS_STORYBOOK)` → `this.dispatchEvent()`
- 参照: `event.button`, `event.type`, `window.IS_STORYBOOK`

## FxviewTabRowBase.highlightSearchMatches()
- 位置: L608-623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RegExp()`, `escapeRegExp()`, `fragments.push()`, `html()`, `regex.exec()`, `string.substring()`
- 参照: `regex.lastIndex`, `result.indices`

## FxviewTabRowBase.stylesheets()
- 位置: L625-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## FxviewTabRowBase.faviconTemplate()
- 位置: L632-640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `styleMap()`, `this.getImageUrl()`
- 参照: `this.favicon`, `this.url`

## FxviewTabRowBase.titleTemplate()
- 位置: L642-655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.highlightSearchMatches()`, `when()`
- 参照: `this.searchQuery`, `this.title`

## FxviewTabRowBase.urlTemplate()
- 位置: L657-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.formatURIForDisplay()`, `this.highlightSearchMatches()`, `when()`
- 参照: `this.searchQuery`, `this.url`

## FxviewTabRowBase.dateTemplate()
- 位置: L674-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.dateFluentArgs()`, `this.dateFluentId()`, `this.relativeTime()`
- 参照: `this.dateTimeFormat`, `this.time`, `this.timeMsPref`, `window.IS_STORYBOOK`

## FxviewTabRowBase.timeTemplate()
- 位置: L696-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `ifDefined()`, `this.timeFluentId()`
- 参照: `this.dateTimeFormat`, `this.time`

## FxviewTabRowBase.getIconSrc()
- 位置: L711-728
- 役割: (未記入)
- 触るとき: (未記入)

## FxviewTabRowBase.secondaryButtonTemplate()
- 位置: L730-752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `this.getIconSrc()`, `when()`
- 参照: `this.active`, `this.currentActiveElementId`, `this.hasPopup`, `this.secondaryActionClass`, `this.secondaryActionHandler`, `this.secondaryL10nArgs`, `this.secondaryL10nId`

## FxviewTabRowBase.tertiaryButtonTemplate()
- 位置: L754-776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `this.getIconSrc()`, `when()`
- 参照: `this.active`, `this.currentActiveElementId`, `this.hasPopup`, `this.tertiaryActionClass`, `this.tertiaryActionHandler`, `this.tertiaryL10nArgs`, `this.tertiaryL10nId`

## FxviewTabRow.render()
- 位置: L780-807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.dateTemplate()`, `this.faviconTemplate()`, `this.secondaryButtonTemplate()`, `this.stylesheets()`, `this.tertiaryButtonTemplate()`, `this.timeTemplate()`, `this.titleTemplate()`, `this.urlTemplate()`, `when()`
- 参照: `this.active`, `this.compact`, `this.currentActiveElementId`, `this.primaryActionHandler`, `this.primaryL10nArgs`, `this.primaryL10nId`, `this.url`

## VirtualList.createRenderRoot()
- 位置: L827-829
- 役割: (未記入)
- 触るとき: (未記入)

## VirtualList.constructor()
- 位置: L831-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.max()`, `super()`, `this.triggerIntersectionObserver()`
- 条件付き依存: `if (!this.isSubList)` → `requestAnimationFrame()`
- 条件付き依存: `if (!this.isSubList)` → `this.#syncSublistVisibility()`
- 参照: `entry.contentRect.height`, `entry.contentRect?.height`, `entry.isIntersecting`, `this.activeIndex`, `this.childResizeObserver`, `this.children.length`, `this.getItemHeight`, `this.intersectionObserver`, `this.isSubList`, `this.isVisible`, `this.itemHeightEstimate`, `this.itemOffset`, `this.items`, `this.maxRenderCountEstimate`, `this.ownerDocument`, `this.parentElement.itemHeightEstimate`, `this.pinnedTabsIndexOffset`, `this.selfResizeObserver`, `this.subListItems`, `window.innerHeight`

## VirtualList.connectedCallback()
- 位置: L889-901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 条件付き依存: `if (!this.isSubList)` → `document.addEventListener()`
- 参照: `this._scrollHandler`, `this.isSubList`

## this._scrollHandler()
- 位置: L892-892
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#syncSublistVisibility()`

## VirtualList.disconnectedCallback()
- 位置: L903-914
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.childResizeObserver.disconnect()`, `this.intersectionObserver.disconnect()`, `this.selfResizeObserver.disconnect()`
- 条件付き依存: `if (this._scrollHandler)` → `document.removeEventListener()`
- 参照: `this._scrollHandler`

## VirtualList.#syncSublistVisibility()
- 位置: L916-930
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.getBoundingClientRect()`
- 参照: `child.isAlwaysVisible`, `child.isSubList`, `child.isVisible`, `this.children`, `window.innerHeight`

## VirtualList.triggerIntersectionObserver()
- 位置: L932-935
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.intersectionObserver.observe()`, `this.intersectionObserver.unobserve()`

## VirtualList.getSubListForItem()
- 位置: L937-942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`
- 参照: `this.children`, `this.isSubList`, `this.maxRenderCountEstimate`

## VirtualList.getItem()
- 位置: L944-951
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.isSubList)` → `this.getSubListForItem(index)?.getItem()`
- 条件付き依存: `if (!this.isSubList)` → `this.getSubListForItem()`
- 参照: `this.children`, `this.isSubList`, `this.maxRenderCountEstimate`

## VirtualList.willUpdate()
- 位置: L953-981
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.get()`, `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("items") && !this.isSubList)` → `this.subListItems.push()`
- 条件付き依存: `if (changedProperties.has("items") && !this.isSubList)` → `this.items.slice()`
- 参照: `this._knownHeight`, `this.isSubList`, `this.isVisible`, `this.items.length`, `this.maxRenderCountEstimate`, `this.scrollHeight`, `this.subListItems`

## VirtualList.recalculateAfterWindowResize()
- 位置: L983-991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.max()`
- 参照: `this.itemHeightEstimate`, `this.maxRenderCountEstimate`, `window.innerHeight`

## VirtualList.firstUpdated()
- 位置: L993-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.intersectionObserver.observe()`, `this.selfResizeObserver.observe()`
- 条件付き依存: `if (this.isSubList)` → `this.childResizeObserver.observe()`
- 条件付き依存: `if (!(this.isSubList))` → `requestAnimationFrame()`
- 条件付き依存: `if (!(this.isSubList))` → `this.#syncSublistVisibility()`
- 参照: `this.isSubList`

## VirtualList.updated()
- 位置: L1004-1012
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `this.updateListHeight()`
- 条件付き依存: `if (changedProperties.has("items") && !this.isSubList)` → `this.triggerIntersectionObserver()`
- 条件付き依存: `if (changedProperties.has("items") && !this.isSubList)` → `requestAnimationFrame()`
- 条件付き依存: `if (changedProperties.has("items") && !this.isSubList)` → `this.#syncSublistVisibility()`
- 参照: `this.isSubList`

## VirtualList.updateListHeight()
- 位置: L1014-1027
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if ( changedProperties.has("isAlwaysVisible") || changedProperties.has("isVisible") || changedProperties.has("itemHeightEstimate") || changedProperties.has("getI...)` → `this.#getPlaceholderHeight()`
- 参照: `this._knownHeight`, `this.isAlwaysVisible`, `this.isVisible`, `this.style.height`

## VirtualList.#getPlaceholderHeight()
- 位置: L1029-1037
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.getItemHeight)` → `this.items.reduce()`
- 条件付き依存: `if (this.getItemHeight)` → `this.getItemHeight()`
- 参照: `this.getItemHeight`, `this.itemHeightEstimate`, `this.items.length`

## VirtualList.renderItems()
- 位置: L1039-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isSubList`, `this.items`, `this.subListItems`

## VirtualList.subListTemplate()
- 位置: L1043-1055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `parseInt()`
- 参照: `this.activeIndex`, `this.getItemHeight`, `this.itemHeightEstimate`, `this.maxRenderCountEstimate`, `this.pinnedTabsIndexOffset`, `this.template`

## VirtualList.itemTemplate()
- 位置: L1057-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.template()`
- 参照: `this.itemOffset`, `this.pinnedTabsIndexOffset`

## VirtualList.render()
- 位置: L1060-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isAlwaysVisible || this.isVisible)` → `html()`
- 条件付き依存: `if (this.isAlwaysVisible || this.isVisible)` → `repeat()`
- 参照: `this.isAlwaysVisible`, `this.isSubList`, `this.isVisible`, `this.itemTemplate`, `this.renderItems`, `this.subListTemplate`
