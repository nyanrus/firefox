# browser/modules/WindowsPreviewPerTab.sys.mjs

source: browser/modules/WindowsPreviewPerTab.sys.mjs
source-hash: 3e9ffc410fef92bc682dc94b949f20ce7f009822
lines: 891

## <module>
- 役割: (未記入)
- 呼び出し先: `AeroPeek.initialize()`, `Cc["@mozilla.org/timer;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyServiceGetter()`

## _imageFromURI()
- 位置: L71-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/thread-manager;1"].getService()`, `Components.isSuccessCode()`, `NetUtil.asyncFetch()`, `NetUtil.newChannel()`, `channel.QueryInterface()`, `channel.setPrivate()`, `defaultURI.equals()`, `lazy.imgTools.decodeImageAsync()`
- 条件付き依存: `if (!defaultURI.equals(uri))` → `_imageFromURI()`
- 参照: `Ci.nsIContentPolicy.TYPE_INTERNAL_IMAGE`, `Ci.nsIPrivateBrowsingChannel`, `PlacesUtils.favicons.defaultFavicon`, `channel.contentType`, `threadManager.currentThread`
- XPCOM: [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md) / [`nsIPrivateBrowsingChannel`](../../netwerk/base/nsIPrivateBrowsingChannel.idl.md) / `@mozilla.org/thread-manager;1`

## onImageReady()
- 位置: L90-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`
- 条件付き依存: `if (!image)` → `defaultURI.equals()`
- 条件付き依存: `if (!defaultURI.equals(uri))` → `_imageFromURI()`
- 参照: `PlacesUtils.favicons.defaultFavicon`

## getFaviconAsImage()
- 位置: L125-131
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (iconurl)` → `_imageFromURI()`
- 条件付き依存: `if (iconurl)` → `NetUtil.newURI()`
- 条件付き依存: `if (!(iconurl))` → `_imageFromURI()`
- 参照: `PlacesUtils.favicons.defaultFavicon`

## PreviewController()
- 位置: L150-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `lazy.PageThumbs.createCanvas()`, `this.tab.addEventListener()`, `this.win.createTabPreview()`
- 参照: `canvas.mozOpaque`, `tab.linkedBrowser`, `this.linkedBrowser`, `this.preview`, `this.tab`, `this.win`, `this.win.win`

## destroy()
- 位置: L168-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tab.removeEventListener()`
- 参照: `this.preview`, `this.win`

## wrappedJSObject()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)

## resetCanvasPreview()
- 位置: L182-185
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.canvasPreview.height`, `this.canvasPreview.width`

## resizeCanvasPreview()
- 位置: L190-193
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.canvasPreview.height`, `this.canvasPreview.width`

## browserDims()
- 位置: L195-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tab.linkedBrowser.getBoundingClientRect()`

## cacheBrowserDims()
- 位置: L199-203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dims.height`, `dims.width`, `this._cachedHeight`, `this._cachedWidth`, `this.browserDims`

## testCacheBrowserDims()
- 位置: L205-208
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dims.height`, `dims.width`, `this._cachedHeight`, `this._cachedWidth`, `this.browserDims`

## updateCanvasPreview()
- 位置: L214-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AeroPeek.resetCacheTimer()`, `lazy.PageThumbs.captureToCanvas()`, `lazy.PageThumbs.captureToCanvas( this.linkedBrowser, this.canvasPreview, { fullScale: aFullScale, } ).catch()`, `this.cacheBrowserDims()`
- 参照: `console.error`, `this.canvasPreview`, `this.linkedBrowser`

## updateTitleAndTooltip()
- 位置: L230-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.win.tabbrowser.getWindowTitleForBrowser()`
- 参照: `this.linkedBrowser`, `this.preview.title`, `this.preview.tooltip`

## width()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.width`

## height()
- 位置: L246-248
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.height`

## thumbnailAspectRatio()
- 位置: L250-257
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browserDims.height`, `browserDims.width`, `this.browserDims`

## requestPreview()
- 位置: L265-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTaskbarCallback.done()`, `composite.getContext()`, `ctx.drawImage()`, `ctx.drawWindow()`, `ctx.restore()`, `ctx.save()`, `ctx.scale()`, `lazy.PageThumbs.createCanvas()`, `this.resetCanvasPreview()`, `this.updateCanvasPreview()`, `this.updateCanvasPreview(true).then()`, `this.win.tabbrowser.previewTab()`
- 参照: `aPreviewCanvas.height`, `aPreviewCanvas.width`, `composite.height`, `composite.mozOpaque`, `composite.width`, `this.browserDims.x`, `this.browserDims.y`, `this.tab`, `this.win.height`, `this.win.width`, `this.win.win`, `this.win.win.devicePixelRatio`

## requestThumbnail()
- 位置: L318-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTaskbarCallback.done()`, `this.resizeCanvasPreview()`, `this.updateCanvasPreview()`, `this.updateCanvasPreview(false).then()`

