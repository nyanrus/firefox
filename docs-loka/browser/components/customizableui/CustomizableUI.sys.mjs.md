# browser/components/customizableui/CustomizableUI.sys.mjs

source: browser/components/customizableui/CustomizableUI.sys.mjs
source-hash: 76cab7f8e4630119c8f166f14bfc5a781f49f5fd
lines: 8679

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `CustomizableUI.getWidgetIdsInArea()`, `CustomizableUIInternal.initialize()`, `CustomizableUIInternal.updateTabStripOrientation()`, `Object.freeze()`, `Services.prefs.setBoolPref()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `gAreas .get()`, `gAreas .get(CustomizableUI.AREA_NAVBAR) .get()`, `lazy.log.debug()`, `navbarPlacements.includes()`

## initialize()
- 位置: L320-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.policies.isAllowed()`, `Services.prefs.addObserver()`, `addons.find()`, `gAreas.keys()`, `lazy.AddonManager.addAddonListener()`, `lazy.AddonManager.getAddonsByTypes()`, `lazy.AddonManagerPrivate.databaseReady.then()`, `lazy.log.debug()`, `this._setAutoTouchModeDefault()`, `this.addListener()`, `this.defineBuiltInWidgets()`, `this.initializeForTabsOrientation()`, `this.loadSavedState()`, `this.markObsoleteBuiltinButtonsSeen()`, `this.reconcileSidebarPrefs()`, `this.registerArea()`, `this.updateForNewProtonVersion()`, `this.updateForNewVersion()`
- 条件付き依存: `if (!Services.appinfo.nativeMenubar)` → `this.registerArea()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.AREA_MENUBAR`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.TYPE_PANEL`, `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.verticalTabsEnabled`, `Services.appinfo.nativeMenubar`, `addon.id`, `addon.isActive`, `lazy.ippEnabled`, `lazy.resetPBMToolbarButtonEnabled`, `lazy.sidebarRevampEnabled`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.policies` / `Services.prefs`

## _setAutoTouchModeDefault()
- 位置: L464-471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getDefaultBranch()`, `Services.prefs .getDefaultBranch("") .setBoolPref()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onEnabled()
- 位置: L480-484
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `addon.type`

## builtinAreas()
- 位置: L491-497
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `this.builtinToolbars`

## builtinToolbars()
- 位置: L505-515
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `toolbars.add()`
- 参照: `AppConstants.platform`, `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.AREA_MENUBAR`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`

## defineBuiltInWidgets()
- 位置: L521-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createBuiltinWidget()`
- 参照: `lazy.CustomizableWidgets`

## updateForNewVersion()
- 位置: L532-1048
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (widget.defaultArea && widget._introducedInVersion === "pref")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (widget._introducedInVersion === "pref")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(widget._introducedInVersion > currentVersion))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( widget._introducedByPref && Services.prefs.getBoolPref(widget._introducedByPref) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (shouldAdd)` → `gFuturePlacements.get()`
- 条件付き依存: `if (futurePlacements)` → `futurePlacements.add()`
- 条件付き依存: `if (!(futurePlacements))` → `gFuturePlacements.set()`
- 条件付き依存: `if (shouldSetPref)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( currentVersion < 7 && gSavedState.placements[CustomizableUI.AREA_NAVBAR] )` → `newPlacements.includes()`
- 条件付き依存: `if (!newPlacements.includes(button))` → `newPlacements.push()`
- 条件付き依存: `if (!newPlacements.includes("sidebar-button"))` → `newPlacements.unshift()`
- 条件付き依存: `if (!AppConstants.MOZ_DEV_EDITION)` → `defaultPlacements.splice()`
- 条件付き依存: `if (currentVersion < 8 && gSavedState.placements["PanelUI-contents"])` → `savedPanelPlacements.filter()`
- 条件付き依存: `if (currentVersion < 8 && gSavedState.placements["PanelUI-contents"])` → `defaultPlacements.includes()`
- 条件付き依存: `if (currentVersion < 9 && gSavedState.placements["nav-bar"])` → `placements.includes()`
- 条件付き依存: `if (placements.includes("urlbar-container"))` → `placements.indexOf()`
- 条件付き依存: `if (placements.includes("urlbar-container"))` → `placements[urlbarIndex - 1].startsWith()`
- 条件付き依存: `if ( urlbarIndex == 0 || !placements[urlbarIndex - 1].startsWith(kSpecialWidgetPfx + "spring") )` → `placements.splice()`
- 条件付き依存: `if (placements.includes("urlbar-container"))` → `placements[secondSpringIndex].startsWith()`
- 条件付き依存: `if ( secondSpringIndex == placements.length || !placements[secondSpringIndex].startsWith( kSpecialWidgetPfx + "spring" ) )` → `placements.splice()`
- 条件付き依存: `if (placements.includes("bookmarks-menu-button"))` → `placements.indexOf()`
- 条件付き依存: `if (placements.includes("bookmarks-menu-button"))` → `placements.splice()`
- 条件付き依存: `if (currentVersion < 10)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 10)` → `placements.includes()`
- 条件付き依存: `if (placements.includes("webcompat-reporter-button"))` → `placements.splice()`
- 条件付き依存: `if (placements.includes("webcompat-reporter-button"))` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 11)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 11)` → `placements.indexOf()`
- 条件付き依存: `if (existingIndex != -1)` → `placements.splice()`
- 条件付き依存: `if (navbarPlacements)` → `navbarPlacements.indexOf()`
- 条件付き依存: `if (navbarPlacements)` → `this.matchingSpecials()`
- 条件付き依存: `if (navbarPlacements)` → `navbarPlacements.splice()`
- 条件付き依存: `if (currentVersion < 12)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 12)` → `placements.indexOf()`
- 条件付き依存: `if (buttonIndex != -1)` → `placements.splice()`
- 条件付き依存: `if (currentVersion < 13)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 13)` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 14)` → `this.builtinAreas.has()`
- 条件付き依存: `if (navbarPlacements)` → `navbarPlacements.push()`
- 条件付き依存: `if (currentVersion < 18)` → `tabstripPlacements.includes()`
- 条件付き依存: `if ( tabstripPlacements && !tabstripPlacements.includes("firefox-view-button") )` → `tabstripPlacements.unshift()`
- 条件付き依存: `if (currentVersion < 19)` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(widgetId))` → `extWidgets.push()`
- 条件付き依存: `if (!(CustomizableUI.isWebExtensionWidget(widgetId)))` → `builtInWidgets.push()`
- 条件付き依存: `if (currentVersion < 21)` → `navbarPlacements.includes()`
- 条件付き依存: `if (!navbarPlacements.includes("vertical-spacer"))` → `navbarPlacements.indexOf()`
- 条件付き依存: `if (!navbarPlacements.includes("vertical-spacer"))` → `gSavedState.placements[CustomizableUI.AREA_NAVBAR].splice()`
- 条件付き依存: `if (currentVersion < 22)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (navbarPlacements[0] === "sidebar-button")` → `navbarPlacements.shift()`
- 条件付き依存: `if (navbarPlacements[0] === "sidebar-button")` → `navbarPlacements.push()`
- 条件付き依存: `if (currentVersion < 23)` → `navbarPlacements.indexOf()`
- 条件付き依存: `if (buttonIndex != -1)` → `navbarPlacements.splice()`
- 条件付き依存: `if (currentVersion < 24)` → `navbarPlacements.includes()`
- 条件付き依存: `if ( navbarPlacements && !navbarPlacements.includes("reset-pbm-toolbar-button") )` → `navbarPlacements.push()`
- 条件付き依存: `if (currentVersion < 25)` → `firefoxViewArea?.indexOf()`
- 条件付き依存: `if (firefoxViewArea?.[defaultIndex] === "firefox-view-button")` → `JSON.parse()`
- 条件付き依存: `if (firefoxViewArea?.[defaultIndex] === "firefox-view-button")` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (firefoxViewArea?.[defaultIndex] === "firefox-view-button")` → `console.error()`
- 条件付き依存: `if (!shouldKeepFirefoxView)` → `firefoxViewArea.splice()`
- 条件付き依存: `if (currentVersion < 26)` → `insertBeforeAllTabs()`
- 条件付き依存: `if (currentVersion < 26)` → `CustomizableUIInternal.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `CustomizableUIInternal.saveHorizontalTabStripState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `insertBeforeAllTabs()`
- 条件付き依存: `if (currentVersion < 27)` → `areaPlacements()`
- 条件付き依存: `if (currentVersion < 27)` → `tabstrip.includes()`
- 条件付き依存: `if (currentVersion < 27)` → `navbar.includes()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `tabstrip.splice()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `tabstrip.indexOf()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `navbar.splice()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `navbar.indexOf()`
- 条件付き依存: `if (currentVersion < 27)` → `gSeenWidgets.has()`
- 条件付き依存: `if (currentVersion < 27)` → `Object.values(gSavedState.placements).some()`
- 条件付き依存: `if (currentVersion < 27)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 27)` → `Array.isArray()`
- 条件付き依存: `if (currentVersion < 27)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 27)` → `placeBeforeSwitcher()`
- 条件付き依存: `if (currentVersion < 27)` → `CustomizableUIInternal.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `placeBeforeSwitcher()`
- 条件付き依存: `if (currentVersion < 27)` → `CustomizableUIInternal.getSavedVerticalSnapshotState()`
- 条件付き依存: `if (verticalSnapshot.length)` → `placeBeforeSwitcher()`
- 条件付き依存: `if (verticalSnapshot.length)` → `CustomizableUIInternal.saveNavBarWhenVerticalTabsState()`
- 条件付き依存: `if (currentVersion < 28)` → `restoreFlexibleSpace()`
- 条件付き依存: `if (currentVersion < 28)` → `CustomizableUIInternal.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `restoreFlexibleSpace()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `gSavedState.currentVersion`, `gSavedState.placements`, `horizontalSnapshot.length`, `navbarPlacements.length`, `placements.length`, `savedPanelPlacements.length`, `verticalSnapshot.length`, `widget._introducedByPref`, `widget._introducedInVersion`, `widget.defaultArea`, `widget.id`
- XPCOM: `Services.prefs`

## insertBeforeAllTabs()
- 位置: L908-920
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `placements.indexOf()`, `placements[alltabsIndex - 1].startsWith()`
- 条件付き依存: `if ( alltabsIndex > 0 && !placements[alltabsIndex - 1].startsWith(kSpecialWidgetPfx + "spring") )` → `placements.splice()`

## areaPlacements()
- 位置: L940-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `gSavedState.placements`

## placeBeforeSwitcher()
- 位置: L947-963
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `placements.indexOf()`
- 条件付き依存: `if (buttonIndex == appendedIndex)` → `placements.splice()`
- 条件付き依存: `if (buttonIndex == -1 && reserveSlot)` → `placements.splice()`

## restoreFlexibleSpace()
- 位置: L1010-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `CustomizableUIInternal.matchingSpecials()`, `afterTabs.some()`, `placements.includes()`, `placements.indexOf()`, `placements.slice()`
- 条件付き依存: `if ( !afterTabs.some(id => CustomizableUIInternal.matchingSpecials(id, "spring") ) )` → `placements.push()`
- 参照: `placements.length`

## updateForNewProtonVersion()
- 位置: L1056-1108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- 条件付き依存: `if (!placements)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (currentVersion < 1)` → `lazy.HomePage.get()`
- 条件付き依存: `if (currentVersion < 1)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 1)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (currentVersion < 1)` → `Services.policies.isAllowed()`
- 条件付き依存: `if ( placements.includes("home-button") && !Services.prefs.getBoolPref(kPrefHomeButtonUsed) && (homePage == "about:home" || homePage == "about:blank") && Service...)` → `placements.splice()`
- 条件付き依存: `if ( placements.includes("home-button") && !Services.prefs.getBoolPref(kPrefHomeButtonUsed) && (homePage == "about:home" || homePage == "about:blank") && Service...)` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 2)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 2)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( placements.includes("library-button") && !Services.prefs.getBoolPref(kPrefLibraryButtonUsed) )` → `placements.splice()`
- 条件付き依存: `if ( placements.includes("library-button") && !Services.prefs.getBoolPref(kPrefLibraryButtonUsed) )` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 3)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 3)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( placements.includes("sidebar-button") && !Services.prefs.getBoolPref(kPrefSidebarButtonUsed) )` → `placements.splice()`
- 条件付き依存: `if ( placements.includes("sidebar-button") && !Services.prefs.getBoolPref(kPrefSidebarButtonUsed) )` → `placements.indexOf()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `gSavedState?.placements`
- XPCOM: `Services.policies` / `Services.prefs`

## markObsoleteBuiltinButtonsSeen()
- 位置: L1115-1131
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (version == kVersion)` → `gSeenWidgets.add()`
- 参照: `gSavedState.currentVersion`

