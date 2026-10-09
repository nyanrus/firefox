# browser/components/migration/MigrationUtils.sys.mjs

source: browser/components/migration/MigrationUtils.sys.mjs
source-hash: 1289865805d2d6cbb7813da5fabf000284d7ac4c
lines: 1226

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `fp.isModeSupported()`

## getL10n()
- 位置: L39-44
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationUtils.constructor()
- 位置: L158-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/gio-service;1"].getService()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.registerWindowActor()`, `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `AppConstants.platform`, `Ci.nsIGIOService`, `gIOSvc.isRunningUnderSnap`
- XPCOM: [`nsIGIOService`](../../../xpcom/system/nsIGIOService.idl.md) / `@mozilla.org/gio-service;1` → `nsGIOService` (toolkit/system/gnome/components.conf)

## MigrationUtils.wrapMigrateFunction()
- 位置: L268-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `aFunction.apply()`, `console.error()`

## MigrationUtils.getLocalizedString()
- 位置: L294-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getL10n()`, `l10n.formatValue()`

## MigrationUtils.getRowsFromDBWithoutLocks()
- 位置: L319-375
- 役割: (未記入)
- 触るとき: (未記入)

## innerGetRows()
- 位置: async L333-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `db.execute()`, `lazy.Sqlite.openConnection()`, `lazy.setTimeout()`
- 条件付き依存: `if (previousExceptionMessage != ex.message)` → `console.error()`
- 条件付き依存: `if (didOpen)` → `db.close()`
- 参照: `ex.message`, `ex.name`

## MigrationUtils.#migrators()
- 位置: L377-398
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!gMigrators)` → `Object.entries()`
- 条件付き依存: `if (!gMigrators)` → `platforms.includes()`
- 条件付き依存: `if (platforms.includes(AppConstants.platform))` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (platforms.includes(AppConstants.platform))` → `gMigrators.has()`
- 条件付き依存: `if (gMigrators.has(migratorClass.key))` → `console.error()`
- 条件付き依存: `if (platforms.includes(AppConstants.platform))` → `gMigrators.set()`
- 参照: `AppConstants.platform`, `migratorClass.key`

## MigrationUtils.#fileMigrators()
- 位置: L400-418
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!gFileMigrators)` → `Object.entries()`
- 条件付き依存: `if (!gFileMigrators)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!gFileMigrators)` → `gFileMigrators.has()`
- 条件付き依存: `if (gFileMigrators.has(migratorClass.key))` → `console.error()`
- 条件付き依存: `if (!gFileMigrators)` → `gFileMigrators.set()`
- 参照: `migratorClass.key`

## MigrationUtils.forceExitSpinResolve()
- 位置: L420-422
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationUtils.spinResolve()
- 位置: L424-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.spinEventLoopUntil()`, `promise .catch()`, `promise .catch(e => { error = e; }) .then()`
- XPCOM: `Services.tm`

## MigrationUtils.getMigrator()
- 位置: async L466-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `migrator.canGetPermissions()`, `migrator.hasPermissions()`, `migrator.isSourceAvailable()`, `this.#migrators.get()`
- 条件付き依存: `if (!migrator)` → `console.error()`

## MigrationUtils.getFileMigrator()
- 位置: L492-499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fileMigrators.get()`
- 条件付き依存: `if (!migrator)` → `console.error()`

## MigrationUtils.migratorExists()
- 位置: L510-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#migrators.has()`

## MigrationUtils.getMigratorKeyForDefaultBrowser()
- 位置: L524-560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/uriloader/external-protocol-service;1"] .getService()`, `browserDesc.startsWith()`, `console.error()`
- 参照: `AppConstants.MOZ_APP_BASENAME`, `AppConstants.MOZ_APP_NAME`, `Ci.nsIExternalProtocolService`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1`

## MigrationUtils.isStartupMigration()
- 位置: L567-569
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationUtils.profileStartup()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationUtils.showMigrationWizard()
- 位置: L612-685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserMigration.entryPointCategorical[entrypoint].add()`, `Promise.resolve()`, `Services.prefs.getCharPref()`, `openStandaloneWindow()`
- 条件付き依存: `if (aOptions.isStartupMigration)` → `Services.env.get()`
- 条件付き依存: `if (Services.env.get("MOZ_UNINSTALLER_PROFILE_REFRESH"))` → `Services.env.set()`
- 条件付き依存: `if (Services.env.get("MOZ_UNINSTALLER_PROFILE_REFRESH"))` → `Glean.migration.uninstallerProfileRefresh.set()`
- 条件付き依存: `if (aOptions.isStartupMigration)` → `openStandaloneWindow()`
- 条件付き依存: `if (aOptions.isStartupMigration)` → `Promise.resolve()`
- 条件付き依存: `if (aboutWelcomeBehavior == "autoclose")` → `aOpener.openPreferences()`
- 条件付き依存: `if (aboutWelcomeBehavior == "standalone")` → `openStandaloneWindow()`
- 条件付き依存: `if (aboutWelcomeBehavior == "standalone")` → `Promise.resolve()`
- 条件付き依存: `if (aOpener?.openPreferences)` → `aOpener.openPreferences()`
- 参照: `Glean.browserMigration.entryPointCategorical`, `aOpener?.openPreferences`, `aOptions.entrypoint`, `aOptions.isStartupMigration`, `this.MIGRATION_ENTRYPOINTS.NEWTAB`, `this.MIGRATION_ENTRYPOINTS.UNKNOWN`
- XPCOM: `Services.env` / `Services.prefs`

