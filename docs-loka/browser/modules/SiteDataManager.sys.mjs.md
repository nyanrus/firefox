# browser/modules/SiteDataManager.sys.mjs

source: browser/modules/SiteDataManager.sys.mjs
source-hash: dc2c7d456219ab5b9c3e9ab6c4c8eec1fc745ee8
lines: 665

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## updateSites()
- 位置: async L60-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this._getAllCookies()`, `this._getQuotaUsage()`, `this._sites.clear()`
- XPCOM: `Services.obs`

## getBaseDomainFromHost()
- 位置: L79-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`
- 参照: `Cr.NS_ERROR_HOST_IS_IP_ADDRESS`, `Cr.NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS`, `e.result`
- XPCOM: `Services.eTLD`

## _getOrInsertSite()
- 位置: L99-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sites.get()`
- 条件付き依存: `if (!site)` → `this._sites.set()`

## _testInsertSite()
- 位置: L123-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sites.set()`

## _getOrInsertContainersData()
- 位置: L146-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `site.containersData.get()`
- 条件付き依存: `if (!containerData)` → `site.containersData.set()`
- 参照: `site.containersData`

## getCacheSize()
- 位置: L171-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.cache2.asyncGetDiskConsumption()`, `reject()`
- 参照: `this._getCacheSizeObserver`, `this._getCacheSizePromise`
- XPCOM: `Services.cache2`

## onNetworkCacheDiskConsumption()
- 位置: L179-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 参照: `this._getCacheSizeObserver`, `this._getCacheSizePromise`

## _getQuotaUsage()
- 位置: L203-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.qms.getUsage()`, `this._cancelGetQuotaUsage()`
- 参照: `this._getQuotaUsagePromise`, `this._quotaUsageRequest`
- XPCOM: `Services.qms`

## onUsageResult()
- 位置: L206-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 条件付き依存: `if (request.resultCode == Cr.NS_OK)` → `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 条件付き依存: `if (request.resultCode == Cr.NS_OK)` → `principal.schemeIs()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `ChromeUtils.getBaseDomainFromPartitionKey()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `console.error()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `this._getOrInsertSite()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `Number.isInteger()`
- 条件付き依存: `if (Number.isInteger(principal.userContextId))` → `this._getOrInsertContainersData()`
- 条件付き依存: `if (Number.isInteger(principal.userContextId))` → `containerData.lastAccessed.getTime()`
- 条件付き依存: `if (containerData.lastAccessed.getTime() < itemTime)` → `containerData.lastAccessed.setTime()`
- 条件付き依存: `if (principal.schemeIs("http") || principal.schemeIs("https"))` → `site.principals.push()`
- 条件付き依存: `if (entryUpdatedCallback)` → `entryUpdatedCallback()`
- 参照: `Cr.NS_OK`, `containerData.quotaUsage`, `item.lastAccessed`, `item.origin`, `item.persisted`, `item.usage`, `principal.baseDomain`, `principal.originAttributes.partitionKey`, `principal.userContextId`, `request.result`, `request.resultCode`, `site.lastAccessed`, `site.persisted`, `site.quotaUsage`
- XPCOM: `Services.scriptSecurityManager`

## _getAllCookies()
- 位置: L275-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getBaseDomainFromPartitionKey()`, `Number.isInteger()`, `console.error()`, `site.cookies.push()`, `this._getOrInsertSite()`, `this.getBaseDomainFromHost()`
- 条件付き依存: `if (entryUpdatedCallback)` → `entryUpdatedCallback()`
- 条件付き依存: `if (Number.isInteger(cookie.originAttributes.userContextId))` → `this._getOrInsertContainersData()`
- 条件付き依存: `if (Number.isInteger(cookie.originAttributes.userContextId))` → `containerData.lastAccessed.getTime()`
- 条件付き依存: `if (containerData.lastAccessed.getTime() < cookieTime)` → `containerData.lastAccessed.setTime()`
- 参照: `Services.cookies.cookies`, `containerData.cookiesBlocked`, `cookie.lastAccessed`, `cookie.originAttributes.partitionKey`, `cookie.originAttributes.userContextId`, `cookie.rawHost`, `site.lastAccessed`
- XPCOM: `Services.cookies`

## _cancelGetQuotaUsage()
- 位置: L312-317
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._quotaUsageRequest)` → `this._quotaUsageRequest.cancel()`
- 参照: `this._quotaUsageRequest`

## hasSiteData()
- 位置: async L330-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.cookies.hasCookiesForSite()`, `Services.qms.getUsage()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `resolve()`
- 条件付き依存: `if (request.resultCode != Cr.NS_OK)` → `resolve()`
- 条件付き依存: `if (principal.asciiHost == asciiHost)` → `resolve()`
- 参照: `Cr.NS_OK`, `item.origin`, `item.persisted`, `item.usage`, `principal.asciiHost`, `request.result`, `request.resultCode`
- XPCOM: `Services.cookies` / `Services.qms` / `Services.scriptSecurityManager`

## getTotalUsage()
- 位置: L381-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getQuotaUsagePromise.then()`, `this._sites.values()`
- 参照: `site.quotaUsage`

## getQuotaUsageForTimeRanges()
- 位置: async L400-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._sites.values()`
- 参照: `lazy.Sanitizer.timeSpanMsMap`, `site.lastAccessed`, `site.quotaUsage`, `this._getQuotaUsagePromise`

## getSites()
- 位置: async L445-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this._sites.values()).map()`, `this._sites.values()`
- 参照: `site.baseDomainOrHost`, `site.containersData`, `site.cookies`, `site.lastAccessed`, `site.persisted`, `site.quotaUsage`, `this._getQuotaUsagePromise`

## getSite()
- 位置: async L470-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sites.get()`, `this.getBaseDomainFromHost()`
- 参照: `site.baseDomainOrHost`, `site.containersData`, `site.cookies`, `site.lastAccessed`, `site.persisted`, `site.quotaUsage`

## _removePermission()
- 位置: L487-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.removeFromPrincipal()`, `removals.add()`, `removals.has()`
- 参照: `site.principals`
- XPCOM: `Services.perms`

## _removeCookies()
- 位置: L503-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cookies.remove()`
- 参照: `cookie.host`, `cookie.name`, `cookie.originAttributes`, `cookie.path`, `site.cookies`
- XPCOM: `Services.cookies`

## remove()
- 位置: async L528-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Promise.all()`, `promises.push()`, `this.updateSites()`
- 条件付き依存: `if (domainOrHost)` → `Services.eTLD.getSchemelessSiteFromHost()`
- 条件付き依存: `if (domainOrHost)` → `clearData.deleteDataFromSite()`
- 条件付き依存: `if (!(domainOrHost))` → `clearData.deleteDataFromLocalFiles()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL_CACHES`, `Ci.nsIClearDataService.CLEAR_COOKIES_AND_SITE_DATA`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.eTLD`

## promptSiteDataRemoval()
- 位置: L580-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmEx()`, `lazy.gBrandBundle.GetStringFromName()`, `lazy.gStringBundle.GetStringFromName()`, `lazy.gStringBundle.formatStringFromName()`
- 条件付き依存: `if (removals)` → `win.browsingContext.topChromeWindow.openDialog()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `args.allowed`
- XPCOM: `Services.prompt`

## removeAll()
- 位置: async L629-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeCache()`, `this.removeSiteData()`

## removeCache()
- 位置: L639-646
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.deleteData()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL_CACHES`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## removeSiteData()
- 位置: async L654-663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.deleteData()`, `this.updateSites()`
- 参照: `Ci.nsIClearDataService.CLEAR_COOKIES_AND_SITE_DATA`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`
