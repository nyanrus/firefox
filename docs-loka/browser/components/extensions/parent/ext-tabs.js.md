# browser/components/extensions/parent/ext-tabs.js

source: browser/components/extensions/parent/ext-tabs.js
source-hash: cb2c4b387df5620b770d418506dfe55cb2feeeb4
lines: 1849

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`, `this.tabEventRegistrar()`

## getLocalizedDescription()
- 位置: L38-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUIUtils.getLocalizedFragment()`, `doc.createXULElement()`, `doc.getElementById()`, `doc.getElementById("alltabs-button")?.closest()`, `image.classList.add()`
- 条件付き依存: `if (!doc.getElementById("alltabs-button")?.closest("#TabsToolbar"))` → `image.classList.add()`

## showHiddenTabs()
- 位置: L55-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `SessionStore.getCustomTabValue()`
- 条件付き依存: `if ( tab.hidden && tab.documentGlobal && SessionStore.getCustomTabValue(tab, "hiddenBy") === id )` → `win.gBrowser.showTab()`
- 参照: `tab.documentGlobal`, `tab.hidden`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`
- XPCOM: `Services.wm`

## onUpdate()
- 位置: L103-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manifest.permissions.includes()`
- 条件付き依存: `if (!manifest.permissions || !manifest.permissions.includes("tabHide"))` → `showHiddenTabs()`
- 参照: `manifest.permissions`

## onDisable()
- 位置: L109-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showHiddenTabs()`, `tabHidePopup.clearConfirmation()`

## onUninstall()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabHidePopup.clearConfirmation()`

## tabEventRegistrar()
- 位置: L118-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.on()`

## listener2()
- 位置: L122-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener()`, `tabManager.canAccessTab()`
- 参照: `eventData.nativeTab`

## unregister()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.off()`

## convert()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)

## listener()
- 位置: L145-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`
- 参照: `extension.privateBrowsingAllowed`

## listener()
- 位置: L156-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`
- 参照: `event.newPosition`, `event.newWindowId`, `event.tabId`

## listener()
- 位置: L165-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `tabManager.convert()`
- 参照: `event.currentTabSize`, `event.nativeTab`, `this.extension`

## listener()
- 位置: L172-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`
- 参照: `event.oldPosition`, `event.oldWindowId`, `event.tabId`

## listener()
- 位置: L181-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`
- 参照: `event.isWindowClosing`, `event.tabId`, `event.windowId`

## onMoved()
- 位置: L188-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`
- 参照: `this.extension`

## moveListener()
- 位置: L193-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.canAccessTab()`
- 条件付き依存: `if (fromIndex !== toIndex && tabManager.canAccessTab(nativeTab))` → `fire.async()`
- 条件付き依存: `if (fromIndex !== toIndex && tabManager.canAccessTab(nativeTab))` → `tabTracker.getId()`
- 条件付き依存: `if (fromIndex !== toIndex && tabManager.canAccessTab(nativeTab))` → `windowTracker.getId()`
- 参照: `currentTabState.tabIndex`, `event.detail`, `event.originalTarget`, `nativeTab.documentGlobal`, `previousTabState.tabIndex`

## unregister()
- 位置: L211-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)

## onHighlighted()
- 位置: L220-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.on()`
- 参照: `this.extension`

## highlightListener()
- 位置: L222-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `fire.async()`, `windowManager.getWrapper()`, `windowTracker.getWindow()`, `windowWrapper.getHighlightedTabs()`
- 参照: `event.windowId`, `tab.id`

## unregister()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.off()`

## convert()
- 位置: L244-247
- 役割: (未記入)
- 触るとき: (未記入)

## onUpdated()
- 位置: L251-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filter.properties.has()`, `windowTracker.addListener()`
- 条件付き依存: `if (filter.properties)` → `filter.properties.some()`
- 条件付き依存: `if (filter.properties)` → `allAttrs.has()`
- 条件付き依存: `if (filter.properties.has("status") || filter.properties.has("url"))` → `listeners.set()`
- 条件付き依存: `if (needsModified)` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("pinned"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("discarded"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("groupId"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("splitViewId"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("hidden"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("isArticle"))` → `tabTracker.on()`
- 条件付き依存: `if (filter.properties.has("openerTabId"))` → `tabTracker.on()`
- 参照: `filter.properties`, `filter.urls`

