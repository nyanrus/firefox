# browser/components/preferences/config/account-sync.mjs

source: browser/components/preferences/config/account-sync.mjs
source-hash: 664a7dcca3cecad27da88897c57255208532460e
lines: 1178

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SYNC_ENGINE_SETTINGS.forEach()`, `SYNC_ENGINE_SETTINGS.map()`, `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`, `document.addEventListener()`, `window.addEventListener()`, `window.createDefaultBrowserConfig()`

## SyncHelpers.uiState()
- 位置: L68-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.UIState.get()`

## SyncHelpers.uiStateStatus()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.uiState.status`

## SyncHelpers.isSyncEnabled()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.uiState.syncEnabled`

## SyncHelpers.getEntryPoint()
- 位置: L98-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.fromURI()`, `entryPoint.replace()`, `params.get()`
- 参照: `URL.fromURI(document.documentURIObject).searchParams`, `document.documentURIObject`

## SyncHelpers.replaceTabWithUrl()
- 位置: L110-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createNullPrincipal()`, `browser.loadURI()`
- 参照: `window.docShell.chromeEventHandler`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## SyncHelpers._chooseWhatToSync()
- 位置: async L131-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `window.fxAccounts.telemetry.recordOpenCWTSMenu()`, `window.fxAccounts.telemetry.recordOpenCWTSMenu(why).catch()`, `window.gSubDialog.open()`
- 条件付き依存: `if (!isSyncConfigured)` → `lazy.Weave.Service.updateLocalEnginesState()`
- 条件付き依存: `if (!isSyncConfigured)` → `console.error()`
- 参照: `params.disconnectFun`

## params.disconnectFun()
- 位置: L150-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.disconnectSync()`

## closingCallback()
- 位置: L155-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.history.replaceState()`
- 条件付き依存: `if (!isSyncConfigured)` → `window.fxAccounts.telemetry .recordConnection(["sync"], "ui") .then()`
- 条件付き依存: `if (!isSyncConfigured)` → `window.fxAccounts.telemetry .recordConnection()`
- 条件付き依存: `if (!isSyncConfigured)` → `lazy.Weave.Service.configure()`
- 条件付き依存: `if (!isSyncConfigured)` → `console.error()`
- 条件付き依存: `if (!(!isSyncConfigured))` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (!(!isSyncConfigured))` → `lazy.Weave.Service.queueSync()`
- 参照: `document.title`, `event.detail.button`, `history.state`, `location.href`, `url.href`, `url.search`
- XPCOM: `Services.tm`

## SyncHelpers.disconnectSync()
- 位置: L191-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.browsingContext.topChromeWindow.gSync.disconnect()`

## SyncHelpers.setupSync()
- 位置: async L198-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._chooseWhatToSync()`, `window.fxAccounts.keys.hasKeysForScope()`
- 条件付き依存: `if (hasKeys)` → `this._chooseWhatToSync()`
- 条件付き依存: `if (!(hasKeys))` → `window.FxAccounts.canConnectAccount()`
- 条件付き依存: `if (!(hasKeys))` → `window.FxAccounts.config.promiseConnectAccountURI()`
- 条件付き依存: `if (!(hasKeys))` → `this.getEntryPoint()`
- 条件付き依存: `if (!(hasKeys))` → `this.replaceTabWithUrl()`

## SyncHelpers.signIn()
- 位置: async L226-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getEntryPoint()`, `this.replaceTabWithUrl()`, `window.FxAccounts.canConnectAccount()`, `window.FxAccounts.config.promiseConnectAccountURI()`

## SyncHelpers.reSignIn()
- 位置: async L245-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.replaceTabWithUrl()`, `window.FxAccounts.config.promiseConnectAccountURI()`

## SyncHelpers.verifyFirefoxAccount()
- 位置: async L253-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.reSignIn()`

## SyncHelpers.unlinkFirefoxAccount()
- 位置: L263-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.browsingContext.topChromeWindow.gSync.disconnect()`

## SyncHelpers.maybeShowSyncAction()
- 位置: L271-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.UIState.get()`
- 条件付き依存: `if ( location.hash == "#sync" && window.UIState.get().status == window.UIState.STATUS_SIGNED_IN )` → `location.href.includes()`
- 条件付き依存: `if (location.href.includes("action=pair"))` → `window.gSubDialog.open()`
- 条件付き依存: `if (!(location.href.includes("action=pair")))` → `location.href.includes()`
- 条件付き依存: `if (location.href.includes("action=choose-what-to-sync"))` → `this._chooseWhatToSync()`
- 参照: `location.hash`, `this.isSyncEnabled`, `window.UIState.STATUS_SIGNED_IN`, `window.UIState.get().status`

## setup()
- 位置: L304-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Weave.Svc.Obs.add()`, `lazy.Weave.Svc.Obs.remove()`
- 参照: `window.UIState.ON_UPDATE`

## visible()
- 位置: L322-324
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_NOT_CONFIGURED`

## onUserClick()
- 位置: L331-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.signIn()`

## visible()
- 位置: L340-342
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_SIGNED_IN`

## getControlConfig()
- 位置: L348-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._failedAvatarURLs.has()`
- 参照: `SyncHelpers.uiState`, `config.iconSrc`, `config.l10nArgs`, `config.l10nId`, `img.onerror`, `img.src`, `state.avatarIsDefault`, `state.avatarURL`, `state.displayName`, `state.email`

## img.onerror()
- 位置: L373-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setting.onChange()`, `this._failedAvatarURLs.add()`
- 参照: `state.avatarURL`

