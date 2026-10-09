# browser/modules/BrowserUsageTelemetry.sys.mjs

source: browser/modules/BrowserUsageTelemetry.sys.mjs
source-hash: 747591972bd724d6b4ac2dbd1a5f7c0819f5e219
lines: 2173

## <module>
- 役割: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.recordPinnedTabsCount()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `getOpenTabsAndWinsCounts()`, `getPinnedTabsCount()`

## telemetryId()
- 位置: L225-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `widgetId.endsWith()`, `widgetId.replace()`
- 条件付き依存: `if (widgetId.endsWith("-browser-action"))` → `addonId()`
- 条件付き依存: `if (widgetId.endsWith("-browser-action"))` → `widgetId.substring()`
- 条件付き依存: `if (!(widgetId.endsWith("-browser-action")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("pageAction-"))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("pageAction-urlbar-"))` → `widgetId.substring()`
- 条件付き依存: `if (!(widgetId.startsWith("pageAction-urlbar-")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("pageAction-panel-"))` → `widgetId.substring()`
- 条件付き依存: `if (actionId)` → `lazy.PageActions.actionForID()`
- 条件付き依存: `if (actionId)` → `addonId()`
- 条件付き依存: `if (!(widgetId.startsWith("pageAction-")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("ext-keyset-id-"))` → `addonId()`
- 条件付き依存: `if (widgetId.startsWith("ext-keyset-id-"))` → `widgetId.substring()`
- 条件付き依存: `if (!(widgetId.startsWith("ext-keyset-id-")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("ext-key-id-"))` → `widgetId.substring()`
- 条件付き依存: `if (widgetId.startsWith("ext-key-id-"))` → `widgetId.endsWith()`
- 条件付き依存: `if (widgetId.endsWith("-sidebar-action"))` → `addonId()`
- 条件付き依存: `if (widgetId.endsWith("-sidebar-action"))` → `widgetId.substring()`
- 参照: `"-browser-action".length`, `"-sidebar-action".length`, `"ext-key-id-".length`, `"ext-keyset-id-".length`, `"pageAction-panel-".length`, `"pageAction-urlbar-".length`, `action?._isMozillaAction`, `widgetId.length`

## addonId()
- 位置: L227-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `KNOWN_ADDONS.indexOf()`
- 条件付き依存: `if (pos < 0)` → `KNOWN_ADDONS.push()`
- 参照: `KNOWN_ADDONS.length`

## getOpenTabsAndWinsCounts()
- 位置: L273-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `tab.getAttribute()`
- 参照: `win.gBrowser.tabs`, `win.gBrowser.tabs.length`
- XPCOM: `Services.wm`

## getPinnedTabsCount()
- 位置: L304-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `[...win.gBrowser.tabs].filter()`
- 参照: `[...win.gBrowser.tabs].filter(t => t.pinned).length`, `t.pinned`, `win.gBrowser.tabs`
- XPCOM: `Services.wm`

## isHttpURI()
- 位置: L323-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `uri.schemeIs()`

## addRestoredURI()
- 位置: L328-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._restoredURIsMap.set()`, `this.isHttpURI()`
- 参照: `uri.spec`

## onLocationChange()
- 位置: L336-471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry._recordTabCounts()`, `Glean.browserEngagement.uriCount.add()`, `Glean.browserEngagement.uriCountNormalMode.add()`, `Services.eTLD.getBaseDomain()`, `Services.prefs.getBoolPref()`, `browser.documentGlobal.gInitialPages.includes()`, `getOpenTabsAndWinsCounts()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this._domain24hrSet.get()`, `this._domain24hrSet.set()`, `this._restoredURIsMap.get()`, `this.isHttpURI()`
- 条件付き依存: `if ( !(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT) && webProgress.isTopLevel )` → `lazy.SearchSERPTelemetry.stopTrackingBrowser()`
- 条件付き依存: `if (shouldCountURI)` → `Glean.browserEngagement.unfilteredUriCount.add()`
- 条件付き依存: `if (this._restoredURIsMap.get(browser) === uriSpec)` → `this._restoredURIsMap.delete()`
- 条件付き依存: `if (!(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT))` → `lazy.SearchSERPTelemetry.updateTrackingStatus()`
- 条件付き依存: `if (!(!(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT)))` → `lazy.SearchSERPTelemetry.updateTrackingSinglePageApp()`
- 条件付き依存: `if (this._domainSet.size < MAX_UNIQUE_VISITED_DOMAINS)` → `this._domainSet.add()`
- 条件付き依存: `if (this._domainSet.size < MAX_UNIQUE_VISITED_DOMAINS)` → `Glean.browserEngagement.uniqueDomainsCount.set()`
- 条件付き依存: `if (timeoutId)` → `lazy.clearTimeout()`
- 条件付き依存: `if (lazy.gRecentVisitedOriginsExpiry)` → `lazy.setTimeout()`
- 条件付き依存: `if (lazy.gRecentVisitedOriginsExpiry)` → `this._domain24hrSet.delete()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_ERROR_PAGE`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `browser.documentGlobal`, `lazy.SearchSERPTelemetryUtils.ABANDONMENTS.NAVIGATION`, `lazy.gRecentVisitedOriginsExpiry`, `this._domainSet.size`, `uri.spec`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.eTLD` / `Services.prefs`

## reset()
- 位置: L476-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._domainSet.clear()`

