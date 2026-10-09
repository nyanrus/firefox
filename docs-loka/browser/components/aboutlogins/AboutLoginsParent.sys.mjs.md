# browser/components/aboutlogins/AboutLoginsParent.sys.mjs

source: browser/components/aboutlogins/AboutLoginsParent.sys.mjs
source-hash: 4021fadcc30686d93f331fe43d350162a6755eda
lines: 901

## <module>
- 役割: (未記入)
- 呼び出し先: `AboutLogins.onPasswordSyncEnabledPreferenceChange.bind()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.LoginHelper.createLogger()`

## convertSubjectToLogin()
- 位置: L61-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `augmentVanillaLoginObject()`, `lazy.LoginHelper.isUserFacingLogin()`, `lazy.LoginHelper.loginToVanillaObject()`, `subject.QueryInterface()`, `subject.QueryInterface(Ci.nsILoginMetaInfo).QueryInterface()`
- 参照: `Ci.nsILoginInfo`, `Ci.nsILoginMetaInfo`
- XPCOM: [`nsILoginInfo`](../../../toolkit/components/passwordmgr/nsILoginInfo.idl.md) / [`nsILoginMetaInfo`](../../../toolkit/components/passwordmgr/nsILoginMetaInfo.idl.md)

## augmentVanillaLoginObject()
- 位置: L71-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `login.displayOrigin.replace()`

## AboutLoginsParent.receiveMessage()
- 位置: async L85-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutLogins.subscribers.add()`, `this.#createLogin()`, `this.#deleteLogin()`, `this.#exportPasswords()`, `this.#getHelp()`, `this.#importFromBrowser()`, `this.#importFromFile()`, `this.#importReportInit()`, `this.#openPreferences()`, `this.#primaryPasswordRequest()`, `this.#removeAllLogins()`, `this.#sortChanged()`, `this.#subscribe()`, `this.#syncEnable()`, `this.#updateLogin()`
- 参照: `message.data`, `message.data.login`, `message.data.messageId`, `message.data.reason`, `message.name`, `this.browsingContext`, `this.browsingContext.embedderElement`, `this.manager.remoteType`

## AboutLoginsParent.#documentGlobal()
- 位置: L164-166
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.browsingContext.embedderElement?.documentGlobal`

## AboutLoginsParent.#createLogin()
- 位置: async L168-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Services.logins.addLoginAsync()`, `Services.policies.isAllowed()`, `lazy.LoginHelper.getLoginOrigin()`, `lazy.LoginHelper.vanillaObjectToLogin()`, `this.#handleLoginStorageErrors()`
- 条件付き依存: `if (!Services.policies.isAllowed("removeMasterPassword"))` → `lazy.LoginHelper.isPrimaryPasswordSet()`
- 条件付き依存: `if (!lazy.LoginHelper.isPrimaryPasswordSet())` → `this.#documentGlobal.openDialog()`
- 条件付き依存: `if (!lazy.LoginHelper.isPrimaryPasswordSet())` → `lazy.LoginHelper.isPrimaryPasswordSet()`
- 条件付き依存: `if (!origin)` → `console.error()`
- 参照: `newLogin.origin`
- XPCOM: `Services.logins` / `Services.policies`

## AboutLoginsParent.preselectedLogin()
- 位置: L203-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#documentGlobal?.gBrowser.selectedTab.getAttribute()`, `this.#documentGlobal?.gBrowser.selectedTab.removeAttribute()`
- 参照: `this.browsingContext.currentURI?.ref`

## AboutLoginsParent.#deleteLogin()
- 位置: async L214-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.removeLoginAsync()`, `lazy.LoginHelper.vanillaObjectToLogin()`
- XPCOM: `Services.logins`

## AboutLoginsParent.#sortChanged()
- 位置: L219-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setCharPref()`
- XPCOM: `Services.prefs`

## AboutLoginsParent.#syncEnable()
- 位置: L223-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#documentGlobal.gSync.openFxAEmailFirstPage()`

