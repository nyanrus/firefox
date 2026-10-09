# browser/components/syncedtabs/SyncedTabsDeckComponent.sys.mjs

source: browser/components/syncedtabs/SyncedTabsDeckComponent.sys.mjs
source-hash: d07aa41e85e1ed4bf18815b544d6a14339456f8b
lines: 186

## <module>
- 役割: (未記入)

## SyncedTabsDeckComponent()
- 位置: L19-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/clipboardhelper;1"].getService()`
- 参照: `Ci.nsIClipboardHelper`, `this._DeckView`, `this._SyncedTabs`, `this._deckStore`, `this._getChromeWindow`, `this._syncedTabsListStore`, `this._window`, `this.tabListComponent`
- XPCOM: `nsIClipboardHelper` / `@mozilla.org/widget/clipboardhelper;1`

## container()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._deckView`, `this._deckView.container`

## init()
- 位置: L66-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(this.PANELS).map()`, `Services.obs.addObserver()`, `this._SyncedTabs.syncTabs()`, `this._SyncedTabs.syncTabs().catch()`, `this._deckStore.on()`, `this._deckStore.setPanels()`, `this._deckView.render()`, `this._recordPanelToggle()`, `this.updateDir()`, `this.updatePanel()`
- 参照: `UIState.ON_UPDATE`, `console.error`, `this.PANELS`, `this._DeckView`, `this._SyncedTabs.TOPIC_TABS_CHANGED`, `this._deckView`, `this._window`, `this.tabListComponent`
- XPCOM: `Services.obs`

## onConnectDeviceClick()
- 位置: L78-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openConnectDevice()`

## onSyncPrefClick()
- 位置: L79-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openSyncPrefs()`

## uninit()
- 位置: L93-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this._deckView.destroy()`, `this._recordPanelToggle()`
- 参照: `UIState.ON_UPDATE`, `this._SyncedTabs.TOPIC_TABS_CHANGED`
- XPCOM: `Services.obs`

## _recordPanelToggle()
- 位置: async L101-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.syncedTabs.sidebarToggle.record()`, `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`

## observe()
- 位置: L111-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._syncedTabsListStore.getData()`, `this.updateDir()`, `this.updatePanel()`
- 参照: `UIState.ON_UPDATE`, `this._SyncedTabs.TOPIC_TABS_CHANGED`

## getPanelStatus()
- 位置: async L128-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `console.error()`, `this._SyncedTabs.getTabClients()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `clients.length`, `state.syncEnabled`, `this.PANELS.LOGIN_FAILED`, `this.PANELS.NOT_AUTHED_INFO`, `this.PANELS.SINGLE_DEVICE_INFO`, `this.PANELS.SYNC_DISABLED`, `this.PANELS.TABS_CONTAINER`, `this.PANELS.TABS_DISABLED`, `this.PANELS.TABS_FETCHING`, `this.PANELS.UNVERIFIED`, `this._SyncedTabs.hasSyncedThisSession`, `this._SyncedTabs.isConfiguredToSyncTabs`

## updateDir()
- 位置: L156-167
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.isAppLocaleRTL`, `this._window.document`, `this._window.document.body.dir`
- XPCOM: `Services.locale`

## updatePanel()
- 位置: L169-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._deckStore.selectPanel()`, `this.getPanelStatus()`, `this.getPanelStatus() .then()`, `this.getPanelStatus() .then(panelId => this._deckStore.selectPanel(panelId)) .catch()`
- 参照: `console.error`

## openSyncPrefs()
- 位置: L176-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getChromeWindow()`, `this._getChromeWindow(this._window).gSync.openPrefs()`
- 参照: `this._window`

## openConnectDevice()
- 位置: L180-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getChromeWindow()`, `this._getChromeWindow(this._window).gSync.openConnectAnotherDevice()`
- 参照: `this._window`