## uniqueDomainsVisitedInPast24Hours()
- 位置: L484-486
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._domain24hrSet.size`

## resetUniqueDomainsVisitedInPast24Hours()
- 位置: L491-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clearTimeout()`, `this._domain24hrSet.clear()`, `this._domain24hrSet.forEach()`

## getTelemetryClientId()
- 位置: async L509-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClientID.getClientID()`

## getUpdateDirectory()
- 位置: L510-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## readProfileCountFile()
- 位置: async L511-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readUTF8()`

## writeProfileCountFile()
- 位置: async L512-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeUTF8()`

## init()
- 位置: L531-564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `this._doOnSavedTabGroupsChange()`, `this._doOnTabGroupChange()`, `this._doOnTabGroupExpandOrCollapse()`, `this._onSavedTabGroupsChangedTask.arm()`, `this._onTabsOpened()`, `this._recordPrefValues()`, `this._recordUITelemetry()`, `this._setupAfterRestore()`, `this.recordPinnedTabsCount()`
- 参照: `lazy.DeferredTask`, `this._inited`, `this._lastRecordLoadedTabCount`, `this._lastRecordTabCount`, `this._onSavedTabGroupsChangedTask`, `this._onTabGroupChangeTask`, `this._onTabGroupExpandOrCollapseTask`, `this._onTabsOpenedTask`
- XPCOM: `Services.obs` / `Services.prefs`

## maxTabCountGleanQuantity()
- 位置: L568-572
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Glean.browserEngagement.maxConcurrentTabCount`, `Glean.browserEngagement.maxConcurrentVerticalTabCount`, `lazy.sidebarVerticalTabs`

## updateMaxTabPinnedCount()
- 位置: L575-586
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.browserEngagement.maxConcurrentVerticalTabPinnedCount.set()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.browserEngagement.maxConcurrentTabPinnedCount.set()`
- 参照: `lazy.sidebarVerticalTabs`, `this.maxTabPinnedCount`

## recordPinnedTabsCount()
- 位置: L588-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPinnedTabsCount()`
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.pinnedTabs.count.sidebar.set()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.pinnedTabs.count.horizontalBar.set()`
- 参照: `lazy.sidebarVerticalTabs`

## _resetAddonIds()
- 位置: L599-601
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `KNOWN_ADDONS.length`

## afterSubsessionSplit()
- 位置: L606-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URICountListener.reset()`, `this._initMaxTabAndWindowCounts()`

## uninit()
- 位置: L621-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this._inited`
- XPCOM: `Services.obs`

## observe()
- 位置: L631-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onSavedTabGroupsChange()`, `this._onWindowOpen()`, `this._recordPrefValues()`, `this._recordWidgetChange()`, `this.afterSubsessionSplit()`
- 参照: `Services.appinfo.drawInTitlebar`
- XPCOM: `Services.appinfo`

## handleEvent()
- 位置: L659-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URICountListener.addRestoredURI()`, `getOpenTabsAndWinsCounts()`, `this._onTabClosed()`, `this._onTabGroupChange()`, `this._onTabGroupCreateByUser()`, `this._onTabGroupExpandOrCollapse()`, `this._onTabGroupRemoveRequested()`, `this._onTabGroupSave()`, `this._onTabGroupUngroup()`, `this._onTabMove()`, `this._onTabOpen()`, `this._onTabPinned()`, `this._onTabSelect()`, `this._onTabUnpinned()`, `this._recordTabCounts()`, `this._unregisterWindow()`
- 参照: `browser.currentURI`, `event.target`, `event.target.linkedBrowser`, `event.type`

## _initMaxTabAndWindowCounts()
- 位置: L717-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserEngagement.maxConcurrentWindowCount.set()`, `getOpenTabsAndWinsCounts()`, `this.maxTabCountGleanQuantity.set()`
- 参照: `counts.tabCount`, `counts.winCount`, `this.maxTabCount`, `this.maxWindowCount`

