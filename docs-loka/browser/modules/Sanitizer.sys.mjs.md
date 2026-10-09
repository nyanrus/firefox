# browser/modules/Sanitizer.sys.mjs

source: browser/modules/Sanitizer.sys.mjs
source-hash: f0d146337bab529afd7f6b108c7388ceb286caae
lines: 1383

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## log()
- 位置: L22-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `logConsole.log()`
- 条件付き依存: `if (!logConsole)` → `console.createInstance()`

## TIMESPAN_TODAY()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `new Date().setHours()`

## showUI()
- 位置: async L124-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`
- 条件付き依存: `if (parentWindow?.gDialogBox)` → `parentWindow.gDialogBox.open()`
- 条件付き依存: `if (!(parentWindow?.gDialogBox))` → `Services.ww.openWindow()`
- 参照: `deferred.promise`, `parentWindow?.document.documentURI`, `parentWindow?.gDialogBox`
- XPCOM: `Services.ww`

## onAccept()
- 位置: L140-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.resolve()`

## onCancel()
- 位置: L141-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.resolve()`

## onAccept()
- 位置: L152-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.resolve()`

## onCancel()
- 位置: L153-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deferred.resolve()`

## onStartup()
- 位置: async L166-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `cleanupAfterSanitization()`, `console.error()`, `getAndClearPendingSanitizations()`, `log()`, `pendingSanitizations.findIndex()`, `sanitizeOnShutdown()`, `shutdownClient.addBlocker()`, `this.sanitize()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `addPendingSanitization()`
- 条件付き依存: `if (this.shouldSanitizeNewTabContainer)` → `addPendingSanitization()`
- 条件付き依存: `if (i != -1)` → `pendingSanitizations.splice()`
- 条件付き依存: `if (i != -1)` → `sanitizeNewTabSegregation()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL`, `Sanitizer.PREF_SANITIZE_ON_SHUTDOWN`, `Sanitizer.PREF_SHUTDOWN_BRANCH`, `lazy.PlacesUtils.history.shutdownClient.jsclient`, `options.progress`, `s.id`, `this.PREF_NEWTAB_SEGREGATION`, `this.shouldSanitizeNewTabContainer`, `this.shouldSanitizeOnShutdown`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.prefs`

## fetchState()
- 位置: L201-201
- 役割: (未記入)
- 触るとき: (未記入)

## getClearRange()
- 位置: L250-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `d.setHours()`, `d.setMilliseconds()`, `d.setMinutes()`, `d.setSeconds()`, `d.valueOf()`
- 条件付き依存: `if (ts === undefined)` → `Services.prefs.getIntPref()`
- 参照: `Sanitizer.PREF_TIMESPAN`, `Sanitizer.TIMESPAN_24HOURS`, `Sanitizer.TIMESPAN_2HOURS`, `Sanitizer.TIMESPAN_4HOURS`, `Sanitizer.TIMESPAN_5MIN`, `Sanitizer.TIMESPAN_EVERYTHING`, `Sanitizer.TIMESPAN_HOUR`, `Sanitizer.TIMESPAN_TODAY`
- XPCOM: `Services.prefs`

## sanitize()
- 位置: async L314-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `sanitizeInternal()`
- 条件付き依存: `if (!itemsToClear)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (!progress.isShutdown)` → `shutdownClient.addBlocker()`
- 参照: `lazy.PlacesUtils.history.shutdownClient.jsclient`, `lazy.PrincipalsCollector`, `options.progress`, `progress.isShutdown`, `this.PREF_CPD_BRANCH`, `this.items`
- XPCOM: `Services.obs`

## fetchState()
- 位置: L335-335
- 役割: (未記入)
- 触るとき: (未記入)

## observe()
- 位置: L347-382
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "nsPref:changed")` → `data.startsWith()`
- 条件付き依存: `if ( data.startsWith(this.PREF_SHUTDOWN_BRANCH) && this.shouldSanitizeOnShutdown )` → `removePendingSanitization()`
- 条件付き依存: `if ( data.startsWith(this.PREF_SHUTDOWN_BRANCH) && this.shouldSanitizeOnShutdown )` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if ( data.startsWith(this.PREF_SHUTDOWN_BRANCH) && this.shouldSanitizeOnShutdown )` → `addPendingSanitization()`
- 条件付き依存: `if (data == this.PREF_SANITIZE_ON_SHUTDOWN)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (data == this.PREF_SANITIZE_ON_SHUTDOWN)` → `removePendingSanitization()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (this.shouldSanitizeOnShutdown)` → `addPendingSanitization()`
- 条件付き依存: `if (data == this.PREF_NEWTAB_SEGREGATION)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (data == this.PREF_NEWTAB_SEGREGATION)` → `removePendingSanitization()`
- 条件付き依存: `if (this.shouldSanitizeNewTabContainer)` → `addPendingSanitization()`
- 参照: `Sanitizer.PREF_SANITIZE_ON_SHUTDOWN`, `Sanitizer.PREF_SHUTDOWN_BRANCH`, `this.PREF_NEWTAB_SEGREGATION`, `this.PREF_SANITIZE_ON_SHUTDOWN`, `this.PREF_SHUTDOWN_BRANCH`, `this.shouldSanitizeNewTabContainer`, `this.shouldSanitizeOnShutdown`
- XPCOM: `Services.prefs`

## runSanitizeOnShutdown()
- 位置: async L390-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sanitizeOnShutdown()`

