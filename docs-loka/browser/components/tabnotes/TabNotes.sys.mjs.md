# browser/components/tabnotes/TabNotes.sys.mjs

source: browser/components/tabnotes/TabNotes.sys.mjs
source-hash: 2ec545b3021e697ad46e77f5b6d874fd96769419
lines: 394

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## TabNotesStorage.#connection()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`, `this.init().then()`
- 参照: `this.#databaseConnection`

## TabNotesStorage.init()
- 位置: L124-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `Sqlite.openConnection()`, `Sqlite.openConnection({ path: this.dbPath, }).then()`, `Sqlite.shutdown.addBlocker()`, `connection.execute()`, `connection.getSchemaVersion()`
- 条件付き依存: `if (currentVersion == 0)` → `connection.executeTransaction()`
- 条件付き依存: `if (currentVersion == 0)` → `connection.execute()`
- 条件付き依存: `if (currentVersion == 0)` → `connection.setSchemaVersion()`
- 参照: `PathUtils.profileDir`, `options?.basePath`, `this.#databaseConnection`, `this.#initPromise`, `this.#shutdownBlocker`, `this.DATABASE_FILE_NAME`, `this.dbPath`

## this.#shutdownBlocker()
- 位置: L135-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.deinit()`

## TabNotesStorage.deinit()
- 位置: L172-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (this.#shutdownBlocker)` → `Sqlite.shutdown.removeBlocker()`
- 条件付き依存: `if (this.#databaseConnection)` → `this.#databaseConnection.close().then()`
- 条件付き依存: `if (this.#databaseConnection)` → `this.#databaseConnection.close()`
- 参照: `this.#databaseConnection`, `this.#initPromise`, `this.#shutdownBlocker`

## TabNotesStorage.isEligible()
- 位置: L190-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.canParse()`
- 参照: `tab.canonicalUrl`, `tab?.canonicalUrl`

## TabNotesStorage.get()
- 位置: async L204-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `connection.executeCached()`, `this.#mapDbRowToRecord()`, `this.isEligible()`
- 参照: `results?.length`, `tab.canonicalUrl`, `this.#connection`

## TabNotesStorage.set()
- 位置: async L235-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `connection.executeCached()`, `connection.executeTransaction()`, `tab.dispatchEvent()`, `this.#mapDbRowToRecord()`, `this.#sanitizeInput()`, `this.get()`, `this.isEligible()`
- 条件付き依存: `if (!existingNote)` → `connection.executeCached()`
- 条件付き依存: `if (!existingNote)` → `this.#mapDbRowToRecord()`
- 条件付き依存: `if (!existingNote)` → `tab.dispatchEvent()`
- 参照: `existingNote.text`, `options.telemetrySource`, `tab.canonicalUrl`, `this.#connection`

## TabNotesStorage.delete()
- 位置: async L301-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `connection.executeCached()`
- 条件付き依存: `if (deleteResult?.length > 0)` → `this.#mapDbRowToRecord()`
- 条件付き依存: `if (deleteResult?.length > 0)` → `tab.dispatchEvent()`
- 参照: `deleteResult?.length`, `options.telemetrySource`, `tab.canonicalUrl`, `this.#connection`

## TabNotesStorage.has()
- 位置: async L333-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.get()`

## TabNotesStorage.count()
- 位置: async L343-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `connection.executeCached()`
- 条件付き依存: `if (countResult?.length == 1)` → `countResult[0].getDouble()`
- 参照: `countResult?.length`, `this.#connection`

## TabNotesStorage.reset()
- 位置: async L360-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `connection.execute()`
- 参照: `this.#connection`

## TabNotesStorage.#sanitizeInput()
- 位置: L372-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.slice()`

## TabNotesStorage.#mapDbRowToRecord()
- 位置: L382-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Temporal.Instant.fromEpochMilliseconds()`, `row.getDouble()`, `row.getString()`