## _setupAfterRestore()
- 位置: L730-743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.wm.getEnumerator()`, `this._initMaxTabAndWindowCounts()`, `this._registerWindow()`
- XPCOM: `Services.obs` / `Services.wm`

## _buildWidgetPositions()
- 位置: L745-827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.xulStore.getValue()`, `lazy.CustomizableUI.getWidgetsInArea()`, `toolbarState()`, `widget.id.startsWith()`, `widgetMap.set()`
- 条件付き依存: `if (action.pinnedToUrlbar)` → `widgetMap.set()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `BROWSER_UI_CONTAINER_IDS.PersonalToolbar`, `Services.appinfo.drawInTitlebar`, `action.id`, `action.pinnedToUrlbar`, `lazy.CustomizableUI.areas`, `lazy.PageActions.actions`, `widget.id`
- XPCOM: `Services.appinfo` / `Services.xulStore`

## toolbarState()
- 位置: L748-770
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.xulStore.getValue()`
- 条件付き依存: `if (nodeId == "PersonalToolbar")` → `Services.prefs.getCharPref()`
- 参照: `AppConstants.BROWSER_CHROME_URL`
- XPCOM: `Services.prefs` / `Services.xulStore`

## _getWidgetID()
- 位置: L829-936
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.classList.contains()`, `node.classList?.contains()`, `node.getRootNode()`, `node.hasAttribute()`, `node.parentElement.id.includes()`, `this._getWidgetID()`
- 条件付き依存: `if (node.classList?.contains("share-copy-link"))` → `node.closest()`
- 条件付き依存: `if (node.ownerDocument.URL == AppConstants.BROWSER_CHROME_URL)` → `node.closest()`
- 条件付き依存: `if (node.ownerDocument.URL == AppConstants.BROWSER_CHROME_URL)` → `CSS.escape()`
- 条件付き依存: `if (node.closest(`#${CSS.escape(area)}`))` → `lazy.CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (node.closest(`#${CSS.escape(area)}`))` → `node.closest()`
- 条件付き依存: `if (node.closest(`#${CSS.escape(area)}`))` → `CSS.escape()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `node.getRootNode()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `host.closest()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `this._getWidgetID()`
- 条件付き依存: `if (node.localName != "key")` → `possibleAttributes.unshift()`
- 条件付き依存: `if (node.hasAttribute(idAttribute))` → `node.getAttribute()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `lazy.CustomizableUI.areas`, `node.getRootNode().host`, `node.id`, `node.localName`, `node.ownerDocument.URL`, `node.parentElement`, `settingControl.setting.id`, `settingControl?.setting?.id`, `shareItem.browsersToShare`

## _getBrowserWidgetContainer()
- 位置: L938-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `container.contains()`, `node.closest()`, `node.getAttribute()`, `node.ownerDocument.getElementById()`
- 参照: `BROWSER_UI_CONTAINER_IDS.tabContextMenu`

## _getWidgetContainer()
- 位置: L956-990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.getRootNode()`, `url.startsWith()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `node.getRootNode()`
- 条件付き依存: `if (url == AppConstants.BROWSER_CHROME_URL)` → `this._getBrowserWidgetContainer()`
- 条件付き依存: `if ( url.startsWith("about:preferences") || url.startsWith("about:settings") )` → `node.closest()`
- 条件付き依存: `if ( url.startsWith("about:preferences") || url.startsWith("about:settings") )` → `container.getAttribute()`
- 条件付き依存: `if ( url.startsWith("about:preferences") || url.startsWith("about:settings") )` → `PREFERENCES_PANES.includes()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `node.getRootNode().host`, `node.localName`, `node.ownerDocument`