## maybeMigratePrefs()
- 位置: L413-493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( `privacy.sanitize.${context}.hasMigratedToNewPrefs2` ) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!( Services.prefs.getBoolPref( `privacy.sanitize.${context}.hasMigratedToNewPrefs2` ) ))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!( Services.prefs.getBoolPref( `privacy.sanitize.${context}.hasMigratedToNewPrefs2` ) ))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## clear()
- 位置: async L501-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.cache.start()`, `Glean.browserSanitizer.cache.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL_CACHES`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L509-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.cookies.start()`, `Glean.browserSanitizer.cookies.stopAndAccumulate()`, `clearData()`
- 条件付き依存: `if (clearHonoringExceptions)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (clearHonoringExceptions)` → `maybeSanitizeSessionPrincipals()`
- 条件付き依存: `if (!(clearHonoringExceptions))` → `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_BOUNCE_TRACKING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_COOKIES`, `Ci.nsIClearDataService.CLEAR_FINGERPRINTING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_MEDIA_DEVICES`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L539-560
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (clearHonoringExceptions)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (clearHonoringExceptions)` → `maybeSanitizeSessionPrincipals()`
- 条件付き依存: `if (!(clearHonoringExceptions))` → `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_DOM_STORAGES`, `Ci.nsIClearDataService.CLEAR_FINGERPRINTING_PROTECTION_STATE`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L564-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.history.start()`, `Glean.browserSanitizer.history.stopAndAccumulate()`, `Services.clearData.deleteUserInteractionForClearingHistory()`, `clearData()`, `gPrincipalsCollector.getAllPrincipals()`
- 参照: `Ci.nsIClearDataService.CLEAR_CONTENT_BLOCKING_RECORDS`, `Ci.nsIClearDataService.CLEAR_HISTORY`, `lazy.PrincipalsCollector`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## clear()
- 位置: async L599-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.formdata.start()`, `Glean.browserSanitizer.formdata.stopAndAccumulate()`, `Services.wm.getEnumerator()`, `currentDocument.getElementById()`, `lazy.FormHistory.update()`, `lazy.FormHistory.update(change).catch()`, `tabBrowser.clearLastFindValue()`, `tabBrowser.isFindBarInitialized()`
- 条件付き依存: `if (searchBar)` → `input.editor?.clearUndoRedo()`
- 条件付き依存: `if (tabBrowser.isFindBarInitialized(tab))` → `tabBrowser.getCachedFindBar(tab).clear()`
- 条件付き依存: `if (tabBrowser.isFindBarInitialized(tab))` → `tabBrowser.getCachedFindBar()`
- 参照: `change.firstUsedEnd`, `change.firstUsedStart`, `currentWindow.document`, `currentWindow.gBrowser`, `e.message`, `e.result`, `input.value`, `searchBar.textbox`, `tabBrowser.tabs`
- XPCOM: `Services.wm`

## clear()
- 位置: async L656-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.downloads.start()`, `Glean.browserSanitizer.downloads.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_DOWNLOADS`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L664-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.sessions.start()`, `Glean.browserSanitizer.sessions.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_AUTH_CACHE`, `Ci.nsIClearDataService.CLEAR_AUTH_TOKENS`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clear()
- 位置: async L676-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.sitesettings.start()`, `Glean.browserSanitizer.sitesettings.stopAndAccumulate()`, `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_CERT_EXCEPTIONS`, `Ci.nsIClearDataService.CLEAR_CLIENT_AUTH_REMEMBER_SERVICE`, `Ci.nsIClearDataService.CLEAR_CONTENT_PREFERENCES`, `Ci.nsIClearDataService.CLEAR_CREDENTIAL_MANAGER_STATE`, `Ci.nsIClearDataService.CLEAR_DOM_PUSH_NOTIFICATIONS`, `Ci.nsIClearDataService.CLEAR_FINGERPRINTING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_PERMISSIONS`, `Ci.nsIClearDataService.CLEAR_SITE_PERMISSIONS`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## _canCloseWindow()
- 位置: L700-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.CanCloseWindow()`
- 参照: `win.skipNextCanClose`

## _resetAllWindowClosures()
- 位置: L710-714
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `win.skipNextCanClose`

## clear()
- 位置: async L715-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/browser/clh;1"].getService()`, `Date.now()`, `Glean.browserSanitizer.openwindows.start()`, `Services.obs.addObserver()`, `Services.wm.getEnumerator()`, `newWindow.focus()`, `this._canCloseWindow()`, `windowList.pop()`, `windowList.pop().close()`, `windowList.push()`, `windowList[0].openDialog()`
- 条件付き依存: `if (!this._canCloseWindow(someWin))` → `this._resetAllWindowClosures()`
- 条件付き依存: `if (Date.now() > startDate + 60 * 1000)` → `this._resetAllWindowClosures()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `newWindow.addEventListener()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `AppConstants.platform`, `Ci.nsIBrowserHandler`, `handler.defaultArgs`, `windowList.length`
- XPCOM: [`nsIBrowserHandler`](../components/nsIBrowserHandler.idl.md) / `@mozilla.org/browser/clh;1` / `Services.obs` / `Services.wm`

