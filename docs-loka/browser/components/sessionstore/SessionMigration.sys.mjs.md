# browser/components/sessionstore/SessionMigration.sys.mjs

source: browser/components/sessionstore/SessionMigration.sys.mjs
source-hash: 4f0dd879c77b6981b659a322d82e1195671e0ec0
lines: 135

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## convertState()
- 位置: L31-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aStateObj.windows.map()`, `groupsToSave.forEach()`, `oldTab.entries.map()`, `oldWin.tabs.map()`, `savedGroups.find()`
- 条件付き依存: `if (oldTab.groupId)` → `oldWin.groups.find()`
- 条件付き依存: `if (oldTab.groupId)` → `groupsToSave.get()`
- 条件付き依存: `if (!groupToSave)` → `lazy.TabGroupState.savedInClosedWindow()`
- 条件付き依存: `if (!groupToSave)` → `groupsToSave.set()`
- 条件付き依存: `if (oldTab.groupId)` → `lazy.SessionStore.formatTabStateForSavedGroup()`
- 条件付き依存: `if (tabData)` → `groupToSave.tabs.push()`
- 条件付き依存: `if (!(alreadySavedGroup))` → `savedGroups.push()`
- 参照: `aStateObj.savedGroups`, `aStateObj.selectedWindow`, `alreadySavedGroup.removeAfterRestore`, `entry.title`, `entry.triggeringPrincipal_base64`, `entry.url`, `existingGroup.id`, `groupState.id`, `groupStateToSave.id`, `groupToSave.removeAfterRestore`, `lazy.E10SUtils.SERIALIZED_SYSTEMPRINCIPAL`, `oldTab.groupId`, `oldTab.hidden`, `oldTab.index`, `oldTab.pinned`, `oldWin.groups`, `oldWin.selected`, `state.windows`, `tab.entries`, `tab.groupId`, `tab.hidden`, `tab.index`, `tab.pinned`, `win._closedTabs`, `win.groups`, `win.selected`, `win.tabs`

## readState()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`

## writeState()
- 位置: L111-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeJSON()`

## migrate()
- 位置: L123-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionMigrationInternal.convertState()`, `SessionMigrationInternal.readState()`, `SessionMigrationInternal.writeState()`
