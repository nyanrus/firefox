# browser/components/sessionstore/SessionFile.sys.mjs

source: browser/components/sessionstore/SessionFile.sys.mjs
source-hash: 5ed858536ad1a9e5803d46ad600adbbc7f9ac826
lines: 571

## <module>
- 役割: セッションストアのディスク入出力を担い、読み込みと書き込みを一つずつ順番に実行する。
- 呼び出し先: `Object.freeze()`, `PathUtils.join()`, `XPCOMUtils.declareLazy()`

## read()
- 位置: L49-51
- 役割: セッションファイルを読み込み、結果とファイルごとの状態を返す公開 API。
- 触るとき: 起動時に読み込まれたセッションの内容や、どの候補ファイルが調べられたかを調べるとき。
- 呼び出し先: `SessionFileInternal.read()`

## write()
- 位置: L57-59
- 役割: 状態を書き込む公開 API。内部の write に委譲する。
- 触るとき: 終了時の最後の書き込みや通常の遅延保存が SessionFile に届いているかを確認するとき。
- 呼び出し先: `SessionFileInternal.write()`

## wipe()
- 位置: L63-65
- 役割: セッションファイルの内容を消す公開 API。
- 触るとき: セッションを消去する経路を追うとき、または消去後の動作を変えるとき。
- 呼び出し先: `SessionFileInternal.wipe()`

## Paths()
- 位置: L71-73
- 役割: 保存、バックアップ、アップグレード用の各ファイルのパスを返す getter。
- 触るとき: 保存先のファイル名や場所を変えるとき、読み込み候補を確認するとき。
- 参照: `SessionFileInternal.Paths`

## upgradeBackup()
- 位置: L137-143
- 役割: 最新のアップグレード用バックアップのパスを返す。まだ無ければ空文字。
- 触るとき: アップグレード時に残すバックアップの場所や条件を変えるとき。
- 参照: `SessionFileInternal.latestUpgradeBackupID`, `this.upgradeBackupPrefix`

## nextUpgradeBackup()
- 位置: L148-150
- 役割: 現在のビルド ID を付けた次のアップグレード用バックアップのパスを返す。
- 触るとき: アップグレード時に作るバックアップの名前付けを変えるとき。
- 参照: `Services.appinfo.platformBuildID`, `this.upgradeBackupPrefix`
- XPCOM: `Services.appinfo`

## loadOrder()
- 位置: L155-171
- 役割: 読み込み候補の優先順(clean、recovery、recoveryBackup、cleanBackup、あればアップグレード用)を返す。
- 触るとき: 起動時にどの世代を優先して読むかを変えるとき、または破損時のフォールバックを調べるとき。
- 条件付き依存: `if (SessionFileInternal.latestUpgradeBackupID)` → `order.push()`
- 参照: `SessionFileInternal.latestUpgradeBackupID`

## latestUpgradeBackupID()
- 位置: L201-207
- 役割: アップグレードバックアップのビルド ID を設定から読む。設定が無ければ undefined。
- 触るとき: アップグレード用バックアップがあるかどうかで読み込み順が変わる理由を調べるとき。
- 呼び出し先: `Services.prefs.getCharPref()`
- XPCOM: `Services.prefs`

## _readInternal()
- 位置: async L209-380
- 役割: 読み込み候補を優先順に読み、JSON を解析して最初に使えるものを返す。破損や形式違いは次の候補へ進み、ファイルが無い場合は absent として記録する。
- 触るとき: 起動時に壊れたセッションファイルをどう扱うかを変えるとき、または読み込み失敗の記録を追加するとき。読み込み後に画像の参照を解決してから形式を確認する。
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
- 役割: 二つの形式の読み込みで得たファイル状態を合成する。どちらかで present なら present、次に absent を優先する。
- 触るとき: 旧形式の読み込みを含めて、ファイルが見つかったかどうかの判定を変えるとき。
- 呼び出し先: `Object.keys()`

## read()
- 位置: async L403-437
- 役割: lz4 圧縮形式で読み、結果が無ければ旧形式(非圧縮)で読み直す。それでも無ければ空のセッションとして扱う。
- 触るとき: 旧形式からの移行や、起動時に空セッションになる条件を変えるとき。
- 呼び出し先: `Glean.sessionRestore.allFilesCorrupt[allCorrupt ? "true" : "false"].add()`, `Object.values()`, `Object.values(fileStates).some()`, `this._readInternal()`
- 条件付き依存: `if (!result)` → `this._readInternal()`
- 条件付き依存: `if (!result)` → `this._mergeFileStates()`
- 条件付き依存: `if (!result)` → `lazy.sessionStoreLogger.warn()`
- 参照: `Glean.sessionRestore.allFilesCorrupt`, `r.fileStates`, `r.result`, `result.origin`, `this._readOrigin`

## getWriter()
- 位置: L440-471
- 役割: 初めて書き込むときに SessionWriter を初期化し、保持するアップグレードバックアップ数などを設定から渡す。読み込み前に呼ばれたら拒否する。
- 触るとき: 保持する世代数や直列化の上限を変えるとき。既定値はアップグレードバックアップが 3、後方の直列化が 10、前方が -1(無制限)。
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (!this._readOrigin)` → `Promise.reject()`
- 条件付き依存: `if (!this._initialized)` → `lazy.SessionWriter.init()`
- 条件付き依存: `if (!this._initialized)` → `Services.prefs.getIntPref()`
- 参照: `lazy.SessionWriter`, `this.Paths`, `this._initialized`, `this._readOrigin`, `this._usingOldExtension`
- XPCOM: `Services.prefs`

## write()
- 位置: L473-561
- 役割: 終了処理中なら最後の書き込みとして扱い、終了後の起動用クリーンアップを行ってから SessionWriter に書かせる。閉じた後の書き込みは拒否する。
- 触るとき: 終了時の書き込みが完了するかを調べるとき、書き込みを拒否する条件を変えるとき。終了時の書き込みは終了前のブロッカーとして登録される。
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
- 役割: 終了前のブロッカーに渡す診断情報(試行、成功、失敗の回数とオプション)を返す。
- 触るとき: 終了時に書き込みが終わらなかった場合の状況を確認するとき。
- 参照: `this._attempts`, `this._failures`, `this._successes`

## wipe()
- 位置: async L563-569
- 役割: SessionWriter を取得して内容を消し、次の読み込みで再初期化されるよう初期化済みフラグを戻す。
- 触るとき: 消去後にセッションを読み直す動きを確認するとき。
- 呼び出し先: `this.getWriter()`, `writer.wipe()`
- 参照: `this._initialized`
