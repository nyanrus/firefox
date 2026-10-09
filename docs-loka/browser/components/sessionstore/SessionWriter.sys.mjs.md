# browser/components/sessionstore/SessionWriter.sys.mjs

source: browser/components/sessionstore/SessionWriter.sys.mjs
source-hash: 5dd6ad7be2271c92a524b43eed1883f4423fc456
lines: 424

## <module>
- 役割: (未記入)
- 呼び出し先: `Promise.resolve()`, `XPCOMUtils.declareLazy()`

## lockIOWithMutex()
- 位置: L44-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sessionFileIOMutex.then()`

## init()
- 位置: L97-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prefs.hasOwnProperty()`
- 参照: `paths.nextUpgradeBackup`, `paths.upgradeBackup`, `prefs.maxSerializeBack`, `prefs.maxSerializeForward`, `prefs.maxUpgradeBackups`, `this.#maxSerializeBack`, `this.#maxSerializeForward`, `this.#maxUpgradeBackups`, `this.#paths`, `this.#state`, `this.#upgradeBackupNeeded`, `this.#useOldExtension`

## write()
- 位置: async L137-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lockIOWithMutex()`, `this.#write()`, `unlock()`

## #write()
- 位置: async L146-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.sessionStoreLogger.debug()`, `lazy.sessionStoreLogger.warn()`
- 条件付き依存: `if (this.#maxSerializeBack > -1)` → `Math.max()`
- 条件付き依存: `if (this.#maxSerializeForward > -1)` → `Math.min()`
- 条件付き依存: `if (options.isFinalWrite)` → `tab.entries.slice()`
- 条件付き依存: `if (this.#state == STATE_CLEAN || this.#state == STATE_EMPTY)` → `IOUtils.makeDirectory()`
- 条件付き依存: `if (!this.#useOldExtension)` → `IOUtils.move()`
- 条件付き依存: `if (!(!this.#useOldExtension))` → `this.#paths.clean.replace()`
- 条件付き依存: `if (!(!this.#useOldExtension))` → `IOUtils.read()`
- 条件付き依存: `if (!(!this.#useOldExtension))` → `IOUtils.write()`
- 条件付き依存: `if (options.isFinalWrite)` → `IOUtils.writeJSON()`
- 条件付き依存: `if (options.isFinalWrite)` → `IOUtils.stat()`
- 条件付き依存: `if (this.#state == STATE_RECOVERY)` → `IOUtils.writeJSON()`
- 条件付き依存: `if (this.#state == STATE_RECOVERY)` → `IOUtils.stat()`
- 条件付き依存: `if (!(this.#state == STATE_RECOVERY))` → `IOUtils.writeJSON()`
- 条件付き依存: `if (!(this.#state == STATE_RECOVERY))` → `IOUtils.stat()`
- 条件付き依存: `if ( this.#upgradeBackupNeeded && (this.#state == STATE_CLEAN || this.#state == STATE_UPGRADE_BACKUP) )` → `IOUtils.copy()`
- 条件付き依存: `if ( this.#upgradeBackupNeeded && (this.#state == STATE_CLEAN || this.#state == STATE_UPGRADE_BACKUP) )` → `lazy.sessionStoreLogger.warn()`
- 条件付き依存: `if ( this.#upgradeBackupNeeded && (this.#state == STATE_CLEAN || this.#state == STATE_UPGRADE_BACKUP) )` → `IOUtils.getChildren()`
- 条件付き依存: `if ( this.#upgradeBackupNeeded && (this.#state == STATE_CLEAN || this.#state == STATE_UPGRADE_BACKUP) )` → `children.filter()`
- 条件付き依存: `if ( this.#upgradeBackupNeeded && (this.#state == STATE_CLEAN || this.#state == STATE_UPGRADE_BACKUP) )` → `path.startsWith()`
- 条件付き依存: `if (backups.length > this.#maxUpgradeBackups)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (backups.length > this.#maxUpgradeBackups)` → `backups.sort()`
- 条件付き依存: `if (backups.length > this.#maxUpgradeBackups)` → `IOUtils.remove()`
- 条件付き依存: `if (backups.length > this.#maxUpgradeBackups)` → `lazy.sessionStoreLogger.warn()`
- 条件付き依存: `if (options.performShutdownCleanup && !exn)` → `IOUtils.remove()`
- 参照: `backups.length`, `fileStat.size`, `options.isFinalWrite`, `options.performShutdownCleanup`, `state.windows`, `tab.entries`, `tab.entries.length`, `tab.index`, `telemetry.fileSizeBytes`, `telemetry.writeFileMs`, `this.#maxSerializeBack`, `this.#maxSerializeForward`, `this.#maxUpgradeBackups`, `this.#paths.backups`, `this.#paths.clean`, `this.#paths.cleanBackup`, `this.#paths.nextUpgradeBackup`, `this.#paths.recovery`, `this.#paths.recoveryBackup`, `this.#paths.upgradeBackup`, `this.#paths.upgradeBackupPrefix`, `this.#state`, `this.#upgradeBackupNeeded`, `this.#useOldExtension`, `window.tabs`

## wipe()
- 位置: async L337-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lockIOWithMutex()`, `this.#wipe()`, `unlock()`

## #wipe()
- 位置: async L346-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `this.#paths.clean.replace()`, `this.#wipeFromDir()`
- 参照: `PathUtils.profileDir`, `this.#paths.backups`, `this.#paths.clean`, `this.#state`

## #wipeFromDir()
- 位置: async L392-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.remove()`, `IOUtils.stat()`, `PathUtils.filename()`, `PathUtils.filename(entryPath).startsWith()`
