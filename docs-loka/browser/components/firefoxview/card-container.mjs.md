# browser/components/firefoxview/card-container.mjs

source: browser/components/firefoxview/card-container.mjs
source-hash: 7967758d51000fedfe63bb12718f94e65747e85b
lines: 204

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## CardContainer.constructor()
- 位置: L27-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.initiallyExpanded`, `this.isExpanded`, `this.visible`

## CardContainer.detailsExpanded()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.detailsEl.hasAttribute()`

## CardContainer.detailsOpenPrefValue()
- 位置: L59-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (prefName && Services.prefs.prefHasUserValue(prefName))` → `Services.prefs.getBoolPref()`
- 参照: `this.shortPageName`
- XPCOM: `Services.prefs`

## CardContainer.connectedCallback()
- 位置: L69-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 参照: `this.detailsOpenPrefValue`, `this.initiallyExpanded`, `this.isExpanded`

## CardContainer.onToggleContainer()
- 位置: L74-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext[ `card${this.isExpanded ? "Expanded" : "Collapsed"}CardContainer` ].record()`, `this.updateTabLists()`
- 条件付き依存: `if (this.preserveCollapseState)` → `Services.prefs.setBoolPref()`
- 参照: `Glean.firefoxviewNext`, `this.detailsExpanded`, `this.isExpanded`, `this.preserveCollapseState`, `this.shortPageName`
- XPCOM: `Services.prefs`

## CardContainer.viewAllClicked()
- 位置: L101-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## CardContainer.willUpdate()
- 位置: L110-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changes.has()`
- 条件付き依存: `if (changes.has("visible"))` → `this.updateTabLists()`

## CardContainer.updateTabLists()
- 位置: L116-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelectorAll()`
- 条件付き依存: `if (tabLists)` → `tabLists.forEach()`
- 参照: `tabList.updatesPaused`, `this.isExpanded`, `this.visible`

## CardContainer.render()
- 位置: L127-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `when()`
- 参照: `this.hideHeader`, `this.isEmptyState`, `this.isExpanded`, `this.isInnerCard`, `this.onToggleContainer`, `this.removeBlockEndMargin`, `this.shortPageName`, `this.showViewAll`, `this.toggleDisabled`, `this.viewAllClicked`
