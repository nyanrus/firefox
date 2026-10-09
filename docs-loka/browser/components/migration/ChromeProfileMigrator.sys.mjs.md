# browser/components/migration/ChromeProfileMigrator.sys.mjs

source: browser/components/migration/ChromeProfileMigrator.sys.mjs
source-hash: e88b69dc79989828d51f693923f1c044c889a5d3
lines: 1299

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## convertBookmarks()
- 位置: L39-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `errorAccumulator()`
- 条件付き依存: `if (item.type == "url")` → `item.url.trim().startsWith()`
- 条件付き依存: `if (item.type == "url")` → `item.url.trim()`
- 条件付き依存: `if (item.type == "url")` → `itemsToInsert.push()`
- 条件付き依存: `if (item.type == "url")` → `bookmarkURLAccumulator.add()`
- 条件付き依存: `if (item.type == "folder")` → `convertBookmarks()`
- 条件付き依存: `if (item.type == "folder")` → `itemsToInsert.push()`
- 参照: `folderItem.children`, `item.children`, `item.name`, `item.type`, `item.url`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`

## ChromeProfileMigrator.key()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeProfileMigrator.displayNameL10nID()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeProfileMigrator.brandImage()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeProfileMigrator._chromeUserDataPathSuffix()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeProfileMigrator.hasPermissions()
- 位置: async L114-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.read()`, `PathUtils.join()`, `console.error()`, `this._getChromeUserDataPathIfExists()`

## ChromeProfileMigrator.getPermissions()
- 位置: async L132-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `fp.init()`, `fp.open()`, `this._getChromeUserDataPathIfExists()`, `this.hasPermissions()`
- 条件付き依存: `if (file && file.path != originalDataPath)` → `this.#dataPathRemappings.set()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeGetFolder`, `Ci.nsIFilePicker.returnCancel`, `file.path`, `fp.file`, `fp.filterIndex`, `win?.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## ChromeProfileMigrator.canGetPermissions()
- 位置: async L163-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.canGetPermissionsOnPlatform()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (await MigrationUtils.canGetPermissionsOnPlatform())` → `this._getChromeUserDataPathIfExists()`
- 条件付き依存: `if (dataPath)` → `PathUtils.join()`
- 条件付き依存: `if (dataPath)` → `IOUtils.exists()`
- XPCOM: `Services.prefs`

## ChromeProfileMigrator.showsManualPasswordImport()
- 位置: L190-192
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `this.constructor.key`

## ChromeProfileMigrator._getChromeUserDataPathIfExists()
- 位置: async L208-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `lazy.ChromeMigrationUtils.getDataPath()`
- 条件付き依存: `if (this._chromeUserDataPath)` → `this.#dataPathRemappings.get()`
- 参照: `this._chromeUserDataPath`, `this._chromeUserDataPathSuffix`

## ChromeProfileMigrator.getResources()
- 位置: async L233-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getChromeUserDataPathIfExists()`, `this.hasPermissions()`
- 条件付き依存: `if (aProfile)` → `PathUtils.join()`
- 条件付き依存: `if (chromeUserDataPath)` → `IOUtils.exists()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `GetBookmarksResource()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `GetHistoryResource()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `GetFormdataResource()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `GetExtensionsResource()`
- 条件付き依存: `if (lazy.ChromeMigrationUtils.supportsLoginsForPlatform)` → `possibleResourcePromises.push()`
- 条件付き依存: `if (lazy.ChromeMigrationUtils.supportsLoginsForPlatform)` → `this._GetPasswordsResource()`
- 条件付き依存: `if (lazy.ChromeMigrationUtils.supportsLoginsForPlatform)` → `this._GetPaymentMethodsResource()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `Promise.allSettled()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `possibleResources .filter(promise => { return promise.status == "fulfilled" && promise.value !== null; }) .map()`
- 条件付き依存: `if (await IOUtils.exists(profileFolder))` → `possibleResources .filter()`
- 参照: `aProfile.id`, `lazy.ChromeMigrationUtils.supportsLoginsForPlatform`, `promise.status`, `promise.value`, `this.constructor.key`

## ChromeProfileMigrator.getLastUsedDate()
- 位置: async L275-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.stat()`, `IOUtils.stat(path).catch()`, `Math.max()`, `PathUtils.join()`, `Promise.all()`, `[ "AccountBookmarks", "Bookmarks", "Cookies", "History", ].map()`, `datesOuter.push()`, `sourceProfiles.map()`, `this._getChromeUserDataPathIfExists()`, `this.getSourceProfiles()`
- 参照: `info.lastModified`, `profile.id`

