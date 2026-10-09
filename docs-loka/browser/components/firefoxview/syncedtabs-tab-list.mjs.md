# browser/components/firefoxview/syncedtabs-tab-list.mjs

source: browser/components/firefoxview/syncedtabs-tab-list.mjs
source-hash: 451b66c022f632fb92527e6017cfadefe628ef12
lines: 177

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SyncedTabsTabList.constructor()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## SyncedTabsTabList.itemTemplate()
- 位置: L33-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `tabItem.canClose`, `tabItem.closeRequested`, `tabItem.closedId`, `tabItem.fxaDeviceId`, `tabItem.icon`, `tabItem.primaryL10nArgs`, `tabItem.primaryL10nId`, `tabItem.secondaryL10nArgs`, `tabItem.secondaryL10nId`, `tabItem.sourceClosedId`, `tabItem.sourceWindowId`, `tabItem.tabElement`, `tabItem.tertiaryActionClass`, `tabItem.tertiaryL10nArgs`, `tabItem.tertiaryL10nId`, `tabItem.time`, `tabItem.title`, `tabItem.url`, `this.activeIndex`, `this.compactRows`, `this.currentActiveElementId`, `this.dateTimeFormat`, `this.hasPopup`, `this.searchQuery`, `this.secondaryActionClass`, `this.timeMsPref`

## SyncedTabsTabList.stylesheets()
- 位置: L67-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `super.stylesheets()`

## SyncedTabsTabList.render()
- 位置: L77-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.stylesheets()`
- 条件付き依存: `if (this.searchQuery && !this.tabItems.length)` → `this.emptySearchResultsTemplate()`
- 参照: `this.activeIndex`, `this.handleFocusElementInRow`, `this.itemTemplate`, `this.searchQuery`, `this.tabItems`, `this.tabItems.length`

## SyncedTabsTabRow.constructor()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## SyncedTabsTabRow.secondaryButtonTemplate()
- 位置: L123-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.getIconSrc()`, `when()`
- 参照: `this.active`, `this.closeRequested`, `this.currentActiveElementId`, `this.hasPopup`, `this.secondaryActionClass`, `this.secondaryActionHandler`, `this.secondaryL10nArgs`, `this.secondaryL10nId`

## SyncedTabsTabRow.render()
- 位置: L145-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.dateTemplate()`, `this.faviconTemplate()`, `this.secondaryButtonTemplate()`, `this.stylesheets()`, `this.tertiaryButtonTemplate()`, `this.timeTemplate()`, `this.titleTemplate()`, `this.urlTemplate()`, `when()`
- 参照: `this.active`, `this.closeRequested`, `this.compact`, `this.currentActiveElementId`, `this.primaryActionHandler`, `this.primaryL10nArgs`, `this.primaryL10nId`, `this.url`