## sanitize()
- 位置: L270-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `restricted.has()`
- 参照: `tab.hasTabPermission`

## getWindowID()
- 位置: L287-296
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (windowId === Window.WINDOW_ID_CURRENT)` → `windowTracker.getTopWindow()`
- 条件付き依存: `if (windowId === Window.WINDOW_ID_CURRENT)` → `windowTracker.getId()`
- 参照: `Window.WINDOW_ID_CURRENT`

## matchFilters()
- 位置: L298-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getWindowID()`
- 条件付き依存: `if (filter.urls)` → `filter.urls.matches()`
- 参照: `filter.cookieStoreId`, `filter.tabId`, `filter.urls`, `filter.windowId`, `tab._uri`, `tab.cookieStoreId`, `tab.hasTabPermission`, `tab.id`, `tab.windowId`

## fireForTab()
- 位置: L323-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `matchFilters()`, `sanitize()`
- 条件付き依存: `if (changeInfo)` → `tabTracker.maybeWaitForTabOpen(nativeTab).then()`
- 条件付き依存: `if (changeInfo)` → `tabTracker.maybeWaitForTabOpen()`
- 条件付き依存: `if (changeInfo)` → `fire.async()`
- 条件付き依存: `if (changeInfo)` → `tab.convert()`
- 参照: `nativeTab.parentNode`, `tab.id`

## listener()
- 位置: L341-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.canAccessWindow()`, `fireForTab()`, `tabManager.getWrapper()`, `updatedTab.documentGlobal.gBrowserInit?.isAdoptingTab()`
- 条件付き依存: `if (event.type == "TabAttrModified")` → `changed.includes()`
- 条件付き依存: `if (event.type == "TabAttrModified")` → `filter.properties.has()`
- 条件付き依存: `if ( changed.includes("image") && filter.properties.has("favIconUrl") )` → `needed.push()`
- 条件付き依存: `if (changed.includes("muted") && filter.properties.has("mutedInfo"))` → `needed.push()`
- 条件付き依存: `if ( changed.includes("soundplaying") && filter.properties.has("audible") )` → `needed.push()`
- 条件付き依存: `if ( changed.includes("undiscardable") && filter.properties.has("autoDiscardable") )` → `needed.push()`
- 条件付き依存: `if (changed.includes("label") && filter.properties.has("title"))` → `needed.push()`
- 条件付き依存: `if ( changed.includes("sharing") && filter.properties.has("sharingState") )` → `needed.push()`
- 条件付き依存: `if ( changed.includes("attention") && filter.properties.has("attention") )` → `needed.push()`
- 条件付き依存: `if (event.type == "TabPinned")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabUnpinned")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabBrowserInserted")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabBrowserDiscarded")` → `needed.push()`
- 条件付き依存: `if (event.type === "TabGrouped")` → `needed.push()`
- 条件付き依存: `if (event.type === "TabUngrouped")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabMove")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabShow")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabHide")` → `needed.push()`
- 参照: `currentTabState.splitViewId`, `event.detail`, `event.detail.adoptingSplitView`, `event.detail.changed`, `event.detail.insertedOnTabCreation`, `event.originalTarget`, `event.originalTarget.documentGlobal`, `event.type`, `previousTabState.splitViewId`, `updatedTab.group`, `updatedTab.initializing`

## statusListener()
- 位置: L452-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (tabElem)` → `extension.canAccessWindow()`
- 条件付き依存: `if (tabElem)` → `filter.properties.has()`
- 条件付き依存: `if (tabElem)` → `fireForTab()`
- 条件付き依存: `if (tabElem)` → `tabManager.wrapTab()`
- 参照: `browser.documentGlobal`, `changed.status`, `changed.url`, `tabElem.documentGlobal`

## isArticleChangeListener()
- 位置: L472-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.canAccessWindow()`, `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (nativeTab && extension.canAccessWindow(nativeTab.documentGlobal))` → `tabManager.getWrapper()`
- 条件付き依存: `if (nativeTab && extension.canAccessWindow(nativeTab.documentGlobal))` → `fireForTab()`
- 参照: `message.data.isArticle`, `message.target`, `message.target.documentGlobal`, `nativeTab.documentGlobal`