## ChromeProfileMigrator.getSourceProfiles()
- 位置: async L304-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `PathUtils.join()`, `Promise.all()`, `lazy.ChromeMigrationUtils.getLocalState()`, `profileResources .filter()`, `profileResources .filter(({ resources }) => { return resources && !!resources.length; }, this) .map()`, `profiles.map()`, `profiles.push()`, `this._getChromeUserDataPathIfExists()`, `this.getResources()`
- 条件付き依存: `if (localState || e.name != "NotFoundError")` → `console.error()`
- 参照: `e.name`, `info_cache[profileFolderName].name`, `localState.profile.info_cache`, `resources.length`, `this.__sourceProfiles`, `this._chromeUserDataPathSuffix`

## ChromeProfileMigrator._GetPasswordsResource()
- 位置: async L369-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `PathUtils.join()`, `countRows[0].getResultByName()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.createUniqueFile()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.copy()`
- 参照: `MigrationUtils.IS_LINUX_SNAP_PACKAGE`, `MigrationUtils.resourceTypes.PASSWORDS`, `PathUtils.tempDir`

## ChromeProfileMigrator.migrate()
- 位置: async L407-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `aCallback()`, `console.error()`, `kValidSchemes.has()`, `lazy.ChromeMigrationUtils.chromeTimeToDate()`, `lazy.ChromeMigrationUtils.chromeTimeToDate( row.getResultByName("date_created") + 0, fallbackCreationDate ).getTime()`, `lazy.NetUtil.newURI()`, `loginCrypto.decryptData()`, `logins.push()`, `row .getResultByName()`, `row .getResultByName("signon_realm") .substring()`, `row.getResultByName()`
- 条件付き依存: `if (!rows.length)` → `aCallback()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `aCallback()`
- 条件付き依存: `if (logins.length)` → `MigrationUtils.insertLoginsWrapper()`
- 条件付き依存: `if (crypto.finalize)` → `crypto.finalize()`
- 参照: `AUTH_TYPE.SCHEME_BASIC`, `AUTH_TYPE.SCHEME_DIGEST`, `AUTH_TYPE.SCHEME_HTML`, `AppConstants.platform`, `action_uri.prePath`, `action_uri.scheme`, `crypto.finalize`, `loginInfo.formActionOrigin`, `loginInfo.httpRealm`, `loginInfo.origin.length`, `logins.length`, `origin_url.prePath`, `origin_url.scheme`, `rows.length`

## ChromeProfileMigrator._GetPaymentMethodsResource()
- 位置: async L544-662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `IOUtils.remove()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `PathUtils.join()`, `Services.prefs.getBoolPref()`, `console.error()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.createUniqueFile()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.copy()`
- 参照: `AppConstants.platform`, `MigrationUtils.IS_LINUX_SNAP_PACKAGE`, `MigrationUtils.resourceTypes.PAYMENT_METHODS`, `PathUtils.tempDir`, `rows?.length`
- XPCOM: `Services.prefs`

## ChromeProfileMigrator.migrate()
- 位置: async L605-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.insertCreditCardsWrapper()`, `aCallback()`, `cards.push()`, `console.error()`, `loginCrypto.decryptData()`, `parseInt()`, `row.getResultByName()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `aCallback()`
- 参照: `AppConstants.platform`

