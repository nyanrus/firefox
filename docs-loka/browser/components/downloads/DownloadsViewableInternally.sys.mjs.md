# browser/components/downloads/DownloadsViewableInternally.sys.mjs

source: browser/components/downloads/DownloadsViewableInternally.sys.mjs
source-hash: 6b508b700f148af560a7c448b3e8283f6f9927ad
lines: 336

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## register()
- 位置: L46-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `itemStr.split()`, `itemStr.split(",").map()`, `lazy.Integration.downloads.register()`, `pref.trim()`, `s.trim()`, `this._shouldViewDownloadInternally.bind()`, `this._updateAllHandlers()`
- 条件付き依存: `if (handlerType.initAvailable)` → `handlerType.initAvailable()`
- 参照: `handlerType.initAvailable`, `this._downloadTypesViewableInternally`

## initAvailable()
- 位置: L112-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewableInternally._updateHandler()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## initAvailable()
- 位置: L141-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewableInternally._updateHandler()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## _shouldViewDownloadInternally()
- 位置: L167-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aExtension?.toLowerCase()`, `handlerType.mimeTypes.includes()`, `this._downloadTypesViewableInternally.some()`, `this._enabledTypes.includes()`
- 参照: `handlerType.available`, `handlerType.extension`, `handlerType.managedElsewhere`

## _makeFakeHandler()
- 位置: L188-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `ChromeUtils.generateQI()`
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIMutableArray`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1`

## getFileExtensions()
- 位置: L192-194
- 役割: (未記入)
- 触るとき: (未記入)

## extensionExists()
- 位置: L198-200
- 役割: (未記入)
- 触るとき: (未記入)

## _saveSettings()
- 位置: L207-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setIntPref()`
- 参照: `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerType.extension`
- XPCOM: `Services.prefs`

## _restoreSettings()
- 位置: L218-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prevActionPref))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prevActionPref))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prevActionPref))` → `lazy.HandlerService.store()`
- 条件付き依存: `if (!(Services.prefs.prefHasUserValue(prevActionPref)))` → `lazy.HandlerService.remove()`
- 参照: `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerType.extension`
- XPCOM: `Services.prefs`

## _clearSavedSettings()
- 位置: L232-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## _updateAllHandlers()
- 位置: L237-244
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!handlerType.managedElsewhere)` → `this._updateHandler()`
- 参照: `handlerType.managedElsewhere`, `this._downloadTypesViewableInternally`

## _updateHandler()
- 位置: L246-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this._enabledTypes.includes()`
- 条件付き依存: `if (toBeRegistered && !wasRegistered)` → `this._becomeHandler()`
- 条件付き依存: `if (!toBeRegistered && wasRegistered)` → `this._unbecomeHandler()`
- 参照: `handlerType.available`, `handlerType.extension`
- XPCOM: `Services.prefs`

## _becomeHandler()
- 位置: L263-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.HandlerService.exists()`, `this._makeFakeHandler()`
- 条件付き依存: `if (!lazy.HandlerService.exists(fakeHandlerInfo))` → `lazy.HandlerService.store()`
- 条件付き依存: `if (!(!lazy.HandlerService.exists(fakeHandlerInfo)))` → `lazy.MIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if (handlerInfo.preferredAction != Ci.nsIHandlerInfo.handleInternally)` → `this._saveSettings()`
- 条件付き依存: `if (!(handlerInfo.preferredAction != Ci.nsIHandlerInfo.handleInternally))` → `this._clearSavedSettings()`
- 条件付き依存: `if ( handlerInfo.preferredAction != Ci.nsIHandlerInfo.useHelperApp && handlerInfo.preferredAction != Ci.nsIHandlerInfo.useSystemDefault )` → `lazy.HandlerService.store()`
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerInfo.useSystemDefault`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerType.extension`, `handlerType.mimeTypes`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `Services.prefs`

## _unbecomeHandler()
- 位置: L313-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `lazy.MIMEService.getFromTypeAndExtension()`, `this._clearSavedSettings()`
- 条件付き依存: `if (handlerInfo?.preferredAction == Ci.nsIHandlerInfo.handleInternally)` → `this._restoreSettings()`
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `handlerInfo?.preferredAction`, `handlerType.extension`, `handlerType.mimeTypes`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `Services.prefs`
