# browser/components/migration/MSMigrationUtils.sys.mjs

source: browser/components/migration/MSMigrationUtils.sys.mjs
source-hash: 6736c2d35274c70bf4abcd4d80f141af030441ee
lines: 747

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## CtypesKernelHelpers()
- 位置: L39-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctypes.open()`, `this._libs.kernel32.declare()`, `this.finalize()`
- 参照: `ctypes.StructType`, `ctypes.winapi_abi`, `this._functions`, `this._functions.FileTimeToSystemTime`, `this._libs`, `this._libs.kernel32`, `this._structs`, `this._structs.FILETIME`, `this._structs.FILETIME.ptr`, `this._structs.SYSTEMTIME`, `this._structs.SYSTEMTIME.ptr`, `wintypes.BOOL`, `wintypes.DWORD`, `wintypes.WORD`

## finalize()
- 位置: L79-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lib.close()`
- 参照: `this._functions`, `this._libs`, `this._structs`

## fileTimeToSecondsSinceEpoch()
- 位置: L102-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.UTC()`, `Math.floor()`, `fileTime.address()`, `systemTime.address()`, `this._functions.FileTimeToSystemTime()`, `this._structs.FILETIME()`, `this._structs.SYSTEMTIME()`
- 参照: `ctypes.winLastError`, `fileTime.dwHighDateTime`, `fileTime.dwLowDateTime`, `systemTime.wDay`, `systemTime.wHour`, `systemTime.wMilliseconds`, `systemTime.wMinute`, `systemTime.wMonth`, `systemTime.wSecond`, `systemTime.wYear`

## CtypesVaultHelpers()
- 位置: L131-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctypes.open()`, `this._vaultcliLib.declare()`, `this.finalize()`, `wintypes.CHAR.array()`, `wintypes.DWORD.array()`
- 参照: `ctypes.StructType`, `ctypes.voidptr_t`, `ctypes.winapi_abi`, `this._functions`, `this._functions.VaultCloseVault`, `this._functions.VaultEnumerateItems`, `this._functions.VaultFree`, `this._functions.VaultGetItem`, `this._functions.VaultOpenVault`, `this._structs`, `this._structs.GUID`, `this._structs.GUID.ptr`, `this._structs.VAULT_ELEMENT`, `this._structs.VAULT_ELEMENT.ptr`, `this._structs.VAULT_ELEMENT.ptr.ptr`, `this._structs.VAULT_ITEM_ELEMENT`, `this._structs.VAULT_ITEM_ELEMENT.ptr`, `this._vaultcliLib`, `wintypes.DWORD`, `wintypes.LPCWSTR`, `wintypes.PDWORD`, `wintypes.VOIDP`, `wintypes.VOIDP.ptr`

## finalize()
- 位置: L252-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._vaultcliLib.close()`
- 参照: `this._functions`, `this._structs`, `this._vaultcliLib`

## getEdgeLocalDataFolder()
- 位置: L263-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `console.error()`, `dirEntries.hasMoreElements()`, `edgeDir.append()`, `edgeDir.exists()`, `edgeDir.isDirectory()`, `edgeDir.isReadable()`, `packages.append()`, `packages.clone()`, `subDir.isDirectory()`, `subDir.isReadable()`, `subDir.leafName.startsWith()`
- 条件付き依存: `if (gEdgeDir)` → `gEdgeDir.clone()`
- 条件付き依存: `if (edgeDir.exists() && edgeDir.isReadable() && edgeDir.isDirectory())` → `edgeDir.clone()`
- 条件付き依存: `if ( subDir.leafName.startsWith("Microsoft.MicrosoftEdge") && subDir.isReadable() && subDir.isDirectory() )` → `subDir.clone()`
- 参照: `Ci.nsIFile`, `dirEntries.nextFile`, `packages.directoryEntries`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## Bookmarks()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._migrationType`