## GetBookmarksResource()
- 位置: async L665-836
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`, `PathUtils.join()`
- 条件付き依存: `if (aBrowserKey === "chromium-360se")` → `lazy.ChromeMigrationUtils.getLocalState()`
- 条件付き依存: `if (aBrowserKey === "chromium-360se")` → `console.error()`
- 条件付き依存: `if (aBrowserKey === "chromium-360se")` → `lazy.Qihoo360seMigrationUtils.getAlternativeBookmarks()`
- 条件付き依存: `if ( roots?.other?.children?.length || roots?.bookmark_bar?.children?.length || roots?.synced?.children?.length )` → `bookmarkJSONs.push()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.createUniqueFile()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.copy()`
- 参照: `MigrationUtils.IS_LINUX_SNAP_PACKAGE`, `MigrationUtils.resourceTypes.BOOKMARKS`, `PathUtils.tempDir`, `alternativeBookmarks.path`, `alternativeBookmarks.resource`, `bookmarkJSON.roots`, `bookmarkJSONs.length`, `roots?.bookmark_bar?.children?.length`, `roots?.other?.children?.length`, `roots?.synced?.children?.length`

## migrate()
- 位置: L729-834
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.getRowsFromDBWithoutLocks()`, `MigrationUtils.insertManyBookmarksWrapper()`, `MigrationUtils.insertManyFavicons()`, `MigrationUtils.insertManyFavicons(favicons).catch()`, `aCallback()`, `bookmarkJSONs.map()`, `console.error()`, `convertBookmarks()`, `faviconMap.get()`, `faviconMap.set()`, `faviconRow.getResultByName()`, `lazy.ChromeMigrationUtils.mergeBookmarkChildren()`, `lazy.NetUtil.newURI()`
- 条件付き依存: `if (tempFilePath)` → `IOUtils.remove()`
- 条件付き依存: `if (favicon)` → `favicons.push()`
- 参照: `bookmark.url`, `console.error`, `json.roots.bookmark_bar?.children`, `json.roots.other?.children`, `json.roots.synced?.children`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `lazy.PlacesUtils.bookmarks.unfiledGuid`, `mergedRoots[rootName].length`, `uri.spec`

## errorGatherer()
- 位置: L732-734
- 役割: (未記入)
- 触るとき: (未記入)

## GetHistoryResource()
- 位置: async L838-936
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `PathUtils.join()`, `countRows[0].getResultByName()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.createUniqueFile()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.copy()`
- 参照: `MigrationUtils.IS_LINUX_SNAP_PACKAGE`, `MigrationUtils.resourceTypes.HISTORY`, `PathUtils.tempDir`

## migrate()
- 位置: L864-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `Services.prefs.getIntPref()`, `aCallback()`, `console.error()`, `lazy.ChromeMigrationUtils.chromeTimeToDate()`, `lazy.ChromeMigrationUtils.dateToChromeTime()`, `pageInfos.push()`, `row.getResultByName()`
- 条件付き依存: `if (tempFilePath)` → `IOUtils.remove()`
- 条件付き依存: `if (pageInfos.length)` → `MigrationUtils.insertVisitsWrapper()`
- 参照: `MigrationUtils.HISTORY_MAX_AGE_IN_MILLISECONDS`, `lazy.PlacesUtils.history.TRANSITIONS.LINK`, `lazy.PlacesUtils.history.TRANSITIONS.TYPED`, `pageInfos.length`
- XPCOM: `Services.prefs`

## GetFormdataResource()
- 位置: async L938-1014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `MigrationUtils.getRowsFromDBWithoutLocks()`, `PathUtils.join()`, `countRows[0].getResultByName()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.createUniqueFile()`
- 条件付き依存: `if (MigrationUtils.IS_LINUX_SNAP_PACKAGE)` → `IOUtils.copy()`
- 参照: `MigrationUtils.IS_LINUX_SNAP_PACKAGE`, `MigrationUtils.resourceTypes.FORMDATA`, `PathUtils.tempDir`

## migrate()
- 位置: async L966-1012
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.getRowsFromDBWithoutLocks()`, `aCallback()`, `console.error()`, `lazy.FormHistory.update()`, `row.getResultByName()`
- 条件付き依存: `if (tempFilePath)` → `IOUtils.remove()`
- 条件付き依存: `if (fieldname && value)` → `addOps.push()`
- 条件付き依存: `if (fieldname && value)` → `row.getResultByName()`

## GetExtensionsResource()
- 位置: async L1016-1051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.ChromeMigrationUtils.getExtensionList()`
- 参照: `MigrationUtils.resourceTypes.EXTENSIONS`, `extensions.length`
- XPCOM: `Services.prefs`

## migrate()
- 位置: async L1032-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationUtils.installExtensionsWrapper()`, `extensions.map()`
- 条件付き依存: `if ( progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO || progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS )` → `callback()`
- 条件付き依存: `if (!( progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO || progressValue == lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS ))` → `callback()`
- 参照: `extension.id`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`

