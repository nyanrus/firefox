# browser/components/migration/360seMigrationUtils.sys.mjs

source: browser/components/migration/360seMigrationUtils.sys.mjs
source-hash: fb91de9958df745faa7ba4b30695e0e16d0372bb
lines: 188

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## Bookmarks()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aProfileFolder.clone()`, `file.append()`
- 参照: `this._file`

## exists()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._file.exists()`, `this._file.isReadable()`

## migrate()
- 位置: L35-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `connection.close()`, `connection.execute()`, `console.error()`, `folderMap.has()`, `lazy.Sqlite.openConnection()`, `parseInt()`, `row.getResultByName()`
- 条件付き依存: `if (is_folder)` → `folderMap.set()`
- 条件付き依存: `if (!(is_folder))` → `URL.canParse()`
- 条件付き依存: `if (!URL.canParse(url))` → `console.error()`
- 条件付き依存: `if (folderMap.has(parent_id))` → `folderMap.get(parent_id).children.push()`
- 条件付き依存: `if (folderMap.has(parent_id))` → `folderMap.get()`
- 条件付き依存: `if (parent_id === 0)` → `toolbarBMs.push()`
- 条件付き依存: `if (toolbarBMs.length)` → `MigrationUtils.insertManyBookmarksWrapper()`
- 参照: `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `this._file.path`, `toolbarBMs.length`

## getAlternativeBookmarks()
- 位置: async L113-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.getChildren()`, `PathUtils.filename()`, `PathUtils.join()`, `PathUtils.parent()`, `lazy.filenamesRegex.exec()`, `matches[1].replace()`
- 条件付き依存: `if (await IOUtils.exists(bookmarksPath))` → `IOUtils.stat()`
- 条件付き依存: `if (await IOUtils.exists(bookmarksPath))` → `console.error()`
- 条件付き依存: `if (subDir)` → `PathUtils.join()`
- 条件付き依存: `if (subDir)` → `IOUtils.exists()`
- 条件付き依存: `if (await IOUtils.exists(legacyBookmarksPath))` → `IOUtils.stat()`
- 条件付き依存: `if (await IOUtils.exists(legacyBookmarksPath))` → `console.error()`
- 条件付き依存: `if (PathUtils.filename(path) === kBookmarksFileName)` → `this.getLegacyBookmarksResource()`
- 条件付き依存: `if (PathUtils.filename(path) === kBookmarksFileName)` → `PathUtils.parent()`
- 参照: `localState.sync_login_info`, `localState.sync_login_info.filepath`

## getLegacyBookmarksResource()
- 位置: L174-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `console.error()`, `parentFolder.initWithPath()`
- 参照: `Ci.nsIFile`, `bookmarks.exists`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/file/local;1`
