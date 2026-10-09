# browser/components/extensions/parent/ext-browser.js

source: browser/components/extensions/parent/ext-browser.js
source-hash: 6dec79782f28d055afed35514819ca02b0a51ce5
lines: 1357

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.assign()`, `defineLazyGetter()`, `extensions.on()`

## isPrivateTab()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `nativeTab.linkedBrowser`

## global.openOptionsPage()
- 位置: L69-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encodeURIComponent()`, `window.BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (!window)` → `Promise.reject()`
- 条件付き依存: `if (!optionsPageProperties)` → `Promise.reject()`
- 条件付き依存: `if (optionsPageProperties.open_in_tab)` → `window.switchToTabHavingURI()`
- 条件付き依存: `if (optionsPageProperties.open_in_tab)` → `Promise.resolve()`
- 参照: `extension.id`, `extension.principal`, `optionsPageProperties.open_in_tab`, `optionsPageProperties.page`, `windowTracker.topWindow`

## global.makeWidgetId()
- 位置: L98-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `id.replace()`, `id.toLowerCase()`

## global.clickModifiersFromEvent()
- 位置: L104-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(map) .filter()`, `Object.keys(map) .filter(key => event[key]) .map()`
- 条件付き依存: `if (event.ctrlKey && AppConstants.platform === "macosx")` → `modifiers.push()`
- 参照: `AppConstants.platform`, `event.ctrlKey`

## global.waitForTabLoaded()
- 位置: L122-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## onLocationChange()
- 位置: L125-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.documentGlobal.gBrowser.getTabForBrowser()`
- 条件付き依存: `if ( webProgress.isTopLevel && browser.documentGlobal.gBrowser.getTabForBrowser(browser) == tab && (!url || locationURI.spec == url) )` → `windowTracker.removeListener()`
- 条件付き依存: `if ( webProgress.isTopLevel && browser.documentGlobal.gBrowser.getTabForBrowser(browser) == tab && (!url || locationURI.spec == url) )` → `resolve()`
- 参照: `locationURI.spec`, `webProgress.isTopLevel`

## global.replaceUrlInTab()
- 位置: L139-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `gBrowser.loadURI()`, `waitForTabLoaded()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `uri.spec`
- XPCOM: [`nsIWebNavigation`](../../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## global.getExtTabGroupIdForInternalTabGroupId()
- 位置: L161-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^(\d{13})-(\d{1,3})$/.exec()`, `fallbackTabGroupIdMap.get()`
- 条件付き依存: `if (parsedTabId)` → `parseInt()`
- 条件付き依存: `if (parsedTabId)` → `Number.isSafeInteger()`
- 条件付き依存: `if (!fallbackGroupId)` → `fallbackTabGroupIdMap.set()`

## global.getInternalTabGroupIdForExtTabGroupId()
- 位置: L177-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isSafeInteger()`
- 条件付き依存: `if (Number.isSafeInteger(groupId) && groupId >= 1e15)` → `Math.floor()`

## constructor()
- 位置: L202-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `tabTracker.on()`, `this.tabAdopted.bind()`, `windowTracker.addListener()`
- 参照: `this.getDefaultPrototype`, `this.tabAdopted`, `this.tabData`

## get()
- 位置: L223-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabData.get()`, `this.tabData.has()`
- 条件付き依存: `if (!this.tabData.has(keyObject))` → `Object.create()`
- 条件付き依存: `if (!this.tabData.has(keyObject))` → `this.getDefaultPrototype()`
- 条件付き依存: `if (!this.tabData.has(keyObject))` → `this.tabData.set()`

## clear()
- 位置: L238-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabData.delete()`

## handleEvent()
- 位置: L242-248
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "TabSelect")` → `this.emit()`
- 参照: `event.target`, `event.type`

## onLocationChange()
- 位置: L250-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getTabForBrowser()`, `this.emit()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `browser.documentGlobal.gBrowser`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## tabAdopted()
- 位置: L276-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.get()`, `this.tabData.delete()`, `this.tabData.get()`, `this.tabData.has()`

## shutdown()
- 位置: L291-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.off()`, `windowTracker.removeListener()`
- 参照: `this.tabAdopted`

