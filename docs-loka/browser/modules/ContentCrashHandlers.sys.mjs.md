# browser/modules/ContentCrashHandlers.sys.mjs

source: browser/modules/ContentCrashHandlers.sys.mjs
source-hash: 0c31dbcbc9c97e3e93e5efdd43cf9e904745efdc
lines: 1398

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBranch()`, `console.createInstance()`, `lazy.cleanerPrefs.getStringPref()`

## BrowserWeakMap.get()
- 位置: L60-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.get()`
- 条件付き依存: `if (browser.permanentKey)` → `super.get()`
- 参照: `browser.permanentKey`

## BrowserWeakMap.set()
- 位置: L67-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.set()`
- 条件付き依存: `if (browser.permanentKey)` → `super.set()`
- 参照: `browser.permanentKey`

## BrowserWeakMap.delete()
- 位置: L74-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.delete()`
- 条件付き依存: `if (browser.permanentKey)` → `super.delete()`
- 参照: `browser.permanentKey`

## prefs()
- 位置: L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBranch()`
- 参照: `this.prefs`
- XPCOM: `Services.prefs`

## init()
- 位置: L101-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L111-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.exists()`, `aSubject.QueryInterface()`, `aSubject.get()`, `this.browserMap.set()`, `this.flushCrashedBrowserQueue()`, `this.getAndRemoveSubframeCrash()`
- 条件付き依存: `if (!dumpID)` → `Glean.browserContentCrash.dumpUnavailable.add()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `this.childMap.set()`
- 条件付き依存: `if (subframeCrashItem)` → `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 条件付き依存: `if (subframeCrashItem)` → `subframeCrashItem.get()`
- 条件付き依存: `if (browser.isConnected && !browser.documentGlobal.closed)` → `this.showSubFrameNotification()`
- 条件付き依存: `if (!this.flushCrashedBrowserQueue(childID))` → `this.unseenCrashedChildIDs.push()`
- 条件付き依存: `if ( this.unseenCrashedChildIDs.length > MAX_UNSEEN_CRASHED_CHILD_IDS )` → `this.unseenCrashedChildIDs.shift()`
- 条件付き依存: `if (shutdown)` → `dump()`
- 条件付き依存: `if (shutdown)` → `Services.startup.quit()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `Ci.nsIAppStartup.eForceQuit`, `Ci.nsIPropertyBag2`, `aSubject.childID`, `aSubject.ownerElement`, `browser.documentGlobal.closed`, `browser.isConnected`, `this.unseenCrashedChildIDs.length`
- XPCOM: [`nsIAppStartup`](../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.env` / `Services.startup`

