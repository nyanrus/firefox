# browser/components/firefoxview/firefox-view-tabs-setup-manager.sys.mjs

source: browser/components/firefoxview/firefox-view-tabs-setup-manager.sys.mjs
source-hash: 92430e0ca549885fff841c977cf49cbc8a26c863
lines: 635

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`

## openTabInWindow()
- 位置: L46-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `documentGlobal?.switchToTabHavingURI()`
- 参照: `window.docShell?.chromeEventHandler?.documentGlobal`

## constructor()
- 位置: L53-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.obs.addObserver()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.UIState.get()`, `this.logger.debug()`, `this.maybeUpdateUI()`, `this.onSignedInChange()`, `this.registerSetupState()`, `this.resetInternalState()`
- 参照: `lazy.UIState.ON_UPDATE`, `lazy.UIState.get().syncEnabled`, `this.QueryInterface`, `this._currentSetupStateName`, `this._lastFxASignedIn`, `this.didFxaTabOpen`, `this.fxaSignedIn`, `this.setupState`, `this.syncIsConnected`
- XPCOM: `Services.obs`

## exitConditions()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabsErrorHandler.isSyncReady()`

## exitConditions()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.fxaSignedIn`

## exitConditions()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.secondaryDeviceConnected`

## exitConditions()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.syncTabsPrefEnabled`

## exitConditions()
- 位置: L93-96
- 役割: (未記入)
- 触るとき: (未記入)

## resetInternalState()
- 位置: L128-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this.abortWaitingForTabs()`
- 参照: `this._currentSetupStateName`, `this._deviceStateSnapshot`, `this._didShowMobilePromo`, `this._lastFxASignedIn`, `this._shouldShowSuccessConfirmation`, `this._viewVisibilityStates`, `this.mobileDeviceConnected`, `this.secondaryDeviceConnected`
- XPCOM: `Services.obs`

## isPrimaryPasswordLocked()
- 位置: L147-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.syncUtils.mpLocked()`

## uninit()
- 位置: L151-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `lazy.UIState.ON_UPDATE`
- XPCOM: `Services.obs`

## hasVisibleViews()
- 位置: L162-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this._viewVisibilityStates.values()).reduce()`, `this._viewVisibilityStates.values()`

## currentSetupState()
- 位置: L170-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setupState.get()`
- 参照: `this._currentSetupStateName`

## isTabSyncSetupComplete()
- 位置: L173-175
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentSetupState.uiStateIndex`

## uiStateIndex()
- 位置: L176-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentSetupState.uiStateIndex`

## fxaSignedIn()
- 位置: L179-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `UIState.isReady()`
- 参照: `UIState.STATUS_SIGNED_IN`, `syncState.status`, `syncState.syncEnabled`

## secondaryDeviceConnected()
- 位置: L190-196
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.fxAccounts.device?.recentDeviceList?.length`, `this.fxaSignedIn`

## mobileDeviceConnected()
- 位置: L197-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.fxAccounts.device.recentDeviceList?.filter()`
- 参照: `device.type`, `mobileClients?.length`, `this.fxaSignedIn`

## shouldShowMobilePromo()
- 位置: L206-214
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentSetupState.uiStateIndex`, `this.fxaSignedIn`, `this.mobileDeviceConnected`, `this.mobilePromoDismissedPref`, `this.syncIsConnected`

## shouldShowMobileConnectedSuccess()
- 位置: L215-221
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._shouldShowSuccessConfirmation`, `this.currentSetupState.uiStateIndex`, `this.mobileDeviceConnected`

## logger()
- 位置: L222-232
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._log)` → `lazy.Log.repository.getLogger()`
- 条件付き依存: `if (!this._log)` → `setupLog.manageLevelFromPref()`
- 条件付き依存: `if (!this._log)` → `setupLog.addAppender()`
- 参照: `lazy.Log.BasicFormatter`, `lazy.Log.ConsoleAppender`, `this._log`

## registerSetupState()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setupState.set()`
- 参照: `state.name`