## placeNewDefaultWidgetsInArea()
- 位置: L1141-1213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defaultPlacements.indexOf()`, `gAreas.get()`, `gAreas.get(aArea).has()`, `gFuturePlacements.get()`, `gPalette.get()`, `savedPlacements.includes()`, `this.saveState()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") )` → `gAreas .get(aArea) .get()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") )` → `gAreas .get()`
- 条件付き依存: `if (!( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") ))` → `gAreas.get(aArea).get()`
- 条件付き依存: `if (!( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") ))` → `gAreas.get()`
- 条件付き依存: `if (i === 0 && i === defaultWidgetIndex)` → `savedPlacements.splice()`
- 条件付き依存: `if (i === 0 && i === defaultWidgetIndex)` → `futurePlacedWidgets.delete()`
- 条件付き依存: `if (i)` → `savedPlacements.indexOf()`
- 条件付き依存: `if (previousWidgetIndex != -1)` → `savedPlacements.splice()`
- 条件付き依存: `if (previousWidgetIndex != -1)` → `futurePlacedWidgets.delete()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `CustomizableUI.verticalTabsEnabled`, `defaultPlacements.length`, `gSavedState.placements`, `savedPlacements.length`, `widget._introducedByPref`, `widget._introducedInVersion`, `widget.defaultArea`, `widget.id`, `widget.source`

## getCustomizationTarget()
- 位置: L1220-1241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElement.hasAttribute()`
- 条件付き依存: `if ( !aElement._customizationTarget && aElement.hasAttribute("customizable") )` → `aElement.getAttribute()`
- 条件付き依存: `if (id)` → `aElement.ownerDocument.getElementById()`
- 参照: `aElement._customizationTarget`

## wrapWidget()
- 位置: L1259-1284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gGroupWrapperCache.has()`, `gGroupWrapperCache.set()`, `this.getWidgetProvider()`
- 条件付き依存: `if (gGroupWrapperCache.has(aWidgetId))` → `gGroupWrapperCache.get()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_API)` → `gPalette.get()`
- 条件付き依存: `if (!widget.wrapper)` → `gGroupWrapperCache.set()`
- 参照: `CustomizableUI.PROVIDER_API`, `widget.wrapper`

## registerArea()
- 位置: L1292-1374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^[a-z0-9-_]{1,}$/i.test()`, `Array.isArray()`, `allTypes.includes()`, `gAreas.get()`, `gAreas.has()`, `kImmutableProperties.has()`, `props.get()`, `props.has()`, `props.set()`
- 条件付き依存: `if (!props.has("type"))` → `props.set()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `props.has()`
- 条件付き依存: `if (!props.has("defaultCollapsed"))` → `props.set()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `props.has()`
- 条件付き依存: `if (!allTypes.includes(props.get("type")))` → `props.get()`
- 条件付き依存: `if (!props.has("defaultPlacements"))` → `props.set()`
- 条件付き依存: `if (!areaIsKnown)` → `gAreas.set()`
- 条件付き依存: `if (!areaIsKnown)` → `this.placeNewDefaultWidgetsInArea()`
- 条件付き依存: `if (!areaIsKnown)` → `props.get()`
- 条件付き依存: `if (!areaIsKnown)` → `gPlacements.has()`
- 条件付き依存: `if ( props.get("type") == CustomizableUI.TYPE_TOOLBAR && !gPlacements.has(aName) )` → `lazy.log.debug()`
- 条件付き依存: `if ( props.get("type") == CustomizableUI.TYPE_TOOLBAR && !gPlacements.has(aName) )` → `gFuturePlacements.has()`
- 条件付き依存: `if (!gFuturePlacements.has(aName))` → `gFuturePlacements.set()`
- 条件付き依存: `if (!( props.get("type") == CustomizableUI.TYPE_TOOLBAR && !gPlacements.has(aName) ))` → `this.restoreStateForArea()`
- 条件付き依存: `if (!areaIsKnown)` → `gPendingBuildAreas.has()`
- 条件付き依存: `if (gPendingBuildAreas.has(aName))` → `gPendingBuildAreas.get()`
- 条件付き依存: `if (gPendingBuildAreas.has(aName))` → `this.registerToolbarNode()`
- 条件付き依存: `if (gPendingBuildAreas.has(aName))` → `gPendingBuildAreas.delete()`
- 参照: `CustomizableUI.TYPE_PANEL`, `CustomizableUI.TYPE_TOOLBAR`, `aProperties.defaultCollapsed`

## unregisterArea()
- 位置: L1381-1425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^[a-z0-9-_]{1,}$/i.test()`, `gAreas.delete()`, `gAreas.has()`, `gBuildAreas.delete()`, `gBuildAreas.get()`, `gFuturePlacements.delete()`, `gPlacements.get()`, `gPlacements.has()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`
- 条件付き依存: `if (placements)` → `placements.forEach()`
- 条件付き依存: `if (aDestroyPlacements)` → `gPlacements.delete()`
- 条件付き依存: `if (!(aDestroyPlacements))` → `gPlacements.set()`
- 条件付き依存: `if (existingAreaNodes)` → `this.notifyListeners()`
- 条件付き依存: `if (existingAreaNodes)` → `this.getCustomizationTarget()`
- 参照: `CustomizableUI.REASON_AREA_UNREGISTERED`, `this.removeWidgetFromArea`

## registerToolbarNode()
- 位置: L1431-1509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `areaProperties.get()`, `gAreas.get()`, `gBuildAreas.get()`, `gBuildAreas.get(area).has()`, `gBuildAreas.has()`, `gDirtyAreaCache.has()`, `gPalette.has()`, `gPlacements.get()`, `lazy.log.debug()`, `placements.every()`, `placements.some()`, `this.beginBatchUpdate()`, `this.builtinToolbars.has()`, `this.endBatchUpdate()`, `this.getCustomizationTarget()`, `this.notifyListeners()`, `this.registerBuildArea()`
- 条件付き依存: `if (!areaProperties)` → `gPendingBuildAreas.has()`
- 条件付き依存: `if (!gPendingBuildAreas.has(area))` → `gPendingBuildAreas.set()`
- 条件付き依存: `if (!areaProperties)` → `gPendingBuildAreas.get(area).push()`
- 条件付き依存: `if (!areaProperties)` → `gPendingBuildAreas.get()`
- 条件付き依存: `if ( !placements && areaProperties.get("type") == CustomizableUI.TYPE_TOOLBAR )` → `this.restoreStateForArea()`
- 条件付き依存: `if ( !placements && areaProperties.get("type") == CustomizableUI.TYPE_TOOLBAR )` → `gPlacements.get()`
- 条件付き依存: `if ( !this.builtinToolbars.has(area) || placements.length != defaultPlacements.length || !placements.every((id, i) => id == defaultPlacements[i]) )` → `gDirtyAreaCache.add()`
- 条件付き依存: `if ( gDirtyAreaCache.has(area) || placements.some(id => gPalette.has(id)) )` → `this.buildArea()`
- 条件付き依存: `if (!( gDirtyAreaCache.has(area) || placements.some(id => gPalette.has(id)) ))` → `placements.filter()`
- 条件付き依存: `if (!( gDirtyAreaCache.has(area) || placements.some(id => gPalette.has(id)) ))` → `this.isSpecialWidget()`
- 条件付き依存: `if (specials.length)` → `this.updateSpecialsForBuiltinToolbar()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aToolbar.id`, `aToolbar.overflowable`, `defaultPlacements.length`, `placements.length`, `specials.length`, `this.tabstripAreasReady`

## updateSpecialsForBuiltinToolbar()
- 位置: L1522-1536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `kid.getAttribute()`, `this.getCustomizationTarget()`, `this.matchingSpecials()`
- 条件付き依存: `if ( this.matchingSpecials(aSpecialIDs[0], kid) && kid.getAttribute("skipintoolbarset") != "true" )` → `aSpecialIDs.shift()`
- 参照: `aSpecialIDs.length`, `kid.id`

## buildArea()
- 位置: L1554-1717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isSpecialWidget()`, `currentNode.getAttribute()`, `gAreas.get()`, `gAreas.get(aAreaId).get()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`, `this.ensureButtonContextMenu()`, `this.getCustomizationTarget()`, `this.getWidgetNode()`, `this.insertWidgetBefore()`, `this.isSpecialWidget()`, `this.matchingSpecials()`
- 条件付き依存: `if (this.isSpecialWidget(id) && areaIsPanel)` → `placementsToRemove.add()`
- 条件付き依存: `if (!node)` → `lazy.log.debug()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_API)` → `gPalette.get()`
- 条件付き依存: `if (!widget.removable && aAreaId != widget.defaultArea)` → `placementsToRemove.add()`
- 条件付き依存: `if (!(provider == CustomizableUI.PROVIDER_API))` → `this.isWidgetRemovable()`
- 条件付き依存: `if (!(provider == CustomizableUI.PROVIDER_API))` → `aAreaNode.overflowable?.isInOverflowList()`
- 条件付き依存: `if ( provider == CustomizableUI.PROVIDER_XUL && !this.isWidgetRemovable(node) && node.parentNode != container && !aAreaNode.overflowable?.isInOverflowList(node) )` → `placementsToRemove.add()`
- 条件付き依存: `if (gResetting)` → `this.notifyListeners()`
- 条件付き依存: `if (gUndoResetting)` → `this.notifyListeners()`
- 条件付き依存: `if (currentNode)` → `this.isSpecialWidget()`
- 条件付き依存: `if (currentNode)` → `node.getAttribute()`
- 条件付き依存: `if ( (node.id || this.isSpecialWidget(node)) && node.getAttribute("skipintoolbarset") != "true" )` → `this.isWidgetRemovable()`
- 条件付き依存: `if (node.id && (gResetting || gUndoResetting))` → `gPalette.get()`
- 条件付き依存: `if (this.isWidgetRemovable(node))` → `this.notifyDOMChange()`
- 条件付き依存: `if (this.isWidgetRemovable(node))` → `this.isSpecialWidget()`
- 条件付き依存: `if (palette && !this.isSpecialWidget(node.id))` → `palette.appendChild()`
- 条件付き依存: `if (palette && !this.isSpecialWidget(node.id))` → `this.removeLocationAttributes()`
- 条件付き依存: `if (!(palette && !this.isSpecialWidget(node.id)))` → `container.removeChild()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `node.setAttribute()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `lazy.log.debug()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `gPlacements.get(aAreaId).push()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `gPlacements.get()`
- 条件付き依存: `if (placementsToRemove.size)` → `gPlacements.get()`
- 条件付き依存: `if (placementsToRemove.size)` → `placementAry.indexOf()`
- 条件付き依存: `if (placementsToRemove.size)` → `placementAry.splice()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_XUL`, `CustomizableUI.TYPE_PANEL`, `aAreaNode.collapsed`, `aAreaNode.ownerDocument`, `container.firstElementChild`, `container.lastElementChild`, `currentNode.id`, `currentNode.nextElementSibling`, `currentNode.previousElementSibling`, `document.defaultView`, `node.id`, `node.parentNode`, `node.previousElementSibling`, `placementsToRemove.size`, `widget.currentArea`, `widget.defaultArea`, `widget.removable`, `widget.showInPrivateBrowsing`, `widget?.hideInNonPrivateBrowsing`, `window.gNavToolbox`, `window.gNavToolbox.palette`

## addPanelCloseListeners()
- 位置: L1723-1731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPanel.addEventListener()`, `gPanelsForWindow.get()`, `gPanelsForWindow.get(win).add()`, `gPanelsForWindow.has()`, `this._getPanelForNode()`
- 条件付き依存: `if (!gPanelsForWindow.has(win))` → `gPanelsForWindow.set()`
- 参照: `aPanel.documentGlobal`

## removePanelCloseListeners()
- 位置: L1737-1745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPanel.removeEventListener()`, `gPanelsForWindow.get()`
- 条件付き依存: `if (panels)` → `panels.delete()`
- 条件付き依存: `if (panels)` → `this._getPanelForNode()`
- 参照: `aPanel.documentGlobal`

## ensureButtonContextMenu()
- 位置: L1762-1790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `aNode.getAttribute()`
- 条件付き依存: `if (!( CustomizableUI.isWebExtensionWidget(aNode.id) && (aAreaNode?.id == CustomizableUI.AREA_ADDONS || aNode.getAttribute("overflowedItem") == "true") ))` → `CustomizableUI.getPlaceForItem()`
- 条件付き依存: `if (contextMenuForPlace && !currentContextMenu)` → `aNode.setAttribute()`
- 条件付き依存: `if ( currentContextMenu == kPanelItemContextMenu && contextMenuForPlace != kPanelItemContextMenu )` → `aNode.removeAttribute()`
- 参照: `CustomizableUI.AREA_ADDONS`, `aAreaNode?.id`, `aNode.id`

## getWidgetProvider()
- 位置: L1801-1819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPalette.has()`, `gSeenWidgets.has()`, `this.isSpecialWidget()`
- 参照: `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_SPECIAL`, `CustomizableUI.PROVIDER_XUL`

## getWidgetNode()
- 位置: L1842-1879
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPalette.get()`, `lazy.log.debug()`, `this.findXULWidgetInWindow()`, `this.isSpecialWidget()`
- 条件付き依存: `if (this.isSpecialWidget(aWidgetId))` → `document.getElementById()`
- 条件付き依存: `if (this.isSpecialWidget(aWidgetId))` → `this.createSpecialWidget()`
- 条件付き依存: `if (widget)` → `widget.instances.has()`
- 条件付き依存: `if (widget.instances.has(document))` → `lazy.log.debug()`
- 条件付き依存: `if (widget.instances.has(document))` → `widget.instances.get()`
- 条件付き依存: `if (widget)` → `this.buildWidgetNode()`
- 参照: `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_SPECIAL`, `CustomizableUI.PROVIDER_XUL`, `aWindow.document`

## registerPanelNode()
- 位置: L1886-1909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBuildAreas.get()`, `gBuildAreas.get(aAreaId).has()`, `gBuildAreas.has()`, `gPlacements.get()`, `this._getPanelForNode()`, `this.addPanelCloseListeners()`, `this.buildArea()`, `this.ensureButtonContextMenu()`, `this.notifyListeners()`, `this.registerBuildArea()`
- 条件付き依存: `if (child.localName == "toolbaritem")` → `this.ensureButtonContextMenu()`
- 参照: `aNode._customizationTarget`, `aNode.children`, `child.localName`

## onWidgetAdded()
- 位置: L1914-1920
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.insertNode()`
- 条件付き依存: `if (!gResetting)` → `this._clearPreviousUIState()`

## onWidgetRemoved()
- 位置: L1925-1990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `area.get()`, `container.contains()`, `gAreas.get()`, `gBuildAreas.get()`, `gPalette.get()`, `gPalette.has()`, `gSingleWrapperCache.get()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.ensureButtonContextMenu()`, `this.getCustomizationTarget()`, `this.isSpecialWidget()`, `this.notifyDOMChange()`, `this.removeLocationAttributes()`, `window.document.getElementById()`
- 条件付き依存: `if (widgetNode && isOverflowable)` → `areaNode.overflowable.getContainerFor()`
- 条件付き依存: `if (!widgetNode || !container.contains(widgetNode))` → `lazy.log.info()`
- 条件付き依存: `if (gPalette.has(aWidgetId) || this.isSpecialWidget(aWidgetId))` → `container.removeChild()`
- 条件付き依存: `if (!(gPalette.has(aWidgetId) || this.isSpecialWidget(aWidgetId)))` → `window.gNavToolbox.palette.appendChild()`
- 条件付き依存: `if (windowCache)` → `windowCache.delete()`
- 条件付き依存: `if (!gResetting)` → `this._clearPreviousUIState()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `areaNode.documentGlobal`, `gPalette.get(aWidgetId).showInPrivateBrowsing`, `gPalette.get(aWidgetId)?.hideInNonPrivateBrowsing`

## onWidgetMoved()
- 位置: L1995-2000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.insertNode()`
- 条件付き依存: `if (!gResetting)` → `this._clearPreviousUIState()`

## onCustomizeEnd()
- 位置: L2005-2007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearPreviousUIState()`

## registerBuildArea()
- 位置: L2018-2041
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customizableNode.classList.add()`, `gBuildAreas.get()`, `gBuildAreas.get(aAreaId).add()`, `gBuildAreas.has()`, `this.getCustomizeTargetForArea()`, `this.registerBuildWindow()`
- 条件付き依存: `if (window.gNavToolbox)` → `gBuildWindows.get(window).add()`
- 条件付き依存: `if (window.gNavToolbox)` → `gBuildWindows.get()`
- 条件付き依存: `if (!gBuildAreas.has(aAreaId))` → `gBuildAreas.set()`
- 参照: `aAreaNode.documentGlobal`, `window.closed`, `window.gNavToolbox`

## registerBuildWindow()
- 位置: L2052-2061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBuildWindows.has()`
- 条件付き依存: `if (!gBuildWindows.has(aWindow))` → `gBuildWindows.set()`
- 条件付き依存: `if (!gBuildWindows.has(aWindow))` → `aWindow.addEventListener()`
- 条件付き依存: `if (!gBuildWindows.has(aWindow))` → `this.notifyListeners()`

## unregisterBuildWindow()
- 位置: L2073-2114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.removeEventListener()`, `gAreas.get()`, `gBuildWindows.delete()`, `gPanelsForWindow.delete()`, `gSingleWrapperCache.delete()`, `this.notifyListeners()`, `widget.instances.delete()`
- 条件付き依存: `if (node.ownerDocument == document)` → `this.notifyListeners()`
- 条件付き依存: `if (node.ownerDocument == document)` → `this.getCustomizationTarget()`
- 条件付き依存: `if (node.ownerDocument == document)` → `areaProperties.get()`
- 条件付き依存: `if (areaProperties.get("overflowable"))` → `node.overflowable.uninit()`
- 条件付き依存: `if (node.ownerDocument == document)` → `areaNodes.delete()`
- 条件付き依存: `if (pendingNodes[i].ownerDocument == document)` → `pendingNodes.splice()`
- 参照: `CustomizableUI.REASON_WINDOW_CLOSED`, `aWindow.document`, `node.overflowable`, `node.ownerDocument`, `pendingNodes.length`, `pendingNodes[i].ownerDocument`, `widget.id`

## handleNewBrowserWindow()
- 位置: L2120-2184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getAreaType()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (isVerticalTabs)` → `elem.setAttribute()`
- 条件付き依存: `if (type == CustomizableUI.TYPE_TOOLBAR)` → `document.getElementById()`
- 条件付き依存: `if (type == CustomizableUI.TYPE_TOOLBAR)` → `this.registerToolbarNode()`
- 条件付き依存: `if (isVerticalTabs)` → `aWindow.setToolbarVisibility()`
- 条件付き依存: `if (isVerticalTabs)` → `document.getElementById()`
- 条件付き依存: `if (isVerticalTabs)` → `aWindow.TabBarVisibility.update()`
- 条件付き依存: `if (tabstripToolbar.collapsed !== wasCollapsed)` → `tabstripToolbar.dispatchEvent()`
- 条件付き依存: `if (isVerticalTabs)` → `elem.removeAttribute()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.areas`, `document.getElementById( "BrowserToolbarPalette" ).content`, `gBrowser.tabContainer`, `gNavToolbox.palette`, `tabstripToolbar.collapsed`
- XPCOM: `Services.prefs`

## setLocationAttributes()
- 位置: L2196-2214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.setAttribute()`, `gAreas.get()`, `props.get()`
- 条件付き依存: `if (anchor)` → `aNode.setAttribute()`
- 条件付き依存: `if (!(anchor))` → `aNode.removeAttribute()`

## removeLocationAttributes()
- 位置: L2223-2226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.removeAttribute()`

## insertNode()
- 位置: L2242-2263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBuildAreas.get()`, `gPlacements.get()`, `this.insertNodeInWindow()`
- 条件付き依存: `if (!placements)` → `lazy.log.error()`

## insertNodeInWindow()
- 位置: L2278-2316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPalette.get()`, `gPalette.has()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.findInsertionPoints()`, `this.getWidgetNode()`, `this.insertWidgetBefore()`
- 条件付き依存: `if (!widgetNode)` → `lazy.log.error()`
- 条件付き依存: `if (isNew)` → `this.ensureButtonContextMenu()`
- 参照: `aAreaNode.documentGlobal`, `aAreaNode.id`, `gPalette.get(aWidgetId).showInPrivateBrowsing`, `gPalette.get(aWidgetId)?.hideInNonPrivateBrowsing`

## findInsertionPoints()
- 位置: L2340-2378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aAreaNode.ownerDocument.getElementById()`, `gAreas.get()`, `gPlacements.get()`, `placements.indexOf()`, `props.get()`, `this.getCustomizationTarget()`
- 条件付き依存: `if ( props.get("type") == CustomizableUI.TYPE_TOOLBAR && props.get("overflowable") )` → `aAreaNode.overflowable.findOverflowedInsertionPoints()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aAreaNode.id`, `aNode.id`, `nextNode.parentNode`, `nextNode.parentNode.localName`, `nextNode.parentNode.parentNode`, `placements.length`

## insertWidgetBefore()
- 位置: L2394-2399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aContainer.insertBefore()`, `this.notifyDOMChange()`, `this.setLocationAttributes()`

## notifyDOMChange()
- 位置: L2419-2435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback()`, `this.notifyListeners()`

## handleEvent()
- 位置: L2443-2459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._originalEventInPanel()`, `this.maybeAutoHidePanel()`, `this.unregisterBuildWindow()`
- 参照: `aEvent.currentTarget`, `aEvent.sourceEvent`, `aEvent.type`

## _originalEventInPanel()
- 位置: L2468-2480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPanelsForWindow.get()`, `panels.has()`, `this._getPanelForNode()`
- 参照: `aEvent.sourceEvent`, `e.target`, `e.view`

## _getSpecialIdForNode()
- 位置: L2500-2511
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof aStringOrNode == "object" && aStringOrNode.localName)` → `aStringOrNode.localName.startsWith()`
- 条件付き依存: `if (aStringOrNode.localName.startsWith("toolbar"))` → `aStringOrNode.localName.substring()`
- 参照: `aStringOrNode.id`, `aStringOrNode.localName`

## isSpecialWidget()
- 位置: L2522-2534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aStringOrNode.startsWith()`, `this._getSpecialIdForNode()`
- 条件付き依存: `if (aStringOrNode === null)` → `lazy.log.debug()`