## WindowTracker.addProgressListener()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gBrowser.addTabsProgressListener()`

## WindowTracker.removeProgressListener()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gBrowser.removeTabsProgressListener()`

## WindowTracker.getTopNormalWindow()
- 位置: L315-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`
- 参照: `context.privateBrowsingAllowed`, `options.allowFromInactiveWorkspace`, `options.private`

## TabTracker.constructor()
- 位置: L328-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this._handleTabDestroyed.bind()`
- 参照: `this._deferredTabOpenEvents`, `this._handleTabDestroyed`, `this._nextId`, `this._tabIds`, `this._tabs`

## TabTracker.init()
- 位置: L339-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutReaderParent.addMessageListener()`, `this._handleWindowClose.bind()`, `this._handleWindowOpen.bind()`, `this.on()`, `windowTracker.addCloseListener()`, `windowTracker.addListener()`, `windowTracker.addOpenListener()`
- 参照: `this._handleTabDestroyed`, `this._handleWindowClose`, `this._handleWindowOpen`, `this.adoptedTabs`, `this.initialized`

## TabTracker.getId()
- 位置: L365-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabs.get()`, `this.init()`, `this.setId()`
- 参照: `this._nextId`

## TabTracker.getTabForBrowser()
- 位置: L378-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (browser.id === "addon-inline-options")` → `browser.documentGlobal.gBrowser.getTabForBrowser()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.docShell.chromeEventHandler`, `browser.id`

## TabTracker.setId()
- 位置: L392-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabIds.set()`, `this._tabs.set()`
- 参照: `nativeTab.documentGlobal.closed`, `nativeTab.parentNode`

## TabTracker.adopt()
- 位置: L414-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.adoptedTabs.add()`, `this.adoptedTabs.has()`, `this.emit()`, `this.getId()`, `this.has()`, `this.setId()`
- 条件付き依存: `if (this.has("tab-detached"))` → `windowTracker.getId()`
- 条件付き依存: `if (this.has("tab-detached"))` → `this.emit()`
- 条件付き依存: `if (this.has("tab-attached"))` → `windowTracker.getId()`
- 条件付き依存: `if (this.has("tab-attached"))` → `this.emit()`
- 参照: `nativeTab.documentGlobal`, `nativeTab.index`

## TabTracker._handleTabDestroyed()
- 位置: L449-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabs.get()`
- 条件付き依存: `if (id)` → `this._tabs.delete()`
- 条件付き依存: `if (id)` → `this._tabIds.get()`
- 条件付き依存: `if (this._tabIds.get(id) === nativeTab)` → `this._tabIds.delete()`

## TabTracker.getTab()
- 位置: L471-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tabIds.get()`

## TabTracker.setOpener()
- 位置: L490-506
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (openerTabId > -1)` → `tabTracker.getTab()`
- 条件付き依存: `if (nativeTab.openerTab !== nativeOpenerTab)` → `this.emit()`
- 参照: `nativeOpenerTab.ownerDocument`, `nativeTab.openerTab`, `nativeTab.ownerDocument`

## TabTracker.deferredForTabOpen()
- 位置: L508-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._deferredTabOpenEvents.get()`
- 条件付き依存: `if (!deferred)` → `Promise.withResolvers()`
- 条件付き依存: `if (!deferred)` → `this._deferredTabOpenEvents.set()`
- 条件付き依存: `if (!deferred)` → `deferred.promise.then()`
- 条件付き依存: `if (!deferred)` → `this._deferredTabOpenEvents.delete()`

## TabTracker.maybeWaitForTabOpen()
- 位置: async L520-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._deferredTabOpenEvents.get()`
- 参照: `deferred.promise`

