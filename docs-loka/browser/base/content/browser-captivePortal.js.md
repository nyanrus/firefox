# browser/base/content/browser-captivePortal.js

source: browser/base/content/browser-captivePortal.js
source-hash: 4f332f0beb3507c82f5bc64d3f02f871023fcbe3
lines: 407

## <module>
- 役割: (未記入)
- 呼び出し先: `Date.now()`

## _captivePortalNotification()
- 位置: L32-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNotificationBox.getNotificationWithValue()`
- 参照: `this.PORTAL_NOTIFICATION_VALUE`

## canonicalURL()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`
- XPCOM: `Services.prefs`

## _browserBundle()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings.createBundle()`
- 参照: `this._browserBundle`
- XPCOM: `Services.strings`

## init()
- 位置: L49-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/captive-portal-service;1"].getService()`, `Services.obs.addObserver()`, `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (this._cps.state == this._cps.LOCKED_PORTAL)` → `this._captivePortalDetected()`
- 条件付き依存: `if (BrowserWindowTracker.windowCount == 1)` → `this.ensureCaptivePortalTab()`
- 参照: `BrowserWindowTracker.windowCount`, `Ci.nsICaptivePortalService`, `this._cps`, `this._cps.LOCKED_PORTAL`, `this._cps.UNKNOWN`, `this._cps.state`, `this._delayedRecheckPending`
- XPCOM: [`nsICaptivePortalService`](../../../netwerk/base/nsICaptivePortalService.idl.md) / `@mozilla.org/network/captive-portal-service;1` / `Services.obs`

## uninit()
- 位置: L83-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this._cancelDelayedCaptivePortal()`
- XPCOM: `Services.obs`

## delayedStartup()
- 位置: L91-96
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._delayedRecheckPending)` → `this._cps.recheckCaptivePortal()`
- 参照: `this._delayedRecheckPending`

## observe()
- 位置: L98-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cancelDelayedCaptivePortal()`, `this._captivePortalDetected()`, `this._captivePortalGone()`

## onLocationChange()
- 位置: L115-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.tm.dispatchToMainThread()`, `tab.linkedBrowser.currentURI.equalsExceptRef()`, `this._previousCaptivePortalTab.get()`
- 条件付き依存: `if ( tab && (tab.linkedBrowser.currentURI.equalsExceptRef(canonicalURI) || tab.linkedBrowser.currentURI.host == "support.mozilla.org") && (this._cps.state == thi...)` → `gBrowser.removeTab()`
- 参照: `tab.linkedBrowser`, `tab.linkedBrowser.currentURI.host`, `this._cps.UNKNOWN`, `this._cps.UNLOCKED_PORTAL`, `this._cps.state`, `this._previousCaptivePortalTab`, `this.canonicalURL`
- XPCOM: `Services.io` / `Services.tm`

## _captivePortalDetected()
- 位置: L155-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.io.newURI()`, `Services.perms.addFromPrincipal()`, `Services.scriptSecurityManager.createContentPrincipal()`, `this._showNotification()`, `win?.document.documentElement.getAttribute()`
- 条件付き依存: `if (win != Services.focus.activeWindow)` → `window.addEventListener()`
- 条件付き依存: `if (win != Services.focus.activeWindow)` → `Services.obs.addObserver()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.EXPIRE_SESSION`, `Services.focus.activeWindow`, `gBrowser.contentPrincipal.userContextId`, `this._delayedCaptivePortalDetectedInProgress`, `this.canonicalURL`
- XPCOM: [`nsIPermissionManager`](../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.focus` / `Services.io` / `Services.obs` / `Services.perms` / `Services.scriptSecurityManager`

## _delayedCaptivePortalDetected()
- 位置: L204-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `this._cps.recheckCaptivePortal()`, `window.document.documentElement.getAttribute()`
- 参照: `this._delayedCaptivePortalDetectedInProgress`, `this._waitingForRecheck`
- XPCOM: `Services.obs`