## ignoreEvent()
- 位置: L994-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IGNORABLE_EVENTS.set()`

## _recordCommand()
- 位置: L998-1122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IGNORABLE_EVENTS.get()`, `UI_TARGET_ELEMENTS.get()`, `node.classList?.contains()`, `node.getAttribute()`, `node.ownerDocument.URL.startsWith()`, `sourceEvent.target.contains()`, `targetElements.has()`, `this._getWidgetContainer()`, `this._getWidgetID()`, `this.lastClickTarget?.get()`, `url.schemeIs()`
- 条件付き依存: `if (sourceEvent.type == "click")` → `Cu.getWeakReference()`
- 条件付き依存: `if (sourceEvent.type === "command")` → `PLACES_OPEN_COMMANDS.includes()`
- 条件付き依存: `if ( PLACES_OPEN_COMMANDS.includes(command) || parentNode?.parentNode?.id === PLACES_OPEN_IN_CONTAINER_TAB_MENU_ID )` → `ownerDocument.getElementById()`
- 条件付き依存: `if (item && source)` → `this.recordInteractionEvent()`
- 条件付き依存: `if (isAboutPreferences)` → `node.documentGlobal.recordSettingChangeTelemetry()`
- 条件付き依存: `if (item && source)` → `source .replace(/-/g, "_") .replace()`
- 条件付き依存: `if (item && source)` → `source .replace()`
- 条件付き依存: `if (item && source)` → `p.toUpperCase()`
- 条件付き依存: `if (item && source)` → `Glean.browserUiInteraction[name]?.[telemetryId(item)].add()`
- 条件付き依存: `if (item && source)` → `telemetryId()`
- 条件付き依存: `if (item && source)` → `SET_USAGECOUNT_PREF_BUTTONS.includes()`
- 条件付き依存: `if (SET_USAGECOUNT_PREF_BUTTONS.includes(item))` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (SET_USAGECOUNT_PREF_BUTTONS.includes(item))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (item && source)` → `SET_USAGE_PREF_BUTTONS.includes()`
- 条件付き依存: `if (SET_USAGE_PREF_BUTTONS.includes(item))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (ENTRYPOINT_TRACKED_CONTEXT_MENU_IDS[source])` → `this._getWidgetContainer()`
- 条件付き依存: `if (ENTRYPOINT_TRACKED_CONTEXT_MENU_IDS[source])` → `node.closest()`
- 条件付き依存: `if (triggerContainer)` → `this.recordInteractionEvent()`
- 条件付き依存: `if (triggerContainer)` → `contextMenu .replace(/-/g, "_") .replace()`
- 条件付き依存: `if (triggerContainer)` → `contextMenu .replace()`
- 条件付き依存: `if (triggerContainer)` → `p.toUpperCase()`
- 条件付き依存: `if (triggerContainer)` → `Glean.browserUiInteraction[name]?.[telemetryId(triggerContainer)].add()`
- 条件付き依存: `if (triggerContainer)` → `telemetryId()`
- 参照: `Glean.browserUiInteraction`, `event.type`, `node.closest("menupopup")?.triggerNode`, `node.localName`, `node.parentNode`, `node?.parentNode`, `ownerDocument.getElementById(PLACES_CONTEXT_MENU_ID).triggerNode`, `parentNode?.parentNode?.id`, `sourceEvent.button`, `sourceEvent.originalTarget`, `sourceEvent.originalTarget?.localName`, `sourceEvent.sourceEvent`, `sourceEvent.target`, `sourceEvent.target.localName`, `sourceEvent.target.ownerDocument.documentURIObject`, `sourceEvent.type`, `this.lastClickTarget`
- XPCOM: `Services.prefs`

## recordInteractionEvent()
- 位置: L1127-1150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.browserUsage.interaction.record()`, `telemetryId()`
- 条件付き依存: `if (!this._flowId || this._flowIdTS + FLOW_IDLE_TIME < ChromeUtils.now())` → `GleanPings.prototypeNoCodeEvents.submit()`
- 条件付き依存: `if (!this._flowId || this._flowIdTS + FLOW_IDLE_TIME < ChromeUtils.now())` → `Services.uuid.generateUUID()`
- 参照: `this._flowId`, `this._flowIdTS`
- XPCOM: `Services.uuid`

## _addUsageListeners()
- 位置: L1155-1160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UI_TARGET_ELEMENTS.keys()`, `UI_TARGET_ELEMENTS.keys().forEach()`, `this._recordCommand()`, `win.addEventListener()`

## recordWidgetChange()
- 位置: L1168-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._recordWidgetChange()`
- 条件付き依存: `if (newPos == "nav-bar")` → `lazy.CustomizableUI.getPlacementOfWidget()`

## recordToolbarVisibility()
- 位置: L1187-1196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordWidgetChange()`

## _recordWidgetChange()
- 位置: L1198-1256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUi.customizedWidgets[key].add()`, `telemetryId()`, `this.widgetMap.get()`
- 条件付き依存: `if (widgetId == "urlbar-container")` → `lazy.CustomizableUI.getWidgetsInArea()`
- 条件付き依存: `if (widgetId == "urlbar-container")` → `widget.id.startsWith()`
- 条件付き依存: `if (widgetId == "urlbar-container")` → `this._recordWidgetChange()`
- 条件付き依存: `if (newPos)` → `this.widgetMap.set()`
- 条件付き依存: `if (!(newPos))` → `this.widgetMap.delete()`
- 参照: `Glean.browserUi.customizedWidgets`, `this.widgetMap`, `widget.id`

## _recordUITelemetry()
- 位置: L1258-1277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserUi.mirrorForToolbarWidgets[key].set()`, `telemetryId()`, `this._buildWidgetPositions()`, `this.widgetMap.entries()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `Glean.browserUi.toolbarWidgets.set()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `this.widgetMap .entries() .map()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `this.widgetMap .entries()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `telemetryId()`
- 参照: `Glean.browserUi`, `Glean.browserUi.mirrorForToolbarWidgets`, `this.widgetMap`

## _recordPrefValues()
- 位置: L1284-1287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordNovaEnabledValue()`, `this._recordOpenNextToActiveTabSettingValue()`

