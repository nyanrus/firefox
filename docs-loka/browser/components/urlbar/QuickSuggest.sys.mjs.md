# browser/components/urlbar/QuickSuggest.sys.mjs

source: browser/components/urlbar/QuickSuggest.sys.mjs
source-hash: ce4dc0f5e3af6b8a4efbb54031b1e6321e0b6b05
lines: 1331

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.entries()`, `Object.entries(REGION_LOCALE_DEFAULTS_EU_157_BOOLEAN).map()`, `Object.freeze()`, `Object.fromEntries()`, `Promise.withResolvers()`, `shouldOnlineBeAvailable()`

## _QuickSuggest.HELP_URL()
- 位置: L313-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- 参照: `this.HELP_TOPIC`
- XPCOM: `Services.urlFormatter`

## _QuickSuggest.HELP_TOPIC()
- 位置: L324-326
- 役割: (未記入)
- 触るとき: (未記入)

## _QuickSuggest.SETTINGS_UI()
- 位置: L335-337
- 役割: (未記入)
- 触るとき: (未記入)

## _QuickSuggest.SUGGEST_TOU_TIMESTAMP()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)

## _QuickSuggest.initPromise()
- 位置: L352-354
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#initResolvers.promise`

## _QuickSuggest.enabledBackends()
- 位置: L360-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByName.get()`
- 参照: `b?.isEnabled`, `this.rustBackend`

## _QuickSuggest.rustBackend()
- 位置: L374-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByName.get()`

## _QuickSuggest.config()
- 位置: L384-386
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.rustBackend?.config`

## _QuickSuggest.impressionCaps()
- 位置: L392-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByName.get()`

## _QuickSuggest.rustFeatures()
- 位置: L401-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByDynamicRustSuggestionType.values()`, `this.#featuresByRustSuggestionType.values()`

## _QuickSuggest.mlFeatures()
- 位置: L413-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByMlIntent.values()`

## _QuickSuggest.logger()
- 位置: L417-422
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._logger)` → `lazy.UrlbarShared.getLogger()`
- 参照: `this._logger`

## _QuickSuggest.init()
- 位置: async L430-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.entries()`, `lazy.NimbusFeatures.urlbar.ready()`, `lazy.Region.init()`, `lazy.UrlbarPrefs.addObserver()`, `this.#featuresByName.set()`, `this.#initPrefs()`, `this.#initResolvers.resolve()`, `this.#updateAll()`
- 条件付き依存: `if (!this._testSkipTelemetryEnvironmentInit)` → `lazy.TelemetryEnvironment.onInitialized()`
- 条件付き依存: `if (feature.merinoProvider)` → `this.#featuresByMerinoProvider.set()`
- 条件付き依存: `if (feature.dynamicRustSuggestionTypes?.length)` → `this.#featuresByDynamicRustSuggestionType.set()`
- 条件付き依存: `if (!(feature.dynamicRustSuggestionTypes?.length))` → `this.#featuresByRustSuggestionType.set()`
- 条件付き依存: `if (feature.mlIntent)` → `this.#featuresByMlIntent.set()`
- 条件付き依存: `if (prefs)` → `this.#featuresByEnablingPrefs.get()`
- 条件付き依存: `if (!features)` → `this.#featuresByEnablingPrefs.set()`
- 条件付き依存: `if (prefs)` → `features.add()`
- 参照: `feature.dynamicRustSuggestionTypes`, `feature.dynamicRustSuggestionTypes?.length`, `feature.enablingPreferences`, `feature.merinoProvider`, `feature.mlIntent`, `feature.rustSuggestionType`, `this.#initStarted`, `this._testSkipTelemetryEnvironmentInit`, `this.initPromise`

## _QuickSuggest.getFeature()
- 位置: L505-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByName.get()`

## _QuickSuggest.getFeatureByMlIntent()
- 位置: L519-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByMlIntent.get()`

## _QuickSuggest.getFeatureByResult()
- 位置: L531-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getFeatureBySource()`
- 参照: `result.payload`

## _QuickSuggest.getFeatureBySource()
- 位置: L560-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#featuresByMerinoProvider.get()`, `this.#featuresByRustSuggestionType.get()`, `this.getFeatureByMlIntent()`
- 条件付き依存: `if (provider == "Dynamic" && suggestionType)` → `this.#featuresByDynamicRustSuggestionType.get()`