## setup()
- 位置: L386-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Weave.Svc.Obs.add()`, `lazy.Weave.Svc.Obs.remove()`
- 参照: `this.emitChange`, `window.UIState.ON_UPDATE`

## getControlConfig()
- 位置: async L394-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.getEntryPoint()`, `window.FxAccounts.config.promiseManageURI()`

## onUserClick()
- 位置: L409-411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.unlinkFirefoxAccount()`

## visible()
- 位置: L418-420
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_NOT_VERIFIED`

## getControlConfig()
- 位置: L425-431
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiState`, `config.l10nArgs`, `state.email`

## onUserClick()
- 位置: L435-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.verifyFirefoxAccount()`

## onUserClick()
- 位置: L441-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.unlinkFirefoxAccount()`

## visible()
- 位置: L451-453
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_LOGIN_FAILED`

## getControlConfig()
- 位置: L458-464
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiState`, `config.l10nArgs`, `state.email`

## onUserClick()
- 位置: L468-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.getEntryPoint()`, `SyncHelpers.reSignIn()`

## onUserClick()
- 位置: L474-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.unlinkFirefoxAccount()`

## visible()
- 位置: L485-487
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_NOT_CONFIGURED`

## onUserClick()
- 位置: L488-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.signIn()`

## visible()
- 位置: L497-502
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.isSyncEnabled`, `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_SIGNED_IN`

## onUserClick()
- 位置: L506-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.setupSync()`

## visible()
- 位置: L513-518
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.isSyncEnabled`, `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_SIGNED_IN`

## onUserClick()
- 位置: L527-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Weave.Service.sync()`

## visible()
- 位置: L530-530
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiState.syncing`

## disabled()
- 位置: L536-536
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiState.syncing`

## visible()
- 位置: L537-537
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiState.syncing`

## get()
- 位置: L574-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SYNC_ENGINE_SETTINGS.filter()`, `SYNC_ENGINE_SETTINGS.filter(({ id }) => deps[id]?.value).map()`
- 参照: `deps[id]?.value`

## getControlConfig()
- 位置: L584-592
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `config.controlAttrs`, `syncEngines.value`

## onUserClick()
- 位置: L598-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers._chooseWhatToSync()`

## visible()
- 位置: L601-603
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `syncEngines.value`, `syncEngines.value.length`

## onUserClick()
- 位置: L608-610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.disconnectSync()`

## visible()
- 位置: L617-619
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_NOT_CONFIGURED`

## get()
- 位置: L627-629
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.Weave.Service.clientsEngine?.localName`

## set()
- 位置: L630-632
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.Weave.Service.clientsEngine.localName`

## disabled()
- 位置: L633-635
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.uiStateStatus`, `window.UIState.STATUS_SIGNED_IN`

## getControlConfig()
- 位置: L636-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.fxAccounts?.device?.getDefaultLocalName()`
- 参照: `config.controlAttrs`, `config.controlAttrs?.defaultvalue`

## getControlConfig()
- 位置: L656-667
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SyncHelpers.connectAnotherDeviceHref`, `config.controlAttrs`

## setup()
- 位置: L668-675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers.getEntryPoint()`, `emitChange()`, `window.FxAccounts.config .promiseConnectDeviceURI()`, `window.FxAccounts.config .promiseConnectDeviceURI("sync", SyncHelpers.getEntryPoint()) .then()`
- 参照: `SyncHelpers.connectAnotherDeviceHref`

## visible()
- 位置: L682-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- 参照: `Services.policies`
- XPCOM: `Services.policies`

## onUserClick()
- 位置: L684-686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gMainPane.showMigrationWizardDialog()`

## onUserClick()
- 位置: L693-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## visible()
- 位置: L700-702
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SelectableProfileService.isEnabled`

## onUserClick()
- 位置: L703-706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## onUserClick()
- 位置: L710-714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gMainPane.manageProfiles()`

## disabled()
- 位置: L719-719
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `copyProfileSelect.value`

## onUserClick()
- 位置: L720-728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `copyProfileSelect.config.set()`, `e.preventDefault()`, `lazy.SelectableProfileService.getProfile()`, `lazy.SelectableProfileService.getProfile(copyProfileSelect.value).then()`, `profile?.copyProfile()`
- 参照: `copyProfileSelect.value`

## visible()
- 位置: L732-732
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SelectableProfileService.initialized`

## setup()
- 位置: L737-739
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.emitChange`

## visible()
- 位置: L740-742
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._hasError`

## setError()
- 位置: L743-746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emitChange()`
- 参照: `this._hasError`

## ProfileList.setup()
- 位置: L752-763
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `ProfileList.PROFILE_UPDATED_OBS`, `this.emitChange`
- XPCOM: `Services.obs`

## ProfileList.get()
- 位置: async L765-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SelectableProfileService.getAllProfiles()`

## setup()
- 位置: L775-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n .formatValue()`, `document.l10n .formatValue("preferences-copy-profile-select") .then()`
- 参照: `this.emitChange`, `this.placeholderString`

## get()
- 位置: L781-783
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._selectedProfile`

## set()
- 位置: L784-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emitChange()`
- 参照: `this._selectedProfile`

## getControlConfig()
- 位置: L788-800
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.options.unshift()`, `profileList.value.map()`
- 参照: `config.options`, `profile.id`, `profile.name`, `this.placeholderString`

## visible()
- 位置: L804-804
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SelectableProfileService.initialized`

## setup()
- 位置: L811-815
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## visible()
- 位置: L816-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BackupService.init()`
- 参照: `bs.archiveEnabledStatus.enabled`, `bs.restoreEnabledStatus.enabled`

## setup()
- 位置: L825-827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Referrals.getReferralCode()`

## visible()
- 位置: L828-830
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Referrals.isEnabled`

## onUserClick()
- 位置: L831-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Referrals.openReferralsTab()`