## openerTabIdChangeListener()
- 位置: L482-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fireForTab()`, `tabManager.getWrapper()`

## unregister()
- 位置: L527-539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filter.properties.has()`, `windowTracker.removeListener()`
- 条件付き依存: `if (filter.properties.has("isArticle"))` → `tabTracker.off()`
- 条件付き依存: `if (filter.properties.has("openerTabId"))` → `tabTracker.off()`

## convert()
- 位置: L540-543
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L548-1847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module, event: "onActivated", extensionApi, }).api()`, `new EventManager({ context, module, event: "onAttached", extensionApi, }).api()`, `new EventManager({ context, module, event: "onCreated", extensionApi, }).api()`, `new EventManager({ context, module, event: "onDetached", extensionApi, }).api()`, `new EventManager({ context, module, event: "onHighlighted", extensionApi, }).api()`, `new EventManager({ context, module, event: "onMoved", extensionApi, }).api()`, `new EventManager({ context, module, event: "onRemoved", extensionApi, }).api()`, `new EventManager({ context, module, event: "onUpdated", extensionApi, }).api()`, `new EventManager({ context, name: "tabs.onReplaced", register: () => { return () => {}; }, }).api()`

## getTabOrActive()
- 位置: L554-565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.canAccessTab()`, `tabTracker.getTab()`
- 参照: `tabTracker.activeTab`

## getNativeTabsFromIDArray()
- 位置: L567-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `tabIds.map()`, `tabManager.canAccessTab()`, `tabTracker.getTab()`

## getNativeTabsOrSplitViews()
- 位置: L580-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `nativeTabs.map()`
- 参照: `t.splitview`

## updateNativeTabAfterAdopt()
- 位置: L584-590
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `nativeTabs.length`

## promiseTabWhenReady()
- 位置: async L592-608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabTracker.awaitTabReady()`
- 条件付き依存: `if (tabId !== null)` → `tabManager.get()`
- 条件付き依存: `if (!(tabId !== null))` → `tabManager.getWrapper()`
- 参照: `tab.nativeTab`, `tabTracker.activeTab`

## setContentTriggeringPrincipal()
- 位置: L610-625
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `options.triggeringPrincipal`, `options.userContextId`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## register()
- 位置: L674-676
- 役割: (未記入)
- 触るとき: (未記入)

## create()
- 位置: L693-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionUtils.isExtensionUrl()`, `context.canAccessWindow()`, `tabManager.convert()`, `tabTracker.addTabReadyBlocker()`, `url.startsWith()`, `window.gBrowser.addTab()`, `windowTracker.getTopNormalWindow()`, `windowTracker.getWindow()`
- 条件付き依存: `if (!gBrowserInit || !gBrowserInit.delayedStartupFinished)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(!gBrowserInit || !gBrowserInit.delayedStartupFinished))` → `resolve()`
- 条件付き依存: `if (createProperties.cookieStoreId)` → `getUserContextIdForCookieStoreId()`
- 条件付き依存: `if (createProperties.cookieStoreId)` → `PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (createProperties.url !== null)` → `context.uri.resolve()`
- 条件付き依存: `if (createProperties.url !== null)` → `ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (createProperties.url !== null)` → `context.checkLoadURL()`
- 条件付き依存: `if ( !ExtensionUtils.isExtensionUrl(url) && !context.checkLoadURL(url, { dontReportErrors: true }) )` → `Promise.reject()`
- 条件付き依存: `if (createProperties.openInReaderMode)` → `encodeURIComponent()`
- 条件付き依存: `if (!discardable || ExtensionUtils.isExtensionUrl(url))` → `setContentTriggeringPrincipal()`
- 条件付き依存: `if (createProperties.openerTabId !== null)` → `tabTracker.getTab()`
- 条件付き依存: `if (options.ownerTab.documentGlobal !== window)` → `Promise.reject()`
- 条件付き依存: `if (active)` → `Promise.reject()`
- 条件付き依存: `if (createProperties.pinned)` → `Promise.reject()`
- 条件付き依存: `if (!discardable)` → `Promise.reject()`
- 条件付き依存: `if (createProperties.title)` → `Promise.reject()`
- 条件付き依存: `if (!createProperties.url)` → `window.gURLBar.select()`
- 条件付き依存: `if (createProperties.muted)` → `nativeTab.toggleMuteAudio()`
- 参照: `context.principal`, `createProperties.active`, `createProperties.cookieStoreId`, `createProperties.discarded`, `createProperties.index`, `createProperties.muted`, `createProperties.openInReaderMode`, `createProperties.openerTabId`, `createProperties.pinned`, `createProperties.title`, `createProperties.url`, `createProperties.windowId`, `currentTab.linkedBrowser`, `extension.id`, `frameLoader.lazyHeight`, `frameLoader.lazyWidth`, `gBrowserInit.delayedStartupFinished`, `options.createLazyBrowser`, `options.lazyTabTitle`, `options.openerBrowser`, `options.ownerTab`, `options.ownerTab.documentGlobal`, `options.ownerTab.linkedBrowser`, `options.pinned`, `options.tabIndex`, `options.userContextId`, `window.BROWSER_NEW_TAB_URL`, `window.gBrowser`, `window.gBrowser.selectedTab`
- XPCOM: `Services.obs`