## observer()
- 位置: L223-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (time <= this.PORTAL_RECHECK_DELAY_MS)` → `this.ensureCaptivePortalTab()`
- 参照: `this.PORTAL_RECHECK_DELAY_MS`, `this._cps.LOCKED_PORTAL`, `this._cps.state`, `this._waitingForRecheck`
- XPCOM: `Services.obs`

## _captivePortalGone()
- 位置: L242-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.round()`, `Services.io.newURI()`, `tab.linkedBrowser.currentURI.equalsExceptRef()`, `this._cancelDelayedCaptivePortal()`, `this._captivePortalTab.get()`, `this._removeNotification()`
- 条件付き依存: `if (aSuccess)` → `Glean.networking.captivePortalBannerDisplayTime.success.add()`
- 条件付き依存: `if (!(aSuccess))` → `Glean.networking.captivePortalBannerDisplayTime.abort.add()`
- 条件付き依存: `if ( tab && tab.linkedBrowser && (tab.linkedBrowser.currentURI.equalsExceptRef(canonicalURI) || tab.linkedBrowser.currentURI.host == "support.mozilla.org") )` → `gBrowser.removeTab()`
- 参照: `tab.linkedBrowser`, `tab.linkedBrowser.currentURI.host`, `this._bannerDisplayTime`, `this._captivePortalTab`, `this._previousCaptivePortalTab`, `this.canonicalURL`
- XPCOM: `Services.io`

## _cancelDelayedCaptivePortal()
- 位置: L278-284
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._delayedCaptivePortalDetectedInProgress)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._delayedCaptivePortalDetectedInProgress)` → `window.removeEventListener()`
- 参照: `this._delayedCaptivePortalDetectedInProgress`
- XPCOM: `Services.obs`

## handleEvent()
- 位置: async L286-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.buttonContainer.querySelector()`, `this._captivePortalTab.get()`, `this._delayedCaptivePortalDetected()`
- 参照: `aEvent.type`, `button.style.visibility`, `doc.defaultView.gBrowser.selectedTab`, `tab.ownerDocument`, `this._captivePortalNotification`, `this._captivePortalTab`, `this._notificationPromise`

## _showNotification()
- 位置: L319-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.networking.captivePortalBannerDisplayed.add()`, `gBrowser.tabContainer.addEventListener()`, `gNotificationBox.appendNotification()`, `this._browserBundle.GetStringFromName()`
- 参照: `gNotificationBox.PRIORITY_INFO_MEDIUM`, `this.PORTAL_NOTIFICATION_VALUE`, `this._bannerDisplayTime`, `this._captivePortalNotification`, `this._notificationPromise`

## callback()
- 位置: L332-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureCaptivePortalTab()`

## closeHandler()
- 位置: L345-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (aEventName == "dismissed")` → `Math.round()`
- 条件付き依存: `if (aEventName == "dismissed")` → `Date.now()`
- 条件付き依存: `if (aEventName == "dismissed")` → `Glean.networking.captivePortalBannerDisplayTime.dismiss.add()`
- 参照: `this._bannerDisplayTime`

## _removeNotification()
- 位置: L375-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.close()`
- 参照: `n.parentNode`, `this._captivePortalNotification`

## ensureCaptivePortalTab()
- 位置: L383-405
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._captivePortalTab)` → `this._captivePortalTab.get()`
- 条件付き依存: `if (!tab || tab.closing || !tab.parentNode)` → `gBrowser.addWebTab()`
- 条件付き依存: `if (!tab || tab.closing || !tab.parentNode)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (!tab || tab.closing || !tab.parentNode)` → `Cu.getWeakReference()`
- 参照: `gBrowser.contentPrincipal.userContextId`, `gBrowser.selectedTab`, `tab.closing`, `tab.parentNode`, `this._captivePortalTab`, `this._previousCaptivePortalTab`, `this.canonicalURL`
- XPCOM: `Services.scriptSecurityManager`