## onFullScreen()
- 位置: L769-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `docEl.getAttribute()`, `newWindow.removeEventListener()`
- 条件付き依存: `if (!newWindow.fullScreen && sizemode == "fullscreen")` → `docEl.setAttribute()`
- 条件付き依存: `if (!newWindow.fullScreen && sizemode == "fullscreen")` → `e.preventDefault()`
- 条件付き依存: `if (!newWindow.fullScreen && sizemode == "fullscreen")` → `e.stopPropagation()`
- 参照: `newWindow.document.documentElement`, `newWindow.fullScreen`

## onWindowOpened()
- 位置: L792-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `newWindow.removeEventListener()`
- 条件付き依存: `if (numWindowsClosing == 0)` → `Glean.browserSanitizer.openwindows.stopAndAccumulate()`
- 条件付き依存: `if (numWindowsClosing == 0)` → `resolve()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.obs`

## onWindowClosed()
- 位置: L813-826
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (numWindowsClosing == 0)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (newWindowOpened)` → `Glean.browserSanitizer.openwindows.stopAndAccumulate()`
- 条件付き依存: `if (newWindowOpened)` → `resolve()`
- XPCOM: `Services.obs`

## clear()
- 位置: async L844-844
- 役割: (未記入)
- 触るとき: (未記入)

## clear()
- 位置: async L850-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.downloads.start()`, `Glean.browserSanitizer.downloads.stopAndAccumulate()`, `Glean.browserSanitizer.history.start()`, `Glean.browserSanitizer.history.stopAndAccumulate()`, `Services.clearData.deleteUserInteractionForClearingHistory()`, `clearChatConversations()`, `clearData()`, `gPrincipalsCollector.getAllPrincipals()`
- 参照: `Ci.nsIClearDataService.CLEAR_CONTENT_BLOCKING_RECORDS`, `Ci.nsIClearDataService.CLEAR_DOWNLOADS`, `Ci.nsIClearDataService.CLEAR_HISTORY`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## clear()
- 位置: async L887-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserSanitizer.cookies.start()`, `Glean.browserSanitizer.cookies.stopAndAccumulate()`, `clearChatConversations()`, `clearData()`
- 条件付き依存: `if (clearHonoringExceptions)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (clearHonoringExceptions)` → `maybeSanitizeSessionPrincipals()`
- 条件付き依存: `if (!(clearHonoringExceptions))` → `clearData()`
- 参照: `Ci.nsIClearDataService.CLEAR_COOKIES_AND_SITE_DATA`, `Ci.nsIClearDataService.CLEAR_MEDIA_DEVICES`, `progress.step`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md)

## clearChatConversations()
- 位置: async L918-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `log()`
- 条件付き依存: `if (range)` → `lazy.ChatStore.deleteConversationsByDateRange()`
- 条件付き依存: `if (!(range))` → `lazy.ChatStore.deleteAllConversations()`
- 参照: `lazy.AIWindow.isEnabled`, `progress.step`

## sanitizeInternal()
- 位置: async L936-1040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Glean.browserSanitizer.total.start()`, `Glean.browserSanitizer.total.stopAndAccumulate()`, `Object.assign()`, `Promise.all()`, `annotateError()`, `handles.map()`, `handles.push()`, `item .clear()`, `itemsToClear.indexOf()`, `log()`
- 条件付き依存: `if (!progress.isShutdown)` → `addPendingSanitization()`
- 条件付き依存: `if (openWindowsIndex != -1)` → `itemsToClear.splice()`
- 条件付き依存: `if (openWindowsIndex != -1)` → `items.openWindows.clear()`
- 条件付き依存: `if (openWindowsIndex != -1)` → `Object.assign()`
- 条件付き依存: `if (!ignoreTimespan && !range)` → `Sanitizer.getClearRange()`
- 条件付き依存: `if (!progress.isShutdown)` → `removePendingSanitization()`
- 参照: `h.promise`, `progress.clearHonoringExceptions`, `progress.isShutdown`, `progress.openWindows`, `progress.openWindowsProgress`

