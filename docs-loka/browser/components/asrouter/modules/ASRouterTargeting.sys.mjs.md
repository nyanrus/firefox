# browser/components/asrouter/modules/ASRouterTargeting.sys.mjs

source: browser/components/asrouter/modules/ASRouterTargeting.sys.mjs
source-hash: 7336d2a27627c8c7809e0ddda8aa8322b60798ab
lines: 2104

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Number.isInteger()`, `PlacesUtils.history.pageFrecencyThreshold()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `parseInt()`

## _extractMailDomainFromURI()
- 位置: L271-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `Services.io.newURI(uriTemplate).host`
- XPCOM: `Services.io`

## CachedTargetingGetter()
- 位置: L290-313
- 役割: (未記入)
- 触るとき: (未記入)

## expire()
- 位置: L300-303
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastUpdated`, `this._value`

## get()
- 位置: async L304-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (now - this._lastUpdated >= updateInterval)` → `getter[property]()`
- 参照: `this._lastUpdated`, `this._value`

## CacheUnhandledCampaignAction()
- 位置: L315-350
- 役割: (未記入)
- 触るとき: (未記入)

## expire()
- 位置: L319-322
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastUpdated`, `this._value`

## get()
- 位置: L323-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (!lazy.didHandleCampaignAction)` → `lazy.AttributionCode.getCachedAttributionData()`
- 条件付き依存: `if (!lazy.didHandleCampaignAction)` → `attributionData?.campaign?.toUpperCase()`
- 条件付き依存: `if (!lazy.didHandleCampaignAction)` → `ALLOWED_CAMPAIGN_ACTIONS.includes()`
- 参照: `lazy.didHandleCampaignAction`, `this._lastUpdated`, `this._value`

## CheckBrowserNeedsUpdate()
- 位置: L352-396
- 役割: (未記入)
- 触るとき: (未記入)

## setUp()
- 位置: L359-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 参照: `this._lastUpdated`, `this._value`

## expire()
- 位置: L363-366
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastUpdated`, `this._value`

## get()
- 位置: async L367-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.UpdateCheckSvc.checkForUpdates()`
- 条件付き依存: `if (!result.succeeded)` → `lazy.ASRouterPreferences.console.error()`
- 参照: `AppConstants.MOZ_UPDATER`, `check.result`, `checker._value`, `lazy.AUS.canCheckForUpdates`, `lazy.UpdateCheckSvc.FOREGROUND_CHECK`, `result.request`, `result.succeeded`, `result.updates.length`, `this._lastUpdated`, `this._value`

