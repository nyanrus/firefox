# browser/components/migration/ChromeMigrationUtils.sys.mjs

source: browser/components/migration/ChromeMigrationUtils.sys.mjs
source-hash: 8e9e34c92c85d655216ccf8cb8dfdf9599329e69
lines: 542

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## supportsLoginsForPlatform()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["macosx", "win"].includes()`
- 参照: `AppConstants.platform`

## getExtensionList()
- 位置: async L46-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.stat()`, `console.error()`, `this.getExtensionPath()`
- 条件付き依存: `if (profileId === undefined)` → `this.getLastUsedProfileId()`
- 条件付き依存: `if (info.type === "directory")` → `PathUtils.filename()`
- 条件付き依存: `if (info.type === "directory")` → `this.getExtensionInformation()`
- 条件付き依存: `if (extensionInformation)` → `extensionList.push()`
- 参照: `info.type`

## getExtensionInformation()
- 位置: async L79-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`, `PathUtils.join()`, `console.error()`, `this._getSortedByVersionSubDirectoryNames()`, `this.getExtensionPath()`
- 条件付き依存: `if (profileId === undefined)` → `this.getLastUsedProfileId()`
- 条件付き依存: `if (!manifest.app)` → `this._getLocaleString()`
- 参照: `manifest.app`, `manifest.default_locale`, `manifest.description`, `manifest.name`

## _getLocaleString()
- 位置: async L141-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `key.endsWith()`, `key.startsWith()`, `key.substring()`
- 条件付き依存: `if (typeof key !== "string")` → `console.debug()`
- 条件付き依存: `if (!( this._extensionLocaleStrings[profileId] && this._extensionLocaleStrings[profileId][extensionId] ))` → `this.getExtensionPath()`
- 条件付き依存: `if (!( this._extensionLocaleStrings[profileId] && this._extensionLocaleStrings[profileId][extensionId] ))` → `PathUtils.join()`
- 条件付き依存: `if (!( this._extensionLocaleStrings[profileId] && this._extensionLocaleStrings[profileId][extensionId] ))` → `this._getSortedByVersionSubDirectoryNames()`
- 条件付き依存: `if (!( this._extensionLocaleStrings[profileId] && this._extensionLocaleStrings[profileId][extensionId] ))` → `IOUtils.readJSON()`
- 参照: `key.length`, `localeFile[key].message`, `this._extensionLocaleStrings`

## isExtensionInstalled()
- 位置: async L203-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `this.getExtensionPath()`
- 条件付き依存: `if (profileId === undefined)` → `this.getLastUsedProfileId()`

## getLastUsedProfileId()
- 位置: async L219-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getLocalState()`
- 参照: `localState.profile.last_used`

## getLocalState()
- 位置: async L235-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readUTF8()`, `JSON.parse()`, `PathUtils.join()`
- 条件付き依存: `if (!dataPath)` → `this.getDataPath()`
- 条件付き依存: `if (ex.name != "NotFoundError")` → `console.error()`
- 参照: `ex.name`

## getExtensionPath()
- 位置: async L259-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `this.getDataPath()`

## getDataPath()
- 位置: async L270-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `console.error()`, `subfolders.slice()`
- 条件付き依存: `if (rootDir == SNAP_REAL_HOME)` → `Services.env.get()`
- 条件付き依存: `if (!(rootDir == SNAP_REAL_HOME))` → `Services.dirsvc.get()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `Services.dirsvc.get(rootDir, Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc` / `Services.env`

## _getSortedByVersionSubDirectoryNames()
- 位置: async L368-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getChildren()`, `IOUtils.stat()`, `Services.vc.compare()`, `console.error()`, `entries.sort()`
- 条件付き依存: `if (info.type === "directory")` → `PathUtils.filename()`
- 条件付き依存: `if (info.type === "directory")` → `entries.push()`
- 参照: `info.type`, `this._extensionVersionDirectoryNames`
- XPCOM: `Services.vc`

## chromeTimeToDate()
- 位置: L407-415
- 役割: (未記入)
- 触るとき: (未記入)

## dateToChromeTime()
- 位置: L424-426
- 役割: (未記入)
- 触るとき: (未記入)

## mergeBookmarkChildren()
- 位置: L439-468
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item.type == "folder")` → `foldersByName.get()`
- 条件付き依存: `if (existing)` → `this.mergeBookmarkChildren()`
- 条件付き依存: `if (item.type == "folder")` → `this.mergeBookmarkChildren()`
- 条件付き依存: `if (item.type == "folder")` → `foldersByName.set()`
- 条件付き依存: `if (item.type == "folder")` → `merged.push()`
- 条件付き依存: `if (!(item.type == "folder"))` → `merged.push()`
- 参照: `existing.children`, `item.children`, `item.name`, `item.type`

## getImportableLogins()
- 位置: async L474-540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._importableLoginsCache.get()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `lazy.MigrationUtils.getMigrator()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `migrator._getChromeUserDataPathIfExists()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `migrator.getSourceProfiles()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `PathUtils.join()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `IOUtils.exists()`
- 条件付き依存: `if (!(await IOUtils.exists(path)))` → `console.error()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `lazy.MigrationUtils.getRowsFromDBWithoutLocks()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `row.getString()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `lazy.LoginHelper.getLoginOrigin()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `this._importableLoginsCache.get()`
- 条件付き依存: `if (!entries.length)` → `this._importableLoginsCache.set()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `entries.includes()`
- 条件付き依存: `if (!entries.includes(browserId))` → `entries.push()`
- 条件付き依存: `if (!this._importableLoginsCache)` → `console.error()`
- 参照: `entries.length`, `profile.id`, `this.CONTEXTUAL_LOGIN_IMPORT_BROWSERS`, `this._importableLoginsCache`, `this.supportsLoginsForPlatform`
