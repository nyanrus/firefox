# browser/modules/ASWebAuthSessionService.sys.mjs

source: browser/modules/ASWebAuthSessionService.sys.mjs
source-hash: c63282b72a61bd67a4457e7283e3fa46039c0d9f
lines: 677

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `Components.ID()`

## ASWebAuthSession.constructor()
- 位置: L20-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.browser`, `this.callbackScheme`, `this.completed`, `this.hasCallback`, `this.headers`, `this.observingHeaders`, `this.request`, `this.service`, `this.trackedBrowsers`, `this.userContextId`, `this.uuid`, `this.window`

## ASWebAuthSession.start()
- 位置: L48-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addHeaderObserver()`, `this.service.activeSessions.set()`, `this.window.addEventListener()`, `this.window.gBrowser.tabContainer.addEventListener()`
- 参照: `this.uuid`

## ASWebAuthSession.cleanup()
- 位置: L55-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeHeaderObserver()`
- 条件付き依存: `if (this.window?.gBrowser)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this.window && !this.window.closed)` → `this.window.removeEventListener()`
- 条件付き依存: `if (this.userContextId)` → `lazy.ContextualIdentityService.remove()`
- 参照: `this.userContextId`, `this.window`, `this.window.closed`, `this.window?.gBrowser`

## ASWebAuthSession.finish()
- 位置: L72-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cleanup()`, `this.service.activeSessions.delete()`
- 条件付き依存: `if (closeWindow && this.window && !this.window.closed)` → `this.window.close()`
- 参照: `this.uuid`, `this.window`, `this.window.closed`

## ASWebAuthSession.complete()
- 位置: L84-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.finish()`, `this.request.complete()`
- 参照: `this.completed`

## ASWebAuthSession.cancel()
- 位置: L97-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.finish()`, `this.request.cancel()`
- 参照: `this.completed`

## ASWebAuthSession.handleEvent()
- 位置: L107-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onTabClose()`, `this.onWindowUnload()`
- 参照: `event.type`

## ASWebAuthSession.observe()
- 位置: L118-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `channel.getRequestHeader()`, `channel.setRequestHeader()`, `subject.QueryInterface()`, `this.hasBrowser()`, `this.removeHeaderObserver()`
- 参照: `Ci.nsIHttpChannel`, `bc.top`, `bc?.top?.embedderElement`, `channel.isDocument`, `channel.loadInfo?.browsingContext`, `this.headers`
- XPCOM: [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## ASWebAuthSession.onTabClose()
- 位置: L150-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasOpenTrackedBrowser()`, `this.trackedBrowsers.delete()`
- 条件付き依存: `if ( !this.completed && (browser === this.browser || !this.hasOpenTrackedBrowser()) )` → `this.cancel()`
- 参照: `event.target.linkedBrowser`, `this.browser`, `this.completed`

## ASWebAuthSession.onWindowUnload()
- 位置: L164-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.service.activeSessions.get()`
- 条件付き依存: `if (this.service.activeSessions.get(this.uuid) === this)` → `this.cancel()`
- 参照: `this.uuid`

## ASWebAuthSession.addHeaderObserver()
- 位置: L170-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Services.obs.addObserver()`
- 参照: `Object.keys(this.headers).length`, `this.headers`, `this.observingHeaders`
- XPCOM: `Services.obs`

## ASWebAuthSession.removeHeaderObserver()
- 位置: L179-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.observingHeaders`
- XPCOM: `Services.obs`

## ASWebAuthSession.trackBrowserIfInSessionWindow()
- 位置: L188-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasBrowser()`
- 条件付き依存: `if (this.hasBrowser(browser))` → `this.trackedBrowsers.add()`

## ASWebAuthSession.hasOpenTrackedBrowser()
- 位置: L194-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window?.gBrowser?.getTabForBrowser()`
- 参照: `tab.closing`, `this.trackedBrowsers`

## ASWebAuthSession.hasBrowser()
- 位置: L204-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window?.gBrowser?.getTabForBrowser()`
- 参照: `browser?.documentGlobal`, `this.window`

## ASWebAuthSession.ownsBrowsingContext()
- 位置: L211-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasBrowser()`, `visited.add()`, `visited.has()`
- 参照: `bc?.top`, `opener?.top`, `top.crossGroupOpener`, `top.embedderElement`, `top.opener`

## ASWebAuthSessionService.constructor()
- 位置: L227-236
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.activeSessions`, `this.initialized`, `this.pendingSetups`, `this.progressListener`

