# browser/components/migration/SafariProfileMigrator.sys.mjs

source: browser/components/migration/SafariProfileMigrator.sys.mjs
source-hash: a84f6d4edf3d2c34cd0e53cd0b1d3f2c093fad78
lines: 688

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `new Date("2001-01-01T00:00:00-00:00").getTime()`

## parseNSDate()
- 位置: L22-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNaN()`, `parseFloat()`

## msToNSDate()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`

## Bookmarks()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._file`

## B_migrate()
- 位置: L41-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `console.error()`, `dict.get()`, `lazy.PropertyListUtils.read()`, `this._migrateRootCollection()`
- 参照: `this.READING_LIST_COLLECTION`, `this.ROOT_COLLECTION`, `this._file`

## _migrateRootCollection()
- 位置: async L82-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FileUtils.getDir()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `PathUtils.join()`, `console.error()`, `this._migrateCollection()`
- 条件付き依存: `if (rows)` → `row.getResultByName()`
- 条件付き依存: `if (rows)` → `uniqueURL.endsWith()`
- 条件付き依存: `if (uniqueURL.endsWith("/"))` → `uniqueURL.replace()`
- 条件付き依存: `if (rows)` → `bookmarkURLToUUIDMap.set()`
- 参照: `FileUtils.getDir("ULibDir", [ "Safari", "Favicon Cache", ]).path`, `new URL(row.getResultByName("url")).href`

## _migrateCollection()
- 位置: async L139-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.getLocalizedString()`, `MigrationUtils.insertBookmarkWrapper()`, `this._migrateEntries()`
- 条件付き依存: `if (aCollection == this.ROOT_COLLECTION)` → `entry.get()`
- 条件付き依存: `if (aCollection == this.ROOT_COLLECTION)` → `entry.has()`
- 条件付き依存: `if (type == "WebBookmarkTypeList" && entry.has("Children"))` → `entry.get()`
- 条件付き依存: `if (title == "BookmarksBar")` → `this._migrateCollection()`
- 条件付き依存: `if (title == "BookmarksMenu")` → `this._migrateCollection()`
- 条件付き依存: `if (title == "com.apple.ReadingList")` → `this._migrateCollection()`
- 条件付き依存: `if (!(title == "com.apple.ReadingList"))` → `entry.get()`
- 条件付き依存: `if (entry.get("ShouldOmitFromUI") !== true)` → `entriesFiltered.push()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf")` → `entriesFiltered.push()`
- 参照: `entriesFiltered.length`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `lazy.PlacesUtils.bookmarks.menuGuid`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `lazy.PlacesUtils.bookmarks.unfiledGuid`, `this.MENU_COLLECTION`, `this.READING_LIST_COLLECTION`, `this.ROOT_COLLECTION`, `this.TOOLBAR_COLLECTION`

## _migrateEntries()
- 位置: async L245-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.insertManyBookmarksWrapper()`, `MigrationUtils.insertManyFavicons()`, `MigrationUtils.insertManyFavicons(favicons).catch()`, `this._convertEntries()`
- 参照: `console.error`

## _convertEntries()
- 位置: async L270-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FileUtils.getDir()`, `entry.get()`, `entry.has()`
- 条件付き依存: `if (type == "WebBookmarkTypeList" && entry.has("Children"))` → `this._convertEntries()`
- 条件付き依存: `if (type == "WebBookmarkTypeList" && entry.has("Children"))` → `entry.get()`
- 条件付き依存: `if (type == "WebBookmarkTypeList" && entry.has("Children"))` → `favicons.push()`
- 条件付き依存: `if (type == "WebBookmarkTypeList" && entry.has("Children"))` → `convertedEntries.push()`
- 条件付き依存: `if (!(type == "WebBookmarkTypeList" && entry.has("Children")))` → `entry.has()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `entry.get()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `URL.canParse()`
- 条件付き依存: `if (!URL.canParse(url))` → `console.error()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `entry.has()`
- 条件付き依存: `if (entry.has("URIDictionary"))` → `entry.get("URIDictionary").get()`
- 条件付き依存: `if (entry.has("URIDictionary"))` → `entry.get()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `convertedEntries.push()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `Services.io.newURI()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `uriSpec.endsWith()`
- 条件付き依存: `if (uriSpec.endsWith("/"))` → `uriSpec.replace()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `bookmarkURLToUUIDMap.get()`
- 条件付き依存: `if (uuid)` → `lazy.PlacesUtils.md5(uuid, { format: "hex", }).toUpperCase()`
- 条件付き依存: `if (uuid)` → `lazy.PlacesUtils.md5()`
- 条件付き依存: `if (uuid)` → `PathUtils.join()`
- 条件付き依存: `if (uuid)` → `IOUtils.read()`
- 条件付き依存: `if (uuid)` → `favicons.push()`
- 条件付き依存: `if (type == "WebBookmarkTypeLeaf" && entry.has("URLString"))` → `console.error()`
- 参照: `FileUtils.getDir("ULibDir", [ "Safari", "Favicon Cache", ]).path`, `convertedChildren.convertedEntries`, `convertedChildren.favicons`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `uri.spec`
- XPCOM: `Services.io`

## GetHistoryResource()
- 位置: async L347-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `FileUtils.getDir()`, `IOUtils.read()`, `console.error()`, `msToNSDate()`
- 条件付き依存: `if (canReadHistory)` → `MigrationUtils.getRowsFromDBWithoutLocks()`
- 条件付き依存: `if (canReadHistory)` → `countResult[0].getResultByName()`
- 参照: `FileUtils.getDir("ULibDir", ["Safari", "History.db"]).path`, `MigrationUtils.HISTORY_MAX_AGE_IN_MILLISECONDS`, `MigrationUtils.resourceTypes.HISTORY`

## migrate()
- 位置: async L400-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `this._migrate()`

## _migrate()
- 位置: async L404-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.getRowsFromDBWithoutLocks()`, `MigrationUtils.insertVisitsWrapper()`, `console.error()`, `pageInfos.push()`, `parseNSDate()`, `row.getResultByName()`
- 条件付き依存: `if (!historyRows.length)` → `console.log()`
- 参照: `historyRows.length`, `lazy.PlacesUtils.history.TRANSITIONS.TYPED`

