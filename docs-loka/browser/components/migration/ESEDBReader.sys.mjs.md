# browser/components/migration/ESEDBReader.sys.mjs

source: browser/components/migration/ESEDBReader.sys.mjs
source-hash: 479bc2fb9b493f97f6f219f6b5f00510b626fd30
lines: 800

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## getColTypeName()
- 位置: L65-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(COLUMN_TYPES).find()`

## convertESEError()
- 位置: L108-135
- 役割: (未記入)
- 触るとき: (未記入)

## handleESEError()
- 位置: L137-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `method.apply()`, `parseInt()`, `rv.toString()`
- 条件付き依存: `if (errorLog)` → `lazy.log.error()`
- 条件付き依存: `if (shouldThrow)` → `convertESEError()`
- 条件付き依存: `if (resultCode > 0 && errorLog)` → `lazy.log.warn()`

## declareESEFunction()
- 位置: L166-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["Jet" + methodName, ctypes.winapi_abi, ESE.JET_ERR].concat()`, `gLibs.ese.declare.apply()`, `handleESEError()`
- 参照: `ESE.JET_ERR`, `ctypes.winapi_abi`, `gLibs.ese`

## declareESEFunctions()
- 位置: L181-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `declareESEFunction()`
- 参照: `ESE.JET_API_ITEM`, `ESE.JET_API_ITEM.ptr`, `ESE.JET_COLUMNID`, `ESE.JET_DBID`, `ESE.JET_DBID.ptr`, `ESE.JET_GRBIT`, `ESE.JET_INSTANCE`, `ESE.JET_INSTANCE.ptr`, `ESE.JET_PCWSTR`, `ESE.JET_SESID`, `ESE.JET_SESID.ptr`, `ESE.JET_TABLEID`, `ESE.JET_TABLEID.ptr`, `ctypes.long`, `ctypes.unsigned_long`, `ctypes.unsigned_long.ptr`, `ctypes.voidptr_t`

## unloadLibraries()
- 位置: L287-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `gLibs.ese.close()`, `gLibs.kernel.close()`, `lazy.log.debug()`
- 条件付き依存: `if (gOpenDBs.size)` → `lazy.log.error()`
- 条件付き依存: `if (gOpenDBs.size)` → `gOpenDBs.values()`
- 条件付き依存: `if (gOpenDBs.size)` → `db._close()`
- 参照: `gLibs.ese`, `gLibs.kernel`, `gOpenDBs.size`

## loadLibraries()
- 位置: L304-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `ctypes.open()`, `declareESEFunctions()`, `gLibs.kernel.declare()`
- 参照: `KERNEL.FILETIME.ptr`, `KERNEL.FileTimeToSystemTime`, `KERNEL.SYSTEMTIME.ptr`, `ctypes.int`, `ctypes.winapi_abi`, `gLibs.ese`, `gLibs.kernel`
- XPCOM: `Services.obs`

## ESEDB()
- 位置: L319-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.info()`, `this._init()`
- 参照: `this._references`, `this.dbPath`, `this.logPath`, `this.rootPath`

## _init()
- 位置: L340-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._internalOpen()`, `this.incrementReferenceCounter()`
- 条件付き依存: `if (!gLibs.ese)` → `loadLibraries()`
- 参照: `gLibs.ese`

## _internalOpen()
- 位置: L348-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ESE.AttachDatabaseW()`, `ESE.BeginSessionW()`, `ESE.CreateInstanceW()`, `ESE.GetDatabaseFileInfoW()`, `ESE.Init()`, `ESE.OpenDatabaseW()`, `ESE.SetSystemParameterW()`, `console.error()`, `ctypes.UInt64.lo()`, `dbinfo.address()`, `gOpenDBs.set()`, `this._close()`, `this._dbId.address()`, `this._instanceId.address()`, `this._sessionId.address()`
- 参照: `ESE.JET_DBID`, `ESE.JET_INSTANCE`, `ESE.JET_SESID`, `ctypes.unsigned_long`, `ctypes.unsigned_long.size`, `dbinfo.value`, `this._attached`, `this._dbId`, `this._instanceCreated`, `this._instanceId`, `this._opened`, `this._sessionCreated`, `this._sessionId`, `this.dbPath`, `this.logPath`, `this.rootPath`

## checkForColumn()
- 位置: L433-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getColumnInfo()`
- 参照: `this._opened`

## tableExists()
- 位置: L447-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ESE.FailSafeCloseTable()`, `ESE.ManualOpenTableW()`, `tableId.address()`
- 条件付き依存: `if (rv < 0)` → `lazy.log.error()`
- 条件付き依存: `if (rv < 0)` → `convertESEError()`
- 条件付き依存: `if (rv > 0)` → `lazy.log.error()`
- 参照: `ESE.JET_TABLEID`, `this._dbId`, `this._opened`, `this._sessionId`

## tableItems()
- 位置: L477-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ESE.ManualMove()`, `ESE.ManualRetrieveColumn()`, `buffer.address()`, `this._closeTable()`, `this._convertResult()`, `this._getBufferForColumn()`, `this._getColumnInfo()`, `this._openTable()`
- 条件付き依存: `if (rv == -1603 /* JET_errNoCurrentRecord */)` → `this._closeTable()`
- 条件付き依存: `if (rv != 0)` → `convertESEError()`
- 条件付き依存: `if (tableOpened)` → `this._closeTable()`
- 参照: `column.id`, `column.name`, `this._opened`, `this._sessionId`

