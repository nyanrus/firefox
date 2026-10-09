# browser/extensions/ipp-activator/extension/api/parent/ext-ipp.js

source: browser/extensions/ipp-activator/extension/api/parent/ext-ipp.js
source-hash: a111f05e5c5276337dda08029c38eafe060ee18b
lines: 363

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## onStartup()
- 位置: L42-42
- 役割: (未記入)
- 触るとき: (未記入)

## onShutdown()
- 位置: L44-44
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L46-361
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ExtensionCommon.EventManager`

## register()
- 位置: L52-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.addEventListener()`, `lazy.IPPProxyManager.removeEventListener()`, `topics.forEach()`

## observer()
- 位置: L54-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`
- 参照: `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVE`

## hideMessage()
- 位置: L71-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `lazy.tabTracker.getTab()`, `nbox.getNotificationWithValue()`, `win.gBrowser.getNotificationBox()`
- 条件付き依存: `if (existing)` → `nbox.removeNotification()`
- 参照: `browser?.documentGlobal`, `lazy.tabTracker.activeTab`, `tab?.linkedBrowser`, `win.gBrowser`

## isIPPActive()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.IPPProxyManager.state`, `lazy.IPPProxyStates.ACTIVE`

## getRegion()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.Region.home`

## getDynamicTabBreakages()
- 位置: L98-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getDynamicWebRequestBreakages()
- 位置: L110-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getTabBreakagesUrl()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getWebRequestBreakagesUrl()
- 位置: L125-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getNotifiedDomains()
- 位置: L131-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## addNotifiedDomain()
- 位置: L143-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `Services.prefs.getStringPref()`, `String()`, `arr.includes()`
- 条件付き依存: `if (!arr.includes(d))` → `arr.push()`
- 条件付き依存: `if (!arr.includes(d))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!arr.includes(d))` → `JSON.stringify()`
- XPCOM: `Services.prefs`

## getBaseDomainFromURL()
- 位置: L169-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `Services.io.newURI()`
- 参照: `Cr.NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS`, `Services.io.newURI(url).host`, `e.result`
- XPCOM: `Services.eTLD` / `Services.io`

## hasExclusion()
- 位置: L190-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`, `lazy.IPPSiteRuleManager.getRule()`
- 参照: `lazy.IPPPrincipalRules.EXCLUDED`, `lazy.siteExceptionsEnabled`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## showMessage()
- 位置: async L207-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.ipprotection.breakageMessageShown.record()`, `Promise.resolve()`, `console.warn()`, `lazy.tabTracker.getTab()`, `nbox .appendNotification()`, `nbox.getNotificationWithValue()`, `win.gBrowser.getNotificationBox()`
- 条件付き依存: `if (!browser || !win || !win.gBrowser)` → `Promise.resolve()`
- 条件付き依存: `if (existing)` → `nbox.removeNotification()`
- 参照: `browser?.documentGlobal`, `lazy.tabTracker.activeTab`, `message.l10nId`, `nbox.PRIORITY_WARNING_HIGH`, `notification.persistence`, `tab?.linkedBrowser`, `win.gBrowser`

## eventCallback()
- 位置: L240-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveDismiss()`
- 条件付き依存: `if (param === "dismissed")` → `Glean.ipprotection.breakageMessageDismissed.record()`

## register()
- 位置: L265-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L267-274
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( topic === "nsPref:changed" && data === PREF_DYNAMIC_TAB_BREAKAGES )` → `fire.async()`

## register()
- 位置: L287-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L289-296
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( topic === "nsPref:changed" && data === PREF_DYNAMIC_WEBREQUEST_BREAKAGES )` → `fire.async()`

## register()
- 位置: L312-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## observe()
- 位置: L314-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `subject.QueryInterface()`
- 条件付き依存: `if (data === "cleared")` → `fire.async()`
- 参照: `Ci.nsIPermission`, `permission.type`
- XPCOM: [`nsIPermission`](../../../../../../netwerk/base/nsIPermission.idl.md)

## register()
- 位置: L346-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## observe()
- 位置: L348-352
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "browser-region-updated")` → `fire.async()`
- 参照: `lazy.Region.home`