## onLocationChange()
- 位置: L233-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onLocationChange()`

## ASWebAuthSessionService.init()
- 位置: L238-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `lazy.EveryWindow.registerCallback()`, `win?.gBrowser?.addTabsProgressListener()`, `win?.gBrowser?.removeTabsProgressListener()`
- 参照: `this.initialized`, `this.progressListener`
- XPCOM: `Services.obs`

## ASWebAuthSessionService.uninit()
- 位置: L260-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Services.obs.notifyObservers()`, `Services.obs.removeObserver()`, `lazy.EveryWindow.unregisterCallback()`, `session.cancel()`, `this.activeSessions.values()`, `this.pendingSetups.clear()`, `this.pendingSetups.values()`
- 条件付き依存: `if (!pending.cancelled)` → `pending.request.cancel()`
- 参照: `pending.cancelled`, `this.initialized`
- XPCOM: `Services.obs`

## ASWebAuthSessionService.removeLeftoverEphemeralContainers()
- 位置: async L294-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `identity.name.slice()`, `identity.name?.startsWith()`, `lazy.ContextualIdentityService.getPublicIdentities()`, `lazy.ContextualIdentityService.load()`, `lazy.ContextualIdentityService.remove()`, `this.activeSessions.has()`, `this.pendingSetups.has()`
- 参照: `EPHEMERAL_CONTAINER_PREFIX.length`, `identity.userContextId`

## ASWebAuthSessionService.observe()
- 位置: L312-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this.onBegin()`, `this.onCancel()`, `this.onExamineResponse()`
- XPCOM: `Services.obs`

## ASWebAuthSessionService.shouldLoadCallback()
- 位置: L329-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `contentLocation.scheme?.toLowerCase()`, `this.activeSessions.get()`, `this.findSessionForCallbackScheme()`
- 条件付き依存: `if (this.activeSessions.get(session.uuid) === session)` → `session.complete()`
- 参照: `Ci.nsIContentPolicy.ACCEPT`, `Ci.nsIContentPolicy.REJECT_POLICY`, `Ci.nsIContentPolicy.TYPE_DOCUMENT`, `Ci.nsIContentPolicy.TYPE_SUBDOCUMENT`, `contentLocation.spec`, `loadInfo.browsingContext`, `loadInfo.externalContentPolicyType`, `session.uuid`, `this.activeSessions.size`
- XPCOM: [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md) / `Services.tm`

## ASWebAuthSessionService.onExamineResponse()
- 位置: L369-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.tm.dispatchToMainThread()`, `channel.cancel()`, `channel.getResponseHeader()`, `subject.QueryInterface()`, `this.activeSessions.get()`, `this.findSessionForCallbackScheme()`
- 条件付き依存: `if (this.activeSessions.get(session.uuid) === session)` → `session.complete()`
- 参照: `Ci.nsIHttpChannel`, `Cr.NS_BINDING_ABORTED`, `bc.top`, `channel.isDocument`, `channel.loadInfo?.browsingContext`, `channel.responseStatus`, `locationUri.scheme`, `session.uuid`, `this.activeSessions.size`
- XPCOM: [`nsIHttpChannel`](../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `Services.io` / `Services.tm`

## ASWebAuthSessionService.onLocationChange()
- 位置: L420-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `location.scheme?.toLowerCase()`, `session.trackBrowserIfInSessionWindow()`, `this.activeSessions.get()`, `this.findSessionForCallbackScheme()`
- 条件付き依存: `if (scheme === "https" || scheme === "http")` → `this.activeSessions.values()`
- 条件付き依存: `if (scheme === "https" || scheme === "http")` → `session.ownsBrowsingContext()`
- 条件付き依存: `if (session.hasCallback && session.ownsBrowsingContext(bc))` → `session.trackBrowserIfInSessionWindow()`
- 条件付き依存: `if (session.hasCallback && session.ownsBrowsingContext(bc))` → `session.request.matchesCallbackURL()`
- 条件付き依存: `if (session.request.matchesCallbackURL(location.spec))` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (session.request.matchesCallbackURL(location.spec))` → `this.activeSessions.get()`
- 条件付き依存: `if (this.activeSessions.get(session.uuid) === session)` → `session.complete()`
- 参照: `location.spec`, `session.hasCallback`, `session.uuid`, `this.activeSessions.size`, `webProgress.browsingContext`, `webProgress?.isTopLevel`
- XPCOM: `Services.tm`

## ASWebAuthSessionService.findSessionForCallbackScheme()
- 位置: L464-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `session.ownsBrowsingContext()`, `this.activeSessions.values()`
- 参照: `session.callbackScheme`

## ASWebAuthSessionService.waitForWindowClosed()
- 位置: L476-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ww.registerNotification()`
- 条件付き依存: `if (!win || win.closed)` → `Promise.resolve()`
- 条件付き依存: `if (win.closed)` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (win.closed)` → `resolve()`
- 参照: `win.closed`
- XPCOM: `Services.ww`

## windowCloseObserver()
- 位置: L482-487
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "domwindowclosed" && subject === win)` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (topic === "domwindowclosed" && subject === win)` → `resolve()`
- XPCOM: `Services.ww`

## ASWebAuthSessionService.observeNextWindowOpen()
- 位置: L497-513
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.ww.registerNotification()`
- XPCOM: `Services.ww`

## windowOpenObserver()
- 位置: L499-504
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "domwindowopened")` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (topic === "domwindowopened")` → `resolve()`
- XPCOM: `Services.ww`

