# browser/components/aiwindow/ui/components/smartwindow-panel-list/smartwindow-panel-list.mjs

source: browser/components/aiwindow/ui/components/smartwindow-panel-list/smartwindow-panel-list.mjs
source-hash: 136800921d5153b349afb2f6344b378503e1d45d
lines: 462

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## SmartwindowPanelList.constructor()
- 位置: L50-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.alwaysOpen`, `this.anchor`, `this.groups`, `this.placeholderL10nId`, `this.selectedItemId`, `this.sidebarMode`

## SmartwindowPanelList.willUpdate()
- 位置: L60-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (changedProperties.has("groups"))` → `this.#selectableItems()`
- 参照: `first?.id`, `this.selectedItemId`

## SmartwindowPanelList.#selectableItems()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.groups.flatMap()`
- 参照: `group.items`

## SmartwindowPanelList.moveSelection()
- 位置: L81-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.findIndex()`, `this.#selectableItems()`
- 参照: `item.id`, `items.length`, `items[next].id`, `this.selectedItemId`

## SmartwindowPanelList.getSelectedItem()
- 位置: L95-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#selectableItems()`, `this.#selectableItems().find()`
- 参照: `item.id`, `this.selectedItemId`

## SmartwindowPanelList.#hasCustomItems()
- 位置: L102-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...itemsHost.children].some()`, `element.classList.contains()`
- 参照: `element.localName`, `itemsHost.children`, `this.#panelList`

## SmartwindowPanelList.#isCommandMode()
- 位置: L111-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`

## SmartwindowPanelList.firstUpdated()
- 位置: L115-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeMoveChildrenIntoPanel()`, `this.#panelList.addEventListener()`, `this.shadowRoot.querySelector()`
- 条件付き依存: `if (this.#isCommandMode)` → `this.#reposition()`
- 条件付き依存: `if (this.sidebarMode)` → `this.#clampToViewport()`
- 条件付き依存: `if (this.alwaysOpen)` → `this.show()`
- 参照: `this.#isCommandMode`, `this.#panelList`, `this.alwaysOpen`, `this.sidebarMode`

## SmartwindowPanelList.#maybeMoveChildrenIntoPanel()
- 位置: L133-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `this.#panelList.append()`
- 参照: `custom.length`, `this.children`

## SmartwindowPanelList.#clampToViewport()
- 位置: L141-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `getComputedStyle()`, `panelEl.getBoundingClientRect()`, `parseFloat()`
- 参照: `getComputedStyle(panelEl).marginInlineStart`, `panelEl.style.left`, `panelEl.style.top`, `panelRect.height`, `panelRect.width`, `this.#panelList`, `window.innerHeight`, `window.innerWidth`

## SmartwindowPanelList.#reposition()
- 位置: L161-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorElement.getBoundingClientRect()`, `panelEl.getAttribute()`, `requestAnimationFrame()`, `this.#clampToViewport()`
- 条件付き依存: `if (valign === "top")` → `Math.max()`
- 参照: `anchorRect.bottom`, `anchorRect.left`, `anchorRect.top`, `anchorRect.width`, `panelEl.scrollHeight`, `panelEl.style.left`, `panelEl.style.top`, `panelEl.style.width`, `this.#anchorElement`, `this.#isCommandMode`, `this.#panelList`, `this.#panelList?.open`, `window.scrollX`, `window.scrollY`

## SmartwindowPanelList.updated()
- 位置: L194-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.updated()`
- 条件付き依存: `if (changedProperties.has("anchor"))` → `this.renderRoot.querySelector()`
- 条件付き依存: `if ( this.#panelList?.open && (changedProperties.has("anchor") || changedProperties.has("groups")) )` → `this.#reposition()`
- 参照: `this.#anchorElement`, `this.#panelList?.open`, `this.anchor`

## SmartwindowPanelList.show()
- 位置: async L212-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panelList.show()`
- 参照: `this.#anchorElement`, `this.updateComplete`

## SmartwindowPanelList.hide()
- 位置: async L217-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panelList.hide()`
- 参照: `this.updateComplete`

## SmartwindowPanelList.toggle()
- 位置: async L222-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panelList.toggle()`
- 参照: `this.#anchorElement`, `this.updateComplete`

## SmartwindowPanelList.handlePanelClick()
- 位置: L227-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.closest()`, `e.target.closest(".panel-item-container")?.querySelector()`, `panelItem.classList.contains()`
- 条件付き依存: `if (panelItem && !panelItem.classList.contains("panel-section-header"))` → `panelItem.textContent.trim()`
- 条件付き依存: `if (panelItem && !panelItem.classList.contains("panel-section-header"))` → `this.dispatchEvent()`
- 参照: `panelItem.itemColor`, `panelItem.itemIcon`, `panelItem.itemId`, `panelItem.itemLabel`, `panelItem.itemType`

## SmartwindowPanelList.handleKeyDown()
- 位置: L248-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## SmartwindowPanelList.#isEmpty()
- 位置: L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.groups.every()`
- 参照: `g.items?.length`, `this.groups.length`

## SmartwindowPanelList.#renderAnchor()
- 位置: L266-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `styleMap()`, `this.getBoundingClientRect()`
- 参照: `rect.left`, `rect.top`, `this.anchor`, `this.anchor.height`, `this.anchor.left`, `this.anchor.top`, `this.anchor.width`

## SmartwindowPanelList.#renderEmptyState()
- 位置: L284-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.placeholderL10nId`

## SmartwindowPanelList.#renderGroupHeader()
- 位置: L293-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## SmartwindowPanelList.#renderPlainHeader()
- 位置: L302-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## SmartwindowPanelList.#computeItemStyles()
- 位置: L312-320
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `item.icon`

## SmartwindowPanelList.#renderTabGroupItem()
- 位置: L324-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`
- 参照: `item.color`, `item.id`, `item.label`, `item.type`

## SmartwindowPanelList.#renderItem()
- 位置: L349-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `ifDefined()`, `styleMap()`, `this.#computeItemStyles()`
- 条件付き依存: `if (item.type == CONTEXT_MENTION_TYPE.TAB_GROUP)` → `this.#renderTabGroupItem()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `item.description`, `item.descriptionL10nId`, `item.icon`, `item.id`, `item.l10nId`, `item.label`, `item.type`

## SmartwindowPanelList.#renderGroup()
- 位置: L390-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `repeat()`, `this.#renderItem()`
- 条件付き依存: `if (group.headerL10nId)` → `this.#renderGroupHeader()`
- 条件付き依存: `if (group.header)` → `this.#renderPlainHeader()`
- 参照: `group.header`, `group.headerL10nId`, `group.items`, `group.items?.length`, `item.id`, `this.#isCommandMode`, `this.selectedItemId`

## SmartwindowPanelList.#renderGroups()
- 位置: L416-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `repeat()`, `this.#renderGroup()`
- 参照: `this.groups`

## SmartwindowPanelList.#renderContent()
- 位置: L424-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isEmpty()`, `this.#renderEmptyState()`, `this.#renderGroups()`
- 参照: `this.#hasCustomItems`

## SmartwindowPanelList.#renderCommandFooter()
- 位置: L432-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#isEmpty()`
- 参照: `this.#hasCustomItems`, `this.#isCommandMode`

## SmartwindowPanelList.render()
- 位置: L444-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderAnchor()`, `this.#renderCommandFooter()`, `this.#renderContent()`
- 参照: `this.handleKeyDown`, `this.handlePanelClick`
