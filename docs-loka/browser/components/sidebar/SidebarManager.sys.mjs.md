# browser/components/sidebar/SidebarManager.sys.mjs

source: browser/components/sidebar/SidebarManager.sys.mjs
source-hash: 09dd32a61cc6020be289d14af544636abea2a18a
lines: 430

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `sidebarManager.handleVerticalTabsPrefChange()`, `sidebarManager.init()`, `sidebarManager.updateDefaultTools()`

## SidebarManager.constructor()
- 位置: L103-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.checkForPinnedTabsComplete`

## SidebarManager.init()
- 位置: L111-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `lazy.CustomizableUI.addListener()`, `lazy.NimbusFeatures.sidebar.onUpdate()`, `lazy.SessionStore.promiseAllWindowsRestored.then()`, `this.checkForPinnedTabs()`, `this.handleVerticalTabsPrefChange()`, `this.updateDefaultTools()`, `this.updateDefaultTools.bind()`
- 条件付き依存: `if (this.#initialized)` → `this.onNimbusFeatureUpdate()`
- 条件付き依存: `if (!(this.#initialized))` → `Promise.resolve().then()`
- 条件付き依存: `if (!(this.#initialized))` → `Promise.resolve()`
- 条件付き依存: `if (!(this.#initialized))` → `this.onNimbusFeatureUpdate()`
- 参照: `lazy.verticalTabsEnabled`, `this.#initialized`
- XPCOM: `Services.prefs`

## SidebarManager.onNimbusFeatureUpdate()
- 位置: L139-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`, `["revamp", "verticalTabs", "visibility"].forEach()`, `lazy.NimbusFeatures[featureId].getEnrollmentMetadata()`, `lazy.NimbusFeatures[featureId].getVariable()`, `setPref()`
- 参照: `AppConstants.MOZ_APP_VERSION_DISPLAY`, `enrollment.branch`, `enrollment.slug`, `lazy.NimbusFeatures`, `lazy.sidebarNimbus`
- XPCOM: `Services.vc`

## setPref()
- 位置: L165-170
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value != null)` → `lazy.PrefUtils.setPref()`

## SidebarManager.checkForPinnedTabs()
- 位置: L180-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 条件付き依存: `if (!lazy.dragToPinPromoDismissed)` → `lazy.BrowserWindowTracker.getOrderedWindows()`
- 条件付き依存: `if (win.gBrowser.pinnedTabCount > 0)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.dragToPinPromoDismissed`, `this.checkForPinnedTabsComplete`, `win.gBrowser.pinnedTabCount`
- XPCOM: `Services.prefs`

## SidebarManager.onWidgetRemoved()
- 位置: async L201-212
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId == "sidebar-button")` → `Promise.resolve()`
- 条件付き依存: `if (aWidgetId == "sidebar-button")` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!lazy.CustomizableUI.getPlacementOfWidget(aWidgetId))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!lazy.CustomizableUI.getPlacementOfWidget(aWidgetId))` → `this.closeAllSidebars()`
- XPCOM: `Services.prefs`

## SidebarManager.closeAllSidebars()
- 位置: L218-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getOrderedWindows()`, `w.SidebarController._state.loadCurrentState()`
- 条件付き依存: `if (w.SidebarController.isOpen)` → `w.SidebarController.hide()`
- 参照: `lazy.SidebarState.defaultProperties`, `w.SidebarController.isOpen`

## SidebarManager.handleVerticalTabsPrefChange()
- 位置: L237-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 条件付き依存: `if (!isEnabled)` → `HORIZONTAL_VISIBILITIES.includes()`
- 条件付き依存: `if (!HORIZONTAL_VISIBILITIES.includes(currentVisibility))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(!isEnabled))` → `VERTICAL_VISIBILITIES.includes()`
- 条件付き依存: `if (!VERTICAL_VISIBILITIES.includes(currentVisibility))` → `Services.prefs.setStringPref()`
- 参照: `this.#savedVisibility`
- XPCOM: `Services.prefs`

## SidebarManager.hasSidebarLauncherBeenVisible()
- 位置: L270-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.BrowserWindowTracker.getOrderedWindows()`
- 参照: `lazy.sidebarRevampEnabled`, `lazy.verticalTabsEnabled`, `w.SidebarController.launcherEverVisible`
- XPCOM: `Services.prefs`

## SidebarManager.updateDefaultTools()
- 位置: L296-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `JSON.stringify()`, `Services.prefs.getChildList()`, `Services.prefs.getStringPref()`, `Services.prefs.setStringPref()`, `console.error()`, `pref.split()`, `tools.includes()`
- 条件付き依存: `if (options?.visibilityPref)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!visibilityPrefValue)` → `Services.prefs.addObserver()`
- 条件付き依存: `if (!visibilityPrefValue)` → `this.updateDefaultTools.bind()`
- 条件付き依存: `if (tools.length > lazy.sidebarTools.length)` → `Services.prefs.setStringPref()`
- 参照: `lazy.newSidebarHasBeenUsed`, `lazy.sidebarRevampEnabled`, `lazy.sidebarTools`, `lazy.sidebarTools.length`, `options.alreadyShown`, `options.visibilityPref`, `options?.alreadyShown`, `options?.visibilityPref`, `tools.length`
- XPCOM: `Services.prefs`

## SidebarManager.updateToolsPref()
- 位置: L347-362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `lazy.sidebarTools.split()`, `updatedTools.indexOf()`, `updatedTools.join()`
- 条件付き依存: `if (remove)` → `updatedTools.splice()`
- 条件付き依存: `if (!(remove))` → `updatedTools.push()`
- 参照: `lazy.sidebarTools`
- XPCOM: `Services.prefs`

## SidebarManager.clearExtensionsPref()
- 位置: L364-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `installedExtensions.indexOf()`, `lazy.sidebarExtensions.split()`
- 条件付き依存: `if (index != -1)` → `installedExtensions.splice()`
- 条件付き依存: `if (index != -1)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (index != -1)` → `installedExtensions.join()`
- 参照: `lazy.sidebarExtensions`
- XPCOM: `Services.prefs`

## SidebarManager.cleanupPrefs()
- 位置: L378-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearExtensionsPref()`, `this.updateToolsPref()`

## SidebarManager.getBadgeTools()
- 位置: L389-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getChildList()`, `badgePrefs.map()`, `pref.slice()`
- 参照: `BADGE_PREF_BRANCH.length`
- XPCOM: `Services.prefs`

## SidebarManager.getBackupState()
- 位置: L404-411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.clearUserPref()`
- 参照: `lazy.sidebarBackupState`
- XPCOM: `Services.prefs`

## SidebarManager.setBackupState()
- 位置: L418-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`