## TabTracker.handleEvent()
- 位置: L530-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.adoptedTabs.has()`, `this.emitActivated()`, `this.has()`, `this.maybeWaitForTabOpen()`, `this.maybeWaitForTabOpen(nativeTab).then()`
- 条件付き依存: `if (adoptedTab)` → `this.adopt()`
- 条件付き依存: `if (!(adoptedTab))` → `this.deferredForTabOpen()`
- 条件付き依存: `if (!(adoptedTab))` → `Promise.resolve().then()`
- 条件付き依存: `if (!(adoptedTab))` → `Promise.resolve()`
- 条件付き依存: `if (!(adoptedTab))` → `deferred.resolve()`
- 条件付き依存: `if (!(adoptedTab))` → `this.emitCreated()`
- 条件付き依存: `if (adoptedBy)` → `this.adopt()`
- 条件付き依存: `if (!(adoptedBy))` → `this.emitRemoved()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `Promise.resolve().then()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `Promise.resolve()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `this.emitHighlighted()`
- 参照: `currentTab.linkedBrowser`, `event.detail`, `event.detail.previousTab`, `event.originalTarget`, `event.originalTarget.parentNode`, `event.target`, `event.target.documentGlobal`, `event.type`, `frameLoader.lazyHeight`, `frameLoader.lazyWidth`, `nativeTab.documentGlobal.gBrowser.selectedTab`, `nativeTab.parentNode`

## TabTracker.receiveMessage()
- 位置: L611-619
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.data && message.data.isArticle !== undefined)` → `this.emit()`
- 参照: `message.data`, `message.data.isArticle`, `message.name`

## TabTracker._handleWindowOpen()
- 位置: L629-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gBrowserInit.getTabToAdopt()`
- 条件付き依存: `if (tabToAdopt)` → `Tabbrowser.isTab()`
- 条件付き依存: `if (Tabbrowser.isTab(tabToAdopt))` → `this.adopt()`
- 条件付き依存: `if (!(tabToAdopt))` → `this.emitCreated()`
- 条件付き依存: `if (!(tabToAdopt))` → `this.emitActivated()`
- 条件付き依存: `if (!(tabToAdopt))` → `this.has()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `this.emitHighlighted()`
- 参照: `window.gBrowser.tabs`

## TabTracker._handleWindowClose()
- 位置: L662-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.adoptedTabs.has()`
- 条件付き依存: `if (!this.adoptedTabs.has(nativeTab))` → `this.emitRemoved()`
- 参照: `window.gBrowser.tabs`

## TabTracker.emitActivated()
- 位置: L679-692
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.getId()`, `windowTracker.getId()`
- 条件付き依存: `if (previousTab && !previousTab.closing)` → `this.getId()`
- 条件付き依存: `if (previousTab && !previousTab.closing)` → `isPrivateTab()`
- 参照: `nativeTab.documentGlobal`, `previousTab.closing`

## TabTracker.emitHighlighted()
- 位置: L701-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.getId()`, `window.gBrowser.selectedTabs.map()`, `windowTracker.getId()`

## TabTracker.emitCreated()
- 位置: L719-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## TabTracker.emitRemoved()
- 位置: L736-746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.getId()`, `windowTracker.getId()`
- 参照: `nativeTab.documentGlobal`

## TabTracker.getBrowserData()
- 位置: L748-774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getId()`, `this.getTabForBrowser()`, `windowTracker.getId()`
- 条件付き依存: `if (!(nativeTab))` → `windowTracker.isBrowserWindow()`
- 参照: `browser.documentGlobal`, `nativeTab.documentGlobal`, `window.browsingContext.topChromeWindow`

## TabTracker.activeTab()
- 位置: L776-782
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.gBrowser`, `window.gBrowser.selectedTab`, `windowTracker.topWindow`

## Tab._favIconUrl()
- 位置: L791-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.gBrowser.getIcon()`
- 参照: `this.nativeTab`

## Tab.attention()
- 位置: L795-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.nativeTab.hasAttribute()`

## Tab.audible()
- 位置: L799-801
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.soundPlaying`

## Tab.autoDiscardable()
- 位置: L803-805
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.undiscardable`

## Tab.browser()
- 位置: L807-809
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.linkedBrowser`

## Tab.discarded()
- 位置: L811-813
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.linkedPanel`

## Tab.frameLoader()
- 位置: L815-819
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `super.frameLoader`

## Tab.hidden()
- 位置: L821-823
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.hidden`