## exists()
- 位置: L306-308
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._favoritesFolder`

## importedAppLabel()
- 位置: L310-314
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `MSMigrationUtils.MIGRATION_TYPE_IE`, `this._migrationType`

## _favoritesFolder()
- 位置: L317-339
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._migrationType == MSMigrationUtils.MIGRATION_TYPE_IE)` → `Services.dirsvc.get()`
- 条件付き依存: `if (this._migrationType == MSMigrationUtils.MIGRATION_TYPE_IE)` → `favoritesFolder.exists()`
- 条件付き依存: `if (this._migrationType == MSMigrationUtils.MIGRATION_TYPE_IE)` → `favoritesFolder.isReadable()`
- 条件付き依存: `if (this._migrationType == MSMigrationUtils.MIGRATION_TYPE_EDGE)` → `getEdgeLocalDataFolder()`
- 条件付き依存: `if (edgeDir)` → `edgeDir.appendRelativePath()`
- 条件付き依存: `if (edgeDir)` → `edgeDir.exists()`
- 条件付き依存: `if (edgeDir)` → `edgeDir.isReadable()`
- 条件付き依存: `if (edgeDir)` → `edgeDir.isDirectory()`
- 参照: `Ci.nsIFile`, `MSMigrationUtils.MIGRATION_TYPE_EDGE`, `MSMigrationUtils.MIGRATION_TYPE_IE`, `this.__favoritesFolder`, `this._migrationType`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## _toolbarFolderName()
- 位置: L342-359
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._migrationType == MSMigrationUtils.MIGRATION_TYPE_IE)` → `lazy.WindowsRegistry.readRegKey()`
- 参照: `Ci.nsIWindowsRegKey.ROOT_KEY_CURRENT_USER`, `MSMigrationUtils.MIGRATION_TYPE_IE`, `this.__toolbarFolderName`, `this._migrationType`
- XPCOM: [`nsIWindowsRegKey`](../../../xpcom/ds/nsIWindowsRegKey.idl.md)

## B_migrate()
- 位置: L361-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `console.error()`, `this._migrateFolder()`
- 参照: `lazy.PlacesUtils.bookmarks.menuGuid`, `this._favoritesFolder`

## _migrateFolder()
- 位置: async L375-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.insertManyBookmarksWrapper()`, `MigrationUtils.insertManyFavicons()`, `MigrationUtils.insertManyFavicons(favicons).catch()`, `this._getBookmarksInFolder()`
- 参照: `bookmarks.length`, `console.error`

## _getBookmarksInFolder()
- 位置: async L402-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `entries.hasMoreElements()`, `entry.isDirectory()`
- 条件付き依存: `if (entry.path == entry.target && entry.isDirectory())` → `entry.parent.equals()`
- 条件付き依存: `if (entry.path == entry.target && entry.isDirectory())` → `entry.isReadable()`
- 条件付き依存: `if (isBookmarksFolder && entry.isReadable())` → `this._migrateFolder()`
- 条件付き依存: `if (!(isBookmarksFolder && entry.isReadable()))` → `entry.isReadable()`
- 条件付き依存: `if (entry.isReadable())` → `this._getBookmarksInFolder()`
- 条件付き依存: `if (entry.isReadable())` → `favicons.concat()`
- 条件付き依存: `if (entry.isReadable())` → `rv.push()`
- 条件付き依存: `if (!(entry.path == entry.target && entry.isDirectory()))` → `entry.leafName.match()`
- 条件付き依存: `if (matches)` → `Cc[ "@mozilla.org/network/protocol;1?name=file" ].getService()`
- 条件付き依存: `if (matches)` → `fileHandler.readURLFile()`
- 条件付き依存: `if (matches)` → `IOUtils.read()`
- 条件付き依存: `if (matches)` → `favicons.push()`
- 条件付き依存: `if (matches)` → `rv.push()`
- 参照: `Ci.nsIFileProtocolHandler`, `aSourceFolder.directoryEntries`, `entries.nextFile`, `entry.leafName`, `entry.path`, `entry.target`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `this._favoritesFolder`, `this._toolbarFolderName`, `this.importedAppLabel`
- XPCOM: [`nsIFileProtocolHandler`](../../../netwerk/protocol/file/nsIFileProtocolHandler.idl.md) / `@mozilla.org/network/protocol;1?name=file`