## ASWebAuthSessionService.unregister()
- 位置: L509-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ww.unregisterNotification()`
- XPCOM: `Services.ww`

## ASWebAuthSessionService.openAuthWindow()
- 位置: async L515-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `Promise.withResolvers()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.URILoadingHelper.openWebLinkIn()`, `openedWindow.unregister()`, `this.observeNextWindowOpen()`, `this.waitForWindowClosed()`, `this.waitForWindowClosed(win).then()`
- 参照: `Services.appShell.hiddenDOMWindow`, `browser?.documentGlobal`, `openedWindow.promise`
- XPCOM: `Services.appShell`

## ASWebAuthSessionService.cleanupFailedSetup()
- 位置: L555-565
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.remove()`
- 条件付き依存: `if (win && !win.closed)` → `win.close()`
- 条件付き依存: `if (!pending.cancelled)` → `pending.request.cancel()`
- 参照: `pending.cancelled`, `win.closed`

## ASWebAuthSessionService.onBegin()
- 位置: async L567-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `console.error()`, `request.QueryInterface()`, `request.callbackScheme.toLowerCase()`, `request.getAdditionalHeader()`, `session.start()`, `this.cleanupFailedSetup()`, `this.openAuthWindow()`, `this.pendingSetups.delete()`, `this.pendingSetups.set()`, `win.focus()`
- 条件付き依存: `if (!uuid || parsedURL?.protocol !== "https:")` → `request.cancel()`
- 条件付き依存: `if (ephemeral)` → `lazy.ContextualIdentityService.create()`
- 条件付き依存: `if (!result.browser || win.closed || pending.cancelled)` → `this.cleanupFailedSetup()`
- 参照: `Ci.nsIASWebAuthSessionRequest`, `container.userContextId`, `lazy.SessionStore.promiseAllWindowsRestored`, `parsedURL.href`, `parsedURL?.protocol`, `pending.cancelled`, `request.additionalHeaderNames`, `request.hasCallback`, `request.url`, `request.useEphemeralSession`, `request.uuid`, `result.browser`, `result.win`, `win.closed`
- XPCOM: [`nsIASWebAuthSessionRequest`](../../toolkit/xre/nsIASWebAuthSessionRequest.idl.md)

## ASWebAuthSessionService.onCancel()
- 位置: L640-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.activeSessions.get()`, `this.pendingSetups.get()`
- 条件付き依存: `if (session)` → `session.cancel()`
- 条件付き依存: `if (pending && !pending.cancelled)` → `pending.request.cancel()`
- 参照: `pending.cancelled`

## ASWebAuthSessionCallbackContentPolicy()
- 位置: L657-657
- 役割: (未記入)
- 触るとき: (未記入)

## shouldLoad()
- 位置: L666-671
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASWebAuthSessionService.shouldLoadCallback()`

## shouldProcess()
- 位置: L673-675
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIContentPolicy.ACCEPT`
- XPCOM: [`nsIContentPolicy`](../../dom/base/nsIContentPolicy.idl.md)
