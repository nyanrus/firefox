# browser/components/migration/MigratorBase.sys.mjs

source: browser/components/migration/MigratorBase.sys.mjs
source-hash: d4e3733c95180f9c78fb7b7d993df3087caf8cbf
lines: 531

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MigratorBase.key()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.displayNameL10nID()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.brandImage()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.getSourceProfiles()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.getResources()
- 位置: L157-159
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.getLastUsedDate()
- 位置: L172-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## MigratorBase.startupOnlyMigrator()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.enabled()
- 位置: L203-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.constructor.key`
- XPCOM: `Services.prefs`

## MigratorBase.hasPermissions()
- 位置: async L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## MigratorBase.getPermissions()
- 位置: async L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## MigratorBase.canGetPermissions()
- 位置: async L244-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`

## MigratorBase.showsManualPasswordImport()
- 位置: L254-256
- 役割: (未記入)
- 触るとき: (未記入)

## MigratorBase.getMigrateData()
- 位置: async L268-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resources.map()`, `this.#getMaybeCachedResources()`, `types.reduce()`
- 参照: `r.type`

## MigratorBase.migrate()
- 位置: async L297-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `doMigrate()`, `this.#getMaybeCachedResources()`
- 条件付き依存: `if (aItems != lazy.MigrationUtils.resourceTypes.ALL)` → `resources.filter()`
- 条件付き依存: `if ( lazy.MigrationUtils.isStartupMigration && !this.startupOnlyMigrator && Services.policies.isAllowed("defaultBookmarks") )` → `lazy.MigrationUtils.profileStartup.doStartup()`
- 条件付き依存: `if ( lazy.MigrationUtils.isStartupMigration && !this.startupOnlyMigrator && Services.policies.isAllowed("defaultBookmarks") )` → `await()`
- 条件付き依存: `if ( lazy.MigrationUtils.isStartupMigration && !this.startupOnlyMigrator && Services.policies.isAllowed("defaultBookmarks") )` → `lazy.BrowserUtils.callModulesFromCategory()`
- 条件付き依存: `if ( lazy.MigrationUtils.isStartupMigration && !this.startupOnlyMigrator && Services.policies.isAllowed("defaultBookmarks") )` → `lazy.BookmarkHTMLUtils.importFromURL()`
- 条件付き依存: `if ( lazy.MigrationUtils.isStartupMigration && !this.startupOnlyMigrator && Services.policies.isAllowed("defaultBookmarks") )` → `lazy.BrowserUtils.promiseObserved()`
- 条件付き依存: `if ( lazy.MigrationUtils.isStartupMigration && !this.startupOnlyMigrator && Services.policies.isAllowed("defaultBookmarks") )` → `doMigrate()`
- 参照: `console.error`, `lazy.MigrationUtils.isStartupMigration`, `lazy.MigrationUtils.resourceTypes.ALL`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE_ON_STARTUP`, `r.type`, `resources.length`, `this.constructor.key`, `this.startupOnlyMigrator`
- XPCOM: `Services.policies`

## unblockMainThread()
- 位置: L308-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`
- XPCOM: `Services.tm`

## collectQuantityTelemetry()
- 位置: L316-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserMigration[metricName][browserKey].accumulateSingleSample()`, `Object.keys()`, `console.error()`
- 参照: `Glean.browserMigration`, `lazy.MigrationUtils._importQuantities`

## collectMigrationTelemetry()
- 位置: L331-360
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (prefKey)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.FirefoxProfileMigrator.key`, `lazy.MigrationUtils.resourceTypes.BOOKMARKS`, `lazy.MigrationUtils.resourceTypes.HISTORY`, `lazy.MigrationUtils.resourceTypes.PASSWORDS`, `this.constructor.key`
- XPCOM: `Services.prefs`

## doMigrate()
- 位置: async L363-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Promise.withResolvers()`, `console.error()`, `notify()`, `res.migrate()`, `resourceDone()`, `resources.forEach()`, `resourcesGroupedByItems.get()`, `resourcesGroupedByItems.get(resource.type).add()`, `resourcesGroupedByItems.has()`, `unblockMainThread()`
- 条件付き依存: `if (!resourcesGroupedByItems.has(resource.type))` → `resourcesGroupedByItems.set()`
- 参照: `completeDeferred.promise`, `lazy.MigrationUtils._importQuantities`, `resource.type`, `resourcesGroupedByItems.size`

## notify()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## resourceDone()
- 位置: L392-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `completeDeferred.resolve()`, `itemResources.delete()`
- 条件付き依存: `if (itemResources.size == 0)` → `notify()`
- 条件付き依存: `if (itemResources.size == 0)` → `collectMigrationTelemetry()`
- 条件付き依存: `if (itemResources.size == 0)` → `aProgressCallback()`
- 条件付き依存: `if (itemResources.size == 0)` → `resourcesGroupedByItems.delete()`
- 条件付き依存: `if (resourcesGroupedByItems.size == 0)` → `collectQuantityTelemetry()`
- 条件付き依存: `if (resourcesGroupedByItems.size == 0)` → `notify()`
- 参照: `itemResources.size`, `resourcesGroupedByItems.size`

## MigratorBase.isSourceAvailable()
- 位置: async L483-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.getSourceProfiles()`
- 条件付き依存: `if (!profiles)` → `this.#getMaybeCachedResources()`
- 参照: `lazy.MigrationUtils.isStartupMigration`, `profiles.length`, `resources.length`, `this.startupOnlyMigrator`

## MigratorBase.#getMaybeCachedResources()
- 位置: async L518-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getResources()`
- 参照: `aProfile.id`, `this._resourcesByProfile`
