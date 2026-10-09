# browser/modules/HomePage.sys.mjs

source: browser/modules/HomePage.sys.mjs
source-hash: 762962c7ca610905f738440d6cd06461f99c2bd9
lines: 399

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getHomepagePref()
- 位置: L25-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getDefaultBranch()`, `prefs.getStringPref()`
- 条件付き依存: `if (!homePage && !useDefault)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!homePage && !useDefault)` → `getHomepagePref()`
- 参照: `Services.prefs`
- XPCOM: `Services.prefs`

## delayedStartup()
- 位置: async L60-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IgnoreLists.getAndSubscribe()`, `this._addCustomizableUiListener()`, `this._handleIgnoreListUpdated()`, `this._handleIgnoreListUpdated.bind()`
- 参照: `this._ignoreListListener`, `this._initializationPromise`

## get()
- 位置: L90-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getHomepagePref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( lazy.PrivateBrowsingUtils.permanentPrivateBrowsing || (aWindow && lazy.PrivateBrowsingUtils.isWindowPrivate(aWindow)) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( lazy.PrivateBrowsingUtils.permanentPrivateBrowsing || (aWindow && lazy.PrivateBrowsingUtils.isWindowPrivate(aWindow)) )` → `homePages.includes()`
- 条件付き依存: `if ( !privateAllowed && (extensionControlled || homePages.includes("moz-extension://")) )` → `this.getDefault()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.prefs`

## getForErrorPage()
- 位置: L123-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.get()`, `url.includes()`
- 条件付き依存: `if (url.includes("|"))` → `url.split()`
- 参照: `win.BROWSER_NEW_TAB_URL`

## parseCustomHomepageURLs()
- 位置: L141-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.trim()`, `urls .split()`, `urls .split("|") .map()`, `urls .split("|") .map(url => url.trim()) .filter()`

## isPreferencesOrSettingsTab()
- 位置: L154-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.linkedBrowser.currentURI.spec.startsWith()`

## getTabsForCustomHomepage()
- 位置: L167-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `win.document.documentElement.getAttribute()`
- 条件付き依存: `if ( win && win.document.documentElement.getAttribute("windowtype") === "navigator:browser" )` → `win.gBrowser.visibleTabs.slice()`
- 条件付き依存: `if ( win && win.document.documentElement.getAttribute("windowtype") === "navigator:browser" )` → `tabs.filter()`
- 条件付き依存: `if ( win && win.document.documentElement.getAttribute("windowtype") === "navigator:browser" )` → `this.isPreferencesOrSettingsTab()`
- 参照: `tab.closing`, `win.gBrowser.pinnedTabCount`
- XPCOM: `Services.wm`

## getDefault()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getHomepagePref()`

## getOriginalDefault()
- 位置: L199-201
- 役割: (未記入)
- 触るとき: (未記入)

## overridden()
- 位置: L207-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## locked()
- 位置: L215-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## isDefault()
- 位置: L223-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HomePage.get()`

## set()
- 位置: async L234-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `this._maybeAddHomeButtonToToolbar()`, `this.delayedStartup()`, `this.shouldIgnore()`
- 条件付き依存: `if (await this.shouldIgnore(value))` → `console.error()`
- 条件付き依存: `if (await this.shouldIgnore(value))` → `Glean.homepage.preferenceIgnore.record()`
- XPCOM: `Services.prefs`

## safeSet()
- 位置: L259-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## clear()
- 位置: L267-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## reset()
- 位置: L274-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## shouldIgnore()
- 位置: async L286-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `code.toLowerCase()`, `lowerURL.includes()`, `this._ignoreList.some()`, `this.delayedStartup()`, `url.toLowerCase()`

## _handleIgnoreListUpdated()
- 位置: async L300-349
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.overridden)` → `getHomepagePref().toLowerCase()`
- 条件付き依存: `if (this.overridden)` → `getHomepagePref()`
- 条件付き依存: `if (this.overridden)` → `this._ignoreList.some()`
- 条件付き依存: `if (this.overridden)` → `homePages.includes()`
- 条件付き依存: `if (this.overridden)` → `code.toLowerCase()`
- 条件付き依存: `if ( this._ignoreList.some(code => homePages.includes(code.toLowerCase())) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(kExtensionControllerPref, false))` → `lazy.ExtensionPreferencesManager.getSetting()`
- 条件付き依存: `if (item && item.id)` → `lazy.ExtensionParent.apiManager.asyncLoadModule()`
- 条件付き依存: `if (item && item.id)` → `lazy.ExtensionPreferencesManager.removeSetting( item.id, "homepage_override" ).catch()`
- 条件付き依存: `if (item && item.id)` → `lazy.ExtensionPreferencesManager.removeSetting()`
- 条件付き依存: `if (!(item && item.id))` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref(kExtensionControllerPref, false)))` → `this.clear()`
- 条件付き依存: `if ( this._ignoreList.some(code => homePages.includes(code.toLowerCase())) )` → `Glean.homepage.preferenceIgnore.record()`
- 参照: `Services.appinfo.inSafeMode`, `console.error`, `entry.id`, `entry.matches`, `item.id`, `this._ignoreList`, `this.overridden`
- XPCOM: `Services.appinfo` / `Services.prefs`

## onWidgetRemoved()
- 位置: L351-356
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (widgetId == kWidgetId)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (widgetId == kWidgetId)` → `lazy.CustomizableUI.removeListener()`
- XPCOM: `Services.prefs`

## _maybeAddHomeButtonToToolbar()
- 位置: L366-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.CustomizableUI.getWidget()`
- 条件付き依存: `if ( homePage !== "about:home" && homePage !== "about:blank" && !Services.prefs.getBoolPref(kExtensionControllerPref, false) && !Services.prefs.getBoolPref(kWidg...)` → `lazy.CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if ( homePage !== "about:home" && homePage !== "about:blank" && !Services.prefs.getBoolPref(kExtensionControllerPref, false) && !Services.prefs.getBoolPref(kWidg...)` → `navbarPlacements.indexOf()`
- 条件付き依存: `if ( homePage !== "about:home" && homePage !== "about:blank" && !Services.prefs.getBoolPref(kExtensionControllerPref, false) && !Services.prefs.getBoolPref(kWidg...)` → `navbarPlacements[i].startsWith()`
- 条件付き依存: `if ( homePage !== "about:home" && homePage !== "about:blank" && !Services.prefs.getBoolPref(kExtensionControllerPref, false) && !Services.prefs.getBoolPref(kWidg...)` → `navbarPlacements[i].includes()`
- 条件付き依存: `if ( homePage !== "about:home" && homePage !== "about:blank" && !Services.prefs.getBoolPref(kExtensionControllerPref, false) && !Services.prefs.getBoolPref(kWidg...)` → `lazy.CustomizableUI.addWidgetToArea()`
- 参照: `lazy.CustomizableUI.getWidget(kWidgetId).areaType`
- XPCOM: `Services.prefs`

## _addCustomizableUiListener()
- 位置: L393-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(kWidgetRemovedPref, false))` → `lazy.CustomizableUI.addListener()`
- XPCOM: `Services.prefs`