## annotateError()
- 位置: L993-997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`

## sanitizeOnShutdown()
- 位置: async L1042-1150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Sanitizer.maybeMigratePrefs()`, `Services.prefs.getBoolPref()`, `cleanupAfterSanitization()`, `log()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeOnShutdown)` → `getItemsToClearFromPrefBranch()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeOnShutdown)` → `Sanitizer.sanitize()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeOnShutdown)` → `removePendingSanitization()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeNewTabContainer)` → `sanitizeNewTabSegregation()`
- 条件付き依存: `if (Sanitizer.shouldSanitizeNewTabContainer)` → `removePendingSanitization()`
- 条件付き依存: `if (needsSyncSavePrefs)` → `Services.prefs.savePrefFile()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `isSupportedPrincipal()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `log()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `gPrincipalsCollector.getAllPrincipals()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `selectedPrincipals.push()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `extractMatchingPrincipals()`
- 条件付き依存: `if (!Sanitizer.shouldSanitizeOnShutdown)` → `maybeSanitizeSessionPrincipals()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL`, `Ci.nsIClearDataService.CLEAR_ALL_CACHES`, `Ci.nsIClearDataService.CLEAR_BOUNCE_TRACKING_PROTECTION_STATE`, `Ci.nsIClearDataService.CLEAR_COOKIES`, `Ci.nsIClearDataService.CLEAR_DOM_STORAGES`, `Ci.nsIClearDataService.CLEAR_EME`, `Ci.nsICookiePermission.ACCESS_SESSION`, `Sanitizer.PREF_SHUTDOWN_BRANCH`, `Sanitizer.shouldSanitizeNewTabContainer`, `Sanitizer.shouldSanitizeOnShutdown`, `Services.perms.all`, `lazy.PrincipalsCollector`, `permission.capability`, `permission.principal`, `permission.principal.asciiSpec`, `permission.principal.host`, `permission.type`, `progress.advancement`, `progress.sanitizationPrefs`, `progress.sanitizationPrefs.session_permission_exceptions`
- XPCOM: [`nsIClearDataService`](../../toolkit/components/cleardata/nsIClearDataService.idl.md) / [`nsICookiePermission`](../../netwerk/cookie/nsICookiePermission.idl.md) / `Services.perms` / `Services.prefs`

## cleanupAfterSanitization()
- 位置: async L1152-1156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.cleanupAfterDeletionAtShutdown()`
- XPCOM: `Services.clearData`

