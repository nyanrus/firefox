# browser/components/sessionstore/SessionWriter.sys.mjs

source: browser/components/sessionstore/SessionWriter.sys.mjs
source-hash: 5dd6ad7be2271c92a524b43eed1883f4423fc456
lines: 424

## <module>
- 役割: sessionstore のファイル（clean・recovery・バックアップ）の読み書きと削除を一手に引き受ける I/O 層。
- 呼び出し先: `Promise.resolve()`, `XPCOMUtils.declareLazy()`

## lockIOWithMutex()
- 位置: L44-54
- 役割: Promise の連鎖でロックを取り、同じセッションファイルへの I/O を直列化する。
- 触るとき: 書き込みと削除が同時に走って互いのファイルを壊す可能性を調べるとき。
- 呼び出し先: `sessionFileIOMutex.then()`

## init()
- 位置: L97-121
- 役割: 読み込み元の状態（clean・recovery・upgradeBackup など）、パス、必須の 3 つの設定値を受け取って書き込み器を初期化する。
- 触るとき: 起動時にどのファイルから読んだかで書き込み動作が変わる仕組みを変えるとき。
- 呼び出し先: `prefs.hasOwnProperty()`
- 参照: `paths.nextUpgradeBackup`, `paths.upgradeBackup`, `prefs.maxSerializeBack`, `prefs.maxSerializeForward`, `prefs.maxUpgradeBackups`, `this.#maxSerializeBack`, `this.#maxSerializeForward`, `this.#maxUpgradeBackups`, `this.#paths`, `this.#state`, `this.#upgradeBackupNeeded`, `this.#useOldExtension`

## write()
- 位置: async L137-144
- 役割: ロックを取ってから #write を呼ぶ公開の書き込み口。
- 触るとき: セッションの保存要求がどの順で処理されるかを確かめるとき。
- 呼び出し先: `lockIOWithMutex()`, `this.#write()`, `unlock()`

## #write()
- 位置: async L146-332
- 役割: 終了時は shistory の前後件数を上限で切り詰め、clean の退避・recovery への書き込み・アップグレード用バックアップの作成と古いものの削除を行う。終了時は自動復元が無効なら recovery を消す。
- 触るとき: 保存ファイルのサイズ、バックアップ世代数、終了時のプライバシー消去のどれかを変えるとき。
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
- 役割: ロックを取ってから #wipe を呼ぶ公開の削除口。
- 触るとき: セッションデータの全消去がどこまで消すかを確かめるとき。
- 呼び出し先: `lockIOWithMutex()`, `this.#wipe()`, `unlock()`

## #wipe()
- 位置: async L346-383
- 役割: clean（旧 .js を含む）、バックアップディレクトリ、プロファイル直下の sessionstore.bak を消し、状態を empty にする。
- 触るとき: 履歴の消去や「セッションを残さない」設定で残るファイルを調べるとき。
- 呼び出し先: `IOUtils.remove()`, `this.#paths.clean.replace()`, `this.#wipeFromDir()`
- 参照: `PathUtils.profileDir`, `this.#paths.backups`, `this.#paths.clean`, `this.#state`

## #wipeFromDir()
- 位置: async L392-422
- 役割: 指定ディレクトリのうち、指定の接頭辞で始まるファイル（ディレクトリは除く）を削除する。
- 触るとき: プロファイル内の旧セッションファイルの掃除対象を増やすか絞るとき。
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.remove()`, `IOUtils.stat()`, `PathUtils.filename()`, `PathUtils.filename(entryPath).startsWith()`