## obs()
- 位置: L706-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `resolve()`
- XPCOM: `Services.obs`

## remove()
- 位置: async L833-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `eachWindow.gBrowser.removeTabs()`, `getNativeTabsFromIDArray()`, `windowTabMap.entries()`, `windowTabMap.get()`, `windowTabMap.get(nativeTab.documentGlobal).push()`
- 条件付き依存: `if (nativeTabs.length === 1)` → `nativeTabs[0].documentGlobal.gBrowser.removeTab()`
- 参照: `nativeTab.documentGlobal`, `nativeTabs.length`

## discard()
- 位置: async L860-870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `getNativeTabsFromIDArray()`, `nativeTab.documentGlobal.gBrowser.discardBrowser()`, `nativeTab.documentGlobal.gBrowser.prepareDiscardBrowser()`, `nativeTabs.map()`

## update()
- 位置: async L872-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabOrActive()`, `tabManager.convert()`
- 条件付き依存: `if (updateProperties.url !== null)` → `context.uri.resolve()`
- 条件付き依存: `if (updateProperties.url !== null)` → `context.checkLoadURL()`
- 条件付き依存: `if (!context.checkLoadURL(url, { dontReportErrors: true }))` → `ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (ExtensionUtils.isExtensionUrl(url))` → `setContentTriggeringPrincipal()`
- 条件付き依存: `if (!(ExtensionUtils.isExtensionUrl(url)))` → `Promise.reject()`
- 条件付き依存: `if (nativeTab.linkedPanel)` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if (!(nativeTab.linkedPanel))` → `nativeTab.addEventListener()`
- 条件付き依存: `if (!(nativeTab.linkedPanel))` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if (!(nativeTab.linkedPanel))` → `tabbrowser.insertBrowser()`
- 条件付き依存: `if (!nativeTab.selected && !nativeTab.multiselected)` → `tabbrowser.addToMultiSelectedTabs()`
- 条件付き依存: `if (updateProperties.active !== false)` → `tabbrowser.lockClearMultiSelectionOnce()`
- 条件付き依存: `if (!(updateProperties.highlighted))` → `tabbrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (nativeTab.muted != updateProperties.muted)` → `nativeTab.toggleMuteAudio()`
- 条件付き依存: `if (updateProperties.pinned)` → `tabbrowser.pinTab()`
- 条件付き依存: `if (!(updateProperties.pinned))` → `tabbrowser.unpinTab()`
- 条件付き依存: `if (updateProperties.openerTabId !== null)` → `tabTracker.setOpener()`
- 条件付き依存: `if (updateProperties.successorTabId !== TAB_ID_NONE)` → `tabTracker.getTab()`
- 条件付き依存: `if (updateProperties.successorTabId !== null)` → `tabbrowser.setSuccessor()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `context.principal`, `extension.id`, `nativeTab.documentGlobal.gBrowser`, `nativeTab.linkedBrowser`, `nativeTab.linkedPanel`, `nativeTab.multiselected`, `nativeTab.muted`, `nativeTab.ownerDocument`, `nativeTab.selected`, `nativeTab.undiscardable`, `successor.ownerDocument`, `tabbrowser.selectedTab`, `updateProperties.active`, `updateProperties.autoDiscardable`, `updateProperties.highlighted`, `updateProperties.loadReplace`, `updateProperties.muted`, `updateProperties.openerTabId`, `updateProperties.pinned`, `updateProperties.successorTabId`, `updateProperties.url`
- XPCOM: [`nsIWebNavigation`](../../../../docshell/base/nsIWebNavigation.idl.md)