## matchingSpecials()
- 位置: L2548-2558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aId1.match()`, `aId2.match()`, `this._getSpecialIdForNode()`, `this.isSpecialWidget()`

## ensureSpecialWidgetId()
- 位置: L2573-2581
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aId.match()`

## createSpecialWidget()
- 位置: L2589-2595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDocument.createXULElement()`, `aId.match()`, `this.ensureSpecialWidgetId()`
- 参照: `node.className`, `node.id`

## findXULWidgetInWindow()
- 位置: L2610-2682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `gBuildWindows.get()`, `gBuildWindows.has()`
- 条件付き依存: `if (!aId)` → `lazy.log.error()`
- 条件付き依存: `if (node)` → `this.getCustomizationTarget()`
- 条件付き依存: `if (parent)` → `this.getCustomizationTarget()`
- 条件付き依存: `if (parent)` → `gBuildWindows.get(aWindow).has()`
- 条件付き依存: `if (parent)` → `gBuildWindows.get()`
- 条件付き依存: `if ( (this.getCustomizationTarget(parent) == nodeInArea.parentNode && gBuildWindows.get(aWindow).has(aWindow.gNavToolbox)) || aWindow.gNavToolbox.palette == node...)` → `node.hasAttribute()`
- 条件付き依存: `if (!node.hasAttribute("removable"))` → `node.setAttribute()`
- 条件付き依存: `if (!node.hasAttribute("removable"))` → `this.getCustomizationTarget()`
- 条件付き依存: `if (toolbox.palette)` → `toolbox.palette.getElementsByAttribute()`
- 条件付き依存: `if (element)` → `element.hasAttribute()`
- 条件付き依存: `if (!element.hasAttribute("removable"))` → `element.setAttribute()`
- 参照: `aWindow.document`, `aWindow.gNavToolbox`, `aWindow.gNavToolbox.palette`, `node.parentNode`, `node.parentNode.localName`, `nodeInArea.parentNode`, `parent.parentNode`, `toolbox.palette`

## buildWidgetNode()
- 位置: L2702-2891
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWidget.instances.set()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.log.debug()`
- 条件付き依存: `if (typeof aWidget == "string")` → `gPalette.get()`
- 条件付き依存: `if (aWidget.onBuild)` → `aWidget.onBuild()`
- 条件付き依存: `if (aWidget.type == "custom")` → `aDocument.defaultView.XULElement.isInstance()`
- 条件付き依存: `if ( !node || !aDocument.defaultView.XULElement.isInstance(node) || (aWidget.viewId && !node.viewButton) )` → `lazy.log.error()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `aWidget.onBeforeCreated()`
- 条件付き依存: `if (!button)` → `aDocument.createXULElement()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `button.classList.add()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `button.setAttribute()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `button.setAttribute()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `aDocument.createXULElement()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `dropmarker.setAttribute()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `dropmarker.classList.add()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `node.classList.add()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `node.append()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.setAttribute()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.toggleAttribute()`
- 条件付き依存: `if (aWidget.tabSpecific)` → `node.setAttribute()`
- 条件付き依存: `if (aWidget.locationSpecific)` → `node.setAttribute()`
- 条件付き依存: `if (aWidget.keepBroadcastAttributesWhenCustomizing)` → `node.setAttribute()`
- 条件付き依存: `if (aWidget.shortcutId)` → `aDocument.getElementById()`
- 条件付き依存: `if (keyEl)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (!(keyEl))` → `lazy.log.error()`
- 条件付き依存: `if (aWidget.l10nId)` → `aDocument.l10n.setAttributes()`
- 条件付き依存: `if (button != node)` → `aDocument.l10n.setAttributes()`
- 条件付き依存: `if (shortcut)` → `node.setAttribute()`
- 条件付き依存: `if (shortcut)` → `JSON.stringify()`
- 条件付き依存: `if (button != node)` → `button.setAttribute()`
- 条件付き依存: `if (button != node)` → `JSON.stringify()`
- 条件付き依存: `if (!(aWidget.l10nId))` → `node.setAttribute()`
- 条件付き依存: `if (!(aWidget.l10nId))` → `this.getLocalizedProperty()`
- 条件付き依存: `if (button != node)` → `node.getAttribute()`
- 条件付き依存: `if (tooltip)` → `node.setAttribute()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `this.handleWidgetCommand.bind()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.addEventListener()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `this.handleWidgetClick.bind()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.classList.add()`
- 条件付き依存: `if (viewbutton)` → `lazy.log.debug()`
- 条件付き依存: `if (aWidget.source == CustomizableUI.SOURCE_BUILTIN)` → `node.classList.add()`
- 条件付き依存: `if (aWidget.onCreated)` → `aWidget.onCreated()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `aDocument.defaultView`, `aDocument.documentURI`, `aWidget.disabled`, `aWidget.hideInNonPrivateBrowsing`, `aWidget.id`, `aWidget.keepBroadcastAttributesWhenCustomizing`, `aWidget.l10nId`, `aWidget.locationSpecific`, `aWidget.onBeforeCreated`, `aWidget.onBuild`, `aWidget.onCreated`, `aWidget.overflows`, `aWidget.removable`, `aWidget.shortcutId`, `aWidget.showInPrivateBrowsing`, `aWidget.source`, `aWidget.tabSpecific`, `aWidget.type`, `aWidget.viewId`, `node.viewButton`

