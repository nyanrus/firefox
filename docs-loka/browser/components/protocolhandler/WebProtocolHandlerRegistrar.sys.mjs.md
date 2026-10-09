# browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs

source: browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs
source-hash: 036e521c7263c4ad84cd3cfafcb99e806bad30e8
lines: 681

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetters()`

## WebProtocolHandlerRegistrar()
- 位置: L9-9
- 役割: (未記入)
- 触るとき: (未記入)

## stringBundle()
- 位置: L41-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings.createBundle()`
- 参照: `WebProtocolHandlerRegistrar.prototype.stringBundle`
- XPCOM: `Services.strings`

## _getFormattedString()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stringBundle.formatStringFromName()`

## _getString()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stringBundle.GetStringFromName()`

## _ensureWebmailerCache()
- 位置: L63-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handler.possibleApplicationHandlers.enumerate()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`, `lazy.log.debug()`
- 条件付き依存: `if (h instanceof Ci.nsIWebHandlerApp && h.uriTemplate)` → `Services.io.newURI()`
- 条件付き依存: `if (mailerUri.scheme == "https")` → `this._knownWebmailerCache.set()`
- 条件付き依存: `if (mailerUri.scheme == "https")` → `Services.io.newURI()`
- 条件付き依存: `if (mailerUri.scheme == "https")` → `Services.io.newURI(h.uriTemplate).resolve()`
- 参照: `Ci.nsIWebHandlerApp`, `Services.io.newURI(h.uriTemplate).host`, `e.message`, `h.name`, `h.uriTemplate`, `mailerUri.scheme`, `this._knownWebmailerCache`
- XPCOM: [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `Services.io`

## init()
- 位置: L99-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.mailto.getVariable()`
- 条件付き依存: `if (firstInit)` → `lazy.NimbusFeatures.mailto.onUpdate()`
- 条件付き依存: `if (firstInit)` → `this.init()`
- 条件付き依存: `if ( lazy.NimbusFeatures.mailto.getVariable("dualPrompt") && lazy.NimbusFeatures.mailto.getVariable("dualPrompt.onLocationChange") )` → `this._ensureWebmailerCache()`
- 条件付き依存: `if (0 == this._addedObservers)` → `observers.forEach()`
- 条件付き依存: `if (0 == this._addedObservers)` → `Services.obs.addObserver()`
- 条件付き依存: `if (0 == this._addedObservers)` → `lazy.log.debug()`
- 条件付き依存: `if (!( lazy.NimbusFeatures.mailto.getVariable("dualPrompt") && lazy.NimbusFeatures.mailto.getVariable("dualPrompt.onLocationChange") ))` → `observers.forEach()`
- 条件付き依存: `if (!( lazy.NimbusFeatures.mailto.getVariable("dualPrompt") && lazy.NimbusFeatures.mailto.getVariable("dualPrompt.onLocationChange") ))` → `Services.obs.enumerateObservers(o).hasMoreElements()`
- 条件付き依存: `if (!( lazy.NimbusFeatures.mailto.getVariable("dualPrompt") && lazy.NimbusFeatures.mailto.getVariable("dualPrompt.onLocationChange") ))` → `Services.obs.enumerateObservers()`
- 条件付き依存: `if ( 0 < this._addedObservers && Services.obs.enumerateObservers(o).hasMoreElements() )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( 0 < this._addedObservers && Services.obs.enumerateObservers(o).hasMoreElements() )` → `lazy.log.debug()`
- 参照: `this._addedObservers`
- XPCOM: `Services.obs`

## observe()
- 位置: async L143-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this._ensureWebmailerCache()`, `this._knownWebmailerCache.has()`, `uri?.schemeIs()`
- 条件付き依存: `if (this._knownWebmailerCache.has(host))` → `this._knownWebmailerCache.get()`
- 条件付き依存: `if (this._knownWebmailerCache.has(host))` → `this._askUserToSetMailtoHandler()`
- 参照: `aBrowser.currentURI`, `uri.host`, `value.name`, `value.uriTemplate`

## removeProtocolHandler()
- 位置: L187-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handlers.queryElementAt()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`
- 条件付き依存: `if (handler.uriTemplate == aURITemplate)` → `handlers.removeElementAt()`
- 条件付き依存: `if (handler.uriTemplate == aURITemplate)` → `Cc["@mozilla.org/uriloader/handler-service;1"].getService()`
- 条件付き依存: `if (handler.uriTemplate == aURITemplate)` → `hs.store()`
- 参照: `Ci.nsIHandlerService`, `Ci.nsIWebHandlerApp`, `handler.uriTemplate`, `handlerInfo.possibleApplicationHandlers`, `handlers.length`
- XPCOM: [`nsIHandlerService`](../../../uriloader/exthandler/nsIHandlerService.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/handler-service;1`

## _protocolHandlerRegistered()
- 位置: L218-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handlers.enumerate()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`
- 参照: `Ci.nsIWebHandlerApp`, `handler.uriTemplate`, `handlerInfo.possibleApplicationHandlers`
- XPCOM: [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md)

## _isProtocolHandlerDefault()
- 位置: L244-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExternalProtocolService.getProtocolHandlerInfo()`
- 条件付き依存: `if ( handlerInfo.preferredAction == Ci.nsIHandlerInfo.useHelperApp && handlerInfo.preferredApplicationHandler instanceof Ci.nsIWebHandlerApp )` → `handlerInfo.preferredApplicationHandler.QueryInterface()`
- 条件付き依存: `if ( handlerInfo.preferredAction == Ci.nsIHandlerInfo.useHelperApp && handlerInfo.preferredApplicationHandler instanceof Ci.nsIWebHandlerApp )` → `this._canSetOSDefault()`
- 参照: `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIWebHandlerApp`, `aURITemplate.spec`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`, `webHandlerApp.uriTemplate`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md)