## getTypedURLs()
- 位置: L468-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/windows-registry-key;1" ].createInstance()`, `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `Date.now()`, `cTypes.finalize()`, `console.error()`, `typedURLKey.hasValue()`, `typedURLKey.open()`, `typedURLKey.readStringValue()`, `typedURLTimeKey.hasValue()`, `typedURLTimeKey.open()`, `typedURLs.set()`
- 条件付き依存: `if (typedURLTimeKey && typedURLTimeKey.hasValue(entryName))` → `typedURLTimeKey.readBinaryValue()`
- 条件付き依存: `if (typedURLTimeKey && typedURLTimeKey.hasValue(entryName))` → `console.error()`
- 条件付き依存: `if (urlTime.length == 8)` → `urlTime.charCodeAt(i).toString()`
- 条件付き依存: `if (urlTime.length == 8)` → `urlTime.charCodeAt()`
- 条件付き依存: `if (urlTime.length == 8)` → `urlTimeHex.unshift()`
- 条件付き依存: `if (urlTime.length == 8)` → `parseInt()`
- 条件付き依存: `if (urlTime.length == 8)` → `urlTimeHex.slice(0, 4).join()`
- 条件付き依存: `if (urlTime.length == 8)` → `urlTimeHex.slice()`
- 条件付き依存: `if (urlTime.length == 8)` → `urlTimeHex.slice(4, 8).join()`
- 条件付き依存: `if (urlTime.length == 8)` → `cTypes.fileTimeToSecondsSinceEpoch()`
- 条件付き依存: `if (urlTime.length == 8)` → `Date.now()`
- 条件付き依存: `if (typedURLKey)` → `typedURLKey.close()`
- 条件付き依存: `if (typedURLTimeKey)` → `typedURLTimeKey.close()`
- 参照: `Ci.nsIWindowsRegKey`, `Ci.nsIWindowsRegKey.ACCESS_READ`, `Ci.nsIWindowsRegKey.ROOT_KEY_CURRENT_USER`, `c.length`, `urlTime.length`
- XPCOM: [`nsIWindowsRegKey`](../../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`

## WindowsVaultFormPasswords()
- 位置: L561-561
- 役割: (未記入)
- 触るとき: (未記入)

## exists()
- 位置: L566-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.migrate()`

## migrate()
- 位置: async L583-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `URL.parse()`, `["http:", "https:", "ftp:"].includes()`, `_isIEOrEdgePassword()`, `aCallback()`, `console.error()`, `credential.address()`, `credential.contents.pAuthenticatorElement.contents.itemValue.readString()`, `ctypesKernelHelpers.fileTimeToSecondsSinceEpoch()`, `ctypesKernelHelpers.finalize()`, `ctypesVaultHelpers._functions.VaultEnumerateItems()`, `ctypesVaultHelpers._functions.VaultFree()`, `ctypesVaultHelpers._functions.VaultGetItem()`, `ctypesVaultHelpers._functions.VaultOpenVault()`, `ctypesVaultHelpers.finalize()`, `item.address()`, `item.contents.pIdentityElement.contents.itemValue.readString()`, `item.contents.pResourceElement.contents.itemValue.readString()`, `item.contents.schemaId.address()`, `item.increment()`, `itemCount.address()`, `logins.push()`, `vault.address()`, `vaultGuid.address()`
- 条件付き依存: `if (logins.length)` → `MigrationUtils.insertLoginsWrapper()`
- 条件付き依存: `if (successfulVaultOpen)` → `ctypesVaultHelpers._functions.VaultCloseVault()`
- 条件付き依存: `if (error == FREE_CLOSE_FAILED)` → `console.error()`
- 参照: `ctypesVaultHelpers._structs.GUID`, `ctypesVaultHelpers._structs.VAULT_ELEMENT.ptr`, `item.contents.highLastModified`, `item.contents.lowLastModified`, `item.contents.pIdentityElement`, `item.contents.pResourceElement`, `item.contents.schemaId.id`, `itemCount.value`, `logins.length`, `realURL.URI.prePath`, `realURL.protocol`, `wintypes.DWORD`, `wintypes.VOIDP`

## _isIEOrEdgePassword()
- 位置: L585-592
- 役割: (未記入)
- 触るとき: (未記入)

## getBookmarksMigrator()
- 位置: L738-740
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.MIGRATION_TYPE_IE`

## getWindowsVaultFormPasswordsMigrator()
- 位置: L741-743
- 役割: (未記入)
- 触るとき: (未記入)
