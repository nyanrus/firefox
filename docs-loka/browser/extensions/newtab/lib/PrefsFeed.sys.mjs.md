# browser/extensions/newtab/lib/PrefsFeed.sys.mjs

source: browser/extensions/newtab/lib/PrefsFeed.sys.mjs
source-hash: 12f7ed94c362bbfa99603431f04e4ae05140db40
lines: 1188

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## recordsHistory()
- 位置: L76-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.prefs`

## isWidgetSearchSapHostSupported()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`
- 参照: `AppConstants.MOZ_APP_VERSION`
- XPCOM: `Services.vc`

## PrefsFeed.constructor()
- 位置: L133-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `this.onAdsBackendUpdated.bind()`, `this.onExperimentUpdated.bind()`, `this.onInferredPersonalizationExperimentUpdated.bind()`, `this.onOhttpImagesUpdated.bind()`, `this.onPocketExperimentUpdated.bind()`, `this.onSmartShortcutsExperimentUpdated.bind()`, `this.onTrainhopExperimentUpdated.bind()`, `this.onWidgetsUpdated.bind()`
- 参照: `this._lockedPrefs`, `this._prefMap`, `this._prefs`, `this._prefs._branchStr`, `this._prefsTransaction`, `this.onAdsBackendUpdated`, `this.onExperimentUpdated`, `this.onInferredPersonalizationExperimentUpdated`, `this.onOhttpImagesUpdated`, `this.onPocketExperimentUpdated`, `this.onSmartShortcutsExperimentUpdated`, `this.onTrainhopExperimentUpdated`, `this.onWidgetsUpdated`

## PrefsFeed.onPrefChanged()
- 位置: L170-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._mirrorSpaceOptOut()`, `this._prefMap.get()`
- 条件付き依存: `if (prefItem)` → `this.updateLockedPref()`
- 条件付き依存: `if (this._prefsTransaction && action === "BroadcastToContent")` → `this.store.dispatch()`
- 条件付き依存: `if (this._prefsTransaction && action === "BroadcastToContent")` → `ac.OnlyToMain()`
- 条件付き依存: `if (!(this._prefsTransaction && action === "BroadcastToContent"))` → `this.store.dispatch()`
- 条件付き依存: `if (!(this._prefsTransaction && action === "BroadcastToContent"))` → `ac[action]()`
- 条件付き依存: `if (isUserChange && this.inActivationWindowState)` → `this.trackActivationWindowPrefChange()`
- 参照: `at.PREF_CHANGED`, `prefItem.alsoToPreloaded`, `prefItem.skipBroadcast`, `this._prefsTransaction`, `this.inActivationWindowState`

## PrefsFeed.updateLockedPref()
- 位置: L214-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this._lockedPrefs.has()`, `this._prefs.locked()`, `this.store.dispatch()`
- 条件付き依存: `if (locked)` → `this._lockedPrefs.add()`
- 条件付き依存: `if (!(locked))` → `this._lockedPrefs.delete()`
- 参照: `at.PREF_CHANGED`, `this._lockedPrefs`

## PrefsFeed.trackActivationWindowPrefChange()
- 位置: L240-252
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (name === TOP_SITES_ENABLED_PREF)` → `this._prefs.set()`
- 条件付き依存: `if (name === TOP_SITES_ENABLED_PREF)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (name === TOP_STORIES_ENABLED_PREF)` → `this._prefs.set()`
- 条件付き依存: `if (name === TOP_STORIES_ENABLED_PREF)` → `lazy.logConsole.debug()`

## PrefsFeed._setStringPref()
- 位置: L254-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setPref()`
- 参照: `Services.prefs.getStringPref`
- XPCOM: `Services.prefs`

## PrefsFeed._setBoolPref()
- 位置: L258-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setPref()`
- 参照: `Services.prefs.getBoolPref`
- XPCOM: `Services.prefs`

## PrefsFeed._setIntPref()
- 位置: L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setPref()`
- 参照: `Services.prefs.getIntPref`
- XPCOM: `Services.prefs`