## reload()
- 位置: async L970-978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.reloadWithFlags()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_BYPASS_CACHE`, `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `reloadProperties.bypassCache`
- XPCOM: [`nsIWebNavigation`](../../../../docshell/base/nsIWebNavigation.idl.md)

## warmup()
- 位置: async L980-987
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.canAccessTab()`, `tabTracker.getTab()`, `tabbrowser.warmupTab()`
- 参照: `nativeTab.documentGlobal.gBrowser`

## get()
- 位置: async L989-991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabManager.get()`, `tabManager.get(tabId).convert()`

## getCurrent()
- 位置: L993-999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (context.tabId)` → `tabManager.get(context.tabId).convert()`
- 条件付き依存: `if (context.tabId)` → `tabManager.get()`
- 参照: `context.tabId`

## query()
- 位置: async L1001-1005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `tab.convert()`, `tabManager.query()`

## captureTab()
- 位置: async L1007-1017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabOrActive()`, `tab.capture()`, `tabManager.wrapTab()`, `tabTracker.awaitTabReady()`, `window.ZoomManager.getZoomForBrowser()`
- 参照: `browser.documentGlobal`, `nativeTab.linkedBrowser`

## captureVisibleTab()
- 位置: async L1019-1038
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.hasPermission()`, `tab.capture()`, `tabManager.getWrapper()`, `tabTracker.awaitTabReady()`, `window.ZoomManager.getZoomForBrowser()`, `windowTracker.getTopWindow()`, `windowTracker.getWindow()`
- 参照: `tab.hasActiveTabPermission`, `tab.nativeTab`, `tab.nativeTab.linkedBrowser`, `window.gBrowser.selectedTab`

## detectLanguage()
- 位置: async L1040-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promiseTabWhenReady()`, `tab.queryContent()`

## executeScript()
- 位置: async L1046-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promiseTabWhenReady()`, `tab.executeScript()`

## insertCSS()
- 位置: async L1051-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promiseTabWhenReady()`, `tab.insertCSS()`

## removeCSS()
- 位置: async L1056-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promiseTabWhenReady()`, `tab.removeCSS()`

## move()
- 位置: async L1061-1230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `PrivateBrowsingUtils.isBrowserPrivate()`, `getNativeTabsFromIDArray()`, `lastInsertionMap.get()`, `lastInsertionMap.set()`, `splitviewTabs.at()`, `tabManager.convert()`, `tabsMoved.map()`, `tabsToMove.shift()`
- 条件付き依存: `if (moveProperties.windowId !== null)` → `windowTracker.getWindow()`
- 条件付き依存: `if (!destinationWindow)` → `Promise.reject()`
- 条件付き依存: `if (isSameWindow && gBrowser.tabs.length === 1)` → `lastInsertionMap.set()`
- 条件付き依存: `if (!(insertionPoint == -1))` → `Math.min()`
- 条件付き依存: `if (splitview)` → `splitviewTabs.find()`
- 条件付き依存: `if (!(otherTabInSplit === tabsToMove[0]))` → `tabsToMove.includes()`
- 条件付き依存: `if (tabsToMove.includes(otherTabInSplit))` → `splitview.unsplitTabs()`
- 条件付き依存: `if (wantReversedSplit)` → `splitview.reverseTabs()`
- 条件付き依存: `if (isSameWindow)` → `gBrowser.moveTabTo()`
- 条件付き依存: `if (splitview)` → `splitviewTabs.indexOf()`
- 条件付き依存: `if (splitview)` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (splitview)` → `Iterator.zip()`
- 条件付き依存: `if (splitview)` → `updateNativeTabAfterAdopt()`
- 条件付き依存: `if (!(splitview))` → `gBrowser.adoptTab()`
- 条件付き依存: `if (!(splitview))` → `updateNativeTabAfterAdopt()`
- 条件付き依存: `if (splitview)` → `tabsToMove.indexOf()`
- 条件付き依存: `if (splitview)` → `tabsToMove.splice()`
- 条件付き依存: `if (tabIsInTabsToMove)` → `tabsMoved.push()`
- 条件付き依存: `if (!(splitview))` → `tabsMoved.push()`
- 参照: `gBrowser.pinnedTabCount`, `gBrowser.tabs.length`, `moveProperties.index`, `moveProperties.windowId`, `nativeTab.documentGlobal`, `nativeTab.documentGlobal.gBrowser`, `nativeTab.index`, `nativeTab.pinned`, `nativeTab.splitview`, `otherTabInSplit.index`, `splitview.tabs`, `splitview?.tabs`, `splitviewTabs.at(-1).index`, `tabsToMove.length`, `window.gBrowser`