## _openTable()
- 位置: L535-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ESE.OpenTableW()`, `tableId.address()`
- 参照: `ESE.JET_TABLEID`, `this._dbId`, `this._sessionId`

## _getBufferForColumn()
- 位置: L549-567
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.type == "string")` → `ctypes.ArrayType()`
- 条件付き依存: `if (column.type == "guid")` → `ctypes.ArrayType()`
- 参照: `KERNEL.FILETIME`, `buffer.constructor.size`, `column.dbSize`, `column.type`, `ctypes.char16_t`, `ctypes.uint8_t`

## _convertResult()
- 位置: L569-638
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(err == 1004))` → `console.error()`
- 条件付き依存: `if (!(err == 1004))` → `convertESEError()`
- 条件付き依存: `if (column.type == "string")` → `buffer.readString()`
- 条件付き依存: `if (buffer.length != 16)` → `console.error()`
- 条件付き依存: `if (column.type == "guid")` → `buffer.addressOfElement()`
- 条件付き依存: `if (column.type == "guid")` → `("0" + byteValue.toString(16)).substr()`
- 条件付き依存: `if (column.type == "guid")` → `byteValue.toString()`
- 条件付き依存: `if (column.type == "date")` → `KERNEL.FileTimeToSystemTime()`
- 条件付き依存: `if (column.type == "date")` → `buffer.address()`
- 条件付き依存: `if (column.type == "date")` → `systemTime.address()`
- 条件付き依存: `if (column.type == "date")` → `Date.UTC()`
- 参照: `KERNEL.SYSTEMTIME`, `buffer.addressOfElement(i).contents`, `buffer.length`, `buffer.value`, `column.id`, `column.name`, `column.type`, `ctypes.winLastError`, `systemTime.wDay`, `systemTime.wHour`, `systemTime.wMilliseconds`, `systemTime.wMinute`, `systemTime.wMonth`, `systemTime.wSecond`, `systemTime.wYear`

## _getColumnInfo()
- 位置: L640-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ESE.GetColumnInfoW()`, `columnInfoFromDB.address()`, `columnInfoFromDB.cbMax.toString()`, `columnInfoFromDB.coltyp.toString()`, `parseInt()`, `rv.push()`
- 条件付き依存: `if ( dbType != COLUMN_TYPES.JET_coltypLongText && dbType != COLUMN_TYPES.JET_coltypText )` → `getColTypeName()`
- 条件付き依存: `if (dbType != COLUMN_TYPES.JET_coltypBit)` → `getColTypeName()`
- 条件付き依存: `if (dbType != COLUMN_TYPES.JET_coltypLongLong)` → `getColTypeName()`
- 条件付き依存: `if (dbType != COLUMN_TYPES.JET_coltypGUID)` → `getColTypeName()`
- 参照: `COLUMN_TYPES.JET_coltypBit`, `COLUMN_TYPES.JET_coltypGUID`, `COLUMN_TYPES.JET_coltypLongLong`, `COLUMN_TYPES.JET_coltypLongText`, `COLUMN_TYPES.JET_coltypText`, `ESE.JET_COLUMNDEF`, `ESE.JET_COLUMNDEF.size`, `column.name`, `column.type`, `columnInfoFromDB.columnid`, `this._dbId`, `this._sessionId`

## _closeTable()
- 位置: L722-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ESE.FailSafeCloseTable()`
- 参照: `this._sessionId`

## _close()
- 位置: L726-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gOpenDBs.delete()`, `this._internalClose()`
- 参照: `this.dbPath`

## _internalClose()
- 位置: L731-753
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._opened)` → `lazy.log.debug()`
- 条件付き依存: `if (this._opened)` → `ESE.FailSafeCloseDatabase()`
- 条件付き依存: `if (this._attached)` → `lazy.log.debug()`
- 条件付き依存: `if (this._attached)` → `ESE.FailSafeDetachDatabaseW()`
- 条件付き依存: `if (this._sessionCreated)` → `lazy.log.debug()`
- 条件付き依存: `if (this._sessionCreated)` → `ESE.FailSafeEndSession()`
- 条件付き依存: `if (this._instanceCreated)` → `lazy.log.debug()`
- 条件付き依存: `if (this._instanceCreated)` → `ESE.FailSafeTerm()`
- 参照: `this._attached`, `this._dbId`, `this._instanceCreated`, `this._instanceId`, `this._opened`, `this._sessionCreated`, `this._sessionId`, `this.dbPath`

## incrementReferenceCounter()
- 位置: L755-757
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._references`

## decrementReferenceCounter()
- 位置: L759-764
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._references <= 0)` → `this._close()`
- 参照: `this._references`

## openDB()
- 位置: L768-778
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gOpenDBs.has()`
- 条件付き依存: `if (gOpenDBs.has(dbFilePath))` → `gOpenDBs.get()`
- 条件付き依存: `if (gOpenDBs.has(dbFilePath))` → `db.incrementReferenceCounter()`
- 参照: `dbFile.path`, `logDir.path`, `rootDir.path`

## dbLocked()
- 位置: async L780-792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/profile/migrator/edgemigrationutils;1" ].createInstance()`, `utils.isDbLocked()`
- 条件付き依存: `if (locked)` → `console.error()`
- 参照: `Ci.nsIEdgeMigrationUtils`, `dbFile.path`
- XPCOM: [`nsIEdgeMigrationUtils`](nsIEdgeMigrationUtils.idl.md) / `@mozilla.org/profile/migrator/edgemigrationutils;1`

## closeDB()
- 位置: L794-796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.decrementReferenceCounter()`
