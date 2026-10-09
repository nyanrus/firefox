# browser/components/migration/EdgeProfileMigrator.sys.mjs

source: browser/components/migration/EdgeProfileMigrator.sys.mjs
source-hash: 37e9116237ee94440c64c55fa3c6312e1fd36415
lines: 571

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `MSMigrationUtils.getEdgeLocalDataFolder()`, `edgeDir.appendRelativePath()`, `edgeDir.clone()`, `edgeDir.exists()`, `edgeDir.isDirectory()`, `edgeDir.isReadable()`, `expectedLocation.appendRelativePath()`, `expectedLocation.exists()`, `expectedLocation.isFile()`, `expectedLocation.isReadable()`

## readTableFromEdgeDB()
- 位置: L69-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `database.tableItems()`, `filterFn()`, `lazy.ESEDBReader.openDB()`, `logFile.append()`
- 条件付き依存: `if (typeof columns == "function")` → `columns()`
- 条件付き依存: `if (!filterFn || filterFn(row))` → `rows.push()`
- 条件付き依存: `if (database)` → `lazy.ESEDBReader.closeDB()`
- 参照: `dbFile.parent`, `dbFile.path`, `lazy.gEdgeDatabase`

## EdgeTypedURLMigrator()
- 位置: L111-111
- 役割: (未記入)
- 触るとき: (未記入)

## _typedURLs()
- 位置: L116-121
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__typedURLs)` → `MSMigrationUtils.getTypedURLs()`
- 参照: `this.__typedURLs`

## exists()
- 位置: L123-125
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._typedURLs.size`

## migrate()
- 位置: L127-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_PROTOCOLS.has()`, `Date.now()`, `MigrationUtils.insertVisitsWrapper()`, `MigrationUtils.insertVisitsWrapper(pageInfos).then()`, `URL.parse()`, `aCallback()`, `lazy.PlacesUtils.toDate()`, `pageInfos.push()`
- 条件付き依存: `if (!pageInfos.length)` → `aCallback()`
- 参照: `MigrationUtils.HISTORY_MAX_AGE_IN_MILLISECONDS`, `lazy.PlacesUtils.history.TRANSITIONS.TYPED`, `pageInfos.length`, `this._typedURLs`, `typedURLs.size`, `url.protocol`

## EdgeTypedURLDBMigrator()
- 位置: L169-171
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dbOverride`

## db()
- 位置: L176-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.gEdgeDatabase`, `this.dbOverride`

## exists()
- 位置: L180-182
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.db`

## migrate()
- 位置: L184-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `console.error()`, `this._migrateTypedURLsFromDB()`, `this._migrateTypedURLsFromDB().then()`

## _migrateTypedURLsFromDB()
- 位置: async L194-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_PROTOCOLS.has()`, `Date.now()`, `MigrationUtils.insertVisitsWrapper()`, `URL.parse()`, `lazy.ESEDBReader.dbLocked()`, `pageInfos.push()`, `readTableFromEdgeDB()`
- 参照: `MigrationUtils.HISTORY_MAX_AGE_IN_MILLISECONDS`, `lazy.PlacesUtils.history.TRANSITIONS.TYPED`, `this.db`, `typedUrlInfo.AccessDateTimeUTC`, `typedUrlInfo.URL`, `typedUrls.length`, `url.protocol`

## EdgeReadingListMigrator()
- 位置: L248-250
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dbOverride`

## db()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.gEdgeDatabase`, `this.dbOverride`

## exists()
- 位置: L259-261
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.db`

## migrate()
- 位置: L263-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `console.error()`, `this._migrateReadingList()`, `this._migrateReadingList(lazy.PlacesUtils.bookmarks.menuGuid).then()`
- 参照: `lazy.PlacesUtils.bookmarks.menuGuid`

## _migrateReadingList()
- 位置: async L273-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.insertManyBookmarksWrapper()`, `URL.canParse()`, `bookmarks.push()`, `lazy.ESEDBReader.dbLocked()`, `readTableFromEdgeDB()`, `this._ensureReadingListFolder()`
- 参照: `item.AddedDate`, `item.Title`, `item.URL`, `readingListItems.length`, `this.db`

## columnFn()
- 位置: L277-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.checkForColumn()`
- 条件付き依存: `if ( isDeletedColumn && isDeletedColumn.dbType == lazy.ESEDBReader.COLUMN_TYPES.JET_coltypBit )` → `columns.push()`
- 参照: `isDeletedColumn.dbType`, `lazy.ESEDBReader.COLUMN_TYPES.JET_coltypBit`

## filterFn()
- 位置: L295-297
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `row.IsDeleted`

## _ensureReadingListFolder()
- 位置: async L322-337
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__readingListFolderGuid)` → `MigrationUtils.getLocalizedString()`
- 条件付き依存: `if (!this.__readingListFolderGuid)` → `MigrationUtils.insertBookmarkWrapper()`
- 参照: `( await MigrationUtils.insertBookmarkWrapper(folderSpec) ).guid`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `this.__readingListFolderGuid`