## observe()
- 位置: async L238-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UIState.get()`, `lazy.fxAccounts.device.refreshDeviceList()`, `this.abortWaitingForTabs()`, `this.logger.debug()`, `this.maybeUpdateUI()`, `this.refreshDevices()`, `this.stopWaitingForTabs()`, `this.tryToClearError()`
- 条件付き依存: `if (this._lastFxASignedIn !== this.fxaSignedIn)` → `this.onSignedInChange()`
- 条件付き依存: `if (!(this._lastFxASignedIn !== this.fxaSignedIn))` → `this.maybeUpdateUI()`
- 条件付き依存: `if (deviceStateChanged)` → `this.maybeUpdateUI()`
- 条件付き依存: `if (deviceAdded && this.secondaryDeviceConnected)` → `this.logger.debug()`
- 条件付き依存: `if (this.hasVisibleViews)` → `this.startWaitingForNewDeviceTabs()`
- 条件付き依存: `if (lazy.UIState.get().status == lazy.UIState.STATUS_SIGNED_IN)` → `this.abortWaitingForTabs()`
- 条件付き依存: `if (lazy.UIState.get().status == lazy.UIState.STATUS_SIGNED_IN)` → `this.maybeUpdateUI()`
- 参照: `lazy.UIState.ON_UPDATE`, `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `lazy.UIState.get().syncEnabled`, `this._deviceAddedResultsNeverSeen`, `this._lastFxASignedIn`, `this._waitingForNextTabSync`, `this.fxaSignedIn`, `this.hasVisibleViews`, `this.secondaryDeviceConnected`, `this.syncIsConnected`

## updateViewVisibility()
- 位置: L298-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.logger.debug()`
- 条件付き依存: `if (visibility == "unloaded")` → `this._viewVisibilityStates.delete()`
- 条件付き依存: `if (!(visibility == "unloaded"))` → `this._viewVisibilityStates.set()`
- 条件付き依存: `if (this._noTabsVisibleFromAddedDeviceTimestamp)` → `this.stopWaitingForNewDeviceTabs()`
- 条件付き依存: `if (this._deviceAddedResultsNeverSeen)` → `this.startWaitingForNewDeviceTabs()`
- 条件付き依存: `if (!isVisible)` → `this.logger.debug()`
- 条件付き依存: `if (!isVisible)` → `this.abortWaitingForTabs()`
- 参照: `this._deviceAddedResultsNeverSeen`, `this._noTabsVisibleFromAddedDeviceTimestamp`, `this.hasVisibleViews`

## waitingForTabs()
- 位置: L331-336
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._waitingForNextTabSync`, `this.secondaryDeviceConnected`

## abortWaitingForTabs()
- 位置: L338-343
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._deviceAddedResultsNeverSeen`, `this._noTabsVisibleFromAddedDeviceTimestamp`, `this._waitingForNextTabSync`

## startWaitingForTabs()
- 位置: L345-350
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._waitingForNextTabSync)` → `Services.obs.notifyObservers()`
- 参照: `this._waitingForNextTabSync`
- XPCOM: `Services.obs`

## stopWaitingForTabs()
- 位置: async L352-361
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.hasVisibleViews && this._deviceAddedResultsNeverSeen)` → `this.stopWaitingForNewDeviceTabs()`
- 条件付き依存: `if (wasWaiting)` → `Services.obs.notifyObservers()`
- 参照: `this._deviceAddedResultsNeverSeen`, `this._waitingForNextTabSync`, `this.hasVisibleViews`, `this.waitingForTabs`
- XPCOM: `Services.obs`

## onSignedInChange()
- 位置: async L363-420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabs.getRecentTabs()`, `this.logger.debug()`, `this.maybeUpdateUI()`, `this.refreshDevices()`
- 条件付き依存: `if (!this.fxaSignedIn)` → `this.abortWaitingForTabs()`
- 条件付き依存: `if (deviceStateChanged)` → `this.logger.debug()`
- 条件付き依存: `if (deviceStateChanged)` → `this.maybeUpdateUI()`
- 条件付き依存: `if (tabSyncNeeded)` → `this.startWaitingForTabs()`
- 条件付き依存: `if (tabSyncNeeded)` → `this.logger.debug()`
- 条件付き依存: `if (tabSyncNeeded)` → `this.syncTabs() .catch()`
- 条件付き依存: `if (tabSyncNeeded)` → `this.syncTabs()`
- 条件付き依存: `if (tabSyncNeeded)` → `this.stopWaitingForTabs()`
- 条件付き依存: `if (!willSync)` → `this.logger.debug()`
- 条件付き依存: `if (!willSync)` → `this.stopWaitingForTabs()`
- 参照: `recentTabs?.length`, `this.fxaSignedIn`, `this.isPrimaryPasswordLocked`

## startWaitingForNewDeviceTabs()
- 位置: async L422-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabs.getRecentTabs()`
- 条件付き依存: `if (this.hasVisibleViews && !hasRecentTabs)` → `Date.now()`
- 条件付き依存: `if (this.hasVisibleViews && !hasRecentTabs)` → `this.logger.debug()`
- 参照: `(await lazy.SyncedTabs.getRecentTabs(1)).length`, `this._noTabsVisibleFromAddedDeviceTimestamp`, `this.hasVisibleViews`

## stopWaitingForNewDeviceTabs()
- 位置: async L440-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabs.getRecentTabs()`
- 条件付き依存: `if (recentTabs.length)` → `Date.now()`
- 条件付き依存: `if (recentTabs.length)` → `this.logger.debug()`
- 条件付き依存: `if (recentTabs.length)` → `Math.round()`
- 条件付き依存: `if (!(recentTabs.length))` → `this.logger.debug()`
- 参照: `recentTabs.length`, `this._deviceAddedResultsNeverSeen`, `this._noTabsVisibleFromAddedDeviceTimestamp`

