# browser/components/sessionstore/SessionMigration.sys.mjs

source: browser/components/sessionstore/SessionMigration.sys.mjs
source-hash: 4f0dd879c77b6981b659a322d82e1195671e0ec0
lines: 135

## <module>
- 役割: 起動時に旧形式のセッション状態を、about:welcomeback に渡す最小限の形式へ変換して書き出す移行処理。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## convertState()
- 位置: L31-101
- 役割: ウィンドウ、タブ、履歴を URL・タイトル・プリンシパルなどに絞り、タブグループを保存済みグループへ変換して about:welcomeback のエントリに包む。
- 触るとき: 移行後に残すデータを増減させるとき、または welcomeback 画面で復元できる内容を確認するとき。既存の保存済みグループと同じ ID のものは統合され、removeAfterRestore が立つ。
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
- 役割: 指定パスの JSON を解凍しながら非同期に読み込む。
- 触るとき: 移行元ファイルの形式や圧縮の扱いを変えるとき。
- 呼び出し先: `IOUtils.readJSON()`

## writeState()
- 位置: L111-116
- 役割: 状態を圧縮付き JSON として書き出す。書き込みは一時ファイル(パス + .tmp)を経由する。
- 触るとき: 移行先ファイルが途中で壊れないようにする手順を見直すとき。
- 呼び出し先: `IOUtils.writeJSON()`

## migrate()
- 位置: L123-133
- 役割: 移行元を読み込み、convertState で変換し、移行先へ書き出す一連の処理を実行する。
- 触るとき: 旧形式からの移行をいつ実行するか、または移行の失敗を呼び出し側へどう伝えるかを変えるとき。SessionFile を使わず直接書くのは、移行時にプロファイルのディレクトリが分かるとは限らないため。
- 呼び出し先: `SessionMigrationInternal.convertState()`, `SessionMigrationInternal.readState()`, `SessionMigrationInternal.writeState()`
