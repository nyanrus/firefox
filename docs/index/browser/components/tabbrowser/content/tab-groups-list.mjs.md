# browser/components/tabbrowser/content/tab-groups-list.mjs

source: browser/components/tabbrowser/content/tab-groups-list.mjs
source-hash: e8d39a7bd6c82bf3f90b53d44b2892bb262721e1
lines: 197

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`, `customElements.define()`

## TabGroupsList.constructor()
- 位置: L32-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## TabGroupsList.createRenderRoot()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)

## TabGroupsList.#win()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)

## TabGroupsList.connectedCallback()
- 位置: L48-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.#populate()`

## TabGroupsList.firstUpdated()
- 位置: async L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerDocument.l10n.formatValues()`

## TabGroupsList.#populate()
- 位置: L59-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.SessionStore.savedGroups.toSorted()`, `win.gBrowser.getAllTabGroups()`

## TabGroupsList.#handleGroupClick()
- 位置: L71-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.closest("panel"))?.hidePopup()`, `this.closest()`
- 条件付き依存: `if (isOpen)` → `group.select()`
- 条件付き依存: `if (isOpen)` → `group.documentGlobal.focus()`
- 条件付き依存: `if (!(isOpen))` → `this.#win.SessionStore.openSavedTabGroup()`

## TabGroupsList.#handleContextMenu()
- 位置: L83-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `popup.openPopupAtScreen()`, `this.ownerDocument.getElementById()`

## TabGroupsList.#groupRow()
- 位置: L94-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `classMap()`, `html()`, `styleMap()`, `this.#handleContextMenu()`, `this.#handleGroupClick()`

## TabGroupsList.#emptyState()
- 位置: L132-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## TabGroupsList.#handleCreateTabGroup()
- 位置: L159-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.closest("panel"))?.hidePopup()`, `this.closest()`, `win.gBrowser.TabMetrics.userTriggeredContext()`, `win.gBrowser.addTabGroup()`, `win.gBrowser.addTrustedTab()`

## TabGroupsList.render()
- 位置: L170-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `repeat()`, `this.#groupRow()`
- 条件付き依存: `if (!this._openGroups.length && !this._savedGroups.length)` → `this.#emptyState()`