## EdgeBookmarksMigrator()
- 位置: L340-342
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dbOverride`

## db()
- 位置: L347-349
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.gEdgeDatabase`, `this.dbOverride`

## TABLE_NAME()
- 位置: L351-353
- 役割: (未記入)
- 触るとき: (未記入)

## exists()
- 位置: L355-360
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._exists`, `this.db`

## migrate()
- 位置: L362-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `console.error()`, `this._migrateBookmarks()`, `this._migrateBookmarks().then()`

## _migrateBookmarks()
- 位置: async L372-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ESEDBReader.dbLocked()`, `this._fetchBookmarksFromDB()`
- 条件付き依存: `if (toplevelBMs.length)` → `MigrationUtils.insertManyBookmarksWrapper()`
- 条件付き依存: `if (toolbarBMs.length)` → `MigrationUtils.insertManyBookmarksWrapper()`
- 参照: `lazy.PlacesUtils.bookmarks.menuGuid`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `this.db`, `toolbarBMs.length`, `toplevelBMs.length`

## _fetchBookmarksFromDB()
- 位置: L387-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `folderMap.has()`, `readTableFromEdgeDB()`
- 条件付き依存: `if (!bookmark.IsFolder)` → `URL.canParse()`
- 条件付き依存: `if (!URL.canParse(bookmark.URL))` → `console.error()`
- 条件付き依存: `if (!folderMap.has(bookmark.ParentId))` → `toplevelBMs.push()`
- 条件付き依存: `if (!(!folderMap.has(bookmark.ParentId)))` → `folderMap.get()`
- 条件付き依存: `if (parent.Title == "_Favorites_Bar_")` → `toolbarBMs.push()`
- 条件付き依存: `if (!(!folderMap.has(bookmark.ParentId)))` → `parent._childrenRef.push()`
- 参照: `bookmark.DateUpdated`, `bookmark.IsFolder`, `bookmark.ParentId`, `bookmark.Title`, `bookmark.URL`, `bookmark._childrenRef`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `parent.Title`, `parent._childrenRef`, `this.TABLE_NAME`, `this.db`

## filterFn()
- 位置: L398-406
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (row.IsFolder)` → `folderMap.set()`
- 参照: `row.IsDeleted`, `row.IsFolder`, `row.ItemId`

## getCookiesPaths()
- 位置: L464-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MSMigrationUtils.getEdgeLocalDataFolder()`
- 条件付き依存: `if (edgeDir)` → `edgeDir.append()`
- 条件付き依存: `if (edgeDir)` → `edgeDir.clone()`
- 条件付き依存: `if (edgeDir)` → `folder.appendRelativePath()`
- 条件付き依存: `if (edgeDir)` → `folder.exists()`
- 条件付き依存: `if (edgeDir)` → `folder.isReadable()`
- 条件付き依存: `if (edgeDir)` → `folder.isDirectory()`
- 条件付き依存: `if (folder.exists() && folder.isReadable() && folder.isDirectory())` → `folders.push()`

## EdgeProfileMigrator.key()
- 位置: L485-487
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.displayNameL10nID()
- 位置: L489-491
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.brandImage()
- 位置: L493-495
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.getBookmarksMigratorForTesting()
- 位置: L497-499
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.getReadingListMigratorForTesting()
- 位置: L501-503
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.getHistoryDBMigratorForTesting()
- 位置: L505-507
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.getHistoryRegistryMigratorForTesting()
- 位置: L509-511
- 役割: (未記入)
- 触るとき: (未記入)

## EdgeProfileMigrator.getResources()
- 位置: L513-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MSMigrationUtils.getWindowsVaultFormPasswordsMigrator()`, `resources.filter()`, `resources.push()`
- 参照: `r.exists`, `windowsVaultFormPasswordsMigrator.name`

## EdgeProfileMigrator.getLastUsedDate()
- 位置: async L527-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.stat()`, `IOUtils.stat(path) .then()`, `IOUtils.stat(path) .then(info => info.lastModified) .catch()`, `MSMigrationUtils.getTypedURLs()`, `Math.max.apply()`, `PathUtils.join()`, `Promise.all()`, `Promise.all(datePromises).then()`, `[logFilePath, dbPath, ...getCookiesPaths()].map()`, `datePromises.push()`, `getCookiesPaths()`, `resolve()`, `this.getSourceProfiles()`, `typedURLs.values()`
- 条件付き依存: `if (sourceProfiles !== null || !lazy.gEdgeDatabase)` → `Promise.resolve()`
- 参照: `info.lastModified`, `lazy.gEdgeDatabase`, `lazy.gEdgeDatabase.parent.path`, `lazy.gEdgeDatabase.path`

## EdgeProfileMigrator.getSourceProfiles()
- 位置: L567-569
- 役割: (未記入)
- 触るとき: (未記入)