## openStandaloneWindow()
- 位置: L639-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Services.ww.openWindow()`
- XPCOM: `Services.ww`

## MigrationUtils.startupMigration()
- 位置: L707-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.asyncStartupMigration()`, `this.spinResolve()`

## MigrationUtils.asyncStartupMigration()
- 位置: async L717-789
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FIREFOX_REFRESH_MIGRATOR_KEYS.has()`, `this.showMigrationWizard()`
- 条件付き依存: `if (aMigratorKey)` → `this.getMigrator()`
- 条件付き依存: `if (!migrator)` → `this.finishMigration()`
- 条件付き依存: `if (!(aMigratorKey))` → `this.getMigratorKeyForDefaultBrowser()`
- 条件付き依存: `if (defaultBrowserKey)` → `this.getMigrator()`
- 条件付き依存: `if (!migrator)` → `Promise.all()`
- 条件付き依存: `if (!migrator)` → `this.availableMigratorKeys.map()`
- 条件付き依存: `if (!migrator)` → `this.getMigrator()`
- 条件付き依存: `if (!migrator)` → `migrators.some()`
- 条件付き依存: `if (!migrators.some(m => m))` → `this.finishMigration()`
- 参照: `this.MIGRATION_ENTRYPOINTS.FIRSTRUN`, `this.MIGRATION_ENTRYPOINTS.FXREFRESH`

## MigrationUtils.getImportedCount()
- 位置: L803-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._importQuantities.hasOwnProperty()`
- 参照: `this._importQuantities`

## MigrationUtils.insertBookmarkWrapper()
- 位置: L812-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gUndoData.get()`, `gUndoData.get("bookmarks").push()`, `insertionPromise.then()`, `lazy.PlacesUtils.bookmarks.insert()`
- 参照: `this._importQuantities.bookmarks`

## MigrationUtils.insertManyBookmarksWrapper()
- 位置: L833-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `insertionPromise.then()`, `lazy.PlacesUtils.bookmarks.insertTree()`
- 条件付き依存: `if (gKeepUndoData)` → `gUndoData.get()`
- 条件付き依存: `if (gKeepUndoData)` → `bmData.push()`
- 条件付き依存: `if (parent == lazy.PlacesUtils.bookmarks.toolbarGuid)` → `lazy.PlacesUIUtils.maybeToggleBookmarkToolbarVisibility( true /* aForceVisible */ ).catch()`
- 条件付き依存: `if (parent == lazy.PlacesUtils.bookmarks.toolbarGuid)` → `lazy.PlacesUIUtils.maybeToggleBookmarkToolbarVisibility()`
- 参照: `console.error`, `insertedItems.length`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `this._importQuantities.bookmarks`

## MigrationUtils.insertVisitsWrapper()
- 位置: L858-875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.history.insertMany()`
- 条件付き依存: `if (gKeepUndoData)` → `this.#updateHistoryUndo()`
- 参照: `pageInfo.visits`, `pageInfos.length`, `this._importQuantities.history`, `visit.date`

## MigrationUtils.insertLoginsWrapper()
- 位置: async L877-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.maybeImportLogins()`
- 条件付き依存: `if (gKeepUndoData)` → `gUndoData.get("logins").push()`
- 条件付き依存: `if (gKeepUndoData)` → `gUndoData.get()`
- 参照: `logins.length`, `this._importQuantities.logins`

## MigrationUtils.notifyLoginsManuallyImported()
- 位置: L899-901
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._importQuantities.logins`