## ensureSubviewListeners()
- 位置: L2897-2916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...gPalette.values()].find()`, `gPalette.values()`, `lazy.log.debug()`
- 条件付き依存: `if (typeof widget[handler] == "function")` → `viewNode.addEventListener()`
- 参照: `viewNode._addedEventListeners`, `viewNode.id`, `w.viewId`, `widget.id`

## getLocalizedProperty()
- 位置: L2926-2969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `kReqStringProps.includes()`, `lazy.gWidgetsBundle.GetStringFromName()`
- 条件付き依存: `if (typeof aWidget == "string")` → `gPalette.get()`
- 条件付き依存: `if (Array.isArray(aFormatArgs) && aFormatArgs.length)` → `lazy.gWidgetsBundle.formatStringFromName()`
- 条件付き依存: `if (!def && (name != "" || kReqStringProps.includes(aProp)))` → `lazy.log.error()`
- 参照: `aFormatArgs.length`, `aWidget.id`, `aWidget.localized`

## addShortcut()
- 位置: L2976-3005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aShortcutNode.getAttribute()`, `aTargetNode.hasAttribute()`, `aTargetNode.setAttribute()`, `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (shortcutId)` → `document.getElementById()`
- 条件付き依存: `if (!(shortcutId))` → `aShortcutNode.getAttribute()`
- 条件付き依存: `if (commandId)` → `lazy.ShortcutUtils.findShortcut()`
- 条件付き依存: `if (commandId)` → `document.getElementById()`
- 参照: `aShortcutNode.documentGlobal`

## doWidgetCommand()
- 位置: L3017-3032
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidget.onCommand)` → `aWidget.onCommand.call()`
- 条件付き依存: `if (aWidget.onCommand)` → `lazy.log.error()`
- 条件付き依存: `if (!(aWidget.onCommand))` → `Services.obs.notifyObservers()`
- 参照: `aWidget.id`, `aWidget.onCommand`
- XPCOM: `Services.obs`

## showWidgetView()
- 位置: L3047-3074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getAreaType()`, `aNode.hasAttribute()`, `ownerWindow.PanelUI.showSubView()`, `this.getPlacementOfWidget()`
- 条件付き依存: `if ( aWidget.disallowSubView && (areaType == CustomizableUI.TYPE_PANEL || aNode.hasAttribute("overflowedItem")) )` → `this.wrapWidget(aWidget.id).forWindow()`
- 条件付き依存: `if ( aWidget.disallowSubView && (areaType == CustomizableUI.TYPE_PANEL || aNode.hasAttribute("overflowedItem")) )` → `this.wrapWidget()`
- 条件付き依存: `if (wrapper?.anchor)` → `this.hidePanelForNode()`
- 条件付き依存: `if (areaType != CustomizableUI.TYPE_PANEL)` → `this.wrapWidget(aWidget.id).forWindow()`
- 条件付き依存: `if (areaType != CustomizableUI.TYPE_PANEL)` → `this.wrapWidget()`
- 条件付き依存: `if (areaType != CustomizableUI.TYPE_PANEL)` → `aNode.closest()`
- 条件付き依存: `if (!hasMultiView && wrapper?.anchor)` → `this.hidePanelForNode()`
- 参照: `CustomizableUI.TYPE_PANEL`, `aNode.documentGlobal`, `aNode.id`, `aWidget.disallowSubView`, `aWidget.id`, `aWidget.viewId`, `this.getPlacementOfWidget(aNode.id).area`, `wrapper.anchor`, `wrapper?.anchor`

## handleWidgetCommand()
- 位置: L3087-3122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (aWidget.onBeforeCommand)` → `aWidget.onBeforeCommand.call()`
- 条件付き依存: `if (aWidget.onBeforeCommand)` → `lazy.log.error()`
- 条件付き依存: `if (aWidget.type == "button" || action == "command")` → `this.doWidgetCommand()`
- 条件付き依存: `if (aWidget.type == "view" || action == "view")` → `this.showWidgetView()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `this.getPlacementOfWidget()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `CustomizableUI.getAreaType()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `button.contains()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `aNode.hasAttribute()`
- 条件付き依存: `if ( areaType == CustomizableUI.TYPE_TOOLBAR && button.contains(aEvent.target) && !aNode.hasAttribute("overflowedItem") )` → `this.doWidgetCommand()`
- 条件付き依存: `if (!( areaType == CustomizableUI.TYPE_TOOLBAR && button.contains(aEvent.target) && !aNode.hasAttribute("overflowedItem") ))` → `this.showWidgetView()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aEvent.target`, `aNode.firstElementChild`, `aNode.id`, `aWidget.onBeforeCommand`, `aWidget.type`, `this.getPlacementOfWidget(aNode.id).area`

## handleWidgetClick()
- 位置: L3136-3152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (aWidget.onClick)` → `aWidget.onClick.call()`
- 条件付き依存: `if (aWidget.onClick)` → `console.error()`
- 条件付き依存: `if (!(aWidget.onClick))` → `Services.obs.notifyObservers()`
- 参照: `aWidget.id`, `aWidget.onClick`
- XPCOM: `Services.obs`

## _getPanelForNode()
- 位置: L3162-3164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.closest()`

## _isOnInteractiveElement()
- 位置: L3183-3251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getNextTarget()`, `target.closest()`, `target.hasAttribute()`, `this._getPanelForNode()`
- 条件付き依存: `if (tagName == "toolbaritem" || tagName == "toolbarbutton")` → `target.getAttribute()`
- 参照: `aEvent.currentTarget`, `aEvent.originalTarget`, `target.DOCUMENT_FRAGMENT_NODE`, `target.DOCUMENT_NODE`, `target.containingShadowRoot`, `target.localName`, `target.nodeType`

## getNextTarget()
- 位置: L3191-3202
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `target.DOCUMENT_NODE`, `target.defaultView`, `target.defaultView.docShell.chromeEventHandler`, `target.nodeType`, `target.parentNode`, `target.parentNode?.host`

## hidePanelForNode()
- 位置: L3260-3265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getPanelForNode()`
- 条件付き依存: `if (panel)` → `lazy.PanelMultiView.hidePopup()`

## maybeAutoHidePanel()
- 位置: L3275-3327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShadowRoot.isInstance()`, `target.getAttribute()`, `target.hasAttribute()`, `this._isOnInteractiveElement()`, `this.hidePanelForNode()`
- 参照: `aEvent.DOM_VK_RETURN`, `aEvent.button`, `aEvent.keyCode`, `aEvent.originalTarget`, `aEvent.target`, `aEvent.type`, `target.host`, `target.isConnected`, `target.localName`, `target.parentNode`

## getUnusedWidgets()
- 位置: L3334-3366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.log.debug()`, `this.getPlacementOfWidget()`
- 条件付き依存: `if ( (isWindowPrivate && widget.showInPrivateBrowsing) || (!isWindowPrivate && !widget.hideInNonPrivateBrowsing) )` → `widgets.add()`
- 条件付き依存: `if (node.id && !this.getPlacementOfWidget(node.id))` → `widgets.add()`
- 参照: `aWindowPalette.children`, `aWindowPalette.documentGlobal`, `node.id`, `widget.currentArea`, `widget.hideInNonPrivateBrowsing`, `widget.showInPrivateBrowsing`

## getPlacementOfWidget()
- 位置: L3375-3391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.has()`, `placements.indexOf()`, `this.widgetExists()`

## widgetExists()
- 位置: L3404-3418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPalette.has()`, `gSeenWidgets.has()`, `this.isSpecialWidget()`

## addWidgetToArea()
- 位置: L3429-3509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.get()`, `gAreas.get(aArea).get()`, `gAreas.has()`, `gPalette.get()`, `gPlacements.has()`, `this.canWidgetMoveToArea()`, `this.getPlacementOfWidget()`, `this.isAreaLazy()`, `this.isSpecialWidget()`, `this.notifyListeners()`, `this.saveState()`
- 条件付き依存: `if (this.isAreaLazy(aArea))` → `gFuturePlacements.get(aArea).add()`
- 条件付き依存: `if (this.isAreaLazy(aArea))` → `gFuturePlacements.get()`
- 条件付き依存: `if (this.isSpecialWidget(aWidgetId))` → `this.ensureSpecialWidgetId()`
- 条件付き依存: `if (oldPlacement && oldPlacement.area == aArea)` → `this.moveWidgetWithinArea()`
- 条件付き依存: `if (oldPlacement)` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (!gPlacements.has(aArea))` → `gPlacements.set()`
- 条件付き依存: `if (!(!gPlacements.has(aArea)))` → `gPlacements.get()`
- 条件付き依存: `if (!(!gPlacements.has(aArea)))` → `placements.splice()`
- 条件付き依存: `if (!aInitialAdd)` → `gDirtyAreaCache.add()`
- 参照: `CustomizableUI.AREA_NO_AREA`, `CustomizableUI.TYPE_PANEL`, `oldPlacement.area`, `placements.length`, `widget.currentArea`, `widget.currentPosition`

## removeWidgetFromArea()
- 位置: L3515-3556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gDirtyAreaCache.add()`, `gPalette.get()`, `gPlacements.get()`, `placements.indexOf()`, `this.getPlacementOfWidget()`, `this.isWidgetRemovable()`, `this.notifyListeners()`, `this.saveState()`
- 条件付き依存: `if (position != -1)` → `placements.splice()`
- 条件付き依存: `if (oldPlacement.area == CustomizableUI.AREA_TABSTRIP)` → `this.deleteWidgetInSavedHorizontalTabStripState()`
- 条件付き依存: `if (!(oldPlacement.area == CustomizableUI.AREA_TABSTRIP))` → `this.getSavedHorizontalSnapshotState().includes()`
- 条件付き依存: `if (!(oldPlacement.area == CustomizableUI.AREA_TABSTRIP))` → `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if ( oldPlacement.area == CustomizableUI.AREA_NAVBAR && this.getSavedHorizontalSnapshotState().includes(aWidgetId) )` → `this.deleteWidgetInSavedHorizontalTabStripState()`
- 条件付き依存: `if ( oldPlacement.area == CustomizableUI.AREA_NAVBAR && this.getSavedHorizontalSnapshotState().includes(aWidgetId) )` → `this.deleteWidgetInSavedNavBarWhenVerticalTabsState()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `oldPlacement.area`, `widget.currentArea`, `widget.currentPosition`

## moveWidgetWithinArea()
- 位置: L3563-3608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gDirtyAreaCache.add()`, `gPalette.get()`, `gPlacements.get()`, `placements.splice()`, `this.getPlacementOfWidget()`, `this.notifyListeners()`, `this.saveState()`
- 参照: `oldPlacement.area`, `oldPlacement.position`, `placements.length`, `widget.currentArea`, `widget.currentPosition`

## getSavedHorizontalSnapshotState()
- 位置: L3618-3632
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (prefValue)` → `JSON.parse()`
- 条件付き依存: `if (prefValue)` → `lazy.log.warn()`
- 参照: `lazy.horizontalPlacementsPref`

## getSavedVerticalSnapshotState()
- 位置: L3642-3656
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (prefValue)` → `JSON.parse()`
- 条件付き依存: `if (prefValue)` → `lazy.log.warn()`
- 参照: `lazy.verticalPlacementsPref`

