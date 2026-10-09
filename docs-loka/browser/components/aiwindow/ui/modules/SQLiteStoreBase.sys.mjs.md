# browser/components/aiwindow/ui/modules/SQLiteStoreBase.sys.mjs

source: browser/components/aiwindow/ui/modules/SQLiteStoreBase.sys.mjs
source-hash: 92f1929e38b70bebd2a0ffae2490ffebc1ef8aac
lines: 566

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SQLiteStoreBase.constructor()
- 位置: L39-43
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#asyncShutdownBlocker`

## this.#asyncShutdownBlocker()
- 位置: async L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeConnection()`

## SQLiteStoreBase.logPrefix()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.logLevelPref()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.shutdownBlockerName()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.CURRENT_SCHEMA_VERSION()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.databaseFileName()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.prefBranch()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.createEntityStatements()
- 位置: L75-77
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.migrations()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.findOldestPrunableRecords()
- 位置: async L95-97
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.deletePrunableRecord()
- 位置: async L104-106
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.log()
- 位置: L115-123
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#log)` → `console.createInstance()`
- 参照: `this.#log`, `this.logLevelPref`, `this.logPrefix`

## SQLiteStoreBase.connection()
- 位置: L130-132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#conn`

## SQLiteStoreBase.databaseFilePath()
- 位置: L139-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `PathUtils.profileDir`, `this.databaseFileName`

## SQLiteStoreBase.maxDatabaseSizeBytes()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.profilerMarkerCategory()
- 位置: L158-160
- 役割: (未記入)
- 触るとき: (未記入)

## SQLiteStoreBase.ensureDatabase()
- 位置: async L175-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `deferred.resolve()`, `e.errors?.some()`, `this.#initializeSchema()`, `this.#openConnection()`, `this.#removeDatabaseFiles()`, `this.log.warn()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.log.debug()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#removeDatabaseFiles()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `deferred.reject()`
- 条件付き依存: `if ( e.result == Cr.NS_ERROR_FILE_CORRUPTED || e.errors?.some(error => error.result == Ci.mozIStorageError.NOTADB) )` → `this.log.warn()`
- 条件付き依存: `if ( e.result == Cr.NS_ERROR_FILE_CORRUPTED || e.errors?.some(error => error.result == Ci.mozIStorageError.NOTADB) )` → `this.#removeDatabaseFiles()`
- 条件付き依存: `if (!this.#conn)` → `this.#openConnection()`
- 条件付き依存: `if (!this.#conn)` → `this.log.error()`
- 条件付き依存: `if (!this.#conn)` → `deferred.reject()`
- 参照: `Ci.mozIStorageError.NOTADB`, `Cr.NS_ERROR_FILE_CORRUPTED`, `deferred.promise`, `e.message`, `e.result`, `e.stack`, `error.result`, `this.#conn`, `this.#promiseConn`, `this.#removeDatabaseOnStartup`

## SQLiteStoreBase.getDatabaseSchemaVersion()
- 位置: async L238-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.getSchemaVersion()`
- 条件付き依存: `if (!this.#conn)` → `this.ensureDatabase()`
- 参照: `this.#conn`

## SQLiteStoreBase.setSchemaVersion()
- 位置: async L251-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.setSchemaVersion()`

## SQLiteStoreBase.getDatabaseSize()
- 位置: async L260-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.stat()`, `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.log.error()`
- 参照: `e.message`, `e.stack`, `stats.size`, `this.databaseFilePath`

## SQLiteStoreBase.destroyDatabase()
- 位置: async L277-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeDatabaseFiles()`
- 参照: `this.#promiseConn`

## SQLiteStoreBase.applyMigrations()
- 位置: async L287-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `migration()`
- 参照: `this.#conn`, `this.migrations`

## SQLiteStoreBase.getDbBytesInUse()
- 位置: async L303-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rows[0].getResultByName()`, `this.#conn.execute()`

## SQLiteStoreBase.pruneDatabase()
- 位置: async L321-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `Math.max()`, `this.#conn.execute()`, `this.deletePrunableRecord()`, `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.findOldestPrunableRecords()`, `this.getDbBytesInUse()`, `this.log.error()`
- 参照: `e.message`, `e.stack`, `oldestRecords.length`, `record.id`, `this.databaseFilePath`, `this.maxDatabaseSizeBytes`

## SQLiteStoreBase.#openConnection()
- 位置: async L393-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.profiler.IsActive()`, `lazy.Sqlite.openConnection()`, `lazy.Sqlite.shutdown.addBlocker()`, `this.#conn.execute()`, `this.log.debug()`, `this.log.error()`, `this.log.warn()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `IOUtils.stat()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `(stat.size / 1048576).toFixed()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `ChromeUtils.now()`
- 条件付き依存: `if (markerData)` → `ChromeUtils.addProfilerMarker()`
- 参照: `e.message`, `e.stack`, `markerData.sizeLabel`, `markerData.startTime`, `stat.size`, `this.#asyncShutdownBlocker`, `this.#conn`, `this.databaseFilePath`, `this.logPrefix`, `this.profilerMarkerCategory`, `this.shutdownBlockerName`
- XPCOM: `Services.profiler`

## SQLiteStoreBase.#closeConnection()
- 位置: async L447-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Sqlite.shutdown.removeBlocker()`, `this.#conn.close()`, `this.log.debug()`, `this.log.warn()`
- 参照: `e.message`, `this.#asyncShutdownBlocker`, `this.#conn`

## SQLiteStoreBase.#initializeSchema()
- 位置: async L469-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.executeTransaction()`, `this.applyMigrations()`, `this.getDatabaseSchemaVersion()`, `this.setSchemaVersion()`
- 条件付き依存: `if (version > this.CURRENT_SCHEMA_VERSION)` → `this.setSchemaVersion()`
- 条件付き依存: `if (version == 0)` → `this.#createDatabaseEntities()`
- 条件付き依存: `if (version == 0)` → `this.#conn.setSchemaVersion()`
- 参照: `this.CURRENT_SCHEMA_VERSION`

## SQLiteStoreBase.#createDatabaseEntities()
- 位置: async L502-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.execute()`
- 参照: `this.createEntityStatements`

## SQLiteStoreBase.#removeDatabaseFiles()
- 位置: async L513-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `this.#closeConnection()`, `this.log.debug()`, `this.log.warn()`
- 参照: `PathUtils.profileDir`, `this.#removeDatabaseOnStartup`, `this.databaseFileName`, `this.databaseFilePath`

## SQLiteStoreBase.#removeDatabaseOnStartup()
- 位置: L544-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.prefBranch`
- XPCOM: `Services.prefs`

## SQLiteStoreBase.#removeDatabaseOnStartup()
- 位置: L558-564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.log.debug()`
- 参照: `this.prefBranch`
- XPCOM: `Services.prefs`