## PrefsFeed._setPref()
- 位置: L266-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPrefFunction()`, `this._prefMap.set()`

## PrefsFeed.onExperimentUpdated()
- 位置: L278-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `lazy.NimbusFeatures.newtab.getAllVariables()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed._getTrainhopConfig()
- 位置: L298-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Services.prefs.getDefaultBranch()`, `allEnrollments.forEach()`, `enrollmentsToProcess.reduce()`, `lazy.NimbusFeatures.newtabTrainhop.getAllEnrollments()`, `this._applySpacePrefDefaults()`, `this._prefs.get()`
- 条件付き依存: `if ( enrollment?.value?.type === "multi-payload" && Array.isArray(enrollment?.value?.payload) )` → `enrollment.value.payload.forEach()`
- 条件付き依存: `if (item?.type && item?.payload)` → `enrollmentsToProcess.push()`
- 条件付き依存: `if (enrollment?.value?.type)` → `enrollmentsToProcess.push()`
- 条件付き依存: `if (valueObj.widgets?.weatherForecastEnabled && valueObj.weather?.display)` → `Services.prefs .getDefaultBranch(this._prefs._branchStr) .setStringPref()`
- 条件付き依存: `if (valueObj.widgets?.weatherForecastEnabled && valueObj.weather?.display)` → `Services.prefs .getDefaultBranch()`
- 条件付き依存: `if ( typeof valueObj.widgets?.weatherSize === "string" && valueObj.widgets.weatherSize )` → `Services.prefs .getDefaultBranch(this._prefs._branchStr) .setStringPref()`
- 条件付き依存: `if ( typeof valueObj.widgets?.weatherSize === "string" && valueObj.widgets.weatherSize )` → `Services.prefs .getDefaultBranch()`
- 条件付き依存: `if (valueObj.topSites?.topSitesRows)` → `Services.prefs .getDefaultBranch(this._prefs._branchStr) .setIntPref()`
- 条件付き依存: `if (valueObj.topSites?.topSitesRows)` → `Services.prefs .getDefaultBranch()`
- 条件付き依存: `if ( valueObj.wallpaper?.initialWallpaper && !this._prefs.get("newtabWallpapers.initialWallpaper") )` → `this._prefs.set()`
- 条件付き依存: `if (typeof value === "boolean")` → `defaultBranch.setBoolPref()`
- 条件付き依存: `if (typeof containerEnabled === "boolean")` → `defaultBranch.setBoolPref()`
- 参照: `accumulator[currentValue.value.type].meta.isRollout`, `currentValue.meta.isRollout`, `currentValue.value.payload`, `currentValue.value.type`, `currentValue?.value?.type`, `enrollment.meta`, `enrollment?.value?.payload`, `enrollment?.value?.type`, `item.payload`, `item.type`, `item?.payload`, `item?.type`, `namespaced?.enabled`, `this._prefs._branchStr`, `this._trainhopConfig`, `valueObj.topSites.topSitesRows`, `valueObj.topSites?.topSitesRows`, `valueObj.wallpaper.initialWallpaper`, `valueObj.wallpaper?.initialWallpaper`, `valueObj.weather.display`, `valueObj.weather?.display`, `valueObj.widgets`, `valueObj.widgets.weatherSize`, `valueObj.widgets?.enabled`, `valueObj.widgets?.weatherForecastEnabled`, `valueObj.widgets?.weatherSize`, `valueObj.widgetsSettings`, `valueObj.widgetsSettings?.enabled`, `widget.enabledPref`, `widget.trainhopEnabledKey`, `widget.trainhopNamespace`, `widget.widgetsSettingsEnabledKey`
- XPCOM: `Services.prefs`

## PrefsFeed._getAdsBackendFeatures()
- 位置: L434-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allEnrollments.reduce()`, `lazy.NimbusFeatures.adsBackend.getAllEnrollments()`
- 条件付き依存: `if (currentValue?.value?.flags)` → `Object.entries()`
- 参照: `accumulator[key].meta.isRollout`, `currentValue.meta.isRollout`, `currentValue.value.flags`, `currentValue?.value?.flags`

## PrefsFeed._spacesVariantPrefs()
- 位置: L463-468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.get()`
- 参照: `this._trainhopConfig`

## PrefsFeed._mirrorSpaceOptOut()
- 位置: L484-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(SPACE_CONFIG).find()`, `isSpacesAssigned()`, `this._prefs.get()`, `this._spacesVariantPrefs()`
- 条件付き依存: `if (this._prefs.get(space.optOutPref) !== !value)` → `this._prefs.set()`
- 参照: `s.userPref`, `space.optOutPref`