## onClose()
- 位置: L327-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.win.tabbrowser.removeTab()`
- 参照: `this.tab`

## onActivate()
- 位置: L331-337
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tab`, `this.win.tabbrowser.selectedTab`

## handleEvent()
- 位置: L340-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateTitleAndTooltip()`
- 参照: `evt.type`

## TabWindow()
- 位置: L357-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AeroPeek.checkPreviewCount()`, `AeroPeek.windows.push()`, `this.newTab()`, `this.tabbrowser.addTabsProgressListener()`, `this.tabbrowser.tabContainer.addEventListener()`, `this.updateTabOrdering()`, `this.win.addEventListener()`
- 参照: `tabs.length`, `this.previews`, `this.tabEvents`, `this.tabEvents.length`, `this.tabbrowser`, `this.tabbrowser.tabs`, `this.win`, `this.winEvents`, `this.winEvents.length`, `win.gBrowser`

## destroy()
- 位置: L390-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AeroPeek.checkPreviewCount()`, `AeroPeek.windows.indexOf()`, `AeroPeek.windows.splice()`, `this.removeTab()`, `this.tabbrowser.removeTabsProgressListener()`, `this.tabbrowser.tabContainer.removeEventListener()`, `this.win.removeEventListener()`
- 参照: `tabs.length`, `this._destroying`, `this.tabEvents`, `this.tabEvents.length`, `this.tabbrowser.tabs`, `this.win.gTaskbarTabGroup`, `this.winEvents`, `this.winEvents.length`

## width()
- 位置: L414-416
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.innerWidth`

## height()
- 位置: L417-419
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.innerHeight`

## cacheDims()
- 位置: L421-424
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._cachedHeight`, `this._cachedWidth`, `this.height`, `this.width`

## testCacheDims()
- 位置: L426-428
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._cachedHeight`, `this._cachedWidth`, `this.height`, `this.width`

## newTab()
- 位置: L431-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AeroPeek.addPreview()`, `controller.updateTitleAndTooltip()`, `this.previews.set()`
- 参照: `controller.preview`

## createTabPreview()
- 位置: L441-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AeroPeek.taskbar.createTaskbarTabPreview()`, `tab.getAttribute()`, `this.updateFavicon()`
- 参照: `AeroPeek.enabled`, `preview.active`, `preview.visible`, `this.tabbrowser.selectedTab`, `this.win.docShell`

## removeTab()
- 位置: L455-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AeroPeek.removePreview()`, `preview.controller.wrappedJSObject.destroy()`, `preview.move()`, `this.previewFromTab()`, `this.previews.delete()`
- 参照: `preview.active`, `preview.visible`

## enabled()
- 位置: L466-468
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._enabled`

## enabled()
- 位置: L470-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `preview.move()`, `this.updateTabOrdering()`
- 参照: `preview.visible`, `this._enabled`, `this.previews`

## previewFromTab()
- 位置: L482-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previews.get()`

## updateTabOrdering()
- 位置: L486-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `inorder[i].move()`, `previews.has()`
- 条件付き依存: `if (previews.has(t))` → `inorder.push()`
- 条件付き依存: `if (previews.has(t))` → `previews.get()`
- 参照: `inorder.length`, `this.previews`, `this.tabbrowser.tabs`

## handleEvent()
- 位置: L509-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.newTab()`, `this.onResize()`, `this.previewFromTab()`, `this.removeTab()`, `this.updateTabOrdering()`
- 参照: `AeroPeek._prefenabled`, `evt.originalTarget`, `evt.type`, `this.previewFromTab(tab).active`

## setInvalidationTimer()
- 位置: L536-560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.testCacheBrowserDims()`, `this.invalidateTimer.cancel()`, `this.invalidateTimer.initWithCallback()`, `this.previews.forEach()`
- 条件付き依存: `if (!this.invalidateTimer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 条件付き依存: `if (!controller.testCacheBrowserDims())` → `controller.cacheBrowserDims()`
- 条件付き依存: `if (!controller.testCacheBrowserDims())` → `aPreview.invalidate()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `aPreview.controller.wrappedJSObject`, `this.invalidateTimer`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## onResize()
- 位置: L562-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cacheDims()`, `this.setInvalidationTimer()`, `this.testCacheDims()`

## invalidateTabPreview()
- 位置: L580-587
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aBrowser == tab.linkedBrowser)` → `preview.invalidate()`
- 参照: `tab.linkedBrowser`, `this.previews`