## MainPreferencesPropertyList()
- 位置: L458-461
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._callbacks`, `this._file`

## MPPL_read()
- 位置: L469-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callbacks.push()`
- 条件付き依存: `if ("_dict" in this)` → `aCallback()`
- 条件付き依存: `if (!alreadyReading)` → `lazy.PropertyListUtils.read()`
- 条件付き依存: `if (!alreadyReading)` → `callback()`
- 条件付き依存: `if (!alreadyReading)` → `console.error()`
- 条件付き依存: `if (!alreadyReading)` → `this._callbacks.splice()`
- 参照: `this._callbacks`, `this._callbacks.length`, `this._dict`, `this._file`

## SearchStrings()
- 位置: L493-495
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._mainPreferencesPropertyList`

## SS_migrate()
- 位置: L499-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.wrapMigrateFunction()`, `this._mainPreferencesPropertyList.read()`

## migrateSearchStrings()
- 位置: L501-517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDict.has()`
- 条件付き依存: `if (aDict.has("RecentSearchStrings"))` → `aDict.get()`
- 条件付き依存: `if (recentSearchStrings && recentSearchStrings.length)` → `recentSearchStrings.map()`
- 条件付き依存: `if (recentSearchStrings && recentSearchStrings.length)` → `lazy.FormHistory.update()`
- 参照: `recentSearchStrings.length`

## SafariProfileMigrator.key()
- 位置: L526-528
- 役割: (未記入)
- 触るとき: (未記入)

## SafariProfileMigrator.displayNameL10nID()
- 位置: L530-532
- 役割: (未記入)
- 触るとき: (未記入)

## SafariProfileMigrator.brandImage()
- 位置: L534-536
- 役割: (未記入)
- 触るとき: (未記入)

## SafariProfileMigrator.getResources()
- 位置: async L538-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FileUtils.getDir()`, `GetHistoryResource()`, `Promise.all()`, `profileDir.exists()`, `pushProfileFileResource()`, `resources.filter()`, `resources.push()`
- 条件付き依存: `if (prefs)` → `resources.push()`
- 参照: `this.mainPreferencesPropertyList`

## pushProfileFileResource()
- 位置: L545-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `file.append()`, `file.exists()`, `profileDir.clone()`
- 条件付き依存: `if (file.exists())` → `resources.push()`

## SafariProfileMigrator.getLastUsedDate()
- 位置: async L574-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FileUtils.getDir()`, `IOUtils.stat()`, `IOUtils.stat(path) .then()`, `IOUtils.stat(path) .then(info => info.lastModified) .catch()`, `Math.max()`, `PathUtils.join()`, `Promise.all()`, `["Bookmarks.plist", "History.db"].map()`
- 参照: `info.lastModified`, `profileDir.path`

## SafariProfileMigrator.hasPermissions()
- 位置: async L588-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FileUtils.getDir()`, `IOUtils.exists()`
- 条件付き依存: `if (historyExists)` → `IOUtils.read()`
- 条件付き依存: `if (bookmarksExists)` → `IOUtils.read()`
- 条件付き依存: `if (faviconsExists)` → `IOUtils.read()`
- 参照: `bookmarkTarget.path`, `faviconTarget.path`, `historyTarget.path`, `this._hasPermissions`

## SafariProfileMigrator.getPermissions()
- 位置: async L626-646
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `FileUtils.getDir()`, `fp.init()`, `fp.open()`, `this.hasPermissions()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeGetFolder`, `Ci.nsIFilePicker.returnCancel`, `fp.displayDirectory`, `fp.filterIndex`, `win?.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## SafariProfileMigrator.canGetPermissions()
- 位置: async L648-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.canGetPermissionsOnPlatform()`
- 条件付き依存: `if (await MigrationUtils.canGetPermissionsOnPlatform())` → `FileUtils.getDir()`
- 条件付き依存: `if (await MigrationUtils.canGetPermissionsOnPlatform())` → `IOUtils.exists()`
- 参照: `profileDir.path`

## SafariProfileMigrator.showsManualPasswordImport()
- 位置: L664-668
- 役割: (未記入)
- 触るとき: (未記入)

## SafariProfileMigrator.mainPreferencesPropertyList()
- 位置: L670-686
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._mainPreferencesPropertyList === undefined)` → `FileUtils.getDir()`
- 条件付き依存: `if (this._mainPreferencesPropertyList === undefined)` → `file.exists()`
- 条件付き依存: `if (file.exists())` → `file.append()`
- 条件付き依存: `if (file.exists())` → `file.exists()`
- 参照: `this._mainPreferencesPropertyList`
