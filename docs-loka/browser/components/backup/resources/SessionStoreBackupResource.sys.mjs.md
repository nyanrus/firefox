# browser/components/backup/resources/SessionStoreBackupResource.sys.mjs

source: browser/components/backup/resources/SessionStoreBackupResource.sys.mjs
source-hash: e78edb86dd7194feea3dc05c904341edd15b1c44
lines: 167

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## SessionStoreBackupResource.constructor()
- 位置: L45-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._sessionStore`

## SessionStoreBackupResource.key()
- 位置: L50-52
- 役割: (未記入)
- 触るとき: (未記入)

## SessionStoreBackupResource.requiresEncryption()
- 位置: L54-59
- 役割: (未記入)
- 触るとき: (未記入)

## SessionStoreBackupResource.#sessionStore()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SessionStore`, `this._sessionStore`

## SessionStoreBackupResource.filteredSessionStoreState()
- 位置: L65-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sessionStore.getCurrentState()`
- 条件付き依存: `if (sessionStoreState.windows)` → `sessionStoreState.windows.filter()`
- 条件付き依存: `if (sessionStoreState.windows)` → `sessionStoreState.windows.forEach()`
- 条件付き依存: `if (win.tabs)` → `win.tabs.forEach()`
- 条件付き依存: `if (win._closedTabs)` → `win._closedTabs.forEach()`
- 条件付き依存: `if (sessionStoreState.savedGroups)` → `sessionStoreState.savedGroups.forEach()`
- 条件付き依存: `if (group.tabs)` → `group.tabs.forEach()`
- 参照: `closedTab.state.storage`, `group.tabs`, `sessionStoreState.cookies`, `sessionStoreState.savedGroups`, `sessionStoreState.windows`, `tab.state.storage`, `tab.storage`, `w?.isPrivate`, `win._closedTabs`, `win.tabs`

## SessionStoreBackupResource.backup()
- 位置: async L97-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`, `IOUtils.writeJSON()`, `PathUtils.join()`, `Promise.allSettled()`, `Promise.race()`, `lazy.BrowserWindowTracker.orderedWindows.map()`, `lazy.setTimeout()`
- 条件付き依存: `if (e?.timeout)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (!(e?.timeout))` → `lazy.logConsole.error()`
- 参照: `PathUtils.profileDir`, `e?.timeout`, `lazy.TAB_FLUSH_TIMEOUT`, `lazy.TabStateFlusher.flushWindow`, `this.filteredSessionStoreState`

## SessionStoreBackupResource.recover()
- 位置: async L135-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.copyFiles()`

## SessionStoreBackupResource.measure()
- 位置: async L144-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BackupResource.getDirectorySize()`, `Glean.browserBackup.sessionStoreBackupsDirectorySize.set()`, `Glean.browserBackup.sessionStoreSize.set()`, `JSON.stringify()`, `PathUtils.join()`, `bytesToFuzzyKilobytes()`, `new TextEncoder().encode()`, `this.#sessionStore.getCurrentState()`
- 参照: `PathUtils.profileDir`, `new TextEncoder().encode( JSON.stringify(sessionStoreJson) ).byteLength`