## MigrationUtils.insertManyFavicons()
- 位置: async L916-955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/image/loader;1"].createInstance()`, `Services.io.newURI()`, `console.warn()`, `lazy.PlacesUtils.favicons .setFaviconForPage()`, `lazy.PlacesUtils.favicons .setFaviconForPage( faviconDataItem.uri, fakeFaviconURI, Services.io.newURI(dataURL) ) .catch()`, `reader.addEventListener()`, `reader.readAsDataURL()`, `resolve()`, `sniffer.getMIMETypeFromContent()`
- 参照: `Ci.nsIContentSniffer`, `console.warn`, `faviconDataItem.faviconData`, `faviconDataItem.faviconData.length`, `faviconDataItem.uri`, `faviconDataItem.uri.spec`, `reader.result`
- XPCOM: [`nsIContentSniffer`](../../../netwerk/base/nsIContentSniffer.idl.md) / `@mozilla.org/image/loader;1` → `imgLoader` (image/build/components.conf) / `Services.io`

## MigrationUtils.insertCreditCardsWrapper()
- 位置: async L957-971
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `console.error()`, `formAutofillStorage.creditCards.add()`, `formAutofillStorage.initialize()`
- 参照: `cards.length`, `this._importQuantities.cards`

## MigrationUtils.installExtensionsWrapper()
- 位置: async L985-1017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.AMBrowserExtensionsImport.stageInstalls()`
- 参照: `extensionIDs.length`, `importedAddonIDs.length`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.INFO`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`, `lazy.MigrationWizardConstants.PROGRESS_VALUE.WARNING`, `result.importedAddonIDs`, `this._importQuantities.extensions`

## MigrationUtils.initializeUndoData()
- 位置: L1019-1026
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationUtils.#postProcessUndoData()
- 位置: async L1028-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `bookmarkFolderData.map()`, `bookmarkFolderData.push()`, `bookmarkFolders.map()`, `folderLMMap.get()`, `lazy.PlacesUtils.bookmarks.fetch()`, `lazy.PlacesUtils.bookmarks.fetch(guid).then()`, `state .get()`, `state .get("bookmarks") .filter()`
- 参照: `b.guid`, `b.lastModified`, `b.type`, `bookmark.guid`, `bookmark.lastModified`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`

## MigrationUtils.stopAndRetrieveUndoData()
- 位置: L1060-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#postProcessUndoData()`

## MigrationUtils.#updateHistoryUndo()
- 位置: L1067-1099
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `URL.canParse()`, `gUndoData.get()`, `gUndoData.set()`, `visitMap.has()`, `visitMap.values()`, `visits.map()`
- 条件付き依存: `if (visitCount > 1)` → `pageInfo.visits.map()`
- 条件付き依存: `if (visitCount > 1)` → `Math.min.apply()`
- 条件付き依存: `if (visitCount > 1)` → `Math.max.apply()`
- 条件付き依存: `if (!visitMap.has(url))` → `visitMap.set()`
- 条件付き依存: `if (!(!visitMap.has(url)))` → `visitMap.get()`
- 条件付き依存: `if (!(!visitMap.has(url)))` → `Math.min()`
- 条件付き依存: `if (!(!visitMap.has(url)))` → `Math.max()`
- 参照: `Ci.nsIURI`, `currentData.first`, `currentData.last`, `currentData.visitCount`, `pageInfo.url`, `pageInfo.url.spec`, `pageInfo.visits`, `pageInfo.visits.length`, `pageInfo.visits[0].date`, `v.date`, `v.url`
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md)

## MigrationUtils.finishMigration()
- 位置: L1104-1108
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationUtils.availableMigratorKeys()
- 位置: L1110-1112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#migrators.keys()`

## MigrationUtils.availableFileMigrators()
- 位置: L1114-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fileMigrators.values()`

## MigrationUtils.MIGRATION_ENTRYPOINTS()
- 位置: L1170-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#MIGRATION_ENTRYPOINTS_ENUM`

## MigrationUtils.getSourceIdForTelemetry()
- 位置: L1202-1204
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#SOURCE_NAME_TO_ID_MAPPING_ENUM`

## MigrationUtils.HISTORY_MAX_AGE_IN_MILLISECONDS()
- 位置: L1206-1208
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.HISTORY_MAX_AGE_IN_DAYS`

## MigrationUtils.canGetPermissionsOnPlatform()
- 位置: L1218-1220
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.gCanGetPermissionsOnPlatformPromise`