## _getInstallHash()
- 位置: L280-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/xre/directory-provider;1" ].getService()`, `xreDirProvider.getInstallHash()`
- 参照: `Ci.nsIXREDirProvider`
- XPCOM: [`nsIXREDirProvider`](../../../toolkit/xre/nsIXREDirProvider.idl.md) / `@mozilla.org/xre/directory-provider;1`

## _isOsDefault()
- 位置: L294-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/browser/shell-service;1" ].createInstance()`, `lazy.log.debug()`, `shellService.isDefaultHandlerFor()`
- 条件付き依存: `if (shellService.isDefaultHandlerFor(protocol))` → `lazy.log.debug()`
- 参照: `Ci.nsIWindowsShellService`
- XPCOM: [`nsIWindowsShellService`](../shell/nsIWindowsShellService.idl.md) / `@mozilla.org/browser/shell-service;1`

## _canSetOSDefault()
- 位置: L315-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getInstallHash()`, `this._isOsDefault()`
- 条件付き依存: `if ("" == this._getInstallHash())` → `lazy.log.debug()`

## _setOSDefault()
- 位置: L338-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/default-agent;1"].createInstance()`, `defaultAgent.setDefaultExtensionHandlersUserChoice()`, `lazy.log.debug()`, `this._getInstallHash()`
- 参照: `Ci.nsIDefaultAgent`, `e.message`
- XPCOM: [`nsIDefaultAgent`](../../../toolkit/mozapps/defaultagent/nsIDefaultAgent.idl.md) / `@mozilla.org/default-agent;1`