## loadSavedState()
- 位置: L3664-3695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.clearUserPref()`, `Services.prefs.getCharPref()`, `lazy.log.debug()`
- 条件付き依存: `if (!state)` → `lazy.log.debug()`
- 参照: `gSavedState.currentVersion`, `gSavedState.dirtyAreaCache`, `gSavedState.newElementCount`, `gSavedState.placements`, `gSavedState.seen`
- XPCOM: `Services.prefs`

## restoreStateForArea()
- 位置: L3705-3782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gFuturePlacements.has()`, `gPlacements.get()`, `gPlacements.get(aAreaId).join()`, `gPlacements.has()`, `lazy.log.debug()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`
- 条件付き依存: `if (placementsPreexisted)` → `lazy.log.debug()`
- 条件付き依存: `if (placementsPreexisted)` → `gPlacements.get(aAreaId).entries()`
- 条件付き依存: `if (placementsPreexisted)` → `gPlacements.get()`
- 条件付き依存: `if (placementsPreexisted)` → `this.moveWidgetWithinArea()`
- 条件付き依存: `if (!(placementsPreexisted))` → `gPlacements.set()`
- 条件付き依存: `if (!restored && gSavedState && aAreaId in gSavedState.placements)` → `lazy.log.debug()`
- 条件付き依存: `if (!restored && gSavedState && aAreaId in gSavedState.placements)` → `this.addWidgetToArea()`
- 条件付き依存: `if (!restored)` → `lazy.log.debug()`
- 条件付き依存: `if (!restored)` → `gAreas.get(aAreaId).get()`
- 条件付き依存: `if (!restored)` → `gAreas.get()`
- 条件付き依存: `if (!restored)` → `gAreas.get(aAreaId).has()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aAreaId).has("verticalTabsDefaultPlacements") )` → `lazy.log.debug()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aAreaId).has("verticalTabsDefaultPlacements") )` → `gAreas.get(aAreaId).get()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aAreaId).has("verticalTabsDefaultPlacements") )` → `gAreas.get()`
- 条件付き依存: `if (defaults)` → `this.addWidgetToArea()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `gPlacements.get()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `gFuturePlacements.get()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `areaPlacements.includes()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `this.addWidgetToArea()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `gFuturePlacements.delete()`
- 参照: `CustomizableUI.verticalTabsEnabled`, `gSavedState.placements`

## restoreSavedHorizontalTabStripState()
- 位置: L3799-3839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `gPlacements.get()`, `lazy.log.debug()`, `savedPlacements.entries()`, `savedPlacements.includes()`, `this.addWidgetToArea()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`, `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (!savedPlacements.includes("tabbrowser-tabs"))` → `gAreas.get(tabstripAreaId).get()`
- 条件付き依存: `if (!savedPlacements.includes("tabbrowser-tabs"))` → `gAreas.get()`
- 条件付き依存: `if (!savedPlacements.includes("tabbrowser-tabs"))` → `lazy.log.debug()`
- 条件付き依存: `if (gPlacements.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.length)` → `lazy.log.warn()`
- 条件付き依存: `if (gPlacements.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.length)` → `gPlacements.get()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `gPlacements.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.length`
- XPCOM: `Services.prefs`

## deleteWidgetInSavedHorizontalTabStripState()
- 位置: L3850-3857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `savedPlacements.indexOf()`, `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (position != -1)` → `savedPlacements.splice()`
- 条件付き依存: `if (position != -1)` → `this.saveHorizontalTabStripState()`

## deleteWidgetInSavedNavBarWhenVerticalTabsState()
- 位置: L3868-3875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `savedPlacements.indexOf()`, `this.getSavedVerticalSnapshotState()`
- 条件付き依存: `if (position != -1)` → `savedPlacements.splice()`
- 条件付き依存: `if (position != -1)` → `this.saveNavBarWhenVerticalTabsState()`

## saveHorizontalTabStripState()
- 位置: L3889-3901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setCharPref()`, `lazy.log.debug()`
- 条件付き依存: `if (!placements.length)` → `this.getAreaPlacementsForSaving()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `placements.length`, `this.serializerHelper`
- XPCOM: `Services.prefs`

## saveNavBarWhenVerticalTabsState()
- 位置: L3915-3925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setCharPref()`, `lazy.log.debug()`
- 条件付き依存: `if (!placements.length)` → `this.getAreaPlacementsForSaving()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `placements.length`, `this.serializerHelper`
- XPCOM: `Services.prefs`

## getAreaPlacementsForSaving()
- 位置: L3940-3961
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gFuturePlacements.get()`, `gPlacements.get()`, `lazy.log.debug()`, `this.isAreaLazy()`
- 条件付き依存: `if (this.isAreaLazy(aAreaId) && gFuturePlacements.get(aAreaId)?.size)` → `gFuturePlacements.get()`
- 条件付き依存: `if (!(this.isAreaLazy(aAreaId) && gFuturePlacements.get(aAreaId)?.size))` → `gPlacements.has()`
- 条件付き依存: `if (gPlacements.has(aAreaId))` → `gPlacements.get()`
- 参照: `gFuturePlacements.get(aAreaId)?.size`, `gSavedState.placements`

## saveState()
- 位置: L3966-3996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setCharPref()`, `gPlacements.keys()`, `lazy.log.debug()`, `placements.set()`, `this.getAreaPlacementsForSaving()`
- 条件付き依存: `if (gSavedState?.placements)` → `Object.keys()`
- 条件付き依存: `if (gSavedState?.placements)` → `allAreaIds.add()`
- 参照: `gSavedState.placements`, `gSavedState?.placements`, `this.serializerHelper`
- XPCOM: `Services.prefs`

## serializerHelper()
- 位置: L4008-4022
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aValue.constructor.name`

## beginBatchUpdate()
- 位置: L4027-4029
- 役割: (未記入)
- 触るとき: (未記入)

## endBatchUpdate()
- 位置: L4035-4047
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (gInBatchStack == 0)` → `this.saveState()`

## addListener()
- 位置: L4053-4055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gListeners.add()`

## removeListener()
- 位置: L4061-4067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gListeners.delete()`

## notifyListeners()
- 位置: L4081-4095
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`
- 条件付き依存: `if (typeof listener[aListenerName] == "function")` → `listener[aListenerName].apply()`
- 参照: `e.fileName`, `e.lineNumber`

## _dispatchToolboxEventToWindow()
- 位置: L4111-4118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.gNavToolbox.dispatchEvent()`
- 参照: `aWindow.CustomEvent`

## dispatchToolboxEvent()
- 位置: L4136-4144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dispatchToolboxEventToWindow()`
- 条件付き依存: `if (aWindow)` → `this._dispatchToolboxEventToWindow()`

## createWidget()
- 位置: L4155-4296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.has()`, `gGroupWrapperCache.delete()`, `gPalette.set()`, `gPlacements.get()`, `gPlacements.get(area).indexOf()`, `gSeenWidgets.add()`, `gSingleWrapperCache.get()`, `seenAreas.add()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`, `this.normalizeWidget()`, `this.notifyListeners()`
- 条件付き依存: `if (!widget)` → `lazy.log.error()`
- 条件付き依存: `if (cache)` → `cache.delete()`
- 条件付き依存: `if (widget.defaultArea)` → `gAreas.get()`
- 条件付き依存: `if (widget.defaultArea)` → `CustomizableUI.isBuiltinToolbar()`
- 条件付き依存: `if (addToDefaultPlacements)` → `area.has()`
- 条件付き依存: `if (area.has("defaultPlacements"))` → `area.get("defaultPlacements").push()`
- 条件付き依存: `if (area.has("defaultPlacements"))` → `area.get()`
- 条件付き依存: `if (!(area.has("defaultPlacements")))` → `area.set()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `Object.keys()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `seenAreas.has()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `gAreas.has()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `gSavedState.placements[area].indexOf()`
- 条件付き依存: `if (widget.currentArea)` → `this.notifyListeners()`
- 条件付き依存: `if (widgetMightNeedAutoAdding)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (widgetMightNeedAutoAdding)` → `gSeenWidgets.has()`
- 条件付き依存: `if (defaultArea)` → `this.isAreaLazy()`
- 条件付き依存: `if (this.isAreaLazy(defaultArea))` → `gFuturePlacements.get(defaultArea).add()`
- 条件付き依存: `if (this.isAreaLazy(defaultArea))` → `gFuturePlacements.get()`
- 条件付き依存: `if (!(this.isAreaLazy(defaultArea)))` → `this.addWidgetToArea()`
- 条件付き依存: `if (widgetMightNeedAutoAdding)` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if ( !widget.currentArea && CustomizableUI.isWebExtensionWidget(widget.id) )` → `this.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.SOURCE_EXTERNAL`, `CustomizableUI.verticalTabsEnabled`, `gSavedState.placements`, `widget.currentArea`, `widget.currentPosition`, `widget.defaultArea`, `widget.defaultAreaVerticalTabs`, `widget.id`, `widget.removable`
- XPCOM: `Services.prefs`

## createBuiltinWidget()
- 位置: L4304-4339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPalette.set()`, `lazy.log.debug()`, `this.normalizeWidget()`
- 条件付き依存: `if (!widget)` → `lazy.log.error()`
- 条件付き依存: `if (conditionalDestroyPromise)` → `conditionalDestroyPromise.then()`
- 条件付き依存: `if (shouldDestroy)` → `this.destroyWidget()`
- 条件付き依存: `if (shouldDestroy)` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (conditionalDestroyPromise)` → `console.error()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `aData.conditionalDestroyPromise`, `aData.id`, `widget.id`

## isAreaLazy()
- 位置: L4348-4353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.get()`, `gAreas.get(aAreaId).get()`, `gAreas.has()`, `gPlacements.has()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`

## normalizeWidget()
- 位置: L4368-4525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^[a-z0-9-_]{1,}$/i.test()`, `gAreas.has()`, `gPalette.has()`, `gSupportedWidgetTypes.has()`, `this.wrapWidgetEventHandler()`, `widget.implementation.__defineGetter__()`
- 条件付き依存: `if (typeof aData.id != "string" || !/^[a-z0-9-_]{1,}$/i.test(aData.id))` → `lazy.log.error()`
- 条件付き依存: `if (typeof aData[prop] != "string")` → `lazy.log.error()`
- 条件付き依存: `if (!widget.removable)` → `lazy.log.error()`
- 条件付き依存: `if (typeof aData.viewId != "string")` → `lazy.log.error()`
- 条件付き依存: `if ( widget.type == "view" || widget.type == "button-and-view" || aData.viewId )` → `this.wrapWidgetEventHandler()`
- 条件付き依存: `if (widget.type == "custom")` → `this.wrapWidgetEventHandler()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `CustomizableUI.SOURCE_EXTERNAL`, `aData._introducedByPref`, `aData.defaultArea`, `aData.defaultAreaVerticalTabs`, `aData.disabled`, `aData.id`, `aData.introducedInVersion`, `aData.onBeforeCommand`, `aData.onCommand`, `aData.type`, `aData.viewId`, `widget._introducedByPref`, `widget._introducedInVersion`, `widget.currentArea`, `widget.defaultArea`, `widget.defaultAreaVerticalTabs`, `widget.disabled`, `widget.id`, `widget.implementation.currentArea`, `widget.onBeforeCommand`, `widget.onCommand`, `widget.removable`, `widget.type`, `widget.viewId`

## wrapWidgetEventHandler()
- 位置: L4538-4558
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aWidget.implementation`

## aWidget[aEventName]()
- 位置: L4543-4557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWidget.implementation[aEventName].apply()`, `console.error()`
- 参照: `aWidget.implementation`

## destroyWidget()
- 位置: L4564-4645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gGroupWrapperCache.delete()`, `gPalette.delete()`, `gPalette.get()`, `gSingleWrapperCache.get()`, `this.notifyListeners()`, `window.document.getElementById()`, `window.gNavToolbox.palette.getElementsByAttribute()`
- 条件付き依存: `if (!widget)` → `gGroupWrapperCache.delete()`
- 条件付き依存: `if (!widget)` → `gSingleWrapperCache.get()`
- 条件付き依存: `if (windowCache)` → `windowCache.delete()`
- 条件付き依存: `if (widget.defaultArea)` → `gAreas.get()`
- 条件付き依存: `if (area)` → `area.get()`
- 条件付き依存: `if (area)` → `defaultPlacements.indexOf()`
- 条件付き依存: `if (widgetIndex != -1)` → `defaultPlacements.splice()`
- 条件付き依存: `if (widgetNode)` → `this.notifyListeners()`
- 条件付き依存: `if (widgetNode)` → `widgetNode.remove()`
- 条件付き依存: `if ( widget.type == "view" || widget.type == "button-and-view" || widget.viewId )` → `window.document.getElementById()`
- 条件付き依存: `if (typeof widget[handler] == "function")` → `viewNode.removeEventListener()`
- 条件付き依存: `if (widgetNode && widget.onDestroyed)` → `widget.onDestroyed()`
- 参照: `viewNode._addedEventListeners`, `widget.defaultArea`, `widget.onDestroyed`, `widget.type`, `widget.viewId`, `widgetNode.parentNode`, `window.document`

## getCustomizeTargetForArea()
- 位置: L4653-4666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBuildAreas.get()`
- 条件付き依存: `if (node.documentGlobal == aWindow)` → `this.getCustomizationTarget()`
- 参照: `node.documentGlobal`

## reset()
- 位置: L4671-4694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this._rebuildRegisteredAreas()`, `this._resetUIState()`
- 条件付き依存: `if (widget.source == CustomizableUI.SOURCE_EXTERNAL)` → `gSeenWidgets.add()`
- 条件付き依存: `if (gSeenWidgets.size || gNewElementCount)` → `this.saveState()`
- 参照: `CustomizableUI.SOURCE_EXTERNAL`, `gSeenWidgets.size`, `widget.source`
- XPCOM: `Services.prefs`

## _resetUIState()
- 位置: L4703-4780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `Services.prefs.clearUserPref()`, `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`, `gDefaultTheme.enable()`, `gPlacements.set()`, `lazy.log.debug()`, `oldAddonPlacements.includes()`
- 条件付き依存: `if (areaId != CustomizableUI.AREA_ADDONS)` → `this.restoreStateForArea()`
- 条件付き依存: `if ( CustomizableUI.isWebExtensionWidget(widgetId) && !oldAddonPlacements.includes(widgetId) )` → `this.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_ADDONS`, `gUIStateBeforeReset.autoHideDownloadsButton`, `gUIStateBeforeReset.autoTouchMode`, `gUIStateBeforeReset.autoTouchModeHadUserValue`, `gUIStateBeforeReset.currentTheme`, `gUIStateBeforeReset.drawInTitlebar`, `gUIStateBeforeReset.newElementCount`, `gUIStateBeforeReset.sidebarPositionStart`, `gUIStateBeforeReset.uiCustomizationState`, `gUIStateBeforeReset.uiDensity`, `gUIStateBeforeReset.uiDensityHadUserValue`
- XPCOM: `Services.prefs`