## PrefsFeed._applySpacePrefDefaults()
- 位置: L507-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `isSpacesAssigned()`, `this._spacesVariantPrefs()`
- 条件付き依存: `if (assigned && typeof enabled === "boolean")` → `Services.prefs .getDefaultBranch(this._prefs._branchStr) .setBoolPref()`
- 条件付き依存: `if (assigned && typeof enabled === "boolean")` → `Services.prefs .getDefaultBranch()`
- 条件付き依存: `if (assigned && typeof enabled === "boolean")` → `this._wroteSpaceDefaults.add()`
- 条件付き依存: `if (!(assigned && typeof enabled === "boolean"))` → `this._wroteSpaceDefaults.has()`
- 条件付き依存: `if (this._wroteSpaceDefaults.has(userPref))` → `Services.prefs .getDefaultBranch(this._prefs._branchStr) .setBoolPref()`
- 条件付き依存: `if (this._wroteSpaceDefaults.has(userPref))` → `Services.prefs .getDefaultBranch()`
- 条件付き依存: `if (this._wroteSpaceDefaults.has(userPref))` → `PREFS_CONFIG.get()`
- 条件付き依存: `if (this._wroteSpaceDefaults.has(userPref))` → `this._wroteSpaceDefaults.delete()`
- 参照: `PREFS_CONFIG.get(userPref).value`, `space.feedGated`, `this._prefs._branchStr`, `this._wroteSpaceDefaults`, `valueObj[trainhopKey]?.enabled`
- XPCOM: `Services.prefs`

## PrefsFeed.onTrainhopExperimentUpdated()
- 位置: L537-549
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this._getTrainhopConfig()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed.onPocketExperimentUpdated()
- 位置: L554-582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pocketNewtab.getAllVariables()`, `this._prefs.get()`
- 条件付き依存: `if ( value.currentWallpaper && !this._prefs.get("newtabWallpapers.initialWallpaper") )` → `this._prefs.set()`
- 条件付き依存: `if ( reason !== "feature-experiment-loaded" && reason !== "feature-rollout-loaded" )` → `this.store.dispatch()`
- 条件付き依存: `if ( reason !== "feature-experiment-loaded" && reason !== "feature-rollout-loaded" )` → `ac.BroadcastToContent()`
- 参照: `at.PREF_CHANGED`, `value.currentWallpaper`

## PrefsFeed.onSmartShortcutsExperimentUpdated()
- 位置: L587-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `lazy.NimbusFeatures.newtabSmartShortcuts.getAllVariables()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed.onInferredPersonalizationExperimentUpdated()
- 位置: L604-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `lazy.NimbusFeatures.newtabInferredPersonalization.getAllVariables()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed.onWidgetsUpdated()
- 位置: L621-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `lazy.NimbusFeatures.newtabWidgets.getAllVariables()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed.onOhttpImagesUpdated()
- 位置: L637-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `lazy.NimbusFeatures.newtabOhttpImages.getAllVariables()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed.onAdsBackendUpdated()
- 位置: L653-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this._getAdsBackendFeatures()`, `this.store.dispatch()`
- 参照: `at.PREF_CHANGED`

## PrefsFeed.init()
- 位置: L667-800
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `Temporal.Now.instant()`, `[...this._prefMap.keys()].filter()`, `ac.BroadcastToContent()`, `globalThis.WebExtensionPolicy?.getByID()`, `isWidgetSearchSapHostSupported()`, `lazy.NimbusFeatures.adsBackend.onUpdate()`, `lazy.NimbusFeatures.newtab.getAllVariables()`, `lazy.NimbusFeatures.newtab.onUpdate()`, `lazy.NimbusFeatures.newtabInferredPersonalization.onUpdate()`, `lazy.NimbusFeatures.newtabOhttpImages.onUpdate()`, `lazy.NimbusFeatures.newtabSmartShortcuts.getAllVariables()`, `lazy.NimbusFeatures.newtabSmartShortcuts.onUpdate()`, `lazy.NimbusFeatures.newtabTrainhop.onUpdate()`, `lazy.NimbusFeatures.newtabWidgets.getAllVariables()`, `lazy.NimbusFeatures.newtabWidgets.onUpdate()`, `lazy.NimbusFeatures.pocketNewtab.getAllVariables()`, `lazy.NimbusFeatures.pocketNewtab.onUpdate()`, `recordsHistory()`, `this._getAdsBackendFeatures()`, `this._getTrainhopConfig()`, `this._prefMap.keys()`, `this._prefMap.set()`, `this._prefs.get()`, `this._prefs.locked()`, `this._prefs.observeBranch()`, `this.checkForActivationWindow()`, `this.store.dispatch()`
- 条件付き依存: `if (this.geo !== "")` → `Services.obs.addObserver()`
- 条件付き依存: `if ( values.pocketConfig.currentWallpaper && !this._prefs.get("newtabWallpapers.initialWallpaper") )` → `this._prefs.set()`
- 条件付き依存: `if (type === "bool")` → `this._setBoolPref()`
- 条件付き依存: `if (type === "string")` → `this._setStringPref()`
- 参照: `AppConstants.platform`, `at.PREFS_INITIAL_VALUES`, `globalThis.WebExtensionPolicy?.getByID("newtab@mozilla.org")?.version`, `lazy.PrivateBrowsingUtils.enabled`, `lazy.Region.REGION_TOPIC`, `lazy.Region.home`, `this._lockedPrefs`, `this._recordsHistory`, `this.geo`, `this.onAdsBackendUpdated`, `this.onExperimentUpdated`, `this.onInferredPersonalizationExperimentUpdated`, `this.onOhttpImagesUpdated`, `this.onPocketExperimentUpdated`, `this.onSmartShortcutsExperimentUpdated`, `this.onTrainhopExperimentUpdated`, `this.onWidgetsUpdated`, `values.adsBackendConfig`, `values.appUpdateChannel`, `values.browserNovaEnabled`, `values.featureConfig`, `values.fxa_endpoint`, `values.isPrivateBrowsingEnabled`, `values.lockedPrefs`, `values.mayHaveSponsoredTopSites`, `values.nimbusDebug`, `values.platform`, `values.pocketConfig`, `values.pocketConfig.currentWallpaper`, `values.recordsHistory`, `values.region`, `values.smartShortcutsConfig`, `values.supportsWidgetSearchSap`, `values.trainhopConfig`, `values.trainhopVersion`, `values.widgetsConfig`
- XPCOM: `Services.obs` / `Services.prefs`