## refreshDevices()
- 位置: async L463-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.fxAccounts.device.recentDeviceList?.some()`, `this.logger.debug()`
- 条件付き依存: `if ( !lazy.fxAccounts.device.recentDeviceList?.some( device => device.isCurrentDevice ) )` → `lazy.fxAccounts.device.refreshDeviceList()`
- 条件付き依存: `if (deviceStateChanged)` → `this.logger.debug()`
- 条件付き依存: `if (!secondaryDeviceConnected)` → `this.logger.debug()`
- 条件付き依存: `if (!secondaryDeviceConnected)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(deviceStateChanged))` → `this.logger.debug()`
- 参照: `device.isCurrentDevice`, `lazy.fxAccounts.device?.recentDeviceList?.length`, `this._deviceStateSnapshot`, `this._deviceStateSnapshot.mobileDeviceConnected`, `this._deviceStateSnapshot.secondaryDeviceConnected`, `this._deviceStateSnapshot?.devicesCount`, `this._didShowMobilePromo`, `this._shouldShowSuccessConfirmation`, `this.mobileDeviceConnected`, `this.secondaryDeviceConnected`
- XPCOM: `Services.obs`

## maybeUpdateUI()
- 位置: async L524-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `state.exitConditions()`, `this.logger.debug()`, `this.setupState.get()`, `this.setupState.values()`
- 条件付き依存: `if (!state.exitConditions())` → `this.logger.debug()`
- 条件付き依存: `if (uiStateIndex == 0)` → `ChromeUtils.idleDispatch()`
- 条件付き依存: `if (uiStateIndex == 0)` → `resolve()`
- 条件付き依存: `if (uiStateIndex == 0)` → `lazy.SyncedTabsErrorHandler.getErrorType()`
- 条件付き依存: `if (uiStateIndex == 0)` → `this.logger.debug()`
- 条件付き依存: `if (stateChanged || forceUpdate)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if ("function" == typeof setupState.enter)` → `setupState.enter()`
- 参照: `setupState.enter`, `state.name`, `state.uiStateIndex`, `this._currentSetupStateName`, `this._didShowMobilePromo`, `this.currentSetupState`, `this.shouldShowMobilePromo`
- XPCOM: `Services.obs`

## openFxASignup()
- 位置: async L579-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.fxAccounts.constructor.canConnectAccount()`, `lazy.fxAccounts.constructor.config.promiseConnectAccountURI()`, `openTabInWindow()`
- 参照: `this.didFxaTabOpen`

## openFxAPairDevice()
- 位置: async L592-598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.fxAccounts.constructor.config.promisePairingURI()`, `openTabInWindow()`
- 参照: `this.didFxaTabOpen`

## syncOpenTabs()
- 位置: L600-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## syncOnPageReload()
- 位置: async L606-611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UIState.isReady()`
- 条件付き依存: `if (lazy.UIState.isReady() && this.fxaSignedIn)` → `this.startWaitingForTabs()`
- 条件付き依存: `if (lazy.UIState.isReady() && this.fxaSignedIn)` → `this.syncTabs()`
- 参照: `this.fxaSignedIn`

## tryToClearError()
- 位置: L613-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UIState.isReady()`
- 条件付き依存: `if (lazy.UIState.isReady() && this.fxaSignedIn)` → `this.startWaitingForTabs()`
- 条件付き依存: `if (this.isPrimaryPasswordLocked)` → `lazy.syncUtils.ensureMPUnlocked()`
- 条件付き依存: `if (lazy.UIState.isReady() && this.fxaSignedIn)` → `this.logger.debug()`
- 条件付き依存: `if (lazy.UIState.isReady() && this.fxaSignedIn)` → `this.syncTabs()`
- 条件付き依存: `if (lazy.UIState.isReady() && this.fxaSignedIn)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (!(lazy.UIState.isReady() && this.fxaSignedIn))` → `this.logger.debug()`
- 条件付き依存: `if (!(lazy.UIState.isReady() && this.fxaSignedIn))` → `lazy.UIState.isReady()`
- 参照: `this.fxaSignedIn`, `this.isPrimaryPasswordLocked`
- XPCOM: `Services.tm`

## syncTabs()
- 位置: L631-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabs.syncTabs()`