## _rebuildRegisteredAreas()
- 位置: L4786-4810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `area.get()`, `gAreas.get()`, `gPlacements.get()`, `this.buildArea()`
- 条件付き依存: `if (area.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `area.get()`
- 条件付き依存: `if (defaultCollapsed !== null)` → `win.setToolbarVisibility()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `areaNode.documentGlobal`

## undoReset()
- 位置: L4816-4875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setCharPref()`, `Services.prefs.setIntPref()`, `currentTheme.enable()`, `this._clearPreviousUIState()`, `this.loadSavedState()`
- 条件付き依存: `if (uiDensityHadUserValue)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!(uiDensityHadUserValue))` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (autoTouchModeHadUserValue)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(autoTouchModeHadUserValue))` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (gSavedState)` → `Object.keys()`
- 条件付き依存: `if (gSavedState)` → `gPlacements.set()`
- 条件付き依存: `if (gSavedState)` → `this._rebuildRegisteredAreas()`
- 参照: `gSavedState.placements`, `gUIStateBeforeReset.drawInTitlebar`, `gUIStateBeforeReset.newElementCount`, `gUIStateBeforeReset.uiCustomizationState`
- XPCOM: `Services.prefs`

## _clearPreviousUIState()
- 位置: L4881-4885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.getOwnPropertyNames()`, `Object.getOwnPropertyNames(gUIStateBeforeReset).forEach()`

## isWidgetRemovable()
- 位置: L4893-4950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWidgetProvider()`
- 条件付き依存: `if (!(typeof aWidget == "string"))` → `aWidget.getAttribute()`
- 条件付き依存: `if (!(typeof aWidget == "string"))` → `["toolbarspring", "toolbarspacer", "toolbarseparator"].includes()`
- 条件付き依存: `if (!(typeof aWidget == "string"))` → `aWidget.nodeName.substring()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_API)` → `gPalette.get()`
- 条件付き依存: `if (!widgetNode)` → `this.getWidgetNode()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_XUL)` → `widgetNode.getAttribute()`
- 参照: `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_XUL`, `aWidget.id`, `aWidget.nodeName`, `gBuildWindows.size`, `gPalette.get(widgetId).removable`

## canWidgetMoveToArea()
- 位置: L4958-4998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `gAreas.get()`, `gAreas.get(aArea).get()`, `gAreas.has()`, `this.getPlacementOfWidget()`, `this.isSpecialWidget()`, `this.isWidgetRemovable()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `gAreas.get(aArea).get()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `gAreas.get()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_NO_AREA`, `CustomizableUI.TYPE_PANEL`, `placement.area`

## ensureWidgetPlacedInWindow()
- 位置: L5006-5026
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...areaNodes].filter()`, `container[0].getElementsByAttribute()`, `gBuildAreas.get()`, `this.getPlacementOfWidget()`, `this.insertNodeInWindow()`
- 参照: `container.length`, `n.documentGlobal`, `placement.area`

## _getCurrentWidgetsInContainer()
- 位置: L5039-5075
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidgetIdsInArea()`, `addUnskippedChildren()`, `container.getAttribute()`, `currentWidgets.has()`, `orderedPlacements.filter()`, `this.getCustomizationTarget()`, `this.getWidgetProvider()`
- 条件付き依存: `if (container.getAttribute("overflowing") == "true")` → `container.getAttribute()`
- 条件付き依存: `if (container.getAttribute("overflowing") == "true")` → `addUnskippedChildren()`
- 条件付き依存: `if (container.getAttribute("overflowing") == "true")` → `container.ownerDocument.getElementById()`
- 参照: `CustomizableUI.PROVIDER_API`, `container.id`

## addUnskippedChildren()
- 位置: L5041-5051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `realNode.getAttribute()`
- 条件付き依存: `if (realNode.getAttribute("skipintoolbarset") != "true")` → `currentWidgets.add()`
- 参照: `node.firstElementChild`, `node.localName`, `parent.children`, `realNode.id`

## inDefaultState()
- 位置: L5082-5213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `currentPlacements.join()`, `defaultPlacements.join()`, `gBuildAreas.get()`, `gPlacements.get()`, `lazy.log.debug()`, `props .get()`, `props .get("defaultPlacements") .filter()`, `this.matchingSpecials()`, `this.widgetExists()`
- 条件付き依存: `if (buildAreaNodes && buildAreaNodes.size)` → `props.get()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `this._getCurrentWidgetsInContainer(container).filter()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `this._getCurrentWidgetsInContainer()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `currentPlacements.filter()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `container.getElementsByAttribute()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `removableOrDefault()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `props.get()`
- 条件付き依存: `if (areaId == CustomizableUI.AREA_BOOKMARKS)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (areaId == CustomizableUI.AREA_BOOKMARKS)` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (!(areaId == CustomizableUI.AREA_BOOKMARKS))` → `container.getAttribute()`
- 条件付き依存: `if (!(areaId == CustomizableUI.AREA_BOOKMARKS))` → `container.hasAttribute()`
- 条件付き依存: `if (defaultCollapsed !== null && nondefaultState)` → `lazy.log.debug()`
- 条件付き依存: `if ( currentPlacements[i] != defaultPlacements[i] && !this.matchingSpecials(currentPlacements[i], defaultPlacements[i]) )` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefUIDensity))` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefAutoTouchMode))` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefDrawInTitlebar))` → `lazy.log.debug()`
- 条件付き依存: `if (gDefaultTheme && gDefaultTheme.id != gSelectedTheme.id)` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefSidebarPositionStartEnabled))` → `lazy.log.debug()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.verticalTabsEnabled`, `buildAreaNodes.size`, `currentPlacements.length`, `defaultPlacements.length`, `gDefaultTheme.id`, `gSelectedTheme.id`
- XPCOM: `Services.prefs`

## removableOrDefault()
- 位置: L5100-5105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defaultPlacements.includes()`, `this.isWidgetRemovable()`
- 参照: `itemNodeOrItem.id`

## getCollapsedToolbarIds()
- 位置: L5220-5236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolbar.getAttribute()`, `toolbar.hasAttribute()`, `window.document.getElementById()`
- 条件付き依存: `if (toolbar.hasAttribute(hidingAttribute))` → `collapsedToolbars.add()`
- 参照: `CustomizableUIInternal.builtinToolbars`

## setToolbarVisibility()
- 位置: L5243-5253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.document.getElementById()`
- 条件付き依存: `if (toolbar)` → `window.setToolbarVisibility()`
- 参照: `CustomizableUI.windows`

## widgetIsLikelyVisible()
- 位置: L5261-5286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `this.getCollapsedToolbarIds()`, `this.getCollapsedToolbarIds(window).has()`, `this.getPlacementOfWidget()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.AREA_MENUBAR`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `placement.area`
- XPCOM: `Services.prefs`

## observe()
- 位置: L5296-5305
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic == "browser-set-toolbar-visibility")` → `JSON.parse()`
- 条件付き依存: `if (aTopic == "browser-set-toolbar-visibility")` → `CustomizableUI.setToolbarVisibility()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `this.reconcileSidebarPrefs()`

## initializeForTabsOrientation()
- 位置: L5313-5428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `gAreas.get()`, `gAreas.get(CustomizableUI.AREA_TABSTRIP).get()`, `gFuturePlacements.has()`, `lazy.log.debug()`, `this.addWidgetToArea()`, `this.isSpecialWidget()`, `this.removeWidgetFromArea()`, `widgetId.includes()`, `widgetsMoved.push()`
- 条件付き依存: `if (!toVertical)` → `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (!toVertical)` → `lazy.log.debug()`
- 条件付き依存: `if (savedPlacements.length)` → `this.restoreSavedHorizontalTabStripState()`
- 条件付き依存: `if (!savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length)` → `gAreas .get(CustomizableUI.AREA_VERTICAL_TABSTRIP) .get()`
- 条件付き依存: `if (!savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length)` → `gAreas .get()`
- 条件付き依存: `if (!savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length)` → `lazy.log.debug()`
- 条件付き依存: `if (gFuturePlacements.has(CustomizableUI.AREA_TABSTRIP))` → `gFuturePlacements.get()`
- 条件付き依存: `if (gFuturePlacements.has(CustomizableUI.AREA_TABSTRIP))` → `tabstripPlacements.includes()`
- 条件付き依存: `if (!tabstripPlacements.includes(id))` → `tabstripPlacements.push()`
- 条件付き依存: `if (gFuturePlacements.has(CustomizableUI.AREA_TABSTRIP))` → `gFuturePlacements.delete()`
- 条件付き依存: `if (widgetId == "tabbrowser-tabs")` → `lazy.log.debug()`
- 条件付き依存: `if (widgetId == "tabbrowser-tabs")` → `this.addWidgetToArea()`
- 条件付き依存: `if (this.isSpecialWidget(widgetId) && widgetId.includes("spring"))` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(widgetId))` → `lazy.log.debug()`
- 条件付き依存: `if (!lazy.horizontalPlacementsPref)` → `lazy.log.debug()`
- 条件付き依存: `if (!lazy.horizontalPlacementsPref)` → `CustomizableUIInternal.saveHorizontalTabStripState()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `gSavedState?.placements`, `lazy.horizontalPlacementsPref`, `savedPlacements.length`, `savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length`, `tabstripPlacements.length`, `widgetsMoved.length`

## reconcileSidebarPrefs()
- 位置: L5440-5497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `defaults.indexOf()`, `gAreas.get()`, `gAreas.set()`, `gPlacements.get()`, `lazy.log.debug()`, `navbarPlacements.indexOf()`, `props.get()`, `props.set()`
- 条件付き依存: `if (verticalTabsEnabled && !sidebarRevampEnabled)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (sidebarRevampEnabled && sidebarButtonIndex < 0)` → `defaults.unshift()`
- 条件付き依存: `if (!sidebarRevampEnabled && sidebarButtonIndex > -1)` → `defaults.splice()`
- 条件付き依存: `if (!sidebarRevampEnabled && verticalTabsEnabled)` → `lazy.log.debug()`
- 条件付き依存: `if (!sidebarRevampEnabled && verticalTabsEnabled)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!positionStartEnabled && index === 0)` → `this.moveWidgetWithinArea()`
- 条件付き依存: `if (positionStartEnabled && index === navbarPlacements.length - 1)` → `this.moveWidgetWithinArea()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `navbarPlacements.length`
- XPCOM: `Services.prefs`

## tabstripAreasReady()
- 位置: L5503-5508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBuildAreas.get()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `gBuildAreas.get(CustomizableUI.AREA_TABSTRIP)?.size`, `gBuildAreas.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.size`

## updateTabStripOrientation()
- 位置: L5514-5636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `changeWidgetRemovability()`, `lazy.log.debug()`, `this.setToolbarVisibility()`, `win.TabBarVisibility.update()`
- 条件付き依存: `if (!this.tabstripAreasReady)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical === gCurrentVerticalTabs)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical && gCurrentVerticalTabs !== null)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical && gCurrentVerticalTabs !== null)` → `CustomizableUIInternal.saveHorizontalTabStripState()`
- 条件付き依存: `if (toVertical)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if ( !Services.prefs.getCharPref(kPrefCustomizationHorizontalTabsBackup, "") )` → `Services.prefs.setCharPref()`
- 条件付き依存: `if ( !Services.prefs.getCharPref(kPrefCustomizationHorizontalTabsBackup, "") )` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.beginBatchUpdate()`
- 条件付き依存: `if (toVertical)` → `this.getSavedVerticalSnapshotState()`
- 条件付き依存: `if (toVertical)` → `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (toVertical)` → `gPlacements.get(CustomizableUI.AREA_NAVBAR).at()`
- 条件付き依存: `if (toVertical)` → `gPlacements.get()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (id == "tabbrowser-tabs")` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (toVertical)` → `this.isSpecialWidget()`
- 条件付き依存: `if (toVertical)` → `id.includes()`
- 条件付き依存: `if (this.isSpecialWidget(id) && id.includes("spring"))` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (toVertical)` → `tabstripPlacements.includes()`
- 条件付き依存: `if (toVertical)` → `customVerticalNavbarPlacements.includes()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.isWidgetRemovable()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (toVertical)` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (toVertical)` → `customVerticalNavbarPlacements.forEach()`
- 条件付き依存: `if (tabstripPlacements.includes(id))` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (isSidebarLast)` → `this.addWidgetToArea()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.endBatchUpdate()`
- 条件付き依存: `if (!(toVertical))` → `this.saveNavBarWhenVerticalTabsState()`
- 条件付き依存: `if (!(toVertical))` → `this.restoreSavedHorizontalTabStripState()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `this.tabstripAreasReady`
- XPCOM: `Services.obs` / `Services.prefs`

## changeWidgetRemovability()
- 位置: L5537-5544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`
- 条件付き依存: `if (node)` → `node.setAttribute()`
- 条件付き依存: `if (node)` → `removable.toString()`
- 参照: `widget.instances`

## [Symbol.iterator]()
- 位置: L5734-5738
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Symbol.iterator`

## verticalTabsEnabled()
- 位置: L5741-5743
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.verticalTabsPref`

## addListener()
- 位置: L6013-6015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.addListener()`

