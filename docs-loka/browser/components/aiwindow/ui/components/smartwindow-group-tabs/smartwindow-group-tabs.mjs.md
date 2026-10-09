# browser/components/aiwindow/ui/components/smartwindow-group-tabs/smartwindow-group-tabs.mjs

source: browser/components/aiwindow/ui/components/smartwindow-group-tabs/smartwindow-group-tabs.mjs
source-hash: baf5b9ef7ff4132108ba6621c19da0a9247d33c6
lines: 451

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## favicon()
- 位置: L21-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `e.target.src`, `info.iconUrl`

## SmartwindowGroupTabsCard.constructor()
- 位置: L48-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#onKeyDown()`, `this.addEventListener()`
- 参照: `this.computing`, `this.duplicates`, `this.recent`, `this.suggestions`, `this.tabGroups`

## SmartwindowGroupTabsCard.createRenderRoot()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)

## SmartwindowGroupTabsCard.connectedCallback()
- 位置: L62-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.classList.add()`, `this.setAttribute()`

## SmartwindowGroupTabsCard.#emit()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowGroupTabsCard.#favicons()
- 位置: L74-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `favicon()`, `html()`, `tabInfos.slice()`, `tabInfos.slice(0, 3).map()`

## SmartwindowGroupTabsCard.#rows()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelectorAll()`

## SmartwindowGroupTabsCard.#focusRowAt()
- 位置: L84-89
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (rows.length)` → `rows.at(index % rows.length)?.focus()`
- 条件付き依存: `if (rows.length)` → `rows.at()`
- 参照: `rows.length`, `this.#rows`

## SmartwindowGroupTabsCard.#moveRowFocus()
- 位置: L91-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#focusRowAt()`, `this.#rows.indexOf()`, `this.ownerDocument.activeElement?.closest()`
- 条件付き依存: `if (current < 0)` → `this.#focusRowAt()`

## SmartwindowGroupTabsCard.#onKeyDown()
- 位置: L102-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.#focusRowAt()`, `this.#moveRowFocus()`
- 参照: `event.altKey`, `event.ctrlKey`, `event.key`, `event.metaKey`, `event.shiftKey`

## SmartwindowGroupTabsCard.#emitPreview()
- 位置: L125-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`
- 参照: `event.currentTarget`

## SmartwindowGroupTabsCard.#onRowFocus()
- 位置: L133-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.currentTarget.hasAttribute()`, `this.#emitPreview()`

## SmartwindowGroupTabsCard.#onRowKeyDown()
- 位置: L140-145
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "ArrowRight" || event.key === "ArrowLeft")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "ArrowRight" || event.key === "ArrowLeft")` → `this.#emit()`
- 参照: `event.currentTarget`, `event.key`

## SmartwindowGroupTabsCard.#suggestionRow()
- 位置: L147-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#emit()`, `this.#emitPreview()`, `this.#favicons()`, `this.#onRowFocus()`, `this.#onRowKeyDown()`
- 参照: `suggestion.id`, `suggestion.label`, `suggestion.tabInfos`, `suggestion.tabInfos.length`

## SmartwindowGroupTabsCard.#recentRow()
- 位置: L169-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `styleMap()`, `this.#emit()`
- 参照: `entry.color`, `entry.id`, `entry.label`

## SmartwindowGroupTabsCard.render()
- 位置: L189-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#emit()`, `this.#emitPreview()`, `this.#onRowFocus()`, `this.#onRowKeyDown()`, `this.#recentRow()`, `this.#suggestionRow()`, `this.recent.map()`, `this.suggestions.map()`
- 参照: `e.currentTarget`, `this.computing`, `this.duplicates`, `this.recent.length`, `this.suggestions.length`, `this.tabGroups`

## SmartwindowGroupTabsFlyout.createRenderRoot()
- 位置: L321-323
- 役割: (未記入)
- 触るとき: (未記入)

## SmartwindowGroupTabsFlyout.connectedCallback()
- 位置: L325-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.classList.add()`

## SmartwindowGroupTabsFlyout.getUpdateComplete()
- 位置: async L330-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getUpdateComplete()`, `this.querySelector()`
- 参照: `this.querySelector("tab-groups-list")?.updateComplete`

## SmartwindowGroupTabsFlyout.focusFirstRow()
- 位置: L336-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`, `this.querySelector(ROW_SELECTOR)?.focus()`

## SmartwindowGroupTabsFlyout.#emit()
- 位置: L340-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowGroupTabsFlyout.#onKeyDown()
- 位置: L344-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(event.key === "Home" ? rows[0] : rows.at(-1)).focus()`, `event.preventDefault()`, `event.target.closest()`, `rows.at()`, `rows.indexOf()`, `rows[rows.indexOf(row) + step]?.focus()`, `this.#emit()`, `this.querySelectorAll()`
- 参照: `event.key`

## SmartwindowGroupTabsFlyout.#onGroupsClick()
- 位置: L373-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if (event.target.closest("button, moz-button"))` → `this.#emit()`

## SmartwindowGroupTabsFlyout.render()
- 位置: L379-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`, `this.#tabList()`
- 条件付き依存: `if (this.groupsListId)` → `html()`
- 条件付き依存: `if (this.groupsListId)` → `this.#onKeyDown()`
- 条件付き依存: `if (this.groupsListId)` → `this.#onGroupsClick()`
- 条件付き依存: `if (this.groupsListId)` → `keyed()`
- 条件付き依存: `if (this.duplicates?.length)` → `this.#tabList()`
- 条件付き依存: `if (this.duplicates?.length)` → `this.#emit()`
- 参照: `suggestion.id`, `suggestion.label`, `suggestion.tabInfos`, `this.duplicates`, `this.duplicates?.length`, `this.groupsListId`, `this.suggestion`

## SmartwindowGroupTabsFlyout.#tabList()
- 位置: L421-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `favicon()`, `html()`, `onSelect()`, `tabInfos.map()`, `this.#onKeyDown()`
- 参照: `info.title`