## flushCrashedBrowserQueue()
- 位置: L209-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.crashedBrowserQueues.delete()`, `this.crashedBrowserQueues.get()`, `weakBrowser.get()`
- 条件付き依存: `if (browser)` → `this.restartRequiredBrowsers.has()`
- 条件付き依存: `if ( this.restartRequiredBrowsers.has(browser) || this.testBuildIDMismatch )` → `this.sendToRestartRequiredPage()`
- 条件付き依存: `if (!( this.restartRequiredBrowsers.has(browser) || this.testBuildIDMismatch ))` → `this.sendToTabCrashedPage()`
- 参照: `this.testBuildIDMismatch`

## onSelectedBrowserCrash()
- 位置: L246-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `browserQueue.push()`, `this.crashedBrowserQueues.get()`
- 条件付き依存: `if (!browser.isRemoteBrowser)` → `console.error()`
- 条件付き依存: `if (!browser.frameLoader)` → `console.error()`
- 条件付き依存: `if (!browserQueue)` → `this.crashedBrowserQueues.set()`
- 条件付き依存: `if (restartRequired)` → `this.restartRequiredBrowsers.add()`
- 条件付き依存: `if (childID == 0)` → `this.flushCrashedBrowserQueue()`
- 参照: `browser.frameLoader`, `browser.frameLoader.childID`, `browser.isRemoteBrowser`

## onBackgroundBrowserCrash()
- 位置: L295-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `gBrowser.updateBrowserRemoteness()`, `lazy.SessionStore.reviveCrashedTab()`
- 条件付き依存: `if (restartRequired)` → `this.restartRequiredBrowsers.add()`
- 参照: `lazy.E10SUtils.NOT_REMOTE`

## onSubFrameCrash()
- 位置: async L319-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.childMap.get()`
- 条件付き依存: `if (dumpID)` → `this.showSubFrameNotification()`
- 条件付き依存: `if (!(dumpID))` → `this.pendingSubFrameCrashes.get()`
- 条件付き依存: `if (!item)` → `this.pendingSubFrameCrashes.set()`
- 条件付き依存: `if ( this.pendingSubFrameCrashesIDs.length >= MAX_UNSEEN_CRASHED_SUBFRAME_IDS )` → `this.pendingSubFrameCrashesIDs.shift()`
- 条件付き依存: `if ( this.pendingSubFrameCrashesIDs.length >= MAX_UNSEEN_CRASHED_SUBFRAME_IDS )` → `this.pendingSubFrameCrashes.delete()`
- 条件付き依存: `if (!item)` → `this.pendingSubFrameCrashesIDs.push()`
- 条件付き依存: `if (!(dumpID))` → `item.set()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `this.pendingSubFrameCrashesIDs.length`

## getAndRemoveSubframeCrash()
- 位置: L361-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pendingSubFrameCrashes.get()`
- 条件付き依存: `if (item)` → `this.pendingSubFrameCrashes.delete()`
- 条件付き依存: `if (item)` → `this.pendingSubFrameCrashesIDs.indexOf()`
- 条件付き依存: `if (idx >= 0)` → `this.pendingSubFrameCrashesIDs.splice()`

## showSubFrameNotification()
- 位置: async L385-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `gBrowser.documentGlobal.MozXULElement.insertFTLIfNeeded()`, `gBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.notificationsMap.get()`
- 条件付き依存: `if (existingItem)` → `existingItem.push()`
- 条件付き依存: `if (!(existingItem))` → `this.notificationsMap.set()`
- 参照: `notificationBox.PRIORITY_INFO_MEDIUM`

## closeAllNotifications()
- 位置: L396-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.notificationsMap.get()`
- 条件付き依存: `if (existingItem)` → `existingItem.slice()`
- 条件付き依存: `if (existingItem)` → `notif.close()`

## callback()
- 位置: async L420-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closeAllNotifications()`
- 条件付き依存: `if (dumpID)` → `UnsubmittedCrashHandler.submitReports()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_CRASH_TAB`

## eventCallback()
- 位置: L438-459
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (eventName == "disconnected")` → `this.notificationsMap.get()`
- 条件付き依存: `if (existingItem)` → `existingItem.indexOf()`
- 条件付き依存: `if (idx >= 0)` → `existingItem.splice()`
- 条件付き依存: `if (!existingItem.length)` → `this.notificationsMap.delete()`
- 条件付き依存: `if (dumpID)` → `lazy.CrashSubmit.ignore()`
- 条件付き依存: `if (dumpID)` → `this.childMap.delete()`
- 条件付き依存: `if (eventName == "dismissed")` → `closeAllNotifications()`
- 参照: `existingItem.length`

## willShowCrashedTab()
- 位置: L487-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserMap.get()`, `this.unseenCrashedChildIDs.includes()`
- 条件付き依存: `if (UnsubmittedCrashHandler.autoSubmit)` → `this.childMap.get()`
- 条件付き依存: `if (dumpID)` → `UnsubmittedCrashHandler.submitReports()`
- 条件付き依存: `if (!(UnsubmittedCrashHandler.autoSubmit))` → `this.sendToTabCrashedPage()`
- 条件付き依存: `if (childID === 0)` → `this.restartRequiredBrowsers.has()`
- 条件付き依存: `if (this.restartRequiredBrowsers.has(browser))` → `this.sendToRestartRequiredPage()`
- 条件付き依存: `if (!(this.restartRequiredBrowsers.has(browser)))` → `this.sendToTabCrashedPage()`
- 参照: `UnsubmittedCrashHandler.autoSubmit`, `lazy.CrashSubmit.SUBMITTED_FROM_AUTO`