## removeListener()
- 位置: L6023-6025
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.removeListener()`

## registerArea()
- 位置: L6052-6054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.registerArea()`

## registerToolbarNode()
- 位置: L6069-6071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.registerToolbarNode()`

## registerPanelNode()
- 位置: L6082-6084
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.registerPanelNode()`

## unregisterArea()
- 位置: L6108-6110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.unregisterArea()`

## addWidgetToArea()
- 位置: L6133-6135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.addWidgetToArea()`

## removeWidgetFromArea()
- 位置: L6146-6148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.removeWidgetFromArea()`

## moveWidgetWithinArea()
- 位置: L6165-6167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.moveWidgetWithinArea()`

## ensureWidgetPlacedInWindow()
- 位置: L6186-6191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.ensureWidgetPlacedInWindow()`

## beginBatchUpdate()
- 位置: L6204-6206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.beginBatchUpdate()`

## endBatchUpdate()
- 位置: L6220-6222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.endBatchUpdate()`

## createWidget()
- 位置: L6424-6428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.createWidget()`, `CustomizableUIInternal.wrapWidget()`

## destroyWidget()
- 位置: L6441-6443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.destroyWidget()`

## getWidget()
- 位置: L6508-6510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.wrapWidget()`

## getUnusedWidgets()
- 位置: L6524-6529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getUnusedWidgets()`, `CustomizableUIInternal.getUnusedWidgets(aWindowPalette).map()`
- 参照: `CustomizableUIInternal.wrapWidget`

## getWidgetIdsInArea()
- 位置: L6542-6552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.has()`, `gPlacements.get()`, `gPlacements.has()`

## getDefaultPlacementsForArea()
- 位置: L6563-6565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.get()`, `gAreas.get(aArea).get()`

## getWidgetsInArea()
- 位置: L6582-6587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getWidgetIdsInArea()`, `this.getWidgetIdsInArea(aArea).map()`
- 参照: `CustomizableUIInternal.wrapWidget`

## ensureSubviewListeners()
- 位置: L6597-6599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.ensureSubviewListeners()`

## areas()
- 位置: L6605-6607
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAreas.keys()`

## getAreaType()
- 位置: L6620-6623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `area.get()`, `gAreas.get()`

## isToolbarDefaultCollapsed()
- 位置: L6634-6637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `area.get()`, `gAreas.get()`

## getCustomizeTargetForArea()
- 位置: L6665-6667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getCustomizeTargetForArea()`

## reset()
- 位置: L6675-6677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.reset()`

## undoReset()
- 位置: L6685-6687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.undoReset()`

## removeExtraToolbar()
- 位置: L6698-6700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.removeExtraToolbar()`

## canUndoReset()
- 位置: L6708-6717
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gUIStateBeforeReset.autoTouchMode`, `gUIStateBeforeReset.currentTheme`, `gUIStateBeforeReset.drawInTitlebar`, `gUIStateBeforeReset.sidebarPositionStart`, `gUIStateBeforeReset.uiCustomizationState`, `gUIStateBeforeReset.uiDensity`

## getPlacementOfWidget()
- 位置: L6746-6752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getPlacementOfWidget()`

## isWidgetRemovable()
- 位置: L6772-6774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.isWidgetRemovable()`

## canWidgetMoveToArea()
- 位置: L6790-6792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.canWidgetMoveToArea()`

## inDefaultState()
- 位置: L6802-6804
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `CustomizableUIInternal.inDefaultState`

## setToolbarVisibility()
- 位置: L6814-6816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.setToolbarVisibility()`

## getCollapsedToolbarIds()
- 位置: L6827-6829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getCollapsedToolbarIds()`

## widgetIsLikelyVisible()
- 位置: L6848-6850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.widgetIsLikelyVisible()`

## getLocalizedProperty()
- 位置: L6878-6885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getLocalizedProperty()`

## addShortcut()
- 位置: L6896-6898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.addShortcut()`

## hidePanelForNode()
- 位置: L6905-6907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.hidePanelForNode()`

## isSpecialWidget()
- 位置: L6914-6916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.isSpecialWidget()`

## isWebExtensionWidget()
- 位置: L6929-6935
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `aWidgetId.endsWith()`
- 参照: `widget?.webExtension`

## addPanelCloseListeners()
- 位置: L6944-6946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.addPanelCloseListeners()`

## removePanelCloseListeners()
- 位置: L6955-6957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.removePanelCloseListeners()`

## onWidgetDrag()
- 位置: L6967-6969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.notifyListeners()`

## notifyStartCustomizing()
- 位置: L6977-6979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.notifyListeners()`

## notifyEndCustomizing()
- 位置: L6987-6989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.notifyListeners()`

## dispatchToolboxEvent()
- 位置: L7003-7005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.dispatchToolboxEvent()`

## isAreaOverflowable()
- 位置: L7015-7020
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `area.get()`, `gAreas.get()`
- 参照: `this.TYPE_TOOLBAR`

## getPlaceForItem()
- 位置: L7033-7048
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `node.id`, `node.localName`, `node.parentNode`

## isBuiltinToolbar()
- 位置: L7056-7058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.builtinToolbars.has()`

## createSpecialWidget()
- 位置: L7070-7072
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.createSpecialWidget()`

## fillSubviewFromMenuItems()
- 位置: L7082-7183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aSubview.appendChild()`, `doc.createDocumentFragment()`, `fragment.appendChild()`, `menuChild.getAttribute()`
- 条件付き依存: `if (menuChild.localName == "menuseparator")` → `doc.createXULElement()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `doc.createXULElement()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `CustomizableUI.addShortcut()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `item.hasAttribute()`
- 条件付き依存: `if (!item.hasAttribute("onclick"))` → `subviewItem.addEventListener()`
- 条件付き依存: `if (!item.hasAttribute("onclick"))` → `lazy.BrowserUsageTelemetry.ignoreEvent()`
- 条件付き依存: `if (!item.hasAttribute("onclick"))` → `item.dispatchEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `subviewItem.addEventListener()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `doc.createEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `newEvent.initCommandEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `lazy.BrowserUsageTelemetry.ignoreEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `item.dispatchEvent()`
- 条件付き依存: `if (attrVal !== null)` → `subviewItem.setAttribute()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `subviewItem.classList.add()`
- 条件付き依存: `if (l10nId)` → `doc.l10n.setAttributes()`
- 参照: `aSubview.documentGlobal.document`, `doc.documentGlobal.PointerEvent`, `event.altKey`, `event.bubbles`, `event.cancelable`, `event.ctrlKey`, `event.detail`, `event.metaKey`, `event.shiftKey`, `event.sourceEvent`, `event.type`, `event.view`, `fragment.lastElementChild`, `fragment.lastElementChild.localName`, `menuChild.hidden`, `menuChild.localName`

## clearSubview()
- 位置: L7191-7202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aSubview.firstChild.remove()`, `parent.appendChild()`, `parent.removeChild()`
- 参照: `aSubview.firstChild`, `aSubview.parentNode`

## handleNewBrowserWindow()
- 位置: L7210-7212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.handleNewBrowserWindow()`

## getCustomizationTarget()
- 位置: L7228-7230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getCustomizationTarget()`

## getTestOnlyInternalProp()
- 位置: L7242-7265
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cu.isInAutomation`

## setTestOnlyInternalProp()
- 位置: L7279-7294
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Cu.isInAutomation`

## WidgetGroupWrapper()
- 位置: L7311-7391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `areaProps.get()`, `gAreas.get()`, `gBuildAreas.get()`, `this.__defineGetter__()`, `this.__defineSetter__()`, `this.forWindow()`
- 参照: `CustomizableUI.PROVIDER_API`, `aWidget.disabled`, `aWidget.id`, `aWidget.instances`, `instance.disabled`, `node.documentGlobal`, `placement.area`, `this.forWindow`, `this.isGroup`

## WidgetGroupWrapper_forWindow()
- 位置: L7342-7365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWidget.instances.get()`, `gSingleWrapperCache.has()`, `wrapperMap.has()`, `wrapperMap.set()`
- 条件付き依存: `if (!gSingleWrapperCache.has(aWindow))` → `gSingleWrapperCache.set()`
- 条件付き依存: `if (!(!gSingleWrapperCache.has(aWindow)))` → `gSingleWrapperCache.get()`
- 条件付き依存: `if (wrapperMap.has(aWidget.id))` → `wrapperMap.get()`
- 条件付き依存: `if (!instance)` → `CustomizableUIInternal.buildWidgetNode()`
- 参照: `aWidget.id`, `aWindow.document`

## WidgetSingleWrapper()
- 位置: L7397-7453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `aNode.getAttribute()`, `this.__defineGetter__()`, `this.__defineSetter__()`
- 条件付き依存: `if (placement)` → `gAreas.get(placement.area).get()`
- 条件付き依存: `if (placement)` → `gAreas.get()`
- 条件付き依存: `if (!anchorId)` → `aNode.getAttribute()`
- 条件付き依存: `if (anchorId)` → `aNode.ownerDocument.getElementById()`
- 参照: `CustomizableUI.PROVIDER_API`, `aNode.disabled`, `aNode.lastElementChild`, `aWidget.id`, `aWidget.type`, `placement.area`, `this.isGroup`, `this.node`, `this.provider`

## XULWidgetGroupWrapper()
- 位置: L7463-7517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `areaProps.get()`, `gAreas.get()`, `this.__defineGetter__()`, `this.forWindow()`
- 参照: `CustomizableUI.PROVIDER_XUL`, `placement.area`, `this.forWindow`, `this.id`, `this.isGroup`, `this.provider`, `this.type`, `this.webExtension`

## XULWidgetGroupWrapper_forWindow()
- 位置: L7471-7500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.getElementById()`, `gSingleWrapperCache.has()`, `wrapperMap.has()`, `wrapperMap.set()`
- 条件付き依存: `if (!gSingleWrapperCache.has(aWindow))` → `gSingleWrapperCache.set()`
- 条件付き依存: `if (!(!gSingleWrapperCache.has(aWindow)))` → `gSingleWrapperCache.get()`
- 条件付き依存: `if (wrapperMap.has(aWidgetId))` → `wrapperMap.get()`
- 条件付き依存: `if (!instance)` → `aWindow.gNavToolbox.palette.getElementsByAttribute()`
- 参照: `aWindow.document`

## XULWidgetSingleWrapper()
- 位置: L7523-7595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `node.getAttribute()`, `node.ownerDocument.getElementById()`, `this.__defineGetter__()`, `weakDoc.get()`
- 条件付き依存: `if (doc)` → `CustomizableUIInternal.findXULWidgetInWindow()`
- 条件付き依存: `if (placement)` → `gAreas.get(placement.area).get()`
- 条件付き依存: `if (placement)` → `gAreas.get()`
- 条件付き依存: `if (!anchorId && node)` → `node.getAttribute()`
- 参照: `CustomizableUI.PROVIDER_XUL`, `aNode.documentGlobal.gNavToolbox`, `aNode.isConnected`, `aNode.parentNode`, `doc.defaultView`, `placement.area`, `this.id`, `this.isGroup`, `this.node`, `this.provider`, `this.type`, `toolbox.palette`

## OverflowableToolbar.constructor()
- 位置: L7764-7787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `doc.getElementById()`, `this.#toolbar.getAttribute()`, `this.#toolbar.setAttribute()`
- 条件付き依存: `if (window.gBrowserInit.delayedStartupFinished)` → `this.init()`
- 条件付き依存: `if (!(window.gBrowserInit.delayedStartupFinished))` → `Services.obs.addObserver()`
- 参照: `this.#defaultList`, `this.#defaultList._customizationTarget`, `this.#target`, `this.#target.parentNode`, `this.#toolbar`, `this.#toolbar.documentGlobal`, `this.#toolbar.ownerDocument`, `window.gBrowserInit.delayedStartupFinished`
- XPCOM: `Services.obs`

## OverflowableToolbar.init()
- 位置: L7794-7820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `CustomizableUIInternal.addPanelCloseListeners()`, `doc.getElementById()`, `this.#checkOverflow()`, `this.#defaultListButton.addEventListener()`, `this.#defaultListPanel.addEventListener()`, `this.#toolbar.getAttribute()`, `window.addEventListener()`, `window.gNavToolbox.addEventListener()`
- 参照: `doc.defaultView`, `this.#defaultListButton`, `this.#defaultListPanel`, `this.#initialized`, `this.#toolbar.ownerDocument`

## OverflowableToolbar.uninit()
- 位置: L7826-7850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `CustomizableUIInternal.removePanelCloseListeners()`, `this.#defaultListButton.removeEventListener()`, `this.#defaultListPanel.removeEventListener()`, `this.#disable()`, `this.#toolbar.removeAttribute()`, `window.gNavToolbox.removeEventListener()`, `window.removeEventListener()`
- 条件付き依存: `if (!this.#initialized)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (!this.#initialized)` → `Services.prefs.removeObserver()`
- 参照: `this.#defaultListPanel`, `this.#initialized`, `this.#toolbar.documentGlobal`
- XPCOM: `Services.obs` / `Services.prefs`