## onLocationChange()
- 位置: L591-595
- 役割: (未記入)
- 触るとき: (未記入)

## onStateChange()
- 位置: L597-604
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && aStateFlags & Ci.nsIWebProgressListener.STATE_IS_NETWORK )` → `this.invalidateTabPreview()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLinkIconAvailable()
- 位置: L606-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateFavicon()`, `this.win.gBrowser.getTabForBrowser()`

## updateFavicon()
- 位置: L610-647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `aTab.getAttribute()`, `getFaviconAsImage()`, `this.previews.get()`
- 条件付き依存: `if (aIconURL)` → `PlacesUtils.favicons.getFaviconLinkForIcon()`
- 条件付き依存: `if (aIconURL)` → `Services.io.newURI()`
- 参照: `PlacesUtils.favicons.getFaviconLinkForIcon( Services.io.newURI(aIconURL) ).spec`, `aTab.closing`, `aTab.linkedBrowser`, `preview.icon`, `this.win`, `this.win.closed`
- XPCOM: `Services.io`

## initialize()
- 位置: L680-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[WINTASKBAR_CONTRACTID].getService()`, `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`
- 参照: `Ci.nsIWinTaskbar`, `this._prefenabled`, `this.available`, `this.enabled`, `this.initialized`, `this.taskbar`, `this.taskbar.available`
- XPCOM: `nsIWinTaskbar` / `Services.prefs`

## destroy()
- 位置: L696-702
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.cacheTimer)` → `this.cacheTimer.cancel()`
- 参照: `this._enabled`, `this.cacheTimer`

## enabled()
- 位置: L704-706
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._enabled`

## enabled()
- 位置: L708-718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.windows.forEach()`
- 参照: `this._enabled`, `win.enabled`

## _prefenabled()
- 位置: L720-722
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.__prefenabled`

## _prefenabled()
- 位置: L724-735
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (enable)` → `this.enable()`
- 条件付き依存: `if (!(enable))` → `this.disable()`
- 参照: `this.__prefenabled`

## enable()
- 位置: L739-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (!this._observersAdded)` → `Services.prefs.addObserver()`
- 条件付き依存: `if (!this._observersAdded)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._observersAdded)` → `PlacesUtils.observers.addListener()`
- 条件付き依存: `if (this.initialized)` → `Services.wm.getEnumerator()`
- 条件付き依存: `if (!win.closed)` → `this.onOpenWindow()`
- 参照: `this._observersAdded`, `this._placesListener`, `this.cacheLifespan`, `this.initialized`, `this.maxpreviews`, `win.closed`
- XPCOM: `Services.prefs` / `Services.wm`

## disable()
- 位置: L769-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.observers.removeListener()`, `tabWinObject.destroy()`
- 参照: `tabWinObject.win.gTaskbarTabGroup`, `this._placesListener`, `this.windows`, `this.windows.length`

## addPreview()
- 位置: L783-786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.checkPreviewCount()`, `this.previews.push()`

## removePreview()
- 位置: L788-792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.checkPreviewCount()`, `this.previews.indexOf()`, `this.previews.splice()`

## checkPreviewCount()
- 位置: L794-799
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._prefenabled`, `this.enabled`, `this.maxpreviews`, `this.previews.length`

## onOpenWindow()
- 位置: L801-808
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._prefenabled`, `this.available`, `win.gTaskbarTabGroup`

## onCloseWindow()
- 位置: L810-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gTaskbarTabGroup.destroy()`
- 条件付き依存: `if (!this.windows.length)` → `this.destroy()`
- 参照: `this._prefenabled`, `this.available`, `this.windows.length`, `win.gTaskbarTabGroup`

## resetCacheTimer()
- 位置: L824-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cacheTimer.cancel()`, `this.cacheTimer.init()`
- 参照: `Ci.nsITimer.TYPE_ONE_SHOT`, `this.cacheLifespan`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md)

## observe()
- 位置: L834-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.resetCanvasPreview()`, `this.checkPreviewCount()`, `this.previews.forEach()`
- 条件付き依存: `if (aTopic == "nsPref:changed" && aData == TOGGLE_PREF_NAME)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (aData == DISABLE_THRESHOLD_PREF_NAME)` → `Services.prefs.getIntPref()`
- 参照: `preview.controller.wrappedJSObject`, `this._prefenabled`, `this.maxpreviews`
- XPCOM: `Services.prefs`

## handlePlacesEvents()
- 位置: L864-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.getAttribute()`
- 条件付き依存: `if (tab.getAttribute("image") == event.faviconUrl)` → `win.updateFavicon()`
- 参照: `event.faviconUrl`, `event.type`, `this.windows`, `win.previews`
