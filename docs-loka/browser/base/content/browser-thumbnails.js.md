# browser/base/content/browser-thumbnails.js

source: browser/base/content/browser-thumbnails.js
source-hash: 6dd7c20dc24d75d56de96c6381e161f03110a67a
lines: 227

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`

## Thumbnails_init()
- 位置: L36-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `gBrowser.addTabsProgressListener()`, `gBrowser.tabContainer.addEventListener()`, `this._tabEvents.forEach()`
- 参照: `this.PREF_DISK_CACHE_SSL`, `this._sslDiskCacheEnabled`, `this._timeouts`
- XPCOM: `Services.prefs`

## Thumbnails_uninit()
- 位置: L51-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `gBrowser.removeTabsProgressListener()`, `gBrowser.tabContainer.removeEventListener()`, `this._tabEvents.forEach()`
- 条件付き依存: `if (this._topSiteURLsRefreshTimer)` → `this._topSiteURLsRefreshTimer.cancel()`
- 参照: `this.PREF_DISK_CACHE_SSL`, `this._topSiteURLsRefreshTimer`
- XPCOM: `Services.prefs`

## Thumbnails_handleEvent()
- 位置: L65-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cancelDelayedCapture()`, `this._delayedCapture()`, `this._timeouts.has()`
- 条件付き依存: `if (this._timeouts.has(browser))` → `this._delayedCapture()`
- 参照: `aEvent.currentTarget`, `aEvent.target.linkedBrowser`, `aEvent.type`

## Thumbnails_observe()
- 位置: L84-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.PREF_DISK_CACHE_SSL`, `this._sslDiskCacheEnabled`
- XPCOM: `Services.prefs`

## Thumbnails_clearTopSiteURLCache()
- 位置: L94-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`
- 条件付き依存: `if (this._topSiteURLsRefreshTimer)` → `this._topSiteURLsRefreshTimer.cancel()`
- 参照: `this._topSiteURLs`, `this._topSiteURLsRefreshTimer`

## Thumbnails_notify()
- 位置: L104-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowserThumbnails.clearTopSiteURLCache()`
- 参照: `gBrowserThumbnails._topSiteURLsRefreshTimer`

## Thumbnails_onStateChange()
- 位置: L112-125
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && aStateFlags & Ci.nsIWebProgressListener.STATE_IS_NETWORK )` → `this._delayedCapture()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _capture()
- 位置: async L127-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._shouldCapture()`, `topSites.includes()`
- 条件付き依存: `if (await this._shouldCapture(aBrowser))` → `PageThumbs.captureAndStoreIfStale()`
- 参照: `aBrowser.currentURI`, `aBrowser.currentURI.spec`, `this._topSiteURLs`

## Thumbnails_delayedCapture()
- 位置: L138-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestIdleCallback()`, `setTimeout()`, `this._timeouts.has()`, `this._timeouts.set()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `this._cancelDelayedCallbacks()`
- 条件付き依存: `if (!(this._timeouts.has(aBrowser)))` → `aBrowser.addEventListener()`
- 参照: `this._captureDelayMS`

## idleCallback()
- 位置: L145-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cancelDelayedCapture()`, `this._capture()`

## Thumbnails_shouldCapture()
- 位置: async L162-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PageThumbs.shouldStoreThumbnail()`, `gBrowser.currentURI.schemeIs()`
- 参照: `gBrowser.selectedBrowser`

## Thumbnails_cancelDelayedCapture()
- 位置: L173-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._timeouts.has()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `aBrowser.removeEventListener()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `this._cancelDelayedCallbacks()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `this._timeouts.delete()`

## Thumbnails_cancelDelayedCallbacks()
- 位置: L181-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._timeouts.get()`
- 条件付き依存: `if (timeoutData.isTimeout)` → `clearTimeout()`
- 条件付き依存: `if (!(timeoutData.isTimeout))` → `window.cancelIdleCallback()`
- 参照: `timeoutData.id`, `timeoutData.isTimeout`

## getTopSiteURLs()
- 位置: async L195-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/timer;1" ].createInstance()`, `NewTabUtils.activityStreamLinks.getTopSites()`, `gBrowserThumbnails._topSiteURLsRefreshTimer.initWithCallback()`, `sites.push()`, `sites.reduce()`, `topSites.filter()`
- 条件付き依存: `if (link)` → `urls.push()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `NewTabUtils.pinnedLinks.links`, `gBrowserThumbnails._topSiteURLsRefreshTimer`, `link.faviconSize`, `link.url`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`