## duplicate()
- 位置: L1232-1257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.duplicateTab()`, `getTabOrActive()`, `newTab.addEventListener()`, `resolve()`, `tabManager.convert()`, `tabTracker.addTabReadyBlocker()`
- 参照: `nativeTab.documentGlobal.gBrowser`

## getZoom()
- 位置: L1259-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `ZoomManager.getZoomForBrowser()`, `getTabOrActive()`
- 参照: `nativeTab.documentGlobal`, `nativeTab.linkedBrowser`

## setZoom()
- 位置: L1268-1285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `getTabOrActive()`
- 条件付き依存: `if (zoom === 0)` → `FullZoom.reset()`
- 条件付き依存: `if (zoom >= ZoomManager.MIN && zoom <= ZoomManager.MAX)` → `FullZoom.setZoom()`
- 条件付き依存: `if (!(zoom >= ZoomManager.MIN && zoom <= ZoomManager.MAX))` → `Promise.reject()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `nativeTab.documentGlobal`, `nativeTab.linkedBrowser`

## getZoomSettings()
- 位置: async L1287-1297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomUI.getGlobalValue()`, `getTabOrActive()`
- 参照: `FullZoom.siteSpecific`, `nativeTab.documentGlobal`

## setZoomSettings()
- 位置: async L1299-1315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(settings).every()`, `getTabOrActive()`, `tabTracker.getId()`, `this.getZoomSettings()`
- 条件付き依存: `if ( !Object.keys(settings).every( key => settings[key] === currentSettings[key] ) )` → `JSON.stringify()`

## register()
- 位置: L1320-1397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`, `getZoomLevel()`, `tabTracker.off()`, `tabTracker.on()`, `windowTracker.addListener()`, `windowTracker.browserWindows()`, `windowTracker.removeListener()`, `zoomLevels.set()`
- 参照: `nativeTab.linkedBrowser`, `window.gBrowser.tabs`

## getZoomLevel()
- 位置: L1321-1325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomManager.getZoomForBrowser()`
- 参照: `browser.documentGlobal`

## tabCreated()
- 位置: L1342-1347
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!event.isPrivate || context.privateBrowsingAllowed)` → `zoomLevels.set()`
- 条件付き依存: `if (!event.isPrivate || context.privateBrowsingAllowed)` → `getZoomLevel()`
- 参照: `context.privateBrowsingAllowed`, `event.isPrivate`, `event.nativeTab.linkedBrowser`

## zoomListener()
- 位置: async L1349-1383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`, `gBrowser.getTabForBrowser()`, `getZoomLevel()`, `zoomLevels.get()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `zoomLevels.set()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `tabTracker.getId()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `fire.async()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `tabsApi.tabs.getZoomSettings()`
- 参照: `browser.DOCUMENT_NODE`, `browser.docShell.chromeEventHandler`, `browser.documentGlobal`, `browser.nodeType`, `event.originalTarget`