## extractMatchingPrincipals()
- 位置: L1159-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `principals.filter()`
- 参照: `principal.host`
- XPCOM: `Services.eTLD`

## maybeSanitizeSessionPrincipals()
- 位置: async L1174-1230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.getAllByTypes()`, `isCookieSession()`, `isSupportedPrincipal()`, `log()`, `principals.forEach()`
- 条件付き依存: `if ( perm.capability == Ci.nsIPermissionManager.ALLOW_ACTION && isSupportedPrincipal(perm.principal) )` → `exceptionPartitionSites.add()`
- 条件付き依存: `if ( perm.capability == Ci.nsIPermissionManager.ALLOW_ACTION && isSupportedPrincipal(perm.principal) )` → `shutdownExceptionHosts.push()`
- 条件付き依存: `if (!(isCookieSession(principal)))` → `isShutdownExceptionApplicable()`
- 条件付き依存: `if (!preserve)` → `promises.push()`
- 条件付き依存: `if (!preserve)` → `sanitizeSessionPrincipal()`
- 条件付き依存: `if (promises.length)` → `Promise.all()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `perm.capability`, `perm.principal`, `perm.principal.baseDomain`, `perm.principal.host`, `principals.length`, `progress.step`, `promises.length`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## isShutdownExceptionApplicable()
- 位置: L1237-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getBaseDomainFromPartitionKey()`, `exceptionPartitionSites.has()`
- 条件付き依存: `if (!partitionKey)` → `Services.perms.testPermissionFromPrincipal()`
- 条件付き依存: `if (!partitionKey)` → `shutdownExceptionHosts.some()`
- 条件付き依存: `if (!partitionKey)` → `Services.eTLD.hasRootDomain()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `principal.host`, `principal.originAttributes`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / `Services.eTLD` / `Services.perms`

## isCookieSession()
- 位置: L1265-1270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`
- XPCOM: [`nsICookiePermission`](../../netwerk/cookie/nsICookiePermission.idl.md) / `Services.perms`

## sanitizeSessionPrincipal()
- 位置: async L1272-1285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.deleteDataFromPrincipal()`, `log()`
- 参照: `principal.asciiSpec`, `progress.sanitizePrincipal`
- XPCOM: `Services.clearData`

## sanitizeNewTabSegregation()
- 位置: L1287-1296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getPrivateIdentity()`
- 条件付き依存: `if (identity)` → `Services.clearData.deleteDataFromOriginAttributesPattern()`
- 参照: `identity.userContextId`
- XPCOM: `Services.clearData`

## getItemsToClearFromPrefBranch()
- 位置: L1304-1313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(Sanitizer.items).filter()`, `Services.prefs.getBranch()`, `branch.getBoolPref()`
- 参照: `Sanitizer.items`
- XPCOM: `Services.prefs`

## addPendingSanitization()
- 位置: L1323-1330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `pendingSanitizations.push()`, `safeGetPendingSanitizations()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`
- XPCOM: `Services.prefs`

## removePendingSanitization()
- 位置: L1332-1341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `pendingSanitizations.findIndex()`, `pendingSanitizations.splice()`, `safeGetPendingSanitizations()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`, `s.id`
- XPCOM: `Services.prefs`

## getAndClearPendingSanitizations()
- 位置: L1343-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `safeGetPendingSanitizations()`
- 条件付き依存: `if (pendingSanitizations.length)` → `Services.prefs.clearUserPref()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`, `pendingSanitizations.length`
- XPCOM: `Services.prefs`

## safeGetPendingSanitizations()
- 位置: L1351-1360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `console.error()`
- 参照: `Sanitizer.PREF_PENDING_SANITIZATIONS`
- XPCOM: `Services.prefs`

## clearData()
- 位置: async L1362-1378
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (range)` → `Services.clearData.deleteDataInTimeRange()`
- 条件付き依存: `if (!(range))` → `Services.clearData.deleteData()`
- XPCOM: `Services.clearData`

## isSupportedPrincipal()
- 位置: L1380-1382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http", "https", "file"].some()`, `principal.schemeIs()`
