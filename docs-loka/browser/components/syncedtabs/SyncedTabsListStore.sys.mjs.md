# browser/components/syncedtabs/SyncedTabsListStore.sys.mjs

source: browser/components/syncedtabs/SyncedTabsListStore.sys.mjs
source-hash: f5a2cfcfa351a7b2a1824812baf5fdc90c309944
lines: 254

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.assign()`

## SyncedTabsListStore()
- 位置: L14-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EventEmitter.call()`
- 参照: `this._SyncedTabs`, `this._closedClients`, `this._selectedRow`, `this.data`, `this.filter`, `this.inputFocused`

## _change()
- 位置: L31-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `data.forEach()`, `this.emit()`
- 参照: `client.closed`, `client.focused`, `client.id`, `client.selected`, `client.tabs`, `client.tabs.length`, `client.tabs[selectedChild].focused`, `client.tabs[selectedChild].selected`, `client.tabs[selectedParent - tabCount].focused`, `client.tabs[selectedParent - tabCount].selected`, `this._closedClients`, `this._selectedRow`, `this.data`, `this.filter`, `this.inputFocused`

## _selectParentRow()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._selectedRow`

## _toggleBranch()
- 位置: L87-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._change()`
- 条件付き依存: `if (this._closedClients[id])` → `this._selectParentRow()`
- 参照: `this._closedClients`

## _isOpen()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `client.id`, `this._closedClients`

## moveSelectionDown()
- 位置: L99-121
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.filter)` → `this.selectRow()`
- 条件付き依存: `if (branchRow < 0)` → `this.selectRow()`
- 条件付き依存: `if (!(branchRow < 0))` → `this._isOpen()`
- 条件付き依存: `if ( (!branch.tabs.length || childRow >= branch.tabs.length - 1 || !this._isOpen(branch)) && branchRow < this.data.length )` → `this.selectRow()`
- 条件付き依存: `if (childRow < branch.tabs.length)` → `this.selectRow()`
- 参照: `branch.tabs.length`, `this._selectedRow`, `this.data`, `this.data.length`, `this.filter`

## moveSelectionUp()
- 位置: L123-143
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.filter)` → `this.selectRow()`
- 条件付き依存: `if (branchRow < 0)` → `this.selectRow()`
- 条件付き依存: `if (childRow < 0 && branchRow > 0)` → `this._isOpen()`
- 条件付き依存: `if (childRow < 0 && branchRow > 0)` → `this.selectRow()`
- 条件付き依存: `if (childRow >= 0)` → `this.selectRow()`
- 参照: `prevBranch.tabs.length`, `this._selectedRow`, `this.data`, `this.filter`

## selectRow()
- 位置: L146-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._SyncedTabs.recordSyncedTabsTelemetry()`, `this._change()`, `this._selectedRow[1].toString()`, `this._tabCount()`
- 参照: `this._selectedRow`, `this.data`, `this.data.length`, `this.data[parentRow].tabs.length`, `this.filter`, `this.inputFocused`

## _tabCount()
- 位置: L189-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.data.reduce()`
- 参照: `curr.tabs.length`

## toggleBranch()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleBranch()`
- 参照: `this._closedClients`

## closeBranch()
- 位置: L197-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleBranch()`

## openBranch()
- 位置: L201-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleBranch()`

## focusInput()
- 位置: L205-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._change()`
- 参照: `this.inputFocused`

## blurInput()
- 位置: L212-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._change()`
- 参照: `this.inputFocused`

## clearFilter()
- 位置: L219-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getData()`
- 参照: `this._selectedRow`, `this.filter`

## getData()
- 位置: L227-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._SyncedTabs .getTabClients()`, `this._SyncedTabs .getTabClients(this.filter) .then()`, `this._change()`
- 条件付き依存: `if (!hasFilter)` → `this._SyncedTabs.sortTabClientsByLastUsed()`
- 参照: `console.error`, `this._selectedRow`, `this.data`, `this.filter`