## _QuickSuggest.dismissResult()
- 位置: async L586-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (result.payload.source == "rust")` → `this.rustBackend?.dismissRustSuggestion()`
- 条件付き依存: `if (!(result.payload.source == "rust"))` → `getDismissalKey()`
- 条件付き依存: `if (key)` → `this.rustBackend?.dismissByKey()`
- 参照: `result.payload.source`, `result.payload.suggestionObject`
- XPCOM: `Services.obs`

## _QuickSuggest.isResultDismissed()
- 位置: async L609-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `getDigest()`, `getDigest(result.payload.originalUrl || result.payload.url).then()`, `this.rustBackend?.isDismissedByKey()`, `values.some()`
- 条件付き依存: `if (result.payload.source == "rust")` → `promises.push()`
- 条件付き依存: `if (result.payload.source == "rust")` → `this.rustBackend?.isRustSuggestionDismissed()`
- 条件付き依存: `if (!(result.payload.source == "rust"))` → `getDismissalKey()`
- 条件付き依存: `if (key)` → `promises.push()`
- 条件付き依存: `if (key)` → `this.rustBackend?.isDismissedByKey()`
- 参照: `result.payload.originalUrl`, `result.payload.source`, `result.payload.suggestionObject`, `result.payload.url`

## _QuickSuggest.clearDismissedSuggestions()
- 位置: async L645-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.UrlbarPrefs.get()`, `this.logger.error()`, `this.rustBackend?.clearDismissedSuggestions()`
- 条件付き依存: `if (pref && !lazy.UrlbarPrefs.get(pref))` → `lazy.UrlbarPrefs.clear()`
- 参照: `feature.primaryUserControlledPreferences`, `this.#featuresByName`
- XPCOM: `Services.obs`

## _QuickSuggest.canClearDismissedSuggestions()
- 位置: async L681-715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.hasUserValue()`, `this.logger.error()`, `this.rustBackend?.anyDismissedSuggestions()`
- 参照: `feature.primaryUserControlledPreferences`, `this.#featuresByName`

## _QuickSuggest.intendedDefaultPrefs()
- 位置: L728-749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(SUGGEST_PREFS) .map()`, `Object.fromEntries()`, `defaultValues?.hasOwnProperty()`
- 条件付き依存: `if (defaultValues?.hasOwnProperty(region))` → `enablingLocales.includes()`
- 条件付き依存: `if (typeof prefValue == "function")` → `prefValue()`
- 参照: `this.#unmodifiedDefaultPrefs`

## _QuickSuggest.onPrefChanged()
- 位置: L757-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `f.primaryUserControlledPreferences.includes()`, `f.update()`, `this.#featuresByEnablingPrefs.get()`
- 条件付き依存: `if (pref == lazy.TelemetryReportingPolicy.TOU_ACCEPTED_DATE_PREF)` → `this.#initPrefs()`
- 条件付き依存: `if (isPrimaryUserControlledPref)` → `Services.obs.notifyObservers()`
- 参照: `lazy.TelemetryReportingPolicy.TOU_ACCEPTED_DATE_PREF`
- XPCOM: `Services.obs`

## _QuickSuggest.onNimbusChanged()
- 位置: L790-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#syncNimbusVariablesToUiPrefs()`, `this.#updateAll()`

## _QuickSuggest.isUrlEquivalentToResultUrl()
- 位置: L817-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feature.isUrlEquivalentToResultUrl()`, `this.getFeatureByResult()`
- 参照: `result.payload.url`

## _QuickSuggest.getFullKeywordTitleAndHighlights()
- 位置: L846-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.getTokenMatches()`

## _QuickSuggest.#uiPrefsByNimbusVariable()
- 位置: L866-876
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(SUGGEST_PREFS) .map()`, `Object.fromEntries()`

## _QuickSuggest.#initPrefs()
- 位置: L886-992
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `defaults.set()`, `this.#ensureUserPrefsMigrated()`, `this.#syncNimbusVariablesToUiPrefs()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `Object.fromEntries()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `Object.keys(SUGGEST_PREFS).map()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `Object.keys()`
- 条件付き依存: `if (!this.#unmodifiedDefaultPrefs)` → `defaults.get()`
- 条件付き依存: `if (!(testOverrides?.defaultPrefs))` → `this.intendedDefaultPrefs()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.Preferences`, `lazy.Region.home`, `testOverrides.defaultPrefs`, `testOverrides?.defaultPrefs`, `testOverrides?.locale`, `testOverrides?.region`, `this.#intendedDefaultPrefs`, `this.#unmodifiedDefaultPrefs`
- XPCOM: `Services.locale`

## _QuickSuggest.#syncNimbusVariablesToUiPrefs()
- 位置: L1002-1026
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `defaults.set()`, `lazy.NimbusFeatures.urlbar.getVariable()`
- 条件付き依存: `if (variable)` → `prefsByVariable.hasOwnProperty()`
- 参照: `lazy.Preferences`, `this.#intendedDefaultPrefs`, `this.#uiPrefsByNimbusVariable`