## _isOpenNextToActiveTabSettingEnabled()
- 位置: L1292-1300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.externalLinkHandling.getVariable()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md)

## _recordOpenNextToActiveTabSettingValue()
- 位置: L1302-1306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.linkHandling.openNextToActiveTabSettingsEnabled.set()`, `this._isOpenNextToActiveTabSettingEnabled()`

## _recordNovaEnabledValue()
- 位置: L1308-1312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.nova.enabled.set()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## _registerWindow()
- 位置: L1319-1340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addUsageListeners()`, `win.addEventListener()`, `win.gBrowser.addTabsProgressListener()`, `win.gBrowser.tabContainer.addEventListener()`

## _unregisterWindow()
- 位置: L1345-1367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.defaultView.gBrowser.removeTabsProgressListener()`, `win.defaultView.gBrowser.tabContainer.removeEventListener()`, `win.removeEventListener()`

## _onTabOpen()
- 位置: L1375-1422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event?.target?.getAttribute()`, `this._onTabsOpenedTask.arm()`, `this._onTabsOpenedTask.disarm()`
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.browserEngagement.verticalTabOpenEventCount.add()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.browserEngagement.tabOpenEventCount.add()`
- 条件付き依存: `if (event?.target?.group)` → `Glean.tabgroup.tabInteractions.new.add()`
- 条件付き依存: `if (event.detail?.fromExternal)` → `this._isOpenNextToActiveTabSettingEnabled()`
- 条件付き依存: `if (event.detail?.fromExternal)` → `Glean.linkHandling.openFromExternalApp.record()`
- 条件付き依存: `if (wasOpenedNextToActiveTab)` → `externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.add()`
- 条件付き依存: `if (!(wasOpenedNextToActiveTab))` → `externalTabMovementRegistry.externallyOpenedTabsAtEndOfTabStrip.add()`
- 条件付き依存: `if (!(event.detail?.fromExternal))` → `externalTabMovementRegistry.internallyOpenedTabs.add()`
- 条件付き依存: `if (userContextId)` → `Glean.containers.containerTabOpened.record()`
- 条件付き依存: `if (userContextId)` → `String()`
- 参照: `event.detail?.containerSource`, `event.detail?.fromExternal`, `event.target`, `event?.target?.group`, `lazy.sidebarVerticalTabs`

## _onTabsOpened()
- 位置: L1427-1435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOpenTabsAndWinsCounts()`, `this._recordTabCounts()`
- 条件付き依存: `if (tabCount > this.maxTabCount)` → `this.maxTabCountGleanQuantity.set()`
- 参照: `this.maxTabCount`

## _onTabClosed()
- 位置: L1442-1485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event?.target?.getAttribute()`
- 条件付き依存: `if ( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_STRIP )` → `Glean.tabgroup.tabInteractions.close_tabstrip.add()`
- 条件付き依存: `if ( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_MENU || metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU )` → `Glean.tabgroup.tabInteractions.close_tabmenu.add()`
- 条件付き依存: `if (!( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_MENU || metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU ))` → `Glean.tabgroup.tabInteractions.close_tab_other.add()`
- 条件付き依存: `if (userContextId)` → `Glean.containers.containerTabClosed.record()`
- 条件付き依存: `if (userContextId)` → `String()`
- 条件付き依存: `if (event.target?.pinned)` → `getPinnedTabsCount()`
- 条件付き依存: `if (event.target?.pinned)` → `this.recordPinnedTabsCount()`
- 条件付き依存: `if (event.target?.pinned)` → `Glean.pinnedTabs.close.record()`
- 条件付き依存: `if (event.target)` → `Object.values(externalTabMovementRegistry).forEach()`
- 条件付き依存: `if (event.target)` → `Object.values()`
- 条件付き依存: `if (event.target)` → `set.delete()`
- 参照: `event.detail.metricsContext`, `event.target`, `event.target?.group`, `event.target?.pinned`, `lazy.TabMetrics.METRIC_SOURCE.TAB_MENU`, `lazy.TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU`, `lazy.TabMetrics.METRIC_SOURCE.TAB_STRIP`, `lazy.sidebarVerticalTabs`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`

## _onTabPinned()
- 位置: L1487-1502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.pinnedTabs.pin.record()`, `getPinnedTabsCount()`, `this.recordPinnedTabsCount()`, `this.updateMaxTabPinnedCount()`
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.browserEngagement.verticalTabPinnedEventCount.add()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.browserEngagement.tabPinnedEventCount.add()`
- 参照: `event.detail.metricsContext.telemetrySource`, `lazy.sidebarVerticalTabs`