## print()
- 位置: L1400-1404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrintUtils.startPrintWindow()`, `getTabOrActive()`
- 参照: `activeTab.documentGlobal`, `activeTab.linkedBrowser.browsingContext`

## printPreview()
- 位置: L1407-1409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `this.print()`

## saveAsPDF()
- 位置: L1411-1564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `DownloadPaths.sanitize()`, `getTabOrActive()`, `picker.appendFilter()`, `picker.init()`, `picker.open()`, `strBundle.GetStringFromName()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `decodeURIComponent()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `path.replace()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `path.split("/").pop()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `path.split()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `Cc[ "@mozilla.org/network/file-output-stream;1" ].createInstance()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `fstream.init()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `fstream.close()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `resolve()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `Cc[ "@mozilla.org/gfx/printsettings-service;1" ].getService()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `psService.createNewPrintSettings()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `activeTab.linkedBrowser.browsingContext .print(printSettings) .then()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `activeTab.linkedBrowser.browsingContext .print()`
- 条件付き依存: `if (!(retval == 0 || retval == 2))` → `resolve()`
- 参照: `Ci.nsIFileOutputStream`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeSave`, `Ci.nsIPrintSettings.kOutputDestinationFile`, `Ci.nsIPrintSettings.kOutputFormatPDF`, `Ci.nsIPrintSettingsService`, `activeTab.documentGlobal.browsingContext`, `activeTab.linkedBrowser.contentTitle`, `activeTab.linkedBrowser.currentURI.spec`, `pageSettings.edgeBottom`, `pageSettings.edgeLeft`, `pageSettings.edgeRight`, `pageSettings.edgeTop`, `pageSettings.footerCenter`, `pageSettings.footerLeft`, `pageSettings.footerRight`, `pageSettings.headerCenter`, `pageSettings.headerLeft`, `pageSettings.headerRight`, `pageSettings.marginBottom`, `pageSettings.marginLeft`, `pageSettings.marginRight`, `pageSettings.marginTop`, `pageSettings.orientation`, `pageSettings.paperHeight`, `pageSettings.paperSizeUnit`, `pageSettings.paperWidth`, `pageSettings.scaling`, `pageSettings.showBackgroundColors`, `pageSettings.showBackgroundImages`, `pageSettings.shrinkToFit`, `pageSettings.toFileName`, `picker.defaultExtension`, `picker.defaultString`, `picker.file`, `picker.file.path`, `printSettings.edgeBottom`, `printSettings.edgeLeft`, `printSettings.edgeRight`, `printSettings.edgeTop`, `printSettings.footerStrCenter`, `printSettings.footerStrLeft`, `printSettings.footerStrRight`, `printSettings.headerStrCenter`, `printSettings.headerStrLeft`, `printSettings.headerStrRight`, `printSettings.isInitializedFromPrefs`, `printSettings.isInitializedFromPrinter`, `printSettings.marginBottom`, `printSettings.marginLeft`, `printSettings.marginRight`, `printSettings.marginTop`, `printSettings.orientation`, `printSettings.outputDestination`, `printSettings.outputFormat`, `printSettings.paperHeight`, `printSettings.paperSizeUnit`, `printSettings.paperWidth`, `printSettings.printBGColors`, `printSettings.printBGImages`, `printSettings.printSilent`, `printSettings.printerName`, `printSettings.scaling`, `printSettings.shrinkToFit`, `printSettings.toFileName`, `url.hostname`, `url.pathname`
- XPCOM: [`nsIFileOutputStream`](../../../../netwerk/base/nsIFileStreams.idl.md) / `nsIFilePicker` / [`nsIPrintSettings`](../../../../docshell/base/nsIDocumentViewer.idl.md) / `nsIPrintSettingsService` / `@mozilla.org/filepicker;1` / `@mozilla.org/gfx/printsettings-service;1` / `@mozilla.org/network/file-output-stream;1`

## toggleReaderMode()
- 位置: async L1566-1580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.sendMessageToActor()`, `promiseTabWhenReady()`
- 参照: `tab.isArticle`, `tab.isInReaderMode`

## moveInSuccession()
- 位置: L1582-1651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`, `referenceWindow.gBrowser.getSuccessor()`, `referenceWindow.gBrowser.replaceInSuccession()`, `tabIdSet.has()`, `tabManager.canAccessTab()`, `tabTracker.getTab()`
- 条件付き依存: `if (append)` → `referenceWindow.gBrowser.getSuccessor()`
- 条件付き依存: `if (append && tab === lastSuccessor)` → `referenceWindow.gBrowser.getSuccessor()`
- 条件付き依存: `if (previousTab)` → `referenceWindow.gBrowser.setSuccessor()`
- 条件付き依存: `if (!append && insert && lastSuccessor !== null)` → `referenceWindow.gBrowser.replaceInSuccession()`
- 参照: `referenceTab.documentGlobal`, `tab.documentGlobal`, `tabIdSet.size`, `tabIds.length`