## sendToRestartRequiredPage()
- 位置: L521-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.docShell.displayLoadError()`, `browser.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `gBrowser.updateBrowserRemoteness()`, `tab.setAttribute()`
- 参照: `Cr.NS_ERROR_BUILDID_MISMATCH`, `browser.currentURI`, `lazy.E10SUtils.NOT_REMOTE`

## sendToTabCrashedPage()
- 位置: L542-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.docShell.displayLoadError()`, `browser.getTabBrowser()`, `browser.removeAttribute()`, `browser.setAttribute()`, `gBrowser.getTabForBrowser()`, `gBrowser.updateBrowserRemoteness()`, `tab.setAttribute()`
- 参照: `Cr.NS_ERROR_CONTENT_CRASHED`, `browser.contentTitle`, `browser.currentURI`, `lazy.E10SUtils.NOT_REMOTE`

## maybeSendCrashReport()
- 位置: L579-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extraExtraKeyVals[key].trim()`, `lazy.CrashSubmit.submit()`, `this.browserMap.get()`, `this.childMap.get()`, `this.childMap.set()`, `this.prefs.setBoolPref()`, `this.removeSubmitCheckboxesForSameCrash()`
- 条件付き依存: `if (!message.data.sendReport)` → `Glean.browserContentCrash.notSubmitted.add()`
- 条件付き依存: `if (!message.data.sendReport)` → `this.prefs.setBoolPref()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `UnsubmittedCrashHandler.autoSubmit`, `console.error`, `extraExtraKeyVals.URL`, `lazy.CrashSubmit.SUBMITTED_FROM_CRASH_TAB`, `message.data`, `message.data.autoSubmit`, `message.data.hasReport`, `message.data.sendReport`

## removeSubmitCheckboxesForSameCrash()
- 位置: L643-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `doc.documentURI.startsWith()`, `this.browserMap.get()`
- 条件付き依存: `if (this.browserMap.get(browser) == childID)` → `this.browserMap.delete()`
- 条件付き依存: `if (this.browserMap.get(browser) == childID)` → `browser.sendMessageToActor()`
- 参照: `browser.contentDocument`, `browser.isRemoteBrowser`, `window.gBrowser.browsers`, `window.gMultiProcessBrowser`
- XPCOM: `Services.wm`

## onAboutTabCrashedLoad()
- 位置: L675-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserMap.get()`, `this.getDumpID()`, `this.prefs.getBoolPref()`, `this.unseenCrashedChildIDs.indexOf()`, `window.ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (index != -1)` → `this.unseenCrashedChildIDs.splice()`
- 参照: `UnsubmittedCrashHandler.autoSubmit`, `browser.documentGlobal`, `this._crashedTabCount`

## onAboutTabCrashedUnload()
- 位置: L710-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserMap.get()`
- 条件付き依存: `if (!this._crashedTabCount)` → `console.error()`
- 条件付き依存: `if (this._crashedTabCount == 0 && childID)` → `Glean.browserContentCrash.notSubmitted.add()`
- 参照: `this._crashedTabCount`

## getDumpID()
- 位置: L734-740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserMap.get()`, `this.childMap.get()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`

## queuedCrashedBrowsers()
- 位置: L753-755
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.crashedBrowserQueues.size`

## prefs()
- 位置: L766-771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBranch()`
- 参照: `this.prefs`
- XPCOM: `Services.prefs`

## enabled()
- 位置: L773-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.prefs.getBoolPref()`

## init()
- 位置: L792-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.createInstance()`, `lazy.RemoteSettingsCrashPull.start()`, `this.prefs.getStringPref()`, `this.showRequestedSubmissionsNotification.bind()`
- 条件付き依存: `if (this.enabled)` → `this.prefs.prefHasUserValue()`
- 条件付き依存: `if (this.prefs.prefHasUserValue("suppressUntilDate"))` → `this.prefs.getCharPref()`
- 条件付き依存: `if (this.prefs.prefHasUserValue("suppressUntilDate"))` → `this.dateString()`
- 条件付き依存: `if (this.prefs.getCharPref("suppressUntilDate") > this.dateString())` → `this.log.debug()`
- 条件付き依存: `if (this.prefs.prefHasUserValue("suppressUntilDate"))` → `this.prefs.clearUserPref()`
- 条件付き依存: `if (this.enabled)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(this.enabled))` → `this.log.debug()`
- 参照: `this.enabled`, `this.initialized`, `this.log`, `this.suppressed`
- XPCOM: `Services.obs`