## _onTabUnpinned()
- 位置: L1504-1506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordPinnedTabsCount()`

## _onTabGroupCreateByUser()
- 位置: L1508-1519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.createGroup.record()`, `this._onTabGroupChange()`
- 参照: `event.detail.metricsContext.telemetrySource`, `event.target.id`, `event.target.tabs.length`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `lazy.sidebarVerticalTabs`

## _onTabGroupSave()
- 位置: L1521-1534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.save.record()`, `this._onTabGroupChange()`
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.groupInteractions.save.add()`
- 参照: `event.detail`, `event.target.id`, `metricsContext.isUserTriggered`

## _onTabGroupChange()
- 位置: L1536-1539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onTabGroupChangeTask.arm()`, `this._onTabGroupChangeTask.disarm()`

## _onTabGroupUngroup()
- 位置: L1544-1558
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.ungroup.record()`
- 条件付き依存: `if ( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_GROUP_MENU )` → `Glean.tabgroup.groupInteractions.ungroup.add()`
- 参照: `event.detail`, `lazy.TabMetrics.METRIC_SOURCE.TAB_GROUP_MENU`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`

## _getSummaryStats()
- 位置: L1566-1580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `data.at()`, `data.reduce()`, `data.sort()`
- 参照: `data.length`

## _doOnTabGroupChange()
- 位置: L1582-1606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.tabCountInGroups.inside.set()`, `Glean.tabgroup.tabCountInGroups.outside.set()`, `Glean.tabgroup.tabsPerActiveGroup.average.set()`, `Glean.tabgroup.tabsPerActiveGroup.max.set()`, `Glean.tabgroup.tabsPerActiveGroup.median.set()`, `Glean.tabgroup.tabsPerActiveGroup.min.set()`, `Services.wm.getEnumerator()`, `tabGroupLengths.push()`, `this._getSummaryStats()`
- 参照: `group.tabs.length`, `win.gBrowser.tabGroups`, `win.gBrowser.tabs.length`
- XPCOM: `Services.wm`

## _onSavedTabGroupsChange()
- 位置: L1608-1611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onSavedTabGroupsChangedTask.arm()`, `this._onSavedTabGroupsChangedTask.disarm()`

## _doOnSavedTabGroupsChange()
- 位置: L1613-1624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.savedGroups.set()`, `Glean.tabgroup.tabsPerSavedGroup.average.set()`, `Glean.tabgroup.tabsPerSavedGroup.max.set()`, `Glean.tabgroup.tabsPerSavedGroup.median.set()`, `Glean.tabgroup.tabsPerSavedGroup.min.set()`, `lazy.SessionStore.getSavedTabGroups()`, `savedGroups.map()`, `this._getSummaryStats()`
- 参照: `group.tabs.length`, `savedGroups.length`

## _onTabGroupExpandOrCollapse()
- 位置: L1626-1629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onTabGroupExpandOrCollapseTask.arm()`, `this._onTabGroupExpandOrCollapseTask.disarm()`

## _doOnTabGroupExpandOrCollapse()
- 位置: L1631-1647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.activeGroups.collapsed.set()`, `Glean.tabgroup.activeGroups.expanded.set()`, `Services.wm.getEnumerator()`
- 参照: `group.collapsed`, `win.gBrowser.tabGroups`
- XPCOM: `Services.wm`

## _onTabGroupRemoveRequested()
- 位置: L1652-1662
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.delete.record()`
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.groupInteractions.delete.add()`
- 参照: `event.detail`, `event.target.id`, `lazy.TabMetrics.UNKNOWN_CONTEXT`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`

## _onTabMove()
- 位置: L1674-1719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[metricsContext.telemetrySource, groupType].join()`, `this._recordExternalTabMovement()`, `this._tabMovementsBySegment.get()`
- 条件付き依存: `if (tabMovementsRecord.numberAddedToTabGroup)` → `Glean.tabgroup.addTab.record()`
- 条件付き依存: `if (!tabMovementsRecord)` → `this._tabMovementsBySegment.delete()`
- 条件付き依存: `if (!tabMovementsRecord)` → `this._tabMovementsBySegment.set()`
- 条件付き依存: `if (!tabMovementsRecord)` → `this._updateTabMovementsRecord()`
- 条件付き依存: `if (!tabMovementsRecord)` → `deferredTask.arm()`
- 条件付き依存: `if (!(!tabMovementsRecord))` → `tabMovementsRecord.deferredTask.disarm()`
- 条件付き依存: `if (!(!tabMovementsRecord))` → `this._updateTabMovementsRecord()`
- 条件付き依存: `if (!(!tabMovementsRecord))` → `tabMovementsRecord.deferredTask.arm()`
- 参照: `event.detail`, `event.target.group`, `event.target.group.collapsed`, `lazy.DeferredTask`, `lazy.TabMetrics.METRIC_GROUP_TYPE.COLLAPSED`, `lazy.TabMetrics.METRIC_GROUP_TYPE.EXPANDED`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `lazy.sidebarVerticalTabs`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`, `tabMovementsRecord.numberAddedToTabGroup`

## _updateTabMovementsRecord()
- 位置: L1725-1744
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!previousTabState.tabGroupId && currentTabState.tabGroupId)` → `Glean.tabgroup.tabInteractions.add.add()`
- 条件付き依存: `if ( previousTabState.tabGroupId && previousTabState.tabGroupId == currentTabState.tabGroupId && previousTabState.tabIndex != currentTabState.tabIndex )` → `Glean.tabgroup.tabInteractions.reorder.add()`
- 条件付き依存: `if (previousTabState.tabGroupId && !currentTabState.tabGroupId)` → `Glean.tabgroup.tabInteractions.remove_same_window.add()`
- 参照: `currentTabState.tabGroupId`, `currentTabState.tabIndex`, `event.detail`, `previousTabState.tabGroupId`, `previousTabState.tabIndex`, `record.numberAddedToTabGroup`

