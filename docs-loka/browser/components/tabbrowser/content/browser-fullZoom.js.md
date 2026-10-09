# browser/components/tabbrowser/content/browser-fullZoom.js

source: browser/components/tabbrowser/content/browser-fullZoom.js
source-hash: 2eeec9066afc8e6a9cdeb7c2f0eb2c629b456faa
lines: 705

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## siteSpecific()
- 位置: L27-34
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._siteSpecificPref === undefined)` → `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## FullZoom_init()
- 位置: L46-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`, `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `gBrowser.addEventListener()`, `this._cps2.addObserverForName()`, `this._initialLocations.has()`, `window.addEventListener()`
- 条件付き依存: `if (this._initialLocations.has(browser))` → `this.onLocationChange()`
- 条件付き依存: `if (this._initialLocations.has(browser))` → `this._initialLocations.get()`
- XPCOM: [`nsIContentPrefService2`](../../../../dom/interfaces/base/nsIContentPrefService2.idl.md) / `@mozilla.org/content-pref/service;1` → `ContentPrefService2` (toolkit/components/contentprefs/components.conf) / `Services.prefs`

## FullZoom_destroy()
- 位置: L77-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `gBrowser.removeEventListener()`, `this._cps2.removeObserverForName()`, `window.removeEventListener()`
- XPCOM: `Services.prefs`

## FullZoom_handleEvent()
- 位置: L89-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getTargetedBrowser()`, `this.enlarge()`, `this.reduce()`, `this.updateCommands()`

## observe()
- 位置: L107-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.updateCommands()`
- XPCOM: `Services.prefs`

## FullZoom_onContentPrefSet()
- 位置: L131-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onContentPrefChanged()`

## FullZoom_onContentPrefRemoved()
- 位置: L140-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onContentPrefChanged()`

## FullZoom__onContentPrefChanged()
- 位置: L156-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cps2.extractDomain()`, `this._cps2.getByDomainAndName()`, `this._getBrowserToken()`, `this._isPDFViewer()`, `this._loadContextFromBrowser()`
- 条件付き依存: `if (aGroup == domain && ctxt.usePrivateBrowsing == aIsPrivate)` → `this._applyPrefToZoom()`

## handleResult()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)

## handleCompletion()
- 位置: L196-200
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!hasPref && token.isCurrent)` → `this._applyPrefToZoom()`

## FullZoom_onLocationChange()
- 位置: L217-319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cps2.getByDomainAndName()`, `this._cps2.getCachedByDomainAndName()`, `this._getBrowserToken()`, `this._ignorePendingZoomAccesses()`, `this._isPDFViewer()`, `this._loadContextFromBrowser()`
- 条件付き依存: `if (this._initialLocations)` → `this._initialLocations.set()`
- 条件付き依存: `if (!aURI || (aIsTabSwitch && !this.siteSpecific))` → `this._notifyOnLocationChange()`
- 条件付き依存: `if ( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal )` → `this._applyPrefToZoom()`
- 条件付き依存: `if ( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal )` → `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (!( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal ))` → `this._applyPrefToZoom()`
- 条件付き依存: `if (!( !browser.contentPrincipal || browser.contentPrincipal.isNullPrincipal ))` → `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (!aIsTabSwitch && browser.isSyntheticDocument)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (!aIsTabSwitch && browser.isSyntheticDocument)` → `this._notifyOnLocationChange()`
- 条件付き依存: `if (this._isPDFViewer(browser))` → `this._applyPrefToZoom()`
- 条件付き依存: `if (this._isPDFViewer(browser))` → `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (pref)` → `this._applyPrefToZoom()`
- 条件付き依存: `if (pref)` → `this._notifyOnLocationChange.bind()`

## handleResult()
- 位置: L304-306
- 役割: (未記入)
- 触るとき: (未記入)

## handleCompletion()
- 位置: L307-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._applyPrefToZoom()`, `this._notifyOnLocationChange.bind()`
- 条件付き依存: `if (!token.isCurrent)` → `this._notifyOnLocationChange()`

## FullZoom_updateCommands()
- 位置: async L334-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomUI.getGlobalValue()`, `document.getElementById()`, `fullZoomCmd.toggleAttribute()`
- 条件付き依存: `if (zoomLevel == ZoomManager.MIN)` → `reduceCmd.setAttribute()`
- 条件付き依存: `if (!(zoomLevel == ZoomManager.MIN))` → `reduceCmd.removeAttribute()`
- 条件付き依存: `if (zoomLevel == ZoomManager.MAX)` → `enlargeCmd.setAttribute()`
- 条件付き依存: `if (!(zoomLevel == ZoomManager.MAX))` → `enlargeCmd.removeAttribute()`
- 条件付き依存: `if (zoomLevel == defaultZoomLevel && !forceResetEnabled)` → `resetCmd.setAttribute()`
- 条件付き依存: `if (!(zoomLevel == defaultZoomLevel && !forceResetEnabled))` → `resetCmd.removeAttribute()`

## sendMessageToPDFViewer()
- 位置: L366-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.sendMessageToActor()`, `console.error()`

