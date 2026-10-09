# browser/components/firefoxview/SyncedTabsController.sys.mjs

source: browser/components/firefoxview/SyncedTabsController.sys.mjs
source-hash: 2c79ad94ed95ef0cc6b83f77cc626aa6f2514720
lines: 468

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SyncedTabsController.constructor()
- 位置: L67-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.host.addController()`, `this.observe.bind()`
- 参照: `this._pendingCloseTabs`, `this.contextMenu`, `this.host`, `this.lastClosedURL`, `this.observe`, `this.pairDeviceCallback`, `this.signupCallback`

## SyncedTabsController.hostConnected()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.host.addEventListener()`

## SyncedTabsController.hostDisconnected()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.host.removeEventListener()`

## SyncedTabsController.isSyncedTabsLoaded()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentSetupStateIndex`

## SyncedTabsController.addSyncObservers()
- 位置: L93-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.observe`
- XPCOM: `Services.obs`

## SyncedTabsController.removeSyncObservers()
- 位置: L98-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.observe`
- XPCOM: `Services.obs`

## SyncedTabsController.handleEvent()
- 位置: L103-148
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `TabsSetupFlowManager.tryToClearError()`
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `TabsSetupFlowManager.openFxASignup()`
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `this.signupCallback()`
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `TabsSetupFlowManager.openFxAPairDevice()`
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `this.pairDeviceCallback()`
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `TabsSetupFlowManager.syncOpenTabs()`
- 条件付き依存: `if (event.type == "click" && event.target.dataset.action)` → `switchToTabHavingURI()`
- 条件付き依存: `if (event.type == "click" && event.composedTarget.href)` → `event.preventDefault()`
- 条件付き依存: `if (event.type == "click" && event.composedTarget.href)` → `switchToTabHavingURI()`
- 参照: `ErrorType.NETWORK_OFFLINE`, `ErrorType.PASSWORD_LOCKED`, `ErrorType.SIGNED_OUT`, `ErrorType.SYNC_DISCONNECTED`, `ErrorType.SYNC_ERROR`, `event.composedTarget.href`, `event.target`, `event.target.dataset.action`, `event.target.documentGlobal`, `event.type`, `event.view.browsingContext.topChromeWindow`, `win.docShell.chromeEventHandler.documentGlobal`

## SyncedTabsController.observe()
- 位置: async L150-161
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == TOPIC_SETUPSTATE_CHANGED)` → `this.updateStates()`
- 条件付き依存: `if (topic == SYNCED_TABS_CHANGED)` → `this.getSyncedTabData()`
- 参照: `this._pendingCloseTabs`, `this.lastClosedURL`

## SyncedTabsController.updateStates()
- 位置: async L163-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncedTabsErrorHandler.getErrorType()`, `this.host.requestUpdate()`
- 条件付き依存: `if (stateIndex == 4 && this.currentSetupStateIndex !== stateIndex)` → `this.getSyncedTabData()`
- 参照: `TabsSetupFlowManager.uiStateIndex`, `this.currentSetupStateIndex`, `this.errorState`

## SyncedTabsController.#getMessageCardForState()
- 位置: L256-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (error)` → `SyncedTabsErrorHandler.getFluentStringsForErrorType()`
- 参照: `mappings.asset`, `mappings.buttonLabel`, `mappings.description`, `mappings.descriptionLink`, `mappings.header`, `this.actionMappings`, `this.errorState`, `this.novaActionMappings`
- XPCOM: `Services.prefs`

## SyncedTabsController.getRenderInfo()
- 位置: L289-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `renderInfo[tab.client].tabs.push()`, `searchTabList()`, `this.getTabItems()`
- 参照: `device.clientType`, `device.id`, `device.name`, `lazy.COMMAND_CLOSETAB`, `renderInfo[id].tabItems`, `tab.availableCommands`, `tab.client`, `tab.device`, `tab.deviceType`, `this.currentSyncedTabs`, `this.devices`, `this.searchQuery`

## SyncedTabsController.getMessageCard()
- 位置: L322-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `this.#getMessageCardForState()`
- 条件付き依存: `if (this.errorState)` → `this.#getMessageCardForState()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue("services.sync.lastversion"))` → `this.#getMessageCardForState()`
- 条件付き依存: `if (!this.devices.length)` → `this.#getMessageCardForState()`
- 参照: `this.currentSetupStateIndex`, `this.devices.length`, `this.errorState`
- XPCOM: `Services.prefs`

## SyncedTabsController.getTabItems()
- 位置: L367-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `tabs ?.map()`, `this.isURLQueuedToClose()`
- 条件付き依存: `if (!(tabItem.url === this.lastClosedURL))` → `JSON.stringify()`
- 参照: `item.fxaDeviceId`, `item.url`, `tab.fxaDeviceId`, `tab.icon`, `tab.lastUsed`, `tab.title`, `tab.url`, `tabItem.closeRequested`, `tabItem.tertiaryActionClass`, `tabItem.tertiaryL10nArgs`, `tabItem.tertiaryL10nId`, `tabItem.url`, `this.contextMenu`, `this.lastClosedURL`

## SyncedTabsController.updateTabsList()
- 位置: L414-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `this.host.requestUpdate()`
- 参照: `syncedTabs.length`, `this.currentSyncedTabs`

## SyncedTabsController.getSyncedTabData()
- 位置: async L430-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabs.createRecentTabsList()`, `lazy.SyncedTabs.getTabClients()`, `this.updateTabsList()`
- 参照: `this.devices`

## SyncedTabsController.requestCloseRemoteTab()
- 位置: L442-449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabsManagement.enqueueTabToClose()`, `this._pendingCloseTabs.get()`, `this._pendingCloseTabs.get(fxaDeviceId).add()`, `this._pendingCloseTabs.has()`
- 条件付き依存: `if (!this._pendingCloseTabs.has(fxaDeviceId))` → `this._pendingCloseTabs.set()`
- 参照: `this.lastClosedURL`

## SyncedTabsController.removePendingTabToClose()
- 位置: L451-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SyncedTabsManagement.removePendingTabToClose()`, `this._pendingCloseTabs.get()`
- 条件付き依存: `if (urls)` → `urls.delete()`
- 条件付き依存: `if (!urls.size)` → `this._pendingCloseTabs.delete()`
- 参照: `this.lastClosedURL`, `urls.size`

## SyncedTabsController.isURLQueuedToClose()
- 位置: L463-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._pendingCloseTabs.get()`, `urls.has()`