## expireAll()
- 位置: L399-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(this.getters).forEach()`, `Object.keys(this.queries).forEach()`, `this.getters[key].expire()`, `this.queries[query].expire()`
- 参照: `this.getters`, `this.queries`

## getMailtoHandlerHost()
- 位置: L487-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_extractMailDomainFromURI()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`
- 参照: `AppConstants.platform`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIWebHandlerApp`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`, `handlerInfo.preferredApplicationHandler.uriTemplate`
- XPCOM: [`nsIHandlerInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## getProfileGroupProfileCount()
- 位置: L525-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.SelectableProfileService.getProfileCount()`
- XPCOM: `Services.prefs`

## findBackupsInWellKnownLocations()
- 位置: async L542-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bs.findBackupsInWellKnownLocations()`, `lazy.BackupService.get()`, `lazy.BackupService.init()`

## getRelayProfileInfo()
- 位置: async L560-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FirefoxRelay.getRelayProfileInfo()`

## getCrashData()
- 位置: async L570-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.crashmanager.getCrashes()`, `crashes.map()`
- 参照: `Services.crashmanager`, `crash.crashDate`, `crash.id`
- XPCOM: `Services.crashmanager`

## sortMessagesByWeightedRank()
- 位置: L604-612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.pow()`, `Math.random()`, `messages .map()`, `messages .map(message => ({ message, rank: Math.pow(Math.random(), 1 / message.weight), })) .sort()`
- 参照: `a.rank`, `b.rank`, `message.weight`

## getSortedMessages()
- 位置: L623-662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNaN()`, `result.sort()`
- 条件付き依存: `if (!ordered)` → `sortMessagesByWeightedRank()`
- 条件付き依存: `if (ordered)` → `isNaN()`
- 参照: `a.order`, `a.priority`, `a.targeting`, `b.order`, `b.priority`, `b.targeting`

## parseAboutPageURL()
- 位置: L671-701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (lazy.ExtensionUtils.isExtensionUrl(url))` → `ret.urls.push()`
- 条件付き依存: `if (!(lazy.ExtensionUtils.isExtensionUrl(url)))` → `url.split()`
- 条件付き依存: `if (!(lazy.ExtensionUtils.isExtensionUrl(url)))` → `["about:home", "about:newtab", "about:blank"].includes()`
- 条件付き依存: `if (!(lazy.ExtensionUtils.isExtensionUrl(url)))` → `parsedURL.hostname.replace()`
- 条件付き依存: `if (!(lazy.ExtensionUtils.isExtensionUrl(url)))` → `ret.urls.push()`
- 条件付き依存: `if (!ret.urls.length)` → `ret.urls.push()`
- 参照: `ret.isCustomUrl`, `ret.isWebExt`, `ret.urls.length`

## getAutofillRecords()
- 位置: async L716-732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `actor?.getRecords()`, `win.gBrowser.selectedBrowser.browsingContext.currentWindowGlobal.getActor()`
- 参照: `records?.length`
- XPCOM: `Services.wm`

## decodeAttributionValue()
- 位置: L736-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeURIComponent()`, `decodedValue.includes()`

## getPinStatus()
- 位置: async L758-760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShellService.doesAppNeedPin()`

## locale()
- 位置: L763-765
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## localeLanguageCode()
- 位置: L766-771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.locale.appLocaleAsBCP47.substr()`
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## browserSettings()
- 位置: L772-777
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.TelemetryEnvironment.currentEnvironment`, `settings.update`

## attributionData()
- 位置: L778-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AttributionCode.getCachedAttributionData()`

## currentDate()
- 位置: L782-784
- 役割: (未記入)
- 触るとき: (未記入)

## canCreateSelectableProfiles()
- 位置: L785-790
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_SELECTABLE_PROFILES`, `lazy.SelectableProfileService?.isEnabled`

## hasSelectableProfiles()
- 位置: L791-793
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.profilesCreated`

## profileAgeCreated()
- 位置: L794-796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ProfileAge()`, `lazy.ProfileAge().then()`
- 参照: `times.created`

## profileAgeReset()
- 位置: L797-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ProfileAge()`, `lazy.ProfileAge().then()`
- 参照: `times.reset`

## profileLastUse()
- 位置: L800-809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`
- 参照: `Services.appinfo.replacedLockTime`, `Services.prefs.userPrefsFileLastModifiedAtStartup`
- XPCOM: `Services.appinfo` / `Services.prefs`

## canResetProfile()
- 位置: L810-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ResetProfile.resetSupported()`

## isFirefoxReinstalled()
- 位置: L813-815
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ReinstallCheck.wasReinstalled`

## usesFirefoxSync()
- 位置: L816-818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## isFxAEnabled()
- 位置: L819-821
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.isFxAEnabled`

## isFxASignedIn()
- 位置: L822-835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `lazy.fxAccounts .getSignedInUser()`, `lazy.fxAccounts .getSignedInUser() .then()`, `lazy.fxAccounts .getSignedInUser() .then(data => resolve(!!data)) .catch()`, `resolve()`
- 条件付き依存: `if (!lazy.isFxAEnabled)` → `resolve()`
- 条件付き依存: `if (Services.prefs.getStringPref(FXA_USERNAME_PREF, ""))` → `resolve()`
- 参照: `lazy.isFxAEnabled`
- XPCOM: `Services.prefs`

## sync()
- 位置: L836-842
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.clientsDevicesDesktop`, `lazy.clientsDevicesMobile`, `lazy.syncNumClients`

## xpinstallEnabled()
- 位置: L843-846
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.isXPIInstallEnabled`

## addonsInfo()
- 位置: L847-892
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/backgroundtasks;1"]?.getService()`, `lazy.AddonManager.getActiveAddons()`, `lazy.AddonManager.getActiveAddons(["extension", "service"]).then()`, `testAddons.includes()`
- 条件付き依存: `if (fullData)` → `Object.assign()`
- 参照: `Ci.nsIBackgroundTasks`, `addon.hidden`, `addon.id`, `addon.installDate`, `addon.isBuiltin`, `addon.isSystem`, `addon.isWebExtension`, `addon.name`, `addon.type`, `addon.userDisabled`, `addon.version`, `bts?.isBackgroundTaskMode`
- XPCOM: [`nsIBackgroundTasks`](../../../../toolkit/components/backgroundtasks/nsIBackgroundTasks.idl.md) / `@mozilla.org/backgroundtasks;1`

## searchEngines()
- 位置: L893-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/backgroundtasks;1"]?.getService()`, `Object.fromEntries()`, `engines.map()`, `lazy.SearchService.getAppProvidedEngines()`, `lazy.SearchService.getAppProvidedEngines() .then()`, `resolve()`
- 条件付き依存: `if (bts?.isBackgroundTaskMode)` → `Promise.resolve()`
- 参照: `Ci.nsIBackgroundTasks`, `bts?.isBackgroundTaskMode`, `defaultEngine.id`, `e.hasBeenUsed`, `e.id`, `engine.id`, `lazy.AppProvidedConfigEngine`, `lazy.SearchService`
- XPCOM: [`nsIBackgroundTasks`](../../../../toolkit/components/backgroundtasks/nsIBackgroundTasks.idl.md) / `@mozilla.org/backgroundtasks;1`

## recentSearchCount()
- 位置: L926-935
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.FormHistory.count()`, `lazy.FormHistory.count({ fieldname: lazy.searchFormHistoryFieldname, lastUsedStart, }).catch()`
- 参照: `lazy.searchFormHistoryFieldname`

## isDefaultBrowser()
- 位置: L936-938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.isDefaultBrowser.get()`, `QueryCache.getters.isDefaultBrowser.get().catch()`

## isDefaultBrowserUncached()
- 位置: L939-941
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShellService.isDefaultBrowser()`

## hasAttemptedSetDefault()
- 位置: L942-944
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ShellService.attemptedSetDefaultThisSession`

## isOneClickSetDefaultEnabled()
- 位置: L945-949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.isOneClickSetDefaultEnabled .get()`, `QueryCache.getters.isOneClickSetDefaultEnabled .get() .catch()`

## devToolsOpenedCount()
- 位置: L950-952
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.devtoolsSelfXSSCount`

## topFrecentSites()
- 位置: L953-962
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.TopFrecentSites.get()`, `QueryCache.queries.TopFrecentSites.get().then()`, `sites.map()`
- 参照: `new URL(site.url).hostname`, `site.frecency`, `site.lastVisitDate`, `site.url`

## recentBookmarks()
- 位置: L963-965
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.RecentBookmarks.get()`

## pinnedSites()
- 位置: L966-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NewTabUtils.pinnedLinks.links.map()`
- 参照: `new URL(site.url).hostname`, `site.searchTopSite`, `site.url`

## providerCohorts()
- 位置: L977-982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterPreferences.providers.reduce()`
- 参照: `current.cohort`, `current.id`

## totalBookmarksCount()
- 位置: L983-985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.TotalBookmarksCount.get()`

## firefoxVersion()
- 位置: L986-988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppConstants.MOZ_APP_VERSION.match()`, `parseInt()`

## region()
- 位置: L989-991
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.Region.home`

## needsUpdate()
- 位置: L992-994
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.CheckBrowserNeedsUpdate.get()`

## savedTabGroups()
- 位置: L995-997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getSavedTabGroups()`
- 参照: `lazy.SessionStore.getSavedTabGroups().length`

## currentTabGroups()
- 位置: L998-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.gBrowser.getAllTabGroups()`
- 参照: `win.gBrowser.getAllTabGroups().length`

## tabsOpenInTopWindow()
- 位置: L1009-1017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 参照: `win.gBrowser.tabs.length`

## installedWebAppsCount()
- 位置: L1018-1020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TaskbarTabs.countTaskbarTabs()`

## currentTabInstalledAsWebApp()
- 位置: L1021-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.TaskbarTabs.findTaskbarTab()`, `lazy.TaskbarTabs.findTaskbarTab( win.gBrowser.selectedBrowser.currentURI, win.gBrowser.selectedTab.userContextId ) .then()`
- 参照: `win.gBrowser.selectedBrowser.currentURI`, `win.gBrowser.selectedTab.userContextId`

## hasPinnedTabs()
- 位置: L1042-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `win.gBrowser.visibleTabs.filter()`
- 参照: `t.pinned`, `win.closed`, `win.gBrowser`, `win.gBrowser.visibleTabs.filter(t => t.pinned).length`
- XPCOM: `Services.wm`

## hasActiveAIWindow()
- 位置: L1054-1056
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow?.hasActiveAIWindows()`

## isSmartTabGroupingAllowed()
- 位置: L1057-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SmartTabGroupingManager?.isAllowed`

## hasAccessedFxAPanel()
- 位置: L1060-1062
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasAccessedFxAPanel`

## userPrefs()
- 位置: L1063-1068
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.cfrAddonsUserPref`, `lazy.cfrFeaturesUserPref`

## totalBlockedCount()
- 位置: L1069-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TrackingDBService.sumAllEvents()`

## blockedCountByType()
- 位置: L1072-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dateTo.getTime()`, `day.getResultByName()`, `eventsByDate.reduce()`, `idToTextMap.get()`, `idToTextMap.values()`, `lazy.TrackingDBService.getEventsByDateRange()`, `lazy.TrackingDBService.getEventsByDateRange(dateFrom, dateTo).then()`
- 参照: `Ci.nsITrackingDBService.CRYPTOMINERS_ID`, `Ci.nsITrackingDBService.FINGERPRINTERS_ID`, `Ci.nsITrackingDBService.SOCIAL_ID`, `Ci.nsITrackingDBService.TRACKERS_ID`, `Ci.nsITrackingDBService.TRACKING_COOKIES_ID`
- XPCOM: [`nsITrackingDBService`](../../../../toolkit/components/antitracking/nsITrackingDBService.idl.md)

## attachedFxAOAuthClients()
- 位置: L1099-1108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.fxAccounts .listAttachedOAuthClients()`, `lazy.fxAccounts .listAttachedOAuthClients() .then()`, `lazy.fxAccounts .listAttachedOAuthClients() .then(clients => resolve(clients)) .catch()`, `resolve()`
- 参照: `this.usesFirefoxSync`

## relayProfileInfo()
- 位置: L1109-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.relayProfileInfo.get()`

## relayEmailMasksCount()
- 位置: L1112-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.relayProfileInfo .get()`, `QueryCache.getters.relayProfileInfo .get() .then()`
- 参照: `info?.masksCount`

## isRelayFreeTier()
- 位置: L1117-1121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.relayProfileInfo .get()`, `QueryCache.getters.relayProfileInfo .get() .then()`
- 参照: `info.has_premium`

## platformName()
- 位置: L1122-1124
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## userId()
- 位置: L1125-1127
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ClientEnvironment.userId`

## profileRestartCount()
- 位置: L1128-1141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/backgroundtasks;1"]?.getService()`, `lazy.TelemetrySession.getMetadata()`
- 参照: `Ci.nsIBackgroundTasks`, `bts?.isBackgroundTaskMode`, `lazy.TelemetrySession.getMetadata("targeting").profileSubsessionCounter`
- XPCOM: [`nsIBackgroundTasks`](../../../../toolkit/components/backgroundtasks/nsIBackgroundTasks.idl.md) / `@mozilla.org/backgroundtasks;1`

## homePageSettings()
- 位置: L1142-1153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.HomePage.get()`, `parseAboutPageURL()`
- 参照: `lazy.HomePage.isDefault`, `lazy.HomePage.locked`

## newtabSettings()
- 位置: L1154-1165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseAboutPageURL()`
- 参照: `lazy.AboutNewTab.activityStreamEnabled`, `lazy.AboutNewTab.newTabURL`, `urls[0].host`, `urls[0].url`

## activeNotifications()
- 位置: L1166-1214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/backgroundtasks;1"]?.getService()`, `Date.now()`, `Services.obs.notifyObservers()`, `lazy.BrowserWindowTracker.getTopWindow()`, `window.gBrowser.readNotificationBox()`, `window.gBrowser?.selectedBrowser.hasAttribute()`
- 参照: `Ci.nsIBackgroundTasks`, `bts?.isBackgroundTaskMode`, `lazy.FeatureCalloutBroker.isCalloutShowing`, `lazy.newTabTopicModalLastSeen`, `subjectWithBrowser.activeNewtabMessage`, `window.gBrowser`, `window.gBrowser.readNotificationBox()?.currentNotification`, `window.gDialogBox?.isOpen`, `window.gNotificationBox?.currentNotification`, `window.gURLBar?.view.isOpen`
- XPCOM: [`nsIBackgroundTasks`](../../../../toolkit/components/backgroundtasks/nsIBackgroundTasks.idl.md) / `@mozilla.org/backgroundtasks;1` / `Services.obs`

## isMajorUpgrade()
- 位置: L1216-1218
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BrowserHandler.majorUpgrade`

## hasActiveEnterprisePolicies()
- 位置: L1220-1222
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.policies.ACTIVE`, `Services.policies.status`
- XPCOM: `Services.policies`

## userMonthlyActivity()
- 位置: L1224-1226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.UserMonthlyActivity.get()`

## allowedNotificationOrigins()
- 位置: L1228-1233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms .getAllByTypes()`, `Services.perms .getAllByTypes(["desktop-notification"]) .filter()`
- 参照: `Services.perms.ALLOW_ACTION`, `perm.capability`
- XPCOM: `Services.perms`

## doesAppNeedPin()
- 位置: L1235-1242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.doesAppNeedPin.get()`, `QueryCache.getters.doesAppNeedStartMenuPin.get()`

## doesAppNeedPinUncached()
- 位置: L1244-1246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPinStatus()`

## doesAppNeedPrivatePin()
- 位置: L1248-1250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.doesAppNeedPrivatePin.get()`

## launchOnLoginEnabled()
- 位置: L1252-1257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LaunchOnLogin.isEnabled()`, `lazy.LaunchOnLogin.isSupported()`

## launchOnLoginAllowedByPolicy()
- 位置: L1262-1267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LaunchOnLogin.isAllowed()`, `lazy.LaunchOnLogin.isSupported()`

## isMSIX()
- 位置: L1269-1280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.sysinfo`

## packageFamilyName()
- 位置: L1282-1296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.sysinfo`

## isBackgroundTaskMode()
- 位置: L1303-1308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/backgroundtasks;1"]?.getService()`
- 参照: `Ci.nsIBackgroundTasks`, `bts?.isBackgroundTaskMode`
- XPCOM: [`nsIBackgroundTasks`](../../../../toolkit/components/backgroundtasks/nsIBackgroundTasks.idl.md) / `@mozilla.org/backgroundtasks;1`

## backgroundTaskName()
- 位置: L1317-1322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/backgroundtasks;1"]?.getService()`, `bts?.backgroundTaskName()`
- 参照: `Ci.nsIBackgroundTasks`
- XPCOM: [`nsIBackgroundTasks`](../../../../toolkit/components/backgroundtasks/nsIBackgroundTasks.idl.md) / `@mozilla.org/backgroundtasks;1`

## userPrefersReducedMotion()
- 位置: L1324-1326
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo.prefersReducedMotion`
- XPCOM: `Services.appinfo`

## distributionId()
- 位置: L1333-1337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getDefaultBranch()`, `Services.prefs .getDefaultBranch(null) .getCharPref()`
- XPCOM: `Services.prefs`

## fxViewButtonAreaType()
- 位置: L1345-1348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`
- 参照: `button.areaType`

## alltabsButtonAreaType()
- 位置: L1350-1353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getWidget()`
- 参照: `button.areaType`

## html()
- 位置: L1356-1358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.isDefaultHTMLHandler.get()`

## pdf()
- 位置: L1359-1361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.isDefaultPDFHandler.get()`

## mailto()
- 位置: L1362-1364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.isDefaultMailtoHandler.get()`

## defaultPDFHandler()
- 位置: L1367-1369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.defaultPDFHandler.get()`

## mailtoHandlerHost()
- 位置: L1371-1373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.mailtoHandlerHost.get()`

## creditCardsSaved()
- 位置: L1375-1377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getAutofillRecords()`

## addressesSaved()
- 位置: L1379-1381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getAutofillRecords()`

## hasMigratedBookmarks()
- 位置: L1388-1390
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasMigratedBookmarks`

## hasMigratedCSVPasswords()
- 位置: L1399-1401
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasMigratedCSVPasswords`

## hasMigratedHistory()
- 位置: L1408-1410
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasMigratedHistory`

## hasMigratedPasswords()
- 位置: L1417-1419
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.hasMigratedPasswords`

## useEmbeddedMigrationWizard()
- 位置: L1429-1431
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.useEmbeddedMigrationWizard`

## newtabAddonVersion()
- 位置: L1439-1441
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AboutNewTabResourceMapping.addonVersion`

## isRTAMO()
- 位置: L1449-1456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decodeAttributionValue()`, `decodeAttributionValue(attributionData?.content)?.startsWith()`
- 参照: `attributionData?.content`, `attributionData?.source`

## isDeviceMigration()
- 位置: L1464-1468
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `attributionData?.campaign`

## isSmartWindowOnboarding()
- 位置: L1476-1480
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `attributionData?.campaign`

## unhandledCampaignAction()
- 位置: L1491-1493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.UnhandledCampaignAction.get()`

## primaryResolution()
- 位置: L1503-1520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `primaryScreen.GetAvailRect()`
- 参照: `availDeviceHeight.value`, `availDeviceWidth.value`, `lazy.ScreenManager`

## archBits()
- 位置: L1522-1533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 条件付き依存: `if (bits)` → `Number()`
- XPCOM: `Services.sysinfo`

## systemArch()
- 位置: L1535-1541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.get()`
- XPCOM: `Services.sysinfo`

## memoryMB()
- 位置: L1543-1554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`
- 条件付き依存: `if (memory)` → `Number()`
- XPCOM: `Services.sysinfo`

## totalSearches()
- 位置: L1556-1558
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.totalSearches`

## profileGroupId()
- 位置: L1560-1562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.profileGroupId.get()`

## currentProfileId()
- 位置: L1564-1569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SelectableProfileService.currentProfile.id.toString()`
- 参照: `lazy.SelectableProfileService.currentProfile`

## profileGroupProfileCount()
- 位置: L1571-1573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.profileGroupProfileCount.get()`

## buildId()
- 位置: L1575-1577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`
- 参照: `AppConstants.MOZ_BUILDID`

## backupsInfo()
- 位置: L1579-1589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.backupsInfo.get()`, `QueryCache.getters.backupsInfo.get().catch()`
- 条件付き依存: `if (AppConstants.platform === "macosx")` → `Promise.resolve()`
- 参照: `AppConstants.platform`

## backupArchiveEnabled()
- 位置: L1591-1599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BackupService.get()`, `lazy.BackupService.init()`
- 参照: `bs.archiveEnabledStatus.enabled`

## backupRestoreEnabled()
- 位置: L1601-1609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BackupService.get()`, `lazy.BackupService.init()`
- 参照: `bs.restoreEnabledStatus.enabled`

## isEncryptedBackup()
- 位置: L1611-1618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## isPrivateWindow()
- 位置: L1620-1629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`

## isTaskbarTabWindow()
- 位置: L1631-1639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.document.documentElement.hasAttribute()`

## canRestoreLastSession()
- 位置: L1641-1643
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SessionStore.canRestoreLastSession`

## autoRestoreSessionEnabled()
- 位置: L1650-1652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## tabNotesCount()
- 位置: L1658-1660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabNotes.count()`, `lazy.TabNotes.init()`, `lazy.TabNotes.init().then()`

## userWeekdaysActiveInLastMonth()
- 位置: L1663-1672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.UserMonthlyActivity.get()`, `QueryCache.queries.UserMonthlyActivity.get().then()`, `String()`, `String(entry[1]).split()`, `String(entry[1]).split("-").map()`, `activity.filter()`, `new Date(year, month - 1, date).getDay()`

## userActiveDaysWithHundredPlusSites()
- 位置: L1675-1679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.queries.UserMonthlyActivity.get()`, `QueryCache.queries.UserMonthlyActivity.get().then()`, `activity.filter()`
- 参照: `activity.filter(entry => entry[0] >= 100).length`

## experimentsLoaded()
- 位置: L1686-1702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterPreferences.console.error()`
- 参照: `lazy.ExperimentAPI._rsLoader?._hasUpdatedOnce`, `lazy.ExperimentAPI.enabled`

## crashCount()
- 位置: L1710-1712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QueryCache.getters.crashData.get()`, `QueryCache.getters.crashData.get().then()`
- 参照: `crashes.length`

## daysSinceLastCrash()
- 位置: L1721-1729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Math.max()`, `QueryCache.getters.crashData.get()`, `QueryCache.getters.crashData.get().then()`, `crashes.map()`
- 参照: `c.date`, `crashes.length`

## crashCountInLastDay()
- 位置: L1738-1743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `QueryCache.getters.crashData.get()`, `QueryCache.getters.crashData.get().then()`, `crashes.filter()`
- 参照: `c.date`, `crashes.filter(c => c.date >= cutoff).length`

## crashCountInLastWeek()
- 位置: L1752-1757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `QueryCache.getters.crashData.get()`, `QueryCache.getters.crashData.get().then()`, `crashes.filter()`
- 参照: `c.date`, `crashes.filter(c => c.date >= cutoff).length`

## isLaunchOnLogin()
- 位置: L1764-1766
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BrowserInitState.isLaunchOnLogin`

## previousSessionCrashed()
- 位置: L1773-1775
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SessionStartup.previousSessionCrashed`

## addAIWindowTargeting()
- 位置: L1778-1789
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/\bisAIWindow\b/.test()`

## getEnvironmentSnapshot()
- 位置: async L1816-1906
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Object.assign()`, `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `quitApplication.catch()`, `resolve()`, `targets.toReversed()`
- 参照: `ASRouterTargeting.Environment`
- XPCOM: `Services.obs`

## observe()
- 位置: L1831-1837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`

## resolve()
- 位置: async L1845-1888
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(object))` → `Promise.all()`
- 条件付き依存: `if (Array.isArray(object))` → `object.map()`
- 条件付き依存: `if (Array.isArray(object))` → `resolve()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Object.keys(object).map()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Object.keys()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Promise.race()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `resolve()`
- 条件付き依存: `if (typeof object === "object" && object !== null)` → `Promise.allSettled()`
- 参照: `Services.startup.shuttingDown`, `result.status`, `result.value`
- XPCOM: `Services.startup`