## ChromiumProfileMigrator.key()
- 位置: L1057-1059
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumProfileMigrator.displayNameL10nID()
- 位置: L1061-1063
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumProfileMigrator.brandImage()
- 位置: L1065-1067
- 役割: (未記入)
- 触るとき: (未記入)

## CanaryProfileMigrator.key()
- 位置: L1079-1081
- 役割: (未記入)
- 触るとき: (未記入)

## CanaryProfileMigrator.displayNameL10nID()
- 位置: L1083-1085
- 役割: (未記入)
- 触るとき: (未記入)

## CanaryProfileMigrator.brandImage()
- 位置: L1087-1089
- 役割: (未記入)
- 触るとき: (未記入)

## CanaryProfileMigrator._chromeUserDataPathSuffix()
- 位置: L1091-1093
- 役割: (未記入)
- 触るとき: (未記入)

## CanaryProfileMigrator._keychainServiceName()
- 位置: L1095-1097
- 役割: (未記入)
- 触るとき: (未記入)

## CanaryProfileMigrator._keychainAccountName()
- 位置: L1099-1101
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeDevMigrator.key()
- 位置: L1108-1110
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeDevMigrator.displayNameL10nID()
- 位置: L1112-1114
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeBetaMigrator.key()
- 位置: L1125-1127
- 役割: (未記入)
- 触るとき: (未記入)

## ChromeBetaMigrator.displayNameL10nID()
- 位置: L1129-1131
- 役割: (未記入)
- 触るとき: (未記入)

## BraveProfileMigrator.key()
- 位置: L1142-1144
- 役割: (未記入)
- 触るとき: (未記入)

## BraveProfileMigrator.displayNameL10nID()
- 位置: L1146-1148
- 役割: (未記入)
- 触るとき: (未記入)

## BraveProfileMigrator.brandImage()
- 位置: L1150-1152
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumEdgeMigrator.key()
- 位置: L1163-1165
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumEdgeMigrator.displayNameL10nID()
- 位置: L1167-1169
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumEdgeMigrator.brandImage()
- 位置: L1171-1173
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumEdgeBetaMigrator.key()
- 位置: L1184-1186
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumEdgeBetaMigrator.displayNameL10nID()
- 位置: L1188-1190
- 役割: (未記入)
- 触るとき: (未記入)

## ChromiumEdgeBetaMigrator.brandImage()
- 位置: L1192-1194
- 役割: (未記入)
- 触るとき: (未記入)

## Chromium360seMigrator.key()
- 位置: L1205-1207
- 役割: (未記入)
- 触るとき: (未記入)

## Chromium360seMigrator.displayNameL10nID()
- 位置: L1209-1211
- 役割: (未記入)
- 触るとき: (未記入)

## Chromium360seMigrator.brandImage()
- 位置: L1213-1215
- 役割: (未記入)
- 触るとき: (未記入)

## OperaProfileMigrator.key()
- 位置: L1226-1228
- 役割: (未記入)
- 触るとき: (未記入)

## OperaProfileMigrator.displayNameL10nID()
- 位置: L1230-1232
- 役割: (未記入)
- 触るとき: (未記入)

## OperaProfileMigrator.brandImage()
- 位置: L1234-1236
- 役割: (未記入)
- 触るとき: (未記入)

## OperaProfileMigrator.getSourceProfiles()
- 位置: async L1242-1251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `super.getSourceProfiles()`
- 参照: `detectedProfiles.length`

## OperaGXProfileMigrator.key()
- 位置: L1258-1260
- 役割: (未記入)
- 触るとき: (未記入)

## OperaGXProfileMigrator.displayNameL10nID()
- 位置: L1262-1264
- 役割: (未記入)
- 触るとき: (未記入)

## OperaGXProfileMigrator.brandImage()
- 位置: L1266-1268
- 役割: (未記入)
- 触るとき: (未記入)

## OperaGXProfileMigrator.getSourceProfiles()
- 位置: L1274-1276
- 役割: (未記入)
- 触るとき: (未記入)

## VivaldiProfileMigrator.key()
- 位置: L1283-1285
- 役割: (未記入)
- 触るとき: (未記入)

## VivaldiProfileMigrator.displayNameL10nID()
- 位置: L1287-1289
- 役割: (未記入)
- 触るとき: (未記入)

## VivaldiProfileMigrator.brandImage()
- 位置: L1291-1293
- 役割: (未記入)
- 触るとき: (未記入)
