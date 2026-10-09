# browser/components/urlbar/UrlbarProviderOpenTabs.sys.mjs

source: browser/components/urlbar/UrlbarProviderOpenTabs.sys.mjs
source-hash: ec57e44f3aecf51662164c588d0ecc44a8bfaf87
lines: 390

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `addToMemoryTable()`, `addToMemoryTable(url, userContextId, groupId, count).catch()`, `lazy.PlacesUtils.largeCacheDBConnDeferred.promise.then()`, `lazy.UrlbarShared.getLogger()`

## UrlbarProviderOpenTabs.constructor()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderOpenTabs.type()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderOpenTabs.isActive()
- 位置: async L56-60
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderOpenTabs.getOpenTabUrlsForUserContextId()
- 位置: L76-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Number()`, `gOpenTabUrls.get()`, `groupEntries.forEach()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `parseInt()`, `result.add()`, `urls.keys()`

## UrlbarProviderOpenTabs.getOpenTabUrls()
- 位置: L111-140
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isInPrivateWindow)` → `UrlbarProviderOpenTabs.getOpenTabUrlsForUserContextId()`
- 条件付き依存: `if (isInPrivateWindow)` → `uniqueUrls.set()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `gOpenTabUrls.forEach()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `groups.forEach()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `urls.keys()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `uniqueUrls.get()`
- 条件付き依存: `if (!userContextAndGroupIds)` → `uniqueUrls.set()`
- 条件付き依存: `if (!(isInPrivateWindow))` → `userContextAndGroupIds.add()`
- 参照: `lazy.UrlbarShared.PRIVATE_USER_CONTEXT_ID`

## UrlbarProviderOpenTabs.getDatabaseRegisteredOpenTabsForTests()
- 位置: async L148-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.execute()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `r.getResultByName()`, `rows.map()`

## UrlbarProviderOpenTabs.registerOpenTab()
- 位置: async L190-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `Number.isInteger()`, `addToMemoryTable()`, `addToMemoryTable(url, userContextId, groupId).catch()`, `contextEntries.get()`, `gOpenTabUrls.get()`, `groupEntries.get()`, `groupEntries.set()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `lazy.logger.info()`, `parseInt()`
- 条件付き依存: `if (!Number.isInteger(userContextId))` → `lazy.logger.error()`
- 条件付き依存: `if (!contextEntries)` → `gOpenTabUrls.set()`
- 条件付き依存: `if (!groupEntries)` → `contextEntries.set()`
- 参照: `console.error`

## UrlbarProviderOpenTabs.unregisterOpenTab()
- 位置: async L241-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `gOpenTabUrls.get()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `lazy.logger.info()`, `parseInt()`
- 条件付き依存: `if (contextEntries)` → `contextEntries.get()`
- 条件付き依存: `if (groupEntries)` → `groupEntries.get()`
- 条件付き依存: `if (oldCount == 0)` → `console.error()`
- 条件付き依存: `if (oldCount == 1)` → `groupEntries.delete()`
- 条件付き依存: `if (!(oldCount == 1))` → `groupEntries.set()`
- 条件付き依存: `if (groupEntries)` → `removeFromMemoryTable(url, userContextId, groupId).catch()`
- 条件付き依存: `if (groupEntries)` → `removeFromMemoryTable()`
- 参照: `console.error`

## UrlbarProviderOpenTabs.startQuery()
- 位置: async L295-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.getUserContextData()`, `addCallback()`, `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `row.getResultByName()`
- 条件付き依存: `if (instance != this.queryInstance)` → `cancel()`
- 参照: `UrlbarProviderOpenTabs.promiseDBPopulated`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `this.queryInstance`

## addToMemoryTable()
- 位置: async L343-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.ProvidersManager.runInCriticalSection()`
- 参照: `UrlbarProviderOpenTabs.memoryTableInitialized`

## removeFromMemoryTable()
- 位置: async L372-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.ProvidersManager.runInCriticalSection()`
- 参照: `UrlbarProviderOpenTabs.memoryTableInitialized`
