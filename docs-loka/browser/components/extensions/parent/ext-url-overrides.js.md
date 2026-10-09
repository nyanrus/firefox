# browser/components/extensions/parent/ext-url-overrides.js

source: browser/components/extensions/parent/ext-url-overrides.js
source-hash: 5be610a63750e9444cca4a2005ecb9d09df220e8
lines: 206

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ExtensionParent.apiManager.on()`

## onObserverAdded()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AboutNewTab.willNotifyUser`

## onObserverRemoved()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AboutNewTab.willNotifyUser`

## beforeDisableAddon()
- 位置: async L43-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.obs.addObserver()`, `replaceUrlInTab()`
- 参照: `gBrowser.selectedTab`, `win.gBrowser`
- XPCOM: `Services.io` / `Services.obs`

## observe()
- 位置: async L55-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.obs.removeObserver()`, `popup.open()`, `replaceUrlInTab()`
- 参照: `AboutNewTab.newTabURL`
- XPCOM: `Services.io` / `Services.obs`

## setNewTabURL()
- 位置: L73-90
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (extensionId)` → `newTabPopup.addObserver()`
- 条件付き依存: `if (extensionId)` → `ExtensionParent.WebExtensionPolicy.getByID()`
- 条件付き依存: `if (extensionId)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(extensionId))` → `newTabPopup.removeObserver()`
- 条件付き依存: `if (!(extensionId))` → `Services.prefs.clearUserPref()`
- 参照: `AboutNewTab.newTabURL`, `policy.privateBrowsingAllowed`
- XPCOM: `Services.prefs`

## processSettings()
- 位置: async L112-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSettingsStore.hasSetting()`, `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (ExtensionSettingsStore.hasSetting(id, STORE_TYPE, NEW_TAB_SETTING_NAME))` → `ExtensionSettingsStore[action]()`

## onDisable()
- 位置: async L120-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `newTabPopup.clearConfirmation()`, `processSettings()`

## onEnabling()
- 位置: async L125-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `processSettings()`

## onUninstall()
- 位置: async L129-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `newTabPopup.clearConfirmation()`, `processSettings()`

## onUpdate()
- 位置: async L135-151
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !manifest.chrome_url_overrides || !manifest.chrome_url_overrides.newtab )` → `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if ( !manifest.chrome_url_overrides || !manifest.chrome_url_overrides.newtab )` → `ExtensionSettingsStore.hasSetting()`
- 条件付き依存: `if ( ExtensionSettingsStore.hasSetting(id, STORE_TYPE, NEW_TAB_SETTING_NAME) )` → `ExtensionSettingsStore.removeSetting()`
- 参照: `manifest.chrome_url_overrides`, `manifest.chrome_url_overrides.newtab`

## onManifestEntry()
- 位置: async L153-204
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `extension.baseURI.resolve()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `ExtensionSettingsStore.addSetting()`
- 条件付き依存: `if (item)` → `setNewTabURL()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `extension.on()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `permissions.permissions.includes()`
- 条件付き依存: `if ( permissions.permissions.includes("internal:privateBrowsingAllowed") )` → `ExtensionSettingsStore.getSetting()`
- 条件付き依存: `if (item && item.id == extension.id)` → `Services.prefs.setBoolPref()`
- 参照: `AboutNewTab.newTabURL`, `extension.id`, `item.id`, `item.initialValue`, `item.value`, `manifest.chrome_url_overrides.newtab`
- XPCOM: `Services.prefs`