## PrefsFeed.uninit()
- 位置: L802-804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeListeners()`

## PrefsFeed.removeListeners()
- 位置: L806-830
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `lazy.NimbusFeatures.adsBackend.offUpdate()`, `lazy.NimbusFeatures.newtab.offUpdate()`, `lazy.NimbusFeatures.newtabInferredPersonalization.offUpdate()`, `lazy.NimbusFeatures.newtabOhttpImages.offUpdate()`, `lazy.NimbusFeatures.newtabSmartShortcuts.offUpdate()`, `lazy.NimbusFeatures.newtabTrainhop.offUpdate()`, `lazy.NimbusFeatures.newtabWidgets.offUpdate()`, `lazy.NimbusFeatures.pocketNewtab.offUpdate()`, `this._prefs.ignoreBranch()`
- 条件付き依存: `if (this.geo === "")` → `Services.obs.removeObserver()`
- 参照: `lazy.Region.REGION_TOPIC`, `this.geo`, `this.onAdsBackendUpdated`, `this.onExperimentUpdated`, `this.onInferredPersonalizationExperimentUpdated`, `this.onOhttpImagesUpdated`, `this.onPocketExperimentUpdated`, `this.onSmartShortcutsExperimentUpdated`, `this.onTrainhopExperimentUpdated`, `this.onWidgetsUpdated`
- XPCOM: `Services.obs` / `Services.prefs`

## PrefsFeed.checkForActivationWindow()
- 位置: L842-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Temporal.Instant.compare()`, `Temporal.Now.instant()`, `lazy.SelectableProfileService.hasCreatedSelectableProfiles()`, `now.subtract()`, `this.store.getState()`
- 条件付き依存: `if ( !enabled || !createdInstant || !variant || lazy.SelectableProfileService.hasCreatedSelectableProfiles() )` → `lazy.logConsole.log()`
- 条件付き依存: `if ( !enabled || !createdInstant || !variant || lazy.SelectableProfileService.hasCreatedSelectableProfiles() )` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.inActivationWindowState)` → `lazy.logConsole.log()`
- 条件付き依存: `if (this.inActivationWindowState)` → `this.exitActivationWindowState()`
- 条件付き依存: `if (withinMaxProfileAgeInHours)` → `lazy.logConsole.log()`
- 条件付き依存: `if (withinMaxProfileAgeInHours)` → `this.enterActivationWindowState()`
- 参照: `lazy.AboutNewTab.activityStream`, `state.Prefs`, `this.inActivationWindowState`, `values?.trainhopConfig?.activationWindowBehavior`

## PrefsFeed.enterActivationWindowState()
- 位置: L919-986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getDefaultBranch()`, `lazy.logConsole.debug()`, `lazy.logConsole.log()`, `this._prefs.reset()`, `this._prefs.set()`
- 条件付き依存: `if (!isStartup && this.inActivationWindowState === variant)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (disableTopSites)` → `lazy.logConsole.log()`
- 条件付き依存: `if (disableTopSites)` → `defaultBranch.setBoolPref()`
- 条件付き依存: `if (disableTopSites)` → `this.onPrefChanged()`
- 条件付き依存: `if (disableTopStories)` → `lazy.logConsole.log()`
- 条件付き依存: `if (disableTopStories)` → `defaultBranch.setBoolPref()`
- 条件付き依存: `if (disableTopStories)` → `this.onPrefChanged()`
- 条件付き依存: `if (enterActivationWindowMessageID)` → `this._prefs.set()`
- 参照: `this._prefs._branchStr`, `this.inActivationWindowState`
- XPCOM: `Services.prefs`