## AboutLoginsParent.#importFromBrowser()
- 位置: L227-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MigrationUtils.showMigrationWizard()`
- 参照: `lazy.MigrationUtils.MIGRATION_ENTRYPOINTS.PASSWORDS`, `this.#documentGlobal`

## AboutLoginsParent.#importReportInit()
- 位置: L237-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `lazy.LoginCSVImport.lastImportReport`

## AboutLoginsParent.#getHelp()
- 位置: L242-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `this.#documentGlobal.openWebLinkIn()`
- XPCOM: `Services.urlFormatter`

## AboutLoginsParent.#openPreferences()
- 位置: L251-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#documentGlobal.openPreferences()`

## AboutLoginsParent.#primaryPasswordRequest()
- 位置: async L255-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.getOSAuthEnabled()`, `lazy.LoginHelper.requestReauth()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (isOSAuthEnabled)` → `lazy.AboutLoginsL10n.formatMessages()`
- 条件付き依存: `if (isAuthorized)` → `Date.now()`
- 条件付き依存: `if (isAuthorized)` → `clearTimeout()`
- 条件付き依存: `if (isAuthorized)` → `setTimeout()`
- 参照: `AboutLogins._authExpirationTime`, `AppConstants.platform`, `captionText.value`, `messageText.value`, `this.browsingContext.embedderElement`

## remaskPasswords()
- 位置: L293-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AboutLoginsParent.#subscribe()
- 位置: async L301-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutLogins.addObservers()`, `AboutLogins.getAllLogins()`, `AboutLogins.getSyncState()`, `AboutLogins.sendAllLoginRelatedObjects()`, `Services.policies.isAllowed()`, `Services.prefs.getCharPref()`, `lazy.LoginHelper.isPrimaryPasswordSet()`, `lazy.log.debug()`, `this.sendAsyncMessage()`
- 参照: `AboutLogins._authExpirationTime`, `AppConstants.platform`, `Cr.NS_ERROR_NOT_INITIALIZED`, `Number.NEGATIVE_INFINITY`, `ex.result`, `this.browsingContext`, `this.preselectedLogin`
- XPCOM: `Services.policies` / `Services.prefs`

## AboutLoginsParent.#updateLogin()
- 位置: async L347-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.modifyLoginAsync()`, `Services.logins.searchLoginsAsync()`, `loginUpdates.hasOwnProperty()`, `logins[0].clone()`, `this.#handleLoginStorageErrors()`
- 条件付き依存: `if (logins.length != 1)` → `lazy.log.warn()`
- 参照: `loginUpdates.guid`, `loginUpdates.password`, `loginUpdates.username`, `logins.length`, `modifiedLogin.password`, `modifiedLogin.username`
- XPCOM: `Services.logins`

## AboutLoginsParent.#exportPasswords()
- 位置: async L372-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `lazy.AboutLoginsL10n.formatValues()`, `lazy.LoginHelper.getOSAuthEnabled()`, `lazy.LoginHelper.recordReauthTelemetryEvent()`, `lazy.LoginHelper.requestReauth()`
- 条件付き依存: `if (isOSAuthEnabled)` → `lazy.AboutLoginsL10n.formatMessages()`
- 条件付き依存: `if (!this.browsingContext.canOpenModalPicker)` → `this.sendQuery()`
- 参照: `AppConstants.platform`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeSave`, `captionText.value`, `fp.defaultExtension`, `fp.defaultString`, `fp.okButtonLabel`, `messageText.value`, `this.browsingContext`, `this.browsingContext.canOpenModalPicker`, `this.browsingContext.embedderElement`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## fpCallback()
- 位置: L423-428
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `lazy.LoginExport.exportAsCSV()`
- 条件付き依存: `if (aResult != Ci.nsIFilePicker.returnCancel)` → `Glean.pwmgr.mgmtMenuItemUsedExportComplete.record()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `fp.file.path`
- XPCOM: `nsIFilePicker`