## OverflowableToolbar.show()
- 位置: L7859-7926
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `contextMenu.addEventListener()`, `doc.getElementById()`, `mainView.getAttribute()`, `multiview.getAttribute()`, `openPanel()`, `this.#defaultListPanel.addEventListener()`, `this.#defaultListPanel.querySelector()`
- 条件付き依存: `if (this.#defaultListPanel.state == "open")` → `Promise.resolve()`
- 参照: `this.#defaultListButton.icon`, `this.#defaultListPanel.hidden`, `this.#defaultListPanel.ownerDocument`, `this.#defaultListPanel.state`
- XPCOM: `Services.tm`

## openPanel()
- 位置: L7891-7922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.defaultView.updateEditUIVisibility()`, `lazy.PanelMultiView.openPopup()`, `this.#defaultListPanel.addEventListener()`
- 条件付き依存: `if (!popupshown)` → `openPanel()`
- 参照: `this.#defaultListButton`, `this.#defaultListButton.open`, `this.#defaultListPanel`

## OverflowableToolbar.isHandlingOverflow()
- 位置: L7933-7935
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#checkOverflowHandle`

## OverflowableToolbar.findOverflowedInsertionPoints()
- 位置: L7949-8014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `aNode.getAttribute()`, `gPlacements.get()`, `placements.indexOf()`
- 条件付き依存: `if (loopIndex > nodeIndex)` → `this.#toolbar.ownerDocument.getElementById()`
- 条件付き依存: `if (loopIndex > nodeIndex)` → `this.#overflowedInfo.has()`
- 条件付き依存: `if (!(loopIndex > nodeIndex))` → `this.#overflowedInfo.has()`
- 参照: `aNode.id`, `nextNode.parentNode`, `nextNode.parentNode.localName`, `nextNode.parentNode.parentNode`, `placements.length`, `this.#defaultList`, `this.#overflowedInfo.size`, `this.#target`, `this.#toolbar.id`, `this.#webExtList`

## OverflowableToolbar.getContainerFor()
- 位置: L8028-8035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.getAttribute()`
- 条件付き依存: `if (aNode.getAttribute("overflowedItem") == "true")` → `CustomizableUI.isWebExtensionWidget()`
- 参照: `aNode.id`, `this.#defaultList`, `this.#target`, `this.#webExtList`

## OverflowableToolbar.#onOverflow()
- 位置: async L8044-8115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.getAttribute()`, `this.#getOverflowInfo()`, `this.#toolbar.getAttribute()`, `win.UpdateUrlbarSearchSplitterState()`
- 条件付き依存: `if (win.closed || this.#checkOverflowHandle != checkOverflowHandle)` → `lazy.log.debug()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `this.#overflowedInfo.set()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `win.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!childWidth)` → `this.#hiddenOverflowedNodes.add()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `child.setAttribute()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `CustomizableUIInternal.ensureButtonContextMenu()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `CustomizableUIInternal.notifyListeners()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (webExtList && CustomizableUI.isWebExtensionWidget(child.id))` → `child.setAttribute()`
- 条件付き依存: `if (webExtList && CustomizableUI.isWebExtensionWidget(child.id))` → `webExtList.insertBefore()`
- 条件付き依存: `if (!(webExtList && CustomizableUI.isWebExtensionWidget(child.id)))` → `child.setAttribute()`
- 条件付き依存: `if (!(webExtList && CustomizableUI.isWebExtensionWidget(child.id)))` → `this.#defaultList.insertBefore()`
- 条件付き依存: `if (!(webExtList && CustomizableUI.isWebExtensionWidget(child.id)))` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if (!CustomizableUI.isSpecialWidget(child.id) && childWidth)` → `this.#toolbar.setAttribute()`
- 参照: `child.id`, `child.previousElementSibling`, `this.#checkOverflowHandle`, `this.#defaultList.firstElementChild`, `this.#defaultListButton.id`, `this.#enabled`, `this.#target`, `this.#target.documentGlobal`, `this.#target.lastElementChild`, `this.#toolbar`, `this.#webExtList`, `webExtList.firstElementChild`, `win.closed`

## OverflowableToolbar.#getOverflowInfo()
- 位置: async L8135-8196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.floor()`, `Math.max()`, `getInlineSize()`, `lazy.log.debug()`, `parseFloat()`, `sumChildrenInlineSize()`, `win.getComputedStyle()`, `win.promiseDocumentFlushed()`
- 参照: `style.paddingLeft`, `style.paddingRight`, `this.#target`, `this.#target.documentGlobal`, `this.#toolbar`

## getInlineSize()
- 位置: L8136-8138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElement.getBoundingClientRect()`
- 参照: `aElement.getBoundingClientRect().width`

## sumChildrenInlineSize()
- 位置: L8140-8157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`, `win.XULPopupElement.isInstance()`, `win.getComputedStyle()`
- 条件付き依存: `if (child != aExceptChild)` → `getInlineSize()`
- 参照: `aParent.children`, `style.display`, `style.marginLeft`, `style.marginRight`, `style.position`

## OverflowableToolbar.#moveItemsBackToTheirOrigin()
- 位置: async L8215-8312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `CustomizableUI.isSpecialWidget()`, `CustomizableUIInternal.ensureButtonContextMenu()`, `CustomizableUIInternal.notifyListeners()`, `child.removeAttribute()`, `defaultListItems.every()`, `gPlacements.get()`, `lazy.PanelMultiView.getViewNode()`, `lazy.log.debug()`, `placements.indexOf()`, `this.#hiddenOverflowedNodes.has()`, `this.#overflowedInfo.delete()`, `this.#overflowedInfo.entries()`, `this.#target.getElementsByAttribute()`, `win.UpdateUrlbarSearchSplitterState()`
- 条件付き依存: `if (!child)` → `this.#overflowedInfo.delete()`
- 条件付き依存: `if (!totalAvailWidth)` → `this.#getOverflowInfo()`
- 条件付き依存: `if (win.closed || this.#checkOverflowHandle != checkOverflowHandle)` → `lazy.log.debug()`
- 条件付き依存: `if (totalAvailWidth <= minSize)` → `lazy.log.debug()`
- 条件付き依存: `if (beforeNode && this.#target == beforeNode.parentElement)` → `this.#target.insertBefore()`
- 条件付き依存: `if (!inserted)` → `this.#target.appendChild()`
- 条件付き依存: `if ( defaultListItems.every( item => CustomizableUI.isSpecialWidget(item.id) || this.#hiddenOverflowedNodes.has(item) ) )` → `this.#toolbar.removeAttribute()`
- 参照: `beforeNode.parentElement`, `child.id`, `item.id`, `overflowedItemStack.length`, `placements.length`, `this.#checkOverflowHandle`, `this.#defaultList.children`, `this.#target`, `this.#target.documentGlobal`, `this.#target.ownerDocument`, `this.#toolbar.id`, `win.closed`

## OverflowableToolbar.#checkOverflow()
- 位置: async L8331-8360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.#getOverflowInfo()`, `win.document.documentElement.hasAttribute()`
- 条件付き依存: `if (isOverflowing)` → `this.#onOverflow()`
- 条件付き依存: `if (!(isOverflowing))` → `this.#moveItemsBackToTheirOrigin()`
- 参照: `this.#checkOverflowHandle`, `this.#enabled`, `this.#target.documentGlobal`, `win.closed`

## OverflowableToolbar.#disable()
- 位置: L8366-8372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#moveItemsBackToTheirOrigin()`
- 参照: `this.#checkOverflowHandle`, `this.#enabled`

## OverflowableToolbar.#enable()
- 位置: L8379-8382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#checkOverflow()`
- 参照: `this.#enabled`

## OverflowableToolbar.#showWithTimeout()
- 位置: L8388-8402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#defaultListPanel.firstElementChild.matches()`, `this.show()`, `this.show().then()`, `window.setTimeout()`
- 条件付き依存: `if (this.#hideTimeoutId)` → `window.clearTimeout()`
- 条件付き依存: `if (!this.#defaultListPanel.firstElementChild.matches(":hover"))` → `lazy.PanelMultiView.hidePopup()`
- 参照: `this.#defaultListPanel`, `this.#hideTimeoutId`, `this.#toolbar.documentGlobal`

## OverflowableToolbar.#webExtList()
- 位置: L8413-8427
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#webExtListRef)` → `this.#toolbar.getAttribute()`
- 条件付き依存: `if (!this.#webExtListRef)` → `panel.querySelector()`
- 参照: `this.#toolbar.documentGlobal`, `this.#toolbar.id`, `this.#webExtListRef`, `win.gUnifiedExtensions`

## OverflowableToolbar.#isOverflowList()
- 位置: L8436-8438
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#defaultList`, `this.#webExtList`

## OverflowableToolbar.#onClickDefaultListButton()
- 位置: L8449-8459
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#defaultListButton.open)` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if ( this.#defaultListPanel.state != "hiding" && !this.#defaultListButton.disabled )` → `this.show()`
- 参照: `this.#defaultListButton.disabled`, `this.#defaultListButton.open`, `this.#defaultListPanel`, `this.#defaultListPanel.state`

## OverflowableToolbar.#onPanelHiding()
- 位置: L8467-8485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.defaultView.updateEditUIVisibility()`, `this.#defaultListPanel.getAttribute()`, `this.#defaultListPanel.removeEventListener()`
- 条件付き依存: `if (contextMenuId)` → `doc.getElementById()`
- 条件付き依存: `if (contextMenuId)` → `contextMenu.removeEventListener()`
- 参照: `aEvent.target`, `aEvent.target.ownerDocument`, `this.#defaultListButton.open`, `this.#defaultListPanel`

## OverflowableToolbar.#onResize()
- 位置: L8493-8499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#checkOverflow()`
- 参照: `aEvent.currentTarget`, `aEvent.target`

## OverflowableToolbar.onWidgetBeforeDOMChange()
- 位置: L8505-8530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isOverflowList()`, `this.#overflowedInfo.set()`
- 条件付き依存: `if (aNode.previousElementSibling)` → `this.#overflowedInfo.get()`
- 参照: `aNode.nextElementSibling`, `aNode.previousElementSibling`, `aNode.previousElementSibling.id`, `nextItem.id`, `nextItem.nextElementSibling`, `this.#enabled`

## OverflowableToolbar.onWidgetAfterDOMChange()
- 位置: L8532-8597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#checkOverflow()`, `this.#isOverflowList()`, `this.#overflowedInfo.has()`
- 条件付き依存: `if (nowOverflowed)` → `this.#overflowedInfo.get()`
- 条件付き依存: `if (nowOverflowed)` → `this.#overflowedInfo.set()`
- 条件付き依存: `if (nowOverflowed)` → `aNode.setAttribute()`
- 条件付き依存: `if (nowOverflowed)` → `CustomizableUIInternal.ensureButtonContextMenu()`
- 条件付き依存: `if (nowOverflowed)` → `CustomizableUIInternal.notifyListeners()`
- 条件付き依存: `if (!nowOverflowed)` → `this.#overflowedInfo.delete()`
- 条件付き依存: `if (!nowOverflowed)` → `aNode.removeAttribute()`
- 条件付き依存: `if (!nowOverflowed)` → `CustomizableUIInternal.ensureButtonContextMenu()`
- 条件付き依存: `if (!nowOverflowed)` → `CustomizableUIInternal.notifyListeners()`
- 条件付き依存: `if (!nowOverflowed)` → `Array.from()`
- 条件付き依存: `if (!nowOverflowed)` → `this.#overflowedInfo.keys()`
- 条件付き依存: `if (!nowOverflowed)` → `collapsedWidgetIds.every()`
- 条件付き依存: `if (!nowOverflowed)` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if (collapsedWidgetIds.every(w => CustomizableUI.isSpecialWidget(w)))` → `this.#toolbar.removeAttribute()`
- 条件付き依存: `if (aNode.previousElementSibling)` → `this.#overflowedInfo.get()`
- 条件付き依存: `if (aNode.previousElementSibling)` → `this.#overflowedInfo.set()`
- 参照: `aNode.id`, `aNode.parentNode`, `aNode.previousElementSibling`, `aNode.previousElementSibling.id`, `sourceOfMinSize.id`, `this.#defaultListButton.id`, `this.#enabled`, `this.#target`

## OverflowableToolbar.isInOverflowList()
- 位置: L8602-8604
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `node.parentNode`, `this.#defaultList`

## OverflowableToolbar.observe()
- 位置: L8610-8620
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aTopic == "browser-delayed-startup-finished" && aSubject == this.#toolbar.documentGlobal )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( aTopic == "browser-delayed-startup-finished" && aSubject == this.#toolbar.documentGlobal )` → `this.init()`
- 参照: `this.#toolbar.documentGlobal`
- XPCOM: `Services.obs`

## OverflowableToolbar.handleEvent()
- 位置: L8626-8675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PanelMultiView.hidePopup()`, `this.#disable()`, `this.#enable()`, `this.#onPanelHiding()`, `this.#onResize()`
- 条件付き依存: `if (aEvent.target == this.#defaultListButton)` → `this.#onClickDefaultListButton()`
- 条件付き依存: `if (!(aEvent.target == this.#defaultListButton))` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if ( aEvent.target == this.#defaultListButton && (aEvent.key == " " || aEvent.key == "Enter") )` → `this.#onClickDefaultListButton()`
- 条件付き依存: `if (this.#enabled)` → `this.#showWithTimeout()`
- 参照: `aEvent.button`, `aEvent.key`, `aEvent.target`, `aEvent.type`, `this.#defaultListButton`, `this.#defaultListPanel`, `this.#enabled`
