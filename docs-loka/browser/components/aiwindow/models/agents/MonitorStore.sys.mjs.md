# browser/components/aiwindow/models/agents/MonitorStore.sys.mjs

source: browser/components/aiwindow/models/agents/MonitorStore.sys.mjs
source-hash: e6002228b0e0e8c5bcf55180738c0547b8ad77c7
lines: 615

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.values()`, `Promise.resolve()`, `console.createInstance()`

## invalidField()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)

## stringField()
- 位置: L38-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.trim()`
- 条件付き依存: `if ( typeof value !== "string" || (!allowEmpty && !value.trim()) || value !== value.trim() )` → `invalidField()`

## timestampField()
- 位置: L49-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isNaN()`, `date.getTime()`, `date.toISOString()`
- 条件付き依存: `if (typeof value !== "string")` → `invalidField()`
- 条件付き依存: `if (Number.isNaN(date.getTime()) || date.toISOString() !== value)` → `invalidField()`

## runCountField()
- 位置: L63-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `lazy.log.warn()`
- 条件付き依存: `if (!recoverInvalid)` → `invalidField()`

## scheduleRecord()
- 位置: L74-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Number.isFinite()`, `Number.isInteger()`, `invalidField()`
- 条件付き依存: `if (!schedule || typeof schedule !== "object" || Array.isArray(schedule))` → `invalidField()`
- 条件付き依存: `if (!Number.isFinite(schedule.hours) || schedule.hours <= 0)` → `invalidField()`
- 条件付き依存: `if ( !Number.isInteger(schedule.hour) || schedule.hour < 0 || schedule.hour > 23 || !Number.isInteger(schedule.minute) || schedule.minute < 0 || schedule.minute ...)` → `invalidField()`
- 条件付き依存: `if ( !Number.isInteger(schedule.weekday) || schedule.weekday < 0 || schedule.weekday > 6 || !Number.isInteger(schedule.hour) || schedule.hour < 0 || schedule.hou...)` → `invalidField()`
- 参照: `schedule.hour`, `schedule.hours`, `schedule.minute`, `schedule.type`, `schedule.weekday`

## watchUrlRecords()
- 位置: L126-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `trimAndFilterWatchUrls()`
- 条件付き依存: `if (!normalizedUrls.length)` → `invalidField()`
- 参照: `normalizedUrls.length`

## initialSnapshotRecord()
- 位置: L134-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.log.warn()`, `timestampField()`
- 条件付き依存: `if ( typeof snapshot !== "object" || Array.isArray(snapshot) || typeof snapshot.pageContent !== "string" )` → `invalidField()`
- 参照: `snapshot.capturedAt`, `snapshot.pageContent`

## expiryRecord()
- 位置: L162-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `EXPIRY_REASONS.has()`, `lazy.log.warn()`, `timestampField()`
- 条件付き依存: `if ( typeof expiry !== "object" || Array.isArray(expiry) || !EXPIRY_REASONS.has(expiry.reason) )` → `invalidField()`
- 参照: `expiry.expiredAt`, `expiry.reason`

## historyRecord()
- 位置: L187-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `HISTORY_STATUSES.has()`, `stringField()`, `timestampField()`
- 条件付き依存: `if (!entry || typeof entry !== "object" || Array.isArray(entry))` → `invalidField()`
- 条件付き依存: `if (!HISTORY_STATUSES.has(entry.status))` → `invalidField()`
- 条件付き依存: `if (typeof entry.resultExplanation !== "string")` → `invalidField()`
- 条件付き依存: `if (typeof entry.conditionMet !== "boolean")` → `invalidField()`
- 条件付き依存: `if (entry.errorCode != null)` → `HISTORY_ERROR_CODES.has()`
- 条件付き依存: `if (!HISTORY_ERROR_CODES.has(entry.errorCode))` → `invalidField()`
- 参照: `entry.checkedAt`, `entry.conditionMet`, `entry.errorCode`, `entry.id`, `entry.resultExplanation`, `entry.status`, `record.errorCode`

## sanitizeHistoryRecords()
- 位置: L217-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `historyRecord()`, `lazy.log.warn()`, `records.push()`
- 条件付き依存: `if (recoverInvalid)` → `lazy.log.warn()`
- 条件付き依存: `if (!Array.isArray(history))` → `invalidField()`
- 条件付き依存: `if (!recoverInvalid)` → `invalidField()`
- 条件付き依存: `if (records.length > MAX_HISTORY_ENTRIES)` → `records.slice()`
- 参照: `records.length`

## sanitizeMonitorRecord()
- 位置: L246-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `expiryRecord()`, `initialSnapshotRecord()`, `runCountField()`, `sanitizeHistoryRecords()`, `scheduleRecord()`, `stringField()`, `timestampField()`, `watchUrlRecords()`
- 条件付き依存: `if (!monitor || typeof monitor !== "object" || Array.isArray(monitor))` → `invalidField()`
- 条件付き依存: `if (typeof monitor.enabled !== "boolean")` → `invalidField()`
- 参照: `monitor.activeSince`, `monitor.createdAt`, `monitor.enabled`, `monitor.expiry`, `monitor.history`, `monitor.history.length`, `monitor.id`, `monitor.initialSnapshot`, `monitor.lastMatchAt`, `monitor.lastRunTime`, `monitor.monitorPrompt`, `monitor.nextRunTime`, `monitor.runCount`, `monitor.schedule`, `monitor.title`, `monitor.updatedAt`, `monitor.watchUrls`

## wrapRequest()
- 位置: L296-301
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `request.onerror`, `request.onsuccess`

## request.onsuccess()
- 位置: L298-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 参照: `request.result`

## request.onerror()
- 位置: L299-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`
- 参照: `request.error`