## Tab.sharingState()
- 位置: L825-827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.getTabSharingState()`
- 参照: `this.nativeTab`

## Tab.cookieStoreId()
- 位置: L829-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCookieStoreIdForTab()`
- 参照: `this.nativeTab`

## Tab.openerTabId()
- 位置: L833-843
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( opener && opener.parentNode && opener.ownerDocument == this.nativeTab.ownerDocument )` → `tabTracker.getId()`
- 参照: `opener.ownerDocument`, `opener.parentNode`, `this.nativeTab.openerTab`, `this.nativeTab.ownerDocument`

## Tab.height()
- 位置: L845-847
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.frameLoader.lazyHeight`

## Tab.index()
- 位置: L849-851
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.index`

## Tab.mutedInfo()
- 位置: L853-865
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `mutedInfo.extensionId`, `mutedInfo.reason`, `nativeTab.muteReason`, `nativeTab.muted`

## Tab.lastAccessed()
- 位置: L867-869
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.lastAccessed`

## Tab.pinned()
- 位置: L871-873
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.pinned`

## Tab.active()
- 位置: L875-877
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.selected`

## Tab.highlighted()
- 位置: L879-882
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab`

## Tab.status()
- 位置: L884-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.nativeTab.getAttribute()`

## Tab.width()
- 位置: L891-893
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.frameLoader.lazyWidth`

## Tab.window()
- 位置: L895-897
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.documentGlobal`

## Tab.windowId()
- 位置: L899-901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.getId()`
- 参照: `this.window`

## Tab.isArticle()
- 位置: L903-905
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nativeTab.linkedBrowser.isArticle`

## Tab.isInReaderMode()
- 位置: L907-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.url.startsWith()`
- 参照: `this.url`

## Tab.successorTabId()
- 位置: L911-914
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.getId()`, `this.window.gBrowser.getSuccessor()`
- 参照: `this.nativeTab`

## Tab.groupId()
- 位置: L916-919
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getExtTabGroupIdForInternalTabGroupId()`
- 参照: `group.id`, `this.nativeTab`

## Tab.splitViewId()
- 位置: L921-924
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `splitview.splitViewId`, `this.nativeTab`

## Tab.convertFromSessionStoreClosedData()
- 位置: L942-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `String()`, `windowTracker.getId()`
- 条件付き依存: `if (entries.length)` → `extension.hasPermission()`
- 条件付き依存: `if (entries.length)` → `extension.allowedOrigins.matches()`
- 参照: `entries.length`, `entry.title`, `entry.url`, `result.favIconUrl`, `result.title`, `result.url`, `tabData.closedId`, `tabData.entries`, `tabData.hidden`, `tabData.image`, `tabData.index`, `tabData.lastAccessed`, `tabData.pos`, `tabData.state`, `tabData.state.entries`, `tabData.state.hidden`, `tabData.state.index`, `tabData.state.isPrivate`, `tabData.state.lastAccessed`

## Window.updateGeometry()
- 位置: L1003-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options.left !== null || options.top !== null)` → `window.moveTo()`
- 条件付き依存: `if (options.width !== null || options.height !== null)` → `window.resizeTo()`
- 参照: `options.height`, `options.left`, `options.top`, `options.width`, `window.outerHeight`, `window.outerWidth`, `window.screenX`, `window.screenY`

## Window._title()
- 位置: L1020-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.document.title`

## Window.setTitlePreface()
- 位置: L1024-1029
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.document.documentElement.setAttribute()`

## Window.focused()
- 位置: L1031-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.document.hasFocus()`

## Window.top()
- 位置: L1035-1037
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.screenY`

## Window.left()
- 位置: L1039-1041
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.screenX`

## Window.width()
- 位置: L1043-1045
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.outerWidth`

## Window.height()
- 位置: L1047-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.outerHeight`

## Window.incognito()
- 位置: L1051-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `this.window`

## Window.alwaysOnTop()
- 位置: L1055-1058
- 役割: (未記入)
- 触るとき: (未記入)

## Window.isLastFocused()
- 位置: L1060-1062
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window`, `windowTracker.topWindow`