## getMessageTriggers()
- 位置: L1916-1921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `message.trigger`, `message.triggers`, `message?.trigger`, `message?.triggers`

## isTriggerMatch()
- 位置: L1923-1956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidateMessageTrigger.params.filter()`, `candidateMessageTrigger.params.includes()`, `new MatchPatternSet(candidateMessageTrigger.patterns).matches()`
- 参照: `candidateMessageTrigger.id`, `candidateMessageTrigger.params`, `candidateMessageTrigger.params.filter( t => (t & trigger.param.type) === t ).length`, `candidateMessageTrigger.params.filter(t => t === trigger.param.type) .length`, `candidateMessageTrigger.patterns`, `trigger.id`, `trigger.param`, `trigger.param.host`, `trigger.param.type`, `trigger.param.url`

## getCachedEvaluation()
- 位置: L1964-1974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `jexlEvaluationCache.has()`
- 条件付き依存: `if (jexlEvaluationCache.has(targeting))` → `jexlEvaluationCache.get()`
- 条件付き依存: `if (jexlEvaluationCache.has(targeting))` → `Date.now()`
- 条件付き依存: `if (jexlEvaluationCache.has(targeting))` → `jexlEvaluationCache.delete()`

## checkMessageTargeting()
- 位置: async L1985-2020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `addAIWindowTargeting()`, `console.error()`, `lazy.ASRouterPreferences.console.debug()`, `targetingContext.evalWithDefault()`, `targetingContext.setTelemetrySource()`
- 条件付き依存: `if (shouldCache)` → `this.getCachedEvaluation()`
- 条件付き依存: `if (shouldCache)` → `jexlEvaluationCache.set()`
- 条件付き依存: `if (shouldCache)` → `Date.now()`
- 条件付き依存: `if (onError)` → `onError()`
- 参照: `message.id`, `result.value`

## _isMessageMatch()
- 位置: L2022-2044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messageTriggers.some()`, `this.checkMessageTargeting()`, `this.getMessageTriggers()`, `this.isTriggerMatch()`
- 参照: `messageTriggers.length`, `trigger?.id`

## findMatchingMessage()
- 位置: async L2059-2102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSortedMessages()`, `isMatch()`, `lazy.ASRouterPreferences.console.debug()`, `lazy.TargetingContext.combineContexts()`
- 条件付き依存: `if (await isMatch(candidate))` → `matching.push()`
- 参照: `lazy.TargetingContext`, `this.Environment`, `trigger.context`

## isMatch()
- 位置: L2082-2089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isMessageMatch()`