## isNewerSchemaError()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `error?.name`

## MonitorStoreImpl.constructor()
- 位置: L320-331
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AsyncShutdown.profileBeforeChange`, `this.#asyncShutdownBlocker`, `this.#shutdownClient`

## this.#asyncShutdownBlocker()
- 位置: async L322-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeDatabase()`
- 参照: `this.#promiseWrite`, `this.#shutdownBlockerAdded`, `this.#shuttingDown`

## MonitorStoreImpl.listMonitors()
- 位置: async L333-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.parse()`, `db.transaction()`, `first.id.localeCompare()`, `lazy.log.warn()`, `monitors.push()`, `monitors.sort()`, `sanitizeMonitorRecord()`, `this.#ensureDatabase()`, `this.#prepareForOperation()`, `transaction.objectStore()`, `transaction.objectStore(MONITOR_STORE_NAME).getAll()`, `transaction.promiseComplete()`, `transactionComplete.catch()`
- 参照: `first.createdAt`, `second.createdAt`, `second.id`

## MonitorStoreImpl.saveMonitor()
- 位置: async L362-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sanitizeMonitorRecord()`, `store.put()`, `this.#queueWrite()`, `this.#withWriteStore()`

## MonitorStoreImpl.saveMonitors()
- 位置: async L369-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `monitors.map()`, `store.clear()`, `store.put()`, `this.#queueWrite()`, `this.#withWriteStore()`
- 条件付き依存: `if (!Array.isArray(monitors))` → `invalidField()`

## MonitorStoreImpl.deleteMonitor()
- 位置: async L384-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `store.delete()`, `stringField()`, `this.#queueWrite()`, `this.#withWriteStore()`

## MonitorStoreImpl.destroyDatabase()
- 位置: async L391-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeDatabaseConnection()`, `this.#deleteDatabase()`, `this.#queueWrite()`
- 参照: `this.#promiseDb`