## PrefsFeed.exitActivationWindowState()
- 位置: L994-1090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getDefaultBranch()`, `defaultBranch.setBoolPref()`, `lazy.logConsole.debug()`, `lazy.logConsole.log()`, `this._prefs.isSet()`, `this._prefs.reset()`, `this._prefs.set()`
- 条件付き依存: `if (!hasTopSitesTempPref)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasTopSitesTempPref)` → `this.onPrefChanged()`
- 条件付き依存: `if (!(!hasTopSitesTempPref))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasTopStoriesTempPref)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!hasTopStoriesTempPref)` → `this.onPrefChanged()`
- 条件付き依存: `if (!(!hasTopStoriesTempPref))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (hasTopSitesTempPref)` → `this._prefs.get()`
- 条件付き依存: `if (hasTopSitesTempPref)` → `lazy.logConsole.log()`
- 条件付き依存: `if (hasTopSitesTempPref)` → `this._prefs.set()`
- 条件付き依存: `if (hasTopSitesTempPref)` → `this._prefs.reset()`
- 条件付き依存: `if (hasTopSitesTempPref)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (hasTopStoriesTempPref)` → `this._prefs.get()`
- 条件付き依存: `if (hasTopStoriesTempPref)` → `lazy.logConsole.log()`
- 条件付き依存: `if (hasTopStoriesTempPref)` → `this._prefs.set()`
- 条件付き依存: `if (hasTopStoriesTempPref)` → `this._prefs.reset()`
- 条件付き依存: `if (hasTopStoriesTempPref)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (exitActivationWindowMessageID)` → `this._prefs.set()`
- 条件付き依存: `if (!(exitActivationWindowMessageID))` → `this._prefs.set()`
- 参照: `new Error().stack`, `this._prefs._branchStr`
- XPCOM: `Services.prefs`

## PrefsFeed.observe()
- 位置: L1092-1136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 条件付き依存: `if (data === BROWSER_NOVA_ENABLED_PREF)` → `this.store.dispatch()`
- 条件付き依存: `if (data === BROWSER_NOVA_ENABLED_PREF)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (data === BROWSER_NOVA_ENABLED_PREF)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(data === BROWSER_NOVA_ENABLED_PREF))` → `RECORDS_HISTORY_PREFS.includes()`
- 条件付き依存: `if (RECORDS_HISTORY_PREFS.includes(data))` → `recordsHistory()`
- 条件付き依存: `if (nextRecordsHistory !== this._recordsHistory)` → `this.store.dispatch()`
- 条件付き依存: `if (nextRecordsHistory !== this._recordsHistory)` → `ac.BroadcastToContent()`
- 参照: `at.PREF_CHANGED`, `lazy.Region.REGION_TOPIC`, `lazy.Region.home`, `this._recordsHistory`
- XPCOM: `Services.prefs`

## PrefsFeed.onAction()
- 位置: L1138-1186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.keys()`, `Services.prefs.clearUserPref()`, `this._mirrorSpaceOptOut()`, `this._prefs.set()`, `this.checkForActivationWindow()`, `this.init()`, `this.uninit()`
- 条件付き依存: `if (Object.keys(values).length)` → `this.store.dispatch()`
- 条件付き依存: `if (Object.keys(values).length)` → `ac.BroadcastToContent()`
- 参照: `Object.keys(values).length`, `action.data.name`, `action.data.value`, `action.data.values`, `action.type`, `at.CLEAR_PREF`, `at.INIT`, `at.MULTIPLE_PREFS_CHANGED`, `at.NEW_TAB_STATE_REQUEST`, `at.SET_MULTIPLE_PREFS`, `at.SET_PREF`, `at.UNINIT`, `this._prefs._branchStr`, `this._prefsTransaction`
- XPCOM: `Services.prefs`
