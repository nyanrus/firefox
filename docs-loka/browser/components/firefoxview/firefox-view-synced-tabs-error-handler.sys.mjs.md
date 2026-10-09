# browser/components/firefoxview/firefox-view-synced-tabs-error-handler.sys.mjs

source: browser/components/firefoxview/firefox-view-synced-tabs-error-handler.sys.mjs
source-hash: d6f0c60f0cb5864b6b501a930788892b50d5bf89
lines: 243

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Object.freeze()`, `Services.urlFormatter.formatURLPref()`, `XPCOMUtils.defineLazyServiceGetter()`

## init()
- 位置: L46-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.UIState.get()`
- 参照: `lazy.UIState.ON_UPDATE`, `lazy.UIState.get().syncEnabled`, `lazy.gNetworkLinkService.isLinkUp`, `lazy.gNetworkLinkService.linkStatusKnown`, `this.networkIsOnline`, `this.syncIsConnected`, `this.syncIsWorking`
- XPCOM: `Services.obs`

## fxaSignedIn()
- 位置: L62-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `UIState.isReady()`
- 参照: `UIState.STATUS_SIGNED_IN`, `syncState.status`, `syncState.syncEnabled`

## getErrorType()
- 位置: L73-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Services.prefs.prefIsLocked()`, `lazy.UIState.get()`
- 参照: `ErrorType.FXA_ADMIN_DISABLED`, `ErrorType.NETWORK_OFFLINE`, `ErrorType.PASSWORD_LOCKED`, `ErrorType.SIGNED_OUT`, `ErrorType.SYNC_DISCONNECTED`, `ErrorType.SYNC_ERROR`, `lazy.UIState.STATUS_LOGIN_FAILED`, `lazy.UIState.get().status`, `this.isPrimaryPasswordLocked`, `this.networkIsOnline`, `this.syncHasWorked`, `this.syncIsConnected`, `this.syncIsWorking`
- XPCOM: `Services.prefs`

## getFluentStringsForErrorType()
- 位置: L93-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.freeze()`, `Services.prefs.getBoolPref()`
- 参照: `this._errorStateStringMappings`, `this._novaErrorStateStringMappings`
- XPCOM: `Services.prefs`

## isPrimaryPasswordLocked()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.syncUtils.mpLocked()`

## isSyncReady()
- 位置: L104-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `lazy.UIState.get()`
- 参照: `lazy.UIState.STATUS_LOGIN_FAILED`, `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `this.fxaSignedIn`, `this.isPrimaryPasswordLocked`, `this.networkIsOnline`, `this.syncHasWorked`, `this.syncIsConnected`, `this.syncIsWorking`
- XPCOM: `Services.prefs`

## observe()
- 位置: L122-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UIState.get()`
- 参照: `lazy.UIState.ON_UPDATE`, `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `lazy.UIState.get().syncEnabled`, `this.networkIsOnline`, `this.syncHasWorked`, `this.syncIsConnected`, `this.syncIsWorking`
