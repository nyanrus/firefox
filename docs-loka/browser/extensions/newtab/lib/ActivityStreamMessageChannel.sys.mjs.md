# browser/extensions/newtab/lib/ActivityStreamMessageChannel.sys.mjs

source: browser/extensions/newtab/lib/ActivityStreamMessageChannel.sys.mjs
source-hash: 4fedd6ab8df69db5367234b92bb1f4bc61915d83
lines: 406

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## dispatch()
- 位置: L21-25
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.type`

## ActivityStreamMessageChannel.constructor()
- 位置: L44-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.middleware.bind()`, `this.onMessage.bind()`, `this.onNewTabInit.bind()`, `this.onNewTabLoad.bind()`, `this.onNewTabUnload.bind()`
- 参照: `this._renderLayersListeners`, `this.middleware`, `this.onMessage`, `this.onNewTabInit`, `this.onNewTabLoad`, `this.onNewTabUnload`

## ActivityStreamMessageChannel.loadedTabs()
- 位置: L60-63
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AboutNewTabParent?.loadedTabs`

## ActivityStreamMessageChannel.middleware()
- 位置: L71-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.isSendToOneContent()`
- 条件付き依存: `if (au.isSendToOneContent(action))` → `this.send()`
- 条件付き依存: `if (!(au.isSendToOneContent(action)))` → `au.isBroadcastToContent()`
- 条件付き依存: `if (au.isBroadcastToContent(action))` → `this.broadcast()`
- 条件付き依存: `if (!(au.isBroadcastToContent(action)))` → `au.isSendToPreloaded()`
- 条件付き依存: `if (au.isSendToPreloaded(action))` → `this.sendToPreloaded()`
- 条件付き依存: `if (!skipMain)` → `next()`
- 参照: `action.meta`, `action.meta.skipMain`

## ActivityStreamMessageChannel.onActionFromContent()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`, `this.dispatch()`, `this.validatePortID()`

## ActivityStreamMessageChannel.broadcast()
- 位置: L103-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `lazy.AboutHomeStartupCache.onPreloadedNewTabMessage()`, `this.loadedTabs.values()`
- 参照: `this.outgoingMessageName`

## ActivityStreamMessageChannel.send()
- 位置: L122-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.sendAsyncMessage()`, `this.getTargetById()`
- 参照: `action.meta`, `action.meta.toTarget`, `this.outgoingMessageName`

## ActivityStreamMessageChannel.validatePortID()
- 位置: L136-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `id.includes()`
- 条件付き依存: `if (typeof id !== "string" || !id.includes(":"))` → `console.error()`

## ActivityStreamMessageChannel.getTargetById()
- 位置: L150-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadedTabs.values()`, `this.validatePortID()`

## ActivityStreamMessageChannel.sendToPreloaded()
- 位置: L166-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutHomeStartupCache.onPreloadedNewTabMessage()`, `this.getPreloadedActors()`
- 条件付き依存: `if (preloadedActors && action.data)` → `preloadedActor.sendAsyncMessage()`
- 参照: `action.data`, `this.outgoingMessageName`

## ActivityStreamMessageChannel.getPreloadedActors()
- 位置: L190-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isPreloadedBrowser()`, `this.loadedTabs.values()`
- 条件付き依存: `if (this.isPreloadedBrowser(browser))` → `preloadedActors.push()`
- 参照: `preloadedActors.length`

## ActivityStreamMessageChannel.isPreloadedBrowser()
- 位置: L208-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getAttribute()`

## ActivityStreamMessageChannel.simulateMessagesForExistingTabs()
- 位置: L212-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTabParent.flushQueuedMessagesFromContent()`, `this.loadedTabs.values()`, `this.onActionFromContent()`
- 条件付き依存: `if (loadedTab.loaded)` → `this.tabLoaded()`
- 参照: `at.NEW_TAB_INIT`, `loadedTab.actor`, `loadedTab.browser`, `loadedTab.browsingContext`, `loadedTab.loaded`, `loadedTab.portID`, `loadedTab.url`

## ActivityStreamMessageChannel.onNewTabInit()
- 位置: L255-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onActionFromContent()`
- 参照: `at.NEW_TAB_INIT`, `msg.data.portID`

## ActivityStreamMessageChannel.onNewTabLoad()
- 位置: L271-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabLoaded()`

## ActivityStreamMessageChannel.setRenderLayers()
- 位置: L275-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isPreloadedBrowser()`
- 参照: `browser.documentGlobal`, `browser.renderLayers`, `win.STATE_MINIMIZED`, `win.closed`, `win.isFullyOccluded`, `win.windowState`

## ActivityStreamMessageChannel.tabLoaded()
- 位置: L294-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._renderLayersListeners.has()`, `this.isPreloadedBrowser()`, `this.onActionFromContent()`, `this.setRenderLayers()`
- 条件付き依存: `if ( this.isPreloadedBrowser(browser) && !this._renderLayersListeners.has(browser) )` → `win.addEventListener()`
- 条件付き依存: `if ( this.isPreloadedBrowser(browser) && !this._renderLayersListeners.has(browser) )` → `this._renderLayersListeners.set()`
- 参照: `at.NEW_TAB_LOAD`, `browser.documentGlobal`, `tabDetails.loaded`, `tabDetails.portID`

## onSizeModeChange()
- 位置: L305-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserRef.deref()`
- 条件付き依存: `if (b)` → `this.setRenderLayers()`

## onOcclusionStateChange()
- 位置: L311-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserRef.deref()`
- 条件付き依存: `if (b)` → `this.setRenderLayers()`

## cleanup()
- 位置: L318-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserRef.deref()`, `w?.removeEventListener()`
- 条件付き依存: `if (b)` → `this._renderLayersListeners.delete()`
- 参照: `b?.documentGlobal`

## ActivityStreamMessageChannel.onNewTabUnload()
- 位置: L350-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._renderLayersListeners.get()`, `this.onActionFromContent()`
- 条件付き依存: `if (win && !win.closed)` → `win.removeEventListener()`
- 条件付き依存: `if (listeners)` → `this._renderLayersListeners.delete()`
- 参照: `at.NEW_TAB_UNLOAD`, `browser.documentGlobal`, `tabDetails.portID`, `win.closed`

## ActivityStreamMessageChannel.onMessage()
- 位置: L385-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.onActionFromContent()`
- 条件付き依存: `if (!msg.data || !msg.data.type)` → `console.error()`
- 参照: `action._target`, `msg.data`, `msg.data.type`, `tabDetails.browser`, `tabDetails.browser.documentGlobal`, `tabDetails.portID`
