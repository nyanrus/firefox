# browser/components/extensions/parent/ext-chrome-settings-overrides.js

source: browser/components/extensions/parent/ext-chrome-settings-overrides.js
source-hash: b144aca5259106767393bd1e4f140abfa9623ac0
lines: 573

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ExtensionPreferencesManager.addSetting()`

## beforeDisableAddon()
- 位置: async L48-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.prefs.addObserver()`, `replaceUrlInTab()`
- 参照: `gBrowser.selectedTab`, `win.gBrowser`
- XPCOM: `Services.io` / `Services.prefs`

## prefObserver()
- 位置: async L59-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `popup.open()`, `waitForTabLoaded()`, `win.BrowserCommands.home()`
- XPCOM: `Services.prefs`

## handleInitialHomepagePopup()
- 位置: async L79-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `homepagePopup.addObserver()`
- 条件付き依存: `if (currentUrl != homepageUrl && currentUrl == "about:blank")` → `waitForTabLoaded()`
- 条件付き依存: `if (currentUrl == homepageUrl && gBrowser.selectedTab == tab)` → `homepagePopup.open()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedTab`, `windowTracker.topWindow`
- XPCOM: `Services.prefs`

## handleHomepageUrl()
- 位置: async L113-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionPreferencesManager.setSetting()`, `extension.on()`, `permissions.permissions.includes()`
- 条件付き依存: `if (inControl)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (extension.startupReason == "APP_STARTUP")` → `handleInitialHomepagePopup()`
- 条件付き依存: `if (!(extension.startupReason == "APP_STARTUP"))` → `homepagePopup.addObserver()`
- 条件付き依存: `if (permissions.permissions.includes("internal:privateBrowsingAllowed"))` → `ExtensionPreferencesManager.getSetting()`
- 条件付き依存: `if (item && item.id == extension.id)` → `Services.prefs.setBoolPref()`
- 参照: `extension.id`, `extension.privateBrowsingAllowed`, `extension.startupReason`, `item.id`
- XPCOM: `Services.prefs`

## processDefaultSearchSetting()
- 位置: async L173-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSettingsStore.getLevelOfControl()`, `ExtensionSettingsStore.getSetting()`, `ExtensionSettingsStore.initialize()`, `ExtensionSettingsStore[action]()`
- 条件付き依存: `if (item && control == "controlled_by_this_extension")` → `SearchService.getEngineByName()`
- 条件付き依存: `if (engine)` → `SearchService.setDefault()`
- 条件付き依存: `if (item && control == "controlled_by_this_extension")` → `Cu.reportError()`
- 参照: `SearchService.CHANGE_REASON.ADDON_INSTALL`, `SearchService.CHANGE_REASON.ADDON_UNINSTALL`, `item.initialValue`, `item.value`

## removeEngine()
- 位置: async L212-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.reportError()`, `SearchService.removeWebExtensionEngine()`

## removeSearchSettings()
- 位置: L220-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `this.processDefaultSearchSetting()`, `this.removeEngine()`

## onUninstall()
- 位置: async L227-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `homepagePopup.clearConfirmation()`, `pendingSearchSetupTasks.get()`, `this.removeSearchSettings()`
- 条件付き依存: `if (searchStartupPromise)` → `searchStartupPromise.catch()`
- 参照: `Cu.reportError`

## onUpdate()
- 位置: async L240-258
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!manifest?.chrome_settings_overrides?.homepage)` → `ExtensionPreferencesManager.removeSetting()`
- 条件付き依存: `if (!search_provider)` → `this.removeSearchSettings()`
- 条件付き依存: `if (!search_provider.is_default)` → `chrome_settings_overrides.processDefaultSearchSetting()`
- 参照: `manifest?.chrome_settings_overrides?.homepage`, `manifest?.chrome_settings_overrides?.search_provider`, `search_provider.is_default`

## onDisable()
- 位置: async L260-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chrome_settings_overrides.processDefaultSearchSetting()`, `chrome_settings_overrides.removeEngine()`, `homepagePopup.clearConfirmation()`

## onManifestEntry()
- 位置: async L267-305
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (homepageUrl)` → `HomePage.shouldIgnore()`
- 条件付き依存: `if (ignoreHomePageUrl)` → `Glean.homepage.preferenceIgnore.record()`
- 条件付き依存: `if (!(ignoreHomePageUrl))` → `handleHomepageUrl()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `this.processSearchProviderManifestEntry().finally()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `this.processSearchProviderManifestEntry()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `pendingSearchSetupTasks.get()`
- 条件付き依存: `if ( pendingSearchSetupTasks.get(extension.id) === searchStartupPromise )` → `pendingSearchSetupTasks.delete()`
- 条件付き依存: `if ( pendingSearchSetupTasks.get(extension.id) === searchStartupPromise )` → `ExtensionParent.apiManager.emit()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `pendingSearchSetupTasks.set()`
- 参照: `extension.id`, `manifest.chrome_settings_overrides.homepage`, `manifest.chrome_settings_overrides.search_provider`