## _recordExternalTabMovement()
- 位置: L1750-1766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `externalTabMovementRegistry.internallyOpenedTabs.has()`
- 条件付き依存: `if (externalTabMovementRegistry.internallyOpenedTabs.has(event.target))` → `Glean.browserUiInteraction.tabMovement.not_from_external_app.add()`
- 条件付き依存: `if (!(externalTabMovementRegistry.internallyOpenedTabs.has(event.target)))` → `externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.has()`
- 条件付き依存: `if ( externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.has( event.target ) )` → `Glean.browserUiInteraction.tabMovement.from_external_app_next_to_active_tab.add()`
- 条件付き依存: `if (!( externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.has( event.target ) ))` → `externalTabMovementRegistry.externallyOpenedTabsAtEndOfTabStrip.has()`
- 条件付き依存: `if ( externalTabMovementRegistry.externallyOpenedTabsAtEndOfTabStrip.has( event.target ) )` → `Glean.browserUiInteraction.tabMovement.from_external_app_tab_strip_end.add()`
- 参照: `event.target`

## _onTabSelect()
- 位置: L1768-1781
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target.group)` → `interaction.add()`
- 条件付き依存: `if (event.target.pinned)` → `counter.add()`
- 参照: `Glean.pinnedTabs.activations.horizontalBar`, `Glean.pinnedTabs.activations.sidebar`, `Glean.tabgroup.tabInteractions.activate_collapsed`, `Glean.tabgroup.tabInteractions.activate_expanded`, `event.target.group`, `event.target.group.collapsed`, `event.target.pinned`, `lazy.sidebarVerticalTabs`

## _onWindowOpen()
- 位置: L1788-1820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.addEventListener()`
- 参照: `Ci.nsIDOMWindow`
- XPCOM: [`nsIDOMWindow`](../../dom/base/nsISlowScriptDebug.idl.md)

## onLoad()
- 位置: L1794-1818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserEngagement.windowOpenEventCount.add()`, `getOpenTabsAndWinsCounts()`, `this._onTabOpen()`, `this._registerWindow()`, `win.document.documentElement.getAttribute()`, `win.removeEventListener()`
- 条件付き依存: `if (counts.winCount > this.maxWindowCount)` → `Glean.browserEngagement.maxConcurrentWindowCount.set()`
- 参照: `counts.winCount`, `this.maxWindowCount`

## _recordTabCounts()
- 位置: L1833-1853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if ( tabCount !== undefined && currentTime > this._lastRecordTabCount + MINIMUM_TAB_COUNT_INTERVAL_MS )` → `Glean.browserEngagement.tabCount.accumulateSingleSample()`
- 条件付き依存: `if ( loadedTabCount !== undefined && currentTime > this._lastRecordLoadedTabCount + MINIMUM_TAB_COUNT_INTERVAL_MS )` → `Glean.browserEngagement.loadedTabCount.accumulateSingleSample()`
- 参照: `this._lastRecordLoadedTabCount`, `this._lastRecordTabCount`

## _checkProfileCountFileSchema()
- 位置: L1855-1872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `fileData.profileTelemetryIds`, `fileData.version`

