# browser/modules/ReducedProtectionNotification.sys.mjs

source: browser/modules/ReducedProtectionNotification.sys.mjs
source-hash: 7bc93bfa4c28751054d6dcd94e4f019ccded11ca
lines: 201

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## observePref()
- 位置: L28-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(PREF, false))` → `this.init()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref(PREF, false)))` → `this.uninit()`
- 参照: `this._prefObserved`
- XPCOM: `Services.prefs`

## init()
- 位置: L45-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( lazy.PrivateBrowsingUtils.isWindowPrivate(win) && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `win.gBrowser?.addTabsProgressListener()`
- 条件付き依存: `if ( lazy.PrivateBrowsingUtils.isWindowPrivate(win) && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `win.gBrowser?.removeTabsProgressListener()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._initialized`

## uninit()
- 位置: L71-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._blockedTrackers`, `this._initialized`, `this._pendingNotification`, `this._shownHosts`

## markUserReload()
- 位置: L82-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._blockedTrackers.has()`
- 条件付き依存: `if (this._blockedTrackers.has(aBrowser))` → `this._shownHosts.get(aBrowser)?.has()`
- 条件付き依存: `if (this._blockedTrackers.has(aBrowser))` → `this._shownHosts.get()`
- 条件付き依存: `if (host && !this._shownHosts.get(aBrowser)?.has(host))` → `this._pendingNotification.add()`
- 参照: `aBrowser.currentURI?.host`

## onContentBlockingEvent()
- 位置: L91-98
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent & Ci.nsIWebProgressListener.STATE_BLOCKED_TRACKING_CONTENT)` → `this._blockedTrackers.add()`
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_TRACKING_CONTENT`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: L100-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._blockedTrackers.delete()`, `this._pendingNotification.delete()`
- 条件付き依存: `if ( aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD && isPending && blockedTrackers )` → `this.showNotification(aBrowser).catch()`
- 条件付き依存: `if ( aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD && isPending && blockedTrackers )` → `this.showNotification()`
- 条件付き依存: `if ( aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD && isPending && blockedTrackers )` → `console.error()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## showNotification()
- 位置: async L122-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privacyReducedPageProtection.bannerShown.add()`, `aBrowser.getTabBrowser()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `tabbrowser.getNotificationBox()`, `this._shownHosts.get()`, `this._shownHosts.get(aBrowser).add()`, `this._shownHosts.get(aBrowser)?.has()`, `this._shownHosts.has()`
- 条件付き依存: `if (!this._shownHosts.has(aBrowser))` → `this._shownHosts.set()`
- 参照: `aBrowser.currentURI`, `currentURI.host`, `notificationBox.PRIORITY_INFO_LOW`

## callback()
- 位置: L152-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privacyReducedPageProtection.disableClicked.add()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## callback()
- 位置: L159-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privacyReducedPageProtection.reloadClicked.add()`, `aBrowser.reload()`
- 条件付き依存: `if (scopedPrefs)` → `scopedPrefs.setBoolPrefScoped()`
- 参照: `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_CRYPTOMINING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_EMAILTRACKING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_FINGERPRINTING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_SOCIALTRACKING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CRYPTOMINING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_EMAILTRACKING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_FINGERPRINTING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_SOCIALTRACKING_ENABLED`, `Ci.nsIScopedPrefs.PRIVACY_TRACKINGPROTECTION_CONTENT_ENABLED`, `Ci.nsIScopedPrefs.PRIVACY_TRACKINGPROTECTION_ENABLED`, `aBrowser.browsingContext`, `aBrowser.browsingContext.scopedPrefs`
- XPCOM: [`nsIScopedPrefs`](../../toolkit/components/antitracking/scopedprefs/nsIScopedPrefs.idl.md)