## ensureSetting()
- 位置: async L307-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSettingsStore.getSetting()`, `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (!item)` → `SearchService.getDefault()`
- 条件付き依存: `if (!item)` → `ExtensionSettingsStore.addSetting()`
- 条件付き依存: `if (!item)` → `["ADDON_UPGRADE", "ADDON_DOWNGRADE", "ADDON_ENABLE"].includes()`
- 条件付き依存: `if (disable)` → `ExtensionSettingsStore.disable()`
- 参照: `defaultEngine.name`, `extension.id`, `extension.startupReason`

## promptDefaultSearch()
- 位置: async L346-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SearchService.getDefault()`, `SearchService.getEngineByName()`, `Services.obs.notifyObservers()`, `extension.getPreferredIcon()`, `this.ensureSetting()`
- 参照: `defaultEngine.name`, `engine.name`, `extension.id`, `extension.name`, `windowTracker.topWindow?.gBrowser.selectedBrowser`
- XPCOM: `Services.obs`

## respond()
- 位置: async L372-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (allow)` → `chrome_settings_overrides.processDefaultSearchSetting()`
- 条件付き依存: `if (allow)` → `SearchService.setDefault()`
- 条件付き依存: `if (allow)` → `SearchService.getEngineByName()`
- 参照: `SearchService.CHANGE_REASON.ADDON_INSTALL`, `extension.id`
- XPCOM: `Services.obs`

## processSearchProviderManifestEntry()
- 位置: async L394-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SearchService.maybeSetAndOverrideDefault()`, `searchProvider.name.trim()`, `this.addSearchEngine()`
- 条件付き依存: `if (!searchProvider.is_default)` → `this.addSearchEngine()`
- 条件付き依存: `if (!this.extension)` → `Cu.reportError()`
- 条件付き依存: `if (result.canChangeToConfigEngine)` → `this.setDefault()`
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `this.promptDefaultSearch()`
- 条件付き依存: `if (!(extension.startupReason === "ADDON_INSTALL"))` → `this.setDefault()`
- 参照: `SearchService.promiseInitialized`, `extension.startupReason`, `manifest.chrome_settings_overrides.search_provider`, `result.canChangeToConfigEngine`, `result.canInstallEngine`, `searchProvider.is_default`, `this.extension`

## setDefault()
- 位置: async L439-517
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `this.ensureSetting()`
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `SearchService.setDefault()`
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `SearchService.getEngineByName()`
- 条件付き依存: `if (!(extension.startupReason === "ADDON_INSTALL"))` → `["ADDON_UPGRADE", "ADDON_DOWNGRADE", "ADDON_ENABLE"].includes()`
- 条件付き依存: `if ( ["ADDON_UPGRADE", "ADDON_DOWNGRADE", "ADDON_ENABLE"].includes( extension.startupReason ) )` → `ExtensionSettingsStore.getLevelOfControl()`
- 条件付き依存: `if ( control === "controlled_by_this_extension" && SearchService.defaultEngine.name !== engineName )` → `ExtensionSettingsStore.getAllSettings()`
- 条件付き依存: `if (setting.value !== SearchService.defaultEngine.name)` → `ExtensionSettingsStore.disable()`
- 条件付き依存: `if ( control === "controlled_by_this_extension" && SearchService.defaultEngine.name !== engineName )` → `ExtensionSettingsStore.getLevelOfControl()`
- 条件付き依存: `if (control === "controlled_by_this_extension")` → `SearchService.setDefault()`
- 条件付き依存: `if (control === "controlled_by_this_extension")` → `SearchService.getEngineByName()`
- 条件付き依存: `if (skipEnablePrompt)` → `chrome_settings_overrides.processDefaultSearchSetting()`
- 条件付き依存: `if (skipEnablePrompt)` → `SearchService.setDefault()`
- 条件付き依存: `if (skipEnablePrompt)` → `SearchService.getEngineByName()`
- 条件付き依存: `if (extension.startupReason == "ADDON_ENABLE")` → `this.promptDefaultSearch()`
- 参照: `SearchService.CHANGE_REASON.ADDON_INSTALL`, `SearchService.defaultEngine.name`, `extension.id`, `extension.startupReason`, `item.value`, `setting.id`, `setting.value`

## addSearchEngine()
- 位置: async L519-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.reportError()`, `SearchService.addEngineFromExtension()`

## onPrefsChanged()
- 位置: async L542-561
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (item.id)` → `homepagePopup.addObserver()`
- 条件付き依存: `if (item.id)` → `ExtensionParent.WebExtensionPolicy.getByID()`
- 条件付き依存: `if (!policy)` → `ExtensionPermissions.get()`
- 条件付き依存: `if (!policy)` → `perms.permissions.includes()`
- 条件付き依存: `if (item.id)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(item.id))` → `homepagePopup.removeObserver()`
- 条件付き依存: `if (!(item.id))` → `Services.prefs.clearUserPref()`
- 参照: `item.id`, `policy.privateBrowsingAllowed`
- XPCOM: `Services.prefs`

## setCallback()
- 位置: L562-571
- 役割: (未記入)
- 触るとき: (未記入)