## uninit()
- 位置: L833-865
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.RemoteSettingsCrashPull.stop()`
- 条件付き依存: `if (this._checkTimeout)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this.showingNotification)` → `this.prefs.setBoolPref()`
- 参照: `this._checkTimeout`, `this.enabled`, `this.initialized`, `this.log`, `this.showingNotification`, `this.suppressed`
- XPCOM: `Services.obs`

## observe()
- 位置: L867-874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.uninit()`

## scheduleCheckForUnsubmittedCrashReports()
- 位置: L876-882
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy.setTimeout()`, `this.checkForUnsubmittedCrashReports()`
- 参照: `this._checkTimeout`
- XPCOM: `Services.tm`

## checkForUnsubmittedCrashReports()
- 位置: async L895-924
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dateLimit.getDate()`, `dateLimit.setDate()`, `lazy.CrashSubmit.pendingIDs()`, `this.log.debug()`, `this.log.error()`
- 条件付き依存: `if (reportIDs.length)` → `this.log.debug()`
- 条件付き依存: `if (reportIDs.length)` → `Glean.crashSubmission.pending.add()`
- 条件付き依存: `if (this.autoSubmit)` → `this.log.debug()`
- 条件付き依存: `if (this.autoSubmit)` → `this.submitReports()`
- 条件付き依存: `if (!(this.autoSubmit))` → `this.shouldShowPendingSubmissionsNotification()`
- 条件付き依存: `if (this.shouldShowPendingSubmissionsNotification())` → `this.showPendingSubmissionsNotification()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_AUTO`, `reportIDs.length`, `this.autoSubmit`, `this.enabled`, `this.suppressed`

## shouldShowPendingSubmissionsNotification()
- 位置: L936-978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dateString()`, `this.prefs.clearUserPref()`, `this.prefs.getBoolPref()`, `this.prefs.getCharPref()`, `this.prefs.prefHasUserValue()`
- 条件付き依存: `if (this.dateString() > lastShownDate && shutdownWhileShowing)` → `this.prefs.getIntPref()`
- 条件付き依存: `if (--chances < 0)` → `this.prefs.clearUserPref()`
- 条件付き依存: `if (--chances < 0)` → `this.dateString()`
- 条件付き依存: `if (--chances < 0)` → `Date.now()`
- 条件付き依存: `if (--chances < 0)` → `this.prefs.setCharPref()`
- 条件付き依存: `if (this.dateString() > lastShownDate && shutdownWhileShowing)` → `this.prefs.setIntPref()`
- 参照: `this._requestedSubmission.notification`

## showPendingSubmissionsNotification()
- 位置: async L988-1009
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.log.debug()`, `this.show()`
- 条件付き依存: `if (notification)` → `this.prefs.setCharPref()`
- 条件付き依存: `if (notification)` → `this.dateString()`
- 参照: `reportIDs.length`, `this.showingNotification`

## onAction()
- 位置: L998-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.showingNotification`

## removeExistingNotification()
- 位置: L1011-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNotification)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (aNotification)` → `chromeWin.gNotificationBox.removeNotification()`

## showRequestedSubmissionsNotification()
- 位置: async L1039-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.trunc()`, `Services.prefs.getIntPref()`, `this._requestedSubmission.reportIDs.push()`, `this.log.debug()`, `this.removeExistingNotification()`, `this.show()`
- 参照: `newReportIDs.length`, `this._requestedSubmission.notification`, `this._requestedSubmission.reportIDs`
- XPCOM: `Services.prefs`

## onAction()
- 位置: L1064-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`
- 参照: `this._requestedSubmission.notification`, `this._requestedSubmission.reportIDs`
- XPCOM: `Services.prefs`