## AboutLoginsParent.#importFromFile()
- 位置: async L454-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutLoginsL10n.formatValues()`, `this.openFilePickerDialog()`
- 条件付き依存: `if (result != Ci.nsIFilePicker.returnCancel)` → `lazy.LoginCSVImport.importFromCSV()`
- 条件付き依存: `if (result != Ci.nsIFilePicker.returnCancel)` → `console.error()`
- 条件付き依存: `if (result != Ci.nsIFilePicker.returnCancel)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (summary)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (summary)` → `Glean.pwmgr.mgmtMenuItemUsedImportCsvComplete.record()`
- 参照: `Ci.nsIFilePicker.returnCancel`, `e.errorType`
- XPCOM: `nsIFilePicker`

## AboutLoginsParent.#removeAllLogins()
- 位置: async L503-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.removeAllUserFacingLoginsAsync()`
- XPCOM: `Services.logins`

## AboutLoginsParent.#handleLoginStorageErrors()
- 位置: L507-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `augmentVanillaLoginObject()`, `error.message.includes()`, `lazy.LoginHelper.loginToVanillaObject()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (error.message.includes("This login already exists"))` → `error.data.toString()`
- 参照: `error.message`, `messageObject.existingLoginGuid`

## AboutLoginsParent.openFilePickerDialog()
- 位置: async L524-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `fp.appendFilter()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`, `resolve()`
- 参照: `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterAll`, `Ci.nsIFilePicker.modeOpen`, `appendFilter.extensionPattern`, `appendFilter.title`, `fp.file.path`, `fp.okButtonLabel`, `this.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## AboutLoginsInternal.observe()
- 位置: async L546-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `this.#addLogin()`, `this.#messageSubscribers()`, `this.#modifyLogin()`, `this.#reloadAllLogins()`, `this.#removeAllLogins()`, `this.#removeLogin()`, `this.#removeNotifications()`, `this.#showPrimaryPasswordLoginNotifications()`, `this.getSyncState()`
- 条件付き依存: `if (!ChromeUtils.nondeterministicGetWeakSetKeys(this.subscribers).length)` → `this.#removeObservers()`
- 参照: `ChromeUtils.nondeterministicGetWeakSetKeys(this.subscribers).length`, `lazy.UIState.ON_UPDATE`, `this.subscribers`

## AboutLoginsInternal.#addLogin()
- 位置: async L596-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `convertSubjectToLogin()`, `lazy.ChangePasswordURLs.getChangePasswordURLsByLoginGUID()`, `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `lazy.LoginBreaches.getPotentiallyVulnerablePasswordsByLoginGUID()`
- 参照: `lazy.BREACH_ALERTS_ENABLED`, `lazy.VULNERABLE_PASSWORDS_ENABLED`

## AboutLoginsInternal.#modifyLogin()
- 位置: async L623-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `convertSubjectToLogin()`, `lazy.ChangePasswordURLs.getChangePasswordURLsByLoginGUID()`, `subject.GetElementAt()`, `subject.QueryInterface()`, `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `breachesForThisLogin.get()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `this.#messageSubscribers()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `lazy.LoginBreaches.getPotentiallyVulnerablePasswordsByLoginGUID()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `this.#messageSubscribers()`
- 参照: `Ci.nsIArrayExtensions`, `breachesForThisLogin.size`, `lazy.BREACH_ALERTS_ENABLED`, `lazy.VULNERABLE_PASSWORDS_ENABLED`, `login.guid`, `vulnerablePasswordsForThisLogin.size`
- XPCOM: [`nsIArrayExtensions`](../../../xpcom/ds/nsIArrayExtensions.idl.md)

## AboutLoginsInternal.#removeLogin()
- 位置: L659-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `convertSubjectToLogin()`, `this.#messageSubscribers()`

## AboutLoginsInternal.#removeAllLogins()
- 位置: async L667-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messageSubscribers()`

## AboutLoginsInternal.#reloadAllLogins()
- 位置: async L671-675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messageSubscribers()`, `this.getAllLogins()`, `this.sendAllLoginRelatedObjects()`

## AboutLoginsInternal.#showPrimaryPasswordLoginNotifications()
- 位置: L677-691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messageSubscribers()`, `this.#showNotifications()`