## _QuickSuggest.#updateAll()
- 位置: L1031-1040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feature.update()`, `this.#featuresByName.values()`

## _QuickSuggest.MIGRATION_VERSION()
- 位置: L1047-1049
- 役割: (未記入)
- 触るとき: (未記入)

## _QuickSuggest.#ensureUserPrefsMigrated()
- 位置: L1061-1094
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Services.prefs.getBranch()`, `console.error()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`, `this[methodName]()`
- 参照: `testOverrides.migrationVersion`, `testOverrides?.migrationVersion`, `this.MIGRATION_VERSION`
- XPCOM: `Services.prefs`

## _QuickSuggest._migrateUserPrefsTo_1()
- 位置: L1096-1134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userBranch.getBoolPref()`, `userBranch.prefHasUserValue()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest"))` → `userBranch.setBoolPref()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest"))` → `userBranch.getBoolPref()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest"))` → `userBranch.clearUserPref()`
- 条件付き依存: `if ( shouldEnableSuggest && userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored") && !userBranch.getBoolPref("suggest.quicksuggest.nonsponsored") )` → `userBranch.setBoolPref()`

## _QuickSuggest._migrateUserPrefsTo_2()
- 位置: L1136-1156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userBranch.getCharPref()`
- 条件付き依存: `if (scenario == "online")` → `userBranch.prefHasUserValue()`
- 条件付き依存: `if (!userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored"))` → `userBranch.setBoolPref()`
- 条件付き依存: `if (!userBranch.prefHasUserValue("suggest.quicksuggest.sponsored"))` → `userBranch.setBoolPref()`

## _QuickSuggest._migrateUserPrefsTo_3()
- 位置: L1158-1163
- 役割: (未記入)
- 触るとき: (未記入)

## _QuickSuggest._migrateUserPrefsTo_4()
- 位置: L1165-1170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userBranch.clearUserPref()`

## _QuickSuggest._migrateUserPrefsTo_5()
- 位置: L1172-1195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EN_LOCALES.includes()`, `["DE", "FR", "IT"].includes()`
- 条件付き依存: `if ( ["DE", "FR", "IT"].includes(lazy.Region.home) && EN_LOCALES.includes(Services.locale.appLocaleAsBCP47) )` → `userBranch.clearUserPref()`
- 参照: `Services.locale.appLocaleAsBCP47`, `lazy.Region.home`
- XPCOM: `Services.locale`

## _QuickSuggest._migrateUserPrefsTo_6()
- 位置: L1197-1214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userBranch.prefHasUserValue()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored"))` → `userBranch.setBoolPref()`
- 条件付き依存: `if (userBranch.prefHasUserValue("suggest.quicksuggest.nonsponsored"))` → `userBranch.getBoolPref()`

## _QuickSuggest._migrateUserPrefsTo_7()
- 位置: L1216-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userBranch.prefHasUserValue()`
- 条件付き依存: `if ( userBranch.prefHasUserValue("addons.minKeywordLength") && !userBranch.prefHasUserValue("addons.showLessFrequentlyCount") )` → `userBranch.setIntPref()`
- 条件付き依存: `if (!( userBranch.prefHasUserValue("addons.minKeywordLength") && !userBranch.prefHasUserValue("addons.showLessFrequentlyCount") ))` → `userBranch.prefHasUserValue()`
- 条件付き依存: `if ( !userBranch.prefHasUserValue("addons.minKeywordLength") && userBranch.prefHasUserValue("addons.showLessFrequentlyCount") )` → `userBranch.setIntPref()`

## _QuickSuggest._test_reset()
- 位置: async L1242-1257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#initPrefs()`, `this.#updateAll()`
- 参照: `this.#initStarted`, `this.initPromise`, `this.rustBackend`, `this.rustBackend.ingestPromise`

## userAcceptedSuggestToU()
- 位置: L1298-1301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `date.getTime()`
- 参照: `lazy.TelemetryReportingPolicy.termsOfUseAcceptedDate`

## shouldOnlineBeAvailable()
- 位置: L1311-1313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `userAcceptedSuggestToU()`

## getDismissalKey()
- 位置: L1315-1321
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.dismissalKey`, `result.payload.originalUrl`, `result.payload.url`

## getDigest()
- 位置: async L1323-1328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(hashArray, b => b.toString(16).padStart(2, "0")).join()`, `b.toString()`, `b.toString(16).padStart()`, `crypto.subtle.digest()`, `new TextEncoder().encode()`
