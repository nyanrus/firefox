# browser/actors/BlockedSiteParent.sys.mjs

source: browser/actors/BlockedSiteParent.sys.mjs
source-hash: 7f348199bc402fdc016d9bc47d967daf2953e8e0
lines: 299

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.strings.createBundle()`

## SafeBrowsingNotificationBox.constructor()
- 位置: L25-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addProgressListener()`, `this.#getDomainForComparison()`, `this.show()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `browser.currentURI`, `this._currentURIBaseDomain`, `this.browser`
- XPCOM: [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)

## SafeBrowsingNotificationBox.show()
- 位置: async L37-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.browser.getTabBrowser()`
- 条件付き依存: `if (previousNotification)` → `notificationBox.removeNotification()`
- 参照: `notification.persistence`, `notificationBox.PRIORITY_CRITICAL_HIGH`, `this.browser`

## SafeBrowsingNotificationBox.onLocationChange()
- 位置: L61-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getDomainForComparison()`
- 条件付き依存: `if ( !this._currentURIBaseDomain || newURIBaseDomain !== this._currentURIBaseDomain )` → `this.cleanup()`
- 参照: `this._currentURIBaseDomain`, `webProgress.isTopLevel`

## SafeBrowsingNotificationBox.cleanup()
- 位置: L75-93
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.browser)` → `this.browser.getTabBrowser()`
- 条件付き依存: `if (this.browser)` → `gBrowser.getNotificationBox()`
- 条件付き依存: `if (this.browser)` → `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `notificationBox.removeNotification()`
- 条件付き依存: `if (this.browser)` → `this.browser.removeProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `this._currentURIBaseDomain`, `this.browser`, `this.browser.safeBrowsingNotification`
- XPCOM: [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)

## SafeBrowsingNotificationBox.#getDomainForComparison()
- 位置: L95-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`
- 参照: `uri.asciiHost`, `uri.asciiSpec`
- XPCOM: `Services.eTLD`

## BlockedSiteParent.receiveMessage()
- 位置: L113-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onAboutBlocked()`
- 参照: `msg.data.blockedInfo`, `msg.data.elementId`, `msg.data.reason`, `msg.name`, `this.browsingContext`, `this.browsingContext.top`

## BlockedSiteParent._onAboutBlocked()
- 位置: L126-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.leaveErrorPage()`
- 条件付き依存: `if (sendTelemetry)` → `Glean.urlclassifier.uiEvents.accumulateSingleSample()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.safebrowsing.allowOverride"))` → `this.ignoreWarningLink()`
- 参照: `Ci.IUrlClassifierUITelemetry`, `this.browsingContext.top.embedderElement`
- XPCOM: `Services.prefs`

## BlockedSiteParent.ignoreWarningLink()
- 位置: L173-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.addFromPrincipal()`, `Services.scriptSecurityManager.createContentPrincipal()`, `browser.safeBrowsingNotification?.cleanup()`, `browsingContext.currentURI.mutate()`, `browsingContext.currentURI.mutate().setQuery()`, `browsingContext.currentURI.mutate().setQuery("").finalize()`, `browsingContext.loadURI()`, `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "malware")` → `lazy.SafeBrowsing.getReportURL()`
- 条件付き依存: `if (reason === "malware")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reportUrl)` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "phishing")` → `lazy.SafeBrowsing.getReportURL()`
- 条件付き依存: `if (reason === "phishing")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "unwanted")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "harmful")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (!activeSHEntry)` → `console.error()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.EXPIRE_SESSION`, `Ci.nsIWebNavigation.LOAD_FLAGS_BYPASS_CLASSIFIER`, `activeSHEntry.triggeringPrincipal`, `browser.safeBrowsingNotification`, `browsingContext.activeSessionHistoryEntry`, `browsingContext.currentWindowGlobal.documentPrincipal.originAttributes`, `browsingContext.top.embedderElement`, `browsingContext.topChromeWindow`, `uri.asciiSpec`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md) / `Services.perms` / `Services.scriptSecurityManager`

## callback()
- 位置: L201-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.leaveErrorPage()`
- 参照: `browsingContext.top.embedderElement`

## BlockedSiteParent.callback()
- 位置: L228-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.URILoadingHelper.openTrustedLinkIn()`

## BlockedSiteParent.callback()
- 位置: L255-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.URILoadingHelper.openTrustedLinkIn()`