## Window.getState()
- 位置: L1064-1072
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.STATE_FULLSCREEN`, `window.STATE_MAXIMIZED`, `window.STATE_MINIMIZED`, `window.STATE_NORMAL`, `window.windowState`

## Window.state()
- 位置: L1074-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Window.getState()`
- 参照: `this.window`

## Window.setState()
- 位置: async L1078-1191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.maximize()`, `window.minimize()`, `window.removeEventListener()`, `window.restore()`
- 条件付き依存: `if (resizeExpected)` → `window.addEventListener()`
- 条件付き依存: `if (window.windowState !== window.STATE_NORMAL)` → `window.restore()`
- 条件付き依存: `if (window.windowState != expectedState)` → `window.addEventListener()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `Promise.any()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `Promise.all()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `setTimeout()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `window.removeEventListener()`
- 参照: `window.STATE_FULLSCREEN`, `window.STATE_MAXIMIZED`, `window.STATE_MINIMIZED`, `window.STATE_NORMAL`, `window.fullScreen`, `window.windowState`

## onSizeModeChange()
- 位置: L1171-1175
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (window.windowState == expectedState)` → `resolve()`
- 参照: `window.windowState`

## Window.getTabs()
- 位置: L1193-1209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.getWrapper()`, `this.window.gBrowserInit.isAdoptingTab()`
- 参照: `this.extension`, `this.window.gBrowser.tabs`

## Window.getHighlightedTabs()
- 位置: L1211-1219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.getWrapper()`
- 参照: `this.extension`, `this.window.gBrowser.selectedTabs`

## Window.activeTab()
- 位置: L1221-1232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.getWrapper()`, `this.window.gBrowserInit.isAdoptingTab()`
- 参照: `this.extension`, `this.window.gBrowser.selectedTab`

## Window.getTabAtIndex()
- 位置: L1234-1239
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (nativeTab)` → `this.extension.tabManager.getWrapper()`
- 参照: `this.window.gBrowser.tabs`

## Window.convertFromSessionStoreClosedData()
- 位置: L1254-1273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`
- 条件付き依存: `if (windowData.tabs.length)` → `windowData.tabs.map()`
- 条件付き依存: `if (windowData.tabs.length)` → `Tab.convertFromSessionStoreClosedData()`
- 参照: `result.tabs`, `windowData.closedId`, `windowData.tabs.length`

## TabManager.get()
- 位置: L1279-1289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.getTab()`
- 条件付き依存: `if (nativeTab)` → `this.canAccessTab()`
- 条件付き依存: `if (nativeTab)` → `this.getWrapper()`

## TabManager.addActiveTabPermission()
- 位置: L1291-1293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.addActiveTabPermission()`
- 参照: `tabTracker.activeTab`

## TabManager.revokeActiveTabPermission()
- 位置: L1295-1297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.revokeActiveTabPermission()`
- 参照: `tabTracker.activeTab`

## TabManager.canAccessTab()
- 位置: L1299-1311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.canAccessContainer()`, `this.extension.canAccessWindow()`
- 参照: `nativeTab.documentGlobal`, `nativeTab.userContextId`, `this.extension.userContextIsolation`

## TabManager.wrapTab()
- 位置: L1313-1315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.getId()`
- 参照: `this.extension`

## TabManager.getWrapper()
- 位置: L1317-1321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nativeTab.documentGlobal.gBrowserInit.isAdoptingTab()`
- 条件付き依存: `if (!nativeTab.documentGlobal.gBrowserInit.isAdoptingTab())` → `super.getWrapper()`

## WindowManager.get()
- 位置: L1325-1329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWrapper()`, `windowTracker.getWindow()`

## WindowManager.getAll()
- 位置: L1331-1341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canAccessWindow()`, `this.getWrapper()`, `windowTracker.browserWindows()`

## WindowManager.wrapWindow()
- 位置: L1343-1345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.getId()`
- 参照: `this.extension`
