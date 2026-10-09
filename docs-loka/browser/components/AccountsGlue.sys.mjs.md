# browser/components/AccountsGlue.sys.mjs

source: browser/components/AccountsGlue.sys.mjs
source-hash: fe44c8924c1ba510091ef875787b1d5f2341efc5
lines: 490

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.Constructor()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## init()
- 位置: L66-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `os.addObserver()`
- 参照: `Services.obs`
- XPCOM: `Services.obs`

## observe()
- 位置: L79-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.UIState.get()`, `this._onDeviceConnected()`, `this._onDisplaySyncURIs()`, `this._onIncomingCloseTabCommand()`, `this._onThisDeviceConnected()`, `this._updateFxaBadges()`
- 条件付き依存: `if (data.isLocalDevice)` → `this._onDeviceDisconnected()`
- 条件付き依存: `if (lazy.CLIENT_ASSOCIATION_PING_ENABLED)` → `lazy.UIState.get()`
- 条件付き依存: `if (fxaState.status == lazy.UIState.STATUS_SIGNED_IN)` → `Glean.clientAssociation.uid.set()`
- 条件付き依存: `if (fxaState.status == lazy.UIState.STATUS_SIGNED_IN)` → `Glean.clientAssociation.legacyClientId.set()`
- 条件付き依存: `if (fxaState.status == lazy.UIState.STATUS_SIGNED_IN)` → `lazy.ClientID.getCachedClientID()`
- 条件付き依存: `if (data == "mock-alerts-service")` → `Object.defineProperty()`
- 条件付き依存: `if ( lazy.CLIENT_INFO_PING_ENABLED && lazy.UIState.get().status == lazy.UIState.STATUS_SIGNED_IN )` → `GleanPings.fxAccountsClientInfo.submit()`
- 参照: `data.isLocalDevice`, `fxaState.status`, `fxaState.uid`, `lazy.CLIENT_ASSOCIATION_PING_ENABLED`, `lazy.CLIENT_INFO_PING_ENABLED`, `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `subject.wrappedJSObject`

## _onThisDeviceConnected()
- 位置: L136-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValuesSync()`

## clickCallback()
- 位置: L142-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openPreferences()`

## _openURLInNewWindow()
- 位置: L156-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`, `Services.ww.openWindow()`, `resolve()`, `win.addEventListener()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsISupportsString`, `urlString.data`
- XPCOM: [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1` / `Services.ww`

## _onDisplaySyncURIs()
- 位置: async L191-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `URIs.slice()`, `URIs.slice(1).map()`, `console.error()`, `lazy.AlertsService.showAlert()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.accountsL10n.formatValue()`, `openTab()`
- 条件付き依存: `if (URIs.length == 1)` → `URIs[0].uri.replace()`
- 条件付き依存: `if (URIs.length == 1)` → `lazy.BrowserUIUtils.trimURL()`
- 条件付き依存: `if (wasTruncated)` → `lazy.accountsL10n.formatValue()`
- 条件付き依存: `if (!(URIs.length == 1))` → `URIs.every()`
- 条件付き依存: `if (!(URIs.length == 1))` → `lazy.accountsL10n.formatValue()`
- 参照: `URI.sender`, `URI.sender.id`, `URIs.length`, `URIs[0].sender`, `URIs[0].sender.id`, `URIs[0].sender.name`, `URIs[0].uri.length`, `data.wrappedJSObject.object`, `titleL10nId.args`, `titleL10nId.id`, `url.length`

## openTab()
- 位置: async L204-222
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!win)` → `this._openURLInNewWindow()`
- 条件付き依存: `if (!(!win))` → `win.gBrowser.addWebTab()`
- 参照: `URI.private`, `URI.uri`, `tab.attention`, `tabs.length`, `win.gBrowser.tabs`

## clickCallback()
- 位置: L278-285
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (obsTopic == "alertclickcallback")` → `firstTab.documentGlobal.window.focus()`
- 参照: `firstTab.documentGlobal.gBrowser.selectedTab`

## _onIncomingCloseTabCommand()
- 位置: async L298-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `closeTabsInWindows()`, `console.error()`, `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValues()`, `urisToClose.push()`, `urls.forEach()`
- 参照: `data.wrappedJSObject.object`, `lazy.BrowserWindowTracker.orderedWindows`, `lazy.CloseRemoteTab.closeTabNotificationCount`, `lazy.CloseRemoteTab.hasPendingCloseTabNotification`
- XPCOM: `Services.io`

## closeTabsInWindows()
- 位置: async L316-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.log.error()`, `win.gBrowser.closeTabsByURI()`
- 参照: `win.gBrowser`

## clickCallback()
- 位置: async L332-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (win)` → `win.FirefoxViewHandler.openTab()`
- 参照: `lazy.CloseRemoteTab.hasPendingCloseTabNotification`

## _onDeviceConnected()
- 位置: L384-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValuesSync()`

## clickCallback()
- 位置: async L392-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.FxAccounts.config.promiseManageDevicesURI()`
- 条件付き依存: `if (!win)` → `this._openURLInNewWindow()`
- 条件付き依存: `if (!(!win))` → `win.gBrowser.addWebTab()`

## _onDeviceDisconnected()
- 位置: L419-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AlertsService.showAlert()`, `lazy.accountsL10n.formatValuesSync()`

## clickCallback()
- 位置: L425-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openPreferences()`

## _updateFxaBadges()
- 位置: L440-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fxaButton?.querySelector()`, `lazy.UIState.get()`, `win.document.getElementById()`
- 条件付き依存: `if ( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED )` → `win.document.getElementById()`
- 条件付き依存: `if ( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED )` → `navToolbox.contains()`
- 条件付き依存: `if (isFxAButtonShown)` → `fxaButton?.setAttribute()`
- 条件付き依存: `if (isFxAButtonShown)` → `badge?.classList.add()`
- 条件付き依存: `if (!(isFxAButtonShown))` → `lazy.AppMenuNotifications.showBadgeOnlyNotification()`
- 条件付き依存: `if (!( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED ))` → `fxaButton?.removeAttribute()`
- 条件付き依存: `if (!( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED ))` → `badge?.classList.remove()`
- 条件付き依存: `if (!( state.status == lazy.UIState.STATUS_LOGIN_FAILED || state.status == lazy.UIState.STATUS_NOT_VERIFIED ))` → `lazy.AppMenuNotifications.removeNotification()`
- 参照: `lazy.UIState.STATUS_LOGIN_FAILED`, `lazy.UIState.STATUS_NOT_VERIFIED`, `state.status`

## _openPreferences()
- 位置: async L470-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!chromeWindow && AppConstants.platform !== "macosx")` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (chromeWindow)` → `chromeWindow.openPreferences()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Services.appShell.hiddenDOMWindow.openPreferences()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.appShell`
