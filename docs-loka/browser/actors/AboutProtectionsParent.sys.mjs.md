# browser/actors/AboutProtectionsParent.sys.mjs

source: browser/actors/AboutProtectionsParent.sys.mjs
source-hash: 8933d7cb8544202e322c36e81356d0216cb5a848
lines: 430

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Services.prefs.getStringPref()`, `Services.urlFormatter.formatURLPref()`, `XPCOMUtils.defineLazyServiceGetter()`

## AboutProtectionsParent.constructor()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## AboutProtectionsParent.setTestOverride()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)

## AboutProtectionsParent.fetchUserBreachStats()
- 位置: async L100-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`, `headers.append()`
- 条件付き依存: `if (monitorResponse && monitorResponse.timestamp)` → `Date.now()`
- 条件付き依存: `if (response.ok)` → `response.json()`
- 条件付き依存: `if (response.ok)` → `MONITOR_RESPONSE_PROPS.includes()`
- 条件付き依存: `if (isValid)` → `Date.now()`
- 参照: `monitorResponse.timestamp`, `response.ok`, `response.status`

## AboutProtectionsParent.getLoginData()
- 位置: async L165-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.countLoginsAsync()`, `console.error()`, `lazy.fxAccounts.device.recentDeviceList.filter()`, `lazy.fxAccounts.getSignedInUser()`
- 条件付き依存: `if (gTestOverride && "getLoginData" in gTestOverride)` → `gTestOverride.getLoginData()`
- 条件付き依存: `if (await lazy.fxAccounts.getSignedInUser())` → `lazy.fxAccounts.device.refreshDeviceList()`
- 条件付き依存: `if (userFacingLogins && Services.logins.isLoggedIn)` → `lazy.LoginHelper.getAllUserFacingLogins()`
- 条件付き依存: `if (userFacingLogins && Services.logins.isLoggedIn)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 参照: `Services.logins.isLoggedIn`, `device.type`, `e.message`, `lazy.FXA_PWDMGR_HOST`, `lazy.FXA_PWDMGR_REALM`, `lazy.fxAccounts.device.recentDeviceList`, `lazy.fxAccounts.device.recentDeviceList.filter( device => device.type == "mobile" ).length`, `potentiallyBreachedLogins.size`
- XPCOM: `Services.logins`

## AboutProtectionsParent.getMonitorData()
- 位置: async L224-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.getMonitorScopedOAuthToken()`
- 条件付き依存: `if (gTestOverride && "getMonitorData" in gTestOverride)` → `gTestOverride.getMonitorData()`
- 条件付き依存: `if (gTestOverride && "getMonitorData" in gTestOverride)` → `Date.now()`
- 条件付き依存: `if (gTestOverride && "getMonitorData" in gTestOverride)` → `this.fetchUserBreachStats()`
- 条件付き依存: `if (token)` → `this.fetchUserBreachStats()`
- 条件付き依存: `if (token)` → `lazy.fxAccounts.getSignedInUser()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `lazy.fxAccounts.removeCachedOAuthToken()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `this.getMonitorScopedOAuthToken()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `this.fetchUserBreachStats()`
- 条件付き依存: `if (e.message === INVALID_OAUTH_TOKEN)` → `console.error()`
- 条件付き依存: `if (e.message === USER_UNSUBSCRIBED_TO_MONITOR)` → `lazy.fxAccounts.getSignedInUser()`
- 参照: `e.message`, `monitorData.errorMessage`, `monitorResponse.timestamp`

## AboutProtectionsParent.getMonitorScopedOAuthToken()
- 位置: async L284-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.fxAccounts.getOAuthToken()`
- 参照: `e.message`

## AboutProtectionsParent.VPNSubStatus()
- 位置: async L299-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `fetch()`, `headers.append()`, `lazy.fxAccounts.getOAuthToken()`
- 条件付き依存: `if (gTestOverride && "vpnOverrides" in gTestOverride)` → `gTestOverride.vpnOverrides()`
- 条件付き依存: `if (res.ok)` → `res.json()`
- 参照: `e.message`, `res.ok`, `sub.subscriptionId`

## AboutProtectionsParent.receiveMessage()
- 位置: async L333-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[7, 1, 2, 3, 4, 5, 6].map()`, `displayNames.of()`, `idToTextMap.get()`, `lazy.BrowserUtils.shouldShowVPNPromo()`, `lazy.LoginHelper.openPasswordManager()`, `lazy.PrivacyMetricsService.getWeeklyStats()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.TrackingDBService.getEarliestRecordedDate()`, `lazy.TrackingDBService.getEventsByDateRange()`, `lazy.TrackingDBService.sumAllEvents()`, `result.getResultByName()`, `this.VPNSubStatus()`, `this.getLoginData()`, `this.getMonitorData()`, `win.openPreferences()`, `win.openTrustedLinkIn()`
- 参照: `Services.intl.DisplayNames`, `aMessage.data.entrypoint`, `aMessage.data.from`, `aMessage.data.to`, `aMessage.name`, `dataToSend.earliestDate`, `dataToSend.isPrivate`, `dataToSend.largest`, `dataToSend.sumEvents`, `dataToSend.weekdays`, `dataToSend[timestamp].total`, `this.browsingContext.top.embedderElement.documentGlobal`
- XPCOM: `Services.intl`