## dateString()
- 位置: L1087-1092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(someDate.getDate()).padStart()`, `String(someDate.getFullYear()).padStart()`, `String(someDate.getMonth() + 1).padStart()`, `someDate.getDate()`, `someDate.getFullYear()`, `someDate.getMonth()`

## show()
- 位置: L1128-1235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttons.push()`, `chromeWin.MozXULElement.insertFTLIfNeeded()`, `chromeWin.gNotificationBox.appendNotification()`, `chromeWin.gNotificationBox.getNotificationWithValue()`, `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (requestedByDevs)` → `buttons.push()`
- 条件付き依存: `if (!requestedByDevs)` → `buttons.push()`
- 条件付き依存: `if (!(!requestedByDevs))` → `buttons.push()`
- 参照: `chromeWin.gNotificationBox.PRIORITY_INFO_HIGH`, `reportIDs.length`

## callback()
- 位置: L1149-1158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.submitReports()`
- 条件付き依存: `if (onAction)` → `onAction()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_INFOBAR`

## callback()
- 位置: L1162-1168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.submitReports()`
- 条件付き依存: `if (onAction)` → `onAction()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_INFOBAR`, `this.autoSubmit`

## callback()
- 位置: L1172-1175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeWin.openTrustedLinkIn()`

## callback()
- 位置: L1183-1188
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (onAction)` → `onAction()`
- 参照: `this.requestedNeverShowAgain`

## eventCallback()
- 位置: L1205-1218
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (eventType == "dismissed")` → `reportIDs.forEach()`
- 条件付き依存: `if (eventType == "dismissed")` → `lazy.CrashSubmit.ignore()`
- 条件付き依存: `if (onAction)` → `onAction()`

## autoSubmit()
- 位置: L1237-1241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## autoSubmit()
- 位置: L1243-1248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## requestedNeverShowAgain()
- 位置: L1250-1255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## submitReports()
- 位置: L1268-1280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CrashSubmit.submit()`, `lazy.CrashSubmit.submit(reportID, submittedFrom, params).catch()`, `this.log.debug()`, `this.log.error.bind()`
- 参照: `reportIDs.length`, `this.log`

## enabled()
- 位置: L1297-1299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cleanerPrefs.getBoolPref()`

## init()
- 位置: L1303-1313
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.enabled)` → `lazy.cleanerLog.debug()`
- 参照: `this.enabled`, `this.initialized`

## uninit()
- 位置: L1315-1326
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._checkTimeout)` → `lazy.clearTimeout()`
- 参照: `this._checkTimeout`, `this.initialized`

## scheduleCleanup()
- 位置: L1328-1334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy.setTimeout()`, `this.runCleanup()`
- 参照: `this._checkTimeout`
- XPCOM: `Services.tm`

## _ranRecently()
- 位置: L1336-1345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Date.parse()`, `isNaN()`, `lazy.cleanerPrefs.getCharPref()`, `lazy.cleanerPrefs.prefHasUserValue()`

## pruneInstallTimeMarkers()
- 位置: async L1347-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CrashReports.pruneInstallTimeFiles()`

## pruneOldReports()
- 位置: async L1351-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.CrashReports.getReports()`
- 条件付き依存: `if (report.pending)` → `lazy.CrashReports.deletePendingReport()`
- 条件付き依存: `if (!(report.pending))` → `lazy.CrashReports.deleteSubmittedReport()`
- 参照: `report.date`, `report.id`, `report.pending`

## enforcePendingCap()
- 位置: async L1367-1375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CrashReports.deletePendingReport()`, `lazy.CrashReports.getReports()`, `lazy.CrashReports.getReports().filter()`, `pending.slice()`
- 参照: `pending.length`, `r.pending`, `report.id`

## runCleanup()
- 位置: async L1377-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.cleanerLog.debug()`, `lazy.cleanerLog.error()`, `lazy.cleanerPrefs.setCharPref()`, `new Date().toISOString()`, `this._ranRecently()`, `this.enforcePendingCap()`, `this.pruneInstallTimeMarkers()`, `this.pruneOldReports()`
- 条件付き依存: `if (this._ranRecently())` → `lazy.cleanerLog.debug()`
- 参照: `this.enabled`
