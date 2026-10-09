# browser/components/sessionstore/SessionFile.sys.mjs

source: browser/components/sessionstore/SessionFile.sys.mjs
source-hash: 5ed858536ad1a9e5803d46ad600adbbc7f9ac826
lines: 571

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `PathUtils.join()`, `XPCOMUtils.declareLazy()`

## read()
- 位置: L49-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionFileInternal.read()`

## write()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionFileInternal.write()`

## wipe()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionFileInternal.wipe()`

## Paths()
- 位置: L71-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SessionFileInternal.Paths`

## upgradeBackup()
- 位置: L137-143
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SessionFileInternal.latestUpgradeBackupID`, `this.upgradeBackupPrefix`

## nextUpgradeBackup()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.platformBuildID`, `this.upgradeBackupPrefix`
- XPCOM: `Services.appinfo`

## loadOrder()
- 位置: L155-171
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (SessionFileInternal.latestUpgradeBackupID)` → `order.push()`
- 参照: `SessionFileInternal.latestUpgradeBackupID`

## latestUpgradeBackupID()
- 位置: L201-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`
- XPCOM: `Services.prefs`

## _readInternal()
- 位置: async L209-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DOMException.isInstance()`, `Date.now()`, `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`, `Glean.sessionRestore.readFile.accumulateSingleSample()`, `IOUtils.readUTF8()`, `JSON.parse()`, `lazy.SessionStore.isFormatVersionCompatible()`, `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (useOldExtension)` → `this.Paths[key] .replace("jsonlz4", "js") .replace()`
- 条件付き依存: `if (useOldExtension)` → `this.Paths[key] .replace()`
- 条件付き依存: `if (parsed._cachedObjs)` → `parsed.windows.concat()`
- 条件付き依存: `if (parsed._cachedObjs)` → `win.tabs.concat()`
- 条件付き依存: `if (parsed._cachedObjs)` → `cacheMap.get()`
- 条件付き依存: `if (parsed._cachedObjs)` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if ( !lazy.SessionStore.isFormatVersionCompatible( parsed.version || [ "sessionrestore", 0, ] /* fallback for old versions*/ ) )` → `lazy.sessionStoreLogger.warn()`
- 条件付き依存: `if ( !lazy.SessionStore.isFormatVersionCompatible( parsed.version || [ "sessionrestore", 0, ] /* fallback for old versions*/ ) )` → `JSON.stringify()`
- 条件付き依存: `if ( !lazy.SessionStore.isFormatVersionCompatible( parsed.version || [ "sessionrestore", 0, ] /* fallback for old versions*/ ) )` → `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`
- 条件付き依存: `if (DOMException.isInstance(ex) && ex.name == "NotFoundError")` → `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`
- 条件付き依存: `if (DOMException.isInstance(ex) && ex.name == "NotFoundError")` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (!(DOMException.isInstance(ex) && ex.name == "NotFoundError"))` → `DOMException.isInstance()`
- 条件付き依存: `if ( DOMException.isInstance(ex) && ex.name == "NotReadableError" )` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if ( DOMException.isInstance(ex) && ex.name == "NotReadableError" )` → `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`
- 条件付き依存: `if (!( DOMException.isInstance(ex) && ex.name == "NotReadableError" ))` → `DOMException.isInstance()`
- 条件付き依存: `if ( DOMException.isInstance(ex) && ex.name == "NotAllowedError" )` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if ( DOMException.isInstance(ex) && ex.name == "NotAllowedError" )` → `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`
- 条件付き依存: `if (ex instanceof SyntaxError)` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if (ex instanceof SyntaxError)` → `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`
- 条件付き依存: `if (!(ex instanceof SyntaxError))` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if (!(ex instanceof SyntaxError))` → `Glean.sessionRestore.backupCanBeLoadedSessionFile.record()`
- 条件付き依存: `if (exists)` → `Glean.sessionRestore.corruptFile[corrupted ? "true" : "false"].add()`
- 参照: `Glean.sessionRestore.corruptFile`, `ex.name`, `ex.stack`, `fileStates.upgradeBackup`, `options.decompress`, `parsed._cachedObjs`, `parsed._closedWindows`, `parsed.version`, `tab.image`, `this.Paths`, `this.Paths.loadOrder`, `this._usingOldExtension`, `win._closedTabs`

## _mergeFileStates()
- 位置: L387-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`

## read()
- 位置: async L403-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.allFilesCorrupt[allCorrupt ? "true" : "false"].add()`, `Object.values()`, `Object.values(fileStates).some()`, `this._readInternal()`
- 条件付き依存: `if (!result)` → `this._readInternal()`
- 条件付き依存: `if (!result)` → `this._mergeFileStates()`
- 条件付き依存: `if (!result)` → `lazy.sessionStoreLogger.warn()`
- 参照: `Glean.sessionRestore.allFilesCorrupt`, `r.fileStates`, `r.result`, `result.origin`, `this._readOrigin`

## getWriter()
- 位置: L440-471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (!this._readOrigin)` → `Promise.reject()`
- 条件付き依存: `if (!this._initialized)` → `lazy.SessionWriter.init()`
- 条件付き依存: `if (!this._initialized)` → `Services.prefs.getIntPref()`
- 参照: `lazy.SessionWriter`, `this.Paths`, `this._initialized`, `this._readOrigin`, `this._usingOldExtension`
- XPCOM: `Services.prefs`

## write()
- 位置: L473-561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.profileBeforeChange.addBlocker()`, `IOUtils.profileBeforeChange.removeBlocker()`, `lazy.sessionStoreLogger.error()`, `promise.then()`, `this.getWriter()`, `this.getWriter().then()`, `write.then()`, `writer.write()`
- 条件付き依存: `if (lazy.RunState.isClosed)` → `Promise.reject()`
- 条件付き依存: `if (lazy.RunState.isClosing)` → `lazy.RunState.setClosed()`
- 条件付き依存: `if (msg.telemetry.writeFileMs)` → `Glean.sessionRestore.writeFile.accumulateSingleSample()`
- 条件付き依存: `if (msg.telemetry.fileSizeBytes)` → `Glean.sessionRestore.fileSizeBytes.accumulate()`
- 条件付き依存: `if (msg.result.upgradeBackup)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (isFinalWrite)` → `Services.obs.notifyObservers()`
- 参照: `Services.appinfo.platformBuildID`, `err.stack`, `lazy.RunState.isClosed`, `lazy.RunState.isClosing`, `lazy.SessionStore.willAutoRestore`, `msg.result.upgradeBackup`, `msg.telemetry.fileSizeBytes`, `msg.telemetry.writeFileMs`, `this._attempts`, `this._failures`, `this._successes`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.prefs`

## fetchState()
- 位置: L538-543
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._attempts`, `this._failures`, `this._successes`

## wipe()
- 位置: async L563-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWriter()`, `writer.wipe()`
- 参照: `this._initialized`