## reduce()
- 位置: async L382-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.currentURI.spec.startsWith()`
- 条件付き依存: `if (aBrowser.currentURI.spec.startsWith("about:reader"))` → `aBrowser.sendMessageToActor()`
- 条件付き依存: `if (!(aBrowser.currentURI.spec.startsWith("about:reader")))` → `this._isPDFViewer()`
- 条件付き依存: `if (this._isPDFViewer(aBrowser))` → `this.sendMessageToPDFViewer()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `ZoomManager.reduceForBrowser()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._ignorePendingZoomAccesses()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._applyZoomToPref()`

## enlarge()
- 位置: async L402-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.currentURI.spec.startsWith()`
- 条件付き依存: `if (aBrowser.currentURI.spec.startsWith("about:reader"))` → `aBrowser.sendMessageToActor()`
- 条件付き依存: `if (!(aBrowser.currentURI.spec.startsWith("about:reader")))` → `this._isPDFViewer()`
- 条件付き依存: `if (this._isPDFViewer(aBrowser))` → `this.sendMessageToPDFViewer()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `ZoomManager.enlargeForBrowser()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._ignorePendingZoomAccesses()`
- 条件付き依存: `if (!(this._isPDFViewer(aBrowser)))` → `this._applyZoomToPref()`

## setZoom()
- 位置: L418-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomManager.setZoomForBrowser()`, `this._applyZoomToPref()`, `this._ignorePendingZoomAccesses()`, `this._isPDFViewer()`

## FullZoom_reset()
- 位置: L433-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomUI.getGlobalValue()`, `ZoomUI.getGlobalValue().then()`, `browser.currentURI.spec.startsWith()`, `this._getBrowserToken()`, `this._removePref()`
- 条件付き依存: `if (browser.currentURI.spec.startsWith("about:reader"))` → `browser.sendMessageToActor()`
- 条件付き依存: `if (!(browser.currentURI.spec.startsWith("about:reader")))` → `this._isPDFViewer()`
- 条件付き依存: `if (this._isPDFViewer(browser))` → `this.sendMessageToPDFViewer()`
- 条件付き依存: `if (token.isCurrent)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (token.isCurrent)` → `this._ignorePendingZoomAccesses()`

## resetFromURLBar()
- 位置: L457-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.reset()`, `this.resetScalingZoom()`

## FullZoom_resetScaling()
- 位置: L462-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.browsingContext?.resetScalingZoom()`

## FullZoom__applyPrefToZoom()
- 位置: L491-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomUI.getGlobalValue()`, `ZoomUI.getGlobalValue().then()`, `this._executeSoon()`, `this._getBrowserToken()`
- 条件付き依存: `if ( !aBrowser.mInitialized || aBrowser.isSyntheticDocument || (!this.siteSpecific && aBrowser.tabHasCustomZoom) )` → `this._executeSoon()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `this._ensureValid()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `this._ignorePendingZoomAccesses()`
- 条件付き依存: `if (aValue !== undefined && this.siteSpecific)` → `this._executeSoon()`
- 条件付き依存: `if (token.isCurrent)` → `ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (token.isCurrent)` → `this._ignorePendingZoomAccesses()`

## FullZoom__applyZoomToPref()
- 位置: L534-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomManager.getZoomForBrowser()`, `this._cps2.set()`, `this._loadContextFromBrowser()`

## handleCompletion()
- 位置: L550-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## FullZoom__removePref()
- 位置: L564-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cps2.removeByDomainAndName()`, `this._loadContextFromBrowser()`

## handleCompletion()
- 位置: L570-572
- 役割: (未記入)
- 触るとき: (未記入)

## FullZoom__getBrowserToken()
- 位置: L590-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `map.get()`, `map.has()`
- 条件付き依存: `if (!map.has(browser))` → `map.set()`

## isCurrent()
- 位置: L597-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `map.get()`

## FullZoom__getTargetedBrowser()
- 位置: L614-636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.XULElement.isInstance()`

## FullZoom__ignorePendingZoomAccesses()
- 位置: L645-650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `map.get()`, `map.set()`

## FullZoom__ensureValid()
- 位置: L652-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNaN()`

## FullZoom__loadContextFromBrowser()
- 位置: L676-678
- 役割: (未記入)
- 触るとき: (未記入)

## FullZoom__notifyOnLocationChange()
- 位置: L686-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this._executeSoon()`
- XPCOM: `Services.obs`

## FullZoom__executeSoon()
- 位置: L692-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`
- XPCOM: `Services.tm`

## _isPDFViewer()
- 位置: L699-703
- 役割: (未記入)
- 触るとき: (未記入)