## reportProfileCount()
- 位置: async L1875-1960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.Policy.getTelemetryClientId()`, `BrowserUsageTelemetry.Policy.getUpdateDirectory()`, `BrowserUsageTelemetry.Policy.readProfileCountFile()`, `BrowserUsageTelemetry._checkProfileCountFileSchema()`, `Glean.browserEngagement.profileCount.set()`, `JSON.parse()`, `Math.max()`, `fileData.profileTelemetryIds.includes()`, `profileCountFile.append()`
- 条件付き依存: `if (!(ex.name == "NotFoundError"))` → `console.error()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `fileData.profileTelemetryIds.push()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `BrowserUsageTelemetry.Policy.writeProfileCountFile()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `JSON.stringify()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `console.error()`
- 参照: `ex.name`, `fileData.profileTelemetryIds.length`, `profileCountFile.path`, `updateDirectory.leafName`, `updateDirectory.parent.parent`

## collectInstallationTelemetry()
- 位置: async L1975-2105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-package-manager;1"].createInstance()`, `Services.prefs.getStringPref()`, `Services.sysinfo.getProperty()`
- 条件付き依存: `if (pfn)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (pfn)` → `wpm.getInstalledDate()`
- 条件付き依存: `if (pfn)` → `getInstallData()`
- 条件付き依存: `if (pfn)` → `install_data.msixInstalls.has(pfn).toString()`
- 条件付き依存: `if (pfn)` → `install_data.msixInstalls.has()`
- 条件付き依存: `if (pfn)` → `install_data.msixInstalls.delete()`
- 条件付き依存: `if (pfn)` → `(!!install_data.installPaths.size).toString()`
- 条件付き依存: `if (pfn)` → `(!!install_data.msixInstalls.size).toString()`
- 条件付き依存: `if (!dataPath)` → `Services.dirsvc.get()`
- 条件付き依存: `if (!dataPath)` → `dataPath.append()`
- 条件付き依存: `if (!(pfn))` → `IOUtils.read()`
- 条件付き依存: `if (!(pfn))` → `new TextDecoder("utf-16").decode()`
- 条件付き依存: `if (!(pfn))` → `JSON.parse()`
- 条件付き依存: `if (!(pfn))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(pfn))` → `getInstallData()`
- 条件付き依存: `if (!(pfn))` → `data.admin_user.toString()`
- 条件付き依存: `if (!(pfn))` → `data.install_existed.toString()`
- 条件付き依存: `if (!(pfn))` → `data.profdir_existed.toString()`
- 条件付き依存: `if (!(pfn))` → `(!!install_data.installPaths.size).toString()`
- 条件付き依存: `if (!(pfn))` → `(!!install_data.msixInstalls.size).toString()`
- 条件付き依存: `if (data.installer_type == "full")` → `data.silent.toString()`
- 条件付き依存: `if (data.installer_type == "full")` → `data.from_msi.toString()`
- 条件付き依存: `if (data.installer_type == "full")` → `data.default_path.toString()`
- 参照: `AppConstants.MOZ_APP_VERSION`, `AppConstants.MOZ_BUILDID`, `AppConstants.platform`, `Ci.nsIFile`, `Ci.nsIWindowsPackageManager`, `data.build_id`, `data.install_timestamp`, `data.installer_type`, `data.version`, `dataPath.path`, `ex.name`, `extra.admin_user`, `extra.build_id`, `extra.default_path`, `extra.from_msi`, `extra.install_existed`, `extra.other_inst`, `extra.other_msix_inst`, `extra.profdir_existed`, `extra.silent`, `extra.version`, `install_data.installPaths.size`, `install_data.msixInstalls.size`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / [`nsIWindowsPackageManager`](../../toolkit/system/windowsPackageManager/nsIWindowsPackageManager.idl.md) / `@mozilla.org/windows-package-manager;1` → `mozilla::toolkit::system::nsWindowsPackageManager` (toolkit/system/windowsPackageManager/components.conf) / `Services.dirsvc` / `Services.prefs` / `Services.sysinfo`

## getInstallData()
- 位置: L1995-2017
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`, `lazy.WindowsInstallsInfo.getInstallPaths()`, `msixInstalls.add()`, `wpm .findUserInstalledPackages()`, `wpm .findUserInstalledPackages(msixPackagePrefixes) .forEach()`
- 条件付き依存: `if (pfn)` → `msixInstalls.delete()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("GreBinD", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## reportInstallationTelemetry()
- 位置: async L2107-2166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.collectInstallationTelemetry()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installation.firstSeenFull.record()`
- 条件付き依存: `if (installer_type == "stub")` → `Glean.installation.firstSeenStub.record()`
- 条件付き依存: `if (installer_type == "msix")` → `Glean.installation.firstSeenMsix.record()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.installerType.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.version.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.adminUser.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.installExisted.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.profdirExisted.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.otherInst.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.otherMsixInst.set()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installationFirstSeen.silent.set()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installationFirstSeen.fromMsi.set()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installationFirstSeen.defaultPath.set()`
- 参照: `data?.installer_type`, `extra.admin_user`, `extra.default_path`, `extra.from_msi`, `extra.install_existed`, `extra.other_inst`, `extra.other_msix_inst`, `extra.profdir_existed`, `extra.silent`, `extra.version`

## getUniqueDomainsVisitedInPast24Hours()
- 位置: L2170-2172
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `URICountListener.uniqueDomainsVisitedInPast24Hours`