## show()
- 位置: L1653-1659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getNativeTabsFromIDArray()`
- 条件付き依存: `if (tab.documentGlobal)` → `tab.documentGlobal.gBrowser.showTab()`
- 参照: `tab.documentGlobal`

## hide()
- 位置: L1661-1687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getNativeTabsFromIDArray()`
- 条件付き依存: `if (tab.documentGlobal && !tab.hidden)` → `tab.documentGlobal.gBrowser.hideTab()`
- 条件付き依存: `if (tab.hidden)` → `hidden.push()`
- 条件付き依存: `if (tab.hidden)` → `tabTracker.getId()`
- 条件付き依存: `if (hidden.length)` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (hidden.length)` → `CustomizableUI.widgetIsLikelyVisible()`
- 条件付き依存: `if (!CustomizableUI.widgetIsLikelyVisible("alltabs-button", win))` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (hidden.length)` → `tabHidePopup.open()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `extension.id`, `hidden.length`, `tab.documentGlobal`, `tab.hidden`
- XPCOM: `Services.wm`

## highlight()
- 位置: L1689-1712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `context.canAccessWindow()`, `tabManager.canAccessTab()`, `tabs.map()`, `windowManager.convert()`, `windowTracker.getWindow()`
- 参照: `Window.WINDOW_ID_CURRENT`, `tabs.length`, `window.gBrowser.selectedTabs`, `window.gBrowser.tabs`

## goForward()
- 位置: L1714-1717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.goForward()`

## goBack()
- 位置: L1719-1722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.goBack()`

## group()
- 位置: L1724-1814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `getExtTabGroupIdForInternalTabGroupId()`, `getNativeTabsFromIDArray()`, `windowTracker.getWindow()`
- 条件付き依存: `if (options.groupId == null)` → `nativeTabs.find()`
- 条件付き依存: `if (options.groupId == null)` → `unpinTabsBeforeGrouping()`
- 条件付き依存: `if (options.groupId == null)` → `window.gBrowser.addTabGroup()`
- 条件付き依存: `if (options.groupId == null)` → `getNativeTabsOrSplitViews()`
- 条件付き依存: `if (!(options.groupId == null))` → `window.gBrowser.getTabGroupById()`
- 条件付き依存: `if (!(options.groupId == null))` → `getInternalTabGroupIdForExtTabGroupId()`
- 条件付き依存: `if (!(options.groupId == null))` → `unpinTabsBeforeGrouping()`
- 条件付き依存: `if ( nativeTab.documentGlobal === window && nativeTab.index < firstTabInGroup.index )` → `tabsBefore.push()`
- 条件付き依存: `if (!( nativeTab.documentGlobal === window && nativeTab.index < firstTabInGroup.index ))` → `tabsAfter.push()`
- 条件付き依存: `if (tabsBefore.length)` → `window.gBrowser.moveTabsBefore()`
- 条件付き依存: `if (tabsBefore.length)` → `getNativeTabsOrSplitViews()`
- 条件付き依存: `if (tabsAfter.length)` → `group.addTabs()`
- 条件付き依存: `if (tabsAfter.length)` → `getNativeTabsOrSplitViews()`
- 参照: `Window.WINDOW_ID_CURRENT`, `firstTabInGroup.index`, `firstTabInGroup.splitview`, `group.id`, `group.tabs`, `insertBefore.group.nextElementSibling`, `insertBefore?.splitview`, `nativeTab.documentGlobal`, `nativeTab.index`, `options.createProperties?.windowId`, `options.groupId`, `options.tabIds`, `t.documentGlobal`, `tabInWin.group`, `tabInWin.group.tabs`, `tabInWin.splitview?.tabs`, `tabInWin?.group`, `tabsAfter.length`, `tabsBefore.length`

## unpinTabsBeforeGrouping()
- 位置: L1746-1750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nativeTab.documentGlobal.gBrowser.unpinTab()`

## ungroup()
- 位置: L1816-1843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `getNativeTabsFromIDArray()`, `getNativeTabsOrSplitViews()`, `tabs.sort()`
- 条件付き依存: `if (nativeTab.group)` → `ungroupOrder.get(nativeTab.group).push()`
- 条件付き依存: `if (nativeTab.group)` → `ungroupOrder.get()`
- 条件付き依存: `if (firstTab === group.tabs[0])` → `group.documentGlobal.gBrowser.moveTabsBefore()`
- 条件付き依存: `if (!(firstTab === group.tabs[0]))` → `group.documentGlobal.gBrowser.moveTabsAfter()`
- 参照: `a.index`, `b.index`, `firstTab.tabs`, `group.tabs`, `nativeTab.group`
