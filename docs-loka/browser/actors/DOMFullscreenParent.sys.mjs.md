# browser/actors/DOMFullscreenParent.sys.mjs

source: browser/actors/DOMFullscreenParent.sys.mjs
source-hash: 3ec1dc8cfa3ae53e7786a66cd3b3130217ec14b5
lines: 374

## <module>
- 役割: (未記入)

## DOMFullscreenParent.updateFullscreenWindowReference()
- 位置: L20-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.documentElement.hasAttribute()`
- 参照: `this._fullscreenWindow`

## DOMFullscreenParent.cleanupDomFullscreen()
- 位置: L28-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.FullScreen.cleanupDomFullscreen()`
- 条件付き依存: `if ( !aWindow.FullScreen.cleanupDomFullscreen(this) && !aWindow.document.fullscreen )` → `Services.obs.notifyObservers()`
- 参照: `aWindow.FullScreen`, `aWindow.document.fullscreen`
- XPCOM: `Services.obs`

## DOMFullscreenParent._cleanupFullscreenStateAndResumeChromeUI()
- 位置: L50-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cleanupDomFullscreen()`
- 条件付き依存: `if (this.requestOrigin == this && aWindow.document.fullscreen)` → `aWindow.windowUtils.remoteFrameFullscreenReverted()`
- 参照: `aWindow.document.fullscreen`, `this.requestOrigin`

## DOMFullscreenParent.didDestroy()
- 位置: L57-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateFullscreenWindowReference()`, `window.document.documentElement.hasAttribute()`
- 条件付き依存: `if ( this.waitingForChildExitFullscreen || this.waitingForChildEnterFullscreen )` → `this._cleanupFullscreenStateAndResumeChromeUI()`
- 条件付き依存: `if (this != this.requestOrigin)` → `this.removeListeners()`
- 条件付き依存: `if (window.document.fullscreen)` → `window.document.exitFullscreen().catch()`
- 条件付き依存: `if (window.document.fullscreen)` → `window.document.exitFullscreen()`
- 条件付き依存: `if (this.waitingForChildEnterFullscreen)` → `this.cleanupDomFullscreen()`
- 条件付き依存: `if (window.document.documentElement.hasAttribute("inDOMFullscreen"))` → `this.cleanupDomFullscreen()`
- 条件付き依存: `if (window.windowUtils)` → `window.windowUtils.remoteFrameFullscreenReverted()`
- 条件付き依存: `if (this.waitingForChildExitFullscreen)` → `this._cleanupFullscreenStateAndResumeChromeUI()`
- 参照: `browser.documentGlobal`, `this._didDestroy`, `this._fullscreenWindow`, `this.browsingContext.top`, `this.requestOrigin`, `this.waitingForChildEnterFullscreen`, `this.waitingForChildExitFullscreen`, `topBrowsingContext.embedderElement`, `window.document.fullscreen`, `window.windowUtils`

## DOMFullscreenParent.receiveMessage()
- 位置: L121-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.fullscreen.change.stopAndAccumulate()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `this.addListeners()`, `this.cleanupDomFullscreen()`, `this.sendAsyncMessage()`, `this.updateFullscreenWindowReference()`, `window.FullScreen.enterDomFullscreen()`, `window.windowUtils.remoteFrameFullscreenChanged()`, `window.windowUtils.remoteFrameFullscreenReverted()`
- 条件付き依存: `if (window.document.fullscreen)` → `window.PointerlockFsWarning.showFullScreen()`
- 条件付き依存: `if (window.document.fullscreenKeyboardLock != newLock)` → `this.manager.updateFullscreenKeyboardLockStatus()`
- 条件付き依存: `if (window.document.fullscreenKeyboardLock != newLock)` → `window.PointerlockFsWarning.close()`
- 条件付き依存: `if (window.document.fullscreenKeyboardLock != newLock)` → `window.PointerlockFsWarning.showFullScreen()`
- 参照: `aMessage.data.fullscreenKeyboardLock`, `aMessage.name`, `browser.documentGlobal`, `this.browsingContext`, `this.browsingContext.top`, `this.fullscreenKeyboardLock`, `this.manager.fullscreen`, `this.nextMsgRecipient`, `this.requestOrigin`, `this.timerId`, `this.waitingForChildEnterFullscreen`, `this.waitingForChildExitFullscreen`, `topBrowsingContext.embedderElement`, `window.document.fullscreen`, `window.document.fullscreenKeyboardLock`
- XPCOM: `Services.obs` / `Services.prefs`

## DOMFullscreenParent.handleEvent()
- 位置: L217-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.fullscreen.change.start()`, `this.cleanupDomFullscreen()`, `this.hasBeenDestroyed()`, `this.updateFullscreenWindowReference()`, `window.FullScreen.enterDomFullscreen()`, `window.browsingContext.fullscreenRequestOrigin?.get()`
- 条件付き依存: `if (this != requestOrigin)` → `this.removeListeners()`
- 条件付き依存: `if (window.gXPInstallObserver)` → `window.gXPInstallObserver.removeAllNotifications()`
- 条件付き依存: `if (!this.hasBeenDestroyed() && this.requestOrigin)` → `window.PointerlockFsWarning.showFullScreen()`
- 条件付き依存: `if (!this.manager.fullscreen)` → `this.removeListeners()`
- 参照: `aEvent.currentTarget`, `aEvent.target`, `aEvent.target.documentGlobal`, `aEvent.target.documentGlobal.docShell.chromeEventHandler`, `aEvent.type`, `browser.documentGlobal.document.fullscreenKeyboardLock`, `this.manager.fullscreen`, `this.requestOrigin`, `this.requestOrigin.browsingContext`, `this.timerId`, `window.document.fullscreenKeyboardLock`, `window.gXPInstallObserver`

## DOMFullscreenParent.addListeners()
- 位置: L297-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.addEventListener()`

## DOMFullscreenParent.removeListeners()
- 位置: L319-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.removeEventListener()`

## DOMFullscreenParent.requestOrigin()
- 位置: L333-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestOrigin.get()`
- 参照: `chromeBC?.fullscreenRequestOrigin`, `this.browsingContext.topChromeWindow?.browsingContext`

## DOMFullscreenParent.requestOrigin()
- 位置: L344-356
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!chromeBC)` → `console.error()`
- 条件付き依存: `if (aActor)` → `Cu.getWeakReference()`
- 参照: `chromeBC.fullscreenRequestOrigin`, `this.browsingContext.topChromeWindow?.browsingContext`

## DOMFullscreenParent.hasBeenDestroyed()
- 位置: L358-372
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._didDestroy`, `this.browsingContext`