## _setProtocolHandlerDefault()
- 位置: L369-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/uriloader/handler-service;1"].getService()`, `hs.store()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`
- 参照: `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerService`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIHandlerService`](../../../uriloader/exthandler/nsIHandlerService.idl.md) / `@mozilla.org/uriloader/handler-service;1`

## _addWebProtocolHandler()
- 位置: L391-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/uriloader/handler-service;1"].getService()`, `Cc["@mozilla.org/uriloader/web-handler-app;1"].createInstance()`, `handlerInfo.possibleApplicationHandlers.appendElement()`, `hs.store()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`, `phi.possibleApplicationHandlers.enumerate()`
- 参照: `Ci.nsIHandlerService`, `Ci.nsIWebHandlerApp`, `h.uriTemplate`, `handler.name`, `handler.uriTemplate`
- XPCOM: [`nsIHandlerService`](../../../uriloader/exthandler/nsIHandlerService.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/handler-service;1` / `@mozilla.org/uriloader/web-handler-app;1` → `nsWebHandlerApp` (uriloader/exthandler/components.conf)

## registerProtocolHandler()
- 位置: L421-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aProtocol || "").toLowerCase()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `browserWindow.navigator.checkProtocolHandlerAllowed()`, `lazy.NimbusFeatures.mailto.getVariable()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this._getFormattedString()`, `this._getString()`, `this._protocolHandlerRegistered()`
- 条件付き依存: `if (aBrowserOrWindow instanceof Ci.nsIDOMWindow)` → `rootDocShell.QueryInterface()`
- 条件付き依存: `if ("mailto" === aProtocol)` → `lazy.NimbusFeatures.mailto.recordExposureEvent()`
- 条件付き依存: `if ("mailto" === aProtocol)` → `this._askUserToSetMailtoHandler()`
- 参照: `Ci.nsIDOMWindow`, `Ci.nsIDocShell`, `aBrowserOrWindow.docShell.sameTypeRootTreeItem`, `aURI.host`, `aURI.prePath`, `aURI.spec`, `browser.documentGlobal`, `notificationBox.PRIORITY_INFO_LOW`, `rootDocShell.QueryInterface(Ci.nsIDocShell).chromeEventHandler`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md) / [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md)

## callback()
- 位置: L479-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/web-handler-app;1" ].createInstance()`, `Cc["@mozilla.org/uriloader/handler-service;1"].getService()`, `handlerInfo.possibleApplicationHandlers.appendElement()`, `hs.store()`, `lazy.ExternalProtocolService.getProtocolHandlerInfo()`
- 参照: `Ci.nsIHandlerService`, `Ci.nsIWebHandlerApp`, `aButtonInfo.protocolInfo.name`, `aButtonInfo.protocolInfo.protocol`, `aButtonInfo.protocolInfo.uri`, `handler.name`, `handler.uriTemplate`, `handlerInfo.alwaysAskBeforeHandling`
- XPCOM: [`nsIHandlerService`](../../../uriloader/exthandler/nsIHandlerService.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/handler-service;1` / `@mozilla.org/uriloader/web-handler-app;1` → `nsWebHandlerApp` (uriloader/exthandler/components.conf)

## _askUserToSetMailtoHandler()
- 位置: async L535-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.testExactPermissionFromPrincipal()`, `browser .getTabBrowser()`, `browser .getTabBrowser() .getNotificationBox()`, `browser.getTabBrowser()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `osDefaultNotificationBox.getNotificationWithValue()`, `this._isProtocolHandlerDefault()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(browser.documentGlobal))` → `lazy.log.debug()`
- 条件付き依存: `if (this._isProtocolHandlerDefault(aProtocol, aURI))` → `lazy.log.debug()`
- 条件付き依存: `if ( Ci.nsIPermissionManager.DENY_ACTION == Services.perms.testExactPermissionFromPrincipal( principal, "mailto-infobar-dismissed" ) )` → `Services.perms.getPermissionObject()`
- 条件付き依存: `if ( Ci.nsIPermissionManager.DENY_ACTION == Services.perms.testExactPermissionFromPrincipal( principal, "mailto-infobar-dismissed" ) )` → `Date.now()`
- 条件付き依存: `if ( Ci.nsIPermissionManager.DENY_ACTION == Services.perms.testExactPermissionFromPrincipal( principal, "mailto-infobar-dismissed" ) )` → `lazy.log.debug()`
- 条件付き依存: `if ( Ci.nsIPermissionManager.DENY_ACTION == Services.perms.testExactPermissionFromPrincipal( principal, "mailto-infobar-dismissed" ) )` → `(expiry / 1000).toFixed()`
- 条件付き依存: `if (!osDefaultNotificationBox.getNotificationWithValue(notificationId))` → `win.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!osDefaultNotificationBox.getNotificationWithValue(notificationId))` → `osDefaultNotificationBox.appendNotification()`
- 条件付き依存: `if (!osDefaultNotificationBox.getNotificationWithValue(notificationId))` → `notification.setAttribute()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`, `Services.perms.getPermissionObject( principal, "mailto-infobar-dismissed", true ).expireTime`, `aURI.host`, `aURI.spec`, `browser.documentGlobal`, `browser.getTabBrowser().contentPrincipal`, `osDefaultNotificationBox.PRIORITY_INFO_LOW`, `principal.host`
- XPCOM: [`nsIPermissionManager`](../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## eventCallback()
- 位置: L596-613
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (eventType === "dismissed")` → `Services.perms.addFromPrincipal()`
- 条件付き依存: `if (eventType === "dismissed")` → `lazy.NimbusFeatures.mailto.getVariable()`
- 条件付き依存: `if (eventType === "dismissed")` → `Date.now()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`, `Ci.nsIPermissionManager.EXPIRE_TIME`
- XPCOM: [`nsIPermissionManager`](../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`

## callback()
- 位置: L619-644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addWebProtocolHandler()`, `this._canSetOSDefault()`, `this._setProtocolHandlerDefault()`
- 条件付き依存: `if (this._canSetOSDefault(aProtocol))` → `this._setOSDefault()`
- 条件付き依存: `if (this._setOSDefault(aProtocol))` → `newitem.removeChild()`
- 条件付き依存: `if (this._setOSDefault(aProtocol))` → `newitem.setAttribute()`
- 参照: `aURI.spec`, `newitem.buttonContainer`, `newitem.eventCallback`, `newitem.messageL10nId`

## callback()
- 位置: L648-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.perms.addFromPrincipal()`, `lazy.NimbusFeatures.mailto.getVariable()`
- 参照: `Ci.nsIPermissionManager.DENY_ACTION`, `Ci.nsIPermissionManager.EXPIRE_TIME`
- XPCOM: [`nsIPermissionManager`](../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.perms`