## MonitorStoreImpl.close()
- 位置: async L399-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeDatabaseConnection()`
- 条件付き依存: `if (!this.#shuttingDown)` → `this.#removeShutdownBlocker()`
- 参照: `this.#shuttingDown`

## MonitorStoreImpl.#closeDatabaseConnection()
- 位置: async L406-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeDatabase()`
- 条件付き依存: `if (!this.#db && this.#promiseDb)` → `this.#promiseDb.catch()`
- 参照: `this.#db`, `this.#promiseDb`

## MonitorStoreImpl.#withWriteStore()
- 位置: async L415-429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `db.transaction()`, `this.#ensureDatabase()`, `transaction.abort()`, `transaction.objectStore()`, `transaction.promiseComplete()`, `transactionComplete.catch()`

## MonitorStoreImpl.#queueWrite()
- 位置: L431-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `promise .finally()`, `promise .finally(() => { this.#pendingWrites.delete(pendingWrite); }) .catch()`, `this.#pendingWrites.add()`, `this.#pendingWrites.delete()`, `this.#prepareForOperation()`, `this.#promiseWrite.then()`
- 参照: `this.#promiseWrite`

## runTask()
- 位置: L439-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `task()`
- 参照: `pendingWrite.startedAt`

## MonitorStoreImpl.#prepareForOperation()
- 位置: L452-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addShutdownBlocker()`
- 参照: `this.#shuttingDown`

## MonitorStoreImpl.#openDatabase()
- 位置: async L459-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.objectStoreNames.contains()`, `event.target.transaction.objectStore()`, `lazy.IndexedDB.open()`, `store.indexNames.contains()`
- 条件付き依存: `if (!db.objectStoreNames.contains(MONITOR_STORE_NAME))` → `db.createObjectStore()`
- 条件付き依存: `if (!db.objectStoreNames.contains(MONITOR_STORE_NAME))` → `store.createIndex()`
- 条件付き依存: `if (!store.indexNames.contains(CREATED_AT_INDEX))` → `store.createIndex()`
- 条件付き依存: `if (this.#shuttingDown && !this.#pendingWrites.size)` → `database.close()`
- 条件付き依存: `if (this.#shuttingDown && !this.#pendingWrites.size)` → `lazy.log.warn()`
- 参照: `error.message`, `this.#db`, `this.#db.onclose`, `this.#db.onversionchange`, `this.#pendingWrites.size`, `this.#shuttingDown`

## this.#db.onversionchange()
- 位置: L489-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeDatabase()`
- 参照: `this.#promiseDb`

## this.#db.onclose()
- 位置: L493-496
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#db`, `this.#promiseDb`

## MonitorStoreImpl.#ensureDatabase()
- 位置: async L500-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNewerSchemaError()`, `lazy.log.warn()`, `this.#closeDatabase()`, `this.#openDatabase()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#closeDatabase()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#deleteDatabase()`
- 参照: `this.#promiseDb`, `this.#removeDatabaseOnStartup`

## MonitorStoreImpl.#deleteDatabase()
- 位置: async L531-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IndexedDB.deleteDatabase()`, `wrapRequest()`
- 参照: `this.#removeDatabaseOnStartup`

## MonitorStoreImpl.#closeDatabase()
- 位置: L541-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.close()`, `lazy.log.warn()`
- 参照: `db.onclose`, `db.onversionchange`, `error.message`, `this.#db`

## MonitorStoreImpl.#addShutdownBlocker()
- 位置: L557-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#shutdownClient.addBlocker()`
- 参照: `this.#asyncShutdownBlocker`, `this.#shutdownBlockerAdded`

## fetchState()
- 位置: L566-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Date.now()`
- 参照: `pendingWrite.operation`, `pendingWrite.queuedAt`, `pendingWrite.startedAt`, `this.#db`, `this.#pendingWrites`, `this.#shuttingDown`

## MonitorStoreImpl.#removeShutdownBlocker()
- 位置: L580-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#shutdownClient.removeBlocker()`
- 参照: `this.#asyncShutdownBlocker`, `this.#shutdownBlockerAdded`

## MonitorStoreImpl.#removeDatabaseOnStartup()
- 位置: L589-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## MonitorStoreImpl.#removeDatabaseOnStartup()
- 位置: L596-598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## MonitorStoreImpl.databaseName()
- 位置: L600-602
- 役割: (未記入)
- 触るとき: (未記入)

## MonitorStoreImpl.databaseVersion()
- 位置: L604-606
- 役割: (未記入)
- 触るとき: (未記入)

## MonitorStoreImpl.objectStoreName()
- 位置: L608-610
- 役割: (未記入)
- 触るとき: (未記入)