## onReloadClick()
- 位置: L685-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.reload()`

## AboutLoginsInternal.#showNotifications()
- 位置: L693-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.insertFTLIfNeeded()`, `gBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.#subscriberIterator()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.MozXULElement`, `buttonIds.length`, `subscriber.embedderElement`

## callback()
- 位置: L723-725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onClicks[i]()`

## AboutLoginsInternal.#removeNotifications()
- 位置: L741-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getNotificationBox()`, `notificationBox.getNotificationWithValue()`, `notificationBox.removeNotification()`, `this.#subscriberIterator()`
- 参照: `browser.documentGlobal`, `subscriber.embedderElement`

## AboutLoginsInternal.#subscriberIterator()
- 位置: L755-770
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`
- 条件付き依存: `if ( browser?.remoteType != EXPECTED_ABOUTLOGINS_REMOTE_TYPE || browser?.contentPrincipal?.originNoSuffix != ABOUT_LOGINS_ORIGIN )` → `this.subscribers.delete()`
- 参照: `browser?.contentPrincipal?.originNoSuffix`, `browser?.remoteType`, `subscriber.embedderElement`, `this.subscribers`

## AboutLoginsInternal.#messageSubscribers()
- 位置: L772-791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#subscriberIterator()`
- 条件付き依存: `if (subscriber.currentWindowGlobal)` → `subscriber.currentWindowGlobal.getActor()`
- 条件付き依存: `if (subscriber.currentWindowGlobal)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (ex.result == Cr.NS_ERROR_NOT_INITIALIZED)` → `lazy.log.debug()`
- 参照: `Cr.NS_ERROR_NOT_INITIALIZED`, `ex.result`, `subscriber.currentWindowGlobal`

## AboutLoginsInternal.getAllLogins()
- 位置: async L793-806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.getAllUserFacingLogins()`, `logins .map()`, `logins .map(lazy.LoginHelper.loginToVanillaObject) .map()`
- 参照: `Cr.NS_ERROR_ABORT`, `e.result`, `lazy.LoginHelper.loginToVanillaObject`

## AboutLoginsInternal.sendAllLoginRelatedObjects()
- 位置: async L808-837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ChangePasswordURLs.getChangePasswordURLsByLoginGUID()`, `sendMessageFn()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `sendMessageFn()`
- 条件付き依存: `if (lazy.BREACH_ALERTS_ENABLED)` → `lazy.LoginBreaches.getPotentialBreachesByLoginGUID()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `sendMessageFn()`
- 条件付き依存: `if (lazy.VULNERABLE_PASSWORDS_ENABLED)` → `lazy.LoginBreaches.getPotentiallyVulnerablePasswordsByLoginGUID()`
- 参照: `lazy.BREACH_ALERTS_ENABLED`, `lazy.VULNERABLE_PASSWORDS_ENABLED`

## sendMessageFn()
- 位置: L809-816
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (browsingContext?.currentWindowGlobal)` → `browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (browsingContext?.currentWindowGlobal)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (!(browsingContext?.currentWindowGlobal))` → `this.#messageSubscribers()`
- 参照: `browsingContext?.currentWindowGlobal`

## AboutLoginsInternal.getSyncState()
- 位置: async L839-857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FxAccounts.config.promiseManageURI()`, `lazy.UIState.get()`
- 参照: `lazy.FXA_ENABLED`, `lazy.PASSWORD_SYNC_ENABLED`, `lazy.UIState.STATUS_NOT_CONFIGURED`, `state.avatarURL`, `state.email`, `state.status`, `state.syncEnabled`

## AboutLoginsInternal.onPasswordSyncEnabledPreferenceChange()
- 位置: async L859-864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messageSubscribers()`, `this.getSyncState()`

## AboutLoginsInternal.addObservers()
- 位置: L874-881
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#observersAdded)` → `Services.obs.addObserver()`
- 参照: `this.#observedTopics`, `this.#observersAdded`
- XPCOM: `Services.obs`

## AboutLoginsInternal.#removeObservers()
- 位置: L883-888
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.#observedTopics`, `this.#observersAdded`
- XPCOM: `Services.obs`
