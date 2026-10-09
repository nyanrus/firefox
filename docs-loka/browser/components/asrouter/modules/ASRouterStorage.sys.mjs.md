# browser/components/asrouter/modules/ASRouterStorage.sys.mjs

source: browser/components/asrouter/modules/ASRouterStorage.sys.mjs
source-hash: 7026dd26d7c6beb2e9767ff2d33e92a1de872ede
lines: 451

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ASRouterStorage.constructor()
- 位置: L22-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dbName`, `this.dbVersion`, `this.storeNames`, `this.telemetry`

## ASRouterStorage.pendingWriteCount()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pendingWrites.size`

## ASRouterStorage.db()
- 位置: L37-45
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._db)` → `this.createOrOpenDb().catch()`
- 条件付き依存: `if (!this._db)` → `this.createOrOpenDb()`
- 参照: `this._db`

## ASRouterStorage._trackedSet()
- 位置: L47-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `p.catch()`, `this.#pendingWrites.add()`, `this.#pendingWrites.delete()`, `this._set()`, `this._set(storeName, key, value).finally()`

## ASRouterStorage.flush()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`
- 参照: `this.#pendingWrites`

## ASRouterStorage.getDbTable()
- 位置: L65-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.storeNames.includes()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this._get.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this._getAll.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this._getAllKeys.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this._trackedSet.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this.getSharedMessageImpressions.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this.getSharedMessageBlocklist.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this.setSharedMessageImpressions.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this.setSharedMessageBlocked.bind()`
- 条件付き依存: `if (this.storeNames.includes(storeName))` → `this.resetSharedMessageStorage.bind()`

## ASRouterStorage._getStore()
- 位置: async L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.db).objectStore()`
- 参照: `this.db`

## ASRouterStorage._get()
- 位置: L89-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this._getStore(storeName)).get()`, `this._getStore()`, `this._requestWrapper()`

## ASRouterStorage._getAll()
- 位置: L95-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this._getStore(storeName)).getAll()`, `this._getStore()`, `this._requestWrapper()`

## ASRouterStorage._getAllKeys()
- 位置: L101-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this._getStore(storeName)).getAllKeys()`, `this._getStore()`, `this._requestWrapper()`

## ASRouterStorage._set()
- 位置: L107-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this._getStore(storeName, "readwrite")).put()`, `this._getStore()`, `this._requestWrapper()`

## ASRouterStorage._openDatabase()
- 位置: L113-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.objectStoreNames.contains()`, `lazy.IndexedDB.open()`, `this.storeNames.forEach()`
- 条件付き依存: `if (!db.objectStoreNames.contains(store))` → `db.createObjectStore()`
- 参照: `this.dbName`, `this.dbVersion`

## ASRouterStorage.createOrOpenDb()
- 位置: async L136-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IndexedDB.deleteDatabase()`, `this._openDatabase()`, `this._registerLifecycleHandlers()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 参照: `this.dbName`, `this.telemetry`

## ASRouterStorage._registerLifecycleHandlers()
- 位置: L162-171
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `db.onclose`, `db.onversionchange`

## db.onversionchange()
- 位置: L163-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.close()`
- 参照: `this._db`

## db.onclose()
- 位置: L167-169
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._db`

## ASRouterStorage._requestWrapper()
- 位置: async L173-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `request()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 参照: `this.telemetry`

## ASRouterStorage.getSharedMessageImpressions()
- 位置: async L192-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `conn.executeCached()`, `lazy.ASRouterPreferences.console.error()`, `lazy.ProfilesDatastoreService.getConnection()`, `row.getResultByName()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 参照: `rows.length`, `this.telemetry`

## ASRouterStorage.getSharedMessageBlocklist()
- 位置: async L235-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.executeCached()`, `lazy.ASRouterPreferences.console.error()`, `lazy.ProfilesDatastoreService.getConnection()`, `row.getResultByName()`, `rows.map()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 参照: `this.telemetry`

## ASRouterStorage.setSharedMessageImpressions()
- 位置: async L268-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterPreferences.console.error()`, `lazy.ProfilesDatastoreService.getConnection()`, `lazy.ProfilesDatastoreService.notify()`
- 条件付き依存: `if (!impressions?.length)` → `conn.executeBeforeShutdown()`
- 条件付き依存: `if (!impressions?.length)` → `conn.executeCached()`
- 条件付き依存: `if (!(!impressions?.length))` → `conn.executeBeforeShutdown()`
- 条件付き依存: `if (!(!impressions?.length))` → `conn.executeCached()`
- 条件付き依存: `if (!(!impressions?.length))` → `JSON.stringify()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 参照: `impressions?.length`, `this.telemetry`

## ASRouterStorage.setSharedMessageBlocked()
- 位置: async L339-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ProfilesDatastoreService.notify()`
- 条件付き依存: `if (isBlocked)` → `lazy.ProfilesDatastoreService.getConnection()`
- 条件付き依存: `if (isBlocked)` → `conn.executeTransaction()`
- 条件付き依存: `if (isBlocked)` → `conn.executeCached()`
- 条件付き依存: `if (isBlocked)` → `lazy.ASRouterPreferences.console.error()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 条件付き依存: `if (!(isBlocked))` → `lazy.ProfilesDatastoreService.getConnection()`
- 条件付き依存: `if (!(isBlocked))` → `conn.executeBeforeShutdown()`
- 条件付き依存: `if (!(isBlocked))` → `conn.executeCached()`
- 条件付き依存: `if (!(isBlocked))` → `lazy.ASRouterPreferences.console.error()`
- 参照: `this.telemetry`

## ASRouterStorage.resetSharedMessageStorage()
- 位置: async L412-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.executeBeforeShutdown()`, `conn.executeCached()`, `lazy.ASRouterPreferences.console.error()`, `lazy.ProfilesDatastoreService.getConnection()`, `lazy.ProfilesDatastoreService.notify()`
- 条件付き依存: `if (this.telemetry)` → `this.telemetry.handleUndesiredEvent()`
- 参照: `this.telemetry`

## getDefaultOptions()
- 位置: L448-450
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `options.collapsed`
